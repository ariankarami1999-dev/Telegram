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
<img src="https://cdn4.telesco.pe/file/Dg0WRgoEdKlhP7PkANmk30b2tUpDP2uTWXcP_2g0PQTAYNGRLZ7wxRcxfFbDvfL1GQKUek1aiZLQ5k0KGbIZEt6qHlKI7LMcIQBpHpQQc33iAykfZdNp_RbMrFsK8bDl7zaxL00WKL1Zn0DWsZKxfIjvq3uddGLuQu34st6Ht89nbr8_HRYSR5cexZ0ysWLKSXxR8XjqF62fPMobkncO3UbPIjStevrr2E3c6DJrarmNqfVPMC8dcQjjvWMK_3td4_rNaadVH5_rzqctO5bIz8PAoBqU9JvcSDfDoDk7VqjqIwvXIAxZpF60KdXmKKOCtk2bGMXo3qxiDWne47L4Wg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 106K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-29 09:03:26</div>
<hr>

<div class="tg-post" id="msg-71923">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d403914707.mp4?token=k1UZwAOPtuRiJ1VrHnZbM6ADR0Ly280YcJMPIrDH0QLGnf4ADVXTLDl1ZpgQ9vsat1JiC7t8sMH8PnOwLpZyFbzJ8B2BdPHCWazTW1b6y2g92l3rOQ33tjLWgf0oT4N2MijPmX5NWQwxMktc4GYSul9t3NVf_VSugdNXTF_2MlGEYzBTyomLyoNnPubeYGxXc8c6sPuL8Rdu3ZrJIQMkXzate2C2yxJZa4ul4upTHxzOV6UsYS7a1v0IYeeDV7Xz_6489Wyfye1WLrfjnyj4sTP7R7bBSEfKARm3ZTDFy-LpZM0nJAck9WEyi7c6vCnYr36OIZu49OoXiXGhY2hkrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d403914707.mp4?token=k1UZwAOPtuRiJ1VrHnZbM6ADR0Ly280YcJMPIrDH0QLGnf4ADVXTLDl1ZpgQ9vsat1JiC7t8sMH8PnOwLpZyFbzJ8B2BdPHCWazTW1b6y2g92l3rOQ33tjLWgf0oT4N2MijPmX5NWQwxMktc4GYSul9t3NVf_VSugdNXTF_2MlGEYzBTyomLyoNnPubeYGxXc8c6sPuL8Rdu3ZrJIQMkXzate2C2yxJZa4ul4upTHxzOV6UsYS7a1v0IYeeDV7Xz_6489Wyfye1WLrfjnyj4sTP7R7bBSEfKARm3ZTDFy-LpZM0nJAck9WEyi7c6vCnYr36OIZu49OoXiXGhY2hkrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده‌ رضا پهلوی:
«امروز این (جاویدشاه) یک شعار است .
یک شعار پشتیبانی و من از صمیم قلب سپاس گزارم.
کاری بکنیم که اون روزی که صندوق رای در تهران برقرار شد تبدیل  به رای بشه , نه یک شعار .»
@News_Hut</div>
<div class="tg-footer">👁️ 447 · <a href="https://t.me/news_hut/71923" target="_blank">📅 09:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71922">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71922" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/news_hut/71922" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71921">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Btyb_i51yzMI91wGGzc7CbxpCX8Zk5it3OmY2HKC4NlKx6SAgSWEKecJV97mkZiFIj7SmvW8a8dCPUJvLDKPZtbbcw-McPCoDMXnYtOsYY3Ea7MFBtKT8Jh4sCc-0E58x0K-7fEqrNTOiRtfNWLgV1kAm2XK6TuQeWw1oANbFbFpOpx1TLtz0t_An0NkbAL4Uu4dWSyHrpXscdCotwsVwJeLoHONwFZVrWGt3b_YHtJRYcUZSZZY4j0brBri3gWJhSpM9EzHlKpdU_H1xhV2MimqimBCXTFgBupHJpfNfZgCFlx9lClmA1JPSOhk0qXgaQ8Rjm4neabNUTlhqhG22g.jpg" alt="photo" loading="lazy"/></div>
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
سرعت بالا، طراحی حرفه‌ای و تجربه‌ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/news_hut/71921" target="_blank">📅 01:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71920">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VkgZ9RWaonZx2dGy_ks25dQ-S41q2j3q2vjuvB7P3YbtanupyvPRKUD8PYch7SOVtrkoASn5mEMa3a6pyycQqOxbpoRbmQf7Gwr47cmFXKC3zkEmynfJTwySlSYLE9yHdZuB9-5BcYRWmOFrduVgwLuC9FT4qfRUShTaRwaPag5SC2rAhpOevdvBSFOmc7AxSdAkux55hc9PgYxu9V7O1oIj7zP4QqNPtxa3YYvBVOUHFu4HGyQAr-WnIyXPs92kQsaldzwxb8_eM6qXH6yhWWD6h0Fok1D9Q6R1S0WgQLWPW60O06bIhlxyO8bdAA84BVJrnaANbUUH-llwHxcUMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت امور خارجه آمریکا با توجه به تحولات منطقه، هشداری امنیتی برای آمریکایی‌های ساکن خاورمیانه در خصوص احتمال بسته شدن حریم هوایی صادر کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/news_hut/71920" target="_blank">📅 01:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71919">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هشدار جدید آمریکا برای شهروندانش در خاورمیانه:
بر اساس آخرین اطلاعات منتشرشده، عربستان سعودی، بحرین، کویت و قطر در سطح «۳؛ تجدیدنظر در سفر» قرار دارند.
آمریکا در مورد عربستان نسبت به خطر حملات پهپادی و موشکی، درگیری مسلحانه و تهدیدهای تروریستی هشدار داده است.
در بحرین نیز آمریکا به تهدید حملات پهپادی و موشکی و اختلال در پروازهای تجاری اشاره کرده و سفر به این کشور را در سطح «تجدیدنظر در سفر» قرار داده است.
هشدار آمریکا درباره کویت نیز همچنان در سطح ۳ قرار دارد و از تهدید درگیری مسلحانه و حملات پهپادی و موشکی به‌عنوان عوامل اصلی این هشدار نام برده شده است.
در قطر نیز وزارت خارجه آمریکا نسبت به تهدید ناشی از درگیری مسلحانه، اختلال در پروازها و خطرات مرتبط با وضعیت امنیتی منطقه هشدار داده و از شهروندان خود خواسته برای احتمال تشدید شرایط آماده باشند.
در همین حال، لبنان در سطح بالاتری از هشدار قرار دارد و وزارت خارجه آمریکا از شهروندانش خواسته به لبنان سفر نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/news_hut/71919" target="_blank">📅 01:46 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71915">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/uRxC05GfOwnxHUR5bcqEYl5m9k2APTweOub0XJdDb3zP24iW48tzf3AJinCYdMXKp_MFd_eHtQby-ZvhK-w150Zkqmsy9C34Ippcv88epjflvh_geL68RNwtgJgo8KmAeGpDz5T6DtU5VbTJp894uW6ONyuE-Cop4LkfXg97-r04ZnJxE3X8ah4s26K57EePne8GaLf0DYC3BPb_p0Qm3qJWahUcZlsDfbZNJzHZk1gEX1CFADVNlopdtxXVnsTYizOBR-9dfWwmYe1B_ZBFdEAnk6FvxRhk8kPvTpejUaIOAmDBcP3w4rKbG3_aOTTj8k4GpppJ-4s2RMHu7-dyNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Lqb8z38SkhdXEk6Oy2v7vINpJb4GUmO5t2hSmLIlXaXSW4vQiuhpczJhTVXkyKrH_N8IB-5voSr9TzlQhw5ziMmX-lYxTWqkR2lF6EKKVrmo7iOf-J7PLZbEhBIq_QpHslrtrYccgNxAkyBX5oHY_mS44yd9VrDvbcUwv8Dnu4AE9iqkXdA4rRP8M2uKcFwV3ozDOYswKRjC9AKgw6GyYvU7AIwyszI-XFQowCXgNW1Bb0zBwY1igXUvYCYJcVLwwMruJXoXVJajDXel-3r6OA2Pzhf9V4ZAEfretMaSex1iR5BnxQtoo0syNyj9gHGUXXBPTs4hfR7iteyFMKn_rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7ac25f2861.mp4?token=Lqb8z38SkhdXEk6Oy2v7vINpJb4GUmO5t2hSmLIlXaXSW4vQiuhpczJhTVXkyKrH_N8IB-5voSr9TzlQhw5ziMmX-lYxTWqkR2lF6EKKVrmo7iOf-J7PLZbEhBIq_QpHslrtrYccgNxAkyBX5oHY_mS44yd9VrDvbcUwv8Dnu4AE9iqkXdA4rRP8M2uKcFwV3ozDOYswKRjC9AKgw6GyYvU7AIwyszI-XFQowCXgNW1Bb0zBwY1igXUvYCYJcVLwwMruJXoXVJajDXel-3r6OA2Pzhf9V4ZAEfretMaSex1iR5BnxQtoo0syNyj9gHGUXXBPTs4hfR7iteyFMKn_rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم بزرگداشت کوروش بزرگ در تورنتو کانادا و استقبال فوق‌العاده مردم از ایشان.
@News_Hut</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/news_hut/71915" target="_blank">📅 01:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71914">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7zAwpgw9kSYdA2ya8azjYfaPZTF_583E7dLI5dxnPYq1AR82Zi1oI7OWQDvYOcpq6A-FjFRNf5HYCE5jjHfFyi5C_vdHWscWmNeV0_oxg6T6pqiS7FbRH-IIVt_6zpseSdJHPPX3hPvoA5sm73fyr6JjJDSNRhbDWUOIl1oY1z_YekzgkBJsdmi0iMeTTS3i59XnVaQRdgKqlJKIvd1MBAV4jMhm5Wya8HgWTA2EMe-y-GItSig77RXdQCUENHp3N1mrDjLH1TpEwMxvYg6B_kOF-3CHq0loLNr_p8lF0GtzecJ0LKxGd66eXE69ctgqZUpAopkeQGUATqiNL5A0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:
ایران هفت شرط را برای آغاز هرگونه مذاکره به دولت آمریکا اعلام کرده است.
پیام تهران روشن و صریح است؛ اگر واشنگتن می‌خواهد از باتلاقی که خود برای خویش ایجاد کرده رهایی یابد و از گرفتارتر شدن در آن پرهیز کند، چاره‌ای جز پذیرش حقوق و شروط ایران ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71914" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71913">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=ZDHSjNN6tckvK-pD4vjbt1UVOn587G9vEKkEOYY22kMfYp2eSTh1fDOr11nf4UmPx5GfQPWIMhO3jZQtQC4awUshrza8NDtOM2cqkwFNBZkEe9V8O6h54HKajoVndAuu7Or0tvCdpqdWO_jiFQhmIeKy5hjTMiB5_aJTEXlkUBzyhlrBBGQX0ve_BRu3bFsH53TvIO7jcFH1N9zUdmkixJyS2uhsUf7RJO23IW2P6Hoeqc09p5KRv18xI9uwp6gL7v4pKirr_l64BrnrgoUQ8byDlTa9RiVmq9cr8LHA3Th11zeHg7sMMOS9Iat8duuK1OUmhaqVcwq_AolCTYxrkWpIkCdVbcYmZfjAoUDOQsCixcOBvu7TomMeOeEUhmHYfi9CLWSXBc4m_WlTaHGxBZOse4pSAOjfiCBY7e0wdxSaBNXrwpr4afU53gZOeIMfRXd2LP1lMb870nLFUGuQBPO13oi2kAz4lnwDKMB9AVjopE7_UPZ_vdTADTjevGc3VlawWclaV_eE47CnQSw-aVhwXNm4Zi-Ww136mWMq1jJGb3XwTtUZAleJ-d6fYbc-bxsF0YKqapwozm6SzjqrWtQob4DyKEbfodxFiKcLHnXE2iXFSJh4kOe6l4xCHXAw6ZnV-VUJQQylx-Dcvo_Rwl5e4oxr6BrxKXEaQeOhqjU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/654a3cad3e.mp4?token=ZDHSjNN6tckvK-pD4vjbt1UVOn587G9vEKkEOYY22kMfYp2eSTh1fDOr11nf4UmPx5GfQPWIMhO3jZQtQC4awUshrza8NDtOM2cqkwFNBZkEe9V8O6h54HKajoVndAuu7Or0tvCdpqdWO_jiFQhmIeKy5hjTMiB5_aJTEXlkUBzyhlrBBGQX0ve_BRu3bFsH53TvIO7jcFH1N9zUdmkixJyS2uhsUf7RJO23IW2P6Hoeqc09p5KRv18xI9uwp6gL7v4pKirr_l64BrnrgoUQ8byDlTa9RiVmq9cr8LHA3Th11zeHg7sMMOS9Iat8duuK1OUmhaqVcwq_AolCTYxrkWpIkCdVbcYmZfjAoUDOQsCixcOBvu7TomMeOeEUhmHYfi9CLWSXBc4m_WlTaHGxBZOse4pSAOjfiCBY7e0wdxSaBNXrwpr4afU53gZOeIMfRXd2LP1lMb870nLFUGuQBPO13oi2kAz4lnwDKMB9AVjopE7_UPZ_vdTADTjevGc3VlawWclaV_eE47CnQSw-aVhwXNm4Zi-Ww136mWMq1jJGb3XwTtUZAleJ-d6fYbc-bxsF0YKqapwozm6SzjqrWtQob4DyKEbfodxFiKcLHnXE2iXFSJh4kOe6l4xCHXAw6ZnV-VUJQQylx-Dcvo_Rwl5e4oxr6BrxKXEaQeOhqjU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن‌استار ایرانی ملقب به «شیر ایرانی» با شروع بسم الله و کشیدن علامت صلیب توبه کرد :
خدایا منو ببخش و از این آتیش جهنم دورم کن بعد این همه گناهی که کردم
بدترین انسان نیستم ولی بهترین انسان هم نیستم به همه میگم خوبی بکنن کارای مثبت بکنن
دنیا خرابه جنگ زیاده سختی زیاده اصلا سختی دنیا زیاد شده و سختی عمر اعصاب آدما رو خراب کرده
خدایا نه فقط من بلکه همه آدمای دنیا رو از آتیش جهنم دور کن
الله اکبر خدایا منو ببخش خدایا دنیا رو جای خوبی بکن خدایا جنگ ها رو تموم بکن
خدایا منو نجات بده نزدیک خودت بکن میخام آدم خوبی بشم خواهرام و برادرام هم میخام بهت نزدیک بشن الحمدلله
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71913" target="_blank">📅 23:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71912">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkQNzfFvMwqde7wgijebXV8K0YQRPktke61pbKm8UW8E8Rvo5nB3do89vfoOouaJqhxYNeK-PNwHbhDFgjr9WIrcj96TMbZuV79rL2sFxfgLL4ox97FfsrGepOu8YjytkRNrBtSh_NI4l8eN5EnpW_rpCRy0UismxFa3RfBdeT05bvACZydyBfsdOIhg3eGowVhrK8dXXn2ceSFxVGYEbRM48hLHZeExx5iDxRmX0tM3TI-N0rng3Ehk2u9cxuJDbbzV9tj1j_3cN69vuXl32D34h2w9eq_nzaJEvRzuMTpkTCjaSq-rcvft_6BKAZm0bm-AilGWDU6FLGQMtNw1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ بعد دیدن این عکس دستور حسینیه شدن کاخ سفید رو صادر کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71912" target="_blank">📅 23:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71911">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZwxYkNYC01RcMSxldV2zYj065EoWc3tj6yd1AJJfOQb6Uk0WX7CN6vLTQPTcxHyuSoMD-UVixoYW_lwVP-PjhnlW5u-dr5psjoqmxkOKGEJ-CjG1PFGSAMNa77TftzSBsfAlwemOcrSmuoDDUu3L3UIjKAhnEJ-6OvwH2WtmPr1NploxULX8RkSMtMOp6QsxpZXYEHUDcyc1BvL5dOsAOLE6nK_jWqmYdGquRG-y0cHbZDw-FiOAMfvgsocacztYUETcMtXnO5Fma3ms4N0oFAoxoLhU3y3h8bIaUx1r1RGGHOgqxMb7m8nMyn0XGKCLb8Rs2b46G8BslyGJPpIVbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شبکه سی‌ان‌ان اعلام کرد که روز شنبه به دلیل ممنوعیت اعمال‌شده از سوی ترامپ، از ورود خبرنگارانش به محوطه کاخ سفید جلوگیری شده است؛ این شبکه اقدام مذکور را «تعرضی غیرقانونی» به حقوق خود ذیل متمم اول قانون اساسی توصیف کرد.
سی‌ان‌ان با تأکید بر اینکه «قاطعانه از تیم خود در کاخ سفید حمایت می‌کند»، اظهار داشت: «ما از انجام وظیفه خود در پاسخگو نگه داشتن دولت و سایر نهادهای عمومی، باز نخواهیم ایستاد.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71911" target="_blank">📅 22:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71910">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=pqhpcC_LTztpb_esvXSEOMm7WQ1xXMf_ajFARtZPOHPR1zHfJtKws3mKSqOSF8c1fMtklgaIBk7F4h-BCFFKDEF62nn7Q4yCeumODs8ergPyg3sxdA6lLPqTZtay7m1REWZk-Q4CYWF83K09xQQlP855jLreUrit71UBTH4HDpu9IXlbn0uGKo09eEktwwvC_IBrPX4iCY8sSP0EOLK5ydEeQPHQpO135YPTTCbzbV6ZBF9hZqunQ5rbNq472SMguHq7gYaU79LplZkxM_JZ-JqiJYmftP27RfIt6mnyQfdUiGbm98pWsYHm4KbEwP5lWl1CnDN6uMn_UHVULVQPHIfdqXijhOjfYXiheMJ_IX1_YB2161Ageijk6102oIIvmybmkLnvqotjoQiK47yNfXhe9SuE4R19BQI1Xh7oSbStw2w-KIQtM_icCbSwxfRoVbv6-FTTFWJP97oVauDDGMYhW15m2Lyx7TRKIcYFSHZ4EkK3IPokpqEgLui1l5P8KLp2WF5whQrbySe2zzrZmSdh8WmQE_ZKpfrdUE823jJnW-oV-g6zW05ffHo-WWe6bg3Iqa-E-_EzdSKBsU_rWcQZAtWuHMLI6fJ3sDX7Xb94VjCAGh2sRe1F13vj5NEXzgNuDk5m7I-WHIkjg8PJK7uPdCqj5AhdbwuM4EFp2CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/411c3a472b.mp4?token=pqhpcC_LTztpb_esvXSEOMm7WQ1xXMf_ajFARtZPOHPR1zHfJtKws3mKSqOSF8c1fMtklgaIBk7F4h-BCFFKDEF62nn7Q4yCeumODs8ergPyg3sxdA6lLPqTZtay7m1REWZk-Q4CYWF83K09xQQlP855jLreUrit71UBTH4HDpu9IXlbn0uGKo09eEktwwvC_IBrPX4iCY8sSP0EOLK5ydEeQPHQpO135YPTTCbzbV6ZBF9hZqunQ5rbNq472SMguHq7gYaU79LplZkxM_JZ-JqiJYmftP27RfIt6mnyQfdUiGbm98pWsYHm4KbEwP5lWl1CnDN6uMn_UHVULVQPHIfdqXijhOjfYXiheMJ_IX1_YB2161Ageijk6102oIIvmybmkLnvqotjoQiK47yNfXhe9SuE4R19BQI1Xh7oSbStw2w-KIQtM_icCbSwxfRoVbv6-FTTFWJP97oVauDDGMYhW15m2Lyx7TRKIcYFSHZ4EkK3IPokpqEgLui1l5P8KLp2WF5whQrbySe2zzrZmSdh8WmQE_ZKpfrdUE823jJnW-oV-g6zW05ffHo-WWe6bg3Iqa-E-_EzdSKBsU_rWcQZAtWuHMLI6fJ3sDX7Xb94VjCAGh2sRe1F13vj5NEXzgNuDk5m7I-WHIkjg8PJK7uPdCqj5AhdbwuM4EFp2CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب حامیان حکومت تو تجمعات شبانه شهر بابلِ استان مازندران داشتن دورهم «کلاغ پر» بازی میکردن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71910" target="_blank">📅 21:53 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71909">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ritkojX6Rm8zfHmJ_bSG8VDis8tSW7S1RMdgNaRyFlsYSHEHuMD8mUhL6jsFGeRvyEo9Yoclc7RBn7Ph7mEhpEzvYlcf4YzPEGEfhd_HSRHcOS1HN-p02Q-CKgeC87iQpDkatLrcwkp7cCKcupjh64Kf6J8ap9n7NYxdTu2yIy6WNaCFsNK3Efvj0upsr4CXEGtTLFE4GXCFJy1p1oIDyRUpdErLf_UKHDXzWIb_Zx6hUNTrPrAGoROLcUjRsAvxfU2-ScWV6XylZ8A-FoU3gS_JKTUlQMUWDYjurnD068_gaWXCwpcif-TVR5augkr-3WckRJScBxtUv8IgR3HMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:نام فعلی هوش مصنوعی چرته و از رأی‌دهندگان می‌پرسه که آیا نام «هوش مصنوعی» باید به «هوش برتر»، «هوش فوق‌العاده» یا «هوش متعالی» تغییر کنه یا نه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71909" target="_blank">📅 21:14 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71908">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=lqE90YOr6cbo9i2vTmdr5DWKEtVh38nUKI08S5RWb1IfD3ILnRyh84LzlCqkT-0TO403uVWeSLxKmEgoXMF8-gsolgQfxVELyMkO1DP_nDy2L7sVyGfwRcxoBMjuiJwiCaQi-5onh_J4_QNSMl-8GvyGTEl1yF0iGOjycErdSmstlt-Ke5X--SfOH6xxNJNlTifrZWXOcr9J_b_him0rbCXqlG79LYaEv4xaGd8bQcQKCQcdRkYsl9h-7DASMK6VCvCdxQTRNZOnFhkfqky7gdvnLrnZCatQunpBGqACGCe090yI3oKd5NkOdMoNuoQlw6arFgK8Qg8FlmprcmCdFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c50e52af4f.mp4?token=lqE90YOr6cbo9i2vTmdr5DWKEtVh38nUKI08S5RWb1IfD3ILnRyh84LzlCqkT-0TO403uVWeSLxKmEgoXMF8-gsolgQfxVELyMkO1DP_nDy2L7sVyGfwRcxoBMjuiJwiCaQi-5onh_J4_QNSMl-8GvyGTEl1yF0iGOjycErdSmstlt-Ke5X--SfOH6xxNJNlTifrZWXOcr9J_b_him0rbCXqlG79LYaEv4xaGd8bQcQKCQcdRkYsl9h-7DASMK6VCvCdxQTRNZOnFhkfqky7gdvnLrnZCatQunpBGqACGCe090yI3oKd5NkOdMoNuoQlw6arFgK8Qg8FlmprcmCdFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تست اکتان بنزین در عربستان …
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71908" target="_blank">📅 20:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71907">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzONjUlKW5dUrqwBhZQ8USEH4E6NgWzSS_r7MnuRuiZMVbk9C8L6ffQMMMPXRjUifj7jHIXFTK6K0BGI-Dm8dWMBzc0ZIsAmvFApLkKdKvQaMSx1IUqcrGaMP31LmJ4Orb4LQtvivWjQoVKQY8rZAVCVpVZ-tK0NBM3xsRswmI0OUjAuTNFoFvceAKSrFw17FeXS48mZ10FJfEIgEoWp98VVUBUtGh_LMIZQUIIfD7kvMad8G37QdQBxlEbwXiRnQL3xQ_Hmu_9GXNM_Ub_5RBp5phhJnSRV33GW-yFlG2STeIRYLUHsPCVnNabSrkHvNEY-2ANT0LshCwNJo2VhVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان هواشناسی: طبق پیش‌بینی‌های فصلی، بارش پاییز امسال در مجموع فراتر از نرمال خواهد بود؛ تمرکز بیشتر بارش‌ها نیز در غرب، جنوب‌غرب، دامنه‌های زاگرس و بخش‌هایی از البرز پیش‌بینی شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71907" target="_blank">📅 19:52 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71906">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، در گفتگو با شبکه الجزیره اظهار داشت که دونالد ترامپ، رئیس‌جمهور آمریکا، در ارزیابی خود نسبت به ایران «دچار اشتباه محاسباتی» شده است؛ وی همچنین بنیامین نتانیاهو، نخست‌وزیر اسرائیل، را به تحریک برای آغاز جنگ متهم کرد.
رضایی با بیان اینکه تهران «برای یک جنگ قاطع» آمادگی دارد، هشدار داد که هرگونه حمله بیشتر، با پاسخ‌های شدیدتر علیه پایگاه‌ها و منافع آمریکا در سراسر منطقه مواجه خواهد شد.
وی خاطرنشان کرد که ایران نقاط ضعف ارتش آمریکا را می‌شناسد و برای مقابله با حملات هوایی این کشور آمادگی بهتری دارد؛ ضمن آنکه اخیراً یک موشک ضدکشتی را در نزدیکی یک ناو هواپیمابر آمریکایی آزمایش کرده است.
او همچنین افزود که ایران به این نتیجه رسیده است که پس از خروج آمریکا از یک تفاهم‌نامه، باید راهبرد خود را در قبال واشنگتن تغییر دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71906" target="_blank">📅 19:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71905">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">رضایی، دبیر شورای امنیت ملی:
رایزنی‌ها با میانجی‌های قطری و پاکستانی ادامه دارد و ما شرایط خود را برای مذاکره به آن‌ها اعلام کرده‌ایم.
ما با میانجی قطری در تماس هستیم؛ او شرایط ما را برای توقف جنگ به واشنگتن منتقل کرده است و ما منتظر پاسخ ترامپ به این شرایط هستیم.
شرایط ما عبارتند از: پایان دادن به جنگ در تمام جبهه‌ها، آزادسازی منابع مالی بلوکه‌شده و پایان دادن به محاصره دریایی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71905" target="_blank">📅 19:25 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71904">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNmANSvseZgXSPmWiRw_jxIQgRIC8Ik3SXBdIta2yfqqqhqi-VcvhMgjZfRhvx8eW4qzfbkEgjG2o83rdLvutLRtTJm9Sh6iUWY67M4VwYsyEmYd8ER9topIw5lGPK_2vb_dEB5j7_Pbw1IULyfKoE8y-9HZG0GAEry3owslAGkxsswqSyTUA8ZwiWxb1_aGBdzYzGqJ21ucGwwlOzrjq2EhUD6dI9VhcuP2eOMMi6jkbf0421eXwmQJ2Z0Q-teWmgANiksOchDqR2SRBDDGdkf8vHM4fY0abk-G28rsUiR977kiqwiQLYAZC8OI9LRJlOj4-Cd8sT-2Lb82Wvg2hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی در گفتگو با الجزیره: اقدامات آمریکا و اسرائیل ممکن است ایران را به سمت خروج از «پیمان منع گسترش سلاح‌های هسته‌ای» (NPT) سوق دهد.
رضایی گفت که ایران هنوز تصمیمی برای خروج از این پیمان نگرفته و افزود که این تصمیم به اقدامات آتی واشنگتن بستگی خواهد داشت.
وی تأکید کرد که ایران همچنان به فتوای رهبر فقید انقلاب اسلامی مبنی بر ممنوعیت سلاح‌های هسته‌ای پایبند است و دکترین هسته‌ای خود را تغییر نداده، اما «نمی‌دانیم در آینده چه پیش خواهد آمد.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/71904" target="_blank">📅 19:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71903">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=oOcNcLVduYBqv1n038tVvMvM9l8koIpz-4TqO9r_oC7sEs1UdNapKqoC7Sm_0krCHdWo-9Bc5P0iZTmwlZ16zaf7_v9-ltuDF0uuli6TU5jcpqR7q5FCxC_kJKirfhcUnxFjWSv6GNxMw2xHdGV5OsrhsWJCpBgcLduJmmOPgvhmomjZgXyFqF0XXpbwHE0kztf2t5JMA0m3jCCCK8IEcPT60xMhlM8qN6UvbucTXc1oJgLkg3zEaUA2lID80KNNmcpt8RLAkAn38TZTPX1FGy-YXxUEnZMtic_-28__bQrE1mjhBxOsHebjpZehBYCfwbWDvgw4Zp-s545i6Lwdpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7703ac3568.mp4?token=oOcNcLVduYBqv1n038tVvMvM9l8koIpz-4TqO9r_oC7sEs1UdNapKqoC7Sm_0krCHdWo-9Bc5P0iZTmwlZ16zaf7_v9-ltuDF0uuli6TU5jcpqR7q5FCxC_kJKirfhcUnxFjWSv6GNxMw2xHdGV5OsrhsWJCpBgcLduJmmOPgvhmomjZgXyFqF0XXpbwHE0kztf2t5JMA0m3jCCCK8IEcPT60xMhlM8qN6UvbucTXc1oJgLkg3zEaUA2lID80KNNmcpt8RLAkAn38TZTPX1FGy-YXxUEnZMtic_-28__bQrE1mjhBxOsHebjpZehBYCfwbWDvgw4Zp-s545i6Lwdpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: کنگره در چه مقطعی وارد عمل شده و به مسئله جنگ با ایران می‌پردازد؟
رئیس مجلس، جانسون: ببینید، دولت این وضعیت را یک جنگِ در جریان نمی‌داند؛ و واقعاً هم چنین نیست. آن‌ها در تلاش برای به سرانجام رساندن یک عملیات هستند — عملیات «خشم حماسی» (Epic Fury) که موفقیتی عظیم بود.
به گمانم در حال حاضر نیازی نیست دموکرات‌های لیبرالِ مارکسیست در کنگره بخواهند به فرمانده کل قوا دیکته کنند که با ارتش چه کار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71903" target="_blank">📅 18:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71901">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=beJ0ukUELKF9xM96HSbh6az1F0azkl1OM0lzneh89RT05op2yPidEZfGR5YELrCyGxqx-4aLvASVikKsFZx7PVX-4rPZ-O8pgOapVMVj5cx5OBvS162glxiulTt_3_TZgaPJabQ2FXKK7-y_2BI4Y5t7s76bHe54v7G7RztNPOMKEZL1StrJ1D_9x6IAlqai6uwHmiTlTuxue2HKhQqH_CF8gmi3BgZn13wQREXvsSI23NgF0VQqHbgOmTtzwnWbly-L4hKNzM1wR0aD9_vRPTNDKLimIv2FZXXFMKrYxxbEIeLYjBVYyc5gXWbfC2qtZeFRY7ODcVwYavcNee4EGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75801e50d0.mp4?token=beJ0ukUELKF9xM96HSbh6az1F0azkl1OM0lzneh89RT05op2yPidEZfGR5YELrCyGxqx-4aLvASVikKsFZx7PVX-4rPZ-O8pgOapVMVj5cx5OBvS162glxiulTt_3_TZgaPJabQ2FXKK7-y_2BI4Y5t7s76bHe54v7G7RztNPOMKEZL1StrJ1D_9x6IAlqai6uwHmiTlTuxue2HKhQqH_CF8gmi3BgZn13wQREXvsSI23NgF0VQqHbgOmTtzwnWbly-L4hKNzM1wR0aD9_vRPTNDKLimIv2FZXXFMKrYxxbEIeLYjBVYyc5gXWbfC2qtZeFRY7ODcVwYavcNee4EGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای اسرائیلی به تخریب خانه‌ها در «میس‌الجبل» و «المنصوری» در جنوب لبنان ادامه می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71901" target="_blank">📅 18:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71900">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=ec1FUYDnk0_AKcV26Af73mvY2GToWqqqjpXsW3fYWYT2MzveeGv438SOor4AwiBdw6hMpidGRDQK0SrxnJY4oeoeFWwahPX6LIj8nJke66xhcWxgDL_WDg8_Uy8Ae4ZzeSVwrbmf4MqFRUFh367jAbDi1n9mq0Rq0pme58tOrY-TwcJjfXl1GbUlEo_IjhngWoMnTeKgk1sT8a2WXKHOjPT1Cz8GY_Shl3MrRj1tcUoNhbWbANwx_9f_oX0O_lVa2YvFluiVlcsXIOpWLg-Y-tzZmRjKxAAuCdWKLJ54lPnJen1jIWqu3YuhJVxtwg-YG_LRT9q5p228j16nOGyH2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8be83e9c35.mp4?token=ec1FUYDnk0_AKcV26Af73mvY2GToWqqqjpXsW3fYWYT2MzveeGv438SOor4AwiBdw6hMpidGRDQK0SrxnJY4oeoeFWwahPX6LIj8nJke66xhcWxgDL_WDg8_Uy8Ae4ZzeSVwrbmf4MqFRUFh367jAbDi1n9mq0Rq0pme58tOrY-TwcJjfXl1GbUlEo_IjhngWoMnTeKgk1sT8a2WXKHOjPT1Cz8GY_Shl3MrRj1tcUoNhbWbANwx_9f_oX0O_lVa2YvFluiVlcsXIOpWLg-Y-tzZmRjKxAAuCdWKLJ54lPnJen1jIWqu3YuhJVxtwg-YG_LRT9q5p228j16nOGyH2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیت هگست، وزیر جنگ، در حال انجام تمرینات بدنی صبحگاهی با «سپاه دانشجویان افسری» دانشگاه تگزاس ای‌اندام (Texas A&M) است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/71900" target="_blank">📅 17:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71899">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">دریاسالار برد کوپر، فرمانده سنتکام:
بیش از یک میلیارد بشکه نفت خام از سوی شرکای ما در خلیج فارس از طریق تنگه هرمز ارسال شده، در حالی که ایران به لطف محاصره آهنین ما، حتی یک بشکه هم صادر نکرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71899" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71898">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71898" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71898" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71897">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9GQhYWoPG7opZe6Nvqs975y73sJ_dx_tWPo1HbisXhEHrwE5N6b72V-X9_O4VIXNUescwkDaWlnWGTgTmBepCsiY1cre6gVb7nPa7t9na5eXqp8Gt0-Ha8v04xiOdbKCRfQhb4njb2BkFVjXYQr0SIXeIGIuhRAGB6k1pmJZb-zzvtfBNPvFV7zS00_ZLtSUXlpB3bnig-0LdZwZz5LVq19DVIcM4HHI7wINd6RDCQ-DYQRWnvk6Gc4nPUKBwvOjjsTs-jhNxHae86zj_Dl6ZO7k0jV55l6RC1XlbMHcAS_q382_8xVs9TtRuphuPnGymITOLB6Af5OpyRypoT_vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان‌انگیز  بارسلونا
🆚
سویا
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
بارسلونا: ۵ برد و ۲۵ گل زده
سویا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ کل زده
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71897" target="_blank">📅 17:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71896">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=OfE8wbOJTMerljbxhBsZu0q0MpeteIkmyJ9NrQiInIOSHH8jA0fFRt7gRkhOQBI2GLcf7zcTc2rhhXUh448M8S2HxMGidOVPdJnBPKltFEfVzt_ss56k5YrlCjoR27SAihO3MHXhcbONZILB4c30pJpcNJuRFE0KIRdip5KTXarqes5VsGmYd_7YwN9C5_eAcWmMRZ-_YEo6Zrs1XPB0IiayW3D7v-hk-9iQwzPu46-i8Q1Cv1ijWm_qpZncOIzrP6UYHSvo5FbMLx-rYO3_f7_tfGDrnaTMXAUyH9fN2TDWxjQM-CfaWjoby3YmeyBSAK8tueElA014czzrCpLBCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7687234b2e.mp4?token=OfE8wbOJTMerljbxhBsZu0q0MpeteIkmyJ9NrQiInIOSHH8jA0fFRt7gRkhOQBI2GLcf7zcTc2rhhXUh448M8S2HxMGidOVPdJnBPKltFEfVzt_ss56k5YrlCjoR27SAihO3MHXhcbONZILB4c30pJpcNJuRFE0KIRdip5KTXarqes5VsGmYd_7YwN9C5_eAcWmMRZ-_YEo6Zrs1XPB0IiayW3D7v-hk-9iQwzPu46-i8Q1Cv1ijWm_qpZncOIzrP6UYHSvo5FbMLx-rYO3_f7_tfGDrnaTMXAUyH9fN2TDWxjQM-CfaWjoby3YmeyBSAK8tueElA014czzrCpLBCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه ده‌ها هزار نفری جانفداهای عراقی در حمایت از صدام حسین دو ماه قبل از سقوط رژیم عراق (۱۵ بهمن ۱۳۸۱)
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/71896" target="_blank">📅 17:35 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71895">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Wex88sT9wMdUAqdBZiVC3lZUYImn0_-0f5Bv3-GPf0AY208mu60XRxBDgqYxNMK8OZJ3fXmtE5peoPCFaPqiI3sJpDszThJMUlLM7Dlg6sDEy7X5uAlGGCuKVBOzUxYLlp-x9IyJrpwka5zKDVEOGGaynl7EC5HvSLenBzXmmy6y47BYLhN--F5ZONvJADbe8qNcMqm9kwdrhFzX3Vao-jaLj1zXS5pHVrA_SpGWk-wesTDLc233vRPLjWCHXqzH6OeVyjd7LxsT5TME327DSU6pi6jVsSDzHDDBvqkpYE6zYIm6478stWMbrOBOS5bulVEANDMRhQaFf16USYVqGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f42ac1c41.mp4?token=Wex88sT9wMdUAqdBZiVC3lZUYImn0_-0f5Bv3-GPf0AY208mu60XRxBDgqYxNMK8OZJ3fXmtE5peoPCFaPqiI3sJpDszThJMUlLM7Dlg6sDEy7X5uAlGGCuKVBOzUxYLlp-x9IyJrpwka5zKDVEOGGaynl7EC5HvSLenBzXmmy6y47BYLhN--F5ZONvJADbe8qNcMqm9kwdrhFzX3Vao-jaLj1zXS5pHVrA_SpGWk-wesTDLc233vRPLjWCHXqzH6OeVyjd7LxsT5TME327DSU6pi6jVsSDzHDDBvqkpYE6zYIm6478stWMbrOBOS5bulVEANDMRhQaFf16USYVqGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه آخوند تو صداوسیما :
اگر یک
قو
با
لک لک
ازدواج کنه بچشون
«قلک»
می‌شه
اگر یه
دارکوب
با
بلدرچین
ازدواج کنه بچشون
«دارچین»
می‌شه
اگر یه
مارمولک
با
لاک پشت
ازدواج کنه، بچه‌دار نمی‌شن براشون دعا کنین
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71895" target="_blank">📅 17:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71894">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QzOdNu2lj-6rXeMcFoA9VZp1V_KIFO0BkHv4rqc7ltHWFWLKYZngtbQrXTnG4YyXGGg2Hy9y2LFyOe6uN8kqQM0ZiooEy51BzCsIOsSUon0U549rfxi1vPLDR4Q-vKnbA7gMRUUAG91bChGmt3loF02EcSysdyWYWJQPDhh1RCxHArb4PJ_JbbCHBot9T8B99-IeFbxFAelvMlLYFaOFyt0rAd9-cIvFvICMaSBPns_oCdI0MoxtEVWIkEWbCvtklGkHR9cXFQJD-2u_RY3Gbb2Vwv3irEbVs1zycs3l-CwfTqj9yCxWng3HsIJ-E1Zf6yFTXaW2B5b83tb_UlWpQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنتاگون روز جمعه ششمین مجموعه از اسناد مربوط به UAP/UFO (پدیده‌های هوایی ناشناس/اشیای پرنده ناشناس) را منتشر کرد که شامل ۷۱ پرونده مربوط به بازه زمانی ۱۹۵۲ تا ۲۰۲۵ است.
این مجموعه شامل ۵۵ فایل PDF، ۱۵ ویدیو و یک فایل صوتی است که ۶۴ مورد از این ۷۱ پرونده، حاوی بخش‌های سانسورشده (حذف‌شده) هستند.
در میان این اسناد، سوابقی از یک برنامه نظامی وجود دارد که پژوهش‌هایی را درباره موضوعات غیرمتعارف — از جمله پیشرانه‌های «وارپ» (warp drives)، کرم‌چاله‌ها و گزارش‌های مربوط به آسیب‌های وارده به پژوهشگران در پی برخوردهای احتمالی با وسایل پرنده ناشناس — سفارش داده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/71894" target="_blank">📅 16:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71893">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=le1TCrsP2ZvLP6DyaCjQchYABN-ARjOnyt8NStE7mDd5rMs-A4eWbamlKDfK3EnMDeXgfgo0R3pHRUe-YbZrK450DFprlkySeA6dwThVhKnG_AGjp8mhwH61mDZ4dfTU16Q36VMTegmivbSSYNEBDD9vQM-So8oLV_gTk7r1AJj5LnTJRr19I6DFNr7h_FsmTsLRvW1zSulfnD6kVFAj1D-RQUREMYmr5sMOu_lXuzyqEWORN0d3yyMuyCdG49iVvTwInk-nm9_3JfNc5MtdQnEVrBcEce6oQ0ZW6t9ZaT-0lXR4XXoKsfj0uaT7V1k3utRK16BCFMEKYhLpOSKkOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4104492c.mp4?token=le1TCrsP2ZvLP6DyaCjQchYABN-ARjOnyt8NStE7mDd5rMs-A4eWbamlKDfK3EnMDeXgfgo0R3pHRUe-YbZrK450DFprlkySeA6dwThVhKnG_AGjp8mhwH61mDZ4dfTU16Q36VMTegmivbSSYNEBDD9vQM-So8oLV_gTk7r1AJj5LnTJRr19I6DFNr7h_FsmTsLRvW1zSulfnD6kVFAj1D-RQUREMYmr5sMOu_lXuzyqEWORN0d3yyMuyCdG49iVvTwInk-nm9_3JfNc5MtdQnEVrBcEce6oQ0ZW6t9ZaT-0lXR4XXoKsfj0uaT7V1k3utRK16BCFMEKYhLpOSKkOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
هنوز مشخص نشده که موشک رو کی شلیک کرد (به کشتی‌های عربستان و قطر) و توافق رو بهم زد!
وقتی رئیس جمهور تو عراق بود، وقتی رئیس مجلس تو مشهد بود، وقتی پیکر رو هوا بود؛ یه عده خودسرانه موشک زدن.
کشور داشت آزادانه نفت می‌فروخت و پولش رو می‌گرفت ولی یه عده بی‌دلیل به دوتا کشتی تجاری موشک زدن.
چرا؟ چون میخواستن شبکه فروش نفت‌ خودشون رو حفظ کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71893" target="_blank">📅 16:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71888">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aVWWDCNN-vZ2ukjYShV2xUT4Jv7YT3nHxIwQ0d3iygc01Obx6IltFrhqWGC_46WtfDlM6aSLiq5K3M0-31KkS2gRcSKou15qk5cepybmn9fLN6DPSO9qq2NICzLOZJygT_nFRG5XA3MpeiyUN-wefOcDam6QB3Ko8kdE8LDKZPtRGrHA1t45jiUMA_lnSZSxPIah00gPmPthfVro6uoBu1ITbvWSj6R51rtkbryOPsZzIvPzTZhzcQBl4JVK1lhfIFUcgxhbIUA-ZK32DmSBXQedVIlWp_dXfo3mrFr5svxsx8MpWS8_LHFEun50S3BpELTiinu-cDrEL0QvHNCehQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZsiIvjX3d6_t1AHZkbCd064-_Uiogf0kLFFXOg4Kase5Gr_71iO8dlmMeXupc3fNsCVvqRUOJT8tEjbgd_6faIazTApbKo9ROKNhiIgHh5CHoygJTBv4Tr660HSTOvA4pwC3J9C5PrFpBhjT1Xz6ybBRTtPbPpSzvmBdYNYeW0Y39oAtyWa5YBItHKQTfp4JDyAlbcrkXhxz37p4m4mkdDNDmuC7k0P3glmO-aH0hMWYHwanLh2YU-SgPa5CNQ_fcZ-U2oAHCvenfTIIMEdOq4nZ2RLXMQsid63HhCN2ffPdMJ_vIXaJBG1xKHQbyj2XesJGYIMaMGp9xfiNfSmmxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Pt9Xws_zCsd2xDM2z6IpUKuPstakXWG6mlrnrspwks446fCE39k5_ILUXbDHZ4r3XmvU_lcLsQvC4LLpftS0L9hnJ0Tffse81gSVWGBWiMF7S9aWz1lic_naGEYHxp8GTm0Mc4fdKHsg9JVOD2AjB1Qp8yrrRV8hs_7YLZB8GAwIHJMOUBo0SD5qOBG0wmHnknSae-GnW_ykuEuADQnflp4WE42felsPnrt8hzgXNuAL2TpTN_0pc-J9oqccTfgdczUN51WxdJXzQO-Oumqwv242buCzGXafg4KEIXOaW7Ntf-SPL_lv6KYlDFMSYCaCd4AebZk4EqPYZSeNsU7_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YtEPBmtb0edi7molDxe8t8Y_1vYQL150bGZebV_psEkCPui_q0Ez1LcFkMWr14tZ94cGZGvaAh1DIXQLibNeZ-uUNT2xslfOuoI1nRJEdcHr6uDcD7xkiDaRmL2NFqM5t4FRKNoWe45iRvGkuK9V60TvFXovg2y2Rcv3WChpRsnOgbivy0QtOwY3pqWPp-LKLTCIY5cs9FggNvC7o8HiV1Tf7DuR2ABC4Z7Bp6_W-nrkJCxXZg78d92r47Ii8ay740bWaHKj_2L4iV9fUhcAtCHCEmiYDwp_Xz0KYBGYYlvl9_26T1KhCcgl5Y9RkwtiLZWzW_DwdyOoHrHvJ6mTpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/t559uhyYee_NASDPFLWZcnnBuro2WRBMD45Z5ti9LJzI24b4XOlJ3IxynyD-j-SrL_pIAgI2kMvJsH5Ie1vfZdePszfcYfVsGbJjC2uFEWClL76aUrrL90D4wv8oB2lClSht4ChBqWfJUed1N9s9t8Ip1LpsK1ghVfHbAsGi91Bk_20Wta8FtuPCIfTi_Zp34R9SzX4tlJXzl_4pN4g4eNcfXUuWBaWmV640pwtQfkM06NHWfLRpLNlkFKmwgfDlsyU9MSP2gVcB8CC5iDIv_7Z7pq_vyeRaGj8rU8U_tEEEnR63bbFZDKS9bhkj5O8q_Q3f1yAWwvvteqVdAdAwLQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه «میداس نیوز» (Meidas News) پنج عکس منتشر کرده است که پیامدهای حمله ایران به یک پایگاه آمریکایی در کویت را نشان می‌دهند.
در این گزارش نام دقیق پایگاه ذکر نشده، اما من آن را به عنوان «کمپ عارف‌جان» (Camp Arifjan) متعلق به ارتش ایالات متحده شناسایی کرده‌ام.
تصاویر حاکی از وارد آمدن خسارات سنگین به یک انبار، محوطه بالگردها، یک پناهگاه مستحکم (که برای اسکان نیروهای آمریکایی در شرایط حمله در نظر گرفته شده بود)، یک ساختمان چندطبقه و یک ساختمان پشتیبانی دیگر است که همگی در کمپ عریفجان واقع شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71888" target="_blank">📅 15:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71885">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q7IrGX7fujW35jheYrhJh85LgUR6S63x54eiyqf9ePnS_2UHvdBYrZAiSGX-M-lRQiu4RGkp55GKg2JkLSrBVyrBpiOhB0_36a7trsUak62vIQp6zRFeNtB73ayAnOQs0t2aMhLo9G9b9FCSflaa6uv0jZ7mLlKwqFkKoXSRtHPDDchUT04vzevo7mP5RCBgXzh_xADDAmHXcMSd3yM3pJrI5HrcXaMCHomlOLCGnFvEG5xDXNvzBOyB2BGEGnyPjbmmU9xXlm3fG7AvF0WSB7RugmnpmPWJIjJlZfgX1zpgeS9jYwuTFnPVDZEZUW1v03P5dCv3lr_cXPrBQBzrDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQJqopT2g0q8rTp1DDnVPvECqHJeMIFAnjQbUnGtP5sngcAy8f_40BdpUPotKiTW8Pl8P3i283jRyW7lH7LPQRkzcz1yxXadNObFTMi69PeEtaCMZA1ZZDCzqrGfVOBaKr92jtPFFK2lbNRgzUkxC5_9-iysOajTaCrI4It7JyhGl_kcagYIwYvJ8w12upqPsYBnaaPXy7en5Ku6eJO1ZD6e1U5f6KuM90JutfpFJaC1gJrKYqBGTGEgn6_rM_SOL2hSp6vc86bQr42B7XVaK9yppQtqFbh8Xu6KIF3Z1rDeijxMlTKXIpJSTSu_M-07qRLwotyZow5SCM57jXBEig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O5-b5b95OC08KmPDvL5LosIF3smD0JmMMIAQ_r3t8wQrhlnOGRC7-fVZ0k0MfhACQQzWlTMQ-B40JgpGNq1EdAGPH_dJir-dTY6t_yfrRYSTVVNBWiGXHXb8iHFviVvvPN7YvTz-xrRO5IyERW_Gz8XW-IbliPGY5V9WxqgVhJFlqPZ4idyEI7DoacQBYX5_hhi6zk_oAdTfzzHdHq-Hjn8Trha6ew3dtTBNkpz68dp4som4eXq9RU5N7qyBhTo10BacqSCzFSUBE2Ao4Pl-xRoEMZig2Riv37ODOsSvYE1Ja7jdGSPo3Sx6-Gu07L3kQHbsbwZdbvknEw6V7GEqNg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارهای پیاپی در نزدیکی فرودگاه بین‌المللی ملک خالد در ریاض
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/71885" target="_blank">📅 14:51 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71884">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=rxquF5nRgg9OVZImL-_ADxtA0T129TRjRDvHzlKeam2sRjC5gyXL3q-SoXO5VM2c36WBvTBXqzSkU21ztFOhNXR2wDFPV-PeLNdn8B3KI6PhESedZkMGxJ_yhQicuFujQ99k0Wzs6dOn_-6jQ0RODjD8Qv8l_Mg45JnDKRTZgIkQw0GCwikx1fJy-7_UaG0IkaqQ4wj_AIGF9EguJByyCSKR1PN2_AsZ_UM-nFQXc0olx3Z37nRzxBeUnkVqJ273WwJMQmPbLVwXRxuasre2CNACIGH_5OD0pwzDlw8mdinXjdpTwIguzkNk_Bg7_WeFD1gNKmI-nu2xmgk5gEMS9A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/974e7b2cdf.mp4?token=rxquF5nRgg9OVZImL-_ADxtA0T129TRjRDvHzlKeam2sRjC5gyXL3q-SoXO5VM2c36WBvTBXqzSkU21ztFOhNXR2wDFPV-PeLNdn8B3KI6PhESedZkMGxJ_yhQicuFujQ99k0Wzs6dOn_-6jQ0RODjD8Qv8l_Mg45JnDKRTZgIkQw0GCwikx1fJy-7_UaG0IkaqQ4wj_AIGF9EguJByyCSKR1PN2_AsZ_UM-nFQXc0olx3Z37nRzxBeUnkVqJ273WwJMQmPbLVwXRxuasre2CNACIGH_5OD0pwzDlw8mdinXjdpTwIguzkNk_Bg7_WeFD1gNKmI-nu2xmgk5gEMS9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف سوال پرسیده: سخت‌ترین قسمت پسر بودن چیه؟
جوابا جالب و دردناک بود:
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71884" target="_blank">📅 14:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71880">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95e492d945.mp4?token=sRDwynbT3Gm7GwpbEm8euFVitQr3of57Um1U1WzDPh2oEC0LBLytEh_2MX-8M95VM72Wa4Gq1JC8JqohdC6yXCFXkJqzML56Ai4jvkfZDUmwX1uEKWmT7b1fpnA1OomLUd3ZhAjG0RP6YsU72hrEdbBvM7uzMgS-sdAkcEkM70FFsp5JJ1-2pIyswqQj-__jUSexQd6IPkDg5dDkyuUVmxsz5wpLgi4TXdDRnzEJftoMz5EbEdkyyR7Js46hWa188Fz1fh0pWUE-FV7X3xvXw1qnKhU50gyUS3oK-dNaJ0tfRqQjamlDt9kCV-yFmJsAadgWirDfqLVGHz3Lg_jscg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95e492d945.mp4?token=sRDwynbT3Gm7GwpbEm8euFVitQr3of57Um1U1WzDPh2oEC0LBLytEh_2MX-8M95VM72Wa4Gq1JC8JqohdC6yXCFXkJqzML56Ai4jvkfZDUmwX1uEKWmT7b1fpnA1OomLUd3ZhAjG0RP6YsU72hrEdbBvM7uzMgS-sdAkcEkM70FFsp5JJ1-2pIyswqQj-__jUSexQd6IPkDg5dDkyuUVmxsz5wpLgi4TXdDRnzEJftoMz5EbEdkyyR7Js46hWa188Fz1fh0pWUE-FV7X3xvXw1qnKhU50gyUS3oK-dNaJ0tfRqQjamlDt9kCV-yFmJsAadgWirDfqLVGHz3Lg_jscg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نیروهای امنیتی پاکستان عملیاتی را علیه یک هسته تروریستی — که گفته می‌شود متشکل از شبه‌نظامیان «تی‌تی‌پی» (TTP) است — در منطقه «کوهات» واقع در استان خیبر پختونخوا آغاز کردند.
در پی حملات بمب‌گذاری روز گذشته علیه مسجد شهر، شبه‌نظامیان مسلح یک مقر پلیس را به تصرف خود درآوردند که منجر به درگیری‌ای ۲۰ ساعته شد.
نیروهای پاکستانی اکنون این مقر را به‌طور کامل پاکسازی کرده و تمامی شبه‌نظامیان را از پای درآورده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71880" target="_blank">📅 14:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71879">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=TomoFCRS5WqIH7tFeh9rOqHiElM4c5R4wxbHzpRfHLpjYvlogyDZZMxH0d1A4NpAOy_ElPdx4FOoPDQzFn0bzG18opiyHqY5YZE3s3_LH4d3gReEvDP0Crk8C5DF1OueP44SEwxPZAs_J3FHCsMQ3Itv1KLXjoWlh9VfieLSGd7GSJk3ArDvanq83gRynANg8XylrZtUdaMXx-8z_6GNBltjQjckf6yomwpKIbhG7Rllr8wp9hja6eFymDLdxPPC9O2hjOM9CtZHqsPDt0PZgBKWi6177eOf_pW0lmTGIPoTvflYC5fQo9RJy6V11vkcQGR-uAV1Ux5rhbEsg_QkMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6895254ca3.mp4?token=TomoFCRS5WqIH7tFeh9rOqHiElM4c5R4wxbHzpRfHLpjYvlogyDZZMxH0d1A4NpAOy_ElPdx4FOoPDQzFn0bzG18opiyHqY5YZE3s3_LH4d3gReEvDP0Crk8C5DF1OueP44SEwxPZAs_J3FHCsMQ3Itv1KLXjoWlh9VfieLSGd7GSJk3ArDvanq83gRynANg8XylrZtUdaMXx-8z_6GNBltjQjckf6yomwpKIbhG7Rllr8wp9hja6eFymDLdxPPC9O2hjOM9CtZHqsPDt0PZgBKWi6177eOf_pW0lmTGIPoTvflYC5fQo9RJy6V11vkcQGR-uAV1Ux5rhbEsg_QkMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبیله‌ای در جنگل‌های آمازون که با دنیای بیرون تماسی نداشته، از هوا فیلم‌برداری شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71879" target="_blank">📅 13:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71878">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=Pw2zQ9YYv4Mw-icUNEfTQcB97XVHybapk2bH9XZBVWdY_C2ZokRYISiF3kmbwV2Cw9Zbjw4bREKGwFG3xgwRmS2iM4SGrs9ZTC2_KZtFowum2_9q5T_LSHvUmbYyHTWgaaf6O39CCfz1t6VcjZ3QFgsGvngFNCDdqV8-x3uYl4tkHTFIepZgdb9DlOaIU1UeF3D09DEpya4_pidc-uMB8K2qQMLc2sHg2JftWMydo6UsoJdnX-tpIG1fubLrfrPXKlYRZKaJwBllk6O3JnpvsvOfIjfw1imKcKUHy3T6rISnnH9U3ilQ2NjB_UdbP-sgN7IFoNNeI3aCmYXfnFWnAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fe570c529.mp4?token=Pw2zQ9YYv4Mw-icUNEfTQcB97XVHybapk2bH9XZBVWdY_C2ZokRYISiF3kmbwV2Cw9Zbjw4bREKGwFG3xgwRmS2iM4SGrs9ZTC2_KZtFowum2_9q5T_LSHvUmbYyHTWgaaf6O39CCfz1t6VcjZ3QFgsGvngFNCDdqV8-x3uYl4tkHTFIepZgdb9DlOaIU1UeF3D09DEpya4_pidc-uMB8K2qQMLc2sHg2JftWMydo6UsoJdnX-tpIG1fubLrfrPXKlYRZKaJwBllk6O3JnpvsvOfIjfw1imKcKUHy3T6rISnnH9U3ilQ2NjB_UdbP-sgN7IFoNNeI3aCmYXfnFWnAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیبی می‌نوازد:
«نصرالله کجاست؟ بعد از من تکرار کنید: حذف شد!»
جمعیت: «حذف شد!»
بیبی: «سنوار کجاست؟»
جمعیت: «حذف شد!»
بیبی: «هنیه کجاست؟»
جمعیت: «حذف شد!»
بیبی: «با خامنه‌ای چه کار کردیم؟»
جمعیت: «حذف شد!»
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/71878" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71877">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71877" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/71877" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71876">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lerTSedMnYIHbUqzfrxWOC1gfnUAPV4W_6AcanVfVtjtwZRqQEfhgKMWdPPYL_PEfYW4zj2U1lSAWxhmIJaSOILwQZDGMN5NvavVWfuoT_x1CR9D42N15K1lKLUoKHS9X7HU5Lew9i60RYd3vg-uOuyJ61qe9EzRVjqFl_6q8Q-gdSNMyO8uI5aC15pkNHBCofQmLjBSHRW2XEqVU5ufV6iCI90BXWmetWIR3jb4zP4OR4QSK4_VbIXGLoFQlidtXP_ZmD7Bvd7fUpx5n6i1kneYNaAztaLHZ1yWJ5ETL3lwaRKqtG-TOaoqYSOeSLwICQdWvC3K4_LCgyJQtUV8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
استون ویلا
🆚
تاتنهام
آرسنال
🆚
برایتون
بارسلونا
🆚
سویا
دورتموند
🆚
اشتوتگارت
اینتر
🆚
رم
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71876" target="_blank">📅 13:09 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71875">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=iMaPXiNgv1fIBtU7IDXTW2Wh12RB8ok-mdt0YOOwEECWAfmQa9BCYj1J6PGdcxs9QwMUP9_A3VJDAiPu1nPhtnLxpkupktLKmuMbHiGBv6JDw8FL4ZGMQUGm4R2d15l84Bdir0cWO5SH-WHgXPIPS7VbA5jLW6sA1Py2xzM-IL2TT89iCAft2N_ZEMXaHcfxziK5YUnIxPQZL5vGcLK79jlQ0ib6LWpCKlbt1imHNWt9hEp5jhazXmMXExkD3PHkY8vBkX5b_2GX_HUENHBOWorMB6ASU6hSZtmACdXotJJmaQ1Ka5lUoGqS_8bbH5-TKdHIgzaICWsR0F-Bs5_JcUSe_J6xQAeR6IASHJmtG63rv0_vh8dForTnfdPp17176M7MgUu9dkqPNBMR-yh58nWcCkAR51pVwGRRM4ylTFSGqcq2fvACAPvrbytzsaWA7EVJXa2c3huDGXBelKGllodHFxdivPZiYXYh8ZgHsHsfIVkOZsKheTvv37-SJLjXA0cHyJVfp3npyusoL-jakbFsv-qUyT3gIcV67k6b7WgsI1xvbr6KARou5_bHJUONdSIrpxnRLFkQm7hCAof8hmd4Ip40MWWF9TViFXd7uYOIJ9LQRIqjFkbqor27M2wiNfuMhB3tg6HmQsChlcUUXrD44YBA8B2sVZCR7PdMgzI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e25ecc6de4.mp4?token=iMaPXiNgv1fIBtU7IDXTW2Wh12RB8ok-mdt0YOOwEECWAfmQa9BCYj1J6PGdcxs9QwMUP9_A3VJDAiPu1nPhtnLxpkupktLKmuMbHiGBv6JDw8FL4ZGMQUGm4R2d15l84Bdir0cWO5SH-WHgXPIPS7VbA5jLW6sA1Py2xzM-IL2TT89iCAft2N_ZEMXaHcfxziK5YUnIxPQZL5vGcLK79jlQ0ib6LWpCKlbt1imHNWt9hEp5jhazXmMXExkD3PHkY8vBkX5b_2GX_HUENHBOWorMB6ASU6hSZtmACdXotJJmaQ1Ka5lUoGqS_8bbH5-TKdHIgzaICWsR0F-Bs5_JcUSe_J6xQAeR6IASHJmtG63rv0_vh8dForTnfdPp17176M7MgUu9dkqPNBMR-yh58nWcCkAR51pVwGRRM4ylTFSGqcq2fvACAPvrbytzsaWA7EVJXa2c3huDGXBelKGllodHFxdivPZiYXYh8ZgHsHsfIVkOZsKheTvv37-SJLjXA0cHyJVfp3npyusoL-jakbFsv-qUyT3gIcV67k6b7WgsI1xvbr6KARou5_bHJUONdSIrpxnRLFkQm7hCAof8hmd4Ip40MWWF9TViFXd7uYOIJ9LQRIqjFkbqor27M2wiNfuMhB3tg6HmQsChlcUUXrD44YBA8B2sVZCR7PdMgzI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنری کیسینجر و توضیح سه مسیر تاریخی ایران:
دولت–ملت
امپراتوری
ایدئولوژی خمینی.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71875" target="_blank">📅 12:30 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71874">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=jHOqjdz39l-dD_KnjYpTJKq0c2ueC-SVfEo-QICyLIRcrAkhXIW9ei1nd1zMQuzLXQHLsrcDQO-IAlaGhbCdISYcydGQlDdgegY2JBleRUZxEEfk6U-6VXrP7PtA3ecVWnlcscsCBT3m2Pr68up2wx8wabnhLyElFPk94nMZYNqktWOx0F-6pHLVJyf6jAhyipUL1hY6YafaCnbAhQu75rPOd7RVXfWQ9_UbmNaNqEaosEqSrhzun_6CwrnTNvUPUsaRl_esDBbgTNwvYyiiklH0kcnL3o0lmz-RyCeTHCynFkoWmTwpVzlrsNUCIg3hf9h99UzDKB1eLEp7Ut3acA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/beaae9822a.mp4?token=jHOqjdz39l-dD_KnjYpTJKq0c2ueC-SVfEo-QICyLIRcrAkhXIW9ei1nd1zMQuzLXQHLsrcDQO-IAlaGhbCdISYcydGQlDdgegY2JBleRUZxEEfk6U-6VXrP7PtA3ecVWnlcscsCBT3m2Pr68up2wx8wabnhLyElFPk94nMZYNqktWOx0F-6pHLVJyf6jAhyipUL1hY6YafaCnbAhQu75rPOd7RVXfWQ9_UbmNaNqEaosEqSrhzun_6CwrnTNvUPUsaRl_esDBbgTNwvYyiiklH0kcnL3o0lmz-RyCeTHCynFkoWmTwpVzlrsNUCIg3hf9h99UzDKB1eLEp7Ut3acA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تئاترهای مملکت این روزا تو وضعیت عجیبی قرار گرفتن؛ گویا شوخی های جنسی برای تئاتر ها آنلاک شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/71874" target="_blank">📅 12:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71873">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=d9cPwO5dCSkJcJ8a-Wt3V5-YCRVy3j4j2mjT3TmIiAoal99xXRNMIEQECqvVViwTNPgiIamOoPDAeEDyMuXPONXxyfeiIdAQasqSpkilOBnmbOjasjvqGScA5VAJxr-9sMCADtnWxhlMvn9AZiwD3pKp11Ds4Cu_opRc3myzxu9Q3J6gP4pwx24Mo57xDE5csW2fveEKLFIUfOEbMs5l8zwMlMUvS6KmZB3380M44oXfLDwbWF67wGccj3QFAnHGdYOvzPxbljAYhgKQ8KE6GECELAeqaIOn-NOo5iyaup-2uLEQ2VeRmm-gSGy6-heBD2VKLeBKCQDJDxisgznhWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77deac1aa1.mp4?token=d9cPwO5dCSkJcJ8a-Wt3V5-YCRVy3j4j2mjT3TmIiAoal99xXRNMIEQECqvVViwTNPgiIamOoPDAeEDyMuXPONXxyfeiIdAQasqSpkilOBnmbOjasjvqGScA5VAJxr-9sMCADtnWxhlMvn9AZiwD3pKp11Ds4Cu_opRc3myzxu9Q3J6gP4pwx24Mo57xDE5csW2fveEKLFIUfOEbMs5l8zwMlMUvS6KmZB3380M44oXfLDwbWF67wGccj3QFAnHGdYOvzPxbljAYhgKQ8KE6GECELAeqaIOn-NOo5iyaup-2uLEQ2VeRmm-gSGy6-heBD2VKLeBKCQDJDxisgznhWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه شغلی در کانادا هست به اسم آتش‌بان. طرف باید فصل تابستان رو در کابینی بالای کوه بگذرونه و هر وقت آتش‌سوزی جنگلی دید گزارش کنه. عمیقا حس میکنم من میتونم خیلی تو این شغل موفق باشم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71873" target="_blank">📅 11:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71872">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=bI0vISI0w4E_Ta56ItitO6p1J7VVtjjAmCnaO9NjO0YpfZ-kVygzHy84XZ_iZtrA2da1DWKAtO6WAiSF0R-xlmM__vOED_irRJJ34Wc_485_vT2IGSJSfHxJKCKryhyxmlNdRyChatEm-q46woALxOjoCKINdTri-XIwIheQOD6Zi_3BiJtOlD4Gs8UL9YFLisING4xuY8h9TkDyHhMF7Vim6Mrffz049Gw_nYdapr21I74V69bAuSpneCR2EYYf2-1VyC1LoVc5JaAXvBXDCM-kSGmdfPmVrTDJCrAg2RtO7v_58gmdp6HKTWZKbYVxdcp4qH0htZVjsTM26vMLXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d090aca4d2.mp4?token=bI0vISI0w4E_Ta56ItitO6p1J7VVtjjAmCnaO9NjO0YpfZ-kVygzHy84XZ_iZtrA2da1DWKAtO6WAiSF0R-xlmM__vOED_irRJJ34Wc_485_vT2IGSJSfHxJKCKryhyxmlNdRyChatEm-q46woALxOjoCKINdTri-XIwIheQOD6Zi_3BiJtOlD4Gs8UL9YFLisING4xuY8h9TkDyHhMF7Vim6Mrffz049Gw_nYdapr21I74V69bAuSpneCR2EYYf2-1VyC1LoVc5JaAXvBXDCM-kSGmdfPmVrTDJCrAg2RtO7v_58gmdp6HKTWZKbYVxdcp4qH0htZVjsTM26vMLXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور:
رهبر شهید به رئیسی گفتند چرا به امیر تتلو نزدیک‌تر نشدی
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71872" target="_blank">📅 11:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71871">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=jRR71FBVvZIh0K3H0uWlQvdLx4fZpJPQu2kcDG0mjc_yAd6Vqq8ac_PP76rWvyZW8CBsBYtN2Ov1B2c0DEIA62Ihxwshabxje2hffPwHjyhLY_r6E6cMSCsEi1Cmx5dz40CDw5yqF9X-Hi_sFDD-QwPmd2G4GCiW2E1VP4bQvVZVkOsbTgYVkwkehi1XCgKGaeWOqw-msEpa9Q_7GAr39-hcVQp6MFumrs39tGqkgJtnjwUuYrzWI314__-P8iRV4KoTAe1MTGJxGpj2dE0O5Wz0HFh747eZB-O6uDAYdVh9Rn_40swL_BzExyB-K1TSDHs-jW5CX43GtCFfj5XVDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/400c93a6ac.mp4?token=jRR71FBVvZIh0K3H0uWlQvdLx4fZpJPQu2kcDG0mjc_yAd6Vqq8ac_PP76rWvyZW8CBsBYtN2Ov1B2c0DEIA62Ihxwshabxje2hffPwHjyhLY_r6E6cMSCsEi1Cmx5dz40CDw5yqF9X-Hi_sFDD-QwPmd2G4GCiW2E1VP4bQvVZVkOsbTgYVkwkehi1XCgKGaeWOqw-msEpa9Q_7GAr39-hcVQp6MFumrs39tGqkgJtnjwUuYrzWI314__-P8iRV4KoTAe1MTGJxGpj2dE0O5Wz0HFh747eZB-O6uDAYdVh9Rn_40swL_BzExyB-K1TSDHs-jW5CX43GtCFfj5XVDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پورن استار معروف ایرانی ملقب به «شیر ایرانی» با انتشار این ویدیو اعلام کرده که مسلمون شده و از خدا طلب بخشش کرده :
کاری به هیچی ندارم ، چرا وقتی میگه بسم‌الله ، با دستاش صلیب میکشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71871" target="_blank">📅 10:33 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71870">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=bID7XPBiJ25ktId-CTia74Am2fnL74AbG8f4XHLZyNz0GF3ZODyU6iT3tuQLq9gHKxwPiIvHTKWFIS6mmNyruhruoUPVmKRxOT59pRClVSC1qyCkvC0-OyK1OaHBLp4J231O3heO__S2su5OzPyJZo0ehj9L7TJY2qPGXxqdxOfiqJfuxOfhLY7qWw8CYOqNoEkOu9dO-a2KIeNKDHhccwLDT-vsLFG52xLfjp7mjqxiOIETqevk52BN5qMOzIsDuPTG7AK-VQ_8mlf4JT5ImaPvNoVISdCikq0OF5VuAZu_7GEOYDE5EJLXXPw6w_pi-RsVd7SaoN2ZqbxhOzpfQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40d28238ee.mp4?token=bID7XPBiJ25ktId-CTia74Am2fnL74AbG8f4XHLZyNz0GF3ZODyU6iT3tuQLq9gHKxwPiIvHTKWFIS6mmNyruhruoUPVmKRxOT59pRClVSC1qyCkvC0-OyK1OaHBLp4J231O3heO__S2su5OzPyJZo0ehj9L7TJY2qPGXxqdxOfiqJfuxOfhLY7qWw8CYOqNoEkOu9dO-a2KIeNKDHhccwLDT-vsLFG52xLfjp7mjqxiOIETqevk52BN5qMOzIsDuPTG7AK-VQ_8mlf4JT5ImaPvNoVISdCikq0OF5VuAZu_7GEOYDE5EJLXXPw6w_pi-RsVd7SaoN2ZqbxhOzpfQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو اسلامشهر ی موتوری خیلی ریلکس و بدون پوشوندن صورتش میاد گوشی ی دختر جوونو به زور ازش میگیره و فرار میکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71870" target="_blank">📅 10:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71866">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=CDiy6MZG6VFG5PDS63tYr3RUoRdD4l2HV5T1WwwfhBK7uCqeU2MadmlOI39n-6F7iEPQ0p0XZvTgbWls7i5bTSTJ2kYByg-qbdnnE5mcyGN73SGl7uWlNaZoGojQZ3MwsmKnjqxUL4c8b-U8drjEJDoAi46QjD8xXtUaHW7Ii3YRaKWL0DoSerxMdmS_x3NVbsb0beU_eSMiHbCwE1Jom0euqpPf8iuJtE73D4joqbH5lsb2jYdp6-Asom-DSw3xDyNpgSXoAEuPFG0wTxW40N-waBd9ukNdistvVl7NVdFAZaxn3UEoEKfGdsq2fnuxRAzZfYCBa8YihHBatfD3AA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6655905e8b.mp4?token=CDiy6MZG6VFG5PDS63tYr3RUoRdD4l2HV5T1WwwfhBK7uCqeU2MadmlOI39n-6F7iEPQ0p0XZvTgbWls7i5bTSTJ2kYByg-qbdnnE5mcyGN73SGl7uWlNaZoGojQZ3MwsmKnjqxUL4c8b-U8drjEJDoAi46QjD8xXtUaHW7Ii3YRaKWL0DoSerxMdmS_x3NVbsb0beU_eSMiHbCwE1Jom0euqpPf8iuJtE73D4joqbH5lsb2jYdp6-Asom-DSw3xDyNpgSXoAEuPFG0wTxW40N-waBd9ukNdistvVl7NVdFAZaxn3UEoEKfGdsq2fnuxRAzZfYCBa8YihHBatfD3AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی ایشون دختر نیست و یه فمبوی(پسر) ایرانیه که خیلیا روش کراش زدن و توی تله‌اش افتادن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71866" target="_blank">📅 09:32 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71865">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=JiI0R4okYhuWlxCv5mxCDvFMAJMX6Dft1_lG2-8cumUVSmA21meJXh-md66I3EKhbD8Pf4p0ZJgqBbOoFsDnMptNX3yH7oxIyG0fGBCL67Q51UP2fv8bwZIbFYg7BCaC43x-vTYsqjNg1xVwHpkHXkybewpV-JI9fXjO4rOADth4KQArje8a4xt_-snJ_mg2LwGGcJhm4MHoTANFa2GWux4dSr7HyxWEfrGIcKfIlmvSoATzeNKyRiABjpnCGV3TNnH0a_ISoiRdDBp1cTEkZhqV7fx4PmCZJz8emZrFkKXYFDJ9Fbyi1O4xU03hAyhpYZGrqvV6D4IICipN6gxaz65KRIx7gU1DlkMBRCVIac6DXL1RYo8Dw4DR_eQ_iE0ibgX3nA9B06fQopwHDL0Xy-y45r4pHcvGPObr2Y0FR1JqhzLFhocXN5K63m6YqX4FMZzg8CDoR0WXy25MkzTgk-054unsLLH3bLQnqhsLQo3EK1zi2QZrdir_YohdXQDJD1gbdytgGiLyudbGGD5xjSxfbWZRaHYs68Dyh6VJM67uSOcWHlNwWp0UMudu2C5lURbNj96a9A8Koj86uD8VHDxKfSGvaVAYYko7tM3TamkZNeQqxPvBPerL3k5Pb53mWXR7baGG0AHBiHn-7ElEVXgKqb62uGMdoq04QlPe288" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf20c1179.mp4?token=JiI0R4okYhuWlxCv5mxCDvFMAJMX6Dft1_lG2-8cumUVSmA21meJXh-md66I3EKhbD8Pf4p0ZJgqBbOoFsDnMptNX3yH7oxIyG0fGBCL67Q51UP2fv8bwZIbFYg7BCaC43x-vTYsqjNg1xVwHpkHXkybewpV-JI9fXjO4rOADth4KQArje8a4xt_-snJ_mg2LwGGcJhm4MHoTANFa2GWux4dSr7HyxWEfrGIcKfIlmvSoATzeNKyRiABjpnCGV3TNnH0a_ISoiRdDBp1cTEkZhqV7fx4PmCZJz8emZrFkKXYFDJ9Fbyi1O4xU03hAyhpYZGrqvV6D4IICipN6gxaz65KRIx7gU1DlkMBRCVIac6DXL1RYo8Dw4DR_eQ_iE0ibgX3nA9B06fQopwHDL0Xy-y45r4pHcvGPObr2Y0FR1JqhzLFhocXN5K63m6YqX4FMZzg8CDoR0WXy25MkzTgk-054unsLLH3bLQnqhsLQo3EK1zi2QZrdir_YohdXQDJD1gbdytgGiLyudbGGD5xjSxfbWZRaHYs68Dyh6VJM67uSOcWHlNwWp0UMudu2C5lURbNj96a9A8Koj86uD8VHDxKfSGvaVAYYko7tM3TamkZNeQqxPvBPerL3k5Pb53mWXR7baGG0AHBiHn-7ElEVXgKqb62uGMdoq04QlPe288" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«آیا خواهان جناح چپ هستید؟ (جمعیت: نه!)
آیا خواهان جناح راست هستید؟ (جمعیت: بله!)»
«آیا خواهان تشکیل کشور فلسطین هستید؟ (جمعیت: نه!)
آیا خواهان کشوری یهودی هستید؟ (جمعیت: بله!)»
«آیا می‌خواهید تسلیم شوید؟ (جمعیت: نه!)
آیا می‌خواهید بجنگید؟ (جمعیت: بله!)»
«این جوهره‌ی این انتخابات است: یا چپ، یا راست.»
ما در جناح راست هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71865" target="_blank">📅 08:54 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71864">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🦖
اینجا فقط ضری ب‌ها نیستن که می‌درخشن...
🦖
چندتا Star آماده‌ست برای کسایی که توی قرعه‌کشی شرکت کردن. شاید قرعه به اسم تو بخوره؛ امتحان کردنش که هزینه‌ای نداره!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71864" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71863">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/news_hut/71863" target="_blank">📅 01:36 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71862">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">#فوری؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.  این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71862" target="_blank">📅 01:27 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71861">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O0Ue7HQeRdS0q3vcTgk7Q0ULiLhar84zF-4r4iVgfQj5ZzN65EjqmpIBT_CC_pWsgD5yznu0s7x2qjEZCesX3Ns5wxyM7txS74Oyi1zBkiqgEemlWX_VaR_smGra72rpXhzA4pzAm9ZwxYSBoMRL3v6vqotQnqNYUgUvHqbLKcd7WG35MMAHKxk1HaEerXCUeB4BmuL2nvlyOUxbLawnYn1TKDK298v3C244uuHIQ_Zo6Em4PNENLKUHwLd6rukMtjsMRJm0ar7myGMvQJwz4lyanC4edKrJaUj2slf1zQdxTa5dJx13rCTPhTNXwMF2iot3pTneSBr0zEC18ioe6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛دونالد ترامپ، رئیس‌جمهور، «قانون لیندزی او. گراهام برای اعمال تحریم علیه روسیه و ایران (مصوب ۲۰۲۶)» را امضا و به قانون تبدیل کرد.
این قانون، تحریم‌های قانونی، تعرفه‌ها و ممنوعیت‌های اعمال‌شده علیه روسیه را گسترش می‌دهد و تحریم‌های موجود علیه ایران را تمدید می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71861" target="_blank">📅 01:24 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71860">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.  ترامپ این توافق را توافقی با «عمر…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71860" target="_blank">📅 01:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71859">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/culd5KUkIb8_tkodhrLrHAWiIP6xBsEbOdEJ7LVHEkz5QRmJZT0ZpyiU5Br51p6w_COxdkJJbUBqYC1iAq8gNm0YKOzgFO6ksYWDbgkgQWb24cUH2qbObaru-llG5VVnAcx94dWWcB1-9a35cImJ-S8PZcb-8vIfpPZXJYrTWc6hGoKv7zCPqCU2WXvNRqi_CTyKfUBomXSpX8miB0HjOo9WtBDwfMqUK2jtt5H5eD8z9hQ2biz5fpUJSFsL1sa4zkjvL9Dov1zCQeJeFXrmc6BokzmAjllRYiO7KBNRiZ_zgxECusZYOi05f-EEXlXZqTqWicj3dM4-cyD9WFdmRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اعلام کرد که ایالات متحده با دانمارک و گرینلند به توافقی دست یافته است که بر اساس آن، واشنگتن اختیار دائمی در خصوص الزامات امنیتی آمریکا در گرینلند خواهد داشت، در حالی که گرینلند همچنان تحت حاکمیت دانمارک باقی می‌ماند.
ترامپ این توافق را توافقی با «عمر نامحدود» و «بدون تاریخ انقضا» توصیف کرد و اظهار داشت که ایالات متحده قادر خواهد بود اقداماتی را که برای دفاع از گرینلند و آمریکا ضروری می‌داند، انجام دهد.
وی همچنین تأکید کرد که هیچ‌یک از دشمنان ایالات متحده اجازه نخواهند داشت بدون تأیید آمریکا، در گرینلند حضور نظامی داشته باشند، پایگاهی دایر کنند یا سرمایه‌گذاری‌های حساسی انجام دهند.
او می‌گوید این توافق برای ایالات متحده «هیچ هزینه‌ای» در بر نخواهد داشت و واشنگتن بلافاصله روند گسترش حضور نظامی خود در گرینلند را آغاز کرده و در زمینه ساخت‌وساز و توسعه با مردم گرینلند همکاری خواهد کرد.
ترامپ این توافق را «تاریخی» و «تحقق یک رویا برای ایالات متحده» خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71859" target="_blank">📅 01:03 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71855">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uHQWlEOSmHKX79caRyATmlfixm5yebNrNqCE8Px1nM1AOl3C3E1ZD3MEPdimFAUzxdsISRGvDIaO2INdTyMcYOcRKRtqwhSyKO40Xio0Bt5LseMKTukKrQMf9ahN2FwX5o2ZEfhh2BRIlCKivvNd-4oYylXdPfWH-RHOHe8eFnu_Z3mIK7X9SUVdLHS1o21R_IAlFJJ2MsE-Xf-d-y_x8qnLnbggkSqwzJqi_GbBUJuRiqVvQhqGXPUx8MH-8TMlkr0ZUOAbYoMinHhCWx3hriLvrn7qSIk9KI5dqxDRNVIed313cdG8eSBe-HCSrJ85nawxm_XxPB7kxi8OaI9HtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENVabH1FoQZGj9ZcdSf6hPigxCyvZNklULJg_1hyK4V83licDAFNyaik_NLFTBa4kuZ5nqGA7W35iVmcJs8op8NzssRSSJ5TPAm-iiti0n3Rfj_x7jkjI9N6KQPoVwgM5ptRcO5eHBASFQgKYengkC6vrMDkFq0IPjl1BTMQXhlrurT4YYyFzqL8LEMjAngdTUYJ873m9VGi6fugKY1ZPbpN2gpdCtykAnLbjIoIbRRKZgFHSKYA0XJRgwC_VFniivX56z6PzMoGtcoz_oo210-ktn4WqQX4xGaOW2rXcUHMMWQaRrqnhmEvQrgkJA3YmH0Mq86b3nDyVFghJ2QXPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z4t8_Rp8u_vejle_YEKf5SeB1Lurri8CHs8Z-DTg0cboPkRlbAMrkNBCIgdtaV-ScRC2UfSHDHyW7MCXeOcSxapFApoPDm7sBG-MMpTHLVWaifNH7blzv3KnpuN9o5pY8lYQvxcMgkswzsoIn7wvRpsa8_LYfAGnLNIcLrWa4Rw3cWyCYATT3UZKMf3qc_eow9uZQY98yW-nGMQCMzeNu-VuCRddHHcwvDygSPKinXV-hRg4ifLE5LSzos-ysGLUzc-5taejp2GFGtdKxALS6Q_2fGraF1SjYLVB68sBRzzc1TGC0tHR3gtsYILn2W0xx_6qd03QK9xEmnzrq-lvCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkspXBnxQFWydY8yy-WFaCpk4cAB_soqfIH6K17v2CeYzowQpwElPCLAIhbMDBqmttOrEWdwAoIAV5W60M-4zBQ-MZANsk5zSiAmAQnDUgnFiLbxGJI_Csljtzf3-EI7nnvWfS8bpXAwH7Y3ok6451Q9Sqa8pC27_qp_r-Hf1KvT220HrJrhZT-fbYVaQ0TfW5llifMCvgQMSJzkc5yw1gRcRu3XwZpwgXu1ygR7_dcbIAg9o2UcEzvLTwvn-AQTOZvvXb3CPvb8dFx6M6fks91OA8fA2quRIMNTh8Tkpa0bz-3RpkzQBXkJJBzt74CVBcmxgv0oaxaMl3opQUBxJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سنتکام:
تفنگداران دریایی ایالات متحده، وابسته به «یازدهمین یگان اعزامی تفنگداران دریایی» مستقر در ناو «یو‌اس‌اس باکسر» (LHD 4)، هم‌زمان با حرکت این کشتی در دریای عرب، به تمرین هنرهای رزمی می‌پردازند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71855" target="_blank">📅 00:31 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71854">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=MxWLE8lfWFy99GMbQItjLVsZQUOQG5B9rqwwsBZe6k51zAqaHzMbzYGWsevciJo41e6-WKEfzMnpL3OSPSdBrV4TxLwujf0anNvNck8jNqKbT_BgIvDQckXZDZZYyy2dzmxaRcBk_lAjuhZ4ApYdOByDRM45wvM760MXvNxc0jP0xq_lZj3bEVv5d3bH3keulmHyEQozZbyMgdsTtZPyWHXqbqansh5g347WlZLtlHz1Xucw_BXpIjTqZ03wdXO9700kHyu-IBh5JuYEZQf63HGvs1GXQ0VOI30GBKcuOF4REC5PXIvhCtxv__-u6eBg30hafKKql09BXL3HiD-Paw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866c3cddb.mp4?token=MxWLE8lfWFy99GMbQItjLVsZQUOQG5B9rqwwsBZe6k51zAqaHzMbzYGWsevciJo41e6-WKEfzMnpL3OSPSdBrV4TxLwujf0anNvNck8jNqKbT_BgIvDQckXZDZZYyy2dzmxaRcBk_lAjuhZ4ApYdOByDRM45wvM760MXvNxc0jP0xq_lZj3bEVv5d3bH3keulmHyEQozZbyMgdsTtZPyWHXqbqansh5g347WlZLtlHz1Xucw_BXpIjTqZ03wdXO9700kHyu-IBh5JuYEZQf63HGvs1GXQ0VOI30GBKcuOF4REC5PXIvhCtxv__-u6eBg30hafKKql09BXL3HiD-Paw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آزادی مطبوعات در متمم اول قانون اساسی تضمین شده است.
ترامپ: ممنون که این را به من گفتید.
خبرنگار: آیا سعی دارید با ارعاب، مانع از انجام وظیفه مطبوعات شوید؟
ترامپ: نه، نه، نه. من از مطبوعاتِ غیرصادقی مثل شما خوشم نمی‌آید. به نظرم شما افتضاح هستید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71854" target="_blank">📅 00:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71851">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=k6exNgRSHECQPps8cKXsrMSrGKoWEg1QUBbP8zRQ91sZ1E7J7zTrwy054PDFoy1_j7lCb4NDt0IvIT7C6tXCgyd0zG39Sq7_GKLSjGWE8f-TYO3RPmxcVBCz1kGitrllO-8YahYp6ulZ-lTKjbhQS3cXLoJ6znnNOqDwoJfQGmjWX9NnZ_CLhaqcy0gtbc8pp0LgX1P8o2Pj_BvrKJg6N4G1tLNm1kBAob5OZnlF40t9hTArsrg-fByCFXebW0Iq8uC0yTuxtaS2Ukm6JQdtf2Gnl_p0LIynC3ua-Jqcq8ISjm2FRd0lU_EUaJAErYNi3uck9SX857nzbTviKVw0Qg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c6db95143.mp4?token=k6exNgRSHECQPps8cKXsrMSrGKoWEg1QUBbP8zRQ91sZ1E7J7zTrwy054PDFoy1_j7lCb4NDt0IvIT7C6tXCgyd0zG39Sq7_GKLSjGWE8f-TYO3RPmxcVBCz1kGitrllO-8YahYp6ulZ-lTKjbhQS3cXLoJ6znnNOqDwoJfQGmjWX9NnZ_CLhaqcy0gtbc8pp0LgX1P8o2Pj_BvrKJg6N4G1tLNm1kBAob5OZnlF40t9hTArsrg-fByCFXebW0Iq8uC0yTuxtaS2Ukm6JQdtf2Gnl_p0LIynC3ua-Jqcq8ISjm2FRd0lU_EUaJAErYNi3uck9SX857nzbTviKVw0Qg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
اگر قرار بود رأی‌گیری‌ای میان «کاهش قیمت بنزین» و «اجازه دادن به ایران برای دستیابی به سلاح هسته‌ای» برگزار شود، نتیجه آن یک پیروزی قاطع و چشمگیر می‌بود.
مردم نمی‌خواهند ایران سلاح هسته‌ای داشته باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71851" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71848">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QGf4HsIpfKkFnZYRJ1AhTCgwNI1HK_3Fdu1OEWvZs0-PAQYaRA4dzJ9_8MExlwm2F72HcJMF3tufVHCtYTgk3WBwVRo0G5_spIv02FaxMT2lBt6QxwUtDuaVO_myDF_11H1foefV-Pp661FRdn51uArycxCqPrHIlSH26rpRYXcu4eWXWM92dVSi8UaIcEAE1o7crnJv84GjcmLrjPDb3s65F-8MHY5LyksjQzYw9xJA0Opkp3ejbo1L2cNdlrR6H3vGnCVc6UvuR7ygTGELX224mJL5nvv5URN12lOUqRqA_WZ93-y6hw9piQwH9iQFErxITNvf-reBtqXF2p5TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H6tm6YtnVd_TPg146HMv2tsPHIAZ_ZhQjfNZYgp_WXkz3hDBg-fmYhxhhwb1rydp3UC0wdzCUd_h0wOEijYhB0FjQH5wDkRPGyTobxh7pEITd06dgRARnmp6yjoVgB-eUefRHKCQTxIp2711zmG0JKRJLmA1oNt1EH0ZTyt0PtcocS3x5vgnCqzCEACEDiked8evu3v_P68LbhBXlwsjfp522uVE3rfP11zd7c_Nrmg6tlTm5jges7BRa3jdnY7gatlZJVDfbOTZbz-n73w7I9xbqplLhU456mcRHagUjujAZaowgAnOWUsAY1Q-N5kffR70i7pW2twdbW0BTvrsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpypTEYUHpkQgSB1-c7k7VsP2wWKCEc0QimEZh0PTiyK6V6cRs6SYZuWN13i22gIQ7hUg6PYWOYu8kO-qc9oOKAN9SqSDQHPpzc4ur1F9VdI9CJipv0RiIjDyMLca6mjVVBELW9LCcdrcL50AF-gAr6anBN60l5yIvtsbB8VGWj4wFXSnrVkLA4_bz1g2EHAN2n3ET8Vgl5Y7fWwTiXn7sO27spfDniY2oa-Q3-__yCwWJaTX3ciUAuDSIqElBvW5uioEEc5Bhlp0Mdyt_4oQqiCL52OkyHY0LjyMCBUwwHDbtLruVGoBYu5WRu_1-wB_RKX1YtH3ytNC_qVjl3_6A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گردان های بانوان جانفدا تو همایش امروز:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71848" target="_blank">📅 23:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71847">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7102741190.mp4?token=ndw-wHgOsQ8VOwH6gt0JKvaqHIbCxtygZ9AzV4vvrwp5FMSzSGNpiFT8JQrTGhHsykqSbtAFPThLlOKSpR01K8NpRIHV5IPIZE5_O0MwBf5EO_eNXEvIs3WOR05CFkC9wJuZr-fV9UEggw4hh1Q_ZdPr1L8yaKSAB490Vtrqa4jQy3rY6lZMeViN2gH5puhew-uY1ZN23LyFtIv3EusxmRin6BHUY3CLp8IVKQhXhUfJzfX0YIvaw18rZRK19CitQZVnAqTBpbWNUUMfcuNjv95MJ0YFca5OQtRLaVcHE_VQUkUSx56MGUCc_GslmUOVbTTogUjv_ybFVHabvY5SeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7102741190.mp4?token=ndw-wHgOsQ8VOwH6gt0JKvaqHIbCxtygZ9AzV4vvrwp5FMSzSGNpiFT8JQrTGhHsykqSbtAFPThLlOKSpR01K8NpRIHV5IPIZE5_O0MwBf5EO_eNXEvIs3WOR05CFkC9wJuZr-fV9UEggw4hh1Q_ZdPr1L8yaKSAB490Vtrqa4jQy3rY6lZMeViN2gH5puhew-uY1ZN23LyFtIv3EusxmRin6BHUY3CLp8IVKQhXhUfJzfX0YIvaw18rZRK19CitQZVnAqTBpbWNUUMfcuNjv95MJ0YFca5OQtRLaVcHE_VQUkUSx56MGUCc_GslmUOVbTTogUjv_ybFVHabvY5SeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خانم تو بخش پذیرش یه مطب کار میکنه. حالا به یه بیماری برخورد کرده که یه فامیلی شاهکار داره و باید از بلندگو صداش کنه:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71847" target="_blank">📅 23:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71846">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=R4oohrOTZ_RHO9L96XgtylxcIarpHuaUl4HTcj9PycjPCsFUWbf1-ODSgjJa2tmah7-ACROzaeV62UXpvUUS4KToYG3uYavUy31x4eYUTTqA1JAJAigHSiY4HQAk-uM1qDiHOteHv6fGs31GOhxcVcjM_5oOmdYFRbOBzHnXIOPm9BUv9DbEDUnJESqEBWS24n_s0a6nuKsJ7e3sExgYYihbsvfOJfhN79QlCrGhQKq1sA5vxHJso5W3iHl8avlEhNVdU3VBrOqcH6XBDA0SO11rXaxjbLBTcNDhKDhemKIlM_11XRhBlMUlT_yRuqFZQyi8bdOhIjKvc9L8ngdd2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edd80b92b5.mp4?token=R4oohrOTZ_RHO9L96XgtylxcIarpHuaUl4HTcj9PycjPCsFUWbf1-ODSgjJa2tmah7-ACROzaeV62UXpvUUS4KToYG3uYavUy31x4eYUTTqA1JAJAigHSiY4HQAk-uM1qDiHOteHv6fGs31GOhxcVcjM_5oOmdYFRbOBzHnXIOPm9BUv9DbEDUnJESqEBWS24n_s0a6nuKsJ7e3sExgYYihbsvfOJfhN79QlCrGhQKq1sA5vxHJso5W3iHl8avlEhNVdU3VBrOqcH6XBDA0SO11rXaxjbLBTcNDhKDhemKIlM_11XRhBlMUlT_yRuqFZQyi8bdOhIjKvc9L8ngdd2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرکات عجیب مجری شبکه‌سه برای توضیح عملی دفع سنگ‌کلیه در برنامه زنده!
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71846" target="_blank">📅 22:15 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71845">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=EIAHhq2dSJUeiFSAfbA82KUjbYQ_N9nZ4PdQtC-XId0xlI3uV1vWA14jQsB2XBtIzfa2ctsvPgK4X_0cdpovVOv4rzShGHmAYAHdhcmXPEo4qmn0LG0Pq9rQNHFhBNWmTDzb1XIggF6ySivStgT0zcGBE5DQJ8sbidrWExa0c66yAt3pYbM8R18KEGn4rtL9ax1CoL3VHAnRJwzzs0tvh2tZ7Jxrveba7axScF4mbopusJD0K94wGF1XCS6LjWPeX5q4uj6dCQ_ZyzIYffywQJKzs-TlbPkBHHhJpBBrO7cTDeoq_cB5ZE3XQfTR4c74_8xjldIQ6_-RQ0KKpnpGuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46fca26fda.mp4?token=EIAHhq2dSJUeiFSAfbA82KUjbYQ_N9nZ4PdQtC-XId0xlI3uV1vWA14jQsB2XBtIzfa2ctsvPgK4X_0cdpovVOv4rzShGHmAYAHdhcmXPEo4qmn0LG0Pq9rQNHFhBNWmTDzb1XIggF6ySivStgT0zcGBE5DQJ8sbidrWExa0c66yAt3pYbM8R18KEGn4rtL9ax1CoL3VHAnRJwzzs0tvh2tZ7Jxrveba7axScF4mbopusJD0K94wGF1XCS6LjWPeX5q4uj6dCQ_ZyzIYffywQJKzs-TlbPkBHHhJpBBrO7cTDeoq_cB5ZE3XQfTR4c74_8xjldIQ6_-RQ0KKpnpGuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گفته شده بعد از انتشار این کلیپ، ترامپ از ترس ۳ روزه رفته تو اتاق درو بسته و فقط داره می‌خنده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/71845" target="_blank">📅 21:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71844">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aIXZgdIE7mZV5Ufn-epZqAEAYUbPco6NgjA3FSxe81qggNzqXxxK7qD1tsWYT3zS8aufvUYp1KIh1KcGGZiXHwLB-Q474rxvVSmaJCJMkjIPrP9A39bbu2ru9qFL0vl2N0c7d8MuApm5ZV9dJhE8bi3DaaAyIAi482_jUgQQJwQcRiMSBZcjliJqdiZOdsU1VhlkoIk650rqQkvogyaWFsOVeJBEwlL3uemY2rbdSe-SxF5qnOsvpOJ7h2pIg_q8Vo3CYmzW_m1hR2RoX4yrmAlGHz8_WFL9mJShjBbCLWtBSFLex23J9bgNX8aSCPpHN3T44ZzEJTj7ygd-X9S92g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز September 18، روزِ عشق اوله
❤️
این روز بهانه‌ای برای یادآوری و زنده کردن خاطرات نخستین تجربه عاشقی در زندگی است.
به عشق اول و آخر زندگیت تبریک بگو و این پست رو بفرست براش
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/71844" target="_blank">📅 21:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71843">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">نیروهای «ارتش ملی یمن» (تحت حمایت عربستان) تصاویری از انهدام ۹ دستگاه خودروی نظامی حوثی‌ها (انصارالله) با استفاده از موشک‌های ضدزره (ATGM) در جبهه غربی مأرب منتشر کردند و مدعی شدند که تمامی سرنشینان این خودروها کشته شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71843" target="_blank">📅 20:50 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71842">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cs7mdWr6ofUK4Mz5hMJDEhpzhoYFDz5XJbjpzkTXrBda4bSJtG6uVAol-nWNeld_0uafkeJ4lsPUDuTC2TrXzkUkVDNf7FMBtBrRjnKMh0kPVP8xnB2_r6t9fI_mGm7YTJVq10azZAuftcT_wWguxDZetfCINEIaIIj39CrTOJ-JVXZ8l64LKTW1lTVzme3Z_balySg0BzPes_sfLF38JpkX7tTofsH0pjRh-OpeylTB8y5jl4yF7PC2qkN_2_dc7PrnBRglpCkin8Upcl920Y0SfrIlAaEiLwV1AFoJq5Ovve1Bzf_CJ1-Fq7DCLl85p2MdkrBn9xxpSZuHmOW5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، در پاسخ به پرسش شبکه «نیوزنیشن» درباره اظهارات اخیرش مبنی بر اینکه احتمال «نابودی» ایران را بررسی می‌کرده است، گفت: «باید دید چه پیش می‌آید.»
ترامپ اظهار داشت که ایران در حال حاضر خواهان توافق است و افزود: «اگر توافق، توافق درستی نباشد، حتی به آن فکر هم نمی‌کنم. اما در حال حاضر، آن‌ها می‌خواهند توافق کنند، چرا که در همه زمینه‌ها در حال باختن هستند.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71842" target="_blank">📅 20:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71841">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ به «نیوزنیشن»: آمریکا با حوثی‌ها در حال گفتگو است.
حوثی‌ها نیز مایل به دستیابی به توافق هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71841" target="_blank">📅 20:16 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71839">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=km-Lc_6i6F2LYw_s4D9D2LAveqvQcTtJHxN8BNO59N4QCAnM5SgjFEe15A1f-_FL7xcnSb1U_ncXUR-UsgGlAGD7jVxTVBwIbKSZbx9-4W50TrgVbCb6llkaEhOUpwJbjl8uAY2_7hSYenCAFiEZXvys42vMKL_1UuAMZ48TcNCreAol3QBUAbrIVSFAw7t5KxON87sI_RWtUJ8UargGPWBgX7a_oORuTtG6GaXojJ6gCvbgl3BwHCm2yBf3qm1gmZhXrUzjCdmduV_cEg4kCQbDMmDBpsMOHaOuddldFcObvWV4aEejdFydeedbGGZiVjpuxmt1igLaDvGTQOChPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/429ba373cd.mp4?token=km-Lc_6i6F2LYw_s4D9D2LAveqvQcTtJHxN8BNO59N4QCAnM5SgjFEe15A1f-_FL7xcnSb1U_ncXUR-UsgGlAGD7jVxTVBwIbKSZbx9-4W50TrgVbCb6llkaEhOUpwJbjl8uAY2_7hSYenCAFiEZXvys42vMKL_1UuAMZ48TcNCreAol3QBUAbrIVSFAw7t5KxON87sI_RWtUJ8UargGPWBgX7a_oORuTtG6GaXojJ6gCvbgl3BwHCm2yBf3qm1gmZhXrUzjCdmduV_cEg4kCQbDMmDBpsMOHaOuddldFcObvWV4aEejdFydeedbGGZiVjpuxmt1igLaDvGTQOChPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای:
ما انگلیسی‌ها رو از ایران خارج کردیم ولی الان کشور افتاده دست چندتا بچه اطلاعاتی!
تشکیل مافیای فروش نفت هم از دوره روحانی و توسط زنگنه (شیخ الوزرا و وزیر نفت سابق) شروع شد.
درحال حاضر چهارنفر دارن نفت ایران رو میفروشن [حسین شمخانی، روح‌الله رضوی (دامادِ سخنگوی جریان پایداری)، علی بایندریان و محمد‌هادی مومنین].
پسر شمخانی(حسین) تو این چند سال، بالای 30 میلیارد دلار یعنی چندین برابر ثروت ترامپ فقط نفت فروخته!!
این چهارتا فقط تو فروش اخیر نفت ایران، 1.5 میلیارد دلار پول به جیب زدن!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71839" target="_blank">📅 19:30 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71838">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nVzpHbyGmZ2MdjOfLEbaNVNcZZvOKEB4Z27M6Fahw5iW7CuIB7CyuFe7jhmbtxHhhQkT01qNHDnjZO0YTch2auOvncUYOIeeDHQgcujz1ACAeGa4qc-6YfhK65UPXuKYePkAo6HPFIcMEmJzwAuBJR5I0sMYkbQbqFVn3Rha5GdcZbgE4_yGxqQ4dZkFUq5OCnefOsbIfNxqJ4n8WPh7On7VGX5t9B0Jlqub7DNgx8j_zTDMM3qFXYSf5R6Zqy2PKiSySK4k9koiYTUHnLCRRwv6IolmHbPX4h5X559b35mh3NFoqu5s_4z4Pk2SdUdTTdvb4JsIg32wP9RXKY9PPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حساب تلگرام در پلتفرم ایکس این تصویرو از ایلان‌ماسک منتشر کرده و نوشته:
ثروت کاذب:
🛩️
💰
🏎️
ثروت واقعی:ممه‌های ۸۵ ایلان ماسک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/71838" target="_blank">📅 18:56 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71837">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=FbFpgAnOt-9tTBNPRc_Vjg3DxMfFPjXpQCl_CDb85BLs9U4KAtjdqUkpZmL0m9rcoDYzMahIZ_9YbeyurrwtxiMKM_QExY33WS8MYl0MN4YqraVSRax8QIM-J2jG7b2pFk-WiimITX6AFsJxRTAHU-K9ci8G8BIh9kD1NtU69Sc1qbg8NhuiA1JKelXsRiTNmu_O8xCcdDtcUGidF-LMBGHis20AzwdQ8Y4IoxyeVHPsnqeh7MRjYNCjZGiyFM_JDcE4FeKsc9YF794tmRPCfteWdPqoxF2XxEUSn3i3LVHumCXb53xhvHCUOh6UmRpKWWFRfBfm--iCD3RMVYqz1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/915a75db7b.mp4?token=FbFpgAnOt-9tTBNPRc_Vjg3DxMfFPjXpQCl_CDb85BLs9U4KAtjdqUkpZmL0m9rcoDYzMahIZ_9YbeyurrwtxiMKM_QExY33WS8MYl0MN4YqraVSRax8QIM-J2jG7b2pFk-WiimITX6AFsJxRTAHU-K9ci8G8BIh9kD1NtU69Sc1qbg8NhuiA1JKelXsRiTNmu_O8xCcdDtcUGidF-LMBGHis20AzwdQ8Y4IoxyeVHPsnqeh7MRjYNCjZGiyFM_JDcE4FeKsc9YF794tmRPCfteWdPqoxF2XxEUSn3i3LVHumCXb53xhvHCUOh6UmRpKWWFRfBfm--iCD3RMVYqz1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجلس نمایندگان آمریکا «قانون لیندزی او. گراهام برای تحریم روسیه و ایران (مصوب ۲۰۲۶)» را با ۲۶۲ رأی موافق در برابر ۱۵۹ رأی مخالف تصویب کرد و این مصوبه را برای امضا نزد رئیس‌جمهور ترامپ فرستاد.
این لایحه «ناوگان سایه» روسیه را هدف تحریم قرار می‌دهد، اعمال تعرفه‌هایی تا سقف ۱۰۰ درصد بر پنج خریدار بزرگ محصولات انرژی روسیه را مجاز می‌سازد و «قانون تحریم‌های ایران (مصوب ۱۹۹۶)» را تمدید می‌کند؛ این موارد در کنار سایر اقداماتی است که روسیه و ایران را هدف قرار داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71837" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71836">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71836" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/71836" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71835">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxxT0Os--ZRHI3OWSHgdmtO303Aw2AT-hRXMKlL_kRMRNz-So1-LpTy2XmRNaJhMsEq2bNu5ItTg2bxCpbJzq15PZAhBkC55LYNho7sEBfDkbvNUMwS8xdY_M0XSkROXJcf2q1VZxQvg06eYUy70fxvxy7_UARhKPcT6MzQHx880X6aYNw5sY7-ZqF8jwfR-DHjM1jpor9bgAOTU-FDhDa7n7FNnilP0V9uKlsCyj9HhbzcKrj7HM9JkM_bS7FfHshXCcygETnJB7lnMdmmJiwQ8Hgp5Q8Mh41KrnJH6wWV9AGTD_4xO1r_PpZBx_qvgDKi403AbILeZ3nFeZmzZ9g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71835" target="_blank">📅 18:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71834">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=NCnyye7olpowq5wGHG1S1vt0I5H1HtlALJFwjBv0HvvdoFyh1lPiYIf9VrNQ5XaSV83j-JKsH7HjGrIQCX5Hx4_2boobtQ_yigQKKlSTM6Tgpi7XNdI4aSuYJZKiG2e0tRO1vSsQDwQz-kgk2St44zbASyfvfM46mq9mV4vY4j8Yty0xLPxymwwdYXvhnNz4wO2f1vn8W64xOHqAHyAEyE-rQ7Wqdxl0oGPj3U14AhmiOf8WGDTcDUikydX21Dgajn9-k4vpZttYGSU_4H57sfY8HGSGghZyx-DsM82GKWNxMiE2U_2MY3JYBu182zzcFzEGl8pGGOFfz0q8OJZt1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b71f8c82b6.mp4?token=NCnyye7olpowq5wGHG1S1vt0I5H1HtlALJFwjBv0HvvdoFyh1lPiYIf9VrNQ5XaSV83j-JKsH7HjGrIQCX5Hx4_2boobtQ_yigQKKlSTM6Tgpi7XNdI4aSuYJZKiG2e0tRO1vSsQDwQz-kgk2St44zbASyfvfM46mq9mV4vY4j8Yty0xLPxymwwdYXvhnNz4wO2f1vn8W64xOHqAHyAEyE-rQ7Wqdxl0oGPj3U14AhmiOf8WGDTcDUikydX21Dgajn9-k4vpZttYGSU_4H57sfY8HGSGghZyx-DsM82GKWNxMiE2U_2MY3JYBu182zzcFzEGl8pGGOFfz0q8OJZt1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
این جانفدا‌ها چجوری میتونن به دولت کمک کنن؟
پزشکیان:
ما باید کاری بکنیم که چرخ کارخونه‌ها بچرخه. برای این کار باید مصرف گازمون رو کنترل کنیم، بنزین رو کنترل کنیم. با همون حمل و نقل عمومی بیاییم بالا تا بتونیم دشمن رو ناامید کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/71834" target="_blank">📅 18:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71830">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=Z0lk_jPlAnpnOMj9_rhHCje6b-I2DFNFJkJBtiAfSqXMoPzr-avyL2jU982_ejIZBg32dGQBpUAQBBsSl9R-RbmBmDrRjOlDDCV96Em1qkS3g3_zRnL-YFrjtRBgR0SSUq6kbO81Cd_6sjRvA7oUe8kpssvRvEt7brmEQBktSVZMJLgBZvf4yBHJoohUOpoKzMhATqt9VxFtoIKFD8AW_NhyvYZRtkwY9IZHnK0zl0ZUBzkYOyee3Bdq_zzLCkEINs4tBup2_bl6Xg34dqzVhuL831JMLPq2zF0kNICzqQVNPtfbwHXMJR9AL7ypP2oyMWf0iV6zsuUZvW4_bPSGGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fefe1a2487.mp4?token=Z0lk_jPlAnpnOMj9_rhHCje6b-I2DFNFJkJBtiAfSqXMoPzr-avyL2jU982_ejIZBg32dGQBpUAQBBsSl9R-RbmBmDrRjOlDDCV96Em1qkS3g3_zRnL-YFrjtRBgR0SSUq6kbO81Cd_6sjRvA7oUe8kpssvRvEt7brmEQBktSVZMJLgBZvf4yBHJoohUOpoKzMhATqt9VxFtoIKFD8AW_NhyvYZRtkwY9IZHnK0zl0ZUBzkYOyee3Bdq_zzLCkEINs4tBup2_bl6Xg34dqzVhuL831JMLPq2zF0kNICzqQVNPtfbwHXMJR9AL7ypP2oyMWf0iV6zsuUZvW4_bPSGGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسجدی در شهر کوهات، واقع در ایالت خیبر پختونخوا پاکستان، هدف حمله یک بمب‌گذار انتحاری قرار گرفت که در پی آن بیش از ۱۰ نفر کشته و بیش از ۹ تن دیگر زخمی شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71830" target="_blank">📅 17:36 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71829">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دقایقی قبل صدای دو انفجار از سمت تنگه‌هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71829" target="_blank">📅 17:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71827">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ارتش اسرائیل روز پنج‌شنبه اعلام کرد که نیروی دریایی اسرائیل و یونان دو هفته پیش یک رزمایش دریایی مشترک در دریای مدیترانه برگزار کردند.
این رزمایش با مشارکت دو ناو موشک‌انداز اسرائیلی و دو ناوچه یونانی انجام شد و بر تقویت هماهنگی عملیاتی میان نیروهای دریایی دو کشور تمرکز داشت.
شناورهای حاضر در این رزمایش، سناریوهای متعددی از جمله اجرای پروتکل‌های اضطراری و همچنین شناسایی و مقابله با تهدیدات دریایی را تمرین کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71827" target="_blank">📅 17:01 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71826">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=H4T5PLnhFnMGthhYfDOFHTqn_jmCGyV9fZvhSmHSKT3YCkpMPHCBwBIpX50OKyriqCsdfnCdhhck3qZWz_DrcyEq4GPQg-SkXuD9vqz9ntAlp1gJHIzWywWySj5X7EGqFwWKIVAvQIXINX_366X2Cetmo1HDflEhLWl2YWKqBv4rrmPheCN9Yz_A4DjqdPRrHQRpGq-xbFTxSfRDT3J7q1CSoiFlAdQnbYIWmQsh2IJzjKm7VVHiUcgfYZP0nlgSTviCRUJt8p_AUg10uYmFUWLRD__jH97fP3nu6kjrxdZS5nxaKMWhLDhP1_hvFDiDYH3CP5WLh6ES-Sse6i9gMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00efcbd138.mp4?token=H4T5PLnhFnMGthhYfDOFHTqn_jmCGyV9fZvhSmHSKT3YCkpMPHCBwBIpX50OKyriqCsdfnCdhhck3qZWz_DrcyEq4GPQg-SkXuD9vqz9ntAlp1gJHIzWywWySj5X7EGqFwWKIVAvQIXINX_366X2Cetmo1HDflEhLWl2YWKqBv4rrmPheCN9Yz_A4DjqdPRrHQRpGq-xbFTxSfRDT3J7q1CSoiFlAdQnbYIWmQsh2IJzjKm7VVHiUcgfYZP0nlgSTviCRUJt8p_AUg10uYmFUWLRD__jH97fP3nu6kjrxdZS5nxaKMWhLDhP1_hvFDiDYH3CP5WLh6ES-Sse6i9gMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند‌روز قبل حدود هزاران تریان که عمدتا سگ، گرگ، گربه، شغال و روباه بودن روبه روی پارلمان آلمان در شهر برلین تجمع کردن و خواستار به رسمیت شناختن حقوق جامعه تریان ها به عنوان شهروند عادی شدند
به آدم هایی که رفتارشون مثل گرگ، گربه، سگ و ... هست تریان می‌گن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71826" target="_blank">📅 16:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71825">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=A4Vb8xTBkICB6nJfQOCW4rjVHBXgiUyn2YuWONA0NUM0CqxTDeR1TkdLd_phVDRBdlMoIYHpE-XRI5H91Cme77epbXU2mpwhnOAxr8Q8uP3B9-EPwYxziLa240a8aBQY73jsZHtaZW4w5v-Ulboy6RP7FQmeNW2l6suMFPhC0bSqS4SqPQLT-M8SnM20zdkF-H-_6bjbWNUN6forKUUWk_vFUaS7DTI_2U_cFJDbmOUBfoqLen6yJpUDH37UpGWUXbonpxbKmD4v68N2TwjTcK4m8sb4WttR4pIbhWVjlAKi6pHsiN3NdtaLCJL35FqOqZwdvjHbljXvtQ8XpkBTZ4MbKwcixNL2OaUZYX0baBGQCsUdaPzE2yFhxlqdbUQh9KEhBcWoTt9OHEtXu7nzzVC6iFBKqIo55auBlQx0a2nPje8TZmloiV2g-Nb6Rd3nCU2It79foz0WcTzYAhIVSOmRMxlvYPK7zLprA5QoQ0DyhifGlyMBTQfg1yTyiXfAEgv_KvLHplWyt3Hy8HxMoqMJJgegxhGdWLnVLbX62ekvmyQ7DEQhJUzag1iO_NkDVzI7GTxXrwfjGjT3PGdRhU6WW7KEFuMmmGkTSR5lBiGDI_LeEpNqy4xE3ZWzLh0Bldj5FdO4MDTv7AVIocRDeJgYKn8WDu38WNLaaBReWjY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2db0ed7cac.mp4?token=A4Vb8xTBkICB6nJfQOCW4rjVHBXgiUyn2YuWONA0NUM0CqxTDeR1TkdLd_phVDRBdlMoIYHpE-XRI5H91Cme77epbXU2mpwhnOAxr8Q8uP3B9-EPwYxziLa240a8aBQY73jsZHtaZW4w5v-Ulboy6RP7FQmeNW2l6suMFPhC0bSqS4SqPQLT-M8SnM20zdkF-H-_6bjbWNUN6forKUUWk_vFUaS7DTI_2U_cFJDbmOUBfoqLen6yJpUDH37UpGWUXbonpxbKmD4v68N2TwjTcK4m8sb4WttR4pIbhWVjlAKi6pHsiN3NdtaLCJL35FqOqZwdvjHbljXvtQ8XpkBTZ4MbKwcixNL2OaUZYX0baBGQCsUdaPzE2yFhxlqdbUQh9KEhBcWoTt9OHEtXu7nzzVC6iFBKqIo55auBlQx0a2nPje8TZmloiV2g-Nb6Rd3nCU2It79foz0WcTzYAhIVSOmRMxlvYPK7zLprA5QoQ0DyhifGlyMBTQfg1yTyiXfAEgv_KvLHplWyt3Hy8HxMoqMJJgegxhGdWLnVLbX62ekvmyQ7DEQhJUzag1iO_NkDVzI7GTxXrwfjGjT3PGdRhU6WW7KEFuMmmGkTSR5lBiGDI_LeEpNqy4xE3ZWzLh0Bldj5FdO4MDTv7AVIocRDeJgYKn8WDu38WNLaaBReWjY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امانوئل مکرون، رئیس‌جمهور فرانسه:
تنگه هرمز عملاً مسدود باقی مانده و هیچ توافقی برای بازگشایی آن وجود ندارد.
در واقع، وضعیت تردد نسبت به چند هفته پیش بدتر شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71825" target="_blank">📅 15:58 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71824">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=MivBeBfNySkJuMaWUa1OS9AX4TBT8_g0-87rlQjNl7acqI7P6Frmcy03Xkmj5rtLgH3LyxKY_EhYFFRPVwkDiLgAlsygJNonjHNP7GSp5RDcLUz60d0m2IXnLMANU42m7dpOsKtJiZL7OpGiKupmu5-U2ithj48qngaEwRX-hR6EvrCcaP6Mkz4vKnfLK-6VLki1r8iaQ6S5FBIGyNal8Ja2sH3YMINAYN5pYfQKd7GX5MCtvJK3xzMpaGzDzQpce02qSDUwsLf9Sts9KCfp0pGzpDm4vDSryk2AymXUzFsUpT2hpm0pAnBl7UGHT7pN6H-iJo6Q7luGerkndH1QtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb0b52718.mp4?token=MivBeBfNySkJuMaWUa1OS9AX4TBT8_g0-87rlQjNl7acqI7P6Frmcy03Xkmj5rtLgH3LyxKY_EhYFFRPVwkDiLgAlsygJNonjHNP7GSp5RDcLUz60d0m2IXnLMANU42m7dpOsKtJiZL7OpGiKupmu5-U2ithj48qngaEwRX-hR6EvrCcaP6Mkz4vKnfLK-6VLki1r8iaQ6S5FBIGyNal8Ja2sH3YMINAYN5pYfQKd7GX5MCtvJK3xzMpaGzDzQpce02qSDUwsLf9Sts9KCfp0pGzpDm4vDSryk2AymXUzFsUpT2hpm0pAnBl7UGHT7pN6H-iJo6Q7luGerkndH1QtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سباستین گورکا، مسئول ارشد مبارزه با تروریسم در کاخ سفید:
قیمت بنزین برایم اهمیتی ندارد، چرا که وقتی پیروز شویم — که به‌زودی هم خواهد بود — قیمت بنزین ارزان خواهد شد.
مسئله، انتخابات میان‌دوره‌ای نیست؛ مسئله، نابود کردن کسانی است که قصد کشتن آمریکایی‌ها را دارند.
اگر فکر می‌کنید این موضوع اهمیت کمتری نسبت به قیمت بنزین دارد، شما آمریکایی نیستید. تمام.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71824" target="_blank">📅 15:23 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71823">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=ZcnVh7hl6yzmfmgzgrWznzuy9kUe31B9ZD7WAWCYjnyrkhW031_ld1UOLqOdme6CB1y-uKmMnDPMdotKKbLDTaHjDIsvfLieBRm8RDZSjqrslHHRQgq0pcb3YmhTOn7_DWDsbKavoGEKQX-wnf_JX7J5R0mzb-UXolDJn9fhrxQSYVEdgVB-yIPNYpU_pHM1QMJOCvIwbWg-Ir17SbBlzTjc_EeIl22bdqwP9UMOXOLB54R173js-2Z2kjQdEF5Bz0glpzJ2Fg4N69TtiSbz781Q8z6NhicJpsEwdIbR2vY18E1k2CuP-Dn9vmeS3iVh-PnnBcoQ5hExTeUokB2uSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b2eeaeb9e.mp4?token=ZcnVh7hl6yzmfmgzgrWznzuy9kUe31B9ZD7WAWCYjnyrkhW031_ld1UOLqOdme6CB1y-uKmMnDPMdotKKbLDTaHjDIsvfLieBRm8RDZSjqrslHHRQgq0pcb3YmhTOn7_DWDsbKavoGEKQX-wnf_JX7J5R0mzb-UXolDJn9fhrxQSYVEdgVB-yIPNYpU_pHM1QMJOCvIwbWg-Ir17SbBlzTjc_EeIl22bdqwP9UMOXOLB54R173js-2Z2kjQdEF5Bz0glpzJ2Fg4N69TtiSbz781Q8z6NhicJpsEwdIbR2vY18E1k2CuP-Dn9vmeS3iVh-PnnBcoQ5hExTeUokB2uSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه:
از مشمولان غایب تقاضا داریم بیان خدمت ، هر ارگانی خودشون دوست داشته باشن پذیرششون ‌میکنیم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71823" target="_blank">📅 15:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71822">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=tyhMbdzAlV7ljrSF6Ik73TFYYwF8pH_Cjpd6GTxt5J-iL4hps9B3M2hslIbAAA7drFuKu_hgLPqIt_ON-QvcyK-Qza_2U4wTCFSoSRsnQJ_8VN36IiqfGCnpMLgZtBwfSn-16kRTNNEovyAAiiWCfDxYBQcW4qlB1IRn203qXtW8PlAlp1_2mgs-hqWL1w4XxFhxqic5RB6oGAc92rhH_Djv-etynEBBTTjZizSofZbuV1LG6T0HYC9Ss1bUOY-giDj8Ds9CJebpjJ1gxUK6jn0zk8NkJGePtig5QdTjlsWm3L0NIK-xT6OPrRE1GKzcXef4kwiqcndAidQ_0zz6LjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc25aa2680.mp4?token=tyhMbdzAlV7ljrSF6Ik73TFYYwF8pH_Cjpd6GTxt5J-iL4hps9B3M2hslIbAAA7drFuKu_hgLPqIt_ON-QvcyK-Qza_2U4wTCFSoSRsnQJ_8VN36IiqfGCnpMLgZtBwfSn-16kRTNNEovyAAiiWCfDxYBQcW4qlB1IRn203qXtW8PlAlp1_2mgs-hqWL1w4XxFhxqic5RB6oGAc92rhH_Djv-etynEBBTTjZizSofZbuV1LG6T0HYC9Ss1bUOY-giDj8Ds9CJebpjJ1gxUK6jn0zk8NkJGePtig5QdTjlsWm3L0NIK-xT6OPrRE1GKzcXef4kwiqcndAidQ_0zz6LjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مدرسه لاکچری؛ شهریه سالی ۳۰۰ میلیون!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71822" target="_blank">📅 14:35 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71819">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=aFEBR3gzQaW84SgY8rEd-wfs1TmI1s1vJh5bxR8GbvWRlYp48g96mRdak0ecKkQNzKUVFu-M0QPuomLjgn8ED5OhN68bCqFQhzR-M-Z5C6i7anOAtVlL57eQm_qhDn-zEAD9c9QG32ztdD0txpovI_TKvxyGszrI5KL-JOv_xsDpHTwj5P7dfSzu29ds2UXCVp_59QfqvGeHcXegzOGHz3pDLOTFQkOTTT-CaSttIbPtPKlzxFd_80WCtu8uLgB-UPgMpy6SNQjOxivSFiWbSLM-2Cd32O8zlqCHqKpE_WqDjz_0PxZUmoUbN4BkmEN2uG_4LHQMmTFOdleyv7I-5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a49d38d.mp4?token=aFEBR3gzQaW84SgY8rEd-wfs1TmI1s1vJh5bxR8GbvWRlYp48g96mRdak0ecKkQNzKUVFu-M0QPuomLjgn8ED5OhN68bCqFQhzR-M-Z5C6i7anOAtVlL57eQm_qhDn-zEAD9c9QG32ztdD0txpovI_TKvxyGszrI5KL-JOv_xsDpHTwj5P7dfSzu29ds2UXCVp_59QfqvGeHcXegzOGHz3pDLOTFQkOTTT-CaSttIbPtPKlzxFd_80WCtu8uLgB-UPgMpy6SNQjOxivSFiWbSLM-2Cd32O8zlqCHqKpE_WqDjz_0PxZUmoUbN4BkmEN2uG_4LHQMmTFOdleyv7I-5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشار سلطانی روزنامه‌نگار و فعال رسانه‌ای فروشندگان نفت را لو داد!
از داماد سخنگوی پایداری‌ها تا خانواده شمخانی
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71819" target="_blank">📅 14:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71817">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=t29ziZiBFEB84rfkAbuD1XGDDIioursrbaJMXd5n4YM4EnVXrP-UlZkjWfEP6eH_2yVk7sS_nh-mzLDtfyu4HzV30gBot8gzsPHFYE59xwGF0rhFrz-4y7_8RtvhgZiIR0kdu__fhulgHpOS3XrtmZ9MvJZV8wA_ccpx4yBKUzsrk2bymPvvZTZtEO0taBn6PnalyicTx-isPPQUdKKHoOaA4ZEfgNgvFr4LXWsdpnoqQarl9MJx580Cx6f4zkLAtg1nq4kqclLKBmHN2WQtEUALcPScUwq1Hov4MqeJGS5hKmLVNd_IFdcVCjmLDfnwXy0fpjqrO3F8G9tI4VAqrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2b23b11f.mp4?token=t29ziZiBFEB84rfkAbuD1XGDDIioursrbaJMXd5n4YM4EnVXrP-UlZkjWfEP6eH_2yVk7sS_nh-mzLDtfyu4HzV30gBot8gzsPHFYE59xwGF0rhFrz-4y7_8RtvhgZiIR0kdu__fhulgHpOS3XrtmZ9MvJZV8wA_ccpx4yBKUzsrk2bymPvvZTZtEO0taBn6PnalyicTx-isPPQUdKKHoOaA4ZEfgNgvFr4LXWsdpnoqQarl9MJx580Cx6f4zkLAtg1nq4kqclLKBmHN2WQtEUALcPScUwq1Hov4MqeJGS5hKmLVNd_IFdcVCjmLDfnwXy0fpjqrO3F8G9tI4VAqrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری مهر:
هزاران نفر در رژه «جانفدا» در تهران شرکت کردند و از میدان امام حسین تا میدان انقلاب راهپیمایی کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71817" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71816">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=rZrfgA7hY3tPs-juyZxtp94fnswlMePpajQDJjDF0DJW0GXO0ghvFGuhQ83Sya9N3ivaNeE__MRYlrAsB6w-DQTd48SaswAgS6cvk473dxQK-5_XHoOZIe4SKCcPlfAs6ClQzwjv1wt-mwUHOWYZF4J2j54MhSQ3X1Y_tW1Zye6746ztQFIKWVq0kq9xVIin4wvOgvx-tL24Bf-6Q7c20HtQboKuihI4J-chmhWsCJB1tD7cezTImFkY6a1dziLHOG_JID-X6hRJIT4B6pbxxUGNlbq4lJQGZ1yMXOFJjs7HxanQim1XBYFVs9Wax7O7hX5GVojtsgDUSMckqtdFbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c319028d9f.mp4?token=rZrfgA7hY3tPs-juyZxtp94fnswlMePpajQDJjDF0DJW0GXO0ghvFGuhQ83Sya9N3ivaNeE__MRYlrAsB6w-DQTd48SaswAgS6cvk473dxQK-5_XHoOZIe4SKCcPlfAs6ClQzwjv1wt-mwUHOWYZF4J2j54MhSQ3X1Y_tW1Zye6746ztQFIKWVq0kq9xVIin4wvOgvx-tL24Bf-6Q7c20HtQboKuihI4J-chmhWsCJB1tD7cezTImFkY6a1dziLHOG_JID-X6hRJIT4B6pbxxUGNlbq4lJQGZ1yMXOFJjs7HxanQim1XBYFVs9Wax7O7hX5GVojtsgDUSMckqtdFbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عادی ترین شوخی پسرا
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71816" target="_blank">📅 12:41 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71813">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71813" target="_blank">📅 12:05 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71812">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سازمان عملیات دریایی انگلیس: امروز یک شناور دیگر در آب‌های تنگه هرمز، مورد اصابت یک پرتابه نامشخص قرار گرفته و در آتش می‌سوزد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71812" target="_blank">📅 11:09 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71811">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=pmFExqYGwD4oLkxVt1YmaY65DzIlbvNUAs5_IjHGgjlN38NKraPMBpSEOfaxyEUYCtojh1QGprvnndL0a0MbGazCmd4qtnjas_cNQ-496Q2s-nBhyn-2ukw5zAplXFDbFpB051fQZY71JEmY0Hp6dY7W6vEJ9W3jxm4xzZreDYezdH13mXLCIJUjRt0bcpIWt5FRsBdS4kqcZdV-hGBb2hpRNpzQ7fnbSMlj5FFxVNR3GITW7QSznA5eXmlb4FX7h4rXiP0077F-V3duZOANlj2V8b_hAujt_MvZTWk2uwC-W40HD7w-mYyD7ZbM3OEMQfnT4YqFrg-p7u3odiHhkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6831b24b0.mp4?token=pmFExqYGwD4oLkxVt1YmaY65DzIlbvNUAs5_IjHGgjlN38NKraPMBpSEOfaxyEUYCtojh1QGprvnndL0a0MbGazCmd4qtnjas_cNQ-496Q2s-nBhyn-2ukw5zAplXFDbFpB051fQZY71JEmY0Hp6dY7W6vEJ9W3jxm4xzZreDYezdH13mXLCIJUjRt0bcpIWt5FRsBdS4kqcZdV-hGBb2hpRNpzQ7fnbSMlj5FFxVNR3GITW7QSznA5eXmlb4FX7h4rXiP0077F-V3duZOANlj2V8b_hAujt_MvZTWk2uwC-W40HD7w-mYyD7ZbM3OEMQfnT4YqFrg-p7u3odiHhkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قائم‌پناه، معاون پزشکیان:
حساب کردم اگر بنزین ۸۰ هزار تومان شود و برق و گاز و ... را هم گران کنیم، می‌شود ۷میلیون یارانه در ماه به هر نفر داد‌.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71811" target="_blank">📅 11:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71810">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGUBu74FbcSngzepdZ9nkcqZwH6nZTROoSI0duke_Koz-nrIaOcJo1-xW535nF75FU--vzQ3tDur0q_DgBUljWs_iFq6r8u2YzmjhaKl7JA4IGKBRPdfO9RJEnpyvAtJX5qNDhxHOZlviPw-zNM-S2bfYUh9-pboTuaT3TvDcZj4H8BSjVVg1j2vqFSja9bV6-4VUV85jXPMVlWmOr_U9jModNvMJ3Z5G2uKF1Jr8Y1VKwKwdF31gWKHbKxgPcCKknncTW3SV7GjA-7AABWHb79TK7jfcKYuFAmQdxgdtTmawO4KeCfd4KXDqnxZ9kiLfhEVwnLsfATQxcmgH-njDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇸🇦
🇨🇳
—مقام‌های اطلاعاتی آمریکا ابراز نگرانی کرده‌اند که در صورت نهایی شدن فروش برنامه‌ریزی‌شده ۲۴ میلیارد دلاری ۴۸ فروند جنگنده F-35 و یک موتور یدکی به عربستان سعودی از سوی دولت ترامپ، چین ممکن است به فناوری‌های حساس این جنگنده دسترسی پیدا کند.
بر اساس گزارش نیویورک تایمز، یک ارزیابی اخیر از سوی آژانس اطلاعات دفاعی آمریکا (DIA) بر دسترسی چین به تأسیسات نظامی عربستان، روابط دفاعی پکن و ریاض و همچنین استفاده گسترده از فناوری‌های مخابراتی چینی در عربستان تأکید کرده است.
تحلیلگران این پرسش را مطرح کرده‌اند که آیا آمریکا و عربستان می‌توانند تأسیسات مرتبط با F-35 را به اندازه کافی ایمن کنند و مانع دسترسی نیروهای نظامی یا اطلاعاتی چین به فناوری‌های حساس شوند؛ به‌ویژه رادار پیشرفته و سامانه‌های شناسایی و نظارتی این جنگنده.
نگرانی‌های مشابهی پیش‌تر درباره فروش احتمالی F-35 به امارات متحده عربی نیز مطرح شده بود؛ به‌خصوص پس از گسترش روابط نظامی، اطلاعاتی و فناوری ابوظبی با چین. آن قرارداد در نهایت به مرحله اجرا نرسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71810" target="_blank">📅 10:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71806">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=S6E0vUsRXsRYxs45HuLe_WjcLec9gIWryaJ7JVlBGgqHKsayYuIKtHtPjes4RPEUze-T-GfNIjcnsR64ABSG6dYLw602Xi__i8d0xTkPBU7UCgvGRJKcF5KFUiQYX8ErqUQjBhIzCHSREkAWWgTKfAEC1VR8Dt0CdcMhP2U_ihanSHFrYrhtyHHYRB-PGPK337-tmzt3Ze3Ck0tR2GwOrBpxZFUQ3UPq4e2TvjF6YPnQ1TEXmMC6NXbw74FhENFQskTgVAgZunA7MXKbcImiwti-HC8z2Sg5zrc0CCaqWTGovyc0b5YQA1Ljpn51_yYUYM_8P_dZPymfSNDLybYU0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44d9bc13c5.mp4?token=S6E0vUsRXsRYxs45HuLe_WjcLec9gIWryaJ7JVlBGgqHKsayYuIKtHtPjes4RPEUze-T-GfNIjcnsR64ABSG6dYLw602Xi__i8d0xTkPBU7UCgvGRJKcF5KFUiQYX8ErqUQjBhIzCHSREkAWWgTKfAEC1VR8Dt0CdcMhP2U_ihanSHFrYrhtyHHYRB-PGPK337-tmzt3Ze3Ck0tR2GwOrBpxZFUQ3UPq4e2TvjF6YPnQ1TEXmMC6NXbw74FhENFQskTgVAgZunA7MXKbcImiwti-HC8z2Sg5zrc0CCaqWTGovyc0b5YQA1Ljpn51_yYUYM_8P_dZPymfSNDLybYU0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پول که باشه، اسنوپ داگ هم واست قِر میده؛
دیروز تو‌ مراسم ازدواج یه زوج ایرانی تو لس‌آنجلس، اسنوپ داگ هم به عنوان مهمان ویژه حضور داشت که هم خوند و هم رقصید!
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71806" target="_blank">📅 10:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71805">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=LplyZOe70v5dmgUmiUErBuhn6Loy7QjD85uvP9UBMqB-7-Rra14q2vDoUv-jLUQ6d9EnskMtTR--zaeF_Sb7rtGa0mcdEgcrCzQW4v8eCEW9E8t82m75NcFUvx4Jr1EtvF7IqDB4Ly7ECsgVkI0bDhN_tSSukB2XsEO-tcnZOwP1932fWkKbGSVKlCGZ7aqedj2ukGAKBGSREkK2IftxdnoPdiTryN-jE6Ayxm7fDNnGddXIX-pi6vU8e6SiQgQBSgDJwy283U4qMLykSAA84klcuTwJ0P-e6fTgliDoimGeubeVU9js5CpcPp3GLw9JFTRYYa3uZ2GqIFEiAyt_8Xo92Dm_flMGXKVMYObUmGUlKRroAKKa-RlFJQuK8cKqEBiFxdvGetq0zERdZn-MfziS6Nv4p2hckYFTUi8bAHlIXpxZSx_MWlHSj-d2F8kJvrtUeVcyC-gPYzoMsXt7KMbTc_XGUWLUL_ap-hBYQnBvwXvUC1mjuPqguisPkL6aQK3Rph-fi62h7pYQ4IkUs9A4e5ajizCoujkKjh8F-kV1itkJXOtI7xAW6W2XP0tAahhzvAkdpl38hLbeo57FTuhPeF_nHtF32074qSwe8AWG1Hzx1pIDSEPXHjISF0Oj84QuYqGmoireoSkgsmYJ3Wrk2YWTRYTfwlnJUm1JHoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/102dbc4ee1.mp4?token=LplyZOe70v5dmgUmiUErBuhn6Loy7QjD85uvP9UBMqB-7-Rra14q2vDoUv-jLUQ6d9EnskMtTR--zaeF_Sb7rtGa0mcdEgcrCzQW4v8eCEW9E8t82m75NcFUvx4Jr1EtvF7IqDB4Ly7ECsgVkI0bDhN_tSSukB2XsEO-tcnZOwP1932fWkKbGSVKlCGZ7aqedj2ukGAKBGSREkK2IftxdnoPdiTryN-jE6Ayxm7fDNnGddXIX-pi6vU8e6SiQgQBSgDJwy283U4qMLykSAA84klcuTwJ0P-e6fTgliDoimGeubeVU9js5CpcPp3GLw9JFTRYYa3uZ2GqIFEiAyt_8Xo92Dm_flMGXKVMYObUmGUlKRroAKKa-RlFJQuK8cKqEBiFxdvGetq0zERdZn-MfziS6Nv4p2hckYFTUi8bAHlIXpxZSx_MWlHSj-d2F8kJvrtUeVcyC-gPYzoMsXt7KMbTc_XGUWLUL_ap-hBYQnBvwXvUC1mjuPqguisPkL6aQK3Rph-fi62h7pYQ4IkUs9A4e5ajizCoujkKjh8F-kV1itkJXOtI7xAW6W2XP0tAahhzvAkdpl38hLbeo57FTuhPeF_nHtF32074qSwe8AWG1Hzx1pIDSEPXHjISF0Oj84QuYqGmoireoSkgsmYJ3Wrk2YWTRYTfwlnJUm1JHoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهترین خواننده جهان به ۱۶پرومکس راضی نشد رفت برا خودش و داداشش ۱۷ پرومکس خرید
حالا حرفای مغازه دار:
آقا محمد مرسی که افتخار دادی اومدی از ما خرید بکنی
واقعا شهر ما خوش شانسه که چنین هنرمندی داره
ایشالا آلبوم های جدیدت رو با این گوشی ضبط بکنی بدی بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/71805" target="_blank">📅 09:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71804">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmf7h4wW-1pfpfCJxhQRUPFvrvvp2FtK22sbgP_V1wUKzoXLEGZSxLEtjBoViQUra9X95lRTbULw75N85criFbVVHakbZal7cscClrkH00QGy40_9jSwJCpS-Q8rDJa0VhVX8ukQmuIO11QOeGGwD8LS-mglKLAm_JuJ5ZGMIWi4j-bGGowQ8q47aio-mWC9oRSowTZA-JFCS-whGh5t8iSjXnu3OGBu4eV20CEn7ck8SvcTIfV-PRiKWqJnCHzkIc92Fwewliy7oJCgnPyGuK2r1intDbWY8yiIgNY3e734KeuD3Q2_2zf40srbb2akqq_YW7DUzWfvOfpiHUTGwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تامی پیگات، معاون سخنگوی وزارت امور خارجه آمریکا:
در حالی که مردم عادی ایران با سرکوب بی‌رحمانه، کمبود آب و برق و تورم سرسام‌آور دست‌وپنج نرم می‌کنند، مقامات رژیم می‌خواهند در نیویورک به خریدهای کلان و لوکس بپردازند. ما اجازه چنین کاری را نخواهیم داد.
ما اجازه نخواهیم داد که نخبگان رژیم ایران از فرصت مجمع عمومی سازمان ملل برای خریدهای لوکس و پرهزینه — که به بهای رنج مردم ایران تأمین می‌شود — سوءاستفاده کنند؛ آن هم در شرایطی که رژیم ثروت ایران را صرف حمایت از گروه‌های نیابتی تروریستی خود می‌کند.
ایالات متحده همچنان مقامات نمایندگی ایران در سازمان ملل، مقامات بازدیدکننده و وابستگان آن‌ها را از خرید عضویت در فروشگاه‌های عمده‌فروشی (مانند «کاستکو») یا کالاهای لوکس در اینجا منع خواهد کرد.
فروشندگان منطقه نیویورک: هوشیار باشید و در ارتکاب این تخلفات شریک نشوید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71804" target="_blank">📅 09:00 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71803">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=PFdbJ2B-b5AW9RmJ370wH5zzLjvULlXlycTzKWWkABSQUR-PhEPH_lg45kmlbfIspfYWmQqfxunT5yu3rYQUAKaHPC4G9yJ3wruYK5o8uBxIiuE9UzOuE5dk2pexrUDi1oVMbkQMCd5n7fySeUruBxMiadb4GI20kB6KsDYoiUK9y3Yr-8G025lRVFqEdpqCYOqTzlS7Oca6lU92rOO4dUA-_xifVCyhkMCOclNH_bfGe6Nz_x-G75tw-o2zw2A3U35ubcBoSEqqefvOE4jGazECM7B0TA9AzfMqFozI88f5yvK_zq7zIIBu6L_vPeYpjq-sFIR2xstPNIMR7e5KSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0d036df0a.mp4?token=PFdbJ2B-b5AW9RmJ370wH5zzLjvULlXlycTzKWWkABSQUR-PhEPH_lg45kmlbfIspfYWmQqfxunT5yu3rYQUAKaHPC4G9yJ3wruYK5o8uBxIiuE9UzOuE5dk2pexrUDi1oVMbkQMCd5n7fySeUruBxMiadb4GI20kB6KsDYoiUK9y3Yr-8G025lRVFqEdpqCYOqTzlS7Oca6lU92rOO4dUA-_xifVCyhkMCOclNH_bfGe6Nz_x-G75tw-o2zw2A3U35ubcBoSEqqefvOE4jGazECM7B0TA9AzfMqFozI88f5yvK_zq7zIIBu6L_vPeYpjq-sFIR2xstPNIMR7e5KSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
به گمانم آن‌ها در آستانه فروپاشی هستند. می‌دانید، وضعیت فعلی اقتصادشان بی‌سابقه است؛ بدترین وضعیتی که تا به حال داشته‌اند. تورمشان از ۳۰۰ درصد فراتر رفته است. حقوق سربازان، نیروهای نظامی و پلیسشان را نمی‌پردازند. اوضاعشان به‌هم‌ریخته و آشفته است. باید دید چه پیش می‌آید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71803" target="_blank">📅 07:32 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71797">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=Adxg7eCV3U0HClZV_E8WXTwBztZ6mNhe9scAlU1Y03RNO5I505ktVYH2G4HEUsEuUX7HSMNW5KFKDH4wgKa7-B5_PCmHCG1rNVFCXLartKJxKRJudR2Kc0gfTkBUz4Gnw98fxL3Uxak0t6FV-tCq4P3-obQylcfTYxS6On1J8ddlnGzROQEpBzP_CucxCmRFqq_DAcTTMn--D6suAoCI4t104E5gqA4mhBdLmUd-5ubURxKn_RpceOoGTO00ZunRC2ToQnyn4UMl6EAVhqmUKtD9th2OsKLcqteWy3-nlcmV9AtrSAFZIe7oEnk_aCtn81Ihi0QI_tNOlZr1ZaH56A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4759c454c5.mp4?token=Adxg7eCV3U0HClZV_E8WXTwBztZ6mNhe9scAlU1Y03RNO5I505ktVYH2G4HEUsEuUX7HSMNW5KFKDH4wgKa7-B5_PCmHCG1rNVFCXLartKJxKRJudR2Kc0gfTkBUz4Gnw98fxL3Uxak0t6FV-tCq4P3-obQylcfTYxS6On1J8ddlnGzROQEpBzP_CucxCmRFqq_DAcTTMn--D6suAoCI4t104E5gqA4mhBdLmUd-5ubURxKn_RpceOoGTO00ZunRC2ToQnyn4UMl6EAVhqmUKtD9th2OsKLcqteWy3-nlcmV9AtrSAFZIe7oEnk_aCtn81Ihi0QI_tNOlZr1ZaH56A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اتوبوس غیرنظامی اوکراینی در زاپوریژیا هدف حمله پهپاد انتحاری (FPV) روسیه قرار گرفت که منجر به مجروح شدن ۳ سرنشین آن شد.
محل این حمله در مختصات 47.7794347, 35.2161182 واقع شده است.
این منطقه پیش‌تر نیز در اوایل ماه اوت (طی بمباران یک گل‌فروشی در آن خیابان) و همچنین در ۲۱ اوت (در جریان حمله به یک مینی‌بوس) هدف پهپادهای انتحاری روسیه قرار گرفته بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71797" target="_blank">📅 00:34 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71796">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=p5Ta-D6eWxR2FLo2ttqU-jMU6Zvb07wIZyAYSg8vgxSEbll_e5id9Aoccs5OimgD9A90eOShIDwJGF3ptAE3XQQbcOpHB7ntJK2JjM8Xacar50nKzHnQo_k8Bld8MrM8lchcRZtjTDZ32QRtWBgweVHN5iiktq3rN6MGe5I1ThRn484IzOvuRVDcA2ZkIKZC3jB84lLbWk6M_fxpyhlPzzAQmE4D6uAkoGyPXHNF_DhIJ8LQRxnrkRueFYtsKnVYoDk8P6Yi4Iks3VEQ1HgoO5kh4yPciePGBdll92RZphMtK4IZryS9WHrnxZH1C9vxg-pFhKc6xjxvklhi5w5zaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e097e163aa.mp4?token=p5Ta-D6eWxR2FLo2ttqU-jMU6Zvb07wIZyAYSg8vgxSEbll_e5id9Aoccs5OimgD9A90eOShIDwJGF3ptAE3XQQbcOpHB7ntJK2JjM8Xacar50nKzHnQo_k8Bld8MrM8lchcRZtjTDZ32QRtWBgweVHN5iiktq3rN6MGe5I1ThRn484IzOvuRVDcA2ZkIKZC3jB84lLbWk6M_fxpyhlPzzAQmE4D6uAkoGyPXHNF_DhIJ8LQRxnrkRueFYtsKnVYoDk8P6Yi4Iks3VEQ1HgoO5kh4yPciePGBdll92RZphMtK4IZryS9WHrnxZH1C9vxg-pFhKc6xjxvklhi5w5zaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سردار حسن زاده فرمانده سپاه تهران:
فردا ساعت 4 صبح رده های سپاه،
یگان های بسیج و گردان های جانفدا از میدان انقلاب تا میدان امام حسین چینش میشوند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71796" target="_blank">📅 23:55 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71795">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">بی‌بی نتانیاهو درباره ایران:
پیش از هر چیز، باید رژیم ایران را سرنگون کنیم.
این مأموریت من و مأموریت اصلی ماست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/71795" target="_blank">📅 23:32 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71794">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ساعت ۲۲:۴۰ پنجشنبه؛ ملوان‌ها در اطراف جزیره لارَک، از چندین انفجار در نزدیک کشتی خود خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71794" target="_blank">📅 23:28 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71793">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5UeQurSqp-NSlRJO7z3G5-01ZVYgn_CygteHnkYkfI0rzIxYvpQ6-14sBUnDeGVq-iZPeay9__48FopByUo1eBZLk_uKYUoMrZ6KAzPSHhS6BRc0ZVWZa-q9AmHwxZmZxMFGhj9Q9GGOAAYjxOajE2O4McVS9XRLpoDb0wMAvxfn89qqj4bc9NT9_ZZIo4CRL8fE4rNjS6eLHwqmOAVVdgt8GWP_dgK6DMiyUzBmdjjeuBoCluxsbJ4OoidOlihuviiyg3qnJApe13UI49PKF-SSGL-Awrp6jnRUb_Rq7kg3DXWImhVlqeOfXBx5QYhDH7U99_Kqc8YbaHulvd7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا (UKMTO) از وقوع یک «حادثه امنیتی» در فاصله ۱۶ مایل دریایی شمال شرقی «خصب» عمان خبر داد که شامل حمله به یک شناور در تنگه هرمز بوده است.
هیچ‌گونه خسارتی به شناور یا جراحتی میان خدمه گزارش نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71793" target="_blank">📅 23:22 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71792">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TpdusbPNcC6X1UeiplOF06c5RPdCcUw6tuBWpSwQGxepU8ORi9QxvXbn_jCtisfG5aspUtO56I2Of_0vb8xhxgwBnqs_S5Ysnx08ZJWsj5P_LEQwekYyIciZkFgGSOir4W6IP-Qrs7ZjvZf3QrRetUdMUoGXj0Tu_NPxGyy-McuM6wcWMFgY1vdJ_miEQ4ntO34wrbVX628DZwPu-X7a7SzGpIZtro-iENVQxQM5_flhkovQkVijFJmgR8oNYEbwNSQTuUF_kVgN2jKplEI0wKnpWHIS8qCgnxQJ_17_pRoDDOkIWFKZVln-tfO4AjvEeG6GYFL1DKVpn2Rn0y1SKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری آمریکا «بیت‌بانک» (BitBank) — یک شرکت فعال در حوزه دارایی‌های دیجیتال در ایران که تحت کنترل بابک زنجانی، سرمایه‌دارِ پیش‌تر تحریم‌شده، قرار دارد — را به اتهام تسهیل دور زدن تحریم‌ها و انجام فعالیت‌های مالی غیرقانونی، تحریم کرد.
این اقدامات همچنین شرکت «تجارت الکترونیک پیشتاز سیمرغ» (توسعه‌دهنده بیت‌بانک) و سه تن از همکاران بابک زنجانی — شامل حسین‌علی ذاکر حسین، محمدمهدی ذاکر حسین و سید عادل حیدری — را هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/71792" target="_blank">📅 22:59 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71790">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nsH8khqWoH6UO_MeEPcEQHvsuVgB2tg64nQ1m2Lwx0yN7672wCEEadg77vFeROT1n7Dt8I6tin3Xyn79QxbTipc_wv1AQ1d8QW7CqNON5V-CF5HAQaVpvUUGxjSkTUoiTVB3kztNp-dfDLp4IdGHMbOIribtFNlkNRAqpG291-v_5emgZ1Pg_eNLdfUuTwKyJIL7NslqOL-0fof4NVF99L-uC5nioX7S49HUA-xIbBQ4Ir8nE7WH__HNe2F7pRoi905xirActx1Tnvuu69CVGGiIfwv1JeYyBrOufxBsB_5JsA5j-vHx_GGIxNXZWqDxBVvS4Rsquc89wntPqaiLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LwkFyP_EF_ZBuXSEFnLvLZEnSMC0PR3LCMkwjWi1c_5etvHhBv7IC-ca9ihuZsEdSCKwixBxFU6ZSSdZDx05KtEQz_wvuQPU1mgC-8T_bVyQWbJGYRq057bDF86m5vX1_PKhac8yuHXwKQYavIP9GSMPv_I2kM6Ior1C2d6N9Ejps6vw8n1L_m73ZdLKOgt49jqssO3C0dtKxT0PkiyFNECX9HYDqDUdGnlTyFlDIr8xWbg4xJZmyhPf7xlB5bffSeFml5XoWw3x0QmgGqI8ib5aYkoSSuJrm7zT8J-mX24F_W9VDD9T1GOuWi8QkfWKoBfzT4sjRf4BJVf1OIFBIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ایران به سرعت در حال بازسازی تأسیسات طالقان ۲ در مجتمع نظامی پارچین است - یک سایت سابق برنامه سلاح‌های هسته‌ای در ۳۰ کیلومتری جنوب شرقی تهران.
ایران یک برزنت بزرگ روی این سایت کشیده است تا کار را از ماهواره‌ها پنهان کند، و در زیر آن ساخت و سازهای سنگینی مانند کامیون‌های کمپرسی، بولدوزرها، پمپ‌های بتنی، جرثقیل‌ها و دیوارهای تقویت انفجاری جدید قرار دارد.
این سومین چرخه بازسازی است. اسرائیل در اکتبر ۲۰۲۴ به ساختمان اصلی حمله کرد.
ایران آن را با یک مخزن مهار انفجاری جدید که در زیر یک تابوت بتنی دفن شده بود، بازسازی کرد.
اسرائیل در مارس ۲۰۲۶ دوباره با بمب‌های سنگرشکن به آن حمله کرد و سه سوراخ در محفظه ایجاد کرد و ساختار داخلی را تخریب کرد.
ایران تعمیرات را تا ژوئن ۲۰۲۶ آغاز کرد و اکنون به طور پنهانی در حال سرعت بخشیدن به آن است.
ISIS (موسسه علوم و امنیت بین‌المللی) بازسازی مکرر یک سایت آزمایش انفجاری قوی سابق برنامه سلاح‌های هسته‌ای AMAD را "عمیقا نگران‌کننده" می‌نامد
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71790" target="_blank">📅 22:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71787">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xte5SIKZJXr4qK47E81S4U4ffjUNSvA8mbQ-VBS2Ad3U9Dd2COrjxfykOAFIqR_7u0-R7u7JEsJpWMSl3Ek7zix1Fv5XSqAs8rn3ipn9cW8zS18wMWIOxm6R90moU3mk3ffNjIendO2BSyAW574zi9rFvTc_-U_eMBR-daXkRXWt7YChS7htTVojBp1j1-dSabgdduqhMjExpX30VJunW6-RIhojybBxL2s3vgpDs89JwfFakMCS3Abe3TrNuJtOleBTCx8q2y6YiJKg85V_LyD8XW_FQg-gBZ-HYBJh5oELncGdUbPYF8M1NZ5gAWTLduG8ynjjEovHEAxIDQ9WZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nLSUg4OcKFT9Fo6ed1B-g3Q_6v-DwqvXxVJrI00U9GCz32ZnwfLXAagKSgxjPJSdN-fv3TspyKieW3O41_ncMKtyQEAn42oMujFhE01T5RdHePCD7rWevvFpS9PeMraJQaXknnClqp9jwlD8Ja8294guwxd8jP0l3kgYXDH1XmL23j8WTbrFPqT_B-GphS0CmsImw-Mfh9gvHvscgfkHPRdnYqCHNajOYQq12jwMb209HQnJXbsswJN9BaDei0325nDr_7Xfrh_112BkyzNuKXXQAb9P-rWHCsFke1F_B96h0i51gKGvE9HmUlXiIB0V5ijPf8zuw5RBQh4YdkbNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDAD-jnpM3_G9qRXXRDAiCelJw0XniZ4J3qK0l3rldZenH-5HlyY7dc9mTkICUZxi1vBxbPVAc_htc1gKNFUsTpKbJmo0czdHx_hSsin3b1HByCAahF8WWWUAiQ_5udxlT7-U58H1JEZvQBCwPwsjPXfifNeC_9xCyuGfuR3lqAj6vYsC4YBLUUsWwXtfypWBdOzIvR0Ryk0deqTEd1QW_chR5KyPBnIGFXzCR9JnUP_Vlgd5r58vNI7gr1w5hMXwISRaieB2DMlyKHW19SxdGWv6cM3QjE-V8LxmQpZySeo1xKV62IiGp3tROYBb0ChgZ0dUK5ty0bN_0Ke-9cjag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عکس های وایرال شده از علی ضیا و زیدی در فلورانس ایتالیا!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71787" target="_blank">📅 22:15 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71786">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=OsjyRKKB_vXUlX7331-M7DNq8o2ch4CZvjGaGLZcQHjdyC5yJ6ecrtaWiqtrhF2YL1gizZNwOeq0s7MPP6x07qj7NWtmbVqY2bcB8SJ6LjWVyKjLY7nUNIaOibdY97JwBQirdsFIZjNkml0VHEdF2X6nOT2n7AN6mrtjdFRqN7h5k7ONPT-zlpvVUvFmuZu9v-98B3LOv1hs69IC3Zj7nPc55hp6KI8gdYzQ5aJR1a_awyzXBl6NeDkE52KX9dBIDxmZv2hZSjVucUBPQOr__-nPYFm8E-YfP04hO2X4j2lh9tDeci-sMApjNY9MTwuvBe_5oRU6RrOTwPwHxGYAIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e44acb8ce.mp4?token=OsjyRKKB_vXUlX7331-M7DNq8o2ch4CZvjGaGLZcQHjdyC5yJ6ecrtaWiqtrhF2YL1gizZNwOeq0s7MPP6x07qj7NWtmbVqY2bcB8SJ6LjWVyKjLY7nUNIaOibdY97JwBQirdsFIZjNkml0VHEdF2X6nOT2n7AN6mrtjdFRqN7h5k7ONPT-zlpvVUvFmuZu9v-98B3LOv1hs69IC3Zj7nPc55hp6KI8gdYzQ5aJR1a_awyzXBl6NeDkE52KX9dBIDxmZv2hZSjVucUBPQOr__-nPYFm8E-YfP04hO2X4j2lh9tDeci-sMApjNY9MTwuvBe_5oRU6RrOTwPwHxGYAIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واجير الونگکورن، پادشاه تایلند به همراه ملکه این کشور در جریان سفر رسمی به هانوی، پایتخت ویتنام شخصاً خلبانی هواپیمای اختصاصی خود را بر عهده گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71786" target="_blank">📅 21:34 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71785">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#فووووری؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.  «تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/71785" target="_blank">📅 20:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71784">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqK7tuxGromfBOXqZMcGrz6En11mtb3YEgq6qNnic35jrBc4sACPwgxhbZ6bPJqaLiEUGeRu3LeweYl6yPmXxbgOzvS6fvYUyAs1gZX3gPhux0NwP4RwmBzxyVDUFyjM0VZs15a6rstElVa2_8I_gflKoT1ePF6aCulPO60vhvDeIrGdW2fh4V9VqdHrVTU-u3SsYMZDnBaojHxbp2Iyfbd1TY6sDerUbisttj9OCp92zMw6xfQL2VTvM2QIrCKNN5UXaKU4FhFqzQyp8wbwA4zo5FmQW2F1h-B6_rfrUbGlvfMhnKD01K24SAlDkxcI74--PiD8KWGvsDCQXWpF2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فووووری
؛ترامپ به وب‌سایت «اکسیوس» گفت که در آستانه اتخاذ تصمیمی حیاتی است: اینکه آیا عملیات نظامی گسترده‌ای را علیه ایران از سر بگیرد یا مسیری دیگر را برای پایان دادن به این مناقشه در پیش گیرد.
«تصمیم بزرگی در پیش دارم. آیا می‌خواهم وارد عمل شوم و آن‌ها [رژیم ایران] را نابود کنم یا نه؟ تصمیم بزرگی است. هر احتمالی از جانب من وجود دارد.»
ترامپ اظهار داشت که قصد دارد از فرصت دیدار با رهبران شش کشور حوزه خلیج فارس در حاشیه مجمع عمومی سازمان ملل، برای گفتگو درباره گام‌های بعدی استفاده کند.
«می‌خواهم بدانم موضع آن‌ها چیست و در چه وضعیتی قرار دارند. ما همواره حامی و محافظ آن‌ها بوده‌ایم.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71784" target="_blank">📅 20:45 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71783">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=vRYpDejv3MVhlcDNKqqAv0TWdBozaAAst82peXKkBJsoYPCjoFkpFU1hBiWd05Q_LZoXFm8No2cQDqnSDsnVDS5OQKLNTXXI1FRAjL3RDRiThAl5zjoyc1Kd-I9jZUYyCPktSN4xt9-cCwEXOMIJEZUZRg-HkuYQEJ15Am_8Xjws8IYoDra7svhoSPuIMDgNq1QtKY5nd9sSjYl8clPxYSwsGHjBQpLRrFvpIyvUkqYoATSXel8ILvYm22qLA8zHVuSI6ffkDPjMwcz080efTY1vCEwZQKulPg-jBHPMZU4dCJvoXlq6oLddKn0l3kDrZEpZ_nvFRZRUN2c3OHXy0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7b5d03539b.mp4?token=vRYpDejv3MVhlcDNKqqAv0TWdBozaAAst82peXKkBJsoYPCjoFkpFU1hBiWd05Q_LZoXFm8No2cQDqnSDsnVDS5OQKLNTXXI1FRAjL3RDRiThAl5zjoyc1Kd-I9jZUYyCPktSN4xt9-cCwEXOMIJEZUZRg-HkuYQEJ15Am_8Xjws8IYoDra7svhoSPuIMDgNq1QtKY5nd9sSjYl8clPxYSwsGHjBQpLRrFvpIyvUkqYoATSXel8ILvYm22qLA8zHVuSI6ffkDPjMwcz080efTY1vCEwZQKulPg-jBHPMZU4dCJvoXlq6oLddKn0l3kDrZEpZ_nvFRZRUN2c3OHXy0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیروز در شهر ری جانفداها با جمعیتی میلیونی رزمایش برگزار کردن تا آمادگیشونو به رخ آمریکا و اسرائیل بکشن!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71783" target="_blank">📅 20:14 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71782">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sieQhmgDIHLEWKzulecw7d_mPJE27eNuPCu0T89k4r1hjL1rXoSNsoniuN1ke2jsnaj-nWfw6p0_X-4eTzijsU9uBppUvKVrkKXTdPCTQeZGEMl3lqsvIeoUh3DjcWa1wZu4SgnIF8jkfVBinh0EEt_Dl8rk-pq1fo8F9wGtrwulu57wN2eXabJQz6zcD6YvooJk72jf8y_X0F1n4QTxtV7chfQS8FrQOjQpLQgc4BVhFNVpZS_4lf7BWJKjoltvUjROXYh_H5-ZIcTNdLzFgLuQZSOy5hac-vhdEF9M5JroS2vLQXuVwoveBqOf8VEeRmyaaY6WJIEb8tacic04ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز، چین در پی درخواست عربستان سعودی از پکن — که پس از پیشروی‌های موفقیت‌آمیز حوثی‌ها (انصارالله) در امتداد سواحل دریای سرخ و پیرامون باب‌المندب صورت گرفت — به‌طور خصوصی از ایران خواسته است تا به مهار حوثی‌های یمن کمک کند.
پکن به‌طور علنی خواستار خویشتنداری، گفتگو و ایمنی کشتیرانی شده، اما در گفتگوهای خصوصی با تهران فراتر از این مواضع عمل کرده است. ایران در پاسخ اعلام کرده که ثبات منطقه به پایان جنگ آمریکا و اسرائیل علیه ایران بستگی دارد و همچنان مشخص نیست که آیا تهران به درخواست چین عمل خواهد کرد یا خیر.
چین هیچ‌گونه تهدیدی مبنی بر اعمال فشار اقتصادی مطرح نکرده است؛ با این حال، روابط این کشور با ایران از وزن اقتصادی و راهبردی قابل‌توجهی برخوردار است. در همین راستا، یک دیپلمات غربی اظهار داشته است: «تهران و پکن به یکدیگر نیاز دارند. چین عاملی است که تهران نمی‌تواند آن را نادیده بگیرد و پکن نیز خواهان بازگشایی تنگه هرمز و تأمین امنیت کشتیرانی در دریای سرخ است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71782" target="_blank">📅 19:35 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71781">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=DMAX3chntWGWnurHjB1LNGdER5LfSOgQYG12X7vbPy8rol3BnEON0roUZFd-EQyeGxgAPncif66fsPopu7tQlu3RU-sT8I28wDmKzcAWQANJguaRUoOVLGPzOWndJ1maP4ClonALpuygFlKP_jG-ZzKkR3t1pfTtVmH1qTWYA7U6IKS6BCL2WGyOPtXRfDY_mPq3OjOxpKGAOInjvfcNjoancwM7TPuW31zfV6h7Q6RPcYZlyMSX4SPBjrZLB2YE5q8fnBckFizD13A-GWWJedXt4kgk_wIm4rT_36enjmybWBEW9RbeteYV6ob3K1Eb2UuaRP4pdJTQgzpkD_U4VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7347b9d41.mp4?token=DMAX3chntWGWnurHjB1LNGdER5LfSOgQYG12X7vbPy8rol3BnEON0roUZFd-EQyeGxgAPncif66fsPopu7tQlu3RU-sT8I28wDmKzcAWQANJguaRUoOVLGPzOWndJ1maP4ClonALpuygFlKP_jG-ZzKkR3t1pfTtVmH1qTWYA7U6IKS6BCL2WGyOPtXRfDY_mPq3OjOxpKGAOInjvfcNjoancwM7TPuW31zfV6h7Q6RPcYZlyMSX4SPBjrZLB2YE5q8fnBckFizD13A-GWWJedXt4kgk_wIm4rT_36enjmybWBEW9RbeteYV6ob3K1Eb2UuaRP4pdJTQgzpkD_U4VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عارف:شرمنده مردم عزیزمون هستیم
واقعا از مردم عذرخواهی می‌کنیم، شرمنده‌ایم که امروز دخل و خرج مردم با هم نمی‌خواند
نمیدانیم چه کنیم، نمیشود تورم ۲۰ درصدی داشت و رشد حقوق ۵ درصدی!
واقعا شرایط زندگی سخت شده و مردم رو درک میکنیم
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/71781" target="_blank">📅 19:01 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71780">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=fytxBjJ7GWC5dEB1Wwt706zuRXrCIzTm23og6c12FbSmoV9rEgMN3J5lVqz-9jRFZ01pPYrgI2-MWH3eDg7pIKYWTWJbvXPtWMvZoCLoOI8Truv3F7Gf2hNgQou3gheT0bw18Vo6-BmZF26YMs_2octtxo3xzccbWi2CeOY_U0TsksGQKP3v6fk9SOOgrUV0oxIq12z2AwxEP6V5-UuwvchB_b8NcyTIz4hpl1PLR7lDInFqHNy0QYi-AYee2VGQtAsubMc9n3Ry3l8gLSu4MqIiwyVOAF_-qxQyl7nYYSQ8dj1i4uGTWqKqUfDizOwL9-M2OrVy9HlVIY2nAB5kkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fff9dea68.mp4?token=fytxBjJ7GWC5dEB1Wwt706zuRXrCIzTm23og6c12FbSmoV9rEgMN3J5lVqz-9jRFZ01pPYrgI2-MWH3eDg7pIKYWTWJbvXPtWMvZoCLoOI8Truv3F7Gf2hNgQou3gheT0bw18Vo6-BmZF26YMs_2octtxo3xzccbWi2CeOY_U0TsksGQKP3v6fk9SOOgrUV0oxIq12z2AwxEP6V5-UuwvchB_b8NcyTIz4hpl1PLR7lDInFqHNy0QYi-AYee2VGQtAsubMc9n3Ry3l8gLSu4MqIiwyVOAF_-qxQyl7nYYSQ8dj1i4uGTWqKqUfDizOwL9-M2OrVy9HlVIY2nAB5kkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طلافروشی از اون مشاغله که نکات دارک زیاد داره
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71780" target="_blank">📅 18:15 · 26 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
