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
<img src="https://cdn4.telesco.pe/file/KRARA2KsghrzjpZ0CM7UOX7J0DPvyG85Qf_0J7ZIJhXQnRHiOmVquN8C-o-P8nX1oE-9ULBqWKbLpC6wGpezzszYT6BybfXMbJxM4MuYeAV8vxkuizVrgqCSeFM4iZn_oSoh8b8M565GJ8i_XIRYoUABbof26sBSVqsRS5DdbuAOFZpnq6yH_lBDWm1VpIYuJOsy7iyPCPP-IfOJBlV4TpX4xumOP3jbMsTXPirCP1IM4GtdpEPoFkO0UQ80aruU024WOC9n7rvcbRxniTkTt2olMefc_jEjVBuwEfZkdPOvTO-0rz7OyJBU47RRt8xs9N_LYcKfcSroNARN_fHQAw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.82M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-31 23:13:08</div>
<hr>

<div class="tg-post" id="msg-457619">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47ea101e81.mp4?token=oQ6cIWYI1A-SjSGT--V1ooRripct1rzqUUr8TGy6l4D90thC12wRKD22dT85wa5yAJvgiNM_NYNHe8sZI-5yNFaZVr9D_-l_oYVlt4pxH6gdFstYIdYcWU304VbhAWuM3QJH9fBt0rlVlLWV0tW0jCzT3AILmBxA3Lbtbxjfq9VWrXl-7EzCeLHJDIzM2DoKmt16RiqtXz0vxcEpMESI3kqA40HkttXCwytmVoJOZWI3MBHu0Z3MulZyGq3G5oJTi7uis_i34bOR4X6bOgEUR3fngWuZKdJAOwNVNX6DAAFNV4V2bi9Q6hBPj8pzJTnAzLs7Kl8_fvHivCjQ0bCD3in23V201_7DtKStxWf7FPCaPZO2wyNRLIm6UrUsG0z47sa13s0zcyJ5OSNZMKTGaiZEFzitclr99lAfOnUQci67lh0ooalvr9Va2VstGLTaEi1N7PWSC8NAO8PxX9ZGAXSEcUD2y4XuMZCze53tmOOJ5FzXAeNTgG8Rx1LcWtVKaeShUp2nOFsUWH6MHO6XZFL_IZxZwo8F_bQleGaaT493pOXa7rQ68ohx8iOiYfl0YdgGu-G7ap8ECLI-NBuW_RTjYGnmv2CYrjy8LwIEZWHX5ekbFcp0xyfhRSOPJokpSQ7aRc1I-miwmOblk4ecypNwd8prP5qstUl49UZFEH4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47ea101e81.mp4?token=oQ6cIWYI1A-SjSGT--V1ooRripct1rzqUUr8TGy6l4D90thC12wRKD22dT85wa5yAJvgiNM_NYNHe8sZI-5yNFaZVr9D_-l_oYVlt4pxH6gdFstYIdYcWU304VbhAWuM3QJH9fBt0rlVlLWV0tW0jCzT3AILmBxA3Lbtbxjfq9VWrXl-7EzCeLHJDIzM2DoKmt16RiqtXz0vxcEpMESI3kqA40HkttXCwytmVoJOZWI3MBHu0Z3MulZyGq3G5oJTi7uis_i34bOR4X6bOgEUR3fngWuZKdJAOwNVNX6DAAFNV4V2bi9Q6hBPj8pzJTnAzLs7Kl8_fvHivCjQ0bCD3in23V201_7DtKStxWf7FPCaPZO2wyNRLIm6UrUsG0z47sa13s0zcyJ5OSNZMKTGaiZEFzitclr99lAfOnUQci67lh0ooalvr9Va2VstGLTaEi1N7PWSC8NAO8PxX9ZGAXSEcUD2y4XuMZCze53tmOOJ5FzXAeNTgG8Rx1LcWtVKaeShUp2nOFsUWH6MHO6XZFL_IZxZwo8F_bQleGaaT493pOXa7rQ68ohx8iOiYfl0YdgGu-G7ap8ECLI-NBuW_RTjYGnmv2CYrjy8LwIEZWHX5ekbFcp0xyfhRSOPJokpSQ7aRc1I-miwmOblk4ecypNwd8prP5qstUl49UZFEH4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بروجردی‌ها: ایرانی غیوریم، منتظر ظهوریم
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/farsna/457619" target="_blank">📅 23:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457618">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df6a14667a.mp4?token=rD5ifXmdaBRIsCv5mmVIZNNyqaYSvOCFXRsDdPuQeugYFRcNdxW8m0Rr4p5W0uXfsVwGDZJq8xL-gQtfubhixMii4CGZPvai79TgcnfXEm3a7xos1WS1ryfHya1RENnzm3BScNlXpBDB_eNRakLBkxLnPtfQlGt8K-BbKQxwXpcWJnUnSeTCDRoNpSQCTjB1-7HXIqMStobFOAnoVoWYDikNGazqkcLf50gcq_DElFvzgpyXO_zZ1lMEIn2SGuV6Sk5YDnzLjftkiEbqnkwtIbf8Hny_FI1LD3nTV2scxbzxJdw_Dtr7SR_QoHvNUpIt4SJASmKQVkoi_tHU6_Ceww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df6a14667a.mp4?token=rD5ifXmdaBRIsCv5mmVIZNNyqaYSvOCFXRsDdPuQeugYFRcNdxW8m0Rr4p5W0uXfsVwGDZJq8xL-gQtfubhixMii4CGZPvai79TgcnfXEm3a7xos1WS1ryfHya1RENnzm3BScNlXpBDB_eNRakLBkxLnPtfQlGt8K-BbKQxwXpcWJnUnSeTCDRoNpSQCTjB1-7HXIqMStobFOAnoVoWYDikNGazqkcLf50gcq_DElFvzgpyXO_zZ1lMEIn2SGuV6Sk5YDnzLjftkiEbqnkwtIbf8Hny_FI1LD3nTV2scxbzxJdw_Dtr7SR_QoHvNUpIt4SJASmKQVkoi_tHU6_Ceww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: جولانی هرچقدر توانست در مقابل آمریکا کوتاه آمد اما همین ۲-۳ روز پیش اسرائیل به سوریه حمله کرد؛ کسانی‌که فکر می‌کردند اگر پهلوی می‌آمد ایران گل‌وبلبل می‌شد این موضوع را ببینند
🔹
اگر پهلوی را می‌توانستند روی کار بیاورند ایران را…</div>
<div class="tg-footer">👁️ 664 · <a href="https://t.me/farsna/457618" target="_blank">📅 23:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457617">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e63ee9ece7.mp4?token=UtAGAdW1gL8YmmUQAy9YhElnoRaxtDCRyMYywiyzA4P0dCASPVVbwg_byS-j2LTbTXSLcbLsxLA-0bGYhxYimUWkop4W42EiblgBLdpPq1EkWF_XXiyntIkIIcWxX8CcbqRGYJFCtlJrQUbh5kwmFszQYoW2-f-IS3wZjCpEccNhROqw61CnauniDio_CRjfLN4cYO2XMu4HoRd9PmXos1wwhbwcl3nBZf5Eg3aD1Vpa9JB3iER1Q8bx3tGswY59ZMDfuq4OBbMqEmfjfr9iK7Mzwu_pLa4T__3TrSrgVW6bgiFt9Jxdn11G_MVgiTfyBZYasvAvmbRaKSTZfg6Stw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e63ee9ece7.mp4?token=UtAGAdW1gL8YmmUQAy9YhElnoRaxtDCRyMYywiyzA4P0dCASPVVbwg_byS-j2LTbTXSLcbLsxLA-0bGYhxYimUWkop4W42EiblgBLdpPq1EkWF_XXiyntIkIIcWxX8CcbqRGYJFCtlJrQUbh5kwmFszQYoW2-f-IS3wZjCpEccNhROqw61CnauniDio_CRjfLN4cYO2XMu4HoRd9PmXos1wwhbwcl3nBZf5Eg3aD1Vpa9JB3iER1Q8bx3tGswY59ZMDfuq4OBbMqEmfjfr9iK7Mzwu_pLa4T__3TrSrgVW6bgiFt9Jxdn11G_MVgiTfyBZYasvAvmbRaKSTZfg6Stw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: بازشدن تنگۀ هرمز هیچ ربطی به توافق ایران و عمان در مورد مسیر میانی تنگه ندارد
🔹
در زمان بازشدن تنگه ما آن را مدیریت می‌کنیم و این مدیریت با دریافت هزینه همراه خواهد بود. @Farsna</div>
<div class="tg-footer">👁️ 1.63K · <a href="https://t.me/farsna/457617" target="_blank">📅 23:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457616">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5154e38b47.mp4?token=lahq105LrDwvPjnoAKi6i_x6z58WTFpmLzNRE7SVizoMtp8nlZBpsGayycY-hNixwRKCxXddIGgetr800QvAihjTj7OvP0m_r8o1RLhqpJdDVNPSWtaAeoYFVjGM3PAWOKZFWMqgYsa0oqm-Wj8iPU8-IJ6lUZTCNyd-jAHjQ7-aZ1xRfdiZO2V6M7dW207Ha87dxHLy2cESxz6oHApbYyq-4tZxU5dy8Qy-dhkDq3x6-Q_PUNQg_OgSvXnzF9gll3ZJbp0cexZl15XLE6tfGwpPNHgburRQaIlm5yJKceQcC2F0QcYCf4uI6g58xR0VA7M_FXHcdOEiKFtv6zk-0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5154e38b47.mp4?token=lahq105LrDwvPjnoAKi6i_x6z58WTFpmLzNRE7SVizoMtp8nlZBpsGayycY-hNixwRKCxXddIGgetr800QvAihjTj7OvP0m_r8o1RLhqpJdDVNPSWtaAeoYFVjGM3PAWOKZFWMqgYsa0oqm-Wj8iPU8-IJ6lUZTCNyd-jAHjQ7-aZ1xRfdiZO2V6M7dW207Ha87dxHLy2cESxz6oHApbYyq-4tZxU5dy8Qy-dhkDq3x6-Q_PUNQg_OgSvXnzF9gll3ZJbp0cexZl15XLE6tfGwpPNHgburRQaIlm5yJKceQcC2F0QcYCf4uI6g58xR0VA7M_FXHcdOEiKFtv6zk-0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: کاملا آمادۀ عملیات هستیم اما با یک شیب منطقی و عاقلانه حرکت خواهیم کرد.  @Farsna</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/farsna/457616" target="_blank">📅 23:00 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457615">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/023bde6b18.mp4?token=hXDZ9a0VYfwqiT3kdSxJpUW-SB0JymVT_IbcooygX2VmaVJskSi-j422-PcJmu65-hzg11duE_zrPLERXh85D5fAAjv6rduxLeArexREeNn_qzf0MCiUaLvA_hh5teflTY___4eiKgldv-7j5TBC9e3BT-ElMiidQQQU6L9OvHwy0CkAxxWueG1XjXBEFRC7pe79ubtP-cZVv0_GtbRhTSd4rvBDP8AZvWKX4ZmMMU0jgKVMaNu64LMCKB5av3VluD2dCjFv_uOphqkzpT_fJp3HmR--c93TGZqJ7u-8BVt3Jc7Md1WGgzp0W_b7ZDay9hrq7Uwp9iCpF4ORPT5gjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/023bde6b18.mp4?token=hXDZ9a0VYfwqiT3kdSxJpUW-SB0JymVT_IbcooygX2VmaVJskSi-j422-PcJmu65-hzg11duE_zrPLERXh85D5fAAjv6rduxLeArexREeNn_qzf0MCiUaLvA_hh5teflTY___4eiKgldv-7j5TBC9e3BT-ElMiidQQQU6L9OvHwy0CkAxxWueG1XjXBEFRC7pe79ubtP-cZVv0_GtbRhTSd4rvBDP8AZvWKX4ZmMMU0jgKVMaNu64LMCKB5av3VluD2dCjFv_uOphqkzpT_fJp3HmR--c93TGZqJ7u-8BVt3Jc7Md1WGgzp0W_b7ZDay9hrq7Uwp9iCpF4ORPT5gjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما تاکنون به هیچکدام از منافع اقتصادی آمریکا حمله نکرده‌ایم
🔹
تاکنون ما فقط پایگاه‌های نظامی را هدف قرار داده‌ایم اما اگر قرار باشد جنگ اقتصادی را جلو ببرند آمادۀ هدف‌قراردادن همۀ شرکت‌های نفتی و اقتصادی آمریکا در منطقه هستیم.…</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/farsna/457615" target="_blank">📅 22:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457614">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e79a6b6eb.mp4?token=VWTnjQw-9LRichx7MYrB6NpYb9joXQnAz04ykrHZZX7edsmSyvKSMsvA01UgPCxIts7OwSDHFDYrG4SV4wEcw94-TjNceFcqaRaDRDe4PMPJ3pmz8sqL5B_QdbHltKRck3a-7Fr7pAx0oRQEJswdHWGS9HrgyM9EOwcRwLj6OkkAirXBX0EUtEIhi3osS4L-y7lJhEvwiHNVpZdGdSp5DA0tyts0VmvOEjjK6wUy7bR4fkbh-Ghy6B0jwafXPHWxIOTe1Jj2ft9hEylJnAmKksUJ8WI0iCzIfjJivdlr2O9RbN0Py2UlgUMWK-KCGHIWatEk4IZvzYpjE_3-GxJc8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e79a6b6eb.mp4?token=VWTnjQw-9LRichx7MYrB6NpYb9joXQnAz04ykrHZZX7edsmSyvKSMsvA01UgPCxIts7OwSDHFDYrG4SV4wEcw94-TjNceFcqaRaDRDe4PMPJ3pmz8sqL5B_QdbHltKRck3a-7Fr7pAx0oRQEJswdHWGS9HrgyM9EOwcRwLj6OkkAirXBX0EUtEIhi3osS4L-y7lJhEvwiHNVpZdGdSp5DA0tyts0VmvOEjjK6wUy7bR4fkbh-Ghy6B0jwafXPHWxIOTe1Jj2ft9hEylJnAmKksUJ8WI0iCzIfjJivdlr2O9RbN0Py2UlgUMWK-KCGHIWatEk4IZvzYpjE_3-GxJc8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما با عمان روی مسیر تنگۀ هرمز توافق کردیم که یک مسیر میانی است اما این موضوع روی کاغذ است و تنگۀ هرمز زمانی باز می‌شود که آمریکایی‌ها به تعهداتشان عمل کنند.  @Farsna</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/457614" target="_blank">📅 22:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457613">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5818c5a880.mp4?token=eMqrBEv1xQqSOtzaePa5bNEvXI-hl2H3MDLG3B5KvEM1jOcOVF3o3tonQfgJchKWdGszCa0ikQXKKzlSrk946v1vdSnU1F_PhutF4jOsf3FP8m9tXu1pbiRV8jkcPrGVGZONpQL6zWojs15Xy4gBxJs0-6ZJRCpDPW2Sl247lb0HHdnnC16pRDCrJ3fpE4OpMYC6UqIqVGyz69E2szljx0xIVECujI2kLdf2CV00FWiI48hu64BYG8X48yAeL60dA9jVy6iR_V1uRUVoWrY0xEtyUBRqP5gqUlvQw5pWa_aPVGC8UG39xrhwAI_mmx9L4S2ryzbvt1e_7bEOsWPLug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5818c5a880.mp4?token=eMqrBEv1xQqSOtzaePa5bNEvXI-hl2H3MDLG3B5KvEM1jOcOVF3o3tonQfgJchKWdGszCa0ikQXKKzlSrk946v1vdSnU1F_PhutF4jOsf3FP8m9tXu1pbiRV8jkcPrGVGZONpQL6zWojs15Xy4gBxJs0-6ZJRCpDPW2Sl247lb0HHdnnC16pRDCrJ3fpE4OpMYC6UqIqVGyz69E2szljx0xIVECujI2kLdf2CV00FWiI48hu64BYG8X48yAeL60dA9jVy6iR_V1uRUVoWrY0xEtyUBRqP5gqUlvQw5pWa_aPVGC8UG39xrhwAI_mmx9L4S2ryzbvt1e_7bEOsWPLug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما فعلا فقط جریان نفت در تنگه هرمز را محدود کرده‌ایم اما درصورت جنگ اقتصادی اجازه نمی‌دهیم نفتی از خلیج‌فارس حتی به روش‌های دیگر خارج شود.  @Farsna</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/457613" target="_blank">📅 22:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457612">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1939831dcf.mp4?token=BZZPE7vENL5BgNCZeXfZv3TtGXepbYUGFx903GksoNA6nETH3OMvr4g8LY-971HUM_5bsVFnlap346riel6hfYHouYaYXflANoGTYfTIBHjSlQjYbbkRLI29VCr8YXEzHzXwop5dqHyMfoAazEXQWDHkjIRRZwvBeICJ_jIP8aa8CUsOkFKnthvpEtgef84rTG9YVONIu2LyNFMxMUyA9gt63k3b5yOpBmhhh3y3HVLrZlobW7Nx6vk6i0VQUk20XzfghPsiTLhBMMpQ4oSNChSlgyZF1UpRMvKaTMPGUdPq6zb70fAyIzqxIu1LI_uX0kiwQSRojvmeMiZBICvEYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1939831dcf.mp4?token=BZZPE7vENL5BgNCZeXfZv3TtGXepbYUGFx903GksoNA6nETH3OMvr4g8LY-971HUM_5bsVFnlap346riel6hfYHouYaYXflANoGTYfTIBHjSlQjYbbkRLI29VCr8YXEzHzXwop5dqHyMfoAazEXQWDHkjIRRZwvBeICJ_jIP8aa8CUsOkFKnthvpEtgef84rTG9YVONIu2LyNFMxMUyA9gt63k3b5yOpBmhhh3y3HVLrZlobW7Nx6vk6i0VQUk20XzfghPsiTLhBMMpQ4oSNChSlgyZF1UpRMvKaTMPGUdPq6zb70fAyIzqxIu1LI_uX0kiwQSRojvmeMiZBICvEYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: آمریکایی‌ها هر نیروی جدیدی به پایگاه‌هایشان اضافه کنند آن پایگاه را می‌زنیم
🔹
آمریکایی‌ها هر حرکتی در مسیر جنوبی تنگۀ هرمز انجام دهند هدف قرار می‌گیرند.
🔹
آن‌ها هر جلسه‌‌ای با گروه‌های ضدانقلاب در منطقه برگزار کنند ما آن‌جا را…</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/farsna/457612" target="_blank">📅 22:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457611">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f680f0b1b5.mp4?token=IQISc2H-r1Q1YEvnBmyVkj1AIqR6RJHFtVjufZy4WQSWrSXLfTtAaVk9vggt4Ua6329M1aQNcuNrb6aaiVbWbK5MCD9OATHb4JiVt2TzI6RG6X16M4iYTObcX6KwP1nn65SF-UY1zD2p4eI40hFUOiuFXPpXt50AT3VePBSwB-QceI5w1qf85GhVvxFUv4efRAhqrYoYSNqLzlUtK4Ur92fiKyaLafw-R_-P1bexRGEnGflWO6dos8gnhbhPDVnc73zVf599qygHkFBitCr7NVOsHi7f2p5bLe1s6cKgPEohn5m34Jtw7T4cs_6pPFk2zZ6AldmFi0-h-HGB1h0HFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f680f0b1b5.mp4?token=IQISc2H-r1Q1YEvnBmyVkj1AIqR6RJHFtVjufZy4WQSWrSXLfTtAaVk9vggt4Ua6329M1aQNcuNrb6aaiVbWbK5MCD9OATHb4JiVt2TzI6RG6X16M4iYTObcX6KwP1nn65SF-UY1zD2p4eI40hFUOiuFXPpXt50AT3VePBSwB-QceI5w1qf85GhVvxFUv4efRAhqrYoYSNqLzlUtK4Ur92fiKyaLafw-R_-P1bexRGEnGflWO6dos8gnhbhPDVnc73zVf599qygHkFBitCr7NVOsHi7f2p5bLe1s6cKgPEohn5m34Jtw7T4cs_6pPFk2zZ6AldmFi0-h-HGB1h0HFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: پاسخ ما به ترامپ مقابله‌به‌مثل زلزله‌وار خواهد بود
🔹
به هر کشوری که با جنگ اقتصادی آمریکا علیه ایران همکاری کند ابتدا تذکر می‌دهیم و اگر ادامه دهند منافع آن‌ها را هدف قرار می‌دهیم. @Farsna</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/farsna/457611" target="_blank">📅 22:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457610">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dff8f0bd5.mp4?token=TNA81KIYJfHGpIFtbtnQ330XuodYJjVsiiCbcUTn341-ynVOmBgSFfYfrvg3H8crkArV-o34UymboTALXovFmC3FTCs1P-qXqe87swz9Sdkt7rZdOLufO8ph6mYsaV_TT-VNomL-KUf8moPoygkQcktE_zz793JdpRgP8c-OS0KsWiMLYm21Fi5AEtXfoTl4MeMHUQ76DtieSst_I-Rhg3GuzPmnxdeM4PX2whiXhwsmWKM1sRJbcJ0iHb8pv2vwJuZBmMVm5O9BQ0S7ww4XfR3oWOu04Pv03RgFTRNRy3y5JXpMw5NcSSSKNj8Lh3YLyYu25KQo5CAZZ2wJRH3hUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dff8f0bd5.mp4?token=TNA81KIYJfHGpIFtbtnQ330XuodYJjVsiiCbcUTn341-ynVOmBgSFfYfrvg3H8crkArV-o34UymboTALXovFmC3FTCs1P-qXqe87swz9Sdkt7rZdOLufO8ph6mYsaV_TT-VNomL-KUf8moPoygkQcktE_zz793JdpRgP8c-OS0KsWiMLYm21Fi5AEtXfoTl4MeMHUQ76DtieSst_I-Rhg3GuzPmnxdeM4PX2whiXhwsmWKM1sRJbcJ0iHb8pv2vwJuZBmMVm5O9BQ0S7ww4XfR3oWOu04Pv03RgFTRNRy3y5JXpMw5NcSSSKNj8Lh3YLyYu25KQo5CAZZ2wJRH3hUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ترامپ به اسم عملیات آزادی ۳ ناوچه به‌سوی تنگۀ هرمز روانه کرد و وقتی هر ۳ ناوچه را زدیم، او ۴۸ ساعت بعد گفت عملیات را متوقف کرده‌ام.  @Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/457610" target="_blank">📅 22:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457609">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c27175536.mp4?token=rWcXmwXPoDCro2aK49E1bxnR-gMbt9lQJH-ZQ8Ds0Tf04MZ-JiCNAl7r5WbmgPr25zoeIC47KUQjUUoZJYXvLOK9viEh7tyB-XBmO4kdYhL055Gn4XuzymGiNVstV4iMzx26Kdqs5prPtP1Hu3fEDkL5hZGRXXMeFI3tvfeMXwLcvEF3qTeVozPVDCDon6l5hlEjVk1WOpBKL9e3qGFeQxm3rky0IiI4enlJitay-6UVdTRlkmrq8LXaN1NMwU2WKDLA5ICbcK4SGh_3Gh0ADV04c2NBOhbGjhTpGOpHPvod1NKSzKDijmvGb9XswYKE2QAL892fZbdVWn04W9v-hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c27175536.mp4?token=rWcXmwXPoDCro2aK49E1bxnR-gMbt9lQJH-ZQ8Ds0Tf04MZ-JiCNAl7r5WbmgPr25zoeIC47KUQjUUoZJYXvLOK9viEh7tyB-XBmO4kdYhL055Gn4XuzymGiNVstV4iMzx26Kdqs5prPtP1Hu3fEDkL5hZGRXXMeFI3tvfeMXwLcvEF3qTeVozPVDCDon6l5hlEjVk1WOpBKL9e3qGFeQxm3rky0IiI4enlJitay-6UVdTRlkmrq8LXaN1NMwU2WKDLA5ICbcK4SGh_3Gh0ADV04c2NBOhbGjhTpGOpHPvod1NKSzKDijmvGb9XswYKE2QAL892fZbdVWn04W9v-hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ما هر روز به اندازۀ تولیدمان آن‌طرف ناوهای آمریکا نفت می‌فروشیم  @Farsna</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/farsna/457609" target="_blank">📅 22:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457608">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/139d0743e4.mp4?token=aRCjhVt_i4RAiXTT755AsekqkTb2DywfYYrcHYLfU89b2gMf1YUCOKSgD2zp6gP59uMzscZC2J8AKnK1U8oJffp8Qdwh98UTkRtcQRa0o8tlZ8PoGvgw20NMm7QTXi7GQmy-K_LHDbVWpQxyaarhwmqvX0pWN935TG8OIpr97nFoAQf2J5jtxubJJEaUz5cj2kQojfY3YUbAf5x0vfD0moSCuO31yiMSo_vtrJP9MqVdEqhofp2ugukEkcTviW5ZLuHy7bfLGLchfjcRjZxHyN9OjPAZWNDhgBsXwc2luDY2Kn_wYgbdBD6LHxtSr0hWc4EVXiV_x1a_4tIdOYl0sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/139d0743e4.mp4?token=aRCjhVt_i4RAiXTT755AsekqkTb2DywfYYrcHYLfU89b2gMf1YUCOKSgD2zp6gP59uMzscZC2J8AKnK1U8oJffp8Qdwh98UTkRtcQRa0o8tlZ8PoGvgw20NMm7QTXi7GQmy-K_LHDbVWpQxyaarhwmqvX0pWN935TG8OIpr97nFoAQf2J5jtxubJJEaUz5cj2kQojfY3YUbAf5x0vfD0moSCuO31yiMSo_vtrJP9MqVdEqhofp2ugukEkcTviW5ZLuHy7bfLGLchfjcRjZxHyN9OjPAZWNDhgBsXwc2luDY2Kn_wYgbdBD6LHxtSr0hWc4EVXiV_x1a_4tIdOYl0sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای عالی امنیت ملی: اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند منافعشان را می‌زنیم.
🔹
اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند یک قطره نفت از خلیج فارس و تنگۀ هرمز بیرون نخواهد رفت و مسیرهای دیگر صادرات…</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/farsna/457608" target="_blank">📅 22:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457607">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e531d1f234.mp4?token=nSplXKuxrvm7cukn45vuxrHSNjQo6YyYDRAPTdj2lqqJfrZiRx78zsKD9Gqft63y9klf9kNhc__FAsoax_4YWySIeICdrBNUeRkOvTtUp0xEi1MyzNpqHbl_DSOIRQBh1moM7_810CL3XmXQAMADCr4ju27GkaOFj2kfj7UhXU9Fpqb_G6q8RXp0thNU8SmK63vAKeDzfPk640EfUD5krs4JFKj4tacEi9IIuZRapj0_jq5JW0Xg8CqY66IJ8zcLoJrkrdQP-17Millr5bUSKEw0ZfkIu_KEzRJIx8wrdVZgncoq-cr-p72EbEeX8tucUwuCEK-KqSFS1xP8oDk1IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e531d1f234.mp4?token=nSplXKuxrvm7cukn45vuxrHSNjQo6YyYDRAPTdj2lqqJfrZiRx78zsKD9Gqft63y9klf9kNhc__FAsoax_4YWySIeICdrBNUeRkOvTtUp0xEi1MyzNpqHbl_DSOIRQBh1moM7_810CL3XmXQAMADCr4ju27GkaOFj2kfj7UhXU9Fpqb_G6q8RXp0thNU8SmK63vAKeDzfPk640EfUD5krs4JFKj4tacEi9IIuZRapj0_jq5JW0Xg8CqY66IJ8zcLoJrkrdQP-17Millr5bUSKEw0ZfkIu_KEzRJIx8wrdVZgncoq-cr-p72EbEeX8tucUwuCEK-KqSFS1xP8oDk1IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای عالی امنیت ملی: اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند منافعشان را می‌زنیم.
🔹
اگر کشورهای اطراف ایران در جنگ اقتصادی با آمریکایی‌ها همراهی کنند یک قطره نفت از خلیج فارس و تنگۀ هرمز بیرون نخواهد رفت و مسیرهای دیگر صادرات…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/farsna/457607" target="_blank">📅 22:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457606">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedb855132.mp4?token=ZRZvjJt-ImFSWVZXWltHj2pvOfUImgwdEIfX49oC_LyLvlwlvE8KXwnGdw3ZCBjlDyVi9HrV0ryhJHymiD3eZHIKxRexUa4DKY-xeFEIJjjkWUEG7c9ziGdT0Z5MFtpWMB-ZUO41hJIHfEYaHEj1vHyxWLzMV4dctFyGydKxa-ik_VzkE8iuk2eQNBW_cE-fp5_W2uN9LFec3QNlHuCi27jjQDszPUBq5Fem9E_nJdDPYoqbkF8sggC7YyRS8slIcvjewhK6Qf0Pph44AsJC7JZ4kMpVe6Gct11wOtBZ3gsn1Zm64PjHHY2tmqbUYdfY7HVyjjMl8uz5qQChI1CsAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedb855132.mp4?token=ZRZvjJt-ImFSWVZXWltHj2pvOfUImgwdEIfX49oC_LyLvlwlvE8KXwnGdw3ZCBjlDyVi9HrV0ryhJHymiD3eZHIKxRexUa4DKY-xeFEIJjjkWUEG7c9ziGdT0Z5MFtpWMB-ZUO41hJIHfEYaHEj1vHyxWLzMV4dctFyGydKxa-ik_VzkE8iuk2eQNBW_cE-fp5_W2uN9LFec3QNlHuCi27jjQDszPUBq5Fem9E_nJdDPYoqbkF8sggC7YyRS8slIcvjewhK6Qf0Pph44AsJC7JZ4kMpVe6Gct11wOtBZ3gsn1Zm64PjHHY2tmqbUYdfY7HVyjjMl8uz5qQChI1CsAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: وحدت بدون تبعیت از رهبر انقلاب اصلا امکان‌پذیر نیست.  @Farsna</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/farsna/457606" target="_blank">📅 22:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457605">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef87d4b16b.mp4?token=WT4iCZVmR1hB9v9jiSBA8c4EphxpLS8MUu3JBkiZSUvpZK88Azw-uQOj1p6C1Hl22hRbS_XCYRSWx8SRZwVRU4Chylpn3OI2EjNbI8v1D-Wb51gfgleSYY0TUszX3Ncl9Q5PZt5UEEXHIEWOZxV2dLYFtiAFVfaoPsH1n34b8Dy1hNMg8_DQ519fnqUiUOwGs2NJnyPZNyBqZbtdxB2fS-JCVXocHD-CnVKkkpiyhFGycm6RLIL3i80IsHZPp8caXOB2fLs1nRtWY6fbd8E9dspD8ykUIORDsbHZF1pvbkHhFUzXuCIKukPzrO5MabpVRXeycOT30VYiopqEx2Le5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef87d4b16b.mp4?token=WT4iCZVmR1hB9v9jiSBA8c4EphxpLS8MUu3JBkiZSUvpZK88Azw-uQOj1p6C1Hl22hRbS_XCYRSWx8SRZwVRU4Chylpn3OI2EjNbI8v1D-Wb51gfgleSYY0TUszX3Ncl9Q5PZt5UEEXHIEWOZxV2dLYFtiAFVfaoPsH1n34b8Dy1hNMg8_DQ519fnqUiUOwGs2NJnyPZNyBqZbtdxB2fS-JCVXocHD-CnVKkkpiyhFGycm6RLIL3i80IsHZPp8caXOB2fLs1nRtWY6fbd8E9dspD8ykUIORDsbHZF1pvbkHhFUzXuCIKukPzrO5MabpVRXeycOT30VYiopqEx2Le5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سرلشکر رضایی: همۀ جهان فهمیده‌اند ترامپ خالی‌بند است  @Farsna</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/farsna/457605" target="_blank">📅 22:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457604">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15f05e55a7.mp4?token=iqpngU5SOBhYW6IdKknHb3e5ccnyI1JPPt2HnJZD0MTI2rmAtRVWqgihe4pcHhHdd_v2tYkGoC8gkdTfCxwvyXYVmhpb7xr4ShKupBdW3sfdNu-difY-ik0F9f_RII36q6zR7ZFL8Zv-bRetwFZ22tL7CDUDVKinMSXLmA0M60fMe6dhe0DhMuXzMTmIaT0ZcoCZeW_yWUE6PLGkLY3jJ0eevkTjtdsW30Y08-SyFt-38GtJqsBorkY9DcvnLAEGebU0biNPzS5jdP1J6DOeMvhKBbmX42jiGGoWpt7c8uIE9Ol7OmF9J1TRQhtCqznbhrWLpg8vKd4mASAXrgx3Ag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15f05e55a7.mp4?token=iqpngU5SOBhYW6IdKknHb3e5ccnyI1JPPt2HnJZD0MTI2rmAtRVWqgihe4pcHhHdd_v2tYkGoC8gkdTfCxwvyXYVmhpb7xr4ShKupBdW3sfdNu-difY-ik0F9f_RII36q6zR7ZFL8Zv-bRetwFZ22tL7CDUDVKinMSXLmA0M60fMe6dhe0DhMuXzMTmIaT0ZcoCZeW_yWUE6PLGkLY3jJ0eevkTjtdsW30Y08-SyFt-38GtJqsBorkY9DcvnLAEGebU0biNPzS5jdP1J6DOeMvhKBbmX42jiGGoWpt7c8uIE9Ol7OmF9J1TRQhtCqznbhrWLpg8vKd4mASAXrgx3Ag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: ترامپ می‌خواهد بازی جدیدی به‌نام جنگ اقتصادی راه بیندازد که حسابش را خواهیم رسید.  @Farsna</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/farsna/457604" target="_blank">📅 22:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457603">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=AJ0vTpRRsYSy9M4UX_rF8uGBiPvWrFbc58Z-WY6WS_w77cOVhGXnYP0eN0JWpJqhhVB8seUAQiv-mQ7iyUlwqj1WhLPrBxH5kDtJt9zuIGI5TwFXwLj4VI4sN-bF7Bn5doHE0oAxge5e-ArM5HFI1zIG02oifLDfeoOQBFvLVFzKmT1P2sHsKwZT1B__5qaO5PlCJkpiEcfhxIt2x7Nu_qZJRPrLpB3rkuEApSzJnOIh_fDxce3l7jowCEiWDjpe1fhiHRHsJI4tMnEDX7dFCA2ZjzqDTpvZgcRuN8CwarYYGRSARbOzZup49GzHbpmpA-KeTjQiY68MRLDQONnhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b35614b49f.mp4?token=AJ0vTpRRsYSy9M4UX_rF8uGBiPvWrFbc58Z-WY6WS_w77cOVhGXnYP0eN0JWpJqhhVB8seUAQiv-mQ7iyUlwqj1WhLPrBxH5kDtJt9zuIGI5TwFXwLj4VI4sN-bF7Bn5doHE0oAxge5e-ArM5HFI1zIG02oifLDfeoOQBFvLVFzKmT1P2sHsKwZT1B__5qaO5PlCJkpiEcfhxIt2x7Nu_qZJRPrLpB3rkuEApSzJnOIh_fDxce3l7jowCEiWDjpe1fhiHRHsJI4tMnEDX7dFCA2ZjzqDTpvZgcRuN8CwarYYGRSARbOzZup49GzHbpmpA-KeTjQiY68MRLDQONnhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دبیر شورای‌عالی امنیت ملی: حماقت ترامپ دنیا را به سمت دستیابی به بمب اتم سوق داده
🔹
حماقت ترامپ با حمله به ایران اشتیاق مردم جهان به بمب اتم را بیشتر کرد زیرا همۀ دنیا دیدند عضویت در سازمان انرژی اتمی و NPT برای جلوگیری از حمله آمریکا اثری ندارد.
🔹
ترامپ به…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/farsna/457603" target="_blank">📅 22:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457602">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ef3531947.mp4?token=p7kt8nearoYLZ2NqP2OzW24bRhHik1n3q_LcS7aKbr36qDW5oqgfgPjUsMo_WV7XDlbT3c-3rLvx21rjYrD96gQBgkofw4Lzn9BuAQEnzwfTwvrTtVoK30bldTNZevMtDZGUeQO0Fyd8E4ESlOTu7CyMu8W88R9bMW5N1dtmbM18WMuPgpmWbW9mr75n0SgIvbKoxy5Jdsm1fM9p9cuty8Bq8nB6AzOrp0IUkjI9UOBiaaG4xFkIuqEcBZUridrQ10pxTd033JAitozic6nG2hm05If6QOSbQKmNw_FABJ7ktOEYl9H5rL8uSS6aFSPbTjGEZLBqxgIhy3pHQ8ASdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ef3531947.mp4?token=p7kt8nearoYLZ2NqP2OzW24bRhHik1n3q_LcS7aKbr36qDW5oqgfgPjUsMo_WV7XDlbT3c-3rLvx21rjYrD96gQBgkofw4Lzn9BuAQEnzwfTwvrTtVoK30bldTNZevMtDZGUeQO0Fyd8E4ESlOTu7CyMu8W88R9bMW5N1dtmbM18WMuPgpmWbW9mr75n0SgIvbKoxy5Jdsm1fM9p9cuty8Bq8nB6AzOrp0IUkjI9UOBiaaG4xFkIuqEcBZUridrQ10pxTd033JAitozic6nG2hm05If6QOSbQKmNw_FABJ7ktOEYl9H5rL8uSS6aFSPbTjGEZLBqxgIhy3pHQ8ASdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: حتما در مسئلۀ ادارۀ شیوۀ جنگ تغییراتی خواهیم داد و در رفتار دیپلماتیک ایران تحولاتی صورت خواهد گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/farsna/457602" target="_blank">📅 22:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457601">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb594bb4f.mp4?token=d12XNl-BNK6altPaYxpXwM4PO8dWq0LhXUQarXLU-YMz80wNrEqJr-mmEOQkZcySwbyh39aW6oTek61Mgk2J3opsFQTupA82qhJ7A_0VsPFRrqFdXU_YXFgRUsQToRV1DCfu5w6LdHWZrWoJxDoBYOfo0ScQaMgica4xvG4H2_twdFITk9TdMGh3b6tnlmvmjlsdsTl5KS6gWiidYx_oexR_rfZUQeLKWZ0CURNEkjlYC95oTB5r5udwki819EPI87QYTr-LDig3-s4ic5ZY30EvKM-hc5Wkl9aKUSh2khVA0GmurpKk01H8Wcjz4VXfPmU4FJY5fdpQVGc_61QUMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb594bb4f.mp4?token=d12XNl-BNK6altPaYxpXwM4PO8dWq0LhXUQarXLU-YMz80wNrEqJr-mmEOQkZcySwbyh39aW6oTek61Mgk2J3opsFQTupA82qhJ7A_0VsPFRrqFdXU_YXFgRUsQToRV1DCfu5w6LdHWZrWoJxDoBYOfo0ScQaMgica4xvG4H2_twdFITk9TdMGh3b6tnlmvmjlsdsTl5KS6gWiidYx_oexR_rfZUQeLKWZ0CURNEkjlYC95oTB5r5udwki819EPI87QYTr-LDig3-s4ic5ZY30EvKM-hc5Wkl9aKUSh2khVA0GmurpKk01H8Wcjz4VXfPmU4FJY5fdpQVGc_61QUMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: حتما در مسئلۀ ادارۀ شیوۀ جنگ تغییراتی خواهیم داد و در رفتار دیپلماتیک ایران تحولاتی صورت خواهد گرفت.  @Farsna</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/farsna/457601" target="_blank">📅 22:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457600">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa8cb4422.mp4?token=efBQu1zuK1FXLVsPpldtZ0nf6QNa3Qchap6qIAbWE0jBOCNgNUtFyneHZCqSOX95Xe5IUiDASjI30HYw_K2q1H1NfVESEbqAxzuYxNcHq6568I35qAN0OQpqor2AE0L7r4OnOPBiU4lMQDTHpt7fcot2vpTpO7S4rgkSj1d-z0VqWRCC_eEzpj8kCZLtuGAXVduXep-3Xd8C15gSddSXmDC3DfKpFR9zvFNbquSoYSJNnZMUz0Cx1C2fdtrrImOAIcTG7QfzSrThH28rS8QEifOrkFdD8ve5KwNK28QQcdm5ZcwPfLnjDgEMBq9gv72ap4vGtvI6ZVD_3x3WtrKt3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa8cb4422.mp4?token=efBQu1zuK1FXLVsPpldtZ0nf6QNa3Qchap6qIAbWE0jBOCNgNUtFyneHZCqSOX95Xe5IUiDASjI30HYw_K2q1H1NfVESEbqAxzuYxNcHq6568I35qAN0OQpqor2AE0L7r4OnOPBiU4lMQDTHpt7fcot2vpTpO7S4rgkSj1d-z0VqWRCC_eEzpj8kCZLtuGAXVduXep-3Xd8C15gSddSXmDC3DfKpFR9zvFNbquSoYSJNnZMUz0Cx1C2fdtrrImOAIcTG7QfzSrThH28rS8QEifOrkFdD8ve5KwNK28QQcdm5ZcwPfLnjDgEMBq9gv72ap4vGtvI6ZVD_3x3WtrKt3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: تصمیم رهبر انقلاب برای آمدن فرماندهان باتجربه معنایش این است که تجارب یک‌سال گذشته حتما در نبرد آینده استفاده می‌شود و جنگ آینده متفاوت‌تر از جنگ ۴۰ روزه خواهد بود.   @Farsna</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/farsna/457600" target="_blank">📅 22:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457599">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/639d6787c0.mp4?token=s6AM756HEBq4SqJaxef8pgVAqaPQoS093BsPYLRiv9VRkx-9e-BVKHCuiSZrNRHcp81KluGhhh846bBU9AMXAyaB3fQYqZwPydkpx0bRE3o_7XKI_m0Vf-0WFnFgOsA_JgZlynw101SN_X0_RVuXORhU80uYqnFH__4PHNmpfRPEo2GPcEazBgvMp1TXzmnd-h8SUFz3JoF2fU5qQx8QG9r0euon-SgHFUf5KupBRshuiMxVncdF6EC3JQSFFeiku3QklZvhuAE7OOpUICfOrlZI-39DcxPPW-c28kZ1lEuogfVAy2oLqvZrI8x88b_KnANjcAJ61rFMjCA3V4vDog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/639d6787c0.mp4?token=s6AM756HEBq4SqJaxef8pgVAqaPQoS093BsPYLRiv9VRkx-9e-BVKHCuiSZrNRHcp81KluGhhh846bBU9AMXAyaB3fQYqZwPydkpx0bRE3o_7XKI_m0Vf-0WFnFgOsA_JgZlynw101SN_X0_RVuXORhU80uYqnFH__4PHNmpfRPEo2GPcEazBgvMp1TXzmnd-h8SUFz3JoF2fU5qQx8QG9r0euon-SgHFUf5KupBRshuiMxVncdF6EC3JQSFFeiku3QklZvhuAE7OOpUICfOrlZI-39DcxPPW-c28kZ1lEuogfVAy2oLqvZrI8x88b_KnANjcAJ61rFMjCA3V4vDog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای‌عالی امنیت ملی: امروز ملت ۵ هزار سالۀ ایران با دولت ۲۵۰ سالۀ آمریکا در تقابل است.  @Farsna</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/457599" target="_blank">📅 22:18 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457598">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7086b89ab.mp4?token=iF1Rx1MMCMHJWUCBjMeMHG2C32OmnvwZtYR5BW0q71bCY78KFiVtQQApePj53WfQWRFp6xj4Ng1qM8_c9XT4kFBZmG1Bau0Zvp8gAQns6q6MURf9XLbv7yXLR0Uy4WVbuprNINq2JptzXhyehOdeJQ-3OIkpuuoXx815YCEW20qqpKUQ_aCLXLfIQ5WLgG8DbULGi3DmAK2BsHdeB8EYtotRyVSdtTK_guu3Sbgc_aJ2zSigimNdOb9l5Dk-aKIOp29Sew89dodDsFmw_dnmZ1rRNOlyQQzAfZWag9bWs5BH1Pl2G84lAncCieaStplM30hTTipAWPqpmtnRnx6dKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7086b89ab.mp4?token=iF1Rx1MMCMHJWUCBjMeMHG2C32OmnvwZtYR5BW0q71bCY78KFiVtQQApePj53WfQWRFp6xj4Ng1qM8_c9XT4kFBZmG1Bau0Zvp8gAQns6q6MURf9XLbv7yXLR0Uy4WVbuprNINq2JptzXhyehOdeJQ-3OIkpuuoXx815YCEW20qqpKUQ_aCLXLfIQ5WLgG8DbULGi3DmAK2BsHdeB8EYtotRyVSdtTK_guu3Sbgc_aJ2zSigimNdOb9l5Dk-aKIOp29Sew89dodDsFmw_dnmZ1rRNOlyQQzAfZWag9bWs5BH1Pl2G84lAncCieaStplM30hTTipAWPqpmtnRnx6dKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای عالی امنیت ملی: باید در رفتار دیپلماتیک ایران اصلاحاتی انجام شود
🔹
در راهبردهای دفاعی ایران تکامل رخ داده و از جنگ تحمیلی دوم دائما درحال تکامل دفاعی-سیاسی است.
🔹
ایران امروز ایران قبل از جنگ نیست؛ این قضیه درباره آمریکای پرمدعا هم صدق می‌کند…</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/farsna/457598" target="_blank">📅 22:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457597">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67d57a058d.mp4?token=mxZnBJGcL0BQlpjuHvIEdtBh53cKPM6KWlJiYeRbCYJ2Sx9VNjb_nZ1yoj1F7kPuGgBxI5k_7NhTtTxxB7Y0SbSiPbU0z8zc0pSVuqw_eGeLGmcI6iprWIoEvt1-uwPy6Kjd2lrJGC7LK8uaxohvdch1e4vmHvJKZFd7y7QgLZVRcV-bz9YsQWLgcxiSoffC_pxPZlh6jxuVIJXdTwIcCMORHFRpAgrHHHGi8SOZaBk2KHKTD6L4K3pXwaTpgjTR_HHirZ1Fjpt72fclI5mYXOzaJL0s-jngW3-2v0jK6G8eqDzsdCX56Utu7JOw0_bL4OK5x7iEkuLTMWuvR_WK1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67d57a058d.mp4?token=mxZnBJGcL0BQlpjuHvIEdtBh53cKPM6KWlJiYeRbCYJ2Sx9VNjb_nZ1yoj1F7kPuGgBxI5k_7NhTtTxxB7Y0SbSiPbU0z8zc0pSVuqw_eGeLGmcI6iprWIoEvt1-uwPy6Kjd2lrJGC7LK8uaxohvdch1e4vmHvJKZFd7y7QgLZVRcV-bz9YsQWLgcxiSoffC_pxPZlh6jxuVIJXdTwIcCMORHFRpAgrHHHGi8SOZaBk2KHKTD6L4K3pXwaTpgjTR_HHirZ1Fjpt72fclI5mYXOzaJL0s-jngW3-2v0jK6G8eqDzsdCX56Utu7JOw0_bL4OK5x7iEkuLTMWuvR_WK1TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شب ۱۷۵ از شب های مقاومت مردم تربت حیدریه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/farsna/457597" target="_blank">📅 22:14 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457596">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/731f4e0fa5.mp4?token=oMhyYO5ARo9HPKK03ZMZBIMCbk--MWL1xKW3dolFRnsDcZV-oFyzEzV2c3mGWmbcitMX5vDmgEKbZ27876xe4MdRcGBP5MfY-Nc0pF0twf-f9BmPTb3UCHAuM6jOFTQ9VdqiA8932X-Q-AKc2TXMvu0YitUUF28jkpknBllMs8HYc7JVI2yc0NwKQKWgpyroGlWPu1n0brklFEiHTsowx2b_HkYc1qwZ2v4WyaR91ewkYqZcHxdQzUpIkV0ulHXWl5xM2FBfoDx1yvmQWu98u-2ULDSZvK_vaXkxdjrSkbnYjBXwzRzJNNAtcB2VOUFpX_GKfsgDVQEeSzzMiyNR5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/731f4e0fa5.mp4?token=oMhyYO5ARo9HPKK03ZMZBIMCbk--MWL1xKW3dolFRnsDcZV-oFyzEzV2c3mGWmbcitMX5vDmgEKbZ27876xe4MdRcGBP5MfY-Nc0pF0twf-f9BmPTb3UCHAuM6jOFTQ9VdqiA8932X-Q-AKc2TXMvu0YitUUF28jkpknBllMs8HYc7JVI2yc0NwKQKWgpyroGlWPu1n0brklFEiHTsowx2b_HkYc1qwZ2v4WyaR91ewkYqZcHxdQzUpIkV0ulHXWl5xM2FBfoDx1yvmQWu98u-2ULDSZvK_vaXkxdjrSkbnYjBXwzRzJNNAtcB2VOUFpX_GKfsgDVQEeSzzMiyNR5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دبیر شورای عالی امنیت ملی: باید در رفتار دیپلماتیک ایران اصلاحاتی انجام شود
🔹
در راهبردهای دفاعی ایران تکامل رخ داده و از جنگ تحمیلی دوم دائما درحال تکامل دفاعی-سیاسی است.
🔹
ایران امروز ایران قبل از جنگ نیست؛ این قضیه درباره آمریکای پرمدعا هم صدق می‌کند و تصویر آمریکای صلح‌خواه و بزک کرده، در ذهن جوانان ایرانی عوض شده است.
🔹
همۀ دنیا با یک دید جدید به ایران نگاه می‌کنند.
@Farsna</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farsna/457596" target="_blank">📅 22:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457595">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پیام‌هایی که شما برای فارس فرستادید
🔸
چرا قطع برق شهرهای خوزستان باوجود وعدۀ وزیر نیرو و استاندار همچنان ادامه دارد؟ در ساعات گرم روزهای تابستان خانه‌ها برای چند ساعت و گاهی حتی بدون برنامه‌ریزی برق ندارند.
🔹
بیمۀ مشاغل آزاد به‌شدت افزایش یافته است. ۳ مرداد رفتم بیمه، گفتند ۲ میلیون تومان باید اضافه پرداخت کنید؛ یعنی ۶ میلیون و ۲۰۰ هزار تومان پول بیمه و مابه‌التفاوت ماه‌های قبل را گرفتند.
🔸
پنج‌شش ماه است که از موعد تحویل ماشین‌مان گذشته، اما چون ماشین گران‌شده تحویل نمی‌دهند. این چه وضعی است؟ این انصاف است که می‌گویند یا بیا پول شش ماه پیش ماشین را پس بگیر یا مابه‌التفاوتش را بده؟ مگر مشکل از ما بود؟ همان موقع که پول کامل ماشین را خواستند، پرداخت کردیم اما موقع تحویل این بازی‌ها را درمی‌آورند.
🔹
سنوات دو ماه ابتدایی افزایش حقوق بازنشستگان تأمین اجتماعی چه تاریخی واریز می‌شود؟ پنج ماه از سال گذشته و حتی تاریخی هم اعلام نمی‌شود.
🔸
معاون اجرایی هنرستان هستم. امسال سامانه سیدا هنرستان افتضاح شده و هر کاری بخواهیم انجام دهیم دستمان بسته است. از ابتدای سال مهلت داشتند تغییرات بعضی دروس را در سامانه اعمال کنند، اما حالا که پایان سال است، نه تنها مشکل حل نشده بلکه هزاران مشکل دیگر هم اضافه شده. الان نه می‌توانیم کارنامه صادر کنیم، نه انتخاب واحد تابستان و کارآموزی امکان‌پذیر است و نه تعریف سال جدید.
🔹
محبت می‌کنید در مورد وام مسکن روستایی پیگیری کنید. باتوجه به اینکه نامۀ معرفی به بانک داده شده، بانک هیچ پاسخگویی ندارد و پرونده همین‌طور مانده است.
🔸
مشکل سوخت جنوب را پیگیری کنید، مخصوصاً میناب. کارت سوخت کفایت نمی‌کند. با این هوای گرم، برای بنزین آزاد هم باید در صف کیلومتری بایستی تا بعد از ۲ تا ۳ ساعت فقط ۲۰ لیتر بزنی. واقعاً مردم نباید دغدغه‌شان این موضوع باشد.
🔹
متأسفانه ادارۀ برق فردیس به روشنایی معابر ۱۶ متری امام خمینی، خیابان تابان، سعدی غربی و خیابان‌های فرعی آن رسیدگی نمی‌کند. اکثر لامپ‌ها سوخته و قدیمی هستند و فقط برق مصرف می‌کنند، در حالی که سایر خیابان‌های شهر با لامپ‌های جدید تعویض شده‌اند. لطفاً از مدیر برق منطقه بخواهید شب‌ها از این مناطق کم‌برخوردار بازدید کند. آسفالت این خیابان هم کاملاً خراب و پر از چاله است و ۳۰ سال است وعدۀ بازسازی می‌دهند ولی هیچ اقدامی نشده.
🔸
ما فروردین‌ماه به بیمۀ بیکاری معرفی شدیم. پیامکی هم آمد که مبلغ ۱۶ میلیون و خرده‌ای به حساب شما واریز خواهد شد، اما با وجود گذشت چند ماه هنوز این مبلغ واریز نشده است. لطفاً پیگیری کنید.
🔹
من رانندۀ تریلی هستم و اتاق سمند سورن را به شیراز می‌برم. ایران‌خودرو از مرداد پارسال طلب‌هایمان را نمی‌دهد. قبلاً پیش‌کرایه می‌دادند و مابقی را ماهانه تسویه می‌کردند اما حالا حتی پیش‌کرایه را هم قطع کرده‌اند. با خرج سنگین گازوئیل، قطعات و خانواده نمی‌دانیم چه کار کنیم. فقط تهدید و وعده می‌دهند.
🔸
یک دارو یک‌بار با بیمه و یک‌بار آزاد خریداری شده. در خرید با بیمه گران‌تر درآمده: با بیمه ۸۵۰ هزار تومان و آزاد ۶۵۰ هزار تومان. تعرفه خدمات دارویی در خرید بیمه‌ای ۷۲٬۷۰۰ تومان و در خرید آزاد ۸٬۱۰۰ تومان است. ببینید چقدر اختلاف وجود دارد.
🙍‍♂️
شناسۀ ارتباطی ما:
@Fars_ma
@Farsna</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farsna/457595" target="_blank">📅 21:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457594">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f36b0dd885.mp4?token=Q9CKfaHptUW2r-n9H6p5ToHJ9gr7G6cuRIjWB8wIumu6_QWXuHSRoFlsagejqfq0x0HyMRd7GT68Dq9uX1eLxCD9bKGoMsfecmlbwJZxPCg-FOYE7i4G_R-A4FnyY9eJd6rLGuqqsIej4sBb5WYkoXTCf_BqT9Eb1ZhP_3lzetAAGjtn-6-7Ud7hjO6AUUPl9dbDrZNi8jRP34pI1IFu8X8zn5QDNdfut3pHpppxgdOkOjbJ0Ha5wtoRw5aFVNAOr76ADVmaM_GUu9sBIIJnjVwMRfmE1Gtz-QhWEvZZOGmEQCD7MdXlN6gkXpHc-Vsm_BTV0UQHZXMfq1rDNgO01w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f36b0dd885.mp4?token=Q9CKfaHptUW2r-n9H6p5ToHJ9gr7G6cuRIjWB8wIumu6_QWXuHSRoFlsagejqfq0x0HyMRd7GT68Dq9uX1eLxCD9bKGoMsfecmlbwJZxPCg-FOYE7i4G_R-A4FnyY9eJd6rLGuqqsIej4sBb5WYkoXTCf_BqT9Eb1ZhP_3lzetAAGjtn-6-7Ud7hjO6AUUPl9dbDrZNi8jRP34pI1IFu8X8zn5QDNdfut3pHpppxgdOkOjbJ0Ha5wtoRw5aFVNAOr76ADVmaM_GUu9sBIIJnjVwMRfmE1Gtz-QhWEvZZOGmEQCD7MdXlN6gkXpHc-Vsm_BTV0UQHZXMfq1rDNgO01w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تودهنی رضا پهلوی به اینترنشنال و خودش  @Farsna - Link</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/farsna/457594" target="_blank">📅 21:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457593">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">📷
ادامۀ جنایات صهونیست‌ها در جنوب لبنان
🔹
تخریب منازل لبنانی‌ها توسط ارتش اسرائیل در شهرک یحمر الشقیف‌. @Farsna</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/457593" target="_blank">📅 21:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457592">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92621de672.mp4?token=MdJUujuTim5nMNpoRL6VmAXp_kN1lfDTRCqX40kNhWDm9RjBVOghXIdvL-T2bFU4-Dz7LlIw6X3anER73MxmM9YpYk_BV_f9Q5L_JEUqJhdWRRToKJuFAR54QQMgjf229fQty2EZLZv3c4PP9fN5pGe3Ev_45e2C5z4_I-rC3HyKMwxIRPor8tmOA5CePK7jCRpPceJ1eRPHsEoXeGjepNzyoplVeFIy3aRKmyCjy6BwZC3XldQrU9y_vMtfmsxVFOvUnWmDcAclJRNCTokX1XpQVOQFd7RU5qBuPbxXHJkAXy3xJkaUgfMY6IHoAhXdyEwpQQq5iT3AJFK7hXwB1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92621de672.mp4?token=MdJUujuTim5nMNpoRL6VmAXp_kN1lfDTRCqX40kNhWDm9RjBVOghXIdvL-T2bFU4-Dz7LlIw6X3anER73MxmM9YpYk_BV_f9Q5L_JEUqJhdWRRToKJuFAR54QQMgjf229fQty2EZLZv3c4PP9fN5pGe3Ev_45e2C5z4_I-rC3HyKMwxIRPor8tmOA5CePK7jCRpPceJ1eRPHsEoXeGjepNzyoplVeFIy3aRKmyCjy6BwZC3XldQrU9y_vMtfmsxVFOvUnWmDcAclJRNCTokX1XpQVOQFd7RU5qBuPbxXHJkAXy3xJkaUgfMY6IHoAhXdyEwpQQq5iT3AJFK7hXwB1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حرف ایل و تبار ما: مرگ بر آمریکا، مرگ بر اسرائیل
🔸
شعار مردم شهرکرد در شب ۱۷۵ تجمعات
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/farsna/457592" target="_blank">📅 21:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457591">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFtU6dBWKM2Nev8xlGTpy49k7tMC_5yICnRlkMzSctfwJxlZdELq6Ksh3YpGwbISGqz-RZQ5Wl0j9OfGtvehseTMuxixWm9CvcUR-DGXRiVKOu6gg9lDhjps9GL6TrtIPT8U2UZYOYJkuIFJlmaJVoqkbY3SNPftzqoJTEUGa6JQ0mlhmlXWIyn5W1UcDB-1XErGjB1lx5fC-ttcgipA5E08jJYkzJ34_f1wUe9OLHUPmnTZggrxWOHhYjps2pLkJXC6QnaaNwpdG8NgaBONl8dQ6BCR0E-vS-XmN4SIjmvm6ZQ5ZQ9W6QLUvf2IfU1Mu25QxinyeFDaDmimkl97-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آزادکار ۹۲ کیلوگرم کشورمان در رقابت‌های جوانان جهان نقره گرفت
🔹
فینال ۴ وزن دوم کشتی آزاد جوانان جهان امشب برگزار شد که  ابوالفضل رحمانی تنها نمایندۀ ایران در وزن ۹۲ کیلوگرم، در ۲ ثانیه پایانی طلا را از دست داد و اولین نقره کشورمان را کسب کرد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.66K · <a href="https://t.me/farsna/457591" target="_blank">📅 21:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457590">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B6-5OsVora4ZJ23QB4sFkPBl2pIAfuTvPh76RJqOUsq7vcYQdOecuq2-tHVEqqzL5A_m5aB7JOW4d5SJRlLyLv5J5tWv6NPiElq-ANa-gZFIU4yDBgw5vSVtD-87n6d0RQKpX3T6AIY1rNcRQGjeNdquA-1wrhGPq9x8RR4hxk8MQOb7GB59BVhsNTWXK5elsXmUF2iD4hmUtDhijr1va_yfDLYMDgjWj_uzA0iy-qIGvmO104-K8fDWWOKN81n5xPKFycetUtOUXD07dX_19XWgnnTuPFDBPfiLxjjv2Y7Sb09Ok5nHDGq3Xq4zItbi75bkrxIDlPJnNXksfqco2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ابهام در پرونده کشف جمجمه ۴۱ آهو در چاهی در شاهین‌شهر
🔹
فرمانده یگان حفاظت محیط‌زیست استان اصفهان: شواهد اولیۀ ماجرای کشف ۴۱ جمجمۀ آهو حاکی از شکار غیرمجاز است؛ با این حال، تعیین دقیق تعداد تلفات و بازۀ زمانی دقیق این شکارها، نیازمند بررسی‌های کارشناسی توسط متخصصین حیات‌وحش است.
🔹
در این راستا یکی از متهمان دستگیر شده و متهم دوم تحت تعقیب است. گزارش‌های دریافتی و کشفیات موجود نشان‌دهندۀ یک جریان غیرقانونی مستمر در شکار حیات‌وحش است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.51K · <a href="https://t.me/farsna/457590" target="_blank">📅 21:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457589">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🎥
ایران چگونه توپ را در زمین آمریکا انداخت؟
@Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/457589" target="_blank">📅 21:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457588">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb7OG6qw5ahBEf3MyMpqyW1_O81Dl-butlFVlI8ZH6LhT46Lfguebyci3WPeMoh25YlvnToVvo1Gn5pQXMbuL-slw3Hu5M0-62CeOCRRn0k91wDp_yozBzNDH8Txvrqbsgb1Y3jPYX-LFcIDRc4f2nMH3iQmzamMwG724GFFYKyAXiInz6IYxJ-6Dpg8510I6zFPNJCDQneHyzdKZG_GQPRm8vWnIdzoXECLtWZx8j2T0fATGQmWvWEyWMk-TUtsfN2JwmQuqSEbqq9ma2SBjxYY3uCOlKrrkmChdfBIgt5RPGfs8tVLBJyKYSzr7uJ1Qc6G96zO-hTamoo3qGKseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو: تا زمانی که من نخست‌وزیر هستم اجازه نمی‌دهم هیچ کشور فلسطینی تحت کنترل ایران تشکیل شود.
@Farsna</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/farsna/457588" target="_blank">📅 21:10 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457587">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90e88e73ef.mp4?token=VyDV9vdD0VVyNo_yt8iy-Y6o98GkgdemCfQDnXQOwF9utiRKOgrjwqRJihpJjYJWUlm0_XUFLhjP9Gi8G6kbTAMTQT7I-gOAj_lcp_aW2N2oqtdrUucxI4CjhTkaiOPe6xUCf8Crv-iyE9J59J3OOF61bQkSkIvc5KJE06jiWWjC7-1wY8TTaTqbPTXAb0VqVho_RM1ciLRdNb6P0YhHmsIzHQ6Yy1cp64VOu5ylF_tuq2GCC4eX2Lxm_ucIBonpf1FYAjHICl1_doYlB3aXB83tcSrkcozOE2e7tNZds5_3Q3n8uPtgIv1Ty9Y3gmPc36lpnhzAeXNIuF6gzHh5eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90e88e73ef.mp4?token=VyDV9vdD0VVyNo_yt8iy-Y6o98GkgdemCfQDnXQOwF9utiRKOgrjwqRJihpJjYJWUlm0_XUFLhjP9Gi8G6kbTAMTQT7I-gOAj_lcp_aW2N2oqtdrUucxI4CjhTkaiOPe6xUCf8Crv-iyE9J59J3OOF61bQkSkIvc5KJE06jiWWjC7-1wY8TTaTqbPTXAb0VqVho_RM1ciLRdNb6P0YhHmsIzHQ6Yy1cp64VOu5ylF_tuq2GCC4eX2Lxm_ucIBonpf1FYAjHICl1_doYlB3aXB83tcSrkcozOE2e7tNZds5_3Q3n8uPtgIv1Ty9Y3gmPc36lpnhzAeXNIuF6gzHh5eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
معاون وزیر آموزش‌وپرورش: ۴ میلیون دانش‌آموز هوش‌مصنوعی را آموزش دیده‌اند
🔹
آموزش استفاده از هوش‌مصنوعی برای معلمان هم آغاز شده که تاکنون بیش از ۲۵۳ هزار معلم در آن شرکت کرده‌اند.
@Farsna</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/farsna/457587" target="_blank">📅 21:01 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457586">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCFxGon557GG9pC_jKOQMk2mWoRGV7ShS0bVVm6LiaF3cgJDPSi_ByPveq-OCom2CfJ4zTn_qhj0eS47PjaKUJsbS9jLzP81kkYGjtRqFWkarWP5nprdfzv5GXfS7d-VI6GkFUjlbF_-qv3SCupt5x6Qb0mq55nC-S01wugmOQAi4vOFe8su6qY86MgT7WW9FeaGUP7EjazsZk2u2v-qjSIV7qW-Siq3H2_gxoboWCbrPjNO1b6rgLvWH2bxOgBC3sLek4n8qzw_NEryE6f_CkjkdeRXo-Sx0pBJdY17u41oti7hbvY1vnoKbZe4a9elCx8ENjgqtWVA-gT6gwZ7AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهریور امسال، کسب‌وکارتان را به خنکای ایران بسپارید!
❄️
🍃
از قله‌های همدان تا جنگل‌های گلستان و دشت‌های کردستان؛ ۱۰ استان دیدنی ایران منتظر میزبانی از گردشگران هستند. اگر می‌خواهید اقامتگاه یا خدمات شما مقصد بعدی مسافران باشد، جای شما در پویش «سفر به خنکای ایران» خالی است!
✅
اهداف پویش:
• معرفی زیبایی‌های ایران
• حمایت از کسب‌وکارهای بومی
• افزایش فروش و رونق اقتصادی
✅
مزایای شرکت در این پویش:
• معرفی گسترده در رسانه معتبر خبرگزاری فارس
• برندسازی و افزایش اعتبار مجموعه شما
• جذب مشتریان هدفمند از سراسر کشور
• ارائه گزارش‌های آماری از بازخورد تبلیغات
📍
ویژه کسب‌وکارهای گردشگری ۱۰ استان:
همدان، آذربایجان شرقی و غربی، اردبیل، چهارمحال و بختیاری، گلستان، زنجان، خراسان شمالی، لرستان و کردستان.
💯
فرصت را از دست ندهید و نام خود را در لیست بهترین‌های گردشگری ایران ثبت کنید.
🔗
ارتباط با ما جهت ثبت‌نام:
🆔
@FarsCampaigns
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/farsna/457586" target="_blank">📅 20:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457585">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_3oxOzHnX3S7nZDuLZZ88odvRp-AzEUzvxzO8EY8Zc_DraIuAFIcrjSFD7fbZ4rV5Rr6Fe0YoFgU47NEMrOx_-hO-qVtyvVIIQffb7rQKRNu03nH2XdrmOk90LnJJE-vz25h_p8rX7KeF_0jwJ-4nlMgyL7hZUCqJZmv8VP0m-ABRDO0OMm75vhhgo7eaQY0Mg8z5eghHT91THL2h4Ays4ulQZ16Ei-70AqcLhl9_QZSD7q9hVc4fBJ8dE4g-znaEpBvA42Ovd5lWwLAn0JzwgJrJ1CsfdB8iNJv9xPSJoDB0iLhK9vINxJVNEtM3JDC8EIiBEaSGdwjbwRNH3HhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
ثبت‌نام دوره تخصصی «هوش مصنوعی در روابط عمومی و رسانه» آغاز شد.
🔹
این دوره یک برنامه آموزشی جامع، کاربردی و پروژه‌محور است که به شما می‌آموزد چگونه هوش مصنوعی را وارد فرآیندهای واقعی روابط عمومی، رسانه و ارتباطات سازمانی کنید.
🔹
در این دوره ۲۴ ساعته، از تولید محتوای حرفه‌ای و مهندسی پرامپت تا تحلیل افکار عمومی، رصد رسانه‌ها و مدیریت هوشمند بحران را به‌صورت گام‌به‌گام فرا می‌گیرید.
🎉
ویژه مدیران و کارشناسان روابط عمومی، رسانه و ارتباطات
📝
ثبت‌نام دوره حضوری
📝
ثبت‌نام دوره آنلاین
مرکز آموزش‌های آزاد خبرگزاری فارس</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/farsna/457585" target="_blank">📅 20:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457584">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/farsna/457584" target="_blank">📅 20:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457583">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">آغاز عرضۀ خودروهای خارجی از فردا
🔹
سامانۀ تخصیص خودروهای وارداتی از فردا به مدت ۴ روز برای انتخاب چهار خودروی تویوتا و چانگان فعال می‌شود.
🔹
متقاضیان باید یکی از حساب‌های خود را در بانک‌های واجد شرایط وکالتی و ۵۰۰ میلیون تومان مسدود کنند.
@Farsna</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/farsna/457583" target="_blank">📅 20:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457582">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdd0803ea0.mp4?token=Rs099xYabSLvhkQ9u7jsPkP2Y8jXHSiGzkr1hFWdSSZEupMKhWnZUREhoqn47AM0vlXAxXgwnRfe3Xmofb-jtPMhDThCfDCwtUVfHyV9XAHF2H9E5bmAXDsDJp9sy3mrml6Ec3D_Rl8saKqdwrpl_onr51IRzVMwu_IivTmHcYNBKMj_8xP2jAsrNIcahOCR_8Q6BVxfjuYcXI7OXitn9rJCrhkXUSgjCUmKNinvAVE99ywT0pzm9ks3vzShEX-ZfHa3QoIemW0LfvDxnzFZkl1BYaQGt08SQUXDwskUue_8aRfkbQ6S4y5W9pnvR6VDp-3LkfTb-5ilcHsVN5kUlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdd0803ea0.mp4?token=Rs099xYabSLvhkQ9u7jsPkP2Y8jXHSiGzkr1hFWdSSZEupMKhWnZUREhoqn47AM0vlXAxXgwnRfe3Xmofb-jtPMhDThCfDCwtUVfHyV9XAHF2H9E5bmAXDsDJp9sy3mrml6Ec3D_Rl8saKqdwrpl_onr51IRzVMwu_IivTmHcYNBKMj_8xP2jAsrNIcahOCR_8Q6BVxfjuYcXI7OXitn9rJCrhkXUSgjCUmKNinvAVE99ywT0pzm9ks3vzShEX-ZfHa3QoIemW0LfvDxnzFZkl1BYaQGt08SQUXDwskUue_8aRfkbQ6S4y5W9pnvR6VDp-3LkfTb-5ilcHsVN5kUlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: حذف رانت، فساد و بهبود معیشت مردم، شاه‌بیت سخنان رئیس‌جمهور در جلسات است  @Farsna</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/farsna/457582" target="_blank">📅 20:24 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457581">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cTqVcWPIWdwA3YHSuWKOa7brO6cxfcbVUoa46u5cMUqwLdVKWM9-v9yHTMtbpPxNPIO8FpyTUERhbnwkyPZWdFNiMT0mJ0bl_2YM05g_e4QH2NNsOV_AkhXnWMkvXiFz-xErSxjRkv2pEYYbV7O1QGxfnc4F2Jbg2jAqHnfL-D7j0xONVs2N2_So7mIsLXvYULxwkq_etn4Ae6CZIrdnff-9ZKH3xO63ajGxaKMGvyXluJMfjZcXD6Jh8abNetd9jYnKXT39Na_u0hKDvm8ZzTTTiwQMgG6_BEydLA-GjYwltQL-4dTkXohiYdRK1Gmm-tojRp3-PEjW6mvDoTM5nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا: مذاکرات با آمریکا را به‌دلیل زیاده‌خواهی آن‌ها پایان دادیم
🔹
دیشب، به مذاکره‌کنندگان کانادا دستور دادم که به اتاوا بازگردند؛ ما نمی‌توانیم آن چیزی را که آنها پیشنهاد داده‌اند را بپذیریم.
🔹
آمریکایی‌ها انتظارات زیادی داشتند و در عوض، پیشنهادهای…</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/farsna/457581" target="_blank">📅 20:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457580">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNeGmXB1lmuk5eIElZ79cmSWqBwpYaExgd_Y7djQ-dTYrSjILVzKFveH8ql8t0e6HagPHwOlgwUa5Od5-7E-UP69wK5xQohYW9V4GA8Os7WP1fhs0aZ4pSyQN40XQhti7wSFp1DJS7aygoUkDVwE2twbf3NNsvqVv19mKzT6MKLIJQ-SEbkrQ_iqTm8yZXubquHArDLaH_G4Dv5tcepmBj0iRSl0Gn2ARtrGHD62W1FO3yOnb8gSZUyS04xK7rVLHGMWnDiS_GWiKEX0yY_GjFDLhSfDoZecqJ2avZN5aQBRBHKC9tn4hMjqjOR8uqc9moBDo7KIQtq0GxnPOKu10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
پیام آیت‌الله نوری همدانی به دبیر شورای‌عالی امنیت ملی: تبعیت از رهنمودهای رهبر انقلاب، استقامت در برابر دشمن، پاسخ قاطع به هرگونه تجاوز و حفظ وحدت از ضروری‌ترین امور است.
@Farsna</div>
<div class="tg-footer">👁️ 6.93K · <a href="https://t.me/farsna/457580" target="_blank">📅 20:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457579">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rychQnTBNmLgEWA8xQIlLoYv5_TdxlF3HMpOZ21IVqkVK1V25MSa_jLHWXSsj_i36BYEdDvFerNci2Xbcewso-rbm8JLgF4xl98O9zPe90roEDik0SERhvUVL3NxeLRYKBR7KCAq2ntcelgbk8FtHfvGvm3NYOkgoIdDUNhOdkrY9GEgjcya5TO9B6MEbLitXLGprfQ0XeN5ljWDLgI_lJZrxeJQcx_DIMcFXOdoKxf0IuDzm5mCoBzMRp2BdfN8R9PyW6qCGMfQwqkiKHjTYdUj-eh5Eu6700iIo4xdR45sedSp0200YtsETS8S5xLatKOSlAVqHjIGZxCBqW1h6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
دریاچهٔ ارومیه از قاب آسمان  @Farsna - Link</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/farsna/457579" target="_blank">📅 20:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457578">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bdca204024.mp4?token=iiS_GNhZ1hS4XfZJSJsok7K7WwPM02l4ym1vPxtW-k52anHBu_R4MT42Qx7mhndw3Gm1YiIQGHTHSbzsHsi-2ln3LQXgsVTmAO_qGTTKkBmfcY-CFgK1G7xO9ik9NmgVz6_CWIVSf400sdhjZts0yQNx2bGNUZuRV5Y6mFHJHk2FfncAoDfb3-FlmgMofjbMW9I9tboqN27xVrRykBlu6RawA7Ndbdf1DkQTex8kVIyb3Ful6Kx3FHBOFQmjcdwyUhRfxv7WP7Fp9MFXDqh14Px5-vf3jpHtZedkqeVobViT4WOJRy2eEWozZoLtRmkL3du-2hAWvPjLDYCSiIgJXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bdca204024.mp4?token=iiS_GNhZ1hS4XfZJSJsok7K7WwPM02l4ym1vPxtW-k52anHBu_R4MT42Qx7mhndw3Gm1YiIQGHTHSbzsHsi-2ln3LQXgsVTmAO_qGTTKkBmfcY-CFgK1G7xO9ik9NmgVz6_CWIVSf400sdhjZts0yQNx2bGNUZuRV5Y6mFHJHk2FfncAoDfb3-FlmgMofjbMW9I9tboqN27xVrRykBlu6RawA7Ndbdf1DkQTex8kVIyb3Ful6Kx3FHBOFQmjcdwyUhRfxv7WP7Fp9MFXDqh14Px5-vf3jpHtZedkqeVobViT4WOJRy2eEWozZoLtRmkL3du-2hAWvPjLDYCSiIgJXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت وزیر اقتصاد از انحلال بانک آینده  @Farsna</div>
<div class="tg-footer">👁️ 6.78K · <a href="https://t.me/farsna/457578" target="_blank">📅 19:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457577">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lspj9XfKZ9JiFntq2nhMaEHXB27Hv3BvA9lTbVn1elVwarzklFuBYd-1v6B2Pt6WoKFxprJAZ7MR1zi3FgMLRO9XWPD5fh3ISF4kwswFlbfSHf_Ff-uv3N748jv_4H-ATWaamsGwqlYs5HLDY2zeGo69Y3IA0saSYVUov38cR5zCk5vSe6XhfzWgHn1pmYBAzWWTdrFuXlw9fefffzhc5A8FIBSoonDnSUXTrWJ4xBjSI7x-HuhAhILztHiRSckNDpTeXbO7XVz7hP7ZFHoXXyv0s6YQVmUK9B8URQO0zfgY8GlzSTvgvaFpT9KAAGBfrMJ0S-xV6o_tAdCV6JdROw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا: مذاکرات با آمریکا را به‌دلیل زیاده‌خواهی آن‌ها پایان دادیم
🔹
دیشب، به مذاکره‌کنندگان کانادا دستور دادم که به اتاوا بازگردند؛ ما نمی‌توانیم آن چیزی را که آنها پیشنهاد داده‌اند را بپذیریم.
🔹
آمریکایی‌ها انتظارات زیادی داشتند و در عوض، پیشنهادهای کمی ارائه کردند.
🔹
ما آن چیزهایی که آمریکایی‌ها از ما درخواست کرده‌اند را نخواهیم داد.
@Farsna</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/farsna/457577" target="_blank">📅 19:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457576">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4370e0903f.mp4?token=jyGuTjj2aO77R0iAjipysaik4AP2_AkCNoLuQ_otV1OhzR4ot3oEgzOOtcSE-cLl4w8UofboEsyI7Ds792J7HsnTE15gOGRb5aRG3Ik2FFehKgZk47K9sJ5JIxnyrpXl5bdglmuSieEXKUqm8aGSkfBYBlSVkm0k3Tc6Zarw9nHOQfDJDDSvBJ9CgS_H8t7Tx3DqfeobAET88Z2duxZxlqN1jRSUvOKYZJ6EfC6eIXSs32aXQggavaadU-t0LVXLYrKnujHcrhpPLkDcZuX5uPNxAPZTf9Ssnmm9qjZvSnHqvZB1x748SevroTJuveRRK85ylqRHD-ft1tAcGHBg8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4370e0903f.mp4?token=jyGuTjj2aO77R0iAjipysaik4AP2_AkCNoLuQ_otV1OhzR4ot3oEgzOOtcSE-cLl4w8UofboEsyI7Ds792J7HsnTE15gOGRb5aRG3Ik2FFehKgZk47K9sJ5JIxnyrpXl5bdglmuSieEXKUqm8aGSkfBYBlSVkm0k3Tc6Zarw9nHOQfDJDDSvBJ9CgS_H8t7Tx3DqfeobAET88Z2duxZxlqN1jRSUvOKYZJ6EfC6eIXSs32aXQggavaadU-t0LVXLYrKnujHcrhpPLkDcZuX5uPNxAPZTf9Ssnmm9qjZvSnHqvZB1x748SevroTJuveRRK85ylqRHD-ft1tAcGHBg8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کارشناس مسائل بین‌الملل: با قبول کنوانسیون «رژیم حقوقی خزر» توسط ایران، تکلیف قسمت بزرگی از آب‌های سرزمینی کشور به کسب رضایت کشورهایی مانند جمهوری آذربایجان گره می‌خورد.
@Farsna</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/457576" target="_blank">📅 19:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457575">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTSDOlPbs4Fcf393JvWrfZgEa9hkBFmW4YpZt5UhEuI08FceY-NvwyUtYoXn4eFiZLi5dz13vqdXYHLcVTWxx6aCXkwOcdK-Pnw_dDZgNASn7Qlua1zFxRnmDqIsoRzR_AnHC0Y3QAkuzFFOtP5MKoc0DYGENE4aIcH8S2423Oziy__K4F5mGjtmdNhd46jKo6mRhTKLN2q4ZZSYDSraON4GuFLtWyvyBEQneDUpeqWI874dMxxmet8hhMBaFpyYGlWbRGwPx-gaaRr8yF3Sy81XStmIkk-Tc6SqwZiOEykDRM6IT4N5hLIUHSTBmMylHbWsLqul9lf1UwQ7BcoeLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیمۀ خالی میانکاله به این دو راه چشم دوخته است
🔹
کاهش تراز آب خزر، میانکاله را که به آب این دریا وابسته است با بحران کم‌آبی روبه‌رو کرده و حالا با خشک‌شدن نیمی از تالاب، دو راهکار برای نجات آن در نظر گرفته شده است.
🔹
محیط زیست مازندران می‌گوید لایروبی کانال آشوراده یکی از اقدامات کوتاه‌مدت برای حفظ ارتباط آبی تالاب با خزر بوده اما این راهکار دائمی نیست. اگر تراز آب خزر به منفی ۲۹ متر برسد، دیگر امکان ورود طبیعی آب از این مسیر وجود نخواهد داشت.
🔹
بر همین اساس احداث ایستگاه پمپاژ به‌عنوان راهکار اصلی برای تأمین آب تالاب مطرح شده. مطالعات امکان‌سنجی این طرح انجام شده و مطالعات فاز اجرایی نیز از سوی وزارت نیرو دنبال شده است.
🔸
خشک شدن میانکاله تنها به معنای از دست رفتن یک پهنۀ آبی نیست. با عقب‌نشینی آب، زیستگاه پرندگان تغییر می‌کند. زنجیره غذایی آسیب می‌بیند. بسترهای خشک‌شده می‌توانند در معرض فرسایش و گردوغبار قرار بگیرند و خطر آتش‌سوزی نیز افزایش پیدا کند.
عکس: مهدی محبی‌پور
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/457575" target="_blank">📅 19:38 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457574">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBTjJJZ1Zs2x4BNHw0MECkqTJGqmvOxr4a9Uf3ZipMu3qMSqDdwq0D9tl-jzHKTKmI5w1CQ3y8hPCtx8BR8mNJQONAsFZ7aUCk2oagPtoGUA-okV-2Lj59rC21Y8HR2k-5usAqzyuYNNWBBPBtZarVrtUUWaXRjHkBbYWo_2lH-xTekUQqqR7im6EEF5mhmyy2oMrMmZrlWK-9v0dU1k8bGpqk2FCyjoC3u-QzCjOPZ4J-xZV5w8kqmwCvRu1SG2PfVfv_elw7R-6WTEKUqR5jes3MQzZlnlciHmVFblAC0RMvqvKwVUgX_KZLNkjwSUscgMWmKk6zFxqDL9Eu47DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
ادامۀ جنایات صهونیست‌ها در جنوب لبنان
🔹
تخریب منازل لبنانی‌ها توسط ارتش اسرائیل در شهرک یحمر الشقیف‌.
@Farsna</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/farsna/457574" target="_blank">📅 19:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457573">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc2f4ee214.mp4?token=Gp62WQRcJI24W8lg3ZUfVokS3xB8N51v2p5dXM2dcXeVCiyXsiBoQLiUYvCZ0NycI65uSm4W9LYDaKlYloLNKaDjs2JkFpuxgMQV0UIftK1S8r_rCXu9MGXoM4v5OUSUjxjwBgMJsoTJtNDj3tXVos_S0azFhEPOaXlw86e_GhOr4eUc6N3bc5Ev_PQ7bh2l-hE3hepEXXqESwVG5N2ByoQ9mHQBbjPf01e2jo5_pWL3Qsikv3X1aSpU6y-RW1Bg1isUev39FSGuMrY0hLnOIgpMOGF-nmi9HmEzsSE8qEp9s9XbiUSmbZtRmda8SvUcUfjIdGrAZak8gznlVZBdSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc2f4ee214.mp4?token=Gp62WQRcJI24W8lg3ZUfVokS3xB8N51v2p5dXM2dcXeVCiyXsiBoQLiUYvCZ0NycI65uSm4W9LYDaKlYloLNKaDjs2JkFpuxgMQV0UIftK1S8r_rCXu9MGXoM4v5OUSUjxjwBgMJsoTJtNDj3tXVos_S0azFhEPOaXlw86e_GhOr4eUc6N3bc5Ev_PQ7bh2l-hE3hepEXXqESwVG5N2ByoQ9mHQBbjPf01e2jo5_pWL3Qsikv3X1aSpU6y-RW1Bg1isUev39FSGuMrY0hLnOIgpMOGF-nmi9HmEzsSE8qEp9s9XbiUSmbZtRmda8SvUcUfjIdGrAZak8gznlVZBdSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: شجاعت رئیس‌جمهور باعث می‌شود اصلاحات اقتصادی اجرایی شود
🔹
هر کاری ممکن است هزینه‌هایی داشته باشد و نمی‌شود به‌خاطر هزینه‌هایش تصمیم نگیریم؛ باید هزینه‌هایش را تا جای ممکن کم کنیم. @Farsna</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/farsna/457573" target="_blank">📅 19:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457572">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bba85334d.mp4?token=mzN3B94VPfTHlt05fv2rwYI0aIaWkiOo3ZcXdeNy4qApi3KAp3t9TqMYdXeEw2E60KknzfK3C5Eb1j-PFsEgCWsgMmmigz5o0C42qf2Erw0xuAxFrq-N6T6ieoxhzLKJjYTE5lDiIFtsfSUyHsRxZSUl4rGXKAVyu2a-WiBBTKBC04W6FpLcvOK4hoQ3AE5Sk-ngQOFasRBagWOhA2-JXuGB4OtgzdZf96dRxommS1H44TPPbnhy6ydGwrWqRkGZwWEXdeLUBQXylngH6a1yKt_q5molm4ML1IISUDFyFWhV2l75Pf_ASWsET07UUGDuCTwEC8AEg_6YnBIYhJSe0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bba85334d.mp4?token=mzN3B94VPfTHlt05fv2rwYI0aIaWkiOo3ZcXdeNy4qApi3KAp3t9TqMYdXeEw2E60KknzfK3C5Eb1j-PFsEgCWsgMmmigz5o0C42qf2Erw0xuAxFrq-N6T6ieoxhzLKJjYTE5lDiIFtsfSUyHsRxZSUl4rGXKAVyu2a-WiBBTKBC04W6FpLcvOK4hoQ3AE5Sk-ngQOFasRBagWOhA2-JXuGB4OtgzdZf96dRxommS1H44TPPbnhy6ydGwrWqRkGZwWEXdeLUBQXylngH6a1yKt_q5molm4ML1IISUDFyFWhV2l75Pf_ASWsET07UUGDuCTwEC8AEg_6YnBIYhJSe0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: رئیس‌جمهور شخصاً اجماع‌سازی ارکان حاکمیت برای اصلاحات اقتصادی را پیگیری می‌کند.  @Farsna</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/farsna/457572" target="_blank">📅 19:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457571">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bca27219d6.mp4?token=NFQTuqNTPQwrFQgnFeSBfOvPXvzDPCOexHmF0Oin27FNs8NKjMNgFraXqD5_pRpq2fahmcyNXgrDW5tIOler9zLkNWJgENCCh7TEhY-kMjQrA_XYPs0gYOy_Wn1NQNTxa51CM6CyjUwhunYuv2EJzv8rGnykVTTtm-orB4fd-AZ-63tfX4UcEry1gVxWD3o5669uZHnEaMTy1vBK0GdEo_u9nu2vRvh0u3xV2641TsJXuge0xGbLBBYbAtAK6zRYf-EgM7WXu_Xcv9CdCAcEki_QdNYPMyX2nj3gNjGbCI0BpD1ftB8Cp9wwq0D96tNimIziTLoyhJV68EuIcIUhow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bca27219d6.mp4?token=NFQTuqNTPQwrFQgnFeSBfOvPXvzDPCOexHmF0Oin27FNs8NKjMNgFraXqD5_pRpq2fahmcyNXgrDW5tIOler9zLkNWJgENCCh7TEhY-kMjQrA_XYPs0gYOy_Wn1NQNTxa51CM6CyjUwhunYuv2EJzv8rGnykVTTtm-orB4fd-AZ-63tfX4UcEry1gVxWD3o5669uZHnEaMTy1vBK0GdEo_u9nu2vRvh0u3xV2641TsJXuge0xGbLBBYbAtAK6zRYf-EgM7WXu_Xcv9CdCAcEki_QdNYPMyX2nj3gNjGbCI0BpD1ftB8Cp9wwq0D96tNimIziTLoyhJV68EuIcIUhow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
وزیر اقتصاد: رئیس‌جمهور شخصاً اجماع‌سازی ارکان حاکمیت برای اصلاحات اقتصادی را پیگیری می‌کند.
@Farsna</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/farsna/457571" target="_blank">📅 19:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457569">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/debfb475a3.mp4?token=GpGzTcwiGhGL3N_OUgkPHhNrhg8Pa7aKVxgP-f0SRkPwYPDUOEqGX9WeO2OX556b20o4rNdLJA8W9WGiHA2Hfijhrv8BMVFny9LmS5ifPlyzWdz_uTv0HgsoY9oyuYNVDS1ny4LU_bKXt1U8F8Eabnmw0FmgCNiAFdqwkomjiXZl_BjGH1ZWel5vDmEzSu34W4kkXqPBZ8lcvpa0N4Y7lm1mRhgZoQCwuPDUTVlMYk85_7zzuFo77H8gt-BOD4vDCluyMFkAogKygveFDnklfR-X-6B_pL6IOnZ_Wc4odfJO0FwgySQvdg70cbakw8a5BCaNd5rlvxEaFMTtjS97gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/debfb475a3.mp4?token=GpGzTcwiGhGL3N_OUgkPHhNrhg8Pa7aKVxgP-f0SRkPwYPDUOEqGX9WeO2OX556b20o4rNdLJA8W9WGiHA2Hfijhrv8BMVFny9LmS5ifPlyzWdz_uTv0HgsoY9oyuYNVDS1ny4LU_bKXt1U8F8Eabnmw0FmgCNiAFdqwkomjiXZl_BjGH1ZWel5vDmEzSu34W4kkXqPBZ8lcvpa0N4Y7lm1mRhgZoQCwuPDUTVlMYk85_7zzuFo77H8gt-BOD4vDCluyMFkAogKygveFDnklfR-X-6B_pL6IOnZ_Wc4odfJO0FwgySQvdg70cbakw8a5BCaNd5rlvxEaFMTtjS97gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چطور جلوی قطعی طولانی برق در روزهای جنگ گرفته شد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.98K · <a href="https://t.me/farsna/457569" target="_blank">📅 19:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457568">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CULokS7DPhJyt4l6p91djSlP2VbLRWKny6k3rwbc9ckM452a2lAXqcCKat6HQufig7amesu7Wz3XPKCKBMJ2hrxBC4UjeBj2rdv45er6NFjKRydlAtGCDZ_LXZ2LqxhOxHEpCrb9X3952xkHOVCoZsmqezyO8tDxyD_NYB3jZgNQbN02qoC2UzNVT7a9jHbKWDO_vSyVmbODHer5VNiZOpDp7Pg64odj9EXdy8xDw-NXWvfq6Q4_z0of1naEXimEQ-0p0mfI1cs7EQEI5mB9LRPDGTiYxCZekIOl4E7HfNsFwLqbcBy7PSyGs39FAuMiZvfpDLrq1gfB9xh1EYAs6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
عارف: تجربۀ انقلاب اسلامی نشان داده که فشار اقتصادی قادر به تغییر اراده ملت ایران نیست و نتیجۀ عکس می‌دهد.
@Farsna</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/farsna/457568" target="_blank">📅 19:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457567">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rlRavhFCin7e3BcilRtMEi59IrsFUpWWjxZ9TBh7r7cCmk3m3oAojRhewk3gkXmD7qkOjV076HPsHjjwZm9FyANR_oFQkSvzfKfllkFvC__nxRtRggUxpVoLQ-3inTOVlnyFoaumuTE6NUed4ok-mSMZCjyAxA8DYclE-QRzSFaS80uhBCuNTHXlZQj1on8CBKTynZjuGnbpj6n4DVnuFeYX7sQX48b1RmEQdUvNRXvvyvyZzOXyBmnMJ7bIPOGuYGLIJ1oMF5kGXe71PJHfH80x-f4_D75H1tPrDvYcRfUgjnqEJSArg82VQIhiu2uQt-Qq0al_cJoYlpPvzbJEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در محاصره اقتصادی ایران هم شکست می‌خورد؟
🔹
«هنگامی که دونالد ترامپ، رئیس‌جمهور آمریکا، بار دیگر به محاصره و تحریم‌های اقتصادی علیه ایران روی می‌آورد، یعنی گزینه نظامی که در شش ماه گذشته به آن متوسل شده بود، نتوانسته اهداف مطلوب ترامپ را محقق کند»؛ این مقدمه یادداشت عبدالباری عطوان تحلیلگر برجسته جهان عرب درباره شکست آمریکا در برابر ایران است.
🔹
وی با اشاره به اینکه تسلیم ایران در برابر تمامی شروط و خواسته‌های آمریکا، هدف مطلوب ترامپ بوده،‌ می‌نویسد،‌ آنچه اتفاق افتاده، دستکم تاکنون، کاملاً برعکس بوده است. غرور، حماقت و اطلاعات نادرست اسرائیل، باعث شده ترامپ در دیدن توانایی‌های سیاسی و نظامی ایران و عظمت حمایت مردم این کشور از نظام حاکم ناتوان باشد.
🔗
شرح کامل این گزارش را
اینجا
بخوانید.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/farsna/457567" target="_blank">📅 19:08 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wo_RBO-Y-u2xyyNTMLvddD6rvExtxdRmvpVZpYGn__L36k0ztYV1-qLSyaviSmmc6puigvci71dVsSomeTI2W2R7TCP77PTBOgr-THgPVvzgDKTZOLd6hjFgHIh1j8GMHbYsw2q5bOP_oXoPlRrC3cIFnEE5OED4b2Plu4uNlzs2ZpJsZ-IBkk78E7-lMnkU9v7yeWc2McncttrczLszpOZja5OW2c6Phl5zcmxuAhDq6Ygj1mSv8g5wvKGBX1Kb9DyxMf9gpaQkLTPyV1BzHHBIOcNamR77uCplpOZLiJzzcn7dZGA47PGqgmHJW1Zj4vlwwFXbfcH3kO6DydFp1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
سرپرست وزارت دفاع: میدان جای خوبی برای آزمون سامانه‌های جدید خواهد بود
🔹
سردار ابن‌الرضا: دشمن آنچه را باید درباره توان دفاعی ایران می‌دانست، در میدان واقعی با تمام وجود فهمید. آنچه دیده و شنیده‌اید، تنها گوشه‌ای از توان ماست. آنچه هنوز ندیده‌اید، بسیار بیشتر است.
@Farsna</div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/farsna/457566" target="_blank">📅 19:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/br1V9DQMs9Gp9ZtWsqeJ1V-xTcBQZ9Mi4T8b6bhahu7kZKqlMC05LNLatdX7a1E22DRghDVWKoeDCq49znB0vxc1HGq07akLDByqCRRNmvGw9KWr25V5a7aT3_PQ4VOO3KyNE-a_RwMQR3B2_hixkp0bVLYbYyTbnJWPQzxUYL9azNCQ8gFhHw1XMWR4alj5O_YMM4E3Z6YacLFCQUDcUfJwjefq4878X5EufXJIRQaV0Os8meQYaQyciyCJxDEclJnllBIQkHJfig_wNwzZigqoIjb1ixX3HLNZTYKaMYigk005UvZmcUi_Sd5bvpe0E9Ha9uKYMwBTwCOGcSRq3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تکذیب عددسازی مقامات ترامپ توسط آمار جهانی
🔹
آکسیوس درحالی به نقل از  مقامات آمریکایی مدعی شده که جمعه شب ۴۰ نفتکش از مسیر جنوبی تنگه عبور کرده‌اند که آمارهای رسمی کپلر می‌گوید تنها ۱۴ نفتکش در هفتۀ گذشته از تنگه عبور کرده‌اند.
🔹
ارزیابی سازمان تجارت دریایی انگلیس هم نشان می‌دهد که از ابتدای جنگ علیه ایران، تردد کشتی‌های تجاری از تنگۀ هرمز از نزدیک ۱۶۰ فروند به کمتر از ۱۰ فروند کاهش یافته است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/farsna/457565" target="_blank">📅 18:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/293c15ea31.mp4?token=lUqHt5u_S9PYSaEcdrsOIA2ILH4NLngRqr7g1cf8Ojrcll4TRPOFf21VjgNU9H5c8629ch4PIuH2xRX5kH2LMOt_4Z2GbiOJVseF60plU0jnHWaVKYGh0xFP1KmBhtMIIZU7WChL3-QjS-vjk0OfQrLh9mONt8iC0ecbyanV3g6bRDy2Ui8PFe5kunpoZjcvskysY_B8DcwrghuM8y9cn67qN3jDkd8fqcsnz-guQW6jmnFPFF8b7PbHrdUv-U1QTYpF2DJ1M45S9OmM_aOLfgSFL4DxUWE9DgxNiKTaejCOk_KqsddRAQChr6jj2xUhHj9Uviv1hXkkRobaN1X7Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/293c15ea31.mp4?token=lUqHt5u_S9PYSaEcdrsOIA2ILH4NLngRqr7g1cf8Ojrcll4TRPOFf21VjgNU9H5c8629ch4PIuH2xRX5kH2LMOt_4Z2GbiOJVseF60plU0jnHWaVKYGh0xFP1KmBhtMIIZU7WChL3-QjS-vjk0OfQrLh9mONt8iC0ecbyanV3g6bRDy2Ui8PFe5kunpoZjcvskysY_B8DcwrghuM8y9cn67qN3jDkd8fqcsnz-guQW6jmnFPFF8b7PbHrdUv-U1QTYpF2DJ1M45S9OmM_aOLfgSFL4DxUWE9DgxNiKTaejCOk_KqsddRAQChr6jj2xUhHj9Uviv1hXkkRobaN1X7Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
در میان پیکرهای قطعه‌قطعه شدۀ کودکان مدرسۀ میناب همچنان خبری از پیکر ماکان نصیری نبود  @Farsna</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/farsna/457564" target="_blank">📅 18:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457560">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ivXZX805e_5QfUhgRgSicQEFnWaVdzynKXHm-349k2rLWu95r3nxCbBag2pPoNWxm9jdkBqsV09EMnOD35XLFUhY-ZCus3JXRJKEv52Tqhh0PpZBM6-ow1flXsaNkeCrx56UfyuZQSpFFSdTuSqfvINYD7kr-zT8MwBpvk2ybBJkyHCX8m95nMbtS_MRD34ArMFQWaDf96vp8aAHtXbnP4AKSTkf6S8_qF8dqaZE0PyiybWlvaEpaBHGbxv9pMhIClOL0tekpjfAO_4lRFRPKjTJ-qqesbzVYJEug64iFCE7Oj8XTwpLNPhfyK4lKiY93aRkIb-v2WBwsGLRMSn--w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPIUa1VZeXTw1xagoiaXVDaQVbsjoDuZvnmmWGKrLmxnhNYxXgZSWdGwVtfK0m6X_jXBL3gGyHgxTtWG-Ad3TowuzMDbZyjIuuswusI-Q5ajNRQ_ZmQqPpzvj_xxovdtEYmkcmC4IFoH5lfFuY20Wbm7TEiCe5337QFDxcV-fEisCxJLv1y95UIZWB75HvCK3FcXvDpz21dcEcrQx5uoiEq_9hu0_ljxIUKYyKgUD03Yza1Nw_0SVQyA8kEsfF1tOGTMAnXhSoWUfWalBftLY9o0CJ_cdv2VykrNTzKherSlgLMx612bPaB3bVKNK2N5A4GmFVVUPKmHz7ncI_FdMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OJ9GhKcFujdWsCmVi44RxFfj4zNtPjvi6NbWuGsvESbF_UsM7He5UkyvRYrsELGo1a96jTvTSOzyIBIr9ktIEtG8jXg4eBsrtvjPsM3O0yAIchWXi038jDjhbir7G9TNt0AzzBQB1pTcePxZVnS6VQdAgd2-hU9Yg2Q2LyiI5WNPebZDFEySgJgMg4HGDe_1-7SsFxP3qYCj40dQ0ilsJQn-Uq9FT1VJXruPspHEitXT6iSew0FjNtzMwiuRJFVI-jL-MB6Ljxf8tGUFR-2Z1GmcKKKFgADwrrFh_KAZYuwhmbGaFCeURXgShsvmagcLSGtNnrZYOEydncANSperPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I6KBjCsxolAumKUOWNzSafFQtg3RgfNWO06F6sSlfzWiCqPlhFXVPiyys0bpE5vZRXJRrSUxFe_FyVkAherUhAuEUj9HvZS57EU-6K8MN9oXPRL4pqbDXfoFp3Why3tJdrw5GCMG2MwsR_SXgUm783H7ISTTNAuOgi9E7ayexPn_JQ7V51OYimr6mA6t38JkTgqIhWDhHMDzBi8Y2omUC1AsmvACYImZR51C4w1FGcY6_YInNYEOD8cRUcg-rftyzq-35ISG8y1qf-Tzv-hCWkqJGyuaYQdaiHx0B_6P4jimZE_uJxC3WOr7xZSfsy7KFPZpmQiKbeL2FYawta_U4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نشست مشترک سران قوا در نهاد ریاست‌جمهوری
@Farsna</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/farsna/457560" target="_blank">📅 18:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457559">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9de26de11a.mp4?token=pg1n4WIcVN5H0XksXN2lSqEODehF9xl3rWWVdvjDWuOdmkjDO4Gtza-CR0b18qiLtRTH_Mm1MpOJbAm61nHGh23ittwLoBR6Qg0oXCHfzqr7XordPz8PYDc9OJtbEDIIEebikcj8_9jvv_7PN2ygZp6OJj7EP86XcPRulw2kTYFogQn4G8NmxjB-jTtGLR_OgsyWHBQvSgsU1SzfKlup_ZpovEufTqClZm35B8U-l1yrUBm2vaFoTkXwJxCrq6oO6wMP8jfMfaB0kVUHu9ogND5l1UO2Y46QOctUQmhYFmctIzxC96gIGOy6-jdj2QMUqYM41Tr1dhjhY9d2H02G4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9de26de11a.mp4?token=pg1n4WIcVN5H0XksXN2lSqEODehF9xl3rWWVdvjDWuOdmkjDO4Gtza-CR0b18qiLtRTH_Mm1MpOJbAm61nHGh23ittwLoBR6Qg0oXCHfzqr7XordPz8PYDc9OJtbEDIIEebikcj8_9jvv_7PN2ygZp6OJj7EP86XcPRulw2kTYFogQn4G8NmxjB-jTtGLR_OgsyWHBQvSgsU1SzfKlup_ZpovEufTqClZm35B8U-l1yrUBm2vaFoTkXwJxCrq6oO6wMP8jfMfaB0kVUHu9ogND5l1UO2Y46QOctUQmhYFmctIzxC96gIGOy6-jdj2QMUqYM41Tr1dhjhY9d2H02G4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش باران تابستانی در بخش احمدیِ هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/farsna/457559" target="_blank">📅 18:37 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457558">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7db51a812b.mp4?token=CbYtaoTrEVICxRWP1DU3EY5VWT29aXg2Q9zLNWA8eIVPeawI7pynGHhadpfWCRl5ETGmwgwzMabFIlrdyJEPGjWBwG4rOkW5_eBdObDwW8Vi6yWu6KbQo0Y-tPh15N19KHHBFkFvqC6inAt4Po61r-r4ijLAW1wM148rVagpj6slZfwMCgWJwl5alH5_3hxmN-_jj4Etj2R6W4g_iuLd354XTBXAF7A8BPq3CV2scUP-fPJ7DPfzoxjztUQ6SD5etH_itCyv2D_YZB_8sp1OjHhxpg0t74wM6c2A2lPL3qp-S3s3FNBqramj_GDgAdcn3CrdzCrbhdSDBTgRASO2Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7db51a812b.mp4?token=CbYtaoTrEVICxRWP1DU3EY5VWT29aXg2Q9zLNWA8eIVPeawI7pynGHhadpfWCRl5ETGmwgwzMabFIlrdyJEPGjWBwG4rOkW5_eBdObDwW8Vi6yWu6KbQo0Y-tPh15N19KHHBFkFvqC6inAt4Po61r-r4ijLAW1wM148rVagpj6slZfwMCgWJwl5alH5_3hxmN-_jj4Etj2R6W4g_iuLd354XTBXAF7A8BPq3CV2scUP-fPJ7DPfzoxjztUQ6SD5etH_itCyv2D_YZB_8sp1OjHhxpg0t74wM6c2A2lPL3qp-S3s3FNBqramj_GDgAdcn3CrdzCrbhdSDBTgRASO2Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اولین کسانی‌که پیکر شهدای میناب را دیدند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/farsna/457558" target="_blank">📅 18:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457557">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0-yWR7-ugVBuj8NWZCJgsGMzB4fTT3GHbZeRmMvB6AKI3uuQEUmK0cSTDUwmTFpQ0Yv91Se_5N86yNGfRL2pcOg_7BewqU2yKidYZUAE_E2mijmbHnnn_cIslvYk1oKUcrO8wPCBRCnp2avER3k0Z02Dclp_FP4bQ_IRfi9Y2UNFPrm-092sFZ2a6rAEvxhyIrGMfzBFVGs0whi4eHScR5SrUYl_X6Ut_sDkZeZ5HAzSs2tEwxRSRoiax2gnqTjrAIipC4DHkMoUZWm-GIt_joV287gxGanQORsJ47eyIYT9_6TAiLYidbMp-JzfyhO70Qv6J90KXrATiVQVNymnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب‌‌الله: انصارالله آماده است به درخواست ما باب‌المندب را ببندد
🔹
قماطی، نائب‌رئیس شورای سیاسی حزب‌الله: انصارالله یمن آمادگی خود را برای بستن تنگه باب‌المندب در صورت اعمال فشار همه‌جانبه بر مقاومت و مردم آن در لبنان، و سپردن «کلید» آن به دست مقاومت اعلام کرده‌ است.
🔹
مقاومت تصمیم به صبر و دادن فرصت به روند سیاسی موجود با هدف دستیابی به آزادسازی کامل و عقب‌نشینی اشغالگران از خاک لبنان گرفته است.
🔹
هرگونه تلاش اسرائیل برای پیشروی و اشغال اراضی یا نقاط جدید با مقابله مقاومت متناسب با ماهیت تحولات میدانی مواجه خواهد شد.
🔹
مقاومت همچنان قدرتمند و تواناست و پاسخ ندادن به هر تجاوز، به معنای ضعف یا ناتوانی نیست.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/farsna/457557" target="_blank">📅 18:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457556">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPrgzLbjr4CflzSUDjGLwvG1hvDKlHpd87fIJFr1OA5aYP_6N7queIWcmsjk2F6WLxoEOI0qqfW2PwvRGY4h35L1-mM7on0Ct8kYvbTlsUGyBpBm_C9kBlNOZcHKIZFoayYe5Pe4VPwv_u8tgIJvai06s3uzeHTUW45996KCCbfiWmfteZps0YvzB-tR61Su7ljAb1--LxfDQHi0KWxel3iJEAqxZgdVt1tSKRpyHKL92ZiJeOfOrc3lT7_phq5MwDp3RniFlNw_rUDNYjVFV8OR22001KV7lpDujFMMqVPdK7omw_YTdVcsvJbaVFq11P6QRKUi8uDCHP5e2NuM9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق اعلام وزارت نفت ۷.۵ میلیارد دلار ارز فروش ۴ ماههٔ نفت ابتدای امسال نیز در اختیار بانک مرکزی قرار گرفته است.</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/farsna/457556" target="_blank">📅 17:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457555">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e1fd8ba3e.mp4?token=NyMBG6Eq5VUkjcOigh21AEtNcHjJmfcPgyAgRbCLUXpE2Bl9AbPfshaJApXA1qo2NX0CPWO4Rx3HpNVGZfjc8ogCfosjo96tGbRvDrml_yakqglFx5p4-21upP5cwkvnEtyrBiSMztGWdRiTm5DY2_dtR9Hd2uzrg0zX25z1vskczLQ5m7cabddnPnXrjyBoiMaokDAiE5lsMbFfLqu6d0ynhYgEW5_3Ft6iHkxgrRikw7NQn7wdB2loGjfEniQRPijYXPN0lqC1kGYHBg7qOH3y_qh2lRulQuzVyeqEG6PXpY1QexaqS-drbHk9e23PsIv8EZtAIb_S0tAJlOdeOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e1fd8ba3e.mp4?token=NyMBG6Eq5VUkjcOigh21AEtNcHjJmfcPgyAgRbCLUXpE2Bl9AbPfshaJApXA1qo2NX0CPWO4Rx3HpNVGZfjc8ogCfosjo96tGbRvDrml_yakqglFx5p4-21upP5cwkvnEtyrBiSMztGWdRiTm5DY2_dtR9Hd2uzrg0zX25z1vskczLQ5m7cabddnPnXrjyBoiMaokDAiE5lsMbFfLqu6d0ynhYgEW5_3Ft6iHkxgrRikw7NQn7wdB2loGjfEniQRPijYXPN0lqC1kGYHBg7qOH3y_qh2lRulQuzVyeqEG6PXpY1QexaqS-drbHk9e23PsIv8EZtAIb_S0tAJlOdeOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حملات هوایی رژیم صهیونیستی به جنوب لبنان  @FarsNewsInt</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/farsna/457555" target="_blank">📅 17:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457554">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سیگنال مثبت ذخایر گازوئیل به زمستان ایران
🔹
کسب اطلاع خبرنگار فارس نشان می‌دهد ذخایر سوخت نیروگاه‌ها در حال حاضر به ۸۵ درصد رسیده است.
🔹
این رقم در مدت مشابه سال گذشته ۶۸ درصد بوده که نشان‌دهنده افزایش ۲۵ درصدی سطح ذخایر نسبت به سال گذشته است.
🔹
در حال حاضر ۳ میلیارد و ۱۷۷ میلیون لیتر گازوئیل در ذخایر نیروگاه‌ها موجود است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.24K · <a href="https://t.me/farsna/457554" target="_blank">📅 17:48 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457553">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6526c92bcd.mp4?token=fVFfIkhG10ZElXQgC2-WDbADXekO6rjApe_rdG2R-1XduJzZ5tZrIV-ToMan1K4gBzQmI2uWiU_RTa1mn41VdpxQZHCNK7xIcq8hVbpzk35drjVVff4Bns7fEFbxuomafjDOZiHZ-9EvDu6I4SBjUrBeDoUNTVzsNwS8wFXGS521cTGtM8we-70AK07chkaequdWwcp5_8X8JGdTxzk3wWfrMnieoWw_TOB6N-lByrNtJL6cqRbK8qDp-oRFMMnrWH6Lfw8_H37pFBLJfQcYOQvyWDAZrkgr90T2CS6XUIO8wL-nFTOOS03frtyN7wMzQ-Xlg1-zmLDJivDEeJhnwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6526c92bcd.mp4?token=fVFfIkhG10ZElXQgC2-WDbADXekO6rjApe_rdG2R-1XduJzZ5tZrIV-ToMan1K4gBzQmI2uWiU_RTa1mn41VdpxQZHCNK7xIcq8hVbpzk35drjVVff4Bns7fEFbxuomafjDOZiHZ-9EvDu6I4SBjUrBeDoUNTVzsNwS8wFXGS521cTGtM8we-70AK07chkaequdWwcp5_8X8JGdTxzk3wWfrMnieoWw_TOB6N-lByrNtJL6cqRbK8qDp-oRFMMnrWH6Lfw8_H37pFBLJfQcYOQvyWDAZrkgr90T2CS6XUIO8wL-nFTOOS03frtyN7wMzQ-Xlg1-zmLDJivDEeJhnwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
چرا لایحۀ کنوانسیون دریای خزر در مجلس دهم به تصویب نرسید؟
🔹
نائب رئیس کمیسیون اصل نود: سال ۱۳۹۷ کنوانسیون رژیم حقوقی دریای خزر توسط رئیس‌جمهور ایران امضا شد و دولت وقت، در شرایطی که آمریکا از برجام خارج شده بود این توافق را یکی از دستاوردهای سیاست خارجی خود معرفی کرد.
🔹
با این حال، پس از بررسی متن در مجلس دهم برخی نمایندگان آن را دارای کاستی‌ها و ابهاماتی دانستند و موضوع برای اصلاح و تکمیل به دولت بازگردانده شد.
🔹
این اصلاحات به سرانجام نرسید تا اینکه تیرماه امسال هیئت وزیران مجدداً موضوع را بررسی و تصویب کرد که لایحه مربوط به مجلس ارائه شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.19K · <a href="https://t.me/farsna/457553" target="_blank">📅 17:43 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457552">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c60d36b56.mp4?token=k1UKLNT7Yd5AZbu-YCjS4llLPPDlsxjHJXqcsooblOIG3thACC56-2uOzAuvaBahUME5z3MnVubHZcUJ3EOvNTnPmjO0aYuGgGbTJTspNPeDN1Gmn_NSE19_IKeXRIJUAqX5CI7sDOst62GuBDH1W3Ic4cXq27Bw0DxDnfBMVfhYB-XyKG38jauTbSq1t34u3hfieGwGRI7NEgtCzw2r5emLx5w8mtjBBP18ZzK5175lyOQIjGPBXZxPAC_Ts1hxidr1qYnncgP3wtCFsSkaSdyTV77oVLCBocvJB4h6I5lKZbR2OXKH2wXWcH3xbmTX_aMsIHzU3xiYktRiExFg_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c60d36b56.mp4?token=k1UKLNT7Yd5AZbu-YCjS4llLPPDlsxjHJXqcsooblOIG3thACC56-2uOzAuvaBahUME5z3MnVubHZcUJ3EOvNTnPmjO0aYuGgGbTJTspNPeDN1Gmn_NSE19_IKeXRIJUAqX5CI7sDOst62GuBDH1W3Ic4cXq27Bw0DxDnfBMVfhYB-XyKG38jauTbSq1t34u3hfieGwGRI7NEgtCzw2r5emLx5w8mtjBBP18ZzK5175lyOQIjGPBXZxPAC_Ts1hxidr1qYnncgP3wtCFsSkaSdyTV77oVLCBocvJB4h6I5lKZbR2OXKH2wXWcH3xbmTX_aMsIHzU3xiYktRiExFg_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انفجار در پالایشگاه دارمان کردستان عراق
🔸
امروز یک مخزن سوخت در پالایشگاهی در منطقه دارمان، در کردستان عراق منفجر شد. تاکنون جزئیات دقیقی دربارۀ علت انفجار و میزان خسارت حادثه منتشر نشده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/farsna/457552" target="_blank">📅 17:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457551">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m53GbR8-Fxx1pJzN7L_IMHKHQF6pJ81jOYtx9jWaFOYyi-x-ARGa_vKEw08HaVTfA_7F88QGLzBe_uZ4W1nuRX5KtVk0hPxo1NbWXJjwOq-_mPYMzvvytumfUA_ieKvqCu_5QU45gh7nhKWaPDYjFMCAHrr-m_KhW0e893l4nE5my6BEOdVCp5tORzYo_wXm46anGFbS8XdjOfzItJq8SVPUfSHhaM9tILnp4J9KGGHCtfOVI3pEYgBKBzMjlID45Ff_Sy4cYhfWecQpJSc7K5RZwwKQY0MevzIl60ARi_l7UiAW-NFSbUHdj5gIAhIfS5KdkI0AwhsCuafl-nvf7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف بیش از یک تن مواد مخدر در کرمان
🔹
فرمانده انتظامی کرمان: در طرحی ۴ روزه یک تُن و ۱۲ کیلوگرم انواع مواد مخدر کشف، ۸۱ قاچاقچی و ۶۱۱ خرده‌فروش مواد مخدر دستگیر و ۸۷۱ معتاد متجاهر جمع‌آوری شدند؛ ۶۳ خودرو و ۳ موتورسیکلت نیز توقیف شد.
عکس: مجتبی گرگی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.75K · <a href="https://t.me/farsna/457551" target="_blank">📅 17:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457550">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d10c8f321.mp4?token=f_TzaRw_adGry-iA8GTBscjd0HqLPWwzDxlpr2_NNYD1BCWt_yopZBlFLwe6TUmZPS3srGSyUhauU4zFQjXiRvn_PzoJdflHCmekqXDqIvCL_mB134z0N_yqoVgHmnSNU6wNF7EUL3FR_5TOtYCq3RcBKxY7_L74RHHxwD9hA7ge87HMmWwP8toB9fbXGxt_646Lg5I991vyuuYV5ZsBbeBHn3QrKpo41bqqtMHWdxPFWNpGudKYS9vdKRzYji9Tqd3yYruNjJdJ8GwLz-e8BhsacV0Gq-46l1cKi7G3djIx6Eba2sQj9WtsXSEXldts41VQdp2adBZMRhB_TU2z7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d10c8f321.mp4?token=f_TzaRw_adGry-iA8GTBscjd0HqLPWwzDxlpr2_NNYD1BCWt_yopZBlFLwe6TUmZPS3srGSyUhauU4zFQjXiRvn_PzoJdflHCmekqXDqIvCL_mB134z0N_yqoVgHmnSNU6wNF7EUL3FR_5TOtYCq3RcBKxY7_L74RHHxwD9hA7ge87HMmWwP8toB9fbXGxt_646Lg5I991vyuuYV5ZsBbeBHn3QrKpo41bqqtMHWdxPFWNpGudKYS9vdKRzYji9Tqd3yYruNjJdJ8GwLz-e8BhsacV0Gq-46l1cKi7G3djIx6Eba2sQj9WtsXSEXldts41VQdp2adBZMRhB_TU2z7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پژوهشگر مسائل آمریکا: تهدیدهای ترامپ علیه متحدانش، از کره‌جنوبی و امارات تا عمان، موجی از انتقادها را در داخل آمریکا به‌دنبال داشته است.
@Farsna</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/farsna/457550" target="_blank">📅 17:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457548">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gwbYIBs6vLd1kDwHU3Qh0Hx5v875yoDdkUAbJlfL3ygSc0HHolUKt5phFgjNKRt-LhZoE9ixT0CYUSs_lVBAvOJAClXihCkuJAdtD2BHVaT4hKGXPB-HBjKqe-El0-80xfqguvSOSb4KM1qNUOowtOhizcCmfI2qRQJqmaaOR90jtNmLBiKpcuxwu1UwunJypy7eCTkdVeZm3tqlShEOVnkoHwfA0Vmy-iainTf9ieg62FeI9m-YD5TWgUakn3SUynb7cWQszhPDxxgl-e_M0f3F1XZiqvicMUtaD7lD7KPJEaBWsPSeTpWv89TznJCaJCdrqOMOdyNVw6in18Dm4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mGTQTW2jB6beKeNm5AD9rwPWCf6iaG6wruOVc_vDpqnykrNhyL21hosGB4fsoktxdjVjsUqjy8B0J4vcBvrJmq8Q7ZzbKHWiqew5GM3cGQxHpEv9SF_1aGt0bfAcR4O3K-B2kfY1QH5eOpIjBt0tBFlD1ck0aGtvPHaiYa5GwI-6Vur_DxsdPowuPYigXGbEcLlV60xh7WGIhTaJypZcAVL0mWoytGZY8wxYVXEEMLNZXIE1H9EPvkNSEUi9uhRlb8yp3QCCxc3AC-YaWzegk67riruFOkteMC4SB_rrpNCQUjPofsAO-Xiw2EESJLwsAL7q45x3sRi7fUOiL0wk2w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔴
حملات هوایی رژیم صهیونیستی به جنوب لبنان
@FarsNewsInt</div>
<div class="tg-footer">👁️ 7.61K · <a href="https://t.me/farsna/457548" target="_blank">📅 17:05 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457547">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4409e126e9.mp4?token=Mh-K2Pc7RquS48pocX3-7OldnOs_omERIaqOmjxIUZJrOmgxFxVSWq5NdbaPw6Kr-L_nfrpSiaxOUjX8J0i8pNL3BO3r-DnI9G2naTjv3nRUq90kFfjBTlXztikllSN2qIFdKtle2DccOawSGgK38Kif0pKy1I7F6dhkNd3-UVirOCnccbyBx2Ar-rijOGRhu_AZAzE3mey9oL0J2uvVZt1o-Iqe3AyR-8PZ4-L70j2lJCnkQBWvc2qn37VXl8ab37jnCdxliQfQram-B6d2bn2QGj-X-FkYvpdOV4ixy1l8W4UWZ_5l5hYx52FdIdmJu1-VCbERnEd7HhwH1JsMuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4409e126e9.mp4?token=Mh-K2Pc7RquS48pocX3-7OldnOs_omERIaqOmjxIUZJrOmgxFxVSWq5NdbaPw6Kr-L_nfrpSiaxOUjX8J0i8pNL3BO3r-DnI9G2naTjv3nRUq90kFfjBTlXztikllSN2qIFdKtle2DccOawSGgK38Kif0pKy1I7F6dhkNd3-UVirOCnccbyBx2Ar-rijOGRhu_AZAzE3mey9oL0J2uvVZt1o-Iqe3AyR-8PZ4-L70j2lJCnkQBWvc2qn37VXl8ab37jnCdxliQfQram-B6d2bn2QGj-X-FkYvpdOV4ixy1l8W4UWZ_5l5hYx52FdIdmJu1-VCbERnEd7HhwH1JsMuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایران چگونه در جنگ شبکۀ فرماندهی آمریکا را مختل کرد؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/farsna/457547" target="_blank">📅 16:59 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457546">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rc9RkH0ECjZh9iAi2By0-1xEojJ8t68zSfQpctP0sTg9NvY9WYwttFVZh-xAC4XMe2kd7QX6rlqUyzbKzWCPMrI3y23flAsqbD47FMwsjnfZ9lgJZ0LKnxjMKhc-G8NO3DttUfZA7-otMey3IrrJHCer_hAJNfOmfgUGBxSn6mtKBeNYPaxVu5U64-JrnpqK2CYZsLmkNLofcPTMViRJUVbtLH9PcWD_lQpectn62sBjnPjqJJdz_3po50gG-X4Rib40ApYNoi4GgMiqlkMClkNN_8JLERF4o6-DoEK_OYnTF4NGlgeKjo1sHe2Q0OAySL4vyiIMldQQDQG9GaPNWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
جشن بزرگ عید بیعت در میدان انقلاب
تهران
🔹
امروز از ساعت ۲۰:۳۰ در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/farsna/457546" target="_blank">📅 16:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457545">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a716f3982f.mp4?token=shpaS_MjZyS4CVPt-cEynXc5-5hZmFWX0Alrk940N3CZSVOm-mWk3XQ18lh1aBfD-N8iHCqKxHeolPgBVtoAqTXX5tDgN0fB0WhIYIQTPPeGsA7ASe0k3f6XPQYN-iMds5LxW6ewjmDU6Q5GeOXOKnv8Ux9GuIl4F7w77JLRcmpvdNvTI_NGA1A4onuSPOZU7f19BNfwYxWOoVQuomLwu5fKBhZTIjmfhqfyvWHztAO6t4-c7pwJA2fUj1QFfvt3LaoCT7QbNMIWzCv-sVWW7PbY3nCe4TJrJBW0aChtPQXmYAUjoFeTKhVwuP6QXjxo0a404VQWu736FrKwVSELEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a716f3982f.mp4?token=shpaS_MjZyS4CVPt-cEynXc5-5hZmFWX0Alrk940N3CZSVOm-mWk3XQ18lh1aBfD-N8iHCqKxHeolPgBVtoAqTXX5tDgN0fB0WhIYIQTPPeGsA7ASe0k3f6XPQYN-iMds5LxW6ewjmDU6Q5GeOXOKnv8Ux9GuIl4F7w77JLRcmpvdNvTI_NGA1A4onuSPOZU7f19BNfwYxWOoVQuomLwu5fKBhZTIjmfhqfyvWHztAO6t4-c7pwJA2fUj1QFfvt3LaoCT7QbNMIWzCv-sVWW7PbY3nCe4TJrJBW0aChtPQXmYAUjoFeTKhVwuP6QXjxo0a404VQWu736FrKwVSELEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای درگیری جنگنده ایرانی با اف۳۵ در آسمان تهران
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/farsna/457545" target="_blank">📅 16:52 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457544">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeb916be65.mp4?token=Oc6TXyHCuGnIyAW7_dJrI_hvw1fqpZRKcp8fUeIucbcxSxEm2NjVjHxxEnLYGeZV_8buFuZc1fui2tZB7UJ8jhiZMCWC8sPRKjxup3XUtNqiHOHweP2oS7v9Za5YjLXPxRTZqiEyEYICf3KB-ARuK9zYgr-xqSUa22I9RqdboYfbFnTXgZ0-HsUs7Cmp9EnnADihfTd-cojZaNuSwjnQVhNbAr6RmvCrutBCdiQtWBH1UXGZ62nXt57D6CXPItWPfPnsX_eTTbuqfPwk3aAsQfJQ_Ks7Q5YG-ceaGeBYuytIEZ0LtPBioiuH0bnM3PZmZGv57LFSSNRGSHSbDjMIJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeb916be65.mp4?token=Oc6TXyHCuGnIyAW7_dJrI_hvw1fqpZRKcp8fUeIucbcxSxEm2NjVjHxxEnLYGeZV_8buFuZc1fui2tZB7UJ8jhiZMCWC8sPRKjxup3XUtNqiHOHweP2oS7v9Za5YjLXPxRTZqiEyEYICf3KB-ARuK9zYgr-xqSUa22I9RqdboYfbFnTXgZ0-HsUs7Cmp9EnnADihfTd-cojZaNuSwjnQVhNbAr6RmvCrutBCdiQtWBH1UXGZ62nXt57D6CXPItWPfPnsX_eTTbuqfPwk3aAsQfJQ_Ks7Q5YG-ceaGeBYuytIEZ0LtPBioiuH0bnM3PZmZGv57LFSSNRGSHSbDjMIJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
دیدار مقامات وزارت دفاع با وابستگان نظامی مقیم تهران  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/farsna/457544" target="_blank">📅 16:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457543">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0I7djpB4MM49nMzCAK720FkdvFXXgpevk6phdE0Hi9qftYwPow7a0v71dnecwoHXj1rwP-MDaq3Xt_8km0iLRbkYNxw5HauM97sQgWbGfic0x2i0xnOuxSNX9Dp1-ppN8fSQLOLFIxRklnctrPIZN-QsgI-uo9rBKEjyo0i-DzEgYuyEY19R9z_vNsG7LIhmZhcrhQuM-kv6I_Eide-brLjMW42eriXEJL7ibajDHCJR-4cEtTBlWj5fcdPPZXF5_mRY2ObcPd83L3sC8VNiyV--cV0ibpCpkkvl8Z9ZGP5T3wDpuX1CTXD1DqcWllWN0pPAREb59Lh1uYtTG-wRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی: بدهی شهرداری تهران از ۵ برابر بودجه به ۱۰ درصد رسید
🔹
بدهی‌های شهرداری به بانک‌ها از معادل ۵ برابر بودجه سالانه به ۱۰ درصد کاهش یافته و بودجۀ شهرداری نیز نسبت به نخستین سال این دوره ۱۲ برابر شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/farsna/457543" target="_blank">📅 16:33 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457542">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRvmZ9mXmULNYjZa3YLvjWuT-jNRAjqI1GyRIomEgswbNa9YLTx80Hz203950SVk62IkoGUnUatBxWQPSHhUK-KfCehT3v1eiXGzt7UUipVJQBInvEMaOwalzEFgtZC72rB0s4JH7G8_b740fTORqlPCqUDWgY6CJaWJkr9RFRPYnp8y8rmcOhl792-Qs-UfROcD3Z-rtR0YVMTvP8qJbaBAC8OUY4uoJLyOh1ribGYSqyij_uNQFdRhpG354BAABoznxNs-Cas8F3av0vjDiasSmlhD5E8nfVIwFNgJAGvyxy1uqEx0sZJuXjPH7s4BKSuscg-qCNSwyRfcs9Ns7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حملهٔ پهپادی اوکراین ۲ پالایشگاه روسیه را از مدار خارج کرد
🔹
حملهٔ پهپادی اوکراین به پالایشگاه نووکویبیشفسک در منطقهٔ سامارا، موجب آتش‌سوزی گسترده و توقف فعالیت این پالایشگاه با ظرفیت سالانه ۸.۸ میلیون تن شد؛ همزمان پالایشگاه پرم، از بزرگترین پالایشگاه‌های روسیه نیز هدف حمله قرار گرفت.
🔹
افزایش حملات پهپادی به زیرساخت‌های نفتی روسیه، تولید بنزین این کشور را کاهش داده و قیمت آن را به رکورد ۷۷ هزار روبل در هر تن رسانده است.
🔹
مسکو نیز برای جبران کمبود سوخت، صادرات بنزین را محدود و واردات از بلاروس و چین را افزایش داده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/farsna/457542" target="_blank">📅 16:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457541">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12c99f6d7e.mp4?token=s7hrsIftJ3pTxjNVgr2Zszq6212tNgjBrdfW7yXrHq_qK60jN2IRIestq1WfZbeqCmf9EA0rdL7wA6dKR0JkS4l2_LwkwNtTge1iNJpV5BsfOVF8oGuy2KjwuW5YBW5AgBnNHBKBMW_Smc5PvJlfSCVI0WNMveyyrkUQin2dEw9NwPNk4x1szAGD3iiJ71GT36z2HhJtq4DtR07UXjIJnj-Dz3HFe_qnvIdCQvQBmqZi46OoTl_3aEpyXTaA1HNXcUTGNZ5yQv9Nk0b2TFHgPTgWjG6uSDydiKTFQ3Jsz6paayUnE8JsPjhPwyEsdDPsLUzaS0BRtYKovXTc7Egy6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12c99f6d7e.mp4?token=s7hrsIftJ3pTxjNVgr2Zszq6212tNgjBrdfW7yXrHq_qK60jN2IRIestq1WfZbeqCmf9EA0rdL7wA6dKR0JkS4l2_LwkwNtTge1iNJpV5BsfOVF8oGuy2KjwuW5YBW5AgBnNHBKBMW_Smc5PvJlfSCVI0WNMveyyrkUQin2dEw9NwPNk4x1szAGD3iiJ71GT36z2HhJtq4DtR07UXjIJnj-Dz3HFe_qnvIdCQvQBmqZi46OoTl_3aEpyXTaA1HNXcUTGNZ5yQv9Nk0b2TFHgPTgWjG6uSDydiKTFQ3Jsz6paayUnE8JsPjhPwyEsdDPsLUzaS0BRtYKovXTc7Egy6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائب: آمریکا پس‌از شکست، به‌دنبال فشار و اختلاف‌افکنی است
🔹
رئیس سازمان بسیج: دشمن به‌سمت محاصره دریایی رفت و تصور کرد می‌تواند با محاصرهٔ ملت ایران را ضعیف کند و به اختلافات داخلی و ایجاد دوگانگی امید ببندد تا آبروی از دست‌رفتهٔ خود را بازسازی کند.
🔹
ملت…</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/farsna/457541" target="_blank">📅 16:22 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457540">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db4e51aae7.mp4?token=nrrv0YUSZg4Uhl2KVEE8Wheb5YCRD6wydXYQmhxNDZrJL7CmYn9XHZ23Sx9kX8UIDL_zFpwafJer2MOQxX0Y57PLwm_iL-JxOZJk_int9bRuZtU93jZHBiNa4H3yL6RNl3hp9GkU1NdNYI_VfFyFX8yMxTDEIwrRH9j8qlraSCAt5tXxCJ8JfwI2D1tI7f-3wNEOGaCaUp8SfA9GAx1C7yede9Xhbf4TLz5bQGOq6eC1BNhEV8u8nwVepWV4zi2_16jvnDUfxSqEuACCC_TbZnitZ5SC193UCZUhviuKtdmCubJn0dg2EKB9joQkqq0Et18EBY99pToGVfYisK3LjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db4e51aae7.mp4?token=nrrv0YUSZg4Uhl2KVEE8Wheb5YCRD6wydXYQmhxNDZrJL7CmYn9XHZ23Sx9kX8UIDL_zFpwafJer2MOQxX0Y57PLwm_iL-JxOZJk_int9bRuZtU93jZHBiNa4H3yL6RNl3hp9GkU1NdNYI_VfFyFX8yMxTDEIwrRH9j8qlraSCAt5tXxCJ8JfwI2D1tI7f-3wNEOGaCaUp8SfA9GAx1C7yede9Xhbf4TLz5bQGOq6eC1BNhEV8u8nwVepWV4zi2_16jvnDUfxSqEuACCC_TbZnitZ5SC193UCZUhviuKtdmCubJn0dg2EKB9joQkqq0Et18EBY99pToGVfYisK3LjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای آخرین لبخند شهید شمخانی
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/457540" target="_blank">📅 16:15 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457539">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLr8r8Ur_p1KDMOlIorBH2U6LkeSFXVlo34f4Aa2Xft_kDr5X7rO_0eSk9X17uw3GPvuYNa_ux81jNV5HJr54q3iTErOqfQx5pnFyGDgiKwcMsBtRzbfj-1y79dSXPFX3_H88u8f6Qomx7MDqp-MEuaGmx6UlYGu0d5hJSUlm7K7h9qA9NU80YiZvAJMmUwXVGQSAQf9GaG2ySVBwbQK12nuGtrlGXLZxVaWsXdQWsPhbt3wwq6fOG6JghGJmNRlGHcAkbauY9wUy2N7Tcb4el3dbhg5P4yf6px5yaBtD6BdriM2UUM6bqTztBroA1iDEEHJsnggdx2YpzBOZSCDuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: در شرایط جنگی هم سامانه‌های جدید وارد میدان شدند
🔹
امروز صنعت دفاعی در ایران با وجود مشکلات و تحریم‌ها توانسته، دستان بلند نیرو‌های مسلح را قوی و با اقتدار کند و با وجود ادعای دشمن مبنی‌بر نابودی آن در خلال جنگ‌های اخیر، با تدبیر و دوراندیشی‌های…</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/farsna/457539" target="_blank">📅 16:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457532">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fSulO-X-uswITZMOOGHXgFjK_-R5eMs4qlIIAZUZN2J9jKVaypwyfYtxlhBGClJAzEajlJ8kOYyhzR4RHuTV0KpYl6nHqbzVlCo75IqUQbEHpZIV7HxbdcHIepmIrMU2m4Vxvho5eghYXHkNCGFUVRz2ufm59nder1p-5EUSVA8EOfvp3T9MTBEExeGrR61YKCOCOS79RszbtZQIoLIvF_n3OZoeLLeIOXV6w6dI2uEldS6FfqWUCjt8BwsZCkLVanW5Zsh1hPSSx52abU7BlWjbi2kbDWUdQUb9i_CF-eC3GYEQphQZm19betWTW50-zmPsyfOPtrzXZAsCynbVcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jB9o47MqP6BIyLRRJHZmdwd74G1UfZOW6PGxKJMRxD_qm98mmIcxq8-WXRUSNUiKfwpE2EYTofI1Z74yKxKtOC56ymWvU5Ucj4xxUja4yTZxcSVI5PFysSroiWn0Qm1EMsFUIE4Ut6NP6Rkt3idteKEV7ERBD_7Ra1e618_ASwRGlrPSN7mWJWpYWjeDf4WuWHrZ25yZAEOZQ8F3duwptNPBkoUt_Eu3oEH5ygFIxeXuStD4g504WydYHfj6B8Y1K-wJ_bKUfLmd4Fy2DEyMZKzRb3odCvEWG383SPe4eQEexIX3anviuW7sQstYA_LaaGKJaEVSTTkIrKyw26rn6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyw5-URzUVIfMiJEIVjcZrNhNKZVKNujHj61DAFKkp1qCUjEODTRkYvs_V85a3gRKsy80oPoyMhf6zG3PBStIAltZMuLK9pPSoYuPH_NqAXsiWeKN3_lok8Bs6K-wPIme8-z3CcGCjHrD8WdjVDh36Q02em8xwgLOCLzmwv8zvYSLX354QRT4_Itiq0NJ2ipAFCJAIESbypdk7GD7FnaiiCcK7G2kYfhe1MBHxXXFa6OkJbQnL53ChR9sfkfmUBIHDDTPpud4sap-DrRGjpHpqTzdVPRBUxgnMJdudtt7YrsuRl4vnJkTdVHRkD4dBeY4k-fXxXTp3uAM80T90eBmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RNHnklP_JaOOnNU4s6mDru6lrgZ9ucTttDBDYTE-e6wAyoEp_H2VioTnNS-Zt5gws7TxZxG6qmNlzn2pLATJ6A2fIQWXkzxwBTgd2pM6ad7FnGdEE7ZGVI9VtJgo8Gcit_bmhq6ANQhUho0lWAknPJ4qfF96FQj_gb-pFdkfRzSZuxNWiSl1kX2-wF7OF-eDrGHAQ1WSLmKUtNw3XdhcKmms0HTlR744V2w6tiEAq9I4XeQn0Scy5o6A8sd2ZuBLT5L5tkYptLLd1KQ_lu-3cxT69V8pxAUQWiAoD9sjE8qIjN1Bf7nlvaS2aGB2n8f2slV58O3jl4TFBUgd_NAIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iZ4-nwH77OVGyKQ0YNWcm9-FR5WfKRxsd_dvWSFIVNYWX0wNNB-8GGzkFgJiRwOekGCVF0FUhx7ahG5G89e2qDr0anYy_pzwxCSMLclLjWkU_-5SFsL_27Q07fLBXylMObeo1W27yPXK6HaLBmKKugKbtk6QHo9SWPcjj5WYpTc2dHUEi4YQ02iRi-FXQ49F2iX6ENynpE8ReskAjO4WC3f-GAH6vx87lCV_dmla2-8MXMq-DtQLLUoq88v7fzfGdXARPLmnWGNuWBx3oBzOgx2deYR6drGfxyVLg8br_SXIB9QsfCkmLv2HkL2zViisyQg5kUVsimIBcCNRUY6lAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nnwHccKK_RpvY18qFoVxBex8foqScN6MfuOQROJgzO4fACSibohyRPKVeGWU4mTN4sTeJD-g-nH1JN1kYSWpX2GIRWzPztNMAmHHBeQWx04yrgGaYDfTP-R3g6chrWgqfz9i7vzwUchi84_X3kSQGN-P_5PYu1t2gsm8GeF8asDGzLSY2nEssnaCZa8_sEGZkH8z13xe8sGT1BbrMgdqNss_6X2UIzH3ek0eh7Rs4OdSEpavo5s-M5pzCwWs9npWoaZfeGy2YllBAz-vXZAlKk_4Si63O02pB7xH2ZpJ-4YmeeoNx9i_Mwic24EVvDKLSv5U9A-HLP0cR_xn8JPOjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l0Oj6CpA2BclbRQ_FrAZjDsNtlXO-auX2djWg7zlmkseaDdL7p240F_9zJ-3HgYAHpgUJ3w6-yH-EKEES0OUJ3RvChS-XfktWo8DliXCCeM8Y1_EFSJAwjdkpnByyOkqyTzi66GZgql4Ib4Gwhe8JGfVd62QEK6Zm9BuckbU5MIQTcifKMyxZ2UXdJwlivZf4i8w0K3ahoTvCvEIv9CaVhc2U0hc-yDYqE5p0ORzWBkv5IhgWK8XHWLTtZGIRnwLuEKj59FLj0HyooyYmSnLlu4VHN_Tzw7nbeTuX-c36Eu-L0ulW6qfZqogJa-srIqQRgrfKtUn-nMR7L4rHUi-4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سرپرست وزارت دفاع: در شرایط جنگی هم سامانه‌های جدید وارد میدان شدند
🔹
امروز صنعت دفاعی در ایران با وجود مشکلات و تحریم‌ها توانسته، دستان بلند نیرو‌های مسلح را قوی و با اقتدار کند و با وجود ادعای دشمن مبنی‌بر نابودی آن در خلال جنگ‌های اخیر، با تدبیر و دوراندیشی‌های…</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/farsna/457532" target="_blank">📅 15:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457531">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e9725990c.mp4?token=WmuIRDOGrSjALen4r5atkjvzofrNXy8TYEl6qlSwU3u-0vVRgSmIalzqchvJvsllTURWmUSKHhO0wqGs0OqP_Net9O_nK2RF5PtaXTTEs3zxmyc8QoKKLuaAEEOMazBnfAlIjl0bQwi7LRPgIi6noflc3lXWR1l1NN1sa78BcLLwUvsvtDLodBJhhmr13_1AguY9VcoqcD2qnrxvPulg-fO6pNfMN0UFMiD_Vi54OVlWUaa0D8tINT80FYfY1NRzMyhislBInLPuoSj-w9ROBdwCWjjX5_r56yO1m_ufWXvXXtzgDHyyLF9svUyMKEAAUjnDxEit4LRa5AAsDb90-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e9725990c.mp4?token=WmuIRDOGrSjALen4r5atkjvzofrNXy8TYEl6qlSwU3u-0vVRgSmIalzqchvJvsllTURWmUSKHhO0wqGs0OqP_Net9O_nK2RF5PtaXTTEs3zxmyc8QoKKLuaAEEOMazBnfAlIjl0bQwi7LRPgIi6noflc3lXWR1l1NN1sa78BcLLwUvsvtDLodBJhhmr13_1AguY9VcoqcD2qnrxvPulg-fO6pNfMN0UFMiD_Vi54OVlWUaa0D8tINT80FYfY1NRzMyhislBInLPuoSj-w9ROBdwCWjjX5_r56yO1m_ufWXvXXtzgDHyyLF9svUyMKEAAUjnDxEit4LRa5AAsDb90-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بارش شدید باران در حاجی‌آباد هرمزگان
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/farsna/457531" target="_blank">📅 15:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457530">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d03d1ff8e.mp4?token=IapewhYObD5Cz-TNzj7rNkS3LCzBcaezEbF5_8nwEtZ_Oy6JWWq2QuYpzSUi3ScX55JUBml9YvszNU5HPRUZCD1-wDQWxtn8dvt_u_wnC9n1Gfwv8dnsoj28meaQJhK3eNkv9s2FWaX53V7iWdKM2BKrYPJQ6oQo85frpmJVw2IKC8cLy53eCqtM0YMzU70w4JCKbuPXURh91chPCrOMrOQaqUgVrueZxAoiwzHng-P5VExMUQac_yD_uRb-GpcP2W8HysrgZSn-U6te-hUJQ74nivScQIgJuZQDNCQnA2dRTtDsUxO6yJMadeoV04Y4hJoP-3vhrUHocmrNJHj7CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d03d1ff8e.mp4?token=IapewhYObD5Cz-TNzj7rNkS3LCzBcaezEbF5_8nwEtZ_Oy6JWWq2QuYpzSUi3ScX55JUBml9YvszNU5HPRUZCD1-wDQWxtn8dvt_u_wnC9n1Gfwv8dnsoj28meaQJhK3eNkv9s2FWaX53V7iWdKM2BKrYPJQ6oQo85frpmJVw2IKC8cLy53eCqtM0YMzU70w4JCKbuPXURh91chPCrOMrOQaqUgVrueZxAoiwzHng-P5VExMUQac_yD_uRb-GpcP2W8HysrgZSn-U6te-hUJQ74nivScQIgJuZQDNCQnA2dRTtDsUxO6yJMadeoV04Y4hJoP-3vhrUHocmrNJHj7CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اعتراض فعال نیوزیلندی به حمایت این کشور از رژیم صهیونیستی
🔹
یک فعال حامی فلسطین پنجشنبه در جریان نشست عمومی نخست‌وزیر نیوزیلند، در شهر کرایست‌چرچ، به حمایت این کشور از رژیم صهیونیستی اعتراض کرد.
🔹
این معترض خطاب به لاکسون گفت: «شما از نسل‌کشی در غزه حمایت می‌کنید. باید اسرائیل را تحریم می‌کردید، اما در عوض از آن حمایت کردید. آن‌ها ۲۰ هزار کودک را کشتند و شما به اسرائیل پول دادید. آنها کودکان غزه را گرسنگی دادند و شما به اسرائیل پول دادید. شما باعث بی‌آبرویی نیوزیلند شده‌اید».
🔹
او در ادامه گفت: «اگر این اتفاق در دهه ۱۹۴۰ رخ داده بود، شما از نازی‌ها حمایت می‌کردید. شما مایه ننگ هستید. شما جنایتکار هستید، شما از اسرائیل حمایت می‌کنید.»
🔹
به‌گزارش روزنامه «نیوزیلند هرالد» نیروهای امنیتی سپس این معترض را از محل جلسه اخراج کردند. این جلسه که در راستای فعالیت‌های انتخاباتی لاکسون پیش از انتخابات ماه نوامبر برگزار شده بود، با اعتراض‌های مکرر چندین فعال دیگر با محورهای مختلف از جمله جنگ غزه هم مواجه شد.
@Farsna</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/farsna/457530" target="_blank">📅 15:47 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457529">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fDn0W9BVRARXObh_hf1dxhJgrVh4eLK--og5SrkRAyfg3w6JZHRjO1N6UWtgMYyA_2NXlg2JHpiGCRrgnepUAgS-a5tup4whJSKeRG0sQXZFHX9Z8xgxtQgMfhQrxQ6ZeqQBSidcBkbSCO7jd5McB0YoQNl5Fzfy2D_-YzwWAvXkNkQy9T2105hSZcd39hIzLcAj3yiSdYN0h88RjZNjGL156EL-CUM10xBnOzztSn1kJUgBvYlKfVfYr4e5bSQLzfG-l_WRuhUbLuyenbAoHTdK7BPOPmLhFnqmAIElBk-H9FYg6jFm1-2uqNUL8YGtkm2l4sCK9X_zYpc22UBHow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
مهدی طارمی با عقد قراردادی به الوصل امارات پیوست.
@Sportfars</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/farsna/457529" target="_blank">📅 15:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457528">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3f4182b4.mp4?token=vxV7bbvwZgajEYVbnLyZsCbtNJkjSeN-xjnDkH_fi4C9fadYumqXX_OU-Q1Wnqmd7L5hBYiQJdkLi5f8f5RMrV6kydbnA1qQV1skZYsU2VCbG_YLQx_Y06pHWobKeu182xwkEAtl9ehfQK43eXrojsI4BSZ1r2IwxCNW4K1PPtUmoZrHGTztk0QA6omZj0EsmANC30261tvMJBJLV-3G_Sb9slqRczKObkL6NPCX346Q76PwPZrOoF68DWlWxxXFKGzCZnEcLJ1_jVumHQiy-mGQrS2DgA7nNcFCt2Y7zYuTVCmyqNt9iHuTy036AtNdSpLvutGhsx0kJA9XEXte8rB2rsNw_4yRs3CO6i1vyXXawF4juQlCz10ZhXzZMA2Ear_azS2gyFYVcVZZrkfI4zyGcNmq06A6B9JL7n2-pKZuMsDnLehad0x97Zi9hzmWvjDOY76NXxNvkIHDwqanomRlcy4Di4JL2fzZ0D6kDvncWG2Lq8tQlhIyHFSSGLn3qQQEhaeTeM4kOLN98at00AckdvtBjRoliPQ-ed-eA8CIVtcQr8_5NK_DN52YtUBn9NbuxM3-zFoB__lpLErjDN_aFgM4o8Wl45UX0vfAaPYEyCS0e77fqk8On8wp_9w9gitqlBEfC5ZlWK3Rv0gwmDb8zwmf-tpimZdJsr2VDXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3f4182b4.mp4?token=vxV7bbvwZgajEYVbnLyZsCbtNJkjSeN-xjnDkH_fi4C9fadYumqXX_OU-Q1Wnqmd7L5hBYiQJdkLi5f8f5RMrV6kydbnA1qQV1skZYsU2VCbG_YLQx_Y06pHWobKeu182xwkEAtl9ehfQK43eXrojsI4BSZ1r2IwxCNW4K1PPtUmoZrHGTztk0QA6omZj0EsmANC30261tvMJBJLV-3G_Sb9slqRczKObkL6NPCX346Q76PwPZrOoF68DWlWxxXFKGzCZnEcLJ1_jVumHQiy-mGQrS2DgA7nNcFCt2Y7zYuTVCmyqNt9iHuTy036AtNdSpLvutGhsx0kJA9XEXte8rB2rsNw_4yRs3CO6i1vyXXawF4juQlCz10ZhXzZMA2Ear_azS2gyFYVcVZZrkfI4zyGcNmq06A6B9JL7n2-pKZuMsDnLehad0x97Zi9hzmWvjDOY76NXxNvkIHDwqanomRlcy4Di4JL2fzZ0D6kDvncWG2Lq8tQlhIyHFSSGLn3qQQEhaeTeM4kOLN98at00AckdvtBjRoliPQ-ed-eA8CIVtcQr8_5NK_DN52YtUBn9NbuxM3-zFoB__lpLErjDN_aFgM4o8Wl45UX0vfAaPYEyCS0e77fqk8On8wp_9w9gitqlBEfC5ZlWK3Rv0gwmDb8zwmf-tpimZdJsr2VDXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
تصاویر ربایندگان نوزاد تهرانی
🔹
این ۲ زن متهمان پروندهٔ ربایش نوزاد ۲ ماههٔ تهرانی هستند که یکی از آن‌ها نوزاد را دزدیده و دیگری او را تحویل گرفته و نگهداری کرده است. @Farsna - Link</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/farsna/457528" target="_blank">📅 15:39 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457527">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/slL58QenS-oh5JePEi4_OwDrYh1L8XAGGW2xt8CaLbuxQidmGeA_b8yp9pD-gKT7sQ9K-Jr7RjAnViURmCxA3dp7w5ciJBay_l1MsaWNu0BlnlqXyBk29ff9LmpQNer6qwGM73OvYoGKGn9fCmMASrWi1n9RWzWtnp9swPLUsAi4TIxejRRysATmNnsUI6Difn633xPqpz7ZjTqEmXVxhOh_yFox63KBveN5ba1J3RybHP42VjHf3Y77ptdKA8_IptbS8xOHJpxkd2cWCmc0vHtUIBHykPWpq8faMdmjRjJAsY-kRwPt6dC1nhtCt-y3AZHY5TMKCV2B2kTqCvJFqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرپرست وزارت دفاع: در شرایط جنگی هم سامانه‌های جدید وارد میدان شدند
🔹
امروز صنعت دفاعی در ایران با وجود مشکلات و تحریم‌ها توانسته، دستان بلند نیرو‌های مسلح را قوی و با اقتدار کند و با وجود ادعای دشمن مبنی‌بر نابودی آن در خلال جنگ‌های اخیر، با تدبیر و دوراندیشی‌های لازم، خطوط تولید تجهیزات و تسلیحات مورد نیاز نیرو‌های مسلح را فعال نگه داشته و فراتر از آن موفق شده سامانه‌های جدید آفندی و پدافندی را در شرایط جنگی وارد میدان رزم کند و این روند همچنان با قدرت ادامه دارد.
🔹
ایران هیچ‌گاه تسلیم فشار نخواهد شد و نتیجۀ این مقاومت تاکنون منجر به شکست بن‌بست راهبردی و سردرگمی برای دولت ترامپ شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/457527" target="_blank">📅 15:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457526">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j602MIeAFljZ8e1ifYB89tCutVfJ5HxQdK_bI-h57O-OxLrtbqtvA5ZSSOHUsG2w6KU9Aju3KtZZ1cWrOpf2pbrERdm_Fx_Hz5wTpHUifvJ8OMuZVIywOqwVVUENiXXyfZtvVcS_ndwvasDudE1Rebm5Cr2Oj0Jmy8af-URGtDTc6oJGsA7ufS-CFk1es08sVvwJ5uvD72A4Tk7ipDJI8u6K1RrAPYRbmnoWISDEJBQOjDAKaM6s9iorVhLEP7Rt2OstOcBLqpp_JDpycyai6iSnaIyrKWNSFo-rxmZ6BJd4kxVKshbwUXbVDpx_xdjHkeO4Fdj6TVNBjbkbB2iikg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بادهای تند در راه ۱۲ استان کشور
🔹
سازمان مدیریت بحران با صدور هشدار سطح زرد، از احتمال وقوع بادهای تند، گردوخاک، کاهش دید و خسارت به سازه‌های موقت در ۱۲ استان از فردا تا چهارشنبه خبر داد.
🔹
خراسان‌رضوی، خراسان‌شمالی، خراسان‌جنوبی، سیستان‌وبلوچستان، کرمان، یزد، فارس، اصفهان، مرکزی، قم، کرمانشاه و ایلام درگیر این شرایط خواهند بود.
🔹
همچنین احتمال شکستن شاخهٔ درختان، اختلال در تردد جاده‌ای و خسارت به محصولات کشاورزی پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/farsna/457526" target="_blank">📅 15:21 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457525">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=R7ESfRxG78TqPKCmS9MbZ82NLfvldPlCNlCfFdT-MrUOUFObskMznWPB3vosGOCCRp9AyPNjLI3sR5Ynrl9_T83lBPo4CWdJDgD8qArrFDXG-ff0VWJj6NY-BsA75YXzHyZQuAfvWPnrz-bZhcnsC0HSc2NpZAYV1L4lk-gtvhh2R3Jv6npl9R6kus0bC1VubL8F2HaK5xup3CgpPrIuEhLo9CPL8ouWz0M004wkdMMCSnXKnIBHom2ApYxAbJklKmA0EKbTZNGybnWibkENjdMApsVIKhyigg8MY12seRLvmHd-EzAavQYJbFBhEUEjEpsdeyKx7HevHHv2WKf2Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e76845d14b.mp4?token=R7ESfRxG78TqPKCmS9MbZ82NLfvldPlCNlCfFdT-MrUOUFObskMznWPB3vosGOCCRp9AyPNjLI3sR5Ynrl9_T83lBPo4CWdJDgD8qArrFDXG-ff0VWJj6NY-BsA75YXzHyZQuAfvWPnrz-bZhcnsC0HSc2NpZAYV1L4lk-gtvhh2R3Jv6npl9R6kus0bC1VubL8F2HaK5xup3CgpPrIuEhLo9CPL8ouWz0M004wkdMMCSnXKnIBHom2ApYxAbJklKmA0EKbTZNGybnWibkENjdMApsVIKhyigg8MY12seRLvmHd-EzAavQYJbFBhEUEjEpsdeyKx7HevHHv2WKf2Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
تغییر مهمی که در پدافند ایران رخ داد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/farsna/457525" target="_blank">📅 14:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457524">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس هنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hijZiR2uRGPjrSQ5-JgkBJpGWVV7NK5qydKZgeXINvvFqOPUN_GGtRTy6OOjoe_obEEEMj7LS4QwrS7iET6_hGRQTsW0fEYCRWwr1Jq6VCxMLpin0vztPtsGdWshMz4gTc51O0miwNzg7w7yKfDayctfSXlyBAe3Q6g9_mRHOLGtoETADxcFvy3x2sqQZehxo5Wwu7e58hzC4-DXzZp78CRwQhNek-Pm65Mj2eUdLup-3oWu09rkdubDpeb6fuzqCx5pJSb-qtK4rGvV2ggIxenFaiIcpJ_0R3wygkxAVv_aeQqMS8FdhGx3HwNdAvk9xS10VHVQzuUdqYkCBlKPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود بی‌سروصدای سریال‌های اینستاگرامی به شبکه نمایش خانگی
🔹
میکرودراما یا «سریال‌های کوتاه عمودی» بی‌سروصدا وارد بازار نمایش خانگی ایران شده‌اند؛ قالبی که برای تماشای سریع با تلفن همراه طراحی شده و حالا با فعالیت سکوهایی مانند «سریو» در حال تثبیت جایگاه خود است.
🔹
شبکهٔ نمایش خانگی «سریو» با معرفی خود به‌عنوان «اولین پلتفرم سریال کوتاه عمودی» یا همان میکرودراما در ایران فعالیتش را آغاز کرده است.
🔹
پلتفرمی که تولیداتش با محوریت استفاده در تلفن همراه طراحی شده و قرار است تجربه‌ای متفاوت از تماشای سریال را برای کاربران رقم بزند.
🔹
در معرفی این پلتفرم آمده که «میکرودرامای ایرانی و آرشیو جهانی» برای سرگرمی کاربران، از خانه تا صندلی مترو و اتوبوس، در اختیار آن‌ها قرار می‌گیرد.
🔹
با این حال، «سریو» در سامانهٔ مجوزهای ساترا ثبت نشده است. این پلتفرم اقدام به بارگذاری تولیداتی کرده، اما در زمان بررسی، امکان ورود و تماشای آثار آن برای نگارنده فراهم نشد.
🔗
ادامهٔ خبر را
اینجا
بخوانید
@Farsnart</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457524" target="_blank">📅 14:32 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457523">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uf-YQB6X-ThHb-MZPd2CuAg7tjhEH4QsfkO2MP28W1pmtGkWHyDohLgE-p9gWySYK4O4SmCG8UIxgbXE5SZo9nQkYmfx-bnrg_Ca4_tbBCflHwWQWzzSXpfpFsILfmD3gb8qlXQrV1pXA_Kym9wM-aS9FGIzXidEbtYLE-0Q66PMDFuUeZVhNr-2Sjkk4uSW3mlJzluum1CFylua0Y1A4oaaEssKVNfC0e51MAfdWJAh7_QPUVTlOYAVA0Z2NKOteP6-zqjIkeYntHvBWY2l6pltFirz4v0XXv2ZIrNjKo_3coMpqqKxr3TcXwiZnCHU1caKbiyJ6Gu-PcZPtricGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشف ۴۱ جمجمۀ آهو از چاه آبی در شاهین‌شهر
🔹
فرمانده انتظامی شاهین‌شهر: ۲ شکارچی غیرمجاز که در یک سال گذشته بیش‌از ۵۰ آهو را در مناطق حفاظت‌شده شکار و ۴۱ جمجمه آهو را در چاه آبی مخفی کرده بودند، دستگیر شدند.
🔹
متهمان گوشت آهوها را به‌صورت غیرقانونی می‌فروختند و سر آهوان شاخ‌دار را نیز برای تاکسیدرمی در اختیار افراد سودجو قرار می‌دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457523" target="_blank">📅 14:26 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457522">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d662816f83.mp4?token=sUxJbomaEIVzHwLtv1yKW1NzcXnl7kk2FpF0NaFmqJa_xaloY8HzMq2xF5isd5F1rfCep_GvAxGI_W761IQwFTLFQU2_r7-GTenCC6cG3DJRqCPvqVYW70lygYDV9UI7v0ZVM7i0zJJ6ULTPBxXgRq04SsCoicfw0cjRcl5cDKa1YWfsBweY5eVf-UPCghESSbzyhv2hMqof_ARJ3Y0Ef8sg7fwzkz1h3itQcBbwTglHYOTSGt1RipfIp-lIzk-t1ttNIaltY02NS20U5ZZsWYS0PHIXI3y45TAqAsccywbCcrXrz96GLXJ-HlPWe_x3_WifvaQRkup_D-ax07Agd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d662816f83.mp4?token=sUxJbomaEIVzHwLtv1yKW1NzcXnl7kk2FpF0NaFmqJa_xaloY8HzMq2xF5isd5F1rfCep_GvAxGI_W761IQwFTLFQU2_r7-GTenCC6cG3DJRqCPvqVYW70lygYDV9UI7v0ZVM7i0zJJ6ULTPBxXgRq04SsCoicfw0cjRcl5cDKa1YWfsBweY5eVf-UPCghESSbzyhv2hMqof_ARJ3Y0Ef8sg7fwzkz1h3itQcBbwTglHYOTSGt1RipfIp-lIzk-t1ttNIaltY02NS20U5ZZsWYS0PHIXI3y45TAqAsccywbCcrXrz96GLXJ-HlPWe_x3_WifvaQRkup_D-ax07Agd4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
بازدید رئیس ستادکل نیروهای مسلح از یکی از تاسیساتِ زیرزمینی تولید موشک‌های بالستیک
🔹
سرلشکر عبداللهی در این بازدید در جریان آخرین وضع تولید تسلیحات بومی کشور  قرار گرفت.
🔹
رئیس ستادکل نیروهای مسلح: دشمن باید بداند نمی‌تواند با ارادۀ یک ملت بجنگد.
@Farsna</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farsna/457522" target="_blank">📅 14:11 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457521">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KATuv-GeZuUWryf7Y6Z1NaLecsPIJWpSuh5oVbougszzNGhIbpd27Y1ztWoQNQta3S_Ny6Ygw8ELiw2w7ujU78G85SM5QY6dGv-n3HCx9sfTW6iIplAWj3zEFmxAzUmUx1DK5RoWP11ixyim9Bex8N5Dph6s9bHobKRdcJtF-LuQu37JP6TO8N-Dypl1CshZVj6Y_koHjlpHlafnCbzimWX3RoVX7dq4IoXYUazOI3BxplzFEugkDFU2ORIrKJxSitkTNpj3ishh9NvZ2G9WplDcye-FSowkhX86tT-KioJrbPOan_7ZFQSeFbfnexQC4mow2meVmTciLDC6mxHIoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🖼
روایت قالیباف از بی‌اعتنایی کشورهای منطقه به اظهارات خصمانهٔ ترامپ
🔹
رئیس‌مجلس در واکنش به تهدیدات ترامپ رئیس‌جمهور آمریکا علیه کشورهایی که به همکاری‌های تجاری و اقتصادی با ایران ادامه دهند، نوشت:
🔹
ما پیام‌های متعددی از کشورهای همسایه درباره شکل‌دهی به ترتیبات امنیتی و همکاری‌های اقتصادی جدید در منطقه دریافت کرده‌ایم.
🔹
ایالات متحده امنیت تک‌تک متحدانش را با قلدری و بی‌اعتنایی مطلق به منافع آن‌ها به‌خاطر منافع اسرائیل چنان به خطر انداخت که آن‌ها برای لحظه‌ای، تمام هستی خود را در خطر دیدند.
🔹
یک نظم بومی و مستقل که واقعاً صلح و امنیت را در منطقه به ارمغان خواهد آورد.
@Farsna</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farsna/457521" target="_blank">📅 13:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457520">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9t0SIv3u7kiQ49Lxxyy4sU4s81oykCaMV2Bt9ic3_lJdhN95CRT0-G0tIh_WDPXw5wKZa20mlXR9i7JUEBkbEkkeDtrKQedf1etOOvag8jg1NAecNVxREX8MfngSwCd1oAHevlH2XAyKG6hSwMjQ1D9AJQf-MMbXCxk77zAFozDnD9ZsIp02Qe5nw4W1vDN4TBKtganCVM9g088d2lA5TB_pDfQ2GFRB_TCMggQLYscBom1_EhczIF0g8eCwnV4saSwzgXc030wrVjHExtkF1R7wu82SBJbbdEve3k03e1_mTHpdXXD0BKhYbhC4U_WZzEgV3Ue6ZgepOTAO-uhFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمین‌لرزه‌ای به‌بزرگی ۳.۴ ریشتر در عمق ۱۰ کیلومتری زمین، ایذهٔ خوزستان را لرزاند.
@Farsna</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/farsna/457520" target="_blank">📅 13:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457519">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv1bp96jLrHgm8wfOnRnxOe7Ho1xi0jci-00wT-E1bixsRRubiKqN8F7OaRkh4xadhbx1fPgNSIE3rsccfCwoAXI617J1rfte8vXVe12LD4MFRGxGd8XTlBaTGpSh_Lpmad68pJ2dQTPdjutxh1HvS4GdRsxhHNdbI9-uxh9W_v9khbCnrU5vN6lekkfS2URRqI9hi10c6Btsv5qpD3NxN3youKCsZnT2ebOIGWVyCZRcjFoR67fk6lL-OBSPsOHG6Es5x0L27UBzhufBdBz1y8jguTiL8_799HSFOfdl1EFIjSVq0r6kTGywc_rdBywgRjnmz_JUYlAJjnlC17hPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس سازمان بسیج: نقشهٔ جهانی قدرت درحال تغییر است
🔹
اروپایی‌ها متوجه شده‌اند که از سوی آمریکا تحقیر شده‌اند و در سند امنیت ملی ترامپ نیز به‌وضوح دیده می‌شود که جایگاه اروپا تا چه اندازه تضعیف شده است.
🔹
امروز نقشهٔ جهانی قدرت درحال تغییر است و این‌گونه نیست…</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/farsna/457519" target="_blank">📅 13:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457518">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85c47d6c6a.mp4?token=kH_U6TsEBgaJDpB9RRdZ4EFIEK0QPxLoWGQi7HTJXYtE-uNOVmHibipDAB3knTCIaRhtleXj09g5k-wHLTzgQco_OxfrqPKotrvkoO_abKuLHZlN2Q4J3gphw1XZYMKZrwm53jsWqvWSngIXJi2oyLgTZ1lJS0ZBINu5r9SxjFqezzd6IfsizsQHcUWX_5Up5gMEqMlU6VtzrnZQkgzD9VUu-ZJGbRaUGCAmk0Eyc1XPX4zATGjpqs4G1nchlmjoYW-tMvwag0GpAXq3Xx1UUPUpNflhICPXWr9zhqsqmcoahPvGPmMrw9x99gqcxFXtOBLdC7V3t5zW895WNbqefg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85c47d6c6a.mp4?token=kH_U6TsEBgaJDpB9RRdZ4EFIEK0QPxLoWGQi7HTJXYtE-uNOVmHibipDAB3knTCIaRhtleXj09g5k-wHLTzgQco_OxfrqPKotrvkoO_abKuLHZlN2Q4J3gphw1XZYMKZrwm53jsWqvWSngIXJi2oyLgTZ1lJS0ZBINu5r9SxjFqezzd6IfsizsQHcUWX_5Up5gMEqMlU6VtzrnZQkgzD9VUu-ZJGbRaUGCAmk0Eyc1XPX4zATGjpqs4G1nchlmjoYW-tMvwag0GpAXq3Xx1UUPUpNflhICPXWr9zhqsqmcoahPvGPmMrw9x99gqcxFXtOBLdC7V3t5zW895WNbqefg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با کلاه انتخابات ۲۰۲۸: باز هم برای ریاست‌جمهوری نامزد می‌شوم!
🔹
رئیس‌جمهور آمریکا بار دیگر از تمایلش برای یک دورهٔ دیگری ریاست‌جمهوری برخلاف قانون اساسی آمریکا سخن گفت.
🔹
ترامپ در شام همراه با خبرنگاران با لحنی طنزآمیز گفت: برای اینکه نشان بدهم چقدر…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/457518" target="_blank">📅 13:44 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457517">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMnGs--HGQvbePR8szh5_s8cAj1JI58L6tN3uUpRi02T3CH-WkvPFUUCcILqzpiX4WRMaOIxrd_R8JscRMCJKwuHRhbrnGeU7gMEZ_YKmAXGgsF-kD09XWpfmvB2OJ8wWYC1hUAiTx0Tbku9m4csNgULzeIUrCtHKoAT1oI1oU5xF1HgQ4atn79aLiogtBpmHMm7AEpM_bjbDvcNcupTrm8BOU1mqIpgWTwJUR7efWmyIbvjVRdgQItuSE5X_IIzLdFMbAaHmQZr0h86sei3NVjGsKmIHuPv2Kf6zaujZPEernK-Rm7zypgyKKSlV5LOYe5UrMfF_8TEOKs4oXPzlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: لفاظی‌های ترامپ از سر استیصال است
🔹
رئیس سازمان بسیج: اگر این حرکت را با قدرت دنبال کنیم، باید بدانیم که روند دشمن نیز نزولی است.
🔹
رئیس‌جمهور آمریکا به لفاظی روی آورده است که این لفاظی‌ها براساس ابتکار عمل نیست؛ بلکه از سر استیصال است.
🔹
دشمن ابتکار…</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farsna/457517" target="_blank">📅 13:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457516">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5WAPXp9gCGSrzVr7DwMRL97zgD9Sh-EZSedb0TZwY-f25RZpbq5iDb6c6VTABJn9w9XLaUm4D_TosWlDtCpFyGLhrwrK5Iv13sFNywtaL7yhjjrfrNEf0jP-haR6jFouEdWCPoyk3L-d9WLRbpfwlqN62NFkcz3njukGqpib2IWiaRW6zvGdHJvn4jYYazCd7SnYyP22yQ8KLacx9AEoQIP5B_kCRhP14VdSOJMZIuZiT-Woh82bOQ6pqzjPshb5K7dvOhUYZ15F0Z4n2LmSNIykqRBan7URlQiDI_0MQqnkAkwh0Lm92e-OBjYxzudcrveQbgVkKFyN-zm13efWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طائب: لفاظی‌های ترامپ از سر استیصال است
🔹
رئیس سازمان بسیج: اگر این حرکت را با قدرت دنبال کنیم، باید بدانیم که روند دشمن نیز نزولی است.
🔹
رئیس‌جمهور آمریکا به لفاظی روی آورده است که این لفاظی‌ها براساس ابتکار عمل نیست؛ بلکه از سر استیصال است.
🔹
دشمن ابتکار عمل خود را از دست داده و تلاش می‌کند با روش‌های دیگری شرایط را تغییر دهد.
🔹
براساس نظرسنجی‌هایی که در آمریکا انجام شده، ۷۱ درصد مردم این کشور معتقدند ترامپ در ورود به جنگ با ایران اشتباه کرده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/farsna/457516" target="_blank">📅 13:31 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457515">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تراکتور خواهان تغییر قانون سربازی به‌خاطر بیرانوند
🔹
مدیرعامل تراکتور: بیرانوند سرمایۀ ملی و از چهره‌های پرافتخار فوتبال ایران است. او در سه دوره جام جهانی حضور داشته و برای فوتبال کشورمان افتخارآفرینی کرده ‌و باید مورد حمایت قرار گیرد امّا با این حال، متأسفانه…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farsna/457515" target="_blank">📅 13:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457513">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qsFa_-N5U5C5pjbn96rNmWkWty9bnxYiEIwROq2RllUtqpNXrtn4_oWscJm857FaXrLKhlnpH4zXk2RIaovRU9W-ppwhGaeBRWKh5Rwf-UwpZVARmNCSUIVO9Kgl98MGbYsFC6mFhYHrwT_UluzfFCxk4Byo3sDCLejvQxkv6bA0JXmodMOEfgkeRuayFB3Fb8KRjkF9-Hok1xRIfrd8b_dvlvmUpzYKqL9gnuUq14E6fFryHhO6hWDfFFuKKSszbI-XlM627RW6w4sK_mUQvQUCleQrydTOGnkPtPIrlarUQTBZ0egJkOXHR9xIEaQ4B1e6S5YX3aZ48tn3qbbDBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fYmsGtUT3Mkyf8xay86CVpA8jV0sdUDMe47e36GcIlqr0VhG_qQdTdDCUSU-glefilNsbiBGMeBbiz15HjCOKGyXX_7RsmJQzdQWe3TfluT9wesPqa1lFFxyBd2f94Vrr3UdWqGyMpgClqJ45kx_Yh4ib3z_aASsfwvSJpAVtszPYw5CbzvvFVnndThKXYCDKNyzEME_UhTLvRWhml0hqDZ2V5cHUMkJM8pcIAy2jl1wxj1C2gl3AtSTw9whz9P77XiYPig7zyZ8vJUiQPtzgJplZkMNF2j9rJvgyyBkRcV58PcwfO6DaPPu-_Cx-BNWeN_RotAYkyrritaQCHtjJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پلیس تهران نوزاد ربوده‌شده را پیدا کرد
🔹
در پی وقوع یک کودک‌ربایی در تهران، طفل دوماههٔ ربوده‌شده توسط کارآگاهان ادارهٔ یازدهم پلیس آگاهی تهران شناسایی و پیدا شد.
🔹
پلیس اعلام کرده که مراحل تحویل طفل به خانواده تا ساعتی دیگر انجام می‌شود. @Farsna - Link</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/farsna/457513" target="_blank">📅 13:27 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457512">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyxHAHzWW3qe7EjxA1LMl-brAukmPecoRlOj-LSnBnQ2z35jvDUhOQHlc2A43M5nWDlS2I5OZHhT5zEcRTQWRWsdYcNWc1czX3RVaYEreXmtqmopgVA8TaSMObXy5kyBR7eOpXa_6qAJ7fadWCum30ZrQNeCUwWY5d5dwLgdOOg1P-pMWgEGZKN5lorQdE-C-_C0NpbKfkirYWaavvs4dyabLG2QpxOwy0TzthIvso_we7e6DTAGEfE9yd3Xh6CXPzHX1-Nh4gm1aCr4LuGi3Tqou06wJbOAK2p6BCoKsc06Oh1OU3ARB3C-tbaU3VydAFFN2rRhHCb9FYZNglhRpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ معاون اول قوه‌قضائیه: تغییراتِ دستگاه قضا ادامه دارد
🔹
دادستان انتظامی قضات پس از بررسی گزینه‌های موجود ظرف همین هفته انتخاب می‌شود.
🔹
در دیوان‌عالی کشور نیز تغییراتی مدنظر است که پس از طی تشریفات قانونی اقدام خواهد شد. @Farsna</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farsna/457512" target="_blank">📅 13:12 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457511">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">گل‌گهر هم راه استقلال و تراکتور را رفت
⚽️
پس از استقلال و سپاهان، ظاهرا گل‌گهر سیرجان هم سومین باشگاهی است که نمی‌خواهد پیش از مسابقات باشگاه‌های آسیا، به تیم ملی امید بازیکن بدهد‌.
⚽️
سهیل صحرایی و مهدی گودرزی، دو بازیکنی هستند که تیم امید برای حضور در…</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/farsna/457511" target="_blank">📅 13:02 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457510">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWhe6NH-L6AmIXKp8ISxsr6oVExn4m4Wv3VJFQ4FF2oGI4wPrEEx1LTzXxCd_T-9vrigogzAkvuSu7mY-utec1jTM0jPZ8MMQ7CigEh6jeyjn9VsgnhWh44Z0zO7PWg3tgZGIjx1hrwN2Q-k5YPaJjwQuLoyc-F--ObJbjauJncsxsqAuVfbuOn6y_nih9eVyULMKsRE4Fs6oZVISBdhzqw07ZH5W0VILn27aFpvw0aSgTrbt5gSawDpZLEgbkc9VVgkc6qBQsRqq3H1lgzqIPyVFVR36eCHKgdmOvA7T0XEWU0jYrJq6wAAZrwgs1Es8mbdxLLFnTqIQlckqtKJaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سرمربی استقلال: علیرضا کوشکی به‌‌خاطر حرکت
غیرحرفه‌اش
بعداز تعویض در بازی قبل، فردا مقابل سپاهان نیمکت‌نشین است.
@Farsna</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/farsna/457510" target="_blank">📅 12:57 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457509">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qsgtdHUBCPtLL94jf7AzXGBwiLvE8yse6GVhtcOt4YWMrG1s11uIcNZO9esaFhTqCtqP0pS8Md5wQ7Q6iFmNVLlXU0GwZgHYy0tkFDrqfAvYEYY49vzVbgpycPeXqavV1FzsUL_SBBrsmCtRd99d2ittCLoEyYgWnHiRdp1Z3PmNloT7NhY7BLL8xBM7GfhQ3AEfxRgHSiKG8rsh_cqoSXwGQ16hFbJQLxbi1_Zh6x2gMiXLZ092P69givG1iQrr4Ayn7ngpAeJK8kRms9psa-WnBkdOT4Yx9pn2etfbilp4xQarPazrEjTgY9WY5ojejt03Ec-5ReUKRHoXCMznxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل تراکتور: بازیکنانم را به تیم امید نمی‌دهم
⚽️
باشگاه تراکتور در فصل جاری در لیگ‌برتر، لیگ نخبگان آسیا و جام حذفی حضور دارد و با برنامه‌ای فشرده روبه‌رو است.
⚽️
با حضور مهدی هاشم‌نژاد و امیرحسین حسین‌زاده در تیم امید برای بازی‌های آسیایی ناگویا موافق…</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/farsna/457509" target="_blank">📅 12:50 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-457508">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df76036e2c.mp4?token=GwThio_EaxAdMypN2K7JT4OfppfahR8hkjDdG4T01f7aNV40kxhMtPU-XViVt6kXAWav3B6JopLCLDMz49kDYufguNjCjTAgZK8hGLPdr1paTUWeZTCORGgXhMpk3mjGS2wDXwBKVzoYgpr5lbwffF9EyeY_R7HduaaYZuFi0WS8yx-RFale04c3NcQBLdp9zX4IQdR55T-zzoSQwlAT13KaTGEq2Pgcjdbu5JkeZZM3f1OL_A8XZoMy5uvNLlH0z2WoNUxbKdgRwFMZ2XQmSaL-4Zg4F682eXhCYcJCKtQ1gWxAvX0Puhzgl8GuZTul9oB70cm-m4VlZZgPwn_Nrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df76036e2c.mp4?token=GwThio_EaxAdMypN2K7JT4OfppfahR8hkjDdG4T01f7aNV40kxhMtPU-XViVt6kXAWav3B6JopLCLDMz49kDYufguNjCjTAgZK8hGLPdr1paTUWeZTCORGgXhMpk3mjGS2wDXwBKVzoYgpr5lbwffF9EyeY_R7HduaaYZuFi0WS8yx-RFale04c3NcQBLdp9zX4IQdR55T-zzoSQwlAT13KaTGEq2Pgcjdbu5JkeZZM3f1OL_A8XZoMy5uvNLlH0z2WoNUxbKdgRwFMZ2XQmSaL-4Zg4F682eXhCYcJCKtQ1gWxAvX0Puhzgl8GuZTul9oB70cm-m4VlZZgPwn_Nrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حاجی‌بابایی: وقتی قیمت نفت بالا می‌رود یعنی ما برنده‌ایم
🔹
نایب‌رئیس دوم مجلس: کسی که به هر طریقی فناوری یا اطلاعات در اختیار آمریکا قرار می‌دهد، در واقع با ما می‌جنگد.  @Farsna - Link</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/farsna/457508" target="_blank">📅 12:49 · 31 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
