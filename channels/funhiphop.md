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
<img src="https://cdn4.telesco.pe/file/nKaNqi6iKzOnoDu8z0qGSclrV0Q2_Naw51JvZEHTAtCZNDndLs_yPYvh5v6JA1TRE_3WRjj9DsZk7kTK1oLmjG5c1IzKm4F0ldIFn6hP--yUwG_MtVPysqgdWDODXgk_XEVbjEtoZIoKdotRAymdaEIy7iZHSixW3omNEuIwt-OQ6_10AfNX-rnSs4Ttn4Ki4UsQeRxYTtpvWJH6_NyFP-yshkrK4aKoMnoT5lmcU1dPnXTEzDvX3mOALSye-N3wmwn3aF9WsptL9KyxTnHNebzcwIcRzuJ4nQ4n3KvLL1ina76Cx7ec0RDfASs1i7gfGYA3c16vV_Ae4OYqbcF8qg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 177K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-13 15:47:09</div>
<hr>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pKEf9aKJSrL_pCq1KMsVDUAjPAHczEU0QrrQfBKKUMAhE3JtC8W-6bidAvJnvlo1UBqP1sek7HIJY-WvJSoivXrnEakhizTlzlROgDE3QEpex7DaWx9J8A8zU-fnktbxG_rVROou3LACmF2G-tovhFAJ-RJokq71gDS2yKkoWFRMkjPFbVDPFdtImC_UwE87Z3-WD0TxR1bQXAvxEhlF6pg7_50a0yH3YNoR-5YUgxxiACED2MbPYLtJ4-eBS1d1AWEh4cLjG2MJRPUkFUrA3JBAkNBsik7DFMEYTmnl5WgA_21u4mqa-bG156hUNesAEL33zQnjkz36F2s4zeKriw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا تا ۱۵ میلیون دلار برای لو دادن شبکه‌ی مالی سپاه پاسداران جایزه گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 616 · <a href="https://t.me/funhiphop/76755" target="_blank">📅 15:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شورای عالی اسلامی عراق خواستار تشییع جنازه علی خامنه ای تو عراق شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.99K · <a href="https://t.me/funhiphop/76754" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">رییس جمهور لبنان حمله به کویت و محکوم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/funhiphop/76753" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sioh7jkurRxmT4YxByi0NxvZXT14QZ0dWK12yBOX4-sqiIEkMy4bU0TViA-yZSMU7l1xAXKhH9snvZBDBMIcb2Lk2TcNfGRi1--GelSjP3QgUxgWJXysQDEnR6qLZpVAi8hbftUWraZg80oQ4iz1hChltthOerCCR7o-TPTkOcx5HYw8FfZyeJOXYw5tYRXjJF-TfCy_qRXJHqzaTy-C1is0oIclv2SJwRNgbRxVX92NccyGDHBT2S7FwvMHBWlUvIPQqzBL-jNdhu63SRXFwgeTEwV7GyN8F3otAUgVHuvw4aem3WvhcLOslKrBeI6FLBXqRn3umM57z3hrwuxC8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C16r9eSM0ytRmiwGpKpBa2oja71NwbWceJ9UpZsu6Q4gAj4MXpuhYTLKDtfJE0HFbrMBVCTT-dleFK47S0mWgTQDmrjnA-0XNECIJFHdLa4_nEBphEpuqTawCyh3ZS4aaWtfsS1av56ojtCJucz-6ZY0OxOqL9VtZB_baq1p1vgvL-PxGlDbYniVQPB4lF22KiF1j2E8LmgLsOp5UoKJ4PDM6VLmQe4Jcf552W0nAMVEqfhtX3VY24KE8RSVg297gaM1Y5z7AlbWG1M-VLJrYbYkKkcWwfsiYoeWEnLKCnEgnW6HsekH1Gz1e9zlDDUooQ29ka2nw9c8w_PV-zywLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZQd8iHkeE7fyF_SaQyw-5ixOxdXYfHEOPHnfnGD0faM8H6XDFuyxdIyGsC3wGEwyb5hsl16RkwkztO0CB5uNuKQXv7pPjjrSo-Ty6X8nT986r5YaGA__Ilw3XXeRGhUUAuqdXecGPe1JxSkUf1DRLpaR5zYQEQ8KAaMX8FcqBEH1aU4uktYo7msb6FSKUl8TLMJF2pMfLqTkwU2QQkau-3EuxVGVUf0W7gtNzkn2i1073h_-ye87zJ9cxN65n3ELC-yk1n8MhMT7DxOFoHvfS2vPtQqcvlSb6SK1nelFattirr2GiH2s75LNR6-eLqu1DF_dbpzXn6qhLH9Y8moeQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=N4pRAuE0jWV9Sgm9hrZUwv-CHDTV83XKGSAfKVoX_WFcf28fvi6tfJLY8L6u4h8kKfxpve_jPI0noZpuJ76eHVnuSmayOAMIWcjZDx5hV-VnrFW3aD5gNqvGaFwrJAJ_Ytyw3JaTxTzS5JJf8A3fd27KUDvxmP7_BmalOw1Dr6CjGkAJDw41B6PZI-pX1LXbUlcRkIm_F8By7bmEV5M4lYn2SZISUlQ06jzU9CoboKK8bd4k1iIXO3Wl6RPKSEjjPgoDvEyEYuUfo5ybY7XY2scfp29Zw-Hf00H7k1EFt5FHe8xb5VQIn-nnODcuOaw9rkswUd5wIuO1_TZgBIt8Lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=N4pRAuE0jWV9Sgm9hrZUwv-CHDTV83XKGSAfKVoX_WFcf28fvi6tfJLY8L6u4h8kKfxpve_jPI0noZpuJ76eHVnuSmayOAMIWcjZDx5hV-VnrFW3aD5gNqvGaFwrJAJ_Ytyw3JaTxTzS5JJf8A3fd27KUDvxmP7_BmalOw1Dr6CjGkAJDw41B6PZI-pX1LXbUlcRkIm_F8By7bmEV5M4lYn2SZISUlQ06jzU9CoboKK8bd4k1iIXO3Wl6RPKSEjjPgoDvEyEYuUfo5ybY7XY2scfp29Zw-Hf00H7k1EFt5FHe8xb5VQIn-nnODcuOaw9rkswUd5wIuO1_TZgBIt8Lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده
ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/funhiphop/76749" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUVRercLgqh_3oh96m8hrdfzyIHC6KCIBT2_huj_mWf4oe-KdhEm6jSwyf5HJS8u0DqISuXieZrc9jWcGz9IeQOFQD5CuPCTFuJBiQOGlXQQlSDlcQIUwJ8sqUEMnfm4c7gWtRL3WBM2Ou61iiFo7yXtWjwOLp5lffxV2ctQuvAsN1jk3NwKY0ehW4mFEKRHIh8_8iWYXJnsVui8EXDu7BL37_qsZp0DFfZeJAhFrQSiiAfJkmqPyvM9y7j1OicIOankMRyUNvl2LSq4hM0vmLohK9Yh6MtUnqkaQ-KYguXxtRiRCBJA3NYhJOcrsVJn0EKR7LQohG4or79aTTI7Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "پیستول" منتشر شد.
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/76748" target="_blank">📅 15:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=K9zh6A8nuInUYwx9bB7EMarkbz4f-HKcyaVJ9cdNU6FtUC7ou8I_Y29NLeKY4mLGNe-C_PeTPj3RJrIZTQQivUywI9YVUz5uyiKLB0bfHT_huTB5_L10qO6cHMIPWQYu0ybLbMI6O8ihV0-UY28lV5ci-Ydbo-JuCFCw4v5X2qNiAW35LkR5_3onlxvh_Ey0hX9_5L2CJTpH291V41NIEtbaSunFLbg8FY4Zdy9yUvtifpoJFYIGkrt-a-N__n8qnJUP78eLJmlx2hjFi3UtsRxCx0LucZu9XyVURa2zOgFNLlVlKryc7QSiuEpNoDfToh7Zjq11t-ML3RjXhExFZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=K9zh6A8nuInUYwx9bB7EMarkbz4f-HKcyaVJ9cdNU6FtUC7ou8I_Y29NLeKY4mLGNe-C_PeTPj3RJrIZTQQivUywI9YVUz5uyiKLB0bfHT_huTB5_L10qO6cHMIPWQYu0ybLbMI6O8ihV0-UY28lV5ci-Ydbo-JuCFCw4v5X2qNiAW35LkR5_3onlxvh_Ey0hX9_5L2CJTpH291V41NIEtbaSunFLbg8FY4Zdy9yUvtifpoJFYIGkrt-a-N__n8qnJUP78eLJmlx2hjFi3UtsRxCx0LucZu9XyVURa2zOgFNLlVlKryc7QSiuEpNoDfToh7Zjq11t-ML3RjXhExFZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/76747" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اوه اوه بندرعباس و قشم صدای آتش بس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/funhiphop/76746" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بنظرم این نه دیگه</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/76745" target="_blank">📅 14:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">هرچند دکی تو ۵ سال کریر بهتری از حصین تو ۲۵ سال ساخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/funhiphop/76744" target="_blank">📅 14:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/funhiphop/76743" target="_blank">📅 14:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">MIGA: Make Islam Great Again.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/funhiphop/76742" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gbQXPAtth0a2cMluLhyQrE5s7nI0gHj9-enF1yP5BwxhJNqldrWMeqk5akd8skQvT5yUjW3P0Yoj6iTKvAs6F-o3Fov02-hxPNPfZ5yXBHmfAIiTbapNyqBe9TCpBRNQ4O0OKcjsbM8O_8-OuvRlZyFKeiU10bc5u1MpqVqb56FkkvFnLq209DS4807_PwZk8A1q6KkAdCY3N3ufpdPVuImutj8dhATOOXQYesUJWqjsuyvqRla5osIbaein8Ja206y_wRinGmoaFWVb-Q1pbEhT48Ph9uHDYVHeffwCP4J386YqIeZPBdBwTc638-29I2EQYxH03RLjiZ2jdIsxRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/funhiphop/76741" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c517113be7.mp4?token=D3qg-OdeQHvNwtIL8PNpFqzgxmXL54sNeg0vBRn_592dyuTNF44kbvDiDGydk3YZRfMY9Kqeg1rbl9wqliTPtwUydBdvgn3iOkzv-wQBOeZMxz2QhVGkh2aZyj8SeO8WO7PbFx4rz9Er34cGmGGpGd02x8pSwj_DT9rHIXz-OuJwVBZlrUdXgYzH3bXtIdxusQXyDtD9T3-SaHq4KpVN_ocv6DZeePXxHpdHua12c_MLxKqLln6BpEbukMlLAM8Eap2Yd2YTbBuH4pN26krOAtbktbiDyaWcXMQKE_QdQz1odSkUGUR6gUuOfenBMv99O-g5c1bELWkmYsoShKAVRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c517113be7.mp4?token=D3qg-OdeQHvNwtIL8PNpFqzgxmXL54sNeg0vBRn_592dyuTNF44kbvDiDGydk3YZRfMY9Kqeg1rbl9wqliTPtwUydBdvgn3iOkzv-wQBOeZMxz2QhVGkh2aZyj8SeO8WO7PbFx4rz9Er34cGmGGpGd02x8pSwj_DT9rHIXz-OuJwVBZlrUdXgYzH3bXtIdxusQXyDtD9T3-SaHq4KpVN_ocv6DZeePXxHpdHua12c_MLxKqLln6BpEbukMlLAM8Eap2Yd2YTbBuH4pN26krOAtbktbiDyaWcXMQKE_QdQz1odSkUGUR6gUuOfenBMv99O-g5c1bELWkmYsoShKAVRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/funhiphop/76740" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/funhiphop/76738" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامپ: احتمالا در مقطعی با آیت الله ایران دیدار خواهم داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/76734" target="_blank">📅 13:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwIxkxx8IpL3PjBtBFCZDQf_zLqosBYJ0VFxPpk30I8seR0Zlzy66wJZC7u89Emxp_7F3tLnA-pKMELQwAmFidwdDRBYKM-7JPMz54Jcen_jSj7G0vmSwbOP0GGX6aEXbVeR4Sim4jMkRl1nI_Kc3JyeqKlvPWF_Dl049DTCMOA5fY3QOKez3vyqZyb9TEFpm6P8NcsspBKiNktYYca3bIja-zjhNhX0jVugMVFNPNiSl1BXzqCaCA1uNoKNtGoY5OHl726Ukkr8bgHxLFStqffb-wQ4Apc0DzyvH77cMg0LhbrF9BDYHV41naCZRcUGdCHdkdGXAi3YJCZ_5BObNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط دفاع رئال مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/funhiphop/76733" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">شما نتونستید بچه ها، شما منو حامله نکردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76732" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دیشب در قم، دو بسیجی در عملیات خنثی سازی بمب های عمل نکرده کشته شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76730" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOzjaUHZkApP--SbQmNAWCCWEvY-ubo3QrD-T1G9e7J8UJxuyROsOXpw8ugIbgloeTXRYHDHONESVxHowbuRDkIsFSBP5M15ZzlBqR-dEE8vXg0wB-PMcCXteCfG9x59OajaiPxrPQk3qDIHd_Lhrd0V0X7jcHxEoaQ2L3BHMhXJgYiNvDos8BstRNAedp7IHXEmiOEYH_FeDC5rCRbPkyF-j0yLmtuNAuKvVSmlEjZn6hA5RC961ntNKy8s60LaFfzoi-oFupcdPpUWhdwpigW8wN5isehEy0UvKZS9BPMWEzWxAO1vQeDQ23nt6CKzB5KvXdnov_l6ncrmOzZH5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید کراش العالمین
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76729" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgJH16nmFKJI7AMi8Krbb418f4IGdiGpWCOAN1abVa_MBoMSnkwulEcdQ-RnqsE7X9sj2nPt57P-Z497gwVbPRS0PGpJoxu2SaJ4op6289FLUdfN1uqmBUdT1grEZ8S3ULmWfXuvMOA_vRkyvLJMNavhifggCZJ_KP1dRT75sMKmJhykJyUj7nptBmDuoCNbKVY4whkzuQMOosLoveENElHr3QNDxvZssF3jpfAkY56GbTM58cH7o394qFQXMuYyDtc-xzQ9Znz6ub_PuubcFqykfIFqUiqDeVavduqxA0yodqCLPFAdBZZvEgMbQO2Pm-018Dn0r8Me955OaxaxRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76728" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pn1mXYOL--Z93WvcSWPrVVd-eC-X6lye3hmlSGyAX8fNKPKz9Rr3YGWvtXQtrtKDFmCgG0RNQtyl1YlfBiWJe2tceYjmu49_fGkfUR5zBVTSS7wuZPf9YzVlKMfFLHGHj5Ri0wNXPai5moXxgcFJNMZEgQU93loyRbfMRfC0uIYfuhPYG72BozBhpi-YWSE5O_ldCkZXK7tk2HLx_95qoUVe1XTZLKBJwtHAsHxw_9YQNvV_L09cwDytv8HNBKT5N-XjyQ85eGohavT-26E9012AAQDHxOd-zkOaLh1JXI9OXEWieef8UxXTzDZiymimDb4Y1Y_S91CzHGr__pngpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kxGWzXKBANcGY6pLCR_0QrYSG5RWtIlGlJvvTZ7VpQjLNfOS9AvFINT-fPWM3nGoOA6OBSKmZfGnHlIMOULYQ5FyN0d_fW3J4_-z0EUMIssmRKtwyj4PEEYGlxXEEEvopE26_uWzvtFtwlRNFNiaGt2MLlegqseqSF6bXVbNX1YHAHVgDnYljwb2RnvFsUA6UIPkciwkAvE4SxNNyDQxo2FVUWi5qO0sEnK4ZiQC9GoPtiZEBNicQTjfrZ356E_tK7YrH7KlBrjYSPGCqsfSjl9rIstBrO96i48Dmp0KKi07yyi6eUWrw1w_20PP_d_8HlZOjDIA9QZLmA7uTN5qow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مراد ویسی (
لادن سلامی
) دختر عموی فرمانده سابق کل سپاه حسین سلامی هست
حاجی سیاست حاجی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76723" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/je5QmHB4Hk1N4pSvIrWQmUAj_QsKVudOzSEM47rAQBPw1Voe9IocKogY9b3rJXlITHuOEKs56a5Ux43topOfaCmF8H7QkTzc-J8MF8Ou5irDsNz26O_uKIU7436rofKDmBbRlKRvSLjZAJRlzkrNjHngNTBbG-B2Eihl50Mxf2mbqz7ikE4Ern62gVs9eseMLw6qikLS-ChDuJdFTTpdcZvXCb-KxZW4vCJzxFB9TcKvvF37_YYER2FChKsM4LdFMFXQXITBD-VCVYvhPO4-_wwffsXAyrQMEPfa-HAe1g7zP4c7J2Z80vEuH0mQjl5U-eIrhICq1bERrZIz7qbvaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده!
هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76722" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76720" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQ6qNZNGmCcIjfOUeu5oeZATpY9vLm6XG8vGe83DnXKPi3EKjsZkOHRYs5o0Xss_Rs_eAPsrqiDyl8UaJceeztDcv_9ZL68i4n6k8uJHukxOlSkIhEoRVtMs6K8GR3wZAglCiTD4VRZQMFAblubwTZE1D57iD5kWuJUYwybycSMf4w_7N6Q-iev4dDgcCo28QD6LZiOQnV3gYp51amU_Exum_K6WeYCaNzmtagpoykpqfT1Vt7ch7lcZgouJVoa0byGBozsI8_-CEuZiCktQCZcXMtjAHmwq8yBpXJGV_Rbz5YYjDtc3vIpIw_hyFh11CNTR9_3ALRU2wSZT9_irZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب تو با آیفونت توییت میزاری نمیگی من اندرویدم؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76719" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76718" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76718" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgk6MFovvmedOcZSPeRFj7UwahqZHVPOWguV9p7ohH3cgwO9eK0imaentjwbLfvm_2i3QFpIlSVX5mK_62-hmO_9W4ZcQ6sHsQuLNffn0slUpc1_N3N3nTFIt7-hV6GqsxxTT66-HZnJhIEBZMEfA-S0T-S-Ea4e8HQ0kauad26wBJf5HASyQ2xHQCnb6P3dbeuSneIxdFD_2f6mQKnJaY2ws8fFTs9nUvclDGUeZaIN7c0jVaPh5CxF4kETuYEZu1dCYFJGAx27KwGczmtapYFI2MUcTAc0dl9qFsF8dsxHLgb7bErWEmnSWdfvGxMUVyMUsmUQkSOC4qmHvExSEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
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
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r13
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76717" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76715" target="_blank">📅 10:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">زدن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76714" target="_blank">📅 09:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">صدای یک تک انفجار مذاکرات در تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76713" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وقتی میگید، کصمادرت ترامپ "🫪" اینو بزارید کنارش خیلی بهش میاد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76712" target="_blank">📅 03:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بخوابید ترامپ خایه حمله کردن رو نداره</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76711" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوبی رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76710" target="_blank">📅 02:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عربستان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76708" target="_blank">📅 02:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آژیرها و انفجارات دوباره در بحرین، کویت و اربیل عراق.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76707" target="_blank">📅 02:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=gYrr16w1udcECmFbt3JkJcwEQJWP6ael2SsqfNtUXlQ2OufuELiqv7h5AkFV9wWhV0d3ZMz_Zb-ACIdp1b5yZr-_G2yfJmyv6W4GkEO5zpA3DD02NqbmFX_gv47W2FukwwkFL3n_TuSDUzClrH_NCeRldi6f3DrdENB7MOD8w7EVwrXwizPGVj9ut7DI0raJNfgQasOED-EE3Hbt2LZG0_TCRZIASf0cW9H4NZJQSFlJivYMDdC7XAxQOORGv72-7AHuGZKImMtZM7JM6mPBdO6098LTvVXxwC6z1d-r4KeBkKbtDjwnq1IkAH0P_fkrG51E97i_Tdwfh1qFiD3Bkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=gYrr16w1udcECmFbt3JkJcwEQJWP6ael2SsqfNtUXlQ2OufuELiqv7h5AkFV9wWhV0d3ZMz_Zb-ACIdp1b5yZr-_G2yfJmyv6W4GkEO5zpA3DD02NqbmFX_gv47W2FukwwkFL3n_TuSDUzClrH_NCeRldi6f3DrdENB7MOD8w7EVwrXwizPGVj9ut7DI0raJNfgQasOED-EE3Hbt2LZG0_TCRZIASf0cW9H4NZJQSFlJivYMDdC7XAxQOORGv72-7AHuGZKImMtZM7JM6mPBdO6098LTvVXxwC6z1d-r4KeBkKbtDjwnq1IkAH0P_fkrG51E97i_Tdwfh1qFiD3Bkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی درمورد روند مذاکرات امشب:
به قول آیت الله خامنه‌ای، دوران بزن در رو تمام شده است.
بسم الله الرحمن الرحیم
﴿با آن‌ها بجنگید که خداوند به دست‌های شما آن‌ها را عذاب می‌دهد و آن‌ها را خوار می‌کند و شما را بر آن‌ها یاری می‌دهد و دل‌های گروهی از مؤمنان را شفا می‌بخشد﴾
(خداوند بزرگ و بلندمرتبه راست گفته است)
ای فرزندان آزاد امت اسلامی و مردم مقاوم و سربلند ایران:
در پاسخ به گستاخی و تجاوز آشکاری که نیروهای تروریستی آمریکایی با هدف قرار دادن حاکمیت ملی جمهوری اسلامی ایران در جزیره عزیز "قشم" مرتکب شدند، نیروی هوافضای سپاه پاسداران انقلاب اسلامی، به فضل خدا و یاری‌های او و وفاداری به عهد خود در حفاظت از خاک وطن، با حملات دقیق و گسترده موشکی، پایگاه‌های نظامی اشغالگران آمریکایی در کشور کویت را بمباران کرد که منجر به نابودی موفقیت‌آمیز اهداف و شعله‌ور شدن آتش در دژهای متجاوزان شد.
سپاه پاسداران انقلاب اسلامی ضمن اعلام این پاسخ اولیه برای بازگرداندن ضربه به ضربه، هشدار شدیدی با بالاترین سطح قاطعیت به دولت آمریکا و رأس استکبار جهانی و هر کسی که اجازه استفاده از خاک یا آسمان خود را برای آغاز تجاوز علیه ایران می‌دهد، می‌دهد:
هر حماقت جدید، یا تجاوز دیگر، یا حرکتی که حتی یک وجب از مرزها و حاکمیت ما را لمس کند، با پاسخی لرزه‌آور، خردکننده و قاطع مواجه خواهد شد که از قواعد و مرزهای معمول فراتر می‌رود و نیروهای شجاع ما در تبدیل تمام مقرهای متجاوزان و منافع آن‌ها در منطقه به خاکستر تردید نخواهند کرد.
زمان "بزن و فرار کن" به پایان رسیده است و نیروهای ستمگر باید عواقب وخیم نادانی و ماجراجویی‌های بی‌محاسبه خود را بپذیرند.
﴿و پیروزی جز از جانب خداوند عزیز حکیم نیست﴾
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76706" target="_blank">📅 02:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">سلام فعالیت پدافند و صدای مهیب مذاکره در بحرین.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76705" target="_blank">📅 02:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">کویت صدای آژیر خطر میاد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76704" target="_blank">📅 01:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ادمینای اینجارو دیدم با ۱۹ تا بسیجی درگیر شده بودن و موتور بسیج رو بلند کرده بودن پرت میکردن سمتشون،
چقدر زود قضاوتتون کردیم.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76703" target="_blank">📅 01:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z68zPdFlWqiOVCwcZ0Y8S5HvJVJOF9cLI79g5bD6pLv4321bAwmK7YKhfN6Aa3654qxI-raB_R_tLBCe4kx-tQFBWpCpSw1yIwjWM5FmHEH4Etbw8MkfJJ1t5zihqAFaFF7hpVTIAk5XEipTOAQg_J74jKvl0C0zhDjhy7OQjO4j9h_6OtsbP_xTV8E5w16efL1uh7GjDUk79WI4pGbMw9N5QedZlHsYkL0SzEeiP_XsQ5zUKY6OkY7fHJqtxLCbxDd7gh8YdhyGcsnyqoeFHRuzzKsbM56MoirpsjyAUJa32psM1Wet0rRi8w6wAcNBVTXKn9qmrOlaKwu0nomF7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ضربه ی اخرو محکم تر بزن، اِبی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76702" target="_blank">📅 01:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دوتا موشک از استان فارس داراب شلیک شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76701" target="_blank">📅 01:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کویت صدای آژیر خطر میاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76700" target="_blank">📅 01:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">این آتش‌بس ما چرا نصف شبا رفع فیلتر میشه؟  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76699" target="_blank">📅 01:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWKeWSOdeBoNdTqm5oH7aySUc1zRGQb_DEG4c-K4fUOPWO6j_uPazhHB2a9o8I7MQpoQwWejDuzNE1LoUwWH1lLEB0Z4doEjcu7sfJgZ3tBKynP_wNVfko6VvJvrKPnyoTdFRHcsECt5mSgdILctemvZApwdDzvkFPDmA9tNPFJ3ucVhS6SDGaDXA7wEXMfgQNq1YnV9h1MBkT2mzvC1mMN-CH3Ch5XJSDn2U5QyxpkYqKrY3c_1lrkdDdk0xhokm3mIxKtCxK7P3cCFk66eDPJBtv0yLOnk6ts9XYYAzdY6zv0S4vkRUbTdcJKeuZHr-7VKbAJGEq9giEKI1kSC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ مورد علاقتونو زیر این پست بفرستید، شب خوش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76698" target="_blank">📅 01:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دنزل دومفرایس دفاع راست هلند و سابق اینترمیلان به رئال مادرید پیوست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76696" target="_blank">📅 00:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ننه روبیکا رو کی دزدیده بهش برگردونه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76694" target="_blank">📅 00:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76693">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خیلی ساده‌اس ما الان میدونیم که ویناک و حصین میمالیدن و دیگه نمالیدن
ولی مثلا دکی چی
کلا نمیمالیده
یا هنوزم داره میماله که چیزی راجبش نمیگن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76693" target="_blank">📅 00:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">از نظر ویناک هرکی نگه جاویدشاه پشت مردم نیست و خایه مال سپاهه، عالیه وضعیت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76691" target="_blank">📅 23:49 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شوک قلبی به حصین:
وزارت خزانه‌داری آمریکا چهار صرافی ایرانیِ نوبيتكس، بيت پین، رمزینکس و والكس رو تحریم کرد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76690" target="_blank">📅 23:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76689" target="_blank">📅 23:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76688">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PS2mXnTKu17xA08IfLyTyUAeiQoTbiJVNPPYa68z9fUc5fnMjMb-eIMqVypfgitIEUHbZrNgu6JtH45ED0sKy2CGsJhwX9amlzmHYZifgpGsU9B-qLPOoMdU8MImiKTzh0Bby-pdp-jdvrTjct6Fv4Dpj_J7AQiNAKdbF7yO6vM7l27paqeBqfZNXrJ4vw5pqGzXWhKm2wlf9vL93si-zVEvbvFtgASELpQXpApabsC-c_QNGoUeSQ7WNDAsRUlxdbxLe_-Yxy8YwbRweLdmM9TawXcrnoKxwARy6xjmQgthGZowofjRXKoxZcXs8uXcTx_kjR8InNp-c3dNMzSbjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخالت نکنید دعوا داخل سازمانیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76688" target="_blank">📅 23:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76685">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JV6xRHsGduFl33vLBx_9A04P014oFf2btPKLLbV7dAl79QES7C5TZOOZ-Hu6Y0LgUfbIt8fEGR0Ypgq3IMk-N8pj1npScHJi4uB0m72Eu0pmWvRfigFkDECyFG8ZcKVIsSS1327hd_J887db00RDXOnkgK0-_wiue3dgTEY87hOtrkVNNltii-04sWmmdBDYe6LgEiS9qXtnVt2XoFYRfi7BNVnloavWNy3BpAlfiPE9_B77EBIKLasf6jC_EBoqTrfbD_cgnQQoXzTUeUbJJVI1uB9lKEW71dqjMVXJGUctHYnj8mwv0auWNaHpC6xa61gTRMx5O9cxY_0AF44qjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دعوای سنگین دکی و ویناک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76685" target="_blank">📅 23:37 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76684">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IbP7431DjAYy6PmQxef_j14B6IDFrN8NG3MA8uOCHEfvvkn_Hl3WCUAgUc_XTJclpowpUhZxSQWIH3ShenSQFrlY2Tkm1W__3GfshCBQRHqE-3pBvlVb7buQCy6LlNqfLZwKUu4CO112d6lwgv9sbMPx5IXB7DpSeBxuYzTIkdxQoUqQ8VBx9TyaaEZ7GlHx1ZKbgus90I8bbBHuCb0kn70i_W7PnZwTCFKvE-8v6SCkjOY4F0cMN4svZQm7s7QWGZmea_oz2kpWvGjiIWHYWrk-JKDFaGvWM--KFCxElqm5MJcJh1s_GaJzprLMIvLefGDaLhfp3ZjMBguvofJwXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76684" target="_blank">📅 23:36 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76683">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/76683" target="_blank">📅 23:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76681">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">رپفارسی دو بخش است
یه بخش مادرجنده
یه بخش خارکسه
یه فدایی ای هم این وسط هست که خداست</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76681" target="_blank">📅 23:33 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SdDuMliN0ANZarjwt3b907qy-P9nnMxL8491Rx0R6Pf-NpSP7Tk1IkDN0nn1OO_CgVukaltt-BFDsAYV14SfSsXPxddximG827SpnONDNEVC0GCs-rANlflqH1mP4TVrRMAaf9rySPJNFD7BTsSGGU5AGhvk0_JVKYDR2D9HtVc2nUSmqzu7vyR4JMWzICMtJFPkH3NeHsRVw50zzjhpQgiiTx3-XB36ztx_63K5hHU9Thx5CILgRhpZvNmvzN_vd5IdRaeJTyKaYYXyWEz9dpDlG_cSRHRE7671j2Oar14v7oQfGPcG_-j1_tqFo58TEeZPnQWVYcL2_SFR4AuFjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76680" target="_blank">📅 23:31 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ویناک گرفت رو دکی و حصین و سپاه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76679" target="_blank">📅 23:30 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromArshia</strong></div>
<div class="tg-text">چرا بی احترامی میکنی بی تربیت</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76678" target="_blank">📅 22:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">من رپفارس رو دنبال نمیکنم اما ایشون دکتر چی هستن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76677" target="_blank">📅 22:54 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76675">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee30f49b5b.mp4?token=plm1mfjtYrutqeXsDzCtKg9kX4t9Y_LK1GbRGeBBowpFK3lppUWqm3v96_ikeE481xdhV61LoRUMUnVlSy9P_4ZCs3Fii9V-JSp7Hp_nZZWbg2h9Vx4rAhRD1ZyHw13hg5ZBZB4H64ckXyZRnxiTlXlvqQJ7FoRHzLNhlsRa2hF-L7bNoMGdvrTlLkinkCzNKxLVKpY251pGedQtMRA-Hi6vexXMw3ElZ3d1650Ixw5dGxs15bsvltm6jqWkq7Ce8Dl546B5pzJkHfsmr2DLxzgbhBKWj5VponRdIGCcfwsEXP5WX820uh4AgMaiLPoGq-4mnUJu0vy2L_4my-F_RVatjdBzwPdBKdxHvLdLXK9rwFjmFsewt5FGrqw0VzuI0J8mDJ6NvJGfyv-0T8rR1wY3uKQVZZYA5N9B0j-697NiYeod41rHsQwlKX7Vjcb8NrvzLnw_wrWw-ELfxVPIAV-brsR48z0Or5abom3gt9vsM77ysNZeKj8v67Zmwvm5r4bKl2RlEnIbuX5J4aM3y5gy-CUDe0vDqEgg-62QmvYGascIeqG-9PrRUcQCeSAL909LSiaaTi_JeSeviWzWytBjKAFJzuYeuWZrLhoKL3KYhNtC0x8C8OmLFKNTSgpCnv4bGeB9c2El8pBNY4pAi6fg1f4ajaBZok7-MJFyEWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee30f49b5b.mp4?token=plm1mfjtYrutqeXsDzCtKg9kX4t9Y_LK1GbRGeBBowpFK3lppUWqm3v96_ikeE481xdhV61LoRUMUnVlSy9P_4ZCs3Fii9V-JSp7Hp_nZZWbg2h9Vx4rAhRD1ZyHw13hg5ZBZB4H64ckXyZRnxiTlXlvqQJ7FoRHzLNhlsRa2hF-L7bNoMGdvrTlLkinkCzNKxLVKpY251pGedQtMRA-Hi6vexXMw3ElZ3d1650Ixw5dGxs15bsvltm6jqWkq7Ce8Dl546B5pzJkHfsmr2DLxzgbhBKWj5VponRdIGCcfwsEXP5WX820uh4AgMaiLPoGq-4mnUJu0vy2L_4my-F_RVatjdBzwPdBKdxHvLdLXK9rwFjmFsewt5FGrqw0VzuI0J8mDJ6NvJGfyv-0T8rR1wY3uKQVZZYA5N9B0j-697NiYeod41rHsQwlKX7Vjcb8NrvzLnw_wrWw-ELfxVPIAV-brsR48z0Or5abom3gt9vsM77ysNZeKj8v67Zmwvm5r4bKl2RlEnIbuX5J4aM3y5gy-CUDe0vDqEgg-62QmvYGascIeqG-9PrRUcQCeSAL909LSiaaTi_JeSeviWzWytBjKAFJzuYeuWZrLhoKL3KYhNtC0x8C8OmLFKNTSgpCnv4bGeB9c2El8pBNY4pAi6fg1f4ajaBZok7-MJFyEWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ببینید این بنده خدای مو نارنجی چی میگه من بلد نیستم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76675" target="_blank">📅 22:45 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76674">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbN6srOE0grzWeBwmqCfDT4RdnQp461N0GPz4MTh5JfskKW1PAWHL6pFJN57iDGaY2JYg-Tjga-t0Ie4L9kyZoFVLaoyBI6He86f1bR2KIeg9GNnG4rQtfrmNkvMH3IfvThFSfoBbfvIojJLTLrNlTxpPo6WNHY9AhPGnz7VWrrlaPBPdySU_jVynIEVl-cCcrDKP3wCmupH5VmzEfE2qcKJU9KDFDhccoO0VnU5BHl3MSiENuh6fHYPUHeLQ0PvjyZD5F1PA038FChFekdXxzpKp9f5KyqFF7O3o7Z5ACGGkONk-QDXA90igdUJrz6C33qDEPc9FwDeEUv79IF9cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلاقیت در ملت شریف موج میزند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76674" target="_blank">📅 22:44 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">درگیری مرزی هندوستان با میانجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76673" target="_blank">📅 22:21 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uuo9NKfovXRixtf_cCMf_jH1xohc_T9tOLAMaXQyA6SSPn8WKIDDVhLlntY0ma5dqGPO-Tys7l6J8XZOOOmGsH_oaq0U1zh-_f-Xcek-ycHgTeCNV8Gv1geFrGGwvSyCVRsBZKeWDvSVVcDgvGjzmUH0rZ-n9UsgAjsHajVqdRY_2YjFxKJ9o7jQ_6uasZU7QoBYXWJ7SXaTmuE5McnGU9fLlq6AvAvGGmCdWTe-Jf-bqeQN_KoorePsjGtfxEg_zYP8W6bye63GiX0ErOOIMO5TL_zzU4GKz973ZK-SPYRXIqNxupchRCjYZP2Z7ouWf0BWADIJFZnpNvsJkyrbPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تبلیغ جدید نایک با حضور لبرون جیمز و G.O.A.T
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76669" target="_blank">📅 21:51 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76668">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lkb8eqIE-HueVn1Rwuf7k6QNBpmdM-h1iQxEP66qPWgnzEQNJVwE_9nE_y8171-NliSnRMwfDdgEsimkbryP_rO04wIKi5Umx7P1mVGvOJ1zjv1VsRYjCMBfwUVEPIX9TVwO1i5ZVSjM1rtb_bhg8gBbBg6NZSCYEHLV1HiXyPaONKBp1d9tULkxTWAElLLUBM5ztXmb_b3V6nd8wx9P1nYG7Z0_fft7QmsiHtqZpSpBx1eulMI-9e_YPb-m8VZ42ehtQ4ems55x8Pw9SQ8d-qhRVv2es3aAtGoA3K0Qao6rb9TjWR04LkUqwGB7UgclkdNQbmKYwVWboOCrWTNV5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین خارکسه اس، ولی به تو هم نمیرسه کصشر بگی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76668" target="_blank">📅 21:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76667" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚀
تعرفه سرویس‌های VPN
🔹
V2Ray
▫️
هر گیگ — ۳۵ تومان
💰
🔹
Hiddify | نامحدود
▫️
سرعت متوسط رو به بالا — ۴۵۰ تومان
🚀
🔹
Open VPN
▫️
• ۵۰ گیگ | تک‌کاربر — ۸۵۰ تومان
👤
• ۵۰ گیگ | دوکاربر — ۹۵۰ تومان
👥
• ۱۰۰ گیگ | تک‌کاربر — ۱,۵۰۰ تومان
💎
• نامحدود | پرسرعت — ۱,۸۰۰ تومان
🚀
@suii_vpn
@suii_vpn</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76666" target="_blank">📅 20:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MNshY-1JPLkTjgwTywsgz1BiqVRbFjphg5nrGQYGo3dPrEIluGZMM7JkqwYE5xYQJStopxrX_itHHk_guEJYfv0pCC5V5724aTJjQA3cBxQHMeF-mmSvbFLbmhr9vy6pI2efhYw2a1RlouADTQ1z3VXxZH8R-ptKb9QWDfslA5gRv5F-1rDb7PGDon1tRwRUDpaq4D7P0ZbjoziqogXY2CK6gmoCSfAvxG9wImvE3SY8M9lF_q2azJ_gv_t5tlSLJ_fHN3p8LfVG0DrDQZeGNr9NnK3YU8NHSA0z2LTQFnEP1_0s94ujoaGSH4RgXkntcPF6qP4zz4D2z_AL3Fq1Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ح   ز   :
این چیزایی که فارس و تسنیم می‌گن مذاکرات متوقف شده دورغه بابا.
این حرفا نیست که اصلا.
ما الان یه مذاکرات خیلی خفن با ایران داریم که خب البته نمی‌دونیم آخرش چی میشه ببینیم چی پیش میاد ممنون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76665" target="_blank">📅 20:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">روبیو: شاید ظرف چندروز آینده خبری از توافق با ایران بشنویم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76664" target="_blank">📅 20:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نتانیاهوی جنایتکار در مراسم انتصاب رئیس جدید موساد:
رژیم ایران در نهایت از صفحه‌ی هستی پاک خواهد شد و و ما کمک خواهیم کرد تا این روند سرعت بگیرد.
در آن نقطه، این رژیم هرگز باز نخواهد گشت تا وجود ما را تهدید کند.
این دستور من است – و این مأموریت شماست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76661" target="_blank">📅 18:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رویترز در گزارشی افشا کرد، ارتش تروریست آمریکا برای هدایت پهپادها و کشتار مردم ایران، از شبکه استارلینک استفاده کرده‌است/ رسانه‌های خارجی مدت‌ها استارلینک را ابزاری برای دسترسی به اینترنت آزاد معرفی میکردند/ چند هزار دستگاه استارلینک توسط عوامل اسرائیل به ایران قاچاق شده بود که عمده‌ی‌ آن توسط دستگاه‌های امنیتی توقیف شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76660" target="_blank">📅 17:57 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mFz4etSciHWHzEDSkhxMF2d8tFKjNuqX5LGrbF8etjhbw2Gx6CfzwdXwSm90xKRVKYS034joXF-xCOSSE8PZTQvurD-IR4CfbeaITNBaoCVhZV9JhZj_541OeExs8Qnv2r0H1gxTMWSO_Yp5XalHwcxKZIDviCSXDKcKBgaN6EBNO1hjGL4KDVV077skit5miZE4Hth7hanPjQdH30b_vZWewbb7CnJ97_85pQ9KgZ3RyNbxv_TF7XY2pnd7nWTQSZ3In67UZycOvkdEsX7ZLdadD9Por8cuOHRecNJV9uk5nNr72gKf7yt10CuWjVENdNTN3ccM6NPUTOnme3H0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیشد
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76659" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hcttHoiGiJUjRDg3lAlpyXbc7OmXXGdeOEhijCtAtWHqfc_OoBUKumbO09HyEnoZPljsMZAj6n7j19OumHQ452RJla6mD11tJnl3Th7WnOkx6GoOOUApMSb24w86Ew1F1JuZbz69u8xPqBGEjxnDefsyOWqtvZj-7npk_aBvSHp3ykdSUoj8Ev4akQpJj2iqtKdn_s7EZ7UEpjDdwwRbGuR8TF3uC6z3CixfsCJJNEM2bTG3-IS8_5ingoGj3SWjV3MHkFpH19QGTB4W6qu-KzzxJ6LI11VZUw7Xn5RZNZ-iE6VKKkkMzcgbMY2QwPO8wX9A32Dydaiaytr-QqxJnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g12
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/76658" target="_blank">📅 17:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رومانو:
کوناته به رئال مادرید
هیر وی گو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76657" target="_blank">📅 17:15 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دور چهارم مذاکرات اسرائیل و لبنان توی واشنگتن در حال برگزاری هست.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76656" target="_blank">📅 17:03 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">معاون شهردار تهران:
برای تشییع جنازه سید علی خامنه ای ۳ روز مراسم بدرقه در قم، مشهد و تهران برگزار خواهد شد
آمادگی حضور ۱۵ تا ۲۰ میلیون نفر را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76655" target="_blank">📅 16:59 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76654">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">میگم اعتراضات امروز دانش آموزا به کجا رسید؟
انگار تاریخ امتحانات رو یه هفته انداختن جلوتر که
😂
😂
😂
😂
😂
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76654" target="_blank">📅 16:28 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">حصین به نصف رپفارس رید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76653" target="_blank">📅 16:24 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76652" target="_blank">📅 16:13 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">یجا گفت مادرجنده با تو بود</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76651" target="_blank">📅 16:11 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">چقد داشت تلاش میکرد وقتی میگه کون لباش غنچه نشه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76650" target="_blank">📅 16:08 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k82x53D_j82hD1-CIkbAjF3AlJ2P8P5oG6aJ6tSEFVqIjfsxeSATwwx_ek-C0XmbnOu4uiInCYzW_sgdn1eeHMUW8HVxAUbBCna0zg-aVAnVUDlQEHXvIji3-zfD8isGa1AdrUuuOA3UpHNwC0sgSM-WQZRqYHCm33hEzloGOU27eHJenDzFij04icZT0P_GcPnJf-6kgY2xjCIohB1GiH7lTzyGiWmyTtR7jpXJwkxA12_bh5A_Hmk24P7hp7t5xnBhbRHzvb_D9EYBngT8F6khOpa50AIcc0tNuxn2b0DXUBRuKpKCgILq4IcpLtxTuUC4cfx-GrD-sNOLBOSk6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ی مشت کونید همتون</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76648" target="_blank">📅 16:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76647">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حصین یجور میگه ویسایی که ازم پخش شده کار Ai عه انگار من موزیک دادم گفتم "گنگ مثل رهبری، مثل حماس پی حماسه و..." دهن سرویس محتوای ویسارو تو موزیکاتم میگفتی دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76647" target="_blank">📅 15:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76646">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کصکش دیسای پنج سالو جمع کرد تو یه ویدیو ۲ دقیقه ای جواب داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76646" target="_blank">📅 15:43 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76645">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حصین بنده خدا انقد فضای رپ کیرشه هنوز نمیدونه دکی مهاجرت کرده فک میکنه ساریه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76645" target="_blank">📅 15:40 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76644">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آنشرلی با موهای قرمز
😂
😂</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76644" target="_blank">📅 15:39 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76642">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">یجا گفت مادرجنده با تو بود</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76642" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76640">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">به حصین دیس بک بده</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76640" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76639">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پوری پاشو پسر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76639" target="_blank">📅 15:34 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گنگ مارو تروقران، به چاقو میگه نایف</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76638" target="_blank">📅 15:32 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">حصین به نصف رپفارس رید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76637" target="_blank">📅 15:26 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FT3nmR3aJ1TPA1FSjJ64r6mBbPLMTj8FckgTrrj-fsD6-GBeO49qvPRc4p2I5R4fxqHl_kPVZj3AJ8faMHeHBRSLhFjAm5SV9J4iQfrd7Ae4rDYsysdEWfqsIDWrHTDiMLPfXO7LsKkk4Ds6MhyP8jI2ppvJHSgf2fXxYjm-aIzc6VESoTxnBBRNi_ip0Bm2Y9JqkzF1_vihTKdgx6x5dQaJPacgmKtO2eye4TyVtft0v7RaqdqS7txZtebEd0OVnZ7sloLzfnrfp5LFsSkE8hYZCunqu1gvQ54RrcM2Ssiy678drDjlpOunUZdixozfWvU9zESwMhYilxgqkZ7Brw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این وسط ابر بنده خدا چرا اوبش زد بالا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76634" target="_blank">📅 15:18 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">📌
🔴
دوستان فان هیپ هاپی مژده مژده، فروش سرور های نامحدود اختصاصی باز شد  یه خرید میکنید کافی برای خودتون و خانوادتون.
🕯
سرور های یک ماهه با ۱۵ کشور مختلف با سرعت فوق العاده( پینگ بین ۹۰-۱۱۰) مجددا موجود شد.
💸
قیمت : ۶۸۰  برای خرید تشریف بیارید پیوی
🔤
@Behdad_sps…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76633" target="_blank">📅 14:56 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">📌
🔴
دوستان فان هیپ هاپی مژده مژده،
فروش سرور های نامحدود اختصاصی باز شد
یه خرید میکنید کافی برای خودتون و خانوادتون.
🕯
سرور های یک ماهه با ۱۵ کشور مختلف با سرعت فوق العاده( پینگ بین ۹۰-۱۱۰) مجددا موجود شد.
💸
قیمت : ۶۸۰
برای خرید تشریف بیارید پیوی
🔤
@Behdad_sps
🔤
@Behdad_sps</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76632" target="_blank">📅 14:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینترنت بین الملل باز نشده
درواقع فقط فیلترشکن های رایگان وصل شدن
#MVSGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76631" target="_blank">📅 14:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سفارت اسپانیا هم مثل سفارت فرانسه و آلمان تو ایران باز شدن و شروع و از سرگیری فعالیتشون رو اعلام کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76629" target="_blank">📅 14:14 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBp-rnv3C4PqPP5uFfNTlzcx7NYL6EPjTGjIoUezl2RZa1zkUv_Fwh4918jB-a0N2XxtFOo8vOV2yjPgKTHOczTq--W_moPVaujXtEK8CekZoxm4K4FlISJHCE2rR37VUB8XG5Bis9IcoWVlmfdD-Y-C--4QX9JSvbfKb0tiaZTY5zTgasKaTMXV5Yw5A7JW2B19KNsh26QT6PFzBHjlJW7-urxCfqua9Z00o-retSvPEZcnMcdXDZVqPIlnK-uR85IAfMQAU-8axTyL2mI7c5XLMtSuYDDwQRQhvF7aesp9W71YUi7o9ueU7LVD6HBDMUu6Mqwmvi14RnBzUN74LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرسنال</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76628" target="_blank">📅 14:07 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">۰۲۱کید من هی میخوام مسخرت نکنم، بعد تو رفتی کیت آرسنال پوشیدی با پرچم ایران داری آهنگ انگلیسی میخونی برای فیفا که پرچم شیر و خورشید رو تو استدیوم های آمریکا بن کرده، حله.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76627" target="_blank">📅 14:01 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">تنگه کص نمکی رو باز کنید تا کیر اتمی نزدم بهتون</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76626" target="_blank">📅 13:48 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76625">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کارت فان هیپ هاپ هنوز استفاده نشده و زیر آستین ژنرال ها و پاسدار های ارتش دو کشور قایم شده، برای همین تو گزینه ها نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76625" target="_blank">📅 13:46 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76624">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">دوبار نوشتم در نهایت، ببخشید سواد ندارم شما یه بارشو بخونید</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76624" target="_blank">📅 13:42 · 12 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76623">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-poll">
<h4>📊 به نظرتون در نهایت کیا باعث میشن در نهایت خار این آتش‌بس و توافق گاییده شه؟</h4>
<ul>
<li>✓ تندرو های داخلی</li>
<li>✓ نتانیاهو و ارتش اسرائیل</li>
<li>✓ جمهوری خواه های تندروی آمریکا</li>
<li>✓ هیچکی نمیتونه کیر ترامپو باقرو بخوره و در نهایت آمریکا با ایران توافق میکنه</li>
</ul>
</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76623" target="_blank">📅 13:41 · 12 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
