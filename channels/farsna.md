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
<img src="https://cdn4.telesco.pe/file/TPN1xTSFsxkULGpdcC8tQFeWP0UKA7UaboZ3WqAXm-F-3YWMkhbDiWKhmg5WcNnUnZvfA7UcDyCMvVdxFNJEb5C9-gpCKHmlQOWUzKwSWAq89tOi36TjdBlz6oy4WcMupy_MVgAhnRocUKbFZq1xsd4U-up7ounAwiuuWyIb6PoHDfDW7tUsKzEFrmlmnkwFQ5lzVfAb7Gx429NKOPFR4ZcXeLsxx5iMh5HpibDuhDUtUb5HzUbG7jfjAwWhU-0hXvDlmkA_ces-BXN9zIvNMs-L593kEnYsOUFqvQTDYlm6CemovP2p8Pqk4JrMkBjPZS3ZkXDL_HU2w51yxtYuYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرگزاری فارس</h1>
<p>@farsna • 👥 1.79M عضو</p>
<a href="https://t.me/farsna" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 حقیقت روشن می‌شود‌‌تبلیغات@Farsnews_adsارتباط@FarsNewsفارس‌پلاس@Fars_Plus‌ورزش@SportFarsجهان@FarsNewsIntعکس@FarsImagesپیام‌رسان‌ها@Farsnaاینستاگرامinstagram.com/fars_newsتوییترtwitter.com/FarsNews_Agency</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 05:11:23</div>
<hr>

