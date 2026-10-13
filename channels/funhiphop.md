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
<img src="https://cdn4.telesco.pe/file/YCYF6kahegkRptXgtw0mdFGZx3gwxwrDy6DPdFJFZLR-RJPN3_9nYncmuLf6mdmqnc-7neShtQT9BdnNpePFoBzggWROH6IZ7XVe8aGOjJlFoU3jVd7bPB9pE-BQIZYVXHWRw-2CfodRl5JPGwa5b9pNsa4ncegA3_GMO4wgWxj1HP3s3EAK5BurS7AxyYBc1btEYlxIi-f5rUhr2mosbtXFpAznzcPpJHpizHAK2hpDHhn6iGnGoJt1AGR4vHJye8ZC3YkhWrTsmVeP98ELnmDYXSAOMXNq2TxXKUhOPcJZ6ttTpyO9a6L0kBucPo4M2htAfxAspUUWv8OlmLXm4A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 269K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 02:50:38</div>
<hr>

<div class="tg-post" id="msg-84812">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">شمام خوان گارسیا رو میبینید یاد نویر میفتید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/funhiphop/84812" target="_blank">📅 01:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84811">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5ukte5C8ShDcp8X4gWRCpX30aRu1gXM_Tk0YgKm6GmlDPlN1EHLledWMQo_aP-vxIX650JMDEMLqsn_Xrvz8jRKkOeBa8iGBQU1TJ-9jYV39jWpJ2LwCmPC13geZ5CADky0a8NbVower0Kgu7t0PUjq3Bz9ZXE6fNHjjuj6Fjs3BSlUlCvuX3mJxYP9DEAbQRUqdg7V8kWsSb8F4xUzbA83KX1klU5vPDvFJSjtP6ATrCVlwfF6rdNTGP8EgyCSH2owcssu6yjjEWN2HGZbTDc8Zm9CR9Vn-Vau7wxkwZpbIBDp0w8Nz96qvus1EzCOIvUU7_q0TuIN8hQr58XpFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هی بگید منچستر قرمز نیست و آبیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/funhiphop/84811" target="_blank">📅 01:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">آمریکا اسرائیل و ایران، هر سه تاشون براوردشون اینه که میخوان غافلگیر شن و هر سه تاشون منتظرن اون یکی اول بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/funhiphop/84810" target="_blank">📅 01:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84809">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65b19bec2.mp4?token=JhSWfSyMfIVmGrxvq_ZtQ7AIQo2ipUNPTYo1ZFc0nexfPaKrLI3AdLTVRn2rsSjJQ9UIsC6J5AjmtNFnWxssk9YCQ4ZWCA2sNxrYE2Feg0XpdGIVXxLtCcK-ZnkVMGT7jSNlkIT4KqpyzzjepJDu3k0rDC8araIezojQQPHi1yw2LA_eUJGsJPJ-UZ77Dz_PFu25r-3NzImkqJpjb9jd3QspH5h9NSEKL2wGMeBWS1swsrJeDdVzpM7WNjax23ih6ytrdENZQIX7PgtjwBNpGozKPwko0qakg0DT_s9mG3m_FjsEASNhjkqjNXe1qMuxGtMxqDuo9EZ3pv5828ba4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65b19bec2.mp4?token=JhSWfSyMfIVmGrxvq_ZtQ7AIQo2ipUNPTYo1ZFc0nexfPaKrLI3AdLTVRn2rsSjJQ9UIsC6J5AjmtNFnWxssk9YCQ4ZWCA2sNxrYE2Feg0XpdGIVXxLtCcK-ZnkVMGT7jSNlkIT4KqpyzzjepJDu3k0rDC8araIezojQQPHi1yw2LA_eUJGsJPJ-UZ77Dz_PFu25r-3NzImkqJpjb9jd3QspH5h9NSEKL2wGMeBWS1swsrJeDdVzpM7WNjax23ih6ytrdENZQIX7PgtjwBNpGozKPwko0qakg0DT_s9mG3m_FjsEASNhjkqjNXe1qMuxGtMxqDuo9EZ3pv5828ba4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا پر تناقضه این ویدیو، شاهی و بیگ شگی و محسن ای‌وی‌ایکس انگار از سه تا دنیای متفاوت ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/funhiphop/84809" target="_blank">📅 00:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84808">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بارسای هانسی فلیک واقعا بهترین تیم تاریخه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/84808" target="_blank">📅 00:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84807">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یامال یه سانتر کرد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/84807" target="_blank">📅 23:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTyzDeExR96PIS3saNAMaRTuC4T8hDo6RV4BaW2A6j6yUC9ncno-1Y-u1ZpWv-ISw8xMo-bLvZZ3XOLI4lhkYMX174OZKtOHs-UMaw_P190VPJj_z-F8um14D9AQIHhvPxoCtJ52gNVQzTVTwiQM5wfzMn7IDTikvUN90i06BvX6fgy2CM5mSxt6yfQgetMqdESbg0Eq_JXt3QiwSCP03jVZxSlK4RMIv08c5j37INnpnIAu4SRpiG3XITWSuql92m6cH-q9fQ6Ipijr6m9AOGvIWn6QT5O5iFr08uwNzIoRJefysB2nw4wnc3_goY-6fKBY-7PKhQSwRmdNfYVX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل نکن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/84806" target="_blank">📅 23:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8tJ-pLBy4Oapjxl8J_2_l6opcfbfl_zGRZyp2lbpXfl372QYbZSYlzcAkVRJ8NaoNF7HY-IV3_hwNa_DZ8jxBGJW-r3yaScGM7ZisRdBdj_-c0tzugY7rh5U0oiOguCr-7GzJvvfJAA9zxZGVd5aT6jzqlqJqnF-eXwWsW7awaQpkTSDO85CMNGJWjuonmGZ2fLx0laZGegNPaT3XAR74L6oFo-J5Jc2GubHGWFNy5BWMvX4_ncbJ7soW2C7PBhENIRuNFUMe7wPNKoxnhI-UWgmqxMf843ARq_7ijHsOovzBtaI6KUTuyy77BNWYULgyB4sKvt9qdf20DSl1pLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvr-RtfLc7MgkK3ss36oKhPze_EvP9YpRGzD4CNb6pCxIlV2vL9VckNuxuHoJJMPP_vAqNtAoUtjHxK7XmCIIG1Y0PoJyaO02LUgZ_tTTWVEjCJlNRz_rXZiyE2KF7OWkO8XqzgQjhp76F9ND_7pFzyoOvp0UhXHTeV8yWCo4DlUaGmrgERTxKKPYkrAry3486cCkcVX3ayuldV1XPMFNxJfLYS9yDuezROBr6av8r95Jy8XvaW504CHyXvlB38n3rL1P22Fsi3cs3KGXWPu-lS_EsYG56uXGmwEQ1A0XlN-WA2o22P-GIvNTypk1u_mSsprWlHS2zfkcfBV3Nb1Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی ترب دارن دم و دستگاه لوازمات جنسی مثل دیلدو و واژن مصنوعی و بات پلاگ رو میفروشن.
حتی صندلی و ابزار شکنجه ام موجوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84798" target="_blank">📅 22:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=Ra60EUfz-4QwfW0pPSxMZEOUtmQ0lhYEe7amij4P2-HFJf9OvOZAO-n1qHjCuBmpooXHo1UL2qwi-gqqBIkGDBoQ6Iz2vNe3y7YSF_DcfzxIekA10Q_b4r3VIWDyPOfyTX2MEszpIkXgpLcGFQnrxwWNSoB3__-t8Uy2g1phsDjaj8Tuq3C23uziR_ZpJeXn1yhz3LSPM8O3daDO53_QB9jG_dptVTP5wyJzJsGCAOm0okIGixwpfdI4K5qP5ZiT5czcQnRY8lVcros6-v-ELCu-xpo_CW_IoYclPdHyUOa2JahPh6pPJbg1xa815rS3ptn2VFCvbgml5v5y4CAIVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=Ra60EUfz-4QwfW0pPSxMZEOUtmQ0lhYEe7amij4P2-HFJf9OvOZAO-n1qHjCuBmpooXHo1UL2qwi-gqqBIkGDBoQ6Iz2vNe3y7YSF_DcfzxIekA10Q_b4r3VIWDyPOfyTX2MEszpIkXgpLcGFQnrxwWNSoB3__-t8Uy2g1phsDjaj8Tuq3C23uziR_ZpJeXn1yhz3LSPM8O3daDO53_QB9jG_dptVTP5wyJzJsGCAOm0okIGixwpfdI4K5qP5ZiT5czcQnRY8lVcros6-v-ELCu-xpo_CW_IoYclPdHyUOa2JahPh6pPJbg1xa815rS3ptn2VFCvbgml5v5y4CAIVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین تی ام واسه خودش و دوست دخترش ۱۸ پرومکس خریده
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/84797" target="_blank">📅 22:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/StxQQa5ezODoqZroeAKtK-oXcf9pQykmhgMb6vvEfPeFZcadTUVUVbR6swHPXcKz_NnjkAA1gA4qRDjtn0TO66CTVWKFndeolyaOa1dpvjmfi0-nLDm92MdxLoN7UU4wEZpZ7b21vq9pNOMXT735jv9vW3LuP7Ti-kKLMuCdBTO1exKg_Wvyw4omvUY-_or1ipbBfHPP1SekdBEJ4Uj1dZaXgOvQq4WmCIU1VEhVHTV2dizBU7IEiVdHhbPq9bL7ZzpiU1fUgAGj545Dnn9Mv3n5M3h6K8zXbz7awjXpBsJkSX1PND4IO2BHYHreBA2bkxotbVSkHdosK9D7JrhZCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار همجنسگرای شهر مونشن‌گلادباخ المان با یک مرد ایرانی به اسم سیروس دبیر
ازدواج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84796" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">The Memory</div>
  <div class="tg-doc-extra">Creator (ft Alidanesh & Sahar)</div>
