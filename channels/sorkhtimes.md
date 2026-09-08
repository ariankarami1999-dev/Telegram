<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/ceML0zhtlD_dDClh53uFW7cgMw6-_RudnrZLzcInUCmVt9F_tNUuuqkHlyntAD5mOpn5it87DxDuT4xQC-Dyyf_U7_L0g1LjZemaM-r-UEqZKNOgB3-fESs8wXk0M_QXzbrCRufJPvPk7dZ6319wVb5MAVp2t-OUSkrnvCQCy7KMg8yozWvQ00Tq1tpexL3EBdYHBcPuUg4c0Zcq_D3BDQa-J6Nn09TwBrAFcl7wPRHQD0BdGf9vfb7wsYNOSV6USJVH7Bvp-Ow6831c7kT3ssV3hGTerkvhIo0swPSfpOF5EzOrulCPMS_x1-kwhFAYyOUpO-VShDG5ck2hmZe1Ww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 17:38:33</div>
<hr>

<div class="tg-post" id="msg-139764">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NW3dFyQyAbXHBwO-xfRtCDHADmO_6OfzfddizJwNXZ8nDfDfy6CmP3it2OrbEoO0qL1QAbzm7-baiqrbAIrrqc0wHMcJ5FpC3aHDPqx-x6UwTYEqAr-lMpQSpCc14li2ZZ9dK024FsWSnCmZYHCcpHyoDqv8MrJHPtfa4vHWbKA4UMtTZvOUrvtUaTE7rW5abnruNG5rPM693Xy88JdfXctbczqHY-BW_mTMvTuZtTQ-j3wASao8pFjdjMhzn5Vga5qP1vcbv5l2-j03wpXFRUie2Y09WuoUo-G-N6SpO7SsEyiAPkOOxP-aoGQepaVMkcKJjlDebi0A6QK8V27-IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
تسنیم: پرسپولیس بیش از حد به بیفوما وابسته شده؛ بدون او سرخ‌ها توانایی خلق موقعیت ندارند!
✔️
نظر شما چیه؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/SorkhTimes/139764" target="_blank">📅 15:49 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139763">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PSYwfbacAhj1KNuOvJGcMOp4h3NDSbgFZfPNFcOBhdU1vWDBxUnVAfuajONriGjgoHz7q5Xuu7vY1l9L9oJuNqD9V3PR-2o5858HxKxzu2agt1fKty-oLtgJaF5mjF-Bb2b_E76Are5d_FQLcnl-n7MUsoCHIDy-pYHxfXnIirTuejhtmTd0bHRm0HRsryA0EaLuOhdcZv6p2I71eKlyILWcDeZfRPVpJnVAwe3VsKMYVhsTokW_lkftTTMR6edH3qNNo0MUqCYzcB5BbYcm-5reAhI2EuR0Rcx-6pwIrPW0aRurrkXvdg2KsPBWf-uGAUI2L0VeZCT7EguI2Jsomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
🗣
شهرآبادی، ایری و لطیفی‌فر به دلیل حضور در اردوی تیم ملی امید، بازی با خیبر را از دست دادند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/SorkhTimes/139763" target="_blank">📅 15:48 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139761">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7ifI-G8Q74PuxLVi6ui4YM0oc_r5tueM_8CqbuFvW_ABdYgqbxhcUZWjcb82VrasXdGKAoO9gaXkm2ES366EPsdzzTVwYFlP3CewAQM98vtDbKqC4aDvrmR18qBwpo75M4F6GRSHr8eA4aTBNnpQl1NXLDJIfym4_g3LIUpjvcA9MnS3rA0ETyORn4H32E3Z6JLmBzoYCkZeLRQN7Qk3hd8oI_bC1doG94_rtmPLJ2W2rNZzwKa9k3fPlii7tK0hpVjSFT05l0YVxzQobCmjw3t9sgsqiC4GsE31k_BeS3ZPT9DgrL7ZIpUvA8_JzkF98chVKrwaHSV7lFGvNIOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🔴
میرور: فوتبال سرژ اوریه به پایین ترین سطح کریرش رسیده و می‌خواد در لیگ دسته هفتم فرانسه در تیم محلاتی مونتینی-آن-گوئله بازی کنه و انتقال اوریه به دلیل تاخیر در ارائه مدارک از سوی فدراسیون فوتبال ایران به تعویق افتاده است!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/SorkhTimes/139761" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139760">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SorkhTimes/139760" target="_blank">📅 14:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139759">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/139759" target="_blank">📅 13:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139758">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">❤️
❤️
بیفوما که به تیم ملی کنگو دعوت شده بود دعوتو رد کرده و گفته تیم ملی من پرسپولیسه و به تیم ملی نمی‌رم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/139758" target="_blank">📅 13:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139757">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">✔️
✔️
پرسپولیس امروز در بازی تدارکاتی به مصاف تیم  پارس جنوبی جم می‌رود تا به بازیکن هایی که دیشب کمتر بازی کردند یا اصلا بهشون فرصت نرسیده، بازی بدهد.  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SorkhTimes/139757" target="_blank">📅 13:19 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139756">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lYoE00NnSMeypw5Le8Ph1DZxS4WH2HelkBiriLKH35QNzMRCCUKeLArwSh5wuRk2NsYxAqM_wjV3czGkROQ5hD4s1dNhcdG4RI8unbVqn-wW1WM1l1AI7fkgqw0fGD-zvLSpt7X7k7u9F4XFMJwXnVQU6IVJu-fuN_AqZ74WfZARQOCOeETE2M3jf7-QN6FNtvQDOrvGQtdSOVX6H5i283R3MIOT7IzbAy2vfLnnhKjwoGmso6x3WDitxlae7yRQDeMvgH_CJT4iHIR-W7UjUoiyO65jGbcUqP8vJoJd3X865d6xvgmvwZ7cBtYACsF3ytIHFFAjNKoXO2IRuu9KoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رئال و اینتر؛ دو غول، برای یک شب بزرگ
⚽️
رئال با تجربه و کیفیت فردی بالاتر، اما اینتر با دفاع منسجم و ضدحملات خطرناک؛ دوئلی که می‌تواند تا آخرین دقیقه نزدیک بماند.
[
رئال‌مادرید
⚪️
🆚
🔵
اینترمیلان
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SorkhTimes/139756" target="_blank">📅 12:10 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139755">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❤️
❤️
تارتار از امیر حسین محمودی خیلی راضیه و احتمالا مقابل خیبر زمان بیشتری بازی کنه//ورزش سه   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/139755" target="_blank">📅 12:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139754">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SorkhTimes/139754" target="_blank">📅 11:58 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139753">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
محسن خلیلی مدیر پرسپولیس: ۸۰۰ میلیارد بودجه لازم تا ورزشگاه آزادی تا چند ماه آینده آماه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/139753" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139752">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFMrex2tsYwBXLhz3wyHKdkF7Qe4rKGfV9U1iv4DuskqhXQFT9Vi7nPBqCd7bH7rnkpkwIeCIRHCqYw-zFnjtItpDFeaW4DWZBU51idHMjUMaGM6xGAJyqQB03S9i5mUElHAGMQZpIVbEG4QCpOorFzym7T3xZkwzpFj3GsUrDqQDFMZwz2A7RzVTr8iumJ8brm2WXn0l58eXpsmnsSxqOjHjMZS30Ix50rwGIbA_W6EodUHFhh9QI_A7pomxBJ85JnveWrJ_uoyQ4u9QDAQuF_LWocPkJBA5oi79iz7c21H6_2I78EfHTa8_Cd8db75XXrwRCAuYgvBb8iuDUZkaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
ایری در پاسخ به یک هوادار: تا روزی که جبران نکنم، شرمنده شما هستم.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/139752" target="_blank">📅 11:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139751">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/SorkhTimes/139751" target="_blank">📅 09:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139750">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SorkhTimes/139750" target="_blank">📅 09:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139749">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G4Ux_dibkyTlKcRoWdNDsnKcDv8c4P-PZvbDfqev15Npkb7FWljod3TqWQQzbQQ_SInNFUgeDukHSdec2z43pb_Jf9ejm9MVuX53MMPAFITAvFdBE1PDJjG6CbMyqjvugD1l5b85-S2MEGYPwmVaVESEmca1_gbJibrGHwARWiaHZXl5cWMBSotUtH-sUBTR5rZZzzodxuyw_H92mz-9JzKoKbhIAc6ZwrPOByZj0ff5TUfrytJO_zFLIEFGAQnq3zAtruSTZuNq6GqyVmn3O0GkAcGP0espDIAN9qcE4HEVV0uNDrP3T0H39HkXQiB6so0TdRmf6Ezm6atLhYQKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
امید عالیشاه: بر اساس چه مدرکی من رو محروم کردید؟ من فحشی ندادم و چیزی نگفتم! اصلا در رختکن تیم ما بسته بود از کجا تشخیص دادید من بودم که منو محروم کنید؟
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139749" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139748">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">❤️
❤️
❤️
صبحی که تیم برده و اومدیم دوم جدول و تیمهای دیگه تو حاشیه هستند و پرسپولیس تو آرامش بخیر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/139748" target="_blank">📅 09:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139747">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESoSKoqMlmhffZ2qMOrrv91rZ0fqr_PMNkNiQy7TrsII82Gc7nCkQjIYs6GAWDz7Utt7cpVkidvEVjzCa5agA3UIzQILNmzX8WyiTCrBF6IdT7yFAtX9C8F66IqRH5ObtHogSY3Nx6ztgfJNbrqJCOasv_eOedRtrye6oIp8nV6POV_GPeO4tAZD5e4grU4pKzdK7KjgTIP21Dvi-xeZSN648CMhpmimqPQ2Bd53UmnCcC6IBJsNtfK00o4ulsy-_UA8ZqwhLXW5CG5QcOLa840yox6vA9in9DlvU9uGgmuD9y738Adh-G8DG_5G_q7N2tHbhhLY4ESaPYDBzveboA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
جدال جذاب در یواس اوپن
🔥
[
الکساندر زورف
🆚
لوسیانو داردری
]
⏰
بامداد سه‌شنبه ساعت
۰۳:۴۰
🎾
زورف با سرویس قدرتمند و تجربه بیشتر، شانس اول پیروزی است.
داردری با سبک جنگنده خود اگر ریتم بگیرد، می‌تواند زورف را به دردسر بیندازد.
با این حال، روی هاردکورت کفه ترازو همچنان به سود زورف است.
🔗
برای پیش‌بینی این دیدار همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139747" target="_blank">📅 01:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139746">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">✔️
✔️
✔️
پیراهن پرسپولیس را بپوشید و به تیم ملی برگردید
✔️
در دو سال اخیر گولسیانی ، گندوز ، باکیچ و بیفوما از پرسپولیس به تیم های ملی خود راه یافتند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/SorkhTimes/139746" target="_blank">📅 01:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139745">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SorkhTimes/139745" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139744">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139744" target="_blank">📅 01:03 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139743">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=JC3z-OWFwF5_g_grZU-j9WLksGEEf72ynGCLtxpz6LpnQnpJJK8muzBjfKDfNTIMmkkxgW31mBIgiamWrfmZRL0vnWzyKBRLzynfxYIUPsl54hp06DKROwg_GU6LjdbKNYHsqjlDMpM_nvd1meiUADqFpQw16X10lNN3MwaELuM9QpbCwv2lpJM9VemVQjUFam5IV6k3rCOa_YaETbMUrF5-jjKA61n6oyHf5R91CGZ4TOmaff-mMs3NHjXK1sGYDmdHpmy27a71BUwJaPWEAt1pkDJ2QE01FUEhe7-Mx8akffseT3SPrQKyXXESsRInx-Ffi7kRD_RhxmNFRvUGOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ae53c901.mp4?token=JC3z-OWFwF5_g_grZU-j9WLksGEEf72ynGCLtxpz6LpnQnpJJK8muzBjfKDfNTIMmkkxgW31mBIgiamWrfmZRL0vnWzyKBRLzynfxYIUPsl54hp06DKROwg_GU6LjdbKNYHsqjlDMpM_nvd1meiUADqFpQw16X10lNN3MwaELuM9QpbCwv2lpJM9VemVQjUFam5IV6k3rCOa_YaETbMUrF5-jjKA61n6oyHf5R91CGZ4TOmaff-mMs3NHjXK1sGYDmdHpmy27a71BUwJaPWEAt1pkDJ2QE01FUEhe7-Mx8akffseT3SPrQKyXXESsRInx-Ffi7kRD_RhxmNFRvUGOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🗣
حجت موتوری مدیرعامل ترتر: به شجاع خلیل زاده و علیرضا بیرانوند در بازی با چادرملو فحش ناموس دادند، آیا این درست است؟
😂
😂
😂
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139743" target="_blank">📅 00:25 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139742">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=awt2_GhO1nGZcqI4FlfZJLrPu_xzFFgKSJNrx5hexbShcX5aHE2PFtI_lr62HKgcSirAts-HroD7RyQmxLxIXR_aL8C4w9z0sqGc1g2heR5bd1rrBmssMgQjeO15b7N_6Mi_y_e1XsFbM2O0u5h1vo8buxl4ixX5kF6s2X0IwN2Da5I7wJn4Z_9UkWwfF1Qf7q4uRPHJgGAuJoVEXFlYHXq69ZWk2GFvLU92b8VfyGz0eKDn_48N0PRJDPDZMA_QhevySRaCbXVhl8Ku866ntWTWJCn6MV_HYlPTO3E6f0qO5pcReIlph-dx-qyCtJEmOpz2KYtPX2tudYIfD13Low" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afa88055fa.mp4?token=awt2_GhO1nGZcqI4FlfZJLrPu_xzFFgKSJNrx5hexbShcX5aHE2PFtI_lr62HKgcSirAts-HroD7RyQmxLxIXR_aL8C4w9z0sqGc1g2heR5bd1rrBmssMgQjeO15b7N_6Mi_y_e1XsFbM2O0u5h1vo8buxl4ixX5kF6s2X0IwN2Da5I7wJn4Z_9UkWwfF1Qf7q4uRPHJgGAuJoVEXFlYHXq69ZWk2GFvLU92b8VfyGz0eKDn_48N0PRJDPDZMA_QhevySRaCbXVhl8Ku866ntWTWJCn6MV_HYlPTO3E6f0qO5pcReIlph-dx-qyCtJEmOpz2KYtPX2tudYIfD13Low" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
حجت موتوری: ویس های فحاشی خداداد را دوستان اول دادند به شبکه های معاند، اول آنها پخش کردند
🤣
🤣
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139742" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139741">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SorkhTimes/139741" target="_blank">📅 00:24 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139740">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SorkhTimes/139740" target="_blank">📅 00:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139739">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=kTAoUCawBQQQ24rx_omms7aWLrw48MyQfgRmLDP4RcN9e0T5tTyYybG66b9w6bWfyZC1YlvAceX7C5bhzlvf0CF61zRQQjCdiRTDlyHmNZwtPvlbzyeoZjeiGyE-di1Ce6xeoqNG19R5_5w376hM-KUIbzIxy2NCt9aUyEOw2GmYiXCkxeBliOU3PTgu82_kFJvzP6QrjnA0SJlKeH6RjG8OnB8DwpblPC5LEadS73JmsoQtO_0SPGES63f3WfK97Yb64xPm_9LahHFj5XEgR0TLtD3g0CyjgFEjUWjfVVzSG_i9ZBMacuLMjUw6TVk9GO-794CtDKGynahmJlJ4tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61b0cebd97.mp4?token=kTAoUCawBQQQ24rx_omms7aWLrw48MyQfgRmLDP4RcN9e0T5tTyYybG66b9w6bWfyZC1YlvAceX7C5bhzlvf0CF61zRQQjCdiRTDlyHmNZwtPvlbzyeoZjeiGyE-di1Ce6xeoqNG19R5_5w376hM-KUIbzIxy2NCt9aUyEOw2GmYiXCkxeBliOU3PTgu82_kFJvzP6QrjnA0SJlKeH6RjG8OnB8DwpblPC5LEadS73JmsoQtO_0SPGES63f3WfK97Yb64xPm_9LahHFj5XEgR0TLtD3g0CyjgFEjUWjfVVzSG_i9ZBMacuLMjUw6TVk9GO-794CtDKGynahmJlJ4tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙️
فرشید اسماعیلی:
✅
کابل VAR را کشیدند چون عجله داشتند که زودتر بروند؛ در گوشی به داور گفتند که پنالتی شده اما داور گفت من سوت پایان را زدم!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139739" target="_blank">📅 23:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139738">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">✔️
✔️
تارتار سرمربی پرسولیس: هوادار دوست دارد تیمش هجومی بازی کند/ قبلا هم گفتم اینجا پرسپولیس است و هواداران بازی زیبا و هجومی را دوست دارند
✔️
✔️
واقعا یک تیم کامل داریم و بازیکنان دارند روز به روز بهتر می شوند  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139738" target="_blank">📅 23:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139737">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">❤️
❤️
❤️
خداداد در طول این ۴ ماه حق ورود به هیچ کدوم از ورزشگاه‌های کشور رو نداره
🤣
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SorkhTimes/139737" target="_blank">📅 23:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139736">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SorkhTimes/139736" target="_blank">📅 23:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139735">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔻
🎙
⚽
🇮🇷
عادل فردوسی‌پور: وقتی به پرونده حواشی دیدار تراکتور-گل‌گهر نگاه میکنم آدم عارش میاد بگه به فوتبال علاقه‌منده! این‌قدر از ترسشان برخورد نکردند که کار به این‌جا کشیده!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SorkhTimes/139735" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139734">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🚩سرخ تایمز🚩</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lo4bOFhr1wt0zfGV3fJdr13S2PZQcsxdP_O5LRwZii1i8U0cfz-Dnm-0mGk7pjvoNlzJymWFIhCKTAJdbUJbrsnnxbJNJ7hw8EXEw1EgdPCgFUivbP84mf7NC_fJDJGR9RhpEwnZOtrsHVR_d04JopVkNEHXMxfHyJ5Cws_3ScM4VkJNcHPCHVoXs20QSzKx2i8EpDNSBpbVvInq2EKSM3b0wbNngffv3Dw_xSNFWFIyYdcUx6RypFN3dqoFkbToCfSyKyoyT0U17Yc_SGaYHUZO16CN3pgaiXRB3dAwzpN2Cv3DsdOOMh_4Tc13-55kImESxUhgC0WJV9mm1tCl1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 1.5K · <a href="https://t.me/SorkhTimes/139734" target="_blank">📅 22:54 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139733">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Witn9M5Grg8AUeL4qttsx0tZpNiNjgfLLE6IoeDfmVVblVtonnlGGhuYpYbKBuDygsvmOuJ6Hi0vu3u4hejTk-D3l3Dl3rW4pDsl9oCdNJzMFn0yK3GPwDklBxOjErBnuLZZ8jQl2GB9yVA6kzz57yB0kVERYqNnoCgzaAwqDkVtbsNnOnxzibUr5YrOFd9_F9KWXT8gFPgmgf1qcZYI3kZL9qvHyiWSvNM43Ti0efyMMflaVwADtxgKzFhiV5EyFXeSz5Ybsp-jRkTo1jx-9R1NTUKqAUNgXaQZ7qv4aUfqh6EtvC1aGIsoTfmF5cWIKLsnyfwA6G4d5eZlANLw5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
نتایج هفته ششم و جدول لیگ برتر
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139733" target="_blank">📅 22:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139732">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">✔️
✔️
محسن خلیلی: ما پیگیر شکایت از یاسر آسانی هستیم و برای اینکه پرونده را به دادگاه CAS ببریم ابتدا باید در کمیته انضباطی شکایت کنیم و جواب بگیریم بعد به CAS ببریم
✔️
بعضی ها می گفتند ما اورونوف را بازی نمی دهیم که او را  بفروشیم/ واقعا خنده دار است چرا باید…</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SorkhTimes/139732" target="_blank">📅 22:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139731">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">✔️
✔️
علی علیپور : به هواداران عزیزمون این برد رو تبریک میگم و گلم رو به علی آقای پروین تقدیم میکنم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139731" target="_blank">📅 22:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139730">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">❌
❌
کنعانی زادگان: تارتار تیم خیلی خوبی بسته است و امیدوارم آخر فصل قهرمان شویم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/SorkhTimes/139730" target="_blank">📅 22:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139729">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SorkhTimes/139729" target="_blank">📅 22:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139728">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">✔️
✔️
تارتار: فشارها علیه پرسپولیس؟ هواداران ما امسال اتحاد خوبی دارند و تا زمانی که این اتحاد باشد ما آسیب نمی‌بینیم
✔️
✔️
کری‌خوانی نماینده‌های تبریز؟ فوتبال از سیاست جدا هست و درباره فوتبال، فوتبالی‌ها باید نظر بدهند.  «سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/139728" target="_blank">📅 21:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139727">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">❌
❌
تارتار: در روزی که خوب نبودیم بردیم
❌
❌
سرمربی پرسپولیس در روزی که خیلی خوب نبودیم اما بازی را با پیروزی پشت سرگذاشتیم/ چمن ورزشگاه شهر قدس خیلی خوب نبود امیدوارم این چمن را درست کنند چون امروز واقعا خوب نبود
❌
❌
واقعا جای سوال دارد که چرا کیفیت چمن افت کرده…</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139727" target="_blank">📅 21:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139726">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">❌
کنایه حدادی به خداداد عزیزی : در این خصوص نمی توانم حرف بزنم اما فقط به آقای خلیلی جنگجوی و با ادب خودمان خسته نباشید می گویم. این نتایجی که می گیریم او هم تاثیر گذار است و در کنار خط در نهایت ادب با جنگندگی حق تیم را پیگیری می کند
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/139726" target="_blank">📅 21:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139725">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">✔️
✔️
مهدی تارتار: دنیل گرا با باشگاه قرارداد داره و  بازیکن ماست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/SorkhTimes/139725" target="_blank">📅 21:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139723">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
🤩
دکتر پیمان حدادی، مدیرعامل پرسپولیس:
❌
امیدواریم روند پیروزی‌ها ادامه‌دار باشد. طبیعی است که از بزرگ‌ترین و پرافتخارترین تیم ایران، انتظارات بالایی وجود داشته باشد.
❌
با توجه به مستنداتی که در اختیار داریم، درخصوص پرونده آسانی از باشگاه استقلال شکایت کرده‌ایم و در صورت حاصل نشدن نتیجه، حتما پیگیری‌های خود برای احقاق حق باشگاه را از طریق دادگاه CAS ادامه خواهیم داد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139723" target="_blank">📅 21:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139722">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/139722" target="_blank">📅 21:34 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139721">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=tmtha8UEn_DUUmwaKxmyHpo6E_y07lPVIDvl2164X2wXySiU3-PSnoSyKKVT6NIPlCC8b_YEXErNj4cxj-Q9eSUcW8c3HKAXrg6vAhzqjAmNYp0gtL5G7yPUVAazhxfzul1t6WGlALhIv-biwRPvsKCfOmK_67lj0w9tE5gGiF16hzdXZX4Hag_G5EXEuVnl0fPYvWlDS4lM89yt1-JbYyiqCYfKAd-NMjm4kLOLxB-8RTBv3bZC6MLzbKHpMEtFIznUBL5DhoxAAfPTe1SZsqRLSyVNf8Nexe-1e6lh7gVbugxiYQgc-r9zT3UZy5XXnXTILgrSNxfq_UTL04qF3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7963e99b5d.mp4?token=tmtha8UEn_DUUmwaKxmyHpo6E_y07lPVIDvl2164X2wXySiU3-PSnoSyKKVT6NIPlCC8b_YEXErNj4cxj-Q9eSUcW8c3HKAXrg6vAhzqjAmNYp0gtL5G7yPUVAazhxfzul1t6WGlALhIv-biwRPvsKCfOmK_67lj0w9tE5gGiF16hzdXZX4Hag_G5EXEuVnl0fPYvWlDS4lM89yt1-JbYyiqCYfKAd-NMjm4kLOLxB-8RTBv3bZC6MLzbKHpMEtFIznUBL5DhoxAAfPTe1SZsqRLSyVNf8Nexe-1e6lh7gVbugxiYQgc-r9zT3UZy5XXnXTILgrSNxfq_UTL04qF3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
واکنش جالب هوادار تیم به عملکرد پرسپولیس: بارسلونا هم بیاید در این زمین شکستش می دهیم؛ 2 تا به بارسا گل میزنیم 3 تا به رئال!
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/SorkhTimes/139721" target="_blank">📅 21:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139720">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=JZqBGRlMPiQ78qpteFaAzVaMMoib6CJ79Gv1mai0_QX-A2O4Uqe1j26JNXtiLQSs2Lb8gLW2-LPQdEtvUFkFDiF6vOdadp11Aj__z9zVpMrHuELGqV0Ny8QjLUi7ZP_lc6lQgW_bTPjiBprDuCe5yw_xVArLKAtTe0Bvn1-lpB1-RqH7kO0xUQLOz8Qg-cx2svo1Xm9s9sG-VLmLE2FiGBmqt04BHCScoTLL9NwgSabqYI-rvscqA-XB7a6pIpq9dgtBcMlykJzgcDWc3LUCZpfL9wGsccSouChXChB9YvGyP2MM-YuwbEcNMf2ULQbu72R88uZxQjSoirG_XxoIvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/809956e0a8.mp4?token=JZqBGRlMPiQ78qpteFaAzVaMMoib6CJ79Gv1mai0_QX-A2O4Uqe1j26JNXtiLQSs2Lb8gLW2-LPQdEtvUFkFDiF6vOdadp11Aj__z9zVpMrHuELGqV0Ny8QjLUi7ZP_lc6lQgW_bTPjiBprDuCe5yw_xVArLKAtTe0Bvn1-lpB1-RqH7kO0xUQLOz8Qg-cx2svo1Xm9s9sG-VLmLE2FiGBmqt04BHCScoTLL9NwgSabqYI-rvscqA-XB7a6pIpq9dgtBcMlykJzgcDWc3LUCZpfL9wGsccSouChXChB9YvGyP2MM-YuwbEcNMf2ULQbu72R88uZxQjSoirG_XxoIvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شادی بازیکنان پرسپولیس با هواداران پس از پیروزی برابر ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139720" target="_blank">📅 21:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139719">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kusqvsmOKzb-DnKzJF9obfVndTsZzFIGzp3ZL8c01Un5qVh93gkAF84dk6pYuHrAHyfvFuSRzKs29G4lZcfiE2XlpvxarjdIpMFP0vVQkRJ0euki5C3X1pS_OL-gr08f4XMm0KT8DxrOyzpauSJNqceEMgWQBZ_e7lXY6soAFgtMcUKYAWCKFi0FCfPq3Iq7UKuCsy8lVQFnNCYB9IzDqLXRvdRwKlCLxf9b5CsIhnjX5gWFOCFKrTWLOQdD4jYSDfekTG0kr0sZMpvOk2iLxwsXa0d3btfjo2aJixbRQVre7Z5oqUYWNzWGB4HHd09lIszsAr1HE6pYUJpU_teOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✔️
علیپور تاثیرگذارترین بازیکن کل لیگ تا هفته ششم
✔️
6 بازی، 3 گل، 3 پاس گل
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/SorkhTimes/139719" target="_blank">📅 21:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139718">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/139718" target="_blank">📅 21:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139717">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=SvuOoXd0O2U6VyOv5o3pTxwPMknsQlMhdjBJolTOmj1HeJ9p0kHfftGnoexfB1A3_t7DacKv7dDdXGR3U2OplMWiXRspqqDIFMJQ8qwwHh_KD5gWv36tenf-Fb0ryCVbz1pLa2SxX4hXFWG4-xVOCUe52TQLysTrcosrXVsKyOEcl78Cx54Rmkout9itXGB7Ro4Pq4mlfKKR_H3v9b3ooD7eP-w2WrjKuET6FXALoajvGtu5kRjyfn2sx9yX44iVMm_PRqes2JMEPe4RXbznRI6--rdn-Cl0e1-z4v-WdkuM8knpPnJG1_pVfyrkCNeDPsAY0WuKHg4xpHPxU7n1EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656ef71eba.mp4?token=SvuOoXd0O2U6VyOv5o3pTxwPMknsQlMhdjBJolTOmj1HeJ9p0kHfftGnoexfB1A3_t7DacKv7dDdXGR3U2OplMWiXRspqqDIFMJQ8qwwHh_KD5gWv36tenf-Fb0ryCVbz1pLa2SxX4hXFWG4-xVOCUe52TQLysTrcosrXVsKyOEcl78Cx54Rmkout9itXGB7Ro4Pq4mlfKKR_H3v9b3ooD7eP-w2WrjKuET6FXALoajvGtu5kRjyfn2sx9yX44iVMm_PRqes2JMEPe4RXbznRI6--rdn-Cl0e1-z4v-WdkuM8knpPnJG1_pVfyrkCNeDPsAY0WuKHg4xpHPxU7n1EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
گل دوم پرسپولیس به ذوب آهن توسط پوریا شهرآبادی روی پاس گل علی علیپور
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/SorkhTimes/139717" target="_blank">📅 20:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139716">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139716" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139715">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">❌
❌
باز هم تعویض تارتار جواب داد ..گل دوم و شهر آبادی زد   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SorkhTimes/139715" target="_blank">📅 20:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139714">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
گل اول و توسط علیپور زدیم با اینکه نیمه اول خوب نبودیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SorkhTimes/139714" target="_blank">📅 20:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139713">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139713" target="_blank">📅 20:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139712">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
اعلام رای تراکتور و گل گهر؛
🚨
خداداد عزیزی ۴ ماه و امید عالیشاه ۴ جلسه محروم شد!  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/139712" target="_blank">📅 20:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139711">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/SorkhTimes/139711" target="_blank">📅 20:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139709">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
این بازی و بچه ها با سه امتیاز بازی و ترک کنن برای بازی بعدی بعد از مدت ها یک هفته تایم و استراحت داریم ...و بازی بعدی یکشنبه هفته بعدی با خیبره  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SorkhTimes/139709" target="_blank">📅 20:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139708">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">✔️
✔️
تیم خسته اس ..ساق بچه ها خستگی داره ..امیدوارم نیمه دوم با آوردن صادقی و بیفوما و محمودی بتونیم از این خستگی رها بشیم   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SorkhTimes/139708" target="_blank">📅 19:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139707">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SorkhTimes/139707" target="_blank">📅 19:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139706">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🏅
پایان نیمه اول
🏅
پرسپولیس
1️⃣
_
🏅
ذوب‌آهن
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes
0️⃣</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SorkhTimes/139706" target="_blank">📅 19:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139705">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=oOEXo43T2x0xUy8a6VbitCPsjv_kLIKMRDx5IWSnEehtAAtGGOU_0IxnioChZZ-I55l8liScfIv2kR_r_OB8dCyYPFfU3T9sSinKhcGzAS4LJPrU1N6EMUZXT1BkFYSoe8_Yy4yTXGHzcC7nV8YgLaKeuor-xo_F5OxZeP0AFgjkb9eI-KWrOD_GEHQ37Fp-QtGGR6vgsSrU5lvlDy939NgqSpaXl9H1IG0dMIun41-HdahfloabSlBN7mfwi0f0z7BW2oSbgpRRtu01zjK834RLsh3gieHJYWGzxvJGLZBB8eARCVUPaIHMGYABNfCINQ1lA7_bbg7PjO9AVMqEJLBmuF66BarGIT7olTXCzeA7TU9kba-PKY9RW84jtTfEuZrh6W91674DSjkS7p-T4fHUDb_45ojzVUe3sl3C9VnSLXDZDL9msgvMjJDnmmKrmCCB1gIPSqdfZLy3jOzMn6CWPkV7XZMqUAlAOLV0z1UaDeXr70ECcrr-19RUOJUX9KjhLZGlwZ0-OjIgQAW7lAIG3xDvLQRIXPpD0-rtlwdmgcXyE5L5N-F4zG96Q5QWIJ75n0c52789Twqdgsd6LzVkL6ii8Cs-i1mrkxyMvbe_QSGyOQ02jyNtxSHPsh-mqXrrYufM3FGMh3Ew30Y4nK4J_o4r_7WcIXeHw2Q20uM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b10d894fc.mp4?token=oOEXo43T2x0xUy8a6VbitCPsjv_kLIKMRDx5IWSnEehtAAtGGOU_0IxnioChZZ-I55l8liScfIv2kR_r_OB8dCyYPFfU3T9sSinKhcGzAS4LJPrU1N6EMUZXT1BkFYSoe8_Yy4yTXGHzcC7nV8YgLaKeuor-xo_F5OxZeP0AFgjkb9eI-KWrOD_GEHQ37Fp-QtGGR6vgsSrU5lvlDy939NgqSpaXl9H1IG0dMIun41-HdahfloabSlBN7mfwi0f0z7BW2oSbgpRRtu01zjK834RLsh3gieHJYWGzxvJGLZBB8eARCVUPaIHMGYABNfCINQ1lA7_bbg7PjO9AVMqEJLBmuF66BarGIT7olTXCzeA7TU9kba-PKY9RW84jtTfEuZrh6W91674DSjkS7p-T4fHUDb_45ojzVUe3sl3C9VnSLXDZDL9msgvMjJDnmmKrmCCB1gIPSqdfZLy3jOzMn6CWPkV7XZMqUAlAOLV0z1UaDeXr70ECcrr-19RUOJUX9KjhLZGlwZ0-OjIgQAW7lAIG3xDvLQRIXPpD0-rtlwdmgcXyE5L5N-F4zG96Q5QWIJ75n0c52789Twqdgsd6LzVkL6ii8Cs-i1mrkxyMvbe_QSGyOQ02jyNtxSHPsh-mqXrrYufM3FGMh3Ew30Y4nK4J_o4r_7WcIXeHw2Q20uM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول پرسپولیس به ذوب آهن توسط علی علیپور
🔥
❤️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SorkhTimes/139705" target="_blank">📅 19:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139704">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">❌
❌
واقعا چهار روز چهار روز بازی کردن تیم و بچه هارو خسته کرده و واقعا تو ساق بچه ها خستگی واضحه  «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SorkhTimes/139704" target="_blank">📅 19:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139703">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">✔️
✔️
تازه میفهمیم که چرا ارونوف و روی نیمکت می‌ذاشت تارتار ‌..واقعا آماده نیست   «سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139703" target="_blank">📅 19:43 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139702">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❌
❌
بریم برای بازی شش امتیازی ..امیدوارم مثل بازی های گذشته از دیدن فوتبال پرسپولیس لذت ببریم ...الهی به امید توووووو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139702" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139701">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbCkeJkLp-fDR2p8jx-yLSdJrC_OebXAUeKr6yCaseZ0BfuaqMD8SHK2rpoD8HDJXcr748fRnfGVIt1KBdWA2wAhxEdCCnXf4XGWyAfXIZ2RJdBPRORoIXuKUIxB18hzMrgY7kTt_V5wqmNpfo80j3v1yGSWu0yb1SHohnYR6fsxupUT5ru4T-hByn3r5H3Wd_UqP7cmlXqUCEAdTpmj8X1jHAtHjPZTtwJqHMIisafTwGJ21Dd2IGH7-D2RL4h_XFCZDicFeIBwb_4Srp4p8r7VtPaz8c5Drfii5_GYqN60QYE6mQroRd6GOsvvg-OT4Z7h1eoT6OnSJ_uX78Im7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎾
نبرد در نیویورک به اوج خود رسیده!
🟡
گرنداسلم یو‌اس اوپن؛ جایی برای جنگِ ستاره‌‌ها
🎾
بزرگان تنیس برای آخرین جام بزرگ سال می‌جنگند.
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی رقابت‌های یواس اوپن همین حالا وارد سایت اسپورت‌نود شو و پیش‌بینی خودتونو ثبت کنید:
👇
2⃣
نسخه جدید سایت:
Sportn5b2.com
2⃣
نسخه قدیمی سایت:
Sport90.bet
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/SorkhTimes/139701" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139700">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/139700" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139699">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">✔️
هوادار پرسپولیس درباره جنجال امید عالیشاه و خداداد عزیزی
❌
❌
آقای خداداد عزیزی به قول سیدجلال ما پرسپولیسی‌ها هیچ چیزی از یادمان نمی‌رود. خدا نکند که ما پرسپولیسی‌ها با تو رودررو شویم؛ می‌توانی از بیرانوند بپرسی. مثل خودت با تو رفتار می‌کنیم. کل افتخارات…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/139699" target="_blank">📅 18:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139698">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">✔️
✔️
✔️
صحبت‌های هوادار پرسپولیس درباره اتفاقات بازی تراکتور- گل گهر و حواشی ایجاد شده میان عالیشاه و خداداد عزیزی!
❌
❌
از کمیته انضباطی سخت می‌خواهیم برای یک بار هم که شده رای درست بدهد.‌امروز نشان می‌دهیم که هیچ کسی حق توهین به عالیشاه را ندارد. امید عالیشاه…</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SorkhTimes/139698" target="_blank">📅 18:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139697">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SorkhTimes/139697" target="_blank">📅 18:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139696">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">✔️
✔️
ترکیب بازی امروز همینه و تایید شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139696" target="_blank">📅 18:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OA1qUGZzR_4CXTlqYYl254dwqtpOi6fDmlzALbOqgBQs694lAKu8BGEWf64meOWUCpJ9lny72_4-4FzauRotDoeZI93YbQsvOHyCaB-2XFYH5gKzyisDWxq7FkxtMmklufLGg3wcIy6SnuosIpUHWvblJSluV2YvQnafJqhZ0XfdX3-_j-vtrxlAf5Fvsz6WWUrxZMoVP6YwMvaX8Jhpa7BAkTBi3bSGpo_hCDDbHBYrwWgcGxvzTOMs5eet7kzYylOXdfJezDG2ClgR1-L35rVeu2Oz-S-a6AGr8bLsKDBkkox9i0mvyziqYMrfNqcTyCatFPsanry39SnnYqua4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3392d48f0.mp4?token=OA1qUGZzR_4CXTlqYYl254dwqtpOi6fDmlzALbOqgBQs694lAKu8BGEWf64meOWUCpJ9lny72_4-4FzauRotDoeZI93YbQsvOHyCaB-2XFYH5gKzyisDWxq7FkxtMmklufLGg3wcIy6SnuosIpUHWvblJSluV2YvQnafJqhZ0XfdX3-_j-vtrxlAf5Fvsz6WWUrxZMoVP6YwMvaX8Jhpa7BAkTBi3bSGpo_hCDDbHBYrwWgcGxvzTOMs5eet7kzYylOXdfJezDG2ClgR1-L35rVeu2Oz-S-a6AGr8bLsKDBkkox9i0mvyziqYMrfNqcTyCatFPsanry39SnnYqua4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
✔️
هواداران پرسپولیس در پاسخ به فحاشی خداداد عزیزی به امید عالیشاه، کاپیتان سابق خود را تشویق کردند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/SorkhTimes/139695" target="_blank">📅 18:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">✔️
✔️
✔️
نیمکت
✔️
امیر رضا رفیعی
✔️
ایری
✔️
ابرقویی
✔️
جلالی
✔️
باکیچ
✔️
لطیفی فر
✔️
یاسین
✔️
صادقی
✔️
محمودی
✔️
بیفوما
✔️
شهرآبادی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/139694" target="_blank">📅 18:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">✔️
✔️
شماتیک ترکیب پرسپولیس مقابل ذوب‌آهن
🗣
اورونوف دلها فیکس شد
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SorkhTimes/139693" target="_blank">📅 18:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kt-H4raiuJsdZJDPNqnPZ2DbvQ4ikheWzwM30jaMpBTA3pQYrjiSAef9T92cvvwdcERVsTQCNvyAALNMoMeBPgPikakThkZTvTaypvmkQpEGzljSD4ta56AY8a6l7fOL6kZL-xFn0pqqXhS5IAFIa80D1nUioy0WsPkCjkNsB-taf-Q5nwL2Eb4kwpcVDIc7I9IxylOd9k0gstBbC3KVEGDiw51bJKp69N7FP9Vlg37lMT_K8GVC8JSooQpKuopInPPUcs9APAoaG6KXUnsuEAQrnHtW9EUaP375VGbMoMUs11U6Bx6Mr55R88axd9aERUmIm7kCS3xTNaeokQpthA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SorkhTimes/139692" target="_blank">📅 18:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139691" target="_blank">📅 17:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=I-eUxd1-uK7vhr9pJdoZBQ6pso6c5qiBhczVR2_OH7AaocWhmfldJsRZN6C6fgI7AVl1UJBI3Hb_7PegobqeXzybDKOv5quyd7G9QIbUtDnMSTbBJkrm4iPWxCz73zSNtO3e1k8GvJUUUf6t8dfTfleJ31VhSA5DmM44uf58s-8ZtjC6CuDp4uFKUr0IfBytslxtJ2xNNuO6WuS8eygCSXkTaFMAs925TG1bYagBs1R7YeTy_ZuY3TDe1yZk_VFTH4JDFJAe6rjKtBh4k2C1QT1dxFceyvAPHUjK-SgM3nqwybeIOcHy5gLQdZNvE3tcaysojCwD0U5fiGqVXo9ebA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7939cefa83.mp4?token=I-eUxd1-uK7vhr9pJdoZBQ6pso6c5qiBhczVR2_OH7AaocWhmfldJsRZN6C6fgI7AVl1UJBI3Hb_7PegobqeXzybDKOv5quyd7G9QIbUtDnMSTbBJkrm4iPWxCz73zSNtO3e1k8GvJUUUf6t8dfTfleJ31VhSA5DmM44uf58s-8ZtjC6CuDp4uFKUr0IfBytslxtJ2xNNuO6WuS8eygCSXkTaFMAs925TG1bYagBs1R7YeTy_ZuY3TDe1yZk_VFTH4JDFJAe6rjKtBh4k2C1QT1dxFceyvAPHUjK-SgM3nqwybeIOcHy5gLQdZNvE3tcaysojCwD0U5fiGqVXo9ebA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📌
هوادار پرسپولیس:
✔️
ورزشگاه آزادی درست بود، بی‌افتخار ترین تیم لیگ (تراکتور) عمرا قهرمان نمی‌شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139690" target="_blank">📅 17:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=LRPHuSN16BONq5BHu8OaBUMEQ36ika5M1u4yTuvvObBm4j71ZltJrR9Yv4Lvmmq49NrzW5BiMgF6GQmNMkvatx9xP9jP6IdlUgehZ49NBgqe1hoDax085z-YQUSl5-XHeYFNtHwxXKJLHtgnr0A3iC77WKagfW0XShFH0qyFFaAiEdiIwBd2zybadCYeUtBChehodWD9rX7La5eZXmrhUD1FUjJzLpjfGrzRq69_zqBO_-rYgvr_hzRoyQhMOgSDJi-c8htvBQdgYkD_Rm1aGn8lq4lw0aQOm0yKyNjJnx_tWHvf6lVsr7mcTGFcb-fZ3G4P8w_RChfepfoj1x88Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8432a81f4.mp4?token=LRPHuSN16BONq5BHu8OaBUMEQ36ika5M1u4yTuvvObBm4j71ZltJrR9Yv4Lvmmq49NrzW5BiMgF6GQmNMkvatx9xP9jP6IdlUgehZ49NBgqe1hoDax085z-YQUSl5-XHeYFNtHwxXKJLHtgnr0A3iC77WKagfW0XShFH0qyFFaAiEdiIwBd2zybadCYeUtBChehodWD9rX7La5eZXmrhUD1FUjJzLpjfGrzRq69_zqBO_-rYgvr_hzRoyQhMOgSDJi-c8htvBQdgYkD_Rm1aGn8lq4lw0aQOm0yKyNjJnx_tWHvf6lVsr7mcTGFcb-fZ3G4P8w_RChfepfoj1x88Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
بانوان پرسپولیسی و تشویق امید عالیشاه در شهرقدس!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SorkhTimes/139689" target="_blank">📅 17:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alss_YIq3D1Kzm8HEj4VWqdslDedj85sCEiVZURT0d79SDlB2Y6R2NGUYe9_xMgrSBpXJ6_51mqqvVxE09DL7iI2TytnkqwXWqwsU3t76j73S79hbtBCRPMii6gcOECq188zGjmiMnwwIjMJGSxRPPzVol5aHTMJTadISXsgL7xWTsvPepEayKsFJQYL1x2mez-vD-tcJLzjhfthdH-jgQPkPOdfyszqRrQ1xSKZnBwzAOzRN70rFRujDMnHTitqETCjkuSQETZBZY2tWPG4vEWXYO7UmRyiIYyKoA9bUWQkJc6wxWMqcVbj1pz8yWiuf37kv8-M9vTvVkNNzgkd4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
عالیشاه وکیل گرفت
❌
❌
شکایت عالیشاه از خداداد عزیزی به زودی در مراجع قضایی ثبت خواهد شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/139688" target="_blank">📅 17:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139687">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOajagnh2fC-GQcY_c9uQvlppXxwSQuK4IkTVEz7apupCM8cfSXGynKdSzOx1_1oXiJOP8EP9P6Ibb_Kws8Jpj-caYxe4P45_V8QmIsQ_VjifcZ7YQNkOYlZPhlDqNvqmCYGJIsJMnfjk-oe-ojYWVCEYB0rTP2u46kd17S7-nYLOUqUZKFfvKhcs33QJN_HfDksE7X1z1_kb4wAXPIyKLX5M9AV9jCURHrU7Q2F3UtpRDXERgg7zgHroPRC2V0V2uSo379O1Es66ACouczPN2qmrVGXO1Y2e9Iwu5ylTOQ-H-nHyHd50iNJyo83KYnrNy9k4IYdAnwbwxs6WuBArw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
هوادارا دم در ورزشگاه شهرقدس
😂
🗣
ورود بدون کارت ملی ممنوع!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SorkhTimes/139687" target="_blank">📅 17:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139686">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">✔️
✔️
گفته میشه که ویسی از که از خداداد عزیزی پخش شده فقط بخشی از فحاشیش به امید عالیشاه بازیکن گل‌گهر بوده و بخش زیادی از فحش ها و صحبت ها پخش نشده و قرار است به دادگاه ارائه شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/139686" target="_blank">📅 17:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139685">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">✔️
✔️
لیست تیم ملی امید اعلام شد.
🔻
اردو برای اعزام به بازی های آسیایی 2026 ناگویا از صبح فردا دوشنبه 16 شهریورماه در هتل المپیک برگزار می شود.
✔️
✔️
اسامی دعوت شدگان به شرح زیر است:
✖️
✖️
محمد خلیفه؛ادیب زارعی؛آرمین عباسی؛محمد امین حزباوی؛مسعود محبی؛دانیال ایری؛یاسین…</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SorkhTimes/139685" target="_blank">📅 16:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139684">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
پرسپولیس با مدارک جدید دوباره پرونده آسانی رو پیگیری کرده و معتقده حضور این بازیکن در استقلال غیرقانونیه. سرخ‌ها میگن مدارک جدیدشون کامل‌تر از شکایت‌های قبلیه و امیدوارن این بار نتیجه پرونده تغییر کنه.
🚨
فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SorkhTimes/139684" target="_blank">📅 16:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139683">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">❌
🔴
پرسپولیس موفق شد امتیاز تیم دسته اولی فولاد نوین رو بخره و تبدیل به پرسپولیس ب خواهد کرد و سید جلال حسینی هدایت این تیمدرا برعهده خواهد گرفت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SorkhTimes/139683" target="_blank">📅 16:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139682">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OtBzul3UvXFq0vW4_XQPGF60kFYEt64MxIS1QcK8E97WpAWu3XFiCqVM1HBLl70mNM9VUo0TyvUPVjG0Vd5X0BSBbhavBMnar0QJE5te_oGjxjxaslQFWWNvndjMIBES0IBlQ2AF1nMmdRR4T808iO-TytYsajC7y6QJqmJLo97ot4-MNgzm3yGI9vEUXQS1Iiyok30jYIoYFylys3b94fa0Ej2MO49l5XPP6qOvctt95i0IGOR18IuiMoEuMz308vWQiFCWjzA9-rAg9pBLC_lyzqFIoSPak1a-4ED__Hem6XtM74xYkWOkfXFonqBdIt4LvvoFN21-weJZnVE-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پرسپولیس مقابل یک حریف سرسخت!
⚽️
ذوب‌آهن آماده برای غافلگیری
سه امتیاز، پاداش یک شب بزرگ
[
پرسپولیس
🔴
🆚
🟢
ذوب‌آهن
]
🔵
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای پیش‌بینی این دیدار همین حالا وارد ربات رسمی اسپورت‌نود شو و پیش‌بینی خودتو ثبت کن:
👇
🔵
@Sportnavad_bot
🔵
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
🔵
@Sportnavad</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/SorkhTimes/139682" target="_blank">📅 15:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139681">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">❤️
🎉
تولدت مبارک پسر متعصب پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/SorkhTimes/139681" target="_blank">📅 15:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139680">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⭕️
⭕️
فوووووووری
🚨
امید عالیشاه با حضور در دادسرا از خداداد عزیزی شکایت کرد
🔔
80 ضربه شلاق در انتظار افغانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/139680" target="_blank">📅 13:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139679">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9NXrrBwuJzG2VargKjx-HI56cq_QSISqs8_V1JRX2nw0uU_xXndyFy_QVZsoACXOju6OIY_UyTTvjOUFMoZRa_YjIcTyEBCz_Z11GEHCgGCqQb5hHcCZamNf7UEqri7irnTa_SSLoUVMqHnNdlY2jWxFugqltTBHJNeVNHZOQv_V32u41bqCBVXW_cyzM3tj2H-KkFg8Ch1B_XXT13zLQtiDFIWep0IyHw_NiE1vk6fShRiQx-ceU7cxwyLW71L2qy5HYD958OkbnKCg0hS-jddBbyQoYbS6xTmOcdCev3X2uIJszyrR32SM2WRiBExi6rQhIm45j-0ACG2EkzOJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عضو پنجم هیئت مدیره پرسپولیس مشخص شد.
✔️
به نظر می‌رسد روند انتخاب عضو پنجم هیئت مدیره باشگاه پرسپولیس به مراحل پایانی رسیده و حسین صابری خورگو به عنوان عضو جدید این هیئت معرفی خواهد شد.
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/139679" target="_blank">📅 13:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139678">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⭕️
⭕️
بهاروند: طبق مصوبه هیئت رئیسه فدراسیون فوتبال لیگ نیمه کاره قهرمان ندارد.
🚨
🚨
پرونده جام حذفی فصل قبل بسته شده و درباره برگزار شدن یا نشدن جام حذفی این فصل هم هنوز تصمیم گیری نشده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes.</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/139678" target="_blank">📅 12:24 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139677">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">❌
❌
درپی‌اتفاقات‌دیشب؛ به احتمال زیاد خداداد عزیزی سرپرست تراکتور دو الی چهار ماه از همراهی تیم تراکتور محروم میشه و امید عالیشاه یک الی دو مسابقه گل‌گهر رو به دلیل محرومیت از دست میده.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/SorkhTimes/139677" target="_blank">📅 10:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139676">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">❌
❌
#فوری؛ بعداز حرفای‌ دیشب تاج برای اهدای جام قهرمانی فصل گذشته به باشگاه استقلال؛ مدیران دو باشگاه‌ سپاهان و تراکتور به فدراسیون اعلام کرده اند یک‌ تورنمنت سه‌جانبه برای تعیین قهرمان برگزار کنند. به‌ اینصورت‌که تراکتور - سپاهان به مصاف هم برند و برنده اون‌…</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/SorkhTimes/139676" target="_blank">📅 10:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139675">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
طاهرخانی ادعا می‌کنه پنجره نقل انتقالاتی کیسه تا آخر تابستون ۱۴۰۶ بسته است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/SorkhTimes/139675" target="_blank">📅 08:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139674">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">❤️
صبح روزی که بازی داریم و شش امتیازیه بخیر
❤️
❤️
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139674" target="_blank">📅 08:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139673">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">✅
می‌خوای پیش‌بینی کنی، ولی نمی‌دونی چطور حسابت رو شارژ کنی؟
وینکوبت کار رو برات ساده کرده!
با درگاه بانکی اختصاصی و امن وینکوبت، حساب کاربری خودت رو به‌صورت مستقیم شارژ کن و مثل هزاران کاربر دیگه، بدون دردسر از امکانات وینکوبت استفاده کن.
🎁
بونوس ویژه اولین شارژ:
فقط با یک پیش‌بینی، می‌تونی ۱۰٪ از مبلغ اولین شارژ خود، بونوس خوش‌آمدگویی رو دریافت و به موجودی اصلی حسابت اضافه کنی.
🟣
آدرس سایت وینکوبت:
wincobet.com
🔗
همین حالا وارد مینی‌اپ وینکوبت شو و اولین شارژت رو انجام بده:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.62K · <a href="https://t.me/SorkhTimes/139673" target="_blank">📅 01:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139672">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔞
🔞
🔞
❌
صدای منتسب به فحاشی ناموسی خداداد عزیزی بعد از بازی امشب تراکتور و گل‌گهر به امید عالیشاه در کنار رختکن گل‌گهر سیرجان! در صورت تأیید این صدا احتمالا محرومیت چندین ماهه نصیب خداداد میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/SorkhTimes/139672" target="_blank">📅 00:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139671">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SorkhTimes/139671" target="_blank">📅 00:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139670">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به…</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/SorkhTimes/139670" target="_blank">📅 00:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139669">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❤️
❤️
ترکیب پرسپولیس در بازی فردا برابر ذوب آهن
🔴
سیستم پایه:۴۴۲
🔴
پیام نیازمند
🔴
محمد‌مهدی زارع
🔴
حسین کنعانی‌
🔴
مجید عیدی
🔴
مهدی تیکدری‌نژاد
🔴
پویا پورعلی
🔴
محمد خدابنده‌لو
🔴
محمد‌ مهدی محبی
🔴
اوستون اورونوف
🔴
ایگور سرگیف
🔴
علی علیپور
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/SorkhTimes/139669" target="_blank">📅 00:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139668">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=W3F6wx1xOKZw7Xi-ybRYG8cEhRUfJ_gKr3hzaADgcjqmf9JnBXYeFtI_OFAkPb1kgCvfhlTOKeUhcx35m8VCrauhByXiqkWg8LqM0BphwYfDqUem2kOaflywxa9-jXtVtP7ebhyxnAg1VT7ZDxlqlMZIecX4W9m44iCNtJxMz2vdS5tfo5PeJh5GkOtmd0oube5cU0le0qoNu9fkxmIwF70jzzJQ-nfAX70cXDa-SJqzmzhkvvMHsKZabiYEzhTBtSjQfgCPBDexxtMEf2LdN4U5aB3W6dWvb9Fj3Tboqj2dFP6PF5phOwBxOTW7T4GogAUPM461lbWYFj61C9x7IA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd7cdc1c0.mp4?token=W3F6wx1xOKZw7Xi-ybRYG8cEhRUfJ_gKr3hzaADgcjqmf9JnBXYeFtI_OFAkPb1kgCvfhlTOKeUhcx35m8VCrauhByXiqkWg8LqM0BphwYfDqUem2kOaflywxa9-jXtVtP7ebhyxnAg1VT7ZDxlqlMZIecX4W9m44iCNtJxMz2vdS5tfo5PeJh5GkOtmd0oube5cU0le0qoNu9fkxmIwF70jzzJQ-nfAX70cXDa-SJqzmzhkvvMHsKZabiYEzhTBtSjQfgCPBDexxtMEf2LdN4U5aB3W6dWvb9Fj3Tboqj2dFP6PF5phOwBxOTW7T4GogAUPM461lbWYFj61C9x7IA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
چشمی باید اخراج می‌شد
✔️
✔️
حسین عسگری:
خطایی از این واضح‌‌تر و محکم‌‌تر نداریم مصداق خطای شدید و اخراج است
✔️
✔️
تورج حق‌وردی:
با شدت به زانوی حریف ضربه زد مصداق خطای شدید می‌باشد و باید اخراج می‌شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/SorkhTimes/139668" target="_blank">📅 23:54 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139667">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxXPxh0oYmz8BzjLTCxfDKYDYW_90aJ6MS_DX38bOpeU6Z0idbDpc_4XgdY2lvdJiE7A48h--YiGOhOX6q7JkUhUn14J5JSWw3kGWsE4so9preViJsA4qj5zrB5nN4lMz7R_JiR9oJuZlfuVCKe9wKfOJklLrJ7cI3kMbc8zL1Obfl-HuNXr8El3aFWPUaLB0Cn9-iOjyAtTZCAbnRcP3utVJOxRBuj3XfufhZCDNxzfuPvXAYerpdQulDltEKYc34aLwlm96ajWWqHKvOfxQg8MEpEQuwjTT8RnhcO3r01Bvqink1BOyu7ZWEktVWALMI_hS__51TKJt3ZrxzsE5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
✔️
اگه فردا ببریم با ۱۳ امتیاز میریم دوم جدول
❌
❌
فوق العاده مهمه ۳ امتیاز بازی فردا</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/SorkhTimes/139667" target="_blank">📅 23:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139666">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🗣
🗣
فوتبالی: اورونوف فیکسه تو بازی فردا
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/SorkhTimes/139666" target="_blank">📅 23:18 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139665">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">✔️
✔️
تارتار: باید با خداداد عزیزی برخورد شدیدی بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SorkhTimes/139665" target="_blank">📅 23:14 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139664">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">✔️
✔️
۶۰ لیتر بنزین ۱۵۰۰ تومان و ۵۰ لیتر بنزین ۳۰۰۰ تومانی بدون تغییر ماند؛ افزایش قیمت نرخ کارت جایگاه صرف معیشت مردم خواهد شد.
✅
✅
✅
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/139664" target="_blank">📅 23:13 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139663">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭕️
⭕️
فوووووووری
🚨
امید عالیشاه با حضور در دادسرا از خداداد عزیزی شکایت کرد
🔔
80 ضربه شلاق در انتظار افغانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/SorkhTimes/139663" target="_blank">📅 23:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-139662">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">✔️
✔️
لیست تیم ملی امید اعلام شد.
🔻
اردو برای اعزام به بازی های آسیایی 2026 ناگویا از صبح فردا دوشنبه 16 شهریورماه در هتل المپیک برگزار می شود.
✔️
✔️
اسامی دعوت شدگان به شرح زیر است:
✖️
✖️
محمد خلیفه؛ادیب زارعی؛آرمین عباسی؛محمد امین حزباوی؛مسعود محبی؛دانیال ایری؛یاسین…</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/SorkhTimes/139662" target="_blank">📅 22:47 · 15 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
