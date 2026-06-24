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
<img src="https://cdn4.telesco.pe/file/C1qMsIJp2fuhFPQW678y7Knk-7YVRhRBvMltrrjG0kqM-XuD2OsllIdyrTSk3Z6Nx2zRjjMtWaXgNpA1ap-uCrsMCxOwzN2wBLBSOMBWO-6aOgwV88jLShGk-5PlzphVVU9BkPSbxsplokeasLb2r5K-h1FOdu7dQf4GFU3NebqfqNm8DsEYtjG4Ur9NEGdsaWRRhImYMN503U7mse7hbaYOdgIe83-qle6aZ84IXYYeibN0dO20hLhdHUp4v-Ylap2-GAv-W_cixekzeNwi53Y6PeYMC_hUMx41EqnLmTdO9uUNXkLLa2-BfGmiVf4csuc7WJk1iXITVX-75SvKCA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 آموزش سئو محسن طاوسی</h1>
<p>@mohsentavoosiseo • 👥 7.6K عضو</p>
<a href="https://t.me/mohsentavoosiseo" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 من تالیف و تولید می کنم✅. نه ترجمه.نه اخبار. نه گرداوریدوره:mohsentavoosi.com/course/seo/خرید دوره:@mohsentavoosisupportyoutube.com/c/MohsenTavoosiInstagram.com/mohsentavoosi.seolinkedin.com/in/mohsentavoosi</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-770">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 402 · <a href="https://t.me/mohsentavoosiseo/770" target="_blank">📅 12:38 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-769">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سوال یک دنبال کننده که احتمالا شناخت قبلی هم به من نداره:  نکات سوال:  پارتی نداشتم کار خوب گیرم نیومد گفت ریاضیت قوی نیست پایتون نخون.  تحصیلات بدون فرصت خوب اشتغال.  نگرانی آینده.  هوش مصنوعی جای سئو رو میگیره؟  سئو رو برای کارمندی یاد بگیرم.  ۹ ماه کاراموزی…</div>
<div class="tg-footer">👁️ 924 · <a href="https://t.me/mohsentavoosiseo/769" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-768">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/injJ1fP1tjkGOMw7dlWuwhDqNiJ9Ez0KkvG3Ty0S-6XzrBPk30P4it_WQtPzzCLNWGUU0IBgZsIz5JI5sPxjHbiAS1dDHopC46mJXBrNbSsZjTI46Byh2gLdqrcjgIjiGm8dt2iL374nXcnBfIKe8xKyvEs8fzsq153LWD8SfyhQNsdjE5IpDcTevfcTEJLzYvHO-YQvovZA2R_iG_1pjtQTTBpUtK4Q-ef2SBnC2cSfO70KfyompqGPsDaUQjQbxuN0T6iZAbbilWOjXDnxg5fRur0m17AB_l9BHKYBaHY4ku7_WLL_JFkDA-geo3StlSTLV0iSqfKAyGaomGSDWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوال یک دنبال کننده که احتمالا شناخت قبلی هم به من نداره:
نکات سوال:
پارتی نداشتم کار خوب گیرم نیومد
گفت ریاضیت قوی نیست پایتون نخون.
تحصیلات بدون فرصت خوب اشتغال.
نگرانی آینده.
هوش مصنوعی جای سئو رو میگیره؟
سئو رو برای کارمندی یاد بگیرم.
۹ ماه کاراموزی رایگان
تو ویس بعدی فقط جواب نمیدم. تحلیل می کنم این  صحبت ها رو.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 980 · <a href="https://t.me/mohsentavoosiseo/768" target="_blank">📅 14:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-767">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">چرا کامنت ها و ری اکشن هارو من باز نمیکنم؟ بخاطر بحث اقتصاد توجه: https://t.me/mohsentavoosiseo/364  نمیخوام ذهنم درگیر این شه که اااا پستام کم لایک خورد. کم ری اکشن مثبت داشت. ااا منفی داشت. . خیلی لایک خورد روحیه بگیرم. و وقتی کم لایک خورد ناراحت بشم. یا…</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/mohsentavoosiseo/767" target="_blank">📅 14:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-766">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">من دهان به دهان شنیده بودم از چند تا از دوستان که زمان مصاحبه برای مجموعه خودشون، کسانی که دوره رو دیده بودن خیلی از نظر فنی و مهارت نرم، متمایز بودند.   افتخار میکنم
❤️
❤️
اما الان دغدغم اینه که کسانی که دوره رو گرفتند، کامل ببینند. چون درصد کسانی که کامل میبینن…</div>
<div class="tg-footer">👁️ 909 · <a href="https://t.me/mohsentavoosiseo/766" target="_blank">📅 14:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-765">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.06K · <a href="https://t.me/mohsentavoosiseo/765" target="_blank">📅 14:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-762">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سوال دانشجو:  من ی مشتری دارم که سایت خدمات راپل و نماشویی ساختمان داره گیر داده که فقط مقاله میخواد و ماهی ۷ بیشتر نمیده و من باید بهش تضمین بدم تو قرارداد بیارم که رتبه میگیره صفحه اول. این حرفش منطقیه؟</div>
<div class="tg-footer">👁️ 1.09K · <a href="https://t.me/mohsentavoosiseo/762" target="_blank">📅 13:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-761">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFqaYWlLMjBH7JG_1YEclAtfs5Z9k5bsoF7xCyaM9ts0F2Dp4EGptEhwypmMGow-KDBhY_FfOLcyxefTuJDnHxSYAJ5t5JwwRPFqUbEfzOjc7umP4mvduIWwHkYeMdK7DF295SueMrJCJi6AMNzfm4zZm0wpKPVGCsAgJtzwmHb1PmbcjQb5RZrm02vcq_SFkbavVQTYRQg1bVHRt0RTSMgw6ecbZnhi_-MA3T58VqM7w0_8rQi5D8wJdlEVf7O3NgYg_BsWgR7LcGvS7zI0kDsQg2VdzLydM-tP0rMgvKarjt_EBsG2w3-VBsV2k01SszXPx_B2w8qcuDVmzJJu5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوال دانشجو:
من ی مشتری دارم که سایت خدمات راپل و نماشویی ساختمان داره
گیر داده که فقط مقاله میخواد و ماهی ۷ بیشتر نمیده
و من باید بهش تضمین بدم تو قرارداد بیارم که رتبه میگیره صفحه اول.
این حرفش منطقیه؟</div>
<div class="tg-footer">👁️ 1.07K · <a href="https://t.me/mohsentavoosiseo/761" target="_blank">📅 13:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-760">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اگر کار دقیقا قابل برنامه ریزی میخوادی جای اشتباهی اومدید. SEO به دردتون نمیخوره</div>
<div class="tg-footer">👁️ 988 · <a href="https://t.me/mohsentavoosiseo/760" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-759">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سئو برای این نیست که بهار شروع کنی تابستون بیای بالا محصولات تابستونی بفروشی یا برعکس برای زمستون و فصل.
نمیگم نمیشه. ولی نباید روش حساب کنید. اگر کار دقیقا قابل برنامه ریزی میخوادی جای اشتباهی اومدید. SEO به دردتون نمیخوره. هرچیزی هم میچینید فقط رو احتمال و تخمین با بیش از 50 درصد احتمال خطا هست.
کار با زمان بندی دقیق میخوای اورگانیک سرچ به درد نمیخوره. گوگل ادز و سایر روش های دیجیتال مارکتینگ ادز محور فقط. که میتونی در لحظه و در روز کمپین رو شروع کنی و تموم کنی.
گوگل خیلی تلاش کرد کنترل رو از ارگانیک سرچ باز ها(SEO) بگیره که گوگل ادز بیشتری بفروشه و برای گوگل ادز تقاضا بره بالا. و موفق هم شد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/mohsentavoosiseo/759" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-758">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/mohsentavoosiseo/758" target="_blank">📅 11:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-757">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">سوال دانشجو:  من رو یه سایت دارم کار میکنم که تجهیزات آشپزخونه میفروشه.یه دسته بندی داره هود اخوان.و تقریبا ۵ ساله همین دسته بندی رو داره.زیر مجموعه میتونه هود مخفی،هود مورب،هود شومینه ای باشه با توضیحات و مدلاش.الان اوکیه من اضافه کنم؟یا چون همون صفحه هود…</div>
<div class="tg-footer">👁️ 1.21K · <a href="https://t.me/mohsentavoosiseo/757" target="_blank">📅 11:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-756">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سوال دانشجو:
من رو یه سایت دارم کار میکنم که تجهیزات آشپزخونه میفروشه.یه دسته بندی داره هود اخوان.و تقریبا ۵ ساله همین دسته بندی رو داره.زیر مجموعه میتونه هود مخفی،هود مورب،هود شومینه ای باشه با توضیحات و مدلاش.الان اوکیه من اضافه کنم؟یا چون همون صفحه هود اخوان رتبه داره اینکار رو نکنم.</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/mohsentavoosiseo/756" target="_blank">📅 11:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-755">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.52K · <a href="https://t.me/mohsentavoosiseo/755" target="_blank">📅 20:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-754">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سوال دانشجو:  من روی کیورد با مشتری کار میکردم و قیمت میدادم یعنی یک سری کلیدواژه میداد و میگفت اینا برای من مهمه و من کار میکردم میوردمشون صفحه اول  علاوه بر این براش مقاله هم مینوشتم و تو بقیه صفحه ها هم کار میکردم  و تضمین میدادم که میارمش صفحه اول اما…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/mohsentavoosiseo/754" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-753">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سوال دانشجو:
من روی کیورد با مشتری کار میکردم و قیمت میدادم یعنی یک سری کلیدواژه میداد و میگفت اینا برای من مهمه و من کار میکردم میوردمشون صفحه اول
علاوه بر این براش مقاله هم مینوشتم و تو بقیه صفحه ها هم کار میکردم
و تضمین میدادم که میارمش صفحه اول اما این تضمین از دید دوره درست نیست
حالا میخوام بدونم مشتری روی یک سری از کلیدواژه ها میخواد بیاد بالا (از 98 تا 1401) روش کلمه ها کار کردم و صفحه اول بوده الان افت کرده و میگه کار کنید تا بیام صفحه اول.
سوالم اینه مشتری از من در برابر پولی که میده تضمین میخواد قبلا من تضمین رنک میدادم
الان چی بهش بگم برای تضمین؟</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/mohsentavoosiseo/753" target="_blank">📅 20:28 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-752">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">سوال یکی از دانشجویان:  هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه  صفحه اصلی هم که معرفی برند هست هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟  با کلمه هایی که براشون دسته بندی داریم هم نوع…</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/mohsentavoosiseo/752" target="_blank">📅 18:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-751">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ادامه جواب بالا
روش جادویی من تو مشاوره هام(توهم جادو)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.37K · <a href="https://t.me/mohsentavoosiseo/751" target="_blank">📅 17:35 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-750">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.36K · <a href="https://t.me/mohsentavoosiseo/750" target="_blank">📅 17:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-749">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.4K · <a href="https://t.me/mohsentavoosiseo/749" target="_blank">📅 17:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-748">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سوال یکی از دانشجویان:  هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه  صفحه اصلی هم که معرفی برند هست هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟  با کلمه هایی که براشون دسته بندی داریم هم نوع…</div>
<div class="tg-footer">👁️ 1.39K · <a href="https://t.me/mohsentavoosiseo/748" target="_blank">📅 17:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-747">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سوال یکی از دانشجویان:
هدف از صفحه دسته بندی محصول اینه که خب محصول بفروشه قسمت توضیحات هم که شاخص ها کیفیت و قیمت گفته میشه
صفحه اصلی هم که معرفی برند هست
هدف از اینکه برای بعضی کلمه ها لندینگ پیج داریم چیه ؟
با کلمه هایی که براشون دسته بندی داریم هم نوع نمیشن؟
مثلا الان یه دسته بندی داریم که دسته بندی تجهیزات هتلی هست که داخلش محصولات لیست شدن
و یه لندینگ پیج تجهیزات هتلی برای تماس بگیرید و هتل های تجهیز شده و …
اینا الان هم نوع میشن؟</div>
<div class="tg-footer">👁️ 1.47K · <a href="https://t.me/mohsentavoosiseo/747" target="_blank">📅 17:25 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-746">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سوال بعضی از دانشجویانی که تازه شروع کردند:  داخل این دوره ی اموزشی طریقه ی این که چجوری کلمات کلیدی که پیدا کردیم رو تو صفحات بزاریم رو اموزش میده چون من نه از رودپرس سایت یا سئو هیچ پیش زمینه ای ندارم و داخل وردپرس اگه من بخوام کلمات کلیدی رو جایی بزارم…</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/mohsentavoosiseo/746" target="_blank">📅 17:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-745">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سوال بعضی از دانشجویانی که تازه شروع کردند:
داخل این دوره ی اموزشی طریقه ی این که چجوری کلمات کلیدی که پیدا کردیم رو تو صفحات بزاریم رو اموزش میده چون من نه از رودپرس سایت یا سئو هیچ پیش زمینه ای ندارم و داخل وردپرس اگه من بخوام کلمات کلیدی رو جایی بزارم باید کجا بزارم ؟</div>
<div class="tg-footer">👁️ 1.51K · <a href="https://t.me/mohsentavoosiseo/745" target="_blank">📅 17:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-744">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfUrO-7_Ko7e9Pk2q4F2iboAmBY2qPuhDnkGXwN36pNFkR4BqJVo2ap2FoGb6l4ZgT9OV1MAmn7QRGDrk315hhZy3Q8qQgpSSMIEtlFoTcZRQrypsrtuwCgn0Vy1bO6ERJl4vSCz-a9fNbkFHPLfj3MMo3UsOK6Ute7mnNfcBQYkaNVi8yED0Gqia-E71CxjKG5eMAunfcDfzi7z4bELWZYEhEnm2hyczZeYsFhnvyThnvqtriva9z0x9V6_VzLe81FWyPWZ5lUx_4vxOQ6lRZHJdk5AdnlPZZrXD_3SFh5W6gXF5oxnpvDj9MGkHVbRMD9kPjVd0DcG8AKkvSARZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شما هم فکر می کنید این بنده خدا و این بندگان خدا، ساده اند؟ یا من تنهام؟</div>
<div class="tg-footer">👁️ 1.72K · <a href="https://t.me/mohsentavoosiseo/744" target="_blank">📅 09:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-743">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چطوری بعضی ها خوش شانسن یا مهره مار دارند و همه جا سریع کلی آشنا و رفیق پیدا میکنن؟
در ادامه دو ویس بالا
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/mohsentavoosiseo/743" target="_blank">📅 18:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-742">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/mohsentavoosiseo/742" target="_blank">📅 17:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-741">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">چرا اگهی میذارن استخدام نمیکنن؟
😏
چرا حقوقو زده انقدر کم با این همه وظیفه؟
😒
چرا همه تخصص ها رو باهم میخواد؟
😒
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.02K · <a href="https://t.me/mohsentavoosiseo/741" target="_blank">📅 17:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-740">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">هیچ اشکالی نداره مدام request index بدی تو سرچ کنسول. گوگلم مشکلی نداره.
ولی حرف من اینه که الکی داری خودتو خسته می کنی. دست و پا زدن الکیه و نهایتا نتیجه زحمتت ریست میشه.
مشکل جای دیگست:
https://t.me/mohsentavoosiseo/737
https://t.me/mohsentavoosiseo/739
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/mohsentavoosiseo/740" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-739">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 1.93K · <a href="https://t.me/mohsentavoosiseo/739" target="_blank">📅 17:09 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-738">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سایت های ابزار تحقیق کلمات کلیدی خارجی مثل mangools و keywordtool و ایرانی ها، از کجا دارن search volume (تعداد جستجوی کلمات) در ماه رو میدن؟
چرا دیتاشون باهم گاها خیلی فرق داره؟ چرا نمیشه به فرمول رسید؟
پی نوشت:
میگم نمی تونی بفهمی منظورم عدد دقیق و حتی حدودی هست. وگرنه ابزار ها میدن همشون. سادست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/mohsentavoosiseo/738" target="_blank">📅 17:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-737">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چرا التماس کردن برای ایندکس شدن درست نیست؟
سایت من لیاقت ایندکس شدن داره؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/mohsentavoosiseo/737" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-736">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سوال یکی از شرکت کنندگان دوره از پشتیبان:  من نیاز به بررسی کلمه کلیدی باتری یو پی اس از سمت‌ پشتبان رو دارم. در واقع میخوام بدونم ویدئوهایی که دیدم درست ازشون یاد گرفتم یا نه  سرچ ولیوم این کلمه رو ۲۱۰ پیدا کردم و kd رو ۱۲٪ همچین lps برابر ۲۸ میباشد دقت کلمه…</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/mohsentavoosiseo/736" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-735">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سوال یکی از شرکت کنندگان دوره از پشتیبان:
من نیاز به بررسی کلمه کلیدی باتری یو پی اس از سمت‌ پشتبان رو دارم. در واقع میخوام بدونم ویدئوهایی که دیدم درست ازشون یاد گرفتم یا نه
سرچ ولیوم این کلمه رو ۲۱۰ پیدا کردم و kd رو ۱۲٪ همچین lps برابر ۲۸ میباشد دقت کلمه کلیدی که بین عدد یک تا سه در گوگل خودمان باید شماره گذاری میکردیم من سه رو دادم. تحلیلم این است که در این کلمه بیشتر باید هزینه off page کرد اگر یک محتوای بی عیب و نقص و تمامی موارد تکنیکال رعایت شده باشد در بهترین حالت رتبه ۸ به بعد رو بگیریم .
ممنون میشم راهنمایی کنید که این داده ها و تحلیل تا چه حدودی درست هست
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/mohsentavoosiseo/735" target="_blank">📅 16:43 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-733">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/mohsentavoosiseo/733" target="_blank">📅 13:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-732">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یک دوستی دارم که همیشه فکر میکنه من یه تکنیکی بلدم که انجام میدم سایت ها رشد میکنن. هربار فکر میکنه دارم میپیچونمش و نمیخوام بهش یاد بدم!  همیشم این رو مثال میزنه. این برای سایتی هست که من فقط یک ساعت مشاوره و راهکار دادم. اوایل فوریه. حدودا یک ماه قبل از…</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/mohsentavoosiseo/732" target="_blank">📅 13:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-731">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sgWfCFwTqQZp7jHwE8hRUiElcWY1jlZytpdrtm8w6_-9jxfpykuwRzzaMT8qkn9boscleEYh9tznbjaqXalsspIEyFj84RV2O0ytvzk6qtq6xFmxaMrSTjaSb8yYmPTrvmGGbUq_wrFUikaB-aakdZixMW3tnG9lg1nMFiCSnZpELYesTawUop9F4o85D0HSCMejyfN_TzGAofi_b9C_EglJjgTJgjsfkAC0ZB4p4_a9Hu-VCizDBO8luWdJ07mSbK6nulmW_7cnQWHJ5bCfxQ7SPdEzQqPix9gz7uuyWYm346z-eJyMvauoU4jsKH43Mf1hlSR3Pxo73DHFziYYlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک دوستی دارم که همیشه فکر میکنه من یه تکنیکی بلدم که انجام میدم سایت ها رشد میکنن. هربار فکر میکنه دارم میپیچونمش و نمیخوام بهش یاد بدم!
همیشم این رو مثال میزنه. این برای سایتی هست که من فقط یک ساعت مشاوره و راهکار دادم. اوایل فوریه. حدودا یک ماه قبل از جنگ دوم(اسفند).
بازار آمریکاست و زبان انگلیسی. و فعلا هم خدماتش در یک ایالت هست فقط.
محتوای صفحات تولید شده هم اتوماتیک به کمک AI و ابزار ها هستند.
من فقط گفتم طبق این اصول باید این تعداد صفحه بسازی. لندینگ نداشت! کیورد ریسرچ نداشت! یه صفحه نخست بود و پنج تا صفحه دلخواه به سلیقه مدیریت!
همین! من تکنیک نزدم! تو سئو کار مفت نداریم. برای همین رشد اتوماتیک هم کلی زحمت نیروی انسانی و تحلیل وبررسی مداوم کشیده شده.
صفحه بساز! (بعد از کیورد ریسرچ)
همین! صفحه با AI و اتوماتیک ولی آبرومند و خوب بسازی، بهتر از اینکه نسازی!
این سایت هم رشد کرد تا جایی که رقابت اجازه میداد. یه سقفی داره. بعد باید دست به دامن Off-Page بشی.
هم تو دوره مفصل یاد دادم. هم رایگان اینجا دو ساعت و نیم. ضبط 2018 هست. الان در نیمه دوم 2026 هم همینه:
mohsentavoosi.com/200
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.25K · <a href="https://t.me/mohsentavoosiseo/731" target="_blank">📅 13:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-729">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لینک رویداد چند روزه رایگان و آنلاین گوگل درباره AI Agent اینه. این رو گفتم میبینم برای محکم کاری، بعد ضبط رو شروع میکنم:
https://www.kaggle.com/competitions/5-day-ai-agents-intensive-vibecoding-course-with-google?registerForCourse=true
ولی معمولا پرت زیاد داره طبق معمول. یک ربع مفید یا یک دید و ابزار بهتر ازش دربیارم کافیه برام.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/mohsentavoosiseo/729" target="_blank">📅 12:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-728">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یک آپدیت بزرگ بین المللی بزرگ هم در راهه. کلا صفر تا صد سئو ولی با AI و چند زبانه و به هر زبانی (حتی نه فقط انگلیسی). این به روز رسانی، یک Game Changer هست.
هرکس دوره رو کامل دسترسی داره، (اقساط کامل)،  به رایگان دریافت می کنه.
بعد از اینکه رویداد چند روزه گوگل درباره اتومیشن و خودکارسازی رو دیدم، ضبط رو شروع می کنم. این رویداد هم برای محکم کاری میبینم. چون خودکار سازی دیگه اصلش با کلاد هست. خیلی قرار نیست شما درگیر شید.
پیام پین شده برای تهیه دوره هست.
اسپات پلیر از خارج هم در دسترس شد و راه حل با وپی انش هم با هزینه جدا هست. ولی امروز در دسترس شد از خارج از ایران.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/mohsentavoosiseo/728" target="_blank">📅 12:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-727">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پشتیبانی دوره قوی تر از قبل شروع به کار مجدد کرد بعد از یک وقفه دوماهه به خاطر جنگ.
پشتیبانی دارای حریم خصوصی در چت تلگرام هست. وبینار نیست. روزهای خاص نیست. آزادانه هست (برای من آزادی خیلی مهمه). زنده هست.
و توسط اشخاص قوی و قدیمی از بچه های خود دوره انجام میشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/mohsentavoosiseo/727" target="_blank">📅 12:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-726">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دوستان گرامی، کانال بالا، کانال محمد قاسمی هست که ایشون دوسال با من همکاری داشتند و بسیار شخصیت باسوادی هستند.
اما مسئولیتی هم بابت معرفی و توصیه کردنم نمیپذیرم. استفاده از مطالب هرشخصی که اطلاعاتی داره، کلا مفید هست.
من منتورینگ برگزار نمی کنم. ولی ایشون انجام میده.
با تأکید بدون قبول مسئولیتی از سمت من (بابت معرفی کردن)، می تونید با ایشون منتورینگ سئو داشته باشید.</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/mohsentavoosiseo/726" target="_blank">📅 11:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-725">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسئو با محمد قاسمی</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Megop_serp_analytics_2.0.4.zip</div>
  <div class="tg-doc-extra">33.9 KB</div>
