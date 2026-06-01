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
<img src="https://cdn4.telesco.pe/file/TRY9RHoJQAFMjUCquG87f7OgyzPJych4yt9PkOTgRGcT42Pm_wIQMjbADhv3Ss6NJUKqeAjj-DunTMRarIs0u9oyUtfV-Rklj4268g2Wjk1kLtHlbJGYV4Y9QbTP9Bi1LIFHtlU2xNa-i8d1bM_cFiFhwBogpWQIzeGMfVBUtzj5Ie_rwyzaAyKoQHZvKt0at9N5-gdMeTnlijbVX8ccJvzV_JezUjgmjFOLaNrKX21SV4rkwon30CJrsrrJqFJXR19EXTUI1MeufL_qWJEFQCYAmHWHsGj_32y7vRwOdilnd_A_aN-lvDIdXrJypX25nsz79XuBL4_-qggwB3LPYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 19:19:40</div>
<hr>

<div class="tg-post" id="msg-439266">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJSfEF0yjgJsoyoQxe-ObfncQsQ0HZXHn-DcxQI4juIjLe_o8ftgm61QDHzGjZAjbgcYnj2vFh5LvtyJWouMYZKAX-Ual6Ad-DNWv0YlHkqDeFU0PDiTMKcypYidyEjS1Aql7sQ4o6gQdHs7BPXNog67RM-ZkGMnlE4hkKMu4vIUxRyMMQBZc6wdXfoQcwP2-BLXs1BQ9zbWvqE-_KcTPZo7HVKvy2blPOTsAZZ-2Q7D1N-WP3oTe2TQnh0GIJX4Pd0RIuS2BfW05z3rmH7IzvkrYs48x8-FWmbifajzfLgEhKG4hdMz6QtqBlxhrMULYNXAGcsZ4bbcPRSPxNoKQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان سرزمین‌های اشغالی
🔹
نتانیاهو در ادامۀ شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔹
با توجه به نقض مکرر آتش‌بس توسط رژیم، در صورت عملی‌شدن این تهدید…</div>
<div class="tg-footer">👁️ 364 · <a href="https://t.me/farsna/439266" target="_blank">📅 19:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439263">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
هشدار قرارگاه مرکزی خاتم‌الانبیا به ساکنان سرزمین‌های اشغالی
🔹
نتانیاهو در ادامۀ شرارت‌های خود در منطقه، ضاحیه و بیروت را تهدید به بمباران نموده و برای ساکنان آن هشدار تخلیه اعلام کرده است.
🔹
با توجه به نقض مکرر آتش‌بس توسط رژیم، در صورت عملی‌شدن این تهدید به ساکنان بخش های شمالی و شهرک‌های نظامی در سرزمین‌های اشغالی هشدار می‌دهیم اگر نمی‌خواهند آسیب ببینند منطقه را ترک نمایند.
@Farsna</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/farsna/439263" target="_blank">📅 19:05 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439259">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromسیاسی خبرگزاری فارس</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WHHMYPULRsri3Sk5gA0TouwK_JrzBG9jbaiuwxiOU2WY4YkQyaXSi7xMMcqIu_3X7XvUQXxZdDYoRb1blYnaKkvTJpxwzxDYsl3fqQO_Qia5NUSixAhK_ZtsVqB0eRVoBVYPZTGFgwDLS6L-WCnHx94K4onQW89Sb60IaSW61w7ljYJYIx9sMMwjxdDPSav0knm997c_9jdTNZWl6IOY0AmF6yfens191oWyh1ozfpgk7eLVBj6_L7P5TwKmerSW9Nu01jn5OCXabL0V7i4GmFzn0pL8E4TYKA3tUY6tfVgr_KI_Xti1-sK3WN5OLRfeWlLsdLjjhXrvm-M4CKTHFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gFMZr_OwcK1r48RqTjVmVSVfNOGd2ZK2gs-FRJVHbhRFdAmaeudfnqcVT4hhiZKFEbuQ6Mx0WcuGP3bTRJbJUsMp57DFxh4KGiK1cS8RKPtUAMsZgZKtY5UOV9q1E-Nqy2yo8dBiAWFex6fcq7cTMcCDpClTzQ9D3bzcQuHNxy1bzjihER-TxqMUTduIykqnfzrcCXp6msDtB9P9tYt9U4rRqcrQmqX8m4IryMM6XgbQ67EcvIxc4kj-oorhDbhqkzG7fWdvDfy5cKYKI2H3QDCxb8gkDVqtHhyjRaJDEBi_GFRe7wLTmM_Qvo7ZOLxruFARPWIGPNme4xbXqOASDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z_qGB6fzrWSTs8hABDdSRIGoaM8_pRiywjBxpceMegJzj5odkGEq6oDzO2O5DxmiXkAK6MFV5XjMaO94DWiD4xYQURRFDyHaMQoVVAK5IYvJ2fOIf1CzkKNEjf-GXbr28Xs5bi4u9UefpYldd8sWGPyMdaVa8K-2mDIvVFW7e19y_e4l7q4isqPljR8vUs9SQc1jlV1K1CMzwntdKvgyo5xHAdHXywXVI_zCB4d-iJE_m2XdfKBxiAq1HSlMSpvvfRRsSAgv67XXSdT5t5thg11e9KKsyp_9Iu1OX-Xjf7kapvz_A0oIIhE8SbZ27bLxv8bhNUTRwjxIlwG8oiiNlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXHvMC59fGb_34BLCXhXFfFT6v5Hv4egKuKH2Nml9y2A3U9cNCJ85uL8tnZ0RDiKQbriCF1v3AOLDTckBOnowgAf1Yaap6LekPX0_KHLpiZVhGnHy4upkiXudRC8fHcCShNjNqLrhYu90igxl2RQzja-n7rifpsj6RU2kmJVXGWpbYwXVcDpZL5KDHMECY4kDGRkpzZIZDURiBOyrPgADMBFBLH2Je-YXc9zibD3oGYBb618L-WakX4aNOL6dxflQNtGt7wBbU0Zqpt7l6A28X2DkPhBR2llkmAKgyJ6gDEXpeN8WW0iitLEOtd_Ze-R3vtxxMxGjYANZrp04R12tA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مصوبه منع شکایت دانشجویان و اساتید ابطال شد
🔹
مصوبۀ شورای‌عالی انقلاب فرهنگی که امکان شکایت دانشجویان و اعضای هیئت علمی از برخی تصمیمات دانشگاهی در مراجع قضایی را محدود می‌کرد، با رأی قطعی ابطال شد.
🔹
سعید فدایی، وکیل پرونده، گفت این مصوبه مانع رسیدگی دیوان عدالت اداری به اعتراضات مربوط به پذیرش دانشگاهی، بورسیه، نقل‌وانتقالات و آرای کمیته‌های انضباطی می‌شد.
🔹
با ابطال این مصوبه، مسیر پیگیری قضایی اعتراضات دانشگاهی در دیوان عدالت اداری و سایر مراجع قضایی دوباره باز خواهد شد.
@Farspolitics
-
Link</div>
<div class="tg-footer">👁️ 2.38K · <a href="https://t.me/farsna/439259" target="_blank">📅 19:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439258">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHYJYLGIkVENeZVaJu3cKcYbC2nU5kq4oLtgZUZGTgYf5f15YpeoF2VqppXy27vcJJUqynWmeQkFX1PT-kB39Ws_ERqBGZwVNV27u42gfedyQsk96hgn-7lmRGwSSkHgPeLgchhkt3QdVLE03E1UuCn3-uf48CnxY8aTvuNSWQF0Hp5jZtp1DTNXX_UVZbwFAPskmao_oHBhdJbQAo-e0qGr6Vei_02yJSQL5aLw7zR83Pke96Y4zJUFmzoLENjn6ySUdK3XbPc1B1N5oNsCInqTwFFKE3NHYdIIO6ylpOdv5llyIPssorV_wXLUvHCDBcT_HiRRvnVOeViPaAcpBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اول رئیس‌جمهور: فرماندهی رهبر معظم انقلاب و وفاداری دکتر پزشکیان به نظام بی‌نظیر است
🔹
فرماندهی مقتدرانه و حکیمانه آیت‌الله سید مجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در شرایط جنگی، ضامن اقتدار، امنیت و آیندۀ روشن ایران است.
🔹
رئیس‌جمهور نگاه خالصانه،…</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/farsna/439258" target="_blank">📅 19:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439257">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1i46lu851RkIjENphYpHwf9KgPCFNw5hjKOVyRX_rcnqz9Ijh7S5_8Ew_Ps_bMaM9AARfyN2DZMpUkJmW3abnw2bvAlP31HKlJy03PdEMuXt5IRULDYTulG1W1bW6JwvdXpANRidZWHY58rBOUaOZGNlDektHIKXYjBYAxzf2se2tzWV04VdKbmNh_BdqM2bz5H-F904tPu9XDqqdKCxr1H-7p6_5WgyY3jZt7aCuuShXQy_pzflkm14Cji2TR7wKPj2xZ0Q4sW6vCflAaM7ttCu65bgKj025o7eVsoudNS0s8zzBPXZ8R_UgIXkMBCjVbcgyv8_2KGgGktUnFpTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محیط‌زیست بخشی از منطقۀ حفاظت‌شدۀ بهرام گور را به یک معدن واگذار کرد
🔹
شورای‌عالی محیط‌زیست محدوده‌ای در ضلع شرقی و جنوبی منطقه حفاظت‌شدۀ بهرام‌گور در استان فارس را به‌دلیل آن‌چه رفع مشکلات شرکت گوهر‌زمین عنوان شده به این معدن واگذار کرد.
🔸
منطقۀ حفاظت‌شدۀ بهرام گور معروف‌ترین محل زندگی گورهای ایرانی است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.13K · <a href="https://t.me/farsna/439257" target="_blank">📅 18:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439256">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac10398c9c.mp4?token=kMXnmKQW4Z-4-qLdtOFGF6AA2h0XIXwWcR1gLgqRfcuPJa-i67w7ONugBtkChNNkk1IflvZWazyAULVE72E8P3B3sUItqpeG0nrS1ffjRXRCWd-61qahtNEp2AW7ulX89aV9iJlnheZYT9PaAllN3673OOcroi3xjAdFZ2tR3D6wSYQxdWafvBiUGtW6DleYRkOb_r-5tzq4_wlo56ZLuh75ctkd47Fq0ciEsQQoSTmmnOv-mtV4uKehvYHAH-e_bd00lJbWCGYZjxigVFuWUWmbxdg3aYpWlF7ogh-9pmJsikkrY2D-NUrDCy0SyW_yF67oRUgehgVOk43MrrIb8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac10398c9c.mp4?token=kMXnmKQW4Z-4-qLdtOFGF6AA2h0XIXwWcR1gLgqRfcuPJa-i67w7ONugBtkChNNkk1IflvZWazyAULVE72E8P3B3sUItqpeG0nrS1ffjRXRCWd-61qahtNEp2AW7ulX89aV9iJlnheZYT9PaAllN3673OOcroi3xjAdFZ2tR3D6wSYQxdWafvBiUGtW6DleYRkOb_r-5tzq4_wlo56ZLuh75ctkd47Fq0ciEsQQoSTmmnOv-mtV4uKehvYHAH-e_bd00lJbWCGYZjxigVFuWUWmbxdg3aYpWlF7ogh-9pmJsikkrY2D-NUrDCy0SyW_yF67oRUgehgVOk43MrrIb8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۶ فرودگاه کشور میزبان حاجیان می‌شوند
🔹
در عملیات بازگشت حجاج بیت‌الله‌الحرام به کشور، نزدیک به ۳۱ هزار زائر ایرانی طی ۱۱ روز و با بهره‌گیری از ۹ فروند هواپیما به کشور بازگردانده می‌شوند.
🔹
براساس برنامه‌ریزی‌های انجام‌شده، حجاج ایرانی از فرودگاه جده به شش…</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/farsna/439256" target="_blank">📅 18:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439255">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bornmohEY4Qa5HbG7KEsgAHN-0eZcIEyLFf_4xgjpnhsR8rlLL3qwi0WHfCd6Do5I1VcXfVbOWHFobJoDoe0w77LQNP3EJtXgfOsiNF-enXuMGWXL-ayHwvk9-ta2PIt1AVOE5DjmxdMkgVDm3mOYAqhfQqNAMLW2xa_cwNaG9cVXUnS2hM9OY_B-vXrBmqvoupnV_7-7VT3NWWGTtpBl-h9cZIkARuSvVYJrsPBA4t9tJ0IoLzmndPtA94CzBm_lGINzr3TvbXWV7wXU4qqoVJ-DBPqujuXyNF0drwsWOhzN-jQjlFkZn2sLYJ-W41CRgj7zynIOP9UgQkqzJol7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل از حضور در نمایشگاه تسلیحات اروپا محروم شد
🔹
دولت فرانسه به وزارت جنگ رژیم اسرائیل ابلاغ کرده که این رژیم نمی‌تواند هیچ مشارکت رسمی در بزرگترین نمایشگاه بین‌المللی تسلیحات اروپا داشته باشد.
🔸
فرانسه پارسال هم غرفه‌های ۴ شرکت بزرگ اسرائیلی فعال در نمایشگاه هوایی پاریس را به‌دلیل عرضۀ بمب‌ها و تسلیحات هجومی بسته بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/farsna/439255" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439254">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShahr Bank | بانک شهر(N@vid)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep6z6GcMxorz6AqfoLKGuKdIKBNnRT6Y45LWzNv9hrt7OHjOX8lTYYhGorIfucLOmVLR8FGSxKlu-tRYxc5UlOyyt2Lb5-9XVMNEJ0xIGzfT1MujH3_bFbXvYC1yUC_cZuFyC0P6j95xe2V5E0U4BE9LyjPmiPSVC-XNDG2Sy6Il-lkZ7ZqaZlUAly1qwzVwtG5w6cpBp1XGlq_qmHKkXEZf_sDEa0V9_-wWJftMgMd6st9iEPx3kMUJYLjHap4Ecb4PYX5Plr3nY6yQW-Zfs8ePlzbCNDTG25JOzVOeEKpJvGWFAfBUKQGQRNVcHDKztw7jnDKEEQWXPZBgP5xFYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو هیات‌مدیره و معاون فناوری اطلاعات تاکید کرد:
✅
«ردبانک» محصول نوآورانه بانک شهر برای ورود به نسل جدید خدمات مالی و هواداری
🔀
حسام حبیب‌اله، عضو هیات‌مدیره و معاون فناوری اطلاعات بانک شهر، از ورود رسمی «ردبانک» به بازار خدمات مالی دیجیتال خبر داد و این محصول را گامی نوآورانه در مسیر توسعه بانکداری هوشمند، یکپارچه و متناسب با سبک زندگی کاربران توصیف کرد.
🔀
به گزارش روابط عمومی بانک شهر، به گفته حبیب‌اله، صنعت بانکداری در سال‌های اخیر با تحولی جدی در انتظارات کاربران مواجه شده است؛ به‌گونه‌ای که دیگر نمی‌توان بانکداری دیجیتال را صرفاً به ارائه نسخه الکترونیکی خدمات سنتی محدود کرد. آنچه امروز اهمیت دارد، طراحی تجربه‌هایی است که در عین برخورداری از دقت، امنیت و کارآمدی، با نیازهای واقعی، الگوهای رفتاری و حتی علایق کاربران نیز هم‌راستا باشد. در همین چارچوب، بانک شهر با تکیه بر ظرفیت‌های فناورانه خود، «ردبانک» را به‌عنوان یک نئوبانک هواداری با رویکردی متفاوت طراحی و به بازار عرضه کرده است.
مشروح خبر را
اینجا
بخوانید</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/farsna/439254" target="_blank">📅 18:49 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439253">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng9S9WkXTuyyV2Yg-swi9f8dokMJVGg0WNo8i5rFpKwioelkYl1so2G2fWyZS9NPPZQCALtyjtIO6roaQy29LOp0pDOpbZMfNE5aD57Wre6p3zKr9aDq9Goche2T5rf-wcIR0YOvZn8c3VCJAy-96H_BB5iexxnaeI3jZ1Thx60D8hTpIRTXy8mb_OS584Pl1y5W2TcsUAGddbR0JbZeP0g074PzIKouL4Mvxd9Vsx0umPixCaa7X45_EYjggOL0k_VB-zGfteO7wmPZodBADd8JvsQZuQb9mITaIZUgJ_MieyJjrbWn_vGTdcWnnrv1kQVvE51RkOu2xbPBRo2hpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
با پیگیری استاندار آذربایجان شرقی؛ محدوده تردد خودروهای ارس‌پلاک گسترش یافت
🔹
با امضای تفاهم‌نامه مشترک میان استانداران آذربایجان شرقی، اردبیل، گیلان و مازندران، خودروهای دارای پلاک دائم و موقت منطقه آزاد ارس از این پس علاوه بر آذربایجان شرقی، در استان‌های اردبیل، گیلان و مازندران نیز امکان تردد خواهند داشت.
🔸
همچنین با توافق استانداران آذربایجان غربی و گلستان برای پیوستن به این تفاهم‌نامه، محدوده تردد خودروهای ارس‌پلاک به ۶ استان آذربایجان شرقی، آذربایجان غربی، اردبیل، گیلان، مازندران و گلستان گسترش می‌یابد.</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/farsna/439253" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439252">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/farsna/439252" target="_blank">📅 18:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439251">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0I2ozWJd4gs2GjAzlpdwd44tp7_AWRwYjyQcCk7nkUiX20yejpjSoyAPre1PJfeqWpBbQrqfqiT_kqouknpNRrtmr2yFt3g0xt-1EOW6yTtYgPgP8BjeuGrVQwnuuXNs6rYelsY25BQRH3GRUQijnvCNDYkY-CBKnHH_4TKKaTO98Mke9hQVd-KFBjASWkPKAY5449fjTVUpxCv70m0CCCEYW1QoNUJC9C56b4csRML9VjAZjlVOdJvbeJXrf6e6rCXzqF4Zt4fDMWxoFJic4_cL0lBsH-MA1aN3n4vW2DQF8QAWJxInbcxLHVDRrwafSspWaZ2QDGPcZZtpqMwzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۸۲ تعرض تجزیه‌طلبان به مرزهای کشور ناکام ماند
🔹
فرمانده مرزبانی فراجا: گروه‌های تکفیری و تجزیه‌طلب امسال ۸۲ بار قصد تعرض به مرزهای کشور را داشتند که همۀ این اقدامات با اقدام به موقع و قاطع مرزبانان ناکام ماند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/farsna/439251" target="_blank">📅 18:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439250">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTfHZ35eVfuYchYgjuj_7FW_Se2kkfW-kJa07gmyK3w8UbXVk5BrxFFFqEHmOWmwM-b2gTElzHpGSf87mPdPVerVen3WjeXCRsnpW1w6J1gy60GepkvN8Yi12fi4qYdf7qUiw9uzz-T470V3GNe-rmfpMh-oSlFD2-LkwXyaZFaTOFm9aczN_Vz1hi4Pr3Bup-mUqdVQs6CborTWptbRW3RgsDR_RUDvyIc-E_KSPPV-3mak32lTUHwfX--q9uvj6nLh7dtDnYwmEXgTnB2W8-9I1Vi30oeHrPyZh0FlHfkpmVXgTpaSCZ5B9r0U4VDNf3rj4WUI9rN9bjoPIs5NvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون اول رئیس‌جمهور: فرماندهی رهبر معظم انقلاب و وفاداری دکتر پزشکیان به نظام بی‌نظیر است
🔹
فرماندهی مقتدرانه و حکیمانه آیت‌الله سید مجتبی خامنه‌ای رهبر معظم انقلاب اسلامی در شرایط جنگی، ضامن اقتدار، امنیت و آیندۀ روشن ایران است.
🔹
رئیس‌جمهور نگاه خالصانه، وفادارانه و بسیار قوی نسبت به انقلاب، نظام و کشور دارد که انصافا این نگاه بی‌نظیر است. مواضع صریح و عملکرد او در دفاع از کشور مایه افتخار است.
@Farsna</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/farsna/439250" target="_blank">📅 18:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439249">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK7tKLcvReU2Cz6TG1AW6F_8iXpomTwyDhrbuwzDZpuH7klTr4KnlQKmz9oPk9sZoZQrLbSrDbEQgDSi3wUZ4sUobW6lYiu02tKmtsWNPXBTzoiY9-dFsXKTb0V1aY5VDeJyQJiugvYgySu-5iAPGjmda4thaNJaWv0QzViszGMBW5uzyfEYonVC0hQuvxm1aDIaIJHnaM8aIBnMul-8NyTlATe4i850u8MuLTrvYu0lEdCLfyTcptBY9hY6R4mtc_C0_072UBYfbEFyw1lI8HiSKO6dpr_n7Btj1JNuRtVv5vrWdf6s5QQy_ZUqaueuw6-GEnt9hy3PyfZUBE0euQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان حملات اسرائیل به خاک لبنان را محکوم کرد
🔹
وزارت خارجهٔ عربستان ضمن محکوم‌کردن نفوذ نظامیان صهیونیست در خاک لبنان، خواهان مسئولیت‌پذیری جامعهٔ جهانی برای توقف این تجاوزات شد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/439249" target="_blank">📅 18:35 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439248">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d88863fe00.mp4?token=trQYJ52CLBahLZcl-ro2WexRg6doZGxCRgE0cfJavqJ3cpgRXrZsiA3qihU9yLJ7ob55LSMtFQ2MT_NahyYMI4tBg_OX1Zx9uVnndhxPNKjbhO8s9e9pYoZPAr65TaizqPEg-xVzVSKIAzrsQ78kMjLNCrIkCyNTYj2-0B5VVjPAijL1GhnT3Lvme4iP2EMgIgzyliZyoz9a3ArBmLB-geJaTbrVCHoY2Zj0XtFBv-2ABAUUpWqrCY-Y0-50dwbC7ZjE-8cYvuAZBH_zeuzvT5wbMLLenot1kTNbyw4_U8vwjLo8zvkOvoFf7KNwpAraTQ1bn85cTM8caVskK0qFVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d88863fe00.mp4?token=trQYJ52CLBahLZcl-ro2WexRg6doZGxCRgE0cfJavqJ3cpgRXrZsiA3qihU9yLJ7ob55LSMtFQ2MT_NahyYMI4tBg_OX1Zx9uVnndhxPNKjbhO8s9e9pYoZPAr65TaizqPEg-xVzVSKIAzrsQ78kMjLNCrIkCyNTYj2-0B5VVjPAijL1GhnT3Lvme4iP2EMgIgzyliZyoz9a3ArBmLB-geJaTbrVCHoY2Zj0XtFBv-2ABAUUpWqrCY-Y0-50dwbC7ZjE-8cYvuAZBH_zeuzvT5wbMLLenot1kTNbyw4_U8vwjLo8zvkOvoFf7KNwpAraTQ1bn85cTM8caVskK0qFVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی برگزاری مهمانی کیلومتری غدیر: مراسم تشییع پیکر رهبر شهید انقلاب در بازۀ عید غدیر نیست.  @Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/439248" target="_blank">📅 18:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439243">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کشته‌شدن یک نظامی ارتش انگلیس در شمال عراق
🔹
وزارت دفاع انگلیس مدعی شد که یک نظامی این کشور روز گذشته در یک حادثهٔ آموزشی در شمال عراق جان خود را از دست داده است.
🔸
وزارت دفاع انگلیس جزئیات بیشتری از دلایل حضور نظامیان این کشور در منطقهٔ کردستان عراق و دلیل کشته‌شدن وی در این منطقه ارائه نکرد.
@Farsna</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/farsna/439243" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439242">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363a2fe1bc.mp4?token=N7fI2HOGmQ2AG4AgNpP__529_G03LT1EU-qJGGSXt1Kn9axHx7FtJ7frZC2zQ2MCkjoXgfvz54SuwFJKRvk4eZZ4LEGlc47WFTzviOALd5A8v3ieBl7xRM_ykaqb2Xk31UEpNiAby9h5YGkeOvJ65sgttYpSxG_VdXjv4UpigAYHVmhbwHrpgg76a7lVqRsSmzM5q4klAGOdC-g_NYIKiDLnTRw0aEAd89mkLZQdNwViHCwRpuMYMBqdz8orDBsTxUKmhPwIOC1relpg1hi_VAMjrKm_nTfo2CoXd8CMzVd23JkHGGnrOD2IE7Z4AxhqXL3-YhSXMiXSI0F6D-Hhbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363a2fe1bc.mp4?token=N7fI2HOGmQ2AG4AgNpP__529_G03LT1EU-qJGGSXt1Kn9axHx7FtJ7frZC2zQ2MCkjoXgfvz54SuwFJKRvk4eZZ4LEGlc47WFTzviOALd5A8v3ieBl7xRM_ykaqb2Xk31UEpNiAby9h5YGkeOvJ65sgttYpSxG_VdXjv4UpigAYHVmhbwHrpgg76a7lVqRsSmzM5q4klAGOdC-g_NYIKiDLnTRw0aEAd89mkLZQdNwViHCwRpuMYMBqdz8orDBsTxUKmhPwIOC1relpg1hi_VAMjrKm_nTfo2CoXd8CMzVd23JkHGGnrOD2IE7Z4AxhqXL3-YhSXMiXSI0F6D-Hhbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی برگزاری مهمانی کیلومتری غدیر: رهبر شهید چندین‌بار در سال پیگیر برگزاری مهمانی غدیر بودند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/farsna/439242" target="_blank">📅 18:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439241">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rm8Bn_olzDrKXX6PZPaV70jDxGYwTSdhZG-guUy1kNVBKvx01iwI9Wr3cvkNCN3UA2rKYDPtDNCWRVysAmw6hUj9griDpDEne7tBEv4Qxa1_Lq_6yCDljXKPpV_sUoMFUyHEI1jVM7mnPrw2VjBFYR4h0fNoUDs14m6EJ-2DmXHCqz4mypRi2wADBL8GmJXoMXqJEit4VhplekJyqkm1wPvI6mNKjya_I7poPFX1Zk5yi427S5OD3nsXPht7WY0_ABFim-S4fQiAtEYEpn0BMaqLMYj-F16hFQwkST8VwRK4zS6mx8arLFMLpi_yxvhwVJuwahDx2G2pjqDl0tnSVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش اسرائیل برای ضاحیه بیروت هشدار تخلیه صادر کرد
🔹
ارتش رژیم صهیونیستی در فرار رو به جلو، مدعی شده اگر حزب‌الله به حملات خود ادامه دهد، صهیونیست‌ها هم ضاحیه بیروت را بمباران خواهند کرد.  @FarsNewsInt</div>
<div class="tg-footer">👁️ 6K · <a href="https://t.me/farsna/439241" target="_blank">📅 18:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439240">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/46161d95d5.mp4?token=N7k2ptVZXWfWemYNjmxycJwiIKIdOrx8YCCYkGnitnvxjw9KsJCz6yPomY-uIXVZSUDSSOWNJcYRKanZS82ebZD_xFv2WtvVm1mG797X1taRBUWDAfIBOnQ1Q5AEsG7twqnmEBmDlHPn2u0V_njKuiYkvsFVMVPTTv9vn2Fn6bvewYPcm2HgsHHhefDcnIDmSt-0069_7wP3V2vCgoxfljV4zvGIk6gSn78Or-82lPWyFSMO4aIoT-mjw40AVgWvl9waiaMn64pizQSE4Pn4OhVNGQA7rs5pr1OYz8CuaJ508LF2REu8Nbk_6bkxvYoomU6yd8G7jMeAz49kSOBaBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/46161d95d5.mp4?token=N7k2ptVZXWfWemYNjmxycJwiIKIdOrx8YCCYkGnitnvxjw9KsJCz6yPomY-uIXVZSUDSSOWNJcYRKanZS82ebZD_xFv2WtvVm1mG797X1taRBUWDAfIBOnQ1Q5AEsG7twqnmEBmDlHPn2u0V_njKuiYkvsFVMVPTTv9vn2Fn6bvewYPcm2HgsHHhefDcnIDmSt-0069_7wP3V2vCgoxfljV4zvGIk6gSn78Or-82lPWyFSMO4aIoT-mjw40AVgWvl9waiaMn64pizQSE4Pn4OhVNGQA7rs5pr1OYz8CuaJ508LF2REu8Nbk_6bkxvYoomU6yd8G7jMeAz49kSOBaBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای تذکر رهبر شهید به تیم حفاظت دربارۀ رعایت بیت‌المال
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/farsna/439240" target="_blank">📅 17:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439239">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-text">ارتش اسرائیل برای ضاحیه بیروت هشدار تخلیه صادر کرد
🔹
ارتش رژیم صهیونیستی در فرار رو به جلو، مدعی شده اگر حزب‌الله به حملات خود ادامه دهد، صهیونیست‌ها هم ضاحیه بیروت را بمباران خواهند کرد.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/farsna/439239" target="_blank">📅 17:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439238">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1383d6bb26.mp4?token=ADCpq8dITsxp02Ns9vJO0kYba3K2ZQ4tW2d3foEI9ZIj6mtne9ckjKPumRMZ7Zd1Td4AMXp2c3_OjkUt6BHz4Up1Sb9XwBNZFiDLmhemBtht02cnwC1oaChf374YMlAco2lELb8WWJHYN0Ha1wu3F2z-bW3wcxIUuxfBjh_xlGQ6kcQt9-doqIwgoANAliEFS6Als6ZKQnjkcZbbeDRiLcf5qcuKKROVHM_Iqs0KyZt0FpCIPklOenfs0TOta8zCZ4R_S6z0LSrwQYT4_2U3Rg4aOpacJwo8DDB7OP0hTmMHVkHbwgGZ9-VvNdTcDKvsuXbSDAKFFew9GNvzRBzfgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1383d6bb26.mp4?token=ADCpq8dITsxp02Ns9vJO0kYba3K2ZQ4tW2d3foEI9ZIj6mtne9ckjKPumRMZ7Zd1Td4AMXp2c3_OjkUt6BHz4Up1Sb9XwBNZFiDLmhemBtht02cnwC1oaChf374YMlAco2lELb8WWJHYN0Ha1wu3F2z-bW3wcxIUuxfBjh_xlGQ6kcQt9-doqIwgoANAliEFS6Als6ZKQnjkcZbbeDRiLcf5qcuKKROVHM_Iqs0KyZt0FpCIPklOenfs0TOta8zCZ4R_S6z0LSrwQYT4_2U3Rg4aOpacJwo8DDB7OP0hTmMHVkHbwgGZ9-VvNdTcDKvsuXbSDAKFFew9GNvzRBzfgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی ستاد مردمی برگزاری مهمانی کیلومتری غدیر: رهبر شهید چندین‌بار در سال پیگیر برگزاری مهمانی غدیر بودند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/439238" target="_blank">📅 17:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439237">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e07cc6e033.mp4?token=PwCwpAEGpFXEx49xvWGvdHiGheUDDZuqZ9tJkU4jklFcW_6aA7Rl3w6M51rOaTZ8fJFT6NrMU8OFC6uKn80m14jHV_EbdImAOmtEAFXqAxIs7FxpnQ5dAuykRaD_0YvG5jj-ZRX1WlkVyobxacxTYGHbB6ZULFOdNcxLyJMeVXsndUXZCkPCsklQHi0E5A-QAfbkslcLZ9UQeXQ53JwWmsPpWj3GSwe-ILtlN-0ZM5_8TO0cJBj3jxuqv67nhNhyQuPoYWS2hUwhIwiY-pkP-Z9I0LbCWutCowVDdYpVjNO-r0YoWBG-25A1aOg1h3spQ-ES54O6SqJxJOH5H8z1fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e07cc6e033.mp4?token=PwCwpAEGpFXEx49xvWGvdHiGheUDDZuqZ9tJkU4jklFcW_6aA7Rl3w6M51rOaTZ8fJFT6NrMU8OFC6uKn80m14jHV_EbdImAOmtEAFXqAxIs7FxpnQ5dAuykRaD_0YvG5jj-ZRX1WlkVyobxacxTYGHbB6ZULFOdNcxLyJMeVXsndUXZCkPCsklQHi0E5A-QAfbkslcLZ9UQeXQ53JwWmsPpWj3GSwe-ILtlN-0ZM5_8TO0cJBj3jxuqv67nhNhyQuPoYWS2hUwhIwiY-pkP-Z9I0LbCWutCowVDdYpVjNO-r0YoWBG-25A1aOg1h3spQ-ES54O6SqJxJOH5H8z1fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فرود پهپاد حزب‌الله روی سر سربازان صهیونیست
@Farsna</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/439237" target="_blank">📅 17:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439236">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e10313c68.mp4?token=uNCYamk7y1ojwJRZdi1E35d5bXJ75MhdlclUzmwN9pqHcpFX0Yk8TwMZi8-V-FmanbSU_ZNE77FX7ToI_7QSXlm6OYXcosl-oX36vnCcu7OmhNXtvKFC9AI7kzwWX4ZBgjA7r9PNU7EPM8mbjYfOAggZs8b-azaMrPJyGs2K8u6lP1may60r0BDESFTV_lj0WhNLbL3KsC7nzHlO5xqLZY2D6CvDRFEEu4RLxuewzE_Om7SXU9nRPlg8fmyL3r0JeGISpJsUSi5E1r6yCKn48dFYLcmLwusDrJsCGMsTPziKne_IEJY3nEhqb1Zhsh2OvluwJJt1aMaLlwYiEpf_pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e10313c68.mp4?token=uNCYamk7y1ojwJRZdi1E35d5bXJ75MhdlclUzmwN9pqHcpFX0Yk8TwMZi8-V-FmanbSU_ZNE77FX7ToI_7QSXlm6OYXcosl-oX36vnCcu7OmhNXtvKFC9AI7kzwWX4ZBgjA7r9PNU7EPM8mbjYfOAggZs8b-azaMrPJyGs2K8u6lP1may60r0BDESFTV_lj0WhNLbL3KsC7nzHlO5xqLZY2D6CvDRFEEu4RLxuewzE_Om7SXU9nRPlg8fmyL3r0JeGISpJsUSi5E1r6yCKn48dFYLcmLwusDrJsCGMsTPziKne_IEJY3nEhqb1Zhsh2OvluwJJt1aMaLlwYiEpf_pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارخانه تولید مواد آتش‌بازی، صحنۀ آتش‌بازی شد
🔹
منطقۀ ساحلی سالینا در کشور اروپایی مالت امروز صبح بر اثر انفجاری مهیب در یک کارخانه تولید مواد آتش‌بازی لرزید؛ انفجاری که ستون‌های متراکم دود را به آسمان فرستاد و به املاک،‌ ساختمان‌های اطراف و خودروها خسارت وارد کرد.
@Farsna
- Link</div>
<div class="tg-footer">👁️ 6.85K · <a href="https://t.me/farsna/439236" target="_blank">📅 17:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439233">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sm1IC4yLg8tyjVL7Y8XZTbVW8kW8ETWw6RAL9fvajq6EKX4MSBYg9cRfXgR37W5rCl9xx68t88seDv9FVTwACTAZwZVLMlWCjb-TQfYayp9iAbEALPe-sR7MmaCTJQzFUCKHCsx6VMUFVWEKlCN1zt1zQKOCzckeATzdtKui4gvquQJDbKbdtjVvaNDDdN8ngP77qQC7v6RKl2m8xiOkKKGlAY3q1uIR9iB8Hsm_A-t4Nh_cvDLGimC8yW5y8cNW_6HzQzIXWKAfVwWKG64lIxCft7WhULfugTteIB_bmTeBQPR4FP40c6QMCZxQfMgAP0Op_-xOxdfR1NZQpVWYTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DRrVPql7Zrqdwcx4SDdz5DzgFNEsxnJ4pQUhe6bSrVpljnPYXkVZ4ZS4vaRhzSkMYtlsnrtb0ESgY1KhXWUkTSZkgugTG5nMNW6Mm0AnR3vO0lTbjSccdIzg9VUwz14dAqUb1XbUYRtAhCESEu2HTdNRPCrsNqETYUrZyFkLrZL3nA3mMOcoHxtljHkKeATQoYzkO4vXUL8z7XbOYqMbwUt-H1AOMWjnf7eOlwJMtH5Pr4tEtHgHKK-5gTINZLWj6UwA8LupVDzL05tKTJbwdCTNGoMh9W6yTEc8HXH-TGnnwNYnpqCqieGVLcnIv9okkUcf63mY568AGo6UkESa4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lvHysmqLbnMZ2xpNMISLTg5HPmZ44zqYLZ9gRF3buQ_P-lla6unLXPOziFsEpHKgWGL9iAnuGpWWnUkNR0HIfn32D-WZ3b3icD_dZc7I655nCO8ZY03i3a4ub6NwPSLwIDMuCqdoJFqGvkgzX5Zy3LRytMldTSG9-YckkPTmkwPArEPNk17B9kiAemEI8CzjwbFsptpcTnqoe07HwS5l2FJlytgVHbzezEVoB78ll3OJFSDAKolrJoZRM1Ofudyub1oi5pUCwl8sv8vMmqjdo5ZMg1wd4bv8caWf6n5a1HMLN0fCorVLeVhrqoEAXMUl81Hyf_kR26pK-IhtfaUGVA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
ابلاغ پیام رهبر انقلاب به خانوادۀ شهدای مدرسۀ میناب
🔹
حجت‌الاسلام وکیل‌پور، نمایندۀ ویژه رهبر معظم انقلاب، در سفر به شرق هرمزگان با خانواده‌های شهدای مدرسۀ شجرۀ طیبه میناب دیدار و گفت‌وگو کرد.
🔹
در این دیدار، پیام و سلام رهبر انقلاب به خانواده‌های معظم شهدا…</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/farsna/439233" target="_blank">📅 17:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439232">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8251471bb7.mp4?token=ak7wLGix58YS6fzTS7fqV8citgpcNpJfflgiztVJlRoxy91oCbcy_EgfLCHqxN8ARrOmHX_eizjyHHtod_KUzYH4WmNiqDreooGaZyi20wjkBHa2M3J4pW3swbUVtBWGvA4ia1jU2-H92DvZgjTZC6Xn2vn3fj-Ht0wru29-KJkB3abtUg-_Q8HniPPvPUWLs3cOpXk2gP6AO-HBSWcJeFoi18w6MDao6R52to_WTWw3D0BLPOqx5L3NKxdcf5i-ZWczyEpUuGrV-NBs3E2N9-ijOjyGB6Eo5CK7DjUhS8tysNZg2mdENrtJNFVgFx-tnMfW4byxuss-j4YjIQFw9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8251471bb7.mp4?token=ak7wLGix58YS6fzTS7fqV8citgpcNpJfflgiztVJlRoxy91oCbcy_EgfLCHqxN8ARrOmHX_eizjyHHtod_KUzYH4WmNiqDreooGaZyi20wjkBHa2M3J4pW3swbUVtBWGvA4ia1jU2-H92DvZgjTZC6Xn2vn3fj-Ht0wru29-KJkB3abtUg-_Q8HniPPvPUWLs3cOpXk2gP6AO-HBSWcJeFoi18w6MDao6R52to_WTWw3D0BLPOqx5L3NKxdcf5i-ZWczyEpUuGrV-NBs3E2N9-ijOjyGB6Eo5CK7DjUhS8tysNZg2mdENrtJNFVgFx-tnMfW4byxuss-j4YjIQFw9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقوع انفجار در نفتکشی در آب‌های عراق
🔹
العربیه نوشته که یک نفتکش غول‌پیکر با پرچم پاناما در آب‌های سرزمینی عراق دچار انفجار است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/farsna/439232" target="_blank">📅 17:13 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439231">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7422b8693.mp4?token=NVVk17TaTnq0Mh2xIAlH2VKUIlnA9r2jb0t_Fq2WgHm6knFWbsSVwlsfYgaogCol87qt7Z9CG7ZZqY81s-E5KEs6_6kEO8tBjvppZUetqSj2z2twSze-HHfVg6GGgyoacnBOZvdMDS72MOiKFGKM_AiycnYuy6TJ6cY1hsaoii4WS0jkIqQjfe40rO3n_iUowZhatndJwtMPyUAJn7v06dxKuQz-7s6SdJMgq8oyP4U14qUG_RwEIqZTys5bytJ1HZvHzvNbCdMUFeTVHun79YRTPAtrDpuob-9WOHBgo7RaWj5DCaGg0sf9nhca27vVCf-vezDJnQOCSwvrJdYMgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7422b8693.mp4?token=NVVk17TaTnq0Mh2xIAlH2VKUIlnA9r2jb0t_Fq2WgHm6knFWbsSVwlsfYgaogCol87qt7Z9CG7ZZqY81s-E5KEs6_6kEO8tBjvppZUetqSj2z2twSze-HHfVg6GGgyoacnBOZvdMDS72MOiKFGKM_AiycnYuy6TJ6cY1hsaoii4WS0jkIqQjfe40rO3n_iUowZhatndJwtMPyUAJn7v06dxKuQz-7s6SdJMgq8oyP4U14qUG_RwEIqZTys5bytJ1HZvHzvNbCdMUFeTVHun79YRTPAtrDpuob-9WOHBgo7RaWj5DCaGg0sf9nhca27vVCf-vezDJnQOCSwvrJdYMgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تسلیم اعتبارنامهٔ هماهنگ‌کنندهٔ مقیم سازمان ملل به عراقچی
🔹
کریستین وی‌گاند، هماهنگ‌کنندهٔ مقیم سازمان ملل متحد در ایران عصر امروز و در آغاز ماموریت خود، با وزیر خارجه دیدار و اعتبارنامهٔ خود را تسلیم کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/439231" target="_blank">📅 17:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439230">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس معارف</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5242d357.mp4?token=o0XK9cl7457f4UsztaJtxXM6tALq6nOyop72s18B7twY5Oertyw-PkP5L8fDw-VAutTYDLLBRspgQVNLdCpWKwtM_B4W5krNsl6cC-nGpWrexTyosmLwb72hqCB89XLLWEZZwSTFiLzg2wUNqBdpD0oGmqpGz62MxWLhKBg0xO6XkJ3cOFgmZDEDSCBWqUIHoOzu9TuV-LnRFfO-3bcZB4d_xNQ-C98nyIEysUnO61CjruZ7gPlnQ-BG0bPoJ_1nRROyUXN9m81lOl8Dp_-efbuxLx-iA2hrybxkF-TqWU1j96NHkxVLAolUgiQRwyH0XMZf6fVNhzTg3VotNbJusg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5242d357.mp4?token=o0XK9cl7457f4UsztaJtxXM6tALq6nOyop72s18B7twY5Oertyw-PkP5L8fDw-VAutTYDLLBRspgQVNLdCpWKwtM_B4W5krNsl6cC-nGpWrexTyosmLwb72hqCB89XLLWEZZwSTFiLzg2wUNqBdpD0oGmqpGz62MxWLhKBg0xO6XkJ3cOFgmZDEDSCBWqUIHoOzu9TuV-LnRFfO-3bcZB4d_xNQ-C98nyIEysUnO61CjruZ7gPlnQ-BG0bPoJ_1nRROyUXN9m81lOl8Dp_-efbuxLx-iA2hrybxkF-TqWU1j96NHkxVLAolUgiQRwyH0XMZf6fVNhzTg3VotNbJusg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
میراث عظیمی که امام هادی(ع) به ما دادند
@FarsMaaref
💠</div>
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farsna/439230" target="_blank">📅 17:07 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439229">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
هشدارهای حملهٔ هوایی در چند منطقهٔ شمال فلسطین اشغالی فعال شد  @Farsna</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/farsna/439229" target="_blank">📅 16:59 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439228">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d738f7e192.mp4?token=QT3czoN0XB1JpOD99ix9n6rRSN31V0ydF5q2oG1hp7Nf10jHmTNnaeNzufvH7Yo29G8aHZZNgx7kXyhos5LOUBl1ITf1O_PGOrbiu33B4pp5ErCyVovzOUqNEJ6SDPcLBhh0G48P5xJhfUYa4zT-Vu2BbXKez-46y1h_dyPQEhZLdYIFPOWHihm88pIr0AXM0NE_KUhLkUtoBD8lc7zZ57AfxoK_Q8s20tyYlGFEf_Hu4K1gnnIV3M9M-4fQdXE734YDL5l4rXA4SyX06JGydl0ZJD3dzWBlATgu35igvxMBvNZC2Loj2lvUQG998U_8lm9YsVdRTODf24exLHoAJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d738f7e192.mp4?token=QT3czoN0XB1JpOD99ix9n6rRSN31V0ydF5q2oG1hp7Nf10jHmTNnaeNzufvH7Yo29G8aHZZNgx7kXyhos5LOUBl1ITf1O_PGOrbiu33B4pp5ErCyVovzOUqNEJ6SDPcLBhh0G48P5xJhfUYa4zT-Vu2BbXKez-46y1h_dyPQEhZLdYIFPOWHihm88pIr0AXM0NE_KUhLkUtoBD8lc7zZ57AfxoK_Q8s20tyYlGFEf_Hu4K1gnnIV3M9M-4fQdXE734YDL5l4rXA4SyX06JGydl0ZJD3dzWBlATgu35igvxMBvNZC2Loj2lvUQG998U_8lm9YsVdRTODf24exLHoAJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات آخرین پیشنهاد ارسالی آمریکا به ایران
🔹
آجرلو عضو تیم رسانه‌ای هیئت مذاکره‌کننده: در مرحلۀ نخست مذاکرات، آمریکایی‌ها خواستار انتقال مواد هسته‌ای ایران به آمریکا بودند که این درخواست پذیرفته نشد.
🔹
در آخرین ویرایش‌ متنی که آمریکا ارسال کرده، دیگر بحث…</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/farsna/439228" target="_blank">📅 16:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439227">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VTK4qxi5ZsNcw7vUYxX9-d1b2DZK1VO4TYwNT3vW5HmhKiDVuWARjMKMHYlRQTirG1jrPWJMAwytaCIHGe2bVjJmr9sQfyF7B2kHKS0yUaViaqrEjIUGBSgAo2w0fNK1BbZpzF_wtQKAAk_sUxsqNiCB1NL1GsfGduNt6Jy9IsyAqLR4dfgWA4h-TaakAftJDZdwRqCM3ANAlMXdEEsjVUO2MOWvMaDiG6O6hnXhrnD-4ZDCSy_07kd8ypLmGX_CECYYlL6IwPv7IeCxDvADEj9vzKr1vRc9IqWsX02cwL5kUlVufoqQda38q31NxLKEc1bf9PPsdOyZI7wXRU9uRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هشدارهای حملهٔ هوایی در چند منطقهٔ شمال فلسطین اشغالی فعال شد
@Farsna</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/farsna/439227" target="_blank">📅 16:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439226">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c59508e038.mp4?token=QYSsNNY2njZRWdPZ4EzC9JDTTDbViWu5ZmjdHO0RWiT6Yuoko0q2ErqbMf29MDDVDSdWVhRncV7ZVNj9jZxQrMguRnsUkEeIfB6ErwbkQnsclFP6kWVzQ64pTMctDHjNTiAJheao622-NpJ3cA85jum1UY8oGuJpAFVIXmAQtk4ktNFOrtYuale2pbMyyPQfU4dHYZJ1NAQY6DHN5RnDeJjhz9gZW5O5QVkVKM8bMvjJ7iIBup_WQg9glWLPQmVmT6Vxq-W1GLLljyBAITJ3J0eevtPajf6Mf7mCafWabGh3c2BZJURE94BcBZ-rm-sxsdMfuhg9GRfZl0LzFtmCRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c59508e038.mp4?token=QYSsNNY2njZRWdPZ4EzC9JDTTDbViWu5ZmjdHO0RWiT6Yuoko0q2ErqbMf29MDDVDSdWVhRncV7ZVNj9jZxQrMguRnsUkEeIfB6ErwbkQnsclFP6kWVzQ64pTMctDHjNTiAJheao622-NpJ3cA85jum1UY8oGuJpAFVIXmAQtk4ktNFOrtYuale2pbMyyPQfU4dHYZJ1NAQY6DHN5RnDeJjhz9gZW5O5QVkVKM8bMvjJ7iIBup_WQg9glWLPQmVmT6Vxq-W1GLLljyBAITJ3J0eevtPajf6Mf7mCafWabGh3c2BZJURE94BcBZ-rm-sxsdMfuhg9GRfZl0LzFtmCRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حضور نمایندهٔ رهبر معظم انقلاب در جمع رزمندگان در سیریک
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/439226" target="_blank">📅 16:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439225">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پزشکیان: تلاش می‌کنیم عبور کشتی‌های ژاپنی با سهولت انجام شود
🔹
رئیس‌جمهور در گفت‌وگو تلفنی با نخست‌وزیر ژاپن: ایران همواره دیپلماسی را مؤثرترین راهکار برای حل مسائل موجود دانسته، اما متأسفانه برخی طرف‌ها از جمله آمریکا با عدول از تعهدات خود و همچنین اقدامات…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/439225" target="_blank">📅 16:28 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439224">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پزشکیان: تلاش می‌کنیم عبور کشتی‌های ژاپنی با سهولت انجام شود
🔹
رئیس‌جمهور در گفت‌وگو تلفنی با نخست‌وزیر ژاپن: ایران همواره دیپلماسی را مؤثرترین راهکار برای حل مسائل موجود دانسته، اما متأسفانه برخی طرف‌ها از جمله آمریکا با عدول از تعهدات خود و همچنین اقدامات بی‌ثبات‌کننده رژیم صهیونیستی، روندهای دیپلماتیک را با چالش مواجه کرده‌اند.
🔹
جمهوری اسلامی ایران آمادگی کامل برای تسهیل عبور و مرور دریایی را دارد. مشکل اصلی ناشی از محدودیت‌ها و موانعی است که از سوی آمریکا علیه کشتیرانی و تجارت ایران اعمال شده است.
🔹
تلاش خواهیم کرد مسیر عبور کشتی‌های ژاپنی بدون مشکل و با سهولت بیشتری فراهم شود.
🔹
ایران هر اقدامی را که در توان داشته باشد برای عادی‌سازی روند تردد دریایی در تنگه هرمز و حفظ ثبات و امنیت این گذرگاه راهبردی انجام خواهد داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/439224" target="_blank">📅 16:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439223">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1023c192.mp4?token=sVYH4UmHHTRXZFNh57sRjQt_U8mcNl1NG_Tb1echRv4NOSUq0Y9i6_gxqm9sMYxm2JHpxvKp1x_WufXbAWY7CEvPwi2mLw39_GFnG-g-DDOGC5Y_uD1tn373SI2UdAbyG_aC4KnoGrGKm1d0GLPyN2t-Xm-xDiiH_-HhqdK6PMxvMAETEDQ4-C8pkPqJbjOCANbhpIcuVKNJq4EDD2y2uUa7VPk1sm_O42_s5bpTw8YwLA_dPHjzuc7_2Sj6Ttkm9I7cjJfPETqEd1ihXwgHG2KvObmgJHHeg4OF06jgyQhTx6VXvxhFoW7haRSF5RTUy7CVhcq4S05px5Z5bdUAYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1023c192.mp4?token=sVYH4UmHHTRXZFNh57sRjQt_U8mcNl1NG_Tb1echRv4NOSUq0Y9i6_gxqm9sMYxm2JHpxvKp1x_WufXbAWY7CEvPwi2mLw39_GFnG-g-DDOGC5Y_uD1tn373SI2UdAbyG_aC4KnoGrGKm1d0GLPyN2t-Xm-xDiiH_-HhqdK6PMxvMAETEDQ4-C8pkPqJbjOCANbhpIcuVKNJq4EDD2y2uUa7VPk1sm_O42_s5bpTw8YwLA_dPHjzuc7_2Sj6Ttkm9I7cjJfPETqEd1ihXwgHG2KvObmgJHHeg4OF06jgyQhTx6VXvxhFoW7haRSF5RTUy7CVhcq4S05px5Z5bdUAYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف علی یونسی به هواداری منافقین؛ روایت‌سازی رسانه‌های معاند فروریخت
🔹
علی یونسی در نامه‌ای که از زندان نوشته و در کانال گروهک تروریستی منافقین نیز منتشر شده، صراحتاً خود را «هوادار سازمان مجاهدین» معرفی کرد.
🔹
این درحالی است که رسانه‌های معاند طی سال‌های…</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/farsna/439223" target="_blank">📅 16:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439222">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNBMm-_n3R1wC0zlCQGnOWBvDzlI5Ne3Q-taJbwq2VTnGr5TQcjOIUmwUQQV-GQTx_AVTe7JrUBjN-CyDQCRorarUsU0hIh2litTu9kV4nsBjKT7KL_bl_XjUmH3hjjQFkmXV3Ng8T52wA6VpC4mYsBHVufRxDnY739pgPAM91lIbPC3fh-p0lrzyhH1juiBekMQRe8bNHnWUjv1leZOfCVeycsNd6TiavojvseR9M1AOgH-NKjYgTKcFQpLAUZfdIL3c63hF46Bh6nqJrV0bywz1PDslHM5pIF6JVvzprtCxyPJu68gxLk1Ch02aVFDn97YNx_9XLQBty5OCJR2Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: ایران پایگاه آمریکا در کویت را هدف قرار داد
🔹
بعد از آن که سپاه پاسداران انقلاب اسلامی از پاسخ موشکی موفق امروز به تجاوز جدید نیروهای آمریکایی در جنوب ایران خبر داد، فرماندهی مرکزی ارتش آمریکا در بیانیه‌ای اعلام کرد: شب گذشته در ساعت ۱۱ شب به وقت شرق آمریکا (صبح به وقت تهران)، نیروهای ایالات متحده با موفقیت دو موشک بالستیک ایرانی را که نیروهای آمریکایی مستقر در کویت را هدف قرار داده بودند، رهگیری و منهدم کردند.
🔹
سنتکام همچنین ادعا کرد که هیچ‌یک از نیروهای آمریکایی در جریان این حمله آسیب ندیدند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 6.61K · <a href="https://t.me/farsna/439222" target="_blank">📅 16:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439221">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c55155dbee.mp4?token=bu1jXnwRyvuubA51tR7p32EFI0a7hMCJhTf5vmeoq8o8CaOuZfB5V3QmeblUHZJpjKB4xCtSTVyAgJocMc36n4k8mwhpxQQtP0o_VomeDk_jsiuZ6v-sOWGx9EnqwgtzJaYNlEgWf3Fy6A4IfFwBXUTnm8CtVfWFePYqWefZVKUaQ5Yjc9kfeuZpLXDS9WaUmU6emVd9y2vvjTpDHFsa7LCGh5SHoNkZNsw3Bsy4x63UH8OAfh0f6IFqrv2_uClP93t7G42G3r3-OflBcmYtJaEEvTxYievyQCfct78H-LUvgJ1LfgK7UUNnyqAF2zuL4tHyvZfSTgr6YSUyeAFXxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c55155dbee.mp4?token=bu1jXnwRyvuubA51tR7p32EFI0a7hMCJhTf5vmeoq8o8CaOuZfB5V3QmeblUHZJpjKB4xCtSTVyAgJocMc36n4k8mwhpxQQtP0o_VomeDk_jsiuZ6v-sOWGx9EnqwgtzJaYNlEgWf3Fy6A4IfFwBXUTnm8CtVfWFePYqWefZVKUaQ5Yjc9kfeuZpLXDS9WaUmU6emVd9y2vvjTpDHFsa7LCGh5SHoNkZNsw3Bsy4x63UH8OAfh0f6IFqrv2_uClP93t7G42G3r3-OflBcmYtJaEEvTxYievyQCfct78H-LUvgJ1LfgK7UUNnyqAF2zuL4tHyvZfSTgr6YSUyeAFXxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌‌
🔴
حزب‌الله: یک پایگاه زیرزمینی متعلق به ارتش رژیم صهیونیستی در شهر طبریه اشغالی با شلیک راکت هدف قرار گرفت. @Farsna</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/439221" target="_blank">📅 16:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439220">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42ebba9900.mp4?token=l-UNo08mbYf8mWU_c5jeei7Umj-lWnEkwaoyBT1E32vqcob0wqmyBvhmPckMXCKkfJ9AIsu2KhwvBiFL3MHkDYyAbZ66cMH8bF-EymdLAx9uXxEGIaAny36z7z_AxIlSg0667OfupqZkhvZYtKSXBNQM7AD0gnbICZvTbL2e1pYgCwacLYX2IjfWZYhrUQc6O0mrMZKv9HeLKUfNx0FoLdV678XkaSHAZXkPH5krBU_hDljZtRFoDTLXybPmIqhZXWE8DAGDOcHqXpzqpqrB1kyxaY3qC7cDS2MdK7LxwTdzdT4s7aBEUakhM_XDvPFADomi36Caof_KcOcIyi5tcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42ebba9900.mp4?token=l-UNo08mbYf8mWU_c5jeei7Umj-lWnEkwaoyBT1E32vqcob0wqmyBvhmPckMXCKkfJ9AIsu2KhwvBiFL3MHkDYyAbZ66cMH8bF-EymdLAx9uXxEGIaAny36z7z_AxIlSg0667OfupqZkhvZYtKSXBNQM7AD0gnbICZvTbL2e1pYgCwacLYX2IjfWZYhrUQc6O0mrMZKv9HeLKUfNx0FoLdV678XkaSHAZXkPH5krBU_hDljZtRFoDTLXybPmIqhZXWE8DAGDOcHqXpzqpqrB1kyxaY3qC7cDS2MdK7LxwTdzdT4s7aBEUakhM_XDvPFADomi36Caof_KcOcIyi5tcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گفت‌وگو با کوچک‌ترین عضو گروهِ سرود میدان ولیعصر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.28K · <a href="https://t.me/farsna/439220" target="_blank">📅 16:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439213">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flM0A3OhcvHva8WXKh9uSHSXLftBrZdzBU07Vlsk5zWBDhKwV-DqwoiQoEVCleO78tgpJ7mR2iRoJjTw0PEbbg1rNwZIT0FO3OWOJ0L_Uo9F5HBLZB6XmZqybpWL9Lp5y3L0QNkV42toalat1CJ_a1dKAtDbuOZ4RW8SRC0FPWxyEAQtCqmvVKofotkg5ZfCPbMGAkYUvugqHnGpYr5uw7ZCWNmwv48ICO_plOVvqyD2FkX33ssVIY-h3HpVtBEY8g3dJtDjiUsFfi-GCVCq54P_ZIS4Hxo6yas8rBD9jFrFruv-vU5lZvhoTEGA-8wVcSQG5V04ssJ2L8ZGX4yfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HfqIZUp3_ttrz1iJEqV8i4sXwEECyWyMD8UYmOPeC_uT8usFrHfDNVr70jxqpNH7g43TL2IX7P32Ro3pTVrm-Xb8MHI4wcFbS6i-hAAD9kTN3GktYnZQWofpbMBYr9Vp868dgRYO6ON4yBCXaN3DnGWz_tOL3QwQGlHBBAKy83avKSgIqlOLcbHypLqKjGp5uKN04y6R0BQVS73VblI_-Zrx1r_f4u2cR-sNlhTa6O9zIHW5-WqcH9M-YXVF7s89VDii8XUKQC3UcOg1AQ6bfsJGAcHrGq1BRnrm6_w-qU_mFBzYMPvu7F4QwQJDKOetDLP_K8ULAZbydE2bdPIN-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p8fqXiZGzqJLNTKRSXcpi71FCndnZ35LmQfDruthCyuK8CHH_DTisBAqwp8O9N9zF69tzKWz3aq6gbODYkqAIQOpqhv1v0BoZG5gNBuA3gFufN2e52dOCTLv5EJAULBdZuWpO_7ZM2ivobnPfwv6Q9KDR_Uet_YvhWUEOaky4tpo1s9Ce6-fDqCWzhUv3jeWNctgQFUDkq7WDCDVF4R7Xw04JHDGO2oXsUhVsuqN4PElDtQOsYouIYdttKiT42wlyCkeekpem0VKErYq3X3qZf79AEH9zWh-stBi7OfEUQk50TvJpk-BT1DWB6o5XcEVqdinkpbeYDyMqYJGUyhtrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rNyNOWGznv1GJf3Q61Sc3WcJ650bYzRS-rDOOVG9ZZUPaVXCWnjUURaw_r2a7AnhSCIMb25K8vnKDE2UehpvgisAJoO0M2wcR-NYWRcqhQKQ9yz_96QvsMY1dcUKM_ENaHyfzJuYp3Nqu9hEyaMdZwhnA8U78oDOQyZdgJ5FoMosvfaqBvihG24Q1jYo-Nix0tReAbpjnmDKdR5iK9RK8zrmr18K1Dqfa0o47tWkU9x9H1bJwYa6nhov0Zqt1j_HTBMbmk94jPpVgzn6j6Xiw999UpKNWsVCEoPx2puMlPTJfqAcMOFOOqwgVwHaZDYngzI8ZWExMRwJG_22tbH90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DfS-CuUYKQe1A7E5VHTI2sPo7aXkT0qUk16L7Vt_r25g33cPyMXHV9ctfP-3iBolTtOPKVPzkb3jmUT7PIbt3UoRLrhfeqgEB05MmnFVksJhNj9Nl1nBrOp-z7i7YTz-v4k1W8MbVUtDgwMDAdEB0uszeS8hbKwDJoK1Yd1oI9zOwl5zhNvJo0_v57KAiADYEfzY3tCJGBgpxImwCp_MbhKZH55l256n3UCB1xXElnTYob-vKO-OV_J6dIGwGu0lHucSFEHeOX-Uzg6p7C5MSWr6jg22T8nao2z0qkMMOR2qrETqJWQRPKsCHuzHWvOh5ZbU1cNEPOHFn6InrTfUUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gCQUxfypID4QQJ_TzObXBu5soZ8hDRPK69tmYLpdYmGY_urTZQYG6DKEHVdZiuukjrtGjxQS4YiO9VmnvQS8uLirevRtssqkoXKUtvYB9vdk0RMesdiDZOlcs6qkDMtYLsCyy3HIxcYZLWDG_vkwWtA5z65AKMRxw9Bas6wnhQCzh0pMZoPsfmvjxeCNqHEWPaZBT5cd5_aXR0V9MikAuO0PaN8vGldC2BW4oo3HS1eRoYAbxNbS1HVTZteymTGPvtVT_sjG4umsTSNkWlA2_5tu9E4u_pk-lgSjhNI-9HO1hbwbn6H_-m9GNCIVB0ptv3JwxGo_hZiFPLlbM3A3JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ohHirKb8B7AU4eC9BHIAyTwUgpKWYNTLVxXP-33IJhdYNXnAkqKepR5aszc24pjpr-KIO6pHrTObh5N0R_9nMc7BICxTjtJOgyyCFZ7Og5447jY-fad3WcsL_NfajTl5EAwncqwCKAZU4xoWX6_Qhxj7fGTSVOozQKmjHcN8y8nY30ixDV4EZacJNEcSrB4nSiqSKN54AUCLfuvq3VCCFE_mayMC_-LBfn7wef_P9B__BrDDIQBiH4Qw45m12bU3xOFO7_tPi2oIkCNz49Kpul6ZE0ya2qYEnLoF8uK15kRRH4syAsFLQ_BGlfE9UfilVata4xEeg0hcSPHDtUxoeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: آخرین وضعیت تفاهم پایان جنگ این است که تبادل پیام ادامه دارد و به جمع‌بندی نرسیده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 7.73K · <a href="https://t.me/farsna/439213" target="_blank">📅 15:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439212">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34a7935398.mp4?token=IzFBzEOSK4KPG203PrjA7WFhDTZ_XWvvEDrVfIGRIXR18TedMOadYhzPqIcuA-ekPMPul6GmnQe0Irh5rXqfLf0_SJDgj6VTEbBMNv4eoxtD-00LBQt3r7dsHHAMXWu-WWPjXpZvuApM-3Ryoi7iNUE2vS3Lw4FlAdziT3RRIBTwxosuFsbz1jVvNkM3T0ivwBCQIJB7x6X6xEp5w34UDee7V2VWvz-tSslPATgC9PbJBOXiXRYih9uo7_eRcmZytAh3fZnY7LYRv_tzD_mvh2eTM-OfjqTySe02o8VuCP3R2r4E4NOYHQbrsOw1qbcuAaBlyWNSbDet-07yQW2kEGlt7nQIuoDt7rxml0Q7a6YlK-8gbbKIHyKZtGOhpMs-PqyPLg2lINRskD11aBlOskG0TOLL1M3nQ-hmTLR5JmYT19CxgFwD-Wpxwk3GE67znsZel0KoZk0FXklq_V4pyQtTlUKNejrLMCHVRtGz5CXULnDT268dfWU0ifHPSTSjSG6HeZDg2ed2B9JzkuBCGZRc7-u6N0Nvbisjxf03Hyvd5N4jZwa5DGgVZUnsNzm6QhgBLnocioo1lIDEEtnr5jxgWrhMWDI9lmBV8a44rNPE6t4CNfzgFHPyWnbgft-Wy40-TlhD0DfJFIcX1C_9XXlrpyDs_sKHhubLxXM1YHU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34a7935398.mp4?token=IzFBzEOSK4KPG203PrjA7WFhDTZ_XWvvEDrVfIGRIXR18TedMOadYhzPqIcuA-ekPMPul6GmnQe0Irh5rXqfLf0_SJDgj6VTEbBMNv4eoxtD-00LBQt3r7dsHHAMXWu-WWPjXpZvuApM-3Ryoi7iNUE2vS3Lw4FlAdziT3RRIBTwxosuFsbz1jVvNkM3T0ivwBCQIJB7x6X6xEp5w34UDee7V2VWvz-tSslPATgC9PbJBOXiXRYih9uo7_eRcmZytAh3fZnY7LYRv_tzD_mvh2eTM-OfjqTySe02o8VuCP3R2r4E4NOYHQbrsOw1qbcuAaBlyWNSbDet-07yQW2kEGlt7nQIuoDt7rxml0Q7a6YlK-8gbbKIHyKZtGOhpMs-PqyPLg2lINRskD11aBlOskG0TOLL1M3nQ-hmTLR5JmYT19CxgFwD-Wpxwk3GE67znsZel0KoZk0FXklq_V4pyQtTlUKNejrLMCHVRtGz5CXULnDT268dfWU0ifHPSTSjSG6HeZDg2ed2B9JzkuBCGZRc7-u6N0Nvbisjxf03Hyvd5N4jZwa5DGgVZUnsNzm6QhgBLnocioo1lIDEEtnr5jxgWrhMWDI9lmBV8a44rNPE6t4CNfzgFHPyWnbgft-Wy40-TlhD0DfJFIcX1C_9XXlrpyDs_sKHhubLxXM1YHU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گشت‌وگذار پلنگ پارک ملی گلستان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/farsna/439212" target="_blank">📅 15:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439211">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frhrPTxMmwu2IPVFgcwbWze2UBIeFt_OGQSyboK3G72HRs24jqO6FylgPrmK0f0KCg1vOqNrpMhmBGdW2UIHoPQZ0Cw9yFPDH0wF5bmyWTF1g_ZUWWJQcMQXZqG8acUVCgmFglIXdqun-JmREdu9J1GMC1OIwHpHHvGuVjACX7lAFlTy3-XniUfXwzD0G00cx3HN5Z94TyPqG9ZcMRMRDEeiqeXpyqRWhZ8oZyjViTlyofRHPvvOTA70pCa4QYGgiw1h71oIXd-qi1sa0Dn8WVU24tkQdS0nO9n_0TdFQrMP8I0D82jZhaOJmbbPOeqQT9jcxRRvRHE_GbL4G6U9DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
آملی لاریجانی:
مردم ایران در کنار مردم لبنان در جبهه مقاومت ایستاده‌اند
🔹
حزب‌الله لبنان نماد مقاومت مردمی است که در سخت‌ترین میدان‌ها، شانه به شانه ملت سرافراز ایران ایستادگی نمود و با وفاداری و فداکاری، تاریخ را رهین عظمت خود کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.42K · <a href="https://t.me/farsna/439211" target="_blank">📅 15:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439210">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromکانال ورزشی فارس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxBT9mk8MWW3qYX0PZYorNUJV8HrkgadS-nqFusykyQkqt46EPz6wcSUfhlUzg3nLoO6Y5t_J9q4KM1QSH-FvKfvp2tZ-e37Z-za_U69c5KQTmOAokKvSYNEPnsB-HZWRCYb84AfcbRY3F9taQe2sM1GDOtRgV1J3gUOzMixfh_MFizqD--OSnN8gJ0g_F2hTnqvUfc1qlmCSsbGLanUiWC_rIlVfm2rthRuMBfkZ26MIZXYxEyzvMS2277AccQe9AeFMQIYef6iLh8VqykKkgdhIsF2hGadkdlie-0lhZTqWrueO1kBGBXuf_dtEzUbVHV1ulkD3qA-dDkdpVvdPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
۲۶ مسافر ایران در جام جهانی ۲۰۲۶ مشخص شدند
@Sportfars</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/439210" target="_blank">📅 15:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439208">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94e235c0d4.mp4?token=fF4OeOqwV9nJ1DQRNoyuRyabGxit6lrY_aiHkeWSckcMO8-D8ojmG-Zlhzhc0vmbMQiRyeh6LLwTXGpicTZCP3q3vkJJehQks5kC-xijrAcbI_Hql0hxg2R0izhQZ0W9Ru58s8pltCkLalphJ2P7-PGaFTjxQCSRm2Lk6p7IP8iwEF2qtjjyWumEfZF1IZt-H4T1JX2xfThPdwA8zs5kd3fSPo5xjc59raXb5on4P4_NrxyEeXkqHc0dLy1gSKXsbt9qWQvfwhwAmMulZkvZgzEPuA_p5Wpu9_ijcyPXuglEnUS3hBltP6yIV5a8p9QbyGhtdCAZCTo1esVTg2wuLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94e235c0d4.mp4?token=fF4OeOqwV9nJ1DQRNoyuRyabGxit6lrY_aiHkeWSckcMO8-D8ojmG-Zlhzhc0vmbMQiRyeh6LLwTXGpicTZCP3q3vkJJehQks5kC-xijrAcbI_Hql0hxg2R0izhQZ0W9Ru58s8pltCkLalphJ2P7-PGaFTjxQCSRm2Lk6p7IP8iwEF2qtjjyWumEfZF1IZt-H4T1JX2xfThPdwA8zs5kd3fSPo5xjc59raXb5on4P4_NrxyEeXkqHc0dLy1gSKXsbt9qWQvfwhwAmMulZkvZgzEPuA_p5Wpu9_ijcyPXuglEnUS3hBltP6yIV5a8p9QbyGhtdCAZCTo1esVTg2wuLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
رهگیری و انهدام یک فروند پهپاد دشمن در آب‌های سرزمینی ایران
🔹
سپاه پاسداران: بامداد امروز یک فروند پهپاد MQ1 ارتش متجاوز آمریکا که با ورود به آب‌های سرزمینی ایران قصد انجام عملیات خصمانه داشت، بلافاصله در رصد و هدف موشک‌های پدافند سپاه قرار گرفت و سرنگون…</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/farsna/439208" target="_blank">📅 15:18 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439207">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nW_wJMzuHSkHFicZIzP9RkEP3uG3iEDiI6VyP1XHZ1NVPV-agNfAGszfJybrNsyoEwQf0v7gDF_JJM_KNSEemSJLdqquM_4Yjwl8u3lXluBlc5tE_cJpxBe0ivVuDUcpNT57YtmxYklxxlh_VcaXc_uZYNVN18-_fRLqj5OPWSOEgNDA8pT-lvtK7oLrNFZTjR5BKAkm847UtjLHIsvw_oKBkfMYVnBTOEombz_cgONYeGOCQc79fTnNKwRf6QyPmXjQc0rdhiADiwvS2DHLJh3VEZjBC1SgK8kZ1v4Dn8fdvOJivUWSUwWai-Oa6ADPKO7LBJRr4FvGyFNv8IQUyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جنوب لبنان این روزها چه می‌گذرد؟
🔹
جنوب لبنان این روزها صحنۀ تحولات سرنوشت‌سازی است. ارتش اسرائیل با گسترش حضور خود در مناطق مرزی، ده‌ها روستا و شهرک را به اشغال درآورده و موج جدیدی از آوارگی را رقم زده است.
🔹
منابع صهیونیستی از استقرار ۵ لشکر نظامی در مناطق اشغالی و کنترل حدود ۵۷۰ کیلومتر مربع از خاک لبنان خبر می‌دهند؛ منطقه‌ای که در برخی نقاط تا رود لیتانی و قلعۀ راهبردی شقیف امتداد یافته است.
🔹
همزمان با تشدید حملات و صدور دستور تخلیۀ مناطق گسترده‌ای در جنوب لبنان، نگرانی‌ها نسبت به تکرار سناریوی غزه و حتی اشغال کامل جنوب لبنان افزایش یافته است.
🔹
با این حال، حملات حزب‌الله متوقف نشده است. عملیات موشکی، پهپادی و کمین‌های میدانی مقاومت همچنان ادامه دارد و حتی تحلیلگران صهیونیست نیز اذعان می‌کنند که گسترش عملیات زمینی نتوانسته از حجم آتش مقاومت بکاهد.
🔹
در کنار نبرد میدانی، حزب‌الله در جبهۀ سیاسی نیز با فشار جریان‌های غرب‌گرا و حامی خلع سلاح مقاومت مواجه است؛ موضوعی که برخی ناظران آن را عامل افزایش خطر تنش‌های داخلی در لبنان می‌دانند.
🔹
لبنان امروز در نقطه‌ای حساس قرار گرفته است؛ از یک سو اشغالگری و بمباران، و از سوی دیگر مقاومت و نبردی که همچنان ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/farsna/439207" target="_blank">📅 15:15 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439206">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmClIBDM1v_uiCJhhw0CnJo35T6Ct0oisQ-4VjMm-MQO1qRCT45aZ1UpEYLO6prZpqW5bczYLuZqPPFOmWfR1dH8UxvYvZynkzRafSrKtZZjmVU4fgDVp2FPbkZZ-R8QZm1qf96MizhGl10TttPKCxRlQEsgyAMhMMQ9cd87vGC6jkC0VIUcTWuEFuGiydi1Mg46F9cdPGR-GY2G2DkG7nYcTrfjqZ8TKf9xyEuw8CrNSq1xgSAATvmsiY9LtcsvbbyId-q8l-HgnP6yKgETqRUJOwxUnjciZvUIeu3kGGwkGEid0YuInb8RsxzTYjXu2JombtSqmltRxRWbLNH2EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
مجروحیت ۱۳۷ نظامی صهیونیستی در ۲ هفته
🔹
ارتش رژیم صهیونیستی: در ۲ هفتهٔ گذشته درپی درگیری‌ها در جنوب لبنان، ۱۳۷ نیرو اعم از افسر و سرباز مجروح شده‌اند.
🔸
ارتش رژیم به آمار کشته‌شدگان خود اشاره نکرده است.
@Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/439206" target="_blank">📅 15:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439205">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4c7b1bdb6.mp4?token=dRqrSOUgTPfvgXqX1UTJs0L16a_XxkUsWMZTuV9622syhuuiFuRUQIKl8AWkuF7XVYlO6jrWpS2Abk5S2h4A7M9LG1_VGJHac4XL3oC-PvRWMzA1ZKzkDK_K5Hg4n9D8RGncLKxQ_p8vsCENB2WonUuq9ylgkdzQVVsNds_a0ptnRJURKndZrPb3Km1OdyR5gZJuRFYqU2xinSrF_OCBh-azZSx0hlDDq74ezTXpg0z1v4-u4TdBHacG3HKFUwn0ldpgr9_Pj5Rri8QzOcAFGgS0jhlJUWCbf6t-3l-Xb1n6y_7auArdidvxT6h0KQZBtQF4jhHZnp2LjDoKrkZkgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4c7b1bdb6.mp4?token=dRqrSOUgTPfvgXqX1UTJs0L16a_XxkUsWMZTuV9622syhuuiFuRUQIKl8AWkuF7XVYlO6jrWpS2Abk5S2h4A7M9LG1_VGJHac4XL3oC-PvRWMzA1ZKzkDK_K5Hg4n9D8RGncLKxQ_p8vsCENB2WonUuq9ylgkdzQVVsNds_a0ptnRJURKndZrPb3Km1OdyR5gZJuRFYqU2xinSrF_OCBh-azZSx0hlDDq74ezTXpg0z1v4-u4TdBHacG3HKFUwn0ldpgr9_Pj5Rri8QzOcAFGgS0jhlJUWCbf6t-3l-Xb1n6y_7auArdidvxT6h0KQZBtQF4jhHZnp2LjDoKrkZkgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
خبرنگار صداوسیما: با وجود اعلام آتش‌بس، به‌دلیل تهدیدات رژیم صهیونیستی، مردم درحال ترک ضاحیهٔ لبنان هستند
@Farsna</div>
<div class="tg-footer">👁️ 7.91K · <a href="https://t.me/farsna/439205" target="_blank">📅 15:00 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439204">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
سازمان پخش اسرائیل: حزب‌الله از بامداد به شلیک موشک‌ها و پهپادها به‌سمت شمال اراضی اشغالی ادامه می‌دهد.  @Farsna</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/farsna/439204" target="_blank">📅 14:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439203">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIBDmQqGMnyPMyGu3WD7LDA_z5mbgj9FbpK_WZ97QIW8rpCGITweeIzPS9X4LVVfEOqUejumyG4Sm4SGMmKcqTMG1EIUAaLFU6y7pXQN7fib0CG9AGp273jwWLIUQ6-aWQwtU_FgWeU8uHNByXylknWGC7WRYzQQYzWJG-IQBIsuFfDfdBZ-NSXU383j8yX6kbfOgFc4O7Fk1NxQ60qZsUxjr9rexTyK7AMJvI3LlYswSmht8NaYFEQjqLkUbYo56ij62ulGm3utpRW8g83HXThHkvlJtCdhViIR4NNCf9A6eEFuStZZiy2fP4RCZ2nXsRPd-nvCl1Knu84V_bucQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سردار شکارچی: تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود
🔹
سخنگوی ارشد نیروهای مسلح: رژیم متجاوز و کودک‌کش صهیونیستی با سوءاستفاده از فرصت آتش‌بس و تجاوز آشکار به خاک لبنان، بیش از ۳ هزار نفر از مردم بی‌گناه، از جمله زنان و کودکان…</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/farsna/439203" target="_blank">📅 14:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439202">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d6821c78b.mp4?token=U-6BHrjJLSF3_5LT-yQP3n4DmCdq7GvuvoM5pdTNuohFI-3JC2Yeue_evVcfcVfQ9jZhsz84GXgybp_kV11LurZa0y2MjsyqMpuG5ri3W1a4JMTDwtnLugamQ8lVYkcf5m0ptaeBgp2elL4ZVT2UtJ7KpMELduEb30f1K5evDMcHTADootZC6SEzfMA8CfjjN5x5oMAjp5JS6hnaZMYgQGRrkRSLsBAOK-VCrTRgdbVBWawvQ5ZkuXyKExdmULVZGDYNARGgMbMWureiCvXFvFTgg1vxjuZ0XtsgASLTRyyM-_xARUmT04W-f7pEhqdiAzpzjv5C8xmTTxh5aDNfXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d6821c78b.mp4?token=U-6BHrjJLSF3_5LT-yQP3n4DmCdq7GvuvoM5pdTNuohFI-3JC2Yeue_evVcfcVfQ9jZhsz84GXgybp_kV11LurZa0y2MjsyqMpuG5ri3W1a4JMTDwtnLugamQ8lVYkcf5m0ptaeBgp2elL4ZVT2UtJ7KpMELduEb30f1K5evDMcHTADootZC6SEzfMA8CfjjN5x5oMAjp5JS6hnaZMYgQGRrkRSLsBAOK-VCrTRgdbVBWawvQ5ZkuXyKExdmULVZGDYNARGgMbMWureiCvXFvFTgg1vxjuZ0XtsgASLTRyyM-_xARUmT04W-f7pEhqdiAzpzjv5C8xmTTxh5aDNfXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایتی از نگرانی رهبر شهید انقلاب برای خانوادۀ محافظان خود
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/439202" target="_blank">📅 14:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439201">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
سردار شکارچی: تداوم جنایات در لبنان برای نیروهای مسلح ایران قابل تحمل نخواهد بود
🔹
سخنگوی ارشد نیروهای مسلح: رژیم متجاوز و کودک‌کش صهیونیستی با سوءاستفاده از فرصت آتش‌بس و تجاوز آشکار به خاک لبنان، بیش از ۳ هزار نفر از مردم بی‌گناه، از جمله زنان و کودکان را به خاک و خون کشیده است.
🔹
درحالی که حکام کشورهای غربی، راهکار سکوت یا حمایت از این جنایات ضد بشری را در پیش گرفته‌اند.
🔹
به سران رژیم ددمنش صهیونیستی و حامیان آن، هشدار داده می‌شود تداوم جنایات وحشیانه علیه لبنان، برای نیروهای مسلح ایران قابل تحمل نخواهد بود.
@Farsna</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/farsna/439201" target="_blank">📅 14:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439200">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YV92t0qrO-cW1T2Sb72sbYJbRlyn_JM1ATO1HWXx7bCQ3BPT4xSr0oN6rcillWgYBhIhdpZJwfWlcYrE9Iuvo0LtGYi5jszZcKhg_JMKKk9Gw5l57kqgLUY0fjeKXbCzALogsGb9TiayPCOUhvyHC7NVcgavNcMelhCIgDD7mLbZcyqNcODbVhyDWJpPPX62ldFLye-PRa3lqMJcER-3QE3YuzijGMthc_NGDAj-O2jLzV6rb1eP3W2ysNczyQW68HrvSTmlK-2UBSHBrDeqBK6INrrhQ7bFkNsnq3CxS23wpqItPQ2iA6kqVY-aF5FWCJEKqZnNn_JtJqRrg7za4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
رهبر انقلاب: دستورکار اصلی مجلس تمرکز بر شعار سال و ترسیم نقشه راه حرکت دولت متناسب با دوران پساجنگ است
🔹
لازم است مصوّبات مجلس، با مسائل اصلی کشور و نیاز‌های مردم، نسبتی مستقیم و مشهود داشته باشد و معطوف به امیدآفرینی و آینده‌سازی کشور باشد.
🔹
جامعه،…</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/439200" target="_blank">📅 13:55 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439199">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMS4ljTz3le6VHgGTHxjdMHY8AisrGEm7-k2l-tf4Q3LjH6w9A_CwC_loPug6wyVEW9uqgS3O0xTjD_1USxNVxMVZ6PF1oRLn7zXUA84yjbWq95loszb6JO4iHSmLi4_AET7ZM2nSGQOawst9ns1dR7SPkTFuczNPASEiItJ6CwmuZKYJVgQVLS_D1foCMAfroPftzIzbicyKBKh65hbkKSQjwRUmOKclWzP0wbnah5Uol_pwMAvB3R0nF0Z_MNsXoGFEKjFIqHxVMJHLLxHDtXSvXhwXO2J9jwghWQj0W_uKhTfaCqzV2Vu0-PUCe0_wtc9aa0II--pfqU2dpny7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
بقائی: حملۀ پلیس هلند به همسر باردار مرد فلسطینی، نقض فاحش حقوق‌بشر است
🔹
سخنگوی وزارت خارجه: این رفتار به‌شدت وحشیانه و غیرقابل توجیه است. هیچ عذری برای حملۀ خشونت‌آمیز پلیس به یک زن باردار وجود ندارد، تنها به این دلیل که او می‌خواست کنار همسر فلسطینی بازداشت‌شده‌اش…</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/farsna/439199" target="_blank">📅 13:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439198">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دلایل ثبت پویش «قطع داوطلبانۀ اینترنت بین‌الملل» از زبان سردبیر پویش
🔹
صالح اسکندری ثبت کننده پویش «فعال شدن قطع داوطلبانه دسترسی به اینترنت بین‌الملل»: هدف اصلی این مطالبه افزایش امنیت سایبری خانواده‌ها و صیانت از حریم خصوصی شهروندان است.
🔹
تحولات و جنگ‌ تحمیلی اخیر نشان داد که زیرساخت‌های ارتباطی و داده‌های دیجیتال به یکی از مهم‌ترین عرصه‌های تهدید و تقابل تبدیل شده‌اند.
🔹
دشمن طی سال‌های گذشته با بهره‌گیری از نفوذ سایبری، رهگیری داده‌ها و استفاده از فناوری‌های نوین هوش مصنوعی، تلاش کرده اند اطلاعات حساس و موقعیت افراد هدف را شناسایی کند. رسانه صهیونیستی اسرائیل هیوم هم در گزارشی که اخیرا منتشر کرده به این موضوع اعتراف کرده است.
🔹
کاربران باید این حق را داشته باشند که در صورت تمایل، ارتباط خود با اینترنت بین‌الملل را قطع کرده و تنها از خدمات داخلی و شبکه ملی اطلاعات استفاده کنند.
🔹
پیشنهادم این است گزینه‌ای نیز در پنل اپراتورها و مودم‌ها برای فعال یا غیرفعال کردن اینترنت بین‌الملل در اختیار مشترکان قرار گیرد. همچنین هزینه اینترنت داخلی و خارجی در صورتحساب کاربران تفکیک شود.
🔹
هدف این پویش محدودسازی اجباری اینترنت نیست، بلکه فراهم کردن حق انتخاب برای شهروندان است تا هر فرد متناسب با نیاز و تشخیص خود درباره نحوه استفاده از اینترنت بین‌الملل تصمیم‌گیری کند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.55K · <a href="https://t.me/farsna/439198" target="_blank">📅 13:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439197">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXBLToGmAQ4nxGsdEOIjsayMZOGgDLEuv3f4499e0M_-JsfkSIA4zL6Q7HC-cvnaRsyS-WMccb17-xigfmrIDx0Lg3y9hAFCgG514heRS2BgD8DI_IC1PQ3UzH7xmjU6m4ie6oCij6mjzwly-1uzZP_haw4gnEqNPqVeQ4pIiVoYTMCh497Uc0gQSP9B4cuDDuGy4diqX3tToZAVIDmbVy8hBaV4NYYHgEUxT47lp3YrEr0FMWShKeK1QU4HuzPm3KIh-D-bV9AlelwMnSJnuko03__YA-97NH9xv8yu2dVL82_8ehilC6pDESKeAgR89X69oN3LSwnLXyQrGBsviw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس به ۴ میلیون و ۳۰۰ هزار واحد رسید
🔹
شاخص کل بورس در پایان معاملات امروز با جهش ۶۴ هزار واحدی به ۴ میلیون و ۳۰۰ هزار واحد رسید.
@Farsna</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/farsna/439197" target="_blank">📅 13:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439196">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🔴
عبور ۱۵ کشتی با مجوز س‍‍پاه از تنگۀ هرمز
🔹
روابط‌عمومی نیروی دریایی سپاه: طی شبانه‌روز گذشته ۱۵ فروند کشتی که ۴ فروند از آن نفتکش بود پس از کسب مجوز با هماهنگی و تامین امنیت نیروی دریایی سپاه از تنگۀ هرمز عبور کردند.
🔹
به شناورهای تجاری و نفتکش در خلیج فارس و محدوده تنگه هرمز هشدار داده می‌شود هرگونه همکاری با نیروهای متخاصم فرامنطقه‌ای، به‌عنوان تهدید امنیتی قریب‌الوقوع شناخته شده و با آن برخورد خواهد شد.
@Farsna</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/farsna/439196" target="_blank">📅 13:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439195">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e2fd67119.mp4?token=WNiY89XGyXR_-yGyu7Nad_n8afV0sFtgDn_ZBa0Nhu2AGIJQydNMG67FDBdbAxQfA18gb-epxWQB-JmXVq9gwDBLPbKam-CdfZFVAj9dGl9SDCym5mXfpB2phaoVup0eJvNWgua3Jdvu1QNVadgEaOpbMIq6HJg7n4Mbf8bWpqWx92MmQTLR-xvKvQFMx54zV6GZNEnaRmwgY7L-5NA3QUpUEDTJ3dzXNpHUGHGs6MBzCLEAqzwr8-KYAheAojrQTv-2UiIJoot3A2HdekKdoxW3q5Gwpi4etfzBGM2Wqwc5zSJPJui-wiEVrwYv0zTkKq2iWxHtNnr-l7U_1x853w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e2fd67119.mp4?token=WNiY89XGyXR_-yGyu7Nad_n8afV0sFtgDn_ZBa0Nhu2AGIJQydNMG67FDBdbAxQfA18gb-epxWQB-JmXVq9gwDBLPbKam-CdfZFVAj9dGl9SDCym5mXfpB2phaoVup0eJvNWgua3Jdvu1QNVadgEaOpbMIq6HJg7n4Mbf8bWpqWx92MmQTLR-xvKvQFMx54zV6GZNEnaRmwgY7L-5NA3QUpUEDTJ3dzXNpHUGHGs6MBzCLEAqzwr8-KYAheAojrQTv-2UiIJoot3A2HdekKdoxW3q5Gwpi4etfzBGM2Wqwc5zSJPJui-wiEVrwYv0zTkKq2iWxHtNnr-l7U_1x853w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
جزئیات آخرین پیشنهاد ارسالی آمریکا به ایران
🔹
آجرلو عضو تیم رسانه‌ای هیئت مذاکره‌کننده: در مرحلۀ نخست مذاکرات، آمریکایی‌ها خواستار انتقال مواد هسته‌ای ایران به آمریکا بودند که این درخواست پذیرفته نشد.
🔹
در آخرین ویرایش‌ متنی که آمریکا ارسال کرده، دیگر بحث انتقال یا دفع مواد مطرح نیست و صرفاً عباراتی مانند «تعیین تکلیف»، «سرنوشت مواد» یا «حل‌وفصل مسئله مواد» مورد اشاره قرار گرفته.
🔹
در مورد مواد هسته‌ای هیچ تعهدی مبنی‌بر دفع و انتقال به آمریکا نمی‌دهیم. در مورد تنگه هنوز اختلافاتی وجود دارد که تاکید ما بر این است که مدیریت ایرانی باید بر آن حاکم شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/439195" target="_blank">📅 13:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439194">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
ابلاغ پیام رهبر انقلاب به خانوادۀ شهدای مدرسۀ میناب
🔹
حجت‌الاسلام وکیل‌پور، نمایندۀ ویژه رهبر معظم انقلاب، در سفر به شرق هرمزگان با خانواده‌های شهدای مدرسۀ شجرۀ طیبه میناب دیدار و گفت‌وگو کرد.
🔹
در این دیدار، پیام و سلام رهبر انقلاب به خانواده‌های معظم شهدا ابلاغ شد و از صبر، استقامت و ایثار این خانواده‌ها تجلیل شد.
🔹
خانواده‌های شهدا نیز در فضایی صمیمی ضمن بیان خاطرات و ویژگی‌های اخلاقی فرزندان شهید خود، دغدغه‌ها، مطالبات و دیدگاه‌هایشان را با نمایندۀ رهبر انقلاب در میان گذاشتند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/farsna/439194" target="_blank">📅 13:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439193">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwZ_HPquS1XMGkrS9ZWnry97aKAD3FK-qm-pbLpuS_QKtPHG2E3baWdUfio-XEQzrmlCfaRiIB_3k_tKRg_nivFeK3so5bOykdcdVyGUU8SjVCh1wB-5CPzbS8xVFkX18r1k735p5wYWAO_ocHmNOBvdCQsPb21lCmECAygBMLayW7YGQSKTnLsmpTHiOiEPTEyKM_3g1YAD7G_-PLh8Lh_boxtTn7JZ5HPPrAeBR3fR9uKT-5wtIoedml9XlFbwlpxbJedj3MDW6YQK5MwhKKGyLDH1pmzdNDdj6UQBCs7ad7Z9NS0cX_dXLd4gszS232hyhgTSzSveO3jK5LDOCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
آیا رقم کالابرگ تغییر می‌کند؟  @Farsna</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/farsna/439193" target="_blank">📅 13:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439192">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jelqknFEvtpUJw0Caco-VfyNgmL0jRZQHt25SvsaysL3bxbeeIc82BPvKcUs4BEssOIh8ODvBo2eHXxZ0lmGd4n1XW7NuSp_OjXWR2oH_gX7pU-bqFUpBEtt8YaumBAMFriteTmg9niIeyPmGzm4lSxuUoQsPgi2JZEHpZsKcwi3-ufdtOIevZcYE1UZtW8-tAu_-xf892F8qQUQqBYVqcWA2Jt46dUdrZ7TQeWs52iZAeKZGnE4JGVN6p6LHmWqMHCcrB8BC6ylQQYbdPWgVwSzDljtkQ-lCsN7NIEq3z3PUB1rEH6iCBWMihFA-cKm-vDDW7uxInOZkgTbLuCgXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
قالیباف به آمریکا: باید هزینهٔ جنایات رژیم صهیونیستی در لبنان را پرداخت کنید
🔹
رئیس مجلس در واکنش به تشدید حملات جنایتکارانهٔ رژیم صهیونیستی در لبنان نوشت: اعمال محاصرهٔ دریایی و تشدید جنایات جنگی در لبنان توسط رژیم نسل‌کش صهیونیستی، شواهد روشن عدم پایبندی آمریکا به آتش‌بس است.
🔹
هر انتخابی، هزینه‌ای دارد و صورتحساب آن هم از راه می‌رسد؛ همه‌چیز در نهایت سرجای خودش قرار خواهد گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/439192" target="_blank">📅 12:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439191">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3c3dc9b9e.mp4?token=V3xZOQGfHMo5cZ7w55pybKnm3XY6vGEdhHEvv9dc3qE2GOC-vImNMlpt0flMTXERJz7EgTXN50ipdSro37_RiQ7ST6bSz2S1LkH4bOi3w80n8H1nK6Fd0rOAuiiiFR9mHU9oXD2aZU0wONR6ar5F2zMsw_sAJ9ibAtgBj1eH9JQubPYRNQwJp51JQ-PzM5bBEfeQeTDUUHx3Vl7QNhW9lqKHwgpNp1JcfulHweRME0caLg5FtJZdGgZLulODlONTKXqN2Pj5f-UX1COrPP5m5gx2aPj4rH_luZZ6K1wf7g6l3oXmpxjQ08XAUV2B--M3QTIEWQnWKc4ID39mpOBqQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3c3dc9b9e.mp4?token=V3xZOQGfHMo5cZ7w55pybKnm3XY6vGEdhHEvv9dc3qE2GOC-vImNMlpt0flMTXERJz7EgTXN50ipdSro37_RiQ7ST6bSz2S1LkH4bOi3w80n8H1nK6Fd0rOAuiiiFR9mHU9oXD2aZU0wONR6ar5F2zMsw_sAJ9ibAtgBj1eH9JQubPYRNQwJp51JQ-PzM5bBEfeQeTDUUHx3Vl7QNhW9lqKHwgpNp1JcfulHweRME0caLg5FtJZdGgZLulODlONTKXqN2Pj5f-UX1COrPP5m5gx2aPj4rH_luZZ6K1wf7g6l3oXmpxjQ08XAUV2B--M3QTIEWQnWKc4ID39mpOBqQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: اختلاف نظرها در کشور نباید به تنازع  تبدیل شود؛ در زمین دشمن بازی نکنیم.  @Farsna</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/farsna/439191" target="_blank">📅 12:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439190">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f695ea1873.mp4?token=AwZ8WsaXMfw-LkSo6HtlxjGvC4jY_Es35DNb985nqRx3iyKvdkQA3fOmrqqbGI5wsXbsLlw75N0E4o_Sy73bUADd4biadjuYE1jmOI5UD3h4TBqatwfTMKkQRh8ATkm5JJjOerh5ULj9K48SdMxsbhV5a7_KU_GYo3yp64OO_FYBVUV-HqwQV105pjaznZ7UWnq9GHwz8ZDv4cnZocKXpriU2kYvClwicStutpvrLoT_BKFi0kD2tpM1LZTUH-Rag-C3WIzv8PkaQmxNP_MjgZL97WJNbs3tm1EvQzNMPV7GfU9q3Wbf5hZ1DVHQrhYqcm1h_sfU_Yc8jBusd8cwnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f695ea1873.mp4?token=AwZ8WsaXMfw-LkSo6HtlxjGvC4jY_Es35DNb985nqRx3iyKvdkQA3fOmrqqbGI5wsXbsLlw75N0E4o_Sy73bUADd4biadjuYE1jmOI5UD3h4TBqatwfTMKkQRh8ATkm5JJjOerh5ULj9K48SdMxsbhV5a7_KU_GYo3yp64OO_FYBVUV-HqwQV105pjaznZ7UWnq9GHwz8ZDv4cnZocKXpriU2kYvClwicStutpvrLoT_BKFi0kD2tpM1LZTUH-Rag-C3WIzv8PkaQmxNP_MjgZL97WJNbs3tm1EvQzNMPV7GfU9q3Wbf5hZ1DVHQrhYqcm1h_sfU_Yc8jBusd8cwnTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رئیس قوه‌قضائیه: اختلاف نظرها در کشور نباید به تنازع  تبدیل شود؛ در زمین دشمن بازی نکنیم.
@Farsna</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/farsna/439190" target="_blank">📅 12:40 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439189">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0543b35b60.mp4?token=nghnkCY4Wvggdrp8mLD1X_rFK_a7XP61Ojk7o5CjLShklVuFzq-OS9jihtCtQ8uJFIbIFzDGwJeENT7NbUsZDsU50rtv7sPMpcBjXO-L71N3TlEP8fnK-zghq0GVqqzZiar7EUoEQ0sjWw68AWtqlatHKLQMAWIMvLTSbix-Hzck4SB1wKBwWLELfkE0RoLNlCC6Qj0NeSBIAHte7MEc2T-4wJov9tEAhLBaMZVGue9sw6Z48NDh6-liOsZsepl9ihF5mrhq_cvo0BPFz_uJqsb4h7oytziC7Ngvl1kzws8e-l_iZkHpxZO59KZUOMguzaexC4VB8jyNIYP1jKzhwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0543b35b60.mp4?token=nghnkCY4Wvggdrp8mLD1X_rFK_a7XP61Ojk7o5CjLShklVuFzq-OS9jihtCtQ8uJFIbIFzDGwJeENT7NbUsZDsU50rtv7sPMpcBjXO-L71N3TlEP8fnK-zghq0GVqqzZiar7EUoEQ0sjWw68AWtqlatHKLQMAWIMvLTSbix-Hzck4SB1wKBwWLELfkE0RoLNlCC6Qj0NeSBIAHte7MEc2T-4wJov9tEAhLBaMZVGue9sw6Z48NDh6-liOsZsepl9ihF5mrhq_cvo0BPFz_uJqsb4h7oytziC7Ngvl1kzws8e-l_iZkHpxZO59KZUOMguzaexC4VB8jyNIYP1jKzhwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ رئیس بنیاد ملی گندم‌کاران: ۵۰ درصد پول گندم‌کاران این هفته پرداخت می‌شود.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/farsna/439189" target="_blank">📅 12:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439188">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5653b7d9c4.mp4?token=Fj-HZ1w40ZJv853_7zpbWMzE97lEbmkG_rtaCioPdPIMdTg5Dhr4nrgzByQkmYrVQtskp2DXWSr1qr8WgMykGw5q0l9fR6g8dW36jEHDVvDMWd-nejaIhPDsIZruiTGekx_TlURnTO4w8BOmDFXwA04pn9KQu-NiNCAJP2dU0Vu_70ij8Vw47S9Myast4EeA5AWE-ACugiF5LLgn6TfDpvwmUnaLcgYZd7p5arhtv40rBmlP3FtwTPqm4vATujJPVhG-XWyfizbnnK_BUJWpabSvvLArmfXnMyolFjO0q38iYTHeVBvUrqhpn7GvIw2VDLTZql8yULycudONH99gznFdsYrR6vzZh2U35zHPgWZKKfQB5a35B2kU_eDGyLpr8hMsAfZyAFsFsVJ1yN5ACe8g35itz2haS9ZzhN-qyypmm8374Y4E9ni_-mHO_ERTRXYbut_lUkP3W6fgKD5qhcIW6d9Elmsp05va03nKPr-LQCrSVgUQbBGd7ZbXnrtOmJ9WRBXG4VOzLKsZA3j8_3eSAlsfXxGRDruqmjQLKZsr-dsb61sfMGIhBxt-4et3tpIsaj1XJ_q37IxpO3gJq68F9MbnNDmGAnG7PhdjC7-itYUTHbxbH9zk_MvihY3vvFromFHCFOqfuWUq6ec9UMP2EHI7QkZTMlFPMIWM4mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5653b7d9c4.mp4?token=Fj-HZ1w40ZJv853_7zpbWMzE97lEbmkG_rtaCioPdPIMdTg5Dhr4nrgzByQkmYrVQtskp2DXWSr1qr8WgMykGw5q0l9fR6g8dW36jEHDVvDMWd-nejaIhPDsIZruiTGekx_TlURnTO4w8BOmDFXwA04pn9KQu-NiNCAJP2dU0Vu_70ij8Vw47S9Myast4EeA5AWE-ACugiF5LLgn6TfDpvwmUnaLcgYZd7p5arhtv40rBmlP3FtwTPqm4vATujJPVhG-XWyfizbnnK_BUJWpabSvvLArmfXnMyolFjO0q38iYTHeVBvUrqhpn7GvIw2VDLTZql8yULycudONH99gznFdsYrR6vzZh2U35zHPgWZKKfQB5a35B2kU_eDGyLpr8hMsAfZyAFsFsVJ1yN5ACe8g35itz2haS9ZzhN-qyypmm8374Y4E9ni_-mHO_ERTRXYbut_lUkP3W6fgKD5qhcIW6d9Elmsp05va03nKPr-LQCrSVgUQbBGd7ZbXnrtOmJ9WRBXG4VOzLKsZA3j8_3eSAlsfXxGRDruqmjQLKZsr-dsb61sfMGIhBxt-4et3tpIsaj1XJ_q37IxpO3gJq68F9MbnNDmGAnG7PhdjC7-itYUTHbxbH9zk_MvihY3vvFromFHCFOqfuWUq6ec9UMP2EHI7QkZTMlFPMIWM4mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تصاویر یکی از عملیات‌های گشت و کنترل تنگۀ هرمز توسط شناورهای تندوری نیروی دریایی سپاه طی روزهای گذشته
@Farsna</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farsna/439188" target="_blank">📅 12:14 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439187">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac59e86c7d.mp4?token=hNNcgkltGJJL__o31en0BZCaR4EFdrdtDNzawFwoNW3_QwSd-u3zz4unjbK7Ro6cn9VRjL8GbQbTnNL0KWB4emfIWSX59NK41XtWNksRbVfLSRTADp0c_Yz-gb066O2g6R0PxgYNuzImOnLrIpD5YygNSOOfwX_0H6KIR7TvsuAbX38WbzMkA9a2ulJuWZMzTpez-9GvwkjCp-P_VdbNuexZ0KNJpGG72tykrwBBQri8f6SYr8hvVm1M98Pkf6MlpZbSwWnyR3OfcinIG89L3jBi6Antu4cPr9i-Odgl226P_kLKPNRWRmmUe_EMSY2r3L-qPHJVyERscrsZLGt_Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac59e86c7d.mp4?token=hNNcgkltGJJL__o31en0BZCaR4EFdrdtDNzawFwoNW3_QwSd-u3zz4unjbK7Ro6cn9VRjL8GbQbTnNL0KWB4emfIWSX59NK41XtWNksRbVfLSRTADp0c_Yz-gb066O2g6R0PxgYNuzImOnLrIpD5YygNSOOfwX_0H6KIR7TvsuAbX38WbzMkA9a2ulJuWZMzTpez-9GvwkjCp-P_VdbNuexZ0KNJpGG72tykrwBBQri8f6SYr8hvVm1M98Pkf6MlpZbSwWnyR3OfcinIG89L3jBi6Antu4cPr9i-Odgl226P_kLKPNRWRmmUe_EMSY2r3L-qPHJVyERscrsZLGt_Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: با عمانی‌ها صحبت کردیم و آن‌ها هم دربارهٔ تنگهٔ هرمز نگرانی‌های مشترکی با ما دارند.  @Farsna</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/farsna/439187" target="_blank">📅 11:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439186">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W67QbgS5L088evCdFOaY4nCE0s997nNSWZq2pOGcXvRpctKCXIbIXgWZ1IxTWJ2NxJC6sGCMNesVK6FexvixPUMfZKLVFlJvknjvFn24yPDm10wB_Gb6lZJY5cKdBGAufSSb6FkMBkUEXzhm3B9ghkROh4q65-eE-pFVscMkFKY3RScmtwpvBK75QnynMCSrk8csgADe6muvbzjXE_0mf2RizI5LktKgGKRhsV6M7Ei6TdAfEryTqAU_M_wpUImfMbbfevGF7WF2ZObirDefBZh8yyS-auVkxUrAuwJKzN6XVC7HQxFyKnu9VZ92WjL9fW45xXFMdFSj3YS7jAoUcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادراه هوشمند تهران در آستانهٔ بهره‌برداری
🔹
ساخت فاز اول آزاد‌راه شهید شوشتری که مجهز به سامانه‌های هوشمند است با طول ۹ کیلومتر به ‌اتمام رسید.
🔹
این فاز محدودهٔ بزرگراه امام رضا(ع) در جنوب شرق تهران را به شمال استادیوم تختی، بلوار هجرت و بزرگراه بسیج وصل می‌کند و ضمن کوتاه‌تر کردن مسیرهای تردد، بخشی از بار ترافیکی بزرگراه بسیج را هم کاهش می‌دهد.
@Farsns
-
Link</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/farsna/439186" target="_blank">📅 11:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439185">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cff7c45be.mp4?token=OA2w3AtKZ4px2RvWVq5TG-FiKt67v48NwUnTaGdxByG2KAI0kLIO96JDGB2Fv9F85FK_CvKZ2ECY-jLldn38slDZCeAXUrXZNhuPpvF0pSaZ2zf_g5uqz-CpluXD6b_0BNPgrQQKB1HDqg8RSa7lBwvDEfAjq0aexsGQKxjvfhHfja-8Bz5wvrmjQ7c049Fc7izrrW06USyNn1j-hAYJMSA7F2YeIygl91Cva1UbFGV9dRh5RlHEBr8vT62-WoCP7YjorgnNPSTo79X1OtTHAGBmTdmRjCRznuH9meBToTlXDwa3U2MkfC11hJW1ln28OY0fv4QtIcZAJBoxGksIuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cff7c45be.mp4?token=OA2w3AtKZ4px2RvWVq5TG-FiKt67v48NwUnTaGdxByG2KAI0kLIO96JDGB2Fv9F85FK_CvKZ2ECY-jLldn38slDZCeAXUrXZNhuPpvF0pSaZ2zf_g5uqz-CpluXD6b_0BNPgrQQKB1HDqg8RSa7lBwvDEfAjq0aexsGQKxjvfhHfja-8Bz5wvrmjQ7c049Fc7izrrW06USyNn1j-hAYJMSA7F2YeIygl91Cva1UbFGV9dRh5RlHEBr8vT62-WoCP7YjorgnNPSTo79X1OtTHAGBmTdmRjCRznuH9meBToTlXDwa3U2MkfC11hJW1ln28OY0fv4QtIcZAJBoxGksIuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر رفاه: کالابرگ خردادماه به روال ماه‌های قبل پرداخت می‌شود
🔹
بخش‌های مختلف دولت مانند سازمان برنامه به‌دنبال منابع جدید برای کالابرگ هستند، اما هنوز منابع جدیدی نداریم.
🔹
در مذاکراتی که با صنایع لبنی داشتیم، قرار است مواد لبنیاتی کالابرگ با ۱۰ درصد تخفیف…</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/farsna/439185" target="_blank">📅 11:46 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439184">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b145f3b466.mp4?token=kJJmup7p024ZCuZchBVHzXmW8lvwrsjsAA0pFgzKZgMZ5UqIaFR81AFMh6ABeZLRf-IJBzC2Qsl5RrrcAJg0vqQzOGXaUIOHuXWKIjY-b3w4NkcV4F_-CcO3kvn2_FA_LZJGeJYjKdQjzq6tD3NqsQQ7dWBgHfkEgL-yeAXPgSnI2a2Qb6PUdNthlxwCH4UEuSQQv92n-4BTQ22KcC20VHBPMHR4duftFoLzTLt7JO1LytJZFA6fAIAAwncRjjpCwQuwKLsaLrv3AEV2qDTRL32eP6NtprRCMXLj5DRvM5r4QwTkmYNJoXASqYVX4JmEOKj_6jyfjoyOrxKAy33G-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b145f3b466.mp4?token=kJJmup7p024ZCuZchBVHzXmW8lvwrsjsAA0pFgzKZgMZ5UqIaFR81AFMh6ABeZLRf-IJBzC2Qsl5RrrcAJg0vqQzOGXaUIOHuXWKIjY-b3w4NkcV4F_-CcO3kvn2_FA_LZJGeJYjKdQjzq6tD3NqsQQ7dWBgHfkEgL-yeAXPgSnI2a2Qb6PUdNthlxwCH4UEuSQQv92n-4BTQ22KcC20VHBPMHR4duftFoLzTLt7JO1LytJZFA6fAIAAwncRjjpCwQuwKLsaLrv3AEV2qDTRL32eP6NtprRCMXLj5DRvM5r4QwTkmYNJoXASqYVX4JmEOKj_6jyfjoyOrxKAy33G-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: حمایت از محیط‌زیست در تنگهٔ هرمز بسیار مهم است و هزینه‌هایی دارد که دریافت می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 7.21K · <a href="https://t.me/farsna/439184" target="_blank">📅 11:44 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439183">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb5ddf5a05.mp4?token=c5Rto-fnkNpMrCGpQKUBOjXd_7_2EqRk_bUnsuCrP-w2nh1iLMtVhQZiR9v-ijsL7EQ-3AJKEB0RxZZS7xgxSr88aq_wIrzmSX_nCAwcMgSU0V2bsyZONPAOujgA-VyzyqdGVcvz8zkwrZIDJdUTn49lhmd6oyohgClo7Pir3ngVCyHmfvPjMyWO1l8KqkhUVfBpVAhi-0ONt86B1alasNlm1cL9Dx2o6F56FhiIcN9rNxDq6BjykW4ThINK-6hPLQ-8Iw4yEvgfCoJjbQW0OTrdRNOHYtFN-TkydnxrQ1dhAaztrHEOhLaCWBrDI9wvCwH22yIInLM9HkkyQYn6Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb5ddf5a05.mp4?token=c5Rto-fnkNpMrCGpQKUBOjXd_7_2EqRk_bUnsuCrP-w2nh1iLMtVhQZiR9v-ijsL7EQ-3AJKEB0RxZZS7xgxSr88aq_wIrzmSX_nCAwcMgSU0V2bsyZONPAOujgA-VyzyqdGVcvz8zkwrZIDJdUTn49lhmd6oyohgClo7Pir3ngVCyHmfvPjMyWO1l8KqkhUVfBpVAhi-0ONt86B1alasNlm1cL9Dx2o6F56FhiIcN9rNxDq6BjykW4ThINK-6hPLQ-8Iw4yEvgfCoJjbQW0OTrdRNOHYtFN-TkydnxrQ1dhAaztrHEOhLaCWBrDI9wvCwH22yIInLM9HkkyQYn6Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: قطعنامه شورای امنیت برای ما تضمین نیست
🔹
در تفاهم اولیه یک بند دربارهٔ صدور قطعنامهٔ شورای امنیت در صورت توافق وجود دارد اما معنایش این نیست که ما قطعنامهٔ شورای امنیت را تضمین می‌بینیم.
🔹
صدور این قطعنامه صرفاً برای پوشش حقوقی توافق…</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/farsna/439183" target="_blank">📅 11:43 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439182">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b04cce048.mp4?token=eApm3QgPlEyC9zbDx4sopujQt7F5XE--O8JXsKtYfDwGk-AiBjDpbHyTMEad6NuZknjs44xZkfJ5LAfSlgA9Xh6igvsA3mgvPKFeXHa-DoRxKB38F0bd5cGqkuZvYL0uJgrGzUJJ3LzvSbH-JAhJWJlNNRxARYmtxMB3Gwae8g7zLv-iNJ6C6aHvTl5rnvWrTdDwNSu0Kn6Xk1JaN3qgCt5DS5GoYdCPfCmW7CD1oTXYB4BTU-rncEv_39CVSDEcIKJzy-m56M_ut5vnVJQIE2mEHS5PMl7K0_hq30vGCJTzWmQZF441UIBZzki1YRj230GGtMtRMpG6d5SGbZkWkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b04cce048.mp4?token=eApm3QgPlEyC9zbDx4sopujQt7F5XE--O8JXsKtYfDwGk-AiBjDpbHyTMEad6NuZknjs44xZkfJ5LAfSlgA9Xh6igvsA3mgvPKFeXHa-DoRxKB38F0bd5cGqkuZvYL0uJgrGzUJJ3LzvSbH-JAhJWJlNNRxARYmtxMB3Gwae8g7zLv-iNJ6C6aHvTl5rnvWrTdDwNSu0Kn6Xk1JaN3qgCt5DS5GoYdCPfCmW7CD1oTXYB4BTU-rncEv_39CVSDEcIKJzy-m56M_ut5vnVJQIE2mEHS5PMl7K0_hq30vGCJTzWmQZF441UIBZzki1YRj230GGtMtRMpG6d5SGbZkWkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: سفر هیئت مذاکره‌کننده به قطر مثبت بود
🔹
میانجی مذاکرات همچنان پاکستان است. در سفر هیئت مذاکره‌کننده به قطر برخی از جنبه‌های مالی توافق خاتمهٔ جنگ بررسی شد. @Farsna</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/farsna/439182" target="_blank">📅 11:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439181">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c2535b069.mp4?token=fqGFGy4cLzrzezYDl1t_7kKiMv0AH1LN-begrqzjpxm0J0WU95ElM5mFrl6Fb8lnab67av_i-sVnTMoCKy8Mla1t4H5hzw6M8dpcBS9L3sJjuusBkP7VmcXtK1qATW1A_GcBlcjTuFoKVc4P_5bADt2xwL_89F-5sEcZ3kq14Sggf3FOzlod2zymiNdl44tm-B3uzCKSKdSmfzatoz0SEQwy9YYHjyhLMtAbI72OOq0l24tWkwg0WaQ5XNa8acrh3hvs-vL4z_DIMbZRu-bAFkxTeJt4UNWQlyzIKhtuENuZAPu86vDN1Of_pvopnNpS25ZTk299iv7KEk5X5S9XrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c2535b069.mp4?token=fqGFGy4cLzrzezYDl1t_7kKiMv0AH1LN-begrqzjpxm0J0WU95ElM5mFrl6Fb8lnab67av_i-sVnTMoCKy8Mla1t4H5hzw6M8dpcBS9L3sJjuusBkP7VmcXtK1qATW1A_GcBlcjTuFoKVc4P_5bADt2xwL_89F-5sEcZ3kq14Sggf3FOzlod2zymiNdl44tm-B3uzCKSKdSmfzatoz0SEQwy9YYHjyhLMtAbI72OOq0l24tWkwg0WaQ5XNa8acrh3hvs-vL4z_DIMbZRu-bAFkxTeJt4UNWQlyzIKhtuENuZAPu86vDN1Of_pvopnNpS25ZTk299iv7KEk5X5S9XrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما حق دفاع مشروع در برابر نقض آتش‌بس توسط آمریکا را داریم و امروز هم مبدأ تجاوز به خاک کشور را هدف قرار دادیم.  @Farsna</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/farsna/439181" target="_blank">📅 11:31 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439180">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9tAxesljl5lexQz-fD8ur45LntaB1Sz54R8x37GWnERKxP0bJD-JLN4-P2-IMaUqcHVU8PJE1F7aZN5aaQgdQ6AfAF7gJpsXgRbWabBGbD03v6YNn0hFEY_2QPICXbO1G1WC0y80hLtualDrRkhUIPsyRfoD1rLOm9_S11KN1R7M18xqNhGF6JfSiN8GO7jAhzonNbuoLcaIcIYfb6-QzM5fEbHIUmoWtiM7Ob-Fo23POpGc9bCs_awP6cDIl6_zm3uarq9pPZ7f5U9dHpDsmrhoUDs8fl3113oTIQcG7XvevtUXQ5FQdCBheIiw_lwSxMPhxfsRXiC8jctdkmwiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان حمایت: افزایش قیمت مدیران خودرو غیرقانونی است
🔹
در‌پی اعلام شرکت مدیران خودرو مبنی‌بر افزایش حدود ۸۰ درصدی قیمت محصولات خود، سازمان حمایت از حقوق مصرف‌کنندگان اعلام کرد این افزایش قیمت قانونی نیست و فاقد اعتبار است.
🔹
براساس دستورالعمل مورخ ۱۴۰۴/۶/۱۱ شورای رقابت، تمامی عرضه‌کنندگان خودرو موظف‌اند مدارک خود را جهت تعدیل قیمت به سازمان حمایت ارائه کنند تا پس از بررسی‌های لازم، قیمت‌های جدید محاسبه و ابلاغ شود.
🔹
با این حال، این شرکت بدون هماهنگی و به‌صورت خودسرانه اقدام به افزایش قیمت کرده؛ درحالی که استعلامات و بررسی‌های قانونی این شرکت هنوز تکمیل نشده.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/439180" target="_blank">📅 11:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439179">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a4848aa7a.mp4?token=dQj2pHBNuubCCg7-lpf8p7qqGSCFfVnu6QgdjFTJZnR9B678AXKYMwCb5SqbBa2or1L2ibZOqL9xwLQ4KQfwHbtIOVvlJmMDj2NZyYNuDfeOHOIM8bHPC276Eaiy_iSFbtOERtzgcETkOryf1m3tSLKA6PYvfHfGK6w_I6tX5aDZStL_SsD142eSWGlG9eberScnpJZDT-_JWVULe2KSns-BVr8JDStQOKz5MPAlcxGsZ0XCbiYVOFpAxpt4ZUI6Xt9aUoEuz9weitmWdKu2-JBRKdoW12gVs5gdK4Nw5qrk4Z7K5V1YXs4LYfaGqNU9_EsDpf6MJvt3qzCsKeVKHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a4848aa7a.mp4?token=dQj2pHBNuubCCg7-lpf8p7qqGSCFfVnu6QgdjFTJZnR9B678AXKYMwCb5SqbBa2or1L2ibZOqL9xwLQ4KQfwHbtIOVvlJmMDj2NZyYNuDfeOHOIM8bHPC276Eaiy_iSFbtOERtzgcETkOryf1m3tSLKA6PYvfHfGK6w_I6tX5aDZStL_SsD142eSWGlG9eberScnpJZDT-_JWVULe2KSns-BVr8JDStQOKz5MPAlcxGsZ0XCbiYVOFpAxpt4ZUI6Xt9aUoEuz9weitmWdKu2-JBRKdoW12gVs5gdK4Nw5qrk4Z7K5V1YXs4LYfaGqNU9_EsDpf6MJvt3qzCsKeVKHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: پول‌هایی که ایران در برجام دریافت کرد، اموال مسدودشده و حق مردم ایران بود
🔹
حالا هم به‌دنبال احقاق حقوق مردم ایران هستیم و هنوز دربارهٔ سازوکار یا نحوهٔ دریافت اموالِ به‌ناحق مسدودشدهٔ ایران تفاهمی انجام نشده است. @Farsna</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/farsna/439179" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439178">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50678b3be7.mp4?token=WXA93DN5HXCnc72eWU1xTwatuY0-bgoDa99_szsGdEhiQIxk4Wpa2kluD4kIGF8kMjJ76FNlvmpwyiSw8cqcIp3Ig57Uf-VuCxqT7hqVOZGdr0xm2rUVtvsbHolyGRt5-362A7NT12l76rRQCKxoG9twWXpfXASNnhBDgwtiKBHXwxlRECe1e9Z6XdqDoOn_wsYuTiKJLXeVZfIZ6s8rovQlmDM4Hw_bYIflKaCcNTb7ihisJdToYRK0CJcuIHMol7VbXGHhFjnulLBVTZh8NvGNFmArB5q1UdvyLmIrU2_Os63H__OtfYM8LjgdQTL-KJxrxKS0NI34MAyj23chwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50678b3be7.mp4?token=WXA93DN5HXCnc72eWU1xTwatuY0-bgoDa99_szsGdEhiQIxk4Wpa2kluD4kIGF8kMjJ76FNlvmpwyiSw8cqcIp3Ig57Uf-VuCxqT7hqVOZGdr0xm2rUVtvsbHolyGRt5-362A7NT12l76rRQCKxoG9twWXpfXASNnhBDgwtiKBHXwxlRECe1e9Z6XdqDoOn_wsYuTiKJLXeVZfIZ6s8rovQlmDM4Hw_bYIflKaCcNTb7ihisJdToYRK0CJcuIHMol7VbXGHhFjnulLBVTZh8NvGNFmArB5q1UdvyLmIrU2_Os63H__OtfYM8LjgdQTL-KJxrxKS0NI34MAyj23chwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
عقاب آسمان ایران که هیچ مأموریتی را نیمه‌کاره نگذاشت
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.3K · <a href="https://t.me/farsna/439178" target="_blank">📅 11:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439177">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4b61af2e.mp4?token=eb642rFtcygBPdPVwLq-T8W4633kaDljETk5qvStjduFVK_FSg2oqhr8zsCTSaMIRJYHd41WL4bGusZ8NQ4noTmvnbH-NXH79UxMDgUPzy1-gZCVi8QIDGveaGAWgLr9dDdHmeo6ZJ1380VxGeCDJrMSDt50BkCRERBUXgcNU86XofpC_fyUtDrxhkm7XYaebFzRYBry3pwnlmjg1LWjEdD71VpYNHF4GPIbe7IWgx9uvv1kC9jTOWqrbTMR4Uzd7slEJFS83bzrQezwk0pQEtcvaFZJep_MTleaWjEo5xVdmJUp-1HiM3DgI8eIa6_eMDp9lIwV0AZQtob0egM31g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4b61af2e.mp4?token=eb642rFtcygBPdPVwLq-T8W4633kaDljETk5qvStjduFVK_FSg2oqhr8zsCTSaMIRJYHd41WL4bGusZ8NQ4noTmvnbH-NXH79UxMDgUPzy1-gZCVi8QIDGveaGAWgLr9dDdHmeo6ZJ1380VxGeCDJrMSDt50BkCRERBUXgcNU86XofpC_fyUtDrxhkm7XYaebFzRYBry3pwnlmjg1LWjEdD71VpYNHF4GPIbe7IWgx9uvv1kC9jTOWqrbTMR4Uzd7slEJFS83bzrQezwk0pQEtcvaFZJep_MTleaWjEo5xVdmJUp-1HiM3DgI8eIa6_eMDp9lIwV0AZQtob0egM31g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: ما با مردم کویت و سایر مردم منطقه که خاکشان مبدأ حمله به ایران است، ابراز هم‌بستگی می‌کنیم
🔹
بیانیهٔ اتحادیهٔ اروپا در حمایت از کویت، مصداق ریاکاری است؛ نمی‌شود حملهٔ غیرقانونی آمریکا و اسرائیل به ایران را نادیده گرفت اما پاسخ ایران را…</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/439177" target="_blank">📅 11:20 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439176">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4g8QmxsZPqD5_D8z9VIj5Hrj0CgsEuudPKBGFaGlperWmxkXnYQxNOqMeXMyRycdDRaCZqGRtfk84Ww9nxsyretCsX-mjn1pkuAVLrT70ImK_6cHM7asEgBHjW4itjrsMzZ-pw8bzC_w2KtEqE_gWOJor-um1r454p2pLSjd7e2z5rpIUfNvSM3YXLrzWgZ7igVoYBfXqFfMYzJy4eRy51pV2q4pDqU41kc4Y0qcWIV1eejoImU_2_nhhvjW7WKwdSeZ9l6V1jI59upehut1T5XKOUat-1T_oSYxjfGE5OHSUC2Xu1hpWsZfGEj6l07GkuvDpCMjcjtMrXuuTCocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
افزایش اجاره دادِ مستاجران را  درآورد  @Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/439176" target="_blank">📅 11:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439175">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ab32b38bd.mp4?token=peUSz9hcBV45crlr8ITln8gul0x8nIDiJT22j03EEM_1jso9oXcZDfKqX-Q0fOm9X4FmdMe-oUTjcUxeaXZ4D0W94JnEIh_bWn3RM576xJYAZGn2S_ukrVHMcbI1vJ9yMZmKFNqr8v_p_myx4r1SKEuQ3_V_fF4H3EcEtUXy0z_D-91Pk5ZVB8sArYovacUFJ09hLxSdamR_SCEw50S9niHm-0uqUdhGpOI8KQEMMoeikPMIKc5GG3mbBZFMEdvTn1h4-CbF0hHcQwdmKMlvyrkTAs1k2uNzxTPts3jOkl_oo-MOXkhJ1044yL0nnTUhl7DN1DxFKTeiWrez4hojzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ab32b38bd.mp4?token=peUSz9hcBV45crlr8ITln8gul0x8nIDiJT22j03EEM_1jso9oXcZDfKqX-Q0fOm9X4FmdMe-oUTjcUxeaXZ4D0W94JnEIh_bWn3RM576xJYAZGn2S_ukrVHMcbI1vJ9yMZmKFNqr8v_p_myx4r1SKEuQ3_V_fF4H3EcEtUXy0z_D-91Pk5ZVB8sArYovacUFJ09hLxSdamR_SCEw50S9niHm-0uqUdhGpOI8KQEMMoeikPMIKc5GG3mbBZFMEdvTn1h4-CbF0hHcQwdmKMlvyrkTAs1k2uNzxTPts3jOkl_oo-MOXkhJ1044yL0nnTUhl7DN1DxFKTeiWrez4hojzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: یکی از بخش‌های تفاهم، ایجاد شرایطی برای بازسازی خسارت‌های جنگ است
🔹
یکی از راه‌هایی که در این مرحله دربارهٔ آن صحبت شده، اختصاص یک مبلغ برای بازسازی خسارت‌هاست. @Farsna</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/farsna/439175" target="_blank">📅 11:09 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439174">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">رئیس دادگستری سمنان:  اموال ۱۸ تن از عناصر مرتبط با سرویس‌های جاسوسی در خارج از کشور توقیف شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/farsna/439174" target="_blank">📅 11:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439173">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e85453ef3.mp4?token=nxvnI5SmqdH9NE65QOrc1Y8jo8D_ODV9eJvQEjzVVpL6Seqc_SzD0fDrr_gDDVpaiN0pvToKrVjk5bqHJhnd53GFJUz6D2gq-9DtQdmXeJxeLIjsg6i_jbj_ymHI8pQ8jeApXP2ImeTFv5tPC1JZ2v8FMYyQZr2WFeiA5pJ7-HLGEvLUn1NX7fWOnZwVStM50WKOHqLz-rKXC2lNo6T3M0mLpkYD4LmCjI9CihvLpM0gP6SksHpBRay_69414Fg0lDPr2WfMNLRgNsRJCCpG9BKGq_70dqcKGmm79iBJsEKCXMbopuu_g69tX_hw79fiEL-faoBxLrX8eydyn994_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e85453ef3.mp4?token=nxvnI5SmqdH9NE65QOrc1Y8jo8D_ODV9eJvQEjzVVpL6Seqc_SzD0fDrr_gDDVpaiN0pvToKrVjk5bqHJhnd53GFJUz6D2gq-9DtQdmXeJxeLIjsg6i_jbj_ymHI8pQ8jeApXP2ImeTFv5tPC1JZ2v8FMYyQZr2WFeiA5pJ7-HLGEvLUn1NX7fWOnZwVStM50WKOHqLz-rKXC2lNo6T3M0mLpkYD4LmCjI9CihvLpM0gP6SksHpBRay_69414Fg0lDPr2WfMNLRgNsRJCCpG9BKGq_70dqcKGmm79iBJsEKCXMbopuu_g69tX_hw79fiEL-faoBxLrX8eydyn994_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بقایی در واکنش به ادعای ترامپ دربارهٔ خارج‌کردن اورانیوم از ایران: ما دربارهٔ جزئیات موضوع هسته‌ای هیچ مذاکره‌ای نکرده‌ایم.  @Farsna</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/439173" target="_blank">📅 11:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439172">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3b8296f4a.mp4?token=O2xNVSqbWj3su_qTENpdHKwf9L8A3DsPtAkKrPdeNSV1uO2smdp0Tn5SLilOsOTtmWCtoyrx30XLktlgojUsOebTxP3DWq8T5TPQg2y-VcodxIJZhBA6_8X5uuS0RE-gYFtul7YoGRv6LuPXyUePD75ri-0nrPgpngZtYKcbz95uHKg0U_j8kkXClBpCRk9mH14sioYu5lL8r183KrR_BC-TIfsy3Dn2ephQlMcztoX0yVM9yIobPcKmdaU0wktpkDQ7WWPsIfq8Q84iDkCwmlQ60pB1JGnL4qUAQSR3-U8wSEvhJ6UkAyfe5Kn3pBnhV1endQ1a7uide27S8PpYhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3b8296f4a.mp4?token=O2xNVSqbWj3su_qTENpdHKwf9L8A3DsPtAkKrPdeNSV1uO2smdp0Tn5SLilOsOTtmWCtoyrx30XLktlgojUsOebTxP3DWq8T5TPQg2y-VcodxIJZhBA6_8X5uuS0RE-gYFtul7YoGRv6LuPXyUePD75ri-0nrPgpngZtYKcbz95uHKg0U_j8kkXClBpCRk9mH14sioYu5lL8r183KrR_BC-TIfsy3Dn2ephQlMcztoX0yVM9yIobPcKmdaU0wktpkDQ7WWPsIfq8Q84iDkCwmlQ60pB1JGnL4qUAQSR3-U8wSEvhJ6UkAyfe5Kn3pBnhV1endQ1a7uide27S8PpYhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: کویت هنوز امکان دسترسی کنسولی سفارت به ۴ شهروند دستگیرشدهٔ ایرانی را ایجاد نکرده است
🔹
اجازه‌دادن به طرف‌های متجاوز برای اقدام علیه ایران از سوی دولت‌های منطقه، آن‌ها را کنار طرف‌های متجاوز خواهد نشاند. @Farsna</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/farsna/439172" target="_blank">📅 11:01 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439171">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19d2e52790.mp4?token=bfzW_f3mmeRa23CQGs6tCsVCz0W_kRCY6oGTElvv2XRIg-kHov8WdoebpjZCvbtwIt7BuX13sjpV3skVAeV5dgNaioG4U0SFhOndwJBnT_caEwF8n9XGb3wE3PPOM2kxOtMfw7nZz1Dsf1YJw2GZqWKBVJxKyYhz7D1eY-9PA1EaIFUrczeL0NopB8IyfrFeb9b8V-S8mvZvaO2vp5N2n6AUfxav3CsCwIbROIi-lKwlBmty7m52ROM8VOqo0uhMR_uqa0HbQ9kTrfi9riNjhnj26OBfgp3UNw4voJxsU99B19bsA3oT20OuV8pntxsckQ_t4rf7ItB4dU7udc2L0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19d2e52790.mp4?token=bfzW_f3mmeRa23CQGs6tCsVCz0W_kRCY6oGTElvv2XRIg-kHov8WdoebpjZCvbtwIt7BuX13sjpV3skVAeV5dgNaioG4U0SFhOndwJBnT_caEwF8n9XGb3wE3PPOM2kxOtMfw7nZz1Dsf1YJw2GZqWKBVJxKyYhz7D1eY-9PA1EaIFUrczeL0NopB8IyfrFeb9b8V-S8mvZvaO2vp5N2n6AUfxav3CsCwIbROIi-lKwlBmty7m52ROM8VOqo0uhMR_uqa0HbQ9kTrfi9riNjhnj26OBfgp3UNw4voJxsU99B19bsA3oT20OuV8pntxsckQ_t4rf7ItB4dU7udc2L0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مواضع متناقض آمریکایی‌ها دلیل طولانی‌شدن روند دستیابی به تفاهم است
🔹
آمریکا مسئول جنایات رژیم صهیونیستی در لبنان است. @Farsna</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/farsna/439171" target="_blank">📅 10:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439170">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc3f7ae84.mp4?token=rOr_0Tj4RhthrHZGTx7-phwC0RbIzmyr5MsVJcD6F7Fq3Bp52kacTQQA2xWGtErEuVvxDkTfZiWNu99MLA-e-uyqgDGZeu8OMtobCymv753b42vET896LPfL8PlmKkS-GHDAcFrxadzbvEP6Of0gnRZ_OTtc0-OiygaeVwvBBVKpL0EKsX5kEkduDFxiqdH8Kk1F-n6j-iigTfXSCmZM0SzLN7uo8vhmPGnehm4StMBt1-j8cbMZmIjehPmqghGaHyR5iRYY8_wUR0sb12dzxnY07xq0Ft1x6cijVFizo6OB1Ia-8cWHnrRHTQLIAVjkerSGP-K2XMeW6iNx6XCCtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc3f7ae84.mp4?token=rOr_0Tj4RhthrHZGTx7-phwC0RbIzmyr5MsVJcD6F7Fq3Bp52kacTQQA2xWGtErEuVvxDkTfZiWNu99MLA-e-uyqgDGZeu8OMtobCymv753b42vET896LPfL8PlmKkS-GHDAcFrxadzbvEP6Of0gnRZ_OTtc0-OiygaeVwvBBVKpL0EKsX5kEkduDFxiqdH8Kk1F-n6j-iigTfXSCmZM0SzLN7uo8vhmPGnehm4StMBt1-j8cbMZmIjehPmqghGaHyR5iRYY8_wUR0sb12dzxnY07xq0Ft1x6cijVFizo6OB1Ia-8cWHnrRHTQLIAVjkerSGP-K2XMeW6iNx6XCCtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی وزارت خارجه: مواضع متناقض آمریکایی‌ها دلیل طولانی‌شدن روند دستیابی به تفاهم است
🔹
آمریکا مسئول جنایات رژیم صهیونیستی در لبنان است.
@Farsna</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/farsna/439170" target="_blank">📅 10:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439169">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aso7RHtaLs5vJZ5Vi2-pbnRQF3IawlepiD3gpFCaztj2RBhL2_gsmWpUg-4xKDlUPEq7QAv87cqM20cAuPXSCkBYPZB5PK8ZMYW-ezqK3LI41JkbAbOIkyMpjFeRYZjpZovsbEU5lglZxO9mKiPVfwHx6ILnFynQi4rKrZn4ReiM-IM9T_aHduJyjmkmYjrTEJOqZ8P1ffZ0mK04bdJHOaXe8D_RgyKOP3ATGME3sD3T2eaRk-UsHtA7PBCe1SmsOb74T0uWjCVEQ3kYQDAI6rsiK1rotl-SrqaV8GnGNRRwo4zTer9Aw13i-ivexhn3O_G8B1k2Cp_cKtNwRJRSLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ بخشنامهٔ افزایش حداقل دستمزد کارگران منتظر ابلاغ است
🔹
با وجود اینکه عضو شورای‌عالی کار گفته بود احتمالاً بخشنامه افزایش حداقل حقوق کارگران در سال جاری روز چهارشنبه ابلاغ می‌شود، اما بعد از برگزاری جلسه شورای‌عالی کار در سال جاری این بخشنامه هنوز برای اجرا…</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/farsna/439169" target="_blank">📅 10:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439168">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e9ea95ff4.mp4?token=vvN0eixjbEnSWP-LAZpAvM7F34JWuudgGzVG9MghFktsINoZHFq3IYrI3G1Y2-UGxa1WRDH_k67hBeKejW1g9Sw86IYAN2wtAfnU8-mBHx12kjJZX4vBD1jZwiGyi53B4ys1dVoRJ6hWnwQD7u4VZKqlnPhodziIWWPfgT1MsUpaZhIVuWf8hUeq9KsPlL_cL9Y_rXcihAUgIeylKRxxotVVIyFAHga5CN13ZepMlM65uNv8nv69yaPOYLpwOurvplUl6WzSIb-V4TdmsNhwfmYacEvGSj-89WR4zlB0Gf_4HWjoURnf1w0Zk70ezB0E7-OhU8ia0vD97WooWEWKBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e9ea95ff4.mp4?token=vvN0eixjbEnSWP-LAZpAvM7F34JWuudgGzVG9MghFktsINoZHFq3IYrI3G1Y2-UGxa1WRDH_k67hBeKejW1g9Sw86IYAN2wtAfnU8-mBHx12kjJZX4vBD1jZwiGyi53B4ys1dVoRJ6hWnwQD7u4VZKqlnPhodziIWWPfgT1MsUpaZhIVuWf8hUeq9KsPlL_cL9Y_rXcihAUgIeylKRxxotVVIyFAHga5CN13ZepMlM65uNv8nv69yaPOYLpwOurvplUl6WzSIb-V4TdmsNhwfmYacEvGSj-89WR4zlB0Gf_4HWjoURnf1w0Zk70ezB0E7-OhU8ia0vD97WooWEWKBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
توقیف نفتکش روسیه توسط فرانسه
🔹
رئیس‌جمهور فرانسه اعلام کرد که با حمایت انگلیس و چند شریک دیگر خود، تانکر «تاگور» روسیه را در اقیانوس اطلس توقیف کرده است.
🔹
مکرون در توجیه این اقدام گفت: «دورزدن تحریم‌های بین‌المللی، نقض قانون دریا و تأمین مالی جنگی که روسیه بیش از ۴ سال است علیه اوکراین به‌راه انداخته، برای کشتی‌ها غیرقابل قبول است. این کشتی‌ها که از رعایت اساسی‌ترین قوانین ناوبری دریایی سر باز می‌زنند، تهدیدی برای محیط زیست و امنیت همه نیز محسوب می‌شوند.»
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.82K · <a href="https://t.me/farsna/439168" target="_blank">📅 10:32 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439167">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2ed333f21.mp4?token=LOwi4fvVXATS62iHA9DtyR43iXq3CgZb0X_i3ReJvO0QS2ezm5wM-0TmoF-icS4Qj4CJuDzZ5SloiftByiYOXys_0zWRPgvp0QfAY2gJPzEvtLDPmG5ozqhLQ2uC-yUXu6S3tCV7D_ISG5tbctwD1Xtaaa894e4ghm48RljbnUFFhcJHTlMTSu4CgF52Rma3RQGE4AI6bWaeDWCpU9shyPNE0vGjulCoTn_TZIIDEI_muQwosC6VNXWd64CKXCOwW-08mqgXiLuNbEiSf1gUYFAGP1YvxM2Oz5Oa1ydS7aMKaMbbjhBXBmOty0UbNVy_PPl8_b4edqVb_A9QMy7s0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2ed333f21.mp4?token=LOwi4fvVXATS62iHA9DtyR43iXq3CgZb0X_i3ReJvO0QS2ezm5wM-0TmoF-icS4Qj4CJuDzZ5SloiftByiYOXys_0zWRPgvp0QfAY2gJPzEvtLDPmG5ozqhLQ2uC-yUXu6S3tCV7D_ISG5tbctwD1Xtaaa894e4ghm48RljbnUFFhcJHTlMTSu4CgF52Rma3RQGE4AI6bWaeDWCpU9shyPNE0vGjulCoTn_TZIIDEI_muQwosC6VNXWd64CKXCOwW-08mqgXiLuNbEiSf1gUYFAGP1YvxM2Oz5Oa1ydS7aMKaMbbjhBXBmOty0UbNVy_PPl8_b4edqVb_A9QMy7s0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‌ سخنگوی دولت: فعلا خبری از افزایش مبلغ کالابرگ نیست
🔹
افزایش مبلغ کالابرگ جزو مطلوبات دولت است اما واقعیت این است که باید خواسته‌ها را با داشته‌ها هماهنگ کنیم.
🔹
باید در این زمینه، مطلوب را با مقدور هماهنگ کنیم. باید بررسی‌ها انجام شود و امیدوار هستیم که…</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/439167" target="_blank">📅 10:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439166">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qriT6tYvg9DwZaRiKXGi0ykKqK0kAQqVRRXIAnbk4leLx7fifK3_3NlP2MvZMkcHLNEK21Ku6cVLfwGDdZtMDp06oHzAN_nEmvRUargtLWN38wUXQfufAIuRVRRZZSxdrvwkt6cv0aoWGwgvRQesv8qIcH4GydS668hSBcSw4pUWuZIEHisF6jLyuT4v5bQlYGXyY23iqTJaujcv0RxFJ3nI1be5VYSpdLU0IIRZiPQfVKDVJ8wjPqVvZst__AkW5K01-Dm3pudqn8r-lwjejYH4NC3FIWNszoE0leMI9hpDqBbCmVcUmD41kWvxv-BtHZNXuSZs40VmB6OrIj91Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تالاب سولدوز پس از ۱۵ سال سرریز شد
🔹
در سال‌های گذشته تأمین آب تالاب سولدوز نقده در آذربایجان‌غربی در طول سال از طریق کانال سد حسنلو انجام می‌گرفت اما امسال برای نخستین‌بار این تالاب به مرحلۀ سرریز رسیده است.
🔹
امسال حدود ۵ میلیون مترمکعب آب وارد این تالاب شده که همین اتفاق نقش مهمی در جذب و میزبانی پرندگان مهاجر و بومی منطقه دارد.
🔹
به‌دلیل شرایط مناسب آبی، تالاب سولدوز به یکی از زیستگاه‌های مهم برای تغذیه فلامینگوها تبدیل شده و هر سال در فصل پاییز هزاران قطعه از این پرندگان، اعم از جوان و بالغ به آن مهاجرت می‌کنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/farsna/439166" target="_blank">📅 10:06 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439165">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
سپاه امام سجاد(ع) هرمزگان: صدای انفجار در بندرعباس ناشی از امحای مهمات عمل‌نکرده در جنگ رمضان است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.06K · <a href="https://t.me/farsna/439165" target="_blank">📅 09:57 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439164">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/juh2BZW_uV8eDQ7v1SW5FcQgrE9KaskkSgJETFsSvcyEeKdqlM6UmxhZHR-U81X4Fb3P7FCaJ-WavnoCTx9EPeEJPQzhLFUpD0IJQLzuA1Hxv1GLqwg0xrS0Lp-pbdMSokoLtBTT5gQnjxsLgUIVZrQdh4PYgrTkT1GFp98N4HVrAl8sjmeKK5ohDDw2DPbUIW3_JQCnVYWup4lZS_Lcw8Vadf5URVhtD2OkYNyrsMw3fhW0Wjd3XtC0WfpVMAARFXxXU1Qk4ckhA9Osgti6vsedRXxrIxJUxyFsboYFPrur4dRUPROsMIP1b_IS25bWAyYK0HYsGtIIIlfJHuGsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
سوگند اعضای هیئت‌رئیسۀ جدید مجلس با حضور ۲۰۱ نماینده به‌صورت مجازی و حضوری  @Farsna</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/farsna/439164" target="_blank">📅 09:56 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439160">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zyyh6HQQI6tIAnoLkSeuGaBvRej850sSiwhO6gp5zRT7QvIde7ronFaD6DjGQBYAMiXjptpjLzhRrwZoa205cQZttSsHey7oM_GKSZJjMkfP5RhNi45x3vIwR-OXf_QvFXEMwRW2KzW1qtDqs0WyubYrEiIxjYg5xufiU7CCKud09myyfWhE53Azd16ZrQ5kbRfIADZzK55lQph1B7Knxm0d9eDl8zpy189mijM7QBaRHHKjZpsRSDV0yaKARynsQcaTUm7rSFGncQt-BD1Z-xwZxyCZvA0LH7-DJtDkOmol8N6CE6e7lsIryPkidKkAbt1D_25ULb_ldLOSeOvZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qyVT2T6cKGq9O62qnL7z7h7N0g69vit3caj4ElFD2y_U_O1H19hoPPY7U9WGn4YljEvyzag7eoGcnxkQn29dkTuk4NtDCThMH9z91jfnf3lb1WYigz8byeDtaZi5CDDMQYpf9mRMS92r-1Zfw-RZNM6MjVuP0HTp8fZKxwodVvkYmMWd-VbemxIDx4n_hy6TaD8jgWkmo_8SKCf6UyE_WxQwnzCxeeJMguZ2TISkpAsx5CdsqN6Im5B6m_dmIeTfGYEdyb9A0isl1L87r9enKua95I5K2LHERBqidgFZlFP5xO1i_uNpqyrR6SjXdsKcISMig0XfCaBp91CljNlOkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J2p_yVqITtOuv9eDDFoA21tiPVaWcpiwTabdIddUFI9cArsCOTVT4RW6PZD-P5BjovjYNZrghi5tfpaVL4OYQjmafL_FfaFIhXpEHOS7GgTVRK1GN0isg003VJUHdDKbWWdnwmPGPqJRdceJhS_ykNTGZklvPpEkcMToD72byyEiEVfAoyvXnv3Ga6YISpXh5WAtf86R9ygVJaax3aAskyiXTiKVfH66fBl-AtPHlgafsZRulkOVVEqtlYHARs0zxHhFqij-j9MOWr1iQeJnIpih5su7gKvjXvIWRpY8SSUxF12MVXVntZPtnvIpn62DUmfNDrptG-zUHkGzQY5F3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQBqcInCkqd_J6H-5BkunRc96FYA5VmkKXhEs31Ke2_9TNZWuh3orSd96lPPQ9XZWWHCUK9Sb9nPqTUSEGWm34tz8t3oLRMoRGhEkJmqTg42U3eyGEDF6skGwLgy94szrVUeXm07gH42GMrmgjN1dZyw1rQ8Hz7hQHuxAKZ_5S1ovSfqjz65E78nwTIK9IY7ABjvhV3wnRDtLheTcVtAMGqkFV6x6AeiMEkt-ckKa-uBfseNOlDY_2IEVZIvHFak-Yx_FrhIRNkhpAQVewjNPWdpj0Dm7jZYOPkYGLtC6NPSmBhzLjvkncdQqUPtJP-hPJSP5xhy3FaczR-AFEkV9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پزشکیان: حاکمیت و جامعه در قبال کودکان بی‌سرپرست مسئول است
🔹
رئیس‌جمهور در بازدید از مرکز نگهداری از کودکان بی‌سرپرست روشنای امید: حمایت از این کودکان صرفاً یک وظیفۀ حمایتی یا رفاهی نیست، بلکه بخشی از مسئولیت‌های بنیادین نظام حکمرانی در حوزۀ عدالت اجتماعی، حمایت از اقشار آسیب‌پذیر و تضمین فرصت‌های برابر برای همۀ شهروندان است.
🔹
همۀ ما در قبال این فرزندان مسئول هستیم و باید شرایطی فراهم شود که آنان بتوانند با برخورداری از فرصت‌های برابر آموزشی، فرهنگی و اجتماعی، آینده‌ای شایسته و امیدوارکننده برای خود رقم بزنند.
🔹
یکی از مهم‌ترین موضوعات در نظام حمایت اجتماعی، برنامه‌ریزی برای دوران پس از ۱۸ سالگی است. باید سازوکارهایی طراحی شود که این نوجوانان پس از خروج از مراکز نگهداری بتوانند به‌صورت پایدار وارد بازار کار، نظام آموزشی، نهادهای اجتماعی و ساختارهای رسمی جامعه شوند و مسیر زندگی مستقل خود را با اطمینان بیشتری ادامه دهند.
🔹
حمایت واقعی زمانی محقق می‌شود که افراد بتوانند با تکیه بر توانایی‌ها و مهارت‌های خود در جامعه نقش‌آفرینی کنند و به جای وابستگی، به شهروندانی توانمند، مولد و مؤثر تبدیل شوند.
@Farsna</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farsna/439160" target="_blank">📅 09:50 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439159">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjMIxf5Hsfwx2ldnh-goIVPleSbLMYg9ms3vZYFMf58i4Z96U7_lqtktiblPs26QqSVPiLL-Yr-0wb6oKVQ8tsgqMLHsKVTK44fqShCtjIAZnWzZ1JFrD02GTAaoZhV3K__H12p5x-jgb413m6Ip99r3xI8RL7aEBV43EnZZ2lhL_oiQvydqpcxXRvcItmXA6aVxRu-xHSX-mHwN-Q_76jsnukL43pbZJ-eZWZs59gzPgErPSf8XXFBuztQ7kbBrceV_fremvylUTbRTZs5U4JclNPyTGDWNrwuNNZBlsqeV_trUMgNyDniqpRh5fvb7WCsQSqybsLabH-S3Ka0y9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ارتش اسرائیل به هلاکت یک نظامی دیگرش در درگیری با حزب‌الله اذعان کرد
🔹
ارتش رژیم صهیونیستی اعلام کرد در حملهٔ پهپادی حزب‌الله، یک نظامی از واحد کماندوی «ماگلان» به کشته شده و همچنین ۳ نظامی دیگر زخمی شده‌اند که وضعیت یکی از آن‌ها وخیم گزارش شده است.
@Farsna</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/farsna/439159" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439158">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48844af690.mp4?token=doXK6_WU6Jg3JtNHlC3D6N2R6vPcUGzByN8Y4NQFPHHhoBhJLJb7XqGFS9_BZs0LyDyg3zRHQlA8aKFkZVSqLujPNcv1U2-W3X4eyOp9MOQ6GodOU3xABFeB7N2YKoxnxVJ3RzZeFkNO5ax6Hy2ZlJys4FyqX1zpGXHaoqQAj23VK-88ydxeXiW0RJcmDJdafmSsayiUld-tvYU9xhHpDhGSfx765HEhB9eH_fcpMS-uejPSXnY4U9OnLi2f95McP9fJv7EjXPl0k1NjDEzhDfkvG0KIJARRRWbceoKQFgDWy100vR7MrLTeFFT6TrkzZaznMIxsS1LUq_mrU-RTRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48844af690.mp4?token=doXK6_WU6Jg3JtNHlC3D6N2R6vPcUGzByN8Y4NQFPHHhoBhJLJb7XqGFS9_BZs0LyDyg3zRHQlA8aKFkZVSqLujPNcv1U2-W3X4eyOp9MOQ6GodOU3xABFeB7N2YKoxnxVJ3RzZeFkNO5ax6Hy2ZlJys4FyqX1zpGXHaoqQAj23VK-88ydxeXiW0RJcmDJdafmSsayiUld-tvYU9xhHpDhGSfx765HEhB9eH_fcpMS-uejPSXnY4U9OnLi2f95McP9fJv7EjXPl0k1NjDEzhDfkvG0KIJARRRWbceoKQFgDWy100vR7MrLTeFFT6TrkzZaznMIxsS1LUq_mrU-RTRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گنجی: حاکم‌شدن نگاه عیسی ‌کلانتری در حاکمیت «سم» است
🔹
کارشناس ارشد مسائل سیاسی: کوچک کردن نگاه به آمریکا در شخص ترامپ، یک کج‌فهمی سیاسی آشکار است. مسئله ما با آمریکا مادیات  نیست، بلکه مسئله بر سر «وجود» است.
🔹
کسی که می‌گوید «در حلقوم ترامپ پول بریزیم…</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/farsna/439158" target="_blank">📅 09:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439157">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پول دولت به گندم‌کاران نرسید
🔹
رئیس بنیاد ملی گندم‌کاران:‌ دولت هنوز پول گندم‌کاران را که هفتۀ گذشته قول داده بود پرداخت نکرده. این در حالی است که آنها برای کشت بعدی نیاز به نقدینگی دارند.
🔹
سه‌شنبۀ هفتۀ گذشته جلسۀ تعیین‌تکلیف مطالبات گندم‌کاران به ریاست معاون…</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/farsna/439157" target="_blank">📅 08:54 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439156">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
سازمان پخش اسرائیل: حزب‌الله از بامداد به شلیک موشک‌ها و پهپادها به‌سمت شمال اراضی اشغالی ادامه می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/439156" target="_blank">📅 08:47 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439155">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbZ-cGubT24TCEzu9YYPumX0xeU2MzGqA_FjHq4WJCKGXwk_jGGDSM5TY9HbUSlZSbcLjiQvsp4264rP1HU7ggb6ndURcg7c-kD2DmSsSjqTnpC39VZAg_3MOzWNcg5uVNvqpk2vF8VnFmvXyiU1VFusvs3ZZ7FH3yWeXH4XhhJqM9OktrqkVX5fHNbLQJvsB9i9CAOPZhg18wG8L8DIapVLz0nQXIFte0BqN-z87MjzBrSpkvN4-GoApuSLgRgXimjiQOAfBtmmOk1M06IAJ1K5iUy3zUMw5YA8bPL4npfWXH9H7hRqpcAoguk_sli-z5fRQp0Q-tDlzcP290BL1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیفرخواست قاتل ایلیا صادر شد
🔹
دادستان استان گیلان: پس از تلاش برای شناسایی و دستگیری متهم حادثۀ قتل پسربچۀ گیلانی، دادسرای مرکز استان رسیدگی خارج از نوبت با هدف ایجاد آرامش در جامعه، رعایت حقوق متهم و تعیین وکیل تسخیری در دستور کار قرار داد.
🔹
با رعایت تمام…</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farsna/439155" target="_blank">📅 08:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439153">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adfa5f3571.mp4?token=vt0mAxHzrrXQF2Qr9bU5y5CvzSG2qw8NLthEqmoT9fbShkJ94vJ9TxWSTbgDfMRj1O7wo3WTg8gouQo3XLE0NbFLbNzpMivcLAJGhWZiPR5YNoF0ho8W8B8JrIVv34lYoJ3gvVLudYSQ2OHIABnkRN462rDyXp8SJnzUbeED8ivNiRHVi2Nv6gbA5rmgZsfcL0Fo2TGmhD_W7jiB9lXb-EkwlS5wxk-WCtll7esqYrvs20y8_yc26fap3qxGgtV71STTb0pnX1k_8IeIrv5JFEMu6ZNfS9fSRc7srwrAFrS_T44bfLIUTd_p_HUfcmT-Fx-IwWEVeBaXd3NYviP2-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adfa5f3571.mp4?token=vt0mAxHzrrXQF2Qr9bU5y5CvzSG2qw8NLthEqmoT9fbShkJ94vJ9TxWSTbgDfMRj1O7wo3WTg8gouQo3XLE0NbFLbNzpMivcLAJGhWZiPR5YNoF0ho8W8B8JrIVv34lYoJ3gvVLudYSQ2OHIABnkRN462rDyXp8SJnzUbeED8ivNiRHVi2Nv6gbA5rmgZsfcL0Fo2TGmhD_W7jiB9lXb-EkwlS5wxk-WCtll7esqYrvs20y8_yc26fap3qxGgtV71STTb0pnX1k_8IeIrv5JFEMu6ZNfS9fSRc7srwrAFrS_T44bfLIUTd_p_HUfcmT-Fx-IwWEVeBaXd3NYviP2-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سپاه پاسداران: مبدأ تجاوز به دکل مخابراتی سیریک هدف قرار گرفت
🔹
به‌دنبال تجاوز ساعتی پیش ارتش متجاوز آمریکا به یک دکل مخابراتی در سیریک واقع در استان هرمزگان، رزمندگان نیروی هوافضای سپاه پایگاه هوایی مبدأ تجاوز را مورد هدف قرار دادند و اهداف پیش‌بینی شده…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farsna/439153" target="_blank">📅 08:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439152">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb82734318.mp4?token=G4KDt0dCTfAh_0tXEM-T-Ij3BOxO_pLCgpV85GFyqLobEowHgDhqjYF3Ejh25yG1mviW2949Mi8VpSoDXGEgtCd_okxsyZ6GkPE2D8r6lGwQD4lpnoW90PoYS8CiSqZ1DfAac79eRu3V6t8SfJ0H7nfDAZSgeUQZaw4ff7qwabvFIsSud-vB7xTVjLP3kIOqr3Ir_W45y1EGz5FmEyB-7YIoVpFVsT80wMHs0dXaly6IoKhTsJR6b7RxEgD4E-TJ7BxD_jiUPIDjIjBXp-C_1AjndmC3rk0NQCUj-JVBgKKhGPZPG2by2-a9_I-l48A5DqohQunAwZpCvfHJsF5BbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb82734318.mp4?token=G4KDt0dCTfAh_0tXEM-T-Ij3BOxO_pLCgpV85GFyqLobEowHgDhqjYF3Ejh25yG1mviW2949Mi8VpSoDXGEgtCd_okxsyZ6GkPE2D8r6lGwQD4lpnoW90PoYS8CiSqZ1DfAac79eRu3V6t8SfJ0H7nfDAZSgeUQZaw4ff7qwabvFIsSud-vB7xTVjLP3kIOqr3Ir_W45y1EGz5FmEyB-7YIoVpFVsT80wMHs0dXaly6IoKhTsJR6b7RxEgD4E-TJ7BxD_jiUPIDjIjBXp-C_1AjndmC3rk0NQCUj-JVBgKKhGPZPG2by2-a9_I-l48A5DqohQunAwZpCvfHJsF5BbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
صاحب‌خانه‌هایی که هوای مستاجران را دارند
🔹
وزیر شهرسازی: تعیین سقف افزایش اجاره‌بها به میزان ۲۵ درصد و تمدید خودکار قراردادهای اجاره به سران ۳ قوه پیشنهاد شده و پس از تصویب ابلاغ می‌شود.  @Farsna</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/farsna/439152" target="_blank">📅 08:24 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439150">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joHPLVG7FUvuGcSjo0yuOdNGEt7Tz2v4rcZgktEHzGZUKvcNAws6Pg4nqkVlD9f_EhuQXR9GzI_577Kth8Yd54LYqibPglBs9ycHcqtY1xb_0Ul895F5YtmOsjnwnjTE081IO-iTnjIKFsydvkCruWRq3rj_HfEiUphlOGDnyX5G6tZBJd2iAXewzBo1ulJ2IFQQ-NH-vlEQs82M99xQn7NDJEpPYNWymb2sxiieryDy7bzP7-B2pLJIf-xRGqQgqZqG4y-NcJtDBZe2o2Fm8WTAPChDBaCJ3Osu4boRvvTHOsL194YE0k3tPifm7EtlQMj6vw4HCwzPzs0nFE0tGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJuxvb5kV3bdZHs0DL5-MI4brJ1Oinq_YaXRdWruTxzJgxN2YIpUnTLZGvGG2OwYCKTR7GYi62EAGrYi_d1fApKunNF2K5HGWSdcWepdtRDTa1gOYzDt68y-uYwwEYY42i6KDfbrx8uE_aa59KuJw4_A5VMvgpMj6-UhDsG9i9OdotpXe5YH40FagyeAaOF4Tt1pIFNrs2VXP2jSZG9w8B3azbxZOjXKzBu_mfr1msu1XrTeludcM7bI1PYQefBOP-0shgnILGG0IVLeH9jXvchXIA4bYTU4iIdBfMCpsSUo1R0vH0LA7WZ_bDKOFb1Ve-_MTwLaUcSvan41pEy79g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎥
عوامل آتش‌زدن مسجد جعفری و حوزهٔ علمیهٔ امام هادی در کوی نصر تهران پای میز محاکمه آمدند.  @Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439150" target="_blank">📅 08:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439149">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اذعان اندیشکده‌های غربی به غیرقابل اعتماد بودن ترامپ در فرایند مذاکرات با ایران
🔹
موسسۀ ران پال: ترامپ در ۱۱ نوبت ادعای پایان جنگ یا حصول توافق نزدیک با ایران را مطرح کرد که همگی فریب آمیز بود و دیگر کسی سخن دروغگو را باور نمی کند.
🔹
فارین افرز: تضمین‌های آمریکا قابل قبول نیست زیرا ترامپ به علت حمله به ایران نمی‌تواند اعتماد تهران را جلب کند و تعهدات مورد نیاز را ارائه دهد.
🔹
کریتورز سندیکیت: اعتماد سکۀ رایج دیپلماسی است، اما دولت ترامپ نه فقط غیرقابل اعتماد، بلکه قابل باور شدن نیست.
@Farsna</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/farsna/439149" target="_blank">📅 08:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439148">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e9fc39208.mp4?token=FY7HJQPv5E-haEE3g2g1Nqpwrl18kKO_1kQTjOYHUusabUlr0Uaep6iCmxHsITzqUJ6skwGz4LMfU3nix-zASjS-eN6IyQJofKW6N_fTaHCr2Ap4ByT6j4xLQ6sInnA3Mi7kkvQpYZ-pJ7Yw5BfHx1N6Fiuh08ElZjPv7iTdhaAzzfVN_hAdeNfKwMMEoL0GrbqcgO3gkAhl_BX_A4x2a93l8gmZGHZziU4wkaPxEDShUjBCOV4ylMpwYlS2NH3r_fcCahLOXhaMDMXewHdWumXMZTNmZX7Umc_ZUFijHym7Oirk_Y42TA7umTdBAyB_AXT_DQtqf6G2mCImO7BCSZkPGP20skyVEFIRH3Mxj8EEd_8wydIb1Ur54iyYsLdQbL3r1bEbmzgfK9GuK_Uiw5q2THIBg-5VQqfVQqIudqnvEq_KeJce_uTg4B2wJyFZdh6hK3j9Mg0td1mNnpsDuXeS6AdHabb2FNn7LBuakqF0tKtnWNg-dTf7Ndl_FelrG-kl1LQzQG3uzZAIyewNUIbv5WUHHXBEO-cbWBI0RnvUuEDqtYdw8HMC2-25ZWk-wJSOkIs6iyuC3bdqV_pW1uIUhxPpUZ8-b55bYm4X_DLyJAniRd7BjBzhol1hgPkAoOB88qCbxXd0l5VPhb4abIMclgVYH5fPfR-p2xWT15g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e9fc39208.mp4?token=FY7HJQPv5E-haEE3g2g1Nqpwrl18kKO_1kQTjOYHUusabUlr0Uaep6iCmxHsITzqUJ6skwGz4LMfU3nix-zASjS-eN6IyQJofKW6N_fTaHCr2Ap4ByT6j4xLQ6sInnA3Mi7kkvQpYZ-pJ7Yw5BfHx1N6Fiuh08ElZjPv7iTdhaAzzfVN_hAdeNfKwMMEoL0GrbqcgO3gkAhl_BX_A4x2a93l8gmZGHZziU4wkaPxEDShUjBCOV4ylMpwYlS2NH3r_fcCahLOXhaMDMXewHdWumXMZTNmZX7Umc_ZUFijHym7Oirk_Y42TA7umTdBAyB_AXT_DQtqf6G2mCImO7BCSZkPGP20skyVEFIRH3Mxj8EEd_8wydIb1Ur54iyYsLdQbL3r1bEbmzgfK9GuK_Uiw5q2THIBg-5VQqfVQqIudqnvEq_KeJce_uTg4B2wJyFZdh6hK3j9Mg0td1mNnpsDuXeS6AdHabb2FNn7LBuakqF0tKtnWNg-dTf7Ndl_FelrG-kl1LQzQG3uzZAIyewNUIbv5WUHHXBEO-cbWBI0RnvUuEDqtYdw8HMC2-25ZWk-wJSOkIs6iyuC3bdqV_pW1uIUhxPpUZ8-b55bYm4X_DLyJAniRd7BjBzhol1hgPkAoOB88qCbxXd0l5VPhb4abIMclgVYH5fPfR-p2xWT15g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
نصب کتیبه‌های ولادت امام هادی(ع) در حرم مطهر رضوی
@Farsna</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farsna/439148" target="_blank">📅 07:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439147">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
سپاه پاسداران: مبدأ تجاوز به دکل مخابراتی سیریک هدف قرار گرفت
🔹
به‌دنبال تجاوز ساعتی پیش ارتش متجاوز آمریکا به یک دکل مخابراتی در سیریک واقع در استان هرمزگان، رزمندگان نیروی هوافضای سپاه پایگاه هوایی مبدأ تجاوز را مورد هدف قرار دادند و اهداف پیش‌بینی شده منهدم گردید.
🔹
نیروی هوافضای سپاه اخطار داد در صورت تکرار تجاوز، پاسخ کاملاً متفاوت خواهد بود و مسئولیت آن به عهدۀ رژیم متجاوز و کودک‌کش امریکا است.
@Farsna</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/439147" target="_blank">📅 06:58 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439146">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
فعال‌شدن آژیر خطر در کویت
🔹
برخی منابع از فعال‌شدن صدای آژير هشدار در کویت خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/farsna/439146" target="_blank">📅 06:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439145">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j38IyDP2ppDw0yorwN2mRSNr1Xniun3K9eFpTAAiLNW3sSrzzztMZ50QLWFJjWp8hZFqN51HLIGRzQbXN2zqXxWMgyk5V0gfCA1rg8goqWoxKUnHlCykpQQ78O_BKab2OFHkfb7SOPQVVbvYja8KBZDbNGXNRq9nYHIH-isun0i7yOpPq1mRChoj2KtlSNUnDJAul011GzLCFQObEPe1BaaNiltVcquQMvtKvL4JXJzvVWB8pGH05iOSohcpVRI8sVE8iUV_Xw3Ne-h0ouT6QASokhX8IdMQGAGlNyG5XK3nRBZZJnsM_DN5VDrwHrt87P3lUp2HGwTRcn7oI3sg4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورژانس تهران سرعت گرفت؛ ۱۰۰ موتورلانس جدید وارد میدان شد
🔹
قائم مقام اورژانس استان تهران: با بهره‌برداری از ۱۰۰ دستگاه موتورلانس جدید، ناوگان موتورلانس اورژانس تهران به ۴۳۰ دستگاه رسید.
🔹
ارتقای این ناوگان، زمان رسیدن خدمات امدادی به مددجویان را به زمان استاندارد ۱۲ دقیقه کاهش داد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/farsna/439145" target="_blank">📅 06:29 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-439144">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2SlvtVLFyzo0fCIdI6sAJ-TCWAQr6AlVifsH0d9gymNE2551zOrVMK4OPP9AXXkQINqHJQUdL9EAwPo5enwJzR1aqoCfVwsnce5j4j-heRi8LnDyQMOB602XnrhffYU_xB00bjg8FtpCtUrtMmDBGGysbZc-Lvir3pLKjTIv-rdfChqD8ftskNxnZl0xgF9QJj14ffWU5FWcOr9WlPhgWjluMGZqOlZUpGrHostxYH1iIq8hfGDiPhqT6EI9KXJwCNr0Ouqu7s5S2vQPCuGINywytCsTViYMgHo9rJX880hnHBLh7KguTCuf4Uzjigmjp8cY1NI_2QWKS5yUPPKLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار مرگبار مواد شیمیایی در آمریکا
🔹
وقوع انفجار در یک کارخانۀ بسته‌بندی در ایالت واشینگتن آمریکا، منجر به کشته‌شدن، و مصدومیت تعدادی نامعلوم با سوختگی شیمیایی شده است.
🔹
به گزارش گاردین، آتش‌نشانی لانگ‌ویو اعلام کرد که این حادثه پس از ترکیدن مخزن محلول…</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farsna/439144" target="_blank">📅 05:57 · 11 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
