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
<img src="https://cdn4.telesco.pe/file/TfjLwu_097OoJnoZ44M-Ji9pmihqQz1FjWjyseytQvM5kXS0ZGqnn8_cutxsxKo6T6jJgf8vd2CqPQVoj6t-G1NA56-GIdEWYH1wDV9JldK01dIJNphvdxIg3vvpd61JYlqgIg_Gf7JDWbSoqs_G652deWwyUjA1SbvITEbBfccgT0Pfnr7TpOKj6RTbp2kwHiIMl1nuBEMp63atZWC1zdiPSjMDDhJzf0JsL-yguXDWXTHpT_Mz89dRXcJtPqMadMYZlayostozdqb3OBK4RX9dO4Q0tmcVbIDtIpksecISNeSEsH4JrNXhk_4_GzGKJ3iolp7co1zWyncW9grGhg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 133K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 15:56:08</div>
<hr>

<div class="tg-post" id="msg-69622">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
الحدث:
توافقی میان ایران و عمان در خصوص بازگشایی تنگه هرمز در ازای احتمال لغو محاصره آمریکا، قریب‌الوقوع است.
@News_Hut</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/news_hut/69622" target="_blank">📅 15:37 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69621">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiB5x62V4UunRwyOVPGONd-RFcnHPFm6FbjnwZutgiOz1yFyaw04QWxIeqN4RkeNTcuq6pvyiltMBCppaxblRqRBEUCYYT_joWbqQvnV6SKPGaK0-gjHhWsIcIWm8cHVSa1BXbiiILz4XWM0nvpAyCP8ywv41mB3lwLIH2HrcqiYNAtbzxzhMNpWbqeNhWoeJ9RChkjl-tDu5jkkhkcaxH5xnAbxWaTSB-4zc735-YoQ29I1yN4juRtJcLVMRCgw1MY-Fm07oZB0icXnvwDYNsS5HGLQxwe-PDZzCadtP720e0-3S108SBuNWeqgNef0NO-YvLTBtIEB0YRFmWuZaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
واشنگتن پست:
🗣️
ترامپ به طور خصوصی به حامیان مالی جمهوری‌خواه خود گفته است که می‌خواهد جی‌دی ونس در سال ۲۰۲۸ پیروز شود
و از عباراتی مانند «ما باید جی‌دی را انتخاب کنیم» استفاده کرده است.
مشاوران تأکید می‌کنند که او هنوز به طور کامل در مورد جانشین خود به توافق نرسیده است و هنوز رقابت بین ونس و مارکو روبیو، وزیر امور خارجه، را حفظ کرده است.
🔴
یک منبع این موضوع را اینگونه خلاصه کرد:
«جی‌دی دارد به موفقیت می‌رسد و ترامپ آن را می‌بیند.» و خاطرنشان کرد که ترامپ دیگر به طور معمول نمی‌پرسد «جی‌دی یا مارکو؟»
البته او با مشاورانش همچنان برای این انتخاب در حال مشورت است
.
@News_Hut</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/news_hut/69621" target="_blank">📅 15:28 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69620">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHRwKYdA8i9yQ933erKjRP2BRqqtWZyhb2Tp7sTto8F6qElY1PmPzcCmMSNFmBUPoW2lRmK2VdJDlj9vFlrDChvjA64UkWatzLFGz8Rr2UzV2tk8w_FZTyHQNXuoUUIZG0vCnHuIMUPAY66-huGsTbyco_GG8P36tQlM3FXR1XhtFo2mscKl-mNlbrzLqcyu-uCCi3Y-v0-epDTOkot4gOwOJcId7wHJnIh0fZbTs7NhLLj2djwQAsYb3jGQEd5cpTI4zFU47A6vnG1dUZbIxMjy2f98-4wkpRzFZhiKVp7GX_tshIYZ-fc-AIwqxrCCHqiqoUgrML-fa0u7kRmFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
آمریکا از ناوشکن جدید کلاس Arleigh Burke Flight III؛ USS William Charette رونمایی کرد
نیروی دریایی ایالات متحده مراسم به آب‌اندازی و نام‌گذاری ناوشکن جدید
USS William Charette (DDG-130)
را برگزار کرد. این شناور از نوع
Arleigh Burke-class Flight III
بوده و بخشی از برنامه نوسازی ناوگان ناوشکن‌های موشک‌انداز آمریکا محسوب می‌شود.
◀️
نام‌گذاری به افتخار «ویلیام چارت» از نیروهای نیروی دریایی آمریکا که نشان افتخار Medal of Honor دریافت کرده بود.
🔼
ارتقای سامانه‌های رزمی
نسخه Flight III نسبت به نمونه‌های قبلی Arleigh Burke دارای بهبودهایی در بخش سامانه‌های دفاع هوایی و موشکی است.
مهم‌ترین بخش این ارتقا، استفاده از:
◀️
رادار AN/SPY-6(V)1
این رادار آرایه فازی فعال (AESA) بخش اصلی ارتقای ناوشکن‌های Arleigh Burke Flight III است. این سامانه برای کشف، رهگیری و مقابله با تهدیدات هوایی و موشکی طراحی شده و نسبت به رادارهای نسل قبلی توانایی بالاتری در شناسایی اهداف دارد.
◀️
سامانه رزمی Aegis
سامانه Aegis یک سامانه یکپارچه فرماندهی، کنترل و مدیریت تسلیحات است که داده‌های حسگرها را دریافت کرده و امکان کشف، رهگیری و درگیری با تهدیدات مختلف را فراهم می‌کند. این سامانه هسته اصلی توان رزمی ناوشکن‌های Arleigh Burke محسوب می‌شود و در نسخه Flight III با رادار AN/SPY-6(V)1 یکپارچه شده است.
❓
نقش عملیاتی
ناوشکن‌های Flight III برای مأموریت‌هایی مانند:
⬇️
دفاع هوایی ناوگان
⬇️
مقابله با تهدیدات موشکی
⬇️
اسکورت گروه‌های رزمی دریایی
⬇️
عملیات چندمنظوره سطحی به کار گرفته خواهند شد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/news_hut/69620" target="_blank">📅 14:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69619">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=MbbP4pG0abWelm6K51zY5ZO342FwtfE293orovXHlZFChhH0qxaxfv68Qu7WwAeJe7luXPni_g5BWy62zbLp0oGWcyiaxYj7gNhHHtOOp8CSFVZh-y9A__bC4XIq8Cpx9cdSmrE8bP2KC1a9am1u_LHfnEVGcbRnicM_qBDoiC_DVzieqxJyU5DXB5VpHdLTDsXEsSYGm_4oTf0o-1Al8CEEgpJKZPOAmGYnkSzFWhd49BBzM5f1DUyf3BeHZXgKhdE121um5tAM5zawMr7SPIllzQ8O4aXxQnvQZQvK29IsJygLSZxbz4YvbEdAuOXxAnodzwSravovsGyL_FTYsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b6e5f9de.mp4?token=MbbP4pG0abWelm6K51zY5ZO342FwtfE293orovXHlZFChhH0qxaxfv68Qu7WwAeJe7luXPni_g5BWy62zbLp0oGWcyiaxYj7gNhHHtOOp8CSFVZh-y9A__bC4XIq8Cpx9cdSmrE8bP2KC1a9am1u_LHfnEVGcbRnicM_qBDoiC_DVzieqxJyU5DXB5VpHdLTDsXEsSYGm_4oTf0o-1Al8CEEgpJKZPOAmGYnkSzFWhd49BBzM5f1DUyf3BeHZXgKhdE121um5tAM5zawMr7SPIllzQ8O4aXxQnvQZQvK29IsJygLSZxbz4YvbEdAuOXxAnodzwSravovsGyL_FTYsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
مراد ویسی تحلیلگر ارشد اینترنشنال:
قاجاریه در عهدنامه‌های ننگین گلستان، ترکمانچای و آخال، سرزمین‌های ایرانی در شرق و غرب دریای خزر رو به روسیه واگذار کرد.
حالا جمهوری اسلامی، از سهم ایران در دریای خزر به دلیل نوچگی روسیه می‌گذره.
مردم ایران، این روزها رو برای تاریخ به خاطر بسپارید؛ جمهوری اسلامی در حال رقم زدن خیانتی بزرگ به ایرانه.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/69619" target="_blank">📅 14:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69618">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=ofJmCq23j_lKgX7CW8VsxfzPuzXr4JPJ1ODXcRebO3tmvm0jh4TC9pQm0baeYj7IlL-HD1GNF75a0L7ES-to3Wvw0CNeEEZK6X_HTsu7LJvcQZLMk-nYDO94zxnysAKvni4o_1ssSUtqlCJpbIBRzZNYh0GSOw6p_t9_YGKZ4Bv0eaClf7i1MiRoh-U5GJsqnUgYrlfT93xPUfdyCshajd0U6WIDYUmn5jnq7yNnx__MajSCUKc7kk4lcVUST8vCTv04RvLm_SA7K4je_CgWbX4ORYkQG-kR_rfvy4epQyLEEX0irSKEa7NPr_rFU_nlpE1F51j6g47rWcihyXYWyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de4ded641.mp4?token=ofJmCq23j_lKgX7CW8VsxfzPuzXr4JPJ1ODXcRebO3tmvm0jh4TC9pQm0baeYj7IlL-HD1GNF75a0L7ES-to3Wvw0CNeEEZK6X_HTsu7LJvcQZLMk-nYDO94zxnysAKvni4o_1ssSUtqlCJpbIBRzZNYh0GSOw6p_t9_YGKZ4Bv0eaClf7i1MiRoh-U5GJsqnUgYrlfT93xPUfdyCshajd0U6WIDYUmn5jnq7yNnx__MajSCUKc7kk4lcVUST8vCTv04RvLm_SA7K4je_CgWbX4ORYkQG-kR_rfvy4epQyLEEX0irSKEa7NPr_rFU_nlpE1F51j6g47rWcihyXYWyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو ای از صحبت های یک دختر درباره مادرش:
❓
کی گفته هر مادری قابل احترامه؟
از میزان اشغال بودن مامانم اینو بگم که تو سن 13 سالگی پریود شدم و وقتی بهش گفتم منو تو خونه 3 روز زندونی کرد و گوشیم گرفت و کلی کتکم زد
بهم گفت تو چه گوهی خوردی تو هنوز بچه ای چرا باید پریود بشی؟ و این خون یه چیز دیگس!
از 12 سالگی هم منو میفرستاد سرکار میگفت باید خرج مدرسه و خونه رو کمک کنی بدی!
همینطور که اینارو میگفت تا اول دبیرستان بیشتر نذاشت درس بخونم و 15 سالگی ترک تحصیل کردم
مامانم گفت لازم نیست درس بخونی باید بیشتر کار کنی چون خرج ها رفته بالا اجاره خونه بیشتر شده باید بری کار کنی
به محض اینکه هم 18 سالم شد از خونه زدم بیرون و الان 6 ساله نه میدونم کجاست نه شمارش چیه نه باهاش حرف زدم
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/69618" target="_blank">📅 13:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69617">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=UIgwHemPib2U-cUBxwwE6FqxkakvNFUZ7X5DZxpe8LHl6lOU2rWsZpDE44RE0v67dYLWTYhLXtoRyPTBLuhytWyjElE9pFtVrucUue0K4j8aiGw9zCspkS8-dUGpnB9TNLEBWXMLL2WeElTriSpnGtXIlbBrSHpsHsJF2EjJtzsflUdu1aRXkRUscLA4-ovOW3GjxAD1cYvhuBuxl0fD4qtTtzA9pcd0TYVC6dTqShtOvfBHTUU10HXk8f2I-u_vv3Q5vdyvwiCwSKQNNqHwKbSMaFt27w18NDV3Nw72K2yHoVftsGyzCBW4cvCl6Un5SdsazJeFAgYUQvpSLOO_ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e79de90eb9.mp4?token=UIgwHemPib2U-cUBxwwE6FqxkakvNFUZ7X5DZxpe8LHl6lOU2rWsZpDE44RE0v67dYLWTYhLXtoRyPTBLuhytWyjElE9pFtVrucUue0K4j8aiGw9zCspkS8-dUGpnB9TNLEBWXMLL2WeElTriSpnGtXIlbBrSHpsHsJF2EjJtzsflUdu1aRXkRUscLA4-ovOW3GjxAD1cYvhuBuxl0fD4qtTtzA9pcd0TYVC6dTqShtOvfBHTUU10HXk8f2I-u_vv3Q5vdyvwiCwSKQNNqHwKbSMaFt27w18NDV3Nw72K2yHoVftsGyzCBW4cvCl6Un5SdsazJeFAgYUQvpSLOO_ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیلمی که یه خانم حامله ایرانی از میزان تکون خوردن بچه‌اش توی شکمش منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/69617" target="_blank">📅 12:51 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69616">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QK3zh7nVzGOzv8urkM6sKjUUAgz4zdXG7E-PH-y4LRdA6WbpUQQl2Sfho_mUSopr_nZsTr4Y6JQQp065Uc5Y0fYhNSIVKGfca3WE6ZW28fKrIUBhcl8gM9iLwILAlMJoDwodiZD4yB8eiQoQBRuACv5gk1s9U4PeNNrVwzCnH2SRh2p5OxcQZCDuU1_bnxH4KUmx6OO-PUdSn4WAu__hFAHaWJWCGqpn5Li_Oj3a2Jf-lzwTKJ5sMxAv2DPTAFCzytfpxxFa0HsFpe5p4lzR6Ydb8XMRSH0AWQRXEM1hshp5J2j8BJsM_RpJFWmde2lhNvpRjazHy21p-h0wQVp3Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
گزارش واشنگتن پست
:
دونالد ترامپ، رئیس جمهور آمریکا، هفته گذشته در کمپ دیوید با پیت هگست، وزیر جنگ، درباره کمبود شدید مهمات در ایالات متحده به شدت صحبت کرد و از او خواست توضیح دهد که چرا به نظر می‌رسد او در مورد این کمبودهای شدید که اکنون تهدیدی برای محدود کردن گزینه‌های نظامی است، فریب خورده است.
ترامپ در جریان جلسه کابینه در کمپ دیوید به هگست گفت که فکر می‌کرد مشکل کمبود مهمات "حل شده است". هگست از خود دفاع کرد و استیفن فاینبرگ، معاون وزیر جنگ، را مقصر دانست و گفت که او اطمینان حاصل نکرده بود که ترامپ به طور کامل از میزان کمبودها مطلع باشد.
در همین گزارش، روزنامه واشنگتن پست به نقل از یک مقام آمریکایی، اعلام کرده است که بیش از ۱۳۰۰ موشک بالستیک تاکتیکی MGM-140 ATACMS ارتش ایالات متحده در جنگ با ایران مورد استفاده قرار گرفته و تقریباً هیچ‌کدام از این موشک‌ها باقی نمانده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69616" target="_blank">📅 12:20 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69615">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=hs0Ra1ODMt_VFgHfth0Ld5WDBR71YzjpBTQhDbpYp-33YMMrpA_Ace8Bp_MKzU4M7_MMan5E1SGj8YeegrjHy5FNFmw49cUdZeRLO6I7dJPD5P01W6WdYP7gzSjpkkWZODDqXQTySivR7erGu2PP4c1LWYdBbVzB9GrXDcNn4BiuAfZ4iIQ0S2r1-fBKffjtpBw0Ih-XzabhuZjVzaAWeduH_T5A9RFITpOHj4Xlvx-VcmGKQnQ--Jcz26VceFS77odXdiIx_4M59-R0cQTmPfdqooiE3rJF868l_s8ZTu4-C7jz5WgliIWcBcdY_cfiSkhgTptpoeKNUyV_lxCjww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58d9f385e0.mp4?token=hs0Ra1ODMt_VFgHfth0Ld5WDBR71YzjpBTQhDbpYp-33YMMrpA_Ace8Bp_MKzU4M7_MMan5E1SGj8YeegrjHy5FNFmw49cUdZeRLO6I7dJPD5P01W6WdYP7gzSjpkkWZODDqXQTySivR7erGu2PP4c1LWYdBbVzB9GrXDcNn4BiuAfZ4iIQ0S2r1-fBKffjtpBw0Ih-XzabhuZjVzaAWeduH_T5A9RFITpOHj4Xlvx-VcmGKQnQ--Jcz26VceFS77odXdiIx_4M59-R0cQTmPfdqooiE3rJF868l_s8ZTu4-C7jz5WgliIWcBcdY_cfiSkhgTptpoeKNUyV_lxCjww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این نقاشی هنرمندانه با ایجاد خطای دید، باعث می‌شه دیوار صاف خونه طوری به‌نظر برسه که انگار داره به سمت بیرون خم می‌شه و برآمدگی پیدا کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/69615" target="_blank">📅 11:53 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69614">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9KmAVsQxldQPBagcPvceFS3ti8kRj20gpAuRXVzRtq28R9SMfr_nj-IDQKdk0PoIa_pZkSMDrZp32AcyvfBVFsxCC7p0feMkRAJVWtFR7iR1eqSkIElBv-2gKrdGRxWjdnPZKacnKa58d8nzNQvSDE_rJH8o-FgUVTjMD5g59X_Yju_e2csyeSm5BmFC3VIVmVm9i_G0BvTBQZ-N3YQ6Per7rFpHFOz5Lss2HlpmHHqyIl_saKpV9OM2Nv5Y_hrotyrii7eclDEgzYPswcZK9iT4Vrl6pjc8P_1Xj1nlliNnBVjXNo1OSxY99EWFfNyRY6VpVu8Yc4KVbISN3Aasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
مرکز عملیات تجارت دریایی بریتانیا (UKMTO)؛
پس از دریافت گزارشی از ناخدای یک نفتکش در حال عبور از تنگه هرمز، هشدار صادر کرد؛
این ناخدا گزارش داده بود که صدای دو انفجار را در فاصله تقریبی ۹ مایل دریایی در جنوب شرقی «کومزار» عمان شنیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/69614" target="_blank">📅 11:25 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69613">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=L2UgWNTcy5ZTHUm4SgJyCIcPXMfjYVvBx6IADUHUcQn4NdvFCBJPa2Nvyk9RZrumovA4bUQaX6BIQbDroVftJ_Ys8WF6nKG5X91--p1oGigf4-itp6_mQreOC7Y1LnnUw1-3NLpcror5dDi_OjNxnjyshKzHJufrenztCC4K8CIGL_GtNQ7luu9pSuXOEQasBERl6-7r5IJe5JDCpSu2keXWppD8_ZRSZs4nEVL55NXNa0NIBEpoSpjLTizr-uztshtG7Vky__XElBS9_x8jgxuoBgff-tS3ltmF1wahOat7sa0sDA1pSRBHL4bK0F2Ygq3MLlz4Nvn4sBpH6_nggw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54b71c6863.mp4?token=L2UgWNTcy5ZTHUm4SgJyCIcPXMfjYVvBx6IADUHUcQn4NdvFCBJPa2Nvyk9RZrumovA4bUQaX6BIQbDroVftJ_Ys8WF6nKG5X91--p1oGigf4-itp6_mQreOC7Y1LnnUw1-3NLpcror5dDi_OjNxnjyshKzHJufrenztCC4K8CIGL_GtNQ7luu9pSuXOEQasBERl6-7r5IJe5JDCpSu2keXWppD8_ZRSZs4nEVL55NXNa0NIBEpoSpjLTizr-uztshtG7Vky__XElBS9_x8jgxuoBgff-tS3ltmF1wahOat7sa0sDA1pSRBHL4bK0F2Ygq3MLlz4Nvn4sBpH6_nggw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
حسن روحانی: اقلیتی می‌گوید اگر این جنگ تشدید شود، امام زمان زودتر ظهور می‌کند! می‌خواستند برای سخنرانی امام زمان در تهران جایگاه درست کنند.کاسبان تحریم ممکن است خوشحال باشند که جنگ ادامه پیدا کند.
عده‌ای دنبال کاسبی از جنگ هستند و از ادامه آن خوشحال می‌شوند.
در جامعه ما گاهی یک اقلیتی هستند که حرف‌های عجیب و غریب می‌زنند.
یک اقلیتی هستند می‌گویند اگر این جنگ تشدید شود و گسترش بیابد، امام زمان زودتر ظهور می‌کند! برای ظهور امام باید جنگ را تشدید کنیم.
خب یک عده افرادی هستند که نه با اسلام آشنا هستند و نه با مهدویت آشنا هستند.
یک عده هم هستند که دنبال کاسبی هستند، همان کاسبان تحریم در واقع. آن‌ها هم ممکن است خوشحال باشند که جنگ و آشفتگی ادامه پیدا کند.
افرادی هم هستند که ممکن است یک تفکراتی داشته باشد که ما باید برویم جهان را بگیریم و تصرف کنیم و همه را به اصطلاح هدایت کنیم.
من در سال ۸۳ رفتم خدمت رهبری برای یک موضوعی، بحثی پیش آمد در آنجا، ایشان به مناسبت فرمودند که فلان آقا، اسم بردند، آمده بود پیش من و از من سؤال کرد که می‌خواهد یک جایگاه بزرگی درست کند در یک میدان بزرگ در تهران. گفتم جایگاه بزرگ برای چه؟ گفت برای اینکه وقتی امام زمان آمد و خواست سخنرانی کند یک جایگاه مناسب و باعظمتی باشد در شأن ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/69613" target="_blank">📅 11:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69612">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxGLgKUB5OwXoXrDgl1W5WfwLOBB1W-z8Jn3KuUQ0kXzLvqPZN_YNy5OiD-I3QWtwWBrCwDC7NAXXnuf8uCaCRWmpTc-cb4H2mI-ftuEGDaPUU-wZdvtsqJzYXHZ6RQjj-tTwa6xC0Ch90EVd64KXwlRbk00qs11xbSvNeNtA38RxhygkdaEBqQTOxBkDz4NBswDsffm1_8y1jR2XLTaYnz9-AngqZYMd0iEyFKj80taS4nuvfkZ2FYXiSlL9Q9_mXPqNsyPbHSxkTxfO-VShfCEMLNqOwORDNy_yQaZWKvZHVY1rop1Y1CYQfq_b4vnCCHyQiTIGpCQq0s9nKuSbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐
اکانت رسمی تلگرام زیر توییت یه کاربر:
یه نفر پرسیده بود: می‌خوام بدونم دورف(مالک تلگرام) کجا قایم می‌شه؟
تلگرام هم جواب داده:
درباره خودش چیزی نمی‌دونم، ولی معمولاً منو خونه مامانت می‌تونی پیدا کنی
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/69612" target="_blank">📅 11:14 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69611">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69611" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پنالتی
راحترین بازی پولساز
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید راحتو سریع برنده شو
👌🏼
💖
مرجع
بازی های روز دنیا در ‌پلتفرم جهانی بت اینجا
⭐</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/69611" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69610">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=qk-nFtGfPMCXwzYyQQwHRuHXTqBuwSWtMYmsaS-Ki8BZj23m4-9bkuploofbnJZKMJCIYJaRIW0U_6JsoX07Fbe8Ume-Zfc_58mg_PycZbbET02N77dFYSgyy_y37mh16PXiI5ysJpBeAWB6nkp6jG2n9-xc5FsKWkezHf-NpJfH5Oiz-8f1eQtXpVGaRx9mBmO3IF-KKlo3mu1Dbz9riVLDdxLP8kG1Evn93tfXXPI350afgecWvg7rnhvTIM9yp2ucz7ADz7sAaeOslQHJo0cfgthuRt2cpTXWZuZ8QWFJNw9XtoOmFmmap4fuKrHXck6LqD7_NODvkZwT55Rpa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58d65b8db.mp4?token=qk-nFtGfPMCXwzYyQQwHRuHXTqBuwSWtMYmsaS-Ki8BZj23m4-9bkuploofbnJZKMJCIYJaRIW0U_6JsoX07Fbe8Ume-Zfc_58mg_PycZbbET02N77dFYSgyy_y37mh16PXiI5ysJpBeAWB6nkp6jG2n9-xc5FsKWkezHf-NpJfH5Oiz-8f1eQtXpVGaRx9mBmO3IF-KKlo3mu1Dbz9riVLDdxLP8kG1Evn93tfXXPI350afgecWvg7rnhvTIM9yp2ucz7ADz7sAaeOslQHJo0cfgthuRt2cpTXWZuZ8QWFJNw9XtoOmFmmap4fuKrHXck6LqD7_NODvkZwT55Rpa4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
آقاآآ این بازی
#پنالتی
چقدر خفنه
⚽
🟢
بازی خیلی حرفه ای و‌
#پولساز
پنالتی فقط‌ پلتفرم جهانی و معتبر
#بت_اینجا
✊
همین الان ویدیو
#آموزش
پنالتی زدن ‌رو ببین و با شارژ اضافی
🤩
🤩
درصدی که سایت بهت میده.
💖
حتما ویدیو
#آموزش
رو ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
r15
@betinjabet</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/news_hut/69610" target="_blank">📅 11:13 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69609">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1558a77094.mp4?token=PY3bsXkG3DYkeJVIWBJLxSVhxirzLboyUVORauE7nzwN87mCDrGnUqmwMYEtqAke3xqqoQk0Iqhtx5t0GN5XQ7CgbCD1jM188yWMfipEi6OnIYFF_OqMynHV8ogjoSt8aLcC-vnbESvVSwGVVlX6ZZS1-lZW8YBVBTq0nRAbrJNjBS54Do0BIZ9UzOiNe2eGPxK5KzwFH9bTxWxdzxlZwm4A8J1lkxDJNgG07lKYqhlkT8C7pRjNAX6LTev8R151rVbOi1J4m79rT0eUlR8TwYkh1b_LiojTGoIsJPzB-6dJjGbT7E_jB8ChbI9Pz86j_X29RBMq03BWHp7_EWZqfw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1558a77094.mp4?token=PY3bsXkG3DYkeJVIWBJLxSVhxirzLboyUVORauE7nzwN87mCDrGnUqmwMYEtqAke3xqqoQk0Iqhtx5t0GN5XQ7CgbCD1jM188yWMfipEi6OnIYFF_OqMynHV8ogjoSt8aLcC-vnbESvVSwGVVlX6ZZS1-lZW8YBVBTq0nRAbrJNjBS54Do0BIZ9UzOiNe2eGPxK5KzwFH9bTxWxdzxlZwm4A8J1lkxDJNgG07lKYqhlkT8C7pRjNAX6LTev8R151rVbOi1J4m79rT0eUlR8TwYkh1b_LiojTGoIsJPzB-6dJjGbT7E_jB8ChbI9Pz86j_X29RBMq03BWHp7_EWZqfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپی که حامیان حکومت برای موشک‌ها درست کردن
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/69609" target="_blank">📅 10:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69608">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=bw1bdbN3MoYH_DqEGBQMWfi21YL7IxMKIN2tEVBuca0z9EsjhP71DRkBCCO4kABLdvcphhhgcchJyHYjCfB8AAX4hiXxdHoe8yJpnBhaIbvachwnEscblrIOX_R66W9XhqVFl9cJ1ZFmCNeyTaB8M3YRZo0OlrfZtD5Pdag4zz9-bi8L-RTyxtwSkXUtDKURuynv_TZIql0SBqh6xhuVJrx2xLSFyD9DiW8FQvDOUphYqE5QtKNCiWt-fZe2c79WrshvXpg8g_jD7UtuMeJFnDUoHQdsac8ZJHPb-34m8Yt6Dyu-fzN4kOdIKg51UyeIT6kXFbSp4d9ECvJ2NyZlRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc659092fa.mp4?token=bw1bdbN3MoYH_DqEGBQMWfi21YL7IxMKIN2tEVBuca0z9EsjhP71DRkBCCO4kABLdvcphhhgcchJyHYjCfB8AAX4hiXxdHoe8yJpnBhaIbvachwnEscblrIOX_R66W9XhqVFl9cJ1ZFmCNeyTaB8M3YRZo0OlrfZtD5Pdag4zz9-bi8L-RTyxtwSkXUtDKURuynv_TZIql0SBqh6xhuVJrx2xLSFyD9DiW8FQvDOUphYqE5QtKNCiWt-fZe2c79WrshvXpg8g_jD7UtuMeJFnDUoHQdsac8ZJHPb-34m8Yt6Dyu-fzN4kOdIKg51UyeIT6kXFbSp4d9ECvJ2NyZlRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
🇮🇷
پزشکیان:
حوادث دی‌ماه پارسال قابل فراموشی نیست؛
یه عده بیگناه هم قاطی اون اون افراد تو خیابون ها شده بودن
وقتی روند به شورش رسید اتفاقات سختی رخ میده و ما دیدیم شرایط اینطوریه گفتیم کد ملی اعلام کنن و هرکس اضافه تر میگه هست خب بگه
کسانی که کشته‌شدگان رو ۳۰-۴۰ هزار نفر اعلام می‌کنن، نامرد و وطن‌فروش هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/69608" target="_blank">📅 10:02 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69606">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=k8WahlDW11x3V-jzss1ThYjcLQi1xxIU5Ohjs_RVrfbCnOhlpS1omaUAwl3mY-8Qt-F0HvIcmOrMDZotBzsahj-41Jj3BRE0J8SiNYRnEDXT5J1RsbotGa1TWA9SKWlHx_O6S5kTIi2ZolapO83d2oyuzV6vdd5JDagzfi4oNCgiaUjN4VxtREJkxP1P4gdqPuNUKqY1DbdCMycvjxl_Dai1aPo6mQT8dJnTTiZnRVbMyVf5bivgLbeb5cDRuQEyZitgudsVDjaxsdAZAlGRGAejlE6tQwoo5pj6JEcvGwaqOpbY_2qUO5y6MAconwDboC6PhX6SRLHPDmOgnxqS-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8bd143a1.mp4?token=k8WahlDW11x3V-jzss1ThYjcLQi1xxIU5Ohjs_RVrfbCnOhlpS1omaUAwl3mY-8Qt-F0HvIcmOrMDZotBzsahj-41Jj3BRE0J8SiNYRnEDXT5J1RsbotGa1TWA9SKWlHx_O6S5kTIi2ZolapO83d2oyuzV6vdd5JDagzfi4oNCgiaUjN4VxtREJkxP1P4gdqPuNUKqY1DbdCMycvjxl_Dai1aPo6mQT8dJnTTiZnRVbMyVf5bivgLbeb5cDRuQEyZitgudsVDjaxsdAZAlGRGAejlE6tQwoo5pj6JEcvGwaqOpbY_2qUO5y6MAconwDboC6PhX6SRLHPDmOgnxqS-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
باقر خرازی (برادرزن مسعود خامنه‌ای):
ما باید از جمهوری اسلامی گذر کنیم. علت اینکه این الدنگ (پزشکیان) رئیس‌جمهور کشور شده و بی‌حجابی کشور را گرفته این است که هنوز از جمهوری اسلامی به حکومت اسلامی گذر نکرده‌ایم.
خدا لعنت کند شورای نگهبان را که این "آشغال" را توی پاچه ملت کرد.
چهل سال است با آقامجتبی رفیقم؛ او بسیار تندتر از پدرش است؛ اما یار ندارد.
باید به نیت حضرت فاطمه از هر شهر ۵۳۰ نفر جمع کنیم و به تهران سرازیر شویم و کار دولت پزشکیان را تمام کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/69606" target="_blank">📅 09:15 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69605">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=C0kxf-l1Hr2A3Vh4FzIwYIctlfma0IZku8dlF5L2F2B9_Pdpy0Cs1w2OP_hrB1JmoIi4neHzFcloC-UjgMsw0Ha9EGjSjmECqjoR5dWmJtwkjy3ReB9GF03b7Sm5nqerPnN4qEH-zVP_Stcv-hlsX3w2PAKKVRL0svYmHf8FRC-Qv0_JWaK2WtBFpEx-qOZuobifihxZpKjb_IhOB3p2dtOhv3JrijPwKKmz2SpzkOjYKxYDXiOywR73KF6SYciZoSbf6kY8D-hg_hB2Et5neqhtd0SzY1ZCsiMYetBpdgZeY1yxIn4Fi3MgnZdTYWJTNBZ1a5hNrDOg2nDR4Hwj3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e59bbff0.mp4?token=C0kxf-l1Hr2A3Vh4FzIwYIctlfma0IZku8dlF5L2F2B9_Pdpy0Cs1w2OP_hrB1JmoIi4neHzFcloC-UjgMsw0Ha9EGjSjmECqjoR5dWmJtwkjy3ReB9GF03b7Sm5nqerPnN4qEH-zVP_Stcv-hlsX3w2PAKKVRL0svYmHf8FRC-Qv0_JWaK2WtBFpEx-qOZuobifihxZpKjb_IhOB3p2dtOhv3JrijPwKKmz2SpzkOjYKxYDXiOywR73KF6SYciZoSbf6kY8D-hg_hB2Et5neqhtd0SzY1ZCsiMYetBpdgZeY1yxIn4Fi3MgnZdTYWJTNBZ1a5hNrDOg2nDR4Hwj3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
ممکن است دوباره قیمت نفت را «بالا ببریم»:
«قیمت ۷۵ دلار است. ممکن است مجبور شویم دوباره آن را بالا ببریم. خودتان می‌دانید وقتی آن را بالا می‌بریم چه اتفاقی می‌افتد.»
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69605" target="_blank">📅 02:01 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69604">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/69604" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">⚠️
#پیشنهاد_ویژه
⚠️
🔥
حتما ویدیو‌ آموزشی بالا رو‌ببینید بازی ساده و بسیار شیرینی که راحت میشه میشه ازش کلی پول درآورد
👌🏼
دنیای سرگرمی و بازی های جذاب رو در این‌اپلیکیشن تجربه کنید
⭐</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/69604" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69603">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=SuFsuZlEmRCUrVjj50D-sxLa6U_s-AhzT3JjFTJ9EVo9R1ZqdksjqKKDQUx0h_Tis_nKEWNhp4spotVsvm_YtvmEZLYllOxoH34K3SZQe26kYmdpMMiE76Sl_H4qq7sCCQYlUjEo_2uw38UEcrOBRZKS6SmH2VNNumolPFvIiASBIeo6iEZojnfBMWBWwk9UQz4YWr4xHEHe3_MpoM5Caf5J0P2ytv3peRenwQP8uN5pAKOfNBsR1SltQ0rp2QHCvtSE4zJDCIJ_amDUxEYSAzTlgKHyE1W3OPkIHp4wGL6sJvS6n2nLZ_5EM00MOd-N9G0Z2RBalxJ6ljeNcK9opA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/936a75dbba.mp4?token=SuFsuZlEmRCUrVjj50D-sxLa6U_s-AhzT3JjFTJ9EVo9R1ZqdksjqKKDQUx0h_Tis_nKEWNhp4spotVsvm_YtvmEZLYllOxoH34K3SZQe26kYmdpMMiE76Sl_H4qq7sCCQYlUjEo_2uw38UEcrOBRZKS6SmH2VNNumolPFvIiASBIeo6iEZojnfBMWBWwk9UQz4YWr4xHEHe3_MpoM5Caf5J0P2ytv3peRenwQP8uN5pAKOfNBsR1SltQ0rp2QHCvtSE4zJDCIJ_amDUxEYSAzTlgKHyE1W3OPkIHp4wGL6sJvS6n2nLZ_5EM00MOd-N9G0Z2RBalxJ6ljeNcK9opA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖱
به راحتی کسب درامد کن
💵
💰
🟢
ویدیو
#آموزش
بازی chicky choice رو براتون گذاشتم خیلی راحت و بدون ریسک و میتونی بازی کنی و کلی پول دربیاری
🔥
💖
حتما ویدیو رو تا انتها ببینید
💻
لینک سایت بازی:
💻
betinja.bet
💻
betinja.bet
🌐
کانال بونوس های رایگان
a14
@betinjabet</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/69603" target="_blank">📅 01:48 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69602">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=k9CAxU4EXlzUDPgejp9VsKrdy0Vf1ZXqSIqH2L6OFot0Dsb2pE8IPlWxYd2owpUtcTsLdXi_K32TtkhSa9znsvgNUaoXms3KjLrKrV8nhi0q3d1hS2kgrv8PyBchmcPphCtnmlRfebssQo5oAS6xGwnCi5bl2E-Q4NRO6V6QlrqBMBSC7nBNJyB-JEq44sfi7UGwfkP9qbiKKRCY6j7OekUsFqJs-vUFWbl8fPr7ThAr9P1-PJCR_OQq1bH1i-w5E_T8DpID3PEnHiJdb5p4Nj7Sitf0oeq-M45VkIgB-nDuD8tYVIuHXl7EW4K02qd47RyrxIBRy4w9qqqrJhBOQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79ecaba828.mp4?token=k9CAxU4EXlzUDPgejp9VsKrdy0Vf1ZXqSIqH2L6OFot0Dsb2pE8IPlWxYd2owpUtcTsLdXi_K32TtkhSa9znsvgNUaoXms3KjLrKrV8nhi0q3d1hS2kgrv8PyBchmcPphCtnmlRfebssQo5oAS6xGwnCi5bl2E-Q4NRO6V6QlrqBMBSC7nBNJyB-JEq44sfi7UGwfkP9qbiKKRCY6j7OekUsFqJs-vUFWbl8fPr7ThAr9P1-PJCR_OQq1bH1i-w5E_T8DpID3PEnHiJdb5p4Nj7Sitf0oeq-M45VkIgB-nDuD8tYVIuHXl7EW4K02qd47RyrxIBRy4w9qqqrJhBOQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ترجیح می‌دهم با ایران توافق کنم، چون نمی‌خواهم آدم بکشم.
ایران به ما احترام می‌گذارد. آن‌ها به ما احترام می‌گذارند.
ما در حال گفتگو هستیم. ببینیم چه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/69602" target="_blank">📅 01:22 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69601">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=pxUSujv-3Rl8OiXXfMvXLYQljw0mo51GFW8ZDb0LvoCtRaVORXWB81jSXuiKBtWH2sd4-Xg2MD7phzG2BMS4XF2Erb4x2xsuRjOYh7nEwtKX9peUiEuMw_pLyfMuQxGMlZl826lDC1UyDVq5TziGq_VT14pmXqWfuje0RWTQQ21CoOc0vB_2W43L1aXhhRC9SrQJu0GhvTa2mzscn0kpvQU-hI-yjZH_bFfE0R2lB2zGR2NWqkSFR9j6PxxC1zOIdaAmU-3K_QxpacqqVMiOot7diJfiEjegIgNHk1Ml3cPEUFaTA24hKdiRWXGdWj4D5Y7DVXAf7j2-WNobMxTvoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca4b2dd818.mp4?token=pxUSujv-3Rl8OiXXfMvXLYQljw0mo51GFW8ZDb0LvoCtRaVORXWB81jSXuiKBtWH2sd4-Xg2MD7phzG2BMS4XF2Erb4x2xsuRjOYh7nEwtKX9peUiEuMw_pLyfMuQxGMlZl826lDC1UyDVq5TziGq_VT14pmXqWfuje0RWTQQ21CoOc0vB_2W43L1aXhhRC9SrQJu0GhvTa2mzscn0kpvQU-hI-yjZH_bFfE0R2lB2zGR2NWqkSFR9j6PxxC1zOIdaAmU-3K_QxpacqqVMiOot7diJfiEjegIgNHk1Ml3cPEUFaTA24hKdiRWXGdWj4D5Y7DVXAf7j2-WNobMxTvoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
هیچ‌کس نمیدونه که کلمه «dumb» حرف «B» نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69601" target="_blank">📅 01:00 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69600">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🇷🇺
🚀
ویدئو منتشرشده از شلیک گسترده موشک‌های اسکندر به کی‌یف و حومه آن در روز گذشته.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69600" target="_blank">📅 00:50 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69599">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTaJ9YZPScV5_S6PgHLPuPGYOCuh5GxbxtGcUQR0V3QXgMVcOw-oVPwmw1hbrQ0TdCE_O1wyAOitU94-MfXbvo-C7cah1vfDHvxH_vTRVah6OVFuUa0W_kUusOecySuinwcMtipDk16mfcjmK-cOUjD86xHJ1Wp7x_o27mfyj-AyCNach0GRqu1qOij5QuRVIIbbxWIQ-0wQUUg44iqztcaG4fkRuzbyAl3PXypvNiJmwUcBk7FB9MoGDKtNSq-elXVvfBL90kYXy4djLAV8LTaf73oT2xmUdCBzbUEnfRH8ks0rwIj0PRha9JyfuU4_HY7sBSssI7FWDc-frNNnMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ مود:
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69599" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69598">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=f-vbOAVl0rYyNbMDT_37dGmw_H9dCwUD0h-rIoaG4SfcgOvaxhJJnicscVqmmdWNkFvR35KBj09DMP7qJzYc_B_-jy8DuWAuC12WbTms5HKZkXx-z0PwhvsN3-6yDjxVOeMqYRC-i3wqtOqaT6MYUHLh1J2Aobnh0UhqfFxCm8mYXDwxS9gphyKSZJmfJuznswcj70LbmlW47WOYd9zFQ-CNyOj1JS7qNBGJNdOf81kKBfdeo6pwPoVV1g3LEvGbWu2dQhHDsoO90bruaXKVUni0ONPSv0DnHN3yXn1zCXF657kux97hAdiG-1ib71se5yfK7CCJ6Mi7Qf66PS-LDg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/82acfe6016.mp4?token=f-vbOAVl0rYyNbMDT_37dGmw_H9dCwUD0h-rIoaG4SfcgOvaxhJJnicscVqmmdWNkFvR35KBj09DMP7qJzYc_B_-jy8DuWAuC12WbTms5HKZkXx-z0PwhvsN3-6yDjxVOeMqYRC-i3wqtOqaT6MYUHLh1J2Aobnh0UhqfFxCm8mYXDwxS9gphyKSZJmfJuznswcj70LbmlW47WOYd9zFQ-CNyOj1JS7qNBGJNdOf81kKBfdeo6pwPoVV1g3LEvGbWu2dQhHDsoO90bruaXKVUni0ONPSv0DnHN3yXn1zCXF657kux97hAdiG-1ib71se5yfK7CCJ6Mi7Qf66PS-LDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فیلم وایرال شده از یه کارگاه آموزش فن بیان توی تهران.
چه خبرا؟ به لطف شما:))
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69598" target="_blank">📅 23:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69597">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=kTqoK6RLlKZgYkuUfgt0Ir1O2X3rg5u7WcWX8WZ_qlzeko3jIBZy5NYFEhhTfKvFTSGL6mdD-ylycHO1ccjbu90cEp1MSM9BgiyfAWK6f1Cwuf56W_4E5BKYS5En9amcMgmhPVe9uA1dZab0muU9R6UzgtAflv9BOuPZ8jN3QiZFSqgyq4vi7QHzdD4AiIL-PHNLr9IDr9D-1b1X93ezER87Z_QzEkPUTz-2tyZ5QF4LfANtimEVuaJuYhgL__aMsHqY4Gm1mDoQa5vSZbLn68X4aQM58CQE5r3akXAEDJvoAEVyccQHjGav7cpRNR2Zs1ZedqnmEdUH4PBjOQRF1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51c05821a8.mp4?token=kTqoK6RLlKZgYkuUfgt0Ir1O2X3rg5u7WcWX8WZ_qlzeko3jIBZy5NYFEhhTfKvFTSGL6mdD-ylycHO1ccjbu90cEp1MSM9BgiyfAWK6f1Cwuf56W_4E5BKYS5En9amcMgmhPVe9uA1dZab0muU9R6UzgtAflv9BOuPZ8jN3QiZFSqgyq4vi7QHzdD4AiIL-PHNLr9IDr9D-1b1X93ezER87Z_QzEkPUTz-2tyZ5QF4LfANtimEVuaJuYhgL__aMsHqY4Gm1mDoQa5vSZbLn68X4aQM58CQE5r3akXAEDJvoAEVyccQHjGav7cpRNR2Zs1ZedqnmEdUH4PBjOQRF1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
دیروز یه خبرنگار از بقایی، سخنگوی وزارت خارجه پرسید چرا جواب صحبتای ترامپ رو نمیدید؟
بقایی گفت چون باید رفتار ایرانی داشته باشیم و حرکات زشت دیگران رو الگوبرداری نکنیم. آخرشم یه تیکه از یکی از حکایت‌های عبید زاکانی رو گفت : "فعل و عمل ما را و دعوی ایشان را"
🔴
حکایت کامل عبید زاکانی:
شخصی اَمردی به خانه برد و درهمی به دستش نهاد و گفت: بخواب تا بر نهم. اَمرد گفت: من شنیده‌ام که تو اَمردان را می‌آوری تا بر تو نهند. گفت: آری، عمل با من است و دعوی با ایشان. تو نیز بخواب و برو آنچه می‌خواهی بگوی.
🔴
حالا معنی حکایت:
یه مرَده یه جوون بی‌ریش رو پیدا کرد، یه سکه بهش داد و گفت دراز بکش تا باهات همبستر بشم [ کونت بذارم ].
جوون گفت: من شنیده بودم تو جوون‌ها رو به خونه میاری تا اونا باهات همبستر بشن [ اونا کونت بذارن ] نه تو.
مرد جواب داد: «درسته؛ عمل کردن از طرف منه، اما حرف و ادعا با دیگران. تو هم فعلا دراز بکش، بعدش هرچی خواستی برو درباره من بگو
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69597" target="_blank">📅 23:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69596">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇮🇱
بنیامین نتانیاهو:
ترامپ بهترین دوست ماست، اما می‌خواهم یک موضوع رو روشن کنم: "موجودیت اسرائیل قابل مذاکره نیست.با توافق و مذاکره یا بدون آن، هر کاری لازم باشد برای تضمین آینده‌مان انجام خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69596" target="_blank">📅 23:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69595">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Esgard-VPN.apk</div>
  <div class="tg-doc-extra">42.4 MB</div>
