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
<img src="https://cdn4.telesco.pe/file/GIS2peHtcf3msVut9FVfG1zY-UA2LjTa6JUZ1qV5tpXrEH5oqAFPEr-WMc5a7fBKGnYcwq2Y7Js2XcycUHWxmJ2pqg_qb7rwD2xjiiv3DDN-t4qMNYxcg172yxPQNYvQaAW62DtrFFuE7agDaFIkVr89Y5gXHD7I5almKt0FibHz_mB0wt0NVYt3ejNVDeHtOvKN376o9KEVmreOMjcJ_OnbZphqYtI3bfNIIEENlngi_LljvhMxhZoKMMXsEc7FMgDZilzsYt-AluJtyh0Gtsp-wqSF6DF9DsYKFNWIYG3vzqy1dXqluakcQ6yvHzqgWQwVJm9y_21S28uKfSohWg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 208K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 15:42:25</div>
<hr>

<div class="tg-post" id="msg-81361">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUXPVenySKtuG0LqfEcgzP9cmzQ9cHEbJZo93u2SsBgkAH9NRWnOw9O8FxU1AYwFoWIsRUdfdyHqS1X-i45ZkSUEphb_7QXculQbG5_T8ZCL9PmrWrE8CIC5pJosVhBCJmn4JTlvUOaL9jPt7nrLWD7mhow6KosdcWSJQg7HGaPD2JTBzE-eALpdSAvFVo5rV68Pu95BywYuoG26B2UVsAXoVzfOTpLVDQ4LT6UdqXsxURKWi1gJz3kQR2M-Wm_EwVXln7b0FpV2FW2rCXCnEBn2ip-kRlKzt5dQ8ORVdqSPa2wLpRwYgr-7aLwip7ioP2W6uEFZ9SEe-e0BjXkeNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای کاش پنج هزار تا استارز داشتم همشو روی عکس شما میزدم بانو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 2.58K · <a href="https://t.me/funhiphop/81361" target="_blank">📅 15:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81360">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تو 5/5/5 تنها کاری که میتونم بکنم خوابیدنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/funhiphop/81360" target="_blank">📅 15:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81358">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/funhiphop/81358" target="_blank">📅 14:57 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81357">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rYdGBYPq4wiQHKJ7uXofmow7zmebMMnraIUSBzLBehz542BIIw-B5vxunZCE-ku_BBnB2rNbaV0o1ZfVksaGZKq_irItcYlylqqo36DmaqzGWMx9spLKuxjNfcQTw3HpDCNbGsgukAzLG_B-4aX4AuLikc2n-bXYpOGcqmXBX1W9Q2MERPWzWt2Uh55IBG_0DXsYFzEY-cSkXq5fcWbLoVRjxiSTm4nAchr_zR04K5P9gofn6s-PU-z8ps4mHOYAjsu07KpPu9Qzd4UIuBxb9ASsDuyW-f-D3fdBGCNAxGcelK1ybJukrrEhuV5Jed5lNswd5Ylsx30NabF0i5nEEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیما تکیدو رو بخاطر برگذاری ایونت تو ایرانمال گرفتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/funhiphop/81357" target="_blank">📅 14:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81356">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVjlfeb3N5EoHi7UBnMtq7UU_Vv-RvZqBFIQ7x9IlUas1NpfO4TWYTNPt8ZYYOPZ9ctbfVjN003mPJGJjK9mwwEqy_UMRFIhCz1qmRIeu4KI-NIneLPKP_T5TfOdetsqYdDG9IV3SyP5pYLPVH5Yax-0bYxYYu7WBIhXFrfG2Kz6xUHxH9JMnARWQj734_9pRvU15lzqil6ayoGqtDCBfBstHJ3WuCR6lKYCxPZ0AiBuZLleoU4g7iitF_17zWpNEn2PkQayaNE1ChLh4qr3U7ZF4kcIakCrZdWS1DZ5tqztdMckGOI27dgPN9H1vKupwmjIW46yyF1HTEFT6B_EeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 8.38K · <a href="https://t.me/funhiphop/81356" target="_blank">📅 14:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81355">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">سری قبلی که نتانیاهو رفت آمریکا ۳ هفته بعدش جنگ ۴۰ روزه شروع شد
پس این سری هم ۳ هفته بعد سفر نتانیاهو به آمریکا یک جنگ تمام عیار با جمهوری اسلامی شروع میشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/81355" target="_blank">📅 14:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81354">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/81354" target="_blank">📅 13:56 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81353">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خیلی دوس دارم بدونم اولین نفر کی نشسته تو فلایت رادار که رصد کنه نتانیاهو داره کجا میره عراقچی کجا میره فلانی کجا میره گاییدین</div>
<div class="tg-footer">👁️ 9.55K · <a href="https://t.me/funhiphop/81353" target="_blank">📅 13:53 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81352">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ipx-rIWjX_9xngFFF1Cj26x4o3XGbCpZ2hrXUq8Er8zb4K_45u7ytlD6ywtLSYbAB6fUQBF5nR_0lXjIit7iI3stHLHkJUd57CLvHdk3PFJZYizulvvqaV-SJDpuQ8koqSBEBLxAJRLhaRaO7W2lpq55pLwQix5cfYH0ShFRFW4QT407tgNAGYi4DJ9yVTKyTU4hLaCEqeF80PfEuRnTFwd5Qc_c4wTcV60as49QUV7rAww6lizbuqQRYP6wnbzQ1HEERxekQg534ft8ehI8B6dkdCz9M8AKKUo4YxSZdxAemjMB6s8iAAngP1bjruKWTtMQ1f3FX0nDdK3ZfNL5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی خدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81352" target="_blank">📅 13:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81350">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ISxZ1JARJmjWaMjZNGDPzspOwzDW6wicvkcqN4LNXwVeADVlVUo8IJ8LyRkB_1QE2zXY-1toOruT8dhJBH4wRZkG7gIbqt1-syTGdRAreiQDckQR1E3DkBy8vjuIHngTtvJ4M94MzgeA657Va2JXuBOKHvARv0ZhI6KzMYPWd9z7BndLnS7YRjXGSRlseRUDMpkrtD3KdrR8QxiJJgY6MwXx2c1ggYaQMMADvBk01xkwvhqmK5xFXUaeZvoMTwy0WAJfpJ-KZo19NYUOnqg3ymS6YneF044yv79fd4QxF5YAa_sLW_aWpEYrjazMrK93I5BgFfLCmNnOFS82PIM38w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد دیدن این عکس حس میکنم تهی منم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/81350" target="_blank">📅 13:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81349">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">این میمون چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81349" target="_blank">📅 12:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81348">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R8Xj7Q8Voji3JRs2xh0uQQPy7Q3GOL5pm7pXxiq3GAi9W70a3_hX5WJBXOb3I6Ap5zNjQGZ4drDVAG2KUPiUXTpywiHZFdk0CRmHHgj8TL2iIrSMUp_8RYIwO6Zk14p8SYvEZJOzZVqsg3OIRP1Hxi21oOhcFWi-eRs0a_1zkDCnH2fH1rLGwt_MR1MmrWUOlMIMNq6hwyy9zcI-rUyGslfBWhZL58PM43HD-UAcRYjuUw-KAJNYpHnvkqo4h20C24aAuZxWrYZoihC-zjaKP6ofyGdNGWLFfYUXvQQSGvQ_9435Ucs5L-smJbdB0IpMnJZ5she4Hl8NI2X-d4GRow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این میمون چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81348" target="_blank">📅 12:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81347">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/81347" target="_blank">📅 12:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81346">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph4YvjhKrVuL18ZHTUKknl_Xz5isDt1vGJCt6nCuKY2YQufbozV1T-1YXRtel0ThOcHMc2_AvbB5tMTRu4JSBTKCUpHfMu3BUM72sQp8RDrw8Pmxny-M-GjgEJ70l99gau5flzo9C5A8CDsFg3alb_lBcjhUp4MtQ3dKIgZb72JSJ0NsekGxLNJZRADGPh66Cloh0ZQtCVpsKv8O_AEQXGwfi-LULVxo5P9uIkQQQ_1f6PVG87fao6zQ8gbsFZ42pQODcAKYm6MunY9-5d90pR-kVKIXfRI1Q4_r23Uyp3Yjtm6_HhdfuSFyY9XjhDI2ey1zS7ar3NdFv58NvAFFZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچی دیگه، ملت اختیار لباس پوشیدن خودشونم ندارن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81346" target="_blank">📅 12:05 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81345">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🔴
نمایندگان مجلس جمهوری اسلامی طرحی را تصویب کرده‌اند که طبق آن، تمامی نیروهای سنتکام و حتی تمام شهروندان ساکن اسرائیل، چه مسلح باشند و چه غیرمسلح، «نظامی» محسوب می‌شوند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81345" target="_blank">📅 11:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81344">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سجاد شاهی پول ویناک چیشد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81344" target="_blank">📅 11:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81342">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U1QwFpiP4UuVdfOdjiePUhCFTTWY05LkNT3Q8saMiUO-eKpAhKKiYKxdyqjddpqHfMFIINOvQBcsH95I_3eJ2kDNwqK3UhssiH0DPZ2R3rlkbj3-ZX11EEucWOgObheEx-j-wQ1SOS2Xvvwg83luhGSi56o4Hl7sB4hZUGGcjNG05NELJpX6K3coLTMv_HMZSRo_0fGU9opM_sB9CJ0RoQmjIjTX2raPVRKnjXq811zEpD52i0SNFlKgpA7lWJAdO0mJ07QAHRJFLOQKRYIysHmak8SO7K2IgEcfVgEXNCFWfmb_ZaDo2fh_-auCVceZE7lcasBPDTf5OOtrRx0xBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CAv5pyTEgCjhXaiz5qonsQlyKphgjz78Gswp1F_vaej0Ctqp-Ke8irFM8r5fqjh8O-01NLfNmNgCYKQr62_7NM6NYic1MSmt0gnUKzmq3J0iSCJuMh7KO3BQ08N3Glt216EZ6FijZCsaHhsuFYGo-FoeiZQAcM0txOISAmZ1DNxqlF_aMhDEUTuwUFdcI5pemR9WzwWqGBdDQzZ3sJinoppGWqMkv3t4aRae2rw9dal18a6TSguAg7h0i2jMDwiKD701cP1qXqllN2YYNRWWCVpPDMC0p3TIc8TVKFyVN9FF2IFE7AeBRoOPSPBfZr6C4yF_Sqpj0y96av4LrrE57A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رونالدو در کنار چهارتا کاپ جام جهانیش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81342" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81341">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4ggASoXfmKqNUbUp9VeH1wosNzP7NJB4N7DqaehGLb9r5vQBvP_KTfryS4pjqC9Zlh29ggwhCLAFCe0y4tUFbNBLKVvj-icu3tesJjhnMfItXGJSdllOglgrb3SJ2oEbRv4-MMsF_3yv3q3daflTwtcxgyVRPx81VZQpGtG4GGtp08-uoZfqzgxRLgr-4dMLe3agN1vvzurPjeA7-6G52q6dIYbr9UO82ox7bVuCE-C_xuCBozFF3BAv9otUq4bgrc9poTKW6L3PBZvBFZbxmywpH0I9F2P_pIP4dBGOBkSNT4CqhlJROsRuNirdO9YwhDlkaVi6IFgUMmiHKT-Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
گالاتاسرای
🇹🇷
-
🇮🇹
ونتزیا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
دوشنبه ساعت ۲۱:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
گالاتاسرای در ۸ بازی اخیر خود مساوی نکرده است.
✅
ونتزیا در ۱۶ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر گالاتاسرای ۳.۴ گل در هر بازی بوده است.
🧠
به ساعت احترام بگذارید، زمان هم بودجه شماست.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r5
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81341" target="_blank">📅 11:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81340">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUQojo29Qjyh7goRX43QFrtYe-BhWdCEMI70WeFHYS8yV0E0eo9R17zdzKsMQtP9AnonZmriybdcQIYM7qeXeL4Br57tXMHiXVAsvWY_N4WWRCl6qcLHREWosviBlt_XFJ0O53DDLFI8i14qds5Na-kKWR7btG7P90aMBwaE9fOIMVTBEhDhjE4rgQOv6xCX5k4MpTYy72e0KuCNLPTpPrmxqQSMfywCSbXRn23ZWillfNdrceNHOu-raXqVkE1Zt7mMdova2AoZzg1SdJhR2z1bzW9PCWlX_nSuWGfx9VDckdoKRZVr8T3WmcHhL0Aq-9-VKaOkn111HItnB9MqTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز، چهل‌وششمین سالروز درگذشت محمدرضا شاه پهلوی، شاه فقید ایران، است.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81340" target="_blank">📅 11:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81339">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">ناموسا دیگه کلماتی مثل "آمریکا،ترامپ،ایران،جنوب،تنگه،پسر عموی مهدی،دیپلمات،میانجی،جنگ،پهپاد،جنگنده،زیرساخت،نماینده،مجلس،اسرائیل،وزیرجنگ" میبینم کهیر میزنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81339" target="_blank">📅 10:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81338">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTD_IrsPGmveuxEnQxfOjtQFXKpo__dfbPj7J7-SvapR1LrnZlYPde4T9okwQVX8VxBRpw3GUrhAbGoOGO53YDFulJn8sqdX-XfXz2LzCrZjH9Wg4VCEse0nw1kZaweGaB0ZSJT1OBqKdxyUenVb3zGolDCXppq6woz-4SowX8BvR-GoHxgox4Hvz5oEBJN86vv7RiwYR6T-226WKnCvyiq-sBFtY5RueMmVHFIZHz8b_ZbpJQ35pYBTp02bXpMsV4lNUkBbOw3hJrhRy34Sf_9Ee0sTQ-XUOYxc1mITbIYxrNJ1vZvpqI9wQLeEmGCpjlPZmY5aN74x62q8V0RnHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به به مگاهیتِ تیک تاکی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81338" target="_blank">📅 09:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81337">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=NbkhsjcapYikSN7DHm663YqqzNGI-NuB2qmjEDJh-YPxUvDkFL8bGUhoySV0QfOeYwWVl8si_G9Wy0IdSyNaqKR26jn0RSKXISePKT2ycb9Xi3SV0jl6cnQxFgYW9fHVJ0_U1tArdMWTM1r92Hy8G3SYoQZUwXnQI1rLUFO2VqxlwWzWttWBHv-PMwIEpNEq8lc8RsqiArRHKRPTgjbIk25PnmwFO0zCmhzHqXk9iuXkModMF0dVfO_BLLybLK38LqspkjRDzG-EDZJXa_716YgziiC0CoeVr_F3MeMfttpGx3qLUVwd_nOgGOLm0ETLfRdnUhQ9fpnpH778ZuyaOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bd0a311a6.mp4?token=NbkhsjcapYikSN7DHm663YqqzNGI-NuB2qmjEDJh-YPxUvDkFL8bGUhoySV0QfOeYwWVl8si_G9Wy0IdSyNaqKR26jn0RSKXISePKT2ycb9Xi3SV0jl6cnQxFgYW9fHVJ0_U1tArdMWTM1r92Hy8G3SYoQZUwXnQI1rLUFO2VqxlwWzWttWBHv-PMwIEpNEq8lc8RsqiArRHKRPTgjbIk25PnmwFO0zCmhzHqXk9iuXkModMF0dVfO_BLLybLK38LqspkjRDzG-EDZJXa_716YgziiC0CoeVr_F3MeMfttpGx3qLUVwd_nOgGOLm0ETLfRdnUhQ9fpnpH778ZuyaOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/81337" target="_blank">📅 09:41 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81336">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فک کن این قیمتای بازیکنا که تازه داره تو مارکت معامله میشه رو بارتمئو ۹ سال پیش میداد برا بازیکن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81336" target="_blank">📅 01:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81335">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">فیتای‌ کنسلی بیگ شگی با پوتک و خلسه از آلبوم اکتیویتی لیک شد:
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81335" target="_blank">📅 01:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81327">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ojJn11NE6alK4-y_ofQ3BP1tFimyihxKebXagmJGvTpKWOt3sm_AViQ9njtC-zTCAb_L7lgrRzDybs9I_S7k6rveXK4LtgG-DBp4QT4YGME8YFgNwSp-a5riyYlJ3oM79TvQQqPGEXK1NWhY2ohLWVHi8J_hBqrvDuEtuMG6JL-_6bojeA7gMfXihsRpLsRu6909wqOdeNFfZqp7Cd52lzj5p0yk8HzDJIQZ044XrhfBjQ_UqXcvFOdcx4hzQ11PfsG8U-iWxS43geofpwhpKlXePPDHEzJ42S90n318qr1J6BA_VhmHKnKdohiTfcH7Rzpnez2RPj_EpK7v380wsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ue3p9jEJl15pbG4nxHurkMqeQgS52SlZ80_BRVCinyodCJ0y1bYY6EHhkSHZiR7J9gMAOQjxFcSultq1G6j6-yjj7EekH9728HMIQTUjSktOckNKlytfWXB8r9VapmKCdWahJ_sl0pU33x6cdooZ9TvzYgq9EWttkytN7UWThwt5d_HiCM8uUWcJ1WyPSep9qN3TEGxovHbmBGXHO1N5YLuuvtCiFe9PPqmZ1x_b7UyjKuPDbRPwFBd4cN8cdSQeixKcDBP0TLAzNDJ4NZr-A9Kmqh1YW9zj76WPSiC6QPKSGdOoDBpmnMEyEaqTCRq3EjAvBa0ITa7xdKLWs1SXjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vscp28LI2jlAJctpoDZ5GqtncGo0vEIYdcgH1Oe4FwZcpP6PayiyxpQFF0XBsa-KdNumPWUyL8R6pCCQf6fvDmhYF3Yt2Qon9diR1vzJ-DAdWloiLTOYb8laRNQW6wCLmBs8IrIvSZIzbEchkeAzdO8DSj5IqjnW4ZjHrrOOA-5GmRXcraqktIDaDxPJQySkx0DFl1mksBlbNAteiVJzohFcPxEEyjt7i3DFd_YSpMvKigyclSCmW_EU4mIla1m0DU9s-ktfymVQj_ElpeBwOK9crf0hPye4f9rItjFwGcBvWrMs0OnfQcoejzmi5E6nlYhmLLt9ULVk-imKV54Uvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ODxP0qRp3y7TQpNMgPJzD8AplddJ7dLA-Z1nNNT5pl01SrgqUfhYjTmVRZ0qOzGbRZm3VA26XBe7qnqI7oqKf-cHX8qK1wP96kTCo8T9qhuRgUV_3GtftWqYCitNVCwcaZ6FuR2Fb6SKEqvqgBIsghbnk1hV1-sD2J1UN0HmTGLpU5x_maexe3BJO9AYpqPhjD6dsQGGnwc-YZFoeCTZ5iMlXRSldJ75mlQmvISQNalLKgicyjpAJlLzfD5eJr2EDvDGEqycD0ACT3jJsq_-pW81yIgaPovPvw7S24Fw_TIjQ3-zDobz7qApwq0Cyt9rdYZgiovGhM6c_Ozx-VETOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ob1fCVD8r7p3NhgB9EIN1l8uquMD-c06rVy-OWxfQfDfAr5y1EGRcQs_8G6jw8U90qeZ-y-VS-jEl2yWsw5E89DKDGl6RR3tKJ9zSCfZBe9SVhELnL7ZSIrBrnhTdIUdQa3sDpzukKDCC7GcJWv_SamJPbivpgpxBY10dHN3k5_Gyn0mc25DDHJtC8GwB2rmtUXvGdNOJrTVlkhzKNceQxsWb8cJtz6TT-ouKhTPPh3e3ou2nWQ9oY1g3iAgyxCSEsrvP0fucFUzpmPtIQKiHVxtUnIUDv6jDMCyshs-1Zv7EDXYOp16EtFL9tVHIuR_oQRCQGfXXTQkbKTG5smtpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UJbQuLCWVHB7OsDyVt-ITWxLQixuwi-dr3gXesaW6o7V-cuJqRH7XcwOvGDOBTxhbM4e4-7JxM3mas6ITzmZChATIGxuSzFYjEclSx6Pi-XuCon8MZ-NJyRGKxPF10SbuY6RB_8Wgdg3UAgzUtCxCoKaXys5SPhTir7_J7QNsfuYQzsF_V91dFkzdhuTwWPE_ttm1K-jMPEBTMjC20eRWxeSQjUGVJA0AMdv9IxqYcHYTernRJ6JRdd7vR6OF4qPGG1YAvn7drAmmK-cBjcq_74FuF1_z26dFjA4qjwxDBbln0_H7PpNV5Y7EQwwM8zJ3CwHHhUrk3RZS2n53sMTgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iiq9bpYwROXDBjNvtnTvElkAbiquLW99OKrdQLqyVOAF6QRrv-OAAm1aGkJY1J3UvDI4huDp5bjwpGaEHb-K4os-lUDsNQQLJpxqXACGCgIrCTn9CPmOHXOVk3FwBm3nQPikDKuGkJRiCizFyIhzmHdIGjbENmokBvaJzAn5pPQotaIrVa4Lcek9Rit8WhZjc955BIq6QL0P_KWEWf6sBZoWvL9W6iq9c-OYvuBqfMtX9pCwwfHkUn0Iyi7HYZgnlVvZGD0DNfmHCvwQSFRNbXkt9LpaMEp1tDLcBlAKLIHJouVovKeJZHFqnmJJIjb0AUQ8uvPDsD1uML8Dk61rXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KsIfWrybWGecjnJzkyFnLjtcqCZyyVBAZHsbN_KMBhD6hUDpeu4iF8PIanOx7Clk3MsYl7_VhSPXbNVrQ1IQKI4DE7Xaalm_RFZxAlH_iknHfXRi_mgq4LWPXlsy6b18eJRhRhMh1-ySLGDyjq5tzOMberFOVvk19_XxWhRRvb2v2v78eGu-lcNXZtm86iRWkdMNfJWDi0UmTTMld84sPJUSav0eFcJQVNzM3PItpB_oIEJSK5-PIgk34F0cjLpsUe_zvbsJsTYVasrWXgetFKTczBi-nce-CMzkI-y-yW38JCZaI0hDOpE7rlRzUPOJq4GmYBcSLE3xIQ02iFMF0A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید بازم براتون جالب باشه بدونید که انگار بعد از مدت‌ها پول داده اشتراک آن‌لیمیتد خریده و برا همین بعد از اون ۱۵ تا نه تنها متوقف نشده بلکه تا یک دقیقه پیش ۲۶ تای دیگه هم پست کرده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81327" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81325">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R95OSKvwFLbjsYh3oSove5R0tUfaTkGDXP_J07Ce6BcdTakn4v2BK_hrQTuruPlUoqmJKayFJNFrdX-NKpfnotx2oURvFJBYrvWIajiWp8US9LrYT621LWjWhIHVjMJ8yryuz8vVnEfhZh8sCv1TvsKQDY4CBy9Jf66rB_PUGw9b6go_xahg_q_LcKbpSksdmAtF5yyH7UJG9nx373o1DrxmbuxJh7e__Vr2_eOO3W56oaV4AsO7DYwlYZB1VVCR4V0gqlRHMFLdlKd1RMbP_pljC1JSI_bhvyoyyqXMAkjeCL6vW8qYcLt_fBxR29oqdMdj0q3yvTM1jb546ymdOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ اگه گفتی وقت چیه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81325" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81324">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81324" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81322">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وارد 5/5/5 شدیم و کیرخر، تنها کاری که میتونیم تو این روز بکنیم اینه که خودکشی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81322" target="_blank">📅 00:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81321">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">جدی جدی قضیه پژمان جمشیدی رو فقط برای پرت کردن حواس ها از عروسی دختر شمخانی راه انداخته بودند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81321" target="_blank">📅 23:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81315">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8KhC0TRkm7UxYJT9FTEsjngRhO3asdUJ5otdjQZ9OvwF0fWEyXlX341krYPSjjI7EVfNRR_G3yzWP1QEscprf6xsnNl-iaIf8JTEInQhkL_K35XIhlTy_wpJbpfhGMQdyBjgTt5fLN5VTrX9ULglDdCFxUXm3TV8dHu6w5zw1jj6LwXQ5r7S3597ccOEo7Z8uJuSDqkWCOa_SaS1kqPrs3KEOYAe7gi8XVkOF_0J_u_AexgwES3flcuQXTh5clWWexenBkrZQFc8iIMu76u4VCkIh54All6_forBWOBrZQ6spjGdNUaieau8la9Z5pwBYurba4-lUyPRqTFIK5c_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNT-6QrfuJw5ipbUqVlYi-LnfqKmxw_A8y5Vilrad0RYi_Kd3ut6mL7wXWmLnumU_jFDkFpzi_yQbvo9yYrqwvsbnRXr6MjKniNviozbX9W9-mHXAQnhsc2I69y72uSk6kUkgrz7vlDK9Mt5_ExPb7sqHdgLO-_pJwmQ6hXzb5JtlSC5s_xnIxnmgMuUFhhzUbowUscXG7eAfJ7C3zGzjHgu58Dk3Q-DorGDGH5c2KOe5qFOreCyvtUA-nnhE8JlnG9KzxO9tTYrLBzsAYee9VQghNzmQcfcFAl8t7sa-qbDEbdfEmWj3SWRcpwojxekogqnj0DaqpVXzz60KoHLnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-tNkSrPT_t7kwibZnhEoz2hi-XgXSMlcPf7AaFRCzuD65Bh3b0smvgF-wpCe7mye5qRcDrGRCPa3F0IkhvQZphjl4zzN1c08G4gbHhf3JtsnAUNJsfio8nnjeJkvxOIaOWrSfK9iOyhjbO5dr9h9CEc_LjPPzK4jYu5qTdI-6gByAb7PmB69fB8qNDq8P3Laki3lFy8C2px4NC58k6AS2vx1djzRBFzW1J9lR5SHOtFtvUufJOGdGe8TacYqGxnn74sPWARIDZ37v9JT6EZp73RibUADzEhFDbU8-70SiYj82Semw81f9aanvzEkjG8wyYu65Xs060mRn_SEF4Crw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UgefSYaP3fyhHuLKcWvo6rBdCcT8Pap9erqdf0U1sDAMaylvdo1edTZVSQst3qdW2GeVYiGhdSJqr0MWDCJnOwhsLPnioliv0dvq5nnF0yq3pDK-1T7ovaTfgbyvn_h6eaPdgWALOsosNo23BRt2SjaWH0vb4A_RPR19sgOH5JI6-7MqAELyzYbcLyOeLBQZ1bQ_8_CkdgK480M94_LUrazKfyES1eD3K9ya6bePnRb_YqU8bn_nFZtApfshEVuwH92VAUOPZWblAJeqkXg0aUCOu-u5HPEDXjtev-b3KvsQmW-w4yQXeeaODklJp7_snFMka0INEo9d8MiBEv1D1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lBeuvFCsMNJp9Site440yvhBZXgGc_0xKqNFkZWBuKRoOXGqTNJ181I1Ft_P96yY6kwPRdzZKeE7NcIWXy4knbTFeWuzxNGSv-GSI1dx1kvnLIcVKqWHXFVjw0EgCPHWSZAI-Ja-ugH5mQBPEuk8vSdl0o7o6MGuSngsvcG9yZAfYQxqZ2pZQPjmBI7ocrYrvCBpUmaObFwROpOGgmPQDCFTwdfj9kOQ4JXYlN9RlHYLFM8FfZjQQp2MLkesEdcFMSL6K96cIPlHThpjHgBG5JxOJWYH8VlsOq06Tw0dHaMY0WYTxsbuTieGcaU5YlAbhLlrQeV_dlhjl--WQqSuQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRVlVuR1GUNU21gVljOj8iJCLdSpbln3UFi22dIh0j8Mht2Rm9Hm9A1hbg6nWZhfNtv66pFU2LSqJNMl-BhvNfZYs_sUeziABJZ0B2Wr1NNnllynqkvtOZdQG5oe53KFs3KFA4VrMqxfrNArcqsZdhQ5080dVsosuZDoou9naQ7luhlC4BCWCRQ-kOs6MYp6YlltEFa2zncReARDGSPULArdhwpui2BY8qQ-5C1eHNqLgsbDLzc51r-JDQSpcS23SGHPvW8aNjv-diQjsWuiQezFzc03uVSro9RKSdmuU85NHGacVCatJOZibWTBYQx-2gBiVrmXBZJFDKaX7D-ihQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گفتم شاید براتون جالب باشه بدونید این اسطوره از ۴۰ دقیقه پیش شروع کرده و داره رگباری کصشعرترین عکس‌های ساخته شده توسط هوش مصنوعی تو تاریخ رو بدون هیچ توضیحی پست می‌کنه و تا الان که ۱۵ تا عکس پست کرده انگار هیچکس دور و برش نیست که بتونه متوقفش کنه یا حداقل ادیتشون کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81315" target="_blank">📅 23:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81314">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k7k9QkxLLdvQtycUnQKGvHd8lFZvzJJDnoOue5u9DVvCNgmeZcb_DImgTfEXHZvxIni8oU0bQ0enxQl50y3V8ikK6Q5mJzBUSE3qwUncwFnSs__bec9i9pFXVTVZuZzk_Bs-a8DWOlTcKlpBj0ngk7xPwPa0gFf_02QEUC4yeCtT31S-yZ10Ej9mhA8xtTVq1vRiFqYKh-gDI7Aso6S9LkMpkFRKwVyLCmyP17xdy6QB3PnYS5unTlRe55Ai1mojWQCT_wZfZA_yCSyDSfEDBrgQN7cvk99kXSjgYvRcVb_F6EoQ7gIdXeNBml4aD1ebI_f3luAu4jr0nvOulGADyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏پسر بیژن مرتضوی اوتیسم داره و استفاده از ویولن سفید تنها راهیه که میتونه پدرش رو در میان نوازنده ها تشخیص بده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81314" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81313">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">در طول روز حوصلت سر میره ؟ میخوای بری سیرک ولی فلجی ؟ یه چنل میخوای همه کصشریو پوشش بده ؟ افسردگی داریو پول تراپیست نداری ؟ پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81313" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81312">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuRsApYo1o_v6Cgw2yCQaP5Mn34q-k8SD2zoNa1qKltuGE8WJ2pKT-PZSjbh_pRVZfF9Xa6WXBXeJUTQ3WHkpJSkkET6Brq0gUVgQLN-yn4csi2W_vN-v-bqeagC5duU75-0X7rducUiYWaJFSEWeamffmTGdshjNyw8CVVWpSjDEzctfcmxyLZgkwrd7wppJ04lmQhZRhec1D3E1YMpMoEAv-de6F2o5gJFbz9BqQzPHMnTDB1fk_cD6_2Si-s1PkFOzMHNpaXO5pHkUedBNQ1gAWZmYty35Eo3RTmmJCgrChY6DjEGtMpWl4QktXmbCNe8_QevpZL_y8ICUOrCNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در طول روز حوصلت سر میره ؟
میخوای بری سیرک ولی فلجی ؟
یه چنل میخوای همه کصشریو پوشش بده ؟
افسردگی داریو پول تراپیست نداری ؟
پس چرا هنوز این متن کیریو میخونی سریع بیا تو چنل
🫪
❤️
@MMD_HAB</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81312" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81311">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtYUoL7cwZmlnke0gs7XPkiLwPHL_DiPvok6hmzaEhkY_t4ikSgMbOd7aMD5ydYzkeR5s0crkAqa0HQrtUNFwnK034qBzMp-g-HvSNZvHlusBWP__CDfpP2U4nk0zYvKqN8PoG_1MpNzmx5Jq5MTtVcVYVeWlX1kWNIUYoD4vIX_QP1FUD-Bst3hR6vl-KgkktBxQFJkPed79xZuaiJzr18i9t0chXmukcm_Jr270is4PiVOQHgPGNRDyKnmW2etu2VwpaceD4v14QQT0an04Oa_EkEdaOIGsFDtRjESaM2APfo196mUQFZKRAsWKi-6TtAgibqSYiKzsZKVjJPfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتای بیناموس یکم از این پرز یاد بگیر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81311" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81310">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Raf1YMLVHzMBMYe6yiKpPHm3Moo_a1b0M5JlFBX4f1wiJK8LKJL8IV2EIXs2OmrnZKX_kqLuEmOUu89RueAtKsZABAp_7waOJiTXOAwsgRMf3WtEK55_IcMno1VPRUS-Prxwz6kVe5QxV8SmCbAbK1JCB3HXZtjYpltMyi8zJik_cxaAnazvzgCQtbNASWmSm_DAqoLKxKPoNld3994dh1HbBoJqfHaBuJv70bKuGjan50lc3ASfuTUJwhUyavfKUcf3xK2DZRIfJ3K0YmKDh3LDuORtYFWaKnswy39v1hOanfvWGaNf1Ib-OsFwVA6GjMJGUlePja0FI0Y9YAQqOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم حصین به زنش خیانت کرده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81310" target="_blank">📅 22:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81308">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6LV4_y2e-6vt6cMyJpom8KVmyMpV4euy4IFziERAQGbP1So2SeKbFzB8MFby8CCf8laSBheExex9RXFOJbI8vkWRCKrAS1wTNT9BAkKSD6nvXP6sBW9P7KhLb5-IlgKrbScKHzeHx4UEWdRsn0NRIlNMephwPslKJL2pjOo67V7pQ-vSj3voqqj6x1a_HwCC22Zbo8iWhy86lilP0Mi7T8Q8_vNk_mUDhoJspPMAmZ7in7e2dFqdz181k5sJKH182hIRBm2L5ujK0B3hLA6jU4_RR3y4QsmgdRJiICcYmlXNefioBGyhNFxyCxXq43bsqxwOTFKwvRKTIWo7fTzyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیامونده رفت رئال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81308" target="_blank">📅 22:31 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81307">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2Oa1ikKGFEMw1fHT8LYMWcEzXhys-Ve0SekqPnwYkFsm4hfevI9cEibIIyxr1fs6XWW4-dbymr7ygWoak0xZ7Q-bTVR-UQyIIdHFVXYSbgEwnrRi5ZYpXX08RVtMNC4R6Bjt1xspKFtfJxI0md2GxTmRGUf3A77XJ-OzUe63OeqFuZAgGfamHuge0-tJVjxe0D5u9b_3vaUykFmz-v24uPyscP07A51iOCBrXiqtgMZwehw05w0TqTm3Sf83qSqZR54VLmRkotCzw97C7HqCPg2LSHotWtOsjlPjhbt2DV_rdwJ9-1h7WwrcvdTlZpqa890MrHsytWxAZPOJE2YPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط کیر، توییت مالک شریعتی (عضو کمیسیون انرژی مجلس) :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81307" target="_blank">📅 22:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81306">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گیفت شجاع خلیل زاده به تلگرام اضافه شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/81306" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81305">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81305" target="_blank">📅 22:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81304">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">درسته پژمان جمشیدی از اتهام تجاوز تبرعه شده، ولی هنوزم باید برا رابطه نامشروع ۸۰ ضربه شلاق بخوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81304" target="_blank">📅 21:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81303">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaKH7L259phfrwkTbYerNWcGMbL3rJjZBlAoQ-BsGgSOCv5o4GPXHPpNBN74avz-qTsqPsq5VsWNAR_NoME3PSGMnAF1-NeHmxbnN6MjKfAFPUgPqpA_sMvT78SBlP21mzNSDMJdILmG4zKiGdje9StJ2ZZFndq7tpvSPwfZ8B_Zm-hD0Pp0TsN0S9qU9Ua1hroG-Di-7ywKpkscme6wLO3yZqRUD1EGHFAZ3WLMZmYRp7QyrO_6ITrjKPmIao8wPEF-eEnbymEuHlO0Dl3a4g3IZH5uc9883toYHJQJOonVTLQDoNLYQHpSxqeebFTj3MiuczI64X7yPTRBEllrxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
وی‌پی‌ان پرسرعت و پایدار با قیمت اقتصادی!
فقط با گیگی 4/800 با بهترین کیفیت ممکن به اینترنت بین الملل متصل شو
😍
🔹
تست رایگان 12 ساعته
🆓
🔹
ویندوز، مک، اندروید، IOS، لینوکس
👁
🔹
دانلود و آپلود نامحدود
⚡️
🔹
مناسب وب‌گردی، گیم و استریم
🎮
🔱
20%
تخفیف ویژه
برای مخاطب های عزیز کانال فان هیپ هاپ
🎁
کد تخفیف
: funhiphop
🤖
برای دریافت اکانت تست یا خرید، از طریق ربات زیر اقدام کنید:
https://t.me/ToPoLvpnbot?start=start</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81303" target="_blank">📅 21:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81302">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SiMkdp6x3-HBTQ8uGYpy7mPX4hxqC5NkvFt3Sw5pPF_8R4FLxWU31MbeVPdE0yLJ6iFsz4LdgHie_53aa_wKly5y7cjPiyfUWI8vdbgU-wSJnzA-wvhrEW5wgZn7ivpLHpscRgBe0X2vVZ_-WT6fs7UP7nEirl_QN2HEeNshRQ9ueBmTUcliijdkl2_BemzEZ-Dqt_8ssPdsXBhwzhnX_o_AaLyREGVQ_hFtYLTjHOQ0ChZz_Kc4qq6Hz0RpRWMPb1oeHlbkCD5XBekQk0PqdIcUIb4QTC8MBjwE-nuLAT3E47SWwk4x1d8qXoLN3V6UytErxl_hWUBMgahp1ULtUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستید دیامونده بازیکن آکادمی بارساعه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81302" target="_blank">📅 21:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81301">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پژمان اپستین تبرئه شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81301" target="_blank">📅 20:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81299">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kWwoxE4x0ORZx_0VJWBVZpJPnkefmXtMwP8DTYbms8O2vIyA6ld53ny1zlzlmojgaoGHEUlZOmO-gq6sQS9u-Iid6kMqxrxVQL_xJ1b70T94GOIZd0yGRBFbJgb5cYxbCj5qjbg7iRmQXG9walyQX9qvSxrb2hQqhheNF4tkFojxZo6sk5bJkGg9gvBRID8qboAroEhWMGDKDWNSn5zcj9zjMOzmyxK3FHS-dwLVggLxzz5XVXzPPDELFOFos2kTbNkC9wAxvK35LMTiVvO8-zPVaQOsvTzeQrpDH7X5jZxqRMK7FcWEPOTeuoDHDsNn5TFaoFaM12pPjTo36VZhOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6iHXTh1FL1ZvLcXZzMlvFCgX8tpChZBsL_ZOBM6bt4HC_0TWd1qnXYF79eaBYHhVR6evUM_gygsgrAzSp153Np3FnvPakLFAZGuKtryfLh02C62LAz7DLkUte3BVAsuba8pAQEsz44IyZyxzsNkWnSUn-m6U1ICDj9YXgaY92re6RPGXrnFzGMAT3G6qjpQ1fMWsAtMZFIMKwKHr3ajVvUxaioygQztV4nxKEHmwlNUKy6QkHmJYH4nnkrpJjoCHaFLT6EdlUHgUePTqJTjlXRPEqSxfioxHWsWHSS0nCd8bDJVT5qaK3maq5no1rRUzM_FYWie4DiFrrLyXMMXpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شتوت جدیپ بانو
سیدنی سوئینی
:
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81299" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81298">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxARK85BWikOpcYi0Y7s_cge-tCwL74d_qCiIK0W1kaWbVXQ4wFuu_1tHdbb_NKWu_vZ9QRk88aymb-M3vDVQyv5mUwBizsfQb4oAw-B2md-23y6ZHGk3JQ_wOXnzpvKVB_vdyDE7QF9qjhR2o9RWabgpVRaFLiWcOsrILhVcJ3GxoNOTCMX8AdFarehDvPSR5-tx1VMUWE98cj-_rmyWjkMmJFy5vIWxF_ZP0gR_R1E9on8SkB5n_GEqjGrrt4mMIhSwdIhjTqNIQuCzBjT4roKis0jq9G_QR7mJ39QQKAaXLFK8Dysla5Xo_g85XbOWRQyn5QixZtVz9U_yLHDeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم چرا ولی کورتوا رو روی مبل تصور کردم
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81298" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81297">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s7XHENmF-Wt68xt_jnMPgX2dCVmpp3I2T_IYrOlk8KXPMbLOT6aKutl7LD8Vbu_4FhLIg2Fi0k6bep-FZ90o-w2VHybhWTdnoy8p2m9Uh1kZ1FXqPVAV4Ej-6aatyF8JHVbr9fGxjti-YDqKIC2fJb0_nB4t0UrodaJoQnPV2gbKtipuBpablHhiyP9rsBvNPv3dhXvMBYoXApEubESOQfvJ1hvlzZIvcF_kgRXoTvXTEwcZgTfxHwvGfh3INdWm1LzN0ove8bvvr5walN4kAOfmmI142FNW2EBewIYUsinSaPb5bNv6XV62udtfYz6XuZ-lhk3DFXoefGk9R7rfcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81297" target="_blank">📅 18:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81296">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">امروز 4 مرداد، سالگرد درگذشت رضا شاهه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81296" target="_blank">📅 17:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81295">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=PQeCKJDD-V0FPwXV0BsdXCihjdTPDei7ssYAc7QlOPqogQ8HrXk7VrE2li0v2CWuiYi9nFY6dL2bRrTa0OCIkS9LHcJtMJDDC-6ozgjRxtjhHG39xL1RDYmkEkg8B0F1TMX4jWoRmCMkw7K6dtq6sYTwS5DD_PGsCQ-8bm-x7WsWXgvzE6xFQX_GZojWZWv76CyweV3pIjQODKNS_amgx9wUEOtNkDZebiSs7pKqeIoiFxaslJXATma3Auo8NRe7fGevfVg0wANKyEdlPAwalZFVToIAdq33Uh4GftUxnQTdxttE_yl0cUGYIPtdXGfjaVyDl0HMn1qisYLvp9v-tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b531ecf71.mp4?token=PQeCKJDD-V0FPwXV0BsdXCihjdTPDei7ssYAc7QlOPqogQ8HrXk7VrE2li0v2CWuiYi9nFY6dL2bRrTa0OCIkS9LHcJtMJDDC-6ozgjRxtjhHG39xL1RDYmkEkg8B0F1TMX4jWoRmCMkw7K6dtq6sYTwS5DD_PGsCQ-8bm-x7WsWXgvzE6xFQX_GZojWZWv76CyweV3pIjQODKNS_amgx9wUEOtNkDZebiSs7pKqeIoiFxaslJXATma3Auo8NRe7fGevfVg0wANKyEdlPAwalZFVToIAdq33Uh4GftUxnQTdxttE_yl0cUGYIPtdXGfjaVyDl0HMn1qisYLvp9v-tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گنگ (هیدن یاس)
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81295" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81294">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=XW8ZaCzDXxWLdVfUn-vgQYE2EX_jy4r9B7jlLswCUd7mRE7u-Obw7vFkz5Zoo0xZGx3nOhTCo2OLNBF0MMFHXl7Gh08z2xjaJK0SZ5_cuVION9U8MXgsPBpYMAIDKjTxRQYjQvo7J8nbjtV_BiYO5hH1_zaF7Up2T1qVx_ZBy9gqijDuykjZsj7zRfVt8P6L4orkwJyuvG0_MF_73qI5yfgLfcczDK4fFNpBZ9yt6ef9y5kMh-CcUDeXuHKfZNNzXGK6uL2dizxWAQmDopK7ZvUUsV9ZC7HdCDgioR0jw9-fh1rgu49TTD1_frCKSz_kNh0ylmFMxdaHEXRFrVurhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c14a63244e.mp4?token=XW8ZaCzDXxWLdVfUn-vgQYE2EX_jy4r9B7jlLswCUd7mRE7u-Obw7vFkz5Zoo0xZGx3nOhTCo2OLNBF0MMFHXl7Gh08z2xjaJK0SZ5_cuVION9U8MXgsPBpYMAIDKjTxRQYjQvo7J8nbjtV_BiYO5hH1_zaF7Up2T1qVx_ZBy9gqijDuykjZsj7zRfVt8P6L4orkwJyuvG0_MF_73qI5yfgLfcczDK4fFNpBZ9yt6ef9y5kMh-CcUDeXuHKfZNNzXGK6uL2dizxWAQmDopK7ZvUUsV9ZC7HdCDgioR0jw9-fh1rgu49TTD1_frCKSz_kNh0ylmFMxdaHEXRFrVurhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#آگاهی_سازی
دوستان این ویدیو با صداگذاری ساخته شده و واقعیت نداره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81294" target="_blank">📅 15:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81293">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMZurVG8zNRGrQrd3lX--EV_4mhN53YZFzkPL8oloVfyswtqmYNTxIyKDMsIcJMQwDeqzI_XSFUWhW1c8ODxV0hvSWVthL6uehA-bA3Y_lN4V7Pfx1l2EGnBwN72v3mNsPKIjjhb8wbKuQ6lkeEsxYOHhA5_i6ZDGnIh8PuRg2dkB-vQ98qSsqi-O-xsStgIFpOe_XISlrnQH6jtrJTFBdTr2lJoeYQhW1Sdr2KM86Bfv9suBTdQLp2TTD6irMoJXZYO1n7Rd3kb0rQz6J4M7wbFsIUN1X20EL9_DpWulNNnugCh6kaD219dSSBMZVLQ9VhA85CVz7SL06nv_C1qRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسام سهرابی هم بعد این که لختش کردن و موهاشو زدن دیگه کلا از رپفارسی خداحافظی کرده و بلاگر شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81293" target="_blank">📅 15:03 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81292">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81292" target="_blank">📅 14:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81291">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=F4qGtv_8vkPkPJxxQ6pE4hN_4r_6hq856Sx1JY7XPxYWADUSQ4NdmfPBtEPO5bV9AXNFXeDjd24qPgpnfvzEtq8xfjxofTwI6QbmBdn35JE-7uLazEyl-cE3lQE8fbHmA_1aYCKP0vllRyH8pvndebd1tA5573w22BIyaCWOseQ6Lfq7pGXFnGRU_eXMQFIykJJXpwAF2-fqfeSRILTM9M4c4Wfj5VnNbk3KjB2PeLbPKqRvpMLAB9O2m3Aj2Mx5ROvR962-CvCg0U8ZRrletUKBYdWad6IZweEwEOQZfBm2QXUykWIw51rXYH4OdZGuPpdoe3pq_JVvXH9nifXbFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=F4qGtv_8vkPkPJxxQ6pE4hN_4r_6hq856Sx1JY7XPxYWADUSQ4NdmfPBtEPO5bV9AXNFXeDjd24qPgpnfvzEtq8xfjxofTwI6QbmBdn35JE-7uLazEyl-cE3lQE8fbHmA_1aYCKP0vllRyH8pvndebd1tA5573w22BIyaCWOseQ6Lfq7pGXFnGRU_eXMQFIykJJXpwAF2-fqfeSRILTM9M4c4Wfj5VnNbk3KjB2PeLbPKqRvpMLAB9O2m3Aj2Mx5ROvR962-CvCg0U8ZRrletUKBYdWad6IZweEwEOQZfBm2QXUykWIw51rXYH4OdZGuPpdoe3pq_JVvXH9nifXbFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب آنتونی جاشوا موزیک سیاوش قمیشی رو به عنوان تم ورودی خودش به رینگ انتخاب کرد و وارد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81291" target="_blank">📅 14:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81290">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امروز ۴ مرداد، سالروز درگذشت رضاشاه پهلوی، بنیان‌گذار سلسله پهلوی است. او در ۴ مرداد ۱۳۲۳ در سن ۶۶ سالگی، در زمان تبعید در ژوهانسبورگ آفریقای جنوبی درگذشت.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81290" target="_blank">📅 13:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81289">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aXF8E5IT5E9UtVvHDvurIw57CME4bOF9nKcsuPf3cfqnjUGozpsgGsZUQwBurxf6JLpSiPsyZPAgmSbyf8NqWylxlmt2eosMWq8jCcnWsZgDI1Yu1mSKDyQU4ZH7tNDzclZqtdz0Wqg3WyfNPrTDTKkriKuP32tczvvD1jXkgM9aSeREKIZetU9mSbqnFJXgbLnwexAs8I1fPpy3x-Di4BwAAacLTPA1OdAAfXmH1uTenzFX8YL7MEymp6Sqmc34p7gRnqVXYP_aZcYWU_konDr05T4eItLFSy1RwuZ4r8y_SkB-UkbkmKg8HtVD8aof64cjerQztjWNYxjuavYHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رضا پهلوی دیروز در پاریس، با فعالان، هنرمندان و نمایندگان سازمان‌های مربوط به جامعه LGBTQ+ ایران دیدار کرد.
شرکت‌کنندگان در این نشست از جمله شش خواسته اولیه جامعه رنگین‌کمانی برای «یک زندگی معمولی» در ایران را تشریح کردند که عبارتند از: ۱. حق زندگی، تحصیل و کار در محیط امن ۲. جرم‌انگاری کوییرستیزی ۳. حق تشکیل خانواده ۴. صدور مدارک شناسایی متناسب برای افراد ترنس ۵. دسترسی به خدمات درمانی متناسب ۶. آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81289" target="_blank">📅 13:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81288">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">جفری اپستین تنها شانسی که تو زندگیش آورد این بود که زمانی خودکشی کرد که ادمین اکانت حافظه تاریخی حوزه پوشش زیاد گسترده نبود و اونقدرا هم حوصله‌ش سر نرفته بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81288" target="_blank">📅 12:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81286">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwYPGWKcarPfJMHyAXxP7r2XmE-HrUNaNZ-_9nqZZQEjR9K9sGHpB6k2Zn5FVCR2D0snaNDvWBluPSvtbh72X07HPeQnLOpoKFGBjqsjuvKHwRojxVFqJCi_zvymVQRoXvasDJkQ0IZK_SIHvrGuj3-4TN8teGNxTFCmEUZMm5vbCkspXltOjxoXufJrSYGExxNczvcXRyqWCWJ8PqZ_yVcPp-Ok9cALTRQ8ufxlclvmvrX8yRJCbWMi83OnQsEr9ttiVg5A4b-ZqB2aFKUiyjSXIWJoJrk6HaR0kngAXxipNVJ7r8_dZFVpe_Qh6CRIiPyhHzyFBuaJPuCnd5FzNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو دیدید؟ رئال مادرید دو سال دیگه برا همین 250 میلیون یورو پول میده
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81286" target="_blank">📅 12:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81285">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfwBKbbISK6W4K72w0_m2XljQZRGX-njjSdhMz6OmduG00tBFTN48GsILGMH-fBplSF6FdY350EFof0ltqcZVkGaJhrS9dCRckH5wQ2rFK7DBXsLHLGEz58E8Wpy3Ay54wrOHGM6e4MqcSoTJYEm2l2WEmFomfxYLU_I7ycDiC-VAN3uG4jbNwXGWXB27enyExjtjiiTkuOaATprHTRKpYsSWyCz5nLrhxUhnRJW8huJyGLFEqJWO4pTwCH48WyKMJZVZwZ70V2cyOGPoP90NpdIk78L84-mDGwPdJejg8fv28FpYlGogY5S1yDeKwDQ5u3xmjUejOZzTlwqiiTHWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید صدف زن هیپهاپولوژیست :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81285" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81284">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/szpuWd5qNpP0jg69aMZvnOEJ41SCd2E6IzsP8hGbpCuoOW2elpz9vUGy75DRlPQsq8BjAa6sBZ_y0hBFL3PBTWM0mSC5pKZGoW4Ho0yLm_Rm158LFqwse281dttW4_zIbenlg1sjNukZR6v-sf6hgWVsSUJ34TXuJqlvBCNqdyvfniy82jI28agnEnltoHsQ5tLFk6NUHcdMZZpZWxIFKxsyH_qcF0zpHkTyLeAjjKDlsrQaEBRqX3zXDu3ctvlFxDYDPgBDUJPhNNPc6PxfidOuCQ0Q8XuZ851n22qEUBCNGdlqJ8QU_PgcqSI7AUWrnFElJoZjwNF1wf2MlT2oDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
برد زودهنگام بت‌فوروارد
🎲
⚽️
دیگر نگران کامبک نباشید. در پیش‌بینی‌های ورزشی، در صورتی که تیم انتخابی شما در جریان مسابقه با اختلاف دو گل پیش بیفتد، پیش‌بینی شما به‌ طور خودکار برنده اعلام خواهد شد. با ثبت پیش‌بینی بر روی رقابت‌های فوتبال واجد شرایط و انتخاب مارکت نتیجه مسابقه (برد زودهنگام)، در صورتی که تیم شما در هر زمان از رقابت دو گل یا بیشتر جلو بیفتد، بدون توجه به ادامه بازی و حتی در صورت مساوی و یا باخت تیم انتخابی، پیش‌بینی شما موفق در نظر گرفته خواهد شد.
📝
اطلاعات بیش‌تر و قوانین:
🔗
bwrd.link/2GOALS
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r4
💻
@betforward</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81284" target="_blank">📅 12:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81283">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wvavk7AIQZfvGUftpj--KN0BtHV1pfdZqLbshdB6we0Sv3sisehyiYMb3FVqsKiIXKTdl2mO4wLZkJkfxZgyXrpph88tj5U4I84g2TWvtfgkUcH4tohYmndpLzIN28KjsKabpcODBifF9iGXHpqq6wmKrWn0VMBs6AfCKYDmLSMG-syyw7LUkqbB_99QF20i2mFcu4rAUAV_sXXidXCPwrbTEwQ8dSLhGOMnbSNCPd8g7gm6ALyVzxWYQ5-zF4ROYWidiZlU6L_UDXQ3ACFKDa0Ii0H4nka9qzmcQtU34xEctR6k_geTk7ecziHQOvpt0yWrJDF0BI9VHmhvPdjlaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تجهیزات آمریکا که تو دو هفته‌ی اخیر زدیم نابود کردیم ۲۰۶ تا ۱۰۰ میلیون دلار قیمتشه.
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81283" target="_blank">📅 11:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81282">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خداوندگاران هفت آسمان را سپاس که امروز من را لایق زنده ماندن و توانا در شنیدن این معجزه‌ی جدید تمدن بشری دانستند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81282" target="_blank">📅 10:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81281">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یادش بخیر امتحان نهایی فیزیکو فرمولاشو نوشتم تو کاغذ بردم سر جلسه، بعد نمیدونستم کدوم فرمول برا کدوم سواله، افتادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81281" target="_blank">📅 10:08 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81280">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzbkHghd9wnzrh1rX9JbPkNW8xTFT_xM1gA93aG4AUqqc_W8ZNy7JElw23POQYaaoXSBJVZo6FyH_vnh8nFnmPdYWPmWpDzQkoQZc5NtMLFCTMXYZapTEwQShtbo2tf9Y4obdcZSiBRwGuWkaJUFpLn8h3c6jl9iCWdTZnmAe49qRvyhAtObO-lSshhFT_kSPGoCn494bXkcXfWyf1q3OQy_KGcnju_IWQGFrkc3wMmgn7U1JRK6ok1UZaUwDCfrtok9qaFTKSHxyk95KcAgldgLNZRQPIDCs9uGbB7RCnkblt3aQzdkQmzdzLFL_z6B6vUtWjI9OFtF34pQ4Qq2rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیاسی بسه، بریم دعوا جنسیتی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81280" target="_blank">📅 10:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81279">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">آلوارز کلا سه تا مشتری داره پاریس، آرسنال و بارسا، آرسنال چون داره وینی رو میخره کنار کشیده، پاریسم چون فران رو داره میخره کشیده کنار، فقط بارسا مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81279" target="_blank">📅 09:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81278">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">امیدوارم زودتر بمیری مهدی اونوقت حافظه تاریخی داستان پسرعمو و F35 زدن رو به همه میگه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81278" target="_blank">📅 09:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81277">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81277" target="_blank">📅 09:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81276">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">صرفا چون ی نفر تو گذشته خایمالی کرده دلیل بر همچنان خایمال بودنش نمیشه، آدما تغییر میکنن همونطور که مردم مخالف رفته رفته از نود و هشت تا به امروز بیشتر و بیشتر شدن</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81276" target="_blank">📅 09:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81275">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یارو پیرمرد افتاده مرده ملت ریختن سر جنازش میگن ۳۰ سال پیش خایمالی میکرده، خب کیر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81275" target="_blank">📅 09:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81274">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سلبریتی تو ایران همین که خایمالی نکنه کارشو انجام داده بیشتر از اون بکنه یا فراریش میدن یا یه بلایی سرش میارن دیگه اون آدم سابق نشه</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81274" target="_blank">📅 09:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81273">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ucggCb-zn28dDs3_ofdIM2KfymaEJv-LsWp4wHL4TA7sZKBQJGDaeHbVtVFQEH7z4HbOGRvOvKrcC5we3Srt2VIZjwuIxormVCH2iBRNb9nO3sJH_q4ukjtO-4BJLTPJUtfXt652nd6q6QKzo4PkHvUZuu3Z9ul2rHkLaEodbofcJmbJ3sfti2BfxDjyCoQt4i_OtQFTdNpY8Yj4DJUY3woG1nveJp5P-AqCQnItHsVbqu1MkaSUAJ1y6uIEkdiDo0MA3Vj791bsj5TZEALhllN4QVnbN3oAk5fR5TOJrhYim3RGSi8AIbe_eEWiBFgcLwtVVVz3NBv9uRskQM3XTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رشید مظاهری اومد مستقیم گفت، چیکار براش کردید که از بقیه هم انتظار دارید بگن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81273" target="_blank">📅 09:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81272">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrwPF17pGnR3N9tizj3tD5JiTXqOS8XGbTyQiUPgnz3OxKaFu6HPXTVdE-Y36XcKSQYWjJvtVGK0k1HMiov6i5kinVIFewqqAgOVGGdXmRBdOdj9uh_ZIpljvXbnwaPAsZCg_34ADwhdTMM_vUP1YgFSim7056i9BuAfmmMJaslrKT6QEPF4EvqLSX4h1X2QsPwtSNBfN3S82z-tJYF93cyaB83nCqzferuB1VQDqcmjIv9znEUzXGOe71m1PglYFkwdmAT57O5--TUPfw-95DG875AcLx8DKJcLJDZj_sasJOo42FD7LP1LW6tuC8jnze9bCct7gUA_pFtIQh_zSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81272" target="_blank">📅 09:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81271">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فیتای ویناک و هیپهاپولوژیست از سپاتیفای پاک شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81271" target="_blank">📅 07:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81270">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eZRyF5-qkGDtr8MNlfCYrfpNEbbd0nE2dRs6wth5pA5vFcO5FbxPoIuXhT8xbjKksOwsCt8qkzSibePBsUFenWGIU3M7akQFVy8m5eljzS8GCcdzbq_0c3mOEVIHCb0mXaPbm4H-1vwXdM6ppjxvFA28BnzWgsOQttZiyCzfYWDmp7NMK8gQ1Dm02vkftmk_riTt_w3xbdhisrhkrN0STXMkEf2WK21FnaWV84QKU0EqD6e5aTnLfF9HXaok5feivXwkuMq9lxQNhIkeUTp5T-xjn7SQSHqx35mZ-14IJLrfZ-h6JLHjuTzYtKKQng0lmnCq_afcc-1THpVJIecNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جود هم پاخور بوده پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81270" target="_blank">📅 02:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81268">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایمان کیرم دهنت چرا کسی جز تو صدا نشنیده</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81268" target="_blank">📅 01:57 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81267">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زدنننننن</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81267" target="_blank">📅 01:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81266">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1-mbSKu9_kH0Z_Iprk7P1_75umFvX-kPF1KaOiFWcn5HGj__kSqPqy3kGsxL9v3r0Rzfd6En04jsvpvq3m-BS8l-NirfZm-IJ6hZW7BR7-vHqlaRyda5fHrM4Zg9tyClRJAux95ViVBACkTDHx-xXZ-LZKHHb0RDht9amFxZsdXljGTltFSjmg_66ZRyJ4tpdR_4BKxEcH-e7Hkd1NidO5ghsSFGFO-O0wl60vrVLLIbIUUREEidUOXjf1LS-rU2jXVd--OuY-_8-p2c0NjqxQanAdgkBfy-gWWJj5Z1C8bBIGvCmurNTDuWFc8p3eEM3f1YDBW83Mhp1hUz3yCSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی رپفارسی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81266" target="_blank">📅 01:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81265">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.  SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81265" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81264">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcewKkPofcdToIAmntXMeFRLmh0Vo97cC1AovclnOpP84aC6w7q_Zpja2UYJv-RN82XvKICNvHMQI6xBSMw_7c339eslhQNNdNotCGZ-3PnTtL8ywZVdCerUcXVIxqZ3DOEsfnd91d9P-pF0vwF2hVi50oz849VPmCufdQxlarB28SqVPi0T-OWDblXZtuRjeZGFIARHV63iKbuieQ9IjZMSezK9_ZDTUr533fNEUjSQnL9Wooqtb7D2V7PLTfi5Qay2QQeNHOKLNMwLc3YsAuCY2SF24kWb-eRFh_KtObB1f-NQNOtezmpQQeI2SB7-jXwIXW9tsxibML49EKgBzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام و شایان یو به نام "تقصیر منه" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81264" target="_blank">📅 00:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81263">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">طبق جنگ ۴۰ روزه امشب شدید میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81263" target="_blank">📅 23:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81262">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تموم شد، دیگه هیچوقت، هیچوقت نمیزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81262" target="_blank">📅 23:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81261">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">ترامپ در گفتگو با شبکه LCI فرانسه، درباره ایران:
به مامان توماج صالحی قسم این دفعه
این‌دفعه به شرافتم قسم بار آخره که به دیپلماسی فرصت می‌دم و اگه برا بار ۸۲۸۲۸۳۹۸ام، ۱۰۰ درصد از ۱۲ درصدِ نصف خواسته‌هام برآورده نشه یه جوری حمله می‌کنم که اصلا خیلی شدید و دروازه های جهنم و این داستانا قول می‌دم قول
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81261" target="_blank">📅 23:09 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81260">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هوف
کانال ۱۴ اسرائیل: ترامپ دستور توقف تمام حملات به ایران را تا اطلاع ثانوی صادر کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81260" target="_blank">📅 22:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81259">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b585792e34.mp4?token=RZiGqQ0g6Rj_qA85oSVs6XLgROH-DbHFwNyfRG8o-dRAiOQftZJokofMD3EUqrdVZv1K8ESiHAtYoOJjMKAiVMF2wOr8QNWIdlmj55RWbRwDr39VoY73z6Iv66V6J6LJ4wZ1arMbiWvAZ0UYV6mqMUW7LNcktlp4vNa0XJfjRpjDVhysgcfevdrp9iOl7U0y-0u5JrYURwJY_LLD78_aG0Nn8xI6NE122RSOCBwfmwvOlDIeX_K93KBoDHv0FQZu2hXrQl6rUmHR-MNsjk-TvKeI9GM4H_Me0sv54bjb55VmnDRC34KmideLXgET51DU9xWEI3zn69a0MIj-fDHpVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b585792e34.mp4?token=RZiGqQ0g6Rj_qA85oSVs6XLgROH-DbHFwNyfRG8o-dRAiOQftZJokofMD3EUqrdVZv1K8ESiHAtYoOJjMKAiVMF2wOr8QNWIdlmj55RWbRwDr39VoY73z6Iv66V6J6LJ4wZ1arMbiWvAZ0UYV6mqMUW7LNcktlp4vNa0XJfjRpjDVhysgcfevdrp9iOl7U0y-0u5JrYURwJY_LLD78_aG0Nn8xI6NE122RSOCBwfmwvOlDIeX_K93KBoDHv0FQZu2hXrQl6rUmHR-MNsjk-TvKeI9GM4H_Me0sv54bjb55VmnDRC34KmideLXgET51DU9xWEI3zn69a0MIj-fDHpVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم از مادر رپفارسی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81259" target="_blank">📅 22:27 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81258">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=HL19MeyVwxdGtyfJiqvxtc8UDEAo3U4ZhUbV6r5tkhN3slOpmTWn8KOIcfLDjHo4PUb0kHl7Rpm32BFIaB-xCJgwCC19VlmfdtVfVCc6BDbM-Ly7JfPdxpPxGzCNTjOstKTP_MFJ6F-1I5dDKkHhyPOEvB_Qe_zVdTkQIWh8pFocq7MPowYcMCvn7XZpbXM3kibFshj9Z0R94jV-QcHG09ZqSWb97CqDDx7wNhBKQIJ4c_UCF-wj5lOxGzy4x0gN3V4gjeFLDTsBHPnRRPYQlEpfljDG46nSsZZ6cVrO9ebW9nxqj88K7Mq7zLEEZPtwFu21Q3v9BrMYYBgNRlfzYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ff8068cd9.mp4?token=HL19MeyVwxdGtyfJiqvxtc8UDEAo3U4ZhUbV6r5tkhN3slOpmTWn8KOIcfLDjHo4PUb0kHl7Rpm32BFIaB-xCJgwCC19VlmfdtVfVCc6BDbM-Ly7JfPdxpPxGzCNTjOstKTP_MFJ6F-1I5dDKkHhyPOEvB_Qe_zVdTkQIWh8pFocq7MPowYcMCvn7XZpbXM3kibFshj9Z0R94jV-QcHG09ZqSWb97CqDDx7wNhBKQIJ4c_UCF-wj5lOxGzy4x0gN3V4gjeFLDTsBHPnRRPYQlEpfljDG46nSsZZ6cVrO9ebW9nxqj88K7Mq7zLEEZPtwFu21Q3v9BrMYYBgNRlfzYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس داوینچی درحال لذت بردن از مذاکره
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81258" target="_blank">📅 22:17 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81257">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0O0qghal86zqYxUNtqtQunBYv2E_lc7HXXM0pAnW0dH1ZCQ0LMQcXI1zVs28GiPU-aPyXeU0zEUeX4woHlgBNf3pMIUVFH6ygpi3RIrYFiZ3kzJ6XK5Ud9eAPVgaxV0NU7oXQ5UySR7iF5ZRTZgKLG8x3WR4FVhutqEFBC721AmajXJHSwECDhNRC0H8wApmxjyonXlEcB0Ym373humPfp5OxyHdeKEdG8NF1cQkmourd7_SDKrvfK4xRjk5qKaL4FmLGEBjwdOCr4z6XfS4PDL4xQTf6U0HIHgjA9VbFfZO6E3hzrqMBXmUHa7x6kLjB7slWcb_XB1pIx8muM2pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81257" target="_blank">📅 21:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81256">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CXwh6Pbqc37BzE-cE5-K8LLH34qjYbaWx_CL151Nu-rygkhnZXurXQidXhyhkAd-ophZbuT8a9C-8FmPftIRClnBRr139dM7HEXrGm5Hw45Wb-dTscQiEXKJy2g-CO9DRvuweu2RiyIibTVpBx4PYjebWFT72qGtIZauRHV9CAovAVD4qAlQ_us3ke8ngCoK9pgw51EZ9GenId0b3EPZowXzQ9GeK9iNHvL8OHgNuoifg9UoTEqGLcJzwsOKlsxYHCOa1rnXQEYzzJL9maiHbv9N5B7SE940cmqQJnTHNXAU4dnGCD7oZqYh4uTKnfm6-WjFU46auyJCythjt06F4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81256" target="_blank">📅 20:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81255">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید:
این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته که بگذره خواهیم دید چه خواهد شد.
#تاحدودی_بماند_به_یادگار
#تحلیل
#اکسپلور
#مراد_الله_ویسی
#خدابخشیان
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81255" target="_blank">📅 20:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81254">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K375AuzEZgmiS-df0b5rdIDH6stjIG09pdlmlC99HA96ugiMooHQpzm08M79C20Cm3-QdZjsXtz9vtL4CA_6I6o3XfDTFa4lcv480m6WmilItzAj4jfxKwc6l_srq6JGfJe2puy0CZ4ZOxTo42BwkWnG0zXDCh0e9Fc3NbECYIthI2stnEVWdIvwSNcTt3A1OfTfJeLrNqjdcCZSXMWU9VJOmRU4GXKo_XjucWn6ojcnBLJWO7JhVH8NDvHP6i9Fe513xmQC0mKFmbOeD3md4NREM4f7PY0I8a57ojaSxQAqAN_BaDVkXIYIFQcXqynHPtzcXlAFMOXRJ-GEYUGA_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید باشگاه فرهنگی ورزشی لیورپول :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81254" target="_blank">📅 19:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81253">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">قوه قضاییه اعلام کرد که ساعدی‌نیا حق باز کردن کافه نداره.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81253" target="_blank">📅 18:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81252">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kErL8nMWzeQ4IW-ER6vYzxUVreJ2VKXx9jG_WU3gH7R1IOonInNS0_4vy4UTFcIoXmDe7z5XOGE8OX5DUyXMJmgL21GFz8Ll7I-VqVGQ4jyMuN6U6Goxy8okcCwFen2lUTOqg-F44QmfSUDeZWzQETsTycs9Nrt63mPjfU60go6hWMl5lCxUqZiQV9yC1zSC7y_Efg7YcVy2XD9cQO2vd9upRyTCMs6eoTuJDdIGdGVSaT2gKYIjd03PVnAypFyarGxysj1RBxDWvE2o8Y6RSovYZQSffGwFIeDPJ3uGdpUXPgu69TczXNL0GKT_PvlqqoHhr-KC9DDLu40WsEwmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میدونستم اینو قبلا یه جایی دیدم.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81252" target="_blank">📅 18:46 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81250">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">خبرگزاری وای‌نت اسرائیل درمورد اینکه چرا دیشب نزدن و چه خواهد شد:
ترامپج می‌خواست خیلی عظیم و گسترده بزنه ها، ولی گفت یه فرصت دیگه به ایران میدم شاید دکتر عراقچی یه کاری کرد، پاکستان و قطر هم دارن تمام تلاششون رو می‌کنن.
ولی برای اسرائیل، این یک فرصت موقت برای ایران است که تغییری در ارزیابی کلی ایجاد نمی‌کند: توافق‌نامه آمریکا و ایران از بین رفته است و
احتمال دستیابی به یک توافق نهایی که در آن ایران تسلیم شود، صفر است
.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81250" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81246">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si6ScNBY9MGI1Wl8aa_z3tFoZ4n4xJ6l4YKkESA70BVbyf-4Hv2HipDm28UN5MVqLIFtaZRMPoDPB4_efH2MIlwBssVqu_xAX3ix0V79h735e_6-k7YKxul6XpwY_pyZ00BYR3425PrL4YtvqZjBYkOedVQkUwyNhfN2l6qGfDfOgGk2gQnIozPr56_-jhI4DLCZ70B2gUg_D1pBkjZHD65l1YBwj8Alu5x7gyrdeaK_g9wVGv8oLajMMVs_dxkg_J28Y2ttYDWePUUJtcR1qafyqREJi42WsxV7DSS6wpEW_G4CQ2kDaZSUwRndvzV3i-IW-s0Afl2xvvCVZ7eiww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدبخت مهدی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81246" target="_blank">📅 16:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیویورک پست:
آمریکا در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایرانه؛ «پیچیده‌ترین عملیات نظامی تاریخ»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81244" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81243">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">عباسدرمن: اگه وزیر نبودم میرفتم پشت لانچر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81243" target="_blank">📅 15:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81241">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxcmYZyOSe9HMcdNKCSfv3femqEdZtj7tXpfl1uaVdj8fnrnq0yHqvgLHUL0OAfZFr27RFdQeK6o1pe_l-fE4JHw5h8blRbitscx9lux23eFlnK5Do6x6em_HgFLSdJvvytYYHDPtcz4R0lGEvHPweQvpDmtwlnUIRyC5oN-a_jFwrQ-XRbOX0aY96bQVU0EcslE2TkL__FQh0KoyLO_MhfCBAi4-K1PPwmlW1Gga105T9716H_iHAp5g7gUyKOeheOFtGTsw8hATinvQpWMxLWPCUJtKBBQxlG1GsQOl8ewi09Nc1kmTOw6CY50nPY1rKQbRs_ozWd3EfLpza2IbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ما بزرگ شدیم علاقه به کودک ترند شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81241" target="_blank">📅 14:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81240">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLkhkvY3mav26vec77KsWGnRl3Z62n1Zy7V9M39jXO2ZbFxFIqe7CuaVzksYStWYs78hfgIM8efbGMZlPrMtzIvn6O-5Hatm1YKPx1BLR2EGkKkQYI8z3NFdy-S21DWGSnwo2kNaBk7T3hnjHCLqXlvYsgEDaYPNbj0ScsD8yFEn8_RNZiYeEtyIU6mFQR3XmoVM2KLIOKM7Jh3g-k9n6rpBd85nfKNLkNfz9DXZqK_pfmoKhdSXsR5vt1jXJJk09w6uq_S7968vMCjJn-fcAxsgDWytTbtgLd-RK8wbiNnxj-2qgKE4yjZzSHfnkpjLTXu6pFBExGv0sr7R4eJAlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81240" target="_blank">📅 14:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81239">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اوکراین چنتا کشتی روسی که محموله های نظامی ایران رو حمل میکردن تو دریای خزر زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81239" target="_blank">📅 13:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81238">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شهریاری، گوینده جمله مگه تنگه ارث مامانته:
متوهم ها باید قبول کنن‌ که آمریکا ابرقدرته و حریفش نمیشیم.
پ.ن: نه مشتی صبر کن رستاخیز بزنیم آمریکا این سری دیگه از خاورمیانه میره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81238" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81236">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJvRcu2TYya33Xf1iLerLL2-c51q6qTwkZ7C-Pv1KQUtMmLCb1djIFC5S0lGJTdeDKdDhToTYMcAIFPQEkPBmEA4FVbSpjZNqct9ifq2uL8Kz8K3ObCXKYh6pMBZ7NJWCzHE6DKNpkLtw55t8uAmpotK1RFKsfWoCUBsrCYpgudweSgn_d-XR4VgyJiGbht3Cd7gksqLeV7rkZ79KfUKWZYS95etRLMWchIAdS9Xc-bamnnXn7TKYgwWRn1JSR8VdQ6iD5FqqlB6YcvDmDAezgJu1eCrVyk5Mhp05V04WLwgfaOdqetuBJDK9t7NVfpTE9rcq8KyMiJNv_X8k9BE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YnwPSi5kFO1QwmGcO1OFvIbdxEhJvpztL_IE5aZc7ttlq7EqyqupGp9VNy4R-fGWJbpPM_liowWAyeGXHI4a9P79ZNUA7CVssr0gEf_k-plcASH3ytTY4ysDG8IbzruXNUEYQ29SxZiNrjbK3pFjD0VU5Hn2oho2H-Mrjl5jn9HReMESSiX876a_s0pZbiAteZIAANKIBkWC3TsLZizwICFAY0VVvd8b94_jQuNB9Gd80t37l9xVaoWKbnlXYGr9vXvF6a6Rmgi-w7u64QP5ByVQMSkWbHeZtaTl6gBsLeJ6yzWZeIlQ9E34jJWtyERjmQa4pBZ-j4eAECa0z_Fvzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اسب که فقط ۵۶ سانت قدشه رکورد کوچیک ترین اسب دنیارو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81236" target="_blank">📅 13:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81235">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">هوا گرمه کصشر نگید</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81235" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81234">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
ترامپ: رسانه ها به دستاوردهای فوق العاده من توجه نمیکنن. من رهبر ایران که یه آدم قدرتمند بود و همه ازش میترسیدن رو کشتم و الان یه دیکتاتور همـجنسگرا شده رهبرشون. اینکه یه قوی رو کشتم و جاش یه همجـنسگرا گذاشتم دستاورد نیست؟!  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81234" target="_blank">📅 11:38 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