</div>
<a href="https://t.me/mohsentavoosiseo/725" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">این اکستنشن فقط یک ابزار نیست، یک مزیت رقابتی سخت و مهار نشده  است واقعیت این است که آینده سئو متعلق به کسانی نیست که فقط بیشتر کار می‌کنند. متعلق به کسانی است که هوشمندتر، سریع‌تر و دقیق‌تر تصمیم می‌گیرند. و در قلب این تصمیم‌ها، Keyword Research قرار دارد.…</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/mohsentavoosiseo/725" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-724">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسئو با محمد قاسمی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd6ab0dbf.mp4?token=aiUmqH7UfX5-MFk6SbaEQgtDntGf-hIY1TsepKlSPvKtVrtLxmF-JsN6QAyoY4E1fK8e59D2wk6GoiuhvhlpR5DnuQc6XV_yPlGLUWUEzDAlSbwcEqhsvZOJjoreCBqly9FZIeR-9DvWvCKqYHGF6larTTUKwB-Y0VQdnrkUsNJsfZ_8b2m-j7pbs3GleYLWWRemILfq6LqmKEP-HBzZ9fch6F9pDVc_oTqEo0Ye9QZgmj9n-tgUR4VmWRm_CFggDciFyrqp2Jmt4ZK7-jKx640fQksdGDb4a4GATqMHzmxs6vj8MvQ-M5guhdnxW_MDBMy3GDpMwRAPOnGtWZltFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd6ab0dbf.mp4?token=aiUmqH7UfX5-MFk6SbaEQgtDntGf-hIY1TsepKlSPvKtVrtLxmF-JsN6QAyoY4E1fK8e59D2wk6GoiuhvhlpR5DnuQc6XV_yPlGLUWUEzDAlSbwcEqhsvZOJjoreCBqly9FZIeR-9DvWvCKqYHGF6larTTUKwB-Y0VQdnrkUsNJsfZ_8b2m-j7pbs3GleYLWWRemILfq6LqmKEP-HBzZ9fch6F9pDVc_oTqEo0Ye9QZgmj9n-tgUR4VmWRm_CFggDciFyrqp2Jmt4ZK7-jKx640fQksdGDb4a4GATqMHzmxs6vj8MvQ-M5guhdnxW_MDBMy3GDpMwRAPOnGtWZltFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این اکستنشن فقط یک ابزار نیست، یک مزیت رقابتی سخت و مهار نشده  است
واقعیت این است که آینده سئو متعلق به کسانی نیست که فقط بیشتر کار می‌کنند.
متعلق به کسانی است که هوشمندتر، سریع‌تر و دقیق‌تر تصمیم می‌گیرند.
و در قلب این تصمیم‌ها، Keyword Research قرار دارد.
اگر این مرحله را با یک ابزار ضعیف، workflow پراکنده و تحلیل سطحی جلو ببری،
هزینه‌اش را در همه‌چیز می‌دهی:
در رتبه‌گیری
در تولید محتوا
در زمان
در انرژی تیم
و در فرصت‌هایی که رقبا قبل از تو می‌بلعند
اما اگر اکستنشی داشته باشی که:
فرصت‌ها را سریع‌تر آشکار کند
intent را واضح‌تر نشان دهد
من همیشه گفتم و همواره خواهم گفت:
intent کاربر استراتاژی است و keyword Research فرمانده است
چیزی که شکاف‌های محتوایی را زودتر نمایان کند
تحلیل رقبا را ساده‌تر کند
و تصمیم‌گیری سئو را از حدس به داده تبدیل کند
آن وقت دیگر با یک «ابزار کمکی» طرف نیستی.
تو یک سیستم شتاب‌دهنده برای رشد ارگانیک در اختیار داری.
این همان چیزی است که سئوکارهای جدی را از سئوکارهای شلوغ اما کم‌اثر جدا می‌کند.
🖋
شاید پرسیدی که چرا اینهه سئوکاری که میشناسی هیچ کدام هیچ نتیجه ای ندارند
آیا واقعاً مساله بلد نبودن کیوورد ریسرچ است ؟
یا مساله در ساخت بینش است ؟
✨
همین حالا این اکستنشن را وارد بازی خودت کن
#کروم_اکستنشن_سئو
#کروم_اکستنشن_Seo
#chrome_extension</div>
<div class="tg-footer">👁️ 1.62K · <a href="https://t.me/mohsentavoosiseo/724" target="_blank">📅 11:38 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-723">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سوگیری شدید و نگاه صفر و صدی در جامعه ما
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/mohsentavoosiseo/723" target="_blank">📅 17:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-722">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برای پروژ های فارسی، ابزار های ایرانی کیورد ریسرچ کافیه.
زمانی که من اکثر سال ایران بودم هم من اشتراکی نمیخریدم. حوصله دردسرشو و قطعی مدامشو نداشتم. همه سه سایتی که اشتراکی میدن همینن.
برای پروژه های خارجی هم یا با پول کارفرما یا چند ماه یبار یه ابزار میخریدم. معمولا منگولز.
اما درک می کنم که یک پنجاهم قیمت اصلی وقتی پول میدی، باید هزار تا اکستنشن کروم تنظیم کنی که اون اشتراکی استفاده کردن ها توسط اون ابزارها لو نره. با دستکاری سشن و کوکی و وی پی ان و خیلی جزئیات و مکافات دیگه. که از نگاه بین المللی، عملا کار غیر قانونی هست. هم فروشش. هم خریدش.
نمیشه هم پول خیلی کم داد هم دردسر نکشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/mohsentavoosiseo/722" target="_blank">📅 16:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-721">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اون 20 نفری که تا این لحظه جواب این رو بله زدند، خیلی دوست دارم بدونم چرا منگولز نه؟
من خودم منگولز پریمیوم 40 دلاری اختصاصی میخرم همیشه. یه سئو هست و یه کیورد ریسرچ. کیورد ریسرچ شوخی نداره. مهمه. مهمترین بخش سئوست.
منگولز خیلی بهتره در کل. ارزون تر با محدودیت کمتر با کارایی بیشتر. البته برای کیورد ریسرچ فارسی، ابزار های بومی ایرانی کافی هستند و نیازی به ابزار خارجی نیست.
برای تحقیق کلمات کلیدی کلمات فارسی، ابزار اختصاصی و حتی اشتراکی خارجی نخرید!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/mohsentavoosiseo/721" target="_blank">📅 14:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-720">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🟢
⭕️
نتیجه گیری:
با توجه به اینکه:
⭕️
تعداد فعلی رای ها که همین الان که دارم مینویسم 200 تا "بله" شده،
❗️
این هایی که بله زدند نمیخرن. نرخ تبدیل پایین تر (خوشبینانه یک سوم) خواهد بود،
❗️
هرکس رای داده اگه اولی (همه ابزار ها) رو بله زده، دیگه نمیاد اون یکی ها رو بخره و عملا تعداد کل "بله" ها رو نباید جمع زد،
❗️
در آینده رای گیری بیشتر میشه. اینستا هم استوری بذارم. 10 برابر در نظر میگیریم.
طبق براورد من
❗️
خوشبینانه 400 نفر ماهانه میخرن. بدبینانه 100 نفر. بعد از 6 ماه.
❗️
سود خوشبینانه: 800 تا 1600 دلار. بین 200 تا 300 میلیون تومن.
❗️
سود بدبینانه: 50 دلار. معادل حقوق وزارت کار. بین 15 تا 30 میلیون تومن. عملا با انرژی که ازت میگیره، ضرر مطلقه. گل فروشی سر چهارراه به صرفه تره.
❗️
امکان توسته پذیری با تبلیغات و پشتیبانی قوی و زحمت زیاد در دراز مدت تا 2500 دلار. و با اوج ناامنی با توجه به تغییرات تحریم، دلار و خود ابزار ها و قدرت خرید کاربران.
نتیجه گیری:
با توجه به دردسرهای زیادش، جای مانور پایینش، پشتیبانی سختش، توسعه پذیری بسیار محدودش،
ورود نخواهم کرد
😅
به فروش ابزار های اشتراکی سئو.
بلند فکر کردم شما هم استفاده کنید. هم استفاده کنید هم انتظارتونو از ابزار اشتراکی 1 تومنی که همه چیو با هم میده بیارید پایین و با واقعیت های میدانی آشنا بشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/mohsentavoosiseo/720" target="_blank">📅 14:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-719">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-poll">
<h4>📊 حاضرید برای Ahrefs ماهانه 1 میلیون و 300 هزار تومن (1300) پرداخت کنید؟ با ماهی 50 تا اعتبار. یعنی 50 تا درخواست(request).</h4>
<ul>
<li>✓ آره حاضرم</li>
<li>✓ نه! No! Hayir! Nein! いいえ! 아니요!, لا! Non!Yox!нет!</li>
</ul>
</div>
<div class="tg-footer">👁️ 1.98K · <a href="https://t.me/mohsentavoosiseo/719" target="_blank">📅 13:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-718">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-poll">
<h4>📊 حاضرید ماهانه برای سیمیلار وب Similarweb ماهانه 800 هزار تومن پرداخت کنید؟</h4>
<ul>
<li>✓ بله</li>
<li>✓ نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.4K · <a href="https://t.me/mohsentavoosiseo/718" target="_blank">📅 13:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-717">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-poll">
<h4>📊 حاضرید ماهانه 1 میلیون و 400 هزار تومن(1400) هزینه کنید برای سمراش؟ Semrush</h4>
<ul>
<li>✓ بله</li>
<li>✓ نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/mohsentavoosiseo/717" target="_blank">📅 13:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-716">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-poll">
<h4>📊 حاضرید برای ابزار Keyword Tool ماهی یک و نیم میلیون تومن(1.5) هزینه کنید با روزی 5 درخواست؟</h4>
<ul>
<li>✓ بله حاضرم</li>
<li>✓ نه اصلا!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/mohsentavoosiseo/716" target="_blank">📅 13:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-713">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-poll">
<h4>📊 حاضرید هر ماه فقط برای ابزار Mangools (کیورد ریسرچ)، 500 هزار تومن هزینه کنید؟ با روزی 25 تا درخواست.</h4>
<ul>
<li>✓ بله حاضرم.</li>
<li>✓ تا ابد نه!</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/mohsentavoosiseo/713" target="_blank">📅 13:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-712">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-poll">
<h4>📊 حاضرید هر ماه انقدر هزینه کنید؟ماهی 3 میلیون و 700 هزار تومن برای همشون. ولی ابزار ارزون تر کیورد ریسرچ رو فقط میذارم:   Ahrefs,SimilarWeb,Mangools KWfinder,Semrush</h4>
<ul>
<li>✓ بله حاضرم. میصرفه برام.</li>
<li>✓ خیر. به هیچ وجه.</li>
</ul>
</div>
<div class="tg-text">قیمت تمام شده (سر به سر به ازای هر خرید) برای هر کدوم از محصولات زیر با فرض اشتراک بین 20 نفر. برای یک ماه.  نرخ محاسبه ریال = 180 هزار تومن با احتساب کارمزد تبدیل و سایر موارد خرد انتقال پول. رنده شده به بالا به ازای هر پنجاه هزار تومن.      Ahrefs= 6.5$…</div>
<div class="tg-footer">👁️ 2K · <a href="https://t.me/mohsentavoosiseo/712" target="_blank">📅 13:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-711">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قیمت تمام شده (سر به سر به ازای هر خرید) برای هر کدوم از محصولات زیر با فرض اشتراک بین 20 نفر. برای یک ماه.
نرخ محاسبه ریال = 180 هزار تومن با احتساب کارمزد تبدیل و سایر موارد خرد انتقال پول.
رنده شده به بالا به ازای هر پنجاه هزار تومن.
Ahrefs= 6.5$ = 1200
نفری 50 تا اعتبار در کل ماه. 50 تا request
1 میلیون و 170 هزار تومن.
KeywordTool.io
= 7.5$ = 1350
نفری 5 درخواست در روز.
1 میلیون و 350 هزار تومن
Mangools = 2.1$ = 370
نفری 25 کوئری بخش کیورد ریسرچ. در روز.
370 هزار تومن
Semrush = 7$ = 1260
سمراش جوری نیست که به درد اشتراکی دادن بخوره. چون باید سایت ثابت بدی. عملا استفاده 20 نفر مقدور نیست. فقط بخش هاییش قابل استفاده است.
دلیل خرید Moz هم درک نمیکنم اصلا اگر کسی میخره!
Similarweb رو میشه به بیش از 20 نفر داد
چون حالت کردیت و محدودیت تعداد درخواست و روزانه نداره. این رو میگیریم 50 نفر.
Similarweb = 4$ = 720
720 هزار تومن.
این فقط قیمت تمام شده خود ارائه دهنده ابزار اشتراکی با این تعداد کاربران نوشته شده هست به ازای هر اکانت. سالانه بخره حدود 25 درصد کمتر میشه. ولی سالانه ریسکش بالاست برای فروشنده.
حالا هزینه جاری و توسعه ابزار و نگهداری سیستم و پشتیبانی هم حساب کن. من میگم بدترین حالت معادل نیم دلار و بیشترین حالت معادل 2 دلار به ازای هر کاربر. به صورت کلی باید روی قیمت ها بیاد. تا اینجا که هزینه خود فروشنده بود.
در حالت فروش دسته جمعی همشون با هم، باز 2  دلار روش میاریم در بیشترین حالت.
هزینه جاری در کمترین حالت ممکن: 50 میلیون تومن. ولی بهتره 100 در نظر بگیریم. حداقل 500 دلار. در ماه.
میزان درگیری ذهنی و دردسر فروشنده: بسیار بالا.
سود فروشنده در صورت داشتن ماهی 1000 تا کاربر ثابت(که عدد بالایی هست):
در کمترین حالت به صرفه:
90 میلیون تومن - 500 دلار
منهای هزینه جاری: در حد حقوق وزارت کار
در بیشترین حالت به صرفه(که کاربر کم میشه چون نمیتونن پرداخت کنند):
360 میلیون تومن. 2000 دلار.
منهای هزینه جاری: بین 100 تا 200 میلیون تومن.
مشتری واقعی پایدار بر اساس واقعیت فعلی هم، 1000 نیست. هزار باشه باز هم عدد وسوسه کننده ای نیست.
نظر سنجی زیر رو میذارم که عدد در بیاد.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/mohsentavoosiseo/711" target="_blank">📅 13:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-710">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">با توجه به افزایش تقاضای ابزار های اشتراکی، من قصد داشتم خودم به این حوزه ورود کنم.
ایراد هایی که به سه سایت ایرانی ارائه ابزار اشتراکی خارجی داشتند این ها بود:
- پشتیبانی ضعیف
- قطع شدن مداوم ابزار ها و هدررفتن زمان اشتراک
- نداشتن محصول مورد نظر
- طراحی و تجربه کاربری ضعیف.
حالا برای اینکه من بفهمم صرف مالی داره ورود کنم یا نه و شما هم بفهمید(!)، نظر سنجی می کنم از شما.</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/mohsentavoosiseo/710" target="_blank">📅 13:08 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-709">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na22Rq3Om_UoEt_ud3-Om3hCnoxj5syn1fyAx1LWLQlqo7z2AU5q9vg_TErFqh2CW4pVxqMhtYpZke8luP-E_EGrQmAVOBxzMe_I-kBh6CM9t1dnm_w8MHFrf5v7jqY1oKp7AOQqvgN9_RwT_tOKQ4eA5SJ9a8d64AGRSrC5an8F4chZNHQUn9mOewrS5Hmn-uuaTVWzE3A2--9t3SIxtykPHS37iazDoo1TcW0RUyOr5t0qMm_dUwxmMag1FeT7jgTX0xelMzlpRPyF9IoKZMTJT5mBUFhJB8_Had2cSMCYsPHXKWUVQHmNLZ_WrviFwyIkRF9jjs8-7E5sVP8U2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر با AI زیاد سر و کله زده باشید ارزش جواب کلاد رو میفهمید. هرچند که نسبت به بقیه معجزاتش چیزی نیست.
وضعیت:
گفته باید رو سرور نصب کنی. ولی به جای "سرور" گفته رو سیستم. منم اونو بهش گفتم.
حالا AI های دیگه بود چی میگفت:
اره حق با توست. باید روی سرور نصب کنی.
جواب کلاد:
منظورم از سیستم، همون سرور بود.
تفاوت رو متوجه میشید دیگه؟ خیلی تفاوت داره ها! خیلی!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.98K · <a href="https://t.me/mohsentavoosiseo/709" target="_blank">📅 18:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-708">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3494a006a0.mp4?token=pdmE2z_JcUfmH8G-pe9jP4haDycQMNY56JfHF2HBKQCxyLNiKkNsoTR3L85DKultblKjgsMhZR5Kmdxwx7z5eu_s1FDaNTX7KeS0Ukh_3rtIpcCONULe5I6HXUCmHZGFaCHpLIiZaXr9cFWtHXSk_jdLTIWQ-LS_aZ0lDO1pv3GEpl5VCyvtfoJTAsdE0i7L3ZSYtkdtS8n59Rsn4oUz5fUOfdpODMLfSrSkdOIE2wymhXoX3y9wj5BLZTeSfU4-fyiCC2sKnb2_SlxKIXiLn6dwpMS4NjjzyQ0yHwkj5JoAaJ9SY3eS7DS7sTzNT8cWX0v-fn9IJLbqQTeRTI7m7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3494a006a0.mp4?token=pdmE2z_JcUfmH8G-pe9jP4haDycQMNY56JfHF2HBKQCxyLNiKkNsoTR3L85DKultblKjgsMhZR5Kmdxwx7z5eu_s1FDaNTX7KeS0Ukh_3rtIpcCONULe5I6HXUCmHZGFaCHpLIiZaXr9cFWtHXSk_jdLTIWQ-LS_aZ0lDO1pv3GEpl5VCyvtfoJTAsdE0i7L3ZSYtkdtS8n59Rsn4oUz5fUOfdpODMLfSrSkdOIE2wymhXoX3y9wj5BLZTeSfU4-fyiCC2sKnb2_SlxKIXiLn6dwpMS4NjjzyQ0yHwkj5JoAaJ9SY3eS7DS7sTzNT8cWX0v-fn9IJLbqQTeRTI7m7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/mohsentavoosiseo/708" target="_blank">📅 17:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-707">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPMi8w_v0pOY1wVm_ZgoTz6q-NwKXbtfWoo_mocWYsnAK-bF4TBp5B_lAqsTnW-xM1EsMx0kNpa-rHVVX7sgII0Mo3u9ZSgYjcY6cmsJoDX2FdTpgiRit9l5VXzEXR5PPJM_xHykdGDYWVj6ALieMNFTGwLmJt9laGuNO1-oxSH4XW_1uVV3oy7Xp2XPR978NPaEUAXNBxgKSUinI4VZMjoJ0q9qc2QcG5Jy7-LWvcYn7sscR5zeMDnc7xU7-NkrOfxhRptnCVoZptzEFyxsFNgsjxBzJatO-QvYeSSvD-XdwTD-ss_LxWqH70H-bPBAh6RmNol5ykFC6uUWvzpUYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کم فارسی انگلیسیش چپ و راست هست. ولی همین کافیه تا عاشق کلاد بشید!
اه! انگار قبلا اپدیت شده بود. بذار!
😅
😍
😍
😎
فقط هم ادا نیست. واقعا بازدهی و خروجیش عالیه‌.
هنوز خیلی ها از skill در کلاد استفاده نمیکنن.
در اپدیت دوره، علاوه بر سئو بین المللی(که الان هم یک فصل داریم)، این ها هم آموزش میدم و هرکس دوره رو داره، رایگان آپدیت رو دریافت میکنه. فعلا زمانش رو نمیتونم بگم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/mohsentavoosiseo/707" target="_blank">📅 16:43 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-706">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a993e8989.mp4?token=hPG5uP9x65fJNGMiC_o0O5tMQjwslJlHxjbfvZSBFG28xrGXsqtoeDNrh8gLYIWH-abayAlt6Voapp4lrVZxsVHdUNaVo1e-bg6lPLRXES15xV900ZdfFb6-mkiue59_boKuvqNqaBMxphfREmvAlj6xlRqdLxWRCljjsz88M-gzHXg6_qgIKBTFnpRM0Gfj7iCfVq53XIw53WBZxayXyD84_vFvVcIZV0YfYATxwEla0SECc1DqESj0NpBomBF1dVVgKo5_3uuYrfVk5XXyi-_lFSESghah5ZFrZMVvQFS_Rpk8ZxehDR_hM4dMUMDvn5q4-97hgVMyaBbaNGg1rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a993e8989.mp4?token=hPG5uP9x65fJNGMiC_o0O5tMQjwslJlHxjbfvZSBFG28xrGXsqtoeDNrh8gLYIWH-abayAlt6Voapp4lrVZxsVHdUNaVo1e-bg6lPLRXES15xV900ZdfFb6-mkiue59_boKuvqNqaBMxphfREmvAlj6xlRqdLxWRCljjsz88M-gzHXg6_qgIKBTFnpRM0Gfj7iCfVq53XIw53WBZxayXyD84_vFvVcIZV0YfYATxwEla0SECc1DqESj0NpBomBF1dVVgKo5_3uuYrfVk5XXyi-_lFSESghah5ZFrZMVvQFS_Rpk8ZxehDR_hM4dMUMDvn5q4-97hgVMyaBbaNGg1rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که بحث مقایسه مترو ها شد جا داره بگم، مدیونی اگه به ایران بگی جهان سوم.</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/mohsentavoosiseo/706" target="_blank">📅 11:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-705">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فقط هم کیلومتری مقایسه کنیم باید مساحت کل اون شهر هم در نظر بگیریم. استانبول ۷ برابر تهرانه. مساحت توکیو ۲ هزار کیلومتر. مساحت تهران ۷۵۰ کیلومتر.
با همین فرمون سرچ کنسول گوگلو تحلیل کنی تا ابد غلط در میاد تحلیل.
مثل نگاه کردن به avg position کلی برای تشخیص رشد سایت!
تازه طرف فکر میکنه چون حرفه ای به کلیک کار نداره پوزیشنو نگاه میکنه! اینجاست که کسی که فکر میکنه حرفه ای تره آمارش غلط تر میشه!</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/mohsentavoosiseo/705" target="_blank">📅 11:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-704">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHzA8QZ-isumFx01OY0dL3P8y6JUyWI5efKSZ44ucd3s0FkU0eRGQ1iLL_PJWEJUeIt37_YtnG0JouOqiC4SU6Xr1a44rvHRzhomz9zIx9gScda0z9X8uXgcga--nO4HJSX1tSxrHkBuRHsI9BttIbQXx8DW3gTvUjdXE-aY2qI2fozX0A6K3UIjxEdWm0AzOGFCx0jbKWYKUrbghwvYhYjuPxMJMLSyenujPEHQKUNHdmufiFHwei_0fIWWgB_Gyi8lPwJ20LbtEAKV0JVLbwShVkAADvirAXx7jqRX8b8qGLCfjdb2y5FEHYf0N29cpkXcxHwmNse4FD_fwf4XHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استانبول</div>
<div class="tg-footer">👁️ 3.48K · <a href="https://t.me/mohsentavoosiseo/704" target="_blank">📅 11:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-702">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B21HHyq4e6KzLnoeNO6wqCXnpdIsmAW9xYXJTz5fvVMQ0UiZA8ResAirb8eF4AT_8vlJ2T4wfKEQRlv1NPsmbb8DU2uAXOgrZWmxxFO1P5-sQbD_KfPqi4wA3ZzJiBP7qxujrAmGJm-PUvRcWYZTiNVjXd0x1BTLqLmBQ7HZ9jlWWQfv95FAcE659WI-JgJxLbUFUSVdPkVXNNP2gJxzXgPOlWHBNs3fEOvb_q6VqaZ7bMa8xCfKt_1aqx7AECPD6nzrpFnWPQtC9rnsgQEyAvZjjrUXZf6cDMtowVZ-8L6GpA1jQwyWnO2a7I73E3zWbwnhjdFtdjQeUWXSeFjXxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سئول کره جنوبی</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/mohsentavoosiseo/702" target="_blank">📅 11:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-701">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfJhTKGmaVIlVznirKSHweP8pJJ8j4NK2dTYAUD_DhMWWCTGa1VuLHkJcDsAWQBqZdLR77d4ZkTN5q8Ps4HiOQd9wMK0nEWi7_ySgP_vZNy4gQpr6ylQr_xrIfjRB69n4sCzs8sT9IM1KDdjXXGl5101iNyYYFu_33QjGF0zt3r_yAkF1DD6WQEq0NoNpW_Au1RYUBMjMAogc3VaRCgFBZrYDSoVRuMTihRyzPbFDvllhCrs295TycXLPOZ-n5b5kUE_wL_920L_IlfEVqQpovP6_3YhZqXphtQB047erh4sgOAtfS2qVCVwqaxHBGmE-ErA26Io6VM_Pk775vs_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسکو</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/mohsentavoosiseo/701" target="_blank">📅 11:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-700">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AGFuUeS18lsBbV1OlN6TsPYWOZa--rgTbvf64Be7FUHSM-CD3KB1Oot99CtHN6CezrdzLgl2b31RY1w16xTTl8VxlYkI_s7K03KO-wj866h34RIKeniD2KfWSu-O-GjrFWddV8brv20LZ8fq_9fDysEn25Bx5NUEfgZYMnW8t0IG5eLnvOTG6GbD0xfEI3E1lJalnCrgQasIoqZijvwyR5iBILeKhtbBkLmopJVp3e3NFLlgYgylfseQ4e0i7oOJRCYxuxiWRyonmgHl2xfqCtGZOLpMbFEQG2fksw3f2kQnt-ZImTo-QPIdgQormQG5aknbyhMZjlyxRKvrQtaFnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/mohsentavoosiseo/700" target="_blank">📅 11:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-699">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/mohsentavoosiseo/699" target="_blank">📅 11:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-698">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoW4Gno20FSsehcD_ulPkb1RkvrksNXIkJYydI-DGF_yv-spueZ8dCCDLnZ1gAgsnTInHLnluO9hNzzi9ljqUmhGZ3613YmMae0q6FtnkJkeEFsALZ_GNlARyfVM87rHIwkf6DYF8oUQ7uaBaasMLWdbYXqIOxmf06ROg6_3AVhl-X7wDyNkBfedNGqDsQXNCIT5-pi_BtzvewEICC9Lg4t3KoaqracQ6ANN7EiZN5-ZpiwYzMnf7kanU9cy25Z2ucL8Kp699S5YJenFLNeiNXqFESv7v1xXnjWzSXs41HNebeCsCgSKj70FTP8rhT8uMuigpcazytzj48TRo1aMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تحلیل هایی که به بیراهه میرن!</div>
<div class="tg-footer">👁️ 3.25K · <a href="https://t.me/mohsentavoosiseo/698" target="_blank">📅 11:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-695">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">احتمال جنگ همچنان بالاست. کارهایی که برای دسترسی گوگل و از خارج برای سایتتون کرده بودید رو همچنان نگه دارید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/mohsentavoosiseo/695" target="_blank">📅 20:45 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-694">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paMwQmZLGIkbAmiYkv61znac90XaPhHdyGnDHZB2Nh8g78s5BjL3QMnwkm0coYjNrdPoBnloG1YnvWA6K-kc7MqMflHTZYrKSVzlSEjne5qkicysZE2NJH0t3iy-dnmuCBkT5qWhk1XDYft3UED-S5Q68GSfORdYGUPNjMqOio4jEYmUdw1FiNgumHs2X-lQDTJzXgC3Q71aYyQ2fUB3dq3Q-MwvaqFiYrthjYp6epb1zay_1YDlYxpxk1z2agWbqcTlVKUzNA6PUAQUIvEJI3TzVrMbd2z1OOCi4-M32ZNBTlKocYHuK5hBXK2fXZnVbtzMiupsipow9zxu8XqFaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز اینترنت وصل شد یه عده بلاگر شروع کردن به سئو مُرد گفتن که AI اومده.  سرچ کنسولای ما که کلیک میگیره هم توهمه.  لندینگ میسازیم بصورت گپ(رقیبا نساختن) ورودی و فروش مستقیما بالا میره هم تو دنیای موازیه.  پول هایی که به حسابا میاد ازش هم فقط تو ماینکرفته(دنیای…</div>
<div class="tg-footer">👁️ 5.35K · <a href="https://t.me/mohsentavoosiseo/694" target="_blank">📅 20:11 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-693">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">باز اینترنت وصل شد یه عده بلاگر شروع کردن به سئو مُرد گفتن که AI اومده.
سرچ کنسولای ما که کلیک میگیره هم توهمه.
لندینگ میسازیم بصورت گپ(رقیبا نساختن) ورودی و فروش مستقیما بالا میره هم تو دنیای موازیه.
پول هایی که به حسابا میاد ازش هم فقط تو ماینکرفته(دنیای خیالی بازی) و واقعی نیست.
ما هم تو خواب، پروژه های کانادا و آمریکا و اروپا و حوزه خلیج فارس،  دستمونه. واقعی نیست.
کارفرماهای خارجی هم تو فیلم Lost مردند و تو دنیای موازی دارن کار میکنن با ما.
گوگل ادز هم جمع کرده ما خبر نداریم. بالاخره نتایج سنتی نباشن ادز هم نیست. این کمپین های ادز ما هم همینطور الکی داره لیر و درهم و دلار حروم میکنه. دیدیم پولمون زیادیه گفتیم ادز بریم.
خجالت داره واقعا. ملت دارن پول پارو میکنن اما طرف صبح تا شب رو تختش دراز کشیده در حال اسکرولینگه و دنبال اینه که چه چیزی مُرد چی نمرد.
اره SEO مُرد. حله. رقیب تو نتایج گوگل کمتر خرج مام کمتر. استقبال کنیم از این تفکر.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/mohsentavoosiseo/693" target="_blank">📅 19:32 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-692">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">موضوع پزشکی بالا که ربطش دادم به AI هم نظر شخصی بود هم صرفا یه پرانتز بود و به معنی بی ارزش کردن کل علم پزشکی نبود.
علاقه ای هم ندارم کسی رو قانع کنم دربارش. شما پنتوپرازول و اس امپرازولاتونو بخورید تا آخر عمر و به حرف دکترتون گوش بدید. مسیر من برعکسه. هرچند که ۱۱ سال هرروز مسیر شما رو رفته بودم.
پرانتز بسته. برگردیم سر هوش مصنوعی و سئو
😎
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/mohsentavoosiseo/692" target="_blank">📅 12:34 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-691">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c800f1b10.mp4?token=fikdRzAxvcuuhhkfwNGYoZhIAltN0kSVbheZ_qda_O4OGLDqX7RH3jIW_-fpwmQcaBoRah5tohY57lJbnQecwU2FkGg7VQQ7hmLlm9f-ExTJnQZ0P6pjtJ-qqXLHjE7WBg_nLjMo9zxcpeiD31JOEL52W7NXVDP-PhnwGBAZtl0xKIAjmJBXpaCi7sYYC3KU-lBigR2ejVM_-jU-qRi5Ox3pLriIIDDP35VqlE6g3aGPUzlDNEvDQuvo0qnup43PFGzGAbnm8YX0OcLCwNEuTl5v8DYJQudDJePgxIRsAedvgnk0S6V2rUuD5DETWVuYwyusJymLG8UASAE0LcM7EZ7YACgGkPpAMWf3BmnmfrZvKhODEwhTu_Y01XGkEXztU08c5bQmMr4OphHfWRpJZPC__WeACPWQ3Bt02B06nYT99obeGJ7LHicaJKEj9HBB06d6_lWqaYgoPtvDngSnUK7l6iku7mM65z1QOoRqlmGIr70tLgGxFqeuRUTK-ZLRYQR1oux_LAq1Xb_zF7FqQSe8lqWXJOUCI0sCnLGmEQmh5iOsvvv2BhBgxsEcDOTcRSksRgu9PKGJ0vJ27nigCr2aDLJbVUmWOtQNj893ay-zsS18yqwIzuRtgO75gQXjJS0VX-f90isWmJRiJJNvktIyoyS9XDPKQsh179Ld1JE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c800f1b10.mp4?token=fikdRzAxvcuuhhkfwNGYoZhIAltN0kSVbheZ_qda_O4OGLDqX7RH3jIW_-fpwmQcaBoRah5tohY57lJbnQecwU2FkGg7VQQ7hmLlm9f-ExTJnQZ0P6pjtJ-qqXLHjE7WBg_nLjMo9zxcpeiD31JOEL52W7NXVDP-PhnwGBAZtl0xKIAjmJBXpaCi7sYYC3KU-lBigR2ejVM_-jU-qRi5Ox3pLriIIDDP35VqlE6g3aGPUzlDNEvDQuvo0qnup43PFGzGAbnm8YX0OcLCwNEuTl5v8DYJQudDJePgxIRsAedvgnk0S6V2rUuD5DETWVuYwyusJymLG8UASAE0LcM7EZ7YACgGkPpAMWf3BmnmfrZvKhODEwhTu_Y01XGkEXztU08c5bQmMr4OphHfWRpJZPC__WeACPWQ3Bt02B06nYT99obeGJ7LHicaJKEj9HBB06d6_lWqaYgoPtvDngSnUK7l6iku7mM65z1QOoRqlmGIr70tLgGxFqeuRUTK-ZLRYQR1oux_LAq1Xb_zF7FqQSe8lqWXJOUCI0sCnLGmEQmh5iOsvvv2BhBgxsEcDOTcRSksRgu9PKGJ0vJ27nigCr2aDLJbVUmWOtQNj893ay-zsS18yqwIzuRtgO75gQXjJS0VX-f90isWmJRiJJNvktIyoyS9XDPKQsh179Ld1JE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در راستای پست قبلی.
مساله اصلی پست قبل، واکسن نیست.
صرفا به صحبت دکتر رابرت مالون که از محقیقن یا مخترعین تکنولوژی MRNA هست درباره بازار سهام توجه کنید.
که خیلی هم بهش گیر دادند که ببند دهنتو.
باید هم ببنده. چون زورش نمیرسه و قدرتشو نداره مقابله کنه. هرچند درست میگه.
و اونجایی که سخنران اول میگه CDC سازمان بیماری های امریکا گفته ما هرگز روی اون موضوع نمیخوایم تحقیق کنیم. (تو وقتی تحقیق میکنی از اطلاعات موجود تحقیق میکنی با AI)
وقتی نمیخوای تحقیق رو انجام بدی یعنی از نتایج اون تحقیق میترسی. و دیتای رسمی که ازش بیرون بیاد کل بازار و اقتصاد و سهام رو ممکنه نابود کنه.
پول، جهت میده به علم. پس تحقیقی که نمیخوان انجام بدن دیتاش نیست. وجود نداره. بعد تو میخوای با AI انجام بدی؟ اینجا باید بری سراغ تحقیقات غیر رسمی تر.
مثلا کبد چرب قرص درمانی تایبد شده نداره. اما تحقیقات پراکنده زیادی از اثر گیاه خارمریم روش شده(همون لیورگل)
هدفم فقط جلب توجه شما به جریان علمی غیر از جریان علمی رایج هست. و شبه علم هم نیست و کار  هم می کنه.
اگر قراره خلاف جهت شنا کنید، ChatGPT رو فراموش کنید. به درد نمیخوره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/mohsentavoosiseo/691" target="_blank">📅 12:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-690">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اخیرا جمینای من از کلماتی استفاده می کنه مثل ای بابا یا کلماتی که احساس حسرت، افسوس و هیجانی رو منتقل میکنه.  این در حالیه که هیچ وقت در چت با من این کلمات به کار برده نشده.  تفکر نقاد هوش مصنوعی ها هم بهتر شده و کمتر دیگه علاقه دارند تاییدت کنند.  با همه…</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/mohsentavoosiseo/690" target="_blank">📅 12:19 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-689">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اخیرا جمینای من از کلماتی استفاده می کنه مثل ای بابا یا کلماتی که احساس حسرت، افسوس و هیجانی رو منتقل میکنه.
این در حالیه که هیچ وقت در چت با من این کلمات به کار برده نشده.
تفکر نقاد هوش مصنوعی ها هم بهتر شده و کمتر دیگه علاقه دارند تاییدت کنند.
با همه تغییرات و بروز رسانی ها
الان نمره ۱ تا ۱۰ رو اینطور میدم:
کلاد Opus نمره 9
کلاد Sonnet نمره 6
کلاد Haiko نمره 5 ولی فقط برای خرکاری روتین و تکراری و بدون نیاز به IQ و درک زیاد.
جمینای همه LLM هاش در کل نمره 5 و 6
چت جی پی تی 5.5 نمره 2
چت جی پی تی با Thinkning نمره 2.5
انگار چت جی پی دیگه عقب موندست. نمیتونم آدم حسابش کنم دیگه. امیدوارم تو نسخه های بعد از 5.5 از این حالت آبروریزی نسبت به رقیباش در بیاد.
پی نوشت:
"خرکاری" و کار گِل (gel) معادل رسمی تر نداره. از همه AI های بالا هم پرسیدم اینارو گفتند:
کار روتین و تکراری.
کار طاقت فرسا و وقت گیر.
کار پر زحمت.
کار اجرایی روتین.
وظایف پایه تصدی گری(جمینای گفت. نزدیک ترین معادل)
امور تکراری و کم بازده (جمینای گفت. نزدیک ترین معادل)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/mohsentavoosiseo/689" target="_blank">📅 11:57 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-688">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ابزار های سئو خارجی رو به صورت اشتراکی از کجا تهیه کنیم؟ از سایت لیمیت پس! Limitpass.com ایرانی چطور؟ ابزار جت  سئو و کیورد چی و چند ابزار خوب دیگه...  http://limitpass.com/ https://www.jetseo.ir/ https://keywordchi.com/    کد تخفیف سه سایت بالا:  mohsentavoosi…</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/mohsentavoosiseo/688" target="_blank">📅 13:18 · 04 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-686">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">احتمالا متوجه شدید که من زدم تو خط نادیده گرفتن. سرمو کردم تو برف فقط دارم فنی حرف میزنم. انگار که همه چی گل و بلبله.
علتش درد زیاده و خستگی. ظرفیتم به پایان رسیده. صدام در نمیاد. من سال ۹۸ گفتم فاز ملی گرایی بر ندارید هی بگید موتورجستجوی ملی. ضررش بیشتر از سودشه. تازه کسانی میگفتند که تو حوزه سئو فعال بودند. پست های لینکدین این موضوع هم لایک میکردند. اون موقع خیلی تنها بودم. تنهایی داد میزدم...
و کلا خیلی حرص و جوش ها. ولی خستم واقعا از دست و پا زدن بیهوده. از خون دل خوردنی که فقط پیرم کرد. از دیدن شرایط و صحنه هایی که جز فرو رفتن تو زمین کاری از دستم بر نمیاد.
اما اینو میدونم نباید همدیگر رو سرزنش کنیم...
به امید روزهای خوب.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/mohsentavoosiseo/686" target="_blank">📅 16:25 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-685">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYYfaQnxLRixNSc6xV8cwZqPli8z1o8md8gsC8ffG-090toT1Brc-okE2dcM3_SEK4lt7_bn9JYBbzbgEVLgrO6uSAYFKF_Vf6V_T7l9s8w6c_4NTujLr8RtRl1OYPI-l74Qp2Je2YOjXWdLCux38P048BsXKboKvqC4U2Osu-PtQYHTYbOSc1DrrLRl7I94S2OWhLuQPCIQz8KtePBuvc2R7vn28ye54WKKMfUZrLkxgi6U4Wj2TzO2TscjI8XZ-FvWfgZODk3eY06T21_kO63RluVoPpIzu81Qk_TKTcS-iDtewc95dRve8_jbaFj90IhscGUZa5mwiweS_r8Niw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به مرحله ای رسیدیم که هوش مصنوعی، خودجوش، خودش از دیتای خودش ایراد میگیره. خیلی خوبه. تبریک میگم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/mohsentavoosiseo/685" target="_blank">📅 21:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-684">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tPzPRKMgJTkxs_MAItbBsxvAddm5cRqeG3Dy-J0mA_J65DhRGyJFAb6AcMSkNEa4FW4-E0vAZcPnvRRqeeC3f-n_MZ5cKG61aN5Odn3fhB-4EfGLb1fDSvlvtKVEDgY2PGcjFbo0fkl0fr6H5N1zr0qzLSIZZHNDC8Ttn7Wd8ZWIbYIBwNt2--20oxct6QwMtnghx618aIhIecn8Em5CJBxS5kgqMqVk98rljGrhyGYm45iVI37EubZT78jbD75G7acqhygnGuKcNmUu1F_lsiWTSHWGmSCbapPhjTCUDY7vY138JMCuuolu4Sjw1SdXHlwR3wHTaa_56TbiMbugmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من یه معتادم! معتاد کلاد!
خودش پیشنهاد داد یکی از قانون هامو که بهش داده بودم تغییر بدم و پیشنهاد خوبی هم داد.
اصلا انگار بشره. توقعمو خیلی برده بالا. خیلی هم ریز بین و دقیقه. خیلی هم عمیق میفهمه.
آنتروپیک پس فردا مثل Horizon Zero Down و Forbidden West، ربات هاش زندگی انسان رو می گیرند و باید پناه ببریم به پناهگاه ها و ربات های Anthropic بشن موجودات اصلی زمین.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/mohsentavoosiseo/684" target="_blank">📅 17:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-683">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/mohsentavoosiseo/683" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-682">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">آموزش سئو محسن طاوسی
pinned «
🔆
به خاطر شرایط جنگی، قیمت دوره از 12 میلیون تومن، به 4 میلیون تومن، کاهش پیدا کرد و این قیمت تا زمان ظهور دوباره امید به بهبود در دل مردم این سرزمین، این قیمت باقی می مونه.
❗️
هیچ وقت هیچ کمپین تخفیف و فروشی نداشتم. این هم کمپین نیست! کاهش دائمی هست تا برگشت…
»</div>
<div class="tg-footer"><a href="https://t.me/mohsentavoosiseo/682" target="_blank">📅 15:04 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-680">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تمام صحبت های من درباره هاست و سرور و دسترسی و Origin Rule و GEO DNS، پست های زیر هست. درباره sync بودن سرور داخل و خارج هم در لحظه نظری ندارم.
هاست های ایرانی که اخیرا میگن دسترسی گوگل بهشون باز هست(ولی از خارج یا باوی پی ان باز نمیشن)، دیگه چون فقط داخل هست، بحث sync نداره. با تست های من و بازخورد دیگران، بعضی از هاست ها اینطوری هستند و گوگل هم بهشون دسترسی داره(اما وریفای سرچ کنسول باید فقط با دی ان اس باشه).
چه هاستی؟ اسم نمیبرم. پس فردا بد میشه میفته گردن من.
این هم بگم که در تمام شرایط، اختلال وجود داره. الان اپ تایم 90 درصدی(به جای 99.9 درصدی) ایده آل هست.
راه دیگه ای برای هم sync بودن هم در دسترس بودن از داخل و خارج نمیشناسم.
البته که متخصصین devops روی سرور های اختصاصی با هزینه زیاد میتونن. یک سری پلاگین وردپرس هم برای sync دو دیتابیس هست. ولی من چیزی که خودم اجراش نکردم آموزش نمیدم.
تمام صحبت های من در این باره:
https://t.me/mohsentavoosiseo/620
https://t.me/mohsentavoosiseo/623
https://t.me/mohsentavoosiseo/624
https://t.me/mohsentavoosiseo/625
https://t.me/mohsentavoosiseo/628
https://t.me/mohsentavoosiseo/631
https://t.me/mohsentavoosiseo/633
https://t.me/mohsentavoosiseo/634
https://t.me/mohsentavoosiseo/639
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/mohsentavoosiseo/680" target="_blank">📅 18:48 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-679">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zz60h26z45d89kl1rSwAN7rFf43y93IkfSLDCNbiR_RY2mvSqfl9kXZJhLqKji02fYnkHdW2q4VPkfRVFuCH1_mnJYM7ARLLeWVtP8VvjqihaKsNIl9UFmw7nT54ApnJTfWt95EY_xFyFvvNa8qHhGmtvjw8iDsP7BWtCOL_QfyBu3e_wxJGdfZFh6Csg88F2dPgIo91ZvZVSKx7F3uOR_XOe8fz9HwhN7eWyN1b7_fumQCWa9BAvA-KtjSXPxmyIr43HDoO8UHNpuIPbUXbAyr0scpcjEuYkurBkMXh2vvkIFq0EVVMaYW2RSxxUWs2xWopugRSh-jrIkJWrBih7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واقعا خوشم نمیاد از این خسیس بازی بیش از حد کلاد. دوتا لینک کرد و خوند، یه دونه گوگل شیت دویست ردیفته و ده ستونه ساخت کلاد مکس(5x pro) شد 22 درصد!
البته با Sonnet کمتر مصرف میکرد قطعا. ولی حوصله خنگ بازیش رو نداشتم چون کار گوگل شیتش پیچیده بود. آدم هم مغزش از جا درمیومد با این تسک.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/mohsentavoosiseo/679" target="_blank">📅 14:32 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-678">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">صحبت تلفط شد، خیلی ها خارج رو شامل چند تا دونه کشور خاص میدونن و ملاک ذهنیشون اینه: ایران و امریکا. ایران و کانادا. ایران و آلمان.
هرکس که مهاجرت کرده، ایران و کشوری که رفته رو راس میدونه تو ذهنش.
ولی بهتره ما جهانی فکر کنیم و کل کره زمین رو ببینیم. جهت خط خطی کردن ذهن هایی که ناخواسته محدود شدند، یاداور میشم:
خارج شامل هند، بنگلادش، نپال، سومالی، کنگو، هنگ کنگ، فیلیپین، میانمار، تانزانیا، گامبیا، بوسنی هرزگوین، مغولستان، لیتوانی، لیبی، مصر، غزه و رام الله و کرانه باختری، صربستان، مراکش، قرقیزستان، زامبیا، شیلی، بولیوی، گواتمالا و... هم هست و این ها هم خارج محسوب میشن و جمع کوچکی از سرزمین ها و کشور های غیر انگلیسی زبان هستند!
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/mohsentavoosiseo/678" target="_blank">📅 11:42 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-677">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تلفظ Claude به انگلیسی با لهجه بریتانیایی و آمریکایی، کلاد هست. آ کوتاه. کلود نیست. حالا شاید با انگلیسی غیر اصیل مثل هندی و سنگاپوری و اماراتی یه جور دیگه بگن.
تلفظ Claude در بعضی زبان های اروپایی و اسپانیایی و کره ای میشه کلودی.
کشور های مختلف هم به مدل خودشون تلفظ میکنن.
تلفط Claude به فرانسوی میشه کلود. با صدای O. صدای اُ . بعد از d هم e گفته نمیشه. کلوده نیست. کلود. ریشه کلمه claude، فرانسوی هست. در نتیجه کلود هم درست هست.
مثل BMW که متولد آلمانه و آلمانی ها میگن بی ام وی. و آمریکایی ها میگن بی ام دبلیو. عملا اصلش بی ام و هست(نه دبلیو). پورشه هم درست تر و آلمانی تره. پورش رو انگلیسی ها میگن.
اما کلاد، فقط واژه اش ریشه فرانسوی داره. ولی شرکت Anthropic، که سازنده کلاد هست، یک شرکت آمریکاییه.
خلاصه: هم کلاد درسته هم کلود. آ و اُ . کوتاه.
نظر شخصی: برای اینکه با فضای ابری قاطی نکنیم، کلاد بهتره. چه برای مخاطب انگلیسی چه فارسی. تلفظ رسمی انگلیسیش هم کلاد هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/mohsentavoosiseo/677" target="_blank">📅 11:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-676">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llj-PbTikLnQdYYUZ7_ulvZW1nEDEnfulbkpFNqz_aZccoYDVRc8fVvmaqb6AHZ7btvE4hwePHhi8Ng0KljDco4PraQwbnSjfx3hA9vNBzWvoHHDOQDWinz-oPLsUMsTgQMAQSnfPw2SOEtCh0tdRsf6KmmuKla58dWoLtNUJola5ZND6QQKk3RGHtIIFWVFujOKVeI7bwQAVDxT_7qgXoqFuLyg5IpMhQPj9kSRP32o9o_4Me4SliQKjT8L-CpFpN4J89EVXdhWsKq9Lsf5OaSRUbyJIDSH9GU9vR5XsqlLJp9VCPpHU7gwXFc37sWpBZIUTrOdDvRa-06hlHfdTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این همه خوبی از کلاد گفتم از بدیشم بگم. مثل chrome که اندازه اسب، رم می خوره، این هم خیلی مصرفش بالاست و گرونه.
کافیه یه کم تسکت متنی نباشه، نسخه Opus بسیار بسیار مصرف می کنه و البته بسیار هم باهوش تر از Sonnet هست.
این سشن ساعتی بشه 70 درصد برای کلاد مکس(5x pro) که ماهی 100 دلار پولشه واقعا زیاد هست.
کلاد پرو برای من اغلب کم میومد. کلاد مکس 5X اغلب زیاد میاد.
یک سری نکته برای بهینه سازی مصرفش از نظر زمانی هم تو
این ویس
گفتم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/mohsentavoosiseo/676" target="_blank">📅 16:16 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-675">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حالا من یه جوری از کلاد تعریف می کنم انگار اکانت کلاد میفروشم(اتفاقا پیام زیاد میاد برای خریدش).
درحالی که برعکس اکانت ChatGPT ارائه میدیم. چیزی که همش تو سرش میزنم
😅
ولی بهرحال اونم کاربرد خودش رو داره. من خود اکانت چت جی پی تی پلاس دارم اختصاصی رو اکانت خودم.
اکانت Cluade Max هم دارم که 5 برابر Claude Pro هست محدودیت هاش. ولی همه اعضای تیم ازش استفاده می کنیم.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/mohsentavoosiseo/675" target="_blank">📅 15:51 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-674">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
اگر یکی از موارد زیر روی شما صدق میکنه، یعنی هنوز بسیار بسیار عقب هستید در دنیای هوش مصنوعی. راه حل چیه؟ برعکس موارد زیر رو انجام بدید و رویکردتون در تضاد با این ها باشه:
❗️
- تو سر هوش مصنوعی نمی زنید.
❗️
- از هوش مصنوعی ایراد نمی گیرید.
❗️
- تفکر نقاد بهش ندارید.
❗️
- به عنوان فکت چک به حرف هاش و بررسی هاش نگاه می کنید.
❗️
- حواستون به سوگیری هاش و مموری که با در چت با شما ایجاد میشه نیست.
❗️
- از حافظه و مموریش برای اینکه چیزی بهش یاد بدید استفاده نمی کنید.
❗️
- بهش فحش نمی دید یا تند حرف نمیزنید و سعی می کنید باهاش مودب باشید و احساس یه انسان باهاش دارید(جدی)
❗️
- در صحبت با شما گستاخ شده یا به شما تیکه میندازه.
❗️
- از بخش های مختلف و نسخه های مختلفشون مثل instant و thinking و deep research و agent و کانتکتور ها یا خوندن فایل و لینک استفاده نمی کنید.
❗️
- موقع پرامپت دادن برای تولید چیزی یا انجام کاری، بهش دیتا نمیدید یا دیتای کمی میدید و بعد از اینکه تولید کرد تازه یادتون میفته بهش مشخصات بیشتری بدید. مثلا برای تولید عکس، نه سایز میدید نه نسبت نه تم رنگی و واقعی بودن یا کارتونی بودن یا استفاده کردن یا نکردن از چیز خاصی و... . اما به محض تولید هر خروجی یادتون میفته که ااااا اینم باید بهش بگم. تصورتون اینه که مغز شما رو باید بخونه اون بدبخت.
@mohsenavoosiseo</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/mohsentavoosiseo/674" target="_blank">📅 15:48 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-673">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">تفاوت کلاد و چت جی پی تی درباره اتفاقات 28 Feb 2026 یا 9 اسفند 1404.
چرا کلاد بی نظیره؟
یه گوگل شیت ساخت و دانلودش کردم. کپیش کردم. و تو یه لینک دیگه بهش دادم. گفتم بخون ببین چی میفهمی.
بهم گفت: این همون فایلیه که خودم برات ساختم!
✅
شما این کارو با Gemini و ChatGPT کنید میشینه توضیح میده. نمیگه این همون فایله.
✅
کلاد بهش گفته نشده هر سوالی رو حداقل تو انقدر حجم محتوا جواب بده. گاهی یه "نه" خالی میگه.
✅
کلاد علاقه ای به قانع کردنت نداره و سوگیریش به شدت پایین تره. سعی نمیکنه راضیت کنه الکی.
✅
از همه مهمتر، کلاد خیلی سریع تر میگه غلط کردم! این چت جی پی تی، یه موجود لفتیست دموکراتیه که کلا فکر میکنه هیچ اشتباهی نمیکنه و تاکید هم داره روش.
فاز اینم داره که نه فلان چیز شایعه هست. شما همین الان برو درباره اتفاقات 28 فوریه یا 9 اسفند ازش بپرس. متوجه میزان و درجه حماقتش میشی. وقتی جواب اشتباه داد بهش بگو برو سرچ کن. باز میره تو فاز اینکه نه شایعه است و... . و یه جوری تاکید میکنه و نقد میکنه که فکر میکنی حقیقت تو دست هاش هست.
بعد گیر میده که تو اشتباه میکنی. بهش میگی سرچ کن میگه نیازی به سرچ نیست!
حالا کلاد چی جواب میده؟
این سوال شما بر اساس فرضی است که نیاز به بررسی دارد. بگذارید جستجو کنم تا ببینم آخرین وضعیت چیست.
کلاد 100. چت جی پی تی صفر.
البته من دارم درباره Opus حرف میزنم. Sonnet بسیار خنگ تر هست ولی باز بهتر از نسخه 5.5 هست و گاها برابری میکنه.
بی انصافی نکنم، باگش تو 5.5 خیلی رفع شد. شما همین سوالی که گفتم رو برو بذار رو نسخه 5.4. کلا در حد ناندرتال ها خنگ میشه دوباره.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/mohsentavoosiseo/673" target="_blank">📅 15:36 · 16 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-660">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">هزینه اینترنت ثابت فیبرنوری تو ترکیه 1100 لیر هست با سرعت اسمی 1Gb در ثانیه و سرعت واقعی 600Mb در ثانیه که دیگه Wifi 5G هم جواب نمیده این سرعت رو. و با کابل باید ازش گرفت که افت نکنه.
میشه ۷۰ مگابایت دانلود، ۴۰ مگابایت اپلود. در ثانیه. (هر ۸ بیت، ۱ بایت هست).
با وای فای 5G تا 300Mb میشه اگه نزدیک مودم باشید. با وای فای 2.4G تا حداکثر 100Mb.
یعنی با دلار ۱۸۷ هزار تومن میشه ۴ میلیون و ۵۰۰ هزار تومن.
بدون محدودیت حجم.
تو کافه ها بدبینانه(استارباکس، اسپرسولب) حدود 30 تا 70 Mb در ثانیه هست(حدود ۳ تا ۸ مگابایت در ثانیه). بدون محدودیت حجم.
هزینه کافه: رایگان. یک بار خرید که پسورد بگیرید فقط. بعدا تو هر شعبه ای استفاده کنید بدون سفارش. بدون خجالت. بدون احساس وظیفه برای سفارش دادن.
اینو گفتم که بگم انقدر ما تخریب کردیم بقیه کشورا رو حالا اینه وضعمون.
به خودمون گفتیم متمدن و باهوش و به بقیه گفتیم وحشی و عقب مونده و کم هوش و خنگ...انقدر که گفتیم هه هه ارمنستانم ادم شد واس ما؟ ترکیه که فلان. یونان که فلان. بابا ایتالیایی که خودشون دارن فرار میکنن. دلار دیگه به درد نمیخوره. دلار مرد. امارات بیابون بود برای ما ادم شدن. عمان؟ اون بیابون که هیچی نداره بابا. گرجستان شاخ شده بلیت برگشت میخواد از ایرانیا! ژاپنی ها که تا قبل بمب اتم وحشی بودن! چینی های حشره خور! عرب های سوسمار خور! اصلا همه جا ایران بوده. همش مال ما بوده.
عاشق توهم و چیز غیر نقدیم! هیچ کاری یا واقعیت موجود نداریم!
حله. فعلا کانفیگمونو بخریم
😏
...
ایران چراغ قرمز مخصوص عابر پیاده نداره. یه دونه به من نشون بده! یکی فقط!
چراغی که فقط برای عابر باشه ها! نه اینکه یه گروه ماشین چراغشون قرمز و گروه مقابل سبز بشه. چراغ مخصوص فقط عابر.
چون از نظر مهندسی عالی و از نظر کرامت انسانی بی نظیریم.
فرض کنیم موتوری هام تو چراغ قرمز رد نمیشن! (فرض محال کن).
ایران از این نظر، هم رده افعانستان و پاکستان و بنگلادش و ویتنام و هند و بخش هایی از عراق و کشورهای شمال آفریقاست.
تعصب یعنی نپدیزیم. خرد و عقل یعنی بپذیریم واقعیت رو که بتونیم تغییرش بدیم.
پی نوشت(بدیهی برای اکثر شما)؛
Mb یعنی مگابیت
MB یعنی مگابایت
واحد سرعت، بیت هست. چیزی که ما بهش عادت داریم و تو دانلود منیجر می بینیم، بایت هست.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/mohsentavoosiseo/660" target="_blank">📅 17:41 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-659">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کسانی که میگن چرا طرف رفت ارمنستان یا ترکیه؟ اونجا که ظرفیت نداره فضای دیجیتالشون. اونجا که اقتصادش فلانه!
باید بگم
قرار نیست برن شرکت ترک یا ارمنی کار کنند. ظرفیت اونجا مهم نیست! از دیجیتال مارکتر ها بعیده این حرف!
اونجا فقط یه نقل مکان سکونت فیزیکی هست که اینترنت داشته باشند و بتونن عین انسان با سیم کارتشون ثبت نام و verify کنند در سایت ها و ابزار ها و... .
ما انقدر خوشبختیم که کلا جز ارمنستان و ترکیه جایی نیست بتونیم بی دردسر سه ماه بریم و یا نسبتا ارزون و راحت اقامت بگیریم.
یک کم داره اندونزی و مالزی هم مد میشه برای دیجیتال نومد ها. ولی اون ها هم دورند هم سه ماهه نمیشه رفت هم پرواز پردردسری دارند.
بعضی ها که از اسپانیا و ایتالیا و یونان هم ایراد میگیرن! انگار قراره برن شرکت اسپانیایی ایتالیایی با حقوق های کم اونجا کار کنند.
چرا ذهن باید انقدر محدود فکر کنه که محل فیزیکی فعلی زندگی یعنی شغلت هم باید وابسته به همون بازار باشه؟ اصلا چرا اومدی تو حوزه دیجیتال اگه اینجوری فکر می کردی؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/mohsentavoosiseo/659" target="_blank">📅 11:19 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-658">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به زودی در شغل های در سراسر جهان و ایران:
استخدام متخصص فلان (گرافیست، مارکتر، تولید محتوا، توسعه دهنده و...)
ملزومات مهم (نه امتیاز!):
تسلط به کلاد
رسیدیم به این جمله که در آینده افراد شغل هاشونو از دست نمیدن. بلکه کسانی که بلد نیستند با AI کار کنند شغل هاشونو از دست میدن. (فعلا غیر از کارهای دستی مثل آشپزی و ماساژ و خیاطی و...)
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/mohsentavoosiseo/658" target="_blank">📅 00:48 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-657">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">https://www.zhaket.com/web/speedix-plugin
این شما و این هم افزونه افزایش سرعت سایت وردپرسی در اینترنت ملی.
کسانی که سایت وردپرسی دارند(که اکثریت هستند)، می دونند درد کجاست.
این پلاگین درمان این درده.
✅
باعث کندی  با وی پی ان  یا از خارج از ایران یا زمانی که اینترنت بین الملل وصل هست یا اگه هاست خارج باشه، نمیشه.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/mohsentavoosiseo/657" target="_blank">📅 00:39 · 08 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-655">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۴
چیزی که بار سنگینی از دوش من برداشت
رها کردن چیزهایی که میخواستم حفظشون کنم
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/mohsentavoosiseo/655" target="_blank">📅 17:20 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-654">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۳
مصاحبه بین المللی
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/mohsentavoosiseo/654" target="_blank">📅 17:13 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نکته های تجاری ارتباطی مصاحبه ۲
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/mohsentavoosiseo/653" target="_blank">📅 17:09 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-652">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 5.65K · <a href="https://t.me/mohsentavoosiseo/652" target="_blank">📅 17:05 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-651">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پست بالا:
https://t.me/mohsentavoosiseo/649
درباره Opus بود. نه Sonnet یا Haiku
و من Opus در حالت Adaptive Thinking استفاده میکنم.
خود Opus مصرفش بیشتر هست. در حالت Adaptive Thinking باز هم بیشتر میشه مصرفش.
برای کارهای ساده در حد ترجمه و ویراستاری نقطه ویرگولی و...، اصلا نیاز به Claude نیست. مثل این میمونه که وسط آسفالت صاف، لندکروز ببری. سلطان رو سر چیزای بیخود بیدار نکنید.
تسک ساده هایی که خیلی هم ساده نیستند ولی پیچیده هم نیستند و فقط نیاز دارید خنگ بازی کمتری داشته باشه هوش مصنوعی، هم روی Sonnet. خیلی با Haiko  تجربه ندارم که بگم دربارش.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/mohsentavoosiseo/651" target="_blank">📅 14:02 · 07 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-650">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">کاهش مصرف Session پنج ساعته و هفتگی کلاد.
مصرف دوبرابر کلاد در ساعت های Peek
چرا اشتراکی خیلی معنی نداره برای کلاد؟
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/mohsentavoosiseo/650" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-649">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">چرا کلاد خداست؟ Claude خداست؟
بدی ChatGPT و Gemini و Grok چیه؟
۳ Anthropic فعلا
Google, OpenAI و
X.AI
صفر
سه هیچ به نفع انتروپیک(شرکت کلاد)
سطح این ویس مبتدی هست. بسیار مبتدی.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/mohsentavoosiseo/649" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-648">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴
در جریان باشید
🏴
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/mohsentavoosiseo/648" target="_blank">📅 21:32 · 06 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-646">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">پیامی از بچه ها:
خود ما از این روش اقدام کردیم و ۲ روز تقریبا سایتمون داون بود و هیچ پاسخی نمیدادن.
پیام دیگه ای از بچه ها:
من هاست خارجم نت افراز بود بکاپ داشتم ازش
هاست داخل هم از خود پارس پک گرفتم ریستور رو انجام دادند ولی سایت بالا نمیومد در نهایت تنظیمات رو خودمون انجام دادیم هم هاست هم cdn بعد اوکی شد الان هم خیلی خوبه هم سرعتش خوبه هم قطعی نداره
از داخل و خارج هم همزمان باز میشه
نظر من:
سایت Down میشه. برای من 24 ساعت down شد. ولی ارزید.
احتمالا پیام اول، مثل پیام دوم بوده مشکل فنیش ولی خودش از پس کار بر اومده.
جواب ندادن تیکت(بعد از فعال سازی) و... هم چیزی که بچه های پارس پک باید بررسی کنند که چرا چنین اتفاقی افتاده و چی بوده ماجرا.
من فیدبک رو میذارم اینجا. امیدوارم چه با روش من چه با روش خودتون، سایتتون رو در دسترس کنید و دیگه از وضعیت "در حالت انتظار" خارج بشید.
@mohsentavoosiseo</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/mohsentavoosiseo/646" target="_blank">📅 15:25 · 05 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