</div>
<a href="https://t.me/news_hut/69595" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پیشنهاد_ویژه
فیلترشکن محبوب اسگارد ‌وی‌پی‌ان
تقریبا با همه‌ی اینترنت‌ها کیفیت اتصال و سرعت خوبی داره. حتما امتحانش کنید
لینک گوگل پلی:
https://play.google.com/store/apps/details?id=com.vpn.esgard&referrer=628035</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69595" target="_blank">📅 23:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69592">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kpAnE54Gyh5M_6D8K0T6vk3GsGNxEFlhNLz5wJ8dOj-RSoOXolR9UqMnz0zxBa5ZqC745bFQS1REPQazzsHQWQ-TLslDfXoO1AOmEYePxSmUf7_2oeDjrz-_4kBO6uLBH4d8nZs6_TLyyRnNogSlvNCF24MkleiZqWiWvcvP04SSxah30bBz7AMw1eRJ7KMx7TFaCVwZ1ZbNR0QJcYsrl4e-M-6GYsAJRpRy469A6wGLgSwu2vmwnazUuYH4KV-74F_zguBvOA5X3ED2h1kAmecd4QhKdoXM96HUul7Bq6ge7VIkFW1eavKeIAZ4zNn-1-4HPYMhzfJrPIqdgGfcFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gX-TgHCaBuMRPo21M79Ks84piJXzqNHbGK7U0mj9MjQRTbhMRILqKlA0X3N8-4S8c0eaUfnOTqHVKBgwHv34jNNhY2Y60nd73zhIZRxXYvG62gsfWLIbVbEOj54l7HgIBDSb8CjNqXIxfSvoYuOeFMs_yawFgQRoGmiN53t1RQ--2Sf9z8rt4NHLoTHL5hxclxyE-fSlmLMmFQal5s4B-diu5GOnGRjyUHzi0BNylvwn50TMc_yJOUy6lOvq-fImpgO5qzqpWQbuvh5CPp5BsNF13hbepS6BNQRVluczZfeWzZChHedL4B1KSdxFjILIXUJHD460OWbil16Tp-P6GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=v5wE3m6eAmBAWKBKvSN41YK_ljRbn8FsCp2tHUC9ED5W9qyiNbv9Xl48uT8Cx5rUn1IMn5r1bL6bKrog_mKXl1Odu36ryh07OEI1E1FzF-3aXB2MCI64zrFpDlgKeSgIcmvX3lBeWJBq7sCYLxoC09g8UIGHkYr_iv7LefBUCmiwkPI3NR0FtqDJ9jN0xeRMLZnfUL7ybawRuYmAbR20f6t7ydXGAdDvrgk0gnhBnHWBjE3OY3jTvXpekDacJ9SFmCF0siKj1L7h7XnAYgCrnjgvYOfUDR3uFA4PEX2woKiZMRyfoTKasTLtLuBPvCQDWQEUnJcGLRxgzyekQ1ko-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6780226a9d.mp4?token=v5wE3m6eAmBAWKBKvSN41YK_ljRbn8FsCp2tHUC9ED5W9qyiNbv9Xl48uT8Cx5rUn1IMn5r1bL6bKrog_mKXl1Odu36ryh07OEI1E1FzF-3aXB2MCI64zrFpDlgKeSgIcmvX3lBeWJBq7sCYLxoC09g8UIGHkYr_iv7LefBUCmiwkPI3NR0FtqDJ9jN0xeRMLZnfUL7ybawRuYmAbR20f6t7ydXGAdDvrgk0gnhBnHWBjE3OY3jTvXpekDacJ9SFmCF0siKj1L7h7XnAYgCrnjgvYOfUDR3uFA4PEX2woKiZMRyfoTKasTLtLuBPvCQDWQEUnJcGLRxgzyekQ1ko-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو لیگ دسته سوم تایلند، بارون میباریده، ولی همینطور فوتبال بازی می‌کنن
یهو یه صاعقه میزنه و صاف میخوره به یه بازیکن و اون بازیکن فوت می‌کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69592" target="_blank">📅 22:32 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvWg1y3cP7Klh5_CAHbtXxpy_kF9jhy14KFi0X6m200jqjSvx6N2I_ajP803i9w0-EyZqS7dJwgAFujXPE7qfMrCfrYxhKCRyPCTpHeOcJkw84E0LYG0g7HkCHstoGwIdSSF56wwDU-GmNva9POxhZIeI_z7ZDG5HAooKJZfhcnvJZbQDnwMSYzp6sajYsg9inHDvZsXSHe2drNvkEvhEEwZLyt8262jy9Xm2SmQnEwKNoKGp2vn9Pw-BF1BFEqJ3LMKshvV-0uP2Y-qncQOji0uU9FZ0aijlnjLZeratz8oWs5V_OvWuHjRyCW5uwDJfSbMDh9c4Z9zAeHtO4lVcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
🇮🇶
وزارت خزانه‌داری ایالات متحده تحریم‌های اعمال شده بر شرکت هواپیمایی فلای بغداد و چندین فروند از هواپیماهای آن را که در سال ۲۰۲۴ به دلیل ارتباط ادعایی با نیروی قدس سپاه پاسداران در فهرست تحریم‌ها قرار گرفته بودند، لغو کرد.
این لغو تحریم‌ها، شرکت هواپیمایی فلای بغداد (که با نام عراق اکسپرس نیز فهرست شده است) و دو هواپیمای بوئینگ ۷۳۷ (YI-BAF و YI-BAN) را از فهرست ویژه اتباع تعیین‌شده توسط OFAC حذف می‌کند و به تحریم‌های مرتبط با تروریسم آنها پایان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69591" target="_blank">📅 21:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPaw0qx88yQMq1jxFX5FY-nOAHIG8Gxx5aUMmCLDDRekkKKMOtLXhLl_C7HE6lzRfiGJTlfu2VgMizad0KFi7jkKvQ1honHiSLQmIzDtepNfoDoWg-W_xml1R7mJGi45kF5av7OR7icUBGSZ7Qrjay0YECSGn6pmGB0tKUm-0IJhnrUxM7fU-ylyP5xgH8T0SVQZrwKABnZiQ8Z-DVHNWoUdFd_ZAdRPonYFp4wnO8cDufZWYwUma_JFVISsRNPd8GiqrubIS1cfDMbtfgrab-_KXBCG19TltHPlTzZbOvFEiBYkgzKz4o5YPrUfnq8MvN4xQCcAkR95x-M9ijnM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی:
ایالات متحده تقریباً ۴ یا ۵ روز پس از آغاز دور جدید درگیری‌ها، پیامی مبنی بر درخواست مذاکره و حل‌وفصل مسائل ارسال کرد.
هرگونه توافق در خصوص تنگه هرمز باید صرفاً میان ایران و عمان باشد.
ما هیچ‌گونه دخالت خارجی در تنگه هرمز را نخواهیم پذیرفت.
با اجرایی شدن توافق جدید، مسیرهای موقت فعلی در تنگه هرمز بسته خواهند شد.
بخش قابل‌توجهی از مسیرهای تردد کشتی‌های ورودی و خروجی به آب‌های سرزمینی ایران از این مسیر عبور خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69590" target="_blank">📅 21:17 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca751f3e8.mp4?token=GQAuoe0pmBOIdAIPeZY8E0BSjVrZWdT8_0ihmgxCcjz48n4-NQRWsPGK23_as7Q1zvwU3_tcc7Cileb3b-14fC1I1erQogllKPncSUF1dXBz481cieZ1UBF4NuTBtjMK_bCZwrEFXe4jle9qSU6Fqm3IZIJIoRZmXrflF7Pf-ldrgNoYl6uHpi6yUBL7w-9TrkQ4XPwFd0XsmCLm3rPsuiCBDhnFm0KYzou9kDdus0_8bQ-MB8eSg9tXy7bSnRafSJAnrk470bE5qDTs6EH2VJKTVzpDO9I5W6kl0ahbnJDo2pq7DlBc5sb1LsjGMz--DmKxsrEGVN5h2U-fze4jVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
❌
🇮🇱
امروز در پی وقوع انفجار در ساختمانی تله‌گذاری‌شده در «مجدل زون» واقع در جنوب لبنان، دو سرباز اسرائیلی کشته و هفت تن دیگر زخمی شدند.
حالا قراراست بنیامین نتانیاهو، نخست‌وزیر اسرائیل، و یسرائیل کاتس، وزیر دفاع، ساعت ۲۱:۰۰ به وقت محلی نشستی امنیتی برگزار کنند. محور این جلسه، حادثه مرگبار امروز در جنوب لبنان است که منجر به تلفات متعدد در میان نیروهای اسرائیلی شده است.
به گزارش شبکه ۱۴، انتظار می‌رود مقامات سیاسی در این نشست درباره انجام یک واکنش نظامی قابل‌توجه گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69589" target="_blank">📅 20:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12fe6dbab2.mp4?token=ZAaeXpxz60vGRalSsCHIy0s-IOwhgcDnX-2PIBBDaIwSl8VgtQfIGYx64OATKB5_JDizJcoXhN2N02WFMa7Egi5Ah57wktDlkb3AIECHlvjXiFK-KyLJ1qZiDszFRkTpz9B3a8fQWJLa4g_q-11Q-6cR_n6_UBI1Ih7gs1SJIY9POC3UC_Ad54n-BgIuzMo1lrbQIVNUT1sFdG8D_B4i2G9qRZ-bmBYbK03fHJjgvf7pBvqM_wo8i_awAd6vqvEylsDMDj9fAd1O_rJlUCIQWNcmANt7xXGNoaEc8bOQgZOUYyKa15klI90erX9JDsrQQhoVzNpYZzDgTk_9oNtlTarrJRbJN6wckK6Rkfk0iK8pT-VU2PM3ri5FVOLkahQt4ZWRlNXa7_eNBeDfJRGncFT7U7X26kh6WHZSfaznAaKPsKferyX-gLT-rsf3XP4sYcpZ7Xyj6WpNvAlixepDX9cfc7xjQDFgcu5JemsQAItZ-D2eeDrdTlOY65LAGZIhZ5__08vBiXLonxu0T_aMeh2fPamNAexFtr4Tozo_wFbg-vDNbro-isi2Kwt7AXPtMKoZtUZHhEPreooHNkD4Fvxc5DfDW9PwiTLnzBYBxYwgP2OuNMmZAZHYtGL1-94Z7RHaMxBM1_A_CrWMKD_WK7D3vLQtT96tCeeHcWH8bPI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فاصله ایران تا آمریکا با موشک فقط چند دقیقه‌ست، اما پیاده باید نزدیک ۱۹٬۳۰۰ کیلومتر راه بری!
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69588" target="_blank">📅 20:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0660a7fbd.mp4?token=BKgwkZefWWmNU_pEUzwVR9uWLzELLsOTDfauAyCXg1mh6UlmoKugXza6OexcTq6B1oT_Z11V6QkerukZF_LSAHvkgOVjtOsTOzw2Zo79koYvNis64nbDzosLBr-rth2zlT-YQcb1wW9SJcZ1uQamm-CKoY-CtoHOftWLWpF4zCWZcwTUvBWRXuEYzwixaXOteo4I03LgWKwnm68nDLqUexkZQxp2VVNjaiqc-FJ5klbj2gcbnZojiDKVMdAvH8yrphM7DNU_E_ZWpErqEGhf3rZQSCg3FllmU0vv-Z93Yk3C4D6rAnqnWiOzywKm8e1YrBlsTtXKmr4Azjw1Cutn5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
ترامپ بزرگ ترین دوست ما هستش اما به صراحت میگم وجود اسرائیل قابل مذاکره نیست.
با توافق یا بی توافق هرکاری که برا آینده مون نیاز باشه رو انجام میدیم.
نیاز های الزامی سیاسی مجبورم میکنه این مراسم رو ترک بکنم.
در حال حاضر توی یه رویداد بسیار مهم نظامی سیاسی هستیم.
این جنگ موجودیتی هستش.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/69587" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69586">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">خفن ترین تیپستر های ایران با هم جمع شدن و TRUST BET رو تشکیل دادن
👍
هیچ سایت بتی دوست نداره شما این کانال رو پیدا کنین
رایگان بهترین شرط هارو براتون میذاره
حتی هزار تومن هم دریافت نمیکنه
سریع از این لینک جوین بدین کانالشون
👇
(این پست پاک میشه)
g14
https://t.me/+cBQ8n7zLQiUzN2U0
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69586" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F1mVBnOY9Il_iowEyHWyypryntWUbv4xZG88JfOx5l82PU7NxP6LNl0T6UcoyZIqvwpvo7SwYBoi8FXN3KxZSpCE7qhyZS4pqjBHELpJTkf9cnvTp-tMSjTGpH8QAe-nIvmuyxzZoNWbtK8xZBGnmJIs_KEqOhvUbS0Wbts4F4ghFaXN_AfnGUmKSBQCGIn4BvU8yfAv2iI35kVRJaNQo7m3hGxWXD82eQW3iBtFLg6QuCPJamSikHcljwBqe5zv5fPkhNGxotQwPGEkYNSQtxV20hkEF9-Xy2wSanjTQ0H9q8b-XcXKiZgcfjrEFt6tz_dIm9jFX3kLLvi5nWp6UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">40 میلیون تومن برداشت روزانه ی کانال تراست بت
🎁
پول دراوردن از بت تجربه و استراتژی میخواد نه ادعا
برایند ماه تیر توی کانال تراست بت: 78 درصد رشد سرمایه بود
✅
40 بازی اخیر 34 برد
📊
💠
https://t.me/+cBQ8n7zLQiUzN2U0
g14
💠
https://t.me/+cBQ8n7zLQiUzN2U0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69585" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69583">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19fc284b17.mp4?token=GgpTwNeM3J9akqUFNh-tqJc3SM1zGMrp627DForFApulrT8XpLskmUxoz2ErJUp0B92DdOXIQ7qIDxDcL_5bG_1Dz8T4QnNOwgY44-kGl5km6LUFUY1OlnaUFiTaCwZIPkUjbUDtQV5A2_SbpH61uYWu9rj-i_Z3ayLnc6G329_OiNtwtcU5UDaE9VT1DaEdsz7_2ZtjNXYrjnE163Fhay1pWfQ9DkwvOrgIS1ntlpEnMgditxSnV7XPHO-jYgfxJ32waS0HTYcKMuu87_FTR7jgntK_csbgFRmCcoyyhHGClWiCkNj6kmAoJN-DhPe7zUt2cVpjmVr7KGsqGEnGhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
پلیسِ رشت یه ون آورده وسط خیابون و شروع کرده داره به دخترها اخطار میده؛
بعد واسه مشروعیت دادن، یه مصاحبه از این خانم رشتی رو منتشر کرده که‌ با میگه:
گشت ارشاد رو دیدم احساس امنیت کردم.
امیدوارم این کار ادامه‌دار باشه چون اصلا از وضعیت سطح شهر راضی نیستیم.
چهره شهر اصلا عوض و زشت شده.
الان همه فکر میکنن رشت این شکلیه ولی خوب‌هاش رو نمی‌بینن.
گشت‌ارشاد دغدغه اکثر مادرهاست نه فقط چادری‌ها!
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/69583" target="_blank">📅 19:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69582">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
منابع عربی از حمله موشکی سپاه به بحرین خبر میدهند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69582" target="_blank">📅 19:24 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69581">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d659457195.mp4?token=vvMRxHR5Yh0q69UVeua6_IGDpXVoFm0-zqNpUd6OtZw-7uLFDcZboPE_39jeBEYfX2KyYSDtUwFbsjzxsDbjzhOFj63QxYQBqXb13qMaM6Y80rNcD5v5AkP1ajRKifqXp_b1I3Ge8Tl6APsBmq7viskOcNdNSMEQ7YGnUO0fKo-CT4MOWFJYdgvuWkxGx9mWi8BpAAbefwstPi3JarkBIEzyCSsXM_1bn8EriXM5lckaNTdV2KhG5MT-QCKUkK5liJ9SMgwPaxnRKclS8XCslV7xaT_oT4IEH0iwBSz5qt_NCYvuIRHwW70yLRFbyb5RHfmz_YJGpmhivudsb1gdWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d659457195.mp4?token=vvMRxHR5Yh0q69UVeua6_IGDpXVoFm0-zqNpUd6OtZw-7uLFDcZboPE_39jeBEYfX2KyYSDtUwFbsjzxsDbjzhOFj63QxYQBqXb13qMaM6Y80rNcD5v5AkP1ajRKifqXp_b1I3Ge8Tl6APsBmq7viskOcNdNSMEQ7YGnUO0fKo-CT4MOWFJYdgvuWkxGx9mWi8BpAAbefwstPi3JarkBIEzyCSsXM_1bn8EriXM5lckaNTdV2KhG5MT-QCKUkK5liJ9SMgwPaxnRKclS8XCslV7xaT_oT4IEH0iwBSz5qt_NCYvuIRHwW70yLRFbyb5RHfmz_YJGpmhivudsb1gdWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مصاحبه تاریخی فیلدمارشال رضایی و خنده مجری:
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69581" target="_blank">📅 18:55 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69580">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tky4zdmcB9VE41RQnjhJ6if7DzftinFqm_thjZMi7skQPtLA1Z3EDd6oRel9xfwlbjUUPBSF6lHykH3VGZkPLmtHLOd3rnreTsVTK_rFuK-S7xNiKQHsfqEvfJ-vZ1l6HEDblr9n1q1Da3uCkdqH4Uiw__KpvpkaETpMcoq7FXUEejds9Mx5-kqR4vqlJUTrWPtw8DGhgJNnPXA8uX2sHTcUm2X1nW39RZpoi71BsSR456VNeNU9UZFjtDYHryGxxCe37Dvt30l1nYKMzlPEbZfZaB2M8TnoljBoLBs-J6K3ZZfvbTpPh2h8UR9qlGKTc_W5Ad11mG4A-8v1iJYBsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پهپاد مافوق‌صوت Quarterhorse آمریکا به مرحله آزمایش نظامی نزدیک می‌شود
واحد نوآوری دفاعی آمریکا (DIU) برنامه توسعه پهپاد Quarterhorse شرکت Hermeus را برای ورود به کاربردهای نظامی دنبال می‌کند. این هواگرد بدون سرنشین با هدف آزمایش فناوری‌های پرواز مافوق‌صوت، سرعت بالا و قابلیت استفاده مجدد طراحی شده است.
مشخصات اولیه Quarterhorse:
⬇️
نوع: پهپاد آزمایشی مافوق‌صوت
⬇️
سازنده: Hermeus
⬇️
طول: حدود ۱۲ متر
⬇️
پیشرانه: موتور جت توربینی با فناوری توسعه‌یافته برای سرعت‌های بالا
⬇️
سرعت نهایی Quarterhorse: تا محدوده مافوق‌صوت بالا (هدف نهایی برنامه Hermeus رسیدن به سرعت‌های نزدیک ۵ماخ است)
⬇️
قابلیت‌ها: پرواز خودکار، استفاده مجدد، آزمایش فناوری‌های پرسرعت
⬇️
کاربردهای احتمالی: شناسایی دوربرد، آزمایش سامانه‌های آینده و مأموریت‌های نفوذ در محیط‌های دارای پدافند پیشرفته
پهپاد Quarterhorse هنوز یک پهپاد رزمی عملیاتی نیست، اما آمریکا آن را به‌عنوان یک سکوی آزمایشی برای توسعه نسل آینده هواگردهای بدون سرنشین سریع و کم‌هزینه دنبال می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69580" target="_blank">📅 18:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69579">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3689824738.mp4?token=ljTaYCX2qiRYAkBpqgAKfiQHwdqYAwUyFysrDHWPtbaBcZIHUi6labNPJsZdCv0I6VcVxPnJJ-WxYTcOTxtCm-iRYzUZ1bj_NGkz1mcXu__zO-hzE6R1lHoX30sDGfr2Mr36t3SvZTT9jAzscMnLvc-FyKnqPat5aZKCR86ueQezoNeVod9Ep6beO-YlnQBSQbaCDKRzSCs9kcphDQ4CJVuM3U5_kQi6-Qsn5zRGKVUxFUy10vuVSU39t6xWIaxoIb3SV7Zb8bJpU5R1b9nSA-oNMIh6gDTX0NwFhV9iyDos7MH-clXE06QkyKDDczUmEEdZK_9-5xu79y3j7Jno9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
یه سرباز روسی توی دونتسک اوکراین لخت خوابیده بود و داشت افتاب میگرفت که يهو…
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69579" target="_blank">📅 17:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69578">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=s079xAAfU0KQMo56ZFKzM6MHw53R7nz3PO0xb5aY5tIb0pYlcZ9ZtTa3-_NHrhxqIAzxIhfvV6vj6yTsqXzXHlEwuVP1dnFjHHdHsDYwjF_4esUcGS1QjL1kjWKFFuoJGnaCHTL3eJ1yxkNxFkVWdwmkNHWfwZ-EPFz0W04k3QE4QDLM_tq3U8wgJhiTJvAP5K7qunfdjvIW26USBoTrVEoky9XKrn-q3hKLeDHUh96sD0Z9IVBloA0PEZHJBevl-8M0kSw5fBL7m8jpJEncPBELjI-_2JHD5SbrS7ceHR8Wyf5J6Fu0cfLnwiDDMLYUjtfYKnKetyD2-Phgzzm-Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fdacb808d.mp4?token=s079xAAfU0KQMo56ZFKzM6MHw53R7nz3PO0xb5aY5tIb0pYlcZ9ZtTa3-_NHrhxqIAzxIhfvV6vj6yTsqXzXHlEwuVP1dnFjHHdHsDYwjF_4esUcGS1QjL1kjWKFFuoJGnaCHTL3eJ1yxkNxFkVWdwmkNHWfwZ-EPFz0W04k3QE4QDLM_tq3U8wgJhiTJvAP5K7qunfdjvIW26USBoTrVEoky9XKrn-q3hKLeDHUh96sD0Z9IVBloA0PEZHJBevl-8M0kSw5fBL7m8jpJEncPBELjI-_2JHD5SbrS7ceHR8Wyf5J6Fu0cfLnwiDDMLYUjtfYKnKetyD2-Phgzzm-Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
توی مراسمات اربعین امسال آهوی ایرانی کباب کردن و به زائرین دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69578" target="_blank">📅 16:58 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69577">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llNH47FKQtmZCiluZWRDb4g0JmamJb6fUxJnV7bfDnE-guffPGC3KfRAHfait5wulMofMVOK8Cq2pxqWTPDga846HyJNvN0iz9M6QQZmsrfQ8W9fOgOITydx_jdFgnBX5YAeel_aZkeJjqi8Op7XW8P_6YULyBLAJMPG2jw7nB6_bbiAk4Db9wentcItbBZlcBIP72aHo_nxomiRT_0yVynRwyaBmmGvfDonaAafjikv7rHyHd3iZjxfeT54TsiPdlWljPjyOQ9CFPN8Yl1i83a_L1FXKZwqDYhu-nmyatSTYOmTmk7uC91qvgBPuxEWeidTVUAKiWpgDCIhdb0OCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛ ارتش اسرائیل برای شهرک المنصوری در جنوب لبنان هشدار تخلیه صادر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69577" target="_blank">📅 16:34 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69576">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66218d020e.mp4?token=vaxHmstkgO7QzcDxPcaRRTo1XvW2xFGoIr2cRjeV5MY1HsLfAZE43Hk-yMJAic9rW4jkd5C--kev-JuVlMqXt6if75hhr9AgmEOkiJ4WjsmwRA2DzWjGgGDcKOdVoWEz5Vkj46Tg0kb8_hXK7iCsTbPOGGbykr6UFBF9LwrSNuzgj2gjpsuLMLf-iy8bI7nuetH1lfz4ZmIx_oJYQ1dgW2-4t7fARYFAktn2DjtMC0XrLuLf3C1N5xxm-lhlKjYyvjLwUSgGhrxLzwA9YDIjM7VXinmJFyLOALpQexJkBDBFfVO-5NAUbmnRVQgCsi61JJsO21dtYqAhdWAYJj6K1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66218d020e.mp4?token=vaxHmstkgO7QzcDxPcaRRTo1XvW2xFGoIr2cRjeV5MY1HsLfAZE43Hk-yMJAic9rW4jkd5C--kev-JuVlMqXt6if75hhr9AgmEOkiJ4WjsmwRA2DzWjGgGDcKOdVoWEz5Vkj46Tg0kb8_hXK7iCsTbPOGGbykr6UFBF9LwrSNuzgj2gjpsuLMLf-iy8bI7nuetH1lfz4ZmIx_oJYQ1dgW2-4t7fARYFAktn2DjtMC0XrLuLf3C1N5xxm-lhlKjYyvjLwUSgGhrxLzwA9YDIjM7VXinmJFyLOALpQexJkBDBFfVO-5NAUbmnRVQgCsi61JJsO21dtYqAhdWAYJj6K1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
🇺🇦
وزارت دفاع روسیه تصاویری از حملات پهپادهای جت‌سوار گران-۴ به سه کشتی باربری در دریای سیاه غربی منتشر کرد.
وزارت دفاع روسیه ادعا می‌کند که این کشتی‌ها تجهیزات مقصد ارتش اوکراین را حمل می‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69576" target="_blank">📅 16:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69575">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/474cba356d.mp4?token=NvfBva6X29TmoR_rGk8rjzADPp6jgk3zAXbiiLZKjUiNwYHvBr1fvTzn02ag2-x9o1dKyXqsv_KCmnBui2ekFRqXNwgAa8HRUHciVIcXbcs1MQgpb1N0tcQn2aONdrAanB73Lcv6e4U5U-WrCjFqhXOPW6Fl5d0HbQxpQ9HeKSU3ucCw-2emFJFXOF-9zCBQIDSEQZSaXGxW-ctxvAGzCGYR56Jl5_Qo86uuIQhZVCWLEi6hE9B66GI949N-CvFYK3Re141pHZzI3wqGKKTj7AYl-7jzZ_tUR_2tq-H7qJeJTrNlG1s8aEnY5My4jsoYVk20kd2yUZSE_hONvW9Y_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/474cba356d.mp4?token=NvfBva6X29TmoR_rGk8rjzADPp6jgk3zAXbiiLZKjUiNwYHvBr1fvTzn02ag2-x9o1dKyXqsv_KCmnBui2ekFRqXNwgAa8HRUHciVIcXbcs1MQgpb1N0tcQn2aONdrAanB73Lcv6e4U5U-WrCjFqhXOPW6Fl5d0HbQxpQ9HeKSU3ucCw-2emFJFXOF-9zCBQIDSEQZSaXGxW-ctxvAGzCGYR56Jl5_Qo86uuIQhZVCWLEi6hE9B66GI949N-CvFYK3Re141pHZzI3wqGKKTj7AYl-7jzZ_tUR_2tq-H7qJeJTrNlG1s8aEnY5My4jsoYVk20kd2yUZSE_hONvW9Y_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی صداوسیما خبر کشته شدن ترامپ رو تمرین کردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69575" target="_blank">📅 16:03 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69574">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WNjWoXlj792yiY_FN7rJp7uncrCGQSZuVFFjJ2PE3oGCX23LwT4XibuhG-wZ5nT_AsTBsNP0XA1syhdNv5IkRmEEogvGIX8qkEvCxRTVUMEcqQwqPjNFfX9aclZmFtAUNr_h_6BIA3wJxAx_SVGEGnNStboZOCaBTRYGiQZ5tJqF1abqUYo7INl9xPVStCi80fB3mqPsJabwpWIx9llI_1jgp-gC3-r0VVA74nR0oYOHuq2KXuoCiuFjLcXwcfoBqBVcLJ1fvHWZYVAjVbpBJARHr7LYdw-PJid5ZZvTTbZJwHhYFC3CdInMHn0hJJTFTVrXNFNSfWw5wKILikweog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
💢
📉
قیمت نفت با کاهش های پی در پی به ۷۶ دلار رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69574" target="_blank">📅 15:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69571">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fTNXIQdiS6UXlwt2a68455aVSS5SOKjGVzJasqCT_xb-LZGrFWqSGmyplDEhgXEvJgqrJACJ1nWngHjFSsYnM8byoBJTnYqdd9QaqjP_h-e2dROYeusDgXI82-EQaIJF7z6FeGLtx4j0RDP5dFIh0ui1BO0mZizJSio-xhw3ilBWMuARsTjAPm85WusJwWXeqhF-lUjyNSI2chGbWnYUxAITLfQHk1LhIQDjXkfFoD13TKox-NRcvfCADZsgbvp4ZfCW81XdXtmMndLtOUSjYu48QpcmVdoyJLpBJf7_o9iUy4Ltg6iBLitRmkzZoEo_TgibleIJhorgyWvrN0sprA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nQLTqC-ZTXv15hOAmSRZicGy6yK4Kz6JYWGh9StPogdMJ3-4ctlP2h2-GWE-MSt4wH51x0qcHXNznMkg46kf9rEw6u3S-1Ucx-_eU5s4jurh8vJ2DHOXGL8eUWjbDFxfN_gs3pWfMWvpAKiAjfx7XeRkOdCbBMHFRyR2MIXWRvLmBwzcu4rTniKIuEu6onfe_PyuJh3m9Ft6cZW1pfIv2RMwf9gRsNX7dXmHdD48sMJfOLQhRIT01wbGgqDyICYiQkgl8W94IzW-VL0ckeUfdFqL1e6xntV5bSWPoUxZKaCAWGrpLZ5kCy_cfEJ3tv4xlYb0CgoFMUpWokqIIAbYAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mpfXcNTccW0nulmn58j5k8s41A2p702iwmYmpgYZcpwF6pSxZ-2sDht3bXLf-Z2iqPVAJiwO2EfurCtofEVW38QY6m1zgPBm5a8VL_mofHxjx32Ajx1JwC7W3INtV39a8aFov3IH-rkEPe0gj6kDy_fhjYBvvZoGZDf5U1vdxJ99CVbGI6WLndCijxyeBrgO6hVqFr3sj9YKlomdJgizN94lCxwWwrbCdrnU3XwZJYeFENNu45LL5p8iwHwzMWshhFGqmPuv7EMUXg9n-plbkIRajL71dQW7etkhsKpRaCY2YTA-RvGY0m4G_58adV60FcttrqpDqFG7glFwRVf1sQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
پست جدید و لاتی کریس رونالدو؛
"
اسباب بازی‌هام
"
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/69571" target="_blank">📅 14:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69570">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usO1AtLrZBbYqTo0eK7W9ERd0YC0LZApOodF3wn1Bou8pJZ0L3sKyEIInLVRlLzQ_JsmQ_Cu_VdVoHkB19OAgW6BJvffClCM_cCF5l4Xn9gs6Xx9qsKq2-OacT0MK0yqctJA3du938tujUWvUbt5bNcGnHl_oZe6mr5j0akCaBAqc-Mx-Mj5ZOzPI3R09le9KRb6xN5Ei9uV_ellBaRVS2fh6b2Ojz958Yijui-dqg4YZrzpZVhh_1D40aQgvzUsus7HLH-obFUIpGJtDZbrJ7y_7YMeh6wFQxK6ShfWWuUkjX9VumZvB9V30G6Ace7CNo0h3ZgBjttCyzVvZH14hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دسته‌ جدیدی از سوخت رسان ها برای مذاکره وارد اسرائیل شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69570" target="_blank">📅 14:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69569">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k11SCFvSykdMGOsbFL8JPuzp3Ek9b7-sayEJq-YgxamXC0OrV9e3VYlqoPww5cF1k0PmbBZAQ-VS6n7BaYymgES8jE3bxAKGXGUfbbJQYxEjBNP17GJk2ijx_51hQ4E3-HKYJPxmYIP_KoZktbF3diZSn2Hjo7duSsONZ-TFiYlpYKlID_TbD9xzXQNpsiqUKKaIjPnlL0NvVv1MdN-ee7mAzLMhf2N91QsYfM3wVFAotBj1v7-9fQS35Yi3Za0Pbj7BaQePkEV6W-J4XWt_PUOUQIWzn1_vvLxs-6QqcxRK6xsu2R77Q2f_xG_0vzn4oKBwFXUokLEENWTWvp5k9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
❌
حمله هوایی ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69569" target="_blank">📅 13:44 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69568">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=OfSOX9eIWy5VtzhLnabZcjyYeeWX4CQhsAXeNNR6m05gzZWqqvy3VbqRw0PWWBZkO6hESZAHFpu-8jS2KcMNHKrcCN_dPTE6smQydOBpnaNXY_kL4Caz2FU8hm2OlrHdVKDztXEFq07uFcp0Xe8V5n7ICqeV3scT8R-dyVF0DpUUNKE9Ena2cYpvcR09aXciWtPf8HRaMikIgN1c88Sn6Pf2tSZRzTLoxBrCGThGQOZ_PpbHbfgfWn7Xejvu0PqmqPYJ_J5GSTmjpnIMAF0mWjrJ5AY2y_G9NcITVt_43ilOWEd2w2was1ZNp8HPBNmOnOeBuUQHoDfgBrb2vv65yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f4b05f8c.mp4?token=OfSOX9eIWy5VtzhLnabZcjyYeeWX4CQhsAXeNNR6m05gzZWqqvy3VbqRw0PWWBZkO6hESZAHFpu-8jS2KcMNHKrcCN_dPTE6smQydOBpnaNXY_kL4Caz2FU8hm2OlrHdVKDztXEFq07uFcp0Xe8V5n7ICqeV3scT8R-dyVF0DpUUNKE9Ena2cYpvcR09aXciWtPf8HRaMikIgN1c88Sn6Pf2tSZRzTLoxBrCGThGQOZ_PpbHbfgfWn7Xejvu0PqmqPYJ_J5GSTmjpnIMAF0mWjrJ5AY2y_G9NcITVt_43ilOWEd2w2was1ZNp8HPBNmOnOeBuUQHoDfgBrb2vv65yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇷🇺
دیروز طی یه مراسم تو روسیه، یه چترباز از هواپیما پرید پایین ولی چترش باز نشد و سقوط کرد و درجا مُرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69568" target="_blank">📅 13:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69567">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VwbpzubukIbkytCC72wnSeYQvzdMBKZi1jGB6cCLHOMZnEkd9cvXDwIb8lw5zmLTot0bA4QFvZHfA5Xg1gxwUuzc-TtPlgAEal8v7KZESur80El4ccotCcw6FtYBRZqjMKBs6wOifD6w4sZGBlO0esXS_eKz8C1t3XFSVhmsK3FCgoRltnjwZE-1XIWRkzPMfO4LIWArXdOIuILkH3CB1jmPqD1l59WVl0shPkkAwwmDTgQO0opz5ZwDRzJ0Kp4QUd0NgMdOlO2cTYc2WRMhYUPU6qnYFlW65-wkK0LMKUSsGaKMwDwGCINnM5cnCP_QjCJtokdaxlSRGLgpF-ysqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
دونالد ترامپ تصویری با هوش مصنوعی از خود منتشر کرد که در آن با لباس نظامی در کنار ژنرال پتن و ژنرال مک‌آرتور دیده می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69567" target="_blank">📅 13:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69566">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=nHVb5M7nbhFeIPID-q48JjhKFwIIMHnGtQanWLLoB1l080y6hWxioGFgh7F9H3Dm-fe0PIR0WMz5uX3M3Q7LPYlH6ETl6ULtEVrKWM_7N7_AS5vbPBD8IRQmX0ImFA8jFAk91aXRWAEtDyl2m4PMo7Y5qpLFV_AB8OmKEB7s4CpphY1iFcYzqb4v_y7UnMuIBnl6MSKz5J6ejBKlWUK0v0Vfqs9CdqcXrVFZNAYg5M8x6GJ4lzWrThVaq5NnQKAloKvW8WMZiCv8ycUeTimTdPGyXbu7wVUogB0SqYS2VXWAtaQk6HI6Bt13Tc_mfYQHRw6kn0I9y2w8XriQds0STw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cc20a5985.mp4?token=nHVb5M7nbhFeIPID-q48JjhKFwIIMHnGtQanWLLoB1l080y6hWxioGFgh7F9H3Dm-fe0PIR0WMz5uX3M3Q7LPYlH6ETl6ULtEVrKWM_7N7_AS5vbPBD8IRQmX0ImFA8jFAk91aXRWAEtDyl2m4PMo7Y5qpLFV_AB8OmKEB7s4CpphY1iFcYzqb4v_y7UnMuIBnl6MSKz5J6ejBKlWUK0v0Vfqs9CdqcXrVFZNAYg5M8x6GJ4lzWrThVaq5NnQKAloKvW8WMZiCv8ycUeTimTdPGyXbu7wVUogB0SqYS2VXWAtaQk6HI6Bt13Tc_mfYQHRw6kn0I9y2w8XriQds0STw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
املاکی درباره ایران:
خب، اگر دوباره پا پس بکشند، ضربه بسیار سختی خواهند خورد. آن‌ها این را می‌دانند؛ آن‌ها این موضوع را درک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69566" target="_blank">📅 12:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69565">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=h5NX-Sek2otlLl8xKDUAqJAFt_9DAun6-lA0HBxexxFF6Oo61Vhiz53mrdJlfuwrjM_QdLyT6cHWCBhccgAR9dG1wVaJ1fWyIMGtMgvEEwU1i8fw9dpIFbR7eZHlOiCoP204ppHZH4lFb07X7TUVpNjLgAgkzeherUJ_fvZ7dIVLlNZPXY5axCT5RTPN7RmWHZ1OiQ-xJ2hVQrFJR9sAwrU_yPa2Ys_WF0xikTEKgjl5ki52Csc-vJnQXf0NaKSqbPYq8GJaAEQjHLXy0Z3Zbe4i15-7MPObCP7u9wpeeJlA6UA4O5OTcCkv8W4Ywk70Prq27scRvP5q4cwTvDOysw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/336dcdad36.mp4?token=h5NX-Sek2otlLl8xKDUAqJAFt_9DAun6-lA0HBxexxFF6Oo61Vhiz53mrdJlfuwrjM_QdLyT6cHWCBhccgAR9dG1wVaJ1fWyIMGtMgvEEwU1i8fw9dpIFbR7eZHlOiCoP204ppHZH4lFb07X7TUVpNjLgAgkzeherUJ_fvZ7dIVLlNZPXY5axCT5RTPN7RmWHZ1OiQ-xJ2hVQrFJR9sAwrU_yPa2Ys_WF0xikTEKgjl5ki52Csc-vJnQXf0NaKSqbPYq8GJaAEQjHLXy0Z3Zbe4i15-7MPObCP7u9wpeeJlA6UA4O5OTcCkv8W4Ywk70Prq27scRvP5q4cwTvDOysw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فریادهای مجری کشمیری(هند)صداوسیما درباره تنگه هرمز:
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69565" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69564">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">melbet.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/69564" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇩🇪
آپ اندروید سایت جهانی Melbet
💥
🎁
بونوس ورزشی هر چهارشنبه
🔥
💸
واریز و برداشت متنوع
💵
⭕️
بدون نیاز به فیلتر شکن
⭕️
R14
🎁
کد هدیه ثبت نام Melbet90
✌️
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69564" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69563">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ae1rK-72W4Wst1V305O2IAeqiSSbXs69kd10huoaBGTzi-6OxNpAV4zu5stmzIjM7Bj4bpL22oU7V3aBsxUmyTrKZfp7gDht-O-EZzGi6RzT5MC_O5i_LoWmRVU8JMSGrj8zYdCij2LNWg5CbnpqGFpiiif530kUhcy188B_IwLh8bLfwS12Zh4WFQfYTZYX_BcBkfmf_yx490QhpbPXzORXCAbfwhI9HzBpJOif7KMYVUZ584C3yzZJVZRSa8qgASMovK-bJYMxo8w6cWzgTXniwjbdFc6qvCtCb8ZOeLlmoeW4jO-MeX5eY-lGl9fnKp8pUbNdIQMXBqPjTCSejw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
دنبال سایت معتبر برای شرطبندی می‌گردید
⁉️
🎲
سایت بین المللی و معتبر Melbet
👍
😁
😊
🙂
🥇
واریز و برداشت ارزی و ریالی
‼️
🔥
بونوس 100% اولین واریز
‼️
⚽️
بونوس ورزشی هرچهارشنبه
‼️
🆗
کازینو و انفجار با ضرایب جهانی
‼️
🎁
کد هدیه ثبت نام :Melbet90
🇩🇪
دانلود اپلیکیشن MELBET
👉
🔗
لینک وبسایت
👉
⭕️
جهت استفاده از vpn از IP های آسیایی یا کانادا استفاده کنید.
🇨🇦
🇹🇷
r14
✔
https://t.me/+x60dZGAgXTUxM2U0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69563" target="_blank">📅 12:19 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69562">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=LpI5X8OOMvQo3Jec6ggnO1eQdtLdhX7-36tvDal1iN-RxeFPjRRWBUb68rm3IZGcsaEhjBQ0owcwKe-dIma8Im5uyt1s1yqjh-4SYfN9Zmrz1e1rDbndNh8Fk_Hz_Fq_SLinup9io7gQB2_9Qp8cj_vywh9EbdKBHJMovLx1lieA02nfUZiDxK4eHxGnjqW1z8OaiCKRaR1hJenWZJuWJn3N8iC_JrCGBZjvPPbFPr-4JwaBSon-dD2aMY_d3IL6SmxYnFwfupEbCJegBRN8hAj34M-GU7PzeI93S0izCaUk522BkZ87N38zkHelCTz8pQZj_8XzZ7R-Rl2x_jFyLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aba5ea669d.mp4?token=LpI5X8OOMvQo3Jec6ggnO1eQdtLdhX7-36tvDal1iN-RxeFPjRRWBUb68rm3IZGcsaEhjBQ0owcwKe-dIma8Im5uyt1s1yqjh-4SYfN9Zmrz1e1rDbndNh8Fk_Hz_Fq_SLinup9io7gQB2_9Qp8cj_vywh9EbdKBHJMovLx1lieA02nfUZiDxK4eHxGnjqW1z8OaiCKRaR1hJenWZJuWJn3N8iC_JrCGBZjvPPbFPr-4JwaBSon-dD2aMY_d3IL6SmxYnFwfupEbCJegBRN8hAj34M-GU7PzeI93S0izCaUk522BkZ87N38zkHelCTz8pQZj_8XzZ7R-Rl2x_jFyLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محسن رضایی :
به عنوان یک سرباز از‌ همه ایرانیا تقاضا میکنم یکمی دیگه این شرایط رو تحمل کنن. چون ما داریم در کنار آمریکا؛ چین و روسیه به قدرت چهارم جهان تبدیل میشیم. این شرایط گذراست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69562" target="_blank">📅 11:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69561">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=l5S2braSJ8-BrfVrjjDWkGGPQpg5IwKlS51JHPZgQbJdyimQROL4r34pPrm-CVDqoQqtLLttu5soIct1q4_TtZPBJY-W21fvLeAeTYy8b5n4uomo9igqmZtLgcrMSIc_MocdwFVmzU6LXS3s0tz1ZT4370t1Nr1Wr37a_XldyHLF7oP6bOim6fxpSh6hJt7cuRHfUnKZIgRmccLv89oH_I4rR4tToDL3YxzUGtASBwWmGM2ENP7i7ENUxVk2EapykSHSJXqk4-2LaPmpo6un4eX3DyCenBKMRuoaoDWGe8IUDd6gk2SvQd2qwwHJBa2leiwewI7pLInMYYU-H1KQyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1729d69d0e.mp4?token=l5S2braSJ8-BrfVrjjDWkGGPQpg5IwKlS51JHPZgQbJdyimQROL4r34pPrm-CVDqoQqtLLttu5soIct1q4_TtZPBJY-W21fvLeAeTYy8b5n4uomo9igqmZtLgcrMSIc_MocdwFVmzU6LXS3s0tz1ZT4370t1Nr1Wr37a_XldyHLF7oP6bOim6fxpSh6hJt7cuRHfUnKZIgRmccLv89oH_I4rR4tToDL3YxzUGtASBwWmGM2ENP7i7ENUxVk2EapykSHSJXqk4-2LaPmpo6un4eX3DyCenBKMRuoaoDWGe8IUDd6gk2SvQd2qwwHJBa2leiwewI7pLInMYYU-H1KQyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکیه دلقک:
تا ۴۸ ساعت آینده خواهیم دید چه میشود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69561" target="_blank">📅 11:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d5b_dG88M4BdnfndD2OC1hlWOpoSU_ejVrXUNImvViQyX_CQNuLYotD8UmYDOMmz2N0EyNfgIMPaiRAhquAqLsFl8UQtJ4ubyiiTTXd2V2luBJOizNeIcnCE7Tm6uiPzE3wo-RmCsqdNxlrfRlAdm1bX0EGagkuIYNcYZqydhEOl-TTn9qSXJySWMtpDrkM7QIYMwvZAyQyZsSDsn_YbOrkrEUzGnBqLeK26JOwYocZ9bqviLQUAxDaavJUHQtlGlC9oy4ll4Rv4_bfmAl07wrVMn_Y1rvY44T3ei3ABTvjY8vtwifXbvjj6579D6Ao-iK7-rFvNK1UQsICZMKw1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=CF8HcPLUaFNxUo7HxFaHyJeR2ePPJ0OU5djXxBoQaLC_ah60IgitKeN42KmITUI4ecRg7OYun--tdTV4dAvLHVP9m_mEl3kzuhPzdsQMQjegBBsqry87h-49M5GZ8VxiV0Q_oc7HQWlQIxT-JUMt3Hydg2fClCXpMhbR6zvTo3NdPV43mkWw37Q9el0PUhCnvIwOmtU48tlIrOLmAJT7qYTCG6oyOG-gHcUY_hh8Y9du39reN6fhfNgQkQASg2NVtnIdjWCVVRdhSkP5tGmhkQ-UaKgHNZqqF8OgVDKuq5BziSLTXTMxR-Th0Y1PSq_Xnt84eKkRqMnF8UznCXmCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2fe475d0b.mp4?token=CF8HcPLUaFNxUo7HxFaHyJeR2ePPJ0OU5djXxBoQaLC_ah60IgitKeN42KmITUI4ecRg7OYun--tdTV4dAvLHVP9m_mEl3kzuhPzdsQMQjegBBsqry87h-49M5GZ8VxiV0Q_oc7HQWlQIxT-JUMt3Hydg2fClCXpMhbR6zvTo3NdPV43mkWw37Q9el0PUhCnvIwOmtU48tlIrOLmAJT7qYTCG6oyOG-gHcUY_hh8Y9du39reN6fhfNgQkQASg2NVtnIdjWCVVRdhSkP5tGmhkQ-UaKgHNZqqF8OgVDKuq5BziSLTXTMxR-Th0Y1PSq_Xnt84eKkRqMnF8UznCXmCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
🇮🇷
جمهوری اسلامی دریای خزر رو فروخت رفت!
در تازه‌ترین قرارداد، جمهوری اسلامی دریای خزر رو تقدیم روسیه کرده و یواشکی دارن میبرن مجلس و تصویبش کنن.
سهم ایران فقط به ۱۱ درصد رسیده! شما ایران رو فروختین و شرمتون میاد بیاین به مردم بگین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69559" target="_blank">📅 10:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=oaBJvUme1Vy2vS2qW1RGQZkWyqKoQminHMmfI41g5vuvfo6rWrbZUqXnIuQKRmyApX0zA9ipwW_UCf3z-ztuVipMeeUlzV_2p_YNuWmNPycR3AX3eNfAIrjm1_4Qq8a9RhUc04bMLdPZhQZN8UBxCzs8kwgDWBEv_Q2mgJilWVS6zmjwzBhPMnY1CmPXUlkBhDKtpxKC8Y8lkYo9B1hV2eHNuKa2HrpR98rULmEZthU61UBbG6clb9Zs5FXUvi7F_kHEueeHxbe1ji91-6Kknk44Qo8HPkSCZ3zjtSQx5dzBM0I9iawtTfXkrBNwRlJ5qMw57lhrB7Jjf8EmlwEZxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb6f67c295.mp4?token=oaBJvUme1Vy2vS2qW1RGQZkWyqKoQminHMmfI41g5vuvfo6rWrbZUqXnIuQKRmyApX0zA9ipwW_UCf3z-ztuVipMeeUlzV_2p_YNuWmNPycR3AX3eNfAIrjm1_4Qq8a9RhUc04bMLdPZhQZN8UBxCzs8kwgDWBEv_Q2mgJilWVS6zmjwzBhPMnY1CmPXUlkBhDKtpxKC8Y8lkYo9B1hV2eHNuKa2HrpR98rULmEZthU61UBbG6clb9Zs5FXUvi7F_kHEueeHxbe1ji91-6Kknk44Qo8HPkSCZ3zjtSQx5dzBM0I9iawtTfXkrBNwRlJ5qMw57lhrB7Jjf8EmlwEZxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
پرزیدنت سابق، جورج بوشِ پسر:
مذاکره با قاتلان، گزینه نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/69558" target="_blank">📅 10:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ER4mrATJe5XS6ftFiEZEBsGo02b1_wqlir6MEPuRMd_kK4FQXjmOZ3wtAQYTLJXcVhu-DGYqYItU7Njsf_rrc5YmylrYcdv2VDTOtX_8M2r-e2oapfByrXjf1lALHB2wtYBZc1n4LwVlzDfE1WA89MDUgll5VVjppXGHHB5i0CVKeAe8YtoC9xof42Z0ukJy6dfzFIt5cwklqZkD1fnNGMAEWIhCjB2A6HSVKkDkJ7H-oAzXjpcSf07oKKtX645qUBw8mP3nHL7tMhkrqTPFoLSPcslU6R_SClL8TuLB1WTdoEI2YLSB_S1y4fv_tr3UBQleH-EdVrp74tF7a5iRug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇴🇲
🔝
بر اساس گزارش آکسیوس، آمریکا، ایران و عمان به توافقی موقت ۶۰ روزه برای بازگشایی تنگه هرمز نزدیک شده‌اند و احتمال دارد این توافق روز چهارشنبه از سوی آمریکا اعلام شود.
🔴
مفاد اصلی توافق:
- کشتی‌های ورودی از مسیر شمالی در آب‌های ایران تردد می‌کنند.
- کشتی‌های خروجی از مسیر جنوبی در آب‌های عمان و با هماهنگی ایران عبور خواهند کرد.
- برای عبور کشتی‌ها هیچ عوارض یا هزینه‌ای دریافت نخواهد شد.
- مین‌های دریایی در مسیر مرکزی ظرف ۳۰ روز پاکسازی می‌شوند و سپس این مسیر برای تردد دوطرفه باز خواهد شد.
- پس از این دوره، عمان و ایران درباره یک توافق دائمی مذاکره خواهند کرد.
همچنین قطر، پاکستان و عربستان سعودی در میانجی‌گری نقش داشته‌اند و کاخ سفید نیز مستقیماً در مذاکرات مشارکت کرده است.
طبق این گزارش، عباس عراقچی با این توافق به‌صورت اصولی موافقت کرده بود، اما تأیید نهایی باید از سوی رهبری جمهوری اسلامی و شورای عالی امنیت ملی انجام می‌شد. یک مقام آمریکایی و یک منبع منطقه‌ای نیز مدعی شده‌اند که این تأیید روز سه‌شنبه نهایی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69557" target="_blank">📅 09:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6oF9L-iGuKcCA6zsoJ7Pun2n7R2Lx_L-wseAXxnZlVg0fZ-OIlRognUX5lnygwBIFoYlHSiA72F3Ryzrp8MXBidbADF69A8ta24j6MJ3epHyonecjBjfWNIiwqia0Ki8gSeRAIlkpaYhDLlwKWpy1-rHfCPMBO6KZr0UcZGCx9XZ8_fJF1nbHiIyeB6CDWlI2kELkIwegpIxjgXA7zomoGYVmhgkvPoAUim6uNgySHWs9HflIZpCfYicF1iY0zkjKy9QD4PVZBJ69sulEI9k91UkW8FjX4rrfeM4Hxa6b1dGmaUEbbrMEs3Uj1qxOAcy3oTbGSNRpphUL1VBMZX5c0I" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5c55d9f368.mp4?token=J6EJGpXiaiS1Put3zbsiILRdkt7Uz1_M9EavW5ELJ8YMPXeNeRj05tItvTiK1icevCKr7h3TjwA8rg-1AKE-tE4B3j4SNa7UAOfD_CugRet_BacKkF34_OWdqSjZzqWcqXPPXiqsuDxsfXYCMqPkr5xluDg409SmTr5Ju7W1NYmryBHbCi6Yxc_gK0Q1MQiNMochJhwMFiCyv07S2m8wN2Rgg8rje5UrKsRj3bd_LfY-afT3o9OAl39Y4iLeguO12RtuyJHCNVAqN0lecF9ugCY9KgDTCbkqw4I06U8wBqQStLxHNQPt9EX4Ua--LA7uPMZ9qXtG7FVZc9EGdSkc6oF9L-iGuKcCA6zsoJ7Pun2n7R2Lx_L-wseAXxnZlVg0fZ-OIlRognUX5lnygwBIFoYlHSiA72F3Ryzrp8MXBidbADF69A8ta24j6MJ3epHyonecjBjfWNIiwqia0Ki8gSeRAIlkpaYhDLlwKWpy1-rHfCPMBO6KZr0UcZGCx9XZ8_fJF1nbHiIyeB6CDWlI2kELkIwegpIxjgXA7zomoGYVmhgkvPoAUim6uNgySHWs9HflIZpCfYicF1iY0zkjKy9QD4PVZBJ69sulEI9k91UkW8FjX4rrfeM4Hxa6b1dGmaUEbbrMEs3Uj1qxOAcy3oTbGSNRpphUL1VBMZX5c0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
تنگه به زودی باز میشه یا ضربه شدیدی بهشون وارد میشه ک باز کنن
اونا با من مودبانه تماس گرفتن گفتن میتونیم صحبت بکنیم؟
ضربه سخت ایران تو راهه ولی قدری دردناکه نمیخام ازش استفاده بکنم
خیلی بحث هایی خوبی داریم ولی اونا نمیخان اعتراف کنن چون یکم نگرانن
شما میگین مذاکرات فوق العاده داریم ولی اونا میگن دروغ میگین
اونا میخان معامله بکنن و بشدت خواهان توافق هستن
در عرض ۴۸ ساعت خواهیم دید چه خواهد شد
قیمت نفت و گاز دیوونه وار میاد پایین چون سه شنبه مذاکرات فوق العاده داشتیم
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69556" target="_blank">📅 09:33 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d290294320.mp4?token=SuitxCtZbeEt8eipDrhgRpyZPqmto7NqgA-omii7AdrxBC6J3hJtop3sKOdRbLvngthZDGmalwftSdgGV_VONl-602Ye1nCWwK5N4kntplvAT7gOD94rFAdpVVAGftO5mibVe5xQSvRZK5ivQat0eFwMOB6oOtCAjD_tK9Ya1Pr16wffZ1QgCbvwqOKZCX0TGSGaUEEqs4y0uHUJ5MCMDPklYz5-4_GJWNmJhGYPASMLCiI3-wJbsa9CyJXWUGbi1AwsHr3k6f0Z0LXzqPZELhiI7hriv_voZksSFrYeLEgiNwRhb1AwDyN0fg_JUykoYJKOw73AHP0Pm_DF4xn44w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d290294320.mp4?token=SuitxCtZbeEt8eipDrhgRpyZPqmto7NqgA-omii7AdrxBC6J3hJtop3sKOdRbLvngthZDGmalwftSdgGV_VONl-602Ye1nCWwK5N4kntplvAT7gOD94rFAdpVVAGftO5mibVe5xQSvRZK5ivQat0eFwMOB6oOtCAjD_tK9Ya1Pr16wffZ1QgCbvwqOKZCX0TGSGaUEEqs4y0uHUJ5MCMDPklYz5-4_GJWNmJhGYPASMLCiI3-wJbsa9CyJXWUGbi1AwsHr3k6f0Z0LXzqPZELhiI7hriv_voZksSFrYeLEgiNwRhb1AwDyN0fg_JUykoYJKOw73AHP0Pm_DF4xn44w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اینترنشنال:پزشکیان و مجتبی خامنه ای باهم دیدار داشتن و این دیدار تو یه ماشین بوده
؛
مجتبی خامنه ای صندلی عقب ماشین نشسته و تو یک مکان نامعلوم و پزشکیان صندلی جلو نشسته و حق نداشته عقب رو نگاه کنه فقط صداش رو شنیده
.
پزشکیان از مکان هم بی خبر بود فقط برده بودن ببینه اونو.
پزشکیان قرار بود از فرماندهان سپاه از جمله وحیدی بهش اعتراض بکنه که زیاد در دولت دخالت میکنه.
مجتبی اجازه مذاکرات رو بهش میگه ولی با هماهنگی سپاه پاسداران.
پزشکیان کلی مشکلات اقتصادی رو بهش میگه و میگه که اینطور بره ورشکست میشه دولت.
پزشکیان از این دیدار خسته میشه و میگه میخام مجتبی رو ببینم ولی به هیچ وجه اجازه دیدن رو بهش نمیدن.
پزشکیان که فوقش یه ساعت میشد فقط صدا می‌شنید چهره ای از مجتبی ندیده بود.
پزشکیان اصلا از این کار رضایت پیدا نمیکنه وبه رئیس دفتر اعتراض میکنه.
میگه این کار جز خورد و حقیر کردن من نتیجه ای نداره .
بدجور عصبانی میشه و جلسه خیلی کوتاه تموم میشه.
تصمیم استعفا از این جلسه شروع میشه چون پزشکیان احساس میکنه دیگه قدرتی نداره توی اداره کشور.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69555" target="_blank">📅 09:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=h3HNECduFJwjyxq5wyXef5LT3OZ2g2QCsnnZBiQrfg8-JDKOx6txYi60JUA6T6O-vmhtlJKOQ1_p6LBKIa42RjxG-DO9C9BESvtxpo9tJoofFaoVfiRHBD-hd695x5qFIZWsTauOENr6grtVmpzYtOGhX4aIc1R_G1CeQZaPXu9CA2lSUfeXwVLmNoLqgATJJv2u42hvp2DFHrIqB65VUDf5YtMAIwK-CnW6Wi0SR83-oUCYfhZfOT8PARFlKGFbnKTRr0wmsqC_tmFnOBGUU1pSbeApK2M6VdxIt0_IeBpX_iqnJvIUnPjjXOG21Gg0291PFVXCr0zhbZ0QXOLIyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7b56246.mp4?token=h3HNECduFJwjyxq5wyXef5LT3OZ2g2QCsnnZBiQrfg8-JDKOx6txYi60JUA6T6O-vmhtlJKOQ1_p6LBKIa42RjxG-DO9C9BESvtxpo9tJoofFaoVfiRHBD-hd695x5qFIZWsTauOENr6grtVmpzYtOGhX4aIc1R_G1CeQZaPXu9CA2lSUfeXwVLmNoLqgATJJv2u42hvp2DFHrIqB65VUDf5YtMAIwK-CnW6Wi0SR83-oUCYfhZfOT8PARFlKGFbnKTRr0wmsqC_tmFnOBGUU1pSbeApK2M6VdxIt0_IeBpX_iqnJvIUnPjjXOG21Gg0291PFVXCr0zhbZ0QXOLIyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازم ترامپ از ترور جون سالم به در برد:
⏺
فاکس نیوز؛
مقامات اعلام کردند که یک مظنون مسلح به نام «جنین جان تائله»، ۳۸ ساله، در زمین گلف «ترامپ نشنال» دستگیر شده است؛ وی متهم است که پیش از سفر رئیس‌جمهور ترامپ، تدابیر امنیتی را زیر نظر داشته است.
پلیس اعلام کرد که متعاقباً از منزل این فرد، یک قبضه تفنگ مدل AR که به‌طور غیرقانونی تغییر یافته بود، جلیقه ضدگلوله، خشاب‌هایی با ظرفیت بالا، مهمات و دفترچه‌هایی حاوی «مطالب نگران‌کننده» کشف و ضبط کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69554" target="_blank">📅 02:47 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">#اختصاصی #فووووری
🚨
ملی‌پوش پر حاشیه در آستانه پرسپولیسی شدددددن  https://t.me/+FgpywJWoBXVmZGU0</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/69553" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69552">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZLGTPKGzV6nvB6y6zH3ZLXTJfR4wsrKvkkL43KL_AbfFyVLDGzB-PRy6x9xqpCTHR0bYBSgQu8SUBBPTP8D_K3iWon3BkLfE18ojnPQaLvnEgBzhw-eu61Qe-YcjkEFUv_vLJTRRgWbqai24tPBK2mW3BOLlNM7dzV9hNXQy7iSYB9ODpUTUuIK2MNw8xh7ieY-ETdiEtDfbhrKX6IGwkhtHYDaBvRijb--SpJ6uDDMtVv96MI8XzDuWWJsjss9Smc8IqPqfZPIjMTN4_QtdiwraOc6Sq9ltZf4gjFes8UB2sDO2ti3cSdpo7OEOZUeHgvGAiec_kKkoFvS6yz2Vaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و پرسپولیس هنوز هم شانس رسیدن به هم را دارند!</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/69552" target="_blank">📅 02:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69551">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nscmnd8d8_rDUKoiqH5NjVUTM_CSQ6LjlZSwEoVa8B5AXCVhmP93iBdmJ-RKXJ1jjubX3YVbADoNCqnhAX0Ny8WR0h2PMf98YKn5IRQEjJGpZPhW996rgPRCltHcDUKChtienCyMI3tvPwY3cmxY7R1_MgTCA1SUnh__RJinHnlt67B62kSO4Z69OlgxFj5BpOL0rJ3cg6LZNnNun2T47rqtZsVoRHQ-ciEsFPYVmxxQEOqvpweLbwBMCvqwIFZir2-6UxnBG8iucXckvrvzdIKHxJuwO5_TIwQqyQ4s-6OCVKp11GXMu14EhpXVnsi60q_9MUPl0-9azOwwwPSyOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیزارم اینو یادتون بره
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69551" target="_blank">📅 02:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69548">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCwYuIV6xFhew2NCeMFWoTB2vCEdB928n_fbZCTTdryNhZOx6QaJHjrDlaE1YPaDgT3CzIp92mUQYgpDWIuIp5F9E_HlWgaqNYpAFBwipOKW5gQy1lin7nz4hCFH57L2VBaaxeSatQyHblJo5aihW3aoAtQi1ln0zvsY57VZy5hr5bg6bud4lKZjeMumYl_KEgdcNmra-k92KbuvakkvLOidujLiO0lkhITDKoWd9VPHXzMgyPhcLqhWivuhH0nGIKsryLBUZOMyobp2BXIswCH38lEtyyP5r0T5c77H0lJkBFhW_cFoMXNn2rzWTbW6L5Dnzp8SDWPJVvuHlheZtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GiTcZxqG3EXYAt3soA_-YrAZvQmnFkxK6i7aCiXyvtTbfpy6l2I9i4JGocok40HgqeoFpjACRW9L_zGSFzBPs84WujaHpelU9xuZTV5M3R9OVppDZcRsf-xqubB5PKapIt5Q1ZK4hLZJz2hsrxHCC_2daAwbNQrPgPRWU0Lj9O1p8pJa_ZP5Li3VjAPWUu-yBMxv30dnLZYJUWD8Pl9W_t8sXi7MiAfjSErHevWI248pJ5vWF0CRThbsYJXMIuGWs37Sngsfq_gQa8CMQxOGlEFt2m4DDqhTtb07y3nCFrkz_wqnTw-mWcMFGZkyeb0bGV0AGW2yUgn6lV7iLboFYg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=nl9DEjAYpg7RxWmICISuudpymWyUUiw-ZUkbvNwik2O6c8vR_OzglurqMRKgvRIrscibsnGio1QQ5zqR8iYqHAvJi2qOHvVCeUTTYSlr56x43KXONbrCtUCq4Gjtz_oIix8m-GeMfVFpwtRSDDmwpGEOH5F7zboQ7sA7tSwm95xt432m8aNNEAMlN0C0VahrFNsNsxG-9DZ5FLxeARQr8Uz3hhaazL6NFNQLwXdZsdzn17pCDvRA3bjbEcj6rdb8cu2uKEoMVXUscQk8ZqQOYdCHCe_f7DLrjHh2uW43YmUDehvK1e_xq8yLDSVqCVFza9Uu3KSPLTB64O84RKP2cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d579f85e4e.mp4?token=nl9DEjAYpg7RxWmICISuudpymWyUUiw-ZUkbvNwik2O6c8vR_OzglurqMRKgvRIrscibsnGio1QQ5zqR8iYqHAvJi2qOHvVCeUTTYSlr56x43KXONbrCtUCq4Gjtz_oIix8m-GeMfVFpwtRSDDmwpGEOH5F7zboQ7sA7tSwm95xt432m8aNNEAMlN0C0VahrFNsNsxG-9DZ5FLxeARQr8Uz3hhaazL6NFNQLwXdZsdzn17pCDvRA3bjbEcj6rdb8cu2uKEoMVXUscQk8ZqQOYdCHCe_f7DLrjHh2uW43YmUDehvK1e_xq8yLDSVqCVFza9Uu3KSPLTB64O84RKP2cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
❌
حملات شدید و سنگین روسیه به کی‌یف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69548" target="_blank">📅 01:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69547">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STr4YesXtW28EalMakrmozOO5Hbr5YHD8GiKEYx-fDm8R7X0cSRIgMUQF9-iSYEE36IaEAuTcmHhfGAfORw6kgp0KC2eAp2-57sxZo1Gtb7-TWM8Evkl8K079235FrvSVRa-tsWJE6es_dVDjkWCg3BwlNzD1YbsUocg4AKzpiim_kHySUKmeW-puISP2RWmLAT_kmVczDZ-s7t2_Rsvs33pOJSZLwdzBLtrdSTUt6EWxnfGtyzhv21-_SiA5opcctlzt7hx-YedlbXsCQHUKPUghq_9f7j7vKbmAyqtId1dJxevIYFVtj_mbyF5kIP_lxxsptx-o-VudRqPFCYQXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
علی قلهکی:به نظر میاد یکی از گره‌های اصلی مذاکرات ایران و آمریکا، ماجرای تردد کشتی‌ها توی تنگه هرمزه و هنوز سر جزئیاتش به توافق نرسیدن.
هنوز مشخص نیست کشتی‌ها دقیقاً از کدوم مسیر باید رد بشن و مسئول امنیت و هماهنگی عبورشون کیه.
ایران می‌خواد کشتی‌ها بیشتر از مسیر آب‌های خودش عبور کنن، اما آمریکا و طرف مقابل مسیر عمان رو ترجیح میدن.
اختلاف اصلی هم روی نحوه مدیریت، امنیت و کنترل تردد کشتی‌هاست.
هر اتفاقی توی تنگه هرمز می‌تونه روی روند مذاکرات هسته‌ای هم تاثیر مستقیم بذاره.
آخرین پیشنهادی مطرح شده مطلوب ایران اینه که کشتی ها حتما مسیر ورودشون، مسیر ایرانی(شمال)باشه و مسیر خروجشون حدود ۴۰٪ کشتی‌ها از مسیر ایران و حدود ۶۰٪ از مسیر عمان (جنوبی) عبور کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/69547" target="_blank">📅 01:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69546">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xh2qS7FPz3xG2lvjkRa6Vvl65xUUNOjbCsYZMxXwiRfV1jrlZEWi5F4pVWl-YN-MtPFFEPodGbtr7BidkYx2jWMu5dzgtAkl24Pm7TX06uI2Z_6UX0PB93z0DnDcW4QeaESFhNs2FdhecPYm5QiCuvP9PQ6PIpsgosQIHoGGdRAbhfAyqoh7OdDsyfEInPuwZHHsL5HOf7JnC_D79C84GxbE6WNNAgFEXb2QKtbobHHyS2gc-N7mnpHDV2ihMY1y8z_V48ntbJk1CU4XhNdcbKCyeJ9E5MLP5jNZZ3NFlnZzKaLMwd079Yl-930gbxiHb5il9c7cP-NdbEWE1ImCsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🇺🇸
بازگشت غول‌های سوخت‌رسان؛ بزرگ‌ترین آرایش هوایی آمریکا از زمان جنگ خلیج فارس ۱۹۹۱.
پس از پایان جنگ جهانی دوم، جنگ خلیج فارس در سال ۱۹۹۱ با استقرار حدود ۳۰۲ فروند هواپیمای سوخت‌رسان، بزرگ‌ترین تجمع هواپیماهای سوخت‌رسان در یک عملیات نظامی به‌شمار می‌رود.
اکنون نیز در سال ۲۰۲۶، با استقرار حدود ۱۹۳ فروند هواپیمای سوخت‌رسان در منطقه برای پشتیبانی از عملیات علیه جمهوری اسلامی، یکی از بزرگ‌ترین تجمع‌های سوخت‌رسان‌های نظامی از زمان جنگ ۱۹۹۱ شکل گرفته است؛ آرایشی که در بیش از سه دهه اخیر کم‌سابقه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69546" target="_blank">📅 01:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69545">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sKvuEVKvGVxQN7fzpgYFDwFpL9Y-Z8e9tRD8l4Vxcbk4f5HP23AomYx4Eo9KgIKZ96pgvSb-NyxL28XaC6nBvmN_64REqG4HFPQxh8h75CgWAnou-d5RnWiJUD_Y1xSUXbgm4Ou7XxlqpQ9cnEVHPybLeifHSoWNmpAtlZKk4-dxglo5kEhbHc_d4B9hC0j6ZFnPlyRKdEXBsOrIRQekYX4iCxICzRHkhoH6EevG5R9gNwENGk_0cemGGxFMDTYV6QeZGKPIlCzlvq8nqeYlTVEDhiLEchAL7gzRQ5iZXEBrPKYPALQOzJ956nnmQWFbrXQFI9YtoX7tVCO-9FWI_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:مسیر جنوبی از طریق تنگه هرمز برای تمامی شناورهای تجاری که قصد عبور از این آبراه بین‌المللی را دارند، همچنان آزاد و باز است.
طی سه ماه گذشته، نیروهای آمریکایی علی‌رغم اقدامات خصمانه و بی‌دلیل ایران، به بیش از ۱۰۰۰ شناور برای عبور موفقیت‌آمیز از این تنگه کمک کرده‌اند و این ترددها همچنان ادامه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/69545" target="_blank">📅 00:30 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69544">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=vVotY4veLhr4KwhJOCNIUzjDqVvY9Amrs-4o2fY6IKVVPJN_5q51T_pLJYGESc_RassVbKjTIuN_ZFSDs4hki5EJkb_FsKvWPMg8zhpPHF8zcArqLpKdOTmXsgbm2_YSSgx2ZKdRyGUYf_EmJAP4ee4GZoTrPmsUv9s6RqS3KkPeu-bFvVFtbGl4vGkSx3SrBDOPCor0u6o5YmSPzJT5HtRLBjrdJm5fwUrLyuytTTPDw7yyrzrCtHGiRTBahq7GZQhBNv4KKrC-2nJ5kdsCniPpxYaauTN9qBMVor7I_6xB6Jko6CpDqOGfq3ahV9NYjXFPV0-CFq-ogQ_gEiFzRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31eaaf6719.mp4?token=vVotY4veLhr4KwhJOCNIUzjDqVvY9Amrs-4o2fY6IKVVPJN_5q51T_pLJYGESc_RassVbKjTIuN_ZFSDs4hki5EJkb_FsKvWPMg8zhpPHF8zcArqLpKdOTmXsgbm2_YSSgx2ZKdRyGUYf_EmJAP4ee4GZoTrPmsUv9s6RqS3KkPeu-bFvVFtbGl4vGkSx3SrBDOPCor0u6o5YmSPzJT5HtRLBjrdJm5fwUrLyuytTTPDw7yyrzrCtHGiRTBahq7GZQhBNv4KKrC-2nJ5kdsCniPpxYaauTN9qBMVor7I_6xB6Jko6CpDqOGfq3ahV9NYjXFPV0-CFq-ogQ_gEiFzRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
پزشکیان:
اگر استعفا بدهم، رسماً اعلام می‌کنم؛ استعفا نخواهم داد و خواهم ایستاد
ما با نیروهای نظامی، کاملاً هماهنگ هستیم.
می‌خواهند اختلاف درست کنند که رهبری یک چیزی می‌گوید و این‌ها یک چیز دیگر.
همه مردم برای ایران سختی‌ها را تحمل می‌کنند.
یک عدد سه هزار نفری را سی چهل هزار نفر گفتن، نشان می‌دهد که این‌ها چقدر نامرد و وطن‌فروش هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/69544" target="_blank">📅 00:15 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69541">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aoZDFwGupEia8zrxiWu6bQMFKFQj86OOH_Ih0fAdNX_egdUk_n-JKIzI2OEWvcFtGbirTEsQkFxPvA32oK81AqW6LoyxOECPbJOC2h1PN_i1lIMCRV7RHKumxAP5cLF6HK9utrttHjKfVAfUrCC2uf6I7nhVVJKvCpSwbSjOe-um0_bfuODaOmO7KPItL6F9I4gRunQpWHb8v9oaoUoWU913-qe6qJPtHlC_Il-HB9rj18-fn1SAa0yiRu4SU4Jvt8AYs0AZYFwsFrAKzVeEeJ9AKJNmN85c2kb5s54W67lW3UAf-xXncoowu_c1wU0M4GgS0IkBbBVNgxlfyis3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iNdUHdEP_oXjLyDvOjtm6X4nHo6esUnUgQtt7q_YK42VanbMsa66937mbojVOb6fhpBZOdpGZyK1F99ngtMvZY9TR6Id0eVr5cI370tofAjoVbLCMH3_URGCJ6HXB2rDtYeg0vQHMZjSutWL3xSixfHZiftsVRe4yA3Z4aE77AOkUR54qXgEzPZ3SiUjvh4fJKqZzxS-_cUoM9tqy8bq0eENmD5GB94G6hrYT_5nyMOCRAtuKuGD3L-L3YKsXnOvmx1JRa_OUFgv4SG_lKaPqWoq5gLDygVLS7y_NtvHc4dmN8gSDdQafR3mvHBWdhqnxtEMa-5cmCZy7dLif0W45A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">▪
🇺🇦
رونمایی اوکراین از ربات رزمی «Droid TW 40»
.
شرکت اوکراینی
DevDroid
از ربات زمینی تهاجمی
Droid TW 40
رونمایی کرد.
این سامانه با حداکثر سرعت
۱۳ کیلومتر بر ساعت
، برد عملیاتی
۵۰ تا ۷۰ کیلومتر
و ماژول رزمی
Wolly
مجهز به نارنجک‌انداز
Mk-19
کالیبر
۴۰ میلی‌متری
عرضه شده است.
برد مؤثر این ربات برای درگیری با اهداف
۱.۵ تا ۲ کیلومتر
اعلام شده و
Droid TW 40
می‌تواند در حالت آماده‌باش تا
۱۲۰ ساعت
در میدان نبرد باقی بماند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/69541" target="_blank">📅 23:32 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69540">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCj6EmlXzLAO9o9VzXHV7u_q2-IkiX_OPyDLZeyxnr55euSTtSCZX3uNLhY9hrdzTODrNxGH_S7PEPCZdwVDa0jYteVfNsWE8J80YNxoFPscZUOgzEatxzY_T0c9CIZ2p8ngzyZMNEs0UfTW0twquUMWa5HP0GirWffHkUOcK_EPoFAuZx0ZPYwtbd6ts0cqcpSqQZUS73ffY0BkomsjqeK4uxrPGcWZaiwVmXcH5xinQNIOtzct_9-gfYZ8e6QpmGiWbFVGQbk8a8PCKJLdLlQIj0s484t-LpRZ0OnLKomWy9bbFNna-3wxI9CVoCTFplOT-4PQglD8Qw_-_wzxyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎨
نقاشی وایرال شده از زمان قاجار:
در زمان قاجار زنان روی یک وسیله تاب مانند میشستن و یک زن قدرتمند، اونارو بالا و پایین میکرد.
شاه یا یکی از سران مملکت هم اون پایین دراز می‌کشیدن تا زن انقد روی آلتش فرود می آمد و بالا می‌رفت، تا ارضا میشد!
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69540" target="_blank">📅 22:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69539">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=ZO7RqUtj9AFlbd2pe3q4kdIveco87me7q_oz1spWsMOcf4gcrUUDeHcw39qjji3j7NlY4k6jPKe-Vdacs7O04MXnbJERbJvMa5158LuNXKFFVrdV1L5NNj5iXJSMq95NTTCfduWBYd_kE-SBCQXASg2Ivei7NOoRIEf3G1iMQoaYwH6-brabbM-Mr5lkRQlkf3U1_VQTt_7Gm4QRfzEuaXGtDldUfEW5BiuNJM8ugTbtSO8X11mM1WjPcfXRsf0wHfYWhbFOiymKM9afb3JSc-3DbxROp6P1CS2zGJZqn7lIzHY8ZzwZguul869l2GaLqFHuCnErxFrgImnUjin01g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c9b5938d.mp4?token=ZO7RqUtj9AFlbd2pe3q4kdIveco87me7q_oz1spWsMOcf4gcrUUDeHcw39qjji3j7NlY4k6jPKe-Vdacs7O04MXnbJERbJvMa5158LuNXKFFVrdV1L5NNj5iXJSMq95NTTCfduWBYd_kE-SBCQXASg2Ivei7NOoRIEf3G1iMQoaYwH6-brabbM-Mr5lkRQlkf3U1_VQTt_7Gm4QRfzEuaXGtDldUfEW5BiuNJM8ugTbtSO8X11mM1WjPcfXRsf0wHfYWhbFOiymKM9afb3JSc-3DbxROp6P1CS2zGJZqn7lIzHY8ZzwZguul869l2GaLqFHuCnErxFrgImnUjin01g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای از یک پهباد روسی که یک شهروند اوکراین رو تهدید میکنه و در آخر هم خودشو میکوبه به طرف و منفجر میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69539" target="_blank">📅 22:16 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69538">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3447971507.mp4?token=mvve_MJAc6V5fi9tu2svLOTYT7aqehNxLVEdSqNt16_dDhhCXwsOq-3R4f6vqYobQWFPbJ7wntrjW9EK36B37ML6_nUmPEEqN8Lpe4dqHOze3Qic8W98do7DVO_h1gGKLD3NOsoLGic_LcxhRbzx9q4k3yTBKHqvbmOEvua5vFac2W8Ckxl9_23E1S6zDL7SDT9VbZk8QeVCGJ9Qd9E3c1v4dHVpLCJ8iYjjO93S1sFE-Pv1H-I0fafw8SKG6PBf6IgtCKQeEzyYd5O09iaHEkzukVP4qxWzJ1LfAvhUg0cKWSGt_hUNQIfYpk4Z-F_8EyuVXUdLw2J8rF0LtwQUxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3447971507.mp4?token=mvve_MJAc6V5fi9tu2svLOTYT7aqehNxLVEdSqNt16_dDhhCXwsOq-3R4f6vqYobQWFPbJ7wntrjW9EK36B37ML6_nUmPEEqN8Lpe4dqHOze3Qic8W98do7DVO_h1gGKLD3NOsoLGic_LcxhRbzx9q4k3yTBKHqvbmOEvua5vFac2W8Ckxl9_23E1S6zDL7SDT9VbZk8QeVCGJ9Qd9E3c1v4dHVpLCJ8iYjjO93S1sFE-Pv1H-I0fafw8SKG6PBf6IgtCKQeEzyYd5O09iaHEkzukVP4qxWzJ1LfAvhUg0cKWSGt_hUNQIfYpk4Z-F_8EyuVXUdLw2J8rF0LtwQUxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
چهار سال پیش در چنین روزی، یعنی ۴ اوت ۲۰۲۰، انفجار بندر بیروت — بزرگ‌ترین انفجار غیرهسته‌ای در تاریخ معاصر — پایتخت لبنان را ویران کرد.
هزاران تن نیترات آمونیوم که به‌شکل نامناسبی در آشیانه شماره ۱۲ انبار شده بود، دچار حریق و انفجار شد و موج انفجاری ویرانگر ایجاد کرد که چهره بیروت را در عرض چند ثانیه دگرگون ساخت.
این انفجار دست‌کم ۲۱۸ کشته و بیش از ۷۰۰۰ مجروح بر جای گذاشت، حدود ۳۰۰ هزار نفر را آواره کرد و خسارتی بالغ بر ۱۵ میلیارد دلار به بار آورد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69538" target="_blank">📅 21:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69537">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=a2hcyZXbtvstVgjBqVbYOBbRp0WiRRQB_e4fnRbeUyTZCyOAMry6wxxdwmdtzcq4HmB5yyfxCTy5XMlOeoXwyvobYm8hrB55OCEA1gtwuwsYWOi8s-pVBddO58zKS2IE--9f-FDbQgo7WPJPRmQuW4XaO5W-ztl6qDQ0tRAGiQgYgorh5OtEvjrAsmxvLleOUWPmtE-poXTAv8W_PlcdBY3k4BiDYTiFRFnYs6pP2vk7_5HzaVLD7FpLNHPGjLnS-8YHzTj53yAxQgKMCx7ly8BD26GrhGoXHCo8CDLCeuobSbbdxAA5Jizyi_Hvqs4Ci5DGwWIbDicr10O4wR4prg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8eaaff36d.mp4?token=a2hcyZXbtvstVgjBqVbYOBbRp0WiRRQB_e4fnRbeUyTZCyOAMry6wxxdwmdtzcq4HmB5yyfxCTy5XMlOeoXwyvobYm8hrB55OCEA1gtwuwsYWOi8s-pVBddO58zKS2IE--9f-FDbQgo7WPJPRmQuW4XaO5W-ztl6qDQ0tRAGiQgYgorh5OtEvjrAsmxvLleOUWPmtE-poXTAv8W_PlcdBY3k4BiDYTiFRFnYs6pP2vk7_5HzaVLD7FpLNHPGjLnS-8YHzTj53yAxQgKMCx7ly8BD26GrhGoXHCo8CDLCeuobSbbdxAA5Jizyi_Hvqs4Ci5DGwWIbDicr10O4wR4prg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
ترامپ و تیمش تصور می‌کنند که می‌توانند حماس را به خلع سلاح و غیرنظامی‌سازی غزه وادار کنند.
آن‌ها پیش‌نویسی برای ما فرستادند که ما با آن موافقت نکردیم.
این پیش‌نویسِ ما نیست؛ ما نظرات خود را ارسال کردیم. ضمناً، ما نظراتمان را پیش از آنکه شاهد هیاهوی رسانه‌ای پیرامون این موضوع باشیم، ارائه داده بودیم. موضع ما همین است.
و ما بر سر منافع خود، هم با درایت و هم با قاطعیت، ایستادگی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69537" target="_blank">📅 21:20 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69536">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_4bjYp_LKmJUb-tqwt9By2s-400L9N0mPiKx8Jc4apEMGZTzqvLFVJz3CUzyt8-we18lXobAhnhlkQlXWrB11wk-DFXzLq2JjSGXL3kBVedyONZ1DWhZrUMjoCiDMuw3NGLLCDqeZvhjGgHgM2PlxIJIxAFQ3O5VZojofOHEWkJK3Dso_TMlyraNZNPlUI5nzqVe9NxYS_iC8SuyBhSz1JR3ofjBRtR1I2tcaKX5ok6nzg5FCQfSRwA1i65hLVpQ3SrLgEwERQpLse5uWzDpiTvemfuNDJAm2JEw9r1_wCftydbZtv9we43apURdnpUXWAW71I7AmmHI-sVgLAtdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وال‌استریت ژورنال: در حالی که دولت ترامپ بر نزدیک بودن احتمال دستیابی به توافق تأکید داشت، وقوع حمله‌ای جدید به یک کشتی در حال عبور از تنگه هرمز و بروز اختلاف بر سر مسئله عوارض در جریان مذاکرات برای بازگشایی این آبراه، چشم‌انداز این کریدور حیاتی انرژی را با ابهام مواجه کرد.
به گفته میانجی‌گران منطقه‌ای، بر اساس پیشنهادی که هم‌اکنون در دست بررسی است، کشتی‌های عازم خلیج فارس از مسیر آب‌های ایران وارد می‌شوند، در حالی که شناورهای خروجی از خلیج بدون پرداخت عوارض از آب‌های عمان عبور خواهند کرد.
میانجی‌گران اظهار داشتند که اگرچه دیپلمات‌های ایرانی در ابتدا از این پیشنهاد استقبال کردند (زیرا تا حدی کنترل بر تنگه را حفظ می‌کرد)، اما تهران خواستار حق دریافت عوارض ــ که احتمالاً با عمان تقسیم شود ــ و همچنین دریافت تضمین‌هایی در برابر حملات مجدد، پایان محاصره دریایی آمریکا و کاهش تحریم‌های نفتی شده است.
مقامات ارشد منطقه‌ای اعلام کردند که آمریکا و دولت‌های منطقه با درخواست دریافت عوارض مخالفت کرده و خواهان تضمین‌هایی هستند مبنی بر اینکه ایران و نیروهای نیابتی‌اش، قلمرو آن‌ها را تهدید نخواهند کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69536" target="_blank">📅 21:13 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69535">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIkU9Al4ttcdIKqKddFRHmyos6KGpT3QXUusWTaUhZFqX_LqHwQysMlJP3ti0OTQ_pxJvwVROzoElq4qQkPA_DTYZKbACCYSISA3X85Yl4Mkrhmt9ovK5vile1kq5-8ChoKGk1aQTqY8mjaIdmYb-PrNDzzGprfmFdP_6xVMq8NfiQBNbrhjcPo5RoFt4eu25G2XT7ofdY6oQ-bUFmKnzqaSqXOLM2sBB7tzcbXLQ84fZEL7S6qf55SrZvFAoWyN_sWhdi6ahlaBfOXGAN4rezWUWLR6gq-NhFUMq4SMvPBYP2p2o32BGky9WgJwpK5bKe5zSlf113F13WXMfscn4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سنتکام:یک ملوان نیروی دریایی ایالات متحده در «مرکز اطلاعات رزمی» ناو «یو‌اس‌اس باکسر» (LHD 4) مشغول نگهبانی است؛
😃
این ناو تهاجمی-آبی‌خاکی در حالی که از محاصره اعمال‌شده توسط آمریکا علیه ایران پشتیبانی می‌کند، در آب‌های منطقه در حال حرکت است.
تا تاریخ ۴ اوت، نیروهای آمریکایی مسیر ۴۵ کشتی تجاری را تغییر داده، ۲ کشتی را از کار انداخته و برای اطمینان از رعایت مقررات، وارد ۲ کشتی دیگر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69535" target="_blank">📅 21:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69534">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=nckyAn90RN40zU20gGOe8Gtmgc6sG53oMipvmfuqxilJyAR41IyLzHBhMRdpA2foJwn0Ed2bJRG-KkXT3okug_Eqkb3qoqbitov_z6zjdDycP84t5_4ILPdwcpKU1ZBNirozkEc5GY5JV3yKcLtL_R4uICZzyRRHJrVksvA5Q1yb22RIHU-YgKoufYfhrq7zsM1aECzS9Tx5iEqCT-u7ML84R8y0GlJUKo6sWE-Z70oF9aniRVwe3z2tuGvBkCwxmQfIXHcnCPtPqrTS5_nabDbv0G-R2-XBLXMQmx5o7TxqYUBDpA5M54UMBLw88Z2krz-WDTtk_JQRBkwi_7FUCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19c9ea7021.mp4?token=nckyAn90RN40zU20gGOe8Gtmgc6sG53oMipvmfuqxilJyAR41IyLzHBhMRdpA2foJwn0Ed2bJRG-KkXT3okug_Eqkb3qoqbitov_z6zjdDycP84t5_4ILPdwcpKU1ZBNirozkEc5GY5JV3yKcLtL_R4uICZzyRRHJrVksvA5Q1yb22RIHU-YgKoufYfhrq7zsM1aECzS9Tx5iEqCT-u7ML84R8y0GlJUKo6sWE-Z70oF9aniRVwe3z2tuGvBkCwxmQfIXHcnCPtPqrTS5_nabDbv0G-R2-XBLXMQmx5o7TxqYUBDpA5M54UMBLw88Z2krz-WDTtk_JQRBkwi_7FUCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنتکام:
یک جنگنده رادارگریز F-22 نیروی هوایی ایالات متحده در آسمان خاورمیانه از یک هواپیمای سوخت‌رسان KC-135 Stratotanker سوخت دریافت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69534" target="_blank">📅 20:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69533">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hVJJ-dCdVlhkWT-OCS64aWXeWh1pP4mAfdmWRXO5Lt7cyywoTglXYp25yO9pdwCrbe66XUJcN1DtB2MXKrRMqEOeHuZZjBAPzo69RTrg8dzpSXnZPtq753lkAC5aNXisHBO1qM7mO8YM1OwlqKFqRNAEn1n0MTIP6XoLTA6N_Qj-epA19w2IIIXOFUO0q0fcXNe1jIijM3zml0Ldo2QewCm0wqxHw6QK12bc5bQzZDWwtltQ9gTuGWwK-WqL6oDlDhAnKMiZv2j3fOYTfGQz93k_X-uRTU8-252OboNLuioNxyH8W_L_ydc_EXI0WMg_j2Csq9yDACgiQFE4NoIabQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ایران در حال بررسی امکان مشارکت کشورهای اروپایی در عملیات مین‌روبی در تنگه هرمز است؛ اقدامی که نشان‌دهنده احتمال تعدیل موضع پیشین این کشور بوده و می‌تواند به تلاش‌ها برای ازسرگیری کشتیرانی و پیشبرد مذاکرات با ایالات متحده کمک کند.
تهران پیش‌تر به‌طور علنی با هرگونه نقش‌آفرینی خارجی در مین‌روبی این آبراه راهبردی مخالفت کرده بود، اما در هفته‌های اخیر و در چارچوب گفتگوهای گسترده‌تر پیرامون عادی‌سازی تردد دریایی و کاهش تنش‌ها، انعطاف‌پذیری بیشتری از خود نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/69533" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69532">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=e6cFKJ8T6jEkUnQmdyu0Aek5BY1v7DzQYlrLV91NaUO_tuWWmJji0q_qOlbPGjJr3WUflze8OuW4gDErS4C8FKrzP_V9i-7nGMyWFUnlcleXPAT7HhcV7BHrdw-2FmPJHNiFyTuwLYY4QTKyesvmtwbVfyu2Uan8CKs3A3HQnAmAdKEYvYz8nrcr9Uhx0a_cq0C03VG8Lhm_XUncZGnTVvzS9DxQRkdfNtxRi4v5alcoKpZkfcXPhuds9IxtupAS91bh9sPnHEgQBUhmniAZA6aF4rqb3Ac31BAGMsgwzX6xnksYqi3c-8S7wJqTK01dvvcxzNQUMQYr16lUGfFKvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3030125dc6.mp4?token=e6cFKJ8T6jEkUnQmdyu0Aek5BY1v7DzQYlrLV91NaUO_tuWWmJji0q_qOlbPGjJr3WUflze8OuW4gDErS4C8FKrzP_V9i-7nGMyWFUnlcleXPAT7HhcV7BHrdw-2FmPJHNiFyTuwLYY4QTKyesvmtwbVfyu2Uan8CKs3A3HQnAmAdKEYvYz8nrcr9Uhx0a_cq0C03VG8Lhm_XUncZGnTVvzS9DxQRkdfNtxRi4v5alcoKpZkfcXPhuds9IxtupAS91bh9sPnHEgQBUhmniAZA6aF4rqb3Ac31BAGMsgwzX6xnksYqi3c-8S7wJqTK01dvvcxzNQUMQYr16lUGfFKvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حسن عباسی:
زیر جزایر و سواحل تونل‌های موشکی متعددی با امکانات متروسازی شهرداری تهران ساخته شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69532" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69531">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتبلیغات</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzsRH9rBhLfjATYlyi9O60PRfRsDTSbBllYIunlgfCyvh0sN5PgypFlfssloFz9XXUNHPHBt3k11hUzPM9nfFcor3qIIzjKrOs1fNdUt3yTYGfrsMWk0boAACkooPodTQDxPoNpxX59DlpnevbZsiaukqBzb676E2YAByPlLUxCUNZ0oTkseaQVQyynJ0c1j5zXVPVZWDzCXzQWZvTQ4-UpFhb2NYtU6idKtqd65UHptLaiU7d1H1JkTPzpp2ijr4hCJxjjnIQCX01u76c89iTS_Bt5RzS56dQ8YBuwCPaybuvQURKuHjAhPFhG_rB_Eghf3vP0xIRIJcEOFEA7JNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
این حساب دوستمه تو ۱ ساعت ٣٥ دلار یعنی ۷ میلیون در اورد
🥇
گفت یه روش که با گوشی انجام میشه
💎
۹ دقیقه اموزش میبینی سرمايه اوليه ام نميخواد تا ریسک نکنی
🚨
بعد ۹ دقیقه میتونی روزی ۳ ۴ میلیون با گوشی در بیاری
رو لینک ثبت نام فوری بزن اموزش ببین
⬇️
⬇️
⬇️
🆓
ثبت نام فوری
🆓</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/69531" target="_blank">📅 19:52 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69530">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=eLYMLKXH8wltjJVdsWhHSyxgrCMheqDw0kekSHQkbJRmQUhNCtt8yawwOEX7bIDzR9ZutPAi7qEacAMxwpYlgabJ_ZEJ96wNKhh0QOB8E5FADD-_8f1IfsWHMacUNUnkxgjhMdYH9MBZXQQviznvoysaLsAvCdt0TPNlC7lbcdHr4q0hM1aHk16ppG234pSeoX5tyrghmSoY6G9qccF0p8XV-9lt_OqvJgl-rxRS7TzlKb3uu8xKLmwKuu710c9OHakWKGR1vy-p6TvmLiVBojXRgWbzFWITfpzrq_KjiK7ftZndfm4JsycjbSCnqaZk1MFrTAR5qh2OMGr0QL_igw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca94237dda.mp4?token=eLYMLKXH8wltjJVdsWhHSyxgrCMheqDw0kekSHQkbJRmQUhNCtt8yawwOEX7bIDzR9ZutPAi7qEacAMxwpYlgabJ_ZEJ96wNKhh0QOB8E5FADD-_8f1IfsWHMacUNUnkxgjhMdYH9MBZXQQviznvoysaLsAvCdt0TPNlC7lbcdHr4q0hM1aHk16ppG234pSeoX5tyrghmSoY6G9qccF0p8XV-9lt_OqvJgl-rxRS7TzlKb3uu8xKLmwKuu710c9OHakWKGR1vy-p6TvmLiVBojXRgWbzFWITfpzrq_KjiK7ftZndfm4JsycjbSCnqaZk1MFrTAR5qh2OMGr0QL_igw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
غنی‌سازی اورانیوم چطور انجام میشه؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69530" target="_blank">📅 19:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69529">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmW1c4QlJa7hyI6Rg5abEkk6Fq7zgH8gFnzkYI2yZlHTA-E7MNelLOfChLibuv5uadUFqTZRzh6601FO6TryWll0aS6kvRR5jSxOUrgN-Rt-UJl9fXY_4yxbI-MHdfrYnKRoV5I3npovKtU7o8KfHO__QuNgj_EmXnAZupge7jYKfU6d_qNCy5ISch1-sZAWgNFWz5WmTwPs0lA6JQJMnQZSvrX34OTDOuSoFgxKhpTYMh6dj2LnDSV-fnSHppjhPBEeqGAPWg3XB5_N6xevGfmVzvHjMYeEgR6lR66hz9ByrqbkQyy63IVsySxUuDGIv9O3yLEAMDfoSPQzs7LeIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
"توافق قریب الوقوع است" با از سرگیری مذاکرات با ایران درباره خلع سلاح هسته‌ای و تنگه هرمز.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69529" target="_blank">📅 18:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69528">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:  کشتی‌هایی در حال عبور از تنگه هستند. هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است. تنگه باز است. ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/69528" target="_blank">📅 18:01 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69527">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=oFYlB8P2cFqkQle5yq311wGsF-eM9XzloyX7FOc_OSwl6rUWR8KqDP5-zixqcFAT-ZwYk-FIEs92bSJVp1lyHoDeVo18TusRWY4gN7ZP9ZkT2wbuIpdh3J2WlPsMB5xE4-NEmj8d-zhaOrubnBgKGmbjJdEJoMwMfKt4SxfBsSzB2MNhSBa2IHFEMiUGBu0Dv7rSfaGoJKhUh8umRdX8pVyi1kvc5aBoL7JeD0mm1ZhuYw7xeZJEY4LEhf9tA4VVnhJnl0wc4bseUtwzrzBVf4M3SkuyQ-PJsuakvmrK2zdtrY_yRUe6HVKHptBBMClnfDikkIu4ZrGQEYs576VKWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1eaa69fa8.mp4?token=oFYlB8P2cFqkQle5yq311wGsF-eM9XzloyX7FOc_OSwl6rUWR8KqDP5-zixqcFAT-ZwYk-FIEs92bSJVp1lyHoDeVo18TusRWY4gN7ZP9ZkT2wbuIpdh3J2WlPsMB5xE4-NEmj8d-zhaOrubnBgKGmbjJdEJoMwMfKt4SxfBsSzB2MNhSBa2IHFEMiUGBu0Dv7rSfaGoJKhUh8umRdX8pVyi1kvc5aBoL7JeD0mm1ZhuYw7xeZJEY4LEhf9tA4VVnhJnl0wc4bseUtwzrzBVf4M3SkuyQ-PJsuakvmrK2zdtrY_yRUe6HVKHptBBMClnfDikkIu4ZrGQEYs576VKWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو، وزیر امور خارجه درباره ایران:
کشتی‌هایی در حال عبور از تنگه هستند.
هم‌اکنون نفت از طریق این تنگه در حال جابه‌جایی است.
تنگه باز است.
ما درگیر گفتگو و مذاکراتی میان عمان و ایران هستیم؛ موضوع این گفتگوها آن است که چگونه می‌توانیم در کوتاه‌مدت و هم‌زمان با حرکت به سوی مذاکرات بلندمدت‌تر پیرامون خلع سلاح هسته‌ای، امکان عبور ایمن تعداد بیشتری از کشتی‌ها از تنگه هرمز را فراهم کنیم.
در مذاکرات برای بازگشایی تنگه پیشرفت‌هایی حاصل شده، اما هنوز توافق نهایی صورت نگرفته است.
ما امیدواریم که این توافق به‌زودی نهایی شود
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69527" target="_blank">📅 17:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69526">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=CK-MEHrb7bFnruTkHmSLV1oPhsxPqmdVj3UNNWj6KbX8f-SsNboUSlwawazFDP-YvxQgUfb5OM8DVskbDa9TTx07_9HjP_m6M18jZPyNmvqi2p9suU38aVLTp9HrSS2BWP4dUXTQVVETeBPSkS9lg4FJRgDNdVUqua5qdTGhVvHYICZNdp0D1n67En7sZBQnO7GrAZwsRhBXs_XjBKGcs9-N3pfVro9jKh55oX0bK7Sg0sioJemfSj5wk3mUdEQto8M1gWFB-HEqk_dQKhFN-XEmoNDsShFxZw0HyzDRcsiBNTOf8fGbSI48RuLfbc5VQIlE6NH3CR74xEfAeBpL6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78294ca69a.mp4?token=CK-MEHrb7bFnruTkHmSLV1oPhsxPqmdVj3UNNWj6KbX8f-SsNboUSlwawazFDP-YvxQgUfb5OM8DVskbDa9TTx07_9HjP_m6M18jZPyNmvqi2p9suU38aVLTp9HrSS2BWP4dUXTQVVETeBPSkS9lg4FJRgDNdVUqua5qdTGhVvHYICZNdp0D1n67En7sZBQnO7GrAZwsRhBXs_XjBKGcs9-N3pfVro9jKh55oX0bK7Sg0sioJemfSj5wk3mUdEQto8M1gWFB-HEqk_dQKhFN-XEmoNDsShFxZw0HyzDRcsiBNTOf8fGbSI48RuLfbc5VQIlE6NH3CR74xEfAeBpL6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز تو پاکستان، یه تجمع ضد جنگ برگزار شده بود که وسطش یه گروه جنگی اومدن انتحاری زدن در رفتن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69526" target="_blank">📅 17:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69524">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36lnT9lARB6JYGhal0-zyLzFozzhITUR4r4Guhxj9CKJqpQ7GxHFEyaoZz6qAElEea7XiH3mLn5drYh7mDxf8Ak2t5sCFQJ8kWTOtcPOroKi0xkTj9vraaVez9TfJ02IqPu_HsGVR8YiTT8SHKwD8vIIxWpJswnK__ShtgATV8Rqno7JjlW8BaQZyaL6dalfxihapMHjPWXPb96Vxn6TqFi26J04NJPqJBmTDSP2Ym3y0zqZ8TEpt7_cLFJkZTRvizEfiUbJt41OjnsEts-PBvf-yrbGoOMo-bO9gKFPAd_teCeEDv9UlJ3cTH2EBseLl-pku51vu5qXRbzkDSsDw9JNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57327c22c5.mp4?token=ctSlnAtD_d5BYNb5qPTIScQ8K4N9pZxm-tSzhry1Ut6nF8ygp-sSA5hQK72tD3gurANNuQ7Spn46-12C8OshHSzZewx5vJZ_UfC0oWQlmGmTsnzOhzKGhOHfbYF2ybDgoz_gYrfQjNrVo8xcxKbFc9YG73hTM3b8LGoLk_oObISa5dw9H_spJWRfKtYckl35k_p3pN2oXki2ljOBj5BUkXkyaCc5hIOEVDMPUlSgxRVcy4wISQxgLitaugvtfdAlh0ea2Vwc7A3BewKiAeGIwa6a3BYElwD1WDyTl6Q1byYuxdcZULgQDfgZDMxYHsOqOp3geqW7sHAo5vBFVL36lnT9lARB6JYGhal0-zyLzFozzhITUR4r4Guhxj9CKJqpQ7GxHFEyaoZz6qAElEea7XiH3mLn5drYh7mDxf8Ak2t5sCFQJ8kWTOtcPOroKi0xkTj9vraaVez9TfJ02IqPu_HsGVR8YiTT8SHKwD8vIIxWpJswnK__ShtgATV8Rqno7JjlW8BaQZyaL6dalfxihapMHjPWXPb96Vxn6TqFi26J04NJPqJBmTDSP2Ym3y0zqZ8TEpt7_cLFJkZTRvizEfiUbJt41OjnsEts-PBvf-yrbGoOMo-bO9gKFPAd_teCeEDv9UlJ3cTH2EBseLl-pku51vu5qXRbzkDSsDw9JNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به انباری از Wildberries در منطقه کراسنی بور در منطقه لنینگراد روسیه حمله کردند.
انبار اکنون در شعله‌های آتش فرو رفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69524" target="_blank">📅 16:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69523">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/523118296c.mp4?token=Gpajn-jaXefbyGUt9LLXD9cHdeA_B8lPzl40y47CyrslWSyfQj4VjXzNQrHk3IhpQuxCMfYIfZkbuVJkwFzh75wE1PIuR0cfMtZpZt6sCvr4APDH_ufEaYVF5GUzDMCCg6WJp5QI3661YDQFmo7HlMImijnCg2vlnhW_56KQpdBPyVWuQIuvDoa469GVb3gwe4x8tWkvQIgMFykn1WbVuYzfQEotS3CThx_8uWz6MTLYIvD27gEe3QK5q7CwFlHJ6WrvdVYTgOHhodZqL-kq03i4ck4fuevhLwbivDy95nJcHH4t_zE2rV-ku8DVgU7VUHuQMhyVca0AUc96D3JdXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/523118296c.mp4?token=Gpajn-jaXefbyGUt9LLXD9cHdeA_B8lPzl40y47CyrslWSyfQj4VjXzNQrHk3IhpQuxCMfYIfZkbuVJkwFzh75wE1PIuR0cfMtZpZt6sCvr4APDH_ufEaYVF5GUzDMCCg6WJp5QI3661YDQFmo7HlMImijnCg2vlnhW_56KQpdBPyVWuQIuvDoa469GVb3gwe4x8tWkvQIgMFykn1WbVuYzfQEotS3CThx_8uWz6MTLYIvD27gEe3QK5q7CwFlHJ6WrvdVYTgOHhodZqL-kq03i4ck4fuevhLwbivDy95nJcHH4t_zE2rV-ku8DVgU7VUHuQMhyVca0AUc96D3JdXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مراد ویسی:
خرازی برادر همسر مسعود خامنه‌ای افشا کرد مجتبی از استعفا های پیاپی پزشکیان خسته شده بشدت و در صورت تکرار اونو برکنار میکنه.
این اظهارات نشون میده جنگ قدرت بی سابقه توی باند های مختلف سیاسی امنیتی رژیم بالا گرفته.
بحران بدجور یقه جمهوری اسلامی رو گرفته.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69523" target="_blank">📅 16:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69522">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/800e043d01.mp4?token=cKT8qh4VVmjbUW7fhvuUdQDu7KhJlhCBTG31hoddCrRRWzSwtdcAukFh7agtQzYSNn6l8Mw-5cGVYskRxOAFgxDlcnah0pZRTu7aqrwmXgjN24-GGnXyG1TrPlgTfRom2qxax_j3mYieHtMZ0ID62wxsrnVTW0iUJ6DBNsQJz8XU7MuekM6m9QdW8LfhmNM65R_SvvqdEYB7ipt2y2A499-rwd8Hjb_lYv3uiPazO-4dyo4zv6e0kJGZsKtflLVxdBsQKwnEqmxnh-E1MDAWuWdPmG68tAds5SJLldZrvBlCekdkmNT7bY5jh_TBNjIoBt3sL1HGsVGTcvuTZZ_0NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/800e043d01.mp4?token=cKT8qh4VVmjbUW7fhvuUdQDu7KhJlhCBTG31hoddCrRRWzSwtdcAukFh7agtQzYSNn6l8Mw-5cGVYskRxOAFgxDlcnah0pZRTu7aqrwmXgjN24-GGnXyG1TrPlgTfRom2qxax_j3mYieHtMZ0ID62wxsrnVTW0iUJ6DBNsQJz8XU7MuekM6m9QdW8LfhmNM65R_SvvqdEYB7ipt2y2A499-rwd8Hjb_lYv3uiPazO-4dyo4zv6e0kJGZsKtflLVxdBsQKwnEqmxnh-E1MDAWuWdPmG68tAds5SJLldZrvBlCekdkmNT7bY5jh_TBNjIoBt3sL1HGsVGTcvuTZZ_0NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
محمدباقر خرازی درباره بمب اتم:
«در اقیانوس اطلس بمب بزنیم و سونامی ایجاد کنیم که موجش به سواحل آمریکا برسه!
تنها راه حل نجات ما ساخت بمب اتم و شلیک آن است!
«با اطلاع»! میگم ایناهایی که با بمب اتم مخالفت کردن اون دنیا در عذابند»
وقتی ازش پرسیدن که حاجی زاده گفته ما بهتر از بمب اتم رو داریم گفت: «جدی نگیرید این حرفها را»
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69522" target="_blank">📅 15:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69521">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IlO8nZAointt10VuQff1wOF-d7_t9-byKvpZ4zhgkE0r82XyUdPFKf5HGQd0obw-fcNFJNPlhF8VtwiomitChAjhGOE_yr_qCBYmUQ99N8yX2RSQBr-HRpmAs4hUTM_ZoCUZEmIncC51hqAQH8SE7jTWkRNkQSaJWzh_vsMUH1BIAsogAUyuDYC4kQe47zGGheHHNx5FSthEtmilmi2T24vlNB_Ad9emIKTK4iTae8ZGxcYRsqwndcRdROgzm2NEUoWw_Ah4ZySCxOYr-J2TGHl63uXluvI_sGXAB4Po5Q5iH2E-JD-IuXZrmxr0KiR8Iv3GGO1sOfbo8StwICAnCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
بلومبرگ:
ترامپ به ایران مهلت داده است تا سه‌شنبه با عمان در مورد تنگه هرمز به توافق برسد، در غیر این صورت با حملات هوایی ویرانگر به این کشور روبرو خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/69521" target="_blank">📅 14:59 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69520">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🇺🇸
🇶🇦
🇮🇷
سخنگوی وزارت خارجه قطر:
تلاش‌ها برای دستیابی به یک راه‌حل کوتاه‌مدت میان ایالات متحده و ایران در جریان است و متن توافق احتمالی نیز تدوین شده است.
این پیش‌نویس هم‌اکنون میان طرفین در حال تبادل و بررسی است، اما هنوز دستور کار مشخصی برای مذاکرات مستقیم میان آمریکا و ایران تعیین نشده است.
تمرکز دیپلماتیکِ فوری، حل‌وفصل تمام اختلافات عمده نیست، بلکه هدف، دستیابی به کاهش تنش در کوتاه‌مدت است که بتواند راه را برای ازسرگیری مذاکرات هموار سازد.
برای بازارها، این تحول سیگنالی مثبت محسوب می‌شود؛ چرا که هرگونه توافقی می‌تواند خطر تشدید درگیری‌های نظامی را کاهش دهد، از تنش‌ها در تنگه هرمز بکاهد و فشار بر بازار نفت را تعدیل کند.
با این حال، همچنان باید جانب احتیاط را رعایت کرد: اگرچه پیش‌نویسی وجود دارد، اما هنوز مشخص نیست که آیا واشنگتن و تهران هر دو آن را خواهند پذیرفت یا خیر.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/69520" target="_blank">📅 14:46 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69519">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnNe5kkRDBTG-RgMHqm6T9L6pFYeYWraAFvbMEiZMibJrN6TX6hvNGGo3Wga3SgFSTFSM1mIMoAt1-w7rawrXY7eNuKJLvxe7qryvPn7BAiaCJUM1ImpE8Sbe9sin9bypdUimilp4kpt1QXoLwL3lBJBKJAwj87_97HFQzUfCudikqUwYF5g9IIa5QyUJ0CUwzSNf3EIfCo_Y0NZP1l2PkZFkNS5Bj6cVP2RAum0su6pu-OvLf3hhKqEX1cikGcK4bo6z8vWqk95t08tkjRt4pmHtPFEgCcoCSSVjW_gU1MNs5ziyhP5G00QMzXU3dQC5P2ZkjfTm_ci18sA1BNhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
هیئت مدیره شهرک صنعتی شمس آباد:
دقایقی پیش یه مخزن گاز توی یه کارخونه منفجر شد و باعث صدای انفجار، دود و آتش سوزی شد.
هیچ حمله‌ای صورت نگرفته و مردم نگران نباشن.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69519" target="_blank">📅 13:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69518">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=TpdSlHskKJ24eLP331R3-RRPknuC12mlxvp2FQBKj4oqdpR-9VhDKoCAzD6VIjXlaz0uJBKEw5Jnh7DJraQKjq7CRzVWRk1QNLjXLxcT7agALC5s-zksuGzr1RMqwzzPpVeNusP55pZGU6U2gavncampIfyfY_XLxOt-AI3pLECc1_pgOf7WWdlEurEcMl0n-_2HBOpGnNjO3p3AOoykYBdLEXN_CYQ9GAZoMtmvH5IUC3Z6uv_5GauWxk4ID-tess0m6OJNM_W11uomrmoGpsQrw3qSw3eGrB_4kCSurErf9jBulB-pGVbBf6c9dj-DBgsG4_Z5eRp0QDZjDiwXbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8fbdc7b7.mp4?token=TpdSlHskKJ24eLP331R3-RRPknuC12mlxvp2FQBKj4oqdpR-9VhDKoCAzD6VIjXlaz0uJBKEw5Jnh7DJraQKjq7CRzVWRk1QNLjXLxcT7agALC5s-zksuGzr1RMqwzzPpVeNusP55pZGU6U2gavncampIfyfY_XLxOt-AI3pLECc1_pgOf7WWdlEurEcMl0n-_2HBOpGnNjO3p3AOoykYBdLEXN_CYQ9GAZoMtmvH5IUC3Z6uv_5GauWxk4ID-tess0m6OJNM_W11uomrmoGpsQrw3qSw3eGrB_4kCSurErf9jBulB-pGVbBf6c9dj-DBgsG4_Z5eRp0QDZjDiwXbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
تهران
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69518" target="_blank">📅 13:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69517">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">⏺
یک مقام ارشد ایرانی به رویترز:
طرح پیشنهادی تهران به عمان در خصوص تنگه هرمز، اختیار کامل بر تمامی تردد دریایی ورودی را به ایران واگذار می‌کند.
علاوه بر این، بر اساس سازوکار پیشنهادی، عمان تنها پس از اطلاع‌رسانی به مقامات ایرانی اجازه عبور به کشتی‌های خروجی را خواهد داد؛ امری که تضمین می‌کند تهران همچنان بر وضعیت نظارت داشته و امکان مداخله را حفظ کند.
این مقام ارشد اظهار داشت که بعید است ایران جایگزینی برای این توافق جهت بازگشایی تنگه هرمز را بپذیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69517" target="_blank">📅 13:33 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69516">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xrlf9nRA-5eiLbPa8ZXOay7wMFvEzwFFJoiLBrzBfCeLQaqSmI1adSSYklQEstUdSz6UASXndQafrRRWmKsICpkvD3QKHfKeZVOJLZHYtsPDM_fs4S5C9ds4SYofcBSigiulHTV8iHNHSHb5TxIVQwSuWUgs4xL_hmnke6VR5iGsh1cdd8_ey2MvYSMARrrf7LnzEU0t-4aOc5L6hKhJKmhMiq63jmbkYVa2GJg8yGglFHgTmT2lLNqnHK3H45SKYoI4hYK2uWh-vuht53ZmNtRvzWxpvp14wwJsaSGqsIuUbef_BiWBWpWQomQ_Js6yHi0yDmR2HQz7nhsxayIf5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/69516" target="_blank">📅 13:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69512">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EIv1wRQaFuUi-sA8_TtH-Kp1OWyDI-FYpZiI7imXeYvLNwmKZpL647VHb-b1wk6_dgNNRcxzQoeuN6u0zr0O-nDHplo7K9q8mBMeiv2dCJ6K6J7ggQFQ1Nrnuiv_tSc_J3Ef83EG2N0ODyKbEh8T1bls582OKm53Ty7LD8uqtRzrTvFiyVfULxeq_D-2GaFrbJ5OMdCsok2Vz4_vR97kI2aUacNg3fuAXkp9woIDZSo5iqh-wWhwhe-DI2rFE5W9ZJnTBHH235dGpByXx3O463qX0DtKkTQGqshgXCPtdGuYMO97-KFDcqsQulUlhob2v4w6dFubOmbh36Z71mJ26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GT1WbfQvAcho0xs-JrRpajkcB4JuhddSp9l3hrrVTOHc6licJeNCW19yjZtqkt-QHpV1TJdLUUgiHlObrkKX8oApe80ZpL1k3vI3MUALOFngM7PDs-P4shNmSF22TTZ6NF_eSgrKm0JjhGBp8yCHebrrR-NAEbK7lBpGuS6QxhHi1jm0BDNgNZF_zE63vLPPrAgVf_EBJybM6ofxb5erYroiHTra8cnPWK72mVGwmNrkG-re50FGEeI16IfQBSUYp7DFwBIwvRJ98IFHsKVdwN1j26wLLsYgaglr23yl2fmUa9Toohn6LPrbEn6zpvH2FoxDDaSXOO6bwNXMwBbKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbxw0Tdbg9LC4eOLNgK7xP8W8EHxXznKTL-9F57fOvuVZfCbmPCRcp1blsJWgJSgvjs1dMAWvnsdm2i33X38ECGACz3QzZgVvSaZh5LTWTp_UgqlQe9QxajSP_CW1yjlbidlqJiYxeWE9EpaWvfIoUhCQofdlM2xu-hoYRP6l39abBlHEQCp7KNoo-Lph-uq2VN-7C6EyM7sUQg-d31jOEjkbwqlETB4jW2ocRlkTKpgAE-orptl7rzOX_t3pkAIcs6V7DA5s4f5QMlRb7xX9ZxY2SN4Ww6lmh6BddDQyvzQ4fLnOA9rL0SR69H3QvYvf8LH-Uvjt2jK_fqLnBuQug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mMUq-tsg_X8aypGi6A2nSNFp-zNVpC_BHcEkzU-yDCZq_IdJINIidr1-5IeRnYaBrXcC8SHolOAs4roSn5LRnz721jL20mYzfuX5vmFw7ZbXQhjz67MlGJqKaXpHSPPVbKPyqWB9Gs0WV7EKkn1YoagGnBljYhPl-SuNmsD6O75HcZMGil0M5PQ50xHqZF2-vpkxxIyTmGaB4IAgPGmo5fBGfqQIahquw42rc1q0cI9GGQ2angIxEMi7pySTI5kScbxA9ozIoi9gpaMFgnyhLeS85jGLZOTL80uqRWbdBx71VMGkqle8HPFojkkz8a2kVoqVPruB93UOG61UG-Yq0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
شهرک صنعتی شمس‌آباد
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69512" target="_blank">📅 13:21 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=JL16IJxtBGIAp_HZQGPkb67nQb75X7k7hxQAOdqZeexa-NKoB6-hlzbH1ZJVLvHqeHclpQXAT9mxt-GjsUt9v3X89kes7Ry7voCBNCspJ7dCmDjsYrq-wjnlgjH80qrFK_gDpI-M-uBTNk8VrdrTJS4thfaEQLbTEWyrWH5r7WV0wQLHGmHGAV9ShcNyqQoHtU17o4XkIWvzA3wKnlhQCU3qXScx6UQ_YSNS1YGUpHLsyR_LaEnrOYH4f6MyiJfzo7khBj-zn3akOcBhJ2AnM4b1xbqg-HyQiMNyp91Ut9RYGkAz0ToexYSbgjV2iFdqCTwD8fnADZNlsJLUc5vZKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ecbf36384.mp4?token=JL16IJxtBGIAp_HZQGPkb67nQb75X7k7hxQAOdqZeexa-NKoB6-hlzbH1ZJVLvHqeHclpQXAT9mxt-GjsUt9v3X89kes7Ry7voCBNCspJ7dCmDjsYrq-wjnlgjH80qrFK_gDpI-M-uBTNk8VrdrTJS4thfaEQLbTEWyrWH5r7WV0wQLHGmHGAV9ShcNyqQoHtU17o4XkIWvzA3wKnlhQCU3qXScx6UQ_YSNS1YGUpHLsyR_LaEnrOYH4f6MyiJfzo7khBj-zn3akOcBhJ2AnM4b1xbqg-HyQiMNyp91Ut9RYGkAz0ToexYSbgjV2iFdqCTwD8fnADZNlsJLUc5vZKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
ستون دود در شهرک صنعتی شمس آباد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/69511" target="_blank">📅 13:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69510">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
گزارش های اولیه از انفجار در شهرک صنعتی شمس‌آباد فشافویه تهران
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69510" target="_blank">📅 13:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69509">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=oJIr01x79AJhx5m82A5H_oiWlz7L2foVJk4V8ofoajrSH7DVHpBm3nQ6akCaPvkH9xdtzkftTgYcpsdaQlVAmyIOrCkXFNJGJudgOkVStkYjsJyw-7Y32umu66RqrPCxz7Av_cLpafLtGBiLe8fcYqpYQ-gOG5zurbvo98WZdaDVQvC4vKmuuA5qo2jh0GWo3gTr7fqfn-VeXNQdtlEqWCYFBG2l98DV3EtQ6qWtmROjL4uASmzH-Xr3VwELGacAzHMZHddJoYXScHcj8bd9Xo48mrw4RTAiIY1CQuXFRlDPQCmGUVXmyL7QSmuqvphVjS7NidkAiv3Sy7nmTiUbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dfb1d4db65.mp4?token=oJIr01x79AJhx5m82A5H_oiWlz7L2foVJk4V8ofoajrSH7DVHpBm3nQ6akCaPvkH9xdtzkftTgYcpsdaQlVAmyIOrCkXFNJGJudgOkVStkYjsJyw-7Y32umu66RqrPCxz7Av_cLpafLtGBiLe8fcYqpYQ-gOG5zurbvo98WZdaDVQvC4vKmuuA5qo2jh0GWo3gTr7fqfn-VeXNQdtlEqWCYFBG2l98DV3EtQ6qWtmROjL4uASmzH-Xr3VwELGacAzHMZHddJoYXScHcj8bd9Xo48mrw4RTAiIY1CQuXFRlDPQCmGUVXmyL7QSmuqvphVjS7NidkAiv3Sy7nmTiUbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فرودگاه رامون ایلات اسرائیل، پر شده از هواپیماهای سوخت‌رسان آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69509" target="_blank">📅 12:34 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69508">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=QQj6zRgUnKOY4yS_a4t8A_CJvspFQ3fzqvjoXXEHO-a4DH6fFh9XjXZO5O3Z313JHJMfN0jypD7toSqqcxGf05D3y7Up8vKHhI5LdsxZHkq0pzWqGIDR63uGVUyCQam11GGIEOP8hDz5PUpVaxGD5dCEw8F011cpJM2C_FcyEb-jnZzMSMFjgHL4O_5YrGuj3n4ecJcTpa-OttvPYg2IEwYq1DbFMR-hqDwt1-I-A6XAIQ03fpab3vD_kxbp1Qjx8p7yT34OX-HH-4v6-xN3RA3PymeajyyDXg-28NEwP8DvBV9xw9rheP43QcCq6Sq-M2dmy3IU9idalCxd3DGzGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ca3c95000.mp4?token=QQj6zRgUnKOY4yS_a4t8A_CJvspFQ3fzqvjoXXEHO-a4DH6fFh9XjXZO5O3Z313JHJMfN0jypD7toSqqcxGf05D3y7Up8vKHhI5LdsxZHkq0pzWqGIDR63uGVUyCQam11GGIEOP8hDz5PUpVaxGD5dCEw8F011cpJM2C_FcyEb-jnZzMSMFjgHL4O_5YrGuj3n4ecJcTpa-OttvPYg2IEwYq1DbFMR-hqDwt1-I-A6XAIQ03fpab3vD_kxbp1Qjx8p7yT34OX-HH-4v6-xN3RA3PymeajyyDXg-28NEwP8DvBV9xw9rheP43QcCq6Sq-M2dmy3IU9idalCxd3DGzGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توی روسیه بدین شکل یهو یک پهباد اوکراینی اومد خورد وسط مردم لب ساحل و 6 نفر کشته و بیش از 40 نفر زخمی شدن
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/69508" target="_blank">📅 11:54 · 13 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
