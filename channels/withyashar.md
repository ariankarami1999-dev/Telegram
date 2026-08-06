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
<img src="https://cdn4.telesco.pe/file/qhC7DGOhKx1GJPxUyQ7AGMq-2TqStP9D7Io1TgPE73D3sI7nhiV2RWXTEjm1kjwuO3sEwv0ikHxw6DKx0g4jTIt5T2N80Ok3a1G-nE33YFA0ThFJWvmansvqYN7_Zf800a-Fee9h_Z1oDzedbTMbNA8I6qfBGb5bYhsYRKM0qghYAo0uFSDkDCRCr7ZExtuvkCzENMhkk87inijm3PAPeypE3e_akUKJSrf6jwGCTeUyAejaD8ewry5xr1wRd2-0ov0lOkQExwTBwG7iog-78dA7Im7We-AijgnDy0jy0JvTyuD43gwlwm6s5KRgcsUIoWzmeQJDzBSGKa_PembK9A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 444K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیل📸instagram.com/yashar🐦x.com/yasharrapfa📺youtube.com/yasharrapfa⛑️paypal.com/paypalme/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 18:14:03</div>
<hr>

<div class="tg-post" id="msg-20574">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ان‌بی‌سی نیوز: پنتاگون جلسه اضطراری برای تأمین تسلیحات برگزار می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/withyashar/20574" target="_blank">📅 17:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20573">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حسین شریعتمداری نماینده ولی فقیه و مدیرمسئول روزنامه کیهان : باز شدن تنگه هرمز یعنی باز کردن راه فرار دشمن و از دست دادن یکی از مهم‌ترین اهرم‌های فشار جمهوری اسلامی.
@WarRoom</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/withyashar/20573" target="_blank">📅 17:06 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20572">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری رویترز : هنوز درباره نحوه اجرای «کنترل» ایران بر تنگه هرمز توافق نهایی حاصل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/withyashar/20572" target="_blank">📅 16:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20571">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54aca75746.mp4?token=pqLDaSQDjZHq8oO_EUhynJTOjdkc26zC-cwm_kTHBXjdlpShbotCJ5rBBNq9dmyfDjIXhXxjgIiv4hlG7cg8EjAU5ds4nOg16NfnWXYlmF5keeutYMrvvdmX7lOQpo1mgFUILyR9nw7Qnk_pYPNVZkNcGFntbgf6yL76-u26wdw7Pt_cynv-KjhaSfJjpiB-OLEYeUBviWk8gXw5uhqMtRB9FUWNdls5IGJgBNVCIWLUHQUK2W9YvO4_Ue3UehvVIb_upR-Zr_LkiJge39ixc9sEde0hjNqRzdfB3-RWAiHfwll2sGd2f6HecGGie3fvSetda8L67eRuiVVsRFesAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54aca75746.mp4?token=pqLDaSQDjZHq8oO_EUhynJTOjdkc26zC-cwm_kTHBXjdlpShbotCJ5rBBNq9dmyfDjIXhXxjgIiv4hlG7cg8EjAU5ds4nOg16NfnWXYlmF5keeutYMrvvdmX7lOQpo1mgFUILyR9nw7Qnk_pYPNVZkNcGFntbgf6yL76-u26wdw7Pt_cynv-KjhaSfJjpiB-OLEYeUBviWk8gXw5uhqMtRB9FUWNdls5IGJgBNVCIWLUHQUK2W9YvO4_Ue3UehvVIb_upR-Zr_LkiJge39ixc9sEde0hjNqRzdfB3-RWAiHfwll2sGd2f6HecGGie3fvSetda8L67eRuiVVsRFesAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مجری: آیا هنوز معتقدید که نوعی تغییر رژیم در ایران امکان‌پذیر است؟
‏مایک پمپئو: 100٪
@WarRoom</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/20571" target="_blank">📅 16:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20570">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">منابعی از گروه تروریستی حوثی های یمن به رسانه های رژیم اعلام کردند تا دقایقی دیگر، نیروهای مسلح ما با انتشار بیانیه‌ای از یک عملیات نظامی گسترده و ویژه خبر خواهند داد.
@WarRoom</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/withyashar/20570" target="_blank">📅 16:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20569">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کویت با استناد به امنیت ملی، دستور تعطیلی فوری تنها مدرسه خصوصی ایرانی خود را صادر کرد
@WarRoom</div>
<div class="tg-footer">👁️ 87.5K · <a href="https://t.me/withyashar/20569" target="_blank">📅 15:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20568">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b68ab7702.mp4?token=vqSSGvPrUvQ-ymRJsWOaY1SEZiC9NSMai9dTci-d4GH_QalsqovkzeHIcdtHyIG2BCI8BTjIaRE36iE11s6fXzi2ZI8eu1O065OAv5i-ruu3ViZo1FQ6qALWs9lNk5l1ClQH1JvPQLuCjDDTogK4J2AnTU9Uetbq6HyNS9QB8mBdcCc9rA7Zb6mwj9qp2GaodBVpTS1Apnf4rg0JWip-OfqHEXV7hDjLgvY-Crw5xqcEWp-dHgiqnBzLjpLlM4Jrv_aYnyuRC53me2X0GbSuxdRZ6xSL0x2lKGYB5Zj3_75l_22SyopbG-pyRHMeLvoby7R7iA8XIZUkwffH5ipRJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b68ab7702.mp4?token=vqSSGvPrUvQ-ymRJsWOaY1SEZiC9NSMai9dTci-d4GH_QalsqovkzeHIcdtHyIG2BCI8BTjIaRE36iE11s6fXzi2ZI8eu1O065OAv5i-ruu3ViZo1FQ6qALWs9lNk5l1ClQH1JvPQLuCjDDTogK4J2AnTU9Uetbq6HyNS9QB8mBdcCc9rA7Zb6mwj9qp2GaodBVpTS1Apnf4rg0JWip-OfqHEXV7hDjLgvY-Crw5xqcEWp-dHgiqnBzLjpLlM4Jrv_aYnyuRC53me2X0GbSuxdRZ6xSL0x2lKGYB5Zj3_75l_22SyopbG-pyRHMeLvoby7R7iA8XIZUkwffH5ipRJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مایک جانسون، رئیس جمهوری‌خواه مجلس نمایندگان آمریکا، گفت:
‏«ما در انتخابات میان‌دوره‌ای پیروز خواهیم شد؛ چه مسئله رژیم تروریستی جمهوری اسلامی را پیش از انتخابات حل کرده باشیم و چه نکرده باشیم.»
@WarRoom</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/20568" target="_blank">📅 15:07 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20567">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جروزالیم پست: اتهام جاسوسی به نفع ایران به دو زوج اهل عسقلان وارد شد.
این زوج، اقدام به تصویربرداری از مکان‌های حساس، از جمله بندر ایلات و کوه هرتزل کرده بودند و همچنین خانه‌های افراد امنیتی را تحت نظارت قرار داده بودند.
@WarRoom</div>
<div class="tg-footer">👁️ 100K · <a href="https://t.me/withyashar/20567" target="_blank">📅 14:32 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20566">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJyuyZJC4TpTPJpNRwXcampu38UQjYgOPBdLnzz8fGdwTvctyl9e4ciAzUXsDkxA502-1D71nlR7JDkMqiGgA4MWpw9c1IzINCFxetuBl1u_shOWb3gdZV8cAvxm69_Hvq1Qxv366IL-Yh8-fs2LpK3PwCwrDZhRmDvFmasEkt-Qcd2u2stLX1rYZrVyRJPS8f06KA4SNI8IzC0WUwvUMVFL1_NiVAeOfqmM8bXIcrglCf0LHGw3EIRDyDUwIGWbUvY9xOHXbRYZEW-zQQmBSazwn2obYBnsmuMmA9rkOXnvOGhT1NRuw4IcWoKJu_DtYsd4_vtAln_Zmh0S-qWhmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانال ۱۲ : نیروی هوایی ایالات متحده تخلیه بخشی از سوخت‌رسان‌ها در فرودگاه بن گوریون را آغاز کرده است
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20566" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20565">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حکومت ایران عوارض ۷٪ را بر تمام کشتی‌های تجاری عبوری از تنگه هرمز اعلام کرده است , این امر برای ایران ۳۸۵ میلیون دلار خالص روزانه یا بیش از ۱۰۰ میلیارد دلار خالص سالانه با حجم ترافیک پیش از جنگ ایجاد می‌کند
@WarRoom</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/20565" target="_blank">📅 14:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20564">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">کمیسر عالی حقوق بشر سازمان ملل می‌گوید ایران از ماه مارس حداقل ۵۶ نفر را اعدام کرده است - افزایش چشمگیری نسبت به ۱۵ مورد تخمینی در مدت مشابه سال گذشته.
@WarRoom</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/20564" target="_blank">📅 13:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20563">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏واشینگتن پست گزارش داد که دونالد ترامپ، رییس‌جمهوری آمریکا، در دیداری خصوصی با حامیان مالی خود گفته است: در نهایت، باید جی‌دی را انتخاب کنیم. این اظهارنظر نشانه‌ای از احتمال حمایت او از جی‌دی ونس در انتخابات ریاست‌جمهوری ۲۰۲۸ است.
@WarRoom</div>
<div class="tg-footer">👁️ 113K · <a href="https://t.me/withyashar/20563" target="_blank">📅 13:12 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20562">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند  @WarRoom
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20562" target="_blank">📅 12:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20561">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد @WarRoom</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/20561" target="_blank">📅 12:57 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20560">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حوثی های یمن موشک شلیک کردند
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/20560" target="_blank">📅 11:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20559">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یاشار : امروز سنای آمریکا قرار است ساعت
۱۰:۳۰ صبح به وقت شرق آمریکا
، برابر با
۱۸:۳۰ به وقت تهران
، درباره لایحه
CLARITY Act
رأی‌گیری کند. این لایحه با هدف ایجاد چارچوب قانونی شفاف برای بازار ارزهای دیجیتال تدوین شده و از مهم‌ترین قوانین تاریخ صنعت کریپتو به شمار می‌رود. در صورت تصویب، بسیاری از تحلیلگران انتظار دارند بیت‌کوین در کوتاه‌مدت بین
۳ تا ۸ درصد
رشد کند و آلت‌کوین‌ها نیز افزایش بیشتری را تجربه کنند. در صورت رد شدن، احتمال اصلاح
۵ تا ۱۰ درصدی
قیمت بیت‌کوین وجود دارد، هرچند شدت واکنش بازار به ادامه مذاکرات بستگی خواهد داشت. با توجه به وضعیت فعلی مذاکرات، احتمال پیشبرد این لایحه حدود
۵۵ تا ۶۵ درصد
و احتمال شکست آن
۳۵ تا ۴۵ درصد
برآورد می‌شود، اما هنوز اختلافات سیاسی بر سر برخی بندهای آن به‌طور کامل برطرف نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20559" target="_blank">📅 10:59 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20558">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZHgsDXZ4gIPvbtgbHAtvwKZuKfuhb52_bZbTGy85dJ7AN-Mwu-hCzaMlUsSPPWo1yLqS21wMN_SSQqeExRSvBKxaU3LTGsuA9GcU5kWq8EpkO-AZMDiX-PT16dYBTJ-CTPqz1Gd2CmBYnH3aEEuFeDIsjbzFJId-Q8QLXuGREneJ6wMqyJ6y-gqVTlLYJRGlXVyUL_omjpB6mI8I03d8a_TXlfZ8v8ms0JPtqWF_1j2b1PcReLXHAwS9u621_GcSWIlrD_r4I5REA9_tRd5SZK0sbtDyrVELvYMURXn6rb0qWNTPEbFt044mA6LsKksNkjlCmlUgf_-FTUS7WC99A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «افشاگران» این اظهارات…</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/20558" target="_blank">📅 10:03 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20557">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9S1anE1ldEHSXAgxxPINMjyGR00uvrWAMaD4boDMdNRwnSVLAPjZLITrWDFliIx2i8_DngI_FUlRf_aDhUVVmoD42joQUxpigL-jH_kDY0_1K_CEhopdtUUeBPrc-xee5Qez6Fm6CpHDYLehPUL82qYQ6tHDmDqHoIJraJaoIvl90MPWz56-HbQ_yG5qi5Kxapo3BTxd0vMyzzUN8_mtBwEOC4VlYx7-9sSv142ImNKF5Q5x5h4qxyRlgv3zqosvEy7OiOt42BsUkE85XLIyq0d9MJmlog4ZB5lZYr67OBWUh1JlDqK-pDwdMDP6l5yOFMCWTLesSiIlvZI9z4L6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجزیره: قیمت نفت در پی امیدها به توافق ایران و آمریکا در مورد تنگه هرمز، کاهش یافت بهای معاملات آتی نفت خام برنت با کاهش، به ۷۹ دلار و 2 سنت در هر بشکه رسید
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20557" target="_blank">📅 09:29 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20556">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFMLm-dJloEHsM5Vx0svCoAg16gku4piVSe54-kt2v1WJvKqohdqjqMOQvXL8c-rHIwX3HQW7n0sSDiOP54_MeFUGig4tJcmkMeWXunYfpCmsXRMAPah2_ZcPFNBzdkPmOfgJaVS-jgFpSHz7pImXev6tXaCIEoqTYUj02a2YVQavy6PUbFn4Str8mqvulFMl56pOFUteZL0HmRluBvo2AseFlyIO_e4gbaMsv4KOLbouOufMzYMde0LD7hMaHQcZLYoMSEhir5P8S0xAhSoWcHykU5SW3OkxMnpYAH4BEU6R5BkyIvDqVDpOzN5gLK0yrl8L-fwS6O71NIki2HEvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : ایالات متحده مقادیر عظیمی «مهمات»، به ویژه از انواع خاص، دارد. علاوه بر این، مقادیر زیادی از آنها در صورت نیاز تولید و به ما ارسال می‌شود. شرکت‌های دفاعی در حال ساخت بیشترین تعداد کارخانه و تأسیسات در تاریخ کشورمان هستند. «
افشاگران» این اظهارات خیانت‌آمیز تحت تعقیب هستند. احکام حبس طولانی مدت برایشان
درخواست خواهد شد!
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20556" target="_blank">📅 09:08 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20555">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=J5hhhBys4_mt6Pt5ddV72aTsc5WzA8gjEKvXg40ANyqpmZytorR9VbZRMJ-_nFHRLzrITF0e7X5zJnSKvcV_bILwbijOeLqD7Fqq9KrLGQZNLFDRgkRLFNMGU5uSQ9CFkJ08ucFnSTWUvjkKFr97Ew7MxbW1KgATe2UUJFlI9Usun9l04h4_haJR1R1eJ49gzfUa5pKZTZBwQlbZSXWFA3ZHtCMK7l_7icYbgZy-vnHztWhudmbL3WiVdGSKC20si03nOkH3kC1Oelu2DX0QIKh8m_GqniyyhE1hAyEgbY7STuqUWLa5o2DCQXZFEPC-ErX_6hV2WJOFKS0rOpqE-Ts6p1BcZSI-i7FyV1nZ04-KqZtKCpop9XLxSCqapUlwIlpRo9MbF6TSngvSknd8uNj2WIKM4KbG2jO7AFIJHUmCm7qfuzFL_2AiNtarf0SR8W__gxLpxjEcATkdn5W91G4bRDJvMcWOGMR_hg3dk0uJoI22HtSxclDKi7VSlk4ycJvfGLiPmRNE8jeRsYHNfMa37YKJl7ihD9-pu1KhoM-BBgJ1B2KfXyyV2w8iKRLVEU128nSGIALpcaTmEiQAREgYJO9vq4YCFgLwyXzGkphQWip16u-IL1VYpw22SdWTccnStKf89ZA71CFCvyuxrZN2iH-eSXIYXss70gQP16w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db57e2ad51.mp4?token=J5hhhBys4_mt6Pt5ddV72aTsc5WzA8gjEKvXg40ANyqpmZytorR9VbZRMJ-_nFHRLzrITF0e7X5zJnSKvcV_bILwbijOeLqD7Fqq9KrLGQZNLFDRgkRLFNMGU5uSQ9CFkJ08ucFnSTWUvjkKFr97Ew7MxbW1KgATe2UUJFlI9Usun9l04h4_haJR1R1eJ49gzfUa5pKZTZBwQlbZSXWFA3ZHtCMK7l_7icYbgZy-vnHztWhudmbL3WiVdGSKC20si03nOkH3kC1Oelu2DX0QIKh8m_GqniyyhE1hAyEgbY7STuqUWLa5o2DCQXZFEPC-ErX_6hV2WJOFKS0rOpqE-Ts6p1BcZSI-i7FyV1nZ04-KqZtKCpop9XLxSCqapUlwIlpRo9MbF6TSngvSknd8uNj2WIKM4KbG2jO7AFIJHUmCm7qfuzFL_2AiNtarf0SR8W__gxLpxjEcATkdn5W91G4bRDJvMcWOGMR_hg3dk0uJoI22HtSxclDKi7VSlk4ycJvfGLiPmRNE8jeRsYHNfMa37YKJl7ihD9-pu1KhoM-BBgJ1B2KfXyyV2w8iKRLVEU128nSGIALpcaTmEiQAREgYJO9vq4YCFgLwyXzGkphQWip16u-IL1VYpw22SdWTccnStKf89ZA71CFCvyuxrZN2iH-eSXIYXss70gQP16w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا : بر اساس این گزارش، فرمانده یک نفتکش در حال عبور از تنگه هرمز اعلام کرده است که در فاصله حدود ۹ مایل دریایی جنوب‌شرقی منطقه کُمزار عمان، صدای دو انفجار را شنیده است. @WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/20555" target="_blank">📅 07:58 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20554">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">جی دی  ونس : من با ترامپ در مورد ایران اختلاف نظر ندارم.
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20554" target="_blank">📅 07:42 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20553">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سناتور تام کاتن: «ارتش ما آماده است تا کار را تمام کند».
@WarRoom</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/20553" target="_blank">📅 07:40 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20552">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rAoPIWhtMq3xGDes_mKdiK_SSCLhJV3sm28Tw6wgUEgewBkB1zPNR7ukRm0h_dK3FaLWpvug3nbjaDxODjcUbXXP35enyxHaIJf__8ND4d8wYkeTelnQoYW9tXS9KBLdD8IBQsBQ8v3d4WjQ3Vy-KbnnVFNzE1gRWf-4sUxaH2Q0sHQjcyv3ZXwJp2jSPnT_Yxi9WQoNK28xR7NA2zbkjBSt-tug9qyawOhhf97pgd-dOoY6Dc5WNyHnurm7NtRe7PgUoLCJ3AsqkJjBepBLeqX0DtRB_M3spkMja2M71xbifgObYQuA8N9dLifZtaQsKTm0Gp9KkVjrczFm0LC1UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک @WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/20552" target="_blank">📅 07:36 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20551">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c627cc882.mp4?token=KUWcKBYKA5WX9Q1cia_7YmoFet6b5ZQWYULHmrUyt1lZEx48vkPSzBnWFJCVyExRah-uAfGP0TaNKs8gar1j50fIRotPfzC9tV44W166a3sfFbxgnHRp80JUnDO7lP_mTfrdAkj0-xbbSfKNI_6Fj68eGJLZywCn54U752rjD75kMfW57ldsH1i4kkJ1DrsHtEKu-yjXa2LxQ2EfRp6BJC4hZByTdXDB-wwrinrX6qjsdAYxacQyjvrWvjrscosIoFVteaUviFRl-5ZbKxqxzRirY8-VjjhSnnUx8fvxHucsxSixkYoTGvtIo_Bqcpk-5gb2b9jY_miSSLp0obr05A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c627cc882.mp4?token=KUWcKBYKA5WX9Q1cia_7YmoFet6b5ZQWYULHmrUyt1lZEx48vkPSzBnWFJCVyExRah-uAfGP0TaNKs8gar1j50fIRotPfzC9tV44W166a3sfFbxgnHRp80JUnDO7lP_mTfrdAkj0-xbbSfKNI_6Fj68eGJLZywCn54U752rjD75kMfW57ldsH1i4kkJ1DrsHtEKu-yjXa2LxQ2EfRp6BJC4hZByTdXDB-wwrinrX6qjsdAYxacQyjvrWvjrscosIoFVteaUviFRl-5ZbKxqxzRirY8-VjjhSnnUx8fvxHucsxSixkYoTGvtIo_Bqcpk-5gb2b9jY_miSSLp0obr05A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در مورد ایران:
ایران با من تماس گرفت. آنها بزرگترین حمله از زمان جنگ جهانی دوم را نمی‌خواستند.
ما گفتیم: "ترجیح می‌دهم این کار را به این شکل انجام دهم." من به دنبال کشتن مردم و نابودی کامل همه چیز نیستم. و این همان جایی بود که ما به سمت آن می‌رفتیم.
آنها می‌خواستند مذاکره کنند و ما در حال انجام این کار هستیم. و به نظر می‌رسد که این [مذاکره] کاملاً خوب پیش می‌رود.
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/20551" target="_blank">📅 07:27 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20550">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8609e5317a.mp4?token=IVDPK5WJ1dnEIXvgqnjgAYUMO9ProBHvCGjimW4qKRJswmlzQo_KjRmUx6DoFaGLAH73f_kloDoC6oFygz8gZsTYkPnKyySew-c3AVUz404jjTJ9vgctWtC6l7P5YolwaESkqr0j49lC3Ii07a2dA5U6KLf3bNHKZsfStNM3UchnM6UId0B9qHVGIg6pvJHmCkI6WkRxBMOqp71HOrlkJuOl27myI6wVeppE1eMBuz0DQO2_BREQaqCsk5vcVO7xK1yOrnoCJol-dVA-7dLpH4An6nc1OrLewlirDqLmUO45OUMDaA3UJTkex349q0Zbs4i8KqrThx-WlcUYCw_UCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8609e5317a.mp4?token=IVDPK5WJ1dnEIXvgqnjgAYUMO9ProBHvCGjimW4qKRJswmlzQo_KjRmUx6DoFaGLAH73f_kloDoC6oFygz8gZsTYkPnKyySew-c3AVUz404jjTJ9vgctWtC6l7P5YolwaESkqr0j49lC3Ii07a2dA5U6KLf3bNHKZsfStNM3UchnM6UId0B9qHVGIg6pvJHmCkI6WkRxBMOqp71HOrlkJuOl27myI6wVeppE1eMBuz0DQO2_BREQaqCsk5vcVO7xK1yOrnoCJol-dVA-7dLpH4An6nc1OrLewlirDqLmUO45OUMDaA3UJTkex349q0Zbs4i8KqrThx-WlcUYCw_UCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور ترامپ در مورد ایران:
ممکن است این بار با مذاکرات متفاوت باشد؛ ممکن است نباشد.
ما آماده حمله بودیم. در زندگی واقعی، آنها می‌دانند چه زمانی آماده حمله هستید و چه زمانی فقط بلوف می‌زنید.
و اگر مجبور باشیم، آماده حمله هستیم
@WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/20550" target="_blank">📅 07:24 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20549">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شبکه i24news درباره تنش‌ها با ایران: "وقتی بازدارندگی آمریکا تضعیف می‌شود، بازدارندگی اسرائیل نیز تضعیف می‌شود."
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/20549" target="_blank">📅 07:21 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20548">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9266609aa.mp4?token=WQWddLvOKAYVC3MoP2kqiNj6rDfYohNHGbasmQkoFCBh0rtKQZWRPxQlhDlU9nZDjjnrNh5k5Oiz5hFSO4PMB92_VEHMgtxCvfjCZAF-FfiPHHMD3Ah01cK2RCb37nL3GI_PG3ylwAr1cJLXXWdkeVSGFTR23KWpyz90o_ni5o3-wIlIWVL78bDe3RtiEcWVrCR8rXW8n7crGB0Cha1C0080dj2g1OrJ8jF3fz0J--0swRFlSubhYP1i3AbrB_8wdlmT40NersJGr4ig536hw6qL0wS02AYoee65mGNCNOfMBfT7ComA86pg2Z4xEeP4uhMxh2_IfXpzkHK6q3vM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9266609aa.mp4?token=WQWddLvOKAYVC3MoP2kqiNj6rDfYohNHGbasmQkoFCBh0rtKQZWRPxQlhDlU9nZDjjnrNh5k5Oiz5hFSO4PMB92_VEHMgtxCvfjCZAF-FfiPHHMD3Ah01cK2RCb37nL3GI_PG3ylwAr1cJLXXWdkeVSGFTR23KWpyz90o_ni5o3-wIlIWVL78bDe3RtiEcWVrCR8rXW8n7crGB0Cha1C0080dj2g1OrJ8jF3fz0J--0swRFlSubhYP1i3AbrB_8wdlmT40NersJGr4ig536hw6qL0wS02AYoee65mGNCNOfMBfT7ComA86pg2Z4xEeP4uhMxh2_IfXpzkHK6q3vM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ، درباره عبدال السید :
این آدم از یهودی‌ها متنفره. بعضیا می‌گن این حرف تنده، ولی نه؛ از یهودی‌ها و اسرائیل متنفره
عبدال السید! باورش می‌شه؟ فقط برای من همچین چیزی پیش میاد
عبدال السید ظاهرش محترمه، ولی آدم پر از نفرتیه
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20548" target="_blank">📅 07:19 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20547">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=TsMIcGYK7FhbU01xVYOA7fscmv2nAXiIDHznCjuSerEPwg3umsdYgSl7EcJnwA4Kd3sU8l9I7pLwV3jX58lcrJLUmOzUphJjy9RCqfy6XqnQYUEhFHTSWPKIiKGLJb27Xl9jne2y9mGW8qRkDQGnvVpACX7ndKvWr3RKQFuBFkdWgqVTV629PtpzUI89sGy2ClKEn730d3CkdZWpHSlS54Q84fweTTTC9NxCAkqQIk1N9M3p844kdtdBMfYAD0MYMX_Msv_G2PZzWwRWA1HJZmd37lQ0f70_djbg_DZuUOHRmXPzbegRg8eX9puKp6SqzugRuRFYyv2z-2A3XWCapg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4f4355b1.mp4?token=TsMIcGYK7FhbU01xVYOA7fscmv2nAXiIDHznCjuSerEPwg3umsdYgSl7EcJnwA4Kd3sU8l9I7pLwV3jX58lcrJLUmOzUphJjy9RCqfy6XqnQYUEhFHTSWPKIiKGLJb27Xl9jne2y9mGW8qRkDQGnvVpACX7ndKvWr3RKQFuBFkdWgqVTV629PtpzUI89sGy2ClKEn730d3CkdZWpHSlS54Q84fweTTTC9NxCAkqQIk1N9M3p844kdtdBMfYAD0MYMX_Msv_G2PZzWwRWA1HJZmd37lQ0f70_djbg_DZuUOHRmXPzbegRg8eX9puKp6SqzugRuRFYyv2z-2A3XWCapg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدال السید در انتخابات مقدماتی دموکرات‌ها برای کرسی سنای میشیگان پیروز شد. او در ماه نوامبر با مایک راجرز، نماینده پیشین جمهوری‌خواه، رقابت می‌کند و در صورت پیروزی، نخستین سناتور مسلمان تاریخ آمریکا خواهد شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/20547" target="_blank">📅 07:16 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20546">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">تگه دعوا شد
🚨
🚨
🚨
گزارش پرتاب موشک از‌ سیریک
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20546" target="_blank">📅 23:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20545">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">به گزارش رویترز، به نقل از ۵ منبع:
رژیم ایران به کشورهای خلیج فارس هشدار داده است که هرگونه حمله جدید آمریکا به خاک این کشور، منجر به انتقام‌جویی علیه زیرساخت‌های حیاتی انرژی در سراسر منطقه خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20545" target="_blank">📅 23:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20544">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی: «هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد. اگر آن‌ها…</div>
<div class="tg-footer">👁️ 168K · <a href="https://t.me/withyashar/20544" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20543">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20543" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20542">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20542" target="_blank">📅 22:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20541">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پزشکیان: حوادث دی‌ماه پارسال قابل فراموشی نیست؛ کسانی‌که کشته‌شدگان را 30-40 هزار نفر اعلام می‌کنند، نامرد و وطن‌فروش هستن
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20541" target="_blank">📅 22:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20540">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">نیروهای یمنی اعلام کردند که با استفاده از یک موشک بالستیک، یک تانکر نفتی به نام "دیزی" که متعلق به عربستان سعودی است، را در خلیج عدن مورد هدف قرار داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20540" target="_blank">📅 21:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20539">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">محسن کج بند : به عنوان یه سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن، چون ما داریم بعد از آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم؛ این شرایط گذاره
@WarRoom</div>
<div class="tg-footer">👁️ 167K · <a href="https://t.me/withyashar/20539" target="_blank">📅 21:26 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20538">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آکسیوس : دور جدید مذاکرات بین اسرائیل و لبنان که با میانجی‌گری ایالات متحده برگزار می‌شد، امروز ساعت 15:30 به وقت رم به پایان رسید. به دلیل تحولات میدانی، مذاکرات زودتر از موعد به پایان رسید، اما فردا صبح از سر گرفته خواهد شد.
بحث‌ها بر روی طیف وسیعی از مسائل سیاسی و نظامی متمرکز بود و بسیار سازنده بودند. تیم‌های فنی پیشرفت‌هایی در تعیین جزئیات کلیدی مربوط به اجرای چارچوب سه‌جانبه داشتند.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20538" target="_blank">📅 20:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20537">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">نبیل الحمر، مشاور رسانه‌ای پادشاه بحرین، مدعی شد پدافند هوایی این کشور در حال مقابله با حملات هوایی ایران است.
وی افزود که در ساعات گذشته چندین حمله هوایی ایران رهگیری و دفع شده است.
پیش‌تر نیز هم‌زمان با هشدار درباره احتمال حمله هوایی، آژیرهای خطر در بحرین به صدا درآمده بود.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20537" target="_blank">📅 19:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20536">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">منابع عربی از حملۀ موشکی به بحرین خبر می‌دهند.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20536" target="_blank">📅 19:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20535">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">نتانیاهو : ترامپ یکی از بزرگ‌ترین دوست‌های ماست،اما یه چیز رو روشن بگم، موجودیت اسرائیل قابل مذاکره نیست چه توافقی بشه چه نشه، هر کاری لازم باشه برای حفظ آینده‌مون انجام می‌دیم
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20535" target="_blank">📅 19:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20534">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">گزارش‌ها از حادثه امنیتی برای
بالگرد ترامپ در آسمان واشنگتن
رسانه‌های عبری گزارش دادند بالگرد دونالد ترامپ، روز گذشته هنگام حضور او در بالگرد، در آسمان واشنگتن درگیر یک حادثه ایمنی شد.
گفته شده در این حادثه هیچ‌کس آسیب ندید.
سازمان هوانوردی آمریکا در حال بررسی ابعاد این رویداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20534" target="_blank">📅 19:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20533">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20533" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20532">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19ce2c280b.mp4?token=BF-wpa7dkNY9nbsY6t5ZZCTrDR2xGNyprstAPdDYe-kOrm7aEEWQT4wbagI0tncNo8_HYHiA79_VN56RfVjTec2NifFV1ctaOZodukSdsSqFNlXQJu-b75bzbImYlUp80a9yniK78JUE366XrKbRGwenlPkfmr6_FE0yub_WY1GDwmbOsV_l7tTiJAUvyM5a1k9BLuC0pqPqOpnosZb7MvvVLpnDmNdmuIUXhaXnoKkjU0FbqX81w9b3QqmuHRTNHlvdvhfG7esMMiv8omk6gUxfbZ4Wf0sDHkUsSm2P3u9ZeETZiTXA8Lel6ln_4GduMDni60B9mJ1lcjYhZrvNJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19ce2c280b.mp4?token=BF-wpa7dkNY9nbsY6t5ZZCTrDR2xGNyprstAPdDYe-kOrm7aEEWQT4wbagI0tncNo8_HYHiA79_VN56RfVjTec2NifFV1ctaOZodukSdsSqFNlXQJu-b75bzbImYlUp80a9yniK78JUE366XrKbRGwenlPkfmr6_FE0yub_WY1GDwmbOsV_l7tTiJAUvyM5a1k9BLuC0pqPqOpnosZb7MvvVLpnDmNdmuIUXhaXnoKkjU0FbqX81w9b3QqmuHRTNHlvdvhfG7esMMiv8omk6gUxfbZ4Wf0sDHkUsSm2P3u9ZeETZiTXA8Lel6ln_4GduMDni60B9mJ1lcjYhZrvNJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل نتانیاهو در یک مراسم:
نیازهای سیاسی فوری این لحظه از من می‌خواهند که پیش از پایان این مراسم مهم ترک کنم.
ما در حال حاضر در میانه رویدادهای نظامی و سیاسی مهمی هستیم.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20532" target="_blank">📅 18:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20531">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سخنگوی وزارت خارجه درباره احتمال سفر قالیباف یا عراقچی به پاکستان یا قطر در پایان این هفته: برنامه‌ای برای سفر به این کشورها نداریم
سخنگوی وزارت خارجه: مختصات جغرافیایی مسیر مد نظر ایران و عمان، مورد تفاهم قرار گرفته
چنانچه برخی طرف‌های ثالث در این زمینه کارشکنی نکنند، بیانیه مشترک دو کشور مشتمل بر ملاحظات و نکات عمده مورد توافق نیز در مرحله بررسی و تدوین نهایی است.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20531" target="_blank">📅 18:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20530">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">داشتون مثل پلنگ اینجاست
🐅</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20530" target="_blank">📅 18:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20529">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805  در این سند هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است. آنچه حذف شده، همگی مربوط به شرکت هواپیمایی عراقی Fly Baghdad است که قبلاً به دلیل ارتباط…</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20529" target="_blank">📅 18:27 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20527">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اتاق جنگ با یاشار : رویترز تبر خورده خبر اشتباه زده
😂
https://ofac.treasury.gov/recent-actions/20260805
در این سند
هیچ شرکت هواپیمایی ایرانی از فهرست تحریم خارج نشده است.
آنچه حذف شده، همگی مربوط به
شرکت هواپیمایی عراقی Fly Baghdad
است که قبلاً به دلیل ارتباط ادعایی با نیروی قدس سپاه تحریم شده بود
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20527" target="_blank">📅 18:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20526">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عراقچی روز جمعه به پاکستان سفر می کند.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/20526" target="_blank">📅 18:10 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20525">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وال استریت ژورنال: ایران همه چیز را به کنترل تنگه هرمز گره زده است.
رویکرد تند تهران، اقتصاد و روابطش با همسایگان را تهدید به نابودی می‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/20525" target="_blank">📅 18:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20524">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رویترز : بر اساس جزئیاتی که روز چهارشنبه در وب‌سایت وزارت خزانه‌داری آمریکا منتشر شد، ایالات متحده تحریم‌های مرتبط با مقابله با تروریسم علیه دو فروند هواپیما و سه شرکت هواپیمایی مرتبط با سپاه پاسداران انقلاب اسلامی ایران را لغو کرده است.
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/20524" target="_blank">📅 18:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20522">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">کانال۱۴ : مقامات آمریکایی تأیید می‌کنند که در هرگونه توافق احتمالی با ایران، تضمین می‌شود که تهران کنترل تنگه هرمز را دیگر در اختیار نخواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20522" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20520">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">رئیس تروریستی سپاه، احمد وحیدی:
«هیچ بحثی درباره اورانیوم غنی‌شده یا سلاح‌های هسته‌ای صورت نخواهد گرفت. تا زمانی که ایالات متحده آمریکا و اسرائیل سلاح‌های هسته‌ای در اختیار داشته باشند، ما به کار خود در این زمینه برای امنیت ملی خود ادامه خواهیم داد.
اگر آن‌ها سلاح‌های خود را کنار بگذارند، ما نیز این کار را خواهیم کرد
.»
@WarRoom
این رژیم قصد ندارد از اهداف هسته‌ای خود دست بکشد. آن‌ها در حال به دست آوردن زمان هستند. هیچ توافقی حاصل نخواهد شد.</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20520" target="_blank">📅 17:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20519">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ارتش اسرائیل: ما حملات متمرکز در جنوب لبنان را آغاز کرده‌ایم در پاسخ به نقض آتش‌بس توسط حزب‌الله.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/20519" target="_blank">📅 16:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20518">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">برای اولین بار پس از حدود یک و نیم ماه، ارتش اسرائیل دستور تخلیه را در جنوب لبنان منتشر کرد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 150K · <a href="https://t.me/withyashar/20518" target="_blank">📅 16:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20517">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">یک مقام ارشد خلیج فارس به سی‌ان‌ان گفت که احتمال رسیدن ایالات متحده و ایران به یک توافق موقت در روز جمعه ۵۰ به ۵۰ است، هرچند تندروهای اصلی ایران هنوز آن را امضا نکرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/20517" target="_blank">📅 16:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20516">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">اصابت یک فروند پهپاد دریایی به یک کشتی و بروز آتش‌سوزی در آن
این کشتی هدف حمله یک شناور سطحی بدون سرنشین قرار گرفت که در پی آن آتش‌سوزی در عرشه کشتی رخ داد. نیروهای محلی تمامی خدمه را نجات دادند و آن‌ها در سلامت کامل هستند. غرق شدن این کشتی تأیید شده است
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/20516" target="_blank">📅 15:39 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20515">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حسن روحانی: یک اقلیتی هستند که می‌گویند «اگر این جنگ تشدید و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم»
رهبر پیشین هیچ‌وقت به دنبال جنگ نبودند
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20515" target="_blank">📅 15:05 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20514">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRKFTzWkKEK4Hw0ucZ6G88rNQtytAdTfVxfLXlUSrMhqmGDyv0OWtocjvgI_J0zNVzpnCY8sJfQplfqXi3VjGaauzGmt3TVio8V32a8pL2h3Rt18YMgGy34qNARtDXjT2QI04b7f_2IR4ukC9IR840yqhtt1ElO1wjn2GHaNNake3GjW1qUHKmZC5r9pcTTQO_yGeVarfJnvIVgmrGmrtaDO6GSB8AuLjvflrA7PbP5Ded0iZudPFCSYN1erLPLdpAvgV_iUjZhI0G2d-S2aZWfdkw0OZqPUQ-cD_aqe1br-lSZx9DwkV8PnvFf-IDFAS4C2yTzMsvJ826irMuxofA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمله هوایی اسرائیل به منطقه المنصوری در جنوب لبنان
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20514" target="_blank">📅 14:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20513">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJZNgIg3Bz4FOus7DcD7WcFrp5uLaXwGFcGx1QHPcYqG2WP3l477nNbUnKL6b7qa4d38yo7CtEWJ6PaQlxMQrdO8DL1a7CZ-XlT7GOKQalg4K_rjBiQdh5KMnsQRl_rmIeHUrbx_rTkO_yUDvI7KD9D9ZhzKCoLVE-hI7lFzTjvIsj_mY8VOL629n_TdCMZ-53fafj4h9_ZT0GH8Vzabgh89kmfIeO7AdgZ3C2qAS_8Nnaov8RJYzGnOld5KMPb3UJTX5eaqkfy52KFI9udEQLy93bJQG2eoMm6kewZVTiGzAmt2Gs6WjOpJCPARxz80hgn72C2YLM2iITYeQ5ITGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش از فروپاشی اتحاد جماهیر شوروی، دریای خزر تنها میان ایران و شوروی مشترک بود و همین موضوع باعث شکل‌گیری این تصور شد که ایران از سهمی معادل ۵۰ درصد برخوردار است. اما پس از استقلال سه کشور آذربایجان، قزاقستان و ترکمنستان، رژیم حقوقی خزر تغییر کرد و در سال ۲۰۱۸ پنج کشور ساحلی «کنوانسیون رژیم حقوقی دریای خزر» را امضا کردند. این کنوانسیون سهم مشخصی برای هیچ‌یک از کشورها تعیین نکرد و تعیین مرزهای بستر و زیر بستر را به توافق‌های دوجانبه واگذار کرد. منتقدان معتقدند نتیجه عملی این روند و نحوه مرزبندی، سهم قابل بهره‌برداری ایران از بستر و منابع نفت و گاز خزر را به حدود ۱۱-۱۳ درصد کاهش داده و دسترسی ایران به بخش بزرگی از منابع انرژی این دریا را محدود کرده است. در مقابل، مقام‌های جمهوری اسلامی تأکید دارند که ایران سهم ۱۳ درصدی را نپذیرفته و مذاکرات برای تعیین مرزهای نهایی همچنان ادامه دارد
@WarRoom</div>
<div class="tg-footer">👁️ 169K · <a href="https://t.me/withyashar/20513" target="_blank">📅 12:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20512">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=tLO7pLREGsjmzBdF4OgLnUnLQJMukXIO_Dmp-bWfu5kM7QwyQ0-sU_RkLtOJtm7OW7LAqdof_-txZlxAEUtBvCzfBx7miMJBx3rrWS5v9OxS2Vib4web8OQh-EEcdksknmi-2AtKmF60RlOjGbkkb-OyCXdISsx7438xvLadfmya1t6bZ4-4RfwEmLp8LWBsvDybTjsJ6N1FLFBNNTmqwLOyzaAqab0kSd8NfRz40MEPv1Sxi56-fbmUBXLocxhkZr3M_EwFA5LIxmnlafpszUEHRNDnFswuO88Idq2buGKKZTw8XTe622VySpyqi7BkJhnB1fz90c4vWWFTSwUG-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f6a7e2519.mp4?token=tLO7pLREGsjmzBdF4OgLnUnLQJMukXIO_Dmp-bWfu5kM7QwyQ0-sU_RkLtOJtm7OW7LAqdof_-txZlxAEUtBvCzfBx7miMJBx3rrWS5v9OxS2Vib4web8OQh-EEcdksknmi-2AtKmF60RlOjGbkkb-OyCXdISsx7438xvLadfmya1t6bZ4-4RfwEmLp8LWBsvDybTjsJ6N1FLFBNNTmqwLOyzaAqab0kSd8NfRz40MEPv1Sxi56-fbmUBXLocxhkZr3M_EwFA5LIxmnlafpszUEHRNDnFswuO88Idq2buGKKZTw8XTe622VySpyqi7BkJhnB1fz90c4vWWFTSwUG-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : تحمل کنین تخت گاز داریم میریم ! داریم میریم سمت قاهره ! غر نزنید دایرکت ! تمام  این مسیر این شیشرو با هم حمل کردیم !
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20512" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20510">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ecb47cbac.mp4?token=K-H1mIfMWe_5zW6DD-Qt4oT8rFSjFmvn4HhvU_CE_TCb3exBMk4GGDQFie1hoBUfFrQdT7j8DeJ2q_CGZicuGUV0zsDPRqPsQIjay90FCwa194Tvwq3fhNymWAfnTHPrpLQ6XFHBS_XIy_p7Azks6cnQMJc4yemm7y4u4tWXxpMaZpJv1c3XPXUrVxqxbgDxqS-NZ-m_ru81KXM4-tgUqPm4DdaGAPf-_hG4IdHn31p2fiJPLlyO529nhsI8SHazOTlzmzn0yq0O2J0LoarNjAxei1VvuurtqeNElc--lNWW5CbpcSSVoPY90oeQPyrY9r3tQGgEN09yOXcb0aInig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ecb47cbac.mp4?token=K-H1mIfMWe_5zW6DD-Qt4oT8rFSjFmvn4HhvU_CE_TCb3exBMk4GGDQFie1hoBUfFrQdT7j8DeJ2q_CGZicuGUV0zsDPRqPsQIjay90FCwa194Tvwq3fhNymWAfnTHPrpLQ6XFHBS_XIy_p7Azks6cnQMJc4yemm7y4u4tWXxpMaZpJv1c3XPXUrVxqxbgDxqS-NZ-m_ru81KXM4-tgUqPm4DdaGAPf-_hG4IdHn31p2fiJPLlyO529nhsI8SHazOTlzmzn0yq0O2J0LoarNjAxei1VvuurtqeNElc--lNWW5CbpcSSVoPY90oeQPyrY9r3tQGgEN09yOXcb0aInig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏خبرنگار: اکنون در قبال رژیم جمهوری اسلامی در چه مرحله‌ای قرار داریم؟
‏ ترامپ: «ظرف ۴۸ ساعت آینده خواهیم فهمید.»
@WarRoom</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/20510" target="_blank">📅 09:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20509">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏پیت هگست، وزیر جنگ آمریکا، در واکنش به گزارش فیک‌ CNN مبنی بر اینکه ذخایر موشک‌ها و مهمات آمریکا در جنگ با رژیم جمهوری اسلامی به شکل هشدارآمیزی کاهش یافته است، گفت: «شرم بر شما باد! سی‌ان ان گزارش شما حقیقت ندارد. خجالت بکشید. ما باید بسیار بیشتر از این از رسانه‌های جعلی متنفر باشیم.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20509" target="_blank">📅 09:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20508">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یک منبع ایرانی به المیادین:
توافق در مورد تنگه هرمز به تعویق خواهد افتاد تا زمانی که آمریکا به تهدید علیه ایران ادامه دهد.
@WarRoom</div>
<div class="tg-footer">👁️ 157K · <a href="https://t.me/withyashar/20508" target="_blank">📅 09:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20507">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">صندوق سرمایه‌گذاری عمومی عربستان سعودی (PIF) به همراه سرمایه‌گذارانی از جمله شرکت Affinity Partners متعلق به جرد کوشنر، خرید ۵۵ میلیارد دلاری شرکت Electronic Arts (EA) را تکمیل کرد و این شرکت را به یک شرکت خصوصی تبدیل نمود.
@WarRoom</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/20507" target="_blank">📅 08:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20506">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">طبق نظرسنجی ها در اسرائیل و اطلاعات کانال 14 اسرائیل :
بنیامین نتانیاهو همچنان میتونه نخست وزیر اسرائیل بمونه بخاطر محبوبیت زیادش و رای بیشتر
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20506" target="_blank">📅 08:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20505">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c23a61982.mp4?token=gENaCCfR7epTSFng-b7SBFQ607YFG9-kcxNABVjsylfA9aE-Ysy8dxb-GL64BAnFV-7OhPhmCpmjdRMRK1habRt4xy01N5yOtA3lPCUnLOrOhEIIEndIgteA9zjsmexbfrEhiz-hyNsA-sB9bQ5K9Zxyqh7YOed_JlHGErX5CjQWVYK_pzmfINzSZAtnx8bUI6FWk--MzM9uA8Rt6rSJDkwRVwdSr52EL1weCS5izcXi6DTwTRTXBylNPbMGk5MTN87MlnagL5-_0y8F18AXjvPx7ouDS9jY_EbWHOpmeGp3l_2o3moW4egt2Ia249hGm6IXAj_cqbg-E2SG32vmcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c23a61982.mp4?token=gENaCCfR7epTSFng-b7SBFQ607YFG9-kcxNABVjsylfA9aE-Ysy8dxb-GL64BAnFV-7OhPhmCpmjdRMRK1habRt4xy01N5yOtA3lPCUnLOrOhEIIEndIgteA9zjsmexbfrEhiz-hyNsA-sB9bQ5K9Zxyqh7YOed_JlHGErX5CjQWVYK_pzmfINzSZAtnx8bUI6FWk--MzM9uA8Rt6rSJDkwRVwdSr52EL1weCS5izcXi6DTwTRTXBylNPbMGk5MTN87MlnagL5-_0y8F18AXjvPx7ouDS9jY_EbWHOpmeGp3l_2o3moW4egt2Ia249hGm6IXAj_cqbg-E2SG32vmcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : ما خیلی خیلی محکم میتونیم به ایران ضربه بزنیم ولی خب اینکارو نمیکنیم، صحبتای خوبی باهم کردیم ولی اونا نمیخوان قبول کنن. اونا به ما زنگ زدن و مودبانه گفتن: میتونیم مذاکره کنیم لطفا؟
ما به رسانه‌ها اعلام میکنیم که داریم مذاکره میکنیم ولی ایرانی‌ها میگن که اصلا صحبتی با آمریکا نکردیم. پس داشتیم چکارمیکردیم؟
تنگه هرمز به زودی باز میشه و اگه این اتفاق نیفته اونا ضربه محکمی میخورن چون ضربه‌ی اصلی ما هنوز مونده ولی امیدوارم کار به اونجا نکشه.
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20505" target="_blank">📅 08:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20504">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فردی مسلح دو روز پیش از حضور دونالد ترامپ در باشگاه گلف او در کالیفرنیا بازداشت شد.
پلیس اعلام کرد این مرد ۳۸ ساله که
ژنین جان تائله
نام دارد، در حال عکاسی و فیلم‌برداری از محوطه باشگاه بوده و ظاهراً فعالیت‌های امنیتی را زیر نظر داشته است. هنگام بازرسی، یک خشاب ۱۶ تیر و مهمات در جیب او و یک تپانچه پر در خودرواش کشف شد. با تفتیش منزلش نیز چندین سلاح، مهمات، جلیقه ضدگلوله، خشاب‌های پرظرفیت و دفترچه‌هایی با نوشته‌های «نگران‌کننده» به دست آمد. پرونده اکنون با همکاری FBI، سرویس مخفی آمریکا و کارگروه مشترک مبارزه با تروریسم در حال بررسی است
@WarRoom</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20504" target="_blank">📅 06:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20503">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آکسیوس: آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و واشنگتن قصد دارد آن را روز چهارشنبه اعلام کند.
بر اساس این توافق، کشتی‌های ورودی از مسیر شمالی در آب‌های ایران و کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان با هماهنگی ایران عبور خواهند کرد و هیچ عوارضی دریافت نمی‌شود. همچنین مین‌های دریایی مسیر مرکزی طی ۳۰ روز پاکسازی شده و سپس این مسیر برای تردد دوطرفه بازگشایی خواهد شد. قطر، پاکستان و عربستان نیز در میانجی‌گری مشارکت داشته‌اند و کاخ سفید مستقیماً در مذاکرات حضور داشته است. عباس عراقچی با این چارچوب موافقت اولیه کرده بود و به گفته منابع آمریکایی و منطقه‌ای، مجتبی خامنه‌ای و شورای عالی امنیت ملی ایران نیز روز سه‌شنبه آن را تأیید کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20503" target="_blank">📅 06:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20502">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رسانه های عراقی طرفدار رژیم :
شنیده شدن صدای مهیب انفجار از سمت ایران در منطقه شلمچه در نزدیکی مرز آبادان
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/20502" target="_blank">📅 23:07 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20501">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مارک لوین : دیکتاتور سعودی دوست نیست
@WarRoom</div>
<div class="tg-footer">👁️ 183K · <a href="https://t.me/withyashar/20501" target="_blank">📅 22:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20500">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=RHsLM1UIpbo5OcId9CJe5aOvoQk8E1Oj1Q5-BnquY7el9p9qiGq7p-i70ujS4zr-5Ag3Ebdk8KTj0mkv75Rz-gJnnlKCqPemB1Rt6nNEO7odoFZvrhwGOgxZhBavXUgWnKgYuzPv6T8UnG9c2e2puuNT07ltP8tRnBcHQyKqKSs9W4oBqeYlNBXeoF31nuo90uc0KN_xF7p7uS9L9dw6GH5GePYPipKfIVxP69d3NNp4nyXGJ9kUmbAES2AtkWiV7F3d34d-ECBToT7lBJzl6EBBB1atj-tJNfDsH4WnsYAAgqTAUn2pE2BqKpS7KSGuoGjHA3QhCTMUvNB9Q21sYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049666fcb2.mp4?token=RHsLM1UIpbo5OcId9CJe5aOvoQk8E1Oj1Q5-BnquY7el9p9qiGq7p-i70ujS4zr-5Ag3Ebdk8KTj0mkv75Rz-gJnnlKCqPemB1Rt6nNEO7odoFZvrhwGOgxZhBavXUgWnKgYuzPv6T8UnG9c2e2puuNT07ltP8tRnBcHQyKqKSs9W4oBqeYlNBXeoF31nuo90uc0KN_xF7p7uS9L9dw6GH5GePYPipKfIVxP69d3NNp4nyXGJ9kUmbAES2AtkWiV7F3d34d-ECBToT7lBJzl6EBBB1atj-tJNfDsH4WnsYAAgqTAUn2pE2BqKpS7KSGuoGjHA3QhCTMUvNB9Q21sYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ عازم لس‌آنجلس و لاس‌وگاس شد
@WarRoom</div>
<div class="tg-footer">👁️ 186K · <a href="https://t.me/withyashar/20500" target="_blank">📅 22:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20499">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سنتکام اعلام کرد که از ابتدای ازسرگیری محاصره دریایی اعمال شده علیه ایران تاکنون 45 کشتی را ملزم به تغییر مسیر کرده و دو کشتی را با هدف‌گرفتن آنها ازکار انداخته و دو کشتی دیگر را مورد بازرسی قرار داده است.
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20499" target="_blank">📅 22:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20498">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIXpgiS14x8PE13Wm072c0Ii6NlrGjeRFuHdU8RdLfqZFIJhVcvWynmAcZaPsK0LQYo_LsOOHG3YA8txuOsFwRn53Q-bZpfuXfn4dLGaHnQI3y6_sbDFYBKS4n9GrIQX8TCl4xJjJsiVg_rf1FMXGs5OL4y4UXRwXOwNdCO2D3AreKsyU2DZcGcYfBqPb5cDWtABoMSexvJQPqTuTE_c_YakomGlmVUM2zoIsUrIz81Rg-u8-gXQoLoZYjNvZcBBPFm-LXkmm3CKtzDRda3aonkl1bKzsCrMvdn12D3TTZuOa1hX5a3gPYsYPvfajO5OQoqoNrKbN7YPSEaUQuJnjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت ۷۹.۳۵$ شد و به زیر ۸۰ اومد
@WarRoom</div>
<div class="tg-footer">👁️ 182K · <a href="https://t.me/withyashar/20498" target="_blank">📅 21:36 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20497">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وال استریت ژورنال: اگرچه واشنگتن تأکید دارد توافق ممکن است به‌زودی نهایی شود، اما ادامه حملات دریایی و اختلاف بر سر شرایط و هزینه‌های بازگشایی هرمز، همچنان مهم‌ترین موانع پیش روی مذاکرات هستند
@WarRoom</div>
<div class="tg-footer">👁️ 179K · <a href="https://t.me/withyashar/20497" target="_blank">📅 21:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20496">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نتانیاهو:
ترامپ و تیمش معتقدند می‌توانند حماس را وادار به خلع سلاح کنند و غزه را کاملاً غیرنظامی سازند. آن‌ها پیش‌نویس این طرح را برای ما فرستادند، اما ما با آن موافقت نکردیم. این پیش‌نویس، طرح ما نیست؛ ما اصلاحات و نظرات خود را برای آن ارسال کردیم. جالب اینکه این نظرات را پیش از آغاز جنجال و فضاسازی رسانه‌ای درباره این موضوع فرستاده بودیم. این موضع رسمی ماست و با درایت، قاطعیت و حفظ منافع خود، بر آن ایستاده‌ایم.
@WarRoom</div>
<div class="tg-footer">👁️ 178K · <a href="https://t.me/withyashar/20496" target="_blank">📅 21:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20495">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فاکس نیوز:یک مقام ارشد دولت آمریکا فاش کرد که لغو جنگ توسط پرزیدنت ترامپ در واقع بخاطر لو رفتن زمان جنگ در رسانه ها بوده و ترامپ این جنگ را فقط به عقب انداخته و مشاورانش به او گفته اند می تواند در این بین و برای آخرین بار به جمهوری اسلامی فرصت مذاکره و توافق دهد و در غیر این صورت در تاریخی که از قبل معلوم کرده و این دفعه امیدوار است لو نرود، حمله بسیار گسترده به ایران را انجام دهد.
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 176K · <a href="https://t.me/withyashar/20495" target="_blank">📅 20:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20494">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=b6BqCuqaOOthCJPVYKJTX1XrMS8-Pj0pCWony9COlkI-UTJ_5b-EJuhZXn-QkcA8x4msFxyZmkcOBn6chGCkoNUsuzFQ1um__VFSZaf8hl9mW6zJP57G5zaHHubdAXKwLnCjd7mnjXkjWiY4e5b1gBaGsshowUGd01RqPNgcR6Si2yWhIAdOqJ2YKimffheSGMdNnHb24FtaA0xP4w3Ko2zxjH22DRbZkn7t3OJ_Ajjk9oK9DT7jdzB2C-TPepOBVI5Y37Ev9UswsCIKULNVD4S1WQp9pDdn1YnhaoLvGLe0LsQm1aDc2DM2E2u42QiOAxkBApBZ8fC10QZlFN_Tyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4509abf5f6.mp4?token=b6BqCuqaOOthCJPVYKJTX1XrMS8-Pj0pCWony9COlkI-UTJ_5b-EJuhZXn-QkcA8x4msFxyZmkcOBn6chGCkoNUsuzFQ1um__VFSZaf8hl9mW6zJP57G5zaHHubdAXKwLnCjd7mnjXkjWiY4e5b1gBaGsshowUGd01RqPNgcR6Si2yWhIAdOqJ2YKimffheSGMdNnHb24FtaA0xP4w3Ko2zxjH22DRbZkn7t3OJ_Ajjk9oK9DT7jdzB2C-TPepOBVI5Y37Ev9UswsCIKULNVD4S1WQp9pDdn1YnhaoLvGLe0LsQm1aDc2DM2E2u42QiOAxkBApBZ8fC10QZlFN_Tyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام : جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در حال دریافت سوخت از یک KC-135 Stratotanker در آسمان خاورمیانه
@WarRoom
🚨
🚨
🚨
🚨
یاشار: اف۲۲ ها هم اومدن منطقه و آماده هستند</div>
<div class="tg-footer">👁️ 170K · <a href="https://t.me/withyashar/20494" target="_blank">📅 20:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20493">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">تلویزیون ایران: اگه ترامپ خودش بزاره ما توافق میکنیم ولی دخالت میکنه نمیزاره
مذاکرات بین دو کشور ساحلی در حال انجام است و هیچ ارتباطی با ایالات متحده ندارد، اما ترامپ با دخالت‌های مکررش، تلاش می‌کند این تصور را ایجاد کند که بر روند این مذاکرات تأثیر می‌گذارد.
ایران در تلاش است تا به صورت مستقل از تهدیدهای آمریکا، به پیشبرد برنامه‌های خود در مورد تنگه هرمز ادامه دهد و تأکید می‌کند که تأثیر ایالات متحده بر این مذاکرات تنها منفی بوده است، و تهران منافع و اولویت‌های خود را بر اساس زمان‌بندی یا خواسته‌های ترامپ تعیین نمی‌کند.
@WarRoom</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/withyashar/20493" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20492">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یک کشتی کانتینربر متعلق به هند در دریای سرخ به وسیله یک قایق انتحاری، نزدیک بندر حدیده یمن، منفجر شد و در حال غرق شدن است!
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20492" target="_blank">📅 19:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20491">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyM_DJtMV4RUUndsXufK77FUz-rmSDhIhFQUcMD99i0TGwmz82MMhaEtdkztdF8LSL2lkncPRyn-OAoWvveO0LrYS_ktBFVxzSDVJStUnUrpaBjGo63bKm0jMcUeid6guhkwVH_pHQyjdpXMdKx1BJd1sVAQnrkT-7u78WFpcGA9agHu3RQrkI5HI-RkfODeApUVAOXSd5v-9fstk3YgpuAPo_kDg-Sof5Ac4XBz2LKzFHw1OEtdNehupiAbvtIP8-mexz5yCA6JWkqzb_X9A8BQKWOA6Ykam87Vw-0nPPiPVMSTcF5IS_ThC1OKsOSSZbtkqp8UAP4Ba1r-7rU96A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ستون دود اهواز ….
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20491" target="_blank">📅 19:11 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20490">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادعای ‌اینترنشنال :بر اساس اطلاعاتی که به دستمون رسیده، ملاقات پزشکیان و مجتبی خامنه‌ای که تو اردیبهشت انجام شده، زمان خیلی کوتاهی داشته.این دیدار داخل پناهگاه نبوده و تو یه محل امن، داخل ماشین انجام شده.
ادعا شده پزشکیان و مجتبی خامنه‌ای روی صندلی عقب ماشین نشسته بودن، اما صورت همدیگه رو نمی‌دیدن و گفت‌وگو به همین شکل انجام شده.
همین موضوع باعث ناراحتی پزشکیان شده و گفته: «اصلاً معلوم نیست اون شخص مجتبی بوده یا نه؛ با این کار منو تحقیر کردن.»
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20490" target="_blank">📅 19:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20489">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SG8E7_8Sh9-9OtOLK31h9_svKELOdBcT00LryRfS0P9I6Rfx_9_FuxEvQ8MKHXlW2FHjWWI1OMvhcSTdvaoko_9pfeZVjvWPYEFS8IhaBm7tXt2OA4fxCMEHuJbMCjlMFuRW3XH6mzs_7Wa8gjt0GC7LrxN-vTF8FenOftDd5QBeXGHTTLN_VV2TD3ywsNW2tP7IfiZ6mrG4E0IG7WpdG_UoofKzOMsjgYXXfoKanw4t4OO8c3CY7IjHmFxLO5exaE4Xj5YC2GwwUFwhm2FdFKg4kr4CDXwhHtGHBSX5oX1UlvCgc_YhoKcUjw7-MHVnfiYPIdzwJpH9E3Ga3DYsNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدای توافق اهواز همکنون …
@WarRoom</div>
<div class="tg-footer">👁️ 160K · <a href="https://t.me/withyashar/20489" target="_blank">📅 18:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20488">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNn5MgGM61s6jhCC2Sa5kp_DL9rI5Kng9mpaYV5XMozlAE-BID_c0V06RhXHdDjPH8E96uDA1_4B9bz2oDkFB9bGxOXMnUuC2aVtWkQRSVz7QulApOCjh-H3EiAd-pEyNPYUeiV3PxuExGV8GB7QrtGW_hxzBQ6KyNrxEQdHnAZBO6_8gpDeKdGo6dBiKPjYG_so1ZbA1fRCmsAyjOVkR114Eokm-WcFbPKWQAvJUvzqvMvF4_Hj_IIhoZ67VtYfBh2A4qT_IIFFbvHRnlm3a6I579ZuKLA7rmJ3rnKT-lolrHPm7iDQlqlb0ct5EzsAxIeDCMh7wHQ0CkSz5siB6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: «توافق قریب‌الوقوع است» همزمان با از سرگیری مذاکرات ایران در روز دوشنبه درباره خلع سلاح هسته‌ای
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/20488" target="_blank">📅 18:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20487">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WGDwI57sXvwEqC4RXdk9RIqQBFuCF4gYS4YDgXR3tEHxE7Ua6UcOTvQJ-bPggct25ZtmF16Gc3OIonBPh-xBz__n9pPt-0mg6YRNNE619e9-jCn-03HFyEADX9fK5eJeKbDKDCBFrU53oTyW5SzE6moA-1lv-ujDMuKTLsjZiKFuvRRPZ3cnNZK_0y_NvkPJ2U_w1ENHCIUJ20ZL5NRovYqiQPfxKrPMimb_ejxngdH5NjmbN73ir5IlXMCRirloyAz7mM43THnT3QVGBde4OASBGliRIn5nC9WC_tdQp9PFeJoHVq8K0oMelYUQtr01zIAyZ6ATTE3LMcNWKuk-8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام ياشار همين الان پادگان سپاه بانه انفجار شديد
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20487" target="_blank">📅 18:00 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20486">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=BXl3eYrEdEKXW-SS3g6OYfrvksYOQnEPfp033BYEsEHdnnVR4FcKOsNgsds9oRn61ZPb5cTOG0qvcLesR7U2JZvCeumKzaps5UphrGpB_DmjkYxBnEzhn9-cXu6JERWKbJGvHy8tBMHVrcLjVHO5Lf0GVorYmivN9oQn3eiEyDDjwvGaXq51nuPUsW7UEKskYn-nOCovWDJsGn_UZazPyQaLWp_VF7CFHb6Ah6yzYqYSLvIc7QeZbFpPVcAafbJtLhiN_1uC5DQbnybU4_g9VfH4NZX-azUlbZwsYBDubD1YjccCcc6e8ZBWeX7900eXj3ghF-sp0lbmRhQfwvYXrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa412933a5.mp4?token=BXl3eYrEdEKXW-SS3g6OYfrvksYOQnEPfp033BYEsEHdnnVR4FcKOsNgsds9oRn61ZPb5cTOG0qvcLesR7U2JZvCeumKzaps5UphrGpB_DmjkYxBnEzhn9-cXu6JERWKbJGvHy8tBMHVrcLjVHO5Lf0GVorYmivN9oQn3eiEyDDjwvGaXq51nuPUsW7UEKskYn-nOCovWDJsGn_UZazPyQaLWp_VF7CFHb6Ah6yzYqYSLvIc7QeZbFpPVcAafbJtLhiN_1uC5DQbnybU4_g9VfH4NZX-azUlbZwsYBDubD1YjccCcc6e8ZBWeX7900eXj3ghF-sp0lbmRhQfwvYXrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو درباره ایران
: در مذاکرات برای بازگشایی تنگه هرمز پیشرفت حاصل شده است، اما هنوز توافق نهایی به دست نیامده است. ما امیدواریم که توافقی خیلی زود نهایی شود
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20486" target="_blank">📅 17:57 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20485">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادعای رسانه‌های کشورهای حاشیه خلیج فارس:
به‌زودی بیانیه‌ای درباره بازگشایی تنگه هرمز منتشر خواهد شد
،
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20485" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20484">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs6AEJcWO6eP2v2JnerI5YABiPKdG4YOMSxby6j02O6rZjxUqSNBbnvyvMUXK7bSwwA2g6n4jFiquWXaIuf2O9U885pMIfnhgBMyMg39LfaOegPcXBGqwsNWNo6Q42e-fhmqLtf-GNzYfsRsOG_umfBtbg9NYFLFE6Zdm94TUnI1m7q8kV1YIcqnrsjHGs1w7H4aWJYlmmSdsXQgIxDTDbMeSa1-6bRzPRHPPjAq8X0f6L9tmR6nYsysSh1OO1JdNu5hCwitYbXBCP2U5_E7OOpfkOds6LiNizgxYrjHUgrxKXXSagwqRX7BIxrrEgM2fSm61rc8jDQuS6sO_MYKJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه داری آمریکا، در مصاحبه با CNBC، گفت: ممکن است فردا با ایران برای بازگشایی تنگه هرمز به توافق برسیم.
کاهش نفت و افزایش اونس طلا بعد از این مصاحبه
@WarRoom</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20484" target="_blank">📅 15:54 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20483">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">«تبریزی»سخنگوی اورژانس تهران : ۱۸ مصدوم در حادثه انفجار در شهرک شمس‌آباد
متاسفانه پایگاه اورژانس هم در نزدیکی محل حادثه به دلیل موج انفجار تخریب شده است، علت انفجار در دست بررسی است.
@WarRoom
یاشار : دقت کردی ؟ موج انفجار ! علت هم هنوز مشخص نیست!  فقط بی بی میدونه</div>
<div class="tg-footer">👁️ 164K · <a href="https://t.me/withyashar/20483" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20482">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بلومبرگ : ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20482" target="_blank">📅 14:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20481">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">یک مقام ارشد پاکستان به گاردین:
مذاکرات میان جمهوری اسلامی و امریکا،
به بن بست رسیده است!
@WarRoom</div>
<div class="tg-footer">👁️ 165K · <a href="https://t.me/withyashar/20481" target="_blank">📅 14:49 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20480">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قطر: متن اولیه برای یک توافق  آمریکا/ایران تدوین شده است
@WarRoom</div>
<div class="tg-footer">👁️ 162K · <a href="https://t.me/withyashar/20480" target="_blank">📅 14:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20479">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اتاق جنگ با یاشار :میگن کارخانه آلومینیوم کاران بوده بد نیست بدانید
آلومینیوم یکی از مواد پرکاربرد در ساخت پهپادها و موشک‌ها، از جمله پهپادهای شاهد-۱۳۶ و آرش، به شمار می‌رود. از آلیاژهای آلومینیوم در بخش‌هایی از سازه و قطعات داخلی استفاده می‌شود و هم‌زمان از کامپوزیت‌ها و فولاد نیز بهره می‌گیرند. این فلز همچنین در ساخت موشک‌های بالستیک، کروز و برخی موشک‌های سوخت جامد کاربرد گسترده‌ای دارد.
@WarRoom</div>
<div class="tg-footer">👁️ 161K · <a href="https://t.me/withyashar/20479" target="_blank">📅 14:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20478">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">وزارت خارجه قطر: تا کنون هیچ توافقی حاصل نشده است و در حال حاضر، مهم‌ترین مسئله بازگشت به مسیر دیپلماتیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/20478" target="_blank">📅 14:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20477">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=vXAG9Du09aMoaXOr-NXOj-EHcCx014kRDZkXHQ7_30PrTXaC4bteseyVIYnlZUt-24br39TSOol8MW0p4-i9KYqkOx41XR2d-hhIBt9azPohhJIX6DWo6Sd8hN7QzDCoCEDYwsizyYc0tOA6mOYLIvGI2L2N_2B2f6fri8iq8hMaGUH5GvqZ2xbPdk9rGwXnVn3RoD3anrJpXSsuUV1IMDhnzgPUZ2HH3U9bQljZVl8Wfm0-yKBYHTPkmuCP2MYmAyr4KzlzTKLHQFxziuyh7X7_zW9SxQN8Unfr4Cxuxl-rzRV7csrXpzmKdPogASC8fKSTlQiYqLn3hAdyp2u_N7uKnPGfyXLW0AO6UzOYnWfsWpLLQofdrXdbMoTHQnwYe7p3ffI7-sz7WnBjvvyATx-rgblG2xcZvWy3ktuXtoUUOKMK3OHMd9etgNqDHKxUsooeJ5LH0bk4EI6TC2z2Ab-Ao0N2t97gTn6Om3-dBIRuk_UK4d73LDCGfjOmvakyXrpoT_KEvLj7W-Ni4hEPIRmwSMJ_ghg4PKidSNzBCGSKI_P7GLskJjcixbgULFeTteQgS_mYnKXijfB9mu_adP_gRwLKns9O4uYV3fjSOlcU-5_CWFMi2CZ8VJTQvVdU78PXwi02IQRrSOPluDXukhejjQlX5CD9wZYbrgkMA1Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b588c7cf3.mp4?token=vXAG9Du09aMoaXOr-NXOj-EHcCx014kRDZkXHQ7_30PrTXaC4bteseyVIYnlZUt-24br39TSOol8MW0p4-i9KYqkOx41XR2d-hhIBt9azPohhJIX6DWo6Sd8hN7QzDCoCEDYwsizyYc0tOA6mOYLIvGI2L2N_2B2f6fri8iq8hMaGUH5GvqZ2xbPdk9rGwXnVn3RoD3anrJpXSsuUV1IMDhnzgPUZ2HH3U9bQljZVl8Wfm0-yKBYHTPkmuCP2MYmAyr4KzlzTKLHQFxziuyh7X7_zW9SxQN8Unfr4Cxuxl-rzRV7csrXpzmKdPogASC8fKSTlQiYqLn3hAdyp2u_N7uKnPGfyXLW0AO6UzOYnWfsWpLLQofdrXdbMoTHQnwYe7p3ffI7-sz7WnBjvvyATx-rgblG2xcZvWy3ktuXtoUUOKMK3OHMd9etgNqDHKxUsooeJ5LH0bk4EI6TC2z2Ab-Ao0N2t97gTn6Om3-dBIRuk_UK4d73LDCGfjOmvakyXrpoT_KEvLj7W-Ni4hEPIRmwSMJ_ghg4PKidSNzBCGSKI_P7GLskJjcixbgULFeTteQgS_mYnKXijfB9mu_adP_gRwLKns9O4uYV3fjSOlcU-5_CWFMi2CZ8VJTQvVdU78PXwi02IQRrSOPluDXukhejjQlX5CD9wZYbrgkMA1Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمس آباد یک انفجار یک سمت و بک انفجار سمت دیگر !
حالا عرزشی چی میگی ؟ گاز و گوزه ؟!
🤣
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/20477" target="_blank">📅 14:08 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20476">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=fKtLGjGPlsKtdwqR6TsuRVgcXaRNQJuMIx018gNzuJvk8C4OXzJrcYvBC0TDHM_xcpLC4_-z16kzLZzB6J-IeHTMN2AUrmf4HjG7RkYSttyTodnBcO19StVCsLwOJlTQC9ORhi2aCrdqkIji7qcEomKpVrJrMN-bTEsZQT69Jmer5wgpTkdNnUir5PsQffhbUi1D0kFgBzPNlwMN217d7l7-qQI33SExTtwEu4BPqSj80YMHP2qj5UVIjJk4g32e4QhB7sUOsp0uyWHQ4BYIWsZt_KRi5HEqnBBv28BuNYVnzBbu_n4-OpDKgdmXxEOzH-81--rs6EoAS5_JdvFZAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0d135103.mp4?token=fKtLGjGPlsKtdwqR6TsuRVgcXaRNQJuMIx018gNzuJvk8C4OXzJrcYvBC0TDHM_xcpLC4_-z16kzLZzB6J-IeHTMN2AUrmf4HjG7RkYSttyTodnBcO19StVCsLwOJlTQC9ORhi2aCrdqkIji7qcEomKpVrJrMN-bTEsZQT69Jmer5wgpTkdNnUir5PsQffhbUi1D0kFgBzPNlwMN217d7l7-qQI33SExTtwEu4BPqSj80YMHP2qj5UVIjJk4g32e4QhB7sUOsp0uyWHQ4BYIWsZt_KRi5HEqnBBv28BuNYVnzBbu_n4-OpDKgdmXxEOzH-81--rs6EoAS5_JdvFZAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار اسلامشهر هم اکنون
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/20476" target="_blank">📅 14:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20475">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFZ1BmO22FXV4kbXJuE2m_VXL0xlCvC2umYCDzXxo0xrfyMBpzg9g-JsLma3d1OKSmAf0nEkOFmeZ9_q1w9FCfhtnAYRuWZb8MAoYpI5GNKyskBinqcTBd412t_6j-UtbTn_G-0-vfVtJitARs3TQBSQ6wmURmM_a5WCdwEdQvoWCayPJ08eL9QzNuHn5Wogq9AaoSCeNXb30k4iJkQWJT4fYd41BKJZ71mnVVAQQsB78T-74QUT-V1QoFt1M6Cd0PHQbDnDxzJLwNyzb4wzrd_w5hr4V5jLZsVmY-yzi6p7qPuUixICCuBik-MkBqUk5CSSJW5R9H_gZI5AZxkwHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت مدیره شهرک صنعتی شمس آباد:
چند لحظه پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
اصلا حمله ای نشده مردم نگران نباشند
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20475" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20474">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گروه تروریستی حوثی‌های یمن اعلام کرده‌اند که یک حمله دقیق با استفاده از پهپاد علیه یک "هدف حساس" در فرودگاه نجران در عربستان سعودی انجام داده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20474" target="_blank">📅 13:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20472">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=VL9GH1_XOy5VXWBfP-h1Xs-IDMq_aMFTbCiLypGfCVWwKhmkYtqgTMvshkBgMn6MOcX4cZpMDzHAerc1b-Q24RfNWA1NFXUAB7k00HHGFVVf_JoU4kvSJI3rbU9bs0IeGjqSDbkQ7doxQQ_H4AWrX-EHY3wTbmHdxRue1cJOlxtaNKSZ3uSt-Dp0NrDtdFqlrEU-VdYqJhSJ6XDkUbLrchRKKz6dGH2D4acaujgVALBMvLOuPFjx5uc0Q86hp7lj5Ik6YcTNedDUsaxx6o22NY-hCXXp6Utb8ah9bVKBxwSVkZe_yvvqEFjYK4lE6jk71H89dC0Mlh16-96sQloDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d96f29aa.mp4?token=VL9GH1_XOy5VXWBfP-h1Xs-IDMq_aMFTbCiLypGfCVWwKhmkYtqgTMvshkBgMn6MOcX4cZpMDzHAerc1b-Q24RfNWA1NFXUAB7k00HHGFVVf_JoU4kvSJI3rbU9bs0IeGjqSDbkQ7doxQQ_H4AWrX-EHY3wTbmHdxRue1cJOlxtaNKSZ3uSt-Dp0NrDtdFqlrEU-VdYqJhSJ6XDkUbLrchRKKz6dGH2D4acaujgVALBMvLOuPFjx5uc0Q86hp7lj5Ik6YcTNedDUsaxx6o22NY-hCXXp6Utb8ah9bVKBxwSVkZe_yvvqEFjYK4lE6jk71H89dC0Mlh16-96sQloDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کشتی باری که امروز سپاه زد !
ایا این حملات جواب این حمله است ؟ یاشار : شک نکن!
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/20472" target="_blank">📅 13:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20471">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MRh9OIpZQuI_4Y2c8jOIGVNWj7Y4g-TmR_-nbKZyOzdgtYl-iys5MF1Im2dltK04Kjyjc3j9-WaORJtWIhY_i9rZbncm5S1oWiMBL4mQevPMzyIKOZ1_ltF1GzKosq_XT0KP8EMVaWgDgYxGWjyWuEv5vULXSvli3MDl0gHen2-vippFEgJc1G9IrvVIJf_52QkhhPzYgS5xI4-ITQec0f1twTqZyfTV1Q7L8kNywE8fqfEkCURX2ykxrU_9xVDMT1IkFBlE76hmdDeew6U0u90DDPuB2tfbLurojOiwUBOGv6ftPoE-NzZJCtwzeXQx0GxJhNilItnYhdHQJBMrDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلاورجان اصفهان رو هم زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/20471" target="_blank">📅 13:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-20468">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=Jnetc9-OE7rhQsmrEKc2SW_UFpmmTErpeO9trncKi44lHD6b7-WjZYaylXFllu15Khch_ejuphiD9hU1LwhoIoHE077Ken3XWCh0Fb87XKGLAAWHJ_9F9KEEnzGWD_zmSSPUENXPbmBzJHlH0r6HrMAUXD7NJIvL5CICHrGD9tn45-GhmoQaSATWy70rPeBjLHelqHQEqNVJbDfzeJYVzYCxdw8lM08Wq8DXBNjoKwOgxayb7_svVrmp0YzoFjrzi_L9JL3-hJDs4Wmv-jN75RDaRJlwIlM_pl_nygpr0UQMIz2Jr9IajFNYGxfgzG4i127Cw6_selCEUiwFFH0vpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/538f54d0f8.mp4?token=Jnetc9-OE7rhQsmrEKc2SW_UFpmmTErpeO9trncKi44lHD6b7-WjZYaylXFllu15Khch_ejuphiD9hU1LwhoIoHE077Ken3XWCh0Fb87XKGLAAWHJ_9F9KEEnzGWD_zmSSPUENXPbmBzJHlH0r6HrMAUXD7NJIvL5CICHrGD9tn45-GhmoQaSATWy70rPeBjLHelqHQEqNVJbDfzeJYVzYCxdw8lM08Wq8DXBNjoKwOgxayb7_svVrmp0YzoFjrzi_L9JL3-hJDs4Wmv-jN75RDaRJlwIlM_pl_nygpr0UQMIz2Jr9IajFNYGxfgzG4i127Cw6_selCEUiwFFH0vpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون فرودگاه بین‌المللی رامون اسرائیل دیگه هیچ جایی نداره و از سوخترسان های آمریکایی در حد انفجار رسیده ، مذاکرات بسیار خوب پیشم میره
@WarRoom</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/20468" target="_blank">📅 13:42 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
