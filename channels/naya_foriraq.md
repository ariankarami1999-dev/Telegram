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
<img src="https://cdn4.telesco.pe/file/mgwJw33Ft-kxdUStciiuPbVSoaMhWAqfTmJ6Lcrw7KO8d4VsYMV_hyr5QfpqLKW8rFR1kaXmPvQXYdKJGn19BJAR41v6E-JKYGKDb2C49jY4rGFxE93v04EYMqGWMT_tCsAkWW4p0b-QmpIkCg10nMHBIbrX24xcoOkHq4vcqFq1tonSctUb5x9YWcm46RFyFv6yNnhLdNoqgurqSPTJvgU6VIJZXHJNye95dgjypudTHNetaYAPTjBC94IARp7p2HqjaQfC-sPKyGx2nx_iLgIhMdn7sgnWTqSWo3ULh30ZyeSQAROHEMHJVG0rH5Plj6YFszCGrQDjgZxfXuvHqA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 252K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 20:17:37</div>
<hr>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c605ae8ccf.mp4?token=Mq8l_KERObjiaEhfMy32_y6s65FpcIGvldHithLEN1XTu15UuFUHN9lTHrMKQoPBPEQ4xZVfAxmmIW7S7wf9cIicovX3pAezv0Y44WqHwIsiBhSCPRefZWj7OyNg_zn1ovCbk89xtk-rrjCn2C3cj99Q4WvvkhRsmwYpE9fldtk0MbBe2r2SD9rcoynQIOXY7UXCOWl8Rql9J1GR_x0cnkpLLKgiB32kTtoT3azVMCBlEwToi6qd-MbJkk8G-GCGFSlyIllxfO0nnfImliBs86DXqiBxyHEzvZQlQRvUINPhHewOaqK-adm4LJoyUAtssPgd5LN_e7Nfvrn923fppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c605ae8ccf.mp4?token=Mq8l_KERObjiaEhfMy32_y6s65FpcIGvldHithLEN1XTu15UuFUHN9lTHrMKQoPBPEQ4xZVfAxmmIW7S7wf9cIicovX3pAezv0Y44WqHwIsiBhSCPRefZWj7OyNg_zn1ovCbk89xtk-rrjCn2C3cj99Q4WvvkhRsmwYpE9fldtk0MbBe2r2SD9rcoynQIOXY7UXCOWl8Rql9J1GR_x0cnkpLLKgiB32kTtoT3azVMCBlEwToi6qd-MbJkk8G-GCGFSlyIllxfO0nnfImliBs86DXqiBxyHEzvZQlQRvUINPhHewOaqK-adm4LJoyUAtssPgd5LN_e7Nfvrn923fppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">غارة صهيونية على منطقة المساكن في مدينة صور بجنوب لبنان.</div>
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/naya_foriraq/77004" target="_blank">📅 20:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77003">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e4d0cbb1a.mp4?token=IiTcAAtvkkDAabl7jZId8yf_EVVYc8hx-lA9kGjnLiDqJWhJGa7tNV970Bq5dMqQicrhIMmT8C9p19uvyXb5gQ6KOMTeWeaIlythLLSubPhIWvp__HlDfVmSRskHurwFj6SF0FPH5JKZwzg43BujBVnvVU11SqI-d_1rtyNs6QEGTCGARixK8K_5lih8ZN3w5o7y-9qFzU0FgeTEZ0T-ygDAuaSlK2DYIkXwF6QQurUp9uWZO_NayEaVW5yW0M-mWjX9Yf4MmfzyjmJvLGKWLmrlow1LMu1K6jH1FWdBgXM5p0tNIbUFjCw76gc7z17Ry4b4fI1Q3OTE7o0SKZPOFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e4d0cbb1a.mp4?token=IiTcAAtvkkDAabl7jZId8yf_EVVYc8hx-lA9kGjnLiDqJWhJGa7tNV970Bq5dMqQicrhIMmT8C9p19uvyXb5gQ6KOMTeWeaIlythLLSubPhIWvp__HlDfVmSRskHurwFj6SF0FPH5JKZwzg43BujBVnvVU11SqI-d_1rtyNs6QEGTCGARixK8K_5lih8ZN3w5o7y-9qFzU0FgeTEZ0T-ygDAuaSlK2DYIkXwF6QQurUp9uWZO_NayEaVW5yW0M-mWjX9Yf4MmfzyjmJvLGKWLmrlow1LMu1K6jH1FWdBgXM5p0tNIbUFjCw76gc7z17Ry4b4fI1Q3OTE7o0SKZPOFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
جيش الإحتلال التركي ينشئ نقطة عسكرية ومهبط للطيران المروحي على مرتفعات ناحية بادينان في محافظة دهوك شمالي العراق.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/naya_foriraq/77003" target="_blank">📅 19:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edbc444708.mp4?token=JamnYx_XDEkb_hNTxykcDxIaTDvTzLdV6_Dmktr6vOd6bmlnevC85Xr2zq2eX5VLOIGQT7D8CUVP1YixolySqLLjz8yh45pthRB-wycc6GhzM5YJiLExIW0O7YdF3ZgPI_ML9XLXHzmHk2DszyhBClufGpry2DMDBl60C5ZD1sjYfKw_dSN_F6BqgrUsh5rfF5-w4yBWHXUEc65Bn2T44ivh2P5G1r42Jr2QhupBp9-0EJmq_SYBMX51GiMgJsKQcwYmNyizLgrWIaX4DLQiWZ1uKZXiyW8L1zgOPBXnRJmxWHJwzTzZ2E75J10l555M7x1vyLIm0dQhzHGHBk5wrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edbc444708.mp4?token=JamnYx_XDEkb_hNTxykcDxIaTDvTzLdV6_Dmktr6vOd6bmlnevC85Xr2zq2eX5VLOIGQT7D8CUVP1YixolySqLLjz8yh45pthRB-wycc6GhzM5YJiLExIW0O7YdF3ZgPI_ML9XLXHzmHk2DszyhBClufGpry2DMDBl60C5ZD1sjYfKw_dSN_F6BqgrUsh5rfF5-w4yBWHXUEc65Bn2T44ivh2P5G1r42Jr2QhupBp9-0EJmq_SYBMX51GiMgJsKQcwYmNyizLgrWIaX4DLQiWZ1uKZXiyW8L1zgOPBXnRJmxWHJwzTzZ2E75J10l555M7x1vyLIm0dQhzHGHBk5wrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
الله أكبر.. تصاعد اعمدة الدخان من دبابات وآليات جيش الإحتلال في محيط قلعة الشقيف بجنوب لبنان بعد دكها بالصواريخ الموجهة والمسيرات الإنقضاضية من قبل أبناء نصرالله.</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/naya_foriraq/77002" target="_blank">📅 19:16 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/581c1b2139.mp4?token=RpFda6vMiHrpRrZELaGZAso_aYw_qBpzbIHG8eBwnSy9T18LCG7WpOTXf1b-LyEuvlDkHgmIxFVrbiyUEWaK8aWoRk0--dAO0ioBmjfH0hD9j3q5EucGnBIVWTt5TOYEZ5xjKin8n89ls-qMATAe2Z2QLzB3c3QkfcJNF7zDgUGXPelXDPmSnbkARGfILBbF3-TlwfyM_jdKjf-DVbTLFHZ8eL0AQ-MZBqEHuNbjIoH4wsH7n7FwLzRpJhbzzYTqza0kE8tIXNt3EOi1BDrDpIYVNyuMT1a3ZT58G7dsjYKlkvGbxtMcW5ZMJe6UU7_ouBA23puRYLSMRoXOxs0nVKKHqpTfQkyZsSbqkuvYX09VK0LLEyDybtUl7luQG_oGlI9mDQqj9NHDVf_QoJE0fBs2qhJwoYbzajAUQWU4Tx5zQ9ob1DVVWtQ7Usi0AK1R_8YaNeJWxcgOUVp9mhESd5yyCIt2IYrUIc0Fd_ThCYNjlrFI6o1z0YeQKTRGtxIWYQo7pnKQf3D9M9L_-7D-4Fr-PEutPuIE53r6YsDRmdY9pRMZXuIkG2K5iScyqZComsCXVMEqhutkhbIFW827Ib8ZhqHGDsa91pI276ljnGDWPL8QibVi7MqyI08eMTODfTTlM8YwT6IlywPX7ohGRw7UHADEgOv48-L6P4U0-PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/581c1b2139.mp4?token=RpFda6vMiHrpRrZELaGZAso_aYw_qBpzbIHG8eBwnSy9T18LCG7WpOTXf1b-LyEuvlDkHgmIxFVrbiyUEWaK8aWoRk0--dAO0ioBmjfH0hD9j3q5EucGnBIVWTt5TOYEZ5xjKin8n89ls-qMATAe2Z2QLzB3c3QkfcJNF7zDgUGXPelXDPmSnbkARGfILBbF3-TlwfyM_jdKjf-DVbTLFHZ8eL0AQ-MZBqEHuNbjIoH4wsH7n7FwLzRpJhbzzYTqza0kE8tIXNt3EOi1BDrDpIYVNyuMT1a3ZT58G7dsjYKlkvGbxtMcW5ZMJe6UU7_ouBA23puRYLSMRoXOxs0nVKKHqpTfQkyZsSbqkuvYX09VK0LLEyDybtUl7luQG_oGlI9mDQqj9NHDVf_QoJE0fBs2qhJwoYbzajAUQWU4Tx5zQ9ob1DVVWtQ7Usi0AK1R_8YaNeJWxcgOUVp9mhESd5yyCIt2IYrUIc0Fd_ThCYNjlrFI6o1z0YeQKTRGtxIWYQo7pnKQf3D9M9L_-7D-4Fr-PEutPuIE53r6YsDRmdY9pRMZXuIkG2K5iScyqZComsCXVMEqhutkhbIFW827Ib8ZhqHGDsa91pI276ljnGDWPL8QibVi7MqyI08eMTODfTTlM8YwT6IlywPX7ohGRw7UHADEgOv48-L6P4U0-PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الصهيوني في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/naya_foriraq/77001" target="_blank">📅 19:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🌟
🏴‍☠️
إصابة مباشرة لصواريخ حزب الله في وادي الحولة بشمال فلسطين المحتلة واعمدة الدخان تتصاعد.</div>
<div class="tg-footer">👁️ 6.37K · <a href="https://t.me/naya_foriraq/77000" target="_blank">📅 19:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن اصابة 3 جنود - أحدهم في حالة خطيرة، نتيجة لعملية لحزب الله ضد قواته في جنوب لبنان تم إبلاغ العائلات.</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/naya_foriraq/76999" target="_blank">📅 18:23 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAa07NFDK_zXets0Zi6NTfoE47eRNNmyj2RUKZ1q_JDzV6vFlYikoCoP-5CvN67GZRb7bWo1alpQoaPI7gF3UD8Oes4lrzmGOljFK4xhIhTJQyMAkBRkQrF1lkg9Jyw1JIDdJFPmRD3licInbFnYvGAh2UNc3-hw00GDBTHroIfASWlkYfsgTxKLM6-tI_1SP9bIBSRCJn2e98hTSAjGfi9dr0UNg0d_qzTLKub6iNNabGJQOXYnwItCC6cmI-iISc_UEFOsvTDxnP7Rbgq2KNDCYfMuvfsGFgtDvcxwVBbb6F314s3cH3Gq5mf2Dv3Tj2pxCroMhGD8_j4iuL8anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🏴‍☠️
لبيك ياشيخ نعيم.. حزب الله يدك الشمال المحتل برشقات صاروخية وصافرات الرعب تدوي في المطلة ومحيطها.</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/76998" target="_blank">📅 18:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76997">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ec8e09d4.mp4?token=V3uuXuDRdMz4coZTiCnVesHlNvEodPjpDEkx2GtrEIEdgwd0DoYu2GPsBn5M_g205CfwVaRM4iw7PC0jrrVmJLPdlvaFMhaoF0SkR-ZNddf-zoFxlALdioFtWa7Rtd5yW48FdfV3dNod5pcr0hwp3l-CHJoVwIThd2OycPsYI18Wixn0c1IlTwsAHYDjcQS2Ax9cTz7nUtAi2qp5eZETxp_sOAcyOSL6WkNjYXK8BFbR9ICiwj42550vBzPe76y_cVHAYu-neEHQgymyR7jWCN7mqJR7KZV4RXhVLVMcyHx4TGBwWMrIGZTowLvjgjSyod864nvwGxIyNfwsb7FbeXCw3AQ5znwdaSMjMrfSSdaBkzv0Jn81ln1fXm9CBUYz0AsZxFiDoldfod6WmE4AVcgTApi7SU1oKQzip2cgiM5NcTc4EpX8hV7jGlgUAadD2uXCc4TSuBqD7fjVFmoyRyI8UPFM6asIe4QBW4HIZAcYgYsCvtICnK5kThc7hMPeyhryw-7H0gdpTQRSD_-Lx0L75EhaLzpY9eW7HUHEbrmhVeeUsVibdo2OAvqAlUdaUksWcLh6KBuxncHuvgqv0YIvBH4zuFrng3JyLhag7NTdOm91xvjG21fx_E4l8ul-W0h1CJ1Gw3z4eDcEvzAuqr6Hfd39r_h9D3n0stJfYCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ec8e09d4.mp4?token=V3uuXuDRdMz4coZTiCnVesHlNvEodPjpDEkx2GtrEIEdgwd0DoYu2GPsBn5M_g205CfwVaRM4iw7PC0jrrVmJLPdlvaFMhaoF0SkR-ZNddf-zoFxlALdioFtWa7Rtd5yW48FdfV3dNod5pcr0hwp3l-CHJoVwIThd2OycPsYI18Wixn0c1IlTwsAHYDjcQS2Ax9cTz7nUtAi2qp5eZETxp_sOAcyOSL6WkNjYXK8BFbR9ICiwj42550vBzPe76y_cVHAYu-neEHQgymyR7jWCN7mqJR7KZV4RXhVLVMcyHx4TGBwWMrIGZTowLvjgjSyod864nvwGxIyNfwsb7FbeXCw3AQ5znwdaSMjMrfSSdaBkzv0Jn81ln1fXm9CBUYz0AsZxFiDoldfod6WmE4AVcgTApi7SU1oKQzip2cgiM5NcTc4EpX8hV7jGlgUAadD2uXCc4TSuBqD7fjVFmoyRyI8UPFM6asIe4QBW4HIZAcYgYsCvtICnK5kThc7hMPeyhryw-7H0gdpTQRSD_-Lx0L75EhaLzpY9eW7HUHEbrmhVeeUsVibdo2OAvqAlUdaUksWcLh6KBuxncHuvgqv0YIvBH4zuFrng3JyLhag7NTdOm91xvjG21fx_E4l8ul-W0h1CJ1Gw3z4eDcEvzAuqr6Hfd39r_h9D3n0stJfYCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله ينشر:
قبّة الطيور ...
כיפת הציפורים...</div>
<div class="tg-footer">👁️ 7.98K · <a href="https://t.me/naya_foriraq/76997" target="_blank">📅 18:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76996">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f5e868ae6.mp4?token=qMC90F6Nr550QZ3a4tnAx-zhSFl4CjwVYGvFBVHM8HXfu-BrIqkzjt9iaSI-TBumGynt8ZFwfFYeI71neNgBEIiEIF4SsNvLe-_eq1SU9iMnGFQYqCTJ0rdaOOk8Ow99LVbh-Etgey9F15xAYKQ1inkxuUhuTKhsXrk6lk5RCW6jsA369IR-ZJ8YXY0UtX9v_rbPs9arYKn6I_qtjdIH65EqXrdMEO04BngDij5BTsT4fuZtymDW9oITzMvdmme716wcOnQHImx-PnBTkizJC9Mo2Jc1eIg74RdqX8lE4ApDDBbb_PbuNX05HDPwxG7W5F3LYnV-Sqlp9DAmAe3AOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f5e868ae6.mp4?token=qMC90F6Nr550QZ3a4tnAx-zhSFl4CjwVYGvFBVHM8HXfu-BrIqkzjt9iaSI-TBumGynt8ZFwfFYeI71neNgBEIiEIF4SsNvLe-_eq1SU9iMnGFQYqCTJ0rdaOOk8Ow99LVbh-Etgey9F15xAYKQ1inkxuUhuTKhsXrk6lk5RCW6jsA369IR-ZJ8YXY0UtX9v_rbPs9arYKn6I_qtjdIH65EqXrdMEO04BngDij5BTsT4fuZtymDW9oITzMvdmme716wcOnQHImx-PnBTkizJC9Mo2Jc1eIg74RdqX8lE4ApDDBbb_PbuNX05HDPwxG7W5F3LYnV-Sqlp9DAmAe3AOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
لبيك ياشيخ نعيم..
حزب الله يدك الشمال المحتل برشقات صاروخية وصافرات الرعب تدوي في المطلة ومحيطها.</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/naya_foriraq/76996" target="_blank">📅 18:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76995">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف 3 دبابات ميركافا تابعة لجيش الإحتلال الصهيوني في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/76995" target="_blank">📅 18:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76994">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
السيد عبدالملك بدرالدين الحوثي:
نؤكد على جهوزيتنا للتصدي للأعداء بمعونة الله وبالثقة به في أي جولة من جولات التصعيد أو أي تطورات في إطار الوضع الراهن.
نحن على تنسيق تام مع إخوتنا المجاهدين في محور الجهاد والمقاومة والقدس تجاه ما يحدث في لبنان وفلسطين وتجاه الإجراءات الأمريكية الظالمة والعدوانية وما يلزم تجاه ذلك.</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/naya_foriraq/76994" target="_blank">📅 17:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76993">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇨🇳
🇩🇪
الصين تحذر ألمانيا بشأن تايوان:
نأمل أن يتمسك الجانب الألماني بمبدأ "صين واحدة" وأن يمتنع عن استخدام قضية تايوان للتدخل في الشؤون الداخلية للصين.
سيكون هناك بالتأكيد ثمن لتجاوز الخط الأحمر في قضية تايوان.</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/naya_foriraq/76993" target="_blank">📅 17:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇮🇷
🇮🇶
رسالة من الشعب الإيرانية في مدينة الكورة جنوبي البلاد خلال الإحتفال بعيد الغدير الأغر إلى عراق المقاومة والشجاعة.</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/76992" target="_blank">📅 17:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76991">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">⭐️
تقرير الوكالة الدولية للطاقة الذرية:
لم تتلق الوكالة الدولية للطاقة الذرية أي معلومات من إيران بشأن حالة المواد النووية المعلنة أو منشآتها، كما لم تتمكن من الوصول إلى أي من تلك المنشآت لإجراء أنشطة التحقق الميداني، باستثناء محطة بوشهر.
في ضوء استمرار عدم رغبة إيران في معالجة قضايا الضمانات التي لم يتم حلها، فإن لدى الوكالة الدولية للطاقة الذرية مخاوف بالغة بشأن احتمال وجود مواد وأنشطة نووية غير معلنة في إيران.
أن عدم قدرة الوكالة على التحقق من مخزونات اليورانيوم المخصب المعلن عنها سابقاً، لمدة عام تقريباً - وهو أمر متأخر جداً وفقاً لممارسات الضمانات القياسية - يمثل مصدر قلق بشأن انتشار اليورانيوم.</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/76991" target="_blank">📅 17:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76990">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🇮🇷
🇮🇷
الحرس الثوري الإيراني:
لن يتحقق الهدوء في المنطقة دون انسحاب الصهاينة من الأراضي اللبنانية المحتلة.
لا تزال هذه الأرض ترزح تحت وطأة العدوان الوحشي للكيان الصهيوني الغاصب. لم تُجدِ معارضة المؤسسات الدولية ودول العالم وتعبيراتها عن الاستنكار نفعًا في ردع حكام تل أبيب المتعطشين للدماء، ولم تُسفر تدخلات النظام الأمريكي المتعجرف، الذي يدّعي إحلال السلام، إلا عن تفاقم الجريمة والإبادة الجماعية.
يُعوّض الجيش الصهيوني الجبان العاجز، بكل ما يملكه من عتاد، هزائمه على الجبهات بقتل المدنيين وتدمير المنازل والمستشفيات والمدارس. هذا النظام العنصري، رغم الدعم المتواصل من الولايات المتحدة والحكومات الأوروبية طوال تاريخه المخزي، لم يستطع حتى كسب قلوب سكان قرية محتلة، وفنّه هو حكم الأراضي المحروقة، ونشهد يوميًا تدمير منازل الشعبين الفلسطيني واللبناني المظلومين على يد هذا النظام المعتدي.
لن يسمح الشعب اللبناني للنظام الغاصب بتحقيق ما عجز عنه في الحرب بدعم من النظام الأمريكي القاتل للأطفال، وذلك عبر اتفاق مفروض.
كان شرطنا الأساسي لقبول وقف إطلاق النار في الحرب الإقليمية هو وقف إطلاق النار على جميع الجبهات، بما فيها لبنان. يجب على العدو أن يوقف هجماته على الشعب اللبناني فوراً، وأن ينسحب فوراً إلى ما وراء الحدود الدولية بإخلاء الأراضي اللبنانية المحتلة، وأن يعترف بوحدة الأراضي اللبنانية.
إن الشعب اللبناني فخر الأمة الإسلامية ورمز شرف شعوب المنطقة، وسندعمه جميعاً بكل قلوبنا، ولن يتحقق السلام في المنطقة دون الانسحاب من الأراضي اللبنانية المحتلة.</div>
<div class="tg-footer">👁️ 8.54K · <a href="https://t.me/naya_foriraq/76990" target="_blank">📅 17:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76989">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وهذا يعني ان اي مواجهة مستقبلية على غرار حرب رمضان فان المقاومة العراقية المذكورة أعلاه سوف تكون بنفس الوتيرة السابقة ولن تتغير اي معادلة اخرى على المستوى الميداني ،، فلم تكن جبهة لبنان بعد البيجر صادمة وحدها ؛ بل كانت مسيرات الحميداوي والكعبي والولائي والغراوي…</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/naya_foriraq/76989" target="_blank">📅 17:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🌟
🌟
ابو مجاهد العساف المسؤول الامني لكتائب حزب الله: ما يخص فصائل المقاومة الإسلامية الخمسة، بالإضافة إلى كتائب كربلاء، فإنها ستبقى على تماسكها، وستنجز مهامها ما دام هناك احتلال للأرض.</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/naya_foriraq/76988" target="_blank">📅 17:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtQfFVkUXhRjjYd5UfuHtVOxTnJ09i7L0Waj6Wx-kvgh1xEjX6IEpc6Nq6CB4pR6mQVQbMhOlaCDW-g6aB-9CI66pe1aO99PIDtFHR3Wtxor2anEpsfYn0OqBnUJUHxFYMZ22zFaTEltuFLAJwctMQWoWnGRiJ22_U8VoMTBb8R_GuaK51yumLuDK0R-CM1htEYRZ-BmJWoQaHzLWJ88G3tc8ojXWfCL4HEYwcPau_gPpklgRB0oWdri7Yyxg6mF-XzKifpX9hqlt7YFlV3O2LNqXPFK9tiJAKJTNqeR7aH8Wxge7u1fQIwzqjS7aL67Sa5N9sY1hDvzvS2d3H-nEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ابو مجاهد العساف المسؤول الامني لكتائب حزب الله:
ما يخص فصائل المقاومة الإسلامية الخمسة، بالإضافة إلى كتائب كربلاء، فإنها ستبقى على تماسكها، وستنجز مهامها ما دام هناك احتلال للأرض.</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/naya_foriraq/76987" target="_blank">📅 17:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76986">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dgbel5uKSPP6QwJ05WpzX3B2_IwygiG1L424tdDkcgvPd-cu_z0IIc5xRfB4hhaSCp3Jd8PeSVHVkxTCPPyFB4cu2FiyRhYzkbW3BhSDdLf3eiKeFoQp30J_owVOfBy7o1MZEh-njEMf037J2FP8i4UyJoXbPlDaPpo9ddbQMt0ZYOml-He4gEHfWFy-sBrZj1hn97RTT2JPsM0KHeiX8rb8xG1NOyWigpsXexaQrxHamSD79n7lV1Mx1rxnxt1evHbtsoyoYRCF9AZbXEq4xGbw0dzvKcezqFg5yVn4IkMB61z6-zVkAO9nPss3xBu_nSD36Wv6R1h99ImildYmbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
سلطات آل خليفة في البحرين تعتقل عدداً من الأطفال من أبناء الطائفة الشيعية
1.سيد سجاد سيد فاضل الموسوي
2.سيد قاسم سيد ياسين الموسوي
3.سيد محمد سيد ياسين الموسوي
4.سيد حسن سيد ماجد سيد فاخر
5.سيد عباس سيد جعفر
6.سيد حسن سيد حيدر
7.سيد ماجد سيد هادي
8.سيد محمد علي سيد نجيب
9.علي حسين جميل المرزوق
10.محمد علي صالح
11.علي عيسى
12.علي حسين جارالله
13.امين الحواج</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/naya_foriraq/76986" target="_blank">📅 17:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QU8EALQqnNa2oHtYMZW7lTib-sGJg_uxtFuiakHAPH-tBA84CjhDJkRpK7sxhFPJX8dDenAiMw0Y87gvBicRvj_InEV_FZXq2f0d7w8uwBTeV0__m_SxplCqX7CmW2e2r7j3T9mC3Pgx44vZS3qoC5iZ5aKYngxlNC5z4r0x72OGoGO83M1IiVXYUxQQ6mkRm2egU9W1OWLHWMgquZEPqvK0chfhObTB4th3fumV25REZy1qArGyK8Zq_XaCcNiOpPg1r_e9w9XBLxWFMHrcPuPZm0PrbMFIIv7oe5-dSvDRkwp6-y9QkGDgpJ8rlNgZ3GuV6y_2vo1x3f7qyOxzEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
بزشكيان
:
لقد كان الحفاظ على الوحدة والتماسك والتضامن هو الإطار النظري والأساس للحكومة التوافقية.
‏استناداً إلى تعاليم الإمام الأعظم وقائد الثورة الشهيد، وفي ذكرى صعود الإمام إلى السماء، التي تتزامن مع عيد الإمامة والوصاية، نجدد عهدنا مع القائد الأعلى للثورة بحماية وصون هذا الكنز الثمين.</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/naya_foriraq/76985" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e658e4f43.mp4?token=kqOIWeJ4ktGBwJ9pcW_9eYoQp2JZKHA-KdSP9FzqvV1L5hAlXn2wjZY0kpDpV89FtTV40dnvudeHFs22jmTExtS_g76w5zcr09_Npbc7mi8ITubS8lCA5aMBHULQEjb1nmj39r1f1DC3P-40_S_JzJTP5sIOHp7DOLImK7BxPUa2DjMKk10TasYGM76ooyf2QJTk_ZCPDdJtQ_D9mo9fM71xAJRk_Mbc06s7SsVIAKloG_OqbmheG8Xi84yFcsdPm90g834AlTS4FxOfAk16USyVWxHAvcFeNe_u7Cy8s9kQvO6nJXEzDUKQZWoAgxNeC6ajszU2YHg0pCL-135QhJZ0HbAjl2rWSS4PDNLfrZv2fAXFVuIkdAEPqTGzP9PHgNdu27-Ixj7Kzu-Oc0ydImRQ_rrJGti9SXpYtuaP1TNWYythN4OaPC7NUCuA0xy_RGClv69Z81EvKdWlnLvA6MIPczcHcGi_xqqxfysFMJXZM9yltcx6HoMzyW04awEXLCdbhCWWbNoZJW7dMU5o-UodoCk3eK3w3n5pzw95tsIomJONxoy8YtDeOg7NOboAyCFj70mNYJc7z_vMsTwdZZIQhJU-nIfLwGanALLfvtyNrgvqgfqy6ENN-HdoclTJ19ZtNdTD1l6OdK_6dh2Umx4dskogeiq9YIE2T9etDL4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e658e4f43.mp4?token=kqOIWeJ4ktGBwJ9pcW_9eYoQp2JZKHA-KdSP9FzqvV1L5hAlXn2wjZY0kpDpV89FtTV40dnvudeHFs22jmTExtS_g76w5zcr09_Npbc7mi8ITubS8lCA5aMBHULQEjb1nmj39r1f1DC3P-40_S_JzJTP5sIOHp7DOLImK7BxPUa2DjMKk10TasYGM76ooyf2QJTk_ZCPDdJtQ_D9mo9fM71xAJRk_Mbc06s7SsVIAKloG_OqbmheG8Xi84yFcsdPm90g834AlTS4FxOfAk16USyVWxHAvcFeNe_u7Cy8s9kQvO6nJXEzDUKQZWoAgxNeC6ajszU2YHg0pCL-135QhJZ0HbAjl2rWSS4PDNLfrZv2fAXFVuIkdAEPqTGzP9PHgNdu27-Ixj7Kzu-Oc0ydImRQ_rrJGti9SXpYtuaP1TNWYythN4OaPC7NUCuA0xy_RGClv69Z81EvKdWlnLvA6MIPczcHcGi_xqqxfysFMJXZM9yltcx6HoMzyW04awEXLCdbhCWWbNoZJW7dMU5o-UodoCk3eK3w3n5pzw95tsIomJONxoy8YtDeOg7NOboAyCFj70mNYJc7z_vMsTwdZZIQhJU-nIfLwGanALLfvtyNrgvqgfqy6ENN-HdoclTJ19ZtNdTD1l6OdK_6dh2Umx4dskogeiq9YIE2T9etDL4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية
آلية هامر تابعة لجيش
العدو الإسرائيلي
في
محيط بلدة زوطر الشرقيّة
جنوبيّ لبنان
.</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/naya_foriraq/76984" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IF7WHre-C4vjo73kf1w2lvikGNJ6ecuemLUFW1jvgNU8siYxThikOp_-6W8GJEIA_mxSn1ilxr-ekIgXRIDw1xVMF2ssCC7TZxBSUNPF2MXCXq_rskqOY4RW95gabO4N5q6fjhBhjnYzxh3M4miYKwPSYD6g14sbuwYcZBxRkIF2yiaLUqJfn39zY31ArgtlY0oikJz7Au7bw-FQI7xlonDjFEv4Zt61eCChEGdc0BvViWTXnx-rE74jzXgCqkGMmBtQWeuT3vrVTK6VoeVtItkVCx4I39IArfuOehZKtiAzu9oTSewfhVwY4F9g4A4mU2ssuzklxVvRPxLX95I33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
بالتزامن مع زيارة نتنياهو والنائب سوخوت إلى شلومي، أطلق حزب الله صواريخ استهدفت المنطقة بشكل مباشر، ما أدى إلى تفعيل صفارات الإنذار ومغادرة المسؤولين الموقع قبل وقت قصير من القصف.</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/naya_foriraq/76983" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKhUjrzCpKxadJU-mexkOrYsFapdpfheAYR8qotA3Npxjc_3teK5qxb6PL5YjkgP6e2DhwB8nVMhXNchy0l1YwL1N7jqdb4m2ZFX-rnsNFggrRv_KTK-ahQhB6IckCnNbNuDB9blh14FthLlovjIPKwMeByD985jjKGpRy69i5yojucgcTK8XGNvz5caiGeDmHFQO1vwq8jK8wUfXjL_DSbjxTO6TLoU0Yvqz_k3Zf6DwR7wymq4qUyW2olBDci2WlVkGMbj4EZPgtfTlRf6rfUwcnC2EfkirirOfq0jnul4advOlK5muSIU9TclJOAj7csvHRGLklXE0HGpQp1h3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
بالتزامن مع زيارة نتنياهو والنائب سوخوت إلى شلومي، أطلق حزب الله صواريخ استهدفت المنطقة بشكل مباشر، ما أدى إلى تفعيل صفارات الإنذار ومغادرة المسؤولين الموقع قبل وقت قصير من القصف.</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/76982" target="_blank">📅 16:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76981">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🌟
🌟
جيش الاحتلال الاسرائيلي يعلن اصابة 3 جنود - أحدهم في حالة خطيرة، نتيجة لعملية لحزب الله ضد قواته في جنوب لبنان تم إبلاغ العائلات.</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/naya_foriraq/76981" target="_blank">📅 16:52 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qOh4xyk_KpzplPupFb0giY_GbL4oTKpcvR_mQ3ilEIUwoVnJ1up7nDzzX7548dfFworIqLwvMbEC7V3zKsHj5-EqKbea_cY0Uojx5UAw13315QRz6_wmHuXHdCu-Yfe4gQVeXwBq8yRJ4oSmxpqzkobY7SPgixgWq9Yx5xkVAhxzdcLpMov_VYkp6N5NDZCt166_roTnq_L2HMNCgYP0UyL2lJRwwaojM9DBVUEcdqDBQkhIpMlf6gxrf9MPc3WuQRNiaxghakAonkuhCALtmf83CtaHbbj6Ww11uOxgkM0fH_4TBufA5FAxY83rOpTVq80xgHCnRlxfUvvz8aH02w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
اعلام العبري: بعد أقل من ساعة من إعلان الشيخ نعيم قاسم: سلسلة من الإنذارات وعمليات التنصت في الجليل الغربي، بينما كان الأطفال في طريق عودتهم إلى منازلهم من المؤسسات التعليمية.</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/naya_foriraq/76980" target="_blank">📅 16:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🔴
دويلة الكويت تصدر حكماً بالسجن لمدة ثلاث سنوات بحق مواطنة، على خلفية تعاطفها مع القصف الإيراني الذي استهدف قواعد الاحتلال الأميركي.</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/naya_foriraq/76979" target="_blank">📅 16:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76978">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الله اكبر...بعد بيان الشيخ نعيم قاسم حزب الله يطلق رشقة صاروخية مع سرب من المسيرات نحو المستوطنات الشمالية.</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/naya_foriraq/76978" target="_blank">📅 16:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76977">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rx2DPdM6ZWePnrzwK3Uoh1qfHkN4snEPATBC4W1_Ff-yzK0x2vxXxwh9bbeIgbeTbj1bLHTOxsRg_vKUQ4Mp9ETp2ksfW2FjXTvkBfzIZlJnL_NJ_alfYO3kzOscIJyxpawyCC54VylppfUrMj4j8TVe_ttu1IX-6qgjNwCQd-kSduPQ22jzyT-r4sthQBQ2c3S6Ed8gxSzo_dcGH5zvDw51mL4ewtv8FQs3TwdozrdSpWZDnL6w69SfpX0wCbtizrm1_uazRGPG693gmXWixy3a8CPgkvqXPfE_zs6pBwSRBI5zULzvah5KiakNfFr9NihQSNuDVP7o_mUBTB_TPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
الامين العام لحزب الله الشيخ نعيم: الاعلان هو خارطة طريق لإبادة قسم من الشعب اللبناني واستبعاد الباقي. جاءت نتيجة المفاوضات المباشرة العبثية والمذلة والمخزية للبنان، وهي المرفوضة جملة وتفصيلًا من شرائح واسعة من الشعب اللبناني، بإعلان واشنطن الذي يرسم المبادىء…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/naya_foriraq/76977" target="_blank">📅 16:37 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:  بيان حجة الإسلام والمسلمين الأمين العام لحزب الله سماحة الشيخ نعيم قاسم في ذكرى رحيل الإمام الخميني (قدس سره) وحول الأوضاع السياسية:  بسم الله الرحمن الرحيم   الحمد لله الذي أرسل لنا الأنبياء وسيدهم رسول الله محمد(ص) بالهدى ودين الحق، وبعده…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/76976" target="_blank">📅 15:44 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🌟
الشيخ نعيم قاسم:
بيان حجة الإسلام والمسلمين الأمين العام لحزب الله سماحة الشيخ نعيم قاسم في ذكرى رحيل الإمام الخميني (قدس سره) وحول الأوضاع السياسية:
بسم الله الرحمن الرحيم
الحمد لله الذي أرسل لنا الأنبياء وسيدهم رسول الله محمد(ص) بالهدى ودين الحق، وبعده أئمة الهدى المعصومين الطيبين الطاهرين، وتابَعهم الصحابة الأخيار المنتجبين والعلماء الربانيين ليكونوا جميعًا مقياسًا للصلاح والاستقامة وقدوة للبشرية.
أولًا: تحية إجلالٍ وإكبار للإمام الراحل الخميني العظيم، محيي الدين، ومحطم جبروت المستكبرين.
لقد وفق الله تعالى البشرية بقيام نهضة الإمام الخميني(قده) وثورته الربَّانية في إيران، في ظروف كانت تسيطر فيه أميركا على إيران ومقدراتها وتستعمر الكثير من دول العالم وفي منطقتنا، طغيانًا وظلمًا. مقابل سيطرة الاتحاد السوفياتي على جزء آخر من العالم.
هذه الثورة انطلقت من خلفية إلهية إسلامية على مبادىء الحق، والعدالة، والاستقلال، وحرية الاختيار، والوحدة الإسلامية، واحترام الإنسان، ومقاومة الظلم والاحتلال، ودعم المستضعفين في العالم. أقامت نظام الجمهورية الإسلامية الإيرانية باستفتاء شعبي، ووضعت دستورها وقوانينها، وأعلنت بأنَّها لا شرقية ولا غربية.
الإمام الخميني(قده) ومن المنطلق الديني والخيار الفكري والثقافي هو من تجليات الخط الرباني لكلِّ البشرية، لمن أراد أن يختار منهج الحياة الإنسانية المستقيمة والعادلة، ولذا سارعت فئات شعبية كثيرة في العالم إلى تبني قيادته ورؤيته الإيمانية الربانية، وهذا حقٌّ مشروع، خصوصًا بالمقارنة مع خيارات فكرية أخرى أو مادية أو معادية.
لم يترك الغرب ولا الشرق لإيران أن ترتاح في خوض تجربتها السياسية بقيادة الإمام الخميني(قده)، فخاض المستكبرون حربًا ضد إيران لثماني سنوات بواجهة صدام العراق، وبحشد من قوى عالمية وإقليمية لإسقاط نظام الجمهورية الإسلامية الذي واجه الحرب بتضحيات مليونية، والحصار الاقتصادي والدولي، بصمود قيادته وشعبه وحرس ثورته وجيشه وقياداته ونُخبه. ومع كل الصعوبات والتحديات تقدَّمت إيران على جميع الصُّعد، ودعمت حركات التحرُّر وجبهة الحق، وهي لم تتدخل في شؤون أحد. وكانت درّة المواقف النبيلة العظيمة مساندتها للشعب الفلسطيني لتحرير أرضه والقدس، ومساندة حركات المقاومة ضد الاحتلال الإسرائيلي المجرم الذي يشكل خطرًا على كلِّ المنطقة بل كلّ العالم.
الإمام الخميني نموذجٌ للقائد الرباني المدافع عن الحق والكرامة الإنسانية. في المقابل نموذج الطغاة من أميركا وإسرائيل وغيرهما، و الذين أشاعوا الحروب والفوضى والإجرام والإبادة للأطفال والنساء والحرث والنسل على مستوى العالم، وهذه غزة نموذجٌ صارخ أمام مرأى العالم يوميًّا. من نختار للعزة والكرامة الإنسانية والاستقامة؟ لنا الفخر والشكر الذي لا ينقطع لله تعالى أن اقتدينا بالإمام الخميني في منهج حياتنا ودعمنا للاستقامة والحق.
لماذا حاربت أميركا والغرب والأذناب إيران لمدة سبع وأربعين سنة؟ لماذا يحاصرونها؟ لماذا يريدون منعها من امتلاك القوة الدفاعية وهو حق مشروع لكل الدول؟ لماذا يريدون منعها من تخصيب اليورانيوم السلمي المسموح بحسب القانون الدولي؟ الجواب: لا يقبلونها نموذجًا للاستقامة والعدالة والاستقلال، بل تابعة ومسخَّرة لمصالحهم وطغيانهم.
شنت أميركا والكيان الإسرائيلي حربين على إيران، واغتالوا القائد الرباني الإمام الخامنئي(قده) وعدد من القيادات العسكري والسياسية والنووية، وقتلوا المدنيين والأطفال في مدارسهم ودمروا منشآت مدنية .. ظلمًا وعدوانًا واضحًا أمام العالم، لإسقاط النظام والسيطرة على إيران. لكنَّهم لم ينجحوا ولن ينجحوا مع هذا الشعب الخميني العظيم الذي تربى على نهج الحسين والتضحية والفداء، ويتألق إن شاء الله بقيادة الخلف الصالح القائد أية الله مجتبى الخامنئي(دام ظله).
استلهمت المقاومة في لبنان من منهج وفكر الإمام الخميني(قده) لتحرير الأرض من العدو الغاصب في المنطقة، ولكننا نقاتل من أجل أرضنا وشعبنا من خلفية طاعتنا لربنا أن لا نكون عبيدًا لأحد، وأن يعيش أجيالنا حياتهم مستقلين في وطنهم مع أهل بلدهم. هذه المقاومة هي زرع الإمام موسى الصدر(أعاده الله سالمًا) ومسار سيد شهداء الأمة السيد حسن نصر الله(رض)، وهي متحالفة مع قوى سياسية ومن فئات مختلفة تؤمن بالمقاومة وتقدم التضحيات في سبيلها.
ثانيًا: في ذكرى رحيل الإمام الخميني(قده) ، الذي يُصادف عيد الغدير وولاية أمير المؤمنين علي(ع) رائد العدالة ونصرة الحق، نستعرض أوضاعنا السياسية المتأئرة بهذه المناسبات الجليلة، تثبيتًا لنهج الأصالة والحق.
الشكر لإيران أنها تساعدنا لاستعادة أرضنا وحقنا في مواجهة العدوان الإسرائيلي الأميركي رغم مواجهاتها الكبرى. وتتصدى لتثبيت وقف العدوان وإطلاق النار الشامل في لبنان كجزء من وقف العدوان على إيران.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/76975" target="_blank">📅 15:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بيان_قائد_الثورة_الإسلامية_بمناسبة_عيد_الغدير،_والذكرى_السابعة_والثلاثين.pdf</div>
  <div class="tg-doc-extra">1.9 MB</div>
