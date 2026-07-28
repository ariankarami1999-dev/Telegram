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
<img src="https://cdn4.telesco.pe/file/vP-6_qDtNeRC8pQMHUYdqrWO0NT6C0u-IY6vAmDbFOmJ8HmnDTj69JQdg1rQ0HThugrjzWKcWwlusRxb9DBu9AL1fF78alIAEDgcw5PrPB3p2MrGWJ3SFjVM2mZZYscKOTBeWZo8H5K0J9fzpGQdyN4BkfggooAGyQpSxkWdRuw97Oqhb90HNUOiA35hl_X9jWYdpeP-WLoSM0gjq52_q3v7QPcE4IvUKRT2ntcjtUzmxdq0zbgOuFB239qI9e7bDmu2Az97nBAUUJu013d50wCxYWqfC3QXUJvm0DbkC3MjSl_h4JQXAtAUWWsndU4apSCWSgSgcUDvZgLJBHPs2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.5K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 08:43:33</div>
<hr>

<div class="tg-post" id="msg-136885">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZHHyjWxaxQLimjlyNId9Lh7cvfOYe6naHO3g1mkeh-e3I_NVn2-VqseephsDe-b_kEUc3E6h9Utfoqrc8wWKcdDzzHxn75MUJgbdST1mMS879QjezaAxa34uvrrFuLvtY3fNmf9FIeg1JDLyIFnrSsxxwKvoMFAruvbcqKEPI9UEQxXNoBKTKhVuW1RWZT0sRxHCdESnBLXyUbByqN02kO_EkdrAm6FvbqnGNpbFBJ5M9GElkp-vbHNdj28bTdilE-72TtuQ0Zdtc94y_rMKQ5xVXj6ANiZQpzlTobJuP1eve-ndpPK-Npc3cNbCwylzOL2MVYgknKuxtm132nLH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🎲
هیجان واقعی همراه با کازینو
اسپورت نود
⚡️
کازینو آنلاین
اسپورت‌نود
، هیجان واقعی با بردهای بزرگ همراه با انواع
بازی‌های کازینویی،
🎮
انفجار،
💣
رولت، بلک‌جک،
🃏
اسلات و بازی‌های زنده
همراه با پشتیبانی ۲۴ ساعته همین حالا شانس خودت رو امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/SorkhTimes/136885" target="_blank">📅 01:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136884">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
🔴
🔴
به نظر می‌رسه پرسپولیسِ تارتار قراره قبل از هر چیز روی دفاع محکم و کلین‌شیت تمرکز کنه. تیم‌های تارتار معمولاً با دوندگی بالا، پرس منطقه‌ای و محدود کردن حریف بازی می‌کنن، نه فوتبال کاملاً هجومی.
✅
✅
سیستم موردعلاقه‌اش هم ۱-۳-۲-۴ هست، اما با توجه به جنس…</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/SorkhTimes/136884" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136883">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🔄
🔄
🔄
آنا: محمد قربانی با رضایت نامه 200 میلیارد تومنی به تراکتور سازی تبریز پیوست
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/SorkhTimes/136883" target="_blank">📅 00:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136882">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔄
لطیفی‌فر فردا به ترکیه میره تا به اردوی پرسپولیس اضافه بشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.99K · <a href="https://t.me/SorkhTimes/136882" target="_blank">📅 00:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136881">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🫥
🫥
🫥
تارتار امیدواره بیفوما و محمدحسین صادقی رو دوباره احیا کنه. بیفوما بعد از یه فصل ضعیف، تو بازی دوستانه اخیر گل زد و حالا فرصت داره خودش رو ثابت کنه. صادقی هم که فصل قبل فرصت کمی برای بازی پیدا کرد، امیدواره با اعتماد تارتار بیشتر بهش بازی برسه.
🌀
🌀
از…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/136881" target="_blank">📅 00:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136880">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔄
🔄
تیوی بیفوما در پرسپولیس ماندنی شد؟!
🔴
🔴
مهدی تارتار اخیرا در تمرینات پرسپولیس از عملکرد بیفوما رضایت داشت و به مدیران این تیم نیز عملکرد بیفوما را گزارش داده بود.  با توجه به عملکرد بیفوما در دیدار روز گذشته سرخپوشان برابر پیرامیدز مصر بعید نیست که این بازیکن…</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/136880" target="_blank">📅 00:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136879">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSWoSpSV_cpwHI0Kqs-vmcatzsYNfeTIo96SDK8EEvMiGVgXbmikjw6S44osvUNY42Td13BBZfsWv2vghK_vB9Bv2sDx6iK0F6z5YOM6prfjy2doiFQzdfXKMIXj969fZj6oIS_XhLMLHoKXjRtryKohmZhf-gRCex0GTecW9S-gqyazkr3Fp3azLsRBrncLbt0mgXEzI9Ohl36SlB-1klMaDiDHKfPSXS7TftQcmW1OnkusS9Xae3fB0LlHUKdOBj3IrSFoMBRB4fbWoJAv5-G1wr1nIS9295SAyW1z2yQ4L0zhYJcL1laL0lDIIQXPpVYeYlCD32vewAok62UBMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
گویا رامین رضاییان به خواسته 200 میلیارد برای
هر فصل خودش رسید و در استقلال موندنی شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/136879" target="_blank">📅 00:19 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136878">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">⚠️
⚠️
قدوسی و حقیری: مدیران باشگاه دارن فشار میارن که گرا بمونه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SorkhTimes/136878" target="_blank">📅 00:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136877">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">❌
❌
قرعه‌کشی لیگ برتر ایران فردا انجام خواهد شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SorkhTimes/136877" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136876">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UtFzeM4YB8KQc6YoeJcMhheOvCJwcuK2SgkV69W0b4d3sok6-ypn6fhKXr-Z5noe1UNagxtm__iHKNeZ3ABW4gdtr_arwK4Hafq_BXmLRO6MK5QSmRUk3v_gK0AnCt-nBzP-8wP-rLAIGFYjFPokarSut2rmYOU57lFcOyZ4fI-GK-mhhMrx_fDfGkrfMU3iYVZGcSdYsPA7oZo5q6M-jaA5zp5V7m-Q9dwJ1VX1CxtGHz6-SpxOkwfl2qhqh_t97ZceXEeSkvEgMPfptdDMCfyXv9YvThiEo2dlWxfOWelp0uh46bwHW9LaEWo2m2Y8WEfOzU7tXhlkU3v41RcKaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
منهای ورزش
⚡️
درآمدزایی اداره برق از قطع شدن برق!
🟪
اداره برق تو اپلیکیشن "برق من" شروع به فروش اشتراک کرده و پول میگیره تا قطعی برق رو از قبل بهت اطلاع بده! نون تو خون ملت به روایت تصویر:
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/136876" target="_blank">📅 23:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136875">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند  #ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SorkhTimes/136875" target="_blank">📅 23:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136874">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SorkhTimes/136874" target="_blank">📅 23:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136873">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGdkVacR63ISrkWRkIN0kvXEUgg_F13SHMuGBmWVdrS3f6utEHJSlmqOHVbzlFhXKzWrzlYX_JjrhfkEx4AkC7Y5fpwjYu7Of8iK-mAuwI-pIveSRoBQE_n2_4XByIKM7cUO0Lw2Fk1lbO3BWzY1e4xC3xYx0fiRKg4WXHzK_O_w6-Nm_V-uocuZ7IeYNr6Ql6qM2zXx1LKDD_TfUb6TSv9sdXRvxHqjgoe_FIFDGUnBsOGyMoFvya_gM40Qcs4KrdKi41L50jw7wYo1GPrj0CRtoiS0aGxay8iJmTQTkubwJA4nMYlEpeceJITEarP_KylxOxa-CAH9s0exFSSOZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
استوری حسین قهار خبرنگار حوزه پرسپولیس در مورد ایری و طاهری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SorkhTimes/136873" target="_blank">📅 23:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136872">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">✅
گرا در بازی دوستانه غایب بوده و احتمالاً با نظر تارتار جدا میشه/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/136872" target="_blank">📅 23:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136871">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkQ2GExJLx03c350TMg10REn74E159bQ1m73L5IUMZfuRelGpBqCHsASBN3dEqpqw825G6uSvvYxZxcTbYalQzzVKaJg2cW7eJ7JP7XPKHEHyqukuhqNkS6SI9qdx4pVyKCnSJyLRiFPVYl4Hybu3bxMf_M8HjC2HewqCMa_1JnWJEVT4S6mZ871Hb4ORmOUkoTJVMX3ebtSNquWvnGlmy-5XJRGaonVBxoV5l0zV_d-fIUnTYAqD9x1aZHDpIFX_vGeCVsep88FujPAvcgoueKBZrawR7VHdVhdPuhyNucMAKGtNKt09STLH0UZYPlrRFUjApZinHtE-nXCX55fag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌀
🌀
باگناما از گل گهر جدا شد، نیاد پرسپولیس صلوات
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/136871" target="_blank">📅 23:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136870">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=tW5y3Ro1RvN4Lnu2CZvlGVnMowPfxL_z2b0CLjJ23obGKVheN4Nwh5-tcCT-rhNvsXeWl698SuhMU0_jOzeisohqVksZqzGKukJ3IeH3ZCdt3xi5t3E0kPGrW5TA4wpS5dyG1tvh0TxyATrc6lsIbrpU2v5hHo5jMo6irw6kSlTKU0gHO7HT4_I2dqARiRTS0mvqRkknpGn52wDNSeVS77_wWzUpiszZCUrnQNQ0X7yu3FWuNJdSrQN4i5ij3Dv34CQRZqawLFAMNGCNKylxPmTNH3Ik5jBjS_k9iWTJqK9sDSL4wyPK8MvVSjJ3RjMcRF2BlsTxKZBl2NICk2XVXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/332e5dd6e7.mp4?token=tW5y3Ro1RvN4Lnu2CZvlGVnMowPfxL_z2b0CLjJ23obGKVheN4Nwh5-tcCT-rhNvsXeWl698SuhMU0_jOzeisohqVksZqzGKukJ3IeH3ZCdt3xi5t3E0kPGrW5TA4wpS5dyG1tvh0TxyATrc6lsIbrpU2v5hHo5jMo6irw6kSlTKU0gHO7HT4_I2dqARiRTS0mvqRkknpGn52wDNSeVS77_wWzUpiszZCUrnQNQ0X7yu3FWuNJdSrQN4i5ij3Dv34CQRZqawLFAMNGCNKylxPmTNH3Ik5jBjS_k9iWTJqK9sDSL4wyPK8MvVSjJ3RjMcRF2BlsTxKZBl2NICk2XVXIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
سه گل پوریا لطیفی فر و پویا پورعلی به پرسپولیس
🫥
دو بازیکن جدید قرمزپوشان در گذشته توانسته بودند سه بار دروازه این تیم را باز کنند
#ویدیو
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SorkhTimes/136870" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136869">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">⚠️
⚠️
باشگاه برای بازگشت امیررضا رفیعی امروز مذاکراتی داشته….!
🌀
چرا مازاد شد که الان…
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/SorkhTimes/136869" target="_blank">📅 23:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136868">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/136868" target="_blank">📅 23:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136867">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahrooooookh Abbasi</strong></div>
<div class="tg-text">منطقیه این عدله و تفصیرتون کاملا
👍
ک پرسپولیس تو پست محمدقربانی الان بازیکن نیاز نداره،چون باکیچ،مملی و دوتا پوریا هامون ک تازه از گل گهر گرفتیم کافی هستن و بلاخره یجاهایی هم مربی این حقو داره ک با اون بازیکن هایی ک خودش میشناسه و خریده بازی کنه چون اینجور بازیکن هایی ک مورد علاقه سرمربي هستن و با نظر وتاکید خودش جذب میشن بخاطر اون رابطه ایی ک بینشونه یجورایی برای اون سرمربی جون میدن و تو زمین براش کم نمیزارن...ولی الان ک قربانی با این تفاصیل جذب نشد اینو هم باید بگیم ک تو پست ۱۰و پشت سر مهاجم حتما یکی مثل محبی،ترابی،هاشم نژادو...باید از نون شب واجب تر و جذب شه</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SorkhTimes/136867" target="_blank">📅 23:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136866">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🔴
🔴
روزنامه گل چاپ فردا:
😀
مهدی طارمی بین لیگ برزیل یا پرسپولیس به زودی تصمیم گیری میکنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SorkhTimes/136866" target="_blank">📅 23:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136865">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
‼️
شماره 8 مرتضی پورعلی گنجی رسماً به مهدی تیکدری رسید تا جدایی مدافع میانی قرمزها قطعی شود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SorkhTimes/136865" target="_blank">📅 23:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136864">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">❌
❌
فارس: تارتار از عملکرد گرا و بیفوما تو تمرینات تیم راضیه و احتمالا این دو بازیکن فصل آینده تو پرسپولیس بمونن. ( شما بخون نتونستن یا اجازه ندادن این دوتا برن..)
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SorkhTimes/136864" target="_blank">📅 23:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136863">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
🏅
آقای هوادار ۸۰ درصد نفراتی که تو لیست اول تارتار بودن جذب شدن و تمام نفراتی که از گل گهر میخاست، لطفا از الان بهونه دست کادرفنی ندید، آقای تارتار طاهری رو نمیخاست و گفته بود حد المکان ایری رو جذب کنید.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/SorkhTimes/136863" target="_blank">📅 22:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136862">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">#شفاف_سازی
⛔️
در خصوص محمد قربانی خیلی هوادارا میگن بخاطر اینکه تراکتور تقویت نشه ما باید جذبش میکردیم، اما بودن خدابنده لو،باکیچ،پورعلی و لطیفی فر به هیچ وجه قابل توجیه نیست جذب قربانی
🔴
البته باشگاه قبل از جذب پورعلی و لطیفی فر برای محمد قربانی نامه زده بود اما همون ابتدا کنسل شد، یکی از عللش این بود که ایجنتش منصور عظیمیه دست راست زنوزی و اجازه این انتقال رو نداد،قربانی از دو باشگاه دیگه ایرانی هم پیشنهاد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SorkhTimes/136862" target="_blank">📅 22:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136861">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">❗️
اعلام ساعت قرعه‌کشی لیگ برتر
🔴
🔴
مراسم قرعه کشی لیگ برتر جام خلیج فارس فصل ۱۴۰۵-۱۴۰۶ ساعت ۱۶ روز سه شنبه ۶ مرداد در سالن همایش های بین المللی هتل المپیک تهران و با حضور مدیران فدراسیون فوتبال، سازمان لیگ و نمایندگان ۱۸ باشگاه حاضر در این رقابت ها و اهالی…</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SorkhTimes/136861" target="_blank">📅 22:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136860">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhossein</strong></div>
<div class="tg-text">این نکته رو بگیم ک درویش با همین مدیر فاسد سر فخریان عجب دزدی کردن غیر عادل هیچ کسی حرف نزد</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SorkhTimes/136860" target="_blank">📅 22:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136859">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🤩
#اختصاصی_سرخ_تایمز
📌
🏅
به گزارش رسانه «سرخ تایمز» و با اعلام عضو هئیت مدیره باشگاه پرسپولیس
⭕
باشگاه پرسپولیس برای جذب دانیال ایری و کسری طاهری به صورت رسمی از سازمان لیگ و فیفا استعلام گرفته تا در صورت نبود هرگونه مانع قانونی، قرارداد این دو بازیکن را نهایی…</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SorkhTimes/136859" target="_blank">📅 22:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136858">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
❌
شنیده می‌شود در صورتی که امیر قلعه‌نویی قول قهرمانی ملی پوشان در جام ملت‌ها را بدهد، در تیم ملی ماندنی خواهد شد!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SorkhTimes/136858" target="_blank">📅 22:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136856">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">✅
✅
فدراسیون فوتبال و شخص مهدی تاج به دنبال تمدید قرارداد بلندمدت با امیر قلعه‌نویی هستند! هیات رییسه با این تصمیم مخالف است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/SorkhTimes/136856" target="_blank">📅 22:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136853">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🤩
#تایمز_توئیت
❌
هر روز برای من مطالبی تحت عنوان افشاگری از مدیران باشگاه میفرستن که بیشتر شبیه فیلمنامه هاست
⁉️
وقتی هر روز یه روایت جدید از نقل‌وانتقالات میاد، آدم نمی‌دونه مدیرعامل کیه، سرمربی کیه، دلال کیه، خبرنگار کیه، منبع آگاه کیه!
❌
یه عده میگن فلانی توافق کرده، یه عده میگن نه، یکی میگه پول نیست، اون یکی میگه پول هست ولی نمی‌دن، یکی میگه لج کرده، یکی میگه اصلاً از اول قرار نبوده!
❌
باشگاه رو انگار گروهی دارن با ریموت کنترل می‌کنن؛ هر دکمه دست یکیه، فقط دکمه «اعلام خبر قطعی» خراب شده!
❌
خلاصه تا وقتی هیچ سند و خبر رسمی‌ای منتشر نشده، این مدل روایت‌ها بیشتر شبیه فیلمنامه‌ست تا خبر. ولی خب برای جذب فالور و دعوا راه انداختن، ظاهراً از هر نقل‌وانتقالی جذاب‌تره!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/SorkhTimes/136853" target="_blank">📅 22:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136851">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">➕
بعد پنج سال به این نتیجه رسیدم حداقل نصف هوادار هامون متعصب،ناآگاه،هیجانی،و تو دنیای موازی هستن و اغلب دنبال کری خوندن و دلقک بازی
➕
هیچ فهم و درکی از فوتبال حرفه ای ندارن و چشم گوششون به دهن چهارتا از خدا بی خبر بچه ساله که گوشی گرفتن دستشون میگن لنگش کنید، هوادار واقعی پرسپولیس رو سکوعه که لب دهن نیستن اونی که تو گرما و سرما از تیمش حمایت میکنه و بالا پایین این تیمو دیده و به مسائل اشراف کامل داره، یه عده فقط لب دهن مجازی هستن و ساخته شدن تو زمین رقبا بازی کنن
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136851" target="_blank">📅 22:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136850">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🫦
کونده رفته به ایجنت ایری و طاهری گفته به بازیکن هاتون بگید استوری بزارن… شما که پول نداشتید گوه خوردید این دوتا رو خریدید به امید اینکه این وسط یه پولی گیرتون بیاد ولی فعلا کیر خر دستتون داده بانک شهر… به قران خود بازیکن ها هم ذی نفع بودن وگرنه هیچ کصخولی…</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136850" target="_blank">📅 21:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136848">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/SorkhTimes/136848" target="_blank">📅 21:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136847">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🗣
خیلی اینکاره این
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/SorkhTimes/136847" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136846">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری…</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/SorkhTimes/136846" target="_blank">📅 21:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136845">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6K23ShxVd7fafdbLz_8VlOak-zqCHk_VR_G2cBtdg0QjRw2a5Lbbt5Pdg2E2LQnUsfR4LY3yJvGB8qbwv4EiF0CuTLVANZUbjDgGrOrX6po2xVZz_qUNX7oj8fFlyZwEgC1jp_C-Fn7PfGWaL1TmGw3M2dWg25WwxSMlMIv_0bexbgTyvgNFNTHHzXpGh4d8ASNUezzQbJPkC8FPCWM2a761Ovo8PXKhRkrguJ-L_5exEsw_oYveIZzDo9ryANLW1p1BH11MgpIL8xlRr3fdG6F5LqbPUl1f5vWhlNN2tcm1JfneH80SzrCRHKgYU6Yp-fQp-MDfA-TKSN5pDb7eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
شهاب‌زندی‌مدیرعامل‌باشگاه نساجی مازندران:
◻️
تا فردا شب تکلیف دانیال ایری و کسری طاهری مشخص خواهد شد. باشگاه نساجی حسن نیت خود را برای انتقال‌این‌دو بازیکن به پرسپولیس نشان داده وحالامدیران این‌باشگاه باید تصمیم بگیرند که واقعا دانیال ایری و کسری‌طاهری رومیخواهند یاکه خیر!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136845" target="_blank">📅 21:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136844">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
✖️
✖️
آنا: یاسر آسانی به سرنوشت دیدیه اندونگ دچار شد و تحت هیچ شرایطی نمیتونه تا نیم فصل برای استقلال بازی کنه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136844" target="_blank">📅 21:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136843">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6Q6gzOSHp7oyM1EqOUh-jNtsIEZPsdMZO89mQmjz8wJOEhR3gPZcdyEe7zRlk2fXZWm_TVkeues72mLkl0MP4VxZ1eq4sLkG592TahDBfwuzdaUop6Rpr0DipAwrXrgp26r_wq7Qf9yg6MS-bHymUekdSZkxHfO2NDT_VykUtTJTSsFnpr-JijEB2jjxeqZw5Z_vDZBgRYSpuAOl43PW0zxUkQz5TcQihPLsVFsihCrFZxTcFZ5BBfgEiUED10iK93f7-c384m9ckbsb6gpAuxu05dIRNQk_JQdHR7ooJRXuzL0lncSxOx5w9QB7PrMJGsy086QbcO7cYWBXb8k2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
👋
گل رو پیدا کن و جایزه ببر!
🧐
وقتش رسیده تا دقت و شانس خودت رو به چالش بکشی!
⚡️
همین حالا وارد سایت شو و حدس بزن گل زیر کدام لیوان هست و شانس خودت را امتحان کن!
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/SorkhTimes/136843" target="_blank">📅 20:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136842">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136842" target="_blank">📅 20:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136841">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">❌
❌
☹️
ادعای ترامپ درباره ایران:ما در حال گفتگو هستیم و به نظر می‌رسد که اتفاقات خوبی ممکن است رخ دهد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136841" target="_blank">📅 20:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136840">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">❌
❌
❌
#فوری | ترامپ:
🔻
برای دیدار با مقامات ایران به توافق رسیدیم
‼️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136840" target="_blank">📅 20:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136839">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔹
🔹
🔹
فوری/کانال ۱۴ اسرائیل:
🔹
ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136839" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136838">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/SorkhTimes/136838" target="_blank">📅 19:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136837">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136837" target="_blank">📅 19:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136836">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
🔴
پرسپولیس برای جذب فرهان جعفری از نظام وظیفه استعلام گرفته و اگه مشکلی نداشته باشه میاد پیش خودمون/قدوسی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136836" target="_blank">📅 19:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136835">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎶
🎶
🎶
صادق محرمی طی روز های آینده از تراکتور تبریز به صورت رسمی جدا خواهد شد و احتمالا به پرسپولیس بازخواهد گشت/ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136835" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136834">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from🔱 Hero 🔱</strong></div>
<div class="tg-text">همه چی رو کنار هم میزاری میبینی کسری طاهری و دانیال ایری و مدیرعامل نساجی و دلال این بازیکنا در کنار بنگاه دلالی ورزش سه دستشون تو یه کاسه هس و دارن آخرین زورشون رو میزنن برای تیغ زدن باشگاه صب ورزش سه خبر میده کنسل شدن الان بازیکنا خیلی یهویی با دستور دلال هایشان استوری مشترک میزارن هوادار هم که خدارو شکر سوار موج میشه</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136834" target="_blank">📅 18:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136833">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">#شفاف_سازی
🔖
🏅
نساجی دانیال ایری رو پارسال ۷۰ میلیارد از ذوب آهن خریده الان زندی گفت ۱ میلیون دلار بدید…پول زور
❌
کسری طاهری ۷۰۰ هزار دلار خریدن گفتن ۸۰۰ هزار دلار… باشگاه میگه با همون ۷۰۰ هزار دلار رو میدیم
❌
باشگاه اگر ۸۰۰ هزار دلار بده هم تا نیم فصل نمیتونه…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136833" target="_blank">📅 18:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136832">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⭕
هرکسی از ننش قهر کرده گوشی دست گرفته کانال هواداری زده هر کصشری میخان میزنن، اون حروم زاده ها اگر میخاستم بیان پرسپولیس چرا رفتن نساجی؟! صدرصد هم خود بازیکن هم ایجنتشون با زندی بستن
‼️
یکم عقل تون به کار بندازید خداوکلی چرا هرکس هر کصشری میگه طوطی وار تکرار…</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136832" target="_blank">📅 18:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136831">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل…</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/SorkhTimes/136831" target="_blank">📅 18:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136830">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
🥇
آقای مدیرعامل بزار چند صباحی از پرونده عظیم فساد تون داخل باشگاه مس رفسنجان بگذره… بعد ادای آدم های سالم و مظلوم رو در بیارید
❌
هر موقع پای میز مذاکره زورشون نمیرسه پول مفت بگیرن که از روش بخورن به هوادار دنده میدن، هوادار هم که ماشالله مسائل رو تجزیه تحلیل نمیکنه شروع میکنه کوبیدن باشگاه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136830" target="_blank">📅 18:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136829">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIZ_RG_RbSAFlWjlZyyqVAMofZmAGhB4brZXshc0drfHoCR_0ofXgmLcTKsarZ9tww-q8sqifmSfmFZv0jgYh1g8-NHGfYUgmXxeScAZntfj7TjWFzsOzw3MtnLA8B5tmQ6M3nIkSyl874Wn7rRubCxIKHsdzG6R_zaBkX-bd7QUSgM96vpgUnVdVxkyIZtSCAsllGpHsX056iLsjTW5rsULVIqeZgbfcGDj5JbYzfVrMpJG64bmfM4ShpKx_NCq0oOUutI0LVcUAjX5v4-QdGE2-Zp3RFUnwMXnJGnQFL5yyldYm4kXz95myoRf3m3GllcdigjkS2eJUgHaoqe5lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیرانوند اصلا دانشجوی دکتری نیست
🔺️
رئیس مرکز ورزش و تربیت بدنی دانشگاه آزاد گفت آخرین مدرک بیرانوند، کارشناسی ارشد است و او حتی دانشجوی دکتری هم نیست.
🔺️
پیش از این بیرانوند در تاریخ ۵ خرداد ١۴٠۴ و در برنامه فوتبال برتر ادعا کرده بود که دانشجوی دکتری است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/SorkhTimes/136829" target="_blank">📅 18:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136828">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SorkhTimes/136828" target="_blank">📅 18:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136827">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔄
🔄
ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم و این شرایط برای خودمان نیز آسان نیست؛
🔴
🔴
ما نیز میخواهیم هرچه زودتر تکلیفمان مشخص شود تا به فوتبال و آینده خود برسیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136827" target="_blank">📅 18:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136826">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/emOnL3qgPadRcFr7u2yo0Ythf3dkBFJMNLOBu5dvM6Y4PHUe-PwDsQAOhKbcHnFbFdlWivN4r1-G970qmkYEfenBhLjacVXhzdK7OcPmGoZ5cehWbZjH2htPUnbuO4nnMnuiExWjHVKYYCT2kpJ6nubf691jF5jW4EIGuqjqW7qSUXFSR1KrKA2EfPLgNjpdXRr_q8j4gUfXcTSoXNchMuQaTfpZLM_SIkI8jou7yfFAOBE70K04QcqSYB--Czitexh9MNGdl_FenHeP4KsnobOlEqoz6k6NkeIoEfm3kydLj1iiIbodc5F69fk9klvQA64psdK3-mnUxvRP7aIh8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
📸
آغاز یک روز پرفشار و همراه با انگیزه سرخپوشان در اردوی ترکیه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/SorkhTimes/136826" target="_blank">📅 18:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136825">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔄
🔄
استوری مشترک کسری طاهری و دانیال ایری برای هواداران؛ ماهم مانند شما بلاتکلیفیم و خبر قطعی و رسمی نداریم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/SorkhTimes/136825" target="_blank">📅 18:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136824">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🔄
🔄
گوهری گزینه ی گلری پرسپولیس نیست/قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/SorkhTimes/136824" target="_blank">📅 18:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136823">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SorkhTimes/136823" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136822">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136822" target="_blank">📅 17:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136821">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">⚪️
⚪️
⚪️
انتقال کسری طاهری به پرسپولیس فعلاً نه قطعیه، نه منتفی. سرخ‌ها علاوه بر دردسرهای قانونی مربوط به قانون «پل»، بابت مصدومیت رباط صلیبی قبلی این بازیکن هم نگرانن. پرسپولیس تأکید کرده بیشتر از ۷۵۰ هزار دلار برای طاهری هزینه نمی‌کنه و تا وقتی از نظر حقوقی…</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SorkhTimes/136821" target="_blank">📅 17:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136820">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">❌
باشگاه استقلال پیشنهاد 5 میلیون دلاری آسانی رو قبول کرد و این بازیکن شنبه به ایران برمیگرده !!!
😕
😕
😕
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136820" target="_blank">📅 17:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136819">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
پرسپولیس و تراکتورسازی پشت پرده توافق کردن که پرسپولیس بیخیال قربانی بشه و تراکتور هم بیخیال محبی تا باشگاه های اماراتی بازار گرمی نکنن و مبلغ رضایت نامه رو نبرن بالا
😐
/ فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136819" target="_blank">📅 17:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136818">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
🔴
🔴
انتقال دانیال ایری به پرسپولیس نهایی شده است.
❌
اما جذب کسری طاهری هنوز قطعی نیست و نهایی شدن این انتقال به حل مشکلات حقوقی بستگی دارد. //خرمی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SorkhTimes/136818" target="_blank">📅 17:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136817">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❌
❌
محمد قربانی: پرسپولیس و تراکتور مرا میخواهند/ مبلغ رضایتنامه‌ ام ۲۰۰ تا ۳۰۰ میلیارد است
🔴
🔴
بهتر بود نام تیم نیاورم، اما حالا که سئوال میکنید، میگویم. هم پرسپولیس و هم تراکتور با من و باشگاه الوحده مذاکره کرده‌ اند و در نهایت باید ببینیم ظرف روزهای آینده…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/SorkhTimes/136817" target="_blank">📅 17:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136816">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/SorkhTimes/136816" target="_blank">📅 17:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136815">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">😳
😳
😳
😳
😳
😳</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/SorkhTimes/136815" target="_blank">📅 17:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136814">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قدوسی اعلام کرده یک مقام از باشگاه منتفی شدن دانیال ایری و کسری طاهری رو رد کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/SorkhTimes/136814" target="_blank">📅 15:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136813">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136813" target="_blank">📅 15:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136812">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">📎
📎
📎
یه سوال پیش میاد اگه واقعا حس میکنید هنوز تو دفاع راست مشکل دارین پس عیدی چرا جذب شد؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136812" target="_blank">📅 15:16 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136811">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136811" target="_blank">📅 15:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136810">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nfbagmarkHdNWGlMGtIx9hwM6pMozMugR0z5FVOvReT_CQhMBarO6IcOA0vnkReAD2mN1iR9ofjJPcKPlndGECFRUC9XLBi4mLpMQS1E3epX-Zkh2iPDeQIL-v5akZIKI-o9oVNeyY8-emX2WYwCSn3h2yiCBfWW1_URfWxh22-I2KLiLJwWvzIguyWZfPuwr4FLiMnVUor_TGFfJigMxGxm90J-MJAcFJMauCux8HhPS09-lLjrV57BOW8HLYIRhX1Jv7jv2RQy-SwOTcx8PBzXXZsxOS3WrYU29VOjJlcbEaaGu7wIa6X7hTmPS3VcufDSqiZzVqf2KRJ-PPqrxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
کاظمیان به گل‌گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SorkhTimes/136810" target="_blank">📅 15:10 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136809">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SorkhTimes/136809" target="_blank">📅 15:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136808">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⬅️
⬅️
⬅️
حسین پنبه‌کار:
🌀
شهاب زندی از صبح در دفتر باشگاه استقلال حضور دارد و مراحل نهایی جذب دو بازیکن جدید در حال انجام است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/SorkhTimes/136808" target="_blank">📅 15:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136807">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
⚪️
🔴
#فوووووری
⚪️
⚪️
منتفی شدن انتقال کسری طاهری و دانیال ایری به پرسپولیس
🔴
🔴
طبق پیگیری‌های ایسنا از مسئولان نساجی، مدیران پرسپولیس حاضر به پرداخت مبلغ درخواستی از سوی مدیران نساجی برای انتقال این دو بازیکن نشدند تا انتقال آن‌ها به پرسپولیس منتفی شود.
🎗️
«سرخ…</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/SorkhTimes/136807" target="_blank">📅 15:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136806">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fg33KppGS8jU2s6h-FfI5hX3zNDmY5lwsqrCsgTOq3s0YXVyT3-wfsqhsaKENzEJIRgnVZ9NVvOm-QUZSACOMLsLWh6p452Y5-a4678_sJ8ordIJ8wJe6Z6HzUV2MmF-BIw18Qq_8g83OceWkA0tVdLIXt7nO2pfQzWRjRIv3MffHDBEpzLjOSoXJ768S6ALL3hLopAemdy79ZM1PpDG6-tqqt4pu13QD_kCSYjxR5YMc8EBcG_1MkvMl0bcvS8Ebs9x28DnRh5S0AXHgdQOP1cwVLDSf1vGW81yDL5fst4YlVKmL6ptSvkwvNcWXp5osDpwzuCCfff_pREIyuQt3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕹
وقتشه پوکرو حرفه‌ای بازی کنی!
🎰
اگر به دنبال تجربه‌ای متفاوت و پر از هیجان هستید، بخش کازینوی وینکوبت بهترین انتخاب برای شماست. از بازی‌های کلاسیک مانند بلک‌جک، رولت و باکارات گرفته تا صدها اسلات جذاب با جوایز بزرگ، همه چیز برای یک سرگرمی حرفه‌ای فراهم شده است.
🕹
همین حالا وارد دنیای کازینوی وینکوبت شوید و هیجان واقعی را تجربه کنید. شاید برنده بزرگ بعدی شما باشید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/SorkhTimes/136806" target="_blank">📅 14:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136805">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">❌
❌
❌
باشگاه نساجی گفته از اقدام پیمان حدادی به شدت ناراحت شده و میخواهد دانیال ایری و کسری طاهری را به باشگاه های دیگری بفروشد
😀
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/SorkhTimes/136805" target="_blank">📅 14:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136804">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
پرسپولیس میخواد رفیعی رو برای بازگشت راضی کنه؛ کاری که خیلی سخته چون امیررضا میخواد جایی باشه که بهش بازی برسه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136804" target="_blank">📅 14:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136803">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
شنیده‌ها: با توجه به عدم جذب اخباری احتمالا یا رفیعی برگرده یا گوهری که بازیکن آزاد جذب بشه
🚨
پ.ن: برای گلر دوم رفیعی یا گوهری هم جوابه بعید برن سراغ گلری که قرارداد داره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/SorkhTimes/136803" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136802">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
🚨
باشگاه تراکتور پاسخ هایجک محبی رو به پرسپولیس داد و محمد قربانی تا ۷۲ ساعت دیگر تراکتوری میشه/ ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136802" target="_blank">📅 13:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136801">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
به دلیل تعلل مدیران باشگاه پرسپولیس در جذب کسری طاهری و دانیال ایری حضور این دو بازیکن در پرسپولیس از سوی شهاب زندی مدیرعامل باشگاه نساجی منتفی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136801" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136800">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">✅
🔴
پوریا لطیفی فر ستاره 22 ساله تیم‌گل‌گهر با عقد قرار دادی چهار ساله رسما به پرسپولیس پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136800" target="_blank">📅 13:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136799">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
به دلیل تعلل مدیران باشگاه پرسپولیس در جذب کسری طاهری و دانیال ایری حضور این دو بازیکن در پرسپولیس از سوی شهاب زندی مدیرعامل باشگاه نساجی منتفی شد /ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/SorkhTimes/136799" target="_blank">📅 13:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136798">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136798" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136797">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136797" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136796">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
🚨
عجیب اما واقعی؛ پرسپولیس و سپاهان داداشی شدن و پیمان حدادی کمپ شهید کاظمی رو در اختیار سپاهان گذاشته تا اونجا تمرین کنن…!
☹️
☹️
🫥
ورزش سه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/SorkhTimes/136796" target="_blank">📅 13:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136795">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/az-mduWZOZqInKWXuxeOlzQT5VrVZUmJbAt_05HDKOxb5KZ6v0zMnhCEzcZd_DuoPqHBwd7Es7J0HKdbdILFFEO3Lrt06niCBABBn63EM7HTyLbw2AkwM_G_wQS8NPgyG0TdlvXWd58FyJVJmL4AQ-1_cWknMmxckk9tjQv1o4kvH8IS1iNRRECKmQNJgKuriCofqUlOahLz3-frm_E9A7fk5kO_bfRya2pF538XGzU-UmYVUsyRQp7meYZK5A2hTnTfuXyJmlJPNRtJs1PrRsyqQlHJHIVP_1scl4E-IS9AIRLtTjjRM0c6psRH9r0JqdpM6yHixE258N9CJKQkUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
باشگاه سیرجانی با انتشار تصویری از محمدرضا اخباری به صورت رسمی اعلام کرد این دروازه بان با قراردادی دوساله به گل گهر پیوست.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/SorkhTimes/136795" target="_blank">📅 13:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136794">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">❌
❌
#ورزش‌سه : ممکن است به زودی یک قرارداد معاوضه به اضافه پول نقد بین دو باشگاه پرسپولیس و سپاهان شکل گرفته و احتمال دارد نام‌هایی مانند محمدامین کاظمیان، حسین ابرقویی و آریا یوسفی در این معامله جای پیدا کنند. حتی احتمال رخ دادن این اتفاق برای محمد عمری نیز…</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/SorkhTimes/136794" target="_blank">📅 13:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136793">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVEQQDQhJnZq0u1xolrNzN_nVjfn2WfDiZhquTaTQ_GOOLsTUPUHB5R0htsw0iLybJJ_FwmecWXkaMIblzef6FW8ZtorXD7sUKS_BqbQToYwh2skcEY0XdXVJ0U2K5OmMphxQ5BC_vIrgqzjZPTLlwnffK5FpmiEm2CQfzajSmW4gsY0ZWiL6xTk1x3UzwikbdSEL2XdUmx_sa_FD5XINEjDIuZuNXZJ4DPgSogecE_fpb3vwtKf6HPFvnyiUkYYM0_1gKg9Sh3tneOGcvj51GeTcCVD2dsM5hSGMCHFi41x3fBQcxivOcW1Fve6ZwI7P4DlWbVgl3e6L2kRqlPdfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
فوووووووووووری :
محمد قربانی به تراکتور پیوست!
😐
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/SorkhTimes/136793" target="_blank">📅 13:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136792">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">➡️
➡️
➡️
➡️
⬅
تارتار به دنبال پاکسازی پرسپولیس!
⏳
💬
مهدی تارتار پس از بازگشت از ترکیه قصد دارد چند نفر از اطرافیان باشگاه را به دلیل لو رفتن ترکیب تیم کنار بگذارد.
⬇️
سرمربی پرسپولیس به چند نفر مشکوک شده و پیگیر این موضوع است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار…</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/SorkhTimes/136792" target="_blank">📅 10:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136791">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
🔴
ورزش سه: هیچ کدوم از هافبک های پرسپولیس بازیساز نیستن و دو خرید جدید پرسپولیس در این پست (لطیفی فر و پورعلی) بیشتر وظایف دفاعی دارن. پرسپولیس اگه پست 8 بازیکن نخره تو شروع فصل به مشکل میخوره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/SorkhTimes/136791" target="_blank">📅 10:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136790">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">❌
❌
❌
امیر عابدزاده که به تازگی بازیکن آزاد شده و احمد گوهری از گزینه‌های باشگاه برای گلر دوم می باشند ناگفته نماند وضعیت اخباری همچنان مبهم است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/SorkhTimes/136790" target="_blank">📅 10:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136789">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🌀
🌀
🌀
پرسپولیس خواستار جذب مدافع تراکتور شد
🌀
باشگاه پرسپولیس با ارسال نامه به باشگاه تراکتور خواستار جذب صادق محرمی مدافع تیم فوتبال تراکتور شده است.
🌀
محرمی پیش از این سابقه بازی در پرسپولیس را داشت و از همین تیم راهی دیناموزاگرب کرواسی شد.
🌀
باشگاه تراکتور…</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/SorkhTimes/136789" target="_blank">📅 10:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136788">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">❌
صادق محرمی درخواست خروج از باشگاه تراکتور را داده و قصد ندارد فصل آینده در این تیم باشد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/SorkhTimes/136788" target="_blank">📅 10:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136787">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">✅
گل پرسپولیس به تیم مصری توسط بیفوما
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/SorkhTimes/136787" target="_blank">📅 09:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136786">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">❌
فرشید حقیری: یاسین سلمانی دیروز پشت دروازه تمرین کرده و احتمال زیاد می‌ره مازاد تارتار
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/SorkhTimes/136786" target="_blank">📅 09:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136785">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">❗️
❗️
لیست تیم ملی امید اعلام شد.
❌
در این لیست 4 بازیکن از پرسپولیس به تیم ملی امید دعوت شدند.
🔴
امیرحسین محمودی
🔴
علیرضا همایی فرد
🔴
سهیل صحرایی
🔴
فرزین معامله گری
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/SorkhTimes/136785" target="_blank">📅 09:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136784">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">❌
❌
خبرنگار پرسپولیس:
🔴
امروز محمدمهدی زارع و پویا پورعلی در تمرینات عالی ظاهر شدن .تیکدری هم مثل همیشه خوب بود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/SorkhTimes/136784" target="_blank">📅 09:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136783">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
🔴
گزینه بعدی پرسپولیس برا گلر دوم گوهریه آماده س ولی برخلاف اخباری سهمیه لیگ برتری  حساب میشه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/SorkhTimes/136783" target="_blank">📅 09:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136782">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od0sEAsCxWVjr96cb4t46CpnJgBP0O67ic4PkuCajWGA8hwCwDh1SruY18v8jT8krqSt563us_04_cYXOAV08x6iK6-x0VEh36eVn9qgNLnNjp3VoULLzdTxIC892CBiTeGlWiR-x1CYSIffx4iHnAga3kGcEN9Xs6siG-30kR1BvQqftKvlI_XElZWhlsrAOQJv1SEIYbQaVHTfLqdon6XBtmVoCYAryT8BfKR107k6iA0OS3yI_SdDKoZfevXs-jgwNb-nYSr17CoqxZJqC5ZSoKSUPQ5flhfR63ZNK5Hd4-C5puBa-BxlQhRhclrTxKepkReub1iJFEpuX-KfJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کریم باقری : پرسپولیس فصل گذشته مشکلات زیادی داشت و من خودم شخصاً جزو کسانی بودم که از عملکرد و نتایج تیم راضی نبودم اما نسبت به فصل آینده امیدوارم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/SorkhTimes/136782" target="_blank">📅 09:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-136781">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GuPcqf7J_aDVqiEB1XaEpcGj9TMvS8dt7fjZZE0AZs0OpJ37wc_IR9436ff9yfEEEkulp3C5drC53vlgTEb3CZRKgFjO9E90QPuMxrqI-coKiAT7_roTo0O-xnUQR-2P8pGJg2CLRnAszajYPVAdW2LcZmrOREYyW4rzbItJ0z9_W1H2E-dDSFbZIbzEq3lj-b6wAwAi0Ae1Rl19Yak3CiF4Yr1v-QhDLTecOd-yCDQi3_Z-IC6WS9bwVJoevkxvesOhiNi1hhS5GfDFHJdRwZxFgbtMbl-HVZowN_XH3Nwjh5ZhMOu3sC5Uc8mGEe_j-PzKrLdTNHkXhP4_dI8hxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
✅
صبح 5/5/5 تون خوش ارتش سرخ
❤️
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/SorkhTimes/136781" target="_blank">📅 08:10 · 05 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
