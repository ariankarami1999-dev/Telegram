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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 01:23:25</div>
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
<div class="tg-footer">👁️ 6.71K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8TmlUukgx1CEMxrplBrST7mcORmueW5TPxmvJyYIx1gXuGnjch6i_jSD6dxQA9wNntu2S2uOLXXgZnMEc_5MsPr2YVuuR5OPlbKMSGK7xmig-nu01nyG8d6GkeyzUxn4tckbpN7A-DKWeZjdRctdIIw0vkX9V69l6raE4_Oinyql337INXK4g2riy7f-GFsi6GF3lhGhIcrg4xvRS6XWe1WuRul9AhWMl13Wrin5WVHXwbzwSxrMa9nxYPEhZaenXITHHcr7OmRGUHDdKQ7THRh37vPrCn9oMKyyrGIcOhk-lU7twZS7Bx-MskFFy87mKoeN8ggtc9CNGde889kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBMwbuDlkTH1ICqMfi3of8VOPccA1m5719MTJPLRX5IWYQYOGAhtOk0S2RpUzpw4nJyh_rbxNSQjKH7Pp55fkhW_vigDjJOMO5R0_OEUYxi3uFkkG0_q5kIK7RZxQnyBnVt6Ab2h66OJphED3dYfmREQwCjp4UmTON3CM-nSgCap2LdBJgz3sKAwc8aWKu58PeoB-h3HKQoPj908Yc8ftHJYB1cWk3BLNFWhYvy-F0mp4yMnKFuag3xcxLGowmVKRyVqdYjVR1-1-cTUFJfOxUw9kGlTE9EJ1Layfn8RmTO4nD7jMdiR5utbdhWwHMIkcItZEZ9YlCctbr_X3gjsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7K2NzuFpbqEjfSswrlJnKnB0cUzt29lx43HuBgJRQ65Avb6ovfrZIxby0X2lFxzj8OOBrBsPbbx8CUmGYgevHCj7JzmcB_r7ijfj_VhodcCH6ghgVOM_zOAQAhP0Zj3NfX1FcXg_5p5PxmHggaiqWrP6YLgN2WPNLic9D6wccaafPz3lzA8U7mvNFrko5n1drZ2xewONmiHFCxm_QEBpJLwMN6ee7JxNLIHP04T8iSIIJY1ujhSTWbhGaHt9yNlsn9gnMMhQtRr_5VbRhcX57WP6jBx5e3fK40bX2VGLVJl_JWpt8r4GKXHt6DaMW6OEKRAajoteX4SfQ58Wq-ahw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_cpzkdtWsBsjYm0qKx2DYvBozVNyCMcPawanpF_2DA3mhXVCFQvbbHnWcEGKrHQeXxKpyiuVhHjiSECHmzmDoZbC_mJCon4Hpr6RWoPNshiHiE9XWAoy2-WsQW5xgRaFFUa66wEjZB82TR800cCuTiQqmlYXZz9-9wk3kDOS7yQgIlSU1VgzxOr59tQ7omizi2zSr7pK4vhpJfLpSfGTq3J4XrOB4CsLKNSvqG9nEGv94KBstt_0pUnXVeM8sfdKpasTiAKgfwPAQ0B-5xQVwMG2NLOe9s-CIwW9vm1SuH2qaw6a7pJazluOGwR0nOMT09fVYwvez9gUCC4EUW1Kg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSEaXrBzC-PrBR8UICXmSM3EneavnKGjngvK7YslkqdvwhoSo5n5OZe8jvczqy8Qi1Ol6iftGIi3Q6EkJa2eP61T2Zq8zAHzxQTKm69zah_X1Pi1tQagDGVk2mnrlbJNvgS-SmLw65uCijZMwGFoBiCFhO5T0WWeqmuFPYzKIvEIQ1uN9oSPZuB9Zl1WUkEhSI2o709Qkl1NTdOA1s-xtMhZ8fEN3PwMjwi9cpzy_fItf66ATFcUk8_37uY1gwH5cov6AtDS6Ei-szlZsZMrYrK4NlDXdLRldASaIKy00RuusFmggGMcmUnwqbLRrfd--dStaQwq-mcnx-KHwOEiUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=GJx5GE4ReHBTlwy8Kc5RxeZlqd9HTfG-NM7x5SXokUixJ3gJquL17JVcCnjgyA_ndzR5EYROdin6fR1CEGHtCTdb7NNvrUTW-y3QyCszCmKgapJ1V4UDPFUNMnqfgx2StJNeUE2Fsp0UEQYwJszeB5kqYwlcejGTWPvpwc4v2w9_J047-iKuJeKpZePYHE1vEKDqSwZ-YjQCS5sbCe7N7BcpjBCLcKuA2YEtKFm14JM2ARvOX-sZOVPQO8YXTuiTCk2pAl6pIjr4z9feX2R4Vhhx5Gimc7xExkzp6vIcP7cXoVk0GICF-uR_UcItLL0vvtmoqF3HL6c71OefCkXQZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=GJx5GE4ReHBTlwy8Kc5RxeZlqd9HTfG-NM7x5SXokUixJ3gJquL17JVcCnjgyA_ndzR5EYROdin6fR1CEGHtCTdb7NNvrUTW-y3QyCszCmKgapJ1V4UDPFUNMnqfgx2StJNeUE2Fsp0UEQYwJszeB5kqYwlcejGTWPvpwc4v2w9_J047-iKuJeKpZePYHE1vEKDqSwZ-YjQCS5sbCe7N7BcpjBCLcKuA2YEtKFm14JM2ARvOX-sZOVPQO8YXTuiTCk2pAl6pIjr4z9feX2R4Vhhx5Gimc7xExkzp6vIcP7cXoVk0GICF-uR_UcItLL0vvtmoqF3HL6c71OefCkXQZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=GMq2GIyplGJljNt1qtSNjOdQe8BZgqI0egK_ItAnDRuShwQiMAl5VT3WaQDXOulxt3wVgqkm_5zkh9L9lPWthzoJMrv8RQC344WseWIg72gieRyC4ihu_L0_adUz0sYxCmd_1ALWfU6e8e1k_7zNBW5O-l3tmZOsrHM9ZYZb_jsXpkNYYKaQ7NKzAj-0yjx3JWDJz7PwoOVXah4i9OATl4oAYnXd__jKgQFzTsyzDsadiOa1fG67Is_e1kCZNg-Tv2LaHYwePQ3oO8sqaEyC3aO_FlJp5Zjm7_ny1zXDY2zBpZ6oY1Lt1s80k6U23iDXHylNy_iRfvPNB3ODNnOYow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=GMq2GIyplGJljNt1qtSNjOdQe8BZgqI0egK_ItAnDRuShwQiMAl5VT3WaQDXOulxt3wVgqkm_5zkh9L9lPWthzoJMrv8RQC344WseWIg72gieRyC4ihu_L0_adUz0sYxCmd_1ALWfU6e8e1k_7zNBW5O-l3tmZOsrHM9ZYZb_jsXpkNYYKaQ7NKzAj-0yjx3JWDJz7PwoOVXah4i9OATl4oAYnXd__jKgQFzTsyzDsadiOa1fG67Is_e1kCZNg-Tv2LaHYwePQ3oO8sqaEyC3aO_FlJp5Zjm7_ny1zXDY2zBpZ6oY1Lt1s80k6U23iDXHylNy_iRfvPNB3ODNnOYow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=dKuHtYTi_p1T-U96VHU3eP0I_fFwjcgedqHKEqoJxjhx34kMPKZ5HjUqWS65KZoNjJY3ehDDDG4lZXtpsE1U3rFTJRSEplYi3GCe7XrBjbZ3FWUjKo-_xk1PZnqmILHEHO5DowbdUb5WZ1kdeooK8IsDsec0NrQryvWLXfPrbErj3sOAFdPDiJmlHHqjmJmvtRbT4dMqrVwlWXaLTozY8-PcY08JTkbqj844rrEzr3meJEDwA0iUfDTJZRHq3XtHOFyffmR5NKNMk-QagqLh4_8e4BAg7sTZGEaKiLzBhlqkGNq-5V6bk6zQwDUoX0ftdX4VRV1VM_k1pxbjMUko_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=dKuHtYTi_p1T-U96VHU3eP0I_fFwjcgedqHKEqoJxjhx34kMPKZ5HjUqWS65KZoNjJY3ehDDDG4lZXtpsE1U3rFTJRSEplYi3GCe7XrBjbZ3FWUjKo-_xk1PZnqmILHEHO5DowbdUb5WZ1kdeooK8IsDsec0NrQryvWLXfPrbErj3sOAFdPDiJmlHHqjmJmvtRbT4dMqrVwlWXaLTozY8-PcY08JTkbqj844rrEzr3meJEDwA0iUfDTJZRHq3XtHOFyffmR5NKNMk-QagqLh4_8e4BAg7sTZGEaKiLzBhlqkGNq-5V6bk6zQwDUoX0ftdX4VRV1VM_k1pxbjMUko_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=an4EKw_XIQ41-5uvPlFAcYiKg8zG3q-Y75YThAzAPzrhdLCxDzM8Xu0BVFVwhSxQn7IxmHNMtFYv8f8PDLoTDZW4Ew-Nnv-28-0NSE1e7CdHz46eK40-LwBoKoGcJoAXJ_ITw236esDEDqn7xuHOPn8zZRspDR8g7JnCd-1uBdqMveiMJKxdO8foQPfmIpia6txOoXuUL262daYLwseHrlyY4x8aALEfBzcmTIEWstW2VAGe_l629gO71nPN46awF9FUFlBlte8YeRu-rIxwAQT463BjQ9JT8CADOcXfkXARg6b1S5sJjZO4RifVpr5PKur85K1rZcJMwL3HB3WBMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=an4EKw_XIQ41-5uvPlFAcYiKg8zG3q-Y75YThAzAPzrhdLCxDzM8Xu0BVFVwhSxQn7IxmHNMtFYv8f8PDLoTDZW4Ew-Nnv-28-0NSE1e7CdHz46eK40-LwBoKoGcJoAXJ_ITw236esDEDqn7xuHOPn8zZRspDR8g7JnCd-1uBdqMveiMJKxdO8foQPfmIpia6txOoXuUL262daYLwseHrlyY4x8aALEfBzcmTIEWstW2VAGe_l629gO71nPN46awF9FUFlBlte8YeRu-rIxwAQT463BjQ9JT8CADOcXfkXARg6b1S5sJjZO4RifVpr5PKur85K1rZcJMwL3HB3WBMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=qHoU_QWQcYi3X7gdbsu8QpY7zpl40lWcMux6v1TmboDxc85ijN7i1nazJEAXbUKcgobrIxj3GktFpaWBjBQYqFh86am7q6KunLzGK7xR6dW5SgjVATK_tIGJEIdmA2VidTGwPHG3NcIF70Yq1VhWNm_nMw8NEOChu8ucwoAmaxCIZmXGTlAHgl3TQKjIEK-w7DNxpUZIXHZVQB5R0BVEfmi9JSsCbSUPpXHa71o97Xk63DjRLtfPvpxTDTAo-szVey-Tyxo2HDwQDT9mP3wFyU6km1-NYR4IZEpNsGgm1M4hN2xo13ckLTMNsJnhVw2j-n7TvDCDJ-97Gr1DnlsIwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=qHoU_QWQcYi3X7gdbsu8QpY7zpl40lWcMux6v1TmboDxc85ijN7i1nazJEAXbUKcgobrIxj3GktFpaWBjBQYqFh86am7q6KunLzGK7xR6dW5SgjVATK_tIGJEIdmA2VidTGwPHG3NcIF70Yq1VhWNm_nMw8NEOChu8ucwoAmaxCIZmXGTlAHgl3TQKjIEK-w7DNxpUZIXHZVQB5R0BVEfmi9JSsCbSUPpXHa71o97Xk63DjRLtfPvpxTDTAo-szVey-Tyxo2HDwQDT9mP3wFyU6km1-NYR4IZEpNsGgm1M4hN2xo13ckLTMNsJnhVw2j-n7TvDCDJ-97Gr1DnlsIwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RkQrmtKP_Xk7mx3cfDZoG_UP3vQrglb_zX1XcUHMLTg9vKMUIe6J3Zb9UXNZINL9lZhT9hbBFMglGdMOv10ADXEnTwHLnbo67VTDIG8ctI3MadixvKGXhtvE0kcGEaOI4WDRDmgII1EDzGDPc7YjevpKqLxd_6paBoX0J7-O0SwW9mHewiI0a9MqowJlF4eKFoi6j6Xq2Q8Rkie9tdLZeu2mZEHUTsBeXBUDVcuYBYOMY2h3ijoyT3FnW2Y5XY_dyKccLQPzMO4_9buzPNvtJiErQVQMVi4pEX488XjrvmWradZd11geGAz0IP0ZX1EvJP2FczO4VV-URDRsU7CGsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vCZLA3u73G1NxtulaI_0SSD4WC7mjJy_C9bhIwVJiyRPxp8OZvdTq_rq5ngmoBckpJu8eZm-FHcTjSzwMcbYKRoGI3rz0Jqf0w72z21TKZRcokxGAEBaj6v8C73vd28tTAbMHffKFf1ryf7_TFt09tkQXXs_ansA_VVcDZoELg9gyRxd2bjXOl2ZdCDsdPPBkXF0KrrGAR4fa10rzjaDq0ETlTvIZvgl7DbnTzzsld6oZuYwxJxOlbNYxoxvuXr524LAGkZ09U9vfEyCaMuhJXHqT13QHJbwJdZ0a7qIjYgShYpL2xxjkTK9iC5lNRANP97kSGpoXNwaMOO_5N-GRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPM5fP6haneHqJ48HYirYOWSrau1CtQe40OuiSZZvZyLTiHdUfX2cBdnpZbrkbSNBekszcGEpwyeeabcXboKGK9oSXQ4WU1hrmmNprAUOi-98R54SPJuHVY5gOuHkL9Pa-PQXbAFlnqrhnT0JLth3L2pZu2iOO7J5awm4GmkLNBuLOwdzN7BU7XCxvqjkwfVA0A-pufTVCYJmHqJD9DDT0I5LivJIt9SvUjA6dr6VH2CJ4kD4iVvK7OkMcT7572GulBUlSsIWXtzGnw5wLofHGdEr3rNBmPqI6I4H-nWUF4qQUKl-J0YeVVCozq8B1THiWHdOCXex7UI4eNG61EgFA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H1A4PvfFRYT-ILEoiGIV4Ou4c9WOGxpeCw4AdIu4sYdoZvj7XPrDfPz7g1w7cvsbNdSIjs5t4uaiOD6TmdT66wDvQJF6UMvEdyhCiQYUqIlbbc5-B5sk_9Sej634QvygSMPVuPfufnS2cJGkR1bDpIc-mvdxLZ6xsx1s-EyVlSb57ghXv8EWEKcqtRkCovqOi84D52K-mWR7mRjNgAbtf7kz7WxJaGfljjSsSb__iNHLha7qxO2cKhN-_ObwmXGJ8nwibia76_axyyPaK2DthKNPKpZDlW8r1YJ044O0qwC1bd1VOVp59tauNlUq96gTaXX5M-OUIkn33SC6n6G4nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LZqN4WGobsjXA075atT71iRXBLbagcC-wOl0JrUVtCAam0CsNXVADCjSMkOw6iu_1MsWSYvUA9LvJHbJpc8hI8eGIJjgi1MDEAF_MXj2UcGRgLE3NZSbMwE3Frbph2-AEMO2AbybZx8O1127A4ZEWtZWLr-RkPGyMe9XHCPLiuF0cJdpYFySUHxwh8PMF78iAo5H-Z1ZFzMrPk9XJemxtG98es5sN28MYRxdnz4gEoDVnG5WF0tDkpvzxhfELOLaFOLncw1exn_kL9J1XFdk1jRnJouIZ8c02KJZmYB2s_PsszE8y4CQ7nvdFV-f9cmHztBbCw_qrckPY4rRMlrQ1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A96DAc3geotK1RKgFkPIOlNX48Il2IjFw2soQSDebk6WYyy7LU5ulkOfVCC6pIMwzRq1wIWCk9AMvv_FIJ6r1JJGHCjgfPpvuEPu5PNRe7rdR_swIr9txVkzaanhVAlKw6mfyy9vN9PIrZMdJrO9xagYpqfHw___fEwa7_q46GXMZe9aY-POPrpclBESGcfNP-gQmmt2_UDm5h6A1WoKe_JBQU98CzQ8we8V2VgryvV0OtPsxhUfjSThfI_Lqge59Q3pMyFBj1PXjg8MItQYFK_tku9AF0idxWrJgRNbujy-GxnodJXWqlBh1FNVBdvZhYYt8Kk40039wxOsB-PdOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irew_ToCxgOhqCV5EO6GAFgeHoW6P6iFSxOBHiTO7KCrchOQ4fZHzuSx6Dq8hSFO6yLQgFwa3NO4BFeVFbkvvpDZ6wiJfKj2fu_vV-OaBFS9GxQJIGQO7ZYFG37IAvhWvsRp3DnbhxrZev4NlO9KEY0cjWntCDlPEXYpf_V40gmzFa5LraxiopRb7JpN-0rU-3uTDg6Y11tfJjH851r3SBQuoeaR5gW5Q6FYCn1q8SXGXcqq8TuerrdWhfMyD9gcfok2td_UDbtEYYpQPlBsAPCvuQirLYASMq0Yv4AWc-JpY2jJxMHWHYrn1s68-fIzrTvi_1jVgO41CPlZNeF-Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONkD9JFf16jFnEBFcP99H4-ozGxjbb8xuBBV7ukRZJJIMXa5vJ3kUxFIUVvNYm7eurSBKoG4HliuV2kWb_38DQofPUcARLoLSNGnTbvmnUlL9htjBdAZ52xko0CGkx9jJfK8UXZ22VAsvbAlZLbOlp_z09GaOowpIJIJEDh-KiuyFKGJ99HtyWP7JdnDLFVNKbyeeSUufwfsbib375CNNpQz2TaUkYnKPubbHTCAN-XxzH4C26NmsQKHyqEUZDCIhbldocSbCF6qbZcYz-8guRH3ushYQr_a8q2rQMnrW0WNkzDCmeKsKhhXYtDalzeIR32P3UQXckVcsysjLGobow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWIe10gcrBCg_bpJHrzv5WSlisYazuXcwJ0OBfZT-BO1xoaz0ErBs37yXXt-hOplfUFPAI3vu35ttvHLChGVlj1r30Z-bPnIIgzfP6KzQrFB8vBCxGKz3KwmcV32EUQCrPXnoZ6oUFwJp8ToAgIHVDxJg4CFjgbCtMLyXGi1g06pUSpd5H39SWzG-y8l-V2CkCq9_lr-YyVrjmrM5TkJz-bA5uVDQf-H7h9ght2gs1nZpoOv6AQP6jE0MTsbcfyzSCJfHjdC0QZlWovANJ7ub7GpqZBo-VoVrtyCXKdRPL9-cAgB7mq2ptAnkIjbglEaHMun5zIoTgVssX3IasWjfw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=OYUzFhi53tqgMZWDGJqu3cdXvHQndCLCS91Q5oU79N_SwTAuxR0Sf9PUWCGvR6Y_5ixFLjGesnRIIFsnvkd8VreXOPm2_H7u0QFbjIVi_y78AcIQW1ltTqyMFUcTI2Q3A3Yo9XOwAfQbb7oSN1oW2nV1N7LtBYlZ2frlhGPMefB7QWCSy62O-9esCfQOs24-398FbnTogQlCnjk5qXMwwFWFY4k_KvJz1Yr1O_7djdlRRImmAqWXSWDU4pYzE2XwBninZdR5YObaM_pKULX5SdewYsfnjayvfGA4-D_RuDuVVPDFXxgx59YAVRa8FDxGM4VtSos899DXeDEtHL8S5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=OYUzFhi53tqgMZWDGJqu3cdXvHQndCLCS91Q5oU79N_SwTAuxR0Sf9PUWCGvR6Y_5ixFLjGesnRIIFsnvkd8VreXOPm2_H7u0QFbjIVi_y78AcIQW1ltTqyMFUcTI2Q3A3Yo9XOwAfQbb7oSN1oW2nV1N7LtBYlZ2frlhGPMefB7QWCSy62O-9esCfQOs24-398FbnTogQlCnjk5qXMwwFWFY4k_KvJz1Yr1O_7djdlRRImmAqWXSWDU4pYzE2XwBninZdR5YObaM_pKULX5SdewYsfnjayvfGA4-D_RuDuVVPDFXxgx59YAVRa8FDxGM4VtSos899DXeDEtHL8S5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=XAb_ydGXWPX_uAnIjw_ehtXYp8L2mkWAXkhUvCSW1-2gW6vG-_y_9J8nThuiaABMoqg8FKo5TOyyOPLCQczlxC-tiYadKB78nMByGcH94nPXypN8V3A1OXM9Af85rZPQh6NVGhzvgXaK35tGynstCH-DcvZb-yh-k9a0pERofwnty49c68Sz3gyWBhhN58CJLyHJAOwM0X3iy-skHt4qAw51-3yAoeBxfDICbzPvBmSJ6lL2DCBF9Oyjk8sqCSaDHwdLI86amAfeXZ-4uisZ6UIl3XJQ8ERnEUA42uU70vBuZr_vK5qMIBMahmajPNbZssUkGBfFDMINziwQUu7Zrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=XAb_ydGXWPX_uAnIjw_ehtXYp8L2mkWAXkhUvCSW1-2gW6vG-_y_9J8nThuiaABMoqg8FKo5TOyyOPLCQczlxC-tiYadKB78nMByGcH94nPXypN8V3A1OXM9Af85rZPQh6NVGhzvgXaK35tGynstCH-DcvZb-yh-k9a0pERofwnty49c68Sz3gyWBhhN58CJLyHJAOwM0X3iy-skHt4qAw51-3yAoeBxfDICbzPvBmSJ6lL2DCBF9Oyjk8sqCSaDHwdLI86amAfeXZ-4uisZ6UIl3XJQ8ERnEUA42uU70vBuZr_vK5qMIBMahmajPNbZssUkGBfFDMINziwQUu7Zrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=iDYAlIHrxkQNBlC8BmUsMUj_2vjMEHr3F2xO9wLEh6Yk5O6lKXE3Bi1Qiq1h0KgxOG-tH3q6Nb80_hIRHcFXlxBJXzHpCI17qLOnWOd83PD2jHsU30fAjIZZgHsBZ1KXoncA5JlH1kqmbUfekpttpvyN8yd8eq2HE3351urD0RGSNALndlnKMHudKb4_fuNKU_N1KVaNbKIaVe7aL48lkCNFYAUi-KvH8AaeaYwrVxx8CBAJqF1Gv6A9O6ZKTxwHD2zQrKfTRQtSc-WI3Akvxg03mtkb_AI5NQl4i062D47yqk9iJwaWmKAsu62RBXMNOeiNA_6LbhtMAakGzI7cag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=iDYAlIHrxkQNBlC8BmUsMUj_2vjMEHr3F2xO9wLEh6Yk5O6lKXE3Bi1Qiq1h0KgxOG-tH3q6Nb80_hIRHcFXlxBJXzHpCI17qLOnWOd83PD2jHsU30fAjIZZgHsBZ1KXoncA5JlH1kqmbUfekpttpvyN8yd8eq2HE3351urD0RGSNALndlnKMHudKb4_fuNKU_N1KVaNbKIaVe7aL48lkCNFYAUi-KvH8AaeaYwrVxx8CBAJqF1Gv6A9O6ZKTxwHD2zQrKfTRQtSc-WI3Akvxg03mtkb_AI5NQl4i062D47yqk9iJwaWmKAsu62RBXMNOeiNA_6LbhtMAakGzI7cag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=RXJsG9XmZO_WwPS8N1L_Wyaplu6T_DDqrs9a21idqJQkZjE8JtJK41p5C_AIV10pLp0OWmlVxkWSZlz1XELIUaq59j4YpiHPIk8qb7a_-xHN3XRBHhUJqTp0vUaxkEWtQW5upifnGbQKtavk1Ejoz7qB__zjuJtdr6k8dWdE1rUlb51jtduPQIwd0pZ8BWowiCYL3_W0IuTLautr1RZMw_fQQRLtdSnZVy9ey_cfRyQ2FoYJMWeUkSAhvKBUyLUdQ__R_Kk7sVv7QuR0Twh0WvR_gZprMgOefy2rR2JmX7FoKWrwAgtpM-kCCTh-UHOKZnzpf160Lyjq0pAZE02-4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=RXJsG9XmZO_WwPS8N1L_Wyaplu6T_DDqrs9a21idqJQkZjE8JtJK41p5C_AIV10pLp0OWmlVxkWSZlz1XELIUaq59j4YpiHPIk8qb7a_-xHN3XRBHhUJqTp0vUaxkEWtQW5upifnGbQKtavk1Ejoz7qB__zjuJtdr6k8dWdE1rUlb51jtduPQIwd0pZ8BWowiCYL3_W0IuTLautr1RZMw_fQQRLtdSnZVy9ey_cfRyQ2FoYJMWeUkSAhvKBUyLUdQ__R_Kk7sVv7QuR0Twh0WvR_gZprMgOefy2rR2JmX7FoKWrwAgtpM-kCCTh-UHOKZnzpf160Lyjq0pAZE02-4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=Cou90tSuEw8eA4lTEKCuFndYoNOqwlPv6xfpqZdXO9AWb97OctEJKKJQ8WLeoT24EPi1eHL4aQN5ZWE7yKPwpmdxDUannJlcWVTAs3IeJ69us75wrUzIhBCK-l_p1_6GXS09W7_mUBg7q-r3KU5lHoBkVMndp0wN1iYaw2oMz_zaFrz_4OwbORyeBNPvNhIT3rh7yBtFMEysDWz8JfrYzBiIL16xi2tJdQhH9ohUr5uQRLZpAI_ndmblB1Tninpjw2vHPNReyU3M39-Raz3baI8NYBsIyq20DuJv-Zz-sKAb8AOFi0L-Qg_GBW2LLNgKJfoYXKYLLehSV1dzAXWO5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=Cou90tSuEw8eA4lTEKCuFndYoNOqwlPv6xfpqZdXO9AWb97OctEJKKJQ8WLeoT24EPi1eHL4aQN5ZWE7yKPwpmdxDUannJlcWVTAs3IeJ69us75wrUzIhBCK-l_p1_6GXS09W7_mUBg7q-r3KU5lHoBkVMndp0wN1iYaw2oMz_zaFrz_4OwbORyeBNPvNhIT3rh7yBtFMEysDWz8JfrYzBiIL16xi2tJdQhH9ohUr5uQRLZpAI_ndmblB1Tninpjw2vHPNReyU3M39-Raz3baI8NYBsIyq20DuJv-Zz-sKAb8AOFi0L-Qg_GBW2LLNgKJfoYXKYLLehSV1dzAXWO5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=KTfCOfO-BwwkEGugHVDqdBtOs-FbPUdKQDZT0-g1ys6S-6iiUoGKVFz-m-LdnbUiTrMddOYUr5dTWodXrjnPk8ISvV4ZMWvGNI1NeijH8-a3LlO8KriAfMdFGTlXsWyhQMtuigJlskYmEq8fXj90bvE3hb4h_DpHj-NkZMo9z-tnJjZQGkvzT4VB1zlfL4_YWr5ZMfDfcWdE5gb6j1IgM9be3Craa24SgeMWyRw9AI3ApceIGll4EGMiAjoqtLgcoEMWFcDH_76idPo12rNo4CqEQ5QG3Qrd2vplgZnG7seB8yjHSIW895tU-EZ7wSWJ-ypb2p7KT9yf5emzJfSpfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=KTfCOfO-BwwkEGugHVDqdBtOs-FbPUdKQDZT0-g1ys6S-6iiUoGKVFz-m-LdnbUiTrMddOYUr5dTWodXrjnPk8ISvV4ZMWvGNI1NeijH8-a3LlO8KriAfMdFGTlXsWyhQMtuigJlskYmEq8fXj90bvE3hb4h_DpHj-NkZMo9z-tnJjZQGkvzT4VB1zlfL4_YWr5ZMfDfcWdE5gb6j1IgM9be3Craa24SgeMWyRw9AI3ApceIGll4EGMiAjoqtLgcoEMWFcDH_76idPo12rNo4CqEQ5QG3Qrd2vplgZnG7seB8yjHSIW895tU-EZ7wSWJ-ypb2p7KT9yf5emzJfSpfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-Gkdzy9xq8CxteFN3ZT7NQzKVUiT7H6ZV84NvT7naC9pN_-7WHB4I2ER9IKDCu3C-KrWADQlNiqhANhURutbArkaC1cK-9figvFKvkp5Hfx97r-Y14ZHgZhJWVA_R6HoT5GnvQSIqENPa496puIbEGYOweydWeJwweRqPJYLF9HPul2zhZecZVmzxolCjHPpKRX_wRG26zQbLw8S72jUqZYNjs2ht0OnUjZGL3ZxxDqaB5cYYqUGtWfm5LgWcf7GdKxzeqZ2yu8VHmsbuclLvocpuV_5lWYvMKtQ33Ap2s0QJBdpxVvMdGDve-qnj7NzVcAHmN80yP0SqZ-Ij6Tmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=rc7X8DbrUB6MhlRyQgtZDlll_pzHy6QNToGTedD_rY82JXOjO0ug7TkDepRAZ7RXTdfxQIFyNbeyUxUewFSGztm_dPtaTWj1i3Md57JNV-grpAzJlfKOg4ej-fWJC5LR7cNvAw_OHQVGc0z8us61ttAUGsSqgWldfyMEGjnqpIxBoFCHZcWvDTgOQqsNvsRKaxqghbrCDaxfZ4-sOsb1T3rCtI5NCX06570Z3pBBbhhp2IXvRMJqJpQwRcC0G_6ufX7TF8mmaEHu5ptEj5Lu9Rxv2hziwwFB2ko1WW51nUoQcnilQu2sgVKWEWSljcT4LpC31r-9ucHzOtcSKYAzkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=rc7X8DbrUB6MhlRyQgtZDlll_pzHy6QNToGTedD_rY82JXOjO0ug7TkDepRAZ7RXTdfxQIFyNbeyUxUewFSGztm_dPtaTWj1i3Md57JNV-grpAzJlfKOg4ej-fWJC5LR7cNvAw_OHQVGc0z8us61ttAUGsSqgWldfyMEGjnqpIxBoFCHZcWvDTgOQqsNvsRKaxqghbrCDaxfZ4-sOsb1T3rCtI5NCX06570Z3pBBbhhp2IXvRMJqJpQwRcC0G_6ufX7TF8mmaEHu5ptEj5Lu9Rxv2hziwwFB2ko1WW51nUoQcnilQu2sgVKWEWSljcT4LpC31r-9ucHzOtcSKYAzkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=cmX-1E2yTFfFMHJqFIpcFowZ7yZLl5Rm1CTiL63SVm9hjTf_Pg-xHTh8-WJQg8m9DDg65Dz56O8hn4DlrA42f7LNvs9wQQgbz2jyc8ojcujObaU0wCRTvyhnDqrA2lUnprTmzyvRP9aPYBy5qkuwTZ0uO5skjpUwWLi48afUuu3Iq5q7ZUxFwA-EhWHkOHyPUB0_1ve-2YV5vSTlYrvErw-vSaej-EiUqZU1BKyfBOX6oKSlRcMXRTXq5Pog0kGF6qnHjWGxiX13q9860F_nl9ADc6DJapbHnvXSq5kR-QMRhVQHksxtnIgWz1o9ZltIRYHOdbNdmUwAjv00ugdEbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=cmX-1E2yTFfFMHJqFIpcFowZ7yZLl5Rm1CTiL63SVm9hjTf_Pg-xHTh8-WJQg8m9DDg65Dz56O8hn4DlrA42f7LNvs9wQQgbz2jyc8ojcujObaU0wCRTvyhnDqrA2lUnprTmzyvRP9aPYBy5qkuwTZ0uO5skjpUwWLi48afUuu3Iq5q7ZUxFwA-EhWHkOHyPUB0_1ve-2YV5vSTlYrvErw-vSaej-EiUqZU1BKyfBOX6oKSlRcMXRTXq5Pog0kGF6qnHjWGxiX13q9860F_nl9ADc6DJapbHnvXSq5kR-QMRhVQHksxtnIgWz1o9ZltIRYHOdbNdmUwAjv00ugdEbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=qoIUX27GUa9LtGbbc6vw0DMvrPTQszmG5YKB_W7ULpK24PwUHh2LBr617SKH-Zd1sRqNoSB6krI21lVL-Vq1EskEGm6TYfX1BpA93aoLT8AkReCyDngxr8UM-6-KmCu9uX06IN_nd7LzGP6BElbyBgAYnGMCL_dr2lPjmcVWL-5tOsTbu7TyldIgZ8fdohlv5Z6oYb7k88-JDdJkhSz1LFvOirPoq-mf8Xwm7RMnCKRx7okMoZSHo8OCtq-cxg6w6dimG3BgrDc6ckf3mOCwBrrFS7QHGxhmxQDtY-mIhJpOeEEZAE3uMP5MW-rIBItgXpEOe9Ek5C2YEl4VJYEYag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=qoIUX27GUa9LtGbbc6vw0DMvrPTQszmG5YKB_W7ULpK24PwUHh2LBr617SKH-Zd1sRqNoSB6krI21lVL-Vq1EskEGm6TYfX1BpA93aoLT8AkReCyDngxr8UM-6-KmCu9uX06IN_nd7LzGP6BElbyBgAYnGMCL_dr2lPjmcVWL-5tOsTbu7TyldIgZ8fdohlv5Z6oYb7k88-JDdJkhSz1LFvOirPoq-mf8Xwm7RMnCKRx7okMoZSHo8OCtq-cxg6w6dimG3BgrDc6ckf3mOCwBrrFS7QHGxhmxQDtY-mIhJpOeEEZAE3uMP5MW-rIBItgXpEOe9Ek5C2YEl4VJYEYag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/biaVv3K7anImtk1-nUhpk5pZhUG_yrgABpKHEBs95vDELSsz23qWKXxvne-4HSgRRHG_D3wE9PsAtSYl_kGL_U0Vz1jp1hD9VOj1GNKv2fFPWnpkCm3wPQ5nh0tr9fVUXRvld7MlOarKbNc_aPdozsxNnCdGQ5sHm2wZWLh-UEe5934zRjE8Y9EfHj4JFURWXGHtm8uquMxVcZOnjQhURhakdQmvmebTly3bR7pcrkHuJOGDvARlAM8tr8sB3_WQpC4_gIqB92BXa66bhqbQmsw69esJ9gqUKNRGJ7nmYUTnvDA6d6NJlf4pFoylxsgzkVD9hYDDha7QLlXOXI-9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Krm-MulWLw8IhO590kZk-8jEzK-OnHPX1ed9NuXtBLTJngML3epjueCb7HE8BxzO9vMr4yZ9hcfypV7Awk8Cuxo9UwKFQTYJc6aRlC2zWh0fNKajknLBPsfAYaPp1tmKCSVKpX8I2BQ7gVjZ97Kudzb0vHIVkHqK9CkFA04AVbm46sopuyrCHJQ77G0fR6tTB7XOnNHi7OmL4Jxpk2YULLbQqRpgEofWSr7Ucw_UBQw-tkv6TZMlOIvYhOCNIyth89S1TSTCMrhPq69A0AknO75JFjHS9_iAlpNoAHHQpq9cBoX0gKi7Yl1nTL5WrGizgYa3NM_StvlINR4hK4nKLQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=A1-UnnonvdKXLvuKWb3vtA8yZJ8ekbYa7LsMKsSa8vy4ZIb_nRgmQPLcE5AdSKHYVH-jF0dH8USEo9_gRDMWjaiAQHYo8kFDiQRXR0IQEd6Jb5NKx7vqR_a82Nx89M6J7lBSVvZroBFccGpUKBq4xiAjkUtvjeylXEdxQSDsuOmF_PHd37l1woVszliHdfO8wOJtXtMt9I_DnmQkLDVM9yJgpgy-vL2vnPqDOhWMqSVWQQQug0cH7IuRFVIjw1JA8OUvOCRS7zM1TK6WpKR9lQjjvesE-Fet9OK9UKNDIchwnpfBtI93N4oITL5QcabEKCJyG6U5eE7RyOii42oL2bX_Bub1Dt_2TwpmyF3Po0RfieUSINkzzAE3KyBPggz79O1YsBZmZz1RoeVz-pLr1i5bmT8y78cx6mSZ65uT6DvH9XW_0P3YZzv0_2pkTtoE4JCf1-OKo37qC-ygieAqyKHmf68lk3qKGVbDyJJxybOmAE1D5zz5gFa_1CuvfC9OCPkg3A4dd1oySSC_SwKrtriCzWnRM7sVeseZ54D6WPrjJH0wKKDWe5mghZnRhHC28ZKmSF3tYE1Bo1lk6D-ziX98ZUIBpYuoDI4GYCVfrGse3tPJjhEr8H9vli4OG2tewJi9bgUcnvCpdoaMPskeUf4G82V-6hWuNAc96PdTC7k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=A1-UnnonvdKXLvuKWb3vtA8yZJ8ekbYa7LsMKsSa8vy4ZIb_nRgmQPLcE5AdSKHYVH-jF0dH8USEo9_gRDMWjaiAQHYo8kFDiQRXR0IQEd6Jb5NKx7vqR_a82Nx89M6J7lBSVvZroBFccGpUKBq4xiAjkUtvjeylXEdxQSDsuOmF_PHd37l1woVszliHdfO8wOJtXtMt9I_DnmQkLDVM9yJgpgy-vL2vnPqDOhWMqSVWQQQug0cH7IuRFVIjw1JA8OUvOCRS7zM1TK6WpKR9lQjjvesE-Fet9OK9UKNDIchwnpfBtI93N4oITL5QcabEKCJyG6U5eE7RyOii42oL2bX_Bub1Dt_2TwpmyF3Po0RfieUSINkzzAE3KyBPggz79O1YsBZmZz1RoeVz-pLr1i5bmT8y78cx6mSZ65uT6DvH9XW_0P3YZzv0_2pkTtoE4JCf1-OKo37qC-ygieAqyKHmf68lk3qKGVbDyJJxybOmAE1D5zz5gFa_1CuvfC9OCPkg3A4dd1oySSC_SwKrtriCzWnRM7sVeseZ54D6WPrjJH0wKKDWe5mghZnRhHC28ZKmSF3tYE1Bo1lk6D-ziX98ZUIBpYuoDI4GYCVfrGse3tPJjhEr8H9vli4OG2tewJi9bgUcnvCpdoaMPskeUf4G82V-6hWuNAc96PdTC7k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AiSik0OHY9nlWwwki66evs4SvVdxp82OHkcdjOV6brLicgT_uehFX1xGgKrZehAjFoDtWP4Ogrs-A8g9GSPh_2yQdA_HDQbQiH6anUKD1zuhTK4wiIeVH18FiC8BeHrScuHiynJiRrPLWQHGyeX1oCT29zBRhRoD1wmangiPeBWCjfwOfPPOyGWzmWFPOUrLE6soc93D5KROoprA0pWjfsuvJmOX6aMrUd2k3SjAfx5apAzLQfBSHSQPhprfUe-4zHwkrwsQ1x81-G8XYdS7x0l2QJdk-n7KtKrUwpNjsI35ChwrY5qXHM_w1xEv3pSdMwXqFeG7mpXC__lUHhJt7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IyhJsqoXyB6je8KgzMyZOtn2QSUOl5dU7WptVr-vshHY39k96GdFTbjsKvS3aAMUIAhadLyzpjmbUrmdtOU9CwfyK3uEguisxbsB6Fd-pJmrbpiEBrt3xLy2fGOw-3EJsMIKv2jRD7W6bOrPq1UMT7vqlYCIwzkuz_B2c00ONkznr8RmklD6vTz0KVXGE-ztwrc6GzIDFFC3p-SaBkMl5njYv8KUrdBof8kRvwoStDsMH3JX4CskRuphZcmiE5nBb-WoDKTOyzgSz0ji0I_jA3z53fm_J-sXltQIBd8TAtKSeoLfbmZs8BiPj808mlwa2r5F-bSQH_tH8CH85KiCEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CPU5QU-qXoM7aQP2X78vUmqX26B6qTlBl4DrR7KXY0yZiTlwv6xh9sLDffBatqG20mdqZ-5IRzf8_KoW_bYpsgbPUuKOYT5LczVhREvKgRE6R8c3g6YAgtOQ3ZbrMqcuwk9KeRVWFu0Gq74pe6pTVZoPDc5aogMNDuxPMcZNyDzBWK5b9cMXOa0tfUxy2a1wzA3BN-_0ol6D30Oplx85bx8a2OXwfTZTwLJVjCTrcrL9GWMIEcXsOFj73XEMZyOuIcRs3Qbqet7qg_DN4OxyXA-AM0J_y901gQn12nHf_3u5ntrn1GaOf-EG8TbWooMvtObONuw7fX-KxOe18PyWiw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhGOzcE1Xwb2pzDUqmCgHb4Evmqc4Rd2KtZl3jp_pTHI_pG4k_lGgqtPdZv7rxFhE78hkJFbygvSbW-xQUWGJRnpN31WfuIjrwblt6wD7exMHjEv6dZobKhjaNJPA8bGybd9FgoW4umTE_dxo5DFVJNjS95clZwsQEhaOb0HulpHaxaG_rlze4hk1MsaHreJx_oqrw9OOO-_2qd430UwP6weUzJBGTJci2BZ1a8fkAHccTp0Uv3oRX7qQVaatjWTFqksr5k2eOFuSs6Hc8SAOuBfLb3PYvWZpVSjKSSoqK-Kxn5f_cAaAbWdj1Pgx3Q3Dsj2M04na7Zm2Z9UZNhfjw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=V5Yce2gto-WsPLQHxVjWEx9aEvFq_7PmPcWazkzS1qkzpBU-4HgYud45w4s441abDwRpZ2JfwCarntYliUQEki3ZloGTlm_HPCTs01rd460-j53xRnxmaiER0V88jLg5JEvtwr0lnBqPq1jgPJBgsBDkwu1BcqMQO-8SOpyTZ2irrl7S5vL0J3jJWSKkiKUD18xWqwVK747Tta1-DdK0OIS5omINNCiBitlzJzydVy4kL01mFZc7ZH0ttbtMmu_ZygCt_7bBKuqVlgN-7VIlRlCOfGc3UqLGd3T0TVS3xpcjZEKHn8L5eTA7bnrtrTvFsvu21Dcn4bg4_L1NudCcwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=V5Yce2gto-WsPLQHxVjWEx9aEvFq_7PmPcWazkzS1qkzpBU-4HgYud45w4s441abDwRpZ2JfwCarntYliUQEki3ZloGTlm_HPCTs01rd460-j53xRnxmaiER0V88jLg5JEvtwr0lnBqPq1jgPJBgsBDkwu1BcqMQO-8SOpyTZ2irrl7S5vL0J3jJWSKkiKUD18xWqwVK747Tta1-DdK0OIS5omINNCiBitlzJzydVy4kL01mFZc7ZH0ttbtMmu_ZygCt_7bBKuqVlgN-7VIlRlCOfGc3UqLGd3T0TVS3xpcjZEKHn8L5eTA7bnrtrTvFsvu21Dcn4bg4_L1NudCcwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=sjoJW49zFAV3iJ_kFpbM-BgrJmWxX75pZDHsYuxnVjb97_CWZHO5ne466PNiX9RVq_nBi-uVHr2pZUSt5E2EigvacR4LmcTAvUDw65POxVXLEMeOhq2sfolQDW4JSCExtGIFteRh4olJbzoLN03OZBAukyV3-QpuOLROGUNXleSQeLJKWkoAt8HZDtqHvcGOTTyN3U_FpxAjVjPSyWL6q9HUpvg6FaAMIxBaF760IK89eFF60NILaU4XpO9rt1a-6HTeXdCZ7gLsyGpCiW7P9B1m6HrJV8_KUxBJQifDjQ1F-FqYrkbb_QNZVQuIbi_WE7_8lk4csGTEU_jLXVVZmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=sjoJW49zFAV3iJ_kFpbM-BgrJmWxX75pZDHsYuxnVjb97_CWZHO5ne466PNiX9RVq_nBi-uVHr2pZUSt5E2EigvacR4LmcTAvUDw65POxVXLEMeOhq2sfolQDW4JSCExtGIFteRh4olJbzoLN03OZBAukyV3-QpuOLROGUNXleSQeLJKWkoAt8HZDtqHvcGOTTyN3U_FpxAjVjPSyWL6q9HUpvg6FaAMIxBaF760IK89eFF60NILaU4XpO9rt1a-6HTeXdCZ7gLsyGpCiW7P9B1m6HrJV8_KUxBJQifDjQ1F-FqYrkbb_QNZVQuIbi_WE7_8lk4csGTEU_jLXVVZmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=CSYvwjcCfGEkjRx6Hzy-QafEr1NDTU9Pc0RIuWZnmMMxeHFWhSyZIKnVt6kFXdAHzq9TGU8rmlIeNvG06O7rDqkLrLpKcEW5xSXSRthwgzBAumIyX8W0aALDAIyUW3lSs2HZHmYNKepEsMLx_5nMwEFjA9faIRmlQG5ZxYEl-HYLQq8oThM9LSuQTClTq2jONHWSMyAR6axeQVdvHUtmqUTBLoxugUzm5TgBFnvdnmdgnlRIheo75gtTpwuF4tSioH-2QDnb-E2QIqm6MDz0s19hexoWq3UkjbHKdutQXNxhOXlSzp85o82Z9L02Z8Dl92bjZgyXi7N7fkiuXQOErw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=CSYvwjcCfGEkjRx6Hzy-QafEr1NDTU9Pc0RIuWZnmMMxeHFWhSyZIKnVt6kFXdAHzq9TGU8rmlIeNvG06O7rDqkLrLpKcEW5xSXSRthwgzBAumIyX8W0aALDAIyUW3lSs2HZHmYNKepEsMLx_5nMwEFjA9faIRmlQG5ZxYEl-HYLQq8oThM9LSuQTClTq2jONHWSMyAR6axeQVdvHUtmqUTBLoxugUzm5TgBFnvdnmdgnlRIheo75gtTpwuF4tSioH-2QDnb-E2QIqm6MDz0s19hexoWq3UkjbHKdutQXNxhOXlSzp85o82Z9L02Z8Dl92bjZgyXi7N7fkiuXQOErw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=QDHZ8EW13e9IuoeIqO17y9LluPB-Mcb-j5X9sNQ9vJPzQ06JxBKQH6G47U8HvVInYHdC2IQCgwJ5Ys8s1BLom0IEHn2tFbV9KCb40Lhak3KH-G3FeL2K3SiBWQl-sa4p2ji3covXjHlBWv01u-TfnTJSRsDlccf2-lq4Lr3i2EQaESNFByy20f_MdLt_lIhyAUO_v91AXagkdFqob-F8PUjplDtrpP82KNj7UbegT0TeXD2njeCDtL4NdItlWhp_NXcoLHwb7Rr_TU_se19fdJkNJrUW3zpV86t8kK2G1c8cbXX0F9paeKEPJBZGN-a2DtcEUWKRH38rNqFdj9QGWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=QDHZ8EW13e9IuoeIqO17y9LluPB-Mcb-j5X9sNQ9vJPzQ06JxBKQH6G47U8HvVInYHdC2IQCgwJ5Ys8s1BLom0IEHn2tFbV9KCb40Lhak3KH-G3FeL2K3SiBWQl-sa4p2ji3covXjHlBWv01u-TfnTJSRsDlccf2-lq4Lr3i2EQaESNFByy20f_MdLt_lIhyAUO_v91AXagkdFqob-F8PUjplDtrpP82KNj7UbegT0TeXD2njeCDtL4NdItlWhp_NXcoLHwb7Rr_TU_se19fdJkNJrUW3zpV86t8kK2G1c8cbXX0F9paeKEPJBZGN-a2DtcEUWKRH38rNqFdj9QGWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=sxIlDt9Nno7-MLokJJeE5W4fiq0P7tBjHIcX1jaF_pew_ppi92pfyrJtxkCt-8U2ZBETzDqFPwGhjMXApDc7lu-l0cXKr3TO14RTv0XIV03Zoqr0EKK1ZY1lHF9FLdVZAhJgjW_voYVsK5EDK4xy4I_pKlsfkLWsYLOoBYCY-NIjyoKK1mYjRPQx2AljBQVfKTdncqcSDmZarvl3133mdRXW8f3zRCY6qnuZGmq6NKnH8C4WAaXs8K4jnsGh_juW_YeuWrSCTySCJ8y7ovbn8dLBUumU6d4XIY32L4xWi9DMxmNAsEiHXeSwFrTPT6qodu1YWBzg_2-TWUbmgZ36Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=sxIlDt9Nno7-MLokJJeE5W4fiq0P7tBjHIcX1jaF_pew_ppi92pfyrJtxkCt-8U2ZBETzDqFPwGhjMXApDc7lu-l0cXKr3TO14RTv0XIV03Zoqr0EKK1ZY1lHF9FLdVZAhJgjW_voYVsK5EDK4xy4I_pKlsfkLWsYLOoBYCY-NIjyoKK1mYjRPQx2AljBQVfKTdncqcSDmZarvl3133mdRXW8f3zRCY6qnuZGmq6NKnH8C4WAaXs8K4jnsGh_juW_YeuWrSCTySCJ8y7ovbn8dLBUumU6d4XIY32L4xWi9DMxmNAsEiHXeSwFrTPT6qodu1YWBzg_2-TWUbmgZ36Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YK8s9uXGkedYu_FZBPXBq1_YQUPCdEQ3J4PpV5CtGAPgekvDknJqgrPj5NYHcKvAnvyoK8C4kJSaOQmFcmaVAKX1dTQKMoJFEnd97WAUxO0obbMvVdslZh4l7qzR0D555e9IRxZ9tdCpIRYLt6__6CEUxuuVDvCOOoTCBEU1TN8pRBg2f-DpuvraCWHkJTOaUB9wkuB-8HyMuz-lQEYBojPMIIaiBDEc9ntbt2rdLtjUWN5uFXeuBD1YhMJE2XDUf1UtdXwQrWQ2T4rsODc3RytlBYb7N1yU8ubXTt0Cm60jLv5Eb5m9XAhvKUzL2GTtPi0iQr1S3oXIz3wUSXaRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=qmDZqGBZ9NdcpouoLdeLpEU86euwKRAkGTCmYScP6Ajy8PnfLiAYWbPfuNs9dc2Kq6vNOhJaSDn5K4rvskJcSOWtqA0HJY8v5AFeMCh6HPnVlLqfOd-qRMYsR6gwLb9skue7xSOVq6TahWOJlLzCdMIX4KeRMgLhYfNN8vO6gSmWyWfY-U-pn07Aw60_L-xXgC51AFy4X_9Z9nBpcm0hHSu3dE44_NTqaGEmlJTQ5IgFbeDMbTmoXdIZawjAn8tO0rTkFivInl63DDr8p7pqijmyaNcCpPY8nFZ_kW4dp53NO6GBY1DQCiIviR50FxiAIG2dWxgZTjrJ1u46UnWXJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=qmDZqGBZ9NdcpouoLdeLpEU86euwKRAkGTCmYScP6Ajy8PnfLiAYWbPfuNs9dc2Kq6vNOhJaSDn5K4rvskJcSOWtqA0HJY8v5AFeMCh6HPnVlLqfOd-qRMYsR6gwLb9skue7xSOVq6TahWOJlLzCdMIX4KeRMgLhYfNN8vO6gSmWyWfY-U-pn07Aw60_L-xXgC51AFy4X_9Z9nBpcm0hHSu3dE44_NTqaGEmlJTQ5IgFbeDMbTmoXdIZawjAn8tO0rTkFivInl63DDr8p7pqijmyaNcCpPY8nFZ_kW4dp53NO6GBY1DQCiIviR50FxiAIG2dWxgZTjrJ1u46UnWXJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=XhYgvFlNsyvlPWXIsR8TwA9yBNgljhW4Oz0-v-bSSTyqEVDI62qXQWX-ehyx44e6-5rgF8KSBfYMdycgvUFg_WSbfV2i789WvSbeMIopRpQEq6yzJvUsyYn5bzzJr1PkjXFc8xL_7tbjB1bsW_6IzqbZ6JwtPNcfliaJNBbuwoQ9fZUnFcN6A2Q59yvJRcDqJmGxtp8xRAwq7_qP2PPe4rTmBze9tYPzRDyc8qseXca2CFSAFzd-xf3bmy99bK00JWUXOiWM6fMriDD9UKPhvHenMLd6xqFFqA4hSnNp8pQiSSvITleOPkExWSIw9Sk24OyjQ79exwLf8Wsef4H43w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=XhYgvFlNsyvlPWXIsR8TwA9yBNgljhW4Oz0-v-bSSTyqEVDI62qXQWX-ehyx44e6-5rgF8KSBfYMdycgvUFg_WSbfV2i789WvSbeMIopRpQEq6yzJvUsyYn5bzzJr1PkjXFc8xL_7tbjB1bsW_6IzqbZ6JwtPNcfliaJNBbuwoQ9fZUnFcN6A2Q59yvJRcDqJmGxtp8xRAwq7_qP2PPe4rTmBze9tYPzRDyc8qseXca2CFSAFzd-xf3bmy99bK00JWUXOiWM6fMriDD9UKPhvHenMLd6xqFFqA4hSnNp8pQiSSvITleOPkExWSIw9Sk24OyjQ79exwLf8Wsef4H43w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=XkhDnrTbAT0u8C7-1yfVJ17kv_2ll3AsGO7h0kQYKhlVxEPsNQm4aKwNfMfCwGDhrEV-YyJlfg-v2n4zFWF1RlblT3-brTHlNslRI-sknkUJVdk4f5jbxjPPuknLYe5A7jecsbucwy_sHF7iFt6oDndiJWvXsTc7QBnu3_V52QARh-DCL_uNasQqApvQkX62Nmk_iVpSAzKO5ZOk9EbJTHIL9Xi-29L7-wuGZfWe1F6T2DeiBt7r8NK1_pmQ3Hl6gt-AxiFzZQkLh1A30qOcDslTe6XvG7bd_7zn7t4UawO7P1elhKDkHuQHOTWwQa56HzDYKCaQLzaFZ7uXWaa9lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=XkhDnrTbAT0u8C7-1yfVJ17kv_2ll3AsGO7h0kQYKhlVxEPsNQm4aKwNfMfCwGDhrEV-YyJlfg-v2n4zFWF1RlblT3-brTHlNslRI-sknkUJVdk4f5jbxjPPuknLYe5A7jecsbucwy_sHF7iFt6oDndiJWvXsTc7QBnu3_V52QARh-DCL_uNasQqApvQkX62Nmk_iVpSAzKO5ZOk9EbJTHIL9Xi-29L7-wuGZfWe1F6T2DeiBt7r8NK1_pmQ3Hl6gt-AxiFzZQkLh1A30qOcDslTe6XvG7bd_7zn7t4UawO7P1elhKDkHuQHOTWwQa56HzDYKCaQLzaFZ7uXWaa9lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=o3qkC23-jL5QBGo_tGWA7bFuu_C3YMiJLN1moPz58Gme8RFSDvie4K1GgKEms4pnwCH-r37KSNSRzS06DT3ZzZEY_YTsUSiE4WvW6GfzdW-VptQKW8pnW2zK08yepI-SzXliuFK7OHQkdPa84jgaMVudvMb1qrxCMh5AoUqF_flTb6XY-eMX07RCOw3BDfwpfUcBs5RVwEcWytkmnn4Oq4OY0JydWPeSh5ndTKCEGGxG9IUk13gGGeAzOo_OYH-g9AxzAkIoRIYnnXMqLXl_jWf7fJu_yMaVHReVffeC0ielTgLiFetHCIZBqP8AjoBCZWboYze7f5GpX0bAkDqjJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=o3qkC23-jL5QBGo_tGWA7bFuu_C3YMiJLN1moPz58Gme8RFSDvie4K1GgKEms4pnwCH-r37KSNSRzS06DT3ZzZEY_YTsUSiE4WvW6GfzdW-VptQKW8pnW2zK08yepI-SzXliuFK7OHQkdPa84jgaMVudvMb1qrxCMh5AoUqF_flTb6XY-eMX07RCOw3BDfwpfUcBs5RVwEcWytkmnn4Oq4OY0JydWPeSh5ndTKCEGGxG9IUk13gGGeAzOo_OYH-g9AxzAkIoRIYnnXMqLXl_jWf7fJu_yMaVHReVffeC0ielTgLiFetHCIZBqP8AjoBCZWboYze7f5GpX0bAkDqjJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=TH17e1rbLnjKgxEDcdhayp9NeoMzUVM1dEK5zvA7rBvsZjWJgNi2xjLQk6s8AQ0tySCpcSvntss43Yl6jtSO2sZI_n2XegTD4Ijw7zbuMHw1H-uY0wU13XfsH3E2VP7UepzKhd0V2NEhL6DSg5FX4oGOw0GdzfrFu_0t5C7y37KItHneNkSxhnOuGKlPjMmKkpwFlEOELFc8MYvJxKb_OVLo-zV3gx1db5dHRtf5GLOWuCRu-fXqa1-o3L88U_eAya-p6qu5a8jkMb8Rz67IiIet-DOW6hRypR-NYeaq4DMCvZOuSMCGqUBlb2X1oPWE7etPDPkljfb_jJdw4COHlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=TH17e1rbLnjKgxEDcdhayp9NeoMzUVM1dEK5zvA7rBvsZjWJgNi2xjLQk6s8AQ0tySCpcSvntss43Yl6jtSO2sZI_n2XegTD4Ijw7zbuMHw1H-uY0wU13XfsH3E2VP7UepzKhd0V2NEhL6DSg5FX4oGOw0GdzfrFu_0t5C7y37KItHneNkSxhnOuGKlPjMmKkpwFlEOELFc8MYvJxKb_OVLo-zV3gx1db5dHRtf5GLOWuCRu-fXqa1-o3L88U_eAya-p6qu5a8jkMb8Rz67IiIet-DOW6hRypR-NYeaq4DMCvZOuSMCGqUBlb2X1oPWE7etPDPkljfb_jJdw4COHlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=VqfqdUEN1-_oNDROgcTYKWaTq-3PXBfEqwiZDCj1GP11a4hWK73JYaV32z-RAm5nxNPb6gWxi9Iti_L02WNAdEmKOOE4kb4MijvWVBECYCKNX1B2unKkePidnFikMAXDkxCE7ywUlCreUvQnwQGhKVDfV9Mmn777QsegI5h7FrNQh1G5yiRfbZ1QBMg5o_SSRm5A8XgLuw3UFhdoo9nSiyiRv31E_Kwz3dB9_-HYgeexiJo-qtUW9ak9RgtchK2D5EONYUwognmwmf-q3DchDrQ3OaMPIdQy7OCaZtolcX_yFeA7Ut4jrb7nYM7rss7i5F3ZXKBGpI1Xmd1JkyFTRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=VqfqdUEN1-_oNDROgcTYKWaTq-3PXBfEqwiZDCj1GP11a4hWK73JYaV32z-RAm5nxNPb6gWxi9Iti_L02WNAdEmKOOE4kb4MijvWVBECYCKNX1B2unKkePidnFikMAXDkxCE7ywUlCreUvQnwQGhKVDfV9Mmn777QsegI5h7FrNQh1G5yiRfbZ1QBMg5o_SSRm5A8XgLuw3UFhdoo9nSiyiRv31E_Kwz3dB9_-HYgeexiJo-qtUW9ak9RgtchK2D5EONYUwognmwmf-q3DchDrQ3OaMPIdQy7OCaZtolcX_yFeA7Ut4jrb7nYM7rss7i5F3ZXKBGpI1Xmd1JkyFTRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=QwYDYbbQljRQxABuoLlZz2UcKL44b1irWE0xhc0gpnUkck_4kyDrUsaqvnPS86LOC_yFyiWEq2gAF1taDbtG0NwcdqHqkJV_xO8mGQEwb2SX9biAdiwVyEzZizQjpAUuI3l8PjFo_peByVeHhB_4u89rGR6lE_bB5BjUmhsVcJ80b5qBYg1xYnGbTBq5QpAEJPWIm9va17V5p7GpG_OX-sSTgrVN6FzmdPAq-IDxj1J1rIBJRCx5b8IRatEiS-aByEUBxKckTD30KNtbv_lAjp8dS7rhSTmOLSFhFrzzVSM_hWPujIpv4vev0PfmX_jZ1w-cXQl_HDQ2bdxYjY_t0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=QwYDYbbQljRQxABuoLlZz2UcKL44b1irWE0xhc0gpnUkck_4kyDrUsaqvnPS86LOC_yFyiWEq2gAF1taDbtG0NwcdqHqkJV_xO8mGQEwb2SX9biAdiwVyEzZizQjpAUuI3l8PjFo_peByVeHhB_4u89rGR6lE_bB5BjUmhsVcJ80b5qBYg1xYnGbTBq5QpAEJPWIm9va17V5p7GpG_OX-sSTgrVN6FzmdPAq-IDxj1J1rIBJRCx5b8IRatEiS-aByEUBxKckTD30KNtbv_lAjp8dS7rhSTmOLSFhFrzzVSM_hWPujIpv4vev0PfmX_jZ1w-cXQl_HDQ2bdxYjY_t0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=ZZhzJFcR2MNYBHQKjuIpyzZ7Qr-VUpVlEDaNiwakRiy20HS3BmQw7RjZmqySHteArGSLHJmIUQpXFxi3q5VijJjWjkct7G8WuA4_QwHvVR-kM4c8iXC4XhJWrdMM2q8WLs63J2-iYMNQTeGP8OmZXNItyegZ7mIoomkzqUbn4Pkjd6L7U6hb_lvZCYbPiOUbBV3KUhuKwifitEY3WjY0fE-0pBsLHvWKBIt0nuWe_QsxBdV7i-VrFTpUgImwPQQosXsuBqHFOiZWbtcGyN0AmzlifqvL7M7_iolDlK4s-Ocsv6gSA1n-Nny-nczOoHqscF9dMUjkZOBAzmCoUUiwNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=ZZhzJFcR2MNYBHQKjuIpyzZ7Qr-VUpVlEDaNiwakRiy20HS3BmQw7RjZmqySHteArGSLHJmIUQpXFxi3q5VijJjWjkct7G8WuA4_QwHvVR-kM4c8iXC4XhJWrdMM2q8WLs63J2-iYMNQTeGP8OmZXNItyegZ7mIoomkzqUbn4Pkjd6L7U6hb_lvZCYbPiOUbBV3KUhuKwifitEY3WjY0fE-0pBsLHvWKBIt0nuWe_QsxBdV7i-VrFTpUgImwPQQosXsuBqHFOiZWbtcGyN0AmzlifqvL7M7_iolDlK4s-Ocsv6gSA1n-Nny-nczOoHqscF9dMUjkZOBAzmCoUUiwNYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZkGLMt55SEvxAWtRRBF0DIOvAiW8QVhSqS3VNA-9NfiBOO0R04I7-RmoyY3CWdkodEE9FOO8PxnWXZqxC6866ZA8ZPohJaFht9kuIRyjGUPKz7HnUDariE_jo7VdQ0A0aiWUFw29tN7m7STlq8cInyMwS9S5B2PAme-xkwCYVyiks77oftkMm8-5ZAaUuqS_ZRRsDBa16cvvEyBuAHVBdS-3oLHLspVBONn_A9V08Oo6D8a-BJiS0Le9t9D8TRtL0mulIw834t340zf04XT4zacxXAEXhmjPN1oyCv-b0uMvfOQJxuDIcIMN0IrBtnBSZKspOWGpvSGXsCrDn-d3jg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=bwJ4jTIzEj0cHlojC54keZrZlPVLJl0ruJxqJIsqQiHMQ0tPx2JNqdFd_C5zwEdhKZzIU765UQkoyrabdl2qfdEJPVbwLeHSOnCQesuX3UiTPxhaDRrT43FNRVxOuwhJT34Z6SutdCE6lQEbIhq-UpxPGcdJ4lwGAVVLfhfk4Lr1YhUiZh8uFhKM9h8TKVOIk2p1XLyo61ec_A7dc65iYWgq_N_09YaPBB0RaUDuxzyW2QIH79QStrqjQsfN7pYhTJAbdgZYPJtFgR45Qc3jafgole6xJt34R2NgrIoCn6iqCI5LE7t5q0yM0YgQkzE-kc4UWvxy38IAwLWWjL5Wgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=bwJ4jTIzEj0cHlojC54keZrZlPVLJl0ruJxqJIsqQiHMQ0tPx2JNqdFd_C5zwEdhKZzIU765UQkoyrabdl2qfdEJPVbwLeHSOnCQesuX3UiTPxhaDRrT43FNRVxOuwhJT34Z6SutdCE6lQEbIhq-UpxPGcdJ4lwGAVVLfhfk4Lr1YhUiZh8uFhKM9h8TKVOIk2p1XLyo61ec_A7dc65iYWgq_N_09YaPBB0RaUDuxzyW2QIH79QStrqjQsfN7pYhTJAbdgZYPJtFgR45Qc3jafgole6xJt34R2NgrIoCn6iqCI5LE7t5q0yM0YgQkzE-kc4UWvxy38IAwLWWjL5Wgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLabEkq3wjrbGpqt82KZ38dvJHTp406AeVUP5TN0sdvlNnqtNhAIIIHgFK8UQ38CxxhV3T4SqiqisXzjecfHN3hBYtd58xmOxotUL8MZQWBfPMX9xRhC6cgmdKyiB2QUzq9a4kWbGpX4U1k0V3P7QxhNoX3dlbC6jO07tI0e5Erqu3WrDbKwX690YyenaTjdo6_saMHTBUIPx795VDzqZUbbSBKCdf-TA4rD56NIk8sJsGZGIAYlhvmtUTxrbQ29GN3-LHFSJmdXF7LQH-0P3mtdaCSRtqBLhY1Vii7AxFkjdpa_AXM24OBh8M5z5wr2d7pyaI4mVRfy_2QehlmSINV4c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLabEkq3wjrbGpqt82KZ38dvJHTp406AeVUP5TN0sdvlNnqtNhAIIIHgFK8UQ38CxxhV3T4SqiqisXzjecfHN3hBYtd58xmOxotUL8MZQWBfPMX9xRhC6cgmdKyiB2QUzq9a4kWbGpX4U1k0V3P7QxhNoX3dlbC6jO07tI0e5Erqu3WrDbKwX690YyenaTjdo6_saMHTBUIPx795VDzqZUbbSBKCdf-TA4rD56NIk8sJsGZGIAYlhvmtUTxrbQ29GN3-LHFSJmdXF7LQH-0P3mtdaCSRtqBLhY1Vii7AxFkjdpa_AXM24OBh8M5z5wr2d7pyaI4mVRfy_2QehlmSINV4c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=tnEayWjCTl3sOJkqFyd8a9wpUvU3tOQK-R-IVyngwV0CZErwaVX6hE2Cw5SsorVuwukV8ciy0LqAJQwW3ibfCUXvEthatpBG9OcoSnUUgWb4zmv-K3HKe6Q-CB09lZvCsTEWmXc-zVf5hvMNxVyiOs8qYv7jijeu7yCCtRe1vGL5Qir9x2UPBqftkZMoTbkK4cR6Ao8xX9LgATOO_R6DX3bypvddqD_3W8c2TxlNtW2Or8NviD8vTkevIbp0-usT0_2geS3yFf8EyNGECB3pw1eXceagNdssp0izsSreL3ueJGq6hQ3cpJ9Q8G7lwR5fnPVqBRYptsxVawQbYSSedA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=tnEayWjCTl3sOJkqFyd8a9wpUvU3tOQK-R-IVyngwV0CZErwaVX6hE2Cw5SsorVuwukV8ciy0LqAJQwW3ibfCUXvEthatpBG9OcoSnUUgWb4zmv-K3HKe6Q-CB09lZvCsTEWmXc-zVf5hvMNxVyiOs8qYv7jijeu7yCCtRe1vGL5Qir9x2UPBqftkZMoTbkK4cR6Ao8xX9LgATOO_R6DX3bypvddqD_3W8c2TxlNtW2Or8NviD8vTkevIbp0-usT0_2geS3yFf8EyNGECB3pw1eXceagNdssp0izsSreL3ueJGq6hQ3cpJ9Q8G7lwR5fnPVqBRYptsxVawQbYSSedA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
