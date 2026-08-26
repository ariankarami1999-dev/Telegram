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
<img src="https://cdn4.telesco.pe/file/TmjqJV9Vm65Fbi0qiDGJyqcQ7-p2v6ntmxbg_ICOybzlmVdjrS_IkB7cUo-l7KGc1kifEZjT8QHzjWhsffoof6e1R24m8M6IrQFW0_CwDe5R-ZQBCU9H4BeNh55Upd43kCShBFMbgCmBZHuQpNxve4hx7ST9yzh8rZCjihySMSA0jWTsing9Og8H-145I8EZ5ikmluXfDIlBQBFh841Ubuy7mboGAbogm0MIZBCgqGNNTjw-vfgLvIlj5ijOOvFOb1YAlm4GGuWH2_qYcJJDqxta5XsdlX4mKVk41LGtiwXGRZy9jsLBOHWNCQBtGCt0iYzu_Nc_lKrcm_JdeJmqKA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.41M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 21:39:48</div>
<hr>

<div class="tg-post" id="msg-684568">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
معاون اجرایی رئیس‌جمهور: توزیع بنزین در کشور عادلانه نیست
قائم‌پناه:
🔹
طبیعی است باید تغییراتی در نرخ حامل‌های انرژی انجام شود اما میزان و زمان آن را باید در گفت‌وگو با دست‌اندرکاران تعیین کرد.
🔹
توزیع بنزین در کشور عادلانه نیست؛ فردی که چندین خودرو دارد از یارانه استفاده می‌کند و افرادی هم که خودرو ندارند از این موضوع بهره نمی‌برند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.32K · <a href="https://t.me/akhbarefori/684568" target="_blank">📅 21:37 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684567">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ادعای
جان مرشایمر استاد علوم سیاسی آمریکایی: ایران به امارات پیام داده است با آمریکا همکاری کنید شما را به خاک سیاه می نشانیم
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/684567" target="_blank">📅 21:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684566">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/684566" target="_blank">📅 21:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684564">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pvn4xV4n9MalpZ_tTZYX38JVCiytyL5HmkKuPR9swNIm1x7XUSGqxIjKibKKTyjbfGzV7cJcb1JXxckoR77m4mECKtMQGH8aky2WYTdGnOT2WBiP7v3em9MFbWcaK8LDgHHaDpbcCJ6u0aCU1urvZQwdQC2BYphZn4JbxwYLuC9fPg9qgWtZDte7klXkRsADtlq_n0vtM0hPRCyKiNUcgUIufSEs9fZZXkiM1ZCPZ7D5UVRdi3T86R0yCWxDZSDlTSQ78eNaUTMDQrN3B0wxeZ99kbkFcas0MMan4X46sQeFSAGiU-Sg37SxbzFbmj_Lyo_8-iuhcBBnjYTY_bhPVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WbC_MADNvU2QvFViQKfsgG2WWPQBZZIrZ1PMFApPymyAQH73JtDkPLImg2P-ujWm556KsaiPkHIgw6uzQltM7fPWpSD2RcBJG5DttovjFWiIK-YH8A1Ds4tr1JcQdOk8aI8dfx2cleSHnKPPY90aLwxFw-E1-10A3n98bVfbg7r4fKwvkjyl4qR0IP3vFTrUsrGtXpy312GkeZBPdLAd90oMXCh3wu0b6xwcIOnlD3lDVT3V67F6K7WnO26sq1ERH8U3z7ayaLSW6J-6UBxxXpmoDjpcppDJEhOvv4LaKJS_gZKPXGxSfu-IaAybR9qC78v9NHyY-90zPWISlHDMNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
سفر ۳ هزار کیلومتری با گیوتین؛ بازداشت شهروند معترض آمریکایی در نزدیکی کنگره
🔹
پلیس کنگره آمریکا مردی ۳۵ ساله اهل کالیفرنیا را که یک دستگاه «گیوتین» واقعی را در پشت وانت خود قرار داده و پس از طی کردن سراسر خاک آمریکا، آن را در نزدیکی ساختمان کنگره در واشنگتن پارک کرده بود، بازداشت کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/akhbarefori/684564" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684561">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c470460c1.mp4?token=g6M1LiL05I9eKpIv-SaiQLmdohQVjMqvSl5nPt14F_4E7yc7a7TKh7M63tnv_JHBcr42psGapQ53aIDn0nqy71RwlPNRvd3p-WPij_wbGtkKsF1GCmQvERcOPbRwGmvjasSJOkJiI7PjNHTfh6ThtU110ObeEuhExinLAd1we1EhWxqNJbSUzYr9rJNAEj3rvSR7Y03JIabw9N7ndmp0pLjLNzXb5vsUxwBJWblBYGvznMtJG3T7THDeKooraNPNxBlyAJ0VWiIkJtGUxj_U9bn46SPctiG0IU03baXmZP3mzSKVfh5h7XBPVSTAl1fUMItkA8JDKddVo6OYuXLYBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c470460c1.mp4?token=g6M1LiL05I9eKpIv-SaiQLmdohQVjMqvSl5nPt14F_4E7yc7a7TKh7M63tnv_JHBcr42psGapQ53aIDn0nqy71RwlPNRvd3p-WPij_wbGtkKsF1GCmQvERcOPbRwGmvjasSJOkJiI7PjNHTfh6ThtU110ObeEuhExinLAd1we1EhWxqNJbSUzYr9rJNAEj3rvSR7Y03JIabw9N7ndmp0pLjLNzXb5vsUxwBJWblBYGvznMtJG3T7THDeKooraNPNxBlyAJ0VWiIkJtGUxj_U9bn46SPctiG0IU03baXmZP3mzSKVfh5h7XBPVSTAl1fUMItkA8JDKddVo6OYuXLYBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بحران محبوبیت ترامپ در ایالت‌های رقابتی
🔹
براساس گزارش شبکه MS NOW، نرخ خالص محبوبیت دونالد ترامپ در ۴۷ ایالت از ۵۰ ایالت منفی است.
🔹
همچنین در آستانه انتخابات میان‌دوره‌ای، نرخ خالص محبوبیت ترامپ در تمام ایالت‌هایی که امسال رقابت‌های انتخاباتی سنا در آنها نزدیک و رقابتی است، منفی است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/akhbarefori/684561" target="_blank">📅 21:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684560">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3sE8Pus2PD5IKElanlshzJ81EcFMhhASsf1nyWfx-uBTUSEX-5ShAnjQKFjh0fkMJCEmIol42E2BABVQbHR3mx9P65j_6Zf0DaVnkw1StWC1i__2LGq311nahA7OVdvlZn3rLfqjIuOe5m4Nox2yxpL5rtUN-GxsBjaCfVSXBTrBeyFSaBgoVd2k3NmoRhCqOc9t77p-OF-7YjE1VZoFVIVq0y0BNlTWE4dN9MfVeansWMPnl1mXiRa9N6G-KzF0d0OYKZKcqYxhEvwKnOQeNEzV_GqZDangFy9-XegAZFvDjZMbKd-PbpcQ_We6Xih6datnuuCZsrqFCbfftvrFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اگر ایده‌ای دارید، اما توضیح دادنش به هوش‌مصنوعی با متن سخته با ابزارِ Squig می‌تونید خیلی سریع یک طرح اولیه از ایده‌تون بکشید و همون رو به هوش مصنوعی بدید تا بهتر متوجه منظور شما بشه  #هوش_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/akhbarefori/684560" target="_blank">📅 21:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684559">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aee581b45.mp4?token=NemLjInteKP7VMRd7p3A6WFt-MfVjPmrIBV5nM1b-P7fBU_AwMPb7zitk8FwYBMF9gTgEvykE6G4dTnb3cqqVOLdS7SIW2H-4O3gaXn3sSKLKrIYjt5omPzp8p9ieaYDb-qcTfLCl81Bsp5P65vDjenZ6JCfvS5yD5-XjA3UbS8LXjZ3NheiY-tY-buhizndfaOD6ZIxByIgOCH3767fNDAX3lGG1l93M-JDgieINhYSTBYgnCXRfZhYUpzvEWxe6vtnthyVSvQ795mpo30gxYOLKxvhwTTQ8BVfUrYb5wtnl4sP2qfP-3rPPmAAqB9LMseL5tCc1ve-xjrGh_gWpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aee581b45.mp4?token=NemLjInteKP7VMRd7p3A6WFt-MfVjPmrIBV5nM1b-P7fBU_AwMPb7zitk8FwYBMF9gTgEvykE6G4dTnb3cqqVOLdS7SIW2H-4O3gaXn3sSKLKrIYjt5omPzp8p9ieaYDb-qcTfLCl81Bsp5P65vDjenZ6JCfvS5yD5-XjA3UbS8LXjZ3NheiY-tY-buhizndfaOD6ZIxByIgOCH3767fNDAX3lGG1l93M-JDgieINhYSTBYgnCXRfZhYUpzvEWxe6vtnthyVSvQ795mpo30gxYOLKxvhwTTQ8BVfUrYb5wtnl4sP2qfP-3rPPmAAqB9LMseL5tCc1ve-xjrGh_gWpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
تولید و پخش پلاستیک آریا
🚨
🚨
به‌دنبال تأمین‌کننده‌ای مطمئن با قیمت رقابتی هستید؟
پخش پلاستیک آریا، عرضه‌کننده عمده انواع محصولات پلاستیکی، ظروف یکبارمصرف، لوازم بسته‌بندی و اقلام پرمصرف بازار با تنوع بالا.
📍
تهران، خاوران، جاده امام رضا، ورودی فرون‌آباد سوم، مجتمع پلاستیک پایتخت، پلاستیک آریا (کیانی)
📦
فروش و همکاری به‌صورت عمده
🚛
ارسال به سراسر ایران
📞
مشاوره و ثبت سفارش حضوری، تلفنی و آنلاین
☎️
09129628810
☎️
09129680633
☎️
09128063394
📲
جهت مشاهده محصولات و ثبت سفارش
به اپلیکیشن های ذیل مراجعه فرمایید.
لینک کانال روبیکا
👇
🆔
@pakhshariyaa
لینک کانال تلگرام
👇
🆔
https://t.me/pakhshariya1
لینک پیج اینستاگرام
👇
🆔
https://instagram.com/pakhshariyaa/</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/684559" target="_blank">📅 21:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684558">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBimebazar</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/THMqNsh5FryELkDapnN08Q0s52pyyfhNeLXSt86qIaJu4y_Ghbh1RG5l7u3w7ZITylYRaylNUporHHLgV5zGnVWM_1m3OcXwitMvxzA9xLyVe7cJXLwmUeqJEg5R3ivqHR-YPMGpE7xDZDqAZiRBgHoeTgHtHmOJeZo17RfIc_QPmO_3wT7yArpCSQy1JnqzIj-vKN1EvZP6ddbrdjxClrc9OXXqWB7l8Mh7_LDpa3OG_K0qImdnmuW9vUIOJj2myyCY3tABHsTJiwMKkfCHJ3_ApcL28L9x1LS-5lNUV8JHL0-bA51lPqS9Rf6ZCTYbtDjvXyusZTNZHSoqEbeoRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
بخشودگی ۱۰۰٪ جریمه بیمه شخص ثالث!
📢
طبق اعلام بیمه مرکزی،
از ۲ تا ۱۳ شهریور ۱۴۰۵
✅
تمام جرایم دیرکرد وسایل نقلیه فاقد بیمه،
به‌طور کامل بخشیده
می‌شود!
فقط کافیه در این بازه زمانی، بیمه‌تون رو تمدید کنید.
✔️
تا 2میلیون تومان تخفیف با کد
pnsc
👈
تمدید بیمه شخص ثالث
#بیمه_بازار
🟡
@bimebazarco</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/akhbarefori/684558" target="_blank">📅 21:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684557">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
ادعای اکسیوس: زیردریایی‌های بدون سرنشین ایالات متحده تنگه هرمز را اسکن کرده و بیش از ۱۰۰ شیء مشکوک به مین را شناسایی کردند
🔹
ارتش آمریکا با شرکت‌های خصوصی برای پاکسازی یا انفجار مین‌ها قرارداد امضا کرد.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/akhbarefori/684557" target="_blank">📅 20:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684555">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JtyPGJEyIP0bG2g7VGv_o5Yf-ZVosEM5rVDyBOqVg6rlv_hwMGdGnGhtaU_yR-zLiNq1fsGOIg_lTPNM2T24uiwDQkbEgp0cHH_LA78DhysMfj3y2ywc7PmBrMZ4BGhvPqL8J9x5xT6okBrpl3xoUcf6f4h0u63wN0c9ONNpbxM79NQPPXvmsplFR7NEtsRzBl8QQvpx0bC_p7pt252vNJOBCW3RhEEtJKxCz86Dv5KMs9hw8jR9ZnldiE7_IbpWvF1PLL485ApEQZsBBU3EPAGxIKh2cDMvtE9_zavvassujmH8fXVqsCSLlf-OKrhgT6F69LLVAKNKIXCH2CRWMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فحش و فحش‌کاری اپوزسیون علیه یک دیگر / علی کریمی "گله" را بهم ریخت!
🔹
همزمان با انتشار استوری جدید علی کریمی، موجی از فحاشی و توهین از سمت سلطنت طلب ها علیه وی به راه افتاده است.
🔹
علی کریمی، اپوزسیون را "گله" و رضا پهلوی را "یک احمق" توصیف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/684555" target="_blank">📅 20:47 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684554">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VB690XZpMhR_rrTJ0KRmCep3YaUT_ZfPTdFTVGQhhkuJ3bRjTYB2ZGpzjKTkntqLP9vN2tCtPXr2ULRcjrMoaI772vwFhIW24AO_23rnHExPqTm2xO5AItq9v4oPMdAzBvRDMER_Mb8sRrTGz2sdOZ9EKi2m5ITmholYuOQXFbkNxWEKP8ldI-gveBjm4Pbv9QoTpsx_QyOCqENQPwl2RsKqskm86aJI-AObnLwoT4Ava9CZFoDJJF40psO5yr0uWWtbRtyHtHPrJkX9mRH25l3KIBfe89gNLlOv2t4E5F60flcDLwNAI-YEDErykF2UnQsQGni2VLGdzJII3LAtfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رهبر شهید انقلاب: زندگی و شخصیت بی‌نظیر پیامبر اکرم(ص) برای همه‌ی دوران تاریخ اسلام یک درس و الگوی همیشگی است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/684554" target="_blank">📅 20:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684553">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
کشف بدافزارهای جاسوسی در تلفن همراه رقیب انتخاباتی نتانیاهو
🔹
خبرنگار شبکه ۱۲ تلویزیون رژیم صهیونیستی در گزارشی فاش کرد که نرم‌افزارهای جاسوسی در تلفن‌های همراه کارکنان و مشاوران ارشد ستاد «گادی آیزنکوت»، رئیس پیشین ستاد کل ارتش اسرائیل و رقیب اصلی نتانیاهو در انتخابات پیش رو کشف و شناسایی شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/684553" target="_blank">📅 20:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684552">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e27096761.mp4?token=XObt8V5AupasvTvP54p7ZqrEZM23Rj-5TNTaNw8ZWcnf9cpqkHf0g6swUHwoZSOkbuE9Upd5VOVzs936doQq3S1KvwJ3w7MGyG1ZBIQu15J_LTg8NUeV_C8nScWv1ha7Unvcrj6QCISQL0zwUNnERgZv0Jf56ySQJTQGvx-QSCF5Yje1uxQdDAZHmzk7ZlpafK2KZA_12IvWKSXDmthdxJIxQunNF6ZfuLUr1SL0sx2KbSQY8MSwyGqik9dgBOyBoiii7GrEJfSrwvg2uld-2yHZxXgXfYar3Qzc3uFqbttNNrKYyAtgnzcrAlLRUOKnDLP72HwaF1Glgut4oRr4lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e27096761.mp4?token=XObt8V5AupasvTvP54p7ZqrEZM23Rj-5TNTaNw8ZWcnf9cpqkHf0g6swUHwoZSOkbuE9Upd5VOVzs936doQq3S1KvwJ3w7MGyG1ZBIQu15J_LTg8NUeV_C8nScWv1ha7Unvcrj6QCISQL0zwUNnERgZv0Jf56ySQJTQGvx-QSCF5Yje1uxQdDAZHmzk7ZlpafK2KZA_12IvWKSXDmthdxJIxQunNF6ZfuLUr1SL0sx2KbSQY8MSwyGqik9dgBOyBoiii7GrEJfSrwvg2uld-2yHZxXgXfYar3Qzc3uFqbttNNrKYyAtgnzcrAlLRUOKnDLP72HwaF1Glgut4oRr4lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مطالبات مراکز درمانی کی پرداخت می‌شود؟
وزیر رفاه:
🔹
سازمان برنامه گفته از شنبه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/684552" target="_blank">📅 20:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684551">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezMgItWX7x2qxX8uqXq0LMJ_W-Up6XfbB8HPUk4-IQIhFpJCzS4A1Rgj7_kssmjZnGJxWGyL-apxA3YP6Npe0R-hTz9tu6f-NBGnNc0OvlIIXNDm6SJvID-0_KBrTNvhWqdkwWU2hkxzGkxmFfGvBy7VIF773m7Dns1ndgv3tcu12sK-W-dDOc7cbKI0F1lvmrfT2EuGlsVGeMntL7rQSgbsMRQxttw2C3qU0jhxZxPztoyYNMSCYR6avqG0JHgqk47F4KXZ2L4WDMtiN2s9rX0sJfUh-rPVI8uhUZoyFSPbDKSvhhj4RHOUoa3DLX_V3tW3os5qISBk5PfpkpIrXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فحش و فحش‌کاری اپوزسیون علیه یک دیگر / علی کریمی "گله" را بهم ریخت!
🔹
همزمان با انتشار استوری جدید علی کریمی، موجی از فحاشی و توهین از سمت سلطنت طلب ها علیه وی به راه افتاده است.
🔹
علی کریمی، اپوزسیون را "گله" و رضا پهلوی را "یک احمق" توصیف کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/akhbarefori/684551" target="_blank">📅 20:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684550">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
نامه عراقچی به سازمان ملل و دولت‌های عضو درباره تروریسم اقتصادی آمریکا علیه ایران
🔹
وزیر خارجه ایران در نامه‌ای خطاب به دبیرکل سازمان ملل متحد، رئیس شورای امنیت و اعضای سازمان ملل متحد، ضمن تبیین مواضع ایران درباره «عملیات تروریسم اقتصادی» آمریکا علیه ایران، بر مسئولیت قانونی و اخلاقی سازمان ملل و کلیه دولت‌ها برای محکوم‌کردن اقدام غیرقانونی و مجرمانه هیات‌حاکمه آمريکا تاکید کرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/684550" target="_blank">📅 20:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684549">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: سفر رئیس سازمان سیا به روسیه ربطی به ایران ندارد
ترامپ:
🔹
سفر رئیس سازمان اطلاعات مرکزی آمریکا (CIA) به روسیه ربطی به تحریم‌های ایران یا احتمال حمله مسکو به انگلستان ندارد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/684549" target="_blank">📅 20:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684548">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3fTomJ3Vlz_qDjzTSOWKpjtPKa4p6hvgxOqDNzVhdOe3oZbrV2yBxhAUR-1t0CKqJENwsWSGmwyMEl2r62NTe_K-fcuyI-iUdXB15WwlXwP8UH_6tQZWqMwhnWHkxrnAqwox2GLPwYNvVK4Y-T0IBHsJS64zF01Lx9n2cWudPJSCH9Y86kOkGdElj39R3GnwAiYdhep5J0YD3b-L3YvbGMewfntG9Rs9erqt-gZXKJ4Z9NAw7JzIywTxNLJqq8ntaPS_tDBJ4DRlZxvXehdFeIS8AEuTVt4hiH7abl5z38DMBEbKJF5s5jr_sc2ToEV3KP4UENzneLWPYLOFlFCxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صندلی‌های سینما و تئاتر، خالی‌تر شده‌اند؟
🔸
در این نظرسنجی بیش از ۲۴ هزار نفر شرکت کردند که سهم روبیکا ۵۰، بله ۳۰ و تلگرام حدود ۲۰ درصد بوده است.
🔸
بیش از ۳۶ درصد شرکت‌کنندگان، کیفیت پایین آثار و حدود ۲۶ درصد هم رونق شبکه‌های نمایش خانگی را از جمله مهم‌ترین دلایل کاهش استقبال از سالن‌های سینما و تئاتر دانسته‌اند.
🔸
به نظر می‌رسد تغییر رفتار مخاطبان و کاهش جذابیت تجربه سنتی تماشای آثار نمایشی، از مهم‌ترین عوامل کاهش حضور مردم در سالن‌های فرهنگی است.
@amarfact</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/684548" target="_blank">📅 20:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684547">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
مسکو: اسرائیل هیچ برنامه‌ای برای خروج از غزه یا بازسازی آن ندارد.
🔹
آمریکا: مذاکرات لبنان و اسرائیل از سر گرفته خواهد شد
🔹
سی ان‌ان: چین تحریم‌ها علیه ایران را نخواهد پذیرفت
🔹
معاون علمی رئیس‌جمهور: سکوی ملی هوش‌مصنوعی که توسط دشمن هدف قرار گرفت را یک‌ماهه بازیابی کردیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/684547" target="_blank">📅 20:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684546">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">05 Ane Manaee (1403-08-10) Marghade Sheikh Sadoogh</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/684546" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه پنجم
حجت‌الاسلام امینی‌خواه:
🔹
دوگانه‌ نور و ظلمت در سوره محمد: سبکی نادر از تقابل ایمان و کفر [03:10]
🔹
از در هم‌‌پیچیدگی دل تا آرامش بال؛ خداوند چگونه تشویش مؤمنان را می‌زداید؟ [06:30]
🔹
همراهی خداوند با سالکان راه حق؛ برداشتن خطاها و بخشش لغزش‌ها [07:40]
🔹
الگوریتم‌ مغفرت الهی؛ کافی است مانع نشویم! [12:40]
🔹
حال خوب؛ وعده الهی برای رهروان مسیر ایمان [16:50]
🔹
حال خوب در راه عشق؛ هر قدمی برای خریدن لبخند محبوب [26:58]
🔹
ادخال سرور واقعی؛ هدایت دل‌ها به آسمان، نه خنده‌های زودگذر [35:30]
🔹
حق، مانای بی‌کم و کاست؛ باطل، میرای پر کم و کاست [59:05]
🔹
ملائکه و بیداری‌های سحری؛ از حاج آقا مرتضی تا مرتضی پاشو! [01:19:00]
🔹
زیارت با هدیه؛ شیخ صدوق به تاجر: صلوات بفرست و دست پر به حرم برو [01:25:00]
🔹
به خاطر یک لحظه دلسوزی بر امام حسین (علیه‌السلام)، تا قیامت در امان ماند [01:28:00]
🔹
امید آخر؛ وقتی کودک شیرخوار به میدان عشق آمد… [01:35:50]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/akhbarefori/684546" target="_blank">📅 20:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684544">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bdacdec44.mp4?token=KoMhe7qZk3RHijijr2PXBGM7R7qBNOc9OTaTyWa4kxww49TplEBoq_MTR10xs6QlZ0AwhDvTrl3Ot932tuCgtaZk1MjZxJ081tjqTuqWRsGZ6JeUXxE8x_ljD-1cj4hRU0iMl9gDn22B_1MCw7pfUn2q6fTcknPoqOJF7nSGTUWh-fBCj0r7Mo4zCwCfYtMyP1uhQZPD6HqosVf-By4SpsAylMbW4J0w2sJl-dWhLmxfOSBz8K3w1qS9ZcVJjo1v9-TG2u1cwbkfe8j5zNXGvbOeyJVG2Dl5yQI4ruOtuDjz3nn-_FxU5EX3K7je2TFc9Ms2e0DA8oVblvF6NeLKUrqRxztStFEMOYdrEnRYsblfh_-sJ1gvxTOzU13AijVlpHn3bDXawT7XbhaM7_l6_hmaaEMN4FS5Dw1ZTRFDSx27vklQmtRhNRZTHFaH-wokFeE4cE2eABbrGibqSA1yjRqvDhla6TZLcaB_aZLsH_8ws4V9GPoCCJI38RnYSd7YqQ5boQ7WpCCAmTeDWHL1Et3vbZK4CZyCTjj4L5ju_T5hr91Ql5hUUTOCHoGsU-UHurhG-hEzM300yCQeYcAk09l8-o0dl-1lHosjvE8yo32vQpWaImHKSyD9VKDfyBqV1Gi5p25iygHwV3aewBlZ04MZJtezFCZfYhkl9RmgCVU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bdacdec44.mp4?token=KoMhe7qZk3RHijijr2PXBGM7R7qBNOc9OTaTyWa4kxww49TplEBoq_MTR10xs6QlZ0AwhDvTrl3Ot932tuCgtaZk1MjZxJ081tjqTuqWRsGZ6JeUXxE8x_ljD-1cj4hRU0iMl9gDn22B_1MCw7pfUn2q6fTcknPoqOJF7nSGTUWh-fBCj0r7Mo4zCwCfYtMyP1uhQZPD6HqosVf-By4SpsAylMbW4J0w2sJl-dWhLmxfOSBz8K3w1qS9ZcVJjo1v9-TG2u1cwbkfe8j5zNXGvbOeyJVG2Dl5yQI4ruOtuDjz3nn-_FxU5EX3K7je2TFc9Ms2e0DA8oVblvF6NeLKUrqRxztStFEMOYdrEnRYsblfh_-sJ1gvxTOzU13AijVlpHn3bDXawT7XbhaM7_l6_hmaaEMN4FS5Dw1ZTRFDSx27vklQmtRhNRZTHFaH-wokFeE4cE2eABbrGibqSA1yjRqvDhla6TZLcaB_aZLsH_8ws4V9GPoCCJI38RnYSd7YqQ5boQ7WpCCAmTeDWHL1Et3vbZK4CZyCTjj4L5ju_T5hr91Ql5hUUTOCHoGsU-UHurhG-hEzM300yCQeYcAk09l8-o0dl-1lHosjvE8yo32vQpWaImHKSyD9VKDfyBqV1Gi5p25iygHwV3aewBlZ04MZJtezFCZfYhkl9RmgCVU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس نپال: سیل مهیب امروز تاکنون ۷۲ کشته داشته است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/684544" target="_blank">📅 20:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684543">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sqv60PxvHOgYkZqrSUJ4onUgpE8EdWdVIczkVGbh8S4rN9pLacx6UmTQmCH2zgOgf2sW7GnjGJ4WFVQqXoAXN6Z3H3ciQWwGxxas2U3DpR81pC7wC7PMbzm-AiPTzHljQhrxLgLH-5HOVj7a1jgTDTHdZ_-TUL2PC4e9oUWkeLOzaW4CZGIayTtmivSETmlu0ozmB_MnEQmPX33YSRwbchB_Yq1P0GAMjj92cD-NhpPCeEFJ6_OHEmLWZWIAEjYVU482FJ-GQAMzD1pCc6FBn4TMK59WW8EsCRZfEHspfBleYmwvwLhuO-pUbbzJW6ODXs267RL0_Pe-3UxNdLEi1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چند ترفند کاربردی که بد نیست بلد باشی #ترفند_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/akhbarefori/684543" target="_blank">📅 20:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684541">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
اسلامی: بازرسی از سایت‌های بمباران‌شده منوط به مصوبات قانونی است
رئیس سازمان انرژی اتمی:
🔹
آژانس بازیچه آمریکا و اسرائیل قرار گرفته است. هرگونه بازرسی از مراکز مورد تهاجم نظامی قرار گرفته را منوط به مصوبات قانونی مجلس و تدوین پروتکل‌های مشخص است.
🔹
سازمان‌های بین‌المللی متأسفانه به ابزار دست نظام سلطه تبدیل شده‌اند؛ انتظار داریم اجازه دهند آژانس طبق اساسنامه و بدون فشارهای سیاسی عمل کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/684541" target="_blank">📅 19:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684540">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
قابلیت پولی دیگری از چت‌جی‌پی‌تی که رایگان شد
🔹
چت‌جی‌پی‌تی استفاده از ابزار ارتقایافتهٔ زمان‌بندی وظایف را برای حساب‌های رایگان هم فعال کرد.
🔹
این قابلیت که پیش‌تر فقط در اختیار کاربران پولی بود، به کاربران اجازه می‌دهد درخواست‌هایی را برای اجرا در آینده تنظیم، پیگیری و ویرایش کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/akhbarefori/684540" target="_blank">📅 19:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684539">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3AY0mN9o_uzMhmpp_V_eWNq2jU7WyK6AJpWh73wf7VxGy9OLHy8i3gikKu5Qr8nj1auEGEZwknVMxMOtnhlGN3JK2FBqwYFfUa4hC4g18mt4VWR3FbTo1CrsKbHqLnDyXcr9Kd8yNQsCYBPFlMsh4UE-aRd2SRvRE3_DkXYI7LaqPb8kk-k5DnBgPOKDD0F9g2J2oCZoskMQDq0IOgYX0fbIU8CU_wWdUggdSpu2thrDTEmKpJEvqLthvIa_VJ9CXBJREnoPwNwxe6bFpoM8aAFgBcGb8oScnwtdhf2Z7g0KvQAMSSshsaw9udPJEuZMj5UUgdkDhHX0ZuBi37riw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سرتاسر آمل در مدار 5G / هدیه ۱۰ گیگابایتی همراه اول برای مشترکان آملی
🔹
همراه اول با تکمیل پروژه ارتقای شبکه، پوشش سراسری 5G را در آمل فراهم کرد.
🔹
این توسعه در قالب کمپین «سرتاسر آمل در مدار 5G» انجام شده است. این کمپین از ابتدای شهریور آغاز شده و تا پایان این ماه ادامه خواهد داشت.
🔹
مشترکان می‌توانند با شماره‌گیری کد دستوری «ستاره ۱۰۰ ستاره ۵۱۱ مربع»، یک بسته هدیه ۱۰ گیگابایتی اینترنت یک‌روزه دریافت کنند.
🔹
در کنار این هدیه، بسته‌های ویژه اینترنت متناسب با ظرفیت و سرعت شبکه 5G نیز ارائه شده که شامل دوره‌های ۱۰ تا ۹۰ روزه، بسته‌های حجیم ۱۰۰، ۱۵۰ و ۲۰۰ گیگابایتی و برخی بسته‌های ساعتی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/684539" target="_blank">📅 19:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684537">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a383a3b317.mp4?token=bN54R-qU9B46cPHSiIPsghZ7R7gMkB13iN8oR1KNLkgAi719EvK6aP-knmoAHB6M2LH-FBLMshGR576tKf9ThsdaMK5sGAgdqsq9ewwEYrWBzZoG-SPt3PytiyWC9VziWI-Ml7ct9SOMSwObWKTzjvHkv2VDqFBztCIZ6JnALftz78tK9SIXDeX4nRQ4b6lt4mHZxhozi2fyf8uFBzC9t5Cm9CZAcmsjUsVjr5eclXai978_ahCHYdSMYot6Yc_qZvmi9hFWRp21I-BAJfk2E5SSV1vdcw3MUN89Lvy8ZfiiFVBvlN5BYP0z5Wu5BhKBsPYcY_fPeJGFHdHyOp_lQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a383a3b317.mp4?token=bN54R-qU9B46cPHSiIPsghZ7R7gMkB13iN8oR1KNLkgAi719EvK6aP-knmoAHB6M2LH-FBLMshGR576tKf9ThsdaMK5sGAgdqsq9ewwEYrWBzZoG-SPt3PytiyWC9VziWI-Ml7ct9SOMSwObWKTzjvHkv2VDqFBztCIZ6JnALftz78tK9SIXDeX4nRQ4b6lt4mHZxhozi2fyf8uFBzC9t5Cm9CZAcmsjUsVjr5eclXai978_ahCHYdSMYot6Yc_qZvmi9hFWRp21I-BAJfk2E5SSV1vdcw3MUN89Lvy8ZfiiFVBvlN5BYP0z5Wu5BhKBsPYcY_fPeJGFHdHyOp_lQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بی‌ارزش‌ترین ویدیو‌هایی که در یوتیوب بازدیدهای میلیونی داشته‌اند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/684537" target="_blank">📅 19:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684536">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cYPDt8-aHy8lHaXwiZXfrqGy-vk3bfvsAOvbZS6nmK13hYLgMXqqxl1cWytlC8TSxbIBDc3ctTlarT0GXF4hmFmi-HUuy6mBBY_4pHM00g-i9LWt5fRfkveRcnRY8vp2T6y6IGkU9lM9HHjzdx0iEXu-0IbpjdLpLAv6F5e9Dlo7E6fHajOI5fVOCBJ5xMujwLuIa0KxZmyE5N1QiOAYbwT589MCm58m55IJr-cuAKTUXxyp0kbn8NQCow-fIwrk9Fj92L7o8PcWzolh-6UF6_YhyHpw7V_aH5ES89QzyEOFboSlZUTOFc4PM0nyWmb9cZCkPcVN0JMuG35gCDLTUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زلنسکی نامه ضدایرانی نتانیاهو را منتشر کرد
🔹
ولودیمیر زلنسکی، رئیس‌جمهور اوکراین در حساب کاربری خودش در شبکه ایکسی متن نامه نخست‌وزیر رژیم صهیونیستی که به مناسبت روز استقلال اوکراین صادر شده را منتشر کرده است.
🔹
نتانیاهو در این نامه نوشته که اوکراین و اسرائیل با «تهدید مشترکی» از سوی ایران مواجه هستند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/684536" target="_blank">📅 19:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684534">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2l-boedpTK8qiYZI9PoXjTkXqx-56iemMGyyC37P0-Fw53aIvyGUICzapWtmkA4UF_dykX7gYrU8iQvcSh3v1Eojp8oSg7UVHcXw5E7k3kWxoF7Qfu2DtQ5xCi2dr_kGnN-L7IiCZx8HuA9I5M0EQwmfuxgohjU0eT69oyaZb1uJ1OBfKra67BSRwpNFLV7DpLUJYxiNEwdSBkAKq_3oYlSQ3s2KKv-6Q1UK2hel7LNiP9VzAUraT_s1ZeSgognTyhOBVycCEPpMzdN9pBNXXGet4wsKUXlkovXqsb_xYfkOUlbvxYUhKFFR9HQjenHnA1kpJrUDynt-chYsbaXUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این ویدیو چند شب پیش در تلویزیون پخش شد که بازتاب گسترده‌ای در آمریکا داشته و موجی از نگرانی را در میان نهادهای اطلاعاتی این کشور ایجاد کرده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/684534" target="_blank">📅 19:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684532">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
تصاویری از ابعاد گسترده تخریب محله‌های مسکونی و نابودی خانه‌های فلسطینیان در پی حملات رژیم صهیونیستی
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/684532" target="_blank">📅 19:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684530">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/585a11a479.mp4?token=unNPTyCNCIIAGXhPvrK6u6tkFcRKgujFfPY7VDWzGu4zKYusO5gkKmRRt_1opAq6AqTrR0ejIoZ5mJyvjCYQRRgzGYkxqreXhwX-lk-_0cMPII3u7hpcpOu-LK0N414Rn_8ciRMji9LdWhBWqa9xbmoS96Sf7haRswFjUp3yLJj5RwncZSpkaObuB8AJh2Y7SIAxRsh1nJaYxEQrIarM7B1269HhNu59ZFt5EZurBCvH9gfphOjwLN9LfK9M0A-Ddw94eRN1HbDCN69vIjIvh-mw0oWr44yJGJ0IeTxPGRNA9feRPQg48cfT41-VORcJArTUEls2NQbeVBL6sAGZbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/585a11a479.mp4?token=unNPTyCNCIIAGXhPvrK6u6tkFcRKgujFfPY7VDWzGu4zKYusO5gkKmRRt_1opAq6AqTrR0ejIoZ5mJyvjCYQRRgzGYkxqreXhwX-lk-_0cMPII3u7hpcpOu-LK0N414Rn_8ciRMji9LdWhBWqa9xbmoS96Sf7haRswFjUp3yLJj5RwncZSpkaObuB8AJh2Y7SIAxRsh1nJaYxEQrIarM7B1269HhNu59ZFt5EZurBCvH9gfphOjwLN9LfK9M0A-Ddw94eRN1HbDCN69vIjIvh-mw0oWr44yJGJ0IeTxPGRNA9feRPQg48cfT41-VORcJArTUEls2NQbeVBL6sAGZbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دیوانه: اگر دونالد ترامپ رئیس‌جمهور نبود، اکنون اسرائیل وجود نداشت. این یک تضمین است. ایران اسرائیل را نابود می‌کرد!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/684530" target="_blank">📅 19:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684529">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzWkP4xueC5RqAGbwJ1scV-p6Vnse8PhePrkgGjq8fGtvHSdy0vsZ84pgRgHEG5d9loKErieE_vKOh5XjBpDdR7ECyA1r_vgA72ZaaMfqtMPsOHKAT8iV1uhwqkv9C5pmqdhD2MehNEgLwSw-wPgjbewbAx0X6CWWZeC1olFyIQ1RpPY_MMw4yY1Pb6EVhesaU_jo_GzEVdl-V-YeGBSeqWHONGwxWpAUC-4xr_Hwq48l3TMf6El3WWwB1BKVpfB2BcL0iwopvkMRnLRGp29bQEkZn1MdrQUjksDGuxBJm30_XZwkzAvMKhbKvt0QrggliFMpQ_MANd4HYSQzqVt0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
امید ملایی قائم‌مقام هلدینگ خبرفوری شد
🔹
با تصمیم هیئت‌مدیره گروه شرکت‌های تبلیغاتی و رسانه‌ای خبرفوری امید ملایی به عنوان قائم‌مقام این هلدینگ منصوب شد.
🔹
این انتصاب در راستای توسعه فعالیت‌های هلدینگ خبرفوری و بهره بردن از دانش و تخصص ایشان در مجموعه صورت گرفته است.
🔹
گفتنی است امید ملایی دانش‌آموخته علوم ارتباطات است و سابقه یک دهه فعالیت رسانه‌ای را در کارنامه دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/684529" target="_blank">📅 19:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684528">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
فهرست چهره‌های خارج‌نشین برای بازگشت به ایران روی میز وزارت ارشاد
وزیر فرهنگ:
🔹
ایرانیان خارج از کشور در شرایط سخت اخیر در کنار وطن ایستادند. جایگاه همه ایرانیان محترم است، مگر کسانی که در کنار دشمنان ایران قرار می‌گیرند.
🔹
فهرست نام‌آوران خارج‌نشین توسط وزارت فرهنگ تهیه شده و تلاش‌هایی برای فراهم شدن زمینه حضور آنها در کشور در حال انجام است./ ایسنا
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/684528" target="_blank">📅 19:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684527">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNWlMwvCplM0PyBz2Z7EZuFY4qVgADe1h4vqrUqtpsM4Mwnm_aEPDYswkMXKXw5P6FjmFJtxzFyaeeW6xCK3gVRS80vRcKZErAdqEVlwhLw5CD2e44F8dM_V8dxQQJtsygXTF-OQscfcQPZxIkoEZ6q1FrK4NLRdIB8Y9FCQISQu7diqyM9l67P-IlGUuzNn7qptGmsUFwL6qO5mfv6TbLnNKGCeU2QZpGPk32IG6l-qotGWEUS3ZrnAW9NQkhs3x7xdBRXwu3C9n9OaALaNdEfGMXL4VM-hep3GAFZeIHCm8TvwJhn6EeZPvZJu5cGT-XusqTG76Vm1Xw_otfhV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
🔹
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
🔹
در ۲۴ ساعت گذشته هیچ ترددی در مسیر جنوبی تنگهٔ هرمز مشاهده نشده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/684527" target="_blank">📅 19:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684526">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b11870891.mp4?token=MYCNTkVaoXmSzffHw2jPh36bvRj9lAcIboFB6OPmxr6555UjYZROF1HcnPTTnd-hLJZIU6HR4ZFMFIu8uY2zJ6QOfV0GBeEsbahGj0XsrLsYnbMOJzaFoCEnSA8rPc_O0Pp2UGIirhM24Da-HwROaiWGZ-a8Z9yC3yMIAlyblBtcNpto032D0UFFCWd8jpAGcy5t8WJeVY8P0VQYvhktpjNrNhVcvRG5KnA0PGG0675gv-UH6HRl30_O_QiCMUfwnOVHXmXtWfyL1z46OzlF5J7TGpyiniXFIsUy4yvFjcql7eiZukVJjuihqgRDtljEtvrDkcGJVbojcPRq0yYt1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b11870891.mp4?token=MYCNTkVaoXmSzffHw2jPh36bvRj9lAcIboFB6OPmxr6555UjYZROF1HcnPTTnd-hLJZIU6HR4ZFMFIu8uY2zJ6QOfV0GBeEsbahGj0XsrLsYnbMOJzaFoCEnSA8rPc_O0Pp2UGIirhM24Da-HwROaiWGZ-a8Z9yC3yMIAlyblBtcNpto032D0UFFCWd8jpAGcy5t8WJeVY8P0VQYvhktpjNrNhVcvRG5KnA0PGG0675gv-UH6HRl30_O_QiCMUfwnOVHXmXtWfyL1z46OzlF5J7TGpyiniXFIsUy4yvFjcql7eiZukVJjuihqgRDtljEtvrDkcGJVbojcPRq0yYt1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: ما قادریم همۀ مشکلاتمان را حل کنیم
🔹
من معتقدم می‌توانیم خیلی بهتر از این عمل کنیم، ما قادریم به سرعت تمام مشکلات خودمان را با همدلی مردم حل کنیم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/684526" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684525">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558b39f2ab.mp4?token=bcIP-Xk2BSq3tFL_5rWhONvEIpojGxigPqXgvm4iyqKTKlYFy1YQCkvj5r1BfHO-Ec9CJYZHmrOR11QggHQjwjyxXOm6jrp9vCBoSH-VfHELofb8t6J4SwTMIkoQwQnwq3qS9gCqZr3gCyHcnIegpivF5O1SOWn1w3ggD0mc6Hc0cHY4QnOBL3Omsj6LtUwCKrdU4xgBwQkp0OLJ5zGnpu-0WrpM3qDzdsHj-XH6Wig3Jq-Wr3os2Gok5nKpaaMse5FfUMdFBG1-yvyaWG4SbY4FcwBY6zMafYmVBGuotu0t3dG8LpoIm-kRKERuAemfucUfyMB5syVTEtho2y_UZSTiW-cS9ve1j6wkLXZ_CF8lg_N_-QWoJnqxEbnfw08qkDCcFr8KfzPs-7HjIGAmbefmIYmk4K8qOqkg0u7hX8jNrENjHjxe_p_G9zyfTCIj2h6jcR-zE8X2nfHnOfjSlOm9D9OVdbT8kvrA5PArqNxWz5QnvU4vx4KI40OkO11uvxZgWLQyI4XEF8CoA86iLRrr0awrDuFjzDca5SzeEW2Z6Xx26jEYmrW7bb1EiUh8Xmy-d9rf9rMmCYZNTCosUXecdFLwqtrKWRUhZTtPIisYg3b0EWsrTkxCkKqXKJBDG_YpUfBH5wAFkHAQ-fFT3c_oXZ4gLoh8KS6837biWVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558b39f2ab.mp4?token=bcIP-Xk2BSq3tFL_5rWhONvEIpojGxigPqXgvm4iyqKTKlYFy1YQCkvj5r1BfHO-Ec9CJYZHmrOR11QggHQjwjyxXOm6jrp9vCBoSH-VfHELofb8t6J4SwTMIkoQwQnwq3qS9gCqZr3gCyHcnIegpivF5O1SOWn1w3ggD0mc6Hc0cHY4QnOBL3Omsj6LtUwCKrdU4xgBwQkp0OLJ5zGnpu-0WrpM3qDzdsHj-XH6Wig3Jq-Wr3os2Gok5nKpaaMse5FfUMdFBG1-yvyaWG4SbY4FcwBY6zMafYmVBGuotu0t3dG8LpoIm-kRKERuAemfucUfyMB5syVTEtho2y_UZSTiW-cS9ve1j6wkLXZ_CF8lg_N_-QWoJnqxEbnfw08qkDCcFr8KfzPs-7HjIGAmbefmIYmk4K8qOqkg0u7hX8jNrENjHjxe_p_G9zyfTCIj2h6jcR-zE8X2nfHnOfjSlOm9D9OVdbT8kvrA5PArqNxWz5QnvU4vx4KI40OkO11uvxZgWLQyI4XEF8CoA86iLRrr0awrDuFjzDca5SzeEW2Z6Xx26jEYmrW7bb1EiUh8Xmy-d9rf9rMmCYZNTCosUXecdFLwqtrKWRUhZTtPIisYg3b0EWsrTkxCkKqXKJBDG_YpUfBH5wAFkHAQ-fFT3c_oXZ4gLoh8KS6837biWVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در پی انتشار ویدئوی نقشه ترور پسر رئیس‌جمهور امریکا، شبکه‌های خبری امریکا از جمله سی‌بی‌ان نیوز با انتشار فراخوانی از حامیان ترامپ خواستند برای محافظت از او دعا کنند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/akhbarefori/684525" target="_blank">📅 19:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684524">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omqbakB4_e0aAzJ0v6gbvLNIa6cSlIxqRE6lvAN_TWvmY2toOWOQaGqnMSL7nJa94VZGsKi7vz2OtlXCPNhZ2JOzuPYFeQX9KvjuuSN0E7CoNCvkq_xo7RfX7pq-ZlOuRkPe7urOFN9pbLeEQ2LYN7opMOWmKjRygjBaTjtVZH___BG2VCZHB2aphgSAKH7fS__HexS_kym1UQQg9ql1bpAdY481d_Jz7_m-3nn4a1H_aIeItgiAjHynZNjzPz2ExfWDuA3U5eLtq4DmWeQMjFHfCdQDKCD4JIZRYvyet8LiGShrplN0_5f-DR1-FpDR_rOzgDQOt80FTc4V4tlQ1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«منافع ملی»؛ معیار انتخاب ایران در اسلام‌آباد
حسین افشین، معاون علمی، فناوری و اقتصاد دانش‌بنیان رئیس‌جمهور، در جمع نخبگان کردستانی با اشاره به تفاهم‌نامه اسلام‌آباد تأکید کرد: دفاع از تصمیم ایران برای امضای این تفاهم‌نامه، دفاع از اعتماد به آمریکا نیست؛ بلکه دفاع از حق ایران برای انتخاب ابزار مناسب در یک مقطع مشخص و در مسیر تأمین منافع ملی است.
به گفته وی، سیاست خارجی زمانی می‌تواند مقتدرانه عمل کند که تصمیم‌ها بر اساس منافع کشور و تشخیص درست از شرایط اتخاذ شوند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/684524" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684523">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآجیل و خشکبار برادران حسینی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ed72d204a.mp4?token=gM2xlykdp3Gxzw5glWU1LEsbMEg-ir6L49lxpFz474X4Y0X9XbhK5HLMYZt4I2E039DKjQHatUlVAyTF3Ps4vFViQl-DRAl3eESoeWezyhhwR6qSmjcSGVIauqES5aQC77C-dRU__Pis9DTfqL_l06e8ckUQnWkRznWAADthZCyPDNLaJPayVg38SRAcmArnnqXDwHtQwzt5g6UGDcyI-PkPjWFJM03g4Xutk9YujWSLL0BIrUFuRmvirp8hf8dLH9x59-ZpSVjd04-nS0jlywHB1tqY9McDLCg_cFZ43m2W_5CNRgIgcgihClcNo0h1nB6XKLqvYsB4WnwPtDQapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ed72d204a.mp4?token=gM2xlykdp3Gxzw5glWU1LEsbMEg-ir6L49lxpFz474X4Y0X9XbhK5HLMYZt4I2E039DKjQHatUlVAyTF3Ps4vFViQl-DRAl3eESoeWezyhhwR6qSmjcSGVIauqES5aQC77C-dRU__Pis9DTfqL_l06e8ckUQnWkRznWAADthZCyPDNLaJPayVg38SRAcmArnnqXDwHtQwzt5g6UGDcyI-PkPjWFJM03g4Xutk9YujWSLL0BIrUFuRmvirp8hf8dLH9x59-ZpSVjd04-nS0jlywHB1tqY9McDLCg_cFZ43m2W_5CNRgIgcgihClcNo0h1nB6XKLqvYsB4WnwPtDQapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌰
برادران حسینی |
🎉
جشنواره تابستانی
برای مشتریان سایت، این فصل
2️⃣
امتیاز ویژه در نظر گرفته‌ایم:
◀️
با خرید بالای ۳,۰۰۰,۰۰۰ تومان
✓ ارسال رایگان به سراسر ایران
✓ یک هدیه از ما، همراه خرید شما
این دو امتیاز فقط تا پایان جشنواره تابستانی برقرارند.
خرید از سایت
👇
🌐
https://hosseinibrothers.ir
خرید و ارتباط:
hosseinibrothers.ir
t.me/Hosseinibrothers1342
ble.ir/hosseinibrothersnuts
rubika.ir/@hosseinibrothersnuts
instagram.com/hosseinibrothers</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/684523" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684521">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qggn5DJ0oCRo_I5PfrQJud2PZ3mfpEGRmwTVkczzuQt-F6_CihMor83RZVCTKr8x_Fy3GPv8gf3jcctH9y3LXuYVKwbRcgyjFc6nAfQlTEREgCUCDhx84k5aJW0zv6sFTbvwXoAMQpIr8sv0CFzRZsUtBQheeFz3LXZCCxb0FQMNUzSRzeA4HBH3qtiu19yfAnBUX0BJv85i7VmgsAM-44bUpJJpI2Nsqfa3euyaLumOZWBQ1-_n69pwC7lEk9VFF8hZvWACfMHjRVBMfE0D0a83R8Vpod3OOuqbXxZxY0Zrg1yVBAaqu8bRwAFOnWqYXDQGW9iVkuXgcHt9eLHmcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
https://khabarfoori.com/</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/684521" target="_blank">📅 18:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684519">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axiGVGEQRiu085-fPpIpMyxjW9IS1IOZN_5rd5vCavSEzPoHllO2RP1Bs_jS_2-IlYQn4-jKB8VFufCSH6GCUbdFIW38pMiMpCvwXbui_b9rfx--nhsC0nbtKSkBgVB7kUNsok1TDhmkFu3hK70ImPwdk7f7oJrf7_AAz2hDpAN3sWGXvaTlNIksfnJzROw0Lsu61k5jLuflHjfO9o2ass4sFzSTrtZUkk-rPJJDSmJ06Bn7hodFLT1ogF76M3LEb7z-rBWYp4jPBGN9zT4yU5B1axHKEyzREVjz_-7jNenltVSUuTNw7LCQFBas-EQt2yU49fkPf_7dkj8VDPi8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سید نظام الدین موسوی سخنگوی دیوان محاسبات کشور شد
🔹
با حکم سید احمدرضا دستغیب رئیس کل دیوان محاسبات کشور، سید نظام الدین موسوی به عنوان سخنگوی این دیوان منصوب شد.
🔹
موسوی در حال حاضر رئیس هیات چهارم مستشاری دیوان محاسبات است که با حفظ سمت، سخنگویی این دستگاه نظارتی را بر عهده گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/684519" target="_blank">📅 18:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684518">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e6dc07ec9.mp4?token=HUlMpmrXDQX66WdJDKkAk1icSrOoVJizOtuNGJaF7o0kQ-nI_IBurMr1_wtw_H067O2gdA6WZRlJREcVkENqEyyuajIiBf8NQuc1FsICNlx7U9wf_T3n7K8llhSoOCbQ6u1_uIJOFInT-bU-ua1dotSdQrBJVU2AoykQeYTyEMIkVbLF6skXIv57CaWwjJ80WbOU5DuNtfjt7k4GRPo3ar0w9kwh5WUcwZB0rO-xLEgKu7WMkcb5HtU3ErraS3L2mRB9-bjt1tWblHJYfUmQ8yRpHaLDQl9pJCTt-Ap0jRdMyQiwGjySee5lW8tyAcxWFSwnPb0eGy4T1eKFDcawiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e6dc07ec9.mp4?token=HUlMpmrXDQX66WdJDKkAk1icSrOoVJizOtuNGJaF7o0kQ-nI_IBurMr1_wtw_H067O2gdA6WZRlJREcVkENqEyyuajIiBf8NQuc1FsICNlx7U9wf_T3n7K8llhSoOCbQ6u1_uIJOFInT-bU-ua1dotSdQrBJVU2AoykQeYTyEMIkVbLF6skXIv57CaWwjJ80WbOU5DuNtfjt7k4GRPo3ar0w9kwh5WUcwZB0rO-xLEgKu7WMkcb5HtU3ErraS3L2mRB9-bjt1tWblHJYfUmQ8yRpHaLDQl9pJCTt-Ap0jRdMyQiwGjySee5lW8tyAcxWFSwnPb0eGy4T1eKFDcawiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پیت هگست، وزیر جنگ آمریکا: ایالات متحده به هیچ‌وجه گزینه حملات نظامی در تنگه هرمز را منتفی نمی‌داند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/684518" target="_blank">📅 18:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684517">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GtdMo_L78YeI87LR9Isg4kUrM0cAAZIDnzWfWLr1NM2xt-MfZ_ulF0oY_I879AuUUnF6ekAPi2XVcC-iAWaWSPjA1UvooBV25Mfvs4WutKzIPMAjsjOh9f-y1cKssASq5lOqX-hN7LdnlL2xTxDIWkAiW4oY6DKNMvdBvV58HE0yEgBdWZ-kc_fm0NwOLDoPStQfkOdjorkc0klWyEU-d5A5F84K1WwcDXD2-jX4-_lJJZb4Dro04jWXwWR7Tf-SpzGiEfxA77PNY_VGRc0hH21o_YIkBtTEV7lzGxfU69_vhqdqCSZAfE5np75MrQ_UFXF4_zRtUOVmpzWLUWIOFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فعالیت سامانه بارشی جدید از جمعه؛ هشدار به شالیکاران برای برداشت سریع
یک کارشناس هواشناسی:
🔹
روز جمعه در سواحل دریای خزر همراه با کاهش دما، بارندگی‌های نسبتاً قابل ملاحظه‌ای رخ می‌دهد، بنابراین هشداری برای شالیکاران است تا در برداشت محصول سریع‌تر عمل کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/684517" target="_blank">📅 18:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684516">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f97d7acf26.mp4?token=gbqmm09AKgN5C3lFMGSPFJeRgtarb5onFnrNaYrCgzDsqfJCiBUAMklN-NoUuGHPehbMeFe3AFL2XRqfgLwIKq9wGJAvtvA0LSD3AGhq6ux4CErcyyAwBqpX08xwgEG6Dclr_Fmo0UwfZ7ZoC60WWSv-1yW2IWLM1g3cDKXDN-ttShYNlhQKeWI_HlwkAWsw51xsBYFj4w5Ix3fwMAmh99fctAbLt4w_eg1S6U4sQlPA5DItk0PjnEdVgJ9WU_VySAe2HRzOwKsYqDUU4feW8SvKkqdbADZ6P54qmGmlMBi2HRqLUIVA4IczdvQX__26QR98xOfEKqdmOSjBBNXxGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f97d7acf26.mp4?token=gbqmm09AKgN5C3lFMGSPFJeRgtarb5onFnrNaYrCgzDsqfJCiBUAMklN-NoUuGHPehbMeFe3AFL2XRqfgLwIKq9wGJAvtvA0LSD3AGhq6ux4CErcyyAwBqpX08xwgEG6Dclr_Fmo0UwfZ7ZoC60WWSv-1yW2IWLM1g3cDKXDN-ttShYNlhQKeWI_HlwkAWsw51xsBYFj4w5Ix3fwMAmh99fctAbLt4w_eg1S6U4sQlPA5DItk0PjnEdVgJ9WU_VySAe2HRzOwKsYqDUU4feW8SvKkqdbADZ6P54qmGmlMBi2HRqLUIVA4IczdvQX__26QR98xOfEKqdmOSjBBNXxGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پلیس نپال: سیل مهیب امروز تاکنون ۷۲ کشته داشته است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/684516" target="_blank">📅 18:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684515">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae39d4883a.mp4?token=orbRvTpPZZXR1vtFBEjTqwd52EMsD8sIkGV3BrKNp0_G-d5pZaFWZoFJAOY9MOXK1KXXqCOSr_Vo69Up-0ngx9LdzeHNUSLxXzBoT5cnwDMF8iA3PkvUKHIjsU7646Lf-qeXu9MBRd2DKQb8SS-3UU-o5NeXUR8mL7VR30ScWnBQ1fSK7VAmSPxHN1I6v6Q0PKBNlKTY5zcUel01rVRj7Btm116AXEkdz_ElNl4xK993KOtR4RAxA8CU9xXUmnk9oDewj-ec7xZQwNLKkDKHSAr-8pzQDHV4vduNbehRw7Ip0GNWY9QcBJHDC--RUPXbRozZk08uivKWCWZnTZoYQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae39d4883a.mp4?token=orbRvTpPZZXR1vtFBEjTqwd52EMsD8sIkGV3BrKNp0_G-d5pZaFWZoFJAOY9MOXK1KXXqCOSr_Vo69Up-0ngx9LdzeHNUSLxXzBoT5cnwDMF8iA3PkvUKHIjsU7646Lf-qeXu9MBRd2DKQb8SS-3UU-o5NeXUR8mL7VR30ScWnBQ1fSK7VAmSPxHN1I6v6Q0PKBNlKTY5zcUel01rVRj7Btm116AXEkdz_ElNl4xK993KOtR4RAxA8CU9xXUmnk9oDewj-ec7xZQwNLKkDKHSAr-8pzQDHV4vduNbehRw7Ip0GNWY9QcBJHDC--RUPXbRozZk08uivKWCWZnTZoYQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چگونه یک خودروی الکتریکی می‌تواند برق را به شبکه بازگرداند؟
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/684515" target="_blank">📅 18:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684514">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
آمریکا مدعی مهار نفوذ سایبری گسترده هکرهای چینی شد
🔹
سخنگوی انجمن داروسازان: واکسن آنفلوآنزا هنوز وارد شبکه توزیع نشده است
🔹
جنبش نجباء عراق تحویل سلاح به دولت را در شرایط کنونی رد کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/684514" target="_blank">📅 18:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684513">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRwyP677V95ExIWXFyC7jstkoyIIGOJyYzIFsJNI-eC3DUAtgJ1VkkCbIUGy_-ajSK81FxS9zFG3NreAimVjFBcFXMbqMt2nYvLmGFnyxop-hEq6pt5SSViMm8g5Dp--DNNQjkaMNWKkGN1P-Xf6K_XIaM4UWEL4Y_DZiI5Tc84BODzSEn--vsuFqyY6FI6IQkdkpvJa-JpBMiAluod_AS5CUMbKX27Z0UBuS8BR-_0h7K-8AH7PnQNLrUKhhEA9AmHtsi5EVGSHSXdexZ8hqeNYZPE2Q8qhk62Gf_ZPxkOT1IXwi3Q0tYFwuoOGsYTk3niDGM4pFxo5gCys-GKEgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا آمپول‌های کاهش وزن به‌تنهایی کافی نیستند؟
یک نکته در توصیه‌های معتبر جهانی (ازجمله سازمان جهانی بهداشت WHO) بارها تکرار شده است:
آمپول لاغری، بخشی از برنامه مدیریت وزن است؛ نه تمام آن.
آمپول لاغری حاوی مولکول تیرزپاتاید (مونجارو و زیکورپا) باید در کنار تغذیه متعادل و کم‌کالری، فعالیت بدنی منظم و زیر نظر پزشک مصرف شود.
بنابراین، تصویری که گاهی در شبکه‌های اجتماعی می‌بینیم ــ «یک تزریق و تمام!» ــ با رویکرد علمی مدیریت چاقی فاصله دارد.
این اصل درباره داروهای حاوی تیرزپاتاید، یعنی
مانجارو
و
زیکورپا (ZCorpa)
، محصول داروسازی دکتر عبیدی، هم صدق می‌کند.
🔗
منبع:
سازمان جهانی بهداشت؛ راهنمای استفاده از داروهای GLP-1</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/684513" target="_blank">📅 18:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684512">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9dtjm0dxph_A4jYJA5B7aaCYyXIm0reYWTJ1UlxNmxxo9Z3pSuukpxmVYVG1CM2jbEVtKJrkq7UXYOhfPPznusJQsk0IuYuWibkLRmLwnXbJJD_KXHvYTHcUmw00j8qwpHfH0gKxJzY0-ljP34QkMhuoC6crVK3M1e6u3AAzqwWZbVj--Ln_LIQTojcf5bcnyZQb-JpuMUOoEKM8De4ncjLcZB2LOAj0wvrs6Ywi-6tznU4FKWaVEamSv8J0_RTXJ9fRDfxKJ63L2wl4uHOQQLuNxBdw3TbidJMPBJHnuEhKstizvNLDZK9-kXZ92jFqoGC-r3grBLngqp1j6XUtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فراخوان عمومی شناسایی ارزیابی _اعتبار بخشی و انتخاب شرکت‌های وارد کننده خودرو در منطقه آزاد سرخس
برای دریافت اطلاعات و ثبت نام در این فراخوان مطابق با شرایط اعلام شده در پیج رسمی سازمان و کانال های اطلاع رسانی به آدرس‌های رسمی تحت عنوان
@SarakhsFreeZone
مراجعه و پس از دریافت اطلاعات به  سایت رسمی مخصوص ثبت نام به آدرس
Plus.khsfz.ir
مراجعه و اقدام به نام نویسی نمایند .
🔗
رسانه مجازی منطقه آزاد تجاری صنعتی سرخس
@SarakhsFreeZone</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/684512" target="_blank">📅 18:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684511">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aba9e1faf.mp4?token=lnuEx5JG09B3WiIBOHsFKbx1OB_THRoJrpzD1hqSLNiqBFPGq3uO006RyFHxeTCi7iyil_z6dJ7sTAL1bTdjbsDjWoZ0G_u3fX8ku2bg0vLouk3mGix7GiDKgDZRZ6qJsn62zmCEyL11oWjtITwSoWdI_2qq3oVzNYmoGZHjGmJ1rtgisNcSlfvBeDuVDAxaR6cZK4c5KeNqNhv7yk4OwP1Bf7zayv0hb2cmAwsP5p2AUyH2pP5xaqdlmbuE7eao48SyCwfu6WpZehoYPV-qtv6XDtvlHbiqDr5fTi0nd4euWyFlsoNtu0neNuhyzszQwavf_kGh5nSfFk5qIl794YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aba9e1faf.mp4?token=lnuEx5JG09B3WiIBOHsFKbx1OB_THRoJrpzD1hqSLNiqBFPGq3uO006RyFHxeTCi7iyil_z6dJ7sTAL1bTdjbsDjWoZ0G_u3fX8ku2bg0vLouk3mGix7GiDKgDZRZ6qJsn62zmCEyL11oWjtITwSoWdI_2qq3oVzNYmoGZHjGmJ1rtgisNcSlfvBeDuVDAxaR6cZK4c5KeNqNhv7yk4OwP1Bf7zayv0hb2cmAwsP5p2AUyH2pP5xaqdlmbuE7eao48SyCwfu6WpZehoYPV-qtv6XDtvlHbiqDr5fTi0nd4euWyFlsoNtu0neNuhyzszQwavf_kGh5nSfFk5qIl794YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
خیلی راحت و جمع‌وجور گرامر اسامی زبان انگلیسی رو مرور کنید #زبان_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/684511" target="_blank">📅 18:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684510">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
سخنگوی سازمان تعزیرات: مردم طلایی را که به صورت دیجیتال می‌خرند، حتماً فیزیکی تحویل بگیرند تا با خالی فروشی و عدم عرضه مواجه نشوند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/684510" target="_blank">📅 17:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684509">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
تکذیب شایعات درباره کمبود بنزین/ تولید و توزیع در حداکثر ظرفیت
مدیرعامل شرکت ملی پخش:
🔹
تولید، انتقال و توزیع بنزین در کشور با حداکثر ظرفیت در حال انجام است. مردم نگرانی بابت تامین سوخت نداشته باشند.
🔹
ضرورتی ندارد افراد صرفا به دلیل شایعات به جایگاه‌ها مراجعه کنند و صف‌های کیلومتری تشکیل شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/akhbarefori/684509" target="_blank">📅 17:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684508">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
نامه قالیباف به شریعتمداری: مذاکره نه مطلقاً خیر است و نه مطلقاً شر
رئیس‌ مجلس در نامه‌ای به مدیرمسئول روزنامه کیهان:
🔹
امروز مسئولیت دشوار مذاکره با دشمنانی که دستشان به خون امام شهید این ملت، دوستان و هم‌رزمانم و زنان و کودکان و فرزندان این سرزمین آلوده است، برای من نه امتیاز، بلکه امتحانی سنگین و امانتی خطیر است.
🔹
و اما مذاکره در نگاه این جانب، نه ارزش ذاتی دارد و نه تابو است؛ نه مطلقاً خیر است و نه مطلقاً شر. مذاکره هنگامی معنا می‌یابد که ابزار پیشبرد منافع ملی، احقاق حقوق ملت، رفع ظلم و تثبیت دستاوردهای مقاومت باشد.
🔹
از نخستین روزهای انقلاب، مرز خود را با غرب‌گرایی، فتنه‌گری، انحراف، تحریف خط امام و هر جریانی که حل مسائل کشور را در گرو رضایت بیگانگان می‌بیند، روشن و عملی حفظ کرده‌ام.
🔹
ما با آنان که به جای تکیه بر قدرت مردم، چشم به دست دشمن دارند، اختلافی صرفاً تاکتیکی نداریم؛ بلکه اختلافی مبنایی داریم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/684508" target="_blank">📅 17:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684507">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8Qt2Ab6Rc2Q-LkoNzpWJa5DBStbJ33BSOgfwQvMVPaZCZGYPQR1sHAwOlojfEtf2JSaIJO3I4wF3kGr0e63jI92e89X15wViTL-KQTLgX1eaDTiUYpt6I6uJVJJFbhgw8yDFBQ8dZEc9sKaJoqsBuQ1vnIhh3SwMjh1sVsdXkYidSKcNAMkN9Kta4IqseO3FFlarmli3oIHR1UprP2Xh10S9HciRXstIHrcEt32odRw9Jha2L3KEDu1DvJ_ZhY2BWVAVJzSHEh66FP-JqhYTLYwpFomey0m0BCCIy9928uHEk1wWZYFk3NeTPQP9x1D5TJoOsjSdtJ-HF-tC3xfgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
پای کار «خاک ایران» / ۱۸
🔹
رکورد جدید بانک کشاورزی در تأمین مالی با ابزارهای تعهدی؛ میانگین رشد ۱۴۶ درصدی در سه سال اخیر
🔻
بانک کشاورزی در راستای گذار از بانکداری سنتی به بانکداری نوین و با هدف تأمین مالی مؤثرتر و پایدارتر بخش کشاورزی و افزایش ضریب اثربخشی منابع بانکی، طی سال‌های اخیر توسعه ابزارهای نوین تأمین مالی از جمله ابزارهای تعهدی، اعتباری و دیجیتال و تأمین مالی زنجیره‌ای را در دستور کار قرار داده است؛ رویکردی که با استقبال فعالان اقتصادی همراه شده و به ثبت عملکردی قابل توجه در تأمین مالی زنجیره‌های تولید، به‌ویژه زنجیره‌های مرتبط با امنیت غذایی کشور، انجامیده است.
🔻
حجم تأمین مالی این بانک با ابزارهای تعهدی طی سه سال اخیر با میانگین رشد ۱۴۶ درصدی، در مجموع به ۱۶۲ هزار میلیارد تومان رسیده است. این رقم از ۱۹ هزار میلیارد تومان در سال ۱۴۰۲ به ۴۰ هزار میلیارد تومان در سال ۱۴۰۳ و ۱۰۳ هزار میلیارد تومان در سال ۱۴۰۴ افزایش یافته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/684507" target="_blank">📅 17:38 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684501">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/arqNO8VYmA90OqCnSOUglcM6pbTTXIms9WNwsbu14W3ap3Aw197VHi7EOybE-Rr1Ea-RNjHSVU56ndhpCQP_GZhP0EY_OMe1HX-p12jize-pZ6zMP7KpNjlIK_BBowsRfeswqnYOaJ6PFJVelpb0XcDeSDror1h79rcKzItOTpPBVgCfM3NvZoYQEDax2PKLvnGlvxm6tHkVwMy5PPBk68h3kG0oY69YpVxhc_dn1_2eUgOU3qHrxHgcXlX-KpkBejgbHBrpg51pJpPp5gzNY1b4FnYdM7xzYJcROHH5Aj7dliybeGWKDmxIEobjxPVmzN-YiWp3xzEHQMcIF2uwjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qJHp6h6zjZzTX6Bb7eR4qUOFr5Wlu4T207kyifekr8eMl12M1bTyJefTsb5qaSzxRCeI0Wj3kWpfoBRetzOeoxe10s9-tx6eIslNU0kPg3BxHpTV4NyV_OROjwbBgtZKXDaIkbDIZfDxWF_I6w-j2moYQYqF_fN6Dvt1oMIQ5GrIumZjohAlkbqLSQdCfSMmO8g-LnXI3PPbNP6i_l9ayWBw2Hoer8obDitKt5ZLDrl-47f8UHmqsmd8syeGmlbCT_Spbp_Sqts7s4Xrf6IERm4QoAhQP6g08Sqpkrg4drk-wk_85zA4SwN1pDbe1TfDYpj4HfHMDHTiXGiXSFLm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tfi4G2o-8cd-E-yW4sP_x4tOvnFvUWNc5FkCvI3D1gptllI-1LQcapG1FW6om6NPA2bm9e7P-q5FUk9Tjx6r638tWaDiiGmcjkDNuirOADToeutwsQItonHYpjfhU_FS1hNVUfnvNTYNq14aucosi3jeq0F8AGlOdGw4Dr4mr87CE8wZvRTdqP3asE_L9iZgbU8i1dL5OGA2AfdRrPOIPV1CA0gUePvTbvHHMEJ2My7_MmxCaPz1l1xPa36Y7gDujIev4eXOQs_nNL6tiBC8vWzSOy6eOcswULBKyDUthuCM6PA4kIjMgSVaML--9VpAy1Jh2VH-62oWU0idmDJaHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KWIYxs2G2lbGwoIPC_61GfeVChJc6VqQ3MXgyD2eT7FwMLkPd5JWaJ8HfA6TheovagasC2qoTO9Ck4CRJYtQF-bHvR3_39OZhNHywxN0x_OTmIecIk_X133MFefeoWuUP93Vk_UKgOabZWHVqO1yD6QWM6ewGMV8S1jmLQ52yrpciyPoVQY5yJeHWvVRoioKh9ECXmD9gReuI99Y1RyLONIZTqMaGTnZSfrIy30V73PbOZbzcTcqTjp1hLNm4PdMBGwIXAvP7WCa2D9Wr_4VbidMHX4eXs-lCe0D-WdGtHcSEtGGFD95Ub266XZTJEhODQizHf-4uUtbPS2UkTzMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QJzj12uPxnQqTzTfSmtl1RpL-BMlvov2qfS6QEmYvlsR59Xm8APzm27qOmXKyObLDyUn3CFttYsuGcJVvQVhqg5ZI2mwy8g92MMo1ogLCV4HqxOpmUiOd_67UEOcpmKzcNxib_rRyuMi8DP8-AK4Fh9Tq6igp1uGs5dpbR02UjeN0t_EgLwdyhBKTL5A9SSvep1db6OQQ2FUNVM0nApFWdRMIPpk9a1FmWxCSeykDFe9xwuqDMuSe1jDkaQ8njPLlvY_IhdQoNpszdgN4rMrv3DzFZKl_k-HKGhubymxxVAVJmWTXTJ8A1Xep2VAAsue7_pGo3QmV-iMIwyOTdb9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rqhaqk85eiVif8_s8kxgkAQf4oIrMkS7q-LWYYBoFlRlUT5wRf05PKOE94j1HVRvvIfyMgpeuqonJ0aAMSkDGCUKEK40iMrI2cSCtwRbiNmsgaa_u4BcRKVeMJvhOKM9_r8rEKhAr5MOIc3gMYd2Y4gWIf1OzDnng_cEN9YNKrWVwS9xuRndJMW2E3HUGNODv9tGLODxEQAAG6bToHSbjfoIKZCWVmYDTEu8-UW_uovt_mRrrtF3GiNC-p9GRggjMsoTUFvC1kHR9b1o7tg0_8FuaANRBsl8BMQ4VUyiCl76wpsYAzZuOgD9Unaqx76dIphHIcTA6x_GupiVQcZ4lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
«بگو چکار کنم» یا «نگرانش نباش، با من»؛ دو جمله متفاوت که حال آدم رو عوض می‌کنه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/akhbarefori/684501" target="_blank">📅 17:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684500">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
وزیر ارتباطات: پرونده فیلترینگ باید بسته شود/ استفاده از فیلترشکن‌ها خسارت بزرگی زده
وزیر ارتباطات:
🔹
سیم کارت سفید مصوبه سال ۱۳۹۹ بود، اما در سال ۱۴۰۴ رسانه‌ای شد. استفاده از فیلترشکن‌ها در زیرساخت‌های ما آلودگی ایجاد می‌کنند.
🔹
در جنگ رمضان ترافیک اینترنت داشت به سمت منظومه‌های ماهواره‌ای می‌رفت و اگر به نقطه بی بازگشت برسد بخشی از حکمرانی کشور از دست خواهد رفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/akhbarefori/684500" target="_blank">📅 17:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684499">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptW0cKN0VcWzho0oZRNZAQUcGBwpy7F-4_LFqypdAtLWfRluHCGByCYkreNO7NJ-qRU2eQYwSIFjTYQ5sgGnNSpycLypCLpoaitY029yNZA-iM1T8lEAVnL4vtylF9Rl7UyHKEr_4qPxqUBbcRViNBmVrU0koWDJIEG2MiNWjYDgrmxW4Brge88xsQ8k-lVR8FopzSllr-9Lbrp0gst3lAnIfbKv0WT5hGZEY962jZ9KpygntKvn_tSXyjAkYVM15zfdZhIUXAhEOI9Ahy-xHFFjyXtapR98wntrDL4bkvE-ZVCIiH0qwAQQiL49tmMjrM9DUm7IFo4ZRJehbFYkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در کدام کشورها سرانه خودرو بالاتر است؟
🔸
کشورهای کوچک و ثروتمند اروپایی، بیشترین تراکم خودرو به ازای جمعیت را به خود اختصاص داده‌اند و کشورهایی مانند سان‌مارینو و موناکو در صدر این رتبه‌بندی ایستاده‌اند.
🔸
در میان قدرت‌های اقتصادی، آمریکا با ۷۶۰، ایتالیا با ۷۴۰، سوئیس با ۷۲۰ و ژاپن با ۵۷۰ خودرو به ازای هر ۱۰۰۰ نفر، بیشترین نرخ مالکیت خودرو را به ثبت رسانده‌اند.
🔸
ایران نیز با ثبت ۲۴۵ خودرو به ازای هر ۱۰۰۰ نفر، رتبه‌ای بالاتر از کشورهایی مانند اندونزی و هند دارد.
📊
آمارفکت | مرجع تخصصی آمار کشور
@amarfact</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/684499" target="_blank">📅 17:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684498">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
معاون رئیس‌جمهور: رییس جمهور پیگیر بازگشت سردار آزمون است
🔹
مشاور سیاسی رئیس مجلس: هر تصمیمی برای انتخابات شوراها باید تابع مصوبه شعام باشد
🔹
سخنگوی فدراسیون فوتبال: احتمالا اردوی تیم ملی پیش از جام ملت‌های آسیا در دوحه برگزار می‌شود
🔹
جفری ساکس، اقتصاددان آمریکایی: آمریکا با تحریم ایران، خودش را منزوی‌تر می‌کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/684498" target="_blank">📅 17:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684497">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUMy-GYyTYVW6ma61EW9PSXZ19shMYjbsizG9qZnIAW1UI7VKhbLUuuKWh8XYlmtuWfHBE0PDQs_3em7xyxa5E6ww5jcBm8NT8Q_B9gHbBrWLkdDgFY2yhuoCRXZU3mIeWUJXDALtM2h8DdoKBw89agShlYxAE8dNzx2OPJBDVPJxXfB1SYeVMujbYEhXB6rVTxiymad06dNs39FZeJLLdzieaSRyCLkwGayn6lPgx6d22KoM3dBEGV6HXtpCA_P9Fmd2mzv62M3qfOY1lwvcBfc-rVxeY10H51Xs6k6XxPAKNTcRLL0gjv8JADXjiTEPbAsWsV2UrGQGLY_-xDnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام تبریک زهران ممدانی، شهردار نیویورک به مناسبت سالروز ولادت پیامبر اسلام
ممدانی:
🔹
میلاد پیامبر اکرم بر مسلمانان شهر نیویورک و سراسر جهان مبارک باد. امروز، ما زندگی و میراث ماندگار حضرت محمد را گرامی می‌داریم، کسی که آموزه‌هایش در مورد شفقت، سخاوت، عدالت، ایمان و خدمت، بیش از ۱۴۰۰ سال الهام‌بخش جوامع بوده است.
🔹
اینجا در شهر نیویورک، الگوی او به ما یادآوری می‌کند که مراقبت از یکدیگر، پذیرش تنوع و خدمت به جوامعمان، ما را در تلاش برای ساختن شهری بهتر برای همه، قوی‌تر می‌کند. برای همه کسانی که این روز را جشن می‌گیرند، شادی، صلح و برکت آرزو می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/684497" target="_blank">📅 17:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684496">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d1af31042.mp4?token=BEr5QoVS1DGF3_4VJ7N84jFsPxjbFNxsUITxE8TTrF40pV9Joi9zZ2uWREhrMLOIj23WV--7wy_OXZ1YQ2y3VK5KkhyGnwb0Zk1_hnd8-vPMWXS3NXR1ncAYetTkDs-7ZHELFTxqaqcKHQPgdUKySqlB2vly05lo1-nhgHUpfxO0nWyZfyFzWbS2mfLqRIggu4t9u8x6ADa9tRh4NNT7boNSuFAJoi-wxAGHDCo1RHxwLi-iFmyCLaLk-XOJhIiyXPio2evK2Kx31KjIwX3tD2HFdrLbTTLyv2MGofR_Xjt8zot2ITnp24QAFs7qoOqizFZEljJF0DMpN-AyEhGiww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d1af31042.mp4?token=BEr5QoVS1DGF3_4VJ7N84jFsPxjbFNxsUITxE8TTrF40pV9Joi9zZ2uWREhrMLOIj23WV--7wy_OXZ1YQ2y3VK5KkhyGnwb0Zk1_hnd8-vPMWXS3NXR1ncAYetTkDs-7ZHELFTxqaqcKHQPgdUKySqlB2vly05lo1-nhgHUpfxO0nWyZfyFzWbS2mfLqRIggu4t9u8x6ADa9tRh4NNT7boNSuFAJoi-wxAGHDCo1RHxwLi-iFmyCLaLk-XOJhIiyXPio2evK2Kx31KjIwX3tD2HFdrLbTTLyv2MGofR_Xjt8zot2ITnp24QAFs7qoOqizFZEljJF0DMpN-AyEhGiww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آتشفشان کیلاویا در هاوایی برای پنجاه و چهارمین بار فوران کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/akhbarefori/684496" target="_blank">📅 17:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684495">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ادعای ترامپ متوهم: دیشب ۲۰ قایق ایرانی را منهدم کردیم
🔹
ما در ونزوئلا به پیروزی رسیدیم و خیلی زود در ایران نیز به پیروزی بزرگی دست خواهیم یافت.
🔹
رویارویی آمریکا با ایران تابع هیچ جدول زمانی نیست و تا هر زمان که لازم باشد ادامه خواهد یافت. #Devil
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/684495" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684494">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
ادامه خیال پردازی‌های ترامپ
🔹
ترامپ در ادامه رویا پردازی‌های روزانه مدعی شد که به زودی به پیروزی بزرگی بر ایران دست خواهد یافت. #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/684494" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684492">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kq2JUd4CRwcLaGnINCnRt3ktp7P31tBSiq21tofl1zjO1pmk19qimmV0IHSXlnEHLVYkh5i4Ts5uLYM7ZAoBrYEqxNIt9V1AcznZ3IlSqPkYQOwLpBE2SXifuxezrSQdavdWk39wvxm8PW84dP_p7Kp5fPlYCioAWCerQOFPMrWOWY0xQQIRlG26Q2XL_CbXoz9tY4JGng050XvvXWhCWr2Us_bMDb_BFkmyz4DlsnYTXNGU541aFP4ddUknX3ccSlbhsP6U2JXvbl2Umsi373ENeUj-KX6djuJWeyy5l7zaVowVtKfmueEvi0tgS7d8r2fJQYy7YAKEvIAU2fjyWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/963c6ddd65.mp4?token=NV1AgqQBsb6v-u8hygAp_TFcfStV44UwYmJdRhlvndDMwZbKLZ8r93EnIJgypWxgmfLSsOLGk-yhPvig1f-UtkK8puJeFH0zHxkIXkoW22jss6uEDZusLpc4kq8Q6gQG5m6RjEW67TI_MLqA9JTsZSf3Cj85xOJm3k6WMkoa_S1SAmqMnMfpBYCwck9OSaiyi1fZeDeKiNx_5mgeF_ZRXiN-W_4dt-dqvoOdnGLJINsQg-ai9YSfxCYTQnwnnfHa7PLZsa7uWfLs8Ls4Ic25HORR4SNmbUIEGFeuBI89kANLfOeeiF1_eBE2K_LXGFDIc3I0t1E4V1sll9WdvXr-NzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/963c6ddd65.mp4?token=NV1AgqQBsb6v-u8hygAp_TFcfStV44UwYmJdRhlvndDMwZbKLZ8r93EnIJgypWxgmfLSsOLGk-yhPvig1f-UtkK8puJeFH0zHxkIXkoW22jss6uEDZusLpc4kq8Q6gQG5m6RjEW67TI_MLqA9JTsZSf3Cj85xOJm3k6WMkoa_S1SAmqMnMfpBYCwck9OSaiyi1fZeDeKiNx_5mgeF_ZRXiN-W_4dt-dqvoOdnGLJINsQg-ai9YSfxCYTQnwnnfHa7PLZsa7uWfLs8Ls4Ic25HORR4SNmbUIEGFeuBI89kANLfOeeiF1_eBE2K_LXGFDIc3I0t1E4V1sll9WdvXr-NzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ویرانگر در نپال؛ ۸ کشته تاکنون و مفقود شدن ده‌ها گردشگر
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/akhbarefori/684492" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684491">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
ترامپ به الجزیره: برای مذاکره با ایران «عجله‌ای ندارم»  ادعای ترامپ:
🔹
هم اقدامات اقتصادی و هم نظامی در مواجه با ایران «موثر» هستند.
🔹
او در پاسخ به سوال خبرنگار الجزیره، افزود که «من هیچ برنامه زمانی ندارم، عجله‌ای ندارم». #Devil
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/684491" target="_blank">📅 16:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684490">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac706e15a.mp4?token=vguQUqS6tz6qUPWiwZSqyJeGBj1EZ_7RkKgAPi3297ahIY-JKkoGcFo7vh3YUSkO3kpR-VWzLAlFBXQHJzvAUwUU7DkXxrDoFyDe7KUCOi61Ht5klq9W949CjJm5Vi8fp8Vni1S06SQZwL1rS9tFcVZoFiZyOGE72yItJy8girgqEbublEBM7BvN1KWKNluOv8tCv-dtymPQAqqcIIxGCkXKOXe3GOfqi7kOZvL0gi-Gw3uj_uYRqIg04mwSDtdihq7GSt9CCQL0ZrFqfUE7SGrLDoQ0Xux3LhjGUbURvuFQBMAvtDcCY6T_tlCx0-VeTT4myefXa-uR7McObtraaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac706e15a.mp4?token=vguQUqS6tz6qUPWiwZSqyJeGBj1EZ_7RkKgAPi3297ahIY-JKkoGcFo7vh3YUSkO3kpR-VWzLAlFBXQHJzvAUwUU7DkXxrDoFyDe7KUCOi61Ht5klq9W949CjJm5Vi8fp8Vni1S06SQZwL1rS9tFcVZoFiZyOGE72yItJy8girgqEbublEBM7BvN1KWKNluOv8tCv-dtymPQAqqcIIxGCkXKOXe3GOfqi7kOZvL0gi-Gw3uj_uYRqIg04mwSDtdihq7GSt9CCQL0ZrFqfUE7SGrLDoQ0Xux3LhjGUbURvuFQBMAvtDcCY6T_tlCx0-VeTT4myefXa-uR7McObtraaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
روایت‌های شما از دلایل تجرد | چرا ازدواج نمی‌کنیم؟
🔹
صدای شما از چالش‌های واقعی زندگی؛ بازتاب موانعی که جوانان را از تصمیم برای ازدواج دور کرده است.
🔸
پیام های صوتی خود را به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/akhbarefori/684490" target="_blank">📅 16:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684489">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
سردار شکارچی: می‌توان رسانه‌های معاند را در بانک اهداف نظامی قرار داد
سخنگوی ارشد نیرو‌های مسلح:
🔹
رسانه‌هایی مانند بی‌بی‌سی، ایران‌اینترنشنال و رادیو فردا مستقیماً به موساد، سیا و سازمان‌های اطلاعاتی دشمن متصل هستند و از آن‌ها خط کاری و پشتیبانی دریافت می‌کنند.
🔹
افرادی که در این رسانه‌ها فعالیت می‌کنند، سربازان صهیونیسم و آمریکای جنایتکار محسوب می‌شوند و حتی می‌توان آن‌ها را در بانک اهداف نظامی پیش‌بینی کرد؛ زیرا از نظر ما این‌ها رسانه نیستند.
🔹
هر خون‌ریزی و خشونتی در عالم با پشتیبانی این شبه رسانه‌ها انجام می‌شود؛ این شبه‌رسانه‌ها منشأ ترویج، تبلیغ و گسترش خشونت در جهان هستند و روان بشریت را برهم ریخته‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/684489" target="_blank">📅 16:50 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684488">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aad3ad1d78.mp4?token=jaBkf52riOp-VEgArPpkus-Mjztl0n1L8zfPBXpgiSu_OKCYFj-xfBVj2Cdt6qdPB-Re80IXOaU5HUeivayeI6U-ZUEMl8tMJ-LsC_zIsB4hY_SEAzaAf5KhJ3MbKamwariakxqzxrcAV6t2LUuKY7CDad1S8M2DOJhpGOc7RfWGSynuYg2u-f11hKnYYiKS-ay1-Zd8AFbJ3pCYW8XyjnrPX3YJRUJfCaw6urodGhpMvNPUw8KBj7DU-qGAKA1qbyCLdPsR6oqfJFdxSi3eDC3mmzt55dWBz6aLqETtWaqSQdsI2J2ucp_Eu_2FZTJZvHQcWijXaY5MLBcSpZ9LKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aad3ad1d78.mp4?token=jaBkf52riOp-VEgArPpkus-Mjztl0n1L8zfPBXpgiSu_OKCYFj-xfBVj2Cdt6qdPB-Re80IXOaU5HUeivayeI6U-ZUEMl8tMJ-LsC_zIsB4hY_SEAzaAf5KhJ3MbKamwariakxqzxrcAV6t2LUuKY7CDad1S8M2DOJhpGOc7RfWGSynuYg2u-f11hKnYYiKS-ay1-Zd8AFbJ3pCYW8XyjnrPX3YJRUJfCaw6urodGhpMvNPUw8KBj7DU-qGAKA1qbyCLdPsR6oqfJFdxSi3eDC3mmzt55dWBz6aLqETtWaqSQdsI2J2ucp_Eu_2FZTJZvHQcWijXaY5MLBcSpZ9LKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید ماشین ظرفشویی چطور کار می‌کند این ویدیو را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/akhbarefori/684488" target="_blank">📅 16:48 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684487">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
جشن روز ملی ارس؛ شکوه یک رویداد ملی
🔹
جشن بزرگ روز ملی ارس با حضور پرشور مردم و ارسوندان، خانواده‌های معظم شهدا، مسئولان و فعالان فرهنگی و گردشگری به همت سازمان منطقه آزاد ارس برگزار شد؛ شبی که یاد شهدا، موسیقی، هنر و معرفی ظرفیت‌ های تاریخی و گردشگری ارس در کنار هم قرار گرفت.
🔹
از اجرای چنگیز حبیبیان و گرشا رضایی و رونمایی از آهنگ «ارس» تا تجلیل از خانواده‌های شهدای مرزبانی سال ۱۳۲۰ و شهدای جنگ ‌های ۱۲ و ۴۰ روزه، رونمایی از آثار فرهنگی و گردشگری و پوستر جشنواره ملی عکس ارس و اهدای ۱۵ دستگاه دوچرخه و یک دستگاه خودروی MG5 در قرعه‌کشی میان شرکت کنندگان.
@arasfz
.ir</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/684487" target="_blank">📅 16:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684486">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
ترامپ به الجزیره: برای مذاکره با ایران «عجله‌ای ندارم»
ادعای ترامپ:
🔹
هم اقدامات اقتصادی و هم نظامی در مواجه با ایران «موثر» هستند.
🔹
او در پاسخ به سوال خبرنگار الجزیره، افزود که «من هیچ برنامه زمانی ندارم، عجله‌ای ندارم».
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/akhbarefori/684486" target="_blank">📅 16:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684485">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2dd13e4d1.mp4?token=ovDlS9IzQwvRk7qP9gWsqM4XpFm9-1bImWYtrgRreioVoMVkbCiFMhIOJntwbg8wI2zTLqw6MDEJKg2MLfdn4FHH0nKu7AOM2KnNF0hbQkuv9p7mH1SxuTGmN1rdCwN2ed4b_yDqP3ymWgcsnkqyKO0vqebGWbEIMtjEI-pzSBAAze7143vMiF-TogeikfP5X0CUI1Pk2Swfs88wQ-v4QBV_sLFYHRSHEuDULgk5V7c-9G0Ygw0ZGYFP6v4SAei71R017KC0clYC_Cv3izZsMQhjPnadS8lsMgBHaa6Q5uOqnqlCdqpucHn4FNpWfoAg1-l8hkdLaim1mA6OuL9bvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2dd13e4d1.mp4?token=ovDlS9IzQwvRk7qP9gWsqM4XpFm9-1bImWYtrgRreioVoMVkbCiFMhIOJntwbg8wI2zTLqw6MDEJKg2MLfdn4FHH0nKu7AOM2KnNF0hbQkuv9p7mH1SxuTGmN1rdCwN2ed4b_yDqP3ymWgcsnkqyKO0vqebGWbEIMtjEI-pzSBAAze7143vMiF-TogeikfP5X0CUI1Pk2Swfs88wQ-v4QBV_sLFYHRSHEuDULgk5V7c-9G0Ygw0ZGYFP6v4SAei71R017KC0clYC_Cv3izZsMQhjPnadS8lsMgBHaa6Q5uOqnqlCdqpucHn4FNpWfoAg1-l8hkdLaim1mA6OuL9bvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: در بدترین وضعیت جنگ اقتصادی هستیم
🔹
ما در بدترین وضعیت جنگ اقتصادی هستیم؛ یعنی جنگ موشکی را همه می‌بینند، اما فشارهای اقتصادی شاید به این راحتی احساس نشود.
🔹
کاری که در چنین فضایی و در چنین جنگی انجام می‌شود واقعا قابل قدردانی است. شاید اگر زمان عادی بود این‌قدر نمی‌توانستیم کار کنیم؛ الآن علی‌رغم اینکه تحت فشاریم و در جنگ هستیم، این دستاوردها قابل قدردانی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/684485" target="_blank">📅 16:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684484">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ8naRvWy9sDazKksV-VcaQkwXOexCEYsLplIRFq4jpUZEoCPPVthsvRp9QqWf0JNhakYiWYQNgxeAbtm7wbYodUYxf_OLLiCyALyKza_ZWtB4pNLtXCeKeBzsCBQ9tazUarfY4He2HJ8QCPh1H-KKDqZkSRNBoPmbAb-ondVK3P0WJlIwhxsutPDmSfFG5YjG7RUPW_wxreHWJ0k0lwo37tec64x2dPJm5eYFXoJSsa85uh3Zmy4SPefucNAgjpYVs65e-skFCq-qCvz57NcMBEN8WOuHcmFD4VmCW6jiWnmwlltggtc94YY32ElaVmQzB-DyBQRxWYOl69gLBX2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در پی انتشار ویدئوی نقشه ترور پسر رئیس‌جمهور امریکا، شبکه‌های خبری امریکا از جمله سی‌بی‌ان نیوز با انتشار فراخوانی از حامیان ترامپ خواستند برای محافظت از او دعا کنند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/684484" target="_blank">📅 16:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684483">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2be2734fad.mp4?token=PqCEMpQe7GeEZY1gtYktMDnYM6L3tSRXBXUZpNwDBGbqh5gKfREdzRg3NuTPDbpiWP6L8ASTEc2s3hI23s1k3Z96pkwwae8-LnS9Cm91CZnSn-w1nXNU-0MDLhPqSTUYP0GD_mhvmJ3JeLei7ZRKbN7Xo_cfsS7TmyyVOT-UpLCxR52ThyVtTzolNjhToOq9TMKHHzAmopNkU-G8jTEsHguhRrwWSDZ_8cpuZ6NupBAaLHwo22qTO80WJL38t6S6_ZU0qB3mHZGH6fSFBAmW6H0tvDUuO17-I6-4HJcywtxjh-HHMZDy9Sh2R7HBVEpaX8-v-Q7yVkiD-3Z1muZT0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2be2734fad.mp4?token=PqCEMpQe7GeEZY1gtYktMDnYM6L3tSRXBXUZpNwDBGbqh5gKfREdzRg3NuTPDbpiWP6L8ASTEc2s3hI23s1k3Z96pkwwae8-LnS9Cm91CZnSn-w1nXNU-0MDLhPqSTUYP0GD_mhvmJ3JeLei7ZRKbN7Xo_cfsS7TmyyVOT-UpLCxR52ThyVtTzolNjhToOq9TMKHHzAmopNkU-G8jTEsHguhRrwWSDZ_8cpuZ6NupBAaLHwo22qTO80WJL38t6S6_ZU0qB3mHZGH6fSFBAmW6H0tvDUuO17-I6-4HJcywtxjh-HHMZDy9Sh2R7HBVEpaX8-v-Q7yVkiD-3Z1muZT0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طلا یا بورس؟ بررسی یک الگوی تکراری که حتی سایه جنگ هم نتوانست آن را تغییر دهد/
تلویزیون اینترنتی مدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/akhbarefori/684483" target="_blank">📅 16:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684482">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d77a7f9cc8.mp4?token=NuZ87rE76rFfYtiqC-26TUN4x5qZu65Pr_j4h05WgHg0ML3UQHvJcK2ynjBL2q7MDw0w5fCZFqVy2AVrAvUEo8rVWbgFMt9XCEGFLg-8eO70NK2JAIigNF2BTNJWPg_EV_gwcD7bU9FVqBbAqnyTnfSq4Enmq1PGV2PM6SP_hIKIqmY76d_PkslxiSgvwfjMfvCqAS9vGsjQBNuWF3dn2UaQeAIXekjVdpIwsTPfORWelag2985sZ4GS6-0TOsk71bEZIq2KzaFDfNq0dRjDbsOZp_We3tAy_7Hxr7a7xNzyOR7ndDvDeCQZwie5OuQILJIbARIpR-5O2XcJmKeQSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d77a7f9cc8.mp4?token=NuZ87rE76rFfYtiqC-26TUN4x5qZu65Pr_j4h05WgHg0ML3UQHvJcK2ynjBL2q7MDw0w5fCZFqVy2AVrAvUEo8rVWbgFMt9XCEGFLg-8eO70NK2JAIigNF2BTNJWPg_EV_gwcD7bU9FVqBbAqnyTnfSq4Enmq1PGV2PM6SP_hIKIqmY76d_PkslxiSgvwfjMfvCqAS9vGsjQBNuWF3dn2UaQeAIXekjVdpIwsTPfORWelag2985sZ4GS6-0TOsk71bEZIq2KzaFDfNq0dRjDbsOZp_We3tAy_7Hxr7a7xNzyOR7ndDvDeCQZwie5OuQILJIbARIpR-5O2XcJmKeQSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متفاوت‌ترین تبریک تولد
!
🔹
نگار هاشمی بازیکن تیم ملی والیبال ایران در جریان دیدار با عراق، هربار که دوربین او را نشان داد تولد پدرش را تبریک گفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/684482" target="_blank">📅 16:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684481">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f28dcbef.mp4?token=W28-iiV3P8pRgfxghtLkeVHzzfTa5yMl7oeHYX8aYLRtDa8QYO94-v-3oXXE-Id32PZQCeDIk4MMck6pEUeQK46eZwOzyTdPuTyecs6fNH-Dpx7SdISPW-bkd4eHj0U8OE0ak4QGHHwZhC5Lmpr9GkZ7in6aMjO2_dI9DhREajl26zWvk1lxHA7yQihdijWgGVFF39f2PBc4pxI2yOuKjZitSFmbmGPJ6-aQIuOnLQChXsPaoJTBLbMXBwH5W6K1iwVFfO9VHgXGUUIBhUj52M4GlSnWBnXgcTBZbgVLVycJTVO2Vloqq9iuxPiA9Xp9wmPrIYYRHkoYXQqKoKHn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f28dcbef.mp4?token=W28-iiV3P8pRgfxghtLkeVHzzfTa5yMl7oeHYX8aYLRtDa8QYO94-v-3oXXE-Id32PZQCeDIk4MMck6pEUeQK46eZwOzyTdPuTyecs6fNH-Dpx7SdISPW-bkd4eHj0U8OE0ak4QGHHwZhC5Lmpr9GkZ7in6aMjO2_dI9DhREajl26zWvk1lxHA7yQihdijWgGVFF39f2PBc4pxI2yOuKjZitSFmbmGPJ6-aQIuOnLQChXsPaoJTBLbMXBwH5W6K1iwVFfO9VHgXGUUIBhUj52M4GlSnWBnXgcTBZbgVLVycJTVO2Vloqq9iuxPiA9Xp9wmPrIYYRHkoYXQqKoKHn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سواد مالی و مدیریت پول مادران در خانواده از چیزی که فکرشم می‌کنید مهم‌تره #دارایی_هوشمند
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/akhbarefori/684481" target="_blank">📅 16:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684480">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/379bc087d9.mp4?token=rsKOIDIWhUKxUSFFnkuQXMUx_KoCN0MpGQ5YD1wnZbNmBVvWOrnowDGMhwHXonBIqMpjGUFS41HzmAr2zEE5K8sike5py-TCFxgMDEpRSye677JUjrlPu79hqbXnkNVwCWenp85_qxzRXhWQSLlDsRiFf-_hStGR5FGpILVGyBxWCXnJ_ZdhZrGMrpTwx0Q0NcBIoMyGNtHkmJPNeHRkEKXVsoBpr0twTIqMROQdWxHiqH8-TlHMPGHp5Jy2mqzRdQ5g8YRPx9brpa1SFpB1h_64lq9f-HGpmvcFP5sb97fx3EV8GwUerVTgm-ejTEBtD8ieVEuKnGGtBU7bmHpycA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/379bc087d9.mp4?token=rsKOIDIWhUKxUSFFnkuQXMUx_KoCN0MpGQ5YD1wnZbNmBVvWOrnowDGMhwHXonBIqMpjGUFS41HzmAr2zEE5K8sike5py-TCFxgMDEpRSye677JUjrlPu79hqbXnkNVwCWenp85_qxzRXhWQSLlDsRiFf-_hStGR5FGpILVGyBxWCXnJ_ZdhZrGMrpTwx0Q0NcBIoMyGNtHkmJPNeHRkEKXVsoBpr0twTIqMROQdWxHiqH8-TlHMPGHp5Jy2mqzRdQ5g8YRPx9brpa1SFpB1h_64lq9f-HGpmvcFP5sb97fx3EV8GwUerVTgm-ejTEBtD8ieVEuKnGGtBU7bmHpycA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزافه‌گویی
نتانیاهو جنایتکار درمورد ایران: به ترامپ گفتم اسرائیل با توافق خوب مشکلی ندارد؛ ولی توافق با این وحشی‌ها ممکن نیست
🔹
من به ترامپ گفتم ایران رو تشدید محاصره کن.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/akhbarefori/684480" target="_blank">📅 15:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684479">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90808e7a06.mp4?token=XC8ABTl9DrUa03AyBtZTtL0ViqoA-6dZOHNqwr_BoOlJ1nGacJU8m_7itTtwAyKlDlb1IuNQtUqJcguWe_-QjD0OUY_vXQeuKcqvWACd0n8AwWkppXC7jvMprkNvhoFMz3armuBTs1rznRo4BUZfYagQvl0MVJiomzIEVcuePRhbhGk-GEyIuZJH7AXqiCjsdFEEeBS-jxvETiek0Xwu2qmXXphynnp7Wv6mmTMtpbrfqcYvmtY7GTrP6rRFNlREjbpIjGbFSJ2bUjDthJYIKJT0qEDFioxtkgUff4s6yHrkaMno8Jt7anKmAqkVESgLq69KTBYjFNCJHaB_hlSbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90808e7a06.mp4?token=XC8ABTl9DrUa03AyBtZTtL0ViqoA-6dZOHNqwr_BoOlJ1nGacJU8m_7itTtwAyKlDlb1IuNQtUqJcguWe_-QjD0OUY_vXQeuKcqvWACd0n8AwWkppXC7jvMprkNvhoFMz3armuBTs1rznRo4BUZfYagQvl0MVJiomzIEVcuePRhbhGk-GEyIuZJH7AXqiCjsdFEEeBS-jxvETiek0Xwu2qmXXphynnp7Wv6mmTMtpbrfqcYvmtY7GTrP6rRFNlREjbpIjGbFSJ2bUjDthJYIKJT0qEDFioxtkgUff4s6yHrkaMno8Jt7anKmAqkVESgLq69KTBYjFNCJHaB_hlSbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: پیگیر بازگشت ایرانیان خارج از کشور هستم؛ معین هم یکی از شهروندان ایران است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/akhbarefori/684479" target="_blank">📅 15:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684477">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
از ملاقات با نوزاد در زندان تا بازگشت به دنیای سیاه؛ داستان باند ۳ نفره سرقت موتورسیکلت
🔹
داستان این باند ۳ نفره فقط یک گزارش سرقت ساده نیست؛ این یک تراژدی واقعی است. یکی از اعضای اصلی این باند، در حالی که در اولین دوره بازداشتش، شاهد تولد فرزندش در میان دیوارهای زندان بود، تصور می‌کرد همه چیز تمام شده است. اما بازگشت او به دنیای سیاه سرقت موتورسیکلت همراه با دو برادر، نشان می‌دهد که چرخه جرم چقدر بی‌رحم است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/684477" target="_blank">📅 15:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684476">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
نخست وزیر قطر به تهران سفر می کند
🔹
شیخ "محمد بن عبدالرحمن آل ثانی" نخست وزیر وزیر خارجه قطر قرار است به زودی به تهران سفر کند. این سفر احتمالا فردا پنجشنبه و در چارچوب میانجیگری میان ایران و آمریکا صورت می گیرد.
🔹
در چند روز اخیر هم فرمانده ارتش پاکستان و وزیر خارجه عمان نیز در همین چارچوب به تهران سفر داشتند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/684476" target="_blank">📅 15:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684475">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00dee499cc.mp4?token=eNlbSe0Q9XPoGBzE_G12a0yNwXgm4B5zfv7phh_dCBqsSxP8mkVqRUlTMYYPdB_dESZ_I7IqrF3R0rGGSQyzNrTlsDKmdmiyilrbHlL5OcGI5DxCzy2WYjK6AXuTk5V-GcNxsBPLSTO6N_k5AA6Isv1x2tgueQSJpOPpiCa3HdmAyrWL7at0oskFOcQRtbvKSsvTgcweLW2agP3ru5QKNdH3BqifXctLVoBSLqMPlG8dIUFGr1MfIHzOf2ShG2oxcq0o2UoKlCk2Cufb2X1oaaMWeVIjvdfB1gUMr38d1d3EydxnGfmwkmANyJpJd-6zLoCyptQJJiUeiGrSVegDdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00dee499cc.mp4?token=eNlbSe0Q9XPoGBzE_G12a0yNwXgm4B5zfv7phh_dCBqsSxP8mkVqRUlTMYYPdB_dESZ_I7IqrF3R0rGGSQyzNrTlsDKmdmiyilrbHlL5OcGI5DxCzy2WYjK6AXuTk5V-GcNxsBPLSTO6N_k5AA6Isv1x2tgueQSJpOPpiCa3HdmAyrWL7at0oskFOcQRtbvKSsvTgcweLW2agP3ru5QKNdH3BqifXctLVoBSLqMPlG8dIUFGr1MfIHzOf2ShG2oxcq0o2UoKlCk2Cufb2X1oaaMWeVIjvdfB1gUMr38d1d3EydxnGfmwkmANyJpJd-6zLoCyptQJJiUeiGrSVegDdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر کنجکاو هستید بدانید نیروگاه های برق‌آبی(تولید برق از آب پشت سد) چطور کار می‌کند این ویدیو را ببینید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/684475" target="_blank">📅 15:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684474">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">♦️
جزئیات تحریم‌های جدید دانشگاهی علیه ایران
دفتر کنترل دارایی‌های خارجی وزارت خزانه‌داری آمریکا (OFAC) با انتشار سندی:
🔹
واشنگتن فعالیت‌های ورزشی و تبادلات دانشگاهی با ایران را به‌طور نامحدود متوقف کرده است.
🔹
این تصمیم سرنوشت آزمون‌هایی مانند تافل و GRE در ایران را با ابهام مواجه کرده است./ شفقنا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/684474" target="_blank">📅 15:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684473">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
آخرین وضعیت تنگه هرمز از زبان سخنگوی سپاه پاسداران؛ اگر آمریکا شرایط ما را نپذیرد، تنگه هرمز به‌هیچ عنوان باز نخواهد شد
سخنگوی سپاه پاسداران:
🔹
تنگه هرمز در اختیار ماست و هیچ شناور نظامی دشمن داخل خلیج‌فارس حضور ندارد؛ تمام شناورهای جنگی دشمن دست‌کم ۴۰۰ کیلومتر از تنگه هرمز فاصله گرفته‌اند و از نظر نظامی و سرزمینی، هیچ شناوری بدون اجازه و مدیریت ایران قادر به عبور از این آبراه نیست.
🔹
آبراهی که در نزدیکی عمان قرار دارد نیز به‌طور کامل تحت کنترل ماست.
🔹
تنگه هرمز متعلق به ایران و کشور عمان است که مقابل ما قرار دارد. ما حدود یک ماه پیش با عمان وارد مذاکره شده‌ایم و به نتایجی رسیده‌ایم که مورد قبول دو طرف قرار گرفته است.
🔹
در این مذاکرات درباره میزان سهم هر یک از دو کشور از آب‌های تنگه و سهم ایران و عمان از درآمدهای آن توافق‌هایی صورت گرفته است؛ آمریکا در این مسیر کارشکنی می‌کند و همین مسئله موجب شده است روند کار به تأخیر بیفتد.
🔹
اگر آمریکا کارشکنی را کنار بگذارد و به تفاهم‌نامه بازگردد، می‌توانیم در چارچوب تفاهم انجام‌شده، تنگه هرمز را باز کنیم، بنابراین شرایط ما باید از سوی آمریکا پذیرفته شود؛اگر آمریکا شرایط ما را نپذیرد، تنگه هرمز به‌هیچ عنوان باز نخواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/684473" target="_blank">📅 15:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684472">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW5bdiev8Ty8FsL5YYR2Pvqj3TAPa2nsP7Y0K39QzVjnkNUSkRnGr4AMQTcmccuKZZXBvLZnSJTpWBC3Ta48guxW-Zxwr_EOKr4xCFnDhwvB4AV_EVDIlcB-e3UOdmM9soKYcyyG2-xoAV5IyoEu45FtwYDcoWT7ImvfTaV7jIkfV9UsnPmBrVg9EB91suehbpjnPaBe_zqJ9Vj7j5sD0m3h_WpnRwEQx4YMe9TUcoxYIMAcBhR6Yh9bIiZ2cXYrJ0Ou-Zr73K5gZWZXL99i24gw-DauYX0f_KJbHrh6DgGtxjPufVpqx5JCUHT614h2TnHgfiTArNAPl68iHpZfYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد فروش در تاریخ شرکت پتروشیمی امیرکبیر شکسته شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/684472" target="_blank">📅 15:13 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684471">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1432aaa5a8.mp4?token=BMr7H0irIuvBZc06Ltf0-vldXzdpDoBnLQ76rEL8jWM6VRDXMgBBQOkWmaOdTLPgyOaSNTH3GJxxrtvrabAY-Lw4JqyfVBDLbT2lCZrkEaO-s7oM-ujWVRiNwXhHnYISYaJ2m3cp9CcAB_hZQaxjiXeMflr1Xvj6fdLXuVYjIQMIVI_Ifwf33gOmfEiBSeWv5z5D1OrPfywgv3FTtaKAzd19DZ6fKuNK3ZG7spoEezUU1R4LJH1q2NqNWrYYMS9mAj0AStxPrWwUTbjssm0Cc4SYkJr1qoc0GZueL1BPkRj3wNWXEEO2fk2ja_-PK5E2I-6VSS2cTkMcJmsiGa2m8XMuoZR1ur30JunYEuwmkDkXM2UkMDRZsosSpUErvwyFVb1hzT4_tCIUh402BX7m3NnfrBPeBQ8fqQl5zNmO6Oy45VxqzVvLUC-KQrLQu40puC8mvg12XO7s6r-MdrZpcEgcmTSot4dF04ysLNcHIrpI_nYAE7_8z05VIbOaVabb3l7jL-IZNRFKsb93ocUw9sd4aHZNsIY65obGAKl33p8Yu9l0NO9Y-Ypp0OVDVvD4UZ0hlufQTvyco8vZbXeaBDsbpsxrRNvo-VjoUh3z2HSCjyndjVS65EVplhDc_2DAXVsIo3HAUR4SM-25E1SfEk0Fb8tKISUtUYlVL3TUcsU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1432aaa5a8.mp4?token=BMr7H0irIuvBZc06Ltf0-vldXzdpDoBnLQ76rEL8jWM6VRDXMgBBQOkWmaOdTLPgyOaSNTH3GJxxrtvrabAY-Lw4JqyfVBDLbT2lCZrkEaO-s7oM-ujWVRiNwXhHnYISYaJ2m3cp9CcAB_hZQaxjiXeMflr1Xvj6fdLXuVYjIQMIVI_Ifwf33gOmfEiBSeWv5z5D1OrPfywgv3FTtaKAzd19DZ6fKuNK3ZG7spoEezUU1R4LJH1q2NqNWrYYMS9mAj0AStxPrWwUTbjssm0Cc4SYkJr1qoc0GZueL1BPkRj3wNWXEEO2fk2ja_-PK5E2I-6VSS2cTkMcJmsiGa2m8XMuoZR1ur30JunYEuwmkDkXM2UkMDRZsosSpUErvwyFVb1hzT4_tCIUh402BX7m3NnfrBPeBQ8fqQl5zNmO6Oy45VxqzVvLUC-KQrLQu40puC8mvg12XO7s6r-MdrZpcEgcmTSot4dF04ysLNcHIrpI_nYAE7_8z05VIbOaVabb3l7jL-IZNRFKsb93ocUw9sd4aHZNsIY65obGAKl33p8Yu9l0NO9Y-Ypp0OVDVvD4UZ0hlufQTvyco8vZbXeaBDsbpsxrRNvo-VjoUh3z2HSCjyndjVS65EVplhDc_2DAXVsIo3HAUR4SM-25E1SfEk0Fb8tKISUtUYlVL3TUcsU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
معماری ایرانی یکی از بهترین نمونه‌های معماری در جهان که از دل اقلیم، جغرافیا و نیازهای محیطی شکل گرفته
#حواست_هست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/684471" target="_blank">📅 15:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684470">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d563470688.mp4?token=LRWvjPLx3DJzSIf1vX-lGY7TNeHPpZq0zhr5frUvQUxrWpq6A8lOZdn9A6j8U-2ZxgHK9AbowvJYm1TpF_GtwW_tcvVQS5m6vbxtdX328kq1xCo-cWoNu-kseHvJ61oiSKFKWvFH3q7rXVcyQ7maQuQoRbhbd8iYgN2OZytdgm8SJhpp0OuJqpP56Kf83nXHGX_7t_1fwok5uJEr9Sog-QcgLk9SOegghCv0o06PlS419nftEOTpRXJwSXygR_oI-95n0Prblh0hQiWytGzBMUwaLXwWE4gM_ZoZn6ucq66xl2dpjrtpDU06bZceRmHnpWzyqN7cKbFOnt4-eP-YPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d563470688.mp4?token=LRWvjPLx3DJzSIf1vX-lGY7TNeHPpZq0zhr5frUvQUxrWpq6A8lOZdn9A6j8U-2ZxgHK9AbowvJYm1TpF_GtwW_tcvVQS5m6vbxtdX328kq1xCo-cWoNu-kseHvJ61oiSKFKWvFH3q7rXVcyQ7maQuQoRbhbd8iYgN2OZytdgm8SJhpp0OuJqpP56Kf83nXHGX_7t_1fwok5uJEr9Sog-QcgLk9SOegghCv0o06PlS419nftEOTpRXJwSXygR_oI-95n0Prblh0hQiWytGzBMUwaLXwWE4gM_ZoZn6ucq66xl2dpjrtpDU06bZceRmHnpWzyqN7cKbFOnt4-eP-YPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس سازمان اداری و استخدامی كشور: حقوق نیروهای شرکتی، قراردادی و رسمی از این ماه مستقیم پرداخت می‌کنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/akhbarefori/684470" target="_blank">📅 15:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684469">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd0097cd7.mp4?token=kKHxkuWRSumSloLAq3FyJ78mOPoBzL30XO9PxiF60EyuMkqubrVuW35WqXswZedYt3PWmJ01EcMs0GR4fZ6z2saFawAqCdOCDilWOpdmZwLt7fgevHHENG6LEpLZz9d09KJ-d_egGg1hmAOF3ZSs3J_p2pre16l8esrR_c-VW_SzxlHSq0nGsLwO7cbgTvcKikINVMXZlUsARIOVOpwqDiwazARNbBDdULS5ujGoK398M8js4qFKKs5A9jSFuIz4wvVUxEWK4A0Yl7ffGrDccSq-zbWREUjYkG1P0J4m97aVttbcpESIirRZNTLDr0LosrSWoHwTSJqnvt43UWpniQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd0097cd7.mp4?token=kKHxkuWRSumSloLAq3FyJ78mOPoBzL30XO9PxiF60EyuMkqubrVuW35WqXswZedYt3PWmJ01EcMs0GR4fZ6z2saFawAqCdOCDilWOpdmZwLt7fgevHHENG6LEpLZz9d09KJ-d_egGg1hmAOF3ZSs3J_p2pre16l8esrR_c-VW_SzxlHSq0nGsLwO7cbgTvcKikINVMXZlUsARIOVOpwqDiwazARNbBDdULS5ujGoK398M8js4qFKKs5A9jSFuIz4wvVUxEWK4A0Yl7ffGrDccSq-zbWREUjYkG1P0J4m97aVttbcpESIirRZNTLDr0LosrSWoHwTSJqnvt43UWpniQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وطن در دل آدمی باید باشد
🇮🇷
🤍
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/684469" target="_blank">📅 14:56 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684468">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d33b77b6e.mp4?token=a9aqOCv3zb4R4XqS6qtDGLnPOC49_BNBqGoaNOgaufFMR3IlzgdTp5XB5QXdiKV5JxbN9r48PGAfNJR4QfYnF81tjeSU262e0rKytsQ_g3PXNNlWHotvNAL9qvQwS_5nRSgHzZMhWYzQIfbZh4U1m9o8hN-a_SQ2WUVf0A2DCN7KLBKhHNSGhE7mouweYsa16KK6gITNBZOB1S_9K2SMdExe1lAFBK-OTr7293PMr95U0lw4u838ByR7CzCtzdfX4OMbIMgzP409FPHfjCJ3PUiNJkIDwFKqsMWF-FEu17RL7qdv2g5pUmLbH0wUcinmI23koK-YDlKeF9mhm25yww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d33b77b6e.mp4?token=a9aqOCv3zb4R4XqS6qtDGLnPOC49_BNBqGoaNOgaufFMR3IlzgdTp5XB5QXdiKV5JxbN9r48PGAfNJR4QfYnF81tjeSU262e0rKytsQ_g3PXNNlWHotvNAL9qvQwS_5nRSgHzZMhWYzQIfbZh4U1m9o8hN-a_SQ2WUVf0A2DCN7KLBKhHNSGhE7mouweYsa16KK6gITNBZOB1S_9K2SMdExe1lAFBK-OTr7293PMr95U0lw4u838ByR7CzCtzdfX4OMbIMgzP409FPHfjCJ3PUiNJkIDwFKqsMWF-FEu17RL7qdv2g5pUmLbH0wUcinmI23koK-YDlKeF9mhm25yww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماهی ماندارین؛ یکی از رنگارنگ‌ترین ماهی‌های جهان
🐠
🔹
ماهی ماندارین یا «اژدهای ماندارین» ماهی کوچکی از آب‌های شور اقیانوس آرام است که با رنگ‌های درخشان آبی، نارنجی و سبز و طرح‌های مارپیچی شناخته می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/684468" target="_blank">📅 14:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684465">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d668cb3f77.mp4?token=fWRdcPqSXLFi4aeEGp6R5JaJkljV9iMAqEPHCj9LZOUcqSSk5NjYsqpjDbvIl71WVZMKOTLLak317MUgzCpzmirSr8BY4ijk-dFQN_iHhtcwfSa7tfKMyiC60yeIU1yeyjd8cutvig4PitjhitDnYDAkh_P4kBRo4WCvMMqKyPdSLfeInTM2yA4jVN3Y2kTAkdVMpg4HaPSxCwUrm484XAxPSgABxWQi5p1JlCC5GtnoN04kG7JaSXKaHEZXVpcpzaCIQ2R5pXGlMyTcTlmbxZ6BtSXw4uE0Snw-KLr7M_pH-SWyDH94qhsXkToagOfN7OdAdb-V0M_I1OE4sSoSXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d668cb3f77.mp4?token=fWRdcPqSXLFi4aeEGp6R5JaJkljV9iMAqEPHCj9LZOUcqSSk5NjYsqpjDbvIl71WVZMKOTLLak317MUgzCpzmirSr8BY4ijk-dFQN_iHhtcwfSa7tfKMyiC60yeIU1yeyjd8cutvig4PitjhitDnYDAkh_P4kBRo4WCvMMqKyPdSLfeInTM2yA4jVN3Y2kTAkdVMpg4HaPSxCwUrm484XAxPSgABxWQi5p1JlCC5GtnoN04kG7JaSXKaHEZXVpcpzaCIQ2R5pXGlMyTcTlmbxZ6BtSXw4uE0Snw-KLr7M_pH-SWyDH94qhsXkToagOfN7OdAdb-V0M_I1OE4sSoSXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا حمام هتل‌ها همیشه تمیز می‌ماند؟
🛁
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/684465" target="_blank">📅 14:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684464">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
قیمت دلار با کارت ملی مشخص شد
🔹
نرخ پایهٔ دلار برای خرید با کارت ملی امروز ۱۹۵ هزار تومان اعلام شد؛ دلار در بازار آزاد نیز ۱۹۸ هزار و ۵۰۰ تومان معامله می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/684464" target="_blank">📅 14:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684463">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bcf9e2aeb.mp4?token=hDorX9ILw8kczvWUswqDMY6fhryZdlAiPVVfJt072Ammw4VQ7A4t7kCM44wRaym5aJvrWy8xFCTUmP9-a1zhfFpptkZiDvagH0r9yCO3EneL5petTO2gGJM9ko1d3_qQVkTPWN64L4X2TCmTI00z98rHeqe39WtXL75ezpu9riWhkWC-cYMT6X51iOQTW6tBPtttqMuSPm0JBXS_dHhzCBDKMi6ThftAdx81p1_RCDqRFf-ZeFwu-AsSpwmCLE-di4-DTRkMTN5vIL_teAnAVLesScc6TuP2LUZS8wDx9Z6ID2sfbRSQXBf6N6TOJJ3jaiqbQEu6tXjWnQBWLOISQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bcf9e2aeb.mp4?token=hDorX9ILw8kczvWUswqDMY6fhryZdlAiPVVfJt072Ammw4VQ7A4t7kCM44wRaym5aJvrWy8xFCTUmP9-a1zhfFpptkZiDvagH0r9yCO3EneL5petTO2gGJM9ko1d3_qQVkTPWN64L4X2TCmTI00z98rHeqe39WtXL75ezpu9riWhkWC-cYMT6X51iOQTW6tBPtttqMuSPm0JBXS_dHhzCBDKMi6ThftAdx81p1_RCDqRFf-ZeFwu-AsSpwmCLE-di4-DTRkMTN5vIL_teAnAVLesScc6TuP2LUZS8wDx9Z6ID2sfbRSQXBf6N6TOJJ3jaiqbQEu6tXjWnQBWLOISQ4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسکن استیجاری برای جوانان
۳۰۰۰ واحد در تهران و خراسان رضوی به جوانان تعلق می گیرد.
آخرین مهلت ثبت نام امروز می باشد.
@Titretejarat</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/684463" target="_blank">📅 14:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684462">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSh2fUvoyYkpzLk4SNp0b4go8o6rm_s7Q5xroIb-V9BlUq2uMUxNB2_2GyuIX8mqrEqCdfxs2Pha_ttHg1MClJ7pUHXzfAnshw9yMbMaRKMatH2mn4ILZ3EvOK_ELER0oHjfPn3dbwajC8LV-vpiVXuNzQ8ysj9ukYN8st3DG2_KfIhmcyEyRklntmfiqWYBJZtjqtzNvH0-18s6XBzH8v3oo1gnMPZOGl2EBkAcQ1KbbAmg5t8Lv4_hKB8I5C0R5ZqkxUsTP_psmC3DbKCAEUpzrpQxeeMREFf8n3uxXD0ARpKiFkkSsQ08gVH7p71ecSqYWr1kB0mTZxy1h0Jafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیاین خودمون بنگل و دستبندهای رنگی‌رنگی درست کنیم تا استایلمون شیک‌تر بشه #استایل_فوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/684462" target="_blank">📅 14:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684461">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pmoI3Y9WF3vjkWw1wWbOQHXBPGz5hItAruxrZ0Ok2ft8g7K0O9ctLHSbYil8GzUfWAIfAL2Avd9zpQ1EUVfbhmr1Eymd8ca5W8x6FvEIsCiyNZJChUdpB0lpwgtrNAMAkAcwnW2DY9nDYuNOh_P5zs6BmslRA-w6O5baXx7ll76uL7hQTXUkuTFGZf14_RFFjm_iVvr6TQ7RqusKQNU2ifALtVNR2Ip9rcFc_eTKXX6A-QQMZUHaExM5cziJSL--blLrUbcS2HId_t82lCdbJv-V_hz88nLVuIP8dGLGCLrBLnJZlFAB-vaGWg7GPP5J2tlytmTodfJMUTcVcgIs2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هر شب، 1 میلیارد تومان جایزه نقدی!
🎉
شب‌های میلیاردی اسنوا شروع شد
🎉
—— 5 جایزه 200 میلیونی برای 5 نفر ——
با خرید از اسنوا، علاوه بر دریافت هدیه و تخفیف حین خرید، در هر یک از شب‌های جشنواره، شانس برنده شدن ۲۰۰ میلیون تومان جایزه را خواهید داشت.
💰
⏳
فرصت خرید، فقط تا پایان شهریور
❗️
🔥
شرایط شرکت در قرعه‌کشی و جزئیات جشنواره رو همین حالا ببینید:
👇
👇
👇
https://s.shdk.net/snowa-telegram</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/684461" target="_blank">📅 14:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684460">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاتاق بازرگانی تهران</strong></div>
<div class="tg-text">▪️
مشاوره مالی اتاق تهران همراه بنگاه‌ها در دوران بحران
🔺
اتاق تهران با ارائه مشاوره تخصصی و رایگان در حوزه مالی، به بنگاه‌های اقتصادی کمک می‌کند با بهره‌گیری از روش‌های متنوع تأمین منابع، استفاده از ظرفیت‌های حمایتی و تصمیم‌گیری مالی هوشمندانه، تاب‌آوری خود را افزایش دهند.
👈🏻
کسب اطلاعات بیشتر: ۳-۸۸۷۱۴۴۷۲(۰۲۱) و
www.tccim.ir</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/684460" target="_blank">📅 14:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684458">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
شرکت ملی پخش فرآورده‌های نفتی:۱۲ میلیون لیتر بنزین بیشتر در راه است
.
🔹
فرمانده پدافند هوایی ارتش: توانمندی‌های خود را در عمل نشان خواهیم داد.
🔹
رویترز: صادرات LNG قطر ٩٨ درصد کاهش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/684458" target="_blank">📅 13:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684457">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
سخنگوی ارتش: قطر از سرنوشت خلبانان سوخو اظهار بی‌اطلاعی کرده است
سخنگوی ارتش:
🔹
پیگیری‌ها از طریق وزارت خارجه، ریاست‌جمهوری و دولت و ارتش قطر انجام شده، اما طرف قطری تاکنون از سرنوشت خلبانان اظهار بی‌اطلاعی کرده است.
🔹
وی خواستار پیگیری جدی‌تر و ارائه پاسخ روشن و مستند از سوی قطر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/684457" target="_blank">📅 13:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684455">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30952a8d65.mp4?token=s6tkxQNyZNHAVxAYHrCtrgI150e8ZatViJLuNvPZOrdaVPZkP7JFZLDOhWpYB00oih3GwO4QNeB_VBv3COPM3HydaiCo4KaabpItoo57s6rG7zmLTdsZHEoDtht5GFUaJ4nIRW_EcNnDiGJLnnnhkNqFH-Z-1aPu5eXgGKOW6v6lw098YWOvi_NA4ajLAkBPj1xaaIZ7uBdaGtKcrdfi007X6RZ2j-F5xRceo95dZiIsTgEr5-Mhgxy5y-4v4YgvYCvpJY-hLecBTx9u1K4-S88tnqNvaewRLclZAxCO3FqcSi0ONlbhI8OLooLOUUXR6BiZONkbDn7NfNvPs6X-2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30952a8d65.mp4?token=s6tkxQNyZNHAVxAYHrCtrgI150e8ZatViJLuNvPZOrdaVPZkP7JFZLDOhWpYB00oih3GwO4QNeB_VBv3COPM3HydaiCo4KaabpItoo57s6rG7zmLTdsZHEoDtht5GFUaJ4nIRW_EcNnDiGJLnnnhkNqFH-Z-1aPu5eXgGKOW6v6lw098YWOvi_NA4ajLAkBPj1xaaIZ7uBdaGtKcrdfi007X6RZ2j-F5xRceo95dZiIsTgEr5-Mhgxy5y-4v4YgvYCvpJY-hLecBTx9u1K4-S88tnqNvaewRLclZAxCO3FqcSi0ONlbhI8OLooLOUUXR6BiZONkbDn7NfNvPs6X-2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیل ویرانگر در نپال؛ ۸ کشته تاکنون و مفقود شدن ده‌ها گردشگر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/684455" target="_blank">📅 13:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684454">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGvt5mIxRyq7FB7XDSB0aomoajnTmiQyESXectcqO-pnW5wcwN-A6op7hehDLFXbOA2AKug0YySN1ksuuQqIp-EC7miQDKb0Ws626UH_SxmytmcNJZUAAIbWv8Ww9hlYAhzWsqCDAbqlbK7E1fSFupvH42aQqKWHZ_DXnM40fNBL9sJihNjrbNSKQ4XoqIAGIJAMcdpa6Gf0vQpA5V__3Rywg2SLne0kOa0RHaxzes7iRgZ8ueK52_yFjVE1uOjOWMyfKoFc7ePvyJALAmsrK2n7IMZsIgd3rfMsVbDDdQVbQojtJbFF8pd3jSdvlAo5WN0SZ9WCpjbch92uLrfk7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دیپلماسی جاسوس‌ها؛ رمزگشایی از سفر رئیس سیا به مسکو | یا توافق نزدیک است یا اوضاع خیلی وخیم!
🔹
سفر غیرمنتظره جان رتکلیف، رئیس سازمان اطلاعات مرکزی آمریکا، به مسکو بار دیگر یکی از قدیمی‌ترین ابزارهای دیپلماسی میان واشنگتن و مسکو را فعال کرده است؛ کانالی که در دوره‌های اوج تنش سیاسی، گاهی از مسیرهای رسمی دیپلماتیک مؤثرتر بوده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3240619</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/684454" target="_blank">📅 13:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684453">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/454460bfe4.mp4?token=BK4B5TcuXcbnqIwVTnnKaysXzZpRozum0D0AVjz4tg0kdTzX0sQfSHjOBFfmjFZM8Ih_EOaxbPEWttOgWyKgVuhOHlR0bgcRqgz9ZoOswaiQlxcMjzR6gQ8Ntclco0peAnDhIQ2yZn3-DEr8NcH-EjR5nF2e8G7s2Q9xon5fMzb03tkhWzMNTYN44_4aj8pfQJdTTOQNxQYV2FRmtplgEuvb_RHk6paj-ZjeYc1lCp-x681s0TAC8pFLwexjINa4S4JEY3-k7pNUnXvnGyx7AtEemJfHyi3FJNUHWCHGn3DE1auxV4dDu1C6gNORqaoc64Oc6FSr6qbYlOPgC-jhsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/454460bfe4.mp4?token=BK4B5TcuXcbnqIwVTnnKaysXzZpRozum0D0AVjz4tg0kdTzX0sQfSHjOBFfmjFZM8Ih_EOaxbPEWttOgWyKgVuhOHlR0bgcRqgz9ZoOswaiQlxcMjzR6gQ8Ntclco0peAnDhIQ2yZn3-DEr8NcH-EjR5nF2e8G7s2Q9xon5fMzb03tkhWzMNTYN44_4aj8pfQJdTTOQNxQYV2FRmtplgEuvb_RHk6paj-ZjeYc1lCp-x681s0TAC8pFLwexjINa4S4JEY3-k7pNUnXvnGyx7AtEemJfHyi3FJNUHWCHGn3DE1auxV4dDu1C6gNORqaoc64Oc6FSr6qbYlOPgC-jhsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سخنگوی دولت: از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی‌کنم
🔹
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/684453" target="_blank">📅 13:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684452">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eded00e64f.mp4?token=ASTpQ6B6WBRrhgwbSrzQ-cUMv4AaXKMI5o4zGTrr_FsblGeePv_IRE0Lb9kyTXRJvdRWXui55_FE1pG-cnOCwRzn1EdViGq1irAfaBi4LWWUupJxXtdxNbDWYN7oc0nkdWTii4ypuGSHLnueqq4-YUB_MlTFz5hK7i-filINH_h4UN6scYSp5YeDAEFNyATIp7vrICsvwZ1G7qdKubFb2fo8wYwxz0P1RzielsmG1HDMXhK6gZ9bto9uAX0SlZNJE5uCA1smfmL0zzRMDPgDLGMCF04o46i3PDHipnBAXqIkbnlE4KoE7huegVuCvQED_3sVVll0Pf7KVyubDHcZAIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eded00e64f.mp4?token=ASTpQ6B6WBRrhgwbSrzQ-cUMv4AaXKMI5o4zGTrr_FsblGeePv_IRE0Lb9kyTXRJvdRWXui55_FE1pG-cnOCwRzn1EdViGq1irAfaBi4LWWUupJxXtdxNbDWYN7oc0nkdWTii4ypuGSHLnueqq4-YUB_MlTFz5hK7i-filINH_h4UN6scYSp5YeDAEFNyATIp7vrICsvwZ1G7qdKubFb2fo8wYwxz0P1RzielsmG1HDMXhK6gZ9bto9uAX0SlZNJE5uCA1smfmL0zzRMDPgDLGMCF04o46i3PDHipnBAXqIkbnlE4KoE7huegVuCvQED_3sVVll0Pf7KVyubDHcZAIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خرد کردن حرفه‌ای پیاز در چند ثانیه
🧅
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/684452" target="_blank">📅 13:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684451">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_PZ4D1jBWXzO6y62WU-uPrukEZQdvxm2vs76WBJ6kXjkxwqUchGiU30FEfbc6J-iW5eMbtkLcrQgQVf79_0QpRDiqwqf8U30hYR9dg6xUfcdxc-pzZFfocGI6_A7OCRHOp7NGwTvpHvgd6Pg8eOj3hwNu_6mmXxvG76RWzQyi8_1xRKgpzukgatY6JFglQ6i-f0dytd3ZvMETe_1e-urfGEeTXt_VaRH9bOk4fuqZXtTPJHN2SgqOdj7JZuAzq7jgT2Ziai2dAmzDhvcoN6ZfYOWGey1MFGH_b2-jmWDY-gHBTMRrXeByx_ZCQJLaWDa_BQhg4kQU7ylOYRgAxBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وزیر صمت: فولاد خوزستان یکی از قطب های اقتصادی کشور است/ سرعت بازسازی در این شرکت قابل تحسین بود
🔹
سیدمحمد اتابک روز دوشنبه در حاشیه بازدید از خطوط تولید و روند بازسازی خط تولید فولاد خوزستان پس از حمله دشمن آمریکایی-صهیونی، با گرامیداشت یاد و خاطره شهدای…</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/684451" target="_blank">📅 13:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684450">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzrClpJ05Dps-0E4ux9sd2efNFDOfdwdxrds-Y39iiy3qkgNCN1gZ88Ljve4-Tmu6BLSQFOYl8qbPknKH2MTAscdHVnTQ9wRP4YXNI3Vq7C9oSTbRLOIspvYCCDBX1yJJw1o3GthzvaVwGGODSMbuTSOxhugW1zIK1KrTpoW100sqRiroKrzjzm7EGYxy6S4Y9Q1Awev-9gZ42zdxaZsnL9wQLx4_H8Y5rIMBvlRnY4aqv_ef4HtFODSPnD0EZJwd7ZX-JEh91UtqycuLvlaWfogzJdEQ_BRU0PjHMOANgLv4s5fXU-rD0ZA1EDT6HMM_z35ohhM2Ew0oQnf1vZWtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
هادی چوپان، پس از غیرفعال شدن ویزای طلایی امارات و از دست دادن مصاحبه سفارت آمریکا، از حضور در مستر المپیا ۲۰۲۶ انصراف داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/684450" target="_blank">📅 13:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684449">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a24138b85.mp4?token=g5qCHe0UjMaA8Ng8gHY90v83xBfjCzMc5bB6oQMUVzmJyhPDreIRnq80tPshsRiVkrl9UR4hAvlypsqbFI3y_s-rPE30vXrY09t9yiMOWfgh8EZ2u3ry-7OdRcQuyWbFzlPSKAnIareG-tMnlu8ZL_00eJl2PK3e5AzsRyU1ubym8kMXsTCZfgFIctvLB4NQGi0U1kFnbR2m125Q6IhNJqXNXSUQIZZO9PiMu_XggxkkQK543iAxh9DCXkdl2anvMUMoWWu1yRYj_VxrxHnt_BZOOozyC2oXhhqYFtAluXR7quA5gRqaNgG6Bvj1pAJ3AhbRV3Z1RgbJn3EX3KlMAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a24138b85.mp4?token=g5qCHe0UjMaA8Ng8gHY90v83xBfjCzMc5bB6oQMUVzmJyhPDreIRnq80tPshsRiVkrl9UR4hAvlypsqbFI3y_s-rPE30vXrY09t9yiMOWfgh8EZ2u3ry-7OdRcQuyWbFzlPSKAnIareG-tMnlu8ZL_00eJl2PK3e5AzsRyU1ubym8kMXsTCZfgFIctvLB4NQGi0U1kFnbR2m125Q6IhNJqXNXSUQIZZO9PiMu_XggxkkQK543iAxh9DCXkdl2anvMUMoWWu1yRYj_VxrxHnt_BZOOozyC2oXhhqYFtAluXR7quA5gRqaNgG6Bvj1pAJ3AhbRV3Z1RgbJn3EX3KlMAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس قوه‌قضائیه:‌ نگوییم نمی‌شود؛ بگوییم می‌شود
🔹
اگر مردم فقط حرف و لفظ از ما بشنوند خوب نیست؛ باید کارهایی که مشکل است و نمی‌شود را انجام داد تا مردم متوجه بشوند ما همت داریم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/akhbarefori/684449" target="_blank">📅 13:19 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684447">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a0d51ad3.mp4?token=DeJAxkyal-QZdaL7yHeadE8nAH6n6kjluN5F6YJ3vttUsMqa4mWSoD5xEVqaJswMKcsq1CxgA4OTK9GiS6WnqlZ8a_hM0VpHGy70-Zdw4R4ucp1WFoVQbhV7-ph5zk6Un6jPMATOROWI7pBMvMeKmZ3gjnXrafcig_Y9DTMJ6ju063p9lxOc2wloQS4nCoq73iYf4vNzZ1v_qrphbK7aO2QcbDDcUsHBYV7KXBIy1i67-wC81kVDOW6xcmf7tJ3HZKIwaNOcP1bFyBNO6TcU1amDCx2ciybkgseYZY7ZJ4mK6DoNpc7x1dO6oNftNvid72BvHJMugw7cBJJtrTAmuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a0d51ad3.mp4?token=DeJAxkyal-QZdaL7yHeadE8nAH6n6kjluN5F6YJ3vttUsMqa4mWSoD5xEVqaJswMKcsq1CxgA4OTK9GiS6WnqlZ8a_hM0VpHGy70-Zdw4R4ucp1WFoVQbhV7-ph5zk6Un6jPMATOROWI7pBMvMeKmZ3gjnXrafcig_Y9DTMJ6ju063p9lxOc2wloQS4nCoq73iYf4vNzZ1v_qrphbK7aO2QcbDDcUsHBYV7KXBIy1i67-wC81kVDOW6xcmf7tJ3HZKIwaNOcP1bFyBNO6TcU1amDCx2ciybkgseYZY7ZJ4mK6DoNpc7x1dO6oNftNvid72BvHJMugw7cBJJtrTAmuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
میدان مغناطیسی MRI؛ ده‌ها هزار برابر قوی‌تر از زمین
🔹
میدان مغناطیسی دستگاه MRI می‌تواند حدود ۶۰ هزار برابر میدان مغناطیسی زمین باشد؛ قدرتی چشمگیر که حاصل پیشرفت علم و فناوری پزشکی است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/akhbarefori/684447" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzaXVKmtq__5JuSgXv19wn7Nf6NplMewJPtjB6LnEm5KnrCtg3vXwIjThAN0LsyiuYlP22pXI_tG0qoEAxqK23gHUed65AdiCzfdJyRp47JAqeX9DLO9GJp5mY1goXTXPhVq_dv6ine8FwOTJXIHZgXWMj9piH0-g129ma26YD6c28cKbE9d1AJLWZ49CMWtXuP4s7X3RWHOkiQElBUdcH1jkdVf_HspMSCV9rnmHyFYJtzzdEl3WKpolRAM8LEOTzmTBT7NU1mq_JWuq9KpJEcRB7cpZkQfxImx317LIvkay4iZ3Y1JK-A-6SJuMlojeTN7uAvbwRu-bqP6nobuHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۴ شهریور ۱۴۰۵؛ ساعت ۱۲:۴۵
🔹
دلار آزاد امروز با افت حدود هزار تومان، از مرز ۲۰۰ هزار تومان عقب نشست.
🔹
هم‌زمان، هر گرم طلای ۱۸ عیار در بازار تهران کمتر از ۲۱ میلیون و ۴۰۰ هزار تومان معامله شد و سکه بهار آزادی نیز حوالی ۲۰۶ میلیون تومان قرار گرفت./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/akhbarefori/684445" target="_blank">📅 12:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-684444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZz_6HOrgMltLLILfD2CWf4x2lZck8KDeXaUP2FsGEGZJE_opDWzIVwb-khtsjUmE1NOeTvi0dYl3JpP0jPcq4wjOG3SiG-856rWVpRsmgoyZuKnMxMkvLGneCWA6bwGNqcTNOJsY4dj9jwkSb8GPg9utNJdyXepuWZ1-_tKsERAwq8GEEDz7oybqpdxbdGAc4wuOlSkPy7D0AhMtKg38WhoxJL4H8_sJuO1uY4-nGDuS9xvv_pP1n7cq7OsxhMqk2XAU5Nk2rpZcmX4fvetCnqDpirP8sCkf1EQvmsJAqnGkvtMVcgmzydZgi_QWF-o9_yl1Fl3E9ZVyZo5w3HTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رشد بیش از ۱۶۲ هزار واحدی شاخص کل بورس
🔹
در جریان معاملات امروز شاخص کل بورس با رشد ۱۶۲ هزار و ۶۹۷ واحدی در سطح ۶ میلیون و ۳۸۶ هزار واحدی قرار گرفت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/akhbarefori/684444" target="_blank">📅 12:52 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
