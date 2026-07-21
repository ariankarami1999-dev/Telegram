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
<img src="https://cdn4.telesco.pe/file/Pn8m4jQS6My3h9qHmJdPGuKEtn33QUv6mPHvJw2mIKjQu1blN-Oo2a2tc3j-mvomdsHFk2aOObrOjHV0ku_qtpRXjiaMHlobajTOKLRfMZACvdqHyikBNcYelQisaRnT07YP43Ys6rMfbUoC8xMu6gNVGhyPX07o3uFUoCzrgOgIQwqvdkCudQBXOBh_Ay-rYEtCqSqJPD3Uo9KuX9TIsrZFLn2yIbK80yGIyqweaCm5Gxwsp-Dj9tQjhVkYFmAdujukDXI6M-gpi5OzmQ2aNhPC9LukYVatM9tjIm0D8kbLGZZl54suE5JlXUfAaCP-4MEVYJnT6cD1ads66cdPHw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 156K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 15:36:11</div>
<hr>

<div class="tg-post" id="msg-68713">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه  @News_Hut</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/news_hut/68713" target="_blank">📅 15:36 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68712">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=eJmPDgHZBCMx9G7AeoUWc73frcqpU7U6brkiG-PGcrn4VAoP1s2MOImKapnqrxkYRbINLdf87bEvia0j-A5sGcebw29CCPypZKXvIgcIhLMAtvImeLPe964apW6vr1Zx3PmQbXqQmppqkJ3VXdubbQ_fZKQiN8ejBdg5zg6jxtuyZNH1tGx8aAXB4JCTzsC89OeHB_OHEr-PDVO7sz7GMraNV-RrxRI68q2XWBBfGSiEnMGH6_NIrBGuSGighwsdFvGF3lhklLmM-GNAkD-M25YViw5n-bN5kweWBaNqgpT1PzeQh-TRt6iSp3nKHV3MN8OaDzc6w6sk_XpsYFIx_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6161f8d4.mp4?token=eJmPDgHZBCMx9G7AeoUWc73frcqpU7U6brkiG-PGcrn4VAoP1s2MOImKapnqrxkYRbINLdf87bEvia0j-A5sGcebw29CCPypZKXvIgcIhLMAtvImeLPe964apW6vr1Zx3PmQbXqQmppqkJ3VXdubbQ_fZKQiN8ejBdg5zg6jxtuyZNH1tGx8aAXB4JCTzsC89OeHB_OHEr-PDVO7sz7GMraNV-RrxRI68q2XWBBfGSiEnMGH6_NIrBGuSGighwsdFvGF3lhklLmM-GNAkD-M25YViw5n-bN5kweWBaNqgpT1PzeQh-TRt6iSp3nKHV3MN8OaDzc6w6sk_XpsYFIx_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🤩
عکس یامال و تیم ملی اسپانیا روی پهباد شاهد چسبوندن که بفرستنش سمت مواضع آمریکا تو منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 1.6K · <a href="https://t.me/news_hut/68712" target="_blank">📅 15:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68711">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7KFb5QCEDRQVWyFlyIgcOEGePjpKJ6dZwnFmpdG_ncMoFujLKKxSiAgU7cbrUPuzsq5xhtRSTovDkrDHOJrJRp40_1nBYtOOtiHxQjrf2gYKpLuv7DUK1Duef8vIEh3TISpPnKeeu_yXSqGbgz1MrLtL5m_ADV1GD9KlUOUU07sfeWa14XXziHCEJB8O-oE8qFtwuXxudfUMkRDj_RuX1qIMAiImNaJfppJPSJHwBZb1gZyNO28WdBJ4zAu8g-MhAkMPGoApdZYZpws_qLBXzEk5oQkVBnyFo-5h51xivCi3-X0Ot6SVQJbVDUD5uDWnLaa-Ez4Z2bFUJcfzjwoTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
با اعلام مقام‌های کویتی ،  چندین نیروگاه برق و تأسیسات آب‌شیرین‌کن این کشور در جریان حملات روز دوشنبه جمهوری اسلامی هدف قرار گرفته‌اند و دچار خسارات عمده‌ایی شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/news_hut/68711" target="_blank">📅 15:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68710">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=dv_cfGt8voO95_vmK_Mwrp4Tnr52g2k9tt42M5LlgVcY1sxf2eRa4OIVoS2bvxJZ9qlyo_wAlLCV8gtCeXa1E70XAgPy896xLP4_OohKBN2P5kw300Q-GM4bJTz0eLg_meeJPVpIcK-QPcsfin8MYcVFlxCSLTj0-gVnnzbt-AoQtvtCPJZNPOSCJvBuYUv4IW2WqpGlkjRvuA0fdGXTDjvUE9Kd586XNVSDn9H9TU_JFQRCQIi6j_YnlCQhwTc1lLm8W_jjCPS6Bu6Y-d1xbqp45D7Gw55xkg2BGh6TOGcNrTrdXTnmuCMRRYWwKOhp-coZtH-bSuU9a3SpU8LEFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/acd31fc49e.mp4?token=dv_cfGt8voO95_vmK_Mwrp4Tnr52g2k9tt42M5LlgVcY1sxf2eRa4OIVoS2bvxJZ9qlyo_wAlLCV8gtCeXa1E70XAgPy896xLP4_OohKBN2P5kw300Q-GM4bJTz0eLg_meeJPVpIcK-QPcsfin8MYcVFlxCSLTj0-gVnnzbt-AoQtvtCPJZNPOSCJvBuYUv4IW2WqpGlkjRvuA0fdGXTDjvUE9Kd586XNVSDn9H9TU_JFQRCQIi6j_YnlCQhwTc1lLm8W_jjCPS6Bu6Y-d1xbqp45D7Gw55xkg2BGh6TOGcNrTrdXTnmuCMRRYWwKOhp-coZtH-bSuU9a3SpU8LEFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ها؟
درست شنیدم؟
@News_Hut</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/news_hut/68710" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68709">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🚨
صداوسیما:
دقایقی قبل نقطه‌ای در ارتفاعات خرم‌آباد هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/news_hut/68709" target="_blank">📅 14:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68708">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🇮🇱
وای‌نت:
مقامات ارشد اسرائیلی مدعی‌اند که تیم «جی‌دی ونس» مانع از برگزاری دیدار میان نتانیاهو و ترامپ می‌شود تا از اتخاذ مواضع تند و جنگ‌طلبانه علیه ایران توسط ترامپ جلوگیری کند.
نخست‌وزیر اسرائیل قصد دارد این سفر را با مراسم خاکسپاری سناتور گراهام در ۲۷ ژوئیه هماهنگ کند، اما تا زمانی که از قطعی شدن دیدار با ترامپ اطمینان حاصل نکند، به این سفر نخواهد رفت.
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/68708" target="_blank">📅 13:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68707">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=rLOjsfMMFexY0VQ8_EgtOC3zCNzsypnmsrBerHrSOWw63q-Rz6sIyRG8POu0JX_CkqrxyuB6hcGfUeaDn4c0idC5m7WHZwPYHMbQv5XUllNwuYRZRWUSDJK2LI5yYC6ubZQCkjWTNPdxoZWTwAmee4zo3YPVnAEldKLS7I4kWg1T8eROnhOoZZ2URGOKaG8zpjm4tYzkRg1euTwkZc_Y4iKSz6Us3-dNFsvKs3CHYErWzOYWhMNXjzSQZ49MyC5zEMFnggfg3OqCPnttgO9AcXarPtgWTIGTiaxwG7pHkDjoKvOnnTjBfh4mZcTBjbVKDp9w3AbGDITmvxLmPAcJnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f5cc929c.mp4?token=rLOjsfMMFexY0VQ8_EgtOC3zCNzsypnmsrBerHrSOWw63q-Rz6sIyRG8POu0JX_CkqrxyuB6hcGfUeaDn4c0idC5m7WHZwPYHMbQv5XUllNwuYRZRWUSDJK2LI5yYC6ubZQCkjWTNPdxoZWTwAmee4zo3YPVnAEldKLS7I4kWg1T8eROnhOoZZ2URGOKaG8zpjm4tYzkRg1euTwkZc_Y4iKSz6Us3-dNFsvKs3CHYErWzOYWhMNXjzSQZ49MyC5zEMFnggfg3OqCPnttgO9AcXarPtgWTIGTiaxwG7pHkDjoKvOnnTjBfh4mZcTBjbVKDp9w3AbGDITmvxLmPAcJnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پاسخ دفتر شاهزاده رضا پهلوی به صحبت‌های عباس عراقچی درمورد توافق پهلوی با اسرائیل برای تجزیه ایران:
@News_Hut</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/68707" target="_blank">📅 13:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68706">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=S0LdsmlX8yyt7kbpw7KRLiK8GaEbiLooZVWaV9e1fokr65GmBDqLwC7IPcqvhnVS9yAYouufSew2aYP3tE-O1GEs1SKTd2XKN4sTo-0H15BaToaObIdd8TmgvDbZft907KYexmpkZS5gEX34Oe7hcHKSImvjTedeIJ89pGeXyYufoFSfv3qiQaaqTM1MaiKJ8iNDcmblae80QJu_FMAkwqZZo08z8V5-9o07kOpwjg5ozhzKEbyD9akP1i1VAADgfhhNspZ1iJMxkjRzYW7S9P8eRX_hF0f7vJhtLslXkC4XNwFHrgqS4y4pr5Fq1huePs5YZ-aJKD4HaPwpcTpzuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427c084f6e.mp4?token=S0LdsmlX8yyt7kbpw7KRLiK8GaEbiLooZVWaV9e1fokr65GmBDqLwC7IPcqvhnVS9yAYouufSew2aYP3tE-O1GEs1SKTd2XKN4sTo-0H15BaToaObIdd8TmgvDbZft907KYexmpkZS5gEX34Oe7hcHKSImvjTedeIJ89pGeXyYufoFSfv3qiQaaqTM1MaiKJ8iNDcmblae80QJu_FMAkwqZZo08z8V5-9o07kOpwjg5ozhzKEbyD9akP1i1VAADgfhhNspZ1iJMxkjRzYW7S9P8eRX_hF0f7vJhtLslXkC4XNwFHrgqS4y4pr5Fq1huePs5YZ-aJKD4HaPwpcTpzuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیو ای از حملات دیشب سنتکام به مراکز فرماندهی نظامی، توانایی‌های دریایی، سایت‌های پرتاب موشک و پهپاد و سیستم‌های دفاع هوایی جمهوری اسلامی.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/68706" target="_blank">📅 12:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68704">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_63Sll41xy9ZJsfZZ_lkUBQbIii0I7PkiPMMzIcPE4tnONGLkAw0XAOtven772Yp7jPDX6w8ghHzOJC6Oy3V2LgyQPOrlE7rSU36Zz4Rgv1ra5sdc_6N0jDROEFR75nv7gsBdrfrpdE9o-tv8Vjo-isP9m0kGjPG80lT2aTOr1nleVYM77glPJTn-D2F2ByLBFm8UQcNxg8h6KuHA0oUO7nyIC9TdiSHQeVoixgXqjXITXQeqRDoglzyo3qT9JgNcfU9vcA9Rzx4DLF0miTKu_tZpS30OHYR_Py_3wme30ejorbnKOfKn95n6gaBlbSEPMxE1GERVdHeb3BdF9w8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYsjs4dZOeyCoZgSi4dx2WM88Ikr7zLw9dmvsFxf0ixksppXaW19fzZM_TQiJH8tROWUbzvTqneu8ynHpb4yEhnZMUkdvyYz9pgrQXgNZ9cKvOzwqTn-M3Az5rcaN_-KUmHxbbkIXWtgkFVZWHFZrlbmjXonne85Eic9vOv9TmeiKtebr4g5qxGcDrZpcP8OCPZGFswf6RJmffmAzUbDLgWzsBxxnMjPebpu9yLShfgrvYFr4CYSgvp1Cdzs_05lCUU6TM27R8IxLYLbaGXn85IDGD37wjZQ_Ua1Oyomx6UeHGlimO66I29DXvnsWUy-GXxMddXtgTmAnaC6q9vNWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
دقایقی قبل سپاه از زنجان و همدان به سمت پایگاه آمریکا در اردن موشک شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/68704" target="_blank">📅 12:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68703">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6PD3-as8ywkMOEzELZf30vgirQK4BUlhj3evbNYzhwKrNtTAj3O3hm0xdW3032843Z5SbOgtu81i_tKBiLvEA7xXWCV9CRgQEeUKv-3D6bZLUxqsXhZVFRyN0nb6SD1XfZkj5cUoVOz3bR1Zt1OJSnO9QPGcTOgKcHyu8jk67cu4Yo5GZETDE90qG7zXNVNUpsGdhdaAwF39QmAj75YrT3tiBAPF2wwbF9mOpRD5EIrXVBEJ0PJDonYr1P3wdzD9lDdc6LehCfW-xIlkm0pm4Hghmgk_YLtVM6b2kFSdqpLz_odWdw9QxiV4EcZ9w_0GuymHG6i9DiU9mVmtRbSIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
باراک راوید:
در خصوص مناقشه با ایران، مقامات ارشد آمریکایی و اسرائیلی استدلال می‌کنند که تنها دو گزینه واقع‌بینانه پیش روی ترامپ وجود دارد:
پیگیری یک آتش‌بس ۱۰ روزه جدید با هدف بازگشایی تنگه هرمز
آغاز یک عملیات نظامی گسترده و جدید به همراه اسرائیل برای وادار کردن تهران به تسلیم.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/68703" target="_blank">📅 11:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68702">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">⁉️
مقایسه ایران و نروژ:
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/68702" target="_blank">📅 11:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68701">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=uyqJPySNBW1IbcNXy6MZ7xg5kmPQka5zrcOd-5U5eofvl_Da9ZS8mZvZSiYCssU9lfAGUF2cPt67eVhhe_rQwdcdy7_LAm3rnYbT_p43NtX-3LcaI6C-eUePlmgtVieR3drgo2YzHrkeTeSqdRDv2GUSNYtzSkTJRosp2O78OgtaiqjoSYGAqf-z-g9zHpHfUeDLL9EY8_g8RPohmu8aB9JpMh5GuibveMLsGpeuNKu9YWC6oXDqdCI4MkVzU6Kcc4PrM51RMsdOiBSI_pmsLAxH4abOZ1SdlLngAH74sm2CzOQAijRoYGCFurJPjGXlrUVsLU8imxn6BL4r8mY4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75b4d07166.mp4?token=uyqJPySNBW1IbcNXy6MZ7xg5kmPQka5zrcOd-5U5eofvl_Da9ZS8mZvZSiYCssU9lfAGUF2cPt67eVhhe_rQwdcdy7_LAm3rnYbT_p43NtX-3LcaI6C-eUePlmgtVieR3drgo2YzHrkeTeSqdRDv2GUSNYtzSkTJRosp2O78OgtaiqjoSYGAqf-z-g9zHpHfUeDLL9EY8_g8RPohmu8aB9JpMh5GuibveMLsGpeuNKu9YWC6oXDqdCI4MkVzU6Kcc4PrM51RMsdOiBSI_pmsLAxH4abOZ1SdlLngAH74sm2CzOQAijRoYGCFurJPjGXlrUVsLU8imxn6BL4r8mY4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
اکرمی‌نیا، سخنگوی ارتش:
اگه پای آمریکا به بخشی از خاک کشور برسه، منطقِ جنگ اینه‌ که اون منطقه رو هم بزنیم و هدف قرار بدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/68701" target="_blank">📅 10:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68700">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=FBdPiLRbpCfRLZgMhVfR2Y3u-zN5BOzlFRvfgWzfJgmguGRvE45qynkjcR691SUjmryRuwXDxRN4i7j0cz7JPSwiPANH3dBD4nUfdJ8z-zbXK9DoNRFkc6-Ja4TRfvrc1SlcBJBM26ZAbuPf_frmePaXvSn3DVwhYk2SQHzJE1aMx4y5gxI9_1dLVlZegKJSD5l0ygBsbN9eeDE0nPP5uR23T69bN5zuZn9vVyaRZvCeYeCOAm1Czo1TBffyfX_acey6OGzyLgoet3sX695asMWgiKhFTv8k7QLpd5X2hTbcn20QU7RmBlDBtk8dI6Z_8o46kowLXMyCpgeAz1U0pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2573b8c6.mp4?token=FBdPiLRbpCfRLZgMhVfR2Y3u-zN5BOzlFRvfgWzfJgmguGRvE45qynkjcR691SUjmryRuwXDxRN4i7j0cz7JPSwiPANH3dBD4nUfdJ8z-zbXK9DoNRFkc6-Ja4TRfvrc1SlcBJBM26ZAbuPf_frmePaXvSn3DVwhYk2SQHzJE1aMx4y5gxI9_1dLVlZegKJSD5l0ygBsbN9eeDE0nPP5uR23T69bN5zuZn9vVyaRZvCeYeCOAm1Czo1TBffyfX_acey6OGzyLgoet3sX695asMWgiKhFTv8k7QLpd5X2hTbcn20QU7RmBlDBtk8dI6Z_8o46kowLXMyCpgeAz1U0pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در سال ۲۰۰۵، نیروی دریایی آمریکا ناو هواپیمابر USS America را هفته‌ها زیر شدیدترین آزمایش‌های انفجاری قرار داد؛ انفجارهایی که حملات اژدر، مین دریایی و آسیب‌های واقعی میدان نبرد را شبیه‌سازی می‌کردند.
هدف یک چیز بود:
فهمیدن اینکه یک ناو هواپیمابر تا کجا مقاومت می‌کند، چگونه آسیب می‌بیند و در نهایت چگونه غرق می‌شود.
این ناو بعد از حدود 4هفته آزمایش با انفجار های کنترل‌شده و بررسی مقاومت سازه در14مه2005 عمدا در اقیانوس اطلس غرق شد.
نتایج این آزمایش بعدها در طراحی و افزایش مقاومت نسل جدید ناوهای هواپیمابر آمریکا به کار گرفته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/68700" target="_blank">📅 10:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68699">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=gQ-ynXZRynUYBJo-nTcTVBTjrQd6Ftmu4WzsZncrhLGyEydFRnswCAbgB6o5rdaboIn2-L0rN6ae7csqaNzuCNbv7I27tvxg8EVY0SFBn_0pNlPy8-j787wvh-KcZC699uQvOVQc5bSOiiUTzmmB6ARTiYPxrPT3fJPy_uXqRm94cEO-KkUcETdlkrKHTYZMCYpVwhVzlqY7NjIXbFWCfK_FXpsRW34ilt9ZbHrmsFWwZ9xOg69_BL3oEAi4rMihu8vvbugZpILo053xLE26ZL7cdY8pgukA1LFanDtYmrN0bMaR5Hs7ixpH-Tj37cBBInQ4imhYc3Hzh1yROEWKPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9ecf589fd.mp4?token=gQ-ynXZRynUYBJo-nTcTVBTjrQd6Ftmu4WzsZncrhLGyEydFRnswCAbgB6o5rdaboIn2-L0rN6ae7csqaNzuCNbv7I27tvxg8EVY0SFBn_0pNlPy8-j787wvh-KcZC699uQvOVQc5bSOiiUTzmmB6ARTiYPxrPT3fJPy_uXqRm94cEO-KkUcETdlkrKHTYZMCYpVwhVzlqY7NjIXbFWCfK_FXpsRW34ilt9ZbHrmsFWwZ9xOg69_BL3oEAi4rMihu8vvbugZpILo053xLE26ZL7cdY8pgukA1LFanDtYmrN0bMaR5Hs7ixpH-Tj37cBBInQ4imhYc3Hzh1yROEWKPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
موگویی:
تونل رفتی؟یه تونل تهِ پیروزیه ، اون یکی هم بالای دربنده ، فرمانده‌ها توی این دوتا تونل زیاد میرن میان!
🇮🇷
عراقچی :
حالا
کونده‌‌خان
انقدر دقیق نگو شاید دوباره جنگ شد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/68699" target="_blank">📅 09:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68698">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68698" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYekbet Support</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQ9s0Ohdz1jEIC1F61UYpsl_265973s48YbwBdQjFM-vQQOovOWaz1BERMOFYn4pXieuhuu1ovU8CBE0PIIfTM8qTrf1PX2R0YUziBa80ZUBOFB42PtQKeFG8avMIoYCVCJSGTuquOqGVhm0tv-VES_ywpZLkZsb688ez6Q-gRW_2y6fBvl7Ju08iQNoQfnJpQhgPslmvVwjAk5MPgLbGQBJPE83f6SrynPFjIHv0fqNGj6kM90cAyLRTpDFZSLuYDZCeDv9RSfAsdbuwhw1cptFWhdVpMCslk-Ae-leSi3cAekLFlXSJzeCeVpgdq5BWy8vPDduTldIo6QE261u1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68697" target="_blank">📅 04:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZltrDHXVt6guSPd7QYKmGg56E2dhqGI6cW8lQ6gyiIxBHLWhhGYOGOIvQYGCGN7Pzj0Zt_o9H1oSJGoCnWeizOk0hI44f6XdHGFn81TDSS3OTy3LV56GHLATf18h7dMDhaU9sUSmi4Q3j7uFH6wq3OUkrQ-lrWFkd18CMG87gqDC5ETT3PRhUutkqUd_Gn5dUpsBeuapAKsr4I1BC6DpupEbmoA4qQSjBOlqO2UwNOVeeiD2doW-ujLJNNs_o-rd-jVUyiG1FPDJnCm66igbgZtEdmKL9Ujg9laTBxotpRDR7fg5dzbYTjdZhhUVrexmIvPQLTX52-7LBdXr1zoBZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68696" target="_blank">📅 02:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68694">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qiPRp7ryaqGWrhpRK7fDLVkh_9r7GDq0kv1tew2kdYDtpo87cLp5rlRjvZcB7jlLx2UBUeEVY0VovNVOButo_sV4xxeMfrY02SQb6ExmTr7lLjqtbnxDIDvzwq7lXf5eAnbUtGr9DuI_inUyRA5fFk3-zIpY4NakORTbIG1twGIGM5lvytl29Go7O-A8Kb7wpDTEvz7HdLea4XPu0kduMfcOUKK-YUqPAy1I6io4H2rEsfRe31UnIxgp1YTUs38sg2P1FgoBLEPLUDAMVSwcdhIBS82P0fwZJOnRubbP1hjNmetjjPZi8zGsFjGfHLZKx8XWlX-lBGG0-2ST9Klp6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
رئیس جمهور ترامپ:
"من گفتگوی بسیار خوبی با نخست وزیر جدید بریتانیا، اندی برنهام، داشتم.
ما در مورد موضوعات زیادی از جمله روابط برجسته‌ای که با بریتانیا داشته‌ایم، بحث کردیم.
ما در آینده‌ای نه چندان دور برای موضوعات مورد علاقه مشترک دیدار خواهیم کرد.
نخست وزیر کار بزرگی پیش رو دارد، اما او قادر به انجام آن خواهد بود و البته ایالات متحده آمریکا برای کمک آنجا خواهد بود!
ما در مورد نفت دریای شمال، تجارت، ائتلاف نظامی، مین‌زدایی تنگه هرمز و بسیاری از موضوعات دیگر صحبت کردیم.
تماس تلفنی جالب بود و خیلی خوب پیش رفت. من برای نخست وزیر برنهام آرزوی موفقیت و پیروزی دارم! رئیس جمهور دونالد جی. ترامپ"
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68694" target="_blank">📅 01:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68693">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🚨
پایگاه هوایی بندرعباس رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68693" target="_blank">📅 01:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
دو انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68692" target="_blank">📅 01:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpojz-MASnh_LSO_MCb9k2ZsW1loBjVAnrps9r0bwdVZO7jbBzsKTdhcGxxYy_TLGJ3E9tjzRQ2JlMHm4Kv6t6OFWlovmnkZ1_Hcs0mIptektMuSQji2_Fhy8j4Xj4KfUYUBRuW_Yy41DYjetV1WtOWfbx_hpbP5roLDmVL8AJQNMq5DG7BIle8nh_Jv2Np3mTH0tt9EzfOHBzs727CjwBYBPIdLiECk_HU7Ga2bbfTfpUyq_JwqENkZ2hfVSdQU7k97rJ28CtdDqApE12o9oIDo_vTI5XKUuik7ZeQCh7UCTpHDR2O7oyrL7AIRU8gynNPwK-lFuuJ1GmLOkY6TwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
سازمان تجارت دریایی بریتانیا (UKMTO):
یک حادثه در ۸ مایل دریایی شمال شرق LIMAH، عمان گزارش شده است. UKMTO گزارش‌های متعددی دریافت کرده است مبنی بر اینکه یک نفتکش از طریق کانال ۱۶ رادیویی VHF اعلام کرده که مورد اصابت یک شیء ناشناس قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68691" target="_blank">📅 01:42 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
مجدد انفجار در بندرلنگه
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/68690" target="_blank">📅 01:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68686">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kAcfFOU97TzYGdOJ_uAYDYX9CohQ_iy7nZ9h66WRxNgsj3wGfBS3osvhprjFYoblEL4TE348_Ly7AtFcYx6Zts4LB68jcyXU6fThLwmalAA6iF7vkAF1QZw-1eeMYTV4tMxUM8wUD3j78N7GXsQEoxumx3UNAIJiVroal8tp-pRrxGDboCG-gEpShGm6K2OgdrrHETAWCZFUH1DRt_e0DZQ10vwXlxCEe-9arYKjroNFiKM3juiwuElRkiNqZMHUNfgrzymtH3Q4K4WG-Qf21iKyz6g6ENBqdnSAud-rwIDWng1mQVEzjQIIJBNEAL84NI4QFNfyGpHeKa0Fn-rg-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aWByc09QF3GAhxnQSSzdHGoQXEjyGZADwO875qIu-m_G4sCNqZAG9Eev2D_QKB4vsP2QvZfCu97m13-vrh7PB6oGXX2bjNbFjFFn2mFhkoxVsqe1XGHYvYaJtjeg_ils7KdmNUCmA_A19UUajgEOBInI8U6a-imWXKOG7iUlayjsjGuUQQ2pZJ2pYOYNOSThILzDILzNqjkgCkveqkH1FmQHyxXYQT_6-0HdQzIXlf7XcQ7yg2nneQLAxgWUGmOXWB1Lb5-wiiXUVLrmmvuLNop1tR4tPCIm1ATQLRbB_jaQyoWTHu_-Cv8dUEoktJt_7E6wXX_5bPXgmSy2XLLlnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YjgDb3wGBCKVwVhhOxE2cPZVmBTWnQP5cDdUvgV3BbHRy3cFHagUsIN0ZJneLi4n4prSph8jrU26xdTyrUqNKussMh15h_5EQTgojJCYPI4XJ9Ns1NfwCbR2jiIAo-yAUbwwJWtkv4FsoFsSdLnoudGwZO610BKxdCBREOohCsDvnaruzSUnlLfhw2mm67kQiLcUHA5F_z8c4-WGfOzRHZ1jdkyV_o8Zt3BDyZfV2Tf4PSYhZIneQh-FQthaO4EukH_eT5c-n-eDMRa14pBk_Sw4_E-nVBLlkIPTMYB24bD1x3Vlii2CRxx4lBhpakmB4SQxR1ro2p5rlBLgc195IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oX2CgFrGOYcaxe5F8XuQmD8WctuPa1yY9fSsTluw7NzyWRyy4EbWQUKlB4RmI2TVxdCw9rgHfhwvDxPcAw4EjOJddY5QznYisMlbPfsy7ZKYCIpRqYaORVbNiXYNIbwZjl4MrCA3u0Xk_Wbk8hQDRtvSoGhr_ZBPg22uv4F-JJwT5-119QLdF2rw-Xenzpgf73_lGrdQ6TpXvLsE23iOEDdBt-L7KHGBh9662CjARzl1DYIw1UXiRr7fblfQHUjYhd1u2tOWvuzQZvrCfWRnntfa8bvLqfIm1HmBSoSJS9GxUOhp_lbyrrrO562g2h8NApgu8fUDhJZ-jp54uiHmjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
کوه دراک شیراز زدن
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68686" target="_blank">📅 01:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68685">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=ih5dL-dgCGiG5RIgo0osK6b5QshvbvHHkWQ3F_QOsWfDpJtTTn5WIIDt3qhTMaG5tMI-7sETZFXm_ZgF0II3Gl-fLlRKkZPXnCE69D9xsM__HJbVrmGhUqsbXpQUjgflfRFWJuzEMPjFHHvUGQn_MIQ9JPKcJnOnoDtON-9ODQSVeUhGf9uXg3KpLZM21-v9tTJvXHbQr-2Is_aZ2ZDF0MKxblLVzmEtQS9_LLzXgQSTn6uVVnaEUNeSb-goKzyIg7VdINUA3yjeljvbWmoQYCKwK7lQo89kjOpN7415fghDr3l3YF0PwK35DGpwqBiD9u1SklcCry_fklew2DV_Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bdf4b6292.mp4?token=ih5dL-dgCGiG5RIgo0osK6b5QshvbvHHkWQ3F_QOsWfDpJtTTn5WIIDt3qhTMaG5tMI-7sETZFXm_ZgF0II3Gl-fLlRKkZPXnCE69D9xsM__HJbVrmGhUqsbXpQUjgflfRFWJuzEMPjFHHvUGQn_MIQ9JPKcJnOnoDtON-9ODQSVeUhGf9uXg3KpLZM21-v9tTJvXHbQr-2Is_aZ2ZDF0MKxblLVzmEtQS9_LLzXgQSTn6uVVnaEUNeSb-goKzyIg7VdINUA3yjeljvbWmoQYCKwK7lQo89kjOpN7415fghDr3l3YF0PwK35DGpwqBiD9u1SklcCry_fklew2DV_Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فعالیت پدافند در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68685" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68684">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGRf1z3-YZgQ3AhWWx_ygbzvmgoquoM36Vw5xr3PgQmhAxHCqj779wgooZF23jwL8K9l9Yt2TxByoD_RWaLOoGPKaHeePbU3aGUHVCYpDoWHqmxmKa7SrWptY2xCZWtONryhetacG0urSS2Yke7HymYcDDi47kPRtUqpSmmtmuO9keQEvkeqsKhF_ZS2cdeIkzRpTzwRMUu4zIhbpKcZBPf2vavB3k4AuTT8zCbVygvQgMVFuLmOKOYxugoQ2s4LxqEsGP5zChFaAsD6onoKBw_3JWhxagU_hUGTKKDalf9ya8_9j-EYQM8KcPH1hjxeZyBDswYfedx48Sz-N0csug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آژیر ها در کویت به صدا درآمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68684" target="_blank">📅 00:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68683">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=u4EZMygMjXVvHBDbX3aGGtM9bCUbZZTlzHtmxP7VLfexfkUJ9MdQ0S4GUXHQXjAcwQd3nwcMjwqxTxuYnIB--M9-Liy8IiNF6bl0ZNJlGJxlB6uaW881W1_CnX9pm5F1pfDv1A3OG8xQ4o8rHCao7UtjsCXvkJ2cV-13_Ksch1ZvlJh6N-bPiOiNT_5c6B03tyTT5HVIilc75EX04Syn-JG9TZYyFDCHZTkf6Sm9jhC3BK_W-kc3IVmRJS8M1iWzeXfI8LNszRnPEqycEjSf_4Lo0CvUZoI1f4-GaNU9Gb8G9eLMSTSlGM90_a5gqNVlbUxIyaJzdm0fV1coRfdXgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e6040eb52.mp4?token=u4EZMygMjXVvHBDbX3aGGtM9bCUbZZTlzHtmxP7VLfexfkUJ9MdQ0S4GUXHQXjAcwQd3nwcMjwqxTxuYnIB--M9-Liy8IiNF6bl0ZNJlGJxlB6uaW881W1_CnX9pm5F1pfDv1A3OG8xQ4o8rHCao7UtjsCXvkJ2cV-13_Ksch1ZvlJh6N-bPiOiNT_5c6B03tyTT5HVIilc75EX04Syn-JG9TZYyFDCHZTkf6Sm9jhC3BK_W-kc3IVmRJS8M1iWzeXfI8LNszRnPEqycEjSf_4Lo0CvUZoI1f4-GaNU9Gb8G9eLMSTSlGM90_a5gqNVlbUxIyaJzdm0fV1coRfdXgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68683" target="_blank">📅 00:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68682">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
مجدد بندرعباس و بندرلنگه انفجار رخ داد
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68682" target="_blank">📅 00:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68681">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
انفجار در اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68681" target="_blank">📅 00:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68680">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
انفجار شدید در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68680" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68678">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d45723674d.mp4?token=bCU_UHtCXQyHcOQLPJiveZ5TARfnLWEQekdTZ7QEb1w0JpJT2KkIOsxfPhC8khrxLPRxQ2oCcJ-815j6dGPgnu-TvuuY_LWc5U1AVsrn_r917Um_KRwqhK7bUgfus85hvGigofiuP3hbMx-_v-2XN-7n1POB7QVYwkNjsQxSZhLJ9-uy116PI_StPM2XHKud_HBnFK0hYvDxUvSCIkV4U-iFuDsKCG6Rg1RgQXjYhosHGBVC_1kHRavKbSP48ZfEhcrQKY0vmWr6snhHu6l41uJcmqwsQxcPn55yS7AvMRYSRYgvh2IbD4r95Canj1aab_5UkTZ8vV7-KuAVi-KiTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d45723674d.mp4?token=bCU_UHtCXQyHcOQLPJiveZ5TARfnLWEQekdTZ7QEb1w0JpJT2KkIOsxfPhC8khrxLPRxQ2oCcJ-815j6dGPgnu-TvuuY_LWc5U1AVsrn_r917Um_KRwqhK7bUgfus85hvGigofiuP3hbMx-_v-2XN-7n1POB7QVYwkNjsQxSZhLJ9-uy116PI_StPM2XHKud_HBnFK0hYvDxUvSCIkV4U-iFuDsKCG6Rg1RgQXjYhosHGBVC_1kHRavKbSP48ZfEhcrQKY0vmWr6snhHu6l41uJcmqwsQxcPn55yS7AvMRYSRYgvh2IbD4r95Canj1aab_5UkTZ8vV7-KuAVi-KiTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/68678" target="_blank">📅 00:35 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68677">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
ایرنا:
در ساعات اخیر صدای حداقل ۱۴ انفجار بزرگ و کوچک در چابهار و کنارک شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68677" target="_blank">📅 00:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68676">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">امشب دهمین شب حملات به جنوبه، اگه این حملات یکسال طول بکشه، هیچ مسئولی حتی آخ هم نمی‌گه، چون اینا با حرومزاده هاشون راحت تو پنت‌هاوس‌شون دراز کشیدن و می‌دونن کشته نمی‌شن، پس تهش میان می‌گن چند تا #پرتابه بوده، دوای درد اینا همون مردیه که الان تو اورشلیم نشسته،…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68676" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68675">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
انفجار در بخش بمانی سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68675" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68674">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
سنت‌کام:  دور جدیدی از حملات به ایران آغاز شد.  @News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68674" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68673">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
چندین انفجار سنگین در چابهار
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/68673" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68672">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68672" target="_blank">📅 00:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68671">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTpKDircmL9zQ6eMJwZ6aR6It-x10eZMy9NQ5OtSZSNsJZsVGehfwC6dTLG8kyZZ8N81FRtk4p8_Qyi_n7hthA0p_o6BLkW1uvVK3c2ZeD_-HezesqD3GD9thpbafgeASCC2YMCbJ-EglIsN9_I8k292Z3gy73Wopg3evr30cDwDW6Bu-WQ41AXFgjhdY73LpbmZJpX08HUceBv3aRp9JPDPYq6BT8SqIPPMhA8CwjqvoGzNvyt9l4hT7MXoPvgnOli4PbyjLt1kldBLs9I76DN3SELw5e536lPkBjNxduKoSNN1aXNw3H42Q3bqwckSZqMIRw3ebDTV4I5tiRbsHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنت‌کام:
دور جدیدی از حملات به ایران آغاز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68671" target="_blank">📅 00:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68669">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
گزارش‌ها از آغاز حملات به چابهار، قشم و بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68669" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68668">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRzXfrlMIVcLyVaLeNZZBMgaYQdSxEzP7IY8R_JPMd-DoBE-3IgVxIXEchfho_sHIyUGTkJICdCHHyzGIxYoWM8Bv9SeztD9eA8F2zlQbUplL7XGDwv1h-aPyTULDkAmMCAOpGLH8mh9FxNV6aS-wEnCa8OJsVJDRb-X6x5MuOP6v49BGRCyjLC5WAvVzYDbMJsa80JArwONSf-MwfPE0rwYqQjb0YxK3yoKxAi_VENNEFJEm2SUaHY1Rg6TL3uEXCedwHmpPAvFq111v6Yzo1ex6YDAJ3CCKCn1xyRZhqFM1_T5RU13vNpiYAoaIW10DwTBhUrjHkTr04DgRoi1Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
🤯
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68668" target="_blank">📅 23:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68667">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LO0Rj7_WIQUWvQ4Z7DyNnQktYJMiZNQGOsXdUCCkK5jlgL3PrsoWOKkvwCF9-BBFFUxM3EaTgC40CpwuRNTTpbUh9NXdFUmnOUYWtKMPXJj92Px08liq54v6DAhKhAJu7dUSqptiyu3HdgcRRXca2siLqnGxFTd1lApjEiBgsvS14uk-B_6SZm4UAjWNimdWcaFE10Rg1GcPYmMsCKtY9ArJvyz6EXZ7f4R9-ZvbtgcsFO7sI48jpbSEyZiAHYLsQgCFtNLB5NIdpFHribJiboPSPJ7Nh3fTVHHZoz6nI_Widj0RYzstc0JAo5WwZf67wQKP-9ifFfIVB-lLxR0n2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
باراک راوید:
«در حال حاضر، تمرکز رئیس‌جمهور ترامپ بر این است که ایران را بابت نقض تفاهم‌نامه (MOU) و اقدامات تروریستی مداومش در تنگه هرمز،پاسخگو کند.
به‌علاوه رئیس‌جمهور، ایران را بابت مرگ اخیر سربازان آمریکایی پاسخگو خواهد کرد و هزینه آن را از این کشور خواهد ستاند.
این ضربات سنگین تا زمانی که رئیس‌جمهور تصمیم دیگری بگیرد ادامه خواهد یافت، اما مذاکرات میان کشورهای ما همچنان در جریان است.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68667" target="_blank">📅 23:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68666">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🚨
دو انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68666" target="_blank">📅 23:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68665">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=PjIHYHq1CUy99uQwQpnd96TPNLpqz8k-mZGRX_dNvZWaK5y9qhsRv4Rt73V17Lsev-06jPIgFG0KnViytPTpFCGyC9iteTTc4PEw7aO97Bn-BKDQR6FB4aExooQZwT0fvGLUDd9NRwjZeopwqm3KGcgViN7lNzQGtO8yIzo12wgMoE5cTH9ttunc5iSP6F3I1Tn60gkZKc6A0sAsaETKuOp9ycei6YGUfIcIyTTuICljQe2rFoVH5TNMQiPn0fww1md_byzZEu2u5xw9CNbA6TuXRubDFeaRb5w_S5SmHPIAFVP-Tts4Q4s8qvPeWmNBHwS5_icPavcsPJ6ufQZmAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeabf951b2.mp4?token=PjIHYHq1CUy99uQwQpnd96TPNLpqz8k-mZGRX_dNvZWaK5y9qhsRv4Rt73V17Lsev-06jPIgFG0KnViytPTpFCGyC9iteTTc4PEw7aO97Bn-BKDQR6FB4aExooQZwT0fvGLUDd9NRwjZeopwqm3KGcgViN7lNzQGtO8yIzo12wgMoE5cTH9ttunc5iSP6F3I1Tn60gkZKc6A0sAsaETKuOp9ycei6YGUfIcIyTTuICljQe2rFoVH5TNMQiPn0fww1md_byzZEu2u5xw9CNbA6TuXRubDFeaRb5w_S5SmHPIAFVP-Tts4Q4s8qvPeWmNBHwS5_icPavcsPJ6ufQZmAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو یه برنامه اینترنتی، به ایمان صفا (بازیگر) یه جایزه 12-13 سانتی دادن؛
مجریه میگه اینم یه هدیه کوچیک از طرف ما که به ایمان صفا برمی‌خوره و میگه بخدا این کوچیک نیست ، اعتماد به نفس ما رو خراب نکن...
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/68665" target="_blank">📅 23:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68664">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OSuybVvmSm0AYK0c2wOT36a2ZoT9euvzeZNepQHOv4jXVYIqrNcQDhu5dSKBf7Eg56CafXSOQv_I6lh-wFOV2hBTXWoASSRDGZqZPck8Dh-kBFAULsDQpV-buBN6ge0d3CqxR6AqMd3OrLBGiOqTZi5XMdnAjqE9MJIn2v-XN2xB3-hP3HvV3Z6mtOR4euwTUK4hPcBEC1NifEU8NKPaxAqxNQbs8vHY7G3QSFpweh8nkNN0Y8XGDxXSirFN5J3DyUQREwclgCP7If_7UAfkAWzzve3AujtqzJWZxkODmSvD3ABlsf28T9XNjuAllnt-vV4RV3DI12LwBpPxkju23A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان تجارت دریایی بریتانیا (UKMTO):
گزارش وقوع حادثه‌ای در فاصله ۱۷ مایل دریایی شرق دبا در امارات
.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68664" target="_blank">📅 22:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68663">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
رسانهi24:
آمریکا برای مرحله بعدی کارزار علیه جمهوری اسلامی در حال آماده شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68663" target="_blank">📅 22:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68662">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/675435558d.mp4?token=eIatgvEjwJERlVprlE6foV8z26Ni12KUekptwFBvUfizSgGhnoYRFU3E9tZoAKxAFyfpQqd-W20lodNH9UnDTfJOlAP1B_UzWcabaHQDZzCN50Zdw6GFxsA2mRWjYat4KWKuF10qqk2gnQePBWYvw1zb78NyTgWVJe9mf9L7Y69smUlEDwoudqtuB9TNq4xOokk7kVWSK2EaDrez1z02cBBPW9g5e7sfhAeR15srGsje9txEeV7jf_DAy6tDh2nXNfl71LnJ_RFZPxROsRGSxJksMN1XEeIyimL53DlhtZZopEKQDP7CKeQcqhxlWXCGYk5bwiJAAi9ned-sqP_LzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/675435558d.mp4?token=eIatgvEjwJERlVprlE6foV8z26Ni12KUekptwFBvUfizSgGhnoYRFU3E9tZoAKxAFyfpQqd-W20lodNH9UnDTfJOlAP1B_UzWcabaHQDZzCN50Zdw6GFxsA2mRWjYat4KWKuF10qqk2gnQePBWYvw1zb78NyTgWVJe9mf9L7Y69smUlEDwoudqtuB9TNq4xOokk7kVWSK2EaDrez1z02cBBPW9g5e7sfhAeR15srGsje9txEeV7jf_DAy6tDh2nXNfl71LnJ_RFZPxROsRGSxJksMN1XEeIyimL53DlhtZZopEKQDP7CKeQcqhxlWXCGYk5bwiJAAi9ned-sqP_LzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
فعال شدن سامانه‌های پدافندی در اردن
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/68662" target="_blank">📅 21:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68661">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8U-aiuKNc5SoQ_9tjkDTOpsxhoKlXcrHQjzskJMNDHR7mMhuwkddx_VIMS8oLSuA_stV1vDYsIEXQJ8RNq-exIB2fPF0rd9hLNp0hvulOa3wWdchRe0ws0VLYwNHpjEwc9Kt6ePbdXzFVNUxPeNVKONPT2th_GkcXbhagAYtTTXjbXYGvbdpB7ne1Yt9PH2BE3iWeuym7ZpoDudxZ4Pl3vAAuoR4LeCuOXBDVzRS0Ut0kznid2A0-UxEMw1xS9TvTh3j10ihmHYOu1oMssbaWHmR0KLU_Mr8jUFpJp0XJ1qsGf2jX42Bv7reSNrc-bpdQyUANdoeWn59jz6ZL1vhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/68661" target="_blank">📅 21:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68660">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در تبریز؛احتمالا موشک شلیک کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68660" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68659">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🚨
نایا رسانه عراقی وابسته به حکومت؛یک منبع در سپاه پاسداران انقلاب اسلامی، که نامش فاش نشد، اعلام کرد:
نیروهای زمینی ارتش ایران در نزدیکی مرز با کویت مستقر شده‌اند و به نظر می‌رسد که نیروهای مسلح ایران در ساعات آینده یک عملیات امنیتی زمینی به سمت کویت انجام خواهند داد.
تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده است، و نیروهای ویژه "صابرین" نیز در آنجا حضور دارند. این عملیات ممکن است در جزیره بوبیان انجام شود، جایی که موشک‌های آمریکایی از نوع ATCAM به سمت جمهوری اسلامی شلیک شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68659" target="_blank">📅 21:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68658">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bDdVsSuqQRbrFWvTv8Altz8ZP9Seisuav-amCNOKHsoJiy0W79LLJTR9LFu3abglcYBzqiMvY0Cb995and6h7nRKWtPrxXiNWUjU2KnHVtLlZeWzt--KyhglxqTcx7X8UkBtSabke28n8M6eedK25khFbqtrOq7lbqIXwIFg-zkMEsYi89EU6AjHADlUdncY2I2SBBZIWeVEfAGYMWL7OImUdp7TO_rDM_W7lfEe6CvW1PMUEZ7f24hYZ0JeewIVAqZIieUl8glVMtxktMGc1wZtfIl_a6PpNN4GnvdR9zQssgRrLEhOXKo2Ac3T0L09r5QTX3hCWdQTtR8paScmaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، توسط شهردار نیویورک، ممدانی، بازداشت نخواهد شد و «اتهامات» مطرح‌شده از سوی دیوان کیفری بین‌المللی علیه او را در خاک ایالات متحده، «باطل و بی‌اثر» خواند.
«بنیامین نتانیاهو در دوران حضورش در ایالات متحده آمریکا، به هیچ وجه و تحت هیچ شرایطی بازداشت نخواهد شد. او در حال مبارزه با جمهوری اسلامی ایران است؛ حکومتی که اخیراً ۵۲ هزار معترض بی‌گناه را به قتل رسانده و طی ۴۷ سال گذشته، سربازان آمریکایی و دیگران را کشته است.»
«تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این چرخه بی‌سابقه مرگ و ویرانی کشانده‌اند؛ مسئله‌ای که رؤسای جمهور پیشین باید سال‌ها پیش به آن رسیدگی می‌کردند!»
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68658" target="_blank">📅 20:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68657">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPeqJZub1wcNeWh2WwRNSXL_NwUr3q31f7OB0VLHrJqIcibVLE_108grVjXhxNxK9xWgBgR35Xne5v4O90LmXvJnVtKRjEf5M7H0RrPCQScnfVsWxvOv3ZHwcE2ygaTe8LDqGNgGrYE4iIxmIsRCkWdJH5WYrjf__LxK3ZZYeVnmgxPrJw2mKkkOr-Yb6utzZwiM8AfOVoYTT-5FZrMlkzTzg3IYZFv9VQmjJG_wiQobJE-lzJJ5m7Y_cBYZOF_CorDNVNsHx5yplZ0j3vienSNLP63yCxqlwyt80q77xIOcFhTCFL_nxcHzATsbjRlnsAPs8fZsHK5yW-HdAgQx4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن کشتار را چندین و چند برابر خواهد پرداخت! این دستور به وزیر دفاع، پیت هگسث، رئیس ستاد مشترک ارتش، دنیل کین، و تمامی فرماندهان نظامی ابلاغ شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68657" target="_blank">📅 20:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68655">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GvicgRhthyflSryr0IKi-XOWyHfYvYqxRn49NkjYzhIP_mpXYAGjBe_5RaRyI9vB5o8Ht0LV6GeXW4FoV-Tpa_RZmnmTM0h4goGDeT0YgpA-rzxYvxCsgFdkAphZ3wtyPvgaMbJSBqjxUa9V2LSat6-hhDdrFsHL5iSGLnLDymRbosFd4Ce_gs-IdBSfWgPF_w1VDUAFcRoEzzjnhEBklrFeBocnAv5CNgjMBYjWkcNbbBA0aPbNbc6-qTiwg_Qwu5qCUy_AvLgsZjDfO27gxybacEDnoby9kwiA-mdg8prlGbGi3axtLRd7EA8hx_whqp_pyGVpX7QXh3ipBMmKBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MEMGMnxpz95QuPCCh3V4fo2jjvMu1sMkwriW7VVMnM4iZWgWVMmwsTfGzkGXbXhayyXca1IetXTxjwfoD4JaN4zfMTss9qjBqyS-Yip8mpkIN1_6BNUGtJbEnK1CYkv89SRh2Y0r6dr2wNCrw6ZDj0n4jyvkTzJbLDmyP_6U23gqS5TFG9rNTMFRX1f1bLBQ2OjVgLSXEaYtFUyrfMVkSggbzkhhB0jw7ayHr22URiGmAPIEpzZAOqnaK3nwGYihsdTyQR9Z2I1D5DysaWOE6gZ4StZLRlW5V2_rxw_CJyy7erGdLSu-rZfALB1_pEE-LBjVTFzQhXEktLF0OesDnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
وزارت دفاع ایالات متحده هویت دو نظامی آمریکایی را که در حمله موشکی بالستیک ایران به پایگاه هوایی «موفق سلطی» در اردن کشته شدند، اعلام کرد.
تایلر جیمز فیهان، ۲۵ ساله، اهل هاوایی
ایزابلا گونزالس، ۱۹ ساله، اهل تگزاس
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68655" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68654">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sZGrxkiyMFsED51TATRN-H2ddKuGvDOFGi6SfvXXBjeGkF6N3BULm1CaHZoXDDDAtDNtKI7613qS_BA5CZ4c7FXeq6FK6UncKYDH5i8XPSQtiewib5QYMITtlPN8CK8lcLIShEAgYY55jAIVpWZShDdCoQXjN_juab9WfX58APuX6_mB2uLFUncUUEOWGcrjqiWut7Bei87ANKsti-xgeM416-OjiyFkm5NtYCLd1HZX3dLP0Qd4sZKI-490mqDj6hPdzp7_t3caZp8kIRW5maUECj2TNstnrebjTwCMLUxMrZrTP0BqT9J4dk1hzgfv9AfOQeux_Hn5h86b9_-W7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امروز امتحان عربی یازدهم بوده، توی امتحان بخش ترجمه چی داده باشن خوبه؟
فَشِلَتْ خُطَّةُ الطُّلابِ لتأجيل الامتحان
ترجمه : نقشه دانش آموزان برای تعویق شکست خورد :))
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68654" target="_blank">📅 20:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68653">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
یک واحد صنعتی در حومه شهر خمین حوالی ساعت19 هدف حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/68653" target="_blank">📅 19:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68651">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ-U5oVFHLKyUQsQaWUFu9i4Y9IBzdO4WD24fhSqMDCrWIxRsQwwrNm_BP9sS-KX9sAq4UnIZlSD6VgjHfPoxzEjhzTf-aK09bDq-1R1GVC1crAAmRIq96prwbZYKwdKbc9vz0rnLXpft7kyxLfIOcEzNGps2F3dkJ9dgdo1e-2YKMN7RI0NrePUwAZ464lE4DaNdUNXUg5Q_KUa1x0bQMvWfWf6_BvzBHzrgsXWUkD-u4grtM5vOI5M-azL5Os_13THXKK4H_aJVGhYW97aaYQtRpfWk1bihmU8qoRPuQDbYbmofBfg8wdcBzJsiyCS5j-DFjyrN78bXasGHOq8Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=aY7wK3gTNVJ_w-XRnpXYfg10nl3QoAAtVRwpA6_Zb9CE8yxe62_5POlXWop-oE4n2uRHDmixqf66L58nQyVZmOK-qPUuyYa8dT9gEBICc2VvoA26GOs2eZNFgN-9rrbnm8b_QomjG1DKkpYTpzj6-SZbvtG-robgmK8t-Rt_81eE6B1hj9m-kVsumKTHuKLZ5strLuzebPGb8ED7OAkZkCJfwPm-V1sLDZbjNd6LsuLqsbLw3wV9frYVUiklPrdn4M65x49f5zghIiwKGJkGnxuMNgjgcg1_4H3QENFtnsBR8JSTubGz0HNs0EEnkar1XK_VcM6vmeeuLNBNM0R8xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/246e0b466a.mp4?token=aY7wK3gTNVJ_w-XRnpXYfg10nl3QoAAtVRwpA6_Zb9CE8yxe62_5POlXWop-oE4n2uRHDmixqf66L58nQyVZmOK-qPUuyYa8dT9gEBICc2VvoA26GOs2eZNFgN-9rrbnm8b_QomjG1DKkpYTpzj6-SZbvtG-robgmK8t-Rt_81eE6B1hj9m-kVsumKTHuKLZ5strLuzebPGb8ED7OAkZkCJfwPm-V1sLDZbjNd6LsuLqsbLw3wV9frYVUiklPrdn4M65x49f5zghIiwKGJkGnxuMNgjgcg1_4H3QENFtnsBR8JSTubGz0HNs0EEnkar1XK_VcM6vmeeuLNBNM0R8xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
دقایقی قبل شلیک موشک‌های بالستیک به سمت پایگاه های آمریکا در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68651" target="_blank">📅 19:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68649">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjvxYXL-r_QSpaPwScSQkUbB-zuFqdEmjmD5PKoS6OCcB7WALunA_UYwEpFNqq0q4nommcB-0vTpHLYgJLvF5QbMk4e2Wova_vfOnlYcpF-pKkKsHvGIp1mkxI2OFAghDXwW_k0fZ589bQKrzhvmMX8u8VNzy2Keqfr86QAGGgRs2ibl3p8MT95W7lYX1HV-k_v5aWA5HwazpC78vWwO2QrSU7mv7siVrxDjw1v-iOItOCWYPV-hL84pmgRDcNFB9coac9RJsePwsidYEMyIJlOXsRr3gniYDvX5Av0-RNG4jx-oZZ7TmqGGiNP5PgcoD_r1syMXgh7tU4_PCkstlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=MJEyaTpcAFpvA6-W4bXrSti3y9I7IOVoElrzQisk93VqdjIjwYNRJfajfIGngBNHoI-WJSVw8FpcAAioBqgRUuDA4mijgKlZLv4-mHVHCIs6VJJ8vUEXK6uSMZGoQDHqJrzSNsO-kK-c4VOLpGdwBE62D60sQmUk8UnzPYvghbTJL9Hzh2OIcefdrtBtHJ8xxFacrFfqJMZ6PnUpnXFhV1l6u32AWT0dmbN4w3p5SiQ6dS0ogOB1OBo9CoaLm0HBsJh899UmkT1gWazgNSB4DYg0bRUS0VZXmvlWKKr0M5LDb6S_-zxNlxX6r0LqSQ7yJVH_tSPXO2JRW2bEY307uQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e216a5ddb.mp4?token=MJEyaTpcAFpvA6-W4bXrSti3y9I7IOVoElrzQisk93VqdjIjwYNRJfajfIGngBNHoI-WJSVw8FpcAAioBqgRUuDA4mijgKlZLv4-mHVHCIs6VJJ8vUEXK6uSMZGoQDHqJrzSNsO-kK-c4VOLpGdwBE62D60sQmUk8UnzPYvghbTJL9Hzh2OIcefdrtBtHJ8xxFacrFfqJMZ6PnUpnXFhV1l6u32AWT0dmbN4w3p5SiQ6dS0ogOB1OBo9CoaLm0HBsJh899UmkT1gWazgNSB4DYg0bRUS0VZXmvlWKKr0M5LDb6S_-zxNlxX6r0LqSQ7yJVH_tSPXO2JRW2bEY307uQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آتش‌سوزی در یک تانکر نفتی در تنگه هرمز، پس از هدف قرار گرفتن آن توسط نیروی دریایی سپاه
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68649" target="_blank">📅 18:54 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68646">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VJCp-KrHYN-kqsC27pdAEDYWzKHYNnxJi0FJOcxHHMeYdnWP_TGRyZwFaGmjA5ygVDXZ8evaJ_Q5Ts6yHlFv3NWqvGbg2VM7nCj6oUr3mKSqcC0IXw-w7Onfq4BXR3GXY-9Nky2disbFq47VFe2L4LQtQoDq9kmNEzi9H9p0QPfkF7FQ2gkFVEXZx7Ry2mnqaS_vbm9gBe1p1xxyNWeTTHIcN0nhuVhLcWx9FW46LqIY2YE6i6o5Xg56AJZnDCOvv80HqU_zArumqX3TviLQJdGCpy-y7fPl47xBnk8hrgW_fDQpzMkRbdVKHdKjFQI3cOumIgFiMBPz4YWqooCFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Er0V0MIH1YR86HzRfvV6lyuGCoWwHuEduHgxOdxenVpfU2LI9LMp7NcRnRgN1oqGw18AqFNHHHwz8KT7Wu4sPf2YmRpGM9j4xTemRVytxa7VANYnBgYYatWlDWev7cB0SaTBml7IVomQz8lZU3GnNKTwbDGXJPDfwDF5yHeZS-xtTzp3HUS52_j4IZG9FsplXK46JsCeJ6n8vifhdjqJ1QKBm83XUXGj4uZwxPTUtw6v5P_ytLDaCe-6Wm3kA0RtU1Gg7BQi5NCWcE_n8HlECJqinDZ9COJaMk9tRb0REAahnyI2E7h3p7AZEhk5sNeWve_vFSLkTResGAuJsjVdCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uVz0fxgeZpYx0OD2efi3EPACyobdbL2JWTzBljnS5du7MCSEb8MBLxtJcMNYKqvNtnVxseaKzRC9C4ayozcTdV7eAuW8xSnOajbIs0yfkZ7ib0PKyf53sEMLD8ixkc8z7Z2wzI0F4ZB5V6jyD6pNZ6ru71zgqqhl7_dboruvTrhYXmo4Akn0zxwNwSp1dzwuwHgCB_r3sSSWuH_fCOH7LJJpVJKKkhVQlt_uFGLmk_Gnqy3b9rB6AtQj-7CTCCEGeMKrHH139xrh6sBnjU_L2eH8s6ZKqohh1SDlq25oEj46C-MSeZNPAQa1Y4nw04Rn1e5P1b6OCSqDrlGhBxp_iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
شلیک موشک از شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/68646" target="_blank">📅 18:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68645">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
✔️
آپشن های متنوع پیشبینی
💥
برداشت سریع با کد پریمیوم ووچر
🩸
هدیه 100% برای اولین واریز
🎁
25% فریبت ورزشی برای واریزی‌های ووچر پریمیوم
🔝
با ضرایب بالا، بردهای بزرگ را تجربه‌ کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/68645" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68644">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d4b8jFswqydFdIIVBwIgpnDmdW6Yyju710NMdok0od6lc31kmk8SKS-ASUbQs8vfpV_Qp7v5EBEhD9kmaZ7MDvflYtU0mtUgjnyiM7ikkAUrsGk4CdaghEDwUO5Kn65wwYpxV_MFCDKDaha9_LPAHu9knCeir4TwBJFznI_mN0I_UFwz4_W13JgXSvqLCvhYcauRV-b6Rqzp_o6qJWqXTaycByypyZ0ds4MgZ_ARZr-zjYSKsG3ZPu5lbLM-ku0kr-aDSGSBr6ODnotrtBKI4JTZ2JPPkxh36ICF02rRJXQO-6nT9JSJOYhUox2GGlMVja58upn2UYU_B3VVcUe3Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
📣
یک حدس، یک برد، یک قدم تا برنده‌ی نهایی
💶
تورنومنت
صد هزار یورویی
گل یا پوچ
رقابت های بازی جذاب گل یا پوچ در کازینو
creedroomz
⬅
️
برای ورود به تورنمنت کلیک کنید
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/68644" target="_blank">📅 18:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68643">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">🚨
❌
رویترز به نقل از سازمان عملیات تجارت دریایی بریتانیا:
یک کشتی باری یونانی پس از اصابت یک پرتابه ناشناس در نزدیکی تنگه هرمز، آتش گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/68643" target="_blank">📅 18:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=TqUTV0iCFMg0i-KgBrOpnrZyYP-uEC2HihKGsL2PWs-_63m8h0q3ngu0uuWFPBJBRAOvdTNcOlJhzMg02oleG8SWhTQSm8nQTnmCNXHbu_t3jzsrC7zyfCKuLESjGg1Yiim2ADu-opZ8amHgV9k4NDV6sB8kYpJAy1LuLoDHWXObYeXL-U3AZqLTMaQunUweUXa7nJj2ua6Itt3WW2m0FFRHB-RJFoNodzBFOFiitN3ctkyZ6k6eK1ODbVQVsZfoPpQkARs7yeavmwCk_5dYoBBRE_HMeanB3eGkPKns-vDXhgOsraewC9VE6YI9v9vX1UkKYDclzqrEbasBZXLEHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc4ef2082.mp4?token=TqUTV0iCFMg0i-KgBrOpnrZyYP-uEC2HihKGsL2PWs-_63m8h0q3ngu0uuWFPBJBRAOvdTNcOlJhzMg02oleG8SWhTQSm8nQTnmCNXHbu_t3jzsrC7zyfCKuLESjGg1Yiim2ADu-opZ8amHgV9k4NDV6sB8kYpJAy1LuLoDHWXObYeXL-U3AZqLTMaQunUweUXa7nJj2ua6Itt3WW2m0FFRHB-RJFoNodzBFOFiitN3ctkyZ6k6eK1ODbVQVsZfoPpQkARs7yeavmwCk_5dYoBBRE_HMeanB3eGkPKns-vDXhgOsraewC9VE6YI9v9vX1UkKYDclzqrEbasBZXLEHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ستون دود در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/68642" target="_blank">📅 17:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68641">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
فارس:
خبرهای اولیه از مورد اصابت قرار گرفتن یک نقطه از شهر شیراز در جریان  حمله هوایی دشمن حکایت دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68641" target="_blank">📅 17:50 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68639">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u2C1pwwV_dBMPv-5Ve9lFm7D4dlmwzb56jd9Oc9hNP5v3IjwzGS3lrOZiM4tYLGHQXB3b1ZRYy7dLVQSXAN4r9josMzu_wYkMCDsRjUzWqRR7ucuF2uRK1VusUDi0glvdXQe9IP6IXEIF3327HafBTkVoCpYJkX2xegDiHc9Vj1sxdZ295XiRnWgTsuhytEJGqiMxraiZ3RS6j7haCZwcMOysskDp41IzJtiabhAndTLNJnoY4jf9weFPUJmQQ9dxGCqpX4pKzSBl-CTcVNbsr9XxphEkyqNsK5ClsaSbAMz4RNBzy0YeLfRLgy5cR8He2dj_wMqY5MMrblhRZFqpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HS9gUEC2nMDf0_VOesFZgjFHqlG0t3Ir99Xq5HAi8RY44RUC6HD7DBZo_0MMp340bvHmj21lzvXIchyEC5cVFZppbGGPGfL1ogKUSkB_9PCkkE8V87OPAZit2eSb6SPj0ODV-nmblPW7_xdDsZpbCsYUj0EQSCzzUlqENhGodq0J6HbLsSjllN5t8e0893Kzy-pVeE1R5w-qYKP68rFI2ta-IE69VEGKZgnI7AtVnyw4DfGLSqM5w-pkU2ad_Y37X_goswWdeOZLWfi21VSeqDmw1zCZJNN_up14wUZdXD4FZOfvQj9xYDCUOsQqoaGyX0MtFBNKDrhOpNo59L2DPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
⭕️
گزارش های اولیه از انفجار در شیراز
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68639" target="_blank">📅 17:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68638">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">⏸
حملات نیروهای مقاومت فرانسه به رهبری ژنرال دوگل به زیرساخت‌های فرانسه و منفجر کردن پل‌ها، قطارها و خطوط راه‌ آهن در جریان بمباران‌های متفقین برای آزادسازی فرانسه اشغالی از حکومت نازی‌ها (1944)‎
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68638" target="_blank">📅 17:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68637">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQHUxyvjP4LeEOTYbakvO8p0d7N1Sw5ssYoo8fOuZ7ZHX20cSC2j9N4rUXEtuaif0F3-jEjvbDk51F48VloLcpVRAIa2sjVLOQn4-CbMatZTcqFdH5Mf7hu2Q5kYrlOVVQBA9_VwGpObzIX5N-puXORDKzWPiMTzSrNmPUJMLvoxxkMfV42DVNLMrz6UzNkC5Q5SQXX1aoqDSzu8eWq5BAxpCAioMTaOK9Jcsz2dnmzNP2-lpVlsN8nTEU8-rdo51JpyXz2wadAzUZK-EHj4etRzKR8m5bw546cWCPGjI3Fi23epEBUhgs7n8mXy7BXvfbCn9gm1T-2yg_SWmmS7fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:با تداوم درگیری‌ها در ایران، قیمت بنزین بار دیگر از ۴ دلار در هر گالن فراتر رفت.
با ازسرگیری درگیری‌ها میان ایران و ایالات متحده و اقدام واشنگتن در برقراری مجدد محاصره دریایی که می‌تواند تنش‌ها را به‌شدت تشدید کند، تردد نفت‌کش‌ها در تنگه هرمز بار دیگر مختل شده است.
رانندگان ممکن است دوباره همان شوکِ ناشی از قیمت بالای سوخت را تجربه کنند، چرا که میانگین کشوری قیمت بنزین امروز بار دیگر از مرز ۴ دلار در هر گالن گذشت و به نظر می‌رسد رئیس‌جمهور ترامپ آماده تشدید تنش‌ها با ایران است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68637" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68636">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">⏸
🏆
👍
ویدیوی کامل مراسم اختتامیه جام‌جهانی ۲۰۲۶.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68636" target="_blank">📅 16:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68635">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
حوثی‌های یمن با صدور بیانیه‌ای، از اعمال محاصره دریایی علیه عربستان سعودی خبر دادند.
حوثی ها با صدور بیانیه‌ای رسمی، محاصره کامل دریایی علیه عربستان سعودی را بر اساس معادله «محاصره در برابر محاصره» اعلام کردند و تأکید کردند که این تصمیم از لحظه انتشار بیانیه لازمالاجرا خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/68635" target="_blank">📅 15:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68634">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SElaJB8m6yv5Zv7emwdAmxkxzZ_5UnOFB5aznkv1sYgd4rLOIa6bnb_C4GTr5VYgLlLelL4_j4yqcnxuTQMTjm4-MyIK0baZRMHMUElzH_bdIYwdfBQfTZpsgtfJ9RSDl5pi30ReDA5KMwMGdDc1GN457zRJpJcVSQVs37ZSh2oZo5YD9WuQ692-_eeOkmIg1PvK7DRZu-QxnPCDkIzR2XhpQ_7YNdLe84N5-F_2fbDFk-i1tKz3WFUdrMyhtVqDWY9BDvubO8B-H_zNJp45VIZ2urdxyYa2biEOcXSkUdGuc--I-xzslEt2EIDWQWf8dY0s74eVBj6SuZBKYnGhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رویترز:
میانجی‌ها به ایران و آمریکا پیشنهادِ یه آتش‌بس 10 روزه واسه احیای توافقی که امضا شده بود، دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68634" target="_blank">📅 15:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68633">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LbSKASLMoH5pu8MkkEgPwyiWbqoTlvWIvM0KoOtkghAN19FUo_mvcZvaFWi2Xki52FCHYlLnAfEVM_9Fqu1g5UayYs9y9RNq1Vbj_6I6nqKZ7N1Ch_UPM3qed3Bs4G7GyFlVU9oIsYN4dZZaTxIP89mhEbnplRTiywN2k1L8THIYSoD_uFx2tRE9apknD3-5EBTeoeH6acwR3ZTa7TufIqIX4NzLY_BzN43jldrhIxGBp0tDrOpFBGeWhO27i5QsLa2Awewh7ilOHZiaJ5jma5u9_KHGuLW895EEq2wrfPr8NzwDsiWrFV47Kh09udVsEdoC7pHUcYO5UAV2S7JD-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
قالیباف:
آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و ادعا می‌کنند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/68633" target="_blank">📅 15:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68632">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=dCgEra37OE7o1u3mfoWO5PENnXIMWYbEFtLiI54e2-XQ-yJU33D_LkA1fTzH2VKN7u1PdG8dkCEPEV3_h_kC71J7jvQSOCfy0J8nCUWE5wxErFRezT6GfblmSU84S0yzA-PKk2PZ0MBgcwxg2HbhAAi8T_kceMUhPdaF9nKB7flB4Krf2mLX8EyQpzHJSAPyhXPQVB0dHC16Svyv9KDJNEUziodylMWh9xf2yX4ASzexR89TjRsuedbRP0OgDMqKS2KY2Or3eV1ec47FcTw3XnzellaWJVfGcWZOelrXhJYDOqZTXDf_yiMUatgELA-tjyxZ6rKhKDnzFQYrDtGi5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e891d77eae.mp4?token=dCgEra37OE7o1u3mfoWO5PENnXIMWYbEFtLiI54e2-XQ-yJU33D_LkA1fTzH2VKN7u1PdG8dkCEPEV3_h_kC71J7jvQSOCfy0J8nCUWE5wxErFRezT6GfblmSU84S0yzA-PKk2PZ0MBgcwxg2HbhAAi8T_kceMUhPdaF9nKB7flB4Krf2mLX8EyQpzHJSAPyhXPQVB0dHC16Svyv9KDJNEUziodylMWh9xf2yX4ASzexR89TjRsuedbRP0OgDMqKS2KY2Or3eV1ec47FcTw3XnzellaWJVfGcWZOelrXhJYDOqZTXDf_yiMUatgELA-tjyxZ6rKhKDnzFQYrDtGi5YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عادل:قلعه نویی موقع جنگ رفته بود بیرون از کشور تو امارات و ویلای خودش تو آلانیا ترکیه بعد اومده به ما میگه شما تو غار بودید.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/68632" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68631">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🅰️
🅰️
🅰️
🅰️
🅰️
🅰️
🎰
لذت بازی در کازینو و کازینو زنده با 30% کش بک بدون محدودیت سقف
💥
تسویه سریع و آنی جوایز شما
💯
اسلات‌های داغ و جذاب از برترین برندها
📱
اپلیکیشن اختصاصی با سرعت بی‌نظیر
🎊
وقتشه با کازینو یک بت، برنده‌ی بزرگ بعدی باشید!
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
••••••••••••••••••••••••••••••••••
💠
لینک اخبار و هدایای سایت
👇
👇
🔸
https://t.me/+ioIBrQfqMLtmMmEy</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/68631" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68630">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7iKh9oCgwBbDZ4k3aWNYrFUEpxJpHYg3TpqNuIE2bLfp_lmcVIvnK62hnTWz2rJ97w8wMLeXHTXut79N-Ri6bZTQRL4cYTMAKf09AydHCjTblMOnHJTQ2cty4l8vfwNJUwVEah_T2zOymJqH4fLN7CfODxke8w5P_J6tvLxfe_oZB3jr5-N00qwWHS9snAUiBPWMFrDQikVsAXUA_gqivP-m5jwvOmozdNdEkmya1oTYEmmOk1zTc_DAj9QoWG87DFkwzNePdt5ZjRBGmBpRaey5rmOC-jtO5ORlQGsTGc1Dt7x9GibAuilcpzCXHu266jJU2Z1SnkhZk0jsCXBug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
سایت پیشبینی
YekBet
💎
🌟
کازینو آنلاین، دنیای هیجان و برد
🌟
🎁
100% بونوس خوش‌آمدگویی به مناسبت اولین واریز
تا سقف 100 میلیون ریال
1️⃣
لینک بدون فیلتر
1️⃣
ورود به سایت با فیلترشکن
📲
@yekbet</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/68630" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68629">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N5VfgA6KrV4HekmI8f4tpac3DHMzRqVUmzNN_gmfMSvzPdqtroKsnCWi1sEO733E6zN9GmesTE7qixGJQaEqmxSXV-CNxck0B89qizgy1d9PR3VovuI2beAN6UK2a2mCLC5fFG89yypQJ0FCP-c8rlc2WfrznwojCGLD--YQpXgig5z9vO9kU8gly1VhvcQIvoT0V_VC4WIQkx_fs96uQCjDsXN3tDWO6n7SXjLeX-JW4I2tEzpYU7jNmsQK0Aqk1z7FnqViP0mag0eUyNNI617nC2UmvPdtsjqEY_XbrpLSG5fjYsztJ9V_6t_lHEQXBoNRy2PAsfYf2GUIbZ2JiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عبدالله شهبازی :
شطرنج پیچیده این جنگ داره به آخرای خودش میرسه.
به نظر میاد جمهوری اسلامی توی این بازی مثل یه بازیکن مبتدی عمل کرد و ترامپ هم در حد مگنوس کارلسن ظاهر شد.
ترامپ طوری بازی کرد که انگار حسابی گیر افتاده و به توافق نیاز داره. امتیازهای بزرگی داد و با طعنه و کنایه، رسانه‌ها و فضای مجازی رو هم با خودش همراه کرد.
این نقش رو اون‌قدر حرفه‌ای بازی کرد که جمهوری اسلامی باورش کرد، فرصت‌های طلایی رو از دست داد و دنبال امتیازهای بیشتری رفت. در نهایت هم نتونست یه «استراتژی خروج» انتخاب کنه و مسیرش رو متناسب با شرایط تغییر بده.
حالا نشونه‌هایی از اجرای یه طرح غیرمنتظره دیده می‌شه؛ طرحی که اگه عملی بشه، ارتباط مناطق جنوبی از هرمزگان تا بوشهر و شاید خوزستان با مرکز کشور قطع می‌شه و عملاً حاکمیت جمهوری اسلامی بر جنوب ایران از بین میره. به نظر نمی‌رسه اجرای این طرح نیاز به ورود گسترده نیروی زمینی آمریکا داشته باشه.
⏺
اگه این سناریو موفق بشه، می‌تونه شروع فروپاشی حاکمیت جمهوری اسلامی در سراسر ایران، طی چند ماه آینده باشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68629" target="_blank">📅 14:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68628">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=f0CP-dcHmLmUn8DsqgW9od7uEFBftah8Rlv-o_0P3hi2LSx7TDibdcq6KwpRXWFZPC0ikNAqwXqXxjwyvhoLPe4rJLaXUpGKKOWCsfgsHDvbhIr4qIfgg55YM82MthXeB1TjlTlAu6Uozba-3cbCH8ebr7mr2h5tzmrDezeA4hie7NomnvWjt8RWdD-cdRtb93S4gJtFsjIyLaE2qCzqKh0I2qi-80IHMwPmjPOn3qSxj7Hm57kB84-YH3yWdtCg0k0-x2SplHYD4g86PYphS8aJ7PGsVjx1q6ceAGRi1pD6HJHjgmxHEdOR5KA8S9XfHfJl4pNwttcql7Zt2M1JAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/357e3ebc2d.mp4?token=f0CP-dcHmLmUn8DsqgW9od7uEFBftah8Rlv-o_0P3hi2LSx7TDibdcq6KwpRXWFZPC0ikNAqwXqXxjwyvhoLPe4rJLaXUpGKKOWCsfgsHDvbhIr4qIfgg55YM82MthXeB1TjlTlAu6Uozba-3cbCH8ebr7mr2h5tzmrDezeA4hie7NomnvWjt8RWdD-cdRtb93S4gJtFsjIyLaE2qCzqKh0I2qi-80IHMwPmjPOn3qSxj7Hm57kB84-YH3yWdtCg0k0-x2SplHYD4g86PYphS8aJ7PGsVjx1q6ceAGRi1pD6HJHjgmxHEdOR5KA8S9XfHfJl4pNwttcql7Zt2M1JAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو:
«اگه اون دسته از آدم‌هایی که واقعاً می‌خوان برای ایران یه کار مثبتی انجام بدن، قدرت رو به دست بگیرن یا مسئولیت مذاکرات رو بر عهده بگیرن، اتفاق خیلی مثبتی خواهد بود.اما امشب هنوز تو اون نقطه نیستیم.
به نظرم دنیا داره به جایی می‌رسه که مشخص شده حداقل یه عده توی ایران می‌خوان تنگه هرمز رو در اختیار بگیرن و ازش به‌عنوان اهرم فشار علیه دنیا استفاده کنن.
دنیا باید تصمیم بگیره که آیا می‌خواد اجازه بده یه آبراه بین‌المللی دست کشوری مثل ایران باشه یا نه. این کار کاملاً غیرقانونیه و اصلاً قابل قبول نیست.
آمریکا هر کاری لازم باشه برای حفاظت از کشتیرانی جهانی انجام میده، اما وقتشه کشورهای دیگه هم سهم خودشون رو ادا کنن؛ چه با تجهیزات نظامی، چه با حمایت مالی، تا این بار فقط روی دوش آمریکا نباشه.
حافظت از کل دنیا برای همیشه، وظیفه آمریکا نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68628" target="_blank">📅 13:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68627">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=RbWk9jCt6KQ2bG3jR5CARVnjI3kErenPaecVBgfV9yEtTUJCShZZKtj6Eh44mDi0eK5m55Jh-Z_AwRzy9EiRD1UOPvo7nhlfmlDrPcIJWcjYy2i3UpzL606zCuqi_p7o9jvjLNjlIb9zDuQACyXb9MnoIGNCXqMAOls34hex-oXkbRJ1bu7ujG2V4uAZik8GGBbT4m1Jtbt90a1AXPcPwtQ5iTl75yz_Nmfx9g0qLgPFT912v1yMGCXnVQ_ztH7nCM6Z4G8OoJEsyYJTlv2yvdhCN6sZ3PltGK8kVFx_pFEz7OV7mbZNjhf-yYK5XBxR1YW8KMPF1bbQVSTGPJM9jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb49be0645.mp4?token=RbWk9jCt6KQ2bG3jR5CARVnjI3kErenPaecVBgfV9yEtTUJCShZZKtj6Eh44mDi0eK5m55Jh-Z_AwRzy9EiRD1UOPvo7nhlfmlDrPcIJWcjYy2i3UpzL606zCuqi_p7o9jvjLNjlIb9zDuQACyXb9MnoIGNCXqMAOls34hex-oXkbRJ1bu7ujG2V4uAZik8GGBbT4m1Jtbt90a1AXPcPwtQ5iTl75yz_Nmfx9g0qLgPFT912v1yMGCXnVQ_ztH7nCM6Z4G8OoJEsyYJTlv2yvdhCN6sZ3PltGK8kVFx_pFEz7OV7mbZNjhf-yYK5XBxR1YW8KMPF1bbQVSTGPJM9jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
مارکو روبیو درباره ایران:
ایران کشوری ثروتمند است. یکی از دلایل وضعیت نابسامان ایران این است که این رژیم هر پولی که به دست می‌آورد — چه از طریق لغو تحریم‌ها و چه از راه فروش نفت — صرف سرمایه‌گذاری در حزب‌الله می‌کند؛ آن‌ها در حماس سرمایه‌گذاری می‌کنند...
آن‌ها باید میلیاردها دلار را صرف سازندگی کشورشان کنند، اما در عوض، این پول را برای حمایت از تروریسم به کار می‌گیرند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/68627" target="_blank">📅 13:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68626">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=bgtmXVgKsmSSsV-rEq8dJvcWgHH7J9icds0uQ_LjvfqP5QVfVHiw08BNNA4qguq04wCnz_GAj7HEQ8ToipuURVDyvjuKi9UWy1X7s1V1FB0evoQvuPcD4uofwDdmAJTaN2Ui4s-Uz6KdJudGYTJUWu2YakomCNSt6ttX0NUaJIDHlmrB_3vf02mgIRobbkVaG_qcom5LM-kfYyJoqGGoXp_PD7VoFKUx76PLuZ3xbbg31t7_wkl0aQkb_hIzwqgriYjeaVm6xsnopxVXRelf9Nv_Yaz7DrwwguR2-a2jkqL9IKAEcfgGXjVv2XnvZKSJoMG7HTjzAcjMc_Ryej9O2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/425aec1f1e.mp4?token=bgtmXVgKsmSSsV-rEq8dJvcWgHH7J9icds0uQ_LjvfqP5QVfVHiw08BNNA4qguq04wCnz_GAj7HEQ8ToipuURVDyvjuKi9UWy1X7s1V1FB0evoQvuPcD4uofwDdmAJTaN2Ui4s-Uz6KdJudGYTJUWu2YakomCNSt6ttX0NUaJIDHlmrB_3vf02mgIRobbkVaG_qcom5LM-kfYyJoqGGoXp_PD7VoFKUx76PLuZ3xbbg31t7_wkl0aQkb_hIzwqgriYjeaVm6xsnopxVXRelf9Nv_Yaz7DrwwguR2-a2jkqL9IKAEcfgGXjVv2XnvZKSJoMG7HTjzAcjMc_Ryej9O2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری:
آیا احتمال تجزیه ایران وجود داره؟
⏺
مطهرنیا:
امکانش هست ولی احتمالش کمه.
همیشه این امکان واسه کشوری مثل ایران وجود داره ولی تجزیه ایران نه به نفع امریکاست نه اسرائیل.
اونا خودشونم خوب میدونن تجزیه ایران بیشتر به نفع روسیه و چینه.
پس امکانش خیلی کمه بخوان بفکر تجزیه ایران باشن.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/68626" target="_blank">📅 12:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68625">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSH84K6Ppd29yLbxMuVnqxwseZF-x4JXfS1gU8SoMc7S1KvS1k3i_slyHSq1D5dhcq8Iyr52-RbDTi2JEgBm61NQUB7LyIozJ7ViOGE1_uo1vPdlPJQHPGwXAVPfAAwjvwpJw1FvvbzS5G0otUPs63n4wpd9FdulUX5HTU1FzeoYUAazPBmhn6NF9c2PakCWmDw2TI3ueu6ypXgpT6Ho5ATvZ8tOjfk8eypk32N58LiLpF73Cj_UYUTflB_Ady44tbL_QQQcycXGxpvWLxopwd5NmafFTtDYRo1kXoasMo9OZQMVVsZO17zllaeI-iQWYT5mL0ST487f_LAxqOhJwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
مسعود قهرمانی تیم اسپانیا در جام جهانی رو به دولت و ملت اسپانیا تبریک گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/68625" target="_blank">📅 12:17 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68624">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=T51TBjRXG8xvR5cFH3h4d-sU3sFEQZWWzsyDkMqqFCYBzV2GHLYIsEvNb8WISrGwPkcO6ttyoELyunuQAlWQv4_U4SYkKQdQ_7LDm0AjweGGamVSkNQX_YBhplw6IWMQt2twHTDwZ91UPUKBuAx6SE_Ms9X8dEMqTBN1N-oewVNP61yycdv42DWy2n8PvXXq6Vh-lUVg4qUKjabU3YeGihw7GfASySNrbDaYjvPALGBYIgVz0Tw7g8Ld7A21M72Wf7YwoR1UcsEkZKtuEfIRjuBRStTrX9WbSY3ngAKzKThXSBGgPon68rxa9E28qUtkbQnNmni_khpb-rHPZDZlCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5ad1a2f2a.mp4?token=T51TBjRXG8xvR5cFH3h4d-sU3sFEQZWWzsyDkMqqFCYBzV2GHLYIsEvNb8WISrGwPkcO6ttyoELyunuQAlWQv4_U4SYkKQdQ_7LDm0AjweGGamVSkNQX_YBhplw6IWMQt2twHTDwZ91UPUKBuAx6SE_Ms9X8dEMqTBN1N-oewVNP61yycdv42DWy2n8PvXXq6Vh-lUVg4qUKjabU3YeGihw7GfASySNrbDaYjvPALGBYIgVz0Tw7g8Ld7A21M72Wf7YwoR1UcsEkZKtuEfIRjuBRStTrX9WbSY3ngAKzKThXSBGgPon68rxa9E28qUtkbQnNmni_khpb-rHPZDZlCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
سنت‌کام ویدیو ای از حملات آمریکا به ایران منتشر کرد.
تصاویری از برخاستن یک جنگنده F/A-18F سوپر هورنت نیروی دریایی ایالات متحده — مجهز به بمب‌های گلایدکننده AGM-154 JSOW — از ناو هواپیمابر کلاس نیمیتز، و همچنین شلیک موشک‌های کروز BGM-109 تاماهاوک از ناوشکن‌های موشک‌انداز کلاس آرلی برک، در این مجموعه گنجانده شده است.
اهداف ثبت‌شده شامل یک سامانه پرتابگر متحرک (TEL) و یک پرتابگر پهپاد است.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/68624" target="_blank">📅 11:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68623">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60340234e2.mp4?token=IcLlif2W9HuGOOJJ6v6gkSpYifbPe1BvXEa2Sbn-v7HjqIXBi9Tiri_tSMgZW7C37jXsZ2_2a3CdmdWk5EjqJUFygPi8xqtY8QZPc32T21kIE7aqCimW02rMk5E4YtZlYn2FWS4pcRH2NVaR6KOuPQ4-1g5efZRggkvU7uOoAJnrrsi450IxIIeOSwT-vhkifKITlTCytCsGFpEG-uDHJlJmINQ8BqLH5miDE98Y1aeYJycm1zIuFkQc5c341Ti5kS6sb5l3wQaDr_lMulwOWBB2HZSGfPvOQ4P7ZbzQDEQMK70WITqPGLpmOAkZE-3RllsvmKWdW2Wks6RGC-oLsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60340234e2.mp4?token=IcLlif2W9HuGOOJJ6v6gkSpYifbPe1BvXEa2Sbn-v7HjqIXBi9Tiri_tSMgZW7C37jXsZ2_2a3CdmdWk5EjqJUFygPi8xqtY8QZPc32T21kIE7aqCimW02rMk5E4YtZlYn2FWS4pcRH2NVaR6KOuPQ4-1g5efZRggkvU7uOoAJnrrsi450IxIIeOSwT-vhkifKITlTCytCsGFpEG-uDHJlJmINQ8BqLH5miDE98Y1aeYJycm1zIuFkQc5c341Ti5kS6sb5l3wQaDr_lMulwOWBB2HZSGfPvOQ4P7ZbzQDEQMK70WITqPGLpmOAkZE-3RllsvmKWdW2Wks6RGC-oLsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ در مورد ایران:
این کار بسیار بزرگتری است که ما انجام می‌دهیم. ما کار کوچکی برای جلوگیری از داشتن یک قابلیت خاص توسط آنها انجام می‌دادیم.
حالا ما فقط به آن پایان می‌دهیم. بنابراین واقعاً همان کار نیست. کاری که ما اکنون انجام می‌دهیم این است که هرگونه شانسی را که آنها بتوانند موشک هسته‌ای داشته باشند، از بین می‌بریم.
اگر به آن نگاه کنید، پس از یک هفته و نیم یا دو هفته [از شروع جنگ]، ما آنها را از [توسعه احتمالی] آن متوقف کردیم. اما من نمی‌خواهم از کلمه احتمالاً استفاده کنم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/68623" target="_blank">📅 11:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68622">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iq5RgAHe-sgRd1WhuwNvlAVOOQde798HnuNC3wn8H-M0HG6wiUf4GUptsOQsS4JT3gAYbAphl8fqzJ723CQwabSBTAwF8sAAKfUWmQ1AOeYY2IY9CG5_Ot6Evu7WTlSvoSVXFCajg7hrMqDTalPFqpqr1OXJ39sbMqiSVzbfdmmFS2Uc51szamuhqp3yrL0geFdSrJiR8M70iI_c0VueKVRqp4__wIq3iouDCdun2TgXSgm_LPk5KK2Tv6Pl__BS8QmKd4duThxc11BnCEJnLpCFC0UdsSALv5Ra1Hzam0rVd6VQ07HrLReNSWJJclHNnk9cSjcY-F3LO1gvDEdZPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📢
نیویورک تایمز:با نزدیک‌تر شدن دو طرف به یک جنگ گسترده‌تر، یک نیروی نظامی دیگر آمریکایی جان باخت.
پنتاگون روز یکشنبه اعلام کرد که سومین عضو ارتش آمریکا در جریان یک آخرهفته از حملات متقابل کشته شده است؛ در حالی که جنگ با ایران شدت گرفته و ایالات متحده شروع به اعزام هواپیماهای جنگی بیشتری به منطقه کرده است.
این سرباز در شمال عراق هنگام عملیات برای از بین بردن یک پهپاد تهاجمی ایرانی که سرنگون شده بود، کشته شد. این حادثه در میان زنجیره‌ای از حملات فزاینده رخ داد که تقریباً آتش‌بس حاصل‌شده در ماه گذشته را از بین برده است.
هیچ نشانه‌ای از دیپلماسی یا مذاکره میان دو طرف دیده نمی‌شد و مقام‌های آمریکایی که به شرط ناشناس ماندن صحبت کردند، گفتند که ایالات متحده در حال اعزام هواپیماهای جنگی بیشتر به خاورمیانه است؛ اقدامی که برنامه‌ریزی آن حتی پیش از کشته‌شدن‌های اخیر آغاز شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/68622" target="_blank">📅 10:32 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68621">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=bJM_4sbTh_YJxM6SIGlpnNy1F592LWL9PQI87SH068rHxckMtDNuem2iaadFLIT4KYJ6dI5oylxZxU-1pkgaPMh6cj1NFZk4Cd_gZxTH13bX6rkMpLS_heIEJlNVUWsIk9m1Bo56zOsxW2-YJEdXPRL4MIT6DjLY2JGCTBRYbQ-Ph63xMwviU6IVlymtVuVzdIq3ncn66aeykNLN5ABA8aM7KFMvFvqumYS0HEuPSSpgi2MsutUX1DHfyFy7ad1oze1G0F1N0LNTwwtAqVxNmI5CBh6x7alZ9IscTx1vat32ICtxM0mJhaxwmCkcluGZNzekfU1NQL9xQF2BZjGbGlaFfE18gukvT0OgJmI0IaZpGxbrCjCEKyE171zLp0gwYmaXpxGcWljM5qhChIjE0DhZx7_2cC8lkHmryL-FFvdfQ3amObyIFkyb85Oq23SiA-ZbezcDwS9Vbc_gVWFPd3uV0Rl7WhokYQT7uubTADNtHh2L45AcLYIKRCIdczYMpHV3xBjcOJjT_s4B10DO6VCG2NoruTajMI0qFdI2GZupGyEwPpQFJLaK4SPSpf7i4C1uc9RQqqmJQYwftZb_Tfkpgytx5uBgfi-Vlo5uYierQbqWo4xO-dqALlM4ndNHhnX_Y1xisFwdnInstOQOIkNZwyH5k8hLvPPW_ErIyU0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ba03b9d75.mp4?token=bJM_4sbTh_YJxM6SIGlpnNy1F592LWL9PQI87SH068rHxckMtDNuem2iaadFLIT4KYJ6dI5oylxZxU-1pkgaPMh6cj1NFZk4Cd_gZxTH13bX6rkMpLS_heIEJlNVUWsIk9m1Bo56zOsxW2-YJEdXPRL4MIT6DjLY2JGCTBRYbQ-Ph63xMwviU6IVlymtVuVzdIq3ncn66aeykNLN5ABA8aM7KFMvFvqumYS0HEuPSSpgi2MsutUX1DHfyFy7ad1oze1G0F1N0LNTwwtAqVxNmI5CBh6x7alZ9IscTx1vat32ICtxM0mJhaxwmCkcluGZNzekfU1NQL9xQF2BZjGbGlaFfE18gukvT0OgJmI0IaZpGxbrCjCEKyE171zLp0gwYmaXpxGcWljM5qhChIjE0DhZx7_2cC8lkHmryL-FFvdfQ3amObyIFkyb85Oq23SiA-ZbezcDwS9Vbc_gVWFPd3uV0Rl7WhokYQT7uubTADNtHh2L45AcLYIKRCIdczYMpHV3xBjcOJjT_s4B10DO6VCG2NoruTajMI0qFdI2GZupGyEwPpQFJLaK4SPSpf7i4C1uc9RQqqmJQYwftZb_Tfkpgytx5uBgfi-Vlo5uYierQbqWo4xO-dqALlM4ndNHhnX_Y1xisFwdnInstOQOIkNZwyH5k8hLvPPW_ErIyU0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
«سرباز روح‌الله رضوی» مجری یکی از برنامه‌های شبکه خبر، اهل کشمیر هندوستانه
🇮🇳
و پدرش به خاطر علاقه‌ای که به روح‌الله خمینی داشته، اسمش رو گذاشته روح‌الله؛
⏺
حالا این ویدیو از این مجری حسابی وایرال شده:
🎙
روح‌الله رضوی:
با سنگ، تیرکمون، کوکتل مولوتوف و هرچی که میتونستیم، رفتیم واسه تعطیل کردن سفارت انگلیس...
🎙
دهباشی، مستند ساز:
به این حرکتتون میگن هرج و مرج طلبی، یه رفتاری انجام میدی که هزینش رو یه ملت باید بپردازه.
تو به عنوان یه مسلمون که به حق‌الناس اعتقاد داری، بنظرت میتونی کاری بکنی که هزینش رو میلیون‌ها نفر دیگه بدن؟
🎙
روح‌الله رضوی :
اسمش رو هرچی میخواید بذارید. وقتی همه‌ی مردم بخوان یه کار بد انجام بدن، شما سکوت میکنی؟ من اینجور مواقع نمی‌کشم کنار...
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68621" target="_blank">📅 10:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68620">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⏸
ویدیو کامل مصاحبه جواد موگویی با عباس عراقچی درباره حوادث یک‌سال اخیر از مذاکرات تا اعتراضات دی‌ماه و جنگ:
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68620" target="_blank">📅 09:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68619">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqhhAPhaiX83aQCV3Qz7l-LcfQOej6NCAUd_Vf9NoixBqv0zLFHfyl-9BWIFC4InMCUVpj_djPV_d6wfFDfRmYvN_8bjCtA4Q_SlYws2oXfV4THysI9OInfprFxebonWjWMGWG582swtowSMD5IBsxA4Hy0buFnSEvzwaR-gc4FeHr6SbY1txtKHelqfB83mJyDdIO3DVXPqSbxHdfPryX0D8GiWOrU04uAyhsycyIyOJJbAxsTVYud1EWNVdkJOnoj_PhirbPuyO_VL5_F9miLodAoxAn2lWMg1AlXl-dYhQZG3hYbf8-O9oqGTZQIGz0G0YrxGmlbSiFu6Jt8RBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آنالیز
دقیق،
برد
تضمینی
!
📊
💵
حرفه‌ای‌ها دیگه حدس نمی‌زنن، آنالیز می‌کنن. توی
Pinbet
، ما آمار و ارقام رو به سود شما تبدیل می‌کنیم
✔️
با ما همیشه یه قدم جلوتر از بازی هستی
⌛
روی لینک زیر کلیک کن و تحلیل بازی‌های امشب رو ببین
👇
🔗
@Pinbet_official
🔗
@Pinbet_official
🔗
@Pinbet_official</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/68619" target="_blank">📅 03:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68618">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDDucV-mDCwNHAf6a9UhIT2CxYZHh6QWJ5tJcgGph1aV8fokje9LhVO5HCdEPdLgukDZYDYcp4aP5kf9czuNAbNbH3isFYv3kvQXcGxJmMPLloiJ8RLmYEEd0A4Mp9TyQlAW2hW9G7Y-HkzEokTL_ezdfPapVjsKOL6DbVkfXS81q9xaWyCqtXVqbzWmkTCc23WKLQBVfpIU0RBu_zyNGsCr_KLHKxBnzioKfyNKLTgWqqTobtftEkC8Kx_uoZGzwoRDl47obaWY6kMthEd9TnhLpCcb1T3E3Y4AfBeHxDCtaVvfTFYBASLc0uXofpYfwX_s6son6tnVSTzeF4e3fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی در نزدیکی سواحل عمان مورد اصابت قرار گرفت و دچار آتش‌سوزی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/68618" target="_blank">📅 03:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68617">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
انفجار شدید در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68617" target="_blank">📅 03:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68616">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
انفجار در خورموج استان بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/68616" target="_blank">📅 03:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68615">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=tnVIoZ8-7e1tWm17lPVtcqgDCvCeIKOhsjSfUeofgU_y89ngUvp9e8JBHlcyxuM7beerSzbiwMhTYGPDS-ZmIlwzo9sPDhAA58Nlg9vCBU2If7I6JKnKdKexexzbdf4BtAKfy32JuiByGtG664btmLGOnx_SsMedFb65SZNSlJy2tDltOoAVXiA78U7uyuae4c5_c_f8UPFQX6ONvIRR-Ztde74KQbbrm3en0codFBzK2jtKwuMBqIj1isXo9AXg0wOBhUMYtLpdPOOqYIyHxQn5h_unFOO4e8yKeaegJYz1wm7-8rXRIs7LHJ3BECxn8jd9bSJ-zjpfM2hrPlTUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f692dfa.mp4?token=tnVIoZ8-7e1tWm17lPVtcqgDCvCeIKOhsjSfUeofgU_y89ngUvp9e8JBHlcyxuM7beerSzbiwMhTYGPDS-ZmIlwzo9sPDhAA58Nlg9vCBU2If7I6JKnKdKexexzbdf4BtAKfy32JuiByGtG664btmLGOnx_SsMedFb65SZNSlJy2tDltOoAVXiA78U7uyuae4c5_c_f8UPFQX6ONvIRR-Ztde74KQbbrm3en0codFBzK2jtKwuMBqIj1isXo9AXg0wOBhUMYtLpdPOOqYIyHxQn5h_unFOO4e8yKeaegJYz1wm7-8rXRIs7LHJ3BECxn8jd9bSJ-zjpfM2hrPlTUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
پایگاه امام علی در چابهار مورد حمله قرار گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/68615" target="_blank">📅 03:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68614">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJpmspnHvstdBYViPe-YButE6Tej9a7K6WFRY_tGJAbpOhjKMAJ7PNsapqxGxrfOM2t245E1pbIZPGyqIeMnHjTIXNrKXtH7SfmApV09elkRkxveaMgKBbGhTGP6ilRbr4sGoa1ldNZsmykqFMlFevtGAJ-dVVN9K4r7aCRogRqTaoBL6EoDs_JTR4OYi8pKoOjsrxcz3v-YcBN2_FyscclkHKOejLhCl42wJpBgrPs-m-c_YJBS_l3pCAG_FzVKi8gBYLtDkHPsmTGvWmeONJat0fBcgCc3MBb-zSZ7uYq4FTA8JkcAtNVJeXZXj43Bz6uMH9Q2ZeHmSxtOxTYbBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/68614" target="_blank">📅 03:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68613">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
منابع حکومتی:
انفجارهای شدیدی در شهر رأس الخیمه، امارات متحده عربی، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/68613" target="_blank">📅 03:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68611">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/521034efe8.mp4?token=WPoXxHDwbfJgvIgu-_9xS-tTkB8j_k0Tk7DwJQJnxOxL72O0KOzJcQsY5GSQHLnzglBDRzwqRB1pjIhlNcVdad4PwzfPyg6YX4em2tdSoJzPCB1ZOJ6GOXFtyL1Xb5SIDnrWz4e7WnaFFcXh75jRNsTlSHfYOE7VhFdKOh_3mHodsjOxqbuGLB8hPEiiGpcUZTRC5JF1K78hVxxaq7FcPsvyOHdbRiEe237tHPOqrEVCozVcjnp1EXSpZEQdfHqUjmOwYnvvF2bR0m72CJ0MBZAV9XRKiBBF55FznK3Vnw2zAnIglBIoK6oemmxmOZ59B0geT5Ml63l9EfSoNm4w5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/521034efe8.mp4?token=WPoXxHDwbfJgvIgu-_9xS-tTkB8j_k0Tk7DwJQJnxOxL72O0KOzJcQsY5GSQHLnzglBDRzwqRB1pjIhlNcVdad4PwzfPyg6YX4em2tdSoJzPCB1ZOJ6GOXFtyL1Xb5SIDnrWz4e7WnaFFcXh75jRNsTlSHfYOE7VhFdKOh_3mHodsjOxqbuGLB8hPEiiGpcUZTRC5JF1K78hVxxaq7FcPsvyOHdbRiEe237tHPOqrEVCozVcjnp1EXSpZEQdfHqUjmOwYnvvF2bR0m72CJ0MBZAV9XRKiBBF55FznK3Vnw2zAnIglBIoK6oemmxmOZ59B0geT5Ml63l9EfSoNm4w5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
وضعیت سربندر ، ماهشهر استان خوزستان
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/68611" target="_blank">📅 03:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68610">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f087874ede.mp4?token=iwRBsaTOeOWdW5Z1-cRqiunjNYFkFxuY6Jpam5H2WlVSJ-Nk4j4FZf1VBFCLaSsz7lA9e4mNSDmBf_d8YQm0QEVNLWyBbJaREoPqb9Hv1phVesZOmsISuSt0jYO74GmWPjCY3yyJl_yj2ynS4F-Ku9SPt-9xKezxWiQuDo7ztmaBWnFl-JLN_NHsarK-Q6P7rzG0o4a8vCs80CrmjRwseLjhN2fhGHhVfQzW64czeilP-cOZLVmixMV-UMpClyGHR-17goJmt_Vm-o_h0C35I8dmQInHigXqCMqjSE0V0dUdmUah4zxE_KfqITtbr1iK3LnEZHzakfJX01SuMrVeNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f087874ede.mp4?token=iwRBsaTOeOWdW5Z1-cRqiunjNYFkFxuY6Jpam5H2WlVSJ-Nk4j4FZf1VBFCLaSsz7lA9e4mNSDmBf_d8YQm0QEVNLWyBbJaREoPqb9Hv1phVesZOmsISuSt0jYO74GmWPjCY3yyJl_yj2ynS4F-Ku9SPt-9xKezxWiQuDo7ztmaBWnFl-JLN_NHsarK-Q6P7rzG0o4a8vCs80CrmjRwseLjhN2fhGHhVfQzW64czeilP-cOZLVmixMV-UMpClyGHR-17goJmt_Vm-o_h0C35I8dmQInHigXqCMqjSE0V0dUdmUah4zxE_KfqITtbr1iK3LnEZHzakfJX01SuMrVeNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
منتسب به تبریز
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/68610" target="_blank">📅 03:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68609">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
تسنیم:
دقایقی قبل صدای انفجار در شهرهای تبریز، چابهار، کنارک، بندر ماهشهر، بندر امام خمینی (ره) شنیده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/68609" target="_blank">📅 03:13 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68608">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
🚨
مجدد انفجار در بندرامام و ماهشهر
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/68608" target="_blank">📅 03:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68607">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/68607" target="_blank">📅 03:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68606">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=pW7f0TW4B9qER7SKqmjJhaCOcb9Nr9_5-noolj7QJ2qMi1jNvpNBVz1QCLPhr1Ot72bOgW7jazlELgFf68zaUD5gBwG34YTMz1Vu-2YG-6DDMjg4oJ2pkIw2l7ST800sjpcxeVLbLDzPtRwCg80kIAtNJjXsPepmO2ihrnqC2ZiIiGBW-wfSKdS56LziETn9ArlmfPsVEwzKAo8hihQAi85s3JtslWQEvWTtQEfzknO7QVGsgRsl1emY2QwZ8XQsLTQUFHjQwea3-daKZ90bV1Z1kWSdTSZW2QNcydbsZdQPksUD-LmN26p_HRzfTR-CLo7-Bzze7Fkh8J8q56ernw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a6436592f1.mp4?token=pW7f0TW4B9qER7SKqmjJhaCOcb9Nr9_5-noolj7QJ2qMi1jNvpNBVz1QCLPhr1Ot72bOgW7jazlELgFf68zaUD5gBwG34YTMz1Vu-2YG-6DDMjg4oJ2pkIw2l7ST800sjpcxeVLbLDzPtRwCg80kIAtNJjXsPepmO2ihrnqC2ZiIiGBW-wfSKdS56LziETn9ArlmfPsVEwzKAo8hihQAi85s3JtslWQEvWTtQEfzknO7QVGsgRsl1emY2QwZ8XQsLTQUFHjQwea3-daKZ90bV1Z1kWSdTSZW2QNcydbsZdQPksUD-LmN26p_HRzfTR-CLo7-Bzze7Fkh8J8q56ernw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حمله موشکی آمریکا از مبدا کویت
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/68606" target="_blank">📅 03:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68605">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
خبرگزاری مهر:
یه پهباد رو زدیم سرنگون کردیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/68605" target="_blank">📅 03:04 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68604">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🚨
شنیده شدن صدای چند انفجار در بندر ماهشهر و بندرامام
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/68604" target="_blank">📅 03:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68603">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=KmnR2PY3vlD90-B17NsXY1c059GIbHgYCi-ylzlj9bKjyEqUduBfPqiRFNnUGou7YVxN8bAxONshJP7k2omeF6D-CmW9uyr0qdJjboB0EP_jh3U861eeqf7HzYAmKzIj32ImBnZ4VvgUgEH35758S26cHLj-yprn2iW1wkfonw-wZbdPVQ5mna1opYTyE5p2oBTh58MDePbNQIRL6l8L5a9L0iPsX9H3VC6TIRJiVo8qjyEWE6auaBgSK-WhzkPfyIuj5fwnjnPnvisqUrdgzV5ulB-JdHODgra31rcp8zUUSAcyg6qa9GKw5oTPXiq0gk6l4lH1AZNODDiYCDlMJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2e2ba6741.mp4?token=KmnR2PY3vlD90-B17NsXY1c059GIbHgYCi-ylzlj9bKjyEqUduBfPqiRFNnUGou7YVxN8bAxONshJP7k2omeF6D-CmW9uyr0qdJjboB0EP_jh3U861eeqf7HzYAmKzIj32ImBnZ4VvgUgEH35758S26cHLj-yprn2iW1wkfonw-wZbdPVQ5mna1opYTyE5p2oBTh58MDePbNQIRL6l8L5a9L0iPsX9H3VC6TIRJiVo8qjyEWE6auaBgSK-WhzkPfyIuj5fwnjnPnvisqUrdgzV5ulB-JdHODgra31rcp8zUUSAcyg6qa9GKw5oTPXiq0gk6l4lH1AZNODDiYCDlMJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات آمریکا از کویت به ایران
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/68603" target="_blank">📅 02:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68602">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LDxIi4Ed9rsJcFhO2KmVrXoRds4Jg9iBdsBO4GB_sRBnzXcPaGdM9wIPVAX6IGJxiJchB3bGHCjcvttPRpnKmWQOtLIRMAQj1IfjRBOgmUuFe7fQhNOtHVD6hEbb2IB52lC-LX5aUknZJp7hxVBQmiS67eCNQlooLpIoA9dQcEsO3vmImX4mqPelvhEEqxe0pUtmapm3z4C0BBeObIogVgPQlSpeaSom0EK3WjauvMEuwzhps1q5Em3zA_kGmwA9Wy-FpkYuJ_QVS1_9U1IiufdL3Su8Z8PguL59169PPwnWZ-PlBqn08suvRjH0tx-8j8PVczheUCZZJIs-CQDKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سنتکام:
امروز ساعت ۱۹:۰۰ به وقت شرقی، برای نهمین شب پیاپی، موج جدیدی از حملات علیه ایران را آغاز کرد. این حملات با هدف تضعیف مستمر توانمندی‌های نظامی ایران که برای حمله به کشتی‌های تجاری و دریانوردان غیرنظامیِ در حال عبور از تنگه هرمز به کار گرفته می‌شوند، ادامه خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/68602" target="_blank">📅 02:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68601">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
چندین انفجار شدید در کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/68601" target="_blank">📅 02:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-68600">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛سنتکام از آغاز شدن دور جدیدی از حملات آمریکا به ایران خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/68600" target="_blank">📅 02:47 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
