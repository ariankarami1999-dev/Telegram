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
<img src="https://cdn4.telesco.pe/file/HGOOaRlDJPCY6p5k643vQKlilVrsrjoLxO2fN_0RLKOsP5pD_2mbYMVZe35mrj4aF-SEPYZUV2-rZZvhsoHd19UD6q8UIEYk7-hs8UGM9K0kKi126v1P8GcvsOMT2lnlew21SheMdT8U9uEc-3_HImNUD2np3LU7cbHyAkKLlvRghVm5vK-4-BqdGl93f3NjGYkqsMCEcASFxakNdH1DeVCXpzu46qK0EBE8g00CC9a_GuUrqyBkTpjXaBSDlRu3Fo24Wc4VqsAETFaW9YwKigF0_WTKd40dqEpm2Dv7p71jIKFqlXWtnx22i6UyR5pQtBuG7gOt9XNMqApTMKbc0w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 117K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 17:05:27</div>
<hr>

<div class="tg-post" id="msg-70715">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=IetUKvSxhICU4qrZc5DoSXQI3DF3fQoqiy3_hBUGjrNnoN0zq-4eqnkJLPXbwZ5AbzSKaFWn5zZi767FzsfsXoTL6_EY92yUiRMpaHkUMLC7KpxVF2fN4gA2yuFWlIpl0SOuZo3YieHvhTu9fEb4ODRAHZjfzA4PxX3cHqHMe-Ribl48B_Ev97b15l1btYuGKkm33rlUzEgCuE1lphgIRxnXBtABGhtKXUNBcPKWijANaWgD4F-UfXl-P0FT2L2t6XOG16nV0E6YPiNBJqAK6zia3OHE7AoO5T9oCQL1xVw-sYAQ3gVJiWyCKQW0VvX3ilP9OcdwDZFejsm993TIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65902c1b90.mp4?token=IetUKvSxhICU4qrZc5DoSXQI3DF3fQoqiy3_hBUGjrNnoN0zq-4eqnkJLPXbwZ5AbzSKaFWn5zZi767FzsfsXoTL6_EY92yUiRMpaHkUMLC7KpxVF2fN4gA2yuFWlIpl0SOuZo3YieHvhTu9fEb4ODRAHZjfzA4PxX3cHqHMe-Ribl48B_Ev97b15l1btYuGKkm33rlUzEgCuE1lphgIRxnXBtABGhtKXUNBcPKWijANaWgD4F-UfXl-P0FT2L2t6XOG16nV0E6YPiNBJqAK6zia3OHE7AoO5T9oCQL1xVw-sYAQ3gVJiWyCKQW0VvX3ilP9OcdwDZFejsm993TIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو وایرال شده از پسری که ماکت آیفون رو میگیره دستش و زیر ۵ دقیقه ازش میزنن!
@News_Hut</div>
<div class="tg-footer">👁️ 1.08K · <a href="https://t.me/news_hut/70715" target="_blank">📅 17:00 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70714">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=NKSnPLojMLwcameanZdBf2kCJuc0ZVFEtWkccUFFnBYFc8ZsMMRvP_6PviItSu8Fi47uahUOHplTegKaQw_LnBT7B8kEhnVaVxxGSMPkYlrRdHP_hlA4lTlccI1oKJAFDXLAdeK9EaySfxc1aViUeBhY6nTOv76g4Z56LFrBOVMMt2bFexOmJ069kJEWHHGmhpI5evyRQE02V6naog4LjDJU3cKsOgrRzCGlqHqr2XoTvdC2X4BBFJh0NDV9DO1jWytkqzBK3P5hGK-VMzABj2eD91dEyjo9ZuOsSLanp7JYcNrrVSZP94CuFlgekOUPN1d3k77aaTOnOVCtl5-f0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50851d2a93.mp4?token=NKSnPLojMLwcameanZdBf2kCJuc0ZVFEtWkccUFFnBYFc8ZsMMRvP_6PviItSu8Fi47uahUOHplTegKaQw_LnBT7B8kEhnVaVxxGSMPkYlrRdHP_hlA4lTlccI1oKJAFDXLAdeK9EaySfxc1aViUeBhY6nTOv76g4Z56LFrBOVMMt2bFexOmJ069kJEWHHGmhpI5evyRQE02V6naog4LjDJU3cKsOgrRzCGlqHqr2XoTvdC2X4BBFJh0NDV9DO1jWytkqzBK3P5hGK-VMzABj2eD91dEyjo9ZuOsSLanp7JYcNrrVSZP94CuFlgekOUPN1d3k77aaTOnOVCtl5-f0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر با زنش دعواش شده و رفته جدا خوابیده، و اما آخر شب برگشت تو اتاق پیش زنش و این شاهکار رو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/news_hut/70714" target="_blank">📅 16:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70713">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1E7ZhDcc3tixenpmtAKY6iAX_sxxj0uxnbQ0CUvoLeuHqzWDO2YfmaR273c826admjLwxnvPWoz6xeItu4A6CK3_AWQNUTNgdME5Ei-z7FJQXVeZsRDDNycVCiy3BWJAmCXVqALumsDLWnVyRltqOXI52fN5et5cGeEgbrA526iktaQG5rB2NPMZmDT8PoB0FZt6knReGCud53XElneDoPJ7qmi-smhqZ55U7GWk3jgeWFlg51w4PUSjGZVvfBI2oQmmMX9GLqOpno5K_bJV9k5h6gdG9NygUycBlv65fYGCYvXmvPoR6aUnDBKwWV-yMpO0lDJVMFbq76j9wOwdJd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c52147d4b.mp4?token=YmX74AC2Hlq9IUMd3ntxaeJRQMyoyzsV0iSeGvNLw21JTcnT3_Pt95Zq1yWTr8nxX1uhrIDP-rOp1VJCqy2yJlI2tpjywQywIfD3IQH_IsnCMTAX7npC9fZGMOKiw5KakqdSqtgn02rbXTcZy5TrGJKNEbJhfi_HqV4u-ifEMF_1fRifAKtWeUkkmBj-THDRZhDdWmKcA-1QtiiJduAZ8KzfVvBw2RW1DZ5CKM0KcseMjrkazGn4XF_4bs8r02AvYCOIabJZq2RnC8TbNeOdLP0ylX09IgC1wxOujQgMfFXkiUQe3vajEzKy5N0LYhrvgfvPWW3bi9xVtJIfg53O1E7ZhDcc3tixenpmtAKY6iAX_sxxj0uxnbQ0CUvoLeuHqzWDO2YfmaR273c826admjLwxnvPWoz6xeItu4A6CK3_AWQNUTNgdME5Ei-z7FJQXVeZsRDDNycVCiy3BWJAmCXVqALumsDLWnVyRltqOXI52fN5et5cGeEgbrA526iktaQG5rB2NPMZmDT8PoB0FZt6knReGCud53XElneDoPJ7qmi-smhqZ55U7GWk3jgeWFlg51w4PUSjGZVvfBI2oQmmMX9GLqOpno5K_bJV9k5h6gdG9NygUycBlv65fYGCYvXmvPoR6aUnDBKwWV-yMpO0lDJVMFbq76j9wOwdJd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
سخنان ویرال شده از یک آخوند اردبیلی که درحال وایرال شدنه؛
تو دنیایی که جوان نمیتونه ازدواج بکنه ولی میگن عیبی نداره تلاش می‌کنیم درست بشه
تا متخصص های شما وضعیت رو کنترل کنن جوان مملکت از گرونی استرس اضطراب سکته میکنه میمیره
جوان ۲۵ ساله شب میخوابه صبح بیدار نمیشه این خیلی حرفه
میگن بچه بیارین آخه بابا پوشاک شده ۷۰۰ هزار تومن شیر خشک شده ۳۰۰ هزار تومن لعنت به قبرتون بباره از کجا بیاره آخه بیچاره
میگن آخوند میره میخره بابا بیا منم عمامه رو گذاشتم زمین
اینا همش شده شعار به ولله نیازی به مذاکره و کشور های دیگه هم نداریم مسئولین ما بی عرضه ان
ایران‌خودرو شده مافیا برا خودش چرا جلوشو نمیتونین بگیرین؟؟ ولی واس یه تار مو میکشین واس یه قسط عقب افتاده میندازین زندان
جلو اینایی که زیر سایه نظام گردن کلفت کردن رو بگیرید ننگ بر شما و حیف این ملت که دست شماس
@News_Hut</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/news_hut/70713" target="_blank">📅 16:02 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70712">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=t3F0Pv1hfNZMDRH_zhAHWx_CWt6n5YT7dhPtdA_59B281DuO4f27vH8Tx0h7ORrnj4S21f-B_807zbf--b76p6pVcgUSsmyf31HEoth5VciO4O9VF970vOvgzX2XicGFNwhn_MW6JLqupzbXP9CqXmy2K4Am3_rdMO3KVtr4hjORORWXjkClVB8BWPf4TQhH5TZmv6zRh2a-jbTfeekLqlVYMHKCCEbnC_cAv5I1KkJ0UsDhkKMVrC2VgkLCHzWm8yibDscyTJHDKEBLMA2WzHx4LcAd7Q9WkbFko7nDgzUtOQ8yOI26cPpJAFsNWwPyeiaAn3Ik1hCnoE6WXUe58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80bc2fd38e.mp4?token=t3F0Pv1hfNZMDRH_zhAHWx_CWt6n5YT7dhPtdA_59B281DuO4f27vH8Tx0h7ORrnj4S21f-B_807zbf--b76p6pVcgUSsmyf31HEoth5VciO4O9VF970vOvgzX2XicGFNwhn_MW6JLqupzbXP9CqXmy2K4Am3_rdMO3KVtr4hjORORWXjkClVB8BWPf4TQhH5TZmv6zRh2a-jbTfeekLqlVYMHKCCEbnC_cAv5I1KkJ0UsDhkKMVrC2VgkLCHzWm8yibDscyTJHDKEBLMA2WzHx4LcAd7Q9WkbFko7nDgzUtOQ8yOI26cPpJAFsNWwPyeiaAn3Ik1hCnoE6WXUe58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سخنگوی دولت:‌ مردم منتظر بهتر شدن وضع اقتصاد در سال آینده نباشند
@News_Hut</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/news_hut/70712" target="_blank">📅 15:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70711">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">⏺
🇺🇸
پروفسور جان مرشایمر استاد علوم سیاسی دانشگاه شیکاگو درباره اینکه چگونه تحریم‌های آمریکا می‌تواند منجر به اقدام تلافی‌جویانه ایران شود:
در سال ۱۹۴۱، ما یک محاصره نفتی شدید علیه ژاپن اعمال کردیم و دارایی‌های این کشور را مسدود ساختیم. ژاپنی‌ها در وضعیتی بسیار وخیم و درمانده قرار گرفته بودند.
آن‌ها تصور می‌کردند که ما با آن محاصره اقتصادی، بقایشان را تهدید می‌کنیم؛ و در نهایت، دست به حمله علیه ما در «پرل هاربر» زدند.
به گمان من، شما نخواهید توانست ایرانی‌ها را به زانو درآورید.
اما اگر بقای آن‌ها را تهدید کنید، آن‌ها دست روی دست نمی‌گذارند تا صرفاً محو یا تسلیم شوند؛ بلکه واکنش متقابل و سختی نشان خواهند داد.
@News_Hut</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/news_hut/70711" target="_blank">📅 15:06 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70710">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
📚
#فوری
؛نتایج امتحانات نهایی تیر و مردادماه پایه های یازدهم و دوازدهم در سامانه بینا منتشر شد.
🔴
آموزش دریافت کارنامه :
۱. ابتدا از طریق پنل سنجش وارد بخش ثبت نام در آزمون شوید
۲. ورود به سایت آموزش و پرورش
۳. مشاهده سابقه تحصیلی و ثبت نام ایجاد و ترمیم سوابق تحصیلی
۴. ثبت نام ایجاد و ترمیم سوابق تحصیلی
۵. بعد از ورود به این بخش از سایت وارد لینک سایت بینا شوید.
@News_Hut</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/news_hut/70710" target="_blank">📅 14:37 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70709">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=r45d25BQpTa_qfAvFHTmOysRmak3CsMPO7ESJ2Ojeyyip-XWExSKf-p7nPiqj1XR-Jx-1N2S_aCWXEc81gwly6-MYE9qCOs6fUvAYgjKOqfxdpCay1LE1PfGRx4X4FjUQ8dIpvvM2sIISLY3EVD_xVK8WUcu6jYiJT6ustEQ45lmObKV4pEJD8SyvsHDAGmr5uu9Qj8tE2qcPer_Nb-Lu1Bk5qSls0vjJ9MO7JXL5z1k6jtGWWhyOs_nO02mR0xju6GZItPcWHeVIVjuCjAGBOArBiMXoDWGHDEdyfkda2mejjfy_NsCxsR957oAk3YgHTj1j9nHRwcTN3oVJfewTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc088cfcb6.mp4?token=r45d25BQpTa_qfAvFHTmOysRmak3CsMPO7ESJ2Ojeyyip-XWExSKf-p7nPiqj1XR-Jx-1N2S_aCWXEc81gwly6-MYE9qCOs6fUvAYgjKOqfxdpCay1LE1PfGRx4X4FjUQ8dIpvvM2sIISLY3EVD_xVK8WUcu6jYiJT6ustEQ45lmObKV4pEJD8SyvsHDAGmr5uu9Qj8tE2qcPer_Nb-Lu1Bk5qSls0vjJ9MO7JXL5z1k6jtGWWhyOs_nO02mR0xju6GZItPcWHeVIVjuCjAGBOArBiMXoDWGHDEdyfkda2mejjfy_NsCxsR957oAk3YgHTj1j9nHRwcTN3oVJfewTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
ویدیویی که بین طرفداران حکومت در حال وایرال شدنه و دارن میگن به زودی این صحنه از صداوسیما پخش می‌شه؛
@News_Hut</div>
<div class="tg-footer">👁️ 9.89K · <a href="https://t.me/news_hut/70709" target="_blank">📅 14:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70708">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🇹🇷
شرکت‌ترکیه‌ای«روکت‌سان» (ROKETSAN) با موفقیت موشک کروز جدید خود، «چاکیر» (ÇAKIR)، را از یک پرتابگر زمینی آزمایش کرد.
این موشک با بهره‌گیری از جستجوگر فروسرخ تصویریِ نسل جدید، اهداف زمینی و دریایی را با دقت کامل (اصابت مستقیم) هدف قرار داد.
این آزمایش‌ها همچنین قابلیت افزایش برد موشک را به واسطه سیستم سوخت جدید، تأیید کردند.
موشک چاکیر که پیش‌تر از سکوهای پهپادی پرتاب شده بود، اکنون توانایی شلیک از خودروهای زمینی را نیز به اثبات رسانده و قابلیت یکپارچه‌سازی با پلتفرم‌های گوناگون را نشان داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/news_hut/70708" target="_blank">📅 14:30 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70707">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/70707" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/news_hut/70707" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70706">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KK9nc7DBqWQcKQI8BaUNnIAr8Tj0fblGDn1Pz-GjlQfSJbeh9O9Z--MXYZJ-uIs2GHfrd_jB5M_3U5qVQsqiN21bH71Er75MBty_rFvNjEwak-m016jXi84JmWv3lXC6-ZsuA8gvi6Gs1TgdB4W1nAOMala6qwKVERqIPLyYb0RXolzGcHqxurUpuZIBI-DVZ-x4PqM7nWEn0cd_tn05tG_2OK-nBFwnfepIN5za-gUWDbmkK1dSG17QIo7TJMIO25QRhZ8OG4I6NFFDj_GVAr86oS99Sa2LhBott1tiMW2Es4Lau1se5z98ILEw4UKB6891oPEQMy_fKLIBhWSpfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد جذاب فوتبال ایران را در
TrexBet
پیش بینی کنید!
🦖
استقلال
Vs
فولاد
🦖
جمعه | ساعت ۲۱:۰۰
🦖
ورزشگاه شهدای فولاد خوزستان
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
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/news_hut/70706" target="_blank">📅 14:29 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70705">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=t_IlkXV-hU3TDONRcbVed-PbWZbAR_Dy0O2d0DzpkI-loxheABJeqIK0ebdNrULGEkV4n9qfgewPT1qZaHA6N9xWB6MrLU_3KsU-Xg2ayL5blxP65C8mmvPG9_YBZIpcvcQySSAkFgSLrqT7BXdDycrVKMjyIgXQzc-AGQQ_YEi-nFoy75Uxb0TQRmmSNPayR45tGE5-WBTLfTrcTaSQluNWNSSxp00PeqR59_GKw2NrRLZA0nHaZ07E0eJLzU0X45PuMQaUnoPdZlwoaoMPLzON6ao970cgk2YtIYwWQGMxXV-e8Gc1fmIAqUp7IoTZrtFsPriHGyktm7S3qtWZ_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e90df5a6e.mp4?token=t_IlkXV-hU3TDONRcbVed-PbWZbAR_Dy0O2d0DzpkI-loxheABJeqIK0ebdNrULGEkV4n9qfgewPT1qZaHA6N9xWB6MrLU_3KsU-Xg2ayL5blxP65C8mmvPG9_YBZIpcvcQySSAkFgSLrqT7BXdDycrVKMjyIgXQzc-AGQQ_YEi-nFoy75Uxb0TQRmmSNPayR45tGE5-WBTLfTrcTaSQluNWNSSxp00PeqR59_GKw2NrRLZA0nHaZ07E0eJLzU0X45PuMQaUnoPdZlwoaoMPLzON6ao970cgk2YtIYwWQGMxXV-e8Gc1fmIAqUp7IoTZrtFsPriHGyktm7S3qtWZ_Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیزر سریال مرد هزار چهره هم اومد و مسعود شصتچی یه جایی عضو تیم مذاکره کننده هم هست:
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/70705" target="_blank">📅 13:54 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70703">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0qxKDzS_OnbJ7HtA1gQZudIkdlH3PmBthMRn_J4Htc_-PHnsFakVbR7UVqN5cDTl2biPD1WZ1QYrJdv6D3Mn0yrVZaJo2RqrN1GEs6rBzZMIbm2CG46CckILM6jb_Z-HzRh8wlreWfsEyqo1xZmlm4tIJ8td8lMQ9h3rqZfwXq5FLXHTODs0jR3EsAehHwdi2s8RR4r-yep-MvDCgCIdaQeArDXKx6Begsg8vJHUitoOoT2IGmllKIuIzkCTdiYAt9QhOejMJlMznoADzqHtrDlruSEQKVfNL89JvP_7NKwj54eMnjeQNV02ACmb2fTPCU9KSKkhnyrf1HhLeah1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PZDqcdSmDdMullMQha2hVrr-XNRl9OPNAjKND188FlPeZdUDEPg7EL2yl4y1z_Zdez8CB-wLyeKKh7f_ckGrgxYJnoRKLmYY4xtz13bWveZpuxu4-OL5df1Ppe5WIdE6cUW5genitg1C-C8alKw8ZrRKZyek091lwnwZ6fgcALevTSHfMbpbRx3AOd7stiRN_bDfhGVOQO3BYPMDQsD2OpC3i0Bq1brbSjeISp1WYz2oQX8fO_RT3VLUcpFuwQ-dNCvVt5tweVqC8lt9x4PU53Rbu5P4i5_Ndz0-UDL4uK1a2nt9svNHiMq20liAdPZppS0s7s_karlX_-DH9c1eoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بیانیه وزارت امور خارجه جمهوری اسلامی در رابطه با تحریم ها:
تمام کشورها موظف هستند از اجرای تحریم‌های یک‌جانبه آمریکا خودداری کنند، و تحریم‌های اقتصادی آمریکا علیه ایران غیرقانونی و کاملاً غیرموجه است.
استفاده از دلار توسط ایالات متحده به عنوان ابزاری برای ایجاد ترس و فشار بر سایر کشورها به منظور وادار کردن آن‌ها به پیروی از سیاست‌هایشان در قبال ایران، نقض حاکمیت ملی کشورها و حق آن‌ها در تعیین سرنوشت خود است.
همچنین، تحریم‌های آمریکا به عنوان نقضی آشکار از منشور سازمان ملل متحد و اصول عدم مداخله در امور داخلی کشورها و همکاری بین آن‌ها تلقی می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/news_hut/70703" target="_blank">📅 13:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ehxqphiRhwMNODIarelYLrnd3jirSx8QWogO3lNGItFhnZJ2eCUDATRLg7lwFoW863yR6PalB8kpUZpcEyRF1kSlNB2vTC5LZ6XYseqBtgASmTb8_11rYJDRDqrXFYEdYHxJMLOIExPXgBr1fxXJD9zTCCLuXEoQy3DxTr7FCK8NJwbmpJmgMdtLh3hR2wEux98_BTWP3b_JGZZgYbM3rMbc-hKLVgXnJGL7abfPnKNYBn6ATWzbp5DZefcBd4vfKS_M7zATaQaucU6-LXp1KjdeeSalxsJEaRWP5KK3fso3HZTnU5u2AlYOu1hd7yQabjwJTjpAOAsLIX4noEyGDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gqZPkCOJWW2S6hIr7c0zQIY6OWOUwtQPTkztGxKq4WOr3eiQ5pGbPeXobgTZiwkShooLyT05jqDb4Cqer1CrhBnMnp-6YluPGn8PkKkiK6QEsQPpf9c8nMjJiJ1DSSB8PNSTSlXDCLD_OsHtWELP_TUd1pP544jtZjxldi5KCOkHwfMRvWApMDscvXUfk0rcB_q8N26TY41ftxyNW0RfY1ZwVWjaIoZMguPN4hqb-rCWUPXrYi-4513WQCJJn9Ml1UHFdj19eQ-akt_jiBgmUcPZU7fQ9iLRiqXsxkNOHjFT3NeObxPThj4VsnHGnmBK7BAU4BAL9fAUGcTi6Z9JTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/mmA5rZ513zMCX9-gUuRqYl3U9e5Vf2hJ6889LHVCjxdPvDVa3oACHxQymddWWeAa2x4dhLFYwHPQFPcQ3e4EOsUchbghHU6NXWknkExyFuD_qUNh1Tq4pDU77xLAmJvJERgueGXGfJrgUpvedV6-PmyvBOEKvn8Zq4lTJbjmQ5V7hCthWng_mbFzrm_05DQ5-g3KlS0zzUh0gfbFzcu3igFJmlWx9xvnok6daTUV9Qj1rD_XwyqYqDSOFoTvaDgI0BjoTq8LNGR8F2Jzd4n7hZS3rj1WbCYP39J80_rgTTkr2NaHk56PCmkPUcFsYm7nFInflewL9h55048Gz_6yKw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
نسخه پرمیوم ایران این شکلیه؛
عکسی که چند تا جوون از دورهمی‌شون توی تهران منتشر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/news_hut/70700" target="_blank">📅 13:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3Y-kcqfbc5Ujw2lqFZaRL-f-BUooOwiRxpAUiP5gB0sOgOVovRpr3Eys-bj47oGtGZSrNz0FjbxDBE_sPwBrZFd9Z2E2nj4Uyz_vaUod13f8x2VDqTZ1N-jdI0MUBiy0cRCGoGoNimhliZ9H8WiCT7T2_PxHZXil7rOXmgIxoPL9eOcJGPUgOTRR-nedMkxZoQ4kyC1pGSHwqa0HM_EEosRF6WcNsrsGbdd-hFIKVy2CiFm0a4Bl7kpeQ0lV1GF373MMoXrrZLlUuuxlYSCZTAlrIDt3sE1Yot201KJcq4tvI75Mdz-8ZU8PNB8ZqImvGLJS7VloKLHbuE-ctPElg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
کافه بابک زنجانی که هفته گذشته افتتاح شده بود؛ به علت بی حجابی پلمپ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/news_hut/70699" target="_blank">📅 12:33 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1291af3432.mp4?token=Wla0jbcWitrmBeG_xkMuBijwdScFfgDRVqxDSOVjwFJXTKr5HOOo4caky8Ije-DaFisI1FtRsB0SmvZGjo9naZiUi2VCUd3PSl7CWGAxI9Ag7IzjX0jGuKFx6WXoBWuy79C2syJRofP5T_9KWMV9S2EZrEYNhYLHUOTvT_URJWASQSwI5w1JhzDLrHUlvtSAbz70rPXUk2BNUnaCQDmUwnjkfffXZ9hSjKriiendl4L0bXLEV0NmHMNv5-6dOLc9JZVVO36vdeGzmEmaM36a3CMyRJDHzzpNJ7a19ht5inupk7fS2hxZN49fjDzCyi8kxN42YM4DeGDQRWD-CvBSRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1291af3432.mp4?token=Wla0jbcWitrmBeG_xkMuBijwdScFfgDRVqxDSOVjwFJXTKr5HOOo4caky8Ije-DaFisI1FtRsB0SmvZGjo9naZiUi2VCUd3PSl7CWGAxI9Ag7IzjX0jGuKFx6WXoBWuy79C2syJRofP5T_9KWMV9S2EZrEYNhYLHUOTvT_URJWASQSwI5w1JhzDLrHUlvtSAbz70rPXUk2BNUnaCQDmUwnjkfffXZ9hSjKriiendl4L0bXLEV0NmHMNv5-6dOLc9JZVVO36vdeGzmEmaM36a3CMyRJDHzzpNJ7a19ht5inupk7fS2hxZN49fjDzCyi8kxN42YM4DeGDQRWD-CvBSRzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
〰️
فرماندهی مرکزی ایالات متحده:
🖥
من دریاسالار برد کوپر، فرمانده فرماندهی مرکزی ایالات متحده هستم و گزارشی عملیاتی درباره مأموریت‌هایمان در خاورمیانه ارائه می‌دهم.
۵۰ هزار نیروی ما در سراسر منطقه، ضمن حفظ جریان تردد تجاری در تنگه هرمز، با موفقیت در حال اجرای محاصره دریایی علیه ایران هستند. ما با بهره‌گیری از غواصان نیروی دریایی، نیروهای ویژه (SEALs) و توان هوایی مشترک، به دستاورد مهمی نائل شده‌ایم: پاکسازی کامل مسیرهای کشتیرانی بین‌المللی از مین‌های دریایی که پیش‌تر توسط سپاه پاسداران انقلاب اسلامی ایران کار گذاشته شده بودند.
طرح‌های بین‌المللی تفکیک تردد (TSS) — که حکم شبکه بزرگراهی حیاتی برای کشتی‌ها در اقیانوس را دارند — اکنون کاملاً عاری از مین‌های دریایی ایران و برای عبور و مرور کاملاً باز هستند. طی چند ماه گذشته، ما به عبور ایمن نزدیک به ۱۵۰۰ کشتی تجاری حامل حدود ۷۵۰ میلیون بشکه نفت خام از این تنگه کمک کرده‌ایم. در همین حال، به دلیل اجرای قاطعانه محاصره دریایی که از اواسط ماه ژوئیه از سر گرفته شد، ایران حتی یک بشکه نفت هم از سواحل خود صادر نکرده است. هیچ کشتی غیرمجازی وارد بنادر ایران نشده یا از آن‌ها خارج نشده است و ما تنها به دلایل بشردوستانه اجازه عبور داده‌ایم.
نیروهای ما با به‌کارگیری بیش از ۲۰ ناو جنگی و صدها فروند هواپیما، با موفقیت مسیر ۷۵ کشتی را که قصد دور زدن محاصره داشتند تغییر داده و سه کشتی متخلف را از کار انداخته‌اند. در جریان بازدید اخیرم از منطقه، شخصاً شاهد فداکاری، حرفه‌ای‌گری و آمادگی فوق‌العاده ملوانان، تفنگداران دریایی، سربازان و نیروهای هوایی‌مان بودم. آن‌ها همچنان با تمرکز کامل، توان رزمی بالا و عزمی راسخ به وظایف خود ادامه می‌دهند و من به موفقیت تاریخی آن‌ها بسیار افتخار می‌کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/70698" target="_blank">📅 11:47 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=cJzanYmioCNRFAnucikNm62RzMtN_mo7l-LAS7NAWLGibcIJ0HtlLWqOWGLMyIlgpssRyOB9qlIxyU-l8v33tr4MOW9C64M5ogBnBXgtZxs18YCzqMS44xOsGjwYCe1uEiRGIpVVHf0b8aJqxfXt4i9plR-8tuuSbFmBWxebSPeHVZdxHAJZKCLeSwFFVQx7MEiybYAwQwkke9NxPH-I3CWKQdHocWzBpDhj5se_jBfGnI8FtpjkuZp3lNo7J-nhlXatcHx0P_cL_TwPJvMwrIJwkHdOazFNsE1qu_hJKIRWeWxry_nX2YsR_sGHfRL3B8RavUzWzG6xHrEKp7qbRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c1e3e3b651.mp4?token=cJzanYmioCNRFAnucikNm62RzMtN_mo7l-LAS7NAWLGibcIJ0HtlLWqOWGLMyIlgpssRyOB9qlIxyU-l8v33tr4MOW9C64M5ogBnBXgtZxs18YCzqMS44xOsGjwYCe1uEiRGIpVVHf0b8aJqxfXt4i9plR-8tuuSbFmBWxebSPeHVZdxHAJZKCLeSwFFVQx7MEiybYAwQwkke9NxPH-I3CWKQdHocWzBpDhj5se_jBfGnI8FtpjkuZp3lNo7J-nhlXatcHx0P_cL_TwPJvMwrIJwkHdOazFNsE1qu_hJKIRWeWxry_nX2YsR_sGHfRL3B8RavUzWzG6xHrEKp7qbRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
از من خواسته شد که پوششم را تغییر بدهم و چادر بپوشم، گفتم که حاضر نیستم و چادر سر نمی کنم!
از زمان دبیرستان روشنگر بودم و چادر اجباری بود و سر می‌کردم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/70697" target="_blank">📅 11:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70695">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLX7dCLPmmCNHmKiONhbD-OgENXVZ4rjiqwTTdMpBLVodICzY4oAaYzqUXLLlWAU1zYKI47llXIDyR8s9gfsB2l6sGrz02vII3nGgGGTaw67wunbI8106cj7laM2LpTgp7hcvtM_VSTb8nhGuX2-bqdZVyCU2hQ7TcOJBh18liw3227gAEDvwTTnfWVzWf9Y_gQILjarfk5zERwM7EOPDQTGoS7jYW5FP1N5rq8IoIt-HduwV0sjNUSF2WxUonkoCIMtIYqMKJ7qyl3_IE06hnsXBBDIhPtnaE9bz80sMEO4fQRxXM0K1-3ik88qGXPbkoZ0faPuDbFb4f_GDV9s-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6029290388.mp4?token=BVneXzvpbsLy0Z_eU3URf8RSPg0MevUtTRPpR_LqIjXI2XD5cEE1rH8Ub_jlCPTNGlHh7h6hoLJENghzUgEJVQ-RTzyC4wWTfXNKGnCSj2rdL9fa5QRlqLSMdQRE_E-jDLlzBAJfM7J-4WJHVbwbcK-K2P_-EaBzcaVVFYwMOOQR-J90aGoA0JFpjQE2mQXWrpzPxm9-PAmI_EdJo5OQmZ8XaASb8ydXZiVZ7YLMK2z2aw9QeDy0BR_Ng-I3fJPfe17bkoP-hEF0BFQAENBQEX1RkufZV48mBhn9d7-5aryjfhTHP1GWRTKG2uTiapiTPjzCNdU0KjPJxckbOdUQXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6029290388.mp4?token=BVneXzvpbsLy0Z_eU3URf8RSPg0MevUtTRPpR_LqIjXI2XD5cEE1rH8Ub_jlCPTNGlHh7h6hoLJENghzUgEJVQ-RTzyC4wWTfXNKGnCSj2rdL9fa5QRlqLSMdQRE_E-jDLlzBAJfM7J-4WJHVbwbcK-K2P_-EaBzcaVVFYwMOOQR-J90aGoA0JFpjQE2mQXWrpzPxm9-PAmI_EdJo5OQmZ8XaASb8ydXZiVZ7YLMK2z2aw9QeDy0BR_Ng-I3fJPfe17bkoP-hEF0BFQAENBQEX1RkufZV48mBhn9d7-5aryjfhTHP1GWRTKG2uTiapiTPjzCNdU0KjPJxckbOdUQXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
📚
آرش عمید دبیر هندسه و گسسته کنکور، وقتی یکی از دانش آموزان بهش گفت ما پول دادیم، اما نصف کلاس یا داری حرف بی‌ربط میزنی یا کلا صدا قطعه، به این شکل توهین آمیز جوابشو داد!
🗣️
بعد این قضیه آرش عمید اومد و از شخصی که بهش توهین کرده بود عذرخواهی کرد؛
ماه‌های گذشته با اتفاقات سختی روبرو بودم، پدرمو از دست دادم و شرایط روحی خوبی ندارم.
اما بازم این کار منو توجیه نمی کنه، بخاطر حرفام که باعث رنج اون دانش آموز شده معذرت می‌خوام.
در ادامه هم گفته که هزینه که این شخص برای شرکت در کلاس داده رو بهش برگردونن
.
@News_Hut</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/70695" target="_blank">📅 11:04 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">💢
‼️
تریلر کاملGT6 که راکستار رسما منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/70694" target="_blank">📅 10:32 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
فیلد مارشال محسن رضایی:
ادعای ترور پسر ترامپ؟؟ توهمات نتانیاهو هستش و اگر ما چیزی بخوایم بکنیم کسی نمیتونه جلوشو بگیره
ضاحیه و بیروت خط قرمز ماست کسی نمیتونه به اونا صدمه بزنه
باز شدن تنگه هرمز منوط به اجرایی شدن شروط ایران توسط آمریکاست
محاصره ادامه پیدا بکنه بشدت اهداف اقتصادی آمریکا رو میزنیم
آتش بس در لبنان و غزه جز شروط اصلی تفاهم با آمریکا هستش
نتانیاهو رو خواهیم کشت
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70693" target="_blank">📅 10:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/51590b7113.mp4?token=P1dhhLQcgSXqczMcle_1jjsjCu8Cpbf9Gk6CL6kSLSNH09JIiSK3t1JIj2tl6aybTw4Rs1tKTpE6mAwqrzCqgSwmQHUQoBQlXTxMT2MwxSnbhSoI6yH9jPHIJj7kupjznEecTTf-WiLZ3v6fVHXaGI42wSgz02pFbR83cN60wJqN--2zz-8Ixva5S3QjT4Vn-petrvXqIAi1umh0E_7Unl1FNQ9ML_Iibd9dAbxrG6tcGe0s0NVjrBnpqnPKoDpuPut0_CYq1nipvTXUUHFfEXqJ3kdiAGcrCrIql3NEo1MLlaeB6eEaqzre-iAc7Mvt3XHtl3eaXg8PLFix4lBavQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/51590b7113.mp4?token=P1dhhLQcgSXqczMcle_1jjsjCu8Cpbf9Gk6CL6kSLSNH09JIiSK3t1JIj2tl6aybTw4Rs1tKTpE6mAwqrzCqgSwmQHUQoBQlXTxMT2MwxSnbhSoI6yH9jPHIJj7kupjznEecTTf-WiLZ3v6fVHXaGI42wSgz02pFbR83cN60wJqN--2zz-8Ixva5S3QjT4Vn-petrvXqIAi1umh0E_7Unl1FNQ9ML_Iibd9dAbxrG6tcGe0s0NVjrBnpqnPKoDpuPut0_CYq1nipvTXUUHFfEXqJ3kdiAGcrCrIql3NEo1MLlaeB6eEaqzre-iAc7Mvt3XHtl3eaXg8PLFix4lBavQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیویی از وضعیت اسکله شهید رجایی بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/70692" target="_blank">📅 09:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEnjNW1HPfQgpe68gBot9Zp9Ng7aOnbdDpRSkRicaPJ5W56ePGtMU5F0gRSMMZgOqhGv1fwoW03naez6bOMCQp5zj-W34fzkTRce4uvgGHDJ38Iw_YjZ_pqhSGUxwj3ljP3h1tnjATALHrWuCc11uZM1i0oCdHy9OH3umqHRtIitBhybdxDDsQE3IvA7xsNQEVG5OTTLmPk9dBpL6J63zvEI80dOe_-erxo5M6RdK_5YdiY5xbghIN3FJWZy7lNFOk-EwZBe4LjK7okSjPpNNAmPanlhPCGAa1OkFGHVjbbEkkdwCDeo2nG_HXDHKTyell2NozLoF1efPxeiTlj6ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
وال استریت ژورنال:
ترامپ بازگشت به توافق اولیه ماه ژوئن میان آمریکا و ایران را رد می‌کند و در عوض بر این باور است که تشدید فشارهای اقتصادی، تهران را به دادن امتیاز واداشت خواهد کرد.
ایران تأکید دارد که هرگونه بازگشایی تنگه هرمز باید بر اساس چارچوب ماه ژوئن — شامل رفع تحریم‌ها و محدود کردن فشارهای آمریکا — صورت گیرد.
پاکستان، عمان و قطر برای میانجیگری تلاش کرده‌اند، اما این گفتگوها پیشرفت چندانی نداشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70691" target="_blank">📅 09:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiSkjyur5HRoSZ-Wq00frx4DtxiSI2jv-YNRzwTYRRCUl0lM0F3r-r5IbghBB4JHFMi38DB7yPwAtbvBjJ7o5u0d-5Om-2M-FpOg8D9GREf581VW4Gp53MxXos9CWh5q88T9KoTDerrkeBcqwbQCOmXGHCEOhX4SzAGvR-9QvGcL38tbUPQcVenV6CTGwjkX882h-9Ua_5WRIBSfrKNep4W8zE4CTFhW41ZdVUbrqPLmMlFJuP1gblOEJUkgbTfn_z2GMcu5nVnrTK-lpmvJBiIBAUXQeTxx9eLyMy2CqCilJfZ0GjTVr38_9s3RV3uJW35UM4AD1tAq5QPX1G22yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ایران کشوری رو به فروپاشی است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70690" target="_blank">📅 02:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLV3rDmyoVBg7dxWwRvJ7SRpSNW7z5wke2LtM4CcMQ9oSrHxBmKhb4b7a4HaP58gG_uNQoa3H4977F94uHmkQmonzytcmnD-SDpgdJNyNPVyuaiL20GBkldcICzTUL53QEjlIx5b0XfI-3GKEIvxRtg0GZnC4WfmQNdd41YRpNVUF1t3Soqq0Ob8AN3xv7-fgwEr4TKMGlmI86j6ZZyPa5g5UX3CAGCNbNdpMlFbmUjGNqfW4ld5-QVO9LAhlXTBwi4u1SM0NnZAoqnEoS1rnEsav6jV2W4ltBIly68RPHhpwghYHxoAgF0fIfAypkHBoEDGUZjxZek75yFDsewRyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت! می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.  @News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70689" target="_blank">📅 02:01 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PF9k0mPFjJPiOxfc0pXIGHk5DIcEaBgdb7ReSpEXO2C0pJaemN5w0IIA-zKxtJHymYVGuXrNRaEmpuZqI17urTjIRffooyFPllIWTKQo8lR-BreNc0bM363TocBeeDPSpNKsYk9dcAJNL75ShUVHfqqyQRlMknDrFmmU8fvFi-5NNocHBOZ2coBZL-B0KMuqfVV7kzhf3ZmMAp04cVKsP69xTiyQIDXTQMOt8eSBnP_faYQZQuSfRQM6bVRSlp7Cpc9-AemUnjMyVdFDMQFzze9mQeNStWtrBErKLTiO73iesi8hhttsGpa1vxsMW-902n8i3u_4I0gYtBVBBXtDeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇺🇸
ترامپ رده‌بندی رؤسای جمهور رو منتشر کرد و خودش رو به‌تنهایی در رده «بزرگ‌ترین» قرار داد.
🗣️
جیمی کارتر و اوباما و بایدن در پایین‌ترین ردیف«بازنده‌ها»قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70688" target="_blank">📅 01:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">⭕️
تریلری که راکستار به صورت رسمی از GTA 6 منتشر کرد
💢
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/70687" target="_blank">📅 00:46 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFY97xaf7BS6pSzSM12qYUfkvP1MxsTFUy0-9siKPYmdZLULcGQ-GxDY9vOWJVU9myRhlM5qHf3ArlTyNDLftlbcUxABlde_jRlbrVn1vgKzWPbFblrACZzcI5FF_9A7oaMewlaGaHhaNfqBNBGnebPf-uZqNmd4nPaeURjXdNVRZhjxb97rO2XOpRTqviIQgE99j8QRw6lDrUBPFb4hFJ8fGKjmh9XdMGOH9RMHHvcef3wTr86Bd5AAhJnCd2bIXjeWDl4Y1X7Pf4ywJcMB68f_VFbdARTIrSniHI7xnNE20KBZFKl9lD7oVrSFbfKJjdLxUyGubaSLBvpwdOzZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
🇮🇷
درحالی که دلار به تازگی از مرز 200 هزار تومن هم عبور کرده؛
دیروز پزشکیان به مناسبت گرامیداشت روز کارمند، از تیم اقتصادیِ خودش به خاطر عملکردشون تقدیر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70686" target="_blank">📅 00:34 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=c91WoR_GP1idgBl178VCxkBVJiGZj4iRTDDxzrCdO8w-Dp56Ds8MzZcmopPylKw82M91m7uNXn1JsMIiu9ErL9u1FUe65qU7fLQW86QBCUtlr4EriqIxZIfmiQy7FTuWGNE3bCXItbyr5AAgHae_6KEvViNM_igECMOucmVkT_sRjxEdJ0f9-KMySJUOyMoLbBjkzFmVkzLVM6HjxSopNbPh-lSRAlAuMYD01xIMSGmjZSKeSTRnQRc60FVHqouEA1i-i44Da2vEHl-wkaDCmN-nm2nQVRzMQ7izpUUemkovXjGbizY9IfK9F4ac6pxsCPJv9jU99YBe_k63w_PhvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13108aa49.mp4?token=c91WoR_GP1idgBl178VCxkBVJiGZj4iRTDDxzrCdO8w-Dp56Ds8MzZcmopPylKw82M91m7uNXn1JsMIiu9ErL9u1FUe65qU7fLQW86QBCUtlr4EriqIxZIfmiQy7FTuWGNE3bCXItbyr5AAgHae_6KEvViNM_igECMOucmVkT_sRjxEdJ0f9-KMySJUOyMoLbBjkzFmVkzLVM6HjxSopNbPh-lSRAlAuMYD01xIMSGmjZSKeSTRnQRc60FVHqouEA1i-i44Da2vEHl-wkaDCmN-nm2nQVRzMQ7izpUUemkovXjGbizY9IfK9F4ac6pxsCPJv9jU99YBe_k63w_PhvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بخشی از یک موشک ضدکشتی جمهوری اسلامی در نزدیکی سواحل ایران
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70685" target="_blank">📅 23:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=FzauQqyJkDN0WOCQxpE1n-Sr4esy2oJ9U8l2aq0oReL8LodM4tdkRf2JMLfvFwnNz8pZZq6at7iMMi8lQU14bLyOvFjKw1yqfDuxts7tYO8wahKZfScW_03E7a2rPNLEx4kwwzvq0gs-pMV9DWhhQgx3KtuK6DmE8Z9iJlJA_0nWzKeBmFFxzdYRvpUuNKYn1tVZYd8PnNN6hExfSU7X0GCEJlQKt1BW4xG36Be01j8z843Cng3ggdStPP63pvP1-UMY-O1yoM3a88ltl5ooS6LsvMbwFKkdDb7cE4G6K_LmbPYf1NynXMfhSzMID5fJVHdPmZLzH7V6C60DIVea4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3febd1d3.mp4?token=FzauQqyJkDN0WOCQxpE1n-Sr4esy2oJ9U8l2aq0oReL8LodM4tdkRf2JMLfvFwnNz8pZZq6at7iMMi8lQU14bLyOvFjKw1yqfDuxts7tYO8wahKZfScW_03E7a2rPNLEx4kwwzvq0gs-pMV9DWhhQgx3KtuK6DmE8Z9iJlJA_0nWzKeBmFFxzdYRvpUuNKYn1tVZYd8PnNN6hExfSU7X0GCEJlQKt1BW4xG36Be01j8z843Cng3ggdStPP63pvP1-UMY-O1yoM3a88ltl5ooS6LsvMbwFKkdDb7cE4G6K_LmbPYf1NynXMfhSzMID5fJVHdPmZLzH7V6C60DIVea4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
کارولین لیویت در آستانه آخرین روز کاری‌اش به عنوان سخنگوی مطبوعاتی کاخ سفید، سخن می‌گوید؛
«احساسی آمیخته از تلخی و شیرینی دارم. تلخ است چون شغلی را ترک می‌کنم که بسیار دوستش دارم؛ کار کردن برای این رئیس‌جمهور، یعنی رئیس‌جمهور ترامپ، افتخار و موهبتی بزرگ در زندگی‌ام بوده است. هرگز کسی مانند او نخواهد آمد.»
لیویت پس از ۲۰ ماه فعالیت در این سمت، کناره‌گیری می‌کند. دلیل این تصمیم، تمایل او به گذراندن وقت بیشتر با خانواده و دختر نوزادش است، هرچند او همچنان به عنوان مشاور ارشدِ خارج از دولت به همکاری با این مجموعه ادامه خواهد داد.
«آن‌ها در مقطع حساسی از زندگی‌شان هستند و بیش از پیش به حضور مادرشان در خانه نیاز دارند؛ بنابراین مشتاقم که وقت بیشتری را با آن‌ها بگذرانم و در عین حال، همچنان به عنوان مشاور ارشدِ خارج از دولت در خدمت رئیس‌جمهور باشم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/70684" target="_blank">📅 23:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c174815597.mp4?token=bNA8MIC2XJGxFJVY6ZptqdlHIe6TMRsMyNYYG1axWKo7wLqYynHZM4IAGbVCXam6mPPuAtm_qnOBaAHsyI-lrGIy_gICemISy_lLsYPs65wCiLsu4UyJZog2eTB11tB6DGn_YfAYZwt-Yy-1_NoBM_PtBpEeyXZetVaFJcUfuIpnGUsoEWLPxOP1dlFyhzh8cuJrABwnxbmP3tVahkctdHaNMj4rnMYnJiL0EmMdDypy6Qk5UZQVNreZeoQ2ACV21Yw2l9xHNr4zn2SCxynKOUOErgwMglF9y9LGeXETK0hZ6SmM_hLxfTdDgI9tnwBdEZ6detGcD2uLDc-swMqlAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c174815597.mp4?token=bNA8MIC2XJGxFJVY6ZptqdlHIe6TMRsMyNYYG1axWKo7wLqYynHZM4IAGbVCXam6mPPuAtm_qnOBaAHsyI-lrGIy_gICemISy_lLsYPs65wCiLsu4UyJZog2eTB11tB6DGn_YfAYZwt-Yy-1_NoBM_PtBpEeyXZetVaFJcUfuIpnGUsoEWLPxOP1dlFyhzh8cuJrABwnxbmP3tVahkctdHaNMj4rnMYnJiL0EmMdDypy6Qk5UZQVNreZeoQ2ACV21Yw2l9xHNr4zn2SCxynKOUOErgwMglF9y9LGeXETK0hZ6SmM_hLxfTdDgI9tnwBdEZ6detGcD2uLDc-swMqlAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای این فرد که در حال وایرال شدنه:
الان که رهبر رو زدن، مسئولیت این کار زدن رو گردن نمی‌گیریم، جرأت نداریم رهبر بعدی‌مون رو نشون بدیم. به هزار تا داستان دیگه داریم. ته جنگ‌مون معلوم نیست. نمیدونیم خونه هامون میمونه، خانواده هامون میمونه، ناموس هامون در خطر هست یا نیست.
بعد بگیم که آقا ما دست‌مون رو تنگه و هرمز گذاشتیم. خب حرکت بعدیت چیه؟ بعدش میخوای چی کار بکنی؟ خب من... شما پنجاه سال این کشور دست‌تون بوده، نمی‌تونید یه تورم ساده رو کنترل کنید. ادعای حکومت امام زمان رو دارید که میخواید دنیا رو برای ما بسازید. خب خیلی خب.
بحث ساده فرهنگی‌تون، آمار طلاق‌تون، آمار احتکار‌تون، آمار دزدی‌هاتون. یکی یکی آمار، یکی یکی دارم میگم. میدونم تمام کل و هزینه سرمایه این کشور رو برداشتید. همین آقایان استفاده کردند به هر قیمتی هم باشه.
من یه حرف رو میزنم. همین آقایان سپاه رفتن میلیاردها دلار هزینه کردند، عجیب و غریب و زندگی من و شما و بچه هامون و نسل های آینده رو به فنا دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70683" target="_blank">📅 22:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70682">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=ewFiBzYlLsWRSR-g_kzoru3IFGH7Stz7BJjCToeUAtTKt0rlgUTyKAaqCabfaKxuaDDqEwHOZttfFsRrUb_WfQQohTDA1EyCEvwWC0UnjkXJfIVVcV4UGVJ1JAethPHX1Uzh-C8u778DjTr5YgEdVl7qlxU7nmlQchoLfmqiwoEzva-NE4GjrgY2vCQ9ABNY3K5PUxvUHGbwR1--KhdjBVb8SO97H6-z23gpAGFr9BbXkum97WU_stblyxqyo1uuvG9mBPo4cSEOOmZWPaltaCTHxmkl1X8jtT797uKOCsRN34XN4zHU5afvBxc66GC9Eta4UqyvUtyk5ZXHXk6Plg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8a6f01648.mp4?token=ewFiBzYlLsWRSR-g_kzoru3IFGH7Stz7BJjCToeUAtTKt0rlgUTyKAaqCabfaKxuaDDqEwHOZttfFsRrUb_WfQQohTDA1EyCEvwWC0UnjkXJfIVVcV4UGVJ1JAethPHX1Uzh-C8u778DjTr5YgEdVl7qlxU7nmlQchoLfmqiwoEzva-NE4GjrgY2vCQ9ABNY3K5PUxvUHGbwR1--KhdjBVb8SO97H6-z23gpAGFr9BbXkum97WU_stblyxqyo1uuvG9mBPo4cSEOOmZWPaltaCTHxmkl1X8jtT797uKOCsRN34XN4zHU5afvBxc66GC9Eta4UqyvUtyk5ZXHXk6Plg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
سر دادن شعار «مرگ بر آمریکا و مرگ بر اسرائیل» در نشست علنی مجلس
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70682" target="_blank">📅 21:53 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70681">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=hk4v7lj63T6TUMVrDDQqTIb8IoSyqwvHv_3SOjiR8HKVQs4DMdKchXHAozWpOLApFwJAFI5SgZkh-HFvatnuOFCQi30lA314fvZ5RvZXn6VpttxpZ7RV9p9xGkpzsSMFEieE0JJcidk06p8PZw7IPMf-fBDocyO0t3rs57THBsP41c3Y3Aq8H8TU3-PWRa1RCLEZ9FP7OtiCExZC_zZ-_pCNj7x3r7Jq1g56TkzW1UMLLdM9y7jzSUCklhqRNcE3bmIJrPJznSOInrqg-FuCDDPC3J3ieZU53JX31kb1fldfnmr5FvQKCitMILFViHvVeNs0pp-wXGDDvqYsj8d0Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cc74b5c0f.mp4?token=hk4v7lj63T6TUMVrDDQqTIb8IoSyqwvHv_3SOjiR8HKVQs4DMdKchXHAozWpOLApFwJAFI5SgZkh-HFvatnuOFCQi30lA314fvZ5RvZXn6VpttxpZ7RV9p9xGkpzsSMFEieE0JJcidk06p8PZw7IPMf-fBDocyO0t3rs57THBsP41c3Y3Aq8H8TU3-PWRa1RCLEZ9FP7OtiCExZC_zZ-_pCNj7x3r7Jq1g56TkzW1UMLLdM9y7jzSUCklhqRNcE3bmIJrPJznSOInrqg-FuCDDPC3J3ieZU53JX31kb1fldfnmr5FvQKCitMILFViHvVeNs0pp-wXGDDvqYsj8d0Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
ما یک خلیج داریم. یک دریاچه هم داریم. حالا چیزی که نیاز داریم، یک اقیانوس است.
بنابراین شاید مجبور شویم نام اقیانوس اطلس یا آرام را تغییر دهیم
😠
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/70681" target="_blank">📅 21:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70680">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70d624c250.mp4?token=HSWXsmUPNHkuC04Ig11fCfOWrwjQRUyp1Kr6OYUHX9uU6Mz8-7iZkTj0Y5fKsfVSYjAWZgBxp8EdLBG_BeSON7laMzKJJwbScf3gmhpsWQooowiMy7PEVAClu1N2LTr3CJLQ1yKQIbs_-4luz3-eSwt6z5PjTPU3iNk9z7cAz1UhL_bFYtV-FqAcc29gGwFJL1pZtG3dn4q_WTv8om5kkobbCEVsAA3svF866nU1Qrwa1mKKNEPYdEVWdbuQIoURBNJBJ22lR3Eq_L7IkesmFx9er__T1eHViXspKzGjNNZ_Eg1B0IdLlTA20_x3U06q5K5PRGNDa8yD8A1TKArYODBbh87dt_yh0IfVtBxEApM-t-4H98RlOCRn61yZHDwJQdugGCe1pf_nk3_d07OtVRte2GJaVvDMLm10bwZHQmahNL1-YRl4HnfV_mXYy4spJ8VBoH_qOz7sQWfXhPd9dHxREuc7S5tpBZLrKtW1GH8RWQGi0DL64CgaETocHO8fzl9hCNt0toHhEtyK66U5IR2h6dGtA3bBMt124UtoWn97IOYHjzrDzF9aAFPZfI0NOQPJnTssKYfGLj5wQhHXw5OGgro1fYF3FBDMblrWvBWGhadhGcXys7acdlvPCaxecdXxG01KWGkYisqYBw60KoBFQl1AWfttMoXRhXcDZ6c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70d624c250.mp4?token=HSWXsmUPNHkuC04Ig11fCfOWrwjQRUyp1Kr6OYUHX9uU6Mz8-7iZkTj0Y5fKsfVSYjAWZgBxp8EdLBG_BeSON7laMzKJJwbScf3gmhpsWQooowiMy7PEVAClu1N2LTr3CJLQ1yKQIbs_-4luz3-eSwt6z5PjTPU3iNk9z7cAz1UhL_bFYtV-FqAcc29gGwFJL1pZtG3dn4q_WTv8om5kkobbCEVsAA3svF866nU1Qrwa1mKKNEPYdEVWdbuQIoURBNJBJ22lR3Eq_L7IkesmFx9er__T1eHViXspKzGjNNZ_Eg1B0IdLlTA20_x3U06q5K5PRGNDa8yD8A1TKArYODBbh87dt_yh0IfVtBxEApM-t-4H98RlOCRn61yZHDwJQdugGCe1pf_nk3_d07OtVRte2GJaVvDMLm10bwZHQmahNL1-YRl4HnfV_mXYy4spJ8VBoH_qOz7sQWfXhPd9dHxREuc7S5tpBZLrKtW1GH8RWQGi0DL64CgaETocHO8fzl9hCNt0toHhEtyK66U5IR2h6dGtA3bBMt124UtoWn97IOYHjzrDzF9aAFPZfI0NOQPJnTssKYfGLj5wQhHXw5OGgro1fYF3FBDMblrWvBWGhadhGcXys7acdlvPCaxecdXxG01KWGkYisqYBw60KoBFQl1AWfttMoXRhXcDZ6c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇺🇸
🇨🇦
ترامپ فرمان اجرایی «تغییر» نام دریاچه انتاریو به دریاچه آمریکا را امضا می‌کند.
🎙
خبرنگار:
با تغییر نام دریاچه انتاریو، چه پیامی برای کانادا می‌فرستید؟
🇺🇸
ترامپ:
هیچ پیامی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70680" target="_blank">📅 21:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70679">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=SCwhuysz27xQB6iXSeA_pIJwtHR77nbDGFHEyhF0gpXp3DPG3Q9ETj-J1VgggpwQOJVAtRWqcRIQfVPzyzDyTUbwlHXDYJ7H4rVujn04Ar0unlo0psjk2YrIqTo_faSCVFyF-ySEZUjuZa7kNLLYR-qkBKmadwQc6ldDNM9vlmCNVTPNtl6tig-xEt8Dd14r7kxWCCw0tWBILN44yBKfgXmL8ag0C_GYaOdqK9kMuwhx4jbGdgPKR3WOi-I5BXBzJUE6W2R7h_6OY80YUqYs4Iri2ZIJFm-jyq5dhF4lnOovbVWxjDaWgY8L6c0VE95LRp9UfUziPzxLhKkWl_11XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609cc5c89b.mp4?token=SCwhuysz27xQB6iXSeA_pIJwtHR77nbDGFHEyhF0gpXp3DPG3Q9ETj-J1VgggpwQOJVAtRWqcRIQfVPzyzDyTUbwlHXDYJ7H4rVujn04Ar0unlo0psjk2YrIqTo_faSCVFyF-ySEZUjuZa7kNLLYR-qkBKmadwQc6ldDNM9vlmCNVTPNtl6tig-xEt8Dd14r7kxWCCw0tWBILN44yBKfgXmL8ag0C_GYaOdqK9kMuwhx4jbGdgPKR3WOi-I5BXBzJUE6W2R7h_6OY80YUqYs4Iri2ZIJFm-jyq5dhF4lnOovbVWxjDaWgY8L6c0VE95LRp9UfUziPzxLhKkWl_11XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
چرا بانک‌های چینی را که با ایران مراوده دارند، تحریم نمی‌کنید؟
🇺🇸
ترامپ:
چه کسی گفته که این کار را نمی‌کنم؟ شما نمی‌دانید که آیا مشغول انجام آن هستم یا نه. لازم نیست همه چیز را اعلام کنم.
🎙
خبرنگار:
با کدام‌یک از رهبران درباره قطع روابط با ایران صحبت کرده‌اید؟
🇺🇸
ترامپ:
صحبت خاصی در کار نیست. ما نمی‌خواهیم با آن‌ها صحبت کنیم. تنگه باز است.
اقداماتی که در قبال ایران انجام میدهیم به معنای منتفی شدن گزینه نظامی نیست.
گزینه نظامی همچنان روی میز است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70679" target="_blank">📅 21:19 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70678">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItHaFvW904edZdCCB1GkXd6aQjBs1IZ7WHJqvDyuW0BsXKeEojm1FtZkAEBRUchJfFQB1f71sHb4ytYiZjGMoFqtcmDJWAYsFGKqh8KXDZHMNTITgPUPp3OKnysBbUDkHqs-p77X_jbqeRAHT8ysUZzI2hzVDvnYwl9apHBWhcmFPYgv7OTzEnruwY_M2j4xK64BEegBixA2tY5vEB9jTi-BqNoRh90zEukSFzLy--q3ETlZ-hDBtOpJsMlbKAvKgvpvmCGUM_d9Jv5jhV3CAR4dpmntPkSIT4IVuRh-ykprzEHbzdYT5aHTZF9xIyFMAXZyO5TdjGMqlWf5SWdE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇼
🇵🇰
کویت و پاکستان یک توافقنامه مشترک دفاعی و همکاری نظامی را در اسلام‌آباد امضا کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70678" target="_blank">📅 20:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70677">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtpRWO_NBZCLfFjB7vn-zxMlT-ccwSfIdkA5ajKvcZBJCDM-6y2xGxxb3KqUUQBuSA8anEjjwOC9FOqxYlm6Zs-UzoazCGOTjY6DrzprfVZoc_sS827T9lw6gUtxylsfscr4SqlnMVLcYdEa4AOjEn2NEW5Z3Qw0CHyqhYkJBOvUEW6UPGF9ID_fML6I2I-d8gmDoWDqXN1nko3IsG5oiP8bqr0FJKp9CZltRLof4AZp8L-1zVt5mvLAn0IbIiB0_3i048H0gtiLBk_5h4g_evWNLp18J4E1heQLZiNYwnjFQVehefbEA1zmd43QDGZjlap349BabOIlN_bFfQAtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
قالیبافِ در جواب بسنت:
این امپراتوریِ رو به زوال، به‌جای سرازیر کردن میلیاردها دلار به سوی اسرائیل — آن عامل نیابتیِ تروریستش — و صرفِ هزینه برای ۷۵۰ پایگاه نظامی، می‌توانست آن پول را خرجِ مردمِ خودش کند؛ اما نه، چنین کاری برای این رژیم بیش از حد منطقی به نظر می‌رسد.
اسکاتی، رفیق، اعتبار تو در خطر است. کاری بکن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70677" target="_blank">📅 20:31 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70676">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=RN9jvkpuoXyrUbxXIVuslWnochhlcNE926QPN8KYYv9csCIvZWtcO-I9ZQMv5Ua2XuyaZPgCFfl6pDwYMFesV1ae9m-YD-4h1alAs9_5U0mxz5C8IvXRkIfeNXVD0dPGlsPqBegvvsHIHhK0B5Z_MmHA8nLHeSoNLBQaz5K4-lkqnmmrhsQeKRYiPZMP-6l8ZSthNgWlJTPOWPuPn2XODYiX-o99LOVPheJaJOogLhfHGcT2a18X5dPgp9sbqG21r9sY-q5s2SmulS_tWAFHQOWlwWjHZ_a_jgtx093o_QZ_vqbXi8-fC8rKOYBpoL8cshvXcGXnj7ZBsl8gcayfUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a4150d1.mp4?token=RN9jvkpuoXyrUbxXIVuslWnochhlcNE926QPN8KYYv9csCIvZWtcO-I9ZQMv5Ua2XuyaZPgCFfl6pDwYMFesV1ae9m-YD-4h1alAs9_5U0mxz5C8IvXRkIfeNXVD0dPGlsPqBegvvsHIHhK0B5Z_MmHA8nLHeSoNLBQaz5K4-lkqnmmrhsQeKRYiPZMP-6l8ZSthNgWlJTPOWPuPn2XODYiX-o99LOVPheJaJOogLhfHGcT2a18X5dPgp9sbqG21r9sY-q5s2SmulS_tWAFHQOWlwWjHZ_a_jgtx093o_QZ_vqbXi8-fC8rKOYBpoL8cshvXcGXnj7ZBsl8gcayfUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صف عجیب پمپ بنزین در کرج دیشب
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70676" target="_blank">📅 20:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70675">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxmaCiPU3Ry-PRD9IvZWLi_Q0UU2lSed_x5CZhFmPKcbUrkefa3ITzr6-R4ghRxQa2bEURWrO2FihRZIthOmw_xtDtK-JdjuPptd_QWdevve4UnBR8cVsr1-JKQ-a8cxMgnGYoxUEVICMB6LArRoox8f7r94CLOOhEPKBvhrFtno-fncHV5I1f7mNJ5FRUqLHp9baoKldCSbEir5g7IPb9sS4v5agyQbvnq2p280YArjXjcu_R5UE7a3MnMH2EDai45VfUtrzOrsayUQfQ-s2458IdzM9leiE11lR04TGZx8kgfnNuMD6JcnSfde8_XhKTQNRr92_Fd4cXALUVb0NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
سنتکام:
هم‌زمان با تداوم اجرای محاصره علیه ایران توسط ایالات متحده، هواپیماهای جنگ الکترونیک E/A-18G نیروی دریایی آمریکا بر فراز آسمان خاورمیانه گشت‌زنی می‌کنند.
تا تاریخ ۲۷ اوت، نیروهای «سنتکام» (فرماندهی مرکزی ایالات متحده) برای اطمینان از رعایت مقررات، مسیر ۷۵ کشتی تجاری را تغییر داده، ۳ کشتی را از کار انداخته و برای بازرسی وارد ۲ کشتی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70675" target="_blank">📅 19:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70674">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0833865a38.mp4?token=Y8KD_rg59JsOpmxNSMlegEeXeUkQ4MUNVqnGh4s65s8R1n3Wr049S3WE_WBQi4ox4kIB3N8yS6POenJfUDWekEBqc4KK7VFTUmPhad-bqlNIfFMmXK9LA7M1knjckElRAFIVC3GRHerl_LpCBjzziv6zlokEmrq2ekaJSbHhtwD1olavRZiubguplFxkdHJ3BApaOxtQvuZPHHMQF0PWg5FG_Apb_18syjtNwAO6xFcTQo-l8S_f_2GvWpRLR4VmHyayikVs-vD_LwfCw56dpLhCS3dfncPSb0-WgWADVRCBFg_SLXhNiOnV199zqA7JCE5Y71o8ZWAHe4CBfjkysQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0833865a38.mp4?token=Y8KD_rg59JsOpmxNSMlegEeXeUkQ4MUNVqnGh4s65s8R1n3Wr049S3WE_WBQi4ox4kIB3N8yS6POenJfUDWekEBqc4KK7VFTUmPhad-bqlNIfFMmXK9LA7M1knjckElRAFIVC3GRHerl_LpCBjzziv6zlokEmrq2ekaJSbHhtwD1olavRZiubguplFxkdHJ3BApaOxtQvuZPHHMQF0PWg5FG_Apb_18syjtNwAO6xFcTQo-l8S_f_2GvWpRLR4VmHyayikVs-vD_LwfCw56dpLhCS3dfncPSb0-WgWADVRCBFg_SLXhNiOnV199zqA7JCE5Y71o8ZWAHe4CBfjkysQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🟥
فاکس نیوز:
🇶🇦
نخست‌وزیر قطر در حالی وارد تهران می‌شود که تلاش‌ها برای کاهش تنش‌ها در این مناقشه، با هشداری صریح از سوی رئیس‌جمهور ترامپ روبرو شده است:
ایالات متحده تا هر زمان که لازم باشد، به مبارزه ادامه خواهد داد.
تنش‌ها در تنگه هرمز همچنان بالاست؛ جایی که ایران اعلام کرده این آبراه حیاتی تا زمانی که واشنگتن خواسته‌هایش را نپذیرد، بسته خواهد ماند.
در همین حال، ایالات متحده با اعمال تحریم‌های بیشتر، فشار اقتصادی را تشدید می‌کند.
در داخل ایران، فشارها رو به افزایش است. صف‌های طولانی بنزین، تورم فزاینده و تضعیف ارزش پول ملی، مشکلات اقتصادی را تشدید کرده و نگرانی‌هایی را درباره احتمال شعله‌ور شدن دوباره اعتراضات برانگیخته است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70674" target="_blank">📅 19:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70673">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=A8RMRv5eMNIyg66aGPa8LGGZYmPUc2ZFiN11dtB5yWlr5WwMjUdCsiIqCRzQOFwVs1XuaLo0puvKjkHGhfEJpGmNsDJsAFAztjIsW8xChksSep4TFY0aQEj_H3xweHhkSRdCrQb3GQ99xkbGMm32UGkoQtgcDLlWYt7iaoGMhq6V8ycmQgl4SDxcDQLOelnKvYmwdVLp0T9CNV4MLtSHTykNGxpY4EyMAzRYDDYA40UpSyiRSW4qkTUhKBouRfwKB4uDuoUB3Qg1vNrdJ0cIE_HUKvO0uDxs5ynv3IiQBi36ekCzJE1fl13J2qoOUi9xBqTnei0gLHD5T9f4RCXIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50aa1684a3.mp4?token=A8RMRv5eMNIyg66aGPa8LGGZYmPUc2ZFiN11dtB5yWlr5WwMjUdCsiIqCRzQOFwVs1XuaLo0puvKjkHGhfEJpGmNsDJsAFAztjIsW8xChksSep4TFY0aQEj_H3xweHhkSRdCrQb3GQ99xkbGMm32UGkoQtgcDLlWYt7iaoGMhq6V8ycmQgl4SDxcDQLOelnKvYmwdVLp0T9CNV4MLtSHTykNGxpY4EyMAzRYDDYA40UpSyiRSW4qkTUhKBouRfwKB4uDuoUB3Qg1vNrdJ0cIE_HUKvO0uDxs5ynv3IiQBi36ekCzJE1fl13J2qoOUi9xBqTnei0gLHD5T9f4RCXIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇱
فیلم از منطقه صنعتی بین کفر رمان و نبطیه الفوقا در جنوب لبنان پس از یک بمباران هوایی اسرائیلی.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70673" target="_blank">📅 19:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70672">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHUf-UGTYythln1xXRRsJm2jhny-NqK_wkDxyUKUuik6-h_RiPWYfcoDVz2rv6qWbO-6VgYWtV97AF6PlAdjnSLYRJuGOj8i7go7Xjw9c8XPp_yCSb0dIsqeIAjr51DsQDbe1LAZCuAJt86aB9zdehFFH23sjwLlDURJAxzeP37l-FtTlyeBVhn8bYSeOo-Nuv6fg6ouAdhfi1l4-Tf03eX1X74tYQm7cRAAA6mVhBYw9-qAFAeHF_0-WUDtP10fTnoN6QnbHV4tC3YcxPYgwrvz499fh4vGWfuqda9aTe6JzUPStVXL-fwcsgj8pCNx7x7Aodi2oL9uVXp5RTZHag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
〰️
بِسِنت وزیر خزانه‌داری آمریکا:
در حالی که مردم ایران برای تأمین نیازهای اولیه خود با دشواری دست‌به‌گریبان‌اند، رژیم فاسد همچنان مبالغ هنگفتی را در خارج از کشور هدر می‌دهد.
این رژیم باید به‌جای سرازیر کردن میلیاردها دلار به سوی نیروهای نیابتی تروریست خود، آن پول را صرف مردم خویش کند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70672" target="_blank">📅 18:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70671">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=QCVaG3MI-tlGwL3sEbhhFtsOSP2NL7kYlAzrMs05o0ImQZYE1p9O7XrU3X6FFP40x2qANVghQqwvCoST6W8jv1--9Rc0pD2WaaP247YY0MV-RaWVVvMDKsPEBjZngK6kfpuyZ5_q-5KcM5V3Ar4B1quqQBMZcJTIu-TztrXCxjHVgxjpmyKqIi_Zne95UW02CTEhAJxQRtOPYRY7_WreWrxP1zi_RmVONND_z-he-qMWU_PC7FMZZ_x0mR-hESVZHr4Kmv6TYzvGWSoW-Ic8TSjj-fSnp_BuAGXKzCHikRkYGB8Mcxi2_ffWkzzKgrvGht8tioawIoFeZYVyOD8dBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2ea391dbe.mp4?token=QCVaG3MI-tlGwL3sEbhhFtsOSP2NL7kYlAzrMs05o0ImQZYE1p9O7XrU3X6FFP40x2qANVghQqwvCoST6W8jv1--9Rc0pD2WaaP247YY0MV-RaWVVvMDKsPEBjZngK6kfpuyZ5_q-5KcM5V3Ar4B1quqQBMZcJTIu-TztrXCxjHVgxjpmyKqIi_Zne95UW02CTEhAJxQRtOPYRY7_WreWrxP1zi_RmVONND_z-he-qMWU_PC7FMZZ_x0mR-hESVZHr4Kmv6TYzvGWSoW-Ic8TSjj-fSnp_BuAGXKzCHikRkYGB8Mcxi2_ffWkzzKgrvGht8tioawIoFeZYVyOD8dBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
کارولین لیویت سخنگوی کاخ سفید:
در حال حاضر هیچ‌گونه مذاکره‌ای با ایران در جریان نیست.
این وضعیت تا زمانی ادامه خواهد یافت که ترامپ احساس کند آن‌ها ممکن است به شیوه‌ای معنادار پای میز مذاکره بیایند.
ما هنوز چنین چیزی را مشاهده نکرده‌ایم.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70671" target="_blank">📅 17:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70670">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=UEfHslhE6AH9nTrx3BmCVyHU5A-pXLLeiRS1tlm1w7YszdeUR6LCfk9hzS7s6sfF0wY5R3MgodvKlq58tSKFTFjx47koNwD60UxtrkcheHRQCefUyO2-Wl1QOTd7--Hrm4CpSZXSHCj1jZq3ZLWcCitbkqJeLVf18BNPt--wlwNhmuUNzq18C75fdKLKm63Ukf8hVJIVjWbmu34MqqO-8C40Dm9yngv4If7t4zXKuXVCcWZnK5s2q1uCSN40HhRXeIMt6ZIy3GdLSY6prumBBr01OLg92eP4Eu-0syBYhcvNSSZhLWUU7hG7knydufDQvuSSpWUfg28bCIN4yX69EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14b224b2a9.mp4?token=UEfHslhE6AH9nTrx3BmCVyHU5A-pXLLeiRS1tlm1w7YszdeUR6LCfk9hzS7s6sfF0wY5R3MgodvKlq58tSKFTFjx47koNwD60UxtrkcheHRQCefUyO2-Wl1QOTd7--Hrm4CpSZXSHCj1jZq3ZLWcCitbkqJeLVf18BNPt--wlwNhmuUNzq18C75fdKLKm63Ukf8hVJIVjWbmu34MqqO-8C40Dm9yngv4If7t4zXKuXVCcWZnK5s2q1uCSN40HhRXeIMt6ZIy3GdLSY6prumBBr01OLg92eP4Eu-0syBYhcvNSSZhLWUU7hG7knydufDQvuSSpWUfg28bCIN4yX69EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
محسن نامجو بعد از ۲۰ سال به ایران بازگشت!
می‌خواهم در این مقطع از زندگی، در وطن، در کنار خانواده و دوستانم باشم و این موضوع برایم از فعالیت موسیقی مهم‌تر است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70670" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70669">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded frommydiplom.ir</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9LfVuWY_3QUK3yiDYs5f7Iav06s8K72pVr8Fz4GOdev72YveJmnNaiesImpVO4_BKVJxCPMnu1VEj7243eUEdezt4YLdN6nuONJcCfSQlH1tnyeFxNNeEduDXx5yG5Y8rLIeEPj7E_zUbRCfa8oygQ7GfEyBt1PRWJOjvVK69DWTY78jKDinjD9nX1B6fx2frclgVjR5rYpQuaWzB5QGDCZI-uoI0vgQZeTATNE1tTmBG8q6o2ymIQbQxVxqRFyreRzsOfnLHO7s3ysr5mf8xhFXS7sIRUXeEvNq8X01bo3Bh9oF-rSQXjRQ7zPU6LP4OvCNhrWYgjqZWQNjAQTGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👮‍♂️
مد
ا
رک رسمی تحصیلی «مقاطع متوسطه و عالی»!
✔️
از دیپلم تا دکتری | کاملاً غیرحضوری
✔️
قابل استعلام قانونی
+
قابل ترجمه رسمی
✔️
مناسب برای
:
مهاجرت
|
استخدام
|
ادامه‌ی تحصیل
ارتباط با مشاور
:
https://t.me/mydiplom_support
ورود به کانال :
https://t.me/+lHweVa-y92IyZDA0</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70669" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70668">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=F_qpEUmUyCFvjAwaBj7RwVKdpXs5fzdKyX6UaD1jG02IK9Getfl4BeY7R8n__EdxuVncOvMzigJDAhxBOUYxPH25zHQCA4NqgKRh7BDPCbLC3TT_OERCethyCWxDabQHMTMG7vMcyFdPSRuVHlLXSR0tG2atAgMYf--o0b01q-KuuxXT_tQLJ1_b0o3tPH4vFCZcB4lJKIBxkiKlgKoYkYgfGhGYSajsRLpBgzPKkPt3WG5UjuBvkyA65w-aompGrJ8WzVuyEL3tsIgVrjoL3Ru_K9rF7MoQmH8eYRHauxAcm0BqUolrOtHp4I3AULPtJHemv0_Ek7Oppv3g7SD8jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bacd124f0.mp4?token=F_qpEUmUyCFvjAwaBj7RwVKdpXs5fzdKyX6UaD1jG02IK9Getfl4BeY7R8n__EdxuVncOvMzigJDAhxBOUYxPH25zHQCA4NqgKRh7BDPCbLC3TT_OERCethyCWxDabQHMTMG7vMcyFdPSRuVHlLXSR0tG2atAgMYf--o0b01q-KuuxXT_tQLJ1_b0o3tPH4vFCZcB4lJKIBxkiKlgKoYkYgfGhGYSajsRLpBgzPKkPt3WG5UjuBvkyA65w-aompGrJ8WzVuyEL3tsIgVrjoL3Ru_K9rF7MoQmH8eYRHauxAcm0BqUolrOtHp4I3AULPtJHemv0_Ek7Oppv3g7SD8jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
بازرسی امنیتی در مراسمی که تحت کنترل حوثی‌ها در یمن برگزار می‌شود.
آن‌ها به دنبال کمربندهای انتحاری و مواد منفجره هستند.
همراه داشتن سلاح‌های شخصی مانند تفنگ‌های تهاجمی و خنجر برای مردان یمنی امری عادی‌ست
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70668" target="_blank">📅 17:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70667">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe281d624.mp4?token=lqN8sNjLqnhdqZko1pP3fR2vhDy5VtxLzxg21e2MurHCAXiU-B4NeGw0R13xvqSj-wHmROsLS2xFRxnquPqqppxXwSTjh85bP63urLYPnYSWx3TI-t2Q2HNx89q4RKsC2-SgBYsbbFFCVrBpWUZCwOmNbyP8RXEijSnSRp08IJAnQSjQGTLfI_6fmGe-TTyd2em9KNSWw6Xa0_aQcltyHXIqxN1ezwaQ6oWB2Fy5lWJhCSA9YUvQ14rQRfGZiqHI8IBx3d4IBZD_XFjJD28MEvIDnSyr6Q9CDnKOPOkSL6qSIhFIFh1e6xJbsD8nP50QjCQwX0QVl6vaY8Evhkug-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe281d624.mp4?token=lqN8sNjLqnhdqZko1pP3fR2vhDy5VtxLzxg21e2MurHCAXiU-B4NeGw0R13xvqSj-wHmROsLS2xFRxnquPqqppxXwSTjh85bP63urLYPnYSWx3TI-t2Q2HNx89q4RKsC2-SgBYsbbFFCVrBpWUZCwOmNbyP8RXEijSnSRp08IJAnQSjQGTLfI_6fmGe-TTyd2em9KNSWw6Xa0_aQcltyHXIqxN1ezwaQ6oWB2Fy5lWJhCSA9YUvQ14rQRfGZiqHI8IBx3d4IBZD_XFjJD28MEvIDnSyr6Q9CDnKOPOkSL6qSIhFIFh1e6xJbsD8nP50QjCQwX0QVl6vaY8Evhkug-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
خنده‌‌های علی مدنی‌زاده، وزیر اقتصاد در واکنش به فشار گرانی‌ها بر مردم
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70667" target="_blank">📅 16:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70666">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=V9PkS0zmvn5EOfUz8N5llnhB-jjyFMrhpIcrioRXo72Y9o6mVxwXpzYFf_tNbAj0G1cCskYfHcS8yO98IzgbC-9yNjnyYfiGx4PtArXHeHnhXTnbUau-hj6nYaIMGnxRaPXfBa-YaEd4J7H701lTV0mcnYnKbLBRKZgvs3EAC0BvXIS9hS1VLutNI02QrUuJjKyQt0XCj4xsvoJrQZsmvddqP5q17QktlzBh0uFWO4vcOWeWdcNKXW1eFWQNpTJLFKz0xUUPQtrgjGNqRvm4iBBLBngvaAivLwf4bM3My_qzMtIUhg3I-69xOstPW5WdEm8Q58C0kKNy7PdetpOmZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc123970b7.mp4?token=V9PkS0zmvn5EOfUz8N5llnhB-jjyFMrhpIcrioRXo72Y9o6mVxwXpzYFf_tNbAj0G1cCskYfHcS8yO98IzgbC-9yNjnyYfiGx4PtArXHeHnhXTnbUau-hj6nYaIMGnxRaPXfBa-YaEd4J7H701lTV0mcnYnKbLBRKZgvs3EAC0BvXIS9hS1VLutNI02QrUuJjKyQt0XCj4xsvoJrQZsmvddqP5q17QktlzBh0uFWO4vcOWeWdcNKXW1eFWQNpTJLFKz0xUUPQtrgjGNqRvm4iBBLBngvaAivLwf4bM3My_qzMtIUhg3I-69xOstPW5WdEm8Q58C0kKNy7PdetpOmZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیو وایرال شده از یک طرفدار حکومت :
قیمت دلار همینطوری میره بالا و ارزش پول ما همینطوری میاد پایین
ولی این میتونه به نفع ما باشه چون برای اون خارجی محصولات ما میتونه ارزون تر حساب بشه و بیشتر تحریک بشه تا کالای ایرانی خرید کنه
این یعنی فروش بیشتر بیکاری کمتر و چه بسا درنهایت مهار تورم و توسعه اقتصادی!!
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/70666" target="_blank">📅 16:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70665">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfy--TkM2zG-_QXdvBiSeF1HK4ieY7ccu7QAArQm-otHrVLhc8XBM4ILX9fqmaFULN5Ukn7F-zacqQUSZmJ2QVq0Iw1-w13vWLuhTOExJu7qkthdk1w8XcWfhtVW0g1PkAUfEvSFLdNgxkut7Sx_tC8RnoKUtwbDp32RN55grVNHQlyQhGxWTSgNtwMRTA_3RJm-YKUCjmQRr0KJHFdK9hRerXZOlGF29PYBcJsHuDt9caiOPrsKaoijHTSFS1mIoiuLM7kVzoY-BFYpTYiRM6m3q0cFmrmKvzkCuv9I5ROenI-qH91BZFFsYgVLgnx9kjQEAspXHpZK6tcQd0zZfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
〰️
📰
سی‌ان‌ان:ناو هواپیمابر USS Theodore Roosevelt همراه با حدود ۵۰۰۰ نفر قرار است در هفته‌های آینده به خاورمیانه اعزام شود.
این استقرار حداقل ۷ ماه پیش‌بینی شده است.
جان پریمن، Master Chief Petty Officer نیروی دریایی آمریکا، گفته خدمه می‌دانند مأموریت بیشتر از هفت ماه خواهد بود و فرماندهی به آنها گفته برای ۸ ماه برنامه‌ریزی کنند.
این اعزام را در ارتباط با فشار عملیاتی ناشی از استقرار طولانی USS Abraham Lincoln قرار داده؛
لینکلن بیش از ۲۵۰ روز در دریا بوده است
.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70665" target="_blank">📅 15:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70664">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=FTatyPJchKKC9eiE-vDxKV-tBZXjlgH4I5FkvzcdIHZj7QnKSxqfrHT6HcBYPMW9tVSPxiS3ssE6Tq6W7s5e9bh8PX7AaeHUyl2nHZGWC9_2JhdzYD0DuN8v7W56MSiQ34-Yoiwie0iFtrzcpFsBgcEG86hpsMN2cU8-ajqEAJpTEf7pTRqv0V33EHiK_PxJ2IAnA9W9jRilWDZASCHiW91uQGzpftfjRTK_2LY-I0urF0WIXn63bpnDgVyu01g2rXl26in0_DmYoRVhNHlbbKFOKxHgo6vPXfNulePPObG5YX00sO7nRDQd1eu_BB6tIMCyCYVo_CI2ysP2dA-jeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efaaeae9eb.mp4?token=FTatyPJchKKC9eiE-vDxKV-tBZXjlgH4I5FkvzcdIHZj7QnKSxqfrHT6HcBYPMW9tVSPxiS3ssE6Tq6W7s5e9bh8PX7AaeHUyl2nHZGWC9_2JhdzYD0DuN8v7W56MSiQ34-Yoiwie0iFtrzcpFsBgcEG86hpsMN2cU8-ajqEAJpTEf7pTRqv0V33EHiK_PxJ2IAnA9W9jRilWDZASCHiW91uQGzpftfjRTK_2LY-I0urF0WIXn63bpnDgVyu01g2rXl26in0_DmYoRVhNHlbbKFOKxHgo6vPXfNulePPObG5YX00sO7nRDQd1eu_BB6tIMCyCYVo_CI2ysP2dA-jeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سیزدهمین فرزند مادر ۳۳ ساله بدنیا اومد
؛
از مرده میپرسن چرا این همه بچه حالا جوابش:
اساسا بچه ها رو دوس دارم من ، هزینه هاش؟؟ هزینه هاش با خدا
😳
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70664" target="_blank">📅 15:01 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70663">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=bxDf5ns0dUTjqpEDF8yH9aqWuDFlKcxPokQj4wXy5ePhFyuvX-Vst3tuOZ3E6dC4dj66HU_td2i_P-VDUggnPzPal47HWjN2tVJSkf7HMQu75wwAbc7eBgvp_K0Nvc-ct2psQI7MMTDtK5FnAvdBm2Ziv3eBQfHcurpRIdNvxLHfUf8jORqfxDlYOnTeosCKQOgMfuWK67aL0zaMQHDvuAoP-WlYrksx4tujzV-EhgvpRPL2KuPVWz8WBQQ0In9voIjGXsEdePuw7cIsPpcZeoKKb9xG-wlkAEJEinrla67oey6wi-MZ_0EbAuytPqdJh5TW1bfNI5fMaehRyFmGsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25e2d9d80b.mp4?token=bxDf5ns0dUTjqpEDF8yH9aqWuDFlKcxPokQj4wXy5ePhFyuvX-Vst3tuOZ3E6dC4dj66HU_td2i_P-VDUggnPzPal47HWjN2tVJSkf7HMQu75wwAbc7eBgvp_K0Nvc-ct2psQI7MMTDtK5FnAvdBm2Ziv3eBQfHcurpRIdNvxLHfUf8jORqfxDlYOnTeosCKQOgMfuWK67aL0zaMQHDvuAoP-WlYrksx4tujzV-EhgvpRPL2KuPVWz8WBQQ0In9voIjGXsEdePuw7cIsPpcZeoKKb9xG-wlkAEJEinrla67oey6wi-MZ_0EbAuytPqdJh5TW1bfNI5fMaehRyFmGsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند شب پیش یه دختره اومد از خودش ویدیو تولد بگیره تنهایی که یهو یه 207 اومد کنارش و سه تا پسر اومدن وسط رقصیدن و تولدش براش جشن گرفتن
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70663" target="_blank">📅 14:35 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70659">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMhE-JjZMWQheHieRyGt-9b_P85jB4LLw_EbjsQ1x40D2q04Yjev5M3WcXkpYjPf5rfGrj857hELI11emR5sRybkdIJE9fcWVnuPcbjUp5XL3bFWp_tmKx1avSOwE2olXQOuH_ARLp8yCzV4AgCFoCXHoTakznOHvepWra_lB43rAIFM8nx_g0D9nWaeNerPZJWyEVn0xA14xYMysFvQJiE-5qkFPmwfiECxBhI4EAaYZ-hDm7WIo9AWkuKAUfnIacc2wbEPxfuW1YILY1DiuHPifMcNaRui2lFDw_fZjgJil4c_TTUg3oqCSem0XbQr8tvg1P52VJRcyQ7iUDPBjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XQnhX_bu1XkSw06jJLVDsEzKB4NwTuaQRC2OK5B-kBIkWZ92Q-9ey07vRbXjhLkezyZWHobtpBhhy0G5_vSdYqNpWr9I0O3ffHTT1wK8HXBFXZR86fVnYXxgcLRk4P0zYL6b1stngRJ-znwejZh4aoj0DOOv0iOwktTmJxhiKfaWzntKs7F5YBeDiYdAxQqau0jqiEHhPsDpfxz6PwAV-7I_kx7QTgTE7eINYskcqluMAGdgWsJ-YZAPk5TS-gOi5BXmzqOZ3dW3luKbpT5suRkI1-z2FEl-DnPMcoEudfAzyv6POZKOR-oETiuefWGejEV6ZDHHktj-kTkN307WnA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=ZS87nxTAAiyKStXHxP_CjGFOe_GNf4abrhMelXxDHLNA4qG74J0_VFAvKQgpW6UqcyG2UpxtejsYxRfFp8paSzoFywkVxRM-vLiym_AnpmB0z_7N-q4Mid19KcknspaOqKjCIpeV1ZJ-a7LZRc1OnmwTXjsF82kUDMCD9QsPrDVz6ODg_MKgAXbo5srubIqQKd6y2Eg0c-qY8CNFKljXoZl_bt7axX63GCuqNdHFaOP7XvOsm6On8DcB9UcOtk1Q8oaRiZQpwHfa1RB-3Hvn9jKy38pcxgFJVSPwEU0FKgFE_KonPUxG1rKsvHDkpwr-14WSWTOxTZbysuprLNdm-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaeab0414.mp4?token=ZS87nxTAAiyKStXHxP_CjGFOe_GNf4abrhMelXxDHLNA4qG74J0_VFAvKQgpW6UqcyG2UpxtejsYxRfFp8paSzoFywkVxRM-vLiym_AnpmB0z_7N-q4Mid19KcknspaOqKjCIpeV1ZJ-a7LZRc1OnmwTXjsF82kUDMCD9QsPrDVz6ODg_MKgAXbo5srubIqQKd6y2Eg0c-qY8CNFKljXoZl_bt7axX63GCuqNdHFaOP7XvOsm6On8DcB9UcOtk1Q8oaRiZQpwHfa1RB-3Hvn9jKy38pcxgFJVSPwEU0FKgFE_KonPUxG1rKsvHDkpwr-14WSWTOxTZbysuprLNdm-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
ایرج مصداقی از نزدیکان شاهزاده رضا پهلوی در یک مصاحبه درباره علی کریمی صحبت کرد؛
صفحه اینستاگرام کریمی در اختیار شخصی به نام امید دانا است.
بعد از انتشار این صحبت‌ها، کریمی در چند استوری به‌شدت واکنش نشان داد، از مصداقی خواست ادعایش را ثابت کند و شاهزاده رضا پهلوی رو مخاطب قرار داد و برای اظهارنظر درباره این موضوع ۲۴ ساعت مهلت تعیین کرد.
⏺
مجدد مصداقی در ویدئویی جداگانه به واکنش‌های کریمی پاسخ داد و اونو مخاطب قرار داد؛
علی کریمی یک آدم ابله بی شعوره که سوابق ننگینی داره و توی فوتبالم هر تیمی رفت اون تیم رو بهم ریخت. هیچ سابقه مبارزاتی هم نداره
حالا اومده ما رو تهدید میکنه. آخه مردک تو عددی هستی شاهزاده رو تهدید میکنی؟! چه غلطی میکنی مثلا؟! داریوش که میبینی که بلایی سرش اومده تو انگشت کوچیکه اونم نیستی.
بهش گفتن جهان پهلوان باورش شده. اخه مردک کسی که دوتا لگد به توپ زده پهلوونه؟! همین مونده بود تو برای ما شاخ بشی. فکر میکنه چون فوتبالش خوب بوده سیاستم میفهمه. ما اصلا تو رو حساب نمیکنیم ابله.
اینا رو ارزش دادنی فکر میکنن خیلی بالا هستن آقای کریمی با تو یا بی تو فرقی نمیکنه زیاد حرف بزنی صداتو میبرن
⏺
علی کریمی هم در ادامه اومده گفته؛
از اين لحظه به بعد؛
از هيچ شخص يا حزب سياسى حمايت نميكنم.
در حد توانم به مبارزه‌ام عليه رژيم اشغالگر شيعه ادامه خواهم داد.
این تصمیم من به منزله سنگ اندازی در راه مبارزه دیگر افراد با رژیم اشغالگر آخوندی نیست.
به اميد آزادى ايران و مردم نازنينش
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70659" target="_blank">📅 13:47 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70658">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGH_1AGQSzH7CB7QgEB37Blt2oGf6pFVkwWZgM3Ay7Xup2UX7XeCkFhA_lb6piyipgh-n_rfpscEgTkkadP8mdi0gPN_pDi6Ip4175xbHKN1cODw89NqHb68rs96o-uRe_CA22l0dwarjQMfSKpgnEe_NmwPVO_dLLKxlgkiIs69yzmmW9AaOgNN6HwiVFu4dTypKsY-LmHna6MIOwlhn0ugFWxP1E9s1Pdq1g5zTrkBMxIp8bG5axGULCRJkE6HUrwCuvdKiZDqmJklGfPLRI1KoJZ7Y8wMqiOgwXD9ZO1QMVGhc9B2-JQrwxxqR_f4YTFlcWebh766AE4IScaFWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
📰
وال استریت ژورنال:جان رتکلیف، رئیس سیا، این هفته در سفری غیرمنتظره به مسکو رفت تا به روسیه هشدار دهد که به کشورهای عضو ناتو حمله نکند.
این سفر در پی ارزیابی‌های اطلاعاتی جدید آمریکا انجام شد؛ ارزیابی‌هایی که حاکی از آن است که پوتین ممکن است در سال‌های پیش‌رو، با انجام حمله‌ای محدود به یکی از کشورهای متحد، عزم و اراده ناتو را محک بزند.
مقامات آمریکایی نگران سناریوهای مختلفی هستند؛ از حملات سایبری گرفته تا تهاجم زمینی در مقیاس کوچک که به احتمال زیاد یکی از کشورهای حوزه بالتیک را هدف قرار خواهد داد.
آن‌ها همچنین نگران آن هستند که کاهش ذخایر تسلیحاتی غرب — که ناشی از سال‌ها حمایت از اوکراین و درگیری‌های اخیر مرتبط با ایران است — بتواند بر محاسبات مسکو تأثیر بگذارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70658" target="_blank">📅 13:15 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70657">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=OUeNJUTfjd2WNO0C-TwOr-xe4DnmUbrx2O8n9mkJW_jEo4iXjitkm5zKaLbpjkVi9Zjr3CMubLYNHgT81vaH2-aNCvoEigNgA36l2QVQ6XJOXyjelJzMGTL3bxO8PIpxilVlhzG3_inAUKtxxYcSCGoKoxevDKbwxZ7m9M5ZClum8Dp8F5WJjJX2TPPdvD31Qy9z3ex5YuqelwI-8kpHap0XB16u4kEx3wxV0qiaQQnrK6hPlWzKsKMrp3LWA0NOwh50nWh2g9FIUPLN9ych7SwJ0WHJA9wyIRy1Lt1KP4NM9JePyeJi0L8G7v5wenbUqfm598z8R8kOsrxwP37uSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/c5ef938e2e.mp4?token=OUeNJUTfjd2WNO0C-TwOr-xe4DnmUbrx2O8n9mkJW_jEo4iXjitkm5zKaLbpjkVi9Zjr3CMubLYNHgT81vaH2-aNCvoEigNgA36l2QVQ6XJOXyjelJzMGTL3bxO8PIpxilVlhzG3_inAUKtxxYcSCGoKoxevDKbwxZ7m9M5ZClum8Dp8F5WJjJX2TPPdvD31Qy9z3ex5YuqelwI-8kpHap0XB16u4kEx3wxV0qiaQQnrK6hPlWzKsKMrp3LWA0NOwh50nWh2g9FIUPLN9ych7SwJ0WHJA9wyIRy1Lt1KP4NM9JePyeJi0L8G7v5wenbUqfm598z8R8kOsrxwP37uSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
از خونواده‌ها میپرسن چقدر خرج کنکور کردین برای بچه‌تون؟ رقما به شدت عجیب غریبه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/70657" target="_blank">📅 12:32 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70656">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaGPIGH3zdXTPvWRSGYosZDnhwBTeKLAwvxY7Jhl0-LDKvII7nrBkPt0bUZIUctlzIBRJqJa-wwelXYcGLWZgCmiM49CUQHMWUQqqeioScoVd525P_-MU4BMEJOZULpoS0pAl-faD7tkBpUXcDPfiZ_SsrMmGnUw4ylhnBKhTeUPQVUw6NHLs_UIrZT7y_pubREphwkLRksSFlO5ZXRl5WtxXQudsbxTPhNGlZui7R5XV2kMTSPZK8JD26GLqwuOX8oMFDcPfB3BX2kCJ4BM448uqt89Skmld862wyyVoSKOjYfHFAqC3IiWNZfPCnG883y7BJLUFMDyGZGS0efAkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی دریافت کردیم مبنی بر اینکه یک نفتکش در تنگه هرمز هدف اصابت یک پرتابه قرار گرفته و در پی آن دچار آتش‌سوزی شده است.
آتش‌سوزی در نفتکش در تنگه هرمز مهار شده و تمامی اعضای خدمه در سلامت هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70656" target="_blank">📅 11:59 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70655">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=PvzbC0EVZhahz9LXePByIoQ8QjB9aF-WsAeOWAeNUv7YH76C8NOzfOhftb6iXasbzh-kC8EXoaFhSUwEv0GaXat_WErfyX6wPQcZ4nrG_Q7kitI-3lcgjewADy7jwxVcmq2Dsx-bWPg3JfRBcDjpBtj3apThGJiR4ap6k_PIAV-ooBmU551xWnupETzI7f9CuZYAM7fK32cmea7-m67hyBy0daCAg4bueEAUVzFkuOeEf0h2PPNDLtGil6pBDhdCnmty_QHpxzG2gqUXJT8YJl_1BXN_P-k6l1GsDjcWGC7k3O9e6DYW1vnNhjQJgnrbPQFUh9Ub3a-_th_i2zvB4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fee8faf9e.mp4?token=PvzbC0EVZhahz9LXePByIoQ8QjB9aF-WsAeOWAeNUv7YH76C8NOzfOhftb6iXasbzh-kC8EXoaFhSUwEv0GaXat_WErfyX6wPQcZ4nrG_Q7kitI-3lcgjewADy7jwxVcmq2Dsx-bWPg3JfRBcDjpBtj3apThGJiR4ap6k_PIAV-ooBmU551xWnupETzI7f9CuZYAM7fK32cmea7-m67hyBy0daCAg4bueEAUVzFkuOeEf0h2PPNDLtGil6pBDhdCnmty_QHpxzG2gqUXJT8YJl_1BXN_P-k6l1GsDjcWGC7k3O9e6DYW1vnNhjQJgnrbPQFUh9Ub3a-_th_i2zvB4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇴🇲
🇺🇸
کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، درباره دلیل و نتیجه نهایی مذاکرات عمانی-ایرانی:
ما گفت‌وگوها را با عمانی‌ها آغاز کردیم تا بتوانیم به آن‌ها بگوییم که حداقل در روحیه همسایگی، این اقدام برای باز کردن مسیر جنوبی می‌تواند یک‌بار دیگر تنش‌ها را ایجاد کند، فرآیند اجرای توافقنامه‌های اسلام‌آباد را مختل کند و حتی منجر به شعله‌ور شدن درگیری‌های نظامی در منطقه شود.
​
انتظار ما این بود که با کمک دوستان عمانی‌مان، شاید بتوانیم این مسیر را ببندیم. با این حال، فشار آمریکایی آنقدر شدید بود که متأسفانه این مسیر جنوبی بسته نشد.
​
سپس آنچه رخ داد را دیدیم: جمهوری اسلامی ایران تصمیم به بستن تنگه هرمز گرفت و در ادامه، شاهد درگیری‌های نظامی بودیم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70655" target="_blank">📅 11:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70654">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=Z5vpdLsOrMDcJtertB-Mdft3rAB-qCdVK2u_nxsXCnL1UtgSe74TeyfVU00hLPOk8NMphL9GEA-Jg-78lEUCPcA7kM7K1oCmtppxpRjdNeXFG6M70wZuYW0jIHWUMZp8MovT2uWsAIK0aegKJlwThmFV4vuEAtae8nWANmuH-7E8RYwDfqkItIr2bjOpvevc77PcESmsO4cVXuqGHQQB0J8fBz9bc3oXtvVVPhMYw49cybBjXqWVM3cnGNm3GO_9UiTdNsY8UWFurbpnBI45TNjp_m6Kjxi_XXut34c5YEKWoSEvcJCnmV05kC7d9Iuwaof_QvScRY2NWd4noi8n9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e7b3da01db.mp4?token=Z5vpdLsOrMDcJtertB-Mdft3rAB-qCdVK2u_nxsXCnL1UtgSe74TeyfVU00hLPOk8NMphL9GEA-Jg-78lEUCPcA7kM7K1oCmtppxpRjdNeXFG6M70wZuYW0jIHWUMZp8MovT2uWsAIK0aegKJlwThmFV4vuEAtae8nWANmuH-7E8RYwDfqkItIr2bjOpvevc77PcESmsO4cVXuqGHQQB0J8fBz9bc3oXtvVVPhMYw49cybBjXqWVM3cnGNm3GO_9UiTdNsY8UWFurbpnBI45TNjp_m6Kjxi_XXut34c5YEKWoSEvcJCnmV05kC7d9Iuwaof_QvScRY2NWd4noi8n9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعارهای عجیب حامیان حکومت در تجمعات شبانه:
دلار شده 200 تومن همتی
یه کاری کن میگن تو بیغیرتی
حیف که نمیشه بکنیم به تو بی احترامی
ریاست محترم جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70654" target="_blank">📅 11:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70653">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45450621ea.mp4?token=f8okifWfevCoaqg8b7EoXMtrQGttYTetSQpQTyxg-4fxe6lusnIRj2HsnYmCM7XBaSpB6oqPBIS8mpKDXsDZ9MXI1t59iygmjd6dX4RM5QP2tPNNv8tn1F4sN3bSHsPoeucpkkrnPGAsOkp8Z7txCVlfnPc7tbNwSwvj-1QgNfmne5L27B1e63CiUE8IeO29FSahTBP-w-zsn1ahfLw7dlJ4ghDgf4Rz1a15ydpbX7r97qm0PxTyD5dRBerSc6SpYihVs0q2QSzX8HMnP58cAIzObvRHJ7BJ0VKYg81YPvRtL4WBpePoxD5x8n8RpZRLG4T2Fz4mb_XKZbI61Yv7xjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45450621ea.mp4?token=f8okifWfevCoaqg8b7EoXMtrQGttYTetSQpQTyxg-4fxe6lusnIRj2HsnYmCM7XBaSpB6oqPBIS8mpKDXsDZ9MXI1t59iygmjd6dX4RM5QP2tPNNv8tn1F4sN3bSHsPoeucpkkrnPGAsOkp8Z7txCVlfnPc7tbNwSwvj-1QgNfmne5L27B1e63CiUE8IeO29FSahTBP-w-zsn1ahfLw7dlJ4ghDgf4Rz1a15ydpbX7r97qm0PxTyD5dRBerSc6SpYihVs0q2QSzX8HMnP58cAIzObvRHJ7BJ0VKYg81YPvRtL4WBpePoxD5x8n8RpZRLG4T2Fz4mb_XKZbI61Yv7xjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
سخنان جالب امیرعباس هویدا و آمار ارائه شده توسط وی درباره وضعیت ایران در آن زمان .
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/70653" target="_blank">📅 10:34 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70652">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
اعترافات اندرو تیت (بوگاتیت چه رنگیه) و داداشش تریسان تیت :
اون زندگی فوق‌لاکچری که از ما تو فضای مجازی می‌دیدید، قرار نبوده واقعیت کامل زندگی‌مون باشه؛
ما داشتیم یه نقش بازی می‌کردیم، مدل کارمون اینه که هرچی محتوامون عجیب‌تر و اغراق‌آمیزتر باشه، بازدید و لایک بیشتری می‌گیره و در نهایت پول بیشتری درمیاریم.
اون بوگاتی‌ها و استون‌مارتین‌های چند میلیون دلاری که تو ویدیوها می‌دیدید اجاره‌ای بودن و اون سوپرقایق تفریحی 50 میلیون دلاری هم مال ما نبود؛ برای تبلیغش پول گرفته بودیم.
حتی خیلی از حرف‌هایی که درباره ثروت عجیب‌وغریب یا داشتن چندین پاسپورت می‌زدیم، بخشی از همون شو و شخصیت اینترنتی‌مون بوده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70652" target="_blank">📅 10:04 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70651">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=FmBA7IVwo3oklaJQXgizxrJmserYiTW-U4Dq9DEihGRyI6urAMQN-v1I7yG3nFA89gAXr2hkFXIwERapNWmB3sabmVxqvumYCZ84sU_p0G9qzX-dCiPHWJSQcFA3fcwe30YJRGkptxl_yhhCclr5zZqa2Qj6sHiNH3iKtw2p684VCCTEIlOKT4PQzeqNndwWguzobH3vGWDMxc8VTUPC3TDVC6EynGSxjUYnVruyvtPWH0y2DEyqYtK6qGlaaMfBYKtuvTXVzqvn_aJaYK0vAJ4Ov17yod0i5gY3ERunlBwg0MHvP7c8iRtmQCHk2tAEdxfRTTrlJ1Mkj_a7X3GWRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630909b4ac.mp4?token=FmBA7IVwo3oklaJQXgizxrJmserYiTW-U4Dq9DEihGRyI6urAMQN-v1I7yG3nFA89gAXr2hkFXIwERapNWmB3sabmVxqvumYCZ84sU_p0G9qzX-dCiPHWJSQcFA3fcwe30YJRGkptxl_yhhCclr5zZqa2Qj6sHiNH3iKtw2p684VCCTEIlOKT4PQzeqNndwWguzobH3vGWDMxc8VTUPC3TDVC6EynGSxjUYnVruyvtPWH0y2DEyqYtK6qGlaaMfBYKtuvTXVzqvn_aJaYK0vAJ4Ov17yod0i5gY3ERunlBwg0MHvP7c8iRtmQCHk2tAEdxfRTTrlJ1Mkj_a7X3GWRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکنا گزارش داده یک فرد که بلاگر اینستاگرام هم بوده، عاشق ماشین‌های مدل بالا بوده و توی دیوار دنبال آگهی ماشین‌های گرون می‌گشته.
با صاحب ماشین قرار می‌ذاشته، می‌گفته یه دور تستش کنم و بعد با ماشین می‌رفته!
نکته عجیب ماجرا اینه که بعدش زنگ می‌زده و می‌گفته من دزد نیستم؛ چند روز با ماشینت دور دور می‌کنم و بعد سالم پسش میارم!
ظاهراً هدفش فقط لذت بردن از ماشین‌های مدل بالا بوده و بعد از چند روز هم ماشین رو سالم برمی‌گردونده!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70651" target="_blank">📅 09:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70650">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=PfH6G57ezWtJOlwhpkt5704WVduCIppBHXKZcU32zbFiBeSn4C_G-2HpexsDxhLg_evSJyt8UXXoU8iVfI5Euhmz4YmGnmYbafuEfIN51jA3Ph1rGsHSaqO_0HuGsCBSE95xx2RVPiAXMeloil1Ou0ozyAJ1a3X_WbNxahcA95SugxIAd64WpyQL7SaJ7jbC_u9VC_m51DnWkVskIrdRs69eKQH9GUZloJDA-akdohC8dVNK6FbiYE6H6_GrNmMl2efxIJ_IqgWIDdguSFPQ1-s8tod9Wg9cNR-zsobwUSrwFIurvC81h3rmk6l98LcmHhyCet0CfkGEX9VweI_cJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29a5f45322.mp4?token=PfH6G57ezWtJOlwhpkt5704WVduCIppBHXKZcU32zbFiBeSn4C_G-2HpexsDxhLg_evSJyt8UXXoU8iVfI5Euhmz4YmGnmYbafuEfIN51jA3Ph1rGsHSaqO_0HuGsCBSE95xx2RVPiAXMeloil1Ou0ozyAJ1a3X_WbNxahcA95SugxIAd64WpyQL7SaJ7jbC_u9VC_m51DnWkVskIrdRs69eKQH9GUZloJDA-akdohC8dVNK6FbiYE6H6_GrNmMl2efxIJ_IqgWIDdguSFPQ1-s8tod9Wg9cNR-zsobwUSrwFIurvC81h3rmk6l98LcmHhyCet0CfkGEX9VweI_cJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
یکی از زیباترین سخنرانی‌های محمدرضا شاه:
هیچوقت به زندگی فعلی خود قانع نباشیم و دنبال بهتر کردنش باشیم.
برای بهتر کردن شرایط زندگی، اولین شرط خونه و سقف بالاسر هست و بعدش قدرت خرید مردم.
محیطی که در آن زندگی میکنید باید شاد باشه، غذایی که میخورید لذیذ باشه و لباسی که می‌پوشید تمیز و لطیف باشه‌.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70650" target="_blank">📅 09:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70649">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70649" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70648">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=F_ZqvyBRPG1es3oUMwtB62o457fwn1yuk0IZe898Z70KEcvcNt2QFbusdxAWpBTKc5GFWEXk-9oY2gLzLssAlP03zLXeP8-okAjwtD0cvBdtIUK6tbaQC1leS80l26NI9HpI8CL2w03ssIbmTA2xHt8Av1PMhpw2guZDtZ37YrSnl1of1FAXrvdN8CryIY9PiMFJI5TV8NS1Yq_mRsK1FzSqEg0rR2rBGCb-a-cHWgDZjndsbXtpn8hJLZ9pNp-SFNxGVOmlNXEhr9ZzGkJ4rpYCytJTQEYqWMF6LmyuPnQ4uZrRbu6p-OMHDgK3ziH-7rWi3xozrvM9bikCYDRVHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=F_ZqvyBRPG1es3oUMwtB62o457fwn1yuk0IZe898Z70KEcvcNt2QFbusdxAWpBTKc5GFWEXk-9oY2gLzLssAlP03zLXeP8-okAjwtD0cvBdtIUK6tbaQC1leS80l26NI9HpI8CL2w03ssIbmTA2xHt8Av1PMhpw2guZDtZ37YrSnl1of1FAXrvdN8CryIY9PiMFJI5TV8NS1Yq_mRsK1FzSqEg0rR2rBGCb-a-cHWgDZjndsbXtpn8hJLZ9pNp-SFNxGVOmlNXEhr9ZzGkJ4rpYCytJTQEYqWMF6LmyuPnQ4uZrRbu6p-OMHDgK3ziH-7rWi3xozrvM9bikCYDRVHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a4
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70648" target="_blank">📅 02:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70645">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aff574e553.mp4?token=D68YqzOkCFEcyZ1tCNuo-Nd8G8EReWdoAzx6TYnRQv75HGNjYT8_n1EbhRd_VO08UkIll6JU67WV93W63LMVhOSCuOgehbREgRw_76_8I0rCeodKaXOadUM10x_PuYRBMxSYeGjnAQ4eRWvRLSSukM-59-JU0YpHxzj3mAHrWb3jH47ge3BFBBTHqEjbgx-sSMqbhff4tF0M-IfsJvr5x0lVV1dLTwwTJVLCTd8mK6mTaIiOHODdALxPlcrRYbov-QKAzcTVGgMHig8cUfADB0htilCZ5cgjg6PI-5NOE1fzo5yBAr9n1zC-iPcr4Yi9E8GkAD_DuQdBxXBTdZinpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aff574e553.mp4?token=D68YqzOkCFEcyZ1tCNuo-Nd8G8EReWdoAzx6TYnRQv75HGNjYT8_n1EbhRd_VO08UkIll6JU67WV93W63LMVhOSCuOgehbREgRw_76_8I0rCeodKaXOadUM10x_PuYRBMxSYeGjnAQ4eRWvRLSSukM-59-JU0YpHxzj3mAHrWb3jH47ge3BFBBTHqEjbgx-sSMqbhff4tF0M-IfsJvr5x0lVV1dLTwwTJVLCTd8mK6mTaIiOHODdALxPlcrRYbov-QKAzcTVGgMHig8cUfADB0htilCZ5cgjg6PI-5NOE1fzo5yBAr9n1zC-iPcr4Yi9E8GkAD_DuQdBxXBTdZinpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شهروندان اسپانیایی ساکن منطقه "سئوتا" به ساحل "ترامپولین" حمله کردند تا مهاجران را بیرون کنند و اقامتگاه‌های موقت آن‌ها را تخریب کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70645" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70644">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afGuagIOP2LDc-XTSHKVE9slW4FX0gVjk6ttQdoZGrxX_v7wjl6en-97shy4WCFsr1HynS4mA-qgp0es2i9h5FOCKJm9FXM_noPN7lEhcHyls2bYZPJD4BMIDu83JR8Hw8Rok1hLWxZGuCvd8VLSh-IgtThk0yDNCTOWMaBNH9rNgjYdyJGfidpDq_8OgY09abQflhwDzDCM3V_-NfhVrh0K0Dd5kEFSCb5Yl7xL606DRUuiUEmK0CvQVbj80dSnnoaWw-tMJoWh0HjsAUUSXI6X6iv1zR4ZH474HvLja8qHBLBtp4Pnf1Xqg-mS63JNTry6QX-m0-gtQfTalo1-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
آمریکا ناو «یو‌اس‌اس آبراهام لینکلن» را برای نمایش قدرت به منطقه اعزام کرد.
پس از ماه‌ها جنگ — و بیش از ۲۰۰ روز بدون حتی یک بار پهلو گرفتن در بندر — این ناو اکنون برای استراحت و تجدید قوای خدمه، راهی تایلند است.
مأموریت: نمایش قدرت.
مأموریت فعلی: نمایش تعطیلات.
«خسته‌ام، رئیس.»
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70644" target="_blank">📅 01:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70643">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3143921715.mp4?token=Jg5A1qSF9X0VqLRjNYh_zVfEGeQZkZagAaG_dTin8o4VqMjr6iZsN-QNd69p5-CSqsfyjJru0x_3QNLj5rhGo96ySSxObwFUO9m-HJ3UE9pNARoQzdKiDKtIql99B4y3ZIHpuoWlksrwwvzq_Q-SIQPLijZBxFMNB70nVtnHTu6rGpgmR5YV8a0IfislOVtTuzux-mqkYBwadJ07_lFQP0wcScs2I2N48IOGOhScZWeAnEd5NxDldP99fZ3j8qvgmHRGqy9JT0bOHq74MljR-2DAFFYjn9yKV9mJvwnEmr_o1kjPNGUPnxKhxKRf__rWVbZDx8CevRqrav09lPSD9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3143921715.mp4?token=Jg5A1qSF9X0VqLRjNYh_zVfEGeQZkZagAaG_dTin8o4VqMjr6iZsN-QNd69p5-CSqsfyjJru0x_3QNLj5rhGo96ySSxObwFUO9m-HJ3UE9pNARoQzdKiDKtIql99B4y3ZIHpuoWlksrwwvzq_Q-SIQPLijZBxFMNB70nVtnHTu6rGpgmR5YV8a0IfislOVtTuzux-mqkYBwadJ07_lFQP0wcScs2I2N48IOGOhScZWeAnEd5NxDldP99fZ3j8qvgmHRGqy9JT0bOHq74MljR-2DAFFYjn9yKV9mJvwnEmr_o1kjPNGUPnxKhxKRf__rWVbZDx8CevRqrav09lPSD9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
شکار شکارچی
اپراتور پهپادی روسیه توسط یک پهپاد FPV اوکراینی کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70643" target="_blank">📅 00:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70640">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7bVmKSfrtCZ4wUiLzJ3db2X_nYg7CcN86SWq8ZJf-0Zypeh5FNu5LvlI9i_BSu4BfFBwpIZGqvLW-nkwenbuaAeDQGCT3K8nQ42C6lUXsFS3pu20fiWlfpX2eDsSNIstZkLv9mLcxyweHPzCl34i1nc1IIy5--bODTvi-KQB9hFtA7L-H9tw3iKZh7MCpnGm6fHlYDFW0fa2MvNenXMpQXdWAkSA4deP6W3iNpCn6c-yYOLSznatk1VdxkcBXKDlRb386cylPGEAlcJdhz9SZHo0R3mfpSTh2ax91NnqZBnMzpey0Jqn_7bHDWCkIG9omN50uhiDpwWXbUh_DgHeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=RTcKoS8nV1OXXh5WpgofQdZJZ88faGiaOLb-b-RRROX9vxYHB8l3WzEDtfs7GmvO-An27NS99RHhpxDe9Xirf7vtsGHhVKycf9ppMBrNSgCRTup6dKY6mkaSam2oZDBfvNyn1qWh2VCvH8esIjsd2iReqrpwOfF9A_zc6-kFxNtTPBoU83TaFDE42Xd05VaiC7FRRhnKkGezN6oalVfAEbml5O64f4bTd-ikV9GfOpnypPHtQJOSzIwv0SL9CRyT1Yy8N6mrsLPv4fXxZZPQiBx3kOUvJyVRVUaEqmIjiIhaztApVJY-GRYx7zxm-x3pLm2NGs7BADIcjECk6AWtRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d4cb4aa2f.mp4?token=RTcKoS8nV1OXXh5WpgofQdZJZ88faGiaOLb-b-RRROX9vxYHB8l3WzEDtfs7GmvO-An27NS99RHhpxDe9Xirf7vtsGHhVKycf9ppMBrNSgCRTup6dKY6mkaSam2oZDBfvNyn1qWh2VCvH8esIjsd2iReqrpwOfF9A_zc6-kFxNtTPBoU83TaFDE42Xd05VaiC7FRRhnKkGezN6oalVfAEbml5O64f4bTd-ikV9GfOpnypPHtQJOSzIwv0SL9CRyT1Yy8N6mrsLPv4fXxZZPQiBx3kOUvJyVRVUaEqmIjiIhaztApVJY-GRYx7zxm-x3pLm2NGs7BADIcjECk6AWtRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇳
🇳🇵
ویدیو هایی از سیل آخرالزمانی و وحشتناک امروز نپال که باعث شد صدها نفر کشته و ناپدید بشن!
ویدیوها عمق فاجعه رو به خوبی نشون میدن!
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/70640" target="_blank">📅 23:55 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70639">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=Q46-MRnW70FUm-nxyjpFUrECEFXrQesmbnc230eg9OmnAlTsXXayGRyAJCTnswJRtMcxRU7Yg9RzKY1PpKLob8M23TOs0W33uXfGChgIFdO9vAIx07JVeAAYHlLnp6lPit4SUYHD4GtE5SFvWceVRlbpSHwiMcT5CIeUEOQuNf9Yuz8EpZMea85qbba1h9jBoavXN_ZqreqSy_ZDMKHXxk_ZvouBvFz-YHfyWiA6QlZL7K8M5UKhfEcDI9abCE8_6-2JIWApPNzcT0I93vTSzG_2j50o3cSyw_mlP_eYCIWb-gk7Xw1K49Q_teocTmSlTL0-eJw2Esu-t4SfpLmJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eee2e6eb68.mp4?token=Q46-MRnW70FUm-nxyjpFUrECEFXrQesmbnc230eg9OmnAlTsXXayGRyAJCTnswJRtMcxRU7Yg9RzKY1PpKLob8M23TOs0W33uXfGChgIFdO9vAIx07JVeAAYHlLnp6lPit4SUYHD4GtE5SFvWceVRlbpSHwiMcT5CIeUEOQuNf9Yuz8EpZMea85qbba1h9jBoavXN_ZqreqSy_ZDMKHXxk_ZvouBvFz-YHfyWiA6QlZL7K8M5UKhfEcDI9abCE8_6-2JIWApPNzcT0I93vTSzG_2j50o3cSyw_mlP_eYCIWb-gk7Xw1K49Q_teocTmSlTL0-eJw2Esu-t4SfpLmJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عبدالملکی، وزیر سابق کار:
دولت دروغ می‌گوید که پول ندارد و نتوانسته نفت بفروشد. در طول جنگ ۴۰روزه، فروش نفت ایران افزایش قابل‌توجهی داشت و درآمدهای نفتی کشور حدود سه برابر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70639" target="_blank">📅 23:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70636">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=MHARsT-u9omeUHJLB_79L3RlpiNt6w5mHvgd4k_VjVM8WE1IWUzbTeAulDWPpEScClbXJo94rAT32u6Xb0NK45p_fw4MUFtCIjPbsZTBLM8BEeaTzYjWgrqHBuQByv521Oyg7PXhKw3gUYAU6lCpnihcYuUlJmYskDudk73YQz_QHSZMP3ze7tG_ZQA6fQj9817SzlLSMAw1W-Vgoutn9OYV0r-RhSHiG9cHXPzLMG7vZFNTIlR-z-CqOYz1VmeSM-QSp8-bIdGuyBUAdXjSa6zhEpaWwFauE0WCwQF974bjhryUXQ1lLulTodA8gwW2kEmWlCg4XsqLEbSOFByveA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07429c6dd.mp4?token=MHARsT-u9omeUHJLB_79L3RlpiNt6w5mHvgd4k_VjVM8WE1IWUzbTeAulDWPpEScClbXJo94rAT32u6Xb0NK45p_fw4MUFtCIjPbsZTBLM8BEeaTzYjWgrqHBuQByv521Oyg7PXhKw3gUYAU6lCpnihcYuUlJmYskDudk73YQz_QHSZMP3ze7tG_ZQA6fQj9817SzlLSMAw1W-Vgoutn9OYV0r-RhSHiG9cHXPzLMG7vZFNTIlR-z-CqOYz1VmeSM-QSp8-bIdGuyBUAdXjSa6zhEpaWwFauE0WCwQF974bjhryUXQ1lLulTodA8gwW2kEmWlCg4XsqLEbSOFByveA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دادگاه محاکمه اندروتیت اعلام کرد ماشین های بوگاتی و استون مارتین اندروتیت اجاره ای هستن(یعنی مال خودش نبودن)
اندروتیت یه مدت بخاطر ویدیوهای انگیزشی و سیگما طور که میداد بیرون؛ حسابی معروف شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70636" target="_blank">📅 22:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70635">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_yONvpcvM9TWXzZ8A_bOBuX_xV35TiwyIzE5qQa9A28qKfZGCJk--bbYjHYFazIcrS2hN52XOSwTh15HqlixAHrzHG75pfJEH8SwdyQtGHN2_1Ps3rRsp7_RDrrzf8jK76AlW4CZAJeTsjgTXExj-4A2LS-v2NMZRZj3dy3RlFDfRy9oPGZH8xNSW1gVvVeh96ckPdXHN1qVtT0J06wrrR553eW6LbXdf80ElTQsEy4xFUarjT-XV2R3xKOrZf38NYJHEnoHqe9S107UZRke-YrTzrxdUovcLTrT148mrdOKYCNL1wegiafjBXy57BIKwT7MdED_IbQlIG7TaXJ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قالیباف:
ما از بیانیه اولیه چین حمایت می‌کنیم که تحریم های غیرقانونی علیه ما رو رد کردن
مشارکت استراتژیک ایران و چین بر پایه احترامه و سازندگی و یک دیدگاه چند قطبی استوار وجود داره
این رابطه نیاز به تایید هیچکس نداره
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70635" target="_blank">📅 22:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70634">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66110614c2.mp4?token=f8vRtVV6bMBf9_u6Fs3iC7cKGLRCL50ikYpD67R30Sr6yNsqU-rSBMHEOLqb6VTrvAvRy746qqaLfGlObm-n5g_6w9GMIAyiWNF8qoPxMifJK2qgGM4ISfEEaCoqHDMiyEKWjtTn78FZJQYITsFR2LiaQzhEhqspYDH0SxeRpLKizIn-A7sLeAO_pV3PiBGs3ivQ5F4J5Puh1va-IuWV31a5be8x7R63Xoh08rno5WcnH3YHxg_GEA4Fg0YLmnfz-0cSdoDCZQ-zDHzPKpcrWKnUMdW-PAzpyizpjxNYC9AAthwuAif_tZZQR02xLEB3ndw597i6GgQMRBoeqlr6oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66110614c2.mp4?token=f8vRtVV6bMBf9_u6Fs3iC7cKGLRCL50ikYpD67R30Sr6yNsqU-rSBMHEOLqb6VTrvAvRy746qqaLfGlObm-n5g_6w9GMIAyiWNF8qoPxMifJK2qgGM4ISfEEaCoqHDMiyEKWjtTn78FZJQYITsFR2LiaQzhEhqspYDH0SxeRpLKizIn-A7sLeAO_pV3PiBGs3ivQ5F4J5Puh1va-IuWV31a5be8x7R63Xoh08rno5WcnH3YHxg_GEA4Fg0YLmnfz-0cSdoDCZQ-zDHzPKpcrWKnUMdW-PAzpyizpjxNYC9AAthwuAif_tZZQR02xLEB3ndw597i6GgQMRBoeqlr6oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو‌ ارومیه یه پسره واسه دوست دخترش یه لندکوروز سری 300 که قیمتش بیش از 70 میلیارد تومن هست رو خرید تا سوپرایزش کنه.
تازه، زیرش میدونین چی نوشت؟
ایشون نوشتن، تقدیم به زیباترین دختر ارومیه...
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70634" target="_blank">📅 21:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70633">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBe6PAa--vrazTQubZhONTql0pHi8lmrsg3SQLU3aqicYNr3yhXcqjLsjxEbahjBZObIq52vzRzVQnXC8FYb5MYj0PJ9s5wKxqLVOuQ-Cc-Y9wyJ-pIDII3sG0zfIBizl1YqqDaNU278H-wE-wk6EFgAPbEirKwhEnGaiPBX86R9U8CDg-y_YsUfpFl4p9iNw7SM6GY5QHUtUpx75rPQmfym7msCNBHOWTuvcx01zfshCn2wb-J6x4z0kDikYGp3YqfmhsXrVNVRlMxNbJbZOZCWyHSb_4HEnr8kA5da2CE0tLpcMDCTmC9zvgo2JBz5zpPNnu_8YMx57I2FnFUnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
فارس:ایست بزرگ مقابل کشتی هندی در تنگهٔ هرمز
یک نفتکش هندی به نام «HAANA» لحظاتی پیش قصد داشت تا از مسیر جنوبی تنگهٔ هرمز موسوم به کریدور عمان عبور کند اما با هشدار داده شده از این کار منصرف شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70633" target="_blank">📅 20:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70632">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyIOfttAV871HHG7ueGIgHh8X3vQ1_9v0c5OAh1NKB1sz7NkMRE3UgXpnI9QMd__BuTHmaKs4MuWxKImQx49-7ZGl83GeCZb_UGtFEQO5FryPMuh9p3qZt9_RaCqbioGQzdZaHf2cB-v2RKejH42kiwzIMJ_d-fHWd4EWqDaOby8v79wG9GkdRz2OfeYiaCM1y9iE2vSpoaR_FqgDrABbtmIR06KZ8FwDc6MrVL5vHOUDm19-ETcaoxj1TNaje48bN9bM55NyRV2P4HVb-rjYVLVN7DWbuYZWfcjCxXwiBQP6JEOApZxVu_snAeVvLxQMqfJ13CLHGisC8bhfVR64w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
پست ترامپ در تروث سوشال
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70632" target="_blank">📅 20:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70631">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ℹ️
صحبتای امیرمحمدزند بازیگر صداوسیما:
حرفم با مسئولین اون وره چون این ور اگه حرف بزنیم احضار میکنن و تعهد میگیرن اخرشم‌ممنوع الکار میشی
قبلا حدقل زنگ میزدن میگفتن ممنوع الکار شدی ولی الان زنگ هم نمیزنن خودت باید بفهمی جلوی نون تورو گرفتن
ما ایرانیا با دلار ۲۰۰ تومنی و طلای بیست چند میلیونی و مرغ و گوشت و .... خیلی مردم شاکری بودیم
هرچقدر هم اقتصاد بد باشه گرونی باشه جنگ باشه میگن باز شکر کن سالمی حدقل
بعد که مریض میشی میری بیمارستان با هزینه هنگفت میگن شکر کن حداقل زنده ای
طرف میمیره بهش میگیم خدارو شکر بابا مرد و راحت شد
ما ملت ایران انقدر شاکریم خدایا یه امتیاز ویژه برامون قائل شو
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/70631" target="_blank">📅 19:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70630">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
مهاجرانی سخنگوی دولت: در میدان ولی‌عصر یک خانمی به من گفت الهی بمیری!
رسایی سرباز نظام نیست؛ ظریف سرباز نظام است
رسایی منافع ملی کشور را نمی‌فهمد!
جریان پایداری خلاف منافع ملی حرکت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70630" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70629">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=MKyHq8JlRuIgQH2cDol_PMNEOHzh8Qo4c32pgAaHM6fkLLhiMa-DQg1eJX_Cn2SEAENTaw0vVx5mm0zCLMyDH4ufsDH1Am8_-8N7Si45SsCpEY9Tbow-eyBxeTfZB8SnWvNWYIV25GSmIMFBWiEmvbRaoylslFin5GeCdKTjdWYNz5gMwVxBWv3aInmBk0_9t6_BQwsvwww9jGX7pxMrS3Hu2GqbWjnqLKBZMuLKfsVVFq5X14ap_TKMxxQ-iLF8BfXa010hrcXTJyWs1jMu7FVALGkhr68Gb7jKodDCSqoc76Zi3MJcJumwnlB-NUnAX65lgYCDQggvGObWM2A6RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=MKyHq8JlRuIgQH2cDol_PMNEOHzh8Qo4c32pgAaHM6fkLLhiMa-DQg1eJX_Cn2SEAENTaw0vVx5mm0zCLMyDH4ufsDH1Am8_-8N7Si45SsCpEY9Tbow-eyBxeTfZB8SnWvNWYIV25GSmIMFBWiEmvbRaoylslFin5GeCdKTjdWYNz5gMwVxBWv3aInmBk0_9t6_BQwsvwww9jGX7pxMrS3Hu2GqbWjnqLKBZMuLKfsVVFq5X14ap_TKMxxQ-iLF8BfXa010hrcXTJyWs1jMu7FVALGkhr68Gb7jKodDCSqoc76Zi3MJcJumwnlB-NUnAX65lgYCDQggvGObWM2A6RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای این دختر در مورد اینکه تو این جامعه، سخت‌ترین کار پسر بودنه، به سرعت در حال وایرال شدنه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70629" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70628">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/70628" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70627">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAlrJ_6ifO5BWSQH04_oTj5wtnq5cueRpVzcx0zvFApy-jDW7PRgEmLlQVp9948BoYHTQ7Uog9n4YZMC45zIY0jsiUTpgDPd25Cg9FBivqhto9qtCkM43gSYzirgtGu3QW5pGwkWXzf6pTQ0n9u9Ps8HPZc-FiccAtJwElv4NzkumJOuX5vCVBt8JxJF8hxlreMVQwvlBYdPVptxurLMJB0_CCYibFB7TV8K_9kOOVvhnjsklrrq3NWF9ehfaCPuC-QMSlD-wtpt8uTLYONkfEBrHIvuxORnSUbRu8VBPREqS90m6uMdL2I5xIdhQ7pUfRwjmDmqvASHHo9tClW2tG_c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAlrJ_6ifO5BWSQH04_oTj5wtnq5cueRpVzcx0zvFApy-jDW7PRgEmLlQVp9948BoYHTQ7Uog9n4YZMC45zIY0jsiUTpgDPd25Cg9FBivqhto9qtCkM43gSYzirgtGu3QW5pGwkWXzf6pTQ0n9u9Ps8HPZc-FiccAtJwElv4NzkumJOuX5vCVBt8JxJF8hxlreMVQwvlBYdPVptxurLMJB0_CCYibFB7TV8K_9kOOVvhnjsklrrq3NWF9ehfaCPuC-QMSlD-wtpt8uTLYONkfEBrHIvuxORnSUbRu8VBPREqS90m6uMdL2I5xIdhQ7pUfRwjmDmqvASHHo9tClW2tG_c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g4
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70627" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70622">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=JcHvirtvScC-9QKfB4oBG-XWzg8QJBNeD1tci0R_BftMUt-K0z8zzpXWJEHGLmZGAsrOertP_XkQM17bUGawsnpMYJW3kYqrazzWkA3113exqmU1_vI8GSEAOmzCAT1hwaw4Z4a3VbZySf0abtmYEgGiPyWuB65VrQ-7rj8JLjNyrlLb7AhnqyJPP2HyehCOe85dptBYnQzVctQ1RBOSRaMhzNjMfxyGI_QQGeuJlm6J013_BDdoWykDbdX19jFAMPDj4DslqRnVkdgltNmOqxC959cQNC20FO7lGD9SyKRTepyiqwwoifwyJJyuvY8VQUebDYDJggWXqy7mvHjJoqoUWvmam1DgR0cMp6v0iZGAiahiz9kKXPLPbHGtWgAJJ6VOTCofljkIf6zUSm9oKDf0jpT1-kCbH9cqsB7K_sZzw4s6_3GANX0XPogmF2zLlz_LCOkJo-mCFwSb7vfdXkHNb9lcXi4nLwijbdMw6rCz62Kg7FPTfuxPU3IkdcDUJoC06bSoBAV0OEo5-qSm0jDvKzxqDOIsSzJy1Kv4DKhTbcvg3A21aKxLZ2-5D_MevkymoaGBxyxbo31i1XIb9-6rW15NnP5nop6-myPoLe-PBb3cexpab6gxsN6irtqr-X4WHmQrlZCOFM0w6GNRkYgFCF4mURyhW4la9EIZqZU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=JcHvirtvScC-9QKfB4oBG-XWzg8QJBNeD1tci0R_BftMUt-K0z8zzpXWJEHGLmZGAsrOertP_XkQM17bUGawsnpMYJW3kYqrazzWkA3113exqmU1_vI8GSEAOmzCAT1hwaw4Z4a3VbZySf0abtmYEgGiPyWuB65VrQ-7rj8JLjNyrlLb7AhnqyJPP2HyehCOe85dptBYnQzVctQ1RBOSRaMhzNjMfxyGI_QQGeuJlm6J013_BDdoWykDbdX19jFAMPDj4DslqRnVkdgltNmOqxC959cQNC20FO7lGD9SyKRTepyiqwwoifwyJJyuvY8VQUebDYDJggWXqy7mvHjJoqoUWvmam1DgR0cMp6v0iZGAiahiz9kKXPLPbHGtWgAJJ6VOTCofljkIf6zUSm9oKDf0jpT1-kCbH9cqsB7K_sZzw4s6_3GANX0XPogmF2zLlz_LCOkJo-mCFwSb7vfdXkHNb9lcXi4nLwijbdMw6rCz62Kg7FPTfuxPU3IkdcDUJoC06bSoBAV0OEo5-qSm0jDvKzxqDOIsSzJy1Kv4DKhTbcvg3A21aKxLZ2-5D_MevkymoaGBxyxbo31i1XIb9-6rW15NnP5nop6-myPoLe-PBb3cexpab6gxsN6irtqr-X4WHmQrlZCOFM0w6GNRkYgFCF4mURyhW4la9EIZqZU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
وقوع یک سیل ناگهانی و شدید در منطقه مرزی میان نپال و منطقه تبتِ چین، خسارات سنگینی به بار آورد.
گزارش‌ها حاکی از آن است که در پی این فاجعه، تاکنون صدها نفر از غیرنظامیان و نیروهای نظامی و پلیس مفقود شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70622" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70621">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
فکر می‌کنم ۳۰۰ [درصد] باشد. شنیده بودم ۹۰ درصد؛ اما به نظرم تورم ۳۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70621" target="_blank">📅 17:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70620">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=qpBm164LFiSdrczFFukEI-savnzs_xwJACbPgyvuoxLU1B6aCq2X6X_B_3SvMiGq55iAgZPkkfLx7rGlHdKLiGrTiJC_X4UOei6yCckY-kBK-vYZ6Hldx8EhT0T8Fy3X1qLA02UtP_FuQ03kxeonb3PgDZdB2Oq5J1QliJdokNIQHxlUulzNlpoNrnWZOJzZIWMad6LBtjJa4DsHpqzMIsVf3Md57f5csHuaZImYGBFtda8-33fsbhdvbBAcT90puPzbM0y59wzYXVJcCNo-FZ8TkjlXoP5Sj6D5XVasy9IXHB3FhCIUyX4MfTeST73rOCE1bbwzeLbeagM9fF1BAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=qpBm164LFiSdrczFFukEI-savnzs_xwJACbPgyvuoxLU1B6aCq2X6X_B_3SvMiGq55iAgZPkkfLx7rGlHdKLiGrTiJC_X4UOei6yCckY-kBK-vYZ6Hldx8EhT0T8Fy3X1qLA02UtP_FuQ03kxeonb3PgDZdB2Oq5J1QliJdokNIQHxlUulzNlpoNrnWZOJzZIWMad6LBtjJa4DsHpqzMIsVf3Md57f5csHuaZImYGBFtda8-33fsbhdvbBAcT90puPzbM0y59wzYXVJcCNo-FZ8TkjlXoP5Sj6D5XVasy9IXHB3FhCIUyX4MfTeST73rOCE1bbwzeLbeagM9fF1BAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
وقتی کسانی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است؛ به همین دلیل است که آن‌ها اعتراض نمی‌کنند.
و البته احتمالی هم وجود دارد، چرا که آن‌ها بسیار تضعیف شده‌اند... به بسیاری از سربازانشان حقوق پرداخت نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70620" target="_blank">📅 17:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70619">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=Ty5d8gRBaEyN4k2eXdVJhe_oM9JwEXnq0whwKiA7DnGP5nHvOmdAyyywAQTfnsWCUJY4QN-iK8EoTL-0wSZQsE7sgDV5_ybwPviXAlp_-cXTVrm1tzWOw3b21PB1p8DCs8lHjjedJOyhlgttcODoGeUWFAQe7Z2VHz0-C6TIswrfrEmG__xo7Ty25VBsgBI9eKCdGv0aJ0OlZzD8idbpWVadhT2scBWeAKa1yGuLFbd1JvNzVcO6u56JWyQRxAn8snPP8ApKwl7SMM3hGDprawdzzhsBY0gS2EEncctjgIwryitV_CRUTxVCycJbxom6b8cylVv7ohXatY_4EDV86w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=Ty5d8gRBaEyN4k2eXdVJhe_oM9JwEXnq0whwKiA7DnGP5nHvOmdAyyywAQTfnsWCUJY4QN-iK8EoTL-0wSZQsE7sgDV5_ybwPviXAlp_-cXTVrm1tzWOw3b21PB1p8DCs8lHjjedJOyhlgttcODoGeUWFAQe7Z2VHz0-C6TIswrfrEmG__xo7Ty25VBsgBI9eKCdGv0aJ0OlZzD8idbpWVadhT2scBWeAKa1yGuLFbd1JvNzVcO6u56JWyQRxAn8snPP8ApKwl7SMM3hGDprawdzzhsBY0gS2EEncctjgIwryitV_CRUTxVCycJbxom6b8cylVv7ohXatY_4EDV86w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما از شر مین‌ها خلاص شدیم. اما تنگه هرمز... تنگه فعال است؛ یک تنگه فعال.
بله، هر از گاهی پهپاد یا راکتی یا چیزی شلیک می‌شود، اما این تنگه کاملاً فعال است.
مقدار زیادی نفت از آنجا جریان دارد.
دیروز ۱۰ میلیون بشکه.
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/70619" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70618">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=hvBOQJx2Umr54NNG8ltcaH6BL7NzJiTZIzc00ABBzsENuKkU28AbR3118LArYnj8vRO4gq-cgp4P1EdnJrbwVLPzTrIy0s5GuqzdeZVWlmlLUhmzec76P_BkQ3alMZOgaYjmbB7BGvo47KIKdbVdPxduOYyzPpFF0ZX6JWSODjof0gmBXcM5Nbnqz2y1MOgnS5Xq-Z1C2_m55W-LwzLa4eThmr1W1lqUEpY_UGzTAtm6XOyTeVKTd7LFHZ0aq4gTc9qTuIeZhJ4cFquZxDUWaqxThgiJSpyMxfmmgxoamiNJ3b5l7VOqDekSNiUR7v8Z7yt5zZh-8bOEBUZtqUkLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=hvBOQJx2Umr54NNG8ltcaH6BL7NzJiTZIzc00ABBzsENuKkU28AbR3118LArYnj8vRO4gq-cgp4P1EdnJrbwVLPzTrIy0s5GuqzdeZVWlmlLUhmzec76P_BkQ3alMZOgaYjmbB7BGvo47KIKdbVdPxduOYyzPpFF0ZX6JWSODjof0gmBXcM5Nbnqz2y1MOgnS5Xq-Z1C2_m55W-LwzLa4eThmr1W1lqUEpY_UGzTAtm6XOyTeVKTd7LFHZ0aq4gTc9qTuIeZhJ4cFquZxDUWaqxThgiJSpyMxfmmgxoamiNJ3b5l7VOqDekSNiUR7v8Z7yt5zZh-8bOEBUZtqUkLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«باید بگویم که آن‌ها اصلاً گروه شرافتمندی نیستند. و می‌دانید، ما کاملاً قاطع عمل می‌کنیم؛
دیشب ۲۲ فروند از قایق‌هایشان را نابود کردیم.
آن‌ها سعی دارند محاصره را بشکنند و وارد شوند.
نیروی دریایی و ارتش ما عملکردی فوق‌العاده داشته‌اند.»
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70618" target="_blank">📅 17:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70617">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=Oh97RGLRNZ_qjLEZ2LwzGHcHXfs2yBrJtpokpuXmMZ7vWrLMCQXUFsP935iRJhGR1F5_kxqEgbZpjwNT0ZUjaCOw8pyt1axHgIHcDWu-VNi9N3MgLcj5Un7FQ1B1YIpwtMyPwt9_p0rghO5jKqbN_mhYJ2JWc86krhqGhv9AxtiDCu2IofsL0KOSt6tCwAR-JiAYIvHg-FjzV6A6oyDsl2i78glMqY2ftUEdOw8UvL53LrWfFChAZMW6yc2q2roHEOWzpWJjj0Q4s7eJODJWJvAEzuy-sQK6_ff-jxUF5jWj_Rf9DLR_l2Mkt343jZbGS_Qxly4TkHtx7HKZ9BVvwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=Oh97RGLRNZ_qjLEZ2LwzGHcHXfs2yBrJtpokpuXmMZ7vWrLMCQXUFsP935iRJhGR1F5_kxqEgbZpjwNT0ZUjaCOw8pyt1axHgIHcDWu-VNi9N3MgLcj5Un7FQ1B1YIpwtMyPwt9_p0rghO5jKqbN_mhYJ2JWc86krhqGhv9AxtiDCu2IofsL0KOSt6tCwAR-JiAYIvHg-FjzV6A6oyDsl2i78glMqY2ftUEdOw8UvL53LrWfFChAZMW6yc2q2roHEOWzpWJjj0Q4s7eJODJWJvAEzuy-sQK6_ff-jxUF5jWj_Rf9DLR_l2Mkt343jZbGS_Qxly4TkHtx7HKZ9BVvwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره مجتبی خامنه‌ای:
فکر نمی‌کنم مجتبی خامنه‌ای مرده باشد.
او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دست و پایش، و تمام آن ناحیه آسیب جدی دیده بود.
اما گمان نمی‌کنم که مرده باشد.
اگر هم مرده باشد، دارند نمایش خیلی خوبی اجرا می‌کنند؛ چون مدام صحبت از این است که باید برای گرفتن تأیید نهایی‌اش با او گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70617" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70616">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=LLBBQGOANa65qKQwDsj-v17VM67P0hxiaNeh19eNlEBIN9fYqKaFE2paKYEc0hyfZzYNrybuE6CPOcK7JRn-UYHNnpuKQIkimO0m1nZ4rPX9WrPbU3ZZ-0_i7ycwEWhRILi0OubnvadjyFlVxyKItp2bjKKetKNIiplqNuD2x9LcwcT2a2PH0qH1Vxno9PEe8OfnjMdMI9TUtODIEUjA2wjSZUZLYyRPRWOos7R8CjKK9XArbo-xoSIjgsbIO1eeB3r4cgNDbVWi2HrRV5e8LwRUDNZxpdENqM_vYeYAvvSDGNRREiYa5dNW2OWywkvHLbktUXK8YHSTRJLqToJ8zA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=LLBBQGOANa65qKQwDsj-v17VM67P0hxiaNeh19eNlEBIN9fYqKaFE2paKYEc0hyfZzYNrybuE6CPOcK7JRn-UYHNnpuKQIkimO0m1nZ4rPX9WrPbU3ZZ-0_i7ycwEWhRILi0OubnvadjyFlVxyKItp2bjKKetKNIiplqNuD2x9LcwcT2a2PH0qH1Vxno9PEe8OfnjMdMI9TUtODIEUjA2wjSZUZLYyRPRWOos7R8CjKK9XArbo-xoSIjgsbIO1eeB3r4cgNDbVWi2HrRV5e8LwRUDNZxpdENqM_vYeYAvvSDGNRREiYa5dNW2OWywkvHLbktUXK8YHSTRJLqToJ8zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز 4 شهریور ماه، زادروز شاهِ شاهان؛ کوروش بزرگه
.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70616" target="_blank">📅 16:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70615">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b4425472.mp4?token=sIcPWAhxKphxrOi4DAad3cP7mRzsx7FIrBN348ecNzFkZKP4XX1sdAB96RzcX4O-m1B5Qhjx-MwvByLh1tFJrFhnE_d9vncmrJ8P3b62MfKZg9S8DxlXhePwA6LMJuDW-dqxWqM1MSb1T_g20U1mdqOjo7ibQliZOWshDrWXjFWMOcGNRyP5VwzOlwfaVjToj6qHb730j6W7NXgA1ZotpyGkt2-rSeQvXGHYkR2cg5kpuP3pgEnoSCIFsp6Q5FUb4GnJB9ECcZ5Sr13Yy_ILvYa7-zxFKRETlLBADIRUWHvhZOjXSxrF5r--XP9mEH4Q53ygzwXZfulysPMSOFhlzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b4425472.mp4?token=sIcPWAhxKphxrOi4DAad3cP7mRzsx7FIrBN348ecNzFkZKP4XX1sdAB96RzcX4O-m1B5Qhjx-MwvByLh1tFJrFhnE_d9vncmrJ8P3b62MfKZg9S8DxlXhePwA6LMJuDW-dqxWqM1MSb1T_g20U1mdqOjo7ibQliZOWshDrWXjFWMOcGNRyP5VwzOlwfaVjToj6qHb730j6W7NXgA1ZotpyGkt2-rSeQvXGHYkR2cg5kpuP3pgEnoSCIFsp6Q5FUb4GnJB9ECcZ5Sr13Yy_ILvYa7-zxFKRETlLBADIRUWHvhZOjXSxrF5r--XP9mEH4Q53ygzwXZfulysPMSOFhlzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کوهنوردای ایرانی موقع صعود تو کوه های آرارات، آیفون17 این دختر آرژانتینی رو پیدا کردن و بهش تحویل دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/70615" target="_blank">📅 16:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70614">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=U6ZpFMlvxxrwYnae2vnE5ivvHO4K-ZBKtltWbgHcDaWY7K16Ems_dnpgYL6KOYP06T9FY8WeFEnqnsZuOQQpYlIYxx1I0LkcrBgW7p1OcJnUGrgz0cSc6KSBi3C6kDhyvcW7gnr9uz3y8oJ6HPZ1rQafaYrqQYAUyF81MoiUNqwMURw-NzBWKVN0AlfFgOCAvPRnd3_OSZLDOk1QNjhCbLgjOweGUHWSeCcz2sjAf4qkTBqqerc2DHxJrClhURfU6MHwwxvV_rh4a3YhUrS-rK03U3nAAEAw7yhacXVDgSoN-CDGlPCMtTnEJs3bMx5P8iR80vXWN2OOw8Hxr0lLPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=U6ZpFMlvxxrwYnae2vnE5ivvHO4K-ZBKtltWbgHcDaWY7K16Ems_dnpgYL6KOYP06T9FY8WeFEnqnsZuOQQpYlIYxx1I0LkcrBgW7p1OcJnUGrgz0cSc6KSBi3C6kDhyvcW7gnr9uz3y8oJ6HPZ1rQafaYrqQYAUyF81MoiUNqwMURw-NzBWKVN0AlfFgOCAvPRnd3_OSZLDOk1QNjhCbLgjOweGUHWSeCcz2sjAf4qkTBqqerc2DHxJrClhURfU6MHwwxvV_rh4a3YhUrS-rK03U3nAAEAw7yhacXVDgSoN-CDGlPCMtTnEJs3bMx5P8iR80vXWN2OOw8Hxr0lLPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی وایرال شده از نوجوونِ 18 ساله‌ای که با موتور کار می‌کنه:
من روزانه 8 الی 10 ساعت کار میکنم!
امروز یکی ازم پرسید چِتی میزنی یا نعشه بازی؟ گفتم هیچکدوم.
با خودم گفتم من باشگاه‌ام رو میرم، خرجی خونه رو کمک میکنم، اهل دود و دَم و دختربازی هم نيستم.
به خودم اومدم دیدم از خیلی از هم‌سن‌هام جلوترم واقعا
تویی که از این روتین خوشت میاد و سالم زندگی میکنی، به خودت افتخار کن، چون مثل تو خیلی کم شده..
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70614" target="_blank">📅 16:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70613">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=dl2l4wA5PheCHeTlLJiVdQI1UezfA3vTmvRfL7TQNLN1fnJdXJdrd-P002_X9Qc90zXyw-qg5pmkgrWddgDo033nzeahwWVZB7e238LDMSZ0vUSIBH7lMuHkrkbBvZBzFK9M_wXYKeu-wrFj4M9oOVMDqEktiWaiofXSuz0pMfkML0lwCjvsM-oI1UU-GL3QeeDXn4VLkpzzBOg264-iTFRZeOg4ebm2Qznz91yJNbeRsG7-m1_5CAcuJY2ecYMRRKJYexWJhWeqSaEcCmHAfuEHxOSUI6CcsiD5VYxeMpgamFLvg9v8gnjV8Dg4a02J2CGavj-S7Z-VSH_x-E2Mvg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=dl2l4wA5PheCHeTlLJiVdQI1UezfA3vTmvRfL7TQNLN1fnJdXJdrd-P002_X9Qc90zXyw-qg5pmkgrWddgDo033nzeahwWVZB7e238LDMSZ0vUSIBH7lMuHkrkbBvZBzFK9M_wXYKeu-wrFj4M9oOVMDqEktiWaiofXSuz0pMfkML0lwCjvsM-oI1UU-GL3QeeDXn4VLkpzzBOg264-iTFRZeOg4ebm2Qznz91yJNbeRsG7-m1_5CAcuJY2ecYMRRKJYexWJhWeqSaEcCmHAfuEHxOSUI6CcsiD5VYxeMpgamFLvg9v8gnjV8Dg4a02J2CGavj-S7Z-VSH_x-E2Mvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ هر ثانیه بیشتر سورپرایزت میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70613" target="_blank">📅 15:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70612">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=tjqEbcYDtElukytUpgPoITLfGhrV-8zY_KMn6OBy4nNJ7Q4rFKFvzipg38U0_81pTeoE6wfBLVnGgljInvNYvD-5V1MbdDmrlDOJXDUhCbqAPeZVEcI4Kir0MQ4hiSWXFyQlWwjs7tpdI8exPGfUqC81L8FhZ-5ax5Hx0X0hjfIPsOT2KFxnBQXxTTJFa8jqNeKFlWXWU7PKyVHexnuCJsKTHH-FwV4uMhD0aOgV3soaNzZNBbNPcwsx6CZ-85Q3adZ1WWRgJEI--0T6nOpFi3tL347Swh7xv0BxO9aKuNn4QGle_cno1Uj2OKrsTRE5bxSluOPcwcwmDTFbkDw8ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=tjqEbcYDtElukytUpgPoITLfGhrV-8zY_KMn6OBy4nNJ7Q4rFKFvzipg38U0_81pTeoE6wfBLVnGgljInvNYvD-5V1MbdDmrlDOJXDUhCbqAPeZVEcI4Kir0MQ4hiSWXFyQlWwjs7tpdI8exPGfUqC81L8FhZ-5ax5Hx0X0hjfIPsOT2KFxnBQXxTTJFa8jqNeKFlWXWU7PKyVHexnuCJsKTHH-FwV4uMhD0aOgV3soaNzZNBbNPcwsx6CZ-85Q3adZ1WWRgJEI--0T6nOpFi3tL347Swh7xv0BxO9aKuNn4QGle_cno1Uj2OKrsTRE5bxSluOPcwcwmDTFbkDw8ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
لحظه شلیک RPG توسط سرباز روسی که جلوی پاش میزنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70612" target="_blank">📅 15:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70610">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=PBSuyEZYB3PwW1DYgmAZETLXCVow095DPjwH502G6UlyUiHthPbKu70YPNVFVbMgT6RFKK_z1izrbsa501cdU2wA01VK_xKo_uYQWTOpc_TT_Sw34RUKlSgU3dD8_wt7yUCNnrGpbxF-B-K5nQ7TcQAxC9JkO3hanLctKwuKgpymh0zIqTWdTkUzq6MKtkOIFIegWUyGBaEk7LEbwbYtjFWGnHiG28DHnly8fwki49chBYfQAw78AAYL24u4wImb4-Y-fyCXydl7g95PuM21Efj_u9OepIkap55PamgDfDslZjH5Op7_oIE4K2L5hx4lMnOYWu8AVgxltN3C3UAD1A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=PBSuyEZYB3PwW1DYgmAZETLXCVow095DPjwH502G6UlyUiHthPbKu70YPNVFVbMgT6RFKK_z1izrbsa501cdU2wA01VK_xKo_uYQWTOpc_TT_Sw34RUKlSgU3dD8_wt7yUCNnrGpbxF-B-K5nQ7TcQAxC9JkO3hanLctKwuKgpymh0zIqTWdTkUzq6MKtkOIFIegWUyGBaEk7LEbwbYtjFWGnHiG28DHnly8fwki49chBYfQAw78AAYL24u4wImb4-Y-fyCXydl7g95PuM21Efj_u9OepIkap55PamgDfDslZjH5Op7_oIE4K2L5hx4lMnOYWu8AVgxltN3C3UAD1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این زوج به اسم مینا و رضا بعد از پنجاه سال هنوزم عاشقانه همدیگرو دوست دارن و پنجاهمین سالگرد ازدواجشون رو به زیباترین شکل جشن گرفتن و رقصیدن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70610" target="_blank">📅 14:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70609">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IFc4ULdbQaqlGsw6wFJiu4bf_7d0P0fJoUGNwXpSEjyt-EDe3BPtncra1fzcxOxKsb6qQkbpEwmDRrtWSHlKiMGfXTrWY1qBqjcN7A1jlmWLywj0-AozPNY-zR5pS7XG1UzLKQOxxBIWmLF06Wvy4xMZRAjsMtJfERFGTtjJhrG4RPnuOVjfs4Mz5r7XQNwBFGriNlNlxI3i3X7Ldu6vEtlWXl5hadMDUPMDeJZKS-9Eb3C5pAiYhK6jCfqq5s0sy6JIbtDmVyIzS4b5N9HE5aehtqedri6kZuM7UgrAQMDLOwm0L47BtaI7mL26pYWeGNQpFV85b7ofstvoSywInA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زمان شاه هر اسکناس هزار تومنی، معادل ۱۴۲ دلار بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70609" target="_blank">📅 13:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70608">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=sjdsFQQbTyhEXCt1Two1EVT0xqQwg1hzW6J1YKDD2YCEyvm3j1Ykg30rdLH5vdIzEhrZm4v7IDZI36SYlgHnUjlVTUTtJXP1m3I2c0fSBZrdTJ9Rf5Tvipy24QZ3rGSETgyHgN1hHtkrL3p63Ea7d4TOgNnVswyB3nO-yHYto1lVrDZRhPYPmlAdCRZ4N_uuND-ErMlSNIlsInfgwKwrPdAYCwh-wGnERPAfJCOmIbzI5MyDlgIBDZSeo_G9dxm8SjdNYIobdOe0g1OADxhOPOTjvZZgwCAd7pwRjtnX-ULmb8aDKgOx2XpV4N6OLqryYvPpYV24Dh7GI7a2fM5yyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=sjdsFQQbTyhEXCt1Two1EVT0xqQwg1hzW6J1YKDD2YCEyvm3j1Ykg30rdLH5vdIzEhrZm4v7IDZI36SYlgHnUjlVTUTtJXP1m3I2c0fSBZrdTJ9Rf5Tvipy24QZ3rGSETgyHgN1hHtkrL3p63Ea7d4TOgNnVswyB3nO-yHYto1lVrDZRhPYPmlAdCRZ4N_uuND-ErMlSNIlsInfgwKwrPdAYCwh-wGnERPAfJCOmIbzI5MyDlgIBDZSeo_G9dxm8SjdNYIobdOe0g1OADxhOPOTjvZZgwCAd7pwRjtnX-ULmb8aDKgOx2XpV4N6OLqryYvPpYV24Dh7GI7a2fM5yyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تا آخر شهریور هیچگونه تغییری در بنزین 1500 و 3000 تومانی نخواهیم داشت
‏مهاجرانی: تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70608" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70607">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=ehk_CvcXQRGme-M32EDgZQS-5CrhrrV620OJO9cJH9vzmc2Qow1uSC-TJy9AMDmqBSZVctz7TZzsl1GD_b0je6pQVWpAovKOIGYSwK-yYo0wblak9chYPpxXwugdAskiv7RWxUKCAz_RFzIWYHB_nQMBbFNysHU-ZzSbNqauq8igSuLQXDFngHbApUeKLw6RfovFwGegluEjVSe1Apsb55mQevLwluUD2A4JtGUYrF4iT0PAfRaurG7oeTe-bRQFT-qARCZF9iO51A7y3MbsPEzvjABlGu4HkU6zi_BeNPdXPdb0bht6X5cC1DzyWgvwvU8VimmkXcn3DhvLaSMccg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=ehk_CvcXQRGme-M32EDgZQS-5CrhrrV620OJO9cJH9vzmc2Qow1uSC-TJy9AMDmqBSZVctz7TZzsl1GD_b0je6pQVWpAovKOIGYSwK-yYo0wblak9chYPpxXwugdAskiv7RWxUKCAz_RFzIWYHB_nQMBbFNysHU-ZzSbNqauq8igSuLQXDFngHbApUeKLw6RfovFwGegluEjVSe1Apsb55mQevLwluUD2A4JtGUYrF4iT0PAfRaurG7oeTe-bRQFT-qARCZF9iO51A7y3MbsPEzvjABlGu4HkU6zi_BeNPdXPdb0bht6X5cC1DzyWgvwvU8VimmkXcn3DhvLaSMccg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
می‌خواهم به شما بگویم: ما همچنان با چالش‌هایی روبرو هستیم.
چالش ایران پایان نیافته است.
ما همچنین باید کار را در غزه، لبنان و سایر عرصه‌ها به سرانجام برسانیم و برای انجام آن مصمم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70607" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70606">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=EL0H0VSl5-lgBWARYTofTuv7dup8prfGKUnC2Rd2XSrXgQRqE-ikH89gvZmqXenjLFGArRShy4Drr7XJms7RmDJofFzeTC5AW3c3mQ9aEVmLDZaL22vxw6qBSWa-KVBEcj9SHdMJM4025jhQwyDn_CoiHRe1Ys27nudboDP-phATzA2vGhP-v4K2--XXErbCbNX16Xdk1HNngFU_j42iuPz0bt6oIS7QvGEoB71zYxd3CppuT5K0U5GX68OjTataKV_9tN6S8TynePSIe0ZxYuJdUDtHNtmyIPJI5V60-x41XBxoeCsTdSvWNpzceimS1v_sJ0yKK66BQqkQxyjgtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=EL0H0VSl5-lgBWARYTofTuv7dup8prfGKUnC2Rd2XSrXgQRqE-ikH89gvZmqXenjLFGArRShy4Drr7XJms7RmDJofFzeTC5AW3c3mQ9aEVmLDZaL22vxw6qBSWa-KVBEcj9SHdMJM4025jhQwyDn_CoiHRe1Ys27nudboDP-phATzA2vGhP-v4K2--XXErbCbNX16Xdk1HNngFU_j42iuPz0bt6oIS7QvGEoB71zYxd3CppuT5K0U5GX68OjTataKV_9tN6S8TynePSIe0ZxYuJdUDtHNtmyIPJI5V60-x41XBxoeCsTdSvWNpzceimS1v_sJ0yKK66BQqkQxyjgtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
⏺
و من به ترامپ گفتم که احتمال سومی هم وجود دارد: تشدید محاصره.
او دیروز آن تصمیم را به شیوه‌ای بسیار بسیار قاطع تأیید کرد.
اقدام دیروز رئیس‌جمهور ترامپ، تشدید محاصره ایران بود؛ نه از طریق تنگ‌تر کردن حلقه محاصره خودِ ایران، بلکه با تشدید فشار و محاصره بر کسانی که به این رژیم — این دیکتاتوری هولناک — کمک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70606" target="_blank">📅 12:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70605">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c258982c.mp4?token=JuZYCOJRQN0euOBWxi-trmPrSSKsSyoOwq3I89X4hde0AXi_BZ9h8oCiJ6yJO9osoIu84ueRJlYfiWYPCgGDkKZhkLI3iEa2Q53aHzPXrUj51jU8HksOfnXi4OSc30hVHksWrgRc97zxD3pCD9daw_-iKQACzKKux3aH4uPgxIXb1WzUWOIxG35mrCTMx3f2dnrlL5QerUNWGZvltOsTpvsqIT5Ll8NlP3qG8L7XzshPo16oT9A-IMG_NfvD9esjKWqJXXhhzxG6CV8g1laKBS8GsNTPUXypdWqIGOimzoiB0J7sjjKlBCtVIcEhZM1l4iS4vFIplFxpo1-b-lwm6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c258982c.mp4?token=JuZYCOJRQN0euOBWxi-trmPrSSKsSyoOwq3I89X4hde0AXi_BZ9h8oCiJ6yJO9osoIu84ueRJlYfiWYPCgGDkKZhkLI3iEa2Q53aHzPXrUj51jU8HksOfnXi4OSc30hVHksWrgRc97zxD3pCD9daw_-iKQACzKKux3aH4uPgxIXb1WzUWOIxG35mrCTMx3f2dnrlL5QerUNWGZvltOsTpvsqIT5Ll8NlP3qG8L7XzshPo16oT9A-IMG_NfvD9esjKWqJXXhhzxG6CV8g1laKBS8GsNTPUXypdWqIGOimzoiB0J7sjjKlBCtVIcEhZM1l4iS4vFIplFxpo1-b-lwm6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
⏺
به ترامپ گفتم:
البته یک احتمال این است که شما با ایران به توافق برسید؛ یک توافق خوب. ما هیچ مخالفتی با آن نداریم.
اما تردید دارم که بتوانید با آن گروهی که آنجا هستند — با آن وحشی‌ها — به توافق برسید.
🔴
به شما می‌گویم: نمی‌توانید با آن‌ها توافق کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70605" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70604">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=cDbugAI3oO3C5x7NmOYnNxRwDC2pcFpRPLpOJAhSUlWSd3G47mA99wEIN_qP38PbZGUlReLzG2TSIMnc3yNFu2NBYqgKe6xDiNIeFAD-QOPa07iNy2ZpECE_RPFdUDWkGFmSbnWdK003fVhCJRsiFMPER7S-inqg_LlW_GYPSzM7fcAfxVFRlFxewsbuFeb-SlM75fPJ1sWyfLbXXrjJGygn5LMI-QaVdbpazTK220j1PRCHSwsbFetDX-WXJnIuPJLNYemYteGJTGbUgYhp7d6MKYUtg_Uk40ITiyy_BIIpIAcXsIIgd6XgRtBTH65b_A6zt0mzxOL_kNirdNfEug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=cDbugAI3oO3C5x7NmOYnNxRwDC2pcFpRPLpOJAhSUlWSd3G47mA99wEIN_qP38PbZGUlReLzG2TSIMnc3yNFu2NBYqgKe6xDiNIeFAD-QOPa07iNy2ZpECE_RPFdUDWkGFmSbnWdK003fVhCJRsiFMPER7S-inqg_LlW_GYPSzM7fcAfxVFRlFxewsbuFeb-SlM75fPJ1sWyfLbXXrjJGygn5LMI-QaVdbpazTK220j1PRCHSwsbFetDX-WXJnIuPJLNYemYteGJTGbUgYhp7d6MKYUtg_Uk40ITiyy_BIIpIAcXsIIgd6XgRtBTH65b_A6zt0mzxOL_kNirdNfEug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رفسنجانی سال ۱۳۶۰:
پهلوی همه همت و دغدغه ش این بود که مردم خونه و ماشین خوب داشته باشن؛ زندگی خوبی داشته باشن و ارتباط ایران با کشورهای جهان خوب باشه ولی الان دیگه اینا ارزش نیست و برای کسی مهم نیست .
الان دیگه مردم دنبال معنویاتن.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70604" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70602">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=gWyT1DBYccE_nzWN0INrKXIo7QxYMSLuLSwz2vI7rEq5ya6vtKgzVlSkybNmXZFjB7rpFiiWV8FW9DngEfU5c-PAwKM272kpe7a2sjdP92o9gNIWXqpU74cycYyJ-vrG7MTR8lw8qvUprcSUTV5twpYLCJSO6WIG5fNp9ysBXEkqHu29dj2ZtNwTqITQJLKZNurgbNJ_gdFw6Jg9C2Hde4Vyop9LaSj0ZpFtGyExi6SiXVrZXkLBg6aFplawsWrKyRcU0XbpU6qwnLMvDr8s7cBtosn_LpdhLbomg1TafO2mGTuTAqfLwrMqUzeMWn7SEy7oHDH7WFjZ__p62u7Vbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=gWyT1DBYccE_nzWN0INrKXIo7QxYMSLuLSwz2vI7rEq5ya6vtKgzVlSkybNmXZFjB7rpFiiWV8FW9DngEfU5c-PAwKM272kpe7a2sjdP92o9gNIWXqpU74cycYyJ-vrG7MTR8lw8qvUprcSUTV5twpYLCJSO6WIG5fNp9ysBXEkqHu29dj2ZtNwTqITQJLKZNurgbNJ_gdFw6Jg9C2Hde4Vyop9LaSj0ZpFtGyExi6SiXVrZXkLBg6aFplawsWrKyRcU0XbpU6qwnLMvDr8s7cBtosn_LpdhLbomg1TafO2mGTuTAqfLwrMqUzeMWn7SEy7oHDH7WFjZ__p62u7Vbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مدیر شرکت «فردا موتور» داشت واسه ثبت نام کنندگان خودرو توضیح میداد که ماشین نداریم. دو سال و نیم صبر کردید؛ باید چند ماه دیگه‌ هم صبر کنید که مردم گفتن «سیشتیر بابا همتون همینو میگید» و ریختن سرش.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70602" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70601">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70601" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/70601" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70600">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0s_QoPLwX0OaYSfoElQO8dX08jO9CFCPQejnB3kT_uiMT8vzjGAZ4G52-fpUExxWXSBJP3GltWx79PASQ8kZ1wHpRq3i-ZMkqvwFv8UmBkOYJZsIfQarC2iyQ9EkgYsrCo4oP0_8XO41j_Nw6RG3UsZRpwxpHHJqwVTxnUO0-2FOzL0ySzwgZB6f0ww_48BQ2NGS-VMThpe1Jo046zWbJ89zs7cQZhuwthzQefLRt4TKoqxloAjEbOqyH0YktR7BFEx43XCNEj4HDJtv9Kcy68iazGDiYvq5T2IWzMYCCQPSj44N_0voFKSn2HJN_sGt5UgI9d5SnaJCJGzmKYqRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70600" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70599">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=LahEsIEJXBRwTxLzF6TeTdO6c7C5pLTpD5C1_YjAi18RNeFpNpvG_q48MmDefr90dGabZaCQ9H0k5DgPVhqQb_Vj42WsyEZL_t1g6IXiR9wg1CMi_ZY4jps4HEeobQqLgC4Z6Wqo0AhZSPcmNWLxZn_yAFNL8r6bqKwZAXSRljBvP-55HZTrZ0CLMNwiEPujvV7cmUhvw6cXUGH331V_1RMKrkrYvxUjUozXKiuFnTZb5ijrHlONm9v9bhFZuPmjAiTAxeThYFk3cPUFSjDXrGdLwPY-p13vs9TvIuj0WlkKo-LubAhwoN7QZdbVvKcow1xC3wjKZCF6cqQ5CIu61Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=LahEsIEJXBRwTxLzF6TeTdO6c7C5pLTpD5C1_YjAi18RNeFpNpvG_q48MmDefr90dGabZaCQ9H0k5DgPVhqQb_Vj42WsyEZL_t1g6IXiR9wg1CMi_ZY4jps4HEeobQqLgC4Z6Wqo0AhZSPcmNWLxZn_yAFNL8r6bqKwZAXSRljBvP-55HZTrZ0CLMNwiEPujvV7cmUhvw6cXUGH331V_1RMKrkrYvxUjUozXKiuFnTZb5ijrHlONm9v9bhFZuPmjAiTAxeThYFk3cPUFSjDXrGdLwPY-p13vs9TvIuj0WlkKo-LubAhwoN7QZdbVvKcow1xC3wjKZCF6cqQ5CIu61Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای یه آخوند طرفدار حکومت راجب حجاب
:
اگه شما آزادی پوشش داری، ما هم آزادی تجاوز به شما رو داریم
چرا اون کسی که میخواد به زن ها تجاوز کنه آزادی بهش نمیدید؟ آزادی باید بهش بدیم دیگه خودش انتخاب کرده که مزاحم همه بشه
اگه مردم آزاد باشن که هرجور دلشون خواست بیان بیرون پس باید متجاوز ها هم آزاد باشن
چطور میگی قانون باید جلوی متجاوز رو بگیره اما قانونی که باعث بشه لخت و پتی نیای بیرون نباید جلوتو بگیره؟
چطور تو آزاد باشی اون آزاد نباشه
هرکی لخت بیاد بیرون حقش اینه که سرش بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/70599" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70598">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=mgWkeHTGpwabVEO5KqQvBXwjnOO4i8cnhZ0dF3MIMooEnRbmznl_kLaejHwHsgBGjWevnTNW6n6P-5zAt6c_3dP_TCmNRZguytwjSPK-rnv9GVJMcMUux0wYEVRO3rMbdKo251jnQuliahRoKbo3YB7hmwb-bYteOfMKoEZl4ZMt-MN9SDoZFqX6R-Bp57XhizNPgXorroIqSVI83nbVUyOys0RSMfDEacCl-nKGddJ92O7iJBTjMeEyk_OelbjB2NhW5d06N3cspA4j6Oa1vBlD3O33su5RlK11w-T6jyx9_L18Os2zQ3ltBOkk-cOwLqTJho8JO-vdXT3JStcLkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=mgWkeHTGpwabVEO5KqQvBXwjnOO4i8cnhZ0dF3MIMooEnRbmznl_kLaejHwHsgBGjWevnTNW6n6P-5zAt6c_3dP_TCmNRZguytwjSPK-rnv9GVJMcMUux0wYEVRO3rMbdKo251jnQuliahRoKbo3YB7hmwb-bYteOfMKoEZl4ZMt-MN9SDoZFqX6R-Bp57XhizNPgXorroIqSVI83nbVUyOys0RSMfDEacCl-nKGddJ92O7iJBTjMeEyk_OelbjB2NhW5d06N3cspA4j6Oa1vBlD3O33su5RlK11w-T6jyx9_L18Os2zQ3ltBOkk-cOwLqTJho8JO-vdXT3JStcLkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این خانمه داره مشاوره میده یک فرد چطوری با رابطه تریسام کنار بیاد
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/70598" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70597">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=sP9JxhbEjJp9iyn1X0lvVdKEmK1TiqG4EvVTNtnDpyyROTT36xyeMri-Zz2SHfqyO0gh5pZkOrKl0RwakTa6JsditQuE1bIWldPCIDeICY7jJ3SaF8l91cs00horg2BI-L_SvTfFOvYGugGImGLaLpwOIVnAFaXQU05_39Z6m7TCIaNadzwUgtOifR8H0vtR-B6CzbJ37DgEWx2U_odKnq9K1LAtZUAdnj_TQplFsM5lelmDnnbR6_TrEN33VkkS01rXCFHHWbgE4RFvBVVfAMPJKv08wvJP-58m36wVnJ2FT8QIYZva4xeSP4QfnABkQ5xiDhucUWi1-4MOMaILlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=sP9JxhbEjJp9iyn1X0lvVdKEmK1TiqG4EvVTNtnDpyyROTT36xyeMri-Zz2SHfqyO0gh5pZkOrKl0RwakTa6JsditQuE1bIWldPCIDeICY7jJ3SaF8l91cs00horg2BI-L_SvTfFOvYGugGImGLaLpwOIVnAFaXQU05_39Z6m7TCIaNadzwUgtOifR8H0vtR-B6CzbJ37DgEWx2U_odKnq9K1LAtZUAdnj_TQplFsM5lelmDnnbR6_TrEN33VkkS01rXCFHHWbgE4RFvBVVfAMPJKv08wvJP-58m36wVnJ2FT8QIYZva4xeSP4QfnABkQ5xiDhucUWi1-4MOMaILlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
همتی رئیس بانک مرکزی :
علت بالا رفتن قیمت دلار طبیعیه و نوسان های خاص خودشه
ما نمیتونیم بخاطر یک نوسان بیایم مسیرمون عوض کنیم
مسیر ما درسته و خوب جلو میره
اگه این مسیر ما طوری باشه که میان مدت دیدیم درست نشد اصلاحش میکنیم
ولی من معتقدم که این شوک هایی که ایجاد شده جوسازی امریکا هست و شرایط مطمئنن درست میشه و رفع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70597" target="_blank">📅 10:04 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
