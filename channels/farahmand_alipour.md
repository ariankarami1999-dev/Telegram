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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 17:44:29</div>
<hr>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5869">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5868">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5867">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اگه توی یکی از کوچه خیابون‌های ایران
شنیدی  «خدا بیامرز» یا «خدا لعنتشون کنه»
حتی بدون اینکه اول
و آخر جمله رو هم شنیده باشی،
می‌دونی درباره کی دارند حرف میزنن!
و همین خودش خیلی چیزها رو
نشون میده.</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5865">
<div class="tg-post-header">📌 پیام #95</div>
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
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5864">
<div class="tg-post-header">📌 پیام #94</div>
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
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5863">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfJcmnNIrdROT93jUDFe16HicYX-kbjTEaLzBUWy0R_QbLUNh4PJliyZ4kXErbfaW-VIqicmP0PHKHP6TE_n-1dccalJvzeBTt44asoXAA0sglWaxMwPvYqZQADAoFp_vcWiaDlsnNoIg62hiDFY0FaYAL9-ESZ3Mzi-cl_lWXJMjZNSdJ7lLY9-63GFakJM-7xIPFdMgf4f4sCUplmCe5hs3I2pBK9pzBBtqWHWFh7Hdhopa6Vqe28JYG4Vnn0tABb71hDEogzns-JqNQuheogk7yxSVCHcaOlzH0oyXL-LabxJnReayoynf1qlZV5kxlZIyv0h9gLKmCeXQkO9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=M5cLA2QwTt9U1k-o98Jp1H5_DmJna36gGGqv2f215Y3zu9JX1Qmi_5Ov8ff8oP4IAwN4rZvu0xCBJc8Uyvp8mqDlliccgW7HNet6dwyo8b0atX_B0UcoDpR-yOS_RxvtVpk5exrzHRwwIuUMWctuJH0S96r2GmYHTnzggMjHxMPqJQW743XlgI60p_Q8eFi2Q2vtrUyp--z0YzlQBX5fsc7EHGzGo5iLVVpqxRKcbdTFu8hefP_YolE25kRnFBRzulkQSEWHYQWp28pmUVdZICHlgxJntZQhfUmL2obv09U_mkFsaJyFwE__GnuQ8Zw7kzegIp5ZPVK7FCESUsMi5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=M5cLA2QwTt9U1k-o98Jp1H5_DmJna36gGGqv2f215Y3zu9JX1Qmi_5Ov8ff8oP4IAwN4rZvu0xCBJc8Uyvp8mqDlliccgW7HNet6dwyo8b0atX_B0UcoDpR-yOS_RxvtVpk5exrzHRwwIuUMWctuJH0S96r2GmYHTnzggMjHxMPqJQW743XlgI60p_Q8eFi2Q2vtrUyp--z0YzlQBX5fsc7EHGzGo5iLVVpqxRKcbdTFu8hefP_YolE25kRnFBRzulkQSEWHYQWp28pmUVdZICHlgxJntZQhfUmL2obv09U_mkFsaJyFwE__GnuQ8Zw7kzegIp5ZPVK7FCESUsMi5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYJRFQvhISI1GvZf9xKq5SrjG7wMbgQR5njcALOEFcufvNAZyMgPf7bQX-5DPVJc5fPWMh-MqzAr2kY3Wjo1_wkwlHvXjoYJ0NfvGIUVxob2HT4E9pSCPafP5YZse0stTFhK0F8cu6bD4wLIBWgt_BUTLTNqNebTxB_0rOFlZYLCOC4jXL2FiaCKM6gGqUYnWdXd_9ihWpv3XgcjKwC3blpO2B-Ra-oNkbGLiMA8jl5xhnSY_h5ysVM4ufC8OPQvfa2o6GiNnpEDPWDBrx72cbeO4Pu7c16DKZY_rWRMwyQfLP2yGOoXcFcWjpFPGfhqYySc115PoPUYiYmfAvDoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU5FQmIvF1wom64UWca7ZKlfD3k7B-pAmTGzBM2FqD-QgEoBo5ERh0H97GkSRKsypX7w9_F0sUnhuzOMsK8DJk4ZwAr5FBm1qFtX03BsFGNOXC4UDRhxQPtBVbHE11Dt3Ky48awdGBbg6YEZTKjdEhbWbdVTkbRf7uoJQtIdv8W7fwwsMjyYznlf7iCsKBSK0uS-niMfX5184niHj86-1D46Oxp6IZVVOv5K5weK9gpt8lY9qzfanSg_FWebNrAFEo7M1AdMV7hbnv03J6gAUxu7Y9i_G5fBMEjy_r3KgFYLA70LN2oAhj1i7wxJ8t7hfjHRo2guYUK1T1YzJQmkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFAKKtADXspnczadcDCULO632uV3rT8mVGpdjj6p4tdnPDgz6HhiFgL8Ow-ZfFk437V9BfRkkmKOaXv0GVYlpArZya6tuxkmnrBvIsSFSfVlnYZuKHYk-4TqkxD0YYUwCIZ7o6TghImmMdkYt_plAAX4rTIDMSdVLZuBT2WrEq-2jIGCPv0vNbPDl45z91rlZLuhKaMwk4o-a8ZGGASFClgVNXF-XsPDVPck-T4CbmZDjG95M11LcH1DrFyqKd7vCtb34jtHx8Iy45i4JCMK2neWAWCwsG8_U8xQnlPwSA8j09mKDLqjmSl1OYJfFRwrxR7lNMn_NSc7_DtMkLeFcw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eACiTeoJ6pispGlVlFeJURWF7u7rg-FfEDUE9aVcLbJ7HkQiC0y3TC5OVtjL-tc5xdsBB6h241sjr1iyKJ48NWDVWEInox09uTLUM6g9wuLZ_q-KNqvju7aMPJyHc0uDQ4Mnh_9AGVjGZqVACwp4iBexkfQrxqb497BtodYnC0zZw-9f_uJkYyZD0PWBy3UMUn7AlLlNjhPdA72WlCH1MkoGFc-46U1oB08SfQjpcxIbxMIZRURqLGoBpQS3YLu7VgUv42_NaWZm3z8sT7oo0Vhvnut8sQ_WQdXmXQBgifpzF-MbcUveKFRr3DlmUaie6o3ABjHyBccLhLdQukJi4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=PaJG4DPR0zRxiSh4ZaPr87oA2RJhylSx2vgO6ga44F2SDTtrXxVyb0WDdI40zhEalfrQo_BopbotZd6UZu7QPaCBNNaltE1QA1H5hjwZ-1LLhaZxgUICfdzpefdSJ1i77X6BiwcXMW0hLXziMJsWLibmfP2U-7OQkqBvLrTICW8NpxQfSRUcTKSykU9FyVtlXwN8MJ4AlyShYuJlDWpELe9qtL6G-fxhVXM-4NBpmp1FukV9LynLUwS34zep23F6wNE-8ADa-bM8wpWyAgh2Njh946NpFXEsE1TZtuZT3snTl6884wtt5OLzGUYQl5iXmIVPMAyRd10ReUYshtCmYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=PaJG4DPR0zRxiSh4ZaPr87oA2RJhylSx2vgO6ga44F2SDTtrXxVyb0WDdI40zhEalfrQo_BopbotZd6UZu7QPaCBNNaltE1QA1H5hjwZ-1LLhaZxgUICfdzpefdSJ1i77X6BiwcXMW0hLXziMJsWLibmfP2U-7OQkqBvLrTICW8NpxQfSRUcTKSykU9FyVtlXwN8MJ4AlyShYuJlDWpELe9qtL6G-fxhVXM-4NBpmp1FukV9LynLUwS34zep23F6wNE-8ADa-bM8wpWyAgh2Njh946NpFXEsE1TZtuZT3snTl6884wtt5OLzGUYQl5iXmIVPMAyRd10ReUYshtCmYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=PzdVchPHDyUJZKo3cn7ztLI0y_IZnb4d1S4u2F5HZeCY1_e7K3A8DNyq3AkhZxALTN3jsIMbLE9uX8lR9phLO5fbwP4f7zX0doj4nyMzMuzGfnScTnwNBFZyvCE-XYItegHEVbrqXh0u3AK6PUX2u3wEjoMz7P8JZ1z3WJ_Dt_Y7H9TvgpzhKZTQVkzSCkOKh5GTpZH3q3YuEsIKrszOodppjcxps6nGDDuE7kZhxK48ZaHOvRJslxMs_gQmtFuXebqUULsv9ZGOORupkUan1ylZjn54I4fsoosGmSQD9Lvm5_9bhahBFcUetLuqQ0BMisodrfxI9lNfjte5j10fHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=PzdVchPHDyUJZKo3cn7ztLI0y_IZnb4d1S4u2F5HZeCY1_e7K3A8DNyq3AkhZxALTN3jsIMbLE9uX8lR9phLO5fbwP4f7zX0doj4nyMzMuzGfnScTnwNBFZyvCE-XYItegHEVbrqXh0u3AK6PUX2u3wEjoMz7P8JZ1z3WJ_Dt_Y7H9TvgpzhKZTQVkzSCkOKh5GTpZH3q3YuEsIKrszOodppjcxps6nGDDuE7kZhxK48ZaHOvRJslxMs_gQmtFuXebqUULsv9ZGOORupkUan1ylZjn54I4fsoosGmSQD9Lvm5_9bhahBFcUetLuqQ0BMisodrfxI9lNfjte5j10fHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=bxKIW7WlUpTdnGi0qKa8akIuRr1C5wwXW2C5OhpCN6Ws1r6P-zIjTI4Sndbmuq7hJ-jIKKrFh35L5kBxf_3iXu_Q0TlPbSWhF206QvhZuF5LvXWZfuemIEp_NNC9FnyYiFW8snCkiH5lkHNunk1XWz_AEvNj9P64rrYfwWtklu8kEg-LAlqq4YlC8urzmEb6He8Nf3g2uyCAguElzV8NmTRc3VITDeZbaW_jUaZhUBZCNDWZ2gembz4jSL9Bf2tZA8cnZoVoLmMGdT2kkePMCq_9cJiqyBnvKp5EL30J2YIMAqoCF4f9xzI3b2wYj1sQTBI57zIogSFh-boTozXAow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=bxKIW7WlUpTdnGi0qKa8akIuRr1C5wwXW2C5OhpCN6Ws1r6P-zIjTI4Sndbmuq7hJ-jIKKrFh35L5kBxf_3iXu_Q0TlPbSWhF206QvhZuF5LvXWZfuemIEp_NNC9FnyYiFW8snCkiH5lkHNunk1XWz_AEvNj9P64rrYfwWtklu8kEg-LAlqq4YlC8urzmEb6He8Nf3g2uyCAguElzV8NmTRc3VITDeZbaW_jUaZhUBZCNDWZ2gembz4jSL9Bf2tZA8cnZoVoLmMGdT2kkePMCq_9cJiqyBnvKp5EL30J2YIMAqoCF4f9xzI3b2wYj1sQTBI57zIogSFh-boTozXAow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=gkQG3AjusXG2V1YLTQIIefzLn4B-DbyxmzHhToeWvIRF7zJftSSXj8iEA3fXZNnts-JAjx3WOEsxVE850_Exfc5mteu_8boJ_46oG6gnzPdbu6heDPcSqhNVa4tp4WXqbyvKngzBYGkFSsk2geqPR4REGeVC1-q0J7hmeu2bOQf0juZEhKrSHcYiqZoj72hMjGuzNfHBxKnG42nLJRNQhlJNCWOt-0NSPN-YXlsSUN0WSTnv-NDsMDzh-lUNQRph8APjUw04pRP7hjZjk2AcOaae1ZRafPpb662bFYwCTUD1FyHu0R3wyIfELpt6SFfidORNGMTNHOr458YADjs0mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=gkQG3AjusXG2V1YLTQIIefzLn4B-DbyxmzHhToeWvIRF7zJftSSXj8iEA3fXZNnts-JAjx3WOEsxVE850_Exfc5mteu_8boJ_46oG6gnzPdbu6heDPcSqhNVa4tp4WXqbyvKngzBYGkFSsk2geqPR4REGeVC1-q0J7hmeu2bOQf0juZEhKrSHcYiqZoj72hMjGuzNfHBxKnG42nLJRNQhlJNCWOt-0NSPN-YXlsSUN0WSTnv-NDsMDzh-lUNQRph8APjUw04pRP7hjZjk2AcOaae1ZRafPpb662bFYwCTUD1FyHu0R3wyIfELpt6SFfidORNGMTNHOr458YADjs0mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=pGNUvrIQkFKEXkmWLqaZ4Q1CFjjpKhizPVuoiDFNrY1Uin1W-7X8GQBgWtAFnczmLMNqJS7LaT8UXKqiREdqEgIFeB8lFdw7-R9-nMTozR-vASeEmXV7YzxLdOptfKwxPfsN6FPc29tOsED1MKneaaTSGi-b9U8prTsiiuyPdwMt0oJ5Ble2ExN_OD4Glr0Hk4muC1R0fhH3CdHqYMmaK2-oI7FFutyOaNDZT-WDGysUsZ5bydngDPpwcSI9RyMsIbyR3QKE90ZOToiZAg73YCojBBMVnVaXFjorDZSi-mOcxU7yd0ry0lF-1AYG4Oae6OalxQ1R9VKkcJxiZ7qwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=pGNUvrIQkFKEXkmWLqaZ4Q1CFjjpKhizPVuoiDFNrY1Uin1W-7X8GQBgWtAFnczmLMNqJS7LaT8UXKqiREdqEgIFeB8lFdw7-R9-nMTozR-vASeEmXV7YzxLdOptfKwxPfsN6FPc29tOsED1MKneaaTSGi-b9U8prTsiiuyPdwMt0oJ5Ble2ExN_OD4Glr0Hk4muC1R0fhH3CdHqYMmaK2-oI7FFutyOaNDZT-WDGysUsZ5bydngDPpwcSI9RyMsIbyR3QKE90ZOToiZAg73YCojBBMVnVaXFjorDZSi-mOcxU7yd0ry0lF-1AYG4Oae6OalxQ1R9VKkcJxiZ7qwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=StIRwtmnzkIKsKKR_IEHbSizo0skVqA0qm0VpLVF6npG5NgtTnjCfsARZIW6mLRjVM-jx49PkjLOqSO0TwNN-quxERSIv7Nn_f2TcHa9HHHNQ4aPV80DOhn5N9VGw3g9aH4M5FBiPcNm1JnyaTLGUUFjZgoxrbdnrMeI89eaMrpQBRfzG_VKxMlNvdgzLS7hp-ZeExv00dIdeiFVjTefTn5SUdffMwkb0c2tuvhpHDoYcRY2hSP1GnXuxCUkgfRGocnbd7np6Y-va8noSEK_uY6C4QZyOFnDibpFbiYExzGiIU7XDLbXzmtWAyk9fQYkV4vhJI0xVdlngMH3_FMKTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=StIRwtmnzkIKsKKR_IEHbSizo0skVqA0qm0VpLVF6npG5NgtTnjCfsARZIW6mLRjVM-jx49PkjLOqSO0TwNN-quxERSIv7Nn_f2TcHa9HHHNQ4aPV80DOhn5N9VGw3g9aH4M5FBiPcNm1JnyaTLGUUFjZgoxrbdnrMeI89eaMrpQBRfzG_VKxMlNvdgzLS7hp-ZeExv00dIdeiFVjTefTn5SUdffMwkb0c2tuvhpHDoYcRY2hSP1GnXuxCUkgfRGocnbd7np6Y-va8noSEK_uY6C4QZyOFnDibpFbiYExzGiIU7XDLbXzmtWAyk9fQYkV4vhJI0xVdlngMH3_FMKTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw20r2MJgFdgWUxXTeKd9cBc7pWI3kjvhp-uUD3lOOIzizYYfg0hcTMMQokTSVOM0uaoPY6SHYksxs-cEDZE5OPKBv5SiHqIA4969LimtsL6T5RKs13QpSFoioUSG9HBQXzUA_jnzcKSaqji-tbQAaiaEcn3jIpbUsiLi7WF7FAQpspQ8fAsUJqoQpXbrW0keH5cYKH8uzcemK5F1fxNHqptF6w_GnbWBKpL7hVHHhLT8Z1u9PguIE_0J3MdHTc-6B80uo9FdiTSBnalWyRS-Jw0LZZ5NfQMWkQM01leJFgQTSHDDnNdE7xlfyev-upUfxa-WSc7m_2rBatP_z6QDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=D5sZjA4LjhRHjL4mncfFFx-H_5RHZnT5oDJjgZQ5-EgcdAuaaDpCNUoiHYKLofLBdB4WHctpv1C-8utzmqHCFc7FglIdczBgruRehZvC_4g4ENKOMlIVtO3uwPC7TS5uGJOyYvkJjvjqdaugqm53gF86Ng-FH6rgWtbqvBE-4Qk3l_zuAOcIHJ13eSnrta6qj7V8PZk4AKBC2kJs1KxgA6uF6PZ71bCKZQA_pS_KGysu2ZZZhZ72AClAVx1MsWI9hBVSPrRucZLlmxRkykiZCXCfe-DZtXN6gZyGBF0sjwnlEs90Z08ClVSzUHQXDOhkkVRT6T0GUU3GRD6lUQBXcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=D5sZjA4LjhRHjL4mncfFFx-H_5RHZnT5oDJjgZQ5-EgcdAuaaDpCNUoiHYKLofLBdB4WHctpv1C-8utzmqHCFc7FglIdczBgruRehZvC_4g4ENKOMlIVtO3uwPC7TS5uGJOyYvkJjvjqdaugqm53gF86Ng-FH6rgWtbqvBE-4Qk3l_zuAOcIHJ13eSnrta6qj7V8PZk4AKBC2kJs1KxgA6uF6PZ71bCKZQA_pS_KGysu2ZZZhZ72AClAVx1MsWI9hBVSPrRucZLlmxRkykiZCXCfe-DZtXN6gZyGBF0sjwnlEs90Z08ClVSzUHQXDOhkkVRT6T0GUU3GRD6lUQBXcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=KsQMT-akanwpRHsAv8N2cDg7fcgNrwrMNPFM2lelKkbz82eBs9kwDemM19m7tNSRIJ9MvjbvgqT4Gj5qKTTYppZgiEFVqwtxBfmQiqd-33XYFohTCnkjoISW3gEc6PAm0XXANimEqIdEfFSviuQ49thL0SZbACih-97PMm3MkoiN1mWv1CG3RtijEAsWeNc1tCXb67os29PNch8hC2actQ3Yj1aB0f5h3B1akqrhEfD2vUf0hSEjvf5uwLAcYZXkDuEQ3q3B6RUbHKiiARrNfuNJnt_ZcVuo7IP6ZmKU-GzPivbsSQjPFSdFv4MZYe43n0PZTcnrb3d0lXoTU1rhkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=KsQMT-akanwpRHsAv8N2cDg7fcgNrwrMNPFM2lelKkbz82eBs9kwDemM19m7tNSRIJ9MvjbvgqT4Gj5qKTTYppZgiEFVqwtxBfmQiqd-33XYFohTCnkjoISW3gEc6PAm0XXANimEqIdEfFSviuQ49thL0SZbACih-97PMm3MkoiN1mWv1CG3RtijEAsWeNc1tCXb67os29PNch8hC2actQ3Yj1aB0f5h3B1akqrhEfD2vUf0hSEjvf5uwLAcYZXkDuEQ3q3B6RUbHKiiARrNfuNJnt_ZcVuo7IP6ZmKU-GzPivbsSQjPFSdFv4MZYe43n0PZTcnrb3d0lXoTU1rhkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZXcVPDlIljbdce2qtRXJhIpHXa7FA2C8UgXQnIT_iKDBz3AuRpGC2gaJzA4tZ8fFAjBp_7dA-_Lb7WtkjR3L4D7pXJOsj29zDoJS9yM-323TlFDtYhIpJkPgi98dFaWvsvgBAVguE-jGPwUYhweiB7jT68_m0pE08MCGS1I2Bri35zBqzXWCe3GI5Wy87l-d1SV72jXHsFtMYxK8P6LGp1oMk59eIMa1JCkfEb4FBGdEdDH5JNB5WZv5USPkKoGQiz31zI8AGql1EODWnKgTOMqOvlaqRQGlVf5jSGjGA1BDTPF-kIygshUqDxMhuIM0xJg1joo4UK1EvmycEim7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lPBAQ3yfGyoG3etQXskc1ygubvsbhnauqKq7x5U2zBHLxstKnIJJqNMbly3QDCZrT6O2EOFn3bKF4_At1QyW2WCLKfc0-txGrocG3tTsv-Dc383JYtB8qpINDRp0eE0_bD1sf-V5a55UiGqU7zIFr3TtoIi_pLmya-fsUU3_0DBDNYIZrDtGwrNjmcojzrsZLgKxCx6l9K-hJIQy_gCYRiZVOkg_8cB8GfqdaySWh9zBNYTQJF5ZhoEWPnWuN4I6VC1S5_ivIJrfF-moAJLZ8CjCtT2PeLWwEhlf86fBY-l3DKu4kVSLXgs0G0kdxvZD45BNcF8oTw1jWbx2G3LseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCnXkMQ-TPaCYFEZi5DQX1d0oCqJ3GsupQKF_eyX-OQvN6WbPjA2BxpuM9JQFTdmgoG_69VQY99EdRhDcBoN-Q2ehIldmZ3cwW5p71DH3fCT5MyyskIchUCh2EQp6ffP5DgKJCmQs2xZXRi30HebqcKAvA2sMIBSLHwwUKwDFYUHJMKdvYpSfvFH-1Dt0ktNBGGfzCBw7lyGynBgRJgKfxS7zQlt0PPYKFkQWRHotiOCSdGDj5EWFqhK0nVgjsJvTOiolKXGHlQUJy5hkqseZFQIwTtlKnCq98j9nDYvTAiYdBsoqFIQOykYWrAJ8awW2Cs8sESqstR5od4z0ZD80A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UkVA3_lKoot4PraYo2kavmaJn6wmwhIChmbF71p5aZQnQzRyYxjm5xU-pI3Kzr2ODZnWYwq7hhdfh4wvT7hmouIWsiH4yKKvaEdFM2JzbiwiME33vcE1VcDQAPlzxr82b4_y6sw7w4ICUWOxb4kxnY1asQ4fMcO7glPXi2VlNTAig9L7j1MZblaE-N9_xvqkOekPz6qi1yPWI3W19Kj3G6ZY92W7GbEzL2QWPdlBTivEV4DMJ2u91P5itFWfr0EvjwDEAvW28QMI4UgvWCzCc5MbXB3AhSNIYtBAlixOYUNiCu_1MBVdCibcMr_OlBkDEl59Sd-AkXUf0ui5YJ63lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LUXjt9oGVqElhHTzW5cokDKKjFS_Q9RYU6IVSrxZZ2r7f_3AxnFn2FdXFf5L3pvSmWsOwvfLa_w56GIiApmis85bM6nEmGRvlC7R9C7UGjWl74L44Fb2V1Jyzr4_k1iLX1ub-pATW1yKRdJr-51y2EBKLEI-CTv6TTzps9VIQhLwxRJcVdW_MnXJq8NYyzksCBDutXbXBJoagvrmpMHYk7yfbP8srQz6FkthezFe2O5mrtnHMjBQd8Z41GxhXS1zvUQ1Fe0uu5ievcvsIhyTBSyMnmcDWQr4LskuVwH7WZc9wgghFhGlJ6tS8Lu1x3KfvwfG6Ff9nKj6J5bGx35sGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gY2pRMiXDNicMVU73Nk5MLGvmfh_2vUODmQt036uS5H9MzdLJVRWR6ecuM2wz1TY9sSSNonSuwklONgniIaivh4M3ARzCA7p-qDhLf_7ULimssBP2SwvCUnhXXG7-ehXILCBBrDyq_zZzTy3oApHjhPz8WvQQE8shew0TpoCXQeo8qSYaekzQwhNO3pcCNO6BQKkhLtRI3qC-cTyoh4z7-LLaVCoTRnoaRtUA4bmEr-w7hSGxlpet0QUCkvxtOdAyXI96Hw4gj--w7PD4zuG8eWMJ3MP8VOS9EhZonO_8hfF1Q0HccQiEU6xAH5yDbCiwL6L3BVd48TbHQlgxcbPsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzV-MFKdwFqkY5IXNxfdwpxBRkvwZi1R8jq1KUN4tFvgzynpBtxkVdNEn1FupAGPegyHWYc1RchQ6iDT8dHCLP38fSOo_ertV49um-TPWruHfSfO2VW_DqkqZ2V1MgNsb_3duU619mRfqGT-xG1LV6n73yM1QZZmSktjVMeM6fSRnwdKC9DuoPmg0dNIZubnc3H7O5IHl4iraRVEBFrE2H3JlduEA5r8VgmgjUAXe1BSeQrcNsAn2xxymB3oNuPxQPxxxdyiSaDplW0wAXfwribmuarb2ADtx_vfoMt53hvdQtLUR8h8hmo-dOes9tRzNp8dnut0Ci4Vou1ewi10fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQ6RZ8huji5vGeE9c_HlrbnoDqSKlKpb4GP8JFSvg6OzZrQGQIYYkGvD57x_sNkktvD5ZhumkJIwDzDKRqrhJGPz9nSpxFxy4l0dOyjw5CIsUKqCDszuZUDDzsnvLIHWgbFuAljaRND5VRNr9Tx4Ph55ScINYZMlxB49i3gECPDoRM3dbqK-W2Aw3js7ADn8deP5vIcYjWoPLHsa1JLhKZrSm2Uq8dfhpoe6hj0slQ8kzwOppeiD320YtHKMeQ_yKE4Aq5xzHxpGsVo7mG2nFxWS-IfhJ2Htig_D799TOLTyBtf7Qm9EKucifp5A_Z_hFCvglYgwL6Uh0ZmSxIqhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgozcA1VncYdWiQtC1SpHozlQdtvOANaHigSYDkaogJQa796DYPexE7YZBoZXIohlPkJxCNyLMQYVadBnbnSmLUGCOIHNLGfEg3gJ6tEeEEl6gOd9QYDP7aFb89dL5_4ClGBpVdE7cWNcdzDNKjFv-ffzckJ5dFWKqYn9AU1uwLmQb_zb9PdHNZxqsjMswFdHgDe4850eJdC64h0h2pL30CxTAnzKXNW4pDjjLa8xsDIrRwauWVbl2I951FBzZCNRFRwUQnl4bx1PmoaO0KpxVLUn3Wp0an1PBUYq-Oomj7_yKODq3NDpOE_bcHb1WXMuKqmIW25Xvcyo54vXDrIKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBWsp7CqeQQ-SzKWoO0FYlLVC6KOCfMiOGwEFVHG2o2597zKuVAK4KVzMwiih6_4t5f1kP2ZH7Wq4Jz6fXVrlU2Elgil7pVJ765NOlEH1b4O4S09wzAHt2WpAOrnuAlURg0JVxjBG0QDn7N3n9zf-Ka7fYZBpXgdjV26W6oTTGxKIG-Ku4-r85tVmGjY5i8UX9Q22XlZkIWhykOfjL04X3-3qo716i6hU6OsIiRmWU3NBC0_CRoIkNX-a7MKNei2or1jLkLAoRV7RXr703XnKfmdnXjslUDB6TUufvAT4wOrC8_8ztMRohowb8nYqDRBNf8Qw4SqQlS24MdkzOdHNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ4o3zRCDEyY6bLiyCN0Dg517SdkT4NRn9GeYFYkolBS6KNVKqJLbwTmNX9dfVLcJXEQisH8xRlLB6FMlMUov18PJf98hgdBDnZU1ExhK_TofxUfa0kvz7lQmFjw4K5v1Tt4aGDTK9DI4kh5bhYUB6mY1bAHUf_XM29zZyKhrNfqh2xRWykUjzJPFobL7nXLyS56XymqOraDWCEO0ekplbTz_eKekTua2jkx2u30R_UBZ8Fxewj_Ygl9hVJSyuerC1CZwXWJ62wBCZt230Ao7u4DExrJRjbQ4roSKdEZWQRN0iY2SvzmeotmfmWW1LgatOmGO-QJPnc0gmh7FUoH2w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=eLD0CwEb5Tk4LWV4kD4EJI4Y6DwBpCSz9oyrlefWRRlQfrMoZRK1SNTCS4NXMtOdXxMlA2NBhwvGgeaC-ZfT7nB4LqPiN602GehB-GIzozJKhpJu-DCQWHb082I76uBD96KZxcCjjTh1WLXRwUIP8Dg8gwbfRijrm2-ssKwvuiVAAap8TxdQRMtbOMwE5_KxA8fU6mFRWEnNCj8vd9BD4t5gBJLWCFy3IhTKPLQwAu8b20foT9uopWBfvotvf7Ara79oLGuuuOjRH8OAbF7LH3GusfVU0fYqaFH4p28dQiTBlGUM5DaUyUhxT_M7PZRlk5pAHQfbnHhamYjw_6fHew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=eLD0CwEb5Tk4LWV4kD4EJI4Y6DwBpCSz9oyrlefWRRlQfrMoZRK1SNTCS4NXMtOdXxMlA2NBhwvGgeaC-ZfT7nB4LqPiN602GehB-GIzozJKhpJu-DCQWHb082I76uBD96KZxcCjjTh1WLXRwUIP8Dg8gwbfRijrm2-ssKwvuiVAAap8TxdQRMtbOMwE5_KxA8fU6mFRWEnNCj8vd9BD4t5gBJLWCFy3IhTKPLQwAu8b20foT9uopWBfvotvf7Ara79oLGuuuOjRH8OAbF7LH3GusfVU0fYqaFH4p28dQiTBlGUM5DaUyUhxT_M7PZRlk5pAHQfbnHhamYjw_6fHew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=EK0glxjuqrvsoywJ6O2_tmSQUGhh1ena3MvY73qG5HW4XXw9zqXN4wNoln36jG65pugMKVG0rUcSD3losNLCv8rfXMebxWwvALNVDgj7hWnHBBIb2Dn8rKv6II493VrX0FYb8dEfYsxJTX4jg_6a8zO4OWEoYu53MSf-1n732gQplYkJ6YrJcp-C4R9Bg4J02KgQcwtyE24p3XG_7xfIQe-rNmfoVMq3IAazzc1apOXzK18A9OoiLwLUEcMLL3xzoVU2I2BucyfZ5BKpwLZ4eaRfUy_KE0L5vEddncybWA_boxonCiNzAer_BKLe26kDTSQV8WZzpzV559M90e9riQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=EK0glxjuqrvsoywJ6O2_tmSQUGhh1ena3MvY73qG5HW4XXw9zqXN4wNoln36jG65pugMKVG0rUcSD3losNLCv8rfXMebxWwvALNVDgj7hWnHBBIb2Dn8rKv6II493VrX0FYb8dEfYsxJTX4jg_6a8zO4OWEoYu53MSf-1n732gQplYkJ6YrJcp-C4R9Bg4J02KgQcwtyE24p3XG_7xfIQe-rNmfoVMq3IAazzc1apOXzK18A9OoiLwLUEcMLL3xzoVU2I2BucyfZ5BKpwLZ4eaRfUy_KE0L5vEddncybWA_boxonCiNzAer_BKLe26kDTSQV8WZzpzV559M90e9riQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=jvnf9taJKsizydy4PZPj72tWUpVAAzM-037-QJPtVFw4yfUaV9vfXmxDkuTQoU3uefKhIBsVCXCLAix0ESjqkGVsW5ZcTW8V5UtAmzxe6MEGVc0wxfQc3w-q4GRyek0LMDKfqLOObuYIhjr9Tsq4bvN-7l9k8gdRnLp5JMzo4kL7jFnLPI39ZJo9KrS8rq6GxBr83E8Vnc7226U23souKH7bf-ThjfNCoDxGd8iWDpez5g2t00tkrnLr-TiO9wE-QT2yXnKg3WtUxyve2sRf2GeC53k2gl9KylSHBUKqDJyow3Ar2kcj9_EOAEYIbC3tqs1N2VKmZdaXwZ1BLXcwpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=jvnf9taJKsizydy4PZPj72tWUpVAAzM-037-QJPtVFw4yfUaV9vfXmxDkuTQoU3uefKhIBsVCXCLAix0ESjqkGVsW5ZcTW8V5UtAmzxe6MEGVc0wxfQc3w-q4GRyek0LMDKfqLOObuYIhjr9Tsq4bvN-7l9k8gdRnLp5JMzo4kL7jFnLPI39ZJo9KrS8rq6GxBr83E8Vnc7226U23souKH7bf-ThjfNCoDxGd8iWDpez5g2t00tkrnLr-TiO9wE-QT2yXnKg3WtUxyve2sRf2GeC53k2gl9KylSHBUKqDJyow3Ar2kcj9_EOAEYIbC3tqs1N2VKmZdaXwZ1BLXcwpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=a96WnlRM3GjTbqSxvefIXEOwHzj5Wkwygv3dhUUHPRoNAihv29Umq_baClqcyCanz1lFRnqa0Jby731KXoVCPVt7emm4rW1hmeUmWJKmN3bmxDSyrdiXoOJk0P32JxXj2KgQaypSM5q-DqYl_ejWHI0XCJU1TxEBwyu7UTQ64l8DKzwcHvvSAA4ySgelNFF5groUyEeHWPd-PRJ_BKubDQQ0M_iz4rD6lXX6jWJYyVGqxbCPAslMqqb5FLrRktNXkUhZ1Fi0re6ACaeQmOrWheKYiUkp_Fn8lulftCI8-g-Hr0zKDH2_4i4gWYppc_HmxMEt79dG4--cqzrKfCgnNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=a96WnlRM3GjTbqSxvefIXEOwHzj5Wkwygv3dhUUHPRoNAihv29Umq_baClqcyCanz1lFRnqa0Jby731KXoVCPVt7emm4rW1hmeUmWJKmN3bmxDSyrdiXoOJk0P32JxXj2KgQaypSM5q-DqYl_ejWHI0XCJU1TxEBwyu7UTQ64l8DKzwcHvvSAA4ySgelNFF5groUyEeHWPd-PRJ_BKubDQQ0M_iz4rD6lXX6jWJYyVGqxbCPAslMqqb5FLrRktNXkUhZ1Fi0re6ACaeQmOrWheKYiUkp_Fn8lulftCI8-g-Hr0zKDH2_4i4gWYppc_HmxMEt79dG4--cqzrKfCgnNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=DNdekk4ZprRRokGhAdJMIAzDhpKCbSpfCbSBMZ-c4bJAOpvSmGmn1FFSWUuL5R1SXG5wdbT3UukpcN2htCGP9LOuhszBzr70-KyU2DKI43oCzx2bs71V-nCJ4aL423-Y0kGG-wSnbghzj5fgFqsQrAayzkukXjo4RZH-XrDI1gtEiPxz1zhZNCeJQ520lC6H8FI0qPayTPPlsCZ6Mq5VKszUbZndkF07HPfLBcuK4YW3Wj2C97j1RQwFFT-XNVArnw33zbY9waiuPorK_nu0rLpfg6Dl7zlRcr8lTCqzqFQ2XilE9IGp559n7f2iBB9ToYLCehqLVY4gC0CCWpakSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=DNdekk4ZprRRokGhAdJMIAzDhpKCbSpfCbSBMZ-c4bJAOpvSmGmn1FFSWUuL5R1SXG5wdbT3UukpcN2htCGP9LOuhszBzr70-KyU2DKI43oCzx2bs71V-nCJ4aL423-Y0kGG-wSnbghzj5fgFqsQrAayzkukXjo4RZH-XrDI1gtEiPxz1zhZNCeJQ520lC6H8FI0qPayTPPlsCZ6Mq5VKszUbZndkF07HPfLBcuK4YW3Wj2C97j1RQwFFT-XNVArnw33zbY9waiuPorK_nu0rLpfg6Dl7zlRcr8lTCqzqFQ2XilE9IGp559n7f2iBB9ToYLCehqLVY4gC0CCWpakSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=erhBo1_Os0qXBDqwMhcrUAKRerKyyqnCHQehIzAB7kcEsgHvfBjOkGA6UtaVbAew_9viQjNAf2tOqZz3imtD8fY-hLdo_5PYCbKE-xDTzlsFFu03vbsM0Twglu0-52c74pWY53k4zmNbtL6Y8VD6EICIqD9C33bAYY56M1GRZNihkYIW8g9hn53Ty-Frv2YCg9oDcrn4wqBobw4KfHJUOVcgN3t534ZgzL_ZnrSYOO2_qqjIfIwVpWB4FW73WV5dWiZu8oshn1Ls50Rfey52gUIxGVuPKF6o9GykhaVW7oDXlohre-jfeu1wjWSHZcKpdrTnmI8fDDsJUNeTLVnS2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=erhBo1_Os0qXBDqwMhcrUAKRerKyyqnCHQehIzAB7kcEsgHvfBjOkGA6UtaVbAew_9viQjNAf2tOqZz3imtD8fY-hLdo_5PYCbKE-xDTzlsFFu03vbsM0Twglu0-52c74pWY53k4zmNbtL6Y8VD6EICIqD9C33bAYY56M1GRZNihkYIW8g9hn53Ty-Frv2YCg9oDcrn4wqBobw4KfHJUOVcgN3t534ZgzL_ZnrSYOO2_qqjIfIwVpWB4FW73WV5dWiZu8oshn1Ls50Rfey52gUIxGVuPKF6o9GykhaVW7oDXlohre-jfeu1wjWSHZcKpdrTnmI8fDDsJUNeTLVnS2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=ggB3CXp_B-Vn55TL1qGFfKXP_bfASgswUYxUmcvE7VUSbvknrM8gHuLL4Xe9PlF5CTIbv1duf6FNiSQLIXm7YYIaSPShNYUs-6XHpbUYv1i_PjgR5Lg1eCTt3mOIcmU11slFFJJgK4cSG7K4_AJDP-fd_7zNfAfQZZXC-lYP0kxnlQ1xcJKvRD0WRb5PyogAZUzBV6FhBOdozXEmnnEedPRmIL5pTfut6ql_4IfT7QPSC_DJIXcCHVgGvDe6gKhFvB0dR2bP3oWhK0sNW91ZfSld_K4tI4ws0FJeSGVUtBbqRdMx7hHG2FqGOcF5_yo59nYy7CW6ztTzU3Rr52Jj4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=ggB3CXp_B-Vn55TL1qGFfKXP_bfASgswUYxUmcvE7VUSbvknrM8gHuLL4Xe9PlF5CTIbv1duf6FNiSQLIXm7YYIaSPShNYUs-6XHpbUYv1i_PjgR5Lg1eCTt3mOIcmU11slFFJJgK4cSG7K4_AJDP-fd_7zNfAfQZZXC-lYP0kxnlQ1xcJKvRD0WRb5PyogAZUzBV6FhBOdozXEmnnEedPRmIL5pTfut6ql_4IfT7QPSC_DJIXcCHVgGvDe6gKhFvB0dR2bP3oWhK0sNW91ZfSld_K4tI4ws0FJeSGVUtBbqRdMx7hHG2FqGOcF5_yo59nYy7CW6ztTzU3Rr52Jj4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1W2RNcM7HEDplO93tfiYZpO4pXBJL5FD4_fnrLN8uv6CJAV9DRq6ZZP2G9P8KkRVKlHc582fSEI53H5SUcY4_o5Re0txQ79hzkpUFjBIN19gstvwYuQ1PMjc2JqokeLrKM0sV-pDMX4s4L10uPI-hmrH6WFTk4AZLmCOx7LwBHeBBtBTXWZO-4W9FItMkXFzp1vJHoQ8LgcmLHCUaToSE26Zf8jHnsN0LE7T9rgofp1Ql5hrxMSjvVCSAIfVnJ4RshVQWH1FDriGrqfh9PLa8jf5S2R83hJLBPrjxWZMldl6Fxw6y8kUYjHg1iLzQtGQqdDkV8KsQWRdTcdQcTSXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=R4mH0JaJF81SnXCsJDuSGvd-4bUYOTZTbjphg5Z7VHcvBLi7VwcdQ7OAfUzsmfQc0iZjOpOK0vT3XWLlPrm9o7HeANLaR8PRQh9CCgyCsVaDELmMdC3lIreQ0l_A_j4LCu8gbIaAN_shXcA1z7eaAeywj9OycW6dTOC1gFF6efqLAYd31W4ubN7VvGPIW2eOcYgffQ_WVFgbtPejtzOrTamGPwRgzMU-MjrblRtq_Qm0zwQx3dNntQF_CB1lZoFyGMrO0i4mdV5fPMQnwCI3zpsteAmkk2kkvjc-6VDtrPaXRlezswKHBPDl4Sa7R__gloVAkENNScDqxCQG2anD9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=R4mH0JaJF81SnXCsJDuSGvd-4bUYOTZTbjphg5Z7VHcvBLi7VwcdQ7OAfUzsmfQc0iZjOpOK0vT3XWLlPrm9o7HeANLaR8PRQh9CCgyCsVaDELmMdC3lIreQ0l_A_j4LCu8gbIaAN_shXcA1z7eaAeywj9OycW6dTOC1gFF6efqLAYd31W4ubN7VvGPIW2eOcYgffQ_WVFgbtPejtzOrTamGPwRgzMU-MjrblRtq_Qm0zwQx3dNntQF_CB1lZoFyGMrO0i4mdV5fPMQnwCI3zpsteAmkk2kkvjc-6VDtrPaXRlezswKHBPDl4Sa7R__gloVAkENNScDqxCQG2anD9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=msUDDcBV55LdQUxrtYvU1NQyIo1_rwjB-5uIoD8JxhVpVhmkG1DyyvhF78kukmCyG6FJzm_2TGCV6o501iCkDmejjFFgmLVQrasKx7m-5wxK_jK1bXdY31xR8xEnJoiMwSUQB8F9JvhlaomEhS_bL86fcYyCk6aQoMHjUxvoxHT9uWtj5f7irbBjquHb02HFobHLUfZnd-Arfos7dTqNdxOmp-GP02zU9JjqS69JxFskLcflr0cyKVEl6q6lXGMcgOdwxgKLMhji5ir8JzSvBn0fkVCXk0KsA2DU11Zi_VBNyDa57scG9eL6JTP6-iwAELRnln0cjTQdTuRBGyqxEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=msUDDcBV55LdQUxrtYvU1NQyIo1_rwjB-5uIoD8JxhVpVhmkG1DyyvhF78kukmCyG6FJzm_2TGCV6o501iCkDmejjFFgmLVQrasKx7m-5wxK_jK1bXdY31xR8xEnJoiMwSUQB8F9JvhlaomEhS_bL86fcYyCk6aQoMHjUxvoxHT9uWtj5f7irbBjquHb02HFobHLUfZnd-Arfos7dTqNdxOmp-GP02zU9JjqS69JxFskLcflr0cyKVEl6q6lXGMcgOdwxgKLMhji5ir8JzSvBn0fkVCXk0KsA2DU11Zi_VBNyDa57scG9eL6JTP6-iwAELRnln0cjTQdTuRBGyqxEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=nM5dvXSgM6N1JxzCNtxdtiaOdZ1NiQdVfugs_T3alvd1flvSbE9qi5rtfKGQp5_JAVokr0vIvi39laGoSIbd83g7ElINBUgC5PFbl-gw2ikixELyNTxHrvqJAcw_k7Leby3gE2POpcMnoh9K3T60UktpkKzNjqNwW5-f00hH9Mx_UBg9V5kkia2yQLXbw2L1Ly_vFTtAZtSiBufBWDL311dcdY5rGwrXscyuGPU2txNtA9kPE4W2y6Ge-0fIOCkLIG-UBBJwR55yAxwAY3e_xRmY14GhhuTWqCh75SqdGHr9BaJUkkag2czhTyNMkPsb1pnP8WB6UD2Zac6tAVnbxqJDWwJ0jiLS-ttBab8vmFlv35vD_QwPx_njFxOWfOpICV8xb8LyHUhRjucWETGJbAr2mHzwnQfzJQeQNzf-QNlbPHB-bYk_L9c2sJwImWhhLVirPmp5XZxmM9rGratkfwnlvd3FUPyqg2bC7lOUkkeEv7j0hurpkumESKMiYYKwL5FTovBMdEnD8OM_KPbABDN6_MwwjYfAkCPJEsLJG4YsKT657syPOBLFpKVyIs-IHtYA_Pbt87oUg_32UT4aFFK4GYWW0q7YB1-6e13uNvDhkqKS4bLDKhfaRNCTHz6StUjYkl6sp3ExOrDNUv1zS2ZasL2s37ldPJilDpj2BmY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=nM5dvXSgM6N1JxzCNtxdtiaOdZ1NiQdVfugs_T3alvd1flvSbE9qi5rtfKGQp5_JAVokr0vIvi39laGoSIbd83g7ElINBUgC5PFbl-gw2ikixELyNTxHrvqJAcw_k7Leby3gE2POpcMnoh9K3T60UktpkKzNjqNwW5-f00hH9Mx_UBg9V5kkia2yQLXbw2L1Ly_vFTtAZtSiBufBWDL311dcdY5rGwrXscyuGPU2txNtA9kPE4W2y6Ge-0fIOCkLIG-UBBJwR55yAxwAY3e_xRmY14GhhuTWqCh75SqdGHr9BaJUkkag2czhTyNMkPsb1pnP8WB6UD2Zac6tAVnbxqJDWwJ0jiLS-ttBab8vmFlv35vD_QwPx_njFxOWfOpICV8xb8LyHUhRjucWETGJbAr2mHzwnQfzJQeQNzf-QNlbPHB-bYk_L9c2sJwImWhhLVirPmp5XZxmM9rGratkfwnlvd3FUPyqg2bC7lOUkkeEv7j0hurpkumESKMiYYKwL5FTovBMdEnD8OM_KPbABDN6_MwwjYfAkCPJEsLJG4YsKT657syPOBLFpKVyIs-IHtYA_Pbt87oUg_32UT4aFFK4GYWW0q7YB1-6e13uNvDhkqKS4bLDKhfaRNCTHz6StUjYkl6sp3ExOrDNUv1zS2ZasL2s37ldPJilDpj2BmY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=SMnMD2fj2KRL6fGH3u0sEPglk8UhRf8BiZzz6mSjXPoIrVJbGek67qUIzZFvG454gDA1bEPyE90-oWMs1v_WNH6WFggowKe_7Xs7vPIkI02hd04upsGO4lgHb3Zm9Mslzs7IGz2ksuEH23_2_Ev1TXPs4Uyr-6wionM_H5Aupw66t7nnXxtrFKVsV99f9Dq0mhp2XzznTLZZtZcIzL3zcN2sOqmRWeHWbzEO2fP3bQbOAaAOSB477viiFNGKEEwSOciZpwHa3z00aZkcgA08UHBmTMOzJFQtbjMg6qmrzknM0or-rWrTbojvey7--yNhzmyADmVRxMZPDUuMO1dyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=SMnMD2fj2KRL6fGH3u0sEPglk8UhRf8BiZzz6mSjXPoIrVJbGek67qUIzZFvG454gDA1bEPyE90-oWMs1v_WNH6WFggowKe_7Xs7vPIkI02hd04upsGO4lgHb3Zm9Mslzs7IGz2ksuEH23_2_Ev1TXPs4Uyr-6wionM_H5Aupw66t7nnXxtrFKVsV99f9Dq0mhp2XzznTLZZtZcIzL3zcN2sOqmRWeHWbzEO2fP3bQbOAaAOSB477viiFNGKEEwSOciZpwHa3z00aZkcgA08UHBmTMOzJFQtbjMg6qmrzknM0or-rWrTbojvey7--yNhzmyADmVRxMZPDUuMO1dyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=TAitiFPKmrkJ_fhgBdC2Ampxk1pO5tSqhwqkFSVqO3zv8OrmYwyZQu17AmErgtI2W9IoGERZygbFLiXsPSW3aDYLPI-qKLBCVrMNpcAxFnscoMR2ukOb44DQF8fUjARknOiRjWro8AwrM8ZH1MA3zniSWlgritMV56tIpbW-j28w0Az6ITVNj2A-wdv_MCyDSwBDtU27dHUAvX49MmogZx1QsAqOcgIvlVQuagpOzXCgBPvB3OmwiWslzdy1ha9YuP_B7GgKM4oDIieMPbm21mwir4oYcqZaJCVLwb1rqk16lMAv9F-qXzS1t39dBTZzg4fvR5zqPwhBpZzB8twbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=TAitiFPKmrkJ_fhgBdC2Ampxk1pO5tSqhwqkFSVqO3zv8OrmYwyZQu17AmErgtI2W9IoGERZygbFLiXsPSW3aDYLPI-qKLBCVrMNpcAxFnscoMR2ukOb44DQF8fUjARknOiRjWro8AwrM8ZH1MA3zniSWlgritMV56tIpbW-j28w0Az6ITVNj2A-wdv_MCyDSwBDtU27dHUAvX49MmogZx1QsAqOcgIvlVQuagpOzXCgBPvB3OmwiWslzdy1ha9YuP_B7GgKM4oDIieMPbm21mwir4oYcqZaJCVLwb1rqk16lMAv9F-qXzS1t39dBTZzg4fvR5zqPwhBpZzB8twbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fAQgHXrl6MwFZUns-XKqMU9nNh8uyBry1o_u_sXP1wqNAcsQU9lwgKGK2w4PxFTRwOrmQJLXX545eI-H7rFipVCq5rlCN2EKvkvWisvskRRtYqemhJxc4D6tz1Ysnekjqd-TchncTpBva5H7yGVi5gLCyiQgz-XltR65JSLjH6QaCgfoCFrNDlm7Qvc-TKXlpA3LkPcNirnvv459sBBiebRSH03ym23Nf2YsKC28ujDz3lHBwqtAvdj9l2fnRD0dZAKfWu1SHRoHquEJEo0greIn-1B0_JDpDyqgcbxkm2jrUQ2zqWiFltK41iQqISFrik919bNA5ggVKFf1sbZxAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cqf5MNa-4KfjeClz9WrTfndQisGS9kWNAlXCeVH220aMQ5L86WkmQCbd7_qi336pAQuej50T8stuAUQK8sU7y1Mc36TSy8zKPTKYCYlJuGYGnPsuGzmd0wkjKHi8FZ_jW2sMT5670D6-XYXtrh8u9aEz2PyWQiABGKf5BvWK5UiIIRa7FYrlxJOHVK7pgl3nO5BBtDxoZ0w09b6E3KtaN08vmgwwIUou1utjCqPGNmsh9PTXf1FNdFRhyGdDN-aNReF9rZyBLcMkpVFqUc7KsEBomUbWI2KAs7n6Sx-Lmd5v9XIao8egYbpz7ZJe9z1IsZnycCk7lOaP8su4VZxwaA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=LcpwlYjDZtxRN0zs4ULfVA2OFIRNs_8JOfy2cA_SfmsB8594mSnRbq5hzY-6iDdq0GJrivUl8CQOyYd18KHb30cV2KpdLBptS1eSaJly1GQFD3aS3HCtYsHDLtynIjP8IeHhgHMboxJgGAYYWI9oJC5NfhBC3faRPqA8qXZZK_ubpL6Pqp8ukT3zI8qkE6_i91dgeBNNhHYXLlU6FjkC3JwJsL1MWRmRluMM21x14E17LCe_UBYB3dxlVptorMeOySSD5Ugi1iIT0DDBHWnSFHD_6seF5Mn9Fz9dYNp_Hkk1fyZynF7ccslTBqlxd-qkvjVxA6cQ2ljfdRVWHcFrO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=LcpwlYjDZtxRN0zs4ULfVA2OFIRNs_8JOfy2cA_SfmsB8594mSnRbq5hzY-6iDdq0GJrivUl8CQOyYd18KHb30cV2KpdLBptS1eSaJly1GQFD3aS3HCtYsHDLtynIjP8IeHhgHMboxJgGAYYWI9oJC5NfhBC3faRPqA8qXZZK_ubpL6Pqp8ukT3zI8qkE6_i91dgeBNNhHYXLlU6FjkC3JwJsL1MWRmRluMM21x14E17LCe_UBYB3dxlVptorMeOySSD5Ugi1iIT0DDBHWnSFHD_6seF5Mn9Fz9dYNp_Hkk1fyZynF7ccslTBqlxd-qkvjVxA6cQ2ljfdRVWHcFrO4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXXIJ3TUUO692I0Oe3IgC8MUeKoy04QN9NLcUTnHjwonNn-IWCpFYscxOZ4QJr8prmZUmjLHkJIT34AfoJvYYhoVu267GCiz96tonIwpQCzP8aDlcj7tk1r24nHbGjPa-PengC-P9UHXUN71cR_8riUy5lkH45-6HPqYkvlbazzjJs8r5cywFV-3ge8dbX0w2m6fQG-Qq7zbNb1nNXBs7s7GL5bj2j-fycrA90lCCA5D0IqpqhJQGNI_wnbi-nj_Bva0tFwTCcCNGZaRfP1JCVzKRc6LAZpExG3BbZ5CWve_eh4e3axU2QgN9tkvhLFP5vpmZAPtYkCrT2zjKtVdNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FPqFpYpVCWs6np9Fd_QTzUCzj4_quMU6xeSCcoJyqODIyvG9vS3EPBiQAmUSEFrRnECEBeLJl9gNc2RajLXWRH6LN3E5pMU2lvKB58DuvGLqIMo45hhSiUAyp_i3puWt93AA3SOvEBjhebjDY_scFhNgE0Ii9XySi7kYSRB4JbwhNwgQLQMM2TaD36rEru5kSzABu-q9AoyIUErlEcHwqU8zD3wVa5gWUc_fad6_MAnwo2j214Et_bFhYrk7ptEMUpcUE3-myVR89CDjQBr7BFBHNCcjf666neesBIRrFe96flucIlCun38y2cjjFlzVSmaFi9ELiiCWp85ehSkm5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkB9DCMjoMp0kSkEUgfQ4Y6-8r-H4LL4KA7BkstCcA9FpCTv20RPkmVQin1-zYaSY8Ou9Tpjm0VxO2hgKVftdyvtFQ0cFVfXWBlesX2bJYJcE-_L9Wx0gIWEpjbKx7FKkNpiOtWLDdtU1T9EYmCse-D5hGoUrqY6sQ-TP1EZSpXUbkkCxvFU2mS4FxaehAc2EUNiZV069wfxmwN7BZX1L-ndMuTcH8XXLt43mzTXbG-Z7-K5h-EDdjSuKjXIlGrthsboPMouv4xW0Mvqh2pVuk-8Y1HOzlKm91cDuXfnjOeW9oPO1AUGtjRq_HrEMUamqo5ZncEzxpHX2aHLIZsODg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7BfbTxrx1G2K5CiCHg5YvmvRgF6cAC06FIspYS7qQ3nNp5T_tThlWDNjbK0yEpkOCAP0bq0qLiT3ZRUwdsN0OAr4eWwslS3B34CDnUmcU72mgXCclV0Phno_MZuS8nT8wuTz_k8XtkEyCZ34s40z8gQ1t5PRDb2w5THkRJgNBnpB7fzN3KTgfRzwfUXOg3U1g06L5bkO-1WNqMRpCOb2T0mUEAh2NOWtvyFVOtWDlmkCnt5xj-0QQpscBj20TyzdB7kOFgPA5qY3DyFLSNkpKAi11QS7j6N4dDFm6hvwQyjSwCiupejSloxqE8JU39jNOHGFpya0gjCg2OKJpkSBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=LvXWPAQXSK7r8-sXumXqwVPGW_yQUALNDG4JwPLhXONgA0BlFOxkCxPfW7ieEgxoLgR7kGQIadT22ReJCBFSA3_5-wulZLvrNcVzQpoobYUYqaAIJv-h3EK-M_VgFcDePXHGqpTxvEsM3JGOCgcx44Zdk-fdYIAGPfQRqDOiTfH1FuN-3hNwIJRHSN0n379vGQDuabNuU2g7oQKKfO_uy0pA7WTxS429XHSgSRrEDz7HoprCaRRmt4ldyGOoc3SrgLPj7Z_keadoogaFQKB-Ht-pVnwuyouWgcfhcKfgfWGbo2hHL_dViy1Uo_zcpZNzywfJzawvecOb5Td6-nxshQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=LvXWPAQXSK7r8-sXumXqwVPGW_yQUALNDG4JwPLhXONgA0BlFOxkCxPfW7ieEgxoLgR7kGQIadT22ReJCBFSA3_5-wulZLvrNcVzQpoobYUYqaAIJv-h3EK-M_VgFcDePXHGqpTxvEsM3JGOCgcx44Zdk-fdYIAGPfQRqDOiTfH1FuN-3hNwIJRHSN0n379vGQDuabNuU2g7oQKKfO_uy0pA7WTxS429XHSgSRrEDz7HoprCaRRmt4ldyGOoc3SrgLPj7Z_keadoogaFQKB-Ht-pVnwuyouWgcfhcKfgfWGbo2hHL_dViy1Uo_zcpZNzywfJzawvecOb5Td6-nxshQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=jNQOA7CrV8IfizXTm5WVrPbMqH6PhdCdcw3Q8zzIfwajUV8WpoXt8VwVVEUn-mTbNVmLB2LDsRn6TxlLmLavqETQ3-pvXlwwrjtF1IVN7b6Nepq86pHIJnjUu_e3ejQJXMav8gzHt1zWCZNofb0EEKm_bSKUwP99SvUfPpE0VC99CK4NhxVHjGPk8z0GORburONvwUxWJZ1O00eYIvh_Q6IB_ymkfh8stNwMt5GyK_jQtWn1CMystvPlI9ziwN4Zv5K3gQUhZEIA53yJ9CbbRDE3mECFrDh4f-i6rL_Vc5RY5yFWKoI5bfK46b1LUccYelilFx1R4jddrL_Rc5GxWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=jNQOA7CrV8IfizXTm5WVrPbMqH6PhdCdcw3Q8zzIfwajUV8WpoXt8VwVVEUn-mTbNVmLB2LDsRn6TxlLmLavqETQ3-pvXlwwrjtF1IVN7b6Nepq86pHIJnjUu_e3ejQJXMav8gzHt1zWCZNofb0EEKm_bSKUwP99SvUfPpE0VC99CK4NhxVHjGPk8z0GORburONvwUxWJZ1O00eYIvh_Q6IB_ymkfh8stNwMt5GyK_jQtWn1CMystvPlI9ziwN4Zv5K3gQUhZEIA53yJ9CbbRDE3mECFrDh4f-i6rL_Vc5RY5yFWKoI5bfK46b1LUccYelilFx1R4jddrL_Rc5GxWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D322EOlg332PVjBVkn5NGreyrQDCVQRPuLWr9oi0Xa8dDo4nTkje1IINAOh_j58dYZZvmrOpQRfMJinszTsnzI4zRqJCKSY1qUmlHNEX5pgMHdnCsXcAYP6ThAyQgjkX97wsDRpfyqpwLlDt3bO1gK51ms89II6SDX_5fbmqT40O9CiXEFlY5dK7FSdP0H2yTAB1opPxNmhVmgM-NcdRFtw4S8100U5ZnudueuHtNaRqw4xSN7BezrETAsDmVRz8oTHNi2EiciXG_hnZ0lu_Pq6bbKIq5pj9oSoJqN-Cmuz5yY_iPgxibshj1I0zJsu7RUaPjTPNaPub-VLVOeLtsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=vU9vUgb8BzPAEOG0XWdkF_yrJpUb5If13ClkQ_WBlDuC-iI6po9a4uf_XP2nozXRRAClaNaOGWakAs7xwKA3NQGjkq9pJNDJBgXhczYTD46HjcHGTosLgDsXyvjK1X115Pfhxlenfe7ApCqZ0q4F1TeC7GI27H6yYoYvRA2UQAjAIrEJQLI5O36H0cKsFUB_jDYoUr5RgT1Ow9HPx-8xtFljDrrFVlrRfdTusY06rV6mUxqIMFTA1phlRBtAmbjodnEd_BKmASWBg-ZbMwGcFS4dsQiEw9xlr9NI3gMiHBlJ4Zx-WB6pLH1c5OMj7nTyWTHf6-7Hp6u86aVDYCofxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=vU9vUgb8BzPAEOG0XWdkF_yrJpUb5If13ClkQ_WBlDuC-iI6po9a4uf_XP2nozXRRAClaNaOGWakAs7xwKA3NQGjkq9pJNDJBgXhczYTD46HjcHGTosLgDsXyvjK1X115Pfhxlenfe7ApCqZ0q4F1TeC7GI27H6yYoYvRA2UQAjAIrEJQLI5O36H0cKsFUB_jDYoUr5RgT1Ow9HPx-8xtFljDrrFVlrRfdTusY06rV6mUxqIMFTA1phlRBtAmbjodnEd_BKmASWBg-ZbMwGcFS4dsQiEw9xlr9NI3gMiHBlJ4Zx-WB6pLH1c5OMj7nTyWTHf6-7Hp6u86aVDYCofxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Pz5QFwJ31dj6OtawEuXLhlo6ZCm9DKkBEsZ3bUBpAeSwGe-Zhj_ahtdcsa6OTO2XTZfrtypBuksmMhToVxmdwkgUC9nawWCLzvMDmdxWD5KzyZN1xjfPB52dnTwhMoBNZzYShSSgu7ljkrh5a6RG4dIohBzteWDtQV3TdewGHYOtVFbjAO8blE1eoYpa3nf9ukyF9LirY_kwKJUvU6wu-jm1N4vJjfVXhyV_9RltAKdkrtFMnpMqcDPpIWCq63TfVK3GUZHq7UwDZe_jZFvMfOSCOorhpEmYu-UApSWxDTFXAI-LjyvvvTQaisyfZhinSzqXLybIMhrG4DEYKaCLUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=Pz5QFwJ31dj6OtawEuXLhlo6ZCm9DKkBEsZ3bUBpAeSwGe-Zhj_ahtdcsa6OTO2XTZfrtypBuksmMhToVxmdwkgUC9nawWCLzvMDmdxWD5KzyZN1xjfPB52dnTwhMoBNZzYShSSgu7ljkrh5a6RG4dIohBzteWDtQV3TdewGHYOtVFbjAO8blE1eoYpa3nf9ukyF9LirY_kwKJUvU6wu-jm1N4vJjfVXhyV_9RltAKdkrtFMnpMqcDPpIWCq63TfVK3GUZHq7UwDZe_jZFvMfOSCOorhpEmYu-UApSWxDTFXAI-LjyvvvTQaisyfZhinSzqXLybIMhrG4DEYKaCLUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=mnuSxKeCAVpaS5o8YMSg4HMfqxRyld6VVGvnNQMGALiJmDeyD0SdwcgmahwJJsPrG2BW_JW9HqtmnHUEoWFG1bWk16Lojk-LjljBtdsyHBMgy8UnCQeckbYlT1sxkYL07J-aRpkapis0P-My2LWKd4uIzr4VaSn_LxzM18f_YnMIfuU2Q6kSNZxUqhHn5IwxlDbge47Rs-fMa5gZy0a9rxpCDn2fYIVVDgiIjTSv6T7vEFRmcFFL9j6xVSk-h9pOe69BXgVYPpZ51-6fqNptQ7VgfKr5qmk0-F77X03hvfiibpudzetIbx9FlZxeh88a8odCMnIsZnvXI1wTrHC3wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=mnuSxKeCAVpaS5o8YMSg4HMfqxRyld6VVGvnNQMGALiJmDeyD0SdwcgmahwJJsPrG2BW_JW9HqtmnHUEoWFG1bWk16Lojk-LjljBtdsyHBMgy8UnCQeckbYlT1sxkYL07J-aRpkapis0P-My2LWKd4uIzr4VaSn_LxzM18f_YnMIfuU2Q6kSNZxUqhHn5IwxlDbge47Rs-fMa5gZy0a9rxpCDn2fYIVVDgiIjTSv6T7vEFRmcFFL9j6xVSk-h9pOe69BXgVYPpZ51-6fqNptQ7VgfKr5qmk0-F77X03hvfiibpudzetIbx9FlZxeh88a8odCMnIsZnvXI1wTrHC3wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoqIfq_zesm7aUOoFhzUHinXC3hl4R_wZJziiRjj1ipjgbEZEX6rU_jBxsR79JeoYIDOhIzXhs567n5D3C-JXYy6fX72NGM13AXOR9aCZZS_D4Q0v9CmVd-TjL5I-3uw3wH3cPqImdCSG6X2c_9_VvFiofOYyv5dzFt-D0J9djv50xn3HJyjGWydYKtASuUjzyRbmElSSkVWQ1_jPRu-0RmhkOzke_qD0Y9stXi1QauyLpTNeGipm5_6hcMtSRvKMIRHIwEfObFd5we8rwFvxWfO-EbTCn5kj80aWR2nZwxfxvhD5V9_0AIoW1fHwFD370dbZlMx0s-XD5gLPTYLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=Kszc-KYJLN099jb6CrukgE9yV4_xR6E4M5To2V2HaLdGIqhRrb6j_wtNIsl9fx1U1hENzopHhJPE8EDaX0H-Ma1vlKBXhrlBawPwPuBVaYmhrI-gedcsSOQP4JKktSqeaR_xh9D3miX3VPzQeBsWTn2kyABjElKvq6F9VM5N4tRBxdKfP1wqbnFxszsffmiGU8YeRpDPBn4X8M76Ge-VS3TybacsV7C9Ueg4xAtNgP043wNwEEMqXAsdSBIn6q6YRTFRL1gbjjjgke0VlScE38TFF7HHBbU_EkIITK7wNsIQGH2qijA_ctZgDTjsmTX-Qe6BomGbjVaIV9ePbLu5UA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=Kszc-KYJLN099jb6CrukgE9yV4_xR6E4M5To2V2HaLdGIqhRrb6j_wtNIsl9fx1U1hENzopHhJPE8EDaX0H-Ma1vlKBXhrlBawPwPuBVaYmhrI-gedcsSOQP4JKktSqeaR_xh9D3miX3VPzQeBsWTn2kyABjElKvq6F9VM5N4tRBxdKfP1wqbnFxszsffmiGU8YeRpDPBn4X8M76Ge-VS3TybacsV7C9Ueg4xAtNgP043wNwEEMqXAsdSBIn6q6YRTFRL1gbjjjgke0VlScE38TFF7HHBbU_EkIITK7wNsIQGH2qijA_ctZgDTjsmTX-Qe6BomGbjVaIV9ePbLu5UA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1qgfkFCMPYFexSiTEaBPjvBH0FCmAYRbs8C9wfmBe6BBQ1GGQkIISHM47AgjNvutM7djQqW2I1iEIbkmNz8tFy2GUnc6QtJIbwgbpHNP5YlM8Amev_-pMEmtUWa24kC3eUOCjNuJjVaClIUQyb1v4VrZVReMimeTIJa_hseQDCUGlGO7iZrlylocjV7iIUKHzc7mwFtaVV7oeF8HELFsQnqj6LX_P-UsAXObK63Zxz8T_-P_pEhBy_FTugo-tRmPRWPpdxiIdLP4NXLtmWLtQYA917_yUZ2LLRTb6juF3-py5xnDv7sxMiGcLEwXBBPsuPn8xkceuIoTd0OogDkOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tqP1rqCxIGDc28lh0A7nSKWQFa_6KintGCA2_7ZwIswVpDGhe45m7nDWoO6Qlh-BiHEmNIroErBghoxfPXY89Gz7IpXr40LtfEY3Z5DfyJ3ThRt_aTtggPEBmVM5ML9oK7URVRL5Ca5gp155qK91OzDS4JS6Gqp-z_aFpOFSVmmllcZy6UhYQ7t8If8Q65umaeapgTvESlOSTKIr_9q5VyZLJiTEzwBFb0eL7YX99lfi0m4qu3OuBKqv827cgm-GJ4H3vRpvs2Tgbsf3M-4yzaEj10W9kx4DYQY09L0k7Qxv4-8RLf6ZsrRcK_lxHoXRaW0xM0I7X0itLuLyNvKhxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vKTWvEFg-GDQxVPYSRdhUD3CzcUByUWmIfU1-kewZMudz6AidtBO3A8Caiz04w2Y206yPtQV38dloPPbgS1dDdMinpnEzyUgHw4inVbJl3wDGwMLEERIpr_PZk_q-qqZkAHHHzf6lfeidnatRTqVv_AQT5n12MrjKchN7psqG2kWmm98nh3wrQlEZQnLkHGvNpfzRTMlKiTwdmzGRKVCMuZxZTm8TvJg9_EyDqW5g88mDKq9emGroOQs2r84IBnHpw_3MIM_2EyNSuu_8yI6r1fTnIOj1hJTaO2AhRpuRYn-BI6_ohDkNDjVWXony7hlC4NuEMf5DONlHm9V8Vf4Zg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=vKTWvEFg-GDQxVPYSRdhUD3CzcUByUWmIfU1-kewZMudz6AidtBO3A8Caiz04w2Y206yPtQV38dloPPbgS1dDdMinpnEzyUgHw4inVbJl3wDGwMLEERIpr_PZk_q-qqZkAHHHzf6lfeidnatRTqVv_AQT5n12MrjKchN7psqG2kWmm98nh3wrQlEZQnLkHGvNpfzRTMlKiTwdmzGRKVCMuZxZTm8TvJg9_EyDqW5g88mDKq9emGroOQs2r84IBnHpw_3MIM_2EyNSuu_8yI6r1fTnIOj1hJTaO2AhRpuRYn-BI6_ohDkNDjVWXony7hlC4NuEMf5DONlHm9V8Vf4Zg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0mhI1I0JOhqH6RkYwXzh1O-YPFP91IJ2lHvX4uhC7GoCXUMmkmOGHNeDqjKLo2gklip7ErAllNKg5G7PMOPUUQ8LvwnCWp1zksOb4LBfq1Mv-dtUuWh9UPWrD5V0kMCRHC-X97M8MAX8X3gzQxzKAEZUn5KFI6n1xaKR-Y5aYEofQefll8SrIljXXR2siOGvtqJAjA6jtBieeH4SeIu00pxGpVdoexcAOWB5ZX_E_v5X0wdzcX2DDA69h8k_ra5N_jRU8qUEsopdQunYwl0H8sf6zI0dlMoQ2uytRclU2anYwVPIj_cctC-kgK51vkxsEso04GbQNz0doHYN-qpgHgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0mhI1I0JOhqH6RkYwXzh1O-YPFP91IJ2lHvX4uhC7GoCXUMmkmOGHNeDqjKLo2gklip7ErAllNKg5G7PMOPUUQ8LvwnCWp1zksOb4LBfq1Mv-dtUuWh9UPWrD5V0kMCRHC-X97M8MAX8X3gzQxzKAEZUn5KFI6n1xaKR-Y5aYEofQefll8SrIljXXR2siOGvtqJAjA6jtBieeH4SeIu00pxGpVdoexcAOWB5ZX_E_v5X0wdzcX2DDA69h8k_ra5N_jRU8qUEsopdQunYwl0H8sf6zI0dlMoQ2uytRclU2anYwVPIj_cctC-kgK51vkxsEso04GbQNz0doHYN-qpgHgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=MKMBSw0unfjh-4v78GX47MXBpbbZUB_AvQhvplyxLdxjHQnChSNv7fTl5_J8oJwxBulcbQREauivoU8d8Xl-qHMDVtQNyJ9K5a7ilynNG5jBb8eBaiZ4GcqmNb9FwIbp721MOBPLVFZp6xreRR2cPma7j28ZdOKToFvNlXYMTztLIPY0cuao8OVZ20Apk2CW52fOHyv4PSJuKkeKJPUA3hctiO7w0u7n1xzLp6OuLcFFQeLUKgucrVKC7pFISPzt5CBzZfOLOYOtJUCBzk2-gUmuyVDJPavMKSkkNV9YZoJSUHrPS1SwjbkGhLDOVexBYpoHmsIjDrny28etGOxbPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=MKMBSw0unfjh-4v78GX47MXBpbbZUB_AvQhvplyxLdxjHQnChSNv7fTl5_J8oJwxBulcbQREauivoU8d8Xl-qHMDVtQNyJ9K5a7ilynNG5jBb8eBaiZ4GcqmNb9FwIbp721MOBPLVFZp6xreRR2cPma7j28ZdOKToFvNlXYMTztLIPY0cuao8OVZ20Apk2CW52fOHyv4PSJuKkeKJPUA3hctiO7w0u7n1xzLp6OuLcFFQeLUKgucrVKC7pFISPzt5CBzZfOLOYOtJUCBzk2-gUmuyVDJPavMKSkkNV9YZoJSUHrPS1SwjbkGhLDOVexBYpoHmsIjDrny28etGOxbPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MZv4eV-7HvjjBH0auZyjbyASH-Gn7-qpvga1SMw6cb-h8yktlXsxfxYKaoD8n2quTFMdEeKkos_chKwa2xQwrRjROzOnGi3DCwGZJPFgI4nh9v2NHVU7ZhqCU75WW60kjsg962i37vHNdqEjp-G1gz_O12GjyEMPD0ykfJEm7izWOEUD03XhVx2PHY9bW_4IJOP-4Et3Vx-eFKA01yGeHpE_rjArBPj9878tyJQEOv2ukYVOVGfJ4KdybqqbZGGV-hmJndVTb3eCRArecrphxpBoVlvXOg2wKNK70PAYw5mnBUatwC9oJ8fe1vvlgx-m5X2_WP4oLKqtEz8RFrafcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=vtxAythytxDTw_mQ7x_DYY8XuldWoZw292sCjkc93fhqvcpivfEOgeBJ9XQznRrbSxCZPMIMaTURqBCE5Jhsfv1zPn2FpfuFEhhX8ngAUExC9bnOyy6r8h85ysjs0sA041r26Cv5z-JkaXUUE3-7hpHJBlIEQJ0p4nyH1aYNDX4h27NT7bROIeNyhxi92yqI_7w9XF9k_bIuWzGHfnoqJAmokWTYulC7zHDSAOiY6cpfqXL4KLMhDLmg7P_rw1fs3C1RS6AJJ41B96oA40HlpmXdcfQMvjttf7GyjQvft6XiKet01nDmqdnJjFXPZLGRuzwesAd9qNgKwcqfdMhI4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=vtxAythytxDTw_mQ7x_DYY8XuldWoZw292sCjkc93fhqvcpivfEOgeBJ9XQznRrbSxCZPMIMaTURqBCE5Jhsfv1zPn2FpfuFEhhX8ngAUExC9bnOyy6r8h85ysjs0sA041r26Cv5z-JkaXUUE3-7hpHJBlIEQJ0p4nyH1aYNDX4h27NT7bROIeNyhxi92yqI_7w9XF9k_bIuWzGHfnoqJAmokWTYulC7zHDSAOiY6cpfqXL4KLMhDLmg7P_rw1fs3C1RS6AJJ41B96oA40HlpmXdcfQMvjttf7GyjQvft6XiKet01nDmqdnJjFXPZLGRuzwesAd9qNgKwcqfdMhI4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qxKD4WGO_1qDipGshVYvEKk75DMe8xHHf51-UKKeTzcKcLR0urkvvp41jqxeXh6Pz6ttu_UEHwnEXtBXUn819TSaZcPe91KI1um0GOcXXKVkKn994Zhf1iCTfjN-33GZu34bXLVBQFjf5Eyrnm2U_-XQ5_vRWVPDUapTNmcTmxBu783UQOEEe6_NVzSSh1Slb5F2Oyl3svm7qIeQQDU1ic6ZQdTkvQk2Z8W6TRXWFoZVqJGhWpHNEnlsYAaEH1Zdh6qwv5-u7QqV2TLgNE7JW2XoBogFgl6D_y8i0uTKMWn2ugpMYF85TosZsj0GBusXY2tBh-jgT9h51VjFmnoxlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=qxKD4WGO_1qDipGshVYvEKk75DMe8xHHf51-UKKeTzcKcLR0urkvvp41jqxeXh6Pz6ttu_UEHwnEXtBXUn819TSaZcPe91KI1um0GOcXXKVkKn994Zhf1iCTfjN-33GZu34bXLVBQFjf5Eyrnm2U_-XQ5_vRWVPDUapTNmcTmxBu783UQOEEe6_NVzSSh1Slb5F2Oyl3svm7qIeQQDU1ic6ZQdTkvQk2Z8W6TRXWFoZVqJGhWpHNEnlsYAaEH1Zdh6qwv5-u7QqV2TLgNE7JW2XoBogFgl6D_y8i0uTKMWn2ugpMYF85TosZsj0GBusXY2tBh-jgT9h51VjFmnoxlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=JZo6UN9I_PzhTJh4QrUGo45V9Q4ZDA22BPmr1hlKJraw77AJw4KzUwurBcyTrGmAzcMDkRI89xbAfoGx7o8Gq7Teg1Kep7IsN7I59sXbWuT9Li_7mx93t6M5nNMMiC3wf3qwFshFku69o60iJRlIIh42E2bhtXUQddnwPRGE9tWni4NaMd1U7ReZrR0vroRAPQmI3S7pT0EzH_0PSd6gDEKO16kCBL1HIyvHOHG9ZDgiSaeEXuAm0ktLhFRrsi7vqFg6eB7DjlShn5A1yb-unpLkK0SJhDVA-jjBz0967Iry3N6oJA1xeOYayyAjnqsgA_57A-6q-mUTNgsBCS5l7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=JZo6UN9I_PzhTJh4QrUGo45V9Q4ZDA22BPmr1hlKJraw77AJw4KzUwurBcyTrGmAzcMDkRI89xbAfoGx7o8Gq7Teg1Kep7IsN7I59sXbWuT9Li_7mx93t6M5nNMMiC3wf3qwFshFku69o60iJRlIIh42E2bhtXUQddnwPRGE9tWni4NaMd1U7ReZrR0vroRAPQmI3S7pT0EzH_0PSd6gDEKO16kCBL1HIyvHOHG9ZDgiSaeEXuAm0ktLhFRrsi7vqFg6eB7DjlShn5A1yb-unpLkK0SJhDVA-jjBz0967Iry3N6oJA1xeOYayyAjnqsgA_57A-6q-mUTNgsBCS5l7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=tIzow-JCYcqCdrVqXZ2vplW3oL8vojZWR-p_Rc-bg8asyUI-zlsysuMkQ9sqEpcBFDUdaL-a7f4F-wCU5v_mSrmT4J8c-N0ZBMT0KjjZWbuREvKYdesoVZayPgCLTu6DGe5I3s-8I7mwwTeWLfYDflOpRct9nKdCloQYK9UkZm9hny_iKyQzGlUZob5iu3tw9McCoe8fOgBs6h29eoO2c5aqQmCOsoEQE8PtaT4Om6My1JiQ2fa55qMZjiK9ATFoS68_vvZlT_iOjecdrc4NtKHv2JMFHPZM48TBxZzq5tly9v9JKFOs5dFCKIaxC3HMsgJOkkdy-cl61qQBFe9BBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=tIzow-JCYcqCdrVqXZ2vplW3oL8vojZWR-p_Rc-bg8asyUI-zlsysuMkQ9sqEpcBFDUdaL-a7f4F-wCU5v_mSrmT4J8c-N0ZBMT0KjjZWbuREvKYdesoVZayPgCLTu6DGe5I3s-8I7mwwTeWLfYDflOpRct9nKdCloQYK9UkZm9hny_iKyQzGlUZob5iu3tw9McCoe8fOgBs6h29eoO2c5aqQmCOsoEQE8PtaT4Om6My1JiQ2fa55qMZjiK9ATFoS68_vvZlT_iOjecdrc4NtKHv2JMFHPZM48TBxZzq5tly9v9JKFOs5dFCKIaxC3HMsgJOkkdy-cl61qQBFe9BBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JFPZ4rRNbdJFlvzzY5a2AZB8nshOOXLeQRqa45khD1JaQA_jOpHsuycifRkBVtEU_jSMtgfBJB48abUpEi9fAPlruburfODldPqblOgWrkYI4CqPN_QECAt_rz8_iNF5BYv4K7D2Csec3549yI_hmLwwi_ezgLBuY4I8XgaKxIwxigpIw4Zfjbog7U4ZyArcKZ1MqUFaa1d6A1gvEmYcvL98GFopuFY25mRUspzYzBqLl57NmeNpIJycafC0vSIkytGVmGOd7n8dh_aHN-NlvjI1Nm7VJzoLGwvacgG4dkEngvoSrhrePGrVgENLhing_3oOyVf30JGFv8FhHGb5tQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=KzILIQUAVF6WBVM1k-AM14FupRQkP4vBVylKpyDBrv8vjpopPKMPX3CFLKQtchJXnS9yZaMVDsr4POMYwS3xq6UouiTloEcqeIQeeq5vJLbb1xRUacPg1dm1YifoFZJZsOh-AxNSEnwD6Vm5V-LDmQo2DY_me_Q6pDLbqxdPWvLT-1Yww01i61EC3jVrqsnt0QLVRLXcx3RMGRB209i8bUNlWwCiE1TqB-FNaU15WOCjExCycSLKQLmFD66hrB14WOEN5tbKfPugGGk5ziTURl9htqfCUd8UDGNY4cFDuS05yyeL4ZIqVt09SyXqejKRcm-SMqqdvbsIbWFnlS1q-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=KzILIQUAVF6WBVM1k-AM14FupRQkP4vBVylKpyDBrv8vjpopPKMPX3CFLKQtchJXnS9yZaMVDsr4POMYwS3xq6UouiTloEcqeIQeeq5vJLbb1xRUacPg1dm1YifoFZJZsOh-AxNSEnwD6Vm5V-LDmQo2DY_me_Q6pDLbqxdPWvLT-1Yww01i61EC3jVrqsnt0QLVRLXcx3RMGRB209i8bUNlWwCiE1TqB-FNaU15WOCjExCycSLKQLmFD66hrB14WOEN5tbKfPugGGk5ziTURl9htqfCUd8UDGNY4cFDuS05yyeL4ZIqVt09SyXqejKRcm-SMqqdvbsIbWFnlS1q-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=qV327oNCAiYmWcP6UsS2kwfskcF98iJahaKsbhUpMVA4shBrQsUYTF0Hz7M2IpiUTajjSkvZKnyaezE2sOdonLakYhS2Hec4YNud--vqjtioxPGeMtJqBTgH1JUC0m9WlfX8VRt1KrSCCn4j_Z_dEvA3WQEqnmACgwMnj0CJUHpjzUBXcAMdMmSqHdnlgI58BKVRPcNVKH8027MGa71y3sZEtx2k4_AWn0zU5Y3M7gUzNwiyxd7eFRhUf5aStQrs8ZxgmlKw9KhNonyei4IlBVH1i99ECth_kSTq4P9F2Zxf9EXqP_HVvgXQ4H7_pNtBgeQGmW4ZS-l2Z5ebks9IPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=qV327oNCAiYmWcP6UsS2kwfskcF98iJahaKsbhUpMVA4shBrQsUYTF0Hz7M2IpiUTajjSkvZKnyaezE2sOdonLakYhS2Hec4YNud--vqjtioxPGeMtJqBTgH1JUC0m9WlfX8VRt1KrSCCn4j_Z_dEvA3WQEqnmACgwMnj0CJUHpjzUBXcAMdMmSqHdnlgI58BKVRPcNVKH8027MGa71y3sZEtx2k4_AWn0zU5Y3M7gUzNwiyxd7eFRhUf5aStQrs8ZxgmlKw9KhNonyei4IlBVH1i99ECth_kSTq4P9F2Zxf9EXqP_HVvgXQ4H7_pNtBgeQGmW4ZS-l2Z5ebks9IPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JCyLzV8p7qfQG-hrbSBLaEiG60IBIfdIOTQL6g_RT8n21hDM35dP6qntLqR62g9slAKORNbV8Hz7N-D0awD2y9sAT0zKclCR0UJ7H0hjupzzz6Ti_rFiwH4EFgRAycH9e12o-XUuc4wXJSo3NleX6djMWh2h4SHbSXxQA-LatZ_rMlykXVwL9PeviGXmlau5qR7ggXqNfQ29ufXzV2AQwANeeFtMp7P8TZF8bk24wdHECxInct8qYFKZqiEZw9hNo8UV4LV1hRDyCaYADrZZ8DFWS8h8Ik1tGbTjB7g7TQPPog4EBn_CVperFal_SGVtEBpFAA5WTZCoPBpW66rWEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=pEZwiPo_8YeZaPHwST2emQdSugdDGEk2DVuUjTEabsnLn9L_msutVjIYuykC_LrPiiVDI215t720CTKuMA6mjkuHp8jOcL2Ys2zARofIr_DrJj_C3JScynnqR1N4TikDcG94unZe0HTd8ak1OialRkXrUjBRV8c-TmXDG5UUolIbiR1_RvUGgaoDkG9x-m0EE2SAhkz4x5s-XtVccut_j4EnPnWA1HTw8FoTl_-d7e5kaPXOWNW6ySd9dBCb7X0OSAviejyyDSJWK52EguaTZzPmvpkCjVcYtTewaROtOujDCGOmg4i98KO4vrieP7BnWPq2D3oVrIla35gPBHRLMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=pEZwiPo_8YeZaPHwST2emQdSugdDGEk2DVuUjTEabsnLn9L_msutVjIYuykC_LrPiiVDI215t720CTKuMA6mjkuHp8jOcL2Ys2zARofIr_DrJj_C3JScynnqR1N4TikDcG94unZe0HTd8ak1OialRkXrUjBRV8c-TmXDG5UUolIbiR1_RvUGgaoDkG9x-m0EE2SAhkz4x5s-XtVccut_j4EnPnWA1HTw8FoTl_-d7e5kaPXOWNW6ySd9dBCb7X0OSAviejyyDSJWK52EguaTZzPmvpkCjVcYtTewaROtOujDCGOmg4i98KO4vrieP7BnWPq2D3oVrIla35gPBHRLMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=DyBKf_NCq0pXgEGaNtaSb3q8ygCUmeLhD3ta2JPfCt_FZ8rmJ7r2WypLPYSvSPzNasjtEPGpLEZ_Elc909vNyzb2L1S1N8R8yYOGitl7PU8ZJTp4pedEOZIc0GsZCsIjYW1pLhbRnQuE_cSYn_oiuhlEB82oB8ayR6-OHHBkEjSUIrdtf3cuGeGgOU_EdRF4ndGBRaiZ9A-QsJPCOdFFkK2ccMiH_zsiTGhE3Lvb5i5p1dck4qNIytX53j-Bhyj3o5T2cBZvZ8ynH5rDpaCTNfMLMHZ_RthmGhWzaVhaTTB7w83fournd3W6JMe-5rthflNlzgbUxf7SStn_wVH5vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=DyBKf_NCq0pXgEGaNtaSb3q8ygCUmeLhD3ta2JPfCt_FZ8rmJ7r2WypLPYSvSPzNasjtEPGpLEZ_Elc909vNyzb2L1S1N8R8yYOGitl7PU8ZJTp4pedEOZIc0GsZCsIjYW1pLhbRnQuE_cSYn_oiuhlEB82oB8ayR6-OHHBkEjSUIrdtf3cuGeGgOU_EdRF4ndGBRaiZ9A-QsJPCOdFFkK2ccMiH_zsiTGhE3Lvb5i5p1dck4qNIytX53j-Bhyj3o5T2cBZvZ8ynH5rDpaCTNfMLMHZ_RthmGhWzaVhaTTB7w83fournd3W6JMe-5rthflNlzgbUxf7SStn_wVH5vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=IycNSrcFyKen608nztyHzhGI9CZdyAsCS6FDHwnfgzkEB2y1eiOE7e0Yz60g_sA1rx2EPDxBPKplPFOdAytjbG_2RNuU7bMOdZ5dn1gjvVVZhskRigoi1VY4K41m68loec_7ApPdfuncp2E0RDKF1yb1hjellxnC4bxL7_zrhNdnXGDd-ZGt6p97efni92aIr_Z6AfvDcLREC5TTUz-CguenLPm-IpFws3Ogt_h0IpomrWZeCotPYmIH9Au9gzldrHzAHDaZNC0hX-dHVOTLg-qQhXp-X8O57Ea8KIZnFeim-_g5vRGTEt4FRGDdJP-wEi9udoVHYpjapy68baZmGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=IycNSrcFyKen608nztyHzhGI9CZdyAsCS6FDHwnfgzkEB2y1eiOE7e0Yz60g_sA1rx2EPDxBPKplPFOdAytjbG_2RNuU7bMOdZ5dn1gjvVVZhskRigoi1VY4K41m68loec_7ApPdfuncp2E0RDKF1yb1hjellxnC4bxL7_zrhNdnXGDd-ZGt6p97efni92aIr_Z6AfvDcLREC5TTUz-CguenLPm-IpFws3Ogt_h0IpomrWZeCotPYmIH9Au9gzldrHzAHDaZNC0hX-dHVOTLg-qQhXp-X8O57Ea8KIZnFeim-_g5vRGTEt4FRGDdJP-wEi9udoVHYpjapy68baZmGDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sNffnn-_V8AT0tCTkEnqEWRWJ4G7rgoFDHpy-twYeQltSpZdARuZZOr_fgr1i4T5sXaIR7zHDKK7gj5NDthtfTqod-OawztoaK9FIW5tq7TpdOeH6-zp6gs2vNj5KdLMuhKPU-5Nqua3yYwjcQ3-RRBEkoVaE5M4H0JV8mJXSpnxYn4sE7mheuxT7OAFGAK57gYXbxoQZv5VLvcBOW6uZGE8AeRHNPilS7_YL8adxZbn_rvuU58K82VVn2oCS3b-AnjjX6FsUuy-VxIDWsvcd2KiyBd2HOXKpP89WT3lYZMaLifP9twRP8mmDoR7IJObOqSv5_1UgoUwJ3roZdwsBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t85TGgKQ3yPwApZ6c7mdeagXkuCTyS-IkcWYwFNnoYA75lazT1Dgc2GtW9W3Mj66no5tbMgCp6BB6I_uDrjwHLp_bn6KuMYxsFb5_9fSZB__9sScy3KbtV3WjlWOhjoFB3UDwTTGFo6h-WO5dHF9reMiNCafFx7pgK_oS7lpHxiMtBog9YkH8ZYVtgo49KktrYqZoBq0KtLtfHHrzLYOuQ95AGCZCsncRpGPnWVrIwC2KcUgffyuyWo233h08vvmZCAkvU8OApr6YBtHInwYf-UEFT5TjvMOJ9vJXaksbmc1QgPnMPWTC_Ap4z0ch-rgqAS9ng2VvyG1903n_3L5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DJO_5C7iz0Y-tRR0aszLZFFAm7eJ4x1KBMg9dIi28U8mo1p2HwkSq1Vk4VyoKBLRmsdBByhr3b5cg5DKZxbT8Q9KhSIZfVCzEbzayLTOKn3tRu6fCuTgoPvzioQ_pk7u0q8l9uvc9HCmtBf5VPWIOXf4WMA6QqB5SZGt7wtfJcXfoEJKqRK0hFDSvyA11uuajzrQRiszER6pK35HKnqXv6nZbXiWNXdcC5S0kn0ohR-B3a2B2gpwoGuZFZJPuyD7R8M5W_YtNBOCQP3fc37HCqowv28TpdMUYO2x0bGADYLebphuSFvT9JhMJIQJ2RBo3j4QLf_K_kmyH0ELlCQYVg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=nyn-muKfEPOU6ENfEchBIfQvDBTv7ZTb59-a7o9rrXH0dMdgB7kSVQUAr2vbk04EQyfxRJ7kCeYCnfzYh3UoQO6nP78fOintIu_XH0e064CzOsM6aWmACzegx66VCUGNk7-31IOoeepEyvBDeRAdrwiTo99bsD-_TkYqAbbP6qXeCZ2XFwx0nm1IL2ia7WvLHTLRWnFMvax1I2abjQOmwhnSyLNxcRW0Nm3G9clMbDs-AyM_R02Kp4s_L2WakqqCnRM0dVEKgKBira1uH3Z3NqkHMiCrE5EkB6o1nSnZyLmfI_-kwJi--opeNJO_4QfrW8m1oz61VwvwGTiZQ8zGyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=nyn-muKfEPOU6ENfEchBIfQvDBTv7ZTb59-a7o9rrXH0dMdgB7kSVQUAr2vbk04EQyfxRJ7kCeYCnfzYh3UoQO6nP78fOintIu_XH0e064CzOsM6aWmACzegx66VCUGNk7-31IOoeepEyvBDeRAdrwiTo99bsD-_TkYqAbbP6qXeCZ2XFwx0nm1IL2ia7WvLHTLRWnFMvax1I2abjQOmwhnSyLNxcRW0Nm3G9clMbDs-AyM_R02Kp4s_L2WakqqCnRM0dVEKgKBira1uH3Z3NqkHMiCrE5EkB6o1nSnZyLmfI_-kwJi--opeNJO_4QfrW8m1oz61VwvwGTiZQ8zGyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_3dTc9ulCqeMF_6LUVD5NNZspQD3B-DsP7vCdB1nvY05xAFbhsAwVusWqBYkQRGfo9YWVf3m9gcQa1ls8SXzlfPUgwVE2UtGITCY5ht_RgJ0_mhftU_4At3sCPS7_dcRQmXkLfxlsPBmphct4_rVHt5vZ3YTmrFlarV_eArHBatmK_-xL8slAyDZWA9Ybs7tuYrUbar-OquhpQrx_VtbJbEAhl46Q8F6PAPz2ooat-5pxuPnuVQHLR-Ng7fey3qvQ3_P38pgB7YW-HTzZyMsZ33INjDaWefPWTLjXnGdOWvHPDjH3I9ftcJaD79DbzIYA34s4ctfJUuQhRHjx-nGafI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_3dTc9ulCqeMF_6LUVD5NNZspQD3B-DsP7vCdB1nvY05xAFbhsAwVusWqBYkQRGfo9YWVf3m9gcQa1ls8SXzlfPUgwVE2UtGITCY5ht_RgJ0_mhftU_4At3sCPS7_dcRQmXkLfxlsPBmphct4_rVHt5vZ3YTmrFlarV_eArHBatmK_-xL8slAyDZWA9Ybs7tuYrUbar-OquhpQrx_VtbJbEAhl46Q8F6PAPz2ooat-5pxuPnuVQHLR-Ng7fey3qvQ3_P38pgB7YW-HTzZyMsZ33INjDaWefPWTLjXnGdOWvHPDjH3I9ftcJaD79DbzIYA34s4ctfJUuQhRHjx-nGafI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=glraqZfKffUVcuZ7NvAzKpyV_4kIfMkmqE7k5-ZR9YdT3Wm01LJqPlx2PUsJiTj4hvu_x5CV-yJU09aeCOxPcumQzlOjnsHQ1Zd4K9m6yIP_VyGaTXJgAAoorXhUa6C86-Sp6Jn9cylwjsTZw6HZqQPne0KKHzgLPSsApWQffFHPPgjJCqQ9wwTlFt1KWhuC8VWJsi0zepdAgQFAzhpgd1keg5mhhBI0-hZ1EbqoAbRXR6XteyHZCt1c9jC-TkIU0HOsHQZFjGYmuMg4Elmus15I2wwHciIsy6g1UbT1rPt0kZw39lsDhpBNUyYsaL_SvnXCtS-1nNm332EiyTIgbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=glraqZfKffUVcuZ7NvAzKpyV_4kIfMkmqE7k5-ZR9YdT3Wm01LJqPlx2PUsJiTj4hvu_x5CV-yJU09aeCOxPcumQzlOjnsHQ1Zd4K9m6yIP_VyGaTXJgAAoorXhUa6C86-Sp6Jn9cylwjsTZw6HZqQPne0KKHzgLPSsApWQffFHPPgjJCqQ9wwTlFt1KWhuC8VWJsi0zepdAgQFAzhpgd1keg5mhhBI0-hZ1EbqoAbRXR6XteyHZCt1c9jC-TkIU0HOsHQZFjGYmuMg4Elmus15I2wwHciIsy6g1UbT1rPt0kZw39lsDhpBNUyYsaL_SvnXCtS-1nNm332EiyTIgbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eACuKwLGzIGnWue2yyodYLILZf4aABDL_40XIoMpL5jABmcVDl-aN2Lt-ggs7MXCWQbsWQ6UjpSA5V3zoO-8YDAee0qHDQ7pC9oxZJSALE03IgYsSB0Ly4xBFYReavTTVvo-Vtc0ew6fjg9YKCc0QJAvVKdOWnTHaoMvNswRZ-h4gcc72zwSdsgOqvLjdLMIibkMKq1mNQ0Hc1WP2Gb_hTQ6Af2JaEP1-erwDeN3zlaHKsDecYeLtY5IAWDhg0mr6sahCmjskWHz6zkOIx8lZDiI52x97EWuG7twYzOttWXLr4sfogKTUxMwG0FVzVIIyuvHmn9SIBMxf38NEqkJJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
