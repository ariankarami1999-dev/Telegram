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
<img src="https://cdn4.telesco.pe/file/NeDnU-n1HsV2ECaadhJeWzAy7hxOTmaza1KHJwzd570GgiL7PbNbmXiYrsedGnaMlfVeBUmYGAXCE_Gnc-QNRvFfR4SArASGdPL7X3Sshfnhm9AunJie9y3a2h4i49XFOhoizDUMTU7k1X6Hw0p3VGagb5NAja6-oBbTxA_i3z_urUKdtBvLTlAiz22Pb_RkBx6qZTCxvCbAoAold_GQbNjSXUnsipX1nRcrlT729wV3YvS_6s_TMOcn5Kk-LS2_JSawIIS0yXigr4oRwY3G6A_i8g5C6AD6ThzKzHtsS17yF5Jk0HvRDVc3HXesTGal9dRo9iSt4cc41wmdP3Y3EA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 442K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 21:14:38</div>
<hr>

<div class="tg-post" id="msg-30628">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbj4JoSxJJj4U9Og02u9FtfN7V1pRXQyTq-74lPSbpUEhEqYN2DY9t7oSXXZnrG9IXZ6QW9dp8OdTfBwebdTChWi4aUjcgRVqQwKeSEVN3-tN_qWHCZYS3KUT_atKxp4NGW2t_9OjsrihALlZhhdSHLmZhOBJrXI6lInL8-9mrkCxsWkqNt7umH14ziEU6PJcwihC9awz5YoTK93d9I4ObkEkGp7HpR-Ce2CnD17UQJ2QvBS4zBWPf4PeOWK8hQLLQUnPfZru39B5lIkY__wTveThwC1kCITySLpN-z_ucElM5SZDIBgFc81yN1RJwj283QADTGHvTS5QYHdQva5hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pj82N7KtlFGFduJq2Ikg7ALvMmj69AyzO7QU2p14DKJ9zOaDim8xhxwx5r7zYmmAVRhVT_-HzoE9ydegElkhc2XWMf8HahiAGcPXypCC9nO8sIBwiaQ45UhzBeXsOdwXwHBM_7omYPZYNVi3REvIOsX5nnX6qaDf0gcwv4gtIu7wLLzUSCLdNKmrX6sW3WjGPB3zygZJ7aolm1cL-yJCpkFv-TNiA2kpa33mgoAJlWGvBMGmBeg4iv_WMPYjH_vKIH1a2YMR428KxHzesvOM2nZn1iPOlyJHlPodPEpxEDVSfAYHqS7Gd8MHpOKZictasj66wG1wX1IwuqfFoh_V2g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی بلژیک
🆚
فرانسه؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 912 · <a href="https://t.me/persiana_Soccer/30628" target="_blank">📅 21:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30627">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmGF3UX-xbvuKxNEOxvD2gQZqd-ku7kYH1SUt0T5aNf99FWZX_wSG2yyCXh-w-zgUKYO9AKRijM2feRW_WziaSsDMahLiEK1Jr_e7zg3AhVWpMS5925VByRjFItM-MMr7G2IL2SRoQ7_0MHwD3UMdFMu6irvrrWAFWDCCKJ3mpyrpB4PqG17imLWVA1Rnnnu2PaxkFs0pnG66YjbTo7wSB3l_BvGG-jvsK7POpoUj8Xvh8vtSfrQqv2GBKZI4U61YUa42PaskwoiZOQOZolBtXRDGdKtspACOLp_u-CFKitIA-b2vn00ln-W6yjjh3zjXRngk-6A_yUAl6gzQkosxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جلسه‌نهایی‌اعضای هیات‌رئیسه فدراسیون فوتبال برای رای‌گیری‌درخصوص اعلام یا عدم اعلام قهرمانی تیم استقلال در فصل گذشته لیگ برتر از دقایقی قبل برگزار شده. تا ساعتی دیگر نتیجه مشخص میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/30627" target="_blank">📅 20:46 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30626">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgGm4pEFXjGJyaVehHAsiBvvY58B-s1hfT9YfWYNRy3NBOIFbKVTHrZsj3U00geY2bV_dxyTEfhdxaldImZWFFBBTim5QhYLF8ARxIYUGHluvS9eZ_SyD4O8AjkSLXdJCIf_xiLhd-cktmVDsrZePPJXU-mT9_X36VZBRTgc-S3GtEEpH2B2oYpm7Qu_T0HaH4tcU4yUUllswEZWMgM6P7QjktFLalrw0DntnvIFHSdSQLYhCLuQIyxXBTj8CGkTAY4QWIpve1L0ue3JK828exTHga8KwoqgilehovUdhkpx_Mkh3j2-ed9xLg9HFWP5SvkgWOG65HFyO9FPbOtH5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ارزش تیم ملی ایران داخل ترانسفرمارکت به 25 میلیون یورو کاهش یافت. یه‌چندوقت دیگه تیم های اندونزی و اردن هم احتمالا از ایران بالا میزنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/30626" target="_blank">📅 20:31 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30625">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=a-JGq64iObWQWurpGR5RZrZXgIcdXVV5OA36bgebhf7b2V93jY5KayKFw6j42Ez-x4uu89LJr3ngog53_AMFHTmBcJ0cNHy3LCEXB34ajfb3iPTEHlFmvi6RuV_TMwfR2jq5VEys6C8y_3nq1ORfwvNv_NHJNFg1-EfywR5_JQh1r49Vzp87TttXzcU-V0dVMZ6tg89yW020n-Mxwz75Dp3RloWkzY8zLKzn6RaiHTcN9j5seQisxrXsuoDf9QDZkYfwdbinIC2dQKG52oj3SCUplpJunAo_0oSkGUqKnc1ayWLXrHcwHtrWyKjveuWSSFQ66ANyJ9-twnDGbbPeJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/769a519ca4.mp4?token=a-JGq64iObWQWurpGR5RZrZXgIcdXVV5OA36bgebhf7b2V93jY5KayKFw6j42Ez-x4uu89LJr3ngog53_AMFHTmBcJ0cNHy3LCEXB34ajfb3iPTEHlFmvi6RuV_TMwfR2jq5VEys6C8y_3nq1ORfwvNv_NHJNFg1-EfywR5_JQh1r49Vzp87TttXzcU-V0dVMZ6tg89yW020n-Mxwz75Dp3RloWkzY8zLKzn6RaiHTcN9j5seQisxrXsuoDf9QDZkYfwdbinIC2dQKG52oj3SCUplpJunAo_0oSkGUqKnc1ayWLXrHcwHtrWyKjveuWSSFQ66ANyJ9-twnDGbbPeJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
حرکت زیبای رونالدو برای هوادار نروژی
؛ یک‌‌ هوادار تیم ملی نروژی پیراهن تیم ملی پرتغال را برای گرفتن امضای کریستیانو رونالدو به سمت او پرتاب کرد. رونالدو هم گرم.کردن را متوقف‌کرد پیراهن را امضا کرد و دوباره به هوادار برگرداند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/30625" target="_blank">📅 20:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30624">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=nsIsIKSxBc7g6X_80V210go2BUN8zsNNh8FPTLtb89e-QHdbhyZwpWZxJF1NwcK7yIyQ1lN82rsDy5wHskzFhrtJHVujzWprWz-hn6ZVPSIak-TprEOG2xS-OJCTHTcitgI-HEu21A-ZS_H2HDCCyZIQPvt_lcHNwQmRCNJwnUtUI5pDnkWvbPVHawkuZln9fdfYhoOV1CLv5X36JthnF6yyQ1_owEhV7ch7mid5P4mHGFRHIZnibBuAf3Uv8CBGSv6zShmEPXHm0HF9m2cEZ68i2ZhBDfm5HVE5OXNqYrumMYD2uJLJNl-097WH1OHEMANo40P88rlte3zB04WEvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/712c04d04a.mp4?token=nsIsIKSxBc7g6X_80V210go2BUN8zsNNh8FPTLtb89e-QHdbhyZwpWZxJF1NwcK7yIyQ1lN82rsDy5wHskzFhrtJHVujzWprWz-hn6ZVPSIak-TprEOG2xS-OJCTHTcitgI-HEu21A-ZS_H2HDCCyZIQPvt_lcHNwQmRCNJwnUtUI5pDnkWvbPVHawkuZln9fdfYhoOV1CLv5X36JthnF6yyQ1_owEhV7ch7mid5P4mHGFRHIZnibBuAf3Uv8CBGSv6zShmEPXHm0HF9m2cEZ68i2ZhBDfm5HVE5OXNqYrumMYD2uJLJNl-097WH1OHEMANo40P88rlte3zB04WEvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی زیبا و ساخته شده هوش مصنوعی از علی آقا دایی اسطوره تاریخی فوتبال ایران و آسیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/30624" target="_blank">📅 19:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30623">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ERNgPgdxVDOc9ew31SPNgUqvB7PArcWT-dN1MzrVPnpiyyM44aJx8WbH-LkG3_jhxyyFsPXSFwHxk5pHsvyK0zBcg73Sv0s6KUJTgvCaUVhuPri8TuX9tWYX_OoXrLU6_2P4-6QugnnRLxG8Fw_R0Jwm8LiTpcDF06BQ5MYTmxmZ2PHU4UGMbLeWJgv6YLoKSej_9i3kh08vM5cGDPAw7o8EQe76LMQqnge2TdH8IcrcZIumR3v67z5QNNgY_TzECXTqZhV-ZUlbj5WJJvATF75PJcOMZ02EeCJK-uYr3xMrpWZSrwkoDYCDG2TnEFSWisXHhbBVyb7dSUqQaOJv1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
نشریه‌آاس
:ژوزه‌مورینیو پیشنهاد سرمربیگری تیم‌ملی‌پرتغال روبخاطرپیشنهاد رئال مادرید رد کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/30623" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30622">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJar3lpii55wgw2Fxv0Co3e8wGSZ7nBIaWhjAB-v1OzxWshXjSTY9UIAB108KmlvaG9UUfKG9mKbvM8MrsqtKYGcLTXDyd_AyEtJ0q3KgBHUcoXPSL9rUCG0BBThxJNR0BZcE5yGd9Jlu8CO9xeVFoPIQfFBNViYpaEWaUThXlcqcd_Yiwbytj7IHJ-xy0f2aDeYqF7uEh9TZPG-TwUwnw0V6CE3sq0oj8qgE3KwePw36V88n23uJxrBeofWYccIg3sCEj6zcL8zM6HEP46Zx1bySacFRxVqMBcoS5uy9A7pPjmAGsLJxT5O3yd8y63hzzbRkYy9MQlTUyba4i5QE_BU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/808bfabc47.mp4?token=cIrmWkE8c2seGETIquXLwj88EQvpCUyWm8eUMoF8TE5oOMN6vvBhErHqUtUMbJwxOzq6I_q8bE9vNZhP25_B1bMBSs3BYL890cTN6LLss-PRpEkD9LsvzZB7LEwc0mzi2KZrJQpvNwiUpA35oZAbHGy10_lvYARo0-GxGYhm0k-SbLKDI3Aq7P3WcWYFIRB5jzdt542jfGfEjmuuMkaPuLHrLM0Q0XkYxffGNQIdlc0jARobUlLIXSe-69BXgAmKkSfHg2hPr0BMjMfKBWn_-aMms932Ajw7_EuOKFjRssk4IOv5ESpAOGvALdFt_va0s-RkOQajv6u9w_LdTJ8GJar3lpii55wgw2Fxv0Co3e8wGSZ7nBIaWhjAB-v1OzxWshXjSTY9UIAB108KmlvaG9UUfKG9mKbvM8MrsqtKYGcLTXDyd_AyEtJ0q3KgBHUcoXPSL9rUCG0BBThxJNR0BZcE5yGd9Jlu8CO9xeVFoPIQfFBNViYpaEWaUThXlcqcd_Yiwbytj7IHJ-xy0f2aDeYqF7uEh9TZPG-TwUwnw0V6CE3sq0oj8qgE3KwePw36V88n23uJxrBeofWYccIg3sCEj6zcL8zM6HEP46Zx1bySacFRxVqMBcoS5uy9A7pPjmAGsLJxT5O3yd8y63hzzbRkYy9MQlTUyba4i5QE_BU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
👤
ویدیویی‌بسیارجالب‌از آنالیز تیم ملی فرانسه سبک زین الدین زیدان در اولین بازی با هدایت زیزو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/30622" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30621">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCp2ywMX7zrPRAZP43oSCgX9yfhtgXLXJ1mZ6frB4sszk3gy4IHsLRNaWEiep0kwUoHU89kEz3DQ2xn5zxII4SKoVVOUQLC2q0I6MmZENwd6q8DcHYgbfGv3c4nupnPo4EHQ9aLlnFfl497SW-7JX1THosCrCEhdREk4bgv2V2QuV7L7KfaFxydTlM1mQf_fg22QBUlR5c4z6llR9sOOaXzVLEdjtCAuu2OgtaPidTEMYkZpXaOg-zsokzHTL-scaaGzll0qvPIdD3CdceIJQJS7EoYzxB_dMM7HDe42AAb7T_HPztScs3bK5dBq-XhX-gKr-OF4mM8G8gv3z8CcpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
خیلیا نتونستن از فوتبال تا الان سود کنن، ولی ما امروز با فرم هامون
400% سود کردیم
که نتیجه تحلیل درست و تجربه یک تیم حرفه‌ایه
👌🏻
هرشب بالای ۸۰درصد امار بردمونه
✔️
میگی نه؟ یه شب
بیا آمار چک کن
😄
فرم های مطمئن امشب فوتبال با ضرایب بالا از دست نده!
👇
👇
👇
https://t.me/+laf8I3RIuq42MDk8
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/30621" target="_blank">📅 19:54 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e3BU4ce7ENJIDS7n5CuQ19UvScgCnvr3RCDa4jBxSYYsg2Zr9Po7MkehTRoFDW3wV95UcjoJ-MYoCyKgmROB4jf7nLV6SW57tLHO-WPKrV5_Fs5RaxdO6trGbUbw2e52ivB9ZPkZIf9OgVF0R7JVwoNIiMKd5E5RwsjVMmlRYD-Nqlnj0uSZfD7aTml5TWXLdElHb3dFS39mATg89TGbN8KQEsZGUbTXq9I5XNaGm6HczFSfIKADWIJg3wp1zZtqebgaQ2FAI_SmTBtC8g5zIj5nwNHQmEBl0lmA6m_32dIVsox4hKWmHZm-KPf1o7K5JGF7CqbvctP0nHGF44MD_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eNWX8DMgiB6HVPpUBucP_M2bG7C7X3bv9NFIldgLIqqzpCN3ok5ODButtkRscQSLJtsm77lTfGKxge-gIlpOYcGetQDRRrTCMAeXga_V2IYbaPdlSEkHdUa_gvJUfchzrJeRnVxoUanJBM3FqwFeGKwZqy1PDDHPo-EGCe2DltYRE--KWGI9nBCTv5eihiGY5p8C5KOVdcO_926EV5dmJKQ-dNg9jDjwTLSn80IBKykWZEHnytWQYITT7jfffmlr7yh_txD0OJGO-150HP8cXxB0iLcfEvIhJ9UMKsLD5q9epNcuQUYW3diqd2PLh_T8K5LX-wWA4bJq5gofToskAA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
جدول پخش‌زنده مسابقات ورزشی در شبکه جم اسپورت در هفته پیش رو..! این پست رو یه جایی سیو کنید که مسابقات رو از دست ندید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/30619" target="_blank">📅 19:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=YhTHsdh8nK5x6TbMm6r14d-dIUJv7rpv-jHUfV4dFN3pL1rV-5S74yJDxVJV23E-qcfwkMXaIBGMzFQYa_oIF6sdlAPQpbV7Ax3_C3eE_9E-p0OeXsTCAAxGIOkKFjuBUACBiwYVH26GR4qkckv18JnfuiRRdi7icvmCj3bKZ8pl_pxGhRAUydEJoEyIAVGYWWitLWqyE_IARqjNTDNhM1bcILxyrgxp0sBKH4mkEDAORm7-Ogax6UAB3FnjA9G1h-XA-2_c-wtAGoG89NHkVVP21-YYqg8KGdFkQrewbp_S-Dn6u-MfVkeSH9aeaRZWSli5lmNh60hs5kMitXSxew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aede9d046.mp4?token=YhTHsdh8nK5x6TbMm6r14d-dIUJv7rpv-jHUfV4dFN3pL1rV-5S74yJDxVJV23E-qcfwkMXaIBGMzFQYa_oIF6sdlAPQpbV7Ax3_C3eE_9E-p0OeXsTCAAxGIOkKFjuBUACBiwYVH26GR4qkckv18JnfuiRRdi7icvmCj3bKZ8pl_pxGhRAUydEJoEyIAVGYWWitLWqyE_IARqjNTDNhM1bcILxyrgxp0sBKH4mkEDAORm7-Ogax6UAB3FnjA9G1h-XA-2_c-wtAGoG89NHkVVP21-YYqg8KGdFkQrewbp_S-Dn6u-MfVkeSH9aeaRZWSli5lmNh60hs5kMitXSxew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتیجه‌حضور تیم‌ملی ایران در ادوار مختلف جام ملت‌های آسیا؛ سقوط تلخ پرافتخارترین تیم آسیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/30618" target="_blank">📅 18:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmsQb83asXGLQxOn7_zvrKByF92W2bjFRhLKrJCR3kHFcmVTnFTksucT3euhtK2rdRMZJVAE1ac7T09dh5h_2f-SIWZq5jw7T45rUxg8wmYtSRDIeOmijTkvc0iAKES_bTddYWlFUADoZTkyh54DiLmd1IF37ID2K646fcA457YfPnut7E4tg1hX4wFsvcfIv1cpAIJNqcYQ2vUmxGUUP4vM0rSnVyQJ4C_z5u7URYyxQmToFc8BXuvXS6QbdSp2ePEUViqYNNaXIB8QpEPKBwyh5cbp41ItwZk-ziERUTdCucj9FjuOsKLzfUufBRH7dpolptATiIKDEuzfeFXCig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/30617" target="_blank">📅 17:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVDgQuOiRna9ncHCXXoS5wbois57tbjgEEPZgyHCyTobgRNmtIHDyc2KhR8ddULu4QifNtakZwxkO-cvqpXLGKh06EuAoqs6ckZLeYScpMrDxixZoiTH6iINDI44RjhU-BONdmnhFkwbXtj6D4_stfkY986-Q3CPTKMI-FWpGdL-h5jMMPnwWnA0_waNxeLtzRjz0Nhrq48KuVUl3TzHO5wBWUMF_pHnOLdC62RiZGeIuQz42hNczputpzV-K6nawrdLGfrsTq6D6i7b0LFEzml-4bXO79jTfN65z0ou4id32BKeP-obbpl13FiOSBUFPi1080YDH6UnjlEteSedRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درهفته‌دوم‌فیفادی
؛ ژاپن در دومین بازی دوستانه اش دو بریک ونزوئلا روبرد و اروگوئه که در بازی اول به ژاپن باخته بود چهار تا به کره جنوبی زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/30616" target="_blank">📅 17:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=OyTDwBCJWT35sESuETiXtRBLSTbM0EktFHDdsH_6ZT_vpDte_ZzrZiOVdzyKkZABZi_luLVPPL36lligQHX-T-RzzvWnh5NnFvoA7byEEVd75nxdoicv-JoTeKx-5zZPWy-3LWoAJkoftDa8aI6GXsmtBEgnzSgb1atTkpNOxeBDokuv-C9v9I1fmsTQECOo4uyPLA8sYlpcB-BD0uxpnrl4_dyr_ci74kTzXOK1KsRH9mmI5SjHY7zK84PNtosiNXux2l4_Yab3kCov__ZI2wzNtpCuj3SjjNBJvUozE9o4R1HYuEYaUklcdxZXSsxjiS-YSGRxlRbdtwmgF3cymg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256eec1e5a.mp4?token=OyTDwBCJWT35sESuETiXtRBLSTbM0EktFHDdsH_6ZT_vpDte_ZzrZiOVdzyKkZABZi_luLVPPL36lligQHX-T-RzzvWnh5NnFvoA7byEEVd75nxdoicv-JoTeKx-5zZPWy-3LWoAJkoftDa8aI6GXsmtBEgnzSgb1atTkpNOxeBDokuv-C9v9I1fmsTQECOo4uyPLA8sYlpcB-BD0uxpnrl4_dyr_ci74kTzXOK1KsRH9mmI5SjHY7zK84PNtosiNXux2l4_Yab3kCov__ZI2wzNtpCuj3SjjNBJvUozE9o4R1HYuEYaUklcdxZXSsxjiS-YSGRxlRbdtwmgF3cymg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های هادی چوپان درباره از دست دادن محبوبیتش:
حس می‌کنم دارم کابوس می‌بینم. این چند وقت چیزایی دیدم که خیلی ناراحتم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/persiana_Soccer/30615" target="_blank">📅 16:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=YhWFqyX3oxZ81wiesB7OMAAz9bBJ9pDoDRoMdVR5nBhtXuvePH7rmTfZ6WZJczDGsxUj8opdfhjKuth7qxR6O37uddpEXV-aejAg54LlTmCUHreeRe91lW8cSpQ2hI1cDfDjsfaYw063CcwBWrra6TotzxUx6YBKlxnnJGg835LCusogyKRUtU4RggUJTpKKLwuFX3VRu8giDwfO8XxkR5Ro5isK4GGilV7s7lkRquhb-MPtRGKI8ufhgNR_NpPIHcjQShRqhl2OY8-25BaK8lPX9MMQeetN1M19p6_I6xlFl6922hKQoQ6Fyu1-yX5xw8SwgfDSlIfdQZvMC5fBKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/924fb238e3.mp4?token=YhWFqyX3oxZ81wiesB7OMAAz9bBJ9pDoDRoMdVR5nBhtXuvePH7rmTfZ6WZJczDGsxUj8opdfhjKuth7qxR6O37uddpEXV-aejAg54LlTmCUHreeRe91lW8cSpQ2hI1cDfDjsfaYw063CcwBWrra6TotzxUx6YBKlxnnJGg835LCusogyKRUtU4RggUJTpKKLwuFX3VRu8giDwfO8XxkR5Ro5isK4GGilV7s7lkRquhb-MPtRGKI8ufhgNR_NpPIHcjQShRqhl2OY8-25BaK8lPX9MMQeetN1M19p6_I6xlFl6922hKQoQ6Fyu1-yX5xw8SwgfDSlIfdQZvMC5fBKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لیگ‌ایران عالیه؛ باشگاه استقلال گفته بیرو مقابل تیم‌ما بازی‌کنه‌شکایت‌میکنیم چون تموم شواهد نشون میده سربازه. باشگاه‌تراکتور هم گفته اگه آسانی بازی کنه ما هم سریعا به CAS شکایت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/persiana_Soccer/30614" target="_blank">📅 16:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7xKvK8gwRGsFy59cbVCWWLMxeFEwzoUbBD6DgfRHhPYMpoc4Nk_zP0K3M3w9ln5YklpQWfv0uqvDqF6bRdnukJ1-5W-O2JPrAUWuF-a_Hhu9uwD3qrbJI4qBBnwjdNp9nw1CJl8SwL8B61ml7zfleAB-tkeqUNw810yN23YOpPIw7Q_qXH-6f7ADpqrkUcsSmmMOWwsLH__l74z3ajvKLVVDq47SUAItg5udmhyEp1eVVh6W0KRpDwzLx8HZf2gmsceUVc7QbkKSovCVrlnei5fTBN1qMC2Q_VzrSRQNFrm6KKfP_9nhkO81Z0wfEcrpVUREt2-GYZnLwVv02pNOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌عملکردهری‌کین، کیلیان امباپه و لئو مسی در سال 2026 در تمام رقابت‌های ملی و باشگاهی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/30613" target="_blank">📅 15:43 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nJV9vjhB_WUL76gK9Xj5BFdWr3B4U2hPptgOK8MLovQMjyKHtup08TOB7u81wsuzQUTrnmYHwLe1J7Ix8BPGcmekM1XEZUXAEGoAktK6ooa8mtwkIYZkVvAe-X3XdPWsRk_mwmqBg0F6MC3DzvJMH-an2gGN0lTF-Eu2Z17Q27Zhy5GzjptMBaH2gJwuJwEnucKPxZRYW_Z9sGswwayH8sD8Hv7AS4xG4CpXpHaBE5lT47haWJ7MQwHhNeWEGnZaa6Zfm8V5lP0XQfnQJZlJwDsqp8lxdcjE_R6U3sAqZB8F5Mb2lq7-5NS6RUbVBeuIJkpyEUQzqgxjRRpyvRpP9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پزشکان‌تیم‌امید؛عباس‌کهریزی‌و اسماعیل قلی زاده دو ستاره تیم ملی که در بازی امروز مقابل چین مصدوم شدند مشکلی برای دیدار هفته پایانی مرحله گروهی مقابل کره شمالی نخواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/persiana_Soccer/30612" target="_blank">📅 15:35 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30611">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4auGifgjSdN6rZR6t9r15YIUrhbq9ZJPJfZh4J18pUZYdq4cKlkun12ogSLogKOtetuz4_64U9mLlLgvSaed1KRe4VgSEz_IFIYLGd8m5-07zQ136dGaJ0CSSxV8HJOPgXtwbq6oz3Dugw6-O4WH4jhtG4INhlOrd7-dPZReji5KFTrqXQGqXN0C7rKGRoGNxby3ZrzpPOaXocVCg6xTUUGgDw0ZtJ9slh31CRnPbgXZZY7nOtyvPNw5D7LCoOr26Hr0soddHRSF_tFR9zxj1J8luB0NKRZekbpOvd5f_283uo8YrzRD6jofOnF1_n8qk4rydWlcMliVgqPnVB_5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/30611" target="_blank">📅 15:14 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30610">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFLcsAFjQLwxrWasmAMQZr5qIedKxY7wEz7--KRfq2CEHpALRZCJWe6Llp4RkpVuJ19usB-MSQN5OEbpOUfM1iivZh2zxdX5bdSPxLrAQsfrkGoPEPvHP8_7knh1MSVgBvNYlLc7K1rg04ooUL59HVYonEK7I6QjMus5BJW_A-abVVgpm42Ns9E_ILcgqQbKI1ZdJq-QbX_Cl3Vzp3xn7SgbE8SRvwJzKUA7sWvaP0POcFwZkv4g2wV92MPmx-lf2dLGMyPPzxbgvBHQwx0D5jTgqv22kBlkOqnDkkZR61Rx-GuWK5rTteMTwst_MXytT3XRnj3F6S8YB4PtvcxR4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/30610" target="_blank">📅 14:58 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30609">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d5lbHCpjb3qWGGdz5VahU8wHXBe45ZW2Br8LCZs_ZeHV9JStgVdWHYk9k6noej1eUs-nMjgvXS_LrQGLvGrokjFUPxhwhJ2qV1yiqJIoDBsJbZooIUZGQyF6mJcqUBl_bgWawYXj9IBeo9cs0dSHe2H1oBnPnk2Ctl9J7DjrMzYJzmpmrkdoKMGNzpgWnMjmCo7fg64EVtUNs2SSLzctlHPLH9qn5q7ABLz5J5oT5KvUOhW6g1RRItjRCAYc8PRjwLgKCQU_n-dP23DAtRuAv9ZjFViV4TI29YhIZSNVwCRZLlXFSsWeoh9Gxjmh5L_-lUbqF-L9YzUL4mjeeFEMXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افزایش ناگهانی قیمت دلار و طلا نسبت به روز های اخیر؛ دلار به 245 هزار تومان ناقابل رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/30609" target="_blank">📅 14:41 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30608">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=CHfjaogaie55Xll7gmt9yMZGAeKYocAjTB3SbBJb7CwUaOR6Zc7B8HPk7Kfys4A6e0iYhVI1CBcTyEEUdnKWL6YxtCLga77EDIUFh2JWg9whGl9QkUHux84m9-pQg5pqxgcCUxTIOV7G2xJoE900HSYhJkzB2CsW-iIrKY_6Y9wYxoS1DpGqFJBLP61bxoi2Jx-8BavgY9lKVlTKmRODDLvNOhQ3fKAqR6HMcFmY95QgAGaXZgu6Lp16hhCiu--MPWQo3cih7N3WBtxpATF7Ud1JTuipumCXPk0LZK1KY4jx-dbgs4TDXC2psN0hVJ99AaW_8LP7rnu4Gkb79gxw7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9144acd02.mp4?token=CHfjaogaie55Xll7gmt9yMZGAeKYocAjTB3SbBJb7CwUaOR6Zc7B8HPk7Kfys4A6e0iYhVI1CBcTyEEUdnKWL6YxtCLga77EDIUFh2JWg9whGl9QkUHux84m9-pQg5pqxgcCUxTIOV7G2xJoE900HSYhJkzB2CsW-iIrKY_6Y9wYxoS1DpGqFJBLP61bxoi2Jx-8BavgY9lKVlTKmRODDLvNOhQ3fKAqR6HMcFmY95QgAGaXZgu6Lp16hhCiu--MPWQo3cih7N3WBtxpATF7Ud1JTuipumCXPk0LZK1KY4jx-dbgs4TDXC2psN0hVJ99AaW_8LP7rnu4Gkb79gxw7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/30608" target="_blank">📅 14:01 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30607">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mj2NN8cIXQs9NjHhKhlfV7tTh_oK7aSCvxjsOJxiZIecixmXO9gZJFf6EmN7djp6qU-MN60F7c66NwVuwQreQAkXIFSfRkEiV208kuJTqyh6oUHWUSyk7Gw9wxcDkUMefbhh_DF_l6RldtdtkIO1I4-kj1bRxEdLH4R8N1ne2MfwDDfKWj8h7ALuKiZW2JJuTU_8G9dMuyQvKWQErgTBTTrgBhbxdnXn10DSZokVhNcumIRmENb3QlmS0JcIefxeiibAn7svGYnKd6h4LYMR_oLOYmgLD3odrLA95h2nwpNKv9zmVlPNd1rchFZ6Cnql-4vUiVK9zVPk0DrayHv6_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛شهاب زاهدی رو هم‌تراکتور میخواد هم استقلال؛ طبق‌پیگیری‌های‌پرشیانا؛ باشگاه استقلال میخواد علاوه بر جذب یک مهاجم خارجی مهاجم 31 ساله سابق‌پرسپولیس روجانشین محمدرضا آزادی کنه. بختیاری زاده به مدیدیت گفته نیازی به آزادی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/30607" target="_blank">📅 13:34 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30606">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sdDx76XLRvwEGjXwmXR0VDw8qtGmx_4ly8IPlZ-aSUw55xCpbA89UW9g8YN_FeWFb0uqbjHkB5fYUQekqbq1dOlHxj2CAHcWImeeQo3s9ZP7Jju9K7mCzhMNbPLyC2NAg3QQxAAZTxMhCl0D04TOTV0CDnrrs1vmeiiSVo1xYwlv19gWxQ6zpFcNFxi_Aru9roZENpeLt4zR98tlR69P0LEaudTtAFR99lxAzMJqooLEeIF5VZ3z9xD6Pv5Zrrs8KsE5eLXDQxwVcqUL5WiS1DnfqnG86Vq2j2CEgE3aNbzuBEbDq7o3rYQY2CFLIdZLDag7V4XKa-d-l4m8RNb2Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌مدالی‌لحظه‌ای‌بازی‌های آسیایی ناگویا؛ ایران با8 طلا، 15 نقره و 9 برنز در رده هفتم ایستاده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30606" target="_blank">📅 13:21 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30605">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s3kXzoMkJp_YEIjhFo_iaEAlnFYOwvK92-aHd4Hlr5ZOO0Rx_cNB1O_-gGCWzC3SRlMQbCMmu6-GOj922YrneIqLnRJq3kOeTrs-VSYJBTrytgJLAr6eGIbuxIhl_Yg901vIQ2-1lF7yfuiaqa0PoG8UuVhYgxTy44PWD0C9DemIuQaq8hiAKnxO0SAmqP91OjZkUuC3Z7qVfJwaxAG9ttAnEtWrCiX9i9dbFtUoXhBEzBw40RrTvt9xJHnc6pTL9Qf10dDEQbSIWggfGP8fCLykcWqby-T0ZmV_LJZszs_dw8LwsWJxAptutqMeUPEEoQXA_AWKqvdtThG8a-hc_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بیژن مرتضوی به ایران بازگشت؛ بیژن مرتضوی، خواننده و آهنگساز ایرانی‌که‌درجام جهانی 2026 نیز اجرا داشت دو روز پیش وارد ایران و روز گذشته در منطقه نیاوران مستقر شده است. مسئولان به شادمهر عقیلی خواننده‌خوش‌صدای‌ایرانی‌پیشنهاد بازگشت به ایران رو داده‌اند که…</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30605" target="_blank">📅 13:13 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30604">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8rcV-bqzrM_hty-adJGIRs793mNNSQar4zbR4fhJ6SE-rFo97jBbQ5XIIiP4ceK1RyPiJG_Xexu-rUtjT1NgFoOeqFvxXslIN3igcvuREO-PVIj43SSmSPl0sL1QesYac-JYrkEInG40Pn_5MQ-qnU7798bzsDcSRJrU2IvlCwWMyKURiE1tqoW0PSg2YwybbhQsbRP-_H4vSysgPYxEmG36rdi3aDWRLcYI9kWPvxmr9RIkuqdL4XnMu34afNh4RVSg3TxM_OHbtcrxbX536frNwxPDoCCOnZIEhujr0AQFgy-ANMnYspvcBMRulOG3tIcoou0do4atXQDtyty1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
این هم ویدیو زیبا اجرای بیژن مرتضوی افتخار ایرانی ها در بین دو نیمه فینال جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30604" target="_blank">📅 12:49 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30603">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZzgBWSPnWswPX1CBuzPZ23tbw5i2NIl8W21trGfHFtfC5NBZJCAEnP3jzhxc3h3Lms-FgwYF6jmNwj2YZghos0Bcy7KZLpiYLoUkBtuM5VebHcSnMEADQWyp-vWEWTOnz1LYh-6EXFFAa6EkgQliCDgrs3tkUKk3meVaAVduA8jCl-TuesGKcJgQwpkRvPcGlbvSbzgeHaLE0o0RqrYheqxE86jO5C_t6kKKTjlWofp2I71owaoDl9P69ThdkTwmmNpK8xiNP3rE8Vh8GXD68PtKgowQrW8nH9AbzWe2_M60Rhm4fl6b6WGrVy7bSd1GB99FY6pKD4zP_bRFRKhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30603" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30602">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adyOfgFGFnJjuh8UuyYPZpdAM-zSzWck-KhDwJjgqSAKlAPsDc_8ELFKFsjwaF0fIwgpKL_-Ome5ZIRV1D8OYRwS6jgnp87AW5Vf8IILe11j6EIk5yTzDytGXt9nkNnBV1esFc-_Zcr-uoj3bA5GhEgGnI82-ztMrRw__bVIHuf61WVYfYbQEGhZ-NO_J8bvl968tFGlJSH5n--naEa6EfoKh_szHRaGswtGPP46feQrsKKZL8M1EQQ2-eHST1vrDr2pm4ratw3HUV4C1UMFL8nborCDL3qm-6IoS9KO2fP8tO_IEPZsEuUSjMYrgvyRQJ2EYMhOAjFtr56XkJKqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه: محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30602" target="_blank">📅 11:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30601">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO9SF_tkFSeUwNPSLGpeQk3KEIO7gd-jqV-crj_BGhDwpO8_Y9d9emD26JS5hhMCWIQh4_58Mz_ek2_VYJgIQfaigZ6mbIDlZDQRLuNTwMz_Bg9cmFuDiQbm5-PEhWsR_SPC0L4m1neOB6D6hbbNr_fyF9J4QnESoGQDMh4Q9fGIWhyg5mvr_ePW1GsOmo-UfLTp9iW7yG3E2jcYoyioYZKdOnxvxMZkRKbyvsOpQgcjPFD8y3grzTskpkZ1R4qCCmz9a1OMR03zW-qQy3DAqfDX850icSbx2oypQqFbiDvQA_Kk9XRgz9wbJlMgzguJO1G60Rq15Jahyc2aJ9B8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇵🇹
گل‌های‌دیدار امشب‌دوتیم پرتغال
🆚
نروژ در هفته دوم لیگ‌ملت‌های‌اروپا درشب استراحت CR7
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/30601" target="_blank">📅 11:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30600">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUEfx2qA8nTegU2YF4PhFGfTm9amHAH-G1Md5r2j3udNUp90gyICaJTOn9u3CAMablujrqlO4Le6L7SsOCK_72F5Ly5cP7WVheNWZEtDfDKFrlBCLLPbLUzo5nmLwoSU47o-uUyPxV5uf4PwjVX4S6unuPtfoOL7R4ehHBIkvyL4l4okH1hieiQBhGFYgTQjhmeRzN0L8wVfHb7BY8OW7or2DMHA3Z1qznzU-_Tl_5pfy12Os0KKboPd0gCI6iW2fNAOgujsSBrt5PVtaP9S0iNuZwDatK4G-4gb-YteR09ExF7Alt28euHtzH8wAVj1HwKjynL1MGe00qAkNY5iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌رسانه‌های‌ازبکستانی: آسانوف ستاره جوان ازبکستان از دو باشگاه تراکتور و استقلال آفر دریافت کرده و نیم فصل راهی یکی از این دو تیم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/30600" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30599">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPgl5VQzWV_ZXNXIgdONXDJ5KMceqFf-O52striaxCIgXJIfwyAPJ2mLMYrpL1JavGKkEyG5k16sC6FLu2CUXURm7HiKvWXyuHR3Kj9nCSmMC3HsVuy4rmYta0gEEOjuJuLlwBBxZqMS5MiCPgrNAyUNBB8Ce3Kn9egalp4raIPcfPTQh_wwozH7Jn7HMZZ8ja1kz5ZUZFbusqPXHmSqtnAHFOPRH39O_W9sKEchqVZWsP-wr6S_hc_Ifa_2RIDECzr8WD9IsopxtVdv4K2_BY4X3QrAUs42LjwswaWtcVB8oQhtH_0XDXFladdO06YwxiCLAPZPQFQL8k1RDS-_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی از عملکرد درخشان لیونل مسی در بازی بامداد امروز اینترمیامی در رقابت‌های لیگ MLS.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/30599" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30598">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#جدیدترین
نسخه اپلیکیشن بدون فیلتر (WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
r6
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا
😮‍💨
بونوس
100
درصدی اولین واریز
💵
بونوس صد در صدی واریز یکشنبه</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/30598" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30597">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔥
هنوز توی
Wepari
با
این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
😀
😃
😄
😁
📌
بعد میاید سوال میکنید کدوم سایت معتبره
✔️
🎖
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
🙂
🎁
کد هدیه 100 دلاری
:
Sport100
🔄
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🌐
ورود به سایتwepari با فیلتر شکن</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/30597" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30596">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsfpvXekcQyqcdDLKxeaOUtQjHqO4dLxK1wptZZSGITqcdRiO2Gm7S7ORXm8WnaUm0JAjM_b_ByjsX27oqmh5w_fpuwiw6-Sjsp-HWut6knBRc9gK5oGVLbF5ZjRzOPs0I6S0cjbbltCOudwmK-yF-9SdrfNwiSLFe0Zlp3P7P2QZLcEHxBsunetyemjOt83zwAJgQV2w-ygzsMmT8mr-3EG8fghYyGQsoPGrduK7PcMzlw1OTZGU64UceDIHpk1yI1JS-KmAClyMVpWEzOeIgczhRjGpiiHsktecvYThZsDXOR5LVnvP-k7xdZ1j8bAot40ixQby_ZZ2gqE5ATzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
سایت‌چمپیونات: شیرزاد آسانوف هافبک میانی ۲۳ ساله‌ازبکستان‌از تراکتور و استقلال آفرهایی دریافت‌کرده و احتمالا راهی یکی‌از این دو تیم میشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30596" target="_blank">📅 10:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30595">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njbGmoqtayDmQcGMBco6xv3OPX8oyo0MqdMk06pRTqlWDLcVYxic15fgKt8vPPqjAv49oMFYkN89olP8d2VVQ_DknmvpJSxDjuX6zlEpaeO96sPCUjhdvTQz8phz94Wxxy6SHvAFboyxZUckabYHT_g_slBS73cs0eJcacmyC_9clnBvt2onSVsHsA-jlbPoB88lCfw2mtmhmGXwrTgLomdHjuL-Edeaqdo0POTSiHbERhLTSFP_8gH5LRLBWFYbnKp11NGXsfCeFXF96hvsNRBQO6uYFlFC0VlCj6cWbI36hHm2sfbm7yi2_1QvkiaZQScruTb3ukwHxFhk-OkVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/30595" target="_blank">📅 10:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30593">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFaYN4ac8dELxEUad6ebRlc0aRTwaJKahX7UERe0TEzVLbQg6vEKFfuHN-ximO_6YNxfD8EENSw2DVBg3D67MYG4o72qPCT_5ijYno_4nCSPx8frpYGUD-DpYDXc7WkmFlJFd5mc8x0XW7H4ZZ-thGmGNrHRgpOcUXrR-eNIVpSH1TwRa8iJZPeEsMhVcESpXgdqmx7PX24bUQ5ackR0OA3Dnvb4MrLbYShtJPHQhMNdCKdClGDU06de3Vxp2njV_GQceWctjlElO_o5OiBRIGRaDvEffC1eFhDHARzy30dDhoKAmOfm7Tn3ayqZkclWDQYhcVGquW2RDyoGRmHgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=iKgJhAo1SilNKLybDujok1p7T8gectisaIC12FUxPOk1k61vnSoSNwHHovOfStKbx4uyulryzYp33vTsn27OgPP79iw6rdBhjviL60eo9B500JdxJHpc5JrCoSBAQIQiFjTUV-fwEGZMiqJG-FDKrKmv0SN5XchpA5D0ZMOhw-c51qjYQB94mjmA-eM7P-A6RVBGRcQrMX9I6i-zOjx4xAIE_j7_-g6gokQJUykv5iRD6OXfM7yQYQGP9loYfzI10imbh3cexpDPiiGDrbOf9qkDAjQXQwFBxBIk-HSbse0PKeKLxia3VHYWWjGmhftGbR279Lb90ut8w_-l-rhh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=iKgJhAo1SilNKLybDujok1p7T8gectisaIC12FUxPOk1k61vnSoSNwHHovOfStKbx4uyulryzYp33vTsn27OgPP79iw6rdBhjviL60eo9B500JdxJHpc5JrCoSBAQIQiFjTUV-fwEGZMiqJG-FDKrKmv0SN5XchpA5D0ZMOhw-c51qjYQB94mjmA-eM7P-A6RVBGRcQrMX9I6i-zOjx4xAIE_j7_-g6gokQJUykv5iRD6OXfM7yQYQGP9loYfzI10imbh3cexpDPiiGDrbOf9qkDAjQXQwFBxBIk-HSbse0PKeKLxia3VHYWWjGmhftGbR279Lb90ut8w_-l-rhh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیدِن‌اسکپیومهاجم ۳۶ ساله آنگیلا که موهای بسیار بلندی داره در بازی اخیر این تیم در دقیقه ۶۹ به زمین‌بازی اومد و دراون مدت کوتاه باعث شد که دوتا از بازیکنان کارت قرمر بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/30593" target="_blank">📅 09:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30592">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=CfUn0ki9yAqFFXDKhvfFJ0_WqYU6ifUvr-MN2zTRlXuAWFJDSWL7V5GbXMMwvU8TyKoRrTmkoTOrYJuIKcww_DZRs3NHh9y4xNW73SpqaLJiAtgg0Q7w1flycaHq5aKfAKjDRXi4oylZuko54Rwy9V6WQCcW0il3qmLIG3dIk_rd0JoYIZDMdAoyby4A683IPKgOtQ_lju5lsmptbG6kzfAzDUFhkFTuUaLW4QYfkhhjDNJ4_TKBaAb2Cnwybif6-hito31oV3LeqQrp0uj5PgTOwNb5QEIRef2t6tqZwjrQPoThLZpRqEyUgLHmTZG5bbuycbk5I_tx9a2nKBKelKlhLTFX4x-Z_VdnaYoF6ZYC3PvGNUZavrrM-82hkOtMrKu0NPSpWb4nvUGxSc4gz2UxQK4-B5Avkg3-40eHyeKEp4i1Llo-WawlMvmtIM3GYc__nJIuMb_BShnVr3TxX_ky_-swOTrV5F8uqEslQPY4Of3JweH5ReJkSJ9AW-FfGbB6iLORt1p9v3pHLCsMM11Oa9411pafjxjssTDV1Denb3XwvxFz5AoWB3XnzXXcy91IxJ6oJ-ISiZEprnKQy_CK2Uv2JwxFulQImcn3cGF4ckU3oSsJoIQ_14VRt0LqOJu9WS10PkEmbvgWB-b2L2pqYMhzckrE3iGUutjfcsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=CfUn0ki9yAqFFXDKhvfFJ0_WqYU6ifUvr-MN2zTRlXuAWFJDSWL7V5GbXMMwvU8TyKoRrTmkoTOrYJuIKcww_DZRs3NHh9y4xNW73SpqaLJiAtgg0Q7w1flycaHq5aKfAKjDRXi4oylZuko54Rwy9V6WQCcW0il3qmLIG3dIk_rd0JoYIZDMdAoyby4A683IPKgOtQ_lju5lsmptbG6kzfAzDUFhkFTuUaLW4QYfkhhjDNJ4_TKBaAb2Cnwybif6-hito31oV3LeqQrp0uj5PgTOwNb5QEIRef2t6tqZwjrQPoThLZpRqEyUgLHmTZG5bbuycbk5I_tx9a2nKBKelKlhLTFX4x-Z_VdnaYoF6ZYC3PvGNUZavrrM-82hkOtMrKu0NPSpWb4nvUGxSc4gz2UxQK4-B5Avkg3-40eHyeKEp4i1Llo-WawlMvmtIM3GYc__nJIuMb_BShnVr3TxX_ky_-swOTrV5F8uqEslQPY4Of3JweH5ReJkSJ9AW-FfGbB6iLORt1p9v3pHLCsMM11Oa9411pafjxjssTDV1Denb3XwvxFz5AoWB3XnzXXcy91IxJ6oJ-ISiZEprnKQy_CK2Uv2JwxFulQImcn3cGF4ckU3oSsJoIQ_14VRt0LqOJu9WS10PkEmbvgWB-b2L2pqYMhzckrE3iGUutjfcsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30592" target="_blank">📅 09:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30591">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=jfit6_Pjx1abThf4eLWRHcykR-bynWqXFFaouYSkGN3fffzqFEw6n7fYJdjzW9JC7vvjpstjdm_4dQwl_qIwHMR0y6dSyBLsm8KvizE2w0TPv35CxQ7HUs2CX-w7aN1W3kbfIeo1OjeU9Mj-eiEZ04vXhJsZFq4mOjpgcaNpYhzWPGwNNYO5DIH4J1asHpdXDxsWvl8kHyOChQX8DMoTyV3ifr_DnMFlB3kW2AbwyEQUagBdQ_vvDmf4AIKlQfPB1X1CiQVmWMiJxelvMk_C1P6DSj1EWVA_ErDzSequ8v7OHxZqlv0xVCC_TyjPD-CIb5FVMNFjfrEbsWLmIiKWwA0eg_wqLnfskmTKIsXfUK9aif33zGHfWV-h_z5U4t4LCReUuzFQ5-YJOTSDvuV_B-asFdqPMLpaZLt-KwYyWWKnRifej_LjFh9u_AiulmNq7rhPkjS9waJFK0Xt6PtTl8u25eVks5OWpGjEWdNgnAaKX8QXkFo6sLlI-Y6GU002O0P4ftE8zlheluPouiFwFOTnX0eI4MqtjsUkLtTFTWRNayhXwN-IO0UKMl5L3kujVylpl4-Lj91sVdoIdUR-UO4OwJh-LdIAbT6nwb-3k3Cr1YYitcfkh4gYYh4Uiv4UDhuj8EQCBdWPtjNCFHPRRyUnmbjPoTUERTz_c9vYwMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=jfit6_Pjx1abThf4eLWRHcykR-bynWqXFFaouYSkGN3fffzqFEw6n7fYJdjzW9JC7vvjpstjdm_4dQwl_qIwHMR0y6dSyBLsm8KvizE2w0TPv35CxQ7HUs2CX-w7aN1W3kbfIeo1OjeU9Mj-eiEZ04vXhJsZFq4mOjpgcaNpYhzWPGwNNYO5DIH4J1asHpdXDxsWvl8kHyOChQX8DMoTyV3ifr_DnMFlB3kW2AbwyEQUagBdQ_vvDmf4AIKlQfPB1X1CiQVmWMiJxelvMk_C1P6DSj1EWVA_ErDzSequ8v7OHxZqlv0xVCC_TyjPD-CIb5FVMNFjfrEbsWLmIiKWwA0eg_wqLnfskmTKIsXfUK9aif33zGHfWV-h_z5U4t4LCReUuzFQ5-YJOTSDvuV_B-asFdqPMLpaZLt-KwYyWWKnRifej_LjFh9u_AiulmNq7rhPkjS9waJFK0Xt6PtTl8u25eVks5OWpGjEWdNgnAaKX8QXkFo6sLlI-Y6GU002O0P4ftE8zlheluPouiFwFOTnX0eI4MqtjsUkLtTFTWRNayhXwN-IO0UKMl5L3kujVylpl4-Lj91sVdoIdUR-UO4OwJh-LdIAbT6nwb-3k3Cr1YYitcfkh4gYYh4Uiv4UDhuj8EQCBdWPtjNCFHPRRyUnmbjPoTUERTz_c9vYwMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بهترین گلزنان چپ پا در قرن بیست و یکم؛ لیونل مسی فوق‌ستاره‌آرژانتینی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30591" target="_blank">📅 09:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30589">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALpMGnodzvG-YuHUB-WeUoC3kbM9eaAZc-PByh5qS4Crew7mLYijPYJQH38hIMxxDB_mgha7O6M7YqK3tnzEZFvYwWpOz4dxwj1Q06u73U0-O04BFEtMJTOBcatcF3sn6QGZmWhH8hb8GsIL0zYJqssyXKtg1XwD1nsv14SNsQsbJsT2DiLJosCOgIMHnmHJWeZZTXy5kpl_ieShH5WkuTvzBLHvvGUEODwO_OMz7QogGIRpRJqMuVKNqBoFwlt1BZW8MYz-oD2WWU5npmHWDPCMojppwO9PaKbTr20mvBYoLC1E2pNT16_WwxFjawEyCVSWktjoPPJqkdzWi_r0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1HhnJ5CZLiezPrmneSRk5Nw0Sa9_d89Gk5nGoNGPDTCuIn6SGoADuXlR_6Fs2DNhoA0ZyBMMvihabIhXylt5X4LtEI9nciEP_g_1ivU2v-7iJ_1Ze-59H0LpFDxy1CExz8LmeRU_UlcXSAlfV_SJf8EV-YOHXPxWVGHi7x6xUk_oRkizrM1Y-m90fmPBAS1psP3refdSq6uAIryF-33__VQ2ygy4x37MCniaQTe-xTIPuFlmFYUMp45j5kC49wL7hvTKfVMxYUl6-7Q_7-0efWAZGZJXilZ7EQlMw7kkxGrRKKziG88XgMy_YR_iwZcXKDDPagJaWpunGOYKZ5kdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/30589" target="_blank">📅 01:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30588">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLDbd9pw1PojICQXadBrd-zYBPSaupVkH7SnrhJceLwm8aDU5xYGF9IFQb3kW5fcyDwdvj1ySp-3ZYY1Hi4KgiCW8be0Od4sqQWeZPnINYxVSMBsQlVkMJQev1x7q_G8cfhQ5FZGdmASPMH_qRansZT8i8Sgf-KoRohGYkFXWRXcQ4U16KzheWyk7hDp6xzAmqYhA3kd5agyRjXnO9SmFPeViYukAj3dgPG5Cl1cqzmwq_Yfkbp7U_Mqoa3ycPXJgyT_-7ZN84lU3oRH4Pld0cm1DU2jdHQKp5PuHR1tqVhwszX2JY27h15FV7nvi4RSf7hzoWvymKPgierLNqGu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30588" target="_blank">📅 01:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30587">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aw8lz1rpSbz9xAfIduZVCT-tw3K9Zdr5Y1z8VKvMUod_5dRA55Td_ZB5Ntt1Y4Xh9_HsI8cY4ugxtm4sQPnfpk8a6QhlIcIHjUFWARQKsUHKQay_wDU-mWNJV3a6tOJM3Pd_3jQ48TX1wn9pH9AaKvGxwaF2VnIX4D8u8gfdVpL-dLU9IJj7P_r87Fbh121bsLZpdwSJ9m_hGbZSOMVAxpzW04PcsvTTyflmja4ivzs4pgykQP0xaVV7cbK6kNKZpoXhwpeXKLhSSujaX62Ms0ihLkCq5dlienl76GxWy1B4DQ-s_8HZYML30ePcoh5VJpXLlRr4JijUAu16Cjj9nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نگاهی به عملکرد و افتخارات شش کاندید توپ طلا 2026 در فصل گذشته فوتبال اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30587" target="_blank">📅 01:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30585">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgTwp3C2adBwlljqs9InR1-cWWXSiRSTj9UCzHhWCeVTgCP3bQ4ijrJq1VHsvUfLUlBSlj90XijW2WoFoPYsRa49CDbBWmfJzH95vXAd0tpWLZQC2qweE6U7w_TfDtJglU6xP3rf1VlCTtkA4D0DncasgYmLSsi6liwRUuR3fZNCwtMY6qp7ffyLVyYONv8n9JBetGuc1mmEws-o4bFM3o6vBn5rs8ySAtFpjRSULyh8d1HyXQIJLu6rUXJ8TTZCmdq_1cbwWm-30ZLCHyXE8XERd9bGIGABU8zrQw4_uctysb9NtvUGQ_L3Um6YWthlyLQXZfl0bZRP9vZHa7zDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌ امروز
؛ دوئل بلژیک - فرانسه در غیاب امباپه و رویارویی کره‌ای ها با شاگردان فورلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30585" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30584">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cvW97VY0VPQMNCKMY8IQpQHOcRNtuBPRMYK67bjkl4DJJneuZhXoX__P8JJX17R5rIK-m2MvOlxrxdpNNa-sQcQgCMdPHhLHdFJsIgERr4HqzDNJ9FezTmarLvAqOwGchC4rsYja1MzEYIPlUvthewAosEBIHSzkaLrhjS7ahWllAA90P2SrVnwuy7_rkWvA1O0pjFAmcjIfz1ZpDbZR1pRyark1lm5PN9FlPe6SmGKGTKHYa1h8_xNhSXTzuCBxOSUQeSgn0DtHdkFdiaexVU_N-4i1YKnv3aLf-DmWr1c-QyoohMYSEg8sriUQRzPt9fwd5GWIFFCxmTe8NbygSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
اولین برد ژاوی با هلند و 6 امتیازی شدن پرتغالی‌ها در گروه با برتری دشوار در خانه نروژ و شکست عجیب ژرمن‌ها با کلوپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30584" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30582">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30582" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30581">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U9_E8S-YOy3j14DhuSRROEgtyrUmd_HJys19z5tywwHvqYqCTXqw3UjoxQ7gsDA4GUxUyftZ5M37i8CxgA5ISzGqbgL76mPh2Sp0XYPr4XMgae-qOChAxashC8vAmYa0Cup2rVi65xrFHC9AuJFUa_gqQG4yL1NfAy4laNk4bAnrhqDVp1CeF6wkDJolkcsv5bcPPfmNa4kRBIt-ppWrsyVkzNF1jTxxAQBhL7j_GZNPW9DrFoXNr2jYJf5StWOJF0zazrjV865aUd0MnDT1oBCwJRoKNWJ6ydlWhankhK84RnQ2coN4mJE2W2cgDdMHqYe12YT8AUo4Hu9g5FHNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30581" target="_blank">📅 00:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30580">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg0VLM29pAksRb95wXrbtC9TDqzt58IzlJYXfRBLZNtX1IMroGUp1sODBLLpBtH6rStoZSpfrqi3LyTlvr6CBm_uuL9-EwN08yrEAkt5oRt5fdHxqH6ACFMDuvExIwgBQJkOOiSS6nGcypoqRY-FSpFpLEgfuv5o6rLgJYuT0oaq6AlvC-s3lfHEc5HkRKLbbF4QRwD_P_w7oDEayYVgBgDt9r1B5_ACID_z5nFnOW7tw3UAE9szEY5FEuPMNnW65XGGY76XVAfv4U6u_cBPkrZvti4123O9M5UJlcL_IksRSVehokwygCMmrbcqvpt6UczcXsLbtXCUuQUMnBvBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی پرتغال در واکنش به نیمکت نشینی کریس‌رونالدو: رونالدو بهترین مهاجم و بازیکن فیکس تیمه؛ امروز چون میخواستیم دفاعی‌تر بازی کنیم و کریس رونالدو 2 روز پیش بازی کرده بود تصمیم گرفتم امروز بهش یه مقداری استراحت بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/30580" target="_blank">📅 00:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30579">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WyPnwvotNdT6H2yRyOLBw3C0MN98DnwPerMdgUoAr-BRXyw5_Dmm79_52y1bKiw5VXHAufgrBxOwecsAq48WiTnXqe7-A_0P6gyDGbCsvLuLG1aeB3ocEiDZqMGDYkJQnIky3eKw_XJXLpHc1Z-RmJ32c7N29cuaFGsbw_G1CUR0luTCyY3HWGpJ3nwLPJ8I_bkRdJE34nHWq0V53soqRoKNVQwL10k2_y2_cYQz4maEMAKvj5iSq-nlS_b5tdQsZidUGcOaIgl8kjUy-wCszqMcPfw2ikeLMwAkgTLxNN0-uR9iAHhrS7Bi_X67FvIql-VB_kg-oRxrM9AKVdOX8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دوایت‌بایکس‌فوق‌ستاره‌باتجربه آمریکایی که سابقه بازی در NBA و لیگ‌ برتر ایران رو داره با عقد قراردادی یک ساله به تیم بسکتبال استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30579" target="_blank">📅 00:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30578">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RmG7ucuWUReoSHIOus7RLKp1gyDNiIkXjBCl_aT7pLg57fVFYJlXlyFuYKBg8vuO3xg8QDUiJXD4UuLLpcq9q35DS8rKFFSt-bjdaDatGWvOPZoJjFwBFFjKgfRHmzwjehohqYLGax0ya7Nm-KZCyVQ65XotXEn2XR9-VaNRMVboMykkFbWVudUYAH4mhutLmFzhb9Y_oqeehEgKIVUGGshLgcxTehIamXUF4sA2wStxL741OtWaeoBvYjeB6nCgxWYrmrYftll1A5P8h661SZoK2Ctw9tku9Y0zG0SiSFM6H1ok9qvlmwUqx5leYZhQVvj9pFBxLmf4p-s-FoLYYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30578" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30577">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV79CUWQMDfYfZIkVSJUzfS4FrXlab0a_7XOw5P_GFGgXa-t9vpKBCtHCN4erRDQxl7TIcx9PhcyWY22mLQTgRT2yZ2n5mVyGqfA8YFBKiP_Ht_JYCCKWu8Gy_Y257k-yRltgVb2KlcWPADpcQz6di93xuUVU-jYT_Agluu_h9WuoB5KntHyfgUN0VwsVbwmw5sVSt4E7XPSHwvXvWHUl66E1Rx1Oy_StRBzCU9Pt_47D-JC9HeBV4jB7SXXyi69mTH0Fo2QwrcI9UAHADaR4GkalfDZCLlHPgrs6E8_0mM8NvYWPU_u9VUAb9IxQsoD7-lkSo5hyHdCFllnSrby8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته‌دوم لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی پرتعال
🆚
نروژ؛ کریس رونالدو روی نیمکت پرتغال قرار گرفت؛ ساعت 22:15 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/30577" target="_blank">📅 23:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30576">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0bCncHb9PfQwbHGYU-yEwkk-1kNEnZenTLsGAt3Sq70q5cKcMA6xzkL2qbur09tBd_jaXkqVL1_9QN9IhG96ju5uoR9aWV8VpQvDPc4KBZLshr1ori8Qr1wZ2pJPsplZ5sVcm2IufdincmeKdWmDOqDHalm4pr6NdpS1p4yvlAWT4A5tvd46szJ-bzEwScX2JBVmpv5T4JNrcl8UGbDFqeUu2FqMJl8jH_MHivXo-S7br1bc4iBqUIfUnJBaeUDpdW8ZSbXBmv8Lhf7X_S4TwOxN5M9hTNgwJ1NSJuZ_H-GjtC7JKaxNQD_XtMNZWTf80X8q-aika3YNdPgPNXK3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30576" target="_blank">📅 23:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30574">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EQVy3G2r_MyiLP6OXvih9UxrSqgMFGp1KihjazFdzajzXGXtJ5iOuQd0QLgUnw2cCg1O8WQspQvw2dItxbrXIjPDbEFibMLIQDLECjaJ8JvROOzg7AIJFzcnKcr4IUXo0P_JtMLgNCZF2z0EhNUs-PdyIu3YtP_hlcWtqVFyjjZIAylHoXEzqF6CTVWIukDYkHtIWGvY4rPrKbtcY2fyIvDaLnBHzXiB0UpuN-NUlyqTnOWnY1bV0Iyj-qngN4oizXxf2QQQ_iqGmpGH-qbuIXIUhFSkKD2ndNvA1ezP3SDu6kYayt4C7ebTECWuqECA1dpEiVHJd16JHasxFLdq8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S_n6PeW0y9k0wuFhaRvcZZBvLLugLCWIK4GSf1QqCnNY3xgQ9C34shvrMEZ25gV8vTcMl0SOfO0_6MXY8nj39_8_qxKq5bGU_kRgfOGhj0BQqsS4eFxicJndZOHLvyGNCh47p4OzEbpZKafNT4kFXdIW6fox-z19hVQPHtQ-kA0yK3W1kIPkbJjZPz-cJwl1DtySvuQLrVpqlH9Kb3j8iC16wiwniS3YlkOrqdQnBOsycGi7rMaYlqnNV2-8RifmEIAh54AKgoXMdPh4aQPOByf84iNvrxmkJEW9e_tkg2GYLiw1B3WqRYbAjUHsmL-gV0yYvC7_8sPAhf7F26FK2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30574" target="_blank">📅 22:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30573">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWZ2n4mYif_NBC9CEMv08ZgU7-jmstVvnlg3ZG5aXL3L38M33dXt4GD5bgm2fZW9MNZbaTMqSalWg__MVmvTmlo8ZWKzxZQD2dd-lHWy0pOsAWo9ojyNwiuxVsgYRwtjRyugAAoAoGHxLAdnz_YoHMZSJPkLcqpGhwtiMxe2R69f_ZG6i9MOUQ__VisfTPubdBp5iWTWyQdPnv7cCZs01mV0OAQZp-8rc-vX2oOoliKF7hVHBpCxa87NVHycjk_ELKSUi0JyqEFtO0VJjTFjMgZD3Uh3PtIrW7n2lb9A7Cgipsexsgs054VfTR4pd4_4KjDnSdCqvWUQQ1jG9lci3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلش‌ بک به زمانی‌ که مثلث‌ BBC امان به تیمی نمیداد. چقدر زود گذشت دوران لذت بخش فوتبال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30573" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30572">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=JN_55JIypC6eLmLr24yZwf51Fu8ea_fGpBLL2F-FS0rQG3rcP3wBsOg7VwVEeVu17WOutV8-swUiZPqq7VESavlbMG75MVXgqZbcPy6xWqOx3DVFB_B4mIcydYcrF1pY5yoyiiIvGzSk9CiVQlw8FdYN9LguevWl8MtgGt66vHOjiRBPiS0KG7L8yFqxQGPAuGOsLPLM1WMxebSO2K7OZaTEgHTXa_ZaUVSRKNHYooAkt-mBxr0VPEm3MRFt6oRd9TXoBSJ_tRgC1CVj0PI4GwbmQDCUFTbkDw840jNLPHXd-Z0zxNjGDyj3iLMnsmEam0OlgdCbnoR_QgWby_1HCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=JN_55JIypC6eLmLr24yZwf51Fu8ea_fGpBLL2F-FS0rQG3rcP3wBsOg7VwVEeVu17WOutV8-swUiZPqq7VESavlbMG75MVXgqZbcPy6xWqOx3DVFB_B4mIcydYcrF1pY5yoyiiIvGzSk9CiVQlw8FdYN9LguevWl8MtgGt66vHOjiRBPiS0KG7L8yFqxQGPAuGOsLPLM1WMxebSO2K7OZaTEgHTXa_ZaUVSRKNHYooAkt-mBxr0VPEm3MRFt6oRd9TXoBSJ_tRgC1CVj0PI4GwbmQDCUFTbkDw840jNLPHXd-Z0zxNjGDyj3iLMnsmEam0OlgdCbnoR_QgWby_1HCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این‌صحبت‌های جواد خیابانی درباره خواهر ارلینگ هالند در جام جهانی در برنامه زنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30572" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30571">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCBn8EDBAz5K3q6D5xIMII2pkceY0YJizztl-8VlX0MH40StnOPXLetbMqwsko3wfNSr7Hm8wQgFSDKugyNPULGAkbFaSMZvMFh7kPbB9K09FtbPpQT0x9YOyogyWBSOKT1f6p_G18RKyKeAYnA8vOJBi6BQ0YzA5tPhI8JgaNtBAUOCi7BgWfK1LovlPRT-ngW6v-oaNPSvB2OHBhkRXDsYjzgvowoVDR2BPJfiwXDlLOYXO88ofLk324W8Uw1Zz5EyOJMcEL2AGGRmstH4NG8t3YIxsmFrX3IXLuZ8u-q7-hiuWhNC_vqYHLA99CH6pTZzi-IbRRsJjTFiaKDXFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
CHELSEA. MORE THAN A CLUB.
🏘
اینجا جاییه که عاشقای چلسی مثل خونه توش زندگی میکنن.
💭
آخرین اخبار، قبل از همه
🔼
نقل‌وانتقالات و حواشی داغ
🥅
پوشش کامل بازی‌ها
📊
آمار و تحلیل‌های جذاب
از استفوردبریج تا قلب تو؛
🤔
Welcome to the Blue Side.
❤️
👇
@CFC365
💙
همیشه یادت باشه آبی برای ما فقط یک رنگ نیست، یک هویته.</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/30571" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30570">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AadPFfAZWg7FtiRdpoSeiJwiK61_19PZkCQtKKbwIAuTSV7zWxhdugLDo1wXA67E3wFPOpzWJNmZvOHvJBlWoH1Y58m2Hrtz-TWU4uCeWnAA66dilEWyY3bAMmLkue-I7zAW_nn81zxF5w40QFpjVfonUI2pbHwBGTBQvPPm6nHbGZ7vrR-8zjr_WCw1IeZIqij57Ax1cSBqwamK2OK9EaoilFzVGg2Dx_7_J-KnDp3Tt1AU7XCgHEF1bgQvh8UwxCCPHatRsEWnvqgIWtFcYRy2Ev2CHKfLiP7LUe19wSsZDm2wkGruGJig-7CCncQ-xWPJ-LMuq3zhYBMtWa690w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30570" target="_blank">📅 21:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30569">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXCqV9muNuPHUZcO7tONuuFeLY_Jz9zT7ohXG28oPq-Hg4aZz-as_NExKUtX5d8XygdSFsITZyPY-j4oufSswH7kM-3w1xH2lswPZfnLuiYGg9D3ViFmMS50kmOdKNSub-9gM6PlFTs2ehs_atBFokah4cgY_mDQZ9WBkVgBdcWgdX4K2QbnAuwzYzbqe_XAtUtTLnS4Tj7n7zSrvA-ZcCMgblKw6nI6QId6afLp136IwTW5xk3l2Si4JayQttejeDzb9tmc7A4QC-CuhyFx3wKf4yC5fnthwofNBjP8LxynlRBKTK1Ai_rHM2doOhG7Sc2arI0X17RbfUnVnTJYjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان: بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/30569" target="_blank">📅 21:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30568">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrNI_VSqjKJ1_XoJjGZgEVOWtDWPqha_cxc2IPRh2QsYHlsXu7tPs6ynGUNc-M6vMD6hUvpv2pxjfPDKHKqcrWISX52XAJEzk65W4rPcLJ14vsKy7fw41zBXYCyrGdINL_5LtTJhvJzawISvpVCBpdoIaILM9IO2JMeVdNt4IBLK-NoV8FNYAMiGutwaqJ9SitgV_zo0UkmLjwqxxYdJmL6dYItgoESIM-JZ4JPvyAs6Gr-5KUkqZMmEZgEnlLCWAw0YBBrNhtXN126KsrsqForZCEbZ2qJvdNe0-Zhe5Pwi_tYk_8hWoVPyo4U5VHxrrL7sauw3uuJDUp2s6OtieA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ژائو فلیکس ستاره پرتغالی النصر عربستان: موقعی‌که کریس‌رونالدو به گل شماره 999 برسه همه جای‌زمین‌دنبالش‌میگردم تا پاس‌گل شماره 1000 اونو خودم بدم و اسممو تو تاریخ جاودانه کنم. با توجه به جدایی رونالدو در نیم فصل از النصر باید تو تیم ملی پرتغال این پاس گل…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30568" target="_blank">📅 21:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30566">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fr7CmFG56gr9orHJZP5rRM8cCEacPyWzEgz8u-TrU9yZR-RGHKVOAr8J8TISoEV9v_Ic7FI-W2lBnY47QFf3148cJPj8-OND_-rJhQ8MgkvyzO_v5L4SGmhm0tVeGlIERIKOrlIjFo0BuYnVnMPP8uBz_Cm9AoQdgcikw_5-x8rn7OQShP6gqqqSUzh7j-ueSINhf7Px2WUfix87u5BP6EvBbuK2UXgTaGdeufqE1C7igJSat2lOGyu_Fw0La805ILEjJozfqdqq3xJ3wnoEzTMMZYvGFOTpceMwap_KD8Ou4jVMp-Mb2wr4z757hhFDx5rwSt-NECU0DeGmuFJnWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wv---0p6RMmX9B6emrRZ1P57NAIyfRoF2SDebFH7z-8GojRTMGnKDA2EKuaq1Pn4tKxoQMUiP3-8AdEnufXMc_NCoUuBOpXzFtiHEeLBDvktxMQNf1ZqHMoDj4AyKWgN9C0lorDq-vMaWL2PYiwtSXuyI3mKh0AeNFCnOEIKFGsMUGGc4Oo7tZW5VaPGgbCFdMpzydfK-ZeGN82KcsLOHIKUgMus60V0o27X4Bwiwkzrxed5jiSyO4z84l1uCZYasAT6ufsIOl23s7O44LJryP_LMd_MdunvGEM8la1XOl5OjSnKNJ3QLMLJnOGa5uOAaxlMnuU5qah1RqU2A3Vy3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30566" target="_blank">📅 20:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30565">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l173uXO6ec-7eT8n-ogxAaVAv5oJES-PU5mvBEiBWPwxDkzZ76BdueK5iNFypSTN-AAeSq8Jg_f4n6OrXhSMjCtZJfOuniCkEekOBN9qmmUWw0D61KHAi4NO0ybVc90kDFIoK2eOJP5E1qv34KhZYAkcpLvcDJ6zTqgy6n2ahkbctpCL_zpINslUyqYFj_Q9S4jQw1TKuX-rR6UjQ01kFIklQ5mPNVcHnrXU8W4mWglH2-u_HpkwUgOfn5hVfMCqEYno4YvBje8ERm3osoxBsxHxK4W9Hf0bsfzXaVDIL8vWUW-Upu5BqVyUvUAKOnVuCHbZtxCMGGaPbb_IU1U0Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/30565" target="_blank">📅 20:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30564">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nH0O7z8KqSVw_pVtnZ1LZZ0A0o4MwrBYr84cnUJmbw80T5B-Ypq7kim50T_DIlBWk7K9o1JaqsHAC9dnJQ81-WzTgv69Y2_A_vnvzUCzrmS2cvesLsrY2CvVj-g5bvp3iTjH3xC8_wqSa_fY6Yyn0lYGT3QSicy19xMpxUVCU1fk2F5Gk6-7CEMARQi3ciB0SffJGFw9rUbNwCYhTyvn40jQJycI4wuW0RbJk5m0RmcjSSMfKEiO2Et3WKLBDr6mA8Q1FsVwAuGV8emSe3suUSZ1BCFoZd1ypjVeGJ6M4ZrUOkRsqZgsErQut7wwV0tV0p1IHGiq6GMkcfWnkLnzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30564" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30563">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Grr1LyGd60LzCuSLBl5-LpDJ8p2pnyepEMb6lGV_nFmnWXdK5MfcAZmMCYNZzmZQj0g_UD_YLWwbAE4omPdWRCUJrYOgVmqq07QkOnLB0at0AdcmyIO2ykcSKoLAhMAN7QZosxUFkivXDPLMrvM88fNn9aADRjhdz8-43r7Xjoa0-sYWTpKGEFAAl9lMIreq9-jSQJJApSpUxBQy2KGDOcrnD61tIE9vzD3DUenepHEInZTCYADgnyOkQGeq1waC4ow197srY188HU6XVyyn5NAlOWLqJNyGGtu2ioybOJ8eNXo5eNLja7JeatDWeJqfnIgvR4prbDu1Dl2seQm1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛ ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30563" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30562">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHO8HGMcX_bpHv4JmzX1ar7WfbGY9QWeATIqTNElAIxzUec0VX6IbJMPWnmnEZX6z0nChiNJvbcU_jATYFBL43Z_KtkjNESQgS0-nctUd4WriQH382e482coGDbh1KW6Gz-GE4l30i_DAnx6_g69o9cgpJseEVstAWso1lK0yO5ebjyqt1WVUJ8oWwk98b_u1O1nheqYa9dV6DL49zgFMb7XtC60ceosNJOaMRT5FIlaIiXtk4aOkozMLQB1foHKukHIM2gaP-1rjKV7ZPDKA3EaRZzZ3a8GRG1RIG_KoGCjqnY6C4qr4HR3xoxhzlh9VhYm-4ZgUB1PyDeU6qfZpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/30562" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30561">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e9tALm1_G1lYnDO1lVpSW0rbHebMISmiHLkdzz8RDxMOlZUevD87AobeLywVTI_gS3zWglZd3wUehFbRJceaaybs9MJpmKnFUj4jdNEOFNucweotZkGf6_VFe5XpaOJ4af3uviMUs_c6HKyg3Ys3dVD9RkcMaEkW6o6mQSzYqBr0o0H-nX70G5q5PWNk6WxzAgkyNYv26DtiduILY6b3Nn_S0X2t2DNXHXn7y2a1sBtQcI2NBnUMXE8LI4KoXQrMeaxEaPMYBH-1SZ4YhZ55YBvxub__nZBOw6Z8BxwJ9JPIQXWyMfl3d1VbrThITg84bqD-c8rE6bact_9Ur54Csg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
فرم Vip امشب با
ضریب 2.
0 بصورت رایگان قرار گرفت, برای مشاهده بقیه فرم ها وارد لینک زیر بشو
👇
https://t.me/+laf8I3RIuq42MDk8
💵
فوتبال های اروپا شروع شدن و هروز فرم های ضریب بالا وین میکنیم
میگی نه؟ فقط یه شب
بیا آمار چک کن
🫡
🔻
اگه میخوای فقط تماشاچی نباشی و با گوشی تو دستت سود کنی این چنلو گم نکن
⬇️
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/30561" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30560">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GExVw5p8qmQLDa71DJOUlTXZHJyGrK2stCAMHruDXtNlpYh3nFG6wuL2A4n3qU049l25CoQ9m0NdYxy2GYs9Yk-IIc-56gf2CRDZ_metMVq0HAUUG9rZKWqee-C6JWR7a6uMDWxcaUTOYmqASZTiD40s5e706fc2QUuL2puH6ibb18ElAx19tCyshwqNp03XWv0PwQmGygx1pC2PaNJ22zgumtv0okgLIE8YtxI5WebykYFRI0DynprvDcn_8EJdaUknxSGN6lFKHD9qkw4DG00qeGkSlvQsHXlwzOh01JMjpRNS27aQfsoT0UwRTX0FilECQljKDfgQRCtyf6vw7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/30560" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30559">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d469366f.mp4?token=Sl724TrSVwnR3tRmnWgAdrdEIg_XPLGWq1PiQUCjKx8BYV3lkhlTSCpLTc_f6TqpY1Qh4lH63tjQWhLq9aeMKrADytlCYLJqAVkw8Quco2GhmmhiOLnYFbFEnyyGSsAGo-j8853vDLGMmE72BsnhIE5WNDinNb_Xk3HPFIvBdyasAG283RgS8M_ebSIVCziKvrGDgCqZsD2TsRKcTe_tJMTgH5oOJeJNRW5BIXUmPXahHfGu_aFJNwc0Apos0Se4DbqP5EBE-HzvSnYt7axBecYtCwOIquTnjglysXLBqm99UVqOLHF0-Q5Umw4T36KsHo8MWQ1H6l13MwpG87AaLX2sGRoitRmCUyYnU6lzpcMM34lDiowVWNcaMdn7_BEEck7Gg8v6fBNyT20VVHlPxdK-BA6FrhaUQIb03dnMT0r5vlLDynjXpG2iGky8P85P9x7CA6YC2MUkH3UogZT1wHUc5BxQ8L2f41utWdRS_qiLAjIEUfIEtR-2pqf-diWVtoJGuenS199qJRIeo_aYIYLXx2fBxfENiW6k4S61Qm_dg0L1VtV5DxQdJlY-h7HZkVCq892OprrngxvwJL0adStAF0uTr51gg2r8tPXxppjj7uH_20AkM9D6met0Oj11IA4ZAae0pSZToqtBIi4Dhn3KFe8qUG-HD68hZcCjLFo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d469366f.mp4?token=Sl724TrSVwnR3tRmnWgAdrdEIg_XPLGWq1PiQUCjKx8BYV3lkhlTSCpLTc_f6TqpY1Qh4lH63tjQWhLq9aeMKrADytlCYLJqAVkw8Quco2GhmmhiOLnYFbFEnyyGSsAGo-j8853vDLGMmE72BsnhIE5WNDinNb_Xk3HPFIvBdyasAG283RgS8M_ebSIVCziKvrGDgCqZsD2TsRKcTe_tJMTgH5oOJeJNRW5BIXUmPXahHfGu_aFJNwc0Apos0Se4DbqP5EBE-HzvSnYt7axBecYtCwOIquTnjglysXLBqm99UVqOLHF0-Q5Umw4T36KsHo8MWQ1H6l13MwpG87AaLX2sGRoitRmCUyYnU6lzpcMM34lDiowVWNcaMdn7_BEEck7Gg8v6fBNyT20VVHlPxdK-BA6FrhaUQIb03dnMT0r5vlLDynjXpG2iGky8P85P9x7CA6YC2MUkH3UogZT1wHUc5BxQ8L2f41utWdRS_qiLAjIEUfIEtR-2pqf-diWVtoJGuenS199qJRIeo_aYIYLXx2fBxfENiW6k4S61Qm_dg0L1VtV5DxQdJlY-h7HZkVCq892OprrngxvwJL0adStAF0uTr51gg2r8tPXxppjj7uH_20AkM9D6met0Oj11IA4ZAae0pSZToqtBIi4Dhn3KFe8qUG-HD68hZcCjLFo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیویی‌از پاس‌های‌تماشایی و خلاقانه تونی کروس دردوران حضور در رئال؛ زیدان در مصاحبه‌ای گفته‌بود کروس بهترین‌هافبکی بود که زیر نظرش کار کرده و به داشتن همچین شاگردی افتخار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30559" target="_blank">📅 19:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30558">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pby7BHO2mEhyPLB4tZOlI-lox2mFyuv5xaGJGDXlCM1miHWnuWVed5P05qGFUa1-N8U6lrNasnVS1fohT1YkVJhoXjN7E47ltkOUEbGYR6NH3j49tQSaPVxCjc_jw74bH_xx3gP96zROOZfsikDtNb2c1aSxxVfqyd-vsDs7mc-hAQI_8Q9rFMx5BZWmh6J4QnhAC2wkMZAjBFW06Y2lHizWt_0EhluVdkdBNwrvX9cQSkSUYa4KV7HXe9yBFmF6BB69b4n26ydvCOpK14HVBHq88nUPJM_lWOW-rPPrOCNYcHxmknUmA-Bx1j6aR1m2acVpEjKKYLggkVoYfdJt4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ سید حسین حسینی اولین بازیکن مطرح تاریخ لیگ برتره که برای خودش فن پیج زده و سیو هاش رو باتعریف‌وتمجید ازخودش تواون قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30558" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30557">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efPE_IGIu8WemuLYMP4aMJqF8_9Lnteb7ye_p-XtxOpWVWsVdlY0amYN5Cym-HaUiglSsad6dkr7nlZt-kmYJVth0jj523TaV9WrprmKQK_5O7Ipur3DM6h3CTrFf03bCzkEv_TpXOF89XfIoMS3HdrTm5ls-xT1pT5NhmFpRhV-GT4PiIIlJhSmhmJhPMdhhtng-LFlBjv_9tMW1YrzSq4m6zWTAibJCzkzWX-ktEx2oaCTAWWWB3feVXMnsE1ZTcDDHA3A2Hr_3ajFJiWl0ptecDVTxnq_xqVHTtJ876sBTEIvkb3CzqRlwjv0lFJQhkoRYYet6P2OzuWZcJaJzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30557" target="_blank">📅 18:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30556">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=Z7_g_0UekANsYTNsLMCzGJ1IEGybLwZ3hvY8IG2pLPtHs6o4i2v390rUXp5xZU2ApTes6m_wfFW0OzKJpAyYjJgZlxFoMf6s3jWcK20Lo9j9Flzhrnnw275kpPjm-2drtHqsCQnll86jm0fCVe-s0WTY1vmqoUtmZPrRy4-QfI18Of_pBsQEJIntVVEKISN4ZGJ4W69nEJGPY3XIzf8h0csyDZ70tg8Cmg2RbRWz0dgjyGPCmVFpuIqgmrOEx872QBBtqYiprZIV-N4y3Am70MhfsbEWsqv6g9PsbNUSgMK9zCeDqnP8wtM8M4GJVfSMJuR-2_8OZ7At6UvLfZaQDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=Z7_g_0UekANsYTNsLMCzGJ1IEGybLwZ3hvY8IG2pLPtHs6o4i2v390rUXp5xZU2ApTes6m_wfFW0OzKJpAyYjJgZlxFoMf6s3jWcK20Lo9j9Flzhrnnw275kpPjm-2drtHqsCQnll86jm0fCVe-s0WTY1vmqoUtmZPrRy4-QfI18Of_pBsQEJIntVVEKISN4ZGJ4W69nEJGPY3XIzf8h0csyDZ70tg8Cmg2RbRWz0dgjyGPCmVFpuIqgmrOEx872QBBtqYiprZIV-N4y3Am70MhfsbEWsqv6g9PsbNUSgMK9zCeDqnP8wtM8M4GJVfSMJuR-2_8OZ7At6UvLfZaQDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30556" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30555">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqfj45DqiyUrJvaCIKhT-oyACrNilz9-sf2rhWBHDpJgYOK9JvKWhda_Xjodtu9qR9KzFD1rVpHAswuv8vHW7l_qBQZIEUCGIdieQflm7hAoTfKeQRdv9SbKxzfNopz8JY-NmoTv_E7ki4gxFx14QneON9MEV4hLzI9kWqWix4GX2dpXlRirWYb9CvhYzfYe_1oOq5XrxxR1mxpAp7XoiNulfrE4SiiSkDDwpGDROkynL1hwFpm7nc-mpievW2fTh3hoWlA4qyiKc4yngDXXJza8wd5awpcsyUat4oeH8yg3tV4SRnmxbAsO9bJHe2-Hj8CPBVugykO_i_owFNrG6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30555" target="_blank">📅 17:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30554">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IaXQOKikbESv9sOmt3wJBXKuj8AEnUozZqKcFV-tFipYmqiDTOwQaJxTXZbs9ZJsKXpiGyD9rXleoYG-9xq7cjOQ2taaHutnjbS8sxKCRFy7MaHZ2EYeN4GaHBeLOQGS6csdoMfirZh0sRF7Z5Wr6P42iA-nxuXnkXlPWJUsiLdj6D8wbxlMRNBX--D5Xu1SyEbbrE968BIZGCcS9Apro9Hf_lQWiXBXp_YW1UdZg4APLOEkcTjgD2X5FSgiawat65T5BhDke-E1bQIeiCQrfPwsbziFpf4vqvEBa3Pin7MTCC2z_NpsofHH5_z7MKdi0ieuNQWy6tuh4GRUkJo1HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حالا که بحث تخلف من سیتی داغه یادی کنیم از 3 فصل شاهکار فوق العاده لیورپولِ یورگن کلوپ که زیرسایه قهرمانی های منچسترسیتی پپ دیده نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30554" target="_blank">📅 17:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30553">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdERyw_10eP8YU0CPUXJV1F7KSSNxWl6j8EQjakBMwD7ykd6Jia2WcFVUhW31EmkL1jage5QEry5G-ZaX8BsC1l7PvHCidztrO-gWQM1Hl46yoztikQIl03iSds8iaD84ac1LeNWoWP62Wwcfv1Ss_9nb7vUxSqW4BJpXkrjOFRpxeE_ui619ps5M6AGxRbsO143w-9XG8WwBSO_KeknrITW7xssSP2UbDY9Eb4nxbZ7pyiTbKPNXl3SmUn4soOioRsWFDC4tzzLa0wurdy-okSGVJ4mSddktffutp7h59Q7_Bz5Qbr-riNv9L_bQ82g0LRKgwm5J1faeWCfk39dtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
سال2014
: کروس به‌رئال‌پیوست‌. 8 هزار هوادار رئال مادرید در سانتیاگو برنابئو از او استقبال کردند.
🗓
سال2024
: کروس با پیراهن‌رئال از دنیای فوتبال خداحافظی کرد. 80 هزار هوادار او رو بدرقه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30553" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30552">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KmYuj1FZt9cq6b2GwoZCEApMEbLUOQvNJCT5RFOJxnznc1CKCfZWQJeLbuE_GUdVT48lvzpfFXzYBwbkV5YQA3eblL2LRZOJ6M2VftVUGiAr5jPux7xu55quHYg71JySTRDCVw0o5_B0QoEClVFOWYJMtfwPFelFaeLhoxw7-9XCF28wgoNiRBUTRqHOpBbTIeV_TMq-yEq2HkvzyghaZOHp2MMdiv0SfAma9J-zNss-3fZkKmYkMkLfl2GZOioqDYmXiUM64Ekvi0ZV-gaG5wgiaV2Sm0ZpMEoPi72yzNDrU7XS78u05yIsZFomQU7dT1MXECKJf3G1eX-ZjfY88Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/30552" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30551">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALfYIMnW5jjdaXAESJ0tzJRzU2lhMmdlG7ybs-_46wVTtEtQ6jR-sR47stxOh_TRiUwGoyyFN1SgAJx6fiYYADLcbK5gzAsXVxm0vcQQGgawaQPWAOGhW1eXazLFhkjO_XfwVT3SpSzKwV0wIv61fET2_UBX0PfOKefw3TP81vrHvREVePg2vr6dHKZAzYNM4wbmjFDUMdycJ8fZjop3-6N5v-M7CnOVPIDunAvHsUV0G28afHgKezB_uQt0nBeSiX02gbzdbXUO7OIXwNEvIyNP9sDa54lAccUtPiFlFbCMyduxk7iuLyyErLE8kBTbyj-ypZegexpQxlAMvmUN7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جما اتکینسون، دوست‌دختر سابق کریس رونالدو گفت که بعداز جدایی‌ بهش‌پیشنهاد پول داده بودن تا علیه او صحبت‌کنه: وقتی‌از هم جداشدیم به من پول زیادی پیشنهاد شد تاپشت‌سرش بدبگم؛ ولی من قبول نکردم، چون واقعاً هیچ چیز بدی برای گفتن درباره‌ش نداشتم پس دلیلی هم نبود که ازش بد بگم. هنوز هم کریستیانو رونالدو رو از صمیم قلبم دوست دارم.
​
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30551" target="_blank">📅 16:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30550">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">‼️
#تکمیلی؛ مستر المپیای امسال قهرمان تازه‌ای به خودش دید. نیک‌واکرآمریکایی قهرمان مستر المپیای 2026شد. سمسون‌داودا، درک‌لانسفورد و اندرو جکد هم رتبه‌های 2 تا 4 این مسابقات رو بدست آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30550" target="_blank">📅 16:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30549">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0sWrkzJ-ttYA0E8ggUhsdMOTMs5kurYjdThI6x2507m1NMb29wijzOMrHtLH0VYy4GCktidcnrZlreh1OirpZp2fowXtlQbDyJ6pvwR33oA3lOQSOpmV7VKx5dU7uXROKi1I1unHMft1_AaZuZ5GK6eQX9o7ArU-cYgB4AGOUYApB-Ql5RY_aGqbOzWVXaGJExgJcAgTg-ul4C2kW3IfWgb2YBg0JYNos8j45GbC1h4WbEZasZIlsDzje6CspierpiSM5dZ_NZ854O_ion_GMjVNka7Rsf_2748fJMff3Ro0YrFFqgBg4790-V4_BTL0sstx7vfLlTe7A7MGr0fHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30549" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30548">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=dbPy1msaYUZOQrxK4BxQFeE9RQx2aDmlaREhMAv_QKFI6gLhhbl2Y6uA7Wm9hxjUztnDuZAOrd6iQ9YYI599XEWOyvHxKFClu0P9dSQC-FCQShQt0qM_rwKGdvBfaWlXKl74tudzIn2YB-wr4bxkRmHa2uaXEJ073MzoaR6NpzG3I4Z1EtrwmnhWyMhEoGBWmsMoWt0OkZckcoNijlPClKf8LKT0nwK3-lktI1aYzb3uUn5VBdzzCDEUOh1gyLA7OV7F5bhfFREiCGSLKvccIPEWbjkZyT8-c1jeaNAAxDUqB8usadDTHStYsMxfv6wKT6FnalHdXueOfPY-zPAs4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=dbPy1msaYUZOQrxK4BxQFeE9RQx2aDmlaREhMAv_QKFI6gLhhbl2Y6uA7Wm9hxjUztnDuZAOrd6iQ9YYI599XEWOyvHxKFClu0P9dSQC-FCQShQt0qM_rwKGdvBfaWlXKl74tudzIn2YB-wr4bxkRmHa2uaXEJ073MzoaR6NpzG3I4Z1EtrwmnhWyMhEoGBWmsMoWt0OkZckcoNijlPClKf8LKT0nwK3-lktI1aYzb3uUn5VBdzzCDEUOh1gyLA7OV7F5bhfFREiCGSLKvccIPEWbjkZyT8-c1jeaNAAxDUqB8usadDTHStYsMxfv6wKT6FnalHdXueOfPY-zPAs4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30548" target="_blank">📅 15:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30547">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3jLm9R1NUMsmHEkgCEpbqJJZDCuuFXa4HBFEj_ukCdUn62H4q4y9BCFwOcPLEjcc-w3V1ezBGvaeFMu_niduNKMM9wwQOkfZ8TW2ooDgTK9wjgoW_C66-1ZB0l6I0kk4prfefbmidIQrSb58dhOE3UDJivbXCxtk88cMTNl6P3LtO9m8OCPnQ2T2W8vi15Y7MnsBKNRprs7d18snwKUxBvmIZFdf5RIr3rh-Es_tnXiKq5_HEfZhcT_kPtrT3Ath6N78I5N568qRLJjeAjDdZF8a3x-GJV98j3RVY740TZuipQ6Bfi0wi1k2ryAxU9WNY-vvIs5ILvwjdenIqPntA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده ژائو فلیکس ستاره پرتغالی النصر دراین‌فصل: 17 بازی، 15 گل زده، 4 پاس‌گل، 9بازی دریافت‌جایزه بهترین بازیکن زمین، نمره 9.1  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/30547" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30545">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MoEEVczPwIpAEc6Q9q2-ZCcNJv3rt9iyp-Isfy4yj-y028hChfKQ-obPCgvXIhF2ExhvUpUB5Dz5B-HMdiJYZ3vHPz8uMkj9P4aTT1oUpqj89y9s9NcqRCGCa1KHl28FfAQ1yBCwCIMCjkWgett6RFK7d0nS9Bm10SY99cMXAG4vCZ9yMRtG8FEuCSzUVCjTL4ZPPwJxALEPY6MfnYdpDQqz2wuRQtzl-Qyd14YG9iCYbDf26smHtUdirIvuBVBITWmLFtveSLw8yAm6gbCp43t7kRVA3xBjv9suyGPjqiAO-hXjbwpKheRKRUYkwXzM_4C_WHQJYXFPgWX_wGs4SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CDh-GdA3b0285zcBnPTXYgVHpRzLJfLGlIfpTnHM_m2FUcFsSyk89H_Po4Lr_7Ah31fdzgHe48_seSmi0VNnuSmux3xJNQ4WzWN_mh8U1yVtS7vzwNdgEBcDnR6-K9slC03JsfRg1Vhk4Xz9wLwri9VsvblSYoHnlYk5yCJRJQt3sPptlIV8xUKuLl_XSp9hio2tjZU342GwRR2HuJwQkH7enft1KFTe7i4M4IkEsZpiYhlhnvC589sR9U0q7fwmdzEDBzJvRXjcRlZIZ7PpgezEIQcNs0gL7MReZWzBPYlMUg5d_ZGNxcC3dycIjJafkRGIOOP0h-fINmLrouJxCA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/30545" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30544">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STbSYb4w357bQSiAVqa1t7UTvD1-wVayk5AhPJDhpw8y3MuXPXR47uh657VjRqkYlKmCm9NDKiSoo357q-cdI3y65T8l7BK9V25gyztG47r9E56YtRVXj0jLLJx3I4IHexYjiyWioOIOHD7nwZBFvwC8pQO76-4c50wUpQ16rI2E5KL5HtegbeYVwswOD3dX1e64x7lHTgHXbCILaVmgq-HtRv2Q70L3CMd-RxS0CrwbyQrkdXRdOqWystdCXCy6tdxV58gy-wWHztqC2J-_OsRc2o5bt7n0yIaoLcopM_g9XEL3MJ-q83-aIR9QLComSj3VvY2c2fLMPi1DIR0eOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30544" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30543">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0l71sNouxekK6NdTIGmegj387epTso57JsG4CQLpI2AJk9F-ihNxbZxHa235sAXmhkzBzp3vlCnKHEolsiii3GrlQYrRS3vHqzcLVxsZIC0bzooTWMqEX2DBjMVz6Sv96DNPyyc27R75kMfwpOS_q4mxlEPZ4MtbwvQeEu2mssSXeKObsnsoOZjFc77K-4zAGoplmwX3zLhjpU_v-EcIhn9OHQjTS-LzYF3wnMufa-ixlOv0dxr-JRkqNPNZnIKbHqdikjeKlZe5CiHKEJtCj_7YpwwzoiB_5CJ9oX5jjzJcDUul4aJMEwC_zPGBDwgQ2cStZlv9agT68UN04YGVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛ بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30543" target="_blank">📅 13:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30542">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5nDGcDuB0NIS0YASmtptYSuPiM-PDZNlNshSRx9AVIqmY9KWzubmPF_9KzDLU-ea_C16N-n1ZPKsO8Jkb7LUUV3KzyNPke2hZTpwy0gJkVr4uI1ZtFynMpH0-qEsUM1qeyO7TsGm0SBxlSn7aoVaW8e_pKLP8I2VMDUA5DGnb1Ti-iQdPCwWkp_NDi_ulu1YB4iz-0PiZKZrHBXzW_PZCXiFFTXaJGA6qre-n5X0kuHeuegxTLxQw9tPlmWTORziFB8dFx2QLs5yqKzwsCOFSuNRmUlRlAK1v-zNzes8svZGgOZBidLVLlZKy6LkUHtJBN_nA-VvGRWJt3wo0uLDnQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5nDGcDuB0NIS0YASmtptYSuPiM-PDZNlNshSRx9AVIqmY9KWzubmPF_9KzDLU-ea_C16N-n1ZPKsO8Jkb7LUUV3KzyNPke2hZTpwy0gJkVr4uI1ZtFynMpH0-qEsUM1qeyO7TsGm0SBxlSn7aoVaW8e_pKLP8I2VMDUA5DGnb1Ti-iQdPCwWkp_NDi_ulu1YB4iz-0PiZKZrHBXzW_PZCXiFFTXaJGA6qre-n5X0kuHeuegxTLxQw9tPlmWTORziFB8dFx2QLs5yqKzwsCOFSuNRmUlRlAK1v-zNzes8svZGgOZBidLVLlZKy6LkUHtJBN_nA-VvGRWJt3wo0uLDnQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ماجرای بسیار جالب و شنیدنی سرمربیگری دلافوئینته در تیم ملی اسپانیا؛ این ویدیو رو ببینید برگاتون میریزه که ایشون چطوری سرمربی اسپانیا شده و هم قهرمانی یورو رو گرفت هم جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30542" target="_blank">📅 13:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30541">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjYh-3r_CNriCCGQGukGSabQcOws83RwZS58prY4JwB5rNiEuY6PZsxceESLCbv838rM68Dwab21UxKij5KocdjbWdrVXF_K_7WagdRl7tqoFBOCTNI9ea2vh3_v4o9dp-S0KJHXwrPoDtLNhIi6E3dAi1ahWnrNSMoPekMSBWxQqkVMGdkt-gTFFK8mq6Iv4813uWpg_4Si3cjDgHuFlTzxsksu-BHD8ezKhPhvyYlS2fIZ5EzBphuwuSsqUJn_Jb0WzxztiD27LqjSubMUBk_NOAQlFBbUlySuXfbJo5UbTZmtgsrb7E8D0w-QqpjqE4asbLclSdkYeuWqP9yfMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30541" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30540">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVE8h9JVMsxZVy48HpXyojK8PezIIVcFmnFwJUkAo6aUPRM5pkEmYZpWbU5w4tkYgkUKXUBqtLcmfRyCgQ_fh6V_o07K_0gHU1H8Ik_LhQ3zHJ-GoethhhZvSHyikz-99woGIen9vTG2tkdEqlz4caZUTpoCFDgK2SMNNRvZQVVtEVyvHxXaobBxuLV6ohsuJ7qG4nVohzu0wkBbe80HBNm5-lS_iwVR41tINDQyvSj4xHYvL4rBKvWpUbwXWxujgwCh3FCt7dqDJL3LbhPZUAy3CaKzoPcMInpNA_cBUETZhN8HVTsh8y_FQL58C2SuBzmeQlxHJH25dwAUYaIssA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛علی‌رغم‌اینکه‌فدراسیون و سازمان لیگ گفته‌اند بخاطر فشردگی مسابقات لیگ، فیفادی و لیگ نخبگان آسیا احتمال برگزاری رقابت‌های جام حذفی بسیار کم هست اما باشگاه پرسپولیس اعلام کرده حتی حاضر است بدون ملی پوشان بازی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30540" target="_blank">📅 13:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30539">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=e479npClsYa_RHJKSxjmm0lT0My5gc3J8-s-vYZPmt226RtV81MGjktgTMBnX0maeG_tiQsZuecdFIrUi33bsjoq3zKGleDlrr_UC31JELd-PgenUDwGv6KOsSphlk1zRrhqd3jjmj0dfZWyiMt1UOCmYgmrnibrFGWPVyi8MVP7WnedE5S7LFM8U6uR79C7X9t_-5DYVK_BepozbF4wNcDCKs6bVgEov9ggTBKUP9VI_6SB6OTmx5FJ9cFhQfONHlMAjoEo-JULpk8p0DKTINo0UYPUx5I02kHVtNTN5qS5oNiSkSLaFdzrAuXQLXeSIBvXY2CYndSsnI6JtjEYFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=e479npClsYa_RHJKSxjmm0lT0My5gc3J8-s-vYZPmt226RtV81MGjktgTMBnX0maeG_tiQsZuecdFIrUi33bsjoq3zKGleDlrr_UC31JELd-PgenUDwGv6KOsSphlk1zRrhqd3jjmj0dfZWyiMt1UOCmYgmrnibrFGWPVyi8MVP7WnedE5S7LFM8U6uR79C7X9t_-5DYVK_BepozbF4wNcDCKs6bVgEov9ggTBKUP9VI_6SB6OTmx5FJ9cFhQfONHlMAjoEo-JULpk8p0DKTINo0UYPUx5I02kHVtNTN5qS5oNiSkSLaFdzrAuXQLXeSIBvXY2CYndSsnI6JtjEYFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای بین دومجری زن‌ومرد تلویزیون روی آنتن زنده: دفعه آخرت باشه که اینجوری صحبت میکنی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30539" target="_blank">📅 12:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30538">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHl2uactZU75Ax9-6dnWrrIrxJNt61WxdBuG2pBOH1WwArDM6CPX6XhguBCLgyIwxJo8Qk8kYtD45oQyyigmAzbpB6kZL_0zISLkdTlNjNStVimywTzd1tcwfam7KR6LgR0LBuUJYXWkSQYRoLrYAnnyoV16BOecH8HojMmC-EB_IpzLrbR6YgkJdRN_WTP9wyvVUMCjJHMn8cVOtQeTvpVS9oTfoIfcpu8GEAAo2GAvkZiTdpmP9_q5T3dCylf4vf52Sj6GDUg7ItSWLL97QOKpDn7x9OYAIiyaZqdyyF0t5fBu8dbC6Ooc2MIgpNYUKxRwKKOPEtH8cj7AFAMEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/30538" target="_blank">📅 12:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30537">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqP19GeXPRI3Fx4UEZ0s4ujx-idhRlUh8K4TmNIlwlqWsKtp9uJQBHDohXQAg6CH61BItn4KE-jDH2ZxX_9L3B0ShQB2rXL6I9m-OUbJ8NlPtZ0q0WVZXocNSADboG3l63RJWIJEU89NR_wOHXp955lCQXVCQLwI0hb2NKMn1aewHV_28ShebV2GSkJM7ZayaKz2tQ2cw4SisRYb_9ISbk-YlWKkoFiC5nBQMCvf8ZQ4AgnoByl-YmmcjS-Gk0Gh9mMrhKj4wqTQHOsh8vsuOU73XvDgearTFAY5LGxKbFzjjgJXZfMXhn3mPTv-qNlD6NXgUT2186yFy-LzC3Ilfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حاشیه دیدار دوستانه امروز؛ کنعانی زادگان و ابوالفضل جلالی دو بازیکن اصلی پرسپولیس دچار مصدومیت‌شدند و اززمین مسابقه تعویض شد. هنوز میزان مصدومیت و دوری این دو از میادین مشخص نیست. فردا بعد از MRI مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30537" target="_blank">📅 12:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30536">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30536" target="_blank">📅 12:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30535">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pXVh8qOAlEcx_3QMGWu6iyS9VrgFLNgQtn6V_Ixwb6ydYXnOq3IHnaU5N7rLSSb1FWGu9vSkFsoMugXsEZTRJDj2T5vCCnFYkN0wTd_Jz5pqRfU7V3E1knSWglFH5uBAhUpKRok9cr385eHR4Kt6Et93q6Cu0D_2KhUecFSBM7tcsXPs41Fa9J4tPyKSrQrMvddNjbmVpAaLHIswk9l8nxJNnV9sA9lkc9MafTj0Y3OuAj1RJXDC8pdIxJ0Fv4Otat09pqmMNkVLnTq9onAubcKgCJ7i5tG0u4-KZUENnhbs4wnqTve1n8rijKvqfofNbjMoxgBI_A3kILFUFNS3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
درصورتیکه سهراب بختیاری زاده تاییدیه رو به‌مدیریت باشگاه استقلال بدهد؛ سید مجید حسینی مدافع میانی 29 ساله تیم ملی با عقد قرار دادی سه ساله به جمع آبی پوشان پایتخت باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30535" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30534">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o792ysqYFoi7FNceHF7hAOb_LQ2zDJg-qNM5wDey0ZA0QM4Rg36stxv4IE-4Jrc5lm0urH8GZdJYydgPeei-3StnP0Dd1bHPvbhrKNwdL2DH9629FX65wRq6OQY2pMvqrl1_Sk8N8mHdlN0jcrVqallYGLv1nYvygEbbv0q5E4UYw-WsYv7hqrfcPiAnFPVgOXKZbSbgIcaeyL_gpyfOMXdtCo9TZKOjeTwd1MOG2itf4znwWVZpCmxFze3_yvRIoRPyXaUrVYfef8c029K285VF9F5TlqBbjmmfsf-IUd0AJIp4t0uKiAGqzF8LRheA2CeGmH5QmUXOVY0duq2s7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو بازیکن تیم فوتبال پلی استیشن ایران که مدال طلای بازی‌های آسیایی روکسب کردند به‌ عنوان سرباز قهرمان از رفتن به خدمت سربازی کامل معاف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30534" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30533">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Swi1IKx_MFilA4kq2tX4-bsAJsMgUHkLCL4oQmNTDB_AEj1MmbB4uYYIa8264cgnBsYJz376jva9qS089iBVjVWH-Mos6csyvJUtmeVM1fe7_KRbv_kBXVK-V2SFhG0wKZ4mm-9MNHelTRhakx5GRRCs8CBMbtkXHfROfAdPvaQG0Md7vRfkKBYnJOCgNPhCJqFsfqTkYTwNSEU8WCXQa_y4qVUH3uNQxPEr-cfmWM_e1c9eMfCdqFYdVzOXcaMLZwjSG3nFTTFT6Jepp1hMwOAUX8Wav_L5dGze2jIfCdUKPSr2ySJVxV9vZhiMr2OqhHlEmJ5huPjoefc4nHoQQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/30533" target="_blank">📅 10:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30532">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1OkkWLwtb9xQmMrgnluK9ciWg3GOJUkizbtXevrUQPgxlRtr3qelHiN7b7m9XQggBwOLk81o3xEW0Ee_maQ_4Kv63hjlpHH3nUv4-horayFYruqAQuAnLrRFWhxSnj7SbfXD5PtrHvg6HmXqP3kk2J5n5H9Svpxcpy3Sbwp5XM7YoVp-JxY0eN_0KsDwWQQbNFMU_Ndwn3ln1aGfX_VE6g1sO6dbP8TfeWpoSisbCPBzdktZY-Q_iISVES1V8lMqyFscxvdWbqIUylgxqYFJ_2R094eZbY6cFZSNXFkAn52xTrjAeRVyRw63QJoAxsmnIhI-Hd0UxIM2QDeeLeHUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی رسانه پرشیانا؛ اواخر هفته‌آینده احتمالا "چهار شنبه" باشگاه استقلال قرارداد یاسر آسانی رو سه ساله تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/30532" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30531">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m4rwyxa2UB566KOi9bUcM85L-SrvRKoOSoxlK8FodzSFmDaaJtrywKqlltgIB_JAbGfuYg5tbyVP2VJCLhdhMFvbDpYWR6-k6ZQzFDaIk7qQQq1EdIh3XyNaoBETuhbHVZrVQkUHDlEV1viVkdw-Fwf45UHvpiyh0VQ9c_QKurebeLpDy8KQIp0d3v1ec9lY8iuEjUw6KiqnJRoO1VdSKtgv_xlbhQgHhWMebk82l_njW4qW0aIGFA4F7SidAAqbWWGdGZgZKXmGzyv2JINnDkasOefMtNKN5EPT-Xn1WrsJwndbHrKEpUZJRH9PTwkd6Q_M2IN0hrIS1ZGK-QI9yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30531" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30528">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R7vl9nYKcDjxkpe-1sn9ZroXSfGoMSogVLRKhVwP9A7MVzW-0tQ3jW0vUyo0IhgDxhwrGzcw-zOAqjFeSAVCQA9Ex6DM0LEHShJymn26PvuluZY9clbtVI326eDS5P2yWRri6vfA8cME_TJMLLUo0bDzjlpz0zqfCk0bcSLL_emgrzuhG93zQKcmq-uJRc7-NzvgJDuU78PivJfBrZCsRJgQp0uyBjdcnjTfiog0ysTvB4ZA5YpVZYzlvefFFTqgdIfFwHcCgbPPxUCQasERIALc4MM1bqIwza28BA1SGGIq9898fNWCLEBOGdVU3TOPqRkuqGxF3p1farbHXydRaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان:
بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30528" target="_blank">📅 10:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30527">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEoeRKcheTvGUmxKcMwUPds86rpLNOa_qVh3W781AJdUxeyvMxSoQkacOSvukG0PQA-D75zdfYSLzCRCciXFcBBXDWxIeUTeI93aW_yS-IcO36uW72Q1fj8hN802rgwtf-9md5zLfGEe02qAsJvcdnIEX52dNjFaTrd6myuKkzeCqiItt8OfqqYLjhYb6eIs1zWh_-PrtxuMRc2WpBo_7pNCZVNTuOWECwOac0G3wK9iHLun9i6QHTR6q2eEIMjiQsWqc_ObY4aBEWEOEcaVQjIrDbyNejxlVYaSWaYdyJGped-WkLFwS1Ld0s6gs9nLzxzNEkdM-6FKHloYRrHr0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30527" target="_blank">📅 10:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30525">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gRIBpdP0OSEx2UmWvk6wQTksha2k-5A_5q5eWHnlxnAsC6sV43hFsInTjO6hcy_VA54cDoSAj13YV5HlbET1xu5MSslF_D5rd3jjYFUavYeSY8kUQbT2AQo6u99KSdjoZ9Dv5v6wwDOZG2Brv5cVP2z1giycXjLvAHXhNroyP-ftXLV5akvtEoZEnOyQcFaUGROzK4mcKvEKR1GaefUdZH4uxETBPY-kiGZNsOvBMv5hGOCKtGC0zwAAX3q0_NhE02jNMhnxKh6xSTB3iBREPTLgRkI8qkfU9YpEVXjsqVqVrnISXpT8oivGgyLSnPMR87QgOATjAvv6HOv3DPAZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب اسپانیا
🆚
انگلیس و کرواسی
🆚
چک درهفته‌اول لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/30525" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30524">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnfPfKL6ws1ZkiM_3OX7amSGUbcvLaP-paTfQv9o81UtsGTSojky2aVGXSEF0GpR7J66YV_HdfVlicdix7EwJDknitJQTWIOLriqKLT7ttvmK6Oko2UGkJuJDZ5i0SOnfaOqI4UwWNZZCKDr94I51LkvGu4qnkxdP8BrqkS09P-Q3OCQ9sWeBRNlEMUiHwAufYr61muh42g7DCyuaEvlxgRkVZdjxwxNFh91ZaUyVAUtqr3EWuicaM7qaBOmueM3QjbGC5tQ4pjR0Bn5EB8xA3WZPt0i_ugNRqLoK5_lpUiAjEvgLvGrZ1TaIe-WJQU7XhnM-22eash0hN-Q6Sb8TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30524" target="_blank">📅 09:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30523">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826b26c676.mp4?token=l1u90ERBu8FkDf7RxGXPzJX5EVV4LC1vu3YZ1OJgH4fNCGccWHggTLYtP1_iQHiq8k0js0XROWc6vvha_NeDGHrnAklmJlF71_ZdfRCb_HW8ZjLuSZcSjxcrdO5DlUwjMxoH3uyqz23hyeCv0-NUvM7qa7UW7cDPvzYMdQnfd-eI0sOTwwV5QoVHZp1V8DMxVaIUJ8_WbkdHoAzNjyf0Pn7LNEE8GaJg8j0SWxL1CvLCTTn1v0EkTCvYrdxELSNxfog84ES8Nf2DBQwKtM5h5heMLOyCV9XC5iYs55aT3WyxUrzGgGPUv_Zstmsp23TchkMFFRPtL694aFUT-FbDVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826b26c676.mp4?token=l1u90ERBu8FkDf7RxGXPzJX5EVV4LC1vu3YZ1OJgH4fNCGccWHggTLYtP1_iQHiq8k0js0XROWc6vvha_NeDGHrnAklmJlF71_ZdfRCb_HW8ZjLuSZcSjxcrdO5DlUwjMxoH3uyqz23hyeCv0-NUvM7qa7UW7cDPvzYMdQnfd-eI0sOTwwV5QoVHZp1V8DMxVaIUJ8_WbkdHoAzNjyf0Pn7LNEE8GaJg8j0SWxL1CvLCTTn1v0EkTCvYrdxELSNxfog84ES8Nf2DBQwKtM5h5heMLOyCV9XC5iYs55aT3WyxUrzGgGPUv_Zstmsp23TchkMFFRPtL694aFUT-FbDVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل دی‌ماریا: اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30523" target="_blank">📅 09:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30522">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8VequIst40nRSSo3gAdeClXBNRLEYhAvrqrOC7UVOD5ZszJLHvRLlrdPebEyGByUFUWkjN9k_4LkL_b674_tBDbAI6_gJ6aKfVeWL_v_339GUujTpGEnO-HrfeV2Bh8hrFktRSO3aqEyHnBNmTJE05aKTmYIxg3xPPa6mTCJho91-qy7v44GBddhZgTs9vW2Gj5QcWL_eU03WRBGk7rkEHrAdid5yVP6FcNz1lrp68QD9l3flzJorIwpEBEngbfnfHp1I4JTbqKKijainQZArCzbCg-xGvPK18-2nT3lrxx8ZDgzjEWyy3z8i7XjAZ3ppqckw-w3Pi9R2jDrpBndw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی رضا دبیر رئیس فدراسیون کشتی: از تمام قدرتم استفاده‌میکنم تابیرانوند ازخدمت معاف شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/30522" target="_blank">📅 08:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30521">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcnM9aS-E9bYt6demfPyZkBimi35y3sXHdSC9FyCR7GuTWoLKg7SSvj69I5ivbJktBHp4qMyZiRkGHa6XSCnyyQCCmYPEbEuxcu28UeH3OHE_T99m-tRaYLEbej8ggqV9e5tZAt2MMZR_PDMujcldVMW9xhChso0kofIdwV7py4rpEAa6tyjGmkiyEBCdKJ27IDEdC85XV8Velpj840zeQy1XeMZlSuF4E3SJQh5WvR0njV2CD-_q1cXWikfG-02ZkyFPxBJpJyG0YkVRlk-CZb6blDUE71c_IzChJPEIz_Q2NCcAqz5CkIGt_gfzNvv1dimP-lKQ4VkMkwR3KaRhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گوگل رسما ایرانی‌ها روتحریم‌کرد و از این به بعد مردم ایران دیگه نمیتونن‌حساب‌جدید جیمیل بسازن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/30521" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30519">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009c394c65.mp4?token=ZSSFT1Z8Go-t07V1g_4gEH3F0HUikMxpmI41dHwLF-t1273niU_nfV91AAUAsEJfb_mxW8EkCsWFuRpvb8lAe3IoXZHlQU0-baqo4R5zDaxdV_AMkzf1SGgn3_5kccYekoJa3wzoiyAJ6Y4y-CFzBw9USKiggf6_ktLlubC7pdVHJQOYdbqjrwCrYOgnz2YZs_jI1vNDr-cx_jJ2VBi86NuHX8fcUMcU8qpN9lmTluFN3-t5kCbgqAFW8NUMvRMO947fsspcCx2Lzsp4t1y-0ZR0yp1Za4Sm6WEH7LgeYO68UN_5t7V606CB695-bTQ60KNvctSydHHbDfJH1nymeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009c394c65.mp4?token=ZSSFT1Z8Go-t07V1g_4gEH3F0HUikMxpmI41dHwLF-t1273niU_nfV91AAUAsEJfb_mxW8EkCsWFuRpvb8lAe3IoXZHlQU0-baqo4R5zDaxdV_AMkzf1SGgn3_5kccYekoJa3wzoiyAJ6Y4y-CFzBw9USKiggf6_ktLlubC7pdVHJQOYdbqjrwCrYOgnz2YZs_jI1vNDr-cx_jJ2VBi86NuHX8fcUMcU8qpN9lmTluFN3-t5kCbgqAFW8NUMvRMO947fsspcCx2Lzsp4t1y-0ZR0yp1Za4Sm6WEH7LgeYO68UN_5t7V606CB695-bTQ60KNvctSydHHbDfJH1nymeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/30519" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30517">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4ZyJ3eGQDX8MqaYga-951U6WrzcQGbYfHAO58y3S9Pd4XGoY1650w6Cm8Y3_sY9rEZHL1Ly6uN-yDSeeUSIUT6P0Nh_L1vEx3pec31F7oiDBOyT-8T2Y7oZT6Fa0IU9pxyxW_9sL16ztkeMHdRKBTNbbT4krA1vfnKTd3Agv02wI9bsSKJsiKb806YwC7Une5VtIaiNnkyytuXlwbRkpFx5iPhsVHrqLrLzDHW6aCeB21-pRC2zoA4OQ8tqDiPaHqvHmbRW4w1MAII7e6c4EXyizM_dzFFD1bgzxR2EcGqUaVXURLbRf23xoH2hljIu8NyiINMspLBi_ARjFs9Y6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ اولین رویارویی رونالدو و ارلینگ هالند با دوئل جذاب دو تیم پرتغال
🆚
نروژ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/30517" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30516">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/exCt23Ct8YzFKAyjhnlfjK16uczKMRTKB83DVXlu9Y5v_nJh1S485HFh9-zyFpEyxR4ryo0dTeSlYpJuNvK6iGDyayCVeUYr4gJYYMMQzgbRlwsDZQq96-ELPQH_QA3cxBnZYLR54Zn4rUBuSiqvTmE1Hqr-1ZBsWyqdu2n_QqnWLsNFjLx-84XcxEK0HsRV19N7a1wS0_GvgT99tklG3X87vgaP3mFtnA1u3NSbOX-1H_ek5D42-5Eg1Rb-wLxxxK4Pz0iGE8yWA828uxvzN_3KaWxCFttMirx92lX30-7FbRmblzvV5vDGeZc8x0UHThj6OEcY8y6XitjbCl7S5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد ارزشمند ماتادورها در خانه انگلیسی‌ها بادرخشش‌الکس بائنا و لامین یامال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/30516" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