</div>
<a href="https://t.me/naya_foriraq/76974" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🇮🇷
بيان قائد الثورة الإسلامية، آیة الله السيد مجتبى الخامنئي، بمناسبة عيد الغدير، والذكرى السابعة والثلاثين لرحيل الإمام الخميني (قده)، وذكرى بدء قيادة الإمام الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/76974" target="_blank">📅 15:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76973">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5xVi4ZaHLQa443ADaFjXyNLn9lrWP_AdjoTpuGvF1ZPjMGu9Qhpym-jfJ4KO5sffK5GPw_-HeIO9dPeMuWHxsT6I773FiI1B87Hwe6Gqg_3i6Z_2dbbE-x1NWokv7MTkvR-TAiWNkF-UQnkX5TbrCF2DCXxT38vEHtPtyZFoLp-WQ2NV2UFTUjZWocBbGSXQ7UqjN7RyWC8HldkZVxjB48M630qT77h1vF3uU_hbk4VQtr8ZgkWp2wDj5AGRYSzvZ-QjdiR3H_03-AC1YzqoLaLEVsidjWzIvmNZOiS7ujKCBCsZGOWCt6HJN0NbKGSMKbqGxAB2sppG0gZ73a4sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
ترمب
:مجلس النواب صوت، بدعم جميع الديمقراطين وأربعة جمهورين، لتقييد صلاحياته العسكرية في وقت يقول إنه يقترب من إنهاء الحرب مع إيران، معتبراً الخطوة “غير وطنية” ومتهماً خصومه بالسعي لإفشال نجاحاته السياسية.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/76973" target="_blank">📅 14:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76972">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11fe7d926a.mp4?token=aHrbZrhtXwG6g44pwXIV7_oyYvS6Ct3Qjng0SHPHZmZQ1LG29Pa41l2LLJ7dwFEZFJxb9MN-gtTIcpTI6fe6FG96FrnjNLlOqgiZoLEKpLxSwqGRI2ya29zL0VY127Cg6dl_EHqvwc6izk1Evfp3eqGsOyZySWyf_3bun-Pfjxh4w7nDwJnUFYu98_W7raW7CoVDHdV1jV677WzIBR07HDwP3Po-lDa-QYRcJW9UF7NnJ4vrnFQdBRyuGd9tvTflai9ypsgan-CDcmMKN7LTrgSusj02cAFA0m0jI5zizOI9VWtEqP2cm0pTcDMQbxBt6WHQYxmANlUPZP6w2KztL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11fe7d926a.mp4?token=aHrbZrhtXwG6g44pwXIV7_oyYvS6Ct3Qjng0SHPHZmZQ1LG29Pa41l2LLJ7dwFEZFJxb9MN-gtTIcpTI6fe6FG96FrnjNLlOqgiZoLEKpLxSwqGRI2ya29zL0VY127Cg6dl_EHqvwc6izk1Evfp3eqGsOyZySWyf_3bun-Pfjxh4w7nDwJnUFYu98_W7raW7CoVDHdV1jV677WzIBR07HDwP3Po-lDa-QYRcJW9UF7NnJ4vrnFQdBRyuGd9tvTflai9ypsgan-CDcmMKN7LTrgSusj02cAFA0m0jI5zizOI9VWtEqP2cm0pTcDMQbxBt6WHQYxmANlUPZP6w2KztL4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 30-05-2026
تجهيزات فنيّة تابعة لجيش العدو
الإسرائيلي في بلدة رشاف جنوبي لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/76972" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76970">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vFrOhG0YTB8dWduq7CnaABp1AZE_u5ORzQZbJxZCVd5w8mOlRdaRG5RhsDq0886Nqeb_T_5VoduS8inHkkgQ_Q6sgLtMvlbwQc8VV3SlEvHiM0DXCEevfkBJsWEp2aATc-Yvgcf5-p6K0YfOPBgFPbgQrk1f8nSxW1k-vZUXlkZqOjP1DG0N7MFpewvQi5jU1c7spK6lqRuEKJ7oLiz0EE5BdhzNkheS9YOaiOY50rqZmZPb-LOOdMM9M4QChNuYPCu0nibGDyxZ7JBFtOpDs5TwlKVbyN-5Svz2jei1FcdFOqFI44tBKbnkW8ocPQopQ2EoM3nk_Pt37J-w58EgoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
قائد فيلق القدس التابع للحرس الثوري الإيراني:
دعم المقاومة في لبنان واجبٌ علينا جميعًا، وإخراج إسرائيل من المنطقة هدفٌ قابلٌ للتحقيق للمسلمين. جوهر مطالب المقاومة هو انسحاب النظام الغاصب إلى ما قبل بدء حرب الأربعين يومًا. سيجني المجاهدون اللبنانيون قريبًا ثمار مقاومتهم الباسلة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/76970" target="_blank">📅 13:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76969">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVWPkiNOID_Sbjmw5ZfSRpitQ5irRiurcMZzRXkGW9037PRzMPB5ZmCVDdZjMONF4r2RkaQuX3IdKOXRjkpu2NRan8r_DRER6m0qx-QyTJawfSGvLb2x860ix2rqTL3j-t8fE3qFl3m5hWpLnTuKRXBbx7NHW88PYORiX-pCZOHZfPUN-7-BsrKeCQw3FgAxIZmPsiYdkKNVs1yG4arZ5_FRdxwQleqBO75aGF0jF1DKFBs_biJctPbY1h_IgeXuBAqqs2EEwhlkQvNMKJUpSYAvrUEExRdjn10gcWw_cUjOX7LfduJkjQem-DiuXylb5IX5cp2G3-HItCl201mHQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/76969" target="_blank">📅 13:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76968">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd8d0ac34d.mp4?token=lVSmSGhTBG0DEUKIuRlpDBziLXsM1Gsf-iv3AuCReofombBpbP35JizdlmDRPnIMfejoZGKmxW1ULswkgbP20VbU4Vo6oJSma58PXEQ8LT9TxNq8PwrMTCDmFC64eJ1giSvbzZYvZ6qtmCrfzgXYvB4u89-vMpf8olA5pbnbmix0LpsR0ta0Yib_U6XLtc8NSYrCP8sMGwPH_9242TI20-5maFqTURQETZli5m1TuQbhqSL0U6krdE2LJpEEfcz9EUGoD3nU7unY2TcBCQxNQzrIZXW-tL_HPP9eGs1AhGd-w1ghzJ6MYCzHjRwKZDUk5u6-nomDoZd_JbVmxpUn6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd8d0ac34d.mp4?token=lVSmSGhTBG0DEUKIuRlpDBziLXsM1Gsf-iv3AuCReofombBpbP35JizdlmDRPnIMfejoZGKmxW1ULswkgbP20VbU4Vo6oJSma58PXEQ8LT9TxNq8PwrMTCDmFC64eJ1giSvbzZYvZ6qtmCrfzgXYvB4u89-vMpf8olA5pbnbmix0LpsR0ta0Yib_U6XLtc8NSYrCP8sMGwPH_9242TI20-5maFqTURQETZli5m1TuQbhqSL0U6krdE2LJpEEfcz9EUGoD3nU7unY2TcBCQxNQzrIZXW-tL_HPP9eGs1AhGd-w1ghzJ6MYCzHjRwKZDUk5u6-nomDoZd_JbVmxpUn6zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد حديثة توثق لحظة العدوان الامريكي الذي استهدف جسر B1 في الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/76968" target="_blank">📅 13:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DEVKpe8jSdCUpm3e2tXSami6CGi2wtf56J1GWRxQHL9juYtyLemJTq3d4D2OV7dW7t1QQfwQP8KMqwQNIvsN5rCUSgv7wYPOB3mpQ4GJnII0MGhj6uvEosvUmxcR7r87Yqzf9UHvVc6aAe2Cwtdbh3na591aOs3IzskPEHYjjSVJtruSdO0nnZgvn2wHcMYQX35JqU0BIhr3IyghOCJMPMarHDbNzD9hQcIxPGE9mzQl4AlpdS3bVUotjW0_o0-AlnmHF0KvN0T0HxcCndXITbIZju-DR7fHIBNQcBIVq0urFSyQ4FKTwgwGNVpVmJIOw8V0Jlh8KrlZHC7RHuEp0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقتل جندي أمريكي في قاعدة الحرير اربيل</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/76967" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 31-05-2026 تجمّعات لآليات وجنود جيش العدو الإسرائيلي في بلدات القنطرة والطيبة وفي محيط قلعة الشقيف التاريخيّة جنوبيّ لبنان بصلياتٍ صاروخي</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/76966" target="_blank">📅 12:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">‏اعلام خليجي عن مصادر: الاتفاق حول الإفراج عن الأموال الإيرانية المجمدة بمراحله النهائية</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76965" target="_blank">📅 12:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇱🇧
اليونيفيل: وفاة جندي وجرح اثنين إثر سقوط قذائف على موقعنا قرب مرجعيون جنوبي لبنان</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/76964" target="_blank">📅 11:40 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76963">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 02-06-2026 آلية نميرا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76963" target="_blank">📅 11:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76962">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ctLzCShIqKa6wMMvn3_w8-n1WdYvjHnVtUvj3-1Z5FfDvTGI438gHQxqVCsH4v9cyiM1jVK48m3XtFjaMo39NiL78t6TDsTISY_BhlXIJDMEHPkuVI3Sm3ft_NeQ-hajbLvWMAvqBYYBggkMiQwkuKyJwvL84hFlw9-CwPMGHLO1Y8_1LqUKMjpk0Uy_7tYuK5pF3Mvs9pRkTxmbCXu2O5higkvoXN4xilTrHvQ3N9imvvcZE2YtzLljUVr9Y5jIuH_asXiqArucKZ-bRYSp5QCrpjziKYyIv_Z0kMOWyAmdvYCDwWmp-qFhgugUgIfm4mbz5fYRPmXT2clYL7LHDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇺🇸
نظرة من صور الأقمار الصناعية
على الأضرار المدمرة الناجمة عن هجمات الفصائل العراقية البطلة من معسكر فكتوريا التابع للجيش الأمريكي في العراق قرب مطار بغداد الدولي ؛ وقعت الهجمات في مارسو أبريل 2026 بواسطة مختلفة الأسلحة ..</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76962" target="_blank">📅 11:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76961">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سرايا السلام تسلم ملفها إلى القوات الأمنية في مقر قيادة عمليات سامراء المقدسة</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/76961" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6b338b2a.mp4?token=uLAZByPlMoIXMHS9K_VlTr2X5MHwfUaZL6HevdHRdPEPuwAa03Ft5hd3fSnpiKKbtftxGEfQzijN-CXhzwJt2HWa0x7q_hF_b2zltD_ik5W-20-OSPqGuXi5uSTa5tpHtce_1Z2z3dvb8_CSqkABjvJoptYNmcYIju_iFjtodwSHLQyIBfRdcRQN2ikjRP2stm8au5Eq1b_pCKd3CLFJKo3Hglmr6vcZkyoduAns7LmfkRRM0v1v1ZY8478YyUpjxS9lHPqrlysnKHkKg4wnL1SlDUF68jL7jFsOshoWcsE1PbgT7AAPC69ONsdzxrGNzuvqhoT2rnYy5i5gbcfhnTP3AG2OlIGbZHh1_xc3288hDs5BK9EWhFWdGi6jcKYApyOB2RUlqW3-iDrXl5RxTBCcYSfuRdoNiuGbX--DQULigpWF2agEpLdLa01AljmnVxd8G0oYGjUCTQWy8aJcMaxrFwIbLxDkV1twYJ4ff9eBuNB6qokASUsItUOB8354NmU3TuxMlPPK4CG7bDxP0PxCnTo189XRqUlbkobIREMRl8irKUlys7ppmAIIpCDsFqvG4cY5qwUq21d63EKJbtbYSpFGzMfep7hCgARUUxt_wRqHCiG8oYvs9dEUtsuK2Q4_m2iftynSPGeKac5mnwWqvx0BIVUDMPLocADrZ-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6b338b2a.mp4?token=uLAZByPlMoIXMHS9K_VlTr2X5MHwfUaZL6HevdHRdPEPuwAa03Ft5hd3fSnpiKKbtftxGEfQzijN-CXhzwJt2HWa0x7q_hF_b2zltD_ik5W-20-OSPqGuXi5uSTa5tpHtce_1Z2z3dvb8_CSqkABjvJoptYNmcYIju_iFjtodwSHLQyIBfRdcRQN2ikjRP2stm8au5Eq1b_pCKd3CLFJKo3Hglmr6vcZkyoduAns7LmfkRRM0v1v1ZY8478YyUpjxS9lHPqrlysnKHkKg4wnL1SlDUF68jL7jFsOshoWcsE1PbgT7AAPC69ONsdzxrGNzuvqhoT2rnYy5i5gbcfhnTP3AG2OlIGbZHh1_xc3288hDs5BK9EWhFWdGi6jcKYApyOB2RUlqW3-iDrXl5RxTBCcYSfuRdoNiuGbX--DQULigpWF2agEpLdLa01AljmnVxd8G0oYGjUCTQWy8aJcMaxrFwIbLxDkV1twYJ4ff9eBuNB6qokASUsItUOB8354NmU3TuxMlPPK4CG7bDxP0PxCnTo189XRqUlbkobIREMRl8irKUlys7ppmAIIpCDsFqvG4cY5qwUq21d63EKJbtbYSpFGzMfep7hCgARUUxt_wRqHCiG8oYvs9dEUtsuK2Q4_m2iftynSPGeKac5mnwWqvx0BIVUDMPLocADrZ-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الضريح المقدس لمؤسس الثورة الإسلامية الإمام الخميني قدس سره خلال مراسم إحياء ذكرى رحيله.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76959" target="_blank">📅 10:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/76958" target="_blank">📅 10:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f58636b4.mp4?token=HsJ7s-ZEY6Uu-sbGsrzQuslIi20zsvs69luLMdLUAHU-L1E5sPfgdvYm9LqkBROIWOZlRxZrhdOFibB2ICk_IXsjJAx0uGleoeKYcaQSY0YYdjaayWI-Ht5X5D_d5Jcqn5iRJ6Xec5hAbY3KH5hc_HrES6NYXwfz2ZW2ZX1ohqpA5swdl_Cala4OS4qumMCnCzsIGK_vJhSGDMa1S-11Ac2rPIcZlzK6DWC4JGUBJHo9UDR_802Ss9JGfAGhpfkCdvt8sm19SB0JzevkkoRGrz7sGGtncUY5-0QNlukxiR_9vNhqTkSlIzxeTQ7GwhzHrPKYQUevy9bXznpzSsEvsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f58636b4.mp4?token=HsJ7s-ZEY6Uu-sbGsrzQuslIi20zsvs69luLMdLUAHU-L1E5sPfgdvYm9LqkBROIWOZlRxZrhdOFibB2ICk_IXsjJAx0uGleoeKYcaQSY0YYdjaayWI-Ht5X5D_d5Jcqn5iRJ6Xec5hAbY3KH5hc_HrES6NYXwfz2ZW2ZX1ohqpA5swdl_Cala4OS4qumMCnCzsIGK_vJhSGDMa1S-11Ac2rPIcZlzK6DWC4JGUBJHo9UDR_802Ss9JGfAGhpfkCdvt8sm19SB0JzevkkoRGrz7sGGtncUY5-0QNlukxiR_9vNhqTkSlIzxeTQ7GwhzHrPKYQUevy9bXznpzSsEvsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
انفجار مركبة على الطريق 20 بين حولون وتل أبيب مقتل صهيوني وإصابات عديدة كحصيلة أولية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/76957" target="_blank">📅 10:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76956">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🏴‍☠️
إعلام العدو: منذ إعلان وقف إطلاق النار، أطلق حزب الله 6 صواريخ باتجاه قواتنا العاملة في جنوب لبنان.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/76956" target="_blank">📅 09:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76955">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏴‍☠️
‏وزير الدفاع الإسرائيلي: الواقع الذي فرضناه بلبنان يقود لاتفاق يحقق أمن سكان الشمال لأول مرة منذ 50 عاماً</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/76955" target="_blank">📅 09:17 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">قناة CBS: مقتل شخص وإصابة 3 آخرين نتيجة إطلاق نار أثناء حفل تخرج مدرسي في مدينة فيرفيلد الأمريكية</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/naya_foriraq/76954" target="_blank">📅 09:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hza0GGNipamKx4cG4TW1SPHDnXtpsANNKQpPaPFUqpyKEgIDGU_HJd0nZNkkLO4LOE_xlBAxcFn6JPVg6ZFa8I7M6PFrM_YXjN7srtMa4_G30eUc4YqYIMI_ptosLVVYUPjtWr5WTFN6BR6Z3CswlUaHO5AIl_gZGzMBV8EhfgFcQgXfJGxrFMrDa-oZDM5jS2xu5J8p2dhGqKKzpK5xFelbBAEb3DRbhCpCf5lg9myrDoCIa2moPLaZ0L9BWYN8RFYRV8zfgjvScZc5WHD3dzOofUyrdZcJNuHTGRWZMJF4aLBOBCvZu2-Do8yurdkbuDtJrsSX9wa-azD2NHqlPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب:
الديمقراطيون يعودون إلى حيلهم! إنهم يحاولون سرقة انتخابات حاكم ولاية كاليفورنيا التمهيدية، وانتخابات عمدة لوس أنجلوس التمهيدية، من مرشحين جمهوريين عظيمين.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76953" target="_blank">📅 09:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E5wutwa-8wJFd8_8bUXF6BiaccMlljvjDoYPNIlhr3tz9CiZX04lKViZh1biZ9nevpu-uPlXipNI20M6KET3ab4VOeHfjn0kLTiOMJnag2tZdvqyWn_AD51V6sHgblqytitiBjFWKZgk3QKCbmZdyEo7etZ1Q4hAAlN5Qmik7YBbYZtmYDLSBvYY8yJk-jJrx0QzG29ehbawPGCloYVvqCaU3QESHe55VY2uGRO761l873ledkhSwBprt8jmNHnJG8SKPVHtfv-SuZU4vw300kxU0tBvW35JPTCzzCnB09-tGQU4UnRFeYAkPxmXDKYICsRbAF20r0xncWR-MJtSJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وفاة المرجع الديني آية الله العظمى الشيخ محمد إسحاق الفياض بعد تدهور حالته الصحية.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76952" target="_blank">📅 09:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKAzet_dsWkOQ1iEcSvQfsXXzCtnHx4geswmfqh8wagLXI1XDZ_sS-_Q0-UupEysFM3S92hX15oXmmGKONVlDFqhJN2_uCv2wW2betJpm4Lc0V7uil_YREV-lCjHCisE6n59m-9g_OgcG731Kapnpflg6_MpFYfRG1nQDq-KYDUBfktGkMRE6FTgN38RKi_sDjNYnElTlGNX6R24X1bBXaOOObGzJwOwrEkMxwK4mCPhgMMlUbqKhfS9e7h6tqfYEhgPYum1sfYDqCMSCfc0YUXVumOELH6VV4uqqJ7zH4Tq7Cj7iDsY0J5I9eX7_oc2Ec7coDNp45aTRz2VTAKlXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
رئيس المكتب السياسي لمنظمة بدر يقدّم قراءة مهمة للواقع العراقي:
على الولايات المتحدة أن تفهم أن نزع السلاح يجب أن يقابله نزع المخاطر.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/76951" target="_blank">📅 03:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76950">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🌟
🌟
🌟
البيان المشترك بين الولايات المتحدة ولبنان والكيان الصهيوني
:
عقدت الولايات المتحدة الاجتماع الثلاثي رفيع المستوى الرابع بين ممثلين إسرائيليين ولبنانيين يومي 2 و3 يونيو/حزيران 2026.
ونتيجةً للمفاوضات التي قادتها الولايات المتحدة، اتفقت إسرائيل ولبنان على تنفيذ وقف إطلاق النار. ويشترط وقف إطلاق النار وقفًا تامًا لإطلاق النار من قبل حزب الله وإجلاء جميع عناصر الحزب من قطاع الليطاني الجنوبي.
واتفق الجانبان، بتوجيه من الولايات المتحدة، على الإسراع في إنشاء مناطق تجريبية تسيطر فيها القوات المسلحة اللبنانية سيطرةً كاملةً على المنطقة، مانعةً بذلك دخول أي جهات فاعلة غير حكومية.
ستُمكّن هذه الخطوات من إحراز تقدم نحو اتفاق شامل للسلام والأمن.
وأكدت جميع الدول مجددًا أن مستقبل العلاقة بين إسرائيل ولبنان يجب أن يُقرر من قبل الحكومتين السياديتين. ورفضت أي محاولة، من أي دولة أو جهة فاعلة غير حكومية، لاحتجاز مستقبل لبنان رهينةً.  أكدت إسرائيل ولبنان مجددًا عدم وجود أي نية عدائية بينهما، والتزمتا بمواصلة المفاوضات المباشرة لبناء الثقة، وحل جميع القضايا العالقة، والعمل على التوصل إلى اتفاق شامل بين البلدين.
ناقش الوفدان إطارًا أمنيًا، استنادًا إلى المناقشات التي جرت في البنتاغون في 29 مايو/أيار، يهدف إلى ضمان سيادة لبنان وإسرائيل وأمنهما وسلامة أراضيهما بشكل مستدام. ويشمل ذلك تفكيك الجماعات المسلحة غير الحكومية، ومنع عودتها للظهور.
أدانت جميع الأطراف هجمات إيران على دول المنطقة، والأنشطة المستمرة التي تقوض الاستقرار في جميع أنحاء الشرق الأوسط، سواء من خلال دعم الوكلاء أو أي أعمال عدوانية أخرى.
جددت الولايات المتحدة دعمها المستمر للحكومتين لممارسة سيادتهما. وأكدت مجددًا أن أي اتفاق لوقف الأعمال العدائية يجب أن يتم التوصل إليه مباشرة بين الحكومتين، بوساطة أمريكية، وليس عبر أي مسار منفصل. وشددت الولايات المتحدة على عزمها دعم القوات المسلحة اللبنانية، بهدف تحسين قدراتها وتمكينها من ممارسة السيادة بشكل فعال في جميع أنحاء الأراضي اللبنانية.  أكدت إسرائيل على تصريح وزير الخارجية روبيو الصادر في 2 يونيو/حزيران، والذي أكد فيه أن حزب الله ليس عدوًا لإسرائيل وأمريكا فحسب، بل هو عدو للبنان أيضًا.
وأكدت إسرائيل مجددًا أن أمنها واحترام وحدة أراضيها لا يمكن تحقيقهما إلا من خلال نزع سلاح حزب الله وتفكيك بنيته التحتية في جميع أنحاء لبنان. وشددت على أهمية المفاوضات المباشرة بقيادة الولايات المتحدة لحل جميع القضايا العالقة وتحقيق سلام وأمن دائمين.
وأكد لبنان مجددًا على ضرورة الاحترام المتبادل للحدود المعترف بها دوليًا، والحاجة المُلحة إلى التنفيذ الكامل لوقف إطلاق النار، مع التأكيد على مبادئ وحدة الأراضي وسيادة الدولة الكاملة. والتزم لبنان، بدعم من الولايات المتحدة، بتعزيز قدرات القوات المسلحة اللبنانية لفرض سيطرة فعالة على جميع أنحاء البلاد.
واتفق الطرفان على استئناف المسارين السياسي والأمني ​​خلال الأسبوع الذي يبدأ في 22 يونيو/حزيران، بهدف التوصل إلى اتفاق شامل. ووافقت الولايات المتحدة على مواصلة تسهيل التواصل بين الطرفين خلال هذه الفترة.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/76950" target="_blank">📅 02:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76949">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7c8f003d5.mp4?token=rDf2rZmF3zI2OCxR3ll_xtGHEpMGOqoc_lv__ePd18E7pyywt8PP6lqPrJoPeSo2712YW1Y7GVbTkghmSU4xR3RDGDtcQMzMMdA3h8ZzcH1YA4VuWTgXs5IJ6zjnivpVcPjTyojRdkKo1pzmF_-Y8npxxTfUngpkDCFkn0Pf89LbRrAxJ3vGtC7iB57jM62Qx3pJKMAYiutr1ZBgEWiRx_JQHxKj88_LT3ksvTxUUu2eusbY5oJcaGmIhlcKkQyQa_h-QbbdfdnhI_HN4RZ1RC2-a3s-hLRCxGMvayqtp9_wYLSBwBhSwb5aqIREI7t6MBu9nWX4JWJKJ_4fjrgueQ1emqfO-tkndj7vE1NAdxsVx58hxOWaBDEx_PB0UmvhZs2-jbpzNJuA7m9T6q7EWcaBa1kl693Xi8Kj8WAIV39vIOQRQHZrmpNo7vDW-qsPBKXGqKoJ4jpKeloYhIRzBwIrmHBgZmeO-n97vQj8bDNJyUoayOPD3pFW4mA40mS7v0NolfIKqA77Q9i9FGK4mxe5wl91dS-7Ufm3CdibHBuOKsoPQDxuSMcgbppaeRNN12O7H3WbHeJXO37rZX8xrlATYDFGn4SkVbrJmDEjRAtAom5dpjw-PvW5Ukd1D7jP1mumKRPOuRkVq8PXmv1hX7NZY03W8cx1NGdIBve53UI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7c8f003d5.mp4?token=rDf2rZmF3zI2OCxR3ll_xtGHEpMGOqoc_lv__ePd18E7pyywt8PP6lqPrJoPeSo2712YW1Y7GVbTkghmSU4xR3RDGDtcQMzMMdA3h8ZzcH1YA4VuWTgXs5IJ6zjnivpVcPjTyojRdkKo1pzmF_-Y8npxxTfUngpkDCFkn0Pf89LbRrAxJ3vGtC7iB57jM62Qx3pJKMAYiutr1ZBgEWiRx_JQHxKj88_LT3ksvTxUUu2eusbY5oJcaGmIhlcKkQyQa_h-QbbdfdnhI_HN4RZ1RC2-a3s-hLRCxGMvayqtp9_wYLSBwBhSwb5aqIREI7t6MBu9nWX4JWJKJ_4fjrgueQ1emqfO-tkndj7vE1NAdxsVx58hxOWaBDEx_PB0UmvhZs2-jbpzNJuA7m9T6q7EWcaBa1kl693Xi8Kj8WAIV39vIOQRQHZrmpNo7vDW-qsPBKXGqKoJ4jpKeloYhIRzBwIrmHBgZmeO-n97vQj8bDNJyUoayOPD3pFW4mA40mS7v0NolfIKqA77Q9i9FGK4mxe5wl91dS-7Ufm3CdibHBuOKsoPQDxuSMcgbppaeRNN12O7H3WbHeJXO37rZX8xrlATYDFGn4SkVbrJmDEjRAtAom5dpjw-PvW5Ukd1D7jP1mumKRPOuRkVq8PXmv1hX7NZY03W8cx1NGdIBve53UI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏الكويت تبث مشاهد للحظة القصف المركب الذي استهدف مطار الكويت واسفر عن اضرار جسيمة</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/naya_foriraq/76949" target="_blank">📅 01:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76948">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دولة الاخ المناضل كيم جونغ اون في كوريا الشمالية تعقد اجتماعًا هامًا لتعزيز ترسانتها النووية .</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/76948" target="_blank">📅 00:48 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وكالة رويترز: الولايات المتحدة ستخفض قدراتها التي تساهم بها في القوات الدائمة لحلف الناتو، والتي تشمل الطائرات المقاتلة، وناقلات الوقود، والأصول البحرية، والطائرات المسيّرة. دول الناتو تلقت تحذيرات بأن التخفيضات قادمة لا محالة.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/76947" target="_blank">📅 00:28 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ ترامب: إذا نجح الاتفاق مع إيران، فربما يستطيع الناس البدء في بناء الشقق والمباني المكتبية في إيران.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/76946" target="_blank">📅 00:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b1w2d57tE5IzwWp_CJkR5mFdgvcSDJr8to6rgMNbye2cnzL0jRqfOtZo7FJAl_NNgCPLaapwjvtaw4C6ezJ5HfAYyFd2aFsAkMIt5EMM9iDefEvP97WpK-V3NXHb9iYhOcwHlWTxzAKUFoPp_b0EJuqa_pE7GOdBGPEA6qzWlqZL8sthWfhh7mAOUqcdbPxJgVT53DVul2I_627wFM7Qf0U9WeVYbmbiK01h_fYDog8F0bxL9ZX5jg4m9yD-_U0zniaeh-2eSfEHSWrzssx1zFiz1uKOxcYrtAC5cIzeIvyF2mhoK38-cbSiI9B8fgZcMa1u53QWY6GyWCBsEeIXdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
إعفاء المتحدث الرسمي باسم وزارة النفط العراقية صاحب بزون بعد تصريحات
مثيرة للجدل طفّي التبريد بالصيف”، التي أثارت موجة واسعة من الاستياء الشعبي والانتقادات الإعلامية، بعد تحميل المواطنين مسؤولية الازمة</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/76945" target="_blank">📅 00:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامب: فتح مضيق هرمز سيكون سريعاً عند توقيع مذكرة تفاهم.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/76944" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامب: الحصار له تأثير أكبر من القصف.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76943" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76942">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامب: نسعى للفصل بين قضايا إيران ولبنان وفتح مضيق هرمز والاشتباكات في لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76942" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامب: أريد الحصول على اليورانيوم المخصب من إيران. سنستعيد اليورانيوم المخصب من إيران في المستقبل القريب.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76941" target="_blank">📅 23:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76940">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامب يهاجم مراسلة السي ان ان كايتلان كولينز: مراسلة فاسدة تقف هنا، لا تبتسم أبدًا. شابة جميلة، لا تبتسم أبدًا. لم أرَ ابتسامة على وجهها قط. أراها واقفة وعيناها تفيضان بالكراهية.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76940" target="_blank">📅 23:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‏ترامب: وقف إطلاق النار في لبنان مختلف عن وقف إطلاق النار في أماكن أخرى من العالم</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/76939" target="_blank">📅 23:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76938">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامب: إيران قريبة من توقيع الاتفاق نظريًا.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/76938" target="_blank">📅 23:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ترامب حول إيران: يمكننا الاستمرار لمدة أسبوعين إلى ثلاثة أسابيع إضافية.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/76937" target="_blank">📅 23:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76936">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترامب: يفضل عدم القضاء على إيران.</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/76936" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامب يتخلى عن الكويت</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76935" target="_blank">📅 23:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامب: الهجمات بين إيران والكويت كانت رد فعل متبادل.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/76934" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">ترامب: المفاوضات مع إيران تسير بشكل جيد، مفاوضات قد تُعقد في عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/76933" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ترامب: المفاوضات مع إيران تسير بشكل جيد، مفاوضات قد تُعقد في عطلة نهاية الأسبوع.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/76932" target="_blank">📅 23:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hha3exk2NkGoiBK0cgaLOJ3cgXv6H6rPtAyCE2FFxlqMFm8L7-eAv2UK5hzcjX_ueTYU6eqVPvdvsOgFE8Skpj_m49VrN2CwpIzFPgCIenwGWRnfIvd0HlENIdi1RWHQOSaZQn0_SwYqVdYJu9P2yWP6LwKGPXonVvEHun7QJ6MCJ8uV0S8EvF0VQH-W_M6tsQzZZcBv-N_VhDKTpoune1uQ9FzpJKNhXoZ9wGPWhMr-fkB_VAzGpqRUKiyWdkNK4eIQjb8O2A_w4pJEvoEguJ_U65NTKO_DEBQMh0B2mnVxBWxCtpmv7y849STHfr6e_tRo2AUTvZO3oBxbCQiL3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏توم باراك يشيد بالفصائل التي نزعت سلاحها:  نتقدم بأحر التهاني إلى رئيس الوزراء العراقي  على هذه الخطوة الهامة، التي تُمثل حجر الأساس لحكم ذاتي عراقي مُتجدد، قائم على استعادة السيادة، والاستقرار الدائم، ووعد النهضة الوطنية. كما نُشيد بالجماعات التي سيُسهم…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76931" target="_blank">📅 23:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76930">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbb7cd4d19.mp4?token=rpZ3Jk9o5WsbQeHdYeUPdOrI-pc1QxbzNxfnQgnII5zFeHr07lvy_K-gun0gzSV9__RHD9l5GnAA10CCKqoP6N-iE6Cgynd29deTG1eyrNTqrrus_o5HEMKcvh0G00_n45slBlHnC5MpoBOwHes6DlxBTzQnrgc7B4JxJdMYTVyEwbcgZkW1FtdYJ-ICuB62-ogMEIR1GtBLkp_YAcBw28Baj0a42TfmwwjidPOHSR2XKjKEAuQzFqF6AK7jap6cnGx22fxjkv8EcooeOUS6GJR5zbVdusAUex63v3SQnWuamlju2BwrwSok7v4YLIlDg1DjIAzqRnmCKIo2kaofjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbb7cd4d19.mp4?token=rpZ3Jk9o5WsbQeHdYeUPdOrI-pc1QxbzNxfnQgnII5zFeHr07lvy_K-gun0gzSV9__RHD9l5GnAA10CCKqoP6N-iE6Cgynd29deTG1eyrNTqrrus_o5HEMKcvh0G00_n45slBlHnC5MpoBOwHes6DlxBTzQnrgc7B4JxJdMYTVyEwbcgZkW1FtdYJ-ICuB62-ogMEIR1GtBLkp_YAcBw28Baj0a42TfmwwjidPOHSR2XKjKEAuQzFqF6AK7jap6cnGx22fxjkv8EcooeOUS6GJR5zbVdusAUex63v3SQnWuamlju2BwrwSok7v4YLIlDg1DjIAzqRnmCKIo2kaofjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الجيش الإيراني: استهدفنا قبل ساعات "مركز القيادة والتحكم" المتمركز على متن مدمرة أميركية في بحر عمان</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76930" target="_blank">📅 22:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76929">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">استهداف سفينة عسكرية أمريكية بالقرب من المياه الإقليمية الإيرانية في خليج عمان.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/76929" target="_blank">📅 22:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/76928" target="_blank">📅 22:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">استهداف سفينة عسكرية أمريكية بالقرب من المياه الإقليمية الإيرانية في خليج عمان.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/76927" target="_blank">📅 22:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇮🇷
🔳
المتحدث باسم الحرس الثوري الإيراني:  أظهر تحقيقنا وبحثنا في حادثة استهداف مبنى الركاب بمطار الكويت أن القوات الجوية التابعة للحرس الثوري الإيراني لم تطلق النار على هذا الهدف، وأن تدمير مبنى الركاب كان نتيجة خطأ في أنظمة باتريوت الأمريكية، التي سقطت على…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/76926" target="_blank">📅 22:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">💲
📈
العقود الآجلة لخام برنت ترتفع 1.81 دولار لتبلغ نحو 98 دولارا للبرميل</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76925" target="_blank">📅 22:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76924">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
عراقجي:  نحن والأميركيون ندرس النصوص التي تم تبادلها ونعمل على صياغة نهائية.  العودة إلى المفاوضات ستكون مستندة إلى تأمين حقوق الشعب الإيراني ونهاية الحرب على إيران ولبنان وفي المنطقة.  أنقل لكم حقائق أن الأميركيين لمسوا قدرة إيران في هذه الحرب خلال الـ40…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/76924" target="_blank">📅 22:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
احتفالات كبيرة في العاصمة اليمنية صنعاء بذكرى عيد الغدير الاغر.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/76923" target="_blank">📅 22:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🇮🇷
إيران الإسلامية لاتتخلى عن حلفائها.. عراقجي: نحن نعتبر لبنان بلداً شقيقاً وصديقاً لنا ولم نسعَ أبداً إلى التدخل في الشؤون الداخلية اللبنانية.  كانت لدينا وجهات نظر وملاحظات بيّناها وحزب الله جزء مهم من البنية السياسية في لبنان.  لبنان جزء لا يتجزأ من الحرب…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/76922" target="_blank">📅 21:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76921">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇮🇷
إيران الإسلامية لاتتخلى عن حلفائها..
عراقجي:
نحن نعتبر لبنان بلداً شقيقاً وصديقاً لنا ولم نسعَ أبداً إلى التدخل في الشؤون الداخلية اللبنانية.
كانت لدينا وجهات نظر وملاحظات بيّناها وحزب الله جزء مهم من البنية السياسية في لبنان.
لبنان جزء لا يتجزأ من الحرب بين إيران وأميركا والكيان الصهيوني ويتعرض للعدوان.
نحن نعتبر أن مصير حرب إيران مع أميركا و"إسرائيل" ليس منفصلاً عن مصير الحرب في لبنان.
هناك ترابط كبير منذ اليوم الأول بين لبنان والحرب على إيران حيث طُرح ذلك في المفاوضات وموضوع نهاية الحرب.
مواقفنا واضحة جداً بأن نهاية الحرب ووقف إطلاق النار يجب أن يكون في إيران وجبهات المقاومة كافة ومن بينها لبنان.
عند وقف إطلاق النار طلبت من رئيس وزراء باكستان إدراج عبارة "لبنان خاصة" عند القول إن الحرب تتوقف في الجبهات كافة.
ما تم في النهاية هو إدراج لبنان في وقف إطلاق النار.
نحن اليوم في المفاوضات التي نجريها للوصول إلى مذكرة تفاهم مع الولايات المتحدة البند الأول فيها هو نهاية الحرب.
في الجملة الأولى من مذكرة التفاهم قلنا إن وقف الحرب يكون في محور المقاومة كافة وأولاً في لبنان.
لبنان دفع أثماناً في هذه الحرب التي فُرضت علينا من قبل أميركا و"إسرائيل".
أصدقاؤنا وأحباؤنا في لبنان تعرضوا لاستهداف من قبل "إسرائيل" وبكل تأكيد مصيرنا واحد حتى نهاية هذه الحرب.
المصير واحد ومرتبط بين إيران ولبنان في الحرب ونهايتها.
إما أن تتوقف الحرب في إيران ولبنان أو لا تتوقف لا في إيران ولا في لبنان.
من أوقف الحرب خلال اليومين الأخيرين هو قدرة المقاومة اللبنانية بالدرجة الأولى وقدرة القوات المسلحة في إيران.
عندما وصل الأمر إلى قوات الكيان الصهيوني بأن تهاجم الضاحية الجنوبية لبيروت اتخذنا موقفاً قاطعاً والقوات المسلحة استعدت للرد.
منذ أيام تنتهك "إسرائيل" وقف إطلاق النار بين إيران وأميركا وفي لبنان لكن هذا الانتهاك قوبل برد من حزب الله.
إن انتهاك وقف إطلاق النار في بيروت هو عدوان وقد أعلنا للأطراف كافة أنه إذا هاجموا بيروت فإننا لن نتحمل ذلك.
قلت لكل قائمة اتصالاتي بوضوح إن نتيجة العدوان على بيروت ستكون عودة الحرب ومن واجبنا التصدي للعدوان.
أتقدم بالشكر لجميع بلدان المنطقة الذين ساهموا بهذا واهتموا وأجروا اتصالات مع أميركا ومارسوا ضغطاً عليها.
في النهاية أميركا منعت الهجوم الإسرائيلي على بيروت بعد الموقف الإيراني والضغط عليها.
في أي لحظة قواتنا المسلحة مستعدة لإستئناف الحرب وضرب "إسرائيل".
قواتنا المسلحة مستعدة لضرب "إسرائيل" إذا اعتدت على بيروت.
المفاوضات تتأثر بالعوامل الخارجية وهذا أمر طبيعي.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76921" target="_blank">📅 21:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76920">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇮🇷
🔳
المتحدث باسم الحرس الثوري الإيراني:
أظهر تحقيقنا وبحثنا في حادثة استهداف مبنى الركاب بمطار الكويت أن القوات الجوية التابعة للحرس الثوري الإيراني لم تطلق النار على هذا الهدف، وأن تدمير مبنى الركاب كان نتيجة خطأ في أنظمة باتريوت الأمريكية، التي سقطت على هذا المبنى بعد فشلها في اعتراض صواريخ إيرانية.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/76920" target="_blank">📅 21:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76919">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427e365e60.mp4?token=S6BBAMeCC0juTfHq7RoaqWIHWrCdCvtvIxiiHKdyUl4btbDt5Fn4EhV2DiCzarJGoc8ixDEljzRf0mbWulKUWavVDlrlMp52ba865pworVS-j5tmlUx8hDkoxbC6KddhnSRD4y5qJsU4qMxmJ94tUaaJIm0idxqbLB-F5OPDdS6a9RvfIRm6KZSrTiX1W7OHXN9k0PHnYluzzV8F7_NnJraiWZ3onJ5af4fO0fG6VdXvGBbpHOw7XlhDndC4NpZAHLqVxaDFiy-8n_r_Wykgg-JthM55E09JFmAkSjicgKxrnrpz_EMljccIxc2rUGDURZkOHq9oW0UUHmzDDipEn7OCrFp6hkJ2CZafcYuHH_J1a9AYpbFr_uXFHzZI29l-ahVJmsmrl7-Ts6dOrAXy39XgIACxHrcXScA9DVsxJa8shiS0HZVIbMJMM0W8gme4z09WaGsgGH1EayRM0TluQUYyArIZpXkDh11dqYbkCajxidTblFtA3wK9clr6K4i-5XOmjo3TOR08BkVAdZPioMlZQh3wp17aBTCSeDeGXESHL03gz6CLu70fvX7dSF9DGpC0jNcp8ulssaILFebdn52AeaWmluo0lRfUIK8xVRv9UHPMFQ4iIn1juBibQkX37KVmfd6bFVx9YmzU22590uCOzK-pm4_AMKXLQN1r9xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427e365e60.mp4?token=S6BBAMeCC0juTfHq7RoaqWIHWrCdCvtvIxiiHKdyUl4btbDt5Fn4EhV2DiCzarJGoc8ixDEljzRf0mbWulKUWavVDlrlMp52ba865pworVS-j5tmlUx8hDkoxbC6KddhnSRD4y5qJsU4qMxmJ94tUaaJIm0idxqbLB-F5OPDdS6a9RvfIRm6KZSrTiX1W7OHXN9k0PHnYluzzV8F7_NnJraiWZ3onJ5af4fO0fG6VdXvGBbpHOw7XlhDndC4NpZAHLqVxaDFiy-8n_r_Wykgg-JthM55E09JFmAkSjicgKxrnrpz_EMljccIxc2rUGDURZkOHq9oW0UUHmzDDipEn7OCrFp6hkJ2CZafcYuHH_J1a9AYpbFr_uXFHzZI29l-ahVJmsmrl7-Ts6dOrAXy39XgIACxHrcXScA9DVsxJa8shiS0HZVIbMJMM0W8gme4z09WaGsgGH1EayRM0TluQUYyArIZpXkDh11dqYbkCajxidTblFtA3wK9clr6K4i-5XOmjo3TOR08BkVAdZPioMlZQh3wp17aBTCSeDeGXESHL03gz6CLu70fvX7dSF9DGpC0jNcp8ulssaILFebdn52AeaWmluo0lRfUIK8xVRv9UHPMFQ4iIn1juBibQkX37KVmfd6bFVx9YmzU22590uCOzK-pm4_AMKXLQN1r9xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
30-05-2026
مستوطنة كريات شمونة شماليّ فلسطين المحتلة بصليةٍ صاروخيّة.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/76919" target="_blank">📅 21:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🇺🇸
‏ترامب: علاقتي بنتنياهو ممتازة وهناك توافق بيننا في قضية لبنان.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/76918" target="_blank">📅 21:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IcTToLdTO7jQzqf2ZYyC4w1cXDrGkZc5iIIjaUKmGN8MdwhcntYqVaSLThJD9jVU4BVFCMhiX9YYL2XmX9vuqUBNvGGPuBMYSb582FROZUELVX8OVmaQkWcmmyrHkMwfXNexXud-jC_24FayYnL0mbITF8C8aKCqJ1E_q7oVFXcMR__ZnNva7mN6F6FPIpgcbjLnk5BUIYvEoM3iBy5vPeeOQDzlKsdGvM3DmNxYusETUrXDZWV8nF9_HgMP0WjzzBaowaoY6MwX6d4q6zB7M_tDbQ4QRXb5ZRq-jruiq07n7f8_5eHxl_XnY7b4xT7YY7kypN-LUoqKgx8ne7fJ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ما حدث البارحة هو سياسة وسلوك ايران الجديد ! لا مزيد من الصبر الاستراتيجي والتغاضي والمراعاة .. إذا فقعت لايران عين ستفقع ايران عينين للعدو .. والعدو هنا هو امريكا واسرائيل ومن يأويهم !!!
من أراد ان يفهم فهم ومن لم يفهم بعد سيفهم رغماً عنه ولكن بتكلفة اعلى .</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/76917" target="_blank">📅 21:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مصدر لنايا   اغلب الفصائل التي رفضت فكرة النزع بناء على تغريدة ابو مجاهد العساف و الكعبي و الجعفري هي الفصائل الوحيدة التي استخدمت السلاح منذ حادثة يوم المطار حتى الان وبصورة فعالية ميدانية ذات تاثير واضح " عدا فصيل الغراوي " الذي لم يظهر له موقف واضح حتى…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76916" target="_blank">📅 20:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76915">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
‏
مسؤولين إسرائيليين:
التقديرات بأن إسرائيل ستهاجم بيروت خلال الأيام المقبلة.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/76915" target="_blank">📅 20:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇺🇸
‏
ترامب:
علاقتي بنتنياهو ممتازة وهناك توافق بيننا في قضية لبنان.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/76914" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🌟
بيان صادر عن حزب الله حول ادعاءات العدو الإسرائيلي الكاذبة بشأن مستشفى تبنين الحكومي:
يواصل العدو الإسرائيلي إطلاق الأكاذيب والافتراءات، مصوبًا سهام التحريض والتضليل نحو الشعب اللبناني تحت غطاء الحرص عليه وعلى أمنه ومستقبله، وآخرها المزاعم التي أطلقها بشأن مستشفى تبنين الحكومي، في محاولة مكشوفة لتوفير غطاء سياسي وإعلامي لاعتداءاته المتكررة على المستشفيات والطواقم الطبية والهيئات الصحية والمسعفين، والتي تشكل انتهاكًا فاضحًا للقوانين والأعراف الدولية والإنسانية وترقى إلى مستوى جرائم الحرب.
إن هذه الادعاءات المختلقة تُعدّ تهديدًا علنيًا للمستشفيات اللبنانية والمؤسسات الطبية، لا سيما بعد الاعتداء الأخير الذي طال محيط مستشفى جبل عامل، وأدى إلى إخراجه عن الخدمة وتعريض حياة العديد من المرضى والطواقم الطبية للخطر، بما يؤكد النوايا الحقيقية للعدو في توسيع دائرة استهدافه للبنى التحتية المدنية والصحية والحيوية، وتدمير كل ما ينبض بالحياة، وضرب مقومات الصمود، بهدف بث الخوف والضغط على أهلنا الصامدين وثنيهم عن التمسك بأرضهم.
إننا ندعو المجتمع الدولي والأمم المتحدة والمنظمات الدولية والإنسانية والصحية إلى التحرك العاجل وتحمل مسؤولياتها إزاء هذه التهديدات الإسرائيلية الخطيرة للقطاع الصحي في لبنان، وعدم السماح للعدو بتكرار جرائمه بحق المستشفيات والطواقم الطبية على غرار ما ارتكبه في قطاع غزة.
إن هذه الأكاذيب لن تغير من حقيقة أن العدو الإسرائيلي هو المعتدي على لبنان وشعبه، ولن يُفلح العدو في زرع الشقاق وبث الفتنة بين اللبنانيين. وإن المقاومة مستمرة بواجب الدفاع عن أرضها وشعبها، وتُلحق بالعدو الخسائر الفادحة، وتُجرّعه مرارة خياراته العدوانية الخاطئة، وثمن تدنيسه لأرض الجنوب وتدميره للمنازل والبيوت.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76913" target="_blank">📅 20:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">بسم الله الرحمن الرحيم  اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.  ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/76912" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇷
رئيس البرلمان الإيراني محمدباقر قاليباف:
علّم الإمام الخميني (رضوان الله عليه) الشعب الإيراني ألا يتراجع أمام البلطجة والهيمنة، واليوم، مستلهمًا من هذا النهج، أظهر الشعب الإيراني في معركته مع أمريكا والكيان الصهيوني أن عهد تهديد إيران دون تكلفة قد ولّى، وأن أي عدوان سيُقابل بردٍّ حاسم وقاسٍ ومتناسب.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76911" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بسم الله الرحمن الرحيم  اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.  ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/76910" target="_blank">📅 20:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🌟
🏴‍☠️
إستهداف دبابتي ميركافا وآلية عسكرية تابعة لجيش الإحتلال الإسرائيلي بمسيرة انقضاضية في محيط قلعة الشقيف بجنوب لبنان.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76909" target="_blank">📅 19:55 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76908">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو مهدي الجعفري</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_Tb82HQouXfZf91Z7YIe2ntwnrm1f6aPFEKd8ogpL0iW-sNdwfkA3_BQXtMiVih0rMFFQatzbXU7XDe3tiEX6MXutT-XzCjCQbr6V1gqzDB_wqMecFKjJp3L8sVNkwm-kNjBdbo6rkdiG_WNN4Fkoxn3pQB9jVSnk3CicLz2JhT4KrBr4LbrYGCAJTwxD8D8nwCjqDYGpACYyAte7SwsVSNaxICwIO4vN1nyIeOkZ4t-RO0Uccj4vIxSe2bDvT2b--2cETrofk7OHU2PxTl-UIVBI3Do1qlM_DvxrjAAic6gqboBEhEmQm2m2gTHTnGlUMbm0WDv5Mw0vGok0ATFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسم الله الرحمن الرحيم
اِطّلعْنا عبرَ وسائلِ الإعلامِ على الدعوةِ التي وجّهها الإطارُ التنسيقيُّ إلى فصائلِ المقاومةِ الإسلاميةِ بشأنِ حصرِ السلاحِ بيدِ الدولة.
ونؤكّدُ أنّ أيَّ مشروعٍ وطنيٍّ لحصرِ السلاحِ يجبُ أن يترافقَ مع خطواتٍ حقيقيةٍ تضمنُ سيادةَ العراقِ واستقلالَ قرارِه، ومن أبرزِها:
1ـ إنهاءُ التبعيةِ الماليةِ والاقتصاديةِ التي تقيّدُ إرادةَ العراق.
2ـ وقفُ جميعِ أشكالِ التدخلِ الخارجيِّ في القرارِ السياسيِّ العراقي.
3ـ إنهاءُ أيِّ وجودٍ عسكريٍّ أجنبيٍّ على الأراضي العراقيةِ ومعالجةُ جميعِ التهديداتِ التي تمسُّ السيادةَ الوطنية.
4ـ تمكينُ العراقِ من امتلاكِ منظوماتِ دفاعٍ جويٍّ وراداراتٍ حديثةٍ لحمايةِ أجوائِه وسيادتِه.
5ـ تعزيزُ استقلالِ القرارِ الاقتصاديِّ وفتحُ المجالِ أمامَ شراكاتٍ متوازنةٍ تحفظُ المصالحَ الوطنية.
وعليه، فإنّنا في المقاومةِ الإسلاميةِ – سرايا أولياءِ الدم – نؤكدُ أنّنا سنكونُ من أوائلِ المستجيبينَ لأيِّ مشروعٍ وطنيٍّ حقيقيٍّ لحصرِ السلاحِ بيدِ الدولةِ متى ما اقترنَ ذلك بضماناتٍ فعليةٍ تحقّقُ السيادةَ الكاملةَ وتحفظُ استقلالَ العراق.
كما نؤكّدُ تمسّكَنا بالدفاعِ عن العراقِ وشعبِهِ وقرارِه الوطنيِّ، ورفضَنا لأيِّ وصايةٍ أو هيمنةٍ تمسُّ أمنَه أو سيادتَه أو مصالحَه العليا.
العراقُ أولًا
واللهُ وليُّ التوفيقِ
أبو مهدي الجعفري</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76908" target="_blank">📅 19:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76907">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1af8c7a50.mp4?token=Vn_OwYgIA0GOJGIhk5bouejvis52b-dfCtCaUg77xjHExSV-xrL8IwlVCqYOIC3aCknlPSnxpctGN8GIdOM1eCsGqlWEWGLsBkhxmt9vlb-p0WLP03goJ8eq_tzcLvIVdLPpv4ccT9gc3kCmBK7OfcekjsP9O9tcefjITnnCpexfklEf6D5OIuG9vJzanzJaQ8EYr6K8KaSycYEBuUuB6C01Vp8c0nia85LyqNcwKi1NPdPLQcJ1dh5YzR4vbs55ionJx2jYqZbpus3DNIgxnUBrGKb6DIW3TdwBstyqcN6FChoaHPVfGboGtzLUtLxMuIPRon0HYeE3gzQ6UFLKtY9Ubb-01JEIe5ykGTI7NnvjH4TznTZ1y_smM2TrlEgcsIhf5A9mxA-s3a6E-E3bdwgnbNVrVRmKf5nE8xKHOrRXvb6xmZzRuYNuQ0eEYnprjF7VFOUCdlwwCbJB6lJR0DEwBlMoI6F77WT4xkOzkIuULz4hoZjIq_0hdXYibIWVZYu20r7V-C9yc0oFvP08bgBE1rS8fYiBSh7S5ZZRJD_J8lhTeAfN4vK1-dHQpm3jdxWP3Zv_heqDsVenHLhbOOPb0o8e0I-WoYOwAgW4PI1iOVgrJgqJjya9gt4SaNu2dHxf_6eH2Z8d8isIdArL-sSmMm9gxSwrSl9bcqGkNro" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1af8c7a50.mp4?token=Vn_OwYgIA0GOJGIhk5bouejvis52b-dfCtCaUg77xjHExSV-xrL8IwlVCqYOIC3aCknlPSnxpctGN8GIdOM1eCsGqlWEWGLsBkhxmt9vlb-p0WLP03goJ8eq_tzcLvIVdLPpv4ccT9gc3kCmBK7OfcekjsP9O9tcefjITnnCpexfklEf6D5OIuG9vJzanzJaQ8EYr6K8KaSycYEBuUuB6C01Vp8c0nia85LyqNcwKi1NPdPLQcJ1dh5YzR4vbs55ionJx2jYqZbpus3DNIgxnUBrGKb6DIW3TdwBstyqcN6FChoaHPVfGboGtzLUtLxMuIPRon0HYeE3gzQ6UFLKtY9Ubb-01JEIe5ykGTI7NnvjH4TznTZ1y_smM2TrlEgcsIhf5A9mxA-s3a6E-E3bdwgnbNVrVRmKf5nE8xKHOrRXvb6xmZzRuYNuQ0eEYnprjF7VFOUCdlwwCbJB6lJR0DEwBlMoI6F77WT4xkOzkIuULz4hoZjIq_0hdXYibIWVZYu20r7V-C9yc0oFvP08bgBE1rS8fYiBSh7S5ZZRJD_J8lhTeAfN4vK1-dHQpm3jdxWP3Zv_heqDsVenHLhbOOPb0o8e0I-WoYOwAgW4PI1iOVgrJgqJjya9gt4SaNu2dHxf_6eH2Z8d8isIdArL-sSmMm9gxSwrSl9bcqGkNro" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
بالتصوير الحراري | مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
02-06-2026
آلية نميرا تابعة لجيش العدو الإسرائيلي على الأطراف الجنوبيّة لبلدة يحمر الشقيف جنوبيّ لبنان بمحلّقة أبابيل الانقضاضيّة.</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/76907" target="_blank">📅 19:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76906">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🏴‍☠️
رئيس أركان جيش الإحتلال الإسرائيلي:
سلاح البحرية سيؤدي دورا حاسما في أي مواجهة عسكرية جديدة مع إيران.
قوات البحرية تنشط في ساحات قريبة وبعيدة وتشرف على عمليات لن نكشف عنها حاليا.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/76906" target="_blank">📅 19:18 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76905">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pboT6k6EKHKB8SRcEXl-an-IYXxIt3vcemvLn3G8L2DgHR3SPVp2cURhcP8UQWXPoWWov8ItijSg_rdkEjyTz57gbPZJuEMXIT0t_frWMY1HI6XHrFoiE-dYfpERM3_mYX_E1So_dbZCIIp_ff1aPzXTOdtc0KydPrLl7NDwkpPXdTIdI9iIyW73nyUvzhZnp0HlOqY7kHyc7Q-1xvsbJk00KaUZ2xvJEVWuzK81GiM3pQH5Xwq_nDrHc8NjOqGT-8HIowuPbUiUWzl1GFjS8AE87s3SFp-bwAHIwju4cbS6avzEyZkD3cF14479KGxn7KFLJRPoS9LLuabaQO5uWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
ماركو روبيو: بعض حلفائنا في المنطقة كانوا متعاونين بشكل عدواني للغاية، مثل الإمارات العربية المتحدة.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/76905" target="_blank">📅 19:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76904">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa386b3d31.mp4?token=sRJAqZMbK2DO_4FrsMB0aRN6AiA_7W1hdPMmAPHKsOiXE4Bn3frYD4yfNhhN75UrwqEgmo_i-2Xgr5sT9szOb5GNGZpkXfjMbrKlxmdaTnUvoY4_328HOZPpAqGBLeTi4LNSAsJoIrzEVtbatgDIUzsKKd9f-Z1ue5x0VlF9xQf969ZU4KuJFHV6AJmYqXTHzIHRrWjxZjdU3y8dirRRbrSwRZ8M9udOMWrybAlsAdQkA9qd4_edupy5cNctWOY8FDStjfLKk-P9KdofedO0MQym-yyw68T2hPe_uX0H5xUp-cXeX2FMPCnzaqFk9jU1rxp4zRzS2ozQip4xhgYW5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa386b3d31.mp4?token=sRJAqZMbK2DO_4FrsMB0aRN6AiA_7W1hdPMmAPHKsOiXE4Bn3frYD4yfNhhN75UrwqEgmo_i-2Xgr5sT9szOb5GNGZpkXfjMbrKlxmdaTnUvoY4_328HOZPpAqGBLeTi4LNSAsJoIrzEVtbatgDIUzsKKd9f-Z1ue5x0VlF9xQf969ZU4KuJFHV6AJmYqXTHzIHRrWjxZjdU3y8dirRRbrSwRZ8M9udOMWrybAlsAdQkA9qd4_edupy5cNctWOY8FDStjfLKk-P9KdofedO0MQym-yyw68T2hPe_uX0H5xUp-cXeX2FMPCnzaqFk9jU1rxp4zRzS2ozQip4xhgYW5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🔳
رئيس مجلس الوزراء الكويتي يطلع على حجم الدمار في مطار الكويت الدولي بعد دكه بالصواريخ والمسيرات الإيرانية.  "امبه سنتكوم ليش چذي"</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/76904" target="_blank">📅 18:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76903">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🌟
‏وزير الخارجية الأمريكي روبيو: إيران ترد على عبور مضيق هرمز بهجمات إقليمية.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/76903" target="_blank">📅 18:28 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
