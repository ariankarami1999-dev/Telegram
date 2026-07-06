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
<img src="https://cdn4.telesco.pe/file/d0pAHRt8jWPFAIqfaTSn-1eeyt2OkXBO75ajzl_eiBfmplvvbI3b8ScQMPjtx8Mln1kIx5rb_06gKSNHaECFaZtV-sYyv8BHG1_HJSdBZ0rM8lVnFzlje9SZl1MjdeaM_QIw_GAjAcBfrG3vcQJicybBt7Eq_NclD7WNP2T7U0qj2AH537FW1XIt2D4XtRo7I4EkxWssXKnAuHASWrDz6cv6QZ7vYBZEP_tlXT6wIGFnk54DCgafVgE63M44OKZXFRiWcQL_WbjZZnKGtJm05iA1-QHFywoqvBsYHJzl2kQaWmj1ZKaHuPB-59xDRXdg9zhbXolAlx3TL8pti0_tNQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 11:41:22</div>
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
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5874" target="_blank">📅 00:02 · 15 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8TmlUukgx1CEMxrplBrST7mcORmueW5TPxmvJyYIx1gXuGnjch6i_jSD6dxQA9wNntu2S2uOLXXgZnMEc_5MsPr2YVuuR5OPlbKMSGK7xmig-nu01nyG8d6GkeyzUxn4tckbpN7A-DKWeZjdRctdIIw0vkX9V69l6raE4_Oinyql337INXK4g2riy7f-GFsi6GF3lhGhIcrg4xvRS6XWe1WuRul9AhWMl13Wrin5WVHXwbzwSxrMa9nxYPEhZaenXITHHcr7OmRGUHDdKQ7THRh37vPrCn9oMKyyrGIcOhk-lU7twZS7Bx-MskFFy87mKoeN8ggtc9CNGde889kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVsQUaVhpBleS0A9HV3qCKxPVTueWm60EDxEVyDX-YvhqL-ejGfJUXV0L56FnLSXA0veX1kicCONQ2aUldvgBrpCZRRyf-NoHhPd6dnUX0LBimSTnMVCu15onwfH6Q8Dv90G0ED81XRPze7hgMj7tboPMZ9kiJB2WxaEyhu5PzHxEhAWvV3FjlIMpylqbuk1U7KeXCsYgY1yBKsGRkS_KHEFfcq9NmfWZlMYqi3bH0dcjrd3q_H3nVqDsKRLly7Ok_cVnSpwHyCUithvijY26yjj3OsC9CXue-GAriOJ7-81Nx_c7RyAQFjbTB_EB9dAl4xpeIPLSLASqj8G7qhHOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1e8TwKDWpgkjm9mSTOVfDoeJZCgFhkCtWw66CFIHTGHlCXOXhWfi0WnOUoPfVeUVY57_DpGzs_gth9i25mJWKBnJj_-wK2as5fsPTuCzCyNSfM4VNviXVCJs9UNqcgbjroGvSsKnsdUjlZbFLm3uGAkDDKuUpgN7-D9JjZlBQgnWVJ9opP_i9PYNJtdYkV96CJUtVvNG-ZecG-cyTs7Qj0zqOwxP-3lUbL05xJvOxkYYqKoAASbLBYVzHg0MqGoTxgpHrYzxi0zh5ZX-Y3T7XZghKLxf29GVceYEFvAGmatrlmKBhcQSbaliPxJRQgMYpYIsuKDMr5QJymx1FAd3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sz2XeNNhTrwAqM2csQQww9OQCviz5TRwnY40E6Qf780PxdYwQNa3xGC_ITnD-3o0V0nRaUsDmyNTHDCQV5rSQpq2iUyGZQR6tQzj2vpYIRAgJ7ieH4xAOZHqxTx2shYOAPlvrTelaXioUaQh6ILYrfKi_qBfU2KQaKHjixdljABIt6un9WnhFYIvCjLJRge1V1foE0O2MsCCnlUycqJlLsnq3lPM-n2npICCh8in7OJdaF_wesEEZ8hffA2ziXnWvQeC64rJXXCZ9Vg-kWAe0DCHAY8h75Gdqjngmn-i4f2DfSok3oRGaecMgp0Qd_qrGnLCrZcBVNWY7k8wOnTWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4nj0_h61brDk5GKExnBcA0kbfnh0gCQDr5nl5y2_qNmNeYd3WmSoVX55XR-0fgxSI-FGP2ubkDOFRFuo62bYfuesvX4bhKCBsbQT-lir9oYweKY5Yd-uvh8qt6u02SJIQPmgWdJDXttauPF_py0BMyfjNlPyWadt8k2q3FdusYkfoWj2Fd3CyQmVAECyx6o5rrwvEsJ9nO11CvUeUislxN5jl1118OiU6xX48HDjcUhBO2SbQ_G0SnjEGGo6B4lN5StynI-od84E7uJ-acwnc_mmT7N0bNWJqkHehFyYvavWL47ovavsmwOo_GTghviGtfDii1BBIVDNqsdwpUBdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eoVzkGn4RXGCz24MWFm5s9GmXsUfGvXtjVxauo0One9WFPToTC7uGOKnVQAkBSNY5i5siMctIil-1y2_SeVkQf7m_E9Yci4hicnqDGo8sr9WwqCR569tt_faAPH1X_dodcyNroc8VYdEiDK5men9-ju5GjUP4Z427Dci6XqjDgHovvzTecU-uSJBl1wTWYyp2WY9XKfpnFpWxpHCLR_4Of1jgTWesN9SoUzckicZKBgQErO0IKYcQKIf32mVhcZ9pdbvfYan7CR7_RB1QLyzpDofPMHVQp5MiiAbdpBfPLPzf1u37qE3715PBUJ2ViE-pX5NfjyuDzRht6T9CZd2mw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_KSfUyc5pe62baJQCwekIJIoEqH_fFV-vodmmr3slWDuCRXP6KKBLTeuaAUc8Y_ZpviGhYGaW-18acPr198pMhMqlabitPrexPqu7fcDbTZPngOXWKQDcEfGUKjp7Ks6iLVvXqgzAQn7nP-kOn1G6R2QHGG--F6UorieoXRxfMUT8gsvbDiB9Gn85lg4AEVygT1FxqJJZTLn0-a1xv6CtRBfj77Q0ALhD54duGS5Pemj6yebbGHqA5ksvA5B3ioBbwhp9x_APNSzz8bA547vBvegiXvawx_bwLg4woPsT0Heo7XmTDqB5CDKPSa2m3fL3ZPLZflSAC45p2q5ru9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=DUKjJUn7OqBrEmpJ-nQXmWQfsX78obd0iGoqdP-n74SIPlpezqNsQkWXEyTQ8UYjOnrIFEkdNEOhJypOYGJdfZS-YbWqw7fxc4iH8xQcTsBVN6MrUoNaw74lO-ZqD9fGxIfsux2lnsshlo_xy4jm2vMIHkOtN0oqDsW_H9wof1eTQke3zgCkDpSwXaeeuNzFOlYghXKPkupxuU-Kx3kX-R3sttMPJyfIlvDpwOEXImmO5kxDt0v8Ii0Ofe5_EYn9vDUvL2FIrHaPjN1nxK3Ty8PbQiiei89s3r_dNNDzoxmcPrI16KJkGG__BPmtkVKPBbXNUtw3knHYCj2VHr7tJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=DUKjJUn7OqBrEmpJ-nQXmWQfsX78obd0iGoqdP-n74SIPlpezqNsQkWXEyTQ8UYjOnrIFEkdNEOhJypOYGJdfZS-YbWqw7fxc4iH8xQcTsBVN6MrUoNaw74lO-ZqD9fGxIfsux2lnsshlo_xy4jm2vMIHkOtN0oqDsW_H9wof1eTQke3zgCkDpSwXaeeuNzFOlYghXKPkupxuU-Kx3kX-R3sttMPJyfIlvDpwOEXImmO5kxDt0v8Ii0Ofe5_EYn9vDUvL2FIrHaPjN1nxK3Ty8PbQiiei89s3r_dNNDzoxmcPrI16KJkGG__BPmtkVKPBbXNUtw3knHYCj2VHr7tJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=DIDnUMz6DNUT8_moKB3I36mN4NKZWvLHF8fRGbsDMChuU9xUhr0c2qt1G-kJqxt4QVHwpbT3S2Xi2H1GFjju3y0dZlqdL8eOexjvOcUZAKYmLTw4Y7okpEvLiM-D5ROyj0VCXc26VaDlheUDdey432aVLyafNJtot9SREGs1j2s4tMNgeS3Mh20znhz9SwF7NtLJQSOx039BkK8PYr4WqaJ63li3Mhk-Fn_QH8RXQwubFmohbC4SurFbihAZ9AJuHtVlEBwHVGCcoGFebOowYABGRSAVZhilbJA8ohkAVMsnsnrISNuXzQz3kRmk3_JsHeoH_DIvMgUE5O_d3bMRlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=DIDnUMz6DNUT8_moKB3I36mN4NKZWvLHF8fRGbsDMChuU9xUhr0c2qt1G-kJqxt4QVHwpbT3S2Xi2H1GFjju3y0dZlqdL8eOexjvOcUZAKYmLTw4Y7okpEvLiM-D5ROyj0VCXc26VaDlheUDdey432aVLyafNJtot9SREGs1j2s4tMNgeS3Mh20znhz9SwF7NtLJQSOx039BkK8PYr4WqaJ63li3Mhk-Fn_QH8RXQwubFmohbC4SurFbihAZ9AJuHtVlEBwHVGCcoGFebOowYABGRSAVZhilbJA8ohkAVMsnsnrISNuXzQz3kRmk3_JsHeoH_DIvMgUE5O_d3bMRlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=NGmJAKF8-g2T6j6o9VYYlndGz0voC7GrAt4Lv20QIyLdxuI61Zr-rbv5RSS8vCS9rJrV8ZWDUcEF2D7c7C5lTABKwd2y7xIMcO_LOpm5i1c_b3W8pblth6ne5OicPur4psTGgGBmyPcIPiY2qbQfNSBM7b7z7H_NRbYrsQQxnZ7vwDQ4VtT_ML4vGd9QSyH-bSMNQ1audgJybiZVdLMnAIuqzBJAuxKdvTbdjgeqHkTZC1ne_0vzn08LZp6Hf32xC5DWyanWg2xpiQbHS6oydZB5xXbKdfzN8Hr3IYGUFXnTMqRspThn3vvPZdPvoDrsjrSVAYx1Xs1v9jVRe_VmAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=NGmJAKF8-g2T6j6o9VYYlndGz0voC7GrAt4Lv20QIyLdxuI61Zr-rbv5RSS8vCS9rJrV8ZWDUcEF2D7c7C5lTABKwd2y7xIMcO_LOpm5i1c_b3W8pblth6ne5OicPur4psTGgGBmyPcIPiY2qbQfNSBM7b7z7H_NRbYrsQQxnZ7vwDQ4VtT_ML4vGd9QSyH-bSMNQ1audgJybiZVdLMnAIuqzBJAuxKdvTbdjgeqHkTZC1ne_0vzn08LZp6Hf32xC5DWyanWg2xpiQbHS6oydZB5xXbKdfzN8Hr3IYGUFXnTMqRspThn3vvPZdPvoDrsjrSVAYx1Xs1v9jVRe_VmAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=AHPzOg9_gJJtSmw5qcaja89Hyq2vGs1XMqacnFmaeRYMCiJB9ObegS0IkR6H6GKPSOHmTZByIxlqsnVZedqe67rSBAVTzZW0qJD6-FnMB3M8ZZ4O4oBRVJMxo7S9TG-wfH-Rg12K0X_WqZUTtk3bzECnDFgw2wTRlKdGJxMp9YMvLLZQz1TbEMq7BMVQC6VXs6SlY2qWhQ9e099iwhNr1s8ypyagmW4yjtzsZI5-3eHtQJGkXPuhHl6JhM1ea5ajNifpe0ECk2Ow6OkY_PyF9bqcjdEAKTQ-H3QKp7NTBgVzLZexNVc1e-7ElOonQJuQ94x35LcaVmZ5WPB5PJaiKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=AHPzOg9_gJJtSmw5qcaja89Hyq2vGs1XMqacnFmaeRYMCiJB9ObegS0IkR6H6GKPSOHmTZByIxlqsnVZedqe67rSBAVTzZW0qJD6-FnMB3M8ZZ4O4oBRVJMxo7S9TG-wfH-Rg12K0X_WqZUTtk3bzECnDFgw2wTRlKdGJxMp9YMvLLZQz1TbEMq7BMVQC6VXs6SlY2qWhQ9e099iwhNr1s8ypyagmW4yjtzsZI5-3eHtQJGkXPuhHl6JhM1ea5ajNifpe0ECk2Ow6OkY_PyF9bqcjdEAKTQ-H3QKp7NTBgVzLZexNVc1e-7ElOonQJuQ94x35LcaVmZ5WPB5PJaiKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=iGGyMPfXp7bEGYjLF2s0N2AIsKKhMcN-ex_qTX591AwiLrKXsiz3a_UzU6-6cdswdP3Bx4DHvkHRD5vkAVOphBsU8c9KeNqUigXOTcGpQ56KoMLEnc7YILhhtz7Fgfk4bUsLBs8kQq0eZsScgA9l04Q5mhzXJDIJHvm5R4QDBtL6AnGcfJaWgrBy8y6jqbSMhVZ6LdGtfBV3DJMdKvVoPJK_1tauMwppOFZ8FncwfpGOQl6BNJA36ycS48vNqcSzV4hrs1KsKCbT8B9O8uyv5dSs00nw0-m0bpJtws5KbPBchZTSb9o-tX0GBiQgEutxGzTSA3EYIC8itNMX7iL16Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=iGGyMPfXp7bEGYjLF2s0N2AIsKKhMcN-ex_qTX591AwiLrKXsiz3a_UzU6-6cdswdP3Bx4DHvkHRD5vkAVOphBsU8c9KeNqUigXOTcGpQ56KoMLEnc7YILhhtz7Fgfk4bUsLBs8kQq0eZsScgA9l04Q5mhzXJDIJHvm5R4QDBtL6AnGcfJaWgrBy8y6jqbSMhVZ6LdGtfBV3DJMdKvVoPJK_1tauMwppOFZ8FncwfpGOQl6BNJA36ycS48vNqcSzV4hrs1KsKCbT8B9O8uyv5dSs00nw0-m0bpJtws5KbPBchZTSb9o-tX0GBiQgEutxGzTSA3EYIC8itNMX7iL16Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=dF_PkfXhM77y2MfeXgV-N05VWJyMV-JpEP88m-BgNwiUVMXU-RcFr9RKzYRoSvZ72ceBAANL7UKVCtLz1Evq052asNSYoKQc6U9wz71vPSYTBEBlL9lHb2j77EpRjLs0hDVKHaj5Dskn5spHBtgAouxysG4szoQYSQk19_y5AKPnWYCzTwZIBmulen27lf5UJK2caSEj-INoX2XJivmIiGVoqO4vmbvYKXzqIehxwUmmY7iHVdhAnnBNN-N15VDIs5kqTe1YaWj9N0Q0Rn6dRgbBjGFJU60vQFk4-H2z0YTbcRMD6NYw4eDK_pT1Ol9pVM9ocJ8pn8la_qtPKBDc3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=dF_PkfXhM77y2MfeXgV-N05VWJyMV-JpEP88m-BgNwiUVMXU-RcFr9RKzYRoSvZ72ceBAANL7UKVCtLz1Evq052asNSYoKQc6U9wz71vPSYTBEBlL9lHb2j77EpRjLs0hDVKHaj5Dskn5spHBtgAouxysG4szoQYSQk19_y5AKPnWYCzTwZIBmulen27lf5UJK2caSEj-INoX2XJivmIiGVoqO4vmbvYKXzqIehxwUmmY7iHVdhAnnBNN-N15VDIs5kqTe1YaWj9N0Q0Rn6dRgbBjGFJU60vQFk4-H2z0YTbcRMD6NYw4eDK_pT1Ol9pVM9ocJ8pn8la_qtPKBDc3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTIrBjIMNKHmrM_u5KznizYyO2BTGym9EsrHtd_Y0VQ_yhs8rlggTIUR5UPevyENRd1BPGPKj0paXKPLyiP6e7WdYXUDdEhJf_7NNlVUmngInzlQcNW7N8bGo7mTzTlIBW7PqwCQzVCOCrwYbUlfphvFyVOspq1NmcaH8u-86huGwV_pOTqeRUj9yWGhbHwaYjHvuKp4CKyV6yqu6tA8HnviiY7sSWOoYJC3Fx9xdGsgJxvuXS7kid7OAuvFzV81fXCwkPQuRGifsc_dvBjQ2s9AWQRwU-Je6vtgQjfWnGl8tlysuezCOIek13vqNGOdb0rt4eHV6vUkIIaH5Tey8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=J-Zw1a9J0fXRosZEqGsrM8TW1krV-5nl6QxOdyXbMsd6DdFyo1RwStGd_Q4wcoZ3fcwZJiGvRX3IBB5FwAaYX-zG6nRow0FavTfMXBiK-K7N6LhQ5bR_24ytTwkvOf4n9T3YT7R1IjWFd1ksZmBAnCx-tep-osdp8-XvSNZI_DDqTYBc81MXOqpDMqQN9EVJJ3S3_u92OVSsLNULPCsQg97ZYUFASLVqQvQL7niym0cprsoWEbeq1fjo8XdzQfH9O8dSwhoMZZLuzLBAXAUpnGHJyscaJqb_NXLTCVkoecb99qiv9b8_Cyu4ZYHCNL95tdM3eXi2r5GmH8-CaO7G9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=J-Zw1a9J0fXRosZEqGsrM8TW1krV-5nl6QxOdyXbMsd6DdFyo1RwStGd_Q4wcoZ3fcwZJiGvRX3IBB5FwAaYX-zG6nRow0FavTfMXBiK-K7N6LhQ5bR_24ytTwkvOf4n9T3YT7R1IjWFd1ksZmBAnCx-tep-osdp8-XvSNZI_DDqTYBc81MXOqpDMqQN9EVJJ3S3_u92OVSsLNULPCsQg97ZYUFASLVqQvQL7niym0cprsoWEbeq1fjo8XdzQfH9O8dSwhoMZZLuzLBAXAUpnGHJyscaJqb_NXLTCVkoecb99qiv9b8_Cyu4ZYHCNL95tdM3eXi2r5GmH8-CaO7G9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=mgmNrzpVLX93zPpBHFut7UPCamdhXpiiyuPfC0TMC7rjnYMjylK95nTl7wJevVMeoqeLUfWOVT4NfJjtKnhV3WJOB7sA4GL5RbbCtveLXZAsQJZTI8SC1ONtilA_Ruay1ngWFhMBglTRvDC2f1BxGevyOSumy3K73qYjNuJC1wjsVUzaEXvKH24BsR_qhV0aQhOLtcEsfAEb1tnuL8QqrM7YK8m4snAsV3NO4JLsJTZFk5qM9xxrs8MpyqCneJzO_M8pbV0nfH0xZUno6ir_c-qVw1eGocqpLfpC1JRLGYvFx4ue-9pWkvh167E1ufYCnpWeAlaR3rcgYlFQ5O5XPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=mgmNrzpVLX93zPpBHFut7UPCamdhXpiiyuPfC0TMC7rjnYMjylK95nTl7wJevVMeoqeLUfWOVT4NfJjtKnhV3WJOB7sA4GL5RbbCtveLXZAsQJZTI8SC1ONtilA_Ruay1ngWFhMBglTRvDC2f1BxGevyOSumy3K73qYjNuJC1wjsVUzaEXvKH24BsR_qhV0aQhOLtcEsfAEb1tnuL8QqrM7YK8m4snAsV3NO4JLsJTZFk5qM9xxrs8MpyqCneJzO_M8pbV0nfH0xZUno6ir_c-qVw1eGocqpLfpC1JRLGYvFx4ue-9pWkvh167E1ufYCnpWeAlaR3rcgYlFQ5O5XPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IELar6P4sujaTndWJx1LnGiCGBU9eFEAlGKaA1GQpfDeJvZgrq3NtLr4On8NwVOlfzRHcYvrW8JBzeRcx6Enhu2zBSP49CKajTsw_Q3zgGNwBPA0ubzUs2H8_P7Duxo5YhyIPnjK9cajyZd9fZyzTSyYRqlOF5ijE4W0ZuPILfeH4IAHRMo3zzy0h6VHhcaOfppnuPxcdJRHz6uWWRAImXsI8rUiRQJ3EHJy9OX_Rwr0XFzZsLVl8ZSF64TefpgEsuC1yz8-y0iF5YZnyHZe9XITlD8OBKaupM9I-hR-pfj7G_iVHmNqGoOs_9PAPmvjf7Y1_KufAKyty_UDv8_DRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhTVogSFoR6z3D54yaDJwiJbf8nYfCFQ3vDUekQl_SNaw0gqhYBUnuR339TPiI94U7aqEmd0c6uS2pH1ExZPkQUDXH_HevR0X58OnOV5C-36oCa97NtfRjHTcUuur63jugiCr5xzSidEhB2kUuwO9dygFNLnghksiFB8bCcLCPRV2GL9RCBgp25QK2e3jn4adHOERyxA00bKWe-umazjGYZwC4P1kwOW2cwJhvemr-ezwIqLLu6g-wl4KLCyP22IYYgunx5EX3KmoHkuEwmEj6W2xlhg8WO-bV5V5uZ0Lkj25Kt54ntfvL3e6PyU1ugOOSJ9befoS4cSm7w0UjKjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KL8_BbIg_DTKgIozo2HEhVw0wFBqwJ0B7uuqPLxaQ0m37HHkV0jbvmgd3rvH4Qg7mIj1FBYQ5VqUsa0TUTdc-LU2_DEjqk80WU2bVG129pH6SFXuCW9Nyyg5U5AzQkzAlFuf8FEPLLyyVimYvJ0CR1sR5bwJoYqg0P2dI58vSM61ccaNnZhzAamAEBqXIvyShyAgPOZREXvn6i3YmhXNlgtfmPiBrnKkx8cC_av3F5ZmU2ZYzqIk_Qq5vPgPNS9beaJW72nk80WigwG35JUAMdZFzG_xR97-nTT57fyQTrCfPUJeBzlZs4VjF9epg4eKy_qoFVVPYYIH1YO1iUyKcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z-VWZ5jExq3V0uW3LceorXWzXQFhPoeA5gjqHiqTts3nGdI4Ra-MjbQk3ffmv_BFcTLbPApEQzaVjEaWIs98cNzxxckMYJtvXSJGS03ULlnwVx7zd4qGSVPefJ1C84WnZz1Eqi4Ziet6UEZdW59UHLSm2NtTkb9XQT9i_T8tN351Jvd_vlm3SNH_jwdrf_BVgOtEseGKSjl8JX4xLC7QDm7uFdeNP5Ig4XizU0MD1vX7bdxcMHGOnCAAcbOUhIEGfZdLupn5etgD2W6UziG2VWripcQZM80OcCWvnOS_jSM-nfYBOtNIEtfkaL1yivbXHyhPuUliHf5YyL8un_ZZcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NngzK1Vo4K1meqX9x-e8vamhry9WRpiWHNcyJZ5Zez5olhVD1VDM1MNUHJqsDrSbSAJjxTZJDp9Tdfs7JBK-1ARgTXS4Se7e_yP2_Dqnm950DElAmkMqiYmMBPoEOu064g8AaNrn8lxztsrzjWhIA-k-XvvWTeiG-wWUWzPwcVd24dp7lMYu8SxvAW3YSTAxHKrwYf8x6JeUlFFOuLMw0Wt69z8OVQlcUfo1p4BB5xjKvdtPsqjZPyxh0d9Fpotml1QO0W9ZJqASDb5lI0xD_YojCHwhZSPVsqgPH2wYodz0jNVlFjbahBwU6oeFuR_NWfcEO1mZZJzMvxhcJGkyVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxIzvCSETl1Kck882DeaYiBtQ7bfd-kR_uu3QNb7b6HFHQhN0drWXwpWAfgUFcpdiJ86beKhiPt6US34Z8YqszCToBGcJrSVyWMxDCSFRdaZKwBRA0sqjZX5-1TyxeK0_QmfKZeH5JOcqzxlBntvhX8mZ8tUP773xf0j8oISLojeZcQgp86uyr5NWYJsw--bNIY8i0b8gI7Y8mpjTREKvNatuhnvwmqlk4-0GZkzECAO3A_FUXNcOSx7CSuKKLW79OR-tb8uKwtwt_mkrmLTkNoAYE2vtu0OgCEx4vzwnr96ytW-IuplIT9x7u7NRllHfK2B-8G4ZNXFCN5KbcxUfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3XNdyfhskZ59YJ_kMzSt2oE8-dcvPQxy7vLAQqTYRdlYPWRH4diPHOjsy0A5yUT-VRIlKuIDw97OBbFAab7dH-c6hmxuf1atFwOFfa2QFZfPvPIyLMZUpap660V0nAlLd8jw88jwR3as8s4iC41LfZ1byh_6Xl5qk01yMe2dVAMBtSCmyDEqpx_eV3Ov_kGvF0vUtcbLnGrz4HO_rqFI2FBTm1Q4kSj9YyFQ71FWbkNWIPPAABZcJJHT9elP7r4jc5sw4pFJuKMC7wB9HTnzBxqrpJSYwws_vPGLAEqOS1KOCC6PW9gN6YKgR_2gP6UP5kD07XEJjl-W2QZck_N-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AGc0G2NvUAYa9t8If-y8mnp40U6OzORfsdq7Hlq1HKHnc5jIJX-oyeb4FGk9KpuWQXGC0z36JpaWSeybUsf67WrDIppK7ELXRyjB2zodPrhtCWwI_tchiW9V2-fzx8M9-5bQnhjtVGyyVCF9fxiHL9oq6Ju0kDZoRGRwCmYPu2GV7sOCkUvYYgYbWBm4QIWZmkRWwzycVw0dHhkT8kynozihbH1w2OQeu8Xw8t5ys0e2g4YbA9GMZuvTiQEK9Djhv9jmv14cdxUTDcyS6dOYqxRPS7hXjsSBcMwz8NcupnEYQeQxyQQD4Ctei_cZXua-h6Cr2WLCxASsbWxTau_izg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/StKARlR9FKxeqPrLM6WVw8a7F9cX_hfjAqhGo9rQU2-1495zFavmrOVYpdZ0e8VH0P9LH_YvF4iL7oyIXUk1rytdXcfinexE5vh9QoqCmqsuUi1nlIH6w1ay09kR5IcV73SLO7z8MFzE2K7SCYtZak5Q2ZQyMjWnCH9r4jVaObpAXK7bniGU2lVDiFlMrKlTA7lsg_UqyyhWJPAaxC2M99TPKx4ODDpJ9dSvdhrAewTGZK316LBUtxTvYz-k3D5EcG4NghkfouTFXWg29Nh9J1TscHFM5UfVjxIK7lck8HJ8WJt-L9czXFopgpzeVK562CNiHA9RVZG8Mq7Pc-pT9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buHS0n4yoBTtGiQHConAySpoF4S9DXeDMjH9qsJtDnhAZGN_-feFtHuBjUFBzW_foYdwfkHmc4Al7oIPgg170s3cOYZ-PHI6bV9xUarZE96f66wRdLCWj_AJ0clEojno3Qts1Gg1lfQpYkqhks7ABJaHh0tfY3wxKgjh81M_DZz9zT6XbFa9DfJf8ozrz4umxGIpk0HXkzXlDggmvRpp3_wmybGl8dxMQuxkGzjyp61Ms5n3wOugVCReWjmFqnXhpuxglGA6pgjHSMHod4yVB-S14v8DTnPCqVRnCRN9TMkVNknya_CpzE9JWQcBKFZKkUbMTvBzjjZ77Dpb322glg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVkHL5Aj15w7iOcb5Qg7SVtkmxT6pnG6JlbTuQ5v5SBIG1D3gWUFxyUojEC9nKNyoSSW0CWOMl0FgBnawfXs7EkmsZ_sZmRn8V9us3vyeHL8v-71I3F8-QHdLVE2QYxCnbv4CE711lP4Ug9LFS50a853fpQIZ_w3shFbTU4_BCDYwzeoU2Dx3EllSZ2hfieSLqRGErb1TqeA6ZnfAiOV0x_dJlCd6QQkMLO9K3Ck41VVXwL4fthPcK3lZT70CBwOm6GuBwYZgfZl-dKYmeU2jmTQ5G5GgimqDYwZgDy7lRZdQ9fuCTDmawc7jaw_S5RG-wqHugWPksV8btj5V9U3rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVtRyCp0G2AXMf1Skx1TGt5HLUxLxjpQULMex8ijp1KeqehRMKYjPvcaUQO7RCEX3goze4u7IBZSU1Jvl3X-_13UQ0OEKwgAX2hAB4LC3ra4laZaDo3Sa61yntcMnV5qcP29fI3Tz_25RDJRkN-UChdv1rV-0E7nRacAJHWOQ4n9uH-oB9CFZ1oWX133tyBB4MG-m2Chpk2HvM36G_CEKBrUzBwdVgQngLSros3ezj3b6iC0CVSi70TvJfaS4mkcUCqBOSdya27jPBP_yeAt9qatDW3MTYv265eyosqHC2ukDJiut2WHGmKtGhXUlfP2NR593iUQnan9KGLoII47dQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Q51y9mahyotZV2cpvPsyAHLo9fVfFcfBUxDwbWCpctwoKoOiX6AlUeqqd-1tEb_imcf39t6RFBK6e_gcFXN01tkuH_T0OmlHir0N6ESqn2NDiOoZW9G1OyGDTYJugBD_BeW9galiqLcfJpVdxNjUPya4pu3zlMdqOLYY6Mp4luzuDtGTKLEnFzX61hoQjYdpfmEo9NQrJeI3RsNzPmP2C_gqDPmNnnpPNA0sDs24dWZSDY0oKZrtXJfMXdKO8O_z_NxGzSE5kRF7sIZt5tpGXQYDoWwwMBmY1l9r5YMGDslKXAScvhc0LENUSBZ0jzXWSU9dT9bwCvATnwBjZvgOTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=Q51y9mahyotZV2cpvPsyAHLo9fVfFcfBUxDwbWCpctwoKoOiX6AlUeqqd-1tEb_imcf39t6RFBK6e_gcFXN01tkuH_T0OmlHir0N6ESqn2NDiOoZW9G1OyGDTYJugBD_BeW9galiqLcfJpVdxNjUPya4pu3zlMdqOLYY6Mp4luzuDtGTKLEnFzX61hoQjYdpfmEo9NQrJeI3RsNzPmP2C_gqDPmNnnpPNA0sDs24dWZSDY0oKZrtXJfMXdKO8O_z_NxGzSE5kRF7sIZt5tpGXQYDoWwwMBmY1l9r5YMGDslKXAScvhc0LENUSBZ0jzXWSU9dT9bwCvATnwBjZvgOTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=gGlxQYM9734FP6bq2gxIgfcPflZV-8mbWTUqgfx975nCO2r08M-FSXfgx7HYtY_ORJZ_PESKJsT7i4p9_q0zE7MSkQJXxeYtVyoZS6exdKccQqAR2LInIc5WpV44JaF5IKa-CxOlBkrYBfNZU3pIADo5IWfQ3Tor65eZ7X0K9AT7lthFIpfDgx7ZjQ_Aasmls8UfH1UR0aNlGOa1U32xf2htS5VS2tT9hlQPBPigdJV56hVJSzLcllcloWkFfMKvbYMTAs_IjBmwciI2uFXQfZ6VjwoPgGZbXk_Vwqs7kXIqUrAvD-8mM_GlPjWzymalqxe2CJ6clj1CeGDytotu1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=gGlxQYM9734FP6bq2gxIgfcPflZV-8mbWTUqgfx975nCO2r08M-FSXfgx7HYtY_ORJZ_PESKJsT7i4p9_q0zE7MSkQJXxeYtVyoZS6exdKccQqAR2LInIc5WpV44JaF5IKa-CxOlBkrYBfNZU3pIADo5IWfQ3Tor65eZ7X0K9AT7lthFIpfDgx7ZjQ_Aasmls8UfH1UR0aNlGOa1U32xf2htS5VS2tT9hlQPBPigdJV56hVJSzLcllcloWkFfMKvbYMTAs_IjBmwciI2uFXQfZ6VjwoPgGZbXk_Vwqs7kXIqUrAvD-8mM_GlPjWzymalqxe2CJ6clj1CeGDytotu1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=avPVYLg8oHlXD9dgSgihBO6wez02Spem8rxEqn1kQW1JoPm58hgP-KHYCCbkkOgKBZjIqKIhlEKHfcWjUDiBlwZl7JpFXlq0xkPcjWDouCl7_MolehGK7RmcKBpYQpnZiUHaeiCI80tm4ZObFKUyQmKM3EFgEHYNx4y53gl2msntQYjlgGEXK2j8irIhoGZscQmwMXL_MjA-PeqikMbw2NVu6XB_4j2EWOrv25GjLld5TP_1m1DAkM-ls4478lxw6K64tZ0W2jdIM-4nByJVZLQkjq8TLbPcRIIlLY4csFvdDJjpF6OFl_eSBokD-EotxukhgDUACszMICOEitjFcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=avPVYLg8oHlXD9dgSgihBO6wez02Spem8rxEqn1kQW1JoPm58hgP-KHYCCbkkOgKBZjIqKIhlEKHfcWjUDiBlwZl7JpFXlq0xkPcjWDouCl7_MolehGK7RmcKBpYQpnZiUHaeiCI80tm4ZObFKUyQmKM3EFgEHYNx4y53gl2msntQYjlgGEXK2j8irIhoGZscQmwMXL_MjA-PeqikMbw2NVu6XB_4j2EWOrv25GjLld5TP_1m1DAkM-ls4478lxw6K64tZ0W2jdIM-4nByJVZLQkjq8TLbPcRIIlLY4csFvdDJjpF6OFl_eSBokD-EotxukhgDUACszMICOEitjFcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=mdFJwmSnTiWb_o1ievE2MwzKVPnF_zKnSINlMm3e4JzJJ3T5Jc_auBCTT8ycG7nOp_KRTjnHSRPGfrP4nTx32eC9Aoh97f_24-qm96274TZmENQvz6otllEaimqk0-rZ-sGZ4CTPvPcliiDh6vIVRn27VjseHQgsfEUogiYP0h3vImQ3lr7bi6WidgUbX4XarqPjEc43jXimE5p5xh0dbqM0w7ekefR1kaCzGfsLjtQ9LrqIYi295bwzbc_23bLO4PfV37iVB7Sm2ImYRfF3wBaJnOdFlx_6n6RJkYrfGIbKmaFZEu7f_28qnBMIHPcJyE7C8CTZ5K5-MFPhXVODQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=mdFJwmSnTiWb_o1ievE2MwzKVPnF_zKnSINlMm3e4JzJJ3T5Jc_auBCTT8ycG7nOp_KRTjnHSRPGfrP4nTx32eC9Aoh97f_24-qm96274TZmENQvz6otllEaimqk0-rZ-sGZ4CTPvPcliiDh6vIVRn27VjseHQgsfEUogiYP0h3vImQ3lr7bi6WidgUbX4XarqPjEc43jXimE5p5xh0dbqM0w7ekefR1kaCzGfsLjtQ9LrqIYi295bwzbc_23bLO4PfV37iVB7Sm2ImYRfF3wBaJnOdFlx_6n6RJkYrfGIbKmaFZEu7f_28qnBMIHPcJyE7C8CTZ5K5-MFPhXVODQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=QimHcVxFYydV0kjKn2A9rUcc7j2Fs_OU4RblSK5CJZEnR6TKpWr9YsDji1IeZuVkU1mTH3K_4BHT48Pkg4G5Qlei3B60yWIONLR8o6RbFt1Oo-3WxH_EfU-myhtNLU_GRs7ghwW5Ce6u17CS88QIIfN0X6KX1l9zOp3uYFx7kowD3h74we4GofLIDeDN6XBtXucnfWGcnEpdOXM3G3Yfw6skCZ1ioV9ZTRpD1xwiaYRpvwbgyqQKQvkgTQTUr2uK8Z3BecTnH-n7MIaBhR-zBrwvK9uz99kJQcBflEu4O6IPJ3YswvrEbC0g5G32UrXY9X7Bq91Tc2SGbXMgfhS_ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=QimHcVxFYydV0kjKn2A9rUcc7j2Fs_OU4RblSK5CJZEnR6TKpWr9YsDji1IeZuVkU1mTH3K_4BHT48Pkg4G5Qlei3B60yWIONLR8o6RbFt1Oo-3WxH_EfU-myhtNLU_GRs7ghwW5Ce6u17CS88QIIfN0X6KX1l9zOp3uYFx7kowD3h74we4GofLIDeDN6XBtXucnfWGcnEpdOXM3G3Yfw6skCZ1ioV9ZTRpD1xwiaYRpvwbgyqQKQvkgTQTUr2uK8Z3BecTnH-n7MIaBhR-zBrwvK9uz99kJQcBflEu4O6IPJ3YswvrEbC0g5G32UrXY9X7Bq91Tc2SGbXMgfhS_ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=CJWZkZEz5wqL75ywww96hVC1FDEHrQYmlR6pOzx5yiHNvZwpzaFj6dHVRyRc-teszw9ubPMq058Q5HMAaCUKkDTVMUDnaLoKPaui6Ocp5uShBYAgcQlfhuJV9woZP_VohN8A9xBv52iG71OSpWtYDknt81ktFUuq_XLPbTbrsHJx75IoHeCGchCnYEeeRBaXvzk34cxyLVuA_L1UsIkULXscHpqDlzCgjprmQaiRr2VTa0Hp-012KWX2d6j7zTawYVOfnxYBKBliLu5radYbp_mg71YTaBp_-zp4wNE_nCHU4-oFKcWZMRQxc74jCMN44uACKka5Yinya7lT7DWH4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=CJWZkZEz5wqL75ywww96hVC1FDEHrQYmlR6pOzx5yiHNvZwpzaFj6dHVRyRc-teszw9ubPMq058Q5HMAaCUKkDTVMUDnaLoKPaui6Ocp5uShBYAgcQlfhuJV9woZP_VohN8A9xBv52iG71OSpWtYDknt81ktFUuq_XLPbTbrsHJx75IoHeCGchCnYEeeRBaXvzk34cxyLVuA_L1UsIkULXscHpqDlzCgjprmQaiRr2VTa0Hp-012KWX2d6j7zTawYVOfnxYBKBliLu5radYbp_mg71YTaBp_-zp4wNE_nCHU4-oFKcWZMRQxc74jCMN44uACKka5Yinya7lT7DWH4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=E65Q8uCMVvY5e_h2qpnzMrcOnLXWjEGElqFvuC7YISiJxi-np6jWAlClISzqn0qrWIH-fSCKS8P8bY_jHseFe0igTmDUASn8Q4MR8OxQWKRKQ-fB1sAvQnyg0WAo0pj3Q3uwGUSIoJm6o_7izHbvKCzvHxQkzDpF5SDrYIIc5psndFKzpjX_LFxWVeH1KuiNtIup8Qcli7NX3dGJD3-QuziGJqCMiYPvgJy8w8hZRVYiR-D6fivjqzw5dnH11OfnF3of0moyT6J9zO9eo_X0PjKWkX6Mq0uz4lxuAyeG6iY1kNN_BXw4XJBIt1EG5umi064A22YpNjY6wbZPBVewlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=E65Q8uCMVvY5e_h2qpnzMrcOnLXWjEGElqFvuC7YISiJxi-np6jWAlClISzqn0qrWIH-fSCKS8P8bY_jHseFe0igTmDUASn8Q4MR8OxQWKRKQ-fB1sAvQnyg0WAo0pj3Q3uwGUSIoJm6o_7izHbvKCzvHxQkzDpF5SDrYIIc5psndFKzpjX_LFxWVeH1KuiNtIup8Qcli7NX3dGJD3-QuziGJqCMiYPvgJy8w8hZRVYiR-D6fivjqzw5dnH11OfnF3of0moyT6J9zO9eo_X0PjKWkX6Mq0uz4lxuAyeG6iY1kNN_BXw4XJBIt1EG5umi064A22YpNjY6wbZPBVewlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHOZ0ewqCowAHV82fLXeqp65yWBQ1o8wQbB8PvLQeZHLeMnWYG5C4lRy-AAadpV2aavy8IngHi6tEUjpEFnIQb8l0zNIbvQlp2Ok-40TFI1EVOS7OHIo5Ry19dio7nEV-n6G2ZFk6qVQyZi5eQq6mZ8xEVvWBx1-dM_bv2glzB1clV95cfb4Tz8vE-PAc1sJfdjcbblvJpjVIpkM9ppV6R5IUatAmLTKwK9rhvkxc8zZYtQQy4yF2FqLrEImrCUtL662c7gTbMiOMhlu8bWYbPeINuifM5KyzCERaJACFaOCUvikK9fOSPjLYkOAUFHWzsL_RohHUBWgg-RnnfGByg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=A0SOL-S5NlVH0ABUq0qvLakHkSJW24AnhQy2Ty5oMwf_Bjx_ekSCKEk1s_4TbCi16DmSpgO83lNxEjYfmbkOU9nIQAVGxTI_aRaSXirCF3urLabYfs_98y01f3pGN90MmHjRv8-BInsTI0vhASB2gdVf2_jS_VCPVDgJrZxsHH6pb5N_x26Y9HQkxFCiZwe78AcSLAbGHSytrvYSWgMMjVVJ-a-61X23UCs_xxGR-MSDsQ9NrhBciUkOT8F_9KjcktCelNtQKexKggWOLNFre-2QQ0QYjVrgk_BBJwQxJ8o505L_HNIl2abg4y0uy0Am5n8ILozj9kkkM5H2xDa_iA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=A0SOL-S5NlVH0ABUq0qvLakHkSJW24AnhQy2Ty5oMwf_Bjx_ekSCKEk1s_4TbCi16DmSpgO83lNxEjYfmbkOU9nIQAVGxTI_aRaSXirCF3urLabYfs_98y01f3pGN90MmHjRv8-BInsTI0vhASB2gdVf2_jS_VCPVDgJrZxsHH6pb5N_x26Y9HQkxFCiZwe78AcSLAbGHSytrvYSWgMMjVVJ-a-61X23UCs_xxGR-MSDsQ9NrhBciUkOT8F_9KjcktCelNtQKexKggWOLNFre-2QQ0QYjVrgk_BBJwQxJ8o505L_HNIl2abg4y0uy0Am5n8ILozj9kkkM5H2xDa_iA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ee4jTzo6QRrBoSMMBwIVf74d1VtJqg3de5BA08EKOZXNs61CqiKTwaDetfgfzW0glGZYpqhakqichhNuI3b7ACuXEDg8IEplsVVXc9ZgNpGXh3NxnePotA5yKZ8F25kSd0XqjvHzCrJwipXjepR4gmSnCPogTZFsYR5Xe2XHTfyTNNtIXRS57qOtHEzgyrAuqayrrqiNFyu4Hb0FgqMQ2ETMaV8aa4ldDAlQw2sgXX9ypZ2tUNOk6dVD0Xf_y_PCpfku9g8vWRjC7IepZUHzXbXbModI3zjlyOlfrNbmINP_1E9GhGn5UQNfVPQ7tHT-e6NXZEyYfTCro3AOYA_QAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=ee4jTzo6QRrBoSMMBwIVf74d1VtJqg3de5BA08EKOZXNs61CqiKTwaDetfgfzW0glGZYpqhakqichhNuI3b7ACuXEDg8IEplsVVXc9ZgNpGXh3NxnePotA5yKZ8F25kSd0XqjvHzCrJwipXjepR4gmSnCPogTZFsYR5Xe2XHTfyTNNtIXRS57qOtHEzgyrAuqayrrqiNFyu4Hb0FgqMQ2ETMaV8aa4ldDAlQw2sgXX9ypZ2tUNOk6dVD0Xf_y_PCpfku9g8vWRjC7IepZUHzXbXbModI3zjlyOlfrNbmINP_1E9GhGn5UQNfVPQ7tHT-e6NXZEyYfTCro3AOYA_QAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=Qy8BDJpbehBpVlEQ2nGv-Nbs_utpEGkorNn2BA_ZxuWYeTPikODOMpeJAqKIyQg65UNjwNXlxsaoYbbALy8jcDxvhx6ThGSAXNOQX50oGV1AdFjVDYOWG5EYcSrOIkcO9dH77lQ7h0Ed5jG9suo-Cq2nknl0NzHLHGjCmAkakLfQkzVcS0hZSCi5N8utYQuTsmL3yUuUvq7XNPpgaMoNEffj7hKlft8t6GpCB6KSlNgSqa0WJvca5ucNhQTzVDoRz76fEytgkaWl86YbECQDz0Bob2xKkbhFKciGRT5SD5qxCSGwyGHnHdM8OGAyIXrYzgPD7nQylAWLw84VyEBHVrEs-y4IpJAIIluUzAHZOa4s8RC6XgTxN5C5kPHwVt4c5M0Q2jvgqvbgqLZoqxleVm2HCUW1wFaS3prEdUTFMDujVDSiG5ZJ9eBk1FGu3v3KD4W1xS4nDvrp3sS866kJqcerkf944UTxyAlg70zFFYTlbiAbOhnb-zDvDPNb20DkZsO8IuqKhsmuS-DaRdAGJ4rvfZQtdTfdHLUcdfxNt-lzmv-aw5LjXN4TQo2rja2dJlj2yx1aKVLvzo82k1fDc8AabhxHUF4awTDckUCwdaH6TDGj-OLw56KL0avzBb5lDbSF7yyFibCzmIs0RCReOWC5sbb8COF7y_8gfDehaoM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=Qy8BDJpbehBpVlEQ2nGv-Nbs_utpEGkorNn2BA_ZxuWYeTPikODOMpeJAqKIyQg65UNjwNXlxsaoYbbALy8jcDxvhx6ThGSAXNOQX50oGV1AdFjVDYOWG5EYcSrOIkcO9dH77lQ7h0Ed5jG9suo-Cq2nknl0NzHLHGjCmAkakLfQkzVcS0hZSCi5N8utYQuTsmL3yUuUvq7XNPpgaMoNEffj7hKlft8t6GpCB6KSlNgSqa0WJvca5ucNhQTzVDoRz76fEytgkaWl86YbECQDz0Bob2xKkbhFKciGRT5SD5qxCSGwyGHnHdM8OGAyIXrYzgPD7nQylAWLw84VyEBHVrEs-y4IpJAIIluUzAHZOa4s8RC6XgTxN5C5kPHwVt4c5M0Q2jvgqvbgqLZoqxleVm2HCUW1wFaS3prEdUTFMDujVDSiG5ZJ9eBk1FGu3v3KD4W1xS4nDvrp3sS866kJqcerkf944UTxyAlg70zFFYTlbiAbOhnb-zDvDPNb20DkZsO8IuqKhsmuS-DaRdAGJ4rvfZQtdTfdHLUcdfxNt-lzmv-aw5LjXN4TQo2rja2dJlj2yx1aKVLvzo82k1fDc8AabhxHUF4awTDckUCwdaH6TDGj-OLw56KL0avzBb5lDbSF7yyFibCzmIs0RCReOWC5sbb8COF7y_8gfDehaoM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=pnfBP0jkvNBBv14-hJidJXDRK3ezM1sTk3xTX_YHAtRhH2jVIJOIKNqQ0B5qM6ACvsE3tGUEmzFHZgAeNPhxPvpOp4rWwwBfFyWuvLdS85FKcsDBqY53mF7evYtx5R3MOSr3ccAyG7jZku8nJLzpeL2gO_QkbofKj9SW9suc8yHtFQ9OIWaKdyDKCpXWqZ3cK37DS-6f1jBPDktV6wVrjobauCha42ErsZ4AD59MtYyJ5SJ9OlnFZAzcgGcCpSSgisClilyk_tVQPnQ1yLVZ0lbmKGMQJLS7ipCCZs7VA3jAWPUL2K_R3Udx4muk-JCkRAxovEtbo3adtgp3hCPN0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=pnfBP0jkvNBBv14-hJidJXDRK3ezM1sTk3xTX_YHAtRhH2jVIJOIKNqQ0B5qM6ACvsE3tGUEmzFHZgAeNPhxPvpOp4rWwwBfFyWuvLdS85FKcsDBqY53mF7evYtx5R3MOSr3ccAyG7jZku8nJLzpeL2gO_QkbofKj9SW9suc8yHtFQ9OIWaKdyDKCpXWqZ3cK37DS-6f1jBPDktV6wVrjobauCha42ErsZ4AD59MtYyJ5SJ9OlnFZAzcgGcCpSSgisClilyk_tVQPnQ1yLVZ0lbmKGMQJLS7ipCCZs7VA3jAWPUL2K_R3Udx4muk-JCkRAxovEtbo3adtgp3hCPN0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=PEs7nFAlNzp_cGT1Gklvv0MdM2mfRk5HUsZKpqKJmEgYd0efIhBMzoBQapbxItgefQTvwWp-94TlFdxxe_2TlhvnIOs8KpyXZptDb_PJNHHc4v7jPRPKjClSuYRj1ly1XLJaynD_W4CAVWMvCINE8_JXCWznQ4YLkodd-wnHfF8hhRyqam0ZIqtiRMKDdlMOVyH8ZxHNB-FsCx9wcUicZmaYcEJdKVw_wo0RvlKaom8S-wWsb0OdlkLiwHNeE6E4ZamjWpdYk5en1iDJ7ZPVCdKqPXi6YVfb_2mgC4Cx4wD6hT62Zqif0HRcad7oo0zcq4x8CjMDx52xUqJUOoQJ-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=PEs7nFAlNzp_cGT1Gklvv0MdM2mfRk5HUsZKpqKJmEgYd0efIhBMzoBQapbxItgefQTvwWp-94TlFdxxe_2TlhvnIOs8KpyXZptDb_PJNHHc4v7jPRPKjClSuYRj1ly1XLJaynD_W4CAVWMvCINE8_JXCWznQ4YLkodd-wnHfF8hhRyqam0ZIqtiRMKDdlMOVyH8ZxHNB-FsCx9wcUicZmaYcEJdKVw_wo0RvlKaom8S-wWsb0OdlkLiwHNeE6E4ZamjWpdYk5en1iDJ7ZPVCdKqPXi6YVfb_2mgC4Cx4wD6hT62Zqif0HRcad7oo0zcq4x8CjMDx52xUqJUOoQJ-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jklInfyAg48-s6XVlFIPtqQgATbbyHMucQzV431aCYI7y88LQmbXbwYfsj_sZH_nlttf6Y2FAOPUN2BForOcMAz-yEfVQ9CftsJyWDxs8MQkpagIJk4pS10qGjJwBR_1ghzXaOdrL3ok754TcCKHxcx2Lv4pJFqEQJpLK-eOs1UjcXJewGoO3hnhQMdbVJLz_CcgMTkxpuu3FZiJZfu40AwQaMo-VKooCP1gD-8-G9iVAYBtfQ2oqznNXm-7StfCpQwqY35kOAokPT_Dp9AvnUHiRONax4D0qTkooJUIEFK8d4LfLBg7AICrcXQ8K-Rti90rHR5WoJGKRn8a8sdDqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k-_f2tML17rJcFJ06SRv9FEP0KQ20lDlXH29O0VQrdYBymWwKy2s7Kk2apo4er5d0LVdmWiyH9DcFmbmRC2E7Vq_6vQbEgGh4iA9SXt2qeBxcWwWhbNe9tqVHknf4_xhjU5ktP2Hrvbw9UeMT_u6-evKIcV87Q6hHHE3HjvrC6FlyA835cfj05zgqcvlp5G6IoRNgr3_R3rWsTdnpE9vTDaRGiNvBQjOy-0Ef_JS7Ww9HS5QiIXY0C-7KjJGC3OapZ9SbMNbp-_ZKw0M_CN6p3blDncnE-CWXyBQm6-Vg63HPt7yuS2hg6IzqgAjEcObEY2-dlDNF2hwwymapodwyQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=EZtX80G6iiGbIdPe_C2qFRkBVVStGoscjU4cYsSznKaM_udIcTEJ-WBIUN0znKciGFSV8Xk2C9YWdChnUJzyAeL6yPrWl-Rdz2rZfBH0QxCroK4kab56Ovmx83uDtfTWXjzVNViXPFQ4aIFlLhwUIrTafKAXLON4F8wSmY46NdidQXC2AD8vYcd4w-wOAeXLgu4cqjFUZe2KncEE6IT9kSd1dS6B9T3CAd1N-4hiaAVBDalL696i-nfkKn36dPWIIFkvIJ9aPxv3Ka6I4lCGwzluBRsN6Y4DJbDiSHL7QwsMWuU5-fL0w80bLL4KD-XRR9WTbCPbq6urdRhDqprEuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=EZtX80G6iiGbIdPe_C2qFRkBVVStGoscjU4cYsSznKaM_udIcTEJ-WBIUN0znKciGFSV8Xk2C9YWdChnUJzyAeL6yPrWl-Rdz2rZfBH0QxCroK4kab56Ovmx83uDtfTWXjzVNViXPFQ4aIFlLhwUIrTafKAXLON4F8wSmY46NdidQXC2AD8vYcd4w-wOAeXLgu4cqjFUZe2KncEE6IT9kSd1dS6B9T3CAd1N-4hiaAVBDalL696i-nfkKn36dPWIIFkvIJ9aPxv3Ka6I4lCGwzluBRsN6Y4DJbDiSHL7QwsMWuU5-fL0w80bLL4KD-XRR9WTbCPbq6urdRhDqprEuYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRol41r7Pg7EiqIARDcGrxHyyYXXpmc6PhbRowYoN2VXrFSbYuq8pYgZmfLD1LmNj1HyNxPvLwYOw50kAOoaKHA7rSYsgN2nFhAUiQkjQk4kzC65iNgjpuvwcbRs1BlPbN7GKoZl3gt3XKLAurdD3qRyod0UITektHQ7wCjfADcOvRaC1rfyuYnd_CXs45xIUJGydmmHFiKLVczNUyBrHk4ZYENReNNe--FuMsEBlWq9WateXHs8t8HEQ7e2gST0F3JkA69YwT503oL9O0m04Z4SaAPD60PienSng1-Jnn4zmu59xyOhLeQcuApmaR494XiMpAPGUgwSPmPvXMwvHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HDmYXhfW5RMzz5uUyeUz0y1hqmaAmTZjMRQqTqoshhwurXU6DTZGRZWsf2_HlPs6aByrotP_AGtTf7YWbmELHh9Rfp4zVuKbW3gO5-ATXZUKNON8qB4GH_XMjpmyHlEBQrdc38GVr-Vlj5kK9v9uUusVg0NzVi1ayBz64Q-h2kOs2Ac_2Od3JvAPH7fhK4dY8C0oetAkz-KckC16lgAet2Hw9_b20gQzjw8QuPEorPNcema7taaz8BWinnwHo6OJhzETcDFpjogDHhPWDYmpEf5mTMuvtcz-OiqQTmRCBDn806KsSwSi_iWyq3bjfb8-9p_wny-J4nv9MZmWdja48Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BpuGPGrEm0fEVkwVYTP6tXyJh8qpWsKtddN_uXvY0U68MoZKMCVXw8o13A1q1flsNjaFOhcv-agv-nvV4nHddQSGj7ZNYa_eP669Qf-rFWcjU_OPwcWZSdQGvXq5gbgufgOa9utXu723xkEWDnUGLGxPD0xpGmDc69LB8Ee5swemooKL6zS0Tr7lQPtxiBYqFcrb1ygXbL4TMUWkhkvyMIg_h9ACH92fQIYwCCAdpQyYvoVGnEKVYEscsnQiTnJCiPBKFQ_NzZEBltdEgZZaQFpUs3EmLMfLmy-RztrfVK_WO9sq_u7BCT2ooJj5HbBEtnVhiGhH0EO9F1zxSlWvaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2KGeMnI1jxUZ7KrhFY2dzbFGcMMtIYMFn7Ml2u3gz-oXFLx1QSsTscdXbXnoFJYApKhVB3j_QCXTpvt5Mipp6M4rT2laT3LIBTIn5ctFtUMXl9AYaN5q5EIYxnlFEz7ke7q8K9gEnFQ30kOmBTmpByPLkyMl-prD21Ayag78y0W4htrIun4gcpUS3CF0Zopcf7P7oFcqb2s_Ve60wE-D_6Ntl9ChMoHKAZBR38irrG9oVY-460cS-sDNnEV-y9PVo9Q-3rpunyHxbRF4J9eeLNLxiRg03KI0PbY_esOtL95HieeZhTOHiVSqcec5GtyioN_Yv0qujGF-ww_O7lSsQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=rOfPRiOru_6fe1TUFLno6oYUtVyjXLQdyi33U_HSDSiOeIen09hJ5rTCNe3PSCIshTUla4Izhcg5z-SZHU8HhuTWNh-ZkRBv0-Bic572MgZ_K82OyfoehToSpL62rQtA4RXzdXRHjPThlMcad9G1fLSYjKdeAQKsbZuaHISzyfa7k4QOVMsubeX2JBjBAfw94gYo5gUGleFiM9dlpoJqq6TZdkgRmJ2Ho1yA-WSgKz4r9KCbgdZb0QsYqFNZErU54qGSgN4DRvkHNFn63T0poxpTmwZNelLrW2nIqopeiZaEXsI7s0G3FR8Cj9HQIsOaOuHfaZDcGorNvOGxeaGX0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=rOfPRiOru_6fe1TUFLno6oYUtVyjXLQdyi33U_HSDSiOeIen09hJ5rTCNe3PSCIshTUla4Izhcg5z-SZHU8HhuTWNh-ZkRBv0-Bic572MgZ_K82OyfoehToSpL62rQtA4RXzdXRHjPThlMcad9G1fLSYjKdeAQKsbZuaHISzyfa7k4QOVMsubeX2JBjBAfw94gYo5gUGleFiM9dlpoJqq6TZdkgRmJ2Ho1yA-WSgKz4r9KCbgdZb0QsYqFNZErU54qGSgN4DRvkHNFn63T0poxpTmwZNelLrW2nIqopeiZaEXsI7s0G3FR8Cj9HQIsOaOuHfaZDcGorNvOGxeaGX0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=LiUSp0Yao_PTjvpw9q3GLjl6gOpMKYHMk8BsKf-Fgy-ShY2noAe3dkN2ZMkFem2T7ZtPCFxEsMN2MqYWi2nh8Fo2BJpsfLpk1_Yo60bjYPh0C-mnuuF74EWkn390i6vTlvHFX1ARN0N7x2Si-HwpDH7nxJE49yrLS-JTC6GehI1M3PKQsic4NGvBu7W5Ub0ZbzYA2cKQabt_3If18kLgmm96Vu1zAfZYO_f5OVjGdYKygvKLSw77tkfMNu86EYqnvKarAbWQhw3JKExHgTVdQ_IDYSNdUYkYMelKtEDeWrBS9kCJZuuvpeeT1Ev6gf3V51luHmluLvkeFSVCuz5X-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=LiUSp0Yao_PTjvpw9q3GLjl6gOpMKYHMk8BsKf-Fgy-ShY2noAe3dkN2ZMkFem2T7ZtPCFxEsMN2MqYWi2nh8Fo2BJpsfLpk1_Yo60bjYPh0C-mnuuF74EWkn390i6vTlvHFX1ARN0N7x2Si-HwpDH7nxJE49yrLS-JTC6GehI1M3PKQsic4NGvBu7W5Ub0ZbzYA2cKQabt_3If18kLgmm96Vu1zAfZYO_f5OVjGdYKygvKLSw77tkfMNu86EYqnvKarAbWQhw3JKExHgTVdQ_IDYSNdUYkYMelKtEDeWrBS9kCJZuuvpeeT1Ev6gf3V51luHmluLvkeFSVCuz5X-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LWPONRzKtQNBRyUEzA0tNLbM2TS3ztMFmM2x5Ftd_vEzXGO7gmGc3EzY67yK9W3yzMk-7Np9mHFIAzGc-l1ULZa9nQtU7ML5RV5ghATq2LUgUqnGstYP6_K7YW5YGlhyhlt6rxbeUUc1jBCCLHcX8UFP_F9IbX6fTnIKcR2shd4OLE5FSmhq_cgd7v6oWHZi2nCbdc_N2D46mwmTAUQOGFfs5K8Wib4M97Vz_Ck5ngEsJOTlHR-L5m-05y4D1feBwiG25zDgChHvL7usUlFEDYKqjC3ouShmyJVl6euHlaLNMPkjt0ASnIKDRBtUNWVgRdM8CTjr5LYN6QIhxS7egw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=VbvaiO87_-snEeCHqUCT2ilrwgu2yC5IQG2ii6U81-29qeMr9XmhjFBHnnq6ycuCb0NuAz5qRrdp6Nw6Ep_d-k2P5i8dHgJ6kUzaLsjPszEMTsiMDrZVmB_psVCqzDb88INPUYB3WYf1Dw1bkOVER0A9zjuVfLBnjHInWPcRWOOkrV7VhlnY5S3_ta9Fg2kVT7Xx0dsX1v-RcS_lmd-Uv-KZzYdXYLLyY-C1XUULO7gvRx9Us9NBRLy9LlmaO_rn5OjdIjQxkPa3T36HLbAESjWIve4Tta82ggsVvObmvrS62Hzfm6wOVrcvMJmeDezA5eSuy-BxFDD3f9g7MuG9DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=VbvaiO87_-snEeCHqUCT2ilrwgu2yC5IQG2ii6U81-29qeMr9XmhjFBHnnq6ycuCb0NuAz5qRrdp6Nw6Ep_d-k2P5i8dHgJ6kUzaLsjPszEMTsiMDrZVmB_psVCqzDb88INPUYB3WYf1Dw1bkOVER0A9zjuVfLBnjHInWPcRWOOkrV7VhlnY5S3_ta9Fg2kVT7Xx0dsX1v-RcS_lmd-Uv-KZzYdXYLLyY-C1XUULO7gvRx9Us9NBRLy9LlmaO_rn5OjdIjQxkPa3T36HLbAESjWIve4Tta82ggsVvObmvrS62Hzfm6wOVrcvMJmeDezA5eSuy-BxFDD3f9g7MuG9DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=XHW_Y2dr8rh5xweP6nlgKWUo-vnos317ImmG_Fr9fVmCQAZOB2Oev7tBfmnzS8AO_RDTmCAtQnnoGLg1SGtmJ7bR1EorXg3-s2-SlrQycCM0aTBObj96-B_KY97sIr6OCi2mSteyzjJ5Mwqxc6C5fJIqsU_WIGXo-9mp3tbEnhKtglRp3XRtRAHlbZOHmg4YavBM6b2ZVhoQZYas8k8wPOEeQ-Mfvzh4ouaEdsCE6VKZtNZGygBwm1tUjMrmrDugq6tl8cPde6wjigDg3bbsHN641my3-nJQ0Ti7RSMHiB8WWS-fK2IF4bqJSBkWM-pjDJqhINkc_uzjDrjEtKcaFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=XHW_Y2dr8rh5xweP6nlgKWUo-vnos317ImmG_Fr9fVmCQAZOB2Oev7tBfmnzS8AO_RDTmCAtQnnoGLg1SGtmJ7bR1EorXg3-s2-SlrQycCM0aTBObj96-B_KY97sIr6OCi2mSteyzjJ5Mwqxc6C5fJIqsU_WIGXo-9mp3tbEnhKtglRp3XRtRAHlbZOHmg4YavBM6b2ZVhoQZYas8k8wPOEeQ-Mfvzh4ouaEdsCE6VKZtNZGygBwm1tUjMrmrDugq6tl8cPde6wjigDg3bbsHN641my3-nJQ0Ti7RSMHiB8WWS-fK2IF4bqJSBkWM-pjDJqhINkc_uzjDrjEtKcaFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=dRqlID5q_jvZ6Iq69uNU1Z_QqPO-gynQNnsugivM1qUiCzKF67anWPtL528GiLGQnL6DWRGah77te0l2PEXRF2QrZ18t5130jG8S1WN3WOGZs1U-fdtdXXeZvBdWfewWYDpTclaat-7REoywxQI--jLg-WeSLzfGV9WJTjRFZjyX3LdDL3pSv8uLSuk8pgTzrC2VcmM0c80NlAr2yEOl4Hxyqqy-fHt0eLoOMwTx7mgDGKc19dPaRqeaqRsjq2xqIXncecKzJxeCsb_t2rScaEu6A07Q0SqBDQ5zipKrIM9Y1qlj95AQp6NRFXHjbx8mFneSvFXDwtIGy58rFuJS_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=dRqlID5q_jvZ6Iq69uNU1Z_QqPO-gynQNnsugivM1qUiCzKF67anWPtL528GiLGQnL6DWRGah77te0l2PEXRF2QrZ18t5130jG8S1WN3WOGZs1U-fdtdXXeZvBdWfewWYDpTclaat-7REoywxQI--jLg-WeSLzfGV9WJTjRFZjyX3LdDL3pSv8uLSuk8pgTzrC2VcmM0c80NlAr2yEOl4Hxyqqy-fHt0eLoOMwTx7mgDGKc19dPaRqeaqRsjq2xqIXncecKzJxeCsb_t2rScaEu6A07Q0SqBDQ5zipKrIM9Y1qlj95AQp6NRFXHjbx8mFneSvFXDwtIGy58rFuJS_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fyafOoaL9Dadb_09Gervd__VjwbBfI26QOnrykhDmd7ZUY6wmVXtGg22lQfcSY9oVCjeub7iTLnRiLswptF1rqXRMG_3QtAg1cPi4KsskryjQeecihVR5m6iacSnwzPvD0lzsVB4eNUIqNAB3nIh3_QNz60hP5lyHPxLego85anisj_3RorzljEfr36nAvKF2R8PIF1D3DwMOVI34JUYCLrIDrRrWUI8OmJ1l_xlFYetv_BdocEYTGbDIoyWtbCAlS2CBBeTOxidzaUloI16h4wJJAz4J6apl-6ULdKEreaSPr7894RrWoZDImJ8JIU4ibRbuMxKB4UuhLPzZdr2Vw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=m5ySt8e5TjUjy21DBiTZkhVvutU5gZY9EpIP6YmE8eRcmOADn5G2uWwc1JOqmGm2gi3nznj0oIvDR4DX0YcTgxKXzPhh3K4NV8lkOKz8LlCI7JrQ6WW_FNPir9oFSXLiMHwG3dfeSD522Ok3BeBix9-Gy-e847P1bpeAvR8S_H4fSNJ6qWNqvZPRw0Tpvwgafc6pQWrrsl9ijLJXInLPHJYUB7sZX1Z-dSUby-wb8J6aTBXbv5f3lvLx9Z9stUOxOOwY0yX6VPb_R8Mhjdkf8kTcZOE3wpAcRf6Qlr1NAaWG1AC7C7kbWV30eTX1owfrdq_ZjXsM8DAMNw1DElWbgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=m5ySt8e5TjUjy21DBiTZkhVvutU5gZY9EpIP6YmE8eRcmOADn5G2uWwc1JOqmGm2gi3nznj0oIvDR4DX0YcTgxKXzPhh3K4NV8lkOKz8LlCI7JrQ6WW_FNPir9oFSXLiMHwG3dfeSD522Ok3BeBix9-Gy-e847P1bpeAvR8S_H4fSNJ6qWNqvZPRw0Tpvwgafc6pQWrrsl9ijLJXInLPHJYUB7sZX1Z-dSUby-wb8J6aTBXbv5f3lvLx9Z9stUOxOOwY0yX6VPb_R8Mhjdkf8kTcZOE3wpAcRf6Qlr1NAaWG1AC7C7kbWV30eTX1owfrdq_ZjXsM8DAMNw1DElWbgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6XgAiPuKyL7sWuEsvwr-SShkUO8oS4E7WvOynKGiy_dRVyXeisFaCQ9Yb4m0plUE0jErn85UuwLrJLEdf6O1bkHVcSh_-hMX3Th3I9ppApaOazqtoX1DUaxyPWI_e14nObCH4emD4XnJpkvdc6ViwutnV1MJna7GxS2HRM8l6nIg6jxM90YBHE8g-wbVcq1MssWmZlA1qDsNVWLNGaNP7MhhtK3GFULYvhKoN9kq1S82vZMyVLyT-8LVqYjlsG-6w7hcBYZ_xCcIhkfNcQTdfDZdDXH_7SKzfZ-cOdMWBc5QB3y16r6ZErbqoEwyYxQb8cvNAGwLyUvMsuMguSCWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TBYOtT9HATq1uwt4n8dY5i2QgM1VmqipkNi9eVE8tLkcCynq2kp3CfrGfTx70ICliJhDmYdEryAl4INXiD5-iYelgFM2CtKRE1V4mfArcxiNQEWPRBWPv3Bzkwxt0ZwEKGvpj-tvCXOt8ZVwWwqNL7706U41m9jQ8An-A193nqsf_rcL1qoM9e1v8aeLlvqBswsO1nTF9YghCjFkI647fCmdQvAfOyxNo_MXH8ecCQxcKDiKNsVnvxRd9fwSvb8pER5h_Ll3tORoxYI-s3jmOchTYhZSajVZxbCSV6UJLCJCh8xdJQ-kyQqUguGxl_EgYW_fDLAHYux8JcOng8HSyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=gC9FG0b90X3vtxbfe_WEFshhQpcO_A2-k6BS3X_-9_IcV4BW_eCjJIfu78yMswKAz1XjguNl8Iq9UrEN4KgRufaKnE29748FzfelzWo7tHJN4CW9cPe7uXWH1rBdfus5rc3EU9GSXkzVNwL0Y-BLY_ISxIlvcwWtDWYh-uS0MC6e2wUHDK84Xc4ophMfMwDwkjT44muDfeQ_QdoY_mZqWuD4-sRJ0ZgnmhXGa2i2KbB7IbRYKIReph1dsdAkeyRGyKCT3DKmkVWYqgYGGGRmnJXZ4M1ltRpdoD3qDWG8Kf2IsPumLllak5HFIQ68lBQK38gqw9Fb-2HCPaUl_EZemg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=gC9FG0b90X3vtxbfe_WEFshhQpcO_A2-k6BS3X_-9_IcV4BW_eCjJIfu78yMswKAz1XjguNl8Iq9UrEN4KgRufaKnE29748FzfelzWo7tHJN4CW9cPe7uXWH1rBdfus5rc3EU9GSXkzVNwL0Y-BLY_ISxIlvcwWtDWYh-uS0MC6e2wUHDK84Xc4ophMfMwDwkjT44muDfeQ_QdoY_mZqWuD4-sRJ0ZgnmhXGa2i2KbB7IbRYKIReph1dsdAkeyRGyKCT3DKmkVWYqgYGGGRmnJXZ4M1ltRpdoD3qDWG8Kf2IsPumLllak5HFIQ68lBQK38gqw9Fb-2HCPaUl_EZemg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0m7h3E94NRrQB_32S4axJUBFzozYo3kmY3vxGc3Wbq1gKDjBTAchRvYvS0LJ8S4WnhMVTdLR31aFi-_1UmQvETpycx1uLyNFLvEQ0mH9DcuYl5Ogt59CsMvPrqZgFaJJaxzdH83Ro_X04E5vqmKeCmH2XbrdhgLzV3_RT_0KJPuBqmP9GDwiQDPn79hcbnbBt9bsWyMhoaFsSTHnGX0QxCa3Q8MYzFeCkwYb6dKtDjJi9ijA3ybMA1dT0NEwaz6_pK1D9PK1cLGzRVW15EPfvQ4T9BahmM9TjEZP8Hq7sxHXKRaLwaX59vvdlSIZGkKlRHQL-sfE20eahf71QKmQr2o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0m7h3E94NRrQB_32S4axJUBFzozYo3kmY3vxGc3Wbq1gKDjBTAchRvYvS0LJ8S4WnhMVTdLR31aFi-_1UmQvETpycx1uLyNFLvEQ0mH9DcuYl5Ogt59CsMvPrqZgFaJJaxzdH83Ro_X04E5vqmKeCmH2XbrdhgLzV3_RT_0KJPuBqmP9GDwiQDPn79hcbnbBt9bsWyMhoaFsSTHnGX0QxCa3Q8MYzFeCkwYb6dKtDjJi9ijA3ybMA1dT0NEwaz6_pK1D9PK1cLGzRVW15EPfvQ4T9BahmM9TjEZP8Hq7sxHXKRaLwaX59vvdlSIZGkKlRHQL-sfE20eahf71QKmQr2o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=gOt_OaGnpt0h0tfqDnvHOSoD053ZIQjnPEa2q0_zOWmKC3R5qjjgLXohdS9ES4NXHo-MdbOxcsWfhM8qitCVoptqQTrcGXl6yzeT9sVEaLOT4Colwmr5fYuR0q2KcYuWDjP7ouLS0k-VjPcc50a8FVuPJVznb33MXY9mroQ31gLr8BQyA7uKoGBSOdzY_HyDfZbdVgoaOxrnesraQ7uENzpGazYmNksYn5OCrpD3h0o5KfGe3LRCb-UhxWgHS-6Z47b6be1EueAM7v-lwcReYCQV5G6AbqV8hiAW5heflTR7DMef_Ib3n2d1UFRSGwHTNbnFD2BERIq1yGnDFiXPzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=gOt_OaGnpt0h0tfqDnvHOSoD053ZIQjnPEa2q0_zOWmKC3R5qjjgLXohdS9ES4NXHo-MdbOxcsWfhM8qitCVoptqQTrcGXl6yzeT9sVEaLOT4Colwmr5fYuR0q2KcYuWDjP7ouLS0k-VjPcc50a8FVuPJVznb33MXY9mroQ31gLr8BQyA7uKoGBSOdzY_HyDfZbdVgoaOxrnesraQ7uENzpGazYmNksYn5OCrpD3h0o5KfGe3LRCb-UhxWgHS-6Z47b6be1EueAM7v-lwcReYCQV5G6AbqV8hiAW5heflTR7DMef_Ib3n2d1UFRSGwHTNbnFD2BERIq1yGnDFiXPzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_Zb_YQa0zntn6YgSvM4ELjfhvnxIbM3v91gO2dPXDj3qb3KnwMmtpHNWT2g6w2tJoO37oDTo8rDAK9uh4WoNWPVBEZD6vN8nvLvr_lo9OG7NcYXa79OBeRsfGa5_3swzmillmkPN-pId1Ohsut_KabI2-X5KcHGEpHFKpNEzi1hS66LisI4G1S-kWyt48fa17EIOeuobY7V8ORhmajPPr5ImkInJmgy2DXnrEujTDpQMCYwjW3INkU4l1UG6pusn1NBQrE8brNywOdvoF-CVoIzkM2KeCL7UV1dGVbFY_yEJDq4W5gg8O-oK4HnccAUKyXVsdekWJtorNTX2e2lJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=khs9RslswyZZLF0saBiMKdOHxjq1rET02fU2thwRHJN-NeU5ePYdpUnfr9sjALzsEHWJ6vphl90gmrCecgdVr06-U_TIladlSdaGfybNZSkz1fI_cFOYOtwxp3tbiJdBJMwvpEpbFYECeQfhGy-n8_cr4D4eak8CURn6faHyut4Llq001veKUx01P3xelVzX2VOfWxk5Jdz0uyejmXv3s7Un-Y-7p7W_7YCMsQIaRhtvyNf4ivJGXq0ABzLvsV6ZhWwp3SYsOYaAm7_bmsKPLYC0YhKCkPOL8UwXy0xiSSA4z18-pn2en3DeCEg7-4MPTqqalOR_UBsLZjl6xY5yOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=khs9RslswyZZLF0saBiMKdOHxjq1rET02fU2thwRHJN-NeU5ePYdpUnfr9sjALzsEHWJ6vphl90gmrCecgdVr06-U_TIladlSdaGfybNZSkz1fI_cFOYOtwxp3tbiJdBJMwvpEpbFYECeQfhGy-n8_cr4D4eak8CURn6faHyut4Llq001veKUx01P3xelVzX2VOfWxk5Jdz0uyejmXv3s7Un-Y-7p7W_7YCMsQIaRhtvyNf4ivJGXq0ABzLvsV6ZhWwp3SYsOYaAm7_bmsKPLYC0YhKCkPOL8UwXy0xiSSA4z18-pn2en3DeCEg7-4MPTqqalOR_UBsLZjl6xY5yOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=WhR4diVqu4xLrAp9y02cKzhx03oOWmkQNMk333TdYmXp9v3X13sYAMjxpHe6piYnTzk2KMXazJTElt3LoCoUMj9RAo8zmBqTOGN4hqYnK2sVCjkTmg0IJWjOwD6AlrBLhr4dOgoYi84blAodA6clGX09klhd70dWV8QF5F1gZev-WklIKTEmYRCXRKUe7y0ZXQIDJ0syXMGNvYazVCkH0gvZbtZ1YO0SN2C5izN0Us8VjIRAg4YxBfeG_zsp-oMD_5WZueJaTq3UggTYeay5OPUPISn2rZrnelV0lC4eFF4DxX2pM7lmDcq4ermrcO1ML3RWwcgYdYcHVB0gxv86lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=WhR4diVqu4xLrAp9y02cKzhx03oOWmkQNMk333TdYmXp9v3X13sYAMjxpHe6piYnTzk2KMXazJTElt3LoCoUMj9RAo8zmBqTOGN4hqYnK2sVCjkTmg0IJWjOwD6AlrBLhr4dOgoYi84blAodA6clGX09klhd70dWV8QF5F1gZev-WklIKTEmYRCXRKUe7y0ZXQIDJ0syXMGNvYazVCkH0gvZbtZ1YO0SN2C5izN0Us8VjIRAg4YxBfeG_zsp-oMD_5WZueJaTq3UggTYeay5OPUPISn2rZrnelV0lC4eFF4DxX2pM7lmDcq4ermrcO1ML3RWwcgYdYcHVB0gxv86lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=eHdtIh2GF7RJrB5120L8ocC0xMUboCAMaiwtk3cEy_LAwr0UD-vzxpdK9q4A4NzMiAXU30dJ9iCazHlvaB18N5h82BTjKneipl9Vo9wJaExnSBNEgNvw_ef-L2SSS6Tv-39sOv7OBGFvmCidOdmSfLWhQqQYCcI8jPdfgS42vCoz61ANLg3JYl2do0le3X_Q9n85eks_tod7F_Acf-rY-BlFZEbiNurHpy6v-IW8nSBf4cGHtXd_rPXj-ne5WUBgC0-FDc1eWJeeJ7EZjcEnvEiBtnOqmlZEUG0gkAc0b1CrOkOBejYNODLzU2QQRt6CAtk0FStEvAMeiwr2sNXGLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=eHdtIh2GF7RJrB5120L8ocC0xMUboCAMaiwtk3cEy_LAwr0UD-vzxpdK9q4A4NzMiAXU30dJ9iCazHlvaB18N5h82BTjKneipl9Vo9wJaExnSBNEgNvw_ef-L2SSS6Tv-39sOv7OBGFvmCidOdmSfLWhQqQYCcI8jPdfgS42vCoz61ANLg3JYl2do0le3X_Q9n85eks_tod7F_Acf-rY-BlFZEbiNurHpy6v-IW8nSBf4cGHtXd_rPXj-ne5WUBgC0-FDc1eWJeeJ7EZjcEnvEiBtnOqmlZEUG0gkAc0b1CrOkOBejYNODLzU2QQRt6CAtk0FStEvAMeiwr2sNXGLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=eq1nRHYzSmypAzm6C9aJLoqPyXO5lO1oi8JLnKnxgCzKiwRcjoRxzEgK3tVI_f6cHeMKLozZjNLc2TnUUXmg2t500wzrx8g0967xwlLdZi0LYTRbn3UJpnVdLdROeE38qE4y-NubxYNUDwCeGhgCGbp0IqyVWwJznMIO-1DAMMXxCM1yyDbwBvXTvN6gbkrxQs3sJqxsWVilyUbveGUddrY298OsAKMF0l9_MIsP1x6LkNl4S20KjXmQAkeUMiFx3T4Wkjt3dHxNlxVqJdF1kQy6hVqaTjHuDOSk6NjPRwH6I6TImdlrhkrRpL7wa3xSkBRR959FTy7e8kOxSTOKMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=eq1nRHYzSmypAzm6C9aJLoqPyXO5lO1oi8JLnKnxgCzKiwRcjoRxzEgK3tVI_f6cHeMKLozZjNLc2TnUUXmg2t500wzrx8g0967xwlLdZi0LYTRbn3UJpnVdLdROeE38qE4y-NubxYNUDwCeGhgCGbp0IqyVWwJznMIO-1DAMMXxCM1yyDbwBvXTvN6gbkrxQs3sJqxsWVilyUbveGUddrY298OsAKMF0l9_MIsP1x6LkNl4S20KjXmQAkeUMiFx3T4Wkjt3dHxNlxVqJdF1kQy6hVqaTjHuDOSk6NjPRwH6I6TImdlrhkrRpL7wa3xSkBRR959FTy7e8kOxSTOKMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWGTBPmOl26NRklTU7nGF_bo9inNQc8QbKhD9G_Ta6RKoBrURaqtH6zYU90mxCOJmFrwfa7aClSa_5YhnCJh5KDH65D7T_hwb-hS86RIe-kcI_6nAAitmxuD3g7c2Hwpbqoj0neefhR5vdHGCSA4e3YjgS9lzIz4NbrvKiBZw5Wwxm4oBPD0xWM1VVHtPlMOEIZQFeOfYeXOr6ubLW-uH-TwCdsHRewz7kedK0jbjuHjl6y8O8a6cQLEX8d3OAgUbMIGm2DD9lEmlmB5X5wxh8kosx9N0jBliQ8ig1X4HG__ykz115xu7mIIQFuERbCHgPUu9EiHPV11So2lFF0HMw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=B9R5ZbzBOWo7g-codGNE9owXK-37cnOCZu1rTTJmQY6S38Df4I2ai8RYtwhE2iy41_Eruv5iPrTkURl_m88s3kcpvoG0yojeg1jAxnw-9VxDj0r2YcX9KjITLJWNfsBJ_bQ89kZjvles-HpvgWdtSz0DMWb9S4mLRFfysfhq2kxeqDeOh3J4QTu-DjvnotGeftPiSuZZt9TQFWMrRTc6AteS9tyKZvy3v5xY8OgfNxaxrQARkqFuwArqmUM4DcDuFDA7esc987yJsnkuNFqwgyBBSCeLgom85YI7sZs43HH0U7SWQF5QxBLSQ_G4R3zyEyjoBE-kRSRyQAsBDaEYow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=B9R5ZbzBOWo7g-codGNE9owXK-37cnOCZu1rTTJmQY6S38Df4I2ai8RYtwhE2iy41_Eruv5iPrTkURl_m88s3kcpvoG0yojeg1jAxnw-9VxDj0r2YcX9KjITLJWNfsBJ_bQ89kZjvles-HpvgWdtSz0DMWb9S4mLRFfysfhq2kxeqDeOh3J4QTu-DjvnotGeftPiSuZZt9TQFWMrRTc6AteS9tyKZvy3v5xY8OgfNxaxrQARkqFuwArqmUM4DcDuFDA7esc987yJsnkuNFqwgyBBSCeLgom85YI7sZs43HH0U7SWQF5QxBLSQ_G4R3zyEyjoBE-kRSRyQAsBDaEYow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=uvHN4gchPQlHv2MWfTZMsb-SLgvFpo0rp_B_TFz_Ut3SVlFu9_we6jTj9tdA02gmJm8CHLkvU1bcw0o3jvvfyDkVDVuuv1bULDo8sSHNpmKgM9qAPRcGNhZmnShqFAuUX8OVCI9H6G9LvtMlmMDsfBLwGwM79pl4uyaBKi-I3XN1K3n6NXtLjbuNl-6tuNZIUyfEWgh_6bFonxu_vk2UquOfY4H7sqrPluhA_XxohmL6yEMJv3pBvJAy9_z_J4qDrhMYtW1GeObL7sEUqPLSyzoOZH2r78Oe-5ayB4ky8eOXEqTbqJKyiABMn649xvP_ASAbiepXknFxdfOLv2hZ_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=uvHN4gchPQlHv2MWfTZMsb-SLgvFpo0rp_B_TFz_Ut3SVlFu9_we6jTj9tdA02gmJm8CHLkvU1bcw0o3jvvfyDkVDVuuv1bULDo8sSHNpmKgM9qAPRcGNhZmnShqFAuUX8OVCI9H6G9LvtMlmMDsfBLwGwM79pl4uyaBKi-I3XN1K3n6NXtLjbuNl-6tuNZIUyfEWgh_6bFonxu_vk2UquOfY4H7sqrPluhA_XxohmL6yEMJv3pBvJAy9_z_J4qDrhMYtW1GeObL7sEUqPLSyzoOZH2r78Oe-5ayB4ky8eOXEqTbqJKyiABMn649xvP_ASAbiepXknFxdfOLv2hZ_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQzPtkov8TTFvn8NQwoWzshyMc8n9XArsEAUsEqM1RVj6sreHOXlJJN8cbJHFt5DoA_TMFThyBYCzjnuBxm1iRSeT-QN99etaIrkk9B3TWv8JlPIOaCzIEEfbL-_3Rm6BSNheD92uL5wti2KqhCTcJw2wuM6bavLx3An0q75XNiEQJreV4e7pTcYnStqLrg4gDemSQUhUbEBF1MuHlUsJosEjkDNiKol-yerSv7NggxoQHACB4jr9t6Sb-dCsXHii00hMHlQvmEoN3WlcWff7Q6OkEtGM1tqVpAy9bdbIRxJZjG_T5ZtZVi8sIycY-KietJXSlb3e_3dX-cg9b-u1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MS7I1OZnO4uRSbXJA5L2MKRyvLxcXa2LjulJlOuTYRd8VWxLHuOe8H1RoFQtc82ubs6E3bMZnOpmXW7iPHDcSHmZYKuF6sLGc42c06B34YS4Gjn460KFTNRz2AdwPGr-MaYdCrUy2hVR6HGQf3jSVm9AGVuNfT3qwWbFIvCR11pLCC7WILbSvbYqI1FIHGtcw7kwnsYa4IgM8Aq0q-s54CjGmaNcCV_I4lso8sYzhMXpo5FghrFTsgZT3-S7JQjwCHaNmHB6sqGbCeQz-b60PfbXPV2xNM3Nva3xUBDaqu-kCrKJ8tpiNqOSo2yM5vltaDNdxoeqtrdiEvtahLtTdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MS7I1OZnO4uRSbXJA5L2MKRyvLxcXa2LjulJlOuTYRd8VWxLHuOe8H1RoFQtc82ubs6E3bMZnOpmXW7iPHDcSHmZYKuF6sLGc42c06B34YS4Gjn460KFTNRz2AdwPGr-MaYdCrUy2hVR6HGQf3jSVm9AGVuNfT3qwWbFIvCR11pLCC7WILbSvbYqI1FIHGtcw7kwnsYa4IgM8Aq0q-s54CjGmaNcCV_I4lso8sYzhMXpo5FghrFTsgZT3-S7JQjwCHaNmHB6sqGbCeQz-b60PfbXPV2xNM3Nva3xUBDaqu-kCrKJ8tpiNqOSo2yM5vltaDNdxoeqtrdiEvtahLtTdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=F5pdKOODPfr1O9REJYmz9-ZBTetSiKazSpyJfvgoWlhMi1ZWeXysh8rv3-naA0K8KAga0iiJAUzeTbYnd9XOGfAZjDgPpztxQx6zmYcFhPHspJFV-ulzQoorSgXnHFbXwPD57S8L4UKXvdqIbpmifsp-f45eVwuR3wFhXE34WVZTCQkkuYglTTgZ6txpctUDaMhi4btlLG0X7SrngFSZr3pkjxjgLArvOGKr2i0h3hPmHe5tMD1yimnh_nmNkSj_2ojV84BNzMgmYXiQ4kwDBhbzUZfu2HAdTxI6g44oOacLRcEC27r0vZVUqrX5Guqdn8y9bs_nGs7V1ICTqb4GBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=F5pdKOODPfr1O9REJYmz9-ZBTetSiKazSpyJfvgoWlhMi1ZWeXysh8rv3-naA0K8KAga0iiJAUzeTbYnd9XOGfAZjDgPpztxQx6zmYcFhPHspJFV-ulzQoorSgXnHFbXwPD57S8L4UKXvdqIbpmifsp-f45eVwuR3wFhXE34WVZTCQkkuYglTTgZ6txpctUDaMhi4btlLG0X7SrngFSZr3pkjxjgLArvOGKr2i0h3hPmHe5tMD1yimnh_nmNkSj_2ojV84BNzMgmYXiQ4kwDBhbzUZfu2HAdTxI6g44oOacLRcEC27r0vZVUqrX5Guqdn8y9bs_nGs7V1ICTqb4GBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=UW6HyPpCWX-8v2bcb8iRxIjUGTrUWtObq_Zv3OYfLQm0CkrMya0svONyNazRfsE7CXcYDW9VJdex46YQlj9zIgx6GCVDpzQW_V4h91rKDluGsxWN151_vq7oCCD6GIeDL5lwa8pxVT6B-2wVJVHBZFkDlmL7VYbFFw7glIInaOUdlmIoJcSiYjxAYQtqgrl3vWbI3b6pCr1ca3zVtfHxkSpbpkl2PLIbOgUzmstgcwXuYRS4BHh_cOz5RU2v50bmmN3UuTEjujkEYfthqTXtlJ4MsSRboDsPFlCgxj58B_MfXSfe6CBFTgMuqMSB87GeFhQn8W5dPnmr635OunljVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=UW6HyPpCWX-8v2bcb8iRxIjUGTrUWtObq_Zv3OYfLQm0CkrMya0svONyNazRfsE7CXcYDW9VJdex46YQlj9zIgx6GCVDpzQW_V4h91rKDluGsxWN151_vq7oCCD6GIeDL5lwa8pxVT6B-2wVJVHBZFkDlmL7VYbFFw7glIInaOUdlmIoJcSiYjxAYQtqgrl3vWbI3b6pCr1ca3zVtfHxkSpbpkl2PLIbOgUzmstgcwXuYRS4BHh_cOz5RU2v50bmmN3UuTEjujkEYfthqTXtlJ4MsSRboDsPFlCgxj58B_MfXSfe6CBFTgMuqMSB87GeFhQn8W5dPnmr635OunljVDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J_JFtf2koxyVpT4mQXipJuGG5abv4nlkU-9TyuYxkx5XrUdgsfLtbxdAOo18Wsxka4LIeybkYYqYp1MQcJu8KA2rkkqgmyg8HrtOqMwk2We8WMZCIquMYSIGC6gUqnQjRewMpqotQL2Vjwe2_wK9c6m0pYDpw2Pgw5I7V3VKhlDI1H_uJA6enf5AmLGSk7TMB-GASZ3xfDAoA3_RcoFCsAre50Jlh1bihkljrEt1CNS5s0h4aRDeFB1jiZnDbLWs8wgzlhfoZ7DNZVnUJH8vjJwj06wA4zu8R3kJHcM0qQx2BIX_jaa5ySnJitUidGo5T7yug4AM0aSLWlUPxwYkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NyyFHhreMqwT0pyyPyVKXO9C-wska87Q9yhScO1P1rtTx_8jcZWUMiKgfZ46RLyYnExyASAlJU7egR2B7Og74Tgwq0VJfVoVL4LxL7qpnthrm8oChfdaWZXTyrRoECAW6xGnAMJQ9poyNZHgUPy8K0H7LX_zczvNOw_2p6sPEHbzedfT35ETghCzPwDNsKNwfPWgRRieibG4Fuf-xXcWRDg_V9NvKIt1yR7RlPirMTKhcK_dLpCKbOrY0arbTtUCxfDvsxkyRbeEIMgdLvmXvoZP4IHbt_MtPHKFlXRBYVULtmZQQTVTEVbY1BKEfe7o3vJ74cVOVAThue91TCmt7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uEn17_1W3JGAj8Byiet-sW4DVNC-qPl05MzAouSxiIo3nSPVh5I5p1F0mz_CVPrPbnjFIK1m7XAluLbdMmhBNX8Jgz2jTBqkpo7fkGghwcmwf3arC2Rz-lDTz2TE_NfTL8FdaVbQ83X5MHhUd_Of2Qx59yNF0cp0vtfAoksNifkIuSqCUlZPt8QpeTiZxEpfl83-sabRoo_uub0xCRv7dIfWnkchZrIdjc_GyYYTIheFP93w_vTvXtiVGNA68swLzThG94ihzdyBYpsCqMgVbJ5aCfvQTdWAYm3Z62UyuXzs81J7ngZiwLDxJg64-4HP6KiQItyzFbD3GHVjr2m9xw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=NFRIkCE35KSgSjJ8vj1yGa3hF-BpQL8GLNJm3Jq7FfqjI-5FwbKf8foOuR94suFwDPHDC85iwU15bIn4d3DFEnE7j07T8OCbzZ5h3EmhNqPObSSWe4Ctz4bk8UjRVoQkXb37JBibRs3eVTmPc-zGz4460gGb9XaB-AqUEOlRl0P2V8V6PIGvLFSSSTr6Yvd7ZNlo4cACZhWQ52AyKCSJXsM9EBiEzAE-DazHHzAFUD6Y9j3Ex_OaRRUlVF8DwlwQRHz-x0zO0wX-kBg0znx-L4qoM8qMam-zx7Qt35f77vZUamzgUHQLwXeKaavury5CdPQs_BNIoZeJAn1VHmd8lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=NFRIkCE35KSgSjJ8vj1yGa3hF-BpQL8GLNJm3Jq7FfqjI-5FwbKf8foOuR94suFwDPHDC85iwU15bIn4d3DFEnE7j07T8OCbzZ5h3EmhNqPObSSWe4Ctz4bk8UjRVoQkXb37JBibRs3eVTmPc-zGz4460gGb9XaB-AqUEOlRl0P2V8V6PIGvLFSSSTr6Yvd7ZNlo4cACZhWQ52AyKCSJXsM9EBiEzAE-DazHHzAFUD6Y9j3Ex_OaRRUlVF8DwlwQRHz-x0zO0wX-kBg0znx-L4qoM8qMam-zx7Qt35f77vZUamzgUHQLwXeKaavury5CdPQs_BNIoZeJAn1VHmd8lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZ3pdzkMmmybhDjZ7EJiSwkSc9yGaD1yMnYLNfaJD_HShWIq8gluUznRZvN5sTQoedwrVT7CVtSuc7vITtJOsqjXmHU9R0rClF1rzoZbKiu2n17TOgeaJQRnLS9lWAnNrJp55vLtK5JNDdmVzgaKgCIeaWgXaZc71fBjgqUeu8Tp9bjmyorpwgfsufXvsYEosT-8-V0h53cMz55TYWXKbTA4zemA3muOrkB7cfP7w7ESV9tFYbeHXcRl1L2WHzlYgpamUj-Rnn0_iymeh-ipD2Z0VHoxmSo1DZ3ePq8gO4QpmJ0VNTd-HKU3xLmxyJ2LQXpsOXC90jcTpLLGd9OAXhk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaZ3pdzkMmmybhDjZ7EJiSwkSc9yGaD1yMnYLNfaJD_HShWIq8gluUznRZvN5sTQoedwrVT7CVtSuc7vITtJOsqjXmHU9R0rClF1rzoZbKiu2n17TOgeaJQRnLS9lWAnNrJp55vLtK5JNDdmVzgaKgCIeaWgXaZc71fBjgqUeu8Tp9bjmyorpwgfsufXvsYEosT-8-V0h53cMz55TYWXKbTA4zemA3muOrkB7cfP7w7ESV9tFYbeHXcRl1L2WHzlYgpamUj-Rnn0_iymeh-ipD2Z0VHoxmSo1DZ3ePq8gO4QpmJ0VNTd-HKU3xLmxyJ2LQXpsOXC90jcTpLLGd9OAXhk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=B9O64Wf__NLSwxiLOOHx7ymLM_Hd3mtpyjh-7grOW50YW6d2d1h6rUBv9sy6eEjPuUd2h_t8YOlOTuyLTD8ZOfXbJ0PYRrMDE91HoWJ808CigxCBw9aPS21qTwXZJtQHQXs9TxZrEw_MEzhEpNFGizXgPCOjF4YCbcbWb4bj45NHSHDa3gHEd0YrcY_ucVcLJf-pvvpTc65oKu6h2xcWxsXenay6mT71Bp0snmaALS_JL6fKadtyyz16BwRR9jYIKhqv7yJBI3XsWGbQ8tr2q5HvlqmR8FAyDT_FYbIGD_rdAEKmRnryCsFXuj7mz5jydMR9jX2OYDpJ2tAc5W8OHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=B9O64Wf__NLSwxiLOOHx7ymLM_Hd3mtpyjh-7grOW50YW6d2d1h6rUBv9sy6eEjPuUd2h_t8YOlOTuyLTD8ZOfXbJ0PYRrMDE91HoWJ808CigxCBw9aPS21qTwXZJtQHQXs9TxZrEw_MEzhEpNFGizXgPCOjF4YCbcbWb4bj45NHSHDa3gHEd0YrcY_ucVcLJf-pvvpTc65oKu6h2xcWxsXenay6mT71Bp0snmaALS_JL6fKadtyyz16BwRR9jYIKhqv7yJBI3XsWGbQ8tr2q5HvlqmR8FAyDT_FYbIGD_rdAEKmRnryCsFXuj7mz5jydMR9jX2OYDpJ2tAc5W8OHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
