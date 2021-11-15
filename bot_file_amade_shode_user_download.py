# written by seyed mohamad mahdi moravej
# document can be exel,word,powerpoint,pythonmtext,not image
from telegram import update
from telegram.ext import *
from telegram import * 
token = "2076371567:AAF7xXQMPI86FpcFWZVgWzlK6jtWKb60DDw"
bot = Bot(token)
list_mechanical = ["36020104.xlsx","36020111.xlsx","36020115.xlsx","041.xlsx","042.xlsx",
                    "047.xlsx","048.xlsx","049.xlsx","051.xlsx","053.xlsx","36020503.xlsx",
                    "36020504.xlsx","36020505.xlsx","36020506.xlsx","36020507.xlsx"]
list_electrical = ["043.xlsx","044.xlsx","045.xlsx","046.xlsx","050.xlsx","052.xlsx"]
list_administrator = [
                    "36010101.xlsx","36010102.xlsx","36010103.xlsx","36010201.xlsx",
                    "36010501.xlsx","36010601.xlsx","36010602.xlsx","36010801.xlsx",
                    "36010802.xlsx","36020101.xlsx","36020109.xlsx","36020112.xlsx",
                    "36020114.xlsx","36020116.xlsx","36020602.xlsx","36020603.xlsx",
                    "36020604.xlsx","36020607.xlsx","36020901.xlsx","36020903.xlsx",
                    "36020904.xlsx","36020905.xlsx","36020906.xlsx","36020907.xlsx",
                    "36020909.xlsx","36020911.xlsx","360201106.xlsx","360201107.xlsx",
                    "360201108.xlsx"
                        ]
list_quality_control = ["36010704.xlsx","36010705.xlsx",
                        # "36010706.xlsx" ''' file isn't existed but should be exist'''
                        "36020401.xlsx","36020402.xlsx",
                        "36020403.xlsx","36020404.xlsx","36020406.xlsx","36020407.xlsx",
                        "36020408.xlsx","36020410.xlsx",
                        "36020601.xlsx",
                        # "36010708.xlsx",''' file isn't existed'''
                        # "36020703.xlsx",''' file isn't existed'''
                        "36020801.xlsx",
                        # "36020802.xlsx",''' file isn't existed'''
                        # "36032004.xlsx",''' file isn't existed'''
                        ]
list_water_without_income=["36021001.xlsx","360201105.xlsx"]

