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
<img src="https://cdn4.telesco.pe/file/KGnE1t2xKdokcPy29rEPDZdGCJn6q0-XFabDxpFG2aC6HQqM3vCFGSXfwkza5tbNNxQG2nRFEcFscpWwkNqWVc7w1YPbb3xseiIZfsjCaxXwOJCc_BCg_7ozW62QhibYWMm7eR9HmjX6odoOA_oGagmTV4P_qVO3PJf5s2cVmxzqP6vokwDtfhauWvDVSMV_ePJQ40nbuPnVotSTYS1kMJpXl--OjAs4E6T3PXuqByGqKfy1dD9dbI8_75UZQUwSxHAeib8S29UpBcxnr0yljHEOezaEusCaDT1uUGFreSd78QuA1o7lfeZNeKEQd8p8eZhHVFp8G6wF_h6y_-53nw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 186K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-19 22:25:00</div>
<hr>

<div class="tg-post" id="msg-67748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ad131e48f.mp4?token=U2IoC9J0w9VYyIMvBqheL51JrUCgnvtX5sYvyhUJSE63SQxkrToN8zb0KJiK41zIjNDBwnxUNRa17qxDmmWZv7HJwF6QQRR4PYORe3dFH5RJGt0833Fj6OUEBFbCCWRwtDxbW8bbu6aBtImj40uzMGBQyuJqDVSjXvf8SbWgpGHXmdtHRdHb58LtdDeiNcUeEOY-QKDhGdr0neWamPiIRN5aRF73lWmyT5kCYseinl2iLhq7C1OTBWINgN-R63gb4P3PqSooc6vayra73B3PIzBm0apmELCG6rSQSBSa9Ujm0mRH4J6djdK0M3WGvKrSbLuMRNv6X2OT95_AVw7rzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رونالد ریگان چهلمین رئیس جمهور ایالات متحده آمریکا:
در این سخنرانی، ریگان با یک روایت طنزآمیز، دیدگاه خود درباره نقش دولت و مسئولیت فردی را بیان می‌کند؛ روایتی که سال‌هاست در مباحث سیاسی از آن یاد می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 2.95K · <a href="https://t.me/news_hut/67748" target="_blank">📅 22:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXb6QQGwU4YyxWrG_0PGLFXwU1i1QqgwksNtCStxLs-nE88Nw2wFxC3DE8UFMJNQGN__Xo7mhSTmfSLh-OvNFVuJUm4U2W7NZQRINMPVRR-FEYkuAWC7-WGEYRy51ZFEB_zjwaZX_Ampl3jza5YbjkwTDo2QfwqR1_AY8t6qcxmSHWS9V1_NM0qedeMn8z2szRa1XBKn54XUeV3bIyVkBwbhm7fOrsJOP7GmNU8Vm61WirsWQDQpBFhdpM6sNQN76nvMDyY_CicuNIR64gIQ7ngMa7_BC13xQ1irQ44-6lSl-n4C2OrTe0mBwi8kF-NEt4AQTqPZd7pht4AopZx3xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اسرائیل هیوم: آمریکا و اسرائیل گزینه‌های براندازی جمهوری اسلامی را بررسی می‌کنند
روزنامه اسرائیل هیوم در گزارشی به نقل از منابع دیپلماتیک منطقه‌ای و غربی مدعی شد که ایالات متحده، اسرائیل و برخی کشورهای منطقه در حال بررسی راهکارهایی برای تضعیف و در نهایت براندازی جمهوری اسلامی هستند.
این گزارش همچنین ادعا می‌کند که در پی تشدید اختلافات داخلی در ایران، مسعود پزشکیان، رئیس‌جمهور، و عباس عراقچی، وزیر امور خارجه، با فشار فزاینده جریان‌های تندرو و فرماندهان سپاه پاسداران روبه‌رو شده‌اند و حتی احتمال کنار گذاشته شدن دولت پزشکیان مطرح شده است.
اسرائیل هیوم به نقل از منابع خود مدعی شده است که عباس عراقچی در تماس با میانجی‌ها اعلام کرده دولت ایران نتوانسته موافقت سپاه با مفاد تفاهم با آمریکا و توقف حملات به کشتی‌ها در تنگه هرمز را جلب کند.
این روزنامه همچنین مدعی است که یکی از گزینه‌های مورد بررسی واشینگتن و تل‌آویو، تشدید دوباره فشارهای اقتصادی و بازگرداندن کامل تحریم‌ها با هدف افزایش فشار بر رژیم ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/news_hut/67747" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67746">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t7q2YCcxvNz_Y7KJ48KJNysT7jB8z-GVSDxsaj-W6wO65DG58YifBhEKCoFhFBsE2yzSFGPNkWi-WAWA0iNPnPAo1NJP6YqmCfzjl3-SkofS_8wVPoBWMmzyeGWE-KOTK5NRSO_txYn-itZ31paHafTNeLe-K1ChXVR9KMdr27OkLiAKvNjS2PPoXQ2CRYPHsz0Jic1vGdRkhBAzLqube6Hu5vtogB3Z9R0vX-0Kd76ij__OawxgsWgX81EHX3rhynyf5BtXcxj5NCY6_RGvYhrFLkoZ2K5gPFkXKCe4kYLzeXYHS5jEcSrudhexgxbT2TsiQvFkpgsYymHqXDD3WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
باراک راوید:
بر اساس گفته‌های یک دیپلمات آگاه از این سفر، مذاکره‌کنندگان قطری با هماهنگی ایالات متحده، به ایران سفر کرده‌اند تا با مقامات ایرانی دیدار کنند و تلاش کنند تا تنش‌ها را کاهش داده و شرایط را برای از سرگیری مذاکرات فراهم کنند.
این دیپلمات گفت که جلسات بین مقامات قطری و ایرانی در تهران همچنان در حال برگزاری است، "اما واضح است که هر دو طرف تمایل دارند به توافق‌نامه اولیه بازگردند."
@News_Hut</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/news_hut/67746" target="_blank">📅 20:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CS_TQaagjmgZ74AAKxBmXwXBOY_B9XsQSxFT-UjW4FPtLHToOLfKZFewi-1ZCEuHfpR0UHhFeAb9CJ-Hp8GLUGin_Wibbtqy1Tl6euJhzXNnDUV2vJ_YBpdENhXkXO8MES0W1E9Y89z0ocipwMHelmy77xBBs2xzxFcy3hP33m8SRyoaALyoSZE9hQsxINzar551KJafFvz9PwHVSkGjiGqDNxtzG9pqOcLXbeaIWc-zE_888v_jQbCV8fr7GGErTVbuaUc_6w5yhDcGVle4K76hQxShcpEn1mhoRO4Ltun92_VIjP7mWxdJKs30dpM0sfDXOOkvHJJF8TEOxeopUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ به «نیویورک پست» گفت که دستوراتی صادر کرده است مبنی بر اینکه اگر ایران در ترور او موفق شود، ایالات متحده باید «به‌معنای واقعی کلمه، آن‌ها را چنان بمباران کند که هرگز پیش از این ندیده باشند.» او افزود که «مدت‌هاست» نفر اولِ فهرست ترور ایران بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67745" target="_blank">📅 20:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bdFEqDwNTxZs2Ii58BzB9q8svz6SgVxULERrn4RA2OTpE8kVst5OljdjfBTAKBu2e1dRED9lLpX27iJDZNH1JpZUCn-KrhTVpr2dR-eJ-zTk9gPDwcJeBPWgelB2PPE_syc2Nmp2gkLcAhVeff212XLJguME0kiao6Xy53Na7pmBGBEziwBdkgCR5z40HY_qbskEFpSon698QroammssZv9ukNCIm50_pEuaX5BRchBEeY7smvDTHf7MasjPyVcYLrotSZGa3QwEU4tccN7y-B1HvB00k_8akO6Hf05xSY_dFbyL2YTBlOt5HfWnuznBMkEPgrdUhh1YskUfvdox6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مرندی از اعضای نزدیک به تیم مذاکره‌کننده:
ترامپ و خبرگزاری آکسیوس را نادیده بگیرید. هیچ مذاکره‌ای تا زمانی که دولت ترامپ به تعهدات خود عمل نکند، صورت نخواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67744" target="_blank">📅 19:44 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
آکسیوس:
پیش‌بینی می‌شود که ایالات متحده و ایران هفته آینده دور دیگری از مذاکرات را برگزار کنند، احتمالاً در سوئیس.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67743" target="_blank">📅 19:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=ZpuYXEKszUxizkN-WWYbzHue7hbIX2lXU3GAQmpu2IQMiPOlSf1442tKMsmS3ZA6GJS1F0HYzw2DE31D5j6ynCTkRdS8HqojREnCJHNuLjAik7-j1eQysAbdvz_tZRZ1DP6HyxNzEYRZ3XkTY0GTfpRn2xUx9Q-znnmSl7iEDfuegT1m6nwoNgS9tzUeGnjNjlHZkEInVCPDtn5RZL_pBTmc_eQSgcHNjvcO-wCn4grwaPNvSSVQygjqzefZoBi9ndwUoNdA76s_I20vCxrkElsArwdERISnTCNNPSSycOufcHRY8QWRwp5angQblej-y5gDqc4NN7EGxNk8X12brg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/258d1105e3.mp4?token=ZpuYXEKszUxizkN-WWYbzHue7hbIX2lXU3GAQmpu2IQMiPOlSf1442tKMsmS3ZA6GJS1F0HYzw2DE31D5j6ynCTkRdS8HqojREnCJHNuLjAik7-j1eQysAbdvz_tZRZ1DP6HyxNzEYRZ3XkTY0GTfpRn2xUx9Q-znnmSl7iEDfuegT1m6nwoNgS9tzUeGnjNjlHZkEInVCPDtn5RZL_pBTmc_eQSgcHNjvcO-wCn4grwaPNvSSVQygjqzefZoBi9ndwUoNdA76s_I20vCxrkElsArwdERISnTCNNPSSycOufcHRY8QWRwp5angQblej-y5gDqc4NN7EGxNk8X12brg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
آتش‌سوزی گسترده در مجموعه اکسین پلدختر در استان لرستان
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67742" target="_blank">📅 19:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuHU0bQPTXx84WC3vxRpgMZHTs6woLF85PuswU3Hxo4pF-IFY9AcyPPQHaqfMU6HckEGoKHKS5VsRfwvhl-Vf81agxvmuUdAoGeKvOqqFn5FXwHV5wrVj8luNBFt7nxEMBzTlHsiDmhPMaEsvM4eebYL7NO1twLcM1lHV9Q3t_NDARYDBymOrxNlX4E9Ez0-tlf_n5ghRPzwUvwwNcHtBfqORvSn5iX0ZXQp5iVGZIa4CvfKWQ3RmCjcIGV2gGX0Ne98h9NncHOec9H1EbCYE_kByY2eridc_HxjW3oLATs5zHnSMkl30rARMlowxYFprStnX1FIrzaVFcIu27BKyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
انفجار در پالایشگاه نفت پلدختر در استان لرستان.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/67741" target="_blank">📅 19:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67740">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUsjWXQG5QPbV5o-yPfic5CkmmhYvqUjOvvNramn5dh6wnzC0nLbrvfysb6qPv3lqXdyStrCgIz0FwR2fHRSnl3H399iTYbmD9LaIuMeM3o8PvGrB9Fz6DuLVE-XujUpeUGZMAFuJ8ZjB64M0IKXf_HoyFUTCrv2Zloe1SvVWK0w24aee3yCCK5-gBD17SqmOL6NFMp37YzZ0i2tOo4C9tkg1slQvA1F0uV2Mv8Eu5y_yplWWHVdmbyPyaSeLXlNJKyQBjj55yChmRdhAe-PRTy_wMXCgyoeKXR2NQg5wo4InipSJadSGnzfUC2l_fUpcVbxukxcFth-hjLDE_CSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بلند شدن دود در کنارک پس از وقوع دو انفجار
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67740" target="_blank">📅 19:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=hFngk352zfmB2YNVoROthRcEMGbEoWLxBO6lxyCv3JCKWHoO3lfpSZ_VCyb6wuq7SJAgdooHay15MC-Jf9K8HriygFT1yhlx-OEVAEFU_ZqFLTMgs3fwDrTrkj8hf8EwhI7ge5rrE9DVphHug2Im_GTSGLbwBoh3rPqSez29jScZJbkw-NRMFQTKggNnWrbuEzFVry3EwJTcpF66zf3mULUs2UDGnxJ5Y0yRnUcJcEGPJdBphkI58JMGU0t-e5MTozVO9eTRjK22FdCzq_YM1qOwEjpfWUOn5gfThX9DvW99_mkAClzRBJuL9Djxj35guBeIquSGXcLGJyUPAp77RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d335d453d.mp4?token=hFngk352zfmB2YNVoROthRcEMGbEoWLxBO6lxyCv3JCKWHoO3lfpSZ_VCyb6wuq7SJAgdooHay15MC-Jf9K8HriygFT1yhlx-OEVAEFU_ZqFLTMgs3fwDrTrkj8hf8EwhI7ge5rrE9DVphHug2Im_GTSGLbwBoh3rPqSez29jScZJbkw-NRMFQTKggNnWrbuEzFVry3EwJTcpF66zf3mULUs2UDGnxJ5Y0yRnUcJcEGPJdBphkI58JMGU0t-e5MTozVO9eTRjK22FdCzq_YM1qOwEjpfWUOn5gfThX9DvW99_mkAClzRBJuL9Djxj35guBeIquSGXcLGJyUPAp77RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مجری صداسیما:
اگه خمینی و خامنه‌ای، زمان امام‌ها بودن، امام حسین شهید نمیشد، امام علی حاکم میشد و امام حسن هم صلح نمی‌کرد.
پیامبر خودش گفته؛ من مشتاق دیدن اینا بودم و حسرت دیدار اینارو داشتم
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67739" target="_blank">📅 18:52 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67738">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arjnpsJ5xnsaeMh8VZUga0qPWjna1lZNgCGA3KteIt383c0K0UIJ468YE6bjuCi1sxV8-wuhe-W3IJRSSZTuJl8WDExrcaY7UKQf7W4vkzzyFW1PUsg3z3kQvGjxDd5hjvzDwLkHbgzH3uDvkQO8DIgnCithsrwpjxtDQFfW0R9YxpHw8AZRKcERDYm-pJmnVZQktNmF_Pgt7wOReHdPCZxplea_ppnICoSUYWQICK_DYCt3CLz750uNc0kkDgWnm6ckugaSxhDsgDWLAe7NJjKtJBQ7EmtIb9FcZS87aGVxpGC3VkW9VFj3q5SrjHsA9FkTWYQTizxlrcLuV_AjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران با ما تماس گرفت و خواستار ادامه "مذاکرات" شد. ما به این درخواست موافقت کردیم، اما ایالات متحده به طور واضح به آنها اعلام کرد که آتش‌بس به پایان رسیده است. از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67738" target="_blank">📅 18:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67737">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FU9Sctj167KWL5BeATIl-nk7KxxONOc1wIu5Oev-J3wArbgw7XHrar8bg4kzNYUhKFRV5onWtVYYJcfMlAx-CZiHdA3ty9P_rsZKU2rq8sUbA1wUPzg-TN66JvCOCfnyhIXq4Hwby9Bcnf9S6Jg1-PTZVn9yWa3LF1k7Cac94n8kmuEv4YxX6E8uRN1DfhaJyFkMcKnrGO_lH98agkztuaZ1FvXMconYlpgYLAAnfkmzUnEIabPM3eKTEU0h6wvKRAGwd3wPfqPCyjlFg2SPz3gqaUfARiTnkXfB8z3QoH7v3IncCX8vtvyD9TlYbH2tBGB4yISCul1ayCwzmY_oQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نیروی دریایی ایالات متحده امروز حضور قابل توجهی در خلیج عمان دارد. یک ناو هواپیمابر و اسکورت آن (حداقل 3 ناو جنگی و یک تانکر سوخت) امروز در فاصله کمتر از 300 کیلومتر از سواحل ایران مشاهده شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67737" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67736">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=kEv1J_Iq_XvCiUvR9CWkN4JEXvbkxCZo7LgICvKLa-DEZ3BdhiLupYDSkEavvQ77HjPEKXbnhzIE6arKHOIRzuZyE5RPQiUG8V2VLApgiOgWLvpoVXgPeEuICvp9WWdcSp0sZBMyJYMN8kzLVkgs8yA55v59V_R87yFt6OKHSjr0gKnDkTcUjbHBfqMrhaOPqUNYLVhe22Nm57dzzbTa33rAq10WtpB2HAY2xkriRX9aM37X3rCK_zgnbbhRAHejTlvqCw_CJMTf2t8J_3tzV1Hwx9xerm0qnSk7zT0wilOOq-kBCO-zmnULhkbynrSr7ihLiSfy0VTRiGI_uesRTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be0edc864f.mp4?token=kEv1J_Iq_XvCiUvR9CWkN4JEXvbkxCZo7LgICvKLa-DEZ3BdhiLupYDSkEavvQ77HjPEKXbnhzIE6arKHOIRzuZyE5RPQiUG8V2VLApgiOgWLvpoVXgPeEuICvp9WWdcSp0sZBMyJYMN8kzLVkgs8yA55v59V_R87yFt6OKHSjr0gKnDkTcUjbHBfqMrhaOPqUNYLVhe22Nm57dzzbTa33rAq10WtpB2HAY2xkriRX9aM37X3rCK_zgnbbhRAHejTlvqCw_CJMTf2t8J_3tzV1Hwx9xerm0qnSk7zT0wilOOq-kBCO-zmnULhkbynrSr7ihLiSfy0VTRiGI_uesRTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ویدیو‌ ای از صحبت های چند روز اخیر ترامپ که در حال وایرال شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/67736" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67735">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">MelBet2.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/67735" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن MelBet
🔄
🎁
کد هدیه 100 دلاری:
Sport100
🤝
اسپانسر رسمی جام جهانی
🔵
کاملترین برنامه موبایل
☄️
صرافی معتبر
🤖
ربات راهنما
🇮🇷
برای تغییر زبان برنامه، زبان موبایل خود را تغییر دهید.
✅
ورود به اپلیکیشن بدون فیلترشکن</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67735" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67734">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LobtDc_3YShnkjUz0Zp-1Hz_gxTikobKfg8bpdfkdlkzwhHaBF-2S7SlU0Ci8Xbjmld_PzsFTSVmewOXBBqsoTtHulgZrMQwmJEzdbau8VHuYC-Nx0-KOeEfvWdOJZ8tZtJ6CT2ybk3tPNh92pVl-eWLaaBeem9V8NbpyzeJHPIUa7Jyedj0keEesKNd3Obxg8Kj3If5jDjwhiC6JM88GQqnJ4pr-boWAqBwMcI5hBL5MqdliBcW82sbkuTTmhFOnxbn03amBg4iVQq5Pv-eTphJY5PSUG6tZearYQjaV3IE8pmAhi9ZMiKKBR0gH6EIHmcLLmjj-rryi589k4ArKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
55 درصد از علاقه‌مندان به فوتبال، فقط 4 سال یکبار شرط میبندن!
حالا چرا جام جهانی
❓
خیلی از نتایج تابلو و قابل حدسه
💯
مافیا که کارش دستکاری کردن نتایجه، زورش به جام‌جهانی نمیرسه و نتایج واقعیه
👀
به دلیل تعداد زیاد بازی ها، دستت بازه و کنترل ریسک و سرمایه آسونه!
🔽
🔼
💡
کافیه یه سایت معتبر پیدا کنی که شارژ کردنش آسون باشه و بدونی پولت امن میمونه، MelBet اسپانسر رسمی جام جهانی، همونیه که دنبالشی!
برای ورود به سایت فیلترشکن خود را خاموش کنید
🆕
Link
🔜
MelBet1.net
✅
🆕
Link
🔜
MelBet1.net
✅</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67734" target="_blank">📅 17:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67733">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cIYW5qFJ7vC-F0n3c9Tx12DobABqlS2B-LctiiH_TY2Ls-3J_i2qA2N73-BDwro92DHCuMOEAl_oHQRKfkyBAR-g2K3bb5j5VkRKAXgxcRQIyzjWF80jNc8OUrO740Eh-mPUkAOzL_Ym18o0WOZrQvu7IYGtx28eOFsZzdUIZSv_qxW0C17shGSdBbxqX2gQpRA5URubh_HdYrp8D4jPNOXygHZMBwTeZt2FKwTfSQt76rKuv60x-h7ddFvXUXqEc1n7nOwhVFfr7OEaEWQMxqoBdWAFnq189OceT_g63c3YV7FPRVN67JIEARMCvJPVKN8XpM4lqNK6rWZVC7Gmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3d6c6e5dc.mp4?token=cIYW5qFJ7vC-F0n3c9Tx12DobABqlS2B-LctiiH_TY2Ls-3J_i2qA2N73-BDwro92DHCuMOEAl_oHQRKfkyBAR-g2K3bb5j5VkRKAXgxcRQIyzjWF80jNc8OUrO740Eh-mPUkAOzL_Ym18o0WOZrQvu7IYGtx28eOFsZzdUIZSv_qxW0C17shGSdBbxqX2gQpRA5URubh_HdYrp8D4jPNOXygHZMBwTeZt2FKwTfSQt76rKuv60x-h7ddFvXUXqEc1n7nOwhVFfr7OEaEWQMxqoBdWAFnq189OceT_g63c3YV7FPRVN67JIEARMCvJPVKN8XpM4lqNK6rWZVC7Gmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
🇮🇷
علی خامنه‌ای،22مرداد1397:
به طور خلاصه در دو کلمه به ملت ایران
بگویم: جنگ نخواهد شد و مذاکره نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67733" target="_blank">📅 17:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67732">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiFDIx6SIWVbqqTWdPlEuWDK1EgV9eIIKw5LqkDp1l4UoE0vmb06414c4JIwNcqYOzEu0IEtEiZKyISeI0Ti6qwoDzlI7XhN6Hh_UfrHmGofkqYsVcHdCtSjfAl1fVGZNZ1vxq88BKbDiXhPOmoOfStHm2TIILRtvYOB3GVD7dQuVcfknJf6DoCrZJQ7jFOauv9dfuTFlX6ktm-9nA8QecvsVzVHn9ywBmpZIsRw3ryjUH8ZFlncEG01Hh3JMyvP5fR8G2RVFhryBqtrpe4o7iihLeCjKFOsNuFcUVPGKBNxhPEgHo-a7qVy6f9GczmB5CGuiMQu1dHgX36v63GHkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کارولین لیویت سخنگوی کاخ سفید :
جوون‌های نسل زِد که از وضعیت اقتصادی و زندگی در آمریکا گلایه دارن رو بفرستید ایران خیلی زود قدر آمریکا رو میدونن و زود برمیگردن
😔
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67732" target="_blank">📅 16:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY1i3-zYKbvImSsuNGFBGq8AKs_W3ir6QzGRuRbBdHImZghylSoat-5jMd7IIb7sRnOeqK5nt5sy7MiJjpnYHHEZt5NuvHDkoqpo7Y-7EDSgsMzzn478Pq2VQzv-Uc4soIIvRPuNtxg55Jcag5z4bWtBzu1uaKbgHGdtJ7-h5AR0KBV4XRFWL6H5DhSgBbB1XGvbldcKLNoXEZa-daIueYZf-XJa_c1iwh7hAcD_hgLotEXMsJgg-SDTsrShKBIcEICbNICejQo1ad2hVi3AIcEo587kNv9hxoZm3X8VAWmOD7X4NwFI8BGnFQ6A50i3muXQungJKNB3vcsmkJpBdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1372691bce.mp4?token=faGyJtVr2kcNS31pCeGOZMazyTj4e3AUvVIorbcc_iQ5rJNjOxrzvF5XxMbhj6FghfidHCMgWzBg86KXYpjJP6wji2_ozuL2p71E2aG_sF0s_s77Qd4Wmj62JBlt6Gelw4sTTu30BZ6lrLhyVVi7p3B0ZVw1_EcXN4x5zNmI6-s5i2fyvGJRqvrMUhsRRl87Atu9zPRh_JhRKoVCjL3u2JIXczN6SuMMfsRi_xZusfIu3Uh6CnfAZy_o7AiMoThfRdMWitlRiONu64XiM6amh7sEAAIowIUDcum6yZFi5pZQJmZo1pz0-fSLgFreVZGLPfXRladVNVnx66XACVuScQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گویا دیشب تندرو ها داشتن بر علیه تیم مذاکره‌کننده شعار«مذاکره با دشمن، خیانت است به میهن» میدادن که مهدی رسولی مداح حکومتی صداشون رو قطع میکنه و میگه بگید«حیدر،حیدر».
این حرکتش باعث واکنش تندرو ها توی فضای مجازی شده و گرفتن روش
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67730" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4niFslqZE0AoBZJ-dmltWAWiO_SCAmrBELRcjebG9bGaF0oA6OXrYPFo-CNaN78SNNUV8c84axNMDp8PdUqqIlUpaq8INLezNLXwJBFw_ohvxcsTnpeaq6l2ptEIG-ZbSrZR73fovMYw0TDb-GdIFxLbqSwgCbhhmAsgVqglFUT6790J0kwhS7nakj9QQRevpdvLWmogh4_W-q3xJ4A6w-ztFWjF6_wXWv72lcE4Vcf15UfRetSzPWYzfXMFGGyq46nRXJL2CRNxgyxv6-1o-L5LPE-v0CcmASgrQfFaRTihQ2NK36FSRRW6SJ9tBCNyCrsOBxqew5BX8wrwnWzug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فرماندهی مرکزی ایالات متحده(سنتکام):
❌
ادعا: رسانه‌های دولتی ایران ادعا می‌کنند که عبور از تنگه هرمز تنها از طریق مسیرهایی که توسط ایران تعیین شده‌اند، مجاز است.
✅
واقعیت: ایران کنترل تنگه هرمز را در دست ندارد. از اوایل ماه مه، نیروهای آمریکایی به تسهیل عبور موفقیت‌آمیز بیش از 800 کشتی تجاری و 380 میلیون بشکه نفت خام از طریق این مسیر حیاتی تجاری بین‌المللی کمک کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67729" target="_blank">📅 14:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67728">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GSINzXHWjiXBv9HILfg3vtgiwshkCcL90_R-gn5gS-vQije_M05oDf8vW25PoIQh-CyVJS709L-rusGHbyKOmdeKI3ttAyv8245QQ9LH52NR7DewseTjEf81RP1Qw3TbVMMR1uLlpwT0QEBn2SgqXDXhtocFQVPvOQ1exNWiNc7IbpeE0OnJCGjVJJgRnGKcRONjyhQD_5DB-0zgI_X19Exwe7cMlBM0_BdIC7OKZU4wE6Wr2BP62ZsAaU_3ZHR9-eZj4HqVOFeIUNDAnZB6yrdVky7pr3dNNRDHXO9I4j3_r96yhrhx08u01a51JazoueI4-MVfMwdnbW7n1LffDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام سازمان سنجش، رسما و شرعا امتحانات دانش آموزا، بدون هیچگونه تغییری و طبق برنامه، از ۲۱ تیر ماه آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67728" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67727">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3590c95ce.mp4?token=XKMS7n3RBy0Ia0qIvarDvVVE4EtT2BmqgT3vR15ZgdaM3ma2NmgiBSQRjHCdMYD2E29hRbzYR0dBKRH1tryjkL2czX9QquWDfbLyKtYAgBFkYP9ElJgKhnHJhStLas3Ax1Z3hNwc4LmR3sYQNUq7-rqZTNS0Jvos1-a-Hbj953ltIhfMtuQ7wAK4sYHYNk8dfIlZGdG4Yh7HqEDdYjeZLAPp2tT6UERl5f3v_o3d7ugLU0bBUiORmhGvKsMCWCQM-7LwcTpfyX3qDqUKYIYXNqXbkQIGAuikjWHoL2utkKfx2K29tMLfexvkOu0TszePONxJj_1wTQWbqffo6Qq1Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکسِ تتلو تو زگیل ابدی با یکی دعواش شد؛
پسره هم وسط برنامه خیلی جدی بهش گفت "
برو بابا یه ملت روت شاشیدن
..."
+ ستاره همون دختریه که تتلو تو ترکیه روش شاشید!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67727" target="_blank">📅 13:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67726">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FG5AouYG2vXMKMf7vor40dyfy-QAZxnqTo9KF-xFxQa8tvLHQxmtgUF80b47rdj7cZJEGnEgA72YjOf2oB3r74UnsGcZ5NscRMxOyPc598dKYnL2Hh8dOyeVMHj_2xp9CR6TLRd6wt06iE8Tj-RdBNZ_yTrS2dW06HdV8x2FOVATIoNWQvNIaFu-FKpyyGupbSmOqnUzmXBmRr72Eeapwh0XK7RACwj2Z-TZq7ILw-NClNuWjCGZZf2fafOzYpRFn5rl1_xjl9uY4TouGMdd_rBP4DNZUsEtmybUEelpNd_aTGAcGMFHVm5Si8hHPUSLYRzE9T9OEbfW9R9GumHIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
زیرنویس شبکه خبر:
آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67726" target="_blank">📅 12:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67725">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/606bce162e.mp4?token=MjMF8fACwKSr7-7xnwtjYzrcMhBATpXruoJrOFEsxvijebijVWyuNKXg8eCOwHFvvGJKf2DM226XS-KB3Nf6g-JMq9OtjhcnOAc1fesDS4N1UCo93RWXevC5rnOL6ea7RHZ9zpiTj7acNpuohf7BpURkcAdTFxwA6SdyJ-6tBbRIpEDSQU5gxKp6LNBgHTOWFSuOQ7IqUVzjuWb0Uh9JfJNys6bgnhQ4jzgB1Dhbkn1OL_69V7KabBBTdbI5ud8x_TgQY_TWET2-STXAR56_ShRiqbQ4JR2uUeIcV0kB5uNtnY6XYmtsSyjPCsSLG0bP46jmxWOs9uZ4WEPWTczjNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آمادگی مجری‌ صداوسیما برای ترور ترامپ؛
نگوزی‌ داداش.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67725" target="_blank">📅 11:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67724">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
⁉️
تسنیم:
مراسم ترحیم امام مجاهد شهید از سوی رهبر معظم انقلاب اسلامی حضرت ‌آیت‌الله سید مجتبی خامنه‌ای جمعه ۱۹ تیر پس از نماز مغرب و عشاء در شبستان امام خمینی (ره) حرم حضرت معصومه (س) برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67724" target="_blank">📅 10:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67723">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">‼️
یه ویدیویی از دعوای دوتا خانواده تو شمال که به صورت گروهی با هم درگیر میشن و همدیگه رو تا سرحد مرگ میزنن وایرال شده؛
حالا فکر می‌کنید دعوا سر چی بود؟
گویا یه خانواده داشتن از خیابون رد می‌شدن و هم‌زمان یه نفر هم با سگش از همون مسیر رد می‌شده.
یکی از افراد اون خانواده که از سگ می‌ترسیده، به سگ طرف مقابل یه لگد می‌زنه، بعدش دعوا انقدر بالا می‌گیره که همه با هم می‌افتن تو رودخونه و اونجا هم به جون هم می‌افتن و به این صورت همو میگیرن زیر چک و لگد :
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67723" target="_blank">📅 10:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67722">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
تماشا کنید: پهپادهای اوکراینی شب گذشته به ۱۴ شناور در دریای آزوف حمله کردند، که شامل ۱۲ تانکر، یک کشتی باری و یک یدک‌کش بود.
از جمله اهداف مورد حمله، تانکرهای روسی به نام‌های Chelsi-6، Aura، Sana-1، Ilya Repin، Venus-3 و Penelope، همچنین کشتی Mercury، تانکر Galasar Kamal که پرچم پاناما داشته و تحت تحریم قرار دارد، و یدک‌کش روسی به نام Alfeo به همراه بارج Aphrodite بودند. جزئیات مربوط به پنج شناور دیگر هنوز مشخص نشده است.
در طول ۹۶ ساعت گذشته، پهپادهای اوکراینی به ۳۵ شناوری که به "ناوگان سایه" روسیه مرتبط هستند، حمله کرده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67722" target="_blank">📅 09:03 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67721">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/67721" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67720">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I8GVgR-PkEaS2n0XV3T9bPfzcI6VgdvWANya3Wp1NhCNepDuAxS3trn2fQtixXr-rLwPl93WpI1WYfEN7GvrFK-cuJWhHetjAyUpzYZnhG3Yu16mqqw1Hhcx6Xrd46R59UTLMYJ4gOM997GNGsjXNw-XGHqU-5tc_UFgasNt_VbUR8fnjYktuJfCHSZ0BpN3wLmS9UsbWcmpxHlTXWnnahrEd3fXp8a6noB6lFoBB9jXsZvWAy3AdDsHX4tyYIItzh58zgCwqE1Sbftnue2bXcR8zvURvRRKrRaK9uaZsr0WXbH2nUQrVSHN8GQSm4pPYh0BqYytSB1F25eOE1zLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67720" target="_blank">📅 01:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67719">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_8SC6uohVWcQ4BfqYY0KC3P0dWU0t-qbUCSY1A3rBVgU1wYp2fDOktn8KAsJ8XKD5v-zCRd9JAEj1Bq55iYyqM7jvZsvbqKxpkrnlGSrPHM85pRFXJKiGbU_DUZ0yThB3wyr_KtAR73_0h9UQqITMZljAFqQRLZjh1pclXTEyc1yC9Ywn_i1aCTdY2R9Y1HnL3FUdTfosA9JanBWv7AVrLDhMimJPHVvW3ivWyX3gDdjaYJNZ76D6rxZp8zmwEWQk7qfT_IEBm4prUaC7BV2vjdrt88E4Z3VFTvLyWF_ovzhASojSIs9OZCzjSVktsTuFfsIr_xoVrt4ieeJcOYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وال‌استریت ژورنال:
اسرائیل اخیراً اطلاعاتی را با ایالات متحده به اشتراک گذاشته است که نشان می‌دهد ایران در حال بررسی طرحی جدید برای ترور رئیس‌جمهور دونالد ترامپ، بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/news_hut/67719" target="_blank">📅 01:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67718">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
صابرین نیوز:
سخنگوی انتظامی استانداری خراسان رضوی اعلام کرد که درگیری مسلحانه‌ای در منطقه "بلوار سرافراز" در شهر مشهد رخ داده است که در نتیجه آن، دو نفر جان خود را از دست دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/67718" target="_blank">📅 00:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67717">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">‼️
خبرگزاری فارس:
41تا43میلیون نفر در تشییع جنازه علی خامنه‌ای حضور داشتن
😆
@News_Hut</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/news_hut/67717" target="_blank">📅 00:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67716">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند. افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.  @News_Hut</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/news_hut/67716" target="_blank">📅 00:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EVGtCgpxzyPQ4VzZ6aYaJOeF6I24wDTKYxsqLe2Aim7WiqlWauC4SdSxpLZLczT-8SmPAirK-gC0Jxkh79ajLLIUisNZ2J4BLe4xwA_F5_BK2-PL8KbP-TIr9R0MBI2oMeWIMNzspdpInEhx6cN5DwqvKaNuo-efNCA4z5iPIbqa6_HpEzv0ROlXJ48hX2wXiBs2antLBXjm8uIr4D4dvGH4j929gmaq40qt2T8pj4i4whrP0ISy3AATnmJUOsx84nNDEETr_1y2sYYffksnOIysPfH8UE-x3GIyubmqrAY-cTnAU3Qn6-nF5N38gb7-8Rj3KZTBWEcEjASirN-w8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Xz-HJF3Kat5cPYpmEV_D_NluR2fPVXwoIz-LJwAnFonKNcj9287vITLZLZifKju0w3IESroWTYQg9hYLbK0OWTbBzfhCywsE9Js6B_pQ_RSw50UAdZSSqjiX7rSdxbXKqubvguwzecLOiOtA6XfgwvQxQS5rdOpydwZpJrB5QPEufeL9rZT_FtixihP9VE0br2GObbvekIvU9hg97ATCE4UTCWYKIbfuSKHSulApLYeCXOvKwYIyF8vDn-tLKXEm4NU8qRR-bcEWi46hyRmN4ngy3RfYbQmJgAAyMpinO02CvtIcoBYXcFjIZkGKOXfQvWoIZJpwGWGobTaPB03bcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⚠️
اولین تصاویر از حمله مسلحانه به ایست بازرسی اطراف حرم در حین مراسم علی خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/news_hut/67714" target="_blank">📅 00:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6lW_dzFTIhNnZbpwf_kjnkBEokIZjpkF8ryGzUqsBoA_93tlH2f4rth169lgaeg_YTpb3Pp_QhSE8RtE8Hd9L4JVfrD75Dm-LM-pAYgLWSoSgCy5o__YwqtEGbNKnF3IK3j1rsoL9jvZ7DC4mqOtY-ITxTtZqj2qPNHTvoesrR80JO8-AaRP6FNuw9A21AS9dyT6z-z6Agh0DSrSQegdtSu8FUxo15g8VG7poCTR9HpVOm2M2sqm4E4OBkEJWp9UUzFpJ48B6Zk7KzEbO43ddzFmO3KDpwNF8cVBqVVpQFypy5iWCZ35Sk6xX-GH2UP2wtnd0NMjHgNLd9-WeMB2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حمله به ایست بازرسی در مشهد دو پاسدار کشته شدند.
افراد مسلح لباس نظامی به تن داشتن و بعد از زدن نیروهای امنیتی با موفقیت فرار کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/news_hut/67713" target="_blank">📅 00:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67712">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R-GVM_YuRvDrf41BnfN9ksO_DmCiO8gyEDicR75UOLyfAOPMMM6PWov46iVnSRmGmbKsYr7o5O6JxS3kWoB_Z0eEPIRU1-J5BDxtkWB_ATKj1_gknl6uAhlAeBKMlzGY42SzqY-QcH0tHRXVj6paKyQ_flVigvm6QEXlUziX9aSqF_8srRpjXd93GEG8quB0BWAqu8C3lP7MWdfaG-iuBU6CXw98qilZP9-akKT5VCGeYtWybijbircoIalziLuacSOxpiuu7SgiHtymc2qvNGaBcuzTv-AWxMTEPLqAQFMW-KECAFl3aVamhQJPbMFV_j-PadXMYbMTYKJOj-JMVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.  @News_Hut</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/news_hut/67712" target="_blank">📅 00:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67711">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
محل تیراندازی در محدوده استقرار یک ایستگاه بسیج، واقع در ضلع جنوبی و خارج از محوطه اصلی حرم است.
@News_Hut</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/news_hut/67711" target="_blank">📅 00:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67710">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
❌
گزارش های تایید نشده از شنیده شدن صدای تیراندازی اطراف حرم امام رضا
@News_Hut</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/news_hut/67710" target="_blank">📅 00:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67709">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=P_aKc9wibbkxg17jYQvijlcXXiCEya0C_CdOeDt1tUASNyshNDL15qzuqfAk1uicVpdriGDoO_IdUwfHbbotjjIr4-DEtXpqNGBkavB56iMx_A72scU2ruMF0tOC5q0TYRi1xkLp9WlgBr5aTxsl1-zFov_O9c_2defzl6Hau6JD4i5C6qyeKKCXvCCSE6B8AcUmu4Qm8mFj2cBtZdtxyQG1hKhOY7A1r2p2WbvBIgfPvkvYC1RaogtNJDYT3REkp7zw7dXR2Yh9J-y8cgkI_ip-5O2LWksiX8HVw86-c9rqz-jAiHF9okKdUAU19hsJRFhUFHRET1rohpltcmdvmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ce06a68b0.mp4?token=P_aKc9wibbkxg17jYQvijlcXXiCEya0C_CdOeDt1tUASNyshNDL15qzuqfAk1uicVpdriGDoO_IdUwfHbbotjjIr4-DEtXpqNGBkavB56iMx_A72scU2ruMF0tOC5q0TYRi1xkLp9WlgBr5aTxsl1-zFov_O9c_2defzl6Hau6JD4i5C6qyeKKCXvCCSE6B8AcUmu4Qm8mFj2cBtZdtxyQG1hKhOY7A1r2p2WbvBIgfPvkvYC1RaogtNJDYT3REkp7zw7dXR2Yh9J-y8cgkI_ip-5O2LWksiX8HVw86-c9rqz-jAiHF9okKdUAU19hsJRFhUFHRET1rohpltcmdvmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امشب تو مراسم تشییع تو مشهد؛
یه مرده داشت شعار میداد (به احتمال زیاد علیه توافق و سازشگرها) که یکی اومد بالاسرش و رسما دهنش رو بست!
@News_Hut</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/news_hut/67709" target="_blank">📅 23:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
خبرگزاری ایرنا:
یه پایگاه نظامی تو حومه شهر بوشهر مورد حمله قرار گرفت
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/67707" target="_blank">📅 23:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67706">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPkuuDFIATKSWoDSBNGkooghSwxWsPaEAMBZpYp_xVL8eL39xEgZCFqzVQJyjLUaFSyhSrTLFreuClE3o85ASRPz5uOeZ8BB5f-jvg3g_40AqMU7y-SijfB2OTFLQq6E84aLHDikg7S_l1Br-owKiDwcfQkPLc-_RYj8TB1XgmxC25sJ68h80cOUcpERt8w7Ms1OamcuQ2BoU58uIaOT6ajCzBpz0PpRouOE4v5PkKyfx3qQ7DIiG---SU4eL75u6miQheykIBrmfV8q5MZQZwq6-UlvTEc1oFUCTwna3coTjMFFlcdZlmODOt-fzQ4UFyXh-KC6DVh9K9aZRKuyEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون درخواست زیاد بود دایرکت رو خالی کردم تو ربات ۳ تا پک شد، کلیک کنید
💦
😁
🔞
🔗
دانلود پک اول
🔞
🔗
دانلود پک دوم
🔞
🔗
دانلود پک سوم  @News_Hut</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/news_hut/67706" target="_blank">📅 23:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67705">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">خب دیگه بسه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/67705" target="_blank">📅 23:00 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JA9m83joKt8V1wZpw1JrFB9pkJjgoSyxpMMywMS-LPtJm8zMKOUCVAZQTokYiEUdaV8cjaVmO3HjwnJIPkTgRwxu3tQFyglIZfdBAm4ACd5HwiW3T15oceU-UV9YeYSuwxpwzHDbZzpw0Ega4YbBr0bzTlYYNONltNQtGCq6bjMLollVR-QJDeHkITTN1Q1nqWu3s53l8nNiWk_P86UeBPpe9Z6p1dglkq3eLlEpv5kzDRFzrxsH_Ke8JCH_UGuq00K6jtwqFD4RQBHmxq675kky5sX56n-FCak_H-OUYqli6gVNBhyC6fslU535I8HY4hfWI0vGDZIA5fuzM1Latw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به بریم برا دعوا #hjAly‌</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/news_hut/67704" target="_blank">📅 22:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t_1cq5QHlBxmO6f8W3zYaEGWbs0cOlmeybnDqR2HDv7vrEYs_cai-x-PDPetIijA5-Ob0vXIwAF72N45SDuDi8febWnIdcIJZqqWHxSldzaOdeXbxRR2pBwYS_IJ4gWtdAInmwsmyoX9oYuGVLsqcz82mI_tgJ1lc7stueeIH4g0mqHozAA5glveWVST9acZLQBQLjVMsGCU7bAFYQG6SqJhNY2Lb7YluwTRgjp-XfGg2yvbH_LMeyWxV7QxwKdEKBSOGQ2e9tpL3IoP96YWxAEbxluhxeiidvHOv0vUFO2-HHEnk5Mv8TdZQq47lQkdeyboKFATH7E3R8F1w7lCnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67703" target="_blank">📅 22:50 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">یه عده هم هستن تو دایرکت فقط دنبال عقب افتاد امتحانا و کنکورن، بشینید درستونو بخونید دیگه
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67702" target="_blank">📅 22:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
نایا: ممکنه حملات امشب کار کویت و بحرین باشه  @News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/67701" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67700">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست  @News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/67700" target="_blank">📅 22:27 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67699">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
ارتش آمریکا اعلام کرد که حملات امشب به ایران از سوی سنتکام نیست
@News_Hut</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/news_hut/67699" target="_blank">📅 22:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67698">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzEHodKj_vxpO5UN8BTki_LCZEoj1TKdNoZop11LA9xmeN9mfzoTXjHBevjvRsGL1EB0k0_cpudy_uiLw93Rgt8qQZMicBGB-T81k5CSOIMuE9Ye4gsedDdNlXD2uiiDNty9v_rg0c1Ot6uQrqp0ANk372pqNeW-ZAqAeHu6tXSBqQUz9mFSGuSTfXBU8WKpeBEe9NcmYZ1Mh-6LaJv0TUp9o5_dPrqWz9IgwtiYRpNdU9YpbZyOJoHju3EA2q2-CDIoGLCZnq8f3_hLD3pD9yzr3BnLrT18Ooio9tXwC4Mrc1aDReHkUN07Y7NPnFz0od-AxTSrQPwL5eOS1QXGCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آماده‌سازی قبر علی خامنه‌ای در مشهد
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67698" target="_blank">📅 22:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67697">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=d9C67YteFfLRHnNhphXn9-z8PqbCTvfICM3LFZwN-WCbYH0SRobgSFnV1X_Ve6y2v-hBl2SVDSu3H3ixf6z9ChXXi-22HpPmXm9MEFdb8iOBfr-ep9PIbig3GE7FXswBdbCPGm0-0bSpxNvZ5s2X4bEoF3kRKDG8XJFo1PIGVW0V2dork4xuKTA-_UIif1NcfKX9OOdzwfSG7gOzLpNsbwXVeU25SqjYkiXR5rh3jfD2bzd7i4xrEYPCUFz3jYpqjNLh6fmRsbNTmMZezDIop0QQ-cRJotLQr1qmpbJVQ6Zt-hlgVu-T3LKTVR3AJgfSrAM4rBMIkLDE3vehQdjSMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8449992fa.mp4?token=d9C67YteFfLRHnNhphXn9-z8PqbCTvfICM3LFZwN-WCbYH0SRobgSFnV1X_Ve6y2v-hBl2SVDSu3H3ixf6z9ChXXi-22HpPmXm9MEFdb8iOBfr-ep9PIbig3GE7FXswBdbCPGm0-0bSpxNvZ5s2X4bEoF3kRKDG8XJFo1PIGVW0V2dork4xuKTA-_UIif1NcfKX9OOdzwfSG7gOzLpNsbwXVeU25SqjYkiXR5rh3jfD2bzd7i4xrEYPCUFz3jYpqjNLh6fmRsbNTmMZezDIop0QQ-cRJotLQr1qmpbJVQ6Zt-hlgVu-T3LKTVR3AJgfSrAM4rBMIkLDE3vehQdjSMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‏
حمله سنگین آمریکا به چابهار/ صابرین نیوز
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67697" target="_blank">📅 22:05 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67696">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67696" target="_blank">📅 22:02 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67695">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=ejZJBVNec4Xq8NXEcGEB76J4ByGIo90HBdUwuKohy-rhiUwKaoRrb9gLs5vpJYKahUKvcJpx-NtO10Qcv1NPH6xo_l2Qw1Sm14vltzStOh4L6E6RWJw1eipVv8a-QFnO7Z23l39gP0cts9WyK8nuT4vsQj48I2rXTKQo9gEvc_gqvD582gWD0YJ204BVko8xOixGpWIzY1V3Eb292tuafEwFH54SjOsRfVgkyTzyw8kkP2rwLV4F9TSlRgoBUm6-mQee66MLM_HC3xIW4UZaqmpuQIVr8gcJ9Iykm0iIiPQ6BJ5XGSyLgWgV23A7P4atIKUU3ciYDIrFlR_Smb0sBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16cd96a62.mp4?token=ejZJBVNec4Xq8NXEcGEB76J4ByGIo90HBdUwuKohy-rhiUwKaoRrb9gLs5vpJYKahUKvcJpx-NtO10Qcv1NPH6xo_l2Qw1Sm14vltzStOh4L6E6RWJw1eipVv8a-QFnO7Z23l39gP0cts9WyK8nuT4vsQj48I2rXTKQo9gEvc_gqvD582gWD0YJ204BVko8xOixGpWIzY1V3Eb292tuafEwFH54SjOsRfVgkyTzyw8kkP2rwLV4F9TSlRgoBUm6-mQee66MLM_HC3xIW4UZaqmpuQIVr8gcJ9Iykm0iIiPQ6BJ5XGSyLgWgV23A7P4atIKUU3ciYDIrFlR_Smb0sBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
مصطفی خامنه‌ای در شهر مشهد بر جنازه پدرش نماز خواند
@News_Hut</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/news_hut/67695" target="_blank">📅 21:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67694">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=rfmgL9IbGEim3UHhQepk5gpz0peHB61TFAQARWZc9Pii_3TK934FDTltC_jgZpHsy4n1HDfemym2JRbB9w8nWRv4MgyjfI2wHoMw0ixnxWXW2veyxNo8xKEGQzhQnledtlFiZnXUScrXNKpqdmxZzDg9k4Sd6XCcsQXjH_4pZOu69EPmCS-HT5vzDrzJ9B2kyPQWKX-uGOKsOz8vo1VjxMdiaR-acuaV2bPR51mQ8XvUazYGoMCN5zWhuUGdPIOJkEE2Zh1Kj6opfYE4hhesnHcFAFnReElVJ5SECrj16UCdnJT7greW8lAHbVbzeOIQ4xpExHCDNQoKPC9iSyyHfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90a8e6ecbc.mp4?token=rfmgL9IbGEim3UHhQepk5gpz0peHB61TFAQARWZc9Pii_3TK934FDTltC_jgZpHsy4n1HDfemym2JRbB9w8nWRv4MgyjfI2wHoMw0ixnxWXW2veyxNo8xKEGQzhQnledtlFiZnXUScrXNKpqdmxZzDg9k4Sd6XCcsQXjH_4pZOu69EPmCS-HT5vzDrzJ9B2kyPQWKX-uGOKsOz8vo1VjxMdiaR-acuaV2bPR51mQ8XvUazYGoMCN5zWhuUGdPIOJkEE2Zh1Kj6opfYE4hhesnHcFAFnReElVJ5SECrj16UCdnJT7greW8lAHbVbzeOIQ4xpExHCDNQoKPC9iSyyHfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
همزمان با اقامه نماز تشییع در مشهد٫ حملات به جنوب ایران شروع شده است
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/67694" target="_blank">📅 21:57 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H5amEZG2DYCPk4XuhaGt5PjOwQnS1Rze7bsdNlfDlbmWEQK-FZH4TlB9v0D3LCAD30CFrdS8NiwpHQsBAfsbi2jo9ns5Zi6o-oWtmt5qxsfkvOs47qCO7KbodBqPlXhfbSW0kV9X8Ao-sLIC73sU71cDv3uotxU3y892_EjvRJ8ZZdQY7AvwTc_HdwZoVAYlkbNRze5xQuNGKK6sg9uJz3PZnYEehtZuWUtsOjSOj9L_x9KVncPdSLBPGeAYZ6T8raK8SZH6MpTCPTtePP9Tb2CqPgb6PrW-oqzWWhxOkOYGvufoeQiGSTHI_47J-lKrCCxFNqSkhlR0AZ_axnfDZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZoUeXdHwJWy0DbxL-JIu4MYb5OHY7UStMlTwfRx-_dDWfKoWiN4emDV5iq6EcnIuoGF7KW8GjLuuNtx6NTHNEJeIbKyNRhfcqnPS1UYtjpLb--XHgx1OhzRkuv_aSm-UJr3_9dZHo_ENOn3AsnhtCElIqVwri5058vttqymbp2jziw03dzuDAPaCLYupqgwubA8IOrb5PyO-IdyBb4nycuXDMT-lkkO_fFUBgRsFlDITGNLtoEO1XVdSgz2hgbFL8m9mSnJ3DmsEUy2kjthDlf9dNQO2bDkDb_OrEod2q7XUV59-GkKvlw3ifXdfvkttE26ocZcGTvTn6xskA4dx-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
هواپیماهای آمریکایی که قابلیت سوخت‌گیری در هوا را دارند، از تل‌آویو به سمت عراق پرواز کردند. همچنین، هواپیماهای دیگری که قابلیت سوخت‌گیری در هوا را دارند، همراه با یک هواپیمای هشداردهنده، در حال پرواز بر فراز خلیج فارس بودند. این اتفاق همزمان با صدای انفجارهایی در جنوب رخ داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67692" target="_blank">📅 21:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
جنوبیارو روزا گرما میزنه
شبا سنتکام
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67691" target="_blank">📅 21:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67690">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67690" target="_blank">📅 21:46 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67689">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از وقوع انفجار در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67689" target="_blank">📅 21:38 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
شنیده شدن صدای دو انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/67688" target="_blank">📅 21:33 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28f6598797.mp4?token=CdiP3TBnmsiUMJ2SRQPgx_V3U4gYeJ5Rf-WEeS0mAkm2Vz46P7abFzt-83KeJqaQBJBVFSK-p9REAVGYphKmgqaHH6HSCRx8TG5KhWaB-BoACr4N4LFfKpBAyxIOblBYktJuaBr4pzjbU1-MOLlmgB-OUd_XJm0ajMjAY1fHDllPNsyoMfgEB5ZLapDGoLP8REGymyM0mNJcnS_HccEljPXV3gAix2HawV9WTnyEkC7C8JF3ORbkh9rYXIcHRVZBUmIsNqyPISPpsgKKZ5IQ9GNHtSRMX7NZP_fbjMtWH1tDAGFgXzLm6G503pXHR-5sJQ6qCXYXbtQfDtqhfrwQUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28f6598797.mp4?token=CdiP3TBnmsiUMJ2SRQPgx_V3U4gYeJ5Rf-WEeS0mAkm2Vz46P7abFzt-83KeJqaQBJBVFSK-p9REAVGYphKmgqaHH6HSCRx8TG5KhWaB-BoACr4N4LFfKpBAyxIOblBYktJuaBr4pzjbU1-MOLlmgB-OUd_XJm0ajMjAY1fHDllPNsyoMfgEB5ZLapDGoLP8REGymyM0mNJcnS_HccEljPXV3gAix2HawV9WTnyEkC7C8JF3ORbkh9rYXIcHRVZBUmIsNqyPISPpsgKKZ5IQ9GNHtSRMX7NZP_fbjMtWH1tDAGFgXzLm6G503pXHR-5sJQ6qCXYXbtQfDtqhfrwQUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
منتسب به آسمان چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67687" target="_blank">📅 21:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
🚨
‌ کان نیوز :
مقامات ارشد اسرائیل تمایل دارند تا مجوز لازم را از رئیس‌جمهور ترامپ برای از سرگیری حملات اسرائیل علیه ایران دریافت کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67686" target="_blank">📅 21:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67685">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
❌
گزارش هااز وقوع انفجار در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67685" target="_blank">📅 21:24 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67684">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
شاهزاده رضا پهلوی: شش ماه پیش، دقیقاً همین شب‌ها، کل ایران خاموش شد و تو تاریکی فرو رفت. ولی حتی اون تاریکی هم نتونست مردم رو خونه نگه داره
به هم‌میهنانم گفتم آنچه شما در ۱۸ و ۱۹ دی‌ماه آغاز کردید، مسیری بازگشت‌ناپذیره. ما با هم جایگاه شایسته کشورمان در جهان را بازپس خواهیم گرفت، عزت ملی خود را احیا خواهیم کرد و یاد قهرمانان‌مان را با ساختن ایرانی آزاد زنده نگه خواهیم داشت.
اکنون زمان آن است که درنگ کنیم، دوباره نیرو بگیریم، و بار دیگر خود را وقف پیروزی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/news_hut/67684" target="_blank">📅 21:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=XC_LjVnbiPfU84G_TwI0SFPKUH46kSDGP2CV_55AKVCrk_6gKooT76BjYHpg-SCMCDmzOU--Xj0hvEdRJk_EQM5FBSlGnAjF4kbCzYR8cpBqhkJQ2N5cyb7E4PAP0d_5qzc6BPJurxjPHViut-BozGyi1Bj_PqpiVYGMcp-FrZO2eKHv4NZHxm1g171Hp-Nv6CPEAJS2xW2MhnWVZyj-NVnagw_GXDQiR3gMILndjU0o1epMVxX0aIEXp5zFTjLbosCzXLF203nGJpTNGa3_B6x0UUSE8t_v_sF35pjsuhRqPBVwED66zvGlUVvR669ctTRbnrIj-2hkAZBPtlb4Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab72866bc0.mp4?token=XC_LjVnbiPfU84G_TwI0SFPKUH46kSDGP2CV_55AKVCrk_6gKooT76BjYHpg-SCMCDmzOU--Xj0hvEdRJk_EQM5FBSlGnAjF4kbCzYR8cpBqhkJQ2N5cyb7E4PAP0d_5qzc6BPJurxjPHViut-BozGyi1Bj_PqpiVYGMcp-FrZO2eKHv4NZHxm1g171Hp-Nv6CPEAJS2xW2MhnWVZyj-NVnagw_GXDQiR3gMILndjU0o1epMVxX0aIEXp5zFTjLbosCzXLF203nGJpTNGa3_B6x0UUSE8t_v_sF35pjsuhRqPBVwED66zvGlUVvR669ctTRbnrIj-2hkAZBPtlb4Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر اسرائیل، نتانیاهو، درباره ایران:
ما به ایران آسیب زده‌ایم و این تهدید هسته‌ای را از بین برده‌ایم.
این مثل این است که سرطان را از بدن خودتان خارج می‌کنید. اگر سرطان را خارج نکنید، خواهید مرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67683" target="_blank">📅 21:01 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIwSTMJ1HGNWzbKdJs0UX3wfi5LAhpZErqOS3PyObG2VBIlfZHX4gSk8F5bOEQW3ZkrS9Pzm7CWVmb0QGN52RO5qGXwMgTII7B988F_L7PbejhsLDjA4EFWTRjWDvfr6agc82GbhkgVGwEZ-TsNSb6st5h0AMANAwjx8SMUWFULCRmuU9G8qcaPu2L3DLQ-dyijPHVWFGlbT3i_UAivqEnjFMSc6cjPA2DoEDxWlDlLEmba9l4JOKL37xre_BMF8_iC26oMKzjWvbxa5r2s0cVm9ShhIeKyv0ocb89TFdMm0e6j4g5aap0quL-H1pN7hEqsu39sCW4CnFAPW4Ho4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو، درباره ایران:
خاورمیانه در سال گذشته شاهد فعالیت‌های بی‌سابقه‌ای بوده است، به ویژه دو عملیات موفقیت‌آمیزی که ما علیه ایران آغاز کردیم.
اگر ما اقدام نمی‌کردیم، ایران به سلاح‌های هسته‌ای مجهز می‌شد.
رژیم تروریستی ایران ضربه سختی خورده است و سیاست ما کاملاً روشن است: چه توافقی وجود داشته باشد و چه نداشته باشد، ایران به سلاح‌های هسته‌ای دست نخواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67682" target="_blank">📅 20:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPbF-TmIa_Jsjx1QLm1caTc6QJrk5c0mvnLlSbSlCPoEuD45zHAHx1-wJeZvc6n88ZmRpPSEPc0AezvAkEpfNGk3lyWzduh76pqpGwVrgSRrnxpa4619Fggbn_--8-G2XYkPO4Qnf5TC8TSESbLOmZz4YRG2eIJScNo2Qu-jp7LUx0QPchB0rCuxIdvkxembD8545uLLwef6LxquFmq1EJDXdwNHA4jnpDCru1OI4Lu4crNaIyjSiRJ5xUK2CnIEesHIVrdgHkVUMMstq8v1UN475bxyQ5n3G1TwzyAIVXPA-sczD8TSUCwb8leeBdU-5Gv-Bm9IOZdEdz5uBei5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید به نقل از مقام آمریکایی:
این تشدید تنش‌ها می‌تواند یک یا دو روز، یک هفته یا یک ماه طول بکشد، بسته به اینکه آیا ایران به حملات خود علیه کشتی‌ها در تنگه هرمز ادامه می‌دهد یا خیر
"ما قصد داریم آن‌ها را کمی تحت فشار قرار دهیم تا متوجه شوند که ما شوخی نمی‌کنیم."
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67681" target="_blank">📅 19:44 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-caHXvy1mUFWKmDiwL1Mi9R7-TN6u6OTAA-tvrRIHzGa8NyAusCYWfX1KovPRAIbBDkHcmV9g4hT2NiCqG5P72eBzwo5G6zrHw46SWRU8r6k_G9fHp5tgXWammgc4R8l2a6a2P3lSAYTAGXXAwo8VxeBGu0wX2kyNBVxOmWaNQMHjF8hjwRyCUQfT_joYXP5Kr0219ewRCGM3nuQ6oDUbM46Or8ogXFnaezNtFur7SvvMYNAzGeKCsJ_qfkF5-DmTy3TqQzmo8BVFu-5_ZjEzg8A2kjgMg6VJXONI6tKsojwF-3U1-uw1WECFmfh1xqUJRLVCRD9RbtoJbTxL3KOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
🇮🇱
کانال 14 اسرائیل :
🏴
علی خامنه‌ای حدود 600 میلیارد دلار ثروت داشت؛
رهبر سابق ایران، علی خامنه‌ای، در حالی که تظاهر می‌کرد مثل فقرا زندگی میکنه، املاکی تو ترکیه، کوبا، مکزیک، ونزوئلا، سوریه، دبی، بریتانیا، روسیه، عراق، ارمنستان و صربستان داشت. همچنین مالک چندین هتل تو اسپانیا بود.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67680" target="_blank">📅 18:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=H4dt8BqdBqZZXoU8XvkASAPkRuSpsxb1JIIZs7ngpnnbX1xVzPORN0AW8zdjMikhnKdCey6J5d_I6Rca2j9nR7PEs2c_K69i3B_amVN93mAtjYFkVSSvYAjEicS9H2sDIRO73LsDbLclszEDlyoYFmdTmccUcyr-7UNBxkamp0C7B0DWb9FEt2BWP8xS43Qqn0D21My566xHgvuGucujmUjyrKXTq4bwu_1eEmHLRdQzVAuoAauQtEmNwc_xwtWObgDd0omKJWHOfl_Udha8b8tNYCwhRSsCc1oqSdajTWTjZrETuoNRwYI5N8liWeMMlHrpHnK-LnXBpYrmkFWbwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bd409d64e.mp4?token=H4dt8BqdBqZZXoU8XvkASAPkRuSpsxb1JIIZs7ngpnnbX1xVzPORN0AW8zdjMikhnKdCey6J5d_I6Rca2j9nR7PEs2c_K69i3B_amVN93mAtjYFkVSSvYAjEicS9H2sDIRO73LsDbLclszEDlyoYFmdTmccUcyr-7UNBxkamp0C7B0DWb9FEt2BWP8xS43Qqn0D21My566xHgvuGucujmUjyrKXTq4bwu_1eEmHLRdQzVAuoAauQtEmNwc_xwtWObgDd0omKJWHOfl_Udha8b8tNYCwhRSsCc1oqSdajTWTjZrETuoNRwYI5N8liWeMMlHrpHnK-LnXBpYrmkFWbwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
علی خامنه‌ای در حسینیه امام خمینی، پیش از بمباران توسط آمریکا و اسرائیل:
آمریکا هیچ غلطی نمی‌تواند بکند (23 اردیبهشت 1393)
اسرائیل هیچ غلطی نمی‌تواند بکند (18 خرداد 1395)
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67679" target="_blank">📅 18:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/277d837de0.mp4?token=uMh-35kh0kwz-EPnq-KOdUTTpYgUTdpj5pjaZZImZQn5HKq7j8I37vizEw5HVKMYhSi72GG_6xy4-IIBMg7jjr7kqVHul4AjjsGrx5fuTr-Dqge9VF0y2p7Sj-TKBpBQR4RXZkU6NrlT-Yz8HVZKaXM-490Pc8g6oOjL9aKg3ptuhEz5RNo02UgkOongPlJXwrD_ndDFksWxTp32tk67QgSlBD5Y8LC3E5fuZI1-mEWC8-az4qDInGklenz1HA3PhC4t04eyJFgpPiJB-SB-SE2SUnp30VZXIJEYeHYGuFspV8pzOa7Vm8OuBwdeHKaiUi_-n3pxHDaSDBP8eH-rvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/277d837de0.mp4?token=uMh-35kh0kwz-EPnq-KOdUTTpYgUTdpj5pjaZZImZQn5HKq7j8I37vizEw5HVKMYhSi72GG_6xy4-IIBMg7jjr7kqVHul4AjjsGrx5fuTr-Dqge9VF0y2p7Sj-TKBpBQR4RXZkU6NrlT-Yz8HVZKaXM-490Pc8g6oOjL9aKg3ptuhEz5RNo02UgkOongPlJXwrD_ndDFksWxTp32tk67QgSlBD5Y8LC3E5fuZI1-mEWC8-az4qDInGklenz1HA3PhC4t04eyJFgpPiJB-SB-SE2SUnp30VZXIJEYeHYGuFspV8pzOa7Vm8OuBwdeHKaiUi_-n3pxHDaSDBP8eH-rvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دیده شده در آذربایجان غربی.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/67678" target="_blank">📅 17:31 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54718627b7.mp4?token=ciwYJMKLi3ElN7EYU4yJVLUvQh4dPju2xef-SZY26KsNoduBN7VzpK_EFf9wpoMLTmMMGtw31949dqggkY1VB1qoW7TManh8IvJM_uhvMj3w9ommnscwXEyHhXzjZtld4AN5_gp-lEk_dEkfQGDMD_YsfW5Td2XBDtN2YznKFKXe9rz1BZzjltC_wg4z17CcSk40yW6_9xRiciqd0SxcPDZH0aoCWNxUzK4awg34PdMfhdrbQdb97ZDk-bXDH6hbz0GkSoTZuDTK3z-w1Ki3vG3Jeh9ibLQtC3n5g7OZiq1jPx27qo8RUQ61HQXmu8sXwkoMmCDRTJhfCsSTWPAmKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54718627b7.mp4?token=ciwYJMKLi3ElN7EYU4yJVLUvQh4dPju2xef-SZY26KsNoduBN7VzpK_EFf9wpoMLTmMMGtw31949dqggkY1VB1qoW7TManh8IvJM_uhvMj3w9ommnscwXEyHhXzjZtld4AN5_gp-lEk_dEkfQGDMD_YsfW5Td2XBDtN2YznKFKXe9rz1BZzjltC_wg4z17CcSk40yW6_9xRiciqd0SxcPDZH0aoCWNxUzK4awg34PdMfhdrbQdb97ZDk-bXDH6hbz0GkSoTZuDTK3z-w1Ki3vG3Jeh9ibLQtC3n5g7OZiq1jPx27qo8RUQ61HQXmu8sXwkoMmCDRTJhfCsSTWPAmKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ویدئو جدید از حملات سنگین دیشب آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/67677" target="_blank">📅 17:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67676">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑬𝑵𝑨𝒀𝑳</strong></div>
<div class="tg-text">دختر خانومای عزیز در این شرایط باید ترمز بگیرید که ایشون فکر کنن ترسیدید بعدش گاز بدید بیاید اینه بغل ایشون رو با مشت بشکنید
اگرم امکان خراب شدن ناخوناتون وجود داره سعی کنید با پا بشکونید
بعدش تلاش کنید فرار کنید اگرم نمیتونین یه اسپری فلفل بزارید داخل کیفتون بزنید بغل پیاده شد خواست دعوا کنه بزنین نوش جان کنه بعدش راحت برید</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67676" target="_blank">📅 16:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67675">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03400665ec.mp4?token=CY0pCAeyCtglFFdfvKyz9HTQx7cQ9-TKzp_IYPiCXUwOareOVxITxTHN7K_QNRc9Y0NnGTvAMQielpBlMNy2iH5vv_oGZT1RDMCJ22DACTB3dhZU05-4oExKurDkiicUSpheoCBH8H-nh2-33NbIyi0hPPAt84O_ZO5fw5qiZkV1i3t8Czu-FOkONl6G3Cy1Tn7pt23sn_EyFXp_adJR6lWddVdLiQIKiOzgIn81igoz2BUCWMkpkl9cXpEqIt6q4ZUaVv6VXMpe7vkTGQLXNUwIKiG8hbl-b3fNwjax5w-h_22Jc6CrfKgQRDwTIL-y1sT5KxgvyGAL5HRM80I0yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03400665ec.mp4?token=CY0pCAeyCtglFFdfvKyz9HTQx7cQ9-TKzp_IYPiCXUwOareOVxITxTHN7K_QNRc9Y0NnGTvAMQielpBlMNy2iH5vv_oGZT1RDMCJ22DACTB3dhZU05-4oExKurDkiicUSpheoCBH8H-nh2-33NbIyi0hPPAt84O_ZO5fw5qiZkV1i3t8Czu-FOkONl6G3Cy1Tn7pt23sn_EyFXp_adJR6lWddVdLiQIKiOzgIn81igoz2BUCWMkpkl9cXpEqIt6q4ZUaVv6VXMpe7vkTGQLXNUwIKiG8hbl-b3fNwjax5w-h_22Jc6CrfKgQRDwTIL-y1sT5KxgvyGAL5HRM80I0yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر داشت از موتور سواریش فیلم می‌گرفت، که یه حرومزاده دلقک این بلا رو سرش آورد!
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67675" target="_blank">📅 16:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67674">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbqOl32deNjeyM_Y3PyfV-h8TAmlVy7ZJ3b7KnObBHb6QG6vITWyHdZMIN-9d2h-NKV1f-VIOCrF348603xWPvDL0SxhgsQrpPnQscDjauRPXqGhaydxFsNubZI004biwWKi6-1trBVX2LO0vwR1EpJTnmTORTI68OvrGLARmXzG7derBT0d8WW3JyH0uNW64INCZZCS4YbBMFe4mV32uv-SCVnZ2AiyOBl901vhlibSGqu_5DCGRRSXUcDMGkeD3JEZNL4NFr8RLjgfzC7EpE_Sai2tsAgXhG2qU9N6ZnWCv8MLktVWTeYt-C05bu29hDXgzl3LTTO2sY-mrLTtqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هم اکنون گزارش زنده ترامپ از وضعیت تنگه هرمز
@News_Hut</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/news_hut/67674" target="_blank">📅 15:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=dJSDQSwz8Gb6-YEDAcyw2U4flmgGUT_XDYZMVIrh0hlfu-Nefpv-q3xzebz5W3LoJr4Tvy1S6Zc_0J71W6zHS04eKbibu0mQYIrJcofWjb6L7NBZ2JrsPBFd9TOxjcOQf48Td3WOBOTdoQLwbV6b-6l60jDGM8F6THJgixeIwAVSjGc9iMcyu_nyoo4SxZGWWIwwg-7zlhfY-Fmw2f37N3CLCgNCFfAki3txWBKYO2_BPAAnPdTuxhGvgIsFoHF8bkcCgeg5VHVnBbl84L0jG4Rwjo2qXOL6CcHINVso9xLQMj0C6yzNZWG4-9NXCtaxzVVZ0H6ADh9U3KIEvVuJR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae15a4dd4f.mp4?token=dJSDQSwz8Gb6-YEDAcyw2U4flmgGUT_XDYZMVIrh0hlfu-Nefpv-q3xzebz5W3LoJr4Tvy1S6Zc_0J71W6zHS04eKbibu0mQYIrJcofWjb6L7NBZ2JrsPBFd9TOxjcOQf48Td3WOBOTdoQLwbV6b-6l60jDGM8F6THJgixeIwAVSjGc9iMcyu_nyoo4SxZGWWIwwg-7zlhfY-Fmw2f37N3CLCgNCFfAki3txWBKYO2_BPAAnPdTuxhGvgIsFoHF8bkcCgeg5VHVnBbl84L0jG4Rwjo2qXOL6CcHINVso9xLQMj0C6yzNZWG4-9NXCtaxzVVZ0H6ADh9U3KIEvVuJR4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
اسکله بنود بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/67673" target="_blank">📅 15:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67672">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
🚨
دو انفجار جدید در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67672" target="_blank">📅 14:59 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67671">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فعال شدن آژیر های خطر در پایگاه آمریکایی "ویکتوریا" در نزدیکی فرودگاه بغداد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/67671" target="_blank">📅 14:51 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67669">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s1zVGVT-Jvf2Chf1yPKlLSvW4E5JPS0KLbPJuKb5yK43i7dQ2A_zqnn9_VwqbR4FWGzymgfTsGoXp8FhwJ-yIEH4yV9YGvXANFfr4hW59lgexkP8iHh5pke6CA8aWlGqnWsooGCxX3pqxelW3-fgTr1YJXzR-JFwHzbggsTeaA-0eCSIreqS1Y9wa-o7AjARW8lus2VNXt-MmS7bFX--gF_rSEX8CjuJePCG9-o_7P-oe8kZ3W0kJsA2-0l3EuiEHVPwyK7u3liASjPLp1c14E4YWofYwpXo16_b5Vf5k6-b1Uj-sB1D_028HL5f2WAeJEVPJVDaV3Ey2DZ7O8MNFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R7JT5AQvG5poEDhG1nm_ANHYJszrWmiYcYjaxu3nFASYq7IOzBkCvwtgHvNLZlF9jsLTfjSv7QU7aatVy1iXKULGmVIBdu1vAbnrRjaT23pqpW9wvTxSjegD6abFZ_FYN7fvVtmpT6yfroeSD9Rqkt_78BcfduU9uFhLG7RRjTcRU7Xjy3qg3xdErchGhyU1pMA_edceciLFFDQy0DzFA8wl7k2f5WJVFqX0arYWXEbFVU_HqvWgAmWLOMwr6-Bpxq5WOl8XXK72AMx9z_Gwo1eDXXDmyMz0-k9_UPt5npnLN6-EVy0q_m8KVZvDi_nwVn3__hLlLt6jcOkm-6kFYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
اسکله بنود شهرستان عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/67669" target="_blank">📅 14:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67668">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZe9kHR3bTd0uNo3TvdeE5OynlQXasumZ2nmO-YDSKBFjitITy-aKLoCiFKpMbpAKl0EDCVpu-G-BLRYPEqaYYt1mgtMtk5RMgYNnlv87f5TPh0t-AKFjxsJirZp2klpJqe-NUZPh9HSXv7-bxrSj5YeCyPdZ7-9xm2-o9uvMG6hDt_hk4afJt6V1Bm3LQdAHEQUC8thpluqqyupRITU2rvZNH3NSFWpZxFCDIxP38SqBZStjhVlg22Ca1mvfA2jCOZpaVDNDTGXHFnfzVXjl_ce35XU87Ib9x4GAtLwdshZwJksklvFNBPm5BDoH5bzD0p6QrdtLmHnkvfCnZJVqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شلیک موشک از تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67668" target="_blank">📅 14:32 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67667">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان  @News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67667" target="_blank">📅 14:26 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67666">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mR_RuhbInA0eeOZlz_XboPSsLb1gonLgsdV9Fo4OTL0LM2KYtj3A3KFZ7AxVXLH_Z9OaYLzTzGO7Zo9A0GcUcqfUTSlNhd3DrJWFp0xIMtLCk6PAec2XVlE3CjOCcOEFEItsq9g3-gYPc5NCI6kr-NhrKKoQarZ9pV6acGrIjkuTnX8n-Is5BFIHPCkMss8UmhEsu0NjlswXzj09zyrD3NuGvoY51ZNmOxIRdIW78w21hgeEw35msH14gx9nftUFsOU4pWxXisjQ1xB3Ai55oOlO5z89AlFStUfg3xNiNgpzq7I6eDi83W1J8nFa4iI3esfInoMcIpxnpZCEPdWs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تانکر ترکرز: ‏
تهران، در انتظار ازسرگیری احتمالی قریب‌الوقوع محاصره دریایی نیروی دریایی آمریکا، در یک شب بیش از ۱۰ میلیون بشکه نفت خام و نفت کوره را بارگیری و ارسال کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67666" target="_blank">📅 14:23 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67665">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کرمان
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/67665" target="_blank">📅 14:21 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67664">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=MPejIxNTcaGGJ8icaCQxF4bFxQCFbzoNnDu54jvJ1x-rwj3-Rcvs6qJSDLkPusW57DXybGuZOZVGNHxBa7SNFeWbMK8usHlQFldw0tXVo8V4kVRUx0v0MwMHkzg6VL7X4u7VGi3ZxLnH1c04al67gSqWLQe9n5AKEp4B8RtEYa6xE0dH5fXpXevAnIB39_zhpf4LVzdT2mc8tUTvUmYPs8G4am-SX3KgK4xTFl1drXwDQyN7RlLRILpTROz9KbJA0mr5L05QGpbnuApM0hvO-kcMKqj-9Ulz2vnyg5WsZ4HOEjmJUb-hDjxITHrK4qWDw9xYQK9SdOteGksHdr5rDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0e2eb383e.mp4?token=MPejIxNTcaGGJ8icaCQxF4bFxQCFbzoNnDu54jvJ1x-rwj3-Rcvs6qJSDLkPusW57DXybGuZOZVGNHxBa7SNFeWbMK8usHlQFldw0tXVo8V4kVRUx0v0MwMHkzg6VL7X4u7VGi3ZxLnH1c04al67gSqWLQe9n5AKEp4B8RtEYa6xE0dH5fXpXevAnIB39_zhpf4LVzdT2mc8tUTvUmYPs8G4am-SX3KgK4xTFl1drXwDQyN7RlLRILpTROz9KbJA0mr5L05QGpbnuApM0hvO-kcMKqj-9Ulz2vnyg5WsZ4HOEjmJUb-hDjxITHrK4qWDw9xYQK9SdOteGksHdr5rDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فعال‌سازی سامانه‌های پدافند هوایی در اردن و به صدا درآمدن آژیرهای هشدار.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/67664" target="_blank">📅 14:20 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67663">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67663" target="_blank">📅 14:19 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67662">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=P8KY9qQbFsJnmUzG2fhZ7BIL4OQYKzhy1JzDE_syDAOWGFIk6_vTfaoAb1lgGawTWaDATH4BeQ69fCpfPidEnw-4NAqo9G-GXNeJlanfJMchZ1fEyvNmmf8rxhXgFKUi1_ByoeKzqjBPtY3Oi2NzgezDvphMbtmS-9kNL3o8_RFKny0A3a86TVrM_4v3ZuX7MCa1stmz3IPPnk4eKiYchYlgELPBSUKX9LjrNtrxEq1Xw5bgRpHQFMdURlAIKYIw_jw2R25pxKGo8GQliRzjxuFfdDuWhyL5nxfPPFc6KdqLNo3G3CL2gBj-0J_fWReEbviz1q1bGYiHLne2Hc1pqqA5zym_sD_OfrFIvM7eA2P5xbJe4st43kdEsbbMoZWXGzP_2QZ8jLGOAVCnGZSyBvyrDBntTspocvqr9j6uE3NjSELe4uPFx4Moo0zmkCTZZm6NRDlZ5yqjA7VkUJVmRK_MpTWXzIgVNnVUJSSIwU3oDjUEBduIe59UDCOqHkuqlvwrtG41yvlFZTr6MNNEuBabpU4CfjpfPwe6d2IuGuc9_s_YhzWYoTJxTyS9Vyp_atghzkbpmjxSo9CE0n_U57JgZ5yZ-ijI0Qz6ymZlV-mBQJhz9t4SvVCGHDKhA5slJOKYiwjXBEXlx5K0oHSIWxmQ8ePWQ_f0RFr8JIgOTJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1373fa65b9.mp4?token=P8KY9qQbFsJnmUzG2fhZ7BIL4OQYKzhy1JzDE_syDAOWGFIk6_vTfaoAb1lgGawTWaDATH4BeQ69fCpfPidEnw-4NAqo9G-GXNeJlanfJMchZ1fEyvNmmf8rxhXgFKUi1_ByoeKzqjBPtY3Oi2NzgezDvphMbtmS-9kNL3o8_RFKny0A3a86TVrM_4v3ZuX7MCa1stmz3IPPnk4eKiYchYlgELPBSUKX9LjrNtrxEq1Xw5bgRpHQFMdURlAIKYIw_jw2R25pxKGo8GQliRzjxuFfdDuWhyL5nxfPPFc6KdqLNo3G3CL2gBj-0J_fWReEbviz1q1bGYiHLne2Hc1pqqA5zym_sD_OfrFIvM7eA2P5xbJe4st43kdEsbbMoZWXGzP_2QZ8jLGOAVCnGZSyBvyrDBntTspocvqr9j6uE3NjSELe4uPFx4Moo0zmkCTZZm6NRDlZ5yqjA7VkUJVmRK_MpTWXzIgVNnVUJSSIwU3oDjUEBduIe59UDCOqHkuqlvwrtG41yvlFZTr6MNNEuBabpU4CfjpfPwe6d2IuGuc9_s_YhzWYoTJxTyS9Vyp_atghzkbpmjxSo9CE0n_U57JgZ5yZ-ijI0Qz6ymZlV-mBQJhz9t4SvVCGHDKhA5slJOKYiwjXBEXlx5K0oHSIWxmQ8ePWQ_f0RFr8JIgOTJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
آسمان اردن
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67662" target="_blank">📅 14:18 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67661">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=R25UBZU2VsEb9UbmcWe1k44yjoRGJz2bYnw9XWNfl-67oa2LWTBpfuYZvkbxqJ2oThCok0_f2hqG9R6IOC6EPxp9SK3sVLBKU5VXnX9xx44c_-Q17Ojnd-SF0-2F9Rl0L_XdWCShBAhb8yosdCznghR_4Cu5febCMUFfn1lYptlg3lrK_EwIv0ppwRQPyNvngSKxGc_3fG3GhLo1SICxJ4jEQYnWz-HvFh7XsDw__plyG_ywYGOS9pwjhNP9rHXHAsGvEMDKND0jxt3PKkB2pG0LHqJIoaXQXgRHWCI4dCEsIFcLq71KOrIRU88belRsr9qtGjLIUUSfDeWn__smmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be7cd95dd0.mp4?token=R25UBZU2VsEb9UbmcWe1k44yjoRGJz2bYnw9XWNfl-67oa2LWTBpfuYZvkbxqJ2oThCok0_f2hqG9R6IOC6EPxp9SK3sVLBKU5VXnX9xx44c_-Q17Ojnd-SF0-2F9Rl0L_XdWCShBAhb8yosdCznghR_4Cu5febCMUFfn1lYptlg3lrK_EwIv0ppwRQPyNvngSKxGc_3fG3GhLo1SICxJ4jEQYnWz-HvFh7XsDw__plyG_ywYGOS9pwjhNP9rHXHAsGvEMDKND0jxt3PKkB2pG0LHqJIoaXQXgRHWCI4dCEsIFcLq71KOrIRU88belRsr9qtGjLIUUSfDeWn__smmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ردپای موشک‌های بالستیک در شهر خمین.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67661" target="_blank">📅 14:17 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67660">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
🚨
نایا:
شلیک موشک‌های کروز به سمت کشتی‌های آمریکایی در نزدیکی بحرین.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67660" target="_blank">📅 14:15 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67659">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=Hqz1F_vPEt2r-sUfPCaKmCPwvzLVqc4NRDp3PFNPR-wIyEhwZCanTvZhGfVVstCoRbrm73XQASOEN6elMEAGUS8ys5iuFGdYG-cpb8dm9NGwWKbz_OIm5R1Tn2vWslEdX39zU8If0x4pKfCIwDK_u3EpcpOGfJj6FndpGh2j9p91SRPdSEBno1hlHBNNfRA15vR1JsNlsnf-dWxTHItZIMMRE8OwM_7E_T-b2D7cjCxG199v0jDJuBXoEwfh27R9b_Dw-PKxztA3hTcNB8UdsPVVo98I16EAMlZGX9tbsh5-WCpWBf_8hyw628TGmZbwASMenbidWSE77HppfpNhDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3cb5d140b.mp4?token=Hqz1F_vPEt2r-sUfPCaKmCPwvzLVqc4NRDp3PFNPR-wIyEhwZCanTvZhGfVVstCoRbrm73XQASOEN6elMEAGUS8ys5iuFGdYG-cpb8dm9NGwWKbz_OIm5R1Tn2vWslEdX39zU8If0x4pKfCIwDK_u3EpcpOGfJj6FndpGh2j9p91SRPdSEBno1hlHBNNfRA15vR1JsNlsnf-dWxTHItZIMMRE8OwM_7E_T-b2D7cjCxG199v0jDJuBXoEwfh27R9b_Dw-PKxztA3hTcNB8UdsPVVo98I16EAMlZGX9tbsh5-WCpWBf_8hyw628TGmZbwASMenbidWSE77HppfpNhDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
موشک‌های ایرانی به سمت پایگاه‌های آمریکایی در منطقه شلیک شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67659" target="_blank">📅 14:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67658">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
نایا:
انفجارهایی پایگاه نظامی آمریکایی "الزرقاء" در اردن را لرزاند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67658" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67656">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C710aBvQSLg71rxIrAym9t-xUxtItshSxZ6ZqvbJIEZ5qgX1GRd5u8TFane_uN5EIka1y99Sdo6FvUH_iK2aomoHXluhtUfX3M3OQ1g9b_qHFctiCLaxITMfgxyFFl_rkgsIPllWLe4l6zyVyMR3_ojSFbtjBtQuWAq8pOuoPoLScw4OZnjeku0JmoupIRqJfKgCbpKNZqjTYdNAISV6jM7v9gwWwcJKtLAelnlqbnq-hh_q-aU2LlpmnYTfr7bNdNVT1cvhAg_5H7UnEYgWmtCpxP2g2i71H9gicax7W9a_ObadpapvRhheHpbfzJWa-dPdpXHb7CqV5SeGoXBWhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQGpYprDorbMNQqHSbH63L3vyDqEV-oIlDNZXGG9atcMTObqsIVDqVffKf9LQdnYai4qjtSxVZyRXOd5wqXDx0IlNuA6qqVevpy4IQTMkSK3ass7Jh69HN0MpU_Habnaew14J9VOnYW2gWdBKgz_0l9wwsIh6lDJGJx3Hg-kTTJhuvql1i9M9yfF3IE6Ls26Kg4IC4H3k04xNkNTKfxR9EQoNibVtA9LZGUPsuMzlnIkoflSaCQ-XBaYv0t19O4VKhX-jPPi1uQaFph4SCzJQa0hefOufVep7KH7BpuIClrIeAZkYTwds5YC9X_SC-xyaT-KCazGS7z4mL5waM6EPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
از الیگودرز لرستان موشک پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67656" target="_blank">📅 14:12 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67655">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
آژیر های خطر در اردن به صدا در آمدند
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67655" target="_blank">📅 14:11 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67654">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VGJHbyDwILokdlPEv1xDH3RjiORXs9rLDaEJOU8b35zNel7hmUqGz2LSWPzMOyoSqF2deinIC2sjP8lNtREAX51uH4ol_dw2JR8krMO3X4ubuvQJhePvf9bde3uilmqT0hsmVrINZlCrjM8V8W0NIiQGpjZazxpE4QPAPqrwHib7be69Pwrtx9fiaGc8smsCqrC0P0sSYAhxZLU4zpUnzZJO5z9mTR7kJzhcRN5spoF1LhTqESYwvmoax74V6mI4qJ42w96wsquTOuL4Ajm19j8YUJ7_6ehqGeZHHckPjmXD43Ch085NIWAwYafdyufDmPlkn_nC52LDjdQpqW_9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
از خمین و زنجان موشک شلیک شد
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67654" target="_blank">📅 14:10 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67651">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QhR0QZABdS9GTPH-a6a_nF_tSLHAzTKbWOCKr5iUfR5RDO9Jm3X-tmbR66c-fDjq0pIx6C6XrI4kW0l5aoid11LAlOiCS312luCRZgeOSzPT7DtGcGNtwLa-7OngPq9Sqp0yRPkQjO8Qfhby-m_vVhOiY2a9nF1McmFEyRdJxF6cbP6kGuyG1gfqX3_fIrLh2pk4QLT2xlkrd4JaOeWkwgao8z-BzYLSywlQJpptpjJ6A9O4B0BvW4prqsnzkswVUxyirwiSox7PWxhlyhSPq7bJBCL7QtECBH6l0tTduYcbUj5XAX8OkH2buUvjXKOEyk5vJ_LNaN-3zwwkCvh4bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTnDRwqCmixtI7Hq1BuX0LBh5nTK0bBpkbX_lkTokmORG2cAiv9K98WxT3lo2vorBhxwWEYN5brjtjB-dqj-RT0rh7OAsdUtpRFrkeFwKhQQdEeU2bB7wS1LHCW4W9CLFGqIkl6KUQm05-pRDehJpqF3yAGVB-6GS861SZEtVTIIU53OurrGYw4g4gMer9R7HfiuKyshQs4DlUXwphL2Kaj03jHrp9RjT55p4QIBtPvK9JfqyxuMtM7vk91k8HONlSmRQSNQMukwiBqYj9Mi3VfRacbHx0s_obggoBh_MZ7maEhyurvN-gr2LohDw0rSmONMteI9zful8ha620JaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bVestIO4pG1dYqHBQTnAZdM33g8uoa36uTidf6bHHqDX-njGNokv7QRemPKGGjMYj43GX5YS2TZ0DVymFEUA2IJNQctmu8hJc-Y7xpduvV3nP-lh1OnL1GoKdGptoUEPTLD1LyKSurXD1m1aln0iS36NoNqpJWCUl5qpe14o8fHwBTeyV7b_TL5vXDM0QVsMs_Q7rQTUYl6UfcEVIkpa9aybViiKfP2AXHEsvk9xlA92B0P9XVFMpx05y5EuZPD5O4txJ1er8PmLDnrKG87aqy7I_6W-FX2dK4jt18iH31gOKKRL7rXScSxZwgt2aD8lzSKAf0wwcIHYGrJqF0NG5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
تصاویر منتسب به شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/67651" target="_blank">📅 14:08 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67650">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش ها از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67650" target="_blank">📅 14:04 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67649">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
🇺🇸
مجدد حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/67649" target="_blank">📅 13:58 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67648">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
🇺🇸
بندرعباس صدای انفجار شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67648" target="_blank">📅 13:52 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67647">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
شنیده شدن صدای چند انفجار در چغادک بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67647" target="_blank">📅 13:47 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67646">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
کانال 12 اسرائیل به نقل از یک مقام اسرائیلی:
طرح‌های تهاجمی آماده‌ای علیه ایران در اختیار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67646" target="_blank">📅 13:25 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67645">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری فارس:
دقایقی پیش مردم در بوشهر صدای ۲ انفجار شنیدند که هنوز خبر رسمی در خصوص محل دقیق انفجارها مخابره نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/news_hut/67645" target="_blank">📅 13:13 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67644">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
❌
چندین انفجار در بوشهر گزارش شده.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/67644" target="_blank">📅 13:07 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67643">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QT6okWsq2ZHRH0xI8TxRsH3DHGqFLdnqwod3BsDmF2b1h7asR007_jp6eCSknnElIK9zNTQb6sddb1EwaYjdkezNG3Ug5ssU-hCIKeg-vtpmLaGXO5wIUVOx1FbfHwvnBMHm1iOl52jiZ6UJF42q1i8ob4QpPzyK59tAJSZDHt_LwobVzyQlC4L48WoQ8u7Bx34pPwU4CTIeIMHMSq-gLtbrhAiBD0hzJDGdAXHR8qqBWRQXsr1hONa29aqkzi_rdQ7SAib3w-qs1XSCv0gcqml6YChhG_e9uJnTkV6ymGWQxdLh4m0EDgcQ2WAG25lLxB29SxrgMzGHPP7DYOAjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
اگه براتون سواله که چرا آمریکا انقد زومه رو سیریک:
سیریک یکی از نقاطی هست که بدلیل ارتفاع و موقعیت جغرافیاییش اشراف بسیار عالی به تمامی ورودی و خروجی تنگه هرمز داره. توی روزهای عادی و وقتی هوا تمیز هست شما راحت تا خصب(عمان) رو با چشم غیر مسلح میتونید رصد کنید. بدلیل موقعیت نسبتا کوهپایه‌ای منطقه سیریک نیروی دریایی سپاه با کروزهای ضد کشتی بیشترین حمله‌ها به شناورها رو از این منطقه انجام میدادند و سریع متواری میشدن. تمامی تجهیزات ثابتِ راداری و موشکی توی جنگ ۴۰ روزه منهدم شدند ولی نیروهای جمهوری اسلامی بصورت چریکی و پارتیزانی از سمت سیریک هنوز اقدام به پرتاب راکت ضد کشتی میکنند و البته خب سنتکام هم مرتبا با پهپاد و ماهواره تحت نظارت داره و مرتبا پیداشون میکنه و میزنتشون.
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/67643" target="_blank">📅 12:43 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67642">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9Dpy347Hrn4wJyRCjDGY6gAkdOK0N27iDLJYYT1OkaWXuCzfK1BxQlenr1cKFumlmsUNP-C3ZCRtAZ2hdwmsIOZrM-LDnRI9BV9KxEturhM2SqpgYtH3QkX90Ny-th5kFu2JDzfkywDhGogQd-P6mA476Qj0VGCkmAwrSr-moBfs8w_0TEIilBWvChIaEZA1fc4wKx2dRSpEJgBm1P3CL6bjNzosDQbN4Dl6SEAVjeNe4Mp0Bq0DvPop6BvH_K-eC6v9-bsTKz5jnQ_VwXwodE9AEKVO4oD_y56ZbIIBkIy5RMvSxRphNOJ5mRCnJxG_WGXyDv8SFPu2kK8nambXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیانیه وزارت خارجه جمهوری اسلامی:
@News_Hut</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/news_hut/67642" target="_blank">📅 11:49 · 18 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67641">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🚨
چندین انفجار در بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/67641" target="_blank">📅 11:33 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
