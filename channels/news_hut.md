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
<img src="https://cdn4.telesco.pe/file/puVy353vPb7d6UE4Gagx_fYfykHBsEkUqxeYAxpYXLs243-rOQSgE-wioe724d4EHr1uHyCnXaHVC0GBlUj2UEfKHZJPMi6qSMDFkYT1qvxbIZiIFct2pR1bKZYxB4FQYKFhCsHhch2xIc-H9-gX0sq4ItrSWywfIHgQXI5L5Wd7iXf6GbbdXaC8eqv8pnqz_PeGj4ht8v3labKRbIdtZUIUjLNu3I7wm7fF1RPcmy1NsFiDRHcuGaQRJuoCkPAcnTAiQ16QjuHcY-fHA_9updrAW63PsugthGpRpkyGy48KYAf70-HAtSdFtuqyPL8ATWsOguX1957MytrI_eFdfg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 224K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-25 03:12:55</div>
<hr>

<div class="tg-post" id="msg-66143">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🚨
ترامپ به نیویورک تایمز :
اگر توافق هسته ای شکست بخورد، حملات نظامی را از سر خواهیم گرفت یا در ازای ۲۰٪ از درآمدهای منطقه، واشنگتن را به نگهبان منطقه تبدیل خواهم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 1.15K · <a href="https://t.me/news_hut/66143" target="_blank">📅 03:09 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66142">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=Doxdxo_d_h3z5v6cFsfr7LVwRQXOerNXQ6zWzEiB6LwnmLV29DuQSOCYaO3Z-oTVOKtuJSuWmdvY3ji9VQg7dg5iVNh6gkgU82c2oHsk8RiglFQWLGkUSseniYLcPylDy0wJAGGbCbWWNDz3orDhtERPghB6Zj6LRtwWqtrFHPUDqe2a5tT_8mExTghgoJs_pc-blm1JFvBKLXgxM_tsv8mCHmRIR0g_st2DvkZqFu6JMKU3OGQFaub3kcJ3P7MayXzwQ0HoqdXKGzusEG4qC6GGSAOZWE7J7JW1L2hUiYSCdovKJIfG1oFXPbthxLpnQz7a8Kz_3qBGT8zsPdHqdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c39322d55.mp4?token=Doxdxo_d_h3z5v6cFsfr7LVwRQXOerNXQ6zWzEiB6LwnmLV29DuQSOCYaO3Z-oTVOKtuJSuWmdvY3ji9VQg7dg5iVNh6gkgU82c2oHsk8RiglFQWLGkUSseniYLcPylDy0wJAGGbCbWWNDz3orDhtERPghB6Zj6LRtwWqtrFHPUDqe2a5tT_8mExTghgoJs_pc-blm1JFvBKLXgxM_tsv8mCHmRIR0g_st2DvkZqFu6JMKU3OGQFaub3kcJ3P7MayXzwQ0HoqdXKGzusEG4qC6GGSAOZWE7J7JW1L2hUiYSCdovKJIfG1oFXPbthxLpnQz7a8Kz_3qBGT8zsPdHqdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شادی مردم لبنان و نوچه‌های جمهوری اسلامی پس از اعلام توافق ایران و آمریکا
و عدم حملات از سوی اسرائیل
@News_Hut</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/news_hut/66142" target="_blank">📅 02:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66141">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">‼️
جزئیاتی از یادداشت تفاهم ایران و آمریکا:
در جزئیات یادداشت تفاهم ایران و آمریکا این گونه که پاکستان مدعی است بر لغو تحریم‌های ایران تاکید شده است.
طبق گفته پاکستان، آزادسازی بخشی از دارایی‌های مسدود شده ایران از ۲۸ میلیارد دلار، بین ۱۰ تا ۱۴ میلیارد دلار آزاد خواهد شد.
آتش‌بس کامل در تمام مناطق و خروج ارتش اسرائیل از جنوب لبنان اعلام شده است.
همچنین به پرونده اورانیوم غنی سازی شده اشاره و آمده است اورانیوم و همچنین تأسیسات هسته‌ای ایران در ایران باقی خواهد ماند.
طبق این جزئیات، یک صندوق غرامت ۳۰۰ میلیارد دلاری برای ایران تأسیس خواهد شد. تحریم‌های آمریکا علیه ایران لغو خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/news_hut/66141" target="_blank">📅 02:20 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66140">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nToN9D3sGMXz-GcMiHdOz_TTI9qPxP8l2Dt6cp4E1Q0J8eVS4A9eX90zq1dSrBvcp7IRMf7EIWg5f2x9xRsxcOOWrUhbcxF46sl_sNO9U5aiuAf-78WxRoQu0fWPUFINaTiSfgBaKNPiZjR4WxCn5lHIIzP7zq2nLTN8r2AcjB80mznDe5MpL7gXF7vwkKzttFFP7HqKiJE_J1L6NbWtS3_9uq6F3pGJTHUUDeV-53rxdCHjhZMuH_gJ3sbgq9h2D977rJctd2u5n54hinQyLWLlypxo3ROhru3sTazJdBTyBrKDoRtBKv_bWe3N9A55nVveK5_5hZzL_gamPOmX1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ:
این توافق بزرگ، صلح و امنیت را برای سراسر منطقه به ارمغان خواهد آورد. بسیاری از رؤسای‌جمهور تلاش کردند با ایران صلح کنند، اما همگی پیش از من شکست خوردند. رهبران منطقه برای نخستین بار، رئیس‌جمهوری را یافته‌اند که می‌تواند به آنان در دستیابی به صلحی واقعی کمک کند. با بازگشایی تنگه پس از امضای توافق در روز جمعه، به‌منظور رفع موانع مورد نظر من، نفت دوباره از هر دو سو برای منطقه و جهان جریان خواهد یافت!
@News_Hut</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/news_hut/66140" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66139">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/news_hut/66139" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66138">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/frOPIMJ-exzuG3hp2xICYScYscvYr9Zpp9qcCw7nY2MrlUD0F17KFrQvT0b9C9DXW8UlQgYLC1WWoEoyXyzO_9sA5tyjTu0UslN6ZzC9XLFRTJB-JrHkpa1ESOreYnSm3E0J0lIBhWBaVwc1qhgU7URBXK9xkhynPfgAzWflIHc9aiuwheXc4k-LbAsZgDJZy8lUR6xLaoss7OZ6W5gu3zQa_C4dfVfd9hiDNz7MaxNQeDecZqFyU3I7522S6TM3GEonnqj1L50V1bFZnYa7h4AThXD9P-8BlD6LIZkr_7AOjPcQekP4hgqnDuR0a3IXU6kj-kDBtWK_Dwjcb_uiXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/news_hut/66138" target="_blank">📅 02:06 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66137">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nonGkhbGYWtRzBiLBQZHPHPvK6B14KreCJLA3K0nwccv2iGDxoPJItw-OsRYeIoxGj4WgWUrOvY1LMgzXRw6NA0pI3rUbfO6QqbP7GfNJXecY4UE7WKYQZixSzpsvMamvAAxLpIoG98LuKyuXc4-7wMCZ-8bH0FN5JvOrAvFccJPjk-PBlslfB4KFed6YcPUuGmfljl6lPV0aiPad0TQZF-oWyEGyDS730dSqnroM7ARofLBnPx7KIBwGRpFVyEeigwNZv_Fjy8ZeFCwFuG4VcFLo7CKjJkDdTE7qk0qwJye-xy1K_gJx2RghBr3BJvgJoTKx_H63d1YPZ7x2XLnEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تیتر شبکه خبر همراه با این تصویر
😂
@News_Hut</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/news_hut/66137" target="_blank">📅 01:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66136">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=Lx7MTuz4ygwZMru7pFTWorDN-rJ9_bBHatgC7aTNKeME4IpHXKRUS0gntt-lMTpmHoUDuRFeMi8LrbA3gHTlM-3w1T8441Gg_I4SDtRzG7noZtFHzi0VDbsIF5NXqCgEWOhcKPV8g7JCw2o385JTrj4UNAj2Yh-ykABV54qJYgHcExxvXbgIIj9IjIyxI9sVbhzavURflJz8K0LLcI4PAZH-I0vNs8GNFYzLEv0xEjL5KjNV6eXxhKmH5ZgWo-kXP81W4dZTKqPL7LbMYifg-gyGnG0EXSepPRw3tkHQpBs0lBMA4nRgkHBnABI_BXQgCMc8gSBvG35N7CAs3orupQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb0ba1bd70.mp4?token=Lx7MTuz4ygwZMru7pFTWorDN-rJ9_bBHatgC7aTNKeME4IpHXKRUS0gntt-lMTpmHoUDuRFeMi8LrbA3gHTlM-3w1T8441Gg_I4SDtRzG7noZtFHzi0VDbsIF5NXqCgEWOhcKPV8g7JCw2o385JTrj4UNAj2Yh-ykABV54qJYgHcExxvXbgIIj9IjIyxI9sVbhzavURflJz8K0LLcI4PAZH-I0vNs8GNFYzLEv0xEjL5KjNV6eXxhKmH5ZgWo-kXP81W4dZTKqPL7LbMYifg-gyGnG0EXSepPRw3tkHQpBs0lBMA4nRgkHBnABI_BXQgCMc8gSBvG35N7CAs3orupQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
علی‌خامنه‌ای یازده روز قبل از ترور:
امام حسین فرمود کسی مثل من با کسی مثل یزید بیعت نمیکنه: ملت ماهم بیعت نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/66136" target="_blank">📅 01:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66134">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=Aoqg-LK7I23gDpSZU2Ld-Jz2DfbOWP2g_gF2WPu_JYUJ-1bq1tcTC7yZVuHTvI6TsqV_JLJuX39kSebe-AkFLYGD52sO6ZPz-LTfDe6Nzonl_khVq2fK0SxXfi5Z_we8ZHETTqaft805iLQHycwZKYERjs6kYDzi0B0w6GLf_I-TwkXEb3zTpFm1xbiQ1oi5Po9hyreDWVgQf8ya5nm5Luozr-jetXBesJnzCXG8Bjg3ODxq1d53axc-pQoAb9hGv0NNnviXdrnUaanc7bGef1B1QaSMk9NtAzM1Jn_FGSQ7fLrmSNWjRvLKxAu_NEQnEhk_X6-wINVz_j63-Enixg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/616572f1d7.mp4?token=Aoqg-LK7I23gDpSZU2Ld-Jz2DfbOWP2g_gF2WPu_JYUJ-1bq1tcTC7yZVuHTvI6TsqV_JLJuX39kSebe-AkFLYGD52sO6ZPz-LTfDe6Nzonl_khVq2fK0SxXfi5Z_we8ZHETTqaft805iLQHycwZKYERjs6kYDzi0B0w6GLf_I-TwkXEb3zTpFm1xbiQ1oi5Po9hyreDWVgQf8ya5nm5Luozr-jetXBesJnzCXG8Bjg3ODxq1d53axc-pQoAb9hGv0NNnviXdrnUaanc7bGef1B1QaSMk9NtAzM1Jn_FGSQ7fLrmSNWjRvLKxAu_NEQnEhk_X6-wINVz_j63-Enixg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اگر این توافق جمعه امضا بشه تازه میرسیم به شروع سناریو زنده یاد مانوک خدابخشیان.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/66134" target="_blank">📅 01:33 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66133">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🚨
‼️
دبیرخانه شورای عالی امنیت ملی جمهوری اسلامی
:
آماده حمله سهمگین به اسرائیل بودیم اما به درخواست ترامپ و پس از گرفتن امتیازات لازم، از انجام این کار منصرف شده و‌ توافق صلح را پذیرفتیم
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66133" target="_blank">📅 01:23 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66132">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44bd274791.mp4?token=bvyA4xteRxK0a6Yno_1w1QBSPG_ncIBxQq0WuKqp512rXTOEPWvEs8JA0Ezx-jlLWY0iAXGibhhWwLfreULIOcs5BCD3dEWgTuwIlKwSHzPPvST_13qH1eMSTqKT-JIbx3LkM0ZM2VD0ITyM3KIv9vIBpC5umrGOVz-rUQynei6v90sgIuxOY_pK_Ai9p_g0Ng_TEPh1IdYFJNAi4mlawhZAx40sBQ5ssTyspS1ITVBQG75aM_9AVwOcDQMYoGlR08fJhOp8FTV_nVnzoHBNgtTYKPMuUnZHI5lwtcfXTAkJDiGfTiknbJP3kuCMnK3MJZHgb_j7wnMNeN3qT-KCBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44bd274791.mp4?token=bvyA4xteRxK0a6Yno_1w1QBSPG_ncIBxQq0WuKqp512rXTOEPWvEs8JA0Ezx-jlLWY0iAXGibhhWwLfreULIOcs5BCD3dEWgTuwIlKwSHzPPvST_13qH1eMSTqKT-JIbx3LkM0ZM2VD0ITyM3KIv9vIBpC5umrGOVz-rUQynei6v90sgIuxOY_pK_Ai9p_g0Ng_TEPh1IdYFJNAi4mlawhZAx40sBQ5ssTyspS1ITVBQG75aM_9AVwOcDQMYoGlR08fJhOp8FTV_nVnzoHBNgtTYKPMuUnZHI5lwtcfXTAkJDiGfTiknbJP3kuCMnK3MJZHgb_j7wnMNeN3qT-KCBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
دود سفید در کاخ سفید. طبق سنت، این به معنای امضای توافق‌نامه صلح جدید است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/66132" target="_blank">📅 01:22 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66131">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
📰
تسنیم: تا دقایقی دیگر مسئولان ایرانی درباره خبرهای منتشره راجع به تفاهم صحبت خواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/66131" target="_blank">📅 01:18 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66130">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3KVJoOh7BzKMyNl2S25KC9By8x0Ne3aoCBYpnp_Ews6UXzs9I-RVu7Vn7imzo_Row66Smr52p362un8o6byi93NnIyjda8Zjw0fSyxTgUV35ORldVVuA4KqQ-eGW4InbW-a7BVlpiiUentIdWCNNwCoNW1CxoAuzddgFxW4JlPLpRr8Sv-gTDsNEiCYFuZvDGRdxg38U79V6B-vc1f35G5M_hZFs0os_D88qDVps1A-cHyqKCMNSQfyZ7x9t8l6lu6zYkYnpk3uOXb6eEayMMUR9_0DeyE3nSBgXnyUB-2MN4t9HZY__HuhxAHnhA1n_uBXnbpnuDOemOo1HyVqjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
یکی جلو صداوسیما رو بگیره. چند دقیقه دیگه تیتر میزنه آمریکا رو نابود کردیم
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/66130" target="_blank">📅 01:16 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66129">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co6EiFZYJfMR3K4y_53eVLYJt95qpCQjdA99ZgJuDYGZgsNQ0StqEv66Z-lg9TXRrGP-EEwQYRhA_jD_Oewy6rmUUldUuFVsC_qN06pWwbTNlKlHOyK8GkN_Q8EwcmO9OXg5dUXYANPeWW1lHITsSVyJLb2ZJHg_vDhD7EKJlAyT-paSgiA-oeCCG80zF4GoOh3wMSgKd3whEv8MW-C3jot9AgmDaY5Tw6cKFzPwVng1Z6geceyCXQAq1qDpCxUZhphg3ZzKFdUTzJwwWpBdldiuHI7liLdtXcCx-QwHLaSoEV9OQinoTMPDtmHd2mbtbVYspAH-a3YzE-aL2zvIQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان وقت چیه؟ آفرین حمله به ضاحیه بیروت
😁
#hjAly‌</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/66129" target="_blank">📅 01:15 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66128">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/66128" target="_blank">📅 01:13 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66127">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFb6kYGslc9U1ukaw6Cx13FG6gooS6a8ZfvkbM_S6fFcn8KdHEq4WqC3ai9ct0HSeYKCyYXxFK2XNVgW_lA-e2RCZggx-HtdGbm82Cm6MJ1LZzMb1PrSkD0RUC2SfXOEcRn_023ZhAdPeEopkTvHd2y4-niiUF3jidtnH4erUAHetfQFsXVDktbcqGTR1zkc3-WXe4ytXvsB3TOEITWCjBY6N34paLQVAU4fNBps0MNEJ-pgHujCGhBiIzVoMQdve0F3lntk3VQXDdPzd5ioJ3N6CVfy9z20t1Zw1CP-FsnY8JfgKKVYZCVfKR-a7Vur8Vy1tJb7YLOdrB7l9obDPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتقام خون رهبرتون گرفته شد برید خونه حالا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/66127" target="_blank">📅 01:12 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66126">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=F4frzzq2UEVmLDFWOdgSgoyqcu1N-msfXSHU_vFLPqyAZnbyPN8JXwcDlNkCXBz9FIJ_yHTtWUVkA8T_tnZH4XTfMiWoMjrct_002DMGhYY6tWH0KsMurSVzt77rrvgBn0uzZSZPoTDMNrrO1rUc0hd5oF8jPREqUvV26a3Zr48OvHhpgQ13g-2tV8zX1Qghkowgu-E1JzsXmouZB2Iq9NvDfMd-uPUR89fJrai_b9828TypJZyW7qXKQsUAJCdpYsnOaYa73WMY822FvCmhMFxmR4RE1I0lP_kavZRgQnL5XZgkp-r7od0dgl_kvePaGF6p6YA9SWLUSpA5Au2FQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/960c47a55d.mp4?token=F4frzzq2UEVmLDFWOdgSgoyqcu1N-msfXSHU_vFLPqyAZnbyPN8JXwcDlNkCXBz9FIJ_yHTtWUVkA8T_tnZH4XTfMiWoMjrct_002DMGhYY6tWH0KsMurSVzt77rrvgBn0uzZSZPoTDMNrrO1rUc0hd5oF8jPREqUvV26a3Zr48OvHhpgQ13g-2tV8zX1Qghkowgu-E1JzsXmouZB2Iq9NvDfMd-uPUR89fJrai_b9828TypJZyW7qXKQsUAJCdpYsnOaYa73WMY822FvCmhMFxmR4RE1I0lP_kavZRgQnL5XZgkp-r7od0dgl_kvePaGF6p6YA9SWLUSpA5Au2FQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اولین واکنش مجری شبکه خبر به امضای توافق
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66126" target="_blank">📅 01:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66125">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBrv_6IML-DM1RgcB_FIA7p8qvPQ6gmMJ43UDafpfMXEsrjQr5HMqfPW7CkGD__yOWn3BMyFNgg8IllAI6TAtNFwCOhmpdXBKewy-856G12-hliBjpDa2wQUqglLxhPd0KXf7PCIqN9O1D2YGOZZZSthlwC-UqoYP7s1bltSYPooXtmPUvnrvxRXnmka7XbFY60S9KS0F_O2xOLY_PjCLeAcJ2RIk5R5GdZl2NzFZgzJaZlXAeQHSWQScD9l0U3sUmWJ81JIiSuqRIoU4_cqhMNL93W70WRO_0E2AtPOTYeSl-c9LKW9A2PfG1uGRk0C4qpIBRHqGGn8f3eP6j7ryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
#فوووری
؛ ترامپ:
🔹
توافق با جمهوری اسلامی ایران نهایی شد. به همه تبریک می‌گویم! بدین‌وسیله من به طور کامل اجازه بازگشایی بدون عوارض تنگه هرمز را می‌دهم و همزمان اجازه رفع فوری محاصره دریایی ایالات متحده را صادر می‌کنم.
🔹
کشتی‌های صلح، موتورهای خود را روشن کنید. بگذارید نفت جریان یابد! رئیس‌جمهور دونالد ج. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/66125" target="_blank">📅 01:02 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66124">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UQTKO9h-ch08lRYQaSfFLa6iizaU_0dLAQRSN5q9XLHfe2Y2jVEi1sfSN2qxc1ym40ILnrUKu3Y6J6mxFNYxwxFB881l1jTwZoDi_2RfFDHxGsfErnpZ2Lx59u1Nom872bCSPpeaQkmTZWBSNEGTKn3d-o5U0kCpnYgsWkmDSNcMtUsiuy8iYl5TSE0B5236oWCHAOt00bFf-1OJvfJB0lnbcQ4YP-NgddVHpDpt-eM1QMJ0Jb_6G-LPBhAc7UEFht5WcoeH5JrEMqB6ENutvNqdgjgqCIjYLQbF1zMnnFqgc5ZIvvb16oX3mhbx8RlSaQI8dmQsX2xP6KN5mNoVDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زیر نویس شبکه خبر:توافق با آمریکا انجام شد
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/66124" target="_blank">📅 00:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66123">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
🚨
🚨
مراسم رسمی امضای توافق روز جمعه 19ژوئن در سوییس برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/66123" target="_blank">📅 00:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66122">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
🇵🇰
🇵🇰
شهباز شریف نخست وزیر پاکستان:
پس از مذاکرات فشرده، خوشحالیم اعلام کنیم که به توافق صلح بین ایالات متحده آمریکا و جمهوری اسلامی ایران دست یافته‌ایم. دو طرف اعلام کرده‌اند که عملیات نظامی در تمام جبهه‌ها، از جمله در لبنان، به طور فوری و دائمی متوقف خواهد شد.
مراسم امضای رسمی این توافق‌نامه روز جمعه ۱۹ ژوئن در سوئیس برگزار خواهد شد.
از ایالات متحده آمریکا و جمهوری اسلامی ایران به خاطر تعهدشان به یافتن راه‌حلی دیپلماتیک برای این منازعه صمیمانه تشکر می‌کنیم. همچنین از برادرانمان در تلاش‌های میانجیگری و رهبری خردمندانه کشور قطر برای حمایت‌شان در رسیدن به این توافق قدردانی می‌نماییم. به طور ویژه از رهبری خردمندانه عربستان سعودی و جمهوری ترکیه برای مشارکت‌های ارزشمندشان در این زمینه تشکر می‌کنیم.
پس از امضای توافق‌نامه، میانجی‌ها تسهیل‌کننده سلسله‌ای از جلسات در این هفته خواهند بود. این بحث‌های مقدماتی پیش از اجرا، پایه و اساس مذاکرات فنی و مراسم امضای رسمی را فراهم خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/66122" target="_blank">📅 00:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66121">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
نتانیاهو از این توافق حمایت می کند و این برای او خوب است زیرا تحت هر شرایطی مانع از دستیابی ایران به سلاح هسته ای می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66121" target="_blank">📅 00:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66120">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
محاصره دریایی اعمال شده علیه ایران موفقیت‌آمیز و قدرتمندتر از حملات است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66120" target="_blank">📅 00:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66119">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ:
من هرگز به تغییر رژیم در ایران علاقه‌ای نداشته‌ام و در حال حاضر با گروه سوم که منطقی‌ترین هستند، سر و کار داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66119" target="_blank">📅 00:45 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66118">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
ترامپ: ایران در ازای توافق پول نقد دریافت نخواهد کرد، اما ممکن است تحریم‌ها کاهش یابد
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/66118" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66117">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
ما وقتی آماده باشیم، مواد هسته‌ای را دریافت خواهیم کرد و این اتفاق ظرف یک یا دو ماه رخ خواهد داد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/66117" target="_blank">📅 00:44 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66116">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهات نیوز | HotNews</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsWlZQUzPUEoc4jIjnVGh_CYSMtuz3oDRP1uRzMhmfsYkREoJBZyXcam-8OPlCXGn5v5QXFjd_xo379o4ZCIJiOrTFGPSVVbG3Mvvc0iw7A__ktf0Yry1ueCACI7FDv9UfQHIu8vNugBuW0J_Q3cdExON3WlyfLMJibId7YBXLbD219QqNzV-m9P1EF8PIQlE6vq_OsSkhAIPhcgZ0ikjl9n4jmX-dkqmCSBKB_uLK2btXubOGN53JB6gFfBpfGurtS5b63ZV2Qr-VZOtbOnVj8agdWiGPprbhkSRkH3YLFRNmeLVc11WyAH_dhytJMFx-f72K41umk-S9s-gq3YFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محتوای تماس بی‌بی با ترامپ:
#hjAly‌</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/66116" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66115">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ و نتانیاهو دقایقی پیش به صورت تلفنی گفتگو کردند
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/66115" target="_blank">📅 00:43 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66114">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
ترامپ: این توافق به صورت الکترونیکی، یا توسط من یا معاون رئیس جمهور ونس، امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/66114" target="_blank">📅 00:42 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66113">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ به وال استریت ژورنال:
بزودی بیانه ای صادر خواهم کرد تا تایید کنم ایالات متحده با توافق با ایران موافق کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/66113" target="_blank">📅 00:41 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66112">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
#غیررسمی؛تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید.  @News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/66112" target="_blank">📅 00:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66111">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dh6Vc1QVzTMhSJRMYg_TjPvA-Ns0qI1H7EENylIcPETt12BAA9kX6xGWVtu9BspHnnQcK9UWI93XJi5p3aPd-_Geff33kHxnHtVST0hV9UM-JlJpY5MRbk3gMsaLc99coV2ndTkV5Xr3R7eXLYIso8psmdA-QJK7zxNN81RQRogSda6FQU_92df1RH6my4v2l7O-2SJSoPhH-ocXs7uBlG5ixpnpaGNMrtuOjBtRJQxxXpCB2BLlhPXqXfZM5RJZB9sU2aolnP0kCdxbUSSw8AvKcIMFgRm1itQUf8gh-gJ5PcK_ZPEuvQ4AeX3erUROv3oz_tKa6tJ5Dp9rWtaWOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
توییت وزیر کشور پاکستان: الله اکبر.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/66111" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66110">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc582fcae.mp4?token=dF0uTJFPyQ_2pDohy9PDWZ1sefkle8jEKxP9e7oeAXWYEgv6jFOaSOLjh74_MmVYHI-mqN19JWD6DRlyJi4NQeS83EFXJdQmjcrnMe9J_AyvtC6ufDsvHc6BSXCBLRlzASEyDCzcM0OrFoA5uhbL-xLPD68QSCSTUcmiif2damVC-vWcXcMQZ3vlpDsycMHb5rQ8IPUnzPDd6fUFdXsFrbvml0cv3XLB9Vsl2ES1mPQesRa0m0LCxUOWQTYiM-n_DWAxYBFuE2YbHvt1kUTpY6gw4NcvRnYy9T0geMuMOv7xXk6GyWljaesI_xQYgGjurKtsuvkYoxy6LIjB7vaaTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc582fcae.mp4?token=dF0uTJFPyQ_2pDohy9PDWZ1sefkle8jEKxP9e7oeAXWYEgv6jFOaSOLjh74_MmVYHI-mqN19JWD6DRlyJi4NQeS83EFXJdQmjcrnMe9J_AyvtC6ufDsvHc6BSXCBLRlzASEyDCzcM0OrFoA5uhbL-xLPD68QSCSTUcmiif2damVC-vWcXcMQZ3vlpDsycMHb5rQ8IPUnzPDd6fUFdXsFrbvml0cv3XLB9Vsl2ES1mPQesRa0m0LCxUOWQTYiM-n_DWAxYBFuE2YbHvt1kUTpY6gw4NcvRnYy9T0geMuMOv7xXk6GyWljaesI_xQYgGjurKtsuvkYoxy6LIjB7vaaTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صداوسیما تو لبنان:
انشاالله امشب قراره ایران، یمن و حزب‌الله به صورت همزمان به اسرائیل حمله کنن و انتقام بگیرن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/66110" target="_blank">📅 00:39 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66109">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
⭕️
#غیررسمی
؛
تفاهم مشترک ایران و آمریکا به امضای دو کشور رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/66109" target="_blank">📅 00:36 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66108">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q87RkcdzYMBSJD7JVJx1wvcPczTP8AaraPNp6nKJxVhmoUstwpbeTlcCQq_x7kqCWFD8CVqiWutgEwSPBNU3u2uXNbgnHbF5dD37E6_GifBEbDgaqxNeKO30AzERZhLD0PgZurcR1wU0_5LeVf0ZKE47jeqD2K4ni4-Pi7JdzHkci0L_fUcL1SpG7P5r4xHZtsbmFLvK6ZbJM30HRZm45LnJC4Jf6wPivLq2akXu9wz5ZsDZMT0zxiYNSCgd5HCWO6RAnb3vnd4VRkTAj2QkCqS2KUwK1uVI8BHzcp73ZH18Ad6znT09Jr1UN4bf1r4rNItX6O5vPrkPa3gxj5nGIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پرزیدنت ترامپ از طریق Truth Social:
ایران هرگز سلاح هسته ای نخواهد داشت و تنگه هرمز به زودی برای تجارت باز خواهد شد!!!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/66108" target="_blank">📅 00:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66107">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
🚨
#فوری
؛ ynet:
ترامپ در حال آماده‌سازی برای برداشتن فوری محاصره دریایی آمریکا بر بنادر ایران باشد تا از هرگونه حمله ایران به اسرائیل جلوگیری کند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66107" target="_blank">📅 23:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66106">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">محمد باقر قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان لبنان و دیپلماسی مقتدرانه جمهوری اسلامی‌ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/66106" target="_blank">📅 23:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66105">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بشتابیدددد که فاک بت آنالیز از بازی ژاپن و هلند گذاشته سریععع بیایید و ازش استفاده کنید
💸
@FutballFuckBet
💸
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66105" target="_blank">📅 23:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66104">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
کابینه اسرائیل:
اگر ایران حمله کند، ما نیز حمله خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66104" target="_blank">📅 23:10 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66103">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FRAKeRc_0WgTlbQb0Fo1Cm8JV7SraXImCLBGlN3PtHiJLE-WtBK5dntN7gp3AZEkj21Ta8ghusgBRDNaTLvOyc-ZMZfll9eZC8fwRNR73PUMKbGVlQl5fCMHonVOue9nPrJ2mJPWu9nzO7kx8DfourEWRrcudWFZd9gQECusRYuvTBMDUFN4lwb-Q9BcIqMZ9IDjwAju-DMnM9HMyL4GbskkJYBuXHWhC-3p6qEehIVoVqS_-utlPlyyRF44pD8T-crHX7iq0kf7BpCWh4gX4VJ-0771x59fVA2dNa7_2KoJ9ayIDki3WpHCV-7t9_mO7qmKzylR0xYJdJxRmdX9Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حضور هیتلر در ورزشگاه و حمایت از تیم ملی آلمان.
آلمان این بازی رو۷/۱ برد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66103" target="_blank">📅 22:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66102">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Me8NL2J2d_jrUy4OZ_tJtZ0Xl6W_lV2TA8t6mAN9etut_a2UMQElOTfcghOhU93l1OU-DUcQfcNUXysSp4uTmRfqooXgyOUWmMVqxIgfW0HohlAejeHz8abOln0uQEa1uTUFEp0rruezJqG54B0roJeN0vATnFkfrdTodNsu7OvduzDAFKsBcAWxnAWgB3aWMoPa_DR_yt8-_vP8k8J3Fw25dIAOV_XpHSFJPQg47tssOnUg3mELH6NbOqXZR9p-wUfgXtVCfvL7ItNdwVtYhcqv3vIfNFNCVoLZFSCa6dPOtERbmbPtLFRaxA_owmoGQH46jgIL1u9czm5h3wHTXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قالیباف:
هرگز نمی‌توانند هیچ بخشی از ارکان مقاومت را تک و تنها گیر بیاورند؛ مجاهدت‌های رزمندگان غیور لبنان و دیپلماسی مقتدرانهٔ جمهوری اسلامی ایران حاکمیت و تمامیت ارضی لبنان عزیز را تضمین می‌کند و بساط دیوانه‌بازی و جنگ‌افروزی رژیم اسرائیل را بر هم خواهد زد، بچرخ تا بچرخیم.
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66102" target="_blank">📅 22:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66101">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
به گزارش Ynet:
نتانیاهو درخواست‌های ترامپ برای توقف آتش‌بس علیه لبنان و عقب‌نشینی نیروهای ارتش اسرائیل از این کشور را رد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66101" target="_blank">📅 22:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66100">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
🚨
خبرگزاری تسنیم: حریم هوایی غرب ایران بسته، و تمام پروازها در این مسیر لغو شده.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66100" target="_blank">📅 22:24 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66099">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0112560fb5.mp4?token=DjvV2CfAD0GE0xD6uKhR3WS6IvQN_SoYVayoZXDvnuGyGbJKx2zCHGclO176O5pN-RxOsDXYDVbZKkW_3EOqHn1iUxZgXd5T96dYS4iBo5umJqDx8S38Sa_wVR0JzgNgjz8WOrbUlkkyQQAEvMqAwtlN_oisVHkiDVBz-UBt7GojE0PnXQYpu1cMhO0wDyflmsghpo7C2Toe46rRNRpgY4Jyz8Sl6vXDZruIrlU7ui5YBqokW1PN3iP-b88jbVmEtHilYAU5Mbm33DEyEMLPzIQqYCd6DSMPRsxxMxzvb6WIT6a9toJKFr02qu0WuoBmITl7ep2Ey_fbrNW6hvl5dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0112560fb5.mp4?token=DjvV2CfAD0GE0xD6uKhR3WS6IvQN_SoYVayoZXDvnuGyGbJKx2zCHGclO176O5pN-RxOsDXYDVbZKkW_3EOqHn1iUxZgXd5T96dYS4iBo5umJqDx8S38Sa_wVR0JzgNgjz8WOrbUlkkyQQAEvMqAwtlN_oisVHkiDVBz-UBt7GojE0PnXQYpu1cMhO0wDyflmsghpo7C2Toe46rRNRpgY4Jyz8Sl6vXDZruIrlU7ui5YBqokW1PN3iP-b88jbVmEtHilYAU5Mbm33DEyEMLPzIQqYCd6DSMPRsxxMxzvb6WIT6a9toJKFr02qu0WuoBmITl7ep2Ey_fbrNW6hvl5dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شعار تجمع کنندگان تندرو
عراقچی بی غیرت اعدام باید گردد
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66099" target="_blank">📅 22:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66098">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
#فوری
؛لغو پروازهای غرب کشور تا اطلاع ثانوی رسما تایید شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66098" target="_blank">📅 22:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66097">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nvCgiJHguvP2tqjxKz-iC1dF3nurqtkkOeisY3Omt_2kbQdbw-SbBrLmvUucr6m8ZhndulWUUZotEq2aLd51cyYdqK3jCBdZp4CI_A3Ccpi4i5Y3Piau-6oKclodbXSVzQVW_WC3wUmd_xmR9Ki5-YnRKeEvPKwO3rZXNFKHZJv99KxcVe9X6mf2IfI_V5UdpQx5pPLCO9xAa14vUjOJDMJMzCczD5Z0wxVpXwWspCsKH13DqsAR2NLrVrzGHqBSfAcFHtKJ1NbCB1u6XqkCPuC-CJxihk7sJVPxfo6yVOILu2rjHRpMGnriHuRsm7kkWh3P1Fw132nKir7y_KosNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
به نظر میرسه ایران حریم هواییش رو بسته.
«هنوز به صورت رسمی اعلام نکردن»
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/66097" target="_blank">📅 22:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66096">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه #hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66096" target="_blank">📅 22:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66095">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
حنظله:
تا ساعاتی دیگر، آغاز خروش آتش های سریع و خشن، به نقاط جدید الکشف حنظله در آسمان تاریک سرزمین های اشغال شده، هم اکنون به پناهگاه مراجعه کنید. شاید هنگام فرار حوادث دیگری رخ دهد!
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66095" target="_blank">📅 21:47 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66094">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🚨
یدیعوت آحارونوت:
ایران خبر درخواست ترامپ برای عدم حمله به اسرائیل در ازای مزایا در توافق را رد کرده و گفته است که به اسرائیل پاسخ خواهد داد
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66094" target="_blank">📅 21:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66093">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
زیرنویس شبکه خبر:
پاسخ به حمله اسرائیل قطعی است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66093" target="_blank">📅 21:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66092">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AhRwEQ4K0SH8mwiHVeURiAm_b-cHjLi4KGqmxjuq5nzU3gmQ-6pxEF-Q3IP9wc6AdXzLFtaqiheV0xcayMiLB4NaM0OUAXzVjfTZMrE6d3w9IEvdQnPiWL_Hnw35foKGRphI4YioV6LhsqP-Xx3rKo59A8avIVh-Te18_fQCxIFlP1iikpGuv4q-3u7n42TNlXY08E9IUu92wvOEWjnZQroENLTAYs0itLIx8__yra14taOUVogHeuhj0zONgQRPiGur98pXIJmQ-yj2pKGOJT7tEOeL-aN3JXUk4TB4xuUCiUWhITJGTcbPm8HnoPRDsilMOJeGmWMIhH_Mp7_12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمدباقر ذوالقدر دبیر شورای عالی امنیت ملی:
‏
پاسخ رزمندگان اسلام در پیش است.
وحدت میدان‌ها یک زنجیره امنیتی در دفاع از منطقه ایجاد کرده است.
لبنان جان ماست و نقض خطوط قرمز جمهوری اسلامی تحمل نخواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66092" target="_blank">📅 21:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66091">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ افتاده به دست و پای بکن‌ ملانیا (سردار وحیدی ) و ازش خواسته به اسرائیل حمله نکنه
#hjAly‌</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66091" target="_blank">📅 20:12 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66090">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOnZxYsNcbowskh25nP8sQUPWot1XNnwIPHTCdbp7b2grziEOmh9oyq7xSHUCBrlKuNXMOLNqQsFMibT97bMegzNbS12N5IG6nt-YbDSZ6PpKum13kdfGkT2qH58NsQPcSsOnWguBjVvfdHLqxUVd2mnsXei2pXf18TbdDK9LFBNa7uoAVa_axzMF_cBhVs7v654xpuVNuyhksDspfOTSXbcTQzEitgeChsh4bnTW76uNIh9o4ICwP9g0rhioeEQU1_U3MeZH1k9CZV6Y3rIAaQIVVVXJ6GR15Yr9gWcgQtO4c5kgqHywBV6GlS-ZK0fE2eJoIKHbwx-m18z7b7azA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئیس کمیسیون امنیت ملی مجلس: پاسخ به حمله امروز اسرائیل قطعی است
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/66090" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66089">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66089" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66089" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66088">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AJyi0C_255dag9yhc8s3-xc_vEskIoUisE2KbBUSdCV0DJoAHATwvjS48fJpQG2atFMMaFEkWXqmYhUw4j4FjDa9FE9_a3KjRPqA4QM7nXtUOub8TBrEnAo_37xUapm8TLWNuJXdwx9pOnR3nIPw0-Yf1mIZdLDN7qV2LXLnBeoUzlBuJdTYddd47aiHjoLb12Mv2wUtJhj3r3EEN-JnzgZE0dD0UWpaCHyZrE4HrSyVHCmKG3Gjb_et1iPYj13hMUhnVmpDsKHMbk_kbqW7OXeALj8fMAJKgODKyY5IkWV31DxFjiobdNPDufujkvW-mjuxjfDqKZ8DpZ2gsBB6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66088" target="_blank">📅 20:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66087">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=Nt16g3moeBNtilo5M5AMiEFoeohh8WsoBqMQ8izJoQdJbS_cCA_RjJBnz10QMN8xji_Fcpp7UyYbhv4qOL0YGoBnQamTxnd1DJCk7dxASDCELcFPVHQzO8gcwnrvyH2gqoITYhdsnuL8Zxa8jRsjA1OQX9hfKdBQxAYIg6Q8OBIugklnSTjuZ1ppobOin4YUur3YLM277CgNR73dskl7HB9kxPZKaAAR8OWFL5dDNLZx4qoNvZZcTme6SICC3AU1g4rgv7xHVQIP33q2yLvubyO0auoZddUoTHsWR6DONJL-QPU42ac8p1OW489sIxfp7J0LLINqt_TqxN5gf38HzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a73d88cf6.mp4?token=Nt16g3moeBNtilo5M5AMiEFoeohh8WsoBqMQ8izJoQdJbS_cCA_RjJBnz10QMN8xji_Fcpp7UyYbhv4qOL0YGoBnQamTxnd1DJCk7dxASDCELcFPVHQzO8gcwnrvyH2gqoITYhdsnuL8Zxa8jRsjA1OQX9hfKdBQxAYIg6Q8OBIugklnSTjuZ1ppobOin4YUur3YLM277CgNR73dskl7HB9kxPZKaAAR8OWFL5dDNLZx4qoNvZZcTme6SICC3AU1g4rgv7xHVQIP33q2yLvubyO0auoZddUoTHsWR6DONJL-QPU42ac8p1OW489sIxfp7J0LLINqt_TqxN5gf38HzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
ترامپ به خبرنگار فاکس‌نیوز گفت انتظار می‌رود ظرف چند ساعت آینده توافق  با ایران حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66087" target="_blank">📅 19:52 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66086">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XyDbLM6H0pSrexZLPcKn2hS-UwJHzOAFpOrf-RaGwysO-zqO-9sNrwtFxUtY3YEremHAyOTyjNj9TVJiYtlCWcYOON_GStbp3E6OZQEUXa4bSc3jhCZl5voWg0Xe4k1yX-U3zv3ThMNP95rtZsOXN8Sephv4-jBmYQqZffBNLhPFfp-hHpsabZI3eJusRJfNIRtp9om6z46b4eElUOZ_7aDstr5_iFDCC27bhYe44wLSPFkugXRN6Cib_VAk3Uo6QAATFGpG6Hf65ARnVjN7bAWG32G6QbotA5ZjyFW6u1qKQUwrOjY1w54eSrDcSAelE6QFzfPbIGWQlzB9FlrpVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید: رئیس جمهور ترامپ در یک مصاحبه تلفنی به من گفت که معتقد است علیرغم حمله اسرائیل به بیروت، توافق با ایران امروز امضا خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66086" target="_blank">📅 19:42 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66085">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
پزشکیان:
شورای عالی امنیت ملی به این جمع‌بندی رسیده است که مسیر گفت‌وگو باید دنبال شود.
رسانه ملی در حالی بیانات رهبری در خصوص عدم مذاکره را مکرر پخش می‌کند که بنده در مقطعی با ایشان درباره ضرورت خروج کشور از وضعیت فرسایشی "نه جنگ، نه صلح" گفت‌وگو کردم و ایشان نیز در همان مقطع مجوز پیگیری مذاکرات عزتمندانه را صادر کرده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66085" target="_blank">📅 19:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66084">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0x_nxc__lmvKZJMpgWhXZ97WgHuZcHfLu6Nj2I5CyTRkFtO2g2WRRQJ94gBlUhKZRRmce7U1WjKrIeUygBHegDsgMrK5SRnby1Caq9YF3Cwcd-JAlzzvdi7vEw3Z01059wyZYmCQf1bJRR5iUB6YEQmOM5fav7GcBlK9bLuu_-lDIiIPDPsW94nBzfn3fdRZ1pqURHFVm9PsG1tBtWYYZFsrwAot5ZT8g_dYjK8xMrPyNtmPihqvEmVDtOkT8BbzlQs_n82adJn4PFRo_16yBjiXGIQSm8s3vvO7Fdr2TVitA25dZOtasb1q6vIM3DJot6CirFoVL2ytiW3L8uXBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ترامپ در مورد حمله به بیروت:
«این نباید اتفاق می‌افتاد، ما به توافقی که صلح را به منطقه می‌آورد بسیار نزدیک هستیم. بیایید آن را خراب نکنیم.» او از همه طرف‌ها می‌خواهد که عقب‌نشینی کنند و حملات را متوقف کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66084" target="_blank">📅 18:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66083">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
وزیر جنگ آمریکا به سی بی اس:
انتظار ندارم حملات اسرائیل به حومه جنوبی بیروت توافق با ایران را مختل کند.
ما در مسیر امضای توافق با ایران هستیم و مسئله این نیست که آیا این توافق را امضا خواهیم کرد بلکه مسئله زمان امضای توافق است.
اگر ایران میخواهد این موضوع دوام بیاورد باید افسار حزب‌الله را مهار کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66083" target="_blank">📅 18:17 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66082">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66082" target="_blank">📅 18:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66081">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66081" target="_blank">📅 18:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66080">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
سخنگوی ارتش اسرائیل:
احتمالا طی ساعات آینده ایران به خاک ما حمله کند
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66080" target="_blank">📅 17:49 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66079">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBwf-47Kbb85aqvW7ex4_LhDScfN6ee3Z2sjD5g3gqLBjj7lq_Z2k14gH5uRe8TbXKVyZnBy8uazm5Odh7Ueo5iajxXbuoeFke25TDbnFyVsAbEw4fA4ISKFqnMt2ReWhZafOS9Hq0jqb1aDHsR6NZmtko8RO9W_9j-16ve2buqNZ-f7W08mfoDNEa_uozHIbbVEhq6NA1TUNN21endehfysp-_OwZhEP5nQHNp1krbVAIP-D3FOk3H9sdcaV1M5CL-LAudOlaPJfXmmoE28CaRinaBi7teKiCEowvfZv3TAPd3SpCpDz68ExsW0yFIuY9x31P_oFMlRdZ6M6y6x2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی:
حتی اگه توافقم بخوایم بکنیم باید اسرائیل رو بزنیم تا ادب شه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66079" target="_blank">📅 17:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66078">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXE9j7TV7p3hR-vXlvNbHVhMe_IEZCgRwJ5Sa0Ex7qtPBsAJrAEF3RKBBsblp7q3mk-g9kht-9KKoFrzU4_ypZqn6n_KMdP_XEbM0gQcS7mVFo4yPKIHzaw__yomgrCvP7DVZv85xCCfxcckjMHKwKCJAzirXAJmfaQz3ECVWIMxVKlKNSzyv0aFr4d0RwaWKfYn7eKTsPp3uzs9H2WKBi_MhedndwDtVekawdBwsG49ty76SsMJVHuVDzdustCNtvrxjP9O7LLBRT1P6JoEMCwdUK2c7ldBapeHlbZdYT_u_oS4BAKEYNcXuD4Ufi7y5S8BDkmd9A7e4Ze6i4NHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
مرندی عضو تیم مذاکره کننده:
فعلاً مذاکره دیگری در کار نخواهد بود
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66078" target="_blank">📅 17:39 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66077">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e954c10201.mp4?token=Az7HmaS3V97Ujw9QVYxfld3t-Qk83bQQ-r3cczxjUtQbOvJwJujZD3ZoGREY_COHGU_5OEI-VUusBwF4NbekCWWs9XHXgV1fIeYiDrrdiNSAaN5FmeKcUwHZfyNiYTE2bzT26eGf-_ds6O_oXyLfe5jgcuaLPs0cZl4BF-ofoICjuyB71zCRzFBfgxNxw4mRuFgH7LVC9HOqOqVyYHjZ9PrMOeFekz18AMOJWpS8Ye2q-6ZWtByfC4bYRobZvbFvq3ElYgAD0_8ZrT74WkG_dOGeFjek-ZHjVPV7YUMpYetWq25dfwFtC_6JIP-6_BrI0naLX7DB4H8dlr8UqIloyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e954c10201.mp4?token=Az7HmaS3V97Ujw9QVYxfld3t-Qk83bQQ-r3cczxjUtQbOvJwJujZD3ZoGREY_COHGU_5OEI-VUusBwF4NbekCWWs9XHXgV1fIeYiDrrdiNSAaN5FmeKcUwHZfyNiYTE2bzT26eGf-_ds6O_oXyLfe5jgcuaLPs0cZl4BF-ofoICjuyB71zCRzFBfgxNxw4mRuFgH7LVC9HOqOqVyYHjZ9PrMOeFekz18AMOJWpS8Ye2q-6ZWtByfC4bYRobZvbFvq3ElYgAD0_8ZrT74WkG_dOGeFjek-ZHjVPV7YUMpYetWq25dfwFtC_6JIP-6_BrI0naLX7DB4H8dlr8UqIloyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وضعیت اعراب حاشیه خلیج‌فارس توی این جنگ
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66077" target="_blank">📅 17:15 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66076">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه! #hjAly‌</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/66076" target="_blank">📅 17:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66075">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بی‌بی همیشه دقیقه ۹۰ دست بکار می‌شه مثل ماجرای فخری‌زاده و برجام، باید ببینیم حملات امروز به ضاحیه ترور مقام بلند پایه مثل نعیم قاسم به همراه داشته یا نه!
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66075" target="_blank">📅 16:58 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66074">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60a237733a.mp4?token=fmHJFMbAZRW-nnhEgrZq05r4NJFhMiVti2EHqixjWCfPeF6e08TL_w5bbnPNdRR6VVrKvvlqlmLrqv9eB-8rnlURVx1Mkmnd8G0deWIvPSSPjhCWdxiK_huqL2pLTMCG16JYHeFs6-r20h46Vyn9jCYqCIVXX38OGJodzcZpWeeCvUriZ93_kH6mgDh_R7CXPZXitveIc9jRQ_RlQ-MjOW3JXjYthdTQZiPwOWb64X5YuJhpOPQMuHMTf1gnA7HT2dzMdTLXOgi9ufOfkMTs-kmu2PR-4IoQjLlY8iDUsw-ZiaPRWaBCqY9zF8Lw9aj6cjTXJdrJ9MguqPwuNQqnxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60a237733a.mp4?token=fmHJFMbAZRW-nnhEgrZq05r4NJFhMiVti2EHqixjWCfPeF6e08TL_w5bbnPNdRR6VVrKvvlqlmLrqv9eB-8rnlURVx1Mkmnd8G0deWIvPSSPjhCWdxiK_huqL2pLTMCG16JYHeFs6-r20h46Vyn9jCYqCIVXX38OGJodzcZpWeeCvUriZ93_kH6mgDh_R7CXPZXitveIc9jRQ_RlQ-MjOW3JXjYthdTQZiPwOWb64X5YuJhpOPQMuHMTf1gnA7HT2dzMdTLXOgi9ufOfkMTs-kmu2PR-4IoQjLlY8iDUsw-ZiaPRWaBCqY9zF8Lw9aj6cjTXJdrJ9MguqPwuNQqnxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسایی نماینده مجلس:
اگه میخواید این تجمعات شبانه تموم بشه باید انتقام خون نائب امام زمان رو بگیریم و این انتقام تنها با محو کردن اسرائیل از کره زمین به دست خواهد آمد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66074" target="_blank">📅 16:45 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66073">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyM8K7LK7oveGtSlA-TQaZE8QRPZRpcwLv2s8Bs2p91Ei038XMAVbYvvQFa_6isgTYMrrEi2cB4ejLNNzC7m3u337F7RhJihR1JVBlWKC9vL358nCwrOX3V_u5ARt_U0tVRaoDq5E6InhN6WKZJyJsTM6sTfaoute4z-5fADBjHIEHmpsmMcjfHbxdkXgZIBkojdrYA7AGVRzd-wI-uoUYHBblpamMtigiOEoGNXXr96-wKvS9hm7OkDnnkDGXIw9FiIjO183vAhWH1V5FjBp2CTE-Ms8PQPIW3XZORSYC-3G1yFGXmkyHIFHTJpF9ABDM5ByJCcgaa-espLq7iw5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
قالیباف:
تجاوز صهیونیست‌ها به ضاحیه باردیگر نشان داد آمریکا یا اراده‌ای برای اجرای تعهدات خود ندارد یا توان آن را. با چراغ سبز نشان دادن به رژیم نمی‌توانید امتیاز بگیرید. بازی پلیس بد و پلیس خوب قدیمی شده است.
اگر اراده و توان اجرای تعهدات خود را ندارید، سخن گفتن از ادامه مسیر ممکن نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/66073" target="_blank">📅 16:08 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66072">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل از مقامات آمریکایی و اسرائیلی:
ارتش اسرائیل،فرماندهی مرکزی ایالات متحده (سنتکام)را اندکی پیش از حمله به بیروت مطلع کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66072" target="_blank">📅 16:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66070">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa7b240724.mp4?token=XufJCEUxH12hbA6lpnk0Ll7dAeCxEuAbmDzILRpBSJaxn3WT93oH7Efz5oLgkLbR56-ol2rOCwXloKK91PBZy77ezRfcCA7xitQz7RpLnc-zgAzb3DxxBte3s1BHcQ5-ebGVhGqTus9nWhtuwKN_pIvSolQYJdPMycn2uwKeskSPuhtAq6r4fHapV9UnfdOqYW0ds-ZzL43ine7JgV6DqPFCM-27c0Sb2S1B7C6IuLBaUhxdD6lNUVPlfp35gqKjYkl8kiHnS4XmdmZhLDVDrN6Z0q4EwXr_n4bo76emJFr2yAmVcLR-ED727hb4BGw0-WwCAwOf3EQl4wxjT-fr9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هم اکنون واکنش نتانیاهو به توافق
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66070" target="_blank">📅 15:23 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66069">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">طبق گزارشات رسانه های لبنانی حداقل یک نفر کشته و چهار نفر در طی حمله هوایی اسرائیل به ضاحیه بیروت زخمی شده اند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/66069" target="_blank">📅 15:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66068">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">Live Volleyball</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66068" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66067">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d546d16a9c.mp4?token=U0SQg6Fy6-fv6T6Phkj2R87V6x9MTaI7f6JrIiPB2KMJLsMxLZl3s-TDSmnhJgfWAyl96-0CPoiSfTrJxACj_ph6cLSUbQRj-My3qBtsetcD1Yii_t41E710pF5eF5FzoHnCc6bjcAUXVQuyQtshpCr2GSqD-XKiHVblpv6dwikIvwRoneZ2upLWUSd_JBroLsEKlbrZfjjritCRd-AuAdgx0iCZGNXLtJ4lSVZQ06USHqTa1G6V5Xf4hX1WOtK_ElRnkDRDUXNxoHXzgeW1X5MBFBd5O7kN23hgQNHFSr9uEv90ERhnL-bI-AXtkDHryF7Eq7sIoN3JnAPbem6_XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پزشکیان: رسول خدا و همراهانش در جنگ لت و پار شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66067" target="_blank">📅 15:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66064">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6b9063a8.mp4?token=nVtNhlJateqBmbPj7dPxDiCL2Htao0HVB7vEPRZtfCARnnCZsYANPabYhzSo4AoziEvYs91NwZlIJaNr7oL9A_xMrgTTOj8Yc2VFL_4-TDvBQpeSSN8oz5Ce-5hr5r7InBwTtEwxHFiukOEUvPQJAOBPpi8IJdgq68gSjf7JfStsc-KhOHB4TrzSqyElwQI_pxObQySYrf3h3YJpOqGqN2oHCZRkuoQpwTNaZq3Qo46eshVemTCUJ2o1gIHpiz-z_Hj5uItiQynVMyT_fZUNDj9GeVB8w_7P07kZkmwF4yifYGXbbIzJgzkWD4WAaVWE9zoRRxJEnRMbbEysEeTy3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو ای که ارتش اسرائیل از حمله به ساختمان حزب‌الله در ضاحیه بیروت منتشر کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66064" target="_blank">📅 14:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66063">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
کانال 12 اسرائیل به نقل از یک مقام امنیتی:
این بار، ما حتی پرتاب یک موشک از ایران به خاک اسرائیل را تحمل نخواهیم کرد.
اگر چنین اتفاقی بیفتد، اسرائیل آماده است تا یک حمله نظامی گسترده و خردکننده علیه زیرساخت‌های نظامی و اقتصادی ایران انجام دهد
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66063" target="_blank">📅 14:37 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66062">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
کانال ۱۲ اسرائیل:
هدف در حمله به ضاحیه جنوبی نعیم قاسم بوده است
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/66062" target="_blank">📅 14:33 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66061">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیشب تو بازی قطر سوئیس، یکی از هواداران(خانوم) شرتشو در اورده بود انداخته بود وسط زمین
⚽️
@fotbal_xc</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/66061" target="_blank">📅 14:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66060">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31239b7a33.mp4?token=UQHk3uNCUvUgRvDOWxHvyFmnakkJ9lXHWQkHtfRFQYjNMrZmqgRy2rRXtkvMheJTTMO4BQ9yxOG3oJ_sANwNqPFqbuvccxNyhZt-91EhtSbMp1mgerzYiU2vtZvwItF1c2vkvwJXA08L5E2bEnJw3CsjOOCoOSZQ7NHHa-7d-mbcvuRlb38kPoJRjLlWn8sNHes5n_CyjFOGMrNFRruzqolCIfvn6Bv9BdES_ZKyDdwfAoIjgXbweorZRgRIvXP7tGGhDBo6JtVVWEd_Ub_uckUvvN7LSaQrTw07T-A0VJMP3HzNrYu2X74F4jYQQgaKUNqt7krfE3dHzJdU9q6zkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چندساعت قبل، اصابت پهباد حزب‌الله به منطقه ای در شمال اسرائیل.
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/66060" target="_blank">📅 14:28 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66059">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت  @News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66059" target="_blank">📅 14:26 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66058">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=c0oxsHxqTajFRcppAuaA2oCBo0NT85HO1Xz8J7d7NCB3NF_aUcO1bdLx0LrBfAxyGG9fbvh0B21nthgNpjN7_uIs_tZV4xAxHul8Y0rjB5kYLuy4ZULkGG6cQx8EiSW4ZHODto6UeCigjh30CYfoo5T-zCXyHBtXs5H90waEG8CW6AlYSu22BV4IDuT7axDrfaFY5zPyEnK9CxGubd0w3hfU44RMkiHTWehvIK5JVoLJkCguhOWwSyiWRwfyjctjHZ4YqykqOhHDmfqvx7beFcB6h4iLj6T9EceYyRQMJJbSAA0nMjj5lBk8HfQAS5EIrNX8U0DoYn3ykHtKSi-u1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07e4fa5e8a.mp4?token=c0oxsHxqTajFRcppAuaA2oCBo0NT85HO1Xz8J7d7NCB3NF_aUcO1bdLx0LrBfAxyGG9fbvh0B21nthgNpjN7_uIs_tZV4xAxHul8Y0rjB5kYLuy4ZULkGG6cQx8EiSW4ZHODto6UeCigjh30CYfoo5T-zCXyHBtXs5H90waEG8CW6AlYSu22BV4IDuT7axDrfaFY5zPyEnK9CxGubd0w3hfU44RMkiHTWehvIK5JVoLJkCguhOWwSyiWRwfyjctjHZ4YqykqOhHDmfqvx7beFcB6h4iLj6T9EceYyRQMJJbSAA0nMjj5lBk8HfQAS5EIrNX8U0DoYn3ykHtKSi-u1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
حمله سنگین اسراییل به بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66058" target="_blank">📅 14:19 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66057">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🚨
🚨
ارتش اسرائیل:
حزب‌الله با نقض آتش‌بس، سه موشک به سمت شهرهای شمالی اسرائیل شلیک کرد و ما در پاسخ به بیروت حمله کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66057" target="_blank">📅 14:13 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66056">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZKhp0_p9W0QGX0Yr20ypSRZ7py-T6VOrH6eUFsAN2oO7tOE7P4Hp8jasPHOmriBfALWRoAodooTIw-UFrXmj8-YCKQIZ_mk1g_TSvVlqEz9VBmCM2pbHq0uYhf2iSbXr6cvV9gqVxw04mlHWbYeAp7LYKIlHtze3qYIoiTfd7oYKuOQZrwJoP1ZLfHKFNOqOGwMyLfOj0kJBA_mRI4SQznh26hE-ORxO97NGpk00AfVw7hH7n7WloH9IfcCExZqHnINeA6KJa0xh_lzHpYDkcrYzwrWSXPQYQi2JgcWvbXKtV___hCy-55qanRtf1bJ3aMsLLy2mts6DZHcvoGGYfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
بیانیه نتانیاهو و کاتس:
ارتش اسرائیل اهدافی متعلق به سازمان تروریستی حزب‌الله در ضاحیه جنوبی را هدف حمله قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66056" target="_blank">📅 14:11 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66054">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVBQekkR2H0dRgTfELLj-XOzcrQgjbIlqd6PhZ47f_hIcnRSGFto_-EZdMpaJ61F9gSWC7Jr887U2FLxre_cu6VVMUqW_sKnJVyT-zC3ha7G5nUT8CvP99cnD1195QnBq7QunqXYkE71UGik1sICpV7UHIzPItDBjHAv8N5CU8vM2etc-j9FnUxTPgKZOD38JNL-r_tbIqQ-diAHw0WZMz6AGBBeBtgExNsg-JdlYx5AmqVO8977McMwekIxTmPO7aXAZGmK6UhUIr2rek2F0osfsWwqx772GpnOwQBuXvCdTaRd0Rfl8IxjgltOQb382ftFPRPwcaItOeswqCte-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گزارش ها ازحملات اسرائیل به ضاحیه بیروت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66054" target="_blank">📅 14:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66053">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=olyAvi7fREZlyu9k__ZSjlMWhTfI2FJDjXnfh21U3XOPyqi9Fw09vIM-5LLJ8GPrjNLaHKitJar68zVpkanZ6HFHBi0rbwoHTdaFNRTR-fUnLhKkTiIdtNtIZOlwg5jm4Xd1HCPnif8-xx2UsbjB_nq_mtYmXv0PYR9YLk2_PlbtbAVpWiiVDxmpjtrAYtRCBdC2foutFeOe78ZCkPeovnoP2clQo5DIc0FwOmvog2NiW3UDDM7pqyEEkX19Y12QcUNUkgsmrLKeDUKjqEYI5-D9Q7ictjGyejee9xl3O1On1gHutEVvdZRi4dkxPABYSdaD5qX7HGryvXjwn7bngQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0119b4719.mp4?token=olyAvi7fREZlyu9k__ZSjlMWhTfI2FJDjXnfh21U3XOPyqi9Fw09vIM-5LLJ8GPrjNLaHKitJar68zVpkanZ6HFHBi0rbwoHTdaFNRTR-fUnLhKkTiIdtNtIZOlwg5jm4Xd1HCPnif8-xx2UsbjB_nq_mtYmXv0PYR9YLk2_PlbtbAVpWiiVDxmpjtrAYtRCBdC2foutFeOe78ZCkPeovnoP2clQo5DIc0FwOmvog2NiW3UDDM7pqyEEkX19Y12QcUNUkgsmrLKeDUKjqEYI5-D9Q7ictjGyejee9xl3O1On1gHutEVvdZRi4dkxPABYSdaD5qX7HGryvXjwn7bngQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
▶️
تصاویری ترسناک از لحظه بمباران یک نمایندگی خودرو در تهران
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/66053" target="_blank">📅 13:29 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66052">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=Eh95frOXNrPghlokdj4uaY-COPv0fijc7D2uY3SD9-bEnKDCsAgTbMNTy1TxbY56pnW4-dd6JuwHiSmzZKsOJV2Mx44lkVmadfu3RC0uOwKHtCEhChOD81ynW8aEZwQ3VjFq7N1gRZFQTHDmvUobIZifb2kpt2GW-uRMsa7r4btp1gnqz8QKqzCOXk6gkMg9ltJVWV814fqFXj7xzu90FmWMkf4F2omJdedhrtl18Bekw5EayVuAaAY1FMAFeceqdZ0GDI9qZBR_ixIGOIH-hph9qMUoCWDml5ci3vVMgts8IESUQGJgO2HDV_ilK9pO6Zz-Uzx5yB23R9eRRgMwEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f17f35bf38.mp4?token=Eh95frOXNrPghlokdj4uaY-COPv0fijc7D2uY3SD9-bEnKDCsAgTbMNTy1TxbY56pnW4-dd6JuwHiSmzZKsOJV2Mx44lkVmadfu3RC0uOwKHtCEhChOD81ynW8aEZwQ3VjFq7N1gRZFQTHDmvUobIZifb2kpt2GW-uRMsa7r4btp1gnqz8QKqzCOXk6gkMg9ltJVWV814fqFXj7xzu90FmWMkf4F2omJdedhrtl18Bekw5EayVuAaAY1FMAFeceqdZ0GDI9qZBR_ixIGOIH-hph9qMUoCWDml5ci3vVMgts8IESUQGJgO2HDV_ilK9pO6Zz-Uzx5yB23R9eRRgMwEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
تو برزیل یه دختر 21 ساله رفته بانجی جامپینگ یادشون رفته براش طناب ببندن و انداختنش دختره هم فوت شده
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/66052" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66051">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/news_hut/66051" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/66051" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66050">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3rnOzZ-6IAHWTYVOQ8PpsPGqx7lrhgVSzOqjLm4ekVzyPEgp2FBIIjtnO_2HD_8PJOlTokhBzt_dvV2oCCfeCxThP8kpMt9NB97C6hyRFMY1NQChHUSwpCMOcJm7tS3B6TYmT6CpoDFDQ_Bzgg5gM2YpnWYZrISaerwqH-mhTg_Ger02EWuJ-KQaGR398vq8ZqxOcv11CUDSH0tFIi_USZaRFVxlQWq4p98yR0wqIGUCBuVtvxBNALUP7e0fx9jPFWIR3aYIf19uiwCzKkR_s6ZCa0jeCzNTyIAyhXLyWNTDvKodEYOSoOlu_UXd4RKqynH5Y62w6LHSQulY50PDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/66050" target="_blank">📅 13:20 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66049">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db36249809.mp4?token=qnj2ULj0oZY6ZPEARe5zkXuKrpAi3dlbKRoYNYUOTq-id7d6UdgNwNNBAqQEgI4_9enDC1UZInTW2iVceZHdODFuesh8HQPuSI884r5EEoJoQ6NMjnqhraEchzlvuNnrSjvsjm5p-_Kzv3mhmPOmDwNC0b_vugagYitgYY73mTwF2p0Cvc8qzmDe3olBMKV10_FT3AG56hLCeqa3cMbZXWxcn7GYCV0d6GmKrnvEzgjnycLcKxCVqOUguHI2JxWewK_XnBOh8xu75H4o71O3qJz16v3s6_Yp_30hTbKxMVV6kQ4XLW7kdY2onXlGzjYCdUvGHllxI1-zTHLUwDRMPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db36249809.mp4?token=qnj2ULj0oZY6ZPEARe5zkXuKrpAi3dlbKRoYNYUOTq-id7d6UdgNwNNBAqQEgI4_9enDC1UZInTW2iVceZHdODFuesh8HQPuSI884r5EEoJoQ6NMjnqhraEchzlvuNnrSjvsjm5p-_Kzv3mhmPOmDwNC0b_vugagYitgYY73mTwF2p0Cvc8qzmDe3olBMKV10_FT3AG56hLCeqa3cMbZXWxcn7GYCV0d6GmKrnvEzgjnycLcKxCVqOUguHI2JxWewK_XnBOh8xu75H4o71O3qJz16v3s6_Yp_30hTbKxMVV6kQ4XLW7kdY2onXlGzjYCdUvGHllxI1-zTHLUwDRMPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۱۵ سال پیش زنده‌یاد مانوک خدابخشیان جنگ میان جمهوری اسلامی و آمریکا رو اینجوری پیش بینی کرده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/66049" target="_blank">📅 12:40 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66048">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
🚨
امتحانات نهایی پایه‌های یازدهم و دوازدهم به دلیل مراسم تشییع علی خامنه ای، یک هفته به تعویق افتاد.
پایه یازدهم: شروع از ۲۰ تیر ۱۴۰۵
پایه دوازدهم: شروع از ۲۱ تیر ۱۴۰۵
جدول زمان‌بندی دقیق به‌زودی اعلام خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/66048" target="_blank">📅 12:09 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66047">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e28745391f.mp4?token=ftVH9lmfyib7gtYmnxt14ofchq7QGrZGTmcHiNtZ3rwB8i9PIk-TeQPZQKzTO16CIQi1JmRa7tg08rCQ0-8pDW1igXv5jfaixVRopoxVescZoBjCaNgAZN85k-ZA0UAt4e47xq8rhyrYLi6lNXrN7xy0h3bGR_Kh9nDL5PaAUA-pPdRfb7EbSOSIFj0MyQhUtCqnQlpWkydvEuQUBufz2hTGlElSm9FoFcA8uN82-tsNaI_issC0443QTGjUd7vei2-1xgavu4B-PLzAE8yF8nrbzrlaQj9EmzUc49S1JvjJXl6582GFWf05G3jo0nFZFdNbhaKAMuwsuS3p37iKvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e28745391f.mp4?token=ftVH9lmfyib7gtYmnxt14ofchq7QGrZGTmcHiNtZ3rwB8i9PIk-TeQPZQKzTO16CIQi1JmRa7tg08rCQ0-8pDW1igXv5jfaixVRopoxVescZoBjCaNgAZN85k-ZA0UAt4e47xq8rhyrYLi6lNXrN7xy0h3bGR_Kh9nDL5PaAUA-pPdRfb7EbSOSIFj0MyQhUtCqnQlpWkydvEuQUBufz2hTGlElSm9FoFcA8uN82-tsNaI_issC0443QTGjUd7vei2-1xgavu4B-PLzAE8yF8nrbzrlaQj9EmzUc49S1JvjJXl6582GFWf05G3jo0nFZFdNbhaKAMuwsuS3p37iKvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
صحبت‌های حمید رسایی علیه مذاکرات نمایندگان جمهوری اسلامی با آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/66047" target="_blank">📅 11:25 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66046">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
ثابتی دیشب تو تجمعات بسیجیا: عراقچی خائنه و من طرح استیضاح رو به مجلس ارائه میدم
@News_Hut</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/news_hut/66046" target="_blank">📅 11:02 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66045">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vchcdRY-zXlAc8y0wKfULFOg6d_ZKynquzuTxEV7XZ9QoQg2MpLfetD17-ejbU2WQlHQQbQr3nV6zB1wopqu2qHLsxkneVSvdQuGXwIzWh3AJEPRE4UV2uSPO_ypX9sX99_ZTzmumMA3BybluIqCzUlU_rJEol2gM-7I6NW22l7lAFiBLjqmqzrILLb6f5T1YJTKwwruMxlRJ42GE_hekp0zRVdt2iB0rnXRP8othxAQSap1Yn05SxVIHTKAX1WsVIHsBvbnJyZZ4QFTJvJ8Ina8vbB4pjWuYq3WCb_oxG9PqiBUwrDlEIhzXwnuTKyaRnIKSnT2pZt7ni70Myl-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی والا مام خوبیم
بابامو کشتن
زنمو کشتن
بچمو کشتن
«ولی رفتم باهاشون توافق کردم.»
@News_Hut</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/news_hut/66045" target="_blank">📅 10:35 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66044">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/375671acc0.mp4?token=ix3N7IMKDVqWhnb3Pp-96SDX9w1yddtbS_Xv9f4dSNDOFHa04XmG4gGLbnJ9z2OlOnJB8u-YfrILjV4TalTY_EYaILp18qHfLSx7nvg2rXrPO6_v45nb4AwZu6ItBNayZWV0b2B-GSiiono4EMp9gGOpBXKYKEyqYq6WmyNx9rbAkc2UzgMx81ZwAZokdfi-DarQ7R943BWqgnkROM7LkON8Jp0fYxr5z217FOs07ydPhtOFSEHyit9S3hUlN-TG8BDYLO_6NNJ0duah0ZZj1_rMWWmx_4ijcfTDXUc0JOIPPXBq32ksQOqQiPjzBm5ct11Jj9FjFWtWhDAyoyAisA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/375671acc0.mp4?token=ix3N7IMKDVqWhnb3Pp-96SDX9w1yddtbS_Xv9f4dSNDOFHa04XmG4gGLbnJ9z2OlOnJB8u-YfrILjV4TalTY_EYaILp18qHfLSx7nvg2rXrPO6_v45nb4AwZu6ItBNayZWV0b2B-GSiiono4EMp9gGOpBXKYKEyqYq6WmyNx9rbAkc2UzgMx81ZwAZokdfi-DarQ7R943BWqgnkROM7LkON8Jp0fYxr5z217FOs07ydPhtOFSEHyit9S3hUlN-TG8BDYLO_6NNJ0duah0ZZj1_rMWWmx_4ijcfTDXUc0JOIPPXBq32ksQOqQiPjzBm5ct11Jj9FjFWtWhDAyoyAisA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ١ دقیقه رو گوش بدید
زنده یاد مانوک خدابخشیان میگه :
رژیم اگر توافق رو بپذیره به جاکشی می افته !
@News_Hut</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/news_hut/66044" target="_blank">📅 10:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66043">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/afTamWuliVjHvNesztStPBXP_zAgGdhs7PVfnFMfD29Em-Nm5U7qfWAvVVRQRb4nR2SeiP2JBfPUlGdkVf3Oxab4a5-6TG4ShRIBmn1t6d7Wj1wdMugW39eFZedd4mDGUDwoLGfjI7-cUiwDzWm9IMCzaltdF7ie5-G593H2hYi4YjvuBpUtqU1pLf6A1Gmoh_eyXorAS7V8bo9m_qk6d90uLlMi5Mbj_9FjUW7nYAepWbsy1rMd9dgmL9lPb6PmHMQxSCpBikT2q-Iep4bS9X7vwdEyUP99v4tsueLKas8lXMt1HgqbcCRbF8DN4VgJ36CaslAN160YaMFqV04JPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط عباس میتونه جوری توافق کنه که:
جمهوری اسلامی ناراضی باشه
مخالف جمهوری اسلامی ناراضی باشه
اسرائیلی‌ها ناراضی باشن
آمریکایی‌ها ناراضی باشن
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66043" target="_blank">📅 09:32 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66042">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/518512af42.mp4?token=CRNESOeaUWy87vXCc04DyBtyTqdVt_cgNBzm4PXEPLnvMl7Np0l3AnJJglfm_o_6EO4HWxqr5-nBg1BAKQpphEq2-j8H00SasnpCLjd9yczBXGyD9KF6x6_wTwMn05kr4dD2wTP47GFLgb72GJdAYABb8Xkvs1J6bLKMn1mMz7Dt3c_HUmAyeMseRhNmrx8f8jD_UTwHN7_PMUa2W83i59CYYvg4soKUqVtzYFV-sDVyBzflweVs0-5uGu5OYtb8jVifThThj7RYJJqz3wLpjO8Rho2yfv9IHTOCuIVRrACKKYaKbrCkXupezxcVSFFDOxXI6SYEWh56iijLRyybNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/518512af42.mp4?token=CRNESOeaUWy87vXCc04DyBtyTqdVt_cgNBzm4PXEPLnvMl7Np0l3AnJJglfm_o_6EO4HWxqr5-nBg1BAKQpphEq2-j8H00SasnpCLjd9yczBXGyD9KF6x6_wTwMn05kr4dD2wTP47GFLgb72GJdAYABb8Xkvs1J6bLKMn1mMz7Dt3c_HUmAyeMseRhNmrx8f8jD_UTwHN7_PMUa2W83i59CYYvg4soKUqVtzYFV-sDVyBzflweVs0-5uGu5OYtb8jVifThThj7RYJJqz3wLpjO8Rho2yfv9IHTOCuIVRrACKKYaKbrCkXupezxcVSFFDOxXI6SYEWh56iijLRyybNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه آخوند آوردن صداوسیما داره میگه به پیر به پیغمبر اماما همشون با دشمناشون صلح کردن شما هم شل کنید دیگه.
«
واقعا بی شرف تر از آخوند هیچ جای دنیا پیدا نمیشه»
@News_Hut</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/news_hut/66042" target="_blank">📅 09:01 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66041">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/66041" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66040">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pkVIXh-7MqBoe2lSTmgrLcJbKpzFndHp5JIkz3yezQrPpi_VRMv8Rl3tUbq5jxjR-0oJTFM-MpNOcFkUE-qzLyP6MPA7uSB2zz0LC5gNIS_5Or8woLE5ENPwSPXEQNE0NT3br8LNDeP6sZWVqH3ytLsZTnkRsADG8ektcxGR0MSsPpUu3ToO-Blh7xNd-0vXF8Mr3tZ_Lb0CIPkOsYYiBhoVx7Ecq2WRS9aLY4dZTgVq1Q-S1OW9u0cA-9OEchkzMS5KCYnR-mzMyV7hW8uZBZFWDFTER23aZtVN-VZEs04nIaOMOp2MInDcAmSSDWwHqlRptMLxIPaxGc7XGA0Kfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/news_hut/66040" target="_blank">📅 01:14 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-66039">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hBSojXyyvjQrs5HUKKZKRWDbMHXz8wpCi9xVwyqY56c6MrCBwEgzFIYvUJggmAUDIsN0dDwSvSijV5w9xDd0alYLzc0QKBKyPektQxifntGVZE7JYh0qXe61GO2CWHFLUxeSjNpxkq6MTgkhSAv_hYbpXnVP1nPpSOcxycYOt8CM09vEG_Y55XtU0sxG8OZhHiEl4RrInJavAHHL4E-Gw2zRqgGtlGEutuGD0Q3qatgZZMxbQ8FPJQWMfskIdYnRLVP-39Stxqx6vbT_W2hFs7ByZBwbsIkkIOjM5p7mYzjTVDek31smBgEc4Mo02WRQEjZFHuTHEtBMDGr5aEFvsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/news_hut/66039" target="_blank">📅 01:03 · 24 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
