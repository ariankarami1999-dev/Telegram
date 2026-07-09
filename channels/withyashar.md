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
<img src="https://cdn4.telesco.pe/file/OG_0QGB-q0_5h2KKxyGgdJHPW9qpbzqgQPFjMQt1V7slUm7EIR5YEksDuUeyStZY5mjhGECw_N0PoF2gPWvX60rKcPIsqck1wGSV7Qz7YTRToZZGS7OBwToqUM5F0skSdOC9rBFaUQZWV5uwBzK1GQgWIBtu7iT-7BeLMU_8tGLAoezvZP-r2SY7zlXLO0KSsMWO4Sgo0Ofcw_gptdU4zLFNyWCm_4gqD2Yill2KKgTNhmwvNZD2pEJ80LfK3iEwx6aSwiv_0DzvLIERLhtuq7ITRu772-yZ7vRsifhEPsE_REuVmh-z9iA0wtOOVGtuDGXmciJn5lbgZgz3Yyv9iQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 355K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-18 15:21:46</div>
<hr>

<div class="tg-post" id="msg-17122">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سپاه ثارالله کرمان هدف حمله قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/17122" target="_blank">📅 15:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17121">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">آژیر ها مجدد در اردن فعال شد
@withyashar</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/withyashar/17121" target="_blank">📅 15:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17120">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کانال ۱۴ اسرائیل : علی خامنه‌ای حدود 600 میلیارد دلار(۱۰۹ کوادریلیون تومن) ثروت داشت !!!!
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@withyashar</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/withyashar/17120" target="_blank">📅 15:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17119">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نیروی هوایی اسرائیل:وضعیت حالت آماده‌باش در سراسر اسرائیل اعلام شد.
@withyashar</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/17119" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17118">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">حریم هوایی سوریه بسته شد
@withyashar</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/withyashar/17118" target="_blank">📅 15:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17117">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گزارشات از شنیده شدن صدای انفجار در کرمانشاه
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/17117" target="_blank">📅 15:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17115">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UhbpDEc7Jbblxgie5C0mqJL9B6YENK-qDRW5_c1yJLg0HMuBZDVQiAaBtUbaaioQBlz3g0hycmebmMtj0YcGA-hvxpfyQBnHIdh_HXxxG8aEC6cvR_vkPzsGC2FzY8nQI8p7JVbqcKiQyDstQNzASRmJxy1GN8k-w1Fx-lkFIAIE8T_YgAMfekvTNogiQPlSILjXbs_KLpILE9JReX7cR2L0gb9tX30bTfzyZWGkbHP77NYM1YhhsgKRBd8-kN4LPJncP1req680XzD-RDmSJKkCy4I-iR78EgydkbdDPD-5pIRNiYTqr-fv1O_AqxYJRfwu94Nf-CuQ3jCnKkCFuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQCrRICO-99ttUop-ETwpUishGenAl0yKRfJ2vizeCSYucBtaXbet3libpiWfmWK-8tLoYGMjujErGsIXycWFT6huOnCHwtA7GRySO8WGOH95oSA43g1-OqkEuHMAB1qecUoxEE5rRupf_fOZHVgp6xRmwGhiM_kslw827dkxEpQ770U5UXEwH6VccsdUmGM4aqPU8ucprl6FEv04giTM0HHWgbdUtSTRpAj7m-b_CIO5xv8ASnvxRc_QAdtUPRTcTQy60zVi-nGb6X2NHV2Q55SBugJBxatB70bBJRB8wvGnms-tjELxvuTBi31GabrowPdSVUyk0SJHdYTCJT2xA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وضعیت قایق های سپاه در اسکله بنودِ شهرستان عسلویه
@withyashar</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/17115" target="_blank">📅 15:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17114">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حمله آمریکا به شادگان در خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/withyashar/17114" target="_blank">📅 14:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17113">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">وای‌نت:  مجدد یه کشتی جنگی دیگر آمریکا تو خلیج فارس مورد حمله قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/17113" target="_blank">📅 14:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17112">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش از پرواز گسترده جنگنده های نیروی هوایی ارتش بر فراز مشهد از ترس حمله به مراسم
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/17112" target="_blank">📅 14:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17111">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آژیرهای خطر در پایگاه نظامی آمریکایی التوحید در بغداد به صدا درآمدند
@withyashar</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/17111" target="_blank">📅 14:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17110">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">تانکر ترکرز: ایران به علت احتمال ازسرگیری محاصره دریایی، 10 میلیون بشکه نفت را در شب گذشته صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/withyashar/17110" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17109">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">پایگاه سلمان حاجی آباد هرمزگان دو موشک به سمت تنگه شلیک کرد @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/17109" target="_blank">📅 14:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17108">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارش انفجار در شادگان خوزستان
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/17108" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17107">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پایگاه سلمان حاجی آباد هرمزگان دو موشک به سمت تنگه شلیک کرد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/17107" target="_blank">📅 14:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17106">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">خبرنگار وال استریت ژورنال: علیرغم صحبت‌های دونالد ترامپ مبنی بر پایان مذاکرات، این احتمال وجود دارد که به زودی به آنها بازگردیم.
پویایی اساسی، بیش از هر چیز دیگری، تمایل به عدم تشدید تنش است. و من گمان می‌کنم که این موضوع در واشنگتن شدیدتر از تهران احساس می‌شود، هرچند که در هر دو مورد صادق است.
@withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/17106" target="_blank">📅 14:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17105">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سامانه های پدافند هوایی اردن در حال فعالیت در آسمان پایگاه هوایی موفق سالطی. @withyashar</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/17105" target="_blank">📅 14:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17104">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">منابع رسانه‌ای: آژیرهای خطر در پایگاه آمریکایی «حریر» در استان اربیل در شمال عراق به صدا درآمد
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/17104" target="_blank">📅 14:39 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17103">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bd8d735f9.mp4?token=eM8JlTZk-6UO71fndf7SHeT9mncXfdVaYln_eYc9MGaqUdUoXG9SkykeqJBs4LCNY5tyeYApcv94suiZbXN2nOLeMsXpF4GDU-kg6u4AhVMUF9-SPtSFK7Hvc6a2NRLg7dZX6OCDSVuUWoPeM6b7r3By9YlTx6sCCvwkhBfCtz3OUjhALRrJeDf4rtox49TJqnSskpiNeiba919e8BXXTtfebCP6QTaCKNC2AKJFUM0GVh_btEqvMCCoar1qU4tMK4cOR8sasZbH9RN8-MSbZ8rQu2gCnLj5TXT_YY06dVIrNVMlZB1wb8yf504V-yJHSXEUgiCIuCluVwAAfxu9Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bd8d735f9.mp4?token=eM8JlTZk-6UO71fndf7SHeT9mncXfdVaYln_eYc9MGaqUdUoXG9SkykeqJBs4LCNY5tyeYApcv94suiZbXN2nOLeMsXpF4GDU-kg6u4AhVMUF9-SPtSFK7Hvc6a2NRLg7dZX6OCDSVuUWoPeM6b7r3By9YlTx6sCCvwkhBfCtz3OUjhALRrJeDf4rtox49TJqnSskpiNeiba919e8BXXTtfebCP6QTaCKNC2AKJFUM0GVh_btEqvMCCoar1qU4tMK4cOR8sasZbH9RN8-MSbZ8rQu2gCnLj5TXT_YY06dVIrNVMlZB1wb8yf504V-yJHSXEUgiCIuCluVwAAfxu9Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سامانه های پدافند هوایی اردن در حال فعالیت در آسمان پایگاه هوایی موفق سالطی.
@withyashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/17103" target="_blank">📅 14:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17102">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سفارت آمریکا در اردن به دلیل «گزارش‌هایی مبنی بر وجود موشک، پهپاد یا راکت در حریم هوایی اردن»، دستور فوری برای پناه گرفتن صادر کرده است
@withyashar</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/17102" target="_blank">📅 14:36 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17101">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R6_lRSemA11KqkwbxYUkXoWkGPoIaDSBp81O1ORs3_fO0c93pExSRGMoN0FNeMK7hjUrrv0c0p-iGV97_3D9T-xapIjqfGWsQxegAvhbPvxtUVwoy5agMj2KUSSzdC405QWYaDSW_1R5TUYvRDI2C74NCNLrntYn1KOFPmRrBnGRG-BeKdPZaQcWUV0jICBWGS5ZCPGshE8uSihRrPDF1XgsT4q6Zd_5XlCjFgE7Dn3x01tAybYHHlvm91y22EDidOWL3cC_l5N0GwMM7s_zMyrR-yKxKH77IZqEzCRK1QwZu0tCfMSPURKLyEWHtcix1QXXtovgcasTKwgMLIAkzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک موشک از حوالی تبریز
@withyashar</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/17101" target="_blank">📅 14:30 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17100">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">دقایقی پیش موشک های کروز تاماهاوک در بوشهر دیده شد
@withyashar</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/17100" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17099">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/withyashar/17099" target="_blank">📅 14:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17098">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش ها از نزدیک شدن جنگنده های اسرائیل به مرز عراق و سوریه خبر می‌دهند
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/17098" target="_blank">📅 14:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17097">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7-a7q2psSTL1uqSNcDUPxvuE877_TpIAK6gPkh51h-vUMvBLNpIq8CiautI8c8s4z-uD2J9IA7qoeSf_7wgQlBO61yV9f9oNPaOA5glIk3A6xGRtozlZmyAQmj8J4zIqzz-q8GzaJXsVIWjVxz29H-YI2-CDAqbrnjtIkYSZaXrPypKJNePHNNdN5EF0QRdtEqos4SNVe3Um0NvrVfPNPNuS7mAVqWkkR67ZFltmecj9RjW6LH5gu2ZHK9CxH61Tg8HYYj-FInhFdBzT1wfXESrSmejbAglBG0cnSgZzccWIGVcqwzYmTgDIq9vAK-Ca4nZb6f722tUA4fJkejMSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس زیبای مقعیت و لحظه شلیک لانچر موشک در خمین
@withyashar</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/withyashar/17097" target="_blank">📅 14:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17096">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/withyashar/17096" target="_blank">📅 14:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17095">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">بعضی رسانه های داخلی خبر دادن مجدد کنار نیروگاه هسته‌ای بوشهر مورد حمله قرار گرفت.
@withyashar</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/withyashar/17095" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17094">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">تانکر ترکرز: ‏تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/17094" target="_blank">📅 14:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17093">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش‌ها از صدای انفجار جدید در کرمان
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/17093" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17092">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گزارش صدای انفجار هایی در پایگاه  بندری علی السالم در کویت
@withyashar</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/withyashar/17092" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17091">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/17091" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17090">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آلارم حمله  صدای انفجار و درگیری پدافند در اردن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/17090" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17089">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36ca620126.mp4?token=FO_7fk6bHAtJpi06YRBfeZE92Nt4ZtJ36KsAeyAm42FNno2LqRLPyNDTeSKI8wrcquf2ghMD40pLWujqL2FY6tbWw4JO8f5s2YEF82CnkTBym2cbHSefBZLSeAJ_5fRSlvB5hvsyGV5DM7pcs-ZYojnwW6ELtlvFqcni49mgJUg2B9TmQJHLeUnZIild46a83kCTJk2bO-cMtSvWSDoo-vG3HBLH0Jn7fW6pDCFwEK6nb1oqwyYkfVPVR7mQpnuyPYzfZY3ITCLVAanqVW-d0CX9dz09tnoB7jKIa5wwYs5rJob4BaDjJ_sJlbZvPGh-g6A1kGaGA50Uas_5TpDs3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36ca620126.mp4?token=FO_7fk6bHAtJpi06YRBfeZE92Nt4ZtJ36KsAeyAm42FNno2LqRLPyNDTeSKI8wrcquf2ghMD40pLWujqL2FY6tbWw4JO8f5s2YEF82CnkTBym2cbHSefBZLSeAJ_5fRSlvB5hvsyGV5DM7pcs-ZYojnwW6ELtlvFqcni49mgJUg2B9TmQJHLeUnZIild46a83kCTJk2bO-cMtSvWSDoo-vG3HBLH0Jn7fW6pDCFwEK6nb1oqwyYkfVPVR7mQpnuyPYzfZY3ITCLVAanqVW-d0CX9dz09tnoB7jKIa5wwYs5rJob4BaDjJ_sJlbZvPGh-g6A1kGaGA50Uas_5TpDs3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از زنجان هم موشک پرتاب شده
@withyashar</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/17089" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17088">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آلارم حمله  صدای انفجار و درگیری پدافند در اردن
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/withyashar/17088" target="_blank">📅 14:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17087">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/di2uhuRHFWtuSA3JAOCFA9muf-RuF8Smpg-Te6p-pvQ9CoctHpFWVHd-t7Sq75PNH6D11jrFwwTnmSNmRAAOOGh-F4T-KnGHG_bsqRuoZCDhp8LSiQsA3y8n4Bm3YNoLFi4MM8vg_UudJbAjznoZUwsZjcZMo72-Na0jzX7PndbQzI5iVHmgOFC-liXzJ-ause6UeiEPPGpFFd2bCe36yoW0Fr26BbUCkzUMKOdBAp_ABCyymYBOCR6PHY-7dSy0dqW7hLYxS_1Knm-9InlFRBKiJhdkb_WKMJd90uzaErm0njINL04a-gaZM5qyqoFPrI0VWhQGkeH6MvEiIUPMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه موج جدید حمله را شروع کرد :
۳تا موشک از بین خمین الیگودرز بلند شد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 69.8K · <a href="https://t.me/withyashar/17087" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17086">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857d372470.mp4?token=M6Dug1B6sC4r0jIZhOMYoNAsZLtiS8-xZVxVzbBsk0vfRzB9T6_x-1YMURlzhcDX7xo_k-wMRiZIrCRmgMzdJVMH-uC2yV7Ap53Ak5xvL0KptjU1DgXQXzVvIeZnivMszbdoFMELlRzoCQECNIUAanahgpjnmVf4JdupdMcZMxr9BB7D5xZLX0ewzhM3jvmpbyjA_uVVn44MWCmViyyGrBFqs4xGR3dKt6uxp3QlfFD3XTKd6ezVvHYGO_EeKzrYuGmwU5O1LWfCZMfmtSu2zVd3YQOL9oddpzgh-u96kihp5upE6pgGCid1ZdB6ZhJHUzGqDsZWxm9783IqqoIvj1iKkvsGqGa7eL6bnBuLvTEp8p--8Gx1Pxd6o5Z6nAezkSR3q9x9Mczq0svlKnRqb3dV9wR1niBe3ia6Ph66rbBtISQhd9kpjcyTstt2-UuTm3Gjn4zyVUUiORX5AjFwRcJGRdWEe9g267X6hgT12elXKnYxpVMTeqNvv_N-2y2kQ9JaaBcowQN4ECOETOZfnWtbwnMJnkTdltJFf4AC9qyJZc5U9dn3Emd4gce-MTNmo5KTgy-8yzwuRTDBPU3XV5sIssdV8_F3JQuYgIIRaDQBlYlM2Vw-AKaQ8Fnf_xouz2g3lFTP_DLCJ7JO-DoCzkLswSzw7cCl6-SyjH8ygag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857d372470.mp4?token=M6Dug1B6sC4r0jIZhOMYoNAsZLtiS8-xZVxVzbBsk0vfRzB9T6_x-1YMURlzhcDX7xo_k-wMRiZIrCRmgMzdJVMH-uC2yV7Ap53Ak5xvL0KptjU1DgXQXzVvIeZnivMszbdoFMELlRzoCQECNIUAanahgpjnmVf4JdupdMcZMxr9BB7D5xZLX0ewzhM3jvmpbyjA_uVVn44MWCmViyyGrBFqs4xGR3dKt6uxp3QlfFD3XTKd6ezVvHYGO_EeKzrYuGmwU5O1LWfCZMfmtSu2zVd3YQOL9oddpzgh-u96kihp5upE6pgGCid1ZdB6ZhJHUzGqDsZWxm9783IqqoIvj1iKkvsGqGa7eL6bnBuLvTEp8p--8Gx1Pxd6o5Z6nAezkSR3q9x9Mczq0svlKnRqb3dV9wR1niBe3ia6Ph66rbBtISQhd9kpjcyTstt2-UuTm3Gjn4zyVUUiORX5AjFwRcJGRdWEe9g267X6hgT12elXKnYxpVMTeqNvv_N-2y2kQ9JaaBcowQN4ECOETOZfnWtbwnMJnkTdltJFf4AC9qyJZc5U9dn3Emd4gce-MTNmo5KTgy-8yzwuRTDBPU3XV5sIssdV8_F3JQuYgIIRaDQBlYlM2Vw-AKaQ8Fnf_xouz2g3lFTP_DLCJ7JO-DoCzkLswSzw7cCl6-SyjH8ygag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئویی که ترامپ از بمب افکن ‌B-2 تو ثروث سوشال پست کرده همراه با آهنگ بمباران ایران
@withyashar</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/withyashar/17086" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17085">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1e5bc22a.mp4?token=hdq_Vin9Es8sFWuBJNtbSglCiiPPvt3mikZRDhaBup29gZiF6V9sROTFrnk-ahPQmy_5vpu6fF6RY8sridceniCkyuWm_w6rJM5j5x0EoAlC5Cc-oyYBtl23H5evO7YH0OXFJX7qCUFBs1YSCbvrksfx51MNAYNOIHsydkHn6u_nSQeun8NV7uWYnjkQ0odbIXTDnIa-i3TEw8yjOqmFjdKPWTQukDt5BD1AQFx8-7f-x8b-YlrBzIkUhszN3I1eDFAJ564LZauRmBSlB2CFFYZ_wusK80hWVMb8hb5LjJ8wWgoD_K0IxMNR2mvF1hX0BT2nKp1uRV_vqgQeNbzUMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1e5bc22a.mp4?token=hdq_Vin9Es8sFWuBJNtbSglCiiPPvt3mikZRDhaBup29gZiF6V9sROTFrnk-ahPQmy_5vpu6fF6RY8sridceniCkyuWm_w6rJM5j5x0EoAlC5Cc-oyYBtl23H5evO7YH0OXFJX7qCUFBs1YSCbvrksfx51MNAYNOIHsydkHn6u_nSQeun8NV7uWYnjkQ0odbIXTDnIa-i3TEw8yjOqmFjdKPWTQukDt5BD1AQFx8-7f-x8b-YlrBzIkUhszN3I1eDFAJ564LZauRmBSlB2CFFYZ_wusK80hWVMb8hb5LjJ8wWgoD_K0IxMNR2mvF1hX0BT2nKp1uRV_vqgQeNbzUMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار
کرمان هم‌اکنون
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 71.8K · <a href="https://t.me/withyashar/17085" target="_blank">📅 14:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17083">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pQ2Mcv9VDlXpGVJsK7th7fdgs1VYhwADoTzVbkAz6URiIb0lu15QYNoCRuYItLus89ACFSKK9eLAXVCd83UiL1u4Jbsi-11NNvFpVJcOIVp7o2XftoJ20X0hGHOFQQlGdlzbXsNgRKd1rv8HnHf0Jc0Oo9irkgLLzvH_Qq2_G8Pry-1IffP5qP1n55HNAO68nfD4HtwqTy7OTd-UdNKOOtfwwMRl-zlo2Lb4dWpn95mvuRgSjbQ4KoiZ7eoBmfgf6kdjqq3POoasL8ygeUHdenntt0nbLIy4NEnfqJl27XvEgtqos-ak_-oPnPliNzWa0B1UzEKUgPx3Gp7aGPbzRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VBzyccLBduL6cUnWkZWtUjIFYdZTaa3LnV4feE6Pr94HvDNaKiNSrzb7dwRHg0Ogq_danzBrmrW0Y_k6U6OxNhtikUuOShCcRYnPVmDPI3l9_gyXdJGh7tSA6gQzQ3w-7uwMMa1CfGwr30umzX8z0kmIpldb4sbXXjeUCx_C-qYYzkv1pOGccg_cf5YMCQsyetOkGFsa5vWqlLF-2KyBqKcs-Wd4JyikolF6exngcYoLBmyhA9T-peIzXnBhjLYhZ2xjCk-K4yHSrWUbMws-xiZG8u1wLndNUvw-v-IX2tbo6vYptj5R6UtTtZcTC65RDTpo_lq63gPGQvUtX_Hw0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویر از‌ انفجار شیراز‌ الان
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/17083" target="_blank">📅 14:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17082">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارررر شیراز
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/17082" target="_blank">📅 14:03 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17081">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">شنیده شدن صدای چند انفجار در چغادک بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/withyashar/17081" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17080">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای انفجار‌ بندرعباس
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 81K · <a href="https://t.me/withyashar/17080" target="_blank">📅 13:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17079">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">منابع نزدیک به کرملین: پوتین احتمالاً جنگ با اوکراین را تشدید خواهد کرد.
@withyashar</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/17079" target="_blank">📅 13:45 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17078">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NXEe6mPN_QXUy95uHtQHKpLVMr2tXcIM24MdYsjGnUWWRkTIdtCWP9aPIoTFEUFkxVA9zVgyBJGNnMTeYp2sDdLfbVpsjR4RD36uhAYLRpiZBTdLiyqMWoCyayvu0owYro8EQhZr9OlRvFb3O786Cv3uCgVuloZjFN-ND1Td79Bb3t9gySPO7lfRUJj8mrwefX0PPRBogdkLs4VjYITvQLazu22XgWojiy-l8LeEF2ufuWuPYUBvxueRNpX8p5VKRHYtWfOIbx93HVNjS3nUVIiVS1-9mb8_qoGhADKvwny9g27gfKGczi03wlRHu-mBV6BVWpNQNh3DtQzGgKNP2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آثار حملات هوایی شب گذشته آمریکا به پل ترانزیتی و مسیر ریلی آق قلا
@withyashar</div>
<div class="tg-footer">👁️ 83.1K · <a href="https://t.me/withyashar/17078" target="_blank">📅 13:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17077">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">وزیر امور خاورمیانه بریتانیا: حملات ایران به شرکای خلیج فارس ما، تشدید خطرناک تنش و نقض آشکار قوانین بین‌المللی است
@withyashar</div>
<div class="tg-footer">👁️ 82.1K · <a href="https://t.me/withyashar/17077" target="_blank">📅 13:37 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17076">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم
@withyashar</div>
<div class="tg-footer">👁️ 85.9K · <a href="https://t.me/withyashar/17076" target="_blank">📅 13:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17075">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">دلار و تتر ۱۸۱،۰۰۰ تومان
@withyashar</div>
<div class="tg-footer">👁️ 87.2K · <a href="https://t.me/withyashar/17075" target="_blank">📅 13:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17074">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آکسیوس:ترامپ آتش‌بس با ایران را تمام‌شده می‌داند؛ نبرد بر سر هرمز آغاز شد/ مقام آمریکایی: آن‌قدر ضربه می‌زنیم تا باور کنند ما جدی هستیم
@withyashar</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/17074" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17073">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری CNN : صبر ترامپ در مورد سرعت مذاکرات،به ویژه آنچه که به نظر می‌رسد تاکتیک‌های وقت‌کشی ایران در مذاکرات هسته‌ای با واشنگتن است،رو به پایان است!
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/17073" target="_blank">📅 13:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17072">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همکنون تابوت خامنه ای‌ رو بردن تو دوردور مشهد تاب میدن
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/17072" target="_blank">📅 13:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17071">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">رسانه های داخلی انفجار‌های الان در بوشهر رو تایید کردند
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/17071" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17070">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">۴ انفجار‌جدید بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/17070" target="_blank">📅 13:06 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17069">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نماینده دائم روسیه در سازمان ملل: رقیق‌سازی اورانیوم در خاک ایران یک گزینه عملیاتی است
@withyashar</div>
<div class="tg-footer">👁️ 89.2K · <a href="https://t.me/withyashar/17069" target="_blank">📅 12:56 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17068">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">خبرگزاری وابسته به سپاه :  آمریکا پل کریدوری ایران با چین و روسیه را زد  بامداد امروز آمریکا با موشک کروز، پل استراتژیک ریلی «آق‌تکه‌خان» در استان گلستان را هدف قرار داد. این مسیر که محل ترانزیت کالاهای روسیه و قطارهای چین بود، پیش‌تر نیز هدف حملات مشابه بوده…</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/17068" target="_blank">📅 12:55 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17067">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SuLuFyWTNxtGWC8RhSqd4MvIuAdzz9lKT9wnz2ZF4FyD8lE3E_iYZ3IfK4IO-R4uKPndGxIAK2KSXpCMu0Z9RcB8upIkJnGefzbAl_gYfJ5n7BokfsNfFD_lCB6jHOmgJT4vEtSJfOsD-NtpDjLTCrkDyh9_5Ga8pgTTaxqP8I4OM__8KUdjgzGclrMAr3ICPDytT5cAuykBhbJYIX51jCjx8_0PEEB-1d9rKoCw1NR_QGHCbwJrZg9IQVIzAc4Wb7sCVzATZ_dVrranjMYEOQ_Xfa-Hdy8kao03uKzTiODvjz4EC5UsR8cVxRGDRmyJfPs2VLGX6TQYOuZcDFU7ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت دفاع کویت : امروز پدافند هوایی ۳ موشک بالستیک
۱ موشک کروز و ۱۰ پهپاد مهاجم رو که وارد حریم هوایی کشور شده بود، با موفقیت رهگیری کردیم
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/17067" target="_blank">📅 12:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17066">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مقام آمریکایی: یک سیلی به ایرانی ها می‌زنیم تا بفهمند ما شوخی نداریم‌‌ ، فضای بیشتری برای تشدید تنش با ایران وجود دارد
@withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/17066" target="_blank">📅 12:48 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17065">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ورود محموله بزرگ ریلی چینی به تهران. ویدیو ضبط شده در هفت و پنج دقیقه صبح امروز گرمسار(دیشب توضیح داده بودم) @withyashar
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 88.3K · <a href="https://t.me/withyashar/17065" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17064">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">آکسیوس: حملات آمریکا ادامه خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/17064" target="_blank">📅 12:34 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17063">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhCXSf6N0f8k9RBwZN4LKrqbtnM3Tgon2jDAw8rqZf7AUEgk1S-oWCiTOwq-NVbKdzPm7JLN0uZmb7A1tOueNYrQVH8HdW9pEj519gHauGySCgGS4jJw6JJoWhx6xuH2KVwIEoQi3s6ZOPL31JbFiy0ISGztdq2OgvzricittWCPO1qBp4s23Zx_wXbsRLQDsIFprgekFRkJ1IACgjRapZHYxhXZ7AUGwy10vLR4mxB9mdSeDyZy4EXj4c9JGiCgb6KHIJYRVuKOzAfMUgGTepXHuuGOddRINLa3pbDqv1F8gdcX-tuox0WI-TSNXyBeEv-7Gn__XVdANuEsKeBBqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید.(تجربه شخصی خودم هم هست) بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ 40 روزه منهدم شدند ولی این الدنگهای اوباش بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون
@withyashar</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/17063" target="_blank">📅 12:28 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17062">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گزارش انفجار مجدد بوشهر
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 91.3K · <a href="https://t.me/withyashar/17062" target="_blank">📅 12:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17061">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">صدای ۳ انفجار بوشهر
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/17061" target="_blank">📅 12:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17060">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">آکسیوس: ترامپ آتش‌بس با ایران را تمام‌ شده می‌داند
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/17060" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17059">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/067e87ce1e.mp4?token=fH4i3yI2yymHvZ2W1mIHWiD7IzcY-FhrQH9FfHPaKd7k-59kRdpB5RS7aRbrXeM09XjkbySJz27DVfXQZYyx1MzSxkPY5-R-Z6QVLs2VYHI7jlglnP48HrvLGK9ofU9pOlfuv40rqKd4Foya30w4PerXPyG6nxKWavJSu5aQ9q6S1xc5IJ3I2V7E3MKDaCGiVseU2VJAnyX-WumtYY9VGRTFWiT0t7SK5s9mdu4FFC2ErSwTkb1gj8u3qmY8AQxRhBAuvwcKP3OUXF73NgVMHOcjinCzk1WQnpBNozwQ2FCbHGisDxRk8Jw609VJfLnT3XQgL2UokkzWmjwCdQtVPHMGhLief2ginuzCFEzFktcmst2CN70uEH3r7sc4gnQY_JFyNu_NONA1NEmBn3FVlYd2GWxhEA12-EbvVmA6JhWVkCZ6uLFknv7QAMakvPsOM-z11PG8VY3mpFIU-iflyWUFpASjpf3iD5dwKixQAp3EEvrILhhFtr4uHayqaqg9oi4xJ9ZqxN2e8IJIl4f4mM9psVueTn4qYcKQIOjDO10ZDtAvAWyCQxJi6UmLJMndvlHb7rR-DfOt4ranOSbI_2gGENvo6FPAC7yNvm48YYPRqYQRN0dIvc1-S4LysfwDvxBgmY_WLsM7LbWnRGuQq6yFsemzL9Q3BSymN4j1VNI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/067e87ce1e.mp4?token=fH4i3yI2yymHvZ2W1mIHWiD7IzcY-FhrQH9FfHPaKd7k-59kRdpB5RS7aRbrXeM09XjkbySJz27DVfXQZYyx1MzSxkPY5-R-Z6QVLs2VYHI7jlglnP48HrvLGK9ofU9pOlfuv40rqKd4Foya30w4PerXPyG6nxKWavJSu5aQ9q6S1xc5IJ3I2V7E3MKDaCGiVseU2VJAnyX-WumtYY9VGRTFWiT0t7SK5s9mdu4FFC2ErSwTkb1gj8u3qmY8AQxRhBAuvwcKP3OUXF73NgVMHOcjinCzk1WQnpBNozwQ2FCbHGisDxRk8Jw609VJfLnT3XQgL2UokkzWmjwCdQtVPHMGhLief2ginuzCFEzFktcmst2CN70uEH3r7sc4gnQY_JFyNu_NONA1NEmBn3FVlYd2GWxhEA12-EbvVmA6JhWVkCZ6uLFknv7QAMakvPsOM-z11PG8VY3mpFIU-iflyWUFpASjpf3iD5dwKixQAp3EEvrILhhFtr4uHayqaqg9oi4xJ9ZqxN2e8IJIl4f4mM9psVueTn4qYcKQIOjDO10ZDtAvAWyCQxJi6UmLJMndvlHb7rR-DfOt4ranOSbI_2gGENvo6FPAC7yNvm48YYPRqYQRN0dIvc1-S4LysfwDvxBgmY_WLsM7LbWnRGuQq6yFsemzL9Q3BSymN4j1VNI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آسمان بحرین : 4 حمله به مقر ناوگان پنجم ایالات متحده
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/17059" target="_blank">📅 11:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17058">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپاه : تنگه هرمز اکنون به طور دائم بسته شده است و ایالات متحده و متحدان آن دیگر هرگز از خلیج فارس نفت دریافت نخواهند کرد.
@withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/17058" target="_blank">📅 11:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17057">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">هم‌اکنون هواپیمای حامل تابوت خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.  @withyashar</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/17057" target="_blank">📅 11:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17056">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">آلارم وزارت کشور بحرین:
از شهروندان درخواست می‌شود به نزدیکترین مکان امن مراجعه کنند.
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/17056" target="_blank">📅 11:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17055">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">هم اکنون وقوع سه انفجار مهیب و پیاپی در بحرین
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/17055" target="_blank">📅 11:41 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17054">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همین الان فعال شدن پدافند مهر آباد تهران
@withyashar
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17054" target="_blank">📅 11:29 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17053">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6621f9c274.mp4?token=qeVnIwwviB78iA4FKVrp9FIlQDlVtBak-tMNRKIHliOien-6g4TvC8nTR8o-tt_70PjytW1H-jiZbUPTqcHiiaCJmyjn-2PyERDo_jivldAu4hC-fZAFcffQ10Iv8WkGUAA61pA2kGmT5_xhTBXqZo0K0oB9G8QuOgNVIKIE7Cq1Rt4PZa3eSxLQYeYEnclivVkQNITNWC-qZgvhFgELXZGoZN_5T8JBKk7Jy95RZ8oG31DGXFw0nNk_jmcs0qaB8H1e2XSy9GqHPrPrCcEyvFGbEaM6WKlD4serke6g4MEPvKuCFbYmHTJfjUEWIsQEe8Rv7EUCg8EdvjQR98lvdS4kVabf6n0XswqwwboT1D1vkCxwNb9_3cbGy_EM1-oFr_H__niLLXuW2_upnWUFbchtpdjDGjO1CnbAdN0yIhH395tgc3jVvGdXWfihjSO0KiOOGu196nmH7LIa6NhBE7AwyppFBYeGqc9FotWrlL6zrZ--zPwIPD3JChG68MEhKmG19lFJ1zxh3ecXwr8QSRJJy84nf33pmxE7pnyIBxaJ-c6HVFc-L-w8Key12UQaZUaJiHq2NnU7JKrt6BZd9h6uewuD1Dco9lJ93Co6Mfoe-2sOmq6otnXMvdnppHmLu-fmJi0CRd4j58ueoLxIJ6-5t-HA2Cgd_u4hiFzTtso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6621f9c274.mp4?token=qeVnIwwviB78iA4FKVrp9FIlQDlVtBak-tMNRKIHliOien-6g4TvC8nTR8o-tt_70PjytW1H-jiZbUPTqcHiiaCJmyjn-2PyERDo_jivldAu4hC-fZAFcffQ10Iv8WkGUAA61pA2kGmT5_xhTBXqZo0K0oB9G8QuOgNVIKIE7Cq1Rt4PZa3eSxLQYeYEnclivVkQNITNWC-qZgvhFgELXZGoZN_5T8JBKk7Jy95RZ8oG31DGXFw0nNk_jmcs0qaB8H1e2XSy9GqHPrPrCcEyvFGbEaM6WKlD4serke6g4MEPvKuCFbYmHTJfjUEWIsQEe8Rv7EUCg8EdvjQR98lvdS4kVabf6n0XswqwwboT1D1vkCxwNb9_3cbGy_EM1-oFr_H__niLLXuW2_upnWUFbchtpdjDGjO1CnbAdN0yIhH395tgc3jVvGdXWfihjSO0KiOOGu196nmH7LIa6NhBE7AwyppFBYeGqc9FotWrlL6zrZ--zPwIPD3JChG68MEhKmG19lFJ1zxh3ecXwr8QSRJJy84nf33pmxE7pnyIBxaJ-c6HVFc-L-w8Key12UQaZUaJiHq2NnU7JKrt6BZd9h6uewuD1Dco9lJ93Co6Mfoe-2sOmq6otnXMvdnppHmLu-fmJi0CRd4j58ueoLxIJ6-5t-HA2Cgd_u4hiFzTtso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر ماهواره‌ای جدید، خسارات قابل توجهی را در یک پایگاه نیروی دریایی سپاه در بندر عباس تأیید می‌کند. یک آشیانه آسیب‌دیده، خسارت به یک سازه در امتداد جاده و ضربات قابل مشاهده که بر دو اسکله تأثیر گذاشته‌اند، قابل مشاهده هستند.
@withyashar</div>
<div class="tg-footer">👁️ 102K · <a href="https://t.me/withyashar/17053" target="_blank">📅 11:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17052">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/17052" target="_blank">📅 11:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17051">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ویدیو از محموله بزرگ ریلی که از چین اومده بود ! @withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17051" target="_blank">📅 11:16 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17050">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">درود وقت بخیر خسته نباشید چرا حملات فقط شبا هس؟ روز ها چرا خبری نیس؟</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/17050" target="_blank">📅 11:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17049">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromnima</strong></div>
<div class="tg-text">درود وقت بخیر خسته نباشید
چرا حملات فقط شبا هس؟
روز ها چرا خبری نیس؟</div>
<div class="tg-footer">👁️ 99.6K · <a href="https://t.me/withyashar/17049" target="_blank">📅 11:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17048">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">قالیباف: آمریکا هنوز یاد نگرفته است که زورگویی و بدعهدی دیگر بی‌هزینه نیست. شفاف بگویم: بزنید، می‌خورید.
دست و پای بیهوده نزنید که بیشتر فرو خواهید رفت: تنگه هرمز، فقط با ترتیبات ایرانی باز می‌شود نه با تهدیدات آمریکایی
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17048" target="_blank">📅 10:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17047">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">وزیر دفاع اسرائیل: ما از هیچ نهادی اجازه ای برای ورود به لبنان درخواست نکرده‌ایم و نیازی هم به اجازه برای ماندن در آنجا نداریم. ما خواهیم تا زمانی که حزب الله در تمام لبنان غیرمسلح شود.
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17047" target="_blank">📅 10:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17046">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">یک مقام ارشد آمریکایی: نیروی نظامی ایالات متحده امشب به دو پل راه آهن استراتژیک در شمال ایران با استفاده از موشک‌های کروز حمله کرد، این اولین حمله آمریکا به زیرساخت‌های ایران از زمان آتش‌بس بوده است. @withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17046" target="_blank">📅 10:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17045">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc7c1dd8a.mp4?token=jqebZJ27WB0Thoegm_tsEao5XzPwXAxatQP7pCPyQLtmrMpd8_MniOV3c_m74WvNEp8hq9YuNolcC62Z46nbKBRi1h2_-xeJD3mKqnFnJLX30kpfIs8XamGFOQi5_ISmj3plP8bO2SAjoQCjvCd9NEmX6cLJi7O7XL8ikzHKFD1pCgGdQrtvO8rjFwz8Frmpc5jQdEjbagScDsSmsKvLJxazzg-pxM7OOMTJGkXszKOzSVPwjoE1waOcc5pPYr8Cq_uTk5LJuaIh0nCLpSAg6yl-Bkodhyv7e3U0aQ0LksnAMdw-Wq87xWRvio0ri8qA_mW21KRFb_2QS4VNlkMRKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc7c1dd8a.mp4?token=jqebZJ27WB0Thoegm_tsEao5XzPwXAxatQP7pCPyQLtmrMpd8_MniOV3c_m74WvNEp8hq9YuNolcC62Z46nbKBRi1h2_-xeJD3mKqnFnJLX30kpfIs8XamGFOQi5_ISmj3plP8bO2SAjoQCjvCd9NEmX6cLJi7O7XL8ikzHKFD1pCgGdQrtvO8rjFwz8Frmpc5jQdEjbagScDsSmsKvLJxazzg-pxM7OOMTJGkXszKOzSVPwjoE1waOcc5pPYr8Cq_uTk5LJuaIh0nCLpSAg6yl-Bkodhyv7e3U0aQ0LksnAMdw-Wq87xWRvio0ri8qA_mW21KRFb_2QS4VNlkMRKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی : سلام. من با قطار دیشب داشتم میومدم مشهد از تهران. ساعت ۳:۳۰ صبح که قطار توی نیشابور واسه نماز وایساد، دیگه حرکت نکرد تا ساعت ۷ که گفتن پیاده بشین و با اتوبوس باید برید مشهد. مثل اینکه ریل رو توی یه قسمتی بین نیشابور تا مشهد زدن. الانم سوار اتوبوسیم و هنوز نرسیدیم مشهد
😔
😔
@withyashar</div>
<div class="tg-footer">👁️ 104K · <a href="https://t.me/withyashar/17045" target="_blank">📅 10:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17044">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IPkPGEcJ6RAKhKenOWESIrZiw8FPspKMhx3CgYWVDvQTIZ88ELFXsQob4DsLcCy8xHxbiCZJX-D35KrHWU0xJtyNUo1be3GFj_GMfWxHUgmdoTl0f2Xx262rFUtUGEiicS1-Y3BM3q0bhw-FR2l_WPK3ddUx8mLK7t5SvqPuv6OntZ0JVwHLqXbTAWqh_4uOocrjdN8OuufjdNU4RH3MuBJ47CICS7bkkdggbVt9MCNvrys9E8bguP3zHgAZDAW4Xdnoe710pTkJsDDCWapR3BI8YscARiVLTDs4jhhxX6bHrdAyGgmS2-B2MxwZQoXbpZkUYct8W6KqUlXS4H2-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان : آتش‌بس رسما تمام شده است/ احتمال انجام حملات بیشتر و فراتر از آنچه اعلام شده است وجود دارد
همچنین به نقل از یک مقام آمریکایی مدعی شد: وضعیت مربوط به ایران همچنان بسیار متغیر است و ممکن است حملات بیشتری فراتر از آنچه اعلام شده است، انجام شود. ارتش آمریکا در حال حاضر در وضعیت «انتظار و مشاهده» قرار دارد و اهداف حملات امروز، موشک‌هایی بوده‌اند که می‌توانند علیه دارایی‌های آمریکا مانند ناوهای هواپیمابر مورد استفاده قرار گیرند.
@withyashar</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/17044" target="_blank">📅 10:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17043">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یک مقام ارشد آمریکایی: نیروی نظامی ایالات متحده امشب به دو پل راه آهن استراتژیک در شمال ایران با استفاده از موشک‌های کروز حمله کرد،
این اولین حمله آمریکا به زیرساخت‌های ایران از زمان آتش‌بس بوده است.
@withyashar</div>
<div class="tg-footer">👁️ 101K · <a href="https://t.me/withyashar/17043" target="_blank">📅 10:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17042">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">باراک راوید ، آکسیوس : کاخ سفید در حال آماده شدن برای چیزی است که می‌تواند به دور جدیدی از نبرد با ایران در اطراف تنگه هرمز تبدیل شود که چندین روز و شاید حتی چندین هفته طول بکشد. مقامات ارشد آمریکایی به من گفتند که مدت زمان این کمپین جدید و شدت آن کاملاً به گام‌های بعدی تهران بستگی دارد.
@withyashar</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17042" target="_blank">📅 09:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17041">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b09f2f3a4f.mp4?token=T08kOAJQfWZlwA0lJ_qpBWsgj04Iw1WFItseegaxqBwXDRK7ZoAwmxeDpFv26TIqka2Ej64IrStiXdabEZ2qCU4AnU4e-XI5lmY_zWeLcW71T7KSAdbUxDFfrx5zOZm6RgO0KPJkB194BZQirhu8sLD3DftaFokO18YSchN1ukVxhjlHsa4z4iJkWI22wc5kZP-ns8c_-TATn-JXRdynpNJbJll5EhtyJsmDnAP1ssGQHDfEArvAMsxxVyRIUschDEvdo8ViAEDmoehPQi1OtBbXJvsgFnIsyTHQvWi0kQyCxaV_6Ztl7X1khCmE_ozZESRpL7vMtuI7i8_dT19gZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b09f2f3a4f.mp4?token=T08kOAJQfWZlwA0lJ_qpBWsgj04Iw1WFItseegaxqBwXDRK7ZoAwmxeDpFv26TIqka2Ej64IrStiXdabEZ2qCU4AnU4e-XI5lmY_zWeLcW71T7KSAdbUxDFfrx5zOZm6RgO0KPJkB194BZQirhu8sLD3DftaFokO18YSchN1ukVxhjlHsa4z4iJkWI22wc5kZP-ns8c_-TATn-JXRdynpNJbJll5EhtyJsmDnAP1ssGQHDfEArvAMsxxVyRIUschDEvdo8ViAEDmoehPQi1OtBbXJvsgFnIsyTHQvWi0kQyCxaV_6Ztl7X1khCmE_ozZESRpL7vMtuI7i8_dT19gZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌اکنون هواپیمای حامل تابوت
خامنه‌ای و خانواده، فرودگاه نجف را به مقصد مشهد ترک کرد.
@withyashar</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/17041" target="_blank">📅 09:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17040">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ادامه حملات پهپادی ارتش به پایگاه ها و مراکز راهبردی آمریکا در منطقه
روابط عمومی ارتش:
در پی تجاوز ارتش آمریکا به مناطقی از کشور و یگان های ارتش و در پاسخ به آن ،  ساعتی قبل و در ادامه حملات ارتش جمهوری اسلامی ایران به پایگاه های آمریکا در منطقه، سامانه پاتریوت در کویت، آنتن ماهواره ای(سایت اخطار اولیه) در قطر و مخازن سوخت ارتش تروریستی آمریکا در بحرین، هدف حجم انبوه انواع پهپادهای انهدامی ارتش قرار گرفت.
نیروهای مسلح جمهوری اسلامی، تحت تدابیر فرماندهی معظم کل قوا(مدظله العالی) با اقتدار و تحت هیچ شرایط اجازه تحقق اهداف و آرزوهای رییس جمهور نابخرد ایالات متحده را نخواهند داد و تا پیروزی نهایی از آرمان های والای انقلاب اسلامی دفاع خواهند کرد.
‎
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17040" target="_blank">📅 09:42 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17039">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">در پی حمله ارتش آمریکا به مناطقی از جنوب کشور از جمله چابهار، مقامان منطقه آزاد تجاری چابهار تصمیم به انتقال خودروهای وارداتی از انبارها گرقتند.
@withyashar</div>
<div class="tg-footer">👁️ 105K · <a href="https://t.me/withyashar/17039" target="_blank">📅 09:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17038">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سنتکام مدعی پایان حملات به ایران شد فرماندهی مرکزی ارتش آمریکا بامداد امروز با انتشار ویدئویی از هدف قرار دادن مواضعی در خاک ایران، مدعی پایان دور جدید حملات به ایران شد. در این بیانیه در توجیه این تعرض این‌گونه ادعا شده است «نیروهای فرماندهی مرکزی ایالات…</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/17038" target="_blank">📅 09:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17037">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6a63174b6.mp4?token=YyLUxq9FxC-ktpyyB5s7M6-4O4s_GFG1Oq63W7O3JvHa3-vTqLDXO_bpXQthMMoLdPXJza5uFDpZ8YVsgovXpl_l59y21KfZoWYg8vrmqAqXUzMLvdvANd5OMPkU_ADvWV7JFccoVsz2x-iED0TIUpQDuploPRhG0zES2XhZSNgCRqFDtyR_5g3vAfw2_WpXRz6mFUmFZr4N37hw99Ls3xgA-xzjUmq12ZLEAjbmB5fi0Dhlde1-w9L_rwMJmic-aVFHWGEjzXWImnXeHq1I6N53BHHIuih8zhYvzMqjO7Pu72iszIOnk_qtt16mJafHACFabEJ8v4dGWog6mleGXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6a63174b6.mp4?token=YyLUxq9FxC-ktpyyB5s7M6-4O4s_GFG1Oq63W7O3JvHa3-vTqLDXO_bpXQthMMoLdPXJza5uFDpZ8YVsgovXpl_l59y21KfZoWYg8vrmqAqXUzMLvdvANd5OMPkU_ADvWV7JFccoVsz2x-iED0TIUpQDuploPRhG0zES2XhZSNgCRqFDtyR_5g3vAfw2_WpXRz6mFUmFZr4N37hw99Ls3xgA-xzjUmq12ZLEAjbmB5fi0Dhlde1-w9L_rwMJmic-aVFHWGEjzXWImnXeHq1I6N53BHHIuih8zhYvzMqjO7Pu72iszIOnk_qtt16mJafHACFabEJ8v4dGWog6mleGXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام مدعی پایان حملات به ایران شد
فرماندهی مرکزی ارتش آمریکا بامداد امروز با انتشار ویدئویی از هدف قرار دادن مواضعی در خاک ایران، مدعی پایان دور جدید حملات به ایران شد.
در این بیانیه در توجیه این تعرض این‌گونه ادعا شده است «نیروهای فرماندهی مرکزی ایالات متحده (سنتکام) در تاریخ ۸ ژوئیه دور جدیدی از حملات را علیه ایران تکمیل کردند تا توانایی ایران برای حمله به کشتیرانی تجاری و دریانوردان غیرنظامی بی‌گناه در تنگه هرمز را هرچه بیشتر تضعیف کنند.»
سنتکام در خصوص اهدافی که مورد تعرض قرار داده، ادامه داد «نیروهای آمریکایی به حدود ۹۰ هدف نظامی ایران، از جمله سامانه‌های پدافند هوایی، دارایی‌های دیده‌بانی ساحلی، سایت‌های ذخیره‌سازی موشک و پهپاد، توانمندی‌های دریایی و زیرساخت‌های لجستیک نظامی در امتداد خط ساحلی ایران حمله کردند.»
@withyashar</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/17037" target="_blank">📅 09:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17036">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تردد قطارهای مسیر تهران-مشهد متوقف شد
راه آهن جمهوری اسلامی ایران اعلام کرد: به دنبال حمله  بامداد امروز به یکی از ‌نقاط مسیر ریلی تهران-مشهد، حرکت قطارهای مسافری در این مسیر با وقفه مواجه شده است.
تیم‌های فنی و عملیاتی راه‌آهن بلافاصله به محل اعزام شده و عملیات بازسازی محل آسیب‌دیده در دست اقدام است و تلاش می شود در کمترین زمان ممکن این مسیر ترمیم شود.
@withyashar</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/17036" target="_blank">📅 09:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17035">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">گزارش انفجار در بحرین
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17035" target="_blank">📅 04:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17034">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">طبق روال عرزشی های هوا فضا نماز صبح رو میخونن جدیدا حمله میکنند
😂
🤒
@withyashar</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/17034" target="_blank">📅 04:09 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17033">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kyfUpd2Gdh6Zg66-gaQDlNMyWEyY41JJPTD1eCk8zCGz8rQBHmBWt9vtejnKyPG5gpgdyG9MMU3K5n1rvn4UVhsECzxXas0qr9O2LQoyQPKS2-POIdBt4D4OowV83I3RhH4iYdm18_mMSyjU0MJBU46nFjCgTrk3ajlxot9JgtWxFZD9nZvQM75e_QA4l7p0d5r79hlUezp9PPzAz9hXB7j7Mof7IJRcR82oxo26EN5rmo9nygtVCcEgqfMChWB0fFB87hpdXQ1Wh2ZIdnmcHDevPEs70uuw6lnLmHh1bu_ieJY4hWUVZGw667GVCr1Ixg262RZb-dIEkeQXsH7FaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شلیک ۷ تا موشک از سایت موشکی خورموج بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/17033" target="_blank">📅 04:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17032">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp5NoEC6Ns2T5MEAavOhle7gV9kXA-NYndzWwBslWGQ2eUa9sVDvS7oEc1etJhGduOnygEwrswuquftfSlpcb_stqL7vuiO9c5tkYyfSzwycBnnZIXuWKP0oBLTjEBAO50JKMDJfz-f4xiXlU1Drx4DQB5NzTw0cEdEyDIiWopQnBB5lg3CZJ8LfxambHtxkjnsQ733v0ILYbjuC_dHaYoVfmVQoYjyRiRWDtiGCjy19va8zeDouH6Q06UDCViijQ6wHsLMGSSrP6roVVGGITBI9A73ounJx8x_lGiXRNvrYVepPy-eUlrraKSuF2Hgnir8JLlYuNbkA98VcshQJRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین تصویر از شروع حمله ۳پا و شلیک موشک بالستیک از بوشهر
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17032" target="_blank">📅 04:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17031">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اتاق جنگ با یاشار : ۳پا یک پا هم قرض کرد و حمله رو شروع کرد
😂
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17031" target="_blank">📅 04:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17030">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بوشهر دو انفجار دیگه
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/17030" target="_blank">📅 03:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17029">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">از زاویه دیگه آق قلا @withyashar</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/17029" target="_blank">📅 03:54 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17028">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d238d2c15.mp4?token=iPC8_s-lxiAaPPIs5HOZyd-IeW7hDX_LCrJIMTBqaAn1HXu0_mDa_yPPmBPbq4q0RGsFL90HzCL3dnXU1FVZ-UJmjAmejMyADVbGWg8sfsSO7xTfZbmREsLvwUQqog50CDFlR6DQ9bgSmeoLIuBPWZzln84ewtkRom6h90ISb4pEZLWBQ4kd8Z-w7hDjNeUpC9won1j0PyMgfPL-08VXor20kwfqMsn6uieTdMPuiGKXt_r1K9C-yEGczOAKYU2qbLBalLg-V8SRQVOVVYjVzqx5OR1Dnxx3HgcvbUtsGsaLF5t9hz71La8IIe_JZDtxh6TrNNBUqB5ASPZArovBOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d238d2c15.mp4?token=iPC8_s-lxiAaPPIs5HOZyd-IeW7hDX_LCrJIMTBqaAn1HXu0_mDa_yPPmBPbq4q0RGsFL90HzCL3dnXU1FVZ-UJmjAmejMyADVbGWg8sfsSO7xTfZbmREsLvwUQqog50CDFlR6DQ9bgSmeoLIuBPWZzln84ewtkRom6h90ISb4pEZLWBQ4kd8Z-w7hDjNeUpC9won1j0PyMgfPL-08VXor20kwfqMsn6uieTdMPuiGKXt_r1K9C-yEGczOAKYU2qbLBalLg-V8SRQVOVVYjVzqx5OR1Dnxx3HgcvbUtsGsaLF5t9hz71La8IIe_JZDtxh6TrNNBUqB5ASPZArovBOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الان هوا فضای شهر چغادک ، بوشهر رو زدند
@withyashar</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/17028" target="_blank">📅 03:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17027">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">همین الان شهر چغادک رو زدند
🚨
🚨
🚨
🚨
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17027" target="_blank">📅 03:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17025">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">طبق روال عرزشی های هوا فضا نماز صبح رو میخونن جدیدا حمله میکنند
😂
🤒
@withyashar</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/17025" target="_blank">📅 03:22 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17024">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/724fff2286.mp4?token=D2Fw4fjB2Grwu3T6iDVQQrYYdVFe6KJIMzsqv_MeB9HeTjr35hecWMcyLXysBY1COTI3QlErpsAqCWZ1wywwIOzPzXgW_VaE7o8-MnKW7TVhNQW9xk_cbmLSe8GN9bsOPwRG2OjBvVOGZY8RUPu4si4Z4cst9aDi5_86fzvpgZJn8-VGum8mIkZhBgNol_wrl2Mo9fy7E_668Qq3SiIgAAyyPh8DzNIDKU2I2LxLPLsWWNazZ49kALhVuGhJT8uxGk6wdZL8NbvGIvF30_W5rEPcbMOKR2v1RxkTbRvsLKJ8ugoVIdwF-KiQChsIi_Q1V7pR5NgkxoSBKpt_z9r7Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/724fff2286.mp4?token=D2Fw4fjB2Grwu3T6iDVQQrYYdVFe6KJIMzsqv_MeB9HeTjr35hecWMcyLXysBY1COTI3QlErpsAqCWZ1wywwIOzPzXgW_VaE7o8-MnKW7TVhNQW9xk_cbmLSe8GN9bsOPwRG2OjBvVOGZY8RUPu4si4Z4cst9aDi5_86fzvpgZJn8-VGum8mIkZhBgNol_wrl2Mo9fy7E_668Qq3SiIgAAyyPh8DzNIDKU2I2LxLPLsWWNazZ49kALhVuGhJT8uxGk6wdZL8NbvGIvF30_W5rEPcbMOKR2v1RxkTbRvsLKJ8ugoVIdwF-KiQChsIi_Q1V7pR5NgkxoSBKpt_z9r7Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به پل ریلی کنار پل دوگونچی آق قلا استان گلستان @withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17024" target="_blank">📅 03:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17023">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سنتکام همچنان بیانیه پایان عملیات امشب رو نداده
@withyashar</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/17023" target="_blank">📅 03:14 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17022">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f1bb7e867.mp4?token=c4MwQtTTaN70SniQm1nNko2tgcuFHSYc02L355tYD59qktsEepEawwtFUcsWhUa5a4iJae3a1eCeIXmL4eeyX8TDWP88yJBspQRYPvSXugtC6maWqN-p19oQXlkYsnp0WqRGwj3PQFv3snqr0O1YNI6vOkVMYHnQkkZEuYUkFyo75fSGlTD1P0i30YaaTd9eQ3Kk_Wp1O3us3BMeED6nIjv0Em0POgiKUunx52JIPAre0amjLWkR-dBOJyhK79ADsWG6vccqALi8VDsYh4T1c-2YdmwLzYEYkCYAx9wjkzPOiwCGH3O6l53JeseqZs1-17XZLsuihnBRH1dOhTwqoFNnQ_duPjsPWPQJGeNCQlQ56elfqVtRJmHmGWJ0mdSI3zbGnY75wDpF0cdrBHVmGgDOdEZJdMuxFH5GjPux6VpIGUP9INbpneS86yBNloKZey4i7U6zXzG--ed-UhHuvBFRhhwRP3mAFd9lAtpUQZkruNTX47Jf0isIZsK3qjXUHM-4Cl9W4OE0egFxOK36XafbQhu6AbEk9qqdok3vORj0je0vnYQCXVw3fBXQ2olnqg-P6ob2qKd7fdbVd7tYEpWNq_nZSxptpEwbZWZ4VBS_NrsUiRPf7XTTZR_caHeuhuWDZTvW90MSvt_uUaHpm_5ufxwHs7Z0EEXazLOmolE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f1bb7e867.mp4?token=c4MwQtTTaN70SniQm1nNko2tgcuFHSYc02L355tYD59qktsEepEawwtFUcsWhUa5a4iJae3a1eCeIXmL4eeyX8TDWP88yJBspQRYPvSXugtC6maWqN-p19oQXlkYsnp0WqRGwj3PQFv3snqr0O1YNI6vOkVMYHnQkkZEuYUkFyo75fSGlTD1P0i30YaaTd9eQ3Kk_Wp1O3us3BMeED6nIjv0Em0POgiKUunx52JIPAre0amjLWkR-dBOJyhK79ADsWG6vccqALi8VDsYh4T1c-2YdmwLzYEYkCYAx9wjkzPOiwCGH3O6l53JeseqZs1-17XZLsuihnBRH1dOhTwqoFNnQ_duPjsPWPQJGeNCQlQ56elfqVtRJmHmGWJ0mdSI3zbGnY75wDpF0cdrBHVmGgDOdEZJdMuxFH5GjPux6VpIGUP9INbpneS86yBNloKZey4i7U6zXzG--ed-UhHuvBFRhhwRP3mAFd9lAtpUQZkruNTX47Jf0isIZsK3qjXUHM-4Cl9W4OE0egFxOK36XafbQhu6AbEk9qqdok3vORj0je0vnYQCXVw3fBXQ2olnqg-P6ob2qKd7fdbVd7tYEpWNq_nZSxptpEwbZWZ4VBS_NrsUiRPf7XTTZR_caHeuhuWDZTvW90MSvt_uUaHpm_5ufxwHs7Z0EEXazLOmolE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله به پل
ریلی کنار پل دوگونچی آق قلا استان گلستان
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17022" target="_blank">📅 03:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17018">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cewsYHL_K5u8uOlZ5fOIkGGbf8l88TCsrmWTKzlaxrvJSm1Zb9cbm9pX4WHLj262jncjRU0-npO1UsjJFxiWTbtp2wU3A_kXY2ha2_ACcT3MO6Kys7IA-RHLIWtEthiJ88B_09yRIJUUG1rl6DezYlg6lAO9--2-g-YTF3gE90LujMPMMw9_o1pOpIfmtYF48ky7guQ_bZutFaNypxmwnI8G1aY6qAWFObY5SXmxybtsq2CbEoSGWv7RvK6wfts_aRxPjcnak-cTY7WtthiR460w_xZ4N2ZCGrHnvQOU2NCtUxidOghyzK1-8KYV92fNjbQ3b4Tzhxj3Oy2wvg5cmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qw0hqt9uIizeBZq4TEzXS8s4fg38WoOTLK5KRnM2W7xm2HJ9YmjdWMABpU-7JoR3LURysN5nk9u6yy3CSJJqDsSmjObqNYU8fh960dyl4qtax7P1RZdzGIF0HKxj6iZmCUn52tzERlozNwiF3IyuOOoyr2ii-LffF0Lif6W_c8B6oJQg50hWBDTVNC0VYU96VOJYmYQ8iLA1JKwArzCH3hPxWoBDPciixj4tcgjYzN-226LuGanP1dvwz5j7oexP3CUxfAxoFoMXIgEwEOEZs0kphkdLi6ZGfuWFOgSWG9aEiZT0CNwroBMQ6cKFFAZHnYSowrZ4wlDpeWvvMF6DHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GHCa3fLnaeeFVnug-t8uY-gfY1NcEkQ_c1Z1PZDJ_k8fYIvL9gpaFRQTd_DSpFyqTl3nbxONxW28q9DZ12iMaoXGpZXCoIDL7jczIknTuDPYnVuQzfqrLzjMh98d6DM_qAnFYUg6BvoIlTsUqiDAkTYPfLVhYPDs0T3IFM5cQLE6U-nR2j69Pe3V8-V_5YbQMsPosMsb64AZ_F5QNlCPH3JtJwmZIbfYZYDij0QpY-u38nMwShnMt62K1QKflILg91NZcgHR3z_sTO44S6Xj9TDKuVakmi4nxsb2SKj6LHr0rk8u7G1lV6W7cO8mR9kNkZ9OedRp7QqXPmHmFe84Cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس‌های حمله به راه آهن آق‌قلا در‌ استان گلستان
@withyashar</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/17018" target="_blank">📅 02:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-17017">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/820564fd6a.mp4?token=cY5q5F48dL2VV26Xh8PbZRZLFVBkf9jmNG0J1IEKR0ZIzBBnpTX0Oipxcc8w0WqkwdlThefyHTi0xZwPH8Yv8W-N8qmrWLKh8jmenDp5CzFDdrbbsoj6RIhW2vBL85k_dMKQNnJ3pEK5I6CrcrdC_ZRh91Kanb6y0kA9T4Jw9yRyyMqPQLjaP7nEstK8re5iCWb0Il2XbaOJqhvtxjOMk9ol4G5lxf-ioCjFa2YFt2TEpDtRWV2Lj6P0-TewAdSRp5M4ATI7tgQY-obOI1HJ2NnbX0ByfnLQHbzjatmg5GOIpEIHfQpRJ934a5LUZr0oZVfCckRyNXpREVgmSm-3bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/820564fd6a.mp4?token=cY5q5F48dL2VV26Xh8PbZRZLFVBkf9jmNG0J1IEKR0ZIzBBnpTX0Oipxcc8w0WqkwdlThefyHTi0xZwPH8Yv8W-N8qmrWLKh8jmenDp5CzFDdrbbsoj6RIhW2vBL85k_dMKQNnJ3pEK5I6CrcrdC_ZRh91Kanb6y0kA9T4Jw9yRyyMqPQLjaP7nEstK8re5iCWb0Il2XbaOJqhvtxjOMk9ol4G5lxf-ioCjFa2YFt2TEpDtRWV2Lj6P0-TewAdSRp5M4ATI7tgQY-obOI1HJ2NnbX0ByfnLQHbzjatmg5GOIpEIHfQpRJ934a5LUZr0oZVfCckRyNXpREVgmSm-3bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از محموله بزرگ ریلی که از چین اومده بود !
@withyashar</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/17017" target="_blank">📅 02:43 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