class MYBOT():
    def __init__(self):
        # choosing contractor
        keyboard_1 = [
                    [InlineKeyboardButton(
                    "آقای فتحی",
                    callback_data="fathi")],
                    [InlineKeyboardButton(
                    "آقای مهدوی",
                    callback_data="mahdavi")]
                    ]
        # choosing strategy :
        # 1:want to download empty desired document
        # 2:want to upload filled document
        # 3:want to fill desired document online
        # 4:want to edit last sended desired decument
        keyboard_2 = [
                    [InlineKeyboardButton(
                    "فرم مربوطه را ندارم و میخواهم با رهنمایی ربات دانلود کنم",
                    callback_data="download")],
                    [InlineKeyboardButton(
                    "فرم مربوطه را پر کرده و می خواهم به ربات بفرستم",
                    callback_data="upload")],
                    [InlineKeyboardButton(
                    "می خواهم آنلاین با کمک ربات فرم را پر کنم",
                    callback_data="fill_online")],
                    [InlineKeyboardButton(
                    "در گذشته فایل مشابه را فرستادم و می خواهم آن را ویرایش کنم",
                    callback_data="edit_previous_file")]
                    ]
        # choosing relevant office
        keyboard_3 = [
                    [InlineKeyboardButton(
                    "واحد فنی مکانیکی",
                    callback_data="download_mechanical")],
                    [InlineKeyboardButton(
                    "واحد فنی برقی",
                    callback_data="download_electrical")],
                    [InlineKeyboardButton(
                    "آبدار ،ضایعات گیر و سایر نیروهای مرتبط با سرپرست بخش",
                    callback_data="download_administrator")],
                    [InlineKeyboardButton(
                    "واحد دبی سنجی و آب بدون درآمد ",
                    callback_data="download_debi")],
                    [InlineKeyboardButton(
                    "کنترل کیفی",
                    callback_data="download_quality_control")]
                    ]             
        # chossing relevant mechanical file
        keyboard_4 = [
                    [InlineKeyboardButton(
                    "فرم بازدید و مانور شیرآلات کنترل دبی و فشار",
                    callback_data="36020104.xlsx")],
                    [InlineKeyboardButton(
                    "فرم بازدید و مانور شیرآلات فلوتری",
                    callback_data="36020111.xlsx")],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس عملگرهای برقی",
                    callback_data="36020115.xlsx")],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و بررسی عملکرد الکتروپمپ شناور",
                    callback_data="36020503.xlsx")],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و بررسی عملکرد جرثقیل سقفی",
                    callback_data="36020504.xlsx")],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و بررسی عملکرد کمپرسور هوا",
                    callback_data="36020505.xlsx")],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس عملکرد الکتروپمپ زمینی",
                    callback_data="36020506.xlsx")],
                    [InlineKeyboardButton(
                    "فرم ترموگرافی و ارتعاش‌سنجی الکتروپمپ",
                    callback_data="36020507.xlsx")],
                    [InlineKeyboardButton(
                    "چک لیست تابلوهای برق",
                    callback_data="041.xlsx")],
                    [InlineKeyboardButton(
                    "چک لیست تجهیزات ایستگاه پمپاژ",
                    callback_data="042.xlsx")],
                    [InlineKeyboardButton(
                    "فرم فعاليتهاي پيشگيرانه دیزل ژنراتور (در حالت سرد)",
                    callback_data="047.xlsx")],
                    [InlineKeyboardButton(
                    "جدول کارکرد دیزل ژنراتورها",
                    callback_data="048.xlsx")],
                    [InlineKeyboardButton(
                    "دستور العمل فعاليتهاي پيشگيرانه (در حالت سرد)",
                    callback_data="049.xlsx")],
                    [InlineKeyboardButton(
                    "چک لیست نظارتی عملیات ایرلیف (لایروبی) و احیاء",
                    callback_data="051.xlsx")],
                    [InlineKeyboardButton(
                    "چک لیست محاسبه راندمان",
                    callback_data="053.xlsx")]
                    ]
        # choosing relevant electrical file
        keyboard_5 = [
                    [InlineKeyboardButton(
                    "گزارش ماهانه قطعات مصرفی تاسیسات برق",
                    callback_data="043.xlsx")],
                    [InlineKeyboardButton(
                    "فرم فعالیت نصب و راه اندازی الکتروپمپ",
                    callback_data="044.xlsx")],
                    [InlineKeyboardButton(
                    "فرم گزارش روزانه تاسیسات برقی",
                    callback_data="045.xlsx")],
                    [InlineKeyboardButton(
                    "چک لیست مواد مصرفی الکتریکی",
                    callback_data="046.xlsx")],
                    [InlineKeyboardButton(
                    "چک لیست جمع آوری تجهیزات چاه",
                    callback_data="050.xlsx")],
                    [InlineKeyboardButton(
                    "نصب و راه اندازی الکتروپمپ شناور",
                    callback_data="052.xlsx")]
                    ]
        # choosing relevant administrator file
        keyboard_6 = [
                    [InlineKeyboardButton(
                    "فرم راهبری و اپراتوری چاه",
                    callback_data="36010101.xlsx")],
                    [InlineKeyboardButton(
                    "فرم راهبری و اپراتوری چشمه",
                    callback_data="36010102.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم راهبری و اپراتوری قنات",
                    callback_data="36010103.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم راهبری و اپراتوری تاسیسات و شیرآلات ایستگاه پمپاژ ",
                    callback_data="36010201.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم راهبری و اپراتوری خطوط انتقال آب / خط بان",
                    callback_data="36010501.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم راهبری و ثبت گزارش اپراتوری مخازن ذخیره آب و تاسیسات جانبی",
                    callback_data="36010601.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم راهبری و اپراتوری شبکه توزیع آب",
                    callback_data="36010602.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم انجام خدمات فضای سبز",
                    callback_data="36010801.xlsx")
                    ],
                    [InlineKeyboardButton(
                    #  negahban fiziki por kone
                    "حفاظت از تاسیسات آب شرب",
                    callback_data="36010802.xlsx")
                    ],
                    [InlineKeyboardButton(
                    #   shir haye shabake tozi va khate enteqal
                    "فرم بازدید و مانور شیرآلات",
                    callback_data="36020101.xlsx")
                    ],
                    [InlineKeyboardButton(
                    # dasture kari ba bakhsh ha karfarma mide
                    "فرم پیدا کردن شیرآلات ناپیدا به وسیله حفاری",
                    callback_data="36020109.xlsx")
                    ],
                    [InlineKeyboardButton(
                    # safi khate_enteql_va _shabake tozi
                    "فرم بازدید و سرویس صافی شیرآلات",
                    callback_data="36020112.xlsx")
                    ],
                    [InlineKeyboardButton(
                    # shabake tozi va khate enteqal
                    "فرم بازدید و مانور شیرآلات هوا",
                    callback_data="36020114.xlsx")
                    ],
                    [InlineKeyboardButton(
                    #   moredi
                    "فرم باز و بسته نمودن شیرآلات به منظور نوبت بندی",
                    callback_data="36020116.xlsx")
                    ],
                    [InlineKeyboardButton(
                    # dasture kari ba bakhsh ha karfarma mide
                    "فرم نظافت و نگهداشت برنامه‌ای محوطه تاسیسات آب محصور شده",
                    callback_data="36020602.xlsx")
                    ],   
                    [InlineKeyboardButton(
                    # dasture kari ba bakhsh ha karfarma mide
                    "فرم نظافت و نگهداشت حریم منابع آبی و مخازن غیرمحصور",
                    callback_data="36020603.xlsx")
                    ],     
                    [InlineKeyboardButton(
                    #rutin
                    "فرم نگهداشت برنامه‌ای ونظافت مستمر ساختمان‌های تاسیسات مکانیکی و برقی",
                    callback_data="36020604.xlsx")
                    ],                                                                                                                                                         
                    [InlineKeyboardButton(
                    # hozchehaye shabake tozi va khate enteqal
                    "فرم نگهداشت برنامه‌ای و نظافت حوضچه",
                    callback_data="36020607.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم شستشو و گندزدایی مخازن زمینی",
                    callback_data="36020901.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم شستشو و گندزدایی خطوط انتقال",
                    callback_data="36020903.xlsx")
                    ],
                    [InlineKeyboardButton(
                    #nadarim
                    "فرم شستشو و گندزدایی خطوط انتقال با آب و هوا",
                    callback_data="36020904.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم شستشو و گندزدایی شبکه توزیع",
                    callback_data="36020905.xlsx")
                    ],                                                                
                    [InlineKeyboardButton(
                    "فرم شستشو و گندزدایی مخازن هوایی",
                    callback_data="36020906.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم لایروبی مخازن ذخیره آب و حمل لای با هر نوع وسیله مکانیکی",
                    callback_data="36020907.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم شستشو تانکرهای آب رسانی",
                    callback_data="36020909.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم رسوب‌زدایی خطوط انتقال بدون دستگاه رسوب‌زدایی براساس دستورالعمل",
                    callback_data="36020911.xlsx")
                    ],
                    [InlineKeyboardButton(
                    # dasture kari ba bakhsh ha karfarma mide
                    "فرم مرئی‌سازی شیرآلات حوضچه",
                    callback_data="360201106.xlsx")
                    ],    
                    [InlineKeyboardButton(
                    # dasture kari ba bakhsh ha karfarma mide
                    "فرم هم‌سطح سازی حوضچه شیرآلات",
                    callback_data="360201107.xlsx")
                    ],
                    [InlineKeyboardButton(
                    # dasture kari ba bakhsh ha karfarma mide
                    "فرم پیدا کردن شیرآلات ناپیدا",
                    callback_data="360201108.xlsx")
                    ]
                    ]
        # choosing relevant measuring quality control
        keyboard_7 = [
                    [InlineKeyboardButton(
                    "کلرسنجی",
                    callback_data="36010704.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم راهبری دستگاه کلریناتور گازی همراه با کلرسنجی",
                    callback_data="36010705.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم راهبری و اپراتوری گندزدایی دستگاه آب ژاول به همراه کلرسنجی",
                    callback_data="36010706.xlsx")
                    ],
                    [InlineKeyboardButton(
                    #    moredi
                    "فرم نگهداشت برنامه‌ای و سرویس دستگاه کلریناتور محلولی برقی به طور مستمر",
                    callback_data="36020401.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس دستگاه کلریناتور محلولی به طور مستمر",
                    callback_data="36020402.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس دستگاه کلریناتور گازی به طور مستمر",
                    callback_data="36020403.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس الکترولیز نمک طعام به طور مستمر",
                    callback_data="36020404.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس سامانه ازن‌زنی به طور مستمر",
                    callback_data="36020406.xlsx")
                    ], 
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس سامانه خنثی‌کننده گاز کلر اسکرابر",
                    callback_data="36020407.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس سیستم تزریق آب ژاول",
                    # mohem
                    callback_data="36020408.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم نگهداشت برنامه‌ای و سرویس سیستم تزریق مواد شیمیایی",
                    callback_data="36020410.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم نظافت اتاق‌های کلریناتور و انبار کلر",
                    # mohem       
                    callback_data="36020601.xlsx")
                    ],
                    [InlineKeyboardButton(
                    "فرم نمونه‌برداری (میکروبیولوژی و باکتریولوژی) از شبکه توزیع آب، منابع و مخازن و تصفیه‌خانه‌ها",
                    callback_data="36020801.xlsx")
                    ]
                    ]
        # choosing relevant measuring debi and water without income file
        keyboard_8 = [
                     [InlineKeyboardButton(
                    "فرم دبی‌سنجی با دستگاه دبی‌سنج قابل حمل",
                    callback_data="36021001.xlsx")],
                    [InlineKeyboardButton(
                    "فرم قرائت و ثبت داده دستگاه اندازه‌گیری جریان",
                    callback_data="360201105.xlsx")
                    ]
                    ]  
        
        self.reply_mark_1 = InlineKeyboardMarkup(keyboard_1)
        self.reply_mark_2 = InlineKeyboardMarkup(keyboard_2)
        self.reply_mark_3 = InlineKeyboardMarkup(keyboard_3)
        self.reply_mark_4 = InlineKeyboardMarkup(keyboard_4)
        self.reply_mark_5 = InlineKeyboardMarkup(keyboard_5)
        self.reply_mark_6 = InlineKeyboardMarkup(keyboard_6)
        self.reply_mark_7 = InlineKeyboardMarkup(keyboard_7)
        self.reply_mark_8 = InlineKeyboardMarkup(keyboard_8)
        
    def start(self,update: Update, context: CallbackContext):
        bot.send_message(
            text="fddddddd",
            chat_id=update.message.chat_id,
            # reply_markup=self.reply_mark_1
            )
    def messagetoUs(self,update: Update, context: CallbackContext):
        if update.message.text=="1":
            print(update)
        # try:
            bot.send_message(
                chat_id=update.message.chat_id,
                text="لطفا نام پیمانکاری که برنده ی قرارداد شدند را انتخاب کنید",
                reply_markup=self.reply_mark_1
                )
        # except Exception as e:
        #     pass

    def query_btns(self,update: Update, context: CallbackContext):
        query = update.callback_query
        # choose fathi
        if query.data == "fathi":
            bot.send_message(
                chat_id=update.effective_message.chat_id,
                text="لطفا را ه تعامل با ربات را انتخاب کنید",
                reply_markup=self.reply_mark_2
                )
        # choose want to download file
        if query.data == "download":
            bot.send_message(
                chat_id=update.effective_message.chat_id,
                text="لطفا بخش کاری خود را انتخاب کنید",
                reply_markup=self.reply_mark_3 
                )
              # choose want to download_file for electrical
        if query.data == "download_mechanical":
            bot.send_message(
                chat_id=update.effective_message.chat_id,
                reply_markup=self.reply_mark_4,
                text="لطفا فرم مورد نظر خود را انتخاب کنید",
                )
        # choose want to download_file for electrical
        if query.data == "download_electrical":
            bot.send_message(
                chat_id=update.effective_message.chat_id,
                reply_markup=self.reply_mark_5,
                text="لطفا فرم مورد نظر خود را انتخاب کنید",
                )
        # choose want to download_file for administrator
        if query.data == "download_administrator":
            bot.send_message(
                chat_id=update.effective_message.chat_id,
                text="لطفا فرم مورد نظر خود را انتخاب کنید",
                reply_markup=self.reply_mark_6
                )
            # choose want to download_file for measuring debi and water without income file
        if query.data == "download_quality_control":
            bot.send_message(
                chat_id=update.effective_message.chat_id,
                text="لطفا فرم مورد نظر خود را انتخاب کنید",
                reply_markup=self.reply_mark_8
                )
            
        # choose want to download_file for mechanical_choose file
        elif query.data in list_mechanical:      
            with open("../mechanical/"+query.data, "rb") as file:
                context.bot.send_document(
                    chat_id=update.effective_message.chat_id,
                    document=file,
                    filename=query.data
                    )
        elif query.data in list_electrical:      
            with open("../electrical/"+query.data, "rb") as file:
                context.bot.send_document(
                    chat_id=update.effective_message.chat_id,
                    document=file,
                    filename=query.data
                    )
        elif query.data in list_administrator:      
            with open("../administrator/"+query.data, "rb") as file:
                context.bot.send_document(
                    chat_id=update.effective_message.chat_id,
                    document=file,
                    filename=query.data
                    )
        elif query.data in list_quality_control:      
            with open("../quality_control/"+query.data, "rb") as file:
                context.bot.send_document(
                    chat_id=update.effective_message.chat_id,
                    document=file,
                    filename=query.data
                    )
        elif query.data in list_water_without_income:      
            with open("../water_without_income/"+query.data, "rb") as file:
                context.bot.send_document(
                    chat_id=update.effective_message.chat_id,
                    document=file,
                    filename=query.data
                    )


    def downloader(self,update: Update, context: CallbackContext):   
        context.bot.getFile(update.message.document).download("154545.xlsx")
    def main(self):
        updater = Updater(token,use_context=True)
        updater.dispatcher.add_handler(CommandHandler("start",self.start))
        updater.dispatcher.add_handler(MessageHandler(Filters.all, self.messagetoUs))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.query_btns))
        updater.start_polling()
        updater.idle()
class mybot():
    def __init__(self):
        pass
    def downloader(self,update: Update, context: CallbackContext):   
        context.bot.get_file(update.message.document).download()
    def main(self):
        updater = Updater(token,use_context=True)
        updater.dispatcher.add_handler(MessageHandler(Filters.document, self.downloader))
        updater.start_polling()
        updater.idle()
# mybot().main()    
MYBOT().main()

