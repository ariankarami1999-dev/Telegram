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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 02:24:00</div>
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
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8TmlUukgx1CEMxrplBrST7mcORmueW5TPxmvJyYIx1gXuGnjch6i_jSD6dxQA9wNntu2S2uOLXXgZnMEc_5MsPr2YVuuR5OPlbKMSGK7xmig-nu01nyG8d6GkeyzUxn4tckbpN7A-DKWeZjdRctdIIw0vkX9V69l6raE4_Oinyql337INXK4g2riy7f-GFsi6GF3lhGhIcrg4xvRS6XWe1WuRul9AhWMl13Wrin5WVHXwbzwSxrMa9nxYPEhZaenXITHHcr7OmRGUHDdKQ7THRh37vPrCn9oMKyyrGIcOhk-lU7twZS7Bx-MskFFy87mKoeN8ggtc9CNGde889kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9YU-I68y0MFII1vhQZPbSroC3VFK9W1KJahDUlbnv9EnYRHVGFyWP4jb6bA8FqvxI8wF5TFZHeH3GbgGE6deXeX-BY_5Z0pQRfEPaQMrfGhRgbCw75pzus8rjOFG37mQuAmzO2tU2a6h6SMyvCgseJraQM9Cb9ZsDxlNbWb7NFNyjcmzVcZUmP_8UVJncxytuU0v82t8k0dIzHwUxHasPYsYhRCwL3yTpCcsYhRjBeB824schhTgstQy6mYmRUDvaPCDaAtgnX_YrO-jfJRCv0p8CzwGlLtfHbjyUxIN9o1I19t9LqiCwgwQlGCU-Qtc_5hco76s4crb18SqQzPPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1A1DOQXvaLgznkFziFe6otJs5BpkhPCjgw73C0OUC6mUeXmBG122s2-siZJocgOEaIPieGZoQcmy5NtP-ai2WlePjrFD2MjLPuMNmkBBOQfxrK8HXJVtbnhA1JhiSg60RwCHB2NEgn2iNpUJygpAga_Bkk15Dypz6G4EVaNPyoFvQINnu-Zfl9-6V8RDA1VFKZpY2NEBsJyyilRet6BirEcw1ZdhCPeyjCvlAQngAXmmslFlcLGEg7H-3Huse009tv-CwrY_2iMhp_KcEn0bXO4Vw6uxENf_-I9jQQOxGetXd4aoMJpIu7BhuM236yCuPU3Ph9DBt9cmoIbnZFyjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyEkhQQMCxcn0UU1Y3NoPa4HgX6Pv6MlDRR_Rx_d88_JgdjWazhN9ZTUpc1LQa3jahUl-4p-f7zEQlzz31KmhP2WhiLmix5KMzJsmHukwE7_ES_lyQgmVklc0i82LwNXfFAYCILz4Jqz-GhVffRJzIiYkkPQnomLZlfYToaTOb2hy9zy1mwmcEtYqNnubggTIjuLxhcAR115Fbz3CaSsDpmUjadlf8dNN0yffKH_OnnusFR-uk-ZEK3ObH2FHe74PH_GBL0xFioE8mjr68M3x3z1RdthEnCqu2_ojFuFNKHZQMR693ceLiH3HnM7WE_IZ-Ca7sy0mtZsvNhMXQbJsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o5PyMh3ndioz1Yh5zHqYb5ETBreddqV0x4UoIyUcxIVVb7OG-Fp6V4-5e6XJcIFxZAm_yTifWuEyASw2y9v4VLYIyG9oCGkT_7AmBigcvKPOIoj7WsEqIzj-ZPo6jizmulAOr804vB1YTkz7mC6BOf4MjgVMQTPWURzT74g46CmFIZIa6BZ4cm_tjiC0YRdtrDW4BISv5BIFqDtkVHGjfT_u1zp83Vz_kN9J143kHDyVU_xZvcDMPHXPKlmb_Z972dr0HXnyod9pUgc3xg6nkVI16UirsK0QIenRcb1CjkmhDkra_oU2vRFK9TtWmicLdampz80_X4xZAgfNbp0aPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rwxUxOZmv-RTvbU6kD_HVFoat2Eqoo74-OuGF1oDOGSONUuMnwbfLSNNlzJGq9TbKGTbatfkNx_SaxzI41EKcf4Sv6G7NylEdGPHze5Xkt-_HQd2mU8NyKE05QpvkmZOi1JaRnI6Bl-KUwor6JDrQcEqmyn2diWvr0LjO9Aeb1DAq0HWAL59ZlQfQYziKbWCc3pZYB-BHI2PEz76mMH9MozjpSFdNGJi8DPowVdS6v7RszBJxX3Jbc58cUQfUB3Nyln1_CJVjrEnubtm-AEYoNwLuANcig8MmRJCc7u_AZwicgHk2isIblTc8Mypx-66L7SHWFrSqaxYooenes8sqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-i5X9s17Get5vcmmkv_oZGcnVNSw3fTwkcHPzY0jIZ6-IW4Fp21dCx_EtGO7eUwVmV4rARC68tC8gnlSijynJ9jqEwBXtucmpENXRkTSVmkb1yz_EeNm4xHMinGcqb3wZ2I-yDevFbjnwkwpWV1C4CVq9D9qrOHwOj7ArFcvp-SlDzjl_AbgkqM1pybB4iY3iRzjvQcrc2P1PIBUNrwqo5CCRQ7kVWeCNHDE1nyivEqwpXEVZKYnsO8-U3Z3d3FYTL7gdY3D1hAWhnPgt3NuZfjcmDBwW4Y6KTLLKnXTrqQG5XtwtBSBe_MwsgXgPtmnUT9tUdCw1QoOG3R3zjZfg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gM-TG2PWIBxYIufed4wIaQDb_cj58Y2Mb7gGP2MGWMaoA4d11t8AMjLmBJ5vliO98AIzR-BMl11-vFUH6ZkrHImm71S7fM_skdKLGXA8XznkZWwC6AQbBtYl8QKE-9g8seJomf3tkhAsVUCqWZcN91YY-9byefWek8zA90WQ1jE8rcxVJ6xa79bofmYdafB5cqlzEvbGitIwIsZxJ2WqM53Dcx2gGvQBrWSL4RhiQgDLEKFQC64TXhkVi5HVDxUvBulavHDcUBj77jbYSTXmy7OnyT5ahUNz-19IdPTfQ4OqtXSsyfzGr8FnJzB3Ktyoy1YIxMrx_YWrqWrAkqhNAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSH5_B56zYquTfDuC8tHaEovVjAx4BL2U1HiPt2puiVMpYSxFZ-syDe5uLT0QDzunfShmx9vkdcg9_5UPYflSJ79U1PWw872ST2nEqOK1cqWnZYwjzry2zR6kj1daIqigbXNOzbWFyna8O0s5DhDKmfuCFGrhdJqj2r-kjAQIOmB2uaxK4FW_OBsYL2R1--0D2bFxUIqvllL4wSQM01XAfBbL5UWHs0Qi8pA41ZdhXNyddTgp0-bz8rmCIIkA99nODEkSPV2quvW2lmEXOa1gmh9gIcLpZ4dQYDLzNM2GVg4iIK4JfQfzJTOTIpN0cOisgBFTq8RDdzzGhgIwlufhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONkD9JFf16jFnEBFcP99H4-ozGxjbb8xuBBV7ukRZJJIMXa5vJ3kUxFIUVvNYm7eurSBKoG4HliuV2kWb_38DQofPUcARLoLSNGnTbvmnUlL9htjBdAZ52xko0CGkx9jJfK8UXZ22VAsvbAlZLbOlp_z09GaOowpIJIJEDh-KiuyFKGJ99HtyWP7JdnDLFVNKbyeeSUufwfsbib375CNNpQz2TaUkYnKPubbHTCAN-XxzH4C26NmsQKHyqEUZDCIhbldocSbCF6qbZcYz-8guRH3ushYQr_a8q2rQMnrW0WNkzDCmeKsKhhXYtDalzeIR32P3UQXckVcsysjLGobow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tsiBQlhGlAKaDzHBRoxKYa4BbYOy9g1jBBjx8QzauqW2ukqZ3wdFWvM5LE99TTZ0NfEa8WpZBK6_8-0GwYB1KH-9_Qzclpu_MMQHQWEnWZ3D08tYJwXYoHWlEOSjj1UdLAuKBjZshTESJJYom9aa2PHcwsQtwo7e3Hskkcuy5RNOWyHl7Aczk-tKCcJpjQ-5LY8DQcExG0Zrbo_KR6o0W1jU81LK4tYkZCKLjnsxUwweglRJTJ7466lkM43-Qlb24-Fgx8dEjoWxzP9vMMU8tqRwTxQBFEwsLHVeA0-EzdTHN3VB6Kqc0h3KCW4qIZpRP_0YfU5g549SQv1OZLelEw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=U_uq66m788W7HkvLa6nVnrknn3zjIj33g2_U-F6br20Hj0iaWkNoNfW9ORRG1KVgdIm1CkKqa9_e-HBByR_aF5juizyEmc3bI814O41NRYnud3am_acph0MoyFzA-U41ei0EMCL-25gMQ_b_lPzsWGbmj9lBfEXHgXLl-AxMdzLfyRNKuXjexz_PhkCyazJTAEBJSC-OjHnetchVyAQTgvuDY45eQmqkCDStrWLjnPwSqR1dRMcudud405p8TIHoXqL7ap6x8BQ_-oFvhVKu0rILvHUsuf1TUDBTGG7uvGw6wlSGUSpc6CZmFWLeJAB_bY51M8wlohjlx9eIGU7H0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=U_uq66m788W7HkvLa6nVnrknn3zjIj33g2_U-F6br20Hj0iaWkNoNfW9ORRG1KVgdIm1CkKqa9_e-HBByR_aF5juizyEmc3bI814O41NRYnud3am_acph0MoyFzA-U41ei0EMCL-25gMQ_b_lPzsWGbmj9lBfEXHgXLl-AxMdzLfyRNKuXjexz_PhkCyazJTAEBJSC-OjHnetchVyAQTgvuDY45eQmqkCDStrWLjnPwSqR1dRMcudud405p8TIHoXqL7ap6x8BQ_-oFvhVKu0rILvHUsuf1TUDBTGG7uvGw6wlSGUSpc6CZmFWLeJAB_bY51M8wlohjlx9eIGU7H0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=UyHHmL36mwmzbQfSeYwYGEqJUKhkHgtNy92_QjSrOsbwgafqi1n5PjU8jKSm75Z2v_Zg1oVAKDfujTHk2LkFvks8FP8iYY71p2Rw-PaIOmram-YcxcbA_7529SgjtNs_yabIOhpk0WId6w9tBsI7ga4w2NMinYSOgSG8Hfcvzc5mICitoAxhe_bESOEof1z-cDBJgVIDyLbwygpG4TjlShJ_ebetx6fnQojNjI4xDhAnBiKjvM8g0PNGUNQwskavI5P06A_z7DcFeJhleRRelXT5FkQIniIBbahf7wfzwGguzeCLSHWX2cta7MzGWqHPB5xV1Kv7JbhpTJw6VQp3rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=UyHHmL36mwmzbQfSeYwYGEqJUKhkHgtNy92_QjSrOsbwgafqi1n5PjU8jKSm75Z2v_Zg1oVAKDfujTHk2LkFvks8FP8iYY71p2Rw-PaIOmram-YcxcbA_7529SgjtNs_yabIOhpk0WId6w9tBsI7ga4w2NMinYSOgSG8Hfcvzc5mICitoAxhe_bESOEof1z-cDBJgVIDyLbwygpG4TjlShJ_ebetx6fnQojNjI4xDhAnBiKjvM8g0PNGUNQwskavI5P06A_z7DcFeJhleRRelXT5FkQIniIBbahf7wfzwGguzeCLSHWX2cta7MzGWqHPB5xV1Kv7JbhpTJw6VQp3rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=l37pDpVGWQvArX1u4dpPsrYyQDG29EnYoRAR41eXidUw-7xlI-kspiLlq7Oytuj-ho0KLi__ItW7g9bEJIU0xonUChIRad3mWdVSaNtN2ogAwokXaW8zCO-y7NKyl_QluG7JEh0JFT7yH9zu1XwE3y5vB46imMS_p9dGb92GxVnlVva-0L_fgzv0NPvuycXOY7OOozcACo70JOAMx0tZP6Avggdzr0rSe7fkPM_dz0sSMjLDjq4QjNpxLLgBhHTXGfP5Z8fs93hZILJwrzLFcfW32c1EXN8ykClwsVIGvkdktffUbfZuw-vzdJ316ySH8JBbS--dl8tgqQ2-XG-Zaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=l37pDpVGWQvArX1u4dpPsrYyQDG29EnYoRAR41eXidUw-7xlI-kspiLlq7Oytuj-ho0KLi__ItW7g9bEJIU0xonUChIRad3mWdVSaNtN2ogAwokXaW8zCO-y7NKyl_QluG7JEh0JFT7yH9zu1XwE3y5vB46imMS_p9dGb92GxVnlVva-0L_fgzv0NPvuycXOY7OOozcACo70JOAMx0tZP6Avggdzr0rSe7fkPM_dz0sSMjLDjq4QjNpxLLgBhHTXGfP5Z8fs93hZILJwrzLFcfW32c1EXN8ykClwsVIGvkdktffUbfZuw-vzdJ316ySH8JBbS--dl8tgqQ2-XG-Zaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=sJKbK85tV5TWOjMZXMh1uAuQJ6R2BKdULxEFQxvKZD4ejas9nXScnlizsd75qY2CaNt15NjkXp3BmyJ6jHWPXr1qutREbOrUkieBpYOkGh_KMjhZ_8gfROnNemeQ8eX4sZOpGHcVho_Yh5Zo4b70IkgykAP_4LdU0nCPA2ZGccL_YfWXglV2fcskIXhcqWs9oRbyEqMBeFhRCAA0ngHkh6CwhRu4PLHRCfFZdwTd8Z4BgNbOUe7MYAZEHwVK2k_guTRuZduJIF0W69IqmX-PaB-iFraad0mesgM58fd2M0y1IiGfJfcgrTDdKxLRiyN379BORLbl4cPFDEsRwYrlXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=sJKbK85tV5TWOjMZXMh1uAuQJ6R2BKdULxEFQxvKZD4ejas9nXScnlizsd75qY2CaNt15NjkXp3BmyJ6jHWPXr1qutREbOrUkieBpYOkGh_KMjhZ_8gfROnNemeQ8eX4sZOpGHcVho_Yh5Zo4b70IkgykAP_4LdU0nCPA2ZGccL_YfWXglV2fcskIXhcqWs9oRbyEqMBeFhRCAA0ngHkh6CwhRu4PLHRCfFZdwTd8Z4BgNbOUe7MYAZEHwVK2k_guTRuZduJIF0W69IqmX-PaB-iFraad0mesgM58fd2M0y1IiGfJfcgrTDdKxLRiyN379BORLbl4cPFDEsRwYrlXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=Fps_lkfAw9M911E8wTdqSBMiXnzGH_CeuzplY3auE-_Akm0jqDg9i_tOkt3vy6aVHX4RmeVAS9M280Oj646NpDXPdjPddJwkg57uLRqfR2MxskBFQm1jqPd0F6RS5MlvQJdoJ8q0HQmL9E6QbtJjScq9iQfk8ZCM86i9Vuudw2ueRN4DoiGvNXVx00BhmKkSbEfRfJ053KEzUIg78oL7bpKmRoMrxmMC_lX2LYOOag6JJALeZLMSDU-nD65dRCq3byFjjpgMHQB1hfzzyd-0HO8H6DemOxgP434la8aMnghzu_Oi1VlD0ePIe8b1dVJMxcXEJ0pvsEyqyHEwvxmZJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=Fps_lkfAw9M911E8wTdqSBMiXnzGH_CeuzplY3auE-_Akm0jqDg9i_tOkt3vy6aVHX4RmeVAS9M280Oj646NpDXPdjPddJwkg57uLRqfR2MxskBFQm1jqPd0F6RS5MlvQJdoJ8q0HQmL9E6QbtJjScq9iQfk8ZCM86i9Vuudw2ueRN4DoiGvNXVx00BhmKkSbEfRfJ053KEzUIg78oL7bpKmRoMrxmMC_lX2LYOOag6JJALeZLMSDU-nD65dRCq3byFjjpgMHQB1hfzzyd-0HO8H6DemOxgP434la8aMnghzu_Oi1VlD0ePIe8b1dVJMxcXEJ0pvsEyqyHEwvxmZJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=dqQRe9OSbxVIV0p8IRx-smnKzTvdUsnkiDY-ct-3_T9kbI3dbAJ4oJ63egeJIIuDG8RkiRtfUnfmITP8A4irt0Hy0Jk231Z3EYD31fNRD_3yBZkVzIDV5PXinII7qWZgpJDKLq30snm0Mv1L7mY8JbE7F3OhyZuC9hQ14q-Z0V7Y8LLbr7xj8CH6ki1GWqdhCSbqUHUB4A-DBYCz-J4Ty1L2Ekae8dYhzlpRMlKMQrEy42MMzyZSsa1IFMJjCk0S-S5F9ph1mn2wg0b7thew474leK9VJ-8nlYsGHyUOHXhGZJ-AftU4erHhNhNCGY2eUURkOlS7H4kwduXioTW1VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=dqQRe9OSbxVIV0p8IRx-smnKzTvdUsnkiDY-ct-3_T9kbI3dbAJ4oJ63egeJIIuDG8RkiRtfUnfmITP8A4irt0Hy0Jk231Z3EYD31fNRD_3yBZkVzIDV5PXinII7qWZgpJDKLq30snm0Mv1L7mY8JbE7F3OhyZuC9hQ14q-Z0V7Y8LLbr7xj8CH6ki1GWqdhCSbqUHUB4A-DBYCz-J4Ty1L2Ekae8dYhzlpRMlKMQrEy42MMzyZSsa1IFMJjCk0S-S5F9ph1mn2wg0b7thew474leK9VJ-8nlYsGHyUOHXhGZJ-AftU4erHhNhNCGY2eUURkOlS7H4kwduXioTW1VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Ku2QZMl_E39LDohe8Lh2j7Io-98TmKR9mOoVMXLqaVtFwXfSOgh7QQDC5TCVZYhz0mzxYE5aHQ0UPqiB7Se25d1uMJ7tSeMNjbmzVdh3EzRPqRXk2wyzEPjPSCCgLR27-10D4I3uVFOpQ4Rczm90XYjdvvXkoOWynDlrQ6TB7vo4AUOJFCfcZJVeAcOr17uMNaE9SPJb67x-6K2Qmfk_swjEM1FLcC9UPJS7qTdpsP-wNQE6q7PkAkditZ_IgggsDsCMOpKiLJZGabr8sjoYThISHM6KSWh1Tfb0480beYnt_qhUS0ZOEf50nIawNP0w7VNaqq-xN0QvRXFXGpo00Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=Ku2QZMl_E39LDohe8Lh2j7Io-98TmKR9mOoVMXLqaVtFwXfSOgh7QQDC5TCVZYhz0mzxYE5aHQ0UPqiB7Se25d1uMJ7tSeMNjbmzVdh3EzRPqRXk2wyzEPjPSCCgLR27-10D4I3uVFOpQ4Rczm90XYjdvvXkoOWynDlrQ6TB7vo4AUOJFCfcZJVeAcOr17uMNaE9SPJb67x-6K2Qmfk_swjEM1FLcC9UPJS7qTdpsP-wNQE6q7PkAkditZ_IgggsDsCMOpKiLJZGabr8sjoYThISHM6KSWh1Tfb0480beYnt_qhUS0ZOEf50nIawNP0w7VNaqq-xN0QvRXFXGpo00Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iP0cMCKMVt7eW6XYgLXrRBbb20tZy-mfu80gYebQzihn--C3LfkBEWHUEbPnx5BfQB1oYaoZeJKLKjmtK3jruziWEt07J9jHsgnwxLK1jFoPOjRD4qiZvy8MyyJUM_-Vtus-CFfk3j6cUGfs51s72h1k40Ng5w11wn4kuP-GKsRxCYMAQC8V0ZKHQbOliiW7-QxV4MdrbPnJyOftYBYOa_IJttv2L74hOvOJ_lZYdEzYTwyQvXl-bwu26O8O4Em5AOGZ6kqukZ1SO1kVcY9ugfltvUFQHdRmSYWmNnnNhQfnp4Bg6kcr-Z--1Lo1IJ7cR4qTOtVGZJDoBIPeJ6AUnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=SjF2IbU24fG9dPNMstyF6cg1IBG-Lqt3oHxP4Cj-ULVjlu9gCuiVrPHWIPsSVJr-rlUeJQPO7D1YXKBhCPyrPC-L4HbYvvxblMl_W-rpAkGe30Zc311GS74cqeZZA7ZLIspM-awTh8fK71uyoqsQdZpS_x_TH9hhaQ8ZuWQQ7m8rh2nd5JfGf0NX-mlaJbcthxosA24XkKN1PpNurZAfrJDIijZTgtJ9jlDJMYEfLVho5djfjNcRe315lYK-8VH-ktPJhcSgK77Hs4WAWNY1B2PVP24L2JPhIdEK8-81e6s55HXlOUCG1VqQa7vVALjyTG4d_qURJlX69R769Bh58g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=SjF2IbU24fG9dPNMstyF6cg1IBG-Lqt3oHxP4Cj-ULVjlu9gCuiVrPHWIPsSVJr-rlUeJQPO7D1YXKBhCPyrPC-L4HbYvvxblMl_W-rpAkGe30Zc311GS74cqeZZA7ZLIspM-awTh8fK71uyoqsQdZpS_x_TH9hhaQ8ZuWQQ7m8rh2nd5JfGf0NX-mlaJbcthxosA24XkKN1PpNurZAfrJDIijZTgtJ9jlDJMYEfLVho5djfjNcRe315lYK-8VH-ktPJhcSgK77Hs4WAWNY1B2PVP24L2JPhIdEK8-81e6s55HXlOUCG1VqQa7vVALjyTG4d_qURJlX69R769Bh58g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=n7yWMTLUJbt5l9S6W2fay-ukzjjrferSfxN3OEnVrLMB_XgD1WbamD3midhXWZF8jRpZ7_Hzh5Yb1qJ4vmOUIVnjurk2NEzFD5zn3YLCFskFaAs8s3QO7vKlB7U64g2i6LPfOYoqvsu_Tg6XAnxq3e4cW91Terj6eMrrb07hs6sl-LDABKHttDLRKsKqWFCqwW6pre5HSEdV8ieM4p1HCFgvWjkTSjpu1fsbuEwucL4Ny7FIYy69F0qnCz8U1GKVv6aD2L8SlHjkxFTY4NJZQtdJfLR6-hBnUGC_yheA9J7QFElhsC9TdQDuLeDF9MBUxYD32A4tjpjQJUO182_p1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=n7yWMTLUJbt5l9S6W2fay-ukzjjrferSfxN3OEnVrLMB_XgD1WbamD3midhXWZF8jRpZ7_Hzh5Yb1qJ4vmOUIVnjurk2NEzFD5zn3YLCFskFaAs8s3QO7vKlB7U64g2i6LPfOYoqvsu_Tg6XAnxq3e4cW91Terj6eMrrb07hs6sl-LDABKHttDLRKsKqWFCqwW6pre5HSEdV8ieM4p1HCFgvWjkTSjpu1fsbuEwucL4Ny7FIYy69F0qnCz8U1GKVv6aD2L8SlHjkxFTY4NJZQtdJfLR6-hBnUGC_yheA9J7QFElhsC9TdQDuLeDF9MBUxYD32A4tjpjQJUO182_p1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Jk6qu4tVh9J9N2l_sV4XON17UaKDegxSbjrx2WIoNKHGdFCbhXvAiHYHUtufZOTaVNpqXzNPsjsx-0XdCeEpgE9K2lV0RyTSeqk6L0EMs1b6VsJCu2kUJ6qqPtGA-Lr6wRhkxc646rr97icruNJrLBZ2ZL1gB_iV77Xk4t5jzHu3-MLT7mnPmso9kjwnPhUr1I0R3FyH81lESCyDEvKWsnMdAFTfbCal69pdmoE_FjJPiBjeEiGujLNYmYgxwoC3nkTHHoWOeus4hvsJuFUSEefmTurzF9AOn73SzaOLXJUFM97FC8evqTS7-6NDY2KAnXri466BqK7j8-xcSgmDpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Jk6qu4tVh9J9N2l_sV4XON17UaKDegxSbjrx2WIoNKHGdFCbhXvAiHYHUtufZOTaVNpqXzNPsjsx-0XdCeEpgE9K2lV0RyTSeqk6L0EMs1b6VsJCu2kUJ6qqPtGA-Lr6wRhkxc646rr97icruNJrLBZ2ZL1gB_iV77Xk4t5jzHu3-MLT7mnPmso9kjwnPhUr1I0R3FyH81lESCyDEvKWsnMdAFTfbCal69pdmoE_FjJPiBjeEiGujLNYmYgxwoC3nkTHHoWOeus4hvsJuFUSEefmTurzF9AOn73SzaOLXJUFM97FC8evqTS7-6NDY2KAnXri466BqK7j8-xcSgmDpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JEWAmlYqcmDMG-wJjdGaWiWnT0NrUUevvuTbZ7gS76yFD_zT_IKMsZeHJpxTJ4g6UN7OSSc6JazBA7hlGvMyLlrT2E1VbFh_SaXK7uqVA1USIFbbRHTw2hkxV3_aDqbHAZOSMfP9JGFTEVMxAZZtftAwv3AjNH8XsQ7bf8jxvWPPKg75C1RuT-DTjs88NLu_PWLn_nWuY_Y5hBHpj9i1ecHbvT0I5GeTNgQOlctazJOWRBXUgtnLoEQSPXGWrGds_xUjQTxqMlZRlGK_lPUpXMcCehdhDJprgTL_lsplw_vPkERrq-WWrKi6vfgg7YIH7eo9S4hsGYeRsBC-g5qNcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGWGWijODylOvAYUU0IJGp-bt3O9TQCm_Ol5hvL3e9r1FgOe7ZhWzQ6mCIdA0sQUar3mKfQ7xPDdFOUJh8xL-K2gSiI1d6FmvG_lAmUQvBu6CX-pY6VTVXITe1HtK4OUHAs4ieTGLe9TRyNICFp2EKmzEI6mtr7fOthl02kbQVgmuRKOjOPkitf0GGcZnCauQHA9y29mNK8Ebd9xEywkx2XVNJcrM8Dcbc0Z7jRx8ct2cw0TSqZZx0YabYYxQl3TaV0bhcLy6WKICNMU6NEzJsbsQ5toXcbim9MLH7XjcHWdJ_3HS1bsZ3EvJ7ziFONSz4VFbp5_NgaloyEWj8a2uw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=rcOPVEM2eU0bNW31fW1ZllqPmeBNYcc31WE2IWUP9CjoaTgU5ZA1gXGMNWJkQfZdxXTqBjrilbHAubd7XvRONesUt1y7ZdpOQFyBdmHEqE7NPZhQEa-E2U2Jzjh9a2rA6evb8io2CRrcQwCDHf_5NwiPgGxFgtgXZw0s2w6CEobymgKAPAMOXAoBY58GFn8Q1Yppb0oA7jQtUESUS5ZCXkC6NmFKezu-fFHiTmsYsNdJXpP5DxtAoYDeXHaSnncxu25iSPCrAFGKGmd6-5-WA1jdnAUEKoYjfN6Vtvp5_DOFbDcVSd_qp6KrkeTIySvum2Cte58CiT4N-xAmCwa6_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=rcOPVEM2eU0bNW31fW1ZllqPmeBNYcc31WE2IWUP9CjoaTgU5ZA1gXGMNWJkQfZdxXTqBjrilbHAubd7XvRONesUt1y7ZdpOQFyBdmHEqE7NPZhQEa-E2U2Jzjh9a2rA6evb8io2CRrcQwCDHf_5NwiPgGxFgtgXZw0s2w6CEobymgKAPAMOXAoBY58GFn8Q1Yppb0oA7jQtUESUS5ZCXkC6NmFKezu-fFHiTmsYsNdJXpP5DxtAoYDeXHaSnncxu25iSPCrAFGKGmd6-5-WA1jdnAUEKoYjfN6Vtvp5_DOFbDcVSd_qp6KrkeTIySvum2Cte58CiT4N-xAmCwa6_oWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn1T51mYZsAIXoIW6qt1a6U-PC8_i_X0dPcF0WzeDFvpR5y9H3G6QeeZju3ojvBrYgek1FcUD9-SGrVXQ6Jl98likiBD71ISkJHd5gHhmp8BnPBzcFy-_CTt9ZfQq2Tu7fef0Rb3VAQRE4UZk82yp88vDyYGHptVb_B3yEEOmwRvO38usDi0b7m4vEnX5juPJC1wbP3cKprluXekpj1amfyXrH1ITtaoaCdCR-m2E3-AbPkn1hoHZYVhpXsiJep5bJHFB7g2ueUU8uyesmzDbVMFcDBRHAyQwWjNj2anwMS6zGkHlHqJernQ4BOkB-fqBXNBv9KnL8ewFDJ8HSPbJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b_fHkHOqlxjDs_DpcytZXjkx_keltm8J-hkpIDtZUpCeNANR_ezU7MlAZbWwpOyj7kNvlVo33ZUdF1WiAj88UCNUTDFqdzNGDId1Vmt7X8PB9uZ8WQHwhHLrEm7vf7lpDTy2ku9ENNvVK4xsMkZTNUVORYutCj12UQuJ2TXP8QpEV7PdE8CzjEcwv2a1kurp9FU77o3Ysk4jniRlkOU5yILGF8LI9dTV0dgPOVyhMX9MhYb3wKGXtDBQOxZJcUC_KyemD4zFdAlPN4R9wL17jQHqTGConN6pQSjgHgdnXD7E7qTXcAfvq02WMZFvdO_QVP137TWsd_p1UJ5qae8WKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GykqBH3uKmVBDAghxFEq67J_aF3tsBLVOsg46do4Thrjtwc47WJxoRUJ-GIOGSizA6gxn4SHCjn8Kj1v0E4M4bnySgdw61pF5O6b8hHzW-BCKSaBKzVlCQlOoywXVGXGQKcespsRaRldW7JLo7IhPOY5nA0w0SI4dNuWjf9JlBSMrk1N60D-SKOTFhG86X9RghFbvJ6gahLiBMg0JcJl-izYKTzUw9IFSmYmmiWeImXgkRaxTThXPRMj0ZhKdHr3cycreW9m4MAHnDVZWCcUpx6Ix99a0F0Ool91saKifOM0MU_RrgRuOhXWsxHjfT6eFkh6BiQtbP939DeJUKcfAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln7VceBOsHCxDz3zbvwOxDupWsGwcv1VnFyWl-PBsYIaD5QTAqb31kiUjq8-l7nvmlILCDO3NTtNjH5V3uHDES0oT1aFEDenDBxncma6v2VEe-Aa9DIaN2ZWBCl84ZCO2X6T7r_F-nFM5ZT69bD8Spnccb4np6GIhnHQaAslL9dN03iN3nVvGL7ZvaCeb65s2HyPsIjeRAjggIh5RsQnXYpSUhEc6tPLVa8aAu_m8phyxaiB3s0fzKsYH-C4pPf0lYxwgDDk-rI13pX7FweaUu-eWnx4MksI5z00zE4r68eRrdsyMx8MD2YTsIDtt9aGKHQX4eNwSZNqCuJbvsfMnw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=WVwMYOPAu95IXCpFCfG4TPomeLaNQSq_mdJD9BH31I88R4BInNnj0wuyHrXlPVnmsDLAeLRJ0jrtOk1uB6C9eS2S1f0SxTEMXjxzTMx2Ca82YWUcspkh0mLCq4bayTgYDTgvuLpTi--zNv2VDez2syQ55gCzobrrqVW79xoCn2cQo4GhVMt95DB_ZLzRG0531Q0TT62qsJV1B-TqPXI6yAjCjK0TqhQ7C3rIYSmvkTj3fB2IvH1Qmz0QerFHtSSMoSuGcKmumLUFZyosUMfwVZEijiKakJy5-mH1AoOAFoBGltoAyG7UhMbqnBJj5JsotO6jzeJEmeYTqS2WkfmWZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=WVwMYOPAu95IXCpFCfG4TPomeLaNQSq_mdJD9BH31I88R4BInNnj0wuyHrXlPVnmsDLAeLRJ0jrtOk1uB6C9eS2S1f0SxTEMXjxzTMx2Ca82YWUcspkh0mLCq4bayTgYDTgvuLpTi--zNv2VDez2syQ55gCzobrrqVW79xoCn2cQo4GhVMt95DB_ZLzRG0531Q0TT62qsJV1B-TqPXI6yAjCjK0TqhQ7C3rIYSmvkTj3fB2IvH1Qmz0QerFHtSSMoSuGcKmumLUFZyosUMfwVZEijiKakJy5-mH1AoOAFoBGltoAyG7UhMbqnBJj5JsotO6jzeJEmeYTqS2WkfmWZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=f-IwL2XDoRvGy1iawWbNG8YLgfnCjN4yJHSKZoSnHvqXoWCFithRWAM5vXKUXQ6qscasknYeMzH5PwY2qVeddgatdWVbQ9YW0g7wu9RK68T17IaTgD0rrqrNChmXWs6xR6cEKk1oyCdWUfqCzksBjGmRd0Hzq72NYWAoRYH84pzGVHLyuMWcVSGSO44_91darxa8-J1FCSHN9UFfCduaK3Y65BbZjsd70GudYYq_K9BCEXXLZLI5fRY-ci3Vdkqaac4ijK_CCzX6thDMqKRa6ygpSFSUq_xgytLCm_bgLe-I3smx8WP-zNRKyyIWPj6GvN0Y0JWJ1it3NIHlrul65Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=f-IwL2XDoRvGy1iawWbNG8YLgfnCjN4yJHSKZoSnHvqXoWCFithRWAM5vXKUXQ6qscasknYeMzH5PwY2qVeddgatdWVbQ9YW0g7wu9RK68T17IaTgD0rrqrNChmXWs6xR6cEKk1oyCdWUfqCzksBjGmRd0Hzq72NYWAoRYH84pzGVHLyuMWcVSGSO44_91darxa8-J1FCSHN9UFfCduaK3Y65BbZjsd70GudYYq_K9BCEXXLZLI5fRY-ci3Vdkqaac4ijK_CCzX6thDMqKRa6ygpSFSUq_xgytLCm_bgLe-I3smx8WP-zNRKyyIWPj6GvN0Y0JWJ1it3NIHlrul65Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddtoDU7-YGQ0cFmX_EtIlOoPXU3UtlG-U-tqYpqTYeXp27h0R_rCs6MVsYBPt6GhTMUUoSrkp3cS5GcKyjl_iDxLVfN8awRVaLp6ME9EjzDWBs66jbJM8FeiIhxQ6pS3ngQtmP3lLBSJQFe3ghIYUE8Pxf3c83EKu1XRLoesjmvisZ1uOrfps0wnajQguTsZq8wqCpeAR-26oKdYxjqEzHF9dMg_8R67iU1Z1BhjWmRbdgMy3NArS4_WiuUIrjN2gp-NyUVBUC34uCNU4LhHhdjS3-oDV3_S4iW-1FpFXi6-ewzy0qCcM8BGN90uRzQKjExExE_Yb6IoaWfh-a8KNA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=nVhzumtNSSeA3Myjv-VTCG9vR6nVV2TGNhbo5SjThXSsDi16svCRajot7Ba3hyT5RHmiZz22FkTbbfrkKmc0Kdzzntr2Y96VxijnLsZGgRFH1B687xlMq7kinnF582UQFlZDhKARqw5K2gBQ34Q4CpC8WcdGOPLX07Y44CB8LJwnd6Ub-gf98F-aFMMyq1J6SvUvYKpi_Tk4ko3GgBOQujJCB07UO-axsKe_5OhQMf0_l3rDHx-zom1A2zbMNr6u5AhxilXtfwy8fofcaxOQwMqrpOeCWyN7RO2zIcATS6ec9UecbcQ5_XmuWhj94FyLJfln1JUGFVSjcUNb5bFk0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=nVhzumtNSSeA3Myjv-VTCG9vR6nVV2TGNhbo5SjThXSsDi16svCRajot7Ba3hyT5RHmiZz22FkTbbfrkKmc0Kdzzntr2Y96VxijnLsZGgRFH1B687xlMq7kinnF582UQFlZDhKARqw5K2gBQ34Q4CpC8WcdGOPLX07Y44CB8LJwnd6Ub-gf98F-aFMMyq1J6SvUvYKpi_Tk4ko3GgBOQujJCB07UO-axsKe_5OhQMf0_l3rDHx-zom1A2zbMNr6u5AhxilXtfwy8fofcaxOQwMqrpOeCWyN7RO2zIcATS6ec9UecbcQ5_XmuWhj94FyLJfln1JUGFVSjcUNb5bFk0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=HE-yc28awGE27D9eHmCXDhPZhrILsf-v9n0Cg4YU2ruuTkD65ViagtbRnPMWAakvCkm-kvr5NqxCZdkRtmpufOu9kVzZQCYDsZ0IaOyG0r7C9T2vfRsPTNeJGxH4zjwDQQUN3B28-_Waw9tDOtqCkMNyMXGmdxXrsR0utNucEeLM-bpM0LvhKZc1S93EJGf0vlbcINeKARPoOJSxbXRO76dbl46n1lVuuLJrv_MIgH2gZxsdSGLMxWLAwO2P_wblPtD5GW5rk_aYFEC3NJiz1r4ijA4iQfJPwrCKRWz8089Y1ZEMTNFtp_-5eEhRVf_lLZtcFfDqcNT-JbYqTqS1Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=HE-yc28awGE27D9eHmCXDhPZhrILsf-v9n0Cg4YU2ruuTkD65ViagtbRnPMWAakvCkm-kvr5NqxCZdkRtmpufOu9kVzZQCYDsZ0IaOyG0r7C9T2vfRsPTNeJGxH4zjwDQQUN3B28-_Waw9tDOtqCkMNyMXGmdxXrsR0utNucEeLM-bpM0LvhKZc1S93EJGf0vlbcINeKARPoOJSxbXRO76dbl46n1lVuuLJrv_MIgH2gZxsdSGLMxWLAwO2P_wblPtD5GW5rk_aYFEC3NJiz1r4ijA4iQfJPwrCKRWz8089Y1ZEMTNFtp_-5eEhRVf_lLZtcFfDqcNT-JbYqTqS1Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=j9PqenZbuz2MQxCX_RziUj3wjdwGvYvOdMCqgX1N_CczDTR-NF68jgSp1O7pokXTYbCFtx2QeKQtSGsEHKTkF9j5hdijhn0F9Jqdmlp_XMquwuci-7pzCTdndcURLqQBM90hu7vXmVZMraYPleI77zzy-qMwQLAJg0t-zlRbtTPZj9SjvzvsEQaPrkBBfXUcAUNzJVZuItQrzZ8bG1vRumbHkETsPolDe534il_9t3ac_2zCoKXupLMZs5qxPhEYgHgpmeudfDhTbHjgAUGvC1IYFDYkwVofosWJL_U6pnGbDaAxie_p5mkmW5_fcw7d-64g31MqS_5DuI43iMMKeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=j9PqenZbuz2MQxCX_RziUj3wjdwGvYvOdMCqgX1N_CczDTR-NF68jgSp1O7pokXTYbCFtx2QeKQtSGsEHKTkF9j5hdijhn0F9Jqdmlp_XMquwuci-7pzCTdndcURLqQBM90hu7vXmVZMraYPleI77zzy-qMwQLAJg0t-zlRbtTPZj9SjvzvsEQaPrkBBfXUcAUNzJVZuItQrzZ8bG1vRumbHkETsPolDe534il_9t3ac_2zCoKXupLMZs5qxPhEYgHgpmeudfDhTbHjgAUGvC1IYFDYkwVofosWJL_U6pnGbDaAxie_p5mkmW5_fcw7d-64g31MqS_5DuI43iMMKeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q6FNqCcNMoa2QTCeEFiVeKfK1q3HnJP_ZJ2JU854RCoKk_T-tPg3Jl4pEf-D3N6v-Znj1ZrebyEHFDH30_Db03TuIQn_6OlZfo43Iksyqm4XtsTJyhXazxVQhbxHejYpXjokmLVCRIBwxHWJkZINBmdXRRmRIrpyp1WQqlNFaErhSFOu00vu1fXreiQrspOw7Bt1em4LAhXEi5zl2TuiafilgFdNvtozzmORY_qSqaAvU4gRp1pbn6x6xTEH_pLCubAAdF9PmiiLhL2CM1Xq9GeaLnGuap6Lv7wqlwvpGiRK_dAsCQuN7l_r0of_GeeSLO8JianjFOeh5RfcNk7ULw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=PI0w4oV58pOtavUEsGGiKQXnMo6Jwv1uo9RuubiXGzucSqhJTWASnQ8nCEJkDchh4QbYYpXtHECZTk2X8CbzfwSmypUM50vFT-e9o6s1JLSIjNpF-pX-ZMEPgp4551y8pHPpkEKxxhRwZS3kd_N0IuSOX-NNnkSOMvLexk0Yru8nJcZbXF34p6ItivbBd3jo-sWUlfxguPPveiygmyXxqGPQoNpQ_WhNmFGT0cNPajQ47U5mHCK6k4ifpwR56HhyoRS1CthMcBArE8HAqCk5CseVc5sbOSWK19usV6m0r5x6u0ENaMhSt5nIK8VZrcWgrUjAiKj-T8ZFiFZxvmQZQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=PI0w4oV58pOtavUEsGGiKQXnMo6Jwv1uo9RuubiXGzucSqhJTWASnQ8nCEJkDchh4QbYYpXtHECZTk2X8CbzfwSmypUM50vFT-e9o6s1JLSIjNpF-pX-ZMEPgp4551y8pHPpkEKxxhRwZS3kd_N0IuSOX-NNnkSOMvLexk0Yru8nJcZbXF34p6ItivbBd3jo-sWUlfxguPPveiygmyXxqGPQoNpQ_WhNmFGT0cNPajQ47U5mHCK6k4ifpwR56HhyoRS1CthMcBArE8HAqCk5CseVc5sbOSWK19usV6m0r5x6u0ENaMhSt5nIK8VZrcWgrUjAiKj-T8ZFiFZxvmQZQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9XosC9EvrUaZrgt_C0tw11oxgX0mTpKSzo5waNEmmLyGbnRPQRFvCxcSbZdyKHZ4t8EIzxbrKSgWL7i1BsOgTlFdt3QtBhtlZW86u3yWgARmkQo4lviXQxdOkNpFy5x1ZNLeljzVFjW3JIUqmeNaLENm5dUfqq30gqWeRV7h_BR4SBxsiASwEnZ2MI3IzVYA9F7fn5uZmTQABGJ8j2ozKSlzLF9OCrqo1cJ59o5g-2GhJIcjGYoq90T6G88cFZtfla7mFNrt6oIcXOFAMXlPHJ21OEIPNduNs-pCkiK9vzLW06XLvg0Ewozacy0KQdvtqlI-AUio-sPyq1aB7bv1PLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9XosC9EvrUaZrgt_C0tw11oxgX0mTpKSzo5waNEmmLyGbnRPQRFvCxcSbZdyKHZ4t8EIzxbrKSgWL7i1BsOgTlFdt3QtBhtlZW86u3yWgARmkQo4lviXQxdOkNpFy5x1ZNLeljzVFjW3JIUqmeNaLENm5dUfqq30gqWeRV7h_BR4SBxsiASwEnZ2MI3IzVYA9F7fn5uZmTQABGJ8j2ozKSlzLF9OCrqo1cJ59o5g-2GhJIcjGYoq90T6G88cFZtfla7mFNrt6oIcXOFAMXlPHJ21OEIPNduNs-pCkiK9vzLW06XLvg0Ewozacy0KQdvtqlI-AUio-sPyq1aB7bv1PLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=Hhjk8OirfC6mNsidaCoWJmuOhsuPpET3u5qkM1OGyJD9cf65v47Yd4kYFvzyQ7vchw4TeAYDOK9VCWIj8WwM-L6ImwBz0XIB9RPGMhsXByCF5BW7eLo5oqcoccL59wVCiS0JVleSd4UZBq6Zv99T2v7JQP6af9KkekI29dshmSciFq8MLqMlE55iVTl_NRXs0RvQ2k70x8qMaYyXrtBWv7RMjldpOx-YPwIzRqA2AM4hnIksY0ewG6c0yN-n7RbXcnrg8_r6IyciPO2HSUKeh0dvOi6-mP5W1mmVrcXa7T8mwIJ5v1d5ca_wLZ-YXsOl79W36t4ZR0uv4qlQiqWs0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=Hhjk8OirfC6mNsidaCoWJmuOhsuPpET3u5qkM1OGyJD9cf65v47Yd4kYFvzyQ7vchw4TeAYDOK9VCWIj8WwM-L6ImwBz0XIB9RPGMhsXByCF5BW7eLo5oqcoccL59wVCiS0JVleSd4UZBq6Zv99T2v7JQP6af9KkekI29dshmSciFq8MLqMlE55iVTl_NRXs0RvQ2k70x8qMaYyXrtBWv7RMjldpOx-YPwIzRqA2AM4hnIksY0ewG6c0yN-n7RbXcnrg8_r6IyciPO2HSUKeh0dvOi6-mP5W1mmVrcXa7T8mwIJ5v1d5ca_wLZ-YXsOl79W36t4ZR0uv4qlQiqWs0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7qhCJhxlHtaMuCQebf8tvZViuh7V2snAXS0EPkdkQzV-d0kgNNgOCBloU3aEa8SgcssdZqu2s_Q1WeWjM_hyMQu3TQ_4xyAlLDocDt4YAzE1yYs0LUCP0E1UcwMzq8MxSMdcnzDnhRtv8pX2H9ekQ65ZG3ZbJ1Ifsqt85xdTmPw5rl2fL0mksZYGC6b_Qn2z5jVyA4N_u6bGCOkKuRe3miU_1Y7aJ9yZcjtTmrpt7AGyC8Vyc_eFkUPBIGw8F1zRcgvZPsVXT4Lt5OPgwTRQX6S-O44eWNLWzb0Y-uagMjyoL9IAdOHBFEjNPzjeHOrvf1ccfFLEvxnfpIUY-IO4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=QL6Wj_RdefEsGwbDw6YrzXMVcuw8zK-XWrmb_CGn_48Qs8xjb_hdCDh_jypVzR_NTt3BDsZpQ4A61aw897u5LCrH9f-ncyDO7okqX2GrfU6GOTZoSMSp8pO68nCqy3qzGypnbKm9egb2CSkYnsV4_XLelGJX0ce6INSZvLJUWifXr88mBiOUigIs5ydtywWwiddhQh3spb4OBU9n7x23rj2xIH5C7rDHyiQHn4vdbT8xZg2GWPamdujHs03OqvQiwZZIxv94yGJYf4VZ1TpURQx3FxPu2vUVK77TMYEYTLnhvvUaWH5Gzo9TjSCQ6jr52aicMvasXkKhaFHP8AnwHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=QL6Wj_RdefEsGwbDw6YrzXMVcuw8zK-XWrmb_CGn_48Qs8xjb_hdCDh_jypVzR_NTt3BDsZpQ4A61aw897u5LCrH9f-ncyDO7okqX2GrfU6GOTZoSMSp8pO68nCqy3qzGypnbKm9egb2CSkYnsV4_XLelGJX0ce6INSZvLJUWifXr88mBiOUigIs5ydtywWwiddhQh3spb4OBU9n7x23rj2xIH5C7rDHyiQHn4vdbT8xZg2GWPamdujHs03OqvQiwZZIxv94yGJYf4VZ1TpURQx3FxPu2vUVK77TMYEYTLnhvvUaWH5Gzo9TjSCQ6jr52aicMvasXkKhaFHP8AnwHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=t94YyqI4k1P_b0xQifJrtZ9Cge4p-EYP6uBZ_OhdrPiRtfOqIATQ-xSCeL8p5VBono1RzsyT9rrQvhP-ekBFJ15DKN7QwXv_r9_943iaRU93OUPMVNhloQaxUXq4rxsGQiCx8u7KHp84t8wToFSbI_A03rMuUd4zniJ4gqmm4gpFYXswjWKJprG28N29_m-Hudt0ceH-Jx7MEUqrZ-0guVkm6wAK40v5cVMWd2CwWoRZvbMDYA-IMvottm1FlZ5h-uoOitTeYXq_yr-TUDLLn8ypvGBHF69aCHYh_ux_uXVKVbkazHBiXBRvazr7joVSleKBRxvQTkyNAipgoCva1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=t94YyqI4k1P_b0xQifJrtZ9Cge4p-EYP6uBZ_OhdrPiRtfOqIATQ-xSCeL8p5VBono1RzsyT9rrQvhP-ekBFJ15DKN7QwXv_r9_943iaRU93OUPMVNhloQaxUXq4rxsGQiCx8u7KHp84t8wToFSbI_A03rMuUd4zniJ4gqmm4gpFYXswjWKJprG28N29_m-Hudt0ceH-Jx7MEUqrZ-0guVkm6wAK40v5cVMWd2CwWoRZvbMDYA-IMvottm1FlZ5h-uoOitTeYXq_yr-TUDLLn8ypvGBHF69aCHYh_ux_uXVKVbkazHBiXBRvazr7joVSleKBRxvQTkyNAipgoCva1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=HwSvsoHM2Zb2HuWfUPiswPmNbmCbSpgNa5t1fBUbNkzcGrMlhPy9JuLNzFWVrXgWzKjeFwKgW3oLXpBF1_sKtYanjX_Ejrv_YSIwSHexQBusp0Kv7ih2L9T0nNcg5t2qFKwcayEhrFGCvc89hXojStEyH_FImijrVKcVNsW2HhqTfaiy_dYfUdKL63bnV2qRFNoAA0oZZW40FEFMxuxlkzVPjvGI5mdVgxe2-GMUjVIpHUsG6VNaHqhpK3OzX0S9vSbcYFfPpWI0PFJA2UeswR9XVsmxqT21prZzdkb4AwviseaLYtc5rgVCJDoyz_tqRvaDiOcW39-ehBFyJU0CBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=HwSvsoHM2Zb2HuWfUPiswPmNbmCbSpgNa5t1fBUbNkzcGrMlhPy9JuLNzFWVrXgWzKjeFwKgW3oLXpBF1_sKtYanjX_Ejrv_YSIwSHexQBusp0Kv7ih2L9T0nNcg5t2qFKwcayEhrFGCvc89hXojStEyH_FImijrVKcVNsW2HhqTfaiy_dYfUdKL63bnV2qRFNoAA0oZZW40FEFMxuxlkzVPjvGI5mdVgxe2-GMUjVIpHUsG6VNaHqhpK3OzX0S9vSbcYFfPpWI0PFJA2UeswR9XVsmxqT21prZzdkb4AwviseaLYtc5rgVCJDoyz_tqRvaDiOcW39-ehBFyJU0CBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=upul7nSRyWaNfpd5SerF7ejdT4fw3sSSC20ztY4Nleiv6jV2kF7hW1WE98MROWPJEjpowU_4-5KapVQGYawfAowiErsY-UisU7a4dZl6zDI24PXaBfLonkbgqEDxBQdWjS-KDEMVZkU5O1iFweaDEuCRPXKc8OmUfO6F749W1OKsfDj3SukKNFLmcPxrtL0MTOZNcNAksNDuIAV8EahVbnR2iFq4i1nzH6LoAsAiHEX4XB_nbDe7MyHAq-P--umJ0RjgzF6I6mFt7Ar9xwQS2MiRapOm0MpKKajrOz3EXrQ7PfQSq3nzFTAbP8tb_kS5KIMpLP0uncYrlHAfng1M4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=upul7nSRyWaNfpd5SerF7ejdT4fw3sSSC20ztY4Nleiv6jV2kF7hW1WE98MROWPJEjpowU_4-5KapVQGYawfAowiErsY-UisU7a4dZl6zDI24PXaBfLonkbgqEDxBQdWjS-KDEMVZkU5O1iFweaDEuCRPXKc8OmUfO6F749W1OKsfDj3SukKNFLmcPxrtL0MTOZNcNAksNDuIAV8EahVbnR2iFq4i1nzH6LoAsAiHEX4XB_nbDe7MyHAq-P--umJ0RjgzF6I6mFt7Ar9xwQS2MiRapOm0MpKKajrOz3EXrQ7PfQSq3nzFTAbP8tb_kS5KIMpLP0uncYrlHAfng1M4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE00hi21N5QyQa-B3yPgtL-cjbmghy8-8iLTEYIy9TuazWNPws1dnGwqZWZySdUhQGQOIfzkCo4MeU8DQWBRwVr7RQ5kiCc_5h9e-OJ-YZMzV47hcMtjYB3DFwpSwtptJ19sYYdIATMAVckBZO9C6Xxy_8voQSU7ofa9LNiGd1yJtl7UQbvo7SBnpXesOBGMdqKrBMem1-B51x9Ahpa9eCeC1zBG8e0LQtuqP2kGUPmTOLDvhKg--GtioAbUEtVptAOaiuXejEF0rn_PSCxtreEDHDdN4qmhBF2x80PP8Yuqaw_b822RGEFm3A4eGoVqDzzkD-MamI8iQzH3bGe7ew.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=ByeicNUk1tngsSyBPqREzmOgQx183ngeOfDM8EOYWp0TUzr75NYIneCpjKEp9-oWTCsM2wOOKTgOvBFHkiEU1JcZh7TSXFTqWJ1DxSP0qd4RwnEb_E-qxb5hm8ToVt-mA26yqQ4xtrh40HKGYAuO59qqbXBenmw4HkXH5IWsUeYliR4DpMEtQhg7XpvQojyDijFXy1rsFx_bHiHa_ltRB6OKA1iZ8uxOPpZ-ZxQRqKjOTztmWvabBpucsEdVZSRW1UNgQcINotQuvp3lVYiBlqUNa-jpnO8-qPsvxmvds9R1Ax7tsSpBI4eLioWxandZY8s2vNWMw7FrGt5Yc7D_Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=ByeicNUk1tngsSyBPqREzmOgQx183ngeOfDM8EOYWp0TUzr75NYIneCpjKEp9-oWTCsM2wOOKTgOvBFHkiEU1JcZh7TSXFTqWJ1DxSP0qd4RwnEb_E-qxb5hm8ToVt-mA26yqQ4xtrh40HKGYAuO59qqbXBenmw4HkXH5IWsUeYliR4DpMEtQhg7XpvQojyDijFXy1rsFx_bHiHa_ltRB6OKA1iZ8uxOPpZ-ZxQRqKjOTztmWvabBpucsEdVZSRW1UNgQcINotQuvp3lVYiBlqUNa-jpnO8-qPsvxmvds9R1Ax7tsSpBI4eLioWxandZY8s2vNWMw7FrGt5Yc7D_Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=IL7sQeeQqksasMLqTAefyg61wjH68aNq9O_VxfCfXVg1TnLt1EPpAKYTDgyGX3QY3djvxSPXl3fJ2OZL8TzB4zIy6ZXpr0cP13FZ-_FPSr6CkGOv3o0KHAsgvSri2JVrQUj6oTr7WYYIzF2T79u98rRmdDv1PU_Bo3SzdJo6dArkFKShvkPgja-fFKAC9gDnD-UMoqJ_JGH2FMRQiULD5w7p7Indz8l4mGQXTLzslBinwodf2bYQlgfcfjvIoLw8FMAB2Fu-TBJCLdXSg799t7-NEsMZAT1OzE4GMkNfB0oVtqGnGGGngD4cqPASusoy3AY8qvKFjr1uauxKl_NltQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=IL7sQeeQqksasMLqTAefyg61wjH68aNq9O_VxfCfXVg1TnLt1EPpAKYTDgyGX3QY3djvxSPXl3fJ2OZL8TzB4zIy6ZXpr0cP13FZ-_FPSr6CkGOv3o0KHAsgvSri2JVrQUj6oTr7WYYIzF2T79u98rRmdDv1PU_Bo3SzdJo6dArkFKShvkPgja-fFKAC9gDnD-UMoqJ_JGH2FMRQiULD5w7p7Indz8l4mGQXTLzslBinwodf2bYQlgfcfjvIoLw8FMAB2Fu-TBJCLdXSg799t7-NEsMZAT1OzE4GMkNfB0oVtqGnGGGngD4cqPASusoy3AY8qvKFjr1uauxKl_NltQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrMhBccU2SiCdjmaUs2opp1bpd1crOXjYF6fjBkCgzMfWfzMRPaENexkLo7jc8DX8nyAkHV4eDpK-R53at79hY1UisKGVvW-K65zSTMCOhR3OyOh7WSmY4KO16Ow1Hygf7vjnpA5_jTZu0_bOgEiWjN50YbJHe1IUQmFrgxOXpgSqIF2AQAGVlpUT8FjAz95ydnFNY1SfkQp466OLgsHMTN7o4JF-gJTlpaRuBVRwtUuV6uO0gLU6Fm5n0zOjPkKej0KCgGl9dEoIsJJrgtIX4qO0tkWs1lzVHGhjKNaOkbkkSuatshrDtIcmZaW3ciuHvh-xLdGzRdPMqu8TiKMCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=N9DPQijXbbVijiQwmdo8uAuR9vTz-zWR49MeaWaUVUHIOLX7KLt1lf9KnRyOh1LVhlRp38tTOQGlU9FcREtscIPHU_9fjKVEcr_vJdqZsrfGmIPz0vir0XK8XIJWcabRgE7yDBRADV071ANL1Hk94lKt8L1MP3HO2mCxfvK0aBacNhgcXtwdZZiEbYFJ86wg68fsIjBbNjheNy0xlY3bZ6xBXGjRVT0f-Y1wLNuwgroOKcKKlaPZoUZu-RRyfDMEqCTk0QP8rMr6yn618AuhV-dzqudt2RrXQ7UoFilCD74TH95rX_0csW3oHRoTUSDdSpCApLm8SohvJFqsu4oEAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=N9DPQijXbbVijiQwmdo8uAuR9vTz-zWR49MeaWaUVUHIOLX7KLt1lf9KnRyOh1LVhlRp38tTOQGlU9FcREtscIPHU_9fjKVEcr_vJdqZsrfGmIPz0vir0XK8XIJWcabRgE7yDBRADV071ANL1Hk94lKt8L1MP3HO2mCxfvK0aBacNhgcXtwdZZiEbYFJ86wg68fsIjBbNjheNy0xlY3bZ6xBXGjRVT0f-Y1wLNuwgroOKcKKlaPZoUZu-RRyfDMEqCTk0QP8rMr6yn618AuhV-dzqudt2RrXQ7UoFilCD74TH95rX_0csW3oHRoTUSDdSpCApLm8SohvJFqsu4oEAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=UoyLNoftTkHorCGtU_B14y_GRu6s0otWdKeayP66KoBv8GN4wi_H0IERRkSUMF2QCDZBgNKv9xmgWobJMBQmkUym9yy7zQmvdM7RaYWd4pM0M3cNYRZOC_VZpJvv-r_CYawVA3iQbkEo_R7uYB4Whb_IsmszVgkZUt5I6z8P0eWdVEVf5_p3cWXsOa57_REbQZxlAXoMhGV-RXwZH1urDP3p5OoGu3XKC4jFRKotoqTRIgjVOZhsm_sviUAw98gKsNAxL002TIHOuPfGtEsZ_L8zEjVaNZgzJQHqWUOUZ46Ta8QDXgjzngWzN1oAI4OzGiWfUaNuN_KmJxqD52teYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=UoyLNoftTkHorCGtU_B14y_GRu6s0otWdKeayP66KoBv8GN4wi_H0IERRkSUMF2QCDZBgNKv9xmgWobJMBQmkUym9yy7zQmvdM7RaYWd4pM0M3cNYRZOC_VZpJvv-r_CYawVA3iQbkEo_R7uYB4Whb_IsmszVgkZUt5I6z8P0eWdVEVf5_p3cWXsOa57_REbQZxlAXoMhGV-RXwZH1urDP3p5OoGu3XKC4jFRKotoqTRIgjVOZhsm_sviUAw98gKsNAxL002TIHOuPfGtEsZ_L8zEjVaNZgzJQHqWUOUZ46Ta8QDXgjzngWzN1oAI4OzGiWfUaNuN_KmJxqD52teYzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FULRJvIG_ZoH5VVbcUuWk70gaSv4D11br9kIlRo7vDajW3sKPXOBdj5F6Bg3sADBqqTuJc1YLg4Dh6c0CDrMfFeRkJdvnkh0-EaBOJcsdCvuDNi5_AdtDfuXXKJpQJ-GLqdcq9FNvM9-OBR5gRBhj7mQcyTfYYdHQ1TuHB6Y_9CV-2RekHQ1U_WrLBWp9HD6Xuwf3PsZYISwwjIPfZRlDqqzvJ6557Rh8goBSHbfsLUZfx_ALp0RWHrmqzCozZJay8sDjfv2K2e_2Ll1Ekk06gUE8B_Ks_gMuBC00Gc5h2qQz4YUvn-03sQZTfzAcDN_DVbE5gUCHDfQhERcmMwCHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tmoww8dgN_AhFDWz0DNPswEtg-V_AYgwxJrjdyzJv8myOZh5-vZ2hK4_OpYrnAorUQzQ0ygqxp9dUmQlneDyop2ODj_BRP7xsea-noKw89iuQCNnJLdM-s_ssAzdHZSkFsn6TXwBLxJtjfIGI-b7dnGA3kZceF4GEzEBhCCe0EP8X2Y2CuRV1tk3PzrIFp5sOHJSwL1Cvg1UKv5G-P0jUckJgkQKMGVxXT-N34UZ9IrpdLGWMYDVqbMvj_7ByivL1Rprnp842osy55OMQwvRG_ZVY2KMMrVw6MK7see3xWPFg_j_ReThE7ljjukGZbDDM523Yr9txp6QteA2v_U0SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GU6PDp1_LKPhMP-PWLNlAd4W3wVeteY6X1-SQf_fthS1R9SBVvj2Lc4PbF78mdijY06WiV2PMtOfo2jvl6by7j5PBNearG1QgrBiNbUrBIZrFtrLrTUt2OhsGo5xtv9b4hZUao-1sc5Ys-PLvkukb9nZF3eUZ-pUaqyAoFBIndtgJ6DUcLm_KE3Hc55xL6xorKNtyXizJgEbw6X6YtTeW-AXGm1Q8Q5LeszS8hXDW7EC0cGS3mz5d3RGVjHG5V60goccIvQbMisZMkuI5HznXIOovTHBR2kRJycEzizoWbPUX0amsRLijATuGoHXTjrm5J6SRoEErdr6cD00gWBUBw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=vdAcI5NmQ_lntLwoqgUbr-O4zpx5LKs7ba16JoKK16c1GJ5KlbSWgtt7mg8Z5thXZ10tsLGM3JS81kr1YDPAudtfKOjcWj1LMB5eT_tgOK-N5Aq1RuRo_D2QlYs-btXxrBZRdvjS_x2Fs4ou1zTi5VfgpdR3YgUQZIDxwaEbKQv1uU3jrrnfUeA1f_BdjAtJ6Po7ANsf5E0ldS2fDBtkeA-eBLdPSA4mLNAjfYECxj6yA9kmk1QZ24GHtqyXwmzsHCnRnZYTbHYfQvErdgWXJPgKjUAm7IDlhb4vPNDtNtew-XLwKBLbbtA_WpyR1zU87z1IuWogew7tef9CjAgAnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=vdAcI5NmQ_lntLwoqgUbr-O4zpx5LKs7ba16JoKK16c1GJ5KlbSWgtt7mg8Z5thXZ10tsLGM3JS81kr1YDPAudtfKOjcWj1LMB5eT_tgOK-N5Aq1RuRo_D2QlYs-btXxrBZRdvjS_x2Fs4ou1zTi5VfgpdR3YgUQZIDxwaEbKQv1uU3jrrnfUeA1f_BdjAtJ6Po7ANsf5E0ldS2fDBtkeA-eBLdPSA4mLNAjfYECxj6yA9kmk1QZ24GHtqyXwmzsHCnRnZYTbHYfQvErdgWXJPgKjUAm7IDlhb4vPNDtNtew-XLwKBLbbtA_WpyR1zU87z1IuWogew7tef9CjAgAnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaR5B3CpCJI8t28LLD-0aQgYvJ2ILPN5gmYo7_0mNZfJq4g0bMwoupVnov74BMjkoHqnrgJm6A0fLrkE9ydrUaqh_G_ERbJG0MEhls5ubMU1SaLsNL36vNl4VWncL2QXsCq3K0EcsftWHsxoE45M71dnNzGhYiHWQJXbZSY92nQVGcgNEu-W50RuUTYc90ehQGIb-IjKKXDNDZxZ8zuo41ukq914l3ftlQRjb2zJkIwVakSYDOLCUddl733JRI3DkhhgpmIFVgLh0X9XjJytulT1MZnY_5uzKNlBIVehjdTl5s66Tgwif-PTusKhtCQLJH6MaAoqM3Xo7LClB2Y0NcGE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaR5B3CpCJI8t28LLD-0aQgYvJ2ILPN5gmYo7_0mNZfJq4g0bMwoupVnov74BMjkoHqnrgJm6A0fLrkE9ydrUaqh_G_ERbJG0MEhls5ubMU1SaLsNL36vNl4VWncL2QXsCq3K0EcsftWHsxoE45M71dnNzGhYiHWQJXbZSY92nQVGcgNEu-W50RuUTYc90ehQGIb-IjKKXDNDZxZ8zuo41ukq914l3ftlQRjb2zJkIwVakSYDOLCUddl733JRI3DkhhgpmIFVgLh0X9XjJytulT1MZnY_5uzKNlBIVehjdTl5s66Tgwif-PTusKhtCQLJH6MaAoqM3Xo7LClB2Y0NcGE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=s4t5kFSemc5ojCvcvItF-SpnntSNBtQK-8YVZ6-ahDl6D1BqOqoZ7KybGxGosgwKBpMETzy1mcz9TyzNT7WNylQWKEIA5k_Wv-MueJAdEHeaIZDMvLqmSqbjfc5LoauV4egoOkO8LsVErktT1h1bdXv47if73Fd7Wzsi63tjoWngUgzZnrzCVZ8ysQ_WQKJ01I5LwBxjYpCk4HseIBD6tH_c9AWbqQ2JKsn3hG7qsu_UHAMY1j-aYrltsabs7kT-VFNMwR7g_MQhXgJjSlv6XkAkOZLHAwhdL5m0beEm2mUtHMSetySbt6OufOn5VcYg97BKyQcV7cMYLy5TeMhZ4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=s4t5kFSemc5ojCvcvItF-SpnntSNBtQK-8YVZ6-ahDl6D1BqOqoZ7KybGxGosgwKBpMETzy1mcz9TyzNT7WNylQWKEIA5k_Wv-MueJAdEHeaIZDMvLqmSqbjfc5LoauV4egoOkO8LsVErktT1h1bdXv47if73Fd7Wzsi63tjoWngUgzZnrzCVZ8ysQ_WQKJ01I5LwBxjYpCk4HseIBD6tH_c9AWbqQ2JKsn3hG7qsu_UHAMY1j-aYrltsabs7kT-VFNMwR7g_MQhXgJjSlv6XkAkOZLHAwhdL5m0beEm2mUtHMSetySbt6OufOn5VcYg97BKyQcV7cMYLy5TeMhZ4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
