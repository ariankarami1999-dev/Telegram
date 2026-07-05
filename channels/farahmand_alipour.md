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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 19:13:36</div>
<hr>

<div class="tg-post" id="msg-5870">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXV1qWa8gp5WoVsx_qCHTiqdZCRW_Yt3xPOe1-yN9NoGnP28L2sU6NxaXWw-R-qlLbYcrTEGbX7cZQ5Ets467IA4zWO_xZkOHVSQCr4cDdKOhmEoWiZ31KozBwvRssRU3rhnIO6rPMPpe5_JALLyk0nwx4hnelJWgJclI63RMKIDzMbFehNhcM1lfWXvToON6RsfgcOw2Bx3Wy8bgbtFoM9L8C9oK4SrTvn7VeiF_6aLfEcsffAq5GyBwJ1bDiXx-sz5aDop3ORe-PIqM9DPMHrYg6EFuNXfVbT5063fjHuod8Y8Yy6a8FImBaU7HXb1QWg1oRs9dXwN0GOFgE9hng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکبر هاشمی رفسنجانی، ۲۴ اردیبهشت ۱۳۷۰:
‏سری به بیمارستان زدم. آیت‌الله خامنه‌ای مشغول صرف صبحانه بودند: خاویار و پنیر
(الان میگن هاشمی دروغ گفته
و فقط یکبار راست گفته اونهم  وقتی بود که خاطره‌ای از خمینی نقل کرد
برای رهبر کردن خامنه‌ای)</div>
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farahmand_alipour/5870" target="_blank">📅 17:19 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/farahmand_alipour/5869" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/farahmand_alipour/5868" target="_blank">📅 15:48 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5867" target="_blank">📅 14:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5866">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvuu48-7ftYW7z8HOLvJsy6aKkGKqTAfGlaEMeuoNYBHEYn7MbgYxG0l6TVK75vToCVhfmlmx9pVyr3vayamPeT4d36-Bmip0WjhKMl6YlKYs5RgXalJ993nHXHf_RzkErXKtjQ4W9dZFZoIPmu9TUTVN_l_Bl8peL6P4p9nGpY9KoFaeJtKhGvcCXJOwqxxsV_LhdkAe4nEa_mU7MeqjHAvxMjfv3rnFiEebWk1CDgDGuWDLirP8MKwRiWp0yK3NZyEvTK9sPP5TpijI5YPBBbwLO8RROzlF5DGnWUlzm7WmnjLTOwRU3yfNbBjdQ39WuWjdpY3lXxDIZKiRH6Fzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیهان، مثل صدا و سیما، زیر نظر خامنه‌ای و رسانه خامنه‌ای است.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5866" target="_blank">📅 14:16 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5865" target="_blank">📅 13:20 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5864" target="_blank">📅 13:04 · 14 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/farahmand_alipour/5863" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5862">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C96CY-fgQo8vVHExU7M2Cw-Ks_GlygWXm_oHh81BvMiqYXuMtV8Et3-yac8yunuuSZ1QYbi-MeVk7F2KMeOMyIhAyeO4bviHmfaLoE4ckJQPNSS_SzC-FNz7w2v2exfSnEx7p3566Hwn-rRPvIM5cGNk9Ts30pHPuBYfoxBpbrZCiRaxrEE66E5kPBD46zRZq25pUXo-qtze2k8V9sLFcoJbDHnc0vkBaWvQwYe8qoMK6plsgQn6CojByIdemCrM5zfBPjRKQNkRuYuuCofBdDbC79kzJ6ogrB4SQCbHJ79heldocu5vaaq5N9yXTYg28MVrqZGoQLQ-ZZn4HmrvyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5862" target="_blank">📅 12:46 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYJRFQvhISI1GvZf9xKq5SrjG7wMbgQR5njcALOEFcufvNAZyMgPf7bQX-5DPVJc5fPWMh-MqzAr2kY3Wjo1_wkwlHvXjoYJ0NfvGIUVxob2HT4E9pSCPafP5YZse0stTFhK0F8cu6bD4wLIBWgt_BUTLTNqNebTxB_0rOFlZYLCOC4jXL2FiaCKM6gGqUYnWdXd_9ihWpv3XgcjKwC3blpO2B-Ra-oNkbGLiMA8jl5xhnSY_h5ysVM4ufC8OPQvfa2o6GiNnpEDPWDBrx72cbeO4Pu7c16DKZY_rWRMwyQfLP2yGOoXcFcWjpFPGfhqYySc115PoPUYiYmfAvDoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2qbZP2GuD1nBirtkKoaBH3LzMp2gryLzXji8KK3sM6DsBzJ4VS4u_AgR2-xUtoa5ZzbgePtOlk7rbWbnRJk8dmpbWCo-D_3TpXnRvtWzAejsb2gaHNoMe0jwlr3Kg0O1fP1mHA0uK33irxODxj6DqnyiNyd4mhYjSIpofQSJykzRy1VnihnTUdDkAqp8Gwy4tqFn41tiNZMgy9tCKUXGcYAVdk0hgS2Me2oeqHeiAgo0twz7DcnTopruYtw3N5SVLKU_pTxYCPAeAlLH2VBb1OW82Vx9YRzkaV0p6j1U8OevfiPfAKmfYpCkeGFxECty8OVjwUfClrUZS3X0bbSBA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=rC7o-v6eLufEOv_yLC9W5Y82rYgEfd8yUuPNRmLcKdjMFhMIpYORKQxAqy-JJWWDpegmVl8jRUXBL_wK21G3t1hHLYRuE5jO33n-1mMJo6gV35BlrPOgYrNkyG_m89KR3EQBLCWjhkbHC2FL_IWJ-rM0UrQxZ1UMr0jsfK05EbzKP7_a_5dR_MPV0RExOnl6GPGB0OotUIJmMobk6c1gfaxfG3Z65ZTgFvx76qMlMLAAqsskOnoPA2UeGWJXcszmEHPkCAV6YzkbOCSQWcjm4PwCFYHJTZGddKLxk3me8xPR-Fv58d4i-2MT1xuke0YYyzs1fSc9PWI4ksEm1P2GPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=rC7o-v6eLufEOv_yLC9W5Y82rYgEfd8yUuPNRmLcKdjMFhMIpYORKQxAqy-JJWWDpegmVl8jRUXBL_wK21G3t1hHLYRuE5jO33n-1mMJo6gV35BlrPOgYrNkyG_m89KR3EQBLCWjhkbHC2FL_IWJ-rM0UrQxZ1UMr0jsfK05EbzKP7_a_5dR_MPV0RExOnl6GPGB0OotUIJmMobk6c1gfaxfG3Z65ZTgFvx76qMlMLAAqsskOnoPA2UeGWJXcszmEHPkCAV6YzkbOCSQWcjm4PwCFYHJTZGddKLxk3me8xPR-Fv58d4i-2MT1xuke0YYyzs1fSc9PWI4ksEm1P2GPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=OCQdKY7Ts6cyNDMJbiKhnK4mtl8hSUTazim6IUFyWWGqTM81Bn9ZFFK6jjDOGzc9r_YDZ1uhPkY4JfGt3v-63ECsyaFm-4YLtozYbQkwbu2SRBLmaqG36bEyn1XV6bC4Y3sffEnwXeI6NZQKhAsI3dlGmC95xoyceeXWzshYk9eFKUe7n8hfDEGApceZ69eYERiI5g7kUi_Idmc1VcvP3Y0gcXtuMRyz5-l0t51jQAhOMuzzHDq3aF41d_pgjNoNQ6Lj1OAnrjbyyb7oj6B8R2LaNlpzJAiMcPqA6sJNJg4-8gI3aIISWGhHgG3oltBOIL3yeNP68itjlxhy4HFZ2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=OCQdKY7Ts6cyNDMJbiKhnK4mtl8hSUTazim6IUFyWWGqTM81Bn9ZFFK6jjDOGzc9r_YDZ1uhPkY4JfGt3v-63ECsyaFm-4YLtozYbQkwbu2SRBLmaqG36bEyn1XV6bC4Y3sffEnwXeI6NZQKhAsI3dlGmC95xoyceeXWzshYk9eFKUe7n8hfDEGApceZ69eYERiI5g7kUi_Idmc1VcvP3Y0gcXtuMRyz5-l0t51jQAhOMuzzHDq3aF41d_pgjNoNQ6Lj1OAnrjbyyb7oj6B8R2LaNlpzJAiMcPqA6sJNJg4-8gI3aIISWGhHgG3oltBOIL3yeNP68itjlxhy4HFZ2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J1wjUW6d-9K9UYgVig-PSemP04EfSB8vZQ7f2aTuNWgMEp2isFVWSsJ_nszNWBeChRcpp1TGgOw3k72K4pwk-w9M5BKz-J5MQKPvnVrFXkaONvJK69-HmPjXRMwin3SoeikzyEsCTfLM72EzEi-nRfFAb1vkG8tAHfel3i_l1WTbpWcsRhiUWAZjVPoU0Z7FDcoLfP6Xpvyh38k29XM-KgnvP6nimMgNxUhxUdInApdiRDTvQzbQJawrXGPRJlEWDOaFeedhQLSyxO4YEsYurA7ADwgdB8Z55vVqxOC0L4lreks7XpbD9XDf4dbASsDxDHqtswv6i59ALTBWxdrhlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #71</div>
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
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQWIzPRNNTSWpQuz4z-hXg4jseskGmXe0hLfhIjTttAffkt0vnjM3t4hnohEIs-uEZwV5c4_GAJ34DMd_aBf9avMaelIHZy56M9ltf8mygB3Im1oEGMFFXL6mDZCFzfF8n4DL-0mL0Zji2nvojGj-fGe9AipGQFwPLBTdt-HQoRXetAdEDpfG-RSkZuE0XUAqUaIMvohkQM_-6-ww89bQ7e5uFU9dF4G5_ZgPE2KSdw95W74vEpVPEZ7k4gC9o7ZadE1QFPDjQN9JhsKzqqtLp70EblslOE_59g-Oa6-TN3Obi2Rb1IYhHJIEuzuLBQhpTYL5byP8MQPZUZunOtTIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LPqKORY0Wys6_bkhrgF9tkAqX1iHkqSH0xuQ7uTWghbCKTxMHHpH6pL4C9UH_lXMFOOTWuRaG019DSFifcdhGJ1HBaSp-l8Phle5VwY8qMP1u9RR4JZzORNo8Y8m6TqgRdDawz-i6jPwKJ9JFQxpOOe9BxyE27kwAPUJSIPzy9F2fqxoRcrRa4h6ayj_LNcCCz-za0RNfVRAc9lfH4Alcp9IRiHUlnE5lf9tXisBc0buXZZiml2cjAs0AIShj93NPTzEtdG1z4WuLmv6x9cgT3B7J6zZlHpAdolLIOWh37HjIZHgXvFc89RygCsBwOtd7zLdYBmsLzxd9ij7JE-Ezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmiLuMKqgCRX3JtK5ItcJwcXQahMjh2s9fn6WIO-q4B_I0grBomYJu7ah1B-O7y-n8Rp0kDPNGH6r616GTDqZ40QkZDzcmWMaNzZjeNFBP0tCpLnLi7j5mE-KdckV1s1MZkQNHQmLRuiu-hdpCswNnl0DHkho7I00PzEBRGMeNL0z_F5FLAljd7ia5wZAkaIYK28kSyqtkJrop-VI9ti46bo7J6hBtrcv4K4IU12ENIluUrjrge4LRUoVZFd1zzzPYOPpiSPTHGuP_WXIUiutLxvQgKVQqSz8bGzoRzVkBiQ0ucT2HiyKOawD0eeM7OJteF8tWEcdTy6no6euYYVLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibuw8eCgLFSmB2CVlITZI-GS_RHQOUWXU4zcF6BaDbJtGmz3bo1HmrWqfplPXg2jjpmjHY7qFPqfFLuOwSzDhx5kUvEVvyHjgq3-276Zwr20GOLGyPrq4PBsjyOqzGHxDwYFrb_77zxKGtHrKkCccSggOzM12Aixhp-UbK-kYTJYotEAvd2V-9405hOchVa6HUy1xRRGxJNNxj7RtF_cqjSqdvU053DR0w2R5L9av6tLK7XSG54veFDHDpBaP6bjxuBJn0Ol2fJxfhUYs7hPGa7Gx59N95NlIilbz_5HNtdRDLYZqUo7yY2s394lXm0IJlAmexAC-PXXoJu-PetB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jbc0OwfRWEFUTsCZ5j8ertCif-sLd9FBXw6ss2thL6TpJNV4fj5qH04aedQXva-UTlWUcY5F1ro81oM179u8Z-8OYsU5EUjsknr7Ze5lqMpIdPCPcwnhHFQxL5SUxpyNC0cgbUzwqrCfjSeNXFBIwFr4RK8nB4HFMBVmWtbm_vZUng6AMZ96JOZ3HQztZy3W-gLbqQDFn5eTemFH4DBU_b_HILUYyaXpRm3EfyLMSHbGtrj0NgoLI9l5EBZ926NyGOa-CgGli8bWZbmXX3K2nTLOfdM-3yk82u-HDTGOA7MALlqiiUnEESDfoCZbGnDkYN4U6Nf1Ipnkse5Q3OlAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y4unq_yfs-PSHbEfsZaTX9rX2ysY859mIRQ72AQD-e0ugMrdwPxkvgOQKLZ534vLFfVtgCfpkChS_KMYNfhWMeZvO21g4saZ3bpPTdqgUQqFpaFwzU80Fsg2-S87NkA-u465vTqPYdlaaczbyEg6vdW9pkYhseCZfXqkKiFJ7ozqxWlUY5zyECBItQDmyLHDT7huR4xMesPO04-upnY5akQ6bLgcIxu4uKkqQgbqz4FJ8q4ObbMo4komZ_dJzqT-et1ZAO9WuaJ2wEc5z9SomvfArShG1Q2x6-cmO0ytf4w0ykbSBQQfgp4skgA2fomHiCRuMblhfOUj8AFIH4LeqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sI3jBnG_3fOlE-5K0Xeaq0asN40OO4rgvb3JMqRqDJL3R4FcrbM-xXtiJ0zESe-YDEAHVsy-uX_79tEGyiGlnRd8s9K3w8Zc12nM8bTFDmtCeShnLGtUTWW2EN8dBXFnhdydQk_4WhzQWXXAxMYsZsXgUELnPGFh7OWggpltbXWlW0WFdtvSUmjegtiCopi-MfL4992qq1N1WIhOc8rOKshThGsPlQfUO94GTcrcDYi_0eRcDgYNGLQ_qaHEebO8VILnhjY-5zqytS5qqErs_p1yq0CDz_6Fqm4ZITwySlk6W8J2Yl-BiFE32EYOmi7SKy5gDaZ_vrWaWRhmE4fdPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DvGEhDdsyzW5dqSzQvHf5d4yZqi-XsJ7g7CcbgVoBpiqPT60nUkYCyY1curBuKHOpDhZOhxVqkUg8OTHgsMDA-EMxZH37bigS_FoEPAyOuEWz4YWnxL5LUjiILy74AsMDTCJpk8l2OtcKkjsb-9niJLguGA_6C0lHpOF4lekvwXJNbCN4UZSw2FJe1yWxb2KDyvO-mjVNBzf072VU4aIKJ0pkuowNxlB01SHixfol_pZWsOLoZGNidRRDalInlOePVjIJjIpMm9oFAEPoPLtChTh8bXiTmFrxbG33gJOSPIFWMMIIv0d_6V9gAzAVtjPanh1f4MGH4l4eL0lIFPdjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AImaAwNgnBVIcJ8hCzOh-_97rhegVxIg7ZmxhkmdGUuhokbGuSKZiC-GVrYzDQTNadW5izxhS-xBwu_GPQnB3-FWkktZJVmJIhtD9-xbEexHGgVNtQ2pIvHy5UYKD2_SzWqu-9msSr5C9eCgIV4A-NR0FfpHfv5YOhci1AldPsM3JQedoYTNo6LrEC0LV9HTdxZ2BfCgQ8ky6ue14KwwD9CJvg9LX5agSGEv6qTd80zXwPub7Oc88CMYe7BZLp6L7YxFKfQ9gDZIPFHal9REOpvOYSjXOp9F1gT8TGhau71t4cC4GrurKd6evAYAmTwsRO1thwKffLgKX6Ymipe4HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GDmfKjy35JlD6wktkap2ithwLD7EX6fYsXeBM4UX_brjQR5afnKEKtwFVjC1ifGu-wR8DWYaoP0LVyM_zA8jtySSaBYE5nFDH4JZ1ffYDw_SD65ZdyYs8aO8qXsjqraBRxFWJb-NDLOsisU4REC9TCjJAvxFcS_u_a-EmtXR8noSMfcdCogs7srRS5HYkprfugizv8EqhBhsgSX7G61W909YV0MYKOQtfwBOPPyD7_HrAsCfEDMhxkUjqDa6wxoNxPFUuZiQGYa9dNGE03204NnT4C07JwemfeJjkmvGnkKlrbWSYg7wtfHz_i8l5o-2fdaI1zkafhB9xN8lZuEjrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFfYm0_dgVeuq4X_6tGW192TsfeeXgot-7P4tTuinjB9S5sztLuSRWqEzDUwQstiM5PKgvtjUJbftCD-HgeEyoRcG2IO1VED8uX_2JQvsr2cLsDSMJt0SdA8mDHoBpO8L7hCtW06OqKlRTw2CVZPkVK6bZ06EFzP8_r01R3pP3c12YREnI8YJ3TNqs_awqMWxkjuCwctaGcFaq1ngsVtDhBMYPtaD6Rgondb5iM14eq7_mYXGTcvFGd63BYw8e0bJEjnIW6P8Y3kDIRRYVfOmCQv31NScMiPan-h_-DzJw2l2XxKX2r6EskWICZqDAzxe9LLHMhRWCNW4s3fSkNBYw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=jTA_416-0QRnOHWSEUfS7v9PimYK9_XXruMRnB4ChcTNajt0JhE_P9dbJj4KfbN2LUQLl7qh6av0l6VZKkjRLiZvULZVSsrs4oYtp3UXu7cgHZYivJmS-u5ajQ0scyg8H4CsRehmaD7JeZjbcDxnCK9hYDJrhHyMhjaeUN2fB0rAx8Q_cATLjpbkvxYOMpntUwCE8fe-jsSZQjUPh8lKqGw9Z3QeakBORsAgCWF7Qw7ZEk1bf-_XqXxTbV8B9gi8ICJgjVaEb4E2u2aXv_dfeApXqp4oWJhZKVnwPUpigsSmrmkK-QLNfvgAVc9p72xjCqKaIeKCw3cs3fdplT7Gsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=jTA_416-0QRnOHWSEUfS7v9PimYK9_XXruMRnB4ChcTNajt0JhE_P9dbJj4KfbN2LUQLl7qh6av0l6VZKkjRLiZvULZVSsrs4oYtp3UXu7cgHZYivJmS-u5ajQ0scyg8H4CsRehmaD7JeZjbcDxnCK9hYDJrhHyMhjaeUN2fB0rAx8Q_cATLjpbkvxYOMpntUwCE8fe-jsSZQjUPh8lKqGw9Z3QeakBORsAgCWF7Qw7ZEk1bf-_XqXxTbV8B9gi8ICJgjVaEb4E2u2aXv_dfeApXqp4oWJhZKVnwPUpigsSmrmkK-QLNfvgAVc9p72xjCqKaIeKCw3cs3fdplT7Gsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=ScSQna1t_eb2naiifHJHAt8Z1URt-_p94ZYLwx9mHQBYu35Xb7VEojVgrLCvIY-SfuQfOTgz5Le7rL6CNUSFc7y2GIFnhsVdQImvYAoSVRb7lN0WfLzGJJy1fq0dDC_EKPGPjOi_ylQGPZ98ejg9PU0m_7w-2qlW9VCTnhJ7-w30Uic7GTqEj6WEFdZb0Ge4oJAsFV_Y3sZbcillomA263vt_Rc0GVFimEmp3XFYE-6u9JumEkz6-GZiNT3zf9Js7q32FlW_ZJYX4o_CEnClK7DI2PjtDRR6aityys2btGBGT5B6vmy1z8PtRmP8IMx3gLSSGkZNm7DxgFLj3uxLzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=ScSQna1t_eb2naiifHJHAt8Z1URt-_p94ZYLwx9mHQBYu35Xb7VEojVgrLCvIY-SfuQfOTgz5Le7rL6CNUSFc7y2GIFnhsVdQImvYAoSVRb7lN0WfLzGJJy1fq0dDC_EKPGPjOi_ylQGPZ98ejg9PU0m_7w-2qlW9VCTnhJ7-w30Uic7GTqEj6WEFdZb0Ge4oJAsFV_Y3sZbcillomA263vt_Rc0GVFimEmp3XFYE-6u9JumEkz6-GZiNT3zf9Js7q32FlW_ZJYX4o_CEnClK7DI2PjtDRR6aityys2btGBGT5B6vmy1z8PtRmP8IMx3gLSSGkZNm7DxgFLj3uxLzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=V7oObvHZRY7c7CKo0XISeNNhm8oG1Xrvi4CERe3_YCXlglAVdezzFLeWW5jhSjDABXcw_uPwP2SOJ0bI-2225wI3He_zmT4D8kFr7j_YBD6ogHjJCm2GRMF_oCLYTrEsWujIvAvonLYG7VlQB1MVPqJoaRi89_fmqcOJTpMrWAMLvzPBuvF2UKiUOw0GRUe9N92c6vkWbz-_n4J5dqeXhHTCXGcAVeaOADas0dr8qL-Cb7neDSFrj3H5AxOp3MgoaC3BTM67iaiOQmutIjRTydmr4W9IzxZ78wiXWtPDPskHJdtXDHK0EjMCjb4v5zfd4FopRZfwyPsj5IMjsU6s7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=V7oObvHZRY7c7CKo0XISeNNhm8oG1Xrvi4CERe3_YCXlglAVdezzFLeWW5jhSjDABXcw_uPwP2SOJ0bI-2225wI3He_zmT4D8kFr7j_YBD6ogHjJCm2GRMF_oCLYTrEsWujIvAvonLYG7VlQB1MVPqJoaRi89_fmqcOJTpMrWAMLvzPBuvF2UKiUOw0GRUe9N92c6vkWbz-_n4J5dqeXhHTCXGcAVeaOADas0dr8qL-Cb7neDSFrj3H5AxOp3MgoaC3BTM67iaiOQmutIjRTydmr4W9IzxZ78wiXWtPDPskHJdtXDHK0EjMCjb4v5zfd4FopRZfwyPsj5IMjsU6s7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Y6DyybKnYRYQ1WOiBt3fK39NYtfVYuL-mQeDjQjgibWwe3D8T-SL4kg7Oqp5XD2hpmMBd9y-gnpvrgOU1jTRof_epkB23uFwx0MTaAu7cgOySIVwr7IcBLQNd9QT6LKD5-mCWe55UzAlmIbJDTNQWCBPTUJCIxh-ESIHMposomyKQrbSn-88vyajiR0cWoUnbyz-Wq0AydlvVt8LvMwXWQDThwOCUlR0JkpsTg3m3Afyc3G-4riZ8Iazq69llBQFyvFlGYj-8oE2_5lhLVZn6ftDSnKE9pQkUykd0NjbK5FBfcHJgo40fE7Z81fhCx9WHyCQOmzDp3voi2vcE_JjWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=Y6DyybKnYRYQ1WOiBt3fK39NYtfVYuL-mQeDjQjgibWwe3D8T-SL4kg7Oqp5XD2hpmMBd9y-gnpvrgOU1jTRof_epkB23uFwx0MTaAu7cgOySIVwr7IcBLQNd9QT6LKD5-mCWe55UzAlmIbJDTNQWCBPTUJCIxh-ESIHMposomyKQrbSn-88vyajiR0cWoUnbyz-Wq0AydlvVt8LvMwXWQDThwOCUlR0JkpsTg3m3Afyc3G-4riZ8Iazq69llBQFyvFlGYj-8oE2_5lhLVZn6ftDSnKE9pQkUykd0NjbK5FBfcHJgo40fE7Z81fhCx9WHyCQOmzDp3voi2vcE_JjWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=NFPX70oxPxp8MW6cfou6GSfFmbXFLOpSam9ag7b74h7FDOe3nKFLdQq8yn2nmE7Vl5tznBd0iS_26Kg9kQq151ecpnj7PQ8Jz3VtvJP4chQjYCcPCRscSr3BJTuBbz58DZU-80pLkEwcPylHtf7qhpxAAisfeH5BAHrGoKoK7WHeWPT_xPzCeCiXmzad7sNnLA5Ui5WnO2Lpb6erGjAb7eZ0SEI7HTVv5fWegda-jWCPNvGQXnkIhUit86-wrUSadJL0Ls_gmmoNSX8jTAppKdfQHlWapiQAFJNE2bF9af6z4WmCsm9R-nqoLNUAEeiqwY9Z0AYRiYLGGKO8NVBwwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=NFPX70oxPxp8MW6cfou6GSfFmbXFLOpSam9ag7b74h7FDOe3nKFLdQq8yn2nmE7Vl5tznBd0iS_26Kg9kQq151ecpnj7PQ8Jz3VtvJP4chQjYCcPCRscSr3BJTuBbz58DZU-80pLkEwcPylHtf7qhpxAAisfeH5BAHrGoKoK7WHeWPT_xPzCeCiXmzad7sNnLA5Ui5WnO2Lpb6erGjAb7eZ0SEI7HTVv5fWegda-jWCPNvGQXnkIhUit86-wrUSadJL0Ls_gmmoNSX8jTAppKdfQHlWapiQAFJNE2bF9af6z4WmCsm9R-nqoLNUAEeiqwY9Z0AYRiYLGGKO8NVBwwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HsMSvpOMsDJvfW5fctei__JbQz5nMDXo4Vejr6qKxGumDEVW7uq0qqhqlkPxszzWjErshy80fhk8NliNph4w4DjmSJ-3Dnn-dpKoF886Yx8OkZvqY1G-lKvFdqCn_L-rHHeJgzXZOuwuGWDp7_ZLNdLw1VEDG9vJORhIrVo92Bw7_9Ogiud2n4XM9pR6hcksCNLtR9M8kC_jvbZZxDsR_VWp7oj52gVhh0uhXpllssyFbt1FYzjGpBbJhOwxbBNN64b-64SlpfqGZf28HdkrzAO80UoCqeDdjGTXsTbCoVYTnC_AwCWfNI_ypxfPYBWmkbtSJJf9fLlMv7OlqidHGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=HsMSvpOMsDJvfW5fctei__JbQz5nMDXo4Vejr6qKxGumDEVW7uq0qqhqlkPxszzWjErshy80fhk8NliNph4w4DjmSJ-3Dnn-dpKoF886Yx8OkZvqY1G-lKvFdqCn_L-rHHeJgzXZOuwuGWDp7_ZLNdLw1VEDG9vJORhIrVo92Bw7_9Ogiud2n4XM9pR6hcksCNLtR9M8kC_jvbZZxDsR_VWp7oj52gVhh0uhXpllssyFbt1FYzjGpBbJhOwxbBNN64b-64SlpfqGZf28HdkrzAO80UoCqeDdjGTXsTbCoVYTnC_AwCWfNI_ypxfPYBWmkbtSJJf9fLlMv7OlqidHGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=uPE9mvnWV4cQxx7oiQe7RNCoBTK7oWUbHk8OOM4FBRlma97tGC3-H3nyXnA9QD5X7qJGFEOxqXsXk06zhHKUTIEuk4GJiZ_nh0W2BrflP1VFXL5nRuM9uPflHO99Ulqi9BmFAGpA-CzfwRG3tf4m6YvJ0CYe45iIWD1qwTQeCGizuqKW9gv1DwgqTgizT9N5784ZFaWEKUM9GpsXyVMbnMwWMl2LRP6-ep4C0biUihdabrJJJOgvB0XOtP86QR_7Cfjwk46zfcXM7q3GhG8fpvBIHJ2xuPkfascBaMY445tUAoK8wzhRcuCl2F5LvJtNHbA4jW71bMsAL2bPj4RX-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=uPE9mvnWV4cQxx7oiQe7RNCoBTK7oWUbHk8OOM4FBRlma97tGC3-H3nyXnA9QD5X7qJGFEOxqXsXk06zhHKUTIEuk4GJiZ_nh0W2BrflP1VFXL5nRuM9uPflHO99Ulqi9BmFAGpA-CzfwRG3tf4m6YvJ0CYe45iIWD1qwTQeCGizuqKW9gv1DwgqTgizT9N5784ZFaWEKUM9GpsXyVMbnMwWMl2LRP6-ep4C0biUihdabrJJJOgvB0XOtP86QR_7Cfjwk46zfcXM7q3GhG8fpvBIHJ2xuPkfascBaMY445tUAoK8wzhRcuCl2F5LvJtNHbA4jW71bMsAL2bPj4RX-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfwb10csZk07aH4nxbeVpKWlIUyfTC0pMwBEvr4Bpz13__lEqLB3q64RJwl5bVzsBo47LfzlFg5ttnu0zMjAsx1dFSSnt50u18hAcsBhFl-96wIXXgNv_O6NUVrgX7RKrWwklFDqac265gcisoYcy7MPplZnGYNd7iFswLA-_lLLXnSfMGWU2Ug5etCdVgSur0iMWF8FFHKs5LWSZDCTk8K-reuKwBe9qoDrUtzuYTV-SK1wsl_-3_EwHj9Meq6x-seBVwqHuYJo0-4sV8rt9zEiAd65uHW0SxiL3chwPk7pBqjJKtcSWIyJzLYDsB4trm2y4pn6YaBRP0hYFasZTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=HKDR_r6azbXwSw22mjiazUfIxjbNkLtwlfap0b-d42RN8qd839vzNPWqAsOJAgfieTvUDB1boFZf_yxOpMfLpyngt33OLBj_jtvR2Y_VQTIwaCv_cTLxVrLNi3g_RAf2DOPPeovKZb7YjdNenljW17TJ3xHUhbXUxJtf11zsyt7aGFGJgleJdDnm_9JXm0cwS4R2FkhlDhOkUhiqJTRGwGvbBf8HxvsKRfE-FPVmZ_EzKfM_Lv2eevVZn3yz1YldhLHZf0YnRB2nu4PLw9CopP2_JunwdLkaJxqH9Rs9AmNUWn7L3LmySygN2v_usXS849Mr2WQ0bsXqVb6XjG6kTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=HKDR_r6azbXwSw22mjiazUfIxjbNkLtwlfap0b-d42RN8qd839vzNPWqAsOJAgfieTvUDB1boFZf_yxOpMfLpyngt33OLBj_jtvR2Y_VQTIwaCv_cTLxVrLNi3g_RAf2DOPPeovKZb7YjdNenljW17TJ3xHUhbXUxJtf11zsyt7aGFGJgleJdDnm_9JXm0cwS4R2FkhlDhOkUhiqJTRGwGvbBf8HxvsKRfE-FPVmZ_EzKfM_Lv2eevVZn3yz1YldhLHZf0YnRB2nu4PLw9CopP2_JunwdLkaJxqH9Rs9AmNUWn7L3LmySygN2v_usXS849Mr2WQ0bsXqVb6XjG6kTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=qaMW9txKHdR5UqK0QK35PmtGMmETAOjmkOoMWrERy4SOlI6qyJ6kqKnYgkHrLCyLBjRbqYuP1Ye84RmK_MybzxNgG7jwZ8hGJDm_pVQy5-fuA-SWd2vrZMZdvWdiVu0Ib39s284bsRIPX76nhV7NE2G_2KIDAN8-kb-ICqtshSkS56qNo3_o-3wDL2C8lc_ejjPBw1wS6PFrH0qTx7PHvTSHwPvXVjws44OjeGdl1Mn2_JLI0SQUsBgv1Lr-oYDIntKNb1nOPrd5tFtIXy4oeApW73yJCrcVJ0o3k6KwZ_O5DwrxZvewivvPYYYK5TPsv4DT4HxS6J7eBBWtCfd4kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=qaMW9txKHdR5UqK0QK35PmtGMmETAOjmkOoMWrERy4SOlI6qyJ6kqKnYgkHrLCyLBjRbqYuP1Ye84RmK_MybzxNgG7jwZ8hGJDm_pVQy5-fuA-SWd2vrZMZdvWdiVu0Ib39s284bsRIPX76nhV7NE2G_2KIDAN8-kb-ICqtshSkS56qNo3_o-3wDL2C8lc_ejjPBw1wS6PFrH0qTx7PHvTSHwPvXVjws44OjeGdl1Mn2_JLI0SQUsBgv1Lr-oYDIntKNb1nOPrd5tFtIXy4oeApW73yJCrcVJ0o3k6KwZ_O5DwrxZvewivvPYYYK5TPsv4DT4HxS6J7eBBWtCfd4kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=tQOQDhOHSvI85cyN6TWCtTHNzSov7FWCX1HVJcc37vSCiVjzspsf2JFEhATAo12Pl7q8tIdnzj0AzbQXBF3ttiM7kTDpogltu_qkL5qACOXfecFq8PSSPGJQkWzK9aUyxAHWmKY0s7NmQ_PtkHiUBeUhjAynLuNTxL8RqmBKwySwI94DHVK0nUXHD8akzfOZkLN7DthCYy8l_qYTzBDV98CooFaNwAdK_S9VI9SxjLnM1RpeLIaQYVEZ9HQxKSYq3xhx2rXe7H5YAf6z8SziWSsVl5_rCkRlHO-VnU91EiCqwPAaDimjdXNn1LXL0IEmHgPFoF0Bq4zuu8naxw34IyYYcZQ6bG4a_QeNSDYsWvWM9CZmdFhzozs7hKErBDPSvKi2Kg8T6CsUHgjGcpp_IzrpDdmvRlx67kwqaamuyrjz98OWr32-pk5kz6Fw2vu1yAgpYtqmmG1snMGgwcX9t1C3DYqX-mudqVvSpyCqrScRuvEilpM77ngDo1opf4vCzJ5PnhOWbmRyhTNiBDttcobuPv7Kfa69Dn5pH7Wqf_6xBjLayuNcpkK8iZAQVFX86-H0hGWmm4Em52H_kOFOQjuzpMi7EKp-RVd-UT0OE0AvBRu4pB_VwkKefYc0ij-OmUQwQP30WwZvOr4POqEYIDUX3GjGOri_gbN5YPItJA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=tQOQDhOHSvI85cyN6TWCtTHNzSov7FWCX1HVJcc37vSCiVjzspsf2JFEhATAo12Pl7q8tIdnzj0AzbQXBF3ttiM7kTDpogltu_qkL5qACOXfecFq8PSSPGJQkWzK9aUyxAHWmKY0s7NmQ_PtkHiUBeUhjAynLuNTxL8RqmBKwySwI94DHVK0nUXHD8akzfOZkLN7DthCYy8l_qYTzBDV98CooFaNwAdK_S9VI9SxjLnM1RpeLIaQYVEZ9HQxKSYq3xhx2rXe7H5YAf6z8SziWSsVl5_rCkRlHO-VnU91EiCqwPAaDimjdXNn1LXL0IEmHgPFoF0Bq4zuu8naxw34IyYYcZQ6bG4a_QeNSDYsWvWM9CZmdFhzozs7hKErBDPSvKi2Kg8T6CsUHgjGcpp_IzrpDdmvRlx67kwqaamuyrjz98OWr32-pk5kz6Fw2vu1yAgpYtqmmG1snMGgwcX9t1C3DYqX-mudqVvSpyCqrScRuvEilpM77ngDo1opf4vCzJ5PnhOWbmRyhTNiBDttcobuPv7Kfa69Dn5pH7Wqf_6xBjLayuNcpkK8iZAQVFX86-H0hGWmm4Em52H_kOFOQjuzpMi7EKp-RVd-UT0OE0AvBRu4pB_VwkKefYc0ij-OmUQwQP30WwZvOr4POqEYIDUX3GjGOri_gbN5YPItJA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=MUowTHb5QRWqBCc8VFtxWGMzQSXAEBilJfwf14QFJ7ommMXx4odN5QJor3C05emZno48icxejycFhqG72XqWwuoGzaUg1-u1q-mXzhC-jazdskHh3LZk_UBp8YiP5SeiS6fx60LVnscF_-SFPuiDxWasiP3lWupt7ZvKBfh7wy2pmHYmGn9AZVkk1-s3oH8W_IM0wbB345d3jpCkiHq8B5GBYaBluqC5Nh7QjRQCGTix6Tp0SpTdEnc_ld5hk22iORqtuiJk6cwVLSXIVwbH4IlZAcA_N3jdUxr2wfRqKogN0qzfXmdd9mGqb8zbgYkBI2oJbbc3K4peXPeEGBd0dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=MUowTHb5QRWqBCc8VFtxWGMzQSXAEBilJfwf14QFJ7ommMXx4odN5QJor3C05emZno48icxejycFhqG72XqWwuoGzaUg1-u1q-mXzhC-jazdskHh3LZk_UBp8YiP5SeiS6fx60LVnscF_-SFPuiDxWasiP3lWupt7ZvKBfh7wy2pmHYmGn9AZVkk1-s3oH8W_IM0wbB345d3jpCkiHq8B5GBYaBluqC5Nh7QjRQCGTix6Tp0SpTdEnc_ld5hk22iORqtuiJk6cwVLSXIVwbH4IlZAcA_N3jdUxr2wfRqKogN0qzfXmdd9mGqb8zbgYkBI2oJbbc3K4peXPeEGBd0dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=N-v5tiDoLXXc8h8Yh0beKKVdnmNSmgeKjnHbvBi9ok-YK2RFRr1zVLI7hgb6fNxGh2UdQebHUAR7IE7kUH-dW6ST8l_plFNyypGcRD_DYDfEmYS7j6qdm-ENX_JZ6jZSurLsFHzyU1apVnClP-aSZks0JGcrTsY2e_5J1blOWpfKDQDXAeAon8gZFkQOHv61SpjKFe5aIiJlNcrY-wpViTn7TXKvSChAx8x6yct6TtgDK_QDSQTGClxYz5FBQYob1BWsFUX5J7VmjJm_qqHHsAjRnirLs7MhMbUZDkCudPsQpLPD02nVzfYc33iFBrqYjar37nOtxdtEGNEiFyYzTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=N-v5tiDoLXXc8h8Yh0beKKVdnmNSmgeKjnHbvBi9ok-YK2RFRr1zVLI7hgb6fNxGh2UdQebHUAR7IE7kUH-dW6ST8l_plFNyypGcRD_DYDfEmYS7j6qdm-ENX_JZ6jZSurLsFHzyU1apVnClP-aSZks0JGcrTsY2e_5J1blOWpfKDQDXAeAon8gZFkQOHv61SpjKFe5aIiJlNcrY-wpViTn7TXKvSChAx8x6yct6TtgDK_QDSQTGClxYz5FBQYob1BWsFUX5J7VmjJm_qqHHsAjRnirLs7MhMbUZDkCudPsQpLPD02nVzfYc33iFBrqYjar37nOtxdtEGNEiFyYzTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8FXaMSxYi4RKP08KLmTjqUAV8NsihlkHqr84LWghN59pHJ5ogPRRV647I9mnP9JlgAAJ6BMVPqcFNzILzGxp4_YfINHvSdhcHJdTdbM-hD0xQTM8fSnmHUEQjgl3ToOD-u02Z2ZnNwF8b5jH3fKvCy2UZZeLhkggUNgf6uBQBAjQQihNH2eyovN8mxiSMXZVZQsQmjr7m2KwbGr7H8V2u1GlmZNnwXI4OjqqaGZtnOz0SGIr0fuhx_1CGmYyZ0kMRYxXy40b38GlrBjLBIkDaq-uWpBU11m0c3pqLt1tAMdzCY7byin_tj5TwTwzAJ6ATELq4EMLFyrIbl9PGKZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gUYorEdn4dDMWzmWUhIer0erdw-_frIKpZQaPAhBdg6OPZZ5gjNjWD67iu14KsPzLAZegfsmjqVo-fnzYxO6jBSaxfjz2wqyAUjrtvGV-jgJOfuRylbPoVxQ9A1dK73-wGxTqao0Emz_80GVXz7EkI_l_At6mJAE07ohmvc8cyW6ekfBBPE9iNi3n-Hns-Izi__L62lJFwwLxrK4_Dek8rQCVMdVDv9mv-gjAy48HhWxAuAz59DcVSA9-aEqdvP4EX1cSKMnPQvrs0OKXZ8IlV4G8Ke3SHVqeStici9KpZDuDbY8edF7vuEVhMu_Jt-eRbczTq90WEebkqfdbkdoqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=CJwp9kWGqB8qmgD9RpQ5tIFkmH-aj-_KN3kXoA2KWZhgTPJgV5ee40Kpp9lLGNaT7BGDB3l6C0a7rlPJXS3RH3JS-0jNJxXbAWORY4zQkK8beT3QAA0_tIKb0M1CtWsbwyaKhQaE_Z0NK6UooXaumeoN5d8b9dqVSYfvX6E6RAXEyZzoYiOJWMTtWPECaIq9Kj01PyLiTdHNFbN8lAEXzEa8DYCW77LNG_OdKAvSupgkZxJ8Iji92YM0c00B37ZAzMFktyP3ZEX01ICqBr3GcCrNPfCwK705nn2pG8XFj0M9dYppowaNwZY4CPWR3_ceLhrLPY6BbsF54ulwSlppcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=CJwp9kWGqB8qmgD9RpQ5tIFkmH-aj-_KN3kXoA2KWZhgTPJgV5ee40Kpp9lLGNaT7BGDB3l6C0a7rlPJXS3RH3JS-0jNJxXbAWORY4zQkK8beT3QAA0_tIKb0M1CtWsbwyaKhQaE_Z0NK6UooXaumeoN5d8b9dqVSYfvX6E6RAXEyZzoYiOJWMTtWPECaIq9Kj01PyLiTdHNFbN8lAEXzEa8DYCW77LNG_OdKAvSupgkZxJ8Iji92YM0c00B37ZAzMFktyP3ZEX01ICqBr3GcCrNPfCwK705nn2pG8XFj0M9dYppowaNwZY4CPWR3_ceLhrLPY6BbsF54ulwSlppcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdQNwln3PlRxHee_lmk9Yyal39wf07VhJ_U0WI29_zKvNCWGu7RwsYWXKwiLcDzj_dbXfa4gm3Pz1-G_nnfumbLFV9Q9sM9ioArMFl7U7LAiLsXor8Z_-eB99RpP0jO-y0J7qzIDlmL5AJLSw69eu23djj_1U3GQ0xLGW4GsokIey7cx605xV91xiwQfAzBi-n_PJKwtZT10n5nXH0IOSOVaLRxxj-NnlZgIX4p_sdhIk6NLz-ldJG7-AbUYpKHa7JfbuzaW6BmbtScY2V4jQrgnC5LnKgHY9kYTJgpI0fCnZL6FJJPTM7SiGNMHCREvgKQ1EycogodtIsjB-lMarg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXvXmpc_L04gGkZFHPbS6r2TxHdYd863YTutvp6rko2VMJgTx4DPZ0n0i-CmIREoP_p9DGbFyJHTN3eNPVr-WzxZK6t9nhenYgx_w0xQDTViiADMXwgf6MOW06f_XzjE2egPDFmyy6aw5KVnWWpGmnqrXhYqeyPejyse3BVTrOO5j9fCTo4CyWGon0jEervjESUprRHggnO4-i6dpxNQ3zL7ZD8jsfvNETMGzJiTNHzrEmYwfHysi_5xUk8ZnLkAuuve1b64rvhXvdpjjMd7iv_dZtfoPIbueyXhqoO3l8G_hnjmksNNtJHfoVwquWWPMyKRuKepiIyFapkKt74M4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DegcVG2eKtizDeWx9Ok5GPsyj19wZKtc7iHw0k69yDD2p55gO-pI4awyNBsnyiigbiZfOF3vtOFyCe2qdGVTVXox5KNaUcBjoPTmKmdoEn1NWg0nhdShTGLuGTZdJ1wbsBnT1ttiVmTNl5_pRJ8gTpUfMv3sEKtisoLHEXyz48w1atsuq0Ay2s5BthTtlnU_yrxJwQfjzadRyZL57bf5-9BHUarYPBnX5WLKXKwizhLhsh4VciIEwsMfks9NkgXayOB6pMJrotoSrr7sHnlcPtXsUJscwzA0YL8XE4YJf3SUiCA65PgViw_pFmU_Oj0lJ8_NKrCB--3E_139FCwH6w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hg0nRtOsmWVvrs50Ult6rxDu8w-uCY2o1cVMbRCyQShvmneZpxJSgLJNiFSOlTbDZvsOFThEmfetzBD3xWpVsR_47JS2kJRQ_DBfRvqnxkbZm2jr6JSmcDfb-7tn4RZ7vcmjssNDQ5bpDww5MridplLWrfWhwDlinrfDznWR9hVR1WSNj4-xI9sJQysFw9kRjZfTX5hcRXoHmKVdcxFTmd0Kb3e-fd_g8b_M1f8QmJTWfQ4go4mevTEkmEDN9Fc0pE7JmeQuL-U-RT6MRTiXx3w3uGr6CS5p6FWjlGwBRKOvBvxoLfI1a9RbRaj3Wj0lR-UvZokc9yw0hJRzdbMhNQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=gQUWZaT5o4gijqalp6vydPVO9NzIWz9-Hj_HG1zpzCpl95NX8wZnkhRphxuqN2T0vX1Kfvn2a8W7DKeqzx7XCe0Yx9szF-oH8povmqYq9P-ec-Mi7qzKKsL9mz7A_ucmAxoTbkSm2ZTVqwhuvf7Of0BF3IKfjo8gbw6qPnuJZhnAPqWux7oKYAi_Q5840fA4nm7rFC1Y10fMX1nS5sBS9_9N9TOvVNugEgBcihqQAANGyL0Tej2CVUCogeKTQvFy--l5MyPpLMJ9lJMKdvTnp9Vx6nGUR1sb_r-asTVNQkh3-qEjHB3j8oH3I57MEVd_5XVn97_MAERAlU23E4NuOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=gQUWZaT5o4gijqalp6vydPVO9NzIWz9-Hj_HG1zpzCpl95NX8wZnkhRphxuqN2T0vX1Kfvn2a8W7DKeqzx7XCe0Yx9szF-oH8povmqYq9P-ec-Mi7qzKKsL9mz7A_ucmAxoTbkSm2ZTVqwhuvf7Of0BF3IKfjo8gbw6qPnuJZhnAPqWux7oKYAi_Q5840fA4nm7rFC1Y10fMX1nS5sBS9_9N9TOvVNugEgBcihqQAANGyL0Tej2CVUCogeKTQvFy--l5MyPpLMJ9lJMKdvTnp9Vx6nGUR1sb_r-asTVNQkh3-qEjHB3j8oH3I57MEVd_5XVn97_MAERAlU23E4NuOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=HSE1Zah0ewdklDX-W_GpwgwCDsBKwRmHpmZL35sKCIlleRDE2cmcDYIbRDGIvhWu3spOiI9SkubEbpJxxvg4RuzF5I9YZXP8WE9TR6ZVQ6n5rEdjRCwl6koA2QnD-GGLjslo5DwCP3olTEqtXupK11v7TXckkfgzjqrjhXwF-MrXB9XJVYF8vmlEPnLarxm9Q167j5VY0vSMZnJO_h-_3qGmzAan8G2HV5w4XBMKhFHV8qjts9k-VB9LgsPmtCIB2KiwyBm4tyjB6uLd8iOajsUW6G47efqtKUdwMtXkBmHKYBOTNYm0SUFw_cPoav627zvmPid5xFSIsxyXqaMHHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=HSE1Zah0ewdklDX-W_GpwgwCDsBKwRmHpmZL35sKCIlleRDE2cmcDYIbRDGIvhWu3spOiI9SkubEbpJxxvg4RuzF5I9YZXP8WE9TR6ZVQ6n5rEdjRCwl6koA2QnD-GGLjslo5DwCP3olTEqtXupK11v7TXckkfgzjqrjhXwF-MrXB9XJVYF8vmlEPnLarxm9Q167j5VY0vSMZnJO_h-_3qGmzAan8G2HV5w4XBMKhFHV8qjts9k-VB9LgsPmtCIB2KiwyBm4tyjB6uLd8iOajsUW6G47efqtKUdwMtXkBmHKYBOTNYm0SUFw_cPoav627zvmPid5xFSIsxyXqaMHHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mLsh32SJZKmJi2ZNFMgtz8mXAMjgTEGF1JPo3lZI8t5voxqUOpSOwkNmomF8tuqPcbIx2kM3j_RL8LJhQB2GV8rszQoaI5c_cr0k6pCDKlMJLjhabv9ipdBgInrtbu0XoqvanytzrC3cbiUYV8VnbZvhDzw4CSIN9dK1aDY40o2cQBNv_AJ5KYydPlOMnqrcuB79-Zaz10A_Z85RFyCxdaLJNIx3q5gJ1wTZnK6dN4N1fy73IS1HmIozqq0NS_cPWE5d95PY3vQCvUumJehdoR2K62yGGLHlHV7iQ-MmEtQ2lNKqgo8rtrXD1bj7pYW-qRyzhRHbgr0sNalOwduCHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=RQmqK2EWYDgpIhpmhMwSPghNaHoGaPm0eu3gW6ZrAqSQccmXjOgOl2_-axD2VLHTlyRbk6urRe18eP36uHmWzWympGa05fXmXfMZu8AweWQ4PyUHIHJPVkMoELD6bqteQW39AIwf9vFlrviKNoiKmpMpvbKAKt32KVuSGQiCzXR9JQ46FwRuI4dVf2A4ri3KnqLlLnnBji-OqQ8wbHKQXyniP-C651NmI8RwJsQWR7o7c5yef77M4TjqRnLApAEtD-9IKgulwmZcxvEmgMJdSw4m-BPzUHYwlPlEv6ZpTkbwt4C7h10PwBAgiiS0ogbpmzXqM_Fow6DvtUy6sY5Zvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=RQmqK2EWYDgpIhpmhMwSPghNaHoGaPm0eu3gW6ZrAqSQccmXjOgOl2_-axD2VLHTlyRbk6urRe18eP36uHmWzWympGa05fXmXfMZu8AweWQ4PyUHIHJPVkMoELD6bqteQW39AIwf9vFlrviKNoiKmpMpvbKAKt32KVuSGQiCzXR9JQ46FwRuI4dVf2A4ri3KnqLlLnnBji-OqQ8wbHKQXyniP-C651NmI8RwJsQWR7o7c5yef77M4TjqRnLApAEtD-9IKgulwmZcxvEmgMJdSw4m-BPzUHYwlPlEv6ZpTkbwt4C7h10PwBAgiiS0ogbpmzXqM_Fow6DvtUy6sY5Zvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=AiVCVN2q9bEBDbzSesJ3475oF5LXTiWUVwHrqYVeFujqqHdS8LJaSAohwmtjSt8ZLOPJUUYiCN0IdWnfdTQoMYPTm_dfE7OAt4FVrTMw5ApvH_jGXF5xZVmaJMVcNHjT7y60NKMQ5YPwrNWvKFWXCLVR_WJfLI1ZmMKXUXuOLudNi_tLB_b2zGXjUnVtLjz2bYZM2-J2vnx6ohyxrffYX4l4GReC0BH9ErZCSBWQ0vpenerwCFu71jbfFzC3TDhRuDkqmCYL4uPJDR1TtBibJn9FrA1KHZ0BL9cHXvWB2eMoBalFMZbY8rGkH1vY0pqfwWU6SdswNjNm2EMOcBzv-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=AiVCVN2q9bEBDbzSesJ3475oF5LXTiWUVwHrqYVeFujqqHdS8LJaSAohwmtjSt8ZLOPJUUYiCN0IdWnfdTQoMYPTm_dfE7OAt4FVrTMw5ApvH_jGXF5xZVmaJMVcNHjT7y60NKMQ5YPwrNWvKFWXCLVR_WJfLI1ZmMKXUXuOLudNi_tLB_b2zGXjUnVtLjz2bYZM2-J2vnx6ohyxrffYX4l4GReC0BH9ErZCSBWQ0vpenerwCFu71jbfFzC3TDhRuDkqmCYL4uPJDR1TtBibJn9FrA1KHZ0BL9cHXvWB2eMoBalFMZbY8rGkH1vY0pqfwWU6SdswNjNm2EMOcBzv-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=iXTITiVE630UeDlgaVEqhOUOGbf-cw_w6J8LLzpKiKJ-z8dr3G5RZ3rl-_ROy_lFari37TGSkdPHIffJDrCGe04eTfuIKI1Piuu5Kd5wjGUPj_ovh_q7WRi5c810nTPwjDWaTPJOqvIDdL8lCpM2o190KcMI_ZGLta9Fd6Pr1BbnFEKvY1eDOk7EwEEjqMo-CaN7Yt56bGR0UlniIrJo5OaRqIcebfMWaY4I66SlzDGDcKHbyXP4m8yGD9ubpe3Noi8jfqWOR0twj6y4fYMH3a94jIj2N47zwvB821EXg7PXc8MSDzRXO5mBNjx9EEVh2pxX_i8Ent0Ee38L6A-gWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=iXTITiVE630UeDlgaVEqhOUOGbf-cw_w6J8LLzpKiKJ-z8dr3G5RZ3rl-_ROy_lFari37TGSkdPHIffJDrCGe04eTfuIKI1Piuu5Kd5wjGUPj_ovh_q7WRi5c810nTPwjDWaTPJOqvIDdL8lCpM2o190KcMI_ZGLta9Fd6Pr1BbnFEKvY1eDOk7EwEEjqMo-CaN7Yt56bGR0UlniIrJo5OaRqIcebfMWaY4I66SlzDGDcKHbyXP4m8yGD9ubpe3Noi8jfqWOR0twj6y4fYMH3a94jIj2N47zwvB821EXg7PXc8MSDzRXO5mBNjx9EEVh2pxX_i8Ent0Ee38L6A-gWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=DrANi_fr8DyBTvApCTy1WD5RalcdEf6WTR6CWa7itj9fwjcJ3d42SCkV5UaTzkyco0noPCLezLv8uV9Or7J7bEf500BUYYtRY3EwC_79yGpknzuxkKEc0sj-iYjekGRnAwelWttecK1oKgXx6jFtZdfCBEh7rbLWj6mDxvndncVT2b4Fivf6ix9aVcd30xq2tIYgeQzZelB_CI9jM4ppqs1VOhpxjX1eFR6HxI0Ifu6Us4Kz-zgTyH431j_XWTOxbZqtw6-3fors15bnxSY8IscqyL8itV9ORCnLYJ1xdkX8jdgmkeJ0josPsbq3zdTmuJSoGXxsrT0sIZ7hr3ONcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=DrANi_fr8DyBTvApCTy1WD5RalcdEf6WTR6CWa7itj9fwjcJ3d42SCkV5UaTzkyco0noPCLezLv8uV9Or7J7bEf500BUYYtRY3EwC_79yGpknzuxkKEc0sj-iYjekGRnAwelWttecK1oKgXx6jFtZdfCBEh7rbLWj6mDxvndncVT2b4Fivf6ix9aVcd30xq2tIYgeQzZelB_CI9jM4ppqs1VOhpxjX1eFR6HxI0Ifu6Us4Kz-zgTyH431j_XWTOxbZqtw6-3fors15bnxSY8IscqyL8itV9ORCnLYJ1xdkX8jdgmkeJ0josPsbq3zdTmuJSoGXxsrT0sIZ7hr3ONcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CgGiB8oNwdnS0YQVjOm3vIRD6ZVvcdBhiCyhVVwpjsyxafu9cxEQxEVC2NuHDM-l9-WYNdBekVgXxmf_G8HJw9UMmFU7Ia37SQOzxjCnpGS4yz7hS--TnpKlrZ7gfroUSsjHnpfls4FxovNjVo90VQjX5_TJgI9r8as3feWBwV4SuzfGYu_jGgSC1OLTG42tDrF-sQt7oxwAXJ8bvdzEOyCStl2T1Wx1ixHR6ExLiMdT47Q82Y0ujvkJQdVVbhgU_nVaY5vtK3BVJHQB8j63kG_61J6QzK2NwKo33SyCk1JLPMFXNc8lOKgu6KBGD9WB37sjIIyTvnl5Gz04qHwl4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vh70nLrd1kU4k7YafW4JP-aHIYPOIBfA1iMMec1rh2OmYbt0ExFjBwCt7Iuun_u3MIv2Ehgyui2EiCTh9dnlNmvCkcA4Pz_v2aYy5e-9EPguC_OQ431vUJ896ey8inn0Nv94hnFvDuCup35AUk-LxSU4Y41eRdSIAJVPi_bfBMWVoaF3-NXMyUAGv1eq9dH87FRNdmhS3kv8J8hFGQ2e9Sq-39s9LACW_UijMru3vY2-TdDwy1stBNc2CQuawscLWYVfdPjZsV8XkatQJvusRUsEza-9zMCeijWVEa-mEvlJZ0zMa9O1WcKFh3nxwycBde2oA98t6C9xck2mUFOcPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=VUpqZUpd9hkB_kayTfncOyTsWSKMnvodavJ5HCQyzHMoB5TEiqwLIcoeWHR0gBue16DTXIPzPknHiS7OhkST_m2e-UaLGeHHBvYZHT37O0wpM6VSOfaUKMt--BdtbbkhFz_9cxhtYR-cpvwu6v3wpWymiao7GuB7mk22elhAzI5qe2fJAFyGrk_VgiJlMV1tUiQDzs2N4Mv_69k4__rYszOHbLZIBn0ms_jfasg2bgY4M6UiCGeY9P6fry8CuUQV_Nev3YAU7ii9o5kfwI_PgSTBX9ABK_NDzMcI00kr8om0UA4lYWfugVZ_S90BqR0zHQv163WUjqiwtKklxGd_Aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=VUpqZUpd9hkB_kayTfncOyTsWSKMnvodavJ5HCQyzHMoB5TEiqwLIcoeWHR0gBue16DTXIPzPknHiS7OhkST_m2e-UaLGeHHBvYZHT37O0wpM6VSOfaUKMt--BdtbbkhFz_9cxhtYR-cpvwu6v3wpWymiao7GuB7mk22elhAzI5qe2fJAFyGrk_VgiJlMV1tUiQDzs2N4Mv_69k4__rYszOHbLZIBn0ms_jfasg2bgY4M6UiCGeY9P6fry8CuUQV_Nev3YAU7ii9o5kfwI_PgSTBX9ABK_NDzMcI00kr8om0UA4lYWfugVZ_S90BqR0zHQv163WUjqiwtKklxGd_Aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Zm8u8BoANavuerK99eBajHHeNVC_vf-g6Rpg9mC6mBbk2oJWBRlhDWI_yd9KVzcqPGjPXi4AsGC3TcC4XdGjJPgWB1YTBSC8yxz2XhjQJkeJHpojfaM0JQ8untLOqhfF2IEN9Agox36oxAhZK8I4HIm0T9unf0ogP1gtCIr1YtY4KxUascIUA6zmu-X51Tn-mnhhNC4L4eY6uE2ykYOl736D0897_vu7FfDJyBg1EhqN_LWfD5UAbdBaw_OeWHicQnyI1iUkze88rdraCHDRhQRYKc3uHG69xfE7M9ydaIWSzvH8Dw9P2pNSytN3LcdK5n1LgFdzefSmXHoDOw6S-o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=NcndDMkcAfVw4qZaWqzAIyzTRudl6vpdLj9YvVWxQzIpPntqhPMSrrEpceKYZgtzSe4cA2RlmbyUYXMK7_EaFN8wtUDh3ZuwQjqWnblkjOWOAB31CbB9yk8RZUX7rTzLIbiFSIyRMzNAqu9TsF0CkQS1NlRZtsbYX5140VxKQl8RUi8W9jTq6CbjJ-ALBoMYIk4uS5PWWJl_3Hb54ZmAoBbQXYLAVltm9ssov38ypSpoxeRJaSr0glzJuM2QWoVyoogDapNUBvtX0zc4ZbuAjtYX-e-yrs6fIuYSAeIFo7qHLX9LPb1sfHqFqleQvxDoxlHtf9CSHlmAfETsVxAD9Zm8u8BoANavuerK99eBajHHeNVC_vf-g6Rpg9mC6mBbk2oJWBRlhDWI_yd9KVzcqPGjPXi4AsGC3TcC4XdGjJPgWB1YTBSC8yxz2XhjQJkeJHpojfaM0JQ8untLOqhfF2IEN9Agox36oxAhZK8I4HIm0T9unf0ogP1gtCIr1YtY4KxUascIUA6zmu-X51Tn-mnhhNC4L4eY6uE2ykYOl736D0897_vu7FfDJyBg1EhqN_LWfD5UAbdBaw_OeWHicQnyI1iUkze88rdraCHDRhQRYKc3uHG69xfE7M9ydaIWSzvH8Dw9P2pNSytN3LcdK5n1LgFdzefSmXHoDOw6S-o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=vuDyNaWtlysCUIibh80hQU-20V3lXt6G8XKgNKuQJWgMqwWp4V-zgY2ch7Phr7XNeVXI7CHVInUYY8rId_LoxaIIYc-cxcuF0bHl_k_5bxTi1T5uO018G8rP_RKcApB4tCM5OSxZjHEgkBaB2bk0mQaqS848X7FTsyJD7wKWc4ciFCUt7QOo93GX2uLeeoOkArR2R_rUJbsGsZGfe8CfcB7tvhrG0Wq1g-Wfms_EqK3QXjD_c7musRMYy0domlSAwd4jcqSXWEMj6AP4zRiYVpif19UmYv9pW5p2c3U13tLzWhz9RsIZwcfIl9YrwHYArDI9M0sQyEPHnvjkihQIWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=vuDyNaWtlysCUIibh80hQU-20V3lXt6G8XKgNKuQJWgMqwWp4V-zgY2ch7Phr7XNeVXI7CHVInUYY8rId_LoxaIIYc-cxcuF0bHl_k_5bxTi1T5uO018G8rP_RKcApB4tCM5OSxZjHEgkBaB2bk0mQaqS848X7FTsyJD7wKWc4ciFCUt7QOo93GX2uLeeoOkArR2R_rUJbsGsZGfe8CfcB7tvhrG0Wq1g-Wfms_EqK3QXjD_c7musRMYy0domlSAwd4jcqSXWEMj6AP4zRiYVpif19UmYv9pW5p2c3U13tLzWhz9RsIZwcfIl9YrwHYArDI9M0sQyEPHnvjkihQIWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMn0LjWlYk8tXIsceaXHS2-uaGpAPTaZOWX16Jwi1astOb1SbEurzMwXweOo9B3gsRsbnI5ax5E5DUm4If1sMNsiFVNiwgbe5a0O1aVhIIPCmD-KmYmw8__UAB5_PKDXgUHQu22x-B-65_KPAGQ12ZRvR0g37GeFMXIiQ1d1SF6DzfjeNzf-X7j6-P91dhdkItSa8BsblCULNa8AjXcPw7fTDh8ooXd0M12OnC6Lgvvfs6vhAVUXzZqmTUnAeNyxzKemcUWRD-CWLve0_cNQgQ7XJe5w97F7GhgOKCcyDMhURJtcMUxffBhXQ-6daSCnXuWWJM_blkeqK-BZLvOMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=gtZHYnuqM1_x8wMQSd1iI2DGfMiz4DiavU1gubzHiNY0G1QZDP25aeUxnmISPngMtnu9f6F9Iy-FbrHrC9Y1ik-4c8Bzn0AJ5WxCJHHCl7cEvoqlsxz8FcHniO9mS-JBU9w2whCyWy4Gh5DU3w31bdfkZvr77RmhzPn5I9ocpzx9myynpRroyrfMRrpEBEgEyTCsTbxKUTUjzV2jm2Z5Rrk8g8yK58zkbzTARPta8jLoN-YePybdnA_U6_wIoE5dCkoe8atR2Ot0bCBi_yIrl8ujtx3iDRX5zUYse0m9ytvjT4Aokt735CAMLwNI9slKq1mArYrfeCkgIQtSbu8C5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=gtZHYnuqM1_x8wMQSd1iI2DGfMiz4DiavU1gubzHiNY0G1QZDP25aeUxnmISPngMtnu9f6F9Iy-FbrHrC9Y1ik-4c8Bzn0AJ5WxCJHHCl7cEvoqlsxz8FcHniO9mS-JBU9w2whCyWy4Gh5DU3w31bdfkZvr77RmhzPn5I9ocpzx9myynpRroyrfMRrpEBEgEyTCsTbxKUTUjzV2jm2Z5Rrk8g8yK58zkbzTARPta8jLoN-YePybdnA_U6_wIoE5dCkoe8atR2Ot0bCBi_yIrl8ujtx3iDRX5zUYse0m9ytvjT4Aokt735CAMLwNI9slKq1mArYrfeCkgIQtSbu8C5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=uj4CFNB4UAeBcujpjJYwyA7zzY2GWbTiOOlBDs5oE2a-Y2PhQj3_mEsnKQLekAiCUBqPIHmRi_lAOhV1SQtmbmQnfG0dKVDUJy5hgty9mdb6jbFpz72tjGeTKTExqV2Ju04T1tBVj_CXA2Uad912tFpp5FyDN35rVxND7W3aJ1aJAzShH-0Ioi-a2H_Ug9BdUeFNNjdftxi5yM4JscyEOIAEOWzWVgisyhPHrqbc91b0b84UsEmNr53p_8XXMNnOeUxnNE1E05uOYmNsx3UyTfjmFHEstrdgGeblaY0fn7M9mDJiDqxWwjBF52B1zicEVQQMql0vkQhLefUbcC5nJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=uj4CFNB4UAeBcujpjJYwyA7zzY2GWbTiOOlBDs5oE2a-Y2PhQj3_mEsnKQLekAiCUBqPIHmRi_lAOhV1SQtmbmQnfG0dKVDUJy5hgty9mdb6jbFpz72tjGeTKTExqV2Ju04T1tBVj_CXA2Uad912tFpp5FyDN35rVxND7W3aJ1aJAzShH-0Ioi-a2H_Ug9BdUeFNNjdftxi5yM4JscyEOIAEOWzWVgisyhPHrqbc91b0b84UsEmNr53p_8XXMNnOeUxnNE1E05uOYmNsx3UyTfjmFHEstrdgGeblaY0fn7M9mDJiDqxWwjBF52B1zicEVQQMql0vkQhLefUbcC5nJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=rJhWswe2ULBuKlKI-VG0tlBY1iH-UpGgUwrAhy_vkhAqsWuiAfDyOzzk5ar3l0GuPTe_w54CsZSlLk2pz25dvLoCv6E9Bspsv9R3yIlUo6u4lcn6Fsm_cGRCA0xfSwBl0TMQ3dOK5nZNjieADUVAVkyKrLkMs3gg0eSkRK3nzdo4g5FjSgAZlrHgR9n2PvLRduqAzuYWsdvrlm4YiQcCF1OwEfFt0s5jUMStInNK7j4qMI1rc0HkEZd9rh3nrG0gfn7RVIKxdieOkVLwgOlAltMC9fIa5NXkxthAYlY7MRvG8HrGZW8socfRItXqFlNmyKHz_-kAi_vt7d0u1ls0Gg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=rJhWswe2ULBuKlKI-VG0tlBY1iH-UpGgUwrAhy_vkhAqsWuiAfDyOzzk5ar3l0GuPTe_w54CsZSlLk2pz25dvLoCv6E9Bspsv9R3yIlUo6u4lcn6Fsm_cGRCA0xfSwBl0TMQ3dOK5nZNjieADUVAVkyKrLkMs3gg0eSkRK3nzdo4g5FjSgAZlrHgR9n2PvLRduqAzuYWsdvrlm4YiQcCF1OwEfFt0s5jUMStInNK7j4qMI1rc0HkEZd9rh3nrG0gfn7RVIKxdieOkVLwgOlAltMC9fIa5NXkxthAYlY7MRvG8HrGZW8socfRItXqFlNmyKHz_-kAi_vt7d0u1ls0Gg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YCqvO_Vh6-v7S7m9UYPDUYVSvh0aDebaOe06nsueQjjLHHIBbGj40Tv0GbraAf3S8b296m4SL8b7zrW6rSKrXE7O7QjhLvVSErwat7vtCMCQSIMy6fJgZxUENduAbr6FjgPh8Pl3VnObN18pTdI2jsw5QxXs6xyRDSHgVv4S4SaEgLAH_X6KwDd0GOORtco30zzM6Cr-fRrsathmc9uJ4Cfwf2739rclvruYbkjouDOKanYbJll0hHqKUEnNJPa8TGy0YYOnl1Okf1k0_PueOgdIYENZGfAiI4RaacFWn1-A8cndc1JUCvonMYyB-Elv6hocErYi4D0xI7Q-rXGd8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=YCqvO_Vh6-v7S7m9UYPDUYVSvh0aDebaOe06nsueQjjLHHIBbGj40Tv0GbraAf3S8b296m4SL8b7zrW6rSKrXE7O7QjhLvVSErwat7vtCMCQSIMy6fJgZxUENduAbr6FjgPh8Pl3VnObN18pTdI2jsw5QxXs6xyRDSHgVv4S4SaEgLAH_X6KwDd0GOORtco30zzM6Cr-fRrsathmc9uJ4Cfwf2739rclvruYbkjouDOKanYbJll0hHqKUEnNJPa8TGy0YYOnl1Okf1k0_PueOgdIYENZGfAiI4RaacFWn1-A8cndc1JUCvonMYyB-Elv6hocErYi4D0xI7Q-rXGd8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJEAptbiVjhc7Ul2iFVrZ73Gn1WHOh1JFunvf1-jEsGhrmdNP9nJGfYBmqWi5BsfqlvQ6cY1d6NjbAaQPZlzHKeDUUQ-eZ6l90T3fVd3cbBXQgQJtfByghn-aNPG2iPE0qRtjUJSc3Wy85EE0b-OVXtiWa8LKs8Fwl4fnDWJ03AItpFWHjdlFcu4InbYJUIhZEv_ljftwVFHeG1bmd_CYoUM6i3GLcHvvB0LeRUwyc-Dg2rg3H85hW7LIpq5hKgT10jPwPQo3v8PFZO5n0tmFcS705yy2oXFufmHVabb7UG1rUfhz3QqpwQJZFonB-UuWzsfQbCQHmhId0Lz8VEXGw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tIUJ9YbDT52QLXVsKJEaPl_PETMdJT_MY-gotwtl9h-Nvyl-STqmRq9y-lY16awJQyWbFAJDmZQY-L8Q43NHUNZZTfxrlgllUjvQf-uGptVy4OSQMN2P9Bk8YSMAdo30NS2ocBjwAWjHrIet0wcWeAXXwYZD4dWBdFvLxbpt9a-F7OxLTnT0R8dxRPgx2A588cth6_ysv-QwpWhju8aTRQpv5b-Nb8iauSqsMZou75ttT2bMut4YZEQAb2Zs8KL7ZRnWAWACAVkXvNTGSzHODj4n4yVkJGtVIXWSG-vhyvaej6Jn8-isLyvznckBe82tVH_HmNBgkwoD_7T6JSRrJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=tIUJ9YbDT52QLXVsKJEaPl_PETMdJT_MY-gotwtl9h-Nvyl-STqmRq9y-lY16awJQyWbFAJDmZQY-L8Q43NHUNZZTfxrlgllUjvQf-uGptVy4OSQMN2P9Bk8YSMAdo30NS2ocBjwAWjHrIet0wcWeAXXwYZD4dWBdFvLxbpt9a-F7OxLTnT0R8dxRPgx2A588cth6_ysv-QwpWhju8aTRQpv5b-Nb8iauSqsMZou75ttT2bMut4YZEQAb2Zs8KL7ZRnWAWACAVkXvNTGSzHODj4n4yVkJGtVIXWSG-vhyvaej6Jn8-isLyvznckBe82tVH_HmNBgkwoD_7T6JSRrJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=tns1xxvPS8TfBs5RhVSRz3J9mxxGl1Uap4D21BgO0vdvhg0vWVPLu8mwW_5r-UNtOzxGMwPuIzNiNWCl8CpqMBtMiulwy7YhuM3ys2myPw3eki39qMtvxYqXlz9PPz1lYzyYoRhw27U5rOGbNdcElx1FBji1LUR9Dcag58wXt8iVy4fr8DZLzKvJNzipRW8AKVO9_CGHnl7wKOhRyDQNRAaF9Xjhmhj8n1uXe2bPKrc8_bg1ASA1_5BO7US8uimNi0xSkYYSNIszlIIOJq1MyQXuwJil-cNWi9tT7MBHh6UpXlRYpuHITm014nQ2jhUOsYGb7EU4_VbFBkr81W3YFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=tns1xxvPS8TfBs5RhVSRz3J9mxxGl1Uap4D21BgO0vdvhg0vWVPLu8mwW_5r-UNtOzxGMwPuIzNiNWCl8CpqMBtMiulwy7YhuM3ys2myPw3eki39qMtvxYqXlz9PPz1lYzyYoRhw27U5rOGbNdcElx1FBji1LUR9Dcag58wXt8iVy4fr8DZLzKvJNzipRW8AKVO9_CGHnl7wKOhRyDQNRAaF9Xjhmhj8n1uXe2bPKrc8_bg1ASA1_5BO7US8uimNi0xSkYYSNIszlIIOJq1MyQXuwJil-cNWi9tT7MBHh6UpXlRYpuHITm014nQ2jhUOsYGb7EU4_VbFBkr81W3YFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-BrRNgu9iSQGUqRZUWoQWLpLeAEI4X9L45kFToTXdFzjcmL4vbONa3Xst8Q-t-2I_hsizgCkmCewKLMJMzGqs6v7dFkgwi0VVbrfGFnM4TWoJaYBGi6sXgDkoUhHeUd_2zxnt2Ue1WD5GelVRaWdM73etdZxPkNe2FKSaH0b1hVKTulKVioEMp4Rga_uW3PmgGP8hFGtSbX-QW77L6vDsBCdpoTbpUUXATAVEvvJEj9yEc0kNZ-PP-gTVw0xwMGpCumE4WwCWZTPbAvWu4eJAIndbZoaf5DSSQYz5S_fo0l-cOXc4VryjB6FYf-9hfjUNzDEPhL23gvYMkNtiAhsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MhmCbNQlnn6FwfZE1UztrVO5FZqjaGR9756JX4bYkG64-ctRqYa2Ug8DzXGMAS5vKhbv5uVuax8s_q5x0xmPIudEmnzeI0gXSsa9fliqEv5HFmy2deF6Bqh8DNh-7HVy-m3LcW450FaQN0xaBgqqCNXXg15s_fSjdISalYBIg456vMMCsZi-iBKiTF0w4C0iGBZ9h_Czf_3fwZQ8jpONkZs-1Hdk93n9CB3dnEcDDbgLRDrWlWVYPec55Hc9Ons3qvKuetm1NvYPdl5UhMKYZDupqlVbHeQw_2A6bEWs-qdh8vdEP1ZeXGZKGLnKdVOmbMAF_Km_EaFfvvpjsUWyRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=MhmCbNQlnn6FwfZE1UztrVO5FZqjaGR9756JX4bYkG64-ctRqYa2Ug8DzXGMAS5vKhbv5uVuax8s_q5x0xmPIudEmnzeI0gXSsa9fliqEv5HFmy2deF6Bqh8DNh-7HVy-m3LcW450FaQN0xaBgqqCNXXg15s_fSjdISalYBIg456vMMCsZi-iBKiTF0w4C0iGBZ9h_Czf_3fwZQ8jpONkZs-1Hdk93n9CB3dnEcDDbgLRDrWlWVYPec55Hc9Ons3qvKuetm1NvYPdl5UhMKYZDupqlVbHeQw_2A6bEWs-qdh8vdEP1ZeXGZKGLnKdVOmbMAF_Km_EaFfvvpjsUWyRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Df3-OwqVqbIgmfzifa8oJmrLl9CnI4hZ-Z9Bi6FrMHs0gnrPHyq_VH36sVFGMPX69e5kP-17MU_uStFP12UKFwFLRK-XDIVbHSHKEQdl8vTkCsT7OmvVNGn4Jyq4ybiuseOH57URTW4WUxu4dHsATP6zU9RLhzStu5twnD4iXUWzKaVGWQJ1VMRKnL9dOiQhmRmgIB8sE8QmMvXaKB0N6FkDMQ2Yb7TFpmQMGdx_mDWUdS-E5lv8H4jD9fwGzMdQHTjdysH7zoQnIOwQDkXCSRmVLKwAVLDnf296jVYOW3e8U-uQ67jB-2kjqibvYvvFse0z2pPDEg7nsILoPxHtJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Df3-OwqVqbIgmfzifa8oJmrLl9CnI4hZ-Z9Bi6FrMHs0gnrPHyq_VH36sVFGMPX69e5kP-17MU_uStFP12UKFwFLRK-XDIVbHSHKEQdl8vTkCsT7OmvVNGn4Jyq4ybiuseOH57URTW4WUxu4dHsATP6zU9RLhzStu5twnD4iXUWzKaVGWQJ1VMRKnL9dOiQhmRmgIB8sE8QmMvXaKB0N6FkDMQ2Yb7TFpmQMGdx_mDWUdS-E5lv8H4jD9fwGzMdQHTjdysH7zoQnIOwQDkXCSRmVLKwAVLDnf296jVYOW3e8U-uQ67jB-2kjqibvYvvFse0z2pPDEg7nsILoPxHtJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=aR0cEQLEacwvkXtJaO7L6RqloHQcZDU5rDGsIwx0O00877q3D_JGzLsse1lQsDCyGIQMxiPlLhT7d85vzZ_ZaYTYojX3eeSPLxWzPC9_zWgzsqKcDKWJ__n2ll5cE-j50G-T4nKNwSonioC8KQV0J-BLeErW6bF4SbBRz01dTObAdTjxfVDHbgf6iJTaTUKFuDGXccmzBcT2XeOcjpfUZT6LFRnEscQ8LR3CZSlnRahQI08SANyicgZl3aSQcOdSl91usRO7rWIVIuQpRYPWoQhhW4kbpStR_v_U_bfbFSRi5axSOedxq5wKIYLEozx_wlzyBzmUfRHWfdjmPuaTOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=aR0cEQLEacwvkXtJaO7L6RqloHQcZDU5rDGsIwx0O00877q3D_JGzLsse1lQsDCyGIQMxiPlLhT7d85vzZ_ZaYTYojX3eeSPLxWzPC9_zWgzsqKcDKWJ__n2ll5cE-j50G-T4nKNwSonioC8KQV0J-BLeErW6bF4SbBRz01dTObAdTjxfVDHbgf6iJTaTUKFuDGXccmzBcT2XeOcjpfUZT6LFRnEscQ8LR3CZSlnRahQI08SANyicgZl3aSQcOdSl91usRO7rWIVIuQpRYPWoQhhW4kbpStR_v_U_bfbFSRi5axSOedxq5wKIYLEozx_wlzyBzmUfRHWfdjmPuaTOjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o6-0p4BVoqwxyq0_ib813HmF5SX0_lu1boF7SNzC2Fr5jCUYeI0NPbbtpacGwg18NclPPxHXCgBUzlao3jXIKjJsZcvqU3uRcqkMCy5fvHSk--oQIgnyn4Rw3jQRc4WkAz7V4iZ-YcF6Yr3rEFgkews38ixKcTz1XqID29ycu2HQWyoqyJkJVqxBgC_iFKL9_LP5xWRCFYJGZgpP5Y2ecAP1EcP7j-GWMhktKi9lbhVFA8B-W0933UgpeWs9w5BHWU-XHIBEf-DCS2LzM8nOJlalBm4AKzk1x2fyKw0_q8A7KljKuHvg_UUelr1LfQudlKtqZ6gNP2Xu9hZA65nQjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MmIci66VuI8eivjIxKDhFS5Mkb86duwGbBoAAuU5qGUxsk1E2RFIenkDJdCzCXxAezu1pvowU-oJDd0yqEH-jEOnswiGE5-VbGqJkPNR4I1G3Fb38rzjkVm6dK1KpO5CwDsMH2J2-gLqFbbXv1sPPOvoGIv42g6yqrKThKTjrvA837Qc9km2VbfxCC-uS0YPZ2096N9aHr00pM7AT2lWwFyhc1MNFPyRfLPrkivlZZiaKfO-keyDd3Pq_YUxYSAyICLhfvmUGdeB2csYU80ILD7mQFbGHZIt3ix8yclD9MUQ2BPAUVAkI2dfMq8S3QQhF1YYZMy5cTnwXQ3gP27A4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p3S_aMe5rGwkahMIlY8xEBZD9O0Il33IvO2zmNLtdAX0a5bsYUPasP7xlEJUoNyBw-_COfWjc1M-6LksCfsr0b9NVIoeeJt2cQpZSMtCiGRmRuU49wUQ548XsgqeUwDYrkYrJHyHxgiEn08_5k9VXh0sfPKubLzlZM9q9wFrXRALX4GWIO0KFvIsYSRuYwEO4zT69SVQEFArvo90thJOMn_EXszFAUxB5uaeS5qDNMdraXf7uGUF5Cfvx94o0tK82NHyD0lhSxXlbRK5GPwaowcV3PbysauNH1ecPoRg2dIJPltXbmwi9FRC2y4Mwg6NqrchS_0LP9MJObLIexQD6A.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=SV-gW1XBabQNQW0eDh3alzHKXV2nrMAg69RKhJDT2AR7LbKBNTGILh8Eot3F5gJ44y1-6yr1cR0u-pYCrcp_W5tao-Q3BrwPVHZjmPDaOlwvEUKYRDZXq7UFOnbOjLk6A-0JfVtBuTbfsMbTfEkfGveP3p_E1t7GLygJXyhpBZcqAANBMsRDkmcamNf9kCeFCmgdOIAibMZSFj9Y0S_nKyLUEV0YEP_b8NPqzkMMRbfGa3ODEU8_IAwOrpDHBB9EkCwxXIBtKd_DLntYAZPXrDs0_J-g3o2N2ReXTjqATxuj7H5wa0HEyQSEjjjPtFCVrGxSjMbbHbfnwGKarofpNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=SV-gW1XBabQNQW0eDh3alzHKXV2nrMAg69RKhJDT2AR7LbKBNTGILh8Eot3F5gJ44y1-6yr1cR0u-pYCrcp_W5tao-Q3BrwPVHZjmPDaOlwvEUKYRDZXq7UFOnbOjLk6A-0JfVtBuTbfsMbTfEkfGveP3p_E1t7GLygJXyhpBZcqAANBMsRDkmcamNf9kCeFCmgdOIAibMZSFj9Y0S_nKyLUEV0YEP_b8NPqzkMMRbfGa3ODEU8_IAwOrpDHBB9EkCwxXIBtKd_DLntYAZPXrDs0_J-g3o2N2ReXTjqATxuj7H5wa0HEyQSEjjjPtFCVrGxSjMbbHbfnwGKarofpNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaXaQMKRZ80qbTJEGtML9xJJNBUqwXJtA06vNIvcaynVPpNs9Ehfc2Y0jXiPpt7g7tfYIP4t8Eqx0RqXARgiyi3IdnRYpzDeWd_B7r82jERME44R50YtaQyYNI05mHaoNVoTbc1z2rBM82kSZbyNmpZbun-r-i1xeZSN5FEBuG4jYyizPW-kAyNFXhJjGqsTWi8fnQRuH2tQ7P4IA_BBihnjZwVIX1FSBYwh4VhNo0ACfLhdnILiusrmxRF9PSYZeraT3zv1USnLddYp_bfzVkHKTuKFmOZ3kgypNAoToMlMrGsHch48VE6Scifp0KgUkOMaWyxbGqSVxBOdDyt2iMGk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaXaQMKRZ80qbTJEGtML9xJJNBUqwXJtA06vNIvcaynVPpNs9Ehfc2Y0jXiPpt7g7tfYIP4t8Eqx0RqXARgiyi3IdnRYpzDeWd_B7r82jERME44R50YtaQyYNI05mHaoNVoTbc1z2rBM82kSZbyNmpZbun-r-i1xeZSN5FEBuG4jYyizPW-kAyNFXhJjGqsTWi8fnQRuH2tQ7P4IA_BBihnjZwVIX1FSBYwh4VhNo0ACfLhdnILiusrmxRF9PSYZeraT3zv1USnLddYp_bfzVkHKTuKFmOZ3kgypNAoToMlMrGsHch48VE6Scifp0KgUkOMaWyxbGqSVxBOdDyt2iMGk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=uj6l2EAvrwVTXUED-6UWIgt6CctXrcptwIPcHGrTvQhARrxYJ9J_QmXxcwbl6mDubhGdle1yUs2XlW5iRdsYpM9vvV9zqcu9Wk2HKuHZnhSJ99TmXAuyhHPfTmtULDtzGkijS_30WdVTXD4zNQNvOdG7HRjpkuzTIBkfHUUrb9p1gfq__hDca7IlI8T-oCgyNPVrFvEElPN8PnTi3x20TS07UB2c8hTOki2kJuYUQRQ6Tkr7Ad1nYoJJsGXpjmMg6LGwX_Xk9NQbOQW4zt16hSZumAULP8pOY3zstV2FaGq1lfCZGw9xHK6fayeuWsyU2Wc26EXkqaaNTA4drRLhgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=uj6l2EAvrwVTXUED-6UWIgt6CctXrcptwIPcHGrTvQhARrxYJ9J_QmXxcwbl6mDubhGdle1yUs2XlW5iRdsYpM9vvV9zqcu9Wk2HKuHZnhSJ99TmXAuyhHPfTmtULDtzGkijS_30WdVTXD4zNQNvOdG7HRjpkuzTIBkfHUUrb9p1gfq__hDca7IlI8T-oCgyNPVrFvEElPN8PnTi3x20TS07UB2c8hTOki2kJuYUQRQ6Tkr7Ad1nYoJJsGXpjmMg6LGwX_Xk9NQbOQW4zt16hSZumAULP8pOY3zstV2FaGq1lfCZGw9xHK6fayeuWsyU2Wc26EXkqaaNTA4drRLhgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZpZmVObErcwTJT-5wBSR9iizswpYKXctJJdBJvGiTgTkBGkgeju3qMkrAxddR4kBLocB05ZeYX7NEfrUhhi0ztb_K_ATZggZVGC7_VB3tFOYHeXoumx7jGSYRyOdrFv2hYAp1VBNl_LsjesGllAU5ner_QGTtT5-yWE3CZNGwAX-_sBimbLHH2EVKU3_4jBdyVoBqsgpyQ6FS-UPwfqAbj-b-cR6y17EQIO0ktzSLA-NAPQcUmi_GqLsoE0kAmfAK9sgvJcrwQJrMzHNqBhgDGjvf3tx931uIdn4qjffu9-tTU9KcEroghHvnQ9kWbgpMb38mn3O14VZ1kjwY4rYQ.jpg" alt="photo" loading="lazy"/></div>
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