<div class="tg-post" id="msg-453486">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🔴
حملۀ موشکی به نقاطی در اطراف شهر اروندکنار
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر اروندکنار توسط دشمن آمریکایی مورد حملۀ موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.09K · <a href="https://t.me/farsna/453486" target="_blank">📅 05:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453485">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔴
نقاطی در شهر اهواز هدف حملۀ موشکی دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 2.11K · <a href="https://t.me/farsna/453485" target="_blank">📅 05:02 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453483">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36195e2362.mp4?token=vMHPnuUAEA1n6VFJt_vnXt3XGK4GHCDwj3a6ImqVtjRk1CsFrNAqwn8ONK2WrhqQIvmODVUX7DJ8YDhu2Q6PU6orPaLYTd3q-D52E3j_DnPnrQbo5kHx2FXexBehVcj_OcvfSf8FcSiABISX854hyhv3r_-kqLU0wruSfGaUTSHzGTGf9p2a-QWiIczkRfyML6DtnRwkDiGYQYAoPu1ErT4ZsiFrwjEYtsxLyrKq6g2D3dB0B2vSA5CuHBYx5AAsxGCyoAD-p1Na2gZbsbBPtsTgqscfI7DeMh6YZa0ZGAhrJOwnkwTp4RorGcHpDN6n6iHUk3AaYdvKDuIkfxhWfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36195e2362.mp4?token=vMHPnuUAEA1n6VFJt_vnXt3XGK4GHCDwj3a6ImqVtjRk1CsFrNAqwn8ONK2WrhqQIvmODVUX7DJ8YDhu2Q6PU6orPaLYTd3q-D52E3j_DnPnrQbo5kHx2FXexBehVcj_OcvfSf8FcSiABISX854hyhv3r_-kqLU0wruSfGaUTSHzGTGf9p2a-QWiIczkRfyML6DtnRwkDiGYQYAoPu1ErT4ZsiFrwjEYtsxLyrKq6g2D3dB0B2vSA5CuHBYx5AAsxGCyoAD-p1Na2gZbsbBPtsTgqscfI7DeMh6YZa0ZGAhrJOwnkwTp4RorGcHpDN6n6iHUk3AaYdvKDuIkfxhWfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌دستی کویت با دشمن آمریکایی؛ شلیک موشک از خاک کویت به ایران
🔹
منابع محلی از شلیک موشک‌هایی از  خاک کویت به مناطقی در جمهوری اسلامی ایران خبر دادند.  @Farsna - Link</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/farsna/453483" target="_blank">📅 05:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
حملۀ دشمن به یک منزل مسکونی در محلۀ چاه‌تنگوی قشم
🔹
معاون استانداری هرمزگان: عملیات جست‌وجو برای یافتن سه نفر از زیر آوار ادامه دارد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/farsna/453481" target="_blank">📅 04:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453480">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🔴
حملۀ موشکی به نقاطی در اطراف شهر شادگان
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر شادگان توسط دشمن تروریستی آمریکا مورد حمله موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/farsna/453480" target="_blank">📅 04:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453479">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
دقایقی پیش صدای چند انفجار در کیش به گوش رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/farsna/453479" target="_blank">📅 04:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453478">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">هم‌دستی کویت با دشمن آمریکایی؛ شلیک موشک از خاک کویت به ایران
🔹
منابع محلی از شلیک موشک‌هایی از  خاک کویت به مناطقی در جمهوری اسلامی ایران خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/farsna/453478" target="_blank">📅 04:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453477">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در بوشهر
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/farsna/453477" target="_blank">📅 04:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453476">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🔴
حملۀ هوایی به حوالی قشم
🔹
معاون استانداری هرمزگان: ساعت ۴ بامداد، نقطه‌ای در حوالی قشم مورد حملۀ نظامی دشمن آمریکایی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/farsna/453476" target="_blank">📅 04:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453475">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🔴
حمله موشکی به نقاطی در اطراف شهر آبادان
🔹
معاون استانداری خوزستان: نقاطی در اطراف شهر آبادان توسط دشمن تروریستی آمریکا مورد حملۀ موشکی قرار گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/farsna/453475" target="_blank">📅 04:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453466">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/blXLyXtMI1nRE9zYEh0LOLGuYpsoKvXuSAT7pKgHqjzZQHEJarlEOqFqzvKUqijzFFvqZ0mOxGCFlY_eXc-VVq9ad-aAKvyPdm8e5IoR5VQOB2XeQQVQwRavPEyVsWjgcbOQ0TUirs2u9E9d72v9DBddZvAqLOzr4F63s8TtBybCfpxfcBk4gR8cx6Mkcq-InN4ISZCpZHicF4B8ZGlOyiPYP0Gc55J8KTx-isC3dA-wcb7I5EiM53vhYj5jOCGcEFDlse7vmOZQPxl2_ePDmFzw5im8A1cDLIdQjyv8-SJIcYBCUS1mSlsA0ipTcpIAi0qej9OH1CWc-aZwgL83zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tEaFqItygf3f_7EX9pCU1yNZ3bz11A-xzGzDg6sCabrXep2E8L3dxg9fQbw7YnPylzDhOt5tQs2HniBNKmGDEMbSihiMlpqVbkoh3MfzuzzwmejJ5nJ1AlmLaOlfqBDEKhijB5P0Tetj6G3C3bilQRETT5egGvjhpP7u0_9IQ5CnNtvSFfPpWaWPA5XifOIQaHmx10KyJ5VUmruyBUsShxaSp7e7XccaX5Nxlg16quI7lSwE_EzctNi7UANbGWNJa4VuSpXUSFDI3KAVtzM6bWT_pcjN4YueWwzHD8yEvkbVaQZ3nnRoyhxKKs1gJ1_8aeLFYyDVOiztDMis5FjdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PvU7pNBbJmk4ncpDFBwwgBwYbxnSMKLP0sLy1W1EFgg4YEWzgx_GAo7XLB-jWkBYiIiyNtsK6u27aZ6IS7LYKroA5jkP4N8ODS01qgMTBcuDH4niErLVwdmT2B4LLKjMxxChLbJj_qpuZUd5lOPXtfeWJ4ITslb5vNLSJ1UDdPk0wJeSwTWRHViU7QMVjnh9nqvWRANNp1Sy4gl1Y4G71xr68SmWIOnrOddOiQZ5-Fabx84ECKfOQ3pLoN9XW7iJYen-bVggVOQC0rLjc99DVhW68kSiayzhj6haSrR0inspqQ8fsPF_SmyV5_RbyKIxrhdrQjREJjQEqmOJPrS7xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tQtVWdWiU0rx2IQzg3qbPu4ek-f0bgjKp_WKgG_cPsgIYidVprqg2xM38GYIBsjLqa3Bh1qmnQb9F10sEg8jIkOX9zVGHtScuLDIX5bWhIBT6N9qRiiy4Geor7iZ9gTk5PVIGMWhzUYp5kxceibFyuWPiNkllOeQDXn57a-wP4IrAeleabgZcJBlE--fesuLuXnurazlhxcRIeDmbLdGxj-k8YJge415LFMGUu-FGawJZ7ojY_F1NT_Q56eukVqeT9z1fHdjIZfkZLKVCzXJVdb71asEfE_atMNnyRNa1h8U9Ix_Rl03UI5oHD-rP3Er-OzOvfrk3V_wl_pyWYs24w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DNeq4CUytGXx14MqnqzOogwFmOjDp6TVbWcKkpFmWl3cNlHdXVuOlM0h5Xi__rWPxDCWtyIXWxnuZnhi0ySHxxZHDWfKGl8IrJFULMnk-2o7cD43-ccMacsltgBme-t98QpYYguBIeMFc0jHJ38xl4QwBuAzzlPZBnsuUsEIt_ouujHrZ44gRMZInXI5Hk9C_B0kQ9W-1w--yKQWEvtIQbkseP5doPN6LPrxiLpDGFk7riIWRU0ej_7oNfh4CYB_Z9_K3L83kCaHu6TlVvtuwBBIKhvYgT-BIqZ5r8OJGDfSNV2M8vwXokInD__g_bugdVseuhqcaliDU5o7njCLYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jgs4qTgAvYtFSASfEPUE-zVUNIVaDnlpZEtR3Wx4wEfv688CbwAxbd0N_YKEa0ZPGk1MPtFzQvMIDNqa1D5KbjrDi_wP16rbeQ3uG6ebePrEr240-mSup-NQcNz-OgQA-RfSgos8twfNgk4doJAfTeAXYTOBHpH5-Zzzb7u_DChkQxfxDhrPLWCWcOfzzH4fCID2BnuorEV0bpZGax0uGiQNkOoMYh1N46CFi8u9w4qiRHYIvVLGTMjaWOe96Qd0HtnJdIZWkvPObuuC_iWXo6MBMMOUUNu_s6kw4WiWBcGshIkkH2ErqkhSi9EyZAlJu1LT9B_K10rCT2TcuWDwaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ca3FlpKgGnuWkXhVfcJI3OFJrPfd5u0ST3JERFWJDhWRIqhKi4ZvD7x7z_VGOXFSvV3QRe77jDQKnQhEM4tLHymbRfYYzn1auiOlK9n93t-PD_HkThGbCITpoeL6YdTzLo2trXBFHNMe4c6Dn4lqZ9QgJp-LThTGl-iyPj58M9cmeY7ioegf6HQe22x-jxRuPpBUb36ItM44C5y0TqAVzU8SvcLVk5fsjNNca994W2JUDrjLaoEbDpqU68mWVoW5jomeW9hjwGiZx7yJuQDHvCpwSZe5OGLEChZNicExYRjayT5woAw1qgSYyd3K0cAsOvC8CYy2r9q44qSzdu2-3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q_0rDj8H09cji6xbB1iHWwRY22qSZPysT50NBxd9R7Yaiv2FRjwb5eKStdg7Z50KVBV83og8i1plZB1usuZdeAJRSa5_ujY3PPKNed6-ujyW5rc65kXcRb63V9vclSYD3YbAIRFL4i5paFy9FmCTL0-uyC98sGdcicd-nkpquDS6TYYHbu-_3wNlpsB7zdZ4KxO2la2z9u82AtG4z81DVgHhhdl76TiAHusNutoIyNmrxYaFEKKYx2Yywc5fYiaYXGRqjuAEiFdfjm93UkmncDWzzI4uQnC03Bi4RU3SpkGKqqjeaFeZCF6yo60wjsbLprilH60H51MOof2EGa3bvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FRM4_X-KSa3_rMcITe8QK29evbL5LF1PvVdbxcl0rNDg57kwRd1J6LLJwvFeokVO_5eAjJ_X-LC0PoHYEd76WBPDnrDG_M4RT6LU9HnwWem4KyBoorD44BF4wPRGELT3JGcjtYMcWZSgrf8rfYoCQfmpmLM5q3lzuWPJdJk_19htcNpVV5VE0w_hwWzM8PKWMPWNhtL_9QqF_5Sff7PcOgsWCuEa8yAdNrZIpHsoSWVnGJq88TswcnlmwlGDALegXMi7yIDRARbD_N1OtuW40-dnkIsKUx1wcd-TqiQthYmihf5NWDcmtDAuLLJBrO3U5ZaY0GjMh4X3sYwJAHhMyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
ویژه‌برنامۀ سالگرد شهید اسماعیل هنیه در میدان آزادی تهران برگزار شد
عکس:
میثم نهاوندی
@Farsna</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/farsna/453466" target="_blank">📅 03:18 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vzrNUj-ypVg_VC35VtzXYMuuZfuZt61ZDVWmor6UCwg9x98OYo1RlTiBLbBmjJ4IJ-oUpOiT96Xsrc7RDNIOMR63CtembgvHpTRBrD0aDpdJWTAGCi8ozXpfNErR5pgNJEpMGcKOUYBqfYP0gpGSf6VMrkPutAPdleQ1YaVE7Z57h4Xz9j2wrsUjXs1h_LxydzEXYm4xeeLIYf7Lr-PoObA9eq4PgvtV0bN9XW5qvdw9mgbjqPAqzmi8oyvdLxVgiGOeeIy1QuvYGvP7GZwIzEML61unnS33Lpxqz42xCCdPykorKWtyZJA9F6VJcVU9XMWgZRJ5s0j4uw0dvYmKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNK3XDpWm3ypv4bWP1uZwvoWFNezDiiL-B-Et6FCktIxZO-dJDCSmA-vAF8BDF4zUtTDUqrNElruvPKW5wCPJmTXYVFYDs3ozyISAOTwITWp9kNV4LWQB_J5XRUC1cVCgYxIUHmT6XGCfMxZnmDSW4PXEp_FmDO02nul2qXSBd8e-777UZyouH5A306Fp0TnIwiOkBkhTGNoTS8bFIoS_pHNy-Hq6LAu1DHK38GLBMPNbX3-nVbwef3j_DjFYQbSVqZvN24EN2acKeXDz2XKETCU9RuRJZ2f1xh7qPZz3YMDuVYnsuhg5k5tYYeCCAkTNUNNU_vdt3C-5yUdz1dDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BU3Ul4LCDl2hPp0C9JgWOlbz77uo8ekNG8Y8bGCEZaAUzjaMJzFYmZFUEo5T-4EPRqMnnoF4-lmDu0psc7vvkyiCgGmyG0fXFkPbUwDs-uIeTfKWFkbTWIew9sSNqrHAFgRIAW9iRH33SfRLemWjAtINUEocwX8yhf-TappjD-BXvcQuLhPsvP8tA7XAmxGhOJL4R5kHFK9cz3N_Gn2UKWH8rkvxeoVUoU5zvsMXMkqlGd_-2qEVE2PTC6-IglITowwp_VPbrp6pmznwmZ1wInrapNw0HPRdLO9UPKkDMrEwMJPCT3MjtUtutv-c_qC4FC4KCe0ohuVBiuqda9bwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UHCSKwiF_0PND7-3XMAno4i-epB9ohCtNX0kobQ5fq9Ao7pa8KPySxpuz4hMW-5e_B14nly2iGmzJPVYHLiHnaSnf91M7kQKphhKU3Esq4eb9h7kRbT_BL4m51vacEsdlFAznTfE0JR-A77VneLnDumem7sMGyJ1KUKHtjeJ6YJ2NfZivIb9W8qBnTZ6bQje2tytSgn_zaM9NMIpMDbhavyhRWySXuLmekrOVu2AIX-ywXS0Tcsu6JZm-gTOtX5XemJUo120fNgY4dybho9M5dRtjkCVC4MCNLdRdmvbzPSAdjFAB_gmmcge1VQxoHiqSOUJQRuRQ8RLPNH13ZK-SQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📰
دکۀ روزنامه | پنج‌شنبه ۸ مرداد ۱۴۰۵
@Farsna</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/farsna/453462" target="_blank">📅 03:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453452">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CZ5_A2445rI16wHvCo_0RUjQzsJ6XyGVCXSxZ2cKppuPb-w7tnhGkiYka4lozvGGqk8Hxps_4_1a2T0fuAqKuoqrRUhz2meiyrzFkly4S6t2pSKcJw8xlqpoY27w-P59OW7PuGvdyXdfLmuh8OY8f4umQt7gFiFWqrBXY_S_uD7jrmlJ_7zeOWUJToePOkx95x0P4VXClXAyxqskikXvDx3duq5sSxYISgW7TYkKvtzID06Lbvni41580zTWWz2xqw_4n-ZnPtjD7S_C9Tr_OT0eDliWYzJpoJY93QJ6T2aS_cgbpInEkhx3IVRe1C06wmV3hUbRseOxdyn3TV2d6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fqNf8nmd2qzQe1Fpn8OFzId8s1nSVVde5lAJixJluCWnzOOyFT_UTaFYLc_D82cXB5PANzsUTTCYcYlNKcdVUZjpNShqGwT1q4JPi1tfBnFuYhADalK_O5es5dI26BveFLGMtDKvkIvx5SUqpAZsIohiUDg8tnOS6Ea4WWAZJ4OWmyx_YIzD7zi90lUReW62eDkXDyYkN_3xsdSPUKcP7V5M__4m_YBAwmXtAee38M11F1lYy2ZK7BH153l6eBH_PcHZXkVBskDlPIcMielqLAlqFi5eBPHPdjQtVqQl3xyDGG3NmSLcYxefPEg3TNxrMG2IZQ2wbSi4Z3egfEYPOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lzKIHxcSO1ATfXou0o6lVhpDv-swOc2lUbk_Xcet6yCfwrd6ClpFu1X8B5exx5ylDfvfB70KfLLAfnmI6J53KI-v8jpVwvOrFWT1uk5UUKWVqqKkQrXe4x7nDBzYqtOVW8BfGAQj0s1bPLCna2GAhNM9Ugo0Th1yfYO-a7PzaxnolP9AGCkqZEpR9ibP8pvzm1YzkVRdRw5M0KLe8-fKsboT-O492QNkBAWoQem2bgCHWAuDhY_k5xS_ocxt6GQerfEQml095tIgTCPwAN0QLNMPgjGqsUioBAeMhm-qir_cHdqUlX1TXQEz5wThWHt2-cDjHGHMbMTGn482bvCZ4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nut7TwaG9RwrqjUab8E17QxFGFyfLVdogslY4Q_wwr1Emtt3vTyfKi8Zeqo-mllHp42viqEIi3VL1ssaOaqDCBWySn0-Y2kZ7yn_xnD3wm6mlJ2YtzxnegDgP-HfCsKeqaUpIWqWqIho1QqZKHgV6BhZCiFZ18_xoI4xtyAfRMda4GTbCehTAQUuOZchzcwICNqFpKxoTCOtOyIefd3YQP7x9dymN_SRXO5gN-QeVLG9QirtFHeBjZezSRAqBOIm1sEUq29yC96c6TFDXf4lm9SO99sqh0Ch4CJyDz3TjduikVq29hUy8PaoikZjQwLggSCmYcyhsAkt7B-yRXtXZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MT12iyVxDKLg196AU49-ETwLiP-T-ghtWYchczDRqXfvST3eTYIkgsFOcsFIz0TnLOfs0SyfyRk9lyPJ5pWhNepTWE5-C81F-GaJmrSgLNzUdYpm1wMHw0xVAWBzKjJ-t3OpqOCiJPVj0F51GsiV68gsekESqxfHBdrOsvMunIw1YcTfro64-jnOUSaznalDDpe8_Kn_Eo9P4gNJcA3j6njTVUFflyekI7IzLMbx1j8Fw2krAH2cCEEzNqQRH16W4Is9LyR-1U-tLYptf6rTyGsB41BsppEb5Lo4SMPKt6vVak8cv_mXCxBPdNf2Kv6WOiC_zQi59_MuWEcoJehdVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TtAA85D3qK4EEsc6FyZOE3s5BHIaKTsAUnDwgKXsXuHyv3z0Tc673bjJDlbOLXNrXWJv0Cnuz_xW_if_RWpBntYzWHeFJLyqYc455yoZfaSo1je2xQqdBOAWwe4JHUiyEUXA0c9HYwm_WUh-PrJyLApUzZ2g5EWtWo-4KSt5LYjjHC6EqTMGee8rvyWpFjpTXqzhP4yY9PL9ApyyJiAeEnB4amdGtWKEKq9_nHDDUEO-gL3id25j-3Qv2FqNdTbZdZM7nYhyB8fcX3zPfxSLr_jNsYp0kCYGE2fpJlDMJpAx9USDm8earehk_qkQtMHtlVoiXz3vL2AU0qmt_Qmk1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vtFrsw3al9KNWHbkFpqTguW2F1q0C3QGv19E_KBw8wN1iuwZYGzESiQ8rEEP8F6KP1cR5uSHDVL0xtpiYhVAj-c0IDtvEaZlYfsnhxaBn5g2U9Dy8c2VPc_7dElP3lhW6OyCBAibf16cBv_I7t8WF2dqlMCC3h7JZzFaxzo6tZlyzqI4Sg3X6D6LIPe_BY8pnPirr7KYenshr3a1Key_SQumisiH_Fr7MZ1K3gUvdaK2sr07Q6ngBl6J-GNCC5hSXDTCVHneSIw1GT1XLHueMD6Es5-3vCGBmmtvUEuCh72duxWt8MouV4GMXkj3TBBvufv01QoC3j-rljU7OxYvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XHZur4kvmbAopeeinY4zgFJj35LFWULsi1qB1EkDmlX8abo2S7RdpKgzkHG2UWZcqY8CjU437kTXXB9U8gGN2eelqkobu6eRr3TRrsJGbqEP6O1xwlIXQeIr90aUddbZRUYT21Kgedu5asOt3Q5drHqH7NfanC_9hC5OgI5mQIU04FF9LlZi4bCv-T85MtzqJpyNAlp7ys_UlPC22dVVZbcISxBSxZ_JgtJihKR1gv0ssZzusoi-Y7VQrzaMhlHm696kjGuPsXt0KUnma48fiEbBm6KGRQoKDz2YOeidqG_S4_0d5O4UNLpI9yNvWYj17SvXAgbtw0_qKhhDooV39A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gX9iKk89Eicn0Zjr51l4IgzXKPla4ZaG85Uq2B9ixnwAwkwPgqR2-7uFdmT0ddO3xenifa2Ev9z7Ps9TLdAlNfn26FL3VQ7elD6KzL5Gpkm-m5DDq2SLeZHDZNLMaF6FSUX0SZvTQcpQfr00EdQ_HEXmH0ZeDBgkxpe80CnqOXn4ec3gAXlFwUHo6VJVN1V6MAiAqXFI_rTC-YcOcY9bFzQLeFqNwA2pfgLaY6hRu9T5t-aP8HcNnbnlYFnGQc93uxHodVz8SFh0YSu9lvfHgiWKA4legY3G7LJlFv1C0yZITbZpUKkaFattNMKmetLDIjk-7DwUmMS1jldVJNM27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lrUTblbgvS9Hv3raeFcmtfuJUt5AbybJD3xGADARd7BRt1r52uJaRdN0OqmiR3n5TlVqFHKyK3htvD-q6FIxNKaynCDfturQ93m8prkYTJ4nxPhcY8JRu330YDZcOZ_bRWXnFIc5VL4INpeMQV1UoWsOYsio4NX1AHULxT1uhSP_w9h_z4eFwqafRplsNV6Cm_hse2ZEnmHZL3fcQqD3uWU6uTvekOwwsrEAYHFeZCPRvulMe7jX6cRbs-AhGU45Pet2FdvbTGitKkivp8vtrPIDE-zTwc1NwYFIWuv21zGKrJ8puHowf1PJW4bBHZDcMRZ_ySFu8aAYZrSYSPENaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/farsna/453452" target="_blank">📅 03:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453450">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFW27AaxicVp67BNranCwNQu90Vo8Z0Cjh2gUSlR4Ll6hlA6bRFIhtS2oS_RitoLmolL1n9mfBwdKSrXzHLYTYLinAdMucUVSOwqsnj763GZrbki0WRS4Doj1QNdehRIgkNQyrChdpW2-uVx0kb1m7ATeKPIJUPgs4WSLyjq9ei5D0lTILSYNXTnnnYdMDL7HWDiV7-_S0Ye7MtlQU3YE0Wp5HhBfYtFki4D59RrAvpLkTtmOqgbGMEIksziEHwrMxWkhTual7EqK1Q8c3MSaCBZLstaVZPGfYSHjbfOlE-MxGbAVfK32IXsBZMuOuXvED784-O6Rm4eE3NmjKvQxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد سنتکام به ترامپ برای حملات ۲ هفته‌ای به ایران
🔹
نشریۀ وال‌استریت ژورنال نوشت که فرماندۀ سازمان تروریستی سنتکام طرحی را به رئیس‌جمهور آمریکا پیشنهاد داده که ذیل آن، تا دو هفته به زیرساخت‌های موشکی ایران حمله شود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farsna/453450" target="_blank">📅 02:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453449">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
رسانه‌های عراقی از وقوع انفجار در مقر تروریست‌های تجزیه‌طلب در اربیل عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/453449" target="_blank">📅 02:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453448">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انفجارهای مهیب کی‌یف را لرزاند
🔹
رسانه‌های اوکراینی از شلیک حداقل ۴ فروند موشک «اسکندر» توسط روسیه و وقوع چندین انفجار قدرتمند در کی‌یف خبر دادند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453448" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453447">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dei_hPiCkZChmXchnnGh7sVYicguf5t9kXJyV9_gv8Pr-ajSSkTG1eUpUTYeBFchRtNnzHGOKeQH2-BjrGrpBa8-fHy9z7xCfg09SutEmt8o_qC507AYPDSjp_jXbHCmOtTiEyRMPFnJWNk5iu16ZiGowdC20ple3RteAbZz7H4rCdDZnUNtxlDXu0JIQCZ7VOJBHBiRKGz4ou6UXdDzZa0sf_zAZuNxga8ewP893uBhWpWhno-4_MTUV8tLazdDe2gCpQ6GMspA9fm2lePXjZrh0mwKHUEqjzT0mg2IfsXa60PlUFBkoTHHXhZXOykIrxnyBna86hDCqsz0eGbcuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
مردم به گرد مزار رهبر شهیدشان در دارالذکر رسیدند
@Farsna</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farsna/453447" target="_blank">📅 01:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453446">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPxWQbyE-3vwJe7m2Br0EW6-f4BIE8wgWdPJ6iiCE3ipOGUbm2Pw6hb7sC6yrvOQ5k9gHIkYiO1aGiAgHvV99lmJHzCGMVqJW8Ym5rtkqoh4GqJ5Xls0mjfDr6I2l_Dpwt6F7DLl1dOB3LcUONHJF-wQYapXSRFRLqqPGwMQhjGjUmGt6-6t1Cfsn1sIhT_Bzj3LmXXptsq2zpaE2kqlyEF63nfYUYgJI1MO4EfuU487BC3sVj6v8a8RY4bUy0TwAAlSP8YY5cTV2GbKjKwP_mCmgS-_618XlqKHCSSN69r7jpDOr9k14j4xw-TA0lgMOaaVN6x4YKA3JxeWvUowMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در پایتخت عربستان
🔹
منابع عربی می‌گویند لحظاتی پیش صدای ۲ انفجار نامشخص، به وضوح در ریاض شنیده شده است. @Farsna</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farsna/453446" target="_blank">📅 01:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453445">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
شنیده‌شدن صدای انفجار در پایتخت عربستان
🔹
منابع عربی می‌گویند لحظاتی پیش صدای ۲ انفجار نامشخص، به وضوح در ریاض شنیده شده است.
@Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453445" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453444">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3648e98935.mp4?token=EAKmofzunR3WT1Et8QlPd-kTeT97MUVZ8O6vMjftrRAoYML_lYgKkvCHZDeKdnJsHXwafopDOtVXJWs6_bTeLzP9hyVwsVK5Gxdwg89sIVAjjBgQjyNDgiY2jIC3vFA3JT14Y61xi_XF0fgXFqOg36fDKmm3eu6b7b7-hUOVwlI3buXzBwImCtskV2s_TqATA-kVLzgvCfLSqsCtf9i4Q68XZ7GGSsxzdy-n5908lUTNc5C-aKT_eofyyBnExqkgJ5Isjo9PFCX4XkDAHPaiji9k-dGFOY5Z9Y3kFIf-mzdtkAIyJ6dbX9iOtSXFd5knKJUi6Yk9jJzh4IdbjNuRdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3648e98935.mp4?token=EAKmofzunR3WT1Et8QlPd-kTeT97MUVZ8O6vMjftrRAoYML_lYgKkvCHZDeKdnJsHXwafopDOtVXJWs6_bTeLzP9hyVwsVK5Gxdwg89sIVAjjBgQjyNDgiY2jIC3vFA3JT14Y61xi_XF0fgXFqOg36fDKmm3eu6b7b7-hUOVwlI3buXzBwImCtskV2s_TqATA-kVLzgvCfLSqsCtf9i4Q68XZ7GGSsxzdy-n5908lUTNc5C-aKT_eofyyBnExqkgJ5Isjo9PFCX4XkDAHPaiji9k-dGFOY5Z9Y3kFIf-mzdtkAIyJ6dbX9iOtSXFd5knKJUi6Yk9jJzh4IdbjNuRdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای رفتار خاص امام شهید با مأمور ساواک پس از پیروزی انقلاب
@Farana</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farsna/453444" target="_blank">📅 00:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453443">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef23210083.mp4?token=NC48F-DpgT11DCe3RHEkusOabT2I89uz7Gdn0PaMKWfdhTOnMea6Qh8xkMKdUlNeL5Vxs16Wv5c5jnUmXMx021ds75evtXiqIhObonU2MfzFnD9FrWuvZuKeeeJ4qETQtyFBTQSeD5RxiD2ZEGcIpumMLUA2JsOuC1bpiLqU0OCGOkO9J4Iym2zrBQhfkb_pkgslbkJkMGEfGsQKgWQWVOc7wHxhrKG8LFEjFMCmd4iXOhJvkr_RCXQa5-X7kQR7Kh7aqI45PjPUrGM8cTo-cKRunJ2M6sV10i9XJax4GxZuB2IARtBVSF0bMGjJUBGKRC2sbCJ_Tz7zWKOjBu78UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef23210083.mp4?token=NC48F-DpgT11DCe3RHEkusOabT2I89uz7Gdn0PaMKWfdhTOnMea6Qh8xkMKdUlNeL5Vxs16Wv5c5jnUmXMx021ds75evtXiqIhObonU2MfzFnD9FrWuvZuKeeeJ4qETQtyFBTQSeD5RxiD2ZEGcIpumMLUA2JsOuC1bpiLqU0OCGOkO9J4Iym2zrBQhfkb_pkgslbkJkMGEfGsQKgWQWVOc7wHxhrKG8LFEjFMCmd4iXOhJvkr_RCXQa5-X7kQR7Kh7aqI45PjPUrGM8cTo-cKRunJ2M6sV10i9XJax4GxZuB2IARtBVSF0bMGjJUBGKRC2sbCJ_Tz7zWKOjBu78UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانیان در نجف اشرف هم تجمعات شبانه را ادامه می‌دهند  @Farsna - Link</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farsna/453443" target="_blank">📅 00:48 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453442">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شهادت یک مامور پلیس در ایرانشهر سیستان‌وبلوچستان
🔹
پلیس سیستان‌‎و‌بلوچستان: ساعتی قبل افرادی مسلح به سمت مأموران انتظامی در ایرانشهر تیراندازی کردند و در این حادثه استواریکم «مهران سالارزاده» به شهادت رسید.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farsna/453442" target="_blank">📅 00:41 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb118187a.mp4?token=EgXLH1qVSyPYBxTuqXMChCQcNMdjOG2HzwLGYRWI1LHWWSgTlcPu_mEphcGte560xhjaWhuen8PSmKpp4UJqzNq_NnE2K5hi-LL5b4AhjOFMEtMKe8c1BimSPHq994kwI-JllsTyqmS-ICx2Ue_7USYygDyJtEmG_dLzXKT-wTQ1q8YwGmICsbrTB52puN9VKirHDSXSIbjfJ4LspUrPiazcU2okOv1yghn_qJOGjs7g17AnHTUxheSjCE4FVIQh41v_575ixJJOXYkIvol8zPEbySXsrl5qMt7nICxKxrDV4xUG3_ssiBU3DIpFZLrA5xlx630vm1lf9rBBCGgCKTIWPi9_4aDO7zbTTaZvDwur6jGlsanc6G7W865BzLk6A-L_t8DU_PwmXfdF2wdo2rTkJmeAQH6OCxmEZj5VyvNzg4fnVAbaV1YwkjRyuAcDJrHCIuzP3DL2uP35vmo_ZUWSrEHl8BzCVZMfNNWjq7ozyAPnsWHkbb-HCsqNZ3TG3Gty6F52zinOmVrjFrngWlVakpWecbTjf5ad1vn3xC_nykMTXPozkjydGor3NECOgUwU7CHbH7GgEjxO71q5YCBYzZl4FZp568egSKNf8N1PmQXPrLqAZMtjw9lPIh2B10X0ibXWRNLStHIyhaUUqiCxHueKw_LUOxFIERDIC5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb118187a.mp4?token=EgXLH1qVSyPYBxTuqXMChCQcNMdjOG2HzwLGYRWI1LHWWSgTlcPu_mEphcGte560xhjaWhuen8PSmKpp4UJqzNq_NnE2K5hi-LL5b4AhjOFMEtMKe8c1BimSPHq994kwI-JllsTyqmS-ICx2Ue_7USYygDyJtEmG_dLzXKT-wTQ1q8YwGmICsbrTB52puN9VKirHDSXSIbjfJ4LspUrPiazcU2okOv1yghn_qJOGjs7g17AnHTUxheSjCE4FVIQh41v_575ixJJOXYkIvol8zPEbySXsrl5qMt7nICxKxrDV4xUG3_ssiBU3DIpFZLrA5xlx630vm1lf9rBBCGgCKTIWPi9_4aDO7zbTTaZvDwur6jGlsanc6G7W865BzLk6A-L_t8DU_PwmXfdF2wdo2rTkJmeAQH6OCxmEZj5VyvNzg4fnVAbaV1YwkjRyuAcDJrHCIuzP3DL2uP35vmo_ZUWSrEHl8BzCVZMfNNWjq7ozyAPnsWHkbb-HCsqNZ3TG3Gty6F52zinOmVrjFrngWlVakpWecbTjf5ad1vn3xC_nykMTXPozkjydGor3NECOgUwU7CHbH7GgEjxO71q5YCBYzZl4FZp568egSKNf8N1PmQXPrLqAZMtjw9lPIh2B10X0ibXWRNLStHIyhaUUqiCxHueKw_LUOxFIERDIC5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ایرانیان در نجف اشرف هم تجمعات شبانه را ادامه می‌دهند
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453441" target="_blank">📅 00:39 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453440">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a28822ab33.mp4?token=ZT_aEOnB5pvMVJvNG90B-sWfrzjNhqWHOjJQujFUZKDwF2PotfVl8LG8MsweB1QmKjRMwphN0typms9JL9FDoBnlBY2raXIRUKN7qLlox5q-jJD_YFve1ym1KO0VuLmMPN9Mkgi36Yt2nK123N3QugeOoq6ARmnoQDxITgkt2LfzxyQIccL7RttCBS3X4Rw8GZiaCBU9xPdqd9bDM_bcPvQ_sDR2V4pa2sYefvAwgehXIaR_IIm-J_bHZmd2U_lgp3dqd5dB6GHKkpeNiu38RYTEKYaEHHnvnum-PPlX7rvTQFWVdGsHEHwhWEYhaE4Sko5eVFfsqQ4c6tw-Lt2wqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a28822ab33.mp4?token=ZT_aEOnB5pvMVJvNG90B-sWfrzjNhqWHOjJQujFUZKDwF2PotfVl8LG8MsweB1QmKjRMwphN0typms9JL9FDoBnlBY2raXIRUKN7qLlox5q-jJD_YFve1ym1KO0VuLmMPN9Mkgi36Yt2nK123N3QugeOoq6ARmnoQDxITgkt2LfzxyQIccL7RttCBS3X4Rw8GZiaCBU9xPdqd9bDM_bcPvQ_sDR2V4pa2sYefvAwgehXIaR_IIm-J_bHZmd2U_lgp3dqd5dB6GHKkpeNiu38RYTEKYaEHHnvnum-PPlX7rvTQFWVdGsHEHwhWEYhaE4Sko5eVFfsqQ4c6tw-Lt2wqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
زائر اهل باکو: آیت‌الله خامنه‌ای تاج سر همه ماست
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453440" target="_blank">📅 00:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453438">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8d9721669.mp4?token=XBgCylfCTXUbrKRSBnYZrUklAED15FrZIOk2eYooDpjF6SQrZV2qES_8yqHMcILLm6uee8MHNIxf-wsPoPulEBQYQT45zVbpFSlkVvDiqNKjGXtjxJvxkhb5djjq_45e3E4dbYXCNm2-OSt8TJX0EoUSZkBgZwF_DCivw6iuq0kZyUWqrw5n0-HAlAhntSWvqd4HHeXcTWTr0IJf720BOIhXAZdrXk8CLer9npNafIzxaOCn3KJ5Mve4HXd-piUt_uReK8DG641U_dpUBnfjA-rKdhFpFMskQZ2FRJKLZ6ILik8-y-RCpdGv01rbCIefFRvyX3yZGN4VkWW8sbTla0KnCMOtyIua-H0Bg89DcRg1tQQC-y43C53r9U6frgfsO_S_cuLEIuHoNyxazKlXn1aUOVWWvU55ftWj58Jx-vBizPOeT0IZbXQ7_KrYM3BvACFFsoWlDJaPYQNE5lAeoJNHb-OWnVFQwB9CwUsRVFjTcP3YyIVqV_bYhExmPjryRitOv87Z6dI4KhvI7B_xP80JRL1ZsPuWm2NdihevL94BqiFf24_KcfzJx9aAw4uPthB5QXxRM64MxjsYWLyQAPp308if2B_XOuB3biNhDnLeo3p01fD4z55lwIvMRa70wwqFMyaBqhwlfVempUuIU__HwklNh7zbpR0DvYqjPe8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8d9721669.mp4?token=XBgCylfCTXUbrKRSBnYZrUklAED15FrZIOk2eYooDpjF6SQrZV2qES_8yqHMcILLm6uee8MHNIxf-wsPoPulEBQYQT45zVbpFSlkVvDiqNKjGXtjxJvxkhb5djjq_45e3E4dbYXCNm2-OSt8TJX0EoUSZkBgZwF_DCivw6iuq0kZyUWqrw5n0-HAlAhntSWvqd4HHeXcTWTr0IJf720BOIhXAZdrXk8CLer9npNafIzxaOCn3KJ5Mve4HXd-piUt_uReK8DG641U_dpUBnfjA-rKdhFpFMskQZ2FRJKLZ6ILik8-y-RCpdGv01rbCIefFRvyX3yZGN4VkWW8sbTla0KnCMOtyIua-H0Bg89DcRg1tQQC-y43C53r9U6frgfsO_S_cuLEIuHoNyxazKlXn1aUOVWWvU55ftWj58Jx-vBizPOeT0IZbXQ7_KrYM3BvACFFsoWlDJaPYQNE5lAeoJNHb-OWnVFQwB9CwUsRVFjTcP3YyIVqV_bYhExmPjryRitOv87Z6dI4KhvI7B_xP80JRL1ZsPuWm2NdihevL94BqiFf24_KcfzJx9aAw4uPthB5QXxRM64MxjsYWLyQAPp308if2B_XOuB3biNhDnLeo3p01fD4z55lwIvMRa70wwqFMyaBqhwlfVempUuIU__HwklNh7zbpR0DvYqjPe8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
روایت فرزند شهید تنگسیری از روز شهادت سردار دریاها
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farsna/453438" target="_blank">📅 00:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">توقیف ۴ شناور قاچاق‌بَر در آب‌های بوشهر
فرمانده مرزبانی استان بوشهر:  با اقدام مقتدرانه مرزبانان در آب‌های خلیج فارس، ۴ شناور حامل محموله بزرگ قاچاق توقیف و ۶ نفر قاچاقچی دستگیر شدند.
🔹
ارزش ریالی این محموله‌های قاچاق ۲۰۳ میلیارد ریال برآورد شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farsna/453437" target="_blank">📅 23:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453436">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575a64f54a.mp4?token=khufEf3-QN9KCaGCrqOEAIFE3biBvJslo0XtgWJd_meKKtiKky1-Ty6Z_zC5R3qRW8m_LPPs4PhRUMnyeNCLwGsusxs93EjPTc6MFnbuWJUT_k_ZsGpoc4jJnz7u0mRhTEhcqHofg_X7O7bS6mcF-6uHZxzqJTwp_hMvwkh7P1Pmb0kV6d7u2tqei2jICTd_8ZEeD_YvSL4em_o81Uuy1fJhSBh3HyasGT7v94b5Fw_BD75LdpFm1dyKl1wMM5t87CejPJJTt1crByYYFbfH3G-VdncDWMz50l3lFjwdrGrXCq9UaTIG03ZD-aeN7KJiLgxUdaEDZqHmBp2QzzORzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575a64f54a.mp4?token=khufEf3-QN9KCaGCrqOEAIFE3biBvJslo0XtgWJd_meKKtiKky1-Ty6Z_zC5R3qRW8m_LPPs4PhRUMnyeNCLwGsusxs93EjPTc6MFnbuWJUT_k_ZsGpoc4jJnz7u0mRhTEhcqHofg_X7O7bS6mcF-6uHZxzqJTwp_hMvwkh7P1Pmb0kV6d7u2tqei2jICTd_8ZEeD_YvSL4em_o81Uuy1fJhSBh3HyasGT7v94b5Fw_BD75LdpFm1dyKl1wMM5t87CejPJJTt1crByYYFbfH3G-VdncDWMz50l3lFjwdrGrXCq9UaTIG03ZD-aeN7KJiLgxUdaEDZqHmBp2QzzORzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شهدای ناو دنا، اهداکننده خون بودند
🔹
خونِ شهدای ناو دنا، پیش از آنکه در راه دفاع از ایران بر زمین جاری شود، در مراکز انتقال خون به بیماران جان بخشیده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farsna/453436" target="_blank">📅 23:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453435">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZQca5uoLhQxvvzFr5z3l9Aho7HdGzcf5Jyupm1q1nFpwZUvB31-gGeW_6vw1aqcImgeyAE-ttJjeRybB5TSMITHEXTTrgjrjlVYzik1vEIPUKhrmJ6WUz0u9-Gc7XAviUL3kqzhSU3CnSrsYu6ZlsszMnqMpXkh5HjMWmYFhQLYRTIrkwDMTEi_J_Q_hmrL3m6bWKg1ldrQCF3r-IpumdNP2aOIRQCHo_KX43qVoW9R02EDDOCq5UaKyWjP_GQ7b_GDHPLbcQQ46xyUF1TO0sY4YuPjPtlesoTmemlabEmarKOyO9M7A-x8CKEP0_Dbkml1B5h7YXHm-0qym-pyPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: نوبت ما است که ایران را بزنیم
🔹
رئیس‌جمهور آمریکا درباره ایران گفت: «آنها را بسیار شدید خواهیم زد چون نوبت ما است که آنها را بزنیم. می‌دانند که حمله در راه است. از ما درخواست می‌کنند که این کار را انجام ندهیم.»
@FarsNewsInt</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farsna/453435" target="_blank">📅 23:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453434">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">روابط‌عمومی سپاه: بستن حساب کاربری ما نشانۀ وحشت از داده‌های دقیق ملت‌های آزادی‌خواه منطقه از مواضع آمریکایی است
🔹
ملت شریف و آگاه منطقه، امت بزرگ اسلامی و آزادی‌خواهان جهان!
🔹
پس از آن‌که مردم غیور و شریف کشورهای منطقه، به‌ویژه برادران و خواهران عزیزمان در اردن و کویت، اطلاعات ارزشمند و دقیقی از تحرکات و پایگاه‌های رژیم آمریکایی را به حساب کاربری اعلام شده توسط سپاه پاسداران در تلگرام ارسال نمودند، دشمنان مستکبر نتوانستند این موضوع را تحمل کنند.
🔹
آنان با بستن حساب کاربری روابط عمومی سپاه، بار دیگر نشان دادند که از داده‌های دقیق و ارزشمند امت عزیز مسلمان و هماهنگی میان ملت‌های آزادی‌خواه منطقه، به وحشت افتاده‌اند.
🔹
بستن یک حساب کاربری، هرگز نمی‌تواند صدای حق و اراده پولادین ملت‌های منطقه را خاموش سازد.
🔹
به‌زودی درگاهی جدید، امن و مطمئن برای ارتباط مستقیم با ملت‌های آزادی‌خواه جهان معرفی خواهد شد تا مسیر تبادل اطلاعات و آگاهی‌بخشی، مستحکم‌تر از گذشته ادامه یابد.
🔹
تاکید می‌نماییم که مسیر مقاومت و پیروزی، با اراده خداوند متعال و همت امت اسلامی، بدون توقف ادامه خواهد داشت.
@Farsna</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farsna/453434" target="_blank">📅 23:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453433">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c1d107d0.mp4?token=rIPDfQjaZFcHLBKU8TGVzWJJBdePsTuBZt6T1TzcJxVUOCJjTN7b4OhoXFBvjWcSBfpRZyRjzcnYxkWS4K9s64H7udlCk_HQGPJ_0t1GaLCl4WraMPnrpf9eH1lQnMVDbmQelw6vLP3r4qAFJPjcpAjdyXA21qyEiQnG8f3fYvU26OZTU8ieqvNVfMEEXpOL0MfoeKT1kSWjr5e1IQtDqXcwYQCf4mw4AqmC_fsb9NU6sUEGHh4CEsvs9oVOrKJHgxCGKJdKTkcYD0qlK7Kl6YQMAjSlXLnr90GfEWd18JVaLOlEPil7IA_emYxI1PMML2qUhpU2xsnZH5d-W43HoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c1d107d0.mp4?token=rIPDfQjaZFcHLBKU8TGVzWJJBdePsTuBZt6T1TzcJxVUOCJjTN7b4OhoXFBvjWcSBfpRZyRjzcnYxkWS4K9s64H7udlCk_HQGPJ_0t1GaLCl4WraMPnrpf9eH1lQnMVDbmQelw6vLP3r4qAFJPjcpAjdyXA21qyEiQnG8f3fYvU26OZTU8ieqvNVfMEEXpOL0MfoeKT1kSWjr5e1IQtDqXcwYQCf4mw4AqmC_fsb9NU6sUEGHh4CEsvs9oVOrKJHgxCGKJdKTkcYD0qlK7Kl6YQMAjSlXLnr90GfEWd18JVaLOlEPil7IA_emYxI1PMML2qUhpU2xsnZH5d-W43HoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شعارهای جالب کودکان نیشابوری در تجمعات مردمی امشب
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453433" target="_blank">📅 23:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453432">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58d6fd193.mp4?token=SxVmSX0XJM1P3z4G26P2Z3GzgRLITkjfzlZOP_YQKqHy-GC9bkwxLupI1wuITPuDSagjnjhprcz-Pwa7tu2vI1E8wHyXcWPde4l52-IbBdoAjNiuRVwRVr6S1A_gnClGUP9Nx_JYF0Ra-6vKsgj-KMTAzJO-dUIZSWqtSBfYMuzIQZmxOXpCw73652VYVPFQ4o0hHVOg2dZSuS47eH_6ZEEqLXgukH-gut9x4xdbA2gKDfUqyThB-STZtZ0dhJVCLkWC7IRWE-mOT2S4wcRqf0Q7LXJVjomGGVO5ul7splA9W-lKNhw9KS9p9er24ZJctHZ2gioCqnnqrQlzvuNoSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58d6fd193.mp4?token=SxVmSX0XJM1P3z4G26P2Z3GzgRLITkjfzlZOP_YQKqHy-GC9bkwxLupI1wuITPuDSagjnjhprcz-Pwa7tu2vI1E8wHyXcWPde4l52-IbBdoAjNiuRVwRVr6S1A_gnClGUP9Nx_JYF0Ra-6vKsgj-KMTAzJO-dUIZSWqtSBfYMuzIQZmxOXpCw73652VYVPFQ4o0hHVOg2dZSuS47eH_6ZEEqLXgukH-gut9x4xdbA2gKDfUqyThB-STZtZ0dhJVCLkWC7IRWE-mOT2S4wcRqf0Q7LXJVjomGGVO5ul7splA9W-lKNhw9KS9p9er24ZJctHZ2gioCqnnqrQlzvuNoSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رجزخوانی حسین طاهری در موج ۱۵۱ تجمع مردم در میدان انقلاب
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453432" target="_blank">📅 23:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453431">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e819a74c33.mp4?token=V5QKf16XWDiuJcAy8EqoHRuqKlOOU-xloGGXIn4hm4tFPdXFBsxP0QfF7hs6P-3aoijcc8lo6mT5anOcsOB5wxMtdY7mHhqvPAIlEhegiEsQaAQUjIZc9TahOUrcKvUyIkNssKGFD_FKRZqj1YPo3Zh9RcgZ7XlkVM6IODOEeLAGdCYDFafqyD5gy93S5UhjN0NGhutoAvhgok-FES54RK71U-MfqnPO4d0tjOxFWzHpfNDRfBr0jBq3fZZrjUGpgs7SVvaD_wNpKq8l9FiZ99eKh2PRyxgplqIR1pVFORMa0FoLP7bZbiHBniA-Le3mYBb22P7emh69-C1WsU2Ztg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e819a74c33.mp4?token=V5QKf16XWDiuJcAy8EqoHRuqKlOOU-xloGGXIn4hm4tFPdXFBsxP0QfF7hs6P-3aoijcc8lo6mT5anOcsOB5wxMtdY7mHhqvPAIlEhegiEsQaAQUjIZc9TahOUrcKvUyIkNssKGFD_FKRZqj1YPo3Zh9RcgZ7XlkVM6IODOEeLAGdCYDFafqyD5gy93S5UhjN0NGhutoAvhgok-FES54RK71U-MfqnPO4d0tjOxFWzHpfNDRfBr0jBq3fZZrjUGpgs7SVvaD_wNpKq8l9FiZ99eKh2PRyxgplqIR1pVFORMa0FoLP7bZbiHBniA-Le3mYBb22P7emh69-C1WsU2Ztg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
امر فقط امر سید مجتبی
شعار مردم حاضر در پیاده‌روی اربعین
@Farsna</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453431" target="_blank">📅 23:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453430">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس اقتصادی</strong></div>
<div class="tg-text">مدیرعامل یک صرافی رمزارزی برای دلارهای صندوق توسعه نقشه کشید
🔹
مدیرعامل نوبیتکس در نامه‌ای به وزیر ارتباطات خواستار وام ارزی این شرکت از صندوق توسعه ملی شد.
🔹
نوبیتکس می‌گوید خسارت هک ۱۰۰ میلیون دلاری سال گذشته را «از دارایی شرکت و سرمایه سهامداران جبران کرده» و این موضوع توسعه شرکت را کند کرده است.
🔹
عضو کمیسیون اقتصادی مجلس میثم ظهوریان این درخواست را مصداق «خصوصی‌سازی سود و اجتماعی‌سازی زیان» دانسته است.
🔹
منابع صندوق توسعه ملی بخشی از ثروت ملی و سهم نسل‌های امروز و آینده از درآمدهای نفتی است که باید صرف پروژه‌های زیرساختی و تولیدی شود.
https://farsnews.ir/N_bourbouri/1785349176168704923/</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453430" target="_blank">📅 23:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453429">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFN1WciCS8_GXZbRsE7n6mr24RRs46x9OLFzC2eJGLW8oKJw-I8NlHxB4NMKKWUP2gs-nhCKKxWhNPBrVe-Ajg5XO589Iodo5PneDEoQcLO7MRJzdcmkbmEeaQnxse471Jhlduema8lmY9vhwAkA5-d33LtViYNhhCVBDmDTvNg4tFr88Go7fGOPwgS4eUskIDd6O3JvjGGRES23Pwr95dsFLUhm16JLPTVBbRxd_VBcxM6RNU-diLHS6kRwMV4M1Mpb_UIxZaHu_ZYd0seribhu5CMPWemFsuFyWJY9A1LlXLGqxRgQ9duZDgQxcysaTI9rzuVE18FbNtpmDgVF8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: آفریقا یک فرصت طلایی برای ایران است
🔹
معاون اول رئیس‌جمهور: اقتصاد آفریقا می‌تواند مکمل اقتصاد کشورمان باشد، اما متاسفانه در توسعه روابط با این قاره کم‌کاری شده است.
🔹
گسترش همکاری‌های اقتصادی و تجاری می‌تواند به هم‌گرایی بیشتر دیدگاه‌های سیاسی ایران و کشورهای آفریقایی در مجامع بین‌المللی منجر شود.
🔹
پس‌از ۲ جنگ تحمیلی اخیر ایران‌هراسی شکست خورده و اکنون فرصت طلایی برای گسترش روابط، به‌ویژه با کشورهای آفریقایی فراهم شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453429" target="_blank">📅 22:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453428">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6650ba10.mp4?token=dSeLzmf290cyCZZLkGhw5RlfcEelx2VjAQcQltBCrkVpqA-Dcv-bW94mGaoUFb37V2DIbdd0LKlMkBmLnFP_kxIpACKgxD-_ep2ko8-R9bcM0UqXiJz_JHz00v-rO7RGFbsLk1qW7xoIVD6nw3PjsCUOu5CFfB6xvkVwRZoNflCvYVLzECbQGSylN3ThyKpWrS1EAcdrejsHfPjKydu8axrqIbD6vSStW64IdO04wOktczUhDfhHTZjAHH55Y5vsgT5arSqvwRohIQHxT0vkj9sXnikdY6SMfFWZaeHhOsZYWxAq9T9pfOtE6wfPC9foK8rSdfCVwuVQI_hyo9j9Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6650ba10.mp4?token=dSeLzmf290cyCZZLkGhw5RlfcEelx2VjAQcQltBCrkVpqA-Dcv-bW94mGaoUFb37V2DIbdd0LKlMkBmLnFP_kxIpACKgxD-_ep2ko8-R9bcM0UqXiJz_JHz00v-rO7RGFbsLk1qW7xoIVD6nw3PjsCUOu5CFfB6xvkVwRZoNflCvYVLzECbQGSylN3ThyKpWrS1EAcdrejsHfPjKydu8axrqIbD6vSStW64IdO04wOktczUhDfhHTZjAHH55Y5vsgT5arSqvwRohIQHxT0vkj9sXnikdY6SMfFWZaeHhOsZYWxAq9T9pfOtE6wfPC9foK8rSdfCVwuVQI_hyo9j9Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
پرچم‌داری خون‌خواهی در مسیر نجف به کربلا
🔹
پرچم خون‌خواهی رهبر شهید انقلاب در موکب شهید حاج قاسم سلیمانی در عمود ۵۳۳ طریق نجف به کربلا برافراشته شده است.
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453428" target="_blank">📅 22:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453427">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b95f960222.mp4?token=M4nuJfBM0alvzWwS0MwgZ-QiLxFyu8czy_Vi3w0CGO16l2Qu8uIIoJ2Jsmf5GiD-kLEiLkWAJYwMyQpcD_gu1kckEsWsfNiIAtpfjSFAxjUYnQMuDjPDojKV0XZ4hWgiW-UZq1sVvl9MTtag3zZR4Cuc9kcmlO8WdKT8pGdn0veIEAiYXUAD5_Jhb_qtidtSNjFBSTo0SdmNvfT35WyTYt3l7zY7eP8sxIIdvLsAOW9TGTf5IeXZWfjfDCCYI3D533tSmvpo0bpky8494sr7cA3WmFzYPrx1V6qDLizmZUzNzjttHET_EXJM-K211ocLx2isEFX77y0ojgk0dVDL3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b95f960222.mp4?token=M4nuJfBM0alvzWwS0MwgZ-QiLxFyu8czy_Vi3w0CGO16l2Qu8uIIoJ2Jsmf5GiD-kLEiLkWAJYwMyQpcD_gu1kckEsWsfNiIAtpfjSFAxjUYnQMuDjPDojKV0XZ4hWgiW-UZq1sVvl9MTtag3zZR4Cuc9kcmlO8WdKT8pGdn0veIEAiYXUAD5_Jhb_qtidtSNjFBSTo0SdmNvfT35WyTYt3l7zY7eP8sxIIdvLsAOW9TGTf5IeXZWfjfDCCYI3D533tSmvpo0bpky8494sr7cA3WmFzYPrx1V6qDLizmZUzNzjttHET_EXJM-K211ocLx2isEFX77y0ojgk0dVDL3jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
موج ۱۵۱ میدان‌داری مردم در تربت‌حیدریه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/farsna/453427" target="_blank">📅 22:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453426">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0bfdd4de7.mp4?token=BUQFKMaNCukyDRBKqx-6jx3QkdO9-8JEKAK-CDV63Rkwe4N6bqQbYrPIzPOJkopUkwsyDefAoYkfI2YLI55n8Pn6cX1_ZLII1aLERpI6zbSX6ExwvKWp-ozuRawdB6Oi_2ybZFekMzb4UJOZ6N8h74WS5kZtwOO57r0L1KOz1BtLdo7N0epTXoY2zqNnxrpFawthHJMzNJmDDSyheqacCMXo06kCpdsHTe18Wb_NVCIIY1voyECE7BmD20wAnv4w5ibMxrNzyP_8MkJrv076prBz0Xs-OKwxc8yZ6tisoRNiGCDt6RjI8qjEys67i-eqOg5k-_6D8ThX2-NLeEVI_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0bfdd4de7.mp4?token=BUQFKMaNCukyDRBKqx-6jx3QkdO9-8JEKAK-CDV63Rkwe4N6bqQbYrPIzPOJkopUkwsyDefAoYkfI2YLI55n8Pn6cX1_ZLII1aLERpI6zbSX6ExwvKWp-ozuRawdB6Oi_2ybZFekMzb4UJOZ6N8h74WS5kZtwOO57r0L1KOz1BtLdo7N0epTXoY2zqNnxrpFawthHJMzNJmDDSyheqacCMXo06kCpdsHTe18Wb_NVCIIY1voyECE7BmD20wAnv4w5ibMxrNzyP_8MkJrv076prBz0Xs-OKwxc8yZ6tisoRNiGCDt6RjI8qjEys67i-eqOg5k-_6D8ThX2-NLeEVI_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سخنگوی شورای نگهبان: در جنگ با دشمن نباید مشغول خود شویم
🔹
در پیام رهبر انقلاب موضوع وحدت چندین‌بار مورد تأکید قرار گرفته و طبیعتاً هر اقدامی که ما را مشغول خود کند، عملاً به نفع دشمن خواهد بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farsna/453426" target="_blank">📅 22:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453425">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9246e47830.mp4?token=fBAP8dGRSzczvEqTJ2nDK0KpQW2lSM3K15VBsJrUcNzN5WEgPDvYGWwJL0wUAFCusd4ruKgjniArJ58kN0B1x-jfKl-Kqr0rrGQbwOQgPeII3PcnQDBc2UUwTeqP6heM6MYkyIyxLK5ty9s2ApdG6pSuDQMOtYjvPYE2pnrbOipX38NSBhhLOay0Px5sXc3y8xQM3Jcu9-WLRVW_qjaa4ZMNk3OkKfIiYRRFcF2eBZjS93_Tr1Sm7UaEjv_mnEqYzy9IzVxQ6kocVP1TQkah2owOsd9lnRD_VZGcnaqo45xu7N_VR2Z3mokMr3FnjGHf2s8ReSl7E_24uCo7KEFoJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9246e47830.mp4?token=fBAP8dGRSzczvEqTJ2nDK0KpQW2lSM3K15VBsJrUcNzN5WEgPDvYGWwJL0wUAFCusd4ruKgjniArJ58kN0B1x-jfKl-Kqr0rrGQbwOQgPeII3PcnQDBc2UUwTeqP6heM6MYkyIyxLK5ty9s2ApdG6pSuDQMOtYjvPYE2pnrbOipX38NSBhhLOay0Px5sXc3y8xQM3Jcu9-WLRVW_qjaa4ZMNk3OkKfIiYRRFcF2eBZjS93_Tr1Sm7UaEjv_mnEqYzy9IzVxQ6kocVP1TQkah2owOsd9lnRD_VZGcnaqo45xu7N_VR2Z3mokMr3FnjGHf2s8ReSl7E_24uCo7KEFoJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
۳ کلید طلایی برای سفری امن در پیاده‌روی اربعین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453425" target="_blank">📅 22:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453424">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d4522cb2d.mp4?token=UCLze3Ly56VSOFEd8hZ5Zzzvc0MCoVua6QTGVn9_3WQR7H9WEthwROoXFgcNDLkL6IuTwNQD3_tBnTOfX4mC11-QKar26vFVWLcKq2Bi3r3FW2TlwEJyt6f_bFstyHqsHpMH5xRFFR5bUt4HyCCem_unADZtoClObW51VUH4Kce6v025bHQ_vPmoC1YPpbe0-OnNht1gvMDyQTuzakDf6jX8vm0CdXWGKlih5PQ3aidJIguYypgSGfkH7CooHkE8SAJfs0FD3JlMgzRyW_Obrwqrz9z8DQ4VIZ5yC8oZVoykhiJLwGZ_Nvq3c-mZj80ZA9se5tsIwlZWF3b3wuLaGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d4522cb2d.mp4?token=UCLze3Ly56VSOFEd8hZ5Zzzvc0MCoVua6QTGVn9_3WQR7H9WEthwROoXFgcNDLkL6IuTwNQD3_tBnTOfX4mC11-QKar26vFVWLcKq2Bi3r3FW2TlwEJyt6f_bFstyHqsHpMH5xRFFR5bUt4HyCCem_unADZtoClObW51VUH4Kce6v025bHQ_vPmoC1YPpbe0-OnNht1gvMDyQTuzakDf6jX8vm0CdXWGKlih5PQ3aidJIguYypgSGfkH7CooHkE8SAJfs0FD3JlMgzRyW_Obrwqrz9z8DQ4VIZ5yC8oZVoykhiJLwGZ_Nvq3c-mZj80ZA9se5tsIwlZWF3b3wuLaGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس بانک مرکزی: از ماه پیش ترمز تورم را کشیدیم
🔹
در تیرماه نرخ تورم ماهانۀ ما نسبت به ماه قبل تقریبا نصف شد. این نشان می‌دهد روندی که برخی فکر می‌کردند در آن تورم بی‌محابا افزایش خواهد یافت کنترل شده. در ماه‌های آینده نیز کنترل بیشتری روی تورم خواهیم داشت.…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453424" target="_blank">📅 22:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453423">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6916d586f0.mp4?token=oov96QEVPpeOR8yPLEtot3hojut778mhVOpYSMRe5WOC0U_QY0qXKMivaMJSkOXirAV0idxKKev47d2C4efBF1FOt39s1PgLK63FzsMKiStUEumPHGvvz0Rveo3y6dcdpIQ802OSRzlhnjSWV1T0HpVS6diSGgbhtkQlJqAGkd7UwYuLPBkvP1ZonoVAf3O_oZnwucmfkZFJbxvimUTVTHp7XmVo84RgvfA72Fk_D9kvsK4q8PMHLGOuTSZPDJ7ls3y422ZmEfya1cZrQ1_orxW221uh_jlJEvRU83rdOhCowsJFeWtBUl6RqNVEbAqQsG3i_hVVMHpuDXFUyLtTL52jJz4FPBCbg0DiJp3xQSjbZWDH6Ht-rSvGxEGPJxuXRZ2YDu9i3Jjeiupng7UgONjurE7DcMHq1DqAIqlU6J0JGVVAqBgfSnGewJL67lOvThl8x2maDG_YjoKdIgT2XQa8cyRta7VJ8eWaxEe-QIfZwbPteyOtvRZzx5aAV_SgKJKeBo9vZm9pweOPlh-8RuNEEIgJ4i5AMXVm0qsUoLrBWe5czLybs3ZL06iFJiFwzvH5fvv4_dLJgiraa3_6DO8Hnu6CSJgLQwHtpBYrD4n31F-TbHMbfaEZH6vBMch0WX4qRIOYTAmvNEZFeCCerqvYDRTCgkqvaVtS7hvkKCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6916d586f0.mp4?token=oov96QEVPpeOR8yPLEtot3hojut778mhVOpYSMRe5WOC0U_QY0qXKMivaMJSkOXirAV0idxKKev47d2C4efBF1FOt39s1PgLK63FzsMKiStUEumPHGvvz0Rveo3y6dcdpIQ802OSRzlhnjSWV1T0HpVS6diSGgbhtkQlJqAGkd7UwYuLPBkvP1ZonoVAf3O_oZnwucmfkZFJbxvimUTVTHp7XmVo84RgvfA72Fk_D9kvsK4q8PMHLGOuTSZPDJ7ls3y422ZmEfya1cZrQ1_orxW221uh_jlJEvRU83rdOhCowsJFeWtBUl6RqNVEbAqQsG3i_hVVMHpuDXFUyLtTL52jJz4FPBCbg0DiJp3xQSjbZWDH6Ht-rSvGxEGPJxuXRZ2YDu9i3Jjeiupng7UgONjurE7DcMHq1DqAIqlU6J0JGVVAqBgfSnGewJL67lOvThl8x2maDG_YjoKdIgT2XQa8cyRta7VJ8eWaxEe-QIfZwbPteyOtvRZzx5aAV_SgKJKeBo9vZm9pweOPlh-8RuNEEIgJ4i5AMXVm0qsUoLrBWe5czLybs3ZL06iFJiFwzvH5fvv4_dLJgiraa3_6DO8Hnu6CSJgLQwHtpBYrD4n31F-TbHMbfaEZH6vBMch0WX4qRIOYTAmvNEZFeCCerqvYDRTCgkqvaVtS7hvkKCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
از شجرۀ طیبۀ تا شلمچه
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453423" target="_blank">📅 22:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453422">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb1f33ae39.mp4?token=TTtgXV4C8tlGEAjqoaU4A64jGYRkK4VyqhwGsB7drUIi02rEWoi-4iO4qgThV4_e4P0V5_UWzh2dr1oHnnbyYKH5JH3DHBsRSAt4LE3g4HMM1QP-iJHClr7NTbohihgZmm7FXL0zOZ1ZhTrLqPRRFkREr47kbyGfLKAtbHBz-n_ALMPh-wOMElg_8MatT2as-UKTo1MVwF1E7L0_CHh3LWxOfoZlCq2nomuCsd-aDCHom2m5hMxvE_nrGZoeGRwVp8g73Ww6AFczTFJz4XVCZlRHzBbiyHmXCPn9WFhJW4P7ngvr5ezcNbfKAo1m0vyN_cUkzzDlgdxrZUZqDucCaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb1f33ae39.mp4?token=TTtgXV4C8tlGEAjqoaU4A64jGYRkK4VyqhwGsB7drUIi02rEWoi-4iO4qgThV4_e4P0V5_UWzh2dr1oHnnbyYKH5JH3DHBsRSAt4LE3g4HMM1QP-iJHClr7NTbohihgZmm7FXL0zOZ1ZhTrLqPRRFkREr47kbyGfLKAtbHBz-n_ALMPh-wOMElg_8MatT2as-UKTo1MVwF1E7L0_CHh3LWxOfoZlCq2nomuCsd-aDCHom2m5hMxvE_nrGZoeGRwVp8g73Ww6AFczTFJz4XVCZlRHzBbiyHmXCPn9WFhJW4P7ngvr5ezcNbfKAo1m0vyN_cUkzzDlgdxrZUZqDucCaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
رهبرمون هرچی بگه همونه
شعار مردم در پیاده‌روی اربعین
@Farsna</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453422" target="_blank">📅 22:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453421">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d9c20a073b.mp4?token=HdGbxydUasV_HWv1upNXi2tbEWaWRuTwGvkbR5JX5I07i55NLRiz0jksiGeh1hH6eXmMKgtDuJjKTXT_aHKNkWh6RcJ4QESKl5k7h7uewl3ukNF3ce-GDH9ygarBXbodcofx_Kv6q9HMeJqHP22F6XPDIg2ndvGX5VraX__P5c7SyMubDqREgK0cikVcxz_ZkEczre7XiZb7Fbr2shK4amE6qkoXIyXfoAl38im4jatNKapOnBExzW171MgR_Zbo6D3EmNFddw9CSElu22jc0zGEFhuURZdc301vWZFklnaC_DLXDtobvEZEbUc1_deW-ZxEi5fUemt8KbPwo-FS3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d9c20a073b.mp4?token=HdGbxydUasV_HWv1upNXi2tbEWaWRuTwGvkbR5JX5I07i55NLRiz0jksiGeh1hH6eXmMKgtDuJjKTXT_aHKNkWh6RcJ4QESKl5k7h7uewl3ukNF3ce-GDH9ygarBXbodcofx_Kv6q9HMeJqHP22F6XPDIg2ndvGX5VraX__P5c7SyMubDqREgK0cikVcxz_ZkEczre7XiZb7Fbr2shK4amE6qkoXIyXfoAl38im4jatNKapOnBExzW171MgR_Zbo6D3EmNFddw9CSElu22jc0zGEFhuURZdc301vWZFklnaC_DLXDtobvEZEbUc1_deW-ZxEi5fUemt8KbPwo-FS3zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حملات سپاه چه بر سر پایگاه‌های آمریکا در اردن آورد؟
@Farsna</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farsna/453421" target="_blank">📅 21:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453420">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vq2tg0XmptoX2y1cZhGo-dLhwdtlApFuq-tUzfL958GvOjF7qR0Qkqv0ZM0GI_nSUNgldt78W60pGgBYOJjq-u4Gmwox6DPrhaHFJiwKyUAOlLHy8g-z_EW4gxv0M5MyEYVTkdOGMbcc1eKPs6Vql89ReCm_YZHf69TXDJ2kxY1OYnHxk1TsH3yvdYVRL5F4mcDMV1PYkTJXND0JNcC1n7gMC1ccPYdfLOYMDEHDwSgwdet3qctAmkHyf0Nt045vQMFggoGYgVF7WZh5_PVeT-FW9qqrGInBKycgjxHKqEZONHu0pdawVWLg1KFBpbouhDKSFamAdL4yRMxSvLB4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎥
جزئیاتی از چند مأموریت غیرممکن نیروی هوایی ایران  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farsna/453420" target="_blank">📅 21:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453419">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/94ad19ca82.mp4?token=ZKXsOukdlPnaz08tx2YOgBRNWqb3r6tmAhXEN17A0Thhtp2XSVmsElu-pU6B78Dezuh1ZJwZ5Ig5BKjQnHUdxkG0IOBHrzV3yVBysNoHrp0xzN8CfYF4YQ7bNDLaIv2cYvQVQS86EAiKPLMGb-A5EV_MI0mj93PEgkmBCVPTbXHIECbRvcWRvG5wSKX4rbN9QJJmXRr-eA68bH1QpcBrTPjWwcMoJRCJwXkxTDgvHtkKLoPl55qUsBa_nR_kUuNWcTdyWQU_CS2_Dh-9vvU7L5vpn6FmF-nOvmTSEItvebDU01Sq6_0h6cmx0hSINM0-Ump3AeFaX34k-ki-CxleGa7kIhTK5141AcXpOw8XetgZWyjUMU_Ms6b9nxeocfg26fOrXEFCc0WREkRTvH01MaZf_yXMSj-vmb0CENMTlQITTiP45mYu1HoSyUfeDz_9LTHK_ymYHqTdX4agzaLXNWnBzNADqK3AgL_DiGVGSfxcq5odCV3oz28wKSPXK2pImU4GZp1M2DI_-Fvp17z-IkIdy2rtoSELi6gvoktTEATaUTzs9E6ZwIR_sZ9KHtbkO3i32B2y7JfGODcjdWBerZUe5qDwT_t8i1-WcYvU5sQmeI5X5DTbc1FtW9UhEX6OoiYu93-5IEJ8Syg301DZBAGTR_hv0oKn2LnO1GdTTrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/94ad19ca82.mp4?token=ZKXsOukdlPnaz08tx2YOgBRNWqb3r6tmAhXEN17A0Thhtp2XSVmsElu-pU6B78Dezuh1ZJwZ5Ig5BKjQnHUdxkG0IOBHrzV3yVBysNoHrp0xzN8CfYF4YQ7bNDLaIv2cYvQVQS86EAiKPLMGb-A5EV_MI0mj93PEgkmBCVPTbXHIECbRvcWRvG5wSKX4rbN9QJJmXRr-eA68bH1QpcBrTPjWwcMoJRCJwXkxTDgvHtkKLoPl55qUsBa_nR_kUuNWcTdyWQU_CS2_Dh-9vvU7L5vpn6FmF-nOvmTSEItvebDU01Sq6_0h6cmx0hSINM0-Ump3AeFaX34k-ki-CxleGa7kIhTK5141AcXpOw8XetgZWyjUMU_Ms6b9nxeocfg26fOrXEFCc0WREkRTvH01MaZf_yXMSj-vmb0CENMTlQITTiP45mYu1HoSyUfeDz_9LTHK_ymYHqTdX4agzaLXNWnBzNADqK3AgL_DiGVGSfxcq5odCV3oz28wKSPXK2pImU4GZp1M2DI_-Fvp17z-IkIdy2rtoSELi6gvoktTEATaUTzs9E6ZwIR_sZ9KHtbkO3i32B2y7JfGODcjdWBerZUe5qDwT_t8i1-WcYvU5sQmeI5X5DTbc1FtW9UhEX6OoiYu93-5IEJ8Syg301DZBAGTR_hv0oKn2LnO1GdTTrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شما روی این کاغذ نام چه کسی را می‌نویسید؟
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farsna/453419" target="_blank">📅 21:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453416">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">بسته خط ۱۰۶.pdf</div>
  <div class="tg-doc-extra">2.8 MB</div>
