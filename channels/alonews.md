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
<img src="https://cdn4.telesco.pe/file/oTF_naOUns1QMXRzE2BIOHta7yf28o7ulF5EO_D-BOdrex52rFOqMkHqEdohTTJBj82UcrfMsq6khu0qPlXUHkebJWLX0GZf8k1zIfmdjXFsJTvRt5-wU_d4ZNn2V5mBiTaQEY4hL9ZfdSqQCL3VBgfgCggL1_tIVoy5hZ5X5ZxOIg99AYGWHWF6K91fGSgjbLXoXxEysZarV4mYY1xbHiqbefNRSW6vG7h3vu_eaQidqoYZHkEhT6vJCgOV0N13Uy7TKU1wHba_5NXRQEllpjJ6DjRPtMOivGY5XzOL5ADjob4U5a__tZ7aoUlNqx5wvdp5LF-FrLcpi6Vz_Wjg8g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 968K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-07 07:44:06</div>
<hr>

<div class="tg-post" id="msg-144334">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
العربیه گزارش می دهد که گروه های عراقی در حال برنامه ریزی برای هدف قرار دادن عربستان سعودی در ساعات آینده هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/alonews/144334" target="_blank">📅 02:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144333">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IAoF2oWiNgyCWjfa2ZrySVpzr8T7noDi6H0X536CJhsG3HFPMNLxq3QumxLTqgKIiOetoNK6sSqq9ELE7DdgnSu__FKtWZ9F6ZWECje8I169kGZ_P5KiARguX8DJw98Qqq91Eo5BZW-5Zehq-B5Sk3Dr-Xm6ib0aDt0u2W453ET1qJBuaupC-1k2-qRjcLDwtuUsS0nkAXCPB_0h7FJC5zDe84N5uAqo0Zq6NLeMmE6el_ux-0J2ZiFA_hcVGZxQKKiMAbc0NuWcju7sJKQvaQSyFPW0HgR2QhOdPRxAUatEDdujef2DO5oy7Ta93Pfcwadfi0EdUltqgSELz82u1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون حملات به جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/alonews/144333" target="_blank">📅 01:52 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
بمباران توپخانه‌ای اسرائیل، محله "دواها" در شهر "کفر رومان" واقع در جنوب لبنان را هدف قرار داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/144332" target="_blank">📅 01:37 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iawpROs6zYIYVRJKbAgqyd9MOovCsOCJMfcAhKM2sy-ruoOagqHGTBY_zvFDvsiDSnQfV2mcuJiHgSvmFG2TSM6Rls8AjzajSFV2Gd_kXzcLlATmfVJcHT8VRAc3mw28MI7PM83tXt1_HZ0YG7ducz2o-9arCFDL2l9gnJqGqzeY6iB6o5Sqsjfx1_r4Pj3nfl6_8xoofZiHvxc6LFi_3iRk8J59IKvg2RC0S2xUOfow0MapFyukkf_iy9vHwvJGO0YRAoptrscOmXo2xt2-tA6QPU6RYYYgtU72Ni3kfaVzPU_7YrssXTMREkBZWdxkK0Yu8OII-teRO1HWFGfiow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی: گرونی چیه بابا فقط انتقام رهبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/144331" target="_blank">📅 01:24 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144330">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_sKby5Nx617oe76IJBwZ8JTva-tXNdVG8AlR8v3N0U_AAFBQ0UGyhDrVJIo1SDThhR7I5X3FkN7Xq1k6ejIB-Jz_e2lYxlz5aDHuOFsqcZN6t21uZA_imKlELUTixMGg6fp0f4hsjnjz8HxGMl-EZDj2vIjYTCgYzZhV5yddeqESry-vnYOfZoo7QqS_iDwkOGagwkVZgoPBMSTJfmgZwS8HbHVRseiCBvVzN1mNsdAahch4D7D2Vnry21jjKNLuwsZCGy1KTdGGtlKq-BEyMC3Pb2ti5toJmLVZJJX0Nj2A12aRGuPGszOGWN28GWTAPX7LeNgsLG3F-o-K9MLjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/طرفداران پهلوی به خونه علی کریمی حمله کردن و کتکش زدن
🔴
اولین فیلم از دوربین مداربسته منتشر شد
🚨
🚨
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/alonews/144330" target="_blank">📅 01:13 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZjNV5cxqv7JYqcTSMFuEGRk0DkvIapjn3u9ipIkeNFVdqHJZDXBtAwRjhKCogSpGdoitTHynqQdr8LTjtaB_bab_SmHVumxwHYIi_EveG6MiyGLcJcXu2vfWx0OF0JECpQn-CJRncDr6UW1VbAv9x8KRKB8cVgaaoKX9D05HyAqmyVLFbUB1W7u0zvq6esjEPasHNNbpIr9UpKbN8WKK_DVr6t_k9k7UC-ASrKMjKif6oo9TnRCbmGuWtG7Td9ZMakDwPdxMCivJ_dz6_5Olpro7OaiYnJ0eimg4R2h7VWWJwMbcTjyq-SSzC3yYWLzku2f-2MHR8YKZ6N2ohInng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پزشکیان: پول نداریم، بدبختیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/alonews/144329" target="_blank">📅 01:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه کانال ماهان رو بخون هر خبری درمورد تورم و گرونی هست اول اینجا میزاره
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/144328" target="_blank">📅 01:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
بی‌بی‌سی: آمریکا در حال برنامه‌ریزی برای قطع کمک‌های نظامی به نیروهای پیشمرگه، که متحد اصلی آن در خاورمیانه است، است. وزارت دفاع آمریکا به رهبران اقلیم کردستان عراق اطلاع داده است که برنامه‌ای برای تمدید توافقنامه ارائه کمک‌های امنیتی به نیروهای پیشمرگه کرد ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/144327" target="_blank">📅 00:50 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144326">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
باراک راوید: بیش از ۲۰۰ شیء شبیه مین از مسیر اصلی تنگه هرمز جمع‌آوری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/144326" target="_blank">📅 00:29 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=STK_oBYvh1C4A-iciMXT4JUhMMZrAGSOf25hlV4fFLFiiFaEnk_9_LBPVwWlT2hEyL1aaz0y5OmCoDb1mvcQm7wfxQE5mBCXK27079AGDRspgek9m6A_9VkhZVQqNcSNF7CYHzZIbles8w2Dr221oid6CpcB2bvtnqAwCEMGP-jOt6YsVuiDpgh9ERxqo_dsIIXFJFYB-zqIqqh3rHyQNKTqWY5JD51BvfhQ4Lrc2yMcg6Gl_MsidQynxVBmGhcTjvzQMt1TXGQ-Vb9cbl3dJrPF-rSajMma5HQlt2sWJevdRsIL-9Er3UJ_AjVXmotT5cci7I678tPdLdNTS9xUjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572fe77a52.mp4?token=STK_oBYvh1C4A-iciMXT4JUhMMZrAGSOf25hlV4fFLFiiFaEnk_9_LBPVwWlT2hEyL1aaz0y5OmCoDb1mvcQm7wfxQE5mBCXK27079AGDRspgek9m6A_9VkhZVQqNcSNF7CYHzZIbles8w2Dr221oid6CpcB2bvtnqAwCEMGP-jOt6YsVuiDpgh9ERxqo_dsIIXFJFYB-zqIqqh3rHyQNKTqWY5JD51BvfhQ4Lrc2yMcg6Gl_MsidQynxVBmGhcTjvzQMt1TXGQ-Vb9cbl3dJrPF-rSajMma5HQlt2sWJevdRsIL-9Er3UJ_AjVXmotT5cci7I678tPdLdNTS9xUjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: به دنبال این هستیم که برخی از ادارات را دورکار کنیم
🔴
حقوق پرسنل را کم نمی‌کنیم اما مصرف سوخت و انرژی ما کاهش می‌یابد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/alonews/144325" target="_blank">📅 00:18 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
کی‌یف بیش از دو روز است که تحت بمباران مداوم قرار دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/144324" target="_blank">📅 00:09 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
پزشکیان: واردات و صادرات ۲۵ تا ۳۵ درصد کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/144323" target="_blank">📅 00:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پزشکیان: با آمدن محسن رضایی، در حال نزدیک شدن به یک زبان مشترک در دیپلماسی هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/144322" target="_blank">📅 23:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144318">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V-JbjFCFchBjABKZPVzp3c_eQQGhXf0IkEOTwyUFSfVliT5Q5QUIF9TKXRwW-H4ESWKba9w3EWq5pRyfc0ax5BA7cqd7tTy4jrQzSO1aaWJBGLB-CQ11vl5_tBq_g-77dR_EszBgOifElxIgLrrcP-iU6QyxhhDV3Y2jUtWCzgzLW768dSCPfRYU9JmHaMZh0SloUG-S4yLsDU3ZJvJOAu4jdLYnGQJFRxeaNQ5hXcydSq4nP5xjbDz3Ja00o2wf1LlO5bVHV7fPYuODleyvGRqCU4fMLjgIPihUhJhkMmbKgr4Z5QZkx9FVDfGu7NLRFf752HBMzmCd12Ur-hCOBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f256f6aba.mp4?token=aZQOLmVJYmrKEtUBlMjyrevVM6tZcdVL_-1KU8XjHmTdQhkRMCPRbqFJEpCjgeFaxjbVCD3qdKREfa2y_wLmo-b9rG8CJzsLkkxd02tP1Vn1pc60D0Ae1_J8q8ip-t8vKm70igxTM1Pr1PB4nV99gaP_F_Dtk0yTI0E3N8TqBVVDzZn-00lsBeRMDS9cmEdYVlTWKUByNfEZrJi6IqXGn3WBDeQYeK1DXNaQEP-gKrPwaMU6vE6s2WOWSnN0N9ZK1IHOkZDURe0VIkeUWc5qdWLREMzKJNt9CMUpY2qJO2oBcSJg1ZeiNIyREpLtnSLxicnhNJLf6IKu__QOEA4XZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f256f6aba.mp4?token=aZQOLmVJYmrKEtUBlMjyrevVM6tZcdVL_-1KU8XjHmTdQhkRMCPRbqFJEpCjgeFaxjbVCD3qdKREfa2y_wLmo-b9rG8CJzsLkkxd02tP1Vn1pc60D0Ae1_J8q8ip-t8vKm70igxTM1Pr1PB4nV99gaP_F_Dtk0yTI0E3N8TqBVVDzZn-00lsBeRMDS9cmEdYVlTWKUByNfEZrJi6IqXGn3WBDeQYeK1DXNaQEP-gKrPwaMU6vE6s2WOWSnN0N9ZK1IHOkZDURe0VIkeUWc5qdWLREMzKJNt9CMUpY2qJO2oBcSJg1ZeiNIyREpLtnSLxicnhNJLf6IKu__QOEA4XZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انفجار بزرگ در کی‌یف، در نزدیکی بزرگراه ژیتومیر، پس از حمله روسیه به یک انبار مهمات اوکراینی رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/144318" target="_blank">📅 23:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144317">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
پزشکیان: بنابرقولی که داده بودیم، باید مبلغ کالابرگ را متناسب با افزایش نرخ ارز افزایش می‌دادیم، اما نتوانستیم این کار را انجام دهیم. در این زمینه از مردم عزیزمان شرمنده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/144317" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144316">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7a29fb5c7c.mp4?token=MM-iSo6sB0XEh9UMqtIo6ZNkr9iniv5QbCu-D3cfr4ruv0Chf-mSouwirqZQBdx6ZubfKO4qvziS_LO6gRdfigkneObJdojyXwMKM_1ft3fqUF1krTQOZFgAza5S45ttTuIcD5HMr_PtZfZJAp9rQyJpDecwxEqH-WWl3kt6mSHhz316HSP1nB1r2aiTSsBDDDSuCOX8pWPGqg3iM9N3CdQbHN61ywIbSOnqQ8pskPCTjG5zUl7KoRsyoOYRuX5YxeEuw4h9WY9ETME4ZfA3-Kq3wkmZN-OxZXXnD9WE6FFeq8yUNc66lqps25_wt7GXoViXNtDEM7PEifIrm1Pleg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7a29fb5c7c.mp4?token=MM-iSo6sB0XEh9UMqtIo6ZNkr9iniv5QbCu-D3cfr4ruv0Chf-mSouwirqZQBdx6ZubfKO4qvziS_LO6gRdfigkneObJdojyXwMKM_1ft3fqUF1krTQOZFgAza5S45ttTuIcD5HMr_PtZfZJAp9rQyJpDecwxEqH-WWl3kt6mSHhz316HSP1nB1r2aiTSsBDDDSuCOX8pWPGqg3iM9N3CdQbHN61ywIbSOnqQ8pskPCTjG5zUl7KoRsyoOYRuX5YxeEuw4h9WY9ETME4ZfA3-Kq3wkmZN-OxZXXnD9WE6FFeq8yUNc66lqps25_wt7GXoViXNtDEM7PEifIrm1Pleg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: واقعیت اینه که ما پول نداریم، درآمدمون هم که مشخصه، کمتر شده بیشتر نشده، مشکلاتمون هم بیشتر شده، در ضمن باید جواب هم پس بدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/144316" target="_blank">📅 23:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144315">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
پزشکیان: افرادی که دستی بر آتش ندارند، تحلیل‌هایشان در جیبشان بگذارند
‏
🔴
طرح نمی‌خواهم؛ اگر کسی می‌تواند مشکلات را با شرایط موجود حل کند، به او اختیار می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/144315" target="_blank">📅 23:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144314">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
عراقچی: به جهان نشان دادیم که آمریکا و اسرائیل قادر به مقابله با موشک‌های ما نیستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/144314" target="_blank">📅 23:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144313">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
رئیس‌جمهور: اگر به تعهدات عمل نکنند، به مذاکرات ادامه نخواهیم داد اما نباید نگاه صفر و صدی داشته باشیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/144313" target="_blank">📅 23:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144312">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پزشکیان: در زمان اجرای تفاهم‌نامه اسلام‌آباد توانستیم به میزان کافی نفت صادر کنیم
🔴
نزدیک به ۹۰ میلیون بشکه را در همان مدت کوتاه صادر کردیم
🔴
من معتقدم اگر در داخل افرادی که دستی در آتش ندارند، تحلیل‌هایشان را در جیب خودشان بگذارند می‌توانیم به صلح نزدیک‌تر شویم
🔴
می‌گویند تحریم‌ها اصلاً تأثیری ندارد و مشکل فقط از مدیریت ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/alonews/144312" target="_blank">📅 23:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144310">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
پزشکیان درباره قیمت ۱۰۰ هزار تومانی بزنین در کرمان که متوقف شد: باید طرح‌های مختلفی داشته باشیم اما اگر طرحی شکست خورد باید این توانایی را داشته باشیم که نسخه خودمان را تغییر بدهیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/144310" target="_blank">📅 22:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144309">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
پزشکیان: مسیرها بسته است؛ کالا وارد نمی‌شود و یکی از این کالاها بنزین است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/144309" target="_blank">📅 22:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144308">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=lKkF4fEXSalv3J7-hV4VtVzOGv4FmTfm9hIZJMw9WTDlhtuesUIxOcSC088G3lJRi7fAco-fB0H_JdDNuRcXFzBjp9bB6HYug7VDsKHDwvVd8lF16ccewOPQdU9Wt5SH8D2XqiALsUl7YEGbpcLsRjZKbSDiBuer7-FMbYDrxpufNEs1mgvkzAg9HlpAcHuWdPPF26TTLwmhNlnulHeq5w4Oqn052lClrB5iVqQ_AiMtQlvz1DqMjJrQqiJiL4gxiCLNrJxRSqrDTXEYbhptMYBI4nJE0tIhYR5PkI1Rgb_3JiLsLHqihkA6tKtdDlHg5Oy150UIXxrrlbQNbx5SQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77ed0196bb.mp4?token=lKkF4fEXSalv3J7-hV4VtVzOGv4FmTfm9hIZJMw9WTDlhtuesUIxOcSC088G3lJRi7fAco-fB0H_JdDNuRcXFzBjp9bB6HYug7VDsKHDwvVd8lF16ccewOPQdU9Wt5SH8D2XqiALsUl7YEGbpcLsRjZKbSDiBuer7-FMbYDrxpufNEs1mgvkzAg9HlpAcHuWdPPF26TTLwmhNlnulHeq5w4Oqn052lClrB5iVqQ_AiMtQlvz1DqMjJrQqiJiL4gxiCLNrJxRSqrDTXEYbhptMYBI4nJE0tIhYR5PkI1Rgb_3JiLsLHqihkA6tKtdDlHg5Oy150UIXxrrlbQNbx5SQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: فقط نرخ سوم قیمت بنزین پس از هماهنگی با همه نهادها و ارگان‌ها از ۵ هزار تومان به ۱۰ هزار تومان خواهد رسید. نرخ سوم قیمت بنزین بیش از ۱۰ هزار تومان نخواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/144308" target="_blank">📅 22:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144307">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
پزشکیان: در روند گفت وگوهای فعلی، نقشه‌راهی برای عبور از تنگه هرمز تدوین شده که توسط برادران ما در سپاه پاسداران، نیروهای نظامی و تیم مذاکره‌کننده به استحضار آیت الله خامنه و مورد توافق قرار گرفته است.
🔴
عمانی‌ها در ابتدا همراهی کردند، سپس ملاحظاتی داشتند، اما در دیدار پریروز، مجدداً به تفاهم رسیدیم و پذیرفتند که مسیر بر اساس نقشه هماهنگ‌شده بازگشایی شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/144307" target="_blank">📅 22:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144306">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
پزشکیان: ما داریم تلاش می‌کنیم از حرف‌های تفرقه انگیز پرهیز کنیم. شما خیلی راحت می‌توانید بدی‌های من را ببینید و نقد کنید. چرا خوبی‌های هم را نبینیم.
🔴
چرا باید هر روز شما عیب من را ببینید و من هم همین‌کار را بکنم و روز به روز این شکاف بیشتر شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/144306" target="_blank">📅 22:24 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144305">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
پزشکیان: اگر آمریکا تعهدات خود در زمینه رفع تحریم و محاصره و آزادسازی دارایی‌ها را انجام دهد، سرمایه‌گذاری را شروع کند و جنگ در لبنان را تمام کند ماهم تنگه هرمز را باز می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/144305" target="_blank">📅 22:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144304">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
طبق گزارش گلدمن ساکس، جریان نفت خام از طریق تنگه هرمز تقریباً به دو سوم سطح قبل از جنگ بازگشته است و تأثیر جنگ ایران بر قیمت جهانی نفت را به حداقل رسانده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/144304" target="_blank">📅 22:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144303">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8f9c4ae0.mp4?token=q_CtCyivoAfM2uYeJM61JBbBur2gYKdFUCajxjwmqdDciAMmQRwAT5I6jb_4PE7RiTtsu0vOwBBQZ5VfRWsSuHJ9K1wb_tACcGORDj6NbYnphAs7QQIKFtJCiwpZQKKA9Wo9EtA3yOAIgw_SZkJm315Oa6G3NpHwMNZRV2ph7sd9iIgfiMz0bKAKBoGxwjF6wWt4EMxyIfQtJqcMiloxa506b8cCI3_DiN_fONuaCQuOf0mA49mR7G_CBR4HjNbc9Txlb6XB2SeQzSHenM32L3jXx3dQYZaDd2p82_IDFmRPs41YpupubykMailU62vFgMcsQQ7Lw3MIcOcig5M-zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8f9c4ae0.mp4?token=q_CtCyivoAfM2uYeJM61JBbBur2gYKdFUCajxjwmqdDciAMmQRwAT5I6jb_4PE7RiTtsu0vOwBBQZ5VfRWsSuHJ9K1wb_tACcGORDj6NbYnphAs7QQIKFtJCiwpZQKKA9Wo9EtA3yOAIgw_SZkJm315Oa6G3NpHwMNZRV2ph7sd9iIgfiMz0bKAKBoGxwjF6wWt4EMxyIfQtJqcMiloxa506b8cCI3_DiN_fONuaCQuOf0mA49mR7G_CBR4HjNbc9Txlb6XB2SeQzSHenM32L3jXx3dQYZaDd2p82_IDFmRPs41YpupubykMailU62vFgMcsQQ7Lw3MIcOcig5M-zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
👈
عراقچی: تلاش کردند که آتش موشک‌های ما را خاموش کنند، اما نتوانستند، نهایتاً چاره‌ای پیدا نکردند جز اینکه تقاضای مذاکره بکنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/144303" target="_blank">📅 22:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144302">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نیوزویک: جنگ‌های ایران و اوکراین، افسانه بازدارندگی هسته‌ای را به چالش کشیده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/144302" target="_blank">📅 22:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144301">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
به دلیل تحریم های جدید آمریکا علیه ایران، بانک مرکزی عراق تعاملات 14 فرد و 19 شرکت فعال در زمینه‌های نفت، تجارت و حمل‌ونقل را متوقف کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/alonews/144301" target="_blank">📅 22:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144300">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D8YDAWkBb0aHhWSKmOnqpLYb7kNccjICSxDYtK9vqBmelDCgoXfjplQu6KwiPNAnNK0CsjB7KFhvggr_UT1uL57tuugxGyXAmnfAsGT3u3Mh4-6syagxHenTJJHRgIqHsaNlILo7qoj05Bb3eJq4htLXcFRypfLTR3MmIGW4iffsAJh6FuhOw_M8znLGe7uPU2e9sRIsKt1YeQY5r1OjA1_lAVaEPBBOkUzjVRnMpMiz14a661kFCn35qfcEatnbgm6NKmhTEyM6pPRdWE1EVDPuQAeJg_yaEj7ismrV_wNPVs9pRnsq9CuP3PWxYBkgk34mt9rssHYl_uNDo6IYGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش وال‌استریت ژورنال، پیتر هگ‌ست، وزیر جنگ، در حال بررسی امکان بازگرداندن صدها مقام ارشد نظامی ایالات متحده به پایگاه کوانتیکو برای یک سخنرانی دیگر است.
🔴
به احتمال زیاد، این جلسه بر اولویت‌های او، از جمله استانداردهای سخت‌گیرانه‌تر آمادگی جسمانی و آراستگی، آمادگی بیشتر برای نبرد و تغییرات بیشتر در سیاست‌های پنتاگون، تأکید خواهد کرد. این در حالی است که سال گذشته، یک گردهمایی غیرمنتظره از ژنرال‌ها و دریاسالادها برگزار شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/144300" target="_blank">📅 21:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144299">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
وزارت خارجه آمریکا: افراد و نهادهایی را که از طرف ایران به فعالیت‌های مالی غیرقانونی مبادرت می‌کنند، هدف قرار خواهیم داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/144299" target="_blank">📅 21:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144298">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
شنیده شدن صدای انفجاری مهیب در اردن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/144298" target="_blank">📅 21:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144297">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMoXHNKFvXUGAAO4V3i8l8ghkF1Tz4Ha6FHSbUwbil5CAY62D9NV7rr6RHuC4pwHUrbdCA6x3D0bP7-CmkFalJzVY2kFBwvd6C-m3U--7xPqICHSWPe943bPz1f9TO4KfqMTJTUgHW3ee6mryE-BCXJbUNv3YYeUDib_RvnHVjv3XpuY05-tx8Co38_vS_4yVP6iKvK95nNPgNX8S4zrKpZhImVOeTLzSNhDkeQ3hOizxpJUMMYlIolYquTZ35xrim_VEIHKw7-FapOb2FuJRxkFALaHcoIJmkuKXbVSm-HQB3FVMyZPMUEam8_rtW00Zehui-cqyJkLTGHrAbCFOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قیمت نفت برنت ۸۸ دلار
✅
@AloNewd</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/144297" target="_blank">📅 21:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144296">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
توانیر: کاهش ۵۳ درصدی قطعی برق در تابستان امسال
🔴
هدف نهایی این است که در تابستان آینده، پرونده قطعی برق به‌طور کامل بسته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/144296" target="_blank">📅 21:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144295">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
کاتز، وزیر جنگ اسرائیل: عملیات موفقیت‌آمیز ترور رهبر حماس در اردوگاه جنین
🔴
ارتش مانند بقیه اردوگاه‌های کرانه باختری، به طور دائم در این اردوگاه حضور دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/144295" target="_blank">📅 21:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144294">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
بیانیه ایت الله مجتبی خامنه ای: از رئیس جمهور و دولتش بخاطر زحماتش تشکر میکنم، بیان دلسوزانه ی مشکلات کشور باعث میشه دشمن روحیه بگیره پس باید حواسمون باشه هم چنین مردم جانانه ایستادن و باید در شأن و منزلتشون مسولین بهشون خدمت کنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/144294" target="_blank">📅 21:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144293">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ: رویای آمریکایی بازگشت. فکر می‌کنم این بار قوی‌تر از همیشه بازگشته است.
🔴
ما در حال حاضر عالی عمل می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/alonews/144293" target="_blank">📅 21:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144292">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
ترامپ: می‌بینید که چقدر خوب می‌جنگیم. ما بسیار خوب می‌جنگیم.
🔴
به ونزوئلا نگاه کنید. ۴۸ دقیقه.
🔴
راستش را بخواهید، با آن افرادی که پشت سرم هستند صحبت کردن را دوست ندارم.
🔴
ظاهر آنها خیلی خوب به نظر می‌رسد
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/144292" target="_blank">📅 20:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144291">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5b86a38e6.mp4?token=HaAc1zTvWsOLnhbYtqR5NcGwxcJSOU2zfXbT7RSVpN9zj1MWons5hHrQsNCLZJiU_-t24npqU4P0n_GTFSqKxccs49gn2ZMwlDOgpW0A-RW96CY7SDN4RnlYIY6tyzbHTvFe1UYYuTsd8ZtVRAzZrc3s8IzXVCB0xiLYQILKkWLMSWHUIX4HoN6uRv69upGSk67XQt1FP5F6VKDXHq4f0ABigmQcIrcj-OfubHXZ0PCW8k9MDXG33uQNKtYsUi_uHqZyUj_1KGGqw1MYj5arahBUMVilA80eGBxJhc79GzLQQmEIGNh-1jb2gZ8joKtKB0z6SmdQsWVTWZoJlAy9AjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5b86a38e6.mp4?token=HaAc1zTvWsOLnhbYtqR5NcGwxcJSOU2zfXbT7RSVpN9zj1MWons5hHrQsNCLZJiU_-t24npqU4P0n_GTFSqKxccs49gn2ZMwlDOgpW0A-RW96CY7SDN4RnlYIY6tyzbHTvFe1UYYuTsd8ZtVRAzZrc3s8IzXVCB0xiLYQILKkWLMSWHUIX4HoN6uRv69upGSk67XQt1FP5F6VKDXHq4f0ABigmQcIrcj-OfubHXZ0PCW8k9MDXG33uQNKtYsUi_uHqZyUj_1KGGqw1MYj5arahBUMVilA80eGBxJhc79GzLQQmEIGNh-1jb2gZ8joKtKB0z6SmdQsWVTWZoJlAy9AjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره فضا: از نظر ژنتیکی، من به آن چیزها باور دارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/144291" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144290">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61032aae6.mp4?token=A_yXvrSixEAuZRH0-b8O_3O4zpeohdGx77lB4YafZBWTa9O_w9yLgREI_Y8jsvXun30Q20hILX0qYQoSKSm4YwXdGXQx58qeCqIt0G2AsZMSZZ_hhcrfzPdh9YMNIRMRPqel6SscFAT6FlsRPLHuO2hGvMLRfUAL14l_RdwpmKVcJnPfKI7_3sH_c7rLLF6A6I2weDu59md-8_r9Bx50QHg0cY4Rn6kXXGukTS_4zMd0snHgM4KEk_yvBHld_ZLOANFkYKzNH0HjW8pTxZYrFC7dMiAA8BH9ZrJna7k39I9Ku_Qsc1GauYpUi3pa0I3jAWecZgf-YgD-qoPqRw3j6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61032aae6.mp4?token=A_yXvrSixEAuZRH0-b8O_3O4zpeohdGx77lB4YafZBWTa9O_w9yLgREI_Y8jsvXun30Q20hILX0qYQoSKSm4YwXdGXQx58qeCqIt0G2AsZMSZZ_hhcrfzPdh9YMNIRMRPqel6SscFAT6FlsRPLHuO2hGvMLRfUAL14l_RdwpmKVcJnPfKI7_3sH_c7rLLF6A6I2weDu59md-8_r9Bx50QHg0cY4Rn6kXXGukTS_4zMd0snHgM4KEk_yvBHld_ZLOANFkYKzNH0HjW8pTxZYrFC7dMiAA8BH9ZrJna7k39I9Ku_Qsc1GauYpUi3pa0I3jAWecZgf-YgD-qoPqRw3j6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ
:
در دوران اوباما، توانایی ارسال فضانوردان به مدار را از دست دادیم.
🔴
ما هیچ توانایی‌ای در فضا نداشتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/alonews/144290" target="_blank">📅 20:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144289">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
دستیار رئیس‌جمهور روسیه: پوتین دوشنبه ۱۰ شهریور ۱۴۰۵ با مسعود پزشکیان دیدار و گفت‌وگو خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/144289" target="_blank">📅 20:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144288">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e59767ff6.mp4?token=MC3sYcKkCOAIWtZ8RZmQ51jNnzfjckCPddOXbkF5nnx7DQCp1RmXozxcazZ73ado9Yoko1O5RhSf0E5Cuvs_TlPKQIBGv2Zy_qXyfFSzLImD2Co1nIXeogRYmKJBSJEFkx-FUY0HR2YOpS4W4cx6xJCJobiNEjO6C0vOKUlwWLtUE3k0oUmKQjEhC430ror0e7ILdacZQ4YICdJfMVhK635cLdPxXFR4oYR6ifNifkppJVI_NAVLxZBLsFxU7LrsCtLJmdXyofqWYAgdy4shL3DC51VeUG4omu8CwmSAdCu5tDLwwdmtXX-yqrRAb6rG1J_tbXS8J9f9wAWqF73wEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e59767ff6.mp4?token=MC3sYcKkCOAIWtZ8RZmQ51jNnzfjckCPddOXbkF5nnx7DQCp1RmXozxcazZ73ado9Yoko1O5RhSf0E5Cuvs_TlPKQIBGv2Zy_qXyfFSzLImD2Co1nIXeogRYmKJBSJEFkx-FUY0HR2YOpS4W4cx6xJCJobiNEjO6C0vOKUlwWLtUE3k0oUmKQjEhC430ror0e7ILdacZQ4YICdJfMVhK635cLdPxXFR4oYR6ifNifkppJVI_NAVLxZBLsFxU7LrsCtLJmdXyofqWYAgdy4shL3DC51VeUG4omu8CwmSAdCu5tDLwwdmtXX-yqrRAb6rG1J_tbXS8J9f9wAWqF73wEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: دستیابی ایران به بمب اتم یعنی پایان اسرائیل
‏
🔴
نخست‌وزیر اسرائیل: واقعیت به‌سرعت در حال تغییر است. یک قدرت افول می‌کند و قدرت دیگری ظهور می‌کند؛ مهم‌ترین قدرتی که باید ظهور کند، قدرت ماست.
‏
🔴
بمب‌های هسته‌ای در دست ایران، یعنی پایان دولت اسرائیل؛ پایان ملت یهود. ما باید این کار را انجام دهیم، چون در غیر این صورت نابود خواهیم شد. دیگر اینجا نخواهیم بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/144288" target="_blank">📅 20:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144287">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAToVNyRHk4jpcHf23FkYOBGi3n5o6FwrULdD4GTQOMS4dVT8uWYUBXFXf8L20RQMOeDqbg-elnXKK88PBw-8KsY323Yc1uCgtmLzJDI5YFu_qGBaAre1HJtf_kXiq3zse8Lr6NDCHUX1h1uzdV-CHABjh4CNMVCVqBi-pYdOJzQSffSmqWuMgI_4Q_YwdBjRWsQjErdnaSebs2UHJeozxzxGrxhydAJxmm2WvrM899QQoDC1f-j_SKE-RqeS9jGhok7MBtZldvD_3leF7WzQeNX1g22D40kuslPX5u9QIilLdRtVVPMBMuEoTy2MzNh_1H1tAm6LAccA3r9QWz0Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت: وزارت خزانه‌داری قول داده است که تمام راه‌های اقتصادی را که تهران در اختیار دارد، قطع کند و در نهایت، تهدید ناشی از رژیم ایران را پایان دهد.
🔴
همچنین هشدار دادیم که کسانی که از ایران حمایت می‌کنند، نمی‌توانند به استفاده از دلار آمریکا و سیستم مالی جهانی ادامه دهند.
🔴
بانک "میصر" در امارات متحده عربی، به سختی این موضوع را درک کرد و امروز، ما اولین قدم را برای پاسخگو کردن این بانک به دلیل حمایت مداوم و فاحش آن از رژیم ایران، برمی‌داریم
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/144287" target="_blank">📅 20:19 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144286">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
شرکت انرژی قطر تعلیق تحویل محموله‌های گاز طبیعی مایع (LNG) به شرکت ایتالیایی «ادیسون» را تا اواسط پاییز تمدید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/144286" target="_blank">📅 20:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144285">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
جاده چالوس از شمال به جنوب یک‌طرفه شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144285" target="_blank">📅 20:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144283">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nba11jayC_c9e4fEaOKaw31U2c4ynN4r1vBi5v8ccxwWY4iyaI3i1L71J_w9RJZxDcisM9Q7Etu0DX7GWCeN_GV33tTeo_wLnKFGr9QWelbQexfUV03FjdabJz4Vkh0zQp2YJflX574ydJlXvB1CE-RkB-Q71Wy-wzr5vMBPnP6SdNVuGBYwooK91KnHpXw-t2VTaKEn9B9f1GXhNZsCw-ARCJ3ihUKsZyl0XgnGIBoyB6V_kiBngYaQssBEsgERRvAyPsccIeZVJhai705ylISg9WMgOF1zZj6bfyXCyY3Tqctoyn0x82O84nCAQmzw7yKTuuGLwOnfIwXe41a3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6_BuvVvsiQxuF9jTXQaiFq90loXl8RLUruyyKhjg6xMfnepGCxjmbALaxl8Nm_MU90QxlCUGj1oe9mW4tnmVAhwj0JbRkV81BQmuTeMeqfNOcYSExYwdKx0ADgNNRzGSlSM-DPVq_HQcYrUnIzn7K9NKndOGfhhjsyh7eNDxridTsUNM0fFovzl4myWKKBUSNByltppurynejgLyHuiheYEUBtDHJrsGsz-XAdbhWjg0sVUqs5fzpIVN5nTXGcoryMUBsbrF-zGlkBVji0kMk_BHJAcURfjK08vsQ88-B1aJFzehDZ57vTds39tW246zTATw1axWTW1jCh-Ngg5Bw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
حملات شدید اسرائیل به جنوب لبنان ادامه دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/144283" target="_blank">📅 20:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144282">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
روسیه اعلام کرد که
با موفقیت یک موشک بالستیک بین‌قاره‌ای موبایل با سوخت جامد را از پلستسک به‌صورت آزمایشی پرتاب کرده است و سرهای جنگی آموزشی به محدوده کورا در کامچاتکا رسیده‌اند.
🔴
این سیستم به‌طور رسمی نام‌گذاری نشد، اما چیدمان آن به‌شدت شبیه به RS-24 یارس است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/144282" target="_blank">📅 19:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144281">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d09db21f37.mp4?token=bHNfbF8pXS8qai_a92tyyuS0ydXJxAcrQPzL-FS3VC7eDl-5tvua1US2_FIT-mRTC6UdypxUE_Tb7cz8oOt7Y4H1wpc3V4l_6bEDeu-ghoJiVhSlgrS64SjL3mZDZO8LRBBXBLvsUuSWcjSHPFX8noyw0GZE6IGPIF5SUZMq1CmQo_6FqH3_0SFCJhq4bWEnU-_ImhWBjjGxrLuMLDHrH4c-B3Hg5YMHC9gN3bXTxJ5Y-PJBJfbRLJgUNCPTyO31uiZ9U82vN8F7lbBStzMYmg1duZx_7P0AeeCubll2cOfU6F4_qfVdBJ4InKsFGQ1NfsXIYnpRLwlol6H9WewoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d09db21f37.mp4?token=bHNfbF8pXS8qai_a92tyyuS0ydXJxAcrQPzL-FS3VC7eDl-5tvua1US2_FIT-mRTC6UdypxUE_Tb7cz8oOt7Y4H1wpc3V4l_6bEDeu-ghoJiVhSlgrS64SjL3mZDZO8LRBBXBLvsUuSWcjSHPFX8noyw0GZE6IGPIF5SUZMq1CmQo_6FqH3_0SFCJhq4bWEnU-_ImhWBjjGxrLuMLDHrH4c-B3Hg5YMHC9gN3bXTxJ5Y-PJBJfbRLJgUNCPTyO31uiZ9U82vN8F7lbBStzMYmg1duZx_7P0AeeCubll2cOfU6F4_qfVdBJ4InKsFGQ1NfsXIYnpRLwlol6H9WewoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ادعای جنجالی ظهره‌وند درباره پزشکیان و قالیباف: «دین و سیاست را جدا می‌دانند»
🔴
ابوالفضل ظهره‌وند، عضو کمیسیون امنیت ملی مجلس گفت: گرفتاری ما در داخل است؛ در اقتصاد ملی مشکل داریم و به همین دلیل نمی‌توانیم بین جنگ، نیروی نظامی و دیپلماسی ارتباط برقرار کنیم.
🔴
ظهره‌وند همچنین مدعی شد قالیباف در بغداد گفته است که اگر نیروی نظامی پیروز هم بشود، مردم گرسنه شورش می‌کنند و کار نظام را می‌سازند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/alonews/144281" target="_blank">📅 19:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144280">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
وزیر کار: به‌جای فروش شرکت‌ها، مدیریت شستا را به بخش خصوصی می‌سپاریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/alonews/144280" target="_blank">📅 19:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144279">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bij6IEA9I9qFiiUHStEsOWUYqOfgDaz6K78yymuB_1qVXTuoEgpLvYiyDitR4LR4kvXLg0L8gj40JnWzyS5AM8fuRRzXgYMwFl-cz8XnxcJZsgFa_0soFQZq9uJKWTHF1r-ScSP6vGle6R5-fsS1n2ms8DuTBZ9IXJHydRcRZ9SBZTl2mE3M1AY3WZER47CcCmoMUN5FlxWTbHsE5E3xrktHOjdmdRmSM9VvTS0Ls0OW0-FOrbi6RWC9W-qpOlJbZ0KWuoc4cDjTZUP6gTa3SGBgUoV0DhJXdWbeGzXNGc7_5YrDmbAjRZQl3veKQHxdYr9pPTWcTpaedQ-sepiS9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری فرانسه: ورود یک پهپاد ترکیه به حریم هوایی یونان و بر فراز یکی از فرودگاه‌های شرق این کشور واکنش فوری جنگنده‌‌های اف۱۶ یونان را به همراه داشت.  را ضروری ساخت.
🔴
این پهپاد زمانی که یک هواپیمای مسافری قصد برخاستن داشت نزدیک  باند انتهایی فرودگاه الکساندروپولیس حرکت کرد.
🔴
اقدام جنگنده‌های یونان باعث دور شدن پهپاد ترکیه از حریم هوایی یونان شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144279" target="_blank">📅 19:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144278">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736924625c.mp4?token=PugYOOq1qK8prW69VIQtMVFaqgnGSJtlXIBXp8pCw-CnUA8c3KwQOFm_5VmVo6i68S-RQ-P49Yi3IfUbgjkW_rDV0FtJQMkxWJHU6ceItN4t7tvnkOnIG3bwjymnuOyKIvYQcRxFTBfXIu-rvcEmShyhIUQdfkdbCVYAnGjBIBVz0zQbjE1TL2Y42Z21xDENNfjiCqzyB-xm7Nkt2XQiwxMHByVG_WybLE2WBlGmafn7jTk92dpAlBpPAz3dmUxb64VfjQD4QWD-pdtXsRkaeNDl8_I7RacZPoJozJ-A0NrWW5scZBLsQZsq2dQFe0x6vvoFNsAm-Zr9dH39MyDBLm7VUoA-SHVu-BsVRkOHyXtLKBepR1Z971a6wJOPyhm_6r977rH6U-x9ONk5GkO18NInoCPwodnffHNsY4mv-bab6lwEKCdWPejl3hL233Odn9AUyoqXiVbrZoj82-S75wiRX2BmktuuetHYGz9i503oGory-hHUzOrR66RpL1ZZwBE5JuONbS9UXzranRCE1nAEwsLkvg1JJaHaSW9ATUyTVGglGLcBvgdTURJuiTRxSerEUxne_oQJdoUgLetgVbZ37TgqFuyrao4Wsf586ZTPO835lQqmN42F_Sc-bWuVvI8ISM_h0BjBUM-e0LMOYzZAbRSMogIyu9ZvV2eDTOM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736924625c.mp4?token=PugYOOq1qK8prW69VIQtMVFaqgnGSJtlXIBXp8pCw-CnUA8c3KwQOFm_5VmVo6i68S-RQ-P49Yi3IfUbgjkW_rDV0FtJQMkxWJHU6ceItN4t7tvnkOnIG3bwjymnuOyKIvYQcRxFTBfXIu-rvcEmShyhIUQdfkdbCVYAnGjBIBVz0zQbjE1TL2Y42Z21xDENNfjiCqzyB-xm7Nkt2XQiwxMHByVG_WybLE2WBlGmafn7jTk92dpAlBpPAz3dmUxb64VfjQD4QWD-pdtXsRkaeNDl8_I7RacZPoJozJ-A0NrWW5scZBLsQZsq2dQFe0x6vvoFNsAm-Zr9dH39MyDBLm7VUoA-SHVu-BsVRkOHyXtLKBepR1Z971a6wJOPyhm_6r977rH6U-x9ONk5GkO18NInoCPwodnffHNsY4mv-bab6lwEKCdWPejl3hL233Odn9AUyoqXiVbrZoj82-S75wiRX2BmktuuetHYGz9i503oGory-hHUzOrR66RpL1ZZwBE5JuONbS9UXzranRCE1nAEwsLkvg1JJaHaSW9ATUyTVGglGLcBvgdTURJuiTRxSerEUxne_oQJdoUgLetgVbZ37TgqFuyrao4Wsf586ZTPO835lQqmN42F_Sc-bWuVvI8ISM_h0BjBUM-e0LMOYzZAbRSMogIyu9ZvV2eDTOM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وقوع آتش‌سوزی در یکی از مقرهای الحشد الشعبی در پایگاه اسپایکر صلاح‌الدین
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/144278" target="_blank">📅 19:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144277">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GIddW_CZruqVRom_xL2KVLKsmVrsw240578NTehtrmKkqhoX8dswQIvT4C1PBDZxeXSvqpcB_3UBiVzTDackAQ-qofTI2fpKqIXde09-sC_LZ-_8s4A1SLM2-dPn_S3iT8wc6ZQInopo5qWTKN7phVe7WIqBZ26Bd7FM5puJnQlRQoG3A_f26U0sgFrPZMUZRUcMUX62jGu7BGrXz1oPayGtE0FE4R1i-GE1d8E6lwv8_4LkKQAZdCqLf3dJ6d2z4gK7n5IGjJkRyHqVOaui7t3MjCpEFAa0bzzScNGSbvv3iTBCdgjrb8oQAMa1F3VNem_X84sAWbS9Cg3TuqFPcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
واکنش نخست‌وزیر کانادا به تغییر نام دریاچه انتاریو به «دریاچه آمریکا» توسط ترامپ
🔴
مارک کارنی: نام دریاچه انتاریو از واژه وندات «انتاریو» گرفته شده است که به‌درستی به معنای «دریاچه زیباست، دریاچه بزرگ است» می‌باشد.
🔴
این نام بیش از ۴۰۰ سال قدمت دارد و پیش از کنفدراسیون کانادا و اعلامیه استقلال ایالات متحده آمریکا وجود داشته است.
🔴
ما می‌دانیم که آمریکا در حال تغییر است. روابط تجاری‌شان، سیاست‌های خارجی‌شان، بناهای ملی‌شان، نام‌های آب‌هایشان.
🔴
کانادایی‌ها همچنین می‌دانند که نامیدن واقعیت به معنای نامیدن آن به عنوان دریاچه انتاریو است - آن زمان، اکنون و همیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/144277" target="_blank">📅 19:36 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144276">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
نیکزاد، نایب رئیس مجلس: جنگ فی نفسه هدف نیست/ باید میان توان ادامه جنگ و مصلحت ادامه آن تفاوت گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/144276" target="_blank">📅 19:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144275">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCEKMlGOXo_T7_B8LnRywY-003ukBhdX4Fud02CoTsXF1hLjnZbftnzVyzQ5XdrNgRVY0wlWvQopA1p0iG1dxvcxWlwmuPaSxgTf2OzG0hZdwqdJyGFz7Ry_sL3Rl_F8g7cLMchrNn68m8YMGAP7TkFNsQpn_yZn_-qAcq-ySKz0BzFBEwqd5pm37YPWP0Aw3F_EH27Vn-zhJJ1D3IiytXn_Ku284WVZjGeWEDOidm85A1TYHiZAtmuyKYau2NaXJoeMJ7BFM96kTA3ymqUaUueK_1w7tbhkzQgJq5kT4Ua0pWfBtoOFG7aWmTCFv3e9NA1ohp36ORfs256BVezttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پادشاه اویو، رهبر سنتی و حاکم منطقه توروی واقع در کشور اوگاندا، در سن 34 سالگی درگذشت. او به دلیل ابتلا به سرطان در ایالات متحده بستری شده بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/144275" target="_blank">📅 19:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144274">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/auqNomgwq-s2tZ8mbEa-ezk-NnIge4qtmHcBsBmlL3sHrZiLvudA4lX67LZNjwqyNEVCoGmx0XDy-0hIzF_dL-qDe-Ot45Dh9gcQGlVSi07a2aUAMnXSWD0H-Z-bYCdslQQMFn-NOU4l4aT53xouA7xkGjPvbnRTOKAld1KhsG4hEEP9IeYFvPEGcyHD7WsVX9Wsc7SsaxqwnAUvwyQqXnI9eUUah7ldPwltNZyCBCHpE8Y7mWfh-ULwx_UDITBRkJJ6tD_eTkRGZ5zW97zO3kjgNZgy1Wkd-6HHR6pGN_3JQN_5QyINkoAwaQFW-nrI_qL-wrBFnp_QCafnUMMKWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دبیرکل سازمان بین‌المللی دریانوردی اعلام کرد حدود ۶ هزار دریانورد در ۴۰۰ کشتی همچنان در تنگه هرمز گرفتار هستند.
‏
🔴
به گزارش سی‌بی‌اس، این کشتی‌ها و خدمه آن‌ها به دلیل شرایط موجود در منطقه امکان عبور عادی از تنگه هرمز را ندارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/alonews/144274" target="_blank">📅 19:20 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144273">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
یاشار سلطانی: قدرت تصمیم‌گیری در کشور باید واحد و مسئولیت‌پذیر باشد
🔴
نمی‌شود کشوری را با مراکز متعدد قدرت، تصمیم‌گیران موازی و مسئولیت‌های مبهم اداره کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/144273" target="_blank">📅 19:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144272">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBNdo4FqH56FXNhI0s1CddZxCRcJD1_Iy4K4-QfMjc9_7fpSVm_ZnSjGh8RTKaleO730mNIC6N2I_tu_6d6OFDCpKExD9me9x5m2h1Sy7PN3WduDW02XiO0CA-X3I-wrVRsj6xKSliBlFbuuvRPqg0dybhnwYExIvf0qZFrVZGaq26n6CpjwTqGHm3DjRiSN3uaGJbBgXBtk2fwhm9wHoZ2UQes0ziQ0NYJ-tl-kR6nPYFl2vJv8fEws3m3g338aQojE4IgI2xeYLDRwJE0vHRxQzO2K5m74ivaHMA6L1k0RdUB1wfJpG0oORkHlkvbFoiyeElaOFVZctGRyV-hhPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یونان و اسرائیل قرار است روز دوشنبه در تل‌آویو، توافق‌نامه‌هایی را امضا کنند که آغازکننده شبکه یکپارچه دفاع هوایی و ضد موشک به نام "زره آشیل" به ارزش ۳.۱ میلیارد یورو خواهد بود.
🔴
این سیستم، سامانه‌های اسرائیلی "اسپایدر"، "باراک MX" و "داوودز اسلینگ" را با سامانه‌های دفاعی موجود یونان ترکیب می‌کند تا در برابر پهپادها، هواپیماها و موشک‌های بالستیک، با استفاده از قابلیت‌های مبتنی بر هوش مصنوعی، عمل کند.
🔴
تحویل این سیستم در طی ۳۵ ماه برنامه‌ریزی شده است و ۲۵ درصد از قطعات آن توسط صنایع یونان تولید خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/144272" target="_blank">📅 19:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144271">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9-5P3SJMY8BZyOyGx3arPOa8uFAvcaCwVP64Yphnt0-RwteF_ZPdbuIMMD_4sqN1qd-SV3hJBmR3tNHnKQlgICuDwyXOz1vyICFFca2O_1LBgQtjeizi_lprkQx_C56LbXffJLzcUBszrzoE8koyvkh2g18h38wjxxGae0cweYaiw3l9A8J0Qg2aT53nxNHLRYO1fE4XeSUa5sSc93GIDXo3LEV51ybwdsJfRxUUbrIw4Eaa06wekUXD2UqPhjZDYZ1q3h9UIyX8ER1eixft4ObKXLXgwvipCc0dW6jzYjf3pfL59jdl6i1AqTqztIPBKhugg9m4rMwoh5Piy2oOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وزارت خارجه روسیه: ما هیچ پیشنهادی از اوکراین یا طرف‌های دیگر در مورد از سرگیری مذاکرات دریافت نکرده‌ایم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/alonews/144271" target="_blank">📅 19:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144269">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTAJ4wwiETeM3b91w1rgoSNASReM-cs5jFXVWKZV6wTkgsvIpnLFe7yte9050bWoHgKj46IQlTBJ-R2vzMj_3T5kys3BxXLbLNowEPORwyj9hgURAm-ELTtDXpolkexodA0s7ip00dRBbM1glZZaS-QdpJbZKv8B9dUUxJXc5-frAzy2D6Y8Q8LqfVtormdH3wrdOc9PgQflIx_hdFi9AlEnUBPupqEsfqXMWZF3UbTx2ijV87t_pafN91UC2vlCEHKASygXwP9fSLx0jsef7cxHbxqPbTfqc_OPBfzzwuUBtctEwT9SS4I6xf3MJ5bg-qzq7mDquFlJpffmllEF-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dcfe8ef66.mp4?token=g5Aq_G5_KXV9smQyYITy5740ESfXBmgbTHtVEojoHBBLPT_B1S2FW9dVpUsvSNQ6umi5Ld5smW6c1r3XR-aFat4-xK738azNwG3gwNcDLzIovfufhDy85em29fQeBK9L8Q9YY-LhM-P9KbhIO8XzSUfwY5KgG4BTcfjIn2O4-6GGhIKCtO1apqBQrIDUOM5OxwP6RiOuZm4Z66PtYZMZNGXNiEhCN6WFrqu6lXUWxv3TXhDBOZRFDRmhBrHgatDbL7RvLeX6mZyYs20rHdBxfZdXBZYBxylwaNzaEDTOaU2VKCZ-uQaYRzFrS1MRuJ0QhSTBlRvCFrJCfi068h5Kcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dcfe8ef66.mp4?token=g5Aq_G5_KXV9smQyYITy5740ESfXBmgbTHtVEojoHBBLPT_B1S2FW9dVpUsvSNQ6umi5Ld5smW6c1r3XR-aFat4-xK738azNwG3gwNcDLzIovfufhDy85em29fQeBK9L8Q9YY-LhM-P9KbhIO8XzSUfwY5KgG4BTcfjIn2O4-6GGhIKCtO1apqBQrIDUOM5OxwP6RiOuZm4Z66PtYZMZNGXNiEhCN6WFrqu6lXUWxv3TXhDBOZRFDRmhBrHgatDbL7RvLeX6mZyYs20rHdBxfZdXBZYBxylwaNzaEDTOaU2VKCZ-uQaYRzFrS1MRuJ0QhSTBlRvCFrJCfi068h5Kcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
«یوسف تیموری» بازیگر و از حامیان قانون حجاب؛ در سن ۴۷ سالگی برای بار دوم ازدواج کرد و به این شکل از‌ همسرش رونمایی کرد.
🔴
پ.ن: طبق منطق یوسف، الان مردها با موی همسرش حسابی تحریک شدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/144269" target="_blank">📅 19:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144268">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wBlCu8cP1Rla3qA8y29WHKYJ0tvSFswAyjkCs_W-J127M9_NJvOIQUwCvNIyQw8Yo1sm4FLTaAvwpcTG5d-gcJEbJgZR9K8ZXQfs0CuO3A2yw2BduSzDsb7G2UbfKVo9t4aYABXDFJGbzyiCh_oQZhOyh2lfzQ5kwN_v78xnRPEpoVwQWgwb8Tfk_YAz4UMPTfwU-VR_VV-Mlbl0UabLPTtohnWTMeXafMxCNmr-DRH9879FGPqWZNpUSniyU-fUHR1SP21mpoxLCbLi90oAKrDYC-hr6uGCe2ZIvm-Z_rhFkhv6dN123stYnyh8Eaf5G7b_fKo2IBQwO_EzKFcSOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله
جدید ارتش اسرائیل به جنوب لبنان و حملات توپخانه‌ای به چند شهرک
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/144268" target="_blank">📅 18:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144267">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
اینروزا این پسره حسابی سر و صدا کرده با سیگنالاش
🔥
هرچی گفته سود کردن مردم
😐
الانم یه تحلیل خفن از طلا زده
👇
https://t.me/+6PPyWURHtW5jN2M0
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/144267" target="_blank">📅 18:51 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144266">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وال‌استریت ژورنال: پروژه بزرگ «نئوم» عربستان متوقف شد
🔴
وال‌استریت ژورنال گزارش داد پروژه عظیم و آینده‌نگرانه نئوم در عربستان به‌دلیل هزینه‌های سنگین و محدودیت‌های مالی متوقف شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/alonews/144266" target="_blank">📅 18:44 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144265">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
عراقچی: هیچ‌گاه حادثۀ مدرسۀ میناب فراموش نمی‌کنیم، نمی‌بخشیم و همواره آن را دنبال خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/144265" target="_blank">📅 18:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144264">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V118_59mkkh-jhHsVR_d2fYKQ6PakJiSdBIBXZq36gLjQvwGllJ8DSCJGrJ8Ll9WrlxeQx4Ke1faLsCug4bPUGMMKrSQ9Kx6_F8pxfUkPekeVQf9-YzEblbJi6BfrjrlBqb0mI6OLqyDl2tX2n-xJFKkUw0sG0pMed6lLsZ-ZvN8d3AP2vtw8eP216_y0uHKR2UE56ffz4Ux3EnpetYJFgs4ecHF659YEOkVnFf6kTN9urnpy2rBHWmR7ft9bmA-ItooqjaNldX3_lZ84TZX094vFn018pv7F7W1fAOqENHkHqHhsdjd3eYXj414RxDRYxNqCRcT7AfisoVT4T4X3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بلومبرگ: صادرات نفت از تنگه هرمز به حدود دو سوم سطح پیش از جنگ بازگشته است؛ با این حال صادرات روزانه ۷ تا ۸ میلیون بشکه کمتر از سطح پیش از درگیری‌هاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/144264" target="_blank">📅 18:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144263">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dMySATCk2N8GX-hsSaut1qiinG5GgRcTf2v_QZ85Qpd1eu1o3d2XeB4k30rWVFsKJZy1t-H3kx8lLCr8b2J_JVLW9WHMFKXpE8fgU0XeBUsqGT0PIVMalHgDdM5fd0SX_CDFv5WiupSwoPFs0ctYqUU6Gp4dYfcuLaUmR-uhSJcRp9R1RBFy3bgP-DCgcIwDIlwVB-xI7nf2NYOk7GkSs-jQ3cUEqWWniMUHMYBKsfhEU92sXx6oBHYCbF5beGdbxSov9eOGMrtJXNyEeZWiCnqRv_RjpdPQCXsmPhGOjx_Dv6tw402VR3qKF3rgNd7QWbaDreJxwAk5hgog6fgQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسانه اسرائیلی : کشتی های که خارج تنگه هرمز نفت کشتی به کشتی میکنند واسه خود ایران هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/144263" target="_blank">📅 18:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144262">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
الجزیره: بر اساس ادعای پروژه داده‌های مکان و رویداد درگیری‌های مسلحانه (ACLED)، از آغاز جنگ در ۲۸ فوریه، آمریکا و اسرائیل دست‌کم ۳۵۸۰ حمله علیه ایران انجام داده‌اند.
🔴
در همین بازه، ایران نیز دست‌کم ۲۰۵۳ حمله در سراسر خلیج فارس و خاورمیانه انجام داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/144262" target="_blank">📅 18:25 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144261">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
بلومبرگ: جریان صادرات نفت از تنگه هرمز به حدود دو سوم سطح پیش از جنگ بازگشته
🔴
مجموع صادرات نفت خام و فرآورده‌های نفتی از منطقه به ۱۵ تا ۱۶ میلیون بشکه در روز افزایش یافته؛ اما همچنان ۷ تا ۸ میلیون بشکه در روز کمتر از سطح پیش از آغاز درگیری‌ها ست
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/alonews/144261" target="_blank">📅 18:21 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144260">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
رئیس پلیس راه مازندران از تردد دوطرفه در مسیر رفت‌وبرگشت در محور کندوان خبر داد و گفت: ترافیک خودرویی در جاده هراز نیمه سنگین است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/144260" target="_blank">📅 18:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144259">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ab5acd2748.mp4?token=CCNRxZTF03vV6_HPBJBm4FwQBL_S477CLGREgR1koMv_HkwTH8Np17Ulsn61Ik3ToOQnvTf2F7fDcSsmZ0wkkiVh5iIIGqhKALCBzV3nTCOzBAP1zbPx4Aip719l07R0W59ETtkcLqqlJPmeQqi8IBETifrYaRbKAkjZ-AmfUVJ4Oon-PDf3BMRDcMGlWs1KxAl2Uba1z7mVLl4kyAwvbJMlMoUC3WjUD6OQwQR7UcXC0-jr4AvaiKx4iRvic6hybGT_diZoInnMbf4FUZwU3EIATdGWMxCLaKt1ve7rsq5n_9Y0tlFPo67FpTngE4aas8RAbf8IZd_KytQ6kegxUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ab5acd2748.mp4?token=CCNRxZTF03vV6_HPBJBm4FwQBL_S477CLGREgR1koMv_HkwTH8Np17Ulsn61Ik3ToOQnvTf2F7fDcSsmZ0wkkiVh5iIIGqhKALCBzV3nTCOzBAP1zbPx4Aip719l07R0W59ETtkcLqqlJPmeQqi8IBETifrYaRbKAkjZ-AmfUVJ4Oon-PDf3BMRDcMGlWs1KxAl2Uba1z7mVLl4kyAwvbJMlMoUC3WjUD6OQwQR7UcXC0-jr4AvaiKx4iRvic6hybGT_diZoInnMbf4FUZwU3EIATdGWMxCLaKt1ve7rsq5n_9Y0tlFPo67FpTngE4aas8RAbf8IZd_KytQ6kegxUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هر دو تست اولیه پهپاد ADD (کپی شاهد ایرانی) ارتش کره جنوبی با شکست رو به رو شد و بعد از لانچ، سقوط کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/alonews/144259" target="_blank">📅 18:09 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144258">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نشست ۷ وزیر خارجه اروپایی و غرب آسیا درباره تنگه هرمز در استانبول
🔴
رسانه های ترکیه اعلام کردند که روز یکشنبه نشستی در سطح وزرای خارجه کشورهای انگلیس، آلمان و فرانسه و همچنین مصر، عربستان، پاکستان و ترکیه در استانبول برگزار شود.
🔴
محور این نشست که به ابتکار آلمان و ترکیه مطرح شده، راههای تضمین آزادی دریانوردی در تنگه هرمز و وضعیت امنیتی منطقه اعلام شده است.
🔴
کشورهای شرکت‌کننده امیدوارند که این نشست، سیگنالی به آمریکا در مورد لزوم ادامه مذاکرات با ایران ارسال کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/alonews/144258" target="_blank">📅 18:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144257">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
الجزیره به نقل از یک منبع مسئول لبنانی:
نمی‌توان حزب‌الله را با زور و در مدت کوتاه خلع سلاح کرد
🔴
اظهارات اسرائیل درباره شکست مناطق آزمایشی، اقدامی برای تعلل و خریدن زمان است
🔴
وقت‌کشی و تلاش برای به تأخیر انداختن روند مذاکرات به‌دلیل انتخابات اسرائیل وجود دارد
🔴
ارتش لبنان کوتاهی نکرده است، اما ما نمی‌خواهیم درگیری داخلی و خونریزی رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/144257" target="_blank">📅 17:59 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144255">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا: تحریم‌های جدیدی علیه ایران وضع می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/alonews/144255" target="_blank">📅 17:55 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144254">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزارت خزانه داری ایالات متحده؛ شعبه‌های بانک مصر (دومین بانک دولتی بزرگ مصر) در امارات را بدلیل همکاری با ایران تحریم (محدودیت مالی شدید) کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/144254" target="_blank">📅 17:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144253">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
سخنگوی دیوان محاسبات: ترک‌فعل دستگاه‌ها در موضوع بنزین را بررسی می‌کنیم
🔴
با وجود افزایش مصرف بنزین در روزهای اخیر، در شرایط فعلی کمبودی در ذخایر قابل عرضه وجود ندارد.
🔴
مردم نباید نگران تأمین سوخت مورد نیاز خود باشند.
🔴
اظهارات متناقض درباره قیمت بنزین به التهاب دامن زد.
🔴
ناترازی بنزین یک‌شبه ایجاد نشده است.
🔴
نمی‌توان ناترازی بنزین را صرفاً به قاچاق نسبت داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/144253" target="_blank">📅 17:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144252">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر کار: یک کارخانه‌دار می‌گفت وقتی اعلام نیاز به نیروی کار کردیم ۳۰۰ نفر برای کار مراجعه کرده‌اند و همه با حقوق پیشنهادی زیر هشت میلیون تومان آمده بودند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/144252" target="_blank">📅 17:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144251">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xa0lCplQPy8Is6v3PUnrjCiPx2Wj6ViFW4LnuGY3LXWA83vxwAlCjy4IcnAOEQzeLdrlxjpOrJAnXVcYmx7btBZThBGboxzcxjKMVh100Asv2zf9jj7gRLEyQ32BYMhqCo4_3--Xz2TAf3e_Yh9bZ0rpr1OLy5BUjuaT16ahbGks82kdeXUfLoCPoKbH8svAhWLlw4y08XCTzicw0QbM-ez_blv04WWGXOPPdLcgfSZTRMDbGpERY5n0SmWwZAxpxk4gd-8YZKMcKGwfg6baNjXdYbpuHBJM2mAs_mCkLrDu5NajuGBL0q1g6nKEzGVwYAD2nY4QJFrg1h_Xtr03vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
انفجار جدید اسرائیل در حومهٔ «مرکبا» در جنوب لبنان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/alonews/144251" target="_blank">📅 17:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144250">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sYT94ecDQVd07Lz8NJhwAocVxjKyj-J6o9IDEgzfbRHiJiQVtbEfJI7zU3JGhOKRSMNKnwocbZTFDuLhsQT8gGN-HJDNzLWFn3p4P68solbwTi4YuR4hSXddjJkbPjtof_VXQNkhpHtb2MA_7g9aCQ07dizCq7n8qzGdASQ6pD-gBkHjC2zADaCzR_KQCsd8RhSq5ABJgt_qPLjLpmxvwxn-epBlnFsvtqmgMnVbOdFmec55zNyyiUKGbiCy27ypwymTEzPtbnTwUMMQT4mQob7pagHk3VgdtEhCa5r5Kr4ZGzRs_XFpire8g4aJJ7Jg1enQ1X9_HJIB0W6c0iPy8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولینگو (معروفترین برنامه آموزش زبان جهان) اعلام کرد آزمون‌های این برنامه از ۱ سپتامبر (۱۰ شهریور) برای ایرانیا متوقف خواهد شد و دیگه از ایرانیا آزمون نمیگیره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/144250" target="_blank">📅 17:10 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144249">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDJohzhIOi-U-OHyvvkLMYjGT-a7hNnW-ut1F48eM_TcUMAdHuGD0j--DbTemv1GvQqRY3dWHiyQ3lHpaFMaz2Xr7vTclea2-BnWTzO53LqGiCBNvnOab3GEwKVuQ9DizCfK1XUvL-BaFzlIET6z7BBwewvt7tEpsNgpBm9fnXmS6xzAEEWLzmHiQIO_H_0hC4aO_0JdVfLS-ejwoxblgrIMm7onlFJGVP9jHLZbjz6wzIE83xM5PqG0FE2l85muRnPofX5rB0fmpsL1aCOfk1Q0yWxq5jMAsUyYnMa7mAaa6OQUTzrWikqTAEDAkOrydYFMQYAdvG1MqizAaVawMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رویترز: کره جنوبی از تلاش‌های ترامپ برای ازسرگیری مذاکرات با کره شمالی حمایت می‌کند، اما خواستار خلع سلاح هسته‌ای، آمادگی امنیتی بالا و نقش محوری در مذاکرات است.
🔴
سئول همچنین قصد دارد همکاری با واشنگتن در زمینه سرمایه‌گذاری، اطلاعات و کنترل عملیاتی زمان جنگ را تعمیق کند و همزمان برای مقابله با تهدیدات هسته‌ای و موشکی کره شمالی، رزمایش‌های مشترکی با آمریکا و ژاپن برگزار کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/alonews/144249" target="_blank">📅 16:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144248">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c129d7d8d9.mp4?token=VIvlJa6HrKO0s2hF173MQM4gbJw_06fPuSC4ChfpTHZCbxPG5UB0Y8kkq8trhybdokf8R7GhjD2vbgMJqEPGEYMDC7HW79qFYBqIm2-PbURh312G7GO5oXyRfHzVIauC1LOXlLqKp0nvXZaS4b-O9VRYqPSfpc44PcxcO_0Ktpt9K3ND8GTqsMnocamiXs4BxzSV5jjW8Kqwj4nA97mynKEQU7x4UDnxcrzneZinQiuWdW4s6GnBtOUH_aa2iWEFDeZOU3frr2CZVxl0CaXGRXc8ePnTHgOugFq_8NVPWVkJDDHoZo5dF34dK3dAcLp225YajvRmCR9iUB-sOvhMfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c129d7d8d9.mp4?token=VIvlJa6HrKO0s2hF173MQM4gbJw_06fPuSC4ChfpTHZCbxPG5UB0Y8kkq8trhybdokf8R7GhjD2vbgMJqEPGEYMDC7HW79qFYBqIm2-PbURh312G7GO5oXyRfHzVIauC1LOXlLqKp0nvXZaS4b-O9VRYqPSfpc44PcxcO_0Ktpt9K3ND8GTqsMnocamiXs4BxzSV5jjW8Kqwj4nA97mynKEQU7x4UDnxcrzneZinQiuWdW4s6GnBtOUH_aa2iWEFDeZOU3frr2CZVxl0CaXGRXc8ePnTHgOugFq_8NVPWVkJDDHoZo5dF34dK3dAcLp225YajvRmCR9iUB-sOvhMfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تو یکی از خیابون‌های ساری، یه خانمی داشت خیابون رو برعکس میرفت!
🔴
وقتی مردم بهش اعتراض کردن که داری خلاف میای، طلبکار شد و گفت من دارم درست میام، شماها اشتباه میکنین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/144248" target="_blank">📅 16:40 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144247">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">به جای روزی دو ساعت خبر خوندن، پنج دقیقه کانال ماهان رو بخون هر خبری درمورد تورم و گرونی هست اول اینجا میزاره
https://t.me/+6PPyWURHtW5jN2M0</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/144247" target="_blank">📅 16:38 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144246">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏
👈
عباس عراقچی:
همه کشورها موظف‌اند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند و تحریم‌های اقتصادی آمریکا علیه ایران کاملاً غیرقانونی و فاقد هرگونه توجیه هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/144246" target="_blank">📅 16:27 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144244">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S3QRLX9BMLYVZ17UT_-FRCw-2ZEvmjZNCP-QLCB8ZlzLBnUdxaikyaQ5Ladnz5i84e14OvlQDR15K9Hw4V66muym4rxhidVmK6A-Vk1_MGtaHVcsAZwx2jcCcAzloFgKysiLomXnIN_sI-V_BnWyc0yzezSDjVxt1I1L9wArcvTVGTE8Ks-IS8FIwRfVNJIy39EmG3ex-0Qdku1t5wGY0yYM-nORmbyJq-FHlEw7TMrWWAySxWPJP8-Q--ZBI5en-qLo0lDfCqSUV9DzDvJR1BBsKcC54TEkVAKAlnRpOBtXIiAqF47p_TFugtWPeKgVEVHH_GeCRo0nvsKDKWHONw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ:
دیگر خبری از پسر خوب نیست!
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/alonews/144244" target="_blank">📅 16:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144243">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hs8jonNZMa2WOE3R3cMYgRq2pNzP12X7RqSNrpSV-8Lx7AUXNZr_PKOH-xHEQ71wUTIfPvVVqC-iOpM5TsM-UvA1_u77aaGoRcpt7yMB_w_CbmV5jA3arnzxEPKEyo6Wf--sLr0Dmce8ZoxJlM3a-w_ka_j-Em6cteAYNnk12hKAg-D85nSe4BTEvPoTxnDHiVHZm3e4PUbrxla8WmMryoX2OG8i5Bi6lMM8NiXyl-bTu_dSt5zJzaJ-yZiwdW0KSIH4y_UJVUJ8VNIffzcc2otJW_6vPnaZ2WnMeFF3ewQjpOBEXlS3lnA_-uixqkOEHSub4dWBh4r5F4b1CK7d-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
تصاویر ماهواره‌ای نشان می‌دهد که یک فروند دیگر از بمب‌افکن‌های روسی Tu-95MS در اثر حملهٔ پهپادی اوکراین به پایگاه هوایی انگلس-۲ آسیب دیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/144243" target="_blank">📅 16:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144242">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCX56N06PJk86Ntpn84VEl4JebTLIOmSZwyoiZ_yAtgPcTHynvG4tL9-xHnZBKA9bi3V1mN91GZHIimfyD-7unyRAbJ1V8lVvDwZkEBXRfQxYgjlbq-eqVtmqvjFb8lRQxB6g-fIKwm7HhkXMEcIPeVuwneNOzS54O4Wx-xCfBYpleAH96dhFxpVM33Vi3qGQ6C7iWzcunGAokmZmntW7fwlrh_bV8pesJi4aSY2KRJgRU2sWjbN9QFQGTb18R2UQNXFv5XSboF_R3HORmvyS8hgPZAMun_s6NPMACV-0PTIU1mbLZTu4Y7oucCE-4mr7ZX9cnzJ7RArH_QZTRElXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عربستان برای دومین بار در یک ماه نفت سنگین به چین فروخت
🔴
به گزارش بلومبرگ، عربستان سعودی برای دومین بار در ماه جاری، محموله‌هایی از گریدهای سنگین نفت خام خود را به پالایشگاه‌های چینی فروخته است.
🔴
این فروش نشان‌دهنده ادامه تقاضای پالایشگاه‌های چین برای نفت سنگین عربستان در بازار آسیاست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/144242" target="_blank">📅 15:57 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144240">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3IdNVxqFhdIN1P3zMhYK5tlLCMGwI9v5SegYKiIb-kRpvJyOQEwfGyKiBgAX5P7BKt5Ycn2-GJg6SiKeqMQMCNc5_31CUCs9XH4VzBR-dSw-0uU32gOcCxK6AiA7tr6TMaG6ZvKY0osnkWBQXr7kIajy1EEfA3ivwYjZu07_yRZemn11zBRO1l5tyGSB7RDBGP7juvxIfm9oVefCuzPXmMmPewTPNLox3J0wXwcsuw5HGxVzx2iBXAWHdvKAls-Kt_SeauwKOcYOwdyk3XfS90gE1sJyuW3t5lS7gAh-zw4-W6F9p9k_s5ZF7mLzOsTJ9DKptcCm_gxn7oh6xtlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توهین علم‌الهدی به مردم:
اگر آمریکا بخواهد یک لشکر راه بیندازد، از همین بی‌بند و بارها و افراد بی‌توجه به دین راه می‌اندازد
#مفتخور
#بشکه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/144240" target="_blank">📅 15:45 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144238">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ko_Udi-5wnzKV5IMsl6CNeqryQNAHHo7j_Mo8ZIeQ-HXcQQf8s7uHVg26E6UOUnxWEmRkelm9fqOHuQrTuThfSlkNf9p-K9jpYdmv343LV0l6TSKEW0ziKsSbl41U3Oc8qrKtYlD0rPkUIVv-zGQiJPUzo55KGOvLk6ni2bOedyLKOoCP-vHVu8R6m1ywup5_BPp6ieVhUOPQhYiUo8ytMafQNuz0OSK7Ue9CR4hd8xLg_5p76VASWJPgED3JV0vMjIYltAWvUtQf404MtwPlmp3ASaAxs8neHDg2GAZCnNbMuH-RYzQ0dJPLb3CS-EYwFRfPuMC13d5jIBNMsndOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gv-wXxE2VY-tNI8vK7PMbzPm-hGLiUU9s4Hty0db4SMuvqPNTaeu9fA6cLFEGNMKkA2WH0-SzMZlLnVIlrswj7ehDyYu4nxh1WFIxFOGFQ4HNb-5jwCZaIu1ba89_8JVDkHSpnID63ZmSTJh4zFtS6vdICPXsapWX3ggGy03z8MqrEN8gbOECEt2aVt4bU4dGpYYxyO6zNAV9ozaTFOZO2MRdiNKuRbPy54ZIK_cW6CCL-liY8iuGGzlOI1EqPyMaGNIkPMsp3VBpvJu21HduSmSxOn1VorQfsWvnSzC_iY0KMK2diroTtwPz3hI7RiEpWfWGK9FMOCAY_HgQO3rOg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تجمع اقلیت بیکار و الاف در اعتراض به وضعیت حجاب زنان در مشهد
🔴
پ.ن: تجربه ثابت کرده زشت‌ها به خوشگل‌ها حسودی میکنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/alonews/144238" target="_blank">📅 15:41 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144236">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/omGDYFHm-30sy538kfwvoCO4kkyWuh4a2-Tahh4TPcEEpOVL4Ya0QB-ESuouRRQqb1JhPvCsHaZg_KKw5OEDWpfmNB6FzIN4uPday6vM2S0Lo2kdL2gcc9Le2OkAB2Bn8P3BlD1ZMZr4l2vbBwpDC_jwOUbaCn4I0bN2fjZx1YkRbFjHveO8E1BepMoEeRNaziB82XaubPV-3hKpg3KWHeMAuTV-EO_dPdgvrRAVk0YGz7sWjt8FQaoOCjUlCMVc0Cbv_Zs3W04xSaoJ54zh_uNDDr8e5RFhw_aRwE8sKbWzOpyR6k5pCHeqbT-1wPu2i2l9HaQKmHd7FDHTOhWhQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاهکار یکی از دانش آموزان
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/144236" target="_blank">📅 15:39 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144235">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
نتایج امتحانات نهایی تیر و مرداد ماه اعلام شد.
🔴
از طریق سایت زیر میتونین نتایج ریدمان خودتون رو ببینین:   https://my.sanjesh.org/
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/144235" target="_blank">📅 15:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144234">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ohn4HITbRqQ90gc5juETocUw676jzW9vH2YEgnUmC8_ZtSeQx6FtefeWRcPfZvOG4tC1AAeNtODDFHhE1tSNcXEE1A6RK2qsmGtruzj0oRXt3SmODlcOcZMs3wOAg33J_A16A-Oe8200watlDsaxD_edKrNG1Cqwq1YFPNpP5hxlP9BdTWtvFT1DJpUg3zShCN2qD0R3B7JyZQDpg5_ZycrGBUYXjNzB0zbkFESJMHnoytf8PkVy6Z5ylawp48CF-CE_B2LPCepJMBA11qfZ1AUedSUhceOgn8mw2uuUeallsSJYhgUiwxroSdsexARxiByBObVFP5-zlw-fjvromg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😐
😐
😐
😐
😐
😐
😐
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.3K · <a href="https://t.me/alonews/144234" target="_blank">📅 15:28 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144233">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYihsPTTxqwK-n9gywIiZgzVnE-P6jYmBfxd4tMvd0PXOEXjUu1m53rad7ctLdzwy0B4Zv6zZ3DQRqlsAsUc-hACfIpVZ260i9nZSVXSgDlEwqs84jjTqKmwCCVFgDrCidrdIRYP0XO4NbpdUFX-VVq33xZn8hlEa776NQj89L0BabRtgHXNZA6jFQSLPCQv-S7J0ClQdqKUbR3I3cXDTIatv4ON6ZcY2c40LurathIQaJcug7zV-wwgcEM6GrLqHdbZLfTV1eKdjfGoGdt7QAi1JbZRPrtct6PYQjsrZJHRhV2DoWxrFFFCGuIpLHbKy8GglUG6XRu1SCXhnhuJYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شاهکار یکی از دانش آموزا
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/144233" target="_blank">📅 15:26 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144232">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نتایج امتحانات نهایی تیر و مرداد ماه اعلام شد.
🔴
از طریق سایت زیر میتونین نتایج ریدمان خودتون رو ببینین:   https://my.sanjesh.org/
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/alonews/144232" target="_blank">📅 15:23 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144231">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
نتایج امتحانات نهایی تیر و مرداد ماه اعلام شد.
🔴
از طریق سایت زیر میتونین نتایج ریدمان خودتون رو ببینین
:
https://my.sanjesh.org/
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/alonews/144231" target="_blank">📅 15:22 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144230">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFOLLL0n-CIB0tkBdC2UUaK8a61uUZT2FuMOEON25jqyr_iK8h900Vknw85EBvxmRwpxFDogdMsD3c8sUE8TlVD7CCTqzS4JnVSDRFr4C3HJPyWqRJxNzgO9ltdr4A2mkHCInz7r6zSyNkQfaDInxRDmYzMqVegiz_vpKCQv3MbnP5a9Mej6nrAfJGDc7owxWR6B0TzhguHFBKETzTpQ-iV4DeY3HPKRd5D6OYqChcbmXahv6rKCCoR0SjgYwtbwW4nMFExpdy1r1N3Iw-jBQDBNr-HZhlMjAdMubOXCWW3CMQ6oAOoobSHpGnxX6HZXe-zHB5XVV83ZW4IOJ2Gmww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اقبالی، از نزدیکان جلیلی:
باید حکم زندان برای بی حجاب‌ها بدیم تا درس عبرتی برای زنان بی بند و بار باشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/144230" target="_blank">📅 15:18 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144229">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
حمید رسایی: حجاب از نان واجبتره، چون مردها حتی با مو هم تحریک و به فساد کشیده میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/144229" target="_blank">📅 15:17 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144228">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ckkDtyiiTt0o0KT9foGby9heldA5tLE-pGC5B6_ODsnF-lIOMKCIJ02lMhPESPySdGpbotE4oUDr4QPnOfL1M_aw9oor-X4JVmlaoV6jqMF16FTonIdUQ_s20AZusWYmu06sUyBjSF3Tk0Vx_1RDRwK62jqnVOiMC8hCMT8s4Cn1lcYj2GzGeEN4KT8BKAXYeaWFBNt32lqQCdvpklQlnnJUI3Q1miUKbtMSchxhYxlj9Na5chOLTSH09VODAx6a4ntbk6IlW7c22a95Rgj7q8Tx9MQz1TDNvR0x0dkRCd9bwp3vMxyj_eFZSdsYRPN1Rx373LMstZ9gcrste_nAvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمید رسایی:
حجاب از نان واجبتره، چون مردها حتی با مو هم تحریک و به فساد کشیده میشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/144228" target="_blank">📅 15:14 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144227">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SfjvjN-znWhdOebN61J4DcBopVRfDkNTWbtk1S984Xw-bvWWYcjWd0J6c-I28vNFl50dwCoYf-cWoNQ0wXo2KlqHP_NAel6C64hSSHWMVJ2cBRwJGGdFQhXtP29FonthBkhq8Xnk9e0U-PcnDvMzaxRmSmlUp2-gpUGndteNcuVyswwB8mySk8bIFOnEMzNW-aR7zLSLVN4_YZGAi0svPpp62p2FduGrr19FY9BoNoJnE6bnsI1bnhjRj6EBUkt0ea30eRk4r8TtBmMSDUCROkZzpzvugFuF3LUhZlOwsjELiZVpycW_BIlcgMhyFfWXXRxNQygemBFTm7DMDQeDAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تمسخر طرفداران پهلوی توسط علی کریمی
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/144227" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144226">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cadbbc54a.mp4?token=uY4ebh5eIzgxeNrK5icIsQRzEqLbRGS6FFii8i-kGGpnQ33bxgTIAr3q3TgBTJq5zFJ3EPJfdEDTiNnJpmtG2qVvXeaVCysRxZqj5WNTiAtICfhoTkgNhWlYnuHwMz4H4VCRbEorQKxMNzlgODUkineLcYDbJoyny4s7QFK-aFz6UQv1ggbQ7yGNzAVb0HQKWKdz4e3Wt6PpHB5wPcNrAW51QuNpUqPtWx3JXkBnKvds7NZdPLoIxGeuVutSXQaeP1VI0rpwsSrbi6_ZmPMv2xUrP605lfV2eUdbJUMfY2p1G4XHYIR6X9i3zfuL0FpOcQ9WZeEUtOuDLL4ZDuiA3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cadbbc54a.mp4?token=uY4ebh5eIzgxeNrK5icIsQRzEqLbRGS6FFii8i-kGGpnQ33bxgTIAr3q3TgBTJq5zFJ3EPJfdEDTiNnJpmtG2qVvXeaVCysRxZqj5WNTiAtICfhoTkgNhWlYnuHwMz4H4VCRbEorQKxMNzlgODUkineLcYDbJoyny4s7QFK-aFz6UQv1ggbQ7yGNzAVb0HQKWKdz4e3Wt6PpHB5wPcNrAW51QuNpUqPtWx3JXkBnKvds7NZdPLoIxGeuVutSXQaeP1VI0rpwsSrbi6_ZmPMv2xUrP605lfV2eUdbJUMfY2p1G4XHYIR6X9i3zfuL0FpOcQ9WZeEUtOuDLL4ZDuiA3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو: ما اسلام را ویران نکردیم، من قصد ویران کردن اسلام را ندارم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/144226" target="_blank">📅 15:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144224">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lH1adrjdUFwG_D9D-8PGjqu4WX8FJawA3RiRjSGl3dgK5k3kO4Yi-I-lAfvw9U_fWOVFYWXI7u2ErxvOkHAEpH4O2nlMOz6evYW3aP3wAnaZNtD53W34baI0NHlxJQ-k-5Sq4ISOGJdzK8XmPKe8xue1f4sRMabso49QuIiF2CK3u5u6ClLL1a-TbOqCnIm_0KUfjmO9YKSoN3Rfme06Xf0bwcdqgmy9Ovaoz_nCuEO0WCJjxOi36dZ0T6yNjrGMYJi6Hc1EDP4uu-0cgy0TjSANCUMO2IObZBfD3AkLyDtwkDCKROH7eww7ruxF3jH_p5gz16WZh_5jsgDbiEVl7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
وضعیت نزولی ذخایر نفت چین
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/144224" target="_blank">📅 14:56 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-144223">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
آکسیوس: هدف ایالات متحده این است که تا اواسط سپتامبر، عرض کانال اصلی را افزایش دهد تا حداقل ۵۰ کشتی در هر شب بتوانند از آن عبور کنند، و هدف بلندمدت، بازگرداندن ۶۰ تا ۷۰ درصد از حجم صادرات نفت قبل از جنگ است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/alonews/144223" target="_blank">📅 14:32 · 06 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
