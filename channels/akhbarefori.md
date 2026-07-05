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
<img src="https://cdn4.telesco.pe/file/gmu0VEvnl7kkk6B3DNeqq3ZS-pldL5X1bIP7IpaMYvIuGHesme0UIMMNKxWBvnHo0VS_gDXoNGZt8PuR7wIdo-zNGnb8FBqQH-tOmqyeXzKkVHZgImNnHMbMGdvrVDMf2MS15TLYCDYfhQdY-ZFnqjZbwE71FJMg3hk0Grg_sTIIOl2uqOXHSAIA-1ai4yg2QiuC9u_hqnvIFb9i_u_2P13ju8RMktUp3Arg2N1dGg9uQUgMjYH_lkvHRLOGU5AEZcXLrg4D7K-xaijVA5his3rrIR_UwXB5lAW0oV9aRhhH6iZk4XQiHnfJw91B0kGgOAe0wpKJYTlNa0bJlclluA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.28M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 14:06:16</div>
<hr>

<div class="tg-post" id="msg-666934">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lhoz0DhIyQznLsXsgDG0lpNwu3rol_sWihHMGckbeslAoad8VIrDns0ZOTWa-XqTrmtU5suDVm-VIQPfXJECAoqXJX2zwbKxNbYi27Uw_qp1CO0PwBDiv1SFDGtKQM_zd7xNwlekYqlgHwYaikCu6wXh-wyMH8RvwEbA2i5nhTawYdn4-slcTGQ16_8wOk_A3dA1wZ4n6pCRMgcqGK1zDbiCjYQRrVFbhJHhLqujn0lxuUx3sljVXelI-jg2L6yNCcqdQNyFbAZFW-h3ITl3-8J5fXW2fijNrSDAqJkTAeQdwn03cZaavDCbONnxeCgu-p8UJBe4cqMPdC0yG6tQIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از قالیباف در کنار فرزند رهبر شهید انقلاب در مصلی تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3 · <a href="https://t.me/akhbarefori/666934" target="_blank">📅 14:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666933">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93f252fd36.mp4?token=BafxhV6QrpkKs1X5eUk6FLukp6vuV8eVVFOb-QqsWhrkblq74NQ7hIzNnZZCzditiyIXaHSzGYDkosxaRL-f_LarRsMDhE4FIWmZqrQwP3xeQyEpmDHd1vl5TQmMDne-tQnQdO-pIc_VyMpBfmEd-voW3SQTX8FgtRuWxUZkQp629UrXHkqQM4c9QsgwhbYZffr_9C-X_ZE2iSKvnRrXJvfmTKdalzKJi5c_1FSkcMOh2PI9cTW-XMRj_qreWRZuB1vv1d1V9WX-fmLI6jIFBa9fv5E8HJXdQFoxEA_9jD8W1hLf1jogCMwpMavPXCMd4OL9nBsXPK6MPMChft_aHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93f252fd36.mp4?token=BafxhV6QrpkKs1X5eUk6FLukp6vuV8eVVFOb-QqsWhrkblq74NQ7hIzNnZZCzditiyIXaHSzGYDkosxaRL-f_LarRsMDhE4FIWmZqrQwP3xeQyEpmDHd1vl5TQmMDne-tQnQdO-pIc_VyMpBfmEd-voW3SQTX8FgtRuWxUZkQp629UrXHkqQM4c9QsgwhbYZffr_9C-X_ZE2iSKvnRrXJvfmTKdalzKJi5c_1FSkcMOh2PI9cTW-XMRj_qreWRZuB1vv1d1V9WX-fmLI6jIFBa9fv5E8HJXdQFoxEA_9jD8W1hLf1jogCMwpMavPXCMd4OL9nBsXPK6MPMChft_aHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محسنی اژه‌ای: رهبر شهید ما بعد از این همه زحمت و رنجی که در راه هدایت مردم و انقلاب کشیدند نباید اجری به جز شهادت نصیبشان می‌شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8 · <a href="https://t.me/akhbarefori/666933" target="_blank">📅 14:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666932">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وهشتم از فصل چهارم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای محسن حسن‌وند که شکارچی قهار بودند و به هیچگونه حیوانی رحم نمی‌کردند در سانحه تصادف به کما رفته و حقایقی برای ایشان در عالم برزخ پدیدار می‌شود و تنها از میان ۴ نفر در حادثه، جان سالم به در می‌برد و به زندگی باز می‌گردد و تغییرات محسوسی در زندگی و رفتار خود ایجاد می‌کند را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: محسن حسن‌وند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/666932" target="_blank">📅 14:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666931">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUqJQ7Ncs1H0YtBK1xvFo0npJ1wcGDL3CNLil9hXOj_T1f0Lk2TlGqXEptFTYf0DXvnJkkVu3w2EshWO8cdxFD8QI6JFAA8CgkWCNvCbm3xh92sFy7RaeRQkX7OMFEs2W4l591RE6JYkoS_52NufZ6TBQBupXi3AxoQe4U26LG6YUzl17N4hlU_al9CwLg7Xm4ARWRaxmNr1rDhELfa2vHiv2JdqRi8arvmCsL7OrhaMYQR-7vD-XKLJLHfJrSJji2USpdVKfS2BrA8FuM33dzbLO6PDIh5ox2uh_qBlUi0Vk8yuZvdHcgQ2g5vHItD1fCFDDi40vb51Ub3oD8gr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویری از شهید دکتر مصباح‌الهدی باقری در کنار رهبر شهید انقلاب اسلامی در حرم مطهر رضوی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/akhbarefori/666931" target="_blank">📅 14:02 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666930">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dXCbwV_GF-bIjDIGJIKeFP9HGlKGGJaoiBBF-M6Uu-C7L1gXIjibpptU3wPV9O5qyQYWIayUPrtqTA_6TjytLq5eaTS1bCAmzDi8keZWyLbruVCf0ZNACtEzpmVVKR_Vgu2eQ1lUKJZoGYPBtQycs_Gv6rYnJTQsv6e1yaKNOXv8VWYKUIKgtOLH1iw6k9txGyP9U8UvV4jUiHTaNDM4FchzaFaN2gaVxeiyjYnrYrQTEbERQAB2Lmp2vq2kIfHq7J5HANqPsj218_-qX8-Ezr2_EfBDoBCfx4YvK4NjwtuZU-LFDqlMWl8BDLQ4wLilEiPjagVQtqWk8eWej4BNdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
منطقه بندی مشهدالرضا در میزبانی از زائران و خونخواهان آقای شهید ایران
منطقه ۱      فارس  و اصفهان
منطقه ۲     تهران ،قم وخراسان شمالی
منطقه ۳    لرستان ،کردستان وچهارمحال بختیاری
منطقه ۴     کرمان ویزد
منطقه ۵    هرمزگان وبوشهر
منطقه ۶     خراسان جنوبی وسیستان بلوچستان
منطقه ۷   کرمانشاه ،ایلام وخوزستان
منطقه ۸    زنجان وهمدان
منطقه ۹     آذربایجان غربی وآذربایجان شرقی
منطقه ۱۰    اردبیل وقزوین
منطقه۱۱      گلستان وسمنان
منطقه ۱۲   گیلان ومازندران
شماره تماس راهنما: 5151-051
لینک ثبت نام:
bayadbarkhast.ir
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/666930" target="_blank">📅 13:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666929">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6405b893a6.mp4?token=JMR_c0FEo-z7HF6zwDpng4BMsXVLHbfJ-_8ouyS-cvsZ-Fq1_FMQv-PLEHWz45Yd5LCvDAT7MB1uq14Yf_A2bzPSOg_5m7e4HNUot4OOinBDW3Me-GqImhl7hpozughq1ONHbA8bYoVpSQh4L5L1VRFBuaKk3l9o651rikxsjKHhGLPENWtjnrYVr9QBuHT9nuLMi4UydUQptC5y5k7kDk1bO54bTmgjWtWPrABqypRCI_WyetgMPXKGhfzXR6a-GZmhc8EBO1CD1TCKXuOvLLZrl-lM0prQ3htRs-HVafL_AP-QbKtT5d6R9miumZqm4LO1iOzgdzPwRc7ksFqGfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6405b893a6.mp4?token=JMR_c0FEo-z7HF6zwDpng4BMsXVLHbfJ-_8ouyS-cvsZ-Fq1_FMQv-PLEHWz45Yd5LCvDAT7MB1uq14Yf_A2bzPSOg_5m7e4HNUot4OOinBDW3Me-GqImhl7hpozughq1ONHbA8bYoVpSQh4L5L1VRFBuaKk3l9o651rikxsjKHhGLPENWtjnrYVr9QBuHT9nuLMi4UydUQptC5y5k7kDk1bO54bTmgjWtWPrABqypRCI_WyetgMPXKGhfzXR6a-GZmhc8EBO1CD1TCKXuOvLLZrl-lM0prQ3htRs-HVafL_AP-QbKtT5d6R9miumZqm4LO1iOzgdzPwRc7ksFqGfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: قول می‌دهم راه امام شهید را ادامه دهم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/akhbarefori/666929" target="_blank">📅 13:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666928">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXIw129mXjT8PuQG__NOxP9v5S0AmsclnP65JLKkmIaSxXtviE88dXH5_1Pb_cGfdZrNYgIFWY-O90rtVRuuE8X2edrApbFei6ymBs0qfGOEwPbZ4_wFMuz6pKbm4c3MBR2WC0JNPUggbO4lCtrWRAXsh3W50M2mDCZb2WqbO52uV_mTxJanXewIaeIEykujCVrr_-3QscrtI2U3Bid9DiI5g85zKTuQ9ONsshp1LctPUZuqw58rjKdx0arR74zXzRZTkLs05Fy0Z6bUkr3xb6hwPSQWMbldicu4Nk6Ixpseqk6qLkXZUuQqXneZRepl1Xs4N1HYs4g4LIL8xEIawQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قالیباف: ملت شکست‌ناپذیر ایران امروز یکپارچه فریاد یا لَثاراتِ‌الحسین(ع) سر داد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/akhbarefori/666928" target="_blank">📅 13:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666927">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
شتاب تورم ماهانه کاهش یافت
🔹
با انتشار آمارهای جدید، تصویر تورم در پایان بهار شفاف‌تر شد. هرچند شتاب تورم ماهانه نسبت به اردیبهشت اندکی کاهش یافته، اما روند افزایش قیمت‌ها همچنان نگران‌کننده است.
🔹
تورم ماهانه خرداد به ۵.۹ درصد رسید و تورم نقطه‌به‌نقطه نیز با ثبت ۸۸.۶ درصد عدد جدیدی را ثبت کرد./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/akhbarefori/666927" target="_blank">📅 13:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666926">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fcb3d9b321.mp4?token=SUR_WVBCc6G9ulQzer59D4j5BX_io3DWxjUYqpBykdq7qz75RzXWpQsz8QYJOzxdHp3Y4pCRCdkf0ooK7TrzG3350SyrXSC6M3_2M-G8kMlbSIU9MPN75PrGFNPyDDdkkobPESJx8FErbZWuDxu3c2cS5CInnAhYRK_2dQ1Q2RVKmlCgH4WCihiIVQPZ8zIWskiXp3BPya4Xtl4y3BJMhSOMN1pkUaUzDUike4OqVvTniKLFQr9DEiv8ZeZW8aKLQls7Na3itYB18ixBUdKdZJGjHCuLk_TQ2Ro6SdWborrHb_fVTWQe9Jla2jw18JxOU5SXV4Y7DevNM4L3rBxTxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fcb3d9b321.mp4?token=SUR_WVBCc6G9ulQzer59D4j5BX_io3DWxjUYqpBykdq7qz75RzXWpQsz8QYJOzxdHp3Y4pCRCdkf0ooK7TrzG3350SyrXSC6M3_2M-G8kMlbSIU9MPN75PrGFNPyDDdkkobPESJx8FErbZWuDxu3c2cS5CInnAhYRK_2dQ1Q2RVKmlCgH4WCihiIVQPZ8zIWskiXp3BPya4Xtl4y3BJMhSOMN1pkUaUzDUike4OqVvTniKLFQr9DEiv8ZeZW8aKLQls7Na3itYB18ixBUdKdZJGjHCuLk_TQ2Ro6SdWborrHb_fVTWQe9Jla2jw18JxOU5SXV4Y7DevNM4L3rBxTxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آزمایش موشک بالستیک ضد کشتی از سوی ترکیه
🔹
تایفون، اولین موشک بالستیک کوتاه برد ترکیه است که پیش از این در آزمایش‌های خود با اهداف زمینی را در بردهای بیش از ۵۰۰ کیلومتر هدف قرار داده بود. این موشک با سر جستجوگر نسل جدید یکپارچه، فناوری‌ سوخت جامد و انواع برد افزایش یافته (بلاک ۱، بلوک ۲، بلوک ۳، بلوک ۴) است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/666926" target="_blank">📅 13:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666925">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسِدخارجی</strong></div>
<div class="tg-text">سلام به همگی؛
خیلی از ما این روزها و روزهای آینده، بخشی از یک واقعه بزرگ تاریخی خواهیم بود.  قاب‌ها، تکاپوها، بغض‌ها و تصاویری که هر کدام از شما با چشم خودتان می‌بینید یا با تلفن‌های همراه‌تان ثبت می‌کنید، تکه‌هایی از یک حقیقت بزرگ هستند که نباید گم شوند.
🖤
«
به همین خاطر، برای ساخت یک مستند بزرگ و مردمی، به همکاری شما نیاز دارم.
»
از هر قشر، با هر نگاه و از هر کجای دنیا که هستید، می‌خواهم داستان و روایت خودتان را برای من بفرستید تا در کنار هم این تاریخ را ثبت کنیم. اگر خادم هستید، اگر میزبان، میهمان، مسافر و زائر هستید یا حتی اگر از نیروهای تامین امنیت مراسمید...  هدف من ثبت یک سند ماندگار، واقعی و کاملاً بر پایه تاریخ است؛ نه صرفاً یک کلیپ.
📸
چه تصاویری برای من بفرستید؟ هرچیزی که فکر میکنید!
🔻
اگر خواستید جلوی دوربین بیایید، اگر خواستید حرف بزنید، داستانتان را بگویید و از حس‌وحالتان در این روزها صحبت کنید.
🔻
فضای اطراف خودتان را نشان دهید؛ شلوغی‌ها، موکب‌ها و حضور اقشار مختلف (نوجوان و افراد مسن، پاکبانان عزیز، نیروهای هلال‌احمر، آتش‌نشان‌ها، پلیس، سربازها، زائران و مسافرانی که از راه‌های دور آمده‌اند). حتی اگر دوست داشتید باهاشون مصاحبه بگیرید.
🔻
تلاش و زحمات دیگران، دلداری دادن‌های مردم به یکدیگر و هر صحنه متفاوتی که توجه‌تان را جلب کرده است.
🔻
اگر به هر دلیلی امکان حضور در مراسم را ندارید، از حس‌وحال خودتان در همان جایی که هستید ویدیو بگیرید و برایم روایت کنید.
🔻
حتی اگر فیلمی رو از روزهای گذشته و برنامه‌های مرتبط قبلی هم در گوشی یا دوربینتان دارید، بفرستید. مثل راه اندازی موکبتون، خاطراتتون در مسیر رسیدن به مراسم‌های وداع و تشییع (تهران، قم، عراق و مشهد) و...
🔻
گاهی پشت‌صحنه‌ها و حاشیه‌ها از اصل جذاب‌تر می‌شوند.
✨
نکات فنی مهم (که خواهش می‌کنم حتماً رعایت کنید):
برای اینکه ویدیوهای شما قابلیت استفاده در مستند را داشته باشند، خواهش می‌کنم به این چند شرط دقت کنید:
🔻
حتماً افقی فیلم‌برداری کنید (گوشی را به پهلو بچرخانید).
🔻
فقط ویديو بفرستید. عکس، صوت و متن لازم نیست.
🔻
ویدیوها باید کاملاً خام باشند؛ لطفاً هیچ‌گونه موسیقی، افکت یا واترمرکی روی فیلم‌ها نگذارید. من فیلم‌ها را با صدای محیطیِ خودشان نیاز دارم.
🔻
فیلم‌ها را با بالاترین کیفیتی که دستگاهتان ضبط می‌کند ارسال کنید.
🔻
در ابتدا یا انتهای ویدیو، یا در متن ارسالی، ترجیحاً ساعت، تاریخ و مکان ضبط ویدیو را بگویید.
🔻
لطفاً ویدیوهایی که در کانال‌های خبری و فضای مجازی پخش شده و خودتون اونا رو ضبط نکردید رو برام نفرستید؛ من دنبال روایت شخصی و قاب‌های اختصاصیِ خودِ شما هستم.
✨
نکات تکمیلی:
🔻
برای من سوژه، نگاه و داستان واقعی شما بسیار ارزشمندتر از حرفه‌ای بودن تجهیزات است.
🔻
با هر دوربین یا موبایلی که دست‌تان است، قاب‌هایتان را ثبت کنید و برایم بفرستید.
🔻
برای به سرانجام رسیدن این پروژه، همت همه‌ی ما لازمه. خواهش می‌کنم خودتون پای کار بیایید، روایت‌هاتون رو بفرستید و حتماً دیگران رو هم از این فراخوان باخبر کنید تا این قاب تاریخی کامل‌تر بشه.
🔻
لازم به ذکره که ارسال فیلم‌ها به راه‌های ارتباطی زیر، به من اجازه میده از این ویدیوها در ساخت مستند استفاده کنم و به معنی اعلام رضایت شما برای انتشار این قاب‌های ماندگاره.
✉️
راه‌های ارسال ویدئوها:
لطفاً فایل‌های خودتان را فقط و فقط از طریق مسیرهای زیر برای من ارسال کنید و همچنین در کنار ارسال ویدئوها، مشخصات خودتون (اسم و شماره تماس) رو هم برایم بفرستید.
سایت برای آپلود:
https://upload.sedkhareji.ir
ایمیل:
Contact@sedkhareji.ir
تلگرام:
T.ME/SEDKHAREJIPM
اگر باز موردی یا سوالی بود بهم در
@SEDKHAREJIPM
پیام بدید
خاکم؛ سدخارجی
✔️</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/akhbarefori/666925" target="_blank">📅 13:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666923">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNXe4zE0O2qrD_DiKPRmPR6kiNSwzWAeqybVN7XPTdHQ0MGoXOUwXGaUwfgpmLY3apuyh1xmXbOJZbV_g0f_SD74zxJH3x7G42ZFQWVly16bFdvmin80ZPwFhujbOTExGHH1LU5kyWXjuH9CJjy1sntxgTffWbm6yT2mEaIES9u_IzK8T3u9rrrV5ahGPrvF0kRKnTzH5oFv-Dh-8FIbL6LQz6lxcaCaezva1gi6RfFcz1I_Kzf7Y7s3ODmVPmxBFa3-Izq0n5Utc9oFjUAtcuABltK6BJTKDIhh30RncLwl3cOgle9TMEwLri75fpu_DIoZ8myhwFOdYzjuw9dDZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/666923" target="_blank">📅 13:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666922">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkNqVPFy9gBKAEPsNWFq9Lb4qYT-1BE1HkcxCeqJkCs0n1Cir5RjMwCtjJEHUaLmJwoVzPZgeNntCYP9fF9EF7zhXo-wHnNYMQeTE9bllnfVE5LZbbmPviNw_dhO7zVg5e6Yj-G-sK0lL4c5zvVCdJ0xBwRCQ7B3qAwHlzU1FF0TklXInpjN5R7bJBFxv6JaTFQu3qXfG_WcZtc8jb9p_bCxIGkkqf1vncyTJZK9mYWjigLVC7Qgg8xHWdvTihyYYSd-Rp_PQkUXnQxo9IqjTm8lRaq3GgoueGxNQaSIriA2IY3RZDJBGnTy_AmJQ_Be176GZ8_7FHkM4QuXhz6xKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ذوالقدر؛ دبیر شورای عالی امنیت ملی خطاب به دشمنان ایران:
این چند روز چشم‌تان را به ایران بدوزید
این همان ایرانی است که خیال می‌کردید چند روزه می‌توانید آن‌ را از پا درآورید!
این دریای خروشان جمعیت، حالا در وداع و تشییع رهبرشان دو شعار را فریاد می‌زنند:
مقاومت در برابر دشمنان و انتقام خون رهبر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/666922" target="_blank">📅 13:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666921">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
قول رئیس‌جمهور عراق به ایران؛ نمی‌گذاریم گروه‌های مخالف ایران در عراق باشند
🔹
رئیس‌جمهور عراق، روز شنبه اعلام کرد که بغداد در حال اجرای توافقنامه امنیتی خود با ایران برای پایان دادن به حضور گروه‌های مخالف ایرانی در خاک عراق است.
🔹
نزار آمیدی در مصاحبه‌ای با شبکه الحدث گفت که عراق روابط خود با تهران را بر پایه احترام متقابل، منافع مشترک و احترام به حاکمیت ملی بنا خواهد کرد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666921" target="_blank">📅 13:42 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666920">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
جمعیت خیره‌کننده در مراسم نماز بر پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/666920" target="_blank">📅 13:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666919">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAl-wGQNmx2uiarrtDs-KUnhipGWqirNOgsphhAOgkpX7RH4jDI45KXp5zV5L6-17hCswIbY-sOfBMkWDwoiizDMaAU6E85Zcqye4qRCtIj1hN2gAZaSoLMHYjfh7vYvkPtsZRdPP9DrLsvR1j4Mvkel7DPZOsXd5GXc75xjDFk_mypwleO4xyF5xrXPR7wQJMkuL2cCwSwVBWZySkoTRVoTqEGttu5TiuLchcwcueZ0uL_eYwrz7wDqdA1NzLY_Z8SFiex-ky-aQRbeQht_sSBf5cYU6lmcQI3E2g_qXXC8agJyfsuCdPdmB81nbZSPQOZ_IXOKPlJ5UqImawJi3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویندوارد: قایق‌های سپاه ۶ کشتی را از مسیر عمانی خارج کردند
🔹
داده‌های هوش مصنوعی شرکت دریایی ویندوارد نشان می‌دهد که از دیروز ۲ کشتی از مسیر موسوم به «کریدور عمانی» به سمت مسیر ایران تغییر مسیر داده‌اند و ۴ کشتی هم به خلیج‌فارس برگشتند.
🔹
دیروز بلومبرگ نوشته بود ۸ کشتی قصد داشتند از مسیر تحت حمایت آمریکا عبور کنند که به ناگهان تغییر مسیر دادند و تعدادی از مسیر ایران برای تردد استفاده کردند؛ خبری که تصاویر ماهواره‌ای هم آن را تایید کرد.
🔹
حالا ویندارد می‌گوید این تغییر مسیرها با حضور قایق‌های گشتی سپاه تلاقی زمانی دارد و نیروی دریایی سپاه به کشتی‌هایی که از مسیری غیر از مسیر امن ایران استفاده کنند، هشدار رادیویی می‌دهند./ فارس
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666919" target="_blank">📅 13:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666918">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
یورگن کلوپ سرمربی تیم ملی آلمان شد
🔹
رسانه اسرائیلی: ترامپ احتمالاً دیدار سه جانبه‌ای با نتانیاهو و عون برگزار می‌کند.
🔹
المیادین: مردم یمن امروز با تجمع در مقابل فرودگاه صنعاء، از اقدامات ایران برای شکست محاصره تقدیر کردند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/666918" target="_blank">📅 13:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666917">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4a7bcf2c1.mp4?token=MVIHshbvSYn6UzKADmaOE3gTUcDY8OEfV3fhjhrdeO9xwyjHWJarv6Aj6fiVq4GYPLabULYPJS3KYlqck9dSgLBFQg2DPKkm8JqH5oCQ7N4_dgBjCXRQuUUEuonmdbQp7iibfQp0_C-DxfRcd4hTETDPFqnkvw58b881L5-PbWe_0b4FcHA2750YoAoZKhsoYRXgE0dl3cPjq_fqgH-MvczZz0a7Sib9DqgzHF3WJqHzJj-Ea4MulzsMyLTw8FkZC4ifpzdMFC0Grod5IZ3AuQQM_PUEhI44mnrB9f7oGk9tgV9u2Bzx_hV1eiN81D_kKyo6KG5YnkMrxiwa7AOwNoFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4a7bcf2c1.mp4?token=MVIHshbvSYn6UzKADmaOE3gTUcDY8OEfV3fhjhrdeO9xwyjHWJarv6Aj6fiVq4GYPLabULYPJS3KYlqck9dSgLBFQg2DPKkm8JqH5oCQ7N4_dgBjCXRQuUUEuonmdbQp7iibfQp0_C-DxfRcd4hTETDPFqnkvw58b881L5-PbWe_0b4FcHA2750YoAoZKhsoYRXgE0dl3cPjq_fqgH-MvczZz0a7Sib9DqgzHF3WJqHzJj-Ea4MulzsMyLTw8FkZC4ifpzdMFC0Grod5IZ3AuQQM_PUEhI44mnrB9f7oGk9tgV9u2Bzx_hV1eiN81D_kKyo6KG5YnkMrxiwa7AOwNoFIefXhdC5LmGL0wQCEVdBTP0gR0FmY0gf51EaBbGnsTwd34342RH2pEgxLiffz5mrerIdy5KakD7-JGyDNuo7c1H3E3xrbZcDnG0t-65smm4pobvj3W0xDVIY3wYHRF9WTMFqgS7uiNSpy8xEzivQYkVT4vhaXKOWzmlKy8286Tyv_Zj4raRmucR0rFDem5xJlxzAeMOuJX5EN9NLvZNVjU_ZXzNKpBXVEF6d9Ju_Bhfhwh__yXpBCD0ruHhR735ISbR9Y-XBeCPV_9Wlde9h2v_BGjO063YsgUygnOsb_HVaZqkJIuGn5K-6c0YyKO6HivI09EeapBylKX91Ux_U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حرکت خودجوش و خارق‌العاده مردم هنگام پخش سرود ملی/ احترام نظامی به سمت مصلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666917" target="_blank">📅 13:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666916">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_sIhBR6RIqgK4zhRj9y9XXpRJxSl-Ueiaq6dToNOL0v7AtayymLakZbxo1NkRpxkBGQypIFIt1i-G3CsaeXLmLps7pIG9rjwvtybDl7GWb80NObeN78JglnbjXDuHj8R_fVrnwsvQ4Vuj-d09_81uXvUULzGknOivDBc2ky4-2T5xNX-eYRM6BnglRH6Pb8i9xzXb2EyOyv5W52_7S9Bvj26ysVLAyK2_o2ObpCYQZlsiKN1XN0caQA_Bc-U2T5R5S0l2o9TmcrVL_w3oH1Vrp9mSPLRGGkjZS3yKMHG2ZEyUjrtyzu2AFueSY3rS4MD-X9QJoovqtGm5bz1KTFeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فعالان اقتصاد دیجیتال هم در مراسم تشییع رهبر شهید موکب‌دار هستند
جمعی از فعالان داوطلب اقتصاد دیجیتال، همزمان با مراسم بدرقه رهبر شهید ایران، با برپایی موکب در مسیر مراسم، آماده میزبانی از مردم و دیگر فعالان این حوزه هستند.
وعده دیدار:
میدان آزادی خیابان برادران رحمانی جنب شهرک شهید فکوری
موکب فدا
https://www.instagram.com/mokebfada?igsh=MWg5bTV1dG5nd2IyYw==</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/akhbarefori/666916" target="_blank">📅 13:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666915">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
تا انتقام خون رهبر شهیدمان را نگیریم آروم نمی‌گیریم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/666915" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666914">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
تلگرام از مرز یک میلیارد کاربر فعال ماهانه عبور کرد
🔹
پیام‌رسان تلگرام در تازه‌ترین آمار رسمی خود اعلام کرد شمار کاربران فعال ماهانه این پلتفرم از یک میلیارد نفر عبور کرده است. کاربران تلگرام به‌طور میانگین روزانه ۲۱ بار اپلیکیشن را باز می‌کنند و ۴۱ دقیقه در آن وقت می‌گذرانند.
🔹
تلگرام در سال ۲۰۲۴ به ۵۴۷ میلیون دلار سود رسیده و با کنار گذاشتن وی‌چت، اکنون پس از واتس‌اپ، دومین پیام‌رسان بزرگ جهان از نظر کاربران فعال است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666914" target="_blank">📅 13:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666911">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ufsLgIpy2b2SQ2gypItHjs1bGkdBs48Y_EpFqLszUTYuTDRKZ1oeYHk03OHRp04wGjF9xUyrcI_b4WBntSYutZuZTVrtJPoAEcEXXdS6vkVDvJVwxWvGLTpt_VxjLDmPysIcVWP5b95w7VEj-sifHiwZkjBFriJWTYq0dg9tismsuH_2IbobVzQ4V7yc4pdjBMncSM9Ny8N4BIUS0vmNEjG5oiNDBuUp4PRShzBNmEaKOSGBRlIfnevO3dr6fe-li5ofFAs1FvEiRbgS3xiboFXA3S00pk_SXWVF0qMcEcsh-b0K2zFxLNCyssudluSR6IQ_SnHcUwgI1VFUhYcMPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LgacVcrZalF3Zic5kWpQdYTizRleLB1KjPG_jrnNYMZZMtetMnhbO4XxSw41k4rClotGYmi6Qftc4qzR3WNLQUnkRdX91zfZUhDCIKkvEdEbfVx3oSSM0cxpGTy2JNXAdYm0lRMM0Rusl-ldtEpJsnNiudCzupRol7stELIhFo-RpYlmcC7IEtPr4gX34UAl2Kx6Q1UVlsmpvshKybEmTIWybdQIy0qnDYcdCWGw-4ftFzPT68YKXI9BgM_Jzv4-6WuafkZiLaFFfjzOMzVwcK2Oe_QwAIQlVeU5RD_py9QOjqXksZW_x9siPIKyY1Sle1XyVPFZqrSplgZZ_lXFEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0KfPWMLmMONmt-uxWdKK0Kxn04eKh8duu47R1BmommXadwVbDfEslkAA4YD6-x7jZ3TIXpETdG93BvzRXxDpFZK4xryXrqSKqYn81rx63C0MAQYMapyF5BwwB28OXys0eaA69GUj6eHZicNgk_F-Py25AvSai96x2u8zUr8X-p1sNpbOFI16p1ZQFioRR8DMpJ6ritoa0U7MXq0tDC5QMqmk2IqiSusUAMuEF0B19Uinvdd16r3-_1Shoq-vearN_X-rALsz3nBa8w6rveWmQN48qMms0NyXL1rHI9iLGslKGjVVDmV09Diu-VXf0SB9uHeFvJnaRrc-yDJSa_Tlg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
بازتاب وسیع وداع با رهبر شهید در رسانه‌های جهان
🔹
روزنامه «گاردین» با انتشار عکس و ویدئوهایی از مراسم وداع روز جمعه نوشت که پیش‌بینی‌ می‌شود مراسم ۶ روزۀ تشییع پیکر آیت‌الله علی خامنه‌ای میلیون‌ها نفر را در ایران گرد هم‌ آورد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666911" target="_blank">📅 13:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666910">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
راهشان تا همیشه ادامه دارد...
🔹
بانوی شرکت کننده در مراسم وداع با رهبر شهید انقلاب: آنچه برای خودشان نتوانستیم انجام دهیم، برای فرزندشان، آقا سید مجتبی، انجام دهیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/666910" target="_blank">📅 13:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666908">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d7d6cdcd1.mp4?token=UDcaWTSFk_Q9gVNTryKnI0Ycw_92mPYEeT0Mp330F-pwLh84xfSkWbT1H-oGQ6DvYf2YdQ6VfvvoZoonbCvoYh4eKZXAhAhU-8y84RGjXLiZQI_k0_4yYBeRLg_bEl4gvIl_fcgbBmb10Z0kSdOmaPtnO4-b-ySoRV_6yJpESrtD1NHrfFeI4tlOQoFQBhSE_N1Ssv6_QWo6XmzwJzDPhTvSuuIHKg6WUVx6Dkr5i-DeEIj5VCprhMDX3GCqKXsPNzc7ZSJKsSYEH2NNUjiwKdjyai2JUK4mscSyZhQkZHgrxVkso1WmZkQ99_NWdzWWPvU0k4kQkMiYIRYn7KZsxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d7d6cdcd1.mp4?token=UDcaWTSFk_Q9gVNTryKnI0Ycw_92mPYEeT0Mp330F-pwLh84xfSkWbT1H-oGQ6DvYf2YdQ6VfvvoZoonbCvoYh4eKZXAhAhU-8y84RGjXLiZQI_k0_4yYBeRLg_bEl4gvIl_fcgbBmb10Z0kSdOmaPtnO4-b-ySoRV_6yJpESrtD1NHrfFeI4tlOQoFQBhSE_N1Ssv6_QWo6XmzwJzDPhTvSuuIHKg6WUVx6Dkr5i-DeEIj5VCprhMDX3GCqKXsPNzc7ZSJKsSYEH2NNUjiwKdjyai2JUK4mscSyZhQkZHgrxVkso1WmZkQ99_NWdzWWPvU0k4kQkMiYIRYn7KZsxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وفاداری تا پای جان/ زائر رهبر شهید: تا آخرین قطره خونم مقتدا و خونخواه رهبر شهیدم هستم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/666908" target="_blank">📅 13:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666907">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Miu8Sg8ZiChuGLOKKi7UfP7bo-H5gUCBjpl388coMVpaFNvyyq6Vi6rbH4_SI4S8DSkfx3_4V6Fv898t0Q6RH5eFKPhb1DVeHGXPc7yz_lrNsdk3o8W4B8yP-F-j56HbBY4ZF1W-uN39KmWkoGd30XBHvjMFMLmpM3PzggIQwDTMwc9TcGmzGtZQ4MTev_ZDiWgVNkb6eTOepEJnq5SK3a_jnLcQ52AwNtgOiuDnmg77sjvBRQzyA0x8wkWske5Rh4TzSUj2XaaBw0BOcUIPZzWUngrJ_ghkvWHH0a5S00cVEi0Eut5fiK-CgItER3ncZUpwfTYfL94pRH9iaCix_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برت اریکسون، کارشناس آمریکایی: برنامه آمریکا برای سرنگونی حکومت ایران چقدر نتیجه برعکس داده است
🔹
محتمل‌ترین نتیجه این جنگ این است که حکومتی در ایران شکل بگیرد که از قبل قوی‌تر و با حمایت بیشتر باشد و نفوذ جهانی‌اش هم به‌طور چشمگیری افزایش پیدا کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/666907" target="_blank">📅 12:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666906">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFt_ms3kd7eUaGNH1eP1eFvY27q5Hk5PGSFFpJ6KyCsjW_uuRftCf0FaxHfWjhlmQXMvfHb_Pztq5lT01QN6TmcDyUFTQJW0vDKvQit-4CfhiLN12I4j0nk_2OlTUy0ehUoFOZWgrCnQyK1AQusPPgS2GLpBwFmHWKaqP40_hjyZsThrkPcasGUcy4tsKVMLyERtQuwIjJMWrGTpACHmJ4PCFiHILGIpknVfshklai0JmET1malIBhN1BV-o5jvMhesZEyltzea4cbU_hDiAnQh8RteMNV1z8wExZ_KYdoPHqyU39wvrRwZ0H7KF9GOJLijG3QVKYE4T__bAW5EpZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نمایی دیگر از حضور فرزندان رهبر شهید برای نماز بر پیکر قائد شهید امت #بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666906" target="_blank">📅 12:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666904">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
تیراندازی در نیویورک در روز استقلال آمریکا؛ ۸ نفر زخمی شدند
🔹
به نقل از ای‌بی‌سی نیوز، اداره پلیس نیویورک اعلام کرد دست‌کم هشت نفر از جمله چهار کودک، شنبه شب در جزیره «کانی» نیویورک هدف اصابت گلوله قرار گرفتند.
🔹
در حال حاضر از جزئیات حادثه، وضعیت مصدومان و انگیزه این تیراندازی اطلاعاتی در دست نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/666904" target="_blank">📅 12:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666901">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
بابل عراق هم روزهای چهارشنبه و پنجشنبه را تعطیل رسمی اعلام کرد
🔹
تاریخ به قدری عجیبه که: اون شبی که صدام گفت فردا ناهارمو تهران می‌خورم؛ به خواب‌شم نمی‌دید روزی بیاد که به علت تشییع رهبر ایران، کشورشو تعطیل کنن!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/666901" target="_blank">📅 12:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666900">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d47a64a2.mp4?token=pz01kDo1NdtoLQ-cKkUDw8yWzpK53ZOdl_Uw3BkUpShUkagVz33CigR2XU0G9scXRg6EwNZRbbUacsivlPQpMiqFgTraWN2aE6F2zV28ZQEeOVK7A_plm2Q6BmaHf4txNCWjpmGnjPpB6d4TgwD951DHXSl-i5BJGZSfWjwG8N7TEhSW8ZYZWGYcUnRC2Y0Qef8t_qmQ0mTfOhhmD-Sp3n-rO9VyrKJ2Q4kKjZy9HPXE2p5NgvNnXPuKVoEdDboNDo8Jg7euxepOMkUliXWzCa1YZnogjbgZXQCrUgcBKipoz2IR4NzJONAmosM0CW8xjfQAIT089A0bdFz_iX8cFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d47a64a2.mp4?token=pz01kDo1NdtoLQ-cKkUDw8yWzpK53ZOdl_Uw3BkUpShUkagVz33CigR2XU0G9scXRg6EwNZRbbUacsivlPQpMiqFgTraWN2aE6F2zV28ZQEeOVK7A_plm2Q6BmaHf4txNCWjpmGnjPpB6d4TgwD951DHXSl-i5BJGZSfWjwG8N7TEhSW8ZYZWGYcUnRC2Y0Qef8t_qmQ0mTfOhhmD-Sp3n-rO9VyrKJ2Q4kKjZy9HPXE2p5NgvNnXPuKVoEdDboNDo8Jg7euxepOMkUliXWzCa1YZnogjbgZXQCrUgcBKipoz2IR4NzJONAmosM0CW8xjfQAIT089A0bdFz_iX8cFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدانگهدار و به امید دیدار آقای شهید ایران
🔹
امروز تیر آخر را به همه ما زدند، اما ما هنوز باورمان نشده که دیگر جسمتان کنارمان نیست.
🔹
امروز همه باهم شهادت دادیم که جز خوبی از شما ندیده‌ایم، این همان جمله‌ای بود که شما سال‌ها در رسای یاران خوبتان گفته بودید و امروز هزاران نفر ایرانی برای رهبر ایران دوستشان سر دادند…
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666900" target="_blank">📅 12:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666899">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e935df3aa8.mp4?token=iigZ7j0Clo3rL394o4NWSjGqHyULIeTgyrYY8ruqpaLoSRUOkT5Tuft_-S-Qky-GOO1HW6Jj87hgb8U_fwHSKC9UpGOwV7KS3n6Vj5xskdSpfxvR1IIMB8JptWqz2MuU6CWc3j7oBowaElYR02WAka_jU0wNXCaq0XdUtnx-voxvPpnsbERhJ9_2T06EkVhlGFhwswevdGLhekDReAhZCcw0Cn7sSIxxgI4elB9rQIBEjBlpcRqS29OMFuCVu4lBcGjyYd-8ObOlrSLbPtIDdLEYzkrGHqF4H4cRMt78C4JZKjFz1ryJU_z6QD-DKX4d3F-7omY5iYyVTNQpuhgwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e935df3aa8.mp4?token=iigZ7j0Clo3rL394o4NWSjGqHyULIeTgyrYY8ruqpaLoSRUOkT5Tuft_-S-Qky-GOO1HW6Jj87hgb8U_fwHSKC9UpGOwV7KS3n6Vj5xskdSpfxvR1IIMB8JptWqz2MuU6CWc3j7oBowaElYR02WAka_jU0wNXCaq0XdUtnx-voxvPpnsbERhJ9_2T06EkVhlGFhwswevdGLhekDReAhZCcw0Cn7sSIxxgI4elB9rQIBEjBlpcRqS29OMFuCVu4lBcGjyYd-8ObOlrSLbPtIDdLEYzkrGHqF4H4cRMt78C4JZKjFz1ryJU_z6QD-DKX4d3F-7omY5iYyVTNQpuhgwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقا حلالمون کن...
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666899" target="_blank">📅 12:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666898">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUpjScpSgSscR2Ksjh6aagthIN0ghlpthC235EjyFRrmSMMrrJ_853jOlmlU0d6Xx-qllcvXoFU-5SSHkAFAH4Xwk6YdIhccM6EHUP9GN0hlIfqqqW3wmSIy_Ri9Cl16U8jstRwZcIW6HTH0ELMNpwgyuJUcS8KYAX5TOZu2dxMdKt24mVKxjLntooZX5YM6O66SZtZq4QSluFZuLwpK8_eDSm6WuEk1YxV4zCbpSQU34HBcl-nmlpPBrKGu-OcyHXzH8fwsat6wFbgaR3o-BVGyowB2HvJ-HPGqZtPqg6VBCBfbu2iifO_yIj3nNtrmy2fn5UOJB96AtpfdATy4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حادثۀ دریایی در نزدیکی یمن
🔹
سازمان عملیات تجارت دریایی انگلیس از وقوع یک حادثه در فاصلۀ ۳۰ مایلی جنوب‌غربی الحدیده در یمن خبر داد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/666898" target="_blank">📅 12:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666897">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWE7KFc14PkKYfUUA2nuIY7aEs_fi-ZmpzbEjVWmI4aZHg7pHwSeVj2f7SN3i1O5ntbwkjBiOH3Whf0SqPVqtZSvq2GggKOJZ1-xCqY1XgrXXOvvASaCbI1FN_yXoxhHTxz8WFtzw-G3PpVvDnv2ISNjXPQNGodo2oyo2vuxFc87sr9sJDs6h0IaiZzM3G1_vEaQPpPQVt-mjj54LneintLJAVYdWxx_D01Mr1d1iXxIDlvzAXMXJApizq0cRmg_aB3lBlJiC5C4HODfd8sHP0U5hcVzoyhvquiFbj4ZNw2eBZyJs0-ycxdNnufc3vvhLs9u6bo1MqfMhCezz7hvvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بلومبرگ: تردد در مسیر عمانی تنگه هرمز شدیدا کاهش پیدا کرده است
🔹
خبرگزاری آمریکایی به نقل از «گزارش‌های دریافتی» از ترددهای دریایی اعلام کرد که میزان عبور و مرور شناورها از مسیر ساحلی عمان در تنگه هرمز در روز یکشنبه به‌شدت کاهش یافته و به حداقل رسیده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666897" target="_blank">📅 12:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666896">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f817e286a.mp4?token=VuSXq7SU-9lf-kg-DxudgT3ppwu75KYsPtAnX--h6W8QDkqzyDN0YEVcxHk6KZORkcdF2AFjm-RCX_XCtGe_hwAW8yUJnUnobxwdstb9YGT1qNm_tzp8xx68-kBQFhvzFqtwCAGcXCt3-nTr7YoNcz2CeeAi9QU73vAAXlizn_WDxTJKKr-R_EOEFNCFNy3Ff7tQgOkr8_P89f74yWG2iITnUMkxabeJ9QPTgWjgsK5eGw44_m9jJQzS9P-p06qB8LdK08DKXrYiFmqU0ROq1rg976_SevAbvzjBR76W47itwiiC-NM0lpwFq5U8tkVkG2Jgo3tcHOJu6BvYvBZuow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f817e286a.mp4?token=VuSXq7SU-9lf-kg-DxudgT3ppwu75KYsPtAnX--h6W8QDkqzyDN0YEVcxHk6KZORkcdF2AFjm-RCX_XCtGe_hwAW8yUJnUnobxwdstb9YGT1qNm_tzp8xx68-kBQFhvzFqtwCAGcXCt3-nTr7YoNcz2CeeAi9QU73vAAXlizn_WDxTJKKr-R_EOEFNCFNy3Ff7tQgOkr8_P89f74yWG2iITnUMkxabeJ9QPTgWjgsK5eGw44_m9jJQzS9P-p06qB8LdK08DKXrYiFmqU0ROq1rg976_SevAbvzjBR76W47itwiiC-NM0lpwFq5U8tkVkG2Jgo3tcHOJu6BvYvBZuow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بدرقه یار...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666896" target="_blank">📅 12:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666895">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSw_4_lk-ujwzPESPAZFgMEMnrknMM1kiq335BKSU3dqIejVuILGpHQKthEoqDwnDN6w_Cp_T9o4s1zpt94Szf7eu2sn0Vw8_lKpYneQTJ_twuCBfXDbUmByGh3QACgiLjW1WkHIfjols3gmMwxKDIe5PvHwio063i1m2fqTHnkplpNu-DRxvS_GfehjqLOUGJG9y0MqGgkuRYTt2KTtmLnauqQkYqaUcKvdmUwvXgf3p7JLIGvPpilly9FMVJ50LVeuOe4U97-ph8w66vEUAdLUcXvx3NU4iUd5kJtaqqhAW9O0lXuE0Q7EA2bBLTX1CkbA7wqg1dhZiHByjtNF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام آیت‌الله مکارم شیرازی هم‌زمان با وداع و تشییع پیکر رهبر شهید: قاتلان و عاملان این جنایت بزرگ‌ مصون نخواهند بود
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666895" target="_blank">📅 12:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666894">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏆
خروس‌ها با تک گل امباپه به یک‌‌چهارم رسیدند
؛
فرانسه به‌سختی از سدِ پاراگوئه گذشت
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/666894" target="_blank">📅 12:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666893">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOEjxr-X76Ju1w5jxhYjJfUM-qTkaU3wwdGCPIWJbXzVT1DAp4OxTUU3jpsPgjRcWJDZF_0R7TslE3d4ffB7SqFAe8y6Ra5bDNVKu8cVpG-AzUx4-gUpqQlZQhAXu_yLyowpL-VHXKsQHmDkkCLqJSEx7_rmKgbZK-JOowKwKczbUihNhIVuIjBLIGdn7c3hNeopM1thV2NVARoBX8HkttkbMQ4HQE4CyZYn_nj_PjVVo77NucL9HsPer3OBJRXlBJDJ9_gRPFu7arLNWyEdocip00FR0SrC8R5Bf2eURHz09VT1O04wJHVO7XEnKPhLDUk1gXI0yBw_ckB4h3CwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اکونومیست: آمریکا هنوز یک قدرت بزرگ است، اما دیگر مانند گذشته بر جهان مسلط نیست
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666893" target="_blank">📅 12:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666892">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
تاکسیرانی تهران: تاکسی‌های ون تا پایان مراسم وداع امشب فعال هستند.
🔹
استانداری هرمزگان: احتمال شنیدن صدای انفجار ناشی از خنثی‌سازی مهمات در امروز وجود دارد.
🔹
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان
خسارت جانی و مالی نداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666892" target="_blank">📅 12:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666891">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cbb8c8226.mp4?token=lTCu_9wbHT3OQBicUuQa8vwGme90jARx4B49HqyCV5Wotxjhsgb6Ow0kZT2ogX0FFdlPCKE33DN5FiOTLf_LJqvDf7twcHFKg92ydzAMA0wexMttsud1XtSrPLkZPNHQjZlprxcfAv1BGtzlqIyjbvB3Kw_wZVnbAIBfXBU42vI4RRMDprZZoeaPWpRtPnCqJFFhnCd4-REwvEmtqlOP5kOrfHoiVWXdJ-r6wtJ7uIDPvCkSWYt6uj9tBNxNkfgYBLysj_ElJW_fiCXfrTcoN8xsPB_Db3uBNQ6T0lmJgefGf88oZ7BWU4z37fFyRPaf31HdNEedXjaHthyuwWAwUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cbb8c8226.mp4?token=lTCu_9wbHT3OQBicUuQa8vwGme90jARx4B49HqyCV5Wotxjhsgb6Ow0kZT2ogX0FFdlPCKE33DN5FiOTLf_LJqvDf7twcHFKg92ydzAMA0wexMttsud1XtSrPLkZPNHQjZlprxcfAv1BGtzlqIyjbvB3Kw_wZVnbAIBfXBU42vI4RRMDprZZoeaPWpRtPnCqJFFhnCd4-REwvEmtqlOP5kOrfHoiVWXdJ-r6wtJ7uIDPvCkSWYt6uj9tBNxNkfgYBLysj_ElJW_fiCXfrTcoN8xsPB_Db3uBNQ6T0lmJgefGf88oZ7BWU4z37fFyRPaf31HdNEedXjaHthyuwWAwUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سیلی حقیقت به دروغ‌پردازی شبکه اسرائیلی اینترنشنال!
🔹
دروغ‌پردازی رسوای این شبکه بار دیگر نشان داد که برای پیشبرد اهداف خود، از تحریف واقعیت و طرح ادعاهای خلاف واقع نیز ابایی ندارد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666891" target="_blank">📅 12:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666890">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o0lWLCMkiELifCe0IyMDyP-QH6oAL3DFSwwon4ZD0952Z9N-7rvzjuBZRosEZHVi6xl-45BlxZXsrokQj8sqEiqub4X9LbC4n0r4yxwHHuWrFjEcDiea5v29HcpPed4JE3BCGjumTUZT0GQZD5JsyuttmErDVd7BAoLzVF0G-K-un4jHziI7gSwnzPlg5cE9LhMGoTjOWYycrfhUrMOEZEu1wpDOb6qg179aW7J5DlClRe0AshIrWP3o63Hz_V2-mzhV2_glDZK1AL9b1BTgJBuUNSV6wEnIwcuiY3VT7vulY8S1ctdGL8LHr3FP4gomlO5ZXBQ1YOmrZtg91MPG5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ویدیو ترجمه آیات قرآن که در حضور نمایندگان آنان قرائت شد
🔹
عربستان سعودی: آیه‌ای درباره دو ارتش که در جنگ بدر با یکدیگر روبرو می‌شوند، یکی پیامبر به همراه مومنان و دیگری مشرکان مکه
🔹
ترکیه: آیه‌ای که کسانی را که در راه خدا می‌جنگند، بر کسانی که نشسته‌اند،…</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666890" target="_blank">📅 12:15 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666889">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
به جز دوشنبه؛ اصناف تعطیل
نیستند
رئیس اتاق اصناف ایران:
🔹
به جز روز دوشنبه، هیچ‌گونه تعطیلی سراسری برای اصناف در نظر گرفته نشده و تمامی واحدهای صنفی مجاز به فعالیت هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666889" target="_blank">📅 12:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666888">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff6cb3a28d.mp4?token=p0Jl0853NFEM3NV_1s8UatfhZ1J-EGChayHyLhch_djardkmvRRbro269JM1We4Z-cFxK5sscknOawYe0bwxcNDRuu850MF6NMqz45DgR6fIJCgIfbNBRztjHKpgukiwQjPww1RYVoCR2k_u26NJXRH151ZkV_SS7Kh1qHwfAJnZaHu50f8qMMF3IsAyRGiNr4-972e2ZhJggMYAmzOvh4B1GYUIq-2eTs9sZuOoCoNmDQk01HnDVBr5SL-74pQlaj6oYn-LgiNQLtW7Kt996UUxgtGg4Yt1_IHQLXfzCR8sgET6ROQalQ6gU_yO3qsXAeC85s8eMzdszT5AJj_rdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff6cb3a28d.mp4?token=p0Jl0853NFEM3NV_1s8UatfhZ1J-EGChayHyLhch_djardkmvRRbro269JM1We4Z-cFxK5sscknOawYe0bwxcNDRuu850MF6NMqz45DgR6fIJCgIfbNBRztjHKpgukiwQjPww1RYVoCR2k_u26NJXRH151ZkV_SS7Kh1qHwfAJnZaHu50f8qMMF3IsAyRGiNr4-972e2ZhJggMYAmzOvh4B1GYUIq-2eTs9sZuOoCoNmDQk01HnDVBr5SL-74pQlaj6oYn-LgiNQLtW7Kt996UUxgtGg4Yt1_IHQLXfzCR8sgET6ROQalQ6gU_yO3qsXAeC85s8eMzdszT5AJj_rdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه آخرین سان‌دیدن فرمانده معظم کل قوا؛ شهید سید علی حسینی خامنه‌ای
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666888" target="_blank">📅 12:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666886">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb70a25114.mp4?token=JWxP2kvV-uEZHt6Gj2sIUmMDZH-0IAb0AgPN8Du0i96JlWLOtYvNqmeD-j-RjZm0kV85ob1_SmRI3Y6I0yEe2Qp5Raz3wznPiktaPSgooFOyYQYkfWrtg8Bt8XC1pPPoXrE5D9Qu570tPx0L_h-SO9l4aElLKuAJ2Ui6uYMqZrtK1KLAS0y769rQIcdhPmiRJiVLmdSLgAmaaGVZRUvRJdb-yJ8BE0d0Dr0FaXxw-l2X0mmew_vkhrwtEYMDX-Rqcn-GGN_nVjqjX1SU0y5YITBuRI5vOrrFxpXRBvmiO8imsVrjLaK-alK6u7JGbG52dDW3crqyqpwsLfyiJajvzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb70a25114.mp4?token=JWxP2kvV-uEZHt6Gj2sIUmMDZH-0IAb0AgPN8Du0i96JlWLOtYvNqmeD-j-RjZm0kV85ob1_SmRI3Y6I0yEe2Qp5Raz3wznPiktaPSgooFOyYQYkfWrtg8Bt8XC1pPPoXrE5D9Qu570tPx0L_h-SO9l4aElLKuAJ2Ui6uYMqZrtK1KLAS0y769rQIcdhPmiRJiVLmdSLgAmaaGVZRUvRJdb-yJ8BE0d0Dr0FaXxw-l2X0mmew_vkhrwtEYMDX-Rqcn-GGN_nVjqjX1SU0y5YITBuRI5vOrrFxpXRBvmiO8imsVrjLaK-alK6u7JGbG52dDW3crqyqpwsLfyiJajvzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دل نوشته عزاداران مصلای تهران در آخرین ساعات وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666886" target="_blank">📅 12:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666885">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
زندگینامه مردی که وجود خود را وقف انقلاب اسلامی کرد و اگر چه او را به خاک میسپاریم اما خاک ایران را به ما سپرد که نگهبانش باشیم. به رسم امانت میزبان مهمانان آقای شهید که مهمانان ایران‌اند خواهیم بود
موشن گرافیک زندگینامه رهبر شهید بصورت خلاصه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666885" target="_blank">📅 12:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666884">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
برای راحتی و آرامش سوگواران رهبر شهید انقلاب در تهران، مجموعه‌ای از تدابیر جاده‌ای و حمل و نقلی و خدمات سفر در نظر گرفته شده
🔹
قبل از حضور در مراسم تشییع رهبر شهید انقلاب در پایتخت، به این نکات توجه کنید.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666884" target="_blank">📅 12:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666883">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d91617dbd5.mp4?token=gs2J4Df6ZZABylzW9a8L3wobl35c0tOF-vcubbYba3skuBCfGCDB7fuApGRztHdB1p19Cu2iRqK19Cvpjx62QdTyt3fQ3-YbMZOfK37SMqwKNb2MAZYuaMieBuBwsX6x3AQFug2NgG_K_PToa-6TnChAvFEdnT5sTqNX8YpdBbz89OKSP7NeEyKJsA2Z9iIu9ozX0fxcb8f4xxI6BnIMeT_gOKuXP-S394JY_ZEngMcooWeFKClcWGHMOcaqtg_d41upMMQcX5Ya4lVDxw0ChjjTaGWx8829zU7IByTnmsj_NuEnr0SD9EvHlukkY7hdpCIyoSabb9o-xPtEP6vNWF5NvlxfE5MLiJOYOJ_w6a89QEdrj8CnmXw0EeLnrQC3DJBlJxut0jhdRq5j5jzXysa6AlgGgoIF-PuwJYzeu5jHYkWS4aqEUFpg36ceejUo0HGmCijwohw8cwn3BhfYQalCxWH0JuMO_Vjn8B6qe6JPdZtDZaA62i1r2cM0jbjetTuaU_B0iHMvMR6dsLpSGbkmpkXStnqSSfK_qhhaCcErF5XnVoHZ2Z_ffXIL65zPPDQZw-jj4Qqy9Z9ThDa0TZih3WzjnnN4JDbiJHdLnD45lyKlGRx67awZZ6Ckj1EpaM8FShaC0-6OYF1Y3ZvpmFluRiokynh4dzj_JlyhCUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d91617dbd5.mp4?token=gs2J4Df6ZZABylzW9a8L3wobl35c0tOF-vcubbYba3skuBCfGCDB7fuApGRztHdB1p19Cu2iRqK19Cvpjx62QdTyt3fQ3-YbMZOfK37SMqwKNb2MAZYuaMieBuBwsX6x3AQFug2NgG_K_PToa-6TnChAvFEdnT5sTqNX8YpdBbz89OKSP7NeEyKJsA2Z9iIu9ozX0fxcb8f4xxI6BnIMeT_gOKuXP-S394JY_ZEngMcooWeFKClcWGHMOcaqtg_d41upMMQcX5Ya4lVDxw0ChjjTaGWx8829zU7IByTnmsj_NuEnr0SD9EvHlukkY7hdpCIyoSabb9o-xPtEP6vNWF5NvlxfE5MLiJOYOJ_w6a89QEdrj8CnmXw0EeLnrQC3DJBlJxut0jhdRq5j5jzXysa6AlgGgoIF-PuwJYzeu5jHYkWS4aqEUFpg36ceejUo0HGmCijwohw8cwn3BhfYQalCxWH0JuMO_Vjn8B6qe6JPdZtDZaA62i1r2cM0jbjetTuaU_B0iHMvMR6dsLpSGbkmpkXStnqSSfK_qhhaCcErF5XnVoHZ2Z_ffXIL65zPPDQZw-jj4Qqy9Z9ThDa0TZih3WzjnnN4JDbiJHdLnD45lyKlGRx67awZZ6Ckj1EpaM8FShaC0-6OYF1Y3ZvpmFluRiokynh4dzj_JlyhCUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صحبت‌های پربازخورد زائر رهبر شهید: از سازشگر متنفرم/ من فقط انتقام می‌خواهم
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/666883" target="_blank">📅 12:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666881">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
هر موبایل یه رسانه‌ برای ماندگار کردنِ بدرقه
🔹
هر لحظه از این بدرقه، داره با دستای مردم نوشته میشه.
🔹
هر موبایل یه دریچه‌ست به حقیقت.
🔹
احساس‌ها موج می‌زنن، اشک‌ها حرف می‌زنن و روایت بدرقه رو در تاریخ ثبت میکنه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666881" target="_blank">📅 12:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666880">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7144b2b2f.mp4?token=HI_SJASOebYQO5UZlsZ2ej06Yzp29Llk5GV-8KlRgNbz-pfHy0ngc0ggNn8QQe5D3xDo6e6pA2sonxjcp5faMSVtE7pjLmaDEOvc9MY7MLBVsd3OpDYZeFTkjJK0NjOjGcrtuHo9vBPvjpUAumgApwRp6iCVmscRR2THDPQUHPacakFrJuAjrGwNZJxWlatPnOMRR93uuU0AGX8fKRhN9clJpITQomcKmKCCwaYWsvzJrPez4D8-jvCLwsKKhFS1hgMpWRKRtKi5qf_7SDJA9Jb3fD2c7KbM5glVHDR6xzjePXYGpJYm5lDME19M2-fjcntD9377hjmjQjMPs3ubZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7144b2b2f.mp4?token=HI_SJASOebYQO5UZlsZ2ej06Yzp29Llk5GV-8KlRgNbz-pfHy0ngc0ggNn8QQe5D3xDo6e6pA2sonxjcp5faMSVtE7pjLmaDEOvc9MY7MLBVsd3OpDYZeFTkjJK0NjOjGcrtuHo9vBPvjpUAumgApwRp6iCVmscRR2THDPQUHPacakFrJuAjrGwNZJxWlatPnOMRR93uuU0AGX8fKRhN9clJpITQomcKmKCCwaYWsvzJrPez4D8-jvCLwsKKhFS1hgMpWRKRtKi5qf_7SDJA9Jb3fD2c7KbM5glVHDR6xzjePXYGpJYm5lDME19M2-fjcntD9377hjmjQjMPs3ubZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشاگری پزشک رهبر انقلاب از علت مخالفت صریح آقای شهید با وارد کردن واکسن فایزر: بعد هشت ماه مشخص شد که ماده‌ای در واکسن فایزر هست که مانع بارداری دختران جوان ما خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/666880" target="_blank">📅 12:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666879">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cc59f37b8.mp4?token=C1o-VBD8Volb3ptHlohajMFd6UVvmh5f3N3UK2sT2mqLNI-msHFU-dWlGST0wxXBpLa6TPQYL0OQVOSH45blItTGSF_znfC9L7x13hiiklxCU4rZncwKmYCLFPdjhKdUm0f7TTqX0QD0a18B2JqbIa5wUlTtV3Qk_DvdCP2VPmYxJPaa9-tbGm0XeE-gt2pqBiKNKiXcC90kF0ZFpnAyjyXvlakom-TprljULiyENcva64nvSaUGcnr4hEcS5L-iPRHtXk5f_yEOSTCx_6Bqf5Iiwlzqd6gmexNxyZOE4QwW0Bu_BYDggXsS0XWChmxFYmW3eXjq0MMK6pZiN96bjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cc59f37b8.mp4?token=C1o-VBD8Volb3ptHlohajMFd6UVvmh5f3N3UK2sT2mqLNI-msHFU-dWlGST0wxXBpLa6TPQYL0OQVOSH45blItTGSF_znfC9L7x13hiiklxCU4rZncwKmYCLFPdjhKdUm0f7TTqX0QD0a18B2JqbIa5wUlTtV3Qk_DvdCP2VPmYxJPaa9-tbGm0XeE-gt2pqBiKNKiXcC90kF0ZFpnAyjyXvlakom-TprljULiyENcva64nvSaUGcnr4hEcS5L-iPRHtXk5f_yEOSTCx_6Bqf5Iiwlzqd6gmexNxyZOE4QwW0Bu_BYDggXsS0XWChmxFYmW3eXjq0MMK6pZiN96bjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در میان فوتبال، غزه را فراموش نکنید
🔹
صفحه «m.z.gaza» با انتشار پیامی همزمان با مسابقات فوتبال جام جهانی، از مردم خواست: رنج مردم غزه را فراموش نکنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666879" target="_blank">📅 12:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666878">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28bfb2f159.mp4?token=ERY4aVpluuxpGEPQloZZ88r3UUuXnkbpcebK_lMxJH9DKhsZGTOlh9tqY_Ju4pAv7EFT_BQFqKbSbGq14kKmPrmuizFCK1noXemJEH0Rh9fqijesy_IhlizXB_C1hsLi17V6eTVPTqfASeRjewyOC762ZJZVuHmb_ij1bFYJSSalSeo0O35ILfG_qvvbTinaPkXF-u0UEP6sSkw4rICl3W3pfN0ghKlGILADxK-ujWm3pUdo7WIlBbeEkscq-Z9sP5tzmXJQEqb2YUIvb3XNyqdRcZLr-iGb3x5fbHBm6DXl3liAfSmk8cfltG_ubEsS-27fCaMB4r-me8WE00D1eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28bfb2f159.mp4?token=ERY4aVpluuxpGEPQloZZ88r3UUuXnkbpcebK_lMxJH9DKhsZGTOlh9tqY_Ju4pAv7EFT_BQFqKbSbGq14kKmPrmuizFCK1noXemJEH0Rh9fqijesy_IhlizXB_C1hsLi17V6eTVPTqfASeRjewyOC762ZJZVuHmb_ij1bFYJSSalSeo0O35ILfG_qvvbTinaPkXF-u0UEP6sSkw4rICl3W3pfN0ghKlGILADxK-ujWm3pUdo7WIlBbeEkscq-Z9sP5tzmXJQEqb2YUIvb3XNyqdRcZLr-iGb3x5fbHBm6DXl3liAfSmk8cfltG_ubEsS-27fCaMB4r-me8WE00D1eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ پس از تهدید مردم حاضر در مراسم بدرقه رهبر شهید، از ترسِ انتقام در پناهگاه ضدگلوله سخنرانی کرد!
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666878" target="_blank">📅 11:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666877">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SjnMI71BRGyTqQL4oz9ajGCynPP5Md8k7hA-DlwnliW7NPAHJsTFqS1LZ7bU1QWK2ibQpeL82SUbWlLHb4MRDbccDoopv9vD0ttFqK0y-Q2wCv6Bp8cDCNEtJxvL1wVbJEwxz4xgWRmSKA2ElXZJoj7fhtZe05v7Xnke_dqQecQbkUBVuCmMzOE2w7VBTueGteRgWvp6XKiO7ggkw6I-Erjq-N7ENuZxPiwUnKoimMALPBdN4_Q62qBsJnjeWteHV5L3v1wqO5OkQfxrJRnvmcQOZHj7kA_Dod5cIkmEtBvg31xUTl-GxY5XB_S_-GJzcXXI643JACoqvbI8_cNCVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥀
به امید دیدار
آقای شهید ایران
ما پا به رکابیم پدر تا برسد یار
ای رجعت تو ناب‌ترین لحظۀ دیدار
#رهبر_شهید
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/666877" target="_blank">📅 11:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666876">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">♦️
هشدار انصارالله به ائتلاف سعودی درباره هرگونه تحرک متجاوزانه علیه یمن
🔹
محمد الفرح، عضو دفتر سیاسی جنبش انصارالله یمن نسبت به پیامدهای تشدید تنش هشدار داده و تاکید کرد که یک حمله ما علیه عربستان می‌تواند آنچه را که این کشور بیش از ۱٠٠ سال رویای آن را در یمن داشته است نابود کند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/666876" target="_blank">📅 11:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666875">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
رئیس‌جمهور پاکستان، هم‌زمان با روز استقلال آمریکا، از دونالد ترامپ برای سفر به پاکستان دعوت کرد.
🔹
حشد شعبی: تمام آمادگی‌های لجستیکی برای تشییع قائد شهید فراهم است.
🔹
داروخانه‌های کشور در ایام مراسم وداع فعال هستند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/666875" target="_blank">📅 11:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666873">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
‏
سخنگوی ارتش: هر خطای دشمن با پاسخ قاطع نیروهای مسلح ایران روبه‌رو خواهد شد
سخنگوی ارتش:
🔹
اگر دشمنان خطایی کنند حتما با پاسخ کوبنده و قاطع نیروهای مسلح ایران مواجه خواهند شد.
🔹
بارها اعلام کرده‌ایم از فرصت آتش‌بس برای ارتقای توان رزمی خود استفاده می‌کنیم و یک لحظه را هم از دست نداده و غافل نمی‌شویم.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666873" target="_blank">📅 11:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666872">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdxsKpBANhH7xoYinj-J52OjRpPLAL4qPp9r-bOxlGj2lWCNTS72OUvoynYgYcLVVOFFWKKPY_fesBLRt_F0GrxFg1R2tj7Xbu29gEJwYWj6Tw0nQZ7wbwAiIO3M5kLYIK5jsD7PgBp267opgDYEy_mRTfePp9moDydqZIZ9qYZGtMawIfKnCFetREGRPJV2iCJf7hG3QxjGgtM6L5Fat1fxje9YmSZSuFYLVzoa3yl9VY2J94EaDPxshR6z3keoYfkIwteOGehIz2wOYU7kE505dXaxUEOqdKJsehvsQn_bi-ST9-AOWcQXI1FCuHt6KjVrGxFGfc32Pnos65r9Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
باشگاه پرسپولیس مذاکرات مثبتی با مهدی تارتار، سرمربی فصل گذشته گل‌گهر سیرجان انجام داده و این مربی در آستانه امضای قرارداد با سرخپوشان قرار دارد/ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666872" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666871">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
زمین لرزه شدیدی شهرستان بستک در غرب هرمزگان را لرزاند
#اخبار_هرمزگان
در فضای مجازی
👇
@akhbare_hormozgan</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/666871" target="_blank">📅 11:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666867">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tExnkx7dxBQ-RWsNI7N1vQl9Zkz3EK5jGsbYZ4ZjkjT_p_8OJfKwNjc4xdNG7qcTo4QLiIbxbXuwebnOURMmzLgppEPw5aeRoYOscGosw1v0eoAoBcfzQiezxbS62f8jBermgZu9dkEbf0DBlS1LWjuZkllLSVdKtBm1CT3v6brg4oPN3P5IW7_WcVgPZxPqrGVYaXuRXBJcYaG_KvdCQvrZSrNhN7PLhsI_IHgJEXSE9NR7uFfVLL_cx0U2EwnFmTuo6iGZJX5ZQrDBO1xoGPhF0eAfOmWcmeP0efJgpxDwWsYc07mkOO05ImqoW0L9aAHMo87qrR2eBVZ_Fcu1Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oqWgsQhSR26Ph0xFMyy0AIPaE4wStCam_Di3vxYIr3z7YfLFzWPfh87scoAbGdTBDnvLMqYwCRxs377Se9YaIyPQEJcqnfARXL1sV7CBhtom1mIIz6wDHTjCpT0nQR3VYaHc1dxjExCAGwNYNVe8rYqV3JAz1NRNebO5BvZ2WGn8qgMx1kZuw7bK8XrCKjTol8ldrD3TVIdFKWEVLPEVZXVUkebpAAOrzhqmC9MYG-7xIYLeJ9_poZHSfZBSclggxQpG-bCpq_6Eic4y4qg0HOpBtMwyMtz9ytk7uGUNZjMahBTIgsBYbEZo4wqxCyOaquykBwRUUNb8ATMsMuDkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G_Z0fPTsh0TVMzxjTvcTqD1Pm9DM8iEq-qSrxi-hAY2lpwLyG5AoRi39ob7REPlAAcoYYmMVp6ZWcSODAjL6bIFfeAzxrKk6kd6Xa-IRAqZgY_lxxNjKvCk-6mpaaWZP15qJ2SAmzN6ujF1-hqrh5iwaGAL9d_fwYWgy7vZ5z99mr-GuDr5YUJ9JHzy3aXFFMBPmf6mKwcSvYm4Pm4yL37YwL3ETFqwRJ1rojmQF7IaCyrfQ1oJOk36nXJXCX0AE7Uy28CTxlEJC6oa_vtrBsWOFTZdN1iSE8QmKxgMkp04R976huTclW-SrPbpNb821z2dssWryxexZEABcEtrZSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hoHXi6rcBY7fw6oy-a3ra-weS0TRYsb73s0E-HBTdochJH6Mo0mlrLj9VXZmtqiudkO29r9GysKJQIVvNqHel_bZh3HGwgYnqH9QJCDfmIfndslR8ddWtTE7TybdqzG5Vo7zM48Vz_HJoU8ZU2MwxN-9vS8vRH_eHtyYQ_LCUWHhiRuLuSpDIDh0owMrVodsPwOcpcqTstwCIlByjx8I7_1Pv6gcevIiki3YqmWo5hiBTpjYVqumvl7fNAxjy7UC9842kqP481F3ACNJdpTk_iszEnpYVtDc-qIdj9iZ9E60Miq7vTUmBEKSYPOLNccNcdQN0br0LiiS7-ntXxSjOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
تصاویری از یک حضور تاریخی؛ جمعیت باشکوه مردم در مراسم اقامه نماز بر پیکر مطهر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666867" target="_blank">📅 11:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666866">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9429f0e319.mp4?token=CpxYIFbo7QOODcEr7R9o516ZYnlRgHWmJHkBc-2NkXE3Am34MY8PMTVaR-I-5JRCwOWyoTgbBro7fBEcZFN6znUXt4Ql9DmVhmMWJFMAtAFSkqfmpm5aP-zO8QLbXejF4yd-jkm5Y626v_Sih8BCCbKPf_FujDxF8wsRuyNSw04igA4todffLdvHWKnRWrYih57axs9BqX2gGgBl7bhzEnKS9ZJWe-lAhkdA3vf5kcxOE5nZJhZnxP2QssCUUyk2y3Gvfn2SKzF_IbGBCiY3W676Enq7urkiWcK9naRJ7i5_8-JYzDwTEY97GzyzG6SxttNMCftsIyi9P-83Y9K-5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9429f0e319.mp4?token=CpxYIFbo7QOODcEr7R9o516ZYnlRgHWmJHkBc-2NkXE3Am34MY8PMTVaR-I-5JRCwOWyoTgbBro7fBEcZFN6znUXt4Ql9DmVhmMWJFMAtAFSkqfmpm5aP-zO8QLbXejF4yd-jkm5Y626v_Sih8BCCbKPf_FujDxF8wsRuyNSw04igA4todffLdvHWKnRWrYih57axs9BqX2gGgBl7bhzEnKS9ZJWe-lAhkdA3vf5kcxOE5nZJhZnxP2QssCUUyk2y3Gvfn2SKzF_IbGBCiY3W676Enq7urkiWcK9naRJ7i5_8-JYzDwTEY97GzyzG6SxttNMCftsIyi9P-83Y9K-5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظاتی از شعر خوانی محمد رسولی:
‌ کسی که کشت امام مرا چرا نکشیم
که ننگ ماست اگر قاتل تو را نکشیم
از این به بعد کفن، جای جامه بر تن ماست قسم به خون تو، قتل ترامپ گردن ماست
#خونخواهی
‏‌
#هزینه_خواهید_داد
⁩
‏‌
#WillPayThePrice
⁩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666866" target="_blank">📅 11:36 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666865">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vSTt7Gxjr-xN_ksWvhxrRxNqCez3y2ZIeL5PIfHSzI4nsCcOW5mlkZ_BSk4eH6mlGRYNVOGCSGvVxgKEtcnneWfdSSex33YuSF0-oXVxh7WALhzGXWveoA1L43QkaOZruXJdZRoXwp-udN6DvLb4hBKiA06R0_HP99TAnUYnNief-ueRgPW83AGkmc1EmYLn1Be6td4M04w_x9o-1O_MvsqOxdCC8t7GBABM1dmh8nEK08uwDAhVdBlt9e-AZ-nM_0xaJV6AFbdKRayDxI8aJ_xL1T822XT_TWbCUdc3crMTiPs3IlkEInw1Ka4qgco3lOpZVE0W4vOW56f1MROC0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استوری امیر قلعه‌نویی سرمربی تیم ملی فوتبال همزمان با وداع و بدرقه میلیونی ملت ایران با آقای شهید ایران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/666865" target="_blank">📅 11:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666864">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
خداحافظی اولین میزبان از جام‌جهانی/ مراکش متفکرانه و مقتدرانه در یک نیمه کانادا را برد
🇨🇦
0️⃣
🏆
3️⃣
🇲🇦
🔹
گراد؛ انتخاب نسلِ شیک پوش
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/666864" target="_blank">📅 11:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666863">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3235b035b4.mp4?token=Ja9G5UO2HcB76E1yv5_5fPs94Hw7gz3jrDTJ5Ek1hIMStR34l8Z4dxNwOJx5xabwk_2eBEVmt0WtiDBIaT5QExSM7LSH2eV663ZqVk0214j_ijD24u6qwXPt-YPWG_BJGDWeVzbcj5Db_uoXTwA9NMs9MH3n-luzqAsNn6olJ40jHVkahPrrg65Fdg5FzW-40BQEH2fgIDxSzay7NTr9oeINs7r5VDz1zk2Nj9qpiKQEVhpnlnPspf3Wuuwyj9n_LpOZ4mBCmlNz3udCL65G0gc7lVdKU2YK8F7ckZ1q82aVsWo19HNKFwgaIYJRgKDsiCVyiUApoijah01HZiJRFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3235b035b4.mp4?token=Ja9G5UO2HcB76E1yv5_5fPs94Hw7gz3jrDTJ5Ek1hIMStR34l8Z4dxNwOJx5xabwk_2eBEVmt0WtiDBIaT5QExSM7LSH2eV663ZqVk0214j_ijD24u6qwXPt-YPWG_BJGDWeVzbcj5Db_uoXTwA9NMs9MH3n-luzqAsNn6olJ40jHVkahPrrg65Fdg5FzW-40BQEH2fgIDxSzay7NTr9oeINs7r5VDz1zk2Nj9qpiKQEVhpnlnPspf3Wuuwyj9n_LpOZ4mBCmlNz3udCL65G0gc7lVdKU2YK8F7ckZ1q82aVsWo19HNKFwgaIYJRgKDsiCVyiUApoijah01HZiJRFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویرسازی با هوش مصنوعی از حضور شهید علی لاریجانی در آخرین دیدار
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666863" target="_blank">📅 11:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666862">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553d716180.mp4?token=NfILKZPz43tYuLlXnKlDbpyVepLMwdz1FSM8ZIsuTteRwisQJU2ukiWV9ZwrKPKL26iMLItv2raWc_ZcD1m9SFAKGSsVXgSI5CqgZgj7bdqYHk2OVKIycwJMSa8mzHMtyS0r-xT0QJpBXcDrMOkKVOVifV_gjDcQh8V-tAqxuWWT2OR5F54jJxjcOT98Cilc6ClaSKAbxCvuVe94igvbgUxiIgIn_t64w_0VyL-Kid5K8ejmCKG68FM48mEUn7mP7XNamwIIiOvatEnXfojlxR0r642OEJfUHBUxPi-Zq8wi1LTYM_8BeUFog4ufIwYrjsKc-ivELVGonpY8ZMjyzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553d716180.mp4?token=NfILKZPz43tYuLlXnKlDbpyVepLMwdz1FSM8ZIsuTteRwisQJU2ukiWV9ZwrKPKL26iMLItv2raWc_ZcD1m9SFAKGSsVXgSI5CqgZgj7bdqYHk2OVKIycwJMSa8mzHMtyS0r-xT0QJpBXcDrMOkKVOVifV_gjDcQh8V-tAqxuWWT2OR5F54jJxjcOT98Cilc6ClaSKAbxCvuVe94igvbgUxiIgIn_t64w_0VyL-Kid5K8ejmCKG68FM48mEUn7mP7XNamwIIiOvatEnXfojlxR0r642OEJfUHBUxPi-Zq8wi1LTYM_8BeUFog4ufIwYrjsKc-ivELVGonpY8ZMjyzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظات انتقال پیکر رهبر شهید انقلاب به جایگاه اصلی مصلی پس از مراسم اقامه نماز امروز
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666862" target="_blank">📅 11:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666861">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/202c4042f3.mp4?token=s7ZvWgOL9UgrxHFc1uCxssIpBdvM5wac74fB5DnB-UgsFElW1JCkxxDFrfoaxDyRIWX1K58vBa3W8QjDdYC-ePFBlHGTEDFVWLj-PvwlJKiRIXapFuJy0euaKwE_IXwQSSSLL1yPfb7YlGVoxtIPlSC43Znr5NQvrUh2jP-V9PBivbe8SWd3zVYRVdoDj6-y3Q0OL71dzj1pu0GWac12yrC7OumVgsVYd96mIKiylEbfExvpmzfspr-1Qvl2f3CqY3l3B_zo0oe4PGCBGhU0Na0DMhexi6RjI2xx3vsnyv4dh5SOwMKRi8IBAstAFv77AwXmTmstbFYJDy4y9IJqwFG3g_c5NfYpsoqUVNb_d0gy1tKTSAVNXbky7kFYwUxNgCv_0_OytbHfMUB8IANwJXzRXSOm4x-I-8S4HiCDuGwErc3vu8A5TVItEGutnt1p6nWjvkOOSO612gXws0VPS6P6oB_SQx9VXtAGPvziQqI2DWULyuoOuZBFPcUyykdMJRTk8LKAKq3Ij_eE7On28SrX_O4AKm1epg53d_b6n2DWPn2FUyrIsJM9Ti0HhvLILGq-I4mJSIaktCIxE8Zaqx0InAeipumK4APscZVADvdPqaaWDrCiMGFk8u5QOpG2JgyQj4qtFvYr5qz5ZfBEdAPx4SyzNhS1c2URUI_hUGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/202c4042f3.mp4?token=s7ZvWgOL9UgrxHFc1uCxssIpBdvM5wac74fB5DnB-UgsFElW1JCkxxDFrfoaxDyRIWX1K58vBa3W8QjDdYC-ePFBlHGTEDFVWLj-PvwlJKiRIXapFuJy0euaKwE_IXwQSSSLL1yPfb7YlGVoxtIPlSC43Znr5NQvrUh2jP-V9PBivbe8SWd3zVYRVdoDj6-y3Q0OL71dzj1pu0GWac12yrC7OumVgsVYd96mIKiylEbfExvpmzfspr-1Qvl2f3CqY3l3B_zo0oe4PGCBGhU0Na0DMhexi6RjI2xx3vsnyv4dh5SOwMKRi8IBAstAFv77AwXmTmstbFYJDy4y9IJqwFG3g_c5NfYpsoqUVNb_d0gy1tKTSAVNXbky7kFYwUxNgCv_0_OytbHfMUB8IANwJXzRXSOm4x-I-8S4HiCDuGwErc3vu8A5TVItEGutnt1p6nWjvkOOSO612gXws0VPS6P6oB_SQx9VXtAGPvziQqI2DWULyuoOuZBFPcUyykdMJRTk8LKAKq3Ij_eE7On28SrX_O4AKm1epg53d_b6n2DWPn2FUyrIsJM9Ti0HhvLILGq-I4mJSIaktCIxE8Zaqx0InAeipumK4APscZVADvdPqaaWDrCiMGFk8u5QOpG2JgyQj4qtFvYr5qz5ZfBEdAPx4SyzNhS1c2URUI_hUGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
صدای کمتر شنیده شده مادر رهبر شهید انقلاب
#بدرقه_یار
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666861" target="_blank">📅 11:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666859">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac8236b59e.mp4?token=It3LF9zYQ7hbTjMuaDeNcEv9f7F1Ji9AmNwlEzbGiro-q1Sg-ipKlHUqI7JPlerpma-nScn3HyKV-y9Dk2Tox-og9mPbcU67KaA5xR4fIFRXsiDcNjaeIIIdwjdfpeV8u9IIp3RUQ9J1ZOdYpnjee9oOTOMb61kuH1kbUA-zV3IMD4gSotsUpksXlw5r3-x-yQtKkkGUdw_4NUrlim86KWPMfi-tdC3PtOry1nQlB7EB7ojU8luLAaOo8vs5SympgZvDfX6XdAj9-WCDni_5_QIm-a1Ezf2uOF54LdJuwCgcHkk8IxmviZFEbUVyIDmjQ67X60WzEt83P360slH_Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac8236b59e.mp4?token=It3LF9zYQ7hbTjMuaDeNcEv9f7F1Ji9AmNwlEzbGiro-q1Sg-ipKlHUqI7JPlerpma-nScn3HyKV-y9Dk2Tox-og9mPbcU67KaA5xR4fIFRXsiDcNjaeIIIdwjdfpeV8u9IIp3RUQ9J1ZOdYpnjee9oOTOMb61kuH1kbUA-zV3IMD4gSotsUpksXlw5r3-x-yQtKkkGUdw_4NUrlim86KWPMfi-tdC3PtOry1nQlB7EB7ojU8luLAaOo8vs5SympgZvDfX6XdAj9-WCDni_5_QIm-a1Ezf2uOF54LdJuwCgcHkk8IxmviZFEbUVyIDmjQ67X60WzEt83P360slH_Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اختصاصی خبرفوری از مراسم وداع و
نوای حیدر حیدر مردم خون‌خواه رهبر شهید در مصلی تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/666859" target="_blank">📅 11:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666858">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b347366e52.mp4?token=mmo1-xdX3sdY2gh2puV63FWSLL9nLgP-hgPJcaUZAsQEyP0Es3UCScMFo6d1bijNaz-P4Aocebwlu4sQtOnAxzXyqxKVBmCzLr6qzUVOFd86c87a9fE6fLYrr11txF6deYm6RxUR46heZznMI8HKhS9-Hox-OZ8iUhQW7LXXNWYrtVubQVZeHJlVcwetksITY92E3L6Adwivq85LAdsmQAwWUx94XJu36ZnijDJXsE_O1yu5S4xV3NCdC_xH9wZ-dCUulu8YIQPQdQGYs5faRFqJhiVwfKPkll9OGBPTB4jFgfOXw7g2m2hvljEqcXa6sYcYnMKfqOjPUQvXaTTiVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b347366e52.mp4?token=mmo1-xdX3sdY2gh2puV63FWSLL9nLgP-hgPJcaUZAsQEyP0Es3UCScMFo6d1bijNaz-P4Aocebwlu4sQtOnAxzXyqxKVBmCzLr6qzUVOFd86c87a9fE6fLYrr11txF6deYm6RxUR46heZznMI8HKhS9-Hox-OZ8iUhQW7LXXNWYrtVubQVZeHJlVcwetksITY92E3L6Adwivq85LAdsmQAwWUx94XJu36ZnijDJXsE_O1yu5S4xV3NCdC_xH9wZ-dCUulu8YIQPQdQGYs5faRFqJhiVwfKPkll9OGBPTB4jFgfOXw7g2m2hvljEqcXa6sYcYnMKfqOjPUQvXaTTiVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فاطمه مهاجرانی، سخنگوی دولت در گفتگو با خبرفوری: تصمیم‌ها در راستای منافع کشور در شورای عالی امنیت ملی جمع‌بندی و اجرا می‌شود و نظر مردم حتماً شنیده خواهد شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/666858" target="_blank">📅 11:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666856">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E3jQgSXll7USUhu6n0DQc1sMvMsDcIopZ8cnPoWkaErkECOqXP_HcLREni-x3H6a22U6ZGrYOZGTnSc-_Id8Ii5JGi1rxtnyWvR82tmvXRUeMGxSs03NKaODx9z-aGlJdCe8bGsVhLqWBGuK4wuJX7Ttb9sEGM-SX_s-8FGeGTC5fvNVgWm1VGq2wZOatSw5i1AtESwdAo6Wf2MCq9oBS_2DNf9hQgaNBkeYcUsjJiicTIIQ9mCRdRbtF7U1LLs3UqdOrNOJGH5m8hFAQCOBjX6ZiBKsyVPwcGLcEL_7-M99R8A7kBA4l9Z0ZwABOkDWuK9vdLPfTUcEQBywKw0L8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hkj_NRuvu0jJAuMEeldJ6-2fK0GRxqHn8K_S-GbiFE4bZtLWmtklo_6dyzlRQZ8HFNaB4VasRlX6jtGAgWxQ7FeL2exfp21fX0hfnBYHS4aB0MA0YfJT_wfUA8SWlQsYBiLwAAcFBEMnXDIaOvyG96o6ICJpWtk8rwyMGXnREpUtfWbGZTTQ3kOe-6F_lRu8ZbtJfvoKgAeseoXh4_baF1MjZSx5AJkgLltl8KJnvi4BfKrZe88BJ4D4tbbgHKgX8KoGinX0l10w1WnmDvQWK81cye_F5T1HbJCMAp1WSW59ylvJGKbcpJzRGuyZs2E96VxCb_ARaps32zyl4fQCmQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
📷
نخستین تصاویر از بوئینگ‌های ۷۷۷ که به‌تازگی وارد ایران شده‌اند
🔹
چند فروند هواپیمای بوئینگ ۷۷۷-۳۰۰ER (مدل دوربرد و پرفروش) که از عربستان وارد شده‌اند به ایران رسیده‌اند. این هواپیماها به‌خاطر مصرف سوخت بهینه و برد بلند، از مدل‌های مهم پروازهای بین‌المللی هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666856" target="_blank">📅 11:07 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666855">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7pAsrVSjoDlTIhol-zODEohoZEfm9SfoZuLBg4OUx3SCZBGoALj3RnJmKH39naNnVDLXL-7n1gA9xGu1XnG0Vm8sLzqg96sd0xTVKfkKcq7AUmxagOyqpP4NlmbAo8o-qDjMlbH_YOawQk8dDx1O0jKZGNxoHgAL5Zo6rqRPoj0UoU3sH0GjHIr95hoaDx8zxtFEGqz40L2Y878kVNZXYW0F7vZTLAw46NOY10YdfOO0hM2oeWfC6AmXrNoOWUrfeLhbCeUzFWhtppxBHJ98GBarfDqE3T4FOaHbaV-DKHEVQB5lBvUbLaL3AyWZkink2zZPCJA8ORASLvXQXOVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور رییس کل بانک مرکزی در آیین اقامه نماز بر پیکر رهبر شهید انقلاب و خانواده ایشان در مصلی تهران
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666855" target="_blank">📅 11:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666854">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62a7352771.mp4?token=g5HjOwoOGyFn_4TUcnomkAlOdZRWMz33C029xwezyvuQlawUP2DPXX8luZYQ8NU1jrFurTYys-MO3AW6u6vF97g-cYEj6Dy6MmnRhgE_MGKtYfikM4OPX8GmmkTlsVcphZ407IfdeWRGWjx-xlu7XUu0fZXJgb9Y36kbVVNfywrXQS8MHK5jBokbjUvPwZksMzjFfUmQgntF1DvXfO6itoY_K-CVKDKFm6oawxhO_Nkw_Nsz9151ctxRCLkZ4V-PA2YVjv5WLYEkgfcdxHCY6aMpS5u5MJ7x0fTLXYTuvkoV6LzvnKqSdXqkjYk2eDV0RV6jG8oBws19uDpCH8oXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62a7352771.mp4?token=g5HjOwoOGyFn_4TUcnomkAlOdZRWMz33C029xwezyvuQlawUP2DPXX8luZYQ8NU1jrFurTYys-MO3AW6u6vF97g-cYEj6Dy6MmnRhgE_MGKtYfikM4OPX8GmmkTlsVcphZ407IfdeWRGWjx-xlu7XUu0fZXJgb9Y36kbVVNfywrXQS8MHK5jBokbjUvPwZksMzjFfUmQgntF1DvXfO6itoY_K-CVKDKFm6oawxhO_Nkw_Nsz9151ctxRCLkZ4V-PA2YVjv5WLYEkgfcdxHCY6aMpS5u5MJ7x0fTLXYTuvkoV6LzvnKqSdXqkjYk2eDV0RV6jG8oBws19uDpCH8oXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انیمشین لگویی وداع با رهبر شهید انقلاب!
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666854" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666853">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
مردم برای حضور در مراسم تشییع امام شهید نگران تامین سوخت خودرو نباشند
سخنگوی صنف جایگاه های سوخت کشور:
🔹
تمامی فعالین به صورت شبانه روزی در تلاشند و تامین و توزیع پایدار سوخت در سراسر کشور برای حضور مردم در مراسم تشییع رهبرشهید جریان دارد و مردم نگران سوخت خودرو نباشند.
🔹
توصیه اصلی ما این است که کارت سوخت شخصی همراه داشته باشند و قبل از حدود ۲۰۰ کیلومتری استانی که تشییع برگزار می‌شود خصوصا تهران، از پر بودن باک خودرو اطمینان حاصل کنند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666853" target="_blank">📅 11:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666852">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=Dv5ZcWnhuwOlWIur81_veGLDKn3y0s-xxnbPTiEhwkaJMgBuuY-fgiC5tFNbmHhYqpwOtS6-vOgiwUvAnaeLzb9kMK7Zal2b06Q9z44C8wkwVbehrZDUJ8FSAGnbpzrX9CxkGT_-EFD0Lhsm1LtQ4S23SNZ0E56xBgtFU8Vhj4A_IoIIz59XyLb8LSUgSeHhi8mOwUHoVPdZd8trYWF34h_5EwhSmsoAVFIoQDAqPlMlMcWiSMd8vJlsvUbYktXF7zOkhCdGXLE22p_k7oDNfb1WQdThtCHTN4jK3M_vQaYch77k85JmS7v_Jg8QX8BYxG9DB-GdetoRYxIB4gLEcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa11f8e93a.mp4?token=Dv5ZcWnhuwOlWIur81_veGLDKn3y0s-xxnbPTiEhwkaJMgBuuY-fgiC5tFNbmHhYqpwOtS6-vOgiwUvAnaeLzb9kMK7Zal2b06Q9z44C8wkwVbehrZDUJ8FSAGnbpzrX9CxkGT_-EFD0Lhsm1LtQ4S23SNZ0E56xBgtFU8Vhj4A_IoIIz59XyLb8LSUgSeHhi8mOwUHoVPdZd8trYWF34h_5EwhSmsoAVFIoQDAqPlMlMcWiSMd8vJlsvUbYktXF7zOkhCdGXLE22p_k7oDNfb1WQdThtCHTN4jK3M_vQaYch77k85JmS7v_Jg8QX8BYxG9DB-GdetoRYxIB4gLEcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نخستین تصاویر هوایی از حضور باشکوه و گسترده مردم و اقامه نماز بر پیکر مطهر رهبر شهید انقلاب و خانواده ایشان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666852" target="_blank">📅 11:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666851">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fe81201fc.mp4?token=F3TazMHN9BclN7HX55ZE7tfvavC0zsmYVWkpIgg9-HzC37oejjIyTfQf2yv5E4sgyK9cK09ubgne_nrCX5tLOVG0_x0c-xbQ3XikIQnM_8-C8NyhjNdHEHe-a1rfYgAsTBG1d8Uk8E-MzJRPaJ3Fvjec_s_bJThyTocCcIiKICTVHT3hEKRY3BHj-gQ1E0WHPLbwtjoEgSCB_QLoHyjjTuXpg63hoYdvH_pRUfJQFBfUm2WD7l__5rmAvWaZbe2sItd1Kc988AkoJgoqV2-wsEiRVGk8JKzNy-bPCF-kMMqzIbdaGk7HptTaLXmeDm9hmowpRpvcpnGhi6-7ajvGFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fe81201fc.mp4?token=F3TazMHN9BclN7HX55ZE7tfvavC0zsmYVWkpIgg9-HzC37oejjIyTfQf2yv5E4sgyK9cK09ubgne_nrCX5tLOVG0_x0c-xbQ3XikIQnM_8-C8NyhjNdHEHe-a1rfYgAsTBG1d8Uk8E-MzJRPaJ3Fvjec_s_bJThyTocCcIiKICTVHT3hEKRY3BHj-gQ1E0WHPLbwtjoEgSCB_QLoHyjjTuXpg63hoYdvH_pRUfJQFBfUm2WD7l__5rmAvWaZbe2sItd1Kc988AkoJgoqV2-wsEiRVGk8JKzNy-bPCF-kMMqzIbdaGk7HptTaLXmeDm9hmowpRpvcpnGhi6-7ajvGFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خداحافظ ای مظلوم جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666851" target="_blank">📅 10:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666850">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b188edccc0.mp4?token=FeVUG66MqFslCm7UlulxZuptNrZbPQ96SP6Mr4qAuSHjBRcLaDhpTLZkzC76FxhBnRbPIaYxp4W3gl64QGJjjNTBU2g0CjR9eZARnEg-SvNtjIC7CT0ht7ZNGtLlGBTswBnNTmWQFmjDB_lVFEMWVqdgNrABlBLNl58-26oIDRIB5n0tjCwMlBfao9_ZPlwQxLGOmlwQU0v_kJWP01DPc6cMaT0d5HiD8TlbafNeRoRNWwft60_BTW7HNQsPmAB0nmPWr3BY9b1c2uCk69DtzzCZgmGkJEaoZw2aPArneEnDNZgA6CKoc1LuHYJBW3bnF_pcidCn84vKQN80Qb-K3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b188edccc0.mp4?token=FeVUG66MqFslCm7UlulxZuptNrZbPQ96SP6Mr4qAuSHjBRcLaDhpTLZkzC76FxhBnRbPIaYxp4W3gl64QGJjjNTBU2g0CjR9eZARnEg-SvNtjIC7CT0ht7ZNGtLlGBTswBnNTmWQFmjDB_lVFEMWVqdgNrABlBLNl58-26oIDRIB5n0tjCwMlBfao9_ZPlwQxLGOmlwQU0v_kJWP01DPc6cMaT0d5HiD8TlbafNeRoRNWwft60_BTW7HNQsPmAB0nmPWr3BY9b1c2uCk69DtzzCZgmGkJEaoZw2aPArneEnDNZgA6CKoc1LuHYJBW3bnF_pcidCn84vKQN80Qb-K3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب اقامه نماز بر پیکر رهبر شهید در رسانه‌های عربی
🔹
شبکه العربی با پخش تصاویر زنده از تهران، از ادامه حضور گسترده مردم در مصلای امام خمینی(ره) برای شرکت در مراسم تشییع و اقامه نماز بر پیکر رهبر شهید خبر داد و حضور پیوسته مردم را برجسته کرد.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666850" target="_blank">📅 10:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666849">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسوگواره بدرقه یار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSePMGwO54K2p4nEEm9-m9oih23UVxC8FDvVSXUpS_KEf-Rz74TPzTaZDS8jUtfYoojBj4zuVVI5F8-bKOVPOp0nI5yGof0bnFa4_jMzkFUDO7K19zqJXWsXP3C9DEOnS3bFpj8-QTDgDMo1yBo9Eegx8HcP6Hlh4oZY2d1vzWOvZjPpnDgeFJdHL6mtJUE_njP-8KLA27HYaPWTm_0GiYB84XuYuku-gRiyzoqnBXVG8IrSO33zA-hVU4X3svMyh0d9Z_h4YsLOmzZMPv2dzN7bRFMFOWBawTrMUI4Cw6QmfWJ-eCVqIdy5bf2DkvTbt9wAFeomP5a-l1LYvhMyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوگواره بدرقه یار
▪️
از تمامی هنرمندان، عکاسان، اصحاب رسانه و تولیدکنندگان محتوای داخلی و بین‌المللی دعوت می‌شود تا با ارسال آثار و تولیدات رسانه‌ای خود با موضوع تشییع رهبر شهید انقلاب در داخل و خارج از کشور در سوگواره رسانه‌ای خبرفوری با عنوان «بدرقه یار» شرکت نمایند.
📌
بخش‌های سوگواره:
• گزارش ویدئویی
• عکس
• نماهنگ
• لوگو تایپ
• پوستر
• نقاشی دیجیتال
• داستان کوتاه
• تیتر، خبر، مصاحبه
• آثار هوش مصنوعی (در دو بخش پوستر و انیمیشن)
📌
شرایط شرکت:
• هر شرکت‌کننده می‌تواند حداکثر ۳ اثر در هر بخش با موضوع تشییع رهبر شهید انقلاب به دبیرخانه ستاد رسانه‌ای تشییع رهبر شهید انقلاب در هلدینگ خبر فوری ارسال کنند.
▪️
به برگزیدگان هر بخش، جوایز ارزنده‌ و یادبود
#بدرقه_یار
اهدا خواهد شد.
📅
مهلت ارسال آثار: تا ۲۵ تیرماه ۱۴۰۵
📩
آثار خود را از طریق آیدی
@Badraghe_yar
در تمام پیام‌رسان‌ها ارسال کنید
برای کسب اطلاعات بیشتر به کانال رسمی سوگواره در تمامی پیام رسان‌ها مراجعه کنید
#بدرقه_یار
@Badragheyar</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666849" target="_blank">📅 10:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666848">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAETXP9OHhIqpMF5zQFLZ_PjDDJZ2_J7danbjKQX8MFbF3N5XVT5ocjklzSgyT3APaC4MjOLwbXwdMM6DM8RtWucMAyMOMPc-Q8_AqrSwT6H9x1QQTzKAAxsZoL8gQB0AaYf3dozb3kGRwTlINZGbcJUjFaw-t-HA-awxiuK756UJRiS7ihDQNSnHPiKvmvcbrBsWg7-kGH9q3XFnp0eV4I2WBvSecEU8KIhjqwYnkW1e0yR0xj5k3XPIsuT1JhByerqX39OBHYSGEmfGYGZbdk9dMmyC7ZDhOazzEXVp3AlrymbemBlFnhWckjpcYF1CyFxQZQhlsDKkSruRbasvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سیر صعودی شیرهای اطلس طی ۱۶ سال در رنکینگ فیفا/ از رده ۷۰ تا رتبه ششم!
#جام_تایم۲۶
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/666848" target="_blank">📅 10:50 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666847">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
میدل‌ایست‌ای: تهران از موضع یک پیروز سخن می‌گوید، نه صرفاً یک عزادار
میدل‌ایست‌ای:
🔹
تلاوت آیات منتخب قرآن در مراسم تشییع رهبر شهید ایران، متناسب با هر یک از هیئت‌های حاضر، این پیام را منتقل می‌کرد که تهران از موضع یک پیروز سخن می‌گوید، نه صرفاً یک عزادار.
🔹
ایران از این فرصت بهره گرفت تا به متحدانش اطمینان دهد که تهران تسلیم نشده است
🔹
همچنین ایران با چنین اقدامی به قدرت‌های بزرگ پیام داد که ساختار قدرتش همچنان پابرجاست؛ و به رقبای خود یادآوری کرد که اقدامات آنان را فراموش نخواهد کرد./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/akhbarefori/666847" target="_blank">📅 10:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666846">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148e57d0a.mp4?token=FI4aGREornwmGOGwGXtS629yjlfJxazd8em7-p8Glgbjh6WSrArnKl7R0z16Tl7_MYOcQxM5jFbpejUGTZAmrKev816IfHCNYVf6WUjWue6pscQanS2c8gani2BlVaFXZAnaL8vRr1slnJVjwV28XPQOrvgxtmDoyleqM36xukhXn3OOYTfkF-oORZjN1jY4hwOTUKiH6efMCHlapZnyb8wfAFyup_ZSuq6oFgPA6LMEFpBhSjGqHbarlyvKACjMmgziwdn2vE_S-peSFOSM3MvyVeZhb8XMBj3vY0wDYFr-i6vGBfL1AM5_HGihgCuJeZsi3GeEs9kDdG4-9wkoEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148e57d0a.mp4?token=FI4aGREornwmGOGwGXtS629yjlfJxazd8em7-p8Glgbjh6WSrArnKl7R0z16Tl7_MYOcQxM5jFbpejUGTZAmrKev816IfHCNYVf6WUjWue6pscQanS2c8gani2BlVaFXZAnaL8vRr1slnJVjwV28XPQOrvgxtmDoyleqM36xukhXn3OOYTfkF-oORZjN1jY4hwOTUKiH6efMCHlapZnyb8wfAFyup_ZSuq6oFgPA6LMEFpBhSjGqHbarlyvKACjMmgziwdn2vE_S-peSFOSM3MvyVeZhb8XMBj3vY0wDYFr-i6vGBfL1AM5_HGihgCuJeZsi3GeEs9kDdG4-9wkoEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عزاداری مادربزرگ ۱۱۰ ساله در عزای رهبر شهید انقلاب در مصلای تهران
#بدرقه_یار
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666846" target="_blank">📅 10:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666845">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNN6vBG0rNC77pZ9NNSdJiw_LTt1ez_NoS5NrokJFyu6wWqYEv15Ze9k6Kn8YQFVmvMmZ6ExCK2nD2EP41A8AkWblIrMQr4m3173lKthYJopsKu5WQ70zyVGFGtXyKRnr6AR_UQ1IrdyTdtAcEWzWa41rxK6LGuYbSg5bgbLDv-g-DjpjhkpD6tdcznfNnCmaVtHy9zjax8O2Qruw_D2O8owfAcRSdb7rQzeA8WAg4Fav3QhsSYqTK4ofngg9ljOdIDInFTM7oLOTnAHDuJQrZnWwOcMNiZz849HbwgTjzjKbBU0psztKlZFzMMgcFS4VVwThlMpC94xn0sFFfeWLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویری متفاوت از لورن استرله عکاس اتریشی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/akhbarefori/666845" target="_blank">📅 10:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666834">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kee9XCCrR6ca0NEZkqCMWDkCzUVgF19bHrJ8r_Q0FVroPvvmyZyBy0qEwmHYGbuwP0CC6-_hhyZMm2cvzoRNz8lQ_ib5KKG-GhHI-bYonoCy-U7YhEoGu1nMZKzP-6Y7sXQGYWoDyGgpP4vdCS-sHBCGpN6ZSgsNpiNpgjIJElCPLRibnpSInzBxbCwvVU_E9tmsw-61sPHEsq3osQ9pkCvVqbQEJznON4XYJyvhzrO34guBpM-lxr5pds369Cd6qgl3v88kEAdYrXvxJKuduMv8Gee-lVuNX94m2LC0-UYOvtqvZTWPyHU5CKOZ7lKXGpJ-LiMRaN1XgdX9idHotQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gbyAb-q5nANLpIegJDAI8lGTO_XIt7Miui-ngrVOzMB58TRA1fQeVoEiyVE-oUwF2TYNKPK-kSo3h-Fo-EXU2L5vJP-wOyoaoleQnuJVZJKp_cCfqheKtLBEQbvvESYTDnXHxHXCvY4jjAfELg2EBj6TMyqvOLfOLusB_zoIjUj1kc17LwQOVKJ3NZ7llBUDxGoxWgT7hA4Rv60KzmKXkbxUoh5lHkjO8H8ckkcljOmlgCh-QkkS-IPpLRGUQfkRmnNf_UJ_Yol9Mb8Zx-R4CvxtNNQEhjW6IS1NYVqa1Tw5m4wov5SpCxgApcD9-mbaIXJAPNSuvrauDEHaN1xPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HTHcDYuGSsVxeBGQec95aoVfBn1F1QIoPKS66entG60QDvzeJvKHtgQBdH59nKXYqZdA0tqtO8ySSs4nOMDDMJji40JddgPWBiQyfsaEeBxGvM2gtt5N3CFnZXPXBgPPcvBbLKCOcYnU2g-DLbXH5rl8FjJABs4BwrUT9Og9eg8xXbUpAdM8hJehTXsJUL243Ty2kjmXrtq_AAmbhXuyN1htQtVVmSxDj4xQgkBA49_0z6txH6CXKFeMR6XDWPpMsQ3-utYa9jtiP0cSJQYnYt_WuPtis5E0E2MplHB6X-L-VHn4AkgyJm9lLpTY2WAY2cMdMMKFHI3IDYLg3ROnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qhhJjkPdsl9l6FQ1BSD9ZfCb6pIAqMkvGPfWKuYunZTZcdRhntRxn_DaxdGqCZ5PEQlO4PNwyGcdHtoHzfveNoqmAS8lDGASreFa_W5efIZFFwwmbP1yeznryY2YK0K19r9X-toFRP13I_MtZ-FLyz0tHBqi57_zK1mbNXy9j94ugJByrNtT9SoZPCZQhcy-szpnnCiQVEAlTBDmHK9DMNVrl6ZZqpP0EmOyHQC3oTIMYSeDmIAfoB9Dn-vE-mKOu1-qa68Km7F0jellFA8dUDMjgMuNek-atYGPXAz4a-Gx2HqjQ7xLrKe4WUVwPXaQtp0u5YbwLA5sC0lcPhXF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L5pvB6t-5uqKiK5-x32O3cCUKrXZ1msvkaPpAGeVKn9-k7rg8VdvnMV-5e7HujjAkcsyOA6ExKTB5StVpZIMVwowr6Qb1YUmSURFV0vnQjLy4Y0j5CtVdqP_CLNQO11QJCBmro-O1XCGIJBcvEkhxmAn8gu8wut80cZs9STKkmtxRTQmAOPE5mzJl4FACkCJaDpFPhgD98gFok_xc4ZHUjFTfWrH5qV25oosUbb2Ry77Xh_HiNxJGpGmNBil7yvS3_5DzLtyJbDrnwxgRGYxGRSXUtgawFO1ImKACXTE3Nf9qfDNa1MWKPuv-2fZ-vqv20Td1vTl9XOrt705eKApNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E2fa8i9oKKDuFB4aSEsH9oafAREzMHeegPQeKE_Uu9tiJyN-FoMxOIqs26-j6TBOV5VvUu7aALGsscNG3NPPzEfZux9D0Y7ps80kVVexmZvFoZJ2I7vCQOCyO01vhANlvMSsX8y5RMrgdfzgR59aW1uegw5FY3CvD5sio0_4UfF-yQkJa46ZVKdbceTGTz5toMLpJPaKaOoz-n9ThjiGymzDI6T74Bn2xVDoTXBRHQOSNAWBuabnLDp0bc3BIuW0TlotLTopHz9xJ-fPodZ_c-tZ10kudHc_aIElVuUdL97ScsBPMosgZ4Qr398a078FOsarI-eiIrlGvdJanWw4TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JhjVMhnVTAE1CjPxf00uvgiqFIaiUD6aBAB6jW4htRvgEkEbsDggUwJA377K-aVmw1FZ5L7kAR96qTSoKDggEnU90v5FmAEeLSqv0jxe1jlMIQ28ewjrn1nt6eoAJfEXJ41-dilAlwMnWQcZe79U1tQvK6SR1eRGIbz-QDfjpakUSxuBtlBsyrZE3WQaPNctHCI_R631zxSk-oDYYa0kwiu122NzHN98erVt6sHvu6hZBjJxcZZYHh2OHizmSotD__PKVWzAJbVXLyIyg1eG9i-RTrS42KyRNHvI8_nh3-Pxm5VIDxoQXY3uALk92BYWjDzVSJ9V83ZSVxOQ76CpEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fBLCxu4LgBtfTVlHEgV_eICxr7rcTXl8n62luhiXC6_wUjB_12ZYeGA1fCbLAGG9WpRosSyQ9apTETA95treDBaBcO6YqIzYNVBJFln0gIb6ixEsMBGsxgDPpDtv3l-kIrMwOnFbWunvbE3KNNOiXtgpY62b04nD0Jf9ZJmfFAt9hBRAvwP2fZrjnQ_t8RDp4dTxtKo6osX6SFWY4aGtXJMXrG3BoRW-UtRxcLuRQqZOhsztoF9HxJXPUIBNuX9eUm-P03Mwtf184dmRguSClL30dYruK-fLQrTXzYDcV-OIfzjDdE1uU9K5GJelM6cluKo8OBCYrxWFJKj--G9FYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/adOGqM1PzYftls2HMN5a9lXGvaLJn3GyUixgLM86tIB9_7nh9Fe08FLWS5jRWats3zvMTuLNKy7WcrZMw7NxLJVnRNPeeFaonh4gZHL7_i0e-1AlGH5ZqUKmyCEWeGwszgH9OdR2mSpUtqinj8Hm_Kf1FdOlFMbw5oYbkA1bggsDYWO9Em16_jJ1VHk2aRuE83kJLjkJRyTbfsX6A3fq_CHpGyWOv1sTcyF0aoYRTxPy7mVahQ2r8m9kDUZwf7HV6_h4Ni-gJRxCx_N7Jaw_01U9yAD4bmWdWg-H9rTfLE9Ug920zD-lHJXV3pgjo9TVytbggvOlpBIPYcKblxr-Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WqyNQERpLaIrUy-QmzQ-I2aw61VpUVpWPdr2Upn_hwPeBBmu_TsMkhgSEskFPUi03GU_no_ZTUy4GBPyqX3DpfdQj85jSutnB5AGtvPBd3huCD7JQNcwxLZJCujcPP6dnrm2WGP140ChXq3n7-lLpLUj6eJ22VPYl5EEbn3ukj7hvlSbo2guEpv5UwRdYI9LbY7dginiEsfNgnatI8Ro1gDiFvXK_bMc_oxxlz3EEnKKL4CGCp7i2U7OG3TAdkVYotv_uyYB0rfMKlVcWz0ICS5YI6qXH-Dxsp4HQLz7UlXT86eoESr_-BIs680pGWnioUz8lob7bube42nnWTKeNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سر از دست دادیم
سرور از دست دادیم
تو علی بودی پس
پدر از دست دادیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666834" target="_blank">📅 10:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666833">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
مصباحی‌مقدم: آیت‌الله سیدمجتبی‌ خامنه‌ای معتمد رهبری در امر نیروهای‌ مسلح و منطقه بودند
عضو مجمع تشخیص مصلحت نظام:
🔹
آیت‌الله سید مجتبی خامنه‌ای معتمد حضرت آقا در مسائل مربوط به نیروهای مسلح بودند و بخشی از ارتباط حضرت آقا با نیروهای مسلح از طریق آقا مجتبی بود. ایشان همچنین معتمد رهبری در ارتباط با مسائل منطقه بودند و رابطه حاج قاسم با حضرت آقا از طریق ایشان بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666833" target="_blank">📅 10:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666832">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ffc7fe130.mp4?token=Y_RCfXIR9Nr9zTSb4_fszRkqYciYy9ZOxcroemEekg7vLec7H4UQcdehSlwYfzWdkmkkPE-XGcGfsfekjF_fnm96nosX_l8yg1-ssIxYEMLfo8YuRhb5yMWYGVwkjfhi9c9Y_ZMo9WkdyBsK829r-PgVjCqlM8_cpjQFkVb5_lQ61RUsU47XNLULqTq_Rp106GVllhitC7QbK7nPYV-wNUtnGuAIgAd4NnSLaa8oJqXDzpqxqae-kpOTArNztwX0Dl9NeKt2vPLVqalryxnCyMEHO5ff9EVuqhaB7W8Gj-oLcl-l60gFSxhwjgdlSC3rC1tEDzhj6zSiaIbtUbpBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ffc7fe130.mp4?token=Y_RCfXIR9Nr9zTSb4_fszRkqYciYy9ZOxcroemEekg7vLec7H4UQcdehSlwYfzWdkmkkPE-XGcGfsfekjF_fnm96nosX_l8yg1-ssIxYEMLfo8YuRhb5yMWYGVwkjfhi9c9Y_ZMo9WkdyBsK829r-PgVjCqlM8_cpjQFkVb5_lQ61RUsU47XNLULqTq_Rp106GVllhitC7QbK7nPYV-wNUtnGuAIgAd4NnSLaa8oJqXDzpqxqae-kpOTArNztwX0Dl9NeKt2vPLVqalryxnCyMEHO5ff9EVuqhaB7W8Gj-oLcl-l60gFSxhwjgdlSC3rC1tEDzhj6zSiaIbtUbpBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سید هادی خامنه‌ای: آقا مجتبی در طول مدت مسئولیت پدر، تمام مراحل را دیده و تجربه کرده است
سید هادی خامنه‌ای برادر رهبر شهید در مورد آیت‌الله سید مجتبی خامنه‌ای رهبر انقلاب :
🔹
ایشان تربیت‌شده پدرش است و تحصیلات قابل قبولی دارد. در طول مدت مسئولیت پدر، تمام مراحل را دیده و تجربه کرده و همین سرمایه بسیار خوبی است./ جماران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/666832" target="_blank">📅 10:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666831">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLTbS_lURaetwsdHbc3tQOY3XrZ-iLYH0u6yxGiYFpJcAcTNZIJk4zqxqn694HAAdCw3tPzW2d7lz7aqpOOKRkYiXTLZTKHkLFNxRG-qWpVpFM4rlS5z23_oJXHtrcrChtUbFREH6GHpdHPFlKt01xHd-gVhTwlMB9YyQNEHm_R0oS5Jg727d9a0RfPg9sBdPaSBQzDsNs8xhz1fz0UtRriXbqQBhso-aa9LaR7NvfdWxhSUMWd-Qghf7z-pxgVHhj0lG_bnSozwN6wB1ghjbN4YtvFi2h9PZ_g9qemmL3txE4dqXLupDRoi0dPXow7JRppKoUmkAyQuCpj_f6P7uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یاد شهدای مظلوم مدرسه میناب در حاشیه مراسم وداع با رهبر شهید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666831" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666830">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6625ee5382.mp4?token=GlvqiEv_m7DmoORPxUcODYpqqixxsUgy4Qb4xmDNPqJLrt45BSZ1XfhA8zIBOqfoOw7yJC1CPRLPSypjAsqRpVjFsa0GrJi8BtnXmhdlipkx3KkCXd7B-No-hB9PU30oPBu25BnhexQIz01yLmMNLvjOTBWMtvqQWeg12R4NDM3PI6f01SdUNL1ZWN-Go6aiTSLSEgb_5uqeQPiCfxmHopTtR66hucxwra5JyrNSPOEXfmi2VASaWR7Wi5bhu4GrNXQVkPtRGRbExT1ZOGTHtkDrQ-QuH0Y7NrkyicqV3jJEjiV2LzZ0xXpu-uZ8ZaYcayR96ThbWYNPSN9SXh9rbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6625ee5382.mp4?token=GlvqiEv_m7DmoORPxUcODYpqqixxsUgy4Qb4xmDNPqJLrt45BSZ1XfhA8zIBOqfoOw7yJC1CPRLPSypjAsqRpVjFsa0GrJi8BtnXmhdlipkx3KkCXd7B-No-hB9PU30oPBu25BnhexQIz01yLmMNLvjOTBWMtvqQWeg12R4NDM3PI6f01SdUNL1ZWN-Go6aiTSLSEgb_5uqeQPiCfxmHopTtR66hucxwra5JyrNSPOEXfmi2VASaWR7Wi5bhu4GrNXQVkPtRGRbExT1ZOGTHtkDrQ-QuH0Y7NrkyicqV3jJEjiV2LzZ0xXpu-uZ8ZaYcayR96ThbWYNPSN9SXh9rbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت یک فعال فضای مجازی: از شیراز اومده بودن، گفتم چه حالی داری عامو، غیظ کرد بهم که رهبرمون واسمون شهید شده ها
دست خالی داشتن دمام می‌زدند، با چوب پرچم و جعبه مخابرات
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/akhbarefori/666830" target="_blank">📅 10:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666829">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e33707719.mp4?token=G8qo8pzos83eOOlaCHcJI8EnQoz_ZdzLUKsk0zyaUNhtE59uMg3rt-U589wR1eBb0-dq6xxZQGgL8udAaHqKH1ufGY3ZXndVXeybQkEuwZjAiukuF0n-jjtfDA3JskY6lVrqCOu2FnBHBtL7kfkpdxE5dpHPjSJaN3TvKhid0L19VJpTPyAUlYCwpt9I7pzKhi1V-h-i-_AJBCJO5X4pU8Ze4HodyN6l-SbbkB9y1flpczVm5sVqsdQe9h_DujGs85X06TkTgo28gdq4_zHnUxS4TbtO-xQOUnhOJckqjelWoR3T0wzi8lmifbQ8ddkJtjbEnhuc8wv4lant_oZkjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e33707719.mp4?token=G8qo8pzos83eOOlaCHcJI8EnQoz_ZdzLUKsk0zyaUNhtE59uMg3rt-U589wR1eBb0-dq6xxZQGgL8udAaHqKH1ufGY3ZXndVXeybQkEuwZjAiukuF0n-jjtfDA3JskY6lVrqCOu2FnBHBtL7kfkpdxE5dpHPjSJaN3TvKhid0L19VJpTPyAUlYCwpt9I7pzKhi1V-h-i-_AJBCJO5X4pU8Ze4HodyN6l-SbbkB9y1flpczVm5sVqsdQe9h_DujGs85X06TkTgo28gdq4_zHnUxS4TbtO-xQOUnhOJckqjelWoR3T0wzi8lmifbQ8ddkJtjbEnhuc8wv4lant_oZkjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اللَّهُمَّ إِنَّا لَا نَعْلَمُ مِنْهُ إِلَّا خَیْرا
خدایا! ما جز خوبی از او ندیدیم..
.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666829" target="_blank">📅 10:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666828">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/akhbarefori/666828" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تو می‌روی دامن‌کشان، جان از جهانم می‌رود...
من خود به چشمِ خویشتن، دیدم که جانم می‌رود...
پشتِ سر تشییعِ تو، روح و روانم می‌رود...
🥀
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/666828" target="_blank">📅 10:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666827">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec20bf810f.mp4?token=Fz1Z0zu6oRtxkjeghe5BpS3dY_XQwySL-U0NombObkfZaVoUSq_z5rfznM2UWbJ4s47B7yJ_3XXJdJc7DqZzZIuCIbEDi8MtrRQLWI8bd6-abDvzkxDNOTnYjnzmk2ExKtH5oEjz_DqahIVKtjD1WvGY1xQZ3SQsixyAPyUVsw99B1YZ0stKzBm5OWJVXA2oqm1mryP77fGgWeGjh_ZMvYVgNdZpSt4N4EVAk1bNDmvsjeeoBzuwvTpRUO69NxdgPnySrrX9QxIJEDvTmd-U-ayqTa68PtO-AOdLgZ6axLy8MED3NSzr7txNYcRPRv4UWfIhAM7husZz2H8WQqwzIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec20bf810f.mp4?token=Fz1Z0zu6oRtxkjeghe5BpS3dY_XQwySL-U0NombObkfZaVoUSq_z5rfznM2UWbJ4s47B7yJ_3XXJdJc7DqZzZIuCIbEDi8MtrRQLWI8bd6-abDvzkxDNOTnYjnzmk2ExKtH5oEjz_DqahIVKtjD1WvGY1xQZ3SQsixyAPyUVsw99B1YZ0stKzBm5OWJVXA2oqm1mryP77fGgWeGjh_ZMvYVgNdZpSt4N4EVAk1bNDmvsjeeoBzuwvTpRUO69NxdgPnySrrX9QxIJEDvTmd-U-ayqTa68PtO-AOdLgZ6axLy8MED3NSzr7txNYcRPRv4UWfIhAM7husZz2H8WQqwzIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اتوبان شهید سلیمانی همچنان مملو از جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666827" target="_blank">📅 10:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666826">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
همونی که براش نمردیم، آخر سر فدای ما شد
🔹
همخوانی محمدحسین پویانفر و حسین طاهری در مراسم وداع با رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/666826" target="_blank">📅 10:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666824">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
واکنش مقام اسرائیلی به تشییع پیکر رهبر شهید: ترامپ نمی‌داند با چه کسی روبروست
یکی از مقامات پیشین شاباک رژیم صهیونیستی:
🔹
مراسم بزرگ تشییع رهبر (شهید) ایران، قدرت این کشور را نشان می‌دهد. رئیس جمهور آمریکا واقعا نمی‌فهمد با چه کسی روبرو است و علیرغم تجربه اخیرش در خاورمیانه، در مسیر اشتباهی حرکت می‌کند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/666824" target="_blank">📅 09:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666823">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjus8hvUqYEUaMslfKEv-ZoGi8lkeCixlmpe2on5TwE9QsckjdK3q3dttcc63JLAwvHkHHtg8NvmqZVUnwit2bF7_mthSsS9KVI3bQX2Rvs-Q2uooBwEAzRgwcsKXnWApNML-5_jtpYrXPJ8lNvy_Dj9R-LHKyf_0VKzaRzW57vqC3kcd05oXd5f7NA1uPBb5EGMxoiHWPCVeDkCOhwazFjog4ZClp2zsl1WQqIJZjVNdDsxsEYaw-WFK5Y5WQN__N9b4-ZUPoirnx6trO9QNXhPEb9qMew0fsnmvTAeFhg2kD4wsFF8BREAlnAA5UpQjHaJl9gK0z0YIcOcB12ACA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اقامه نماز بر پیکر رهبر شهید انقلاب روی آنتن شبکه‌های خبری پاکستان به صورت زنده پخش شد
همه شبکه‌های تلویزیونی پاکستان با پخش زنده مراسم تاریخی اقامه نماز بر پیکر قائد شهید، گزارش دادند که میلیون‌ها ایرانی در بدرقه رهبر خود حضور دارند و همه آنان روحیه‌ای قوی برای گرفتن انتقام خون شهدای جنگ تحمیلی آمریکایی-صهیونیستی دارند.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/666823" target="_blank">📅 09:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666822">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oniv3SpQdc0chsTZ-bPqF1Ilh3zO0tAxDWkzxP9mdEtQ7x9QB5oxbWKBnE0P5S5jFOWPERUxdzmfd1hV6Be05kk1ifCYf0QmHmPBeX9Ws2El_GRMWV3i9s2Caj7_gGlrF5FkFpxiWJAZKpTyCncJnqKRE0HiostaomiAEg55O8i6f1w1IpQ-CKrHiBNJ3t9MfozQbkpDC01ykL9NOpT_5CTF27sodE6nIMJel_WAVu3qf7yOdoZCkdJ0QpqdyTnjSQKRc1ipjV4v9ew3eOjjDP2kizcKY4hUen3Gq9J5RmLtAcQGLmBI_nOpSql1cSgUELwtkj4B25PM3zP_QG3eLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری به مناسبت مراسم تشییع رهبر شهید؛ پویش مچ‌بند سرخ
🔹
مخاطبان عزیز خبرفوری، برای شرکت در این فراخوان کافی است با یک مچ‌بند سرخ در مراسم تشییع حاضر شوید و تصویری از حضور خود با مچ بند سرخ را با ما به اشتراک بگذارید.
🔹
مچ‌بند سرخ، پارچه‌ای به رنگ خون و نمادی از عهد، وفاداری و خون‌خواهی امام‌ شهید است.
🔹
بیایید در مراسم تشییع با مچ‌بندهای سرخ حاضر شویم تا پیام ایستادگی، حق‌طلبی و عدالت‌خواهی را به نمایش بگذاریم؛ پیامی که نشان می‌دهد یاد شهیدان زنده است و جنایت و ترور از حافظه امت اسلامی پاک نخواهد شد و همواره خون شهیدان خود را مطالبه می‌کند.
🔸
تصاویر خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/akhbarefori/666822" target="_blank">📅 09:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666820">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cuyj078mdqklgD7NVmPXo3DyIQlYOOhnr4wlcY1lUkHl-olr594mObV0KH7ZxNkHVfNfIUpzHLGyGAh1FrYC4ppN_2kBcFdABETZhWR71S5-YVBKiVEPuQPZ8VfZi0T2_6pZwE2uQPrwGHtgdLt_rD-lh6gl4YmzjmNonJYrwwWMVuMwlhrw7swSnu_uVF8l7JMcxTwM9yOWf7prv9pHPISk1KtFTGMAibPUQwv89bRCs8ZOj-wgHDtchYBUX6GIQ7c44tV5H2luiSPnN8JAdvExrlNKDa_lLQdMWIXim6ymceVzMfwPjCV9Tj5yP4iJj26ehjXtXVfTUMEXrNTwlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سی‌ان‌ان: دومین روز تشییع رهبر شهید با حضور گسترده مردم
سی‌ان‌ان:
🔹
همزمان با طلوع آفتاب در تهران، دومین روز مراسم عمومی تشییع رهبر شهید جمهوری اسلامی ایران با حضور هزاران نفر از عزاداران در مصلای امام خمینی(ره) آغاز شد.
🔹
آیین اقامه نماز از نخستین ساعات بامداد به وقت محلی در مصلای امام خمینی(ره) آغاز شد؛ مکانی که پیکر رهبر شهید از روز شنبه برای وداع عمومی در آن قرار گرفته است.
🔹
تصاویر منتشرشده از محل مراسم نشان می‌دهد که از نخستین ساعات صبح، هزاران نفر در اطراف مصلی گرد آمده بودند تا آخرین ادای احترام خود را به پیکر رهبر شهید انجام دهند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/666820" target="_blank">📅 09:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666819">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd70fd41e2.mp4?token=gaOiyeKbm6OxtKcLa1oY_eg-oTZiVs7AAtl1qH8ITVZkQm562bS5lVxLr6H2zMiJcd792pk27zQcjcM_RCXJ3Q9watwrb8VDZ9ldsfKAAZJIPIMujMwRbtzT496N0ne-xkPvsyUEeCuLzzvjLZARxMh6XSGqJDLacj5i5qUdnB-8jjsAfwg_SSG4c88gaOy_D1h6BbTutUy0-5_6DdVHJv2wt3LQzDNhX8LRpQar-aaiVpxM9GBRxaeF2kej80s2zGGWqcUC9tp4NiIE8tQUlZhPmDbq_3uwJdvzpzOM9cH3pDansGluchFJ6ZcFF7qxj_FNJpJrmId7UeJmFbFNUVRuHPKTG0QkvTU-fmLfSygZN7XqOrRzNs28pe3OGjCaBWJ0sl9-mZNfNy4kUZxuZ3GPP8R9mgAGa5-4gg4Xvz6jdFkuJfuPnPs9-UB8hqU6hZ5q0vwRXvQPlIHZX2TyR_skQW8Tc8dqx6N_1Lw8MgVoHqaO3cPrxKtKubib6ZOpemCdhWCuZSnhxYxD75N9Oxi-eFDC-pKP8rk6D0izA8S_E4uCP73uQxGkJG5ecYREJSmd4n8qaB5nK6k5_ppiXHdpgSfUOUa7La9KAXJb90FXAeV2WbWzew6QryvmeTk7RrgdZCMDiDtGQyKafVz40NrIIf4SPUXBAxSyC9wdrpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd70fd41e2.mp4?token=gaOiyeKbm6OxtKcLa1oY_eg-oTZiVs7AAtl1qH8ITVZkQm562bS5lVxLr6H2zMiJcd792pk27zQcjcM_RCXJ3Q9watwrb8VDZ9ldsfKAAZJIPIMujMwRbtzT496N0ne-xkPvsyUEeCuLzzvjLZARxMh6XSGqJDLacj5i5qUdnB-8jjsAfwg_SSG4c88gaOy_D1h6BbTutUy0-5_6DdVHJv2wt3LQzDNhX8LRpQar-aaiVpxM9GBRxaeF2kej80s2zGGWqcUC9tp4NiIE8tQUlZhPmDbq_3uwJdvzpzOM9cH3pDansGluchFJ6ZcFF7qxj_FNJpJrmId7UeJmFbFNUVRuHPKTG0QkvTU-fmLfSygZN7XqOrRzNs28pe3OGjCaBWJ0sl9-mZNfNy4kUZxuZ3GPP8R9mgAGa5-4gg4Xvz6jdFkuJfuPnPs9-UB8hqU6hZ5q0vwRXvQPlIHZX2TyR_skQW8Tc8dqx6N_1Lw8MgVoHqaO3cPrxKtKubib6ZOpemCdhWCuZSnhxYxD75N9Oxi-eFDC-pKP8rk6D0izA8S_E4uCP73uQxGkJG5ecYREJSmd4n8qaB5nK6k5_ppiXHdpgSfUOUa7La9KAXJb90FXAeV2WbWzew6QryvmeTk7RrgdZCMDiDtGQyKafVz40NrIIf4SPUXBAxSyC9wdrpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گزارش رسانه عراقی از حضور میلیون‌ها ایرانی در مراسم وداع و تشییع رهبر شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/666819" target="_blank">📅 09:37 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666815">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6acf0490b7.mp4?token=arvF0bSS1n2KCWNtmrf29LBFZWNVGyQzQzh97w6OqXqc9UmW7gGgLz6XPHRTR2SXYCBUu6V6KaWchvEDTDLd4YTPpBfjKrXM-qARRnKWzcS4JOJG3Rs782T4FNuarvuuERW6uSJ31CscvYGOL3sl5jsfpAy7_zUiGjLNIq9x1N7YuS-PbSzA5NxEKkODcIQ-S3Ilh_OxijRCk50V4CrXA5nJiT_noMzmcV3FKgO-5afRRGI9dSaAG-0_MDrLcRP3-_teXlsDy2bdQImD2xlC-mFeGY2u-3TX2wGASDnJ77ZxM95HkURe1t0Awd5QXfqnyLbW_Dijd9nSk7TWT_9J-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6acf0490b7.mp4?token=arvF0bSS1n2KCWNtmrf29LBFZWNVGyQzQzh97w6OqXqc9UmW7gGgLz6XPHRTR2SXYCBUu6V6KaWchvEDTDLd4YTPpBfjKrXM-qARRnKWzcS4JOJG3Rs782T4FNuarvuuERW6uSJ31CscvYGOL3sl5jsfpAy7_zUiGjLNIq9x1N7YuS-PbSzA5NxEKkODcIQ-S3Ilh_OxijRCk50V4CrXA5nJiT_noMzmcV3FKgO-5afRRGI9dSaAG-0_MDrLcRP3-_teXlsDy2bdQImD2xlC-mFeGY2u-3TX2wGASDnJ77ZxM95HkURe1t0Awd5QXfqnyLbW_Dijd9nSk7TWT_9J-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سر از دست دادیم، سرور از دست دادیم
🔹
نوحه خوانی مداحان در مصلی امام خمینی(ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/666815" target="_blank">📅 09:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666813">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce3be48ad.mp4?token=gR3MM5URpG6aZuixLy5VdeBfx4K9Z232ueQQHZZI_BlWED8Pnzt5HAURIsPxsHnbaeqxNo2yzj9k-TpbKsGNyqE7Qv0APm_Dm3pNjli2xhgKkYufb3o_Pu4IBkEKXdHH_lvLu_1GKfX3HwCyjcG8O-cNgCw8SljCGioZSDf8xSUeGFNCXIqgmL0ZmRtPwrciguvG_-uAusCStNQ1mqwR-lIkcNgsK9i7QL3lVzBqbJnbNiNb5X6uSGts-pKEA3_Vu84TkvE4WJImuyBU0HYVYOKgU9BiLve68qVB3DZdBGB1wfdajkZdbbw0VmDzhkZe8wl3vHHCtDbDKmAzaZ9yOUuHW4XOCmKKamdrCeiJt7_1Oe-k6K5XVqlbx5q689HdMbamY0mqVRLHMfR3dAMea7vA52JzJy6W4Sqw9Sj7URGbumnaxucF3RMjJNwRsElO9dPLHH0hGmk-uiM8FfsgT3wea807I_VvbK0oOcBRMOj9WsPbPvCAunFO4Kr0kK6wP7udT4WZ2eUzspy-1A4ovLmtHwVzZABP-xgRpDCMC_KWpGBQjmed-pH0Lb0pio1zn1cv4RNn0rmYZT3-brbnVBIMbqExFeXCDHNL6ddW6axyevJHHE2Mri1nJCrX_xE63PwKPModRZXAVtXA7XCgIRPfXz496KnRLMHngMUPTvU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce3be48ad.mp4?token=gR3MM5URpG6aZuixLy5VdeBfx4K9Z232ueQQHZZI_BlWED8Pnzt5HAURIsPxsHnbaeqxNo2yzj9k-TpbKsGNyqE7Qv0APm_Dm3pNjli2xhgKkYufb3o_Pu4IBkEKXdHH_lvLu_1GKfX3HwCyjcG8O-cNgCw8SljCGioZSDf8xSUeGFNCXIqgmL0ZmRtPwrciguvG_-uAusCStNQ1mqwR-lIkcNgsK9i7QL3lVzBqbJnbNiNb5X6uSGts-pKEA3_Vu84TkvE4WJImuyBU0HYVYOKgU9BiLve68qVB3DZdBGB1wfdajkZdbbw0VmDzhkZe8wl3vHHCtDbDKmAzaZ9yOUuHW4XOCmKKamdrCeiJt7_1Oe-k6K5XVqlbx5q689HdMbamY0mqVRLHMfR3dAMea7vA52JzJy6W4Sqw9Sj7URGbumnaxucF3RMjJNwRsElO9dPLHH0hGmk-uiM8FfsgT3wea807I_VvbK0oOcBRMOj9WsPbPvCAunFO4Kr0kK6wP7udT4WZ2eUzspy-1A4ovLmtHwVzZABP-xgRpDCMC_KWpGBQjmed-pH0Lb0pio1zn1cv4RNn0rmYZT3-brbnVBIMbqExFeXCDHNL6ddW6axyevJHHE2Mri1nJCrX_xE63PwKPModRZXAVtXA7XCgIRPfXz496KnRLMHngMUPTvU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازتاب اقامه نماز بر پیکر مطهر شهدا در شبکه‌ المنار
/ تسنیم
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/666813" target="_blank">📅 09:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666812">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
بیش از ۷ میلیون سفر با مترو تا صبح امروز برای حضور در مراسم وداع با امام شهید
🔹
همزمان با برگزاری مراسم وداع با رهبر شهید انقلاب از ساعت ۵:۳۰ دیروز تا ساعت ۷ صبح امروز ۷ میلیون و ۱۴۱ هزار و ۲۱۲ سفر در شبکه مترو ثبت شده است. مراسم وداع با امام شهید در مصلی امام خمینی (ره) تا ساعت ۲۰ امشب دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/666812" target="_blank">📅 09:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666805">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JzKHpieF_O39BJNidqQdhfdaXdyUXxQ2hObybuGC1_Y4W7pDGeKvQtiP18aqygmJM6VAEYoX8FiSqtF686q_z9Sy3jrQwzfGETrAo2yoEfxWEZkpVQ8ZLMerCATZ38ZtsxEXQpY7p3G65dETBLRuJy1gdLwjV-pcZTR0ILb5G7eNS17N5QHNNjkXCsBQ2tcZydWkmlNcPiMz5WqlC6Dh2I7FyWjILA00G30EkEpiDy9QWsljXDyZWTyPddHHBztCcq0arQRncMnW8lumDt0GBSX35DoksN1m8Er7GwWy3wrJdzd_L0hnzqmgFkFGwmsNQug3e7IN7dBFBi7q19-XbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ltPIrzLPpi3cGxFNqkn_H1N-DtEEgeR8wInCSR1XIP9Od5lIaKTYP-C2UfS7zkG1L1XcXNeT0hMYSTuvmWPhaLDCz_gK7macsLUPFkvzta0PDc5BBRTcqFvKkLooKmV-gZc01FQbok0YwgQKDi5Oe--BYWPCzH8J8JEOjZ92VJp1e_SPceLvyUzjbWFokDq5Oi7TS9BP-zGacrQMI-9qTAPWYryJQj89rMTwZ1a1ArffuAYpi3CWNPxGzue1phOxLNbziNpDYYfSeOpLqgyE-g3JlwkM5H9CYS53d1YpljV3YojIlYKcB_fpGGfUW5kGBBJMCH5K0V6k59eP1Q0ugw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jeMGnfQCxrr036Umogz3cUK0ROMDkoXcNb16LX7ws9HlkfrROQ-Q3wLr9Kq5q9u72KnAhWpglHWbElpR849Tfy0YagAxIV43Y8B2nbYM4md_1TRNLT2KNMmfj9UPozgypJ2Co0Iwz2xMACTVSxCi9EkpToLqUBF2pmLVDc0hmxu0cvG9wNanB_HmH3zQvSCF5v75WCI7Qiq2oEsuHtu6jvV7CcCGzaqLrJiWr5STivHmr0svlLRmxKQmXhi982KcFiLpaIXOs_91eCj4tF-VT9XRiBGr4AFF8DFPUJ1HlwaZDMyjc9liVwZBaN6ck3ti4gRsPY_Mn_xEu677lnBSOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RWiRJsVpEU_W4pJW3c2QQSRG2YxJel8M-_kh6WbkZIa2GKVnO4s9L93RVLpJrRzLhVceQV15QvEshmxb8nHaArGP2_7o7vuxChul_BFCIW6aT4TCuYhEsEFEfu9WDJ5VSNwjkOvAMhhx4NpBkqORGLo3j_ik0g8mJ-Pl2e9OWIQgPZjHaha2_FyZCG1FWpWEGbAqrICDsPNyobO29s1r5qWjKRpXEO6dDwO-Fmse-nc_Um6mqRlVWLrr8SfFtGFukgP04Ta9AXHQFzYSBxUX6a2Oplmk3JZyoQTWWNnWMxYV2nUnSiWKP3cb_NsyipoJSLF-BnG-W0-KR_7QMND_6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rv0tyiy5jsW5YzSq5MN6UwgCJI0qHFfHrRc7BW7ec4Lw1RImybS7CnKqwjJ2tvyNzVxbi0LYsaWoXOWJf7GPuE9zMW2ZX3TgHkXZX82qTpW1D0OPPHQODcKtStvd43sUcxRma9ihxsn_oh1gHEllif5xr1QzTWd_vV4Sj8YTNJ5Md45IKleBQDs7vH04B9ScNvfe8eyjQ1HcxaHSXE--Sx1iSvpxSDAgoc8hxfk58ISACHCnM4W0PDzXvbqNgspYVERd84WtRJiRGEH-VNiodL7fNBiioCJBRii0e4058KiIb2VHTme5L2vsBlDBloKoUn4eAS2Vh6qDRgZ-zmHY7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gVyKwDtEi4yrB08Qhtmz2tifaH_z5Vn_zkJj_75wcut801zdAHGv4alWGKYxWfX69ibywY7x74dM3VNh4lUG5UbURhBkKzKVotKtp9q3-Dxi3cATu0M2uPJrF9XynYbxRRq_NetZkdgGCo2qk863HTnPxkB0IcXxxo4uIZC_86Y_jQLUtFfspfafFwvrKWTuX0jmDEv-RtXMXPX5WL0hFkl4ezny0Aa-xDT1agmk4NemQ5iUFd-7W7vKqg0prTZFxfGyhHSO0SWb7kRoJP76UL-agJKmbgAZD6z1w0yrO8U_IWwmR8YDli2a4soXlHIdoRDCXHQJNgSlEIEXcmD4vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d36ae94c32.mp4?token=iBgrTQ_V2VW3znrMSbUXFojCYemy0x6wm8UTpylJ3hnN85rgyuIxdRzUFaBwzm-31ukXJxeymIkykW2Hnd-tF4cJui36mEk5dp08S7aqoh527SB2Kg2JMuidf20hosfljDLdXTMM5WlJE5afqtrUbBe_7EIFuheqxq7H9Kt1WtaouBKjaPEk5k_-woQAvzYi8LTLn4B7Nevm9UlyKWt-od0QFT77l35Hdhr983-WZ2kUqSli5l7xnWyt1ddr_EIo6p4fc7wX6XCg2KO7wAAJSj8EHUR7hsyDsEIwVdPF1bFKrxuPbwXYj-aXiY6h46Cwf3eaLyP3DAM1sWG_dxr1gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d36ae94c32.mp4?token=iBgrTQ_V2VW3znrMSbUXFojCYemy0x6wm8UTpylJ3hnN85rgyuIxdRzUFaBwzm-31ukXJxeymIkykW2Hnd-tF4cJui36mEk5dp08S7aqoh527SB2Kg2JMuidf20hosfljDLdXTMM5WlJE5afqtrUbBe_7EIFuheqxq7H9Kt1WtaouBKjaPEk5k_-woQAvzYi8LTLn4B7Nevm9UlyKWt-od0QFT77l35Hdhr983-WZ2kUqSli5l7xnWyt1ddr_EIo6p4fc7wX6XCg2KO7wAAJSj8EHUR7hsyDsEIwVdPF1bFKrxuPbwXYj-aXiY6h46Cwf3eaLyP3DAM1sWG_dxr1gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر اختصاصی خبرفوری از آیین وداع با پیکر رهبر شهید در مصلی تهران
🔹
عکاس: سمانه صالحی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/akhbarefori/666805" target="_blank">📅 09:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666804">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mf4ob46WLyIQY5a1GUudcoIJwLW_aRfKcd_IldcMZggbOgt33y2G1eHKHZPyqkjktjYudV9Jn1DSAhm66xdE2xtSQWhnKvPgySNbHlJrlydlBEPffvAZTdBDJ9c86rea4JQ7HoPUU9LpS7ahUrZytAKAmUkcuNj55_KZ9NnSXwWGiC0BO9-Pkv7Em3XmameEr7EDIUnATrD1aCfbre-e52rVP2_IndnPH2vTX60i2-8oPNesMnZVGltEzJiJ_ZGv7rTLKOg5TXwWxrFwKTk1_cgF_Ufd6LBqFMMp2LOEeJ7VobEVabI-bMpEBkIZeaEJoz1BPt9k-b9vSb_60ti4Qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هم‌اکنون| تصویری از خیابان‌های اطراف مصلی تهران
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/666804" target="_blank">📅 08:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666803">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I5fxf3L9gBXECNkEg_31pwxXRmw165OQw41sdo8DKsXAMDTmNLn8nCZva-UMuSpgaKjoJRMLzEMRzD558MMY0YgioenmKSuof9sSAWdgqULVEamCDLIdUScjN_M5BDYxj5GLZKODFcAF2GSo7n6oDPotCP3UxnBYkIkz0aUfSRnGdWebN-3RZeujs202w4QQFv7x2Q3wUvo321k0j31lPnB-3vFJdiNrtq4Kvgs5IYfi0ttGLyfgLVUfW6klucyhUdDLiVqGX0gmbG_6Q8smyriIZdmzjsnlyJ_RxfbiF5qrCsJyrlQ3V1K_8Ino-Pj5z_1Xa7faM8IoRNlpPlqJEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پلاکارد‌ یکی از شرکت‌کنندگان در مراسم وداع با رهبر شهید: « اماما؛ پس از شهادتت، ما هم خانواده شهید شدیم»
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/666803" target="_blank">📅 08:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666802">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37305e26ab.mp4?token=kd8X-TYEYnLsLPFx-n2YRFosZkUIJDLkh5SAvBQH3C5qh8ZZyu2REnDswTVBrRlxAetSkhjA6uEiYN4TBhrZymJw_EN8ka4KwuRzSiiU0sD6k1pF2Va1U8yEDjgXFdRSIBWfp610zXy2C-qL_jnuwBqwKIC8jNc-FfqewozqjjHDYKfdam25ULohRNB_5v_ODiMyjFna2OMtR5GCLeR61NAaOJFvm9OrTKb2bbmbzYMza4wAV15l6nNR62xNHEa73mgW6MYti25ySWuU_rj8jiFBTkD9pP3-w-ANCdyEM2gQBv61Z1wzdIKrMWV08qOuFkUzlgyHKV8LX0g-iUw6VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37305e26ab.mp4?token=kd8X-TYEYnLsLPFx-n2YRFosZkUIJDLkh5SAvBQH3C5qh8ZZyu2REnDswTVBrRlxAetSkhjA6uEiYN4TBhrZymJw_EN8ka4KwuRzSiiU0sD6k1pF2Va1U8yEDjgXFdRSIBWfp610zXy2C-qL_jnuwBqwKIC8jNc-FfqewozqjjHDYKfdam25ULohRNB_5v_ODiMyjFna2OMtR5GCLeR61NAaOJFvm9OrTKb2bbmbzYMza4wAV15l6nNR62xNHEa73mgW6MYti25ySWuU_rj8jiFBTkD9pP3-w-ANCdyEM2gQBv61Z1wzdIKrMWV08qOuFkUzlgyHKV8LX0g-iUw6VTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ای غیور ما، سید علی صبور ما، خدانگهدار
🔹
لحظاتی از شعرخوانی مهدی رسولی در مصلای امام خمینی(ره) تهران.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/666802" target="_blank">📅 08:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666801">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHR-cPM-GRMorHgimJb1oP0fNWhwK2GFtVL7lAHNrTkvNDSsVev9ISNXZ9l_ygo6Yu1KSR1cqeqglLZK7Q-Fp81HGHOYk3WU31Et9-q1sla9ig_Fda-qEZ0zohXt67FjfyDcgLg5H775ycmgPcuPIOiWiw0MkXfR1rn7peVuUobcOyPfFdBEBnapM5__RV-NEHKbQ-Y45fF6-5yOXsXHMZ1NhPQqcqjTwZ85S5Jlse4HTe78Ta45VbPXhspqf7m_qDHMhD88WlbQnUWySxeoSZrTcCTV48KY4NVoX4WODNoI7YDXwismwiQTslSgMHfVpHddtwCw6Bu34k2vvxtXKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استاد سوئدی: ترور رهبر عالی ایران، حکومت این کشور را قدرتمندتر کرده است
آشوک سواین، استاد دانشگاه اوپسالایِ سوئد:
🔹
انتظار می‌رود نمایندگان بیش از ۱۰۰ کشور و ۲۰ میلیون ایرانی در مراسم تشییع پیکر رهبر عالی ایران شرکت کنند.
🔹
ترور غیرقانونی رهبر ایران توسط نتانیاهو و ترامپ، ایران را به یک قدرت بزرگ و حکومت ایران را قدرتمندتر و مشروع‌تر از همیشه کرده است./ تسنیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/666801" target="_blank">📅 08:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666799">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DfubpvhAs62rMh1gNsCfmZQw6qkFxBekm7iPXU_rUKojTs6wD3KOXpD7tx6r9Irl4jyl5-9hPM1kRnhhjIn05mIzY8ImTi3eEBBy9A5NNSV148U97sOBB8odspenpMS9dN-fjH4ypi_1evARHFDhk0ISbFH5lBvgYB_abAeOz1sVnLQL4L5uco4C3m-tVC_jmWHwP5894yI6nB3TceC1tIS9ups25wgXloZ6ZflGh9mqO-TJLFzh3IYBgU3WTWhBneu6iynFJ6GvIBKZe8wlfOkaV0S1_OVcypWjqszuHAuePUBZksVcqxkRkH2MiKaCQOUwmuFNTBDZAxo8gCObRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تلویزیون عربی: خیابان‌های اطراف مصلی نیز مملو از جمعیت است
🔹
جمعیت امروز بیشتر از دیروز است؛ خیابان‌های اطراف مصلی مملو از عزاداران شده که با شعار و پلاکارد خواستار انتقام خون رهبر شهید هستند.
🔹
پرچم‌های سرخ و محور مقاومت در کنار تجدید بیعت با انقلاب و رهبر جدید دیده می‌شود.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/666799" target="_blank">📅 08:33 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666794">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P-zqWwUVQQB9jzjhNg0fn_ibKBdpndxS_c9xLO5MRyM4jyLy_oPPCy8DeBxV2CJEDZZYfw-c9mBBPdG_YxjhzyAlFgH1mTflfv0wTrZnns-BS9Kj28jRb7ch_e68k2_MJV-1Nm6bMQhFNAOxY9Mxm6uuuFTvxm0oKA10A4a6bXOJdbeg9hMy_ewRslTETneLp1VGCofeaOnLas8gkGuSAzOvjbEyecOi_5P9QPzNyOOTPliSSS_sVhQBYu7tTSONORzxyFO5odx9Y7EjJjvIQW9_sRyEDuDGICnKg9_RaXqlLxBZeR89WBU0otBM-UFWjpfsQgyf7VLCSl7qeQZ9hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kw0RJXVPBwezlEDO60KUvOTO1jX5_MFcQ5GVKf3xKpVA-REz6M6RGji5t6Zgl-NImQzir2kaB6oLQ1WAgj6TiTS59awVvMMoI2N6IT5wmYKr86FIMfCSSDkhwCiVnaO0u9JF7IbBPztABZiMIcrdUPOW0tMbV6qqA7vx2mtl7Jvmh-K8FwY2Wi9aJZsXpB3OGwByL1JkPUwcI97ENmvih9MN-4Zump5WWnhJrIKRsF0t6jndLgVIoxA_cOHNNiXtdEAYLIaRT2PzNyE5rG-UBvp_0fCI1Nwijsz14m3BH9y1HhHog2SdctPPo0xc--G5rmZrhJ5O1m-2HJsZGSG3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5_D1JwQa2ZGSp_E3F8qVuHMqidrBI8VqLyFPzbddpo2U-iSfpUJvYupVZ85uFhS00ZYkeSiGekrqpMRBWK5gIacWRY1IL_oq1rkqGkfjl1UtUidTPma1VsSx8Pcc0cPBkrYAyB9gN--UP2Wj3JphMjdb4zibDstogUYHw6oY8W9YTqz9SN_oLqpXB07GTkizEj_MWdiBmkzRCtFXgtUPDPV0MoiGOaG6BG52IEIkVIILVc9srEqnWaXnbD6OyRJvE-7o8erp2Qlg_lfYvDY-rg4EAniWbonXsERKgEO8v0Y6jKUhKrpG4-99TcWTL1fBPtrx-GXMMzpyus4X3A1cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Oc6u4Om-s0qKa_XLQrBq-E884Ygcu__2uW1eF5sBMOmh3HLsJiw426DW9qgzwm584w4SS-A-FNC8IReg18LkhFkjpTxwOtEQxZXcLfsQlM86jJ9w5LHQfJEwKoLXK7XhXGw-5th4F-r0rFqnHMEXt1nDfe6IutpxwRPquXRupgVoWmL22CoIi7xYX_z4OsUcWb84OyfXILJl5S1JjYXBsUqHlRVWVars6-vpE7v2QIJANeUZmqQycPD9ZsIUe9k6LawYe_yktqOPRcg2CQeNJBluchqjqdmqhnvJgxetHiulMD-O0F6Del-ZqIMoXyvJCTWnDjAv3szXSl8PW0ur-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZnfruFPyTVZ3we8sNM0Sk5wBqOPIQIZYgqgUkihdzaSnEXd5TuMTx5aqj7zZfrjh7s9SUPlIlSrCE7ACiYwUJlvkZffi_hlItvLAgzZg0O1gKAGZzFcq0B5jphL-DsgPvVvzRIM7seNvxeq7wYkwBXz1Cra0x1_9eYH_87YMF8eA7sOBk-lw_7MJru6K9QFUWto_F-BRVh7vFgbFPFIG-aXv2-fIdlgLVOo2D40DcFGniZAABitIranU03mm6xi9ZJqswLLLmDkftOtf0hSmncVMR6WFP8fshOiwWjS5Vh-wb2BMkLcHUQ89Zhvrw-3cJjFomBQRRdEIXcfSD9qkBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
مراسم اقامه نماز بر پیکر آقای شهید ایران
🔹
تصاویر خبرنگار خبرفوری از اقامه نماز بر پیکر مطهر رهبر شهید و خانواده ایشان در مصلای امام خمینی (ره)
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/akhbarefori/666794" target="_blank">📅 08:32 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-666793">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7451993ab0.mp4?token=CuW4-7CFshGPF0o_OhHwwBjj1hhRaffASDEfVOdnVcw001PZcrkgrBhupeG9LAf7AYNPPGIh40sxs7PlsxlB5m1pPVtEqBr3wXgB8CTYDn9GBelIKuWCLkmddLBlSmhBOgLs81NqH_rw18126B6Wp_DchgAupUJ5CYcok8l4yszb4RsmIT-bWd11OZgE1VTwfmUgCn06Lh7Kg89jIiRNedBSLn7rjMDJza71Qmc507NPdRC5rizd9_m7kdzPwD9EUi8oMy91l3eKbGAZmppEFWk-_j10CqzhShekP9YWmFnj0KQbu4ef3iBl7DEw_Z3Ovz63kkIOvpjPALC3M6utDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7451993ab0.mp4?token=CuW4-7CFshGPF0o_OhHwwBjj1hhRaffASDEfVOdnVcw001PZcrkgrBhupeG9LAf7AYNPPGIh40sxs7PlsxlB5m1pPVtEqBr3wXgB8CTYDn9GBelIKuWCLkmddLBlSmhBOgLs81NqH_rw18126B6Wp_DchgAupUJ5CYcok8l4yszb4RsmIT-bWd11OZgE1VTwfmUgCn06Lh7Kg89jIiRNedBSLn7rjMDJza71Qmc507NPdRC5rizd9_m7kdzPwD9EUi8oMy91l3eKbGAZmppEFWk-_j10CqzhShekP9YWmFnj0KQbu4ef3iBl7DEw_Z3Ovz63kkIOvpjPALC3M6utDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اشک‌های مردم در فراق رهبر با مداحی حاج محمود کریمی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/666793" target="_blank">📅 08:27 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
