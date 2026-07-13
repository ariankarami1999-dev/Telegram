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
<img src="https://cdn4.telesco.pe/file/IA4z8_mTi4qDtHN8pBhHo_jjKJYSkS7f-zWq5zV0siMUAMDdoir_PHax9LP3i9S09mMPlqs9iiBwz7xTd7u1mt5LbvVDlX71z6ZYkhEBSp5oO_ZaqhoC6Gnzb-RTORzgmP_c019I2Oc3jZv2d7OQpanZXR8BfPjP0fZVnGzD1ZIWEBsN-hXW28DC2UoIUjnvYHQvyCY9Nn7n-a43eY3dfZnwxNVdRlwJ_8FCSyMYsAOqPaYn1RyHrIYpNxTXpNJ8xQrm9mDV3MJ9EaBWBszKqdUnpkleGvLNnCDJKHoSi1sh58LpO-ru4299oj2hUkIe_EJKbVEdwfRqEED3ASIygg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 196K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 21:56:29</div>
<hr>

<div class="tg-post" id="msg-80230">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LJhLW3L3ml791aIJPynPDfQZNGEJm_nolq73XHJxr00_E2kE7czeXGc0JzB5ke39YCtOyUFR2rjOCfCLVg4xnlGbY9-2hAvK2SD72RgnONoSuznzyaU-RU3vO3ZYrGItB88A_xZYW-wWXVw5tMBUkQvikGILe2iiDdrRZwdh7Cc15Lg6W68CVXD6y48RAm0vuPsqc76hR1X63iENv59_a0he4KyrIPt0EF0_Og6N2xn34oIlahtySoRnq4mTFaSbjZDIc4vv7DTh3AtZBFm9e5b9o53AOj1hGIUm8cgfkcO6cvD2T_cXhHPQG8tIScyyKew8WLXQe30ykFObyy1CUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرطان حلزون گوش گرفتم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/funhiphop/80230" target="_blank">📅 20:54 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80229">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">یکساعت وقت دارید خاندان اژدها رو ببینید، یساعت بعد میام همشو اسپویل میکنم</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/80229" target="_blank">📅 20:44 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80228">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">طبق تحلیل من با این محاصره ای که کردن تا بعد انتخابات میان دوره آمریکا خبری از جنگ تمام عیار نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/funhiphop/80228" target="_blank">📅 20:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80227">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from2METi2</strong></div>
<div class="tg-text">باحاله</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/funhiphop/80227" target="_blank">📅 20:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80225">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/80225" target="_blank">📅 20:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80224">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">جمع کنید کازو کوزرو علی گرامی ترک داد</div>
<div class="tg-footer">👁️ 7.38K · <a href="https://t.me/funhiphop/80224" target="_blank">📅 20:19 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80223">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اوه اوه بیبی اومد
ترامپ:
امشب ما مهمانی بسیار ویژه خواهیم داشت که در حملات ما به ایران شرکت خواهد داشت.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/funhiphop/80223" target="_blank">📅 20:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80222">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">اسرائیل سر انکار هولوکاست از محمود احمدی نژاد کینه سنگین داره و دیده هر چقدر خودش تلاش کرده نتونسته ترورش کنه؛
الان به جاش تصمیم گرفتن اینقدر تو رسانه‌های مختلف درموردش شایعه پخش کنن و بگن آره این ۵۰ ساله جاسوس ماست، مکان حضرت آقا رو این لو داد، یه قدم مونده بود براش کودتا کنیم به قدرت برسونیمش و... که یه روز خبر بیاد خیلی اتفاقی دکتر احمدی‌نژاد تو نیم متر استخر غرق شده یا مثلا خیلی اتفاقی پاش لیز خورده از هلیکوپتر شخصیش پرت شده پایین.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/funhiphop/80222" target="_blank">📅 20:05 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80221">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آقا مگه قرارمون نشد تا پایان جام جهانی، تفاهم‌نامه برقرار باشه همه‌چیز گل و بلبل باشه تا جام‌جهانی در آرامش و کاهش قیمت سوخت و اینا؟
مگه ما ایرانیا مسخره شماییم که این‌همه تحلیل و آنالیز سنگین و دقیق و پیشبینی مانوک پسند می‌کنیم و بعد همیشه سعی می‌کنید جوری کیرمون کنید که تنها خوشی و استعداد ذاتی ما رو کاملا زیر سوال ببرید؟
۴ ماهه تو این چنلم کلا ۴ تا پیشبینی کاملا منطقی کردم هر چهار بار بزرگترین کیر زندگیم رو خوردم خب الان کدومتون پاسخگوعه؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/80221" target="_blank">📅 19:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80220">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش تکان‌دهنده نیویورک تایمز در رابطه با جاسوس موصاد بودن محمود احمدی‌نژاد:
بر اساس این گزارش، احمدی‌نژاد در اوایل سال 2024 برای مذاکرات سری در بوداپست، پایتخت مجارستان، با مقامات اطلاعاتی اسرائیل دعوت شد. او به بهانه‌ی یک کنفرانس علمی به آنجا فراخوانده شد و طبق گزارش، دو بار در سال‌های 2024 و 2025 با مقامات موساد دیدار کرد. منابع آمریکایی و ایرانی به این روزنامه گفتند: "این بخشی از یک تلاش چند ساله اسرائیل برای پرورش احمدی‌نژاد به عنوان یک دارایی اطلاعاتی است، که در زمان مناسب، بتواند به رهبر جدید ایران منصوب شود." این در حالی است که احمدی‌نژاد، در دوران ریاست جمهوری خود، برنامه هسته‌ای ایران را تسریع کرد، خواستار نابودی اسرائیل شد و انکار هولوکاست را مطرح کرد.
در سال 2024، حتی ددی بارنع، رئیس موساد، شخصاً به مجارستان سفر کرد تا با احمدی‌نژاد ملاقات کند. موساد، این جلسات را به سازمان سیا (CIA) آمریکا اطلاع داد.
بر اساس گزارش، اسرائیل به طور پنهانی مبالغی را به احمدی‌نژاد پرداخت کرد و مقامات اطلاعاتی اسرائیل در چندین نوبت با او دیدار کردند.
این تلاش‌ها در اواخر فوریه امسال، در روزهای اول عملیات "غرش شیر"، به اوج خود رسید، زمانی که یک عملیات جسورانه برای انتقال احمدی‌نژاد به یک مرکز امن موساد، به عنوان بخشی از طرح سرنگونی رژیم، اجرا شد. این طرح شکست خورد.
در 28 فوریه، روز آغاز عملیات، یک حمله هوایی اسرائیل به محوطه اطراف خانه‌ی احمدی‌نژاد انجام شد و هدف آن ساختمان‌هایی بود که محافظان و خودروی زرهی او در آن قرار داشتند. پس از حمله، یک خودروی پژو مشکی به محل رسید و او را به سرعت از صحنه حادثه خارج کرد. رانندگان این خودرو، ماموران موساد بودند که احمدی‌نژاد را به یک خانه امن و مخفی در ایران منتقل کردند. با این حال، احمدی‌نژاد که از این عملیات نجات به وحشت افتاده بود، تصمیم گرفت خانه امن موساد را ترک کند، اما جزئیات این اتفاق هنوز مشخص نیست.
موساد به درخواست نیویورک تایمز برای اظهار نظر، پاسخی نداد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.57K · <a href="https://t.me/funhiphop/80220" target="_blank">📅 19:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80219">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترامپ:
مجتبی مرده! به احتمال 90 درصد کشته شده.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/80219" target="_blank">📅 19:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80218">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6fb756260.mp4?token=GPC6kP3BlRuXr_HBu1MTZsDM6TCzKN3X65uErzoo4ZHPhEBG_b7wUcFanb1na_LPWuz-dTMnN5qFMerhocKK8rbx0U1g4KZJBbydlTfIptFF_43ag6slWPacPxcSTLtT62JIGeDZItQjnZdQezL1ykWb4ioqjqPVM0CS9FvxUdXOs7ukB7GCUVdH_ZS0_IkBl5F-lbd6cWDgujAw0LwhXP52rGNKVDAFARAfaar4eDu7EAc4JsgWCyajqbI47bTx1awlhLLNj9axgegCGrmih9TyjELY7ieU1aG71G3jjOmWr6sgErSL0rJHX1V8es5ylIEYJvMNK__gVLLlLYCeSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6fb756260.mp4?token=GPC6kP3BlRuXr_HBu1MTZsDM6TCzKN3X65uErzoo4ZHPhEBG_b7wUcFanb1na_LPWuz-dTMnN5qFMerhocKK8rbx0U1g4KZJBbydlTfIptFF_43ag6slWPacPxcSTLtT62JIGeDZItQjnZdQezL1ykWb4ioqjqPVM0CS9FvxUdXOs7ukB7GCUVdH_ZS0_IkBl5F-lbd6cWDgujAw0LwhXP52rGNKVDAFARAfaar4eDu7EAc4JsgWCyajqbI47bTx1awlhLLNj9axgegCGrmih9TyjELY7ieU1aG71G3jjOmWr6sgErSL0rJHX1V8es5ylIEYJvMNK__gVLLlLYCeSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیف دکی و ویناک انقد جذابه ترکای اونارو ول کردم کصشری که مرصاد داده رو دارم گوش میدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/80218" target="_blank">📅 19:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80217">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2VjJ-fI4S4IUsmjz2wNJDueAVSYVK001e3p5tVHavaaX42_mC3byEhGiIw-xmT_gSOHGuboyx_r0TyJJQz2frdOqK3kjR412F268S1YOn6_J_v5IHw5f7s6OPR-8EDqChNDVCuCoPiSeXhCtNRWCCaieBtH0-txvHQsoRQDsAjwRfX7bnuc8R9CmwuUOQ71Giqts2aC4uIi7ZB8IyyqlLQjh3JJgf1YQIKmDDkz_fM5cluMpgTMaiWNl3yODAUURSEhy3nTxbgQsO5UEAmEe1Vf9Yn9wGM_2NBIq3YYZt3zl1fHCh5Dzosv4m-Cm_WIERzJGgdDEcZnOx875bSppzmA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2VjJ-fI4S4IUsmjz2wNJDueAVSYVK001e3p5tVHavaaX42_mC3byEhGiIw-xmT_gSOHGuboyx_r0TyJJQz2frdOqK3kjR412F268S1YOn6_J_v5IHw5f7s6OPR-8EDqChNDVCuCoPiSeXhCtNRWCCaieBtH0-txvHQsoRQDsAjwRfX7bnuc8R9CmwuUOQ71Giqts2aC4uIi7ZB8IyyqlLQjh3JJgf1YQIKmDDkz_fM5cluMpgTMaiWNl3yODAUURSEhy3nTxbgQsO5UEAmEe1Vf9Yn9wGM_2NBIq3YYZt3zl1fHCh5Dzosv4m-Cm_WIERzJGgdDEcZnOx875bSppzmA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیزهای اختصاصی بت‌فوروارد، مرجع تحلیل مسابقات برای تصمیم‌گیری هوشمندانه
🎲
📈
در بت‌فوروارد، هر مسابقه با بررسی دقیق آمار، تحلیل عملکرد تیم‌ها، شرایط بازیکنان و مهم‌ترین داده‌های پیش از بازی به‌صورت تخصصی تحلیل می‌شود تا با دیدی کامل‌تر و اطلاعاتی دقیق‌تر، تصمیم‌گیری کنید.
📗
برای مشاهده آنالیز اختصاصی هر مسابقه، وارد وب‌سایت مجله بت‌فوروارد شوید، سپس نام تیم یا دیدار موردنظر خود را جستجو کنید.
👍
ورود به مجله بت‌فوروارد
کلیک کنید
mag.betforward.com
کلیک کنید
mag.betforward.com
🅰
g22
💻
@Mag4ward</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/80217" target="_blank">📅 19:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80216">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ: بیشتر رهبران ایران کشته شده‌اند. خامنه‌ای از بین رفته است و ۹۰٪ از پسرش از بین رفته است. ما آنها را از بین بردیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80216" target="_blank">📅 18:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80215">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ محاصره رو دوباره برقرار کرد: تنگه هرمز باز است و خواهد ماند، با یا بدون ایران.  ما تحریم‌های ایران را مجدداً اعمال می‌کنیم، که این تحریم‌ها به این نام هستند زیرا فقط از کشتی‌ها یا مشتریان ایران جلوگیری می‌کنند تا وارد یا خارج شوند. سایر کشورها می‌توانند…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/80215" target="_blank">📅 18:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80214">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LV4rghX5d5KpegtyumTTzlLZr3RrQgD0-Vwe6i8l4nw9gZQyEZuZeSMb5BxfQov6qpsnL1eTnuSxq6oYaNKjXpr5KB3eZQFVFf7Tlyr5e_xqQ1c1Cd5kU7LmW1xHZu4vLlGqEcNUqw7CCiKfZTZct4yCwITHsE-uExVF5Max1YMJ6o9HGpGbOZr2sduPWlzm5sB4HF4yLyd0--R0jnT59Iw4WrWo33emF0pEN08vewWm8_TAvkSa-gHxn50XDp3rpFkryiK3dnOoQuB1sZH6P2Mf2hD9Vm_YFsT-BEcE3rkyWdbUjCTSbI-Cn1yAl9BvogAnMxhj-S7zOgmJmOIQJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ محاصره رو دوباره برقرار کرد:
تنگه هرمز باز است و خواهد ماند، با یا بدون ایران.
ما تحریم‌های ایران را مجدداً اعمال می‌کنیم، که این تحریم‌ها به این نام هستند زیرا فقط از کشتی‌ها یا مشتریان ایران جلوگیری می‌کنند تا وارد یا خارج شوند. سایر کشورها می‌توانند به طور عادلانه و آزادانه از این تنگه استفاده کنند.
ایالات متحده آمریکا، از این لحظه به بعد، به عنوان "نگهبان تنگه هرمز" شناخته خواهد شد، اما به عنوان نگهبان و به عنوان یک اصل عادلانه، برای هرگونه هزینه لازم برای حفظ امنیت و ایمنی این بخش بسیار ناپایدار از جهان، مبلغی معادل 20 درصد از کل محموله‌های حمل شده، به این کشور پرداخت خواهد شد.
این فرآیند و تشکیلات بلافاصله آغاز خواهد شد. از توجه شما به این موضوع سپاسگزارم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/80214" target="_blank">📅 17:53 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80213">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یکساعت وقت دارید خاندان اژدها رو ببینید، یساعت بعد میام همشو اسپویل میکنم</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80213" target="_blank">📅 17:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80212">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکساعت وقت دارید خاندان اژدها رو ببینید، یساعت بعد میام همشو اسپویل میکنم</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80212" target="_blank">📅 16:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80211">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امروز ترامپ یه جوری سنگین تهدید کرد که بالاخره می‌شه با خیال راحت چسبا رو از رو شیشه‌ها کند و با جزئیات صحنه‌ی امضای توافق رو تصور کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80211" target="_blank">📅 16:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80210">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80210" target="_blank">📅 16:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80209">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80209" target="_blank">📅 16:18 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80208">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65c80ff7fa.mp4?token=Z9Y_9Ta1yKOQAiWy9tFMNj0g-fmw7nDr4aJY6bAIkrlO9aW2q-iuwdh-bN3IjDMhjUYhTxe8Ufp0ZvbxcRZwCKg-wlgvg5-4-xYA6O_WGIrLo1qxx-S4HhuSrKAlxbycbYsV-3vuMW9ok1m3gSOEZssPw2BWtn9S24D2aj444cZYXDtinLRRxdgUN0oG4BLTbYEGlFeASSgrjM8tIUOhEKkLAL8_VJt8yRjy-6c8JIfLUWC1BLO37wTuMwf6SEPAbMnzBJXHSx-4kclIeaS6FvtXoMtdKde9BFSQP8M82M4UeLsHd-A0a4T30ZFqNYSR8ZfCMBo3gco1CnhRFmlgMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65c80ff7fa.mp4?token=Z9Y_9Ta1yKOQAiWy9tFMNj0g-fmw7nDr4aJY6bAIkrlO9aW2q-iuwdh-bN3IjDMhjUYhTxe8Ufp0ZvbxcRZwCKg-wlgvg5-4-xYA6O_WGIrLo1qxx-S4HhuSrKAlxbycbYsV-3vuMW9ok1m3gSOEZssPw2BWtn9S24D2aj444cZYXDtinLRRxdgUN0oG4BLTbYEGlFeASSgrjM8tIUOhEKkLAL8_VJt8yRjy-6c8JIfLUWC1BLO37wTuMwf6SEPAbMnzBJXHSx-4kclIeaS6FvtXoMtdKde9BFSQP8M82M4UeLsHd-A0a4T30ZFqNYSR8ZfCMBo3gco1CnhRFmlgMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آغاز اعتراضات رانندگان و حمله ماموران با گاز اشک آور و باتوم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80208" target="_blank">📅 16:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80207">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd12e51ec2.mp4?token=dub0kMEGfNFoqWL_3sqUPHw3vAhw9s7vdccqAq1V3wMBrPlA6PCJ3WEscH-K_PJN_4VrK3brGHcQjNjAkybb3hZXBxpggKkQVCerIVZUguge3vZ1PeDumm22UGmOjMxYiLMjQ8nnxx0hpXWsIGyGugltxvXjqjgl4rirS_p0ls7bKMLci1A-AyC9XH59MmD3uQrittfhgqP-kXROMz7uawLoP0ObUPA3fT2HccCGAU84fn0w6oVdjL932W-sFHCiqXSnVRFKP9crADVGyvuhiUARDKMIU_SlCG1Qy3ChP236gWTlazDLZ_3mibZoI7TddSpy3wcKxdRA8mkU2Kublg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd12e51ec2.mp4?token=dub0kMEGfNFoqWL_3sqUPHw3vAhw9s7vdccqAq1V3wMBrPlA6PCJ3WEscH-K_PJN_4VrK3brGHcQjNjAkybb3hZXBxpggKkQVCerIVZUguge3vZ1PeDumm22UGmOjMxYiLMjQ8nnxx0hpXWsIGyGugltxvXjqjgl4rirS_p0ls7bKMLci1A-AyC9XH59MmD3uQrittfhgqP-kXROMz7uawLoP0ObUPA3fT2HccCGAU84fn0w6oVdjL932W-sFHCiqXSnVRFKP9crADVGyvuhiUARDKMIU_SlCG1Qy3ChP236gWTlazDLZ_3mibZoI7TddSpy3wcKxdRA8mkU2Kublg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش زدن مادر فرودگاهو گاییدن کجا میخوای فرود بیای  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80207" target="_blank">📅 16:01 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80206">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ای کصکشه تاجر
ترامپ: ما عوارضی را برای اسکورت کشتی‌ها در تنگه هرمز دریافت خواهیم کرد.
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80206" target="_blank">📅 15:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80205">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlFqkRalSq6lut1Z9i6FvI5aSC_49FVbtZf9i_rf5M_73mvTaaddbqywGkEmUTB0RjF3IoHTQKgOWUTxnh94j0FuXVGBa9QTjNhIq4XQm3KqbL-eHG2qBmxDytgT1f3UgFx_GgiffErzLvCS8wY8SFZAiCYCyDNrb5P-Nx14JKj3voPG_TD8klWfFKRF58Oyd24kJg8PzarB2CnCEVF5b-9i8o-jgMkWH8oPy7b551_ZiQILmYmJpLPoe8bYDYBLZaUFuDpub5AC3XGTCNilmpPFnvLbafASIreYiaJSOf15T8EAIlyfesBkP_H8sm8VUffPrup3yeBViFqozWJsmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علت مرگ لیندسی گراهام پارگی آئورت بوده.  @Funhiphop | Reza</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80205" target="_blank">📅 15:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چه عجب
دولت بریتانیا، سپاه پاسداران انقلاب اسلامی (IRGC) را به عنوان یک سازمان تروریستی معرفی کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80204" target="_blank">📅 15:10 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80203">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">جلیلی چه پولی داره خرج میکنه، کل تبلیغات فیلترشکن های رایگان شده بنر های تبلیغاتی جلیلی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80203" target="_blank">📅 15:03 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80202">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Qwlh-5PiYBSRqUAJ9FC-VdIMNkHd6xpYecdVdV4T9_nBBYOvo5AqLXRR_0erYoS3qzA0BgUd3nGyLMHhgkmiNFMKJjP3y1Y-_S4eSYZ6Hm-neuvrZMDUQkhdPHCtn_sxRLoWO2oQX3JemYqGmF4a5yUred4EhAEwjc7KT9XGt6_A1BktOYiB9lwB-ZtHLdg5rLr2zMxGDT0_AR5eVI0zE0-_uFVt0DEaOu6hz6wy3S9Y1Z6RKVzGT0rLb6sGCtIJZgT5U05HsQR2UZkDQCbB-UvvnnIZRMhAeGTJ8ConuGe6jA47dAqefFRLjzBQXn9PIYO-pFAcIIU4I5gwCnRIqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش زدن مادر فرودگاهو گاییدن کجا میخوای فرود بیای
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80202" target="_blank">📅 14:59 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80201">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">امتحان امروزتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80201" target="_blank">📅 14:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80200">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2c54c8a06.mp4?token=qu4GqTaw4lH0g3fv8Aj4RNmmdBFzchMXxCgAg1OREF2eOvHmNCrv15n6dDGdSjvP_alm2RHbbVBn86KfeQ9f8UmEVvf_cgj5kVMChFX2NdoYtn---itS3U9IKInPRvCH78CMK8bdvIJJC5uRt72PamAD58b9YnePnfwO2H7W7ZM9lpj9jxUqgCCRauGzzgXG68Swo0voKxpjOk2ML68oHKoASHocvr-rlCqPHjaL7Ic7Hm5Bc4D20rpshXbbjN1I4w0u1QEur-z4ILnx_4zjiu8c4MCeDsNPwM5b104vrhWSLY28IF2FrlzMmqaxy9pWD0pHm7ETJqpl1XUs-HOyyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2c54c8a06.mp4?token=qu4GqTaw4lH0g3fv8Aj4RNmmdBFzchMXxCgAg1OREF2eOvHmNCrv15n6dDGdSjvP_alm2RHbbVBn86KfeQ9f8UmEVvf_cgj5kVMChFX2NdoYtn---itS3U9IKInPRvCH78CMK8bdvIJJC5uRt72PamAD58b9YnePnfwO2H7W7ZM9lpj9jxUqgCCRauGzzgXG68Swo0voKxpjOk2ML68oHKoASHocvr-rlCqPHjaL7Ic7Hm5Bc4D20rpshXbbjN1I4w0u1QEur-z4ILnx_4zjiu8c4MCeDsNPwM5b104vrhWSLY28IF2FrlzMmqaxy9pWD0pHm7ETJqpl1XUs-HOyyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کصکش رید به حرفی که یارو میخواست بزنه
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80200" target="_blank">📅 14:15 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80199">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmWfNQ0CnwBo2dg3rGerEexNutka5iILoX2xqU1dcg34YrcO0aEtbtGY-mpcGVMpIbclEab6vF6H-47eyG4q94n0P9lAt_VOb5-0yTaQFIjDa_t14l9cF5PWb9yk2o1Xn5QJTE0Pr_2kmIn_4BHmrl-XQg9CviibwjREth5M9F6T6xVuQn1QnTWk8cJRvgVaaQTSR9lsvlSfReNFXDLzmKjt-Ggbp8RwzJKl5uOZ1bk9GCi-Q_joThnUb0jTAGJLXSLY2M-0UGrpmVpBWC5kMw8XovP5BI8FCJCpO3dT3NzhC81aH9aefxYereVnkkDm7BPzJ36PUndIirdFH1mKqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فحش آزاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80199" target="_blank">📅 13:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80198">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E54Gy9wPVQkJU_6lezcR-xmnJWHV9uuHJt7CoKfkprewHkdf2jZC0ZtO95_7UrVjCscWXY7eR3wP6X3MIqIDi4f5ZALZjvoxUAgsJLtrox4psH_yMsdVsZDOouFYurq7l3AOSHb6pPcf9tbiZAZ1dmzrsgygbDDR0B_7PtlwZtXvZrafvLVLgnsHoENypc1iAlW2K-n8pzDoDGmkTa4ysy1p7DD06zDiozRmBP6cjmgnmxmmsRNDKxaiUNJKNZXEMPNLLuJ2EdWE0cS6CTBpyPuR9Hzt0skuS75KVOWL4YnCEcTzoF3ZJODW4a30obvXPs8C25a_5JOrd18xVXps0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا رضا مچتو گرفتم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80198" target="_blank">📅 13:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80197">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">باز زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80197" target="_blank">📅 12:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80196">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v_qYmyY6NX5DlxFdmVM-ri_sai9PBUVEqrTYnDcI40KroZ1k1umBeCmssWxLp8ZM-Y8Hw5SlehcEZDuAbLJB6ITvy3sG_dNlowPXzJa0ntDcOvzQdffo9QWaLKZbr4D9Zb18G1Fq1VtXGBOKkdFjTYw9bm30KDmMyZqyjRu0J5nvMdsS9NTgb84AcD_6h01DzFfM5JY0crx2XUZlwXcseu_GPQfRuuwiq5g3WOgJyeE4OYtUSCfGLud73DmiHHuMIvL4mTwQMiGO54kIHoxFvzqU_f77aKy8s6PFH-VvBji2S4GlKsMxxeuKCK4POSFH6w4a7BtHeQbmnZJ5CUiuwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری تلخ هادی چوپان...
💔
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80196" target="_blank">📅 11:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80195">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW1G42xH4W1GFF2qS8DkpGNuJwMYV8BkCyRMgPPe07IJYfuNHf6rzI6R5l2GNFiinBlnmDcj8t-3EdHp0tJRhbO07OPhfS35qdJDA_CZ6RoXfbtcFN237dDVGeAFO5KmbKn69jf5Q9OYG1fTRUXBkSn2k0fpOuWc8UqQ2V4kri8XVVFsSfby5RLFk5BsnBke_cEgIRiRgh6xrBn4VzQMSqzcSWLnJgjMAwtsblzuP43Hgx9mPKolo2F3sOvGnlp4zvPnAPk4M6DL-Th0cr_vbxngwdkYoI4QTF6e4QtnTU6PfSR1IEIhpxRwFYEfMnwipuuLVUhBDIYFoEa0AQBWCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دلم برا حمید سوخت پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80195" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80194">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2VhCQar9fPBwEx_YdoFivM2XulpEtuQHpKPPSx_fsnHV9FL52rAY9-ChMsIWgZebqNk3dKqNs7oeO9supZfn2SWcrcKCffuRp81YgxpqiN-15On1J1H7OSjaXoAwk3YtRjzVeUeuQwb4RPjy1RMSED2wmIw4TPktQLLGI1EPmPHPQxIGYvRP6Su9GuKoOzXgokoHQXrv4lRDVl_q3ymAWT6IS9P8XDtolzHVheUGh-yohAoxfH8OYXynIkK-WEWfStM_Uws_GCJYi0kLvTd97UjKW2ADFyxiSCPktCT-tutaT5wzgyn01vv0u9PzwM83vEztuwC7-0I5vXNDQemx72EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826125c863.mp4?token=h1RPw_DCRo4smWlbuaEyJb9zTZDZ3OST8B2XCDwyNejAkkRwcSElosGBb-EtGumrnijcofFTi88sNGwmpZJLHAn4Rwc8uG3cDCPvsLZl7FT4ALUXdtjvhXJirxSOv2ctSISZAmY23EPWmqgY7t3PKzeK-rawmOzYRt3BfLmmDxIxADt_QAbQR7n7UAjCbVquBUu0v42526FJprtAqq98fQa39_NF9rmG60lNzoyYy-I2-DfGY3FDydVfrl8FvmmGussQZTvhoHSSWuPrFhBqEGCKGSWkyhrpKQPfP1LN2pdeisyaoMio43iETWlIk13FK4vYi3prQFu81pMqFTZ2VhCQar9fPBwEx_YdoFivM2XulpEtuQHpKPPSx_fsnHV9FL52rAY9-ChMsIWgZebqNk3dKqNs7oeO9supZfn2SWcrcKCffuRp81YgxpqiN-15On1J1H7OSjaXoAwk3YtRjzVeUeuQwb4RPjy1RMSED2wmIw4TPktQLLGI1EPmPHPQxIGYvRP6Su9GuKoOzXgokoHQXrv4lRDVl_q3ymAWT6IS9P8XDtolzHVheUGh-yohAoxfH8OYXynIkK-WEWfStM_Uws_GCJYi0kLvTd97UjKW2ADFyxiSCPktCT-tutaT5wzgyn01vv0u9PzwM83vEztuwC7-0I5vXNDQemx72EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
آنالیزهای اختصاصی بت‌فوروارد، مرجع تحلیل مسابقات برای تصمیم‌گیری هوشمندانه
🎲
📈
در بت‌فوروارد، هر مسابقه با بررسی دقیق آمار، تحلیل عملکرد تیم‌ها، شرایط بازیکنان و مهم‌ترین داده‌های پیش از بازی به‌صورت تخصصی تحلیل می‌شود تا با دیدی کامل‌تر و اطلاعاتی دقیق‌تر، تصمیم‌گیری کنید.
📗
برای مشاهده آنالیز اختصاصی هر مسابقه، وارد وب‌سایت مجله بت‌فوروارد شوید، سپس نام تیم یا دیدار موردنظر خود را جستجو کنید.
👍
ورود به مجله بت‌فوروارد
کلیک کنید
mag.betforward.com
کلیک کنید
mag.betforward.com
🅰
r22
💻
@Mag4ward</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80194" target="_blank">📅 11:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80193">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">علت مرگ لیندسی گراهام پارگی آئورت بوده.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80193" target="_blank">📅 11:02 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80190">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یامال بالاخره ۱۹ سالش شد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80190" target="_blank">📅 03:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80189">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">نه،تعویق نخورد امتحانت، بخواب ایرانی</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/80189" target="_blank">📅 03:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80188">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">امشب با اختلاف سنگین ترین حملات از سوی امریکا رو شاهد بودیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/80188" target="_blank">📅 02:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80187">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سلام باز صدا پهپاد میاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/80187" target="_blank">📅 02:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80186">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تایید نشده عمران عقیلی، رئیس واحد ارتباطات عملیات ویژه در فرودگاه اهواز ترور شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80186" target="_blank">📅 02:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80185">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQpj56c8bRuskn9q-MpZUjKbEvqHk6lATbtxrzd4fnAQjUpA7S72uantjVauIfCaVQ2b2xHb83AH_gClSAZxAckw1hf9My7qyaKeu6YESz99v1eR8kljkeiqj8gKHakJATF-eKDZDR1ejaTVSn9yprqW5iN2pQP7vnXegQK5krMK2RJc1fuHaRDQktZDRMl7SPyoLDQJUQ_ra1OKAgLr_M2cvIP6PmbG26GxybOfY9GJcJqS9Z7qZdyN6qA0Dmh_8uLG_lOw1eoh6ZXksPTpc2OG-XC28pfrBJ6E1YjPU1N-B9Hy2Ck1lK4uP2y0h10tqewS17lwE0q4zj1eKwe71A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوافضا سپاه بعد از اینکه همچین سرباز آماده ای پایان خدمت گرفت طول کشید خودشو پیدا کنه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/80185" target="_blank">📅 02:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80184">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">راستی اینجا(شمالغرب) یه ساعت پیش داشت صدا پهپاد میومد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80184" target="_blank">📅 02:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80183">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تایید نشده
عمران عقیلی، رئیس واحد ارتباطات عملیات ویژه در فرودگاه اهواز ترور شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80183" target="_blank">📅 02:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80182">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">این هیمارس هیمارس که میگن این لانچره‌اس که خفن ترین موشکش 500 کیلومتر برد داره فقط و برای جنوب کشوره  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80182" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80181">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بچها شوخی نکردم اسمشو  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80181" target="_blank">📅 02:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80180">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIWuAVUbh-oCebEc13KAOXi0BI-HaJXyJ9KlT3rUPFb6ZVwzcX_9BmuTG7tvm-ht9DZ4gqohNlee3uw0oTKvIXWOBwGfG0sLFkY5Ena9xNOd_QcrkDG1ho3C9NFKY8Hj8qwPYgTkDZAH_tnWNNgpElTDw8dK_kU1CpATp_PnhTza7USdYZqRdS-Pdy_nwlwsYkFZx5-Ldawr1g9egyqfmNEeSvn0iOci7Z2kCefM-_3yZ7y_GeStGjfKzWbprDGID11nDzBGO9t308x9wGvhxnBJBOqrTl2bTlC2Ff1YJbZkFZvcj1uVCM9_Z3JaOK6jH6pIMtGrWkIXmHJAgax56A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدافند مجید در کرمانشاه فعال شد  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80180" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80179">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">پدافند مجید در کرمانشاه فعال شد
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80179" target="_blank">📅 02:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80178">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یزید تو چرا بیداری دیگه
معاون استاندار خوزستان:
در ساعت 1:40 بامداد امروز دوشنبه 22 تیرماه نقاطی در شهرستان‌های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80178" target="_blank">📅 02:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80177">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHX5umPHRpS2atF-nHPSXIScgvqEOY-LcjDcoLGQeqBe2C-j0U484_Lqn5Yjaf_G8WB21fBNi8nrFEmbXPxwXaQ6o-9n6bm3VXz-pQwzZtpLQjaMb-Rz0-HGAN24X-wCnvSQ5gR7L_xiPpeK2c729SJweiB_wwSrxjyKQ1TTjGdoQRR4v4sqcrZHAqQ_q39XV8dCHpt2R6h5ph5WYUrjonrjF_5jCujRR67YOW8f5ol0nVCfmfgzq19WmLVhZlfeZmazaJtliEx3KlAvaXfUXAqxr5i9DO62uIGJS1v37Y5whmkaEi9XKpRw4QMcsXqyGgcxFoiCkA22ggaI6UKE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هیمارس هیمارس که میگن این لانچره‌اس که خفن ترین موشکش 500 کیلومتر برد داره فقط و برای جنوب کشوره
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80177" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80176">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhiDyDvRUOhnQfLTc4lbwy8ngzO_CRLWnLybFyenVyrdmDMdqzKcyR1dj7WuDQLDOFOtIME494hw2VTfd-yfWts8oVvoIuqvo4Q43NkgQN-DWcn-dZczY_LPcRiSyXEs3vA19KoYIaCtDoBalE0Gl2CR8mr4zK2ip20Hsbs6gr32cqzrBaqF-r6SZ77Vc4fh5FrexKW4LwDfb4074TpZDFCzhcI7gAaXn1xp6Ewd7Ije_nkF_arfi31ZiZ9liOFAyWGauFzw07ZHG3YYRgRjY0EaebR6hz_8xIF6e4y2WbIROzdr4u1K98Fmpuv5Zmz1OeAu7Yo5wF562A3scei2Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی انگار باز داره جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80176" target="_blank">📅 01:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80175">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جنوب کشور عجیبه
روزا گرمه شبا جنگه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80175" target="_blank">📅 01:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80174">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دانش آموزای عزیز سریع بیاید چنلم سوالات امتحان پس فردا رو نذاشتم ولی میتونم دلداریتون بدم.
https://t.me/salamkhobichekhabarchekaramikoni</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80174" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80171">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">گویا اهوازو با سنگین ترین بمبا زدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80171" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80169">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یه زمان به لبنان و سوریه و عراق و این کصشرات میخندیدیم که هر روز تو کشورشون یجا میخوره، الان وضعیت ما بدتر شده، ممنون از جمهوری اسلامی   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80169" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80168">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یه زمان به لبنان و سوریه و عراق و این کصشرات میخندیدیم که هر روز تو کشورشون یجا میخوره، الان وضعیت ما بدتر شده، ممنون از جمهوری اسلامی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80168" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80166">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شب شد و همون همیشگی و تو همون شهر همیشگی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80166" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80165">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شب شد و همون همیشگی و تو همون شهر همیشگی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80165" target="_blank">📅 00:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80164">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بعضی منابع هم میگن 3 تاشون کشته شده</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80164" target="_blank">📅 00:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80162">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KR7pwWGULDpNbJsc20OjCiZnrbM56R5iJUJZzHfk3GOEVAQunR94LOyjn8Hm3cu-ddwDHMeX2OjmQ7ANFSDdBcA8UYZB69cmfqqdx7RqtCvPaZf3_a9YX5pBU2RJS0e6oMqBo4IfoaBKsbRh2q7nDKlMixJ6M5DHIHcifjcEoG84ewHV16UEUJLaQ5G6sAV9n1GTCTdecYQOyjHDVf783y0WTpXdbwVGcP4mxVbwU59JHF5qVirCpMINqkTvZgyMd-WqzAwdMxQhEDNFih3KEMRGRb7btWbdFqHY_pm7PNjz5a-HQKKnHpS76YNQr2d27lEOagGbUKrwJQ1RX0Kh5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80162" target="_blank">📅 00:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80161">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcJRaI1t7RWsc_XCGXgXuhIvRqY9i3FsT3DpSoM9ZxrssTyxvwjtD31bqbVf_K1wydVZ16gXmWikX_qgGEA1m2c2rH1R-HuUtjUEL1Z3EgdZPU6REDFhsrl_wksTZez3OwengcUTkRCZ9huObOsBNUSfZkO6m-arFFCoZSGJZW5q3uoyXEHfX1KsELdhlv7g_klQjlXKywBSonxsc3QjpYJaCvL1U2A4cakhVGU7KD535vQ1F64cqpx4L88bHTS0k8lScbcF7P08ym4JhzPGZWq1Qs7AGtx6pwDjtLkpGmf89jJJuzkBP0YDaRjSCLsOTE-CP8ahds4dmRAF5cVC3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرینو کصکش فقط گلر واینستاده فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80161" target="_blank">📅 23:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80159">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EqxZ0a9hox0LZgGsoSmJV7Z4qQN7Z2zRD_yzF5_AdHsrPAafp0zdQvPAaQQ5f_P9L1El28VwEc4gqI1mGFCkqH193NUDu5va-TUoT4cATWrum35guWz0U8ULqPJY2pZaVUnFRu_7UsYSNBRvpuL5XWheN0HHWNRCWjkMs6hH_jzdoM1wjA7UHKeG7irFqhtb7kbgcF1sl6Q1Z5T0ZZzWaXe0Cu8yCBjYz-3bMw8WmXp-qrQegQERjWsZ4jVMkv5gQlEHYJXuUEl5huGV0VLiXIt97ySB7UHmtoxPNHRWfj4HAmovQ3GgUsMc0HfXj0Fg84n68OSXG-o4VXevSx8gxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXUipmtb2degKroiOIGlwfAM0NF0eqSfu7_qQSi4a3YdaWUVS6bji-SaNAWv_cWQn2TTUOUOPxwULd9YHeTbYTg72lF4mb-7apHtFB1U_XcxL4unzY3LvIw0D4CIeZJ_C_sEgUzQTe-bjypCECbm6XL5oz2dphIMD73Tnv1ATkXnUdqGKSRs4s1DV9uvCBH5AaQDjrNgKsGpKgAK_g7MT-JPWtJDOJQMnkIC0YqxPj8nTINx681jtyI4-xfuFPDeyJ11s4BUAvE-n-HKh7tiQ3z0CZOv3EYSExGbABJbRXAYOX9oQaHgAycxN-6-F7mODvAii465BgY3muKNrpTUFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب بخوابید خیره
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80159" target="_blank">📅 23:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80158">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80158" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80157">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">راستی 021G زنده اس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80157" target="_blank">📅 22:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80156">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بچه ها یچی میگم نخندید، ویناک و منیجرش معتقدن مایی که زمان جنگ وصل بودیم به سپاه وصل بودیم و قراره بعد انقلاب اعداممون کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/80156" target="_blank">📅 22:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80155">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بازنده تمام بیفای دکی صدف بدبخته  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/80155" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80154">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بازنده تمام بیفای دکی صدف بدبخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/80154" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80153">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpbGZr_bFyV-MbFFIQHDCIlTMtCO9vumY8eOZ89oVfUZ161n0jf6T0yrIDhqCqdD2Wzp9cGzApT9ulZo2lXLVzTE7kU8puAWuxaTAAwxBFYpVomc3iew_OO0lFxvz4qSCDOIagt9UzTfq99ULLBhk0XAVYOjv3NR3m7She2l-kBgH6ZpsqoBQxeYZdXZ94f5qrGPrfvIMvy2ux-_Jty-HOMYNg2-ugvHOXa5MKSPCNYnErKM-uk9Pb8qtml5y0CjcVbuMtkkPbFjvt4LfEI5zsSMPLuWtUp-y8Enpwnk42f71Tmpt9vyyAW3o2eCqvNnKyO1-jWhAcayMH4TQi2YRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر تو جنگ و بیف بعد 6 7 ماه حضرت لنا رو بچسب پسر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80153" target="_blank">📅 21:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80152">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">این حرف ترامپ که میگه امشب بصورت ویران کننده ای ایرانو میزنیم فیکه هنوز چیزی نگفته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80152" target="_blank">📅 20:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80150">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">14 تا سرباز امریکایی زخمی شدن 4 تاشون وضعشون خرابه بعضی منابع هم میگن 3 تاشون کشته شده اگه سرباز امریکایی کشته بشه احتمال گسترده تر شدن درگیری یا حتی از سرگیری جنگ زیاده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80150" target="_blank">📅 20:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80149">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e73f890bb.mp4?token=R9KSncndUzDgFvI35mh8BUi6Bpo9P0YT_gB1MRkZ2xLeRzkziciBOaeoUcYhULrKKlymBUCvS4-hGOochAYdinNLZHZfAbJ05Aiegc84VQUlgaSY4Enil3LlVQTWf6D8MSRWmRwzADZYqcW12K8KESLeMxYCKHFIxAGgQrlDjDsFQ7aLHQ5dBcaWlIU94GtgpN4wRHIikz2g6cmlZSS7fz4l1hdQglaRpweXKPKdGzA7QfCW9mGjWAKpOyJAEw7NKJRa4PS5oAYiOmqCkO1xcyLMzMAjdloO6dNN8Q7H5VfLT5otJ3vwYGreeREJbJj-ES8KfmmFKCoo9sWBYDkQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e73f890bb.mp4?token=R9KSncndUzDgFvI35mh8BUi6Bpo9P0YT_gB1MRkZ2xLeRzkziciBOaeoUcYhULrKKlymBUCvS4-hGOochAYdinNLZHZfAbJ05Aiegc84VQUlgaSY4Enil3LlVQTWf6D8MSRWmRwzADZYqcW12K8KESLeMxYCKHFIxAGgQrlDjDsFQ7aLHQ5dBcaWlIU94GtgpN4wRHIikz2g6cmlZSS7fz4l1hdQglaRpweXKPKdGzA7QfCW9mGjWAKpOyJAEw7NKJRa4PS5oAYiOmqCkO1xcyLMzMAjdloO6dNN8Q7H5VfLT5otJ3vwYGreeREJbJj-ES8KfmmFKCoo9sWBYDkQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80149" target="_blank">📅 20:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80148">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qUSApus5WCVKm8yhvwOctK73Y4yiT-tSBeqVUwQ9QlqfDCGBY1tHMlf_Tzr3ZF9sNbxgkZxwu15UgbvLNJ9TiYaPeD-xUPJfD__Dn4rHm0akNlz_EmIKV9GLAFjKz27njVrYU1L4NCXodaBs9OX39Fpsx7nCWkuVHys6-YUTxEAG6ez8fJekra_tjdqQr1urOKDzUrpJCLt6RxxQaptQL1lCsGM6WHMs1toVa5kh-bVuihhmnAnp5ws4J-uBWCytlUuceHCjsf76F2Uj5YF5wRPZjEhR77e9KO8NwDtHfGjEskZi3ElVgxyafA1p67fk0rbz_1vy2vmCIeYdSzHh4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داداش تو عضو بلادم نبودی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80148" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80147">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
g21
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80147" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80146">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سلام فرید جان ما قشمیم اینجا رگباری صدای انفجار میاد تموم هم نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80146" target="_blank">📅 19:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80145">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">جنوب کشور درگیری بسیار شدید گزارش شده</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80145" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80144">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فارس: شنیده شدن صدای چند انفجار در بندرعباس و قشم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80144" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80143">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وضعیت طوریه که ممکنه جزایر نشینای ایرانی امشب تو ایران بخوابن صب تو آمریکا بیدار شن
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80143" target="_blank">📅 19:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80142">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">خلاصه ترک:
کس ننت
کس زنت
بابات سپاهیه
پدرزنت سپاهیه
تو خایمالی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80142" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80141">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80141" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80140">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80140" target="_blank">📅 18:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80139">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80139" target="_blank">📅 18:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80138">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">بیت چرا داره هوس شد؟</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80138" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80137">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80137" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80136">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80136" target="_blank">📅 18:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80135">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80135" target="_blank">📅 18:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80134">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این که همش ناموسی میده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80134" target="_blank">📅 18:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80133">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">اومدم ختم کاکولد
بجا تو میکنم ننتو بلاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80133" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80132">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80132" target="_blank">📅 18:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80131">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بیف سر دقایق بیشتر موزیکه نه پانچا، کصکشا مگه پادکسته</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80131" target="_blank">📅 18:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80130">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80130" target="_blank">📅 18:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80129">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80129" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80128">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcSIBbk9kHV-K-DAuWWE4N0qnQcraO3D3n6dVvFvLEMajhb1Y4RkvrauSoYx80pDrfIqW8xCmHtGGcHOHCYbMRV7xsjeXFsfptfgRIKnxGUB1CUMqxG71zBBagxmpYwxzkn_liwTl2doFFmrCh6dWtaKQvk6jDtNtsslBLLOroEuQ_hIGOibJgoPJdV_ukppt49QQ4GBk0jnG8hb3iOrn9OWLfpbSL_alNf-wp3LVwEOD403DRkugZ9qX11fTOl7Ys9jGt-HY0jJvnsTr_5Vn5Euszc9ztVHFYsdpv9k7HrguXJtXGrxNTokkqcQECwcjgC13-Hp3KMU1GKf4s4LVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80128" target="_blank">📅 18:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80127">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ویناک کسکش بسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80127" target="_blank">📅 18:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80126">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6x0C4o7Yk9EOfcsIjc7v1z9NSeeIphKf9ovGgeTssP6KvE5THRo8e9yFUdNvoSbM8dQeMY-KZh4gy1eKtn1yG-eR2jedsFnenDL-V5-Grhm-Vm6koQavdL_w4QiIt3DXj6De-kW6uXsF_lOJj9jmD8rGDb_vl3gEwGdjLFpZmu2Dca62lOdHOwrHvU4rOU7bEN9q1df1MsarISAYEYt0XaKQUAxfqDkDWEvEVhr4PDvJJNPOeHXrjnIOLVJN1ARpz-CcoANq_3cma1Lh0DvRpHkt0q3njqXq8THBcSIURZxyx9rzJj239rlPwhwawzY14pTf5zc00h1FibgQKB1ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۳  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80126" target="_blank">📅 17:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80125">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ویناک فک کنم داره موزیک یساعتی میبنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80125" target="_blank">📅 17:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80124">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">حالا ما هیچی، کانر خودش خجالت نکشید بعد اینهمه تشریفات با مشت اول بگا رفت؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80124" target="_blank">📅 17:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80123">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6869027e93.mp4?token=bbjWScTZ7KBHVTcTvytGO9PZ_NAFlLCCduh3VqQ-Tu3TQ_oD55QPz1D8lPfORkoAU_NpE5Ue68jg0Uff7xDwmLaIfkGw6s8ix2tR1h7joKDPvBR1OkVAb1jQVvMy8ffeBbuArGP5TgX0-EQZPe1RaggCIwtc3ojbPkOj1lxcB5uFmuPL6EIkrp_HkC-iXKcty_kl_GiULfobaHv2vgqHPoWoNSFsRa0tTBO7oSJBxMqmYIZDaNV6vjBOcgn1SOhr2t-PrlMBInlXfPHUPC9LHgN9wGQmBwsvfj6C3ZMGm5rDcc0jHHVNdrcP3-Y7Z3wfdjnlqq3uGP2nZEOT6QWxVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6869027e93.mp4?token=bbjWScTZ7KBHVTcTvytGO9PZ_NAFlLCCduh3VqQ-Tu3TQ_oD55QPz1D8lPfORkoAU_NpE5Ue68jg0Uff7xDwmLaIfkGw6s8ix2tR1h7joKDPvBR1OkVAb1jQVvMy8ffeBbuArGP5TgX0-EQZPe1RaggCIwtc3ojbPkOj1lxcB5uFmuPL6EIkrp_HkC-iXKcty_kl_GiULfobaHv2vgqHPoWoNSFsRa0tTBO7oSJBxMqmYIZDaNV6vjBOcgn1SOhr2t-PrlMBInlXfPHUPC9LHgN9wGQmBwsvfj6C3ZMGm5rDcc0jHHVNdrcP3-Y7Z3wfdjnlqq3uGP2nZEOT6QWxVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشاسین تیراختور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80123" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80122">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pZeWi4YkvWv9gV1ByC4_DnvjJ2NARTfeG62rv57kzwhZdkQ7TLz_HKAEEVVTgq7JrAfOqiN8xlh7Iyf7ThZ3QlJnYMvVjIdiBY7E0lhIiWWfPtEBrlmIxKrPFqmh0wiX8ThUNYj-hW-e6b3gH3nbpqkIUdVNuz9Zv86Wu2Ksc0Ss0Rzl055zQ_uCxU01u6sliD_0xG8xWHsNMBWb8iOloYICQ2Oojb6Ym6QnVdg0_Evdqsbcmj596xEOP5t2VujdG0uOY2upsvVMBAvKmiqnVmxKWo6ZPh1c77HvNqg9zc5m2KQmjIBAzzyg3LLAQHjZnQbwjV_r86fBLHGwhdi33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده من تو این هوا بدون کولر چطوری زنده بمونم وقتی برقم قطع کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80122" target="_blank">📅 16:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80121">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دشان از تاکتیک های ناشناخته فقط یچی شنیده ها، اومده خبر داده بیرون که سالیبا و اوپمکانو همزمان مصدوم شدن و نیمه نهاییو از دست میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80121" target="_blank">📅 16:06 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
