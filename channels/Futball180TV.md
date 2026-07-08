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
<img src="https://cdn5.telesco.pe/file/vB9xIVf5gQy9DFHWlrxQGSLgXICoMtY-_OIHsdOUuKFBkZi5FEvDYR_uAaOyk2-9oAknWfvh5H2js8m8Nh0g48IY078UpPx7wLJKm34v0ZFz5CEUxbeB33Vqfi7A0xso5oh0gjN3myLD4VCJsfaIc1BsTjkZWDC8d5TjcA71SeMjAjH_7u4Eeyu3-we2ZxMKA18GkrWrTfTKqZ36nGuScbyC1iZhseEu4zkB7j82Bkmp2jpwz0Nkiy9m1UOwi8A7WN_CyadCNp9a85ziJ37L8x4RacNhdY_2QLyoNTa-KyKbPtPOg5beXGs6DYxk8uWjLyG9OgLBL3ENtcD8JMlvqQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 611K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 22:46:24</div>
<hr>

<div class="tg-post" id="msg-99097">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aRQ9XhlyrHttUhgsh8F1QGn1f8dWNvRd_3j3gcrLoAMd6g1XAdumowe2rgkgJiIJMuCBWv_8ryFu_DQQ6WhU-RNELmyGhsBFPwIFbgcQlkTVxXeRf7U_f_jI8x2RfrEj1ZwPLbhOF6rAieM3wIXVoLAs1X4y7e-WOOi1yZKS2KBLeSXn6sCvqK3qrCEGHNSt-8UIVeiimlY4D9AXFmZY9uYquXqaRqZw0rQKUUKuCrYGxLDpKD6W1YWC0s0LLiiRsSZjORiAlhzt0RKdRj4BGrJ4VDkejGnuaTou_wGzexz-gJGOghsN3fCuqLmbkK26VZKqaoS5uqFc8UFQWVMbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در چنین روزی در سال 1990، آلمان با بردن آرژانتین برای سومین بار در تاریخ خودش، قهرمان جام جهانی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/Futball180TV/99097" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99096">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqsAg-aDxcZhox9wU0nPBkoL9ATnQ3rIJEISBV7k7AQiatuaKaaymHICXDFzbkzvVLHKUnAsQa8X4SO4CQ5wsOMCK9hfUA7arn_-grgkIRfdxRKNNr9ilCoApaqMvHVIFKh6JMZMRywe7jcg2Ohh5JjNDcuQVtPgmuQTcEcJI6ZTqhEVfcDXLRLEB1fMNFQ9EqKAaprajdJColDGt0N12XFs_AtlOhhOEAfwRCSh1GGdCnihDpcI9VFn13fvsTFtKPKdLe8I_p1zRCGQS4tGpkMxoIA5c9lTbrkcbzSAbK_tnDIEO56mY8dnM1EgnU9fB13dw2C2SalF1RpHbaZKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
شانس بردن ۱۱ جایزه ۴۵میلیون تومانی داری
فکر می‌کنی از بقیه سریع‌تری؟
😉
⚽️
وارد این چالش شو و
کارت فوتبالی اختصاصی
خودتو بساز
⏳
فقط ۴۵ ثانیه
وقت داری؛ سریع جواب بده، امتیاز بگیر
و ببین
سرعتت شبیه کدوم فوتبالیت و ماشینه
👇
👈
شروع بازی
👉</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/Futball180TV/99096" target="_blank">📅 22:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99095">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3rOQ15k849MsC7Rrj-c_eX4ozKcR_TYKGw8u3H-_bCzl20PA5X60i38qNkAXXlf3-rH1Pv4Rg_H2vpPb084ZptCu8x1vyJjTH78qH3oSPzH-nyhB675du040dRAfwych6hyEZrTfxnHm_UBf3qfnuTv65o53bAuxzogceID7ZkMrI37Io2_iM3sLgV7GhYDXsZol1GXh10bfukqFr0hJojkQ5CRGgjnQ2gvWctPbeUBbgp5lS0nPh66CaytB7-EbM-dzCUmWqWgx2tBxtwS7TCp7gdm6_uVNNyXYb5QNrVCJQVLC1IVHzZqVeQ4-tiHjZWcpKhWoKd8wvJH5xJpsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
فران گارسیا رسما به رئال بتیس پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/Futball180TV/99095" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99094">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4kgKaYFq0mDNR-_q-xdNJuntZ47_VHBPTcxh_KcZF8WR2Rk6vGOiq7SNW2FEcg-3AJ8ibqobiFL5AXamsGhJJxLjfthkkCnZw9LqgF--NCz8ws-mw28sPFtP-4IhpNkHDVwc-Yq8A1GjXwEpuFCf4LXMfEGp9TlbiPsrvZSglDapFCD8UHMSASYIeXDl5WHq5toGa8JTWt85xbkqyMuQAcs-rcYHXhA0nmuibZ9rIN3De5_rpK-lhgmg7pbkKVcWxIpDzDKbuhEBWmgHb1tKKDx19ItHxDSmC_73n2CQNPiCFLX8bKiFvnFDlb71yGJo8dg3HGbrns65qasjuSOOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هوادار یونایتد رو که یادتون نرفته؟ هنوزم بعد 634 روز منتظره تا من‌یونایتد، 5 تا برد متوالی بدست بیاره تا کله رو بتراشه
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/Futball180TV/99094" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99093">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agn6zVoV1_K3TXynnn9mVbTU7M6ETb1g5j9-FBje7akCt-2M_a9auposWKPVu8yvF4tU2VHxeUOE7Cq-po7t2JZbtZw5ZSdSipZKp2ksiy0PrVCir0b5R8xNC1AakDxbgp0jFWr4N8ekHHL-kEk9Dvtikw1-WW3tDEkSYgZv0IXsQNexI0hwwBTJo-KnRodw7RWrhWjBBMUqvYyJZ2AY2unax5dYqnrqohjKYZwWMD2Xr_2JGz82qMX1Nak2XHGyzFGA8lu2ogOpi-vbqtZaAcWwrldN7cg2oiDyXW1SuZseW2D7lLsxnldM7MFvYdnqJ--3ZBjoWinyNbH4_-6DrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
ژرژ ژسوس رسما سرمربی تیم پرتغال شد.
🔻
ژرژ ژسوس رهبری پروژه لیگ ملت‌ها، یورو ۲۰۲۸ و جام جهانی بعدی را بر عهده خواهد داشت. او این فصل به همراه کریستیانو رونالدو در النصر قهرمان لیگ برتر عربستان شده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/Futball180TV/99093" target="_blank">📅 21:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99088">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rgyeMb-GH7nC0D5l9EYe-i_aahAODZSpmvqJv-4bbGK3DqI8WmGzlJxdRYwspyfh3tHNo9JXuAZtyPk0JTem9kM0VKKsk_oa43yYY3XfQrOO5A7JYXcOEH5pYnbDj78iP-RAJ2Kq-XawggEJ70sV5R6AF7SxWK_6stw68IqYMZn1WRF8Ve7WUrxgDm5lelnhSK9Z46lVXsS8WWr2ZaJWc5d92MADD3Wzxn5KahkgWvqMI_VDM0c1DHhwIxgJ3IxFeaJLl_shDqdHpCA_wWNp17nSHjilVFn8ewtBU6ukN1ASB4gfkX1NugW0NXfBWmYvX2K5WFyVUtx4s9_2CDAsTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ADergnm_adM_OzIZfrZoi2pKg7QjU62YETQCCauEQ6qiRqgAj5WThsmC4gY-KZf4NyfSQm9jrVcITCAZE7RDGGgnK8SHIx2JhhWFFQpNcAajgIv-ri2Q2VG4kAfI0E6oe_CJR1WoJ4gq2XlJlBWa_c_6rdQHFI-WLd3R2hiFB4D2K3yPkk5TMbKhp5FKpcg-E6aOZJTHCdYSPm9BuJFtPJcIivZhC5kyo0nfQAqSsUtBiphJdemwrmaS0BzS1_scRbeCJ20jO1ZHLnmteJqsFHAuqi0qDf8QKQMQUAPJ0BO10AeBhMz-J6lmq-ZiMpHye1hPnLF8Rkkf40HD4J4LHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQl6dP-vFtaOilYNFYzGCZQ2yOqo4dAMvdpZYcxF4krzBJcNwMZK15o2VHDxQ-53POgvrj5bcD1z-No40BGMPrDGid5rOeAqMtBa953hPdk7p3XLPC7RQdA9UxYNgteEb4LPlhTsDjyutB6BF2FomWSoPSZ8IUQBlcB5KeAsJiqkRtXxynM9c4nZrf9mZaRfKjpC3epNfylpqfG3zHn-5fC03Xu56J_QRfyFyeeoClI9k7yh0DCz8vsPEjXKVSm4ScfZZMSNkvTQGFqDKbgOTg0FxFJYYxt33ubtqiNXT3I7furhnHD1spr2khDzJvYSTcN1znPq3RIL7qPdPjdrWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XCpAGsisYFiNnHms5YLg7jyKLAGCD3wCDsvMwPy1RSi74-6wuoooP3tiXJg-wPhgtXSj8htyvWKAxUIPbywRJeEsHSNnrstC_EmGdd7jXrvza582mBik9Khge2XlwabW3uzbno4sknJ1hOr4fZzKv0fFkoKPrtlMlsY17WGtCCIHixTHfdY2qeK9IhvlnPZzedE70IQ601SS8jBJ5CvNf49T3rCR8El8yD2VObK2YunzNTpooEwth-zXV3vtoFwjPYyEmpBD2vF7egXSU-mT45CSX2Y4lEhW6px3k2oHGxJtOs3-1fZusuAT3o4pAjyMcyOla55zYImhy5vhrPN4MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCBddQWbFMqJvkSxfHr1HAGWFZDoZUAjZpR3wyt6XqPvo0E7l_RB0b_lAmMbQYJu5H43SWMs--KL1xzaSTzxmrnJDP7QLc5AEH8OrYldNLe-OV9G19TO32XlSfb2ZGop4pOyBlKXhxblaFwE0G74SgKfQXTWIAn4FNFJMaBuaCgzagD1cC3REQn2QrygoYApp80zFrknPQt6Bi-_LYSkKpNQRgsIi6pwy0tEIGq_RJ9EGRTXug464oPvpJFSC01a4KG_C-sWEFXzHDzgZ_KvwE1XV2ZIoQ_i1EhjX3jcQ2nKzBYHfZR6p3HeNj4jdVEd-H5LtbjaHvlbZEgteTrazQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
والپیپر آوردم براتون :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/99088" target="_blank">📅 21:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99087">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lheicuy1zYWEF1GCKfT5QAyatNfybMLL5NeTULmuTX6wffqp9gseFelxozeWr85fknPTpVzEi2163t8OxTY5WkduCckTVMf9JbrVJq8rO4GC8npcgnqqlfL3xk4on73_riKQzPbOMejXFjlhuGtI2DRVxutHsp_DqPPhTHyjqyeQNSjz0nXBjS2T_VpHUbN6OY3nstUJK4iLyXGdVMM9p4Kbftaf2gBtkAkwsClqJmfHn1RQpjrmoRIqprAI-vwoCiMzPEbI9nmdxFZr7vs-NT6SsnmRrVMpiXUmqRQT-sjbB8HZ5acUGQQ1gxZvcLo7jKoWqY8kJCXul3pd3vdyPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوووووری
؛ رسانه‌ UOL برزیل: نیمار احتمال بسیار زیاد بزودی از فوتبال خداحافظی میکنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99087" target="_blank">📅 21:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99086">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A44VUQHi7OlCEPxKKcqhj9gQy1TUhmcFBbGYcu6XhS_zz4CgH7KPpZeg3Z0DZa6HewPnXjEKb03OuiUMlnIhfjPa2YE3t9zX402MUDpNokZqFYyp8Nqt9qrtXgn0SBYz7j8AiSrJ2oqgWF-fiamu4mZhl5U_sciPnXoCIi-CB3NmTOi2UvJIYvQAY_HjVSDjZgg-9f2_L1VQPMKXrZE5_XeooIj-NrHBEsqEvLFm0yX-JbCFt7bz99CcKGUH6eN-XlX4wh8md-mZcYLRNYATigau4Lv4NwR2JAoO45BAArTjXXJTqiknRGBXJ1ANwxM_RjWEAh2gc9nQgzh8fbEHhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
آرژانتین میتونه بدون بازی با حتی یک تیم از ۱۰ تیم برتر رنکینگ فیفا به نیمه‌نهایی جام جهانی برسه
‼️
🔺
علاوه بر اون اگه آرژانتین سوئیس رو شکست بده و نروژ هم انگلیس رو شکست بده، آرژانتین میتونه با شکست دادن نروژ در نیمه‌نهایی بدون اینکه با ۱۰ تیم برتر رنکینگ فیفا بازی کنه به فینال جام جهانی برسه.
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/99086" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99085">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNN011yqaAbB1uxn7heIUf6P6llDPxvdDY9B2RrevoCCHlQYR3bRJNcbZoQadfvFDu9AwgD9kRdtly8r0tj8erBONS14617977oug76qmne-gZznN42ltfXxFljbfke9wdktc40DoR_1K2NKWOIUaJ7IIedzWhRWVavBx79dCZnCT2b_1V4EZelSh2POkXI6S9of6In3b1fkj23Cp25sKPOJVBVsgvHTOoTMrO_tCm2s4xEYgEzYq8bMpfrBfQjcKLR2ZSNjI-S968aqaPYez2axFlsd0W8SPdO5qOnMh7d57BVs2WtQz9X-u1_Ded-00_3H8MnsGN7EgdsyELZZjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
#فوووووری
؛ فنرباغچه ترکیه با مارسی به توافق نهایی برای جذب گرینوود رسید تا این بازیکن را از تیم اتلتیکومادرید هایجک کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/99085" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99084">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YetI3D6ltOMSp5en7PnZPlqYjaaYU0F2P_yRX6R2VRx8lZJzLhqwEYAx97lkW7AkbGDi7YPZM9dNEMosC-kOx4MXM-olYmi1N6dLafIw_RG2B75zaijlbkMnvErmGiOqvn6SKC8ydM82RMuIKFxA-fc5YRvdii-CCIxfzt6H54jPRlahM9DXGyVhO2uHtiIQJjCoaiY-kTSPkBVwS0yN7Ul_ZLH1SxE5eQElBqJysx7uP6SZ8ssaTHimWYrK4WlypUk5KGQX6hAUB7hd7cil4DqCiTHYO-NfWOMRxbJznf7FLzCM_Ey5dXT1y7Byug9ZZ8QiUkJzFXHRWPo1Aa4qYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیش‌بینی خودت را ثبت کن!
🇲🇦
مراکش
🆚
🇫🇷
فرانسه
🎁
۵۰۰ دلار جایزه
بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، مطابق قوانین سایت تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه.
👇
انتخاب شما کدام است؟
🇲🇦
مراکش یا
🇫🇷
فرانسه؟
🤖
برای ثبت پیش‌بینی روی لینک زیر کلیک کنید:
https://t.me/betegram_bot?start=p4_r4EF37DCE
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/Futball180TV/99084" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99083">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLy7DmPfgIobCR3b8RCSUbSYj7e800GVQo6n9batmDdAyIchOmhcQokTXb3wyGoebguyscwB1dleNjwqJ_492_Xxtgs0YdtVjVo8Tk6hCleZfqC-t9jwxsvbCVqbnfbdOte43TE8k_i33KRb_NmZrV1GaWYaBNiq6pDm6Kze5hBCWeQn2mXzi5D06amVB7LbmtHn6OfL4z5Vh9d-vVOXNpRDnV4NhCdJI1Ibe2p5XLRS_9AC-aV1yb0WMq2w_HSp2Zvh3silmUziGM1nqEr5CtzcRhrfjTuuzbIAZBxqmJ88vVlpgQk-9QGibJXKr9YZ_KJZJh5GYt_OqLEm3MF7cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁳󠁣󠁴󠁿
#فوری
؛ روبرتو مارتینز سرمربی اخراجی پرتغال گزینه اصلی هدایت تیم‌ملی اسکاتلند است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/99083" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99082">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ5gSxa9FGFYGmstJnacsZRm7ejKvIGv7_h7b2rtzcN0e0p-CRGP39-lzVsXXDAjBWf8qnTsok-BEQngkbyKL37EDnqe-Gg6Qk9zPheGJcPLnl4KToLwH8IYf-Ni0K8ASGK0NlvtMfp5vYx1exE2e254rpQcW00vQXgMGnS3bTWt9SvHe_qZ3rMGbjTHlLYCY7vVjw-RFwPgkofJHJ-nWj5TBoEHrOV6h9SPEfeZZgqKlQIB3VwsxR6mxxJPSaA07Ur3zxPOx6M7Mm9xrjCf-FgzCzP8jSFOo_0ex1PjIPeuBp9LIHuMzohKxM6RTdUMj5AiCkn8h_-0r2OD50tCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
الکساندر نوبل دروازه‌بان بایرن‌مونیخ با عقد قراردادی به بشیکتاش ترکیه پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/Futball180TV/99082" target="_blank">📅 20:46 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2GUYsNrljKu6DyYHGnEWhZz5Yp5A-Go-sFvqS82t7BdnLskHwnYQGmRB1-ZUPwFG-Z3dXMnu1CsgcUq04Viu0TLSZ128XH9bwbyf62Z3PkKbJ3Sk6igJ721q8uN7smY_rvv51p55F4SYfgiqPxRlIewKv7cNaXk9yv7-1KI_JxCcjQpk7mehAHfyI740o9tyJTCV11gSJLGnX2XtCgWot8F_ChrGkt78Rqfd9bELkvGAfCTqOzp3GJELUPY4XM_CMWMi7rdBQa4I0rbA29IgZ-QZPXGW6S7BX34IEtri3FItD7pYtxwRTb4Jeq4LtOx7f7-1EQ4l2RV3cNc363Lsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچسترسیتی به رودری اعلام کرده که ستون اصلی تیم در فصول آینده است و هیچ قصدی برای فروش ستاره خود ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/99081" target="_blank">📅 20:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری
؛ ادعای برخی رسانه‌های انگلیسی: رافائل لیائو برای پیوستن به تاتنهام به توافق نهایی رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/99080" target="_blank">📅 20:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3Nv5JM-gvIAAyJ463wFQKr18jsNRmB5kFAhc1cbT3LWUw2mfyr-4kJVQBi_sW5AIr03XYCrLjaD8PJaRxe2rXXrvK20tw8NDthETxdr2FA8SqUqB6r9foXraxBly8mVaw2RybrHt1C-DpawhOKGL6x5qBCv02UzkWlpALBA7g05nxukQQrPI7vK20ugE2UDDyNwMxH5XcEJ2VFgees4vItxJJviFgwrSymQ0Xzpw8vdro-Xcm23zE22XH3-t5LQ2APmZ8VcWwpeoCn8j3nCsLN0wwEYb6XYb5p5Z7IEyqklRJmq346E0tf7Y3sCbVrIkLGiV_Oe1cd6r52kJD5bJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
دیوید اورنشتاین:
برونو گیمارش از تمایل خود برای انتقال به آرسنال به مدیران نیوکاسل گفت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/99079" target="_blank">📅 20:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c18362372c.mp4?token=Z_jgPbZf527IN13htYgdAYZKonDpo0XEYmTELhGJ4zI7b9CgKzKkSFU-OTN8PTnjwIAusYY_8uzniB2cn3ugqLHMa__MCR-NSq60LpRMdOMCuAskQ9Xar7gcThioBaxji42Ux1DdWuDxct-W2IXEzbjRwVpHccf6xktPxy8XXK21uYQhAA3AwRRpRVvgEIYK6KbDrMnco4AB4r1ylrWHw2jvyDDBVMgF7YrxEZwU91ozFFKRqQ-LzU52hgfUPtQkeBBYbz7B9bhMpfBlmQUFIgfahzf3__o3PZIlWxHpzBSyTfWsXqONy4ysxDtb_Eb3FPrr9pdl1OCOGlmeFlff0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c18362372c.mp4?token=Z_jgPbZf527IN13htYgdAYZKonDpo0XEYmTELhGJ4zI7b9CgKzKkSFU-OTN8PTnjwIAusYY_8uzniB2cn3ugqLHMa__MCR-NSq60LpRMdOMCuAskQ9Xar7gcThioBaxji42Ux1DdWuDxct-W2IXEzbjRwVpHccf6xktPxy8XXK21uYQhAA3AwRRpRVvgEIYK6KbDrMnco4AB4r1ylrWHw2jvyDDBVMgF7YrxEZwU91ozFFKRqQ-LzU52hgfUPtQkeBBYbz7B9bhMpfBlmQUFIgfahzf3__o3PZIlWxHpzBSyTfWsXqONy4ysxDtb_Eb3FPrr9pdl1OCOGlmeFlff0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
این چه سمی بود خدایا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99078" target="_blank">📅 20:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99077">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3xUHghBTZT1ewV_lBtF1-kgRFjFPnVScPbD3gTw_5KiEs8XuP9pq1_pEAOpRyI6nRaEkBi0XTs2TwjEG4rHPIZTwws9ZVNCF5yFewGpESDGNB4mdXJK2R_PV_EZmN-NBvrXvTfzThgAytHLIittXV7ObbiYg9L9-HoN_p6RDeEXH-ITFQbz-A-XcKkRAeODvZtuISllskRXn0xabGBELQWrPzB3NqXxamjqbpjtKjdQz6smxNYLOB4K38RtjOeCVLPvrWkl_xbvihDAKDYsamAAXpOLVxaaLdDZZG3b65uMmEAr2kwsonYUGfbz0yRU_cMpzzPpkbJHUUWWa8K8CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
🗞
روزنامه رکورد پرتغال
: ژرژ ژسوس در تماس با CR7 اعلام کرده که مایل است به حضور این بازیکن در تیم‌ملی پرتغال ادامه دهد مگر اینکه خود این بازیکن تصمیم دیگری برای آینده‌اش بگیرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99077" target="_blank">📅 20:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99076">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQKpLJcDtSgiVuWMhT4odiIr_QSqSz5w6SiLtJtstA8qQlpNO2-22Scwows787r2aACA68CTgUd5dxxT5Fme5OlApGmaz0j3YuMUF9IBO_vtV2_hdc9H-5gk_ITD_O64kuZlAVQuZZbGiQd2gmlqerUC_tEZaGq-i_ejo5U9DuPdXwCSJAIR-6Fp7I0Uq1mOyfqZnw3VQDsOaTtU6DwrkoegxJNtz8i82UjOkOMuqhHIN7nLGoQ2BQ9WAlUaLgH4dT2ezBgNO6ewS928AlbnEFk0FG0IY79Bvect_JI3D9nRmdUptvzRqoh4ozmrZT2OtLFv4Nr7e-O1YjU_OhAu9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گلهای دقیقه اخری جام جهانی تا این لحظه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/99076" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99075">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0dCDUOWMj4Fr4JKdB6no6Q1gIO-gbxVyXbJCXND_JST4FyxdTG-TvElWtgZHh-teMzaXzzo-RQZlLOoPDMSAbgL--TN0Cl0UNCTAIWnpSDfkostqAawI3apbyyQUx1nQq2iWTlNKBDa-LHtY1jBFXR9Nby5jD8fdeXdsjrGgNffrNO9S6w_JhjQ4okfc3FxkTMefYHTWpXDSloPulo3wMzaUi7FUlHVP6y2QwZYfvCRdDFiTInoS-5V5SmGMl63LkAjzo5cJMUXEk-4mJnfX6n7aSHk3glqbzGPxadHdZPL03FA81J_V2bvKLiWX7iZQgVc8n_lZLd4ifyFtq7e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
مارکا: موضع اتلتیکو مادرید هیچ تغییری نکرده.
❌
❗️
اتلتیکو قصد ندارد به جولیان آلوارز اجازه دهد به باشگاه رویایی‌اش منتقل شود. این موضوع چند هفته پیش به خود آلوارز اطلاع داده شده بود. اتلتیکو تاکید دارد که تغییر موضع در این پرونده غیرممکن است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/99075" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99074">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet @FuckBet @FuckBet @FuckBet @FuckBet @FuckBet</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/99074" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99073">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Bw88yalEF_-_GDVMYbDRPkkuSOREBWmWDfbSXAi9zcFGhl9XJxC5G3P9E_eLm29mMQ0fjYUndP_oh9Gso7RJ3AX7B6923QjFSMGU8twQwHZLW6_nXASTugC3QZhQDtHll5kRhQzahAWiyGcqipIuHu8iweGNTuu-4UpdpxjAeGe1tm0oXWufuqntfl0D7ru0gfjyRnpkUmIEnZNjhHvSiYyoLioQj0kCjhVIOsugQrod2KT4kPpAnH7dRAio3s6Z30zi5tsxkW6KY5OFMXr2G29o9oN-epK1NvAQxfoPaoF4Um2LCDAUtr3OK5j88FfHDsOQq9piTNjTqBtkcMbUwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/99073" target="_blank">📅 19:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99072">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745dbc9962.mp4?token=ZoYfM2Z7204AQ1LHe8Idgbp3BQP9jpJqmqD3ItBVmAdYEr3CvmEKuddO2QsKzdi3rap1Ydmd5tnBrlbJXwgUpxF5YM49GKD2oM5TkLIUaX9wZoAFZ98JDBwvbCZzTi-TCAgrzxBdQcAa-HFSouSD8oqQTBETiJed6MLs4VqFwLoCWtdBZg2g9MPrRLIcr8Ox9uihP8snW5CY4HYZGezOgbVXpLVOdEwL83IqtRf_TWa-wAPgfQoFetzjT16S24IQJHpxPFH0Uxia1i17vmHxin9dwPSxlGWeTspw0qiYtz5uZnU-oBg9JNDXM1j0I1FiJ2817giOK7ylq2D18k9YHmTtJ0sGh1OSrrfWN6OiuoGcf5B4bU4GlhYjP6LNWpUP-buwBwECeytu7bz0I9eXkQlwXGO8ENHR5UtsVxRYE8E-taqjK7zpOkPetF5azzPoyrdFxByS9ymW_WBE08u3kJh_uzLMxAlE-FTWHILfVP-KXGi5WqS7GiuPKuGFKDo_GfNM7kfvbUxZGywYMS1QZYowfnt37IE5klYatqPnyJWG3Iz8LB7SYTkA1Th9pkLMZo67jTW9j22njv3_pUfKpk0xRL9dT7tlw9GVhmzKfDLGWjBiastisgYBWHVr0YE8Bj4D_TSFCvCahL-XY8TshWSyOFStwnOv6a27VJoduIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745dbc9962.mp4?token=ZoYfM2Z7204AQ1LHe8Idgbp3BQP9jpJqmqD3ItBVmAdYEr3CvmEKuddO2QsKzdi3rap1Ydmd5tnBrlbJXwgUpxF5YM49GKD2oM5TkLIUaX9wZoAFZ98JDBwvbCZzTi-TCAgrzxBdQcAa-HFSouSD8oqQTBETiJed6MLs4VqFwLoCWtdBZg2g9MPrRLIcr8Ox9uihP8snW5CY4HYZGezOgbVXpLVOdEwL83IqtRf_TWa-wAPgfQoFetzjT16S24IQJHpxPFH0Uxia1i17vmHxin9dwPSxlGWeTspw0qiYtz5uZnU-oBg9JNDXM1j0I1FiJ2817giOK7ylq2D18k9YHmTtJ0sGh1OSrrfWN6OiuoGcf5B4bU4GlhYjP6LNWpUP-buwBwECeytu7bz0I9eXkQlwXGO8ENHR5UtsVxRYE8E-taqjK7zpOkPetF5azzPoyrdFxByS9ymW_WBE08u3kJh_uzLMxAlE-FTWHILfVP-KXGi5WqS7GiuPKuGFKDo_GfNM7kfvbUxZGywYMS1QZYowfnt37IE5klYatqPnyJWG3Iz8LB7SYTkA1Th9pkLMZo67jTW9j22njv3_pUfKpk0xRL9dT7tlw9GVhmzKfDLGWjBiastisgYBWHVr0YE8Bj4D_TSFCvCahL-XY8TshWSyOFStwnOv6a27VJoduIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⁉️
تاریخچه تعداد یازده بازیکن در فوتبال از کجا شکل گرفته؟ ویدیو جالبیه ببینید حتما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/99072" target="_blank">📅 19:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99071">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
نکته کنکوری: اگه بازیکنای یک‌کارته در یکچهارم کارت دومشون رو بگیرن از بازی در نیمه‌نهایی محروم میشن. اگر کارت دوم رو نگیرن، تمام کارتها بعد از این مرحله پاک میشن و تیم‌ها تر و تمیز میرسن نیمه‌نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/99071" target="_blank">📅 19:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99070">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHx8SJETcrC15oc1KPJNgAVYvrY6tPUHz7EQEwgM6eh6W3sZpTTufggoIHABEB8nRe0WYrKNYo7yw4CZHnleT5oAKqxB_v03atcK35UORhLIYhOORonbl2NI8izrE4F9fTscGyADBaEjpfHBGYBqsQbXdYceSr040UtnrlKC4bFD_gZ1bKB28ZltAaU8VrdXzSyXFPwqukgY2lunL_zubXWiw7ZxhhrQb18HDkpwCf1PuMPeyxkLse60QSNPYhtSw9x4aScI-zFGZKOeDXt0m2IExzVsK3sQP_Y_iDNUXrwWvc0-bMKtKx3oDpu_WCR4zORTR5gwrrze4qJ60EQ8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نکته کنکوری: اگه بازیکنای یک‌کارته در یکچهارم کارت دومشون رو بگیرن از بازی در نیمه‌نهایی محروم میشن. اگر کارت دوم رو نگیرن، تمام کارتها بعد از این مرحله پاک میشن و تیم‌ها تر و تمیز میرسن نیمه‌نهایی.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/99070" target="_blank">📅 19:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99066">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m1t54yXQlJsYKXvbxOY3zejj-4heSBAud4jHqQoCD48k4La2JhxqHKAcc_6qAJIIeDgn8_H-u8pY-A9lJMXqgqzuKXAJjSpdlINpNCK2Xv3WNbnndBSvdjttgIBUGeH0LSpnR_6rzekZLpxY9_G6FXqFC3hxb5Oc1NU6yWi6IMcK13WxyeFWkPJM-udAoHc2098CbmOE7GUUbsb5q48sDkOdhsKG8raR-p7d6TwymlaC0w7DD2hpOPUG5qhxOA3aa0gepkoXBvMCy11hEHuZR3T202DEZ7ggkwutc1kNdXO8o85mhB8uDaTi7Pmeutzfbh1oZwCwlJaVf568gCNi_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBKSqkLR0Z3jmbmZCotlR5Id3jv9KSFPZOUqlY9w6BxTfpHSSN6FUA5VTeRhX5w5a8x2rRq3EXT-39WAM9PIJ9zTC8pWF40PgrxG03-b18BFP5KN6Xs5Gi6vqv8ipnSvkPrzBeVV5Syt5OcvnghV6IYBYLXvd2ALNmOJ4i8XDZh30BAZwTJkV2-aH0lPYjfam13Ytjc0IyaGrMinyqdk0syCTBVYGkQ_j-I0kyv_Om37wxCCOcrADDFvfzp8oTb1gASrW3-P_0o0bHjNfwXeEVjNKuglJg3GEg_8bpsXLc-LQhnrjgmtw3gDpdB5-Uv0MTd-c1v5vLvOKBetAq3yAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H_U59ClL_JF4gl2wlWRqbnEQB8gRI1hHP0rAdDvY6vf_38ASIjjsvz_hiHIN6VT_XgjyCsho-4CkUeR7cCPKPeCwzTxPYimOsQ42J9-m12tujaEF6CrXntGCa6UnmpEyekGfANMshh6B8wbOA0BFyC4gAgoJzpZPA_KBRf_iQja3uIKi-d3OJ772DzAMvjPvFh2G1G7K4IOly0fcd_SCCk7g9jm7rdB5Z_BcpCza0w6zuw04mwRdMtjMt63I7u_TwUTVTYuZW1hKbMfaIu3UqITHYezWbQJ2VfFwsxkMZdSkG-wuATXyeHSJXK0eH6m29vK0coDIH8hQWxPyqk8eOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Up3Sg2QqLxOfhsUlkBfTVYtcQRjTv-wl-Z2WC7DxUCC2SVzZX-SH9Db0vIKW90RPOGZmhejZVZG0-rTcO5dVXz60Ll1oFfS1nvUCc-iFoQW2M_CFlOPPUZB7BLgtPxIwo50w6kCfZspB3H4A8CguFbIPRQtUx12HT3WBKO1oJFJGO2THhAvduFjjhoFPqZorCO11ap5Y6L1_KxRW-gNlRf2E_IYJ8chHs7SYjgYdva254zmKKpxsROqRrmmbcxE4B6ioaRWtyo6LRkw2ZEsekxm9vKZl1DLdRvtZ6VpYsRboOer1ztZ4FIhwFaMpo3P852WboXBSrgHNqNKHIQqU5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
🇧🇪
همسر جذاب کوین‌دیبروینه در آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/99066" target="_blank">📅 19:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99063">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cKXPRBaqA_fOzD3jprmY1DiovgDfKN6VgkyIXuiVwZgyW4ZTBqy3OladjnoEVrHx8YelYbcNdEtodi2ruFhXhN3FyJtngShgE_7rfZA-CYsqHhMMLJlBZ24I9Ra4U0qrEhJDdWcKlgvsyPoEEamKtQkLyEdxxmv7LhNIm36TswE6szqT6eDkakfQVQfXEGWgfx-msB4e_01Wq0FIwQ8Bg60vCxArcM8AnKS9qDygrQXrKHbhPahzIUNduN_VKK2gYFNsNbiKhzLnlxSxKH9KmLbZQdKLwl8j9zM6l6Al8o4MMO3n_cKAQJtIy8Ff2VDutVpZWJjTlHa9645t7A8eWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ezzimqn9jrQLftTAO9tbMfCV4JZP5XkT7nusQdfu0Mierb_VLEgp8V3UdkaweyolkYHL51Gjk0RosTcIFkS5VL6DjbjMCG4u4butfnW1K7Uu19dO7R9fKKS_CJQoAlAmFdzis9qK80xw6UkIOXGKUsSD65gyCCuuaEXC9wD3m7I0b850x-s1NM6ciI4gwLymx2Soeuh7QtcS_YLddYlK8-5Rsm0R-7t96ZRk8f2A8hRmeUqjPS65rcx85W5VXnxbfC9U1sQcElfv50bTf3AkqfGg5P9x42cUQvAq6BehvelT0Di4X3CHpYtMHxN7HDsIjLRluOTBZh-Qbi5g312cBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdpZL93TO6Fd4zKzBBwQDGj0X8TPbrZUYa4iowEHCJv8-gmOv0YpBEgyIGPXRhYEg5n0OlHwcvdcAT-Eny4Pp8Yi4gM_YQMAi1VOUl3hQD4ZQHbWPE-AdrsO2hUEJyQ5lMK2E8idWGSgipZZHdg6b_bTKmiUKJlkA1Zsh1jccwQvzTvjhOmkRR5CLVKI9V5F1-KWDgaFHGNNw1uGasPl6UmexFxMcEP3hfs6coqWLwydj4YXpSLVWfxOVA-1wJGZf4v6bmZOscn5MZt4lR2EHVWfZlXoYyzkUXtrkoTDVT-LaClbNjOu7wzEgxMo1QsdxmJ1yIEwEphhTvitCkrnAw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اگه اسپانیا قهرمان جام‌جهانی بشه چه چیزاییو قراره تجربه کنیم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/99063" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99062">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fafdc23a54.mp4?token=bKgheiteTyw-pBOEFFc593oYEM_xShOaeAhFQooCTDVF8QKq14Mia44Q2cUJ_Xas-4lTA53J9hTX6CyXeibXT0IVJr_wEHsiKAcdb0eHLExMZIKD3atIrqilndO-l_VnWmNOcaYDsUxfvuL-lygQZI672FkF5T__sZ6So50SG86JLhSnoQtUx4MCH4H_Tuk7GiZIr-yr-WT-_sVchfsf7ThhR-7gbY6BtcXlaCnad0zTE_I0ERefTEcO8ddFBTnqVsyjrMjTRNOjsQbqLX10cz69WWmOzhwd5uLWgQbToMU-um9X17MpwtXpjuXdqenwnpEl7985ogSF3y2pEbeKgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fafdc23a54.mp4?token=bKgheiteTyw-pBOEFFc593oYEM_xShOaeAhFQooCTDVF8QKq14Mia44Q2cUJ_Xas-4lTA53J9hTX6CyXeibXT0IVJr_wEHsiKAcdb0eHLExMZIKD3atIrqilndO-l_VnWmNOcaYDsUxfvuL-lygQZI672FkF5T__sZ6So50SG86JLhSnoQtUx4MCH4H_Tuk7GiZIr-yr-WT-_sVchfsf7ThhR-7gbY6BtcXlaCnad0zTE_I0ERefTEcO8ddFBTnqVsyjrMjTRNOjsQbqLX10cz69WWmOzhwd5uLWgQbToMU-um9X17MpwtXpjuXdqenwnpEl7985ogSF3y2pEbeKgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
صحبت‌های جالب علیرضا فغانی درباره چگونگی آشنایی و ازدواج با همسرش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/99062" target="_blank">📅 19:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99056">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIj93traFWym-PNFKeYBnBmyjzwCnO9_PBpG2kHNr3rmsfOoCXI87luGkbrrrVWmiPehM_Rd-bQMFSAC0uhNP1bPOaR5oKcU0wXlzj78W29g282P4yICZtFopq4qkYjQkKN20uj9Z-ZkYUzXhJ9zlFPEN-ZGf_3ZYS-oSXE0gUg28-_X9JJANr5VUyhND4OlSVuXak4F80aYdCNHf9dvrsER0N0WQDZvvPbkL0hywJl_m22r2hr5iGsYgSqBnRe0p3PH4Dp9YrLhk_gZriZ5VofSMJ1O4FW9wz6BA9csloWOV8d9s7uAd0utkqNenIw7gDnN8FfYVzFnr3laW5nFcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JskIMPxKJlwLxl0ThNqfhDQUbWKMllk_6DpvFvwfuuRL7O7RPcByAoXv7n3ftDVxkM7eClW7Lh4r8EGZQ8g0MQQM-bi7SujWaPGNnyuRAWqnkRSSv6OgrTRAovLovLVKVnp3GjocWDmTwf4SJl67QQU97OCEC3S47uYzqZGShoHABfCJ_IM2aIsomGOAecIR0qTjwbo1Eik3E6GopbIVoKHpB0iPYN-Vw_JmK8VNZWTXTP3fIWrxLgrVGC99WcvRgwq2BwlTXB3FvZ37zcl0-1Jl5eshMLyyzeYLKyh8tVWN1UQ74Ja8Nc-Dic8NLb-PYFMHC4e6fF5DqUq9E8P8FQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eK_PKFqszNZbzPwEIGqJXl3WpY6T5inxrwhh7UmpJqcZb_LznUAquvIxxh9FXJXj-7zNUFFiFvgyhh6IvpLWoUzeQm-FFEJMxrXFK71Hppu1UgwARgMpAVDQuMXyn56_YojiBlLGRaaIEi-ZjltNr0M9mvQ1XJXSHIelaYcbjRx2INA_DSi_WRTNi0Ny4Ot-klubBCxfp7aQa--w8sUWcZB09KPSUeEFRs2ZllCX_hxMptRv3cyzYcJXwBiPZ8iiH3lNk9T9Du1RI7TIgVCJBtjtjFSaN9FAFxyaC3IzfPTmStaI6suPYpff53xPHRHcakMWGgSBUviDO32WmwkM8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dZ8IrO8pj43MjB7KijTSF8efL59JxymnEPFhh5e9fhvlMWE58JyVMSyDyRTf7-4EtKhTlrk3Pmmtrhqwy2c_8AsmSQFgTbhH-Oj3QGYL-SdYDNBYU6DKlbmcSFWWFZe6His2yvi2-N4IihfEMDZdWrBkpIh9JPvTHMxP_5s7lYuJNbuCYPwEZHOlebu4Uy6v_mfZS3QHJi7WBBKrTKSGrQdt_RE4c4habtlyh4GlYyYOeQW5y9S2oEHSOYBzQyS4f5yR_U4T-zMcJDZ41tNaTB_XPUoxXYtU4sozlK1t2Ltkwq9TJQc6ZKAXJxbKdCIu6PHSNZZYKw1FJbcQwZcnyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NM6wnfRHOyfXalZAdjf1LwOovRnjaG9WSXR1bn1LjD_aj71qqPvkHtRfVdk4huxq6Q8fZz-bmqpz1X9HeBg02zDlX-D2koLk9tDxpwndnF7kM6SdM8ojmvRmA-zir8ennva7rBXbaCMnxqipiYbQo700MBWCw40V55alNDK1SS5QyEiof8tYEMHbS-xrvCStZpzTDZqznruBxxI7DW2tJKNfR5kA0Kq-PjVPc_0rFN1GDKeDL_pe3HMLYNgA_Mze7eudxNe2-bTzWMKuZ_F6INPdRzFKYRlqoaYnBGcS2nNapFYUoC9vDIr_mG5tydsmfW1XofOLhhLQ_IC-rbhyaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🇪🇸
همسر باردار فابیان‌رویز ستاره اسپانیا در محل برگزاری بازی با پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/99056" target="_blank">📅 18:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99055">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nr8I9WQaJxZ9uXKRBLF7GCfNyMEqOHNXDPr171MOWLrJBgAL024zGGXkrmCuQvaQVqabvRHliJuU9gag1mhvz3TjkYbot-Vxefpjqf7o4UFSaF9He7vm9HWEiW4jNQRQItv6ctXY6WthiNJgHZShjhXBFyE0imF4kNdY2QjFhJAEAp2e5PIhDNhFWjuSVl5kzsU7PS--amlKyesnwj7wMtwnrDfeKlgO-IEu4TgSOuR3wlLSzLMPyxkPlI_pA8pr_HDylDwy8OzLQ8A47vh46TBvNfF99wYSBHq9ZzUlqX1JoilMBy7Kr1rVg_ANZQ3x8xdoOor2rxyuMRUjcR0XHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚪️
فوری از رامون آلواز:
اورلین شوامنی با اطمینان 100 درصدی در فصل آینده در رئال مادرید باقی خواهد ماند و از این تیم جدا نخواهد شد. او به منچستریونایتد نخواهد پیوست، این موضوع به پایان رسیده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/99055" target="_blank">📅 18:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99054">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0ZuQsGpYiV9ASZQ-wxubGUgegZJd5yy8yEZvYNacbs2xYRgSVU1LVOwsYFAVcCsc9ipHJlfRCKaIrqDsdU4Zb6Sh0qEqvZ5nFLbc53-W_3PNATsbdTjQ4GXyi2Zn42dQfJbr78hr1AAGOnsaXVhwzGzBJp4OaKVgGr2jrVW3KOryADHNIyDmHbwSpDGg_Jah8BAkgUuZoT5IGsFcDL6HxZfX9NlggsFjVBj2CtdECMSQAs_ilYQvCCvTUY03DT_-jj3LucUa4o-rPCMpT7qBLPc3jW-fPjsfFlD6BL23Kx16sZ49sLIZUoiUxIlZccV-fG-Uf_aiXeUrDDIz4w_8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇫🇷
🎙️
دشان در مورد انتخاب داور آرژانتینی بازی فرداشب با مراکش
:
"انتخاباتی وجود دارد و ما باید با آن کنار بیاییم. من به داوران اعتماد دارم. امیدوارم داور ما به اندازه آقای لیتکسر در بازی آرژانتین و مصر، کارآمد باشد. رقیب ما مراکش است، نه داور."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/99054" target="_blank">📅 18:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99053">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W6Y_TdKVRwfsSXg5OwRG6t7b_SaIYPB7iduvgcR1DSDOv1p8YDzq0tjs6HNNYBDRC4dHRIzdSn5OlVYarIR39gp8Z96ePE4wwLFActboUOVHSGn9HF2cTluv1mN5pGrKymKgtQXUCgdFMmk3F_OHRRMaa4V6PNHLw4KpoaiT7evm2zXF91ZMcvSSrQIqcy6GIRTSh-nb3_03k6N5fsCdJBTHIhezQVF_O0qVosXpMKAkJVSFluPBrciT4-Ze8Z7cD0pxVjupEMXlAW-_3HpVw9BYMsx5xNlfa7jf_b0Cxf9y3zrhrftdI6bziFMo9QtR8oJfA0bgnhnOxdWNSrxeug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇦🇷
عملکرد لیونل‌مسی در ۹ بازی اخیر جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/99053" target="_blank">📅 18:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99052">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipTIlFvut0dbNqbuEWVoKUKedSTLv0vCJYjx3K_6TGYyPjq9_o6z7cDXKLPF3JGugzQQt0xI1QFA5TS0MVBYRchtxC0V-1kbTI1pW_Wz-DYIG3BA3D89cRChuVdmOIM0TmYznn2qlKyqYQyEA-dZpfkRVS_thy2am8gD-4BEMMsK86SKWXs0yfbP5tBjuaC3Bvnyrn0O3bz2SAmU_3C9oW2eqZELksDdx3Xrh_maUkh-3Awy3A2sSeUWALUlJeLDw5FCa_cGkJsf7UfO8fFgBk8SO97Xsnjd_yB8vaZTR2XJO8IHgPcQAL7VPK0VCS2RX1COsueloIiV6HjuDs9Syg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇪🇬
ابراهیم حسن مربی تیم‌ملی مصر: هدف فیفا برنده شدن توپ‌طلا توسط لیونل‌مسی است درحالی که همگان می‌دانند لیگ‌آمریکا را نهایتا ۳ نفر تماشا کنند و اصلا سطح فنی خوبی ندارد!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/99052" target="_blank">📅 17:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99051">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=Xc5rO3UzRcvNlLqpHzqrrGSwsgVw3CrM8Q5GUX-8S4_2zYKvbT9RvzJfOYONMsmEMDr0-bFQxLybud_u4y5KBfLRWn6nyfn-0ahoLMgAzf5HnVRGl7drvhU5Knj-Igmq9vNnUh_YqPcbV53pqcLRfkn6-yJE-3GYKOCveXg0Q_w4YqFgh8IiE_JQWGxNKcAw6axyLAYKzH0GrQuOLZaTvbWJKBeBS2bFdklTm7F3O2U9J_Y_MD5bvhXn5ovrTWA6T9TcE7Q-sJ-UySwZaZ4LmxJtkRBtCNTkpgoHH65fvviBjRVT23TRAdu2SWs17AbMZkRA1Io3Gb-V7yedVzM3VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e25d8855.mp4?token=Xc5rO3UzRcvNlLqpHzqrrGSwsgVw3CrM8Q5GUX-8S4_2zYKvbT9RvzJfOYONMsmEMDr0-bFQxLybud_u4y5KBfLRWn6nyfn-0ahoLMgAzf5HnVRGl7drvhU5Knj-Igmq9vNnUh_YqPcbV53pqcLRfkn6-yJE-3GYKOCveXg0Q_w4YqFgh8IiE_JQWGxNKcAw6axyLAYKzH0GrQuOLZaTvbWJKBeBS2bFdklTm7F3O2U9J_Y_MD5bvhXn5ovrTWA6T9TcE7Q-sJ-UySwZaZ4LmxJtkRBtCNTkpgoHH65fvviBjRVT23TRAdu2SWs17AbMZkRA1Io3Gb-V7yedVzM3VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
🇦🇷
صدای وحشتناک شادی مردم در خیابونای شهر بوئنوس‌آیرس آرژانتین بعد گلزنی لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/99051" target="_blank">📅 17:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99050">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=aUS3pD2XHX3E-KkcLrehIXWzhAWq4lM5Vvem7cAbxtXG_dHRUbEPAoUmO9t3yQzJrZ4T3KaP7Rq5nlUPIh-APPB4Fqt79H4kG_KWGV2IXKanbzN_i6m2m_73NsxsoUTf_KdHLU9uoFXiHL2VcDc-Zv4XVadYfU9Z7F52-BZkVjL5PF_dNmq9nE7MGpV8g1T4w1G01AMGXe9wfgPh519ZGOYEValwUXF1kClJgCggy7YajcbUaBaW5cAMAyd6yFGB2oAohZRcquXgOQgwKxR1oLtUw5C9AIRPalCbQGc1I_zqhhgXWnO1daNjubF0tvo6D9lxsegID6fvVc1hJwCEQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44599c3a8a.mp4?token=aUS3pD2XHX3E-KkcLrehIXWzhAWq4lM5Vvem7cAbxtXG_dHRUbEPAoUmO9t3yQzJrZ4T3KaP7Rq5nlUPIh-APPB4Fqt79H4kG_KWGV2IXKanbzN_i6m2m_73NsxsoUTf_KdHLU9uoFXiHL2VcDc-Zv4XVadYfU9Z7F52-BZkVjL5PF_dNmq9nE7MGpV8g1T4w1G01AMGXe9wfgPh519ZGOYEValwUXF1kClJgCggy7YajcbUaBaW5cAMAyd6yFGB2oAohZRcquXgOQgwKxR1oLtUw5C9AIRPalCbQGc1I_zqhhgXWnO1daNjubF0tvo6D9lxsegID6fvVc1hJwCEQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
آغوش گرم‌ لائوتارو و همسرش بعد بازی دیروز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/99050" target="_blank">📅 17:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99049">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری
؛ ترامپ: پیت‌ هگست از ایده ترور مقامات ایرانی در مراسم تشییع علی خامنه‌ای استقبال کرد. ممکن است دستور یک حمله تمام عیار به ایران صادر شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99049" target="_blank">📅 17:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99048">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=IVkp4r8qVpd8RkrQWw8ojKzZs1KFRhaWf1hCDzqMdfdBuIiG3_4-U7TjRQVnbqjUFf_SR99aijm0B2BmtFCwmn12K8fYzSokraAMsxZXN-Vkl2KNPf9zzSXVfPJE359TQpS3TVhWTqoEp_CIQEcZzhEBI531gUXCLCW42CTcKlJhPyjcqpjFn_ODQ1ctJjnEcHdbR1IY8QGr5us6EJqpniI-7lvQw2ahZIXr5CSsoDwHxeo4J0H8Xx6ooBzNLxWgQEKwLLFUek_sjir4k7OVOgQrcAly8dw3R74J8z5f1eAcluN5qs6NiVINeHfStuRn0AYs8_Oop-xTL4HiAxbxp4XSjknDRhF0UTSXCKAhNLcU0knubEkxz_wvcKp89PkzYH6reNduywV-gmgmQYm1ArIGBFAeTPfxBMY0SzX49fA3HUDH9xbYOA--Ek7gQKOCamMfDqioP4vc7Tff9eH1XDK7MbLshhhCkOo_KsnlC6LaI0b-IxELAeIhEdj5w-Gjvhb46IJN3Bm2cLSaZ2EmVe4oEd8jRDbwQT3uYbBliBPibxAeI1BDXQttWdNScK1KnQipuC_ksBO-h1tt37RsNsESW6-oHhy3xZL7ppdwVlkdMv7aHPkxBvHjSaZEPFXCKlxREf09OcOh86S4tnX6dPqkc21v1ztrFZqa8n-_nmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b20b4ab0.mp4?token=IVkp4r8qVpd8RkrQWw8ojKzZs1KFRhaWf1hCDzqMdfdBuIiG3_4-U7TjRQVnbqjUFf_SR99aijm0B2BmtFCwmn12K8fYzSokraAMsxZXN-Vkl2KNPf9zzSXVfPJE359TQpS3TVhWTqoEp_CIQEcZzhEBI531gUXCLCW42CTcKlJhPyjcqpjFn_ODQ1ctJjnEcHdbR1IY8QGr5us6EJqpniI-7lvQw2ahZIXr5CSsoDwHxeo4J0H8Xx6ooBzNLxWgQEKwLLFUek_sjir4k7OVOgQrcAly8dw3R74J8z5f1eAcluN5qs6NiVINeHfStuRn0AYs8_Oop-xTL4HiAxbxp4XSjknDRhF0UTSXCKAhNLcU0knubEkxz_wvcKp89PkzYH6reNduywV-gmgmQYm1ArIGBFAeTPfxBMY0SzX49fA3HUDH9xbYOA--Ek7gQKOCamMfDqioP4vc7Tff9eH1XDK7MbLshhhCkOo_KsnlC6LaI0b-IxELAeIhEdj5w-Gjvhb46IJN3Bm2cLSaZ2EmVe4oEd8jRDbwQT3uYbBliBPibxAeI1BDXQttWdNScK1KnQipuC_ksBO-h1tt37RsNsESW6-oHhy3xZL7ppdwVlkdMv7aHPkxBvHjSaZEPFXCKlxREf09OcOh86S4tnX6dPqkc21v1ztrFZqa8n-_nmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نمایی از نیمکت مصر در صحنه دریافت گل‌سوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99048" target="_blank">📅 17:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99047">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=Gny_x9mY4NxdgIdlGLd8nb5YnEUEw8jegdezFKsqf98KtDnIEYoFsvcIELDYF0KpA_dfuykVp-f25-25jbkGFAv569pwVZzTPhdEF9OdVPmxj8mg-YTI-L8-H2-dp9Xi6IZ4kNcA8w1_ayK5KMfkAWufhezo0UgToGX1dJmVmRBXrbMx7lRP2wJLpeWuP-9RJLRGDDNAZlBmTRt0Sw23m2osvUN2DeihACD4uncl5QkSX5wgXH8-PIW3Ibwk9sI4JsS-f_3-l-48xG-XLWr59yM5HWLTv49RRA0ufnqHA3lzOOv03hCzvIqJoieTZv_oXrBC3GvhvS6P2uwncFnTVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1dea537f8.mp4?token=Gny_x9mY4NxdgIdlGLd8nb5YnEUEw8jegdezFKsqf98KtDnIEYoFsvcIELDYF0KpA_dfuykVp-f25-25jbkGFAv569pwVZzTPhdEF9OdVPmxj8mg-YTI-L8-H2-dp9Xi6IZ4kNcA8w1_ayK5KMfkAWufhezo0UgToGX1dJmVmRBXrbMx7lRP2wJLpeWuP-9RJLRGDDNAZlBmTRt0Sw23m2osvUN2DeihACD4uncl5QkSX5wgXH8-PIW3Ibwk9sI4JsS-f_3-l-48xG-XLWr59yM5HWLTv49RRA0ufnqHA3lzOOv03hCzvIqJoieTZv_oXrBC3GvhvS6P2uwncFnTVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🔥
آنالیز‌ گل‌سوم آرژانتین مقابل مصر؛ چه ضد حمله وحشیانه‌ای زدن و انزو چه کاری کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99047" target="_blank">📅 16:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99045">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qh6JE_Q-v099OYVXm28hZZfkHsP0a2ETFOoWlfkyR74yLSp8kzjkUP6H2XucTqmZfp4-DA4JJY2B5_cVXUmm8vn3BSbHkY2Wgehcl4mXxPkweoXEmcJh9UJzv5ycdqjfRwz8yjwBEotuniGPBZx2AosU6wzqKs2Lp3ksgnHyI7SG4OvSWjKVT1uQTahnGXcY17pbdZXf1YMNJrliBhpxJUOCp7DD4begsB4nnYt0fAZYiYODMT0xmfjLNgqx9beM3odREPPyXfHbfn4GfEUwM_YuTOKKEYS2AY1COgPesCLuYU1E9H1QPijf6agddeXhtgh09bY3JsjPsG4SmtlZzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NLlu8sYmgcJWH3FAF0fD05s_sIPUzz6uF0hFQED4rSV6PL2EE_yk4kmmeQ_oXl4uOn4y66Y1ckFjFJqs40iXtYn7B51pVbw0WafLijHWzD4AxqvgaF-icvwJ6C20skQ2iIoZK0RJbh3w-9Bav_Y00WPeUq6WDI3lHb_WNDqMiqXk_ccrbmAOUo_LxOVPflwAHtlJxeJlS1Cf77HvHgucJShNHUA6wk4rgXaWkjykwDBsWp2gB898n2J8jl2xNRJZnu28CyIqun0RlkEaJMwy0nUWXXq3HnU13dr3VjcCHt0nF6MPjvPjRzgqmM8M_iO3EKhcbkpZNDVyGCibldMtsQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
بازدید روبن‌ آموریم از موزه افتخارات میلان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99045" target="_blank">📅 16:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99044">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔥
🇦🇷
هیجان بالای گزارشگر تلویزیون آرژانتین در صحنه گلزنی مقابل مصر
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99044" target="_blank">📅 16:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99043">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLX9c0RRSZWOxo8MUpJj6p0Z3gszoGnDvJ8XjQK-FPLzNCZ-kIIb5_wMEy4uh4dc8s-VkHvDgppjMgoR46F39hWBLfV6_L86kDzdsCUFSOvrFGbvXHnLeC_KrjvjmAz7yI6JXyPg7vZLxjxbH0Tmmj7WjqcFpdEYY3TtYS5HXveyJFg3l26j80hEvT3uI1ac-SlAg0yWu7f_N_PleAZWDMXVw21iJYkfrlrQT9LFFg0TFEUurezi2RBgKvtXtaGDdYCn3PfW7_KvhONm_UEY4pyqsLsddpe8Iwg_bO32MWWjuZPRQc0cwnydF5IdA6QhpBd3wK-Pusa3nRv1JKbQkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇦🇷
🇪🇬
تصویری جنجالی از داور بازی دیشب مصر و آرژانتین در ⅛نهایی جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/99043" target="_blank">📅 16:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99042">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80c79c91f.mp4?token=X96-1H2nVfoZXcpuYMmaiSPLL_NCFMVw44qRCZ8KOZurSarWCqfN8d7ItLOIarmDroitxuMf-364BRKbKd4jrKiDg3dCIPgK3vVVWOR99djFhS97ZUOU2GinJkRC-7adFqcK0FH9KQ6t5B6sVBadRDtZiY8pQu8iXZd7nB-3qC5RLaWgj9-DpXUzjJWRPvoPF_xiZp2A7YSVECBpmDJQsDKhudEKPk1HFTo5K6UrlHuhMyEmuiC4fjj2rGXluqNrKL0nuwbrMzddeolVsHpZdOY_KVrAb-wc-4DLJKY4CrPJdlDTiWsxB1YVO7cJSpb4mrSE5cJj4rOaCXsH-R-bcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80c79c91f.mp4?token=X96-1H2nVfoZXcpuYMmaiSPLL_NCFMVw44qRCZ8KOZurSarWCqfN8d7ItLOIarmDroitxuMf-364BRKbKd4jrKiDg3dCIPgK3vVVWOR99djFhS97ZUOU2GinJkRC-7adFqcK0FH9KQ6t5B6sVBadRDtZiY8pQu8iXZd7nB-3qC5RLaWgj9-DpXUzjJWRPvoPF_xiZp2A7YSVECBpmDJQsDKhudEKPk1HFTo5K6UrlHuhMyEmuiC4fjj2rGXluqNrKL0nuwbrMzddeolVsHpZdOY_KVrAb-wc-4DLJKY4CrPJdlDTiWsxB1YVO7cJSpb4mrSE5cJj4rOaCXsH-R-bcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
⚠️
🇪🇬
تصور اشتباه مصری‌ها از لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/Futball180TV/99042" target="_blank">📅 15:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99041">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=Cxr33i3ptcvq4UtSIv4kXCFPA4PRkZeXEUa4WkgTbOFjx5dKnl4Xjuanf3AvHYcYC3XKOW2aORu8HCbbnG0XQ1uiLYevIWZ4R0ktQAIHnxrmfdogDlVmBZJn2Ae0FHGkEO-OaucOag-zPoWEx4jV7OUFTRLgRbjhPKxq5R7u8Wi9iD2EJva212f83NI1PaU599Fw-21EE4_3TKHXbWhpwx8GVRmxTc5gLIQ0b972zNv27yCeZC9isapCW2pEmCQcerD9ydGcqMxdRv2ZWwvo5C7_6icrJf9j01JCGXtnJl7rG5-rTTACvyaFiXp4KyBvgy2k9oYqUrYJETp0yZOGV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5807d621b7.mp4?token=Cxr33i3ptcvq4UtSIv4kXCFPA4PRkZeXEUa4WkgTbOFjx5dKnl4Xjuanf3AvHYcYC3XKOW2aORu8HCbbnG0XQ1uiLYevIWZ4R0ktQAIHnxrmfdogDlVmBZJn2Ae0FHGkEO-OaucOag-zPoWEx4jV7OUFTRLgRbjhPKxq5R7u8Wi9iD2EJva212f83NI1PaU599Fw-21EE4_3TKHXbWhpwx8GVRmxTc5gLIQ0b972zNv27yCeZC9isapCW2pEmCQcerD9ydGcqMxdRv2ZWwvo5C7_6icrJf9j01JCGXtnJl7rG5-rTTACvyaFiXp4KyBvgy2k9oYqUrYJETp0yZOGV4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسخل‌بودن که شاخ و دم نداره
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99041" target="_blank">📅 15:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99040">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=Bs-nn83WwnQWLpiIXvc3PDqS06J8UpRXQWQaka8hOUJn6OPf_Pe5wMvNxsesgrEkMdVSsezbNlJIiUtULByQB5aSQk2uMyAD079dn0MO4kdPHgJympA8tHvUZoE_7e9EwQ_FeFEum5fttYVKHF_ra5dmMThvTjxuoukFveWH51JU3KIYtzhMf24j_YQRo9VJKk-YwP7a-dhJ9Ec-_MoxdsSjZoR6bQzgHZ--UcKTjR6lDHUUEmi5j_eMIbs9HbwT2k8ktgDcBHzG7h6GtbnOsXXldsTJI-P8ra8wIUeKhakb6sCevL2dbn3jVvuuktJSQe0ca_rHv95GD-sDHyo2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/537c4a99f2.mp4?token=Bs-nn83WwnQWLpiIXvc3PDqS06J8UpRXQWQaka8hOUJn6OPf_Pe5wMvNxsesgrEkMdVSsezbNlJIiUtULByQB5aSQk2uMyAD079dn0MO4kdPHgJympA8tHvUZoE_7e9EwQ_FeFEum5fttYVKHF_ra5dmMThvTjxuoukFveWH51JU3KIYtzhMf24j_YQRo9VJKk-YwP7a-dhJ9Ec-_MoxdsSjZoR6bQzgHZ--UcKTjR6lDHUUEmi5j_eMIbs9HbwT2k8ktgDcBHzG7h6GtbnOsXXldsTJI-P8ra8wIUeKhakb6sCevL2dbn3jVvuuktJSQe0ca_rHv95GD-sDHyo2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
👀
ارزش دانلود 1000000000000
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/99040" target="_blank">📅 15:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99039">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lp021JLC_ewVeGP_w3ai6feL2j4OoC5tSG2c1gf8MqTHOBwfQ0XP8nQzDcjGIS3UkbgX9k78sHKqCdqhXzeksXKwcIhGLVGz6C4yFRCcL-a8pODy83U_unJ7-0k7DsrzRytWulpicx1jLL96R36T8CfNERbNmEWA54-178hFyOObWA6U66AyI_QqBb1LsQcIj0ihP8MLWInh4dUKdrchn5-u_NC-taCfL-xlVFJLDd1ZyjrLvJTJz2z_TB8neS1r9FzvkAleLL0aqvmX9IfPkh7fbeP6W1XqfyP5NNeEVKmSDSOoTxDFo35uapm0i7ApYZY1vBHReIEsyQDap6uyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیشترین پاس گل تا اینجای‌ جام
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/Futball180TV/99039" target="_blank">📅 14:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99038">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=IVhEIrBcqh5tyee9pz62oap9m0cqIvnRypf3345WPWw_fGr7B6A7hzrWO22OIRrhoAb8zsKrnAi8epU_OapDiTnAZEYtBN2agKt6sanNSv6-gqK7kwyf5XYGofSzf2Mqr5fucpGP3OkZ3vUK6x7peDxPxE4G_KkSCX7GYaQDtqtrTPf0qLx14VuLMM1Wj1Dow0axtJ32ELkFSzdykF3GqLmBzF2JSVADJ4f9-qVzXiZXyC3ORv80lf1H50UxmBE7FCQbwO0EiehxoQVeEWktqYDcrCtlxdcQR11Jljlf3yHqEEhjF_LXdep_KrHzW9Lvvclz_784jnXpPBXW3D5X8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41611ce35e.mp4?token=IVhEIrBcqh5tyee9pz62oap9m0cqIvnRypf3345WPWw_fGr7B6A7hzrWO22OIRrhoAb8zsKrnAi8epU_OapDiTnAZEYtBN2agKt6sanNSv6-gqK7kwyf5XYGofSzf2Mqr5fucpGP3OkZ3vUK6x7peDxPxE4G_KkSCX7GYaQDtqtrTPf0qLx14VuLMM1Wj1Dow0axtJ32ELkFSzdykF3GqLmBzF2JSVADJ4f9-qVzXiZXyC3ORv80lf1H50UxmBE7FCQbwO0EiehxoQVeEWktqYDcrCtlxdcQR11Jljlf3yHqEEhjF_LXdep_KrHzW9Lvvclz_784jnXpPBXW3D5X8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پدرو پورو
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/99038" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99037">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/99037" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/99037" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99036">
<div class="tg-post-header">📌 پیام #54</div>
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
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/99036" target="_blank">📅 14:41 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99035">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👀
نظر دخترای آمریکایی راجب بازیکنان منتخب ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/Futball180TV/99035" target="_blank">📅 14:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99034">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZ37GpYnri9Xzo8v81qZDXb6Gab3xfjgMdERl0OVZ4GnMDH6s32-5IiVQDe-18JP9y3PE2dO_iy1tuQy4pEgYT_2xZDI-TTuk72lDbLGGfnqm9lAw3BOOYxrFM8mvNhuWjVTS00mVFbB9BRzc5FyjyzYrFR0xV-9J7xWgPIScXAWsioDBeEAKG1j13ZcmXH7Me7XeszfySbK65ls6djAxtZV6ls6lpg4K64PArtgDXkXDjy_go9PE9fCql0oxiDO8PKYW1rbTIhNItlBt-1PnDyhU-V4OMt_m0JjU6cHJSamDPucBjd3Ne06maUX4psrY_GHyQPW3Xc7ZYcuZCGK-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇷
تیم ملی کرواسی از جدایی زلاتکو دالیچ سرمربی این تیم پس از 9 سال خبر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/Futball180TV/99034" target="_blank">📅 14:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99033">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=a8CJK4_oHRBpd6mBazsn5-0kyM-3z0lXpKfBUrI3Hr2JDI0fiNqKWr5aBOn88IMxp9PTxWRN7TNRUaN5-u4qT01mCb6QYzghos4zXBx9Rrd--L27UiGl5OFsIKjSZzApJ2iyotN54UYwR64YyHgJFC1bgqn_djIMPc5CROo9rNh5jVdaF6lDRgFVJPNxt0dKFbAFOMb4ZZjmsZyQPAP7v8Ad-XkikYoNs20CzdTOimb8hLdJRLBoDO-H_g0rGkMFBPZ6zFswDOGCTJJV2ie__LhyN9Enwpei1EFzZvWg_Gi1kYnh0bYYfDt6KnbzKg2y7SNH_6B3qp1atuhkAQyH6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fa320e90.mp4?token=a8CJK4_oHRBpd6mBazsn5-0kyM-3z0lXpKfBUrI3Hr2JDI0fiNqKWr5aBOn88IMxp9PTxWRN7TNRUaN5-u4qT01mCb6QYzghos4zXBx9Rrd--L27UiGl5OFsIKjSZzApJ2iyotN54UYwR64YyHgJFC1bgqn_djIMPc5CROo9rNh5jVdaF6lDRgFVJPNxt0dKFbAFOMb4ZZjmsZyQPAP7v8Ad-XkikYoNs20CzdTOimb8hLdJRLBoDO-H_g0rGkMFBPZ6zFswDOGCTJJV2ie__LhyN9Enwpei1EFzZvWg_Gi1kYnh0bYYfDt6KnbzKg2y7SNH_6B3qp1atuhkAQyH6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
تمجید لائوتارو مارتینز و خولیان آلوارز از مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/99033" target="_blank">📅 14:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99032">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaKI2rwLHfrlRmzZAlkcVFQ4h1jqolPBqrQkRDRwuYEVJ4SnK1FJhf9auVMuzUXrz8TiSGunsN9IsiTaLb6eEV7L4UuHPpZiIBekgpFnyryZLXq9GETWOnJ0qZVPpEYeqadEqiPHOoZ7H8uUh8klfV3EdAg3qq6OHX8-2FeiobqCn2LuoNVdIh_hvB_QlT7-sqNZDj4THNwA6tA9MSIS_X7_p-U1duOW8dSfMsN8ZS6bWK3n7WouvSavTIW7qlCSsEQvwDp1Wkm3bbkbxh8oOMxoKRmNYcueEcQ-FKBeEg_5Zuu6L2g6HJeWFn-DVnvaqttNKEpVpKL-qaqbVc9NRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙂
وضعیت قلبی برخی از طرفداران فوتبال:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99032" target="_blank">📅 14:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99031">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=I-AFkWPMfOFl3pVRQiN0zNj6A9hy5XxrWDJAL2s7X20Ik9NH6ztAgHtZxE-w0v7xRNWxzGi3jVEbr8kzkYGjb9BUIBWTwcC7J2lOLOJyVdMl8SdiLL2WFKDpOf5vZOTfNGqDbrupbxRsfuYOOs9nrVf8nzAlPzPEBdMnHhYu0qHpEv_FF44PuZDbKdAfS6AVhUPl_cFyS271Xtk1NLejdhPcjlFwCoCwJB8J_WcplBUntK5y1GyCVP2hhNAoYsHf7tNVL1oL-S5b5BxxnQGxAFqSF7zXNxDk10VHR804ySjdKpFgwojul7KPufsrN5cjd1oMj-odCCPMWm5UKjtrIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e4a201f71.mp4?token=I-AFkWPMfOFl3pVRQiN0zNj6A9hy5XxrWDJAL2s7X20Ik9NH6ztAgHtZxE-w0v7xRNWxzGi3jVEbr8kzkYGjb9BUIBWTwcC7J2lOLOJyVdMl8SdiLL2WFKDpOf5vZOTfNGqDbrupbxRsfuYOOs9nrVf8nzAlPzPEBdMnHhYu0qHpEv_FF44PuZDbKdAfS6AVhUPl_cFyS271Xtk1NLejdhPcjlFwCoCwJB8J_WcplBUntK5y1GyCVP2hhNAoYsHf7tNVL1oL-S5b5BxxnQGxAFqSF7zXNxDk10VHR804ySjdKpFgwojul7KPufsrN5cjd1oMj-odCCPMWm5UKjtrIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
#فووووری
؛ ابوالفضل جلالی بعد از مذاکره با مدیران پرسپولیس، بدون صحبت با خبرنگاران، محل جلسه را ترک کرد. گفته می‌شود کار او با پرسپولیس را باید تمام‌شده دانست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99031" target="_blank">📅 13:57 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99030">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pSevVGVRUZIdAV896rJ3ctl_RWYtZ3auHUiL8CfUCeiHpGu7BYNK3juV1lnmUOev1XWWHZ683_p1VE7FRBr5a5KK5B6oOtkz6BDmnEMlwvcHs3RWlDR3yDnkZS8Q18UrIk7mlUrBkwRhcGFM26yJUi5bg-qhX1lXJKd3ZR7VdPa4X11o9Va6Xdq6eaEBguGrLFOtf4oJLjZ99dB_8gL3o-92LKvk-bOD3RVvWTkeNsobNQyATW8djE47UnE-ineaJJwW010c6appL_Zwz2Q-gQq6d2Xlnv9Hw_ZEW5qT6bB9l3RlTlkuw2p6f0jAAS_sJFcZWec2u46-Q1yf4TPQmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇦🇷
#فوووووری
؛ بدلیل توهین‌های نژادپرستانه هواداران آرژانتین به اسپید، فیفا قصد داره فدراسیون فوتبال این کشور رو جریمه سنگینی کنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99030" target="_blank">📅 13:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99029">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afc2e7e2d4.mp4?token=osnUb-aC9ApBVdmm17uejGybw0FzQT53fZFZRKqvwghmy0_f2NkHM-ZKenTZdhkc4WZD7LPr_bU5xtA1ckG5lmY7Wy2pUrUL7uVDRhKNXKOH7wUkvKe90quBQ86yTNN8Qqa_PxDWMP6WiMJDHQbKBLRHahJ1bEo-sW_f2Yp_bdFkzR-u4hwOOdg2FVUVRH3vWtU2w-pQ1hIf9TqAQEeKBqenVZLMS6myY50a8i8uBJLZW2_Ozhq0Vrz_UYeebkc0jeRDgtk5spw3qn110n1XVGvDSn3JqG7syM0TCozKYar0wBfwx9Xz3TT9wlXPsxGsE-a9Cx7Si5D97DWh9zmuLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afc2e7e2d4.mp4?token=osnUb-aC9ApBVdmm17uejGybw0FzQT53fZFZRKqvwghmy0_f2NkHM-ZKenTZdhkc4WZD7LPr_bU5xtA1ckG5lmY7Wy2pUrUL7uVDRhKNXKOH7wUkvKe90quBQ86yTNN8Qqa_PxDWMP6WiMJDHQbKBLRHahJ1bEo-sW_f2Yp_bdFkzR-u4hwOOdg2FVUVRH3vWtU2w-pQ1hIf9TqAQEeKBqenVZLMS6myY50a8i8uBJLZW2_Ozhq0Vrz_UYeebkc0jeRDgtk5spw3qn110n1XVGvDSn3JqG7syM0TCozKYar0wBfwx9Xz3TT9wlXPsxGsE-a9Cx7Si5D97DWh9zmuLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🐐
نیازمندی‌های خونه هر مسی‌فن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99029" target="_blank">📅 13:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99028">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
⚪️
#اختصاصی_فوتبال‌180
؛ آرمین‌سهرابیان مدافع استقلال که از حضور در تمرینات آبی‌پوشان منع شده، پیشنهادی از گل‌گهر سیرجان و مهدی‌رحمتی دریافت کرده که در صورت توافق مالی، این بازیکن بار دیگر به سیرجان بازخواهدگشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99028" target="_blank">📅 13:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99027">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🔴
⚪️
#اختصاصی_فوتبال‌180 #فوری؛ حداقل دو بازیکن گل‌گهر سیرجان در فصل‌گذشته بزودی با پرسپولیس قرارداد امضا خواهند کرد. یکی از این بازیکنان مهدی تیکدری است که قرار است جانشین دنیل گرا شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/99027" target="_blank">📅 13:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99026">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZB3ajIJThWdfUKTknl8X9ILoLvrUWu5UzbQ6dm7jgjA-Ed_CgdXj_EoYbCD90ivlkdpW62tMcUjQHZf-OZ9VK_szdKjurk6uxWUhwq3c4UwGlG1ttqSmIs9Wos87AVjoG8hYeSQd_DT-gw4FAHFjYKecJd4VsCe5tefWKe_q5KH8cDiiAHu4xS3bfcewiUf-dzaVN6pShp9lJ2Az1u4bRqpOi7lL_Xiuyn3aCQGUtXUomw-Fplc1gwFXaXOyK7PULQQ3wpo2Wy7oi05HbyYpu_rjPzKPckbjF48uTOmENTNCtnoMnoZE4YUmDxTz5dJNqU0i6bUzUbuGuIlduuRJcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
جمال شریف، داور بین‌المللی سابق:
- تصمیم داور مبنی بر باطل اعلام کردن گل مصر، تصمیم درستی بود.
✅
- تصمیمات داور مبنی بر عدم اعلام پنالتی برای مصر، تصمیم درستی بود.
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/99026" target="_blank">📅 13:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99025">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eo7PlKvSuLiWWOYfpd4hQ52hjz77h86wvm5kibHT0Fu48Cpcr_2YzIT1X425W64iMs1eBYTrVRThDu6vvZEWT0Rm0VCKfEvtrgjTikeBmzWP3OCYiyV_ExF-DCqoY_qWNuhxf8ArjNYjtxEl1hDjOBJvigqdRzLBvh9DMGDFqVRH_eMtRb2ZXFFGM2sGDxLfhTDisNbJOt9iosTDOVSe6Kt1lsbhtX3m3xQDVddxrvywZg0zIb6gJnG2EElHsUIZwfLtFxROulychSPWk0fseZZGTitfDSM_Z3k2TCeFUeMrzWKftoUl-s7vqJ0iJAQGQKraBJRXce50g6gifAPITg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
‼️
تعداد دفعات اخطار (کارت زرد) دریافتی تیم‌های راه یافته به مرحله یک‌چهارم نهایی جام جهانی
:
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس: یک کارت زرد برای هر 7 خطا
🇲🇦
مراکش: یک کارت زرد برای هر 9.8 خطا
🇧🇪
بلژیک: یک کارت زرد برای هر 10 خطا
🇨🇭
سوئیس: یک کارت زرد برای هر 11.5 خطا
🇫🇷
فرانسه: یک کارت زرد برای هر 12.2 خطا
🇳🇴
نروژ: یک کارت زرد برای هر 13.6 خطا
🇪🇸
اسپانیا: یک کارت زرد برای هر 17.5 خطا
🇦🇷
آرژانتین: یک کارت زرد برای هر 22 خطا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/Futball180TV/99025" target="_blank">📅 13:12 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99024">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ddf556eb1.mp4?token=aT1EMWf9iUkckMIcQNeQs2bti2YMUfSBYDBL8YkMXQfIzssD3AGVW1cQTP54G4yFLcsgTQEr_HxImmUTc-imY316ZAfsOZX1c36_nt6JGAR5BMtn6TrXdF6UCTttMvqdswEZfbLJK767SiQT_-SHbrkCBKlKj_1xi71e8ugHaPb5MRaFcY8wKST77H37FMKJyAfADilI1kWMQi8zX-Yr1tc20EAavZv_5bX6enMMtQ6dLRRuzeBCte3p-K14VEZuWSlKm-vuX7z44jKnFG8BP8g_wi1l-piHh7TYPP6zZWaZcy-xRMiey4td8kN0pbC0bFgrLX23N9Xs53oj7a07cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ddf556eb1.mp4?token=aT1EMWf9iUkckMIcQNeQs2bti2YMUfSBYDBL8YkMXQfIzssD3AGVW1cQTP54G4yFLcsgTQEr_HxImmUTc-imY316ZAfsOZX1c36_nt6JGAR5BMtn6TrXdF6UCTttMvqdswEZfbLJK767SiQT_-SHbrkCBKlKj_1xi71e8ugHaPb5MRaFcY8wKST77H37FMKJyAfADilI1kWMQi8zX-Yr1tc20EAavZv_5bX6enMMtQ6dLRRuzeBCte3p-K14VEZuWSlKm-vuX7z44jKnFG8BP8g_wi1l-piHh7TYPP6zZWaZcy-xRMiey4td8kN0pbC0bFgrLX23N9Xs53oj7a07cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسطوره تاریخ فوتبال لیونل‌مسی
💀
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99024" target="_blank">📅 13:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99023">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aff9a0d70.mp4?token=v0qjz3VW13IEellQCWJE_7hF9l6zqxn5okUtWzga5IEmyAbscq3tmT8mzOE1ZWNcbROk7CHXwWUDCRRceaHhdUu_Z7PK9GVp4fiYl84ehVz73LTPHqfmkO2k83wd4-aDfXtBfOG5OhXK4QCeM813WB-emo5UPMccNDXQ6A2SFdCyYKKqgO2KhjEKRrdObBuwJOUC2gmTUP3Bhd-Ms5KTxXZTpmawg6r4VgU_bzLjhCDI5lkO8AKjAqMqVj9phHZqzy-NWkJzd7DjvTzJLkUPkWLmtYPbXW8owEksY6Ly0xcsYupy9hogdo5VAJHH0uQEIcjw-5YF7XB10Qy16enXPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aff9a0d70.mp4?token=v0qjz3VW13IEellQCWJE_7hF9l6zqxn5okUtWzga5IEmyAbscq3tmT8mzOE1ZWNcbROk7CHXwWUDCRRceaHhdUu_Z7PK9GVp4fiYl84ehVz73LTPHqfmkO2k83wd4-aDfXtBfOG5OhXK4QCeM813WB-emo5UPMccNDXQ6A2SFdCyYKKqgO2KhjEKRrdObBuwJOUC2gmTUP3Bhd-Ms5KTxXZTpmawg6r4VgU_bzLjhCDI5lkO8AKjAqMqVj9phHZqzy-NWkJzd7DjvTzJLkUPkWLmtYPbXW8owEksY6Ly0xcsYupy9hogdo5VAJHH0uQEIcjw-5YF7XB10Qy16enXPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇹🇷
تو یکی از لیگ‌های سطح پایین ترکیه جوری داور رو کتک زدن که بنده‌خدا نای بلند شدن نداشت
😐
😐
😐
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/Futball180TV/99023" target="_blank">📅 12:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99022">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🇧🇷
فدراسیون فوتبال برزیل حمایت قاطع خود را از کارلو آنچلوتی اعلام کرده و این سرمربی کهنه‌کار به فعالیتش ادامه خواهد داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99022" target="_blank">📅 12:34 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99021">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/869cf9501e.mp4?token=CRJru3PRFfu4BnUErgRYIjsiy2rT8OJ3q2zqkQQ2cFQJ-SQVv_ZmJNjQtaYf14_VrL53KJVZM4h4OPpKUUnqgvHI1aYjq_iAosCl4Y_GdGjswMrr1rPCFd5QHATaSNZ1--4RyJrNLyIpcgGRTffNowJxltjP-g6LXUrggPvAIY7OTcZaEJBBzTxbCFIqN-K_2_9UeOiq2HwgGE3Uev9MS6bJaUshGYYdl4RLdVNKfxdiVSbiudmqAihHDxGHtB3spNt617qoq2jK3XobKs8DlGSeJAYNnaTsJ-65FfDPVrjvXaFIXqtS_zFbbyBjmU3Xo_rjZxTQQ05g5UoHqW_qvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/869cf9501e.mp4?token=CRJru3PRFfu4BnUErgRYIjsiy2rT8OJ3q2zqkQQ2cFQJ-SQVv_ZmJNjQtaYf14_VrL53KJVZM4h4OPpKUUnqgvHI1aYjq_iAosCl4Y_GdGjswMrr1rPCFd5QHATaSNZ1--4RyJrNLyIpcgGRTffNowJxltjP-g6LXUrggPvAIY7OTcZaEJBBzTxbCFIqN-K_2_9UeOiq2HwgGE3Uev9MS6bJaUshGYYdl4RLdVNKfxdiVSbiudmqAihHDxGHtB3spNt617qoq2jK3XobKs8DlGSeJAYNnaTsJ-65FfDPVrjvXaFIXqtS_zFbbyBjmU3Xo_rjZxTQQ05g5UoHqW_qvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🇦🇷
لیونل‌مسی با این طرفداراش محکوم به بردنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99021" target="_blank">📅 12:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99020">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
‼️
🎙
🇦🇷
اظهارات ژوزه‌مورینیو سرمربی تیم رئال‌مادرید علیه آرژانتین و فیفا:
🔹
وقتی شما دو گل هم جلو باشید، باید به این فکر کنید که تنها با ۱۱ بازیکن آرژانتین که در راس آنها لیونل‌مسی است بازی نمی‌کنید بلکه باید توجه کنید که اتاق VAR و فیفا هم مقابل شما قرار دارند…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/99020" target="_blank">📅 12:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99019">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WZJ95YyZc1xVwbMlFw_35VmCdwNp3Ay5IuvbPWp_xzMVhRHmhBQ8WqnDVl5Gxxp37qHT_S_TIyUf0eC7j3rkbHgT3C2jIrxCEveBS8X1G5U1Jqc4trSwa8ol4eG3bptBn8R-E2KMCY-OwxJL4dD6hivAGl7E_tYt3qC9xME9eBDqq_8eaqPua7-3NtY83gIR3IniMcCjUeLxKGb75imVpYVn0WIgub6DSEk45u5jnzUG--HRRvpnZ8KWKg6UGfwFKSUcOstcS8ype5YTCGSSxFhin6j8Do2s7yxsPeed022BHgGNvJdPYTIaA-oJU0pILubZCxAQRIMz23ihNU8jZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خوزه فلیکس دیاز:
منچستریونایتد به اورلین شوامنی پیشنهاد قرارداد پنج ساله داده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/99019" target="_blank">📅 12:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99018">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfJne72c8SxSv4LC9RZwckGHEki7NddSuk_ABxIDWyBT6M4-g-W35AB0et9uZP7wcH_TWJYeHD5uBTmsZeY6l0psm19KPGtpU8_l0tdMhChl9cPlNlT_y5jPOyKBGpITWU26NvhXpm2jUsnPKYxkSJBFLkRr5HzR5-V6nbS_yYjWRZ2_nkhI5Th7aNAxLQXbkwICLcpu05sh2e4f0h-ZD5UIimUu_77q83NDfoXGLhRTQHwB8m5vA9yK7FHEI-m6XuVmP_r0VCSigAm6H7ci2BfeE6qPp1BWjxc1Eo--YCfI7LSQ9-9-qhc-95GIbFPVnG17TENA_2obLrJwQAG1KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🎙
🇦🇷
اظهارات ژوزه‌مورینیو سرمربی تیم رئال‌مادرید علیه آرژانتین و فیفا:
🔹
وقتی شما دو گل هم جلو باشید، باید به این فکر کنید که تنها با ۱۱ بازیکن آرژانتین که در راس آنها لیونل‌مسی است بازی نمی‌کنید بلکه باید توجه کنید که اتاق VAR و فیفا هم مقابل شما قرار دارند
🔺
مصر شجاعانه بازی کرد و باید به آنها آفرین گفت اما این سناریو مانند فیلمی است که از قبل نوشته شده و برنده داستان هم قابل حدس است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99018" target="_blank">📅 12:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99017">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TjQ5v5nDcyoOZvm4xQUarosu3VcGWb0ATXZuSPgD6T8l3Y5hinmJmcsagijKnl3JJQ4umoRne3RtXThkbGo2Lmzh4cQukluKp9PnjyOFQVXUinIdOVpcQ05DxrAPSm95v2G03zk9S1zeE7LCwpRjBf3IgOQVq_803Ng5IEbB54HFb1_0RdHRtAxxU1tUm-CGWcv6YxDg9degwwpKR3mMDxRySKSwbz87W9vHaXT98cFieJa7nnjkZzGplrJ1MUzwPXTVby7gtI4WZ_1D5AEoBwKyRkhCT9O3k0b9NCSJGCRwx8w0OT38cYc7VCaBPZV8s0iDSWMqg-8a4Fn3s3tkHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🤩
ابوالفضل جلالی که چندی پیش اعلام کرده بود حضور در پرسپولیس به معنای توهین به هواداران استقلال است، تا ساعاتی دیگر با عقد قراردادی دو ساله رسما شاگرد تارتار خواهد شد تا به عنوان یار ذخیره میلاد محمدی در جمع پرسپولیس فعالیت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/99017" target="_blank">📅 12:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99016">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری از ترامپ: تصمیم برای ادامه مذاکرات را به کوشنر و ویتکاف واگذار میکنم اما از نظر من دیگر تفاهم‌نامه قابلیت اجرا ندارد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/99016" target="_blank">📅 12:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99015">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوووووری از ترامپ: آتش‌بس با ایران به پایان رسید و از این لحظه هر دستوری بخواهم برای زدن ضربه نهایی خواهم داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/Futball180TV/99015" target="_blank">📅 11:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99014">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری: ترامپ: توافق‌نامه همکاری با ایران به پایان رسید. ما زمان زیادی را با ایران تلف کردیم و باید کارهای خود را انجام دهیم و دیگر خبری از معامله با این افراد شرور نیست
🔴
شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/99014" target="_blank">📅 11:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99013">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوووووری
: ترامپ: توافق‌نامه همکاری با ایران به پایان رسید. ما زمان زیادی را با ایران تلف کردیم و باید کارهای خود را انجام دهیم و دیگر خبری از معامله با این افراد شرور نیست
🔴
شب گذشته، ما به ایران با قدرت زیادی حمله کردیم. ایرانی‌ها مذاکره‌کنندگان کثیفی هستند. ایران به کشتی‌ها موشک شلیک کرد، و به همین دلیل، ایالات متحده واکنش نشان داد.
🔴
آن افراد بیمار در ایران، چیزی بیمار در ذهنشان وجود دارد. آن‌ها بد هستند، من آن‌ها را دوست ندارم، هیچ‌کس آن‌ها را دوست ندارد، آن‌ها شکست‌خورده‌اند، وگرنه تا همین حالا یک توافق به دست آورده بودند. ما رهبری اول آن‌ها را از سر راه برداشتیم، و حتی رهبری دومشان را هم. آن‌ها افرادی بد و بیمار هستند، باید از ریشه نابود شوند، مثل سرطان.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/99013" target="_blank">📅 11:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99012">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3T5kKh7grDR86sPN7wYIjnCfvcZy8ynq3u_Dk8uuj_RhOrBa_6C_kbFJOSn-PcsyFdxaX1XQzie7W9BhLAjfV4If9dG1Cp_aFU9EOe733XiEJqH2V0WFZG1JxpnHoIytpbdDJ5OlidyocaxyUHUEWSkZOkQ2EhL9kmU51Nwtf_oB-bLG__gkoly5-10AZ0X5JjGeQgcXemFlM3WmRL2I5Q3hOTGPTKHKxBQE36X9Cn9FS1FxzPHBU9u7w1p3SpI6bbruKx9E52Fccy76mIbN4RBiI52GiDBVGwwVZBbS0vLhh0WoriIxxABNwsXFADg0tB4Z09UoKkk2eJE0HP3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
اتلتیک: رئال‌مادرید تصمیم گرفته که در کنار داشتن کوکوریا، آلوارو کارراس را نیز حفظ کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/99012" target="_blank">📅 11:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99011">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uAQ5b_i4_zjK4ZOFYzqODvZ_7_nFpMUinm_wCZ1aqt3EvLy1mKQH9HhmrYG_ZTP43yKmm0nxSj0UoEechHMzsVEJDkv9C2LfcjX5l10FPoNQky07eqKja8PFmbcXybfss6KCLaZoHVc825gvBv4-vnxAN9dELb-zO1JrEh0Oh5XiSq5ku8e5W_-e3sfnHsBO6aW9S3kw59TKSjJO5PLwGL8Ld9ella4aiGUVqjooTTlxvlQ44TZAgW-TVhYAHWTIlEWgBOD0i7Nge6-wrX65EDDMwIFJ1byyCvOOxkUvrbLJZnFMMeFZtadfldO3OtI9JfLXtAWvCsF-lvaxzhUiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🤩
ابوالفضل جلالی که چندی پیش اعلام کرده بود حضور در پرسپولیس به معنای توهین به هواداران استقلال است، تا ساعاتی دیگر با عقد قراردادی دو ساله رسما شاگرد تارتار خواهد شد تا به عنوان یار ذخیره میلاد محمدی در جمع پرسپولیس فعالیت کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/99011" target="_blank">📅 11:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99010">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37082570ef.mp4?token=keUM382AD5vmcnsYqheBHT6MXkQhvubEsRjrccYAAFZqNHEODXkzJ8Ejgi5fLrTjKliqIMePBWV7AMqnsrftrOIIFwD_Nu6lREQX_a-oOLlFkloQGz3n3_q_0_SOj6f_FZIX54WyhKPD_1ylNyyKbfqqhO4IPvO4kGS3vaQeBZR30mGRYR2-aMIANXB_QB4MN2x3pIoUsn83DWFUcQXKcGvSs2RxdVjc1o9xe8UQH1j2Pj9_leetBE5RRNb2up4SyllBDWownKxJeDIFBlRSnjt-I8x0nZ-jd8bUXGDdyhGe5OM3KfsisdvBX4ceBqOCxjiC-OarQtPSEDopnFM8I6JeN2Hsvm3IIdox6KUOXzTV8EVTKCPu8rJxLotnAHcZmuzgPhVPsC86Gl7xLugHq0LNoqCKCGdwXbtaHrqBDof1NxlfbsHAxnf0UYtKnmV9aKpbIPhLUDnuWuKxN6Jjg4AtIBgJWoYWe3WSaSHq8Bv5VyXSoYaN8sJOU_z-B8Oa4wekykQuNfSfl87bn4lroDvM7-5iLFxTgyHxtoeLqQTY4YtCaTnItGeyFF8CYJJNrIYw7RiJG3BDS4h6TgbsCnK4dyLTLviGVXKF9r9cjKB4otCA7VX343aqzv_VMnreE5La56JBcL0D8vL-D7n61VImsxjifrEVix5mYux_nEE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37082570ef.mp4?token=keUM382AD5vmcnsYqheBHT6MXkQhvubEsRjrccYAAFZqNHEODXkzJ8Ejgi5fLrTjKliqIMePBWV7AMqnsrftrOIIFwD_Nu6lREQX_a-oOLlFkloQGz3n3_q_0_SOj6f_FZIX54WyhKPD_1ylNyyKbfqqhO4IPvO4kGS3vaQeBZR30mGRYR2-aMIANXB_QB4MN2x3pIoUsn83DWFUcQXKcGvSs2RxdVjc1o9xe8UQH1j2Pj9_leetBE5RRNb2up4SyllBDWownKxJeDIFBlRSnjt-I8x0nZ-jd8bUXGDdyhGe5OM3KfsisdvBX4ceBqOCxjiC-OarQtPSEDopnFM8I6JeN2Hsvm3IIdox6KUOXzTV8EVTKCPu8rJxLotnAHcZmuzgPhVPsC86Gl7xLugHq0LNoqCKCGdwXbtaHrqBDof1NxlfbsHAxnf0UYtKnmV9aKpbIPhLUDnuWuKxN6Jjg4AtIBgJWoYWe3WSaSHq8Bv5VyXSoYaN8sJOU_z-B8Oa4wekykQuNfSfl87bn4lroDvM7-5iLFxTgyHxtoeLqQTY4YtCaTnItGeyFF8CYJJNrIYw7RiJG3BDS4h6TgbsCnK4dyLTLviGVXKF9r9cjKB4otCA7VX343aqzv_VMnreE5La56JBcL0D8vL-D7n61VImsxjifrEVix5mYux_nEE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
این 45 ثانیه رو ببینید بعد بگید هوش‌مصنوعی خوب نیست و بی‌روحه. خاطرات زنده شد.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/99010" target="_blank">📅 11:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99009">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeadf8f078.mp4?token=giJDCWF4oEisxTc2KbGMsZVismWL-2YctqM6hKr9fO7FvmqP1teb5DeLWD4YOyO8RhWFQuB2albnETusc2PEFZGJw_NCdCboqhHsJgAUK6dTyt3xcgbUiu9x-gaj9HfZKykgTzPei_2AfZVJmkS9WxTww3c_leV0tpHWGbDazaxT3VHJzaKXwxG3tGihFZSvBbhsjsF6iVfV3RkngiKwDSSzicmxr0uvvVjHIUdUJGzq-4bJjZi1h3QbqafygKMByEKhzo5qCTaPI2kPMYK8NBRc0qYyIH1gOb8s2pwxSf-fAP8_U0qfeOQ2O3m1axvmaaEVVqVsP7cxYhQ8akWtARGUjhy_BOKPzUoKugZAbuDiUXHcKe149r0WR3hF52NAFg620m30jwgZx6O8xkuwdRgKJ_SBqFc9BQXqv7WVhiYgQsMxGO_RdTGV2KhgZ_UXHrDhAnYpif-8-IGpNgWlSqjswPrmbDROOHAICpLnJmw4hDKQL_pwkOaHhbHiSKkOmEOikbroCgam3y2Yx9ETgYM1Ep5Q1EMMDXyYgJd3hnJf9ahVveMka379s-NeR_uETLNuivwQEqQHahnGLcD2QaWIzHEqKv25SMoiJrQCXFmjS0MHt8IhYe_WZ_x8O9yYvHH21t1w7gL03N1p8de8uenvLO4hP7fbk7_GjPDvh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeadf8f078.mp4?token=giJDCWF4oEisxTc2KbGMsZVismWL-2YctqM6hKr9fO7FvmqP1teb5DeLWD4YOyO8RhWFQuB2albnETusc2PEFZGJw_NCdCboqhHsJgAUK6dTyt3xcgbUiu9x-gaj9HfZKykgTzPei_2AfZVJmkS9WxTww3c_leV0tpHWGbDazaxT3VHJzaKXwxG3tGihFZSvBbhsjsF6iVfV3RkngiKwDSSzicmxr0uvvVjHIUdUJGzq-4bJjZi1h3QbqafygKMByEKhzo5qCTaPI2kPMYK8NBRc0qYyIH1gOb8s2pwxSf-fAP8_U0qfeOQ2O3m1axvmaaEVVqVsP7cxYhQ8akWtARGUjhy_BOKPzUoKugZAbuDiUXHcKe149r0WR3hF52NAFg620m30jwgZx6O8xkuwdRgKJ_SBqFc9BQXqv7WVhiYgQsMxGO_RdTGV2KhgZ_UXHrDhAnYpif-8-IGpNgWlSqjswPrmbDROOHAICpLnJmw4hDKQL_pwkOaHhbHiSKkOmEOikbroCgam3y2Yx9ETgYM1Ep5Q1EMMDXyYgJd3hnJf9ahVveMka379s-NeR_uETLNuivwQEqQHahnGLcD2QaWIzHEqKv25SMoiJrQCXFmjS0MHt8IhYe_WZ_x8O9yYvHH21t1w7gL03N1p8de8uenvLO4hP7fbk7_GjPDvh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇮
کشور شاد و بی‌غم فنلاند یه مسابقه راه انداخته به اسم حمل همسر که میتونید ببینید
😐
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99009" target="_blank">📅 11:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99008">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=eiuvfJ7KrBrJ7iD1k2Hm1MUagUhfRx5db8xTLOF907pfdeC6MvJ_kJ-5x9j7eOjoAgiesxSL_dXIFjEKADo2PnoH-RqyaqTlw0s9MARaul3r6sQ6xN7CItq-Vntfe4Pdqh95qaB8TRj7Y-n3PV9qOnBAI59t12VYpOEAOt_ruUcbAvVy3JvZUZLjSJNd112ogcP5yx1ftzj1qQ3J7N7xZlx9Wb5t5CprlRZgb_nTTWgIlJOZnnLLpK2ktv3DrLPmL05p2yd4qP7U_h4pmWfojqOog2SPsSHfNhFToL5U4koyLZJXyX5gMZcHa_KtJ1II39hA_3GlWFohZM4E3YF4Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f700303ae.mp4?token=eiuvfJ7KrBrJ7iD1k2Hm1MUagUhfRx5db8xTLOF907pfdeC6MvJ_kJ-5x9j7eOjoAgiesxSL_dXIFjEKADo2PnoH-RqyaqTlw0s9MARaul3r6sQ6xN7CItq-Vntfe4Pdqh95qaB8TRj7Y-n3PV9qOnBAI59t12VYpOEAOt_ruUcbAvVy3JvZUZLjSJNd112ogcP5yx1ftzj1qQ3J7N7xZlx9Wb5t5CprlRZgb_nTTWgIlJOZnnLLpK2ktv3DrLPmL05p2yd4qP7U_h4pmWfojqOog2SPsSHfNhFToL5U4koyLZJXyX5gMZcHa_KtJ1II39hA_3GlWFohZM4E3YF4Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇳🇴
تیزر تقابل جذاب انگلیس و نروژ
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/99008" target="_blank">📅 11:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99007">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dIMnifX7HgV9gG-Z1zA9qpgg571kh3d1hlCh6kOiCbqPmyTf7RrqGtCNcHFiEHw3BFnlManS_bAUrNh9qFrqUrgz3U9eDvm1iMmUklJ7y2k6fIajCdN4czKV6R-jPxZ7ARXTihtEdePFfaAnNSFmxOs0athja50HdxuDX9W561OkfaFi6bh-Zgr20FJRpIMpR-vkBX_ZhtD3IajfPvXUnOOHJ5mqxepVKCi3whZEBnEweAv4SWekDhdGgtSIUWRJlVDC35L_OluLhVWEwI8-YfLrOcQkWB12MVurKUA0z3h0RtjDkHAiFytNbFuoemiG2hd5XD0-18vcLcoFgtf9oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇲🇦
♨️
مونیرالحدادی ستاره استقلال در آستانه عقد قرارداد با اتحاد طنجه مراکش قرار دارد. این بازیکن که با آبی‌پوشان یکسال دیگر قرارداد دارد، به استناد به شرایط جنگی ایران و بارداری همسرش قصدی برای بازگشت ندارد و احتمالا با توجه به تعلل مدیران استقلال بزودی قراردادش با تیم مراکشی را رسمی میکند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/Futball180TV/99007" target="_blank">📅 10:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99006">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/99006" target="_blank">📅 10:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99005">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=NkeDbl7kTOQt_kondN3MUxQEq-lxgPLptnt9a0rL7mu4HAENBABWyXtsh10pdKxCVcWi5HSu-QU_pn1Hyp9paSJnmlObdd7QC_bK_JwwyiiUCUydoFAjmwLGjPETcJfu3tmJNfYt2JYeXfqwXF_Agp3e8TL9vkBiAxTACPMbhO6erTZvETKis4YKok2sihnlApVoyrqqAykLtH08If0JZKe_1UgQIIVl-oT5BylaVd5XJA5V8bfUTVgezLD2Os3p0B2WHHLm7RmwX9KeBJKSZAJ5_FF7BgrXenkMqlqbYpLfXH1vZ7Q8bco3ll993HkwUMgSZZl8kRbpqpPKAqBd9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235d7e30f7.mp4?token=NkeDbl7kTOQt_kondN3MUxQEq-lxgPLptnt9a0rL7mu4HAENBABWyXtsh10pdKxCVcWi5HSu-QU_pn1Hyp9paSJnmlObdd7QC_bK_JwwyiiUCUydoFAjmwLGjPETcJfu3tmJNfYt2JYeXfqwXF_Agp3e8TL9vkBiAxTACPMbhO6erTZvETKis4YKok2sihnlApVoyrqqAykLtH08If0JZKe_1UgQIIVl-oT5BylaVd5XJA5V8bfUTVgezLD2Os3p0B2WHHLm7RmwX9KeBJKSZAJ5_FF7BgrXenkMqlqbYpLfXH1vZ7Q8bco3ll993HkwUMgSZZl8kRbpqpPKAqBd9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇫🇷
🇲🇦
تیزری جذاب از نبرد مراکش و فرانسه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/Futball180TV/99005" target="_blank">📅 10:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99004">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12da15f688.mp4?token=KQf-MjTfF6IvpH0-k4E_D4ct3oEBPVsBpYuwuVtLMZRiqOgL8FosI5zqZ2sVeDFtAsRVvy4L2cHVCMaCLauA2D4umYQ09Nqjxvnvy3EqTPJJdYXml9D1-U5tkIxxNC6WOhmKPpYXxUe0xrI-_dwJ1PXRj0sO2geRr6GzOimvncx_-DvhXnM22f3YYl-Z4S4708C5nDb3PsZQ-HsXGoAAppgnpwUAA0hkzgHVUULrmMlY68CBUANdyD8Sx6Swj7c6mzvCIfUhgehUgXsxfLCJqceSVBBZ4kTUEJJbY8ZzCsaz36jGTM4fqRDjI_2Xn6t_CwBS_lu6G2au9yMH2i4e80ey7Idk-r_y9lOQhw4cvGV0cSy-ZH8RK7BQeYXni8Z0WtHh4-CjgMiglvTZuVNIAYLeqgaZWkjhfcuP5yVl3L2rxaziV7QPzxEL2zMHBx1mZdhj95uPZiHUEqtzrstf34dTILEx_CPNKI3CcK5KM2gVSaR-vpMWG969gEzqJX9rIqg1giyEVQerux9Q4f6NekV_t4xSrrrAru-eRNfbCsmu7Z2z3j1cr0Az7fIJjK44xtvwU53Zr71NFydYwpRqcvntXyJIUCaTcnzEU17dxFXBBY-7kEP_aHiIss5LW29lg4lonqE_-J-psPUYUq2ydFiVib_TpLTf7p-vG-vTCBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12da15f688.mp4?token=KQf-MjTfF6IvpH0-k4E_D4ct3oEBPVsBpYuwuVtLMZRiqOgL8FosI5zqZ2sVeDFtAsRVvy4L2cHVCMaCLauA2D4umYQ09Nqjxvnvy3EqTPJJdYXml9D1-U5tkIxxNC6WOhmKPpYXxUe0xrI-_dwJ1PXRj0sO2geRr6GzOimvncx_-DvhXnM22f3YYl-Z4S4708C5nDb3PsZQ-HsXGoAAppgnpwUAA0hkzgHVUULrmMlY68CBUANdyD8Sx6Swj7c6mzvCIfUhgehUgXsxfLCJqceSVBBZ4kTUEJJbY8ZzCsaz36jGTM4fqRDjI_2Xn6t_CwBS_lu6G2au9yMH2i4e80ey7Idk-r_y9lOQhw4cvGV0cSy-ZH8RK7BQeYXni8Z0WtHh4-CjgMiglvTZuVNIAYLeqgaZWkjhfcuP5yVl3L2rxaziV7QPzxEL2zMHBx1mZdhj95uPZiHUEqtzrstf34dTILEx_CPNKI3CcK5KM2gVSaR-vpMWG969gEzqJX9rIqg1giyEVQerux9Q4f6NekV_t4xSrrrAru-eRNfbCsmu7Z2z3j1cr0Az7fIJjK44xtvwU53Zr71NFydYwpRqcvntXyJIUCaTcnzEU17dxFXBBY-7kEP_aHiIss5LW29lg4lonqE_-J-psPUYUq2ydFiVib_TpLTf7p-vG-vTCBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
لیونل‌مسی ورژن جام‌جهانی ۲۰۱۰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/99004" target="_blank">📅 10:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99003">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
❌
با اعلام کمیته جهانی المپیک، تمام تحریم‌های مرتبط با کشور روسیه لغو شد و این کشور میتواند در مسابقات مختلف نماینده داشته باشد. بزودی فیفا هم معافیت‌های مختلفی برای روس‌ها اعمال خواهد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/99003" target="_blank">📅 10:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99002">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
🚨
🚨
#فوووووری
؛ موج جدید حملات آمریکا به بوشهر و بندرعباس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/99002" target="_blank">📅 10:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99001">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=RedAG_vA55q8DQ43vTva7q68AS0tOLMahFrL3gSowwmUjc8bNa7G6aBllupsFrcNyEYZTGWsvK236DYcLcH1hpqvj-mlGd682vaDmLWyzOzqrQOsy-rZzPluuVKzmbk63OfQwMumGqj154sw8zRpDrSIEPPuZTtkPlD5SiS9HxMNoTZ_WRlJtZgm1c18pTshR3KfeRQSlmWEjlWbY-L59rvIT-5vnymFNWoGKmZt7nj_Ldh0oVZMDLXTVn7OvQ2X_8SRFv4_jmz5yHU56ffXbZkfzARvIn01awhrPZdlxFjMGzwNR7msUP-c1cOksiw18i2LSKHeA7wpaQcW_YZrFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb36066e1d.mp4?token=RedAG_vA55q8DQ43vTva7q68AS0tOLMahFrL3gSowwmUjc8bNa7G6aBllupsFrcNyEYZTGWsvK236DYcLcH1hpqvj-mlGd682vaDmLWyzOzqrQOsy-rZzPluuVKzmbk63OfQwMumGqj154sw8zRpDrSIEPPuZTtkPlD5SiS9HxMNoTZ_WRlJtZgm1c18pTshR3KfeRQSlmWEjlWbY-L59rvIT-5vnymFNWoGKmZt7nj_Ldh0oVZMDLXTVn7OvQ2X_8SRFv4_jmz5yHU56ffXbZkfzARvIn01awhrPZdlxFjMGzwNR7msUP-c1cOksiw18i2LSKHeA7wpaQcW_YZrFjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇦🇷
دیشب هواداران آرژانتین برای فشاری کردن سرمربی مصر با پرچم اسرائیل تو ورزشگاه بودن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/99001" target="_blank">📅 09:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-99000">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKftlP5n28K7OgrGWpE33Q1uItWlQSktsM-4_wTbL_swLmJOSLJjBefBT5HtpMrRZ_Z-F4ebv7jcKN0FmJK8diOdwymqcToAKECyERn7XGOemyBtOa0UpVabz--KsWxqGa7P8FBOJvIXn5Sd2fkdMHKqLUh25MI7-h8k10Txc3t0btUImmRpAmZk16Ti0Vh-K54rK4OZL12s-fsoHIOQwtNOeiDG2eWmoQ4tI6HGQGPOm4m-2Rq0XMYTP0YDOmkVh0f5yWtBHgOZgDXZSSKIAbADzVU1OpVTU5-DP6aWI6Ui0zzLY9OwQOvdUhyyX2oQ8nwztW-paeoMvizh3h6bIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
🏆
🇪🇸
مایکل‌اولیور انگلیسی داور بازی حساس بلژیک و اسپانیا در ¼نهایی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/99000" target="_blank">📅 09:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98999">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=dybNJmHSIo-usIvDS3FyFwvO87PtNfjV2uRFVVZ2yb2P5jqiSkmvEOvMn-gI68YJlucLHoFORSY7qXc5mCqGiIjj-0i3H3c5FfI4IkK1lL0jWs4__-H3pgR_kjQXgO5AKfdk0HJh4JRIm9WzYAgv9lE5_M41z_0phbZc6_NWmSkAzoE39ALhCzxyj8EM56h9QxEFPS615zFvyoMQWw4DJeLKywFwhcKLWTgN9bd37_k21qwwl-cuNyv_dH8eAqJWBgcJcuqzf814V15iTXVl5W65BsIEyik35XhMdfnTPalX92WduYWzGCjB_l8xvkIIVYUoC0bl945YPN9IXbP4EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ef60ffaa3.mp4?token=dybNJmHSIo-usIvDS3FyFwvO87PtNfjV2uRFVVZ2yb2P5jqiSkmvEOvMn-gI68YJlucLHoFORSY7qXc5mCqGiIjj-0i3H3c5FfI4IkK1lL0jWs4__-H3pgR_kjQXgO5AKfdk0HJh4JRIm9WzYAgv9lE5_M41z_0phbZc6_NWmSkAzoE39ALhCzxyj8EM56h9QxEFPS615zFvyoMQWw4DJeLKywFwhcKLWTgN9bd37_k21qwwl-cuNyv_dH8eAqJWBgcJcuqzf814V15iTXVl5W65BsIEyik35XhMdfnTPalX92WduYWzGCjB_l8xvkIIVYUoC0bl945YPN9IXbP4EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرژانتین به یک چهارم نهایی رسید.
🔥
🇦🇷
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/Futball180TV/98999" target="_blank">📅 09:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98998">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FrVrfz---ERtGINk5LCU0XpVm5J8LCH9i-00Ko7s-MVQvebhHZXJpQmBA95gr04eaTNyZ9OwZGnmFDuwjrcyrq6aoZIL5hBanBz1w4YsGb7rUhsg5EaRKfPWsnsm42Od6gbi3RcztfLuG_5CENR-l1hU8t6u-W7PfzzLyKvmVcdoZF3I74XTxDIl-2ouGgwb3vQExKsDv8XrOBgbPZ4CIynJU-TGqUlv60v2qz71vHF7-SGAQZtHXYT1HfX4Bf1H0MtdrJijnOdLXlucHKiTHigy_cOHhFzu6eON1KpRjv_sy0nutC2D_nbsDOzrd3D1BwQNgEXdN5Qu4AoNapSSDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
| فابریزیو رومانو: قرارداد کانسلو به احتمال ۹۹.۹٪ با بارسلونا نهایی‌خواهد شد. الهلال و بارسلونا بر سر مبلغ به توافق رسیده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/98998" target="_blank">📅 08:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98997">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FGWz82LupgWdwaUdnA--QPH9FWMzXo3D03kwZzzY7te-mp01Z1GJtf8bJnkyy9WXeD8NZd17TIA3j3TuX1Vu0UbEq1AZDmSTEJrdvw_e7xtOOPpWKYvPV6Cb3S0E4kJJ4izgkGxAQp7mkgyJnYjCUxCL9kAFlkS9yIsXf8nftcIL_CMtx2RBWAcr26QDGZdhgROMBVIN_brf-8B3zJuKykJASIN20CZ-y8HWvcefJEwYVjfA1CEm23PKzDX6V-rG6lHhbkKIupo_tOL_7LLblnxZLONQBHBhA8Aey7JyKiW6NCz_oOwL9lh6pHBZegHcVEAFTOqDPdvy8fVGImWNlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
◀️
تو گروه D جام‌جهانی ۲۰۱۴ یکی‌از عجیب‌ترین اتفاقات تاریخ جام‌جهانی رخ داد، جایی که کاستاریکا از گروهی که ایتالیا، انگلیس و اروگوئه ۳ قهرمان جام‌جهانی توش بودن صدرنشین صعود کرد و تا مرحله یک چهارم نهایی اون جام‌جهانی هم تونست بالا بیاد.
👏
🔹
جالبه بدونید سایت‌های شرط‌بندی شانس صعود کاستاریکا رو 6٪ پیش‌بینی کرده بودن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98997" target="_blank">📅 08:17 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98996">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=cu5X-5Z-30LLmWcrtLAiNXoJHnVeF842OohUzR9_FHEdbtsDZ9PI15yslbRRMBmvRGpJcFziWZKRfirK0DE3mXaXcRnAv_o0HD3bj8mKLZmTFyws2QRAKJeObBST5wQBvvOCMIPTGTTh4ZoMgWZOBcrO3z8C4fbGvWYBQ94L3mgJGlTs3TFTr41jzC4ll5Rd1RBgR3dIgnEwGA_uxn_ja8eLza_VU2rnLkenMUsYLJ7y-1VbcmftqK3k8NevEdRVzUnbSir2DU04KeAiBZL0_deNKaGv4mp5q0fV1dHUFOSZE3XWUm5d5w7il01_ZV7_gVOQBTjNc7TqQ0Unpjp_hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/805dd3bff7.mp4?token=cu5X-5Z-30LLmWcrtLAiNXoJHnVeF842OohUzR9_FHEdbtsDZ9PI15yslbRRMBmvRGpJcFziWZKRfirK0DE3mXaXcRnAv_o0HD3bj8mKLZmTFyws2QRAKJeObBST5wQBvvOCMIPTGTTh4ZoMgWZOBcrO3z8C4fbGvWYBQ94L3mgJGlTs3TFTr41jzC4ll5Rd1RBgR3dIgnEwGA_uxn_ja8eLza_VU2rnLkenMUsYLJ7y-1VbcmftqK3k8NevEdRVzUnbSir2DU04KeAiBZL0_deNKaGv4mp5q0fV1dHUFOSZE3XWUm5d5w7il01_ZV7_gVOQBTjNc7TqQ0Unpjp_hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
برای خیلی از پسرها، فوتبال فقط یک بازی ساده با توپ نیست بلکه پناهگاهی است برای فرار از شلوغی‌های زندگی، جایی برای نفس کشیدن و رها شدن از فشارهای روزمره و فرار از دغدغه‌هایی که شاید هیچ‌وقت درباره‌شان حرف نزنند. وقتی بازی شروع می‌شود، برای دقایقی تمام نگرانی‌ها، استرس‌ها و خستگی‌ها رنگ می‌بازند و فقط یک چیز اهمیت دارد، عشق به فوتبال و تیم مورد علاقه.
🔺
فوتبال به آن‌ها یاد می‌دهد بعد از هر شکست دوباره بلند شوند، امیدشان را از دست ندهند و تا آخرین لحظه بجنگند. و در این میان لیونل مسی برای میلیون ها نفر از مردم دنیا شاید بزرگترین تراپیست دنیا باشد. برای خیلی‌ها، تماشای بازی مسی فقط تماشای ساده فوتبال نیست‌ ، تجربه‌ی آرامشی است که در کمتر چیزی می‌توان آن را پیدا کرد.
لذت ببرید از سالهای آخر بازی مسی
🩵
🥂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/98996" target="_blank">📅 05:23 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98995">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=O2WkL_IJoQp68CqbcfoVCCtOFSpMNsAcTIsnQXTNbGNLyvhcTG788IEgidHjgzVSPJxtE4ZvpM4lUYVZi4OHzQl-Yh4uPUkF4TP9Hg2LX6VNbc_YO0tH58T1NGoyv7f8qpMscvIaJG4mEBvxvUdNgZHTjwDvJwPUBDdiNSR_exk4TRelmZQwwR46JUxJMSciy9SWqFEauIZc-tFAPoJm-15qYueIxGJ2piJKPXRbgwRUY1oUuCD7HD9OhtnljgMJEICviVuSaNh_aAQGZ5slHRvfPGorFA0OlDHpNqAeo-ZAH5ASQpzI86l5z2HYq-48OqL-ddmBgl5p--_C3g9DtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0d112899bf.mp4?token=O2WkL_IJoQp68CqbcfoVCCtOFSpMNsAcTIsnQXTNbGNLyvhcTG788IEgidHjgzVSPJxtE4ZvpM4lUYVZi4OHzQl-Yh4uPUkF4TP9Hg2LX6VNbc_YO0tH58T1NGoyv7f8qpMscvIaJG4mEBvxvUdNgZHTjwDvJwPUBDdiNSR_exk4TRelmZQwwR46JUxJMSciy9SWqFEauIZc-tFAPoJm-15qYueIxGJ2piJKPXRbgwRUY1oUuCD7HD9OhtnljgMJEICviVuSaNh_aAQGZ5slHRvfPGorFA0OlDHpNqAeo-ZAH5ASQpzI86l5z2HYq-48OqL-ddmBgl5p--_C3g9DtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
‼️
12 سال پیش در چنین روزی تو جام‌جهانی ٢٠١۴ یکی از تحقیرآمیزترین نتیجه‌های تاریخ جام‌جهانی فوتبال رقم خورد؛ آلمان ٧-١ برزیل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98995" target="_blank">📅 05:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98994">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgS5o8vd-cxGAAKPZ1ZKSNfJ_ttjGoqBBGNIR9D1lpNQBlDlhO_5UrlJsIoMz9nHkTEJ6BuuOQ_pikr3npoTDeQozZLNNZmrDcGRPwBUoCieKaNT_h-GA8QbFxwmJyqUu1Iri-bowHhPaJ3wWWe87mG1r6Ie9X9lEZd7o76MCXIdyVQ4aicl7YrV4qc35l9TIfMBUi6czPvJwMYfxVSvx7_XHYQrw2svZVg8ZS_3Eu99nsh607m0QOHCEnhogU4WzP55bnOIx-zJ0l1W-ypOd87gpSbu0bi1M_74DTl5M6zNKjCHWY6jpPsMcQbqUPYcf9rmMH7udE6U6-Goko9SYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🎙
💥
لیونل مسی:
«من گریه کردم، چون احساس کردم که هم‌تیمی‌هایم را به خاطر پنالتی که خراب کردم ناامید کردم. اما خدا برای من یک اتفاق ویژه دیگر در پایان این بازی در نظر داشت. من خیلی خیلی خوشحالم.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/Futball180TV/98994" target="_blank">📅 04:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98993">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/Futball180TV/98993" target="_blank">📅 02:39 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98992">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGYtEVtjIw7KamyuSzVt-HN1M2wxKl8Mx4QwmYc3OumLR_QpjS-xEgHx_4r6WWF9DI7TE0B24_PbLVTlcQ8kWhQ5UkUYtdE7nh21H83iGpvToc3EZl8reweixbNH48CGoAcS5LjNFGYvcr8BO2FP-nb0UVt9oLdJDdgiXzlsE4C_IlFiCsq2pVH39xdWDKat1zhr7mZAHdlg_6v9mPJ7DYfOdk4JWPTtmDjT9s7CddebXDFsuj5xbXlYO3dQb1W1Bs9XtPDXFk1_n5o-QHvMxKxSIQkl3AHHqqSFOhbXjYlGnBXIR-beIeydAo1sPWTivqsMCE7pkt3ISUmjoGfN5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
🏆
بهترین گلزنان جام‌جهانی تا پایان دور‌ ⅛
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/Futball180TV/98992" target="_blank">📅 02:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98991">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZG2HVGEy0U6iiRJJqvdzTxm72hBfssFzaGJ8UWCMivJNHm0ueT52HOg68ixu7POObYUEQytj1Ngcx7Zym-tZOY8hLltswV3DIHhOjO2bOtlGxusP8nrC93lcEDRlPz_Vgj7d1NPmdX33kvo3pErrmHq1EMFJ1-hAq3WlY--M5zIWUhDahopxAbjjuQX2q8HqvZo31qP1tshklfmk2H8_matTgl1fOEMpy4Zp5qKR16Bb8Had_dvQsUhbiceKfDYaramaC0L5rqXm0untk7QZdaAn9Kq6RiEVNoHNr6u73YP3wy5ZOwDQJgaZSCsKIZihxXgTLWGtv0HnUoLuAyztg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#رسمیییییی
؛ اسطوره آربلوا سرمربی تیم فوتبال فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/Futball180TV/98991" target="_blank">📅 02:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98989">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LTcjK1zvPUZObWzZ1bCW7poGLzTatddPABvGcuM_Z6gpW6oytaK77YalZ8DEcwrf-bPG4I6pDloJLRgVecqmAG7TCopUGIBk4PNYLMa1JU-Vb_YFhk4eobMHW7EmGegEDKEcHR-VRS1W1oBCpb-7NMgzABjf49NG0v8VRAk1b0NNhhC6ssV6t9MmukmEtcIThYraBaQBlYV9d_BH12NZV0r6PszqR_OEdgfvakHqLrpYEzoneU3tJPG8fUzhErkoVO32r_cjk4UYOA4IhUab5Fpz4fJb_i1ALdCv8Jt-UsFyYUsC7u3EKsRaoWfHrk4nSth4F78S9iK_ULjUK3DPrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه کامل مرحله ¼نهایی جام‌جهانی
🇫🇷
فرانسه
🆚
مراکش
🇲🇦
🗓
پنجشنبه ۱۸ تیر ساعت 23:30
🇪🇸
اسپانیا
🆚
بلژیک
🇧🇪
🗓
جمعه ۱۹ تیر ساعت 22:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
نروژ
🇳🇴
🗓
يکشنبه ۲۱ تیر ساعت 00:30 بامداد
🇦🇷
آرژانتین
🆚
سوئیس
🇨🇭
🗓
يکشنبه 21 تیر ساعت 04:30 بامداد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/Futball180TV/98989" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98988">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCltEq2Vf8qYEngg21hlK8WvgOwUFbkc5ITUExf4OoLNB6GYWFFyoBGly9zJKBRl9QMB0KAnS1C5--N1cxCaaPJ6Z0H2IWFYdgRbYW533mpjCi3TSsl9HYkCaQThBPrnrM-Iwax-I_W3bMkSuZIs6Pu1CDdiwA437S48rtjv_uXWxmDUjvosUCOAr5EY2M3-FMgiTw59FbwE4MTpQdfvb1-050yqH_YTPTpMDOG46iooEbiIqBf52OHQNIsGUBRNg9_JLrlPjOuff3dyLtV5c3rUKMgq5_9Wz1ihjCg0PTLcvdMtg2noHdBa0cCAaN9BuRntR28tWXj1rQUcQvzGpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🏆
تیم‌ملی سوئیس با برتری مقابل کلمبیا در ضربات پنالتی راهی مرحله بعد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/98988" target="_blank">📅 02:21 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98987">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/Futball180TV/98987" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98986">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">گلگلگلگلگگلگلگل و تمامممممممممم</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/98986" target="_blank">📅 02:20 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98985">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سوئیس بزنه صعود میکنه</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/98985" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98984">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromجام جهانی 2026 | فوتبال 180(𝐄𝐬𝐦𝐚𝐢𝐥)</strong></div>
<div class="tg-text">🚨
▶️
🏆
زنده از ضربات پنالتی(بروز میشه)
🇨🇴
✔️
❌
✔️
❌
✔️
🇨🇭
✔️
✔️
❌
✔️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.37K · <a href="https://t.me/Futball180TV/98984" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98983">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گلگلگلگگللگ</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/98983" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98982">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">لوئیز  دیاززز اومد</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/Futball180TV/98982" target="_blank">📅 02:19 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
