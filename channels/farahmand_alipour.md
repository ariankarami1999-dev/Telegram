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
<img src="https://cdn4.telesco.pe/file/R0ukF6YuJGfk6QR4W_kUt4LZoWXyR68nGhgAaGRupxOXfzeIIvxIVHchkX13f6nYxRluNLgGnGxRryGHZsg5Gz_bYJ0i_WlhCmKCKJJ3vOQlSM0MDEV0lJOJt3C33K0YPgOf8DjgSW0Qwjequ2px8d2oOXbHLewFGOSJcaWgxVRrYhHs3NKqBRcCQSQIg-hrRlTKxMyBFI-XM_qtbkJz_YQW6S-CCXRXBI0HZXM_YB6EDvYxY7Aihn-05mB4weml-2o_hemEB5_nXvP-KdD4adsn5uA6sEzs37Dc8ckoQlAy7yNLxeMx8afLKYpmYCGsFg8c6qLDawW0-MRi8cViJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 07:13:44</div>
<hr>

<div class="tg-post" id="msg-5874">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8af28806.mp4?token=aRfQCNtzXLOm5HtXBMMd6iAZewy1TQR_olhJOMPfhfDEf602MXqtp_qzjz8WNXLCrH4ObHtZTKOkuQ_0IC45uzXcenj0WvVsYHuwTTBvFnYs81K6qGPOVNu6mnzJVjHkAs5sLEwORtOf2TxEEx1_P88Iw3VAQjwZ5o-cBlQ276emCkpvxq2kPWTK2pNJ_MABoHj6psamibA0sQrJKO05ovtSgHfwGbqS3ydzipCSLLnZ5NohmT4kUNkeRp0cFhm1dkVtbPn3JAsk16Rdch98OkhSObpitCPVcc9RscRIs-b_WoqJJmCX8XD81Aow5QdEB3yPIjzAIv1CXyWm-VkY5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8af28806.mp4?token=aRfQCNtzXLOm5HtXBMMd6iAZewy1TQR_olhJOMPfhfDEf602MXqtp_qzjz8WNXLCrH4ObHtZTKOkuQ_0IC45uzXcenj0WvVsYHuwTTBvFnYs81K6qGPOVNu6mnzJVjHkAs5sLEwORtOf2TxEEx1_P88Iw3VAQjwZ5o-cBlQ276emCkpvxq2kPWTK2pNJ_MABoHj6psamibA0sQrJKO05ovtSgHfwGbqS3ydzipCSLLnZ5NohmT4kUNkeRp0cFhm1dkVtbPn3JAsk16Rdch98OkhSObpitCPVcc9RscRIs-b_WoqJJmCX8XD81Aow5QdEB3yPIjzAIv1CXyWm-VkY5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویژگی‌‌های یک زن خوب از نگاه اینها
حدادعادل داره از دخترش تعریف و تمجید میکنه :
مثل یک خدمتکار کار می‌کرد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Hr_ni2aMd0iaNt6qnRy2KuW4m6kDLvOlL3Eura7ABTceAx70WYEI_b0PxfGiw3U2KUJVFx4DWjqBwn60SVErcljFH8qCgxlhCHURb113zfeZHn4KRZH40_dW2EGWUbWBqx9YADPSrbu7GQqWVgGeKyJ_5kEAi0ozpy32APdMFO6cn21gS0OEkmxYPZuXh6a2PFek780XrCzvJJoJ_8HLNwAelBIqo87nh8ngpdamTc9E1NeWZp1rnfbXPXyg2ZE2OhNOfRJ1ENAobE3nF629TH5WDAgG61QecXHMJIz5grR5PcKxo42G4khfP6xYFC34z2nIKFfIQ7OkQ_2sSyTX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Hr_ni2aMd0iaNt6qnRy2KuW4m6kDLvOlL3Eura7ABTceAx70WYEI_b0PxfGiw3U2KUJVFx4DWjqBwn60SVErcljFH8qCgxlhCHURb113zfeZHn4KRZH40_dW2EGWUbWBqx9YADPSrbu7GQqWVgGeKyJ_5kEAi0ozpy32APdMFO6cn21gS0OEkmxYPZuXh6a2PFek780XrCzvJJoJ_8HLNwAelBIqo87nh8ngpdamTc9E1NeWZp1rnfbXPXyg2ZE2OhNOfRJ1ENAobE3nF629TH5WDAgG61QecXHMJIz5grR5PcKxo42G4khfP6xYFC34z2nIKFfIQ7OkQ_2sSyTX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8TmlUukgx1CEMxrplBrST7mcORmueW5TPxmvJyYIx1gXuGnjch6i_jSD6dxQA9wNntu2S2uOLXXgZnMEc_5MsPr2YVuuR5OPlbKMSGK7xmig-nu01nyG8d6GkeyzUxn4tckbpN7A-DKWeZjdRctdIIw0vkX9V69l6raE4_Oinyql337INXK4g2riy7f-GFsi6GF3lhGhIcrg4xvRS6XWe1WuRul9AhWMl13Wrin5WVHXwbzwSxrMa9nxYPEhZaenXITHHcr7OmRGUHDdKQ7THRh37vPrCn9oMKyyrGIcOhk-lU7twZS7Bx-MskFFy87mKoeN8ggtc9CNGde889kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/266ca65797.mp4?token=Tnn0xsgkKjbwfqj34MmkiRDI2vEgeCblEMfjZL3zRKKMTHprPuc4npIKab04bF3g6TIFzQsyPKZyUVM1_g9TgKo_mN34zotqu1DRzLmKkb1ME1J119fGYl4y2-lkyHBSjGCMvXtsjT48H71V_vDQRXwjiIj-qq6D9i0WCo9hpDgQxM5MsEc4RU7Bv4xFxtN8LXIJVC0ZAipHJU2CJwFn5XRXdYiezFg4F-kIQo5lfi9kZ0EMTc4958GUDKjqrCEPCMuGIE146EdXjVly7rBYyPqEFBXoCZOrBBcmMMCFRF9zt0bc0ATDQyn753yWvnbhoWb-yLK_hDzXpwIb2soaJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/266ca65797.mp4?token=Tnn0xsgkKjbwfqj34MmkiRDI2vEgeCblEMfjZL3zRKKMTHprPuc4npIKab04bF3g6TIFzQsyPKZyUVM1_g9TgKo_mN34zotqu1DRzLmKkb1ME1J119fGYl4y2-lkyHBSjGCMvXtsjT48H71V_vDQRXwjiIj-qq6D9i0WCo9hpDgQxM5MsEc4RU7Bv4xFxtN8LXIJVC0ZAipHJU2CJwFn5XRXdYiezFg4F-kIQo5lfi9kZ0EMTc4958GUDKjqrCEPCMuGIE146EdXjVly7rBYyPqEFBXoCZOrBBcmMMCFRF9zt0bc0ATDQyn753yWvnbhoWb-yLK_hDzXpwIb2soaJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقام انتقام!
بسیار به جاست که یادآوری کنم
اولین گروهی که رفت دنبال انتقام و خونخواهی
خامنه‌ای، گروه تروریستی حزب‌الله لبنان بود!
و پاسخ نتانیاهو چنان بود که جمهوری اسلامی برای نجات حزب‌الله و بیرون کشیدنش
از زیر دست و‌‌ پای اسرائیل،
به آب و آتش زد و  پایان جنگ در لبنان رو به عنوان شرط اول مذاکراتش با آمریکا عنوان کرد! در انتها هم بخش زیادی از خاک لبنان دست اسرائیل موند و یک میلیون شیعه حدود ۴ ماهه که آواره‌اند!!</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KoAu1PmwVYA3LP68ppIXDozJmFHdeRrkmvN67PiomR_RHpWdzfs_oIK70uhkgaDf6AaBvZYaZUj9hK_5b1bk7orTDFl8UJi731_ZzxqgrMUsXARjIt7T5Vio9QPcka-PmOSYnkeLcqjzK4WLgTgF4xSqmVGecK0ft3deQPGy1XnadoY2RFUpHJZXUAy5ABmK2kHGGDefVG7XE9aK2uBgfxOzeZSi2s0jbCvXN-7l3CredUCp72ZgQaPEsqdTB3AYMumhqts6q42e1NpDdPK_CG7TzwA_0B9Il52cDa-b0zERux8FAVVU1JQSbv6Umkh_WwfxAENCOJIEKYEauZpujg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه تروریست‌ها
الجزیره از دیروز شیون و زاری میکنه!
زمان جنگ هم، در حالی که جمهوری اسلامی به قطر موشک میزد،
الجزیره به سود آخوندهای جمهوری اسلامی گزارش میداد.
وجود جمهوری اسلامی سود هنگفتی به قطر میده.
قطر و ایران یک میدان مشترک گازی دارند، بزرگ‌ترین جهان.
۸۳ درصد درآمد قطر از همین میدانه!
راز ثروت و جایگاه قطر از همین میدانه.
سالی بیش از ۸۰ میلیارد دلار به جیب خاندان حاکم بر قطر واریز میشه. کشوری که جمعیتش (بومیانش) کمتر از ۳۰۰ هزار نفره. چیزی که باعث شدت قطر ثروتمندترین کشور جهان باشه بر اساس درآمد سرانه!
جمهوری اسلامی اما به خاطر تحریم‌ها قادر به صادرات گسترده و رقابت با قطر نیست!
تداوم جمهوری اسلامی، یعنی تضمین اینکه قطر همیشه بدون رقیب می‌تونه از این میدان برداشت کنه و درآمد هنگفت داشته باشه.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f51396b862.mp4?token=K7VRVhrjEkMp5debIpOvaYKyRjnooX_ACYbu3oa-Odr8kNgcrj3Dp-3ms1imFzdA7imqoLMB-B_i7D2cf2wNyuxEv9m83f3M3zfmbGSofRwHzUhl4g8-fd2mVNSBFKPbZbn3XQI6Y9x5MqiddSQ5FYdXQ49mk8DtCKn3Gpd6wY4H5sHgdWvIjzGI7IW39P17edMXlwVnRBNIMOUZo6bkoLIdcJgrFyhgpu9Dk-1VI6r7BpcbmRSwklAs9i1VNXj8LaiaB8wSVL2TyMiBBx519py9yMG_Qn76NDvl8qfdKyb1RsJapPIfjffCwcopH3GJ8geBk6XCdQybgZEw_6QE9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f51396b862.mp4?token=K7VRVhrjEkMp5debIpOvaYKyRjnooX_ACYbu3oa-Odr8kNgcrj3Dp-3ms1imFzdA7imqoLMB-B_i7D2cf2wNyuxEv9m83f3M3zfmbGSofRwHzUhl4g8-fd2mVNSBFKPbZbn3XQI6Y9x5MqiddSQ5FYdXQ49mk8DtCKn3Gpd6wY4H5sHgdWvIjzGI7IW39P17edMXlwVnRBNIMOUZo6bkoLIdcJgrFyhgpu9Dk-1VI6r7BpcbmRSwklAs9i1VNXj8LaiaB8wSVL2TyMiBBx519py9yMG_Qn76NDvl8qfdKyb1RsJapPIfjffCwcopH3GJ8geBk6XCdQybgZEw_6QE9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک گروهی در جمهوری اسلامی نشسته بودن و برای هر هیئتی که برای ادای احترام می‌رفت، یک آیه خاص قرآن انتخاب کرده بودن!
یک تئاتر و شوی آخوندی!
مثلا برای گروه‌های تروریستی حماس و حزب‌الله این آیه‌ها بود که آفرین به شما! کارتون عالیه! ادامه بدید!
برای عربستان این بود که مسلمین دو گروه شدن، خوب‌هاشون (جمهوری اسلامی) مبارزه میکنن و بدهاش (عربستان) کافر شدن!
برای حسن خمینی هم یک صحنه‌آرایی کرده بودن و یه آیه‌ای بود که مثلا تو به اندازه کافی جهاد نکردی! (خامنه‌ای خیلی جهاد کرده بود!)  و….
ولی از اونجایی که این خودش نوه خمینیه و خودشون این درس‌ها و مکرها رو به بقیه یاد داده بودن، وسط خوندن آیه ، احترامش رو جمع کرد و با خودش برد!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=PtPrIdECUAAJeo3D4DPRTEclqEuDboVBt_wgtaIdZbeg0D0ZWHlqBglUXBdgSyljDGtB_55O7q1FpzfwFY0EqULKRW9t7L_aBR70c1qbVIzW3MtZIK2y4e6BWre822T8aD1gBD3dVeUGIy4Xp-MQ09k6Y6EtBHPXX8H8_IPshSLTAk-QROmH7ahAKy1oKg1RP_wju66CXX3Tu9tdz5NObErZ4I9iFvkgvoH8YemAaPhjHFalyQQYlDogfrBW7wS7VHmBInyhYK-5VlHiv9UXlQU7ozO2LqapTY6G7ffc4roGTihA-y85DmSIriN9srtd_E3jpzr5MQELE5nTz6FWeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/517b3aef1f.mp4?token=PtPrIdECUAAJeo3D4DPRTEclqEuDboVBt_wgtaIdZbeg0D0ZWHlqBglUXBdgSyljDGtB_55O7q1FpzfwFY0EqULKRW9t7L_aBR70c1qbVIzW3MtZIK2y4e6BWre822T8aD1gBD3dVeUGIy4Xp-MQ09k6Y6EtBHPXX8H8_IPshSLTAk-QROmH7ahAKy1oKg1RP_wju66CXX3Tu9tdz5NObErZ4I9iFvkgvoH8YemAaPhjHFalyQQYlDogfrBW7wS7VHmBInyhYK-5VlHiv9UXlQU7ozO2LqapTY6G7ffc4roGTihA-y85DmSIriN9srtd_E3jpzr5MQELE5nTz6FWeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با امن شدن اوضاع، سه پسر خامنه‌ای هم پس از ۱۲۰ روز غیبت دوباره ظهور کردن،
اون یکی‌شون همچنان در غیبته.
رافضی‌های جمهوری اسلامی اینقدر کینه‌توزن
که برای مراسم خامنه‌ای، ۳ رئیس جمهور قبلی
(احمدی‌نژاد، روحانی و خاتمی) رو هم
دعوت نکردن!!
بعد در میانه جنگ میگفتن «علاج در وطن است»! حتی برای خاکسپاری رهبرتون هم روسای جمهور خودتون رو هم حذف می‌کنید و راه نمیدید!! تا این اندازه تمامیت خواه و کینه‌توز!</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=hcLr0lPgBWpt673HV6_kxiRYojBhfrUTnzSIA4ipBZb3nSFO0qRLomrEOYR-AgrjRwpUqZWSf1a1e4SIn2LBfXgewo6n3tX1f2-5cuuGgvj0u_56XcET9V7prFWJnnC-VDTk3XpvOovDLWXg6k9nR7mY2D3iTSbFz1oDytARdd-61lubQCdjv-E7HILYxdxVJyx9z7sS05iqjquxHz-EDA1Q7mTGR8hRH-sxXfDJjjOxvPPY1kUTXDwrxx0BdKlQM4-jeKCLUnn7WZ0brhz0itn_KjfIoPbyjUjB9xYJ9RrDajaWI_nJgMWN2z0MEsjREfXu9ycroF7p-fnT7Rm19Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/264a3cd93b.mp4?token=hcLr0lPgBWpt673HV6_kxiRYojBhfrUTnzSIA4ipBZb3nSFO0qRLomrEOYR-AgrjRwpUqZWSf1a1e4SIn2LBfXgewo6n3tX1f2-5cuuGgvj0u_56XcET9V7prFWJnnC-VDTk3XpvOovDLWXg6k9nR7mY2D3iTSbFz1oDytARdd-61lubQCdjv-E7HILYxdxVJyx9z7sS05iqjquxHz-EDA1Q7mTGR8hRH-sxXfDJjjOxvPPY1kUTXDwrxx0BdKlQM4-jeKCLUnn7WZ0brhz0itn_KjfIoPbyjUjB9xYJ9RrDajaWI_nJgMWN2z0MEsjREfXu9ycroF7p-fnT7Rm19Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">۱۲۰ روز رفته بودن توی ۷۰ تا سوراخ قایم شده بودن
الان که می‌دونن همه جا امنه اومدن بیرون
میگن انتقام بگیریم!</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLU3ZqkixYOl4MtuZt7Vv-YQ1gq-9xpYT_NXxaYUydy8vMnhrU1gO5XBS8q_skoBscMlT5swg7ci85jwe7mrhlyL_s9vVjDgv2x2XA_u08JwVnO7J34ovqELTTDVECunq4bzOOrK8vheYemFy3j_MlJNnY7OxMmIfWaJyiuLwnSTewvXgjen-BhpwZQ90x73K4yGFiMprkyV41_J7sUIAvkrNk2KFhOczZvn2oKfu5AOIqfDOywqeLYumc43pOkYpaJHhpNZAeU5IL7sH2Vpgz-LZaNqNx2zkTNy26im47AEMIpm4qAULj5Q6gsg7jO010JUZbWrXTX6TZHOry7low.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=loGMjPF6Oc_hE3iaYHXvjgF-dn1vuEqoseHlWra_geqt2gnbct8JHqxg1XhlbfESZgCLUkXw20ZbFfICSBA4kuwZSFvmLUCS0QYfaDY3M59yLeiP44KCEC5eihAEiWjspXPfdlECpt39RAO3mOiSkpFsO3SbILzDcErkjHsdi2qZKwAL7J46X78rcn_1aGQQwcSvI_GPfrDYF-1fV9P_WcSNmK7e2HkYxXDj47WtE_m8AHND0ViYWX-7cCzfbYBW6mX-b0HOixowIkx_U-5cZEKq_bVJf-6UX4Ue1FwYgiYQHA9QwAdjASXMIfYbs3mluuigVvj06uBVq2tsB-YKaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=loGMjPF6Oc_hE3iaYHXvjgF-dn1vuEqoseHlWra_geqt2gnbct8JHqxg1XhlbfESZgCLUkXw20ZbFfICSBA4kuwZSFvmLUCS0QYfaDY3M59yLeiP44KCEC5eihAEiWjspXPfdlECpt39RAO3mOiSkpFsO3SbILzDcErkjHsdi2qZKwAL7J46X78rcn_1aGQQwcSvI_GPfrDYF-1fV9P_WcSNmK7e2HkYxXDj47WtE_m8AHND0ViYWX-7cCzfbYBW6mX-b0HOixowIkx_U-5cZEKq_bVJf-6UX4Ue1FwYgiYQHA9QwAdjASXMIfYbs3mluuigVvj06uBVq2tsB-YKaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=M5cLA2QwTt9U1k-o98Jp1H5_DmJna36gGGqv2f215Y3zu9JX1Qmi_5Ov8ff8oP4IAwN4rZvu0xCBJc8Uyvp8mqDlliccgW7HNet6dwyo8b0atX_B0UcoDpR-yOS_RxvtVpk5exrzHRwwIuUMWctuJH0S96r2GmYHTnzggMjHxMPqJQW743XlgI60p_Q8eFi2Q2vtrUyp--z0YzlQBX5fsc7EHGzGo5iLVVpqxRKcbdTFu8hefP_YolE25kRnFBRzulkQSEWHYQWp28pmUVdZICHlgxJntZQhfUmL2obv09U_mkFsaJyFwE__GnuQ8Zw7kzegIp5ZPVK7FCESUsMi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=M5cLA2QwTt9U1k-o98Jp1H5_DmJna36gGGqv2f215Y3zu9JX1Qmi_5Ov8ff8oP4IAwN4rZvu0xCBJc8Uyvp8mqDlliccgW7HNet6dwyo8b0atX_B0UcoDpR-yOS_RxvtVpk5exrzHRwwIuUMWctuJH0S96r2GmYHTnzggMjHxMPqJQW743XlgI60p_Q8eFi2Q2vtrUyp--z0YzlQBX5fsc7EHGzGo5iLVVpqxRKcbdTFu8hefP_YolE25kRnFBRzulkQSEWHYQWp28pmUVdZICHlgxJntZQhfUmL2obv09U_mkFsaJyFwE__GnuQ8Zw7kzegIp5ZPVK7FCESUsMi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjmnD5ZzfO0uysXnXoc8tr5tBCeE08TyGgZj_SYRTpv2lBtW7Tj3KBP1xE2-H645h2UxKXK2V_Ou4-T8DJSNjY80m3fMCfFdOGVLBoNf95s_hacPZefUXr_3lepR3kxRrBM8lz3QuJ7ogzpAzhxrEniojxd-lWGDRncgKUzaCq_DR1PKOWt9NuGiQyKvTRJEZIv_8gq7wTuLCRBIPVbO3zAwMY2-DYDxQ9PvTVUVtRET67DTm_SopFOKdWEFOcSqfuvlq1Yk8K7T-tunk2KGxVVTPRFQhmUWX4Tffdz_3qyb1vcrOhHGlsZhgJFPMc9I6EBlEDHd88_OP2yBvf1iNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1A1DOQXvaLgznkFziFe6otJs5BpkhPCjgw73C0OUC6mUeXmBG122s2-siZJocgOEaIPieGZoQcmy5NtP-ai2WlePjrFD2MjLPuMNmkBBOQfxrK8HXJVtbnhA1JhiSg60RwCHB2NEgn2iNpUJygpAga_Bkk15Dypz6G4EVaNPyoFvQINnu-Zfl9-6V8RDA1VFKZpY2NEBsJyyilRet6BirEcw1ZdhCPeyjCvlAQngAXmmslFlcLGEg7H-3Huse009tv-CwrY_2iMhp_KcEn0bXO4Vw6uxENf_-I9jQQOxGetXd4aoMJpIu7BhuM236yCuPU3Ph9DBt9cmoIbnZFyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3KdvTpJ6XIY-nar_1iKo6cYT8ldpSivG29335jKiRrOb6nkAkSjYXqjPlv8pDh6E10x8FLxzu5SZNLe38WI46Ql-bJ1wdN9dPjvb-hTnaTvs9Q8_UrN8hrHBis5nKDefsNVrBZDx1o5s8oZ1-tM3Em0uVaQzs6RvIctQXdwkuvHnElf0CZgRDVd94AmVaS2sLucOqHqxia_LRpadLC3EXje1hDENghi7CIU4MDPRlFXEXstbr8yzxZ8ziatHeSLy3-QQkodpuKp-t-E_17CrhNUhPOuVUD9ZOlF-WJb_Zvb6-YsUQEvGnFI8atF5MHofMPcnHw5uKYUrx6cf8sBdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N53pLiBBgmUbgwBEyjLxAycvw3kwhA3gxAarGe3R8l2rQIlj6xtY5Chl5gA_d-22mLJWYJgoaEcDN_YCsEXnnp3hw099nLrS5CrR1NpEnLMlZsummvYu8Oz_z5zIo1VXbt57JtoLnQAGgUsueUeUebotao8RlSUB4AO9VLUoHRCPzsZizWwYYsJkgyTtaPo1Ac2BN6ph_lklkSbhj2BvqahEe1MjKNBOnUH7wHD1Ga56Wi2qT4Tq_iVKpuC4MbQVClqn58tQSnL3jf-5nWHDFutIeqdzBi4N3JvOEOIctvldPEPmnxyZrfIO_05MuL8JhwN55ha_KvZxzAMJKCE34w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/koV_uRZpJ88QBKtrvensmoX_AZD2TLAphApPw7sUP_IEfB-6dm2ceGIhpicjJVHzG4jLqyAH0epXDfVE2UDXJpz4gDyrWKMuD6y-1CUwc6t2zjFMphY8bNkwFWHYuVjLE1mM8f30DsTjl0AA_Of76HLRSTjEM0uxWx--zAbtZq_DhpHDpuKtnCm3R3IhaW_Tr6Vt5DLtH67VRiSz44WJTx8Rt9NyiqR1FtH7CYzsjnP4j_86C2BSiVaGk_UmCQ1B1O0sABC04MjOlXPPszGf65VQATvYkjx_4_gNnwztD0sByQrsH5roYN61tD6t1EdNK_g8ZttCizqCtdbe8thY0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=eCBh5Zi9R5eIo8VJbHGorENpL0rsXTKLxheyLTltmwTdHJu4zh1G6jlDr0ypU8ReSybpigJGDLTRCRspWClvPMzXjmWjThs0jCRmDeUf_QrYGpRhclek_3EsanZb34SEWv9GZNUNld-1LpgdanJiqYYLaNW3dSv1TJ2UlLrWTSOHQBd_KthRq1N1abRvd2BUMaFeIMWLZFWVhwFWqR1EnPVV0pVekr5K5iyCIMQx81x3D5DJPE-sPPV7cvkW5b7uX0_r7vMO1lz6FkrgsOV5eumYUOpQvR3hDx6hzn4rE2SrF87neOEcHYXr74KOsfk3u0DosdJeQVfYYtYEjCGKrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=eCBh5Zi9R5eIo8VJbHGorENpL0rsXTKLxheyLTltmwTdHJu4zh1G6jlDr0ypU8ReSybpigJGDLTRCRspWClvPMzXjmWjThs0jCRmDeUf_QrYGpRhclek_3EsanZb34SEWv9GZNUNld-1LpgdanJiqYYLaNW3dSv1TJ2UlLrWTSOHQBd_KthRq1N1abRvd2BUMaFeIMWLZFWVhwFWqR1EnPVV0pVekr5K5iyCIMQx81x3D5DJPE-sPPV7cvkW5b7uX0_r7vMO1lz6FkrgsOV5eumYUOpQvR3hDx6hzn4rE2SrF87neOEcHYXr74KOsfk3u0DosdJeQVfYYtYEjCGKrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=MIJGkATlfBOHs5kpUN9oLTeAwV-tZGVwKbg0sOKXbMKXxztpk1UqO7Xhs5YMBJOyTfOw_aPWk7OWE00pwxLJUlxYUNGEfr5mK_zvWiumHLgJxOk8zRk7bjOgroxVOMK-h-QmuVnCmLExARTsskJww-rJzSX6h069Ro6XU7mRfDqBPEkp6LSaxiNkTfmFYcFH2j1tHktbxrqnW6iJCo5GDQ3JrsMBMyZA2dAMEBUxOAy6dxTnlJ2Yzlk6hkM-vxBChPBP7j49SbOKFM7Adq-bMRqNifKTcuHTCESe1rjroS3RJIDtdJpgNHUGRawAMXPlRkKTIg94ud2kCArEZE-bWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=MIJGkATlfBOHs5kpUN9oLTeAwV-tZGVwKbg0sOKXbMKXxztpk1UqO7Xhs5YMBJOyTfOw_aPWk7OWE00pwxLJUlxYUNGEfr5mK_zvWiumHLgJxOk8zRk7bjOgroxVOMK-h-QmuVnCmLExARTsskJww-rJzSX6h069Ro6XU7mRfDqBPEkp6LSaxiNkTfmFYcFH2j1tHktbxrqnW6iJCo5GDQ3JrsMBMyZA2dAMEBUxOAy6dxTnlJ2Yzlk6hkM-vxBChPBP7j49SbOKFM7Adq-bMRqNifKTcuHTCESe1rjroS3RJIDtdJpgNHUGRawAMXPlRkKTIg94ud2kCArEZE-bWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=SqdITNzX17gPwRnDbdvo5AR65ZAWlDEaXnAZLjR_CodxLXGe987Yk9DmEgQq5KsQkjf4GSe24WtH5pVk7K3MAqXWtSXQ8lWbVhM22CxYpS8x9ZM3Ns-DJPFGT62U4bmjn5ZLr7SaKMeM6KUwTf11DICZoHMsC6us4TVGVNdkBxIG0QgGcp0qQ1raaNLEQ3r2ZtB9qSXomGm7NRMRu6IMaP0_N-9bp4OY1QGWXZklQ6IwYc4zqo4OPr5m8jV6kcefPa8YK0vlco6tW9Y2WJkpZcl4JU8YRGgCOfVEzOcB51lERaLCL6wUKICkaCjwAWPi_cW2q3OP2M-nNbeV-H3YqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=SqdITNzX17gPwRnDbdvo5AR65ZAWlDEaXnAZLjR_CodxLXGe987Yk9DmEgQq5KsQkjf4GSe24WtH5pVk7K3MAqXWtSXQ8lWbVhM22CxYpS8x9ZM3Ns-DJPFGT62U4bmjn5ZLr7SaKMeM6KUwTf11DICZoHMsC6us4TVGVNdkBxIG0QgGcp0qQ1raaNLEQ3r2ZtB9qSXomGm7NRMRu6IMaP0_N-9bp4OY1QGWXZklQ6IwYc4zqo4OPr5m8jV6kcefPa8YK0vlco6tW9Y2WJkpZcl4JU8YRGgCOfVEzOcB51lERaLCL6wUKICkaCjwAWPi_cW2q3OP2M-nNbeV-H3YqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=ok-UbpcVDic3DVtWMycczSTEms5KpW5G2rQNh_KfiGompB9qn75UO0LODGOtNB80fH4un4LcIKUN4gbrsY8OCF3iHAh325fdAMvsYPzNAIR5OtzqQG7JdAWPVtsiHbcfYl3tj4RgLjnKDJKPGdpiLQ63cHddJXqi52QKyKjCsVXpFrY-OZgiRj6OGUcfST0cfzvvYzact7_BMet-82VBm4qK9ze7Tm27NvxeVKOjNK1qmxgeYyVtgQyJV6zNKEWf-SqHHhvUhYzwzZCNXHGZ9_JyUAJLvwr8idgz33rFfOVUPOgV-uZRFf4Ra6sjUBPMUCuwuXNCiChvjr_5ZG574g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=ok-UbpcVDic3DVtWMycczSTEms5KpW5G2rQNh_KfiGompB9qn75UO0LODGOtNB80fH4un4LcIKUN4gbrsY8OCF3iHAh325fdAMvsYPzNAIR5OtzqQG7JdAWPVtsiHbcfYl3tj4RgLjnKDJKPGdpiLQ63cHddJXqi52QKyKjCsVXpFrY-OZgiRj6OGUcfST0cfzvvYzact7_BMet-82VBm4qK9ze7Tm27NvxeVKOjNK1qmxgeYyVtgQyJV6zNKEWf-SqHHhvUhYzwzZCNXHGZ9_JyUAJLvwr8idgz33rFfOVUPOgV-uZRFf4Ra6sjUBPMUCuwuXNCiChvjr_5ZG574g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=HNEZ9Ok6BSAdHy6kSbVxxr2H_zEJna0U-7c5N35EAy-Elariw_VnXeaPLg4YPAvJ5i1sx8H3Zz1WuwbeYij5mJDHjhXp0-CE2UORhVdExeE26SJwu5l-1GBB2OtbixRhIbkMeMinXPZZ2fNx0lbuWXZ87-qW6BQfPu2k7-ST1Hy_IKYFYcyTxq2GT5sgn5XBHUDRGdFAIshM1lrSHVaQcEL6A2GzWWjx_1Ea2Dgw2tdXsJXQEpXGNNv-iAUqUfWirv5AWIbSnCkP0-Somi4tc1-V23KLP7pLXSGDCjk3JXDRNBBhynC7x5HB3m9Fhgc6P3TQIOOYB-1NwsY8eyMGtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=HNEZ9Ok6BSAdHy6kSbVxxr2H_zEJna0U-7c5N35EAy-Elariw_VnXeaPLg4YPAvJ5i1sx8H3Zz1WuwbeYij5mJDHjhXp0-CE2UORhVdExeE26SJwu5l-1GBB2OtbixRhIbkMeMinXPZZ2fNx0lbuWXZ87-qW6BQfPu2k7-ST1Hy_IKYFYcyTxq2GT5sgn5XBHUDRGdFAIshM1lrSHVaQcEL6A2GzWWjx_1Ea2Dgw2tdXsJXQEpXGNNv-iAUqUfWirv5AWIbSnCkP0-Somi4tc1-V23KLP7pLXSGDCjk3JXDRNBBhynC7x5HB3m9Fhgc6P3TQIOOYB-1NwsY8eyMGtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=kVfp3kSPPBzeoVzdpDLgFnsm0nIxYOW668BDjZ3VRQJBahCm6_h-uYSMQWa3xiq30EbAE1JmoLmW8cGDdLxCh4eb8IN2I6VQviRBytkNF7WeAoETgD0I8kErPirtB2BsTnEKkYr8PA6yHyLa5585irVU3pK3lCvaopWJa8T3bOQuKUVjZ6KytCe8uyTayBy1sDvqMDdbOA2_4niz_Ly2qOo9jbeuQtw9XQmoLZnTHWf670RuHKNvfXKISgaaykLNX6SaeLhgeCl9Pb10ayXdzLatcQXdyTwu7PKKjB49sNZyYBOPafG05gi5JE7zlU2Mmd_Uulu4YGS9vQrj-37Y8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=kVfp3kSPPBzeoVzdpDLgFnsm0nIxYOW668BDjZ3VRQJBahCm6_h-uYSMQWa3xiq30EbAE1JmoLmW8cGDdLxCh4eb8IN2I6VQviRBytkNF7WeAoETgD0I8kErPirtB2BsTnEKkYr8PA6yHyLa5585irVU3pK3lCvaopWJa8T3bOQuKUVjZ6KytCe8uyTayBy1sDvqMDdbOA2_4niz_Ly2qOo9jbeuQtw9XQmoLZnTHWf670RuHKNvfXKISgaaykLNX6SaeLhgeCl9Pb10ayXdzLatcQXdyTwu7PKKjB49sNZyYBOPafG05gi5JE7zlU2Mmd_Uulu4YGS9vQrj-37Y8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtYV4HChpUmhq2OsYMl9e0uGQxjtULyR941LBzmI-ig1dFFoV3q-gDUMyMvzOK24Bk_-B_XStp4mXP6avaVYr5FY7fWa-JHD94dbmX_bb7s67vUOYL9hxV9mfuLkwm_GSGd4OzwhJlMfpgKUkwWFIe3vrcLtR6Xx_jmri00oNuDh6aAwlfqw8f6MGPKEpSJe99y2bXF0NgExT-xUiHs6YmuE9PO4yAOI8IOdyCKJ0rJ8knn0uz_DRmVWrUb0azmbhzsu0jpSKFYeALo_aTZuf1u8wFeG9cFCzd2O1wBPwQPJxiwcCyp1sVhY4pVQb-_pn3AkpJToqFTyxOgqtYVcMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=HNCtI0a-l3UEwSU4g5ACN_o3kvmr3oukpw-S95xl4r-KzfAo7ABa7r3WV_MsKdRpNLLi6lutGFyGNB6Kg8wcf5mo0lWGmKbqFytS1DzJv_gebhaNu68lVusXtZDtMnM11-R5EAGYSMbLNU9SnqkyERLlX2T7q2o_mp_2Uu7ysG86SkihqaTKBXkgZ3ZuDY41jORdBZbpob4mZhK-mcuA7JdQOBNlqU1G4I925wgqucb7lSnIUBWRrb3MoiBNjdazERWvQ1EYMV1Iy0U0rgqN7gts_dH--WM9M2zZOvQbTbTeBJiQdXF9k_PdkgXsP-WBP7pFtPRHeWbNb_lf8loYBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=HNCtI0a-l3UEwSU4g5ACN_o3kvmr3oukpw-S95xl4r-KzfAo7ABa7r3WV_MsKdRpNLLi6lutGFyGNB6Kg8wcf5mo0lWGmKbqFytS1DzJv_gebhaNu68lVusXtZDtMnM11-R5EAGYSMbLNU9SnqkyERLlX2T7q2o_mp_2Uu7ysG86SkihqaTKBXkgZ3ZuDY41jORdBZbpob4mZhK-mcuA7JdQOBNlqU1G4I925wgqucb7lSnIUBWRrb3MoiBNjdazERWvQ1EYMV1Iy0U0rgqN7gts_dH--WM9M2zZOvQbTbTeBJiQdXF9k_PdkgXsP-WBP7pFtPRHeWbNb_lf8loYBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=N8l80QTVj0qcuaroiAYj9XrRHufDbCkTU58igRplifoNAYG5NYTeBEi_lUjd9KbyI-0iAlk2ZoR_8EnjdBbYUGisTOz41_wTP45Rz9RrpMkjC-0z1Vr7pi64IzaPjha7ReKdG4DAQ0WZTP9wDE-yvMZEb-leORtpmdGhH6oXxgdcM54Q9JQoEpnJIxl4OH-hFsSSoKkBEs7XFMb8TjaQgdW07l3P4-2-r-U6L_1ZU34Wn_UjSCY2u6Ad-1e-mK1qBUZZKXrozgHNVP_lhDTLSqJDjpd3xoDqyKjE6tLvpTYZYAW1aexQTsw-jEMDln_e6j2PG79N3e0WZASwVJ7qPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=N8l80QTVj0qcuaroiAYj9XrRHufDbCkTU58igRplifoNAYG5NYTeBEi_lUjd9KbyI-0iAlk2ZoR_8EnjdBbYUGisTOz41_wTP45Rz9RrpMkjC-0z1Vr7pi64IzaPjha7ReKdG4DAQ0WZTP9wDE-yvMZEb-leORtpmdGhH6oXxgdcM54Q9JQoEpnJIxl4OH-hFsSSoKkBEs7XFMb8TjaQgdW07l3P4-2-r-U6L_1ZU34Wn_UjSCY2u6Ad-1e-mK1qBUZZKXrozgHNVP_lhDTLSqJDjpd3xoDqyKjE6tLvpTYZYAW1aexQTsw-jEMDln_e6j2PG79N3e0WZASwVJ7qPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oIvjRG_Vx3Ve9GQ1qGZIppPV6S2tVuq-TRshI1PczDrKtLLO5iJxtuKFNCbwIY4A4O6RSB1nlBbHMxg4OMNX0if_VLOGMtgBwxw4b6--2jhY3F7qEZ2kez_NDPhE6SFSh1NVDFz_kCYrO_0wH0Cq9NZ7sI_g8uTbJ77_Cztv9kkuZtarsBvgbkPcd7O2QrTsEbLrg4iNQYHnTMAlYaNTUccSYedjYr1yOsdpE0UObbuwDcJ2EhIzRzXeMqhnpJ_h1RcXuiDdyIYj3jhvjEAZWFe1No0uRy6FCZQYBday8NNLfma_r0iI0qnEbwuoGsIUsml3vsPyDiroUIc06-QQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5PyMh3ndioz1Yh5zHqYb5ETBreddqV0x4UoIyUcxIVVb7OG-Fp6V4-5e6XJcIFxZAm_yTifWuEyASw2y9v4VLYIyG9oCGkT_7AmBigcvKPOIoj7WsEqIzj-ZPo6jizmulAOr804vB1YTkz7mC6BOf4MjgVMQTPWURzT74g46CmFIZIa6BZ4cm_tjiC0YRdtrDW4BISv5BIFqDtkVHGjfT_u1zp83Vz_kN9J143kHDyVU_xZvcDMPHXPKlmb_Z972dr0HXnyod9pUgc3xg6nkVI16UirsK0QIenRcb1CjkmhDkra_oU2vRFK9TtWmicLdampz80_X4xZAgfNbp0aPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyYH40CfWDXoplJzYitNtHT46mRcDmnUQRjgw532WcN-bbuEfBHTedU4BLQ_QiUsseGj79I9GRj6ZPL0WXAB6HEklDCtvftTXVqIgV-V0quqiEU6ZbgP0H_JC7OtC_HUm9lCsvgjaJ6MyYtzTc3S0iyF3zDuUH7qTvZu2V9UaIjWDypFdM19jAhbVbcgDnZIeU4E-hF_Y7vUmLBo-Q27CEziefsyczbMvmlWCMOFu5NTV0SVr0UiehNh3h-HKboQMRUTfyXtm8txvlDQ0Wd9Rzt7lxZ8Kn3JyXIaMNqRfIxI4XYvIUW8qIl_AxLoCoAb_0bmWPrzqCwlvC4M4XsOQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vDeOPvWrnJN1K5B5YDtYdi9e_mqGkhA7S7JCsSGRWQDuwyKYVob3vmmxftwtp219JOF-TrhGCNd5hWwNNypRZEzq9M1H41L-cXVvtEXfDGQUEbAfWHid6cUERCTiBMAPEZGYCIj4Lny-nnZVq4oHO6i2RLyuOh-VCmvWGx16h2F1Kwiih9jOomZBhnytG_3vkj2U0vnNkV4i6NTah-w8UcKw4tu1RRuCeVpSGEZI0ujnWGDgpXGFxI2Wi3DsLev7TDSeSGlEv0W-9f6AyoQ7fr0NRS9BWVCL0LYKpNkQwXcsg5b60a8Ua4lC1pH-W68-LUXy5ln6hsPUbfDO5H2vZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAOZtIyDaz5t-33kjVjDw7UZXso-7UjiaufsgP7bvfqRLVQZJyvnldorFgd0Wr_-vlZ5y_FDm-FL6SPr-lySPp77GKVjit9u94-w2UQMLPX9PxBUOw0fiEtsdqLoDsAuLVjjdKZPmP28UlqaQ0Uwr5tMQI9XmsqGXnq7IXm_vpsP9qehiZ3nNcHfJoP5vLN1MOTm8a7B5X3uA_7uVvU52zkjUHLykHfg-ToTpgdQhXvUAJ5_ej3zWfrd0frrjXTxkbI0DZ2hQM05DpzeHzh2sC3FPI5NQMS2bks0ad7TSfK6SDHpn5dq8Gzo2ehvsJsLCS5nD-Juzkj3_HadN_6Sng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1Nzx0Vt5LYZRdmqZTu8iTeo3K7k7RwCrGKicPKyI0O14wsQMcx3-PqB42vaANyB-KJ-bqSarAX5egZbcSfJn-KZzHEcyZPSqjGGBwuOyhAO65jRt3QoS-JHEanoJYfE3wqdpfnn7gfUZvj_LrDgPXmVErZ78CCpvlOI57qAxpcEOYx4BG5zoND8II6Ry5rGNi4DRw253jiGPFBxDWDgOfmhpKSW14KQP4ngZxUb437wAaY0lwJei5aGaWZ2b9DTb1W4sHe6DyGffvm4DoR6611hj-xw-P4qzMnIcl0YK4H6ocbfeXEW27_dVeyp-ZpBha-9-VOMC7eaXn63WbnFZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/chocAMrILs-3zUlhZfKuCwRg-R53OZYOUo5ByN4cSayO5HcRnArggYciiuQ3xG3M32w78FGYIQ7kZwyV4EfMCh4dgNzIP6suWD9lpOAVolXWhQWBZtWL1eHBqJyCAbBLP1OAi7vUCpyZJ3uGpLPXZ7tdRuxKNo0oDotx-8TtaqyF6Z9Gid3AniKVOp7OblTaNvvMQvEla86YbCFVPAKBNwZWziS8rzS7ZZLFGaXP25osFufSdySv7fMNmjGjVkSLgC3Kq3GiRwm2CBqzaMl_jafGRGATCQPROO7SYNlb1MF9Kh7mRmindA4zszW_tETT69QFypiOUDLxhGNaZC8qiQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vcF6YC4K_jRgvK23LI8e8C_u6xcPHCI_eWKbdoyQjJhMHRsaRqV22MadYbSCT-RIJxaIravr7cPmmr-GdCEU15j1D5tkTEoa337VYv92vep_BXeR4mBpkusBTjAn2ROtN5bdDCDDz83Bwn2YbfPu6hdM1bMMuDNwo50TUWQu7EN6QuO9zZuv7On7lqgVxMSNPkpuLPpAjPkqOZwaPILEQDCrhhY_ooV3twx_gVA0jBoUV2cVhXMpXLBShIZXUCyFuWykMoKlb_4h8KSgX_yK2JjCTVyLTZmootr6l9nY46ZYl43qdkiEOTYDP1n4becvc5xzpi-jg2FdgWZvUT1hBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h0g0wQ3gHOf_jahsOYHSWdPkVOXouTmhSY5kvWBLC-4NF6Gqt3y9XNT7PN1ZBE9O12UrZxbOKVGj25K3DDEIVQwr25lVwUsbHepCgVekfMaPsv9yswAht-oAs7Gl6MyLpYnOnyd4VDr1HvJGSA1h3YRKpbXPaFfoHHIcvh4zSScM8MF_CiTjdCA4g_yPMDjChLZEtnZVacAShYDvtKuf6Y_TAy4149JsxYNc3f-fbJ-Pg1ob67iXjHdgT4ErdBc4rUOaUWCxvx5OfD7_b-BiVfTkF5y9MBhltXRKY09OjmfhkynEU0F-fGEMzjBJj1BeAed1Hf641mBJCKzo8GrYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwNmImw1QjGEewHzEHGp7N99dQY-tJPzr1ZFT7nKamVLbp1htHKcJeKGCAnJbdZVqeUJeYHAtH_YyHb8Sfr-Bl4n2ocH4skCWs6PMFyLff8NTfazT_FbKCr74FC6hZrKaJRYnWgq9GrFF4qtTedX7grKRHOnNLxk8D1nRzj1wZiSEs7lfbyQaFXxAgS45PK34RCFoXLQe8uXGdZSTNJvq9tR0qj6-gKXiP6KANwN-DXJWTkCYujrlVKePl1wRWo2ZnjQl-rJA2gMju8eNagOhVzIVPVaEy5xXJT5oa0xzDR_GkP-6OAYeF1OMggm2SQDkO5cnf0LcGnlTaCaCwXnQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/id774mXHbOwU9TlN4J8xtYN_EVMlVXU2Uii1jFMAcFxSX_bkDBUWcT837P92scy1BYqxWxXAYHhbsZTNpgifhInyozHfBw805aY84ENzmho0skJCzVSysmzt4t09T7wykPT1kGzK8dhKHHpeDS9D-OiXHY_DNIaJgw7L05w2_GEZifEsaAMyJlAXEicKnfj4j8jyt7KAluVTEMUeexSM26rqts4RpBIKRU7rdOdfFn44UatI_SXJi3PZXbd0NspjWfCUVK7p8Fd5GVs10wiXqFR8nW1yKx1_q0wsyFpAzaSZIoIKsyHEYiIUhJKnX-f7lWfG41Ntg2G656JRGZJQlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=ls3DU-K6ylfeRxiS7kaipqTy7ih__PA0KNOL33bAB_ftEr7HOfD7fq8uuGQFTa5Dgko1Ubl24jbZtDWTY8Piv0iPpcnFQDPhQXTX8AqfYlYzPab1mCfd__1bPy5Vl_iYoC51nFaa5iUyBDd4MfEY0lMSe75e4bLymosh4d2YELMhzJx3rNXZzsChxSyjCvE1mW3AWeRepjdzfLgQirUA3RkvEdw0rfI_ypD8j0PGg4hBWknUX60Q8MHBtCfE4hiHMWj1mwvMeRuUJl62lny4uohJGoiBy9zZAQONattP1M2OwJoUsAWVR13TApdQ_PgrwjfyTmM-NfGbcRmWoRw3hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=ls3DU-K6ylfeRxiS7kaipqTy7ih__PA0KNOL33bAB_ftEr7HOfD7fq8uuGQFTa5Dgko1Ubl24jbZtDWTY8Piv0iPpcnFQDPhQXTX8AqfYlYzPab1mCfd__1bPy5Vl_iYoC51nFaa5iUyBDd4MfEY0lMSe75e4bLymosh4d2YELMhzJx3rNXZzsChxSyjCvE1mW3AWeRepjdzfLgQirUA3RkvEdw0rfI_ypD8j0PGg4hBWknUX60Q8MHBtCfE4hiHMWj1mwvMeRuUJl62lny4uohJGoiBy9zZAQONattP1M2OwJoUsAWVR13TApdQ_PgrwjfyTmM-NfGbcRmWoRw3hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nWkWsEhBjXecfKrEcLGKD8HNUPU2pGQ403ZbqRnxKBdGSIUG1MM-BURzM-nBQ2Vkdgj6YgltTpuam9o6F_4UKq0-6ynn37gWL2M4EnX4f1h5TQ-J7HVjHN6bGHy4kYu91uoJg-ZLlCJz2TZ9OBB0fXZwlaWKg6nwbm-8-h0rps1GOHQiNAZ7wV4s2Gv2wFDuzQ8BCu_PLoKYNjZx2Oi8gwWeTc-1uYw5LZPSHoE-msG4eSbjXS-_GF3g4nLafzBMtBV0qTq2FvVZRlXFHTi0vJDbKjdIrUK3LIp5Xgo2w8f1o3GPzAdgNk0M4RUwpB-Z9Jg5jfuucCimXpRPdB867w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=nWkWsEhBjXecfKrEcLGKD8HNUPU2pGQ403ZbqRnxKBdGSIUG1MM-BURzM-nBQ2Vkdgj6YgltTpuam9o6F_4UKq0-6ynn37gWL2M4EnX4f1h5TQ-J7HVjHN6bGHy4kYu91uoJg-ZLlCJz2TZ9OBB0fXZwlaWKg6nwbm-8-h0rps1GOHQiNAZ7wV4s2Gv2wFDuzQ8BCu_PLoKYNjZx2Oi8gwWeTc-1uYw5LZPSHoE-msG4eSbjXS-_GF3g4nLafzBMtBV0qTq2FvVZRlXFHTi0vJDbKjdIrUK3LIp5Xgo2w8f1o3GPzAdgNk0M4RUwpB-Z9Jg5jfuucCimXpRPdB867w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=UHserMN2Jvgi33-eJLyG2WOgqjiHrOrANg6paSU8wjtc7owhNHTkiOiJvO8X2BBHVoBRQ8Knv6NGJb93GC6BXeeKr46YSytIHwy5tkiF7v0YaeSNIiQqeS3NVf3443fzZaqdMByVXIyA6Q-Fdu6FKL_YhEQ-JyUsgvAt3yqSi-A4L-4BaY6vA_HBY5U1t5u1LY9t9hchxDq4ge9vptJJhT3VxO0IcrWFY4j3g420wxJ5-h8WIrDAV0NYZ7Xt11jBYx_7l44D-UimaZB2DNqjkC571TqEOhfcBt7iCBp93h5UjrztEES4KzxmxdFY3I-1Pw7cpQhSA3Dx5URmf8SDLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=UHserMN2Jvgi33-eJLyG2WOgqjiHrOrANg6paSU8wjtc7owhNHTkiOiJvO8X2BBHVoBRQ8Knv6NGJb93GC6BXeeKr46YSytIHwy5tkiF7v0YaeSNIiQqeS3NVf3443fzZaqdMByVXIyA6Q-Fdu6FKL_YhEQ-JyUsgvAt3yqSi-A4L-4BaY6vA_HBY5U1t5u1LY9t9hchxDq4ge9vptJJhT3VxO0IcrWFY4j3g420wxJ5-h8WIrDAV0NYZ7Xt11jBYx_7l44D-UimaZB2DNqjkC571TqEOhfcBt7iCBp93h5UjrztEES4KzxmxdFY3I-1Pw7cpQhSA3Dx5URmf8SDLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=pworkK2wfBhdoEOHRdqmoknxzFM_-cXCwUjx4y1UdK-yB-ek--2KlJ9J-m8VBqgNJ2HRYA2JVaiJ1xxmIoFAPtSbiJ69JaxF9N0tnnDoaY1OpAg9w5aDsrDnraYATu4ySypdN1WAE0VS9_hr56cQAR6EyLLwA5mEtYYnrc_fygqXvPJLOARqnQP9nZzaQ8une_InwkclPD6FYz_QZKxQgXfaeKJX-72SL4gvtRqncAUBpfWH5ewVrDqjGWgkY8m9qLRVnXC9ySdwkXzZ-BSX-Zb-tDBfZgUCqzh0kbEHk3UbJHYxGcCtepHN0rY5o9lSGDQE6N3nPsV-0eVO6bvIQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=pworkK2wfBhdoEOHRdqmoknxzFM_-cXCwUjx4y1UdK-yB-ek--2KlJ9J-m8VBqgNJ2HRYA2JVaiJ1xxmIoFAPtSbiJ69JaxF9N0tnnDoaY1OpAg9w5aDsrDnraYATu4ySypdN1WAE0VS9_hr56cQAR6EyLLwA5mEtYYnrc_fygqXvPJLOARqnQP9nZzaQ8une_InwkclPD6FYz_QZKxQgXfaeKJX-72SL4gvtRqncAUBpfWH5ewVrDqjGWgkY8m9qLRVnXC9ySdwkXzZ-BSX-Zb-tDBfZgUCqzh0kbEHk3UbJHYxGcCtepHN0rY5o9lSGDQE6N3nPsV-0eVO6bvIQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=CAD4v89c0OCXq_zXXuDbzf3T5VXxALvFMV_Nv4hzXODr3_1lA_99Eeg6VZidRrgtT5MSyj1DaW5ev5ClM-GqTqfPkQY7ueDTrILdSKU5cnHGz3uBTLNqjBXQWz5FRjgyDEG5xpxqPJV6IJkJZbgOqpk1ECYiVG5fzuvit0M-zLWDFFBTQQITMYB-VNIlbpdBELBIB0SUR6Xmjrcfq0SrvV3SGko7MSHd0gfqzol3g_q6GU5VjmOlD6lLkkaZyir7VowF1LdaOZqtb3JzDW6lKuploPiIoKZwsLI8RnDPMMyJh1WILtEfwBbvPI_yFUF3HtjJeJMSiy6Dv-zRUWsvaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=CAD4v89c0OCXq_zXXuDbzf3T5VXxALvFMV_Nv4hzXODr3_1lA_99Eeg6VZidRrgtT5MSyj1DaW5ev5ClM-GqTqfPkQY7ueDTrILdSKU5cnHGz3uBTLNqjBXQWz5FRjgyDEG5xpxqPJV6IJkJZbgOqpk1ECYiVG5fzuvit0M-zLWDFFBTQQITMYB-VNIlbpdBELBIB0SUR6Xmjrcfq0SrvV3SGko7MSHd0gfqzol3g_q6GU5VjmOlD6lLkkaZyir7VowF1LdaOZqtb3JzDW6lKuploPiIoKZwsLI8RnDPMMyJh1WILtEfwBbvPI_yFUF3HtjJeJMSiy6Dv-zRUWsvaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HWfLAMod4aDLCgMgCorTZWRwVhbGYNkIVQ6XxT1LHGQGiGnvkcDdDZjh43INPDTiJHFoyNU7Uhg_hWSiNy6Hr0iPqwN_4jbmsO3tdKl-YYTMqODyaX860LKaCY06LzWFhlI-XKHcb-HSFmzc_CBd_0I-zQmzHTOX0uO4KiLcN9ts9nNo8EqbAGCGI4bfmKInlHL8YsQqRJYl3E0UgcX5RX41yqdnkq0JGxzCao9WFnSA0N1SGA-xNYoklEYC_sCEQWxeD_xeWqqJ0LcZk1tp8eujrO0ntdDiuI6pPGwu6dVPmcphBYCmLHaY7vgpyUyZlPtB8zSk7wXffgvSibWt4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HWfLAMod4aDLCgMgCorTZWRwVhbGYNkIVQ6XxT1LHGQGiGnvkcDdDZjh43INPDTiJHFoyNU7Uhg_hWSiNy6Hr0iPqwN_4jbmsO3tdKl-YYTMqODyaX860LKaCY06LzWFhlI-XKHcb-HSFmzc_CBd_0I-zQmzHTOX0uO4KiLcN9ts9nNo8EqbAGCGI4bfmKInlHL8YsQqRJYl3E0UgcX5RX41yqdnkq0JGxzCao9WFnSA0N1SGA-xNYoklEYC_sCEQWxeD_xeWqqJ0LcZk1tp8eujrO0ntdDiuI6pPGwu6dVPmcphBYCmLHaY7vgpyUyZlPtB8zSk7wXffgvSibWt4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=BDVnmtTot6by9kY-fdGTQRCO7tTdm2V3wp9C7WW5ZN2JBCW0wOKCG6_8eTJn0pmlKuxfS_KNLaSqwWS4H5dk64B6rATaLVKrUkVeCYiRorFVer7LR6VrM0oEgPyfM9F6mgrWggGttL6O6vzWs5UfrGFuRXiQPYdsf4t9cQlHThd9_4rdymhJ8FgXQbxbIuUi37KJiU4BBKwxUe22sZOe-5cqYMIHpZmdffqWUSHV4B6v6V98O9C9iSmRi56CH11l6NAmpT3wdlHL1fhbb4148ONZyMBauhx997XpDXBAxoxag22Wwj2_oHINbrGUFJZW-nfNhYNybwTGHv2dj7tj-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=BDVnmtTot6by9kY-fdGTQRCO7tTdm2V3wp9C7WW5ZN2JBCW0wOKCG6_8eTJn0pmlKuxfS_KNLaSqwWS4H5dk64B6rATaLVKrUkVeCYiRorFVer7LR6VrM0oEgPyfM9F6mgrWggGttL6O6vzWs5UfrGFuRXiQPYdsf4t9cQlHThd9_4rdymhJ8FgXQbxbIuUi37KJiU4BBKwxUe22sZOe-5cqYMIHpZmdffqWUSHV4B6v6V98O9C9iSmRi56CH11l6NAmpT3wdlHL1fhbb4148ONZyMBauhx997XpDXBAxoxag22Wwj2_oHINbrGUFJZW-nfNhYNybwTGHv2dj7tj-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o3jiEdTWFiDxod20B4iBP4ZjJEFVI8x_g0I-lRbgadfrsUyS7zEHLyOre7yuBSjAq4b3_hvna-25fkCWn8hce_A3kvlKH3K7MvKQ2gLeer_1ctCyhTiTUeUifso77-rMXlrFvL02-tfJ_x1W66zjaUjJljSOqpcDawVbm_0XxQf5BkILjuyQ1KKoFnmbxM7NKtTa9zbTyrC5K6cADjpDdEUJdwmdSwHfJfiBmB6FTgd8TMlrg2LtV9wRIz3ELkjVyYslS_QpaNI9a81aLYP0ef1u-QuPJq7GuP_PQ9jtepLIym_rzBomFzXDsUu0DDJzqlxbb0pO3mco-LOOnCpQ_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=QNFbw-23U_De0shoU4QRSH5eupqGTnicWaFmtleA10tN0aEImpN1TTpiu_jWv_gFouayhCeeHDOY3XRt3_ICXOqFvPhIGr5aUUDlX_HQRpy2zCwuwz2TmN0x0dEQaosUIiyfG48e6ZldkJe4lfhgrIaDikBnP3wJ2jhF12HCxwsLYe0_c2oCARG8AkZh1MY5jwnw2J-wD-sq1p7WRiCyCqhewkmrHq0ct5DttOvQqsWCNyRKif9xTfM3rhhzbWd0h7lXALtoZ5ZGYaupQ29DrFzc5nrdAXOeCLcPiki4Qx0NKO-99H2gY_wDXZ2w5F2AIPAoe3FtZeXg0q2lpNPmAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=QNFbw-23U_De0shoU4QRSH5eupqGTnicWaFmtleA10tN0aEImpN1TTpiu_jWv_gFouayhCeeHDOY3XRt3_ICXOqFvPhIGr5aUUDlX_HQRpy2zCwuwz2TmN0x0dEQaosUIiyfG48e6ZldkJe4lfhgrIaDikBnP3wJ2jhF12HCxwsLYe0_c2oCARG8AkZh1MY5jwnw2J-wD-sq1p7WRiCyCqhewkmrHq0ct5DttOvQqsWCNyRKif9xTfM3rhhzbWd0h7lXALtoZ5ZGYaupQ29DrFzc5nrdAXOeCLcPiki4Qx0NKO-99H2gY_wDXZ2w5F2AIPAoe3FtZeXg0q2lpNPmAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=YteQGCs04ZxzJXc7c9WiKR8YZ9MfqOBmcZZoGTeHV0jtzmIDdudu0fA3wwf_W7fuSE4F96SxREvycyQVp2N67ia3nvz8CBEGQ_PtXmqG-raLS9BSzoMcOeK8H5wkQoBYbF1KXaiR1HpIpMl2AVfKev_1RjplfkV6S1TKySR1mHIiYWzgbBY2GXw1x6TU76Wxjbm4GOhZGvZ2iK1HHZg_6yJOhP3nBfwQdu5RdsVCaoBSuIknK9bsRQj_qrKL7LPvTnDmmq4dofEpCkLBxqhbu7utcpsZjjnhyJ7zgaiS-8NFdvzD1FgQbT8-eGjN4sfWaSld1GBN45z61JcTS8ebRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=YteQGCs04ZxzJXc7c9WiKR8YZ9MfqOBmcZZoGTeHV0jtzmIDdudu0fA3wwf_W7fuSE4F96SxREvycyQVp2N67ia3nvz8CBEGQ_PtXmqG-raLS9BSzoMcOeK8H5wkQoBYbF1KXaiR1HpIpMl2AVfKev_1RjplfkV6S1TKySR1mHIiYWzgbBY2GXw1x6TU76Wxjbm4GOhZGvZ2iK1HHZg_6yJOhP3nBfwQdu5RdsVCaoBSuIknK9bsRQj_qrKL7LPvTnDmmq4dofEpCkLBxqhbu7utcpsZjjnhyJ7zgaiS-8NFdvzD1FgQbT8-eGjN4sfWaSld1GBN45z61JcTS8ebRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=pfVONw2e9npjLNWTAEXm4aTAsIVsKNRTp_jSNknRwc4exffp0FI1-w74zMHjUeK9o3fzB3rft3aYigmlyNMdRVXe5l4ZBVoL_r-1vEYIZl5Sw1BOEEf46tL8Nj_PVf7MFfne-9MZbM0zRXtNFTgALooVQKY2Hu2giaq714kbQV5uh8e0S2U9XdYUTvk5-2BVzkdKbVijqOULj4r_ot6qLJDqsD5IJ5exYpGCa1XznI5xZK1kO4k2gk4zJB5sDAmshsAHbYm4XMe5rAADj_laPZKqg2-p5msTCBZ3k--2iXE9mn238XR5ZN6jt8WqwmDvtlL1CK1lhB-58QCRhug_VL13IITK2lwhCRBObRB5cQiLOYgq9v2yL_8no4sGu4UdjW5fQX-dxUE-TQPTwEpxlcVSJ_YW8yMb3UOOC6gCQekur2nI49VmedmXd8GoCf59BzPy_Y7vK_YHIVv7QdBYIsPfZEyAtJ_Y7beTczV31xnntN5j1K9mIUGVdpU7OSX0hn8HXvt7dcqPYQYIGKDUpUnTTxqZBW71yIZcbQmcIHLuEa7p0WlsOLHlQL5FO8tcxDNKylz7SJMgdexGPLCiUs0VnNWCCin7YEHoZZvx5sW0S9AEw8zWjcgOebLNgf4HOHacin-zC0NYZSW5aph0GXYTLEbEY4XXdVLk0G7hZqs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=pfVONw2e9npjLNWTAEXm4aTAsIVsKNRTp_jSNknRwc4exffp0FI1-w74zMHjUeK9o3fzB3rft3aYigmlyNMdRVXe5l4ZBVoL_r-1vEYIZl5Sw1BOEEf46tL8Nj_PVf7MFfne-9MZbM0zRXtNFTgALooVQKY2Hu2giaq714kbQV5uh8e0S2U9XdYUTvk5-2BVzkdKbVijqOULj4r_ot6qLJDqsD5IJ5exYpGCa1XznI5xZK1kO4k2gk4zJB5sDAmshsAHbYm4XMe5rAADj_laPZKqg2-p5msTCBZ3k--2iXE9mn238XR5ZN6jt8WqwmDvtlL1CK1lhB-58QCRhug_VL13IITK2lwhCRBObRB5cQiLOYgq9v2yL_8no4sGu4UdjW5fQX-dxUE-TQPTwEpxlcVSJ_YW8yMb3UOOC6gCQekur2nI49VmedmXd8GoCf59BzPy_Y7vK_YHIVv7QdBYIsPfZEyAtJ_Y7beTczV31xnntN5j1K9mIUGVdpU7OSX0hn8HXvt7dcqPYQYIGKDUpUnTTxqZBW71yIZcbQmcIHLuEa7p0WlsOLHlQL5FO8tcxDNKylz7SJMgdexGPLCiUs0VnNWCCin7YEHoZZvx5sW0S9AEw8zWjcgOebLNgf4HOHacin-zC0NYZSW5aph0GXYTLEbEY4XXdVLk0G7hZqs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=aIZ-OpgBLxbxLLjYK8jD9kp9GvZRF52EODSpC_MOHLgtPsKItuptRHwZdZVqSnHe0LvLpR6zSO2JDMBEC1Py-xA9dY5zR9o_zcTi6m2BH7At_VEfvKMIi6oNenXtzeivWGBtRVQ6jgYMLOj_1_pnAFE0QRJVRZYTv46zTlLW96PUhybB2kaq6eOSyQ6PGOKFyRaxXYdKJ28ros31PHXsQzs1dbSSA9ofB9NqPjKw08oJYmIuMAFrqk-lfQQtPkOnIN4pkivEMFq0sPAOT6YeURAfE4FI4u3eotqql7tiG6RnJuLLCRU9dLgX6kRDW7ii013LR0JaM7on0BHEjANlwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=aIZ-OpgBLxbxLLjYK8jD9kp9GvZRF52EODSpC_MOHLgtPsKItuptRHwZdZVqSnHe0LvLpR6zSO2JDMBEC1Py-xA9dY5zR9o_zcTi6m2BH7At_VEfvKMIi6oNenXtzeivWGBtRVQ6jgYMLOj_1_pnAFE0QRJVRZYTv46zTlLW96PUhybB2kaq6eOSyQ6PGOKFyRaxXYdKJ28ros31PHXsQzs1dbSSA9ofB9NqPjKw08oJYmIuMAFrqk-lfQQtPkOnIN4pkivEMFq0sPAOT6YeURAfE4FI4u3eotqql7tiG6RnJuLLCRU9dLgX6kRDW7ii013LR0JaM7on0BHEjANlwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=JEy_5x5wTZ9vGZDEa4OCjADWrkQ1SCdOGaZzqwzgiHrR2JiD5xta9297cUFvVs88vsW9IxRcZ_f4OSbwNTKZEshcApt35LHjmpyYla5IuY_KWaTR50W20XjnD84OJcIa9h-rFfBLJZfFarTDWyuTfXfy-OBPtSdVIl7itPtt-Z5aD5T9QmlWMg3BSwIgDsGKCsFjoxjzV8CsX8hIYA873Md4Z8bfYEZ2C3-9CH_o5ZwIIXSTHTEUYuEdc5BU7m7aJ0emITJR2gHcbN_cAiOOufoMZWKh2SXvZ58MJPXNKQPXkWCGjJQ9JbUtbaipadxIQn77bPzvJQNF_vZqoZBV6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=JEy_5x5wTZ9vGZDEa4OCjADWrkQ1SCdOGaZzqwzgiHrR2JiD5xta9297cUFvVs88vsW9IxRcZ_f4OSbwNTKZEshcApt35LHjmpyYla5IuY_KWaTR50W20XjnD84OJcIa9h-rFfBLJZfFarTDWyuTfXfy-OBPtSdVIl7itPtt-Z5aD5T9QmlWMg3BSwIgDsGKCsFjoxjzV8CsX8hIYA873Md4Z8bfYEZ2C3-9CH_o5ZwIIXSTHTEUYuEdc5BU7m7aJ0emITJR2gHcbN_cAiOOufoMZWKh2SXvZ58MJPXNKQPXkWCGjJQ9JbUtbaipadxIQn77bPzvJQNF_vZqoZBV6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z8SaF44QBe20Zk6_1aaPXgw-ZjIKl_zw8hIK42SRubrzmnbzqb0PsV0CWScCqMuVgLvKzCJCh6i-QG80U3jR6tnnZ3vhdaoTN-WeZhOVNhla0CIA62hzk41MUtE92JvwJyI3j8D4JDS6WgKY874XdDmLRpm-src6LfUiQ623DronYLhOUFgxTjuDpFcSYIlCnS0zKheF--RbTJjM8K1qBPf2zJNIjcllIY_uRmFJOl94YABu87ZZOxPVdiZLMWfzzEQIBLP7dL7DtmFxfdPKvshjd0ZJ_SeLeYl9OJFO7Mh4kg0s5XNatRBejMeWuiLsS0uGt-rO-pnhyyW27Jj3ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ra3Bija6asUV5KBKWU32pOP_j5wNaao14AGuanwx5ooba_PBNyUVgti4cmqA2C0sW2hiJcqjZO16-8pLRwFFo1UX-Cq3COeXL44wwzXZFOsyn6KAYE2uY5diWLiYZM8rRpR5CBldXunxqhDE3h1C4jwlRYhsE73h8pd694i9lol9mnLXSM7TTKrdFXuE6YuGSMzjLEYGzG_wijSyZ9NiQFYb3xcrwxop0Xbq4SBCfuXMiaw58yw92OePVjdQlrFEUqBsm6XeGR9DKQ2kE6MnMhD9ZhGIKLnwWGBnJSad6rf0KI2-TmewiCD7FMnmcP0IK35YiRmAjW1_7kzTUi6tjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=DTzsOikoa5ewSia6XdjzuwoefbRuTjivm52GiKVss8T4EA5AI9VCQfYp-8TvVQO0N5BFlv3iWgIJ-ls_44g0HWAcTk7LuKak2XKlmiPQZC1yEYOLIu707Knku7Wo_RlB3jexFPC0sZ0Ovs06mMu16hzERsJVqhl1ZrB6fMZOb9bkP7XRXjOd6HdrQmyaQWNKyc7JePpszI82DFD1A087p1Pz9MOljxlYlNkzl4zaGqRIAeKCGBN0dKqbowBWvvZ1VYNN9Wky3_yUjAG_sTYbECiNF1GXkxccAaBiL8OXp_2SpJvzYDfZOYknJLYgBNq2mUgiq2lfp-bBxMF0H2ybxLisNm0jDFrSOt8dzDknf0Vr-BqasN48YhuTHwwXqMopVgVGBKgPn9N3XqPxZpUCAhjTrDhwPN2tlkK_ymeA4ll6nfA4ZN1A5WytAhJ-rsaV7vn7Fr_N_XRryur25kAVhJKx7iP6aCMJ8Wxq8YCQkphOrPdpL05szWjI7MuabtqbIhIKozmpSk2wl_qOuDrBsnwUZpwRH592XTAWN3_3SGABdqK-qni6bjkqL2-tessObNqS6T0G_S8z_-ET4xtwBeTgqA2pBGWkFm4HcRtFu07TCcgzuhroN8Qjjp7UWZXYLgUHN1zK3Ob41Z19bf3lBfYykD-0p7lvng7ICGgtYZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=DTzsOikoa5ewSia6XdjzuwoefbRuTjivm52GiKVss8T4EA5AI9VCQfYp-8TvVQO0N5BFlv3iWgIJ-ls_44g0HWAcTk7LuKak2XKlmiPQZC1yEYOLIu707Knku7Wo_RlB3jexFPC0sZ0Ovs06mMu16hzERsJVqhl1ZrB6fMZOb9bkP7XRXjOd6HdrQmyaQWNKyc7JePpszI82DFD1A087p1Pz9MOljxlYlNkzl4zaGqRIAeKCGBN0dKqbowBWvvZ1VYNN9Wky3_yUjAG_sTYbECiNF1GXkxccAaBiL8OXp_2SpJvzYDfZOYknJLYgBNq2mUgiq2lfp-bBxMF0H2ybxLisNm0jDFrSOt8dzDknf0Vr-BqasN48YhuTHwwXqMopVgVGBKgPn9N3XqPxZpUCAhjTrDhwPN2tlkK_ymeA4ll6nfA4ZN1A5WytAhJ-rsaV7vn7Fr_N_XRryur25kAVhJKx7iP6aCMJ8Wxq8YCQkphOrPdpL05szWjI7MuabtqbIhIKozmpSk2wl_qOuDrBsnwUZpwRH592XTAWN3_3SGABdqK-qni6bjkqL2-tessObNqS6T0G_S8z_-ET4xtwBeTgqA2pBGWkFm4HcRtFu07TCcgzuhroN8Qjjp7UWZXYLgUHN1zK3Ob41Z19bf3lBfYykD-0p7lvng7ICGgtYZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FxcW2A5GlmwupfLG-K30Jx87lOuGzp0krLgYE_kvKGSNgwi4QI1pNvUPrJNdi7fl--eizHsKJM-WmD2qZFRnps0KTtNhGT6LOPIj1zKTP-TuZwRQzueO3v_7AWdJKuCuFVL6yc20pITU9B0k_tIl81vUQL4AqK5wOirQn3MNwsJLAJKc6gyvzvatvWMvUw6lW3JjqmiF3W4RNG46lCeS-KUaD2Og2YW2fc7dhmnP_QPti4dWl0A3g3mzXKQefFqbovpJEpuYN4do4C3OyDRlojdurcILoTrHmpzHtkCqSjj6UveTx8nToD4k1l_-rIXKaVpW7f1s-Nwe3sGoH5x_nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9eIAC4uqxooFVQvd1AZxAJ4ws9owAVUVZQOmtlHdAf7jDtFGoSaPy7rUAjlWDxDa2MYa2yzjKJAKzOh6I3j3NvySRUw3L4p6WfpwQGwt753NfiAQr8RwTHLWF0-7cCGvGgO-uKWtOAyRYzqPkqL8xjEPcjFIFKiTRvI9xipNcIjHPIjEVobMTRxRi5mUHIkootIu4tXNdFn0OfIaJBOWi6XoudAQKioZwd1YvG-AlR18modHuFdWAa-f8QVwpn3MSYtTs16tuvIemfWEkBxcDCFzQcu_2YnJSi7M-738Wds0P8vVBoxh_14MJIFGObLqXLn_XdzUXZULSAMPNGG4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mi8Moejh1kPHYEGGmIyp52urgQOCcp0RiTS3Kjf8g8kUp8JCPo2o1rzWOONLtOI_WowQG1vjc_j5raM-ECbZZgZfYa_z02gY_vyNslN5S8SZJZS2tzQJhEBC6eRUI7XNl2DANutDyAuH4CTchM9P-uxsYnnGNuDAe_ul2VA0oON2oXfwvU8ff9DZZs8GPkxbL6J_kb5gnO8zO7X6uWMfUfcxzgDBV-3kLh2-CcJ73Z8gC-DSO5pNLNYE3NVIzemGodf2A1hPDmxIlBydkqV59Tz7yFS3fAJZZxoJ6P6UV_w75hbcsy2niYPZ0kVwQNMiBIWwwFRL-R29IHXqCSm8AA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X642x75lfalHZlprt2pUqvmTbyOg-eCErd22rjhHNNkL1_VbnsG5Kza_Ayf0V063dBYq-BDxaOC5QGd1QAk-nfiY4A1Ujwh8ACf-j3f24HJ8IIhgRUGRWcAd_rG33zhIlqlVBZAHiDtppAPLZpI0enRNGjishZajpOFyPjVam-QV0c2TEHIRGmkS9QM8L_7CE7TUvWFPeiUpgr4KvaKq0jxdCuDzxZc78HQWIQqIhYoEkSX-8oxvHdv-6JQysMiuOlKe3ZITXKC02VOegfc3lHwSkXy9PXpm-nQi0oLpCt00Xp7TE1jf1KGK64I6w-1qZz_V3_vBrlCsiws462-1Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=rFVgEbhP3KCTKeiFizFzPRUXcRpkGDiiQS8QxN8X5b3Qd_GQS95byR5g73QcyNGRXhCiszGg-T19PdKxzPBL9AoIoTM1wP5XTrEtIa0AnzjJzOax96eZhajF3wezPkkpxutDoUrbwHclHTOEAtkMbBB_VcwFXi0U9cYSJtHJzadKWkwvHGbX-4mj95NbuXl5Si_OSpwB8gdOFtNDrvVdA4tHFvQdf4E7R3RzyCg_xBle9PIJoyM74RUQgxSF80I-08ctw1WYVGt_2OY_NesQnXb25p0imP16o09XCC_f-YOHsbFKxoDUxAgq-rtwB_iItKFeG4hp_T0HhkRuk1KJbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=rFVgEbhP3KCTKeiFizFzPRUXcRpkGDiiQS8QxN8X5b3Qd_GQS95byR5g73QcyNGRXhCiszGg-T19PdKxzPBL9AoIoTM1wP5XTrEtIa0AnzjJzOax96eZhajF3wezPkkpxutDoUrbwHclHTOEAtkMbBB_VcwFXi0U9cYSJtHJzadKWkwvHGbX-4mj95NbuXl5Si_OSpwB8gdOFtNDrvVdA4tHFvQdf4E7R3RzyCg_xBle9PIJoyM74RUQgxSF80I-08ctw1WYVGt_2OY_NesQnXb25p0imP16o09XCC_f-YOHsbFKxoDUxAgq-rtwB_iItKFeG4hp_T0HhkRuk1KJbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=abvEBiAM_Ga0X3-M4ohg492ebPuFg6iMob4C0dUfiP_ux41hLmFMpZrS9dY73OzKXxraIeM8UWxtyM2GeiDC-7UiEI3VsBVNT37F8h8iVF1DD1OvVq1i2Uy16rk3DQhjDzsYr_Ro2YFuqiGBpOuo238TozLzzeZpCbl9Xo8aqO4UyzmQ7ZD0VgsMw9pp5n_CVtvw2Z1J281jVksoR9qSO-USSyavjpnyJL9q2EurrCV_T5si2QlD4ImYtOwLf3HZjnMoRj7kb21DkE6V5YKdV3jaAgXXLaqMGhaafBE-071xA0f5sqhrR9Ry402rqn78CfeqAhAtZQxDwnkO1tx4Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=abvEBiAM_Ga0X3-M4ohg492ebPuFg6iMob4C0dUfiP_ux41hLmFMpZrS9dY73OzKXxraIeM8UWxtyM2GeiDC-7UiEI3VsBVNT37F8h8iVF1DD1OvVq1i2Uy16rk3DQhjDzsYr_Ro2YFuqiGBpOuo238TozLzzeZpCbl9Xo8aqO4UyzmQ7ZD0VgsMw9pp5n_CVtvw2Z1J281jVksoR9qSO-USSyavjpnyJL9q2EurrCV_T5si2QlD4ImYtOwLf3HZjnMoRj7kb21DkE6V5YKdV3jaAgXXLaqMGhaafBE-071xA0f5sqhrR9Ry402rqn78CfeqAhAtZQxDwnkO1tx4Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvpxM52Sz7tpmw19RrbCj9-c8ncYhXooEKZoOMxnWTtJp3c7RB188jvV2ax1dkWJTaOFiHMdGF1p_W2bKE3OOkF7M0pkliPcD5N4FYYICjpC9fLhq7ecU1t8ApZ7yOY9wXPMx1lH_iw7ktnr8cXrwBIWki9NXJTtjRVjF1gKATHNe98XlkYfUQQu9h9aHB--Fg3DAcdsjOMQBffOzdKGCBxZielU7MwhUBjmvvK_2J6ge5OvbcCHHmzhWaF_m67W1NlD0gRGs9toptgAn6vt6iei3HMzqAznq8GfOZgiE5CxU1-hBf_UApD8WTULkFmhd1CGXRq9anCFYLRbi2OF4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=XgALgKSmq7kmKVjDOogc-2OPPiOuiMw-tsR7tPJtoMyYy18xTLHHDtxzkNSe5i8YTf_7gMyiLagVij2YJcmbWrxCLgAEY_YA3jXn9uJUVj63OtpbGB7iwNnbNiUN6qPoBNaDFXtDtkwuFbmvRWFcIhC2_2e57Qp1_NC6OzvBFg8CAMJq4qGTxZr_X6Kstm84QcxYsGIm94H32gtzcTltoTxqJ4HJaHC-Fz4WIPww-UqUY6oKqHMm5zzTe20kDucABwkPBl2JRcusKLKsfFc6Nx2-uVlB-tvL7uKoIcs_vxxX-xFDiCh2e676UgGQo0bWHIo7QnzhWPZ7X3J0HoN60w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=XgALgKSmq7kmKVjDOogc-2OPPiOuiMw-tsR7tPJtoMyYy18xTLHHDtxzkNSe5i8YTf_7gMyiLagVij2YJcmbWrxCLgAEY_YA3jXn9uJUVj63OtpbGB7iwNnbNiUN6qPoBNaDFXtDtkwuFbmvRWFcIhC2_2e57Qp1_NC6OzvBFg8CAMJq4qGTxZr_X6Kstm84QcxYsGIm94H32gtzcTltoTxqJ4HJaHC-Fz4WIPww-UqUY6oKqHMm5zzTe20kDucABwkPBl2JRcusKLKsfFc6Nx2-uVlB-tvL7uKoIcs_vxxX-xFDiCh2e676UgGQo0bWHIo7QnzhWPZ7X3J0HoN60w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=tzPUW-8wBEG8Qx8tpi4HtyxH62S-Qv0-dUCe_1ihqEqaBr9DXXDZcA2Uza4VhNkP_1AJEO_RFjWY_HCOx1TcsiunUEBPKhta3lA7OeVab6QhCkOgBpvyLbOlFi7xijOmR_pw39btAR3x4bokq4suraRVieBMRFZX4jcjcY_hE05SGi3q4-SmKPE2q3TBzMkQoYv5ZMQcDGvwgDzPneSAPXGTE7GKjkS-d59nyCuDUoorHxGXHn22TBEKVrMjsUOsTpZpcPb1CsUxlcZo9Jn0Sw3zlHAZ_xwp4qw-P6b6Ys5gLbtxzHO0-ONCqWcFvyTBXU5A0otqBvOjrYs58bMMdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=tzPUW-8wBEG8Qx8tpi4HtyxH62S-Qv0-dUCe_1ihqEqaBr9DXXDZcA2Uza4VhNkP_1AJEO_RFjWY_HCOx1TcsiunUEBPKhta3lA7OeVab6QhCkOgBpvyLbOlFi7xijOmR_pw39btAR3x4bokq4suraRVieBMRFZX4jcjcY_hE05SGi3q4-SmKPE2q3TBzMkQoYv5ZMQcDGvwgDzPneSAPXGTE7GKjkS-d59nyCuDUoorHxGXHn22TBEKVrMjsUOsTpZpcPb1CsUxlcZo9Jn0Sw3zlHAZ_xwp4qw-P6b6Ys5gLbtxzHO0-ONCqWcFvyTBXU5A0otqBvOjrYs58bMMdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=KvofysD8nOQ8TDQ6Hu-FGjAJLetdo5lxZ_KpDl9mwBdR9klVXhh_jX4yDTJwLYM84UUWiO3yoXO_xHKZ7-Ohq9NXtLj1RXQzlLW6BJ0JSktEHHGWRZRKM9PoxrkYyMeQSyU4UUvAsN2LaJlzI28ADDLtaHzoHyEZZLBmgSW-GGMHmBMe6KV5NamGkFRfHf-aG5dj9KJPGyVezNO4NXUyAetdg7IQlz8d0E1mg2ZFxn6IkBoHYLq6mPEIbeJvwGOWKHo8XofNnM2TLWuOEyaP1yxQC6V82sDNAGBeDfmPLauAEIFWiTFZ990bnSRlgL0bun2At0YThfPaeFQ1k20BZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=KvofysD8nOQ8TDQ6Hu-FGjAJLetdo5lxZ_KpDl9mwBdR9klVXhh_jX4yDTJwLYM84UUWiO3yoXO_xHKZ7-Ohq9NXtLj1RXQzlLW6BJ0JSktEHHGWRZRKM9PoxrkYyMeQSyU4UUvAsN2LaJlzI28ADDLtaHzoHyEZZLBmgSW-GGMHmBMe6KV5NamGkFRfHf-aG5dj9KJPGyVezNO4NXUyAetdg7IQlz8d0E1mg2ZFxn6IkBoHYLq6mPEIbeJvwGOWKHo8XofNnM2TLWuOEyaP1yxQC6V82sDNAGBeDfmPLauAEIFWiTFZ990bnSRlgL0bun2At0YThfPaeFQ1k20BZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIscMYp4Jxl8jIeHCUWHFoINwJLRkHlFfD9-pEf7-RBCAtrYp_WgtLRCzvUPf7H0cSBpoDdAdDDuwgiB5NjQHxKnMEpQjSo0LdGovZcJvX7zMLP7GxuSCVs0W0gcDyiI66ropstcJHOP5aQWCM4GF-2a-kkH5Y_oxzyLJu-QFr1E6CkiPmJMXA4eOqqD4l6IrRvatcFexRjSzOaTh0C4D2M3leKb6TH5GXlj9HgnvGu-BPk5X6jjJx541clRWwO99YWnhilqgPOZ3iPLOWU6hoqcl-W_hyE2s8DNSkKxZBzQv9kMTeeYZ5Qw9_CvecTn5fo1NVuESG9ZYQmB8-J2Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=rSimeGqR3GuehjJpZKkuTg8UPDCfiZN47KS7U-tp36O77hbem0XdZJOuzYnJN-q-rC09FEgDYAw_4MPHKJKNTGUQKNJvYaLeUFDP_lzfSsJO1nIT8pEE2tPwGwccA6TDgQXMpGDtA06loAF0CFKvYOZUuG4j-lJr2rRvFJTwAuLgWp82NxjJlY2_CsWig_TkPMMKgBJUxkhNIPVNOOTXISmyn3w1UEknzv_kGvwXxGMGVC-XbiiNy27B-vX7HVnv6aYRXtVmQOBs1OyPedNFAg01V9Uga48q6116Qn-dVd9bon9Qlj8wINKLp2AoazbSAZHNO7cBKPrPOF3NtfHWdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=rSimeGqR3GuehjJpZKkuTg8UPDCfiZN47KS7U-tp36O77hbem0XdZJOuzYnJN-q-rC09FEgDYAw_4MPHKJKNTGUQKNJvYaLeUFDP_lzfSsJO1nIT8pEE2tPwGwccA6TDgQXMpGDtA06loAF0CFKvYOZUuG4j-lJr2rRvFJTwAuLgWp82NxjJlY2_CsWig_TkPMMKgBJUxkhNIPVNOOTXISmyn3w1UEknzv_kGvwXxGMGVC-XbiiNy27B-vX7HVnv6aYRXtVmQOBs1OyPedNFAg01V9Uga48q6116Qn-dVd9bon9Qlj8wINKLp2AoazbSAZHNO7cBKPrPOF3NtfHWdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOy6gHrHEnXgeMFk9lwr4XcSwqevkNiYaYsS_jdxaZYIE0hU8WB36170ZQmLzAF0MKg_eQT4v0-wBAx_Bv764KxIy9f06SkTZAay2k_joqofEO35HuCvL0PK-cBm7HvUHOyMwCO2u-2H7jhmDtOeHE_aZwc3gvpotVcNuYTx2NMad7EjVEggRdXzBHR3wE_X2gmvNkdcoQ83tQSE3hF1t9gBAFC5VbDRLelUBjp9f6l72GAl5conYBXc3RE47xtypHn0HJLdXTG9Cwzz8LlY9o6_qrqwTcBzabhiSRXmJ27LRKs1TjjpMy6PDOI9S-aQbiLwxQbWcM-nJHmC8Sf4qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfkKlVfMSy7WU8cL0MGr3fMX6M3CNGadX_6XFoTze2o0s1XM4HYvbpDmCutDz99VC6OzrEIuQXgwvV8lS5UcYRiEu7Qy8ps9UhtzCncfnTSwvKcmS9ngT8BVyiJvfYkqtGUE4IgZ3c1jBhKBC07GZvgxLC7TW6UjvHIc3F5oFTF9Rx_EuzP5n2vu_hyYQmrymee3l3OBY0ZTuexwOznJcdqCveDZKfoQkmaLZr0eveZU-Y_4EyUuyURDknv29WXc1aG32dsEKtU3GRG6J6SBw7O-35vM7sczIfAw91vPgQps1eQekVPkKkkBKhkV_l7LWNEvzz9lCiP1Krngsq0BVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=bg1alZBUIXCjEjbvDIRqb7DmPtHcAa1w5I5rn_6HQBpLtovZSlYRBkiLIivt5M4XwUWwNEMj2EIsZo4_j_eKEwjUs7k6cL5Vnp98g3mQMIBC3fy6FYWIG9Q6rzDaDduOx4c-ZxzFPIxDjokgl0d7mLhechE4y6LHVNZfOCLByiRBzEUa1I9JOk_nSmVYmYLhChiLiLhXm1xhnIwl_6-WbMx5SkBGGkk0ynZggMoYu_ZZcfREr7PrrTmEPkYWS-ccnnvZrU3FoKtzclRQjeckJuD3YPiuQUgFWLmN3FH7b8R624a8Pkrv51pdhGtkb0bmq-C-tqjY74emThLG0JLx1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=bg1alZBUIXCjEjbvDIRqb7DmPtHcAa1w5I5rn_6HQBpLtovZSlYRBkiLIivt5M4XwUWwNEMj2EIsZo4_j_eKEwjUs7k6cL5Vnp98g3mQMIBC3fy6FYWIG9Q6rzDaDduOx4c-ZxzFPIxDjokgl0d7mLhechE4y6LHVNZfOCLByiRBzEUa1I9JOk_nSmVYmYLhChiLiLhXm1xhnIwl_6-WbMx5SkBGGkk0ynZggMoYu_ZZcfREr7PrrTmEPkYWS-ccnnvZrU3FoKtzclRQjeckJuD3YPiuQUgFWLmN3FH7b8R624a8Pkrv51pdhGtkb0bmq-C-tqjY74emThLG0JLx1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Qnqq5VAahcDmEUe_i775bHN4zanVcdWo2yZeEUWrurrJTJfdgqylPDvN0pzKnz9WC2ftyadVvke2pEiUISFI-CYWHg0vFDDKUumL4ODIEpIIsEb6alupeLzxRB86UbkAWMQjw_h9_3ugqZFUVUqfZNAjei3YMcDbKUm1PUmbEUez6gxtwe5q1-X8dgJuL0xSfEkLwKuo5EJIj86iPLK59Cuc8C7jM5voufs0D5YJ_BMZBk_5e3Mt1bPUVMSIASt_dDxF6vG_dWci7QAyXlhoZRgHKEMnYm04G1w2Y7_ZYxwkxD-Gc8HygH4vaTKn-Rg0YyTV-3Ol_XxqvROz1utcL0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Qnqq5VAahcDmEUe_i775bHN4zanVcdWo2yZeEUWrurrJTJfdgqylPDvN0pzKnz9WC2ftyadVvke2pEiUISFI-CYWHg0vFDDKUumL4ODIEpIIsEb6alupeLzxRB86UbkAWMQjw_h9_3ugqZFUVUqfZNAjei3YMcDbKUm1PUmbEUez6gxtwe5q1-X8dgJuL0xSfEkLwKuo5EJIj86iPLK59Cuc8C7jM5voufs0D5YJ_BMZBk_5e3Mt1bPUVMSIASt_dDxF6vG_dWci7QAyXlhoZRgHKEMnYm04G1w2Y7_ZYxwkxD-Gc8HygH4vaTKn-Rg0YyTV-3Ol_XxqvROz1utcL0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=J6aGCsHHdeNlMZT5RWZQWtREpKTDYAGn3Jmr41OAWGuhutjmlYY5WNasTfb9k0FpJspzG9H9jozO9peRFfnvDBoZ475mlLgnkEtKhMC_0sAw7zKV22liuiRmKpj3mWsAVO-dY7eY0RYMn9CAR1dWtszqL_mWxJ0_MsiCjt8AYVj5OsBMPTLuusQuATp1TLlate-FLg0SIhG1rtTd1aP8PYhb78BzPBD0WoHugks3Ra6AULoHIUflwxST8JRs7n1CDUDjYQ9ZbrI3X1igjGK4Al7lEV3m1TJxuL0aIbtVGBaVdW3yLy4NPbBRIrwIlofjKHxJJULjJwSi6b7BWBH6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=J6aGCsHHdeNlMZT5RWZQWtREpKTDYAGn3Jmr41OAWGuhutjmlYY5WNasTfb9k0FpJspzG9H9jozO9peRFfnvDBoZ475mlLgnkEtKhMC_0sAw7zKV22liuiRmKpj3mWsAVO-dY7eY0RYMn9CAR1dWtszqL_mWxJ0_MsiCjt8AYVj5OsBMPTLuusQuATp1TLlate-FLg0SIhG1rtTd1aP8PYhb78BzPBD0WoHugks3Ra6AULoHIUflwxST8JRs7n1CDUDjYQ9ZbrI3X1igjGK4Al7lEV3m1TJxuL0aIbtVGBaVdW3yLy4NPbBRIrwIlofjKHxJJULjJwSi6b7BWBH6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wAmy7kktv-SVdANNNA2yOC3eawqgHQGjxETbDwkyXS_z_M9AV5lJq25KMDlXlKcE8q-3xjGGJ050NhjJyfmR0Y7gRLYhCcxnpJanOMNpc1-O1ovjzo_rp6yRi6Ys4H4DUSYYdsAbxYC9jhlwWvn2xUGXPeBU5EQCHOlCzcJNu8b1QGoO-YKuZ-FSa3Tfn-b4ajPLgBPfv3XZnHgKwKAeoL9NBDTwTCEn7WQN15udOFHRHG3FblK-JG3OQJ3NdH_N7zKRwIXsiHTMwVqZeCGf9QnK3DZcgDsyG22RyhAOYh-14NeftrCZoheRcPx2q16LjfvnF4MMsYW5oFa3iYE4CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=ufbqmPoN2Ze9J1cPiB_iLPtPV9F-3kE0P0vHRE7yBvE-AIr2N3_HGt3fV3xcNCFKsZZiX_sYcfnEqvWPQ0WO-x-49rXmbD47y544MKiDiQ5aAag7bOd4WV3GClJQC4gJu1KjQ9y2PCFM_1sJToPLdgVtBROt6XMFaAeH4aOUhIwnNr3YbqCOAr6d8R0NFuBFfhnJyo8dMvLAMiCr8FJ6CnVxH7-Ce2RX9MEtUGGcbAR4w5JgegzAPR0hyl86D11PXcvI9BUxrvSEEmCFWNXa7Xeye6oUNhUr-Aqdl3-U0zQ_pS0s3oEfd2KhV2tcp8sHc_8a_8srvpn87KIPLfRzNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=ufbqmPoN2Ze9J1cPiB_iLPtPV9F-3kE0P0vHRE7yBvE-AIr2N3_HGt3fV3xcNCFKsZZiX_sYcfnEqvWPQ0WO-x-49rXmbD47y544MKiDiQ5aAag7bOd4WV3GClJQC4gJu1KjQ9y2PCFM_1sJToPLdgVtBROt6XMFaAeH4aOUhIwnNr3YbqCOAr6d8R0NFuBFfhnJyo8dMvLAMiCr8FJ6CnVxH7-Ce2RX9MEtUGGcbAR4w5JgegzAPR0hyl86D11PXcvI9BUxrvSEEmCFWNXa7Xeye6oUNhUr-Aqdl3-U0zQ_pS0s3oEfd2KhV2tcp8sHc_8a_8srvpn87KIPLfRzNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qnFE8kxx1JaciUeaaoH5AZAVIArB0AOWT70gKGINIMz-8MnrWF9AMJNMlNMsjJqotkcXgTL5mLQha3QqAc2YLr1l9lCY_xQpwJGdtcxNq3EeM6euqJA5OhNhbQin9Flhb_jq_YvgLe9fGN3rLYhB0VJPzG6NgTo2buC0tLiy3gJBYutv5hyCxMveJ5K1W39YlEjRL8ISMiTW8ZEyFJ94bxdGBbGQMC-HUaKRscnly2xq1VqVGifMpNadV4dm5qpsTDlvcGK1_8QGiLDrjAVGpvhH8VdRYkIwkNsy1CrYh3ldofOCTzYH_LfpVO6JtuNdkHlgm-OGGEUU2N36n11S7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qnFE8kxx1JaciUeaaoH5AZAVIArB0AOWT70gKGINIMz-8MnrWF9AMJNMlNMsjJqotkcXgTL5mLQha3QqAc2YLr1l9lCY_xQpwJGdtcxNq3EeM6euqJA5OhNhbQin9Flhb_jq_YvgLe9fGN3rLYhB0VJPzG6NgTo2buC0tLiy3gJBYutv5hyCxMveJ5K1W39YlEjRL8ISMiTW8ZEyFJ94bxdGBbGQMC-HUaKRscnly2xq1VqVGifMpNadV4dm5qpsTDlvcGK1_8QGiLDrjAVGpvhH8VdRYkIwkNsy1CrYh3ldofOCTzYH_LfpVO6JtuNdkHlgm-OGGEUU2N36n11S7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=cA8BYY0QGpgPAvOq1BIWMWSHNWD078EjKVdM7Q_c1CYH2PG4teVFU0LYrT8j0e8KMGQ-clSpnWPj0DSX2PvCMLBw-a7jC03xj-2e8GNO5mqWzbbPiR7VkcKkgeqhU6hShQjP_acIv40PBxQq-CVninUDzp1ULbMYwQet_z5C-UpV5OexY0jlgW7SuOBFMnvH6QQ4jA2aIHycYyD0I1J7N5pNtph1Y9fRSP-ANJhtxwFdUBZbNPJDKyCL-nth-H2TyDv9jcd-IyqJ8NDuYq7HTcDBQ8r-45uESwkFNsWawwM2eJkO_RP9zKw4NrGmmmd8qIDJq1lkl2yXdjcaGqd5rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=cA8BYY0QGpgPAvOq1BIWMWSHNWD078EjKVdM7Q_c1CYH2PG4teVFU0LYrT8j0e8KMGQ-clSpnWPj0DSX2PvCMLBw-a7jC03xj-2e8GNO5mqWzbbPiR7VkcKkgeqhU6hShQjP_acIv40PBxQq-CVninUDzp1ULbMYwQet_z5C-UpV5OexY0jlgW7SuOBFMnvH6QQ4jA2aIHycYyD0I1J7N5pNtph1Y9fRSP-ANJhtxwFdUBZbNPJDKyCL-nth-H2TyDv9jcd-IyqJ8NDuYq7HTcDBQ8r-45uESwkFNsWawwM2eJkO_RP9zKw4NrGmmmd8qIDJq1lkl2yXdjcaGqd5rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=Zlfc80frKpgEvelTBmSdxzmbhB4DN_ge6EMK5Ir0bb3Bzr1BbGHzLjRkHA9bOsZJndyE2AQpl0cUVxImE16XEng6aCJ5kqM2aMMGjZRIoqJX7298nSjRt8l5-tCGgF7V_4n1Zsqz6HPCorMRmNOG3Z129HzuKSe2S9OwYHCmJIkMpJ1_nR5DutSqTANROQ2AWfaS_adm_oMXHzKjwgSbxgsuhzi5mt_q-DteOwN54YH6JO3oMZa8rnPGMRK2G-BgQSRY38NXVgzXFpsu7dCPvzBbgYFMnLkHZ5zl2vhmUYSgOTTZ2Iuazo_q83_xrFegNYLYRn04k14soOkFrNIp4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=Zlfc80frKpgEvelTBmSdxzmbhB4DN_ge6EMK5Ir0bb3Bzr1BbGHzLjRkHA9bOsZJndyE2AQpl0cUVxImE16XEng6aCJ5kqM2aMMGjZRIoqJX7298nSjRt8l5-tCGgF7V_4n1Zsqz6HPCorMRmNOG3Z129HzuKSe2S9OwYHCmJIkMpJ1_nR5DutSqTANROQ2AWfaS_adm_oMXHzKjwgSbxgsuhzi5mt_q-DteOwN54YH6JO3oMZa8rnPGMRK2G-BgQSRY38NXVgzXFpsu7dCPvzBbgYFMnLkHZ5zl2vhmUYSgOTTZ2Iuazo_q83_xrFegNYLYRn04k14soOkFrNIp4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8ZeV9FJ3WTuPoabZe7zPJqghy9C6DGcV07dh8lQqVUj_rJbN6PMZ5HOl8ZF21qrPl_AGrh6eSuPmgwtXykCRZRT4Yzn_pONb6ana_MuIpj4a5gPvIhtFIpHOc8X8r9ilXTnOKwoIpLM4ELMvN-hS1tohK0vgYV8D3yoWa3nz_YCqLPMGMJwvS7D7qy6H8Y_X0LxPmWXN5FX0bSV6sRzob5KSuA4ll1DvzW_HSoOYgyt9VSnR-eL4f_X5rZQpWiM084dh0L2vkG3VRQ--adQ6swr066AQFco6RhtgIv4UwT4X6CbPf6Z53o3agH_ILX4OYVZDewtBeDmtzlrxtknsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=eKbPuMsAOXUfgiJhITOHpSm6ZGb7YtikNfdncO6XLyKcuT_bQMbi2SX-GxN5bXySBmGYjHLDnxMb6fMlJQkno90xha7b4McUcD7f91mzH-HoAHdZ-rVLmkuyEzoLl5Q0-TKajLTMKwAZDlkOYXOMB4zSkZwspDRCMsFiZdsNExcbKyKMntyxD_reWmLPsmZJLjWXHHVDX2yq5qKr1hc3mpnBpzbHFFp2QX7rkFAZzLgC1V3SNN9La8oIoRE_s50IvCCgy_Nx-Ql16s_HkhDgdXLWGfuCry5yEqI5aQjNVZ73qOVEqyRCdySr7iqkkFaNaQlR-zVXnwVS3Uea7EmSJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=eKbPuMsAOXUfgiJhITOHpSm6ZGb7YtikNfdncO6XLyKcuT_bQMbi2SX-GxN5bXySBmGYjHLDnxMb6fMlJQkno90xha7b4McUcD7f91mzH-HoAHdZ-rVLmkuyEzoLl5Q0-TKajLTMKwAZDlkOYXOMB4zSkZwspDRCMsFiZdsNExcbKyKMntyxD_reWmLPsmZJLjWXHHVDX2yq5qKr1hc3mpnBpzbHFFp2QX7rkFAZzLgC1V3SNN9La8oIoRE_s50IvCCgy_Nx-Ql16s_HkhDgdXLWGfuCry5yEqI5aQjNVZ73qOVEqyRCdySr7iqkkFaNaQlR-zVXnwVS3Uea7EmSJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=rY6rskHm3gOCGkkYncdCv__re8qYzOFLxcav9MCfNBn7O-scBc75icBTGOcx93weUxIuAZoC3tko_0A6CcDvKPxOzfLryZgCN6xr58b2E_EtkEXr-Zz3JWnO1EYRGHuM6E7cxOC1gSjo6VupRK3WHRdJ2ZpBQTI7AX-mRS5MEHpv6WagpXxnclnfLIRFZ5SAmzMZ2JTvuHUs77W6t8RRpSZpyn5Ln3CD0uJuqObN_bvZ7-Hn8nMdwWOCrtNZzvA3L4gQIiIGWYKVZQnrSU8u6njq-8oqRsousTKjvwpnNms02PH8ZPTx91DY5LzuotxJKTcMs_5oyfXRBt166gYrxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=rY6rskHm3gOCGkkYncdCv__re8qYzOFLxcav9MCfNBn7O-scBc75icBTGOcx93weUxIuAZoC3tko_0A6CcDvKPxOzfLryZgCN6xr58b2E_EtkEXr-Zz3JWnO1EYRGHuM6E7cxOC1gSjo6VupRK3WHRdJ2ZpBQTI7AX-mRS5MEHpv6WagpXxnclnfLIRFZ5SAmzMZ2JTvuHUs77W6t8RRpSZpyn5Ln3CD0uJuqObN_bvZ7-Hn8nMdwWOCrtNZzvA3L4gQIiIGWYKVZQnrSU8u6njq-8oqRsousTKjvwpnNms02PH8ZPTx91DY5LzuotxJKTcMs_5oyfXRBt166gYrxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFSX8aV_invQcdMG5LwsbP2w6-j1Yy1nXFKlC2LOHLQ09394hILs0GAUvaUEDVrTfY0IvZXJCDu9oGeMiINOxoxRLUdO6REv1cRGdrbET5V5TfXepNSKUh-kI9jrtYxHFY4RL8s1Ml-8XvGu-uwIU2iIe4fQdnf6xkBQks6530UQitKv0EuxTYukEuQapdAohMdv-CzYbNHx_D2LZJvKR5crGrDffqoQTbkND5w-OfftUieXY98WCcP_07g-rUkGt7FjC3c-ub4QTOZbGU75ruY6o7rUiwQVbsppM1_6aCGrvcKcOm9HnjJg7bDLI7TgBYyxSmFrmoxAKTuY8WmH_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=YjIjYHx-EsKIT_dWbhGQOMVSV4-MD49piX0f2VMNqufH9YFRLOjSYeFNGu5fMZxSwoQ2uEuJQvRSBJs7r2gtkdl7S4HJljFDcnEHb39lriyztMHzEv-7gsPff0e2IjRa5gHJ1dOHCjxqHhUaZTzkbmWDBEA5ueYMo9lpiWSh-_luVIIfpVB3RbrQutX-Ol-Sf_rF4jzCjCDa2SAMsMkY2uQm0HY5toLryj_g8mR5iEX7uwxPMoJPxTuzw9yL8dNmK6r3seDEwah8EqnCwz-J9jHXHtqTRqh1xzpKHrsU2IOrqKqb6RMitHhHg0M70Vp2ycwoVh7KvmKECDj23307vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=YjIjYHx-EsKIT_dWbhGQOMVSV4-MD49piX0f2VMNqufH9YFRLOjSYeFNGu5fMZxSwoQ2uEuJQvRSBJs7r2gtkdl7S4HJljFDcnEHb39lriyztMHzEv-7gsPff0e2IjRa5gHJ1dOHCjxqHhUaZTzkbmWDBEA5ueYMo9lpiWSh-_luVIIfpVB3RbrQutX-Ol-Sf_rF4jzCjCDa2SAMsMkY2uQm0HY5toLryj_g8mR5iEX7uwxPMoJPxTuzw9yL8dNmK6r3seDEwah8EqnCwz-J9jHXHtqTRqh1xzpKHrsU2IOrqKqb6RMitHhHg0M70Vp2ycwoVh7KvmKECDj23307vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=WKczjTUJb5AMnyi31wy5bQKWaLfXwM_Nr6O9uGhyUpjgi5AxcqmPbRoIhrXQtmqJgoqBXKog_uhfY09T_vKm1HdEVB9cXkVuAlmuqim2KcYjrFwnz99Va9OrDYYoVkiFfSBS_GvqE__IutR9cir6dEPp7AXbNjVCO9yP6ifuWhKzt4Rsz1LEB5BDJMqNGoCugAmzlSf47MzZgly2ilnzXB9OcG1cBJazDzQykN4oSMOQIugfA-e-TbWHYmYk40YRU5WMCQ2WLaF9IFdHPEPAbUXBCPfTjcqusFPE6y1d7gZF76oS5IAtYcJyPC8NstVzNIknmEa6Z9Lx47SEIplMjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=WKczjTUJb5AMnyi31wy5bQKWaLfXwM_Nr6O9uGhyUpjgi5AxcqmPbRoIhrXQtmqJgoqBXKog_uhfY09T_vKm1HdEVB9cXkVuAlmuqim2KcYjrFwnz99Va9OrDYYoVkiFfSBS_GvqE__IutR9cir6dEPp7AXbNjVCO9yP6ifuWhKzt4Rsz1LEB5BDJMqNGoCugAmzlSf47MzZgly2ilnzXB9OcG1cBJazDzQykN4oSMOQIugfA-e-TbWHYmYk40YRU5WMCQ2WLaF9IFdHPEPAbUXBCPfTjcqusFPE6y1d7gZF76oS5IAtYcJyPC8NstVzNIknmEa6Z9Lx47SEIplMjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=M2-0CoSw4W0nGetqklFBiXKokF2OipfdnwmEHCFrQwoUq7dheZ-1TvC_fBSbeG9qGuSFlcQnHl_vIBpay8ZBP2exsLYiE5-1LeaueRdNstGcA0KC4JU6-TnSE0AayjXD8DGV_lN7QnzrHZzP-rXHcOt3QSm7EBlnaV_FjsOISj5yC1JI0ibg2X_q_0NyvOkONVIOqh3cX8RyvSYsvUd2QUcgXo8h1HT6aSuK5oPbgeaZ4TYHnfmCBFuHGue1RHRFWRvpFvXaWbaErEIVMN03f6nyPQLK86iqEjUyOy6pfSrCg6yUEc7zSOxZjb4SDimdEu6xl_HFUJXVHL7JuYXkJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=M2-0CoSw4W0nGetqklFBiXKokF2OipfdnwmEHCFrQwoUq7dheZ-1TvC_fBSbeG9qGuSFlcQnHl_vIBpay8ZBP2exsLYiE5-1LeaueRdNstGcA0KC4JU6-TnSE0AayjXD8DGV_lN7QnzrHZzP-rXHcOt3QSm7EBlnaV_FjsOISj5yC1JI0ibg2X_q_0NyvOkONVIOqh3cX8RyvSYsvUd2QUcgXo8h1HT6aSuK5oPbgeaZ4TYHnfmCBFuHGue1RHRFWRvpFvXaWbaErEIVMN03f6nyPQLK86iqEjUyOy6pfSrCg6yUEc7zSOxZjb4SDimdEu6xl_HFUJXVHL7JuYXkJYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qB3oj3X93xh6ly3_o_GzlHvTxPjhvBRZ_oUjLeKJzCuHKVsDDINp5ClyayEipLGNMwJ8eH6X1SaTCdT1Vmtu4oBWZGVzwfcCAGF-JrZGeUY-eJ3H6ZKghMUl_QjlH1tLFNbIgrHf2Nirnd3Jz9HCd_BfCEG5r2poRkDg_FQs3e6Ahl6qp2vRZUENBs0PyGeqE1kY1dvDeGduFo84Gtgfv_q0xN7p_9KCZhhnlge0bk1NNdooMeAacvfUI3Nnj9Y42DGrRcFhj8aZApc-aEe0cZSPC2x5z7Ds7Y4ljABjWw8AIqq5syI_9IlmBFSD2gm-NhXvirepZ5Qr3M0Dx5WeOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tmoww8dgN_AhFDWz0DNPswEtg-V_AYgwxJrjdyzJv8myOZh5-vZ2hK4_OpYrnAorUQzQ0ygqxp9dUmQlneDyop2ODj_BRP7xsea-noKw89iuQCNnJLdM-s_ssAzdHZSkFsn6TXwBLxJtjfIGI-b7dnGA3kZceF4GEzEBhCCe0EP8X2Y2CuRV1tk3PzrIFp5sOHJSwL1Cvg1UKv5G-P0jUckJgkQKMGVxXT-N34UZ9IrpdLGWMYDVqbMvj_7ByivL1Rprnp842osy55OMQwvRG_ZVY2KMMrVw6MK7see3xWPFg_j_ReThE7ljjukGZbDDM523Yr9txp6QteA2v_U0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZP-s3-Rdsm7Q6aBuhEps4-KE17idDhHvK1VPhpv-lRlReLB1PgCcPoG3Z2L3UDebrW2KoWvtME6_n176hbt5DDNCH3BrpgHvNlsY0OnqzkO-ZNIRFBrY7eBpr_vpF5Ikfpu_ZUp63G9gcxbvgytXDO7H7UshsoFZSeV5RgdiuVs1-XPiIWRahb3gtik_UGzlFRemL2GmYyVvRGouvb0vLnxeXi0sf5fGa23oNrqfJNSQ94SGtcfEENLJCmK5C7DH1CdzV692is7HzLRZz8y2sznvP5zmT5UCJyhMqZa-CEACBN-3g9T9BpIaMwEfqpGrk47aDgVwqwn7iASac6w82g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=unPZp1L_on0tzI9etzm5xV7806jr-CKWapsG0WDZY_za5P9D5yAhnn8IrnVLDgCZbhB0qOrH_17tfBv38xHBCcvUiquJ1yZQ7Z2-G_4OFUG24ECwJJQrCEYa-yZ3HOqOWvT9LTh2_eGTcPkQeBj8nBQUgj1JLHii3cLm7twrahauc3iAEWKiALxLuwb790b_7Q_puVEVj8WxOnMKgErEpsEvzK9fgwqlHp4R2dh3vb1OlIvhJ9dEu-VzgYyuCoNP4foflvbZ7qJtq0BJ7DwYL9UFHX-Mdc9XYyXRKrVGxVavo4TWfNkPF2mtS6am_ufIsKpe5WWYbofT2PZUbfKsQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=unPZp1L_on0tzI9etzm5xV7806jr-CKWapsG0WDZY_za5P9D5yAhnn8IrnVLDgCZbhB0qOrH_17tfBv38xHBCcvUiquJ1yZQ7Z2-G_4OFUG24ECwJJQrCEYa-yZ3HOqOWvT9LTh2_eGTcPkQeBj8nBQUgj1JLHii3cLm7twrahauc3iAEWKiALxLuwb790b_7Q_puVEVj8WxOnMKgErEpsEvzK9fgwqlHp4R2dh3vb1OlIvhJ9dEu-VzgYyuCoNP4foflvbZ7qJtq0BJ7DwYL9UFHX-Mdc9XYyXRKrVGxVavo4TWfNkPF2mtS6am_ufIsKpe5WWYbofT2PZUbfKsQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaW54vprKEL_IyOHsp4EJHlmIZXVa0hngytnDYe6jkFYPTE87dsxrbHpcxIfqIMxTnpddgSByTy881q6-t5uBMbGywpA2t7hvqhcAd_trkmhzOUjFJF1GALkAZyj1gXpuHRIBb8GOMpOvv6JALo2UgMTYoCZ_Dq051vUblLciKUeGuQRjLlTdLplimZTqjbP7r3BEsCGmzBioVdu0_25WRaO_8_T-IiFrZOqmgpMQ4ViCYnRITPKIOLlvbdrXJrwJ4ZtHBwSXQl1qjR90WcICA-Zo3upGgHbPfCOAMjyNiANhMIcg2NpExCRoNIL5ege46w9ghh4BLn92eJkC1Er_wX4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaW54vprKEL_IyOHsp4EJHlmIZXVa0hngytnDYe6jkFYPTE87dsxrbHpcxIfqIMxTnpddgSByTy881q6-t5uBMbGywpA2t7hvqhcAd_trkmhzOUjFJF1GALkAZyj1gXpuHRIBb8GOMpOvv6JALo2UgMTYoCZ_Dq051vUblLciKUeGuQRjLlTdLplimZTqjbP7r3BEsCGmzBioVdu0_25WRaO_8_T-IiFrZOqmgpMQ4ViCYnRITPKIOLlvbdrXJrwJ4ZtHBwSXQl1qjR90WcICA-Zo3upGgHbPfCOAMjyNiANhMIcg2NpExCRoNIL5ege46w9ghh4BLn92eJkC1Er_wX4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=EVPLpOkUF8j5ZkEIDB-ASWWV0Tkzm9Ta2L5V6ngIV1QaKy7snASZunpIMpD7Ltz_zPxI9ptCs1D56i15R7t0hJNlgVcNm8N5sjpoSwpfI5tN1zrkQX0tOPOmLsH70XXWWl-UOCGOr1j-4jUBaQuOT8uwqZNmNrIhRL2HJRwoItu9MNq5lSj5Mcw-MseEVhIknu4OSh_a2_j3AqBBEIf97vSZPhJZvWjEAMrGm7pUZwlHPI5ppaHfgLmfQUlMi3u8S-jLY0aZaNHi8ax3ZU6hoQAMkAxFbxmptfvjIqxSOqADgoFX_viaYpYnavGl2VofVbD7WLKdsxu5P5lQhlcmSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=EVPLpOkUF8j5ZkEIDB-ASWWV0Tkzm9Ta2L5V6ngIV1QaKy7snASZunpIMpD7Ltz_zPxI9ptCs1D56i15R7t0hJNlgVcNm8N5sjpoSwpfI5tN1zrkQX0tOPOmLsH70XXWWl-UOCGOr1j-4jUBaQuOT8uwqZNmNrIhRL2HJRwoItu9MNq5lSj5Mcw-MseEVhIknu4OSh_a2_j3AqBBEIf97vSZPhJZvWjEAMrGm7pUZwlHPI5ppaHfgLmfQUlMi3u8S-jLY0aZaNHi8ax3ZU6hoQAMkAxFbxmptfvjIqxSOqADgoFX_viaYpYnavGl2VofVbD7WLKdsxu5P5lQhlcmSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
