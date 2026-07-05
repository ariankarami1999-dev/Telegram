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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 20:27:24</div>
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
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/farahmand_alipour/5873" target="_blank">📅 19:47 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5872">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hX8TmlUukgx1CEMxrplBrST7mcORmueW5TPxmvJyYIx1gXuGnjch6i_jSD6dxQA9wNntu2S2uOLXXgZnMEc_5MsPr2YVuuR5OPlbKMSGK7xmig-nu01nyG8d6GkeyzUxn4tckbpN7A-DKWeZjdRctdIIw0vkX9V69l6raE4_Oinyql337INXK4g2riy7f-GFsi6GF3lhGhIcrg4xvRS6XWe1WuRul9AhWMl13Wrin5WVHXwbzwSxrMa9nxYPEhZaenXITHHcr7OmRGUHDdKQ7THRh37vPrCn9oMKyyrGIcOhk-lU7twZS7Bx-MskFFy87mKoeN8ggtc9CNGde889kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2073797265995526507?s=46</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/farahmand_alipour/5872" target="_blank">📅 19:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYJRFQvhISI1GvZf9xKq5SrjG7wMbgQR5njcALOEFcufvNAZyMgPf7bQX-5DPVJc5fPWMh-MqzAr2kY3Wjo1_wkwlHvXjoYJ0NfvGIUVxob2HT4E9pSCPafP5YZse0stTFhK0F8cu6bD4wLIBWgt_BUTLTNqNebTxB_0rOFlZYLCOC4jXL2FiaCKM6gGqUYnWdXd_9ihWpv3XgcjKwC3blpO2B-Ra-oNkbGLiMA8jl5xhnSY_h5ysVM4ufC8OPQvfa2o6GiNnpEDPWDBrx72cbeO4Pu7c16DKZY_rWRMwyQfLP2yGOoXcFcWjpFPGfhqYySc115PoPUYiYmfAvDoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU5FQmIvF1wom64UWca7ZKlfD3k7B-pAmTGzBM2FqD-QgEoBo5ERh0H97GkSRKsypX7w9_F0sUnhuzOMsK8DJk4ZwAr5FBm1qFtX03BsFGNOXC4UDRhxQPtBVbHE11Dt3Ky48awdGBbg6YEZTKjdEhbWbdVTkbRf7uoJQtIdv8W7fwwsMjyYznlf7iCsKBSK0uS-niMfX5184niHj86-1D46Oxp6IZVVOv5K5weK9gpt8lY9qzfanSg_FWebNrAFEo7M1AdMV7hbnv03J6gAUxu7Y9i_G5fBMEjy_r3KgFYLA70LN2oAhj1i7wxJ8t7hfjHRo2guYUK1T1YzJQmkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8gAsu6fGs5-d5yf7gqjE-ZmERtkqrxo99Ku3g8kO3dAOuQZYTD5C8oUpcXsPNVOr5BnP_PZ43bvgMAccB-eEKy0Ji_Nkc-ok31Xft0bidw0xXVAM-Wd53kh6exfkS8pHJfkq2NTwAFoXR-K9AqDIUuYZSvCVbSlAoFl46NvPYATA8bS83h3EpnwPILS1cBDvILz6zmyLu_4YS8UqH6L__wlMmB8jv7tMv6_8pVECymuWI3x_PBknURATSdTgzEULRaI3LVBI8N32Cp67UEDmthT3aSghWzF_SDiYqUZHC49j5sqciC7KjgM-q_jTo8XXWZDl1gm1U1rVi741mHLsw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2qbZP2GuD1nBirtkKoaBH3LzMp2gryLzXji8KK3sM6DsBzJ4VS4u_AgR2-xUtoa5ZzbgePtOlk7rbWbnRJk8dmpbWCo-D_3TpXnRvtWzAejsb2gaHNoMe0jwlr3Kg0O1fP1mHA0uK33irxODxj6DqnyiNyd4mhYjSIpofQSJykzRy1VnihnTUdDkAqp8Gwy4tqFn41tiNZMgy9tCKUXGcYAVdk0hgS2Me2oeqHeiAgo0twz7DcnTopruYtw3N5SVLKU_pTxYCPAeAlLH2VBb1OW82Vx9YRzkaV0p6j1U8OevfiPfAKmfYpCkeGFxECty8OVjwUfClrUZS3X0bbSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=rC7o-v6eLufEOv_yLC9W5Y82rYgEfd8yUuPNRmLcKdjMFhMIpYORKQxAqy-JJWWDpegmVl8jRUXBL_wK21G3t1hHLYRuE5jO33n-1mMJo6gV35BlrPOgYrNkyG_m89KR3EQBLCWjhkbHC2FL_IWJ-rM0UrQxZ1UMr0jsfK05EbzKP7_a_5dR_MPV0RExOnl6GPGB0OotUIJmMobk6c1gfaxfG3Z65ZTgFvx76qMlMLAAqsskOnoPA2UeGWJXcszmEHPkCAV6YzkbOCSQWcjm4PwCFYHJTZGddKLxk3me8xPR-Fv58d4i-2MT1xuke0YYyzs1fSc9PWI4ksEm1P2GPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=rC7o-v6eLufEOv_yLC9W5Y82rYgEfd8yUuPNRmLcKdjMFhMIpYORKQxAqy-JJWWDpegmVl8jRUXBL_wK21G3t1hHLYRuE5jO33n-1mMJo6gV35BlrPOgYrNkyG_m89KR3EQBLCWjhkbHC2FL_IWJ-rM0UrQxZ1UMr0jsfK05EbzKP7_a_5dR_MPV0RExOnl6GPGB0OotUIJmMobk6c1gfaxfG3Z65ZTgFvx76qMlMLAAqsskOnoPA2UeGWJXcszmEHPkCAV6YzkbOCSQWcjm4PwCFYHJTZGddKLxk3me8xPR-Fv58d4i-2MT1xuke0YYyzs1fSc9PWI4ksEm1P2GPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=towzXgF0NMieEs_IjLfsiw5oFRce3_j_0tiyDrIsqG5ITC6gckBDe0O6K0vSqbUlvjxIjnJzS-hqb6V_dqv6OjVutvyr3QTx9AG-AaHTrM-LgIiw7fIKtccE-Xn_ozVI00F9WrrZFUgskxdSx4ewTAjcLg7G1EngkJ3wG4OuPAGUrXzT4zXxYOYwMqwF3Rd5QXyPLOqgaDT4NzDz1-KAH5APhkI6CZOLIcIbWQ9gA5mK4mk_qbQWG29m7AL-Y67NwDFseVG0ZO49ieYi4bGaAQTMVYSQIsF9wynrRl4pkZ9Jcak-1QqSDKABGIdwLSz1hyeDxVlNzTp4yOnPehitWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=towzXgF0NMieEs_IjLfsiw5oFRce3_j_0tiyDrIsqG5ITC6gckBDe0O6K0vSqbUlvjxIjnJzS-hqb6V_dqv6OjVutvyr3QTx9AG-AaHTrM-LgIiw7fIKtccE-Xn_ozVI00F9WrrZFUgskxdSx4ewTAjcLg7G1EngkJ3wG4OuPAGUrXzT4zXxYOYwMqwF3Rd5QXyPLOqgaDT4NzDz1-KAH5APhkI6CZOLIcIbWQ9gA5mK4mk_qbQWG29m7AL-Y67NwDFseVG0ZO49ieYi4bGaAQTMVYSQIsF9wynrRl4pkZ9Jcak-1QqSDKABGIdwLSz1hyeDxVlNzTp4yOnPehitWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=jSr-VgAQr6uphvXvTncAHxHQOJI7m5IIX2D3gNp5j4h3PK6CcGqOBNH5qPDwJUV8vFYUuEtJb0uPeh4-g_oLoqWOL0Po248XxbCU_vcbe0QlOIwN9eRPjMnx63vua4kPPsFsBydPkihXOgkKVQ3WARVwHpBY4aPR-xDjb8IOWJm8dOJb9YNO1mxuOphcVljyvAxPRcPgx6Swwtu_P9IMEzxIWAY7WVNEUew-ScpnNuOhbG6XTxWmEgAmapSDjAQL8FjetByNPyoduUPT9iWjAqNIVt0Uyr0nsXbPDfzQb1K8bmaGwHDxxdlb3ES8HNzmbEp8gtYwLpqzcDsZ5_bW2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=jSr-VgAQr6uphvXvTncAHxHQOJI7m5IIX2D3gNp5j4h3PK6CcGqOBNH5qPDwJUV8vFYUuEtJb0uPeh4-g_oLoqWOL0Po248XxbCU_vcbe0QlOIwN9eRPjMnx63vua4kPPsFsBydPkihXOgkKVQ3WARVwHpBY4aPR-xDjb8IOWJm8dOJb9YNO1mxuOphcVljyvAxPRcPgx6Swwtu_P9IMEzxIWAY7WVNEUew-ScpnNuOhbG6XTxWmEgAmapSDjAQL8FjetByNPyoduUPT9iWjAqNIVt0Uyr0nsXbPDfzQb1K8bmaGwHDxxdlb3ES8HNzmbEp8gtYwLpqzcDsZ5_bW2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=J-FT-t5toG4sLm6nn8KsRxLzSKn7kZuMB_gZUWDTAa4gD76zAw5kyq7h8N8lQ0oI52sbq5QnozUdN2WnNqTey25J9t9srKIAy_Kj1191C5a6OuxIKuWrrYv86VZ--oET38sJzjI6V5xD6e0BnZFKP65xH39MlWDt4Kztnh4LzCodEZ5TMRyT5tmq-_9Dn9jnC6qOO-mJpCsgpL6K-ulctOI5_jwQMxI0OX3OEFy1_v6em1cNq66GFO2Yvdy1iDNSJ6N_w7gpkb2TSKHgUP7PEySiOIeQLNuGNwzAmqchqXU5ZEq_WXifeZ6N-gN7Z_ytcKLjHyX_4DjHNYzuwnlSFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=J-FT-t5toG4sLm6nn8KsRxLzSKn7kZuMB_gZUWDTAa4gD76zAw5kyq7h8N8lQ0oI52sbq5QnozUdN2WnNqTey25J9t9srKIAy_Kj1191C5a6OuxIKuWrrYv86VZ--oET38sJzjI6V5xD6e0BnZFKP65xH39MlWDt4Kztnh4LzCodEZ5TMRyT5tmq-_9Dn9jnC6qOO-mJpCsgpL6K-ulctOI5_jwQMxI0OX3OEFy1_v6em1cNq66GFO2Yvdy1iDNSJ6N_w7gpkb2TSKHgUP7PEySiOIeQLNuGNwzAmqchqXU5ZEq_WXifeZ6N-gN7Z_ytcKLjHyX_4DjHNYzuwnlSFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=OCQdKY7Ts6cyNDMJbiKhnK4mtl8hSUTazim6IUFyWWGqTM81Bn9ZFFK6jjDOGzc9r_YDZ1uhPkY4JfGt3v-63ECsyaFm-4YLtozYbQkwbu2SRBLmaqG36bEyn1XV6bC4Y3sffEnwXeI6NZQKhAsI3dlGmC95xoyceeXWzshYk9eFKUe7n8hfDEGApceZ69eYERiI5g7kUi_Idmc1VcvP3Y0gcXtuMRyz5-l0t51jQAhOMuzzHDq3aF41d_pgjNoNQ6Lj1OAnrjbyyb7oj6B8R2LaNlpzJAiMcPqA6sJNJg4-8gI3aIISWGhHgG3oltBOIL3yeNP68itjlxhy4HFZ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=OCQdKY7Ts6cyNDMJbiKhnK4mtl8hSUTazim6IUFyWWGqTM81Bn9ZFFK6jjDOGzc9r_YDZ1uhPkY4JfGt3v-63ECsyaFm-4YLtozYbQkwbu2SRBLmaqG36bEyn1XV6bC4Y3sffEnwXeI6NZQKhAsI3dlGmC95xoyceeXWzshYk9eFKUe7n8hfDEGApceZ69eYERiI5g7kUi_Idmc1VcvP3Y0gcXtuMRyz5-l0t51jQAhOMuzzHDq3aF41d_pgjNoNQ6Lj1OAnrjbyyb7oj6B8R2LaNlpzJAiMcPqA6sJNJg4-8gI3aIISWGhHgG3oltBOIL3yeNP68itjlxhy4HFZ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=Jy5IzmrJxuGozdfms1wADgK3DkE_jFjzQAR339dWlEv65AO1caeSM6KXNlpmozJe3dsxib7pMQM_Spk-JdHLJ6gbvFKJbrpx3G-oyfvO62eUVtyfAJz_3GgpOVMyTV9pRebdDw78Vnmuqj0TU21BGPFrkhNSGGMRaos33zKmTb9xiOXwtbun4agIajIdsPrx70pLIcB47ZzWZxhGFXzX9PUGITHVTvoD9eGXSYojXYvXbNdQHK8xaPeuxJaJV9JIbKf6M7uH7rSsFcMYevBrhyXumBmad8yBflBApaxdI4tYUvuTCpsYPgMJpgMsqpZyWJzp92NUuINqcf5H2d8ckQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=Jy5IzmrJxuGozdfms1wADgK3DkE_jFjzQAR339dWlEv65AO1caeSM6KXNlpmozJe3dsxib7pMQM_Spk-JdHLJ6gbvFKJbrpx3G-oyfvO62eUVtyfAJz_3GgpOVMyTV9pRebdDw78Vnmuqj0TU21BGPFrkhNSGGMRaos33zKmTb9xiOXwtbun4agIajIdsPrx70pLIcB47ZzWZxhGFXzX9PUGITHVTvoD9eGXSYojXYvXbNdQHK8xaPeuxJaJV9JIbKf6M7uH7rSsFcMYevBrhyXumBmad8yBflBApaxdI4tYUvuTCpsYPgMJpgMsqpZyWJzp92NUuINqcf5H2d8ckQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1wjUW6d-9K9UYgVig-PSemP04EfSB8vZQ7f2aTuNWgMEp2isFVWSsJ_nszNWBeChRcpp1TGgOw3k72K4pwk-w9M5BKz-J5MQKPvnVrFXkaONvJK69-HmPjXRMwin3SoeikzyEsCTfLM72EzEi-nRfFAb1vkG8tAHfel3i_l1WTbpWcsRhiUWAZjVPoU0Z7FDcoLfP6Xpvyh38k29XM-KgnvP6nimMgNxUhxUdInApdiRDTvQzbQJawrXGPRJlEWDOaFeedhQLSyxO4YEsYurA7ADwgdB8Z55vVqxOC0L4lreks7XpbD9XDf4dbASsDxDHqtswv6i59ALTBWxdrhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=p4JDeaheT7yefY5smEeBH9F4ITEqLBE377X4NXeh1uRKKXrFN_36BehgikJhlSS0DSzyaMPgOyRnetO_4BgLxeCHlSsn4VNaizyU-lBISSlsakgCNuS-xfguzdJfiVLhu8p_TDBEgCZ41Me97Z5a1Dmrr7pB-y8WYlWtffBjOkC2HvGOSemVXPJcTSe7IxDsrwzP3KDNgJfXyHWMgZjN_ZEJNHvdHKFNJQuykCSPFhEtcpbeO36HU3fONHWLEXczBRfV1CDSWY59Vz2jVfcp2bHDyTthZfKDND53uQDuouX59kXMA2M40HaVD636HUqgzUgF24YRQIfaXqlriCx_0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=p4JDeaheT7yefY5smEeBH9F4ITEqLBE377X4NXeh1uRKKXrFN_36BehgikJhlSS0DSzyaMPgOyRnetO_4BgLxeCHlSsn4VNaizyU-lBISSlsakgCNuS-xfguzdJfiVLhu8p_TDBEgCZ41Me97Z5a1Dmrr7pB-y8WYlWtffBjOkC2HvGOSemVXPJcTSe7IxDsrwzP3KDNgJfXyHWMgZjN_ZEJNHvdHKFNJQuykCSPFhEtcpbeO36HU3fONHWLEXczBRfV1CDSWY59Vz2jVfcp2bHDyTthZfKDND53uQDuouX59kXMA2M40HaVD636HUqgzUgF24YRQIfaXqlriCx_0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=ZUtLPJ230DBJ5aA-wxD0rBvDCb1vEtEsfk3Ua4LvLvZLalZL6A3h3kR-4hh-45MgRkS-KPluEJELl_TteRjxigHZYOW0tsaAnTf8hFc5brLdT_7HUiBMJsZCJDn8ittIjpm6BUwhtU2tCD5bktaDaxIPI3uCtueGMFKU2jdTvQmdAcTBGgmlj3Xc4ItgMcO5M0aLnGl0NgX1BXGVaUCpRupaD9Wf9eFh9Euq1DF3xysC7nn_nkU-5NEkl4XR_nqO5owX_Wt_lU4jILTcluhY4tkeV6FRHerZru5Y8nghP6Xa9q8yZYhfVBwsvjEj9mLD1AcLCUNDH1_iu34p4NZJaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=ZUtLPJ230DBJ5aA-wxD0rBvDCb1vEtEsfk3Ua4LvLvZLalZL6A3h3kR-4hh-45MgRkS-KPluEJELl_TteRjxigHZYOW0tsaAnTf8hFc5brLdT_7HUiBMJsZCJDn8ittIjpm6BUwhtU2tCD5bktaDaxIPI3uCtueGMFKU2jdTvQmdAcTBGgmlj3Xc4ItgMcO5M0aLnGl0NgX1BXGVaUCpRupaD9Wf9eFh9Euq1DF3xysC7nn_nkU-5NEkl4XR_nqO5owX_Wt_lU4jILTcluhY4tkeV6FRHerZru5Y8nghP6Xa9q8yZYhfVBwsvjEj9mLD1AcLCUNDH1_iu34p4NZJaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQWIzPRNNTSWpQuz4z-hXg4jseskGmXe0hLfhIjTttAffkt0vnjM3t4hnohEIs-uEZwV5c4_GAJ34DMd_aBf9avMaelIHZy56M9ltf8mygB3Im1oEGMFFXL6mDZCFzfF8n4DL-0mL0Zji2nvojGj-fGe9AipGQFwPLBTdt-HQoRXetAdEDpfG-RSkZuE0XUAqUaIMvohkQM_-6-ww89bQ7e5uFU9dF4G5_ZgPE2KSdw95W74vEpVPEZ7k4gC9o7ZadE1QFPDjQN9JhsKzqqtLp70EblslOE_59g-Oa6-TN3Obi2Rb1IYhHJIEuzuLBQhpTYL5byP8MQPZUZunOtTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPqKORY0Wys6_bkhrgF9tkAqX1iHkqSH0xuQ7uTWghbCKTxMHHpH6pL4C9UH_lXMFOOTWuRaG019DSFifcdhGJ1HBaSp-l8Phle5VwY8qMP1u9RR4JZzORNo8Y8m6TqgRdDawz-i6jPwKJ9JFQxpOOe9BxyE27kwAPUJSIPzy9F2fqxoRcrRa4h6ayj_LNcCCz-za0RNfVRAc9lfH4Alcp9IRiHUlnE5lf9tXisBc0buXZZiml2cjAs0AIShj93NPTzEtdG1z4WuLmv6x9cgT3B7J6zZlHpAdolLIOWh37HjIZHgXvFc89RygCsBwOtd7zLdYBmsLzxd9ij7JE-Ezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmiLuMKqgCRX3JtK5ItcJwcXQahMjh2s9fn6WIO-q4B_I0grBomYJu7ah1B-O7y-n8Rp0kDPNGH6r616GTDqZ40QkZDzcmWMaNzZjeNFBP0tCpLnLi7j5mE-KdckV1s1MZkQNHQmLRuiu-hdpCswNnl0DHkho7I00PzEBRGMeNL0z_F5FLAljd7ia5wZAkaIYK28kSyqtkJrop-VI9ti46bo7J6hBtrcv4K4IU12ENIluUrjrge4LRUoVZFd1zzzPYOPpiSPTHGuP_WXIUiutLxvQgKVQqSz8bGzoRzVkBiQ0ucT2HiyKOawD0eeM7OJteF8tWEcdTy6no6euYYVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibuw8eCgLFSmB2CVlITZI-GS_RHQOUWXU4zcF6BaDbJtGmz3bo1HmrWqfplPXg2jjpmjHY7qFPqfFLuOwSzDhx5kUvEVvyHjgq3-276Zwr20GOLGyPrq4PBsjyOqzGHxDwYFrb_77zxKGtHrKkCccSggOzM12Aixhp-UbK-kYTJYotEAvd2V-9405hOchVa6HUy1xRRGxJNNxj7RtF_cqjSqdvU053DR0w2R5L9av6tLK7XSG54veFDHDpBaP6bjxuBJn0Ol2fJxfhUYs7hPGa7Gx59N95NlIilbz_5HNtdRDLYZqUo7yY2s394lXm0IJlAmexAC-PXXoJu-PetB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbc0OwfRWEFUTsCZ5j8ertCif-sLd9FBXw6ss2thL6TpJNV4fj5qH04aedQXva-UTlWUcY5F1ro81oM179u8Z-8OYsU5EUjsknr7Ze5lqMpIdPCPcwnhHFQxL5SUxpyNC0cgbUzwqrCfjSeNXFBIwFr4RK8nB4HFMBVmWtbm_vZUng6AMZ96JOZ3HQztZy3W-gLbqQDFn5eTemFH4DBU_b_HILUYyaXpRm3EfyLMSHbGtrj0NgoLI9l5EBZ926NyGOa-CgGli8bWZbmXX3K2nTLOfdM-3yk82u-HDTGOA7MALlqiiUnEESDfoCZbGnDkYN4U6Nf1Ipnkse5Q3OlAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4unq_yfs-PSHbEfsZaTX9rX2ysY859mIRQ72AQD-e0ugMrdwPxkvgOQKLZ534vLFfVtgCfpkChS_KMYNfhWMeZvO21g4saZ3bpPTdqgUQqFpaFwzU80Fsg2-S87NkA-u465vTqPYdlaaczbyEg6vdW9pkYhseCZfXqkKiFJ7ozqxWlUY5zyECBItQDmyLHDT7huR4xMesPO04-upnY5akQ6bLgcIxu4uKkqQgbqz4FJ8q4ObbMo4komZ_dJzqT-et1ZAO9WuaJ2wEc5z9SomvfArShG1Q2x6-cmO0ytf4w0ykbSBQQfgp4skgA2fomHiCRuMblhfOUj8AFIH4LeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sI3jBnG_3fOlE-5K0Xeaq0asN40OO4rgvb3JMqRqDJL3R4FcrbM-xXtiJ0zESe-YDEAHVsy-uX_79tEGyiGlnRd8s9K3w8Zc12nM8bTFDmtCeShnLGtUTWW2EN8dBXFnhdydQk_4WhzQWXXAxMYsZsXgUELnPGFh7OWggpltbXWlW0WFdtvSUmjegtiCopi-MfL4992qq1N1WIhOc8rOKshThGsPlQfUO94GTcrcDYi_0eRcDgYNGLQ_qaHEebO8VILnhjY-5zqytS5qqErs_p1yq0CDz_6Fqm4ZITwySlk6W8J2Yl-BiFE32EYOmi7SKy5gDaZ_vrWaWRhmE4fdPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RU9bs99us1v0d2baTb1fr7gFqw5AJFwlZcxhTx68HRKiiW-u2gkaICYHhw4cTnfFT2X4FJYvuV2GDo7Y-SbIfjxXIkL3lcpVVrmHjP3SusCchG6PcFiZJFWsOBLdTy7v_C241YTxfiid6gjwZoEjXtwW8BSnyGmKyELsXNMh09EXVJf6RVJdBK_zJTkkqPfdrUApujaKY39S8_1hCOWa8iPAyBE8WYD6kvb4fE0pUOAfejaX4hUwyEL6Boav5edRYwdwqHR7GWtImO0T3ggIJvXdXSTbmWjSO53mRNLnlxALKMTQEl5Jmr8r4FBpsVFvs8034DaNVjN469YEgJ577g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/at7YP6_rrGev2YpT3WNDPv9sjbgAkWRzqf13aI1jgCU6F8EubUAn-O3XmboUwnfTTb7kQg-N8yxeK4n5kkx1UzMXSDxzDKpyIqdZxVe5iM1GhKUsCgIFVdEgGeWnPeifkLZS4U7SxHka9xGsFCdFuV9cRh5PwuqdAQdBToj1QsdqExaUjVxsjhCK1KIfNvi6jd-MOryZ2HmeGAP6Z3lK4uO3b80MLTP9bU5M_7XVqH1UmxacZdR6kUvRfDGRA0wfXbD8bZue7bLlEAyUwsLmXfYDKPaofWnABxQsSbdjvRqBxZX2LejZBYFMet5Tlz0Z3Y_z2vKn86JuM575mShAkg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kYNHQyAPBR5MPQzHeuqG5tjswzxx5nRvkpnjN8lUyT6DGXVveWMe9qKLhvtJG1h_AOmTpZknl_B2CdouyvV1kJvjpz_A1vPQZhKbhsxuF0Bm01l-h6gOn1-osAcnPEWYXTGNWRv9sQW1-Q8h5a4aopcsSrVwF3NO1_9euLK7eroVpkCs0NnkE7iZMgUKco-mQ1W239C3DgOMjomFlh9SEiS6bsw7Em82NmyKgaY_somnKxun-GKzWHRqWWaTGI5RIONWI6_dEDeKjyNxOYg_X8kBGUEHpbAk2lzuPQgUPaKzehfQwpRBG35GufW6rWdFtJj8UjHeTsXTB_oKL7aOZQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=jlsflPyTrdEc2h7q9YerFdTUtU3WhsUcPoaWrumoVRVbVIL0TKwmrd8rW12IYM-hDMaK2nqYLZHF8EpG6cT98ObS4dDFLBYpAbbKrI8U7IbyTsRoNID8vrSgvH_1sC0Ra1wdZFGhcLuC-2k-T7Q309o3BMOyHiEqInyzWiLYDQfZMAaK6B_uNvD7ySoJ8LSErqfY5sGicvgOlwEy-XSCD_vl8GY0NIXUqzhOKmue-sQUfQsfq2NXMvhDjG5XqAN0qz3j3gr7SkHQJwkiBE3oIzQuSOxRz6jmBFG3UOA0KkwpXJqZ-cp3MU_7wkcoIAF_yL9xcLaclsrrOviMZCXHBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=jlsflPyTrdEc2h7q9YerFdTUtU3WhsUcPoaWrumoVRVbVIL0TKwmrd8rW12IYM-hDMaK2nqYLZHF8EpG6cT98ObS4dDFLBYpAbbKrI8U7IbyTsRoNID8vrSgvH_1sC0Ra1wdZFGhcLuC-2k-T7Q309o3BMOyHiEqInyzWiLYDQfZMAaK6B_uNvD7ySoJ8LSErqfY5sGicvgOlwEy-XSCD_vl8GY0NIXUqzhOKmue-sQUfQsfq2NXMvhDjG5XqAN0qz3j3gr7SkHQJwkiBE3oIzQuSOxRz6jmBFG3UOA0KkwpXJqZ-cp3MU_7wkcoIAF_yL9xcLaclsrrOviMZCXHBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=UxSeLz1SOvhenyZtIxqnecRsOtJk7KdMCY1Jzoerrd8fc_p3LCXMINWKub1LPUBJsDIBRaJEs5KHegESTsOxXI41rUTOMnepUDcjFigaOt6W_NqMJoLlcssM5C6KP6L_TC13LVPaDz1-lc49-uu9nYrJJ9_7fE7kpTGWR2BLiJUCUgMktaOBPdnk8pXEXmmYL_8MTbmErpFqEF8Ys8DrrugAZaO_y6qbe_RswFub1QKZSM090iyVnOJNIDxxLIXJKFHb5qR8hDC1o1oh4xwujLE8qBS91HZ-M0REr05Mf0R9-jEWvbN7HGJ9es4_ACBJIOTFq-UBZCgxB7fzkvuEtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=UxSeLz1SOvhenyZtIxqnecRsOtJk7KdMCY1Jzoerrd8fc_p3LCXMINWKub1LPUBJsDIBRaJEs5KHegESTsOxXI41rUTOMnepUDcjFigaOt6W_NqMJoLlcssM5C6KP6L_TC13LVPaDz1-lc49-uu9nYrJJ9_7fE7kpTGWR2BLiJUCUgMktaOBPdnk8pXEXmmYL_8MTbmErpFqEF8Ys8DrrugAZaO_y6qbe_RswFub1QKZSM090iyVnOJNIDxxLIXJKFHb5qR8hDC1o1oh4xwujLE8qBS91HZ-M0REr05Mf0R9-jEWvbN7HGJ9es4_ACBJIOTFq-UBZCgxB7fzkvuEtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=suWUj5bcbjFQqBTXxlX3qqiWMkgARlJrYOphYDG5X-9jn8T2d8vnZ7ktIDR-q6AX8GSPOkTPvkETz3kgkcd-Jj0SEw-bx6F7JjlQNtfofautKM--EJvBam_lJxKblXJab3qZPApjz8oLav4J2jgaks4qTOXYS1D7Fa46uoVPkY9hCcUEtZxqEf9zkWxdpjp6xbd_pTTGdYew0VtuqfH_cdgsqQb5MKDDoy3BtjZC_eU6yMN-BaXJlYwT7gQ0SuIObQAVifFAmN_UUI0fRIegKCzvFFWQ9KKa4WXfXNmHxXwtdnwKKRcWpPDYfkpwjNkOeg_QKIwX1ZFP-DzhXENlPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=suWUj5bcbjFQqBTXxlX3qqiWMkgARlJrYOphYDG5X-9jn8T2d8vnZ7ktIDR-q6AX8GSPOkTPvkETz3kgkcd-Jj0SEw-bx6F7JjlQNtfofautKM--EJvBam_lJxKblXJab3qZPApjz8oLav4J2jgaks4qTOXYS1D7Fa46uoVPkY9hCcUEtZxqEf9zkWxdpjp6xbd_pTTGdYew0VtuqfH_cdgsqQb5MKDDoy3BtjZC_eU6yMN-BaXJlYwT7gQ0SuIObQAVifFAmN_UUI0fRIegKCzvFFWQ9KKa4WXfXNmHxXwtdnwKKRcWpPDYfkpwjNkOeg_QKIwX1ZFP-DzhXENlPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=BtN--fAaK_hyZbsEtWt1qHE3BziY_E-LZL3M29298LQZYxx4V2FgRcMHANCDmnWtu2ydEIXjeyikMFIUPDNUBe5pFMZCubX3HbxcxXvHDzlQ6fMtDTnwgPSdbGELSQBZXP9gl-3K8QqC3qTtfWyfhtzNh2BhJYOZA-zgaFB4cpn-Nq1xdBTf38BsMTT9VnrcuX3qW-VclbgA1nMEAv9-045mBalhoTjGhK6EeTab_8Fwf7FAmiwu24UaTw-7ZpE-yhN_ONP_rEx_iygN0XBDHJ6_5Ayt6FzEUNfOvNUYPPVk7HmDOez4Teij4ZgGKyWvlBEZvzBlFuXWXAL7siKyxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=BtN--fAaK_hyZbsEtWt1qHE3BziY_E-LZL3M29298LQZYxx4V2FgRcMHANCDmnWtu2ydEIXjeyikMFIUPDNUBe5pFMZCubX3HbxcxXvHDzlQ6fMtDTnwgPSdbGELSQBZXP9gl-3K8QqC3qTtfWyfhtzNh2BhJYOZA-zgaFB4cpn-Nq1xdBTf38BsMTT9VnrcuX3qW-VclbgA1nMEAv9-045mBalhoTjGhK6EeTab_8Fwf7FAmiwu24UaTw-7ZpE-yhN_ONP_rEx_iygN0XBDHJ6_5Ayt6FzEUNfOvNUYPPVk7HmDOez4Teij4ZgGKyWvlBEZvzBlFuXWXAL7siKyxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=ROECPHvU93-8pfrFaWQTTggt7kmlhGUTuE6hC-QCyFPJpHrQJ9lKf1hKv9Wl54gJmRMvA-IAZXbEiW5QLZHL5LLLrDbB5JIBPujVoskqb2c1l2TNPuckNxJqA5iuqrQis2Md894EGZ-g7t6TrqVfqD95z9JAKxdM4to569nTlyRpUxS2Uz2YpXNlz08PluFbGUBRBaQdHrqQU7RZJoU4F_TA1YRuZGcVAleBvhOeed6vRLcdpjXKSNpq9vAQzToYlGVtTu5thGAzibKmKCrOhrEeaQUY8V_vZSa6ma0hrPIUYynUc-zA9_tv8M9hQFEu-0Mi7UL5d7BJDu2svtqi1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=ROECPHvU93-8pfrFaWQTTggt7kmlhGUTuE6hC-QCyFPJpHrQJ9lKf1hKv9Wl54gJmRMvA-IAZXbEiW5QLZHL5LLLrDbB5JIBPujVoskqb2c1l2TNPuckNxJqA5iuqrQis2Md894EGZ-g7t6TrqVfqD95z9JAKxdM4to569nTlyRpUxS2Uz2YpXNlz08PluFbGUBRBaQdHrqQU7RZJoU4F_TA1YRuZGcVAleBvhOeed6vRLcdpjXKSNpq9vAQzToYlGVtTu5thGAzibKmKCrOhrEeaQUY8V_vZSa6ma0hrPIUYynUc-zA9_tv8M9hQFEu-0Mi7UL5d7BJDu2svtqi1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=cSXRFXIZDtfvcFoHMKIcHdIOLvtTvMNtU2h2DlL4GB_nM6QaoYJog8aioZi4MJJ86McO4DXZKMA5TLhMYqcjWxLHLnTa6M4g7uCiDQdDzE3-36-9q2YP7DaGGeXtVRn6e3opRrcH4pTxJ6cQt_MCIO2NN4z2xdYBTVdOk3Y9dOePZdEKoG0Yn-BaQ6-EOtvIi3a1mibhatsIVSYgqCA_YWg2RVuSDSrVUvpGMYAgV7I0UlJUoVdcY2SynVohPwVWMs6wvcA-iGoz-xm0xVz8_ICu9TqBZPjbZh_YRWXr5Btyzgf0ln6ziOmnKDEWI6scCo1iqlCfUlyPkm1VAN21sA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=cSXRFXIZDtfvcFoHMKIcHdIOLvtTvMNtU2h2DlL4GB_nM6QaoYJog8aioZi4MJJ86McO4DXZKMA5TLhMYqcjWxLHLnTa6M4g7uCiDQdDzE3-36-9q2YP7DaGGeXtVRn6e3opRrcH4pTxJ6cQt_MCIO2NN4z2xdYBTVdOk3Y9dOePZdEKoG0Yn-BaQ6-EOtvIi3a1mibhatsIVSYgqCA_YWg2RVuSDSrVUvpGMYAgV7I0UlJUoVdcY2SynVohPwVWMs6wvcA-iGoz-xm0xVz8_ICu9TqBZPjbZh_YRWXr5Btyzgf0ln6ziOmnKDEWI6scCo1iqlCfUlyPkm1VAN21sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=q89ShGvyumIoSxc_bJ96Qhc9q3GjKL-15305ItV8PleenTVT85fn0YPv6KPmVYcZ3wiMWqpLJKLNUefe11fX1EHvNv8ZmUzziliTbaxdHetJSZsPrlUR25wOKJ-uqlLtTBfDgY0sPeFdMdUwD5V0RNJHxQhrHW7XK2oHBSBU2itDo_lS9TThwCxCwD-jOPcLWiED-t2qFiP1itMGA-E2tuw2_KJvQ2yoGr1oKd9kED8BxFbiNlg0cq8_cuXuTZoraSctFKyeFSz9We-y7Fhiyv1pwhlQ5yZhOfHAKIWyaUtyWAxXaeoEhpDEOMlDKzU0sX-QJazBA2XmzEJGesqtaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=q89ShGvyumIoSxc_bJ96Qhc9q3GjKL-15305ItV8PleenTVT85fn0YPv6KPmVYcZ3wiMWqpLJKLNUefe11fX1EHvNv8ZmUzziliTbaxdHetJSZsPrlUR25wOKJ-uqlLtTBfDgY0sPeFdMdUwD5V0RNJHxQhrHW7XK2oHBSBU2itDo_lS9TThwCxCwD-jOPcLWiED-t2qFiP1itMGA-E2tuw2_KJvQ2yoGr1oKd9kED8BxFbiNlg0cq8_cuXuTZoraSctFKyeFSz9We-y7Fhiyv1pwhlQ5yZhOfHAKIWyaUtyWAxXaeoEhpDEOMlDKzU0sX-QJazBA2XmzEJGesqtaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Z3FyHmMX40ebmi46R3NjGhL5yazjyWZc0t6YYnyj1qYsXYL3aaTLHSjK5MGKH7vU1dYPSJMK5jv6d7AbcOJygKDPVKDf9ixKAcNOzChI0hdE9qshIj0GW5SsUWLFcw9XZqefRqIDhbGZwXV2mdPVJNaSnIuK1esck1p6EI8S0_ghP7SPQCNqH8swbabRhIEtJTkYuwClS4_4w-QaywUy5G1Bneqdj8y8UoNR2IzRVXG_HRa1LZKKU6LdbdqK5HUlDw_h9ISUQDQPdsX0x6Ox3NyJL3w2Iszrfjzir1vkGFvBOQakyVYSSwkb7iyMVA6-T8Q5oma2Dfi3i3PEsTvXSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LqYXBPj12hwJgYEZ1aJX38bj83Am984XPRu2gSjf1bkmCSOouwAb7gpme0GZVB0vvZETRzzowN3vzAWwI51HPNKjWM4ra4gi12xq6D9bS9uqr7BJXi8g8_RwzQyPaPxilk3-CAxvfarLAz0kViFKT5Tnabr_uFpjR1whw5IEMOdc4YDL8znPKg9uwtApzWcbFMH6Q2l9jCT7VD_mMJKAefGwIoCJUfcXOSHZ1C0qH-_9dPT7kAnl1OfrnmJCU_xE_1EqDTSKFXk0PF6o_zqh0q06j1SukQJjmpIf9Dtl8s8lFBLlr_LE9LQmPSI0cjakPBbGujg_Ub8qvsfRxzzRtg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=Coh2ueMgW1Woq7nT9W6TFNMGn8YsH7_cfvk61jlkjmBJcoEFBTQgfvonPbB5i8vT3yLGuxuLEJzrO5P34irHMxmiz_aeFujj0abMsSShiIlt0CLjGMQp-WHzK6M9wGl5Y_6MZmVf0hj-r4UoBDxS16gaSmlsYM2rDjp6nx7XX0EW1op-_zao9R6NmrWympT5fPybWUjemxkuaMHNW7pGwCHhi-iiLtZWZX8D5uJXYn_8v9CF8V_uYS33DAzT6TG36GXUu1O5yksHmDnuUIIum_vYPC1xJMWUDTsc8Wqzdb0DoWXBK3B6Rb-9ZMnYy_ZbdVmw9Q4W9lXZiJQn0p9nTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=Coh2ueMgW1Woq7nT9W6TFNMGn8YsH7_cfvk61jlkjmBJcoEFBTQgfvonPbB5i8vT3yLGuxuLEJzrO5P34irHMxmiz_aeFujj0abMsSShiIlt0CLjGMQp-WHzK6M9wGl5Y_6MZmVf0hj-r4UoBDxS16gaSmlsYM2rDjp6nx7XX0EW1op-_zao9R6NmrWympT5fPybWUjemxkuaMHNW7pGwCHhi-iiLtZWZX8D5uJXYn_8v9CF8V_uYS33DAzT6TG36GXUu1O5yksHmDnuUIIum_vYPC1xJMWUDTsc8Wqzdb0DoWXBK3B6Rb-9ZMnYy_ZbdVmw9Q4W9lXZiJQn0p9nTjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vyzklOb3kYJqCveNJmOFP-fVt3jnQD8hI0m1SHREY5jyYc5Gyof0MyJ1bOsvKEccPqXp6Z6BGN7jPbiVrThdIM7gg4LnlF1CweB5ydE_Cwo9tSJUWXix8EXUiT6wYVjoWyOMVDVlj6GbN7l_4Tcyrl6wxtfW-K4Ce5Rj1K-9aljHLPlJdATSId1WPoUJIQxFas5ICXxIIWsFLsR7oBBxxTafgMIrNAXbHnPKJGBi8M1nkQJ2_uH56ltra8GqQnDTPpKrF9M_OV4KcLaLq2jDxLkPoST3aGFMwimhcrklCDlnUa7MsNzu69Eg3TCaLJ36DMEIPvjepjNkYPdjre_G-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrFNSYl4oy9oIrl_H1ij3BrunQiQYAxN3W9_xQVT5KSmqz8WhvJO5ZVUpGLdnD0hxDvec1FVPN1QUROUrU8Eg_skTugJJ6zJHxEwNShb1z2o8pzl_oJIa2AhU_Q7-Tka0VhAlVvI7hBCmq6KXcMfxn-8DObHVqydwgSewIPGzrmg1AGjM7DENGNakZH4gOq6oQOtv5jPkjaRT23x3aimIYGGBm1juf7jexbzwXa6U_BV_8reRzaYuMtH0lbkJOOvfwKy2hSrNa_4LVfpt99I4qmK9TKLbThOCo3pU8Bcrr2M2Jrj6LgwgjaxRFQU1eRtdtR-4nLISwXcTnEtJEGvpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QaJRTwuvq2u2y1gVim5esS322s805fXrFytbqBWVvtb2-pTntuHt5qc3V47kJqKc57_I7a28QWjzLXCjGNjxCL1DAmEyyobwfkz-sS7j8xhhFJPLVa-R0AOUxHSAGpAxioyTqSJq9kN-VMX0ny2KKTp_6V9JbTnLVJ0nmiufqdVZQHBaecsK-rQqqtQ935bbWDqUyxMpam0abxJf4G3DKfULLiYZMgJ-mbY_Rr7clT-eISvBU4f9qVeEpsi9-v16GWA7RitSv_vUVJd4UNWFTxM8T3I5GtcgZ2cSbRnyc_6pzyN5jToqWDeZ35wlx7wT4rmKftwWVLJsQg4RVcSbGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jHznLjtfVzdVpR5MwQgn_02COuMztzydaCsAv_Q1hl4HEb090zSpoI3nd2KgrF7oyxjsG5yJrfXpjkyaVJTJLO9Nwwbznv2C85jOJovvFcr8yoYIxwoJxdsN6EbeC5obsbeo7T4bkuJkAWkBlvHzh9Q4TwoxxfqsWb4A4q0PF_T4Xm_i0r_jClnI5UbH0JBilvRmRhCeLzOTdi4imoU6-44jwHcobbdJdnz5niMuT1i2-T8ofjR0PYeKkCJc5ph5Nywwt2_IjFf6RjNKiPIZffP0guNyOVMCbA3e_3AU-Nsmwuj4wMoLUWox_kKSJ1Ou-tLQJP2l_cOhMr2oF8oXBw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=eXW8hb9a7vPCGolI6-7vAex5srfdluxnh5pRtTBBw73rTl5fBGUjHhTRK-jmvqnY3lH64eb-DLZRSSuNfV8o23yeqQVYHP84jdFg5MgYYUZT2Te7mTkTcFB0GMwsOYzLQdouC6M4HGm1OfWwatTCmlrJie7uTARKV5RzSTsRaf4dpIBydFXhKFr7tSGqGoE7zj70o6x5PpAl4GdloNqbyR9VemkUd3zSOPhZoaKNfRC9HhrDR9ynlbfDZOBcA2aF4luQBtU_FtoL6syOl3H1q5RZn96rsLtXOI8-NKy_E82kBkhRf9KAOV8_C4ecTqIGOVv1tupFH3gkDfxXxBJhEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=eXW8hb9a7vPCGolI6-7vAex5srfdluxnh5pRtTBBw73rTl5fBGUjHhTRK-jmvqnY3lH64eb-DLZRSSuNfV8o23yeqQVYHP84jdFg5MgYYUZT2Te7mTkTcFB0GMwsOYzLQdouC6M4HGm1OfWwatTCmlrJie7uTARKV5RzSTsRaf4dpIBydFXhKFr7tSGqGoE7zj70o6x5PpAl4GdloNqbyR9VemkUd3zSOPhZoaKNfRC9HhrDR9ynlbfDZOBcA2aF4luQBtU_FtoL6syOl3H1q5RZn96rsLtXOI8-NKy_E82kBkhRf9KAOV8_C4ecTqIGOVv1tupFH3gkDfxXxBJhEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=V-EX6F4dhy6drRWDAToly_RgCdi1VcHHdpQx2DNUA8sV8WsPkjSyFESY2pCvZd9v71Eehh4gh3ckw8rYSWIsUuyrhgc6AilO-UrCeR-pek1765J6iVzLE18p48mclCQ0RsFP1UXU_jIsH2LlgsW0mqt6xOvzuNyF22dJ-t8KQ04Pu1Zz4WNzmgEDue8mf64rqjFsCpGm8ycxXUu_9zYnxBBcO3KbZr7M4MNxpgqwXleyZslxW_E8OZacGlLsKwdBbti3_kv53Z4hLwfcxApq--4PaZKG8r4ATH6Y8gsU85jbdAr83948fcJ2Dv0_wzh_4V0DXf1tOWuZ-JaznyLeqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=V-EX6F4dhy6drRWDAToly_RgCdi1VcHHdpQx2DNUA8sV8WsPkjSyFESY2pCvZd9v71Eehh4gh3ckw8rYSWIsUuyrhgc6AilO-UrCeR-pek1765J6iVzLE18p48mclCQ0RsFP1UXU_jIsH2LlgsW0mqt6xOvzuNyF22dJ-t8KQ04Pu1Zz4WNzmgEDue8mf64rqjFsCpGm8ycxXUu_9zYnxBBcO3KbZr7M4MNxpgqwXleyZslxW_E8OZacGlLsKwdBbti3_kv53Z4hLwfcxApq--4PaZKG8r4ATH6Y8gsU85jbdAr83948fcJ2Dv0_wzh_4V0DXf1tOWuZ-JaznyLeqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8-Q158MGrlZY9lYpybtYycMX37hIuoVaY5dOToKNP-ypmgrMQ3NYrSEcieZFQdfLm06W9xdyfWORkOp7r5UhdrSHZQJkg4d5WdpQErnT9w8PnL7HZ2vqCjTj7GB_evjwAwb7HbTLf9zeG-JAyeoC74wMUB9SJeNiGW3RHGfCnEP_OyJsfpt7HOax-Cure1P1BJ_CjA5UteOpFNruVEtKYtWY7Oh5KnrfpQ1Wrxb-9ZywMdXRbzYzja3AfWCVjftmoNGnFPmaERNIJ4q1f9jvA8m-49W00DW28d9PwCtKmX1My06Qg6zsAmN7SS5107FrhRKZZZGCzQyxIF1TNlbng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=MjroESG03t0pnMm7n003cetbryclS95OxqlmJEgX4vxWSatoNeOmcVAjVDvKYMeUilk_rscFTXq48goxoO0_V4PPqUUwfePbXvu1ZMs63kxLM9cwWN4AmWBzz2N-rb4qkZmcnHTgdZ5oytdT3Sz0BigF4wrmfeP59E64OsoXLntCZ5uusMt-Ongujv_8bqt7tCNI5Fs9skkysgqv09rC1x7hJfecfhoQcUR9rUmnuMp6zxdm-BL58uezu_-FrMLcjcA1Qrc4x-ACtaueFQFRixPBG1x5NAxXH4ValO2TytiDPT4UMTG3B8LbhVgSKuU8uE4keyY_odleMhFHZWmeFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=MjroESG03t0pnMm7n003cetbryclS95OxqlmJEgX4vxWSatoNeOmcVAjVDvKYMeUilk_rscFTXq48goxoO0_V4PPqUUwfePbXvu1ZMs63kxLM9cwWN4AmWBzz2N-rb4qkZmcnHTgdZ5oytdT3Sz0BigF4wrmfeP59E64OsoXLntCZ5uusMt-Ongujv_8bqt7tCNI5Fs9skkysgqv09rC1x7hJfecfhoQcUR9rUmnuMp6zxdm-BL58uezu_-FrMLcjcA1Qrc4x-ACtaueFQFRixPBG1x5NAxXH4ValO2TytiDPT4UMTG3B8LbhVgSKuU8uE4keyY_odleMhFHZWmeFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Ag74gAZBm5hQ6cTSDzyw9tvU5qU_A8wxgdsNpssmi_ZeftQgQxTOmkTzmCUfuVw5bIWI4eA2y-_xSCYxIKH4Jujgx8GiMfhyMMyWEit_hLAdNGJtOWo-YB1TmQF3ABohI3AIOQwk9z2RaIInAP7TBW2pdPa4d4sFLVYmbjtYMR_O1dnUvN0qYzbMbLbkqeSfw5Cx44A7hiMq2fMn1iSQ3SfwPweGYfoDQjJVAH9fAdtfpJaqnqmiap7nCwFvYm9TallecOGF__vN6ignwR2CiwGt_PbIAzQnwyFQPG4MLLPJzabpidDb5R1XfbKTUruYtry7EjDxflf6P3eiPZa-DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Ag74gAZBm5hQ6cTSDzyw9tvU5qU_A8wxgdsNpssmi_ZeftQgQxTOmkTzmCUfuVw5bIWI4eA2y-_xSCYxIKH4Jujgx8GiMfhyMMyWEit_hLAdNGJtOWo-YB1TmQF3ABohI3AIOQwk9z2RaIInAP7TBW2pdPa4d4sFLVYmbjtYMR_O1dnUvN0qYzbMbLbkqeSfw5Cx44A7hiMq2fMn1iSQ3SfwPweGYfoDQjJVAH9fAdtfpJaqnqmiap7nCwFvYm9TallecOGF__vN6ignwR2CiwGt_PbIAzQnwyFQPG4MLLPJzabpidDb5R1XfbKTUruYtry7EjDxflf6P3eiPZa-DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=S6OcvnQb3VinuGJ984sUfr7RWoFposgn9qhsxHTF7q2EB_hVu7T4wfbWfPOEHlnT-3FRt8vWkQqgk_dDDc4phcrGFnjD5jGU_cPP8tmsk79-jegkdLkhccy5hw7sFir9gfd-xeyrMrdwtPpQmDyoDx1Vs6ZR4Hsf-4RhSnDUEXp8qh-BY-yf03Ue1S6zGjOTBX1svg0fOR92Dp91FYepwv4VStTP5XzD1UV1vwsLqkNXlXokh1vQXJBnjtOOSEunHPggreyIo321RUUceSh2OCDNILTMNiBRlWCZ3uA_2FdyEiebZWa2iAfceXiAn2b-erDpvEHtpVRwPY1JgHFniA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=S6OcvnQb3VinuGJ984sUfr7RWoFposgn9qhsxHTF7q2EB_hVu7T4wfbWfPOEHlnT-3FRt8vWkQqgk_dDDc4phcrGFnjD5jGU_cPP8tmsk79-jegkdLkhccy5hw7sFir9gfd-xeyrMrdwtPpQmDyoDx1Vs6ZR4Hsf-4RhSnDUEXp8qh-BY-yf03Ue1S6zGjOTBX1svg0fOR92Dp91FYepwv4VStTP5XzD1UV1vwsLqkNXlXokh1vQXJBnjtOOSEunHPggreyIo321RUUceSh2OCDNILTMNiBRlWCZ3uA_2FdyEiebZWa2iAfceXiAn2b-erDpvEHtpVRwPY1JgHFniA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=JBTgWh14-A_7IwLFjLI_KSJPONhS_MzmOGdtzrhL2seuGjGL54TpkCrsJhntFSD7oTCNM6Vx_XEL2zavd-6x5V75NtrqZacT62hnEKcV1KaYEh6dPCsEHD6_--Kr-vk9v-FldhetM-ctZwuMwKHd0yd3c9MhyrJwAM6KsFlxu2KVNbWsdzGgJzVeQI6otdUOjyYjjd-V5ogHXsUEJPa41Jkm82ugKtnN3CEs1O5zOkgLB_lBt-rUr8VUoiwcozU2Hou8jqBc_uq1mF2-1-fk8jKDysoeAHJUc4cCRz2yIGd07OsLYUmatDUg1KMJTy8b6yrj733yvaMd5eKXD0MBuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=JBTgWh14-A_7IwLFjLI_KSJPONhS_MzmOGdtzrhL2seuGjGL54TpkCrsJhntFSD7oTCNM6Vx_XEL2zavd-6x5V75NtrqZacT62hnEKcV1KaYEh6dPCsEHD6_--Kr-vk9v-FldhetM-ctZwuMwKHd0yd3c9MhyrJwAM6KsFlxu2KVNbWsdzGgJzVeQI6otdUOjyYjjd-V5ogHXsUEJPa41Jkm82ugKtnN3CEs1O5zOkgLB_lBt-rUr8VUoiwcozU2Hou8jqBc_uq1mF2-1-fk8jKDysoeAHJUc4cCRz2yIGd07OsLYUmatDUg1KMJTy8b6yrj733yvaMd5eKXD0MBuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXUoNZF5u4OwYYemAmgEUiiVaCPSbW_PMHc_snD7qYALFJzp6XruhsbH8MFs12oxzN3SN5vMEs5Xgu5ff2nXpEHHiLeqmQbtwfnZKRmTfh00rTE1HmBU46l7pXuChkDYu33FL5fmWcx8RkSn7PRIFzS2N_E1vD4Zmaz1oBixvozbvA9Ak54gP0gllZzlAbTDG7ApBIAX-OwDUpciA7Vcq4FonuYJUpPTLNfWeRUyZ-WtIsK3dtLfU0D3kH-BX4pPQrYQZAE3ofssiT4uIv1SYkv6jeDZdPsRGGtL5zzjFJPVU0jA3LrxcCpHtMI-BXjdWSzooPx-KmDTURGHpAb8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKin1mk2qe4oiEYPhwZRhAAgajhEt0dtUVu1lVced-ruywOMYqdysd1wYZl5bQNbcinuAeegjy1twf6NbWT_KWvFfv2l-8Soi5RUO0v7-kCcpWEx8fgrZRUjClUCUJVq-Y3Z3BVwbl1IvXflUe_2vQUh13IPk57S5Op4COXyEXVjrKH5FZdTWA6Sl9MfUli_ZT1YRpLgjiIq0JDKjdSKA3cImDQHy5jzpqgMARhaAxC_Kuog9QzK-bXv4EbxqmXUVgIa79pg8iW5Kl4YYqCtBV6CcfGiQoLJZB0OXtTbCuJ8mOXXNAn-QZj0TCOpBbaG1rTX-_Erjm8SvQfclkcxOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=PNuPtQxGIneWKWv-U4EtWapT_Ev52XfE2fDlbnX-K3vqrsbRurU0dJiVHpUG5CBox9lAZeKSwx_2f6R9NTdPIEjxWxAtMTP0BhPG5Rz3gqIaJsA0ezh9YkNqFbBnq0L7onnoRjPvpEikS_mbnWA01bzo7Ta-sD7aTtBEQl4FCaKAkPjn_CnJDobIjZteAJFCYOeJeA09ZA3mCWy0QYTx8pzGXBGhM9kI0Ih8egFnJBM7UZ-IyoOalWHNgmmL7qx2oc1r90_ANluuWVgjJ-mRJLVArDTc0ypkjzFl-Z8inM_y-RrZLVu_IfOyHGDWx2kxUVQfF4FnLdz9WKU4j_5sLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=PNuPtQxGIneWKWv-U4EtWapT_Ev52XfE2fDlbnX-K3vqrsbRurU0dJiVHpUG5CBox9lAZeKSwx_2f6R9NTdPIEjxWxAtMTP0BhPG5Rz3gqIaJsA0ezh9YkNqFbBnq0L7onnoRjPvpEikS_mbnWA01bzo7Ta-sD7aTtBEQl4FCaKAkPjn_CnJDobIjZteAJFCYOeJeA09ZA3mCWy0QYTx8pzGXBGhM9kI0Ih8egFnJBM7UZ-IyoOalWHNgmmL7qx2oc1r90_ANluuWVgjJ-mRJLVArDTc0ypkjzFl-Z8inM_y-RrZLVu_IfOyHGDWx2kxUVQfF4FnLdz9WKU4j_5sLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Urbmsf1JbCPqCM9nEEHe--eJjlOPn7bVFDmr6SBcoe6kBMpzqgkhNKpXPiKpMdy2OGi5Y61PJDiyRpj9kOaiIbyKkqWdlEmCInSjn9RBa3PCMF9iAzzNPw9zbJ3iLYvEw7dabuieYzfCCidRJ3MAWHPy4m0HVnpFMEsuGoLdwt5DwL2--B7thjxflL7e8w4TNMJERD7BAuPkDwcai0w2Oi0XmiSE5tuBZ82Mp9GK2ViqVqvlAYBTKUohl3SeFok7PuyENbz6D3RO46Yiy-Bc_0Xj-mDH4ZLNQ9y3XIcPTzkq2sWKVKqqvaqyExISDiNAz-oiBbYDcMof8IgQqIu16o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Urbmsf1JbCPqCM9nEEHe--eJjlOPn7bVFDmr6SBcoe6kBMpzqgkhNKpXPiKpMdy2OGi5Y61PJDiyRpj9kOaiIbyKkqWdlEmCInSjn9RBa3PCMF9iAzzNPw9zbJ3iLYvEw7dabuieYzfCCidRJ3MAWHPy4m0HVnpFMEsuGoLdwt5DwL2--B7thjxflL7e8w4TNMJERD7BAuPkDwcai0w2Oi0XmiSE5tuBZ82Mp9GK2ViqVqvlAYBTKUohl3SeFok7PuyENbz6D3RO46Yiy-Bc_0Xj-mDH4ZLNQ9y3XIcPTzkq2sWKVKqqvaqyExISDiNAz-oiBbYDcMof8IgQqIu16o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=RfOrOzRvtPBRu8hRlFiXbnzVtZj783YV2SJKpH1fJMc4XrLGVGKFOSp_PRZe36ZosfwS_8REeFfLdYl5D_RW8j6W8BURxEjMs-7x1oBHvuYJTkVAMasKnRXZvssIeaUp4WomZbe2ggn0H4On0iqvJ3YX81xqITv3ZLt5_2E8d-LohgiymiAI_l5maK82IQNrlXA6azGv7kYxEHC1AnS1Fx9zcbwr7BVTymTrKKSeKFAuDeTplrw8ml_f_q6NwqL-NK9SGh5vKtrBbko1UDg8Wkh4evVKpSL5i7xfhh9y1q6sTuopG1aJVNVSljvVh5d10bk8Sg6MFdCaWQWC7TIKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=RfOrOzRvtPBRu8hRlFiXbnzVtZj783YV2SJKpH1fJMc4XrLGVGKFOSp_PRZe36ZosfwS_8REeFfLdYl5D_RW8j6W8BURxEjMs-7x1oBHvuYJTkVAMasKnRXZvssIeaUp4WomZbe2ggn0H4On0iqvJ3YX81xqITv3ZLt5_2E8d-LohgiymiAI_l5maK82IQNrlXA6azGv7kYxEHC1AnS1Fx9zcbwr7BVTymTrKKSeKFAuDeTplrw8ml_f_q6NwqL-NK9SGh5vKtrBbko1UDg8Wkh4evVKpSL5i7xfhh9y1q6sTuopG1aJVNVSljvVh5d10bk8Sg6MFdCaWQWC7TIKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HflheeGWyxSyJ-RRD7PnQC2CK9QfIL0as57iFMRVry68tCYkWL_7qfXUK_Cgxbehdw9V8k5M_gmK3YcXjnDgH_Slx1bzqaxHObA-bsOWUjei8Oxlv5NemIHLIEQre-R0uupr4tnYFUHl9AQ5Z_kdjReQjlRxPkNIyOwDbjckbZmZXUZsAAboo7jytKNSGbalSsJ8D4VFhQS_GoFSBcI_8OyTjOhH7WwokiqefkHQzHoIjCBzIX2S0A4s_O6Cig7JUwzpeHK3WWZvcZwFfEti1jajlLsujiiGuZiT0pE_brlAfs0tPQ9cfARgzpjMWNiWJmreGnnMho9SPIBpdR5dSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=f7_9k0WwHTZesqyMTjEA-kEJqFaWcJm7mp7lJKMrX13xF0s_vVc4Ik5RehSfC1mPJjzqq8gMthUnSWf8rOfuaSUZT8p9FCev7nLdCTEyYOFezDO1gZfK1wtahdtJGJxkmJ8Ae4ae4n-hlF72Sne5L5dbqdpLWmo2udbM5oVHwZt18stcRCaMP1-rbNYWcrbFa657aB3MXpi3xUIbH6moIaLSH7SFtwsJgjes6sIG7yAFv9zUf1Txq79G-OKrlErvkyYKtc2dPA_JSi2HUgauDlrjGeyKtfpyUPZ1cBqKbcrfc0bRdnYtsZGTGK5qDbPL4ZemGA67n232KuFpRCZ6dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=f7_9k0WwHTZesqyMTjEA-kEJqFaWcJm7mp7lJKMrX13xF0s_vVc4Ik5RehSfC1mPJjzqq8gMthUnSWf8rOfuaSUZT8p9FCev7nLdCTEyYOFezDO1gZfK1wtahdtJGJxkmJ8Ae4ae4n-hlF72Sne5L5dbqdpLWmo2udbM5oVHwZt18stcRCaMP1-rbNYWcrbFa657aB3MXpi3xUIbH6moIaLSH7SFtwsJgjes6sIG7yAFv9zUf1Txq79G-OKrlErvkyYKtc2dPA_JSi2HUgauDlrjGeyKtfpyUPZ1cBqKbcrfc0bRdnYtsZGTGK5qDbPL4ZemGA67n232KuFpRCZ6dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=NC-7KuRmPhDT9zOBhnWAcBjKMWnfysa7JkagdhnYjImgtfLqWeRcmmiFSbQp_7-aCmsiFl_wRw1zpt2HQR_c47iTknLHes_O6Xp3yRH3lVea5n8hv4MQYr1sEMCpQo76A4m2_P7BSUd7hEYLy8iUbb7ZD_1AcJ4-PzsLpWYyJyqKA19h6B2FB0k6sO5YuiGjDtuvesdbXKNrqaN3TkvZ8eql3t2Cza5ReVe4gCHhRzNOft7Z87pK5ntGLvIqc978j2H2Vpdtf90E-HjjiCcUisR0_AUqy3Od1iGY60LVxOa_tL4JV_N_F5DdZMqmB0dzRchkRwFfISMCA8Gz9RMSqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=NC-7KuRmPhDT9zOBhnWAcBjKMWnfysa7JkagdhnYjImgtfLqWeRcmmiFSbQp_7-aCmsiFl_wRw1zpt2HQR_c47iTknLHes_O6Xp3yRH3lVea5n8hv4MQYr1sEMCpQo76A4m2_P7BSUd7hEYLy8iUbb7ZD_1AcJ4-PzsLpWYyJyqKA19h6B2FB0k6sO5YuiGjDtuvesdbXKNrqaN3TkvZ8eql3t2Cza5ReVe4gCHhRzNOft7Z87pK5ntGLvIqc978j2H2Vpdtf90E-HjjiCcUisR0_AUqy3Od1iGY60LVxOa_tL4JV_N_F5DdZMqmB0dzRchkRwFfISMCA8Gz9RMSqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=rMm19K_PypMTemZod06uOOhSYocm_yv6B-90nQBV8z63MjkRYNERZqW0QZvIXYMy22J8BsvQ9a6kF7O1NQ9TTEWW6sboS9hmlrVA3B-PTwZufsW0a3dWUdwU1I8d6I4W5KAv8Gr3n2kMkvhflG4pcGYFQeWynIWNd44MC-AEd8hvgqgvRUnBLddxG9iOMu01A6Xcig0-Be17FfQEi30cjPkEKi0U2UarA3M4AFFwwzGA0KR4bmczKJcPHRbIeS_NuPu2PozffXnSJdI3aFoPkIX4cMfBtKGKYp19uDasChKuoEhMrXq3DPFQ0WGM9zK-OLp1rO8Ua5L5XzXNZGvomQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=rMm19K_PypMTemZod06uOOhSYocm_yv6B-90nQBV8z63MjkRYNERZqW0QZvIXYMy22J8BsvQ9a6kF7O1NQ9TTEWW6sboS9hmlrVA3B-PTwZufsW0a3dWUdwU1I8d6I4W5KAv8Gr3n2kMkvhflG4pcGYFQeWynIWNd44MC-AEd8hvgqgvRUnBLddxG9iOMu01A6Xcig0-Be17FfQEi30cjPkEKi0U2UarA3M4AFFwwzGA0KR4bmczKJcPHRbIeS_NuPu2PozffXnSJdI3aFoPkIX4cMfBtKGKYp19uDasChKuoEhMrXq3DPFQ0WGM9zK-OLp1rO8Ua5L5XzXNZGvomQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=mej_kwmNsFiEG0MlVGwOA69UlZ4-lP8AFBXlxCrIpi5L3yXQDWcWsUYSVypsy8g_O2BE35-fNYQRFKAazSfIy-0h7GCFlx3E50Hzl-VrzjPIlMl50fsO_Crxx-feY7H6e4nxqMz98wgYIVxooNanLB12-hgNq4yWv9YWhCmNnI6VTIrGGSnhFlCBWu7poP9Mu0Aa8Zl1sT7mQdYNO3R7K6HHQDlJo9W2Rm8TAfp4a0BYEpeFRoCI080GATsavjzR9iLcCi5a0UZHe_xCwCgMLc1R8Yiklq4UgXrabXQkL0sKsGNPlBjnKXXEIGNLtvW4fyg7N_713bZn5cA_OpBOaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=mej_kwmNsFiEG0MlVGwOA69UlZ4-lP8AFBXlxCrIpi5L3yXQDWcWsUYSVypsy8g_O2BE35-fNYQRFKAazSfIy-0h7GCFlx3E50Hzl-VrzjPIlMl50fsO_Crxx-feY7H6e4nxqMz98wgYIVxooNanLB12-hgNq4yWv9YWhCmNnI6VTIrGGSnhFlCBWu7poP9Mu0Aa8Zl1sT7mQdYNO3R7K6HHQDlJo9W2Rm8TAfp4a0BYEpeFRoCI080GATsavjzR9iLcCi5a0UZHe_xCwCgMLc1R8Yiklq4UgXrabXQkL0sKsGNPlBjnKXXEIGNLtvW4fyg7N_713bZn5cA_OpBOaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2-JTZSERcRDg-7_w9hHP4XgBHHQ9VfIGVFvH8jklaKf4YzJCzjEtZjPVwpLu_0mdBuE3yvOIPA7nC4soQRb9eelRE28j8Kbi_yLsKq4k1wXBVKdxVB5qp-_kbFkJc7wcpY7HKjICokdi2-vWlzBKqw1SgJHTXCNDT6wI8sfkb4o_3a5WTZSN2dp9gEUHpgY0JBx-io0Umy0HC50RPR-XGTFkB1UY_bDwLOnQKJgjhKhetgXbDNB_6hrJcIrahjr71MNID9cqpRbH97vT-H6JjxTO6RxRikH3JasQim3Vhe7XoO3CgLSz_iO201BogViG6TzTxOkKvmA-EFUP2zZ-A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=nP1g_E8SKxqMZDqbUUtlbxsDU89WmcXX4I9xjZgtA3S2692tsnp2tk9fBs_vK2Mt9wPqhWbMZCPumAap-mrCkTElslLmWNhNOBsDo4KjJDBV9cActf39J08yMKXjPC8N2jXqMDQu4ostx7ikf5OvjP9pgtJds083S_WlrKsgRVR4Y0kVrRT_aw0cDXXIejfpiUzQ2x2pGB9KmMiFQONPZjIMtAXtz65fqHNRGL_Ay-AjeQVd5N0X04gTb8fTJfZ2yY2LzsTcIl8rG2GIXmwe--Kxxj94GhQSUdsTOkebDSFIuUo1q3EeP_AcOMMynXePRpdXl0dVmT1DLS65wU5eiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=nP1g_E8SKxqMZDqbUUtlbxsDU89WmcXX4I9xjZgtA3S2692tsnp2tk9fBs_vK2Mt9wPqhWbMZCPumAap-mrCkTElslLmWNhNOBsDo4KjJDBV9cActf39J08yMKXjPC8N2jXqMDQu4ostx7ikf5OvjP9pgtJds083S_WlrKsgRVR4Y0kVrRT_aw0cDXXIejfpiUzQ2x2pGB9KmMiFQONPZjIMtAXtz65fqHNRGL_Ay-AjeQVd5N0X04gTb8fTJfZ2yY2LzsTcIl8rG2GIXmwe--Kxxj94GhQSUdsTOkebDSFIuUo1q3EeP_AcOMMynXePRpdXl0dVmT1DLS65wU5eiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=A7kU1M1V6qeyJr3Z8z_KWBIwifjCigcx_c-gMmoGV97H2DN0aZbL8zYxQHjVzVEBiGstW45bPlZJS6TmojXMUoB2NnFxFQt5GGpPSWxq-Qa9mTtiJ2EIB-w-_OaIv3jxZ8LbFpDBsAyVmqQv2d4adQYto01fo9wBrjE_KD0mwGO6AxuKrqtzhpjzvVhZ-xCBvsKIeKCk4BVvQpKU6CjMeTB876DtspRGMbrWj-DNGAuwQcrbnbFbJ3aKXF_XemQVDQSkezBEB_91ICNQNpED2b-_UAWTnaufUCGYa_iwf1aGlrTXiueWwWFusb47bb_lbBFtqlIirMuwuQ3pQ5ipmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=A7kU1M1V6qeyJr3Z8z_KWBIwifjCigcx_c-gMmoGV97H2DN0aZbL8zYxQHjVzVEBiGstW45bPlZJS6TmojXMUoB2NnFxFQt5GGpPSWxq-Qa9mTtiJ2EIB-w-_OaIv3jxZ8LbFpDBsAyVmqQv2d4adQYto01fo9wBrjE_KD0mwGO6AxuKrqtzhpjzvVhZ-xCBvsKIeKCk4BVvQpKU6CjMeTB876DtspRGMbrWj-DNGAuwQcrbnbFbJ3aKXF_XemQVDQSkezBEB_91ICNQNpED2b-_UAWTnaufUCGYa_iwf1aGlrTXiueWwWFusb47bb_lbBFtqlIirMuwuQ3pQ5ipmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcJP_oZ1jAttDKkE2rVBM7zY7JrNBBTNrBjKeFMzA4fVV2ecNUyrUOMbID5Zbuo8QDjNv4rDAv7iDZ-4dno_D2jS2QsVbSru0UjN9kwMpdtjspDKTtEQIK1fc0iLaCKtzrvpEiPNYlVVjyYFOrddHPaQ1vHMILNO7sw237alLgcb_Ydfj57rvfJQmVrM1tWSCQZ0WxyB18OwbVGiad3fRJ07GSJQz_EeAdaGsfyBSjTiOq_1ZNutbNEqxfxWTHLxoe2k6HeLlQdQEXDqoRl595U8rXwvDHJaNz4Qv5z4Xd1nElt-MCKilxGmBdnBoZ4vqnQ_NHFzeI0_IrCEwRAAew.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=GvrLSHoH5vlxz_57aL1Bg7ruhF0E4vb0wkGcDikLpW4Wp3IMPCMfDhlFhamLDc2RwabW6NS9leV0fHb2GO2NRNhDYNVcVFRl73pu7xQGLtN8vjro8v1alUl8RqM4exO8sZsMDt3dKHZgGYIWwb5mjrTLTgU6TBFPBPbzM6ZMxWTrvLpvKnC4wgXMKBq1meCqOArIq18ZHOWxosF11yNK2DRH7A3AZoBrHTe4qx8xTP98b29H8xXku3m_0CCq9b9E_dpNVgBtOfg7lQheveugAVoaPmSsbi0hTCabuyqaaukpjdOartdNpGm-IQmaUpqYsEYv1cjKhJlEEXmrrYaIxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=GvrLSHoH5vlxz_57aL1Bg7ruhF0E4vb0wkGcDikLpW4Wp3IMPCMfDhlFhamLDc2RwabW6NS9leV0fHb2GO2NRNhDYNVcVFRl73pu7xQGLtN8vjro8v1alUl8RqM4exO8sZsMDt3dKHZgGYIWwb5mjrTLTgU6TBFPBPbzM6ZMxWTrvLpvKnC4wgXMKBq1meCqOArIq18ZHOWxosF11yNK2DRH7A3AZoBrHTe4qx8xTP98b29H8xXku3m_0CCq9b9E_dpNVgBtOfg7lQheveugAVoaPmSsbi0hTCabuyqaaukpjdOartdNpGm-IQmaUpqYsEYv1cjKhJlEEXmrrYaIxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=UjwO9o7EhqdoMH_DCB5kmUF8QY_1cFqcXEIZOfkHxePQEwCCiUHequYzzrwNnk4O17XXu44b0VbFFXi7g7nriTShZ9HrkWqsVj4wyyPG6ys3PhCUm0xeGNlLK0qYbwAAaiivUvd4D6WFGybyP4rlFj6LZ6565qpMvol3TWYEKyGb_HYYcG6cMWacR_L7lJlhyW6yS1l0Y3hnOiwlsndLKoMvsH1qZ2EeK9CmRKhrCGn4iaCEheU7Z7DrNaC4qYuze3azyVB3-lNXGJKXKPdFyQvxT2QfMo1FXAfLeOLk8nVbeuP3YbQC1nBIUXkuANbQDSQvyRVevtmoIWOB8OEWhjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=UjwO9o7EhqdoMH_DCB5kmUF8QY_1cFqcXEIZOfkHxePQEwCCiUHequYzzrwNnk4O17XXu44b0VbFFXi7g7nriTShZ9HrkWqsVj4wyyPG6ys3PhCUm0xeGNlLK0qYbwAAaiivUvd4D6WFGybyP4rlFj6LZ6565qpMvol3TWYEKyGb_HYYcG6cMWacR_L7lJlhyW6yS1l0Y3hnOiwlsndLKoMvsH1qZ2EeK9CmRKhrCGn4iaCEheU7Z7DrNaC4qYuze3azyVB3-lNXGJKXKPdFyQvxT2QfMo1FXAfLeOLk8nVbeuP3YbQC1nBIUXkuANbQDSQvyRVevtmoIWOB8OEWhjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OHSoHIdybLD04CZy8LjH7ZxX7u8nmJI3mdBKLJKM8_bcjCTgTiEnoSPqfW5lZki8MDaTMnJoiW_1wYg1ZaZ2-feJ1drHDG_jnuOlpyjvWKZoTHqC5UR5Rs-WMknsf5Fd_rSW01BB1n42FWIFD0f2cTCs9lmZ0Ncl224JRfwAYWrUCcjfgrozi1Y5IaUJalM7culfef85yNidgGnGvF8n2fJDDi0tQhAakwxxhfb5pKGwk-mrFqGgvjGf2hyTum5cPyb_F6xp2XGDbGnl9FN1wPN9wUhlZQc7lfhxqAjGiPwJ4LWbcLvmrkhHIdr612AvKrbbT59YOAKdSPRPthzCiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lV5SFMM7VjFXFSL8AU4XTgBHXGcOPQFeJEwGexLSzIxQb6MP0eevU6Efz310aN5sH934IlLALPek66fF0f-oKmRHq3P0f31AY2X3a6amATiJXQ4zyiFwYbHXSCl8O4e_TU1-ONHSP80_OGktvhOH-Dy93z-Bxwg7SRF1SDHhADneqX7Xu67Z8CffUDR6cnDZe6ySUn-cebiH9LZwxCUczCQCYk37BKA1xE97_zRMrmAfHrTqQ5lB-5lgF6Rk42JsRAVyriyQPubBPG31KvB3Q0_xqcI4FJc65HpVqpIKVKGTvxtT3KG--9WI16gzQz0RDPcd3bmP6PEej7vDM1vzsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uQaWVFuhbuqaX55O_3Ga4sO_2Z-jmp2qp3EK1_SeVjfohxjszEqYwR82tbGyJ2pXa3Tt4LgFQAWBsGdKgzojniWPUOeOY9Jb_4EBw8lAjRPGl1A-Qf-F1Pg5PgMvEn5-Bh1-cmFeQiMOyEH-jAWuXXQTpzIePuD-mZyOf8F2iqzTwrKLeXhUgJVssyX1B0MRYB9NtnDZIsRc2IVZAoayV1kMWQjVqAR6dtG-3FoSJIkIaq5XTmshqEq5TESC6BgsP07gIc_WO-yzWT-Dird4MxQZ54n4T2_PP6E0yp3RXvEj_hDPLfVM-uRLZj8kab71zWLFijiQCuwXcsY_WG4vhw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=RBVpqMw-1O3KodhVEZvP6iCPeS_w-UTZVDD_BS_OUhC140WwWlaQQHq6yTANPPSEoJmTkWx_c0z0hLH9VabJ-gl8g70mHzOdyMxxHimSkjmUZYcqHCW6dcEWLR7oE9jxPEVapxzKAInTEQAZtKnjbfwplzmzmfZxsIZ_iTk1izq1myL7DscWfqNJQ7XeUsItjAJx4JfdUQ2BlfVOmY5iJ_cYeJmEJvNoCyo04WaloUuFloSezV3iBv48vIlLC-_hMRn3abet02hssSMd35MyVamZgVDVFtDbGDpR8p7uxyn__3muGAmpKMAh21bKfI8HaCGK3fS2Szqwno5SnR4jGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=RBVpqMw-1O3KodhVEZvP6iCPeS_w-UTZVDD_BS_OUhC140WwWlaQQHq6yTANPPSEoJmTkWx_c0z0hLH9VabJ-gl8g70mHzOdyMxxHimSkjmUZYcqHCW6dcEWLR7oE9jxPEVapxzKAInTEQAZtKnjbfwplzmzmfZxsIZ_iTk1izq1myL7DscWfqNJQ7XeUsItjAJx4JfdUQ2BlfVOmY5iJ_cYeJmEJvNoCyo04WaloUuFloSezV3iBv48vIlLC-_hMRn3abet02hssSMd35MyVamZgVDVFtDbGDpR8p7uxyn__3muGAmpKMAh21bKfI8HaCGK3fS2Szqwno5SnR4jGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaIi6dLzvbpjoS5ZW4araxYNnNqZvQGYOSoodBE3mSehBxV5nD6hoocfAnjq5iWrxcC2Ge8dnQsvWeFVYTn1BvNNgcm4eH47PJrm0R97PZPfljz_wvoa3gjeeNSt1osqD-qMJs3_XHkoDE7n34hTZn_0EdXSaevy8mtMjqearbA9JHl4vU3-jsReCvLGWV5bUPoLFAYGyFScVnW-83CN_Id0kHRhPyu1JYkrs9t3qVwlJztHOtuK9sUFJgsc9vmHTzS212A0_t6u-m6UcmbvgHkGLBwq-Ke9Ah_nvWYYKn9DGFw4mftNuG78HPhE7J0AsNOOePkskLx5l7_56uhzOaY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaIi6dLzvbpjoS5ZW4araxYNnNqZvQGYOSoodBE3mSehBxV5nD6hoocfAnjq5iWrxcC2Ge8dnQsvWeFVYTn1BvNNgcm4eH47PJrm0R97PZPfljz_wvoa3gjeeNSt1osqD-qMJs3_XHkoDE7n34hTZn_0EdXSaevy8mtMjqearbA9JHl4vU3-jsReCvLGWV5bUPoLFAYGyFScVnW-83CN_Id0kHRhPyu1JYkrs9t3qVwlJztHOtuK9sUFJgsc9vmHTzS212A0_t6u-m6UcmbvgHkGLBwq-Ke9Ah_nvWYYKn9DGFw4mftNuG78HPhE7J0AsNOOePkskLx5l7_56uhzOaY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=FNTzu2d4Xcr2Ohce9wyb-6Hqmo1ay746Yv_mqhlW2Q_l-E6ki9ukft7Zb3b4p3h02lgGrgXGWvLzgyPInbthdBgS6dgqOdghZTi4fA7RudXj2Q0UFjDRZZdTymhokO-5l8XHBHETRvHnurtquulIDeOlh_l2bzI4J3vXafyTrtK1h6FkeB2UR9CqC1pYdq3NN5VYDMNnlhhRfX_KlYjBj0G6oW9C41s-IvztYsvZcBn5e7aIjXNWJ0Nzz0_WfoGF04cbsgza7XzfWep31OJIMSfBhoBwRnmDEUdHhf2sJYUSUVayC6Kwzo6QsepvrWDCkZQfwpUT6R9GEjZwZ7Nk2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=FNTzu2d4Xcr2Ohce9wyb-6Hqmo1ay746Yv_mqhlW2Q_l-E6ki9ukft7Zb3b4p3h02lgGrgXGWvLzgyPInbthdBgS6dgqOdghZTi4fA7RudXj2Q0UFjDRZZdTymhokO-5l8XHBHETRvHnurtquulIDeOlh_l2bzI4J3vXafyTrtK1h6FkeB2UR9CqC1pYdq3NN5VYDMNnlhhRfX_KlYjBj0G6oW9C41s-IvztYsvZcBn5e7aIjXNWJ0Nzz0_WfoGF04cbsgza7XzfWep31OJIMSfBhoBwRnmDEUdHhf2sJYUSUVayC6Kwzo6QsepvrWDCkZQfwpUT6R9GEjZwZ7Nk2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHGtRxaxa-UZqpMvhoBAzqzcPZeh_7QDcWOVIAeV7o-3hPpXJjtGVrQKwiwU6c2Q8ib0b1gmvCcFKcr6Kz6_gMScfozbiwDEKLch3ECKPgAMyrifjjY6uHMXjFWyHt6lRyEWK6Ct_F_2bxjWC72Hvrps_d8fR6KLSPN-QMok5FeAxOL28n1bLkFWHKbOC4I523YmoSr8YKvWGiyEDOy-tW7EgLUsomZnGWEi-QT7tdc7-e0yV3z9p1iDlJClX-Q-wH1NNwJcIlIePQyx7MAozUbd3DJB7I07XUpIN1AivjvHabv1fToLlrOG4r_DEW4v8_DE3LMaKYadUSrtwQ3Xjg.jpg" alt="photo" loading="lazy"/></div>
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
