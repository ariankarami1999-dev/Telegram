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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 23:18:13</div>
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
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8TmlUukgx1CEMxrplBrST7mcORmueW5TPxmvJyYIx1gXuGnjch6i_jSD6dxQA9wNntu2S2uOLXXgZnMEc_5MsPr2YVuuR5OPlbKMSGK7xmig-nu01nyG8d6GkeyzUxn4tckbpN7A-DKWeZjdRctdIIw0vkX9V69l6raE4_Oinyql337INXK4g2riy7f-GFsi6GF3lhGhIcrg4xvRS6XWe1WuRul9AhWMl13Wrin5WVHXwbzwSxrMa9nxYPEhZaenXITHHcr7OmRGUHDdKQ7THRh37vPrCn9oMKyyrGIcOhk-lU7twZS7Bx-MskFFy87mKoeN8ggtc9CNGde889kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KQpL2hFUDPNY9I9StQRqA-Vtov96G88qq-3yTeMRM8TttXgZOgCmkJzqygWM1wBqhVoEDkZlBJFfu-GXRIOxISBf1_iLvd8M_jhbXlhvpLSmn5ZGSwCdpXh4v--oqJvoPS1sToqKFPntn15M3jIaZMqTqEipJPbpPm0nHKvotU-T5zIKwBD6Xb4F2WBcFpnxN6DCzphfqWS0O51s5m7iL_0OyVgTHzP9BEYokGFheP5nFLGHKkk6FXMY4y1gce-1BvpcoGsuAy0YaK5LZsxIUpq_vk_1eQx4yM3UQU2m-3zK4Gl8tk6vD0PuTFDtkLVKu0eYxOWDwyAan0OWQB_rMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUhVVbFQus5RFYD2NY-dmar7iX9sow41ilZEAp-Du_pWH-Csglhz32sku9BuUlcZ60AOtVkH1MmUJELRLE4nPLmWrPrn9wNkaQJ6RQA6igVhQ8nrZ-XNZ2r09Dv4rGo3pWd9POR0-lMA9l3PhQm31tairCKEj74hdTburssw8dWVN2gknHY21PNKpuICVg2aMCv7x0gxy9k5Q5KBIsq5sEkgDOlBjYJqwZCLpXvwu9BZkvN3MxmnjnT3jQolLEyCBNMBTpPW8zXNglc4nwLT9i2ci07CoNwUQDXJgo14_9y1-4qs8utnKRg5MHvhmDzB3q_oSDBUtDH4QlXbTYvcow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvi7CLzxEKwRHeWEy6cEekX5fes4ljI6QKhiOHW55MJWQCRbBfHfhQ8dq5YlErwYt_3JdRTU1kuwIpAadF6ITx1pyZbx784_H58-tT0z00J_1jnsYE3etcdkGTNT4EXPhOBW8HCb3BjXn8SB_8WBmcwU9aKyVxSWM4gDYoCAg7F8M2sSCbrNGZncSg_5fbawfRsKYNDhA4zzRGwwVq2XzMh0L8ShT2gt6ffmmxoX_15zypfdypIGKjpG3FETzItH7DUo7XryCVBfsseRIUxcS-edX7PImeePy8lKwgW0tRDU5Sd_40oPEPDfPEIWm_CUrEyCI2fq3JHUgrGNot5WWQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeXpJE7fLD6FMbwi23y3nw2fX0WN4Q5C-V8h_h1JJgKnJZ44dKlOf_yhHY8hI7o6CUd-5_I8RhX-7UIMXLzM9Bjv9aomHUZUEg3z2gTI-aNnoybDJqCjGOpK-GQZ4XgrYaezzPJPt_klWA_DSv1-PAkPVceSbIbJVJTMBfwLtVEPqQivsCuNouv2um3OCxq_iIKcY9YvW_spfDkOkP_UvLfUErJBYE-cUmz7HikLf8_cVXNzTqYCuC-1AOVh3YjAspfDTbzLjsIzpktdODHK4fN75d5ciacLlh4uulqiRJ7ebSmABSeHnUNUAHbNRs3YwIAuMjZR_nkeCW9GJ6TPwQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=FEDtGa-JcCnLVeUD_g308XJAZF0sNV7ludYPo0y6o6oITyqDEIkY3Ntfk3F9CCKQQ4VADKALZDvHIQq-PGnXDqsxhxozLgbIAvba2jNnF3qbjN1q_SewXs2GaQsQ6F4JBv6kHZSWaUebm_rIJpBkIdNKojeRjIFTT64nHtCu-JUhr5wsqdQE55cFucHxac6vriRQlXhYIkR1RY0CTJAncZhESzzgfkCL4aAcKbGu1uUVcQR62XNMNNSoKGw0y2zAYZa26L9B9OA_Yx2kUBvY61vmc_eFZmzqYvLPszWD2IPyD5YsFkDBXhyu4llPAOEoxDGY8yMTUbMKfgM6FF-0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=FEDtGa-JcCnLVeUD_g308XJAZF0sNV7ludYPo0y6o6oITyqDEIkY3Ntfk3F9CCKQQ4VADKALZDvHIQq-PGnXDqsxhxozLgbIAvba2jNnF3qbjN1q_SewXs2GaQsQ6F4JBv6kHZSWaUebm_rIJpBkIdNKojeRjIFTT64nHtCu-JUhr5wsqdQE55cFucHxac6vriRQlXhYIkR1RY0CTJAncZhESzzgfkCL4aAcKbGu1uUVcQR62XNMNNSoKGw0y2zAYZa26L9B9OA_Yx2kUBvY61vmc_eFZmzqYvLPszWD2IPyD5YsFkDBXhyu4llPAOEoxDGY8yMTUbMKfgM6FF-0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=M7jalGPIqgfIePLGumCh3cRU6P9Cr-FuZlcQdMcoz8JOEXfc1wDMgWIcY10D-ZbJpV9lkrrkUfT7U2NkSpu_UypabCZ-lgfiZhwaq6owjtlgU7Y089DC7UFdcfwY37evwABim4sEGcMAlqPmsQaqgjdrL8lv9ActmnubSW-NYOeauDOKALquCkmmxCCCheZXZmha96CrbRieOJZ3-DaHwBmi9Mov6_TIOOCNfBtlPERg5xZQNDWwZg5Vq6oAGQrr-5TapwPbFnmgVsLvrkmzkvyH4mV5vhqiMjwv4C0hGMUpR2nsuukxKuwQuGAcIuSYBweEcDWGWRauYj7fReE_mQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=M7jalGPIqgfIePLGumCh3cRU6P9Cr-FuZlcQdMcoz8JOEXfc1wDMgWIcY10D-ZbJpV9lkrrkUfT7U2NkSpu_UypabCZ-lgfiZhwaq6owjtlgU7Y089DC7UFdcfwY37evwABim4sEGcMAlqPmsQaqgjdrL8lv9ActmnubSW-NYOeauDOKALquCkmmxCCCheZXZmha96CrbRieOJZ3-DaHwBmi9Mov6_TIOOCNfBtlPERg5xZQNDWwZg5Vq6oAGQrr-5TapwPbFnmgVsLvrkmzkvyH4mV5vhqiMjwv4C0hGMUpR2nsuukxKuwQuGAcIuSYBweEcDWGWRauYj7fReE_mQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=RVOFVsZxhniarZyKP7HCzz2tV5yYxGHgt7tOKCyBjYBSiLYNhSgH5jjw9XBiJ22-RsFeaVsJ3hWNlh725Ltv_3vw1F9ufhsiA2MvPLQfe5NtYdTIa9V_K-eAvGuEHjvVKxzCxGYrSuHOlGhBuJQ0G5kZpyvolu-eu9M854inyVJwIiqeqMESZqL9z4l5Dks9Ys2mSg0TMrM5QEgEhYZ7kTuE68xhZ8E-Sltm8Fr3IWYTWmcFUZcl5vvoCbGio4tLch6a3p0Khi5B-NDKLV3ad3j9busA8z3vGunl54tMNtFNCS9YY1SH7aTSW3yj-pjhJcssodSNnqzEKWuRm4xrGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=RVOFVsZxhniarZyKP7HCzz2tV5yYxGHgt7tOKCyBjYBSiLYNhSgH5jjw9XBiJ22-RsFeaVsJ3hWNlh725Ltv_3vw1F9ufhsiA2MvPLQfe5NtYdTIa9V_K-eAvGuEHjvVKxzCxGYrSuHOlGhBuJQ0G5kZpyvolu-eu9M854inyVJwIiqeqMESZqL9z4l5Dks9Ys2mSg0TMrM5QEgEhYZ7kTuE68xhZ8E-Sltm8Fr3IWYTWmcFUZcl5vvoCbGio4tLch6a3p0Khi5B-NDKLV3ad3j9busA8z3vGunl54tMNtFNCS9YY1SH7aTSW3yj-pjhJcssodSNnqzEKWuRm4xrGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=NlbUI19q1eiB3Yi8dkpwiApS2sLHFcK8QGX9oigXsyZ2dci6vWs_AWgvB4labgnHxDJmAdK1XHyk1M2J4nDmAovKNV3iyz0S-92DYDdFNEvEQGGyaQpjbOHPXm78DUgIO_NN8pSMeKXX3rdXcam0R3ftBBo9l4MbE2zwxxvQo_g0Yc5Z_H3jylVVIFbPZ0u8MRIpcRKe252c7tvgIsmuQkg6Ryg3NTGa5R1bUJfxcpqNqLzUxc14ZP5ccG7usJBFgLgGbpmKUZpu-XrdCy9aL0TcHXWzNArQGE3wy-bitKKNhkHycLG3kDAgu81QBuXEE4T4IFPFhdWu908F_ceTFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=NlbUI19q1eiB3Yi8dkpwiApS2sLHFcK8QGX9oigXsyZ2dci6vWs_AWgvB4labgnHxDJmAdK1XHyk1M2J4nDmAovKNV3iyz0S-92DYDdFNEvEQGGyaQpjbOHPXm78DUgIO_NN8pSMeKXX3rdXcam0R3ftBBo9l4MbE2zwxxvQo_g0Yc5Z_H3jylVVIFbPZ0u8MRIpcRKe252c7tvgIsmuQkg6Ryg3NTGa5R1bUJfxcpqNqLzUxc14ZP5ccG7usJBFgLgGbpmKUZpu-XrdCy9aL0TcHXWzNArQGE3wy-bitKKNhkHycLG3kDAgu81QBuXEE4T4IFPFhdWu908F_ceTFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=rLN_ONiOTa1RtsWDuXNg0KzY5p_M8x2_ozw7Eyec_IpnNk4u9QK3B12pkUB0zpyC78NrGupkCAoAp-a-niILTNSc1s5bkboxfFtikKSK09srRjklmf8LkbYtX_Idq1BOYxGznIz2SytMNnAmbCTvwlxRE2Q60Vt2lSoGYhjqt96fBcNNugVC9Ww1abOHo9Gmhr627W6CsAXCB129PFiINa_9B_AhRbHuMZLnWyGLaZJe8m2UokjY9Pv16iDr_ADF2P86DNS-vQIRVx4GddJRPnAUwIpRp5qDsmA1YuP1_2nXUZs12FLvlzdHz00c2Z2yuWg1dBrGoEjrKQHBXEs-Kw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=rLN_ONiOTa1RtsWDuXNg0KzY5p_M8x2_ozw7Eyec_IpnNk4u9QK3B12pkUB0zpyC78NrGupkCAoAp-a-niILTNSc1s5bkboxfFtikKSK09srRjklmf8LkbYtX_Idq1BOYxGznIz2SytMNnAmbCTvwlxRE2Q60Vt2lSoGYhjqt96fBcNNugVC9Ww1abOHo9Gmhr627W6CsAXCB129PFiINa_9B_AhRbHuMZLnWyGLaZJe8m2UokjY9Pv16iDr_ADF2P86DNS-vQIRVx4GddJRPnAUwIpRp5qDsmA1YuP1_2nXUZs12FLvlzdHz00c2Z2yuWg1dBrGoEjrKQHBXEs-Kw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=OnL1uC012HldEz0azcO-hpVLy5r6yoqi4H4wzb8s-w4JWgifnBLg-8M64MwDR1wpwMttC65e0Km4VzDpAc2F4Ik3n8QwoiFe8zTFE610_vhxYlmPvpQE-9hGbBbBN8BNNtphLeP3Oc3IkkmT6swjVFVo5ISxoDnz1yWVbD9VWQpdpwYfuCT_eQwJynIt3DG9N9gbnTh4wq9iIyYZ21qZV3hA6ksWEcpXxFSHB5UZfPBWeLelwwb_qLaiEVyZem16dZBggAUj_d3tyrQG0Tjm1-AwE2nwFJ5TwOxoG0t-qrbyIZt94iSoYw4P-hBIoyh5Kuhzqzzr_qtzUolIcXIs7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=OnL1uC012HldEz0azcO-hpVLy5r6yoqi4H4wzb8s-w4JWgifnBLg-8M64MwDR1wpwMttC65e0Km4VzDpAc2F4Ik3n8QwoiFe8zTFE610_vhxYlmPvpQE-9hGbBbBN8BNNtphLeP3Oc3IkkmT6swjVFVo5ISxoDnz1yWVbD9VWQpdpwYfuCT_eQwJynIt3DG9N9gbnTh4wq9iIyYZ21qZV3hA6ksWEcpXxFSHB5UZfPBWeLelwwb_qLaiEVyZem16dZBggAUj_d3tyrQG0Tjm1-AwE2nwFJ5TwOxoG0t-qrbyIZt94iSoYw4P-hBIoyh5Kuhzqzzr_qtzUolIcXIs7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7OZl6O69vIojT_0fiE9y3R4rabPnZcfzkyFRY-83InoneDUqyFG9mbqDOLI_FBQqMjf6vYMs9cX7dlJdU4VPu0D3MENs--zcDot3KgfklJyttNjmNToCjTMxeAWppSi7S5P6fxz8EnlqA2wYLOFJjQBlZ8eiOpT_O_7YnVcob2TgQg76Nb2ulgNkFbJRcFB9yJHd9C36AHf3L4Z9rrCZH2KEeDMDhynVqmzU8fojGYHGpSmX_nZp_-4CTIu_pIN9J3kKFtu77I6oVFwDvZVWH00hFTfLj5f9PvtPKYIYMAJ0AkHxePJsl7Q2sWuZqzKYllulTNU-tFxzNGZizd_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=lUWsDr7hW8zaE2py4k7Bv414ifZI3tC1q0CESGlzgI82wRos5zXhz7qjhtLLz88UwqcOn9BHtCQ6bA_0wWU_ccvcBZB3TQGs8iHhwRs62phP8Rq6ikTrUcaRuf9guEOsqVyrA_oZp3SY0epCdBmy0qvaX4JP9hnVWTFMQhKLfh2OBCdpMEm2OrIfBVGCKKy5dUICkkbr-hrF7b4bvGBO5uhGtr961q4x-1_m3wGv-owLbHupGeKgeTA0PNdCrY15PEkJhtdD9pjBM0hXHEJ2g81S5vH6iDBTvfSkiIE6JzqlWxYgIs7Ng1giMsdF1lzf_AtObMsLZxq8nfaqite4aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=lUWsDr7hW8zaE2py4k7Bv414ifZI3tC1q0CESGlzgI82wRos5zXhz7qjhtLLz88UwqcOn9BHtCQ6bA_0wWU_ccvcBZB3TQGs8iHhwRs62phP8Rq6ikTrUcaRuf9guEOsqVyrA_oZp3SY0epCdBmy0qvaX4JP9hnVWTFMQhKLfh2OBCdpMEm2OrIfBVGCKKy5dUICkkbr-hrF7b4bvGBO5uhGtr961q4x-1_m3wGv-owLbHupGeKgeTA0PNdCrY15PEkJhtdD9pjBM0hXHEJ2g81S5vH6iDBTvfSkiIE6JzqlWxYgIs7Ng1giMsdF1lzf_AtObMsLZxq8nfaqite4aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=DVFzyluWqSd8QmDZ0GhD5627z7mZG6xWsKjYGr-QSEPATlziZNqNwBVPtu1D3ZkF5xa_uZ_aX4E55oyVuZAzQOhYYckCappDj-vUu-oF6n_WRqOaT7v0FlnK4gHyUSuUw7uJ62PDoshyfoRFxpUfHMhh7pzW4tuNI4JPWezpqxrmbJJ8BgN0MuQ1mSLcUVTsF82y2mT-slU71m41LbDYBA-mH04vRB6VXCp9iosgcfGFoKI8ldkMaDMziUBnwgZQAoR76Z2j5rMAmdy_cvbD9VyYP2O3_St_V6AoBwYOJ2IEC_1s0uS90mFSX4f_NP8_ZzPKxqQmR070-LHYCTnB7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=DVFzyluWqSd8QmDZ0GhD5627z7mZG6xWsKjYGr-QSEPATlziZNqNwBVPtu1D3ZkF5xa_uZ_aX4E55oyVuZAzQOhYYckCappDj-vUu-oF6n_WRqOaT7v0FlnK4gHyUSuUw7uJ62PDoshyfoRFxpUfHMhh7pzW4tuNI4JPWezpqxrmbJJ8BgN0MuQ1mSLcUVTsF82y2mT-slU71m41LbDYBA-mH04vRB6VXCp9iosgcfGFoKI8ldkMaDMziUBnwgZQAoR76Z2j5rMAmdy_cvbD9VyYP2O3_St_V6AoBwYOJ2IEC_1s0uS90mFSX4f_NP8_ZzPKxqQmR070-LHYCTnB7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKrkQPSom-DnUwe37S9vHNcv7spgnyiZAN7MLvm4vUoAb7ogjpzx3OqynCBljqOH6F861ndeBcXWGPSCTmVQWHFAFqfnFRwBvSTsSJXH8x__hlkg5NCrXbvu7THRk2hzsTgBwfIgX3PswR_bC0F49zZxy3HAAYjENwPIOp2nXtL5iQUSDAW6zRExmnTDs1f3wwljPl18hWMWPMWgD5Byf5RMYuET-4BqaBG6rTCOgXyJ93m-gEo34l_ogfCOjSXuiK4FKg1cZ4KyKgPY3wQV_K9phdMxDg-tsGZBM6AYpIbM4piN685zHRVkQ2Xum5qoxADJulwvWc0f5t_EZBY-vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sQMQU7DsXIYo4zIblK68A_ufSNQb0EQFnYezsgh1jL-pW7twGeCFvi2KfCshE12KtlH-sp0Pa-pqS1B4ZIe3tnrE9DtLJL65iTUL8neEMkQ5ZFv5zG4yPzinVTY-Wdttlngd6c3QG8WnpSbIimx3M3KCZ2THXaPF9oGxY3lbPNblgi-jh8AOUui4bAWIjleqRI5qnlNuLzwFfOQ41qh-yHubUWM6V8GHMm-vN08HTwduK12_jj_hSVqBraOigzBoSTgb_p2d8vznQUF8JkhRQIcMZzwjEU8curndPHAoyRsjyy-KsR7CcaC3QE96bJCTjFVWo3_PNAt7dPQPXVDgxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwqYGMgNKDe8ns6gMrnHLLdRTLDrElpZKVk7H8eTqK7rsMRAvCgb-kyD-U4K2JjCIYbuzpoJH0ayjder1vhE93kEc_dKlcZPYGwenY_KqQQUuuY2ERNI9w_G2_U3wMQ-Ao3eYZwxJGCgn9B-wb1DHvqOA8Lv3IVkIH_bF8yu7WQoQV62Ymy16FWCzvp5qbvxbXi0QytN8T3U6AX8e7ouq207mrSbx2pqHYQF939TqDJFInayGD94SwUlOYXO06V0ffy78c3GQ1Ej_lLSkq0mi7a62M0SZYY9efX0zDB2yL5vtLLA8LcFOHb2bajiJMgXUUkMADZ2vT6MghdHt9TrCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLT_K1-B1Suu5Tnub8z_A6dtrqTX51NAn8PAzPPBRXnAg3S4V7THlYhaUTjZbJqwTIn5DSuJPZ16OLoa2Gk8RQnryagozpLQHbGOlF5ib1RnoBzrYpTVnjl3RjqjC4llK2SNeVxTecp1iPT3B9GxHTgw-rFLS49g-BwiLSYKGvSXcyHSbECKw_rx1RE-Q-lgTqE7QDaddJJKCJMdAz8Hya4kQDr8V_q09fLirLL9izTVK0ABNuAHwi-0uCeQAh87U6PN7XiqzGhmiECVv7wuzUGsZEYKtyTHFVaSi0U2LhabXoJmuzQ8ynIsRhgAdRO_9zdv1dISDoU4a5cqzWSIJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nqEvvHftQhvK6Q-1JLGFv0JkB2ENrsqM3jNqaKqWdT-W8tY2YJb3fSRHkuAd9FAvhPnJl5ckQ0yqBZ8DW9Vf_eyccTIGLgwkomA7eX2rWrEgen7p_av1yMmHRiyWknB81HXGnKN_x7PSWaOUJDQmW11TPV8dznfErMBu8BTJsZfwtNXhrvrGUcUrHqKCQmgASGBICHvuNVkg7jurxQ-A9O7oF-pifGz8E0Nq4J_FiR9JFcJl2E-IqKciUHHsHGOH0Vpratfl5goPWOTzqwFRawaUjdf15mwZiOgbpyDHQrC7XvROJuhXH5GGtq0TgTCwZkprZNG01cK12lhRR7x36Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ghLvr89M4k5chTScy9XkMl-0OfEpt-AarSJF-Z3fGMnvJvhx_KBBKsW7h0SMAQNuXD_OF2YeUR7xFkVvrV8wYj6715RdBNB_9WTK6gqGyNs8Zhv1rWkDjCdj3DwJACTyr4ofpxs8P_tpEhYkdn0VUzopxen5hN_UOpTV7HiysWyyjpcc3xAAabAM0yNeUPJ-6xQNTY54E2RLvIH1F02SG9KMiv-T2A8uxggoueRGTCBukERT8_K95cqorj60XYnknZuJfEU_-zTasQKGnd8F6Ec6L1HmK5lJrmD6RZbITkNuAnqyRjlWrh40ekUFmCG_igxIY2UN_RwdYEqcx56hHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYYCADlkvJ5FzqmMiTbIovMBjm9jtxzKuDUb2u6KjvjHc2_ti9V7ENAeFI4DL_PSrqTf5QjNFXcw3qG6E9ihVxYSwMBllh2vR6F7Z8A9cUmLVq7y43ugXzO3eZQjwvf-R6bak6ku2lXrPM0ODHh0Y0EeyNEEtQNgeBUU8VsgtJUkGwRU7s5AE4V9pZKeCFqMc0shGzibTz_AlWatVBrbxUC_RowMBUgGwZ8niYWpM8hOf7fOT9xv30155P1dtWSymRdztwtnBs3WubllbpVUiNmwS1gTY_HYUAOKd9AJnrDLPRFleWReMUrO1yBzjq6ZJZeMsg3Rpdf7TJx4-xJLEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/si1qLRKlpJd0oUeHegswxpSCSHTGQeSB_AFeFbDFMv4-tDEi874ydPL5NyfL3C4wecYi77yy6x7ptf_-mJbnLdSy7wDK4T4gsQUXjCBeNiUbCf_N3z8z7SPNZZx_u6ZSGRSwxbdAPbVPgeNoQSv0-x4oRhQS8hpLX-HkaFTOR7_-Ss065RlNCZtdlfYOgqnuZBxh_ziHtNKH3Uap9P3WaX-puc0TG-OpuUO_BTGH5G7ytI4usTSUGFPWYofd6WE8qjSIMKP_Er6CFNYGHrVtZpptpOOuC8y_Cm4rXDvmiBWm-JD8YKJccR8yAz3SVjAxwqvX_NN2K3QT4xPUgHe4gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAxU-MLL4QAMJIYNvH075TrQc58OUnjErBEL5ye3dCsR8wdZwo4BQG8i4NB69zJS1Hb738REYNhwb0m0DjxDXsaZaIXSPMk98E9Lbvx0U1558FR4tyZc7aUh7xUjVUMP38rMK2qkTmKTGWsJJxyy6I2XJMwHQ-ME_95l86yBRx4ntuY5OUnDaDXSj0q5p53nF-sCgA3H7jldFddRDkfdOKHxM_xwJUQnKZ8snEUYs3Sy55X4VOm01nn8knsos4jlmCHY-ctkdH93vPx_05hpLFwra-MdKlTOedSwuZrQGgvZJOyF8EwDzxPoO8jESaaRMAGw65svC-JP6cjbtNdg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f7wMs7DmAV-QH0-Q3v2bUSNTX8ra0V-W2kGZcI8mpdz4yAPt5jv9gLhTkwVpveh-NqkU-Cg27jB8TDZjD5y6J2tsGETmmkRhikIQ7x6WocLcay0sRTgjPKePiXY7mxa10DL5r1DbvIXf5qhruEE-wWovTl1YTvbj53hbekTfgOtinctphq-23eR7NOJe72KbT0yNEW9s9gYeCp0BrpFFWaQpdhtSmPCXBlSeiW3PCQ0p_MPK8UT19htDI1RlBD4reNw_9M27uOAnC6oNiDs7lsLbDhGoHL7IREx1dWIiPtYJmUMu6iY388lhcL6wB8lqbGIYkghmrexxPJtkklDkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DA_7wjg3LX2LkV8VG1KcWteIlMv--NIaaJmFsjODUWNf5sLJI9K_UFpBeJcHJZaJ4QALs77hNyc6aKWzcRkzfoVgonm-aUxnoKULluYTk7JGATVk8khCN4ix2Z-temusbBxQqRmIpEMcXDLo7z-Qt3SvBGS1T8m1gnd8V2CpPcan9HFML-nWFRB19tVnmsymsou2wD3U64Xgv0iCeo8d7Sr7d8eCWvzrphDLP5_LSDSn0D7WoE5sK-ys8nqPf1X49BjxhfYHtQyzWah2IrZDwwmb-98CtilwhqGG3xrRRubJCrNQr131I8KmAxm1qgRiM6YLsCGiUyrP-wn7GPT8Sg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=DqgZg4RdO9IcIrFCvZNxWgNGuvKB_NpahViHHQ2uIttIEs4PqicfPJ3_DgFqzgsHsYee_8GgjPXSoRF9LaqAixAyB9UA6J0xWawFOP9UkZwPKBQCu_wOzGlIjGQwsFSqhe4ZUYQhfI-_dtx9ZOq2scNAnySDJeFQE_ZRZsmJ7gUcg7wjambbYcHgKjGlmcb7g9IF8r-TQO-a5I-V63BVvu0xY67ho98uKJoPqdNno3XU30-0Qk-N7jAlwshxgwTP-9M8DPyR8cxLee1fW05_dqawDcxtooun37kp1MJLU2J_QRLVTivfgOJC0VsxqdIqtN_fOMd6SmV6Kmw7vcC2Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=DqgZg4RdO9IcIrFCvZNxWgNGuvKB_NpahViHHQ2uIttIEs4PqicfPJ3_DgFqzgsHsYee_8GgjPXSoRF9LaqAixAyB9UA6J0xWawFOP9UkZwPKBQCu_wOzGlIjGQwsFSqhe4ZUYQhfI-_dtx9ZOq2scNAnySDJeFQE_ZRZsmJ7gUcg7wjambbYcHgKjGlmcb7g9IF8r-TQO-a5I-V63BVvu0xY67ho98uKJoPqdNno3XU30-0Qk-N7jAlwshxgwTP-9M8DPyR8cxLee1fW05_dqawDcxtooun37kp1MJLU2J_QRLVTivfgOJC0VsxqdIqtN_fOMd6SmV6Kmw7vcC2Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=NfTJ0lMI36UqLrChw3GNG5XytQZBCZ5zizHHT6YAkPQFPpoyJnukuUd97XCLb3cQJNoc1lolg7ICLn6-42ffXEnTPNjCm_45C1ZjxbDUrylLaBS6HauVdDecgAnTx5_ElrUvinG1wrRpq1o6VrPLIL8N3Whhi-53cD5vfvZgiY6wmtOntZo72BVvPFqCaIB8bVdRN7QrKLjjxtjM-oUV7fd2m8zo2m7tR2HeISKHbZ1UYokxb7VygLa2K2jH8t07W4GPGqRwlCCy5kVQ3hqLyXFFi8iDEbkRRhIv6BikyHbNZJDBbhm7o4U6pDrtXpPWL8avdn3-IWahLqell4xMVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=NfTJ0lMI36UqLrChw3GNG5XytQZBCZ5zizHHT6YAkPQFPpoyJnukuUd97XCLb3cQJNoc1lolg7ICLn6-42ffXEnTPNjCm_45C1ZjxbDUrylLaBS6HauVdDecgAnTx5_ElrUvinG1wrRpq1o6VrPLIL8N3Whhi-53cD5vfvZgiY6wmtOntZo72BVvPFqCaIB8bVdRN7QrKLjjxtjM-oUV7fd2m8zo2m7tR2HeISKHbZ1UYokxb7VygLa2K2jH8t07W4GPGqRwlCCy5kVQ3hqLyXFFi8iDEbkRRhIv6BikyHbNZJDBbhm7o4U6pDrtXpPWL8avdn3-IWahLqell4xMVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=DRT_Iid7qfpTxtQVocJKM1AtzFqLTtN2JdTgzO7HQm-yNy0oedYbnlPSTl8o1UOmbNAb5f_jbt1RLH-RMzEl9Ni_-2zHE1SxaBWLNzrR-mMtu0jhBBDVh69lxRBptnkOzlPQTnfW0yk5bNeKtniOKcdazWHUZXlIPbT13E7QrRkytAaMRI6qWA9d8hX4rFEPDUiMDuH5UPh30FPrDo-yVnNl1Kz9fuUp4qH647mVjI0EZtOJ3AxUBtdDf_pP-ILFXDq8Y6OoS3uIfmlqzLnRbVBIIcu9JZqsLH66cvcSD7VdfKlB3JC4lBxEbPltdKcrHPb4WFC69ydLyRfP6Y3XQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=DRT_Iid7qfpTxtQVocJKM1AtzFqLTtN2JdTgzO7HQm-yNy0oedYbnlPSTl8o1UOmbNAb5f_jbt1RLH-RMzEl9Ni_-2zHE1SxaBWLNzrR-mMtu0jhBBDVh69lxRBptnkOzlPQTnfW0yk5bNeKtniOKcdazWHUZXlIPbT13E7QrRkytAaMRI6qWA9d8hX4rFEPDUiMDuH5UPh30FPrDo-yVnNl1Kz9fuUp4qH647mVjI0EZtOJ3AxUBtdDf_pP-ILFXDq8Y6OoS3uIfmlqzLnRbVBIIcu9JZqsLH66cvcSD7VdfKlB3JC4lBxEbPltdKcrHPb4WFC69ydLyRfP6Y3XQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=kIxVHWvfC5TvMpNKJ1b3XVUqt_D3c4Yow6zUNM7z5iXcPS_VMIX27N7cELOO9ZO4YTll5XyxyvfXRKWYkOuDtG5sAn8POGgScB-ZmqMj-KS-Nsu-0K0YnhJu8H77lWbtN-hzJxX6_VSKSzNtc9vT-ROqUDevc_OBwEGiM6efQErqqW8DDGc7nEif-b1Qh5WKWtPy6WiU2mlmNqf3O5DS7UxP0yRV94OUZb-54iGq1F9M7UTWr8G1ik5pIb8S1WB9lOlbKcRuA7-U7fT3z4u-RwOIh9QPiIiGc6XMiPxVi7dwNEE24hxGfbFnjATui0q6UtdW-cjZfXqbkXbzjiTBgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=kIxVHWvfC5TvMpNKJ1b3XVUqt_D3c4Yow6zUNM7z5iXcPS_VMIX27N7cELOO9ZO4YTll5XyxyvfXRKWYkOuDtG5sAn8POGgScB-ZmqMj-KS-Nsu-0K0YnhJu8H77lWbtN-hzJxX6_VSKSzNtc9vT-ROqUDevc_OBwEGiM6efQErqqW8DDGc7nEif-b1Qh5WKWtPy6WiU2mlmNqf3O5DS7UxP0yRV94OUZb-54iGq1F9M7UTWr8G1ik5pIb8S1WB9lOlbKcRuA7-U7fT3z4u-RwOIh9QPiIiGc6XMiPxVi7dwNEE24hxGfbFnjATui0q6UtdW-cjZfXqbkXbzjiTBgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=pcdpRwtrxKX2YTHGj6crXSBYtWGx7qV8mgs8ZHkVkHao0F6CSNeebYK0ZF6tGLY_D7qhO598fGMdb8CrMhgyi62il6VeJsEgN8vYljsqh3in-U2BQksIYgLo0B0RlAJLrCzKWzd_59_40zboi1vcokCAW5Tf7BR9ZEpr89LVVYJJEguSkhHdCa2mPc912qeGttl7S1NOT8nDjaVsustDq-QXEnRmFo6dfsmTgshBKH4HH7gImXKHcQTvY-zvH6cHFVmGB-Zbzr3qtVr_mYYcEFgYQuTKyFprZCh0iGhrY2z20buz6LrVCZX_Uf_CA2BJpnrgGDohy75RgoI_9vsLog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=pcdpRwtrxKX2YTHGj6crXSBYtWGx7qV8mgs8ZHkVkHao0F6CSNeebYK0ZF6tGLY_D7qhO598fGMdb8CrMhgyi62il6VeJsEgN8vYljsqh3in-U2BQksIYgLo0B0RlAJLrCzKWzd_59_40zboi1vcokCAW5Tf7BR9ZEpr89LVVYJJEguSkhHdCa2mPc912qeGttl7S1NOT8nDjaVsustDq-QXEnRmFo6dfsmTgshBKH4HH7gImXKHcQTvY-zvH6cHFVmGB-Zbzr3qtVr_mYYcEFgYQuTKyFprZCh0iGhrY2z20buz6LrVCZX_Uf_CA2BJpnrgGDohy75RgoI_9vsLog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=Yv_N9F-ZkjB2GIB79HDEZNFNGTYNElIaMK7eur3_YPcVrbEDKGSMEu96yiGvPpVrQajXQnImSPxER5Jo0r19-FDnHvYRsjx5_TuVXwOURuSJG2RmA1FND9nCvb1fVX8cItIQ26rz3BEDlUC3hZkfl0QDsrXexb06iLIziqTKZJBkyGdNODYiR-ks83PzlfPl14SqYcKrrmxgC4SO9c3E0CrA-B4Qh6pxNt8Az5qFL6dc-AstfAYa8sWoZ2AT5NM-Nw1L1dalJhhvz77lwNwQAgol3vr2qfIR37pKpgWW4c1p6zCVAffZQKFHIfQGxMRXBg1WJ-AdtGLa4OlA-c8xyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=Yv_N9F-ZkjB2GIB79HDEZNFNGTYNElIaMK7eur3_YPcVrbEDKGSMEu96yiGvPpVrQajXQnImSPxER5Jo0r19-FDnHvYRsjx5_TuVXwOURuSJG2RmA1FND9nCvb1fVX8cItIQ26rz3BEDlUC3hZkfl0QDsrXexb06iLIziqTKZJBkyGdNODYiR-ks83PzlfPl14SqYcKrrmxgC4SO9c3E0CrA-B4Qh6pxNt8Az5qFL6dc-AstfAYa8sWoZ2AT5NM-Nw1L1dalJhhvz77lwNwQAgol3vr2qfIR37pKpgWW4c1p6zCVAffZQKFHIfQGxMRXBg1WJ-AdtGLa4OlA-c8xyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=v8bQ6_MtNubFUGDLdt3-WqfOUNsh1GiCYvu3zIpQv0cNi6kzfEMaQO5kpaior6K-kEH9ylU-a2NGT6qquXYYfYRJTBO3Rjx6QOXCPip7_9KvgUnjm0HM6bAzAnSwf9O-5nv3O2LoNWQhHgDWycXYiELvJGxp1IuP1CzZ_f_W1XIwWztv5UFWykqh1OAcSSaFqmRTJJPdrt2D-zgTXyjhAGZedHfgPDJ-ht9xSBzZUpy_YauTxOzEhhxcGZ28Li4PpIYMY5NwDa3Gz0kyT3H9cs_NzbC9tj4SSMxStvm9o-3hdP3vEk6HcxGCMPSG7SzMIu1QTek3YYAQLaJ9jKUBEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=v8bQ6_MtNubFUGDLdt3-WqfOUNsh1GiCYvu3zIpQv0cNi6kzfEMaQO5kpaior6K-kEH9ylU-a2NGT6qquXYYfYRJTBO3Rjx6QOXCPip7_9KvgUnjm0HM6bAzAnSwf9O-5nv3O2LoNWQhHgDWycXYiELvJGxp1IuP1CzZ_f_W1XIwWztv5UFWykqh1OAcSSaFqmRTJJPdrt2D-zgTXyjhAGZedHfgPDJ-ht9xSBzZUpy_YauTxOzEhhxcGZ28Li4PpIYMY5NwDa3Gz0kyT3H9cs_NzbC9tj4SSMxStvm9o-3hdP3vEk6HcxGCMPSG7SzMIu1QTek3YYAQLaJ9jKUBEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIkDAJvPNHY4BYRuPJbMCJori5uZIx5wuSSZvwf7Gz-77_FKp379x0DHuc7yF2_-D2NxOr8IIz9zJEN8FqWY52LQQHyQodbyM10HMmvLX796CPxMRFfSj065Uei2zgbqC_cpOWfYyvtHxn4K4VHn-KjTXBDaDWLRJdwuEeqnS5nlqZPHYN4YbieaC4U6tiQbYXI-n1Qx8eXMMyfDjuYBEVOjr5B9niGK_t93zX9ejc0-ijBIxm4_SiUGJuImc5SwPE2wGZhsxesf96iZfzVTDU9Q6q3aqMkOdFSfUhHzHkUK4S0JaeHa82G6zYCxZxve-hVqAEPenIHNUEqI5RwvmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=e6velsGeNVY3-dpKxViQwme2dy8T0SfI6lrSJJM-WNT50OFCHdAs-8g2WjoB4pEH5wy-P73vXAFmE8kRIeoo5fpFg_zCi2WpINXT-sq8xT6aSkykbfrjXYOYzENSMeMDoxwls8E-bAjugLOQt01gP0431Uo7CQs0nk4OvtJsf5tz64oT8MJkj68KOUFlPhc_qQilwDMRolN9PNmlVlW_KEBt4gvgAIgIlFnxK81LYm9CwNyGoFH7qymb76YZ029KxlwnqOFq1eBy3fCG4SexyOjju7ofIwlEfP4vFt0N5lOB-X8G99o5C68vz4B08f2CNr5WJsmM_Bw6Brjb7aeGxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=e6velsGeNVY3-dpKxViQwme2dy8T0SfI6lrSJJM-WNT50OFCHdAs-8g2WjoB4pEH5wy-P73vXAFmE8kRIeoo5fpFg_zCi2WpINXT-sq8xT6aSkykbfrjXYOYzENSMeMDoxwls8E-bAjugLOQt01gP0431Uo7CQs0nk4OvtJsf5tz64oT8MJkj68KOUFlPhc_qQilwDMRolN9PNmlVlW_KEBt4gvgAIgIlFnxK81LYm9CwNyGoFH7qymb76YZ029KxlwnqOFq1eBy3fCG4SexyOjju7ofIwlEfP4vFt0N5lOB-X8G99o5C68vz4B08f2CNr5WJsmM_Bw6Brjb7aeGxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=qEpCbLpb1Q6VkmNEx1iTvH8mUUlauMEFG1izI8zvq6-i74PApDP5coxTElgo32cj61hPX3Wfzxy60ParnDf0IVfVxUAZ63hybptAmTGTojlqnlf4s0KFw-53wId-ZijnkTGwRqQ58vA2NSevATtDmBA3ZLBUIb4-eCKlVQwv5zhDh693S3gcH4jZ7FafIPLHFr7VBnK9GFcpjAmIFmuR9bD6fGkEfNlsQXGQswGbol5xLPkm3oubm_81U1rskYEcLDgMr4VRQAZ3rj-e4ZW-jgUwoY-AmG3AfiKdETMVeUsRzn7o0BNXVMMPvpGT9haETwkd7qOm6T-n9jgtR90SuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=qEpCbLpb1Q6VkmNEx1iTvH8mUUlauMEFG1izI8zvq6-i74PApDP5coxTElgo32cj61hPX3Wfzxy60ParnDf0IVfVxUAZ63hybptAmTGTojlqnlf4s0KFw-53wId-ZijnkTGwRqQ58vA2NSevATtDmBA3ZLBUIb4-eCKlVQwv5zhDh693S3gcH4jZ7FafIPLHFr7VBnK9GFcpjAmIFmuR9bD6fGkEfNlsQXGQswGbol5xLPkm3oubm_81U1rskYEcLDgMr4VRQAZ3rj-e4ZW-jgUwoY-AmG3AfiKdETMVeUsRzn7o0BNXVMMPvpGT9haETwkd7qOm6T-n9jgtR90SuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=pez9-CVGPXe9RSliuNj6IodAC-Sm9EFh1TdgJr3E-0rWAhVfKu0OcsOW8DRSaBvhtnskFGadVHLjzBXKE-vnG6tZiRlWzw6jZX2tdtJdgbkogbRs6IgaWPHeEtf0lz_uHglZaMb1dq7-SEtMfbYtEEenHv2UsDteB1MpJeyYwYIPISlSV5-S1O_dLc0Zyfyj_LM8Pki1CLOD-An2x4bJ2TFS6HnaWI0nOFUsqUO623MqmQLbKZGM2ZTnEwOA_GT-FEcXAgdL6Jcm4mp3ERkYelXREnmOv1n5k_zL55bXLJ7MwMTgPI1jybmg9atekvp-NBE7-uyN6m5Wa4F_O-gboAf0WCELqTe0AYUk2-BCEiuWTTCWTTmT-k8iqFLI8vYD6gWKaf26-L6X3oVe_3FUth2JV8jPWHSz9EoFdmn5AxQKmqSOh-IqGsKfCQjeb-f-Ru4cWd85TzlnqXirbxkJ0Yzx0MnMJifDB84zFtT8oppdaw_jyZYLI-MkBh7OvXyIJGrVRcFRNZSUHMKqs5Z_AyBDWuh7t2K60YxTH6McsAGYaq_aKeqZ8CPuZeoYCmLPMkMp1hNbr99THeLd88s-EXV1UbywEbMwrJnZn9mMB7C-BEs1OB3PCU7zyH_AOU9FuRvBa2vNQ23ecrZd5a_qbgf1MQGfCcoDypEo-VVklI4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=pez9-CVGPXe9RSliuNj6IodAC-Sm9EFh1TdgJr3E-0rWAhVfKu0OcsOW8DRSaBvhtnskFGadVHLjzBXKE-vnG6tZiRlWzw6jZX2tdtJdgbkogbRs6IgaWPHeEtf0lz_uHglZaMb1dq7-SEtMfbYtEEenHv2UsDteB1MpJeyYwYIPISlSV5-S1O_dLc0Zyfyj_LM8Pki1CLOD-An2x4bJ2TFS6HnaWI0nOFUsqUO623MqmQLbKZGM2ZTnEwOA_GT-FEcXAgdL6Jcm4mp3ERkYelXREnmOv1n5k_zL55bXLJ7MwMTgPI1jybmg9atekvp-NBE7-uyN6m5Wa4F_O-gboAf0WCELqTe0AYUk2-BCEiuWTTCWTTmT-k8iqFLI8vYD6gWKaf26-L6X3oVe_3FUth2JV8jPWHSz9EoFdmn5AxQKmqSOh-IqGsKfCQjeb-f-Ru4cWd85TzlnqXirbxkJ0Yzx0MnMJifDB84zFtT8oppdaw_jyZYLI-MkBh7OvXyIJGrVRcFRNZSUHMKqs5Z_AyBDWuh7t2K60YxTH6McsAGYaq_aKeqZ8CPuZeoYCmLPMkMp1hNbr99THeLd88s-EXV1UbywEbMwrJnZn9mMB7C-BEs1OB3PCU7zyH_AOU9FuRvBa2vNQ23ecrZd5a_qbgf1MQGfCcoDypEo-VVklI4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=U7c6sO60Ncy0CIUNTTAqvcilpsIcbbLp7zbxmKgBNScFFvbqsCwn0ZpReCYrJMM-65ZVTrIOYajidIxMKDCRmg3RKqMvseOXRsMRJQu5u97Lzf3t5yTIAXG-7WWEExNbanI8zETTED2s6asDn1wEiyjufYwS13Nddn9KjP9fRLjKjJ_Gdvnak1plMDCW6fFn__7ofqwGAJc_uwGWhkO2Bwiho-fcYKRR5w_cnB42xMASY01sRZ9JBFNVIZQjIOwyRCf2duQQ9EQ7FAH3avLqNkhgqsvFK-s6puSoAIkbkmbd4sI_taHfahpIXtXkmJma-NskRNYvyYeX1QNnHnhMOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=U7c6sO60Ncy0CIUNTTAqvcilpsIcbbLp7zbxmKgBNScFFvbqsCwn0ZpReCYrJMM-65ZVTrIOYajidIxMKDCRmg3RKqMvseOXRsMRJQu5u97Lzf3t5yTIAXG-7WWEExNbanI8zETTED2s6asDn1wEiyjufYwS13Nddn9KjP9fRLjKjJ_Gdvnak1plMDCW6fFn__7ofqwGAJc_uwGWhkO2Bwiho-fcYKRR5w_cnB42xMASY01sRZ9JBFNVIZQjIOwyRCf2duQQ9EQ7FAH3avLqNkhgqsvFK-s6puSoAIkbkmbd4sI_taHfahpIXtXkmJma-NskRNYvyYeX1QNnHnhMOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=ASwDOkNpQZCmdQ1bGLGdurMO5zIgLMZqv5pMz5z9TX_LI9loqseNd4DIWuI0e9kF5IWvVyeZhZ41VEeWM4-ivA60aqTDmS2FZmf46zonVfDZMZ6k99vlk5Go2w_p0gTHmhGTDFws5rbL09VeUsfypce_E8hZJLV5h6iKv3MiBeyZJpWPFyYnnm4Q9HCGgSKCHwSoDU2xDaEL8XOZhWXZNt_RjfGlro71e_s3bjHwpSsdfThV7weVc9t-bToG7f1-iH7p-U-Z3bJrR_HKo6IInCcZmyo2yvn4Vi3Pn5wgEEcInGkIuoC61cyUqQKnYQDfMaZCYcQI_ZvWhcb0jU32yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=ASwDOkNpQZCmdQ1bGLGdurMO5zIgLMZqv5pMz5z9TX_LI9loqseNd4DIWuI0e9kF5IWvVyeZhZ41VEeWM4-ivA60aqTDmS2FZmf46zonVfDZMZ6k99vlk5Go2w_p0gTHmhGTDFws5rbL09VeUsfypce_E8hZJLV5h6iKv3MiBeyZJpWPFyYnnm4Q9HCGgSKCHwSoDU2xDaEL8XOZhWXZNt_RjfGlro71e_s3bjHwpSsdfThV7weVc9t-bToG7f1-iH7p-U-Z3bJrR_HKo6IInCcZmyo2yvn4Vi3Pn5wgEEcInGkIuoC61cyUqQKnYQDfMaZCYcQI_ZvWhcb0jU32yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gG7irNufltTvUe_Be_9pvAPmpOFx9c11N_YxEV4B0e1GmDCXUdDEhWpvUbKOnT-3JjjwW-l7QMyA_hT4s2vVDyYp0aaMTptFURiE4aMoUoyP7ijLottnZ84foOX0Fl1SYtj1NG1gOvf7q8pEfpmxfTGg-O5LiCPkIdPnG6SoL-okbEZUR1IWOjqPLglw-Z7XdTZHp2HGveGN8RWPFqGN_-R4778QvRvEB8vP3AlepBrt34yPRKOYopmsUDIaVijnAdBT25SaIQw61U6v4tZcYx0hKB13v0t4ty_ZGzjBwaTRllQoL-lQwx3adMEwTH641AI_QfaKurQ8O16dHFaubA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gn49J6G1m8plHN0_Geb0nC7EwVSAmmu6KLraa8J7RcyFL886O-xqnPOfzSHKRWQ8s4p4Ez5B4qrgBjor28MqSx7vgvGrLldRTYNGGdqteIJARmw6h6vyUXKUlNDa2QBUI0lZYT1Z0S9ts4m4G0XvRVIc7ZngyIUdmJhzCTBjrf1IChiL4J6R4WK33XrN297sJkFnthZ05MR1FZRU1_VzY01TZqT1E65rzI8Hvh43nTGsD1bR2KAthxdNdH75Dsrmf7zofj-utzFyQzz2vvm0ZNEOqNkY0I6gq-JLB5DtYQoncidX-tdUBuDSDGtr0sBWzCl0UwbO5wnS9cojEWXo9Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=ZHuQAQ8Ucd6HXAvuHLGOzNRlbtpABJGI_P0tgSMwwQQuAiziFsZ0Kwa_aTzr6Fu7NXtlo4PKz7pOUZqjhP6hIdx-jzibL0t_ny86mw80UkQsq9ejoHsHIATqHEtxwxFK85s48phjZ402krtqWpnpuWBkYcxv7psW15Ii9NFsbengYcA26bQefiiktjiEA9S9piOxYnj-JPpkpW5NTUH_-kyf0nAQQUEo3FQavRil61-kVy8m0CEd_sY5lDbecVW3nx2FOvnMWiA3IuuLmkl-cIRujc7pmy0dGzT2pv4NDc_7eVi3fCbmtbHerUE5IByes00bJ5e5oU7yXmyNhteqv5k_7oe7aUCl1hTwMKXrM06mM3Sp4fVfflEz5Bj79w4DEZyvcBrJn2WqrgOHK1tVbrewPzkuDyA1GIrmr5Vw-QDjxx7wtGTY2Q-Fugn0rEDu5hgX1m_T3q7tOFkO39cxjfrQksTpcVLjwETeneIid-Uzftbc91jOJa0KOMJKdh-zuVMTRBvp26BPbhmejj2EXf81cyBsZHDpYKyYsvROlF1wLYM--8RsqyCCr8YVcl525h5td4Re6y05I9lscmfa5uZt0GQT-1zNCPwGHpFaRZW5MIz9D8e0yqL0EbNi8Apd5NUKVALsr0F65nD7OiJqWwsw7dBbd9p3EHm1S0eynBU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=ZHuQAQ8Ucd6HXAvuHLGOzNRlbtpABJGI_P0tgSMwwQQuAiziFsZ0Kwa_aTzr6Fu7NXtlo4PKz7pOUZqjhP6hIdx-jzibL0t_ny86mw80UkQsq9ejoHsHIATqHEtxwxFK85s48phjZ402krtqWpnpuWBkYcxv7psW15Ii9NFsbengYcA26bQefiiktjiEA9S9piOxYnj-JPpkpW5NTUH_-kyf0nAQQUEo3FQavRil61-kVy8m0CEd_sY5lDbecVW3nx2FOvnMWiA3IuuLmkl-cIRujc7pmy0dGzT2pv4NDc_7eVi3fCbmtbHerUE5IByes00bJ5e5oU7yXmyNhteqv5k_7oe7aUCl1hTwMKXrM06mM3Sp4fVfflEz5Bj79w4DEZyvcBrJn2WqrgOHK1tVbrewPzkuDyA1GIrmr5Vw-QDjxx7wtGTY2Q-Fugn0rEDu5hgX1m_T3q7tOFkO39cxjfrQksTpcVLjwETeneIid-Uzftbc91jOJa0KOMJKdh-zuVMTRBvp26BPbhmejj2EXf81cyBsZHDpYKyYsvROlF1wLYM--8RsqyCCr8YVcl525h5td4Re6y05I9lscmfa5uZt0GQT-1zNCPwGHpFaRZW5MIz9D8e0yqL0EbNi8Apd5NUKVALsr0F65nD7OiJqWwsw7dBbd9p3EHm1S0eynBU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teeP-GAWQMSfOvQvPjCUJnsF_1fDnZNS4tgjshWNVlHQ7SWB-u4rSh7qIC6ms5_mm-F87Y3msFsjq0MKx7FGyrkPZeh8-yv9l1EgALn1lxvCVtzVM6YJPZ5QE9zIBR0FIbneA2FsVr7w5BRabQtdNm7y8qwRyiY2wdC6Dn7lFp7lczRsE1p-kIzfeEXpR6TxUUV4xsE6b8JwLFBr80DarYZ_UuNQbC8P0XhC0w_4PPZbx3BmXIuhUk6cQywZ6RWFeO2vbma8NGe8QSCewlajRIf1tn__5xBocnoLEZ8hBBjGkZ10ae73lQ7Wzl5ogIjZuUUVe3H8KAHC4Hd6dQtaig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lWr4OTkIQJ-Ha-VY-KdFQqH-6RtlWX0q6N3jaXXr9x1Y_H1MYoKqA1w6SU0EGSsHqryCF24qvx2n0K5AkEkRdWUP5MdF-dvOSjnO9FTC_1I634Wu0MaCUa9WI5h3j3ldU2-aqNE7oCexDhyGOdLe0HSh8i6IIxI0jmNIrLHAPkHenT7l2jnltMduqmh2I5U_Or_fdPYrZDh12gedp4vFKY4fXhZV3eaFQnjFwC79h6ooxcOG2L83km24hrocUq1Ptehc44rXLgn0x4dq-ZzEmi_iuJ_b1n_tixjaQhIjS_g_1hwom5tL34eVNWrAjbShn61wMRJo52MVf-jxxVReGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ucx8fcuSqmL5KcNfBdcPRd_DNaIjXGKKSK3vOzosn8JjcgCbRBy0-5j3Q9A7P8S4b5v5f-6ePE5TcBMOBUJIf1dNUJkOaQNqQrspQx4wGdSdZ_lKxyvhCWeMA7-xIvbYRI0yotm9KWsd5JnEsnTHXb1CWwwvLi_INywPvGgjn3JoQCWl4UC4SHX9tVMb-Mp8yXasg9QJXhm1voWpHyadHBf6K0tX9e1ZBrCdxUGEfUeXH_3AL2293uW_283OoGYzjb4UffDjka0-zM2W1ByPtURXYmjcNVAry8P9K5Q-6kr-Ol7SNkobOnKj-doBczypW2wvRd1_wd4gbTo1s6CNdg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZW0wk9SjEv_nKY3oxi9tns5SmshG3-Fobm6JHsPWozqDrJ_4t55sewtOyLf1wcLUUGye8kB6KbZtUFxDgY2HJ9G9Frud6tItndJ3sxT4Ozy4dLagux5uVZg5qasN5hTB5SJiF7o0XbpDudbedRsAKPEPV1-uObqQNqdrL997lJ07f47BYH1HTHREpLsqqr3Kc1wmrCZZovagD7FCvOvYzJGt02z6Uab5dSo9BsjHuCNlfK9DAISRepKo1PTkULP4CSCP4HmX_hmAHV2RVbMAORukJf5C7NZkAr8NsCUfYLGuVCYtwYOseojToliQJfK_rSDw18Wf94EF9cUd_xrOA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=C910dT0Zo8-ibigc__Ts9qLVgULWfpJuekauttLz-8JM9GC86CrhGpjuhf4hNdn6WyBa2T9GAOsE7t_oXh5SG5zsWaS_zS6ONqjo0Lo7ZdwQ6opQqo2Tr5eA6OkYDeZJ0doc43XKp-sdlYlNt2bseWEjmOSCh0f6lUbzS8BuXGEJHtZBeBJnVGslp9Zc99g_I2guCXpnVp_WgY5ZcQWL7Sp-9sSzBoW7d3WHV3xjoXYtycuiF93dOkHerrHieVaJFMAGwQXEnyAlt6O04ieUbMehjMcjGRm9k27pwCUrRYOUk3InoWpuangA57qoPjS5voAwrT076VmNDUzT490pBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=C910dT0Zo8-ibigc__Ts9qLVgULWfpJuekauttLz-8JM9GC86CrhGpjuhf4hNdn6WyBa2T9GAOsE7t_oXh5SG5zsWaS_zS6ONqjo0Lo7ZdwQ6opQqo2Tr5eA6OkYDeZJ0doc43XKp-sdlYlNt2bseWEjmOSCh0f6lUbzS8BuXGEJHtZBeBJnVGslp9Zc99g_I2guCXpnVp_WgY5ZcQWL7Sp-9sSzBoW7d3WHV3xjoXYtycuiF93dOkHerrHieVaJFMAGwQXEnyAlt6O04ieUbMehjMcjGRm9k27pwCUrRYOUk3InoWpuangA57qoPjS5voAwrT076VmNDUzT490pBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=kJ7ShGh9ZE_ZVfryo2MO86c-toFLOpFDzyfkMBlkN9PGYSWF2346GxCWKW9z4VJfza3OZnrmIJ6-oVtGc6GqUkRD9mVGAvqVtPN9---Eo8KVFP3xVGw1LFa48cH4f9HCxgaFKDpuInf2uZRLCP-CWr5lLZARDwoxprS-b1jHuxZ3c1DIfw6IgWZCMlWEw9ga0sQUSWK2XC_FDl_3wHplmV0PnAsHjr8FUM5l0z4nOvSEUAwaUGcGj5KZIochaey0Od5BTCo6u5i9k88zkFwcSZ9uDEbDuSeofbMVuByHosP1PCMqMuAzb3gZ3U53C6V2KyBiQhBYYj0ytdl6WYcYgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=kJ7ShGh9ZE_ZVfryo2MO86c-toFLOpFDzyfkMBlkN9PGYSWF2346GxCWKW9z4VJfza3OZnrmIJ6-oVtGc6GqUkRD9mVGAvqVtPN9---Eo8KVFP3xVGw1LFa48cH4f9HCxgaFKDpuInf2uZRLCP-CWr5lLZARDwoxprS-b1jHuxZ3c1DIfw6IgWZCMlWEw9ga0sQUSWK2XC_FDl_3wHplmV0PnAsHjr8FUM5l0z4nOvSEUAwaUGcGj5KZIochaey0Od5BTCo6u5i9k88zkFwcSZ9uDEbDuSeofbMVuByHosP1PCMqMuAzb3gZ3U53C6V2KyBiQhBYYj0ytdl6WYcYgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XM6M9UQW5VZZYCIsVmH1xidniWnGrXJphPMkRoyfwiUhRVx4gyadQpFMs7Fdj9PD7hxAwXKB10xs-hlzcSNGfEEeDErI7HiAK9Un525Oge5Jmmc3GbllBJvkVlXpqEkJvttHfrb8jde18Jb2GzVn45-JKDvkAPUFtOK9ua2SsaHMGcceKlrUEEe7Pgm9npnxe02krHN7111DNf9lzFFsrHqs60Qp60eAYfkAJBGPtbYDXA65k2n-5z40_m1jhzkn-VaF9f7V_eebYL_dnOkedxPpIrtmnCSCUYVV9aSAud3SHU25JtQpmYQj549O3xfxk9NkZNWJbhyWCgwNLOPwsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=rIG5ws53YInlHh6sWwO-heJsftVEeHXdzjIebmgPixZcwhg3aeMytN3WjAoNaZHUesKg-DPYU8mSIe5Gf7hg7vmJBs_XNUWsaUc1goifZTIg6j7GyrKZJ6mckyD5PgDt3U52kSQl0O4FO4APE-b44CQizIFqOxs4wBcy03zOK0GMcPICaqUUTIusQXlw9aXk02ujHGduOTpIl7dhDh6SenWBkJgRqSwRHn0rS49hXytnhrlfbacZz1Devic_JoqOl1qEC6catvhGPbocOPrjuZ9JB5ywfjIZv8FwEx58kT0yEn-5PA7lS3z2v1ftV8FjKWA72c1G_s0ssQX_2EfjfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=rIG5ws53YInlHh6sWwO-heJsftVEeHXdzjIebmgPixZcwhg3aeMytN3WjAoNaZHUesKg-DPYU8mSIe5Gf7hg7vmJBs_XNUWsaUc1goifZTIg6j7GyrKZJ6mckyD5PgDt3U52kSQl0O4FO4APE-b44CQizIFqOxs4wBcy03zOK0GMcPICaqUUTIusQXlw9aXk02ujHGduOTpIl7dhDh6SenWBkJgRqSwRHn0rS49hXytnhrlfbacZz1Devic_JoqOl1qEC6catvhGPbocOPrjuZ9JB5ywfjIZv8FwEx58kT0yEn-5PA7lS3z2v1ftV8FjKWA72c1G_s0ssQX_2EfjfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=HaIXrMcM_jvFoJebsOxWEbQHfRsT0zXX3jixrr0zXfOImqbE4qQfKSmZqfbvQHo_W2NAT_cEjEQGr_prYq1GYK54yeKK5mhsB1Mjw4SU8ykWBjA-Q8i-dFw9mmn233E1AHPqmIwNFi1_M0JmDrcYASTPNFbiyd1XI58hpy1SnGORaNch4lH8TIFBl3J1wTAcmyUV22cQgJ45S1PMXIDylJ-VR6vwMlLZvG43IRxllVXZR8FpoMU5l1GM2zLmAjV8OQbStQlyyahiARdVzD6mTQnErNvgpPQ-OdBNPc3M7_6eEBh1_Pa4B1oLpGyph4UrNbR38f20hRbloMTogg5hLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=HaIXrMcM_jvFoJebsOxWEbQHfRsT0zXX3jixrr0zXfOImqbE4qQfKSmZqfbvQHo_W2NAT_cEjEQGr_prYq1GYK54yeKK5mhsB1Mjw4SU8ykWBjA-Q8i-dFw9mmn233E1AHPqmIwNFi1_M0JmDrcYASTPNFbiyd1XI58hpy1SnGORaNch4lH8TIFBl3J1wTAcmyUV22cQgJ45S1PMXIDylJ-VR6vwMlLZvG43IRxllVXZR8FpoMU5l1GM2zLmAjV8OQbStQlyyahiARdVzD6mTQnErNvgpPQ-OdBNPc3M7_6eEBh1_Pa4B1oLpGyph4UrNbR38f20hRbloMTogg5hLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=QChkkhL3-G5hgpOFWonPl7h9znCoNLicwVleaZxBmrw64gVHZ10X0oi9FWR4GZfGQNoy7-0fg3ArmxVyMJ007d_8grwdAeZ4F_jANu-dP0PR0QLEZQ4P8nbldHEP7wE3zolZl0pklr4LJG5hDXnmgf-32bIe7c5T0cM5PaYhNp7FZyelq0flpl5ehC0HV80LCLa_WXxBF4lUB9Ysq6sc4WvYRusHLxf5OrUMyOXBwSFkMqxcJJ5HHXn86wmtLD53GdI03BC7lhr_l1ymiYn20jh30TkUuaM13pFyeWLSjUWlJfe36cRV06Te1lBq0MaPLS2MbtQcrpdOvutEwvW39A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=QChkkhL3-G5hgpOFWonPl7h9znCoNLicwVleaZxBmrw64gVHZ10X0oi9FWR4GZfGQNoy7-0fg3ArmxVyMJ007d_8grwdAeZ4F_jANu-dP0PR0QLEZQ4P8nbldHEP7wE3zolZl0pklr4LJG5hDXnmgf-32bIe7c5T0cM5PaYhNp7FZyelq0flpl5ehC0HV80LCLa_WXxBF4lUB9Ysq6sc4WvYRusHLxf5OrUMyOXBwSFkMqxcJJ5HHXn86wmtLD53GdI03BC7lhr_l1ymiYn20jh30TkUuaM13pFyeWLSjUWlJfe36cRV06Te1lBq0MaPLS2MbtQcrpdOvutEwvW39A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bIscMYp4Jxl8jIeHCUWHFoINwJLRkHlFfD9-pEf7-RBCAtrYp_WgtLRCzvUPf7H0cSBpoDdAdDDuwgiB5NjQHxKnMEpQjSo0LdGovZcJvX7zMLP7GxuSCVs0W0gcDyiI66ropstcJHOP5aQWCM4GF-2a-kkH5Y_oxzyLJu-QFr1E6CkiPmJMXA4eOqqD4l6IrRvatcFexRjSzOaTh0C4D2M3leKb6TH5GXlj9HgnvGu-BPk5X6jjJx541clRWwO99YWnhilqgPOZ3iPLOWU6hoqcl-W_hyE2s8DNSkKxZBzQv9kMTeeYZ5Qw9_CvecTn5fo1NVuESG9ZYQmB8-J2Hg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=KL4q_ktg6UxOXjv5--jqqSKwbfd0ytFe49pxNTCzFNtYvCgRDvu4C2CV853uqMSlE_7gVeXXlGmVRcbrE9FeIWIoTd50VbMYQf5kccNtdNQRiks77RCwRBbQB7rD1YfgFYWnFB040la-jmFqxhBK3AdYKkQDamBOTcZVwIvOig3z-8jpdJnM5370nakwvJxUMihJSwJvyJNSvT0VQN8I7IimrNNBCYJTGkP-QOpLfYqCw-bZigP3g7ET73-UVIHqY2T79uI1afYBr_UDTco4TZDh7nYhbEHfCTt1ZbH4TTcW8nGqT78hGr3be9alIY7dyv0mKPivTuN9UR-I3KzROA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=KL4q_ktg6UxOXjv5--jqqSKwbfd0ytFe49pxNTCzFNtYvCgRDvu4C2CV853uqMSlE_7gVeXXlGmVRcbrE9FeIWIoTd50VbMYQf5kccNtdNQRiks77RCwRBbQB7rD1YfgFYWnFB040la-jmFqxhBK3AdYKkQDamBOTcZVwIvOig3z-8jpdJnM5370nakwvJxUMihJSwJvyJNSvT0VQN8I7IimrNNBCYJTGkP-QOpLfYqCw-bZigP3g7ET73-UVIHqY2T79uI1afYBr_UDTco4TZDh7nYhbEHfCTt1ZbH4TTcW8nGqT78hGr3be9alIY7dyv0mKPivTuN9UR-I3KzROA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W9aHJLxhrxCi9i2QUxfX8xYawGkDqQUyOFNRYf2R8Q0EmGxWV6RSI8Kg1ZOkod6KkGMBhoSIdRtECDlnNmiBcaViN4b5H8fsz8CpY21iZqESTje3nha1tBgKcojqNkKSd0zqo8PZOsNnn5Z-1p5qyDAXCytGWpoqzLd2V70eoS7VPkt5w3pvZeTUzkwwJjC_ACcYYItfnAqXyXNQKWcla6rTesE9qCGmvq2_Bz98Hw0lMWOT76uve3DwkuPZT-Wzpi3Hot8xnc5b6olkULOg0CCuXL2N-tR6w7WU7ul9BKDNwsxFjp4ebNiTcbGDrKminYaiOq0rfmxa-IBjowv5lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MEY1yQRTm9mqSUGHyTOughy6q3WYoWZqStHAJK68MrmGJdpWtfLTtbMQj9VdR-5Sdv35HI0RYsbsyWe_Ch8VHgH2qBeYeKuIKO4SVD7iCS3Eljvn2aVBFgxyXmeqBbrnE9qtDTEh_JA-daxAQ70XJCaCiHzigYofaf-Y3IFy_kyMlTACPGqWR0tsL6daoDw4yzc3hi_KrUlslytuYPd3kYTBM_KNZyiISsvwbaD2ykYTJeKWDwksfr9MNaUvN4vaUtXGCIjSNSI14u3YcyaKzWg4eQT-eX_KWaYCWufxdyu5uNA1dPAAcpX9PIIM8ifg49vvjjZQynf7UI5kepb3cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=Bf9WhF623Oqj9zMLhEhsVb56j_DxMpOYzlEx4eFc75IGZsOg_KZJo4l9JXsFtTatornaP8UoaFeyHFRkHtnd6rDvuBS1Ytmv9BjeaJvasSKJ2aUhHfB1ccbu5YCR3EmbJ6pUPdvtlIuuofSOkBcok-Hw-MhfC1ylHptyyHCvqSKHv_nxCsF21kVklUp17cc_zwpWDKNokgzRasCHdPn2JqRD2wnBQ4zUBdMBlwlvoKPvmnW2hvwPHPZHh8mpECRqWolYzHZNfsvM01Sq_yFR9xd5aAaqOTrZn_MiEi3sQf7uqfmT8JRTQXow3d30r4VBhOgSrNYCrnhlb8NLLNS1Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=Bf9WhF623Oqj9zMLhEhsVb56j_DxMpOYzlEx4eFc75IGZsOg_KZJo4l9JXsFtTatornaP8UoaFeyHFRkHtnd6rDvuBS1Ytmv9BjeaJvasSKJ2aUhHfB1ccbu5YCR3EmbJ6pUPdvtlIuuofSOkBcok-Hw-MhfC1ylHptyyHCvqSKHv_nxCsF21kVklUp17cc_zwpWDKNokgzRasCHdPn2JqRD2wnBQ4zUBdMBlwlvoKPvmnW2hvwPHPZHh8mpECRqWolYzHZNfsvM01Sq_yFR9xd5aAaqOTrZn_MiEi3sQf7uqfmT8JRTQXow3d30r4VBhOgSrNYCrnhlb8NLLNS1Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Rd3gSQmV2vQAsJAVqOUnTIWtedJci_KUTTGBJCFcyoD6BVGKZp4PJh13-YYhuUw6emA1iSABD6_BgDvOEcmSZ0Ec2afECtHl-CJNRsSyg7i5TtZsVEC12Vj2yOIjtvf4ZhaZBEJjmh7cpWZqmsvJFdB7L1Jwn1tc5hO22aHZPwTjUMmy4kFRwGaLShzHXraexYGg-X7vCKubmgfXPYPsHdX9ZHGyKJWVCT40Q4JHlfG-kMdlf4DNhiEVar_DJoK62KkMrZfKXC0O_OlLWilLm7LyYu4l_yDYg652jRgP9bUV9YBUVsTeccRHCfh2Yu3boK3w_sEx3ZTyTDE8lQwLr0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Rd3gSQmV2vQAsJAVqOUnTIWtedJci_KUTTGBJCFcyoD6BVGKZp4PJh13-YYhuUw6emA1iSABD6_BgDvOEcmSZ0Ec2afECtHl-CJNRsSyg7i5TtZsVEC12Vj2yOIjtvf4ZhaZBEJjmh7cpWZqmsvJFdB7L1Jwn1tc5hO22aHZPwTjUMmy4kFRwGaLShzHXraexYGg-X7vCKubmgfXPYPsHdX9ZHGyKJWVCT40Q4JHlfG-kMdlf4DNhiEVar_DJoK62KkMrZfKXC0O_OlLWilLm7LyYu4l_yDYg652jRgP9bUV9YBUVsTeccRHCfh2Yu3boK3w_sEx3ZTyTDE8lQwLr0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=UuFtyoHSciyltfwQvZwjq2IDxDUwMPCkYv0ApCfU4hDduF-55NNMLi43rN68rlR2GyKvFoNY3tNHlIsd8Xl1xsfC3sXlmNZI7F1PbhnkuOedIKpBRLrQkeSzoyrxASXKLcUgfIrjNnR1RKZhvtzJ_GMzzZehxo6Gh3LSxGexH_9U8QaKsb7XTu1tTu6OWLMd6UvEf5MRMaRfM-Mc1PJE5JSX4M7MWOAMQ6_PdzXJEjxVdEIUymMsXAs-JkaAujoLp-FLI59v7eovrou8Yf5Gbr6_i3uD563_GPPvpvMOys523gkBdg1ICoeMhGkzQ2i0osww-QsCuwpjXVjXlJUQvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=UuFtyoHSciyltfwQvZwjq2IDxDUwMPCkYv0ApCfU4hDduF-55NNMLi43rN68rlR2GyKvFoNY3tNHlIsd8Xl1xsfC3sXlmNZI7F1PbhnkuOedIKpBRLrQkeSzoyrxASXKLcUgfIrjNnR1RKZhvtzJ_GMzzZehxo6Gh3LSxGexH_9U8QaKsb7XTu1tTu6OWLMd6UvEf5MRMaRfM-Mc1PJE5JSX4M7MWOAMQ6_PdzXJEjxVdEIUymMsXAs-JkaAujoLp-FLI59v7eovrou8Yf5Gbr6_i3uD563_GPPvpvMOys523gkBdg1ICoeMhGkzQ2i0osww-QsCuwpjXVjXlJUQvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ci8mf1j2JXQ4N10o9ZoUeTjvNhUKXzCN_5FXHJwygOlKiAkKnX4fx88HC526a8FbORpOgWJRRsf019atJtyV-O5icQiB4epK2WveoTXTg_X7INHP0cFqUz1zlDvzyXsJuq_VsSwCCb9G-vTIEyOy8SqstBncQS-mVwkT_lImCn6bFllkYPlsSoSHwU2tFcJ2Eyq0wmP7ZWRtkqXGNyan5TBq53oEkoWWjW_KU_sJI0vuYHGvXDTUYDVWcldMCJQIaG116Mz-360UXFhk9ZVFcBZP8wm_wp-x8vYDlsBRH0WLTIBQr8kLPFzUvk_cq5P76LEPbVidfi8qkU3ZFC2mMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=jFinXZjkblxqWG0OJoDkYZQlzMb9oBreDq4XtBwcm7CB8Mz9AYPVz9ouNBaMTeOrVc9lYXrHz1g2HPDLno10g2o8qeBY6qSISg0FMt5_l-kREaOzO0JjNuSLsE4zS24ujTDfNPjiwOWKinQ7jjE4j1UAzwH0CCRUW86HsVwiUB_BO7p_b5d2lLH8vf_4iLjPCzdGogwfMKmZnkS5NVj4aI4PokJitP028BoKOzKWzvP7ipgpcHz3vxRHfrKAKVgUm-x8wqCJEQFW7t88t2ylD4CJyeH4TiSVE0Foe5XdXg-UDYTFc7QJ6cfKaaaO3HVC0B22JuyVDUvFEa0bUFKnQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=jFinXZjkblxqWG0OJoDkYZQlzMb9oBreDq4XtBwcm7CB8Mz9AYPVz9ouNBaMTeOrVc9lYXrHz1g2HPDLno10g2o8qeBY6qSISg0FMt5_l-kREaOzO0JjNuSLsE4zS24ujTDfNPjiwOWKinQ7jjE4j1UAzwH0CCRUW86HsVwiUB_BO7p_b5d2lLH8vf_4iLjPCzdGogwfMKmZnkS5NVj4aI4PokJitP028BoKOzKWzvP7ipgpcHz3vxRHfrKAKVgUm-x8wqCJEQFW7t88t2ylD4CJyeH4TiSVE0Foe5XdXg-UDYTFc7QJ6cfKaaaO3HVC0B22JuyVDUvFEa0bUFKnQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=u7NPEIpVWrWwDiROM5htduz1l6DzrV9du055NRJLprKF5AuBKfhxBKWXGBfnjQZY2n4fWyMLAB6WB1W3cWhgfG13pWATwb5mPuAace3kQbYG2cgpnew6rsDN0ov7QkqBsc8QsH7MnVRBlJQuzR7DvdGGUQVUImRTWQNoQlRJAR7SDgZhT0eyUJELdJqTqGAXSWU_XseCR-X1Pt6GOTZu4p36mM6oJmt-n5EMh8sRhUo_qtM-lifyhMjzy-ZwwXU9zU-qUQwd0YOzMPGZDYnBqESKRoMKlMk5WO2_WpQT_X6K3aNCNE0DyXIb_qXIsEuKUFK7_XxUP2KOyJ-SnbK3FA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=u7NPEIpVWrWwDiROM5htduz1l6DzrV9du055NRJLprKF5AuBKfhxBKWXGBfnjQZY2n4fWyMLAB6WB1W3cWhgfG13pWATwb5mPuAace3kQbYG2cgpnew6rsDN0ov7QkqBsc8QsH7MnVRBlJQuzR7DvdGGUQVUImRTWQNoQlRJAR7SDgZhT0eyUJELdJqTqGAXSWU_XseCR-X1Pt6GOTZu4p36mM6oJmt-n5EMh8sRhUo_qtM-lifyhMjzy-ZwwXU9zU-qUQwd0YOzMPGZDYnBqESKRoMKlMk5WO2_WpQT_X6K3aNCNE0DyXIb_qXIsEuKUFK7_XxUP2KOyJ-SnbK3FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Q1B1HURWwN0ilZ8Cd3knIeqKBaam5nTDzZPCiJQdSvkO-68reE_ABPj5Waqx2cDH368EZnKWJiD8DUQw01btCTmuC6wxS7IFRP8he0mKsps41gMyzQ4GDXpIfr4QrzgpcsWOu-AM1XFY-Wgpz3C8NRDhxdZT5t3ijsvSYH-HHJFDmTP9epJ1_2H8py34uzBAyCCWGNVZon6cEHkjrq5mgDW9EAbiH6qyQoaFwYckxPmvu2wZfnLb0FukVeDrySMkDf-DJ6Qu7hGjxPDnbV7pZABgNNRm4K24uiIhLmoh7kZKTXLa-H_LWIIM_Sg7gK4fvbK2QfOGRjcree_99gweKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=Q1B1HURWwN0ilZ8Cd3knIeqKBaam5nTDzZPCiJQdSvkO-68reE_ABPj5Waqx2cDH368EZnKWJiD8DUQw01btCTmuC6wxS7IFRP8he0mKsps41gMyzQ4GDXpIfr4QrzgpcsWOu-AM1XFY-Wgpz3C8NRDhxdZT5t3ijsvSYH-HHJFDmTP9epJ1_2H8py34uzBAyCCWGNVZon6cEHkjrq5mgDW9EAbiH6qyQoaFwYckxPmvu2wZfnLb0FukVeDrySMkDf-DJ6Qu7hGjxPDnbV7pZABgNNRm4K24uiIhLmoh7kZKTXLa-H_LWIIM_Sg7gK4fvbK2QfOGRjcree_99gweKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=asuOveAokfXEQXSyLeJFbIa6WKuOCalUF0EKQ2WLzCGNKDv5BO21HDTma44rKSUKdhCQIxcI7b-fQboKvsR9vnmC5-F0z5yHqXmLxa8Bm5bPlFOL29OsmfWqCvGG6moM6fqGV551zK0RD9K2GW5XtowRJRCjvfh6TxSX2ch2IgUEUuMiFQ7927oVemGzz8M1nAI1OnY70mkOH36Gs0WqnRfzrGdK-ITIW2sBGUnjUpELd9X64jU8N9sjd9nrtyjqB72b6M22xaK6QA7mR5AWe3ErBnp8BZ0YXh89uoQsfwOGhhjCI_4Xi8ZnmC-KhSWLw_1O5rlkDNIOFcEl4NwvqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=asuOveAokfXEQXSyLeJFbIa6WKuOCalUF0EKQ2WLzCGNKDv5BO21HDTma44rKSUKdhCQIxcI7b-fQboKvsR9vnmC5-F0z5yHqXmLxa8Bm5bPlFOL29OsmfWqCvGG6moM6fqGV551zK0RD9K2GW5XtowRJRCjvfh6TxSX2ch2IgUEUuMiFQ7927oVemGzz8M1nAI1OnY70mkOH36Gs0WqnRfzrGdK-ITIW2sBGUnjUpELd9X64jU8N9sjd9nrtyjqB72b6M22xaK6QA7mR5AWe3ErBnp8BZ0YXh89uoQsfwOGhhjCI_4Xi8ZnmC-KhSWLw_1O5rlkDNIOFcEl4NwvqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FmI_FxgW1jdRILyvD2X-H83pdDqQVjqZ02R_si8xIBmi4oP_1OfOQMAEkE29ip6l9QhqhIzEhF6NZuitRwetPx7O8F3kk99FuzOPkdM5G6jv4_He_A8HS14RMfZCu3Ohv3tpHaEi1YnhuJOQeV_N47mzHBT3rZhtIJIkvA1AndvfWG0cs_YQIdMs4s6L9Zay-i9S8LH0oc-2U77kNlFtjhpD3u4U1gRfieLgRUjSUcB7yZc1PG-jWOhi70-gZyV9XRB_9WLhA60LngT9wHcZnaN7IfhuGKKiGJJrGfHJS5n27PvtGeRUUGA8YlZd4TjV9gKlA2Lelxi0skD8vbKU3w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=K6lsTfbp6n6G4v5aFbPzdNY6sUTGe77OnFeUJ4X8FuG7NksryCRw46GMoFjfBvWYBnAUtDjpwDGP6nHDrQnt7wlFmg3Dsfy0wsCOP826LEjxFquL08CoU-AgITgmtRsD0mDKzLcML3eAEtfX0AJ6hSxq4qjNHfg8m7Ii6FQ3CRPmEeFLjgUNcQx-RxELmYBVD5rsNe2cM8IBKi6xbG7Jb7iw8YSupkPok9LkOqOyuVieazdmkg0i_59BLJ9mbDmH0fvDFuhSi62GaUf6tuJiq1CcyAQhV1Z9obOn9WrcNGAwt1muzEHER2rb3NdEVqMrZ4qj2uJ6DDIaUyBb2RPO3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=K6lsTfbp6n6G4v5aFbPzdNY6sUTGe77OnFeUJ4X8FuG7NksryCRw46GMoFjfBvWYBnAUtDjpwDGP6nHDrQnt7wlFmg3Dsfy0wsCOP826LEjxFquL08CoU-AgITgmtRsD0mDKzLcML3eAEtfX0AJ6hSxq4qjNHfg8m7Ii6FQ3CRPmEeFLjgUNcQx-RxELmYBVD5rsNe2cM8IBKi6xbG7Jb7iw8YSupkPok9LkOqOyuVieazdmkg0i_59BLJ9mbDmH0fvDFuhSi62GaUf6tuJiq1CcyAQhV1Z9obOn9WrcNGAwt1muzEHER2rb3NdEVqMrZ4qj2uJ6DDIaUyBb2RPO3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iT4wCpnGAGvfBcNHzR51Z6ccAOd7aD93HjdPuWeZv12AlJYPbNSMTPmyqizFng-hB3fggjbg-lNMQ5yp9TLL3OIh03plObmq_a3UXfR6sYl9eCYfmQdRFXjwdC1PBIbiCSlwI87HLpqrD-LOwXW2bbKGUNsoS2e-eKEI4Xz9rtTR7bMB26ngTGuEbC7NldxAEwy__D0WFglZ0sZgBAJqsdHNy-tsRs80iVvjbJ_rdaJfYf3pOuCidnO1z8GZgsMSvEOWD-iaN-f4yEpU7ZwKh3vPuX8dRzYKdR0spjDVu7zGeRpt4LU4NFnR8xokV7EZxaKkIOLIoc4rGy1030B_Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=iT4wCpnGAGvfBcNHzR51Z6ccAOd7aD93HjdPuWeZv12AlJYPbNSMTPmyqizFng-hB3fggjbg-lNMQ5yp9TLL3OIh03plObmq_a3UXfR6sYl9eCYfmQdRFXjwdC1PBIbiCSlwI87HLpqrD-LOwXW2bbKGUNsoS2e-eKEI4Xz9rtTR7bMB26ngTGuEbC7NldxAEwy__D0WFglZ0sZgBAJqsdHNy-tsRs80iVvjbJ_rdaJfYf3pOuCidnO1z8GZgsMSvEOWD-iaN-f4yEpU7ZwKh3vPuX8dRzYKdR0spjDVu7zGeRpt4LU4NFnR8xokV7EZxaKkIOLIoc4rGy1030B_Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XQbhTzw3lPY1xYgP1TUfR99E4dGIyPbsF9FGRwNCB58OglZBoFuLD4ZDgwjeGAEM0qWS9B9gM73tBRDz3wvQdVb34-lflgVkbHMGhYGbilL7cGA554SHTBg6uxMekrErLm7P8v8rB6RTKXivXhEBcVw9YCqWlKGat9EsTKcnkPBK0rGIsHs_mmeTyinXgzyX93yhZA7Yytht_9nf51cCo2yJu1dELlxRFHuKnOxYFSTfLV0FPBgg2qNGHktmQ9d0bAnUpAAS1fK3ijShxMlxert7YzyLZq5k4nN3716IZMBEaRxYQDRUQRAQF-utVi9xZmi2ng53l56sNywyNbwJqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=YjIjYHx-EsKIT_dWbhGQOMVSV4-MD49piX0f2VMNqufH9YFRLOjSYeFNGu5fMZxSwoQ2uEuJQvRSBJs7r2gtkdl7S4HJljFDcnEHb39lriyztMHzEv-7gsPff0e2IjRa5gHJ1dOHCjxqHhUaZTzkbmWDBEA5ueYMo9lpiWSh-_luVIIfpVB3RbrQutX-Ol-Sf_rF4jzCjCDa2SAMsMkY2uQm0HY5toLryj_g8mR5iEX7uwxPMoJPxTuzw9yL8dNmK6r3seDEwah8EqnCwz-J9jHXHtqTRqh1xzpKHrsU2IOrqKqb6RMitHhHg0M70Vp2ycwoVh7KvmKECDj23307vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=YjIjYHx-EsKIT_dWbhGQOMVSV4-MD49piX0f2VMNqufH9YFRLOjSYeFNGu5fMZxSwoQ2uEuJQvRSBJs7r2gtkdl7S4HJljFDcnEHb39lriyztMHzEv-7gsPff0e2IjRa5gHJ1dOHCjxqHhUaZTzkbmWDBEA5ueYMo9lpiWSh-_luVIIfpVB3RbrQutX-Ol-Sf_rF4jzCjCDa2SAMsMkY2uQm0HY5toLryj_g8mR5iEX7uwxPMoJPxTuzw9yL8dNmK6r3seDEwah8EqnCwz-J9jHXHtqTRqh1xzpKHrsU2IOrqKqb6RMitHhHg0M70Vp2ycwoVh7KvmKECDj23307vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=qY7gUwfgWO-_xX6lj6rzOf8VapOnwipMFADCvSpvVOcTg3YII6lbdIPEyp_HKeIuYny3r3X9bBXwPSS0tQ_5JmjzR11i6d-B9iewH04gq8ESxSQgFzO85NO5QXBcwxVnOv43BgoIs8lGVoyW1nvJLypbDC3YvzIJXpxbHboxAa4l5j4EZckKSuWoP-QP6GuQBv80QWXzDNL33ti7jHbkESdn0phKW6wukiIMTrZgD9JpD69kWsVUFC9JPe5R21K9jJBmabBGfVxIWUVpjim1TEZZlgEO2vUPuEJzh90LEmn1EZFm7mgISO7EJW9YC9f--JYeMv2ZzluaqGAQXvcwNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=qY7gUwfgWO-_xX6lj6rzOf8VapOnwipMFADCvSpvVOcTg3YII6lbdIPEyp_HKeIuYny3r3X9bBXwPSS0tQ_5JmjzR11i6d-B9iewH04gq8ESxSQgFzO85NO5QXBcwxVnOv43BgoIs8lGVoyW1nvJLypbDC3YvzIJXpxbHboxAa4l5j4EZckKSuWoP-QP6GuQBv80QWXzDNL33ti7jHbkESdn0phKW6wukiIMTrZgD9JpD69kWsVUFC9JPe5R21K9jJBmabBGfVxIWUVpjim1TEZZlgEO2vUPuEJzh90LEmn1EZFm7mgISO7EJW9YC9f--JYeMv2ZzluaqGAQXvcwNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=VpsrJ-K1lbqWCd5pZsmlbC80dGnmb9NX5HhIqCJB-93BR9XrW3vJBjlzuDVqsyTxWIrd2abhu7hFfPqICsYwvkDj1n7NJMWmz56yAR-hQ2ym92OTHEnv29yWQBkody21AfZc4me9Zq5bW7q9SFmkUPjFx7gx3rB01eq_khFhLQm6txqrBeVp4Z-qyGTOurgPXDkbl0KOoiS04mmK37I7ADmN6pUroLaYnhOUoCgb6bXzRO9MC3vTMCWZsMtU0xxSw3YlkvwYtlaccHychYEEKhN9gqag5aQDG9G4NuFYeuEkO8Kr7Zw6IdEqoP0uh8XUsw_5-orIhpp1mGyWa3nijDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=VpsrJ-K1lbqWCd5pZsmlbC80dGnmb9NX5HhIqCJB-93BR9XrW3vJBjlzuDVqsyTxWIrd2abhu7hFfPqICsYwvkDj1n7NJMWmz56yAR-hQ2ym92OTHEnv29yWQBkody21AfZc4me9Zq5bW7q9SFmkUPjFx7gx3rB01eq_khFhLQm6txqrBeVp4Z-qyGTOurgPXDkbl0KOoiS04mmK37I7ADmN6pUroLaYnhOUoCgb6bXzRO9MC3vTMCWZsMtU0xxSw3YlkvwYtlaccHychYEEKhN9gqag5aQDG9G4NuFYeuEkO8Kr7Zw6IdEqoP0uh8XUsw_5-orIhpp1mGyWa3nijDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K7NmDhSNRtkKQIK_Pys1-U1A-09P9EXa2Vzv2L7VxcGoaWadYCP-oX4ERi2iYRUPArua60dnpH1KG1M7WQ9Imq5q7ffbuQRL4za-l4evB9XLPrZEFt_-j8IrOxDAVKCpe6yTuqLAnYLBmPnm5ZO4I_SljwJE-MiZUT5Jzh1e32BMStF6FOoWh1Lseit6aas2sk4Ia3jROhdfDO41TV3mw2AY77qrY6Sf3om8KDRL11WZ0FSoO8j146xGgw5O4419h1VXswyCG81YyRe18oAjc4W2f_F06SKYkutWbUWBN3q4FY5ffAYqbQiLRQ1G9AHPt0o86uiyTsECu27pyuz0Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TFoqAflWjiwFwm2n2kqA2Tnas_TeaUFI3k6up97m-0VvMgtcbV45Xw8FjSlH6Eifw6B9hozittw3REvYIoQaRWjul0ccjrFs8HltbyLMs5pIN0tX-RswUNo3emGrP1wr_QJI0BMAK5AB2wihxvvE4MPGbtCi1KLJFjj6jKYE8qbeEmziV_FtmfIoMLN0wqG3A6OzdYgQ9TCnGhLrX5rRzQkNnjQcFpSVBvQptaW7RMdxEV7b_s55XhBKkpYnCLwO7tER4TVBoBXBjz8zsIyrwBm4bQPQ6jWXse_0vrJ8fRN90-lMgF2eevpaNHkW3DBKJe6FZ2uXKC9dKarMGjTKLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LXg847Z-8OR-wHO8PUVHzIZN4kzgm0Ao1YIJrex05UckrFprqbbP-2Rb4La1ADGs5Rueq_Kez8I06MHh-NQ0YH3krtED7s27sfVYQWBnRJPEUq94Yj6xRphjkdAoaQjd8H9qRaNMgqEvxBWIk7sWDrbTLTc6Pm9h3NxR_IFbzW5qJFcKqh9x8iOUYhWjpVu5_RC4MJtwP6JNTCUvju22lwXqFZa4JJgC9pkEqU4SrfB4ks6BqZOpt-cHqSvn8FPBxEWi_89uCG8-6l3BwxSgLWF_ygpBb5EFr3IeSxDXqDR0UuOmEdXgJ0lKuYuSj9H8oQkGdITq1wCMX1wC3o9Q-g.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=cRQ-i3CrXZEcf7otbxPODbQhWVb0sRh_JGcT9Sf-7xv9k6WX7YYNdu9J48SHjVKvvP4LnVaeFTrkbVew30wj9D5NCbvtn_3dkq7ElpLnAjLasKZMbrEksnlcXem499dF3xTw0DRyY9bXB1ucwxGdMTAsiadsLzN_RbzIfZuNzBB57AB-aoodhyfGXfILbNhAZUccVtranHSjpubTOLycuOaRwYmgsUyL7PIYZKLylnroBa3hkBfI-uFSHCBiYpOqRBmIO9eqO1AhRBs1PSoHA8z__GNsiV7VqW3Gqy9_l7GmY9XseTgsCKQNu2hQ7WgEALA1Enjv2OFikRjhQz3reg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=cRQ-i3CrXZEcf7otbxPODbQhWVb0sRh_JGcT9Sf-7xv9k6WX7YYNdu9J48SHjVKvvP4LnVaeFTrkbVew30wj9D5NCbvtn_3dkq7ElpLnAjLasKZMbrEksnlcXem499dF3xTw0DRyY9bXB1ucwxGdMTAsiadsLzN_RbzIfZuNzBB57AB-aoodhyfGXfILbNhAZUccVtranHSjpubTOLycuOaRwYmgsUyL7PIYZKLylnroBa3hkBfI-uFSHCBiYpOqRBmIO9eqO1AhRBs1PSoHA8z__GNsiV7VqW3Gqy9_l7GmY9XseTgsCKQNu2hQ7WgEALA1Enjv2OFikRjhQz3reg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaRo3zJpdR3nuig4mqghftmQRL_D5yTQa37hRzKW0IjO0FjOYk1wGK31TFiVryeBYNYH4H2LVcBJkz0G_5rGdTOLEyb1CXKgn8lZLVHulBjmoWWe9OOTIbiRN_NTkbmL0R8w8BjzQbmk9YTeVn8beu73z14mr_pTtCNFGvIWCFVRpb5s_IIyecA4ldZbpFrtPSztq4qwYciACnNDSLZtSeTB_XUBb2WYrW2VqbfvM8binCN1warCviiKnaJbXgzalApwp-2TQP-zsYItX5KH31QzIpBrDkd0Bel2WiYnZdVYjQWOwtYCrYs_lN0W13ZrxYDMnIw_RpRDCDLsIPCUI5cM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaRo3zJpdR3nuig4mqghftmQRL_D5yTQa37hRzKW0IjO0FjOYk1wGK31TFiVryeBYNYH4H2LVcBJkz0G_5rGdTOLEyb1CXKgn8lZLVHulBjmoWWe9OOTIbiRN_NTkbmL0R8w8BjzQbmk9YTeVn8beu73z14mr_pTtCNFGvIWCFVRpb5s_IIyecA4ldZbpFrtPSztq4qwYciACnNDSLZtSeTB_XUBb2WYrW2VqbfvM8binCN1warCviiKnaJbXgzalApwp-2TQP-zsYItX5KH31QzIpBrDkd0Bel2WiYnZdVYjQWOwtYCrYs_lN0W13ZrxYDMnIw_RpRDCDLsIPCUI5cM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=ZP8SNGMgbxvWF-kAizJCNA_Koa7ZrEwwTAHIQSSf_8-HEkY-rRpPm6RZtUBWtSPPAWe-u1pZe_UCx5TFk866DBgIreUJfN4cbnHY7xtRz4z7cBHJps5FEs4jLjqYuEgj494c1DnGA3apkkutVMYFbonAgSDJDB-3yvIgneJrC83-ooR_UygMZCp4ktFrrzBOkAkCCY3pZivLXLH2N5RZ40nCsoZYK9jG-UAdn8WLiY9SoJp7py356M3nIvYuslyMouL0ECA1UZR-pWsUOkObC1wAYQr3lqpwJ7RARqRacVRHcabzEisF1RDjBO8cPOBVytXTCBlsihhcT0EwGdrjNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=ZP8SNGMgbxvWF-kAizJCNA_Koa7ZrEwwTAHIQSSf_8-HEkY-rRpPm6RZtUBWtSPPAWe-u1pZe_UCx5TFk866DBgIreUJfN4cbnHY7xtRz4z7cBHJps5FEs4jLjqYuEgj494c1DnGA3apkkutVMYFbonAgSDJDB-3yvIgneJrC83-ooR_UygMZCp4ktFrrzBOkAkCCY3pZivLXLH2N5RZ40nCsoZYK9jG-UAdn8WLiY9SoJp7py356M3nIvYuslyMouL0ECA1UZR-pWsUOkObC1wAYQr3lqpwJ7RARqRacVRHcabzEisF1RDjBO8cPOBVytXTCBlsihhcT0EwGdrjNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzMmY5rS91_4cvf0rIwH0etoilO_vGxbhN7RJcn1XE8Xe631_NDlvNh21BVqgzM9eP8D2auuq4b7t5nZtD4YgtQ_B9LShmacPePJPzd5kRgQkZOw6-t_AvlwsHTWumOZO-SgDwjSJf_sHyGYxmgldualMM6FcW2e9omWSph437pPBgXXF5xxmhlOQuX88mnDPz1r2NFmO-0S4tXXC7O9RG07jNpsqj50xUu64bD21o5p00AY6bcOZo4oeB4nDzlVItOTJHtDr2dxEIPNrsqkaVIxZe16MHU44e8uZpXaBPNW8E7SW4Mtm5kzWF3wibMsPs3PoJliU0JaqytSfqCHBg.jpg" alt="photo" loading="lazy"/></div>
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
