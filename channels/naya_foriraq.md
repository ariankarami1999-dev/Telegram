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
<img src="https://cdn4.telesco.pe/file/RWfWfb1S_AxWny7SMXdS8xIzVhAdvqceyAnEkfmKSY_B4lRr16z7cBpoAGWaZL6FMk98EiDsWZaLKs33w7NSNEZKwOruzvmRgU-g3Lkefd3jz6SLYVE0N7tUaNL6JTXfeAmsY9PZAFvQ5vxkTqPj5g6XSx3l0Ev49k-Emk94Jayd_XUBKAtyMRbv3_INgVJ0CQt7AaroT3XYRIWZixdXxDyJ6ZUqE4VHX6zmRerIK80dUdDVXZxar7J2eNex4tedoHVlq_g06wl2tmzjwhG8oeZnvCugfomFxChUWfzr1PTUn_XQnVvnY-rIZQPRBzd1usBsYGYLBCVYXEaBNSLN_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 271K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 19:50:12</div>
<hr>

<div class="tg-post" id="msg-85123">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">موجة اخرى من الغضب الحيدري</div>
<div class="tg-footer">👁️ 1.59K · <a href="https://t.me/naya_foriraq/85123" target="_blank">📅 19:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85122">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">‏
وزارة الدفاع الألمانية
تعلن أنها تعتزم سحب سفينتين حربيتين من منطقة البحر الأحمر</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/naya_foriraq/85122" target="_blank">📅 19:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85121">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">موجة اخرى من الغضب الحيدري</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/naya_foriraq/85121" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85120">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇺🇸
مرة اخرى تنوه الخارجية الأمريكية
😆
:
على الأمريكيين في الشرق الأوسط الاستعداد لاحتمال إلغاء الرحلات وإغلاق مجالات جوية في المنطقة.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/naya_foriraq/85120" target="_blank">📅 19:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85119">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔻
Here's what the Iranians would say to the U.S. ...
🔻
Naya team on telegram</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/naya_foriraq/85119" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85118">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juNwuRPZByrkQslMArHLiKwzLXIasazyNf4895W7HgKfu4afrr25QtTPlW0iu8D3V04j4WdHvGCOnqSk4X8kobE90T-B9eU4owqkUWUmRD666aS0ALRmpHC1ZouUqYCz9fAvwrxIOgraagZndIT2sxONhKMx4JcVRsRB5zU6xnwW1x76dqJvCIxabd3X3rj3dcE9fe8aYHD264IMdEp6F0PIY4sxNjUWakiMGcw7seY9dc2X6-ggWq7dWAHMYP8mLRU3zZ2i8s9dotZ6MM_OuZI3XG4FguiqzjMpYptHKPlKd3lwPgea_wADwy4rVSOXlbkbgv1rI4s6mOvk0FApZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب الإيرانيين لم يتلقوا بعد الألم</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/naya_foriraq/85118" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85117">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شبه لهم يا حسين
ما طحت انت من ميمونك</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/85117" target="_blank">📅 19:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85116">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">موجة اخرى من الغضب الحيدري</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/naya_foriraq/85116" target="_blank">📅 19:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85115">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/naya_foriraq/85115" target="_blank">📅 19:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85114">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/naya_foriraq/85114" target="_blank">📅 19:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85113">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">تفعيل الدفاعات الجوية الإيرانية في سماء قشم</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/85113" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85112">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">ارتفاع اعمدة الدخان من منفذ العبدلي الكويتي</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/naya_foriraq/85112" target="_blank">📅 19:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85111">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انفجارات عنيفة تهز الكويت</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/85111" target="_blank">📅 19:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85110">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/naya_foriraq/85110" target="_blank">📅 19:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85109">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/778c692cfe.mp4?token=QUTqQl80eg9fcmM5JZSjuy6RLtCDHpahEfdJAJ0hgtUk_K2gn9npj8Y2jaBPfMXJTDIgeQr0jetimme9cmDTV-oOat2acfUgntGsJNU16WZ4dMVidqaZI-MEcSl0XHePS2ykm3iet6FeRgPRuu1GvW6g1xAYbVAyA4vW_LmMr67wcpXpwrvEOCrdFOIxpr9n7jz5BeBx5vhzEGSLOXTxN4Qw7Gydgd7e02NRt-ojWVxDNzwNCdESwetZyeb5JdTSheTM92Ox6hqGyLGmbMNOE-HWvq7FpMx6UqLDMKFQD6y9M0pUOyQHS9c-f2iCnQEia5guRpIFOIyRXGYUjgNyIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/778c692cfe.mp4?token=QUTqQl80eg9fcmM5JZSjuy6RLtCDHpahEfdJAJ0hgtUk_K2gn9npj8Y2jaBPfMXJTDIgeQr0jetimme9cmDTV-oOat2acfUgntGsJNU16WZ4dMVidqaZI-MEcSl0XHePS2ykm3iet6FeRgPRuu1GvW6g1xAYbVAyA4vW_LmMr67wcpXpwrvEOCrdFOIxpr9n7jz5BeBx5vhzEGSLOXTxN4Qw7Gydgd7e02NRt-ojWVxDNzwNCdESwetZyeb5JdTSheTM92Ox6hqGyLGmbMNOE-HWvq7FpMx6UqLDMKFQD6y9M0pUOyQHS9c-f2iCnQEia5guRpIFOIyRXGYUjgNyIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع اعمدة الدخان من منفذ العبدلي الكويتي</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/85109" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85108">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=sdN8Hx1V9lqVH8PeAHQULQY8grqynUPjUldQU0xeDv2wdENDDkMeWjf56m45LwiwIsArifbPfMJsQ3z_WJE60y97NxDN1XJjprhO1wxNC2JuJuMC4mWls3pmyEeEAsZBzC9_lXdoDWREXsgH7zFiHGiYtOhC5dZMxMWnEyh73a6vC9HV7lZn1BKThKZACdwws3HQuXXVb1Jf1rpxVmfUkXFmsybTZ2u_nJ-X_SgpzjQwbOLyIu-zvI6l2RKhwpBJg6HxHxRGGR1qeniUMCVGeDH3GGmE-hvN-zuDj_wlGZytuy_JyLeaqftVZY4dAFEE-JxE13FoMHpVAL0vDYQoJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4befd2a6b8.mp4?token=sdN8Hx1V9lqVH8PeAHQULQY8grqynUPjUldQU0xeDv2wdENDDkMeWjf56m45LwiwIsArifbPfMJsQ3z_WJE60y97NxDN1XJjprhO1wxNC2JuJuMC4mWls3pmyEeEAsZBzC9_lXdoDWREXsgH7zFiHGiYtOhC5dZMxMWnEyh73a6vC9HV7lZn1BKThKZACdwws3HQuXXVb1Jf1rpxVmfUkXFmsybTZ2u_nJ-X_SgpzjQwbOLyIu-zvI6l2RKhwpBJg6HxHxRGGR1qeniUMCVGeDH3GGmE-hvN-zuDj_wlGZytuy_JyLeaqftVZY4dAFEE-JxE13FoMHpVAL0vDYQoJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لا عزاء لنتنياهو و ترامب... إسبانيا تتغلب على الأرجنتين</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/naya_foriraq/85108" target="_blank">📅 19:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85107">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇺🇸
ترامب
: أنا بصدد التفكير في هجوم ضخم - أكبر من أي شيء حدث من قبل، وأنا على وشك اتخاذ قرار، وانضمام إسرائيل إلى الضربات ضد إيران سيترتب عليه "عواقب".</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/85107" target="_blank">📅 18:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85106">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">▫️
المفتي العام لليبيا
: الأردن يتستر على وجود القواعد العسكرية الأمريكية فيه وأمريكا تفضح ذلك.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85106" target="_blank">📅 18:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85105">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">▫️
بيان لدول الخليج والأردن:
نرحب بقرار رئيس وزراء العراق حصر السلاح في يد الدولة ونؤكد دعمنا لإجراءات حكومته.</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/85105" target="_blank">📅 18:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85103">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇱
بلدية يفنيه تفتح ملاجئها وسط الكيان الاسرائيلي.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85103" target="_blank">📅 18:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85102">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🇮🇷
🇸🇦
🇾🇪
التلفزيون الرسمي الايراني :
الاهميه الحقيقية لحصار الحوثيين للسعودية ستكون عندما يتم إغلاق قناة السويس عبر اغلاق باب المندب
حينها ستحدث الصدمة الكبرى لسوق الطاقة في العالم.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85102" target="_blank">📅 18:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85101">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو يتحدث عن إحباط خطة إيرانية للتسلل إلى إسرائيل واستهداف كبار المسؤولين.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85101" target="_blank">📅 18:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85100">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سرينا يا رجال الله</div>
  <div class="tg-doc-extra">عيسى الليث - علي الديلمي</div>
