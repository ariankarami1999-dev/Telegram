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
<img src="https://cdn4.telesco.pe/file/tecJTruiXiy5IwUOpV9OAVtCL2OtqO_FGAyrgw4wuTaP9DfGFit6YvYRFmGh1cTmUhOYUPiGJSMnFob09nbOHGdlY7dt9z44PtDwp-D_3cWRPvzxGeqaQXw6k6shHsFrj28mJU-4aqRevT112nOVufHftKZ5ppBeL5mNqiTMqwudQL_Lt3D-3bNt5n7vvhYpnRdJNTtvfohpmTTtCqmAf4TvQNIFHV7wAQBwCRr4miq96rHDOhtSrJrRzZCwFW_b5lT64rzFUh_d7Pmrhu5zlBWhpdl9YsKHc0VqRdkiNj0Al2wKcM_2LuHq6zPoCZ6FfWQlQlq44wMATpgIjp8AVQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 107K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 14:01:41</div>
<hr>

<div class="tg-post" id="msg-71718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gEh69QbmQAAmj8xjUZ2MJMfJ3sO3POPO5BE0lVrOfzWc1p-ZwnoiMXV_-Ib4KL-YwGkSVxZCajgcBpfJjSyImLLxflynnwbtp6THm2XHcH8oNZ8-iliSXgA7leb9CxOm71_6JsB4E0ZRT7JrZze_SJrPWxGYhlBzP4g6JSWby9SxpQX_lM3HsAykJcCnrFJSxSDs2J9au7MdY1YuRSOTBJw-myMs1W05bQ4uidWsEY-vSDaHRq2XjsMh39W7dKUKcjF28UwNmYCrDQUw4EdauzKb9qpU5oqzzUnm_tvJnkeam6L7yBSBOb2ZydzS1EP150Sf7nD_ztMce8PJHjtobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشته است
این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری می‌کرده، که در فایل فروش هم این اطلاعات موجود است
@News_Hut</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/news_hut/71718" target="_blank">📅 13:08 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71714">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49a175287c.mp4?token=SUGZVbGQ6JPPfd7F0CrQDeTuI5G9AYzN5mpbS-nHBud4jmgkOeiX_7eJEMQN64zwYMbP2UiZv2XsCcDlWMCx1B2bvrJ6NohNq9aALEGwbv49sXVjJnLb1RVfmuBMclZMJXGB-1mL6_0YVMtJYYZHj7Ufstq8_uiaCd_0mK-UqzZfG3jToPG726Ujwf4Pzh-oUvNUdSfJ9jNN6RtUxPAt3V1dMfMOQOzQfMo5pzMzEd_oha3Rz4PUnSEF4TwtvLMLHtUhT86z8DzMHPMeCaxcfEVekbKtTeF-r-4yajiKPANE_Cdm7BpjbYD6CG4AMDGZgw8Llf54tSOaCkE2NV1sAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49a175287c.mp4?token=SUGZVbGQ6JPPfd7F0CrQDeTuI5G9AYzN5mpbS-nHBud4jmgkOeiX_7eJEMQN64zwYMbP2UiZv2XsCcDlWMCx1B2bvrJ6NohNq9aALEGwbv49sXVjJnLb1RVfmuBMclZMJXGB-1mL6_0YVMtJYYZHj7Ufstq8_uiaCd_0mK-UqzZfG3jToPG726Ujwf4Pzh-oUvNUdSfJ9jNN6RtUxPAt3V1dMfMOQOzQfMo5pzMzEd_oha3Rz4PUnSEF4TwtvLMLHtUhT86z8DzMHPMeCaxcfEVekbKtTeF-r-4yajiKPANE_Cdm7BpjbYD6CG4AMDGZgw8Llf54tSOaCkE2NV1sAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
:ویدیو هایی از اعتصاب عمومی در سنندج،سقز،دیواندره و دیگر شهرهای استان کردستان به مناسبت چهارمین سالگرد قتل مهسا(ژینا)امینی به دست حکومت آغاز شده است.
همچنین ویدیو هایی از شهرستان پیرانشهر در استان آذربایجان غربی رسیده که نشان می‌دهد بازاریان دست به اعتصاب زده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/news_hut/71714" target="_blank">📅 12:07 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71713">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یه پسر ۱۴ ساله با یه دختر ۱۳ ساله وارد رابطه شده و ا‌ومده پیش دکتر میگه من پرده اینو زدم و گشاد شده؛
حالا اومد پیش دکتر ازمایش بده ببینه این دختره قبلا رابطه جنسی داشته یا نه.
سن رابطه جنسی تو ایران داره به ۱۲ سال میرسه!
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/71713" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71712">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71712" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/news_hut/71712" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71711">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZF7dBHFCxJAjsa1Fuyb_AwSNAGvtgka92vvYt2iJ7D72kpgMv-xsjq6q_OCMd6G1TH5CXnwnede3-yKEIS0lHSqgm3iBk5ysmRxsFtelDZXDvHYsKPW2RhxtXdvzzOFUeL2mybwy4ry1rEQcPKi32gFmRWSIhjx7_weu5XV703Tu9ZxpN2e-6Vvs9rT9luhCYZB33HM6IE1Q6fPPbXU0N3govsR7Spwh3vhDYWfTG9ayWmhpC_R0n3hx-LPcUbNU2W05jZ9E0pY_4tVEqwtEcD4EH3Pf-cYejWfpY6oNNSh8snFbVbjDXgGfsIQIvoTs_BRYoHe-Uyr0jxMvkS-h6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
جدال جذاب لیگ اروپا!
نبرد هیجان انگیز
⚽️
بنفیکا
🆚
میلان
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل اخیر دو تیم:
⚽️
بنفیکا: ۵ برد و ۱۵ گل زده
⚽️
میلان: ۳ برد، ۲ تساوی و ۱۱ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/news_hut/71711" target="_blank">📅 11:28 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEc_qQDBfY1wYSpfA0lHZSpOtsSyD-uX5IBstxtjbLipgXHArxbdrfXaO_Qb4DpV9Y6208ljnP8qkT2V5_q-0Z7o2atmnnJ21ltkkuR4gNjheYgGI_r9xJrfXqLyWaQXC5EBT3NZ1CN_Sar5adwPZi3RRU4YW4FQVLQdk4NzatZgpI73GWyxAbe-Gh1RZPbfo2gSynMSmWED9zB-TAB2LJPmPJ-2P3hm6-284ds0GjqcAQHEAKQRiy4cOSnHaxeFhP9_wdvhe0yAsjiL4B3KQ6qVzgWTEIPkbFVlz7nLqj_q4CZPhZ6dpyk0c9rpjdBT7n3HarCsFTOkgGTgq7ZkOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایالات متحده برای اولین بار تأیید کرد که سلاح‌هایی در مدار دارد.
مینک، وزیر نیروی هوایی:
ایالات متحده اکنون سلاح‌های کنترل فضایی در مدار دارد که قادر به دفاع از نیروی مشترک در برابر اقدامات خصمانه دشمن هستند.
از بیان نوع، تعداد یا زمان پرتاب آنها خودداری کرد.
نیروی فضایی می‌گوید که می‌توان از آنها برای "اختلال، تخریب و حتی تخریب" به صورت تهاجمی یا دفاعی استفاده کرد.
کارشناسان فکر می‌کنند که به احتمال زیاد، پارازیت‌اندازهای فضایی یا جنگ الکترونیکی - سلاح‌های جنبشی - مشکلات مربوط به زباله‌های فضایی را ایجاد می‌کنند.
این به دهه‌ها ابهام رسمی پایان می‌دهد.
اولین نقاشی نیروی فضایی به معنای واقعی کلمه یک هواپیمای فضایی را در حال نابودی یک ماهواره متخاصم نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/71710" target="_blank">📅 11:00 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26353c8137.mp4?token=FyJQaCIsn4Dg7zcG7s_S0d5FuR6-dVA72hRu6zZsLCnbk-tqvK9dsXhkCTYoEiVUtEHvgHjsQy6cE5BpiYoJZwTLv4J04y2R9rL8GkxNeDJah-zxPokHBPMPdqKVYlYjGCdDFzc1Fos2GpFwoB20bk_p14sA3Py6yYzLS4QtQJKAe99Fh1Y-3PoBjo7fb-RB624PxUZhFvZMOShn_BFUUvfB5kloNwSHrBXn1T1L76swI5eEOr7yovfYXuoKMsJAjXkExpkDArb8MyYuKH4v0MiOMX2OAyOPSPlI8B-tCK_Z0Pvg_mGhJ6-z4kzPwsfAlvFPZgrSKD-gKMTEG1lozw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26353c8137.mp4?token=FyJQaCIsn4Dg7zcG7s_S0d5FuR6-dVA72hRu6zZsLCnbk-tqvK9dsXhkCTYoEiVUtEHvgHjsQy6cE5BpiYoJZwTLv4J04y2R9rL8GkxNeDJah-zxPokHBPMPdqKVYlYjGCdDFzc1Fos2GpFwoB20bk_p14sA3Py6yYzLS4QtQJKAe99Fh1Y-3PoBjo7fb-RB624PxUZhFvZMOShn_BFUUvfB5kloNwSHrBXn1T1L76swI5eEOr7yovfYXuoKMsJAjXkExpkDArb8MyYuKH4v0MiOMX2OAyOPSPlI8B-tCK_Z0Pvg_mGhJ6-z4kzPwsfAlvFPZgrSKD-gKMTEG1lozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک دانش‌آموز دختر برزیلی بعد از اینکه نمره‌ی خوبی تو امتحانش نگرفت با چاقو به معلمش حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/news_hut/71709" target="_blank">📅 10:32 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=W6VZRQ2huGJY5ovGjcj7dWkiH4X0gdmJNQjHzv58BiOsCZjMmBjI5IhAl8dpRWGP3DKtUmo2RPbCd9-MX8y0SY4FseFw6bEGful_zom5MiSwtuQtlV7dKwlm6tnt5LgP0msMhqEs_fgG_wjwBR5ysFB5iCPOGw7UaVmfe6BVuZFTj3nPp_waU3Je1gv_s6OguEyVafhkcqmuabALB1CeZmKZvtXD4_S_nbHOlvxCQhhWykEEAZjJRVH7YCF6noecnINfz3VF8eKx9Q1HKcJdVVQvtqTX8qbd30tSkzHLuzPgKD8ntvv_Z1OKWZeHDFvxhl09rV-mYtqhdVOtiJIuSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f46fce321.mp4?token=W6VZRQ2huGJY5ovGjcj7dWkiH4X0gdmJNQjHzv58BiOsCZjMmBjI5IhAl8dpRWGP3DKtUmo2RPbCd9-MX8y0SY4FseFw6bEGful_zom5MiSwtuQtlV7dKwlm6tnt5LgP0msMhqEs_fgG_wjwBR5ysFB5iCPOGw7UaVmfe6BVuZFTj3nPp_waU3Je1gv_s6OguEyVafhkcqmuabALB1CeZmKZvtXD4_S_nbHOlvxCQhhWykEEAZjJRVH7YCF6noecnINfz3VF8eKx9Q1HKcJdVVQvtqTX8qbd30tSkzHLuzPgKD8ntvv_Z1OKWZeHDFvxhl09rV-mYtqhdVOtiJIuSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طبق گفته خانم دکتر(روانشناس بالینی)؛
خودارضایی نه تنها ضرری نداره بلکه خودارضایی یه چیز سالم و بی‌ضرره که به عملکرد ذهن و مغز کمک میکنه، باعث کاهش استرس میشه و حتی به رابطه شما کمک میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/news_hut/71708" target="_blank">📅 10:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71704">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-Dt_l5x6Xm8CyBL6sB1fk6cKhuaQjXD6OXuxBZ0ZFtgAECWQU6NwFm5RyVU05BNR_y_4lv1qAgOFj4vvaMZHt5hh-c90EQLxQ9q_wcwq7yn4if94S-dF6w0cvGUv90OiZJO3gdCZS5ZNfBofGeD5bzv25bnO3f8JQkrn7ZvjFjQrM3tTgd9jj9nUpOwsmdzjWp4_wxDtVkR4lAx71zx9AGWhxWmUcCiP1ERLoBBOoYN5TNTC9-aQZyBf_yaK_9FKy4cLwB33xlm3HNBrKrcLynnqKFe3b8YTEuBp7CvaQnzFr2zCI5cKDjkSbzAGC8eN6mqa6_Fy9lF9L3MUpAZJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=vUa5J3I_tZe3R2sBn4ReJXiRqSXlI2opmrySEWPBOpT6MOrmoEzSOn21EK6hWbTeyTczlIgD78__Bmyes8v800aMATQPV43VXAwF8eoFtD23cUXwlxGQ9z3pG3GSSOd-hL67gVOKrUfuQxQgFZhSFedNaAXSGYti0Hrr5V7hn5O9NziXFSGxrxtHT8JOpWzac5cYgouiNz8-CL_HrM3y8NosLyZzhE1ERD_Atve2rRhO_MoPa1YsJSNafvNPIhXh64HeQH46HpE9Id9qygmM-ucS-4ouqtDbHONcCvPLZwIMlyECgti7rsj1gox2n1xQl4FtFjt6xvhnycZUaBxpEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97e620d35.mp4?token=vUa5J3I_tZe3R2sBn4ReJXiRqSXlI2opmrySEWPBOpT6MOrmoEzSOn21EK6hWbTeyTczlIgD78__Bmyes8v800aMATQPV43VXAwF8eoFtD23cUXwlxGQ9z3pG3GSSOd-hL67gVOKrUfuQxQgFZhSFedNaAXSGYti0Hrr5V7hn5O9NziXFSGxrxtHT8JOpWzac5cYgouiNz8-CL_HrM3y8NosLyZzhE1ERD_Atve2rRhO_MoPa1YsJSNafvNPIhXh64HeQH46HpE9Id9qygmM-ucS-4ouqtDbHONcCvPLZwIMlyECgti7rsj1gox2n1xQl4FtFjt6xvhnycZUaBxpEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر تیک تاکر به اسم فاطمه تاجیک دیشب توسط چندتا دختر که میگفتن عکساشونو گذاشته چنلش خفت شده و خودشو دوست پسرشو کتک زدن.
@News_Hut</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/71704" target="_blank">📅 09:34 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71703">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEzuwC4eSf_d30pndB0QMKwvtoDSqZiFFHOJQjIfiZjRbp_yztnnhLGcnvZk0874V83X2bCiziRsQG-NQQDB8s0xy6VtmOoFtv5qaB9Rg9TrBOCNhVVA3rj4sK9KiwpX6MCIykkVBWLYObpKC9tKIjRh3nPNm6iqqNZwFelFAFLpLT1J8-xpEpcWVolCZogBIVLzgmN96boD4Wyn-JrypO1Hy1XYrc6BXF84Ma0J3klp74j3ieYC1nE3TDzA5u7qLO22fBc-p97n6JW9wPBcEKac5WvyvRF7PIcwNTPDVNsQ9zBQZRH9DY5o-ofE50h0RD2wLJf4lre9mWAOFPKR1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکسیوس:
فرماندهان ارشد نظامی ایالات متحده، اسرائیل و هشت کشور عربی هفته گذشته در آلمان دیداری محرمانه برای گفتگو درباره جنگ با ایران و امنیت منطقه برگزار کردند.
این نشست که به میزبانی «سنتکام» (فرماندهی مرکزی ایالات متحده) برگزار شد، با حضور فرماندهان نظامی اسرائیل، عربستان سعودی، امارات متحده عربی، بحرین، کویت، قطر، اردن و مصر همراه بود.
دریاسالار برد کوپر ضمن تأکید بر تداوم حضور نیروهای آمریکایی در منطقه با وجود حملات ایران، شرکت‌کنندگان را در جریان برنامه‌هایی برای گسترش تردد کشتی‌ها در تنگه هرمز قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/71703" target="_blank">📅 09:01 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71702">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71702" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71702" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71701">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GF74KEl991UPZ95IRQWdVu2IMDfEzbcjnN_PKPEGvy53R1SQBpmJKuxNE0UYkw3_pmQblTCfF0jvfN9RhSZ6Rog2acAULED3-oYdkrxIjiCjvBvPUFS5-deBPRi9zsG_mDaBWxiFFodcKlnnQcDI30I-WyLrxnKgJiV5vcpYMUTV8tS2HrblkYsadKGvBNoZznzpPa3fV7rl6YY05Lt6BD3OfwMGWygnYZVSANJSWGA7oR2ZzXOvi4PcUioN0HZ7Y5kL9DVV0t_BEbFjAx8FLM_DaFkap0JMglTkfifGRHgc6W7wAc_7eDaw5-QLh7KVIKbryAA-38JhnuqcoUp_kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71701" target="_blank">📅 01:58 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم  @News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71700" target="_blank">📅 01:38 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
⭕️
گزارش‌ها از شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71699" target="_blank">📅 01:35 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cGBhlm2p60MqAlMw6ctkBKrw8XsGpp6MnwQEJwsWT_xAT19NqURRg2IPwDPqZmsGr-0bYbbJ69LuE38OTQw3_zOcJmSf2HoRbsFfl6metcZEakMDMpiL7A0Y1u_HQebAAD4-2IXKR13xjziBgePC1cIrcC8U9dqafkUoQJnDfN6lk6K-rH7Ok0hnCxNDC0GwkQV-AmIyk5CDerDf_-VumcDXFKwntXqE8E2V4xHA1ztmNcOahXblduB4q0Sqyqd6i9k6298n7MqJZmTGvAQAcBhbsKLKarJ1W-se8cVEae-jfyS4rwFI9Bb_zNClyOy0_dbRAySjCehe6lntePGmcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری آلمان (DPA) مدعی است که حوثی‌های یمن اکنون در تنگه باب‌المندب مین‌های دریایی کار گذاشته‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71698" target="_blank">📅 01:27 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=FVd1WAAyb2LyFI0SxKqM9bXiEQMSgbVeMshnVaXmKyHXYr_0MVbA8A3u7Y9PfVGtR8cvNeNwyqpXhpOMDXt5JIdgxcZU8fhLSwc1Btrp3pC7L-TAwHeBhexsjGPUexPoxu9jjESS6pFpi8w_VP_0YTXFLc7eq-TtIui6a-GVJ7jkmwwFxUYq2w8PgIahbBAguCbJhT7cFIp7tS6PwLVlCTMAvKD5nqaIg-FwzI4FUuq5MV_bp__iLKWM68SZy7ZRNYB2icoa-aMbn7a2fXR3ktvJCLutr7HurATWT4UBCiKEQvpuPuyRD-r4h2QPt05eHprod8M-Tj9HPIIXkjKu2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/307693b5b3.mp4?token=FVd1WAAyb2LyFI0SxKqM9bXiEQMSgbVeMshnVaXmKyHXYr_0MVbA8A3u7Y9PfVGtR8cvNeNwyqpXhpOMDXt5JIdgxcZU8fhLSwc1Btrp3pC7L-TAwHeBhexsjGPUexPoxu9jjESS6pFpi8w_VP_0YTXFLc7eq-TtIui6a-GVJ7jkmwwFxUYq2w8PgIahbBAguCbJhT7cFIp7tS6PwLVlCTMAvKD5nqaIg-FwzI4FUuq5MV_bp__iLKWM68SZy7ZRNYB2icoa-aMbn7a2fXR3ktvJCLutr7HurATWT4UBCiKEQvpuPuyRD-r4h2QPt05eHprod8M-Tj9HPIIXkjKu2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا به‌تازگی طرح استیضاح دونالد ترامپ را که توسط «اَل گرین» (نماینده دموکرات از تگزاس) ارائه شده بود، با رأی قاطع و سنگین ۲۳۲ به ۱۴۷ رد کرد.
بخش بزرگی از دموکرات‌های مجلس به این طرحِ پوچ و بی‌معنی رأی منفی دادند، چرا که اَل گرین خودسرانه عمل کرده بود و آن‌ها می‌دانستند که این قطعنامه به جایی نخواهد رسید
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/71697" target="_blank">📅 01:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ونس امشب گفت که تو ماه‌های آینده، جنگ وارد مراحل جدیدی می‌شه؛
اما در شرایط فعلی همه‌ی تحلیلگرهای نظامی معتقدند که بخاطر انتخابات میان‌دوره‌ای، جنگی گسترده از آمریکا نمی‌بینم.
اما یه نکته‌ای اینجا وجود داره، انتخابات سنا و مجلس نمایندگان آمریکا  نوامبر ۲۰۲۶ (۱۲ آبان) برگزار می‌شه ولی نمایندگان انتخابی، با ۶۱ روز فاصله به سر کار میان، یعنی از ۱۲ آبان ۱۴۰۵ تا ۱۳ دی ۱۴۰۵، سنا و مجلس نمایندگان با همون اعضای قبلی ادامه می‌دن و می‌تونن قانون تصویب کنند؛ بنابراین از لحاظ تئوری، بهترین زمان برای حملات دوباره‌ی آمریکا همین دو ماهه (در صورتی که دموکرات ها پیروز بشن)
ولی یادمون نره که ترامپ یکی از غیرقابل پیش‌بینی ترین سیاستمدار های دنیاست
#hjAly‌</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71696" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WM9onFjRvK1ID4z9x1dG6EoXtRvqKlDSai6jKDYEOLvI141lZrmSesUWXR4lTjyQ5Gg7Z5Xu6VFiiQXQZIuhXntd-f1cmgeu_8ZEafeXZRFHlvvViCdPWlMH_pm-kYLLZIJqyoE2qv385EB7xMDRFf6GsE5a-MDKNyzda95yL7xhj6fqS3gxir_m0KLd2IsuCD8xKbMyAV6K6D6TGlwOonsvvFBhqzcZV30BAmtUk67f7y1KUvvYoywDfYnRwKdcFAUL6WxN7Ln9IzFAqJIm82oM-PZjhBgQ_jhvXOCzV0fQ4t6fBH2D3EHmKB0oyJyC3zSB66KTvBIssRFKxohPKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایلیا هاشمی:  امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت. مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71695" target="_blank">📅 00:03 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ایلیا هاشمی:
امروز صبح به برخی اماکن حساس دولتی در تهران دستور تخلیه دادند و چند ساعت بعد جنگنده در آسمان غرب و جنوب غرب ایران مشاهده شد، اما ناگهان همه چیز به حالت طبیعی بازگشت.
مشخص نیست چه شد، شاید یک حمله نظامی به اهدافی در پایتخت که لو رفت و در آخرین لحظه لغو شد؟ یا مسئله‌ای دیگر…
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71694" target="_blank">📅 23:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71693">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=JcAXVaAzQIowGZrLan9ha8Q0TMot1QPpdd_8IT1Ckwl5ZvPK0hpYQf7VZEgc3M_NHwjbZK5QkfSl-FdYlarCmxNnuT1zVr2XYAUqsfKjz2m4fh0cDSsNp9oTaack5ANSqtrtEnDuBtCVgrQAU3W7lAWF5YE8HndCFtnTpO7_Wov6BC3Z0fdl0iE7bM4wXz0cIm9mKy4N8C2a20ElTW02_zs-qhpIwBAOzP80ssBhTF1r_iMQ_x5Iyv2ofu7PeHgQjjNXTq-gFszIstK70yaenX5txDpsxHkpDMVI3nhau6q_mKVGKFcDpjXMpIaKk_c7k45hxG8YlyksRJSyav8HyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad7ec7235a.mp4?token=JcAXVaAzQIowGZrLan9ha8Q0TMot1QPpdd_8IT1Ckwl5ZvPK0hpYQf7VZEgc3M_NHwjbZK5QkfSl-FdYlarCmxNnuT1zVr2XYAUqsfKjz2m4fh0cDSsNp9oTaack5ANSqtrtEnDuBtCVgrQAU3W7lAWF5YE8HndCFtnTpO7_Wov6BC3Z0fdl0iE7bM4wXz0cIm9mKy4N8C2a20ElTW02_zs-qhpIwBAOzP80ssBhTF1r_iMQ_x5Iyv2ofu7PeHgQjjNXTq-gFszIstK70yaenX5txDpsxHkpDMVI3nhau6q_mKVGKFcDpjXMpIaKk_c7k45hxG8YlyksRJSyav8HyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سریع‌القلم:
آمریکایی‌ها بعد از انتخابات کنگره به سراغ عملیات نظامی علیه ایران می‌آیند چه دموکرات ها پیروز شوند چه جمهوری خواهان!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71693" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71692">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71692" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71691">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71691" target="_blank">📅 23:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71690">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=kyHWkgB1BqkKfs1IbGL7nSIaU0FqiQzmZwXxdZplGpYx5v3g9yj-H-9KjF3FFeoRAnBDxEIqfLOED46n4jTbqSan9AXN4Gj3fUyobDKRFO1EqiURMinqd1kYqjei4wAGjRNIIxTnQRG8nQCsi-ru-xYcwUyq1xNqHR5lJkA9gqaPeRtBdWPoLnogcYkpOAmDPN-_7fPsQL3PDwpyMVoxVl1Nvy008azY3dujo8bPeBXrhqwyDu_0a81pJ6zQzSiudZ83y7HGxsHvmMvgPSVnE7pf46ZKSN8YfM0PUczAS7ZMF_gHDbp_Y_eBnI196DZ3kehaxb5MBR1P8Hih9P9q8w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a06568e4fb.mp4?token=kyHWkgB1BqkKfs1IbGL7nSIaU0FqiQzmZwXxdZplGpYx5v3g9yj-H-9KjF3FFeoRAnBDxEIqfLOED46n4jTbqSan9AXN4Gj3fUyobDKRFO1EqiURMinqd1kYqjei4wAGjRNIIxTnQRG8nQCsi-ru-xYcwUyq1xNqHR5lJkA9gqaPeRtBdWPoLnogcYkpOAmDPN-_7fPsQL3PDwpyMVoxVl1Nvy008azY3dujo8bPeBXrhqwyDu_0a81pJ6zQzSiudZ83y7HGxsHvmMvgPSVnE7pf46ZKSN8YfM0PUczAS7ZMF_gHDbp_Y_eBnI196DZ3kehaxb5MBR1P8Hih9P9q8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبتای جنجالی یه
جنده
: دختری که ادعا می‌کنه باکره‌اس، دقیقا به چی افتخار می‌کنه؟
تو قطعا ایراد داری، مگه میشه یه نفر با کسی رابطه نداشته باشه؟ آقایون حتی توی سوراخ موش هم فرو میکنن، اونوقت تورو نکردن!؟
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71690" target="_blank">📅 23:15 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71689">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=DxzIw9wcFfUSjCn-FKljniA1a_wxDTeKprcD1cVRqrs6JXTyBRXzaP3ug3XHO-yZQQCNJshoyukRqhQDkb8p3vmRpRAsbepSYTLUXxcy11w4SnXZgUJ7zSVw98Q8JYDw98zRiw_WmJhBCC7H1rAD9ah-S9tnw6tE0BHWv0GDDPW8NAGJ7yzfCHPAIqI84TBtUGHNMOOkOioh_5Tk9JwWGofEE2Vs77eSj5OJTYG-Gf_qA37qNSdustnXBrFe8WRhJFt8BBUtEoz-8bO4_gaUccq-iiFVH2SujlXA8lXuU0eUmmADkoCzRYHnYv_fh6xT96dpkFmgzNnbS3Svkphozw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/626fac3cc3.mp4?token=DxzIw9wcFfUSjCn-FKljniA1a_wxDTeKprcD1cVRqrs6JXTyBRXzaP3ug3XHO-yZQQCNJshoyukRqhQDkb8p3vmRpRAsbepSYTLUXxcy11w4SnXZgUJ7zSVw98Q8JYDw98zRiw_WmJhBCC7H1rAD9ah-S9tnw6tE0BHWv0GDDPW8NAGJ7yzfCHPAIqI84TBtUGHNMOOkOioh_5Tk9JwWGofEE2Vs77eSj5OJTYG-Gf_qA37qNSdustnXBrFe8WRhJFt8BBUtEoz-8bO4_gaUccq-iiFVH2SujlXA8lXuU0eUmmADkoCzRYHnYv_fh6xT96dpkFmgzNnbS3Svkphozw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی ایران یه تور راه اندازی شده به اسم «هیلینگ آب دریا» ، این شکلیه که میرین کنار ساحل و تا جایی که میتونین باید گریه کنین.
برای شرکت در این تور هم میلیونی باید پول بدین.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71689" target="_blank">📅 22:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71688">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ائتلاف نیروهای سیاسی کردستان با انتشار بیانیه‌ای مشترک، برای(فردا) روز چهارشنبه ۲۵ شهریور ۱۴۰۵ (۱۶ سپتامبر ۲۰۲۶) فراخوان اعتصاب عمومی صادر کرده است. این فراخوان هم‌زمان با چهارمین سالگرد ژینا (مهسا) امینی و آغاز اعتراضات «زن، زندگی، آزادی» اعلام شده است.
در این بیانیه از بازاریان، اصناف، کارگران و دیگر اقشار جامعه خواسته شده است با تعطیلی مغازه‌ها و بازارها و خودداری از حضور در محل کار، در این اعتصاب مشارکت کنند. صادرکنندگان فراخوان، وضعیت اقتصادی، فقر، گرانی، بیکاری و همچنین آنچه تشدید فشارهای امنیتی و صدور احکام سنگین می‌دانند را از دلایل این اقدام عنوان کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71688" target="_blank">📅 22:07 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71687">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/265561794f.mp4?token=kGE5ckojkGscB4XWsPw-FpY_u_6lMor6-BmqWF6E9utAoaKvLd6HY2ho4EwZv3Sea8tpcizDtV09-jgcKgabgJv6YLKahiQXYzGBJy8RfJGkVghfSl9IiszlXjcyuAbpXenszkZTGuBb_-wlhzMHuef7m9kI0vqV0kQ8S4okV7Sldym7Q8bqAsMYqos_KvXJdJPymFmGT6hnaHMY5-H4W6XKbUAJXEE7Rs49AmbaS3Nj08ownaIg9zNZ7Jl2V_y9711bVcFkHwHUJXEHDjp0tW2fS676L5f55fyFnzVId1S2scvVJ9KeoaEA3eyYBpx_JRtwF1K9Iysh8DraMZ-Thw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/265561794f.mp4?token=kGE5ckojkGscB4XWsPw-FpY_u_6lMor6-BmqWF6E9utAoaKvLd6HY2ho4EwZv3Sea8tpcizDtV09-jgcKgabgJv6YLKahiQXYzGBJy8RfJGkVghfSl9IiszlXjcyuAbpXenszkZTGuBb_-wlhzMHuef7m9kI0vqV0kQ8S4okV7Sldym7Q8bqAsMYqos_KvXJdJPymFmGT6hnaHMY5-H4W6XKbUAJXEE7Rs49AmbaS3Nj08ownaIg9zNZ7Jl2V_y9711bVcFkHwHUJXEHDjp0tW2fS676L5f55fyFnzVId1S2scvVJ9KeoaEA3eyYBpx_JRtwF1K9Iysh8DraMZ-Thw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهاجرانی سخنگوی دولت :
امیدواریم نیازی به تغییر سهمیه‌های اول و دوم بنزین نداشته باشیم؛ ولی اگه بخواهیم گرون یا کمش کنیم حتما شما مردم را در جریان خواهیم گذاشت و بدون اطلاع‌رسانی کاری نمیکنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71687" target="_blank">📅 21:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71686">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">شنیده شدن صدای دو انفجار از سمت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71686" target="_blank">📅 21:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71685">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/61894edf33.mp4?token=A1J2p_XF-SJeyqNFFHXZ5B_WMrVqrzp7OcGHkA8N3thuk6e3-KnQytW9KzHKp6JsR9f2NzqA05AgawmUkJnzxZ-uVcWuwQxfkkjfV32MIN2_IsCs-EOqdBh5rvgxWBtQelhU9qc8SMDwV8Ot25hsASsi61C8k76vi3mmmzxomEVxBaUahIg3UMxmdGDUoF2E-4tQvlnu2S6RYwBgpeOwUhMOkaBNhVp_Pg74a8D8e7JAc1KqgEoWaJURysNkw9sEiHjEaNyDxtg5WcrhMLZH2Ff-0GpNYHuDsly-HcOIbmhyQG-46UhpmEvVSgYOsmlnhtDQPpCHQyn9qceTi1yOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/61894edf33.mp4?token=A1J2p_XF-SJeyqNFFHXZ5B_WMrVqrzp7OcGHkA8N3thuk6e3-KnQytW9KzHKp6JsR9f2NzqA05AgawmUkJnzxZ-uVcWuwQxfkkjfV32MIN2_IsCs-EOqdBh5rvgxWBtQelhU9qc8SMDwV8Ot25hsASsi61C8k76vi3mmmzxomEVxBaUahIg3UMxmdGDUoF2E-4tQvlnu2S6RYwBgpeOwUhMOkaBNhVp_Pg74a8D8e7JAc1KqgEoWaJURysNkw9sEiHjEaNyDxtg5WcrhMLZH2Ff-0GpNYHuDsly-HcOIbmhyQG-46UhpmEvVSgYOsmlnhtDQPpCHQyn9qceTi1yOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ساعاتی پیش، هواپیمای تهاجمی A-10C Thunderbolt II نیروی هوایی ایالات متحده، مواضع داعش را در نزدیکی «جبل‌العمور» در شرق استان حمص (مرکز سوریه) هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71685" target="_blank">📅 21:19 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71684">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q1QdwUeNvTTaRd3l3W-AxIG5ONgTFoAAR_xEPvclStGG6YgNdKClYSJ8-xJqNLF8e4hvfPKIB2ZEHrzxYeJnFuhYxH9LX4Mu9o4TPxDe9qbxpW2LpAjkUyAH_8rcWnygumXkttijTPA_D5s-7Xjy-lrXgCYnP3dWownPIYOPuZqPKxLiQ5GVEeCvws40JjfjH7TRry8dIsZMijmBMQJKggPtYrJcB6epoha0YKTLcLCC5nEsiU6UI0gRcbB8nHIyK-OsohJaPhytGDDonrm37beHT59l1vkJd6r6TA-t1tz4VuiwBirr_9dieGknVXNg0lgwm9PYNL2hWomvCw2t0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واشنگتن پست:
دولت ترامپ در حال تدارک فروش ۴۰ هزار بمب سنگین (از انواع MK-84 و BLU-117 با وزن ۲۰۰۰ پوند) به ارزش ۲.۸ میلیارد دلار به اسرائیل است؛ این بزرگترین معامله تسلیحاتی از این دست در سال‌های اخیر محسوب می‌شود که هزینه آن از محل پول مالیات‌دهندگان آمریکایی تأمین می‌گردد.
این‌ها همان بمب‌هایی هستند که بایدن پیش‌تر به دلیل نگرانی‌ از تلفات غیرنظامیان، ارسال آن‌ها را به‌طور موقت متوقف کرده بود.
این قرارداد برای تصویب به کنگره ارجاع می‌شود و می‌تواند آزمونی برای دموکرات‌ها باشد؛ چرا که در ماه ژوئیه، بیش از ۱۰۰ نماینده دموکرات مجلس نمایندگان به کاهش کمک‌ها به اسرائیل رأی داده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71684" target="_blank">📅 20:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71683">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=YWVDJPkUdkbI1-FNut-9vghZJYcvmIyhgFX3sv8gJFhnnvAwUP9KYKqsQrfMZzFoErVyHTu1oPsH3WHncyktcyp3AnRm5OehlxLTZ2dZwpH8fcwsTbuBCqii-nTdOkn4kj5cxCQfCfCVVWA2_fNV546oQGS1y4w3j9SKjn7R1AkVe-HSr5WToetLedE2ARanfdkDAGheuuz4cm5heW3jFhBNI98kz--c1NNQkoaVqWazuh5KfPwGnTSjVTQl8ouLG_nHZuSgWCL4bksg5S_NnLB-qOl-Hor2F4ziCokF8DYarONutkGRzm2jLJxcLQyksKzurNDn7lNZuPcxntwBBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc6afc5269.mp4?token=YWVDJPkUdkbI1-FNut-9vghZJYcvmIyhgFX3sv8gJFhnnvAwUP9KYKqsQrfMZzFoErVyHTu1oPsH3WHncyktcyp3AnRm5OehlxLTZ2dZwpH8fcwsTbuBCqii-nTdOkn4kj5cxCQfCfCVVWA2_fNV546oQGS1y4w3j9SKjn7R1AkVe-HSr5WToetLedE2ARanfdkDAGheuuz4cm5heW3jFhBNI98kz--c1NNQkoaVqWazuh5KfPwGnTSjVTQl8ouLG_nHZuSgWCL4bksg5S_NnLB-qOl-Hor2F4ziCokF8DYarONutkGRzm2jLJxcLQyksKzurNDn7lNZuPcxntwBBYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران تصاویری از نفتکش «ال‌گایا» (EL GAIA) پس از اصابت به آن در بخش جنوبی تنگه هرمز منتشر کرد.
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که ایران ماه گذشته با موشک و در پایان هفته جاری نیز با پهپاد به این نفتکش حمله کرده است؛
در مقابل، ایران مدعی است که این شناور پس از ورود به «منطقه ممنوعه» در بخش جنوبی تنگه، با یک مین دریایی برخورد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71683" target="_blank">📅 20:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71682">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbKAAWY07A0k3HPbI7Ge3exU-lxhjPjeUeqPv8SskLIR4oZVw4bK3qswcHXzufopv6DxOZuy7vBTUBHRaBlZ6LbtjQORVqyurUD-DOOzoGzVEdVNZUGYkyzNFov2R05XMILqk8t8lEFMAWpVjkvLnM9VDzPUgXIguX9upRoa1lOmG3y9FU2P1IMXfuNd8caJjtQS4uRFwbwXUCweCRFtmsJvC8s46j66RZA0UDwBLd57IXHnnWIqe8qCeDHplFjj9glORTUeDzmX17IijD2lsSXTllfeb12_F-d4-Q6_mvdewOY0pqIlW6a8JgbukN3txVBI5Fwk75eHVOk-e7Jg5lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cc9cce711.mp4?token=pvj2JYAm5JEkvoAro3_eBmgYfBalV_iCZ-VBRQ8HBCBZz4Xgq7_UhpnzFnXQ9uGdICVC9lWFJhCBqFHt_pTADUHUQ2jUqoZe5S8_orN34AQEvWWokZVHAumrSj9QGj2IbAXcL0LOWdsnl3YizjlI92c3ervHS3DDQ9c9IHqnQ6weve2uHkoxA_Qy66dQm8Yd0JunVvcSEB7QcTM9tuSYHnw57fNNSWDU08wWE_BhHp4zwX0Ip45P4C9h43XGg457GLzqf8wbEAq84ruTnMPQC7Wv6am1es6t74uHS0MM9WutS0ahFvz1EorDilpFQ4rmzocAQDtG8lw8hPLyGK0fbKAAWY07A0k3HPbI7Ge3exU-lxhjPjeUeqPv8SskLIR4oZVw4bK3qswcHXzufopv6DxOZuy7vBTUBHRaBlZ6LbtjQORVqyurUD-DOOzoGzVEdVNZUGYkyzNFov2R05XMILqk8t8lEFMAWpVjkvLnM9VDzPUgXIguX9upRoa1lOmG3y9FU2P1IMXfuNd8caJjtQS4uRFwbwXUCweCRFtmsJvC8s46j66RZA0UDwBLd57IXHnnWIqe8qCeDHplFjj9glORTUeDzmX17IijD2lsSXTllfeb12_F-d4-Q6_mvdewOY0pqIlW6a8JgbukN3txVBI5Fwk75eHVOk-e7Jg5lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت وزیر خزانه‌داری آمریکا درباره ایران:
تنها کافی است به سخنان رئیس‌جمهور، رئیس مجلس و رئیس بانک مرکزی ایران اشاره کنم که اذعان داشته‌اند اقتصاد کشور در وضعیتی بسیار وخیم و بحرانی قرار دارد؛ هشداری که خطاب به هم‌قطاران تندروی آن‌ها در سپاه پاسداران و همچنین مردم ایران بیان شده است.
ما شاهد سقوط ارزش پول ملی و تورم سرسام‌آور بوده‌ایم؛
و در کمال ناباوری، کشوری که سومین ذخایر بزرگ انرژی جهان را در اختیار دارد، اکنون با قطعی برق سه تا چهار ساعته مواجه است.
این وضعیت اسفبار اقتصادی ناشی از تحریم‌هاست؛ ترکیبی از تحریم‌ها و اقداماتی که ما طی ماه‌های گذشته برای شناسایی و مسدودسازی مسیرهای مالی و سیستم‌های پرداخت آن‌ها انجام داده‌ایم و در حال اعمال فشار شدید بر آن‌ها هستیم.
به باور من، واکنش‌های تند و خشونت‌آمیزی که اکنون از سوی آن‌ها شاهد هستیم، درست مانند رفتار حیوانی زخمی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71682" target="_blank">📅 19:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71681">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=ekkFnccnzeMli2rfOysqx3Zva1OoJCiqNFhaldWO8ioEi6FURRzBZN7b3-cV8lwgr1cwUw_VKTTEpliermRjfyNzV_stlZlpLaNGAD-rzMp8kOHrjWQF-HGGOIEfR_g57bNgFmmUY-EQGDgC89-7MReOXvptp2wx_qzV0YEC1-XQ7nqSej-P5rwZSsstJL823BRVqKdwowDI6HUtLz3Pg8-mr-s67ZPQv9TCEjKl-VofHGQdSgJtDw0oFWYlAm1zsMZYA5vypKyp2a7VwKEV3KybW_1Yi-hKUTsY4MA1-iM0IfgOjhMhPoxwyJKY1PfwUpr_ujyHuRI-Y26TP_eFrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d47763dcd.mp4?token=ekkFnccnzeMli2rfOysqx3Zva1OoJCiqNFhaldWO8ioEi6FURRzBZN7b3-cV8lwgr1cwUw_VKTTEpliermRjfyNzV_stlZlpLaNGAD-rzMp8kOHrjWQF-HGGOIEfR_g57bNgFmmUY-EQGDgC89-7MReOXvptp2wx_qzV0YEC1-XQ7nqSej-P5rwZSsstJL823BRVqKdwowDI6HUtLz3Pg8-mr-s67ZPQv9TCEjKl-VofHGQdSgJtDw0oFWYlAm1zsMZYA5vypKyp2a7VwKEV3KybW_1Yi-hKUTsY4MA1-iM0IfgOjhMhPoxwyJKY1PfwUpr_ujyHuRI-Y26TP_eFrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویر، آتش‌سوزی‌های گسترده در تأسیسات ذخیره‌سازی «آرامکو» در «ابها» واقع در جنوب غربی عربستان سعودی را پس از حملات پهپادی و موشکی حوثی‌ها نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71681" target="_blank">📅 18:53 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71680">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
لحظاتی قبل یک پهپاد دیگر از نوع MQ-1 متعلق به آمریکا بر فراز تنگه هرمز با استفاده از یک سیستم پدافند هوایی متعلق به نیروی قدس سپاه پاسداران انقلاب اسلامی سرنگون شد.
این سومین پهبادی است که سپاه مدعی سرنگونی آن در روز جاری شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71680" target="_blank">📅 18:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71679">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8132b94509.mp4?token=dq_SlCtrwzOnbZxUSB8-kPNKTiK7G3eJvyaNA2KXDTZ8NpcnbL5Y50Dbx4hkJjmP7Zl5hdm_IlrmUMjIsoYSmXgzihjpBHgx7lsS72QQY2oXjQ72pNQVbPeTqBjfY9b-jqNP580Pg6WWFR7rWQgc6wphCFbD9vFKowE12hdE_F-W6qRA2O7b2duzcxGgt5_EfjGAa-ZBfd-7TyMo_CZnePPZDfRCpqjNpYsCBM2QJDJ49OO1rfWaYH6Iy2IEvD2_BGczAQRsx3jrKTNLB7_GER9hRryhSpDrSWHqK3U6vgUKCjyvtYGBm5hcibdg1TI0nkTmXA7dwomPhdHDb47u7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8132b94509.mp4?token=dq_SlCtrwzOnbZxUSB8-kPNKTiK7G3eJvyaNA2KXDTZ8NpcnbL5Y50Dbx4hkJjmP7Zl5hdm_IlrmUMjIsoYSmXgzihjpBHgx7lsS72QQY2oXjQ72pNQVbPeTqBjfY9b-jqNP580Pg6WWFR7rWQgc6wphCFbD9vFKowE12hdE_F-W6qRA2O7b2duzcxGgt5_EfjGAa-ZBfd-7TyMo_CZnePPZDfRCpqjNpYsCBM2QJDJ49OO1rfWaYH6Iy2IEvD2_BGczAQRsx3jrKTNLB7_GER9hRryhSpDrSWHqK3U6vgUKCjyvtYGBm5hcibdg1TI0nkTmXA7dwomPhdHDb47u7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از پروازهای داخلی(کرمانشاه به مشهد)دچار سانحه شده و بخشی از کابین دچار شکستگی و اسیب میشه، خوشبختانه مسافران این پرواز سالم به مقصد رسیدند. جزییات دقیق این پرواز و نقص فنی هنوز مشخص نیست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71679" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71678">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71678" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71678" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71677">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crMEWfHuMyOHXrfUtnN81NGw5j9cc6FzdekykFE8CaKEfBx-fOXUyPKmsxrPlh6Wxu1SO6D7TwGwAJ4NGTus-dSFZwNfSYXq2Wje8UiubCX4_i02UOGM7ZCTrcEevJTQgqs6SUmDf4HQPxCeZKFg1RPSXXdJNynghfLw116kPVswdTBdm4pAIema9czlF98Eu6s9o3g7A_AGwGWjmvM1BnB3ShLRYVTNpXbYobEpkBbjoYRyBvvPJQFwRExHmfIW7re7Zxnq_OD8Y_fpQQ1aihg6eFXoO9gz9cJHPN4nJeLE-Sx_SZg6beKrcodVYWTRVtYYM99v_p4gR6n2O9rUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
تاتنهام
🆚
لیورپول
⚽️
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
تاتنهام: ۱ برد، ۲ تساوی، ۲ شکست و ۵ گل زده
⚽️
لیورپول: ۲ برد، ۳ تساوی و ۸ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71677" target="_blank">📅 18:17 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71676">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=ZhwmMuxNIs8f28Pv_vuZbiwfuoIQ-7Hcd6fZLsANNWV75tZ-lqpJXDUOrW1x48O8l3uq4Mw0d25SG45RrU1oXgXLvso6BGqHCq7mKEEuW-WqxRULfStpu1h4orwm5mxOsJvcSdnbs1K8sjwfOetDjUHo_wSxnhvY70sZpnStlkvLNkyKhoqPQjbezpFIrUmqbS-CLsJVha_88oLM9EbiVjBxO-tjWDNBBPEiPsRAyz-vOHiml7pkcpLg7xPejydI5aeG_uktdLW_RVuJeunvKh3g2M_rKs0TbIidZtvDfkynfer4TA305e6qYhZ3iqw0_IfyECj-v5_IDTXE6JVZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea966d07eb.mp4?token=ZhwmMuxNIs8f28Pv_vuZbiwfuoIQ-7Hcd6fZLsANNWV75tZ-lqpJXDUOrW1x48O8l3uq4Mw0d25SG45RrU1oXgXLvso6BGqHCq7mKEEuW-WqxRULfStpu1h4orwm5mxOsJvcSdnbs1K8sjwfOetDjUHo_wSxnhvY70sZpnStlkvLNkyKhoqPQjbezpFIrUmqbS-CLsJVha_88oLM9EbiVjBxO-tjWDNBBPEiPsRAyz-vOHiml7pkcpLg7xPejydI5aeG_uktdLW_RVuJeunvKh3g2M_rKs0TbIidZtvDfkynfer4TA305e6qYhZ3iqw0_IfyECj-v5_IDTXE6JVZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛
بسنت درباره ایران:
ترامپ در حال اقدام علیه رژیمی است که خود را وقف شعار «مرگ بر آمریکا» کرده و برای تحقق همین هدف به دنبال دستیابی به سلاح‌های هسته‌ای است؛
اقداماتی که رؤسای جمهور پیشین مدت‌ها از انجام آن طفره می‌رفتند.
تحت رهبری او،آمریکا دیگر تهدید ایران را مدیریت نمی‌کند؛ ما در حال پایان دادن به آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/71676" target="_blank">📅 18:12 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71675">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2t9p3t6b7FSVgiL56gbJa-JYV50ViX2Ec1qIZdVHqCn5pLKM9bTaISaR2cDN6GsVUwQ-kGr1I7kUgrOqNEbtuuUYqhMQ3EN-CkGcN5YRcuJUH-LXaiSwpMwqGY5OMLonqTzGZa4AmABWu1t54iBMS-8TlE7aif1DdoLFtr6tFp3COmx8Dca8JYYmnjS5sKCpObr8xhJep6-v9BJYMaSlQPyBjps8QeqNOFa4rEE2PbleWB8tM0kEQh-OUDtzMZ-awjs2imm-OSiTf-Jm1s89SEBWIynAiyN_1Hd7OrAyJ_oQMNu2LO9ipIa5chd_SGMdSz-aAQ0Yu2eaodZvs8qvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس. تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.   @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71675" target="_blank">📅 17:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71674">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=ip7hYvmURuGxFaJU-GwLNcKUAb0roSU1IWvm6GaY1hfWRNSbsY8RFUYSPhfB2eHZ1WCxs9Tol1pCsPLuAIOQnUkN8YkcP9YI3jyt6ljjM_9eFvE283TKd0LsfOVPch7zRmoHSh-uf6MApXCZtGIQk0299RPBk9_tely6bdmQyDY9J-S6rrjpCmsasWdvOt6mh2m9lpOIm4TIZuc4fmsyHmHP8XRYSX9VCHdP-ODbNk9zuvliJcDbXVQnuAGzvkdHd6qO5pH8jSqi-xOj6Ki_fmSIMSdGRfaAk16u6ABfCULQRcpVDIVtBi1h2y5yEX4kv2XHrLPx8narIjt97b2P8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4824aba9.mp4?token=ip7hYvmURuGxFaJU-GwLNcKUAb0roSU1IWvm6GaY1hfWRNSbsY8RFUYSPhfB2eHZ1WCxs9Tol1pCsPLuAIOQnUkN8YkcP9YI3jyt6ljjM_9eFvE283TKd0LsfOVPch7zRmoHSh-uf6MApXCZtGIQk0299RPBk9_tely6bdmQyDY9J-S6rrjpCmsasWdvOt6mh2m9lpOIm4TIZuc4fmsyHmHP8XRYSX9VCHdP-ODbNk9zuvliJcDbXVQnuAGzvkdHd6qO5pH8jSqi-xOj6Ki_fmSIMSdGRfaAk16u6ABfCULQRcpVDIVtBi1h2y5yEX4kv2XHrLPx8narIjt97b2P8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو سی‌و‌سه پُل اصفهان، یه پسر نوجوون اومد مثلا یه حرکت نمایشی بزنه و از یه ارتفاع نسبتا بلند بپره پایین که فرود ناموفقی داشت و با سر رفت تو زمین...
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71674" target="_blank">📅 17:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71673">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=Lar9fTAF8ykU-9As4s7GbJh3yKzACW4OV7Ym-me5_CAk5zJftOWBzEUVCP2aktZwIobQ-slK6nuKW2Eng6DgaQxz3NFKh5Mn_FF_Wq5Drq4wWVIr4vMflV3acB_gZXI-u3ZfENI6QRF7pR1dTple-381JgUIBjSLJrC_ZCT2kfglqfwgxr4WUnNzblLsktMLHHhoDe2dEjWpGcCk0LDS7W8NgbQgfI9ehTO0ddxg42GKQMoH8xPMQNHSEEO0LE83sJdoitGEWG-K-mLqd9L6rVBC6cplJlorQVzDTl6AysdSx8j6Wg1NbDeMyWLvSLW18iSl4s5M6AsFEkijTio35g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b63b29bdd.mp4?token=Lar9fTAF8ykU-9As4s7GbJh3yKzACW4OV7Ym-me5_CAk5zJftOWBzEUVCP2aktZwIobQ-slK6nuKW2Eng6DgaQxz3NFKh5Mn_FF_Wq5Drq4wWVIr4vMflV3acB_gZXI-u3ZfENI6QRF7pR1dTple-381JgUIBjSLJrC_ZCT2kfglqfwgxr4WUnNzblLsktMLHHhoDe2dEjWpGcCk0LDS7W8NgbQgfI9ehTO0ddxg42GKQMoH8xPMQNHSEEO0LE83sJdoitGEWG-K-mLqd9L6rVBC6cplJlorQVzDTl6AysdSx8j6Wg1NbDeMyWLvSLW18iSl4s5M6AsFEkijTio35g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محسن هاشمی: من خبر دارم مسئولین در هر دو جنگ از تونل‌های مترو به عنوان دفتر کار استفاده کردند
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71673" target="_blank">📅 16:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71672">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">نفتالی بنت درباره ایران:
این رژیم فاسد و پوسیده است؛ همچون درختی که از درون دچار پوسیدگی شده و سرانجام فرو خواهد ریخت.
در مورد این درخت پوسیده، می‌توانیم اینجا و آنجا حفاری‌هایی انجام دهیم. منظورم صرفاً اقدامات نظامی (کینتیک) نیست.
صحبت من درباره اقدامات اقتصادی، کارهایی که نمی‌خواهم نامی از آن‌ها ببرم، و همچنین تقویت معترضان داخلی و تقویت دشمنانِ این رژیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71672" target="_blank">📅 15:40 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71671">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=AU7qe3XrZunjlX5bRnW_hjE6_KqiXRil0xuqneQBSxgbB-OJGmF4p2a_PYp2aYNqKLsxWngYX6RZTmEuUSNq8orRRYxpmA3VPnaHo7Q-UXGS2wjpy5hYMKlxNPuZcBxd493nkINXS1yrvnmE4dI24V7ADNET8s_XVg_g2yiqfAEmev-d2snk5nEM8eE3jg-q7YpmCWZM5DoUGtlwVvoMrI81auJNanuLQBD93xAdKrTxBJhVH1r2R69N3HyWp9GWQvkegSs0fK22SLHAt-bkuBZ3UNc3zvq9130kfN4UKaBTU4Obg8YKCbV4CALEJhbiKrXwLGb6xsxRdHlJI6Q7tA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afac6b01df.mp4?token=AU7qe3XrZunjlX5bRnW_hjE6_KqiXRil0xuqneQBSxgbB-OJGmF4p2a_PYp2aYNqKLsxWngYX6RZTmEuUSNq8orRRYxpmA3VPnaHo7Q-UXGS2wjpy5hYMKlxNPuZcBxd493nkINXS1yrvnmE4dI24V7ADNET8s_XVg_g2yiqfAEmev-d2snk5nEM8eE3jg-q7YpmCWZM5DoUGtlwVvoMrI81auJNanuLQBD93xAdKrTxBJhVH1r2R69N3HyWp9GWQvkegSs0fK22SLHAt-bkuBZ3UNc3zvq9130kfN4UKaBTU4Obg8YKCbV4CALEJhbiKrXwLGb6xsxRdHlJI6Q7tA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌ های این خانم به‌شدت وایرال شده و دخترا هم خیلی بهش انتقاد کردن:
اگه یه مرد، دارایی های خودش رو به نام خانومش بزنه، اون زندگی رو با دستای خودش نابود کرده.
آقایون اگه ۵ تا خونه هم به نامشون باشه، هیچوقت تو دعوا خانوم‌ خودشون رو بیرون نمیکنن
ولی اگه خانوما یه چیزی به نامشون باشه به این موضوع فکر میکنن که میتونن بدون اون آقا ادامه بدن.
من خودم خانواده‌هایی دیدم که به دخترشون میگفتن تو که ماشین و خونه به نامت زده دیگه احتیاجی بهش نداری، خودت برو زندگی کن.
خانوما اصلا جنبه‌‌ی اینکه چیزی به نامشون باشه رو ندارن، اون اگه بخواد زندگی کنه با یدونه سکه هم زندگیش رو میکنه، آقایون بفهمید من دارم چی میگم...
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71671" target="_blank">📅 15:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71670">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=I3ko91kt1zMYZVdHDZabnWM9I-XJ2R3J4ilLY5VN_yvXZL3nkAkfEmeAZeOvUmB_oAJ7e4M10Wwonwli_Jqy2b0quZM1krwAUQvkNUyT9NL4GMFXnRahpCawD9vnknhiRXNroy-w4gqQm2qdpID2k80sprUUjdZW1su4PP0w8hg3g9ytRa02AwLoGQYLzy34psHdZ0vNywfd_aX8DRO_ordLk1-2MN0R9pbF8AiXG5MnU68HB4tcB7sA-y9Nclx8q1y4pnRWyc4i56icY6mlj-0QumgkG2AfuaRnH-F7_ixLE9fUx96CnUFBuMfS-CRdE6n_bECNkTyzvevsZyUBLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5632e037a5.mp4?token=I3ko91kt1zMYZVdHDZabnWM9I-XJ2R3J4ilLY5VN_yvXZL3nkAkfEmeAZeOvUmB_oAJ7e4M10Wwonwli_Jqy2b0quZM1krwAUQvkNUyT9NL4GMFXnRahpCawD9vnknhiRXNroy-w4gqQm2qdpID2k80sprUUjdZW1su4PP0w8hg3g9ytRa02AwLoGQYLzy34psHdZ0vNywfd_aX8DRO_ordLk1-2MN0R9pbF8AiXG5MnU68HB4tcB7sA-y9Nclx8q1y4pnRWyc4i56icY6mlj-0QumgkG2AfuaRnH-F7_ixLE9fUx96CnUFBuMfS-CRdE6n_bECNkTyzvevsZyUBLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیراندازی نیروهای انتظامی به سمت بالگردآمریکایی در جریان عملیات نجات خلبان مفقودی آمریکا در روز روشن
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71670" target="_blank">📅 15:03 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71669">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=o7ZfIASwl0ZECb3I2i4WvV9lcCrTRmNWDU1jJDyfNIcCimUWP9NBNIjXheZIgHHL9d8fvRMCVR-_yjKaELghGHim7wIFpgt-OjYz_LBJgZhvvRPSXabhYXPTi1X_sIeuMAbYI3FHSTaUMF2UwnPHMA-ccmVtlhKcnoHgEtDIdVsyxudvGD9o7QQYr1DXlOO3447BZzy9j4Q9XIuADJTIaIYZnuAUFP6lnaaR7OgPbHyiuKVkcPClhqfmNRmtUBrZKK2mA07qTCM3yi4ezErF9T5uWKDOAJiU4xznjoAydLDX9jaofb_Mkg2ty4aq5uf1zV414Wj1zlSRmB4jHbtAJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ada1fff69c.mp4?token=o7ZfIASwl0ZECb3I2i4WvV9lcCrTRmNWDU1jJDyfNIcCimUWP9NBNIjXheZIgHHL9d8fvRMCVR-_yjKaELghGHim7wIFpgt-OjYz_LBJgZhvvRPSXabhYXPTi1X_sIeuMAbYI3FHSTaUMF2UwnPHMA-ccmVtlhKcnoHgEtDIdVsyxudvGD9o7QQYr1DXlOO3447BZzy9j4Q9XIuADJTIaIYZnuAUFP6lnaaR7OgPbHyiuKVkcPClhqfmNRmtUBrZKK2mA07qTCM3yi4ezErF9T5uWKDOAJiU4xznjoAydLDX9jaofb_Mkg2ty4aq5uf1zV414Wj1zlSRmB4jHbtAJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برادر زنِ مجتبی خامنه‌ای:
مجتبی خامنه‌ای با همسرش سریال " فرار از زندان " رو مفصل نشستن دیدن و درباره اتفاقاتی که داخل سریال افتاده بود هم صحبت میکردن.
یه بار تو یه جمعی گوشی یکی زنگ خورد، من گفتم این چه آهنگیه دیگه؟ که یهو مجتبی گفتش این آهنگِ یکی از فیلم‌های کریستوفر نولانه دیگه، چطوری نمیشناسیش؟
‌
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71669" target="_blank">📅 14:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71668">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RF8kf94Rldj-I2TWcftQ453DC-7u-VAYWIIMUCgdlNqmLU5ktXNSX10V6tGkUbafL5-EqK30iE-5DBVKx6_m8nHt_jVPIA8MLwDBx-8lxx4CKQ1nNz_gfV-uCOhP3BmWRR52VLT0j8oxvqo6BrGTYXBl0mjG5RNPaOd7BrBiL-ERAl3PLtiuctwjpe5xixLZ_dzmX0-Odz9GjdHco1LH_qWN98puRBDTMj4T0J6tjOPhS2gXR0yXmJruF2RCsmfbaaEPedsv98iCSVLBhM3HtAEezCuFozkXrCHUAnqGswco_rjrYvOM7rgdPKeXsDitbTbPcRFm92NgTZBnVgI0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی:
«نشست عمان» با حضور کشورهای خلیج فارس برای تثبیتِ مسیر تنگه هرمز، با نقش‌آفرینیِ جدیِ آمریکا و برخی از کشورهای حوزه خلیج فارس فعلا لغو شد
عربستان» به بهانه اصابت خط لوله‌اش و درخواستی که از پاکستانی‌ها داشته تا ایران را راضی کنند که به انصارلله بگوید از فتوحاتِ جدید عقب نشینی کند، «بحرین» بابتِ ناراحتی از جنگ رمضان و پرتابه‌‌های متعددی که بخاطر میزبانی از زیرساخت‌های نظامیِ آمریکا در خاکِ کشورش دریافت کرده و «امارات» هم بابتِ اُفت جایگاش در آینده‌‌ی منطقه در صورتی که مسیر جدید تنگه تثبیت شود، در نشستِ مهمِ عمان شرکت نکرده و کارشکنی کردند!
ولی بازیگرِ اصلیِ لغوِ این نشست، آمریکاست!
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71668" target="_blank">📅 13:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71667">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حملات موشکی/پهبادی حوثی های یمن به مکه، طائف و جده عربستان سعودی
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71667" target="_blank">📅 12:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71666">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9B2JysG81KebXFLV1lmMH-vNesC7_DF0nk2DgEXpRMnmHb8ZAlXDq_ldN2cVLUvLPcc8joIR6TuMBi28IjLqsd4nKHQFd04JLffs-gWqJ2CSKep_o7tQ2sGi-89EBfjL7ewDOPkeBeuhG5VPIH6RZn0bgdLDR0FtG26a3nniY3wQ8Sk99XDLSWA8Y8uPwK0-FVGTcY22KrvBka5QVpbxedVbcsQCxciud84ZGkYo2s4V1PYYBDJpRrRaZ5TFH1uUVP00jQjTSSc83q6JEOf0gc3WyARtXX0bWpRUPyOMAWbVgLfnFzS6-OfLuuadD89jE3CvFWYk_mZkhqOBjZIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) :
گزارشی با تأخیر زمانی درباره وقوع حادثه‌ای در تنگه هرمز دریافت کرده است.
یک منبع موثق گزارش داده است که شناوری مورد اصابت یک پرتابه ناشناس قرار گرفته است.
هیچ‌گونه خسارت یا پیامد زیست‌محیطی گزارش نشده و مقامات در حال بررسی موضوع هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71666" target="_blank">📅 12:52 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71665">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=coDTa4QI1A6FkH4__DkLhJ8Op3l-_faqXmW-oA2HGHK1JQGOmYACJjjYHkPC4P-O5H_UMEY8bDFoWeIMRqPMTXMSbC5RbEqtZfoWTf819hrFBtjFarIX-e3U5rcFacX69G5huxk5G2Uk3t6sF9QlCOXhYF_-y6HL0OFKbPVRkjSf2ruVf5z2Sb2TMWyNn5ln0VdVs2SMapm-3uAwRQGMwSaqoIrBCW78m_rD15FYHiE_BndbuFVQxyMiL2Y3N-znfGsp5z3KRG4sdVdoUtjJ3tXT26dmWzwzMCqEUVjqfLl5yhCR9C6rQG5VAy-23bOoUH3QWjYr_T-iv9xtKcLAag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee29acd4a8.mp4?token=coDTa4QI1A6FkH4__DkLhJ8Op3l-_faqXmW-oA2HGHK1JQGOmYACJjjYHkPC4P-O5H_UMEY8bDFoWeIMRqPMTXMSbC5RbEqtZfoWTf819hrFBtjFarIX-e3U5rcFacX69G5huxk5G2Uk3t6sF9QlCOXhYF_-y6HL0OFKbPVRkjSf2ruVf5z2Sb2TMWyNn5ln0VdVs2SMapm-3uAwRQGMwSaqoIrBCW78m_rD15FYHiE_BndbuFVQxyMiL2Y3N-znfGsp5z3KRG4sdVdoUtjJ3tXT26dmWzwzMCqEUVjqfLl5yhCR9C6rQG5VAy-23bOoUH3QWjYr_T-iv9xtKcLAag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبه ناو سپاه با عنوان «رودکی» که در جنگ ۴۰ روزه منهدم شد در حال غرق شدن است. این کشتی تجاری بود اما به نظامی تغییر کاربری داد و گفته شد هلی‌کوپتربر است اما هدف حمله قرار گرفت و نابود شد.
در جریان جنگ ۴۰ روزه تقریبا تمام شبه ناوهای سـ.ـپاه و ارتش از بین رفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71665" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71664">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71664" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71664" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71663">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9CFvO6-Lby68UxAsCpGKiFeChZVN-dospJw-w_9gxsC0lAxzqEI3H84nd5pPZG4CVbn13QxGrjAtvrsTl_HMLFV2XrVMTet9sqIY2vXbGxkgBvDbQwnAy5ZJCqG7ZMA1KQ4hzzJSgcLBo31jqzbJ23dwNaDN7nwnWqPCasgg7VD0sAb-usi99AIn6BUygxZRLTntl1Mmh0gAqX12j-XI-4jDtVvwefeUGPjoluj6wKPTAwLBtM3yarmg0KnWcOqCFciytkNHwKuDh8OSGdqy6Vhpwin5UkVTjCtVqSqiqbXGX2i0ewx8NlyPnaT-AOMJAuGx442m92tBpxhjQH6vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز
⚽️
رئال مادرید
🆚
الچه
⚽️
را در TrexBet پیش‌بینی کنید!
📉
نگاهی به آمار دو تیم در ۵ بازی اخیر:
⚽️
رئال مادرید: ۴ برد، ۱ شکست و ۱۴ گل زده
⚽️
الچه: ۲ تساوی، ۳ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71663" target="_blank">📅 12:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71662">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/rvRQ43W1tJetzmWgp05F8lzWJsPknW4C2QXJIFZm_QaoMK96DC9x5xSFGKrsOo_97EJaolxa-GjWySDmYTYLejHUOH1x_ctrMqgAAq_yhIzv-EDbwvMHGVpY4G1jPB_2tlsL5hGWGox4fJ0Fr-ASoWdbn4TopOc5TFop6mQzwOaGrP9mpvylBvtCfMQ4SA5C--OLvbMCZyZuhzF88efUIolJTRYpSHEXKQdyeX08EyUrBkRmDSxyhCuRBvs9304UVeT29hacFzk8zr8azLJzHnaktkoLP5HoGZp2zy_PIjvQJRHk0ap8ZU5FAsKuExI9K1MFARlDJDnwW5BIH4QlWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک فروند هواپیمای دولتی ایران با شناسه پروازی «IRAN06» از تهران پرواز کرده و بر فراز ریاض، عربستان سعودی مشاهده شده است
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71662" target="_blank">📅 11:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71661">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=ahHOAJjDA5qQXVwMaG3UBi2jscQj5jRBvyueE_4lMVKozz0RZNiF0HhzQhxi0E8O_FHpYSlPG7koZ510vhsb5oqxTfGKOni1NeCHpYskvluvdMJ6Jz0OISYWv1B1sqGIvBJlo9Ur8DDy35JbddrpMvIyPEEsO8kNk3mvK2JgXCZz3BFjAgUSLjtdNnS-vxiiPgvtUTh2TLV6r0C7iQKG5n4mIYKv-eAYvlHjrJvL89wnWlKIsrJWSxSo-74rlz9FWTDXeTWUgAGBV5nMmGp9jQdKteasLdfcFdzft2ZAZhSBvo3viQ7KhDlQgrXR1VngKr1diYLa7kl9XmWm3F0OdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f2f2bddd6.mp4?token=ahHOAJjDA5qQXVwMaG3UBi2jscQj5jRBvyueE_4lMVKozz0RZNiF0HhzQhxi0E8O_FHpYSlPG7koZ510vhsb5oqxTfGKOni1NeCHpYskvluvdMJ6Jz0OISYWv1B1sqGIvBJlo9Ur8DDy35JbddrpMvIyPEEsO8kNk3mvK2JgXCZz3BFjAgUSLjtdNnS-vxiiPgvtUTh2TLV6r0C7iQKG5n4mIYKv-eAYvlHjrJvL89wnWlKIsrJWSxSo-74rlz9FWTDXeTWUgAGBV5nMmGp9jQdKteasLdfcFdzft2ZAZhSBvo3viQ7KhDlQgrXR1VngKr1diYLa7kl9XmWm3F0OdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری: آیا قرار است همه ما تا ۱۰ سال دیگر بمیریم یا نه؟ موضوع بحث همین است.
ایلان ماسک: خب، متأسفم که باید این را بگویم، اما همه ما خواهیم مرد.
مجری: می‌شود یک بازه زمانی مشخص کنید؟
ایلان ماسک: بله، نرخ مرگ‌ومیر همچنان ثابت و ۱۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71661" target="_blank">📅 11:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71659">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🎙
صحبت های این خانم درباره سگش:
خرج ماهانه سگم حدود سیصد/چهارصد میلیون تومنه
😳
روتین روزانش صبح حدوداً ساعت ۱۰ بیدار می‌شه، یعنی صبح همه رو بیدار می‌کنه. بعد تا ساعت یازده که می‌شه، یه مربی شخصی داره که میاد می‌بردش یه جا مثل فضای باشگاه.
بعد هم که ساعت سه و چهار غذاشون رو می‌خوره. پوستش حساسه و یه سری شامپوهای خاص داره که ما همیشه می‌زنیم.
شب‌ها من یه دور پیاده‌روی می‌برمش و بعد هم شامشون رو خودم می‌دم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71659" target="_blank">📅 11:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71658">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=AawL6EkMurlzgKTFJyiEHMD22Yg5g03WahgPQlotiBM0jgJMVkDztwluFHfiuPMngZxWMzBsBknzmrcMjFSLHFZAFO9nAChCSe7m4O9ijMBVcRvxhynE6W3Rr6ZAq6VHWMSrTzJGXFTlyFLs_PZB0_8rzNc5DTG8OGjyLWi4IbarO2GMBBbDRsJtzUk9pZQBV1-O1ZGqbxuIYNyNn3RcCaGASID-a29GkoD4zHOGLDfJsh9c_46tFsCgIuHUVgQCT2VyBWdRTjK7O_DRMbLD0h6Az4eosoa9yiTiqSLPjcDtAT3_WVm6PqREOPQIacECCoHUTIY9cmuRCB4f6wqrZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ea33bdfd.mp4?token=AawL6EkMurlzgKTFJyiEHMD22Yg5g03WahgPQlotiBM0jgJMVkDztwluFHfiuPMngZxWMzBsBknzmrcMjFSLHFZAFO9nAChCSe7m4O9ijMBVcRvxhynE6W3Rr6ZAq6VHWMSrTzJGXFTlyFLs_PZB0_8rzNc5DTG8OGjyLWi4IbarO2GMBBbDRsJtzUk9pZQBV1-O1ZGqbxuIYNyNn3RcCaGASID-a29GkoD4zHOGLDfJsh9c_46tFsCgIuHUVgQCT2VyBWdRTjK7O_DRMbLD0h6Az4eosoa9yiTiqSLPjcDtAT3_WVm6PqREOPQIacECCoHUTIY9cmuRCB4f6wqrZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعارهای عجیب علیه روحانی در تجمعات شبانه
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71658" target="_blank">📅 11:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71657">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوباره آمار مبتلایان به کرونا تو کشور داره می‌ره بالا، خیلی مراقبت کنید
من خودمم دو روزه به شکل عجیبی گلو دردم
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71657" target="_blank">📅 10:43 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71656">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/840407be05.mp4?token=lD_hT_1xvKk8jPpAp_nQTk9RKQp4UG2TDhd6Uq3pqrDdBiHxp3vmROh3Hkmsk1Cff3HuTxd_iXqxp5rZ5qRks2I0nBeNgij_TEmZR0NrUUtIjsPaDAVU2gA3qUlgIQokYywN8EZ3FBiO8bZeF2lBXjE0oQpOFEGfCaRuwjO2ht3yZ8vfb8qYZK5TGkuWQY3ec93CjX0rgQg3AlAJ4JvJZmZ6sWR01NR2JJRPp3n_M8bvns0vP8egA-IcKMYmrdgMf17KyfRGqXraERexnmDi7LawtscF4dubXASZHTxARBYKAZu9yeOJ0qTWDU2bRwGimXfdWWbtTBwvOI4p_bKbog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/840407be05.mp4?token=lD_hT_1xvKk8jPpAp_nQTk9RKQp4UG2TDhd6Uq3pqrDdBiHxp3vmROh3Hkmsk1Cff3HuTxd_iXqxp5rZ5qRks2I0nBeNgij_TEmZR0NrUUtIjsPaDAVU2gA3qUlgIQokYywN8EZ3FBiO8bZeF2lBXjE0oQpOFEGfCaRuwjO2ht3yZ8vfb8qYZK5TGkuWQY3ec93CjX0rgQg3AlAJ4JvJZmZ6sWR01NR2JJRPp3n_M8bvns0vP8egA-IcKMYmrdgMf17KyfRGqXraERexnmDi7LawtscF4dubXASZHTxARBYKAZu9yeOJ0qTWDU2bRwGimXfdWWbtTBwvOI4p_bKbog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلار شده 240 تومن؛
همون لحظه صداوسیما:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71656" target="_blank">📅 10:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71653">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=KhN2L1qPF62Obfr2h0FvH8O3yPVN6Nnv66VNi6kamwLckXySm39FRb0G6utep1_OGuRNRnENMGw6azSl2jox3BP2aTueyfhFbcTBSrhyhv2OAEh5PE__y9nV5EH6asUCnmtmej6eDCLziSLrjqLDeOy910gF8Wu3lykG52-WPGGDT3O1-ZSE-yokrHI47-oBDcwFt6miUVh2ufH76FHRVNUx_YzlHWylYadAaz8cAIpTTQaCg81jQgulTw45LsHa81LpotskbXXFqJ_XsgdbSF5VFqc36J-hsvYn5bFZgCELI6fyDjsJDz8oUxyRkm0z2vDaFfF6gLtpAIr_hIYWwq4iI9Urb5JPCsRISqsiMtNexHdjNbqSmpF8-iUPDndSyxA_q3f8kWtyVZ_wxkZboR4cfCcFfgyAtAh4snZ6tBtm5S0jPaoZP39rjr-k-O6G7P799yABGfWT1BaVvZz26nBnjshzR5H13O_5IznL5frPvtaAu3dRgqIJCOj7cA0VgABuJdvi2YnDci7v5eEJkKrri_yjdBwNYzuMF0jdRsE_570U2JdXONcyiPVdiCAEWGhEEihljCsUkPhqTsZu8fq3_Lz107P2RZbw4xj6wmLA65T1VjSdIAFgUE0TwDyAKkCMHmNZ49Mk6RyJKPV8NKsgkl_tbm9G8tvCv3TE2Vo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1a54c7cbd.mp4?token=KhN2L1qPF62Obfr2h0FvH8O3yPVN6Nnv66VNi6kamwLckXySm39FRb0G6utep1_OGuRNRnENMGw6azSl2jox3BP2aTueyfhFbcTBSrhyhv2OAEh5PE__y9nV5EH6asUCnmtmej6eDCLziSLrjqLDeOy910gF8Wu3lykG52-WPGGDT3O1-ZSE-yokrHI47-oBDcwFt6miUVh2ufH76FHRVNUx_YzlHWylYadAaz8cAIpTTQaCg81jQgulTw45LsHa81LpotskbXXFqJ_XsgdbSF5VFqc36J-hsvYn5bFZgCELI6fyDjsJDz8oUxyRkm0z2vDaFfF6gLtpAIr_hIYWwq4iI9Urb5JPCsRISqsiMtNexHdjNbqSmpF8-iUPDndSyxA_q3f8kWtyVZ_wxkZboR4cfCcFfgyAtAh4snZ6tBtm5S0jPaoZP39rjr-k-O6G7P799yABGfWT1BaVvZz26nBnjshzR5H13O_5IznL5frPvtaAu3dRgqIJCOj7cA0VgABuJdvi2YnDci7v5eEJkKrri_yjdBwNYzuMF0jdRsE_570U2JdXONcyiPVdiCAEWGhEEihljCsUkPhqTsZu8fq3_Lz107P2RZbw4xj6wmLA65T1VjSdIAFgUE0TwDyAKkCMHmNZ49Mk6RyJKPV8NKsgkl_tbm9G8tvCv3TE2Vo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوهای این خانم معلم برزیلی مهربان و زحمتکش بخاطر سبک خاص تدریسش حسابی وایرال شده:
تو یکی از ویدیوهاش که حسابی هم وایرال شده به یه دانش آموز فوت فتیشش که درسشو خوب بلد بوده به عنوان جایزه اجازه داده پاهاشو لیس بزنه…
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71653" target="_blank">📅 10:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71652">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=dhvfq8esabwzRs_S3k2dzYyNNaFU_MCRNpEPCbLg-UqDHFA0_1wcSt0nE8TXUdDuoqM0rOrIvkDZTjg7LhKxp6lf8Rmh1eZMaqLjohdkJqjrC5DlRPfJbbe3D8LgCnrwAUSTUM-v-PBHiDYxa1rvuBgntE8GgyVADlBT6BaUYE0cg-tNz7RstKhcfxgfX7mwEfmA3SLbg9CKLEz86iIdlEyHGFjS9YBYb9IufyuBcUUHNM15GV6wgZ73v9eRfTKdZaSZnM-lhoNxoHLpeVCuAwoIGo7qh0oVi4oMQwGdfM4lKWfqNls8OqCosIwxGborUVWHJ4y8I49lNVX_QwZ7wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f71ea40a.mp4?token=dhvfq8esabwzRs_S3k2dzYyNNaFU_MCRNpEPCbLg-UqDHFA0_1wcSt0nE8TXUdDuoqM0rOrIvkDZTjg7LhKxp6lf8Rmh1eZMaqLjohdkJqjrC5DlRPfJbbe3D8LgCnrwAUSTUM-v-PBHiDYxa1rvuBgntE8GgyVADlBT6BaUYE0cg-tNz7RstKhcfxgfX7mwEfmA3SLbg9CKLEz86iIdlEyHGFjS9YBYb9IufyuBcUUHNM15GV6wgZ73v9eRfTKdZaSZnM-lhoNxoHLpeVCuAwoIGo7qh0oVi4oMQwGdfM4lKWfqNls8OqCosIwxGborUVWHJ4y8I49lNVX_QwZ7wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوستاد خوش‌چشم، کارشناس صداوسیما:
در عرض ۴ ماه موشکی ساختیم که هنوز اندیشکده‌ها و رسانه‌های غربی موندن که سیستمش چیه. موشکی که بدون نیاز به ماهواره، ناو در حال حرکت رو پیدا میکنه و دنبالش میره.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71652" target="_blank">📅 09:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71651">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/168229fd60.mp4?token=CdCPBj-q2qZlLesnKQbd32Ju6uIhGRjnmgJK-KY5Zu0QEQV--YL5OPH7c-z3Ca2n1a2zVLE-6NIixgwNeo8HUKSOUsB2c_5oQOkOlsZi0RycE8xQYkPUGPKgcQA9nq9MJDq9LaxPhScMcP-J_XMrQ4WVBzg9GGhvjANNuOgE5LFJWNLD15fOmrspHOJ2f84AbC-LdU1jiPJRX6GroLaO4phkAbmtLHqJzKSFCUbE4er_JLkN78B1jvpmGjlnlIpUztkSqWBzgTELh0tbCN8VqYxLUcFeb_YgHHlIIHt6An-kITTIIeLGlOWlh6OAUidyRdLPab5pDbXRbyulmVsvaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/168229fd60.mp4?token=CdCPBj-q2qZlLesnKQbd32Ju6uIhGRjnmgJK-KY5Zu0QEQV--YL5OPH7c-z3Ca2n1a2zVLE-6NIixgwNeo8HUKSOUsB2c_5oQOkOlsZi0RycE8xQYkPUGPKgcQA9nq9MJDq9LaxPhScMcP-J_XMrQ4WVBzg9GGhvjANNuOgE5LFJWNLD15fOmrspHOJ2f84AbC-LdU1jiPJRX6GroLaO4phkAbmtLHqJzKSFCUbE4er_JLkN78B1jvpmGjlnlIpUztkSqWBzgTELh0tbCN8VqYxLUcFeb_YgHHlIIHt6An-kITTIIeLGlOWlh6OAUidyRdLPab5pDbXRbyulmVsvaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواب رییس کمیسیون امنیت ملی به روحانی:
اون روزایی که تصمیمات غلط میگرفتن اون زمان دنبال رفراندوم نبودن بلکه دنبال حاشیه بودن
اکثریت مجلس خواستار برخورد قانونی با روحانی هستیم و این تقاضا رو ارسال کردیم
قرار نیست یکی تو گذشته مقامی داشته الان از عدل الهی و کشوری مصونیت داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71651" target="_blank">📅 09:00 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71648">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=QTFVQJHs-MTNEFzZ9lN8LyBj6hzvM4APcM_g3etLog5WPXdN_WHt7un_dyYXu8i53H8OcnldNfnShi-zEBtFk0AGzCaZpYOV5FNAe8IykB_NYi1SlO1rS-0xr0YGfbukFEV0jZr4QYOH0hVhjjl3dEmSCfapPuQaq2HFWE7jjR1BzTdj2vlkr-V_9sGcVNn6LYnfUp-948XOicrvZKR5WNVKXtfvRkUPHWJrp0Defsm-UIfcnWhU_MeEGk1K3OLKRVttxgkP5_imNSlrDzTxnShVZ0C2zVmRTLMgQBMoxELIG4YqHq7Gaf4K_zPfKwAZGaGdn0tqXSvC7mbio8BALQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8b5c1f510.mp4?token=QTFVQJHs-MTNEFzZ9lN8LyBj6hzvM4APcM_g3etLog5WPXdN_WHt7un_dyYXu8i53H8OcnldNfnShi-zEBtFk0AGzCaZpYOV5FNAe8IykB_NYi1SlO1rS-0xr0YGfbukFEV0jZr4QYOH0hVhjjl3dEmSCfapPuQaq2HFWE7jjR1BzTdj2vlkr-V_9sGcVNn6LYnfUp-948XOicrvZKR5WNVKXtfvRkUPHWJrp0Defsm-UIfcnWhU_MeEGk1K3OLKRVttxgkP5_imNSlrDzTxnShVZ0C2zVmRTLMgQBMoxELIG4YqHq7Gaf4K_zPfKwAZGaGdn0tqXSvC7mbio8BALQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل یک عملیات ترور علیه یک فرمانده حماس در غزه انجام داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71648" target="_blank">📅 00:54 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71647">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J-S78yUNtE_fKk953XWk00_8T8N2rxku8zLeUWAx_El2Dw5dPj2cj7nLRjAajzcgu84p8xv_U8Sz0zLRGEAvPfyBaWhZQa5piTh3vatjPp97or2hxmrzo8z0pyBZzGfqYxx5WzTDOSsvGldcqNk6bHHObqivmZognbxzbIrid45xdOwDvCEzmplLkKoUShdKbRMgrTNOiprvDaTqeyPOqbS4cxLKStj-zS44ZCr9Bm40eUqDOB1iZKRtjspgo6xDH709bfN3JleHoZJlUJVbgvO1AT2_EIiUxh2N20q0V6heEXAC6Wp_jh_tr2LhSR4vCq9LbtNUXd5L6BBnBXhHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
با سیگنال‌های متناقض رئیس‌جمهور آمریکا حواستان پرت نشود؛ از «مذاکره نمی‌کنیم» تا «برای گفت‌وگو آماده‌ایم». معادلات مربوط به نفت و تنگه‌ها تغییر کرده است. دست و پا زدن برای کنترل تبعات، جلوی آنچه در‌راه است را نخواهد گرفت.
تا زمانی که شروط ایران محقق نشود، هیچ مذاکره‌ای در کار نخواهد بود. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71647" target="_blank">📅 00:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71646">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">فارس:حمله پهبادی ارتش آمریکا به دو قایق در حوالی بندرکرگان در آب های خلیج‌فارس.
تعدادی از صیادان مفقود شدند و عملیات جست‌وجو و امدادرسانی آغاز شده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71646" target="_blank">📅 23:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71645">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fIYrVyCai9v9iaW6SKerC1Rd7FidAbA8rTvRtwPhVC20C-922xpwCWmmWxiKRFMRfsLqd5_HhXUETVBdsf-Sv6U61fwDUiMQca7eFocxHT9SShpCR9nHVKQQwkE2cBkWruwjfI2hVEgilmFl7DKPH2YTW8uYEkMUewgYoqDMKPHDvnKTSDPg0qLKU3zk0EsigZvJdQf6QAR2Xf_BaGRktNK8tfcI_Wz2ouE7tC8xf6dEWWP7povsbQHcChYZwvT7oN019qthF85-aQQRtZYqPMlVuycmw7iFZJtiqqFldA3voWM440IdqxQUm18E8kThwIa9jbDzGwyzhpe8XI5W-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
ماه گذشته، نفتکش «ال‌گایا» با پرچم پاناما هدف اصابت موشک ایرانی قرار گرفت و از کار افتاد. آخر هفته گذشته، در حالی که این کشتی در آب‌های ساحلی عمان لنگر انداخته بود، ایران بار دیگر با استفاده از پهپاد به آن حمله کرد.
این نفتکش هم‌اکنون توسط یکی از شرکای منطقه‌ای در حال یدک‌کشی است. ادعای کذب سپاه پاسداران، نمونه‌ای دیگر از دروغ‌پردازی‌ها و تلاش‌های این نهاد برای ارعاب و ایجاد مانع در مسیر تردد کشتی‌های تجاری در این تنگه(هرمز) است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71645" target="_blank">📅 23:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71644">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دیروز در بروجرد گروهی از معتادا در اعتراض به شرایط بد کمپ از اونجا فرار کردن و با این کار انعطاف و آمادگی بدنی بالای خودشونو نشون دادن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71644" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71643">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71643" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71642">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">یه گروه همفکری بت زدیم مخصوص دوستان بت باز
😂
✅
https://t.me/+6XLorNFkXGgzNmE0</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71642" target="_blank">📅 23:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71641">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFMfIqxVh6Vk_PzOYUXxmwsyThhSRDmkoeslyHT90vWZDjWslQdY96WJxfLIXzzjIrIIjkAPPl89WYhCTsd8jSTZyxqMEMozlozei2UnMd_YjVft0evyJ5YwrwS5chOO8yoPED97RSuBOaYPfcSg-tZxlFUeNsYVZAR81LzM3-YvcuR62JdskPpDvphWft7GvAmwTYY6tfw6AU9MtTB1rjCZun7ppzCuVAzpxsagZToDD9Gh6mwUc3sb0Vnls4JbhFBzd9pbf-zrDaxKX8DRoEGkS8T8w4OSWsmo7hKLOeYfGRaJyhgHgAfPT9tkvlgs664Puk0Yc5VJ6-CSodBsZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
نفت‌کش غول‌پیکر «ال‌گایا» (EL GAIA) هنگام تلاش برای عبور از یک «منطقه ممنوعه» در جنوب تنگه هرمز، با یک مین دریایی برخورد کرده است.
تلاش‌ها برای مهار آتش بی‌نتیجه ماند و تمام بدنه نفت‌کش در شعله‌های آتش می‌سوزد.
سپاه پاسداران اعلام کرد که پیش‌تر درباره خطرات این مسیر غیرقانونی هشدار داده بود و تأکید کرد که تنگه هرمز «همچنان بسته و تحت کنترل هوشمند ماست.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71641" target="_blank">📅 22:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71640">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d776b60914.mp4?token=HUoTSjCpUM5k8BcDR05fTGKA3fssU9cRDIYS0Oqi-uru55Pg8RSuIVDVbuMO7jNFUUjZqMJ68YSSpSsKQMszlpK9HcW0EQzUvMxIUC8Y_yfyI_BAKHMYshLsCiIN5PDiu9ZhZfTybX52KNi1mTp5MDAqu2HshFbdZXVC9TfoxLq3ZpibsDdr0qnaX0xI9o6LtCWGoUSZtWNcqxQpIs1DnCxJ4fmDVMqYJ2LGY1pT9IwoFvFS0fK9bSZrwZKXVMBNbhjS5zi3BMT5x9rCFW2r8PpTQwgLdGrL_6hVV2JhuISojH52BEd1woI_X9BahzuP9ZC-MqpOlguFcYkjB9XQAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d776b60914.mp4?token=HUoTSjCpUM5k8BcDR05fTGKA3fssU9cRDIYS0Oqi-uru55Pg8RSuIVDVbuMO7jNFUUjZqMJ68YSSpSsKQMszlpK9HcW0EQzUvMxIUC8Y_yfyI_BAKHMYshLsCiIN5PDiu9ZhZfTybX52KNi1mTp5MDAqu2HshFbdZXVC9TfoxLq3ZpibsDdr0qnaX0xI9o6LtCWGoUSZtWNcqxQpIs1DnCxJ4fmDVMqYJ2LGY1pT9IwoFvFS0fK9bSZrwZKXVMBNbhjS5zi3BMT5x9rCFW2r8PpTQwgLdGrL_6hVV2JhuISojH52BEd1woI_X9BahzuP9ZC-MqpOlguFcYkjB9XQAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای یه آخوند درباره سرگرمی های روزمره :
سودوکو بازی نکنید اعدادی که کنار هم قرار میگیرن یه رمزه یه چیز نهفته رو آزاد میکنه
فضای سیاه سفید تخته و شطرنج هم شدیدا جذب کننده اجنه هستش
🎙
مجری:
اونوقت بگو هیچی بازی نکنیم دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71640" target="_blank">📅 22:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71636">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/dYx4x7ZwYVhMuxnP43mh7iZvpZDtLhGei2Cl9Lh-qgvXQ2g6-1Nvku-LLGBEMCEC0BH61WTqt9erqobdKV71hY0SH_QaRyQBKvL9yj2Ccj0Kx1WUShXOiE7qOxUBZgbVWV3iqCw1_-rftmhseLr9S2MoL6s6hhrPwI1ZiJPCN-l0aFDzJlRr9OqCcYIHvF_nhRRApf3gW3ewCaLsM7E8vp8mKW1rcBV9GrjfkTTBFFYTD05GEyMbjexEaVHJ7tcq3-l8O9b-_x3iuSgfUKYG4_r1f5BnmFCx-V6dbRIpONziXXpSWMSKC_4yShmnw-gsjeLaTtxCqMwuvBDplfXpZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/JPhKkjTXfZIbhG2cKQxiHbcZjva_iGsstFj29XAA-_Pb99rXy1Wq3-eIKcB1TTCWoGweNJeSLHevJWzPay9qllIPhqL9r9_QPgYFHwzthmpoYoyAjPVyJaBSvL51p2sMxcwyRwzEUDirL22vBGKPucX-jEJXzn3o1FUftwcOMqXNiBuPDqSdxMvJLj52VvY4XzpG3sqsrXKevTcgXY6yweFUkkNz6nzOeQI33YHCwBebHfEt5gsH76eYkhCfliUJKQQE4nQc1VwXBbdQOptmNDjdDB3qB0FieVO-K0C1ro1PQZzXpRYJo3JX5szQQrhfbegHuraWU7sF_ywgqBMp0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیامکی که داره برای مردم ارسال میشه، از فردا رسما جانفداها برای شرکت در دوره‌های نظامی و امدادی، اعزام میشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71636" target="_blank">📅 22:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71635">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22f9266483.mp4?token=mDx_RKOF41CsM5LE8njlbVUnIz-yyVsVpNN0kZC-ewsdnhUCsDkjmcLgAoZ58Y9sjVEdeWwX409D20M70mlheWTxp-riNzMUxe7-VntM1nCJe9oxARglC6oQWYBxIvngZuM-TKOMtwhxT1mZqI8zW1agNO5qDsuq5V9X0A4sP4pWOIgzDfNU_PCl23v76yOlN3hypUHdPissvGlGzILDTsFkh4P2PJWwGrrrzLlzUmSXf7Z5Npnp_FHtMdMNl-26bmES-CwBDQ8RDQm77FjOp1BMQ0G-xnb0fkYTbVlmPpY9OG9luQNs8XLis5tEnIiOAs1aHvAK0ZiUIf6tYOrt6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22f9266483.mp4?token=mDx_RKOF41CsM5LE8njlbVUnIz-yyVsVpNN0kZC-ewsdnhUCsDkjmcLgAoZ58Y9sjVEdeWwX409D20M70mlheWTxp-riNzMUxe7-VntM1nCJe9oxARglC6oQWYBxIvngZuM-TKOMtwhxT1mZqI8zW1agNO5qDsuq5V9X0A4sP4pWOIgzDfNU_PCl23v76yOlN3hypUHdPissvGlGzILDTsFkh4P2PJWwGrrrzLlzUmSXf7Z5Npnp_FHtMdMNl-26bmES-CwBDQ8RDQm77FjOp1BMQ0G-xnb0fkYTbVlmPpY9OG9luQNs8XLis5tEnIiOAs1aHvAK0ZiUIf6tYOrt6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
سیاست ما روشن است: ما به نابودی زیرساخت‌های تروریستی در «منطقه امنیتی» لبنان و رفع هرگونه تهدید علیه دولت اسرائیل ادامه خواهیم داد.
به دشمنانمان می‌گویم: اگر تا به حال درس نگرفته‌اید و تصمیم دارید دوباره به ما حمله کنید، ضربات سنگین‌تری متحمل خواهید شد.
هنوز کارهای ناتمامی باقی مانده است و به یاری خداوند، آن‌ها را به سرانجام خواهیم رساند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71635" target="_blank">📅 22:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71634">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoEqI0kZb7cgQfcT6y0RZ_VU0cfe0qfdHmjfzZWqEmp3DpZ2HUXR_hnMceRbyTZrmFL7cd9f6e1h1DOK-rZ0QCwb68zEYb_BLz79cbZTXFr_oZIym_VYks15qHqcpDaFBTnC0zgpdsQ3LP0zXNPP4ezTWFQ3AsKeh3y-o6y4ct0gHPb3AEOemQm_04KBKROsdw0iRYZXXNa8UPxGcWdMM7V5--2u96NK2ulyWgwv2D9xvoQortaULXTL_YaFuflnTM9Ck9RoPCWLynDpnprSWrRxoNCBR1BKeSRPa8yaGbTa7sFn5bbGBibzMEBbaXADsZ430fVxR8-3AAuWuBR3DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
❌
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
وزارت خزانه‌داری «عملیات طرد اقتصادی» (Operation Economic Outcast) را با هدف قطع تمامی شریان‌های حیاتی مالی رژیم ایران و حامیان آن آغاز کرده است. به همین دلیل، من فراخوان جدیدی صادر کردم تا افشاگران اطلاعات خود را درباره کسانی که اقدامات تروریستی ایران را تسهیل می‌کنند، ارائه دهند.
خطاب به هر کسی در سراسر جهان که اطلاعاتی درباره این شریان‌های مالی دارد: این فرصت شماست. اگر اطلاعاتی قابل‌استفاده برای وزارت خزانه‌داری دارید، ممکن است واجد شرایط دریافت پاداش باشید؛ فارغ از اینکه کجا زندگی می‌کنید یا چه کسی حقوق شما را پرداخت می‌کند. اگر چیزی دیدید، اطلاع دهید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71634" target="_blank">📅 21:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71633">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGLyEU0nU40WY_h8W1IIZBIiRk3Fh4aZjWJbhSZuGi7Cu537J2ra_94sP_ddhnLdumywNsj-7SdU2LcbeVdsYs_KaXMOQSudFLGyT2yQ8HYXuaoJjv-M4F8WgCwrmImuKdf8m-0s5a8jkKygZwBPs9QmbLxDZQhguTLWfYbXDUov-LvTSsJVAP2YXKqyxLGvriYptiwQ_mInmiGQx89jvF-oF5NAU5S_SixesE0D4-Br5fSNIsTj61PEwvHToU1RAV4aH0WLcndvxAAtlSXhGofkE1mv1doEwusfNBJH7LTtyhvCZBsg04BLQx3stujGSiGkV1OqSDvOd3xHavpT6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
نفت در حال عبور از تنگه هرمز است.
کشورهای جهان — که هیچ‌گونه کمکی به ما نکرده‌اند — باید پس از پایان یافتن این غائله و فتنه‌انگیزیِ ساختگی، هزینه‌های ایالات متحده آمریکا را جبران کنند؛ و قطعاً چنین خواهند کرد.
ما این کار را بسیار بیشتر به خاطر دیگران انجام می‌دهیم تا به خاطر خودمان، و نسل‌هاست که چنین رویه‌ای داشته‌ایم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71633" target="_blank">📅 20:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71632">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZWQ2FIieEEuRc-EFEO0eZp-CNl9tzl6lDmvbixq_06FIjujf2Uu8Jyh6hXKRXhwzbSWDzZYdvWcBDZzINckczmpHJUzl0wk-WzTqHqtdTvNfP6UBCcm_wWPxQp-bf-sOMNbUeK4B2qQQZ_sRTUlt7OegNAqnLmqOoSwiQDqBY7gFUdCvGzu9pigQDMh43lltf83MWljeLa0dLQ66kFXTR7X29Id_zxrB9cC-NMsFSsvYDW1P4lfCU0izunpw_8FG_9nA9659K6ZYDHZyzucGQ3s44vzmUSrGEsopbdwkoyEEABub41EisAUKM5sz6HAEtcIMsCk8B34Lr40UJzRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
امیدوارم همه متوجه باشند که افزایش قیمت‌ها در سراسر آمریکا ناشی از عملکرد «جو بایدنِ خواب‌آلود» و دولت او بوده است، نه «ترامپ».
حتی قیمت نفت در دوران بایدن بالاتر از سطح فعلی بود، حال آنکه ما مانع از دستیابی ایران به سلاح هسته‌ای شده بودیم!
به‌جز نفت که فعلاً وضعیتی متفاوت دارد، قیمت‌ها به‌شدت در حال کاهش هستند؛ قیمت نفت نیز به‌محض پایان یافتن درگیری نظامی با ایران — که زمان زیادی هم تا آن نمانده — به‌شدت سقوط خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71632" target="_blank">📅 20:08 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71631">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGGH7USwrHKdW4LQDhe8xt7kw00Cb1LUEXxzLGl8HRxpsZ8eQbQYmZLdg8jXumkiiJP5uWRf-EcmHSedaMmDojI2YtQtCClgn-0VXMqvWq9j2nGZjdl5jOiRSe6-kmJKqzPlR3ofydHK5X6GWJQALKeVcKkNLel-oSATk6gruamuAlScqIcLH46O2bu591SnCODEEYO4Yem0v9XDIkzokCp85zxdM_eoEWkYAjRJxNnaq7cqE4Tg1yuqKj75GFefinHizUMDf3ro8ubFonW8GTn2vjRuq7ad_9xP7zsdFtcTv2MNbpDDFj5hsI_2--1t2wub4ok60eorIgNn_FOrQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
من به تازگی گزارشی دریافت کرده‌ام مبنی بر اینکه ایالات متحده بیش از هر زمان دیگری در تاریخ خود، سلاح‌های نفیس و ویژه تولید می‌کند.
این سلاح‌ها روزانه به نیروهای ما در خاورمیانه و فراتر از آن تحویل داده می‌شوند. کارخانه‌های شرکت دفاعی ما به صورت شبانه‌روزی در حال فعالیت هستند و همزمان به طور متوسط هر کدام ۴ تا ۵ کارخانه جدید در مقیاس بزرگ می‌سازند!
تمرکز اصلی این تولید بر روی پاتریوت‌ها، سیستم‌های THAAD، تاماهاوک‌ها و سایر سیستم‌های موشکی استاندارد بوده است که ما در حال حاضر تعداد زیادی از آنها را در انبار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71631" target="_blank">📅 20:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71630">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
تسنیم:
ایران بارها اعلام کرده است که به دنبال مذاکره برای رسیدن به توافقی با دولت ایالات متحده نیست.
ترامپ همچنان ادعاهای نادرستی درباره توافقی با ایران مطرح می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71630" target="_blank">📅 19:58 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71629">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:  «ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد. این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.  @News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71629" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71628">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wwk8WVNvwAg3lQg6vx3BKnKQNhd0mJRvIZ5rNej-wHwLgu_cpiIzKL3VGkpUUQg73R_JZXbXd6KJ79nSfHMgbc0Lo54dSuZPWrZ27enssufWwQplaT0RDNtaruXsiOq3AvaOMO2d_MyUVdBxqCP-NU3NmQCmR8clyC-uXlJNB1Uny3KNfIwOEUxp41OCcGuLdkCOYAEr01Om8K8b_ul3ndrxo15sq7zzXUnZGcwREoX6sfdEOMzMCmrFgstveN6c1OmjnX7tgeqikVZaAka1i7HqASnkKw0TEwwqL414KNTjQl8kl5hRitt9n4fSmSVXjVwmeVzO6__b6tzdi_Bgag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
«ایرانِ در حال فروپاشی، می‌خواهد هرچه سریع‌تر و به‌شدت به یک توافق برسد.
این من هستم که تصمیم می‌گیرم آیا آمریکا وارد این تعامل شود یا نه؛ البته ما در اصل، با چنین ایده‌ای مخالفتی نداریم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71628" target="_blank">📅 19:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71627">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=jn6CPvg3ceYv8G6x7Vm8Dth1Itq_kToEa7s29SmxF4mYxoiQWqsZgjGl_F3DZutm6QI4tA584DJJHEckIN1aWRXQ5bs0KF6ZzgkDuCYFnmXDcDCa7gQQMa-iVtIPzCZ7njca3crlXs--QNdz32ia9lilb_XF26Oks-0XOXkmEbocwvvZ-aPEOh_ujTgInDuoQHbUrwsfLMCw9qf7pstnYsVbq-ie0lcg909KF4ycrUyZYDnwgh12NJzxe7njrKvz4WRXQYj42HpuYRhqsa4-gHqsHs9VpC66QhaKghIlqT663Ms9gU5qk3ZifVPzJC3yVin7L4TzPl_lpt_ofhImZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7f7efeeca0.mp4?token=jn6CPvg3ceYv8G6x7Vm8Dth1Itq_kToEa7s29SmxF4mYxoiQWqsZgjGl_F3DZutm6QI4tA584DJJHEckIN1aWRXQ5bs0KF6ZzgkDuCYFnmXDcDCa7gQQMa-iVtIPzCZ7njca3crlXs--QNdz32ia9lilb_XF26Oks-0XOXkmEbocwvvZ-aPEOh_ujTgInDuoQHbUrwsfLMCw9qf7pstnYsVbq-ie0lcg909KF4ycrUyZYDnwgh12NJzxe7njrKvz4WRXQYj42HpuYRhqsa4-gHqsHs9VpC66QhaKghIlqT663Ms9gU5qk3ZifVPzJC3yVin7L4TzPl_lpt_ofhImZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ رفته ایرلند و چپای ایرلند هم برای اعتراض این حرکتو زدن؛
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71627" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71626">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71626" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71626" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71625">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RubBiyKbbsm1wahkQwM_97btBDA8XRTUrysg67r78tpQXDCmQRfWsZPrIidfY9CsJM4KW6syGRWoxB2c0Jj2eTYV7ZC834qb5MLMvid-hIHQbBTsf4xGF7oUrz0kv2iU0e3aG6mSghAWSAzPjhi1p7YN23pQJYGIlrvq52oad-PuNZ8kOVm9Wul6UOIxHPujQCV9IGpmMJ07Tzg-iQWcKoD6H9OTXgDIicuFUlqXzA6DAtugLd9SYqxyHW-5qzz42IyiYtPxs8JGu-exVcJilgU0a2kRoZOpDxVUuj4A7fn4isiUonhCI5HYisKH1QChJOgAYwnYMfK2rWUqB93XMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
شب بزرگ فوتبال آسیا !
نبرد هیجان انگیز
⚽️
السد
🆚
استقلال
⚽️
را در
TrexBet
پیش‌‌بینی کنید!
📉
نگاهی به ۵ تقابل دو تیم باهم:
⚽️
السد: ۲ برد، ۳ تساوی و ۱۰ گل زده
⚽️
استقلال: ۳ تساوی، ۲ شکست و ۶ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71625" target="_blank">📅 19:04 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71624">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TXnDfTAOrlwbghPFNH32N9CJnjxFiMhRIqjMop_90G4PQUtOIADN3o-gzAWbkdm5XeeYgpJNhU9Lvftk56ACf5dGm6LP7mpKkWaK05IaEF3G2Doezlw0hoYLxq7wf26mJdYmibN5SCH9OMOpR5qDfGt0cXOJUeHFXVP8CZkm-As-uOg_uF_Rcn7LjMSu6GsE5XMP_wxYMFZN1P5mVNSKSHYDo5gzsdxzocMuDpb2s4yVLhoKnEH54tiGhaJ_SdDpY-nBcAHrf-bGPkgrTWFNXLfRif5cu4bLWv_Aga9wJkisBh9XSnWUe96WZBIRCGdC_Iq60fynLfJiqeiyHLRZZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
اوکراین موافقت کرده است که به تأسیسات انرژی روسیه حمله نکند؛ روسیه نیز متعهد شده است که همین کار را انجام دهد!
افزایش قیمت جهانی گازوئیل عمدتاً ناشی از جنگ روسیه و اوکراین است، نه ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71624" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71623">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
دقایقی پیش چندین انفجار سنگین در چابهار سیستان و بلوچستان رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71623" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71622">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
ویدیویی از عملیات نجات افسر تسلیحات ملقب به "براوو Bravo"(زیرنویس فارسی)
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71622" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71621">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEUksD9cshhepjcdNw6QRN6U5MV-ObqWcHD9i4ohbCiNvEUmla-ppPoI_eVW2rdN1-xSFE0WvjHYHweWlKECQ-wf2qC01BWbFYChYsZWXP7OExjpM4L5qeJBVYjDxRbylFoDUkNeioQQdlSXFmpP5MQjtT8csk0hQFOyVYNnpnStdXQvpyq0jLso6BDlRgXHXhM7odOPgq3xoAgtQEyVmOsZqQTmAk6rkDtIH9rIG8o2y2GSOsU10xxfdpdrP02PCROfzG6Eu_zypenpCJwoKT_NVqH_1mm20SVVyTPl9VfUDil7PC-cb1BZM2D83Osp_MFN9-em9qmImD4euPsntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو هفته آینده برای سخنرانی در مجمع عمومی سازمان ملل در نیویورک خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71621" target="_blank">📅 17:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71620">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=PhgqC4JauKivJWpjlhScFk4ohO_jHY3eDbhmtbeKa18uDfv4ghM9yX9LqwX5HbKiJshpTKCLjA3tBPkoK_Zbz8rhGj96qbzekvNbzXVhJhe-GZllDkEVHPICyCCrnEDV-QxNacDD7RQeToDgIFaiCqqFaDVkiMBbW56yUkeu0wl93R5pSUt4_w9v5s2iY65bYc8gvY5DNGvVWHlOc0xfzuARbQlpnMktueQtQGpk4jtd2NfAE-Cgk9dLaUUeF8XrEShNWKvjCWTlWXAFHxrL0kxhugKY55-jrfb95dcCdfYFdnAKflpDiaJvRIYBLOw4pU-3Xae9f9pUGnTmahPRSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36d8765cb4.mp4?token=PhgqC4JauKivJWpjlhScFk4ohO_jHY3eDbhmtbeKa18uDfv4ghM9yX9LqwX5HbKiJshpTKCLjA3tBPkoK_Zbz8rhGj96qbzekvNbzXVhJhe-GZllDkEVHPICyCCrnEDV-QxNacDD7RQeToDgIFaiCqqFaDVkiMBbW56yUkeu0wl93R5pSUt4_w9v5s2iY65bYc8gvY5DNGvVWHlOc0xfzuARbQlpnMktueQtQGpk4jtd2NfAE-Cgk9dLaUUeF8XrEShNWKvjCWTlWXAFHxrL0kxhugKY55-jrfb95dcCdfYFdnAKflpDiaJvRIYBLOw4pU-3Xae9f9pUGnTmahPRSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
یک پهپاد روسی «گران» (Geran) در بخشی از جاده در شهر «پاولوگراد» که مملو از خودروهای غیرنظامیان بود، سقوط کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71620" target="_blank">📅 17:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71619">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=lq_IpqkOss5SokCPUKPqDRrc0_bCDbB1u7ljr869xAc_eDEEhGK77ZqsOMAAFfY_lYNpe94A765EnS2D0Q0gomK4bHs28bg4hvSnwBnLo4MpnsvKzc9TDYzfalCmzUTEE__UrnozLNkwBb-lYQk5X08Oa-opFlXRpTzVJfySTwX0kwyOr73hVkb1kOt69DilY8pDD12d25m-vdZonsV_fNWCxK9syoQN4M6tzKWmWF4pWjEBdxGx824OI1O73ndha5Yx8xgL25aoiN8Rx-ruwAN--GhxAjg_wbI2wAQKcUOihUlkldPhUcf6LbvP2WJLCOYBZpokdQhwn1P6WEARKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00f9fc5142.mp4?token=lq_IpqkOss5SokCPUKPqDRrc0_bCDbB1u7ljr869xAc_eDEEhGK77ZqsOMAAFfY_lYNpe94A765EnS2D0Q0gomK4bHs28bg4hvSnwBnLo4MpnsvKzc9TDYzfalCmzUTEE__UrnozLNkwBb-lYQk5X08Oa-opFlXRpTzVJfySTwX0kwyOr73hVkb1kOt69DilY8pDD12d25m-vdZonsV_fNWCxK9syoQN4M6tzKWmWF4pWjEBdxGx824OI1O73ndha5Yx8xgL25aoiN8Rx-ruwAN--GhxAjg_wbI2wAQKcUOihUlkldPhUcf6LbvP2WJLCOYBZpokdQhwn1P6WEARKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
برگزاری این کنسرت خیابونی مختلط توی کیش باعث شده صدای طرفداران حکومت در بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71619" target="_blank">📅 16:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71618">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=oOLiTO7Z-QVpL7cFtSwMTIqIelDUA5zssPdN01cu9HnHSqYm4KU-9UhUI83-b68IKMuolc2ymEs0X6ZnZkEI56OZlYcZGjT4dkKCCis_wxA16SYr5OXaUjOJ6kC6r_yGcCS8mcBtcbHbtDowq__C7WacU0_llCpx05B2A7bsO7BNcNOS7TUIi2M0lmEz95tOmjSNijd3nKE5x7ER0J8Lfw9KdwITdKXJI-Gg9hcT78f_UexHx1rjLSqHR_3GlfStuT0gJbd4flZaKILP-NZm4LfVZwXx5VjktRY6FF5uIUw67otA0M26tOehCBM1Jq8oV732F8gxibbiVULrMWfFLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9cbffc3d5.mp4?token=oOLiTO7Z-QVpL7cFtSwMTIqIelDUA5zssPdN01cu9HnHSqYm4KU-9UhUI83-b68IKMuolc2ymEs0X6ZnZkEI56OZlYcZGjT4dkKCCis_wxA16SYr5OXaUjOJ6kC6r_yGcCS8mcBtcbHbtDowq__C7WacU0_llCpx05B2A7bsO7BNcNOS7TUIi2M0lmEz95tOmjSNijd3nKE5x7ER0J8Lfw9KdwITdKXJI-Gg9hcT78f_UexHx1rjLSqHR_3GlfStuT0gJbd4flZaKILP-NZm4LfVZwXx5VjktRY6FF5uIUw67otA0M26tOehCBM1Jq8oV732F8gxibbiVULrMWfFLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ و بی‌بی ترسیدن نکنید اقا
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71618" target="_blank">📅 16:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71617">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=EPqlVOlKxFCHEGT8gay5vFY_pLnhOalp1QW2q5Z0n3t58GvyhgylwSTDZUDxSxU4zUZgU0t4z-pfuxl1Pit0ckKDzB9alT5yAygIunnxOzzbCmI6dRu1cT3rXK_mUxpqkFAVOPcdvLrdXf6zwur8DzLcOTci4fKUkBL8Sxju8MaRmJeoiiDxNxwah8uyWY_mwzopNXdpiGCFkMsm2xovVnhyX5aJvHOYYKPPdd1VOOzQse6Ye3MeGPO4EC8wMVZOKvsoviBZkHIoFwwAy_HDo_Z4lTjYETCrImbprnQZ0E7QLdCGNRLTuIaUBTwDSNmlJipn0JkuSHtkKsqPc3Ye9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2eadd25c0f.mp4?token=EPqlVOlKxFCHEGT8gay5vFY_pLnhOalp1QW2q5Z0n3t58GvyhgylwSTDZUDxSxU4zUZgU0t4z-pfuxl1Pit0ckKDzB9alT5yAygIunnxOzzbCmI6dRu1cT3rXK_mUxpqkFAVOPcdvLrdXf6zwur8DzLcOTci4fKUkBL8Sxju8MaRmJeoiiDxNxwah8uyWY_mwzopNXdpiGCFkMsm2xovVnhyX5aJvHOYYKPPdd1VOOzQse6Ye3MeGPO4EC8wMVZOKvsoviBZkHIoFwwAy_HDo_Z4lTjYETCrImbprnQZ0E7QLdCGNRLTuIaUBTwDSNmlJipn0JkuSHtkKsqPc3Ye9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سرقت آیفون ۱۷ پرو ، در کسری از ثانیه در کافه ای در اندرزگو تهران
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71617" target="_blank">📅 15:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71616">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=CxDyQ4OytWVI5gIe8k3Hg_eLfpDINhyVU2Fz6QNnekpTFV7qZs_A4Pri5zL0Iz7xnVZxQPWOyP8BMS08Orm3dDYU9kMmCjQPfhy-b3iM5HefiGdF0xKtLRssWJjrYhniHzvbsGCZ8Etd1_cmxbnVvFHNsRM1CYyfHxI6vXoCeatlXDjhQHDR0L8hE-tsGnQUcCqJ5AfIqWI2nkVCk8S4rCu_duj4BOx3tOgvnVcTq4R4qbW8d9QjLJODQmjLiIOU8Z6uFQXFG62_hwLfFok_vzF3bjEqf4wn1g0euhXPyfBpml0r6DHLiJ0SkEFEdoppz0WtTIFEZbU0TIHOVKRIVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4caee63fca.mp4?token=CxDyQ4OytWVI5gIe8k3Hg_eLfpDINhyVU2Fz6QNnekpTFV7qZs_A4Pri5zL0Iz7xnVZxQPWOyP8BMS08Orm3dDYU9kMmCjQPfhy-b3iM5HefiGdF0xKtLRssWJjrYhniHzvbsGCZ8Etd1_cmxbnVvFHNsRM1CYyfHxI6vXoCeatlXDjhQHDR0L8hE-tsGnQUcCqJ5AfIqWI2nkVCk8S4rCu_duj4BOx3tOgvnVcTq4R4qbW8d9QjLJODQmjLiIOU8Z6uFQXFG62_hwLfFok_vzF3bjEqf4wn1g0euhXPyfBpml0r6DHLiJ0SkEFEdoppz0WtTIFEZbU0TIHOVKRIVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
در ۴۵ روز گذشته، ۹ آتشفشان فوران کرده؛ انگار در جهان، یک تغییر بزرگ در جریانه
!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71616" target="_blank">📅 15:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71615">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=HeJhysYL0qb6Mf4IuhQbceLtcuoVD0pPuQUnoj9UCFb5Md_MHiI9_aHbjDNLMSWmkqTvPfgAe4I17cuZnn_Qwdy-b4Pq2_kCnKW2c9-x9EyR_L4gHX3HTqW1omhgPNOV1d0yQrbBZ6DbqW34MWcwmTH3GketpiqT1_43ZljqxeR_b-9TLmiO5y9Wmb3MfwWpb3vxLq6wY9EZEbNFh2hgv0SetQXhxtnfAX-ISWZbp_-DWKZarwsWzJLDyO-iO2G9nbnIFY-1-KNMA_Y8t14LUg_QYZtwuBQjvxC4RqVtzvLTpGantNvjOkoW-gSN2U0xK00Ss4r1rJlvrZBv2lh3JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c7aec3e1c.mp4?token=HeJhysYL0qb6Mf4IuhQbceLtcuoVD0pPuQUnoj9UCFb5Md_MHiI9_aHbjDNLMSWmkqTvPfgAe4I17cuZnn_Qwdy-b4Pq2_kCnKW2c9-x9EyR_L4gHX3HTqW1omhgPNOV1d0yQrbBZ6DbqW34MWcwmTH3GketpiqT1_43ZljqxeR_b-9TLmiO5y9Wmb3MfwWpb3vxLq6wY9EZEbNFh2hgv0SetQXhxtnfAX-ISWZbp_-DWKZarwsWzJLDyO-iO2G9nbnIFY-1-KNMA_Y8t14LUg_QYZtwuBQjvxC4RqVtzvLTpGantNvjOkoW-gSN2U0xK00Ss4r1rJlvrZBv2lh3JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رادان:
ما امروز از قبل از جنگ هم آماده‌تریم!
تو حوزه مرزبانی، انتظامی و خدماتی آماده‌تریم.
با امنیت مردم شوخی نداریم، ما شرایط‌مون جنگیه، اگه وطن‌فروشی به دعوت دشمن بخواد ناامنی ایجاد بکنه، ما اون رو مثل دشمن می‌بینیم و باهاشون برخوردی رو می‌کنیم که دارن با دشمن برخورد میکنن.
دشمن میخواست چهارشنبه آخر سال 1404، همون مدل دیِ 1404 رو راه بندازه ولی حضور مردم تو صحنه، متوقفش کرد.
مردم ما فریب دشمن رو نمیخورن، 30 میلیون جان‌فدا داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71615" target="_blank">📅 14:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71614">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgXxCwDY_pur76FFXze3KAHiUD080BWrayoU-Ycl68jSU8wfQMIWE6JWZfPG3bXyD0aEjQDNXfblulGorlW4crhGoGYR_ouwHDHgRcBm45DXZYirvrzHxKpDPJLXnfsiODxf3k13puPtkP1c_abbBZjzb2iQVyaHw7xlIOTZ-PwQ6FAgZmgdC4ULKItyKwFcKerV-Zn6u3l3BYvWYxY7CJRzEVueo98SKCUATnWJL8hCmOE501El2hHuy0Yt0ycnktRuFD1V46PD0oP-ZbeJvPmtM48QwZ-j2Px8uukJv8rOf6-NKqfIMfXflqUOK9x_Z06GTfBpLh7Xwq3KZY1j2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖥
🇮🇷
🇺🇸
بلومبرگ:
پس از آنکه اتریش تحت فشار دولت ترامپ از ورود محمد اسلامی، رئیس سازمان انرژی اتمی ایران، به این کشور جلوگیری کرد، حضور او در کنفرانس عمومی آژانس بین‌المللی انرژی اتمی در وین منتفی شد.
قرار بود اسلامی روز دوشنبه در این کنفرانس سخنرانی کند؛ اکنون احتمال دارد نماینده‌ای دیگر از ایران در اواخر هفته به جای او سخنرانی نماید.
انتظار می‌رود کریس رایت، وزیر انرژی آمریکا، در این کنفرانس ضمن تأکید بر اینکه «ایران هرگز نباید به سلاح هسته‌ای دست یابد یا آن را تولید کند»، خواستار همکاری کامل ایران با آژانس و دسترسی بازرسان آن شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71614" target="_blank">📅 13:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71613">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=KgOf9KhhOJrskU8WDOoZ6EgGYa_UCEZp_5B9kCdPYrhWD5iTfnoEIO_kRkH18ogBi4mfDQrUUv1P0cS-UlnvgLGPae1PkA0I_aitXLI62Msoockusih1sVhTgnMSU0cXrVOZ_lf6oj78itSvIFsLEq_-sAOleWFDIajVao22RF2umSGnRJvudlXabLIvnBYYYvnDDuqv5gAjAblrxNZMdBC03vC4STEpbvurbe6aRToo1hokjzvA__iTKy8W202ipIs2wRFVk1Xfwq73cc_usgZWxAfW0N3CNpmWLDnMHCYTHRUkxe5xGD-sv8drZAd5KhjQpkKi2xhAnMbx524V9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ec91c05b9.mp4?token=KgOf9KhhOJrskU8WDOoZ6EgGYa_UCEZp_5B9kCdPYrhWD5iTfnoEIO_kRkH18ogBi4mfDQrUUv1P0cS-UlnvgLGPae1PkA0I_aitXLI62Msoockusih1sVhTgnMSU0cXrVOZ_lf6oj78itSvIFsLEq_-sAOleWFDIajVao22RF2umSGnRJvudlXabLIvnBYYYvnDDuqv5gAjAblrxNZMdBC03vC4STEpbvurbe6aRToo1hokjzvA__iTKy8W202ipIs2wRFVk1Xfwq73cc_usgZWxAfW0N3CNpmWLDnMHCYTHRUkxe5xGD-sv8drZAd5KhjQpkKi2xhAnMbx524V9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇳
سخنگوی وزارت امور خارجه هند در جریان سخنرانی مسعود پزشکیان در اجلاس بریکس در دهلی نو، با خوردن یک‌نفسِ یک ظرف آجیل — شامل خوردن، لیسیدن انگشتان و برداشتن دوباره از ظرف تا زمانی که کارکنان تشریفات آن را گرفتند خبرساز شد
😏
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71613" target="_blank">📅 13:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71612">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567356c89d.mp4?token=RlDl4gq8AopXi55-6CLcGOd3pJkJi9VHn0ZqyuS1FcEOkrPpNNShgG5Ve-SKgOiIcHh01PdcUWh-XfcmQ5_-nbf05LeooeBn71J6Q8Hvy4g-HU_SM-LvTkU8MoRTgWmaEvSjxsSZ7oF0OuaL-r-yissnUO4z_HrLpnb9LJWYA8pq3EF8aM1VJmnqvDU5L5FbJa43y-p5ZmuUUUCSkJSZzjQQMcWj6mvKeoU2ptR2p7fs5NhkfYYTMtYxpvwv9m2yg1MqkHybEP3Qq3p5NZtquL9_VxHEJmCTJBgoudkZQoQZHg8cyZywrcyD2aEYcJJhdoaQ7X-0rComRxmyJ5AtHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567356c89d.mp4?token=RlDl4gq8AopXi55-6CLcGOd3pJkJi9VHn0ZqyuS1FcEOkrPpNNShgG5Ve-SKgOiIcHh01PdcUWh-XfcmQ5_-nbf05LeooeBn71J6Q8Hvy4g-HU_SM-LvTkU8MoRTgWmaEvSjxsSZ7oF0OuaL-r-yissnUO4z_HrLpnb9LJWYA8pq3EF8aM1VJmnqvDU5L5FbJa43y-p5ZmuUUUCSkJSZzjQQMcWj6mvKeoU2ptR2p7fs5NhkfYYTMtYxpvwv9m2yg1MqkHybEP3Qq3p5NZtquL9_VxHEJmCTJBgoudkZQoQZHg8cyZywrcyD2aEYcJJhdoaQ7X-0rComRxmyJ5AtHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه جمهوری اسلامی:
توافق میان ایران و عمان حاصل هفته‌ها مذاکرات فشرده است و حقوق حاکمیتی هر دو کشور را به‌طور کامل محترم می‌شمارد.
از کشورهای همسایه انتظار می‌رود اختلافات گذشته را کنار بگذارند، برای تقویت امنیت منطقه‌ای گفتگو کنند و نفوذ بازیگران مخرب فرامنطقه‌ای را محدود سازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71612" target="_blank">📅 12:48 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71611">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/COaqfo_wFTRbSghpH3I7DwL5FNLbRopvXWZ9VpvCdTY1nML0d0oOzdBzAVGS1WPqtSs_A26gMjAyV324UPBFwfeo-Yj8yG3qtfuPJWJUeyVi-BYwp_Fzi18RGp3C-C71JY40wXjIn3fSUH9Gcdra1UPcD1qrLYjJ3Zneej8TGqHuEFpuTWFuUjiNR6gz1zis1-3-y1D3Nh1gjsMhlCp81zpuFb3mjJv2IEmYMcdzaQcOh5hDQSmRbyHmyHj5A8TNpuPbnmSbvW37M-lcNM03p9FSCalmJQd2vxbbtqUpCyQXY-wFveWirXEkALd7ZIRLWNkXzX3e_0Rtrf58GXv6jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه دختر شماره یه پسرو که روش کراش داشته داده رفیقش، و رفیقش تو نیم ساعت این اطلاعات رو از پسره درآورده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71611" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71610">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71610" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/71610" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71609">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfzTduGw_m4VPALCGwxzOUYPn5OdEdrpJUR5uq-xdmrD6T--ZU7EmPYC9Tuz7dArGAHbPlrzi5yJ15pcGnXN9geYW1hUzRwUeR81lE0Erf5VB77NMOBrmv_VxMDT_smPnZDv79k1v2zDJ53ZqIGQTy5yOQcOIPtICK2giil8tyRfKzyW7aiSobTcNqKAHyUsMhQBEHXD14xkjmq6zRHGg2deKAXr1sms-8MbgH2q-6kmJa1gGxtd6aGr6yaquBzb1W2c7GnNga1s-1TeowgfNpDD-TdnhDJK5ufQFse_Xwbi6FKWVVc4IEi6oTn8kiecbRPO9vTKRU2XkNNcrewdxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
نیوکاسل
🆚
لیدز
رم
🆚
تورینو
اودینزه
🆚
اینتر
السد
🆚
استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71609" target="_blank">📅 12:31 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71608">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/001bfae793.mp4?token=l1XahpOr8_BQIDOk-Z1AAXn1__k9LI_nlWBXQ2x0VFm2ug_HGpXyHvgfQdpS0F4mphPjRVmJtzLixdIVL5PlV1YMQ6FnIpKalsfVnnHp7Tj7GNtvrjyhKAR-6Vt0b_QcYq8OHioJ4_15D8bwZUeA1rONoi40tNqmHdzpgI1OaT5218nNn0KEXIO3NBTREnEdfUXULnaII95bNqy-FdsEkKVoiKCCw2gf-iTEHg-u3luF6JkB7xwWFh0mCRmBjObM6ab-s2NDA-sMJdQuAZJ0_DVb4Kf63EyIH_5MYyfyLNAAsy15fUbNKhnwgsCqMxPASD7KDd4xiQQY1EJJgAu3tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/001bfae793.mp4?token=l1XahpOr8_BQIDOk-Z1AAXn1__k9LI_nlWBXQ2x0VFm2ug_HGpXyHvgfQdpS0F4mphPjRVmJtzLixdIVL5PlV1YMQ6FnIpKalsfVnnHp7Tj7GNtvrjyhKAR-6Vt0b_QcYq8OHioJ4_15D8bwZUeA1rONoi40tNqmHdzpgI1OaT5218nNn0KEXIO3NBTREnEdfUXULnaII95bNqy-FdsEkKVoiKCCw2gf-iTEHg-u3luF6JkB7xwWFh0mCRmBjObM6ab-s2NDA-sMJdQuAZJ0_DVb4Kf63EyIH_5MYyfyLNAAsy15fUbNKhnwgsCqMxPASD7KDd4xiQQY1EJJgAu3tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤡
مجری صداوسیما:
اصلا نگران نباشید اوستاد خوش‌چشم مجدد توی برنامه ها شرکت خواهند کرد و انقد پیام ندید و مارو نوازش نکنید که چرا اوستاد چند وقته نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71608" target="_blank">📅 12:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71607">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=gRJ3sJ0ylOWA3qZJgZrRRJl_DPQ1_1lK68OnL4zWX3WpS3Nw6KI3hREb6K17pryWdwexA3W7lc5y43TGBamjAYZ0JJX96HqDsOvlurEqC49az5eZlf6cLP9d-fJL1GPzJUwzD0pfT7czMT1uJW62Q9sAjcU2eI8U8u-WK6z8J5oIKrRvzRzAfIlOH-5TbrP5cBgRMzUeXwBnGnd3NEsOsvE-45hIg5Olzol92UZT03RAD3_68K9O8lUfDS93wVemBPlSLCuh2IrhwOxZpfV-JT2qvkesvTCwMx_Izb5_XnKIuGwigX3KP8YUYYCg6mZpA9fTZvQ0PxXqqlmbir7D4gJ2UyuqvEJZrGou47ATD68HBLlee6IbQctIBHSI5AvpJ31FNTkH0Xn28rW0utsi23SprSQhPRpETkEFtOB7EmdXW41wMzwYfbAssmDFiFgBkn9_ISMkBwaYieqenhcSRJ0-i5mYSVnm2SyFg-I60QEFUuO7bM8xd-8tf0f1Po1Rsp1A28cGd1J67eFNApc8LT5Fuc6ShUb1NTISEb1o1hy4M5OjdoVAPgJtPSqi3ZRV-nt7iLYPqCkmUbPW551t-L5P9U9FzH6E4dKbC8cpf9K8v14OTTqQIql_t5QihSB61QzyvaT5xyD4mfaGuLCXUDOmOctrECImyrakMUzSdgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f19ca22a78.mp4?token=gRJ3sJ0ylOWA3qZJgZrRRJl_DPQ1_1lK68OnL4zWX3WpS3Nw6KI3hREb6K17pryWdwexA3W7lc5y43TGBamjAYZ0JJX96HqDsOvlurEqC49az5eZlf6cLP9d-fJL1GPzJUwzD0pfT7czMT1uJW62Q9sAjcU2eI8U8u-WK6z8J5oIKrRvzRzAfIlOH-5TbrP5cBgRMzUeXwBnGnd3NEsOsvE-45hIg5Olzol92UZT03RAD3_68K9O8lUfDS93wVemBPlSLCuh2IrhwOxZpfV-JT2qvkesvTCwMx_Izb5_XnKIuGwigX3KP8YUYYCg6mZpA9fTZvQ0PxXqqlmbir7D4gJ2UyuqvEJZrGou47ATD68HBLlee6IbQctIBHSI5AvpJ31FNTkH0Xn28rW0utsi23SprSQhPRpETkEFtOB7EmdXW41wMzwYfbAssmDFiFgBkn9_ISMkBwaYieqenhcSRJ0-i5mYSVnm2SyFg-I60QEFUuO7bM8xd-8tf0f1Po1Rsp1A28cGd1J67eFNApc8LT5Fuc6ShUb1NTISEb1o1hy4M5OjdoVAPgJtPSqi3ZRV-nt7iLYPqCkmUbPW551t-L5P9U9FzH6E4dKbC8cpf9K8v14OTTqQIql_t5QihSB61QzyvaT5xyD4mfaGuLCXUDOmOctrECImyrakMUzSdgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ℹ️
باز و بسته کردن (مونتاژ و دمونتاژ) کلاشنیکف AK-74 توسط این بانوی روس
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71607" target="_blank">📅 11:30 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71606">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">‼️
اگه نیسان کشنده ندیده بودی
این ویدیو رو ببین تا ببینی همچی توی ایران ممکنه
😟
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71606" target="_blank">📅 10:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71605">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=Jf_joWAOfIksxz0QTEwlzqqA-vsEWv1T7QSwfbmijUk6yTCW_ptmk2rIXJ4bzLILASycJ8Vmpo_ubnUjWAbPbZATtnvI125RLy5EobRnr8LZYi4-8W4fX76LClqWSoLmxqiLAVs7NxlEglwYF7Rb5O913sXAr7HifCu5yjTTNGWLH9Y_dzcEgoHlfhHiLBL-xUs-a5tWRPCHSnxtbuHYfyaIK3Mk8EU0X0C-nmqKej9fdIvcIhvSi9u3GJ0Iuku56JvASiew9hLVrGOdDBddPZN_Ui0_Pare33ueDbygzmaqdL_ARzAphnccaikL2q8jBXMGH8EdzzxezNOuoZ9USg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48ed023bda.mp4?token=Jf_joWAOfIksxz0QTEwlzqqA-vsEWv1T7QSwfbmijUk6yTCW_ptmk2rIXJ4bzLILASycJ8Vmpo_ubnUjWAbPbZATtnvI125RLy5EobRnr8LZYi4-8W4fX76LClqWSoLmxqiLAVs7NxlEglwYF7Rb5O913sXAr7HifCu5yjTTNGWLH9Y_dzcEgoHlfhHiLBL-xUs-a5tWRPCHSnxtbuHYfyaIK3Mk8EU0X0C-nmqKej9fdIvcIhvSi9u3GJ0Iuku56JvASiew9hLVrGOdDBddPZN_Ui0_Pare33ueDbygzmaqdL_ARzAphnccaikL2q8jBXMGH8EdzzxezNOuoZ9USg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست سلاح جنگی بر روی شتر توسط یک عرب
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71605" target="_blank">📅 10:32 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
