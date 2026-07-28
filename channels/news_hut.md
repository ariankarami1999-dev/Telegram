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
<img src="https://cdn4.telesco.pe/file/O4y7_nVToHYxusaREwx8d8sM7w88xMfGmuipw6sHA4rsD13pkL1H8wz0s-2IEDirmsw4oNLAfBGEm5BxhFL8ArH7jiSRawffylSnKV7F4z885ms-dDmPB5VKZW2TGRlKC7P6W0VhhYhb-fPK4z9Jq2QVGGa0DC0w0iz6oq-rBVIG_5m7R_GrRgSNb3Nm9mhWSmvRZMvJIf6HEJLi20OUMYMiPhVWzQu8894Q9SOLda0nnQftnrMuxEk6AxuspOZm5jgfOCUFWK9Vg9hKz0pm_qF_u8ou-B3rT6DRadscfnnh1aC1OEas5PBmvA3tQr5jaXcH9vrbgLh6pump7ftLjg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 145K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 11:27:23</div>
<hr>

<div class="tg-post" id="msg-69105">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0eb0677cd.mp4?token=NZeI9DEaMOiYWw7gxG6J23elBWvVQym3sfRoJErBdwFyinHkJiEtzbEzxoFL9h-fuRgTDqnfqHJ8_m1_jpG0IpJQuP9yOvNtxdJ70IW6gMK--GULmHhM_tXPgzFkzdIZaIZ95qtaHRmiAsOr_-Q0p8rVFpPc3qi84npoW44anizBN0mKEpVC-UbHOg_DhDUHI0iTu4PNBs6Q4L2MiTcBKfs3yIvD_Eh3qX5wJKLaWUkSVrOlHgNA35Vykg7Wkb9NC2aNZMX3iXvcPal1z5Lb2wTcRh1R4P1J5HFX917eSoJ0HZud4LMJr1gSvlT1r_ZKkPVMQ3M0kmSSDjTGuTbkVzC-wTS88jwIVKmcTJBDwAU-OgFX22Yr24GjijZGdXAnSiLzBOJtDVjd0DrwZ5OflT6faB2wXuAcnP6urbOmhieDtIO_EY4RcLilnhzcCiHy57YJAnJXe3aMOAyUXtGca0oE3GdJLgEpWwaRY95souyVaGjds9S5C0EcHEQTLhwg2zan89yWBTML_fcj_tVUgG8AyT2_NMY6y1MOs0nUVZeXdeO0-rdkU7o5EFBhNf4xHFJuP-ox7zNKQsLzcJjFjmxFWnjQn6bL7FZWXFxmhVQuK7nHuOyTPHOckY1NGwSCexy-kr6K6w-51qgfxUn3kUUlBzlWlD5_fTxV7U4ACrk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تسنیم این فیلمو راجب
ملانیا زن ترامپ
منتشر کرده تا اگه کسی قصد ترورش رو داشت از این اطلاعات استفاده کنه
🙂
@News_Hut</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/news_hut/69105" target="_blank">📅 11:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69104">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=nPUhrXPfckz-vf3zt-gtGf2M42Kwfpe0O5o87D6lWSNfKbHB-gRDOxDtffQEEh_ThVfvJ6uqdxGHdTQ-vyKirW5h319Wd9pRm8_DDrsN6Q5XqLFI9FmzAoiNfO6NFGYyoMi1IQc96Ksj7IPfcxNA_iymFu11AVAWgqj1cvhW2LSEPKnL-0FIWMLrK-YiMQTk2InfdwIiJddZQ6lJA5ytMk02p8dKImL_Pmndj14Kf24PUM7Ff4hQGX7qrZ0Gr76VqReSjjSQ61nE_R1EPh6Om6p9YhXmEqAsnmjvqSBe2DwPW6GpJK39M8DssU-RMkrU19YJyFCkM6B8VNcj1_IbVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76bcf42cd4.mp4?token=nPUhrXPfckz-vf3zt-gtGf2M42Kwfpe0O5o87D6lWSNfKbHB-gRDOxDtffQEEh_ThVfvJ6uqdxGHdTQ-vyKirW5h319Wd9pRm8_DDrsN6Q5XqLFI9FmzAoiNfO6NFGYyoMi1IQc96Ksj7IPfcxNA_iymFu11AVAWgqj1cvhW2LSEPKnL-0FIWMLrK-YiMQTk2InfdwIiJddZQ6lJA5ytMk02p8dKImL_Pmndj14Kf24PUM7Ff4hQGX7qrZ0Gr76VqReSjjSQ61nE_R1EPh6Om6p9YhXmEqAsnmjvqSBe2DwPW6GpJK39M8DssU-RMkrU19YJyFCkM6B8VNcj1_IbVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
مجری :
کراش فوتبالی تو دوران نوجوونی داشتی؟
⏺
غزاله اکرمی، بازیگر :
آره ، غلامرضا عنایتی
خیلی زیاد دوستش داشتم ، نمی‌دونم واقعا چرا به شدت روش کراش بودم!
@News_Hut</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/news_hut/69104" target="_blank">📅 10:30 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69103">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vUV1bjPxGEc9pqIGg-5elzi4ghvuC9FDziNz_MTfWHN3qEe74xZNyCyFaNKzjo30XwRy8f4vxOUqC_T7eeQhJxdjFAi1BCV1yRVo4jwS4Eh2m_P5OIwDsobrF_Wv3IsGpwKZutPvNRNSKBZTPImopzi8XRnKaI21jfWnPIYJFVwvPxNUJdp69UXhFz3LmgA-R0QLbaxnRUKTJ7JJiSiKPU_ZbO21PMaGHjge86Zb-ZUGtLATN5BGenvwdWo9touG_YYTqvWWRTMGmAEYrQ-fDqCgztlQciMhIQd8yqrgkJTYxgjRiolydRvh4NjMYalCKWGwtqppEqro1_oC44fgdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به کشاورز زمین داد، چریک شد!
به زن‌ هویت داد، آنارشیست شد!
به کارگر سهام داد، کمونیست شد!
به هنرمند اعتبار داد، توده‌ای شد!
به مسلمان حرمت داد، تروریست شد!
به دانشجو بورسیه داد، مارکسیست شد!
به اقلیت حقوق برابر داد، جدایی‌طلب شد!
@News_Hut</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/news_hut/69103" target="_blank">📅 10:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69102">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=g6WXummbxzskFPSK935Yqr6tCHVedBxVdeM53MqQeoSFuOJFigbjqwBKyCUZYxMaRfWuGEmdNKpWXBVoDct1eDVX9jQRJ2JqnUlcQtzSpZMp_YJNjlclBs0i7m1fr955Hv_cBci0hh3xgVWvRK1OMxrBNqQFfAgYBwIUv1imTaCytRMZJfVhpucBrbaqjYGgccBZNli24rehVbU4vsqv4QXbZJMrDedGNfpQQlCHJJM8XbWTZsq3o4zeSzKjsCuT9Yg8pcQiOGNnFz3JBrkHH1aOXIFoCIHiN2vatNJ3ZeMD_u-rtz39wohzsyUt4YSZzT0Vv3a6l89f554LUwM63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88a652ec4.mp4?token=g6WXummbxzskFPSK935Yqr6tCHVedBxVdeM53MqQeoSFuOJFigbjqwBKyCUZYxMaRfWuGEmdNKpWXBVoDct1eDVX9jQRJ2JqnUlcQtzSpZMp_YJNjlclBs0i7m1fr955Hv_cBci0hh3xgVWvRK1OMxrBNqQFfAgYBwIUv1imTaCytRMZJfVhpucBrbaqjYGgccBZNli24rehVbU4vsqv4QXbZJMrDedGNfpQQlCHJJM8XbWTZsq3o4zeSzKjsCuT9Yg8pcQiOGNnFz3JBrkHH1aOXIFoCIHiN2vatNJ3ZeMD_u-rtz39wohzsyUt4YSZzT0Vv3a6l89f554LUwM63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏸
ارزیابی رابرت پپ از سناریوی ورود نیروهای تفنگدار دریایی (Marines) به سواحل جنوبی برای تصرف محدود نقاط بنادر و عواقب آن.
@News_Hut</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/69102" target="_blank">📅 09:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69099">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jdsbe81osTFb4pOrF4_Uo6icxw-Q09sFiWXlnPoajV_h0TDHeDQNoX5k8rZPDljX5bDu9Qy2--x0RoxUVlJULqhSzd54MhIJvcYKp2biD8L7n6XnvAEXpTKA--U3p8IgT2xRAFNO9pMEOUXPbmLjb42yJy1D_jG8AmzdO9TRxk6S4JH3yBC3ptHRjvnj1HKk-FZBoST-yVCC37fxCKefLxSumde51pChikq97NSTRkx7V2IEcC49bOswwRjskatp5LNEV_U8Uhh02wKywJ0Yl5xaY-yM3FQ10KVZ0fp235DRAhXCgaQahwf4Yf-mjtl_yrd-JZhwhBE8S1WVEUxFag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nuTsAa_5IKnvSpKWmhS3iYcWs6W8Nxk-Zm2IBu6rX6lPA0ElL-ra_APo9C44m75YTdxZUv_Lge1UwKVsCmshMSam7spnmdBlv4-jZw6YMI2qeFU5T-PfF1bI8bHniqC_HX4YprSbNn9RN3hxHd1KSNjS4wExIga36bwrDFIkWnfcGNrU5k65pkh4SSas3qtIDN_bMVa6oDkx1lvyYeJkGi-U-mpziCium9sLiqmy2Pzvk5oIrXG00giCQnDqxpR_v6OdcMSTFAb63ZQjXCVspRvLNNw8bo_iaqEGJ-qgTsqRrA0PJ-wa3FBUEimaBKJhIkUygCbNk4DaUA1pd-aNcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یادتان گرامی جانفدایان میهن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/69099" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69098">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#رسمی؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.  @HutNewsPlus</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/69098" target="_blank">📅 05:56 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69097">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">#رسمی
؛ جمهوری اسلامی دقایقی پیش، پس از اذان صبح، ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری را اعدام کرد.
@HutNewsPlus</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/69097" target="_blank">📅 05:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69096">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">متاسفم برا یه عده که ذره‌ای شعور ندارن و چند ساعته مدام در حال پخش انواع فیک نیوز هستند، بهتون کاپ طلا می‌دن که خبریو زودتر منتشر کنید؟!
#hjAly‌</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/69096" target="_blank">📅 05:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69095">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=ogt0YlaIZYKOiSgZnvcR5N8kChf2NkRD_4sCSGM5fh15APFfjByoGRp_1H8tmurXgG-crAwT_1KZftZcOpdw3KsnlhN4NsF7Y19nETOl7jfBD3ztLjIBlS59Jgn6vU250gbyQxqiElvtWENH2dVwsxNtsPX2XAnXRg2kJTqzZgmPUC-YH6yv6m2Md7IAF8swfYuHDkHlUSz9-2hhZWBbFUVg87VjBKQ7Q6DORCjzW28wCqiCO1UcPIjDUI-S-fd825_n31ershEB5ssv9jbA6Qic1Mq_NMc9AbB4tM3DphX8pi4_AQae4cwQicD9ow8htswBZ5bZLXyzn_GoA_UHzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f40f91b5.mp4?token=ogt0YlaIZYKOiSgZnvcR5N8kChf2NkRD_4sCSGM5fh15APFfjByoGRp_1H8tmurXgG-crAwT_1KZftZcOpdw3KsnlhN4NsF7Y19nETOl7jfBD3ztLjIBlS59Jgn6vU250gbyQxqiElvtWENH2dVwsxNtsPX2XAnXRg2kJTqzZgmPUC-YH6yv6m2Md7IAF8swfYuHDkHlUSz9-2hhZWBbFUVg87VjBKQ7Q6DORCjzW28wCqiCO1UcPIjDUI-S-fd825_n31ershEB5ssv9jbA6Qic1Mq_NMc9AbB4tM3DphX8pi4_AQae4cwQicD9ow8htswBZ5bZLXyzn_GoA_UHzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مردم دارن شعار سر میدن
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/69095" target="_blank">📅 04:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69094">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!  @News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/69094" target="_blank">📅 04:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69093">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">دفتر رضا پهلوی از جامعه جهانی خواسته هرچه زودتر برای جلوگیری از اعدام معترضان در اصفهان وارد عمل بشن!
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69093" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69092">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">لحظه‌ی اذان صبح و آماده‌سازیِ شرایط اعدام، در میدان علیخانی اصفهان</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/69092" target="_blank">📅 04:06 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69091">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69091" target="_blank">📅 03:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69090">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">باز می‌گن چرا مردم ایران دین‌زده شدن، شما یه نگا به کشورای عربی بندازین، مردم، حاکمانشون رو می‌پرستن، بعد این شیعه های مفتخورِ بی‌همه‌چیزِ خرافاتی، جوونای مملکت رو دارن تو ملا عام اعدام می‌کنند به بهانه ها و دروغ های مختلف، همونطور که ۱۴۰۰ ساله چیزی بجز دروغ و خرافات ندارن به مردم بگن
#hjAly‌</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/69090" target="_blank">📅 03:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69089">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/780d746559.mp4?token=vTxt-jX5uNMRWlgvA6BN2Nvy8G0nSWvUL9H84ZS3ecPaF9bNp0VKmqfR4NyeoMor-83xAUyLbl2QBN1QJrTswQpM-U0m0UD4U6JYO0-dmR9uFisHILMGOByPj3HkJzH0_hXo3yjml9i4XSo-j04wlzn1c-zJjqRJ8EHkmvaLT8sreV9S6EUqtG9TJPXOVDurALpQjLNHzDm1bi3KgfK0anlSGXdGT6n5cHP-ZDq64gwe2Tj1HazVZaoy20x-uKgNsJE3_YZTJV_EkCaDnAnaY5leyPL1qJQpejP_gPR_OJTvPXHNQ--8u31u8041-KkK-Kwp3g4bENGFFVvLQxj4mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/780d746559.mp4?token=vTxt-jX5uNMRWlgvA6BN2Nvy8G0nSWvUL9H84ZS3ecPaF9bNp0VKmqfR4NyeoMor-83xAUyLbl2QBN1QJrTswQpM-U0m0UD4U6JYO0-dmR9uFisHILMGOByPj3HkJzH0_hXo3yjml9i4XSo-j04wlzn1c-zJjqRJ8EHkmvaLT8sreV9S6EUqtG9TJPXOVDurALpQjLNHzDm1bi3KgfK0anlSGXdGT6n5cHP-ZDq64gwe2Tj1HazVZaoy20x-uKgNsJE3_YZTJV_EkCaDnAnaY5leyPL1qJQpejP_gPR_OJTvPXHNQ--8u31u8041-KkK-Kwp3g4bENGFFVvLQxj4mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69089" target="_blank">📅 02:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69084">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlqrKuZmVX9yitzN7jA9vC4oIecmreKk8purk10CfNZQ1kZ0XgID6iUMHofN9f1aR3XwfNrnb4AWrFuwQgcLtnu5F4bnvE9klPXHCYuGukPgkZEzAD9QVPG9JF6FAEnFGu1pXrXtmVVodHu3Y4verYCnW6KH3EPL9_GBEXZmkFGEW7yhdisomZDpGl9MTaeBmFZoxpl6SvMkxmNqNIqsSFa6UbDndBDLOun4d-WJUoDM2cUaYYYHk6IsrC1SiXiPzKKl6_CfM6PbuBcb8pgcmaspoIt_FzCSKi6YvpGM2zNZb2lOuBeWmGnOMylM_VlDH9CipKF1BN0XaJS_FetPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IjnRbPL0gKmeSVRIQ55ydtleZndlWRy6dSheiLBi0Kqnjv2boqwUZAUdLZlQJa_SMvpSJMmN4X-_ehHCzJn3Gdg4hUwXmmD5lFU9I-bGq9_5nApDjfMCYdl1HSVkaPFIn8RKVhx2nIwmg74R_l7ThqjFNHIlLkAboBgd1yoGWvtzEZoiU7PCTzVpBOAnfESsBSNCeud_mTlKBfosvYCYOVAy5dvziRDsXz8P3akoSaz0RoffxTblXc-RDdYr1j3XE5NHgGUFUm9yH887GbS1KXqga1877cLhP86AtaT64LeXdR97or857RZn6s7inMoeWEBmKO4b3KZodGa49_jLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H-aIQnU62DOAuH9pBxeg9zaDhtoYXSj-Zfe61HSKQiWCI1RgKvV_v3G3k0Xi1QKWrg1e_jiwJMg8zJjg_-NeP6k8xpEcp6Is8jZmXKiJNoQs-3XRjB0GhkNEabhvztlXrWwmtTqNsN_uerNpCNkjbnMwBfwlOwwXuRPXKaI3KWX-727AOA0uawy9vXaXirvqAAnVccOPzGgOO01maqRqWQ0374Uurr5nfAWaFSBgPGY3mRP0Zpy-GYZlmNwd_6UmY_2VVt0CWY_3FT4qpzFrCgvhWf76jWbmRWQLNacZQZjvPFpNr7q3UNbldo6k-VbD7ImdS1KSKfvbTysma40BUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=e40-PYmRHc-UiBy_VT5pi4rVjcvR4wasmJD2iemt7q6RNXyOAS9iBamOnCGbxvuLzP4iKV5RLkhWfNVWq-B_EXPduIeksdvKJFs5OBPoRaZB07nTaBZIwrGtpjrCwluhXwab54PWWRS6PUGG9yoAgjtLsP5edUefJa2gqy2h8Yv-PgGqgaUj9bI3qjv3l00znZAvr_Ih6q33F-yjieEZxBH9LFaDjz9dTrN9IZJ4aHORhiBeOhzikixWUnShABCRg6SOLkzpsTvq_Y7vRetinloKbNLOoVuFduY_TfBN6N30XBnbWAtmCF11vNhmtFwdgYUtQ_NZXkJ10f9om7TgGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/491b6de7b5.mp4?token=e40-PYmRHc-UiBy_VT5pi4rVjcvR4wasmJD2iemt7q6RNXyOAS9iBamOnCGbxvuLzP4iKV5RLkhWfNVWq-B_EXPduIeksdvKJFs5OBPoRaZB07nTaBZIwrGtpjrCwluhXwab54PWWRS6PUGG9yoAgjtLsP5edUefJa2gqy2h8Yv-PgGqgaUj9bI3qjv3l00znZAvr_Ih6q33F-yjieEZxBH9LFaDjz9dTrN9IZJ4aHORhiBeOhzikixWUnShABCRg6SOLkzpsTvq_Y7vRetinloKbNLOoVuFduY_TfBN6N30XBnbWAtmCF11vNhmtFwdgYUtQ_NZXkJ10f9om7TgGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بامداد سه‌شنبه؛ تصاویر از وضعیت میدان علیخانی اصفهان
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/69084" target="_blank">📅 02:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69083">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=l_K9Oi3Hxcaw7YKxOrpAKfovJ2ZUB3WN6CGaIF7YdtBQyvFrnF4ErAelpPjUlYnrqGkSjju04fA4oZiurbRgO3WjwmvJMmA8E0YZ42Fr575FCYGGvs8TJJfhmotmf_ucmB_plTQgz2kfjiIBX0xQRWN05-N3WC70-V7FHSZg3B-rTfzazvFT5i7927mAV9quRVY8J4RWrn54zx6mpTp9ekbpP74KciZwZzbxgYN9SYe9lrYMQZBcO0-OWlELhEQrufGAll_u7c58-W1pdqz6iTd480GlQh_VBYZ-3hy25ef8uUJ_bywKcF6Fon0EJjdOxiTLOqLRwOG1INryxmQD3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7f398a76c.mp4?token=l_K9Oi3Hxcaw7YKxOrpAKfovJ2ZUB3WN6CGaIF7YdtBQyvFrnF4ErAelpPjUlYnrqGkSjju04fA4oZiurbRgO3WjwmvJMmA8E0YZ42Fr575FCYGGvs8TJJfhmotmf_ucmB_plTQgz2kfjiIBX0xQRWN05-N3WC70-V7FHSZg3B-rTfzazvFT5i7927mAV9quRVY8J4RWrn54zx6mpTp9ekbpP74KciZwZzbxgYN9SYe9lrYMQZBcO0-OWlELhEQrufGAll_u7c58-W1pdqz6iTd480GlQh_VBYZ-3hy25ef8uUJ_bywKcF6Fon0EJjdOxiTLOqLRwOG1INryxmQD3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داربست رو نصب کردن و جرثقیل هم آوردن و متاسفانه با اذان صبح، این جوونا اعدام میشن
🖤
طبق گزارش شما مردم وقتی میرن میدون علیخانی و می بینن مامورا اسلحه دارن، جرعت نمی کنن کاری کنن و فقط نگاه میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69083" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69082">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GC1Xw8Cj2OJA7MMbnJFL0jSiaa4qnMzKfdeQA0Fb1NZX6hI8x-fDteF_0qIxrtwilI-6v-BserQEMZ6YZuNlPp9ATqO4-b0Gvy3_ChAu6fYMe22J1As_2Eg3QrZOaNQuWJI8pG8RGmfg9l5moDmkSEPhMW97G20N12gp4VyDyc0pvTsA4bZNdqZ3MzvmycPCBkzegE99j2zCc8KzuSvSywHEXBmmxm85r1eb1J1sprkLdYeRcKNPzUn0xQ4W16I2uZNd7S2PB2g6y-S3U6QvBbb0V54YnJMgvkhIkpyZUirwGuiADEIckvb4amiuEHRKT_AiHio351fm5Ng44AeNZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316f36114d.mp4?token=GC1Xw8Cj2OJA7MMbnJFL0jSiaa4qnMzKfdeQA0Fb1NZX6hI8x-fDteF_0qIxrtwilI-6v-BserQEMZ6YZuNlPp9ATqO4-b0Gvy3_ChAu6fYMe22J1As_2Eg3QrZOaNQuWJI8pG8RGmfg9l5moDmkSEPhMW97G20N12gp4VyDyc0pvTsA4bZNdqZ3MzvmycPCBkzegE99j2zCc8KzuSvSywHEXBmmxm85r1eb1J1sprkLdYeRcKNPzUn0xQ4W16I2uZNd7S2PB2g6y-S3U6QvBbb0V54YnJMgvkhIkpyZUirwGuiADEIckvb4amiuEHRKT_AiHio351fm5Ng44AeNZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از آمار تا پیش‌بینی
https://t.me/+L5I8ulM6jEc2YmE0</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/69082" target="_blank">📅 01:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69081">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KhBuQGyyPr6eyWJcmt_U5zLfLqYKjafqXFgIH6Buz0TMYOC3AwGpZji_GnTMXCtf3jqBjHh37TDJ6N4b225ehR8aIBQ2iB4uxBiT1lmbsEEG6j5NhHl-cFYk1xLtlSFH4_Crds3SgkJk35__b-vOjB-27rzQYa3UQ0qGigK_IV40EBcyyhdLVEEdRr0CuAHfX2SNyrI1u0gb7d10HXooAwq4o048XQcWZPzttU2I-Dp4ETf4w2ml6vD7th2kBzpcVCg-NGbpvoKMUznmE06ppypFnjj3pprRRoammZvU49kIu81fe6_df5SkqeUh3WaxiC7iwxziXg4YK2TE36Q-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر نصب شده توی میدان علیخانی اصفهان:
«هیچ جرمی از نگاه قانون پنهان نمیمونه، دیر یا زود عدالت اجرا میشه»
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/69081" target="_blank">📅 01:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69079">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sSiitJHnnsizCihsCX1SA-2B_HL1Fj8rL9cOJbn8268E9xV3C10Kuqv5c9iZ-Gcd12uxFML1J_BYsoFFQRrp3utI38C70hslJ8SM7ITTH_wSnNwHWP8PvcpgrpgfIeXqk41WTttbYogGqO5lza6qET2-EP67OnS4QrxWf6sbtinWZh-p-I-ozYVMGynbjSxX1BwKrv_R1iiissgrhZbsIckRmB6kO8tOUdeQ1xp3XRvq0_MFO3ipBBFLMPojYkFOETFuwzWO39cPMhpYNtNCV5-DGWt4m6MIFokhhzO9X1omUr9W5P9mI913n-QxFaevE70YmXzoDZ8S8Bsza0p_ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DbA_XbCnOEGyMVzXmEvO36VBUzs5nB4B5bTQDw4QjiBXusKM_PDE78X5JOZINGZvwkYiwUHbYloSpa52KKpA208NlmwSpuhaXd-EMmcA86xJekr9QgN0l7CSFCRXXIPLbeMI1ZO_aJOvsKqjW88Pl1vKqFTycCBfqvhYRfqkGKeOmlMLbvZ8Qo8AvGZR5XftpOUsCNQrAWBruA6Q4VLXfl7AqALKX91ZqCmKUjOH0oG-hT_USur78dd8_A83B3rnfm94uq96DYrNG35GI484diGpmP47ByKT_ZRCtBDdL_0glg47jEuuUUfi3V5JKxh-Yypyi8PhJHwPg0RID7svtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گزارش ها
توی میدان علیخانی اصفهان داربست نصب کردن و جو به شدت امنیتی شده؛
طبق گزارشات ابوالفضل سپاهی، علیرضا سپاهی و امیرحسین صفری از معترضان دی‌ماه و پرونده میدان علیخانی اصفهان به انفرادی منتقل شدن و قراره توی ملاعام اعدام بشن!
طبق گزارش ها این سه عزیز آخرین دیدارشون رو با خونواده هاشون داشتن
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69079" target="_blank">📅 01:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69078">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=e35AWVXQdPdGK00CJxmkPwkL2NOLYtqDnJSS0mrwC6jje9OT5wDOqeyn3zx3-B3PqeKVjN1-EL-abBZ_APT-7ZWNM1hAI6NXCNtnp8fmGerIfzOrDgeATuaNkKGal0W4fRqqABhaQTFhaV6qjYIDRphDO_3oZmntJV4DCAN6n8QuQ9WA38WEgQybFLKxxWIxkQf3CRSgWQGhF-PDfMRyUdc26-bo6Dp-4pRF7yswjvPtkF9iCH9Af5yYnctE2VN1cvqXNC-zgyrDnIIQ6YgGp8fFrpCcArpI3mwsHEjYqsF6BzMSxX-2cjlF9n0ZT2G1Th6QJtcKn6kS4tq945yaaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3738c7aef1.mp4?token=e35AWVXQdPdGK00CJxmkPwkL2NOLYtqDnJSS0mrwC6jje9OT5wDOqeyn3zx3-B3PqeKVjN1-EL-abBZ_APT-7ZWNM1hAI6NXCNtnp8fmGerIfzOrDgeATuaNkKGal0W4fRqqABhaQTFhaV6qjYIDRphDO_3oZmntJV4DCAN6n8QuQ9WA38WEgQybFLKxxWIxkQf3CRSgWQGhF-PDfMRyUdc26-bo6Dp-4pRF7yswjvPtkF9iCH9Af5yYnctE2VN1cvqXNC-zgyrDnIIQ6YgGp8fFrpCcArpI3mwsHEjYqsF6BzMSxX-2cjlF9n0ZT2G1Th6QJtcKn6kS4tq945yaaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
همان اتفاقی که در ونزوئلا رخ داد، در ایران هم در حال وقوع است.
مردم فقط آن را نمی‌بینند.
نمی‌توانی به آن‌ها رشوه بدهی؛ باید شکستشان بدهی. و ما داریم حسابی آن‌ها را درهم می‌کوبیم.
مذاکرات دوستانه‌ای در جریان است. ایران می‌گوید: «خواهش می‌کنم، خواهش می‌کنم، محاصره‌ای در کار نباشد.»
سوخت برای مدتی پایین آمد. بعد، آن‌ها درست رفتار نکردند و من مجبور شدم برگردم. حالا دوباره دارند درست رفتار می‌کنند.
هرگاه کسی جلو آمد و پرسید: «چرا داریم این کار را می‌کنیم؟» فقط بگویید: «چون نمی‌توانیم اجازه دهیم ایران به سلاح هسته‌ای دست یابد.» خیلی ساده است. همین و بس؛ دیگر نیازی نیست چیزی بگویید.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69078" target="_blank">📅 00:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69076">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWvvY0owfPbWxb7l8STSmAKde0mo96ElwXhdGs2av4symFPONA13GMwitdD6t3afXP4cilzOMqHUjQEhVgqE3jshEeNFSUe17q_SOV97HcWJaIJ3NyJKKszDOr7dAtr7plAGVkMnN-qhQHPF7k3Mi20NLNPcMdbgdAnPBZ57q1bca02EV7xb5azMDVXI3RkKJGsyjtUTq6mXs5BF5aV5MBw5Wk2lxwHfCHuzIJJKK2fR9pMjpgVfjAIbV7lnI9fxH6uYs0H7hKizFhRRQBnwcoUwUFzipDisTVZNIwwUGGyHxY22yNlP0Zazc-KsCdPdDcsq3GYeLV5WBqRSPQcYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
کانال 12 اسرائیل: دونالد ترامپ، رئیس‌جمهور آمریکا، روز دوشنبه در مصاحبه‌ای با شبکه ۱۲ اعلام کرد که تصمیم گرفته است حملات آمریکا علیه ایران را به تعویق بیندازد تا فرصتی دوباره برای مذاکره فراهم شود؛ با این حال تأکید کرد که در صورت شکست تلاش‌های دیپلماتیک، ممکن است دستور انجام اقدام نظامی شدیدتری را صادر کند.
- ترامپ در این مصاحبه گفت که ایالات متحده در حال انجام «مذاکراتی بسیار عمیق با ایران» است.
- ترامپ افزود: «اگر این مذاکرات به نتیجه نرسد، ما به اقدام نظامی قاطع بازخواهیم گشت.»
- رئیس‌جمهور توضیح داد که با درخواست میانجی‌هایی که از او خواسته بودند فرصتی برای مذاکره قائل شود، موافقت کرده است.
- وقتی از او پرسیده شد که تا چه مدت حاضر است به تلاش‌های دیپلماتیک فرصت دهد، پاسخ داد: «مدت زیادی نه. یا کارها سریع پیش می‌رود، یا اصلاً اتفاقی نخواهد افتاد.»
- ترامپ گفت که روز جمعه تصمیم به تعویق حملات گرفته است، زیرا کشورهایی که میان ایالات متحده و ایران قرار دارند و همچنین سایر کشورهای خاورمیانه، از او خواسته بودند فرصت دیگری برای مذاکره بدهد. (این کشورها و افراد شامل عمان، قطر، پاکستان، مصر و همچنین نمایندگان ترامپ، استیو ویتکاف و جرد کوشنر بودند.)
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69076" target="_blank">📅 23:35 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69075">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
قرارگاه مرکزی خاتم‌الانبیا:
آمریکا در تداوم شرارت و ناامنی در منطقه و به دنبال اجرای محاصره غیرقانونی دریایی ایران، طی سه روز گذشته اقدام به تهدید شناورها و کشتی های تجاری و نفتکش ایران در آب های ساحلی و سرزمینی کشور ما نموده است.
هشدار می‌دهیم این اقدام آمریکا به منزله توسعه جنگ در منطقه تلقی می گردد و همانطور که نیروهای مسلح جمهوری اسلامی ایران در میدان عمل ثابت نمودند هرگونه تهدید و شرارت ارتش تروریست آن کشور را بی پاسخ نمی گذارند و با آن برخورد خواهند نمود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69075" target="_blank">📅 22:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69074">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=Myd03zLlAHndm4fO9c_r1Dh4GmbcKZ7KYIeRHkNxnRma0JGU67kwfT6rJVITacTj0OZlsKub5ooanTwdqqQF9BCFTNarTjVJgO-EwdKGhMgYwMVcKdBuHdaztA1mANn0uIeYlSBOOKRXHBCPc6UR8_HrMwbqeBd9PwkJSzLTK1lv9Ols9LMnDi0uf3sC0T7BMyKTo4h86WJgKAWNYgyQwjGQVadKtr19PV4sNsoNqOoa9VVPTB9JEXxS7NH_d38dccMcZbPd7vIzq1MsSmGcsHhLnWKxZ_7NXLCP8q3XK1mnnI3531EpVIIoo7uXWVVm8eeTStYXsb79qR4dMk1l8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b46871a0cc.mp4?token=Myd03zLlAHndm4fO9c_r1Dh4GmbcKZ7KYIeRHkNxnRma0JGU67kwfT6rJVITacTj0OZlsKub5ooanTwdqqQF9BCFTNarTjVJgO-EwdKGhMgYwMVcKdBuHdaztA1mANn0uIeYlSBOOKRXHBCPc6UR8_HrMwbqeBd9PwkJSzLTK1lv9Ols9LMnDi0uf3sC0T7BMyKTo4h86WJgKAWNYgyQwjGQVadKtr19PV4sNsoNqOoa9VVPTB9JEXxS7NH_d38dccMcZbPd7vIzq1MsSmGcsHhLnWKxZ_7NXLCP8q3XK1mnnI3531EpVIIoo7uXWVVm8eeTStYXsb79qR4dMk1l8Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان:
هر کس رفت سراغ s400 روسی, یعنی کارش تمومه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69074" target="_blank">📅 22:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69073">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/69073" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69072">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUzFelpAKkjFEsaglVX1vT4Gia7qms-npYENNv7adEsoXXSQ7_GSAGvVyFMypAGysoIwSbRM1GWkXGPtudkbqKPUy4xVGitmdy-9D-L9JITREPOwMU7n8KcMXlrces0RFrZqDKCURVQzIcgGpCEO1r7lMgzRg0kLon_fhtyckAtiCNkk5nwTIqtr5GlwUpZRn-T4ja7y_2PH4gHuw_pEEI3LBRv8PtriC7lPNg0MbA9_AS7RalzNbsc6B0bT4scTI2YRlomTbXntI_l3xasCgGtRpj1s6WeE0Pk-ofGbsbmG955KxXOe8lboWt4-HluA3TMlrqx_BzrIcS9j9wpyUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
فرم نتیجه دقیق رایگان با ضرایب بالا
💎
بهشت سنگین زنا و افراد کم موجودی
👍
https://t.me/+LVbtmWdHFTdmN2Rk</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69072" target="_blank">📅 22:23 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69069">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=ayMyS7KXwzR2XD5GPLqyIZya3XYU6MS99fjuX-QH9YW2KmeaRCa8D9roosYOzsXpHHSVuHfLlzBfCovoQ_fziqIxaNrzVwGsjReNMAK-zjmFNSxZbzgqkjXe3s1sPQ6d4v_kHXcfQHHoI_BGwjVQwiz-oo3RJsGzu193rtdVKkz_2PF1pNsnAsprILEVtIga4Cw-dsQWQdmZoFVCLrW_ncSKFZBGVGR0OM5FcY4F0ScxbwSOTaU8YfDZZ3j6LoEOIUzE1m73fZgOB5S_BVyjCLzDUadOXEXAlXqrpm3TomURebDNwb7IwyroK1GeTYF6Ird1EmJez7zrg4tB4v5z-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4dc96cd73.mp4?token=ayMyS7KXwzR2XD5GPLqyIZya3XYU6MS99fjuX-QH9YW2KmeaRCa8D9roosYOzsXpHHSVuHfLlzBfCovoQ_fziqIxaNrzVwGsjReNMAK-zjmFNSxZbzgqkjXe3s1sPQ6d4v_kHXcfQHHoI_BGwjVQwiz-oo3RJsGzu193rtdVKkz_2PF1pNsnAsprILEVtIga4Cw-dsQWQdmZoFVCLrW_ncSKFZBGVGR0OM5FcY4F0ScxbwSOTaU8YfDZZ3j6LoEOIUzE1m73fZgOB5S_BVyjCLzDUadOXEXAlXqrpm3TomURebDNwb7IwyroK1GeTYF6Ird1EmJez7zrg4tB4v5z-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⏺
حسن روحانی درباره اعتراضات دانشجویی تیر ۱۳۸۲ (17خرداد 1392):
آقای قالیباف من دلم خیلی نمی‌خواست بگم، ولی شما من رو ناچار کردی. شما می‌گفتی دانشجوها بیان تا ما گازانبری برنامه داریم تا تمام کنیم.
ما می‌گفتیم راه این نیست که ما مجوز بدیم بعد بیاییم گازانبری این‌ها را دستگیر کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/69069" target="_blank">📅 22:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69068">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_TG2bAzuCO37ti2blp3hnjozEv-AEWy4huFp7CrUfzvs5QZ_QYtPrONmBNfs5ZM4EbIM4JjiOiwdfdCcu-ZPdx5Wcej9NAxH_RFXdsJ7SjExMtd6_4pv-fLLha-65MOPZnXk-5NutLL6D-ZVPQ9Cdp0EcHM81hVBdol3eZ0e7yjz2iKQsmSWfBfJpGOsnQRSg10_l-VHik9FWmM9viFlSTuW462qwae7iiEuTh2oZaD43_sHVzoYi9aAOO-_HqAYQsIQ2bDy7xWnt03frVOsifedyMAPgPy3X2cSdz4kQ9zi-8iRSBcgT-A5P46lSENFNUA6yKKwOEzLyV1AxvrFpos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ab4cc3c2d.mp4?token=qT0rkXMXMGzoDjKC9-88HuVAvq4eO6JmV2Zb3X2Cg5y6UfL2ZPoSa9L-1Ddx8PvsjOOq_1kWklHwvC8Y3I40Qz4bAC2b1zy5NWGrQj0RB-ffi1heemEyyLlomDjC2qYlTzvTQcWHbMU9LX14xwXnYA2mvfG4zzd6mk-vhd_ToG7VCaIkYhuHAbZcUSAcyWN_AqQPy0MofNmZLucQYvZ1yG5WFLtKzi4TtOae38WnLN64Cyac3d8IOfvABt6NLon8Jqd1YhE0TiiHdlNTZT-gUuxW7Mxp-JiVxeGPqr0PVZQgBPEPoRfYy2dgdWycNdo68JH7puGF3tgaQ-xersTK_TG2bAzuCO37ti2blp3hnjozEv-AEWy4huFp7CrUfzvs5QZ_QYtPrONmBNfs5ZM4EbIM4JjiOiwdfdCcu-ZPdx5Wcej9NAxH_RFXdsJ7SjExMtd6_4pv-fLLha-65MOPZnXk-5NutLL6D-ZVPQ9Cdp0EcHM81hVBdol3eZ0e7yjz2iKQsmSWfBfJpGOsnQRSg10_l-VHik9FWmM9viFlSTuW462qwae7iiEuTh2oZaD43_sHVzoYi9aAOO-_HqAYQsIQ2bDy7xWnt03frVOsifedyMAPgPy3X2cSdz4kQ9zi-8iRSBcgT-A5P46lSENFNUA6yKKwOEzLyV1AxvrFpos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❓
توضیحاتی درباره کوه کلنگ و چگونگی نفوذ به تاسیسات آن.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/69068" target="_blank">📅 21:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69067">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=sZOIGoyNh-WhiyOWKuj6MToOIpkyF4RtPn2ar8Mr-FfldyrwSd9Ke1gwPdl5fJiqeUa9EOqr-x7mH8SAc5i1sCzJ2E-fsYGxiB1vEeQIKXWo4YESTl_K4KLjLluL5oidi6mPH9MZKfWfOjs7R4aU8wEa5ds3sJ8WP5GxvoOGCFN0AbTaBGmAu9rC5cepVdH8brrKDHiz72zfGDEehqp766nSMwTPNRFO27TkW1Xs2TXEK5ldzI0o0ccV3O4oruR7xmY8i_WmHGX_FF44JPiiLPR1fIdY0Z_fSHR4g0tPZ7ro0Eg0njJTFmBrNnfXDBIvsz9bJiXCNyYcp9s5mkmAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3cf7ba0e57.mp4?token=sZOIGoyNh-WhiyOWKuj6MToOIpkyF4RtPn2ar8Mr-FfldyrwSd9Ke1gwPdl5fJiqeUa9EOqr-x7mH8SAc5i1sCzJ2E-fsYGxiB1vEeQIKXWo4YESTl_K4KLjLluL5oidi6mPH9MZKfWfOjs7R4aU8wEa5ds3sJ8WP5GxvoOGCFN0AbTaBGmAu9rC5cepVdH8brrKDHiz72zfGDEehqp766nSMwTPNRFO27TkW1Xs2TXEK5ldzI0o0ccV3O4oruR7xmY8i_WmHGX_FF44JPiiLPR1fIdY0Z_fSHR4g0tPZ7ro0Eg0njJTFmBrNnfXDBIvsz9bJiXCNyYcp9s5mkmAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
آیا نتانیاهو می‌خواهد که شما با ایران به توافق برسید، یا می‌خواهد به حملات خود ادامه دهید؟
🇺🇸
رئیس‌جمهور ترامپ:
«بی‌بی» عالی بوده است. [قدرت] ایران به ۸ درصدِ آنچه چهار ماه پیش بود، رسیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69067" target="_blank">📅 20:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69066">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73754cc159.mp4?token=Ukz55_dqPAUpK7JHY9do2uLV41K1HBVfWDIdEDlfga7zMPy4Tl4ykB0VJmY_uEGajD4LDfTzaTSNKND5kTQBFMgNW1lHqSSf_AGtQHo3IaOrQjJg7lrlBoJQVCTW6uYbByFokxU-LRKI49dsbnBanFLiPAjoYfRJbPcKo2IvOg-stvLL3oiClJod5jHHHgCNchibL-OuiWwtj7AMBXU2TfSHv4Zhw4c4vo77vPQfTDb_itq5rBWkze1FKxONvbg9h7GX_vOeii3cBhiSi_73920ZGyA8xEEgR18fPCWaoLCSegMfp5vvnUz5T7NMPZ1mgCyim_snY_VqOmYX8ysZpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73754cc159.mp4?token=Ukz55_dqPAUpK7JHY9do2uLV41K1HBVfWDIdEDlfga7zMPy4Tl4ykB0VJmY_uEGajD4LDfTzaTSNKND5kTQBFMgNW1lHqSSf_AGtQHo3IaOrQjJg7lrlBoJQVCTW6uYbByFokxU-LRKI49dsbnBanFLiPAjoYfRJbPcKo2IvOg-stvLL3oiClJod5jHHHgCNchibL-OuiWwtj7AMBXU2TfSHv4Zhw4c4vo77vPQfTDb_itq5rBWkze1FKxONvbg9h7GX_vOeii3cBhiSi_73920ZGyA8xEEgR18fPCWaoLCSegMfp5vvnUz5T7NMPZ1mgCyim_snY_VqOmYX8ysZpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
درباره جنگ با ایران، از توصیه‌هایی که هگست در ابتدای کار به شما داد و نتیجه‌ای که داشت، ناامید شدید؟
🇺🇸
ترامپ:
نه، اون کارش رو عالی انجام داده.
ما ارتش ایران رو نابود کردیم.
اونا می‌خوان مذاکره کنن و ما هم داریم مذاکره می‌کنیم.
این احتمال وجود داره که به توافق برسیم.
اگه اون کاری که ما انجام دادیم نبود،
الان اصلاً حاضر نمی‌شدن با ما حرف بزنن.
هم از طریق واسطه‌ها و هم مستقیم،
خودشون درخواست دیدار دادن.
الان هم داریم مذاکره می‌کنیم و امیدوارم اتفاقات خوبی بیفته.
امروز قیمت نفت هم حسابی افت کرد.
مذاکرات خوب پیش میره و
احتمال زیادی هست که نتیجه مثبتی داشته باشه.
اما اگه توافقی حاصل نشه،
برمی‌گردیم به همون کاری که دو روز پیش انجام می‌دادیم.
🎙
خبرنگار:
شما و نتانیاهو درباره ایران هم‌نظر هستید؟
🇺🇸
ترامپ:
یه اختلاف‌نظر کوچیک بینمون هست،
ولی در کل تقریباً هم‌نظر هستیم.
ایران توی 14 روز گذشته ضربه سنگینی خورده.
اونا خیلی محترمانه از ما خواستن که
«لطفاً حملات رو متوقف کنید، بیاید مذاکره کنیم.»
الان دقیقاً توی همین مرحله هستیم؛ باید ببینیم آخرش چی میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/69066" target="_blank">📅 20:22 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69065">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klTK5t0OXCI6uNkPbjlVPhblzhIy3m1BmUD-Fxmp1i0z7uJdt7iEJGg-RBRxCWlSTkbmQdN1u21mSLiqCZ-o24Nw6-7ImLPh7OgXnI9stdon3uQCaIe9ZTgkdj44vPPnED5P1Dt_jVzOASJ1mCcwLLyATXy9tPKGekxGU3PBes_gl_COVQtrRcLM6mmuXSvLWPpgXXnZsh2Ds9nNON--CoKnCyqLyjnRGbNcABqUTAaos1hNVdbB6VO01bAFMbLw3BMF5WVkLz6g_SSwj8Q3map9S8uyjFsWzM2wOl4JOMFSa5-EUfjexnchBjFdlNqIsGX4d4NQsh9KhqkFqoA0nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇦
وزیر امور خارجه اوکراین:
تهدیدهای ایران غیرموجه و بی‌اساس است. رژیم تهران شریک مستقیم تجاوز روسیه به اوکراین است و با تأمین تسلیحاتی که از سال ۲۰۲۲ تاکنون موجب مرگ اوکراینی‌ها شده، به جنگ جنایتکارانه مسکو دامن می‌زند.
ایران هیچ جایگاهی برای وانمود کردن به اینکه قربانی است ندارد، چه رسد به اینکه بخواهد تهدیدهای خود را با استنادهای مضحک به منشور سازمان ملل توجیه کند.
ایران همچنین با این اظهارات تلاش می‌کند تا توجه‌ها را از اقدامات تروریستی روسیه علیه کشتی‌های غیرنظامی در دریای سیاه — که امنیت غذایی جهانی را تهدید می‌کند — منحرف سازد؛ اما در این کار موفق نخواهد شد.
حملات روسیه به آزادی کشتیرانی در کانون توجه نشست اضطراری امروز شورای امنیت سازمان ملل قرار خواهد داشت و ما انتظار واکنش‌های قاطع جامعه جهانی را داریم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/69065" target="_blank">📅 20:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69064">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=tyMFVzgu3OcOprLW4shxBFsSfgtlNqGfT2iTzCFBXFgAl1vIFVvoTIR1HW8u9Sq7BhD_is2gszB2F248-XJRFh2sp9NraWsDXbMSrR3q98yaMIJD_ggXADl1SlcMUAtN1cp48B6xFZum399MFQkgiWwBGt261PQfUxjEld0Cs1x2v83Yy-ENBrn_hie4DSWbxwqg1GeS-246Lm8BTuNH_8L_3uGcVW8XUEz4N1hr49LoG4Df9t-RdNRVV8jjKQs1uCcn9C01mSfmFL6bHWsuKvfDla69Zy2J9BZhUp0gUwv0lRdqKBsQ7qxdMn9A3vBweI8YAp2jPkBavKIFNC1T4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec0fc6074.mp4?token=tyMFVzgu3OcOprLW4shxBFsSfgtlNqGfT2iTzCFBXFgAl1vIFVvoTIR1HW8u9Sq7BhD_is2gszB2F248-XJRFh2sp9NraWsDXbMSrR3q98yaMIJD_ggXADl1SlcMUAtN1cp48B6xFZum399MFQkgiWwBGt261PQfUxjEld0Cs1x2v83Yy-ENBrn_hie4DSWbxwqg1GeS-246Lm8BTuNH_8L_3uGcVW8XUEz4N1hr49LoG4Df9t-RdNRVV8jjKQs1uCcn9C01mSfmFL6bHWsuKvfDla69Zy2J9BZhUp0gUwv0lRdqKBsQ7qxdMn9A3vBweI8YAp2jPkBavKIFNC1T4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
محمدباقر قالیباف، (اردیبشهت 1392):
در اعتراضات کوی دانشگاه عکس‌ام روی موتور با چوب هست. جایی که لازم بوده چوب بزنیم کف خیابون چوب می‌زدیم. افتخارمون هم هست.
در شورای امنیت گفتم هرکسی بخواد بیاد کوی، منِ قالیباف لوله‌شون می‌کنم جمع‌شون می‌کنم.
محکم وایسادم مجوز تیراندازی در کوی رو گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69064" target="_blank">📅 19:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69063">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ به کانال12 اسرائیل: اگه مذاکرات با ایران جواب نده، دوباره حمله می‌کنیم
«الان داریم مذاکرات خیلی جدی و عمیقی با ایران انجام می‌دیم، ولی اگه به نتیجه نرسه، دوباره دست به یه اقدام نظامی خیلی سنگین می‌زنیم.
زیاد هم به دیپلماسی فرصت نمیدم؛ یا خیلی زود به نتیجه می‌رسه، یا کلاً بی‌خیالش می‌شیم.
همه کسایی که توی مذاکرات با ایران درگیرن ازم خواستن حمله نکنم. مدام می‌گفتن: "شلیک نکن."
برای همین تصمیم گرفتم فعلاً حملات آمریکا رو متوقف کنم و یه فرصت دیگه به دیپلماسی بدم.
به نظرم ایرانی‌ها می‌خوان به توافق برسن و منم قبول کردم حملات رو فعلاً متوقف کنم، چون نه چیزی برای از دست دادن هست، نه چیزی برای به دست آوردن.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/69063" target="_blank">📅 18:47 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69060">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8aee1d66.mp4?token=pM19W93uwqGrF7Vs1XBlyXuyw8og9LHnMO6lbUCYxnqc0NM6H-BSAd-0jo5es5_nLSZ_PcK6-RDzTWPHJYjrDk8JNnCuN0l2dg3V-OT868ydK6ggeqDPMvsqk-LPwMZL-DBAOL9mONQBJWv-b1lAEJXTvCABeiZZh8oi8d3QpZSyV_FHLDlkLOKyZGKuuBczcMlAJSyJmQFg4yHF6Grw7d-UVM6XLbbQiO45lTyETxfcHy_2-TyQjP5cvZSI1-MmkukqBfOqc6vabEdZaG0kFAEv-0-8asAxqB6E4pJpBewpFaGq22WVD2Z325hGduTxxRic_4GbSjOvDbow04GV7J8XJaTqoLHcR3pLuO_C4oj3-qpPMb_kiH9VC7PILo0dk2COvoUhUyc8flPVU0xvDXqjk9plpCU6eetMg_hdVbcJAlaLN-b1mmnMRWeTeIUHLAdjg1XIhyg_irfBMG4hL7SqrpcuwINroTxoy-TAtd2k8kjVUy5mcj5q0MIYMAxq9GLA9QZiAtb-PfFUXKsmegEP1wdsV_Mlc6l6ovSvaMsS98ATf8R2J2owuQrHxObR-XuaknlNmziGgDsZN4S1pb1C4RE_KLf0yBxbLSTZrxkeuAy4kFQtk1j2pNZcum0aO4J0HzcrRTTSvIrxvc69sdU8hJjBNWTd2F3SminZLYU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
دیروز بعد از 25 سال، قلعه‌ی الموتِ قزوین با رای مثبت داوران یونسکو، ثبت جهانی شد؛
قدمت این بنا برمیگرده به 1100 سال پیش، دوره‌ی دیلمیان، که ازش به عنوان یه مرکز استراتژیک استفاده میکردن.
سال 654 هجری‌قمری، حین حمله‌ی مغول، هلاکوخان دستور میده که این بنا رو به همراه کتابخونه‌ی ارزشمندش به آتیش بکشن.
امروز فقط خرابه‌هایی از دیوارها و پایه‌های قلعه مونده، ولی هنوز هم به عنوان یه جاذبه تاریخی-طبیعی خیلی معروفه.
قلعه الموت 30 اُمین اثر ایران تو میراث جهانی یونسکوئه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69060" target="_blank">📅 18:14 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69059">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1028348d85.mp4?token=JhWm_H2tnjoPdm9rhsAsElV0kH-eO9rQEE9RBvvZtQ2GuMCPh51zBHJPowt6vgQi97aQm-MD5TtVrt2hrSCzZP8Iqzp-eFX2SpFju_u3xw0XKOVwT43haWetBGFvGv1S9aXFovMZFnSP4NSMMhamZdY1OKExc06MS930WU5xPxKFKmLZDCyWqYLMHHCi9xPBad7zarq6L4P5x-F4JnmxlsKydwpD28hivjpyUsyztOHA5ZfxQfIHPJSwmxoKe2IfoP-qHnSho4_kTXVyplxGqfAwHzbWkMnD4m4vINaZFRbd33y8GGwfkVY2Ye665iUX5_PDNq3eaJnjSPUgytLiGLHirssbeFAIWTaB2YLfCN6J_VqfXtI2__l_2YKwHEDMUweGd8HMx8utEE4b_aUfbG2PePol96ZQhjXyL-cXjNgIy4J1ZBWEBnFOl0h_rHXiAdJnehFla_BZkEFWz394b2lb8eymNA0snB2gKwNFMYbHmEQY_LIDmJzsPjvOwOYRVXSuuAyfEtLlwgY-ztqwPdxiC8JlWjnbJOXdSrZgcNcJIspUVZSqSUwJyTHbsJf81OiQ0OKIdPHAlsL5iAQ8aoc4RV1XQFH1Ic74-C27jFKO5y4tf_DqogMlnjEO4NW_UadobimmWfyyHTQABlwakZY8NaSyfzMs7ukqd3QH7mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از یه هموطنمون که برق خونش رفته و کولر ماشین وصل کرده تو خونش
🙁
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69059" target="_blank">📅 17:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69058">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eN2MQqWqY63aoV93m1KV4GvrQ_OgbCG9RURDVSLMkWj6xgL_baFzD_NGBSvvqgeFx9f1ELhqaCK1-TWPAHfDK_E7A0xOq8mNPQnYRyz5JRg7ERwYXmfEwDA0dh3wQnrA-x07cg4cAeSAeDPEnCSmjXY7poXdf0hRa8xBmRCJbpMepxFxDmDkuK8JnNdjUNYoVpzFVrxjL0TBHtdpG7H0nt6xJ8Fxys30pUPd9UGjMUvozU-pqISXF2KuTOhIyZ568arVciPxN4ZDh59N0Rkomc7U7aJMcS1kFCnBdIai3J03G9Uf-JoDap460RHAGK9n97Vb9SuE_r77qEd7F2qpMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
قالیباف خطاب به مردم آمریکا:
دلتان برای قیمت فعلی بنزین تنگ می شود.
بنزین در آستانه لیتری ۱۰ تومان
!
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/69058" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69057">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M4svIsG0l_KaI6or_AEgGqGLx2t8H4LgBntmzDtqupgWeUFSzQH4HuP_RYuQVD_qETEi8QQ-2HcvdmG58iLeoVQJ65WnizFDQT5P8rgwcDcf4nFXyi8AtXouD23m_TUQYD8zmWFAH85cEsuq7tXLuQE0scjhNM_tL5mKCx7MWC5BcSiDuow5N2NWUDihgxnhgx7SHX8zfVoi--SPEHVea2rdoRcSJcJ3G9_RAvFSmWEl9TQUgRs-u_04boUKnbwEghFctVgxAmbhqwblJ1holDtUfccnYCgVY41UfZ5ykkHfdantEnC_eJ_VKdSZeWSUVOYjTF9n7yHCxl6cH9kacQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
همشهری:
سران قوا با بنزین ۱۰ هزار تومانی برای «سهمیه سوم» موافقت کردند.
درحال حاضر، سهمیه سوم بنزین با قیمت ۵۰۰۰ تومان عرضه می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/69057" target="_blank">📅 16:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69056">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UU9AREx5A5ZVxBP8tPeBYLU0ABAkZL3IByZxtAKA-0pz35R909d9AbEDPD2JqEvVlxjVhlGhrjNOiOEpjGsmpTUGglB6EAVGb2RXFnwObdCq0vQdkuM69-zgAZ7PcKg0A1x38Zzd84gKKi-1HqsRAX179o3YzNt22SSYK_jug_s88NkQKJXm-w7NjDHbAFdlT5Ko4O8tv7WlWdOdcdv8i-8INkBiVwc1DRrnVnlbRout8BPaqwNL8VzziLeFrsrT6t6t_FoDlcSWiAsL9lc-zmAGkSQ73sG0YnZGrCFtoiyYmIeVXq2WNW6wM-kPR8pLmsvyX2BXx9KeNK44Fw-9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇦
وزارت دفاع عربستان سعودی:
رهگیری و انهدام تعدادی پهپاد که از خاک عراق آمده بودند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69056" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69055">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=PQIqh3KYnld4F0Ygkvf54WUUxg1PyxsR1HXl7VhggtTokpa7uMc9HbRkmXqlA3JYHjQovY8qVgsMM-zRhOLNET72aWheYOXSB_5vFfvdSjKAHD52Zb3C3b0BmAZQyhLLbgbS59fL_cGiXuaSPmkZpBlvRBWmxs69eBziWt9IgAavJrjKSw7fr_tgi-hJv829u5RO2MFboSWdr7B3A5fi1uVMxf8VXWSmIdFtLK0ybR5Yi0QW92uIzFWV4Tpoj0HIuqQsAvwzZ4J08l195Z_GoOUIggxLmMyiNqxx4gjS7RY2oDZmUFGxwKIk5v-59QzDjFGkFdDq-yTmic-nd0Jl4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69d958cc0a.mp4?token=PQIqh3KYnld4F0Ygkvf54WUUxg1PyxsR1HXl7VhggtTokpa7uMc9HbRkmXqlA3JYHjQovY8qVgsMM-zRhOLNET72aWheYOXSB_5vFfvdSjKAHD52Zb3C3b0BmAZQyhLLbgbS59fL_cGiXuaSPmkZpBlvRBWmxs69eBziWt9IgAavJrjKSw7fr_tgi-hJv829u5RO2MFboSWdr7B3A5fi1uVMxf8VXWSmIdFtLK0ybR5Yi0QW92uIzFWV4Tpoj0HIuqQsAvwzZ4J08l195Z_GoOUIggxLmMyiNqxx4gjS7RY2oDZmUFGxwKIk5v-59QzDjFGkFdDq-yTmic-nd0Jl4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برخورد صاعقه به موشک چينى در لحظه پرتاب‌
👀
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69055" target="_blank">📅 16:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69054">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=pItSRNsJN9zE2gKs_iS7xp4glhcTg2KlQRKgJHQ8C3FH2SEzPAqXUXFD9Ba4t_BnD9d5YJ6gIXdu57eQVZmd6HHDWaoJyr9J88jrO-q9NaQklvl_UVeyEwzKcMurwWRvM6PJyRpLBfc41cAydXcQgllNUNRBQJsxTSDiAyfYk86L4XoxLbr8-POmJPSAsedv-dnR9UE_CITlDpDueZuglo7n8FH7Z-NqDovAaswIMaxlNDruBSsUk2SlLzmy9sRPdvViPmpKR5Kq7k0SV7hiSZ66g9ZKTh8zxFtvIF9_mhLKjCAaKllS8kNPoqIdjD2OH9n0pK5BmeNBF5S0OTzcFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e50eb610c7.mp4?token=pItSRNsJN9zE2gKs_iS7xp4glhcTg2KlQRKgJHQ8C3FH2SEzPAqXUXFD9Ba4t_BnD9d5YJ6gIXdu57eQVZmd6HHDWaoJyr9J88jrO-q9NaQklvl_UVeyEwzKcMurwWRvM6PJyRpLBfc41cAydXcQgllNUNRBQJsxTSDiAyfYk86L4XoxLbr8-POmJPSAsedv-dnR9UE_CITlDpDueZuglo7n8FH7Z-NqDovAaswIMaxlNDruBSsUk2SlLzmy9sRPdvViPmpKR5Kq7k0SV7hiSZ66g9ZKTh8zxFtvIF9_mhLKjCAaKllS8kNPoqIdjD2OH9n0pK5BmeNBF5S0OTzcFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو:
من در راه واشنگتن برای دیدار با دوستمان، دونالد ترامپ، رئیس جمهور ایالات متحده هستم.
این هشتمین دیدار من با او از زمان انتخابش به عنوان رئیس جمهور است، بیش از هر رهبر بین‌المللی دیگر. این یک امتیاز بزرگ است، اما همچنین یک مسئولیت بزرگ است.
بر اساس تجربه من به عنوان نخست وزیر، باید در این دوران پیچیده با عزم و اراده قوی و خرد فراوان عمل کرد.
ما تمام موضوعات دستور کار را که در صدر آنها ایران قرار دارد، مورد بحث قرار خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/69054" target="_blank">📅 15:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69053">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
🇮🇷
اسماعیل بقایی سخنگوی وزارت خارجه:
«در حال حاضر هیچ مذاکره‌ای با ایالات متحده نداریم و به هیچ آتش‌بسی تعهد نداریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69053" target="_blank">📅 14:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69052">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNnvCh4P-R5I6WaW6NgyQelCH2s54Cvzo5Sp2-izO5Q0Na4mfBVhXV2rsAvfG0uXQIjKZ2ppudynrodNMdXnjvzJLHSlxkKRAPFPrjkp2KUw7gecHb_4VTJMSJdykpZHJ9OsEgFreIEEzdXd9TaJJtcC7G3Yi6NUvN9d26eOL7u2ZvxeEqiikUDK5pvSvJopLqPh1po_Ial08LwOFjriTsLpGrBQQki4cpeUmLHWJI5HivFbinhnpSuxjvBTBcr2D-B_acgRZ0dvUV9BgKvmtaoLdDjpqTqhHXVJZXJ1npcC2x56cMvhDUjY2LHnT978tYQyiVuXFa7Zg6rCd_ig0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇮🇱
🇺🇸
هواپیمای نتانیاهو عازم واشنگتن شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69052" target="_blank">📅 14:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69051">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ri3zgKDD4PzB-hSUZl5DEEQ1ok9ZOK8LqfTPUFfZIVwjxqNhGMIRzDXlRDMcBhZ-60tQ7om9gktzy240sSHuJDzcHv__TjNbNmuNh8VFDAqojH1rRHsy6eISsyvWOWDO_6GIJsBPGRwtQVegwh3m8wWNog_--b9RRv174DjLh-eOMIdzYZrf43VatafxR7xaMnx6DRL7WOS8u5m_VnpBecjk8Qfdkn_SyaAhXMSAcBTKBjv62KEZz_dI6MJoFw4vXt11-1H2UiCug5R5DhZbwhSoAPJ0hCpCDGtq0_nXuIhMJp-2OP-Y9fjP9aHtTB2B8LCpiNBEr2LjVqbV1r6V0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
کروز AGM-129؛ موشک کروز پنهانکاری که از «بالا» نامرئی بود
موشک کروز هسته‌ای AGM-129 Advanced Cruise Missile (ACM) یکی از پیشرفته‌ترین تسلیحات دوران جنگ سرد بود؛ سلاحی که بسیاری آن را «یک هواپیمای رادارگریز بدون خلبان» می‌دانند. طراحی این موشک به‌گونه‌ای انجام شده بود که از زوایای بالا کمترین بازتاب راداری را داشته باشد؛ به همین دلیل ظاهر آن برای بسیاری شبیه یک هواپیمای وارونه به نظر می‌رسید.
برخلاف موشک‌های کروز متداول، سکان عمودی AGM-129 به سمت پایین قرار داشت، ورودی هوای موتور در زیر بدنه تعبیه شده بود و خروجی موتور نیز به‌گونه‌ای طراحی شده بود که امضای حرارتی و راداری آن از دید هواپیماهای آواکس و جنگنده‌های رهگیر شوروی تا حد امکان کاهش یابد. این طراحی نتیجه تغییر تهدیدات دهه ۱۹۸۰ و ظهور رادارهای «نگاه به پایین، شلیک به پایین» بود.
این موشک با بردی بیش از ۳۲۰۰ کیلومتر، سرعت نزدیک به صوت و سرجنگی هسته‌ای W80، از سامانه‌های ناوبری پیشرفته شامل ناوبری اینرسی، تطبیق عوارض زمین (TERCOM)، لیزر داپلر و حسگر LADAR بهره می‌برد که امکان پرواز دقیق و پنهان در ارتفاع پایین را فراهم می‌کرد. AGM-129 تنها توسط بمب‌افکن B-52 Stratofortress حمل می‌شد و هر فروند B-52 توان حمل ۲۰ فروند از این موشک را داشت.
با وجود فناوری بسیار پیشرفته، هزینه بالای نگهداری، کاهش تهدیدات پس از پایان جنگ سرد و تمرکز آمریکا بر جنگ‌های ضدتروریسم باعث شد این موشک بین سال‌های ۲۰۰۷ تا ۲۰۱۲ از خدمت خارج و تمامی نمونه‌های عملیاتی آن منهدم شوند. امروزه آمریکا برای جایگزینی آن در حال توسعه موشک هسته‌ای پنهانکار LRSO است؛ برنامه‌ای که میلیاردها دلار هزینه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69051" target="_blank">📅 13:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69050">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Avd69e2wBFFcmBb1oEjAIWkk9VvvWfyncVAIZQWjSs2PckiofFvH3_nicQdnWT47lNrpxnA3OVrxbOFnA0Wk9Lk2Iyk77xlJiOyByPm3hWgZ0t69br99_WEI8sav1i6I9FVJDr9xtZFEn9LnEdZu1XLetIHnVSSCjvaxof6MYP_rHk1vYkmJlau2Zdbs1Drs2ziLlRuvQraepRlgDiG4CPh_YYtdM16SpMxXqvohevC_oq9k4uUL_EyFYvLnESm9OZxWiZu31uyYBrd0OuYztfTdQzYCyGg406rclC8qoG5JUqZMZ6wvz0msPphPqITd-JbrR01-LYm7SSExKf2AXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
👑
شاهزاده رضا پهلوی:
چهل و شش سال از درگذشت پدرم می‌گذرد، اما او امروز زنده‌ترین چهره سیاسی در پیشگاه تاریخ و دل ایرانیان است.
شعله عشق ملت ایران به او روز به روز بلندتر و فروزان‌تر می‌شود. همان‌طور که جاویدنام مجیدرضا رهنورد به نیابت از میلیون‌ها جوان ایرانی نوشت: «نسلی عاشقت شد، که تو را هرگز ندید».
پدرم با تمام وجود، عاشقِ ایران بود. قلب او با طبیعت این خاک می‌تپید و باریدن باران بر دشت‌های ایران، برایش بهترین و زیباترین خبر بود.
او در ۲۲ سالگی، کشور را در شرایط دشوار اشغال متفقین تحویل گرفت و با تکیه بر میهن‌پرستی، ایران را به سوی دروازه‌های تمدن بزرگ هدایت کرد. اگر فاجعه ۵۷، مسیر تاریخ ما را منحرف نمی‌کرد، ایران امروز یکی از درخشان‌ترین قطب‌های رفاه و توسعه در جهان بود.
هم‌میهنانم، اگر به راه او باور داریم، مسئولیت بزرگی بر دوش ماست. برای وفاداری به نگاه او، ما باید ایران را از این فرقه تبهکار پس بگیریم و آن را دوباره بسازیم.
پاینده ایران
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/69050" target="_blank">📅 12:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69049">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=QByXbmFwCq6r5wPaLTADyD07TZ9K7IQFPHkzHOmFy3NsSvS2Bgo9LG7Vw30M7H0lOpeaQhiMocQ-bMOy3Wxy9gY0901J7PP6N7ui6xjlC4lbPtvdqFt50Fx0OZGXMdwepRxITb6VqRtU8zD76LHxcwCcjnMhbR686LkLum_bfioxIM2Mf3a628WHBKoBm_MqkF4b-UzvLz6Q-rX5GLPw94B2L9nKkBmAFHN18JJGh3UuQUYETw8M_fUc1ImuIuGppu5d0g244idLPMth3HL4UvozesdIkTuKqGYXgRmEy6D2YRJudPJG7LHdKrpNGWZ8Mx4bmbwZ5TzGeNkrUcf5KA2sI6il324k0ZwEMU-9EaDtWOaZOLPeFn9kHpXp2d7O_zTW-mZnmA94HERT446d82ghvxOnDCx9TaOAl2Mu53XQQt4Ptgt585arGKBuE2K56MtTxPMIfyuGhvesVJKHp2GFVqks34qdly3ECXNzWpxvnzFmgNTWf6tQCA7J6SdrUiKSzRwSnS9HWO6a9e344wg7BhPKk2RsAErTjXk_XZo9YBuDXHTdaIuNAPNHIcPg5r33_RURs8qTjMEC6bmWCMDldtlHBa-8uu4U7kf4wbQOlORG9zegMzGbu0KfWyeI9Dtk3VJa-QOcp6TkF5g-jG2E2nmiPt7X8vGYbcqHUmE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/743c9eadbb.mp4?token=QByXbmFwCq6r5wPaLTADyD07TZ9K7IQFPHkzHOmFy3NsSvS2Bgo9LG7Vw30M7H0lOpeaQhiMocQ-bMOy3Wxy9gY0901J7PP6N7ui6xjlC4lbPtvdqFt50Fx0OZGXMdwepRxITb6VqRtU8zD76LHxcwCcjnMhbR686LkLum_bfioxIM2Mf3a628WHBKoBm_MqkF4b-UzvLz6Q-rX5GLPw94B2L9nKkBmAFHN18JJGh3UuQUYETw8M_fUc1ImuIuGppu5d0g244idLPMth3HL4UvozesdIkTuKqGYXgRmEy6D2YRJudPJG7LHdKrpNGWZ8Mx4bmbwZ5TzGeNkrUcf5KA2sI6il324k0ZwEMU-9EaDtWOaZOLPeFn9kHpXp2d7O_zTW-mZnmA94HERT446d82ghvxOnDCx9TaOAl2Mu53XQQt4Ptgt585arGKBuE2K56MtTxPMIfyuGhvesVJKHp2GFVqks34qdly3ECXNzWpxvnzFmgNTWf6tQCA7J6SdrUiKSzRwSnS9HWO6a9e344wg7BhPKk2RsAErTjXk_XZo9YBuDXHTdaIuNAPNHIcPg5r33_RURs8qTjMEC6bmWCMDldtlHBa-8uu4U7kf4wbQOlORG9zegMzGbu0KfWyeI9Dtk3VJa-QOcp6TkF5g-jG2E2nmiPt7X8vGYbcqHUmE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ایلان ماسک : در سال ۲۰۳۶ پول دیگه اهمیتی نخواهد داشت.
پول رو برای چی می‌خوای؟ برای کالا و خدمات: غذا، مسکن، حمل‌ونقل، سرگرمی.
اگر ربات‌ها و هوش مصنوعی بیشتر از اون چیزی که هر انسانی بتونه مصرف کنه، کالا و خدمات تولید کنن، دیگه به پول نیازی نداری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/69049" target="_blank">📅 12:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69048">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">و همچنین یادمون نره طبق اطلاعات موجود، آمریکا همچنان به تاسیسات زیرزمینی هسته‌ای ایران حمله نکرده، یعنی اورانیوم ها همچنان در دست ایران هستند، اون فتوای پدر بود که گفت بمب اتم نخواهیم ساخت، ولی الان مملکت افتاده دست پسر و تندرو های سپاه، پس آمریکا حتماً این رو در نظر داره اگه نیروی پیاده نظام برای نابودی تاسیسات هسته‌ای وارد نشه، ممکنه از طرف مجتبی خامنه‌ای با یک سورپرایز مواجه بشن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/69048" target="_blank">📅 11:18 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69047">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIiHSXPWcwKYPoN2sFDYXimLMzMUZcfCDHIIco9FSg4z6CKcBm9qZ6NQaajJ1GkBQ5q2Jy-tT8d6ij0dZyJG4w-UwywIZKmCoM08-4eePuSCTx7IfrRrjzjA7Ko3r8kvemLyC4XnPJ0-uTfN-6JfmojHwgA_Zkof8ipCGUsZiJjBv7lkVQZTEcIs8ff8yHpmZelmwf6Jk-cDrhngHvnrravhBCZ2vIBKAnFFWs1o06o0-9XuG9X6VrBtgHXgqg14BXFlVseCI6Khv4l8KZrXimBu7KFEWSLkmlMJx53zmUu90B8_56A78T0oDQbgIEJlCqAQauvCMyI90QUmyWPhZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
وال استریت ژورنال:ترامپ حملات به ایران را متوقف کرد؛ در حالی که مقامات در حال بررسی کاهش ذخایر سامانه‌های پدافند هوایی هستند.
ترامپ برنامه‌های مربوط به یک عملیات هوایی گسترده ایالات متحده علیه ایران را متوقف کرده است؛ این در حالی است که مقامات، مسیر دیپلماسی را دنبال می‌کنند و نگرانی‌ها پیرامون کاهش ذخایر موشک‌های پدافند هوایی آمریکا را مورد ارزیابی قرار می‌دهند.
با وجود اینکه ارتش برای انجام حملاتی که می‌توانست تا دو هفته به طول انجامد آماده شده بود، اجرای این عملیات به تعویق افتاد.
در حالی که ترامپ تأکید دارد ذخایر تسلیحاتی آمریکا همچنان بیش از حدِ نیاز است، میان فرماندهان نظامی در خصوص اینکه آیا کاهش موجودی موشک‌های رهگیر «پاتریوت» خطری جدی محسوب می‌شود یا خیر، اختلاف نظر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69047" target="_blank">📅 11:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69046">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=A_t1p6PWs4f_A4UXytXZxJDfmEgZkOyH-yxJV9d4nPira06rjH7fqQTqcrmgtanuXtN-R5ZOMOA9BQXfMmRNCjhCZffU9uJw4scqgOrolH1P0OUf1jCu5_KHo6T3QxC44EFbFIrVHIW-p1PvBliLMMyGFSWQCrHWhomoWQrRiZO6BOjl0CHSNITtG9KCVmVyueTwX51_0o9_g2oQ17iTkLl7A3FFOc9z4a5HG4S2HrUMrtk5w5gl_uHR6kdmU7hMeMgVyvtwy6oOyZDWOxTwTiHgDyEr7k4hYy9svtXCUxzpqjovPRWkWLSCvEdiJL_O_FUSTC88pKtUPICqfWfeaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f112ef275e.mp4?token=A_t1p6PWs4f_A4UXytXZxJDfmEgZkOyH-yxJV9d4nPira06rjH7fqQTqcrmgtanuXtN-R5ZOMOA9BQXfMmRNCjhCZffU9uJw4scqgOrolH1P0OUf1jCu5_KHo6T3QxC44EFbFIrVHIW-p1PvBliLMMyGFSWQCrHWhomoWQrRiZO6BOjl0CHSNITtG9KCVmVyueTwX51_0o9_g2oQ17iTkLl7A3FFOc9z4a5HG4S2HrUMrtk5w5gl_uHR6kdmU7hMeMgVyvtwy6oOyZDWOxTwTiHgDyEr7k4hYy9svtXCUxzpqjovPRWkWLSCvEdiJL_O_FUSTC88pKtUPICqfWfeaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در ۲۹ دسامبر ۲۰۲۵، خودروی آنتونی جاشوا در نیجریه با یک کامیون تصادف کرد. در این سانحه، سینا غمی، مربی آمادگی جسمانی و دوست نزدیک او، جان باخت. جاشوا پس از ۲۰۸ روز دوری از رینگ، با آهنگ «نقاب» از سیاوش قمیشی به یاد دوست از دست‌رفته‌اش بازگشت و در یک کامبک احساسی دوباره وارد رینگ شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/69046" target="_blank">📅 10:32 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69045">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y63g368mC-DrL4S7PKX5wTpxKtF2ia3OR2xCRW4pgwkqU6yY0h1NUAwmKGSEYQ3m30422w1uWe9P0LG4tc_NbyIB-Iqlyj1a7k3VxZKkw7IqBz7uidI9CC3COA8QNoVlo0p22djZx0LC_nEALYirVHKBnmb1uegre4JCLY375N_Wl9_Q2RpajO8sTM9dEMBWQtIZ6iTQu2lk6yq8_GYQrvA8rTebbyqd8siKnDpDiO89DtzXDIDKDLBALpU3Ue0bI1nBgiIaey7hwLwIBguQ4Kq4nnFRx6wICElY9Q5CYl_uqXIHn8xwIIE9xr2vZ-ODHg_2CIMXhIWSscz8n7cE_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دوش پرتاب میثاق ۲ / ۳ دست نیروهای رژیم جمهوری اسلامی:
⏺
نقاط ضعف میثاق-۲ و میثاق-۳:
برد و ارتفاع درگیری محدود
وابستگی به خط دید و اپراتور
آسیب‌پذیری بالای نیروی شلیک‌کننده
محدودیت در برابر اهداف سریع و مانوردهنده
عملکرد ضعیف‌تر در شرایط بد جوی
محدودیت در مقابله با پهپادهای کوچک و کم‌حرارت
ناتوانی در درگیری هم‌زمان با چند هدف
تعداد مهمات همراه محدود
فاقد سامانه دید حرارتی/شبانه پیشرفته برای کشف مستقل اهداف در تاریکی
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69045" target="_blank">📅 10:01 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69042">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/J0LRFoFDrNzAXaF9YJOpAaYmWnlBiZSJ6bAbKHNdPWNsaOjMLGUP45wJnTZ6oP15-O9JYBU-2uQa8_Y0E1IjD_s5U7aVMmQqB9seHVn13aK9JoCfaRdLqbrSt236tSCAl4dEfB_5-dXmP41nM2crqY7FK7QVCiO2M23UUccyjeP5u17qDmFjaNOFtA6hyHbpQB9p2Zq3rdIhTr6nio8jV9ccOEKZJemt4esqDlmafzU_YE8_WoDZy0IVCCDgVto4pDnTrfmINmrIZkt0qzF7mZgW9bbsiUI0YIzQ79LbZug9Z2vJ2tRdjq1K1NblzoUZ3AVtuMm8wHVmk6WRLEYf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WbthO4noy3RKhI7z6AvF4YlYnA6D2ZH85Ps9kn-rb7_nheZZl1PQVr0NlJ91vLwyhAc2mWxxVTlAryXCtz4IsVhWS4oe01OwFMegSANAOB5Mgr3FisYvNY2yRU3WNhLP1CFFO9aQOL9Q0q5tDCHz-o1muvlxNC0siKtB7Osr7bm7KI9bSAEFySYX_VhPd5c-wJwEZojqmXUUwFNUQyw9IoIPzMGZh00zbbP7fCfvItIhCy3GRDFWJexN4rNjF90n8xs4lHCujZDgB2SbbHAQsHoh7aF3O0gwM8_MyVuG4iCOw1U73cUT8RhvjsfX8VNJgKXn187KobN8YNsHZHmWdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sGVVv6rxbYLZpYSydJ9bJvTtISI-1c8-hqUz73n5NIceXYR_0S8pw1jbF1YOeEE7jjNIV9aXbNYhFDAa3lQUUtlSRpQVZe6y4Ys8xIImjZW4Un1grFRtXSj_Zzt_FcNmFVEW6FJ_m4sYOLZq4jaUPvb6eRE_JKYroCnyo9p69iAG8H9eyA3ufmUhtu8fE6tCGm_ds3SU8L88z1h19UStI5yPueHRd10JCJDiI3yywc4V1pUNpKXS9nHbJk5fPEYYXP64Rq4ev9ViU9UJ5Csk3-DnxSH5ky-SzzVBgf5514-Y8XO5gUGAYgy2Ht1zvwdk8rmn40Q8tAS_bg56AqrJrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/23b96717f5.mp4?token=sGVVv6rxbYLZpYSydJ9bJvTtISI-1c8-hqUz73n5NIceXYR_0S8pw1jbF1YOeEE7jjNIV9aXbNYhFDAa3lQUUtlSRpQVZe6y4Ys8xIImjZW4Un1grFRtXSj_Zzt_FcNmFVEW6FJ_m4sYOLZq4jaUPvb6eRE_JKYroCnyo9p69iAG8H9eyA3ufmUhtu8fE6tCGm_ds3SU8L88z1h19UStI5yPueHRd10JCJDiI3yywc4V1pUNpKXS9nHbJk5fPEYYXP64Rq4ev9ViU9UJ5Csk3-DnxSH5ky-SzzVBgf5514-Y8XO5gUGAYgy2Ht1zvwdk8rmn40Q8tAS_bg56AqrJrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69042" target="_blank">📅 09:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69041">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUPXuQvMtoRdHhkxClRbSyFrjsfB0ei_jUnuoX_Z--jLBh_mMQo3x2C5xqOUhSEw7-puOCd8f3nCIxGJ9t-6U81woMuddaKh-lNi_SPU37P_ePVFN66cv-gkr-vDIVyGAmR5m90VI5Vcprpk7gK2tmu4VYGGPL8XAcwB-IZ60VRxQKH9xMvoaFD_f3RoSWSrCarS96J1lS9osRzqHZ2v79wnvOJbF5pq3PlIhNWtJBTKSRpoOkcyHgr5ImrYjqyoiKuQB7_BOghZfOK2pX484hsKb4pWcuqM93kGyKwh0j9ve6ig3QpmEKSAn18UCQQyIJcoAABtWfAqKbNfKFZSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ابراهیم عزیزی رئیس کمیسیون امنیت ملی : هر حمله‌ای به ایران همیشه هزینه داشته و امروز هم همینطوره. آمریکا و اسرائیل این موضوع رو خوب می‌دونن.
اوکراین هم ممکنه به‌زودی بفهمه که ایران هیچ اقدامی رو بی‌پاسخ نمی‌ذاره.
فهرست اونایی که درباره ایران اشتباه محاسبه کردن، هر روز داره طولانی‌تر می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/69041" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69040">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mmq2jKqkvH1fvxW3aj8viT_hq5Z2eSN2fNOBebesMXT5_EZoUrVwDeZtAyaZqolVMIDzfUAc86aoASXCFuVojzMCd4OTxBuszlITNwSLlIA9Dme8KJBNJhbvWvaZB0bNf8KWucM1ex2tp2LW9-2I__6BEoL7B2RwjX2Qd8suDvnqhSlVw1iDOXeRw2gXJc0ABphfbzk-ENXRxNfj0vQWVwZvM4UzQPPbfAIYyF9whaU64qGH3WYiJoTN0KUpR-oYI-H-2bXZVKrmSg6M7B7cuVwZVdt1MjqY6FrTSEzAxpOCRjAvD7QKjA1Y2ARdOLrhbgXlrH79YUmTSWXfypDmRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامپ آمار تلفات نظامی در دوران ریاست‌جمهوری خودش رو با رؤسای‌جمهور دیگه مقایسه میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/69040" target="_blank">📅 00:50 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69037">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FOA0Ay_NKX4zTDJ7ERxdGi7fiOyba5JtOJRWg5miS99qijMU3bw4S_9asokhAsVuKu13vBr0XdQCv0Dt8S_Tw6SJVB5-mKMOJ4-UVUiq_FuJ4ETDibnUFG9hJwijRNQbv6gwGmKAgmeRt3xhoexAYGGruDUsu9cCcmLUHccA6QRbCu8LTtNOkARC5RdEJkLTEY7MWlBGvgYRck500Wh8srt55O0YP6O7ZgXjz09ecVJSIjqFQGYHAOxxgd30eu7jQ5f3Esku0_LxuECZ2E0qM_roKqlpST6McGwuGGSuuIF0umMdoyZZrDOvFvUITj5_w-17YlkmSQxaiKQxxGrhoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WclbKZ3VbCgBMK7kqFM70a_vHT3PQgo7aaah7-iOkg_FFrQpqqfw29IZWBcLe-g9SJ_uaLyUm7gmWF0BPewLUFcew6LLuuORVUmX1EATDZ7nejtEea0B98hLr281R4Ni4Fay4iyYd4RgniDf-Vfb3-AnEGs0gWfsc1rHnCvq-2EDJRsOisIg87WRGnkraxvz3OoCARHFLW5e_MKWGj7XpEL-ij5nLW1ChTDKhyxZCCV_GCouGRb54orsgUpUgIgL2IeHargOBCMwiZqx6KlNEWe68-1AfTNmSasiT3kEaxWNSJsoKuPqjNNT0qqox4H5ggWU1lAx_K5CAK7kEl2Gtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yqzy3ffnik4hvwVo6Bg96kJed3bvWcMV2bjFLbTrzr0Ee3WfzKE0JDfb2XcPmYjI4J48w35kSXuq6W8pamXWKDfZw9Jaj2gv6BZXzMlo_zgN6AT3vG421xxbELNyVy8xrOuEHY-DjU3U_s_g3K8-pU45bS0V42x-KBR_268OZZ3yJvzOBcWaPhemrzE8daCntYsf_9B8glZM6m6GGngYTWcYVKRZrD8NEXiYj19WaTRhyrzkSmiAhNAmNBtNTar9SGRr8EF8O2RjaSL13tMzILgYtorjUFj8TwzlwpxXFVZIPezQ2_l_vnvBeM-e977u8XxVktDfKojuWPnDf0FzGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇺🇸
ترامپ در تروث:
- به طرح اعتماد کنید
- وحشت در واشنگتن
- آمریکا بازگشته است
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69037" target="_blank">📅 00:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69034">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LX6eICXMCavd6o-O9-spIhe01B1ctdOn4s1DiWiTyRWu0fWZruRHs9OtnntbVnvLwxfLu3hDDqo7jyYrUWLbl6ra49PUBcMlpqYgYwSgfuNot1_cxcCF-JO4zaeOf9f8GHDOBd2zeGKZmaTZxU-Yn5MIFDusHc-HewoeVbHsCgL_eYK5A1w1oL-kQ-__nfhATaipQyKdhQPfAAUJTexYHNNDPSITR_tRCdu2qT-5luaxfcu-2EKyb0HEg8H2PKil-qxr641gpARO85sm3dGtyJ2QhNNEQHz9dd4fAdipZgIGPQbkHekAZ9qsgAnTp9aJJzIqIM0bLPPyxFQewqcUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzQfN9o4SsNgkboQYYHciN4Il5X_pb_UBMNStcY1WPA__CSb_VmVILrFgnv9do7156ieYvTe5sHfZxCJpyMCmGNUVeTUVHRtMh_4LjDd_Glpk6IMMVzw5ca571BruRDSbvIn6dUdGUCrl1K2TKi1vxt2DtGk4Pn6OEA3Q8PKgA48E_UDLTFd-nX8CLTMW-MZShodkY1miZkElqF7C3zavIruJU9VHRjZhI0ZZLOQtD8kaz6HsijaDQyT3Y5CR8lhSXlESgYhxYZI2k3yUbA7V5Rmo3GDKYiyOxxsNPd6sJTYQ2Hc1za93OC-MTjjdgBb6DOfhbRioQkglb_L6BlMCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qYCvj8B5eUBBgzlBNs36afgN8XxRFHPXMeo_XCMKgoueqzFk_Iumq1zxWTVa_2eTmVt9sqgyux6SakwkJNZATNZlKbQ8xxd0JuhxeprnZzKo4AlgGhdM5JfPnJ_PZBDUH9TzwIrLPsVcHQCAc01ZPUW8oWYLUBVKo0CLtQojq0TC7cBtAr5BuFXroQjmnp1q8xTRndlZcOpdbJ8KWs1Vhw_8wsZole8JemBMrqcNcVVMS0LaqW6Lsm9v0q4VIe4XPyVglifM2AdNFcv5vMGQ81dasHMAF6NZXlrvTKl0OYwQLvHeHe3MFTUHZ0dknB24SrQEqPcJ-boqsvo48gR-Wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">املاکیه دلقک
😂
@News_Hut</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/news_hut/69034" target="_blank">📅 00:24 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69032">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/utyQDPIS7Ktz7PaMmpzkYGlgluRBq_Og8YsMcwphXJneplzQIchpqvNowms5nPF0VQ96_hvk6kPQO8oJSubWDPFz9Yy5IcgbEjAEyDDeTz8xPkFSboJs7P3OcfwcZiO_eat6dkspX4UlRRSVB5U3-rxqeh2n1rwzo8xeef-dcyD0FkArOdglx8Vl5Bg2vN9iAiPy1PERPuDaG8qBXo6Vyx1o8XJqFTd6MMCgjdRdrkKA-HEfp8WBydO26XZyrrj0PDPm899q9snI_TmIog1UU5s2HTK7YFrQOYL_ReewvFYGISyK-OtVNRJBKncCXf6DsPGBRoP3EcBc73EiPqh9UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KQduswxdCjxutPDKOwr_aiF9rYRGPYj1UAOZZaTGSXXsvLq5C63oeAjlmc26Cv2qwKCqZcbFHuKDpyf-h35KK8ToQXzikfbr3vK05fK5ufYnmS9C1DFgHjnf2wEho0AsRKSmmnVfjT50oZRZmJ4uX66FBnqw7sfaI7tj5XGMwE7nyxjtNaym5btrX0RB3T0ei7W7WJmTrNCNy2MW2gTy8BTdO7bphHDOfbnz0tfUYnPTUa0H8bLJliUiJrNNwInjFj6FvFV8BGt8AU0oUHwZ0jiFGhdObPdSSk8Qk_hUw_gT76oPt4sXEt8RnF89XAIM207dYBr1IzhCS5fJ37HY6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
همچنان ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69032" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69031">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رفتیم تو 05/05/05 برنامتون چیه؟
🧐
#hjAly‌</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69031" target="_blank">📅 00:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69028">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M6n00MQQLTtNHYXkJDDq7ffo2g3tO6ieBdhmi_ZRTsvi8MvFc6s7_0_hzwbIwTKjzBxXivplV7xrp3CJwbGsOLrfkKEGxGV7fCq8D6NgC_deLckDMLhPhflUHvq_DjaKGd0_XRsqMfvQK8F-ug4QnAuRWfoilY6lcGxcmtScN24hiZoWlAsBp3R1XsHFEBu5RFgLyT9aMJa4HuKjK79YCG7n7wXeCrBo_VGMQhm9J1Xjv-Evv3eRP7BEKHadsN1bEfq9DeAFF4YnpjxBzqcvkAhJWbPnBUs4xBr6qVLaRvPjcQ8wMNFv_p37wXvusdBumX6EALs7z7N58FhqerZ7AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S8RiHgS0XiR_Yh6oZzRTAWLzE5GCPLLAS2KrBRRmBZgWb2dTQmWHWTcwmf_1BbOXdv9HN43DkTnttl06nu9vhCTYYH1FyKWdrtmUn5dOEOWHSwp0oSp7kQ_yNqTBatXgmZC9BoMhGQu7ztxgxxfh-cw1atx8nPLZcXHzisUZjj3Uws2cmSoX-6Zj5XCKW38wUzVm4PTe8ho45EuV5Hve3924FnAVXwtgOvie2MKXhzX8ePTJhyT0V2i8x8tOihmmER_NlWegheF8sVKSqLhza-Z-GUCV0ZEjqtuefuq3AkCZOA549RJ0kc1aCHqfAg7WREoxiJA0_TkKMMWo6CjgYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RJFvuM4JCUmU9YxpP6p0bSvM68Zagk9hoJ4OUSfV-MuwntLM-QZKNzeUF9uZjMvD_xmXStaY5hlNjgL63SgP3tmtnKFqYjgdgScRpSKirZhe_vg3NDQ7qsmy3hPmmyVzIY1Uxja3J_ImxFlxyaqYR-N-Ds-C2-Q4M_HBXXXTgIRFu0QnU5g5yd4W34XD3VHkOFoFThu-QuPSN5scyOziKHxr0ryKArUiaGpgtjVx-llYcdQEbyb3ZLb0ZRlRLmMtg4n84-2LpcXTNKsr1G6Jwtmsvm48zcC3SKG0igwSkAhtEoD2xsljgKYrpLTfL7s6ChKNfy9XGWevTL13h7ZyQQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🇺🇸
تصاویر دیگری که ترامپ در تروث سوشال منتشر کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69028" target="_blank">📅 23:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69027">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد: حمله به خارک  @News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/69027" target="_blank">📅 23:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69026">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqnmy-exPZ_egSdYqgPEPv6TOrznOWQuaABK25trP26ZoJwFPSk7bQ5XwBe2kFTHwTcFjYu8V9Cm3Ia5S-2hHYLtMDpdIJKWszmdRSZoI4KHfs-l8VXV6RCZBkq8Lw7DD60Cax6nbb8Eq6JCFff9ofq8DCDrA9-7j7XatJPD7my42860ulojzIgCQeaPJVWB2zqo9uLmMdUf3KvxGY_I_K-71tIshXd6Gf-wm6edEj3fiOErVdkFfMrUQ_MDpVFzIEYqAS4dJyM_m1fvt4tRDYrZTn8yXIV0LBY2x7XAGS4xZIUfsgeR7EGdhZ9Ws2q06xeS0qd_pt45WOkSyKPspA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تصویری که ترامپ منتشر کرد:
حمله به خارک
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/69026" target="_blank">📅 23:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69025">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=gqmp0uSh1GEgJS65jgGhEMwhyhhd8zzGDnEQ8-pUdPbM31XaZitgT4lTHem_FkBOo4ZkcGjCgiIq9epAtIpaBQOxW7DTHv9IF2GK2SYNbcrwRosOY9UpE7geb_whDf7_FiEe5Wv_u4B6PqEX_okKu9yCOIwtjF2LDZoYAoye9TRR5KXLDfRPpb6SJP1k9IcYgdaAFSiF8N79sH8JFJe8fDfl81huq8Pp_qZQqfI32I6zAwD1-1ySdSYfzveExGEyHt3ZgXUKHkqS06cdFbOqskDfIZRVqiZSROvWflT6Jxf9oRvOUq2wwxolcONUfGpCOwc_u941co9rCJvixZmKTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e3f5c86e5.mp4?token=gqmp0uSh1GEgJS65jgGhEMwhyhhd8zzGDnEQ8-pUdPbM31XaZitgT4lTHem_FkBOo4ZkcGjCgiIq9epAtIpaBQOxW7DTHv9IF2GK2SYNbcrwRosOY9UpE7geb_whDf7_FiEe5Wv_u4B6PqEX_okKu9yCOIwtjF2LDZoYAoye9TRR5KXLDfRPpb6SJP1k9IcYgdaAFSiF8N79sH8JFJe8fDfl81huq8Pp_qZQqfI32I6zAwD1-1ySdSYfzveExGEyHt3ZgXUKHkqS06cdFbOqskDfIZRVqiZSROvWflT6Jxf9oRvOUq2wwxolcONUfGpCOwc_u941co9rCJvixZmKTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇮🇷
سخنگوی ارتش درباره عدم حمله ایالات متحده به ایران طی دو روز گذشته:
«آمریکایی‌ها سردرگم شده‌اند و استراتژی مشخصی ندارند.
اهداف آن‌ها برای بازگشایی تنگه هرمز و نابودی توانمندی‌های نظامی ایران ناکام مانده است.
🇺🇸
ایالات متحده اکنون ممکن است یکی از سه گزینه را انتخاب کند:
عقب‌نشینی از جنگ
انجام یک عملیات هوایی گسترده
اعزام نیروی زمینی.
ما برای هر سه سناریو آمادگی داریم.»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/69025" target="_blank">📅 23:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69024">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MnT1L318l6mjbfiKnoyF5Jsy7RsoPsq27VCsoJNtlLbyFrr9zRbKWdrZlHjp_tDt7tyi50C9s_U60QXaZCv78rTs4HSSy7fEVCEJgiOcpd7wEw68-PIAG237RvsOP3b2Rw1Z8I0Nv9KPRcxk8FQL9ScYtjWnUgYz6gO1xixupk-dk7Vy_1XAAoFswbdrEvarPr9J46Y1uCDloYlpduwsnhT803cCa-INUR7OkpLTjw1QU0LvBOQl71cMZxyWmWpBjIgfSa5VWUVM8PrqHTfm4e9uj9k9xvnZDxsGoY7fvcCmN70HPC_fmNF6nrwcuxLSYH5a1-UsCgWz_YURRyUUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇬🇧
🇺🇸
اکسیوس:آمریکا و بریتانیا برای برگزاری کنفرانسی بین‌المللی درباره تنگه هرمز برنامه‌ریزی می‌کنند.
دو دیپلمات اروپایی و دو منبع آگاه به وب‌سایت «اکسیوس» گفتند که ایالات متحده و بریتانیا قصد دارند هفته آینده نشستی سطح‌بالا در لندن برگزار کنند که بر تشکیل یک ائتلاف بین‌المللی احتمالی برای حفاظت از کشتیرانی در تنگه هرمز متمرکز خواهد بود.
بازگشایی این تنگه برای کشتیرانی تجاری، عنصری کلیدی در هرگونه راهبرد خروج ایالات متحده از جنگ با ایران و همچنین در تلاش‌ها برای ایجاد ثبات در بازارهای جهانی انرژی است.
به گفته دیپلمات‌های اروپایی، برنامه سفر و تاریخ آن همچنان در دست بررسی است و هنوز نهایی نشده؛ این رویداد احتمالاً وزرای دفاع و فرماندهان ارشد نظامی کشورهای غربی و کشورهای منطقه را گرد هم خواهد آورد.
پیت هگست، وزیر دفاع، و ژنرال دن کین، رئیس ستاد مشترک، احتمالاً در آن حضور خواهند یافت.
یک مقام کاخ سفید تأیید کرد که ایالات متحده و بریتانیا قصد دارند هفته آینده این کنفرانس را برگزار کنند. سفارت بریتانیا در واشنگتن از اظهار نظر در این باره خودداری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/69024" target="_blank">📅 22:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69023">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbmdtoVo5IUTMt24KK_P5wYpf-czFo5CIf74V5Un0uxs0CUairs9YL-CkRVlJNdMcthhElhLFYMovoH5Ba6AJB_MpGHcGpk3ZrxfypY5W7KoRDqOqVHlz7t1yJHa1oU39yk_dQhQZmvZvKa8KC_ZVPYmhicr6oqX7DOsqPC4q7SvX1rAflq7-KAB7bMTjFNxIepy39jSHYW4-o4sYXgldfO7_oyZYh_MTXwcg3eDjjl037aBVghI4TWL4dHdruKVOUAEabSilgbZnnxtYdCGzOi9PN3qNe-QJ_CVvN43CmG1xjnNHec1PLV6QDIyraUSRaM3tnfmTMEdFSECzc5gbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
آکسیوس: دریاسالار برد کوپر، فرمانده ارشد نظامی آمریکا در خاورمیانه، توصیه کرد که کارزار بمباران در اطراف تنگه هرمز متوقف شود، زیرا این عملیات به سقف کارایی خود رسیده است.
- این تصمیم پس از نشستی با مشاوران ارشد و مقامات نظامی اتخاذ شد؛ کسانی که طرح حمله جدیدی را برای آن روز به او ارائه کرده بودند.
- در روزهای پیش از این نشست، ترامپ تمایل داشت که به عملیات رزمی تمام‌عیار بازگردد، اما دیدگاه او از عصر پنجشنبه شروع به تغییر کرد.
- او تأکید کرد که دو هفته حملات در منطقه تنگه هرمز، توانایی ایران برای حمله به کشتی‌ها را به‌شدت تضعیف کرده است.
- کوپر خاطرنشان کرد که اهداف تعیین‌شده برای بمباران، عمدتاً تمام شده‌اند.
- فرمانده سنتکام گفت که گام احتمالی بعدی می‌تواند ازسرگیری عملیات رزمی تمام‌عیار برای تکمیل آن ۲۰ درصد از اهدافی باشد که ارتش آمریکا تعیین کرده بود، اما در جریان «عملیات خشم حماسی» (Operation Epic Fury) به آن‌ها حمله نکرده بود.
- او تأکید کرد که در صورت عدم تصمیم‌گیری برای بازگشت به عملیات رزمی تمام‌عیار، ادامه کارزار بمبارانِ دو هفته گذشته هیچ فایده‌ای نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69023" target="_blank">📅 22:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69022">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hrpehwzz1S-BZZRl39qiYPYoXYxWfhwo9N_J0ajK_BRwtNTxLmYNuDQOs9-SeNHIuoTng_Lq9VIZLNtR-A1AlqNOiJ5rCvkMtHz6N32UOb-DYWuPY1bbj7L_P0hJYhG_iDnNumn9XYrQpS8T8VlrZZkgBc4Gm86dCmmAeC3-wv_7Q9nWrkqP9_BWDAlGOMoPwsjcTJBJ3JwZRV5FXsaLvfPfFwmNKY14-_ZbmuLptXettEGWx2szs5u4jCsbxti1yqzpyz3KAg1CKtx3wM6h8zFQUegIKVgk3LgUSIO-CixJ8Z6Kgnvg9KDloaECSSUvgNvIhmHgMCCBq-FTrrzw2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
ان‌بی‌سی نیوز:
فرماندهان نظامی آمریکا عمداً به برخی از موشک‌ها و پهپادهای ایرانی اجازه عبور از پدافند هوایی خود را می‌دهند تا ذخایر رو به کاهش سامانه‌های رهگیر را حفظ کنند.
با توجه به اینکه ایران از آغاز جنگ نزدیک به ۹۰۰۰ موشک شلیک کرده است، فرماندهان اکنون فقط با تهدیدهایی که به سمت نیروهای آمریکایی می‌رود، مقابله می‌کنند - و اصابت به باند فرودگاه‌ها، رادارها و انبارهای سوخت را می‌پذیرند تا پاتریوت‌ها، تادها و رهگیرهای سری SM را که جایگزینی آنها سال‌ها طول می‌کشد، حفظ کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/69022" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69021">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhy7b1g_NwNlJBSLYtpa8KKiWvJ7gdpbGnGQrGo8DsslHIh_ji0YVfi6bWLv3VgyjrLz5cUuJMcIUN4qWw-tyegyUM5A1TbAQzwp1de8g9DyAAzMUyIM8xJRgdTHN7jTw2Q04Xj0gb4mNPJXXU000ma7-Wcz5pA49O9uxweZ9epZJhUFokuKokt9mpotfBs3h0g3keGzwt4phFCVhJ2iqT4l0cwqqzzd0xDKMskRKaOn-5KasWp8pKSA7EJD2bqjcHvvpyByD-fImtJLQdIScU1v0s3BtywYtF5XUbPCpsWMXRVHdHdMkk9aUvOfxYwrcHwaLeqcflJnmRhUfWKxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
عراقچی:
زلنسکی به یک کشتی تجاری ایرانی حمله کرده و موجب کشته شدن یک دریانورد شده است؛ اقدامی که نقض آشکار منشور سازمان ملل و به دستور اسرائیل، با هدف کشاندن اروپا به جنگ آن صورت گرفته است.
در گفتگو با «کالاس» (نماینده عالی اتحادیه اروپا) و «لاوروف» (وزیر امور خارجه روسیه)، تصریح شد که اقدام آن عنصر مفت‌خور در کی‌یف، هرگز بی‌پاسخ نخواهد ماند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/69021" target="_blank">📅 19:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69020">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d78921238e.mp4?token=H9wpuMvrOCKL7Q_m2w-uPOzxCNOBca-uFER7zUYMNU-vHjQObTJIelUgAZGE_BpWrsdJ7WW6wWz4YuAGv3nS7UCoe4HTex5KPMp2yabMe0BBi1Y3dmD74UOd67mLOvhDWLGIUD5RgqZzvz3jtvCFCjhJS-iE3jrHwa6Z3Zz2ej3jC2d7KoXUAGosslk5DZpJc95BXjighWif-hkvSt-k9g-X77ke2Q3oGW0fES2zi5F7TfG4ex8wtHdf2gnfSXBGIQinZ2V6orG2GE8XLySDWgoQrSYsvyQkQQciAKmaYsY2xSHI0s0atCptn7XdJRGhSYk8h6sTKg55QbLBVXD0MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d78921238e.mp4?token=H9wpuMvrOCKL7Q_m2w-uPOzxCNOBca-uFER7zUYMNU-vHjQObTJIelUgAZGE_BpWrsdJ7WW6wWz4YuAGv3nS7UCoe4HTex5KPMp2yabMe0BBi1Y3dmD74UOd67mLOvhDWLGIUD5RgqZzvz3jtvCFCjhJS-iE3jrHwa6Z3Zz2ej3jC2d7KoXUAGosslk5DZpJc95BXjighWif-hkvSt-k9g-X77ke2Q3oGW0fES2zi5F7TfG4ex8wtHdf2gnfSXBGIQinZ2V6orG2GE8XLySDWgoQrSYsvyQkQQciAKmaYsY2xSHI0s0atCptn7XdJRGhSYk8h6sTKg55QbLBVXD0MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوتا جوون خواستن برن جزیره لارک دیدن قایق نیست برداشتن شتر هارو انداختن تو دریا دارن میرن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69020" target="_blank">📅 19:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69019">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd02960948.mp4?token=N3j7IQZCS9LQsjNt136WDAgVlbQBlPe0hKhoUsEXmnbP7xukujCyae3uLy4CmEqDpFBwmIy5LRjPI4tywpI5BHk70e2cVMimlgARe2Dfj_qtU88G2G79_89sDU7w-PkzUPKc7dV20HlObscSRGteSyi0EmKIs2ZF7UPNAZCKB7b8yF22uicJVkhAKbLvXU0KxSj93AwpwDKo3iNr-b5c4bubxbrIYWHTqUfPqzib3suSGUGure-qYK7DjylT7LlmuVzetn9wiKsqAbanVqoMHMh3sKu-oAbetjfHgE-ZZnFgE_lSZTCowIru5jw6ILDTqQVJ88qIB1lRcSsPnxkjxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd02960948.mp4?token=N3j7IQZCS9LQsjNt136WDAgVlbQBlPe0hKhoUsEXmnbP7xukujCyae3uLy4CmEqDpFBwmIy5LRjPI4tywpI5BHk70e2cVMimlgARe2Dfj_qtU88G2G79_89sDU7w-PkzUPKc7dV20HlObscSRGteSyi0EmKIs2ZF7UPNAZCKB7b8yF22uicJVkhAKbLvXU0KxSj93AwpwDKo3iNr-b5c4bubxbrIYWHTqUfPqzib3suSGUGure-qYK7DjylT7LlmuVzetn9wiKsqAbanVqoMHMh3sKu-oAbetjfHgE-ZZnFgE_lSZTCowIru5jw6ILDTqQVJ88qIB1lRcSsPnxkjxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ویدئویی دست به دست شده با این مضمون که اگر فکر می‌کنید ترامپ واقعاً دنبال اینه مذاکره کنه با جمهوری اسلامی سخت در اشتباهید، این ویدئو رو ببینید تا متوجه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69019" target="_blank">📅 19:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69018">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=ebwraftU5jnb_ka0PxBTqFj3EUkYbY5lKtRacPV18gi1QQYvmQKTFN9hoTD6Tw6CuIdnDxJZBTSaKqDJnIYrVHxPCjayPzr_aytHxacp3L6FtDZbEk_ZzF56Gk1dErQkydozc1QGtZG7-cYljZCsfB0WgS2KdWAdT2cXSO9tXFHNxAIkSed2mKtKlDj7rJ-JQiftla6PCdcIPY8MJs27n-IPT5GPz8JvCZQWlnwvO6fYiZUfl-SG_LvEsDBlBdHpkf7PdT6vwLHP148KYxaiYjnlcWF4xMlLu-lgSdu92_TUnM0nfzEcu_gflzeJLb5XO3dvWIZ2ifNn5AuscUe6uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bca3e5bc1.mp4?token=ebwraftU5jnb_ka0PxBTqFj3EUkYbY5lKtRacPV18gi1QQYvmQKTFN9hoTD6Tw6CuIdnDxJZBTSaKqDJnIYrVHxPCjayPzr_aytHxacp3L6FtDZbEk_ZzF56Gk1dErQkydozc1QGtZG7-cYljZCsfB0WgS2KdWAdT2cXSO9tXFHNxAIkSed2mKtKlDj7rJ-JQiftla6PCdcIPY8MJs27n-IPT5GPz8JvCZQWlnwvO6fYiZUfl-SG_LvEsDBlBdHpkf7PdT6vwLHP148KYxaiYjnlcWF4xMlLu-lgSdu92_TUnM0nfzEcu_gflzeJLb5XO3dvWIZ2ifNn5AuscUe6uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
🇺🇸
مداح حکومتی خطاب به ترامپ:
"تو گوشِ کَرت اینو فرو کن، خارک‌و‌سه جزیره مال ایرانه"
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/69018" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69017">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbZGtxTKrnFEZodAIiVR9FhJMK5cj5ojhVyT8fTz67_mkbqJzt4iys1NguqaXzk4CWM1c_r7K9dFuKJ0Fbz2GWCJmiS2wRTDTWU8gsshmQPQn8ZC5FB28Tv2EYhTBVmAtB8Hi0bzxwNFFi8Nf6dbMgg16ExEs9lyRRApKQhv9AWtSjeEA61XYQWc4C64BY9WC7YcdsWyQzjQqbBeGZ-rq7KfZaWRvaEb3LX3Qc59V4qOEM0HmL20Dh_kOFGB1WPt0IYp6bfblyQjCYI8KXuKBnkv8vXme2nJb9jHehLMfF9UnFgUIVUp75dxGAaeP_IUYMeAL6mCRBHlNs5yt1PgCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇺🇸
العربیه:
- ایران به پاکستان اطلاع داد که از مذاکرات خارج نشده، بلکه مشارکت خود در آنها را به حالت تعلیق درآورده است و تمایل خود را برای از سرگیری مذاکرات در دوحه، ژنو یا اسلام آباد ابراز کرد.
ایران به میانجیگران گفت که با ایجاد مسیر جدید در تنگه هرمز موافقت نخواهد کرد و به پاکستان تأکید کرد که باید طبق یادداشت تفاهم به مذاکرات بازگردد.
ایران خواستار آن است که مذاکرات ابتدا بر تنگه هرمز، سپس بر دارایی‌های مسدود شده و در نهایت بر مسئله هسته‌ای متمرکز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69017" target="_blank">📅 17:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69016">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=lcbXSq7MqoMQPjSG-pdFwXwsuz6Fy5orJDDO1-OKeMj5Qv57IWnGsCBvUntK0PkEfRlZT5lWPOiVE9avl1vl1mSbOU0FuRahA3IQrmOeuQ-d1cBkFAdAYCENXtq7PSUMrns-Wq8VHZ7Olonq3wHIdEOTRoUAbmeRFZvi1ftDn31xturgFd4RzjYu20mptEF_PFgt5i0HhEylk2-vhJa-J-SC9sj446Q29r1E_7jAMbpE-u_57lBCJ0O8b-JllBV6cOJvxNVnxjtCPQBfRcaaPsS4oQA3OKP2X9OBPupJyoeVkj4ACJ5cCWHkV82WKGCGiddnyrB0v4HIce7b3EYQWaWN-P7_MHE4_qO0Huzw0K5FdCDkoP9y5qGyU75N8Kp8zxDDtJzWWCmUJU2YCvBtrFg8s5LgmACg89M5n5Hf3wa-yIYkav3mOT4lfPBxMVQS201UShqioVR4Plz3G6CJIY5HUMEsGtRyIJQf54oootosbBoz0VDbI2iGseXmn5_LEoRHlOxnuBZ247ZzAB2cFcoAkabU3In17YrdTo8p0LO80yuf8y93a51XwGixEiiQjCuJO1Hd_dy5UUQTp_1vqkcNpeOcvU9FKGU7xZiznvTdt_GY6YHe48c-XsiLLRpD2TPSljT52tGywwwbpGNVACg9w_9NOTwxead24bfGTl8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dcf952e60.mp4?token=lcbXSq7MqoMQPjSG-pdFwXwsuz6Fy5orJDDO1-OKeMj5Qv57IWnGsCBvUntK0PkEfRlZT5lWPOiVE9avl1vl1mSbOU0FuRahA3IQrmOeuQ-d1cBkFAdAYCENXtq7PSUMrns-Wq8VHZ7Olonq3wHIdEOTRoUAbmeRFZvi1ftDn31xturgFd4RzjYu20mptEF_PFgt5i0HhEylk2-vhJa-J-SC9sj446Q29r1E_7jAMbpE-u_57lBCJ0O8b-JllBV6cOJvxNVnxjtCPQBfRcaaPsS4oQA3OKP2X9OBPupJyoeVkj4ACJ5cCWHkV82WKGCGiddnyrB0v4HIce7b3EYQWaWN-P7_MHE4_qO0Huzw0K5FdCDkoP9y5qGyU75N8Kp8zxDDtJzWWCmUJU2YCvBtrFg8s5LgmACg89M5n5Hf3wa-yIYkav3mOT4lfPBxMVQS201UShqioVR4Plz3G6CJIY5HUMEsGtRyIJQf54oootosbBoz0VDbI2iGseXmn5_LEoRHlOxnuBZ247ZzAB2cFcoAkabU3In17YrdTo8p0LO80yuf8y93a51XwGixEiiQjCuJO1Hd_dy5UUQTp_1vqkcNpeOcvU9FKGU7xZiznvTdt_GY6YHe48c-XsiLLRpD2TPSljT52tGywwwbpGNVACg9w_9NOTwxead24bfGTl8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو رو ببینید تا از انواع بمب سنگرشکن و هسته ای اگاه بشید.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/69016" target="_blank">📅 17:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69014">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=o1t1_TjjUyBNdI7sxeM8Cm2XKuY36fSGLbYuQeX9pjsW5w_Gn5TUSyiwZ-u0n8uVc4Kq6jdCVCo42iO-JcGuhZn_b2iVS0qxg9u_nZYbAHGrOdDVs5Zc71PB3jTOJOi26f2mDdu_3dQwv1ANPke1t_Gd9KcF7wwclQf2TBJAYVwZMtuCtnEogqmoaOfV6W-g6bj-Yf80CfSyi---U-sNVZSLtz6I3-Fii1Tr1wZLKaJcIg2NAF_lVZhMMrcj1EXB0YA2xWYrtrmhETSPfzhzzZMmZCUEJlgRtU2NycIKmkxnb05Vkgpr87tUfpLDWY1xFq379hHH3lGAr87-OcrzSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ead75df70e.mp4?token=o1t1_TjjUyBNdI7sxeM8Cm2XKuY36fSGLbYuQeX9pjsW5w_Gn5TUSyiwZ-u0n8uVc4Kq6jdCVCo42iO-JcGuhZn_b2iVS0qxg9u_nZYbAHGrOdDVs5Zc71PB3jTOJOi26f2mDdu_3dQwv1ANPke1t_Gd9KcF7wwclQf2TBJAYVwZMtuCtnEogqmoaOfV6W-g6bj-Yf80CfSyi---U-sNVZSLtz6I3-Fii1Tr1wZLKaJcIg2NAF_lVZhMMrcj1EXB0YA2xWYrtrmhETSPfzhzzZMmZCUEJlgRtU2NycIKmkxnb05Vkgpr87tUfpLDWY1xFq379hHH3lGAr87-OcrzSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👑
شیوه برخورد با آخوندها در زمان رضاشاه از زبان خمینی.
رضاشاه، روحت‌شاد
👑
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69014" target="_blank">📅 16:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69013">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLycKNUKDKcRG7yTS3YYuQTyOn4PaF4wcmAcQ5VwFVx2hnrdz2p3etVNEntBS9kL4o1CrKbesqjKkkHgfMFloxjY_q0wR72u3lzMfkIU-HG59n2qmDaA6bEcn8DFR0YNsUzElwkh_kty9yj1S41i_NWtX70kERJS_vbdBY_8dtz_KvZ0nPu4hNnTW7FX0guR8Eq1JPf2lR7AcvTqDXKEhLJ4nti5OhDdKMHouKCsYGEihQ8BxlynutIZP9bUsrqa65oZix3tIO9MWKKUWNAi2m1jg_VIwphG4VDJ6q07jNum4XNfw8_RhCWVV2a_At_ydGAZayiD193Z7Mf2bTUEpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
العربیه:
آمریکا و ایران به پیشنهاد مشترک پاکستان و قطر برای ازسرگیری مذاکرات، پاسخ داده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69013" target="_blank">📅 15:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69012">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZmsBr28BtZNu87IDdUxFdZCQmTwoIG-fkRPdGk9bJlURWvRs5UzNQrSSB1VGhgroO_G6M7ACoAycRkIENv8ojgSmJVWsm4HuMPmwBHMONrHZG58NgJu7tJV4lkz77vqD1Vir8UCz4F9QC6Cipt1p69vVWw90uSdp0W0059g2Mh3SXeQX3UcRsWdGu9Et9Yp3PFJQ51REDRcL0ePrY0J4VB4hlCbV2LhqcXFZdwdMbkoAE_NFSw3sxFibRW0Wx0Q3hyZz3Hht_yqz3N59bVkd8dRFHrpSnPnZGYXN3LGxpAQXGC0ZSNPUqBwd9edwNmnPxVmYqCbSkL5Dd6RVH8FFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
امجد‌طاها روزنامه‌نگار عرب:
ترامپ حملات علیه رژیم جمهوری اسلامی را نه به دلیل مذاکرات، بلکه ظاهراً برای انتظار جهت برگزاری جلسه رهبران اسرائیل و دریافت آخرین تحولات از سوی آن‌ها، به تعویق انداخت.
این وقفه بیشتر به خریدن زمان شباهت دارد تا تغییر مسیر؛
تأخیر به معنای توقف نیست و آخر هفتهٔ پیشِ رو می‌تواند سرنوشت‌ساز باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/69012" target="_blank">📅 14:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69011">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=eKWG4d7sozfHXtMtS6NNyERKzLfMsWt7-3xmTY-YXR-78zUalK7xUOWCb633hCstE2507ESkOFjMvnHYOqRQuvOcBvMYk1UGI-sGz5uaedD-8xShlgYy39vTE1nhqX_mcbDTb7D_CCi-5HKmUsKgeMI9NSVT4oHyLNMUqBkNVEzI18U-Ha8TOl3zh7IdY6Giiesu0jcUI9T40IN6UbQBuqxlOp6FUnOJYyxDEUX-hV-NQbn9OYi8p8QVpzFIcymKbzujkfUn3-6WxNOdX_aVawtDqCS4TyVfITS_CiIaDNL8VeQ-1g6n2yP1fPpTRmKiYXF5m0bJM_tmLBDxKRDy4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3998a4eda0.mp4?token=eKWG4d7sozfHXtMtS6NNyERKzLfMsWt7-3xmTY-YXR-78zUalK7xUOWCb633hCstE2507ESkOFjMvnHYOqRQuvOcBvMYk1UGI-sGz5uaedD-8xShlgYy39vTE1nhqX_mcbDTb7D_CCi-5HKmUsKgeMI9NSVT4oHyLNMUqBkNVEzI18U-Ha8TOl3zh7IdY6Giiesu0jcUI9T40IN6UbQBuqxlOp6FUnOJYyxDEUX-hV-NQbn9OYi8p8QVpzFIcymKbzujkfUn3-6WxNOdX_aVawtDqCS4TyVfITS_CiIaDNL8VeQ-1g6n2yP1fPpTRmKiYXF5m0bJM_tmLBDxKRDy4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
فردا به دعوت پرزیدنت ترامپ به واشنگتن سفر خواهم کرد تا با او ملاقات کنم.
پس از آن، در مراسمی به افتخار یکی از دوستان بزرگ اسرائیل، سناتور لیندسی گراهام، شرکت خواهم کرد. باید بگویم که او از زمان تأسیس اسرائیل یکی از بزرگترین دوستان اسرائیل بوده است و شایسته است که این افتخار را به او بدهیم.
من با رئیس جمهور ترامپ ملاقات خواهم کرد تا در مورد تمام مسائلی که در حال حاضر در دستور کار است، از جمله وضعیت ایران، گفتگو کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69011" target="_blank">📅 14:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69008">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/al6Z9wHDTx7ZRvvoERe-dGp0X81rGI2aZ6ha_az6zZK70-kFH5Jg7p6gAtvCxLOvCSgSeEJBzB4yKQBztQHAuDWz4TQoBIKQ3S4XuOtKFSC92FGApx2tg5Vhdml_cfl64KCVJuaIOUt2XA3_dJ6He1XLsiKhAX1dsyRbpSDP2Evh8dP4E-guIGCbHusVzHFthvLTpgOJtsPNhtGrJkOcMFkTEdzSiZpIkRCW5EbbKVjhNZBB8ztnBGhpWnwzzoBGvNRdkgXTwNPfQq1sTwTh5GYJsHYewVtpRqbMqIvEE6g1tWxGx02mrBQmy0PYQXnoFOW3RW9NJnxylwGCPDV9Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/s9p5ritHFGJElNsjdsFAuS3ABeI-pjLRXfHHm701YXL9BtuR8hBl4Mt_OIjlk5K4jYF0npHYEsGOrIx19HdfJnRqIyIBsfBC3C-5siHB5u0GiLfjZvJWVaEt2rscGAJeIBriyS98sWvp7xyCcb6L-iUdAqKdnMuTgIuvy_Ucpe56Ydn9aX3aDOnRYFt7Jq470Wp5J73IdCwsqVN2f4dewcJ8naIjRkxNRFXm9gEVJdCio0oubZxqDLLEka_83Yb34cKBlbIq3XTYgwf_mpeP0Q2-mxr7eoHK0iqiBNmg4EedVMjoTfU0ImXEUuQledVDh3gv7OEXFjtVNKrJl7Hjyg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=f0Qup1yXBa8-pnYuLgtP9ow7uDIsyqshlWLlzu48Z1blBk6QkErOSEPEOvGb-_7DuQPCrMmfmJxaYmSHdMRDRmmk49xWR7Rfr_2yW_gQUSUMz_t-FvufD9QlU2a4WX2Uqaex2PxiaySSEwUkzbhsyFtmhXBdbfgTymDL1Yci94Y_yahJxhziQra911aJEmm4PSYKnVjHb7qj9IHCIsDKVPYI2KQz3Ps9l0QrCp20_j3CPlcox3aiWADwxdNE29ilji29ShUzafETtp285n0mQbxwGDnv2YY3azPhkVVJfL2KhtacGeuq-xu0LSNOWExIvXpoGEuIJuyHtMWGDiqNDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb51b8cf9a.mp4?token=f0Qup1yXBa8-pnYuLgtP9ow7uDIsyqshlWLlzu48Z1blBk6QkErOSEPEOvGb-_7DuQPCrMmfmJxaYmSHdMRDRmmk49xWR7Rfr_2yW_gQUSUMz_t-FvufD9QlU2a4WX2Uqaex2PxiaySSEwUkzbhsyFtmhXBdbfgTymDL1Yci94Y_yahJxhziQra911aJEmm4PSYKnVjHb7qj9IHCIsDKVPYI2KQz3Ps9l0QrCp20_j3CPlcox3aiWADwxdNE29ilji29ShUzafETtp285n0mQbxwGDnv2YY3azPhkVVJfL2KhtacGeuq-xu0LSNOWExIvXpoGEuIJuyHtMWGDiqNDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز ۴ ام مرداد، سالروز درگذشت رضا شاه بزرگ؛ بنیانگذار سلسله پهلویه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/69008" target="_blank">📅 13:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69007">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🇮🇷
محبی سخنگوی سپاه یه لیست از خسارت های آمریکا گفته:
⏺
در حوزه راداری و پدافندی:
۷ مرکز فرماندهی و کنترل
۳ سامانه ارتباط ماهواره‌ای
۶ رادار پدافندی پاتریوت (سامانه‌های پاتریوت به قدری ضعیف شده است که موشکها و پهپادهای ایران بدون رهگیری به هدف می‌خورند)
۳ رادار کنترل و مانیتورینگ هوایی و دریایی
۸ سامانه راداری کشف و اخطار اولیه
۷ رادار دفاع موشکی هوایی
۳ سامانه راداری EPS
۲ رادار EPS 117
۵ رادار برد بلند
۲ رادار پدافندی
۱ مجوعه راداری تاکتیکی
⏺
در حوزه پشتیبانی و لجستیک به منظور کاهش توان عملیاتی:
۶ مرکز تعمیر و نگهداری جنگنده و بالگرد
۳ مرکز پشتیانی و لجستیک
۱۲ مخزن سوخت
۱۷ انبار پشتیبانی تسلیحاتی و قطعات شناورها و هواگردها
۶ زاغه موشکی
⏺
در حوزه زیرساختهای عملیاتی:
۶ آشیانه پهپاد ام کیو ۹
یک سوله آماده سازی جنگنده اف ۱۵
یک سوله پهپادی که ۸ پهپاد آکبند در آن بود
۲ مرکز فرماندهی
یک سکوی سوخت‌گیری ناو هواپیمابر
یک آشیانه هواپیمای پی ۸
۴ سکوی موشکی هایمارس
۵ آشیانه جنگنده
۴ مجتمع پدافند پاتریوت
۶ سکوی پرتاب موشکی
یک ایستگاه پمپاژ سوخت
۲ مرکز مخابرات سیگنالی
یک مرکز داده‌های اطلاعاتی
یک مرکز هوش مصنوعی، پایگاه مرکز پردازش داده مربوط به شرکت آمازون
یک مرکز دپوی شمپاد (شناور مدیریت‌پذیر از دور)
یک اسکله سوخت
۴ شلتر جنگنده
۶ رمپ پرواز و توقف
⏺
در حوزه عملیات هوایی:
۱۱ هواپیمای جنگنده و بالگرد (روی زمین)
۱۷ پهپاد شناساییی و عملیاتی (۸ تا آکبند بودند)
یک هواپیمای جنگنده اف ۱۵ داخل شلتر
یک هواپیمای پی ۸
یک هواپیمای ترابری سی ۱۷
۸ هواپیمای سوخت رسان
۴ بالگرد سنگین
۶ موشک ذخیره
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/69007" target="_blank">📅 13:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69006">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⏺
🇮🇷
بقایی، سخنگوی وزارت خارجه جمهوری اسلامی:
مقامات ایران و عمان در تهران گفتگوهای سازنده‌ای درباره تنگه هرمز انجام دادند و رایزنی‌های فنی و سیاسی در این خصوص همچنان ادامه دارد.
چندین دور گفتگو در روزهای جمعه و شنبه در سطح معاونان وزرای امور خارجه برگزار شد. در شرایط کنونی، هیچ تغییری در تردد کشتیرانی در تنگه هرمز ایجاد نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/69006" target="_blank">📅 12:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69005">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
ویدیوی تعجب انگیز از داخل هواپیمای یاک-۵۲ که در آن تیراندازِ صندلی عقبِ اوکراینی، از کابینِ روباز با استفاده از تفنگ خود، پهپادهای گران (Geran) روسیه را سرنگون می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/news_hut/69005" target="_blank">📅 11:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69004">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=aEF37n-GaflSr5kbHBgJFyEPZCNBILPkEZ75UcnkCuidDeg4y_2LCtrOv3uPH3KWs5EoXhClJCwwFd9L-Bg1YqbXcjGC2BYZf8y66hidLTW6swAk4sX5ld8ZE1Y_QbZfcgAsPE6wndbVy9dWzxRsV4NjjB9rSHqGjMEX7V9Kw3405hrvvVI5ijp9LTucm6MK9QLdl1MWjB-AW6ye1mg5JBMeFXkSttl9FhhiA8I8OQC01i_AwDHAOoOGV1yNxvDIBdE_2g6iBH4Z8Dh2mh3cbOfY3b-ugqhMCsubItJqg0iG1GcP1btMXT8yKQiwEEAUXPFuQxo2PydRxQ9xgSxiqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/739d5c9e05.mp4?token=aEF37n-GaflSr5kbHBgJFyEPZCNBILPkEZ75UcnkCuidDeg4y_2LCtrOv3uPH3KWs5EoXhClJCwwFd9L-Bg1YqbXcjGC2BYZf8y66hidLTW6swAk4sX5ld8ZE1Y_QbZfcgAsPE6wndbVy9dWzxRsV4NjjB9rSHqGjMEX7V9Kw3405hrvvVI5ijp9LTucm6MK9QLdl1MWjB-AW6ye1mg5JBMeFXkSttl9FhhiA8I8OQC01i_AwDHAOoOGV1yNxvDIBdE_2g6iBH4Z8Dh2mh3cbOfY3b-ugqhMCsubItJqg0iG1GcP1btMXT8yKQiwEEAUXPFuQxo2PydRxQ9xgSxiqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
اکبراعلمی: مزد خدا بود و پاداش الهی بود که مجتبی انتخاب شد
😐
خدا امسال سه ماه قبل از قدیر ؛ قدیر رو برای ما نهادینه کرد و خدا برای ما مجتبی انتخاب کرد.
شهادت میدم والله خدا انتخاب کرد مجتبی رو.
با این انتخاب خدا کاری کرد نه نام خامنه ای نه راه خامنه ای تعطیل نشود‌.
@News_Hut</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/news_hut/69004" target="_blank">📅 10:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69003">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=WP6hio5ThQ7bwpc-umCXYqfPTsamTFaaRiho6xAL_74HLSw51t2zmEB_ypY_ZUNSVY9AFdAMZ69uo5lbKKXDz9ytY9rLUQ6KsQM1WdSGa07DkD2punl-mCsiaqtImoyHIrY10XXSOuTA0lvbhj8tbexyxbITnT_26P_G8ujMLmgIaBd_Hmtdm8AG9QF9He63FlDi6U5G6Md2QaExEzAe7rjwFZtxUVcdlggOnmtnLPiddC4fPkrRbhZf0nTj90eYI1hWlB56YaBtDVmQ3GuiVyi76eX_IdqrgAkg1zjc6vb1Q7TLOuEOUy3z7j45pKGNhrMWLFislTUH4MDwl-rrhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1efc7d4c9e.mp4?token=WP6hio5ThQ7bwpc-umCXYqfPTsamTFaaRiho6xAL_74HLSw51t2zmEB_ypY_ZUNSVY9AFdAMZ69uo5lbKKXDz9ytY9rLUQ6KsQM1WdSGa07DkD2punl-mCsiaqtImoyHIrY10XXSOuTA0lvbhj8tbexyxbITnT_26P_G8ujMLmgIaBd_Hmtdm8AG9QF9He63FlDi6U5G6Md2QaExEzAe7rjwFZtxUVcdlggOnmtnLPiddC4fPkrRbhZf0nTj90eYI1hWlB56YaBtDVmQ3GuiVyi76eX_IdqrgAkg1zjc6vb1Q7TLOuEOUy3z7j45pKGNhrMWLFislTUH4MDwl-rrhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبل از مرگ خاطرات آدم میاد جلو چشماش
من موقع مُردن:
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/69003" target="_blank">📅 10:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69002">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GmHpjcwRoXWf1GBkGD77rld8pDrtt1EA7MkupWRMN3XqmtBTN81eEvKAdfg4YgROo-zdff9fgZHL0XK9xs0qGTMeDAQH3j6aO-HL1K80Wr5wndpwKhOimd_YSNVFFvsMQpgS8h-xUsNauqWFF2B69rkR1jkLvVhTS9mMhwYOComTZmjQAids-2sM1Q2EaYz7zv4eSM3xDJRpm7RWfidYAYcNU4_yBp-3ChCip1YgDLDYtb3wPMdxFeOXz8w26rzzNRGYLbHvFmLFBdJjil6iTErjAcO00tJpjg4ftN49ZYRIWL8sLyjuXgflnH1LUQEwCFCiK_Mo5IYZAS1Y65RsEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
نیویورک پست:آمریکا طرحی را برای ربودن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایران بررسی می‌کند.
نیروهای عملیات ویژه آمریکا در حال آماده‌باش هستند تا «پیچیده‌ترین عملیات تاریخ نظامی» را برای تصاحب اورانیوم غنی‌شده ایران از تأسیسات هسته‌ای به‌شدت مستحکم‌شده، به اجرا درآورند.
جوزف راجرز، معاون مرکز مطالعات استراتژیک و بین‌المللی، گفت: «گفتنش برایم ناخوشایند است، اما فکر می‌کنم محتمل‌ترین راه برای خلاص شدن از شر مواد هسته‌ای ایران — دست‌کم آنچه اکنون در اختیار دارند — یک عملیات نظامی است؛ زیرا مذاکرات پیشرفت سریعی ندارند.»
یک منبع آگاه از برنامه‌ریزی نظامی روز جمعه به واشنگتن پست گفت: این عملیات بسیار پیچیده شامل هزاران نیروی زمینی خواهد بود که به تأسیسات هسته‌ای ایران حمله می‌کنند - از تله‌های انفجاری عبور می‌کنند، از خدمه ساختمانی استفاده می‌کنند و یک نیروی دفاعی بزرگ را در اطراف این سایت‌ها حفظ می‌کنند.
به گفته آن فرد، از آنجا یک تیم کوچک از نیروهای عملیات ویژه، عملیات واقعیِ بازیابی را انجام می‌دادند؛ فرآیندی که «بسیار خطرناک» توصیف شده است.
این یک عملیات لجستیکی سنگین و دشوار در یک محیط رقابتی خواهد بود. ارتش ایران کاملاً نابود شده است، اما آنها هنوز از افرادی که از مادورو محافظت می‌کردند، پیشرفته‌تر هستند.
بر اساس گزارش رسانه مستقل و مطلع «های ساید» (The High Side)، این گروه از نیروهای عملیات ویژه می‌تواند شامل «اسکادران نقره‌ای» (Silver Squadron) از تیم ۶ یگان ویژه نیروی دریایی (SEAL Team 6)، گردان دوم تکاوران (Ranger Battalion) و گروهان ۲۱ مهمات ارتش باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/69002" target="_blank">📅 09:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69001">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N01Z5TPWtq6sIhRSpULQaYPtoHrwSzHLJBO4DnDLfkr4fzVcsvs1L-KHYHXOnBhZWD0RRp3O-d-cQjfO6uIILqRoYczj-bZ5hTTdfhRDqoEKwYjHdQDV8W9eKxNngAkjkq-SBRNm533ayQ2bQrlEBpVCtJau61vSq3QBXhAIZo_3Vw8qPOVX_tph_wF9qGH6AiIGy0KZVI4h2t187RHQH0eZL7Zj-MvDAnXvJET-uZxqaN6akQZY-nMm_-B-NzqwPVgGGxvWKJ0tfX724FZtQWui0bhuu81MohqdJpkN1uweEBhqbzCb0hvEG7auP7bixNqOVJ6-39QUyD4xvAa7qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
رادیو و تلویزیون اسرائیل:
با وجود تعویق حمله آمریکا به ایران در روز جمعه، روند پیوسته ورود هواپیماها و تسلیحات آمریکایی به اسرائیل همچنان ادامه دارد.
آمادگی‌های نظامی آمریکا، حتی پس از لغو حمله برنامه‌ریزی‌شده برای شب گذشته، همچنان در جریان است. این تقویت قوای نظامی، بخشی از تلاش گسترده‌تر آمریکا برای حفظ فشار و در عین حال، تلاش برای بازگشت به میز مذاکره محسوب می‌شود.
در حال حاضر، حدود ۹۰ فروند هواپیمای سوخت‌رسان هوایی به همراه یک اسکادران از جنگنده‌ها در اسرائیل مستقر هستند. طی روزهای اخیر، محموله‌های تسلیحاتی و موشک‌های رهگیر بیشتری نیز وارد شده‌اند که یادآور تدارکات و آمادگی‌های پیشین است.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69001" target="_blank">📅 02:34 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-69000">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eae9373361.mp4?token=PvLdgZ-8fOmB5r19zjPOVaCvhUx_BUx5-MiD34613VsVd9aOG5IIwAHpG0smVCDt4fmXNvjZkhmaVfZHvGnIg_OshUZ1PoORf-_Y-Pdkfj9e8PwHwqkTeXveMwfJ9dGumZlXoA9nZaKpwDStDtnoWFYc7i93tFS9fmdVZXct17QzEQgDx8Y1V_5rViIGbFf1Y35mTNnuYbbW3a5zfvOmTDzRUTIMJQyP2vuzwnHMyiQ_PyLivUOBh05e_Uci1ZCsWK4Rmm2ZuzY4oGkcLegRcLVFDLZiR79BxYe4KN4jGndyRBNlcCZnF3uMLx-j7oLqDpuPPVXNBmfxl_tt4QjqrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eae9373361.mp4?token=PvLdgZ-8fOmB5r19zjPOVaCvhUx_BUx5-MiD34613VsVd9aOG5IIwAHpG0smVCDt4fmXNvjZkhmaVfZHvGnIg_OshUZ1PoORf-_Y-Pdkfj9e8PwHwqkTeXveMwfJ9dGumZlXoA9nZaKpwDStDtnoWFYc7i93tFS9fmdVZXct17QzEQgDx8Y1V_5rViIGbFf1Y35mTNnuYbbW3a5zfvOmTDzRUTIMJQyP2vuzwnHMyiQ_PyLivUOBh05e_Uci1ZCsWK4Rmm2ZuzY4oGkcLegRcLVFDLZiR79BxYe4KN4jGndyRBNlcCZnF3uMLx-j7oLqDpuPPVXNBmfxl_tt4QjqrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو خاورمیانه همه دارن هر شب در هم میذارن.
🇮🇷
واکنش عباس داوینچی:
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/69000" target="_blank">📅 02:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68999">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=M90ZEtYttntyZRDOfqI_lDIzMFwYMWOJzAbAXd-HguY4sBWLt777GG4f8yzj3P8C7XNEK-Mpd3Ws71SSRmKwDtpBUKIrWDmKx3syeYioj73aMqMLulmQ3YLBImUyyh1jUEDZwnrb51ZyY1P5VkLzJJJE6CsXdUpNTJM3IRZUNclt5Qb1-J8YU84rNcnyBEKhi25MLTz4348l1g7PvJ1tfAWAtJpnQqWz1yM6KCVot_vzb8ImtIm7a96X6GKGYuiJfLlc4JuFKkGtjsRfzN7wVD_IKZ4cwF0i-0aM2YEV0E2ZrrCMa857495EXL9oLi7-gjujIltLq3JDCiBC-Z0feQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c262408b6b.mp4?token=M90ZEtYttntyZRDOfqI_lDIzMFwYMWOJzAbAXd-HguY4sBWLt777GG4f8yzj3P8C7XNEK-Mpd3Ws71SSRmKwDtpBUKIrWDmKx3syeYioj73aMqMLulmQ3YLBImUyyh1jUEDZwnrb51ZyY1P5VkLzJJJE6CsXdUpNTJM3IRZUNclt5Qb1-J8YU84rNcnyBEKhi25MLTz4348l1g7PvJ1tfAWAtJpnQqWz1yM6KCVot_vzb8ImtIm7a96X6GKGYuiJfLlc4JuFKkGtjsRfzN7wVD_IKZ4cwF0i-0aM2YEV0E2ZrrCMa857495EXL9oLi7-gjujIltLq3JDCiBC-Z0feQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
فرماندهی مرکزی ایالات متحده:
محاصره دریایی ایران توسط ایالات متحده همچنان با تمام قوا در حال اجراست. تا تاریخ ۲۵ ژوئیه، فرماندهی مرکزی ایالات متحده (سنتکام) مسیر ۱۲ کشتی تجاری را که قصد عبور از این محاصره را داشتند تغییر داده، ۲ کشتی را که از دستورات پیروی نکردند از کار انداخته و برای اطمینان از رعایت کامل مقررات، وارد عرشه ۲ کشتی دیگر شده است.
پیش‌تر در روز جاری، نیروهای آمریکایی عملیات بازرسی و تأیید وضعیت را بر روی نفتکش «چارمینار» (Charminar) با پرچم کومور در دریای عرب به انجام رساندند و این نفتکش اکنون به مسیر خود ادامه می‌دهد.
نیروهای سنتکام در تاریخ ۲۴ ژوئیه، نفتکش «لاوین» (Lavine) با پرچم موزامبیک را در دریای عمان از کار انداختند؛ این اقدام پس از آن صورت گرفت که خدمه کشتی چندین بار تلاش کردند محاصره را نقض کنند و هشدارهای مکرر را نادیده گرفتند. این کشتی دیگر به سمت ایران حرکت نمی‌کند.
نیروهای آمریکایی همچنان بسیار هوشیار، متمرکز، مرگبار و آماده هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/news_hut/68999" target="_blank">📅 01:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68998">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cdb9t9T9ofzNfg_AfEzCk_iKcnJfSgKAkgDpljyZg7RNs6LmpouD5D6BF2dN22Fm0A72cZoISZc0LRjLV1pVQ4tF1CkhjePXF-WYc7dhz1_DYTHudxnoXtyh0DUaWfw6jPu46rF15ig0jqY2Ja6TvCWSUsV7uhwmfRRkaEz4XBfdMAwXIC3UioRYBIoERa7M3pi_nRu-1OlCOPu3VjZ-_UADePvh1qxV81YF3lA0jQljrsfJlFq4OzC-qmzIqhxzjRjzWtzZMmHzqq9sel30SgqKPlMRfjOYZBzTNE7aWCNPMD9fLiHZOg3sHpYFaDPl1rw7XYOhoxdxtvf1s2pnoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۷ فروند هواپیمای سوخت‌رسان آمریکایی هم‌اکنون بر فراز خاورمیانه در حال پرواز هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/news_hut/68998" target="_blank">📅 00:45 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68997">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
اوکراین، یک کشتی متعلق به جمهوری اسلامی را در دریای خزر هدف قرار داد!
تاکنون مرگ یک ملوان در این حمله تایید می‌شود، رئیس جمهور اوکراین می‌گوید این کشتی حامل محموله نظامی بود.
@News_Hut</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/news_hut/68997" target="_blank">📅 23:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68996">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=eZQ1GG-SLIF1R-9AmeE5pVCT-ZGg-R6G7vX7R6b4C25VrE42fzYUaI_qIwZPqkqM_dRO0oaUriGY8-8ilsESBIB-TzLx8lJ8ZETe1Mnaqj2_Dxp5a1QXwfsMJw-lvsg2-ol1jIhZOsSrPn1NeI2SMy6x9q0sZwL4Sovd1Qr1nk-7V9hhnq73VWKJY3tYOHcqmdxqGMy1Ud7753DQcYOn2DStPrS0ctRfc3YeFxy8hECfdB_iDVC4lDb_kpU0MQVdDHGXlCCKp6Luk0GeoRDuU7eOeAhwWshq_BPwDS9JQu1AKsQeMWNYmjnuEJdvTCisQX9qf6K9kpMjZcOExWN5zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0101d071e9.mp4?token=eZQ1GG-SLIF1R-9AmeE5pVCT-ZGg-R6G7vX7R6b4C25VrE42fzYUaI_qIwZPqkqM_dRO0oaUriGY8-8ilsESBIB-TzLx8lJ8ZETe1Mnaqj2_Dxp5a1QXwfsMJw-lvsg2-ol1jIhZOsSrPn1NeI2SMy6x9q0sZwL4Sovd1Qr1nk-7V9hhnq73VWKJY3tYOHcqmdxqGMy1Ud7753DQcYOn2DStPrS0ctRfc3YeFxy8hECfdB_iDVC4lDb_kpU0MQVdDHGXlCCKp6Luk0GeoRDuU7eOeAhwWshq_BPwDS9JQu1AKsQeMWNYmjnuEJdvTCisQX9qf6K9kpMjZcOExWN5zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
پیروزمند:
تا کی قراره ایشون ( مجتبی خامنه‌ای) بیرون نیاد؟
🎙
مجری:
تا نابودی کامل عوامل جنگ.
⏺
پیروزمند:
خب اینطوری شاید ده سال دیگه طول کشید خب ما تا کی اماممونو نبینیم؟ اینطوری همیشه در موضع ضعف میمونیم.
@News_Hut</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/news_hut/68996" target="_blank">📅 22:50 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68995">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlRkHqSelH3zHB2BqGcXAQ-4R4trrNZq8bWQEVOY-VD2xWMiByKquzGDXOil4hy0p1mUa9B6z87EWCq5E1yBfxbRreO0pFVqgrRZIqhYTCOOOlSRRuVbbQLipDbgaj7JTrkt0_MpgxtJqre74p3kUBSQxqSYWtJcivrvkwuw2OfFgLGk2vo4U9BJMJGeruUz09iSFZBW879rCD6EkON2NZcY5OSIA7rawL7xW6Z47ZS1EvODt87Yd9OzD2lN92MrOxrkKPjCK2zbTb4juxaw-N0J8a1KSP6AgeDE2pLGT81gbga0CQfBQMgiJxMg3J9TOYKI5nmq00Y7qWW0RGn2LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ در گفتگوی تلفنی با شبکه فرانسوی «ال‌سی‌آی» (LCI):
اگر «صددرصدِ آنچه را می‌خواهیم به دست نیاوریم»، «قطعاً» گزینه ازسرگیری جنگ تمام‌عیار علیه ایران را مد نظر دارم.
@News_Hut</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/news_hut/68995" target="_blank">📅 21:48 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68994">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BtMNkRw4_fTEmuyhOxuWAkztDkhVuhd4Fl6JyRx4lF0IVy_xC7hkNuV9CV_TnRMcvRwucJVfE6O3ILYyg4059Fw97cJGqlSiDp1orAjOxj-AkvpBIKWktuSzJHQ3nBtt09spZpdt0s35EBJ_kWllTZYZzz5-iNys-WaJ4aGA7i7l8I6QgpiXA-x-glKW-cxxx6SGhYyzRhGndOIrCJa6Hjc3RNoUo6FguW_zvO0q-2_FJ7-vdq2VsK0hdvlmy_kKvqqw5gmQ3_SIKBu22GlSl88WkIx629-TCb-eB9V4y1PDIhkcllya5Wace1p3c2lUD4kkCofQqTnhOCbKKLgwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
اکسیوس:
رئیس جمهور ترامپ روز جمعه به ارتش ایالات متحده دستور داد حملات به ایران را متوقف کند و به تقریباً دو هفته حملات روزانه پایان داد.
این تصمیم در حالی گرفته شد که مقامات عمانی در تهران مذاکراتی داشتند و گزارش‌ها حاکی از پیشرفت در جهت توافق احتمالی برای بازگشایی تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/news_hut/68994" target="_blank">📅 21:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68992">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzKnBdtzydQ7R5RlfhtWBlz1p0Ry5dpX-LRuMgfSATpamK9nNQQ9kWJp_iY12fp9qX7MsSND3vYSRsghX5ytfyRsPREpP8E4N7DslmxiDIQmUQuNl3BJ7dgdLC7bdzxtL__DCyBGLRDp-I3wbTRhg8N9uSVw4LZNqis19B8K9pjrVrd7JfIZEl-RvEWz_k8y6_ov38_HKsDFnCjc2HGsYJuNa9WakKmvWcYnICCu_y5v_lfCPEpNP_4EV6agIZlAsFcPGh4h6GZBaqquQVfae4W79TdChQezfZjoL74b8My5cOy9m5TK-A1VuxQudbZVEcDyy5OSYqDheS-qd-sChg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=C7aTELvvvBjK_c45wijfamuzbqDpPjymFD1uhvpT0zT2nvB_7F6m3bHFpciVEjLkyP5vpQEWoIe-HDGPySpqJmGiBJz-BOFypZnwouADvVqHtuqH7f_Yn_kSeLwaevxQKSU9fpYBq1IL3W8m3pwTxjvcKafTtAtq6aIz-apHTqACIvPvataLSt0bRuaKuZXtYsqLiVdOnIATZl_DjpWxCk_zZPu_mfieV9-x-TzwpY12BCM-8gZDTAX92pOVW9psJKO4uhx6OihmLAf0bkHiZMDfUP8z_mc5t4dNUPUsxdQ_V7BkAA84mDb_zdoT6JFfN7gOwAK8XF15S2RwC9qpGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d601f15a28.mp4?token=C7aTELvvvBjK_c45wijfamuzbqDpPjymFD1uhvpT0zT2nvB_7F6m3bHFpciVEjLkyP5vpQEWoIe-HDGPySpqJmGiBJz-BOFypZnwouADvVqHtuqH7f_Yn_kSeLwaevxQKSU9fpYBq1IL3W8m3pwTxjvcKafTtAtq6aIz-apHTqACIvPvataLSt0bRuaKuZXtYsqLiVdOnIATZl_DjpWxCk_zZPu_mfieV9-x-TzwpY12BCM-8gZDTAX92pOVW9psJKO4uhx6OihmLAf0bkHiZMDfUP8z_mc5t4dNUPUsxdQ_V7BkAA84mDb_zdoT6JFfN7gOwAK8XF15S2RwC9qpGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ساعاتی پیش یک هواپیمای آمریکایی در فرودگاه جده فرود آمده است. به نظر می‌رسد این هواپیما یک هواپیمای آواکس مدل E-3Sentryباشد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/news_hut/68992" target="_blank">📅 20:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68991">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9BHiuj_muMJuFyT_RCjKI-0wbTyw41RqIG70Id7Fw555Wx1Y6wpZXEEALi68myf766vsHEsMZND-9ZRrsNTJIw5L6ZldwLKksfwb4iZPRW2_FORIrdcn2B5PIoL4mmms45tJZwNGPk4PNepnVFt6akioX2f5-oVlLcF8te3bp0i16JEnMscZjFmMDEpVb9TdogH7L-Wp_zRTDK_0VN9TcuZmfHnN02iIlcvWMWUPTZrSEAquH72kHHLCf5R8wJmHFfdtJuNeE9_y3yLR7IRZLciIE_Z7-a1s3IaYKq0GUAq53_eWmNSQm_khfkR6bEXdPMkgPuCSfx7FwabrgxURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⏺
باراک راوید، اکسیوس:
آمریکایی‌ها دیروز برای عملیاتی گسترده‌تر در ایران آماده نشده بودند، بلکه برای حمله‌ای تدارک دیده بودند که از نظر وسعت، مشابه حملاتی بود که هر شب در طول دو هفتهٔ گذشته انجام می‌شد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/news_hut/68991" target="_blank">📅 19:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68987">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4bab692977.mp4?token=nPWaP-d8Ub49zoqdIVNE0orOnyQ7D76wQXIneATEZVxbhzfOhLAsfZRlp9C8l5ilaYRjM1n4u92Y4L4LOXmBxxx7Mot_V9Ad4NmmjlcHwDXgq53qWxbXFAOOJku1S9BXG6l5B2DzAKWlmf3LKvoQCe09Zu5CDM7gcdk1lxXj1OJLxxUOs4ScGtYOocIZY5IFenRxTfAtGiZTNsQI-SMEuFaGfTiVkPWzX4DIlSREARPuJ21OdDa9lwafOSvbYzPWz6z7KV8UV7BC852sga5BcqHQd9M9PBvp6e3mNFDuAtkWTl2qSliDLDPfr-pMF9Z2BJpKxJGu9VA-61vQGCUnmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4bab692977.mp4?token=nPWaP-d8Ub49zoqdIVNE0orOnyQ7D76wQXIneATEZVxbhzfOhLAsfZRlp9C8l5ilaYRjM1n4u92Y4L4LOXmBxxx7Mot_V9Ad4NmmjlcHwDXgq53qWxbXFAOOJku1S9BXG6l5B2DzAKWlmf3LKvoQCe09Zu5CDM7gcdk1lxXj1OJLxxUOs4ScGtYOocIZY5IFenRxTfAtGiZTNsQI-SMEuFaGfTiVkPWzX4DIlSREARPuJ21OdDa9lwafOSvbYzPWz6z7KV8UV7BC852sga5BcqHQd9M9PBvp6e3mNFDuAtkWTl2qSliDLDPfr-pMF9Z2BJpKxJGu9VA-61vQGCUnmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلنج شکن معروف اینستاگرام که هر چی داف بود میاورد پیش خودش و نالشون رو درمیاورد دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/news_hut/68987" target="_blank">📅 19:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68986">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=TC5NT-4WhDL0ISfnMuVS3wOZJnu7YVE6arVhV8sfhnKrfIFs_QW4vgU4pgN8Q4Nwh59gthp2FUkwViGy7kvufuij49AED3IJcU8vg6s98XV9fmdL5E_uCTo5UMdVrHan90cKwc-VZvSKSSs3TfQ8dlOBnOtREmEWvDkyzMhDb29oGmR0xt42fV-s_01Y3zeGyWd45nzy9mIs4ERm74K7lOwtLawUergQXtqA3B8Kk4xeY93Z4fkPWgD5xKf7R5QdMZ78OJ3aR_5MGL28Ab1EUJEbyCqZfixy0BHWXFr0fLD1tzS3DWv085pGXTOq5rtHT0qGmIg4Rb7zC4s8H72yIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bef5afefe.mp4?token=TC5NT-4WhDL0ISfnMuVS3wOZJnu7YVE6arVhV8sfhnKrfIFs_QW4vgU4pgN8Q4Nwh59gthp2FUkwViGy7kvufuij49AED3IJcU8vg6s98XV9fmdL5E_uCTo5UMdVrHan90cKwc-VZvSKSSs3TfQ8dlOBnOtREmEWvDkyzMhDb29oGmR0xt42fV-s_01Y3zeGyWd45nzy9mIs4ERm74K7lOwtLawUergQXtqA3B8Kk4xeY93Z4fkPWgD5xKf7R5QdMZ78OJ3aR_5MGL28Ab1EUJEbyCqZfixy0BHWXFr0fLD1tzS3DWv085pGXTOq5rtHT0qGmIg4Rb7zC4s8H72yIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
تیم‌شی‌هی سناتور آمریکایی:
جمهوری اسلامی گروهی افراطی و تروریست هست که 47ساله کشور رو تصرف کرده و ایدئولوژی نفرت انگیز خودش رو گسترش میده.
این رژیم اهمیتی به سیاست های حزبی یا اینکه به چه کسی رای داده‌اید نمیدهد.
آنها میخواهد همه ما را بکشند.
ما این جنگ را شروع نکردیم، اما تمامش خواهیم کرد.
حملات موشکی پراکنده به کشتی ها یا تحرک قایق ها در تنگه‌هرمز نشانه قدرت نظامی نیست بلکه دست‌و‌پا زدن یک حکومت در حال سقوط است.
@News_Hut</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/news_hut/68986" target="_blank">📅 18:56 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68985">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmVKLsXYQ4yRcld0_9lHKaReNz6IKejShGox9DavPOS-NJR-4QSaxIUv8pebRgT6pgfOwF0quVPWVMX9CquJRLc2hnoV1Z1dqCP8FJoBCvInhoJYHh6sy6T8ZHIuM0X6rarDI8m5ZanwJI0ov05Zw_hpdgREpLNHX9GRM2Nld0adygZmx9nOV3tTDD8jqdtnbKqO8WF8HbR4kEePg1qLjzMATd9uLNEIckfJCqclHDD4ec2vtCHWp1MumCCfvBOuEsATWXxBaRqm3u7TylxhH3iC3EC-Lgl743K2eBTBjFoU1evRZQ2mtLFqS_hGyMAIvEWx8QFQFzLhCi3y5bCa5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
وای‌نت:اسرائیل انتظار داشت که ترامپ دیشب ایران را بمباران کند، اما در نهایت از اقدام علیه تهران صرف‌نظر کرد.
اسرائیل روز گذشته را در حالت آماده‌باش برای یک حمله بزرگ آمریکایی سپری کرد و انتظار وقوع آن را در طول شب داشت؛ اما سپس متوجه شد که ترامپ در حال عقب‌نشینی و دادن فرصتی دیگر به تهران است.
قطر و عمان فشارهای سنگینی بر ایران وارد کرده بودند تا پیش از وقوع حمله‌ای که تقریباً قطعی به نظر می‌رسید، کوتاه بیاید. برای نخستین بار طی ۱۳ شب گذشته، ایالات متحده هیچ‌گونه حمله‌ای گزارش نکرد.
یک منبع اسرائیلی وضعیت را این‌گونه توصیف کرد: ترامپ تمایلی به حمله ندارد و تنها به این دلیل به سمت آن متمایل شده که احساس می‌کند دیگر گزینه‌ای پیش رو ندارد.
ارزیابی اسرائیل تغییری نکرده است: احتمال دستیابی به توافقی واقعی صفر است و تهران تنها موفق شده برای خود زمان بخرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68985" target="_blank">📅 18:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68984">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=HrL0VQta26-GFJFTvJkhpF_-PToWHdz3H4AqM8M8Yq2vCHSLma5dz4mOgVHmKa6gPgIIGeu8xXx7FaPGI9fczJ-KiWan-L-uzAMcoLi0cWBiEymKMlDFlcn2zLOt5trjPoGAFFtkxCzMpv_uuMWY4bJO1pgR6YGz8YBKztby5I_yKKIy3xQLrPJ4uTdrRpVf3h9Wbq0Co0XA7vXuyGX0to-L82ogkQxswSsbFoxZy7_d357ltpMOLO5HxykcBwn3j8uX5XzgbU4pZfkuv0ZLziPB71Rt-oMcaV-wFPkDv6xIqhu_2XnEj4OpmXS2CcIWTfwx-uRSjj8m_LQoABg_Bg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c910168c.mp4?token=HrL0VQta26-GFJFTvJkhpF_-PToWHdz3H4AqM8M8Yq2vCHSLma5dz4mOgVHmKa6gPgIIGeu8xXx7FaPGI9fczJ-KiWan-L-uzAMcoLi0cWBiEymKMlDFlcn2zLOt5trjPoGAFFtkxCzMpv_uuMWY4bJO1pgR6YGz8YBKztby5I_yKKIy3xQLrPJ4uTdrRpVf3h9Wbq0Co0XA7vXuyGX0to-L82ogkQxswSsbFoxZy7_d357ltpMOLO5HxykcBwn3j8uX5XzgbU4pZfkuv0ZLziPB71Rt-oMcaV-wFPkDv6xIqhu_2XnEj4OpmXS2CcIWTfwx-uRSjj8m_LQoABg_Bg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فارس با انتشار این ویدیو:
مردم جاسک، اسلحه‌ به‌ دست منتظر اومدنِ نیروهای آمریکایی هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68984" target="_blank">📅 17:29 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68983">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=hc9UdCb1i46vkfDI8q2TeamiNj41ZDZ9f1tL8xYj0Qri_SElJhiRMNbgTxeepdzdYWDiLQgc0YQlDPvZHdkiYv0FLNDf_MBUgMrntbPDr3ljabEPZ6vVt2qQ3903dGv4IYSJv4quCarmEe2bfaLekALX5DCyRw8sQSGKfqeAKkV-0vsclaIePK0S1yMaN72d8dWbdy5OWLhMZHZfwlaJ408OmwjiHo1cAf6m6TNksZsTaSRfTQLZKNdi0lRk3I44OKhRFa29ptiP370x3z5Kf4pUSQQ383nlecq5ukLX434Q9LttdHMMWmg8-Ab6N4sAe3OmJUVkNpeA2MJsUvDmiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3b976f59.mp4?token=hc9UdCb1i46vkfDI8q2TeamiNj41ZDZ9f1tL8xYj0Qri_SElJhiRMNbgTxeepdzdYWDiLQgc0YQlDPvZHdkiYv0FLNDf_MBUgMrntbPDr3ljabEPZ6vVt2qQ3903dGv4IYSJv4quCarmEe2bfaLekALX5DCyRw8sQSGKfqeAKkV-0vsclaIePK0S1yMaN72d8dWbdy5OWLhMZHZfwlaJ408OmwjiHo1cAf6m6TNksZsTaSRfTQLZKNdi0lRk3I44OKhRFa29ptiP370x3z5Kf4pUSQQ383nlecq5ukLX434Q9LttdHMMWmg8-Ab6N4sAe3OmJUVkNpeA2MJsUvDmiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی از طرفداران حکومت، با انتشار این کلیپ آمادگی خودشو جهت
مبارزه زمینی
با آمریکایی‌ها به رخ کشید
@News_Hut</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/news_hut/68983" target="_blank">📅 16:55 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68982">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">⏺
🇾🇪
بیانیه نیروهای حوثی:
در پاسخ به تجاوز آشکار و جنایتکارانه عربستان سعودی، نیروهای مسلح یمن دو عملیات نظامی دقیق و موفقیت‌آمیز انجام دادند. عملیات نخست، با استفاده از ده‌ها فروند موشک بالستیک و پهپاد، تأسیسات حساس شرکت آرامکو در جیزان را هدف قرار داد.
عملیات دوم نیز با بهره‌گیری از تعدادی موشک بالستیک و کروز و همچنین پهپاد، تأسیسات حساس شرکت آرامکو در ینبع را هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/68982" target="_blank">📅 16:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68981">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=MpHAAVtdP_pnptrcfGXBJnf80bXYNuy-oouvBL7RYoWE-whygf_JjMLG4wT9qRjXJCix7-GtUM_sY0BE49xH2vxnNRADD_zLht7T6Uy6iPeXqcBF_PugmCzfJE515jNyV-tlJIf48YEPbwNm5n-49o4avybCndlb6raro-Jz1HNoAAxSLyn-R9PqUrcmit9eYZt1mOQelUHRqykMKfQOoOSdDhtMFgG7uLCgTZ2JM-aK6zl1quZOde2bSjzqKajfRU8jRPe_wQhTOKZhZEp-pfGXiq-aM9nNnb17J7pjUu1Gpmj5RRToCJZxfn5sYpRUwoD2wW-ewpUtXpLsvrUhQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e90df6b87.mp4?token=MpHAAVtdP_pnptrcfGXBJnf80bXYNuy-oouvBL7RYoWE-whygf_JjMLG4wT9qRjXJCix7-GtUM_sY0BE49xH2vxnNRADD_zLht7T6Uy6iPeXqcBF_PugmCzfJE515jNyV-tlJIf48YEPbwNm5n-49o4avybCndlb6raro-Jz1HNoAAxSLyn-R9PqUrcmit9eYZt1mOQelUHRqykMKfQOoOSdDhtMFgG7uLCgTZ2JM-aK6zl1quZOde2bSjzqKajfRU8jRPe_wQhTOKZhZEp-pfGXiq-aM9nNnb17J7pjUu1Gpmj5RRToCJZxfn5sYpRUwoD2wW-ewpUtXpLsvrUhQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صحبتای دیروز پزشکیان که تا به بحث مذاکرات رسید صداوسیما سانسورش کرد:
بعد از جنگ 12 روزه، علی خامنه‌ای رسما اعلام کرد که ما دیگه با آمریکا گفتگو نمیکنیم و صداسیما هم اعلام کرد.
یه روز رفتم پیش علی خامنه‌ای و گفتم خودتون گفتید نه جنگ - نه صلح، حالا ما چکار کنیم؟ گفتش که برید مذاکره کنید و ما به دستور علی خامنه‌ای گفتگو با آمریکا رو شروع کردیم.
تو آخرین پیامش هم گفتش که برید مشکل رو حل کنید چون تو حالتِ نه جنگ - نه صلح نمیشه کاری کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68981" target="_blank">📅 15:35 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68980">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=HtAGmqOp3LH18DO-UWhr8rPc678_v6Mnhe_TzJsG9D5_CKaHtTsaD8iK976sGe5A3ju24MGFSZSSOrgszNfCP0nEtI4hRpXqQ-QXVf2bKCUXPfiufVs2ybseLUwpk_GQ4SdJLW7Z7MBfBxkDgqeU9XBRN2CAF4jfxDRgF5P4FaX0FNDdvWTtyCuGEQ1CCnmLRV8vdaN2FWXtKh-KoMj6Xmh1zpdXQktwk0D8M5ZlsSB0C-GMSrTZaHExUh1Z2gBpN9tCZU1ZjdGuXpMayQMiJ8XUfMaCTgO-AD-Mv1XYzqjJ6mu_BETznEgNciK4fG5rjJ-FZ3XRcLMeqZiLaE-79g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0e5554ef4.mp4?token=HtAGmqOp3LH18DO-UWhr8rPc678_v6Mnhe_TzJsG9D5_CKaHtTsaD8iK976sGe5A3ju24MGFSZSSOrgszNfCP0nEtI4hRpXqQ-QXVf2bKCUXPfiufVs2ybseLUwpk_GQ4SdJLW7Z7MBfBxkDgqeU9XBRN2CAF4jfxDRgF5P4FaX0FNDdvWTtyCuGEQ1CCnmLRV8vdaN2FWXtKh-KoMj6Xmh1zpdXQktwk0D8M5ZlsSB0C-GMSrTZaHExUh1Z2gBpN9tCZU1ZjdGuXpMayQMiJ8XUfMaCTgO-AD-Mv1XYzqjJ6mu_BETznEgNciK4fG5rjJ-FZ3XRcLMeqZiLaE-79g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروهی از طرفدارهای حکومت با مقوا عکس رهبران ارشد نظام درست کردن و اومدن تو خیابون
😳
@News_Hut</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/news_hut/68980" target="_blank">📅 15:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68979">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=Qzsu0c6IqJiSZucPt1koylJO9TrJd2nTJzWgVcmHYjmMT192hjxPxau9L_6fCEiS0O_xnRSGnbWadR7_toozuCC8CqfsFnhUTHkbrUomirgqfm2fAzmfzJ_Nd0UrZeiiSBQnf84Ro62ywzW0YK-UpPGQJ3PRr0SbY8n8kkTrPNGxS3uSVyZ8Mr-4De33vC5FG2Q3WNUiZkvUpqUIyxdpW46i25Zwl1E9PoowjwGMpXX8hMi8kLCXN9YCTliKnqkORyBKEo2XMytzHKZ6lWkeXwWnfVoTZfynFztIjptAVSlEewNy5HkC2bg_jvmaIYlu6etpBtYlmMoL2gVl3TCJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93bb8b04cd.mp4?token=Qzsu0c6IqJiSZucPt1koylJO9TrJd2nTJzWgVcmHYjmMT192hjxPxau9L_6fCEiS0O_xnRSGnbWadR7_toozuCC8CqfsFnhUTHkbrUomirgqfm2fAzmfzJ_Nd0UrZeiiSBQnf84Ro62ywzW0YK-UpPGQJ3PRr0SbY8n8kkTrPNGxS3uSVyZ8Mr-4De33vC5FG2Q3WNUiZkvUpqUIyxdpW46i25Zwl1E9PoowjwGMpXX8hMi8kLCXN9YCTliKnqkORyBKEo2XMytzHKZ6lWkeXwWnfVoTZfynFztIjptAVSlEewNy5HkC2bg_jvmaIYlu6etpBtYlmMoL2gVl3TCJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تغییر قیمت یا سهمیه بنزین قطعی است.ما علاقه‌مند به افزایش قیمت هستیم!
@News_Hut</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/news_hut/68979" target="_blank">📅 14:14 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-68978">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/glpgNTU5y5Gw6X374lm3hVXvszdw_usZ0KjV66N7PzwqecCHbQV5myHzbGd5B9obVghTXAjjUp-x1Uq6U77Fm_q45sYS09oJ1LCSfG3wQMaHzM16W2TvkGzZUcqRVnKwEz_UReJFO-ZOe5D0ta125K-aA1khNmyzh_j_CqYwL-eYhwevVEwhs_ts8uQ6FQuf8mx0rbAbC5TwSRABXQD1bCy70eWhwHyNmO7Ls2XIt9Fzn1i1lRo_LQ0bT0g-1QY6f-LyP__MrpMffP6RUdd-FSdgelcfs45b9rQG6K0sMJ8CFIlPDTiXlYiviJFUVBeuU56IHVYaZj8x6dBFA5PG9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقچی:
در پی حوادث تنگه هرمز، طی مذاکرات سوئیس تصمیم گرفتیم برای جلوگیری از سوءتفاهم‌ها، یک خط ارتباطی مستقیم ایجاد کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/news_hut/68978" target="_blank">📅 13:30 · 03 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