</div>
<a href="https://t.me/farsna/453416" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">بسته خط ۱۰۵.pdf</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farsna/453416" target="_blank">📅 21:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453415">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxSyOcnLtJ4YgTgIxwyMU_s17KnwLuklK6c1Tz3qj58DuJGoToSG89I358e9slEL1GqQP_5q8Igzgc-DzLPXGq4uLLykZANM2MCWektPvjJLluD2ew1ViKLbEMIjR-Ifj-pL1lG59CbHtxsFk_QniiszgzZKSq_wQnMb7MwFIVKStcb3x_IGFyV8K0Qs5OZmxvhxysXLymCeJpMu9esaxC5yMsu4UclEbXRkkEOFS5Jk44EEW0_q8Sa8fJcyJ4NQFhpT7cSWDxZa6hwY8-0NIhuAxKbC2r3jUdcSoMkw06_eN3jksTQJfr0JhQqQYQNOK3atLlEmuRaV4KwLCjciBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزئیات برنامه‌های وداع، تشییع و تدفین ۲ شهید بسیجی در مشهد  دوشنبه:
◾️
مراسم وداع: همزمان با نماز ظهر در رواق امام خمینی(ره) حرم رضوی
◾️
مراسم وداع: ساعت ۲۱:۰۰ در میدان سلمان فارسی
◾️
مراسم تشییع: ساعت ۲۲:۰۰ از چهارراه برق به سمت حرم رضوی   سه‌شنبه:
◾️
مراسم تدفین:…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farsna/453415" target="_blank">📅 21:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453414">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند.  @Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453414" target="_blank">📅 21:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453413">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
منابع عربی: نیروهای رژیم صهیونیستی درحال پیش‌روی به سمت دره الرقاد در خاک سوریه هستند؛ همزمان توپخانه این رژیم حملاتی به حومه غربی درعا دارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453413" target="_blank">📅 21:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453412">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔴
منابع عربی از شنیده‌شدن صدای چند انفجار در سلیمانیه عراق خبر می‌دهند.
@Farsna</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453412" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453411">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnwsPM9bdGfNnz9HpwiGNTd6X4bno7ZTHw2kyyVPDhuHPnbHOrY6LPpPcm9AxCaZDj6R1FnOVwkPLkiC062dRWOxP748wpauYmVqInWPLwsxhz7D-PKVFDxIin6ekchunDleDe-YiIV5HWEaSZg-k9QLhdxEaQEYS_b-v9iKs0S1aJ6564p8CrTAto9hp21qabK5H7F2l_rA_5NHvROAm4UjhzDhLVqaNlzVa_9Vt8cfyVmrRqWRctTjEFzqM6y7cgdEDxYxT-igWMIJHDlI2G8FmcZlzZZ45Y0Rzna7NfZH407SPl0Xxyl6lSMvvKtrVthR_pQ7teYQLbypH3Guuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامۀ امتحانات نهایی برگزارنشده پایۀ دوازدهم ۴ استان جنوبی
🔹
امتحانات نهایی برگزارنشده پایۀ دوازدهم استان‌های خوزستان، بوشهر، هرمزگان و سیستان‌وبلوچستان در روزهای ۱۵، ۱۷ و ۲۰ مردادماه برگزار می‌شود.
🔸
امتحانات نهایی پایه دوازدهم این استان‌ها که قرار بود از ۲۵ تیرماه برگزار شود، به دلیل شرایط خاص جنگی لغو شده بود.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453411" target="_blank">📅 21:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453404">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YEUlQXZP7J06SBFAxkxMx5rJpLMD1H4AqKlyk8GgWIFeJl-gtK-rkVZcANh2_3cST7zdIGpSvQTrR-Z0cBcluv3Aa8jUu1qI7fk8xdDHBtmo-sXD3nYrsNwmZkoxZSJStnAYocdCalSTrBNaObN1hoTTSEoF-yCsQ9AtAr_k4nrU9QF6xmnBgnl5DS_96dP-7eoD8dlJ8Vie6eJF8umpCnw9ioN1-g05I8GC2bfaVVv92IqZdY20T1KJgO6J1cleQD4fUcrF7vX8nmtyQFyHCNcqLSl-pM7Q_KBNBJ8NPsq_P3gKobmADnhrjHWjkL3224uaaiWyEmEzat1aEwyLHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/njyKmE3RSLD6qstcT1rASteTvKdYvhH1jXZpmlNwBhfNoT7k2rIOhXDTCw-K4Oc1JKXS6QaOCY0dYcH6-480FxtBCubAwOf9G1jc0l-Tlt9ZxtY9n69Nbz7tc37GrdQSaTuySwc3uaFeJ6baSELrdbEGn4MQ36PssSf6UEbJLXIG8-40B2pcVEz1pMdfiC-FzGgR7cXfx6_LltDk7AxiQ3G6AABrmBEr-3l3K3yJbqb5BVKlJnrUYCgrJJb4_yZ6-aMVQvMBlfRz8u4G8EAbI_4WWcWtYqp77Tz2vrdf5J2PC4PtgkVyies7mFTz9_hQhR9OuJedV3CapUvvjzyy4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5HWajHq11f1cz1ZyJHm4oU6fK4eaVKdjljV8Crj84Fv69V9Ezt3N4oZ-f_gbTg_Kj0U6HPUM6OGAm5e6t1FwgVLFJ_Ohhv-HVyhzA8P8yIWZcV-1yVrd5s-CtVGpK88jx3fv6GJhY3i38LpQh3Fp0fww6MIRneA8Twht5Ax34sE8W6HhK92t-Ar9K0prqwpAbN_pNzlvpvYeNbRF6c10YUJWzkXCirA-DJNqe81ejGR_G4dSpdv-DcuLiiQe4TZBvqK9czYtglAtYCTqROko16L7HNSMHDV7G8gvuuIfIkiRDt_gZL4bfFQy6CojJ2Iv9RtCVGv82fSz8bw9xwnxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WeGUJpe2qYgqwtHDwHkTkjt8M2ifHVcY1c6y1HXN5TyKJ_TIoQFa8scgUjGE4wFOxD5l0xGsxvfQpoLoc8jz8po_XjSnuuJ3PLJNVWXXHNnwIp07egh-hM1LHsnokgN4NMBr7PW-fQ2rKpkiuK-lWYnsshW5xEJLm0GSvq5z44KFR-Bbd5RPoyXSPJKPUmVOJ-XpuFxcdBOkbiHJeyZUuwJt9GPEaHOGeUzeD1azWkv3B0oeB5NvPPMw4OlaMvXSYZzQbotXKHbbA0oY49X_SZQr9s71px3yua5ve0aby3jn6WqjJxoskvRsAzTVPD067c2GJU3izIUghtW6wl9_9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KTaRkXCHhxFGfEO5ND1d8qSWjRN_Mrvsl4-Mr1oS01WSa8LRhQs1o-tWDgsdvMIW0UYtDh2cBZkqGfLGa7vwgtFLFSD8xJv_vzC7jPxa87xfTmiGkhYZ5XAIOsPyGMIjGEB6ogH6PyUxBU6yT2G6z1WwuffhYH_ozt1O3Il-iePzn__w5_liDp1XpLa6zAEdzo4c1tkYyr9EoqEAOV6PmULdGDaJbPL5fU15ebFz0FkjLD-I_OSoZi4pLDkD-l4aD6k-x_KTVvGHxuzq6kaRVjUcRG-7i45m8bsVfcI7sjzztm01fANba6PmJjgeY5TzaeVd-jc-mPTSJvDCcB7o0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGfjmDD5lNNo_sHopCJd7fLfT9Cvbw1ijxHLVhe4Nrp1ggqKVkxJWS5ft_tV3O3kv41ezdccH-AF1RAKTK9ynQvvB-_DLE7rxG2ON5SEiF4bHhUM_RTBEG2pDyF5RGRq0n0f1NjPITjEdGqdgt6LlKD9UnS_nboRKs_KhXG3Z5OGnyXX4x8xGIbNdlA_51ihacrz-2PRDhAKo-hcZz566Hqq1pB-v3ZA7DKKpPjIevtFuw-J6FNcj-OEkRF4o-E3pef-aYRGNguNh2WBdJpZfD1yitDY_DvC4FmnKC8beox6WQYrpHgjURXHV76z9HQPtHPzBy0RokcQUJZpvk43yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rvh5jWj3WOQzc1ZMam10SB906omrAwzUOLlo5fOVFzfKkLPeFY_MMh7LLwUniwO_c7II1KNIqfgXWovHvffqNiaegfJOR7nJT-tuBJQgY0OngZ-FF-r_reEoitCWh9DUr1MSgYBtDBqE3rAzoYh4A023r19tl-NfM5TSLYrILrI5CO4lNqeud1bVdtWtEWXl42MFJniXUtyWn1OPmTe841-q02UDImRhP-98pA52terR4You1hHA_V4hbeI2D3YeqR7hu7FaFH6PMUJSD_Ju7D3morBG_wFTJyFk-eq8_6I9DUwYiTbzblRGfTXcV6ZR4Yf45fE6_bty_9Njluddng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
مراسم یادبود زنده‌یاد اکبر عبدی
عکس:
محمدحسن اصلانی
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453404" target="_blank">📅 21:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453403">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea1178ca1.mp4?token=ZQUCmh0giOEYeleoTg9A_DWmVGio5Q2MY0Ku6qnXZN5qyi7aJR4sSj5nXdm2h96x3RTKgTb9KTZ6ndREd89AG1fLqiEyJCJqaptx41Wt8HhPItDPnopvMJ5gvkYrJ4HbIRUSHhhziEODgfG3m60AkXOgxq_5IaiscftTBQhmc9mgGTVDupDQFMD7eDnGGwrt8TppsE0xQ540mjLjRNXUsGXyWVUH5spsvBZw4A1iBjQVUnUeCPIh1sugsSZMdjQqrdOvUf_HofSOPtpn-UdxQAhBuPmrgcxFQFJTkS3dkEFUiwHjFHKxLeDw5gdK-67HtERpw8VHPF2hY9LAN1YKbL7AZpXz97W2X6NEhYsyK6VEq9qCAEodTd5AupmRcx2sJxJg4zw_ZaptsRssZA2LUKBNg3cXkNVi1Eo09yzlzphKKUfi4GbcnqJ0vupmXJcXcQYJ0OG7RMXbUHtOt6i0kK8188Aoh3uzA0oQWwAv6R-Fs0EI7F6ZzQ3S_t0iDr5NTA-aX6u2RfV7yAEB0c6HuM0oHA1wZqCkfMqkbC5tM7W5MondTvk3osD8XJ4yTliXYcRxbNb7DaWTJI_fSz2v7RrT7P_U8jv_1cmjY10ZIJJ9cV5X3Sne9nwJn9EfJdp5JZUAMkvtANtBLVYc9Z6ocNH-AQ_sB4p50wAaDtSCBWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea1178ca1.mp4?token=ZQUCmh0giOEYeleoTg9A_DWmVGio5Q2MY0Ku6qnXZN5qyi7aJR4sSj5nXdm2h96x3RTKgTb9KTZ6ndREd89AG1fLqiEyJCJqaptx41Wt8HhPItDPnopvMJ5gvkYrJ4HbIRUSHhhziEODgfG3m60AkXOgxq_5IaiscftTBQhmc9mgGTVDupDQFMD7eDnGGwrt8TppsE0xQ540mjLjRNXUsGXyWVUH5spsvBZw4A1iBjQVUnUeCPIh1sugsSZMdjQqrdOvUf_HofSOPtpn-UdxQAhBuPmrgcxFQFJTkS3dkEFUiwHjFHKxLeDw5gdK-67HtERpw8VHPF2hY9LAN1YKbL7AZpXz97W2X6NEhYsyK6VEq9qCAEodTd5AupmRcx2sJxJg4zw_ZaptsRssZA2LUKBNg3cXkNVi1Eo09yzlzphKKUfi4GbcnqJ0vupmXJcXcQYJ0OG7RMXbUHtOt6i0kK8188Aoh3uzA0oQWwAv6R-Fs0EI7F6ZzQ3S_t0iDr5NTA-aX6u2RfV7yAEB0c6HuM0oHA1wZqCkfMqkbC5tM7W5MondTvk3osD8XJ4yTliXYcRxbNb7DaWTJI_fSz2v7RrT7P_U8jv_1cmjY10ZIJJ9cV5X3Sne9nwJn9EfJdp5JZUAMkvtANtBLVYc9Z6ocNH-AQ_sB4p50wAaDtSCBWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
کشیده شدن درگیری‌ها به حوزه دریای مدیترانه چه معنایی دارد؟
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453403" target="_blank">📅 21:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453402">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b491f68d88.mp4?token=axlTS7Kkhht18YXuAdKwHajkhsnKKJqvdnoasH3Sio-Z5Fwf-ODiNlfLByMNpystOGRs3V9IcahQSYXhaqixDK8zKpcM5ogKiv5DCmc03JBXvKAOmRnGN7gau2X1q24yp2A6jwDWCpv5QpG9shvtU-EYN_w4f889zxgQkE9Dt4ptnDXD5gBlC16gV9Tae4VKUsnr3zNskXktxLzVHLN8mXFuDmyIJ45MEu8h7GY11zREw9JdZ8Fd2PJXgh7OtJHQFtBBhPah4BNyoAtDoFxKYTag3BZqWRfj_zfK-_AqDfZyhyprNS2aeT_sNVyOtV2I_yC1ThOxQY4N7o533y81qVZ1UH1BUUWFnx0nUNLsvnT89Wwqhcsovj4c1NkUUwDFPEJfDjYeTCZGywC8otdx3JjJIpfEazFyJb3nWTK6rwAqoESOOJivov_IF3fuCGk47JfuzKiSnceL9D0pel4w5oaO-h3pR3LIizbIPYhQLs0jNZdEEcvDzyrqJRZfWdYnUBL4JRMUjvgoEc7ZRo4CQ4S8yPJj7dyliLjr9c1uHHp9nyGJqIhzxWYP44Nut3NIHdbN7K--JZIGPWPq_aXa5D7dpAOUGP6HfZoPNmlaNOSQxjkoDHTyvf7WpZYt1qHjEJEjqXk05dyshIgg1D32yzklbOcXqxO48aZtZ7j7ruc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b491f68d88.mp4?token=axlTS7Kkhht18YXuAdKwHajkhsnKKJqvdnoasH3Sio-Z5Fwf-ODiNlfLByMNpystOGRs3V9IcahQSYXhaqixDK8zKpcM5ogKiv5DCmc03JBXvKAOmRnGN7gau2X1q24yp2A6jwDWCpv5QpG9shvtU-EYN_w4f889zxgQkE9Dt4ptnDXD5gBlC16gV9Tae4VKUsnr3zNskXktxLzVHLN8mXFuDmyIJ45MEu8h7GY11zREw9JdZ8Fd2PJXgh7OtJHQFtBBhPah4BNyoAtDoFxKYTag3BZqWRfj_zfK-_AqDfZyhyprNS2aeT_sNVyOtV2I_yC1ThOxQY4N7o533y81qVZ1UH1BUUWFnx0nUNLsvnT89Wwqhcsovj4c1NkUUwDFPEJfDjYeTCZGywC8otdx3JjJIpfEazFyJb3nWTK6rwAqoESOOJivov_IF3fuCGk47JfuzKiSnceL9D0pel4w5oaO-h3pR3LIizbIPYhQLs0jNZdEEcvDzyrqJRZfWdYnUBL4JRMUjvgoEc7ZRo4CQ4S8yPJj7dyliLjr9c1uHHp9nyGJqIhzxWYP44Nut3NIHdbN7K--JZIGPWPq_aXa5D7dpAOUGP6HfZoPNmlaNOSQxjkoDHTyvf7WpZYt1qHjEJEjqXk05dyshIgg1D32yzklbOcXqxO48aZtZ7j7ruc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
«خیابان با ما» به مشایه رسید
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farsna/453402" target="_blank">📅 21:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453401">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6175f46d57.mp4?token=LzozulLTj6T4oVu7pQjuGD5XltqcMLmUyRWaaePR8iolizB1Xe39mifhXeYVxByPNyHwOUFu4E2UGrCz-V8bqacDlcxLYNCH836itrhD32MCd3xQKtye1X1XqDsHWmQi-duPGug08waYttny-7qGq4-H3rGbmC5RusHjYQEHnBMHd-rqafOYxZObQkpOujp0CnuZAf5OMs6XqPfxF1QR9YlSm5EOA2DykQP5r5b6W580wXgKcOVjIj5kmO2GpwNGJxc2hxiPvstK-7aBR5T94Z-K8XiC5osuOhzqxUnSoSOeQMPnkrlNb9qQnOK9OuJAGW1O21vb39sTYZCfdeihaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6175f46d57.mp4?token=LzozulLTj6T4oVu7pQjuGD5XltqcMLmUyRWaaePR8iolizB1Xe39mifhXeYVxByPNyHwOUFu4E2UGrCz-V8bqacDlcxLYNCH836itrhD32MCd3xQKtye1X1XqDsHWmQi-duPGug08waYttny-7qGq4-H3rGbmC5RusHjYQEHnBMHd-rqafOYxZObQkpOujp0CnuZAf5OMs6XqPfxF1QR9YlSm5EOA2DykQP5r5b6W580wXgKcOVjIj5kmO2GpwNGJxc2hxiPvstK-7aBR5T94Z-K8XiC5osuOhzqxUnSoSOeQMPnkrlNb9qQnOK9OuJAGW1O21vb39sTYZCfdeihaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مردم عراق! ما این اتفاق را فراموش نمی‌کنیم  @Farsna - Link</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453401" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453400">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gSM9vUsdE0bOTAgiylPSo8bob-3619w8lhVxv7NqZ66VtC-mG3JzDHXWOm-pq0buDJtPsgphX_YDUu3p-mQDvpfcO3u5gY0SDs10tpoIOftHX__4DNDTkYDfOLSyuYchSaz6O9jMbEdn3FNWDi7nOB3xzdtunAQPTEhCf8Sgwb5IU8emCkGpvXguNde4iMGX0RrqXR51g4h0RHE9qe3eeNRYUPLsTWFqGjYU_vUVUA7IdAWRR9sEcNrRYi5SmbawRfpCg2Tsayx4JvvdkDd1jkhvNA1XC8UmRq7oM3q31Rw_FLfPIX6pSjVFXvEkxXidfEKgDV2onufDVmouJD1v7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل ارتش: تا آخرین قطرۀ خون از خاک پاک ایران دفاع می‌کنیم
🔹
سرلشکر حاتمی در پیامی به‌مناسبت شهادت امیر سرتیپ دوم خلبان کاظمی: شهید کاظمی و همرزمانش قهرمانان حقیقی ملت ایران هستند؛ آسمان ایران، میدان رشادت مردانی است که جان خویش را سپر ملت کرده‌اند.
🔹
ارتش، بر عهد خود با ملت استوار است و تا آخرین نفس، از نظام مقدس جمهوری اسلامی و خاک پاک ایران و استقلال آن در مقابل متجاوزان، دفاع خواهد کرد.
🔹
شهید کاظمی و سه همرزم دلاورشان که خالصانه برای سلامتی آن‌ها دعا می‌کنیم، نیز در همین مسیر پرافتخار گام برداشتند و نامشان را برای همیشه در کنار این بزرگان به ثبت رساندند تا نسل جدید ایران، الگویی راستین و حقیقی از قهرمانان را در مقابل خویش داشته باشند.
@Farsna</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453400" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453399">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzyOAYnsKZSjTnNLDRpIn92Meiee2i1h7xVAXehiPxIdR8xOapCxLQzWJ_sv49dPjxSVj9-FuYvkCQaamUbuwl_IKvBAkFiFmZAjd55V_0pj3VnBVYiZiDOLCJ33xYvfxXeUpbmaEi56kFal1ycEaRU5efiqUlPKHXV_m1J5IBx-TK2NW-RYgB_irB2XE6et8ckNBCbpDuyAuLy_fATxwc_2g1vHhy5yPIkUM3cTvCzrWReYpVIwaxZYHgG4tpoEI8sCsBaqmDb5Yphld3xzzGqC2rLCMVpjcih-5Sy7Ut_DUOJ15KBBwVHDR23BtRr7LUE694lSPk6dYBcQ2TSuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یمن درحال بررسی دریافت عوارض از کشتی‌های عبوری باب‌المندب
🔹
رویترز به‌نقل از منابع آگاه مدعی شد یمن درحال بررسی طرحی برای دریافت عوارض از کشتی‌های تجاری عبوری از تنگه باب‌المندب و جنوب دریای سرخ است.
🔹
به‌نوشتۀ رویترز، هرگونه محدودیت یا تغییر در تردد باب‌المندب می‌تواند مسیر جایگزین صادرات نفت عربستان را تحت تأثیر قرار دهد و نگرانی‌ها دربارۀ عرضه جهانی نفت را افزایش دهد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453399" target="_blank">📅 20:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453398">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84a967bfa8.mp4?token=vIrHGYD15j3IuKJp69epWFyrdm8VOHraHIzBBWKjFZkpcMTyD-s4VyRNEsI21waoCmCd5MzZ3NNfkR-Rcjg0O0l3QJfObrdRYIPWawyJ1wiAVooyBp1KFwFyfs7o0LIZDGw_ETF0qqt3y3ZA-kLAw1w5bIA5SQJhqN2MaIxF59mUx6X9FtOWWxQNI2hsnDX6Iil5uqnvgi5odUV6fc8u4ek7LibZwyZnwTMoLH4UQVOdUppL-PqAeX_RjnfSbnancsuR-mJWy4tKku8GvsaoaTzyscZbO03MOuxh6PlPsy_ir-bfw_XVIGutD4xS7pCL9MgrEzhc1Vo46eVnhswQrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84a967bfa8.mp4?token=vIrHGYD15j3IuKJp69epWFyrdm8VOHraHIzBBWKjFZkpcMTyD-s4VyRNEsI21waoCmCd5MzZ3NNfkR-Rcjg0O0l3QJfObrdRYIPWawyJ1wiAVooyBp1KFwFyfs7o0LIZDGw_ETF0qqt3y3ZA-kLAw1w5bIA5SQJhqN2MaIxF59mUx6X9FtOWWxQNI2hsnDX6Iil5uqnvgi5odUV6fc8u4ek7LibZwyZnwTMoLH4UQVOdUppL-PqAeX_RjnfSbnancsuR-mJWy4tKku8GvsaoaTzyscZbO03MOuxh6PlPsy_ir-bfw_XVIGutD4xS7pCL9MgrEzhc1Vo46eVnhswQrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرز خسروی ۶ روز مانده به اربعین
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453398" target="_blank">📅 20:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453396">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/286802a563.mp4?token=J4JXwCXKApkY-5WswU-2OMElnR-GW78VeW84rPLA4fmq73TbWRzZnCbE7gGMQq6Yk2b0QnKsmXeqH3aYa51ItNaT1IjM-0baAY2BEztZKP9Zh-hNlclX6qhr-PbqhKGs2UuU6EGnxtyKzS60KHx47wqcWS_tvlkmLy8Di3VV36CTe5RH9pfAgZyh2fnaTFemkH1iujAvUHX3qw800EM2nikVsJoRf4zJudY62QgkqmRx9olcmnv5Av4c_BdEDKwlS1OmwAK2QQO9xnnx5t55WiFGycXW1tTabEuL3pnjDiFw2w3jeUUwsguGqMalqV2MQBjqE1UidGqx24thN8uDCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/286802a563.mp4?token=J4JXwCXKApkY-5WswU-2OMElnR-GW78VeW84rPLA4fmq73TbWRzZnCbE7gGMQq6Yk2b0QnKsmXeqH3aYa51ItNaT1IjM-0baAY2BEztZKP9Zh-hNlclX6qhr-PbqhKGs2UuU6EGnxtyKzS60KHx47wqcWS_tvlkmLy8Di3VV36CTe5RH9pfAgZyh2fnaTFemkH1iujAvUHX3qw800EM2nikVsJoRf4zJudY62QgkqmRx9olcmnv5Av4c_BdEDKwlS1OmwAK2QQO9xnnx5t55WiFGycXW1tTabEuL3pnjDiFw2w3jeUUwsguGqMalqV2MQBjqE1UidGqx24thN8uDCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله پهپادی به تأسیسات گازی آمریکایی در مصر
🔹
شرکت امنیت دریایی «امبری» اعلام کرد که دست‌کم یک پهپاد به تأسیسات آمریکایی ذخیره‌سازی گاز طبیعی مایع (LNG) در دمیاط مصر حمله کرده است.
🔹
امبری افزود که تأسیسات شناور ذخیره‌سازی هدف قرارگرفته در دمیاط مصر، متعلق به یک شرکت آمریکایی است و توسط همان شرکت نیز اداره می‌شود.
🔸
شبکه ۱۵ اسرائیل هم گزارش داد که این کشتی آمریکایی حامل گاز با پرچم جزایر مارشال در منطقه دمیاط مصر با پهپاد مورد اصابت قرار گرفت.
@FarsNewsInt</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453396" target="_blank">📅 19:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453395">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b57d7228a9.mp4?token=qWLRGnPRmoCcf5wRWUoUhzZVMl57dP24wZBltSxBoy_-EAEe4pt-INTD1_MNstFRfwDqlhyzBn79vvircrUPZYOAlVFJQ9D_XlDIZm6DiUjAu-iqgPnGLDIm7OAmg8Vlnacnb_JkjqD7svAOLTQf9jwpKsTBwIVSIMSkLKczwVwWcTwR5mJx-1i9NKD36ogjc530UqzKhug0w6mkYWNts572QScBRFeAEJB87yainhTy4_1GGwhF1xcVvk53t2TZ6z-rO3m75Eek9YOLu3BQlpyLff1qqnjrNMHPjbq7sHYCCG-Doi2zlLMek68Gwp34aSy-8UhAuyqPzF6o-8e9UQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b57d7228a9.mp4?token=qWLRGnPRmoCcf5wRWUoUhzZVMl57dP24wZBltSxBoy_-EAEe4pt-INTD1_MNstFRfwDqlhyzBn79vvircrUPZYOAlVFJQ9D_XlDIZm6DiUjAu-iqgPnGLDIm7OAmg8Vlnacnb_JkjqD7svAOLTQf9jwpKsTBwIVSIMSkLKczwVwWcTwR5mJx-1i9NKD36ogjc530UqzKhug0w6mkYWNts572QScBRFeAEJB87yainhTy4_1GGwhF1xcVvk53t2TZ6z-rO3m75Eek9YOLu3BQlpyLff1qqnjrNMHPjbq7sHYCCG-Doi2zlLMek68Gwp34aSy-8UhAuyqPzF6o-8e9UQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
فریاد مشترک دانشجویان آزادۀ ایرانی و عراقی در طریق نجف-کربلا: ترامپ را بکشید.
@Farsna</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453395" target="_blank">📅 19:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453388">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uxDBVu3bZHoJx8fqwf1IsYJ7Lb0bm46hW2qX8DHlnr-Az1TzHmxlCj6xpxwVbeZArlKWqK-RCD-639shZ4u5TCG1FQIJxWvA7JLfOS_eczR40wbaCkkvvw2ypMRo6JAsX85cP-SYcA6lZGcwsr37H_xU61EFhwxoLBb_cawuRfdsG1dRgISVuHnCUw3bmFoep1kcCdeujA4VrpHoDLCDVUA8jkUG65tQhEBMQhElMvghHjGc4zvBDZzzh_Py1z_AWJUXg98Oow7Ydu1tqLSmNRsdrkSlDdM3LUzDk-wUtiHRu2AbpLo0GA4Q9ETPA34nRvFkdkUX_rxKwErscs0TMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R6kzy-KpDOOYP_v2_s0h9fR7Lj5I6xsws-bgElDq2RVM8L9slEv4q0JFo7SqlbxGvtMBC__1g5kLlPw5QG_zWy2YIxUMz5k7v1fyiyWY_ZnsHOZHqkP0NEHEoIdgWrJLm28TDs_T9z7XW8ezSYPN5e_BW9Du0rK1jJeeNI1CnHcup8TdI1dWm5XwUWutYSMuX885G_DICZM-tBPFON5i26vgwdyn9Rd9npTKPmIy9qFDG9v95XHJZVeWD_44l1fL7dckXsZJrO0JJWTMg3OJT0D2O6WRDgIW4rkDC4RiZq0WCrmAtRng7PIm1nA5bgxmw4w_TZYgmQRg2ntq9yLHCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mz4LBLGoKFhgfq5jWo8JsAPqtGHRo4i16ATV6NiZky1WaAlr7KM1lma7wH_5QE2A1zO32wfXmh8SntetLmCue1jJTWA4neOpM2FalVrsfeGFoqhV2VYYxQcM5e7gQCmHzAvHjlO313GiXc8zdFl5WlRLQO1Z_razgFikTAhj8vYiOGk2UOYze__ReAe0vcQz8UGmA96kKiZHQtiP65icPZx8e4FLepUuTddgoujuIsFhmGLsxcmzDs8Blmy9PaNu0jFW84CLGU80AJ_TsxAGNchgMUpK37awevasYlADkweKeXl1pk4i_5FJvUBAMyUQkphNqr34rnjPocOZ6lU6ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U6bKKw8i1OGFqpJN9vje66C_DpGnDbfWenb3JNiTlkxjZ5WLwgnnFNLiESnhYeUbyhzlv0P1EjwhT18N04zOzTGRlay4z17cN6X7Lp6XW6Ez3YpbPu1Ij4zqeyHMZUny_RTQaCR_Nfy7lItAZGsnpdeTn2cVH60SzLVsomBdbcMnrF6bNjigGahwgwalbsOl3OkQoiZuGhhVMKWPY1UXop2UTvVbmwKYzUCFzk58dIOPRO3_R_cuKYiEz0ZQW0nqKDzKcoD_HYofLNfhCucU7QpBrMVE5QeW4w_0UyDL3RXOLP4aSnW-lB5L4-vkYUP5MULPviviYBKjY7zym5WFBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JvShNdyedT01yW7Q4GRo4Z-HKsclNgbcj9K--oRTuhlTAKFBdd9eCyC-HlqFMHl5X9mJd7OR_VSsMqcUOf66j1MTBJM_oUyEQNCUMwm4Tl4_fzovGtvgQthcqMQMDNuoDKN_4dDazQm8ky3vu5SxAixDDYHMfeznaBiuQ21PPqRPb-xFqKj5QfNi4b_BgpKbXa5xJCYVTC8dTL1g6vG2Mg4TtZaESSGog_ChlJkFRtswAJEMcj-Va8Q_IW97GAgsI18QqN7jmXU7o99Y53zYnmLvRJT33W8SsrKNbijRGnv0ExDxzHK_9fxYz6CBfYD9jWHITVBGyMVRu3fF8dOxUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fXxJBGGhc8Fvh_uYa0sAtmIaK3sUDN8z0kqL5saa7Bv2IjW6027cOQmui-EFo9KqCrKPlin-kE8UpPnVjXb5ETDggJGkk7-VV0K70yBtiddcJuNPFa4p1nmJsbilqVjPSAQxGrW3oTsLcW9GQ1NUYO225O02xhRxOXeBogbEXgl-yfMtO7ro5aEKNUmMSwYgQ53gY19HmC0rhNr3TY9YK8rAC34dlQe9raWQUDYPr_-jpgtJ4XHVkQOM3mpK6Cj3POmcdEaQ4l8Gsku61h0YTjFXS_IGzjmEQAdIsfL9BYpdD-VZJdd9PvwRFPq0zftj5UtRaO732sQE-DYDJugDOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DqQf3knx6wSROUbII1DlCmPSGa2Xuwn0ghrWki0Mn7pyKxBnmQmAKeFf0QyJDn9NI716B5Ou1V9XmQut-FwW6lHZrgldQNVAW-m_Tr_6IB4Gl5ybQMJ5gRrkJ9Z5xoGTwPZWGM_HK7IL6WBfCXm8Cgk9LtLmAL_5_3DLhro-_JKmoE9K9weYAFuvXqcXgwBMBMsrVbmScAnEnvo62wv6OpcOxv0XIvzxqj-dSYTFOx5eqVonPVlP8SLFhtqUuo0s2Euk2UFxYITV5bqQF9vVfNX0ODZcZsAHbx-JEr0eHl11vOgBSTLFPpqXk0JzT86YaufNAAAykvXrKwRzGD17OA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
طریق، میزبان زائران اباعبدالله(ع)
عکس:
دانیال همتی
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453388" target="_blank">📅 19:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453387">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">هلاکت یک تروریست در بوکان
🔹
قرارگاه حمزه سیدالشهدا(ع) نیروی زمینی سپاه: درپی اقدامات اطلاعاتی سازمان اطلاعات سپاه آذربایجان‌غربی، یک عامل وابسته به گروهک‌های تروریستی تجزیه‌طلب که با هدف انجام عملیات تروریستی و اقدامات ضدامنیتی وارد شهرستان بوکان شده بود، شناسایی شد.
🔹
این فرد پس از درگیری مسلحانه با رزمندگان قرارگاه حمزه سیدالشهدا(ع) به هلاکت رسید.
🔹
در بازرسی از او، ۲ سلاح کلاشینکف، ۶ خشاب و یک موتورسیکلت کشف و ضبط شد.
@Farsna</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453387" target="_blank">📅 19:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453386">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس ورزشی</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e12a6efbc.mp4?token=f38Yb-2jNs1CETVxvjFTWl_peLPWnJKfiB__MX2LubAFJtk9Fc_ZEAmnXKYtD6LmX6ZK2dfZYuAUbomA6Op7ddQo-Yfa9f5OAkQ5LIGTJ6HUfxO5Q_54LrSQbzzylvCimk7qkrCz6tm6inv19psPwo3zt-RDuOAf4Tj44hw2oJKya4NAMRs8ONhqtGXuO3p1yekjTKRtx1I1lJS6tkyyWqpc4fU2_FEdMSuCQ-Fm71sBwiouy7jsKWg0w6DZGhAkyu-Zs_tRKZQYvvwShewT3TgYCy_Jc_TovI7PhbxcecYnKY_2dlMPxbg4mCIBsjkucdVIm2-HDVwS5jG84FgeMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e12a6efbc.mp4?token=f38Yb-2jNs1CETVxvjFTWl_peLPWnJKfiB__MX2LubAFJtk9Fc_ZEAmnXKYtD6LmX6ZK2dfZYuAUbomA6Op7ddQo-Yfa9f5OAkQ5LIGTJ6HUfxO5Q_54LrSQbzzylvCimk7qkrCz6tm6inv19psPwo3zt-RDuOAf4Tj44hw2oJKya4NAMRs8ONhqtGXuO3p1yekjTKRtx1I1lJS6tkyyWqpc4fU2_FEdMSuCQ-Fm71sBwiouy7jsKWg0w6DZGhAkyu-Zs_tRKZQYvvwShewT3TgYCy_Jc_TovI7PhbxcecYnKY_2dlMPxbg4mCIBsjkucdVIm2-HDVwS5jG84FgeMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🐿
یک
سنجاب مسابقه بیسبال را به هم ریخت
🔹
دیدار تیم‌های دیترویت تایگرز و بالتیمور اوریولز در لیگ حرفه‌ای بیسبال آمریکا (MLB)، با اتفاقی عجیب برای دقایقی متوقف شد. یک سنجاب سیاه که وارد زمین ورزشگاه کومریکا پارک شده بود، توجه هزاران تماشاگر را از مسابقه به خود جلب کرد و به سوژه اصلی شب تبدیل شد.
🔹
این سنجاب از اواخر اینینگ ششم وارد زمین شد و با فرارهای پیاپی، بیش از ۱۰ نفر از عوامل اجرایی ورزشگاه را برای دقایقی سرگردان کرد.
🔹
در نهایت، نیروهای خدماتی موفق شدند سنجاب را بدون آسیب‌دیدگی از زمین خارج کنند و مسابقه از سر گرفته شد.
@Sportfars
-
Link</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453386" target="_blank">📅 19:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453385">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2c469c61a.mp4?token=dT3LD9O8UuDT02OieJsVM--02h0tFbgLCpYbShjo0yOAT3jRlYBF0CZRrXOvFARp3tkZc6kUgUuwxtSGnoJAdL1qq2-GR1j-lfNoQAUIVdn0mOwZzQe1so-bL36nCmYchnQA8rEsQDK0gQMPSbqVAn7zYii6FaCUiwsEHw5JOPs3xy7-4oltvBWyBBC1Z5vNtEfASn46hia26inhK64xyAUjVOC-P6Par_TdrrRd1CvhzILNmp38Otqu2VLr3judsYyZbuNaqZzC1XsbJVkLHKWTyZmavYRrNvNKkur6oDBiZxkfTzq4Ci4Ei1LXGnYKL9RyVgfqYZdtS5ASjxurOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2c469c61a.mp4?token=dT3LD9O8UuDT02OieJsVM--02h0tFbgLCpYbShjo0yOAT3jRlYBF0CZRrXOvFARp3tkZc6kUgUuwxtSGnoJAdL1qq2-GR1j-lfNoQAUIVdn0mOwZzQe1so-bL36nCmYchnQA8rEsQDK0gQMPSbqVAn7zYii6FaCUiwsEHw5JOPs3xy7-4oltvBWyBBC1Z5vNtEfASn46hia26inhK64xyAUjVOC-P6Par_TdrrRd1CvhzILNmp38Otqu2VLr3judsYyZbuNaqZzC1XsbJVkLHKWTyZmavYRrNvNKkur6oDBiZxkfTzq4Ci4Ei1LXGnYKL9RyVgfqYZdtS5ASjxurOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلیل موشک‌‌باران مدرسۀ میناب اینجاست!  @Farsna - Link</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farsna/453385" target="_blank">📅 18:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453384">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‌
🔴
مقاومت اسلامی عراق: پاسخ ما به عربستان و آمریکا قطعی است
🔹
برای حفظ امنیت زائران حضرت اباعبدالله الحسین(ع) و خادمان موکب‌ها و جلوگیری از هرگونه اخلال در مراسم اربعین، پاسخ ما به تجاوز آمریکا تا پایان این مراسم به تعویق خواهد افتاد؛ اما این پاسخ قطعی است…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453384" target="_blank">📅 18:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453383">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">‌
🔴
مقاومت اسلامی عراق: به نهادهای دولتی عراق که خواستار خلع سلاح مقاومت شده‌اند، تا ۲۳ صفر فرصت می‌دهیم تا عملکرد خود را در دفاع از عراق نشان دهند. @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453383" target="_blank">📅 18:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453382">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دولت عراق به محکوم کردن تجاوزگری آمریکا و عربستان اکتفا کرد
🔹
شورای امنیت ملی عراق در نشستی اضطراری به ریاست فالح الزیدی بدون اعلام اقدامی عملی، صرفا به محکوم کردن تجاوز هوایی آمریکایی-سعودی به مقرهای الحشد الشعبی بسنده کرد.  @FarsNewsInt - Link</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farsna/453382" target="_blank">📅 18:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453381">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/489f6a5e97.mp4?token=CImDQ1BGuXu7ydliV_M0srMb8FxmJbRZ5DmTbGhSntK-Q-lNTV3eg6KaLFoepGBaTmRoJn_HcDd1NMCNDt53aTILAachyUDIPr1uvyMK05yyHpLq4ZYwDp-xiPml6HGfrPQQz_w8VRvPn2PTyBRhC1-OW0LVkThhb4-fF5VKgTjZdSjnBbc15cBQ0CzFjmI-zXeu-R3Esepu8AMlpfNdEX0s0x_r6ENMa8VwHE2w7TV7GqVirn8ndwGNqJBT9LIMyAC8Fv4wGgQ-Ud0CsYpGXM1SAwgI_9oXjHvoV5sGU4TVah04ksb77TmorHlRdvikbXZp1IihPVTWgKRlbwXCfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/489f6a5e97.mp4?token=CImDQ1BGuXu7ydliV_M0srMb8FxmJbRZ5DmTbGhSntK-Q-lNTV3eg6KaLFoepGBaTmRoJn_HcDd1NMCNDt53aTILAachyUDIPr1uvyMK05yyHpLq4ZYwDp-xiPml6HGfrPQQz_w8VRvPn2PTyBRhC1-OW0LVkThhb4-fF5VKgTjZdSjnBbc15cBQ0CzFjmI-zXeu-R3Esepu8AMlpfNdEX0s0x_r6ENMa8VwHE2w7TV7GqVirn8ndwGNqJBT9LIMyAC8Fv4wGgQ-Ud0CsYpGXM1SAwgI_9oXjHvoV5sGU4TVah04ksb77TmorHlRdvikbXZp1IihPVTWgKRlbwXCfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احراز شهادت یکی از قهرمانان سوخو۲۴ ارتش
🔹
شهادت امیر سرتیپ‌دوم مجید کاظمی، خلبان یکی از جنگنده‌های سوخو۲۴ ایرانی که اسفندماه پارسال خسارات سنگینی به پایگاه العدید آمریکا در کشور قطر وارد کردند، با آزمایش‌های تخصصی و بررسی DNA محرز شد و پیکر مطهرش تا ساعاتی…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farsna/453381" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453380">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f64a062d.mp4?token=ht3xpfdhroy3_ee27ZVHclrOC5sSoa8P8eAa3XmRxmDdAjqP3NEwfIIqFOSsvpNN090igpuDNf80JF-xHQZ5xlGVL8clUEYVYqO-mqCuy8s0IPc7qsgx-qaXlFgBNq4e2FPGgCL4qa84AJMaJ_ktu8xLC8veJZ7RAfrysAnZ5XCUNMhewM6FmCYWj6NWF_m-dGc8-fMt9GFPzmSnSwKdvTEytQIQkjpTo6QIXhcdcDZ1ZnaHDh23igs4g_lhsMPQZBnG6QiJP4I08pNXasv6rTYYN3eJY8wa8P-cKN3vFJW9z1TIG4kx4YExV2cWun60vjK3gkc-vFqr6ukCcgzkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f64a062d.mp4?token=ht3xpfdhroy3_ee27ZVHclrOC5sSoa8P8eAa3XmRxmDdAjqP3NEwfIIqFOSsvpNN090igpuDNf80JF-xHQZ5xlGVL8clUEYVYqO-mqCuy8s0IPc7qsgx-qaXlFgBNq4e2FPGgCL4qa84AJMaJ_ktu8xLC8veJZ7RAfrysAnZ5XCUNMhewM6FmCYWj6NWF_m-dGc8-fMt9GFPzmSnSwKdvTEytQIQkjpTo6QIXhcdcDZ1ZnaHDh23igs4g_lhsMPQZBnG6QiJP4I08pNXasv6rTYYN3eJY8wa8P-cKN3vFJW9z1TIG4kx4YExV2cWun60vjK3gkc-vFqr6ukCcgzkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
مرز مهران؛ گذرگاه عاشقان سیدالشهدا(ع)
@Farsna</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453380" target="_blank">📅 18:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453379">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGH3wXXyri_IQ0Gd0ZBtfmvpoDef19SCMs-qFlSrArX-IJJD0WWFkigr8GHdrzRJa3RG4ipa0BGOHk1tjVfsBowEGttGHpQtJQe0ogx99Xe9k-hk195Bw1HUHr2OLHxNho1x6ZYrRppU2juT0YbjeKAJz6k2DBQVAETmkpBJ5kVlOOkFb04DgasGi3Lir8DpjbKk28g3wsl3no1f_SEIyaSZZrQutqlMNEH42T9vA6hnyQZE8LXuzRz9Cvjlfh1zXHyolfO5D-aRE2yQxTzOBaT8JKF3D3fwYUsAzcYfiA_emWzqd4cKrybLXBtupalMmSW_-5TNDiZelCAqZBwZiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دولت عراق به محکوم کردن تجاوزگری آمریکا و عربستان اکتفا کرد
🔹
شورای امنیت ملی عراق در نشستی اضطراری به ریاست فالح الزیدی بدون اعلام اقدامی عملی، صرفا به محکوم کردن تجاوز هوایی آمریکایی-سعودی به مقرهای الحشد الشعبی بسنده کرد.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453379" target="_blank">📅 18:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453378">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انتقال تعدادی از مجروحان عراقی حملات سعودی-آمریکایی به ایران
🔹
درپی حملات بامداد چهارشنبۀ آمریکا و عربستان به یکی از مقرهای نیروهای مقاومت عراق، تعدادی از مجروحان این حادثه برای دریافت خدمات درمانی به ایران منتقل شدند.
🔹
این مجروحان به یکی از بیمارستان‌های مجهز غرب کشور منتقل شده‌اند و روند درمانی آن‌ها آغاز شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453378" target="_blank">📅 17:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453377">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">آمریکا دوباره ایران را تحریم کرد
🔹
وزارت خزانه‌داری آمریکا ۸ کشتی و ۱۰ شرکت از ایران، چین و چند کشور دیگر را به بهانۀ ارتباط با ایران تحریم کرد.
@Farsna</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farsna/453377" target="_blank">📅 17:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453376">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANy7_Wv67ovo0jfYu8s97-KhV-Wxo5Gj8txdFCoxG9RLdirFKJBjy0Urx3Arq0YNMGLOeH7dG_jWDF4dedmff68UETu3tcu1hdbghSnQiI-9Iygbb31Da9rzzKiO0AgjlVfMZ4w9oLOgfPKE6i6vEw5hm_6mw9JUQwh5h8pITLGExn6oa_MxSNDzZFhGtFmI0XLbalzRM_L6AkVXFKM2B1DL9KYK_Q7lVkTNlggVHR-q1hCSOpwpAlTqyrhllypWVZWjhH1CEIxZUUsOeoS7IQTryEnVZNANRUrSDQg06Mlk9RekOHaYRszN1SF4pxdAPk7tWuaCqhAkzwYnUy9_Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پس‌از حملات امروز ایران به اهداف آمریکایی قیمت نفت حدود ۶ درصد گران شد.  @Farsna</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farsna/453376" target="_blank">📅 17:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453375">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbf4ef825.mp4?token=ZSo5DUZSw_pl1rgR-NFRXYBraVNHdExzsWDxKpixj_zigERGXIWSs0Lv2_hMj_DppuBm-UIjiZWBaJ9fJhfC6UznCbOpUQK8gsaI8q4yhfBJx0wSubZvwN3smZy54zt2LyfM29O0mtlYGujbqf2l2uNBVSAqJdXGmCbuvN8EfyAynYadWC3JNemQodErn6RPBBqVJ_x4wj2gwftggfWhiCA-FOBiJn9D9qcBG16VWa29wMS_7D58ijcvJdf6Mt-t8vmfOlfFU78Qt6dU-1StwEba_flrTxM9iMkTWiSUGCxuAaUHhwBkZwiG03ep0_qR1wHgObiuwDVRIqqbBSNQfHNHXQ8cbn2jJ2ZyCi1Uz3yEIAT7yg2tKnASQJNl_fXvkv23uRewgcsMVlbT0bGKwHKZ_qLLf1_hnjCHO73e8g-nl6xw8Tc7xMOITGzEILcqhANjYR4wGESU4rO9gSpKm7sefOVN3siX0gZoRssnmasw5suiIfHXnJB1UKROCr-xxgZc_F-ukXaMDay4Rk0u0WcMKyYikdB__Z_gM_VtZ4U2RRF0f49RAvxKIZeJPKp-6f7KyezajHeo1WeSutOZ_7WZIye1UlqCf8qpwAR6MxNDZLyYPnWBIrF4yNGorkeX3pp7KgoB-aBhr3pS1T7R8QnUHEatbxS7xnPnAOVa2Hc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbf4ef825.mp4?token=ZSo5DUZSw_pl1rgR-NFRXYBraVNHdExzsWDxKpixj_zigERGXIWSs0Lv2_hMj_DppuBm-UIjiZWBaJ9fJhfC6UznCbOpUQK8gsaI8q4yhfBJx0wSubZvwN3smZy54zt2LyfM29O0mtlYGujbqf2l2uNBVSAqJdXGmCbuvN8EfyAynYadWC3JNemQodErn6RPBBqVJ_x4wj2gwftggfWhiCA-FOBiJn9D9qcBG16VWa29wMS_7D58ijcvJdf6Mt-t8vmfOlfFU78Qt6dU-1StwEba_flrTxM9iMkTWiSUGCxuAaUHhwBkZwiG03ep0_qR1wHgObiuwDVRIqqbBSNQfHNHXQ8cbn2jJ2ZyCi1Uz3yEIAT7yg2tKnASQJNl_fXvkv23uRewgcsMVlbT0bGKwHKZ_qLLf1_hnjCHO73e8g-nl6xw8Tc7xMOITGzEILcqhANjYR4wGESU4rO9gSpKm7sefOVN3siX0gZoRssnmasw5suiIfHXnJB1UKROCr-xxgZc_F-ukXaMDay4Rk0u0WcMKyYikdB__Z_gM_VtZ4U2RRF0f49RAvxKIZeJPKp-6f7KyezajHeo1WeSutOZ_7WZIye1UlqCf8qpwAR6MxNDZLyYPnWBIrF4yNGorkeX3pp7KgoB-aBhr3pS1T7R8QnUHEatbxS7xnPnAOVa2Hc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
دلنوشتۀ شهید نخبۀ نبرد سایبری
🔹
شهید مرتضی فکری حوالی ظهر روز ۱۱ اسفند ۱۴۰۴، با زبان روزه و در حین انجام کار به همراه ۷۲ نفر از دیگر همکارانش در حملۀ رژیم صهیونیستی به محل کارش به شهادت رسید.
🔹
پیکر مطهر شهید حدود یک هفته بعد از شهادت، از طریق آزمایش DNA شناسایی شد و درنهایت در قطعۀ ۴۲ بهشت زهرا به خاک سپرده شد.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453375" target="_blank">📅 17:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453374">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08a2da8fe8.mp4?token=cqBjBIvaoSOtBK-d9jn5SDBpCLuJGDz4t04WPwNMt0xkLwhkG25eQUOWCoJrwt2qThJ9vVx0ugQXtT6OFjxpztSk3fWZRiIJbe-3E4zKW-WqqvPiiGXSuZ6esCKyhMDn7EEhDVmj0xNiU0JOaplPdAgJRUHbWUmp7abe5lMViK1FGT-76yb-jpxMtwHfC6H-7ayR0zzD9irzkHUcreuxMWBM-tc6UqrZ-276ODirpecQFMyNgFV_oqkcgb6mVn9W4WBptdk2jIZGKcMz9jbBVLN3boidVhdcEWpmb49WQYauAP9PD00_5mAKrYR4diXPDl4mCABN1AYuZ1XwgVr1uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08a2da8fe8.mp4?token=cqBjBIvaoSOtBK-d9jn5SDBpCLuJGDz4t04WPwNMt0xkLwhkG25eQUOWCoJrwt2qThJ9vVx0ugQXtT6OFjxpztSk3fWZRiIJbe-3E4zKW-WqqvPiiGXSuZ6esCKyhMDn7EEhDVmj0xNiU0JOaplPdAgJRUHbWUmp7abe5lMViK1FGT-76yb-jpxMtwHfC6H-7ayR0zzD9irzkHUcreuxMWBM-tc6UqrZ-276ODirpecQFMyNgFV_oqkcgb6mVn9W4WBptdk2jIZGKcMz9jbBVLN3boidVhdcEWpmb49WQYauAP9PD00_5mAKrYR4diXPDl4mCABN1AYuZ1XwgVr1uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
شوق وصال در مرزها؛ زائران به‌سوی کربلا روانه می‌شوند
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453374" target="_blank">📅 17:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453373">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oDmBqag36EPdW_Mdnxtp0EuEBW0wOrYAGFTgl1GWjSzW5-PD0WThJK0XPl4UQX0-L6HV89eBfAJKCx4-I4EXaJ2SJHiTSwSbBhJMKsXB1Jar3-sx6CsKh1sEMSqNA3l6cZOpbeIT80lzB3I8LaCsDLClXD9Ljbi6BKnkyWmUM-joPY5ePdNT-wuso1eD9hYbT6nQW4I4iJhvmzvEPmbL83IaN6Xb_8xmzAfZSDyDHLwAEFcjbL48WtV11ZZYvbjtsUk9uPSbLDRyk0TYQY4jLCZ14Ez_AXzJqdfa6s4eWF2001n-9-vFQTk06NraeL3d3zUJjtfEArQvd-aGvwUeow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورود پیکر خلبان قهرمان سوخو ۲۴ به تهران
🔹
پیکر شهید‌ خلبان مجید کاظمی، صبح امروز وارد پایگاه هوایی شهید لشگری در تهران شد و مورد استقبال فرماندهان و کارکنان نیروی هوایی ارتش قرار گرفت.
🔹
پیکر شهید به‌منظور برگزاری مراسم تشییع و تدفین، به پایگاه شهید دوران…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453373" target="_blank">📅 17:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453372">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7589cd384.mp4?token=Gh6sfkyvVvwSJrdcMyRVLw1q1B0hcOC_YjZ35LYaIwdaZsbIwot8tBW8n_Fm5V4opOqqt3SW35h-8mW6EHXGXdSuZSuIa1BG15UuvryQKPi5Gxfx2OVlCzcoxJYalasbiCZzRCDCi72rw36FUkdd_ElhwIyFA4U2MXMXgkNBfT_fl5bOTmkT8kQzPxTbY5OZTqniL35btfe9vTxS9a76spuE9jXuOVCS20ZrIowwaXCXB9IejolzIUjXEja5xR5H0IHDqqpO4_IOaEpi8LAjOA3a4wqyXDHH7ynDuPX49ScGBPGVdpFX3t5flsyFpcKo4nbF-AINQVpT7kG1Mjvj0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7589cd384.mp4?token=Gh6sfkyvVvwSJrdcMyRVLw1q1B0hcOC_YjZ35LYaIwdaZsbIwot8tBW8n_Fm5V4opOqqt3SW35h-8mW6EHXGXdSuZSuIa1BG15UuvryQKPi5Gxfx2OVlCzcoxJYalasbiCZzRCDCi72rw36FUkdd_ElhwIyFA4U2MXMXgkNBfT_fl5bOTmkT8kQzPxTbY5OZTqniL35btfe9vTxS9a76spuE9jXuOVCS20ZrIowwaXCXB9IejolzIUjXEja5xR5H0IHDqqpO4_IOaEpi8LAjOA3a4wqyXDHH7ynDuPX49ScGBPGVdpFX3t5flsyFpcKo4nbF-AINQVpT7kG1Mjvj0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📷
نبض اربعین در حرم امیرالمؤمنین(ع) می‌تپد  عکس: محمدمهدی دهقانی @Farsna</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farsna/453372" target="_blank">📅 16:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453371">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e9338c9b2.mp4?token=K2On_-H0yBk4S2GoV4HW5cDHT9xKyTF_MupeDBq3Bmzd_fAh3huvc8SQSaxyMp1-BtCvTKuf1jhfJorRvZlSJY1kfh45r2PPP6bdenCKd-fJpjtIJfj0QSayrsKTJJ_uz4lNmysM_0c3-9dTCTU5dkF0mea3Y-MIV3sIrRiQ4kdtnptbO7PR2Q0pedXHMgQ1dcUr7wMRRRcvasZeuE-xcIEHJO16OVXttQ54jQqvqSLeAL4Zh9L40emHmcldYliJiR3G5k3apWuqzyl70AF_8khby6wiGOKyJBrM1ejcw9ydZGlSfjRi3o3KFoPfaV1BbAv0nWyKwTlogfatJ7DkhAFhsnRUUdHGhrczQaVgAYMMPx4eFJqDpojubXOwrvM8Mu8u2KjzuEEJShuqUtcVyy-B9ZZeczUMMNaQeEUK3BcO6cHPO3-VVV6lcWGFT48cl3dGr1pdKFRIlU5-z3exYvmwPm8LkJoPApiWv-wqhi_mBc4MDuiNA5VxSk6PsivxBZnQnv124S1UleSPCBlhmdGekoobGBgkd8brTZA5iNUFj_HRPaN8byZlAPSqHXGCBXBKx3mwLgaJt3gfWKaolNvaCJ5opYA7xWpmH2sHz1mwJAGbWMYDyWZjPQMggxDfBrO90LyY8ijtTOVnBb_QizY-Fbuh5q3erZCrvpiEnvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e9338c9b2.mp4?token=K2On_-H0yBk4S2GoV4HW5cDHT9xKyTF_MupeDBq3Bmzd_fAh3huvc8SQSaxyMp1-BtCvTKuf1jhfJorRvZlSJY1kfh45r2PPP6bdenCKd-fJpjtIJfj0QSayrsKTJJ_uz4lNmysM_0c3-9dTCTU5dkF0mea3Y-MIV3sIrRiQ4kdtnptbO7PR2Q0pedXHMgQ1dcUr7wMRRRcvasZeuE-xcIEHJO16OVXttQ54jQqvqSLeAL4Zh9L40emHmcldYliJiR3G5k3apWuqzyl70AF_8khby6wiGOKyJBrM1ejcw9ydZGlSfjRi3o3KFoPfaV1BbAv0nWyKwTlogfatJ7DkhAFhsnRUUdHGhrczQaVgAYMMPx4eFJqDpojubXOwrvM8Mu8u2KjzuEEJShuqUtcVyy-B9ZZeczUMMNaQeEUK3BcO6cHPO3-VVV6lcWGFT48cl3dGr1pdKFRIlU5-z3exYvmwPm8LkJoPApiWv-wqhi_mBc4MDuiNA5VxSk6PsivxBZnQnv124S1UleSPCBlhmdGekoobGBgkd8brTZA5iNUFj_HRPaN8byZlAPSqHXGCBXBKx3mwLgaJt3gfWKaolNvaCJ5opYA7xWpmH2sHz1mwJAGbWMYDyWZjPQMggxDfBrO90LyY8ijtTOVnBb_QizY-Fbuh5q3erZCrvpiEnvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
ماجرای شهادت مظلومانه مادری که جانش را سپر فرزندش کرد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453371" target="_blank">📅 16:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453370">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id-I-lw1U3KNwdL1FSia22EgF6A7q_Kmm1NHUIrVcF1FvKM-CKUrcKmU17dJMeC3hs9LxwYopByY1oswMHMR2gy5N9vnnLldl7cXgWQ08tYuUgsbeJnMKQQnuD5fnuNsFhGdAQD2knb2hMXre9hAKjNYaVLgOngoYIaRnA7lNoJEdvjuJECZrcA7tpDjrNep9TVbJJcXjVoCq6A0cHVWdanSIt1v5hKfOMOxYHGhqErdX3FXTqX9UjxvZKJVy61yLtQ5qn_OPpxqt4G46Ih4L2PDGc2HNoCpQgH8j7T7CVnXV4vrTeZeuG53GZ9_ZtbqNdCDh4r8Tt8NQJDXNwqybQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تلاش نتانیاهو و زلنسکی برای هماهنگی علیه ایران
🔹
رسانه‌های صهیونیستی گزارش دادند که دفتر نتانیاهو و دفتر زلنسکی در تلاش هستند تا در حاشیهٔ سفرشان به واشنگتن، دیداری دوجانبه در مورد ایران برگزار کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farsna/453370" target="_blank">📅 16:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453363">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CyRO8jQgYNlUZCDRnWhtWA39hX4A6tGicxI8wutO_GVQss1XdB7PzhuKpzJm9u2CPdJwe7eUVbwUNhk3zRU9suui8XV-4eso9M7JlXNgy7xV-zPQwO_Sg7AAg4GXCKA30bfqmAadKDsSXxag_Ks_ayhZnBA4CiVMh2QoP15ysS9T0PpP8sNMQ4F5VIKLL8iwtPpo9r-cAzTvnw-yowRjRfr2iQg__e6yG9-jSi81jHeF0w-3bitsCq3DKVLoFBH3v-ppkOn3fdbbepBpE6DGsUoVllvk2zany-JJyLLkrhlY0B7c2E4xQERH3iVeCJDsUZV-_nAjiWKCgosmF2yu1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GKsDaTXwuuQX4QNFTjwm6DXk5jepUDJZRQx_pxHmjYV9LKbOL0rp5_HsyOMvsmqcLzRBLfND9YDQI6ozWlioMXasmg7r6YC92VxUgnVE3Tgu0B44VOA3ql7Wn8jrn50LQQNgeeHYtEks2bPJM3clyyOzIWpthGMmZ9w8g9hfeN1rxP7FqNcPF-hliX55kR5B5sQyqzTjkd9AVESHGoYF-S7zAibm1vd7PUS2fnxTxLlG4MadU-V1d5J7Lb060CatNTZYCaifj36b-TElqWUrcnN0N_Zc015Z8PLiortOzoB7KGtXUNX_yXhx5UXQPwKuacrkz2I-FVM0G8EWGl0puw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DE2iNYDNA5PyNQNS83-ttVpLCz9hIL1fUH8d033GCnDlOPnoqPnqG2obIrp7dWljR7bp91j4_ZZW7F2po6hIDzBJDdMvAPH5kjZCxBxVgpEChZELON7_zw1WRU6lzBuQcJaOKPWJ4lDi72W9UpFo-eLD-ezcYJ_0LZ55upQOKCaUizHw1oj6Mymo1__0OsJNs305bG3bBH09l7evbwxu_IKYCWmVD6n7L5c6FRqNlMXWvh_2VqZM1pBZy0mdym2Bry1YjAB39hwjHjcPB9os9fQh7OJzIxTdAX3etp6Fs9MKwfnj2iN1Zm4_A3XR6wI2w6YjQw44XjHOLiwZXa563A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ccn61apv9dVvCACNekEV7mU1TrMkpEOHTBBDyMPccWqDmRcBshyONgI4FF9A5_91_Dgzkdceh1KK5ubeYjajOBFSsGy9P65csQ7p8eHuHS2cTOR49abD9aW2xBF2ESpztNodPKFo_mOVa5Si2o24ZpC-xxRlagZ7GA3nYmTKnvHywkaiIY2bd4ezBWnFUAdkwPMDza9pqV6W7021E_j7mUwSMNx7MWz9Hk3WdQhEQIkhxJi2UGseOf_yEAq3qD1SiANG9LQSdzR0z1sEEqI8ifJtBcH_aTU4ZcqtFwSDxVzZES49TERmfbY6M4IIJDvdr2Qt8WKXEGhI559MQrdNbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TNAPZt0ZU_0O5O6feJ9ccjp4490GQaME3gSiEBFdoIQrY0Yo9aPmItl0qhYu5OdX-rUQsf8qS1aNuQFaFotOV8xrZmTVbgHYKYMlnUzgvjAFiuE0OslLrUDBPpj1iAaYgpBLsOgk33mJSVnMYJwgNqKrWMhoiKjCLrt0IPBfeKOXk1S4HBc9lw3rffm2huvUdBBKsDMqTSLrwAv9hGOvstp30cMIAaYo3ticYZtxOHrR4fjATnS8ayw0V80bfaYNEdQ94MoximnPBKzr5CGDRpQer3DpSAsgs31dDd04a7N99qX3A0kPMBfCKoc3L936j2XEYkgZOqetzM1mcClNmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gsXnfYAH1QX31IC7nYY8m-NdIrZeIBwBucpQDBJyx9M_3QJuipVJJp3iGzObQ5AH-oKVtnlxhetHUBXJ7r-4PjSB7wBk-hSb4FUiytFpGTYhIYs9T_oXr7_Vtw_gj77VNpeP89KGcQKTxOQ2CVqkNFWMQ3e9iQRVYjhf0Q0CCB648wVrX-yN7MribUgruDZKXrjZi_Iq174P5cyS9xi7aT2ElKjozozNBoY5JiYjtZ9631Z4ficpFtU1ibe7qNwNud-kB1RJ5X8EF0yZ_PFb_pW16ptJvk3M-rWAaw8yTnNDO_opjBnc-97V1QwOy7DQOsyRFpARSxtbNGjIlt1lNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LM_AfSD4DUUbgcxdmxwxbtTmZ1ThwVjIJEDwflwlf64H7z6MsmnaurLlws1WuXNXFoxRd30CnU31HA46FmuOVLjOSbbLtWBg7rwv8YOcjKnwrq-HOB_TbZgO4uYkpt1dWEOt3HaOFfCs1Y38EV7TNHA7ZrcUDlR98nuzg1IYbOngaq5vJ8DAeeQX77GqiJsG0IFL5YDEKOS2Z7pkCL6ZsfHuFRPMXaBUOpUauSOS5cpLPR7y2rqvfblKROXGGxwTzGM03eZGksq07U2CSaeaCA55BzZ0R0_0jC7YocfkJFEImXeZhMahraF_Ussa3ahRw6okrtZgH5bStf0O73sRiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📷
نبض اربعین در حرم امیرالمؤمنین(ع) می‌تپد
عکس:
محمدمهدی دهقانی
@Farsna</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farsna/453363" target="_blank">📅 16:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453362">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ukNKdtyfwClCK2OpQjeoZhzeoIHG5fggMTtwf-xl3v73YhuP6qhjY7DzjoPizqSz8BMN2aeCyT0VSTVqYs1C-arNNXL-8iFtPDE-4CGOcJ2lHZdu7xFUz9BkcHM72vWesJds2KtW4y-4FNLrKY-_Jl9QNUR14YGOVrixKkUyt9LBebyKkMqSjr1Jr9xio_GFJdlIgPSWPpNImX5D6J1G1yEiLpInPYATG6eRJM-8he43RkpH3jS0DVgGj5IckIFyB4nrVCJqqC_ZwE7MdLLa49TURLLBy7t-OFHn0ccU5NOulrbjsiGWMd5GGcGsEoForWWAHBEEvt4eNXMgfkWWJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنبش نُجَبای عراق: اجازه نمی‌دهیم حملۀ آمریکا و عربستان بی‌پاسخ بماند  جنبش مقاومت اسلامی نُجَباء اعلام کرد خون شهدای حملات آمریکا و عربستان بی‌پاسخ نخواهد ماند و از دولت عراق خواست:
🔸
پایگاه‌ها و نیروهای آمریکایی را از خاک عراق اخراج کند.
🔸
همه اشکال همکاری…</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453362" target="_blank">📅 16:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453361">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYZv4b5pfGYXrm-ECvZwnlRj3lM6YtJ7DDIXvGnzp1ZqJBrGv8KkJgyFhhJJAwqQ-NF_u-Ju3WeadbKleUJvQviVlwh0f1_hUrhzc59py7ZyN77zmK0gBid4fO9jnmAxxEDI__HH-1k8JqCY57xsDJVH63370GuLocx3-hJ2WXB94S4-o8899_sypK9BfiPRwp00gYtQbNSlFsYcdYoJbX0FBbfNBLTUzb2X6nCI4bDZY22tYQwUUCgyUO_wUEj3M1pv-Le_RgYth70PALkiHK04BvHEfaZt3FUX4EAGJr-hcmEbVP4YO_P6YfAqQK6veVMBigxtU28eRLeYKeeVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: از حملۀ جدید ایران غافل‌گیر شدیم
🔹
حملۀ ایران به نیروهای ما در اردن غافلگیرکننده بود و نیروهای ما فقط چند دقیقه فرصت داشتند تا موشک‌های ایرانی را سرنگون کنند. @Farsna - Link</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453361" target="_blank">📅 16:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453359">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4a5be6f42.mp4?token=a0cPk6-KDsFqVPrNxn_3l2cVZ0S8DowEYoH7y7oALypfKycAwLH694Mr6T41ityhQUmOaRarwwEE5JR5cPkGrLjCnn1nBeIe-TaHMdPI3C0z9o4qBFMe7Fl03jCgiYU7QNF_78baEu4I8sQdFOqL_H9ceUGKd5JZyYEk2mugaU7UWd7k0rGMI7JEN3xrb5dqwgi609IXDEiQOfZrLo76DvCAvyXyyXI1u-5dosjgJYqvy2RM0DqEDmmiiIBRtSjN8OVaO6fCJqOmnAK9JU7ptPcDbpZo9HUbccz_Q7HGH5hOe-d59meHAZMDFCip6bWjRhiW1iBk2R5Jg8ztlTvaOVJR7Hdf9e9kaBv78d3TOyD7i_gNHCNZoLGLDv2dnpgTVLylP_VqSprE7G-MhHHtRs4gK-dkbdosiHmA8yPbsNRJ2rXeAaUceisPB4ieewn19XdLecI730y0_aerX1rBmlstv-6aLpXfS0Icv2oumIZnSrBL_51-LP22-O9VHOmwB33h4GAJty-fuG7fYEfM8N4tlbnBA0qxcddnZBn6k3fBamiPPzuzoI4EwRZT3I_MFkkqlq5g7rW56RTKlA9tzbWe7H3KjHSGyPD4OsjenbeilQSXUzxOePyb-NAn4-nRSFW4PrBLv9snhukqCIOL1v_3XiJ-qbBi3m-SMGtWxCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4a5be6f42.mp4?token=a0cPk6-KDsFqVPrNxn_3l2cVZ0S8DowEYoH7y7oALypfKycAwLH694Mr6T41ityhQUmOaRarwwEE5JR5cPkGrLjCnn1nBeIe-TaHMdPI3C0z9o4qBFMe7Fl03jCgiYU7QNF_78baEu4I8sQdFOqL_H9ceUGKd5JZyYEk2mugaU7UWd7k0rGMI7JEN3xrb5dqwgi609IXDEiQOfZrLo76DvCAvyXyyXI1u-5dosjgJYqvy2RM0DqEDmmiiIBRtSjN8OVaO6fCJqOmnAK9JU7ptPcDbpZo9HUbccz_Q7HGH5hOe-d59meHAZMDFCip6bWjRhiW1iBk2R5Jg8ztlTvaOVJR7Hdf9e9kaBv78d3TOyD7i_gNHCNZoLGLDv2dnpgTVLylP_VqSprE7G-MhHHtRs4gK-dkbdosiHmA8yPbsNRJ2rXeAaUceisPB4ieewn19XdLecI730y0_aerX1rBmlstv-6aLpXfS0Icv2oumIZnSrBL_51-LP22-O9VHOmwB33h4GAJty-fuG7fYEfM8N4tlbnBA0qxcddnZBn6k3fBamiPPzuzoI4EwRZT3I_MFkkqlq5g7rW56RTKlA9tzbWe7H3KjHSGyPD4OsjenbeilQSXUzxOePyb-NAn4-nRSFW4PrBLv9snhukqCIOL1v_3XiJ-qbBi3m-SMGtWxCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
انهدام ۴ هستۀ عملیاتی گروهک تکفیری و بازداشت ۱۵ تروریست در جنوب‌شرق
🔹
اداره‌کل اطلاعات سیستان‌وبلوچستان از شناسایی و انهدام ۴ هسته عملیاتی گروهک‌های تروریستی-تکفیری هنگام ورود به کشور خبر داد.
🔹
در جریان چند عملیات اطلاعاتی در شهرستان‌های زاهدان، چابهار، ایرانشهر، خاش، تفتان، نیکشهر و قصرقند، ۱۵ نفر از اعضای اصلی این تیم‌های عملیاتی دستگیر و تعدادی سلاح کلاشینکف به همراه مهمات کشف و ضبط شد.
🔹
این افراد قصد داشتند با اجرای طرح‌های خرابکارانه، زیرساخت‌های اقتصادی، خدماتی، قضایی و سایر مراکز را هدف قرار داده و امنیت استان را برهم بزنند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/farsna/453359" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453358">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38ba69f36.mp4?token=m5Ojv9C6vNLwno6MkLRv8utWEROTisHbAw6NFYR17ogbH5hATW1s3kOaKCrDA-k5guc6-DY1uDcmQp-ieDeKDoF_QhvdXEvdtny7B_htDY_df3mZWdXkVA7SBacpyLDHz-cB0rv0YH_bLbzxsB8dlMlEwbI-DVSVAjy7TxhgjIbKVcmR67f6sMOGlZcmL4hBy3u3HSgg2e8hH9Jak8eeF5dMj9zmuaTuYnIj4u8Mi0UGg3HthA00adljeopMhvFGYIgD8Ndjf-_aTpkn5q57D_IKgjgpw4kzEPKUqBt_YCw3BxnRfhhdop5yiKETKqTn7LH98a5ya7MjjkXxplIsEKIoqe8bf12iT4HqHW-X3052XUVrS4caK05bk9meEFcwLBaqI6scckdAyfPMFlJn9kuNCMHQySPlFB8RQXHD5KGKYOKvOb1-qgDDPlHzG8f5jsxc20Ur7UfL9zXwdQ1bvUiGmyT5uooO6_8f9gukTaHJeqfOKRJY88xXKR1qKtJpPKdfl6M8AM7ckywasFQSHjixFHwdvjFcydDEMBFaF2QqdUZQMyqz76j-oKJL84rwko7Xy6M3Pn7349JjzDkOKLsfAmei90mkLsk8EzihTS84Vlyu7oliwiACxIhaNjPJ2UcpaIrMAPChq2lYDtoJXnZIguaM_YrHlBNLctlRJXk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38ba69f36.mp4?token=m5Ojv9C6vNLwno6MkLRv8utWEROTisHbAw6NFYR17ogbH5hATW1s3kOaKCrDA-k5guc6-DY1uDcmQp-ieDeKDoF_QhvdXEvdtny7B_htDY_df3mZWdXkVA7SBacpyLDHz-cB0rv0YH_bLbzxsB8dlMlEwbI-DVSVAjy7TxhgjIbKVcmR67f6sMOGlZcmL4hBy3u3HSgg2e8hH9Jak8eeF5dMj9zmuaTuYnIj4u8Mi0UGg3HthA00adljeopMhvFGYIgD8Ndjf-_aTpkn5q57D_IKgjgpw4kzEPKUqBt_YCw3BxnRfhhdop5yiKETKqTn7LH98a5ya7MjjkXxplIsEKIoqe8bf12iT4HqHW-X3052XUVrS4caK05bk9meEFcwLBaqI6scckdAyfPMFlJn9kuNCMHQySPlFB8RQXHD5KGKYOKvOb1-qgDDPlHzG8f5jsxc20Ur7UfL9zXwdQ1bvUiGmyT5uooO6_8f9gukTaHJeqfOKRJY88xXKR1qKtJpPKdfl6M8AM7ckywasFQSHjixFHwdvjFcydDEMBFaF2QqdUZQMyqz76j-oKJL84rwko7Xy6M3Pn7349JjzDkOKLsfAmei90mkLsk8EzihTS84Vlyu7oliwiACxIhaNjPJ2UcpaIrMAPChq2lYDtoJXnZIguaM_YrHlBNLctlRJXk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
محیا اسناوندی، مجری صداوسیما در کربلای معلی: با وجود همه مشکلاتی که وجود داشت، مردم خیلی بهتر از سال‌های قبل در اربعین حضور یافته‌اند و این مراسم باشکوه‌تر از همه سال‌های گذشته درحال برگزاری هست.
@Farsna</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farsna/453358" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453357">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8wSGO4wDNmrShAd4fc-VhY04wY7oOr9wroxzHp89rdZ-8UbISymr9Fe8KwyFh3o6VnieS8ocHTo4EylEAQzmlJNd_cuRp4bEtLcK1S2keqeepA18MOeVi71PcoM3IgCV5xtXeIVX9q7mBcatnNiY4cP2FeboKnZgZCKFMnIcto6OlfgSxVuldHtOLu5_IXg5QFipHXoV9wnt9fKhSnJMP3S6K3yS0_BIuduH_WjfPl6c-drFFMBXlcMVZ2liMIEYaXL5rjlp-TeVhk_XZGXX1NMR-P5_eHvbymaL5Qxr9Nc-fiXqlLrCSAr03tk_4N5Yi4yBnwrhN9otZSfs-JYwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: حمله به «شبه‌نظامیان» در عراق با هماهنگی دولت بغداد صورت گرفته است.  @Farsna - Link</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/farsna/453357" target="_blank">📅 16:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453356">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f22a9d150.mp4?token=oBo-mqIGpNYsaVa5BOq7-aA9NANLnXpWgXSCqoGRe8He-llNbKuKnxGeTlRJgz2UCf0zBO6_y20b6h9kIm2WWcUnTTeEEZm1GEbeZl9A0d2lm5s74zaXya1P14ebScIJ99LsW4ZnLqlcGpJ4ekHfMg8RW9KJh09bBcclBGfVlBE7Qm6499QUHmxmlLQJVrpkbEKcahMG5YA4bE5uwfb8Pub6Dgca5K-NYGqgG0fXtFAeY_Cyixfpm7LlXQIsifemDG5hv1CwYL2dnUTB0hjJ9A-o3XzCFrmTcJOlj64hCZSs7liMfNpRbR-f4-asfSriZRpy6u4RVIJmalEgHqdxL4eM8hQaSH2XKJF3z2ZCjBgHig6fX588CLb694eVpwsVMEzy0uKXl-FIk7hiHlAv0APFC954Qb2-jCxFP8BUX6Tzkw2Q0du7AGRYDQWQQEJVMt1XTifUA89KxjANYmIlSipK5BtjWv6fPBXM_dFCu8Wawn9-HcoNncogxHFNSL6swJY3Nuim-q_4UUAqY4CYnOw-l1_lSVTVWoPGqHXBEc4tLP7JC9yr56XECXJvu8KS43sa-pciPX9IUhdiCx8cmQzLBtU8jks0yab8NdbwD3uz0CbL0ZsfWLxPfuDLhj33cAIdRWmceiOfxSpG1YcqeZOW2ei0UFJJdY3NrcJBpxY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f22a9d150.mp4?token=oBo-mqIGpNYsaVa5BOq7-aA9NANLnXpWgXSCqoGRe8He-llNbKuKnxGeTlRJgz2UCf0zBO6_y20b6h9kIm2WWcUnTTeEEZm1GEbeZl9A0d2lm5s74zaXya1P14ebScIJ99LsW4ZnLqlcGpJ4ekHfMg8RW9KJh09bBcclBGfVlBE7Qm6499QUHmxmlLQJVrpkbEKcahMG5YA4bE5uwfb8Pub6Dgca5K-NYGqgG0fXtFAeY_Cyixfpm7LlXQIsifemDG5hv1CwYL2dnUTB0hjJ9A-o3XzCFrmTcJOlj64hCZSs7liMfNpRbR-f4-asfSriZRpy6u4RVIJmalEgHqdxL4eM8hQaSH2XKJF3z2ZCjBgHig6fX588CLb694eVpwsVMEzy0uKXl-FIk7hiHlAv0APFC954Qb2-jCxFP8BUX6Tzkw2Q0du7AGRYDQWQQEJVMt1XTifUA89KxjANYmIlSipK5BtjWv6fPBXM_dFCu8Wawn9-HcoNncogxHFNSL6swJY3Nuim-q_4UUAqY4CYnOw-l1_lSVTVWoPGqHXBEc4tLP7JC9yr56XECXJvu8KS43sa-pciPX9IUhdiCx8cmQzLBtU8jks0yab8NdbwD3uz0CbL0ZsfWLxPfuDLhj33cAIdRWmceiOfxSpG1YcqeZOW2ei0UFJJdY3NrcJBpxY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
علی صدری‌نیا ، مستندساز و فعال رسانه‌ای: شهید لاریجانی روایت می‌کرد که برخی حکام عرب متوجه شده‌اند که آمریکا و اسرائیل خیر آن‌ها را نمی‌خواهند اما چون در مدلی از رفاه زندگی می‌کنند نمی‌توانند پای حق بمانند و مقاومت کنند
.
@Farsna</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/farsna/453356" target="_blank">📅 16:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453355">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromكانال اطلاع رساني بانك كشاورزي</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7QRRMAbO1vjmG1q6w6WbBH3dlZWoEomh4G7x0pJTJlxfeDzfBeOo-H-gT0KZjB_x1ziGoSg4YayLbgi_jEVPafgiiX6ioG2KgnWyj5rI48tBMBLrB0MtStccLbyby2NsH8yzplFCXrG6BaeR_dvYeWUEeDgXxlzrYkXSwd_RR9quDb6aqo9jz5m6JJgyuvfGxHs7-SbQlfwbnt3kxEIYV9zRr6f3jagV3EUKnM1wTBCLik2eGhbqlQA11_dckg3pUH1N5CPDzSBcUzOZ91SQwYxLStuI4TAOgz6ux_6Lhdgfvs98fX_O4dV3LSX7IUmk3_NMsyLIueFdnCaixDKRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
متقی‌نیا تشریح کرد:
تأمین مالی ۱۳۳ همتی در چهار ماهه نخست سال؛ رویکرد هدفمند بانک کشاورزی برای تضمین امنیت غذایی
🔻
مدیرعامل بانک کشاورزی با تشریح عملکرد این بانک در چهار ماهه نخست سال جاری، از اختصاص بیش از ۱۳۳ هزار میلیارد تومان حمایت مالی به زنجیره‌های تولید و صنایع غذایی خبر داد و این اقدام را گامی راهبردی برای پایداری امنیت غذایی و تقویت تولید ملی دانست.
🔻
وهب متقی‌نیا تأکید کرد: این حجم از منابع با رویکردی هدفمند و از طریق تلفیق تسهیلات نقدی با ابزارهای نوین تعهدی، جهت تأمین سرمایه در گردش و تکمیل طرح‌های فعال به تولیدکنندگان و بهره‌برداران اختصاص یافته است.
🔗
مشروح خبر
🔶
🔶
🔶
@bank_keshavarzi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farsna/453355" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453354">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/farsna/453354" target="_blank">📅 16:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453352">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jb7J9kf6GDom_7FN484BEnNl5zj1n6v60xueTJS_xGqUWRK2PBwVHifICltmFoX02qRjZmwkaQkJ8IH3WhSuiTmv8Wjf85r32jOSijX39qdX-IdaSV5EgC73VAa7gSFPn11Z9I9fot7SeMfbabtEqjJ0xqsG_ibMWeRMJjrttvgC30bceM5rSLnWgmMGOSHsaQXxNOc4vaJm2mVaDgmvPOd6N7TXGwiBzfzGIxzC6ZXcEZFyGSi1ZqjRgLpjK2gkV11ztwcXPmYX990mcBHAUdPaXvY5VCXTJGRbxo7m9mljiPWWCv7mbhEbYHMTC2G5mDbE1-iIO8Od1pAyGwcK4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجهٔ ایران حملات تجاوزکارانهٔ آمریکا و عربستان سعودی به مناطقی در عراق را محکوم کرد.
🔹
وزارت امور خارجه ضمن ابراز تسلیت شهادت جمعی از مردم عراق در جریان این حملات تجاوزکارانه، بر حمایت و همبستگی کامل جمهوری اسلامی ایران با دولت و مردم عراق تأکید کرد…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farsna/453352" target="_blank">📅 15:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453350">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee822b028e.mp4?token=TDye5COuYPEZLqXnj2UK5ALShUGAgYygrvdIBPtYticIwTkfq8U6_90G8NXLq3l16BOagx0u3L_tKaCz3-ivqPfSUIwAU5Z6JOlTkcb9juxrlV-8wg9LuXnkBEYbrBzaw6vK3Wm-mnJfJbsJzIBG5YKqZp_zo7B_cW9_7BV_gouycvTJDEZY2tFOzvRivLvU9JPAntOjuyWMsBKvJjQX8B8KeCVZ3r3l2ILZqrDtUWGlOImBtVe6FrNkfLcP67KHcq8OU9unifkW_FC69klbd6Fawt3dR25JPEGfHmDBJAO5B5WIvwHWXLlVusMc78UgkmV8Y-VON3aWmR8FIwoKmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee822b028e.mp4?token=TDye5COuYPEZLqXnj2UK5ALShUGAgYygrvdIBPtYticIwTkfq8U6_90G8NXLq3l16BOagx0u3L_tKaCz3-ivqPfSUIwAU5Z6JOlTkcb9juxrlV-8wg9LuXnkBEYbrBzaw6vK3Wm-mnJfJbsJzIBG5YKqZp_zo7B_cW9_7BV_gouycvTJDEZY2tFOzvRivLvU9JPAntOjuyWMsBKvJjQX8B8KeCVZ3r3l2ILZqrDtUWGlOImBtVe6FrNkfLcP67KHcq8OU9unifkW_FC69klbd6Fawt3dR25JPEGfHmDBJAO5B5WIvwHWXLlVusMc78UgkmV8Y-VON3aWmR8FIwoKmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
گاز سی‌ان‌جی رایگان شد
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453350" target="_blank">📅 15:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453349">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ساعت کار ادارات قم تغییر کرد
🔹
استانداری قم: ساعت کاری دستگاه‌های اجرایی استان از روز شنبه ١٠ مرداد تا اطلاع ثانوی از ۷ تا ١٣ تعیین شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farsna/453349" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453348">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/068a507fb7.mp4?token=qz_pRzi_rdZ5nOseg9XqQn9v9fi5UMOmMkkU26OcXvHHMpOsTt6qDoiziZFdkwtys_-x02gjX14ghop9PGJkLUoxEvS90sVEu3tajAoviwSQpd5fNdzKO8ZaWG0Iz2NiyTRXlFF2RQllLvzB663_ZfaJ8QK--E0585zsnJIZkd3bmVeuj0rcMZV1NXbBMlhcHbtGZIhsJ3hL1WmOvmAPn57BUpDVU9m8txF9vL8NY4Co5F_1XUM67tG_EC1VVg6MK6m15i5uGQ_VZ6xnPomwApNGNN2knQmh_u5f8d6jphwHmXXLSGgxEeH_36Jug3QAjc-7rb-BITljzJPb7orTPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/068a507fb7.mp4?token=qz_pRzi_rdZ5nOseg9XqQn9v9fi5UMOmMkkU26OcXvHHMpOsTt6qDoiziZFdkwtys_-x02gjX14ghop9PGJkLUoxEvS90sVEu3tajAoviwSQpd5fNdzKO8ZaWG0Iz2NiyTRXlFF2RQllLvzB663_ZfaJ8QK--E0585zsnJIZkd3bmVeuj0rcMZV1NXbBMlhcHbtGZIhsJ3hL1WmOvmAPn57BUpDVU9m8txF9vL8NY4Co5F_1XUM67tG_EC1VVg6MK6m15i5uGQ_VZ6xnPomwApNGNN2knQmh_u5f8d6jphwHmXXLSGgxEeH_36Jug3QAjc-7rb-BITljzJPb7orTPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
حال‌وهوای مرز تمرچین
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453348" target="_blank">📅 15:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453347">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WAzlT0RKFRbtwIQMvNuDcsXvQcMbeED_M5ttQihUvN4sjkwNgbaWgkuXseNQ22PfxcFmFCXceZ2c8zgSM6SLy4PW6rIIMyXGlf4WQZW4y-1dRe-WGJxiVq4eykSIQ5rqZLrIBwGPjthVPTwvxL2utA9BpIwh05m91r1zwODKAUAbItsfhDrKlWzGA4PlLLnrfOcPQ9UhEuZGRfvZ6nbPX4WPxTY6wzORUJt1yXMumYhkwg_HtE473kxtbQV8g5kuU20a9FFvd03Q03RVkBychQVEqGU2kT4NS1uhuAb6MYEMimB00V72k04fs0cCMY2epsXw2NotfZ1GTmJA_kIXQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلیمی: طرح دوفوریتی برای مقابله با ماینرهای غیرمجاز تدوین و بارگذاری شده
🔹
عضو هیئت‌رئیسۀ مجلس: در این طرح، مجازات‌های سنگینی برای متخلفان پیش‌بینی شده است.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453347" target="_blank">📅 15:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453346">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtT4STsWE8hXomBZ8ZiTUofKG-rR9y5jUuwaS-77Qx-jRdtnIeB5WBlOvGnLGgs0e1_SI-hi5cCHc7FMGqYjpxoI0BBHv85rgV9ZyDQfoTqHm2Z13t71z6JKaUqI1MhqFSSil_uuy-zHjpKLxHq-ZJeaMxiv4bDRvlloxKEFPICOEtpFEJB9HIzvUM1VGtOuqSVc1REmmRD3BFFz3daE8EXSJ2nqWUwnyH95HpBRZvR5cuot5hAs4i9rwgbNXPXEaKEbZK7D3bI-Q9MegVQIaDdAgNUHlUWFJUsDnjGJ1xWSBUI4VMtwKruBL6W3U42cYTjSzaukOUCHpTZVxTGFXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکم جلب بین‌المللی مالک تلگرام صادر شد
🔹
یورونیوز: روسیه اعلام کرد برای پاول دوروف، بنیان‌گذار و مدیرعامل تلگرام، به اتهام «همدستی در تروریسم» اعلان تعقیب بین‌المللی صادر کرده است.
🔹
سازمان امنیت فدرال روسیه (اف‌اس‌بی) مدعی است تلگرام کانال‌ها، گروه‌ها و ربات‌های مورد استفاده نهادهای اطلاعاتی اوکراین و گروه‌های افراطی را مسدود نکرده و این موضوع به انجام حملات مرگبار علیه غیرنظامیان کمک کرده است.
🔹
اف‌اس‌بی همچنین ادعا کرده این کانال‌ها و ربات‌ها در برنامه‌ریزی حملات تروریستی و فعالیت‌های مجرمانه سایبری در روسیه نقش داشته‌اند.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farsna/453346" target="_blank">📅 15:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453345">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفارس بین‌الملل و سیاست خارجی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPGI4UB0YJU_wxax2zIA0LV-fvXdS1iUy4_sid0eIc_M0JHIHO0nTOTKKfl4GgZXIgWAxPCMaaBoYrwub_TQSbv5seolKrF1pDlCgPK3fxul18V_dIAeXDojR_zVs7WO7j6q2TYc0PUR4e_3Rm0GmKv3mmIrCGCfgn9GjgfDoLDl7rT7n08oFfPeOLHcCfLzx4UhTN1aHD2ZDC1YkFR8ljFyJ7R0KeUiRgsBSXRmXcpjv6AuhPMD5VSKgdU1xjw1qwEngvpH-w2sBf8GO9cArKO-c2vtazFLBmI0I9T0q8G48JDvnC-pmR6lKMTqPLpGYYAM4ODGLOmxaDZDrKJX5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هراس آمریکا از ایران؛ سنتکام: تلفن‌های همراه را کنار بگذارید
🔹
فرمانده ستاد فرماندهی مرکزی ایالات متحده (سنتکام)، به نیروهای خود نسبت به استفاده از تلفن همراه هشدار داده و تأکید کرده که ویدئوهای ضبط‌شدهٔ آن‌ها که به صورت آنلاین منتشر می‌شوند، می‌توانند به ایران در هدف‌گیری پایگاه‌های آمریکایی کمک کنند.
🔹
به گفته رویترز، این موضوع تا آن اندازه برای آمریکایی‌ها چالش‌برانگیز شده که ممکن است به نیروهای آمریکایی حاضر در منطقه دستور داده شود تا گوشی‌های خود را تحویل دهند.
@FarsNewsInt
-
Link</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farsna/453345" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453344">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HsfEciVYbCSdqnOPQiICayS6fMNpV0pqzrLgg1ZhXiMhvcjMroaiwr0HmcDALzI_LHa2rspgaLLYL6IviVOVOgNLbCvaTo0aaZJFmo_Sl5J3DdSU49KVDLOIp_xEg4u8t4qxiL8dlNwHbAinNX9BH4X0P6Umc4A662SjvGMtQ5JGF1UXUoyxU3wQuYRifclM2WN517quLMVn9YRruEO7CQtCj6ZXHduBmAJ96ChmdCaLeNe6wNLM3BJcWuSTlzZV7siH-CQ8YKjZkozol1G3AkmYNIIPW5SfluInp4EcI4RbC43g5YvkobDYOo9Je_lg8B7-uD-meAXHlZlcUK6mOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌
🔴
سفر نخست‌وزیر عراق به عربستان به تعویق افتاد
🔹
پس‌از حملات صبح امروز ائتلاف سعودی-آمریکایی به عراق، الجزیره به نقل از یک منبع در دولت عراق تأیید کرده که سفر «علی فالح الزیدی» نخست‌وزیر عراق به ریاض که قرار بود فردا انجام شود، به تعویق افتاده است. @Farsna</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farsna/453344" target="_blank">📅 15:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YgnlslKgiVD2I20c9SoIHkrhMdeW7cmu39yazTxc5xGNh537sazFUfKPWsCxYUTCjsjXRutVIVPsbEpsJ7rUImV-Mmm1cqmBsIkacgbBPGqwYHIGu-W6aiLsi_ptj5i_LlvaTyOIZoq2BbGoBpmkI7M8U__YpnELIfXJAK-yvEhbG24lR2RaScODvU5HPicgsmGtgsSMMXUaaejcFzGMPWXB5L-Rb0ztWMh6fohXqzVtrOFpSdeILaqg0P-A7X8LwfCR35q60eOKYMWR2tm8vCKSx3KifjZHOBW4GqUgPUV2uPPsIJOtOxPlGdhK30-3IXatZDEfOGoGACxrWfp_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عارف: وزرا و مسئولان اجرایی اختلافات را به افکار عمومی بکشانند عزل می‌شوند
🔹
اگر میان دستگاه‌های مختلف دولتی دربارۀ موضوعی اختلاف‌نظر ایجاد شود، باید در صحن دولت و در حضور رئیس‌جمهور مطرح شود تا راهکار لازم برای حل آن گرفته شود.
🔹
هیچ دستگاه دولتی حق ندارد علیه دستگاه دیگر اقدامی انجام دهد یا خارج از سازوکار دولت، تصمیمی برخلاف نظر سایر دستگاه‌ها اتخاذ کند.
🔹
اگر وزیر یا دستگاهی در موارد اختلاف، اقدامی خودسرانه انجام دهد یا اختلافات داخلی دولت را به رسانه‌ها و افکار عمومی بکشاند، به‌گونه‌ای که موجب التهاب، نگرانی یا تشویش در جامعه شود یا اقدامی برخلاف نظر دولت و منافع ملی انجام دهد، دولت بدون هیچ تردیدی برخورد خواهد کرد و تا عزل عالی‌ترین مقام آن دستگاه پیش خواهد رفت. دولت در این زمینه با هیچ مسئولی تعارف ندارد.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453343" target="_blank">📅 14:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453342">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHur3ttqWZ0FDfYZB5A8uDk27XWB_527q8r5AsuvP4QLBbXAjFGxtp1lhXej6DKDWXim3VR2VONRvRuxSo-R9SmkLh-8kWl-cREC_eWSYh9cf-igWslbvYvw7Nd1zXwGHK6lVbrxmXeeLOox55BmzAQL0kHY764PM1NoXtBuZeoYKGcbUqU2w5OQ5g8VEtnLpEOIJI3taLHJvVr7FgIqugRiFIpjrR_MoboZ86fXzEPMw7t4fjM1-YB-ggCYfuqQkO_DmRE_4q5NW5YWxU5upTcWlEmjbAGuAPM0_RB4-fc24woytCTu9OUc_pMiWSTd5mShvy1lDJQWn3LqzDH1HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خروج ۳
کشتی‌ ژاپنی از خلیج‌فارس از طریق مسیر ایران
🔹
روزنامه کیدو ژاپن: ۳ کشتی مرتبط با ژاپن با عبور از مسیر ایران از خلیج‌فارس خارج شده‌اند.
🔸
نخستین نفتکش ژاپنی که از زمان جنگ علیه ایران از تنگه هرمز عبور کرد، نفتکش «ایده‌میتسو کوسان» بود که اردیبهشت اجازه خروج دریافت کرد و اوایل خرداد در سواحل این کشور پهلو گرفت.
@Farsna
-
Link</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farsna/453342" target="_blank">📅 14:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453341">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a961d9a0d5.mp4?token=HjakAAwP25qHzvVsotMUmLjEtS9hzifKVkAB6tFvVmJGQX9iDva0WcGbFdG4c354-0NexNIzfkOUf0NzJGv1dqxB5X2kbDKNUnUsA_5zyJVt3cvMGAze2DxPS0JRylg1Eh__YemLZO5dMnZXMA4xFQ-LE6XO11EFnKAs5gx2IRE5kLrlLUPpMxIeA3HlCp-MSOXqXrs5hU9f9oZ_YLMc2wy6BjlAcWtVxdrf6DP6hSV3eQ2KJt_Bys2dMQ32YWwqE3ilfEY5C6uPAVxXTLbg9LKdjQIlLSa6REsa7-k1UbD2qutNk8rrsDF07oPRxtmCi3skF57xH_Oub5KiCnW6GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a961d9a0d5.mp4?token=HjakAAwP25qHzvVsotMUmLjEtS9hzifKVkAB6tFvVmJGQX9iDva0WcGbFdG4c354-0NexNIzfkOUf0NzJGv1dqxB5X2kbDKNUnUsA_5zyJVt3cvMGAze2DxPS0JRylg1Eh__YemLZO5dMnZXMA4xFQ-LE6XO11EFnKAs5gx2IRE5kLrlLUPpMxIeA3HlCp-MSOXqXrs5hU9f9oZ_YLMc2wy6BjlAcWtVxdrf6DP6hSV3eQ2KJt_Bys2dMQ32YWwqE3ilfEY5C6uPAVxXTLbg9LKdjQIlLSa6REsa7-k1UbD2qutNk8rrsDF07oPRxtmCi3skF57xH_Oub5KiCnW6GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
سفر دریایی زائران به کربلا
@Farsna</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farsna/453341" target="_blank">📅 14:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453340">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bXunJNJOS5WEddZmeQwEshDWdqljOgvIPGrG340ut522noI_u8x358k681ls32KKvQw5R4BAw-B1WCoDKSJSsaN9Sahtsp0zZCn9Q7d4i-CNBNiT1ReKqRPwWvtaV9OvXbGAcNbusqnHvblNHXdchZRb2dgqd1XipSZg35dd2PNkp88aymFsTg1odQnWZ8R5qS0KEmS3QPWzac6X0TLzNwxcjV1KyySQTsfwJ3x_-hPFhjf90y_8P_VagUntiu-6o4o7LD8xm4jQO80oTlz3Aa_JXODc-mnx6hzUcl5wIpo8Ls88npQkd-4Tx3B56x94_AiPFpNPmzPY3o74XsAwSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌ آمار شهدای الحشدالشعبی به ۲۰ نفر رسید
🔹
الحشدالشعبی اعلام کرد: براساس اطلاعات اولیه، در حملهٔ تروریستی ائتلاف متجاوز آمریکا و عربستان سعودی دست‌کم ۲۰ مجاهد شهید و ۳۲ نفر زخمی شدند. @Farsna</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farsna/453340" target="_blank">📅 14:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-453339">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/017513eea3.mp4?token=bhTzv_hqhxw7eB6joJpkwanXzj4thy3LHgo6L2t-Wg2FXtqm114vbwUj5iyNvBzyJ4hHaS6RQlkpe87xMOhhDxtl1R0-4VgQXNcAx8cFahooHM4jmUzm0UFK9CnIUHpaxpD5-eRsCrYyeI1OwCwBWwhb1hoY6l6glZhe7lZLeeYPElUas3wAO6_v1cN0afL7cSH56Nz4Lu5_3Sly3_tDcaEP3SfwQIxqUzD387N0vEwfZEUJzminXr-TtNHOwCAmvqslyMdPiYCt0Aelkd-b6aNKZRFK2pEW5lKidxY9ph5AR6x_mGPwd39Or4h-4Yft2MGro49dAzR4tF3D3pfvSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/017513eea3.mp4?token=bhTzv_hqhxw7eB6joJpkwanXzj4thy3LHgo6L2t-Wg2FXtqm114vbwUj5iyNvBzyJ4hHaS6RQlkpe87xMOhhDxtl1R0-4VgQXNcAx8cFahooHM4jmUzm0UFK9CnIUHpaxpD5-eRsCrYyeI1OwCwBWwhb1hoY6l6glZhe7lZLeeYPElUas3wAO6_v1cN0afL7cSH56Nz4Lu5_3Sly3_tDcaEP3SfwQIxqUzD387N0vEwfZEUJzminXr-TtNHOwCAmvqslyMdPiYCt0Aelkd-b6aNKZRFK2pEW5lKidxY9ph5AR6x_mGPwd39Or4h-4Yft2MGro49dAzR4tF3D3pfvSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎥
اقتدار به روایت صیادان هرمزی
🔹
صیادان جزیرۀ هرمز تصاویری از اعمال نظم ایرانی در تنگۀ هرمز ثبت کرده‌اند؛ تصاویری که نشان می‌دهد کشتی‌هایی که بخواهند از مسیر غیرقانونی عبور کنند دچار دردسر می‌شوند.
@Farsna</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farsna/453339" target="_blank">📅 14:20 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
