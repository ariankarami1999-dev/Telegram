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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 21:30:48</div>
<hr>

<div class="tg-post" id="msg-5873">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Hr_ni2aMd0iaNt6qnRy2KuW4m6kDLvOlL3Eura7ABTceAx70WYEI_b0PxfGiw3U2KUJVFx4DWjqBwn60SVErcljFH8qCgxlhCHURb113zfeZHn4KRZH40_dW2EGWUbWBqx9YADPSrbu7GQqWVgGeKyJ_5kEAi0ozpy32APdMFO6cn21gS0OEkmxYPZuXh6a2PFek780XrCzvJJoJ_8HLNwAelBIqo87nh8ngpdamTc9E1NeWZp1rnfbXPXyg2ZE2OhNOfRJ1ENAobE3nF629TH5WDAgG61QecXHMJIz5grR5PcKxo42G4khfP6xYFC34z2nIKFfIQ7OkQ_2sSyTX7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa0113a474.mp4?token=Hr_ni2aMd0iaNt6qnRy2KuW4m6kDLvOlL3Eura7ABTceAx70WYEI_b0PxfGiw3U2KUJVFx4DWjqBwn60SVErcljFH8qCgxlhCHURb113zfeZHn4KRZH40_dW2EGWUbWBqx9YADPSrbu7GQqWVgGeKyJ_5kEAi0ozpy32APdMFO6cn21gS0OEkmxYPZuXh6a2PFek780XrCzvJJoJ_8HLNwAelBIqo87nh8ngpdamTc9E1NeWZp1rnfbXPXyg2ZE2OhNOfRJ1ENAobE3nF629TH5WDAgG61QecXHMJIz5grR5PcKxo42G4khfP6xYFC34z2nIKFfIQ7OkQ_2sSyTX7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چمدان‌های تیم ژاپن از برگشت از آمریکا
و چمدان‌های تیم جمهوری اسلامی</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8TmlUukgx1CEMxrplBrST7mcORmueW5TPxmvJyYIx1gXuGnjch6i_jSD6dxQA9wNntu2S2uOLXXgZnMEc_5MsPr2YVuuR5OPlbKMSGK7xmig-nu01nyG8d6GkeyzUxn4tckbpN7A-DKWeZjdRctdIIw0vkX9V69l6raE4_Oinyql337INXK4g2riy7f-GFsi6GF3lhGhIcrg4xvRS6XWe1WuRul9AhWMl13Wrin5WVHXwbzwSxrMa9nxYPEhZaenXITHHcr7OmRGUHDdKQ7THRh37vPrCn9oMKyyrGIcOhk-lU7twZS7Bx-MskFFy87mKoeN8ggtc9CNGde889kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=M5cLA2QwTt9U1k-o98Jp1H5_DmJna36gGGqv2f215Y3zu9JX1Qmi_5Ov8ff8oP4IAwN4rZvu0xCBJc8Uyvp8mqDlliccgW7HNet6dwyo8b0atX_B0UcoDpR-yOS_RxvtVpk5exrzHRwwIuUMWctuJH0S96r2GmYHTnzggMjHxMPqJQW743XlgI60p_Q8eFi2Q2vtrUyp--z0YzlQBX5fsc7EHGzGo5iLVVpqxRKcbdTFu8hefP_YolE25kRnFBRzulkQSEWHYQWp28pmUVdZICHlgxJntZQhfUmL2obv09U_mkFsaJyFwE__GnuQ8Zw7kzegIp5ZPVK7FCESUsMi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=M5cLA2QwTt9U1k-o98Jp1H5_DmJna36gGGqv2f215Y3zu9JX1Qmi_5Ov8ff8oP4IAwN4rZvu0xCBJc8Uyvp8mqDlliccgW7HNet6dwyo8b0atX_B0UcoDpR-yOS_RxvtVpk5exrzHRwwIuUMWctuJH0S96r2GmYHTnzggMjHxMPqJQW743XlgI60p_Q8eFi2Q2vtrUyp--z0YzlQBX5fsc7EHGzGo5iLVVpqxRKcbdTFu8hefP_YolE25kRnFBRzulkQSEWHYQWp28pmUVdZICHlgxJntZQhfUmL2obv09U_mkFsaJyFwE__GnuQ8Zw7kzegIp5ZPVK7FCESUsMi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5dODDg3fb81p5u6a_ck5bJLdYkPSXTGydinYk2d4WJADl9fnY815EInC8-JK759-2XGwmijzLqvgnEtFzEhWA3-2bAfpVAS01AKudy7WcCAbGvOyz-mS2d59sohFy5Hot6JmfNBKHfI7xiRuF7IoA7dW9onkO6gpb87GIP1iM7Hja1LqIqz2Zcl5BN3nSqWlLI6cNe2MhtR7pjLSDqHUs_KTi_QBLGVDCXY7Whc66qSC9HoW40HO9F8H2pvuDMNdg71fSZo_N3NqKwjnwEQgD79xZd32_0kZa7fk6HuMC-OM3OKlJctQR2q2janKs7Nj9vYd22fWt8iAmphlbSgeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IzsFmndgHJ11Vw-EFFYO3uct6LyyWfVoUjjlMxMOZldXCuz-SrOa3rc1F1-WS8xgch2Ey-ksuUEEVcjJmj9IKZQR83Moj_r4v1LNpGNzob4ROQ81MlfzLMaQaLD5xwMpLxOGwVcworwmlKuNFBg5rAGQ3rgDZ613IxB9p75jdBUFf50kvMFuPDQkl-7z1MXK0CJdHUcc0H3wabENYd9xrhFc7NojnKrF5-nrz7054ZXSZS727L7FsJBuwNOsomDOCJsyGn-DiJ9Uq-ITCALoHLK63HsfyAC89hgGlYF3hu397d4j1G3zLBN9p6U71E_7IkX6iTbSjqWuY4_GX5x9_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HV28Zu2zTmTeeS40QkXz_1u3Ee_461_hYFRx-U8tp6RpW-ZnMIpg6lTokKvAyPXF_RescB8S5OqawzKiYeLdo5uamHaZYu0TS_y2aDTnM8qPqT4j06XgPQvhf9BX_yU4iq8zdydJZt7d7MRW_7lMbGh2js_NHK0KbXBGF1waRUGSS0gDJ05IG7GWCPBlANG7dsLhK5vtHQQ1eAyqZKEUjlRSX2JRxSBm7XrlLoQuh3zbJ_FID2qU8CXfRijOnzoELOSBdO16XIP5_MRu7lqEeHfu0kcIlhE5EeCTStK_ON2eoKyRSqPAm8El8sLSIQDVIxswD7JBipRNTBMQB9MkJA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ao-F5lssV0ueVlI9NqDoNQJhSC13oZPGdkjYK0kdFX4dc77OBAr0c6eT57uDvzo7WHGUjH4P8Jr_U5v5ZSijQ5nwrdU3Bf99mTwXrmoJsOye5r4l0l4obMGKyqVl8igSFde2Pn2CCkeo4dcskyX8XcQBUP3ZMGAYA_Ua7dMO70CEVcHCekwgntX85BShtXLd2-1GjIToicOiOHxsGjZyuxlPs-5WluMhhosnNOtoT5rV6OJZihiQg1HK5BZjDED8OXb1GkuPPbVLaS0NAf0rg41bvSdfVTA4PExmaAlIBhdlRoWNeEw3OBaYQp0puljofFYnTO7WuY3Cc6Yo3W8lVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=p8P3V2i2-0xAq5qau3Ky2LLKXV3S4AMAaSSlbejiRJV7BygsTB5RDG0uPwOOEga1zaXQYsoJDAMhPaH56rX96kUOW42IDPm1MsKjWenDi0hnyn9dZnV1HVoa6rHlwi-VetLkMzzjJgJrb14aiLvE5GdUpkabFTfbvNMAfjkGvdOLmvTNTY0Z1R91AmFl58WXv8qcN31zkXMmXXJDzH2K98QLTDOsL7NNkI__-M_43TvU9prdeEJlFQu-nN6K7oZ5PFAKlO5SXR2vC7fEJhUVmNMH9PNOY6XjbMtyoBfd7mQPyBbRRQtiLAv3Ri96k0Iu4B3RNXxGI8h0mmGua5VIMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=p8P3V2i2-0xAq5qau3Ky2LLKXV3S4AMAaSSlbejiRJV7BygsTB5RDG0uPwOOEga1zaXQYsoJDAMhPaH56rX96kUOW42IDPm1MsKjWenDi0hnyn9dZnV1HVoa6rHlwi-VetLkMzzjJgJrb14aiLvE5GdUpkabFTfbvNMAfjkGvdOLmvTNTY0Z1R91AmFl58WXv8qcN31zkXMmXXJDzH2K98QLTDOsL7NNkI__-M_43TvU9prdeEJlFQu-nN6K7oZ5PFAKlO5SXR2vC7fEJhUVmNMH9PNOY6XjbMtyoBfd7mQPyBbRRQtiLAv3Ri96k0Iu4B3RNXxGI8h0mmGua5VIMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=V7GOm13w3rUyZYk7HI-AwZswwXHCVruJvl9AmFOjWD8z-xUT95OFq22Or14HinfybKujcwVjNX9rtBkzbnOcWTCCqtPs-JjYeMXN1Jfz2VBdPmqcfLt2LfZBl9hgZ82AluHz0vOAA2sYx80K4SobquIwGEzle9M9DxxsoJnLVXVjInnIspjuJHFfwpQ2NEbLfCjMh8oE3Kl9pv9eVAsGfvKTmJEFVRYjrbIJulQ4Z31fWc95n-SW2yP1NokrzBxXMFc0I2v5FjDoXuK_qQO-pLHC2OEJqNUpfGdl-s5AyO36lgEDDZQ1-RtnGguIcvxLQMsv2_h03b_E3EaIxOCzcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=V7GOm13w3rUyZYk7HI-AwZswwXHCVruJvl9AmFOjWD8z-xUT95OFq22Or14HinfybKujcwVjNX9rtBkzbnOcWTCCqtPs-JjYeMXN1Jfz2VBdPmqcfLt2LfZBl9hgZ82AluHz0vOAA2sYx80K4SobquIwGEzle9M9DxxsoJnLVXVjInnIspjuJHFfwpQ2NEbLfCjMh8oE3Kl9pv9eVAsGfvKTmJEFVRYjrbIJulQ4Z31fWc95n-SW2yP1NokrzBxXMFc0I2v5FjDoXuK_qQO-pLHC2OEJqNUpfGdl-s5AyO36lgEDDZQ1-RtnGguIcvxLQMsv2_h03b_E3EaIxOCzcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=MIL1pT-WQJLoiuUKi3cGCbDJJGLK_x7oF35BSS9WZfZ5VwNB3gTIs30L6CYfp1Dw3CO9wR8kH2SLnIGyZn8xrvfLgu6G97DiIqKv5ttJj7UL23Q3strdtQDPG5lFm7rRYzltHtqKNJF39cWCRd4VjRSKH9rjR3ID_APhwf5gPCH4uz0UMw5oalKU0kNpHFmPV4sWxjxRE0cN34s_jE_ofLG9E-4nIQtFpdN7lW9b3G7gKJFaIaGUDnESSUXdEyno_d2bJuvXaoWM9xwC485XTzkX3qYYEXihFR6UyF7Tw0g5AF8TRLKH8M9dHYY0s72fAVfnG2Z8tzj8-4HE_k3Pqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=MIL1pT-WQJLoiuUKi3cGCbDJJGLK_x7oF35BSS9WZfZ5VwNB3gTIs30L6CYfp1Dw3CO9wR8kH2SLnIGyZn8xrvfLgu6G97DiIqKv5ttJj7UL23Q3strdtQDPG5lFm7rRYzltHtqKNJF39cWCRd4VjRSKH9rjR3ID_APhwf5gPCH4uz0UMw5oalKU0kNpHFmPV4sWxjxRE0cN34s_jE_ofLG9E-4nIQtFpdN7lW9b3G7gKJFaIaGUDnESSUXdEyno_d2bJuvXaoWM9xwC485XTzkX3qYYEXihFR6UyF7Tw0g5AF8TRLKH8M9dHYY0s72fAVfnG2Z8tzj8-4HE_k3Pqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=BoyQ1LjmPfkfDIyWcrfkI13IWKmXq5dq5CTnDMcFxEq7mRlDKeQDIWCRf6xpNZO6DUFlo2R2_G-v8PGwiVlDDyPP66f2c5aeHzHlZak5leUjch5gkyomUtZX7YMP4TEl13BdI54NMSGImTo0f6G57KAlpJZxbL7yJs8QguxAPNtbg0D7Pb7JRq3AMYkAKoqMoiDaJUmzxMFl9kTNrhsxi0KbO071VEm89Se-hySrvfbYP9gqR9RqppzL9GNmzE4QuI9isx9Xsy6jyCCOtfCkVguz82iyNJUpQOx9RG25-Ly0i25d5_tJgv7cGpTqs_S3j8o98sNq-v7KelMU8yWCWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=BoyQ1LjmPfkfDIyWcrfkI13IWKmXq5dq5CTnDMcFxEq7mRlDKeQDIWCRf6xpNZO6DUFlo2R2_G-v8PGwiVlDDyPP66f2c5aeHzHlZak5leUjch5gkyomUtZX7YMP4TEl13BdI54NMSGImTo0f6G57KAlpJZxbL7yJs8QguxAPNtbg0D7Pb7JRq3AMYkAKoqMoiDaJUmzxMFl9kTNrhsxi0KbO071VEm89Se-hySrvfbYP9gqR9RqppzL9GNmzE4QuI9isx9Xsy6jyCCOtfCkVguz82iyNJUpQOx9RG25-Ly0i25d5_tJgv7cGpTqs_S3j8o98sNq-v7KelMU8yWCWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=Sj4ZnjjYAuGPj9m7ny9BlKKCE9HxSIhzVFfD4gDc-HS9GrsLufZ_8cBMhcYwrLVUz2mO94HNm0izKxRkDzeztqbzk8wa-m0u8xSKpJPkPrIeDf2EyQurgZ2RI5pYadjy0MMEsm8AUWCzqfCjrz2LPmv5Y3c1x5YSFp5h_vOPLeaGwdqjUQwd6OakLZD5AQuzHevpTdfDQ9efNbQwMkOUE5-tzVWC3vaZVUAsEHE2hvVGTY75d7kbI2o1wMHlxNDKx14hxmBv3Ey7w5EumV3z-Ovs4QHyp0YoIwfhWw2Cr4E6p13RYDo9y7pzgp8cEC6PLfG4VfadCCc466fh-vx9Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=Sj4ZnjjYAuGPj9m7ny9BlKKCE9HxSIhzVFfD4gDc-HS9GrsLufZ_8cBMhcYwrLVUz2mO94HNm0izKxRkDzeztqbzk8wa-m0u8xSKpJPkPrIeDf2EyQurgZ2RI5pYadjy0MMEsm8AUWCzqfCjrz2LPmv5Y3c1x5YSFp5h_vOPLeaGwdqjUQwd6OakLZD5AQuzHevpTdfDQ9efNbQwMkOUE5-tzVWC3vaZVUAsEHE2hvVGTY75d7kbI2o1wMHlxNDKx14hxmBv3Ey7w5EumV3z-Ovs4QHyp0YoIwfhWw2Cr4E6p13RYDo9y7pzgp8cEC6PLfG4VfadCCc466fh-vx9Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=guoTzQlaqH15mdu9dF6Gk4HQXKIbQJefnHko4VEb5DdU--oedcKba5rPqkulrR6Muycez4KxWhgMLYhtNsRu3ndhKWiJcnouEysLaYtoIGUxvFGVXL5b5ZO4hGqYpUy80aVpPMLp5BT6Fv59hgaD1x0rj3MyHggkiuRBnD7eA2izQSdE3SWOWdATN0zwCL4n1myWUB4mZnHV_Fe9NnnSt6-c_nL_WQlqXkVr4IKt9Io0NcbWg2kD_Jo169vDr9oDzesG6PCF44n2_45ny9C4FzERCXItiQ132Hw_z93OFs7Yuw4kfdR58FeIDiYvXH9iEgBOO9NhFuUKDpNiXVAw8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=guoTzQlaqH15mdu9dF6Gk4HQXKIbQJefnHko4VEb5DdU--oedcKba5rPqkulrR6Muycez4KxWhgMLYhtNsRu3ndhKWiJcnouEysLaYtoIGUxvFGVXL5b5ZO4hGqYpUy80aVpPMLp5BT6Fv59hgaD1x0rj3MyHggkiuRBnD7eA2izQSdE3SWOWdATN0zwCL4n1myWUB4mZnHV_Fe9NnnSt6-c_nL_WQlqXkVr4IKt9Io0NcbWg2kD_Jo169vDr9oDzesG6PCF44n2_45ny9C4FzERCXItiQ132Hw_z93OFs7Yuw4kfdR58FeIDiYvXH9iEgBOO9NhFuUKDpNiXVAw8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0YpuZtmagDBuUJPy8xFnckmVD2VMqJIj5GktooqiGpWBd-Rp_daSM_OLsbc-j-U1QZNtxo2ZzWVZ0WX1WMd-3ocpXjbL_NAeEEuSjxE_xUi4YNO2XuNX6wKgmnbsmlZDBaHSunXC3rGLAl9lKpUvCmJgty78TWjI1PL6ja3vYbSpR7k16rG3TWs4CVVJ818JT6muobc1FyDAkEinV_M4fCckfaMj6sHbnGjj0c4JCK6dS1-ZhR2GU6gyVafIs1lv4ixrqxi1oojN_tijzR2DOd7tc64ga8-OuUa8VZaXySoarUh6rYFtF6LEa6J4EQECk60w3FDjXKonZa3qTCg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=rtRHrWDCKo6NP2tImTND51hKEC9DptL5pjr_VOMyDhezDvP8g9e0XkT6VXirjG0nMIK32gZ9rCajoHBtyB3T9s4oBKuwatceFTrT9euU_GGXzlZ6EtIak_ytMpw-ZAHx0nna5pn_IwHAEp2_bvqpZapIFYqiM0E_1H2HLTfDHq8YRgyKq5eua4L1_spM69WwsGHxFkKzl46j4VOMr5QCR2gLSFfW63nPWKdOWXYmviTPNXepZ-cq6071qALV5Ykv3fnK4vTElbY35pBokrK46SJ-9GIEq2QYBhSfBU_wuvAtZ1TPY69C-1hLBM11ccyUOXvoh7sCaZE1a-v9I0HsZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=rtRHrWDCKo6NP2tImTND51hKEC9DptL5pjr_VOMyDhezDvP8g9e0XkT6VXirjG0nMIK32gZ9rCajoHBtyB3T9s4oBKuwatceFTrT9euU_GGXzlZ6EtIak_ytMpw-ZAHx0nna5pn_IwHAEp2_bvqpZapIFYqiM0E_1H2HLTfDHq8YRgyKq5eua4L1_spM69WwsGHxFkKzl46j4VOMr5QCR2gLSFfW63nPWKdOWXYmviTPNXepZ-cq6071qALV5Ykv3fnK4vTElbY35pBokrK46SJ-9GIEq2QYBhSfBU_wuvAtZ1TPY69C-1hLBM11ccyUOXvoh7sCaZE1a-v9I0HsZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=lg2e1ISVQggfhwfsBNi2nB0ixzROEgzcy4O75dCg88dmZOrXqn2kFlQ7vMEAKB2b7mmnrOCVMy3bSCO6D8iv1R53NdKOVqBH1tkDz9b2ScOSApn_8H1csR2FFJb6qJ--W2YPzJ6C_ekHSsybnW7niz4Eet3MQ-zCc4z2ZDWcfStgR9kX2Uczcq8JOCVegmjI37swoSIXaFL-R040PYniXuaQTy8QQWBz9Iprf7ghdf2Pzengv8HsZCbHi9QcgQW1zkakxN_6Ime7ZU9KmMU-Q1D3R6lbc2TW7SlFIJebF8TTy6oJju5iM731b7E9KxOfiYJwMEaiFCuipfuo4WAAuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=lg2e1ISVQggfhwfsBNi2nB0ixzROEgzcy4O75dCg88dmZOrXqn2kFlQ7vMEAKB2b7mmnrOCVMy3bSCO6D8iv1R53NdKOVqBH1tkDz9b2ScOSApn_8H1csR2FFJb6qJ--W2YPzJ6C_ekHSsybnW7niz4Eet3MQ-zCc4z2ZDWcfStgR9kX2Uczcq8JOCVegmjI37swoSIXaFL-R040PYniXuaQTy8QQWBz9Iprf7ghdf2Pzengv8HsZCbHi9QcgQW1zkakxN_6Ime7ZU9KmMU-Q1D3R6lbc2TW7SlFIJebF8TTy6oJju5iM731b7E9KxOfiYJwMEaiFCuipfuo4WAAuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVNrVQL9WHhSIDLNmsn6SGONXE7dLc0AN3UqhAlJch5gXO7ZsQFZGWIZmJWHRAFELdkWZsOUpHsIpvCjpbOpPqplAvmn30W5ongO6xpVNB9z3E2p1oGzi0ggDgKFuySlhcZrCUMCbAUe_GP0cqfN9Ei3xuEok9PhOAPcrD3FXoAsR4RWIt-Alh91oJ39P2l3op4ToDB8s9wsNoTmbcnNfdu27BmS7W3gr5X2fIGHPQS19DXSTt1XyW4kVZwp6iRSxHE8UxelY9jFXxqThFx-CFas8Vl0uN-abNTsjdla9taxmuRvDLgYQIJDVNYJZ1mbvn_3m-Kebesf7SF1dwjhfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UaVawb1vSUcgnoTNeLplAxBbxtJywRhfz3ofyTQJlleWJzqGhV-W31hX7aC5YGXxcO4Mfu3UpsV23l2_YYLCuImOtoIUz67vpgD72Jp6hWmXnISzQUNf1A9emadkp8eEh3Nii8D0gYp_MJMPKbR58ifPZI-MxSfbFNu5OlAsCJUkmgPnLeScs8ULvCd_0ofSso3PVleMZhHvz_Ryibu6s8r_6G3ObWlIsbBorZEQYADLJnRjceH4ac89UICXDl12PKPfoTeUB5NGswuAoltYUh_WmChEs570UtQDf5MP9zFu5uyfA4MmneoHsZjZO4hXw51is5ut7E3srTeRoG8QbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hmatr4RrZ5s1x6bhtrfyo3tG_l5dhxl5pnDKaniOuFjSO0TtngzbNUXQOvLiaapJz9xsJu-nt1jLuV8YqZ2_4xMdorxZpwGElWv9imrm7U06k38HAgR4-r2RDmabPnfhScrFlRWoQao9Nay-cPjrOuSZ84s9Fj4bRAX1sA7-cGf7v9dOqAQ7nM6NIAebDuXoaVrjr8XrSpSQbo7uGz1kwhjsb6v3lFD3EaZzOpR0WsHEz1Gw6TRHtASKtaV4eFXnP5Ebp7HAj6ww7IzpnAs6Ba1yeX51XLeMh0o-paa0rn6t0poY-H-AJ94kDjAT7mNEMjKhEGYeiwY2VB0Ty9F2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkPasqoVamDAAeSLOmORZUvaFaH6XkXUhCfQwT8IBdg2RqlRjBW0L_TS8SGXWwCeTHn2WlFo1WWnyfvNlgTJrB_83gk_X9LX9O9IFzHyJvdpmcwtJGyL-Oqq1Kf_sQbaBW_fM3ExF2skDeIl1ipZoI15RUTDGA1qksKk3WFQyGH_aMcSuTIX6A9gxC-VxsTVjB8pSFAM3kFa-VIN7jsez3WKPsYOjcCnnMg7WXx03N4B4bb7WTQHvv3UdUGIYcthgia1d0tW4XEW3NrwhvJ3HcrytwyZs63l5ZW6l9wYtvUEzBg5pGdeLc-NcjjVZEPF1r_VOBs5KhkfEMjiEn3-4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NYATAYPqf2ihqNZ-M3WK4gqX0WihUj41fyMtQKN3z0d5UM13RCXFuVegC8Qes9E7vBgA3PaxApbzBjcV4VaZKwtAsT6NxIPPUF9d_BHROsb4_oy0wjko2smVdrJQdacfnkj8IIusXp21DIpWdcb5oGC5UmUhDMYGbYJFLoFb_lqCfl1OFs1cRojAg08pMQrLcK2-T3l26c8f6Bii4EnKnP131Dl7RlZnDjmjXZk8IQg5xppJQ_haU9BntCMtWHWwlcAayPl0crWva5NXVsDFUzczF657KKL3IUeIk5_xBKj-RLXr5ggq6I_zCtVJC7HEhD0zwInbxRmHmhWdfLF__g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HkEy8CGQIVQd7GOrXD9x4FZ7DcpA2hf-yOxtmI53J60ozo2oAIIvRdufCbHYbd64HUM6MJXD8GXuOhKK7Zfedn5ymHSMz1fHX9jwSAR4IJ5iDqAIaPHr_j7Erl2Pwl8aDGWoHhNmCGQ6bxsi347JxryRadRRa0RNoFL_rBChwkYKu3Xk7wZHnalRlHstgzRbg4GIz5syYbbACqYlTOd7dsybVkZ64ADo2Xb6acSNwdtcGyvjvrouDdh2DstffPHbU8mHf6v7B_GYRj4sICdhTn0svTZeYVvXl_vtSSLrN79ctwiMVNQrAknNPsZq75ixHy8E_s6Jmn7RYG1yKYRtTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fb0si9iCVSwSERHWm-Sa1onRGvRBXdivQviuqrDc0M6NvaTmy17SKd_Cmr9BLN8vb-cORa7-Fcet4s_RQYEXTg_Vz515M289kbqGM4Tcdx_JYlg1W2DArWjAiQ8KCwXj3A_tZCOTl7q4HiTYS6BldBRkzYgxS93gJ9pw80PQ9Cdz4Z9BP99PqCZuhG4lbmZZCLId2nJ4bq3Ds5FrVIDFuUTnFAQKCvPWzdKCM8ZPkKP6BNtj5ZTLYnepduPKxa89mIHMIyqCld9taQfK2MGmovFCoaY7HP4UjHsCyRekNcvrAaLh_WEqGtYyyYiqi4M0cwW5VrxO52cW3B-FZwm0ZA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCi1jIDdxE9hHx1AeK0hq71X4q9xSq9pcdBqzXVxxiyzncAYE0EuYJ7OI85oOVJxXd0zFmUFf-n1lgk5kNiTidZTaDjzy6NI1cqPYQ0Ss5dtg_OU-Tz5AdxUnGn6pj-r6hRRTfA4kfKkHIMFyd3eBNs8ahmjTHXinuQUDw_kpJxUsJlbLAp50ktvezVghSkPufBhdyBvLVupL4hXBdBm3RSEvaATtgQ3uGfmsO7ACmHWNIM17jclOCikwbB2lbEPpPwlj9to9_LZohd-u6t-XA0JXaWFI-pO8lMrd4qEZorVMA3VCJwlftU9rKISR7MK55Io7F6lQfTQvJDCBPl3dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CyK7SAW52uqXGYQc5YtkHYADaafARmvF0DeV4Zbo-jaJYUBIRVDbXy_TAZfD4jP40ethG2kxSM-FB7AGiKAwUk1sTrCoEsqltVOAdhwu36CW9d41ibmWHLXZfwAK6uJW1dlc-TwO_R3EAXvBOQG_36dwPOiQZG4WXK343QTDSQZqCrqu6zR33fC-xupO5WXUD4jJWn2cd1FkUW_UiUMYuIndlEvU1f-JMPcLnPb8Z9LQTrxb5xiBa_FmXMmw4zwasYdWnPU1Di37xFkP-bf5qHU5NDgSCGzAcsx4QpYyjF2R_THaugTD6hayLbakhXI8X17_SM9qVQ4uetlc8NFObw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUQhurEdgzczEOj4Z6MIH7PbmN62s8_3-qdv2WoskpUPKGLtx_kw0ySBrvLjiVno4Y2n9vk0caW0PC0MywnxN9X6A9QXQRM_wMC2xKda--I82VL5Zfq95xBuTA5rTZHBVnEgY2DhRZGX3mTdGzZ6k_r0cMZbwNGvCuaMrz4jxps8WyjpXVUehLHJQ7OaFf9kgRL49jKPefASNuJq0PN7SwXhGsdU3NgvB4pVR7bUTxj6kriNb_hhGnvkwrpqh3kgDCnj6F-i02gvDqQyyPr4ZNKJ830YJgDo8rybUdgrpjXh0-t1Kc8-jb6bUFIfhYx09tUmRvPeqUiV4lKDuSfpug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opBhnNeqeP1f22VJ2iHH3mNE_3UDMXAOSuRA8Ol5iraBY6mfArAUcvbno3fPAHR4maI4krTlyx_wwqPlyjxKI_I9kKq6nuEBXVuZJBtPr22Nu0wZt2IPTf2L5bMcy0BVRE_T1N83BgywWXjG8U2321F91m1mmZyfMn7_7SdCB_Avptl4cOzJvn8bKJLz5brKwZ37ig_Dfg5zAL2d0cwN_LCcLM8x-CTQ9lzGXRlWW5tLZgO8aw_b7v3xBbjkk16-kuAGVCXiAxaSb9DN6RC7uUjljedEND3aC3QXe1_btn2C8O2h2D-06Ig8pMdgGjk4pZhmxQVjnmbxwsUtD3UwWg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=lEnURXRsNd6tg-rz4z_gJSk7DpRjtO_0ue4vtthCOdgWl8JMS-COoYId4CZsWHKj76O-EubIxDZHvHdmfJHVPg8BfHkSp7I6h71xM8-sXPzol6nu48YJCpuMhBN3vVkFkld5yH_iUWtP-4APqZi6-NOh54V1MyaCz-IOqRTJ5nP40srvtRPt47N8XOMQ53f5Wa3nYfYiYwb57zVT_uNKLxvwFPteE_9Sua5SYtJjFl5l66YzvAOFhIrJw-9PXmfQpCcBW3LknSEYvOs9nfMIDNhbnupArRAmPhK4KXSRYQQ98RM4Aa7Ts6v-cJpPhN4vQ4mO3CM2JlMiL9W_qAI3LA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=lEnURXRsNd6tg-rz4z_gJSk7DpRjtO_0ue4vtthCOdgWl8JMS-COoYId4CZsWHKj76O-EubIxDZHvHdmfJHVPg8BfHkSp7I6h71xM8-sXPzol6nu48YJCpuMhBN3vVkFkld5yH_iUWtP-4APqZi6-NOh54V1MyaCz-IOqRTJ5nP40srvtRPt47N8XOMQ53f5Wa3nYfYiYwb57zVT_uNKLxvwFPteE_9Sua5SYtJjFl5l66YzvAOFhIrJw-9PXmfQpCcBW3LknSEYvOs9nfMIDNhbnupArRAmPhK4KXSRYQQ98RM4Aa7Ts6v-cJpPhN4vQ4mO3CM2JlMiL9W_qAI3LA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=WCRlVZQ3lYOwUI85im0o7rLQouBUgyEHXDJUcolI0BO0P96DJwsuFFYfLeYtwFhyTS1U5jkxdq3aAXeV9bGwwGRY6GVrxjWE4AnC2evnB9wpcNrTxjUu0dkuA-WV__p5XCFIaStbRtYAaSxfxEBeDTDGYhdAJ1IajOHCkWbAEzwuRcRpBbUcZjvKQXqn3atxgV-wvhz0AUhM1tpwIfr8nUo4orXtNDcwk85_9ea9INosNzie5EqCZMLPGCL1S7e0PT2n9oKlXNaYdz8fFBRqL8rng4xTDePmjJIZao0eAkxeJGRbL3HJNsqKDYVU1fVwKswA79XZs9jYls5BGziHmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=WCRlVZQ3lYOwUI85im0o7rLQouBUgyEHXDJUcolI0BO0P96DJwsuFFYfLeYtwFhyTS1U5jkxdq3aAXeV9bGwwGRY6GVrxjWE4AnC2evnB9wpcNrTxjUu0dkuA-WV__p5XCFIaStbRtYAaSxfxEBeDTDGYhdAJ1IajOHCkWbAEzwuRcRpBbUcZjvKQXqn3atxgV-wvhz0AUhM1tpwIfr8nUo4orXtNDcwk85_9ea9INosNzie5EqCZMLPGCL1S7e0PT2n9oKlXNaYdz8fFBRqL8rng4xTDePmjJIZao0eAkxeJGRbL3HJNsqKDYVU1fVwKswA79XZs9jYls5BGziHmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=lYpvf8fSTWL7bq5PoHNCvou95fOFMFR6euspVxb7q8lJh4jHe0je0J2E0o47QSnQ8ir9mwYaig_209ose9jgM9t15dEn8NTbT3O8tDaTmi3PdEOLZ4LtcY5KKzxXGNbhLXsgP9u-4N4P2MoS6lRn2drB40H7KUFt4-X8T5V6UQO5_tZiO193hSvUYvJC52NdRDr_mFvY9xZPeXntL4YtBPJoK5Bw5lrKvysMQ-xmVb6g6Pum_9GX2YnvdvPMOji9VySEOBOBsoOYk_haykNP7SDeMAbyF7NSVe0F3Ug4hCvud-AyIa4MwA-Fn7W4WRwu-8-WUfPDQg0xOxFa6ODiyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=lYpvf8fSTWL7bq5PoHNCvou95fOFMFR6euspVxb7q8lJh4jHe0je0J2E0o47QSnQ8ir9mwYaig_209ose9jgM9t15dEn8NTbT3O8tDaTmi3PdEOLZ4LtcY5KKzxXGNbhLXsgP9u-4N4P2MoS6lRn2drB40H7KUFt4-X8T5V6UQO5_tZiO193hSvUYvJC52NdRDr_mFvY9xZPeXntL4YtBPJoK5Bw5lrKvysMQ-xmVb6g6Pum_9GX2YnvdvPMOji9VySEOBOBsoOYk_haykNP7SDeMAbyF7NSVe0F3Ug4hCvud-AyIa4MwA-Fn7W4WRwu-8-WUfPDQg0xOxFa6ODiyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=VMD1KxOXxhzosJ49uru7EcaTaGYZmhD47Q81Enl5dYnvhnQZjcZNtd6WSqAsPRTprK0koiaPQgWNWJwOYz_Kt_kRM8NpEKd_fgS98VkgLhAIFH0ogta3F2Kt8rb4neDCHcQyQJDCCAvM1qwkEJ48lWOEnLvOjR03vOyM3qej9rPSqKjH9mV8u_e0ZN6eBNMLM_a1QcHb-g08qblRDUUJQdT7OmeV3ZGqBSJV0mneTAOcrFXuWOqvzc2XJsvYLh2Hlbm5wf8-p9GL5BEj7H1ewYtBErqSTUoFppFTq_CzXtRY86DMZMnFc3lCa0VZqAijjIAMwu9V80M8POemBYuYzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=VMD1KxOXxhzosJ49uru7EcaTaGYZmhD47Q81Enl5dYnvhnQZjcZNtd6WSqAsPRTprK0koiaPQgWNWJwOYz_Kt_kRM8NpEKd_fgS98VkgLhAIFH0ogta3F2Kt8rb4neDCHcQyQJDCCAvM1qwkEJ48lWOEnLvOjR03vOyM3qej9rPSqKjH9mV8u_e0ZN6eBNMLM_a1QcHb-g08qblRDUUJQdT7OmeV3ZGqBSJV0mneTAOcrFXuWOqvzc2XJsvYLh2Hlbm5wf8-p9GL5BEj7H1ewYtBErqSTUoFppFTq_CzXtRY86DMZMnFc3lCa0VZqAijjIAMwu9V80M8POemBYuYzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=i8bEpa2sry6FYpYUP6WOWXcon1u-Ui8maD93Z4DLjlmDjnmCs0aqjhgtvqkSASI527lZoSpM67u5B0Tuza70I_tPsXE2ago2126reqfBwXnibFYfBRRpTAmUwLcibW_QD98MitHBrTfUFOMX51MEWP5HCU0fBLzLH7UI53CTD_HZm6mc0gPBUkDf8vQHAIC-d3PDiMzIYWvKDGPwEkxfmh4xLuKa904hvk2fuQiyuA_NOOMyI_Iqbjp_7i0mXzXrbE0SOmQKfcDBdgbeWiXEExp5YFNpTc-fT6O4QqsBGmiFUtWJsNTT9DCkBVQGqQ6vLr1_gu9LUe6dbQgClZSE-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=i8bEpa2sry6FYpYUP6WOWXcon1u-Ui8maD93Z4DLjlmDjnmCs0aqjhgtvqkSASI527lZoSpM67u5B0Tuza70I_tPsXE2ago2126reqfBwXnibFYfBRRpTAmUwLcibW_QD98MitHBrTfUFOMX51MEWP5HCU0fBLzLH7UI53CTD_HZm6mc0gPBUkDf8vQHAIC-d3PDiMzIYWvKDGPwEkxfmh4xLuKa904hvk2fuQiyuA_NOOMyI_Iqbjp_7i0mXzXrbE0SOmQKfcDBdgbeWiXEExp5YFNpTc-fT6O4QqsBGmiFUtWJsNTT9DCkBVQGqQ6vLr1_gu9LUe6dbQgClZSE-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=juuRcEojr8ZRpI-GxRgxkQ0KCI7DBi39OL-Emgs8bmVSaOY38appkGcVBzREA3UqA_Woyk-4hpET5NADwqXbDqErzuzB1vmolpqIzch23Me29QD8TsroIoHEang9RO8747LDw_6dWOD4B8AXCmO9IuCutvByvhsJCE8luATFFiVGEUY1ucfFEgt3Pqj_7LMCb3coEmskiQz9ILPkHTfj0RcVB-8QQcz0V2dHqyHrlqjczN02BtJxB6OscHL8bqHQZjsAYSMybqv6DRomWesmiY2t7e9SB_6QxE2WPdY1IxfV0zoXmkX3YV23ZZZnMbm1myAjympavnR1PRfcVXPFUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=juuRcEojr8ZRpI-GxRgxkQ0KCI7DBi39OL-Emgs8bmVSaOY38appkGcVBzREA3UqA_Woyk-4hpET5NADwqXbDqErzuzB1vmolpqIzch23Me29QD8TsroIoHEang9RO8747LDw_6dWOD4B8AXCmO9IuCutvByvhsJCE8luATFFiVGEUY1ucfFEgt3Pqj_7LMCb3coEmskiQz9ILPkHTfj0RcVB-8QQcz0V2dHqyHrlqjczN02BtJxB6OscHL8bqHQZjsAYSMybqv6DRomWesmiY2t7e9SB_6QxE2WPdY1IxfV0zoXmkX3YV23ZZZnMbm1myAjympavnR1PRfcVXPFUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=sD2WLvzOUpxT1zhQLlcjZghLKGlf5U46N2cO1KJKQxKRJRJ9K2l2T6CltICirQESvs5KuQ1FBbtyeOUvkhjnuC6sroWOoPRpJHEyFhfcFWmRam3gE7z9LetGlmFRvJ1xBvhLgAZ1XDPc-AVEvQgH4kMdOQErgcR2Ps_NpWAUTNwlQd52At2KKU7CoPK6GBVpbaFc6mBrjlnlLskMb3NDHsZXcn3dU5Fw_NDaqnI_SHi0spfiPxjCkAMO112hzmyU12UNzafFDJPdYg-fIE7lP4ObYOhq-j_h2ArTpx8sGPr_WuqQ7CBQ1rshNJ_q9P1vWI4pznfHp2zZcrf5UZiUOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=sD2WLvzOUpxT1zhQLlcjZghLKGlf5U46N2cO1KJKQxKRJRJ9K2l2T6CltICirQESvs5KuQ1FBbtyeOUvkhjnuC6sroWOoPRpJHEyFhfcFWmRam3gE7z9LetGlmFRvJ1xBvhLgAZ1XDPc-AVEvQgH4kMdOQErgcR2Ps_NpWAUTNwlQd52At2KKU7CoPK6GBVpbaFc6mBrjlnlLskMb3NDHsZXcn3dU5Fw_NDaqnI_SHi0spfiPxjCkAMO112hzmyU12UNzafFDJPdYg-fIE7lP4ObYOhq-j_h2ArTpx8sGPr_WuqQ7CBQ1rshNJ_q9P1vWI4pznfHp2zZcrf5UZiUOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqnE0x5TbmJQUzUaulFXGicWaWn9tTKZ6hkyKEm73mAwejVh-BqboGudocdSsn9dCq_hB1nVSKiStQNqt5DGDIeoNRWxuIBrJZ8m535D31oqvAUjJktb-ivbCXFTmKseo6ZpWt-T9Z2spPQy76vimnZ-zYNF4uqd9j_H_wHJB1q4cteRS8srBmA1J6LNMPMiK2_6yTRMba1f-lf3V4vzoLs_-SJA52wUUvQUvLmuF6b4WsWxIdNrHl3-guJgoBV027L4OnrkKf0FkYuu1nx26EjF2_i7nGw2G8_PlsnvTQR92T-eqfprMZ5Zla5n0EW5bXkE0_Pl818pjnI0XtZ6rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=QegE1uNNsehxUzcS12dtPGbhsc6sqb8ykwX8nbIKDGlrU1gRuigEwIXjW3zAglHDryPIjFjHxBvngMnznWPDXpykiQTYTSupv5pceI5BlGmZWrVoNfERhX2ii6IOHSzqIqzh6K5u0-9TTi49l55Aq68YSQJTh7Mnc46nFWBEUroPPA0xw3ODEDA-L1gsy7RCtRw-jX3K6Ja8xKs537nhGUAmb40k6KAE6huDKZiI7mq7kWwSRxUdYRef_f_vCFRgPI0LWkHYvgCAtUXp-cJsnKDMEnVoUIgO32DyrZ6Ei4w8MxH5lWHNOcsN6-fgrEAf87RICt6WJUxmLFKYNmNwJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=QegE1uNNsehxUzcS12dtPGbhsc6sqb8ykwX8nbIKDGlrU1gRuigEwIXjW3zAglHDryPIjFjHxBvngMnznWPDXpykiQTYTSupv5pceI5BlGmZWrVoNfERhX2ii6IOHSzqIqzh6K5u0-9TTi49l55Aq68YSQJTh7Mnc46nFWBEUroPPA0xw3ODEDA-L1gsy7RCtRw-jX3K6Ja8xKs537nhGUAmb40k6KAE6huDKZiI7mq7kWwSRxUdYRef_f_vCFRgPI0LWkHYvgCAtUXp-cJsnKDMEnVoUIgO32DyrZ6Ei4w8MxH5lWHNOcsN6-fgrEAf87RICt6WJUxmLFKYNmNwJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=o79xhaV31iRdm8DlCFBuzYtRtZF016_XAgPkPwl2TiO26TaOXWiGRs6EHlEk1eefLcHvJND4EYf5E_ILeftP6Wb9QxJ5OAGHY5GExIkiR67alFmozbgHKHKH3cL8-FQKNDfF26bX5eihJaoTGQHleibzYQ4ng_rZVtKoqNeH5gkvhSSUV4vGUzVtoLotLGCNYdIau9xDq5HH8gapS66icQUUh1tTLWXt0k6ZoKA6r5CcN7V2phZOe46O66S2S7w-mNqFMPHJUNEM67ovji3Xkn-FPOxD5ej9XzACJZVohUkBlvCaN16ib_EhQl4bSpnK33Q3Xhwz_FLtg_vGNIDDnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=o79xhaV31iRdm8DlCFBuzYtRtZF016_XAgPkPwl2TiO26TaOXWiGRs6EHlEk1eefLcHvJND4EYf5E_ILeftP6Wb9QxJ5OAGHY5GExIkiR67alFmozbgHKHKH3cL8-FQKNDfF26bX5eihJaoTGQHleibzYQ4ng_rZVtKoqNeH5gkvhSSUV4vGUzVtoLotLGCNYdIau9xDq5HH8gapS66icQUUh1tTLWXt0k6ZoKA6r5CcN7V2phZOe46O66S2S7w-mNqFMPHJUNEM67ovji3Xkn-FPOxD5ej9XzACJZVohUkBlvCaN16ib_EhQl4bSpnK33Q3Xhwz_FLtg_vGNIDDnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=ptGR9JNRh8e0jFwFZ90l4WF65HC6OCLrXTeTwxGIA-KlM7BU_xGBzNJeYzBxgfMN4mL2HeB8wU4j3tPB6sYCb3Po1d4IgOo0BfBTWGhVGtNUgYUnEaTNi5r-k2p3zvZN_cRG-ty5IDRq6TNLUpbZk8OWdFoSqhJjrz0f9naAPqRDP94_S6IC3MhXTLZY1aMSPgkDa_w8esJeWD2bF8mz0v2Hr0zV3Z0grsLZcDN8aSooXJ7RkYgiiiik4hNma3emW8D7NLgPhnH-mZPkuXkdMpnS7mHsAiLha1npxjKFjhpBrGEqmozVQbppOyP7sW3VyG-7wX6sa3DPL674WkurwplQ3zSr8iBQHU2Kq9rc05PS60Gz6A4kkAzH9JpOcGRkNDwP2S08TMdV-vEepAjnh9E3FeCEI8CEJYkWzf5LOoVvywWKCPJEYAVlESF-0RvkLGTgHwzCe_MeDTAxIZhBjmY9bzB9-61AlkeNwY-RvPKwDbTICWnnGoFEq4SWa3xrv8zx4tWBnzynLRYV68jDY50oZOQ5f7HM_wlCEBha6kmyxU4sBaVMBOV5ZBVQaLWqDWhC13G8HNRbRKJ_G_tNxsI0yZ7ZIjkB_-sEbKS_6XmEtmWpYXqBrAz_wFpKfl_mZtfuy3z02K_NwbHBa_w_O9l2uUqknyttaEAJ6QKvJQY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=ptGR9JNRh8e0jFwFZ90l4WF65HC6OCLrXTeTwxGIA-KlM7BU_xGBzNJeYzBxgfMN4mL2HeB8wU4j3tPB6sYCb3Po1d4IgOo0BfBTWGhVGtNUgYUnEaTNi5r-k2p3zvZN_cRG-ty5IDRq6TNLUpbZk8OWdFoSqhJjrz0f9naAPqRDP94_S6IC3MhXTLZY1aMSPgkDa_w8esJeWD2bF8mz0v2Hr0zV3Z0grsLZcDN8aSooXJ7RkYgiiiik4hNma3emW8D7NLgPhnH-mZPkuXkdMpnS7mHsAiLha1npxjKFjhpBrGEqmozVQbppOyP7sW3VyG-7wX6sa3DPL674WkurwplQ3zSr8iBQHU2Kq9rc05PS60Gz6A4kkAzH9JpOcGRkNDwP2S08TMdV-vEepAjnh9E3FeCEI8CEJYkWzf5LOoVvywWKCPJEYAVlESF-0RvkLGTgHwzCe_MeDTAxIZhBjmY9bzB9-61AlkeNwY-RvPKwDbTICWnnGoFEq4SWa3xrv8zx4tWBnzynLRYV68jDY50oZOQ5f7HM_wlCEBha6kmyxU4sBaVMBOV5ZBVQaLWqDWhC13G8HNRbRKJ_G_tNxsI0yZ7ZIjkB_-sEbKS_6XmEtmWpYXqBrAz_wFpKfl_mZtfuy3z02K_NwbHBa_w_O9l2uUqknyttaEAJ6QKvJQY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Stiy2TqySr65DCxlwrOdA3D9dXJlDz0Qp7GRU9YGbR6UPSL0L5iQCbIOxqBDGsVVMVp_UxCiG_WLj7JHab6Z3B5d5tWhtAoiBKWzuvvsb1QFt0LpnUdr4ARdG1NkTuCA4kxnwafaz8rHFsfTdQcym8bOBE9G4xyXaRmYqsVZkWcUiWGsXSTgEPZXqpfqZ6HsVx7piX4T34Zh7FiVi3zjQtOZ7O_XN5rlH_f0UM7h8e7GizkVWICO7TZj9C__ZRXAtjApXUsP5qpturyk9oGalwYZl000YrQXAdk5BSpP1kAOBrsiYTCsXft0kVbo6qKYi2_QVgnvdEn2pM1CiIv7QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=Stiy2TqySr65DCxlwrOdA3D9dXJlDz0Qp7GRU9YGbR6UPSL0L5iQCbIOxqBDGsVVMVp_UxCiG_WLj7JHab6Z3B5d5tWhtAoiBKWzuvvsb1QFt0LpnUdr4ARdG1NkTuCA4kxnwafaz8rHFsfTdQcym8bOBE9G4xyXaRmYqsVZkWcUiWGsXSTgEPZXqpfqZ6HsVx7piX4T34Zh7FiVi3zjQtOZ7O_XN5rlH_f0UM7h8e7GizkVWICO7TZj9C__ZRXAtjApXUsP5qpturyk9oGalwYZl000YrQXAdk5BSpP1kAOBrsiYTCsXft0kVbo6qKYi2_QVgnvdEn2pM1CiIv7QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=CXv019L5YHuPbkLtlRuVY98EWQBMucRKSIz5ZQfZXSqcnAEpikpFlECdQ10G6bpNDx2NQqQC5t17tAW8qjQgqnzU3kJNyQtQiGVaAtD-ADbMWAOytDhjfVzvNGsesvxSv3WRI8XBrkCsJheC5MWAu5s7lQFFN_jXwXRgjKZermI1RPgd3R1zPwp8-kRVcgHkfkhwPR2sKDFb6uyxRF7pls0BWhQ5Qi_jSVr14ZeEMWUDCXkY53eq0rVht5fRid3byGKcSHkfVrimRwcT0Zk8cx31E7BQjbHOpLSS1ZVYgQcx3JQwAQ3PAzly34hu1IFTVD41XhufyujXKbLKNBBTTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=CXv019L5YHuPbkLtlRuVY98EWQBMucRKSIz5ZQfZXSqcnAEpikpFlECdQ10G6bpNDx2NQqQC5t17tAW8qjQgqnzU3kJNyQtQiGVaAtD-ADbMWAOytDhjfVzvNGsesvxSv3WRI8XBrkCsJheC5MWAu5s7lQFFN_jXwXRgjKZermI1RPgd3R1zPwp8-kRVcgHkfkhwPR2sKDFb6uyxRF7pls0BWhQ5Qi_jSVr14ZeEMWUDCXkY53eq0rVht5fRid3byGKcSHkfVrimRwcT0Zk8cx31E7BQjbHOpLSS1ZVYgQcx3JQwAQ3PAzly34hu1IFTVD41XhufyujXKbLKNBBTTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p1kN9ejOI_2wHCx8VogcFVdKawTdbbqry3i-RXwnzAVN6akr-Gd9qQyik0hsgiJZz8ui96MCCuIM9SkSgJ2OBAxu9Jl7npsF2dYbgVVQKDQlNXA484zmOOnGcH1hhmc4LFNP1zr_S4OmpbW9MxS6bfGjjbt6PZMgWaEqzOtC8LWI7fZzsnR8Aj0M2I-FDr8pYLyKFr3bPzdnQbIvWKtHOy7uj6-9ihySAJmYRYmgfhuySWlGKyUaAcDmrUq8Ge0mvwVbgnoZu6xuAljBSDvBgUPuZoR1JotdEjcNT5p1vtOE0a2RnEmUz0okW_YOLdHhvyeMft0YZIrTvu2GiFTiIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lE9q7N8RVp9ACbgTF0181ha4cOLnmhqP5K1EjbYy8BQufycF0uMQIeCF6GlFG-rGWLJmD0QGVRI5bD4jv2Zm70f3SvBdDhIGYGtehWMMrFNJstQXFYcTkUDmSTRTZTZwSfEYUUhjoQWg9gL4VbE7c0fGrLbeFSr1Rs45omGaQQ6mNHXPOa5fUfiApbUD_KPh-sWJobPXtfAyToR2m1U2k4llJzDM3pHu0LYdA28wSBGlCJ_kP_hCLRL0YVlKnt7ebGoSJMv9RYisQNkUV7NF-wLzE_4zo4aS4tUsjzc1wltvmhwG1ZrHWkls3py5kn5X53EybQuSSdXmX53LsiBBsw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=otKNIY25loedrmIRXZoe2aop-yTvkXBbrMeRxh9sfgS4GdE7L6WPDEkmqZmAAupdDdGz-gFQFhiZ6zRJR30jk_nCaHQoyJLB7pVb6EoMC4lbJTGIDTaPshwnEd-EQAILVeQnx_e-x7CAYM-CcrQwpFjfad-ZKP7Uwc-DXZ7etiC32mshMQKKceaVf8X_3Df1JG1QweZr9waEAcroWxh0wg6x8YoS526UHs8nX1_rar83YMgNyQNQMfeKxMm9e7lgcUOjWACh49qLKMI7ih55WmXhQoOPkzSVxZ6H8QsOB-jPDU4zup9997rlEPJfMcSXn8G7n18QZSJeSd0M1OZz_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=otKNIY25loedrmIRXZoe2aop-yTvkXBbrMeRxh9sfgS4GdE7L6WPDEkmqZmAAupdDdGz-gFQFhiZ6zRJR30jk_nCaHQoyJLB7pVb6EoMC4lbJTGIDTaPshwnEd-EQAILVeQnx_e-x7CAYM-CcrQwpFjfad-ZKP7Uwc-DXZ7etiC32mshMQKKceaVf8X_3Df1JG1QweZr9waEAcroWxh0wg6x8YoS526UHs8nX1_rar83YMgNyQNQMfeKxMm9e7lgcUOjWACh49qLKMI7ih55WmXhQoOPkzSVxZ6H8QsOB-jPDU4zup9997rlEPJfMcSXn8G7n18QZSJeSd0M1OZz_IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2okvvbwJZd1O2i4uT6rRi2LIuNHHbRSsq5RFXRX7SUJMGTQwow85rX1mHJDi1QyXn2-eFY4TpImfAEbqyeiXvmhXNipVRu20Id_8cN4ZfztjXyNPF8ttXDR-_TgIQEl8ZnLwhBmxlYqHoFdx73M6xdkZ1y-3ayDaxv9ORgQ5AKSwERGwX5UDRaVBTi9polczC6XRAnaLFS6vAWfD0rM3S2Pb9MuL70iot7hp503f_Gu31CNw1A2nAww3C8YeurBHYA0Zg_voO2GHiV5my458RLgGjUhrgpybPbrUb81YiPgfiN0O4dWjN3kXS4sLp7iw3OG2ET5ZM29CBGW0tbrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zy8WCNsLTG5r2I4I2Gb0Y3fIAOTNI9lSSSZcLsUAI8hq09BKSRWHo2_yutfLvEq_dlbuPBFR4QRajmolfmBl6wd6o4A9HDE23hrsYHeMZr4CsW0Z_UpjFUPwTN29youaI7WFsF6aqpcSxx6egSjRQd8f77TLFOVKrqN3u2sPiGfFRSu6Gwgw4tUq0kvVvXEJ69iEYz2hL_yl5Y2oRIMlchhjA246fpMBIU3KsMRaGz_r5gTgjicq8msnvcDn5WrqXs1in_TBHWxx3m_LHKcKZl7tcA-Y_clCtqZmkKBUWnL_c8cNdxz5xYVgk83ekz8YiT7uFyqWqCW0HDFYQzSD3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CzDVU4znTQ0_cAo9VucvSJToRZ_4_9Nx2W8Q_Htt1ioRl65Uw9EZq1Le6zNFeXOmE46vCfuFGBURwCr05M07gi2hMZnxPLaJoTuU3U89ETmdBIt7rBUYQTf2dHJPJe-f-ru0lcA6Moe4XJaD4LO_UwLaOhHsJCH_V7b0VIFg_uM2sZIbUmTRVG2e7e36YqDdaUshjc0P4p2ZJoAW7DR2ss3Dv4s19D9-H-RJb8KiINmkyON7NqrrsNvWc40ZKWEjUCG3J2nhbaodWEo_QC2X3cV5laxNib0JLxlKj5lj08ijxuKvBNioeRzuIs5tEBp6X1MRuJilfxXNvTKBgFyYhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HPRx3ljOeUnTBeCRiidTZnltGKL3CAlU4isGU8RowWVVzaqNpLfUr-jFvRXsTAq7RWAXnAcy-lYXvtm06K7gP-jzaFMrT7je-dq5AoZGKDfK72wxgDNmU-wp-kPH4lWbIbklA7E1dq4Rv2QcpXxjM3yRFMiIq1GkH00LhovClGZrcCj9LnZ0hWkoFMhv1cWaAnrdjHrs5E9QIgbFkbDTgjhOKGIhkfLgiQr4YaWpfK5EezMtIVUI93_2MwAdK-j9ScXcYxiCIQLDGez2txc1wsS5-4GPp2goI1zJmGjsYjRfoH6JA4MjAGeri9zFxhxtpziI5Jtb-x2P7kXNxWNLDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=aEF4nA1JgHjLHDQ3Jf1zsdWkxFA00lRTec3N2PlPVIaMJV6YETV3ALbayu-hEOH13X148hsQPh4or6KGDc8fqGP85k2RU8FBK9pmdnIZezHlYLBV_PzFwYeD2huKkCt8rHvmxJzzUtTrk_g15HUenxtS1N_V3wcp8rvXtqzqllF0iYctTvUcEY25bSOGVRqLzDYd_YRfWAmMx8seioQADvo5lvFAU0BXKcc3SUR-1LpaKaQdw_i9ZL0JjrhKjsUGAJxhs07ZLFgjaj2RFjjyzEHmL8rygY4gLFfkVlEOPDwskXOokKzm-VsrmF_OXf8gdD1bSwuBlhtwPpEIkHSpXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=aEF4nA1JgHjLHDQ3Jf1zsdWkxFA00lRTec3N2PlPVIaMJV6YETV3ALbayu-hEOH13X148hsQPh4or6KGDc8fqGP85k2RU8FBK9pmdnIZezHlYLBV_PzFwYeD2huKkCt8rHvmxJzzUtTrk_g15HUenxtS1N_V3wcp8rvXtqzqllF0iYctTvUcEY25bSOGVRqLzDYd_YRfWAmMx8seioQADvo5lvFAU0BXKcc3SUR-1LpaKaQdw_i9ZL0JjrhKjsUGAJxhs07ZLFgjaj2RFjjyzEHmL8rygY4gLFfkVlEOPDwskXOokKzm-VsrmF_OXf8gdD1bSwuBlhtwPpEIkHSpXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=pKTnJZrV63sMS7axMBHIi-C5V4HtpIJMUqdjmyQHwaAvtRpmX5SeTgpKsrA25kxuMIlizA21XDGox5C71PvHybux_VZMJi5TsZeRbbZ70bxULUe5gQbAicFm0ZziSeyz1n3Sr0XkSuJYDZeBBQyAUMHYTkcg-7wTJCw8frg5zocgGjFlJ_k2fQT9AcxdZe2y728pqmRP8LSrwKUV1IhSm3yUs7HIpTe0GJPPpiMgFHRVKFWGBIcW9xhz_tCHeYHWRqeL1BamLaZNEnQKHdcfRhO9o617c-8dzDxDDUpLveJfruIeR-D9QxtHlYhteo8UjKOfD2c_IN9zT_sJqitKKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=pKTnJZrV63sMS7axMBHIi-C5V4HtpIJMUqdjmyQHwaAvtRpmX5SeTgpKsrA25kxuMIlizA21XDGox5C71PvHybux_VZMJi5TsZeRbbZ70bxULUe5gQbAicFm0ZziSeyz1n3Sr0XkSuJYDZeBBQyAUMHYTkcg-7wTJCw8frg5zocgGjFlJ_k2fQT9AcxdZe2y728pqmRP8LSrwKUV1IhSm3yUs7HIpTe0GJPPpiMgFHRVKFWGBIcW9xhz_tCHeYHWRqeL1BamLaZNEnQKHdcfRhO9o617c-8dzDxDDUpLveJfruIeR-D9QxtHlYhteo8UjKOfD2c_IN9zT_sJqitKKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/osNCZP2_8Bk1nNxgXTfE9jLzTNdRRq08KuzK8F2Nf6gGu9cfZLlxuDeHVlqBKkg4HTEEKy7UC4i3C9b1Z3FuOLcQEhMSfYa5QQDqdC0TUgTmrTxbX862hVftV3ouMH8gywLTEplfY1BM3XnKkZZmYvnFm6L6RDEvR6PfPkTwnPAZbktcksjXS7_1MQEvePClUtrnr0JRdUdWNwh98j68kyIl05YQzSBjfxLmofcqM617ijiSIVpIulEhan2MVxRDrT_nO9bVcrpuE6eibpz4gB_VqG2HC0391af6YWMg3rZwpOzNN16tUP9SUWfMrjskNyUTFyhoTZMdSfVZDL98kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=ieBHGCtimmmQ9X607IFsuS5ys2ExW7ytYYYU0hXLT3l4Qq5Xnoqsm6_NMeD2llsvvfzxzJ3G5NKzbWSoNaHanBfLV5dSMCRVPcjXNLOsXYGymcFBHqXpJ7ZLmEgtoM2digdyCDqU5CELHyWnANroSSGyAhyQpYXW4hKOWBTEEEY1QW7MFzcBJQF9hxF2ecem06WkEpjpkPvjlSWA0tUFlU9WoeQp8WRHA9aW_vHJuN-L5791daADfqPsZiSsAKujz38edCYsqx-IyzU9QImP6HGM9Uc41Qi8eaJbxt_yJ84BK-mAhxs_fpUe2WiA_8RUjqok2rUVtkz_6XmB33imXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=ieBHGCtimmmQ9X607IFsuS5ys2ExW7ytYYYU0hXLT3l4Qq5Xnoqsm6_NMeD2llsvvfzxzJ3G5NKzbWSoNaHanBfLV5dSMCRVPcjXNLOsXYGymcFBHqXpJ7ZLmEgtoM2digdyCDqU5CELHyWnANroSSGyAhyQpYXW4hKOWBTEEEY1QW7MFzcBJQF9hxF2ecem06WkEpjpkPvjlSWA0tUFlU9WoeQp8WRHA9aW_vHJuN-L5791daADfqPsZiSsAKujz38edCYsqx-IyzU9QImP6HGM9Uc41Qi8eaJbxt_yJ84BK-mAhxs_fpUe2WiA_8RUjqok2rUVtkz_6XmB33imXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=pFrLhS4ePXNNAGwHUSz2uflFOWIUGiOy62kYK4uQXYaAe_N1qTZVAfZMLBIPEgkjRUD5OSWS4M1TLpQfpdU3tdeuhdG9uD8MJxIiTrJJCi97n1YtcpACKdx2fkfq2bP3qMlRnthLLiL8zhhEy_iJFW3ZaQe863U-qFhsCXaIlVR9bG4_Sze2bpRwcgnmvhzQWnuNn33Q_fYwqV6Nc3KLElFNFM8vPGPlhQlkFxrnRo0ZSd5g7803rBntmIjnJiJnYq5jFErNw6j47LIBOuyT3Z7eMCj7XWoEp5kikgRACWORDHuPC0gyngElRuQpuxXVFY9ZvFZCzbu5QJ7R7F9zig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=pFrLhS4ePXNNAGwHUSz2uflFOWIUGiOy62kYK4uQXYaAe_N1qTZVAfZMLBIPEgkjRUD5OSWS4M1TLpQfpdU3tdeuhdG9uD8MJxIiTrJJCi97n1YtcpACKdx2fkfq2bP3qMlRnthLLiL8zhhEy_iJFW3ZaQe863U-qFhsCXaIlVR9bG4_Sze2bpRwcgnmvhzQWnuNn33Q_fYwqV6Nc3KLElFNFM8vPGPlhQlkFxrnRo0ZSd5g7803rBntmIjnJiJnYq5jFErNw6j47LIBOuyT3Z7eMCj7XWoEp5kikgRACWORDHuPC0gyngElRuQpuxXVFY9ZvFZCzbu5QJ7R7F9zig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=aEMOVxAjckpe9ZVhybe1o7ZweRR4R4ehIvQvE9dOihwwJMV6fU8OTZW-Se67MxyJfZI2-GaQ-oO_1eWI3Jnggx0A0V-MYJ0jF7Xx1s5aJD2LEduwWr8IckWr21Jp1rgXNiRAxlOnzpkZp9sZWUNBnaOlJRcbOM-mfvflehLa6xyFCQD6nlNACzj4GpERWH03t2sYJ2l-cn97NFuKbWlk7kM0NQLFOcDzah_PSYep08o7Db6kBuYf0ml8fDvO_xAUFiDzr6QRL082xnFbMDkNFbytwF8hojgEf5v7i9iKGZAoTaNPixdjwPR8rplXJD-kEqDGUMnnxOZQ5q8xs7tV4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=aEMOVxAjckpe9ZVhybe1o7ZweRR4R4ehIvQvE9dOihwwJMV6fU8OTZW-Se67MxyJfZI2-GaQ-oO_1eWI3Jnggx0A0V-MYJ0jF7Xx1s5aJD2LEduwWr8IckWr21Jp1rgXNiRAxlOnzpkZp9sZWUNBnaOlJRcbOM-mfvflehLa6xyFCQD6nlNACzj4GpERWH03t2sYJ2l-cn97NFuKbWlk7kM0NQLFOcDzah_PSYep08o7Db6kBuYf0ml8fDvO_xAUFiDzr6QRL082xnFbMDkNFbytwF8hojgEf5v7i9iKGZAoTaNPixdjwPR8rplXJD-kEqDGUMnnxOZQ5q8xs7tV4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoqIfq_zesm7aUOoFhzUHinXC3hl4R_wZJziiRjj1ipjgbEZEX6rU_jBxsR79JeoYIDOhIzXhs567n5D3C-JXYy6fX72NGM13AXOR9aCZZS_D4Q0v9CmVd-TjL5I-3uw3wH3cPqImdCSG6X2c_9_VvFiofOYyv5dzFt-D0J9djv50xn3HJyjGWydYKtASuUjzyRbmElSSkVWQ1_jPRu-0RmhkOzke_qD0Y9stXi1QauyLpTNeGipm5_6hcMtSRvKMIRHIwEfObFd5we8rwFvxWfO-EbTCn5kj80aWR2nZwxfxvhD5V9_0AIoW1fHwFD370dbZlMx0s-XD5gLPTYLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=Rm1qQHD9d-aJ5EmoEC7AfRjp-Kl2Gsu4K3c-3LM-pfEkq9ZJvUpIiVYTr0rSItHm0PSwElBp7OY0ABlPqHIB3W_KllRpSyfeiqQxTv3kMw13AKvU9RdqIjUl3Fzjl4cM9L7pfhvriy4bxXXqXJYhqYVLfrziBsxT9_tbJW6JZ0PwKFJ9Pjty6KVPk61GnB5S5U_0btebQI2Pv2GVC4bL7HMsFgT2KHyvBJmc6OtoGgV6pIPMmTiG5OB1FjtLZAGy260LtuHBKQlakMomlX1nFhrk0fQJnSuGzNBgHtOm32ACgKEkndd5qA8tvvm38K2NDEpsAqo-vYcpFzMjlnAcEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=Rm1qQHD9d-aJ5EmoEC7AfRjp-Kl2Gsu4K3c-3LM-pfEkq9ZJvUpIiVYTr0rSItHm0PSwElBp7OY0ABlPqHIB3W_KllRpSyfeiqQxTv3kMw13AKvU9RdqIjUl3Fzjl4cM9L7pfhvriy4bxXXqXJYhqYVLfrziBsxT9_tbJW6JZ0PwKFJ9Pjty6KVPk61GnB5S5U_0btebQI2Pv2GVC4bL7HMsFgT2KHyvBJmc6OtoGgV6pIPMmTiG5OB1FjtLZAGy260LtuHBKQlakMomlX1nFhrk0fQJnSuGzNBgHtOm32ACgKEkndd5qA8tvvm38K2NDEpsAqo-vYcpFzMjlnAcEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XrhcRrnbiJ99uiWoM2K5AGG0SES98hnaIZlYHflwju9nDCJIMZxaI5veVWC-hsYH5U9pnXdos9Wgml_FKuEcfVjm_N_H67fd0qW2s7oYsnf8EsgJg4suKLxI6VI3kJ-EgQBQydO6oI33A2h3kZ8G0TYY_c258l1lX3ERiuNbeMsdo_7tebO1n8HO2jGMPaYoYxRO93WKoghGsZX7mD7c0B6c525NBSEL-vRetZxqwpTmI05OPjw9NyLRfvPfZbeC6gyrOQkjMxRv5Uot_iTm4l532eZC3GUII3q9YoLCVTUhoiPLRqwzQdgvT1N7eCq-g6agSgsPMZM7y8mke0yglw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4MZct3DC2SRAYtltCtpXvUC7xfBdP0Fhb6X9faEptnFTz6G3EVHb8Bqoi4Y5T8NLhVJoLIjPdlEFVq8Hw_-t1gvQpxP4veuz06fXfTjb4HutrZYdaF8JvoGnra1_hGPaH8BsGUd5KRtP6n977FbvGIXFNSX8R0A7vnp-9LC1rFQtI2x6gkYAw6uW12duLWp-ujcUMHlMrBVDItF4u-_zGo8VnPgqr353o9ESJ7rStdBU5c1rDMT6jhJCWR72PelwI65e9qPQUQSW5zSagX093JnemtEVNim8LA-T174FuOd96HmUijJs6qqMNZRWyawk_tgTGPTeiq5YMKEG9ey8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=In2lZw4eYnmvU-_CyzFRRClyqyBrQtzu6tfu-vjsqAbLt07-0PdZinfCoLdp8ygP4CmoYfHKcAXDwMQdfZy5RW01chZj2OrCD1wxkyM_BDfbm6aunTzL8G6MIU-cALCjIL-Zh7B_eCKFV1jy_EA1Xwks_q1UpbG0bzO6CHn2cAiRt0P2srQrc5B1ItdLgLw1rdAzH-JGENfIaO2jKYJPUUzjQnCFPNJvftHeiaWyJDTs7H7zaCy_0aIiqLkpijqPEb0Z1NugSQFsneR6ZxMAY9Q7Wvze0Fy7VLJ98fhtg6ud4zGrTc0dnMMHBUtpezrTJUYMjBny1eosJIzeR3mh7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=In2lZw4eYnmvU-_CyzFRRClyqyBrQtzu6tfu-vjsqAbLt07-0PdZinfCoLdp8ygP4CmoYfHKcAXDwMQdfZy5RW01chZj2OrCD1wxkyM_BDfbm6aunTzL8G6MIU-cALCjIL-Zh7B_eCKFV1jy_EA1Xwks_q1UpbG0bzO6CHn2cAiRt0P2srQrc5B1ItdLgLw1rdAzH-JGENfIaO2jKYJPUUzjQnCFPNJvftHeiaWyJDTs7H7zaCy_0aIiqLkpijqPEb0Z1NugSQFsneR6ZxMAY9Q7Wvze0Fy7VLJ98fhtg6ud4zGrTc0dnMMHBUtpezrTJUYMjBny1eosJIzeR3mh7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0q2yPUHpYPBBr2twe8z-13pAIKY0qc3VP35UdfEzG9AzARtgzz8U98Sw7N6vE4xm2QBOHpjD3KzdvW0v8pbewjJpQA--uQnojANrw4op0N1rENFkohTA6f_A70n_1torCaXgm7AjHYWtHTukX2nfZsxFrNY_jTnL9XJZoQWGkB1n7Px9SqIvGnbcm2fOmfwlYQH9LDZegkYuN_BCZKgSBMMqpKLf6BpDPBBT2T_WuZRAysZF7UohQVOr4c0reT6KoRTz8AmA9zcaFC3Dj69Bsn8FD8D6agX95sj6n4Xe89d0NFVzf7agTJokT35A18Yi0iPrXziDILAPCVnWwphRX3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0q2yPUHpYPBBr2twe8z-13pAIKY0qc3VP35UdfEzG9AzARtgzz8U98Sw7N6vE4xm2QBOHpjD3KzdvW0v8pbewjJpQA--uQnojANrw4op0N1rENFkohTA6f_A70n_1torCaXgm7AjHYWtHTukX2nfZsxFrNY_jTnL9XJZoQWGkB1n7Px9SqIvGnbcm2fOmfwlYQH9LDZegkYuN_BCZKgSBMMqpKLf6BpDPBBT2T_WuZRAysZF7UohQVOr4c0reT6KoRTz8AmA9zcaFC3Dj69Bsn8FD8D6agX95sj6n4Xe89d0NFVzf7agTJokT35A18Yi0iPrXziDILAPCVnWwphRX3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=sd5kMqlQq_O8QWfvowd6Yz1Jim6eH3tQGEXmJeN5DkyowpRAvLNJvInCk8tXVh3qiZtywGAy1Jt7QYSLGpIHdHEwm9MnFtLZjAtyyK1BHZ7PGsPT5OpMAHQqaB7jaePH2CLqRHFhhCFd6avIEkqOS3hPCZHebAz7KtRGM1HFCDZs9l1b3TRJ4KmZg8KTbhDCqepy1eC4D1UmJ59g2q1rbJYq8b3YL0issyCwIKEfOf5LD7FxwVieeQv1EqnjnbyTnoaZTwbNU6KMGE7yjCgVipPwBx3VxDFfUDCy2kclnCbVWQ1dWdp4VCK62n-g5_AJKlWYT-BS2t2TWXdYqZdSlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=sd5kMqlQq_O8QWfvowd6Yz1Jim6eH3tQGEXmJeN5DkyowpRAvLNJvInCk8tXVh3qiZtywGAy1Jt7QYSLGpIHdHEwm9MnFtLZjAtyyK1BHZ7PGsPT5OpMAHQqaB7jaePH2CLqRHFhhCFd6avIEkqOS3hPCZHebAz7KtRGM1HFCDZs9l1b3TRJ4KmZg8KTbhDCqepy1eC4D1UmJ59g2q1rbJYq8b3YL0issyCwIKEfOf5LD7FxwVieeQv1EqnjnbyTnoaZTwbNU6KMGE7yjCgVipPwBx3VxDFfUDCy2kclnCbVWQ1dWdp4VCK62n-g5_AJKlWYT-BS2t2TWXdYqZdSlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RPKHTvivE_LZDTjlqi9OAbizaVVQ-dnUg5D8laYCGyUgNaYsvF0MtchXh8iQRPfV0fAE6z9F7wcQzI3RFDX9EX2gVtDnjbb3qb42S-h2DBKGeC4-CUx9UfgdHpsZpESju3Yct6H6QqcWnfj0PJmS4QkZb0P4WZEV0PqbGrxAaqVu0_0G72f7p4qrgeCmo6rj5Gf-nucDrkGKYUqALYjvzu-ZHfLKHSwTmMiR50IWSBx6muYcGaImWfTYsWlDiJjVE8NZgBb_CMGmig0h9aMDSY1uaWlVaOf6uoJ8K3ib_l4unM4ELKv-gPiWOyE7I4DdPPq7JfUlcel0fo9YFOp0ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=ITqJknev9bGMQzgaqlfeOxfQQD14ci6WrqFgiDr5-U44fP2x0PGSj554aVak40ZSPMEKBgII0xU9teMBisYgZEuDWA7sKBT0vfo7orju3FaUDE_Xq46kTNjwGBuEHE13H5lzr69k5XR0lE7TTSIc-5PCU3CUMFrJ6CrB3l-xZ1I_WTRKUzm9yPwWxWPLMPGZOGZv-nmRBHrD6gYebptDsGxRnxUqZZz3hQfDwse4-EaWSLiZH9ud0QyE4xkwhbsnK79tDQb-AvWE_ptCuwU-b6pyrqtYTmDf7EXDJ-4oVL8LNnH8vgUrMqPar5Z9CLmwhZHulqakb-bGrmWNnD4AUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=ITqJknev9bGMQzgaqlfeOxfQQD14ci6WrqFgiDr5-U44fP2x0PGSj554aVak40ZSPMEKBgII0xU9teMBisYgZEuDWA7sKBT0vfo7orju3FaUDE_Xq46kTNjwGBuEHE13H5lzr69k5XR0lE7TTSIc-5PCU3CUMFrJ6CrB3l-xZ1I_WTRKUzm9yPwWxWPLMPGZOGZv-nmRBHrD6gYebptDsGxRnxUqZZz3hQfDwse4-EaWSLiZH9ud0QyE4xkwhbsnK79tDQb-AvWE_ptCuwU-b6pyrqtYTmDf7EXDJ-4oVL8LNnH8vgUrMqPar5Z9CLmwhZHulqakb-bGrmWNnD4AUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=WR3a8Y7QDKCnrHYtn61yWefUc3csOwdmO8MPQywf3cwU842ieeywpiC1RpZcOO-nbNP0RJ25Y0Knsvec6ULf5uPsrAsdxfMwMGNOO2C8hww80CGVohH7NYy9vGLADsoiMvdmEgbFbXKcc7vcMsNV6dViHtCcFe2rxfh9XmrxRA38cM8xG2UzMSTSyQ3lGX3kKUfUNZZrdL_byVwXVVGD0zgnYH8XCALKpcNJJJrSIKbL8KLXTFug1buIqreKY1xhvw4oy6g6Qx5m0eexFWDIueW2ncJQoltFOQF-nSi8Up2Ui-haWHJO7QglcazpW0CzwcKvlMcJj7pXxzbN3T8v4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=WR3a8Y7QDKCnrHYtn61yWefUc3csOwdmO8MPQywf3cwU842ieeywpiC1RpZcOO-nbNP0RJ25Y0Knsvec6ULf5uPsrAsdxfMwMGNOO2C8hww80CGVohH7NYy9vGLADsoiMvdmEgbFbXKcc7vcMsNV6dViHtCcFe2rxfh9XmrxRA38cM8xG2UzMSTSyQ3lGX3kKUfUNZZrdL_byVwXVVGD0zgnYH8XCALKpcNJJJrSIKbL8KLXTFug1buIqreKY1xhvw4oy6g6Qx5m0eexFWDIueW2ncJQoltFOQF-nSi8Up2Ui-haWHJO7QglcazpW0CzwcKvlMcJj7pXxzbN3T8v4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=KbkqNsUNDYIqaIhSsz_yzcsbEYB6_aLO3Vxrb8zp_iytZqqvkDwKz_zvxwXNEnOvQeoc2WeHR_j3JYb_CN8CHid3OieqhzcgqprB7NmzX3xW03UDTJllhxRLE6bwsWLBMAqqDGuiAKN0epjzVx5xUnvUqqDKXoeNj2JRhtzlygczREbGXyA0Qi8_Nv59XrBpoPcKea1v_Dr8i27-192E35G3c0dhVoGVcI0_NCnAJWK8cC5YMGa2QyLuxhmP4soEZ8lKQI3Ps0Z95otoC5UtYfdkzYgcjJn1LAtviKz8I8UoLoaeS6XmoTUNhPoNxnHDmkAzh_b7rgBtKi978HgP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=KbkqNsUNDYIqaIhSsz_yzcsbEYB6_aLO3Vxrb8zp_iytZqqvkDwKz_zvxwXNEnOvQeoc2WeHR_j3JYb_CN8CHid3OieqhzcgqprB7NmzX3xW03UDTJllhxRLE6bwsWLBMAqqDGuiAKN0epjzVx5xUnvUqqDKXoeNj2JRhtzlygczREbGXyA0Qi8_Nv59XrBpoPcKea1v_Dr8i27-192E35G3c0dhVoGVcI0_NCnAJWK8cC5YMGa2QyLuxhmP4soEZ8lKQI3Ps0Z95otoC5UtYfdkzYgcjJn1LAtviKz8I8UoLoaeS6XmoTUNhPoNxnHDmkAzh_b7rgBtKi978HgP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=hHP26uhkJDzWnXEh76NxYxx5YLb8FCOz-cft0GDacfpllapRtk2f-QGsOUmrF37FtCe5RoGBzfmKu_sUnJzX7fgHD1aaxRgpGTyMZtncG3_2K2hrQru4lDX2hehSXy8IGVwW7LmQtVhhSphedjS67dpri3gODj2kahYdbGLzsKU2ZqlvKW7r1lT3Vx_Ba8URlswO_1irne21HP1EeRF-VF2R1SSk7DlMS8jULHd131S8kKCbWDGefWCOmjdZmZC_Ec8M-mHdun4Xsqspg9Dx193NKIiTpTnpDRbxdJGtlPimFZUIC9zbCpRBQ3GJB0TrHCgpUZplX2V18jwJb39ung" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=hHP26uhkJDzWnXEh76NxYxx5YLb8FCOz-cft0GDacfpllapRtk2f-QGsOUmrF37FtCe5RoGBzfmKu_sUnJzX7fgHD1aaxRgpGTyMZtncG3_2K2hrQru4lDX2hehSXy8IGVwW7LmQtVhhSphedjS67dpri3gODj2kahYdbGLzsKU2ZqlvKW7r1lT3Vx_Ba8URlswO_1irne21HP1EeRF-VF2R1SSk7DlMS8jULHd131S8kKCbWDGefWCOmjdZmZC_Ec8M-mHdun4Xsqspg9Dx193NKIiTpTnpDRbxdJGtlPimFZUIC9zbCpRBQ3GJB0TrHCgpUZplX2V18jwJb39ung" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dBgnlVdGAkiX6c76T54Zr6kvacp-6991y5jbgJYFu6HfD0DwIhnK0bB8WIJdZuCBgk9DoaDivDlP-LuHj_MyRLdoTLHyXgjvD5g6LA_DmD34kMgmi7mmmwwlFeqUY57we9UBQKeDZILoPXUDHvMcZbXat1Pp1Vj-H8smkL_B1Kpma8G32qDee27HieFyv6xRjxzA5zh1qf9ylvXQeUVI0PSqVPgSWOOJ_DWTVvdYm8U0amfOcxM4Z_1S6pNq2fCjN3IHfjQRpUtNpOGdP_eYs43l4o_ScVByihti3CPoNeiMVCzQ6em-ia3qZtkD2elJS3-CWzjCiSvb7QYMQFbt2A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=ST1sZ-MBvO-SvYR2VoY5SVaWFlrBwDophRkW6Kv2IW6yw0bwqtSSLbvvwQFQ-UUsBxjIwxfQQniETlZYZv8VsJLRmnyODfq0uXdaXixFec7VsrY8qm0f093hDQ7Ag0yhH8X1LvCzNvNrPDYp7AxvADcxBUNQZuiKyMWr-OC4wZoj4HLManV3jsbEF31B6ILg14UIv_SWlB0oRTPMS--nRVSAx1g1W_vQUp6MOt0CWwoM4JMfxBF2ywHXKdHUJJxwWF-bnMlu_sJ2RLqCo47ifNy1ScFu_G0iFI33XnJBaDYhXgjvr01fIi49QvD2oo7CXMR-2-r9vz3t6NTzWtTB4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=ST1sZ-MBvO-SvYR2VoY5SVaWFlrBwDophRkW6Kv2IW6yw0bwqtSSLbvvwQFQ-UUsBxjIwxfQQniETlZYZv8VsJLRmnyODfq0uXdaXixFec7VsrY8qm0f093hDQ7Ag0yhH8X1LvCzNvNrPDYp7AxvADcxBUNQZuiKyMWr-OC4wZoj4HLManV3jsbEF31B6ILg14UIv_SWlB0oRTPMS--nRVSAx1g1W_vQUp6MOt0CWwoM4JMfxBF2ywHXKdHUJJxwWF-bnMlu_sJ2RLqCo47ifNy1ScFu_G0iFI33XnJBaDYhXgjvr01fIi49QvD2oo7CXMR-2-r9vz3t6NTzWtTB4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=nymuA_EoMAVOns2hQwIrQx5N0idCqGYOq0AjVoVl5omve6_zQaD50cwPysuHMCcjuGxxr2Yktx5jVBdLaHCwIPRHN1E4aFTQkzkQHcLw7Q7bLwdUWGQKwO5gQbujD1QHxn3KoIuFZYoFq0Y2kgDKRJn7XDW93PG_uBQtUF81Tz5NoLlD0fSL78uvpt-c-x3fr30tj054X194opXdNIqcm252e86c1w6EmonGjSadxZaHaek8btmqlwgKkUAeFivl-cHBkLdWw_f9ryjNvrCKVUjQ36PahjqyYqOw0QnbYoqemN8X-5SX1bDbV2xZnn3lGV06IoVriw0Z3fkxfzvhUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=nymuA_EoMAVOns2hQwIrQx5N0idCqGYOq0AjVoVl5omve6_zQaD50cwPysuHMCcjuGxxr2Yktx5jVBdLaHCwIPRHN1E4aFTQkzkQHcLw7Q7bLwdUWGQKwO5gQbujD1QHxn3KoIuFZYoFq0Y2kgDKRJn7XDW93PG_uBQtUF81Tz5NoLlD0fSL78uvpt-c-x3fr30tj054X194opXdNIqcm252e86c1w6EmonGjSadxZaHaek8btmqlwgKkUAeFivl-cHBkLdWw_f9ryjNvrCKVUjQ36PahjqyYqOw0QnbYoqemN8X-5SX1bDbV2xZnn3lGV06IoVriw0Z3fkxfzvhUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0yTcTAa0gvbFD7fr-Zq_HHF0sXidXZXp-1ULwlgo2ncxBq78LOkcMVkzF_vcp4kbfb2r0r-ES-2f36agQrre3wYbUH3qR4FCj4HRxkAtZvCwXVCIbQz6bSRllFoNEx9jgkLM9CBMe4CcgF7NBCoLIU1dO8Gm7Zc4sPPAWYVBqNSZIapsVFNH9kVN0Wa0ZLO4hUSoFzlbGgfRSoOU5TCzo1rTkGBqr6XVWVE7rYNjgVK6OinA1_ESkfUwa2v9Ckdq5Ik9HoiJljimGbntal9phKjHYP5X0Qditm7xyV3lnBEzn2Yul1Z1YRwO-DHbDsSllpKl-1RAr4cimuyGl-buQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=bHc8PoYJfDuR4jjzQgbGieZoYEKkuGKA0MvVsxpqUcjCvGoHLxY2EKZ_A5YZzENG1gOU8RrO6wU4oh1_hYYcSIc3TrRu6GXUjLdsduYOrVc3sKTCC2uMUMlTOQstIakxdUDF8dUjqnOLBw3-bFdQ6R1kj3ru-m8TE5Jo3d9z7a21XFAJISxayjUGtnQs6rNEx9cE0DSCvF-JNOs0LJdKImsVxpekpwte-AQ1OLPtxhoT398vH6O8O7Cx9TKam9xXtnReTN6nV9BZOe4yV2M8i-uYmOMGd-OKtN_fDP1NnFqnPgDDIeuaXMDnxZ8z8Ex44nSmdqdm8lxTOHcWT6wBww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=bHc8PoYJfDuR4jjzQgbGieZoYEKkuGKA0MvVsxpqUcjCvGoHLxY2EKZ_A5YZzENG1gOU8RrO6wU4oh1_hYYcSIc3TrRu6GXUjLdsduYOrVc3sKTCC2uMUMlTOQstIakxdUDF8dUjqnOLBw3-bFdQ6R1kj3ru-m8TE5Jo3d9z7a21XFAJISxayjUGtnQs6rNEx9cE0DSCvF-JNOs0LJdKImsVxpekpwte-AQ1OLPtxhoT398vH6O8O7Cx9TKam9xXtnReTN6nV9BZOe4yV2M8i-uYmOMGd-OKtN_fDP1NnFqnPgDDIeuaXMDnxZ8z8Ex44nSmdqdm8lxTOHcWT6wBww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=nUiGhSffKWcVDE2n1p56kJTtPs_wu87AUIUKYvYAopJU-scBTDfclz0nGMITuHFngnpaU1hgWXGneiTFIy2YiiYTun2myS2FhxM7VRfdxEEeM4UBAM_5okBtFqagHzA2NkugBepM7kSDfFgT9aqPNfDaHpq25ybouMKmRdQIezUpca98FBHok3LG9Qc4Ujvf13RlgfhtAhPNjc_ZBxvfUY5n81bPLelVDiEGRqsIYHHQ4wwWXM3fSvGlZUG_PEP1Y82I1MT1VLfl2R8dfi6s6XHy_v4YlVrPpKWacFMIUyxO9oJQmzlq-mXfIje2caFfxCKXoNhqzJrswhBVEoH1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=nUiGhSffKWcVDE2n1p56kJTtPs_wu87AUIUKYvYAopJU-scBTDfclz0nGMITuHFngnpaU1hgWXGneiTFIy2YiiYTun2myS2FhxM7VRfdxEEeM4UBAM_5okBtFqagHzA2NkugBepM7kSDfFgT9aqPNfDaHpq25ybouMKmRdQIezUpca98FBHok3LG9Qc4Ujvf13RlgfhtAhPNjc_ZBxvfUY5n81bPLelVDiEGRqsIYHHQ4wwWXM3fSvGlZUG_PEP1Y82I1MT1VLfl2R8dfi6s6XHy_v4YlVrPpKWacFMIUyxO9oJQmzlq-mXfIje2caFfxCKXoNhqzJrswhBVEoH1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=nnuR4Sd4v5y8d3a6EGdpy8ecmvGs5i4gGoflpepcTDpsVI5pg3Sj-938MJX7w-iR0fU8aGKflbiUxG6WqjOtbAOpxY6QGoszYYARE-LShOclr8GLCWdLh2bdLlQ9zpKG9r4oS8JP-Wp5cl4XeTVCnLp_tuFaKWd20ENkr-kbNkMDsToDuumLIy6mekn1RUtNb3WWxoNl-cMzWUJ_yI7B3eQiU7u2Yk-STj6NcZo97_p41_I5GpTGOJaGEOWRVNeew2cGe4K62QIwxjcpdygoFIfBPURA_pBqHhyfay0kBCfz0mhgsg-pNDmhwrkaKlN9XEcD4l6yuRCSrqBxkKswijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=nnuR4Sd4v5y8d3a6EGdpy8ecmvGs5i4gGoflpepcTDpsVI5pg3Sj-938MJX7w-iR0fU8aGKflbiUxG6WqjOtbAOpxY6QGoszYYARE-LShOclr8GLCWdLh2bdLlQ9zpKG9r4oS8JP-Wp5cl4XeTVCnLp_tuFaKWd20ENkr-kbNkMDsToDuumLIy6mekn1RUtNb3WWxoNl-cMzWUJ_yI7B3eQiU7u2Yk-STj6NcZo97_p41_I5GpTGOJaGEOWRVNeew2cGe4K62QIwxjcpdygoFIfBPURA_pBqHhyfay0kBCfz0mhgsg-pNDmhwrkaKlN9XEcD4l6yuRCSrqBxkKswijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QpNo4e9OnGqydKR78pKZaFwfmWpy14F7wepqaMNCHzir2d8xNJZ9ghQtXxQ-oK_ifEa65Rsf5Oq4PssYgqIZiWcrZzVeWKZLwr6yzqp8GFbD6Qjbas72mRc2o3u2a4UeS2TaB0st0c8qm_4mI2zJMPMDfAByI6iZA9-qlLbUw14xWB7xJsU-MJYV6eX7sJb6OOcYsfh2cX8oPFJb2OwHr-FQ0DYuohk7Dk8zY87Uzql4HhXR2_MLwHHtDzk6U9-H1mjYgU-HJ50ooHdElq1LcWPf3BD6fh-DrNZx4lcsu3HXntBrySpOXd7FtvNKwwaLu3uNvb1LjHzzkU23Fw0lYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLDKsCTO7Ngqw2BfNad4r39vwKoumII3L3YqQ9gptwJiXWIatQGRMLXg1ehPAbqqhDFxZMKfJ0WBGDiBgtGu5zPKUBs1ZS1pXL7BgFsHtO0ELnr_eJ4vFA3Kfh6OF59R-JwXoHptVsFkyknu2Mm6DQurhCxkCT6zKxW6xQjflyBoGPe7jmoM7um4nLAEy40QKBfYncjnYkvacyt0xE59ShDO_VUgNWnoBgTrIE3FC7Fq5I2lDOKNyzYzdFGXt5wkXpKDKsobdVC7NBNnNUZICQoUrMHfGmSscLE3EW1uPxR4vz-Z7Vp1jTCYN4rb6Wg__XpfjhUQqp-k-Lw5aRkagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OQPnaQbzJpQ4qhyPlM2bjbmG6EiIIAQi_UMYIERLAylDBHhbyN01qG3USD36Oj_VJAs4hyV8fxsiSc2CgCF5KhwJ3uW8hMXDP2AdhsrZNxgK93Q1IK2XqGi1rbhRixYlbvVHsk5ZOoWmeRZymmdOd5zCbIJViZLg4Dd8juSL0LLi311PLmtWQfO-vsDlUJuJojAQOfls-FdC3CACkcEssB5268TwvGsEGG9gzvZyHQO1X_cwUQSne-j2tWjOE732k_SPYeB0qCUikVHsuypG1UI_4hKRduTkSFI1A75Y_1WAV3gq26ll55QkfZMTdGO4Ntms_Sey69QqY8EmU6lJ7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=f-cNTm_euerI9UpHgZvcl7DUDzW5WPQG9z3OCPtr1Hgzv69V4yMwgP1OeKwLv2d8hDVk2K8wm6Jl5fr3jtUmcnFXa-ALO00BXYFL8QJli82SxlC98HZBFeBBvxkTKxKWIUKdNUbWTZfcgIPlGjwqi60GEhfYe4ckOcnLSU_VRQirDrtCZ_BGLqeemonxSAYtFTYQLQkTs8ibDtCn2n50X9C3XPkPVC9eKu1NTdK_TJu2Z7iifqMvqEvx1nPWhv7D3ZOWzRFxNrXy8GIBiAORoNH54se1CXh5bQrx-OCtreg-ZYKv958dNHEknAs-pReXz4rLl_d0pnIm-xgnP3-9rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=f-cNTm_euerI9UpHgZvcl7DUDzW5WPQG9z3OCPtr1Hgzv69V4yMwgP1OeKwLv2d8hDVk2K8wm6Jl5fr3jtUmcnFXa-ALO00BXYFL8QJli82SxlC98HZBFeBBvxkTKxKWIUKdNUbWTZfcgIPlGjwqi60GEhfYe4ckOcnLSU_VRQirDrtCZ_BGLqeemonxSAYtFTYQLQkTs8ibDtCn2n50X9C3XPkPVC9eKu1NTdK_TJu2Z7iifqMvqEvx1nPWhv7D3ZOWzRFxNrXy8GIBiAORoNH54se1CXh5bQrx-OCtreg-ZYKv958dNHEknAs-pReXz4rLl_d0pnIm-xgnP3-9rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaalauOwlY4WMCOTPedgr3xwv13yJxgHnyvVAv7_ONk-TK4n-h19BoQg6ltukWuHkt_Y1qADaqVgL3CUa3yg-x_vx0gUK5nSO-0lRO6zeC1AfyxsBR_O9vOgDsDdFRGq2X2QKqRhwSpBDI768Np7Xb14CMcm6J_p6-4W0al2QFQd1oloUa1rYHp5ku69rpJ_V5gAc6ri1zebAezGGxHtx-8qXyd10iBWDb1oKbxyv-U1mTeDpSrtJ0nWg81W-8KS2eyZOarN_R2c4fW_Ut2I3esSh-s5ckK1r9fslAPiruG_unnYHl_8X1299Qf0dieFTdMxMjuvWrQ9b08rjdiYijcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaalauOwlY4WMCOTPedgr3xwv13yJxgHnyvVAv7_ONk-TK4n-h19BoQg6ltukWuHkt_Y1qADaqVgL3CUa3yg-x_vx0gUK5nSO-0lRO6zeC1AfyxsBR_O9vOgDsDdFRGq2X2QKqRhwSpBDI768Np7Xb14CMcm6J_p6-4W0al2QFQd1oloUa1rYHp5ku69rpJ_V5gAc6ri1zebAezGGxHtx-8qXyd10iBWDb1oKbxyv-U1mTeDpSrtJ0nWg81W-8KS2eyZOarN_R2c4fW_Ut2I3esSh-s5ckK1r9fslAPiruG_unnYHl_8X1299Qf0dieFTdMxMjuvWrQ9b08rjdiYijcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=iyYtldMuieX0E2N45O788_k9IKXtrPlMr_yb6SZkS59kEt1LTcxdaLJQ1rUSI8F22wzBT70qXL2R-kKnsWrVQMqGcvA2jvdb2PqdhmjsLSyJiEHIxxoKghi2O3f6HsCrVQUQxHak3sE7FZX90p9mhJsJx8vuAG-yx0S25IGuqh520JLH3rETKH28D06Gp3EO8CxMyE6dBcj_L9Z-2hcSKIlGyvwXf1t9MxIo0u1EHLH_cnM0EakR5N6IbrbSgy5EIW06_YKCX8wzHXrx3iA2Hq16c58J1tNSI9r8sA8CfjEqWmcZxC5DIQuMo6D5dxiS1-4StvWMvk8Gh1p9ycPvGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=iyYtldMuieX0E2N45O788_k9IKXtrPlMr_yb6SZkS59kEt1LTcxdaLJQ1rUSI8F22wzBT70qXL2R-kKnsWrVQMqGcvA2jvdb2PqdhmjsLSyJiEHIxxoKghi2O3f6HsCrVQUQxHak3sE7FZX90p9mhJsJx8vuAG-yx0S25IGuqh520JLH3rETKH28D06Gp3EO8CxMyE6dBcj_L9Z-2hcSKIlGyvwXf1t9MxIo0u1EHLH_cnM0EakR5N6IbrbSgy5EIW06_YKCX8wzHXrx3iA2Hq16c58J1tNSI9r8sA8CfjEqWmcZxC5DIQuMo6D5dxiS1-4StvWMvk8Gh1p9ycPvGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/br9-S2GZIrAKF3IJZBaqDwd_dSoMCNJ_WAvrKRYZ5HupHvsSLBl5ro7OrWA2ZtZljzVZcK5MVYnvRn2xu4-ziJkjGr25jXH_Ugpj7ZKxdso6YS3ovWrksENlgkld1aZ11Hds9IjTHkMs8qS8MiQeIc_26zGPc84MbeIfKUoMjWTxvhI0ZgCDrhjKWMsM6sL2YGrJsr4Xke1cdBC_OI-fo2KVIs6_Kzjb1D79iHSrNtEPHUZYBjMWRkYDDWp-OJ0AcEMBQ_yzIuU8TKb1T7oCCDs5O_5HmWLueIicqOqzPPVkUl8C5zqQxf88y-fi_7E9nLQXEgwZXiTPXSJFMimAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