</div>
<a href="https://t.me/naya_foriraq/85100" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇾🇪
ورسالتنا لعشائر اليمن الكريمة
#شاركها</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85100" target="_blank">📅 18:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85099">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇾🇪
الرئاسة اليمنية في صنعاء:
لن نتردد في استهداف أي دولة تتعاون مع السعودية.</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/85099" target="_blank">📅 18:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85098">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">الموساد: خلية ايرانية كانت مكلفة بتنفيذ هجمات ضد مسؤولين كبار.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85098" target="_blank">📅 18:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85097">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو يتحدث عن إحباط خطة إيرانية للتسلل إلى إسرائيل واستهداف كبار المسؤولين.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85097" target="_blank">📅 18:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85096">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇱
🇮🇷
اعلام العدو يتحدث عن
إحباط خطة إيرانية للتسلل إلى إسرائيل واستهداف كبار المسؤولين.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85096" target="_blank">📅 18:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85095">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/103d326f00.mp4?token=T28iGbQSE-cfaXug04DignQcdTQkAKXICFtt9l7gdOcrWsEYyzyeHBohc4FA1wwfl0OdvMMUgB0sb5LsIkN0WIA5lQolA8FnAHwWN9sQGDl9wJb7Tp6GGtADe6CiQGN8CprHjgVkTSPv7e26kKkKSHK35HkLxCEdLKi9Ix_g0h951yaiHT9OMI8UlLiTu_ojDBndag1uC-38wrLt9VO65TwEx1vIPg8vAzzh1XbYcEwz3eFkVL9a6SJi5RCOWOIdcC2g2_rRBwUokgu1JpwyXhtxnA4UlBmASbD1V7Zcki4VEA1ow6ZPQ3wP4IfAzmGTYvea-clF6iaeeR1ZVKOqpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/103d326f00.mp4?token=T28iGbQSE-cfaXug04DignQcdTQkAKXICFtt9l7gdOcrWsEYyzyeHBohc4FA1wwfl0OdvMMUgB0sb5LsIkN0WIA5lQolA8FnAHwWN9sQGDl9wJb7Tp6GGtADe6CiQGN8CprHjgVkTSPv7e26kKkKSHK35HkLxCEdLKi9Ix_g0h951yaiHT9OMI8UlLiTu_ojDBndag1uC-38wrLt9VO65TwEx1vIPg8vAzzh1XbYcEwz3eFkVL9a6SJi5RCOWOIdcC2g2_rRBwUokgu1JpwyXhtxnA4UlBmASbD1V7Zcki4VEA1ow6ZPQ3wP4IfAzmGTYvea-clF6iaeeR1ZVKOqpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
استهداف سيارة للدفاع المدني اللبناني من قبل طيران العدو الصهيوني على طريق عام النبطية الفوقا - دار المعلمين وانباء عن شهداء وجرحى بالتزامن مع حديث جوزيف عون في واشنطن عن اتفاقيات مع كيان الاحتلال.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/85095" target="_blank">📅 18:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85094">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📰
وكالة رويترز تزعم:
أرسلت إيران قادة الحرس الثوري ومعدات متعلقة بالصواريخ إلى الحوثيين اليمنيين هذا الشهر.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85094" target="_blank">📅 17:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85093">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/icBJE2HDN2TuqOeSCqUh7x-bw_THVPRhB5xQ86ZJnbn4Ry4iEeSQoQKpguQtVV-wMDo8x8iwFzElUycMbAIhnv7TYuVc6WR71xn81Z2LSW-yvmLvThVm3wBTFcMDlO7fl4eC2zKLxW3cFWRvJmimbkS0Xj20T72ZZmjrXO8-Cl4FhEpVbEmIoPHypYdZPfOi2XLSst9TLNX6-2SfJqVPQosbsFdjMTx5rYPTpti3mpzuVHxsKhPBtA77fAPMEqWvJkDjh5zvfALZ-_jrV_y1KP3L6dlgTNyC_IoeEM1QAcczjna9WXvsHiSQ1h8Zc6Y0H5TnEWLFOsOcJlb4rfijHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هيئة الاعلام والاتصالات العراقية توجه تحذيرا لقناة سكاي نيوز الاماراتية بسبب استضافتها غيث التميمي وتدعوها لحذف اللقاء وتقديم اعتذار رسمي خلال (3) ايام</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/85093" target="_blank">📅 17:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85092">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇺🇸
البنتاغون يقوم بتحديث قائمة المؤسسات التي لديها أنشطة مثيرة للقلق؛ وتتضمن القائمة مراكز أكاديمية في الصين وروسيا وإيران.</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85092" target="_blank">📅 17:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85091">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇮🇷
🇮🇶
توقيع مذكرة تفاهم بين العراق وايران لمدّ سكك الحديد من كرمنشاه - خسروي - خانقين - بغداد</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/85091" target="_blank">📅 17:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85090">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc04871c7.mp4?token=B9oOmiMi6tAirpg5kPRF9X8VhcXEoqYiTS5W6D-SrXhomdI1AN-L4dhtnE82U89k5T_aehy1nPEsyBK2_e7hHtY0ej7nBxbUetxlBcZGQsFhiG_prkDrO4fgIocM6NlDEoOKlwFG1Sem2wFZvX3ak1mJ3TpYOuz8rpVkdIKH3SS-iL6B0ZmLoKFoNhpFh1JX-cCpLGzM5XJKk6KSBvbqg8Cu7Xb_W5wcb_nVMqyTG3dwECXUyMsKK1UuuSrqnWcLdPI3W87hxNnEZI-LBcgiNTjK9tbL4fJLQ0C0m8hPvnD_v7CMV_tDb_rPkX5276nXC3NH13bDizGw_iyJw6idDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc04871c7.mp4?token=B9oOmiMi6tAirpg5kPRF9X8VhcXEoqYiTS5W6D-SrXhomdI1AN-L4dhtnE82U89k5T_aehy1nPEsyBK2_e7hHtY0ej7nBxbUetxlBcZGQsFhiG_prkDrO4fgIocM6NlDEoOKlwFG1Sem2wFZvX3ak1mJ3TpYOuz8rpVkdIKH3SS-iL6B0ZmLoKFoNhpFh1JX-cCpLGzM5XJKk6KSBvbqg8Cu7Xb_W5wcb_nVMqyTG3dwECXUyMsKK1UuuSrqnWcLdPI3W87hxNnEZI-LBcgiNTjK9tbL4fJLQ0C0m8hPvnD_v7CMV_tDb_rPkX5276nXC3NH13bDizGw_iyJw6idDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
صور تظهر هجمات الصواريخ والطائرات المسيرة التي نفذتها الحرس الثوري تحت اسم "يا أبا عبد الله الحسين" وهي مقدمة لزوار زيارة الأربعين.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/85090" target="_blank">📅 17:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85089">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇰🇼
‏الإطفاء الكويتية تعلن السيطرة على حريق منفذ العبدلي بعد عدة ساعات من الهجوم.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85089" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85088">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🔻
حرس الثوري الإسلامية:
في إطار مواصلة معاقبة المعتدي والرد على ما وصفه البيان بجرائم الجيش الأمريكي، الذي قال إنه هاجم فجر اليوم طريق زوّار الإمام أبي عبد الله الحسين (عليه السلام)، مما كشف - بحسب البيان - عن حقيقته وأظهر للعالم وحشيته وقسوة قادته، نفّذ مقاتلو الحرس الثوري صباح اليوم، في الموجة السادسة والعشرين من عملية «نصر 2»، وبشعار «يا أبا عبد الله الحسين (ع)» وإهداءً إلى زوّار الأربعين الحسيني، هجمات مركبة أدّت - بحسب البيان - إلى تدمير وحدة الحرب الإلكترونية الخاصة الأمريكية في قاعدة العديري، كما استُهدفت أماكن إقامة أفراد هذه الوحدة، ما أسفر عن مقتل وإصابة عدد منهم.
وأضاف البيان أن برج المراقبة الجوية في القاعدة تعرّض أيضًا للقصف، مما ألحق به أضرارًا، مؤكدًا أن العمليات العقابية للقوات مستمرة.
ذكر البيان أن الولايات المتحدة، بعد فشلها في ساحة المعركة، تحاول مجددًا - بحسب وصفه - استخدام الخداع للحصول على فرصة لالتقاط الأنفاس وإعادة التسلح، مشيرًا إلى أن المسؤولين الأمريكيين يكررون الحديث في الأيام الأخيرة عن العودة إلى المفاوضات.
وأضاف أن العدو يجب أن يدفع ثمن نقضه للعهود، وأنه لن يُسمح هذه المرة - وفق البيان - للولايات المتحدة باستغلال أي وقف لإطلاق النار لإعادة ملء مخزونها من النفط والذخائر ثم استئناف الهجمات.
كما جاء في البيان أن الجيش الأمريكي، الذي كان يستخدم صواريخ كروز تُطلق من سفنه في المحيط الهندي بعد استئناف الحرب، لجأ أمس إلى استخدام قاذفات B-1 المنطلقة من قاعدة فيرفورد الجوية في المملكة المتحدة، بعد نفاد مخزون الصواريخ على تلك السفن.
وأكد البيان، مستشهدًا بتصريحات مسؤولي وزارة الخارجية، أن أي قاعدة تُستخدم لشن هجوم على الأراضي الإيرانية تُعد هدفًا مشروعًا.
كما وجّه البيان تحذيرًا إلى المملكة المتحدة، متهمًا إياها بأنها كانت السبب الرئيس في معاناة شعوب المنطقة، وبأن سجلها يتضمن - بحسب البيان - تقسيم الدول الإسلامية، وارتكاب مذابح واسعة، وفرض حكومات استبدادية، إضافة إلى تنظيم وقيادة احتلال فلسطين وإقامة إسرائيل، واتهمها أيضًا بالمشاركة في الهجمات الأمريكية والإسرائيلية الأخيرة على إيران، محذرًا إياها من الاستمرار في ذلك</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85088" target="_blank">📅 17:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇮🇱
مكتب نتن ياهو: انضمام المملكة العربية السعودية إلى اتفاقيات أبراهام سيكون قفزة تاريخية إلى الأمام نحو تحقيق السلام في منطقة الشرق الأوسط.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85086" target="_blank">📅 16:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامب يقول ان الموافقة على النووي المدني السعودي كان بشرط تطبيع السعودية مع الكيان.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85085" target="_blank">📅 16:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85084">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رئيس الوزراء العراقي: أمن العراق وإيران مشترك ولن نسمح بوجود أي تهديد لإيران ينطلق من الأراضي العراقية</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/85084" target="_blank">📅 16:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85083">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHCImkytt4A5yr5YqKjSUGHtzf4EAG7eSQqRuBpIkukTiY859o0kPfnk3Nsn6oe0iRZSALiITPj5VJMFY8M_OJ_w_aTVbx7jhNCmBkbJ1y4FBdGYbsCHPDUFYNlEIIE5pB3CspmMw5eLQy6KRG6lWW93AQCta23Gsw1tVlmkVBjtXhbNL5mxA2CipeDi3vpIhGPyGrlwp3GUOLhvv-V6cjdsa_pfiYTngflzICgy0Dx8bgV-mpUOFuyMN9957DX5vFPSA747Vrk0uLK3tjCO2QkKUDsgSfDpSwoRweDlcZnGG5gdmngks87ZB_e3pviVRXqcDVM8cYaRPxyD2nzZEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسعار النفط تتجاوز الـ100 دولار للبرميل</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85083" target="_blank">📅 16:39 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85082">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الصين تصدر تحذيرًا أمنيًا لمواطنيها في السعودية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85082" target="_blank">📅 16:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85081">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3RldCEbueBfXFhX37TufatLq6A-VupUMk6VJ8e1Vsozi9wrbSWzQAO1RKGPfym8SvFZJRxy3qZclIilpmpP6ZwhAnhbGzICRCjiDZSqegoZEmjkCWQuogiP0M3JZ3f5AxICv1ozrP_OvaD09wRwTuuLzk3vVKQZ74TGebY504mVlmC6AQ-umET44ZyMkxbB6ZhdeqHSCHGO_SoViS57XDChhxz-QLP-vW3Pt-yhCluRqC1o_Mpoh54KfJihAvKtoAPP-edrlwp_UOfV7_Z1o5Y0BgaL72AaLkzpatUXNNagTGlDAR7JXOIaUJpf3fopopUFYULPRbBUr1dK7x5Uxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد مخبر مستشار ومساعد قائد الثورة الإسلامية:
سعر النفط الذي وصل إلى 100 دولار حتى هذه اللحظة هو نتيجة لتعطيل عملية نقله فقط، وليس نتيجة لزيادة الإنتاج. الحريق الذي تشعله أمريكا في حقول النفط والغاز في المنطقة سيشتعل ويؤثر على جميع أنحاء العالم. قواتنا المسلحة بالتأكيد، وبمبادرة وذكاء، ستحدد مستوى التحدي "درجة أعلى" من مستوى العدو.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85081" target="_blank">📅 16:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‏فرنسا تدعو انصار الله إلى وقف الهجمات على ناقلات النفط السعودية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/85080" target="_blank">📅 16:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85079">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/px8ie1sr13XmWm_dHj1sg84CvkhOtXPofg8mOLor5AMwvLx6786QEIF8mjt5UpIodgRscov0bUGX4K29YT9zOlibsmNodqQJZECLDFmjMbWuVvQhhXw2g367QRoKi6Xh_7h9l2XR0rM2F93vcBsdjbMi_LmqEYu58O1-u58sDJJa0HKp88mGOs_K-NXHwvCGhGOVZLEXKgcu156V4FRvW0AezutNL6-m0frwpw8QQCgQrOMfQqgCOISJSyGCcKOFn2p9qChaMdhvY5WaYeCXNM8MruKBysUl4JsBdzFSPtd4C9-0JqyE8i3ybRYnlIuuVQB3Ei3TB-uC5QrWAttyjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇭
نظام دويلة البحرين يعتقل الرادود الحسيني علي عباس الدرازي ضمن حربه على الطائفة الشيعية.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85079" target="_blank">📅 16:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85078">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">عملية طعن جديدة قرب جنين</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85078" target="_blank">📅 16:13 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85077">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">عملية طعن جديدة قرب جنين</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/85077" target="_blank">📅 16:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85076">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f-L4_g_AnLbGbBxWrQ5-E7VERzG4IZos1fvex3J8i7VMxat54ZU9Dw776hk8diS0i3BGojVRbog_it7HPl_sHLXBj0MISKGEGs1YKtkaWQiFFA3h5QWOGVkVkcUwk5SNFqee3-Lay08VYq1H_kaBM_DewFe6rcxRoqsRtNHMzM1-yY54NaMEhhXae8XLikqnaLYebbFPWPofkMEZEjIZsIItWuXZ_b5qpsGMYav_S8eW7UO-XvoDRruHjRvvzzi41g-iei2yusf86x72-R5XoGQIi5Dt-HwcNPUCubL2vS3AQUxEz4nSyNUmptOSFWE1WjKNFK8PZKka17SRBQk47Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
قبل عام، شنت الولايات المتحدة الأمريكية هجومًا قويًا على الحوثيين لتدخلهم في التجارة، وذلك بإطلاق النار على السفن. ومنذ ذلك الحين، وخلال نزاعنا مع إيران، تصرفوا بمسؤولية كبيرة. وللأسف، عادوا الآن إلى أفعالهم، حيث أطلقوا النار على سفينتين سعوديتين الليلة الماضية. أرجو أن تكون هذه الحقيقة دليلًا على أنه إذا كرروا هذا الفعل، فإن الولايات المتحدة ستُحمّل إيران المسؤولية، باعتبار الحوثيين وكيلًا أو ممثلًا لإيران، وسيتم إنزال عقاب عسكري كبير بإيران، وبالطبع بالحوثيين أنفسهم، الذين أشعر بخيبة أمل كبيرة تجاههم لأنهم تصرفوا حتى الآن باحترافية وذكاء.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/85076" target="_blank">📅 15:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85075">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ed6c7ae4.mp4?token=sqlilcAbMPmA-e_s_CWuggi1Wzj326EOF2zsJJwvNorFcbEuvp_ZOCwNAm8HyN7-c4Ay1XPqFgx2MqUfnIalui7Jn6mNhiV_aMCW1leDU0Cy050npTN2CuzZwpIGei_1dthyHlytYXYSYPcVNPx5CzzkYf5etqB7oOTyzyKXHKuWt3g1yu4HU6UzyF3qnxeEM8qszNPzn7xJrB-EgLcYsQtwwsJV96ixCyRmwCcutvqzi9MRtB3IVD0zXz8bk5WTukhx5Y_Gv6aENmUekPdTB0qwJKQqNvBNCD1xYcXBlVsHuuH4A72W0qYwrKpjuITyExfpJzijDnRXypQ6eXrRHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ed6c7ae4.mp4?token=sqlilcAbMPmA-e_s_CWuggi1Wzj326EOF2zsJJwvNorFcbEuvp_ZOCwNAm8HyN7-c4Ay1XPqFgx2MqUfnIalui7Jn6mNhiV_aMCW1leDU0Cy050npTN2CuzZwpIGei_1dthyHlytYXYSYPcVNPx5CzzkYf5etqB7oOTyzyKXHKuWt3g1yu4HU6UzyF3qnxeEM8qszNPzn7xJrB-EgLcYsQtwwsJV96ixCyRmwCcutvqzi9MRtB3IVD0zXz8bk5WTukhx5Y_Gv6aENmUekPdTB0qwJKQqNvBNCD1xYcXBlVsHuuH4A72W0qYwrKpjuITyExfpJzijDnRXypQ6eXrRHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
🇺🇸
صور الأقمار الصناعية التي تم التقاطها اليوم تظهر أضرار لحقت بملجأ طائرات الهليكوبتر في معسكر بوهرينغ التابع للجيش الأمريكي في الكويت في أعقاب الضربات الإيرانية الأخيرة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85075" target="_blank">📅 15:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85074">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرنسا تخلي فريق سفارتها في طهران</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85074" target="_blank">📅 15:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85073">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXWq_eK_tcMz2yU6wlmZsc0xY1DHk-Hri2LZCHDS33Z_V9pi8HHD8yIBhkiz4LDhuYzeiBHG247wSF89MYakwuM_o9Ua6JXPgrX7eawTcI13RUTUJM-BCowVhTkI-ehxwG8xwiVyBB-DolL-I6-LGfD3GkpxwDudOW_9BBAmsZKPpR3fFvmhdSEUbyVX79bfp02W0kfKFTupCxGOT6KlS_oI4Y3zARY3hx9EOlOzZ_F1zerrlNmAZu1_N1mgp0p7_Mtc_kKXHqXtmJqtPwqxxQiVetkhotG5oKhv-n_UknT1bhpF6X4W4aW4QrE3v_-uw6Qv_5y4zDDWwPj6gi-Rww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسالة مهمة بعد قليل نسترعي الانتباه</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/85073" target="_blank">📅 15:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85072">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رسالة مهمة بعد قليل نسترعي الانتباه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85072" target="_blank">📅 15:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85071">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🇮🇶
عراقياً
فراس مجيسر عضواً في مجلس النواب بديلاً عن حسن الخفاجي الذي حكم قبل قليل سنتين من قبل القضاء العراقي</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85071" target="_blank">📅 15:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85070">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OMVP2kfufZDmjgSBO2pXdZyAYmeQ4uCQahBDzUTGhZ9agfUwJVqn2S_lr9NiOXfngcPf2w82zGnAK4OROD9o_RSzzVCQQwPHtjTzdlehBu1qM9jGd7_Nl0OU9mgVEtyl6mt4OKd1Xzk5Lz1oZc4aPX7UL0Ak4FHzybdpk1Cj0ahUGLqCKQgc3pcyeH-446LDzqGGIeM6WCbK6qeZ6D7YEt5X0wEZWPU3Y1e5LtFEgHkaqkjhKl_OSCqJvlKg--9YDt3dMT-iP3wgK0cljj0r51KeSP-WBdNHnMdEp5rQ-P65CgZtrfoza44IH1aP-GL3TXy4vr08Us4-xKT5I9mf5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏ترامب: الولايات سيتم الموافقة على الاتفاقية النووية المدنية بين وزارة الطاقة الأمريكية والمملكة العربية السعودية، والتي تتعلق فقط بالاستخدامات غير العسكرية (لن يكون هناك تخصيب للوقود!)، ولكن بشرط مشاركة المملكة العربية السعودية بشكل كامل في اتفاقيات أبراهام…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85070" target="_blank">📅 15:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85069">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏ترامب: الولايات سيتم الموافقة على الاتفاقية النووية المدنية بين وزارة الطاقة الأمريكية والمملكة العربية السعودية، والتي تتعلق فقط بالاستخدامات غير العسكرية (لن يكون هناك تخصيب للوقود!)، ولكن بشرط مشاركة المملكة العربية السعودية بشكل كامل في اتفاقيات أبراهام الموقرة والناجحة. الولايات المتحدة ليست ضد المنشآت النووية المدنية (غير المخصبة).</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85069" target="_blank">📅 15:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85068">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">‏الجيش الكويتي: منفذ العبدلي مع العراق تعرض لهجوم بمسيرات معادية</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/85068" target="_blank">📅 15:20 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85067">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔻
الاعلام الرسمي العراقي يؤكد ما انفردت به نايا: الجانب العراقي تلقى إشعاراً من الجانب الكويتي بإغلاق منفذ العبدلي الحدودي بشكل مؤقت بعد تعرضه لقصف بطائرة مسيّرة.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85067" target="_blank">📅 15:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85066">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دوي صافرة الإنذار داخل قاعدة التوحيد الثالثة في السفارة الأمريكية بالعاصمة بغداد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/85066" target="_blank">📅 15:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85065">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/690c07aa39.mp4?token=v8x7jNQR4EzNm-TRRqmPUx75C-VoehBXW9tu6IE0So2gJd0fCGyjnSGKpEiSdC1X9Rjr1U1hlMunailF3irfE4mScVE6e5ETSRVmDqHfDGiXU_lzcFKyIKruBrMpXNB1TMnoSy6rfHL_aT3-sAySEof6XXy3PruLVlktsvs_YQPwKuafieIwN7f2EEgKHhrXvdiO-F-m4vj62LXBnSl8cuhIAvQUI_KwsvsJ6yQTtrxmsVMkwbjqtCvnm0P0kryeKpMz6J1vQwC-GCU3pC8SvIXtkk8b22fAz3dxxdQUPlgOh18CPpUNv30DuGzcq1iTIRlrRZWf0L-lEgEs6q6FZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/690c07aa39.mp4?token=v8x7jNQR4EzNm-TRRqmPUx75C-VoehBXW9tu6IE0So2gJd0fCGyjnSGKpEiSdC1X9Rjr1U1hlMunailF3irfE4mScVE6e5ETSRVmDqHfDGiXU_lzcFKyIKruBrMpXNB1TMnoSy6rfHL_aT3-sAySEof6XXy3PruLVlktsvs_YQPwKuafieIwN7f2EEgKHhrXvdiO-F-m4vj62LXBnSl8cuhIAvQUI_KwsvsJ6yQTtrxmsVMkwbjqtCvnm0P0kryeKpMz6J1vQwC-GCU3pC8SvIXtkk8b22fAz3dxxdQUPlgOh18CPpUNv30DuGzcq1iTIRlrRZWf0L-lEgEs6q6FZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇰🇼
صور الأقمار الصناعية الجديدة تؤكد وقوع أضرار جديدة جراء الضربات الجوية في قاعدة علي السالم الجوية في الكويت بعد الهجمات الإيرانية اليوم. ‏دُمرت عدة مبانٍ، يُرجح أنها كانت ثكنات للجنود، ولا تزال أعمدة الدخان تتصاعد من الموقع.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85065" target="_blank">📅 14:57 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85064">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">يوم القيامة في الجانب الكويتي   إغلاق منفذ العبدلي وخروجه عن العمل</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/85064" target="_blank">📅 14:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85063">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🇮🇶
🇮🇷
وزير الخارجية الايراني عباس عراقجي: خلال المشاورات مع المسؤولين العراقيين، سيتم بحث ومناقشة موضوعات مثل اتفاقية التعاون الأمني بين إيران والعراق، ومسألة زيارة الأربعين الحسينية، والقضايا الإقليمية.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85063" target="_blank">📅 14:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85062">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇮🇶
🇮🇷
وزير الخارجية الايراني عباس
عراقجي:
خلال المشاورات مع المسؤولين العراقيين، سيتم بحث ومناقشة موضوعات مثل اتفاقية التعاون الأمني بين إيران والعراق، ومسألة زيارة الأربعين الحسينية، والقضايا الإقليمية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/85062" target="_blank">📅 14:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85061">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51fa914cc2.mp4?token=jlWeIbjCgQWseuB7CKkzohFH6dUrJBGMBCz3aXB_xGzw7KIzfLbF2w1No_Px_1Uv84o29Aupgl_dEB5RGbzva0odhe4v1a4c3CdumESSNbWgf71fgm65nU9cZOszM675LK3gn1JwK63k9ETT2abg24Yp2oez3nRgx0Xl6K64_r6pKywQEdwynq1R1dTt3Wwm2Ym6--KIowB2yXL-CowwIWXvfkKdI2V4kZPlUys6NmBpLjciIrlPHRB6suchok7CzTasERr3dabED4Dksw2XhjdDWA8iuCNDYSRhJ0lchowmeNL1voogmfN5TOIQumxDtcVJSsNeVzawDw2c_hyfBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51fa914cc2.mp4?token=jlWeIbjCgQWseuB7CKkzohFH6dUrJBGMBCz3aXB_xGzw7KIzfLbF2w1No_Px_1Uv84o29Aupgl_dEB5RGbzva0odhe4v1a4c3CdumESSNbWgf71fgm65nU9cZOszM675LK3gn1JwK63k9ETT2abg24Yp2oez3nRgx0Xl6K64_r6pKywQEdwynq1R1dTt3Wwm2Ym6--KIowB2yXL-CowwIWXvfkKdI2V4kZPlUys6NmBpLjciIrlPHRB6suchok7CzTasERr3dabED4Dksw2XhjdDWA8iuCNDYSRhJ0lchowmeNL1voogmfN5TOIQumxDtcVJSsNeVzawDw2c_hyfBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
لحظة إطلاق الصواريخ الباليستية "حاج قاسم"، "قدر"، "فتاح"، والصواريخ المجنحة "باوه"، والطائرات المسيرة "شاهد" ضد القواعد الأمريكية.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/85061" target="_blank">📅 14:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85060">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🇮🇶
محكمة جنايات مكافحة الفساد المركزية العراقية تصدر حكماً على النائب حسنين الخفاجي بالحبس الشديد لمدة سنتين عن جريمة الابتزاز بمبلغ قدره (500,000) دولار فضلاً عن تسجيل نسبة (40%) من مشروع حوراء بغداد السكني لمصلحته باسم أحد العاملين في مكتبه.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/85060" target="_blank">📅 14:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85059">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اغلاق منفذ سفوان من الجانب العراقي بعد تدمير المنفذ الكويتي المقابل له</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/85059" target="_blank">📅 14:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85058">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇨🇿
تحطم مروحية تابعة للجيش التشيكي ومقتل عدد من طاقمها.</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/85058" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85054">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآية الله السيد مجتبى الخامنئي</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RgXIGIxfRuV5ZIVpgN7WUd6Mheg_5V_aiTX_6kE9toTwH3o_QQ1B686NSU1GtxNjLfpMAb8QF1KKJVzXZ-GYp5LC3mkj-sxZ2doDCrsRQNgGJxhBHIY0vJAYB0Bxm-9E8XmmFoDzWWybzV1qW9EjrRRaf30k5jC5Uh7GlcPMMYdoVMLdiezIdU8w1moIlc-g5bmKTAvIXYnH0l9oZTbmuM6c-2cEyCf4zXfWUP6FNJM5FHzFZ5T5FfsQiHwHoyJ27TdeNiTPOsSeaoQyq48wtdadYK_QNSKSkjC9q7b1bRz0jQ39PHC2PfeKuU_XETPG45L9Q3wEIDemplkTAOyI2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oiaNgptFXUOBAJzM60t7lAusvqeB2V8tUFFQDOLghLy0GrO-gWkuo_rtS0D0CgLKmq35dSovGxWUHjQCItkyynCTgXUD58WTAY_r9L5OQ6B-14U-gMIgMzYe3UWvtKmZ12GMd5SZpL9H0YsbNHtysSwrbGNUNlWwROLSQ5rdeJPRnXdTUzYM6ornvlsfogTJiqNwP4LuQM-CJz4vh_DH6usER5TUfdNYcwaCxyD39G3_Tz54LI2L7iRQScT2URotEsqIHshuJA2WmhiOHCblwGOetEskKw_IC0w3tOp3BmNOMwB9HxkVx-QEG6ajMlmzjqGPUuV21sfBfpUX_VJRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fyRc-zXpOB2X-9XUYf119dLhCipJgkKP0vBRCgdERS-YKuPhFC7lc0qgDQYbLLntO18zHQGTj8XUAq942NXtbshJk2-puYa5RbwPctwZEsn2Nyc7mbKevdzkwzxKkWlymbOp9fUwtTUuUYrGtJcZKHWmuUO-j2QuieDp6_DQqewbjSz-YZow_oCT4F4_LwQGkmuX413vOCDhi6H7-KOKsmEPwtPQUJapOqWuk-OrdUfk7N30Cir3dniMR5NqakHW0_U1mUINqNu0hdXRbpcjkXrm5KzsDfyFg5U_9DWX8csLi0voxBtL09dFceW_BkF7D7Ol86DBrnLrY2MzfxdBSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xf27GW2NX-bH86i51Bv3JEnUieE0BuVDPBBHADSJFTvf-s3FX700AUSMOkVHSWJO8fugWbIWxK3RlYuScPxQViJrH9VgP7qCrJ5dP2oizLnFNa6bTw7InDlOJ6RiTFvxn-9V13sa5-PvPKICSDsXTBz2hn4o2oYFT4YDzF-RZjDPt6BXsiD4aIqWKXRad7c1qMdZ9DMMmJjXOAGSt-nHiD5VUpm7qdGAl6l5fMy2xaMGSaskko1AnVm43nSe6U8Fh1sAokLNHUL8LPQ9sb5GHezub13xyz1OvxlCwjlmTG8h3_K2g8Xo7qNPGUKEUdNex3X7Hn5FLQ2A22ESE82KLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🖼
لا ريْب في أن قادة الاستكبار قد ارتعدت قلوبهم هلعًا..ورأوا كيف ذهبت تلك الأموال الطائلة التي استثمروها لتخريب العلاقة بين الشعبين [العراقي والإيراني] أدراج الرياح.
🛑
مقتطف من رسالة شُكر آية الله السيد مجتبى الخامنئي إلى شعب العراق بشأن تشييع إمام المستضعفين | 17/07/2026
📍
بغداد - ساحة التحرير
🏴
#قوموا_لله
#تشييع_إمام_المستضعفين
📲
t.me/mkhamenei_ar</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/85054" target="_blank">📅 14:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85053">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اعلام العدو: فتح الملاجئ في الجليل الاعلى</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/85053" target="_blank">📅 14:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85052">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">يوم القيامة في الجانب الكويتي   إغلاق منفذ العبدلي وخروجه عن العمل</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/85052" target="_blank">📅 14:32 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85051">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
شهود عيان لنايا:
طيران حربي يجوب اجواء البحرين.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/85051" target="_blank">📅 14:26 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85050">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60bbe27969.mp4?token=ra1rmb9Xxnd_4L6S57LWwiTPo7Zd2aTZZ4rA6tmQyMmCMkgyfm2AsVQrVP_0XzflbBaPG5yTzNHPqs0XKo_si4fjW2EWLoG1TbLFTnaNjPhOR2XyocP5tfUz2WTdY1j5ve3dLwkphCeWOoJF8U_Sjk-4dPiywkvJKsCf_pvMybHTTNBTw-r4081GjWIcyN9wUPPdzm_fiK2TGfiDhJq0lTkFs6q1U7vhlYrXe33QsfkPo1XJND1TQLB_tZSCZ4Xb8Ch90AwUwMIz2Fa0QYFznpqxwVWFrLX4bPpkNKgnk6NdGqluVCMenFzp0Meof-SShOOm9I92ycr3njE1aHh33A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60bbe27969.mp4?token=ra1rmb9Xxnd_4L6S57LWwiTPo7Zd2aTZZ4rA6tmQyMmCMkgyfm2AsVQrVP_0XzflbBaPG5yTzNHPqs0XKo_si4fjW2EWLoG1TbLFTnaNjPhOR2XyocP5tfUz2WTdY1j5ve3dLwkphCeWOoJF8U_Sjk-4dPiywkvJKsCf_pvMybHTTNBTw-r4081GjWIcyN9wUPPdzm_fiK2TGfiDhJq0lTkFs6q1U7vhlYrXe33QsfkPo1XJND1TQLB_tZSCZ4Xb8Ch90AwUwMIz2Fa0QYFznpqxwVWFrLX4bPpkNKgnk6NdGqluVCMenFzp0Meof-SShOOm9I92ycr3njE1aHh33A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">يوم القيامة في الجانب الكويتي
إغلاق منفذ العبدلي وخروجه عن العمل</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/85050" target="_blank">📅 14:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85049">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اعلام العدو: فتح الملاجئ في الجليل الاعلى</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/85049" target="_blank">📅 14:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85048">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c6c7a1b6b.mp4?token=Tvy2riEGKXvRHAe_lJJFz6HvLbZg12XLt-JfWyAJtHmwVvxiPu3zDQ1HkVnPKyCDQndE-TTN2C6P3cChjrTqdkDX4gjBv_nYnlrOqB0LhqJ4G2Wb14v37MOar0jc8geJJxTfTPKdJdvq_JK85m49YDh6ZEbOJfLSITGqgl-yiMQ7NfRTbrPYU_K1Z15JQvsFkuW4n6b5u3ekI-okh_dvvB42G89f_JKjXxA_j69fzMqOX6z8Z3Dn4mdxDmWVlZ00WNcF4sM7jQd9_-ACOUIwv1mSUdl6uIn-O0K1zlJ_he1cv21B3LvmYMkvOhe55p7gIOctYhaabo-YY1sU1NZmFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c6c7a1b6b.mp4?token=Tvy2riEGKXvRHAe_lJJFz6HvLbZg12XLt-JfWyAJtHmwVvxiPu3zDQ1HkVnPKyCDQndE-TTN2C6P3cChjrTqdkDX4gjBv_nYnlrOqB0LhqJ4G2Wb14v37MOar0jc8geJJxTfTPKdJdvq_JK85m49YDh6ZEbOJfLSITGqgl-yiMQ7NfRTbrPYU_K1Z15JQvsFkuW4n6b5u3ekI-okh_dvvB42G89f_JKjXxA_j69fzMqOX6z8Z3Dn4mdxDmWVlZ00WNcF4sM7jQd9_-ACOUIwv1mSUdl6uIn-O0K1zlJ_he1cv21B3LvmYMkvOhe55p7gIOctYhaabo-YY1sU1NZmFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العراق يعلن استئناف العمل بمنفذ الشلامجة بعد توقف مؤقت بسبب القصف على الجانب الإيراني</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/85048" target="_blank">📅 14:12 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85047">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfFZ4tdB6LQCJ50XlwyC2PDfmmB5FNmtYPx1ObMWcUrVZvsbx5yUQMSFiZjsdKdOBb1JhCDCkRd6LNLQt_Tkv6SAkndnInjmwAUGg1RDAV3u2qI7l6RqKu5JX4gmMTyl4JVQbHt4xD6oeH4v-uW5WeTL22DoPBNtOxpD_kshnCX2Mecswdo2_KSB36bUo77co70hg1iLv8lPwaKkqkyvJTyQQmGNUQgbX5uL66bx3Bs9g9svhwN6NrUibmOXjA0FiJHvwUbSybi3xrSJDvdYdz2Gh31XBPxh7zK8eqO_MX1Pu0RtyCsvrI3EK5paqti8ACQyeT5tNa9NGgJdezjQow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشاهد من الانفجارات في منفذ العبدلي</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85047" target="_blank">📅 14:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85046">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18e775f6a.mp4?token=MmxQlI2Hie88CoNHlQAtSKN7_k6kuT4dY-KSIAbcKmR6R7sczt0ZH5e4X5w1Dv-ILhSm9m1CFL8N_-nCwrqZwxzn0Kk7qO11SXvWRTrCrDQZW7HJIP2RNQ2kKXlMw_G6oTJ0bq_lPbv99mvdAykPbwa9jjSBrRlS-4CziEv-_cs50bDLMNLTgJ2OzC7LN2gbOqu-26qSb2Xb_ihMuo2oXOw6g8yxhAdRCk2qLisDhpVQEI1nz9BThvQGQsdwEjl9t8s8H5bu9_FWRMX-2zBYWtNEZ2VFnbE_gBXprwMXh8AIh8Lq1YbuAuX-TEn7RaK2E5oI8HnndLi0tXt5ZFdnww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18e775f6a.mp4?token=MmxQlI2Hie88CoNHlQAtSKN7_k6kuT4dY-KSIAbcKmR6R7sczt0ZH5e4X5w1Dv-ILhSm9m1CFL8N_-nCwrqZwxzn0Kk7qO11SXvWRTrCrDQZW7HJIP2RNQ2kKXlMw_G6oTJ0bq_lPbv99mvdAykPbwa9jjSBrRlS-4CziEv-_cs50bDLMNLTgJ2OzC7LN2gbOqu-26qSb2Xb_ihMuo2oXOw6g8yxhAdRCk2qLisDhpVQEI1nz9BThvQGQsdwEjl9t8s8H5bu9_FWRMX-2zBYWtNEZ2VFnbE_gBXprwMXh8AIh8Lq1YbuAuX-TEn7RaK2E5oI8HnndLi0tXt5ZFdnww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجارات في منفذ العبدلي</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85046" target="_blank">📅 14:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85045">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50af4d9d9d.mp4?token=n9s9ugq56I5pxGXUxF9aHFqh6ut0zODoeLzvXj8faxL3_xl_I8vITBMjoRT7tVkOTL9wBRllyHUMuhvbR19fttIp1IzsiVsdfQ0gz75d8UWeXXIzLOKdo91zzegirmjWCSdvXolWwNnunv2pZ0o_yl9Z57DzaG6sEbJ3ps_fFT3pYCKlPI_NY-8qtjpegZvrcnLzYslWK9TCrWb301hVgOFKfl5vtbUwrv2fhVSqZarAxhC4PcKiu2ohTIdNl0OIJwifeTfoiSc60ZYR6BlT25Wxnldo-u-eSsFLTGP792yq1ZQVNacX0cQYHLD9MfmycUV9xNUe5bC4c4wY3BWrIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50af4d9d9d.mp4?token=n9s9ugq56I5pxGXUxF9aHFqh6ut0zODoeLzvXj8faxL3_xl_I8vITBMjoRT7tVkOTL9wBRllyHUMuhvbR19fttIp1IzsiVsdfQ0gz75d8UWeXXIzLOKdo91zzegirmjWCSdvXolWwNnunv2pZ0o_yl9Z57DzaG6sEbJ3ps_fFT3pYCKlPI_NY-8qtjpegZvrcnLzYslWK9TCrWb301hVgOFKfl5vtbUwrv2fhVSqZarAxhC4PcKiu2ohTIdNl0OIJwifeTfoiSc60ZYR6BlT25Wxnldo-u-eSsFLTGP792yq1ZQVNacX0cQYHLD9MfmycUV9xNUe5bC4c4wY3BWrIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر
منفذ العبدلي الكويتي يحترق بنيران حرس الثورة</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/85045" target="_blank">📅 14:03 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85044">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الشلامجة مقابل العبدلي
والعين باربعة عيون
بيت ابو يمعة صبرا</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/85044" target="_blank">📅 14:01 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85043">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmiafOTik4wY-IkkwA4K2Evuj-Xt69zcyR8HsXAVdSuMzx_2xa6xsd2ju4iK3AYzaiH0ykcv1JKG2uc29XCOxIoV3CsbmtyZDoynjS1GrTS0TGXxhqUrMLnpTKunNWpzsMrg0JQPTX4khQRDenpMXzbyM92P-GfuaV7kb2unwpEZcQZ5hyROjahCMUHoGmbG7YOguBr3FJSPfxYwgQ4jr4i4HIpUDuZhIgI9HFs18hjtTkFQKeijGVdX01zYQ3kHZmuE1ZEAr3QXSoZlyRH9sx0OrHYRi-C6qtMinNBUP32jDrOxR9zXR1DXBXIQWZ-BEIQeHLalyVXAiAL-eMFd0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعمدة الدخان تتصاعد من المنفذ الكويتي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85043" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85042">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3517028276.mp4?token=Bv7OT-p2pfqy3RFVYQ-kAm8PYPa3NxxORSN26Ph59ZOrCYkMF0kA5piSGNnNDFniVvFOiCQwftm7DCHQk11OHrREJO9y1ZD2Qh8EuXH54qz0AKYy6h0K7db-bji__71jJz7ib-3dPt_oLLFeHY67UjYT2rdkvE19dDmXIqaO3Q3PyxeOSwkn34QMqQKt42MoEzgKyGR3DsQCPl4tc4wsVJfAe8uRWEv-wTkonCYqiXINQkLlDDlgEWVWK8AUJZ8AINa7vJUIyf6SJ4psqwzzvnlCZQkgPKCv00EPOKqXBCrt70A-D9G_oOch2h1GPrUPHtlBZ2H6R7Ji0OMsDSG8ujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3517028276.mp4?token=Bv7OT-p2pfqy3RFVYQ-kAm8PYPa3NxxORSN26Ph59ZOrCYkMF0kA5piSGNnNDFniVvFOiCQwftm7DCHQk11OHrREJO9y1ZD2Qh8EuXH54qz0AKYy6h0K7db-bji__71jJz7ib-3dPt_oLLFeHY67UjYT2rdkvE19dDmXIqaO3Q3PyxeOSwkn34QMqQKt42MoEzgKyGR3DsQCPl4tc4wsVJfAe8uRWEv-wTkonCYqiXINQkLlDDlgEWVWK8AUJZ8AINa7vJUIyf6SJ4psqwzzvnlCZQkgPKCv00EPOKqXBCrt70A-D9G_oOch2h1GPrUPHtlBZ2H6R7Ji0OMsDSG8ujzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من منفذ العبدلي الكويتي</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/85042" target="_blank">📅 13:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85041">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجارات في منفذ العبدلي الحدودي</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/85041" target="_blank">📅 13:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85040">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/85040" target="_blank">📅 13:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85039">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fa0db633e.mp4?token=qLX64Qo7HZ4A1jsu8wpWGTmOMQoYSB8oVCsSy_wl9FgPgPtG53EYdlqIPYNM-Gw02lWyr1Y8O_RwBwzRNQsN2as0OuEQDLTy_KbY-0yyjkJKCY4fa6yhImdOEBCao3b28gN8mqaOpl_dw2O0S5xdN0vNzh1Jc-L-9cTaekkTn7lolKjNTaFZBRo65CgMoQuEIyRSJlFbPhy3SgWVfCP7-Sljjzh3SafNTtpfN63qsDD2EDaiUKJcLpw7xYJoyKTFlZn7iA-pQQ77M0UmX2439DxxkhgtP6ZGhPKJdmV7IFqGvvj3eBPmApqFbE2f1txQ3xyicwiF0d0IAtl_-HoGEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fa0db633e.mp4?token=qLX64Qo7HZ4A1jsu8wpWGTmOMQoYSB8oVCsSy_wl9FgPgPtG53EYdlqIPYNM-Gw02lWyr1Y8O_RwBwzRNQsN2as0OuEQDLTy_KbY-0yyjkJKCY4fa6yhImdOEBCao3b28gN8mqaOpl_dw2O0S5xdN0vNzh1Jc-L-9cTaekkTn7lolKjNTaFZBRo65CgMoQuEIyRSJlFbPhy3SgWVfCP7-Sljjzh3SafNTtpfN63qsDD2EDaiUKJcLpw7xYJoyKTFlZn7iA-pQQ77M0UmX2439DxxkhgtP6ZGhPKJdmV7IFqGvvj3eBPmApqFbE2f1txQ3xyicwiF0d0IAtl_-HoGEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
الرئيس الايراني مسعود بزشكيان يستقبل رئيس الوزراء العراقي في طهران.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/85039" target="_blank">📅 13:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85038">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇱
اعلام العدو:
تم الإعلان عن حالة طوارئ في مزرعة "ديرخ أفراهام" بسبب الاشتباه في وقوع عملية طعن. هناك مصاب خطير في منطقة الصدر.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/85038" target="_blank">📅 12:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85037">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تصاعد اعمدة الدخان من قطر</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85037" target="_blank">📅 12:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85036">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تصاعد اعمدة الدخان من قطر</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/85036" target="_blank">📅 12:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85035">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/85035" target="_blank">📅 12:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85034">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/85034" target="_blank">📅 12:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85033">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔻
حرس الثورة يوجه رسالة الى الشعب الكويتي
أيها الشعب الكويتي الكريم والنبيل،
إن إخوانكم في الحرس الثوري الإيراني، في سياق معاقبة القوات الأمريكية التي تقتل الأطفال بسبب تدخلاتها في مضيق هرمز، نفذوا هجومًا بطائرة مسيرة ضد مستودع كبير للمعدات العسكرية، ونظام دفاع جوي "باتريوت"، ومخزن للطائرات بدون طيار الأمريكية من طراز MQ-9 في قاعدة علي السالم الجوية، مما أدى إلى تدميرها.
كما هاجم إخوانكم أيضًا أماكن إقامة القوات الأمريكية ومخزنين للمروحيات في معسكر العودة. قُتل أو أصيب عدد من القوات الغازية، وتضررت عدة مروحيات وطائرات بدون طيار بشكل كبير.
كما استهدف المقاتلون برج اتصالات ردًا على الهجمات الأمريكية على أبراج الاتصالات في إيران.
في بعض الأحيان، يُزعم أن إيران، من خلال هجماتها، انتهكت استقلال وسلامة أراضي وسيادة دول أخرى. هذا الحكم خاطئ تمامًا. من وجهة نظرنا، فإن استقلال وسلامة أراضي وسيادة حكومتكم تحظى بتقدير كامل.
ما هو بالضبط القاعدة الأمريكية داخل دولة أخرى؟ إنها مكان يمكن للأمريكيين - وأي شخص يختارونه - الدخول والخروج منه دون الخضوع لرقابة حدودكم. في بعض الأحيان، يتم نقل أسرى من دول أخرى إلى وإلى هذه القواعد. يتم فرض الانضباط هناك من قبل الشرطة العسكرية الأمريكية، وليس من قبل الشرطة العسكرية لقواتكم المسلحة. القاضي الأمريكي هو الذي يحكم على الجرائم التي ترتكب هناك، وليس قضاةكم. القانون الأمريكي هو السائد هناك، وليس قانونكم. ليس فقط أفراد الجيش الكويتي، بل حتى وزير الدفاع الخاص بكم ليس لديه الحق في الدخول دون إذن من الشرطة العسكرية الأمريكية.
لذلك، فإن الولايات المتحدة هي التي انتهكت سلامة أراضيكم وسيادتكم، وليس نحن. نحن نهاجم الأراضي التي تحتلها القوات الأمريكية - وهي قوة لا تعرف سوى ارتكاب الجرائم.
أمس، أقام شعب ميناب الحزين مراسم دفن لبقية أجزاء أطفالهم الذين قُتلوا، والتي تم العثور عليها أثناء عمليات البحث تحت الأنقاض، ودفنوها بجوار بقية رفاتهم. كانوا 168 طفلاً قتلوا في اليوم الأول من هذه الحرب في هجوم من قبل القوات الأمريكية التي تقتل الأطفال. هذه الجرائم مستمرة، ويتم تنفيذ بعضها من خلال استخدام القواعد الأمريكية على الأراضي الكويتية. من حقنا الشرعي والديني والمنطقي استهداف المعتدي على بلدنا وقاتل أطفالنا، أينما كانت هذه الهجمات تنطلق.
نشكركم على تعاونكم.
"والنصر من الله وحده، سبحانه وتعالى، الحكيم</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/naya_foriraq/85033" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85032">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسرائيل تفتح الملاجئ في الكيان المحتل</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/85032" target="_blank">📅 12:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85031">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/85031" target="_blank">📅 12:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85030">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYXWrZkVU8U5DnEfwRG05tZ0H1UdqGdqcvISRSzV6KUKDSmydWqHQEgoMttuS8UdGD24sSZ6Chh30PrzmJ0utcXHPpHyKjnaF9sp93e615ZCXMdBWH_NoaZOzNLtPu8XNNPa8sCm2F0VZuhkTL-TB5VSeITudT7OcFrEtpggQw13-725tT7z9BjD7Wp2vawNdd77vmDQxnMO57PssEXKu0MhmrdLvhKvk8KcQs_GrwNZXyUDASWdZ4lY57xAIwapGrFLIr0jITkpJ1JGvlpjPv-30CZdVFGug9QAqh8RyXOlGOwv_CTJwXOHNm7WZr6Ac4lOaB_xBb-gZPzWPyV4pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
النفط يتجاوز عتبة 98 دولار للبرميل الواحد ويقترب من 99 دولار وذلك في ظل تصاعد الصراعات في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/85030" target="_blank">📅 12:17 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85029">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔻
مصدر امني خاص لنايا
القوات الأمريكية والشخصيات الدبلوماسية المهمة غادرت بغداد قبل قليل . دون اي توضيح عن الأسباب</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/85029" target="_blank">📅 12:04 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85028">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5C75nfNsCy4xyy3AkObH44eTy48G3jw3C0j3NDbQmKyjwbRMLVW5cuMAdr0nemN4sR-hh5vidfowHHPyQBBUp4pV2PONbNtjvMsgOvP95B2_Jl237zzeTaq2P45Nqc80pKd0Zxnhqz89N1wKTFNGR9yIJXgpIz18Hq_jfFa2yW3sUWP7_h5ntlLCHRL_WUTEMCpXqCVRz-VGhvrqddp26bYtx9XzJN-WQXb2uKsTDggfVyP1JujR_z2j69NKxQZDnsYDGSYa49Rnbta0EpydMVLs-qKHTc6wakmQl2j--YFoWiIGPcRkyZgA3eN2KeYQ1pYrh25mh9AgDHE9nrPLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">إطلاق صواريخ إيرانية باتجاه قواعد الاحتلال الأمريكي في المنطقة</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/85028" target="_blank">📅 12:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85027">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
🇺🇸
اظهر مقطع فيديو صوّره سائق شاحنة مدني في سيريك، جنوب إيران، بالقرب من مضيق هرمز، آثار إحدى الضربات العسكرية الأمريكية الأخيرة. ووفقًا لتعليق الفيديو، فقد استهدفت الضربة عدة براميل قديمة متروكة في منطقة نائية. وأعرب سائق الشاحنة عن دهشته من أن ما يبدو أنها براميل قطران مهجورة منذ زمن طويل قد أصيبت بما وصفه بذخيرة موجهة بدقة عالية، باهظة الثمن،هذا مثال واحد من أمثلة عديدة على استهداف مواقع ذات قيمة منخفضة في جنوب إيران , كما يصفون هذه الضربات بأنها دليل على يأس إدارة ترامب في سعيها لإنهاء الصراع.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/85027" target="_blank">📅 11:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85026">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سلسلة من الانفجارات المتتالية تهز الأردن وسط فشل منظومات الدفاع بالتصدي للصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85026" target="_blank">📅 11:54 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85025">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس الوزراء العراقي يغادر العاصمة بغداد متوجهاً إلى طهران في زيارة رسمية إلى الجمهورية الإسلامية الإيرانية.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/85025" target="_blank">📅 11:53 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85024">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي‏روبيو: يبدو وكأن الحوثيين ينخرطون بالنزاع</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/85024" target="_blank">📅 11:50 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85023">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
إعلام إيراني: سماع أصوات عدة انفجارات بالقرب من كنارك.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/85023" target="_blank">📅 11:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85022">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/85022" target="_blank">📅 11:37 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85021">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇺🇸
وزير الخارجية الأمريكي‏روبيو: يبدو وكأن الحوثيين ينخرطون بالنزاع</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/85021" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85020">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سلسلة من الانفجارات المتتالية تهز الأردن وسط فشل منظومات الدفاع بالتصدي للصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85020" target="_blank">📅 11:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85019">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجارات تهز الأردن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/85019" target="_blank">📅 11:12 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
