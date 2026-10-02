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
<img src="https://cdn4.telesco.pe/file/Q5Nx13nVKqasMosJi2mG6wDrE9levHdQiWiZ8Bf7Q_UVUMyQ_fTzwUBWIvmnnUdu8GMAxH_9PdxSi5p7Bid3EwcqpUxf-qy6Vf466aPKv5ikdFLrPf4Vt5zzR_lIS9U7d0Mj_0QZY5iUMj_hp7vfw7yXuZLW7_or8D_6_N04sZgfBeCO3H-ni_C5en4G38aQPpG6C7P6r2X0XWswWLOdbXjp5AqN6AGTzNevyxDEsslF1VpR9-cCArnrvDDG-EiqkWUadLRrh-n7KD65DzJbqajgC-uQj2MMiJWT4PxK07ekUByF1UQdLLRYASfMNR3K-pOgbGmF6Nf9h0PIQqxVXA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 12:14:42</div>
<hr>

<div class="tg-post" id="msg-150548">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z84jKeXMJRfoD2fsX7ji5d85rQ7vYhYS-aajvV3Mh6flyoBi1cQB0IS_7PWkQDUxhdKRbxcwLnsR31JWFAQ8lIWGjOgzh7T6LdTfs5_keLVTQtffELGOJd_0gJnY_slt7-sK-fiHBaisX5O8dTqpsGq-VFOwlv1AaI27HzJiZ2UvzAu-162_WOsGqeKkdXzxWkirPPTjE2VPNM6jfmCP8YR1y4E_DLYFrcXhCYhmTbSHo3Z0_5eBrdW7mjZhHG84GzBeroREp6_brrBUNihJwOYsYuNzq15UuTEvMRm6GpXHNqojVfX9mI2-KErCnM1aJ9uttfSi7Aqp2-187aEAUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
در اغتشاشات و کودتای فرانسه تاکنون هیچ کسی کشته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/alonews/150548" target="_blank">📅 12:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150547">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/219d012c04.mp4?token=C2KM9NvddSQ2ixIyIop6ogsnrsWWA4f2CWlns6qGXUZVfhnqcD7sFSWfG5-w3bvlWaq3XKX8oY01Qm0FvdH9ZtoQGbgmy4sHrQnUQgwId6JxUnFd0Ka6ssRAOeunZKmY2swEGBi-8j7JrddV6dy-bEZZSNoZ0z6jbildFVzVgk4gN-AX8huJS2yn3POXvDSNBIrSB5ksgfkI9-Zzt0qgoWLDujhy6YefqWNOdNJA1nzN2HIEGZeNgWeYHgN6nKKTSNGlZuLMTJedEqair5G-OjXzMVsTWM91pD2bX9WbGCH6H7lYNLgzjSP_-ALGvEbBFhStg2xRPyl0g7Xmw1CBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/219d012c04.mp4?token=C2KM9NvddSQ2ixIyIop6ogsnrsWWA4f2CWlns6qGXUZVfhnqcD7sFSWfG5-w3bvlWaq3XKX8oY01Qm0FvdH9ZtoQGbgmy4sHrQnUQgwId6JxUnFd0Ka6ssRAOeunZKmY2swEGBi-8j7JrddV6dy-bEZZSNoZ0z6jbildFVzVgk4gN-AX8huJS2yn3POXvDSNBIrSB5ksgfkI9-Zzt0qgoWLDujhy6YefqWNOdNJA1nzN2HIEGZeNgWeYHgN6nKKTSNGlZuLMTJedEqair5G-OjXzMVsTWM91pD2bX9WbGCH6H7lYNLgzjSP_-ALGvEbBFhStg2xRPyl0g7Xmw1CBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دلار هم اکنون 259,900 تومان
✅
@AloNews</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/alonews/150547" target="_blank">📅 12:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150546">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnlfXLQMpbBF0Dur27mDR1-TClqHOJkD27zzyv-qUeY0WIJPMK_YxbrKEvhpjHaUdREajTRsl_NYilDCsonJy2w4u8UkW-C5HzwYrFV0EKongA5merPhjiPIwGIBbWHHnA1s9KYb1XN_r5yQlAzNalsRvEKOgO73FNpF5XmTNHYnyB4F1Lq0ohJ7wtxTtxFTqqHEWzhGYabezsWO_w3IvZxZo-QpdIvrFidZJtCY-I9tJsXNRzYyiwgIrwHSVtvMCqjyjQLL0mPTvwCGOyyq4opcjKIm5kZDK2WRpcQ_VN91j9THOIf4WdjReZ8sAmQCNsCQIcKGaY3LTEJh_lmYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین دوباره ۸۶,۰۰۰ دلار را پس گرفت و در تنها ۶۰ دقیقه، ۱۲۰ میلیون دلار از پوزیشن‌های شورت لیکویید شد. در همین بازه، ۴۰ میلیارد دلار به ارزش بازار کریپتو افزوده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/alonews/150546" target="_blank">📅 12:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150545">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بزرگ‌ترین خریدار LNG جهان: انتظار نداریم LNG قطر به این زودی به بازار بازگردد
🔴
فعالان بازار نگران زمستان پیش رو هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/150545" target="_blank">📅 11:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150544">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=b7DiUYyaUXZoGXChUYADgq-75gwqnkbPD8FgEqlAhxMdkGySzqo7snu3EniOspIqcoA3VNVlCQZAVrJznls_Xhke_HeWoZCFGJnWK2fKuiyl6oKakAj3eN6NGJ8VaMcNSwNv8m2o_ClpHdFLuFR7QGU3IHx4p8fkFPrE7KY2gTnDK4NQ4YdYfP3hdpbpvD_LdqQCCgKXDO74QftYbjWmmauTg5OYChkDPSjlZBAJc14HOBMMagRjQEbR77uabQ09M7h6vu9Lo4uHR-gxOYMAygot68MDaN1ygf8jZNypDmDO0a1qAVCaBZx3Cv5GmoCIAoo3cCFVAUAvG4sOTX8Hhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8bbc2f536.mp4?token=b7DiUYyaUXZoGXChUYADgq-75gwqnkbPD8FgEqlAhxMdkGySzqo7snu3EniOspIqcoA3VNVlCQZAVrJznls_Xhke_HeWoZCFGJnWK2fKuiyl6oKakAj3eN6NGJ8VaMcNSwNv8m2o_ClpHdFLuFR7QGU3IHx4p8fkFPrE7KY2gTnDK4NQ4YdYfP3hdpbpvD_LdqQCCgKXDO74QftYbjWmmauTg5OYChkDPSjlZBAJc14HOBMMagRjQEbR77uabQ09M7h6vu9Lo4uHR-gxOYMAygot68MDaN1ygf8jZNypDmDO0a1qAVCaBZx3Cv5GmoCIAoo3cCFVAUAvG4sOTX8Hhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ونس: وقتی به پرونده‌های منتشرشده اپستین نگاه می‌کنید، فقط یک چیز کاملاً روشن است: بله، این دونالد ترامپ بود که جفری اپستین را به پلیس محلی معرفی کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/alonews/150544" target="_blank">📅 11:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150543">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC0QJlLjzttiD2sUB79HHxOKNI5NzYh4G3hz9o3g0juvwYhViuYaYT4lxdAG-VvZ9peCOgu_u88WmBGCasytOz0imL_6JzXo2c1qpbOpI8kDKjfipBP3B_YS8-42oHie7JX_5W0heqgnjn9GyCP3IH1t9L7rqo0ZwmqpxqRe_W5Bcf3K5kD6Tb_lMv8cxgCBsLfN5rq521K2U4I4kpeOXrnv4yiMNTJf01_lvvETqbtpDyzdJfzRUtBEwQ9XGhR00pMWvbbODa6ouszp0V6SdoUe6nfkNTbRdFscgCFryviXrA1GI1MY0Ge3wpx_UdjKaVmo7Vx6_5xOnCCd-l9XuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جکسون هینکل: سفر مخفیانه نتانیاهو به امارات مقدمه‌ای برای جنگ روز قیامت علیه ایران بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150543" target="_blank">📅 11:46 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150542">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=kRWssItUgRAOh7PEfxHV1gzUOlKEYhY9UqzCD8Q8novXcIqDFD1-rxUuzvaGdRONoWCQSEPH146BMY4FEec26AGc_-Twk55T0dnKnX7M0QcJnVPUtYx0-1LSKo_-uA9emlutu0mwWYJrk7l5bQtqn7wCQo6nePlBzLrARvKcJc2bBNpm_2sDYWYfwREGolyjsYRJbfNhPToQd2q8Ji8i-O_ESi9JTnRKpdgTHPaKwQn7ve8_ns8NS5whGeKKpQzwrk8yGnV3QHMuO03cQL5EJSmk6CJyqjjet1LDKItJiW7T_PFDvKwNr6LvhblgySEuRMRV9KbR30siz1rZkqigpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148764d5c.mp4?token=kRWssItUgRAOh7PEfxHV1gzUOlKEYhY9UqzCD8Q8novXcIqDFD1-rxUuzvaGdRONoWCQSEPH146BMY4FEec26AGc_-Twk55T0dnKnX7M0QcJnVPUtYx0-1LSKo_-uA9emlutu0mwWYJrk7l5bQtqn7wCQo6nePlBzLrARvKcJc2bBNpm_2sDYWYfwREGolyjsYRJbfNhPToQd2q8Ji8i-O_ESi9JTnRKpdgTHPaKwQn7ve8_ns8NS5whGeKKpQzwrk8yGnV3QHMuO03cQL5EJSmk6CJyqjjet1LDKItJiW7T_PFDvKwNr6LvhblgySEuRMRV9KbR30siz1rZkqigpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور برزیل: ما اکنون نفت در حاشیه استوایی کشف کرده‌ایم/ ترامپ از شدت حسادت، تلف خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/150542" target="_blank">📅 11:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150541">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
معاون فناوری وزیر ارتباطات: با این روند، در بحران بعدی مجبور می‌شویم علاوه بر اینترنت، برق را هم قطع کنیم!
🔴
به دلیل نفوذ استارلینک
✅
@AloNews</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/alonews/150541" target="_blank">📅 11:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150540">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2b8312ee49.mp4?token=dHZI-_RnPY9tH1t6RQWSqp8075d4WQSOOQuianzHthnL4N4x_nmY-LdK0mMicKOq6WbH-MwMUXcXzHpgXY8r0gaLOmXm4NNnQi31f3g5OOuGcVPQ85DFkNd_ecePS6rU26LYx02s0DF5dXRy0GMVNLdRw85cJ9BxH8BsRui539x7-avtZX4FFUHzqJrbd_oNlS3emYJqSnHoMFZGOX58ZXgbpCKlJrDxg9H7pf1OAsMsLTxvc0RHZD6PDW_asvKFh7Ji4lRBBu593Zdpt_HcO4dqlftY1EShxObIeAb9m8BQaIBCyXuRpG4u8ICB3wyzB-S-t_h_E1hwnS-mQUmJwKYRO78xGPVBtMtROVfPniXnDSlyoeJKiMgRSSHzhFsp-cRllTfpBTqic2pUIgj5ND0g_Y0dxLGM2DC1_PL1fIg1PjVFAmWalXzxJXAHsIehFBc-r5bJmXhRjFjvSZRbNx2Fe1BPBY8XhlMbsVLTqOw3vULTbBcVXGJv2Z2FKQgoyshFuFXdqSH5mR2rC5qcsb-beuo8iv5Iy7cjyPbTg5l2e3AzPzOxvm5ssHSZZ-CQP11AWRjQj4vJcWBqenfgZkmrOcQ9lpqvUeno7qn6GbMBuKArmE8dk5UhJKTpo1by5AGO2ZZYaOm-SbtGbfaYjI4yrsUV3MR9IA6kOTeN3LI" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2b8312ee49.mp4?token=dHZI-_RnPY9tH1t6RQWSqp8075d4WQSOOQuianzHthnL4N4x_nmY-LdK0mMicKOq6WbH-MwMUXcXzHpgXY8r0gaLOmXm4NNnQi31f3g5OOuGcVPQ85DFkNd_ecePS6rU26LYx02s0DF5dXRy0GMVNLdRw85cJ9BxH8BsRui539x7-avtZX4FFUHzqJrbd_oNlS3emYJqSnHoMFZGOX58ZXgbpCKlJrDxg9H7pf1OAsMsLTxvc0RHZD6PDW_asvKFh7Ji4lRBBu593Zdpt_HcO4dqlftY1EShxObIeAb9m8BQaIBCyXuRpG4u8ICB3wyzB-S-t_h_E1hwnS-mQUmJwKYRO78xGPVBtMtROVfPniXnDSlyoeJKiMgRSSHzhFsp-cRllTfpBTqic2pUIgj5ND0g_Y0dxLGM2DC1_PL1fIg1PjVFAmWalXzxJXAHsIehFBc-r5bJmXhRjFjvSZRbNx2Fe1BPBY8XhlMbsVLTqOw3vULTbBcVXGJv2Z2FKQgoyshFuFXdqSH5mR2rC5qcsb-beuo8iv5Iy7cjyPbTg5l2e3AzPzOxvm5ssHSZZ-CQP11AWRjQj4vJcWBqenfgZkmrOcQ9lpqvUeno7qn6GbMBuKArmE8dk5UhJKTpo1by5AGO2ZZYaOm-SbtGbfaYjI4yrsUV3MR9IA6kOTeN3LI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تایوان نخستین ۲ فروند از مجموع ۶۶ جنگنده F-16V Viper خریداری‌شده از آمریکا را تحویل گرفت.
🔴
این جنگنده‌ها در پایگاه هوایی چیهانگ (Chihhang) در جنوب‌شرق تایوان فرود آمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/alonews/150540" target="_blank">📅 11:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150539">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
آکسیوس: گروه آمفیبی، نیروی دریایی پیاده‌نظام و گروه اعزامی دریایی سومین گردان تفنگداران دریایی، از پایگاه دریایی سان دیگو به سمت خاورمیانه حرکت کرده‌اند.
🔴
آن‌ها حدود دوازده فروند جنگنده F-35B و همچنین حدود 2200 تفنگدار دریایی آمریکایی ویژه به همراه خودروهای جنگی پیاده‌نظام و نفربرهای زرهی را به همراه خواهند داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/alonews/150539" target="_blank">📅 11:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150538">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W7isMjVT7pg4IsiRjKDHu40udm-bqNge2Fb5ckOis3rtHBmae9SaMXnPnKm45QurGgM1CQtJvuDicYr2W6MKp-QJrFjgtiKbsUkqkC7_1kieT10GUTqs_HsJgogctxIHTx4WMfYXgsmdfkArtr1UleUMm4ngNvhnQWauRK6Oo2wOANRMyMrvI0i5Qlth8DDCkaaQIZk2Y3dp2Tf3YxjMwpRy9rAKnwJhstaoWCGM2fxTf6G91fNPAsK_0-gLMx20xn7vLx9j4YgfofrR4Lf76XTRPBYcjuIAUXJVRY9kwAkKkBN5iI0Z6Tlnfy9aFMcwXeRgLjBIZQK5Pk4McKH4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قطر: دوحه حمله حوثی‌ها به یک ایستگاه توزیع برق در مدینه را که برق مسجدالنبی و تأسیسات غیرنظامی را تأمین می‌کند، به‌شدت محکوم کرد.
🔴
قطر بار دیگر بر همبستگی کامل خود با عربستان سعودی و حمایت از اقدامات این کشور برای حفاظت از حاکمیت، امنیت و تمامیت ارضی خود تأکید کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/150538" target="_blank">📅 11:21 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150537">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYIiBrRgXYN0tz3OEzh8rBKEMfKC6BkhDRVrzMEWSy1ekd3ejFZvneo53SzACBbJxtFRbpzQzloEx-cloet7eSRguhevSSPAli96ciMYlFMiV2xJ0CyWfS22jFV3jSERkWh0n5Bj1oiFonLy6-nF2kkHNsYQMIMLcdvcuxAcA9-PccQO6cZ8_kaFMfUgbZ3jIKfxZCc4Oh6vtfIPBYL2CfrdEE7hcyYWmHRhxptAnDeeSsHrjS1po0mRBBIb7C6VQ--K2sZXPgYfrr7r9YTkbW55ZuqSnnPNSLf7-vrXJ7-njepHtTOHhG-1-CKtyBu0FYoBmzPGtXepSew1w7YfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک هواپیمای آمریکایی مدل E3، که برای شناسایی زودهنگام تهدیدات هوایی استفاده می‌شود، دقایقی پیش در آسمان شهر ریاض، پایتخت عربستان سعودی، در حال پرواز بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/150537" target="_blank">📅 11:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150536">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
لغو پروازهای شرکت «العال» اسرائیل برای بازگرداندن مسافران از دبی
🔴
خبرگزاری فرانسه گزارش شرکت هواپیمایی «العال» اسرائیل اعلام کرده است که پروازهای برنامه‌ریزی‌شده امروز برای بازگرداندن اسرائیلی‌ها از دبی را لغو کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/150536" target="_blank">📅 11:13 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150535">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
یکی از تاثیرهای بستن واردات خودرو گرون شدن خودروها بوده !!
🔴
پژو ۲۰۷ اتومات فول رو دارن ۳ میلیارد و ۶۰۰ به بالا اعلام میکنن !!
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/150535" target="_blank">📅 11:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150534">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33a884a3e7.mp4?token=Lc25ODFScD19HBS9xy0bzTFyQdvnIzm6AsR5JqtGFC-olQYRjtZ2zT5GQ0IDVmx0HUfGExOWlPKxTWUUNMe3L2y2L_eiHcljMtKjLe05--Lqle6eY3L7XCVd4Z7YjeS71eecnVU9Ddq7VG3ZQWWJ1kP6j1q4AdbhBu8TvnVhoVf11H23ueTYjb6y-70ffNVxOHjfyYs9Ced8NI259bB1KZKOBKEQZhlBrF9ivdcyD5xYX7yhLrAa9lUBOfr1bbwlnXZiH5D3gQSkjWKWHwHlzAWNgdQ7fTdO1M7jT5FyqdlcvajClXtF8donPzvRxLJ713K3MSVQtRRWRA2QvKuMZporYOlpWSxjrfAPNz6JczIU8k595Roz39fqES4FhQcAOtYR3vnor1wVzg6TPhLRAuf5Ua5FQRw7-MGQT63ilKdMuxjJjiM8CR9Td6FHQwplruvwRa-_Y9MnjROCrPar74gBcHiRHVNJuoqGVO0ZRfTFCrDnbhpF8oVLXf8HusiVfE9by9q03mWl9tr0sFqbY1PId_pbBez_La4stDQhFdE2Qpoq_r0vEBzcauvMFcEqCeVjgRqGArQvtIbxq7moopyYBpVqACB4xuR_uHL3m-qQjIe84Fg1JcQJNpTqdajKAbMiQwSeTIJtdFzPyChsTs15DSUMdwVj_X--RNAj0xY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33a884a3e7.mp4?token=Lc25ODFScD19HBS9xy0bzTFyQdvnIzm6AsR5JqtGFC-olQYRjtZ2zT5GQ0IDVmx0HUfGExOWlPKxTWUUNMe3L2y2L_eiHcljMtKjLe05--Lqle6eY3L7XCVd4Z7YjeS71eecnVU9Ddq7VG3ZQWWJ1kP6j1q4AdbhBu8TvnVhoVf11H23ueTYjb6y-70ffNVxOHjfyYs9Ced8NI259bB1KZKOBKEQZhlBrF9ivdcyD5xYX7yhLrAa9lUBOfr1bbwlnXZiH5D3gQSkjWKWHwHlzAWNgdQ7fTdO1M7jT5FyqdlcvajClXtF8donPzvRxLJ713K3MSVQtRRWRA2QvKuMZporYOlpWSxjrfAPNz6JczIU8k595Roz39fqES4FhQcAOtYR3vnor1wVzg6TPhLRAuf5Ua5FQRw7-MGQT63ilKdMuxjJjiM8CR9Td6FHQwplruvwRa-_Y9MnjROCrPar74gBcHiRHVNJuoqGVO0ZRfTFCrDnbhpF8oVLXf8HusiVfE9by9q03mWl9tr0sFqbY1PId_pbBez_La4stDQhFdE2Qpoq_r0vEBzcauvMFcEqCeVjgRqGArQvtIbxq7moopyYBpVqACB4xuR_uHL3m-qQjIe84Fg1JcQJNpTqdajKAbMiQwSeTIJtdFzPyChsTs15DSUMdwVj_X--RNAj0xY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : آنها به سمت کمونیسم می‌روند. آنها سوسیالیسم را پشت سر گذاشته‌اند. بدترین افرادی که تا به حال دیده‌ام، در حال اداره امور هستند.
🔴
اما اگر جمهوری‌خواهان در مجلس نمایندگان و سنا پیروز شوند، من به تمام شهروندان بزرگسال آمریکا، به هر نفر یک چک ۵ هزار دلاری خواهم داد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/150534" target="_blank">📅 11:09 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150533">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HXa84hH8SwrG3iEcu0Xzs2j_mepGDbV4fv19YGWtDscvBdxO_r_akZMX6OPz8PpLdtXywo7kt7iF3-Hhq47hZBiW516NhjxL9RskyhxNMIdt5r40CiMTfkmM_phNGCkzmAcaoykhYCouXy82fe4FtoeU3AyAR5Ak95GLpNyNimycoHCDDqRAIcgVp1HIY0BLmx12ZvfKJGyQ8_pBJhsl9SX2AOlacXAbhkjjJec7zYads4S1M-TNlwkDm_qE9ChoEhs39q6SYHFVCERmzF4GIo2IuN7tco_xgCBvHLAXL_6egsKAEQSL6h_YeZnGuDiOBvpGijWgZV34yxCQ2qLXU5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=plgr3y4kC4YspfhM7zsr6AF2-dr0YSHiU20V0rVnfpCRqJ0EH4i6ZaJS7q3RKOtQa-d62eFoCEAoY9_WwR-aHqo2TVPBB1gbWo0XPdI7sMPE5OTfRHNola9NNEi6OPNMhqs5sq6uDVfm1IQNUS2bK_jm-DnoA-KoPxf7PXDtKOXLUjLd2N2hGgkFzgamZXRXLCz9RC-1G9PCZYnQl16ptyTz-W_4amlsEbFeMt8R9cNjQN79ANkmzvBXVaAe0dY1ZM2KdvhdF5I4SeSc0sTQrLFYCk790Lw5omIScBc6ZVMn2w3KjKyPIzJvmDtXrf_z_bj-iqYrlyBX35H4oPF6HXa84hH8SwrG3iEcu0Xzs2j_mepGDbV4fv19YGWtDscvBdxO_r_akZMX6OPz8PpLdtXywo7kt7iF3-Hhq47hZBiW516NhjxL9RskyhxNMIdt5r40CiMTfkmM_phNGCkzmAcaoykhYCouXy82fe4FtoeU3AyAR5Ak95GLpNyNimycoHCDDqRAIcgVp1HIY0BLmx12ZvfKJGyQ8_pBJhsl9SX2AOlacXAbhkjjJec7zYads4S1M-TNlwkDm_qE9ChoEhs39q6SYHFVCERmzF4GIo2IuN7tco_xgCBvHLAXL_6egsKAEQSL6h_YeZnGuDiOBvpGijWgZV34yxCQ2qLXU5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ، رئیس‌جمهور آمریکا، درباره حملات ژوئن ۲۰۲۵ به ایران:
🔴
«آنها درگیر مواد مخدر بودند، اما در عین حال روی برنامه هسته‌ای کار می‌کردند. اما این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، به‌شدت هدف حملات قرار گرفتند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/alonews/150533" target="_blank">📅 11:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150532">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfWZu-1RFyScViHrf50tS02jq5rLitwVnHzCCvKrM0ePcjaR7wKzFcpfaxu0wcz_1NqF4RniWpH8_1kz8730MAREFK13S6sLp0Gcfw_55p1MPsBVPJDvMu0Tr6ZIWlKWVK_zEEn7y3PFCGU6bgeYaWAhyE3q8f9z4iF3o2JoLxd5QREjHcpIKOQvhzo9XnMJFO51j6gs2FOmb8UX1VxG_G05cIBBTogGfk2sNdkF-LQmLQX0gWIjxarAKjK6lZSqRH4YXkyAvjy0VYjdlf4Mk5lzJFPsY5Wn7v_vVb-Z9Gi-6ExqV0aUS-Pj7TFg-MhiHNwzLW66E5VYnejJFVZxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دولت سنگاپور برای اینکه آمار ازدواج بالا بره یه سایت همسریابی راه انداخته که فقط افراد بین ۲۱ تا ۳۵ سال می‌تونن توی این سایت ثبت‌نام کنن، این سیستم فقط یک نفرو بهتون معرفی می‌کنه تا الکی وقت‌تون تلف نشه و درگیر انتخاب‌های زیاد نشید، هر کسی رو هم انتخاب کنید و باهاش قرار بذارید، هزینه دیت اول رو دولت بهتون میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/150532" target="_blank">📅 11:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150531">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc84ea8cfb.mp4?token=FFrHCDGNYmJYlhcVKIF0ob0tt-5sVmJrPclu43FaoGz0iH7sQHXCNuZ_Xq1RPnWGCmWvOQLv0V70iJ1t1Ls-Zh1PY2yDJ-8exJQiPbY_VxmQYN5xG0NgCcxtm1r86ejyI6DvDe5zkJHMJ1N-kmUohEK5h9S5HI4ADhWJwLCIJsmYgsx-wCz9QCLF-B_2Md6V9sCkf8DQTngceaJk3zYV65z-geAyELOkOMpjGYI-GMd3LVrkrAm4dJ9thmq1UMChnILDyjkZrDeiEEBnmN_F2hFhPEsYiRHYlr2OczHFjkidlWNYyKzHsJ_VxpLpV7YwtbZOag_i0H2bOgb4gHDkSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc84ea8cfb.mp4?token=FFrHCDGNYmJYlhcVKIF0ob0tt-5sVmJrPclu43FaoGz0iH7sQHXCNuZ_Xq1RPnWGCmWvOQLv0V70iJ1t1Ls-Zh1PY2yDJ-8exJQiPbY_VxmQYN5xG0NgCcxtm1r86ejyI6DvDe5zkJHMJ1N-kmUohEK5h9S5HI4ADhWJwLCIJsmYgsx-wCz9QCLF-B_2Md6V9sCkf8DQTngceaJk3zYV65z-geAyELOkOMpjGYI-GMd3LVrkrAm4dJ9thmq1UMChnILDyjkZrDeiEEBnmN_F2hFhPEsYiRHYlr2OczHFjkidlWNYyKzHsJ_VxpLpV7YwtbZOag_i0H2bOgb4gHDkSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «ما همین حالا در عصر طلایی آمریکا هستیم. ما داغ‌ترین کشور در سراسر جهان را داریم.
🔴
ما دیگر به آن جهنمی که برای مدت طولانی در آن زندگی می‌کردیم بازنخواهیم گشت.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/150531" target="_blank">📅 10:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150530">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1cb92e856.mp4?token=DErAwM-y8_G9X2t38MJA60HwcyAdGGE9zrKZH-fAseliNWzM-jAwDLdkrrE_V5BFBSQD2gpW491DP0opAdhC25gxufZh1NpKxM6oa2fe1VkdZjQnLL8VRdIDLf-Ktu5SGrMZ0mDHsCCLi8Tuq_MO3cmMHUCiW-DDjhSt3No3ZDKm-Cx--enoCf9_o6Y1mVH20EMmOxlWx39fdu-aFfvGoGqeWyiHkFUEK2tet8YNpBR5_VgHVdPzeyMbpyVvpsULUKMUkPWlviQB5UHxJg_4Uy-mhqy4yR3PM-DAfh7cA_MO9fv0LxYsyNGfpLNYsCf7Sth5UlgMq4Jk5_AC8fOyEmobPW0hMuwuAiqRolx58i08xRWNwFvwEEZJWQkgoz9RXZXoqytg0B4o-rI2MIb2PPLa_Bbo9xd1rNiVIzpWeQ2eqdgTrBmUA7U_C8O4QwjOHWmrXTpXcDluzMxvAK1JkVLKoxrgnrRvZtBsvbnokxTcY08WBMFQGorhD41hTQyJBqp0CGt4WCobWDpUpI1_n9wlV47PRLUpPjACYdwR9AfAeCCdeELFpLFD-u1_XIb9lmOcpt74nS_6KepejTmwIjQnvzb6QH5Qr078geqvvgMhh9WQbX2AN2xWdc31EC4uG2z57SyHEJc8Z68x8cQN0VI_4u_lCgOp7ajSrkJpS3M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1cb92e856.mp4?token=DErAwM-y8_G9X2t38MJA60HwcyAdGGE9zrKZH-fAseliNWzM-jAwDLdkrrE_V5BFBSQD2gpW491DP0opAdhC25gxufZh1NpKxM6oa2fe1VkdZjQnLL8VRdIDLf-Ktu5SGrMZ0mDHsCCLi8Tuq_MO3cmMHUCiW-DDjhSt3No3ZDKm-Cx--enoCf9_o6Y1mVH20EMmOxlWx39fdu-aFfvGoGqeWyiHkFUEK2tet8YNpBR5_VgHVdPzeyMbpyVvpsULUKMUkPWlviQB5UHxJg_4Uy-mhqy4yR3PM-DAfh7cA_MO9fv0LxYsyNGfpLNYsCf7Sth5UlgMq4Jk5_AC8fOyEmobPW0hMuwuAiqRolx58i08xRWNwFvwEEZJWQkgoz9RXZXoqytg0B4o-rI2MIb2PPLa_Bbo9xd1rNiVIzpWeQ2eqdgTrBmUA7U_C8O4QwjOHWmrXTpXcDluzMxvAK1JkVLKoxrgnrRvZtBsvbnokxTcY08WBMFQGorhD41hTQyJBqp0CGt4WCobWDpUpI1_n9wlV47PRLUpPjACYdwR9AfAeCCdeELFpLFD-u1_XIb9lmOcpt74nS_6KepejTmwIjQnvzb6QH5Qr078geqvvgMhh9WQbX2AN2xWdc31EC4uG2z57SyHEJc8Z68x8cQN0VI_4u_lCgOp7ajSrkJpS3M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من می‌گویم: «می‌دانید، تعرفه کلمه موردعلاقه من است.»
🔴
و رسانه‌ها حسابی به این موضوع واکنش نشان دادند و گفتند: «پس خدا چه؟ همسرت چه؟ خانواده‌ات چه؟ مذهب چه؟»
🔴
بنابراین حالا تعرفه را به پنجمین کلمه موردعلاقه‌ام تبدیل کرده‌ام.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/alonews/150530" target="_blank">📅 10:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150529">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb897effec.mp4?token=BYLK2vrqCsT1iMvwjgY7b7jrzg7wSmphPJl8R4kG_Sbqw1eqUajktejxRsFDYjQsUkwwN-0wdtc7Ycdzk8ujf9bT19w6xxj1HdolZ6mNq-_ffOfPx9VVzvVQ9bp3Dk8lmsHXfelWutYGkPq2ILkUP-VZDSIbz98n6atwcCEelc5aPPZ2vwuUhUKIEOzTXnvR3VkTTkheWhXnfNKIDy3_bCJaOWzwZ6YOSPYijoIkZxfcfTaxemq4XTr0nM9AdUmJBc7-On6sUb9jNOog-KOStbOZoBJMfGE7623Hdrc3mPt3pPSCDUzCuJV0ahUtGPXhz21jwkaoYW5tk4xk6vD2obk3NYY7iy5UdipxUuflwZZYTfHQeJ_1rOqVvSF90UoztszI3JPzoZZDd-dHTUeR5Yu0dNabPlEESWJ-1ptBtq-xe41hbxmKYd6pqnnuQxY6bvvwDyfwab0GsCnj2ruCylWWu8MDI9jHVxV-w5AoXeEqdD1UTUU6ZsO9dMg7wb-MfA9YdwfPfTQlPeoles2diZ0R7khqQNKL2-KF_Qzq-HOLo-_dEcqgZw3dJ2CssmCqtOHTDVSnnVEVkjtiiefwUrvlJPyg1dFFqR9GWPdAoGaVQm3g-dgFwpvm-pGXJp-XRCgP_8pwg_SGmPPZS86F5i4bsVTmCJutGIMDZHK1Lgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb897effec.mp4?token=BYLK2vrqCsT1iMvwjgY7b7jrzg7wSmphPJl8R4kG_Sbqw1eqUajktejxRsFDYjQsUkwwN-0wdtc7Ycdzk8ujf9bT19w6xxj1HdolZ6mNq-_ffOfPx9VVzvVQ9bp3Dk8lmsHXfelWutYGkPq2ILkUP-VZDSIbz98n6atwcCEelc5aPPZ2vwuUhUKIEOzTXnvR3VkTTkheWhXnfNKIDy3_bCJaOWzwZ6YOSPYijoIkZxfcfTaxemq4XTr0nM9AdUmJBc7-On6sUb9jNOog-KOStbOZoBJMfGE7623Hdrc3mPt3pPSCDUzCuJV0ahUtGPXhz21jwkaoYW5tk4xk6vD2obk3NYY7iy5UdipxUuflwZZYTfHQeJ_1rOqVvSF90UoztszI3JPzoZZDd-dHTUeR5Yu0dNabPlEESWJ-1ptBtq-xe41hbxmKYd6pqnnuQxY6bvvwDyfwab0GsCnj2ruCylWWu8MDI9jHVxV-w5AoXeEqdD1UTUU6ZsO9dMg7wb-MfA9YdwfPfTQlPeoles2diZ0R7khqQNKL2-KF_Qzq-HOLo-_dEcqgZw3dJ2CssmCqtOHTDVSnnVEVkjtiiefwUrvlJPyg1dFFqR9GWPdAoGaVQm3g-dgFwpvm-pGXJp-XRCgP_8pwg_SGmPPZS86F5i4bsVTmCJutGIMDZHK1Lgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : «ما با همه چیز برخورد کرده‌ایم. با تورم مقابله کرده‌ایم. قیمت‌ها را به‌شدت پایین آورده‌ایم. آنها این قیمت‌ها و همه این مسائل را به ما تحویل دادند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/150529" target="_blank">📅 10:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150528">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95c42cae8a.mp4?token=TjPzdjXLv0Y1ZwHzkeLb91gxFtjYVMfma1ppc69PPYHwDbjGtuh7Rg9mlqkNl57o_u_Wt3nSzVPAIIyUOP6GMNxMiEbjt-qU_VbUfMVm49uTfuaPgNgM91SieGAgnlqfWiwMw0QMUWph8fqmlGLIrg6DlGs6_lDjTO92P60qEFbjCvLyMf9lvTNKOvzVmiQXvn4MJQC5SG9haa0jvkBM0LiwNM_1WYjnobQd0AGAYTcRaeto0Hi8m7lQyFFhGuW_li5VrLILWaKXAFIOkZMVwieP2jZr4CD7jTGX9p8O8fw9cYSYgdNNI6XOR8y7nJs7_Sxwuno5jJVim202DBniykESeV8rTCJvkEOU-PQO1z9YeBVAP4uKCNiTRvxgfV7OMteqmhBjxmtkuVidD8uackT3JiCGGlg2REpOMv8LbJDsJT5wtuEc9RrxRrwPk1_xKeF2gmrTmjFhy2OaSNqScRlnH_4_fZU7OWTA0YdMScY7Kjj8Q0DSZYM___r0UU172trnUe0hTI4TY6Y9xQWn22dx5i5Kr-DoLY2j8eMTcTpIcTR6UCW2SpkPNuGe9bTUlxH1ppAcdWJz62xnNMiUO8y2wg_V8utaQzUTJl0-HN060Z8u3QyHTauMlpJozAXWc07SCuwGDkUxJZ9oDaN2eLdUtKUX82KGMs3D2AL1rLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95c42cae8a.mp4?token=TjPzdjXLv0Y1ZwHzkeLb91gxFtjYVMfma1ppc69PPYHwDbjGtuh7Rg9mlqkNl57o_u_Wt3nSzVPAIIyUOP6GMNxMiEbjt-qU_VbUfMVm49uTfuaPgNgM91SieGAgnlqfWiwMw0QMUWph8fqmlGLIrg6DlGs6_lDjTO92P60qEFbjCvLyMf9lvTNKOvzVmiQXvn4MJQC5SG9haa0jvkBM0LiwNM_1WYjnobQd0AGAYTcRaeto0Hi8m7lQyFFhGuW_li5VrLILWaKXAFIOkZMVwieP2jZr4CD7jTGX9p8O8fw9cYSYgdNNI6XOR8y7nJs7_Sxwuno5jJVim202DBniykESeV8rTCJvkEOU-PQO1z9YeBVAP4uKCNiTRvxgfV7OMteqmhBjxmtkuVidD8uackT3JiCGGlg2REpOMv8LbJDsJT5wtuEc9RrxRrwPk1_xKeF2gmrTmjFhy2OaSNqScRlnH_4_fZU7OWTA0YdMScY7Kjj8Q0DSZYM___r0UU172trnUe0hTI4TY6Y9xQWn22dx5i5Kr-DoLY2j8eMTcTpIcTR6UCW2SpkPNuGe9bTUlxH1ppAcdWJz62xnNMiUO8y2wg_V8utaQzUTJl0-HN060Z8u3QyHTauMlpJozAXWc07SCuwGDkUxJZ9oDaN2eLdUtKUX82KGMs3D2AL1rLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ، رئیس‌جمهور آمریکا: «لطفاً فرض کنید من هم در انتخابات شرکت می‌کنم. فقط فرض کنید، چون نام من روی برگه رأی است.
🔴
اگر پیروز نشویم، در نهایت من را استیضاح خواهند کرد.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/150528" target="_blank">📅 10:57 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150527">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
کرملین: برای مسکو، توقف ارسال مهمات و سوخت به اوکراین از طریق دریای سیاه، مسئله‌ای مهم است
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/150527" target="_blank">📅 10:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150526">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
«شاید چیزی که بیش از همه به آن افتخار می‌کنم، همین آمار مربوط به فقر باشد.
🔴
وقتی درباره نرخ‌های تاریخیِ پایین فقر صحبت می‌کنید، یعنی افرادی که در خانواده‌هایی شبیه خانواده من بزرگ شده‌اند، فرصتی برای دستیابی به رؤیای آمریکایی پیدا می‌کنند.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/150526" target="_blank">📅 10:34 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150525">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا:
«تحت رهبری دونالد ترامپ، آمریکایی‌ها سرانجام واقعاً پول بیشتری در جیب خود نگه می‌دارند؛ بیش از آنچه دولت و تورم از آنها می‌گیرند.»
🔴
حالا بعضی‌ها خواهند گفت که هنوز کارهای بسیار زیادی برای انجام دادن باقی مانده است. البته که همین‌طور است.
🔴
بایدن ما را در وضعیت بسیار بدی قرار داد، اما ما پیشرفت‌های زیادی داشته‌ایم و اگر به تلاش خود ادامه دهیم، می‌توانیم پیشرفت‌های بسیار بیشتری داشته باشیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/alonews/150525" target="_blank">📅 10:32 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150524">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc3bfa2209.mp4?token=He6HFk9ldvKIFfh_NKlhGwnWDQ7VSL0sHMXldnU3z02PNQUu2Anp3Sus6xf988qdl-BOxoteqWy7MDFDh_4NO2AXi0-JoDyUJe17kUWCWMrZSRMOUHroH2RNk8x30fnJvs01QPiQJaQXjkkLwc1TcQSoRC-QkiQQGNwrVqzMUgJRvYMMFBOg7T8lRov5gRY1tcKAid6NcltpNj5vK0RMFAo4cuzcEp2q2R8H7kZzHt425cBzrmmpxWuNBzlpVGwS59aT-HhdHIjCGXyyOabOYXAsUSeR0dzxZZa1PBSQaK9p3VArjmLZuI_ke5imB4F-mzm2omoXI6m_BXLz2w_JOZefGTZlcknTKDn_GAYAU4Y1lPhYepoh5vWUoGfcI2kiif_aEU6b-91an9vGoIBTKQ201zTqCQNWAin_ReSqJ10fkqpo9ToPQAeCncp6wm1d1zKoXuhezeq3UANmjK7ye0bRwRjzgtlby0hccE_PD44FbMmy2nFWOBZzBkMZRsV-kA-2mjDMoGziRItAN9ZVavziV6RAS05lDv8FpIGYN4iSdCK7TN1LopFt3rTyJYsQJ1vy5-_ibPZaj2rTbsM0vI4BWDL7p_xwcCV5_wndkwo3oI7CEtQWqS-HlRsmVtYijVL4sJOsW-2U0jxAw16Z51XCBP8g1oNU-RaWMHNTPAY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc3bfa2209.mp4?token=He6HFk9ldvKIFfh_NKlhGwnWDQ7VSL0sHMXldnU3z02PNQUu2Anp3Sus6xf988qdl-BOxoteqWy7MDFDh_4NO2AXi0-JoDyUJe17kUWCWMrZSRMOUHroH2RNk8x30fnJvs01QPiQJaQXjkkLwc1TcQSoRC-QkiQQGNwrVqzMUgJRvYMMFBOg7T8lRov5gRY1tcKAid6NcltpNj5vK0RMFAo4cuzcEp2q2R8H7kZzHt425cBzrmmpxWuNBzlpVGwS59aT-HhdHIjCGXyyOabOYXAsUSeR0dzxZZa1PBSQaK9p3VArjmLZuI_ke5imB4F-mzm2omoXI6m_BXLz2w_JOZefGTZlcknTKDn_GAYAU4Y1lPhYepoh5vWUoGfcI2kiif_aEU6b-91an9vGoIBTKQ201zTqCQNWAin_ReSqJ10fkqpo9ToPQAeCncp6wm1d1zKoXuhezeq3UANmjK7ye0bRwRjzgtlby0hccE_PD44FbMmy2nFWOBZzBkMZRsV-kA-2mjDMoGziRItAN9ZVavziV6RAS05lDv8FpIGYN4iSdCK7TN1LopFt3rTyJYsQJ1vy5-_ibPZaj2rTbsM0vI4BWDL7p_xwcCV5_wndkwo3oI7CEtQWqS-HlRsmVtYijVL4sJOsW-2U0jxAw16Z51XCBP8g1oNU-RaWMHNTPAY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس، معاون رئیس‌جمهور آمریکا
:
«الان وقت آن نیست که بخواهیم درباره
همه مسائل کوچک و جزئی گلایه کنیم
.
🔴
ما باید کارهای بیشتری انجام دهیم؛ به همین دلیل لازم است دو سال دیگر به ما فرصت بدهید تا بتوانیم نتایج و دستاوردهای بیشتری برای مردم آمریکا رقم بزنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150524" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150523">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
ترامپ: قبل از دستگیری مادورو از هوش مصنوعی مشورت گرفته بودم
✅
@AloNews</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/alonews/150523" target="_blank">📅 10:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150522">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13f5adc6d9.mp4?token=F9o5wZyh0IBhIPba8xftAuvYKJdteHx925dMZ5TWu-r5n6t4GwKKZ4T3-4xjo0itlfWKDSurSgKQFBcKGhVlURaurKoz0H_Vp_2rRJeoaInbK91U88qHXD1sfrXTZy0Ax0a1lcVGyMHbkcT-Nu5R7YqXMRZZFjDOamJXweUoiHUKL7rA4x7ejixKSsPkdxTKUmur3YU7BFfPh4ed8vDaHqFtTmHOQcFo0bj4-XOEDoS1gJRhr4BGomfNuQdWs4INaBrTT5jxldoNDExSwt8zqxSExL6QyDRgiDEBX173nZUMoSYVItDbLjHpowSHNk19BMSWT7DSVFg9zr728aMjdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13f5adc6d9.mp4?token=F9o5wZyh0IBhIPba8xftAuvYKJdteHx925dMZ5TWu-r5n6t4GwKKZ4T3-4xjo0itlfWKDSurSgKQFBcKGhVlURaurKoz0H_Vp_2rRJeoaInbK91U88qHXD1sfrXTZy0Ax0a1lcVGyMHbkcT-Nu5R7YqXMRZZFjDOamJXweUoiHUKL7rA4x7ejixKSsPkdxTKUmur3YU7BFfPh4ed8vDaHqFtTmHOQcFo0bj4-XOEDoS1gJRhr4BGomfNuQdWs4INaBrTT5jxldoNDExSwt8zqxSExL6QyDRgiDEBX173nZUMoSYVItDbLjHpowSHNk19BMSWT7DSVFg9zr728aMjdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک انفجار نامشخص در فرودگاه تفناز در حومه شرقی ادلب، سوریه، رخ داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/alonews/150522" target="_blank">📅 10:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150521">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKpFwqVshtdkm7dxthIu5vYCpG0ODGPUzA7Dwg2Lf5GM98H2iY2TIXEZ7pr5v84Jpp0XoQcKdMkIzYoP02lHIqDzyiTna7bkg241KaKZ0MPjeDvsF3s5pe8MnE4GwxFY4BiTFQb0xV7IzYm6v6Nu-Ob1NU5YepbP6jVW9wQ04JRrrywBU0TU5PK4DUiKEh7rs-Re6abCerBc6kyuFPWSfjebT2KBeF9XrHEqWgp1euM7LL9l-dn-WwnMdOR0ppXuZkDJDyedpmhSfri-Cm20K6e6n29DVA57TbMLVhG4zrs1ClfYy7uJjoRL8LGh95WlhIrd1N3NhmB1fBE2Y8YvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک آتش‌سوزی در نزدیکی سواحل عمان مشاهده شد، که احتمالاً مربوط به یک کشتی هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/150521" target="_blank">📅 10:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150520">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8147803e67.mp4?token=ufbpfD3LkFIY7aEz8IcueOrtLfJG7jPkJsU-ol-jqv_7qaoqvleTKYtlzpeBWbsMlYbfGl8yaM93lxsHUFvxDQxcm3vHPsk7pcC_DeeLJGJ_B4qaI1o3BSLWlYhRcaRIEDiXySacS-ZZO4f9q5L0tTC8_9y31BH32Vexhg7IFFpoL67uDZGFePzs6IZZVpwlM5sk3PtjBu2obGTz-gKpyFSuiPVk_IVL1yzoPAq0OJbwM20PzAGL87pD0F_tzIXPwFVQfkFaY9GrvOLZnIhYVNCMAem3yQefb6NgePNPD7brKLjLrQ5YUp2xk5erxdz24edtcyg_NX76QQnYYkywG6QCVNNgkYUOK8KB5z82sYrag06IQTnrMueXH0Wx8o_vxp25ozQJPctiZsFP9U7XjFXzKLIzPGse_YoRHLahAYmvff_L45LZuMwKqYl1yTv0G03cbnEab03nKnLhGRQSiE-eZIl81DbRrYs6WLrqL6m0ecYVAtPbHWv7FzZs5U4YPgVdW4jaME4knaWSN7ZP4fb8Y78ZeNz1uvOWrE0cH2rLpigdri-wFiebWDbU8SqJiikgqWynFG-Rkl1idFkINQbGQHIdbXNES4_8ptP9JUXDIwA6T9jmV9sZQLNJpx4wrecTUDcjl_UFQdqZUf0NZWD7K1EE5_iT4hapLvYVETk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8147803e67.mp4?token=ufbpfD3LkFIY7aEz8IcueOrtLfJG7jPkJsU-ol-jqv_7qaoqvleTKYtlzpeBWbsMlYbfGl8yaM93lxsHUFvxDQxcm3vHPsk7pcC_DeeLJGJ_B4qaI1o3BSLWlYhRcaRIEDiXySacS-ZZO4f9q5L0tTC8_9y31BH32Vexhg7IFFpoL67uDZGFePzs6IZZVpwlM5sk3PtjBu2obGTz-gKpyFSuiPVk_IVL1yzoPAq0OJbwM20PzAGL87pD0F_tzIXPwFVQfkFaY9GrvOLZnIhYVNCMAem3yQefb6NgePNPD7brKLjLrQ5YUp2xk5erxdz24edtcyg_NX76QQnYYkywG6QCVNNgkYUOK8KB5z82sYrag06IQTnrMueXH0Wx8o_vxp25ozQJPctiZsFP9U7XjFXzKLIzPGse_YoRHLahAYmvff_L45LZuMwKqYl1yTv0G03cbnEab03nKnLhGRQSiE-eZIl81DbRrYs6WLrqL6m0ecYVAtPbHWv7FzZs5U4YPgVdW4jaME4knaWSN7ZP4fb8Y78ZeNz1uvOWrE0cH2rLpigdri-wFiebWDbU8SqJiikgqWynFG-Rkl1idFkINQbGQHIdbXNES4_8ptP9JUXDIwA6T9jmV9sZQLNJpx4wrecTUDcjl_UFQdqZUf0NZWD7K1EE5_iT4hapLvYVETk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ:پادشاه عربستان سعودی گفتند که ایالات متحده زیباترین کشور در جهان است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/150520" target="_blank">📅 09:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150519">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7f2907c5a.mp4?token=MUG0R7RK6ERYoAVzBUxzZ5Yy4Z99sDYu5T2KTOQKVnx00ZyZD8zFFT0nXy6xIIz2XnwJo2fF0jGLODPovu4CyD7FjvvDgA2-i_OKV7ryc3QfOiy-gJ_tQn41qHzFU3MlRelY84AQ49qBfBAE-XcVOEwR0sbOLbBhA6gZ86fIXT56BgzAYrAxiJkqgS02QmZsMROfGacLjYH1asgUkVaW8kxmS69d6GzSWafKczQr-60WaUxEPxRzxlXGZTgYborOluT4PAowiKV077jCCast3K0HBtY2jCxKqv8RPS7NeqsUtLio9bEBNSZ2CFQUOi7OPgwgRrEiRGrjTVFWHB8XZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7f2907c5a.mp4?token=MUG0R7RK6ERYoAVzBUxzZ5Yy4Z99sDYu5T2KTOQKVnx00ZyZD8zFFT0nXy6xIIz2XnwJo2fF0jGLODPovu4CyD7FjvvDgA2-i_OKV7ryc3QfOiy-gJ_tQn41qHzFU3MlRelY84AQ49qBfBAE-XcVOEwR0sbOLbBhA6gZ86fIXT56BgzAYrAxiJkqgS02QmZsMROfGacLjYH1asgUkVaW8kxmS69d6GzSWafKczQr-60WaUxEPxRzxlXGZTgYborOluT4PAowiKV077jCCast3K0HBtY2jCxKqv8RPS7NeqsUtLio9bEBNSZ2CFQUOi7OPgwgRrEiRGrjTVFWHB8XZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در مورد عملیات "شب پره" علیه ایران:آنها تمام بمب‌هایشان را پرتاب کردند - و این بمب‌ها مستقیماً از مسیرهای هوایی به این کارخانه‌های مواد مخدر اصابت کردند. در واقع، این کاری بود که آنها انجام می‌دادند. آنها سلاح‌های هسته‌ای داشتند و مواد مخدر قاچاق می‌کردند. آنها به شدت به این کارخانه‌های مواد مخدر، که در واقع "کارخانه‌های هسته‌ای" بودند، ضربه وارد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/150519" target="_blank">📅 09:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150518">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nBYnj02DaCOnqlGjIygHaMfyG8Iii6SjJGlUNfl8EkrTLSH9YZMHtNb3o4duAvX7EqKAZiocZwviIIT5ukq6Q1J9kS92-6ghJjGEy2s4tS_po0DCySEIiiRoPDuaT4iaWQd9DSU2rzBzdNPlCOHUg0vNMLezdLQ8fq8YDDXUgVqynzqhPdB5u9d13v7n27x6KbqvOzc_IqUGQdTQA0yZHsGjmRx0i3UuhdN4PcvR83sPmzYnZuHZaumrl-CwdRYkKvSftlAGW04UqywCxkg9hZGPp4MLe9m1iLbQKsqq-ZKZZW6i1EtdmrWi0pRSDe65tuffw0LZZa1j_cMCrZtKbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویر منتخب ماه سپتامبر رویترز |تصویری متفاوت از دیدار ترامپ و شی
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150518" target="_blank">📅 09:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150517">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXD7UvUD16ZN-FLhm_w4wgmAbWDOgqDq_pS_J_yjBEbJ15JizdebH5JI57D_7BghPbDanWrytTVtpZmlcdAQbYtVcc8LBn9wMm7UcBmoRAY6R62nn0td4WK9bftwUUJajRJzZzPFQLcFFhkzwDe6H1SuuApHRuMmxUjWxD47kl7oCB1BS6f7HSW7lLzY7oyQ0U6ahLJPuAM7NYLvu0OzJA4f7xqOim8Sm4r6v-Df6db1KLMhT9mOuJfKBaXPVGJ8pmwxVbrIGuLqm8X9mfmSF7e3ca52wopiJRMqiEU5w5hKJ_ZlYO4Gw-veBIFdzXsT4Mc6gstHjsT-S7gC8_I62w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیروهای امنیتی عربستان سعودی در مکه فردی را به اتهام ایجاد مزاحمت برای رهگذران و ایجاد رعب و وحشت بازداشت کردند.
🔴
مقام‌های سعودی اعلام کردند که نیروهای امنیتی بلافاصله به این حادثه واکنش نشان دادند
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/150517" target="_blank">📅 09:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150516">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d51a563f90.mp4?token=LC39vjds6Mb0tYqCbv2NAHsVq8MLz8Qy4XBb86U7zDo5z90t1J2tFVECSGgYIu0vbMtpBWBz4Pt-fgyN6nEITiig3J_SVrJu3ERDqKmBlHTUdZjk5OoywIeQRvfnoXahVtI2RDWQv6_DKwiJu_7Wuxw4FAC4IiizU9k2dcAj9aHxV3VcARH93MSzJlKsjwpyGkgELyn87F4Vt9keHE6zGi4EPIrjcuxCa9AEM3gp5r19foM2FNrnk9fkXNM5BKNsg3p7gKsAm0yrw-nMYmqD9bnrJP6yINj80ZfVDfluqeSrxsnoYEFqfLehc0l0k6zf5gYOADZkMqoh4grf8lLx3rcY4ieeEDuGjpCcJGaAdjX17pIpyi2GL2JvknE2K5t2xxVr0H9NHwUof-jptMKDGrbPalbNCW3eimNF4qpwTBcG-ari1MkZEav07jxoR_EIbXG42XuxA0A_qkkxw14wjuK79alOM9SDawkg4_hF9uOSA80cwoP0-qh2TMqlOasYvq49r34QMyrG5_bNuvcsPPTTCO5nmEQxRDWsvmyhRt9tzQr8s_8ujgJaMEp366hJ_ru5oD1A4dLo88VrVN332Tg3MMbrqHu0w-Gtcr2jaNP5X1quKKwyxrwJ0B6dBG3z__o6mIXYNur05iyj2NrmDHeuyMS-wKvFICPA9MkNflU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d51a563f90.mp4?token=LC39vjds6Mb0tYqCbv2NAHsVq8MLz8Qy4XBb86U7zDo5z90t1J2tFVECSGgYIu0vbMtpBWBz4Pt-fgyN6nEITiig3J_SVrJu3ERDqKmBlHTUdZjk5OoywIeQRvfnoXahVtI2RDWQv6_DKwiJu_7Wuxw4FAC4IiizU9k2dcAj9aHxV3VcARH93MSzJlKsjwpyGkgELyn87F4Vt9keHE6zGi4EPIrjcuxCa9AEM3gp5r19foM2FNrnk9fkXNM5BKNsg3p7gKsAm0yrw-nMYmqD9bnrJP6yINj80ZfVDfluqeSrxsnoYEFqfLehc0l0k6zf5gYOADZkMqoh4grf8lLx3rcY4ieeEDuGjpCcJGaAdjX17pIpyi2GL2JvknE2K5t2xxVr0H9NHwUof-jptMKDGrbPalbNCW3eimNF4qpwTBcG-ari1MkZEav07jxoR_EIbXG42XuxA0A_qkkxw14wjuK79alOM9SDawkg4_hF9uOSA80cwoP0-qh2TMqlOasYvq49r34QMyrG5_bNuvcsPPTTCO5nmEQxRDWsvmyhRt9tzQr8s_8ujgJaMEp366hJ_ru5oD1A4dLo88VrVN332Tg3MMbrqHu0w-Gtcr2jaNP5X1quKKwyxrwJ0B6dBG3z__o6mIXYNur05iyj2NrmDHeuyMS-wKvFICPA9MkNflU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دختر حمید رسایی، نماینده مجلس در تجمعات شبانه: افتخار میکنیم‌ که آقای رسایی بعنوان یک معترض به بی قانونی و دستکاری متن بیانیه مجلس و تقلیل دادن شأن مجلس به وسیله‌ای برای تطهیر یا تعمیر آبروی از دست رفته شخصی رئیس مجلس الان در زندان هستند!
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/150516" target="_blank">📅 09:25 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150515">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c89d377a6.mp4?token=JmDlfPSiAp2o9U7TW8MtsK_UuaCvrQGLdONQDHWmfGZOZYaTYuGqsnFt1mlijmy88GebuVf3bXYH0v_q64xDI_jZDnulvH-M7x3lMb1SSLQ76zUyxz9zyYEVI_cV_kuEQctqKIrpD5pv5F6McXXd2arYP71akPK46uwJ2bVL4p2gUBhShHuQNJWIa7pP_QnZBBNtCgZBcIOfby8QMcu61XhOOm67SqMgOcK_IUinVrWAXbLOHqjXhQsqPrhiJNBFyYfZxA1HlDnXKeyrTr6GMQTJiNLfhfuSdycQ4FkCBtNsw-aM9X3POSSPc4EPw3GzOfIdyV59NCMslAuPT94lQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c89d377a6.mp4?token=JmDlfPSiAp2o9U7TW8MtsK_UuaCvrQGLdONQDHWmfGZOZYaTYuGqsnFt1mlijmy88GebuVf3bXYH0v_q64xDI_jZDnulvH-M7x3lMb1SSLQ76zUyxz9zyYEVI_cV_kuEQctqKIrpD5pv5F6McXXd2arYP71akPK46uwJ2bVL4p2gUBhShHuQNJWIa7pP_QnZBBNtCgZBcIOfby8QMcu61XhOOm67SqMgOcK_IUinVrWAXbLOHqjXhQsqPrhiJNBFyYfZxA1HlDnXKeyrTr6GMQTJiNLfhfuSdycQ4FkCBtNsw-aM9X3POSSPc4EPw3GzOfIdyV59NCMslAuPT94lQoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی: «یکی از چیزهایی که به آن افتخار می‌کنم این است که ما در یهودی‌ترین شهر ایالات متحده آمریکا زندگی می‌کنیم.
🔴
هیچ فرد یهودی در شهر نیویورک مسئول اقدامات دولت اسرائیل نیست
🔴
اگر می‌خواهید کسی را پاسخگو بدانید، باید سراغ افرادی بروید که این تصمیم‌ها را می‌گیرند؛ یعنی نخست‌وزیر و دولت اسرائیل. همچنین باید نقش و مسئولیت ما به‌عنوان مالیات‌دهندگان آمریکایی را نیز در نظر گرفت، با توجه به اینکه می‌دانیم چه میزان میلیاردها دلار برای ارسال بمب‌ها هزینه کرده‌ایم و همچنان ارسال می‌کنیم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/150515" target="_blank">📅 09:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150514">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10f877c2bb.mp4?token=oEpe0RpNdTE3gFjwXNeFH7fLZlxvjdoAyZzy49AaXKMhdcOiP0vuhN1n6yq9EujY9xsChjJvwv3jA7dRpnC48JjqnTWe5kmcU-KUKJLE1ZZ2GbWPCq-H8AsGCNN3fvR1tTwBrnONn2LcHjs4FDbJl7Gb_8pUEvBPtgsVXKn-QyqhrNE2noN8-xtPkla_f2Kj7FDSAQDsX1DZaNJWyHdpSDSl9JDfjM9B3-wUI4XD3sUg_N8KS-IL-Zlz0RZ1liTj-YhsBnqx2ALf7gnFKOUkHBO2Lx1g_l2OTHrEsI4TatMqJDKiyOExEv58fatz5_-_QmhRYYLWkofmXxMt2YPg4JAJyCJWEcWskw2J_lAB11qal_IsvnxRliY5A9jiFZ8NFm45KimXflSgG6gD0-4ZitOFWuHoBbHL4dqE0ApwFHetq0lUjeLCBI9yE04ijtqR4KfJbOg0PRDWPdmR67g5GTSasaj_SUTR3UEQJN45wa72rbub-p2YD4CFNWwCN_rE_L1tKQf6LsHopz-wILGlZqFThKhg0QMRAz0JmlBGACURDY1MJ_aWi1DzNLpi1VpcfBwZ20DxLXLwV3Wi6UDvAavGE1PSnGKCGauSZx3O8qHE7h3vZNEawIbWkex5PQ0iv9NvPjFr9BqLTtoT1KECxgkWkHtuyyjqiO8V9nIYdlc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10f877c2bb.mp4?token=oEpe0RpNdTE3gFjwXNeFH7fLZlxvjdoAyZzy49AaXKMhdcOiP0vuhN1n6yq9EujY9xsChjJvwv3jA7dRpnC48JjqnTWe5kmcU-KUKJLE1ZZ2GbWPCq-H8AsGCNN3fvR1tTwBrnONn2LcHjs4FDbJl7Gb_8pUEvBPtgsVXKn-QyqhrNE2noN8-xtPkla_f2Kj7FDSAQDsX1DZaNJWyHdpSDSl9JDfjM9B3-wUI4XD3sUg_N8KS-IL-Zlz0RZ1liTj-YhsBnqx2ALf7gnFKOUkHBO2Lx1g_l2OTHrEsI4TatMqJDKiyOExEv58fatz5_-_QmhRYYLWkofmXxMt2YPg4JAJyCJWEcWskw2J_lAB11qal_IsvnxRliY5A9jiFZ8NFm45KimXflSgG6gD0-4ZitOFWuHoBbHL4dqE0ApwFHetq0lUjeLCBI9yE04ijtqR4KfJbOg0PRDWPdmR67g5GTSasaj_SUTR3UEQJN45wa72rbub-p2YD4CFNWwCN_rE_L1tKQf6LsHopz-wILGlZqFThKhg0QMRAz0JmlBGACURDY1MJ_aWi1DzNLpi1VpcfBwZ20DxLXLwV3Wi6UDvAavGE1PSnGKCGauSZx3O8qHE7h3vZNEawIbWkex5PQ0iv9NvPjFr9BqLTtoT1KECxgkWkHtuyyjqiO8V9nIYdlc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
زهران ممدانی: «حدود ۶۰ هزار نفر از نیویورکی‌هایی که به ترامپ رأی داده بودند، در این انتخابات به ما رأی دادند.
🔴
در فضای سیاسی امروز، وقتی می‌خواهید درباره کسی قضاوت کنید و او را کنار بگذارید و بگویید: «او به آنها رأی داده، پس دیگر نمی‌توان با او صحبت کرد»… افراد زیادی هستند که فقط به دنبال کسی‌اند که شرایط واقعی زندگی‌شان را تغییر دهد.
🔴
بهتر است وقت خود را صرف گوش دادن به آنها کنید، نه اینکه برایشان سخنرانی و موعظه کنید.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/150514" target="_blank">📅 09:18 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150513">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
نیروهای یمنی: در سه ساعت گذشته، 20 حمله هوایی علیه مواضع حوثی ها در مناطق مختلف استان تعز انجام دادیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/150513" target="_blank">📅 09:12 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150512">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
شنیده شدن صدای انفجارهای شدید در ریاض پایتخت عربستان
✅
@AloNews</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/alonews/150512" target="_blank">📅 09:06 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150511">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
فرماندار خارکیف: در ۲۴ ساعت گذشته، حملات روسی به ۱۳ منطقه از استان، ۶ مجروح و خسارات مادی به بار آورده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/150511" target="_blank">📅 09:05 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150510">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HgexABhoLGp1m-GSZhZ6Ud2FM8nIjKFYrFzbyr_FunzPatFvluzBf1qQc7lmvD9dhBLyIY5Yw2M4ZuZm7fOnEJlUXKkfLHdMyb6uAGj7kiM3R7utkJGGFiUtCpWtQtCJk9ScwEjjpYMR36oeTwaU_XSPGlX7r1Io6z-jinmsC63BQKeg0HHKIZXo6gsKP-rWTO9UqDukiFbkkGqtTd1AEAFyUAtRAelA0GJvwA74aPsx0AAhMqECW07aVQ46uJ3_YhfnphAl1kAKmLETKNOhnOnepIZLgKkkilupDM_yD6OACGfGAEXhwknFKHAzlIQufxdgfHbvbgOwAu0AusLiFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سازمان دریانوردی بریتانیا (UKMTO): گزارش‌ها حاکی از آن است که یک نفتکش در تنگه هرمز هدف اصابت یک موشک ناشناس قرار گرفته و دچار آتش‌سوزی شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/150510" target="_blank">📅 09:01 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150509">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
آکسیوس: آمریکا دو پاتریوت دیگر برای حفاظت از تأسیسات انرژی به عربستان و قطر فرستاد.
🔴
آمریکا برای حمله به ایران به آسمان عربستان نیاز دارد؛ ریاض بدون حفاظت از تأسیسات نفتی بعید است موافقت کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/150509" target="_blank">📅 08:56 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150508">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: ایران در ماه سپتامبر هیچ نفت خامی را در نفتکش‌ها بارگیری نکرد. دولت ترامپ در حال قطع مهم‌ترین منبع درآمد ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/150508" target="_blank">📅 08:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150506">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/n7sCc5vq7k39F5dpta32uOP6tJRDrxxZHZyENOC_-MAe4saJ_f7E2fI0rY8rZPQE7cR4GSRt0WN8PRbuE_8HuPwDnX-VBtqQ6fKCnFtgCZTrpSqLUpKFS2QjO_EDTYgYtCKoE_x_NpZ1PihJJvMfDHZl607bv1qeJ899hBenTyAylSd3f9G6HHkeQqf9UnIFDrOX0Fvtl3yMZUczM6N6NRJmNVaP_VBD2MCv5fgzPn7C8__w3GxLMPpBN8L1LatU_pK03_t9fDVsKe3MC5MRNcnr18Fp56oyKsID0mjVkeJVtN9PFpm51QiKHZ8_UF8Jm8XNxU8e0Pj7Z7rpipL6Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/rbO3uPHmDdTBKTD6ITHJuJTEf8EzWj77HjWyhaWAE7MCAv1QxDkagenySX4zqmd0OIO2ULYMmA_pRcIFk5tMU_WAe7JNANAysEUEkF6J_Xl1AacZypu9SG5X3WksC6yj0DNRPNQn38L2yI5mBklj74v7Y12U-zEgInBzTVK2NMhj0lrAotyLreHmaivQvY4EqNSDQzDu29O35VqBQTudFrh4fLuVZgBCvx1ngPaU52eXyqQ_Sz1YHcwzUFZcs1NgHWIg3WrE-XZMmRxbt7AKlrpLKtqXq0C65FHgSZPZ2ypPYhQUH16KXtRjFF2R2pFedaYLxVz_8QEOdhWq-euK-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای از حرکت ناو تهاجمی «یو‌اس‌اس ماکین آیلند» به سمت خاورمیانه خبر میدهد!
🔴
تصاویر ماهواره‌ای Sentinel-2 که روز ۲۹ سپتامبر ثبت شده، ناو تهاجمی آبی‌خاکی USS Makin Island (LHD-8) نیروی دریایی آمریکا را در حال حرکت در اقیانوس آرام به سمت خاورمیانه نشان می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/150506" target="_blank">📅 08:48 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150505">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GbjPMQHVxENkyWwymjliUikm7riMuY6Krqp0emtl_d4P0wDw3QEpDgGILNsvyB2f_HZxf8Czf3w1v6EoxbxmZ_3L_m5KYjFOBVXscJEAJo1Icv_jsxmyNbBHPI1phzSoq6JPSs6yoEnrSSVB9xoN5dl5f4oanAcCO9p5xC_O92RksRC2Ik00qiePX9y4VdQUwt4nBPbYxvf4lBfkTcBOqPkgbpgZCGNMz-0ki-GrMvedGxpTdJ2Db37BykA7EWp8siS8qeLhO6GF693ftCrH8BF2A6CeWr1fQjOu_4d_1EUy1feLD4tMkdC8tQK-Mh37cHCRbgBJPj9lDfpK0hKPoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما: همه هنرمندا و خواننده ها دارن برمیگردن به ایران؛
رضا پهلوی
هم میتونه برگرده و به عنوان یه شهروند عادی زندگی کنه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/150505" target="_blank">📅 08:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150504">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ: ایران رادارهای پیشرفته‌ای ندارد و گاهی اوقات سعی می‌کند مین‌های دریایی کار بگذارد، اما ما معمولاً آنها را قبل از اینکه بتوانند مستقر شوند، از بین می‌بریم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/150504" target="_blank">📅 07:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150503">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8c69aba0a.mp4?token=am1mqfcQDDFV_OlG-LNz2-8Ur5q0J1mEchj1DTmdmwa7N7YSHQa94rvQJzDEQX3XTN0mfwIs3abtsP8jdjZa_DPCpAK34BoRuivyF90qotkCNforFYrZsf97ahL2fiKVjhpnTTt9YeTOn0buLj-0jNiZHcmgYppd-m6plWNDPqVCs0Cc4tRSuc81vkPwI4Myx2t0hP6yiHbBmf8NGE_lCZYXhTD64v67mCgebrcQHkQHZX4fS5yx-hwe9kjw50-YO5AgDEC6pnsRh-R5j_XziHtff-sHoFoUTmELMw7ta53lBsWuPdBNl47ytqR4susOJERhjhoMZnnEbRNLG8m-rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8c69aba0a.mp4?token=am1mqfcQDDFV_OlG-LNz2-8Ur5q0J1mEchj1DTmdmwa7N7YSHQa94rvQJzDEQX3XTN0mfwIs3abtsP8jdjZa_DPCpAK34BoRuivyF90qotkCNforFYrZsf97ahL2fiKVjhpnTTt9YeTOn0buLj-0jNiZHcmgYppd-m6plWNDPqVCs0Cc4tRSuc81vkPwI4Myx2t0hP6yiHbBmf8NGE_lCZYXhTD64v67mCgebrcQHkQHZX4fS5yx-hwe9kjw50-YO5AgDEC6pnsRh-R5j_XziHtff-sHoFoUTmELMw7ta53lBsWuPdBNl47ytqR4susOJERhjhoMZnnEbRNLG8m-rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ: رهبران و رؤسای‌جمهور ایران دیگر در میان ما نیستند، اما ما تلاش می‌کنیم با فرد فعلی [در رأس حکومت] با ملایمت برخورد کنیم.
🔴
بالاخره یک زمانی باید با یک نفر وارد مذاکره و تعامل شویم، درست است؟
🔴
اما ما نمی‌دانیم پس از رفتن اکثر رهبران ایران، با چه کسی در این کشور طرف هستیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/150503" target="_blank">📅 07:10 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150502">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27eb1079ee.mp4?token=KtXJEPGza-zIlLH5-Nat0GCxpyUB_uktgz90pNmpj33cNvzzotmTmv5MTFrfQqEu5bcfYGe16JJk4FvE14H2u_BwbFxsVOwQnhD7EEDgUJkNfekGDOo0OwtkzsDUzFaRq6y_hUKgu0io5pIWdnXrcY1dFrLU_GQ5itqzamYpsha0vlebbM2AWigaI5qIIem09vO47QjKWMB1KTCllCRBejUeE2kM3VCaf8KG9kpYOnDsD58V6r3EymbuXQ0c46gJCLyWqTY1ixkiMXUPvAOBz7Bz8IFdU_WeNl1AUc25Sv0QTzB_8IM_nXA445dVW2CQfWjSMl_psXAABU8ij_wwMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27eb1079ee.mp4?token=KtXJEPGza-zIlLH5-Nat0GCxpyUB_uktgz90pNmpj33cNvzzotmTmv5MTFrfQqEu5bcfYGe16JJk4FvE14H2u_BwbFxsVOwQnhD7EEDgUJkNfekGDOo0OwtkzsDUzFaRq6y_hUKgu0io5pIWdnXrcY1dFrLU_GQ5itqzamYpsha0vlebbM2AWigaI5qIIem09vO47QjKWMB1KTCllCRBejUeE2kM3VCaf8KG9kpYOnDsD58V6r3EymbuXQ0c46gJCLyWqTY1ixkiMXUPvAOBz7Bz8IFdU_WeNl1AUc25Sv0QTzB_8IM_nXA445dVW2CQfWjSMl_psXAABU8ij_wwMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دونالد ترامپ:
«ایران آماده تسلیم شدن است. ما همین حالا می‌توانیم خیلی راحت پیروز شویم.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/150502" target="_blank">📅 07:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150501">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromver2 vpn</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hqg5sNg3n1zHcBW8-unG4xg8dvUBIIrhUCEjb_rikTq-q7tQXfM1YG4eFHrqtAP747aPQUtFBK1wgwi3zfp6n_-wf9Nl90giLh67P89_zJa1FPs3Up8W_5ldKU2RuKpwSg1UcYYCaNUgFBNzlxiNUBZY3OtIE4ntCdDOxwfc8Z2UPUdnaBOUGyDxMdTME47xWUI8Gdh1YXxXapY9N2tIeT-u0MRRczLBZ4UHDRnIC_1Sv8-dWpbm8OJ6qbh7DgZj-hQO8_NCHXdYXrgRzEh3Ur7ktsgeZlM93ogm-9eYB8Q2t2KHBxxf1-TQ3ZoHViTaSj_GoBOugJktfuJo2ESEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر گیگ فقط هزار تومان!!
🚀
--------------------
همه کانفیگ ها با ضمانت برگشت وجه و پشتیبانی۲۴/۷ تقدیمتون میشن
❤️
💥
قدرتمند ترین سرور ها در جنگ
💥
سرویس های تانلی بدون قطعی
💥
سرعت بی نظیر و IP ثابت
-------------------
💬
تعرفه ها
🔸
سرویس ver2
▫️
30 گیگ — 60,000 تومان
▫️
50 گیگ — 100,000 تومان
▫️
100 گیگ — 200,000 تومان
🔹
نامحدود ver2
▫️
تک کاربر — 200,000 تومان
▫️
دو کاربر — 250,000 تومان
▫️
سه کاربر — 300,000 تومان
🔸
سرویس ver2 ویژه
▫️
10 گیگ — 40,000 تومان
▫️
20 گیگ — 80,000 تومان
▫️
30 گیگ — 120,000 تومان
▫️
50 گیگ — 200,000 تومان
▫️
100 گیگ — 350,000 تومان
🔸
سرویس اختصاصی
▫
5 گیگ — 35,000 تومان
▫️
10 گیگ — 70,000 تومان
▫️
20 گیگ — 120,000 تومان
▫️
30 گیگ — 180,000 تومان
▫️
50 گیگ — 300,000 تومان
▫
100 گیگ — 600,000 تومان
▫
200 گیگ — 1,000,000 تومان</div>
<div class="tg-footer">👁️ 76K · <a href="https://t.me/alonews/150501" target="_blank">📅 01:20 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150500">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
اسامی ۸ شرکت خودروسازی ایرانی که امشب تحریم شدند
۱- ایران‌خودرو
۲- ایران‌خودرو دیزل
۳- پارس‌ خودرو
۴- سایپا
۵- زامیاد
۶- نیرو موتور دماوند
۷- نیرو موتور شیراز
۸- هپکو
🔴
همچنین راه‌آهن و شرکت قطارهای مسافری رجا به همراه چند شرکت فولادی نیز تحریم شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/150500" target="_blank">📅 01:17 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150499">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ترامپ: ایران به‌زودی پایان خواهد یافت؛ به هر حال، یک‌جور یا جور دیگر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.6K · <a href="https://t.me/alonews/150499" target="_blank">📅 01:08 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150498">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qj3_zNAMKIyUNRBDG2wdy2dy5_0LL-Yfu_wkEu_0OLlS4cIyOlK6bwIUMn8OYcDHCLHKz3pbhKwZt-VJPuTuadOI87Mk2xFrw-_8DBA_qb6zVzLMFQBa2StMGvzsFrK1sW8F6YtJv9enNQMul18pJWxfbysLT_sLqZbiv1SPHuAGWkqGDx9D8Q7wrz261_8MkstnHfQfVrzYxI3JIijeyDm5Smm4lbwlQqHyQHMl9TZqkhLd5WMtu9B9l2Fu8t2nFpnzlrmr1SBo7t5cpBvu2aw6D9hjBvxVGyaBgvf9a9I1VFL6xhkUMzBLwpmkBcRl3wgvpJCTJrS14hXukmDqgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
جلیلی: ما قدرت اول جهان شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.4K · <a href="https://t.me/alonews/150498" target="_blank">📅 01:04 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150497">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qp5crZPPYsAMQeFI09_FMkllMAhMoynebt4ZKQIBpX8_pN89VfxAY-otc3UKuby08_Fj-4SaQDegjANnofm02r3pOcw6_kXWxpClpA9rEMlOdsFozoyPLTCpzDAHS-NfCGqqObLtq_8Hqm7wTWPxnVrTM32XiopmpPbcrKSUYySGqsD46-PyccQaPtOsyoPZ3tRk0oYfXlwuyg-cw__OpAxwtDkUxArKNHSefjJjuiP6m1OvxKOO38ENutG5QQPsTFuCWMePa6Qa9YDoyWYt9q3WyqSFi_Yo3H7wCqBV8uOBhUcbnvkdSp8ZHbtNb5puKL7XbORx_KXwwebxgMYlxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
سردار قاآنی:
آمریکا رو ما از عراق بیرون کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.8K · <a href="https://t.me/alonews/150497" target="_blank">📅 01:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371c09764.mp4?token=u7iZfE3aelgF7zU6SOYkLiLKdz-7iaGgFcLNZw67okcyhQUD1ggWXx0OU9mzJVQ3HdKqxSp9M5hNfdYVTHWoDIcJ94Qra9kDU_1K6xUuFVP8TF8TsSMO-4papySkoXiaeAolc9R8c9HY2e6HNA1MdDV5qlwYe32_YQyjAG4U7txOzKVDX6WUYLDDBOmM8ScIL8Zyy02j67zML9PHjXFaUqCEXB1ervgLiojrYCopAVhUwfyugvN6BZgWlsMRQu70jqG59yHI41yPssCgxJb_w477W_KTSLv8fo8OmfiRwMgS2D1tT5mKML41f7NRLJAwUKiYkv8mu1ONhwK0qMg2kQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371c09764.mp4?token=u7iZfE3aelgF7zU6SOYkLiLKdz-7iaGgFcLNZw67okcyhQUD1ggWXx0OU9mzJVQ3HdKqxSp9M5hNfdYVTHWoDIcJ94Qra9kDU_1K6xUuFVP8TF8TsSMO-4papySkoXiaeAolc9R8c9HY2e6HNA1MdDV5qlwYe32_YQyjAG4U7txOzKVDX6WUYLDDBOmM8ScIL8Zyy02j67zML9PHjXFaUqCEXB1ervgLiojrYCopAVhUwfyugvN6BZgWlsMRQu70jqG59yHI41yPssCgxJb_w477W_KTSLv8fo8OmfiRwMgS2D1tT5mKML41f7NRLJAwUKiYkv8mu1ONhwK0qMg2kQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مامور های عربستان یکیو دستگیر کردن که با خودش انتحاری برده بود سمت خونه خدا که منفجر کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.9K · <a href="https://t.me/alonews/150495" target="_blank">📅 00:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150494">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
احتمال مجازی شدن کلاس‌های دانشگاه‌ها افزایش یافت!
🔴
معاون آموزشی وزارت علوم اعلام کرد با توجه به شرایط هر دانشگاه، به‌ویژه در صورت گرما یا سرمای شدید، ممکن است بخشی از کلاس‌ها به‌صورت مجازی برگزار شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.8K · <a href="https://t.me/alonews/150494" target="_blank">📅 00:45 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150493">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
منتظر افزایش قیمت وحشتناک ماشین های ایرانی باشید.
🔴
ایران خودرو، سایپا و راه آهن ایران تحریم شد
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/150493" target="_blank">📅 00:41 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
میانگین درامد ماهانه (ناخالص) همسایه های ایران:
ایران 80$
قزاقستان 780$
روسیه: 850$
ارمنستان 750$
آذربایجان 600$
ترکمنستان 300$
تركيه 800$
عراق: 600$
افغانستان 100$
پاکستان 200$
عمان: 2000$ کارگر ساده تا 500$
امارات: 4200$
قطر: 3800$
بحرين 1800$
عربستان 2800$
كويت 3200$
✅
@AloNews</div>
<div class="tg-footer">👁️ 82K · <a href="https://t.me/alonews/150492" target="_blank">📅 00:36 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ویدیو ‌وایرال شده از تلاش یه موش برای نجات خودش وسط سیل گرگان  [@AloTweet]</div>
<div class="tg-footer">👁️ 77.5K · <a href="https://t.me/alonews/150491" target="_blank">📅 00:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150490">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=qnv7JCv4e0B7t8SruEe_lxbeEq6PfM6gMydz2fzxVPsOLL4rY1jNjHO-S_bEnFzbBDLTLuonLOvFUV_LvIZ4B1mepuPESwAoIrTr6x3hXhTY3PdWMK07dye5F-4zbDuH2PfM-69zn5YZHxjrvai0rkZpk4exKIP1_od7F-thgqEnu0Oz9Y9Pk0sbOuyjHyNgP0dRgtprBpUVeEsz8Ms5cBRA4jgOaLKBLg4iOach69JI9Mrb7zJCT5VChgJ6f6vrV5Jiz9tMmtzm6T8ajyJsSVA67x7-jmGxA1t1bCTwGlejTLhM9WPLilEvXykDcUWGCZ9bVEXQczyRgwB10YJYmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=qnv7JCv4e0B7t8SruEe_lxbeEq6PfM6gMydz2fzxVPsOLL4rY1jNjHO-S_bEnFzbBDLTLuonLOvFUV_LvIZ4B1mepuPESwAoIrTr6x3hXhTY3PdWMK07dye5F-4zbDuH2PfM-69zn5YZHxjrvai0rkZpk4exKIP1_od7F-thgqEnu0Oz9Y9Pk0sbOuyjHyNgP0dRgtprBpUVeEsz8Ms5cBRA4jgOaLKBLg4iOach69JI9Mrb7zJCT5VChgJ6f6vrV5Jiz9tMmtzm6T8ajyJsSVA67x7-jmGxA1t1bCTwGlejTLhM9WPLilEvXykDcUWGCZ9bVEXQczyRgwB10YJYmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
سؤال:
«آیا ایران در
حادثه پایگاه RAF فرفورد
نقش داشته است؟»
🔴
دونالد ترامپ، رئیس‌جمهور آمریکا:
«
بله، به نظر می‌رسد همین‌طور باشد.
»
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/150490" target="_blank">📅 00:23 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150489">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">‏
👈
رویترز:
پس از گزارش ها از اعزام سومین ناو هواپیمابر آمریکایی و نیرو های تفنگداران ویژه ارتش آمریکا به سمت خاورمیانه،
قیمت نفت هم اکنون به شدت در حال افزایش می‌باشد و مجدداً از 100 دلار عبور کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.8K · <a href="https://t.me/alonews/150489" target="_blank">📅 00:07 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150488">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a8a55537b.mp4?token=A8YcWKBRU1kKMJ_SqoZ7e1-Bq6-ZDnOFm3vIWPqwoJ3golrnWmQUhYa9IV3CJReWzEXJWBReBOqps84IOZmZ1Sb4-9D1K3CLwC_GUlAZ7x4udC3Lf-IpU2c-yU3-DVMN4hSMrFOPaB1EIn5hSHQEj83V0Rwk5t6MAPD3w0G7E_3YrK-LgU1nEEtQJLRIsCrqObbLxFQVGMEu_gpwwMWtLpOazvDNJ66PSepaOxGXNjl_RQubyKQJcXTEWHEQB8mV5O3US6Z6aOSdV9nhB6bX2e1nCZA_kFHmTuKLxklAGIUho9100rtFEXXGB4vtzOA6T-Lvff4i0tVMBvdQtBHIng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a8a55537b.mp4?token=A8YcWKBRU1kKMJ_SqoZ7e1-Bq6-ZDnOFm3vIWPqwoJ3golrnWmQUhYa9IV3CJReWzEXJWBReBOqps84IOZmZ1Sb4-9D1K3CLwC_GUlAZ7x4udC3Lf-IpU2c-yU3-DVMN4hSMrFOPaB1EIn5hSHQEj83V0Rwk5t6MAPD3w0G7E_3YrK-LgU1nEEtQJLRIsCrqObbLxFQVGMEu_gpwwMWtLpOazvDNJ66PSepaOxGXNjl_RQubyKQJcXTEWHEQB8mV5O3US6Z6aOSdV9nhB6bX2e1nCZA_kFHmTuKLxklAGIUho9100rtFEXXGB4vtzOA6T-Lvff4i0tVMBvdQtBHIng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک مداح: مجتبی خامنه‌ای ولی خداست
😐
✅
@AloNews</div>
<div class="tg-footer">👁️ 83K · <a href="https://t.me/alonews/150488" target="_blank">📅 23:56 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150487">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
ایران اعلام کرد که 3 نفتکش امارات را شب گذشته در تنگه هرمز با موشک هدف قرار داده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.4K · <a href="https://t.me/alonews/150487" target="_blank">📅 23:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150486">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
نیروی دریایی بریتانیا گزارش داد که یک کشتی در تنگه هرمز مورد هدف قرار گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/150486" target="_blank">📅 23:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150485">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YZr4sGp5VELibmunxgZuqn55fUn6ValfJknvz5gWsNUlAn7NFu-0HkbWtA_WuzxY25GqgPNSuhtNh_K4nQc9b6HkOonSHs5S7w6RakdiOJl3R1tCklEU1AkKsb7KsfHSKhk0rvLxFmBkOJB2JZqkqRaHIIGbBJZRwZA54jRENarZKM-z3uYggyLraqi6-rH5I8d5jertSW4K2e1MMfxWOk4ptkmc2pP6aD6KX_-V9Qw_d2-kAS6flc3lQf16paX_m3EoU7somJHccxZT1SgL2Ocvcw9y1fM3TDFprI7pZEx6Cl-sdh6aJ6ch_WhgBTQo_8Vnxyw5aQnvz1HLtCmqFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قلعه نویی: یه مشت وطن فروش با تیم‌ملی دشمنن
✅
@AloNews</div>
<div class="tg-footer">👁️ 88K · <a href="https://t.me/alonews/150485" target="_blank">📅 23:38 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150484">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
وزارت خارجه ایران: خواهان بازگشت برقراری پروازها میان ایران و عراق هستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/150484" target="_blank">📅 23:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150483">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
تحلیلگر فاکس نیوز: نتانیاهو مصمم است تا قبل از ۵ آبان به ایران حمله بزرگ کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 84.5K · <a href="https://t.me/alonews/150483" target="_blank">📅 23:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150482">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
پزشکیان: اگر در مصرف انرژی مدیریت کنیم هرگز کم نخواهیم آورد
🔴
ما سه برابر انگلستان گاز مصرف می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.4K · <a href="https://t.me/alonews/150482" target="_blank">📅 23:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150481">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
یک انفجار گسترده که گفته می‌شود توسط اسرائیل انجام شده، در منطقه المنصوری در جنوب لبنان مشاهده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/alonews/150481" target="_blank">📅 23:16 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150480">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/v8n1OFoueRGL2tE7nxYKb3yKejXEhcC2gi2E-RQCXcBuHeABC3Q4XBiRw0hCB-lG9xvjOmM3cTHDvwFxXVU5MI4lDob28beapZggmoFVlwREs9YH7yFqmK1DVyLKAI7s75bo9Ol0pqBPIa8S0C5CMC2BlxPEEv8kE2p9k8JOFC9tfFG8uaQ4MtoYMNRex5Ff1JYC1TjkBlAqhzL4jWU6lLvG_ijngt5TmaWgLrNh_Ck46o-YedI_EyCnIODiIARBl3t0UEoGwC8k-qPr7Q-gRNrtXugDk2ycrKnBx4Cp3tdUkYqzI4_zZ1Re4F-Bomg478MnqWE5V0UNQoEHgmTdgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اسکات بسنت، وزیر خزانه‌داری آمریکا، از کشورهای اروپایی خواست ارسال و عرضه محموله‌های انرژی را تسریع کنند تا به ثبات بازار جهانی کمک شود.
🔴
او همچنین گفت نباید بار کمبود گازوئیل بر دوش شرکت‌های آمریکایی گذاشته شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/alonews/150480" target="_blank">📅 23:10 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150479">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⚠️
اگه نمیدونی تو طلا و دلار چطور سرمایه گذاری کنی حتما اینجارو داشته باش
👇
https://t.me/shahab_gold_trading
https://t.me/shahab_gold_trading</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/150479" target="_blank">📅 23:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150478">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
فارس: منابع محلی گزارش کردند یک سوپر نفتکش با ظرفیت ۲.۵ میلیون بشکه که در مسیر غیر مجاز تنگه هرمز تردد می‌کرده در ۸ کیلومتری سواحل عمان مورد اصابت قرار گرفته و در حال سوختن است
✅
@AloNews</div>
<div class="tg-footer">👁️ 80.2K · <a href="https://t.me/alonews/150478" target="_blank">📅 22:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150477">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری / وال استریت ژورنال:
10 هزار نیروی نظامی آمریکایی عازم خاورمیانه شدند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/alonews/150477" target="_blank">📅 22:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150476">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
تسنیم: پلیس خشن و نامرد فرانسه امروز به معترضا گاز اشک آور زده
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.3K · <a href="https://t.me/alonews/150476" target="_blank">📅 22:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150475">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5b019bf6e.mp4?token=EMiQ3LLWQ08Jp8GWyM1uwE6snWed5rmt1XfcWOzv0Vvn6p9KH-1PK4yQCUMLepc17iCAlSrZOixeYCcekBtqvoE3JGxLVoQWNuOBTg5wXss4JvmYFDZXG3PWT0sCcj3nL_V9CnFcFMwsMQYvmDGbrOzItj9K4BGpKFIbKU3zDaMFp-CEQ33-4xyWPV13hVmVyrJsikCHLTnHf1bFb3tMXK6TcG6Megt_5jI6IHX9sgTQ5JtIsKGDue1EGm05EBN3v3gyBYX0Dgn8Qm9Ns0PhxzwR3uOGy1rZrHeX7jTYOQbKXBgm_44Rue0bRJ-qjDSGlfw_Co7vd4xj51Asjp_cMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5b019bf6e.mp4?token=EMiQ3LLWQ08Jp8GWyM1uwE6snWed5rmt1XfcWOzv0Vvn6p9KH-1PK4yQCUMLepc17iCAlSrZOixeYCcekBtqvoE3JGxLVoQWNuOBTg5wXss4JvmYFDZXG3PWT0sCcj3nL_V9CnFcFMwsMQYvmDGbrOzItj9K4BGpKFIbKU3zDaMFp-CEQ33-4xyWPV13hVmVyrJsikCHLTnHf1bFb3tMXK6TcG6Megt_5jI6IHX9sgTQ5JtIsKGDue1EGm05EBN3v3gyBYX0Dgn8Qm9Ns0PhxzwR3uOGy1rZrHeX7jTYOQbKXBgm_44Rue0bRJ-qjDSGlfw_Co7vd4xj51Asjp_cMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پوتین، رئیس‌جمهور روسیه، درباره سوئیس: «ما از بی‌طرفی استقبال می‌کنیم، اما اگر قرار است سوئیس بی‌طرف باشد، باید کاملاً از تمامی تحریم‌ها علیه روسیه کنار بماند.
🔴
بی‌طرفی نباید فقط در حرف باشد. سوئیس چه چیزی به دست آورد؟ هیچ چیز.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.9K · <a href="https://t.me/alonews/150475" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150474">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
کارشناس صداوسیما: ژاپن توسعه داره ولی هویت نداره و با کشوری همکاری میکنه که اون فاجعه هسته ای رو براشون رقم زده، مردم ما نمیخوان مثل ژاپن باشن
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.1K · <a href="https://t.me/alonews/150474" target="_blank">📅 22:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150473">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/onTVWEw6WDUqyJQuQV1tSj8zKM9LRT5Lyp2Ht6-3FYZsSrydRbF-ti9d24jN-43VyXeOCnqe748ISkPvnG3X_p3xIMTsetZmHCOAkjUtDOMxpiQcC_UjjL7TnpNYVkXYcVSRAKMeeFLi3i2vNlgMlMbHlK_JnsASZJUhgPQ3rF6v1H684SrPlRnq56I26FJaacxg_zfcp_-wfEwaUXulsKe67wWjeFLUsJ8TpUE647KmxeU8gujxp2SHPW-VsHpKS0EuZa6ZZkAWaJTKDAIwW8aKGwecaC3Lf3bKMoq1CsBYnhvhqogtECt6P0o54BaXKSD5ohwXQZNLRsEWWnv_uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : قیمت‌ها به طور چشمگیری نسبت به زمانی که بایدن و دموکرات‌ها قدرت را به ما تحویل دادند، کاهش یافته است. به همین دلیل بود که من انتخابات را بردم، و اکنون قیمت‌ها به سرعت در حال کاهش هستند.
🔴
این تقصیر دموکرات‌ها است، نه جمهوری‌خواهان - اما ما در حال رفع این مشکل هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 80K · <a href="https://t.me/alonews/150473" target="_blank">📅 22:18 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150472">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
بلومبرگ: ایران به‌طور غیرعلنی پیشنهاد کرده است که در ازای کاهش تحریم‌ها، دسترسی بازرسان هسته‌ای به تأسیساتی که در جریان جنگ آسیب دیده‌اند را دوباره برقرار کند
🔴
امتیازی احتمالی که هدف آن شکستن بن‌بست موجود در روابط با ایالات متحده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.7K · <a href="https://t.me/alonews/150472" target="_blank">📅 22:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150471">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
منابع عربی: ایران پیشنهاد داده در صورت کاهش تحریم‌ها، اجازه ورود بازرسان هسته‌ای را صادر کند
✅
@AloNews</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/alonews/150471" target="_blank">📅 22:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150470">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
گزارش‌های اولیه از شلیک‌هایی به سمت تنگه هرمز منتشر شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/150470" target="_blank">📅 22:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150468">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QL1Upf3fsRMoPDfh0jzIfCyN_4tJ7VjqP8CJEQ9p04l_7WKFrLCBSyhO3Jmvbyt3lKcSRQhKXSb-LtAjgXQ1wYY267I2KVgiqzGFsUY81-UhBaFUl9Ish-UzP6-I5BDCC0UnAPi4WWOmJ2Cw6oKIw2omlXKYNzbR1U56Rx2hwHB_9O5EdoRBEQe-_OEX9KLL9eNemVCZMtsjvYD1dp6LQfglO4RuvbeueMCHXhfHQEtx2bf-Twf6s-cLcRfoInbznfBNIde069K2_VoHSvKv1ARrBoqYtVRslr-nRG8kBuNxMakI5TtmjxjCUq0FoGhGQNNIHGkct5A2H4fuDDTxNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983fb64c5e.mp4?token=s_n9h0QSNBajuo2aHe1Sj_O4AfIQYDMaApdy_K1BLgW5I7Z-4DxIrbqCyozgnvQfN8_gwIEXMgPNCvMrwsCNdSXDQKafTXscQmvF3xbZAwF0yOFCDOZPhMA2mOXBsaa1vEuzcJVw9SYp6PnGU6tBdo5jBwJ03ZVPPRk8hw-VcSkZwlt5DJDMSxdIs4rs8-YKN8kbCuVB-fVypv1YitBTHWFN-SCXu5uz09pV7As2lkaNMJXKvyEzr43B69_3aByoeJ1FtaEEDffyqZzSdGoT7JyBn7IkYoaOTyUiJrC_eBquCBIdFWxCp7yPGeCAcvkqvsHClzw8nHSYjlWXgcTmUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983fb64c5e.mp4?token=s_n9h0QSNBajuo2aHe1Sj_O4AfIQYDMaApdy_K1BLgW5I7Z-4DxIrbqCyozgnvQfN8_gwIEXMgPNCvMrwsCNdSXDQKafTXscQmvF3xbZAwF0yOFCDOZPhMA2mOXBsaa1vEuzcJVw9SYp6PnGU6tBdo5jBwJ03ZVPPRk8hw-VcSkZwlt5DJDMSxdIs4rs8-YKN8kbCuVB-fVypv1YitBTHWFN-SCXu5uz09pV7As2lkaNMJXKvyEzr43B69_3aByoeJ1FtaEEDffyqZzSdGoT7JyBn7IkYoaOTyUiJrC_eBquCBIdFWxCp7yPGeCAcvkqvsHClzw8nHSYjlWXgcTmUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ در‌تروث پستی از اعتراضات ایران منتشر کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 81.7K · <a href="https://t.me/alonews/150468" target="_blank">📅 21:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150467">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وزارت کشور عربستان: تحقیقات اولیه درباره حادثه هواپیمای شرکت هواپیمایی دبی نشان می‌دهد که خلبان توسط کمک‌خلبان مورد حمله قرار گرفته است
🔴
خلبان هواپیما و کمک‌خلبان آن، پس از بهبودی کامل، صبح امروز همراه با یک تیم امنیتی اماراتی به ابوظبی عزیمت کردند.
🔴
تحقیقات درباره حادثه پرواز دبی توسط مراجع ذی‌صلاح پادشاهی و با مشارکت یک تیم فنی از کشور امارات انجام شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/150467" target="_blank">📅 21:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150466">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
سخنگوی نیروهای مسلح یمن: در ۲۴ ساعت گذشته، جنگنده‌های سعودی ۴۷ بار به یمن حمله کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/150466" target="_blank">📅 21:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150465">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">بچه هاااا
من هیچ وقت تو زندگیم شانس نداشتم که چیزی و برنده بشم. امروز گردونه صراف و دیدم، چرخوندمش بهم 3 صوت طلا دااااااد
😂
فکر کردم الکیه تا اینکه ثبت نام کردم نشست به کیف پولم
😐
😂
شما بزنید ببینید چی در میاد
👇
https://r.saraf.app/s/agrd346</div>
<div class="tg-footer">👁️ 74.6K · <a href="https://t.me/alonews/150465" target="_blank">📅 21:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150464">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
صداوسیما : فرانسه با معترضین دانشجو و دانش آموز به خشونت رفتار کرده و گاز اشک آور به سمت آنها شلیک میکند و حقوق معترضین را نقض میکند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/150464" target="_blank">📅 21:47 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=egsjGnNwsghaocd_iwvBT9_VuC2NRkblJpOdbePmlAjXoIHSAxG3F5lfEDRcKv6-8j2ooklsEW0vIra6ZzwS9yY79CbLMsMVzRejDyztS3wYv71mxFWMilqukixu7bf0Wm7M6S_Gt7IK1D7t8CuDtlITCK_SzZQTfwwbWovQx-tZqWVui_hwLNLMWjP5SPDVGHdn9Uh-KWKRdu-fYqs3Bw6mU69MLAIKA8HWpzAigGxC-hnu6V8QQI-7Of5wYx18ugUmOJ45gRKZ78DkNW_4XVqEPkvNo32745ySXQw1tTZ3QJ9hwlyZ2dmiZErQE6PJnmucqfD5mLxyLZNS7VrkxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8620d94f.mp4?token=egsjGnNwsghaocd_iwvBT9_VuC2NRkblJpOdbePmlAjXoIHSAxG3F5lfEDRcKv6-8j2ooklsEW0vIra6ZzwS9yY79CbLMsMVzRejDyztS3wYv71mxFWMilqukixu7bf0Wm7M6S_Gt7IK1D7t8CuDtlITCK_SzZQTfwwbWovQx-tZqWVui_hwLNLMWjP5SPDVGHdn9Uh-KWKRdu-fYqs3Bw6mU69MLAIKA8HWpzAigGxC-hnu6V8QQI-7Of5wYx18ugUmOJ45gRKZ78DkNW_4XVqEPkvNo32745ySXQw1tTZ3QJ9hwlyZ2dmiZErQE6PJnmucqfD5mLxyLZNS7VrkxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما خواستار محاکمه محسن نامجو و بیژن مرتضوی شد که به کشور برگشته‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 75.4K · <a href="https://t.me/alonews/150462" target="_blank">📅 21:45 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
کانال ۱۶ اسرائیل: اسرائیل در حال حاضر هیچ نشانه روشنی مبنی بر ارتباط خلبان عمانی با ایران ندارد؛ این در حالی است که رئیس‌جمهور آمریکا، دونالد ترامپ، پیش‌تر چنین اظهاراتی مطرح کرده بود.
🔴
در حال حاضر هیچ اطلاعاتی که دخالت ایران را رد کند وجود ندارد، اما هیچ مدرکی نیز برای تأیید آن در دست نیست
🔴
تحقیقات در عربستان سعودی همچنان ادامه دارد، اما تصویر کامل ماجرا هنوز مشخص نیست؛ بخشی از این ابهام به دلیل آن است که مقام‌های سعودی تنها اطلاعات محدودی از روند تحقیقات منتشر می‌کنند.
🔴
موساد و شاباک نیز از طرف اسرائیل در این تحقیقات مشارکت دارند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/alonews/150461" target="_blank">📅 21:40 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/alonews/150460" target="_blank">📅 21:35 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150459">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوووووووووووووووووووری</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/150459" target="_blank">📅 21:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150458">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YSSW0VWOrjpREbIpJ3axRM7nCO6Age0YYMWoPYjZe5ibq5Dlltep__GWlsHyseHLyhL96KnJkOhc940TDu_geNProS8-4PZev7P0qKKRWy7yMrbTUnekA4WvIf5hofBtrgMIFuq1sHfXoxPY4XAkuTMGprEVaa9z4nCeQ5oWzrmCOe97uiefFUhQWdsyIpu0ijllG9Oiu6kzTwbub4Y80HwbeqBPtFFObeGAIAK0DKqz3ZQpy-dpQlOuaYKMJnnoU_YjBePcKFU3KKzx7WcTYh78EVWdut7WGIOhGdqpW-EYftbrdFxQL0BnsJvWrW90QAOohArvzaArvRG96eVqiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ:
من بارها اعلام کردم که برای از بین بردن تهدید هسته‌ای ایران، به ۴ تا ۶ هفته زمان نیاز است، و من این کار را در یک شب انجام دادم! بقیه زمان صرف این کار می‌شود که مطمئن شویم این وضعیت همچنان ادامه داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.4K · <a href="https://t.me/alonews/150458" target="_blank">📅 21:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150457">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
پوتین: جهان از شجاعت و مقاومت ملت ایران شگفت‌زده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/150457" target="_blank">📅 21:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150456">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
وزیر خزانه داری آمریکا: تحریم های جدید ایران(راه آهن و خودروسازی) حامیان آن را هدف قرار داده و راه را برای خشک شدن منابع مالی این رژیم هموار می کند.‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/alonews/150456" target="_blank">📅 21:13 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150455">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=B82S42P1-zwyO5mscLJzZcmZ1e-AqyrSpp5SEv_mufDQWBbaseYvWbjeiIl8WHrCKxx668C84r6KVl0CMkP3nktWnOfSI8z9sZiDuG5o7uzZCp9P4Qk5g-dk6cdCRe-tjB2UxebOaa7XRRH6-fZenu9VICy4C-dZaZsDLBgYt4BWB9OPzPuovSjTZrSkcBOOnPy9qUbtWnJoZif5wYsI4E2TfdoRSh-CW54jXnq144Mnh98JcGjOuKkyNjWahqb3HYi54HA-l-Eee4nGcvDkTdx-u3L6-GBOoIpEZ8ebHN-a6IQur_mt0_1rDXtyKfdYFcdgdxicIww59hfEJa0pTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b62a7d15bd.mp4?token=B82S42P1-zwyO5mscLJzZcmZ1e-AqyrSpp5SEv_mufDQWBbaseYvWbjeiIl8WHrCKxx668C84r6KVl0CMkP3nktWnOfSI8z9sZiDuG5o7uzZCp9P4Qk5g-dk6cdCRe-tjB2UxebOaa7XRRH6-fZenu9VICy4C-dZaZsDLBgYt4BWB9OPzPuovSjTZrSkcBOOnPy9qUbtWnJoZif5wYsI4E2TfdoRSh-CW54jXnq144Mnh98JcGjOuKkyNjWahqb3HYi54HA-l-Eee4nGcvDkTdx-u3L6-GBOoIpEZ8ebHN-a6IQur_mt0_1rDXtyKfdYFcdgdxicIww59hfEJa0pTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
میلی گلد این فیلمو از طلاهاش منتشر کرد و گفت دزد نیستیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.1K · <a href="https://t.me/alonews/150455" target="_blank">📅 21:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150454">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
پوتین: جهان از شجاعت و مقاومت ملت ایران شگفت‌زده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/150454" target="_blank">📅 21:02 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150453">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
ترامپ: اگر ایران پشت آن حمله به هواپیما بوده باشد ضربه بسیار محکمی خواهد خورد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.7K · <a href="https://t.me/alonews/150453" target="_blank">📅 20:57 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150452">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=iQ5SluAghWBLz8PLVlYPzh0QP_9YqMXIZhLRgClJ7-d8VBZVQxwr_sq4xEoD3R63L2s8a3Ry3YB1R4thtgQ4HO18Dh1jphIPoOuA3DZxk8Axwueblh2-LCyEE3n3Us_4-fkgD1JUlTb5Tb5zOa0XHMcI-pKK8tL-vxAnGAVl4pbf3YEB6OBhc2qviPzeKbkGJD0GnA1rpV1eMGWf5Ctyn0hH0sYFaNjJ_a1_tPFMLNWlHGG59q_Ec7OWjeAkkWXwBjeWkGzjCZIBYqGQTJwhi3kkWkilY3fS3C8oXorSEU85HUly8nyZVz8DG5jRNW0_Q0xvtjXGVYk-6vUABkXXaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=iQ5SluAghWBLz8PLVlYPzh0QP_9YqMXIZhLRgClJ7-d8VBZVQxwr_sq4xEoD3R63L2s8a3Ry3YB1R4thtgQ4HO18Dh1jphIPoOuA3DZxk8Axwueblh2-LCyEE3n3Us_4-fkgD1JUlTb5Tb5zOa0XHMcI-pKK8tL-vxAnGAVl4pbf3YEB6OBhc2qviPzeKbkGJD0GnA1rpV1eMGWf5Ctyn0hH0sYFaNjJ_a1_tPFMLNWlHGG59q_Ec7OWjeAkkWXwBjeWkGzjCZIBYqGQTJwhi3kkWkilY3fS3C8oXorSEU85HUly8nyZVz8DG5jRNW0_Q0xvtjXGVYk-6vUABkXXaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: وضعیت نیابت‌های ایران، مانند حزب‌الله، چگونه است؟
🔴
ترامپ: آن‌ها با ایران می‌روند، بنابراین نیابت‌ها نیز با آن می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.3K · <a href="https://t.me/alonews/150452" target="_blank">📅 20:55 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150451">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
ترامپ: من به دولت، اقتصاد و همه چیز نمره A+ می‌دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/alonews/150451" target="_blank">📅 20:48 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150450">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🔴
فوری/ترامپ:  اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/alonews/150450" target="_blank">📅 20:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150449">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
ترامپ: ما ذخایر راهبردی ملی خود را با نفت ونزوئلا پر خواهیم کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/alonews/150449" target="_blank">📅 20:34 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e448c031e.mp4?token=q6QJvnVcepgYEC1KUUtkUorPMDmkZUcE9y3fEqyNbRZryTJ9_pnVJH7redohmopm8M-hzRBkE8DQil3ZFCJwM4D0Kcrr-DeLmpaWF4vD4eIX7HMTLo3x80hb9dumKY6sw235UMxvUqbsShHcNe-nBgFwOPuy198wEV-T0cxuiBcUslMONJ4O399XdjBROcEECEc7__aYQVtAIIfyceM2RDC78TCsNBJwayoFUaIe9zP_qrNQNQ_oWmhCrXLynJ3odpq-F1oqgB0E6APg8HJ86ar-yMNmW_4mYt5Eewt0ZHQkqbd0Pyriu4F10hlWLF58cxlgvAzFG-rK2oL7DKCyYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e448c031e.mp4?token=q6QJvnVcepgYEC1KUUtkUorPMDmkZUcE9y3fEqyNbRZryTJ9_pnVJH7redohmopm8M-hzRBkE8DQil3ZFCJwM4D0Kcrr-DeLmpaWF4vD4eIX7HMTLo3x80hb9dumKY6sw235UMxvUqbsShHcNe-nBgFwOPuy198wEV-T0cxuiBcUslMONJ4O399XdjBROcEECEc7__aYQVtAIIfyceM2RDC78TCsNBJwayoFUaIe9zP_qrNQNQ_oWmhCrXLynJ3odpq-F1oqgB0E6APg8HJ86ar-yMNmW_4mYt5Eewt0ZHQkqbd0Pyriu4F10hlWLF58cxlgvAzFG-rK2oL7DKCyYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فوری/ترامپ:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 78.5K · <a href="https://t.me/alonews/150447" target="_blank">📅 20:27 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
ام بی سی: مذاکرات به یک باره مثبت شده است
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/alonews/150446" target="_blank">📅 20:25 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
ترامپ: مقدار نفت عبوری از تنگه هرمز در حال حاضر بیشتر از قبل از جنگ است
✅
@AloNews</div>
<div class="tg-footer">👁️ 76.1K · <a href="https://t.me/alonews/150445" target="_blank">📅 20:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-150444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فووووری/ترامپ: ایران پذیرفته است که سلاح هسته ای نداشته باشد‌‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/150444" target="_blank">📅 20:17 · 09 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