</div>
<a href="https://t.me/funhiphop/84795" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84795" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp9iFEiAAIePekaxu6Z58r3hQGTuwMt_YMkOCCC2lmfsP8_K7zBg7r62vkzkfLpvlythfNLm7Pul5qfSAW3KxkYfref4HEpzX-6qMZX1kCZvdT4FgJM_iAijYeoW3V87ytlK5zW3npQ8RQLFXwBJfaSclA7ypPeS22cFE8QyvjFTuCSCHTrPp1pfnpEKuu2OgPU6uS_iktvQvdVUPaTtNnefeZT9P5zhqND_3enp3cLTWOaG-yOCNgDDMq1GvHJjGdRqM3JI_lrLsbN8mqSuQXtvFVDdR91UaKgvI2SC4SF4VJpjiSy6G_dfDZuyxHZBiMqhEQbOE_gEkcvDs5xcdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/84794" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=KURysiTUVSI9VP0Ha5QEPzmFXakd8zWpPBA0tXP__lBoMxjPKszvfZ7ovScGs0zh2Pe_usCP7NQb42i4GzGOnbf2AYRBH_D99hpe-qeEJHvaDgi4nn2xYEm2J-XAGTUEFmLyY7bd_65ckW-0lfPejzB-OubA-gzGjdH0IInwl9nA4M9oAhWXwES8igxxEgjQKySGuDSvyVGUJzJD9mNOLryruLL7cFZThoZWaiadw_H8QJw62ztxIFg7MiOb4E-ttcXSbvRxiOhsw2gggyIk7h_EyhxqUHp4p-5nLWUCG0FLxydalZswAO9_7On_Qp7S40e96v0jN_qQjW3hn1G52w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=KURysiTUVSI9VP0Ha5QEPzmFXakd8zWpPBA0tXP__lBoMxjPKszvfZ7ovScGs0zh2Pe_usCP7NQb42i4GzGOnbf2AYRBH_D99hpe-qeEJHvaDgi4nn2xYEm2J-XAGTUEFmLyY7bd_65ckW-0lfPejzB-OubA-gzGjdH0IInwl9nA4M9oAhWXwES8igxxEgjQKySGuDSvyVGUJzJD9mNOLryruLL7cFZThoZWaiadw_H8QJw62ztxIFg7MiOb4E-ttcXSbvRxiOhsw2gggyIk7h_EyhxqUHp4p-5nLWUCG0FLxydalZswAO9_7On_Qp7S40e96v0jN_qQjW3hn1G52w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84793" target="_blank">📅 20:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84791">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZqF_YmHSAlm6gY3Ksr_zhQZH8QzaquohGKPV-IMef_AjpvTricqP8BdrpszDfa-WQVb_tVsg2z9FODPiuzJmMymCtv2taI2xcAc6FpzbajGnOWt7FVm594ednleYA2UpXtwLs2hwvEEht4BG_RSvQ5BHn9q8HcPu6mza9FAYserAnqImCR179kqSLHXICF5z8MqMWWog6XeI0ROKqfUeMk6UFjVtr3DJcu75quyEu6NFXWIfaqe4oUbForK4ogcvCss6Fu-gvFATi6fATXuPUpQki2ILuR-1BDC4s0va3EMCu637hrpQlJTUOqplT45eMskkLZRsCBM7saKJvL9e_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ZjWUjOpka3a-Iz6mxzcByJBFigoPtsAIh-n7QuijWKFLP7RTuCzI3nYyodpz9coiKMsromBpSdd6PziXWuCwK5Me3xml9atQsz15nNBsqlmbLWZ32thlXEjMavE8LmpQPD_H6Up4WFfZEXrxjSiVNQKW4x3cINA-I-YeHmEbSPYkioM4wCO5ma7RqOMpZgK2F5MKBo5KyzxrCFsHqw-ajv1atMFiwb6-7ItCtvzXtnbbD4qNYEea89uKFvVbvc1CmtuoNra5jMltZwmsl-qSfn0S05UfiJyvv8ExWCV3uDAzAj4dj_fZktkznlrFChCv1PrVmnwL8X-bvMX10P4vKA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بررسی تخصصی و کامل معنی “سیکتیر”
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/84791" target="_blank">📅 20:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84789">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQLMFcCshk-uQee0DO7am1hK7ENVElQBOl8ytz62Cz2qPVDDXjLwajYioXSmAb59it9v60MyecM88YgwD3DDVFvX-ZvAM_I-zwDxuhDBTR0AA6xWnrewfK3BViD-GCJHhNTvsMbhKcFddr_nPx7k5mg49YadJk4qtX0RmpuwPN21dW4Vv6v7zz55e684rAliuwsTs3EKCznvDHKIXbIMtc2YZhhVwjRmjGpJbXFXdXqvH40H6RPKp4OzQWEcaHEQUnYr-wS1h9oiVIMBgN-789wZOUM4mhWmi6X0NwQlp_skLiN3EWiWrsDxLAx4TwEY8W28oJ7Z0RnxiNESExXPbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=vp9zc__6LEZ4nbBN-EbnDn9vPMPDDPsG8_Xo9SLatE99dEbUHF0AW2yg9kUPgq6RZH8zRB6F--1BTk8IkVbj4dBehRJN1Rmf5oqb8MwtUhBUUn9gvV_JWeMfL_swcIyLg5edYqnir4CfFQXZRi5OpLi0u1uNKp3xcSiOTameh32WNycyxoiIumhIU6ZeK4WIw5G0VLj-dG8AAnhSaTsRJgZzlbOhqzNvsuMrU-YS7fjtJ1eNkV1kX-v9YbDdp4Sxfr2iWVheAn7HAl7mpqDZ8ZYXGk3_Laj8hXgHOkfueXNzcXVyvt8Mfb0NKKuF2C_JAUn3kavNyTlpn6wdmZTjFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=vp9zc__6LEZ4nbBN-EbnDn9vPMPDDPsG8_Xo9SLatE99dEbUHF0AW2yg9kUPgq6RZH8zRB6F--1BTk8IkVbj4dBehRJN1Rmf5oqb8MwtUhBUUn9gvV_JWeMfL_swcIyLg5edYqnir4CfFQXZRi5OpLi0u1uNKp3xcSiOTameh32WNycyxoiIumhIU6ZeK4WIw5G0VLj-dG8AAnhSaTsRJgZzlbOhqzNvsuMrU-YS7fjtJ1eNkV1kX-v9YbDdp4Sxfr2iWVheAn7HAl7mpqDZ8ZYXGk3_Laj8hXgHOkfueXNzcXVyvt8Mfb0NKKuF2C_JAUn3kavNyTlpn6wdmZTjFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بعد از اینکه «محمدرضا گلزار» به «رضا عطاران» تیکه انداخت که به خودش نمیرسه تا مردمی جلوه کنه؛ دیشب عطاران با این تیپ توی‌ جشنواره فیلم بوسان کره جنوبی ظاهر شد.
@FunHipHop
| Temsah</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/84789" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84788">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/84788" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84787">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wh_hzfqpxbjEGvr2hnN0x3g72QtxPQZmkEzWFxctWmPAoOu06EGeC_lDYGqC_vjl2uiwhr83w730secnN_t4mrtsU_XoRScjfviap5g8oBg33ib4bWgeE-rVsla7kQAtD8Dur_wckgfeEz0vtPX6gbTwojQsMp42LqogBSFaRnjB7ruXPb74d0B3HYIpflalVAIZ1ZGrRPM8n1782DtMzLg4JaRef4c41yqdtQRaxNqWXYZlpwIAlGJ9Wb9bhXjTsQ0N1_7k_STAb7trgqqaE_iRWlu7zWWeU22FXB7ToQD3HoZ7EgM8aVTs9R0bx7puiqFjOiJIQ1iQZ7pO93NIiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G21
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84787" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84786">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:
بزودی درباره ایران تصمیم بزرگی‌ خواهم گرفت.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/84786" target="_blank">📅 19:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84785">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=fCFPMyTBIqPnJy2aY6uXZtLh2ckp6FNeLqnNXVI81jDNmc7zuEJXplp6namnX_f87BKH59iFeWc4Qq2muxnTd9a0LH-Ocyax3R8YJYm6mOsvrhRMwrql3piG-1sLGVhr0wQd1D7rMiZ9QD840GqVq5GKljh0Wm1a4j4TCqotZgxg3RFuORWKU6HP2Utdr2eA7rpKuquoojtOs0HqDrXgote_YubhnBEDK0em4Kvy2V8OhwoufONOGVFawEIjmhGILEFxEndQIxT7852h81ZGf6-BIhjMr_ImsLaqTAoryrUDxUzQQpy8MIXDRQ9o8UXlMWi7Wh8JjbXGZSctXfF9VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=fCFPMyTBIqPnJy2aY6uXZtLh2ckp6FNeLqnNXVI81jDNmc7zuEJXplp6namnX_f87BKH59iFeWc4Qq2muxnTd9a0LH-Ocyax3R8YJYm6mOsvrhRMwrql3piG-1sLGVhr0wQd1D7rMiZ9QD840GqVq5GKljh0Wm1a4j4TCqotZgxg3RFuORWKU6HP2Utdr2eA7rpKuquoojtOs0HqDrXgote_YubhnBEDK0em4Kvy2V8OhwoufONOGVFawEIjmhGILEFxEndQIxT7852h81ZGf6-BIhjMr_ImsLaqTAoryrUDxUzQQpy8MIXDRQ9o8UXlMWi7Wh8JjbXGZSctXfF9VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه ایرانی‌ها، کرجی هستن ولی خودشون خبر ندارن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84785" target="_blank">📅 18:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84784">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=W4c8Z5BzJ_CDfmicOoaRgSIcumvpbqy4qZhfWyD6WiqAKu9Z5zyVcRzBN-cFot_hd3yFwuBnj2NZ-c5ZAHi6V_PeRpttHFIIu06C-hgwhlLeKZb868YlhaFbrvEaCRV965GdXwWfbeDXQ1LKjiUiQAQPR2OmeBK_cppS_La30YB9vJUPb6N_Xi1Xr5rAdkX3mSkGMezZ5S-01fMtGD2fgh7GZzA7yuWkdthYevYBvcb5tpZKBhgHfa7Wx2ofSA_nBklwX2CY_5hES4t8tSHBvK8Kqd1KxzRZKJc-CyAuS6G2McsQjPlMCiJTQcPt1bBZOAjHVmJtPuYvk812qqIH6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=W4c8Z5BzJ_CDfmicOoaRgSIcumvpbqy4qZhfWyD6WiqAKu9Z5zyVcRzBN-cFot_hd3yFwuBnj2NZ-c5ZAHi6V_PeRpttHFIIu06C-hgwhlLeKZb868YlhaFbrvEaCRV965GdXwWfbeDXQ1LKjiUiQAQPR2OmeBK_cppS_La30YB9vJUPb6N_Xi1Xr5rAdkX3mSkGMezZ5S-01fMtGD2fgh7GZzA7yuWkdthYevYBvcb5tpZKBhgHfa7Wx2ofSA_nBklwX2CY_5hES4t8tSHBvK8Kqd1KxzRZKJc-CyAuS6G2McsQjPlMCiJTQcPt1bBZOAjHVmJtPuYvk812qqIH6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید سحری برا استقلال و یاسر آسانی کار زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84784" target="_blank">📅 17:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84780">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G9sHSnNUF7_hA_SIZs6QUH86RdZHazgbHq2UVIwl05yP6NJBYC1cCVhIfnsp8FQ9eYccAFyWXi6SW9Q1zX3iMw5cG8Lre7Le_QVqJqbz4VupEJ4srGfUdxCPXRcGLYJwjHg7x1KbsJQBHgOseS6vVhrsin4vs7EmM6BD0Asdp9jXeUwUU5qJgKAbfhkUq9UbdoBLNlUprFvyr61JHSBSj61ebrRuPdvv1x60pkDgZ3lyQ0XhBN9YBg-Em5mbbdgwbui0G2SVOf3TmvQkUe2_TTW8BP6PtuZhNc7YN7fVYcGw9pOLywjdBkPCNJpc2nzy1LXuqeQqvn41kr-sY2eVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFIWImMq0nDMUgFL_ZxkMe5PJKx0pRwL7qMdq7_ZUcjzjo_LpJ-qMvXzyhKhdJ7lNOnjH3JKrJ4--Izp1PlPyn2Vcr_IIlICILv8nLzi_2ae7eTC01NH7vLD8Qqnc7YkqWLWAGMC7SJX3VEK4LgcvXtImMmj9XplFy_KeV6CnLNs15AZYYMPi1XjFCbXPcI2haoCtOJ_zfjc9gNyllR8NiQdLYP7T2tdtH2X98EDraN4JKFHITYhb2ESEts1P96hY-E8cUq1O2s3FmkXN0CLRKGOSBLDRWgFPHIenJdPjuKWE9Vjfg1AGzLSpD6GF7bU4o_diw4zT10hbbq-hXDt1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SOx5CB80EiLqQNNFhZ5Ji-vLEN8tgaWFXN_quXd0dSVn1uhkt7TiqJhgZ_KNqiKVvCaAUyv-o57ft6j1nW8SgK2aqhIYC5akNIWAwX5NR_h-mD4nwb0iYXXeD2-ipFtoCOH_J1qOfXEegXYullJNdQU7DiduvEZ5GUi7Id8tUEFwTMVwY7Vr-hQX16WpCtdNiKSSmhPYq8LMv-fTfN7fgVPqT8F70j9pvTyWBi6v5B2iVOutGvhAi8uV0ktMOgtuREsvYmOnUBxtkL5P2PiBludNhoxqzi_maDNHMFjA0MGfYRBmTmXJlixOlBWO_1KavmuzwQp7jtWMyNpK5G0ttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jZ8riJXqgrX99xEb2JALty9HmCi_96DoPoXelwM5AdHFMxEdnA61SM02qFsnbYjQLtwdy78DtYUFHiyHquC7pEtWkYlq1n7bce4F5-shqYwG_LbFfkUT9ZF4n5tIHR10nIfFwSCNh9AU-mO1hdF78TiYDlngbDdSO1SttTSkkLpnkWjj0I4ZIGCd5FHgg0FH8S-MuwfMdwZdcZmPAZCuV5AynTXyg94oooZf2gl9r0Oocm_M5ilUK95nFnDyXOTKfMxvGXASosuge2p31YLskxRZ2BWWwMu7uQ5vnhQNeSNa-TBJVzr7Cu3orMcFhOVgnqx6uaLXkooeVIJ_v7tiqQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه؛
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84780" target="_blank">📅 16:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84779">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=JZj_A6BX7OMrVtdno19ppcIdq38QFXe4HivTG-G_WekIAComJFwI8c9edZMLJ91rwnBNtEG2RBFqrgqgP_pKCUm7hnB1dwheHoGPurtohIADuX43E61oSWbTPTpA_HXT-DqLKY_jFaWInDKB_R0T-NoFDTyRyXU_7a-tUSx41FU9lxvjc2Mm8BZXhPDofouFph424R6Ss9v7HqGHKSZKocuVi5M-FtzdUHHJYGrAjcRi0zqzEs85RLwc_Hjqy8_DVEG1TBravCuNAm-GCasTmCi5u9f5UbUuFBjxWGseUKXAw2KWjTxWkCvE_z7KocBykri_qhdwCDN1LDJHAa1YkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=JZj_A6BX7OMrVtdno19ppcIdq38QFXe4HivTG-G_WekIAComJFwI8c9edZMLJ91rwnBNtEG2RBFqrgqgP_pKCUm7hnB1dwheHoGPurtohIADuX43E61oSWbTPTpA_HXT-DqLKY_jFaWInDKB_R0T-NoFDTyRyXU_7a-tUSx41FU9lxvjc2Mm8BZXhPDofouFph424R6Ss9v7HqGHKSZKocuVi5M-FtzdUHHJYGrAjcRi0zqzEs85RLwc_Hjqy8_DVEG1TBravCuNAm-GCasTmCi5u9f5UbUuFBjxWGseUKXAw2KWjTxWkCvE_z7KocBykri_qhdwCDN1LDJHAa1YkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست یه خانوم از اثار کتک خوردنش و 10 هزار کامنت این شکلی...
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84779" target="_blank">📅 15:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84778">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi</strong></div>
<div class="tg-text">بنظرت لیگ دانش آموزان بلاروس پخش زنده داره؟</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84778" target="_blank">📅 15:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84777">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">مرگ دختر جوان در ژاپن بر اثر سقوط یک زن از طبقه یازدهم
زنی ۲۹ ساله که قصد خودکشی داشت، از طبقه یازدهم یک ساختمان به پایین پرید و روی دختری رهگذر سقوط کرد دختر جوان جان باخت، اما این زن زنده ماند؛ گفته می‌شود این زن به اعدام محکوم خواهد شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84777" target="_blank">📅 14:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84776">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">کل مصاحبه گلزار فقط اونجاش که گفت اینایی که پولدارن ولی مثلا برا مردمی بودن به خودشون نمیرسن و درویشی زندگی میکنن کسخلن
تا خود صبح باهاش موافقم، کصکش پول زندگی خوب داری چته مثل کیرخر زندگی میکنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84776" target="_blank">📅 12:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84775">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=syvbqVqfODQ978MGkzxzQpHtgLAqZyTBgPJVR83xBOuva7eYAvyoUep5uHnTsdxVpEaHOqhly5TSDO1RkJ0_fhrMzBKNP3AK4nwaCuim2Tc0zIRx5G3rJZNw0EQ-9aZ9OmIEV-LbXN7yWBJ_MfyQjlVKejwkI90UboUNtr8HV-JgBju7g6mBNMFK4-rjLvRU6swwWdF_I5pbr9wxDhfWDHJUo10hVQEUsmcdWXHXPQmXB69U2Ox4PxTnS-aYF31uDw8M-wkm6YQAznAW9U4WtaRJYeFsrygq-RrMexkKzXOwOvpptp6mdzEyV-zGHyeDcRD7thM1iaEMTKaHivt6VYDtQJ6g-JIrX7NIgEehNaJYTYa56MiGyQPJwBdIFDrb-1Z6kyO83gNY8tkBfIpmyBzuZMEX4OxYuYn6BDFf4Xw_o9tHSxB9B93QycAPIGg2aA249wWwoVe2oryMy_RVJufvd6xb-A0yIp0fKodnXG4jhNV_J7R7diYNlS_B7e_TuRTseUOwtTHVBGxdBtoilOlwpLBFZRWBRBkY87Ntnjc9FaicPCPMJuTVblZMAX7vDFjTTLP6yfELuv3363_z4Q3bfA9URjt_7r3ScOzBs8wm82MOg_nl6wiuWy7Aev1tpW8OQCrdXur2PvQVRTlRAY-JzEm2-zVjhIXQFveW7qk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=syvbqVqfODQ978MGkzxzQpHtgLAqZyTBgPJVR83xBOuva7eYAvyoUep5uHnTsdxVpEaHOqhly5TSDO1RkJ0_fhrMzBKNP3AK4nwaCuim2Tc0zIRx5G3rJZNw0EQ-9aZ9OmIEV-LbXN7yWBJ_MfyQjlVKejwkI90UboUNtr8HV-JgBju7g6mBNMFK4-rjLvRU6swwWdF_I5pbr9wxDhfWDHJUo10hVQEUsmcdWXHXPQmXB69U2Ox4PxTnS-aYF31uDw8M-wkm6YQAznAW9U4WtaRJYeFsrygq-RrMexkKzXOwOvpptp6mdzEyV-zGHyeDcRD7thM1iaEMTKaHivt6VYDtQJ6g-JIrX7NIgEehNaJYTYa56MiGyQPJwBdIFDrb-1Z6kyO83gNY8tkBfIpmyBzuZMEX4OxYuYn6BDFf4Xw_o9tHSxB9B93QycAPIGg2aA249wWwoVe2oryMy_RVJufvd6xb-A0yIp0fKodnXG4jhNV_J7R7diYNlS_B7e_TuRTseUOwtTHVBGxdBtoilOlwpLBFZRWBRBkY87Ntnjc9FaicPCPMJuTVblZMAX7vDFjTTLP6yfELuv3363_z4Q3bfA9URjt_7r3ScOzBs8wm82MOg_nl6wiuWy7Aev1tpW8OQCrdXur2PvQVRTlRAY-JzEm2-zVjhIXQFveW7qk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فنای گالاتاسرای دیشب جلو هتل بارسا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84775" target="_blank">📅 11:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84774">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یعنی هنوز ایرانی ای وجود داره که فیسبوک استفاده کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84774" target="_blank">📅 11:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84773">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗺𝗶𝗻</strong></div>
<div class="tg-text">ما سیاه پوستیم((((؛
همونایی که…
بغض نمیذاره حرف بزنم
حرف دلته؟
خب حمایت کن سیاه پوستا به حمایت نیاز دارن((((؛</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84773" target="_blank">📅 11:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84772">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">من دقت کردم از وقتی فوتبالیست های خوب دنیا سیاه پوستا شدن برکت از این ورزش رفته، چرا انقدر عمر حرفه ای ورزشتون تو فوتبال کوتاهه شما سیه چرده ها، ملت هنوز با مسی و رونالدویی که تو لیگای پرت دنیا بازی میکنن کری میخونن واسه هم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84772" target="_blank">📅 11:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84771">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=vJ3Eg0sivltrADLb4N141pnRFO73K89pv-eTYraqf0p-G0bEwrvLDjSZEWc3Rg_pQ0GnmD0vq1NLtt6l-jkwf24THPU8WOhBLrt3CcCnCXs-pkUDq0gjymSUlntAKjtZ3rzjogo5D6F1G1GbMkxB7_R-agmTPI8a8qzGfQubBt1uznRtF-L7j3PFs2_1PPdiQ0VijApQtILcVxH8mwnJzbV7PQ5UauZYx3h2fRbevcnO3UGm7rrM9GlrjDLq64EWe-LO_JnTBOHFxT1dF2z0Qwue1xR_KmBxZ0n2EiJKGnDXjGCKP34RLH8VAz6LgPWR0-95Ut71jh_0iBvk5WcTKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=vJ3Eg0sivltrADLb4N141pnRFO73K89pv-eTYraqf0p-G0bEwrvLDjSZEWc3Rg_pQ0GnmD0vq1NLtt6l-jkwf24THPU8WOhBLrt3CcCnCXs-pkUDq0gjymSUlntAKjtZ3rzjogo5D6F1G1GbMkxB7_R-agmTPI8a8qzGfQubBt1uznRtF-L7j3PFs2_1PPdiQ0VijApQtILcVxH8mwnJzbV7PQ5UauZYx3h2fRbevcnO3UGm7rrM9GlrjDLq64EWe-LO_JnTBOHFxT1dF2z0Qwue1xR_KmBxZ0n2EiJKGnDXjGCKP34RLH8VAz6LgPWR0-95Ut71jh_0iBvk5WcTKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شعار موردعلاقه‌ ام «گی‌ها حامی فلسطین هستند!» می‌دانید اگر گی باشید، تو فلسطین چه بلایی سرتان می‌آورند؟ شما را از بالای ساختمان به پایین پرت می‌کنند. شما را به بالای بلندترین ساختمانی که دارند می‌برند . البته ساختمان چندان بلندی هم ندارند ولی از آنجا به پایین پرتتان می‌کنند. با این‌ حال، مدام می‌بینم گی‌ها از فلسطین حمایت می‌کنند!»
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84771" target="_blank">📅 11:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84770">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBgI3aZbFGuwlSB3dD4mHRhyyW54KWdhhT-1TiktvqEHpyHmhvK7dklK425wSajhTUVu2irz7UF0YhyMoh3zAQD-RnqFHHlKll9gO249Jestbk_DmjXJvxfpTLyQ_s1NCB5b908fMQFW7T_YrzO0leYn19QH7MPBcE9EArNKI7wnbRVPdIQ_IPEoXgUOo2HRD-OjjpuJ8dUDllX6EJYT7W6cvcgRyz3r0l6QfQ7nLpZ79PBmBQAYFcL2UArgqABXsYPhFk9T62uNG98BjauPzpb-4TlSA80k4cuS2RDoyF7rwFQa6rBVZZ0et5_2fVxIR9iOk8msFIrZRcll7uQvnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت دیوار پر شده از آگهی فروش سبدهای گل دخترهایی که به مناسبت روز دختر، جعبه گل هدیه گرفته‌اند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84770" target="_blank">📅 10:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84769">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84769" target="_blank">📅 10:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84768">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=XAHXQeib4gfQgPM6OGquyETAOvnPrnEN4wZGIpxiX6lK1L1Ac_D-QFw2vc46OoVssPNKCN6L7XEBt4zBKpKRfMmFpmVAavChUEi74-X0eGJefWnIyF2ih0ui61j4NgZN8lmJ5OTHV3ygmlASMrtpVWfULzRJcxEpmj3agk75F-XJz7y7csZk_ztY6DA_N8QOY2vqa5xMc8ALj4PsYZG72RB0W9sbVXzEtO1nGJ8SfE28waMhDjG93leJyD15jW5XQpcVQfyFBfmpdOhgbpdUfkfHQlcuD-ENMPfSkR0C9cBD4IzGFLDl64BGiWhbLlB2hgefAxmExvKbw3Cc6h9GGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=XAHXQeib4gfQgPM6OGquyETAOvnPrnEN4wZGIpxiX6lK1L1Ac_D-QFw2vc46OoVssPNKCN6L7XEBt4zBKpKRfMmFpmVAavChUEi74-X0eGJefWnIyF2ih0ui61j4NgZN8lmJ5OTHV3ygmlASMrtpVWfULzRJcxEpmj3agk75F-XJz7y7csZk_ztY6DA_N8QOY2vqa5xMc8ALj4PsYZG72RB0W9sbVXzEtO1nGJ8SfE28waMhDjG93leJyD15jW5XQpcVQfyFBfmpdOhgbpdUfkfHQlcuD-ENMPfSkR0C9cBD4IzGFLDl64BGiWhbLlB2hgefAxmExvKbw3Cc6h9GGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل مسی اسرائیلی نباشیم
☝️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84768" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84767">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P5hXEQQTiYbv9DD73xSwijX8TSEk1IYHrygmxlQeUb_zDw0kxSHYUTqMpepRY8ucts6vpyWLSKnZBOfIRwhtOIypuEoAq1zGnlUVMrECw0bolcx1k73vUIqC9gyU5andipASrjrs01MIcrLyvAsx87IGrXQ69yMhq8gQo7YwaLq1mwzt4933LLtpCrOfsyIylTfS7fau-yghlHo7nGejci963ybff7F1_MeZPzYgLlWQp75Q2uSuajDS1-KxdHSXbN5DcVFYleaOpA6FXuQX2vRuI4rLoiLU71p4Sxx_GzzRzJ_j4UVlp-ON0nvSq_tZZAtBPqkdwnVgJ962rnFo3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r21
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84767" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84766">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=ZfucsC2PCIjvRPaUnTTkaMOwfxFXBSfHmp3Aloycteb76kHyZM7CxNvElS9WtYIPzVnRL5_Mr5M-Vzktw64UJNnhdInWr05dXWV9MdRaa9jdyfSY7o-mQwqdKjRWzmxQZwdqevCvPWL-9hkouHhJggR5vG7z6-Q_5GKzgLwQwbZCzB7XSqEnvBJ-mm0z4kzqx3r9wmyoAlhnztz8qYo6hJoTaqKzVUOAynN7eiXwCAm8HbZTZtijwh4Hl0OXLC8BXeDhnCqrE_4u48Tgb0UBWhKhSOOE3BJuS88uA2GLMcIqEw_LyQ5RObgCeojhOpkqe681cRbL2WVQVRCHrGoPYYbB5AGUn0nfvpLEA-fuHWzpKPHVYloFPR7TZ3pf2djM5f2hSgHOamhuEkzCbjZUqRfHQ5ZnOPCwP6HGMS0O8ZHW_RPT3mXiKYvXhnO7l3moRny-3a_SrBI4ErvKtJPTE9PnItr32LuNV-P2IKFDZZhDuuHHhprLvQRqt-z4a9M0b9-1EJQcJ1S4IUEFTshFRO4Cu6IMa-Zutk8fSYrBSBp6r9mjVB5ogqqYoO27lrdw_ISUOGPzQ0AHjDsRg949waAKN0geuRdAcrM8Kpj_732bcvbVP90IAVNs2i7TVOrrNFLfKBIP7ySbMQEpKqx-p-Bboc5h0QXAM5Pk6hGf3no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=ZfucsC2PCIjvRPaUnTTkaMOwfxFXBSfHmp3Aloycteb76kHyZM7CxNvElS9WtYIPzVnRL5_Mr5M-Vzktw64UJNnhdInWr05dXWV9MdRaa9jdyfSY7o-mQwqdKjRWzmxQZwdqevCvPWL-9hkouHhJggR5vG7z6-Q_5GKzgLwQwbZCzB7XSqEnvBJ-mm0z4kzqx3r9wmyoAlhnztz8qYo6hJoTaqKzVUOAynN7eiXwCAm8HbZTZtijwh4Hl0OXLC8BXeDhnCqrE_4u48Tgb0UBWhKhSOOE3BJuS88uA2GLMcIqEw_LyQ5RObgCeojhOpkqe681cRbL2WVQVRCHrGoPYYbB5AGUn0nfvpLEA-fuHWzpKPHVYloFPR7TZ3pf2djM5f2hSgHOamhuEkzCbjZUqRfHQ5ZnOPCwP6HGMS0O8ZHW_RPT3mXiKYvXhnO7l3moRny-3a_SrBI4ErvKtJPTE9PnItr32LuNV-P2IKFDZZhDuuHHhprLvQRqt-z4a9M0b9-1EJQcJ1S4IUEFTshFRO4Cu6IMa-Zutk8fSYrBSBp6r9mjVB5ogqqYoO27lrdw_ISUOGPzQ0AHjDsRg949waAKN0geuRdAcrM8Kpj_732bcvbVP90IAVNs2i7TVOrrNFLfKBIP7ySbMQEpKqx-p-Bboc5h0QXAM5Pk6hGf3no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه بادیگاردا این یارو رپره میگفتن خلوت کنید آقای بولینه و نمیذاشتن طرف نزدیک بشه، دو هفته مغزمون گاییده نمیشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84766" target="_blank">📅 08:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84764">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=InpkO143sKh19JPcAEEUkzz1_8VrVBvbYAoWFFV_jOCjwb7uupQqZqO5SAIvdY_i70K-3sDdzM2siwdjoHpiSa6_Xr0vg813aKzRQVBgQvvEJmfGoEIAEHPXLIbzb215HnW7b0rnt8dBWrFBmhCDzXBf7CZq4l80wNsJ6x7kIs2lSdP7AZp977sW-HD-SAfy_sckdAXLWRAC8ID6mMgzpvEHtarzJToZCPT7ngEZiIJrBfuzsV0dbybPFyi_htUO8xDQB8WWQ-CXxOLxjRiVMOKbnoJAQpbOMy9q5NYqczhPkMAjxGPRskJ1mAjnD_lo0Uwm_Zg2Dqyd4EUr-Pflwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=InpkO143sKh19JPcAEEUkzz1_8VrVBvbYAoWFFV_jOCjwb7uupQqZqO5SAIvdY_i70K-3sDdzM2siwdjoHpiSa6_Xr0vg813aKzRQVBgQvvEJmfGoEIAEHPXLIbzb215HnW7b0rnt8dBWrFBmhCDzXBf7CZq4l80wNsJ6x7kIs2lSdP7AZp977sW-HD-SAfy_sckdAXLWRAC8ID6mMgzpvEHtarzJToZCPT7ngEZiIJrBfuzsV0dbybPFyi_htUO8xDQB8WWQ-CXxOLxjRiVMOKbnoJAQpbOMy9q5NYqczhPkMAjxGPRskJ1mAjnD_lo0Uwm_Zg2Dqyd4EUr-Pflwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورکا حسابی خایه کردن از بارسلونا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84764" target="_blank">📅 07:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84763">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=L0XnvcI8-xGjrHlg951i_hrGKqTJN9jBCXJCKD9OCbHQ7WmlAkJCjeejUGgFwUGz67Cnq3FyTEXGWIEtWZt2a_WrjNe-jR8NTyewjkvoqX0SptdGEUzt4Z5ft9g0pFNAAsO90nvVwmtcBEVGKs1CGWN1B3iuI339H6hsJ-AZoxTuFhsb95mYYLsbNzlxpRNhP_yrVn8cdXRhMr__b5pG3atKvTEsY-CUJv5cjGYCuGjIcw2HXrZdUe1sQndykcySbfk_c_mTFEhXNgIM1_EZE6o6LeOunFQHugCVwDI14JSjb5gsHVjATqQRYMbkbwaJS1z94Sov7Fporbue5EzmHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=L0XnvcI8-xGjrHlg951i_hrGKqTJN9jBCXJCKD9OCbHQ7WmlAkJCjeejUGgFwUGz67Cnq3FyTEXGWIEtWZt2a_WrjNe-jR8NTyewjkvoqX0SptdGEUzt4Z5ft9g0pFNAAsO90nvVwmtcBEVGKs1CGWN1B3iuI339H6hsJ-AZoxTuFhsb95mYYLsbNzlxpRNhP_yrVn8cdXRhMr__b5pG3atKvTEsY-CUJv5cjGYCuGjIcw2HXrZdUe1sQndykcySbfk_c_mTFEhXNgIM1_EZE6o6LeOunFQHugCVwDI14JSjb5gsHVjATqQRYMbkbwaJS1z94Sov7Fporbue5EzmHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثال عملی سخت کار نکن هوشمندانه کار کن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84763" target="_blank">📅 01:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84762">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT7qK5oHdzexfD7eRJWmgsphzuBx-cT9ctTfYvH8DTuiKiN7hUbgrHPnJFFc6yibu_ja4LkOzNWsvYne31KadK1c_2ss8fVZE3MrrgYk4as0kRk2U_rW7rbI-btL5zXNukIC8j2xfd28e5_fOdyjhR_F1rqcUbwBq_lcWDam0OXr5lDoMC0IfFg1wW1fnVjlBjGh5cyn61hLO5wo3N2JC7gZ_uJ49wnGToMgUhCph-15CKs37vGfIdD8jQKPqJf_8YeurEDlVzZGq03KeX3GfOAgF3Sj-mxmaxVKYPQqqW4JJlOhbEHcwosgfiTfXhM4Ixmtmha9htVXAxuTN8Nmww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84762" target="_blank">📅 00:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84761">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خدابیامرز نقشش تو سریال اینطوری بود که اگه اون لحظه جلو آدم سبز میشد تیکه تیکه اش میکردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84761" target="_blank">📅 00:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84760">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2kmg8GDzO90e0YxrR8qsQZmDlahYGiGOzAfc6ebjCQ0DJtuHcZ2JPjjMtSN7G3ZQCo0TfH72gzVFX6TMWbMPiAisdK1v74XrFzhWO4oy23HjkT-OyfKITIlB4_LAyFeGvGxRicJg4SpGSIHoF2D_uyQCa30MTslQELTk08wosr3ZqNYI1xyUP6hiV8vkn0gGj4_encVKM20oa-9ee_pD00oKFaj8-upbwDAeuEbK3WrcxrmbOb2YGhAn87xjxII05Ickak8hS4lRFSMKo0M658K1lCkm-X-MjlfBII2a1q3Pv9CiB6vzQ8vS7Mzj9wtfFax-Q41w1eeDZ8eecVsPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84760" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84757">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDdzYz79VIzP2uuz4BIlpMsWczz__YsZzW0bKiklug1EEh-1kLOclCXbt-nr_XyflqgPqepusGLuX4nHARXgvHLf4O-ND7ckmRWBT1j8ScVFbTUVgU8OgWt_Kn6QL6DHODNJP1DuM3gVGDQS18ePyE1VAVqihgoOLkvBFvH13skDbLvnPZ6T5kgUXN71Vcekv5lBxdBIX8dgip5wAvEnoPgGcBDI-XsrMST5KHkdY4vgKX0_u8JNbv6_AojTv6JHDQTVktWV5fxZZJr3MHN5mpuiqlRB5MeYx67VHWkbnhslcTaYe7TuBKkley1xJ55BceB90XQrWXfju6dYWWauAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داشتم زیر استرس جون میدادم حاجی</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84757" target="_blank">📅 23:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84756">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swvvBQTvM69L2ymHF93sOTjDSkwAk2D6uFL-iS69jSnN6t80NsZniMOtVKzuKOpOHp8Uv1VXXaLBP4j9no-QyRa_0ML3I69izrMNiFLo268dTMRO2lzMRbvi00VURTfDobyJCGinnstoKfDToQhAwrdfqW0RSkRks-cOxzQGlaDUJ788D_n3ms1j4x69XWbLUTKhdOr3tF6WwlUg-pNfuC518beWBKgD2h-pLC_KrYNEVRCCLr1O5ZJ-M9ntDv7Bem6MoqP3yRv5vGonyUjzd0FzBt4hC28m3PJll6_l-9so5oXsQpTcCytoqjmk-lq0Mtx9bvP0X9iuSertHncXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید فدایی و شاپور و رفیقشون ارین بختیاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84756" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84755">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حبیب کیرتو بخورم</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84755" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84754">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RC56VrKuQRfADaiBNMcYug0vRbKgiaYLWV4PKaXsxQrCKyUwsBZ9lUZD2Bo-x4cbzrTNuPC0K_O9MSprxJLERpptHdij1lbzOnwp0WLgquPBzUjrv9J4pTwz2rdCOtUIfBkN55nMDuAcomesNXbVELj_8HMKdNjiEnh5DnaGdno3pXlqCD7Sb2Z9n9VMDD2BLecy0oZ6Exujdny4nMAVy2Y-G62riU2Vpn_tpmsYdqvVfQud50mofiZ_scvSqPMBZpAPkeqTFu1p1k3HtInmNeCHfLr208KCnrWw89Q8a7rtZTQrCb3Mj8UK7FlsNBtIvFvqmlSp-TMhkleWr6pNUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه رو
😂
😂</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84754" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84751">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">هنوزم نمیتونم درک کنم چرا هلدینگ دو میلیون دلار داد این سعید دالگخیزان رو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84751" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84750">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtfzKPAJD9jgGDY1ddt6cwQ30uSMzy7KMjAwMsXunyeQcPjFnt7nXKGQcZ173vJWUub25R-Lls-mwHhq3ndbBzxuvFxU9Psf2Eifz0ayXUl23WuLxcQ_-6MJGWhYMF-psyfLYXZ5eQvoso8wtkeNJa_CJckPjgfjcXlpCHN_oNNTLZLHDREakZRgQ0IujxmUX5aiynTUr5qMqADxsV_DmmPWWrE-ph3yY2C1whVM9cWl98LCUX091_LgX60pXVYu3EG9GkNswVtD_vhlu3FI3eqOM8ENBsjZRjgY73moywuuv5FzDu5-yNcbOdvTb8xocTzh_setKrJGryBGcVJo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84750" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84749">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84749" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84746">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940390f975.mp4?token=Ed5eLIJhwP_l4c96MsYuLz626PXIwaguDx6-h1w8lEkyllHiYnmLLMsmHk_KSFswo-nY4-6bvTsewwZg1vUfXLg1zrU3iUCCVTukVib02_yv56fEcU8qGr866PYwgc5_yDhnS6qy-W4IBQrKtB1Bw6IWwcvSqOcY7_-rjRh0vo7gQeIgxpbKV8IMkcD1ZxXfbBi1PkLfmfwTtV2RkyGe7mUu6XVy6ROCYgVsM3ECzPwiQL9k7s9Q5b15uPSL-qSfP3vhKD2hwrS5iwXg-vlH7uZE_OBiZv65IAoyU3Jj_wkoXZMER3qpT3tmC7ODUdXnvqAY7DTCXB1LDXNmwjVRdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940390f975.mp4?token=Ed5eLIJhwP_l4c96MsYuLz626PXIwaguDx6-h1w8lEkyllHiYnmLLMsmHk_KSFswo-nY4-6bvTsewwZg1vUfXLg1zrU3iUCCVTukVib02_yv56fEcU8qGr866PYwgc5_yDhnS6qy-W4IBQrKtB1Bw6IWwcvSqOcY7_-rjRh0vo7gQeIgxpbKV8IMkcD1ZxXfbBi1PkLfmfwTtV2RkyGe7mUu6XVy6ROCYgVsM3ECzPwiQL9k7s9Q5b15uPSL-qSfP3vhKD2hwrS5iwXg-vlH7uZE_OBiZv65IAoyU3Jj_wkoXZMER3qpT3tmC7ODUdXnvqAY7DTCXB1LDXNmwjVRdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84746" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84745">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=FIg908R2xixaHGi-2JggZukB-gqMgXyYFJvgRYDl62Wb6MfWng1KfMGMDVLGFz_Gig3AoyVWV4raXlng1Mm8g1nBTBYWHqP40iX_bxYfL2-M6PX8Aod9F9pIMdhhClYbNohcf7C895fG6DOjXOZREhYzy8xBTOSo1AxHu-Al1KNvo9ZG3bfYpBDYy6dN4MYS0SvDuo2kFbU4seIspyiblAn8MYDjv7zB2uppzEjHJX5GAd3nXD_YLT6J4linw2R5mhfFRo5xbkdAphF2MtuQDJecb3jGkk7tcx9CpSMWJbCJGV5FPMUDTBJ4XdcuR9cUXYB7UwbSaGzMrZNOWwqEQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=FIg908R2xixaHGi-2JggZukB-gqMgXyYFJvgRYDl62Wb6MfWng1KfMGMDVLGFz_Gig3AoyVWV4raXlng1Mm8g1nBTBYWHqP40iX_bxYfL2-M6PX8Aod9F9pIMdhhClYbNohcf7C895fG6DOjXOZREhYzy8xBTOSo1AxHu-Al1KNvo9ZG3bfYpBDYy6dN4MYS0SvDuo2kFbU4seIspyiblAn8MYDjv7zB2uppzEjHJX5GAd3nXD_YLT6J4linw2R5mhfFRo5xbkdAphF2MtuQDJecb3jGkk7tcx9CpSMWJbCJGV5FPMUDTBJ4XdcuR9cUXYB7UwbSaGzMrZNOWwqEQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر بخاطر آژیر خط امنیتی (احتمال حمله حوثی ها به ریاض) به تعویق افتاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84745" target="_blank">📅 22:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84744">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بازی پرسپولیس الهلال بخاطر حملات موشکی حوثی های یمن به عربستان لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84744" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84743">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ناموسا آسانی حقش لیگ ایران نیست</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84743" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84740">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">استقلال یه بازیکن داره اسمش احمدی عه، یه بازی قبل دربی رفت سال پیش مصدوم شد، ساپینتو میگفت به دربی میرسه، یسال گذشته هنوز مصدومه</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84740" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84737">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">آسانی نیست استقلال در سطح تیم سالن بچه محلای ما بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84737" target="_blank">📅 22:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84735">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بازی استقلال تو آسیا شروع شد...
گزارش لایو با چاقال اسپورت
🤣
🤣
👇
@Chaghalsport</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84735" target="_blank">📅 21:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84734">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o06x800Am0VIoZCcanNQm4YJiRHEWXTs1J-C-PF_hUdgzJX9IkBxPslDaRYKDgkpeJEispqJXIgNpm4oJxVkjPihXYkvigQpaB6-oHNs0qPiLZa__aAzyMCSGt_s3VelH223KpA7JP5mPW7pZDTIqM9f-FN3ICmB020IKRBkYjxe59pIDXozfg2vgr28QciSrE5U7tknwB7RUswbaLWEOYcltB2jyQxnYcMEGRDE_wV5fSiW3wH44uY0D4PgNzgjmtd7NXICc2F6apoEhs9tjPfcFETw04ogJxNfyRHeWrCN4Y_3DOdbFOa8Yl4i4IrfzCCzzQI3C7dIxpoBRBPGSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پرسپولیس برای بازی امشبش جلو النصر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84734" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84733">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=UCGdogdGcK27x5uCbSLLXqAIp7BMTSPbCP8UVSlcOppqpryCsWguy1nRZEAPUXYif86yRvdt8XuS_KONF0ix7WFXfwaVh5o0pURvtGPVTU2VVezHNvQi4a4Q48tZIqQXWjcdthvRXeOx0x7GTA1Le7KE80OcDNLBtngtZEESXI1_ohZDTjfVmMwHlG6-muQIVDivnwmvEFDYUZnGGh9N5yOD1BFSkfO4ivLQa5NSNZTfHS5cFp8lwE-lAFUVZ4-NaldoKJbisSlb0EeWEqMpUOVe9Xe_Fnb_wzmNHFFBslgL1Ai6HKzIY6daViVHpuiZKOFToabcZQPxOqyBfBiHgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=UCGdogdGcK27x5uCbSLLXqAIp7BMTSPbCP8UVSlcOppqpryCsWguy1nRZEAPUXYif86yRvdt8XuS_KONF0ix7WFXfwaVh5o0pURvtGPVTU2VVezHNvQi4a4Q48tZIqQXWjcdthvRXeOx0x7GTA1Le7KE80OcDNLBtngtZEESXI1_ohZDTjfVmMwHlG6-muQIVDivnwmvEFDYUZnGGh9N5yOD1BFSkfO4ivLQa5NSNZTfHS5cFp8lwE-lAFUVZ4-NaldoKJbisSlb0EeWEqMpUOVe9Xe_Fnb_wzmNHFFBslgL1Ai6HKzIY6daViVHpuiZKOFToabcZQPxOqyBfBiHgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا چیکارش دارید خودش دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84733" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هالند راجب شایعات سقوط منچسترسیتی و جدا شدنش از سیتی: خب اگه سیتی سقوط کنه مسی باید نگران بشه، چون من برم چمپیونشیپ رکورد ۹۲ گل تو یسالش تو خطر میفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84732" target="_blank">📅 20:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ApYR-sPWPJ2r813pZh8W4dnTMK5rbb3W-7JfqjmUNs4OqTC9oN1fF1OZmzSP0QgpXi37BdKcBwF43eSdBXmlLRyetZJGMDv8NI1kELqPBdjfDz3j7FXesWcDrl8fkwnp9vbGrJnNOlQ9se-h3EKBaf_9vcY7CWO7EvgPznlaQ8OkLKmSupmXi5jKxckH68QVAzre_qNDHPyyxvegcakXVrK0fGOJTAcQHSVPIisyWYRocHteFaw--MZG7i6rU-pZZJvNCMJj3RxD4qZnb0YbAPxfK0e6Zqx4cbAHCJDmxp69v5fjRRSMtW2GUAkwcp0KeFg5qcMMJ6k6UsnCTN3Mtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران رتبه ۴۵۹ بهترین شهرای جهان رو با کمال شایستگی کسب کرد‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84731" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=v41MXH4bL1bvcmrT9MnbNJiTl1O7PZqwyw0pPzaw9U5P20f9tjlFgmZVlh6fXoczmUG4chZCcr_XxExTtOPfNZvvbkxyVP7Ym1_82O3QniyK-tXupeVjg5srCUZIJoxPEwGWDLa94asj38Vnfs0hoXZSsMRbEeYebNd_GHX2nbNPyJsLoqd40K4gWjHH4uiAX3XEcvMyGpeey0f4SIwzWwTAGLDqNNri1iN9gKyXwlhHovkdDwO3ODz4wo0HmiNJ_N-WFdl8Fl67OGOPkKrf90r5Bo1DBrd8AHjHhdtJEiJTtV9PxkHYml2wo78zdY_wU9DTjLCGpRAz5tT44vuVpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=v41MXH4bL1bvcmrT9MnbNJiTl1O7PZqwyw0pPzaw9U5P20f9tjlFgmZVlh6fXoczmUG4chZCcr_XxExTtOPfNZvvbkxyVP7Ym1_82O3QniyK-tXupeVjg5srCUZIJoxPEwGWDLa94asj38Vnfs0hoXZSsMRbEeYebNd_GHX2nbNPyJsLoqd40K4gWjHH4uiAX3XEcvMyGpeey0f4SIwzWwTAGLDqNNri1iN9gKyXwlhHovkdDwO3ODz4wo0HmiNJ_N-WFdl8Fl67OGOPkKrf90r5Bo1DBrd8AHjHhdtJEiJTtV9PxkHYml2wo78zdY_wU9DTjLCGpRAz5tT44vuVpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کن برا ۲۵ تومن حقوق مجبور باشی بری تو باغ وحش درس بدی، معلما واقعا بدبختن حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84730" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CTuuCZSx_utRk86Nid1k21VwtJbHbHBlCAj1dwfOfliDiNTrCEEmqMYra3Ym5ndPStW9GNtApDYf2tXGSayArceuZBMXAASgOvZ5SaPvIidgMFGtobCL27wv8slq3YQANVElcR9ZqGH-FigaIWUy-UokidDZdTzBeXM357i8KPS1H-U-JOXOr9IxDf9CFr3x_ILjykMxP4j_v4XDhGDo0BkutxYUEIc8KStsGjzskIwDK5GJtn7NXlAieJ8qShX_NCOzrJvN-NJi8vuyHZ4dbWtOdwXPvi1tQ9az_v51-7cW3rDxS-ItOMIABrH9CQihKTYkzyj8vDnAb-S4PUMjcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84729" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شاهین نجفی میخواد بیاد استانبول، دسترسی بهش راحت تره لطفا با راکت بزنیدش</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84728" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84727">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">نخست‌وزیر بریتانیا: حمله به پایگاه RAF فیرفورد تقریبا به‌طور قطع به دستور سپاه پاسداران انجام شده است.
اندی برنهام اعلام کرد:
«می‌توانم تایید کنم که ارزیابی ما نشان می‌دهد این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریبا به‌طور قطع به دستور سپاه پاسداران انقلاب اسلامی انجام شده است.
ما چنین تهدیدهایی در خاک خود را تحمل نخواهیم کرد. با استفاده جمهوری اسلامی از شبکه‌های مجرمانه مقابله خواهیم کرد و از تمام اختیارات خود برای هدف قرار دادن این شبکه‌ها و منابع مالی آنها استفاده می‌کنیم.
تحریم‌های بیشتری اعمال خواهیم کرد تا توانایی جمهوری اسلامی و سپاه پاسداران برای آسیب رساندن به ما را محدود کنیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/84727" target="_blank">📅 18:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84726">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شین: پرتاب دو موشک بالستیک از یزد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84726" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84724">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PpL-IN3yhsSUQyEbydCyA4l2rmWzrOvGdq_Ux_CDSZOXV6Z2nRbuMUT-g-imqabUcL1PdN-1B2r1FAm22FOKBoGHwkVaLfBkTfTgUTH69uyCVF9jsLExFMvtu4inpM_O_iKDakAygnemOtIFdhf_OUNNL-wtjoVSUMvm99aqdjefdToams2S-Bc0ThPJ7MMiYmF1GjSibjrLUhkwI7SkgX9MUssBvhaN8UqyCTSRkD-ChW_j16GsW6KXWk0MmL_ZdsKJhPGPdjyS_rDWOI1MQBMPBVYMsE1p_4lO515xApVQqZSXCXcHAAOHaAIxj9Profz-yC_LopD5eEQw7A6wqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WaXyRp6O7M173BjjVKSjhR2qB9bFjSGALInna3yqH36cyoXMMDXG2Y82MEDqnTjRwgj0euPPeoRN1ber-u2JhRRMsNw8pLuWFIvVRmlTdEFnVEqGlIDgugYemOiHH1x4Gm8FST2dAINms3CEBnGZm_es1Xfk-rEcBgDRpADDBw2c38LirDFlY9zctvAjTjJlm4MU8htxzkwneereGG__0T8D9-txbRtytG49RannsIHH_qp-oPHtsyiH31y5F0jIV253eiCZPyVdikbsBUvJ7FLiIAyqvIIeGHk-IaItCMRCPg3C8bwt-fZCDDmQsFmPBB5ADPxSWyuCumGDYeCKtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84724" target="_blank">📅 16:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84723">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=s7qayJbl_ePoI8Xar0CdJ9ivstI25I2Szl2P3qBTjJaDNsKH5PrfveGyC6-vvInlzzLRzIF5GY39SaTwgkJDSX5CcH27-1rJVi_JNPmjoo8JhmMMNc7v8vHZtnEPx2FLAhOK9DHV_X1bpqn2IG7H-fcsLky3C5cLzczi4439X93UNq4ytjnbSYATQXWCaSsM3pTdBJMqIzLo-9SU1HEMC8JZVGYcK-kXuIb6tGDUtmqaNyHXP7_Fy1ag2y-cow9GGMloaY_90A4IqERTy9WLff-mPM0py9vCbWkY7JxVi-ibl5cCS5eOWDJXy50pAMBPHCKLLyYr3X_8Su-IXi_7eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=s7qayJbl_ePoI8Xar0CdJ9ivstI25I2Szl2P3qBTjJaDNsKH5PrfveGyC6-vvInlzzLRzIF5GY39SaTwgkJDSX5CcH27-1rJVi_JNPmjoo8JhmMMNc7v8vHZtnEPx2FLAhOK9DHV_X1bpqn2IG7H-fcsLky3C5cLzczi4439X93UNq4ytjnbSYATQXWCaSsM3pTdBJMqIzLo-9SU1HEMC8JZVGYcK-kXuIb6tGDUtmqaNyHXP7_Fy1ag2y-cow9GGMloaY_90A4IqERTy9WLff-mPM0py9vCbWkY7JxVi-ibl5cCS5eOWDJXy50pAMBPHCKLLyYr3X_8Su-IXi_7eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ی نفر تو ارومیه اومده واسه ی مسیر نزدیک اسنپ بگیره بعد اسنپ رفته بخاطر ۱۰۰ هزارتومن یه راننده از ساری فرستاده، راننده و مسافر هر دو پشماشون ریخته:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84723" target="_blank">📅 16:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84722">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bgCluZq_3g-Ep_UzL1XDY9AzHFUmjQqW9Kyn5g5TZZSmTkKnjph5kLWhFjPcSRM0s2LShvw-k0jKqpIcKxWPOktc5IsgPso_qyOKBxbJKyrNddmSg2xUetvsCJSrd0gdzG0MwneNK7PPmjUwf0iprqOvinh3yKRUM8SUrxyPWnqMkr6e26hc0txhmi219lgqc1kfQ82OVgaOKLhTAoi8B-1wl7B2qf18f-CLAwVXuPzv5X9VajvOwTENdF2yztHzwktFEP-nDE3oWaiqRrZoz1jT26Tu12sJEyzECzzSLg8V-FUWyA8pId23L1rP0e3H3vHGPFxs6HNaZKnTvQ5SWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84722" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84721">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=OkbxZ8C2sssMHQ8HBlomXEFjFtrRoXRjz_JkBXv3l3_kgsPUQJt5-WC-ubGjSSmF4UNeuCl6QVmQ3Ks5ORe06moUaLBrTuN5GmgmMVzmpSz6bVpcWn3ePt9ZWdYg_2uroKWPZTW86wIU8TAcvd4he71xFQ-OV20s7TaQ36mcc0JHQHbuTmjsFCxm64C0s9VS2HIIhReeLG_fh_3FiptdQtJjZbddBJRgSdbGjL4vKbuRQVl7DlFCaXd7QFI2_OxDodv-PjFKTaKtG2qaAoOmjE4TEOmvL2H3YPi2PrYsG3FAcR-AdZYP5D5gFbsGWxFD07FCHQdNPYB-CBpV95o5gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=OkbxZ8C2sssMHQ8HBlomXEFjFtrRoXRjz_JkBXv3l3_kgsPUQJt5-WC-ubGjSSmF4UNeuCl6QVmQ3Ks5ORe06moUaLBrTuN5GmgmMVzmpSz6bVpcWn3ePt9ZWdYg_2uroKWPZTW86wIU8TAcvd4he71xFQ-OV20s7TaQ36mcc0JHQHbuTmjsFCxm64C0s9VS2HIIhReeLG_fh_3FiptdQtJjZbddBJRgSdbGjL4vKbuRQVl7DlFCaXd7QFI2_OxDodv-PjFKTaKtG2qaAoOmjE4TEOmvL2H3YPi2PrYsG3FAcR-AdZYP5D5gFbsGWxFD07FCHQdNPYB-CBpV95o5gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین حرفه ای کماندو ها و نوپو تو سنندج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84721" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84720">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84720" target="_blank">📅 12:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84719">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">پزشکیان : داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟ باید برای حل این موضوعات چاره‌ اندیشی کنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84719" target="_blank">📅 11:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84718">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IWJrLGrR7yc0nT-j5PODlGvjMq75HUL07phjfUrJ9qcLevN7o_7SD6ijx-mU8BMEnPjKV8MkyVz4f0ly0fAMWyXcU8SwkRdPk1FB4LStJshW9Y8H6_ArlTXzEBDJDC8QunkZvKf1IjFcYSwgezEFKzuP3UNVajDDlY7KseP9KZW8RIOBhjPobk5BV47gXl52LRW-Ytg_lKNTO9Quq51n9tWDA_M7Wsn9-jdN3SxfU3Hrm0OzU4T5ZykmHcGGtZ_KTdHb9DfVfY_q8BvPiopty74oKlJ9ekYiGV-zH8jvDxurcLpmvHeDlysHzqP8lmgxOSmtHlYVsVgg2I4YW8VUIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84718" target="_blank">📅 11:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=ufMTQukTtMEFw0gd4lJWHMNxj0tlT-YSsDsaKvSJRooOCyoe4TAX23sLzDufa2EQvumCXp1fOssYcnaqCMVYiqbE5ufcUFIdIJAlWQBLY17qIcDy6t45jphVOv5e8VvujL9Gsz25YOW_1sNOfUT1uFMNNbyyTv_NsMOB4mAphDTo1sL78njCNKo26lvTeRfIDdK5HsWPgAXb95StBxIHaPpbru25XnuQMg2RXoELnbG-s74FmY0WKDH1XkjIvmrUYip5_k3L2j_ofpaxTxP7uP9DtGZtYlBipPiPrCc3KyY9Cp1P5e8oxBrAUbVywJKm_GIu_jzyGIocmZCYrmvtEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=ufMTQukTtMEFw0gd4lJWHMNxj0tlT-YSsDsaKvSJRooOCyoe4TAX23sLzDufa2EQvumCXp1fOssYcnaqCMVYiqbE5ufcUFIdIJAlWQBLY17qIcDy6t45jphVOv5e8VvujL9Gsz25YOW_1sNOfUT1uFMNNbyyTv_NsMOB4mAphDTo1sL78njCNKo26lvTeRfIDdK5HsWPgAXb95StBxIHaPpbru25XnuQMg2RXoELnbG-s74FmY0WKDH1XkjIvmrUYip5_k3L2j_ofpaxTxP7uP9DtGZtYlBipPiPrCc3KyY9Cp1P5e8oxBrAUbVywJKm_GIu_jzyGIocmZCYrmvtEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره دختر اومد تو اکسپلورم باورم نمیشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84717" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJTSvvqQX0MWbXmI32iWKHxMA9H9rOYBtQiiOXepUIs6L89hhi6lXG8JjXCmktjlCfKEUeOBRQo2a9ARVxnd22rxW4lc2fr8biVoZhlvAnpPFqCI9mqpXMAquy7P1ljCTwn2fJGIPLt6cRUevATljxRHwy94hCThVB4hBlpiIL9itOD4AYQOrGQxR2kxzO35pTad3B6L8jXhfRvg8KBMx6DRdcny-KSq7QlZcHRX3DVVcY6h-s81Q7yFIPJ3lAfo_AX_PJnrQvGSImHIKhGcdqwp25IxkvzcOI7jFhV_XUrKN4im9xzneEb8-sNaNNZ7AZOI74qG97VjPP6VzxVlog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84715" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=CSNI3oSV9VlyC5gwoKPckODUdfYjEbIz_TlZyB6K_I5yl06zCGZ5_TUzE2Jy1Z-hty7OfkCQiETFDPn1fTgNc9qYvVjlYpOQW0wiLHJNJvfx1GHZZZ-sEThBZ931QtVzhtS2mFwlnFTs-dwnulapvaVgPsegbfs25iVdPHi5AEx2WNbouBUGCAEhvaC2v4jOT2NMa2ACobWvodGkmL9SgDnJe7BMF-bFtj9kYnJ1pQgLZjfVnkTy2ArPrDnEIb5FhNp5-f_giQozJspHV6oFuGKL0vpdEr0IVl-Ix9YzTi8Rea6Kromk4SUwE2VTdoOtCU--XRZlPpFEZ-1lRzhsJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=CSNI3oSV9VlyC5gwoKPckODUdfYjEbIz_TlZyB6K_I5yl06zCGZ5_TUzE2Jy1Z-hty7OfkCQiETFDPn1fTgNc9qYvVjlYpOQW0wiLHJNJvfx1GHZZZ-sEThBZ931QtVzhtS2mFwlnFTs-dwnulapvaVgPsegbfs25iVdPHi5AEx2WNbouBUGCAEhvaC2v4jOT2NMa2ACobWvodGkmL9SgDnJe7BMF-bFtj9kYnJ1pQgLZjfVnkTy2ArPrDnEIb5FhNp5-f_giQozJspHV6oFuGKL0vpdEr0IVl-Ix9YzTi8Rea6Kromk4SUwE2VTdoOtCU--XRZlPpFEZ-1lRzhsJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار دعوای دخترای دهه نودی بخاطر یه پسر
انگار یه دختری به دوست پسر یه دختر خانوم دیگه تو اینستاگرام ریکوئست داده و همین باعث ناراحتیش شده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84714" target="_blank">📅 10:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84710">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">دسسسسسخوش و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/84710" target="_blank">📅 23:31 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84709">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbvQrFWeTrN5Y2Sbc252uXBoJnxgehzxRJAurSOEijyvn2q7xK6bJIRIgNDHyqtwCfxAy2JisB0c5Xpr9QQLk1P5laIG2nCCnin148B-mM1CvxLqCFQE58JdDGQebZ0PbacO3-zUhw_ljZSbEhPjN1rQSIZi4-cKw1OVvvwNHIoOWdPTQcWy15Cff8LxqmcKNc-knhFR-COfusMfO17qOL3JIt0g2KeU4nb2zsssO3kCq3ay_DQv3GbhNxyg4U0PPLBORz-14VdH967RDNRRDlZZ95o9KO2Xi-3NZS7knuE_hMv_n_9TZvJprnGn4nBaqY9BRaEB09aBtL6J2c7znQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان First blood از اینجا اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/funhiphop/84709" target="_blank">📅 23:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84708">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/84708" target="_blank">📅 21:12 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84707">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">تا دیروز هر روز صبح میرفتم سایت چک میکردم بلیط بازی بارسا و گالاتا رو بخرم یه امروز چک نکردم کسکشا تصمیم گرفتن بفروشن و تموم شده</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84707" target="_blank">📅 21:11 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84706">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خاطرات وینی پرایم داره برا ارائوخو زنده میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84706" target="_blank">📅 20:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84705">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوکو خداسسسسسسسسس</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84705" target="_blank">📅 20:26 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84704">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDY9_2LZeKTVgbWcyhjBhBMfP_PCsbmXFQGmX1GlRgKho9Mv_lpZ0uW_1PjpNhF-bFuf1xQYsRQMJoiFx_0XptfI04eH2fe0w1XufBErLLoOlB_kHvkZITi6_nwkDiOL7iFnJTSxxYIcE61bP6JNic7bc_cQcbdo7IrfXinZsPnmyd33xtUnJAdnIel3tiydxwoaVHw03F3pSl7XS8abVYHuwaXexwye-4RJsAo8r4RomICYwyHPPtEhCL4D3p8TinbqceJDcmLRmqmrH1nHJW3Q9-FOtUOatrTWKDJ4mDhDj8j9oBktp3KlaRe3YisHMRwyIUvubox_R8vo7tVfsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه سخنان شگفتی به زبان  می‌رانی، ای مرد؟
❌
چی کصشر میگی کصخل
✅
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84704" target="_blank">📅 20:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84702">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AkJXbFSqOXLDby4Fd6M1favN8thplFrw0RlRv50oArkg9vJyk8V2tqxbBDDkbJfCsBAYMBXLxbkpIvHVfeW2g7wPZ3XoeGN2-v795ccsd13D6Oy8UAnJSKV2osC8fNdPsVcdVMj_uuovKMhxIeyvF1mh4UE0RKa5o2GavlFlUcg46cNsKS_7QfnuSyt8Or02ed3vcUJqJDLMW-ztm9TQTxgyatVYk__pLQIZ53aQe0z-1hVMHGP3DIax2pjL1XxPDPjSG6QmtWxqW6ifdmCyGnO21ZBrL5W21W-cmbMQUZCksd102b5z2CB1uWSNdWJyZZBs4ZoAtbl-MJoE9HZ6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بابلسر ی کافه افتتاح شده که با پستونک به مشتریا نوشیدنی میده :
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84702" target="_blank">📅 19:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84700">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnovMToWAEF9CBECd3HXSj88JqVlepZiDhLbuE1W9XxEUbCvTgvnU2ZvMFfx3lWPCNQmZfpZFDa1T-zqFO6SWz-YgZlSwPK1I-LE2qIhZnkeK9bxww_Hv97oab15AxmWcnpqM-ONbAulC_ofuy-FQjbHEAqJb7sJGYkcDMcZO0u6-zTQ-FmH21rwR9Tm1DXnggQdJHxMCOSCdiyzl2eB2sUiWW3ThBKXf3hJpBO6nJ_6Opq5ntd8OPs4k41cjI7DTGfbvNQw1ZGuzSnZtAT-aGjpNIkjvSWsKh9w37DNmqxX_3mWYPeRpnKB3i6s5_U0KDCYvD8jp8PjDwFqCwpNqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا به طرفدارا لیورپول صبر بده، حضرت ایوب هم نمیتونست همزمان مونیوز و بارکولا رو تحمل کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84700" target="_blank">📅 18:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84699">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cP-_Kocz_flEhPBQKLlvInKk1MfLfJHeoJqr6RaT2wut4aOoROzRKEV1MfWkqsK8i3hCBGC-E7dwJnJZWEeLR_rm8vo7jKRjgMcC46HOQjYjww3kirgRk5Z50a5uEDBU412X45yu8Od95Li6ls6-93eq4neGQ3hhX4b5s9p-brz8lt-UwVIIjnHrlrYvqDp3Kkoknrfjk8UDtkcgSy_6d5W3s8X4LlE9LkBAeTCayerVWeyp9N2cZEwTQ2sPfUvHt8pgI8QsCpIhHsTU2Rq58IGW6Oxi2qg0x4sPX1ikaB91KLBz-7Xj9u91OULJogmACtTlfU0g-P6DVrb0ZfkSnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسیری که گل‌گهر برای رسیدن به بحرین رفته:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84699" target="_blank">📅 16:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84698">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=HLuRZrX3r60l2rEKVJ8jfAXvDtOgcKZoLmwSwzNZyYSMFZ-JDk8MBvIJgg2qV1-B1KecozsmFuNqyP2bfGrxft7WcPzXcqSbpPVKNJ-1R_iHfA9bh-qIPZMcPkTHK4VupRhoM-B-wjyxhiip6hhvi9KMpQakXG-LLddNgkIcwZ4-lUPpp0U1CO8ma6--u8b3Nuee8rDcSPCP_5WqO7wcoK-nSlvW9SrnEq6kDlOLEcU4QWWKPixbTRn2y-05AZJNWj5jZYaFURlpqVlM0IQVyf6EbhKksQlPyzeUz8TzSrjrABTP7yoBnCW6Z5ms1dUr3-pOuO89f0VPlkNH-jc9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dde88b838.mp4?token=HLuRZrX3r60l2rEKVJ8jfAXvDtOgcKZoLmwSwzNZyYSMFZ-JDk8MBvIJgg2qV1-B1KecozsmFuNqyP2bfGrxft7WcPzXcqSbpPVKNJ-1R_iHfA9bh-qIPZMcPkTHK4VupRhoM-B-wjyxhiip6hhvi9KMpQakXG-LLddNgkIcwZ4-lUPpp0U1CO8ma6--u8b3Nuee8rDcSPCP_5WqO7wcoK-nSlvW9SrnEq6kDlOLEcU4QWWKPixbTRn2y-05AZJNWj5jZYaFURlpqVlM0IQVyf6EbhKksQlPyzeUz8TzSrjrABTP7yoBnCW6Z5ms1dUr3-pOuO89f0VPlkNH-jc9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا ابوطالب یک رپرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84698" target="_blank">📅 16:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84697">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دختر خانومای گل، روزتون مبارک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84697" target="_blank">📅 16:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuqtaKsOO_YBJXxbiiuhpgz_Pff9PWPdR4Nymwp5T8mh8jBkZt2aW-Y4hOmli9ofXgmbAPEftt0bYWd7Co9ENORqGR0-9m7ptLHmS1FdVbcJ2t2hGj0pLUJ__qLy4HmhUh1J3T8DBgcPqfOuakO0VK6TYzSloTQg0JPKfnPgEvLk4F7J02rPpQ2mU8AvhPN71YXGAH9LYp99mQzLl9eqxkrVYi2Xxd6XqVshkBMyoWNKq_c41e_2z690BKbHalBxXFHjE2aYOTuOkRR7NJ-EAoNFJLGyzHS8W2r0tQ5-IcUO7k6vGKmC5hwq6h-_5F8eKv4AzaPyumJkWhXdeToiHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گراز پدرته کصکش، حرف دهنتو بفهم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84696" target="_blank">📅 15:44 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJRiI0g0R2D9FNmvUqnSIaDaZV8tIj1IFa-wvz7j5Y4-fhJTZ9VtxSOo6BkDX8KwLBUtvCN3fQTdkb3tB-KRyuc-ioA7IO5rzhtt4uN_Bb8DpMiqWUuAp0hw3nhdLlqAtTIajS6LzxEOUqXrp-DORmDlKTSlY68ujFzYEmf2rpQbOGJ16luNFdPKQbbtXUpnYVxMokhBI9WtkPgg-G8BIICLLD0JZh3b2TyzixasJukho50KSSmZIFrhWSVVSbbmTf81s8iFYi_iSoHbaN1cfv3TgetP5sq3TxoIAYlQJy6cRFQXdlhXV6e4K0PfAaNSIu_-HszEWYxCSUXrf3yw4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم یه سری رفتم موزه همینجوری تابلو راهنما رو با یه شاهکار هنری اشتباه گرفته بودم دیگه نرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84694" target="_blank">📅 14:15 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">زلنسکی:
اوکراین آماده است تا حملات خود به پالایشگاه‌های نفت روسیه را متوقف کند، اگر روسیه نیز حملات خود به زیرساخت‌های انرژی ما را متوقف کند.
پ.ن: این ترامپ لامصب چیه که از یه راست افراطی مخالف مذاکره که کشورشو به کام جنگ با یه ابرقدرت کشونده همچین آدمی ساخته
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84693" target="_blank">📅 14:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=Hdv6hmP70JN_QeIbWTtYi4_pFXqSPdx-lC3KTcbKcxEMlXS9JdFQQg03TXbh5zBnjYWwdfy20_u2DzhZA9er1CsD0HFo-JA_uexQGKmKym0xXstefwgPbg1VVsgEA2rYPgnV3M_FA7W556PWr3UqYUJ33L6EVuNJVonoEUB402-KacUiM6w0xmGVifnhttemOFZfzg4Ih1515hEwZqikvpX-28tkejc7F1Qqh_YQOHo8cjmRm9RpRKphVQB2aJA-WrazvK2oXAjGtd_T0Ua0ITP1kH57GIQJYILNJ8T04lttPTfYjLUeqN7InRpJsb5OD2BolJJdeEaSeVaimjsR0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/548dd7a29a.mp4?token=Hdv6hmP70JN_QeIbWTtYi4_pFXqSPdx-lC3KTcbKcxEMlXS9JdFQQg03TXbh5zBnjYWwdfy20_u2DzhZA9er1CsD0HFo-JA_uexQGKmKym0xXstefwgPbg1VVsgEA2rYPgnV3M_FA7W556PWr3UqYUJ33L6EVuNJVonoEUB402-KacUiM6w0xmGVifnhttemOFZfzg4Ih1515hEwZqikvpX-28tkejc7F1Qqh_YQOHo8cjmRm9RpRKphVQB2aJA-WrazvK2oXAjGtd_T0Ua0ITP1kH57GIQJYILNJ8T04lttPTfYjLUeqN7InRpJsb5OD2BolJJdeEaSeVaimjsR0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنازم یه جوان فلسطینی که کشته شده بود بعد از به صدا درومدن آژیر خطر پاشد فرار کرد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84692" target="_blank">📅 13:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ShHOyf_pC4133dobARfY_ALbHC3P7WHGEwV44nAN_8p8gaTeXKtn_WLmMaTg66LWRqhHpkenELJOxab09tQFAHTj-_1qWlHrX1ZN_DOoW5qgDuKqbWQBLRFrSfDmJopDYFH7DRNqo-08WXRgoaX_ZmsP9dPY0dXgyrdafZWuaHaLVRHb27LWCoe5y53q2NAq-nvN447DfopLXoVfG66V6edZhS7_VgLJmUOwpCjwgwAqFNwHkg6tYi_H7eJ1sbaH76PsoZ_LklB-hxwbLxA8292MBamXzNbEsYhy8oRwdYgAiw7I7VhVkYeUVUeIMb62BIjw6ILhh4s9IiG4ZTolPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگتون بالاست مشتی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84691" target="_blank">📅 11:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qJwv8dimqhqNHPJMCOYt_kIeEoVmYePw7ZQl1AdWKVwuXjaNafniax0QFRjqzCthQthqEfUcBBwCujeXhX9PkLjIrWfUk4Ef2S1fkH_7OAAq2aiA6A0zi3dUEhGEixwtvESo-FJLxOQCnjlwNFhPRvT04sZfKmWkAdxVj-JnyK8BkdNEmZxvKdg9CPcPtJwJ_5ZFnwhql7-6OxH6PxtpX1Wdfv2Rm0fMTuOMXDq3Hm_D4kyQPapqUlEW8sx8kr3f_DC5wUAzSVf5jwKiVWpoB72wu7UwK2qaFHS4ekUVhd1BOIVQtx9d08qs0kpFSCn1Cmc1L5McTy3vFpNCX4HUsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دم هرکی اینو ساخته گرم یه ماه بود از تهه دل نخندیده بودم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84688" target="_blank">📅 01:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfxakGFDzOnpncF6MFNXKaAP8_7ZzHlqs1oxffJqOmMksyCEf_gBg7uNqlIy-3sxuNdmySolFLY5GnnYOog-ZMcYJMWuHo7pX3N60vC2HT_z9UQvm5DMUN5kOtIDIftNqWtDx9A5k5fmGuP58wruiGsP_bev3ljrbR867koP1t5YLjFajUiP3gNZUfRX3Q_A7IgJbk4wygIo6GijBSNVyyKjiVRq0CHhdglCpS7wAjQTWropJqEbfl-mb-mQQY1unoPLVtJ5YBez8k_53oczH8mQBWgxtSyd4X7ULRZAqsLxZEhTD4MW8ksHo7FZW82AXc3BS4VFY4th66DopDNzsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم واس دلت دادا
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/84687" target="_blank">📅 01:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84686">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">داور کسکش فقط به من کارت نداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84686" target="_blank">📅 00:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=ho0mUlmvhLZSVqyXSKb71HXmXjESSBdp_9dlYX4HrWPDXh3J0SEKPvRfq59udm4E50UvDlNi-jUznt3C8cpEjvmeynPudVqVwLbQnvwdIk55N0QfCYr8kNN1We3xCLrtobVwLGH-iUsjA-QdlPh6bxoRG2rviZe3R__1TGwASN_U44L6HfWOcYbWAf8TsI8uI8C9xyGNO3u9mqFK8CGCpYRSOGk0zAKfb_IWh33o7BkHyWq-6gyqU6Z-kFpwInGoSm_nTKnfY4E4lagtCxtlbK2OgT-gd42gCYYnl3WdhkxICnO2CqPc6A_kwtak4dZQOUa96SccwI6iEUKCHZxIsy8yx6UiTc7lPC0WIabNaQK_WMkm_Nkx1HAQvj6peuJG3-4kJdqre1JP9Gxzt_1OA5EXVWah9l_1mwk_sKFVUBzB7IA4hZeLOC6GkjTFBH5s__F7Tl95rYgjMEs1GjZhkkW0makzP-GSTvAQsvORLUItcriJPvNm_sOOwHRnYdiWKWlEkWWxqeJr8SjIzR5xZ5FF82oW-4SBi5gElAv-J417ZsMmKn5t87gpOkrstDOKCZQa3FV5AQWsZ_5ZnDstGF9q35lC3QF7fCwlA5qLAszE0R9VarFpqWNMS3cjmR8_3fq0J61qCqLhGReCgyYP5g_lajwcjH3H8iWlCkD1Qdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b32a1ac263.mp4?token=ho0mUlmvhLZSVqyXSKb71HXmXjESSBdp_9dlYX4HrWPDXh3J0SEKPvRfq59udm4E50UvDlNi-jUznt3C8cpEjvmeynPudVqVwLbQnvwdIk55N0QfCYr8kNN1We3xCLrtobVwLGH-iUsjA-QdlPh6bxoRG2rviZe3R__1TGwASN_U44L6HfWOcYbWAf8TsI8uI8C9xyGNO3u9mqFK8CGCpYRSOGk0zAKfb_IWh33o7BkHyWq-6gyqU6Z-kFpwInGoSm_nTKnfY4E4lagtCxtlbK2OgT-gd42gCYYnl3WdhkxICnO2CqPc6A_kwtak4dZQOUa96SccwI6iEUKCHZxIsy8yx6UiTc7lPC0WIabNaQK_WMkm_Nkx1HAQvj6peuJG3-4kJdqre1JP9Gxzt_1OA5EXVWah9l_1mwk_sKFVUBzB7IA4hZeLOC6GkjTFBH5s__F7Tl95rYgjMEs1GjZhkkW0makzP-GSTvAQsvORLUItcriJPvNm_sOOwHRnYdiWKWlEkWWxqeJr8SjIzR5xZ5FF82oW-4SBi5gElAv-J417ZsMmKn5t87gpOkrstDOKCZQa3FV5AQWsZ_5ZnDstGF9q35lC3QF7fCwlA5qLAszE0R9VarFpqWNMS3cjmR8_3fq0J61qCqLhGReCgyYP5g_lajwcjH3H8iWlCkD1Qdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
این فوق العادس پسر. من میتونم کسشر ترین حرف‌ها رو بزنم، و شما تشویق می‌کنید.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84685" target="_blank">📅 00:23 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84684" target="_blank">📅 00:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مورینیو رو
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/84683" target="_blank">📅 00:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEPQjBT7lGLaYwSae13nT3_IPcNgJoa8RkziWn78dyjcpHbmBPQiG3hqbFHk4to_m-7YgD2nJhN89Iw39KfhJxDBVR_zKI2smv9zetffHnQpjb3KSeEZHOcZuCTQyYRObb6TWlfuXx14iOg_GFXOuLo1UbmR4URlFjdNx4BSFSiTrNUQ5K-D7AGZDl4BBmDIc_nNo2AQivE_NteEdN1vSWP_kvPw6tr6jgA1vgg4wMVVIRaOPT_TqeYOgulxuhnuplH9E4ufz7zRmSR0cTGR3Q5EWlKv5NYdLVTLR5tHpNGkZ2Ntn3WFHlzpo7gNxofuIzfdZu0QkDGDgVlUp2nqqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R0nEwS7xeCOhUlA_blIydu5VwXFOcmvEylPUENbAgh4o11rbsj-BUET8TYBh_pptDvt-BkOHfZ9MRDJCoXTog0WCqsluT0gck_CIUWKkbZotnaAge7YpdibYeZULvAYCjTVx3RG15QM-sLXJS0rmtxIhJFNkKwOv9Djj5AWqfecFxjZEnwn_lKzO5Ao1IOPO7X_ZxCz2BspmPwpt3PYR2h8VRbIpBdYICMbi8YE5jQmrAwNgO-2VTed7QpmOBC6jZ8J4E0Icsje_D9tHZZ-wJv8VW3YjXZ3q998cGacrTEZj1t55RvL9w2cNsq75duwPA3t8OcvRluyoRv2QHlfCRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">با پاسپورت شمرون به ۱۹۵ تا کشور میشه سفر کرد؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84681" target="_blank">📅 23:46 · 18 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
