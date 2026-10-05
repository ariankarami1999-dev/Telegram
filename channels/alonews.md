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
<img src="https://cdn4.telesco.pe/file/Z5P0Rgbq6jBZCK3Y3sNxSfo0pwNkRda6IAY61ySDJd2Oomd3KaMMbvalNPD1_liIuTZYsSkk0P8zSQbwWlip0RwXSJ_3XJ5B_q0YiHVlxXhLKXstFxmptKrhIYAm9O52AWsxZmElfXXKaoMu1Ph1kWVjy2jve_n-J7Y7e5fI83ujI2a5_Y-SjXXhwg99HhJdB4Ivs4GJ88a4UabL0biuBJpvSTbFgx4ErrzY0s7LYIQhfpW8RZ8Li8ueSFu0JYeIi3484mFT5uJE7HyKhfEyMgjgV_8A3N7hxTAQl-Tv4aPrFW7YIkKIJqh7vCNC5S32YzglLZDHaDWy_xT9CRWXHQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-13 05:41:06</div>
<hr>

<div class="tg-post" id="msg-151012">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🟡
طلای ۱۸ عیار: 26,327,800  تومان
🔻
حباب طلا ۱۸ عیار: -1.89% ______________________
🟡
طلای دست دوم: 25,976,804  تومان
🟡
تتر: 268,950  تومان
🟡
یورو: 302,960  تومان
🟡
هر گرم نقره: 549,720  تومان
🟡
سکه امامی: 271,075,000  تومان
🟡
نیم سکه: 142,610,000  تومان
🟡
ربع سکه:…</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/alonews/151012" target="_blank">📅 01:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151011">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4pFsOi0-ffEENJJtsf9ZwvACeNbtHgE3fu0ceyNMCZ6JQSUNDJcuinalyJU-b_cuHq8dniPI68sB7YWis_oKal0VLQkPEFJIkFCoCAFHVVpex7WxNEHPAyCYc_2tG60UtiGfCRsecS9GZ6BI1aV9F4redpDvavm2QrlwYoLs-7WROyXbxlE1l1ItDOXoiz6w5EwgsEDm9kBshC6k6VTBTSkpiiROeUssV6OyURTYmT9zGxoBnA3wi_6oyni9moqegai7XZtUuemT0lcbkt-D-qz8JqBi8-17S-CCtVmBPHfCRSzZkTJjKKZoDSyT8nJPbvObroyB8BMu9A3O0XjOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بارون‌های انفجاری از آبان میاد
🔴
هواشناسی میگه بارون‌های این چند روز در مقایسه با چیزی که تو آبان میاد هیچی نیست. قراره از آبان بارون‌های انفجاری شروع بشه و هفته‌ها ادامه داشته باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/151011" target="_blank">📅 01:45 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151010">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=a2YLqE0jVEQVpi5y8-esk9KgByqISHmJAOobxS2Cu1M8mv0jfqyXyowvbEIJt7GiB4KhLONPwwv1p8hPendjMa9i1iNaMqn_l2R3LiNZEm20aYu9sdf0yfMms3f-5TG9snDo7RF6Joo_jVqpCQDM5DOLXIPtSihzfg3WRKn7Te3R6jprxrA-mIqP5iwriv_ljkZHEOJZOu0CqJxsIfX53BETtqjIbWNZdsfa1eW0p1Nlokk01p3IQou4asPexbNMdYaVxcqXWfgP04e8PkLQCrAiMyFT69DlpuX8c2cu_dWJFqJW6pCUTRgIE06mi-tiimFRfkTDyiGEzpIN3Ga9Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e436b8c05.mp4?token=a2YLqE0jVEQVpi5y8-esk9KgByqISHmJAOobxS2Cu1M8mv0jfqyXyowvbEIJt7GiB4KhLONPwwv1p8hPendjMa9i1iNaMqn_l2R3LiNZEm20aYu9sdf0yfMms3f-5TG9snDo7RF6Joo_jVqpCQDM5DOLXIPtSihzfg3WRKn7Te3R6jprxrA-mIqP5iwriv_ljkZHEOJZOu0CqJxsIfX53BETtqjIbWNZdsfa1eW0p1Nlokk01p3IQou4asPexbNMdYaVxcqXWfgP04e8PkLQCrAiMyFT69DlpuX8c2cu_dWJFqJW6pCUTRgIE06mi-tiimFRfkTDyiGEzpIN3Ga9Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مراد ویسی: جنگی که توی راهه، آخرین جنگ ترامپ با جمهوری اسلامی خواهد بود!
🔴
اما به قدری این جنگ شدید و گسترده‌اس، که جنگ ۱۲ و ۴۰ روزه، پیشش یه شوخیه!
🔴
شدت بمبارون‌ها خیلی شدیدتر خواهد بود، کشورای بیشتری درگیر میشن و این نبرد آخره!
✅
@AloNews</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/alonews/151010" target="_blank">📅 01:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151008">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSH8aGogPjkLQ5u93XthGHOm8g38RhS8Wl2j9UIKr5lmxlXX-FAcDougainAPGzdMBbQcV9KSiAZ_9M6V6xiu_KOVc2bW2S3xXgdApGDbW0CPJFdyxn1UUB2J4JMuVQoRcF4fBUiI-vMwCpYrTgjIOoYy-j_GRnTYr7eFQlgoZFhW8-q94coFoeHFluUDdk2iUT7MePAOGFA8s7JxsirsVpi53GKmg9DtQKAkJzzSYvW1YFWFxMcRbtquHBU8cw8MZevaLxpZQCsZrCT3ppNbT1FE8_ohNbyNHA8Q_Uw6jwyF3moJKWcUge8gxVn2uA8qdjf0nTR_1V02q31udK54A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار نزدیک به دولت ترامپ : پنتاگون در حال آماده‌سازی گزینه‌هایی برای حمله هسته‌ای به ایران است.
🔴
این را به خاطر بسپارید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/alonews/151008" target="_blank">📅 01:16 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151007">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc0a3ccc7c.mp4?token=PozBk0YXnjGHz3t1dhp-rfRyCKR2AiGd-JlN0NeQ3VmoIyUkesFr1pHtWEvtitiGmX-iw5eXT5f2JkwWKEkJ411DLrhXgVVqZ40Id28afiyUgbfT0CdyDI_cWwhnFsWZrTVTwaHoA6ZGDxZMUmDX9remCZNH1qf0ecglw_moybg5kCvB4diAl4qruUZb_F5XlbWtyZYxy7iPAhZM0zdisy5980xaSRv4LoIj42sd2s94gzhyMpD80NOaGTne_Tlni5a2skjN7zYgXBMYj3aIg_-HNuPD8agph4yMXvdqSVFTKaPnBvJzRDqGHnekmqkNUHFB9VXN9kpOUCaWc1_o8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc0a3ccc7c.mp4?token=PozBk0YXnjGHz3t1dhp-rfRyCKR2AiGd-JlN0NeQ3VmoIyUkesFr1pHtWEvtitiGmX-iw5eXT5f2JkwWKEkJ411DLrhXgVVqZ40Id28afiyUgbfT0CdyDI_cWwhnFsWZrTVTwaHoA6ZGDxZMUmDX9remCZNH1qf0ecglw_moybg5kCvB4diAl4qruUZb_F5XlbWtyZYxy7iPAhZM0zdisy5980xaSRv4LoIj42sd2s94gzhyMpD80NOaGTne_Tlni5a2skjN7zYgXBMYj3aIg_-HNuPD8agph4yMXvdqSVFTKaPnBvJzRDqGHnekmqkNUHFB9VXN9kpOUCaWc1_o8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: به کسانی که برای پرداخت هزینه بنزین، غذا و سوخت دیزل به سختی می‌افتند، چه می‌گویید؟
🔴
پرزیدنت ترامپ:
شما بازنده‌ها هستید. این بهترین اتفاقی است که می‌توانست بیفتد. اگر در این اقتصاد به مشکل برخورده‌اید، یعنی بازنده هستید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/alonews/151007" target="_blank">📅 00:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151006">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgQvW9rxXZizzXdnhEm2qD8L94Cpoe8AJI71sBD6WBEVEek86rg1ocxeaECvXPXvL-gE5U9LzjWxgdxj_BhjgHV1YLaNIXHYUDFgg-3QUDHcCSiC7PYc1hGOhqjuijSRHPLsYAC3RGu8FwGgkUg8jonbjntNiTUUDZqu-LN4j9ddNG06O8oF5XXYCOQpU3siXQx027_UsOp7lveesZb3mT2RjP_dRk8Dmg4_vavt-AZxwBASzXLEjkJ02VybpbIRlBDUDT5IaODERMsJPbWwACsfmnY8E1J_BV7WaiEKdrZDFhTD5FT5CL2CD2xTAkmNOiNywDg8OMgdwdgujNhUmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این عکس رو ببینید!
🔴
در نگاه اول یک تندرو و سوپر انقلابی است اما درواقع وی مهدی نادری جهرمی، جاسوس ارشد موساد تو ایران بود!
🔴
این شخص فارغ التحصیل دانشگاه امام صادق و موسس اپ ۷۸۰ بوده!
🔴
خلاصه پایداریا و تندروها و این قماش کصخولا اکثرا فیلم بازی میکنن و درونشون یه چیز دیگس
🔴
این شخص الان تو سواحل تلاویو داره آب پرتغال میخوره و به ریش یه سریا میخنده
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/151006" target="_blank">📅 00:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151005">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f64fad2c13.mp4?token=AaqH7VtbJ7eaiyMku9ENRydDxbg0r13-6TxqAlFATUuj7ubCGA6znU9uT5uMv9qB3Hi2ZUel8-LrFmxJjHYGNba1ChUdgoPHioWjWHngm4nb6cKWhFJrrc2fBHAKHd3_rYNAT-aFRwxLyy-ZaDQLep0TMgGOUBd_Xh5zgGi79su00QlQLoK38lwrDrnjunTgooOv62pXl-UPR_i68ir-Smxy-UzaSngASUMzl7Fizux2G2UPUjffjhl5ekG6MX4_el69WhKyR91Hk8Yr__gvct4AlgTtSGEqVx2X_UgOSVtIjK-Ux7bTrgwVOhDAWdVViPxhMLG4Cn2zF4KQdgSa3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f64fad2c13.mp4?token=AaqH7VtbJ7eaiyMku9ENRydDxbg0r13-6TxqAlFATUuj7ubCGA6znU9uT5uMv9qB3Hi2ZUel8-LrFmxJjHYGNba1ChUdgoPHioWjWHngm4nb6cKWhFJrrc2fBHAKHd3_rYNAT-aFRwxLyy-ZaDQLep0TMgGOUBd_Xh5zgGi79su00QlQLoK38lwrDrnjunTgooOv62pXl-UPR_i68ir-Smxy-UzaSngASUMzl7Fizux2G2UPUjffjhl5ekG6MX4_el69WhKyR91Hk8Yr__gvct4AlgTtSGEqVx2X_UgOSVtIjK-Ux7bTrgwVOhDAWdVViPxhMLG4Cn2zF4KQdgSa3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
با همین افکار تخمی، لاکار رفتید
🔴
سردار فدوی: قیمت گازوئیل تو اروپا 2 یورو شده که یعنی 700هزار تومن
!
ما اینجا 10 هزار تومن پول بنزین میدیم که حتی یک دلار هم نمیشه و اصلا متوجه نمیشیم گازوئیل لیتری 2 یورویی یعنی چی
حتی با اینکه قیمت ما سه نرخی هست بازم کمتره به یه دلار هم نمیرسه
این شرایط قیمت ها بخاطر ابهت نیرو های نظامی جمهوری اسلامیه که بوجود اومده
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/alonews/151005" target="_blank">📅 00:34 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151004">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
آکسیوس: آمریکا باز هم درخواست عربستان برای شرکت در عملیات علیه یمن را رد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/151004" target="_blank">📅 00:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151003">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سردار فدوی: ایران و عمان بر تنگه هرمز حاکم هستند و قوانین تنگه هرمز را ما می نویسیم و در حال اجرا است
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/151003" target="_blank">📅 23:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151002">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
وال استریت ژورنال: آمریکا تمامی بمب‌افکن‌های B-۱ خود را از پایگاه هوایی RAF Fairford در بریتانیا خارج کرده است؛ مقام‌های آمریکایی روز یکشنبه گفتند این تصمیم در پی نگرانی‌های امنیتی درباره طرح‌های احتمالی علیه این تأسیسات اتخاذ شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151002" target="_blank">📅 23:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
سنتکام گفته ایران باید تسلیم بشه یا جنگ سختی هم اقتصادی هم نظامی راه میندازیم!!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/151001" target="_blank">📅 23:46 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151000">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
سردار فدوی: در صورت حمله زمینی آمریکا ما هر نقطه‌ای که مربوط به آمریکایی‌هاست، پایگاه‌های آمریکایی‌ها، هر شناوری که مربوط به آمریکایی‌هاست را هدف قرار خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/151000" target="_blank">📅 23:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150999">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0df3435529.mp4?token=ESHTdN1ITiYq6-198hz3ewU6YpCpU4ym1kLgMyKgD30pESmA9Jw01Co8_2MtKORJIxAV1MmzHoxLOJfPXIQIzEhDVufw4kkyudifapiaommH3pG0V1dN7Kw9ZHMYeJS7qi9uBiCxn0SVVGQ8Qeh3hUUnHpEbh4WRyZpY6fNttS_o9BL2QfJiwjIweu09M-rskR_EJbFnKk7ky_T2GdwI7AbHWSzRpk7S2cUEudalVNHt4ds0V8lzQWYOcYPmZvjqAilxvylm2rS6EIr6EJ1mpVa1A6GPk3PmOIb3I0UJXxhIOHDi32XeII-nudGJ8PzesKckU8IISbtDi-zPvjoFEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0df3435529.mp4?token=ESHTdN1ITiYq6-198hz3ewU6YpCpU4ym1kLgMyKgD30pESmA9Jw01Co8_2MtKORJIxAV1MmzHoxLOJfPXIQIzEhDVufw4kkyudifapiaommH3pG0V1dN7Kw9ZHMYeJS7qi9uBiCxn0SVVGQ8Qeh3hUUnHpEbh4WRyZpY6fNttS_o9BL2QfJiwjIweu09M-rskR_EJbFnKk7ky_T2GdwI7AbHWSzRpk7S2cUEudalVNHt4ds0V8lzQWYOcYPmZvjqAilxvylm2rS6EIr6EJ1mpVa1A6GPk3PmOIb3I0UJXxhIOHDi32XeII-nudGJ8PzesKckU8IISbtDi-zPvjoFEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حسین یکتا در صداوسیما: ما یه جنتی داریم عمرش از خود اسرائیل بیشتره
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/150999" target="_blank">📅 23:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150998">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
آمیت سگال، خبرنگار مشهور اسرائیلی: این هفته، خطرناک‌ترین هفته ۲۰۲۶ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/150998" target="_blank">📅 23:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150997">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUu6wTdWz6_B1V3cQKcl704cwo3Ri7YXQacFVR_dCYcMuGf87-zlqeguajjxyJnBG2XYIf3-Ebtk4sIhSdn3rm3U7jAvRKXgSz7wjVJtTKhJnyCOx1gSVE_pnd7pShDnTGEC-irSVIsVnfx6GxJkV_lKMU6sXdRdqJBziUI6smjlmeSeaT0jrB5MzJDJ-7hXKojMWKq_pfDSngspE3UfHPI7M7yCYgWTbbvhluYK6LCGUeFI2IH573aUsfYzrdhpxmbQ5hKb5TDnZLRCt2Mav94AiT92eLwYQF4fHt_tunEsGnlzpik_Vrxu8dBD3EaDGbJPahUkLpPzBOlf8n3e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
کوچک زاده: منم بکنید تو زندان
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/150997" target="_blank">📅 23:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150996">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
گزارش از گشت جنگنده های ارتش در برفراز تهران
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/150996" target="_blank">📅 23:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150995">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OpM8b1a-vNb4Wl31OjFNl6x7er_iLJkhtoYRIYfws7CFo4aHy1HIjGsRJulvRYp1LiFeEJQdIRpCQelKh5m3_18SBPDIdzlP25CFcc86lG-pGBuTuh413DLdTCF9I2YAc2i8WmSXtCu9nIncST21GhDKLVVYAfGggJ_kUYeOlmUEdFxqajUnFo4RuquJiGMazXEhlNRjvBTyKeMXu8bw420jbTQrS3UBp6NGLZsIDyUloQUaIYfj7hPuIV_iTX8GLrPjqMJ2j40Y5G2wK0ezawQB7mojioZfIWeujDMDGIL7trLUAVlqycQ9zbNH1TWvOLjP-c0dhtCHhKtXl22lZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حملات سنگین به مواضع حماس در نوار غزه
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/150995" target="_blank">📅 23:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150994">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وزیر اقتصاد: مردم صبوری کنن، مشکل تورم بزودی حل میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/150994" target="_blank">📅 23:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150993">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/674d1e998f.mp4?token=kkJTlj5EbkDkgqiYd6AcYO7FDfLWHkA2bJMQKSVCxb-E7YmrTrzv1xMxeDqjJKeMJLTcaMUkeMiQIgzH2BlHB5_-qTH2Ie4ztMrsQmWrvY2ZNrRCdsQNgsVMpoVRdhSzxT85MEcfd6P14jS09V_Pk4lD6bVWXBTbqHtdUYJD08oSF1DB4Nke4RINeZvjncsKWKX-PrQAlR7FY2PjgoPx5CJsWa6qZaW80qfu6njsZBcYqSrcpzjOIC0_OA3M2OY6UZHqtsYjd4oyT-1WKeo_YY5LMbZ3u7C6nYKm29XLqQ0NCnhoA-hKjMeMJxaWg7_26-KLCbmNuhbZ3vx-1gWNZB4tnvERw7dqZZ8_vJTPg6cZics9rdpsVf54etGeXOWDoDVhfrnTjGEqxsz3tFsU02ko8u_WFco5cFCGMJQsfQBJN74WwsKHGjQw4E4L-rbFAybvbah5wlmlk8tqlfCF9b4UW6mXXKI8OvX7M18V2TtP1poQTnR1maau3V5CkmtA55eGFAtkOK8zyto0BqL1xvDLt5lHXzjnLT73pXTynDlW8uvIZ0GWTUWhPSk9hO-nrlbtPua2hPGbUJq1lymn8z8mFDq6snsV1ur3ZQ1AoyTBXrQ41HuXhLoz32WIpYWm_6TuKmS5pvbx718NZ61ZWV8OerxkRncXo5p_bXqXsdY" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/674d1e998f.mp4?token=kkJTlj5EbkDkgqiYd6AcYO7FDfLWHkA2bJMQKSVCxb-E7YmrTrzv1xMxeDqjJKeMJLTcaMUkeMiQIgzH2BlHB5_-qTH2Ie4ztMrsQmWrvY2ZNrRCdsQNgsVMpoVRdhSzxT85MEcfd6P14jS09V_Pk4lD6bVWXBTbqHtdUYJD08oSF1DB4Nke4RINeZvjncsKWKX-PrQAlR7FY2PjgoPx5CJsWa6qZaW80qfu6njsZBcYqSrcpzjOIC0_OA3M2OY6UZHqtsYjd4oyT-1WKeo_YY5LMbZ3u7C6nYKm29XLqQ0NCnhoA-hKjMeMJxaWg7_26-KLCbmNuhbZ3vx-1gWNZB4tnvERw7dqZZ8_vJTPg6cZics9rdpsVf54etGeXOWDoDVhfrnTjGEqxsz3tFsU02ko8u_WFco5cFCGMJQsfQBJN74WwsKHGjQw4E4L-rbFAybvbah5wlmlk8tqlfCF9b4UW6mXXKI8OvX7M18V2TtP1poQTnR1maau3V5CkmtA55eGFAtkOK8zyto0BqL1xvDLt5lHXzjnLT73pXTynDlW8uvIZ0GWTUWhPSk9hO-nrlbtPua2hPGbUJq1lymn8z8mFDq6snsV1ur3ZQ1AoyTBXrQ41HuXhLoz32WIpYWm_6TuKmS5pvbx718NZ61ZWV8OerxkRncXo5p_bXqXsdY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از لحظه نجات یک خانم گرفتار در سیل ایذه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/150993" target="_blank">📅 23:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150992">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
شبکه 12 اسرائیل: خلبان عمانی اعتراف کرده میخواسته هواپیمای فلای دوبی رو ترمینال فرودگاه تلاویو بکوبه تا تعداد تلفات بیشتر بشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150992" target="_blank">📅 22:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150991">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDSkQAxbhTx0JcayHGcEFkbyvUdStIMOiHU4NCeeIreZigzTzdho5aiTDLMsAK9VApEVT2aKNjO8_BAgTYavnAQwnRDFgPFh3_vO7Rm-3jn6I5o-Im5Zu0CiKNzF8NuybyjXmUImgf16CSoQSGwcv8Fu6cWtPiPfty2cX-nGuKmbekBv30I67233J4FyaZl8efTvY4x-I6NF3yeasu1XagUbXVO8VdeLjtt8u8F43tEi3jxfp-bvBT8qYkA23vzfXOrUtSHTiQLG5IzyBkS9TPp_-HkBtcXYqnN_6Uc93N4gm_kRQUd0DOw-eiFJEOJjdeBcKSI89x0oEdsu9RU4Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله به یک نفتکش در سواحل یمن
🔴
سازمان عملیات تجارت دریایی انگلیس خبر داد، گزارشی از یک حادثه در ۶۰ مایلی دریایی جنوب المخا در یمن دریافت کرده است.
🔴
به گفته این سازمان، یک نفت‌کش از وقوع چند انفجار در نزدیکی خود در جنوب المخا در یمن خبر داد، ولی خدمه در سلامت هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/alonews/150991" target="_blank">📅 22:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150990">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzuVoHP6ex5v59A82x1nvOkv9Bi2dwOPuYGVqT4inV08SZH3hk2-8Cm4BpksgaKjZmeQ5bsX9F5WBwh8b7OJSKzk0673hlyfgMal8a1rngd8nREP83j99I97GFHy8A9gpHxOqw5oA5tAsQhX0n5vmeOk2j9O1XT4nJYAT_dX133jBoEXN3Lt47B7ZckajqJA1pkdPgOqd4rcPuwEGYJYwuTtEKrZ0eZomvAK_mHOHCgGVKSnfsU7FjtA7hP3WR4d6mNW12Jmgt6liM-fvx2R48eMt47-axqv3hD51809jsQpagBDp5tpNHmFM3V8yhlmX1VC9dQZ76xqQNtj3Hy5Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ با انتشاری عکسی از خود در کنار رئیس‌جمهور چین نوشت:
ترامپ جوان‌تر به نظر می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/150990" target="_blank">📅 22:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150989">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: به نظر می‌رسد که همه طرف‌ها در حالت آماده‌باش کامل هستند و منتظر هرگونه تحول نظامی هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/150989" target="_blank">📅 22:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150988">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🟡
طلای ۱۸ عیار: 26,327,800  تومان
🔻
حباب طلا ۱۸ عیار: -1.89% ______________________
🟡
طلای دست دوم: 25,976,804  تومان
🟡
تتر: 268,950  تومان
🟡
یورو: 302,960  تومان
🟡
هر گرم نقره: 549,720  تومان
🟡
سکه امامی: 271,075,000  تومان
🟡
نیم سکه: 142,610,000  تومان
🟡
ربع سکه:…</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/150988" target="_blank">📅 22:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150987">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
قتل همکلاسی بعد از زنگ آخر مدرسه
🔴
اختلاف دو نوجوان همکلاسی در سال ۱۴۰۲ پس از تعطیلی مدرسه به درگیری خونین با چاقو در پارکی نزدیک مدرسه منجر شد. آرین، نوجوان ۱۵ ساله، مدعی است سیاوش او را به بهانه پیدا کردن یک ویپ گمشده به پارک کشاند و از پشت با چاقو به او حمله کرد.
🔴
آرین می‌گوید: در این حادثه از ناحیه
است دچار آسیب عصبی و محدودیت حرکتی شده است. او همچنین گفته برای دفاع از خود یک ضربه به همکلاسی‌اش وارد کرده و بابت آن به پرداخت دیه محکوم شده است.
🔴
سیاوش در دادگاه وارد کردن ضربات چاقو را پذیرفت، اما اتهام شروع به قتل را رد کرد و گفت قصد کشتن همکلاسی‌اش را نداشته و تنها می‌خواسته از او «زهرچشم» بگیرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/150987" target="_blank">📅 22:05 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150986">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا (UKMTO) گزارش داد چهار نفت‌کش طی ۴۸ ساعت گذشته هدف حمله ایران قرار گرفته‌اند.
🔴
خدمه یکی از نفت‌کش‌ها که ۲ اکتبر هدف حمله قرار گرفت، ناچار به ترک کشتی شدند.
🔴
نفت‌کش دیگری که ۳ اکتبر مورد حمله قرار گرفت، برای مدتی کوتاه دچار رانش شد و سپس با کمک یدک‌کش به سمت فجیره در امارات حرکت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.2K · <a href="https://t.me/alonews/150986" target="_blank">📅 21:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150985">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
خروج بمب‌افکن‌های راهبردی آمریکا از پایگاه فیرفورد انگلیس
🔴
۱۰ فروند از ۱۲ بمب‌افکن استراتژیک B-1B Lancer نیروی هوایی آمریکا که در پایگاه فیرفورد در انگلستان مستقر بودند، در حال خروج از این پایگاه و بازگشت به خاک آمریکا هستند.
🔴
انتظار می‌رود ۲ فروند باقی‌مانده نیز امروز خارج شوند، به این معنا که هیچ بمب‌افکن استراتژیکی در پایگاه فیرفورد حضور نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/150985" target="_blank">📅 21:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150984">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این پسره پشت پرده دلار رو لو داد
😐
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/150984" target="_blank">📅 21:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150983">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1433d0f2d8.mp4?token=Y-0-t-_Rao5xHrQMsYETwTxwrBzSwSVsShrUBfRwK4muwOIO9q_UdHG-HXGXXEQbpsb9RxkJH9zrM3DYGjUEo4mbUH_jrvngq4JcL71atkkdQ-r7xHOBAWCQHNNFpFdVU7J7dL5svjOVEzG2f9af4_dah0u4L-n4NxW0qRgizVxQ7QWuF69gnAJPA0q9QtyIhO2LGZu8eNLPUYIl0rvRs8OkOMymYThx_mwZuBqyULOHF5SanjJeu0rSiXUYQxnM4aGPlYffhFZWl5VmKJgGGmxzWKn8pi2kspHS04TgBtiDC0nsuQhQYXmVG2CQftnrXzyAzGZvogY6pE26Oe8cMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1433d0f2d8.mp4?token=Y-0-t-_Rao5xHrQMsYETwTxwrBzSwSVsShrUBfRwK4muwOIO9q_UdHG-HXGXXEQbpsb9RxkJH9zrM3DYGjUEo4mbUH_jrvngq4JcL71atkkdQ-r7xHOBAWCQHNNFpFdVU7J7dL5svjOVEzG2f9af4_dah0u4L-n4NxW0qRgizVxQ7QWuF69gnAJPA0q9QtyIhO2LGZu8eNLPUYIl0rvRs8OkOMymYThx_mwZuBqyULOHF5SanjJeu0rSiXUYQxnM4aGPlYffhFZWl5VmKJgGGmxzWKn8pi2kspHS04TgBtiDC0nsuQhQYXmVG2CQftnrXzyAzGZvogY6pE26Oe8cMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مرتس، صدراعظم آلمان: اقتصاد روسیه نمی‌تواند این جنگ را به طور نامحدود ادامه دهد. ما می‌دانیم که اقتصاد روسیه از قبل به نقطه‌ی بحرانی خود رسیده است: تورم ۷ درصدی، نرخ بهره بانک مرکزی ۱۴ درصدی، کاهش درآمد حاصل از نفت و گاز، و کسری بودجه‌ی دولتی که به طور فزاینده‌ای در حال افزایش است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/150983" target="_blank">📅 21:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150982">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vy6b2X9PNopsbfxPquSzTqtaAT8g9zKpl7OqHRP0Z_VJiY6bYfZoer5bRjV1kUiINkzGKljmc1B3eab7Ow2D1XJGL174JbsrM2jYh551Tx5LhzICLRpdhJkyDhQZ6wjo2SCBmgyrY63Srsw45Iyu6xi-MJpcyNcl7fPxYhBm9IAZ0OkDZYkRhV-ztuxovwXX7KbHgQqrZjdG3Qs1ZlwTsDcZcwPWXA3AugGrkDOsKCjQF1kV68WZPVs8HBGr_vovqAXNnF4157YZL4s3q_EiOgw-McZj2KzKLX86OgFIZGX9XIv4ebBlYrdJaKtdO3sjcaD5A9m3WZ9ZS-L_cCN1kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ تصویری از خود به همراه پنگوئن‌ها در گرینلند منتشر کرد.
🔴
پ.ن : پنگوئن‌ها در گرینلند زندگی نمی‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.2K · <a href="https://t.me/alonews/150982" target="_blank">📅 21:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150981">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aaf4c3a90.mp4?token=vrz2vwfSoDR8rEs_GZl1au6hKQ5IdxZOARYAR0wxhPwR566kaQ8cnvz3bydJQQf0WMjRuLNysnSjLCBdtoQYSjGixKBCTm-o0iniG2vmpS1oma4_J5WKPuU4h_3WP7wZgcqAXsra6hxI1i9MW_VlmrCvKU53Y0vZ1DUHmTCWBkdfAwcO1s7d_XvYRqt1VwPZotzcUvP4i9XBtoE4dGLn5pPdM3QmS7LJ6HbPnlFg7-Y1D29g2FXDv9yged8q0L-NPrT19G8JNMuNtg9hnyFO9ii1hNO_zaRGSHbRTfjHGRCGxwZrYdcYGlQLTit8q6yx3P7HpwOcMN-l-A9gu67V3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aaf4c3a90.mp4?token=vrz2vwfSoDR8rEs_GZl1au6hKQ5IdxZOARYAR0wxhPwR566kaQ8cnvz3bydJQQf0WMjRuLNysnSjLCBdtoQYSjGixKBCTm-o0iniG2vmpS1oma4_J5WKPuU4h_3WP7wZgcqAXsra6hxI1i9MW_VlmrCvKU53Y0vZ1DUHmTCWBkdfAwcO1s7d_XvYRqt1VwPZotzcUvP4i9XBtoE4dGLn5pPdM3QmS7LJ6HbPnlFg7-Y1D29g2FXDv9yged8q0L-NPrT19G8JNMuNtg9hnyFO9ii1hNO_zaRGSHbRTfjHGRCGxwZrYdcYGlQLTit8q6yx3P7HpwOcMN-l-A9gu67V3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی ها داخل شهر تعز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.7K · <a href="https://t.me/alonews/150981" target="_blank">📅 21:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150980">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقام آمریکایی:
سنتکام درباره آغاز حملات در یمن نگرانی‌های جدی داشت و این اقدام را عاملی برای منحرف شدن تمرکز آمریکا از ایران می‌دانست
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/150980" target="_blank">📅 21:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150979">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06a3608746.mp4?token=S5aVuRDC-LIavteuPngkiyBqmUndex93WfCLBGfVbOVlnZKPwpu5tsMPbukjdqptnZLkOnxXhEEQXvLe-RNelXZfvGoyOdqKY5qyynRGb-7sbrIPBcPdfY1SAIEvNCF-y6Kh2AF2XFvEWez9XQkCXk5yOdIa-2_J4wROa4E5utuP_-fvftckozoGnS2pMxi2wuQOBjtm5kg6GK5hs7jDh7piS7w01MqVba3kiNFSPoV1pw70DbXauvwGeI4HAPV4bVA5mn9b23EElAB7DmKet_ha49iS0SqVBsk5UKMjVmUQqhDsAp_jZ26PvcyODatICZBHiu0EXI0NUYkf_85l60BwDtT8Tk-ACvEiIqKJtiZY2WluGbRUHwaqiiHMr5NEJvJodf1lWzTsMLrFpLzEsprui0_8VhSPqCm5VxQjwLCiM_-BZ1oHtUduHLu1kg7mod78iIgjLh-9sTsFRMZwrh-GwZYl00WV5Wcd-NlNboASvJcPLkXPs7CAjOCE--7B9NNn3oobbrgwr4OJDER_9QXPt42cVlLfLUVQZ-q7fIVA1SvosAc1lhvgxHbHPM5WZiAGKqxdZR-CfDBGbf1lgLJ8ZoitnUdUR8DvtN0U9k_enrbixF_U6K1cupVsq8Cc-17ZOiUbtv7nNv8V64p4xJDGgP_6NfnfzI8jh23tDUM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06a3608746.mp4?token=S5aVuRDC-LIavteuPngkiyBqmUndex93WfCLBGfVbOVlnZKPwpu5tsMPbukjdqptnZLkOnxXhEEQXvLe-RNelXZfvGoyOdqKY5qyynRGb-7sbrIPBcPdfY1SAIEvNCF-y6Kh2AF2XFvEWez9XQkCXk5yOdIa-2_J4wROa4E5utuP_-fvftckozoGnS2pMxi2wuQOBjtm5kg6GK5hs7jDh7piS7w01MqVba3kiNFSPoV1pw70DbXauvwGeI4HAPV4bVA5mn9b23EElAB7DmKet_ha49iS0SqVBsk5UKMjVmUQqhDsAp_jZ26PvcyODatICZBHiu0EXI0NUYkf_85l60BwDtT8Tk-ACvEiIqKJtiZY2WluGbRUHwaqiiHMr5NEJvJodf1lWzTsMLrFpLzEsprui0_8VhSPqCm5VxQjwLCiM_-BZ1oHtUduHLu1kg7mod78iIgjLh-9sTsFRMZwrh-GwZYl00WV5Wcd-NlNboASvJcPLkXPs7CAjOCE--7B9NNn3oobbrgwr4OJDER_9QXPt42cVlLfLUVQZ-q7fIVA1SvosAc1lhvgxHbHPM5WZiAGKqxdZR-CfDBGbf1lgLJ8ZoitnUdUR8DvtN0U9k_enrbixF_U6K1cupVsq8Cc-17ZOiUbtv7nNv8V64p4xJDGgP_6NfnfzI8jh23tDUM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کارشناس صداوسیما: در صورت حمله اتمی به تهران، سه‌میلیون نفر کشته خواهند شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.4K · <a href="https://t.me/alonews/150979" target="_blank">📅 21:11 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150978">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
گزارش ها از انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/150978" target="_blank">📅 21:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150977">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
سناریوی هولناک در پرواز فلای‌دبی؛ نقشه برای کوبیدن هواپیما به تل‌آویو
🔴
رسانه‌های اسرائیلی گزارش داده‌اند کمک‌خلبان عمانی پرواز فلای‌دبی قصد داشته پس از از کار انداختن خلبان، مسیر عادی پرواز به تل‌آویو را ادامه دهد و در لحظات پایانی هواپیما را به یکی از ساختمان‌های شهر بکوبد؛ طرحی که به‌گونه‌ای برنامه‌ریزی شده بود تا جنگنده‌ها فرصت مداخله پیدا نکنند.
🔴
این کمک‌خلبان در میانه پرواز با تبر اضطراری به خلبان حمله کرد و هواپیما طی حدود ۳۰ ثانیه بیش از ۱۶ هزار پا سقوط کرد؛ اما مسافران وارد کابین شدند و او را مهار کردند. مقام‌های امارات این حادثه را «تلاش برای حمله تروریستی» توصیف کرده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.5K · <a href="https://t.me/alonews/150977" target="_blank">📅 21:01 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150976">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
تسنیم: استان تعز یمن به کنترل انصارالله درآمد
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.6K · <a href="https://t.me/alonews/150976" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150975">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPpfT_C2gj7h3HyqpeKKE81v4BG3KzQ3BirBjqOLCiS_xEJM9DAOkBCBEl-OMr_JPMyDe3KwUe-Fht95XfumMJCDroD6tFGYZbiBydxCo7jNRA7sujoHW0_a9yzkTOl1NJzVrqQA1f86oom7eHRWPg2lPzilw3cgSWcJ6gHfR_Nk0NpyEVNml4b4ZI3DucJzeOPrKxmd5TEfl9wgEmnbTNfVAeAe9Hdn_5w23qk4lMwcFDU8bMi80RsrZurok_a_xUqsrwH56yU2Ag9ThZnx8ipAgM84a7Grh8kewycI28wCXzyyMvg_TlMwJ4OeXcz_0CS6cccxEWkoP23rNfja1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بازرگان، کارشناس تلوزیون: طبق محاسبات ما اگه آمریکا به تهران اتمی بزنه ۳میلیون نفر درجا بخار میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/150975" target="_blank">📅 20:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150974">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🔴
آکسیوس به نقل از مقامات: با میانجی گری قطر گشایشی در مذاکرات ایجاد شده
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/150974" target="_blank">📅 20:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150973">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTAM23INIZ2QgJ06x_OeB0Lvx_51E0ikZXxCmoxZaGHBqBX724QLU3ZiF63c7QdG_5kkeN2PHHmjt6XVFkCM5u4I-iJ1uy5Xe_SNOS-T-AD0T6K1w5PJlFHdUDfD3PfTVT6MDNRYeAfqvF7VKbumezetUa8FVJZTH9_mf66TtpFf0qNJhENvGST9uX5EwEqYuSHP7M9ZxS4eR1yZzf89i_JDjE8bxnOzGQGY46g8XyfKxPhrcYfI6Nmj7T-aAPk9_aR44IznDLnXQ_6AqJv3UlPqfKcsF8eAw_1Fz4EjSlh_xGd_MgXYoB4X3lFVDJQpsPEPkO4gVjKnRfFWd4Qu4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۷ فروند هواپیمای تانکر آمریکایی در نزدیکی تنگه هرمز در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/alonews/150973" target="_blank">📅 20:47 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150972">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
وزیر نفت استعفا داد
🔴
بورد سرپرست وزارت نفت شد
🔴
«طباطبایی» معاون دفتر پزشکیان: با پذیرش استعفای محسن پاک نژاد طی حکمی از سوی دکتر پزشکیان رئیس جمهور، حمید بورد به عنوان سرپرست وزارت نفت منصوب شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/150972" target="_blank">📅 20:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150971">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ایال زمیر: باید آماده یه جنگ غافلگیرکننده باشیم
🔴
رئیس ستاد ارتش اسرائیل می‌گه که باید خودمون رو به آمادگی کامل برسونیم چون ممکنه هر لحظه یه جنگ ناگهانی شروع بشه. این حرف‌ها در حالیه که تنش تو منطقه هر روز بیشتر می‌شه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75K · <a href="https://t.me/alonews/150971" target="_blank">📅 20:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150970">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XauByKVdNVQfYrLp4vSjNKva4GrUwvk7IMw1t2yjA59GgHIBveZMbZoQ6Alnh6NVjaTGcR9yrKtpvXphPj52JUI4uOWuRrXNt11phgW4l2b2JuRDq7zbOpk40kK22iFCJXdvDfnSs9CZQ4L_tbK2ccHIlnyAfzGu7irJPCzTMmFOqyri0ftkBoedP_Zyid-s01jrOrneXXHXmfKkUO4KvRosy9OUoGSvIO7gTjki5ebqfuWBp-RwuUV5QGj-9lw3zraBHVvzf7_60f39n1vdy1cuYZp3qOsO6V2ltHbtSft9QDCCKRGplWgMMPfdp4P-IvQiqO8k1YPgAmAMUTAwYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاید باورتون نشه ولی نتانیاهو تو اسرائیل میانه رو حساب میشه و رقیب های انتخاباتی و قشر تندرو بهش میگن زیادی به فلسطین و ایران آسون میگیری
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.1K · <a href="https://t.me/alonews/150970" target="_blank">📅 20:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150969">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d8f4fd4a.mp4?token=Lxu9CX7bhPMINCTgXQVTY2NeeZEoGSqgRUI_uY50Ax1Jt2puxoFQ4VN9CjUipY84Y1dRQARqt9WqA6HQt34Q2rnxHSMF_kLP8bf10h9QNpQgvlxBjM1TyNuK5byeSv5noFqxayx9vlU8gAdMEaajJuC9svzh1CzKd3VUuXBxMB0_CWJmTfVjhfDHnbBF9joWMsD-Pz7jYWTQBlydq9W4sd2sRSLOgEhacwqWyHCHCkZFIkSZMH8nzQCaqqQD9OjewwCrl5jFUR4zdx1KN68ujIj3ncBhl4oVaWL8bkiIIX27UDsgC2DSvFb--TVQPyn9I0a4JBoXh-vfMwX2OGFKuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d8f4fd4a.mp4?token=Lxu9CX7bhPMINCTgXQVTY2NeeZEoGSqgRUI_uY50Ax1Jt2puxoFQ4VN9CjUipY84Y1dRQARqt9WqA6HQt34Q2rnxHSMF_kLP8bf10h9QNpQgvlxBjM1TyNuK5byeSv5noFqxayx9vlU8gAdMEaajJuC9svzh1CzKd3VUuXBxMB0_CWJmTfVjhfDHnbBF9joWMsD-Pz7jYWTQBlydq9W4sd2sRSLOgEhacwqWyHCHCkZFIkSZMH8nzQCaqqQD9OjewwCrl5jFUR4zdx1KN68ujIj3ncBhl4oVaWL8bkiIIX27UDsgC2DSvFb--TVQPyn9I0a4JBoXh-vfMwX2OGFKuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آمار جدیدی از میزان تقاضای استارلینک در ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.7K · <a href="https://t.me/alonews/150969" target="_blank">📅 20:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150968">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KbpJir4k2bKLLb_wQ6gi3bQXSVN89o1BGqwadFpH5uernY105w3CJZaf5XLuNx7czimfIU6VoUN2hGKtEoCKDK5M1FvzRGOxzFmOHqCTuorJuYerXq2Sk7hMFzRMeBXwmjUyGt7ehnMj0la56lcXOFl7HohGUxvAzwOcJojL7VGrkDVwuguH-Og4v_L8h0Q1mb9pmnTL1XE9_ZLe4A4ejGwhob3AJGPKFsRIP05icbPbvdxAGZP9shMiRpoCDjF0jHKODc2L_KvV42R4qR-jbugrxi-TFl_FW5zOaqNcB_8oTEak1yWZjNfo-LCAF5ElEUURefI3NuumxIDtdkSu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پاسپورت ایران در جایگاه ۹۷ رده بندی پاسپورت‌ها
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150968" target="_blank">📅 20:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150967">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
پشت پرده ترسناک دلار
😳
‼️
خبری که بازار رو ترکونده
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/150967" target="_blank">📅 20:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150965">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7wmAdnYn2kMYaBEHMrAlkD6g1dZsIbp6HgLpAysqWfHXK4QeVHUnOumJLdOI_roRLDirDqvQ9ZRf-gb7GrC1ffYVlbh0BlrfzIBrT4te5m-TOKy99ajWf9aaYAMWYyb_9AxTrlEFZo4lfIQE2Dlr5SyCYA9IOU9tW47SB2-SzEgc9sZyEZW1FKRPalRhJFNaOg6vNutl0hQFLuR9cnj8YyGz47lvyrYeh_34JJarQWRBXOQNnenjEp1vBDFw_hGPq9AqEOmcqVmyOsjgZsOFZxG8t05tsIYsDYOMkN_TLnXeE3UIRMyJXQwSju0iO2k0pTOg09IMqfRQHL067JV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bo0e8wTaSxD2LmWAHwnqYX4IVL9SJz9e81Qx8F0NptSSBjQUBdfbRt3LbfUQhBjFoNA6_GGjomKOjCeOkabLn3mfWzFAzAvvEOtvaIG99m5y4E15JAvjYbYNvGlOGeZ-r5fEUQoOsaP_OhuMgcjQl7LcrSoowp5oSqOOleuk7Orqwm5LTvwaeMWo9jvl9Zzo-KlJHVD5heIroqZ2szqBSNkFAMZum8aNFOe_IX5du1pSSvnPF2LO_phsPQ3UZ6r2mhajAOhCEMAIaAiT4YlpxoTGIKxYUroiPwsdRa25z_p-qqnhFfO_bsGSNe87iX_vawv7LZcCSiPS7SDK1gxvzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نظر برخی دانشمندان فیزیک کوانتوم، تصمیماتی که الان میگیرید ممکنه روی گذشته شما تاثیر بزارند و اونو تغییر بدند.
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150965" target="_blank">📅 19:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150964">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
3000 سرباز آمریکایی در اسرائیل مستقر شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/150964" target="_blank">📅 19:31 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150963">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d0340afb1.mp4?token=b6cS7V6Dfm_8plkvjC94Z7c98-7myeplefEJcBUqbabIO7cjvbtu3ryIEAdfzLrYWzcZBeZ1rTHgCQTXxLriEsFresiQsWXRTu0k_R3OG3Hdz9HCexQfQHY8p_e4QPSGSOnsXRxw7xAJ9DktL5S8b78tMqMV17nLhpvoccCyKRJoe1y61Ozfpuk3zIWJoClTx0aPZPXfcqAg83k-kxduAw2piAA4f8S7-cWTcSl_WxFiZ8PJakR3PKj4yKJ4fCveuwXZ2up57ADlCFfk0W-Yk3uVs1fqG--mf9Ytl6t_uv7xsILqoi7qLB-wO5nLcJqUcig5iV3Fuiz35nXPmAtxGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d0340afb1.mp4?token=b6cS7V6Dfm_8plkvjC94Z7c98-7myeplefEJcBUqbabIO7cjvbtu3ryIEAdfzLrYWzcZBeZ1rTHgCQTXxLriEsFresiQsWXRTu0k_R3OG3Hdz9HCexQfQHY8p_e4QPSGSOnsXRxw7xAJ9DktL5S8b78tMqMV17nLhpvoccCyKRJoe1y61Ozfpuk3zIWJoClTx0aPZPXfcqAg83k-kxduAw2piAA4f8S7-cWTcSl_WxFiZ8PJakR3PKj4yKJ4fCveuwXZ2up57ADlCFfk0W-Yk3uVs1fqG--mf9Ytl6t_uv7xsILqoi7qLB-wO5nLcJqUcig5iV3Fuiz35nXPmAtxGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آتش‌سوزی در یکی از تأسیسات آرامکو در عربستان رخ داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150963" target="_blank">📅 19:26 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150962">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
اورشلیم پست:
جمهوری اسلامی کمک مالی به حماس را متوقف کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.8K · <a href="https://t.me/alonews/150962" target="_blank">📅 19:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150961">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔴
فوری/سخنگوی وزارت خارجه:
تهران پیشنهاد مذاکره هسته‌ای واشینگتن را رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 84K · <a href="https://t.me/alonews/150961" target="_blank">📅 19:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150960">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
آکسیوس:
ارتش آمریکا درخواست عربستان سعودی برای بمباران حوثی های یمن را به دلیل تمرکز به روی ایران رد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.2K · <a href="https://t.me/alonews/150960" target="_blank">📅 18:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150959">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
وزیر انرژی آمریکا به سی‌بی‌اس: رئیس‌جمهور ترامپ به طور موازی به فشارهای دیپلماتیک و نظامی بر ایران ادامه می‌دهد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/alonews/150959" target="_blank">📅 18:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150958">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdpHikD2h7sHZ-Q97S3E7iG9A3asN79DzavLKQ6Yhzq2Bi7vCiqYnX3hk9akvsRecyeZRCNoelRBpBIpSZUjRpWcTdx9Y9Q2jPMF4Kb8E7ox54IjCuJHRDBIOjKd6x9csPK6x6ZsQwTCRWK4UnITreywqN3_cHCWvcq9difbCeckOARL-fw2_HJtr14xfzay8mWqG3oss1jk5y6Pir3YcTWMAnXx4sDLbJR4quGF-4Mw_wu0nGQaN6luXHDOWQeAN9VYyLD7UlEr-crq09Vv-D-M4tx-z3o4dUDemI104JMVQurMvO2bpofHunpDktFmMYOSgZSCakpyoJBTcFDN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از تهران که در رسانه‌های بین المللی منتشر شده تحت عنوان تحولات عظیم در ج.ا
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/150958" target="_blank">📅 18:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150957">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46a09eee01.mp4?token=p_9nKredju3TjMfuDFhy8QhprFEoOGSYGBAwHjGcGASeD9tQZ-0hxYNkFd39kq8TwUMRXGf4uZZS7yodNLJ-DNdU3OLw6CU02cuLzdBtx7h6fazxxB_DgyRqAGYfYcZDcDHatL76_wUnJ6Rp5xfKHd--HiWPG3kgnOlI5KfnHwZ6tcwj6I59AB0sY_iZLRvWBvEBq0UjzwhqbG0CgKxDSyWKIUG8UIha3-rPqBG2znGRXuvXn0t8B_rlDRTKOlrwjQ9QObdUw5Xw8R-7E7-TosRM02tVKAdCGUqiseoGO7H8cfiFysqVIbA5hIdLx_eBkVGFHGnQ_-tdchf49CeRaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46a09eee01.mp4?token=p_9nKredju3TjMfuDFhy8QhprFEoOGSYGBAwHjGcGASeD9tQZ-0hxYNkFd39kq8TwUMRXGf4uZZS7yodNLJ-DNdU3OLw6CU02cuLzdBtx7h6fazxxB_DgyRqAGYfYcZDcDHatL76_wUnJ6Rp5xfKHd--HiWPG3kgnOlI5KfnHwZ6tcwj6I59AB0sY_iZLRvWBvEBq0UjzwhqbG0CgKxDSyWKIUG8UIha3-rPqBG2znGRXuvXn0t8B_rlDRTKOlrwjQ9QObdUw5Xw8R-7E7-TosRM02tVKAdCGUqiseoGO7H8cfiFysqVIbA5hIdLx_eBkVGFHGnQ_-tdchf49CeRaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی یکی از شب نشینی‌ها، به یه دختر بچه گفتن بیا یه شعر حماسی‌ بخون تا علاقه‌ات به حکومت رو نشون بدی؛ اونم رفت و این شاهکار رو خوند:
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/alonews/150957" target="_blank">📅 18:39 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150956">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
بازار خودرو به شدت ملتهب و در حال رشده، کوییک به لحاظ قیمتی شده قیمت همین ۳ ماه پیش ۲۰۷ و ۲۰۷ داره میشه هم قیمت مزدا 3 های نیو قدیمی
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/alonews/150956" target="_blank">📅 18:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150955">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akVr3cI2Lc-y7wA0n2sexh0GdAnfLu1Gc0GFTmviDY0KIGO1CigzQP_fJLICHq1sQC5_XTUno4b9ZDNkIG5vWbnucPC-FLQX-HuU_A2bkoGp8wxWntRxLuYy8dAkdFTAp2TSUR-KWWsRPUc5bEu1xO2JDPw0unASR3-UOEY6i5JiCs1tZiGaUrJtOEFB5yWypvl3DoB2Fkj9oWwi4FrXKd4KsRugoCesCeLToxrzEY3VfoRZhYU8u3ZeJDNi7DsQ-x4Xj9mqTJ6SyIt5Pp7x1zLUwpUQ5RObJmN7PnA5ahV-cOyuBi5TjIg_onnEXBKvFPfz4zsg5GXtfbYJtPUT2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: آمریکایی‌ها میگن ایران ابرقدرت شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.6K · <a href="https://t.me/alonews/150955" target="_blank">📅 18:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150954">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84aef80fb7.mp4?token=YD7zlKc5R3XGDUgaF6zVCm9njRmatJ395QfYwG5Ym7wpAEIdbbwSqmUkv5IyDwzSNJaQtB3MYSr6qTzlSvfK9RYIcnHddKrkQQAmBFdHXeWtLcfZs1Q_IfjMRJzHN2CuRrI62tK06f3pDbPcaFuV8FfEpMZiLIqT0CY95KnTyvD7tHpKnk9nxUgBQ1C6YGoVNwYfDPnjpqatR74rLKOaCzDN6pBAWRQcJp-dxlmkG5W9851hUxoJRphUzQL4j5Ar8Eks5pC0vq51R4Kl2cVSmkeexofGqi74jn9uYY3hk22XLCF0tAl1BDQ8hdD4ATgUNFfpE_Ve9i1iu_HW4PuF-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84aef80fb7.mp4?token=YD7zlKc5R3XGDUgaF6zVCm9njRmatJ395QfYwG5Ym7wpAEIdbbwSqmUkv5IyDwzSNJaQtB3MYSr6qTzlSvfK9RYIcnHddKrkQQAmBFdHXeWtLcfZs1Q_IfjMRJzHN2CuRrI62tK06f3pDbPcaFuV8FfEpMZiLIqT0CY95KnTyvD7tHpKnk9nxUgBQ1C6YGoVNwYfDPnjpqatR74rLKOaCzDN6pBAWRQcJp-dxlmkG5W9851hUxoJRphUzQL4j5Ar8Eks5pC0vq51R4Kl2cVSmkeexofGqi74jn9uYY3hk22XLCF0tAl1BDQ8hdD4ATgUNFfpE_Ve9i1iu_HW4PuF-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرار هیمتی از خبرنگاران
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/150954" target="_blank">📅 18:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150953">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
برآورد شبکه CBS: اگر انتخابات میان‌دوره‌ای همین امروز برگزار می‌شد، دموکرات‌ها با ۱۱ کرسی بیشتر، اکثریت را در مجلس نمایندگان می‌گرفتند
🔴
اکثر رأی‌دهندگان معتقدند جنگ ایران باعث افزایش قیمت بنزین شده
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.9K · <a href="https://t.me/alonews/150953" target="_blank">📅 18:03 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150952">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
زلنسکی: آمریکا در تدارک برگزاری مذاکرات سه جانبه است
🔴
ولودیمیرزلنسکی، رئیس جمهور اوکراین گفت که آمریکا می‌خواهد تا پایان اکتبر مذاکرات سه‌جانبه‌ای با روسیه و اوکراین برگزار کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/150952" target="_blank">📅 17:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150951">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزارت دفاع روسیه: دو کشتی باری حامل تجهیزات نظامی اوکراین را در نزدیکی بندر اودسا در دریای سیاه بمباران کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/150951" target="_blank">📅 17:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150950">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
ارتش دولت یمن تحت حمایت عربستان سعودی عملیات نظامی گسترده ای را از سه جبهه به سمت صنعا، پایتخت حوثی های یمن آغاز کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/150950" target="_blank">📅 17:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150949">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UX06ObxdEEY_2NXpZUnEH_jmi-Jmr90tr6dXVGSkE10sDvEfVDJy_5f3ci7RqGfNHN6UxuSob_sQV_D3C3TT8_Gjp4bODpxSnagrKdDyehqp608UTzdG-h1cM28M43nPt5N_imvLxldjrMsCxc6MOY9xkado4esIjSwwUiGkXywEfF1nWBVQIRZxroIZ7kr8kfgeh376KYti-1jeDFTp40R-YvYRbm0WO9uyfuNnKX5JCTJlmCY9KmAAGO9J5I-2Chdfikg-VMmKc2zgv4o3MYvTxxZndmUn0NqGHAQ7-iGfR4XVXDLlhPTXAvY8C59IvA-h5K0NyAd4Jd7XXXRLcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وال استریت ژورنال: ایران انتقام خواهد گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/alonews/150949" target="_blank">📅 17:36 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150948">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
گزارش انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/150948" target="_blank">📅 17:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150947">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
ناو هواپیمابر جورج بوش پس از ۶ ماه حضور در خاورمیانه در تایلند پهلو گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.7K · <a href="https://t.me/alonews/150947" target="_blank">📅 17:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150946">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vbnWpUEzhksbWEjavZ966WSWHxs3T4coGnG2mzSpfFDjP4j9gStq_U_snrLh4JxXq69Kpr6YsAsC0XZ281lP48e82RYmjlCZWfpi7onuqaqIorikkLbdhKTGLT5kaaIVNbCbnLmCiCnwtxiNfS7zWeraR8pHbI3pm6scvGVQhmGXV4GflPESA-_cB-dXaCHLZqNKFYWYNdQLoxfn8Qrqh8EBAgTV4SrOwWleYekH_lQKCEwA4yx9sGvdXhS0S4ReOy_OFsSWo8ekTdolEiku39etywu0-3rglnft2AjjGK5u9Rq5TOy_ECBUbiq-WlDUYUdo2R6f-ipNkfwc6ATvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل: حال امام خوبه
✅
@AloNews</div>
<div class="tg-footer">👁️ 79K · <a href="https://t.me/alonews/150946" target="_blank">📅 17:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150945">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🔴
این تحلیل ترسناک رو حتما ببین
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/150945" target="_blank">📅 17:09 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150944">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
فوری / معاون وزیر خارجه: آمریکا پاسخ طرح ۷ روزه ایران را ارسال کرد
‏
🔴
این نظرات در مسیر خودش در داخل کشور در حال بررسی است و نظرات نهایی ایران آماده شود، از طریق مقتضی اعلام خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/alonews/150944" target="_blank">📅 16:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150943">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWNFSSTxxzu8QKiFaakonKX9S1asIvfBwSpwE9U5KbOifSSuLj-x1e673o-TVsTZXJFlIhpaFDa1Ode1gNdv7ROSG6U1VInrcbmv9gJxqn4Q4Y8JD29zMPIvG3SoU2cD9N-J47LtMI7xvj6Iu7RdGcNFkDd72v3VmqLtYHUr6TTtRlh5jcuU1Ilx4sQzuw2qBBwQsGnN5v7G-r9PBjEQI_UKGHFeHGBAo7Rh1xXdatPjmEt4sUhwtGqm5FvHqlVbS_emgfZIvo0JN5bodAotR34n7huQ7LiwPosDmicLcUQctS6wQgNMpVuyU4RzXC2RDmQY2Mr-bByMKXJVHYQfWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
کوچک زاده نماینده مجلس: اون مردمی که میرن ارز دولتی میخرن، دلال و دزد هستن
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.4K · <a href="https://t.me/alonews/150943" target="_blank">📅 16:53 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150942">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=LQrHyB0TZvQSTVxNadZMvI9WENGwQY97x6MhCiiZhJqP7MpBPF_aLq7YRwUYLsI0dqudXn5u-38d0t8-Gv2L5HHIciJe0PR-r-tE23TL1xdxnD53-z3e1hG0QYlYi4TmTaAQNf7SI838-03FLB58qgdHvoNjza2ra9BuY3tWVg9pVEpPhiAK6MVmGQ1iC1OFra1-wImDXPL9CrXi_XrYND4zCRJpqDL6K55A38zgCfxuVAKFSwF7O1D2-OsOkVw3__N0vYpf_nEZNewNL5QgKocw1-ml1BTTQL1yFFode5is7UUO2Aw3HNKkbm4ZB1cbkTlHjA1xqNaWv0yZ-txkRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=LQrHyB0TZvQSTVxNadZMvI9WENGwQY97x6MhCiiZhJqP7MpBPF_aLq7YRwUYLsI0dqudXn5u-38d0t8-Gv2L5HHIciJe0PR-r-tE23TL1xdxnD53-z3e1hG0QYlYi4TmTaAQNf7SI838-03FLB58qgdHvoNjza2ra9BuY3tWVg9pVEpPhiAK6MVmGQ1iC1OFra1-wImDXPL9CrXi_XrYND4zCRJpqDL6K55A38zgCfxuVAKFSwF7O1D2-OsOkVw3__N0vYpf_nEZNewNL5QgKocw1-ml1BTTQL1yFFode5is7UUO2Aw3HNKkbm4ZB1cbkTlHjA1xqNaWv0yZ-txkRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هواشناسی یه بالن فرستاده بود هوا تا اوضاع هوا رو چک کنه که یه سری نگهبان معدن فکر کردن پهپاد آمریکاییه با برنو زدنش
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.9K · <a href="https://t.me/alonews/150942" target="_blank">📅 16:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150941">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
دقایقی پیش یک هواپیمای ترابری سنگین نظامی روسیه تو تهران فرود اومد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150941" target="_blank">📅 16:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150940">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نیویورک تایمز: کمک خلبان پرواز فلای دبی ارتباطی با ایران ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.3K · <a href="https://t.me/alonews/150940" target="_blank">📅 16:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150939">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2a27e50f8.mp4?token=LeZ4XJ6a0y2WQ7ZqAYK3L0CHTdaPqrMqrX8TofKMsKSpG4uYQZkzWPkssO-mjFgBnpkUDftRniXiqXvlW6dJbJ9nssI9N6PBjvvqC4pV4GYcpL8hUx4Wg5TB1D-Zmd6BsMTfNr0V9_psriLmCGOtMJl_LvjKFmnix6C4VFRSOgLxeDFGxiw0NEvJJOD12DgV-NkSQCFFLD338LOoamh6u0c30Z1xQWMmzJxRJ3G0nmei3UG95H3-5YoUuohssgmp1bdbljdii9UzDdNXHINAdOi-wRnzWPrvzrDqjgZXQD6s7sl-H4chys8ddFmiwyKNKWC_OBh8GLtL_YAynF5j5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2a27e50f8.mp4?token=LeZ4XJ6a0y2WQ7ZqAYK3L0CHTdaPqrMqrX8TofKMsKSpG4uYQZkzWPkssO-mjFgBnpkUDftRniXiqXvlW6dJbJ9nssI9N6PBjvvqC4pV4GYcpL8hUx4Wg5TB1D-Zmd6BsMTfNr0V9_psriLmCGOtMJl_LvjKFmnix6C4VFRSOgLxeDFGxiw0NEvJJOD12DgV-NkSQCFFLD338LOoamh6u0c30Z1xQWMmzJxRJ3G0nmei3UG95H3-5YoUuohssgmp1bdbljdii9UzDdNXHINAdOi-wRnzWPrvzrDqjgZXQD6s7sl-H4chys8ddFmiwyKNKWC_OBh8GLtL_YAynF5j5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حوثی‌ها خانه رئیس پارلمان یمن را تصرف کردند
!
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/150939" target="_blank">📅 16:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150938">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7e5a3bac.mp4?token=r_Ks3rA6mKIVDfERdf1Zlf1KpbbV2S-KCSJOaHGVX3nJ67k5naPDXppryLEDPK0N87s2htrAIW6dG8RW5Yw0jCAzdINt6Af0Ibgpaia98uMMFaNwzJRnxyKaqPJA3dhlu-bQP6anZke1M8bSM-I6Y1IBnK4VRcoORiNbM9Ax69dB1ox0jvQ0Ym8nWA3p1Jhpx-5Ittuf6xNThKT1XC6dzC_xE681OtY2A2HLvZiJv5pXLlub14mk2lsm7iNog4yxk9VtFFhP5EuD3NHa2g0eHi6NOE6T4bIPjGDcvTQWmu7bJjoX1QCd7DcTnv-suuHyi-Y9OWbep8_3O_Bgi94U_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7e5a3bac.mp4?token=r_Ks3rA6mKIVDfERdf1Zlf1KpbbV2S-KCSJOaHGVX3nJ67k5naPDXppryLEDPK0N87s2htrAIW6dG8RW5Yw0jCAzdINt6Af0Ibgpaia98uMMFaNwzJRnxyKaqPJA3dhlu-bQP6anZke1M8bSM-I6Y1IBnK4VRcoORiNbM9Ax69dB1ox0jvQ0Ym8nWA3p1Jhpx-5Ittuf6xNThKT1XC6dzC_xE681OtY2A2HLvZiJv5pXLlub14mk2lsm7iNog4yxk9VtFFhP5EuD3NHa2g0eHi6NOE6T4bIPjGDcvTQWmu7bJjoX1QCd7DcTnv-suuHyi-Y9OWbep8_3O_Bgi94U_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سخنگوی دولت اسرائیل: چشممان کاملاً به تهدید تروریسم است
🔴
اسرائیل در زمینه تروریسم با چشمانی کاملاً باز عمل می‌کند.
🔴
ما می‌دانیم سازمان‌هایی وجود دارند که تلاش می‌کنند کارزار انتخاباتی ما را مختل کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/150938" target="_blank">📅 16:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150937">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JDJSQfg8wJ8xMJwONzp2VNLsxehCEbVMpAkHYmh68ycYd3IUVXNT9ssXaX2UyvyKySKcbxTTWMxIy_by_mAaA1KtdyQl-CBNYTqI4z9jTiTQg83XoxSkz3MlZ1_LRkKFRSn1BzIM_j5p5JoxqQF2Rr0gtJ4V7xMjqATUtj7GBOb5rApveYLLA71636fD-SGb-UOOqqpSZQd92_M7i_cpLJxsJ8H8XCSZLnAsf4QuLBs-50-1KaZyJLeuAdjSdJJz5FseowonPnVuGyPQI_qaxatWChNnTmtuP-XGnRoOBzPtxc68fNLSg2P0Ipmhk2I-diqh3O3JEsHxjg742v7eUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : او چقدر دستمزد می‌گیرد و از طرف چه کسی؟ او در تمام پروژه‌های من حضور دارد و اعتراض می‌کند.
🔴
افراد دیگری هم هستند که دقیقاً همین افراد هستند. این‌ها معترض‌های مزدور نیستند، درسته؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/alonews/150937" target="_blank">📅 16:13 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150936">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fb1eiSWKRAAW9k2vLXSfkVQkjqgZeCMHBnew1g-wZm7prjwJorw_b31eXibYkjHu5VtDXFLLHt6Ja9Pt-ejiQ4NMZ_Wz7sNq-ayt3Ji1a9e0viv_o5kztD8xiTLXVIOH1resba04RKgPs1aQQRq792eLDp96of83taFlSLxePMI8_QF-ZCaG93Yg7IRX0tuGaBd1g-9VQyuJV8Yi_xGrE_mLn504ggDpffkggHozY1F3V1kvYE0Bg-BHn0dKOvfMgucrcO2g-j0mLL4GPIQPjgYLXJd13gpgs8AV1KwU19GklOdmftyRf8CFC2MyH8LQ_8Url63kdXUscuMGxPB0YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از ایجاد یک "نیروی فوق‌العاده هوش مصنوعی" (SIF) جدید در سطح فدرال خبر داد.
🔴
ترامپ گفت که این گروه ویژه، تلاش‌های فدرال را برای حفظ رهبری ایالات متحده در زمینه هوش مصنوعی پیشرفته هماهنگ خواهد کرد و همچنین بر تعامل دولت با مصرف‌کنندگان، گروه‌های ذینفع، گروه‌های مذهبی، ارائه‌دهندگان زیرساخت‌های حیاتی و شرکت‌های فعال در حوزه هوش مصنوعی نظارت خواهد داشت.
🔴
این "نیروی فوق‌العاده هوش مصنوعی" شامل آقایان جی کلتون (مدیر سازمان اطلاعات)، اندرو فرگوسن (رئیس کمیسیون تجارت فدرال)، امیل مایکل (معاون وزیر جنگ و مدیر ارشد فناوری) و اسکات کوپور (مدیر اداره مدیریت و بودجه) خواهد بود که مستقیماً به ترامپ و سوزی وایلز، رئیس دفتر ریاست جمهوری، گزارش خواهند داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/150936" target="_blank">📅 16:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150935">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
اصغر فرهادی: آمریکاییا خودشونو برتر میبینن و اصلا دموکراسی ندارن
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/alonews/150935" target="_blank">📅 16:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150934">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/muZGp55rbL4yM-8mLIBMSKC9hjosKW4o1NXshKftu4s4cIvYltk3nhBVlOs9nCbZoRFLm7FCpb0Q2NLkliZo1rAk6H5d8HoKnjqncURqgbfRB1PRCm4aqGQUrsjPtjiMytioDizf1Hy5ksHGwmiuUCOnsz3-GKpIn3B-YutAXc0g-ba7irOg-cmfMb7kdLahaZ2xymojIE7MYsnZQz4Lnj9kPIgUt5b-IrXp8gcprrhjBYInIOpX_f0ZOsZJHaaZI8W-Wly34rVoa4L8c4ldAdr1zbmiq648ubzOjhoNzQptFXIWAg49A0dBipRdxUfiQ9Nbye7vx2_ecQ8_r2ObxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا، جان کوال را به عنوان نماینده ویژه جدید خود در امور گروگان‌ها منصوب کرده است. پیش از این، آدام بوهلر این سمت را بر عهده داشت.
🔴
ترامپ گفت که بوهلر به عنوان مشاور ارشد، "به انجام وظایف دیگری نیز ادامه خواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/150934" target="_blank">📅 16:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150933">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
گوگل دسترسی کاربران رایگان جمنای را محدود کرد
🔴
از ۹ اکتبر (۱۷ مهر)، کاربران رایگان جمنای تنها به مدل Flash-Lite دسترسی خواهند داشت و مدل‌های Flash و Pro برای آنها حذف می‌شوند
🔴
مشترکان AI Plus نیز دسترسی به Pro را از دست می‌دهند؛ کاربران AI Pro و Ultra همچنان به هر سه مدل دسترسی دارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150933" target="_blank">📅 15:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150932">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=pZxM2pNBJjem7sA61xSB12S5OsKKSc-Mjt7MSvYa0fzFVdvSkNEmU67-z4SED77NDUYDQcVU8PSG6U7mly3vEie_ZEjhtAgvL5CMmvoK0puea8sw83mjqVK7i9i9khgmi12ei5At62T5jDtYTLyVmlWbDEzr2e4u5PWc2nbrpQmUD2t2T17LO3Kd1H5ZllM0AqVjBF90-_YiRJX90CESPWR7KVRn2BNYqrxAB7qM5wNMijmhLyWqjOEsrRjxzVJLqc6e5KkcgSiEnJRVGNN98rx1pr2AorRdPe5R3z8rkAsBrcCyb2XIvAZagMl5eOmxktc9zWuR5u9aj50_L5k6HkiaNQ0uoWAsMtJm4x77huiq9hDxTNW5_pjx2dByWuks_AG2tAvG5PA8et1_PK3Snno4E2RUeg-VSWRt7zbXwyGyPuKp2N15tmRQdPm57hpuyw_YXhoCU2iZqZHrYPF5HfnAanxKBS4DFJxgUxyRG7MxSQ0dy0-didZ0UDhwE77lpX4NCU8x6VIb8rfLU-PG9Z3AKBAmtwxrgAPeHPqqOgU9k3tMhCHRh2hM9tRDMhgyrQHsgChrc54yvjhzSgNMU3Gcqe2pYwjVikXKmPzzy8_CXweDqrjgE4Myo_ebYAaqKBYV2IroYj1uYJFp4xBtmFdT591pVUf4qXH1nk4L6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad9e96757a.mp4?token=pZxM2pNBJjem7sA61xSB12S5OsKKSc-Mjt7MSvYa0fzFVdvSkNEmU67-z4SED77NDUYDQcVU8PSG6U7mly3vEie_ZEjhtAgvL5CMmvoK0puea8sw83mjqVK7i9i9khgmi12ei5At62T5jDtYTLyVmlWbDEzr2e4u5PWc2nbrpQmUD2t2T17LO3Kd1H5ZllM0AqVjBF90-_YiRJX90CESPWR7KVRn2BNYqrxAB7qM5wNMijmhLyWqjOEsrRjxzVJLqc6e5KkcgSiEnJRVGNN98rx1pr2AorRdPe5R3z8rkAsBrcCyb2XIvAZagMl5eOmxktc9zWuR5u9aj50_L5k6HkiaNQ0uoWAsMtJm4x77huiq9hDxTNW5_pjx2dByWuks_AG2tAvG5PA8et1_PK3Snno4E2RUeg-VSWRt7zbXwyGyPuKp2N15tmRQdPm57hpuyw_YXhoCU2iZqZHrYPF5HfnAanxKBS4DFJxgUxyRG7MxSQ0dy0-didZ0UDhwE77lpX4NCU8x6VIb8rfLU-PG9Z3AKBAmtwxrgAPeHPqqOgU9k3tMhCHRh2hM9tRDMhgyrQHsgChrc54yvjhzSgNMU3Gcqe2pYwjVikXKmPzzy8_CXweDqrjgE4Myo_ebYAaqKBYV2IroYj1uYJFp4xBtmFdT591pVUf4qXH1nk4L6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رشاد العلیمی، رئیس شورای انتقالی یمن (PLC) که از سوی عربستان سعودی پشتیبانی می‌شود، آغاز عملیات نظامی گسترده در تمام جبهه‌ها را برای بازپس‌گیری مناطق تحت کنترل حوثی‌ها (أنصارالله) و احیای اقتدار دولت PLC در سراسر کشور اعلام کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150932" target="_blank">📅 15:50 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150931">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
اگه از بازار جاموندی اینجارو داشته باش
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/150931" target="_blank">📅 15:49 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150930">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
ایهود باراک، نخست وزیر اسبق اسرائیل:
نتانیاهو در حال زمینه‌سازی برای آغاز جنگی است که برگزاری انتخابات را به تعویق بیندازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150930" target="_blank">📅 15:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150929">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ilkw364O7cQQUSS6Y0eDoldZ-FNUuqznUV8MOPkTaGpMleXBwnND3kE37i4SRqYnD-B4AV_rHMLTJ2FInOidPrHEIes8aJoyIr1zQspx4YNShlynF6r-Q0mvL67wvtRsQXEUcAVBMi5-0l9S07yT1lzwk00yBW2cgJ-PbCF5xITIqN6oKfHUOMFZjyof15RAkCZP73sIhfOh3yzXtA2Yk3HwrjYaQgXKI5my7QlDSMO7Jvl8WAk5R2L9YO8lVKH0QeqBJ6ojBxfJh3u1F5c73dkHHzjw77ct8hQFTsceoEFNFWgjKhbE1hN9Vgue1bNRbQmR0pEqnIt0OTCeyl4bCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اولین برف پاییزی بر دماوند نشست
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/alonews/150929" target="_blank">📅 15:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150928">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
کوچک‌زاده، نماینده مجلس : مملکت رو دارن به آمریکا میفروشن. من گفتم این جنایته. به خدا اگه از جهنم نمی‌ترسیدم، امروز خودم رو جلوی بانک مرکزی آتش می‌زدم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/150928" target="_blank">📅 15:25 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150927">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e6ff2766.mp4?token=PitSHUvJYAQQF4MuAq9Ftv-JwLs9S4haJWp4mubmBvDzvMoSFXU_gRyF1mWlB6ti_hczo0xfa8DBwpZGn6V_yS6LYZPzAz-flBh-m7F9aVSJGCPGp6FUXqt_YK1-72mQBUw-GRxa6dXJSGuIZDh6APcyt8hmaoW4wl_xIuSdCwUIgB-rvqHxSn3H2OtL46bi_F8n8ouxY2phgeV-JBq1THPsSdo-AMKWPWSKKC-6eM4iMsgOxBqoujBr_HxFdBADZ8J378vg1huaGHoU4YTvb2dPjPACc5BztGe_faSHxkxzZ4pse_SFdaKF4Hx668UROaSJa18vTGIZVNinBeaE4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e6ff2766.mp4?token=PitSHUvJYAQQF4MuAq9Ftv-JwLs9S4haJWp4mubmBvDzvMoSFXU_gRyF1mWlB6ti_hczo0xfa8DBwpZGn6V_yS6LYZPzAz-flBh-m7F9aVSJGCPGp6FUXqt_YK1-72mQBUw-GRxa6dXJSGuIZDh6APcyt8hmaoW4wl_xIuSdCwUIgB-rvqHxSn3H2OtL46bi_F8n8ouxY2phgeV-JBq1THPsSdo-AMKWPWSKKC-6eM4iMsgOxBqoujBr_HxFdBADZ8J378vg1huaGHoU4YTvb2dPjPACc5BztGe_faSHxkxzZ4pse_SFdaKF4Hx668UROaSJa18vTGIZVNinBeaE4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئویی از پاکسازی یک سنگر نیروهای روسیه توسط نیروهای ویژه ارتش اوکراین
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/alonews/150927" target="_blank">📅 15:23 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150926">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
نایب رئیس مجلس: وزرای پیشنهادی اطلاعات و دفاع تا پایان مهر به مجلس معرفی‌ می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/150926" target="_blank">📅 15:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150925">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
تابناک از احتمال بازگشت گلشیفته فراهانی به ایران خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.2K · <a href="https://t.me/alonews/150925" target="_blank">📅 15:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150924">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا از حمله موشکی سپاه به یک نفتکش در تنگه هرمز خبر داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.2K · <a href="https://t.me/alonews/150924" target="_blank">📅 15:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150923">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnX3DP-Mymf6UrK-N7zK5ARQJePVYPi4EwJfrXFUmJZpewQjo-1GMtIqBTgQ5nKNsDnKIs9OQAo5Q7H4DYSXThAjafWyjlIqC6XpxivmWxWElCCVzCT7RSslAz_cN3mSZI6-5t1UA4_ekiCXLEOQvg8VhpgUz-k1yFqv8NTTHcBiQkSIYZTE24hgULAiD9_mDmVVAXyCO6mG3tVsvLv_AcDZcdDJyQhJgflpcquyo3GumDT95-mJ6w_-V40RekAKmprKV9VBOgtiIv-j6FcskYismBHyHT1gp8v5b3Najx2OE73nalWXT3JhjFrTLPkwep4SW8dwAXYV3HJctguphw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حوثی ها کنترل العزاعز و المنصوره را به دست گرفته‌اند و به سمت الاصابح پیشروی می‌کنند و به حومه شهر تربه نزدیک می‌شوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/150923" target="_blank">📅 15:07 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150922">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
کارشناس صدا و سیما: تو راه قله‌ایم و کوهنوردها میدونن که نفس آدم میگیره تا برسه
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/alonews/150922" target="_blank">📅 15:04 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150921">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
نیویورک بهترین شهر جهان در سال ۲۰۲۶ اعلام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150921" target="_blank">📅 14:55 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150920">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a486bfc79c.mp4?token=CP43feDyzLzhYcSyMqyUipgY7gfpbqNMaFIN2SnB3TloNhqr4Qyq98rDmqcDsIjnK23DCJ1Vt3ioClPbJ3E13oq-kt6c2eoPOCJqkSxPrdBKDv-NhCQ6FiNjC7bvycS1wJt6n1_qikdIZs28GOJlJmqQX_5m6c4C7uB1Ms6tYsI9iImVKUucT-fHJl7WqvCxsxt-IDZEsGqf6oSvlcs9RBoWhP3kAPW_55pq-NkkKUq7EaSWef5M_Z2j66YQCBA_YxaRUr6EBEJzn0ajOj0-XUy8ns5hANVfBsGcIlF0p9U8DTjJcWKb6N_OG3Y9yrIvJmh0a8HRycp0nQZKJdmoWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a486bfc79c.mp4?token=CP43feDyzLzhYcSyMqyUipgY7gfpbqNMaFIN2SnB3TloNhqr4Qyq98rDmqcDsIjnK23DCJ1Vt3ioClPbJ3E13oq-kt6c2eoPOCJqkSxPrdBKDv-NhCQ6FiNjC7bvycS1wJt6n1_qikdIZs28GOJlJmqQX_5m6c4C7uB1Ms6tYsI9iImVKUucT-fHJl7WqvCxsxt-IDZEsGqf6oSvlcs9RBoWhP3kAPW_55pq-NkkKUq7EaSWef5M_Z2j66YQCBA_YxaRUr6EBEJzn0ajOj0-XUy8ns5hANVfBsGcIlF0p9U8DTjJcWKb6N_OG3Y9yrIvJmh0a8HRycp0nQZKJdmoWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ثابتی و شهریاری تو کره باستان
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/alonews/150920" target="_blank">📅 14:45 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150919">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fecd2cc8b.mp4?token=okZ05fIhVyHD_ePpMoSb7AqHL9HwUXA8gMbo1-K8qx250EUQuMRKcgFbWgkOYqpEJS6Y12KgmwgnJ5gLLzIfPdlkSH7qwdqu10rU4hqWLn1p5m4naAV0rNIDg4tuduUy1iacu53TWLwo5iaazvizJtT4PWq0KmpdnHXH4N4e3X_TSQ2-wvLHcRIsvebxmrRhdpxsEG-yJVtqxQP6j5_EAn2qEdsF7bZjgC-C_JHqOxQ69LqTk7en68ZvngP4aKhWGn0drmgVE1tvQXinnK7g5chTmxUKmXjXYsg3TY9aW3yEqzYLRnGyJ9ymu8UOGEbt5PcHgiIU3RLF6YvZage5Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fecd2cc8b.mp4?token=okZ05fIhVyHD_ePpMoSb7AqHL9HwUXA8gMbo1-K8qx250EUQuMRKcgFbWgkOYqpEJS6Y12KgmwgnJ5gLLzIfPdlkSH7qwdqu10rU4hqWLn1p5m4naAV0rNIDg4tuduUy1iacu53TWLwo5iaazvizJtT4PWq0KmpdnHXH4N4e3X_TSQ2-wvLHcRIsvebxmrRhdpxsEG-yJVtqxQP6j5_EAn2qEdsF7bZjgC-C_JHqOxQ69LqTk7en68ZvngP4aKhWGn0drmgVE1tvQXinnK7g5chTmxUKmXjXYsg3TY9aW3yEqzYLRnGyJ9ymu8UOGEbt5PcHgiIU3RLF6YvZage5Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
عرزشی‌ها بعد از ۱۰قرن حرم امام رضا را از یک مکان مذهبی به یک مکان سیاسی تبدیل کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/150919" target="_blank">📅 14:38 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150918">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZNSyXGzd2qhjTltKX-jz2k0YPqhWJ7g_Cy9GiFkzIFvohOt7scegyaFrcUd-QAtuykf5oQo9TylrS1aYO4gANsxY4IijzFMwhv_S8YBwsNEcwkC_LA1x5qrNpqZfAnxntn2adUWRBGIQPWem43aQ6qo3dvbiWNtUZ1_XMYCtNqQbDOQ7wVAczjnK-i5c4-Chh93Ca_llk81yXeHAtqksf4uNIA1xp6wtId_dB1PgtOIA1XMlstAH8YjYGtFnzOGrKQjX_e7J8Bq6gQEls7rQwi4NWkZa_1hHraoQE71FBxmCbHX4XmvBxAtjDzQCQJESIcIVRYB6U3ZnZu5uWGgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هزینه اجاره یک سوپر نفتکش برای حمل نفت از خلیج فارس به خاور دور به حدود ۱.۳ میلیون دلار در روز رسیده است.
🔴
پیش از آغاز جنگ، این رقم کمتر از ۵۰ هزار دلار در روز بود!
✅
@AloNews</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/alonews/150918" target="_blank">📅 14:35 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150917">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0558dea8d7.mp4?token=Obk2i5VR-DKNWBIQvCJK_oJn8bCPJHqiTnW1nCB9QGr8Y-U1xZNwjHNTuBBsuUuyPpUQ1BoYne7JtfIvEallsH-cIuZiaGu_jsoRDBjCZy7ISQ3s3JI79QpFCzB3tNwrL10UBjSbohSRqey-afMoEPXVl-m2C6OeQKMnuYJu6WdcYr2yR7NKVhUiPOsI-INvoh9h_F3by4dXPMS-b_qqU-xqLwQftR2lvMqP5Ug82flO_lHXJpCDvCiXV_EebacGAVlsAy3pZTplXuhbQfMLPQi4W9SNnDFWs5FA7lf2ELRg6QZsyGyftLiRL7zZ-bEdcdRJWu1iSN47ALBqrXjqwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0558dea8d7.mp4?token=Obk2i5VR-DKNWBIQvCJK_oJn8bCPJHqiTnW1nCB9QGr8Y-U1xZNwjHNTuBBsuUuyPpUQ1BoYne7JtfIvEallsH-cIuZiaGu_jsoRDBjCZy7ISQ3s3JI79QpFCzB3tNwrL10UBjSbohSRqey-afMoEPXVl-m2C6OeQKMnuYJu6WdcYr2yR7NKVhUiPOsI-INvoh9h_F3by4dXPMS-b_qqU-xqLwQftR2lvMqP5Ug82flO_lHXJpCDvCiXV_EebacGAVlsAy3pZTplXuhbQfMLPQi4W9SNnDFWs5FA7lf2ELRg6QZsyGyftLiRL7zZ-bEdcdRJWu1iSN47ALBqrXjqwzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
به صدا درآمدن آژیر خطر همزمان با دیدار زلنسکی و مرتس در کی‌یف
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.3K · <a href="https://t.me/alonews/150917" target="_blank">📅 14:29 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150916">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
بابک زنجانی: وضعیت گاز خطرناک است
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/150916" target="_blank">📅 14:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150915">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
پشت پرده ترسناک دلار
😳
‼️
خبری که بازار رو ترکونده
👇
https://t.me/+ViT7_yfzcKRmOTNk
https://t.me/+ViT7_yfzcKRmOTNk</div>
<div class="tg-footer">👁️ 70.1K · <a href="https://t.me/alonews/150915" target="_blank">📅 14:18 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150914">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
کارشناس صداوسیما: تمام اتفاقاتی که داره میوفته از نشانه های آخرالزمانه
✅
@AloNews</div>
<div class="tg-footer">👁️ 73K · <a href="https://t.me/alonews/150914" target="_blank">📅 14:15 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150913">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=kfJzraNLr4z7iv-5NiCPK83lZkTy_pR468lNqICl5TBGk94mkZWASDaBttNY0fxfIxDPiMGN0cTsbPl7zDf246qDubxIduReZ3gQotROssKiHrweHGSS2nt8bBs2B4REBCLrpdxxHuYI6D9beZFWpbC870V4MuOapmEQLll75XfpSNkuowCKBvq5IYpAWpt1EmYNx1kHSKuSnvZBI0UtIlcTinjdwqP7t7YVJWtEnZcftDfBqm1KADstXQttEpF6WZwrG3QdEWy6C8yx4dq-FqjsRmTpJnyxqVFGy_t88CWMxS2801LrzCaTA-vZL2DSbyHzzS2dXynYjBidz89h722SjaTQtrcTC5I4hf2gKICE-P0sY_AFpSjLSm1sXM1y8h0ERS7WCQENp3fHO4jt7Tf14NLDtTZEqKgkH671CUE5SsfgLzgUN5S1a91ibB2HF2mDLPmTp53SXnjxuqu5N7gQDyRrD1jK1EorLB0N2mXXLQkrHSx4ejJvicibhxq_D0wEXCElqx_r4yhH_G2cUlMFsIsbOx-fXNF866msaz93nPwcroL2opALaQ5DNYeBdRWF-KPIbJWjkf18LKIr2FftWYi36ZaDoOh3GFHCLnIc2P54BTaGrFvEQeOlTllgeGfFqPLrJZnrqVdTrgshGpXgRMhBY6zyiClbnto8NDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e464e1d963.mp4?token=kfJzraNLr4z7iv-5NiCPK83lZkTy_pR468lNqICl5TBGk94mkZWASDaBttNY0fxfIxDPiMGN0cTsbPl7zDf246qDubxIduReZ3gQotROssKiHrweHGSS2nt8bBs2B4REBCLrpdxxHuYI6D9beZFWpbC870V4MuOapmEQLll75XfpSNkuowCKBvq5IYpAWpt1EmYNx1kHSKuSnvZBI0UtIlcTinjdwqP7t7YVJWtEnZcftDfBqm1KADstXQttEpF6WZwrG3QdEWy6C8yx4dq-FqjsRmTpJnyxqVFGy_t88CWMxS2801LrzCaTA-vZL2DSbyHzzS2dXynYjBidz89h722SjaTQtrcTC5I4hf2gKICE-P0sY_AFpSjLSm1sXM1y8h0ERS7WCQENp3fHO4jt7Tf14NLDtTZEqKgkH671CUE5SsfgLzgUN5S1a91ibB2HF2mDLPmTp53SXnjxuqu5N7gQDyRrD1jK1EorLB0N2mXXLQkrHSx4ejJvicibhxq_D0wEXCElqx_r4yhH_G2cUlMFsIsbOx-fXNF866msaz93nPwcroL2opALaQ5DNYeBdRWF-KPIbJWjkf18LKIr2FftWYi36ZaDoOh3GFHCLnIc2P54BTaGrFvEQeOlTllgeGfFqPLrJZnrqVdTrgshGpXgRMhBY6zyiClbnto8NDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حضور بیژن مرتضوی و همسرش در دربند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.9K · <a href="https://t.me/alonews/150913" target="_blank">📅 14:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150911">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkVha8_GWs6ZG7Tz3mKlOmje8YvmCv1b4oWqkzdfxAv4ZltWQpI--8-M9x2K-H0tc86PTRJbsfE741_PgM3YmEo9ZVoam2kxU3flWwHQgOb6rKULilZL1Hl8h155WV93EIldIB6i5uUfROpShx6WUc56z_eoWRE71bOnkPJyEVlQUCo1wW-dEX1t7pc9WHeNYVsLhz7qMquxLmIbNAlRdJ5C54yHFbloqCXj_IDRDhISKV4XaPc3okbPBwNIq3UCN3RifIik8oEdpBEBET8HMRB8HOdEE0A9z70UFa6wJBjxFKe9CMs4PPFRCSBhzk27VUOJLBdC3uA_wUP3BzQKJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای حوثی به منطقه العزاعز، نزدیک تربه، رسیده‌اند و در حال درگیری با نیروهای وفادار به عربستان هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.9K · <a href="https://t.me/alonews/150911" target="_blank">📅 14:06 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150910">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
قسمت ترسناک ماجرا اینه که با وجود خبر تزریق بانک مرکزی و جو امنیتی و بستن صرافی ها و عدم نمایش قیمت، بازار بدون واکنش به مسیرش ادامه داده
🔴
قبلا این کارا یه مدتی موثر بود...
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/150910" target="_blank">📅 14:01 · 12 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
