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
<img src="https://cdn4.telesco.pe/file/L6eANzg5E2ope30iE-H-ULCvd7G7wVWIzTloBYNqXcmq7zn-BobyVwCd0ZwAclmZtL_4gOq305cOK_MNfXllWc9Ghw-N5A-7QcSViJlWV32TqHyeaEgq8bzSO_VEmRmyYqaAbOdW_vCzZ-JcIb07rKRQLOFSjUuM5iS6zvwXmoMvJua5fn0wrpvSzoQ9IMvMi_pwZhmhqxKiIlhITFeABtp7aJT7qOuu73bYRJCtsrv958Q73_FuX_29Ohm1VrCwbsH7Y0Y0jWezT3ftlakOfIwZMVPTN-iDEDm_jFnCuG7Yl3sQV64eReV09A-6N68B1MZWsFNVBiZk5FFidrM78g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 15:22:34</div>
<hr>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=GBbnwk_3cWViMDxug05O_NFc8GT1jGBNsh0sPfbmjcP8OZe0m9t-U3pERAlYi05wZu8XkLeBACG2HWN33A7zzpweQQldIxwJJ-BT3gpAleL6PywJrQ8Ag_pytiw-EmX_R8Yh3ZTFfPRMByOxgL5EGIhNfBTgYgB-FHOufVc4NWlr9VGtrjl42nS3QqxcO7UtNsoeFGceSlGB-gnaqkRI35XwF38g26NTfsjCCqQethEiZnRKzTbBzzFl99RXEF44hMOLiwQDFeFcBL11Yv1Oohfj7X8-VIt60zkYVt_ATJKtn6cqHwNF0Lv56VUcGEbzCfAcHAKTO0lBp50-8cA22ZdNHWJo6gEiQ2yd9YIGcXxzeh8CQgusZj-YKTwa3kmtd30kON0xFumeTPzn5qAZOAHl0Z4VEbeK0v_kERvDfewH1JBMYS3qEv_1qPwjan_dCp2fcRvnEIaOkfDdDZgR7ufxEXXXwSvgJHVzv3VKJ984PzC2GUlM3E8reAxaWwbmrjgEsotOhcsLb3llhPbO1Vcg3-5JqzEo0FptjtfdG2r9qpkuIh36O5O6B3uiIheY5tTAGqjHawYapeZaMxZapDJ2gyyWYecKIrXA6N6ZnhoMXdZRhfuaOIvNk0kxYPMZ2Y7JpH3bg2wXq70VYxcvWR7P1SvDZ0LGhcIk49OnMl0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=GBbnwk_3cWViMDxug05O_NFc8GT1jGBNsh0sPfbmjcP8OZe0m9t-U3pERAlYi05wZu8XkLeBACG2HWN33A7zzpweQQldIxwJJ-BT3gpAleL6PywJrQ8Ag_pytiw-EmX_R8Yh3ZTFfPRMByOxgL5EGIhNfBTgYgB-FHOufVc4NWlr9VGtrjl42nS3QqxcO7UtNsoeFGceSlGB-gnaqkRI35XwF38g26NTfsjCCqQethEiZnRKzTbBzzFl99RXEF44hMOLiwQDFeFcBL11Yv1Oohfj7X8-VIt60zkYVt_ATJKtn6cqHwNF0Lv56VUcGEbzCfAcHAKTO0lBp50-8cA22ZdNHWJo6gEiQ2yd9YIGcXxzeh8CQgusZj-YKTwa3kmtd30kON0xFumeTPzn5qAZOAHl0Z4VEbeK0v_kERvDfewH1JBMYS3qEv_1qPwjan_dCp2fcRvnEIaOkfDdDZgR7ufxEXXXwSvgJHVzv3VKJ984PzC2GUlM3E8reAxaWwbmrjgEsotOhcsLb3llhPbO1Vcg3-5JqzEo0FptjtfdG2r9qpkuIh36O5O6B3uiIheY5tTAGqjHawYapeZaMxZapDJ2gyyWYecKIrXA6N6ZnhoMXdZRhfuaOIvNk0kxYPMZ2Y7JpH3bg2wXq70VYxcvWR7P1SvDZ0LGhcIk49OnMl0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=FbY8k1hHtO-50MP521HlW_DztfBJ-Zlo5NpBeW0PhsEiAiV1s13LZb9NI96xDyLMvRjuny2j3ass0hVk2qaqJWZ2Z5RS4hWQFYvgfynbZsBz28Y367VZdPgmqAliAqDwi6si3IYVlosOPAf9ktpInqEizf6LlzvxIyx6H0QIbCMej4PtBdPD-1fLaqTFMAnm6S12BNAS5KW4oiIaHqMG9HDJDwPVEodCE4rqRt10ScZ5xQBs_X-ZfXDDx11MFSLQjY_WSL6Vx8ScEUjxtT9NWmj65HOuSRSG3B81Bwd-gHKe1h6bE1upRJ0YrpllgQPPSykYpHSFSlYKo0JZ3mpIwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=FbY8k1hHtO-50MP521HlW_DztfBJ-Zlo5NpBeW0PhsEiAiV1s13LZb9NI96xDyLMvRjuny2j3ass0hVk2qaqJWZ2Z5RS4hWQFYvgfynbZsBz28Y367VZdPgmqAliAqDwi6si3IYVlosOPAf9ktpInqEizf6LlzvxIyx6H0QIbCMej4PtBdPD-1fLaqTFMAnm6S12BNAS5KW4oiIaHqMG9HDJDwPVEodCE4rqRt10ScZ5xQBs_X-ZfXDDx11MFSLQjY_WSL6Vx8ScEUjxtT9NWmj65HOuSRSG3B81Bwd-gHKe1h6bE1upRJ0YrpllgQPPSykYpHSFSlYKo0JZ3mpIwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=K_hVU1REAgYCzV5qh5_zXIlC_NX8aVqpvDyJtRZUoF-DKmUheuQsj-nxqd5RD8PLyvv4LAXuy_THpOOWCegaaMRGu3IX3-TRd63UfRzFJsjb9GE3-MwMOLnfBtBLSHCdc637qkbGct8PdiQIj9BdfFqM1MXTQ3tkCUQgYLeynQF4g5KtZ5Dd1LzsKFUsRd7EGaKkhbEExvjNAzvz9NHdwiYA9z1YQVWVqnC3cba2zzHNFY-W6WqU1sYfra6_2i2jGjU4vB0VI0zAxOGIQ05QX0K7DzNSrnIRVysjM_DnzVAfR0JTWb9czCH26dxS8UdDpEMN_Psst_UmvG46SJBsCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePD7R4akJNHgtADoLLrEGmggcBlHSCWonPMhTvzps1rXUU5QHyOhW7AEJU-wsoCKCUkneA0rIVGxQdV09hWNvoY_TGlJ5JscAuvtZwx_FjQPBCNolGMx4uy_2miPHn3C0he8F-Gdy5AhkwXxOAByaQgsQ6GpjfFXJ4p_LDkiDMTeeIU7FewLD761zzIK_nzdyGFUILhJoniqmXXl9-JDzIa8tRb9z7d-WDIwbk4RDxJ302fMiZ5dqD3kwvZ6QpD9-bgN2Xcb8y5ApKiAcjQ1GStsDV-1ajjMCVLCx40W1Q92zkQk43Tf-lPU9Wl2idMzPSEFegspk8Z5VfDYGxnJqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fahTgi4jsNM3S9IweY50s1VBGNfoHpiiZlJ1GG4UftA0KGr1gEJy8J-zr4MhwZ-xKyLYgzPjYRgkxJgtuXDJCLQYxnqjIsn6yowDqYlu7yIpsWs93Z5j-MppWVYNi8GMJOdoZUwlM-cSJHRx2JWfmljPzCP6Y7_8Mxf-yGHtVHEZWj0zfPgXUZc4Oe8QlqmovLr-ViaaCaqSe-U0ZoO4S2VTwtWyVXVxBnz3hdD7_r28_ydLtBIATwbt6qFTAlD_8jyV19w0aJzIN4o8ep0ZMIaiwXTfojX8gmDD66CPQP_35DRgUUfe0oDfTavWdnVLieTvkCe8yQYqlN3ctkyt4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=J12XfAPqKXlUM3VTbQnv_Pigmgu0Cht8-m5YH83LY3s7Dv7YY_aD2lus0Wy6Ab2TbczCRabL6jz24YD9rqjl_ePmHkEUvz_kdPSGudU_kFGOfEiO_86R3Q4_s9gHig_ycWkjn7Oe1ko-2U3ce5CN4PXQg1c2Hag2tprbmiuVlFaORd1pZ794YtLxwsvw_kjqrxl4BaUC0Axo1_sAbFdDv5qFt-UHD2F3-4mFJknlAap30fdecSK0U5-AP2bmgxPwKJ0IP1U60HTqjEdfFtuAfmYg0cZLgogazA136V_E4HalsR5GnraXRxJAzS7BOZGbHdIz0YlRWfMDLK1pn2Bl2IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t4fKtz9aVfS6J92jL69gAiGDLK-hG0_m_Du9Y2aq_OjI1YQUEsBqRGdm1rNOwFBZFWpQY1Qyvm18NDHceTCKgn5vRB_LWiExThmh8TkQ6f7cGwXIc-aV7YhrQUYgHJT6rRXHehEP-aosnmcK9z2Bvv71pt_Xo4wx00bpAcrgZJtPo7wcpRaT8tHOmL_hxZpB0EDZQiw6kS8u-hyX6BX-wc7CEDlEXqBbjNbOh0PP3ONGn0L_dX2hQCxkjgB4lBpL_qw7WhyPdfJ4-hxX9AGeowUnGHk2_5FwgXo1P50MSQ-8AyaqOF8R8aKCDxqcaNOzABPwBgoofO7RS3isGG6oVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v4HqklxJfku_mrrXqYQ1CIzBAaSAdMXnTBy2XWgsIZ8NLZpYhdYtn_0Ffil2ADCLPv5yaEQLKbn-1vkJRDS4nQJNYSdsJlnh_ev36mChCgcKMggsMDhaNSi_KyKQA5p675Mf9Pd3eDlUTcCJJrjAuHhTqAeN2sodFUvihxE92uuUigBTsTgyrn7CVmuUPICvqDNITQBDMw6q1IbVqcI929Dg08qTsuwE_3iEWeC3HwJWisRYmWud7z_-PoUxJEERLLbI7p2ycV6DFRuL4e_u_n1Xqj6u52voOKN9gn3d6a6uSPSnCmJZRekX9_iU6-6Fx0FKaWuLy2XRmpe9_Gjn9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSh8XnVVJtqMeqBeoxSdMkzBP_9sBj26r_9c7BS5O8G50pjkEuePFJQs5eo_jZGjkFvKIoU3A7UhkGeML7_jHBDPg7_jYGZ8Ufy7LCfo_XN9HuwXrMHjrtDPwGs9MXLshAfn4KYhEYO1kIxBEObAKUfhEELYFiUPtJNNpWvfY7gOV2twztQrUqAcD94kxPXcBt7xKe_WTsTodQSqcx_OCm-dqyBoLnjbODXdqhZ1NK9XYaf7iuuLbOcDMECGn7ObWNXsGTAjXWhYWia_4xk0U5IylXiR64mEu7ObKRNND4F2k1Nyn2c7_NBzdCsKHWDQdngLx7rizzeCc7pYRja47g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/smUgyRuPHGfoBzNjz_qKV2ynpKmsOiKaDYcjLsTVVo8MQI0VqP0uRnyqfoDbmHADBRSVMQW4krTK4Avt-bHYhBn3rwQvEhCMMOtwm73H_EyzxX3MXo_oAPoAcWF9qC_BFuzFWVirrGe4HQo_6dMxdgLWM_a5IdPyFqbYBTYhaFko-G-mvJentcqXn3qnUR_ponLAuvlw2c95RnsorSuEJNWnNyy661Ev3OrnCSin44VR7goG6AYs5sI3PSZuTVo7Uk0Jmo0M7gcn95z0TJRJzJ-ZCqX3A68VmAQ_k1Updg-20aWhVXplP9t7TSeBQIPFMJWD_MzcE6B0-YLijBu3Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=p9cfUxdsT5kiqt9RnqXR2_DlfpyKzrdcapghQ_9W5lt5pQcbO68VygWZBmVWlmcG5__A1w_WGx7ea6ba7i1BLh4Ix0Vp-UeH_kKfr4h5YKX0TlOVAAssoObnZuJzXNhnVuQf9tfJ4ZNex_fHmMkkH7TkHHtgIjYsecS7KLrCW8-yi3DQlw-5kyJnrcx-U0U4Nap35HVgQHiB1YXsDN6lw2kBR0EV8rSxBFMECJbiO2C98aKoctUPRavoMCdDabpqVSED6bOjKfcwXO6dCo0hZsKM1wM12tMGcibdynFhF8Uk0FWWbhm16WgSQTAAhSgVQFCrkI_ZXVRcT8KEEHfgjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=QQJIZr0MEjxAsoODBxMHx604QVqgejCzXidAFUSZJV87DGrtFSobyC7ooX64Y2JMzRuzsTwbONnjy8V7N7klLSenKYIA5YdGzLEYYvgZUvBdYyyCCZQI8m_Pbw3iTJl1D7Rb4s4mMAksFaOZYeeA7D6HkgDWMEy-vY583-leNKj6SvfJzybnkKd8VpCBZCBg-YZFH7UrU4NIO2fRNqvxNSJP5C0lqk5_lN5FiB2JkatF-sBSt5IMPLHahwI6JbfArSQEzCdTlfMR4o0h-e4gMGNh5n5IoEox12K57uwQs0Cah-sV_391H_KNm_uSxr0pL9a7ee1Rnbu6mlXIEcm4WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m46TuP3PAp490yyTC_6e09TgZAx8XWoRcMECmbj6fcvYVRoeicLLevldZpWfnzBzyY4woizHV0xqr0FG4zfqtSoOZ4iLdrOrkLOXw79rp_1EZd-PyPvlw-0GqVJLZlQIvtRaRAMTlUHkVpbIKdfjXT42CvmUxKyPNp7YQa8L7gtI2aImBYzy3FM05CHdDZYei0B5Mf2meSKimT_160ytU_tTh0L9vL94IdqjyTmeMsUl_ybzBXveR2O3rEnX-aanuHjlN2dKwdIN0t_58qagDMn90noEcYuBuMa-vjw3PZRd6kUVBZk5DXPoVX_JBnNQm6gHPWbx69tyAohLzN79fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Q8TLDuR_9QfuBYQ9kFOZUJZSNNfY6iKlb_uq4V-tJ0L1L4fdEIiZkZMEOUM8QbLIzgV_ArVmNLkgxWfXOuAmKXsvn0dXmsz5TsKzjjubDKlmcfp09brXBBkEeZpjwbDisiuX_8AeJ2ZENVP6TKyTb3X-IRkPoDoUos2wOXZp_JbZnyJgrs_vWbNoE_KbYsqJtmrSQDToNNbYvg08nNAI8ALFq2OkFE4X6zJDAD8ZaoUdzEBjPlrBKSCXGXkNPJhb42rRQsSOI3e6hrP0sdwPYlxFr06TRyXXLq1rGd6irUNI57YGRXCboWl3Q5lOW-3QKHNCydQuFSUlFTWw00j6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=Q8TLDuR_9QfuBYQ9kFOZUJZSNNfY6iKlb_uq4V-tJ0L1L4fdEIiZkZMEOUM8QbLIzgV_ArVmNLkgxWfXOuAmKXsvn0dXmsz5TsKzjjubDKlmcfp09brXBBkEeZpjwbDisiuX_8AeJ2ZENVP6TKyTb3X-IRkPoDoUos2wOXZp_JbZnyJgrs_vWbNoE_KbYsqJtmrSQDToNNbYvg08nNAI8ALFq2OkFE4X6zJDAD8ZaoUdzEBjPlrBKSCXGXkNPJhb42rRQsSOI3e6hrP0sdwPYlxFr06TRyXXLq1rGd6irUNI57YGRXCboWl3Q5lOW-3QKHNCydQuFSUlFTWw00j6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=VbTSEL0KEGOq4JKiz2dNuodS1tatNKABjZVSCPzus3UiUe_pwpn796JAeVzpnc-9e0DFUT287ZbwnEIk5Ke30dVQVOCywf_7xE7pA1DpxKUH3_uWkJ9o9fSw2izgRqZ-pLF8pSmVEnnaZ-cD1YM3lZ7m2mkaDdP2fpeJLzridHdxc6LwEsRv5VoLfx71rko5CwJ-jrrYZWTL2dcgia-ZFUWEHVjIuDdQ9q1Nn3CzuGeWyeELNj8oqzv487WrcDJ-lIJZFci_0bq7eyrOjFsMHfw4a0T_kt8KPMMsZhIfBgMlfOpGSObQkyuJhAhi2tUxbe50cgQYMn8XAbFnwzpWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=VbTSEL0KEGOq4JKiz2dNuodS1tatNKABjZVSCPzus3UiUe_pwpn796JAeVzpnc-9e0DFUT287ZbwnEIk5Ke30dVQVOCywf_7xE7pA1DpxKUH3_uWkJ9o9fSw2izgRqZ-pLF8pSmVEnnaZ-cD1YM3lZ7m2mkaDdP2fpeJLzridHdxc6LwEsRv5VoLfx71rko5CwJ-jrrYZWTL2dcgia-ZFUWEHVjIuDdQ9q1Nn3CzuGeWyeELNj8oqzv487WrcDJ-lIJZFci_0bq7eyrOjFsMHfw4a0T_kt8KPMMsZhIfBgMlfOpGSObQkyuJhAhi2tUxbe50cgQYMn8XAbFnwzpWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=YQ9jhX0V4au9-TB6KT3K4pvFzY1tcwrxAtDJX0NqILQbptdycHmCb8LXgP-sHrDVWXo1FKFTm3yjypmszMUmG8idcz28hg5ZqQa2cMbj32rSuAQpr9Od2XXxA1ye7t6jBG02-A5kQK0Txv6JEvcZRV60r8meCJWZ1ToZePNeah8h4jWC80J3dRYv-8g_dpq7KzJZbSrzCsbg5hFEAw64Dnvrr6ER61ezDTbialkyVzquQR4BkqDVkhfiJZyKLjfq0lq6pW_DYXmIX2P0nh6uN3ltkvkjlGd67urc5Q1z-Lv8_aozFZke9mlU91wZwQYxnr6IWyyp66b-BU0o9NhGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=YQ9jhX0V4au9-TB6KT3K4pvFzY1tcwrxAtDJX0NqILQbptdycHmCb8LXgP-sHrDVWXo1FKFTm3yjypmszMUmG8idcz28hg5ZqQa2cMbj32rSuAQpr9Od2XXxA1ye7t6jBG02-A5kQK0Txv6JEvcZRV60r8meCJWZ1ToZePNeah8h4jWC80J3dRYv-8g_dpq7KzJZbSrzCsbg5hFEAw64Dnvrr6ER61ezDTbialkyVzquQR4BkqDVkhfiJZyKLjfq0lq6pW_DYXmIX2P0nh6uN3ltkvkjlGd67urc5Q1z-Lv8_aozFZke9mlU91wZwQYxnr6IWyyp66b-BU0o9NhGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e-4utLnC0vn9T_cJEj_gr5lkZIrySIBL8l9JUXN8-NUQAMdI1AhsUfcuYRyCxfkg7_HpMIVF2V_4N0CUwi4CKIHr_HVZro2E55GipR_Kf_7K-pd698twgnunPv0DS6pkl1uv8iWgCUMbWhbIZPVl4k-serSV3VT4BzhEr0JSPNHd4jz-nhs7sJwps8fg5b5Y8OgkS9QxADJjIyKl9ZrzT82_41yXqfK2gp9O_AsIZVsnQtcnXzUz2phLRg33sozycvVxdUjfsMbrfhPtJOJTop5H0LlbbFKEKNhr3U3DieVJ3yNnAgXIJxyWcmh5tE5BY4mPTFQrbMtjbJygOep_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=rt75ycl7jUGh-IeJ6m5psOL9utTNVrwUVPqnF6Uk2_PkgRLCZW_IVDqNUE_VJyC5bVRx1Y9xgb8QxOHwgDlNIiqjPKneWFD4EF6MTLznmhFcbgL6o1noXRA5Kjy92yR7rCvpk_k0cm0qR9xzcy11yCUjifseSYoTQZa9S1kZv52Fvf0rnNQT_i1t11T6RInkbFfCkWvyHDHlHXHWG_3WWe8ccr8m8_etfnzKjByDRsqlSBwtniY3zYnlzRsEWztJBvECQ3h--QIdvveFyGWwraNmcWFxF9cKXJ5ubYunvsQQzVVLtIRSoO91niZOhbGxHFsi8zKNtJZ3QXuqyT7JCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=rt75ycl7jUGh-IeJ6m5psOL9utTNVrwUVPqnF6Uk2_PkgRLCZW_IVDqNUE_VJyC5bVRx1Y9xgb8QxOHwgDlNIiqjPKneWFD4EF6MTLznmhFcbgL6o1noXRA5Kjy92yR7rCvpk_k0cm0qR9xzcy11yCUjifseSYoTQZa9S1kZv52Fvf0rnNQT_i1t11T6RInkbFfCkWvyHDHlHXHWG_3WWe8ccr8m8_etfnzKjByDRsqlSBwtniY3zYnlzRsEWztJBvECQ3h--QIdvveFyGWwraNmcWFxF9cKXJ5ubYunvsQQzVVLtIRSoO91niZOhbGxHFsi8zKNtJZ3QXuqyT7JCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nrZfSGxq-DlYIAGS5WHG7dZ6g-ieMOhzuGWb5ILTNhYVb1g1ZZUJR45QdKku61n2STsYQGzpOApdJMb4DmGU8BCXvr3YfL4WA2WJyM_zmm1sW9x3U3bziDfW_gJ8rSbhLu34aZa6QTKCnKW3i8D6hMbKSGXpFzz2_zTdW5RZe-SjHf9KqYGHhaK69QM-2FEod1W9qneq4SP6ZE76mvBZ2Z4Y6_AgDZHds_8lswa94AWg7NthXvJfcdo-tnZolAbtdEe2cRxmaTozQi9685DKPYtaPtrdk4rSC5t37X4kQJLOQWBZ-c__qemL6uvjly477AljYLRxCGcC3_0V6NvfuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AMSZdvWTLmn29dsiR2do8iGpOB1SeNpkJXzHNDHppwu8o1za8lSZ_oyef9II4iat_dWXsauSTYaTUFjnGIX0Ret3wN3J9ce86tAVy3Nqv5gEJtbjEKZ1IRfeJGBImbW_6H8Ls4hXb4CFCoeuZVP-_lGbGRiOyNakbn64Pzx7DQIWfH5NKFETpquFCbfeW5A3d9z10iS7z5-bLUt97y9QaxV78I6x8m5-UkGAcDwmgNDL5vykvl97jAGh7Iw-UdRytji5Yh1uAAJbu7ds8SXRxkP0juSYDoehI2JulJ0iZZWPIQxxu8ObAxqTAu9OdEvLiS-rAqCID79RZylET6eBkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=cACrjXRK-FzPO1Q5R0YKxOfLp-geHFk03MK4JeVZeW1EX9pQmUIwheQuNK6t1zQfLcjmZbUBSMn5dZn3lCW8ylXqFIpC6JgdEhUo7nunUatqNxdssQIVxz84yPrhnNdNtxiSSS1CQK4LrYrrkR4MI5_SDYOCl7t09591JCflAZNxCdWMJp2f6j1EKctnPDrrb4--FI5XZltyQwsDpteWFEBSqplKecTXl1pdtefO6fQPz79bYE4xcSjAE1QzD8CTeGOu7VZkC_co6Zgb_e4C3LI1Tq5ZbTKKVYU6MACcWKMOlD5A9AedhPPAwDzSrQH45W82BBX_Ry6Yg-wqu339Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=cACrjXRK-FzPO1Q5R0YKxOfLp-geHFk03MK4JeVZeW1EX9pQmUIwheQuNK6t1zQfLcjmZbUBSMn5dZn3lCW8ylXqFIpC6JgdEhUo7nunUatqNxdssQIVxz84yPrhnNdNtxiSSS1CQK4LrYrrkR4MI5_SDYOCl7t09591JCflAZNxCdWMJp2f6j1EKctnPDrrb4--FI5XZltyQwsDpteWFEBSqplKecTXl1pdtefO6fQPz79bYE4xcSjAE1QzD8CTeGOu7VZkC_co6Zgb_e4C3LI1Tq5ZbTKKVYU6MACcWKMOlD5A9AedhPPAwDzSrQH45W82BBX_Ry6Yg-wqu339Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0lO1foepZVKkaJA-CRRe06Mbv2a8Q3N--eAiJ7uorxB0Zw4ToLhXs_7Rs5GXPsKBPJzVkFB7Zoa6HYv-iiYyDkNt8R_0tvTk30NORHpLHegFZbhSAXV7gbcvOIlm-DPYxNtL8XFtEoop4oWMhoFxTrp2hlIzEsn-h7K4slAohkIxYLHgTS-fvOyilNwRy1HISiaOxj3Vt9ZS6BvkxTX8BJJUchXvYCvkYxmobjcdl6jAth2tkpGUNAhSCF7z5jYsTnWnYX8H_6kZPRPh1ONrzz7QzvxJv4WwAFqfDhHSldNQYmihVSsziMOl_j28Utpt_P98qG9yYJaKBGIfIePYJ9U" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0lO1foepZVKkaJA-CRRe06Mbv2a8Q3N--eAiJ7uorxB0Zw4ToLhXs_7Rs5GXPsKBPJzVkFB7Zoa6HYv-iiYyDkNt8R_0tvTk30NORHpLHegFZbhSAXV7gbcvOIlm-DPYxNtL8XFtEoop4oWMhoFxTrp2hlIzEsn-h7K4slAohkIxYLHgTS-fvOyilNwRy1HISiaOxj3Vt9ZS6BvkxTX8BJJUchXvYCvkYxmobjcdl6jAth2tkpGUNAhSCF7z5jYsTnWnYX8H_6kZPRPh1ONrzz7QzvxJv4WwAFqfDhHSldNQYmihVSsziMOl_j28Utpt_P98qG9yYJaKBGIfIePYJ9U" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=YIBckw7KOuzfJNyreRb5VOJbdRzsSfVwq0RqfbIfLkK9OFnJCEWQ6Eca-vLP6Mhn8FsL3Ib2slWrD6ZhDprQsbnb7SurroomWvCtxdrKhJVSGwadGxXqVyiosCVyYzGv6XKA8A0ZxDt9Rj1nQcchS4QgsabUEQpKKVlzxSYjRtfIUH-48BsoC-O_UnHqzCem2dbHJGS5Ywrbge2glOXJO8mVaU0keX6WS8Sbv9_-hvQ3ArJ-7JLmBNJAdEoSpuRnzFe5OcOHWsveg8_PYWQ0CHSiQZvoFd1VeoPBUMhOq7LRpfWUnPXvve8ZwR9P-X9JvsFx2Flt5e7rCs6y7cUiWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=YIBckw7KOuzfJNyreRb5VOJbdRzsSfVwq0RqfbIfLkK9OFnJCEWQ6Eca-vLP6Mhn8FsL3Ib2slWrD6ZhDprQsbnb7SurroomWvCtxdrKhJVSGwadGxXqVyiosCVyYzGv6XKA8A0ZxDt9Rj1nQcchS4QgsabUEQpKKVlzxSYjRtfIUH-48BsoC-O_UnHqzCem2dbHJGS5Ywrbge2glOXJO8mVaU0keX6WS8Sbv9_-hvQ3ArJ-7JLmBNJAdEoSpuRnzFe5OcOHWsveg8_PYWQ0CHSiQZvoFd1VeoPBUMhOq7LRpfWUnPXvve8ZwR9P-X9JvsFx2Flt5e7rCs6y7cUiWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G2q-KbLJtiz1R2fTz1EpIuTZqCBRCg49a_EJBC5VjA9h4cDRKs8qoF_SeSyHReA6uRft4v7XxD5ZDqrnvj0Mg5T4tGdInwP6Jyboygdajf-H8v4Cq5Bu-5l9GOoFgZr9H-y8vFCTqqSISX2J-ZO7J8MN93eNWAFGv-I_--nIijYwxJUFyk4I8opGqiVwv32_zNgZJWv3lu4YCL9BTb66zayjP2FCgHPIAKZVtQdNtPJd_tG1i90a1cQzpRKFrko1vam4-UR8Oorm60ClkvG00IaUofXf0XBnq4jbkf-shev-YpT4fS1NCVheuPmn3yRT4rs6rBSnEvsU8lMPncEKdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=KGSsE6OznJ0ukmCDtsXDKR_1tVy734nva9yPb4KcQiYgTcrmooKyp3Vupq9oXUsAHLC4ntOisbj1b1bDqlEVz7EqEtdzO3BSkxP_Nyjv0HFLtQ-aB-hn6rrQwsuos0-HHc9OLmGwIIsZnYR3TCTJ5NqgLWaa2iCvt-ANtvskwtHMRi_J4pGl5vB0Tunbn9W6DuXLz63Vu6U2qdKvcjS-0dyBi0JoEPKXyN2DA2DLsjoeUbkO2-lfHLnK5zviW5VOukkikcF-g0Za8It8XYZ9NscEUx84YhAxtu2hrELkJ6mkuwkobySv_pWJDhaMa4bn2JxHgAIVowv6Cbz_CxqCZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=KGSsE6OznJ0ukmCDtsXDKR_1tVy734nva9yPb4KcQiYgTcrmooKyp3Vupq9oXUsAHLC4ntOisbj1b1bDqlEVz7EqEtdzO3BSkxP_Nyjv0HFLtQ-aB-hn6rrQwsuos0-HHc9OLmGwIIsZnYR3TCTJ5NqgLWaa2iCvt-ANtvskwtHMRi_J4pGl5vB0Tunbn9W6DuXLz63Vu6U2qdKvcjS-0dyBi0JoEPKXyN2DA2DLsjoeUbkO2-lfHLnK5zviW5VOukkikcF-g0Za8It8XYZ9NscEUx84YhAxtu2hrELkJ6mkuwkobySv_pWJDhaMa4bn2JxHgAIVowv6Cbz_CxqCZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=YY-jpoq3A-uix_he7PGYneug3gyB9DeeI1bUL9WvvZ9w6Y71bXF8gbVBcwvRheFBgmgXkNtODXPcu4clep2CHFi1LnGbAjltg-CaKOzE8yJdRAvHR-hHW9wjRCU-DsLXc3kJUls1wFpnQKWv4_JWBwYLPjygZPC-EYb7h1eOa5FWkTsglxdxn2s7-DbF7AIo27gKeoFde11h_f41LitJfIJg0eNTofQHf-8ty6VBuBJw-8tV-lQUzCids5kMTfTIUSShwEuEuacYGo_5tkawk0IYn45GApt7oJgcebNKgrQfhwFNZsPjKLWVhkN8IE6LjPhovGI_EOGKAzeaaHXCFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=YY-jpoq3A-uix_he7PGYneug3gyB9DeeI1bUL9WvvZ9w6Y71bXF8gbVBcwvRheFBgmgXkNtODXPcu4clep2CHFi1LnGbAjltg-CaKOzE8yJdRAvHR-hHW9wjRCU-DsLXc3kJUls1wFpnQKWv4_JWBwYLPjygZPC-EYb7h1eOa5FWkTsglxdxn2s7-DbF7AIo27gKeoFde11h_f41LitJfIJg0eNTofQHf-8ty6VBuBJw-8tV-lQUzCids5kMTfTIUSShwEuEuacYGo_5tkawk0IYn45GApt7oJgcebNKgrQfhwFNZsPjKLWVhkN8IE6LjPhovGI_EOGKAzeaaHXCFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=XzRuEw9onavzI7Yyn-TUfaWd5rpU5k4HRt6g0JUmkyOWQBmHq-1AaGMSkWckoCx1UzzLL6M_9i-o8r_aZp0r0FKohjj69CJ-3r2-CgVAXfRYJ1jjZg2lMQirTNTbznH4gPogBoZX_yJvpmCM3Lu52lDSHNkebYlpe_cZ09yvtNeYuCFUPPB585H0NHdm9JQegWF2sCCLN9ABKdFn_IeGz8VaPFEMeUNcX8G7fX5pxWJIwWvycVvofkINj2MpH8XVFMrVoPEPC3ovpJiXifryD8K5BnqSOgcI3-R1VxcqlK6bZXNh57fJqiGEsTtjBI4eg0hSkPFwWUBtTjFSoU8ozA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=XzRuEw9onavzI7Yyn-TUfaWd5rpU5k4HRt6g0JUmkyOWQBmHq-1AaGMSkWckoCx1UzzLL6M_9i-o8r_aZp0r0FKohjj69CJ-3r2-CgVAXfRYJ1jjZg2lMQirTNTbznH4gPogBoZX_yJvpmCM3Lu52lDSHNkebYlpe_cZ09yvtNeYuCFUPPB585H0NHdm9JQegWF2sCCLN9ABKdFn_IeGz8VaPFEMeUNcX8G7fX5pxWJIwWvycVvofkINj2MpH8XVFMrVoPEPC3ovpJiXifryD8K5BnqSOgcI3-R1VxcqlK6bZXNh57fJqiGEsTtjBI4eg0hSkPFwWUBtTjFSoU8ozA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=j5BY-IQ2I23CzLRm7mqzzs9XVKPL204TIt9-LaFM7_tw3c6TJ73ha5RMZGQ1vwzvmFJctkPNfAU3KIrQ_bHvHAZYEfuUpgWd-uyq2U9iDjs0I5FtbBq-IjBEQDX4pAGSsf76Owwl9KSY9R3pLWRhZ2w0ANvspkwA4Zw8HflL_SMxpAfxgTZ1nqCEFpzMOvs6gaCQ7_WBU18nhPz13_wgCZuCzpf1MvnQWtIn727vyz2PPDQVrUMM5K0tVyec_6xlz7pg_j4lOiGBIVa0Zdo6jLNrT64JSrNa4BKB_sWNAXyMGXxAKPPtcYkpqv1ZBW5MO-WVY-YVHML7lNK0_M_1Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=j5BY-IQ2I23CzLRm7mqzzs9XVKPL204TIt9-LaFM7_tw3c6TJ73ha5RMZGQ1vwzvmFJctkPNfAU3KIrQ_bHvHAZYEfuUpgWd-uyq2U9iDjs0I5FtbBq-IjBEQDX4pAGSsf76Owwl9KSY9R3pLWRhZ2w0ANvspkwA4Zw8HflL_SMxpAfxgTZ1nqCEFpzMOvs6gaCQ7_WBU18nhPz13_wgCZuCzpf1MvnQWtIn727vyz2PPDQVrUMM5K0tVyec_6xlz7pg_j4lOiGBIVa0Zdo6jLNrT64JSrNa4BKB_sWNAXyMGXxAKPPtcYkpqv1ZBW5MO-WVY-YVHML7lNK0_M_1Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRoUswMsrmJv82esQtWrCx2ezouKBR4WnvUPq6GvotlAM4IJ-je7Xt5X-WiUnKP1SyuOhIqrvsG_uAkkDqfH_4X9VoFtqYVIH_9RrLM5eMV0PUIMhoNFRKa8e-p6uDZBV3qxSKwSXxQLq8ziIMbfqdlSN0P1unYeZ_fqSUoCUsggIgOOvVUM8eeQG-hQpDkcOTRWzcBPrTyH_NOuOmh5NjRBaR8MAC27wsH3j6-h8ld5YHEfkXlmSWkZr-L2atNDZ7-t3Tl-y1ZbBxRf1uYFqz_T0yfQJIXTKQJ7SMxExhD2xYEU0kHSBa9VtjNdhAN1Hjuxs3cj2CZEEWVxFP_R6Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=GVixAD2cYL9iq-ZZtNlTVf7p0nYhT4M2VIO8NVq5g_uLhs9cdTQeB4BggaIhUaxckzDP3w2NSJDUJItJKxsH8r_8YHokpP05TND930C4UUytpSKuwUnXWcS9evXG_6g17yB7QQ4rz7-hnDMHZxFJABVfs9Xod747z7oHlIGjtA8LHA98Z8CyMMmcAGsHsCGbES7f4QtVz-VsxV-MEITb-CMZ7NBJr7kYlSIGwTQPeBCidJEQTrQm6_BMUDGDLAnn2RwhWIzUa-F8dNP6u-hn8qxeJMYA417t0Uyq3CixVioykA0Dmmg8UvXfyJTGA7-llNWYrOC-s5gCrTbhucrLNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=GVixAD2cYL9iq-ZZtNlTVf7p0nYhT4M2VIO8NVq5g_uLhs9cdTQeB4BggaIhUaxckzDP3w2NSJDUJItJKxsH8r_8YHokpP05TND930C4UUytpSKuwUnXWcS9evXG_6g17yB7QQ4rz7-hnDMHZxFJABVfs9Xod747z7oHlIGjtA8LHA98Z8CyMMmcAGsHsCGbES7f4QtVz-VsxV-MEITb-CMZ7NBJr7kYlSIGwTQPeBCidJEQTrQm6_BMUDGDLAnn2RwhWIzUa-F8dNP6u-hn8qxeJMYA417t0Uyq3CixVioykA0Dmmg8UvXfyJTGA7-llNWYrOC-s5gCrTbhucrLNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=J6l5D0C-JcE11TjbJVLVg3Gu5LAGOYFw4InI1HzfkV-2qOkImkWqV2Gpaa-nOE8F_sAjzfz4GkP4XVGEuZ40Zb8nmX0WwW4ZuAdAmEnxA7bPOa9wXeJ7fGYMvQokf2qisRwqyc3FXhWiIYzbBnbyE0AJ8M-qedp4qbxOircZZm4o2Yep8qmlT_3p2pspsrg0A2nIvZGRPSEQGJKHzmyIR3oC0Mv8EuuMALF3OMPubajTsUgnvxfUNV_Z9VMkFNMGHgnrVJTMm-26gJb8utLZ_EMoGWuqnN0Lb_dFNtwx8MFngPYmBpw-iKDwaPvT4BHgUKcgJOu3zKckIery2eNYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=J6l5D0C-JcE11TjbJVLVg3Gu5LAGOYFw4InI1HzfkV-2qOkImkWqV2Gpaa-nOE8F_sAjzfz4GkP4XVGEuZ40Zb8nmX0WwW4ZuAdAmEnxA7bPOa9wXeJ7fGYMvQokf2qisRwqyc3FXhWiIYzbBnbyE0AJ8M-qedp4qbxOircZZm4o2Yep8qmlT_3p2pspsrg0A2nIvZGRPSEQGJKHzmyIR3oC0Mv8EuuMALF3OMPubajTsUgnvxfUNV_Z9VMkFNMGHgnrVJTMm-26gJb8utLZ_EMoGWuqnN0Lb_dFNtwx8MFngPYmBpw-iKDwaPvT4BHgUKcgJOu3zKckIery2eNYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/htJdU8ojnCpmwz6dENFC3NPwXBFOMZstD8P30lo-0yoY2U3q3LJvaRV89LlR6-ch-W9Rfik78X4jw0qGg_54v2IbfX1gCKiBWpgborN5L2ug2nw47wI6hoQyGS9XAn92T1CDsPfhqrteeZV-DGrKEQ6hyIiIAr6qIbQOVnzfp6ui10RAzJLDcwjl8FbhsXkdd5FRfWsAhSnN_M1QawrZX_dCk_DC8WCa4bVSIAERZf1JUgImWldoMl_tNEQwWoDeyWFcmkBTQy1KjfEkYu_81nK17qc0NuQGYI8nO8P2z2YaITVQSkwwjZfT_Oqije53PKbNOmTTSZI-fx0np5qlsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=QH_TYmgLd1zvWftq0WM2gW4nP0x6k7nyVUA_m8EnucIgYRgYQg6DQJ9UH2EfSKlgonpc5deN0SiWFDaI4n4SH0fW6TvjVtAwjZCdyFEyTZTwSIMePuLhdzOpZ08vCJrwah7JrL4rXJ6jD40QSRwlIbHgkHng93gdPCPWEmRttH7l9ilwpLKysFJ0EbbQOFXaBY_3rgKXv_V1VK-6VckmqjaeZmGeBqJBFiEDQsDKEsSABNt9h_TSD-NVzvHXwV3dvTpp60cU_z0kXDPSwl6B_RmlTAW0cqoInXM6QGH4ZLUhjRyRPnKDF86WcSes1H6s_7_aSckpk1KHl8HeVSOdwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=QH_TYmgLd1zvWftq0WM2gW4nP0x6k7nyVUA_m8EnucIgYRgYQg6DQJ9UH2EfSKlgonpc5deN0SiWFDaI4n4SH0fW6TvjVtAwjZCdyFEyTZTwSIMePuLhdzOpZ08vCJrwah7JrL4rXJ6jD40QSRwlIbHgkHng93gdPCPWEmRttH7l9ilwpLKysFJ0EbbQOFXaBY_3rgKXv_V1VK-6VckmqjaeZmGeBqJBFiEDQsDKEsSABNt9h_TSD-NVzvHXwV3dvTpp60cU_z0kXDPSwl6B_RmlTAW0cqoInXM6QGH4ZLUhjRyRPnKDF86WcSes1H6s_7_aSckpk1KHl8HeVSOdwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=TxUFbTzokw1US_rcs5E3SGh0NaypNLMCN5hu2mZinZxO1_FD3XtVK3OmZWtPR8OpGXmK5k5TEkKCK6XjQ9Ofz96I6M3pN5oCyNoMytjrI0xLLzvQqXDcaTdfUxAgNfGSWIJX-yQcevVVgj9JXrryUFBnZ2UZ4iImfnPGciQDnAbeLfHzxHl7BCO3_HxPIYbi_rmTXGnTFyQgM3eQaU9L8gf5gj4Z8DgGdWA3zugTdpc1dap26l0QiI8TVhuuAn89p2Zm2XKi3LnTcp1iAI7hg140PZcjjtcbYCsM66V50Emudon5YxvyVlJGapJJhS4jKsLA0sI4LUMeaRwKURAI1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=TxUFbTzokw1US_rcs5E3SGh0NaypNLMCN5hu2mZinZxO1_FD3XtVK3OmZWtPR8OpGXmK5k5TEkKCK6XjQ9Ofz96I6M3pN5oCyNoMytjrI0xLLzvQqXDcaTdfUxAgNfGSWIJX-yQcevVVgj9JXrryUFBnZ2UZ4iImfnPGciQDnAbeLfHzxHl7BCO3_HxPIYbi_rmTXGnTFyQgM3eQaU9L8gf5gj4Z8DgGdWA3zugTdpc1dap26l0QiI8TVhuuAn89p2Zm2XKi3LnTcp1iAI7hg140PZcjjtcbYCsM66V50Emudon5YxvyVlJGapJJhS4jKsLA0sI4LUMeaRwKURAI1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=swj8LoHDcz05aCbJnnr80rkuRkd0vwtgMDBoUH3Jzvf48y5oArmdj2HhDyWJHDeagc-ifv7KR3lUZgvb7EyinwVVKgTuz29tjwmRwdG4__5zyHHKsNTHkL_ZWBxnpyIV4TcvJVoQ7jfC_-xJKXg3OdcMgZK8f0QPnSg1xccbcvY26RPkhsgsIuw3AQSmaexHAy-DUMInPXJTI3tIxvp5sA_WENRm8vscSvwz4nKnKPNHQ6AAbuURFUw5d3K2rOcEgZZFdsF2Z4XPGDDMeMrUwdHABXMGutCRUNRtuAqsVgkTDU2vvAUHYvuTLWketGF4hUbqPePemrxiI30A-4TT7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=swj8LoHDcz05aCbJnnr80rkuRkd0vwtgMDBoUH3Jzvf48y5oArmdj2HhDyWJHDeagc-ifv7KR3lUZgvb7EyinwVVKgTuz29tjwmRwdG4__5zyHHKsNTHkL_ZWBxnpyIV4TcvJVoQ7jfC_-xJKXg3OdcMgZK8f0QPnSg1xccbcvY26RPkhsgsIuw3AQSmaexHAy-DUMInPXJTI3tIxvp5sA_WENRm8vscSvwz4nKnKPNHQ6AAbuURFUw5d3K2rOcEgZZFdsF2Z4XPGDDMeMrUwdHABXMGutCRUNRtuAqsVgkTDU2vvAUHYvuTLWketGF4hUbqPePemrxiI30A-4TT7zzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/unPzI2fbBta7dkwdPysm0qPsTtK-69HIZE0zMh-U9l-ipZDYosxpCzkVFHhwlYYupXkRjs-DPOO6BScQb_Ji_mmIkqol5_OngiicTGrxitCoO9aslzfOfhCVQ7Ys-vV8tVUoeMfMO4zYecV45ERn1Xw4DZ1RWe0PmaWjYPKWMqKU1I6urxIM3l9A5HC22j_AxWARml6gBQ-PKw3O3RNTcS3mG9VI3FDJzqFVbETY_99LW9R9ZdfM0ggDvfzkx2vbQOcvlcwc_xutWAOALF0yVX2H1VrWaajVpyXdjQrhX2RuukZOvBl5P1SfMokb1is3W4yznrGWC_GB2xmWgml16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tgJ2rdOiugfdxeswDWP9deGNCdppSQBnTsi9nivL_eo9X8r2Ye7z_x-2FpUe2dhlIFTQrsUAzlax8q7mRlnB3li3H0hDpm5JToHHRZcboLd0cSdBHl1yKNSLvoIpD27reCVdwLup67RnfEAWOEsq7qMVCXGN1bCLJd0NzLeaD958inSAjJTF0OrcB5gttoVWpdNFNfBEQoPmTMvT95J35utVc2TThFscu2b4pPO7wKJtAftDAjNQEj7bBV8TCpb2OFglESNOlOavz9KiBx97IhNle-L9u1YoUXud3UHFFNM8mLisSIgVbsgkM8F43TbkIEWvvCCE5-GVihxs-AZXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hu39ja4iaV6KLnfQpnyzsZy0m3VD7CnUDru1V_SloAGqc3sLAdR-itY4j8LUAegoF6zOBaiCv7Dc_MVRX5cds2llrK60maIYeAg8iKKCeYFJEbzb4rxg7oq0s2WyRmqYjlYmz1O6EqNxDRsA3e9Lg6OZ0dY8MhrzmMnF7tV-O00WKqENOazHL0_drV3-P8RFj-jOdqmpblSETibge9DV2pO73wy4MSEoNCGjI8i2r3KCXJDl5AK_szZKz3Wl5G--dsqH24MrOHaS_4VI4YtQRI_KRKhnHa-KIHeZrDlT-TIPrCpRPdJ27SRjFOr8fI5_OlocP_HKSBaHRU7rA5IZgw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=h4gLjFP6XwnCZJfnQN6rp1od02SclXFMGYUezp462WpVuDi0FBErULdLSb4mXI6VNIGU5ptlmb5HCvDv-u3OBE46IpU7-YmT-WfkCJhoKjUnBzKUhDnAcFkEQpevPhdpo2pe9TWv4fWZLOasCOOa0DrrM_8YGyIaITDpB6mDzJkOwRAOcJ83u6hwAGeO2MBKHFh5da95JhroF2U5Jvn0cCfLeTkOHGEbZCzj5CVwuq1lY8ZT3WB1i0ztLypLDDZpbga7Zv0IIQtJhHSEQJgTzJaQgFLhR2qQe9x6Qk6K9VFFhA_ChXjNaLqDVeTBs622kX2_WXS4i9arV3m-G3t2Hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=h4gLjFP6XwnCZJfnQN6rp1od02SclXFMGYUezp462WpVuDi0FBErULdLSb4mXI6VNIGU5ptlmb5HCvDv-u3OBE46IpU7-YmT-WfkCJhoKjUnBzKUhDnAcFkEQpevPhdpo2pe9TWv4fWZLOasCOOa0DrrM_8YGyIaITDpB6mDzJkOwRAOcJ83u6hwAGeO2MBKHFh5da95JhroF2U5Jvn0cCfLeTkOHGEbZCzj5CVwuq1lY8ZT3WB1i0ztLypLDDZpbga7Zv0IIQtJhHSEQJgTzJaQgFLhR2qQe9x6Qk6K9VFFhA_ChXjNaLqDVeTBs622kX2_WXS4i9arV3m-G3t2Hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_zNxqepozD1mCpCzzm52l4NCN9IaVx0p6GtwI4Nl-cirRtoyx-Il2dTKpPinqExXqtkITud3_uIeNJGFiMRiDgqdnhIPcCnCAwobY9v9u1fCRHj1pHAGJ0tHmNiArpTawHnjEmbhda0rm_BhIMFG2Rl-jj-g7s8Bfjaks1xJ286inChaty53xPrz-JkPu8er-xIA7yor0Kerd3rZfOwtfmsIjfakx7CKrSbi1YK6aTMiEbR7Np6IUm-_KWHJOAR7BcpJSKlLVenlWfH1mDuio7mXt3nYuEAGukpJFBZcoiTNpHcoskA-9mdLk7FAVFcAyFSkdH4h70uzKZ6m8srwNMc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_zNxqepozD1mCpCzzm52l4NCN9IaVx0p6GtwI4Nl-cirRtoyx-Il2dTKpPinqExXqtkITud3_uIeNJGFiMRiDgqdnhIPcCnCAwobY9v9u1fCRHj1pHAGJ0tHmNiArpTawHnjEmbhda0rm_BhIMFG2Rl-jj-g7s8Bfjaks1xJ286inChaty53xPrz-JkPu8er-xIA7yor0Kerd3rZfOwtfmsIjfakx7CKrSbi1YK6aTMiEbR7Np6IUm-_KWHJOAR7BcpJSKlLVenlWfH1mDuio7mXt3nYuEAGukpJFBZcoiTNpHcoskA-9mdLk7FAVFcAyFSkdH4h70uzKZ6m8srwNMc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=Tb9xWx6lYVvjROOEg3cPTabXwtUTlSA5E1rKEGIlV8ZD_YpbCkrLG9XxtmoHSc8nM_0zzVBTdQLC04Sq9sNl_tk3KzdoX9GukY5e3AyT6kTss7tLkeq0wIdNoDJivDLeOugE4IHwVQSaBcWcs4vMbQJA4ZG7d2KVfHLFWGlPzV5Pb49C00ZYKaArsRD0GVgiuZT-ySxJ8Mh9pJfOobgSekpBwxmiJch_qcgtvyMHN6r8hoL3zkSJSGymVPXA0a_onPcNkJDnzK6Nb7nwD8QRnZfkWpavf80WYrTVhzNt_rDqaocUuJikxhiNOvytDtLwZoi_k3hOWZGpPz_libI6vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=Tb9xWx6lYVvjROOEg3cPTabXwtUTlSA5E1rKEGIlV8ZD_YpbCkrLG9XxtmoHSc8nM_0zzVBTdQLC04Sq9sNl_tk3KzdoX9GukY5e3AyT6kTss7tLkeq0wIdNoDJivDLeOugE4IHwVQSaBcWcs4vMbQJA4ZG7d2KVfHLFWGlPzV5Pb49C00ZYKaArsRD0GVgiuZT-ySxJ8Mh9pJfOobgSekpBwxmiJch_qcgtvyMHN6r8hoL3zkSJSGymVPXA0a_onPcNkJDnzK6Nb7nwD8QRnZfkWpavf80WYrTVhzNt_rDqaocUuJikxhiNOvytDtLwZoi_k3hOWZGpPz_libI6vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #58</div>
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
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIwWlcvE-4KpAhPrVCvjYzDrc5HFCKVC5dPV04AuaH3YZARAThTz45wAfDYKN8iicJXzdNhBAK7rVfBlyOGKiWwply-DZ55T6wkTeQhr0RLKI8Oq2qSXwmIREkxOiDDrObOW-E_6OmU7ZeJoprYUjdNNJq_HCJKxfoIUsn5RXh2js_PRcMTgZv1n-UsRyFrDibRJfxQcOHz_Y3O4-O2TeVJfNVyXrtmSMdlfKl-tDp4_Ot6z2aTKheS63_EbCOCh6cXCaFMLYnQvkLrQDxkcrnzXAOgSOKyVQCIQPbBFDnzQc3U3HeiIRUi-DUs0zkMIajE_8yLv4nmR6S5pFca6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuThsYT7HRApKKEUe-XBiIVotBcbogmO6HS1-cXXaGIt6p4KflGKxwCaggs9Ug5zpxAa0KR42PDLMWA58auMSCQ2dK0S_RKd6qArVMnTImuYwjivUTR02XACrpX2aLaT0iqG1Lv1988DsqtWJnrTlJA9LzTDmSEDoMy_a8OVIyvgImzgSFYHdjSDfe6PwAs6SGU-EWX8Z2-pu5iVRUXaEjUc6YYLtQpELUjVPJhzD0iRLWtLi8O0M5zNfkDOnsoUdXq5ME9xsU1pq7__jyCAbsLqCgeIH1I1FACWaAlBcqy_IdLaQAAbybokhiZNWSzQFuyr2Uaf7rNKTTrgIZij37ko0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuThsYT7HRApKKEUe-XBiIVotBcbogmO6HS1-cXXaGIt6p4KflGKxwCaggs9Ug5zpxAa0KR42PDLMWA58auMSCQ2dK0S_RKd6qArVMnTImuYwjivUTR02XACrpX2aLaT0iqG1Lv1988DsqtWJnrTlJA9LzTDmSEDoMy_a8OVIyvgImzgSFYHdjSDfe6PwAs6SGU-EWX8Z2-pu5iVRUXaEjUc6YYLtQpELUjVPJhzD0iRLWtLi8O0M5zNfkDOnsoUdXq5ME9xsU1pq7__jyCAbsLqCgeIH1I1FACWaAlBcqy_IdLaQAAbybokhiZNWSzQFuyr2Uaf7rNKTTrgIZij37ko0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NJQ3xFpLOF3VQDwPT08xqIHvj1KGLDM464OXlcQ5j7_IJAbgZeBbIyMwz6gOfR3W6tvdFFOb8m-vJFmH7HBcV27Vwf_LtrPxDKIe-kpCxVxQoKg3FMvJGIRm3RxNHyF7d93jbWZbz5cD0JSBZBf-sJZq6updvsCdJWTMT4OPR_PkqpQx3ql75rbun6H5slyz4Ua4613yYHB4gHk1q1jBJ7jcixNeLuaDydWA5V0ZpT-9cPeHsdu6OcNjWPiTW3zfPnfgqz-XOnwncfGk55HgjEm0UTezuZoILmZuLuSYaFkPk35oq81RPCXEMczNSR1GSTuNb_RfJhvJkdJlc_mILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=bJHYaBbzTodmVM_ZsSxuyBHbLAyTSWU704y-uosaXbmDf0MvG3CbinV64yoIsGVQM6csjuc3BiRGDC8QTqvmhpZWPTKNGjFo1ueA7CxAfuPm4snub1I8AVb2bSaYMtkVcVJdFJOCdb28GhgxZ5__VxpGFtKb7HbDtOXxze6ux2oZaqwRS3Nyp3CSGPj7IAovUvQDLTfoiIjSplQPqyR3JWVOpuQJTfNTrAIh6JLKHeJJC91gMoVhOgGDNbLZ_G7MzpzRDFvedWkRBrQtmpi2sbyTfK7z_f5n9U-O4c6IT2T-FdIFGFoCyyJYFB1DZ7_QaIBHrS9ym076Rckjet64mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=bJHYaBbzTodmVM_ZsSxuyBHbLAyTSWU704y-uosaXbmDf0MvG3CbinV64yoIsGVQM6csjuc3BiRGDC8QTqvmhpZWPTKNGjFo1ueA7CxAfuPm4snub1I8AVb2bSaYMtkVcVJdFJOCdb28GhgxZ5__VxpGFtKb7HbDtOXxze6ux2oZaqwRS3Nyp3CSGPj7IAovUvQDLTfoiIjSplQPqyR3JWVOpuQJTfNTrAIh6JLKHeJJC91gMoVhOgGDNbLZ_G7MzpzRDFvedWkRBrQtmpi2sbyTfK7z_f5n9U-O4c6IT2T-FdIFGFoCyyJYFB1DZ7_QaIBHrS9ym076Rckjet64mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=qYswfOoFBGvLutFeVlpYrXiWDhC5vGiTAu6qvSBXqJVlk91KeRrLI9KjnMg83XNx2hYiPhldiqQXqsUhvzengqy9gKn-Cxd0dQIzFNFs4Al0v3I51P4P8Lp37OmXXALrRFAXQG5Q4znh-EMXoizszUvcyS4NFGSnFBpom6EwFkoa7zm143Do4a9AHLNLckV0Hp5_Czo7emGy3EKwhEjHRqWb0TcRVcWWZcp40x5VVbbFdP--AaWlKEqp_ea0n9EXAmniHf6XHapI38-iG-0UZ03uYjwp8RKEYZHLC3WtFd7XfCY0rWWWftM1KHaI6jTnBn2RdbiAWF9EWNMd7BUE2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=qYswfOoFBGvLutFeVlpYrXiWDhC5vGiTAu6qvSBXqJVlk91KeRrLI9KjnMg83XNx2hYiPhldiqQXqsUhvzengqy9gKn-Cxd0dQIzFNFs4Al0v3I51P4P8Lp37OmXXALrRFAXQG5Q4znh-EMXoizszUvcyS4NFGSnFBpom6EwFkoa7zm143Do4a9AHLNLckV0Hp5_Czo7emGy3EKwhEjHRqWb0TcRVcWWZcp40x5VVbbFdP--AaWlKEqp_ea0n9EXAmniHf6XHapI38-iG-0UZ03uYjwp8RKEYZHLC3WtFd7XfCY0rWWWftM1KHaI6jTnBn2RdbiAWF9EWNMd7BUE2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=RVDhEEfZkfOjmWEAM3qt3k3_5x3gtw-7yNeqjortFpxSKeSesC6Jiz5-Y1-RGnzdjO_-jpW4AP2ty7nE2PTFDdPQZ2f_GrM05ZWc5vqUg3lcGTyWn16X4voE1XZzz0PLkbNlywp9rY2saHijEGcn7fzRbCtkGQUML1Svo01N6PWJFW1LjrePStwzTFRd1Mayefee2gygNHYWABtjeLkepj9fXXojGZLQM3xlP6eQmeBV1VlaD_V_m99tfZ2kuhXpbobQBTNcMaBN2xzMksqHUrfJdGsajHj9zVrbiX3yYGZAxVClfkalgvxrlKrPzfHGSBFhY9aStgl4lYh0lLuwDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=RVDhEEfZkfOjmWEAM3qt3k3_5x3gtw-7yNeqjortFpxSKeSesC6Jiz5-Y1-RGnzdjO_-jpW4AP2ty7nE2PTFDdPQZ2f_GrM05ZWc5vqUg3lcGTyWn16X4voE1XZzz0PLkbNlywp9rY2saHijEGcn7fzRbCtkGQUML1Svo01N6PWJFW1LjrePStwzTFRd1Mayefee2gygNHYWABtjeLkepj9fXXojGZLQM3xlP6eQmeBV1VlaD_V_m99tfZ2kuhXpbobQBTNcMaBN2xzMksqHUrfJdGsajHj9zVrbiX3yYGZAxVClfkalgvxrlKrPzfHGSBFhY9aStgl4lYh0lLuwDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvBWXJtLW6RKchZzXpJLCYjqKWBZstpmq72PGq8nJ_3T0H3Ar4T0wlNekOsI5AvUHvWvnlt9Qr5Qh19fdg5XYJK8CN1Udsioq4DluCrw8fQDG5aalPsFZELOveZ-MNZUgz5VwCuq2wLTgmQTbn4cZeyRX44wsK6PqkIuW7b_VTKR0unsILrky8vLaMbVZ5tVie0QVvKcIu-Lp_KEMbRb2WQbkG4Hl9oSFO62RRd2p5rIVBwaoEm6ywOnJrRR9_vZkKG4Oi1MRfCfZh6hkt0vEqLwIknYK7xfQC9reNH4VQoAoDG-aydQKe8NFcF5VI13lkKwLUJ0k_Ie40A8_PYSLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX8gpOyPeK7LBdv1R5UY6oKCvUu6QDhQL4qEZZC1h10pL02gTkwZ5_R20q_9zoWZA5IApAofOl45W2wXj5Zo3U9P8m6BupAjGSsNZnUSwCmdozYidLgpvUw6tyvJryuh1hYvTSoZquCKoAG2VszLvBlYYcCDMOredo8ahR2c7a_mifqCHt3a-gvRH3wauFoG2gcZTaiuLY_bmGL6k5BTFdYz6jzyhL3JuzSg9B_gIbaNTLc0HFzW_TvCsCD--ylPIFy0zeVYQB6LrSXWWE1mrxAb9Wt2FICdIkxNiPZ1tvx08VCWemqJcsZR_9hTFg1SQK1zI1Jcpvbdu3d5DcrkIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=GEc7goDfkld1qBlOYFvdv1I-GcYWv00EXzJcM8MYioYoMzAbNI-vBqvBBHpHqlJBNWToFOchjj9qE2cIvdKGhfUvsJVvha9ueizQVergNbio3RG5UQowSMjJmt33vfTmiK_NFWWVXkED5XtGCnk2zjR1J-hmAJvM1STvyHyB8FxVZk7u7ItIhZwvNyoCXwxhR3HjSor2NeLRZc2hosLkV-OudYa6Uiw4NXLA6tW-8c8-8vL2cVU42sqEJr8_X6D4MBDbwVFmvkSqpouIfyjOae7-iP6YnOWJQmeZF64MlgNzD-32WyNXG6gCfkTG5knD-tRuP8J-TxQRIzW2nWk_8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=GEc7goDfkld1qBlOYFvdv1I-GcYWv00EXzJcM8MYioYoMzAbNI-vBqvBBHpHqlJBNWToFOchjj9qE2cIvdKGhfUvsJVvha9ueizQVergNbio3RG5UQowSMjJmt33vfTmiK_NFWWVXkED5XtGCnk2zjR1J-hmAJvM1STvyHyB8FxVZk7u7ItIhZwvNyoCXwxhR3HjSor2NeLRZc2hosLkV-OudYa6Uiw4NXLA6tW-8c8-8vL2cVU42sqEJr8_X6D4MBDbwVFmvkSqpouIfyjOae7-iP6YnOWJQmeZF64MlgNzD-32WyNXG6gCfkTG5knD-tRuP8J-TxQRIzW2nWk_8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/efDYQbHJaH5tIDFMYPvzN0_L6kkjbDPyD7IcFTNHKs0rSn0LUw3gBOeg6TrDbNR2dluU1zIPwTQn2ilus6bYEoKLs6O6a4gl-vp6o09-XBRae278KaneEP08_LcwvGxTg2NZ5wTeP9rgva-5QcH38i3niG1uE2XcUl-PG93Q9ofqXgAH51oZjpeWbqOHTMLAubyBZ3ICCOqI8HSXuz8oBxqlP262FUHfeleTFseJPYfpCjajrcxoj7G1pJa-JFU9Z7e77od5DbVtQ0iyF6ZAP66Xw5By4Fnnfb_1m-u18ZQcC9QkpcQdk2_LopLVsFZyeGn99dr1D-It-H8dDAtQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX-jhdg8ttcjuEm0kqEQr64BiCW-JCP5T91lo_AFNFBi9RxBwZx5bgTWdQ15rSUL49Hk69RHnEsXlKkkaTF5RqBXun23pJvMXWZRx506pm4kMQVTQmj3Bi4yEENf4jYUV_DC9eNIq6sx7Rx6oBkOf8WPlF-cgpRJBSY9Rmw25dv9_XEos9pAuSmoRRHaEHbPAWmemA60dcJ-sx0_Ym-w-qymV0h8c6tFeX_2fHXr-mam5t_KZ79m5jXwQiRRPvT5NDa4yTr0ov5kJr6XEAQggJUKC3JSFN_3IZGLE50Jt8SFqxpbm6KHrtYafVt3zQkDNBUCQcWn9Wc1tzHOSuQLFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=q-iA5lygPzwjYucZvJT-7xRa76OC2ZKhHORl2FtkgdXJazkL5a1AsXZ67gwfjI5QXt98m7-bAx-cm4CE1qjw6IKS5M_1-QBwHn_E94-V-E7_E_XgaJEZjCr2OJ4SfmXchhB4DoUb5vmEBbMT0aXuYAYZEAs5xIbB9BQXf5C9DxkzJifX5rqujoe2-mFojwREL4CJB5EhIazkbj1M_8Wjj7JCiwPnToL_-tElv89KJy78x9zQuZJk-O_6qaL3UdzlkvYTPW2J3Kt-DtbUtz4YDWkHm1N2-SyUtORtVpn9hInSi_IQhHr8LBZTlV0vluQngLWd9kDmikHjCLhVkqhiGLMExzWAc7T6m1COS0KD76rSRYRXngAFImjigPI1F9DSJEK_CvfgikHR0oPf37JtTCScwDOJy_SMVxoi3t8y8l-_w3UWTeDVU6pGIEZG9ohm1mvVeJVJQMMJ5nCM4eJBhIqbJeIDYYkvx25xc6x885HImMTyu_pG2524owRtc2fvTUu-yNSIIJpZj0W1wdlfquHJx7E4v4RxD9_jHdMWlpZ5KlUTxXjLgyDExzOXTPl68LaLkdG0bXZe8UjQgPpjT0jXfxtWSqXR8YJIudHETEUsszHLhH9GaKZg0wVyS-DyERmVCFB2mDqMluugwwGtf9wM3Q6YdPRDvCli4JqV_v0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=q-iA5lygPzwjYucZvJT-7xRa76OC2ZKhHORl2FtkgdXJazkL5a1AsXZ67gwfjI5QXt98m7-bAx-cm4CE1qjw6IKS5M_1-QBwHn_E94-V-E7_E_XgaJEZjCr2OJ4SfmXchhB4DoUb5vmEBbMT0aXuYAYZEAs5xIbB9BQXf5C9DxkzJifX5rqujoe2-mFojwREL4CJB5EhIazkbj1M_8Wjj7JCiwPnToL_-tElv89KJy78x9zQuZJk-O_6qaL3UdzlkvYTPW2J3Kt-DtbUtz4YDWkHm1N2-SyUtORtVpn9hInSi_IQhHr8LBZTlV0vluQngLWd9kDmikHjCLhVkqhiGLMExzWAc7T6m1COS0KD76rSRYRXngAFImjigPI1F9DSJEK_CvfgikHR0oPf37JtTCScwDOJy_SMVxoi3t8y8l-_w3UWTeDVU6pGIEZG9ohm1mvVeJVJQMMJ5nCM4eJBhIqbJeIDYYkvx25xc6x885HImMTyu_pG2524owRtc2fvTUu-yNSIIJpZj0W1wdlfquHJx7E4v4RxD9_jHdMWlpZ5KlUTxXjLgyDExzOXTPl68LaLkdG0bXZe8UjQgPpjT0jXfxtWSqXR8YJIudHETEUsszHLhH9GaKZg0wVyS-DyERmVCFB2mDqMluugwwGtf9wM3Q6YdPRDvCli4JqV_v0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6561LlxSQkrLZgcUHh4nvl9OUOVKl7wtwiRz3-A3pIcY8zJs94TA7KouETEg8KQxmL7GDqEnhvqyVJmBB2C2vbmFikifYFDuS1vYB38sMhmKzosEmbGx6xYtbf4HUBC6KZLx8u-ELmL9jrE6IB319RGjubd6ZqcxNZe7m_WBO4742eEMODnFqV5UI9CCSFMopC8b4iZ4LxWnHNzhbX9DIxFvwr1Kj6v-QAEYfdECuz5sjpo1Buo4PhVJLDTKpbmyWShjTz_DXJFTMEKCmIDCsKdW6bM97o6Bv-LlLxThgMXCHU6TG4kpOVOuM-7f8jF-d_amxyVLw9ScTR-6lMJBoF8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6561LlxSQkrLZgcUHh4nvl9OUOVKl7wtwiRz3-A3pIcY8zJs94TA7KouETEg8KQxmL7GDqEnhvqyVJmBB2C2vbmFikifYFDuS1vYB38sMhmKzosEmbGx6xYtbf4HUBC6KZLx8u-ELmL9jrE6IB319RGjubd6ZqcxNZe7m_WBO4742eEMODnFqV5UI9CCSFMopC8b4iZ4LxWnHNzhbX9DIxFvwr1Kj6v-QAEYfdECuz5sjpo1Buo4PhVJLDTKpbmyWShjTz_DXJFTMEKCmIDCsKdW6bM97o6Bv-LlLxThgMXCHU6TG4kpOVOuM-7f8jF-d_amxyVLw9ScTR-6lMJBoF8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=FFNsnWBY3ggKccW3PubL47tPKiWCKDKu43bzMJMqcQhDEWVXXbBxs86PC4Hk3LQbffc1Vo8ET2bYvVI52ionnnwqf1QR26dviA18vEXrnSvhQlSWAG82heL0f2enFY-FshuPEgxTq1IdCZH4XeLf6LHoaCyF90AiLryU5A0XAKAHL4s4bJF9JgNYqkX09dbPcLGvypG8fhOwFWLXr6A3e_gN3JRUNh6vWm3cg_GTY4t56y1NBsm0eqrkKto934ularOsrmBaD3oiH3Qa69iMxyAjL6BaQiIMMqeab2sOprbb4EB5iMrAPPZOfCP5yeQ6jfi4CnlOCrNm9qKkvMAl6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=FFNsnWBY3ggKccW3PubL47tPKiWCKDKu43bzMJMqcQhDEWVXXbBxs86PC4Hk3LQbffc1Vo8ET2bYvVI52ionnnwqf1QR26dviA18vEXrnSvhQlSWAG82heL0f2enFY-FshuPEgxTq1IdCZH4XeLf6LHoaCyF90AiLryU5A0XAKAHL4s4bJF9JgNYqkX09dbPcLGvypG8fhOwFWLXr6A3e_gN3JRUNh6vWm3cg_GTY4t56y1NBsm0eqrkKto934ularOsrmBaD3oiH3Qa69iMxyAjL6BaQiIMMqeab2sOprbb4EB5iMrAPPZOfCP5yeQ6jfi4CnlOCrNm9qKkvMAl6oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=N1F24gXHgLDk5cL3ksaXy3CouUGoDoFEHTXC_adexsBb9JO6vneTIHOfUrS6l-FeVsWFR7BNAXWiCAh7eBA30xE6S9bjs54_aBqRNHq9nDh4y2aL3zAm9aIHdKG1X6r7Z2fI0EiuU0Nj86BKwQw1EeTIesGwN-YAaR8AWU91Krful4CahamlfbHNQl8CCZvn8LAGdd3gAtQa2SLBYJhwnveO7QIyF7j7c-Sy3G0eZvCTvcqu94-SniWhpnNaegsTsvGh7ae4-W51H2ICNfCJf4ruE34ATOUfP6uqLvt-AN5L3yGFY2I02YufXdNBRuVtFZ3zgrOzg9Qvi9FMnqbxUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=N1F24gXHgLDk5cL3ksaXy3CouUGoDoFEHTXC_adexsBb9JO6vneTIHOfUrS6l-FeVsWFR7BNAXWiCAh7eBA30xE6S9bjs54_aBqRNHq9nDh4y2aL3zAm9aIHdKG1X6r7Z2fI0EiuU0Nj86BKwQw1EeTIesGwN-YAaR8AWU91Krful4CahamlfbHNQl8CCZvn8LAGdd3gAtQa2SLBYJhwnveO7QIyF7j7c-Sy3G0eZvCTvcqu94-SniWhpnNaegsTsvGh7ae4-W51H2ICNfCJf4ruE34ATOUfP6uqLvt-AN5L3yGFY2I02YufXdNBRuVtFZ3zgrOzg9Qvi9FMnqbxUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u0zDtlwtPSRyCnDS9YkFWgPgwO3lBLoqd7-e7AtrTbLx0llhXvQTDNvpkTlmH8o7kiSlhi67W2QxYUlMLyFZhJGdJFo_4dg3Gc26_PLZR3NWRrmPknq0qe3lFFNX69i_O0A3_oH6kGbB7KNzGh-t60lfHTctFhM-nKDBncg7YnSSJkBjiA6bsGwXJTk9rx6A_CEF_Hm7KUeydgPZGgkL6EcfvnXGNe4J09JcMPgLHJp6O1YsZ4d1Nn-yWOKF1plzsbcNz7pLCksjZtTitJy0P80pBrr7WB8tBwy5Z_syk77NHmgFI6i1cZLhsHkD36iE3mSvNZ72GRdu4hbfEEqTEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kl3VckJClJI_mWWsewfTvfPEq8i_8grGB11ckhVUiaVNx1Gkbo7a_SX1fjaXxYj9ELtZtipH2vPMSWde16aKgRGUJ0NArSO8krzsGF653LDqundy5n9E0nPjKqO1QNl5GHclG6lATrVMDscgRmdILCurNljzvkNehEZNvgpxY5jQmAxyrU-ufea22X3F_kGRQWCAyejDLyTyEYTxV97o1Lq61g7nGcobkSlVsfi_LJOjKlimYeN56MYqYB7MiOrQ8jTeWlbEcJE-j6oKZXo8qji27ECIDxP_nr2OS27KMCpy7D7hUTtc2Pb5M3UD7eqeMjqW8BVkiBbhIekAhL_SBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش‌بسی که دولت لبنان و دولت آمریکا
به دست آورده بودند رو رد کردند،
اول ۳ پ در یک بیانیه و بعد حز‌بالله،
۳ هفته آتش‌بس رو انداختن عقب،
۵۰۹ نفر دیگه کشته شدن، از جمله ده‌ها کودک،
تا بگن «جمهوری اسلامی» این آتش‌بس
رو آورد! جمهوری اسلامی و زاده‌هاش،
اینطوری با خون مردم بازی میکنن!
اساسا چرا این جنگ رو شروع کردید که بعد رفتید دنبال آتش بس؟ برای خوانخواهی خامنه‌ای بود دیگه؟!
چرا بعدش افتادید به گدایی آتش‌بس؟؟
ادامه میدادید تا شکست و اخراج دشمن از خاک لبنان!
مگه الان ۲۰٪ خاک لبنان رو ندادید اسرائیل،
آتش بس چرا؟؟  آشغالا!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f2ceybxAVToy4bGpIEPt6TezPZzYaoUVEuZUndN7p3PDYPBPmn4aDv1dii0OtlIzBrR2fHtMo9xqpiLW-MyZ89fx97Yv9f4aF53crEe8D86_sIvKRRgbB5iW2Fdb__LYm_GFPuTgCzQrJPP_5zi-CTb3oYnO0kinyV32EGdj8LfmWMXFWGkYpjbGwOYG4Ik-oZofziwhwMPDxVeV3YWiIE2k7GUtNTpfXjIgHW9OH1PiuspQh4oG44lDQpkBFuvKBNAq9gK0W9XzBdBXchDa76ZC9siYLaAfM6m4Sr-JNhSKsKjXpKCneRTMqSWG1_BXZxjS3XbuP98CdvThzFE0QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NL6buJ4roN3NDUohfdRF8Xv5uAJ3OfoeICVOoMJe21SAX3sL0obEl5w1XB5hf4Db5bQS90wtqHgRG5yfZH9Ft2PR1sHJlqCbvus3b4vBuRYM5H9BSFbNrDK7MsU7n6l2yc048VZwZzvwK5ETUPNcNUoNw60mzyiJp5iwCDnIW40wpqdNpE2sfPHxQADN4PNtaJh-nCNZEiWttjABzeI-nCyHgAN2PbNxCW2TAJD-K5c099X9__KrNDK6ujSmqvV8wUE6HiBTkeZT3jtWYPd1CaZ7WKePrxaALBrnNUelYDAftLj-tkfUh0e-xYZCTE2vz6MoVn7XQXPBVqzM9HOYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOHmrRBKVOeBeZrotiUBV_1-CuVlNrmW5sUaHrDmfUFJ5uPt68yxN3sCU54IFDCbkUexgWSO-z02jcivwBcnbBcdOuEAya2C7HxEfMUo9svQ92mxG57CTiKwviS93qX3Yd2xHqyeLRfFdyZf9YUmUfC2VjmIz6GH3BUhDzTpPR1eJ9WJwDa_V0VkRR26KLCNrq4zbUAtFFyM3kmh_akqECg1Zy0dtenL9YthgtoCJpH2zvMig-pvsAphCj1FD1FeiA1yDmsoG0LWo2VdgKDhkJCip1THa4EUyPAEIwg0_Jn8FHCveLiCxQNOQiR_vbqEJFwRCOfgQESw0OfqBKlltg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=n7OlwSDRHbkUh4PzYiz1EDlajwcBxoyHX22G1arSE97HuKuwz8IqQvhNj_7s5pEwR61IPSHtTDUDJEtm9CDgH0fP9_c_uu1iKou99_gU45Z6D9WDUspS29IcuN1Pinri0fnEtWtrENYiKxhNdPRsgvIbSEdokt1CBz1yxn-eApkAtMgU5jnrKtrRs7LhWec4nq4rISwBcVugno8gjDnpICoP_zilxRs55LDqhk7GOoh1bDAT11tLDaj1yJUOHU61y3iyoSXc8JO25a02gs6sCbNZuoRFNCXVGQee4eU0HzfMKEhJ371frhP7nOjw9zjasUdMNEElKH78UHaAIEenvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=n7OlwSDRHbkUh4PzYiz1EDlajwcBxoyHX22G1arSE97HuKuwz8IqQvhNj_7s5pEwR61IPSHtTDUDJEtm9CDgH0fP9_c_uu1iKou99_gU45Z6D9WDUspS29IcuN1Pinri0fnEtWtrENYiKxhNdPRsgvIbSEdokt1CBz1yxn-eApkAtMgU5jnrKtrRs7LhWec4nq4rISwBcVugno8gjDnpICoP_zilxRs55LDqhk7GOoh1bDAT11tLDaj1yJUOHU61y3iyoSXc8JO25a02gs6sCbNZuoRFNCXVGQee4eU0HzfMKEhJ371frhP7nOjw9zjasUdMNEElKH78UHaAIEenvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=J4MUGqWiYhXqJ-KAW_HpQNtnwHveCNr6fCgQ06eDZp3-n2gHpmRp16a0yEv90t1suG1OuDG4CdLSI21IM4tMd7tXyxCZ1TiSlfAtFlXE8UTrdl6Lv4UGqtCbbpSFouqt0wuOHlt4sglLe6hgwlSUuS9F2g20FEzP_0Z26beRVjP8EiJBLEOt8Wfkv2k28FIDEHjWbhvKIGHj9BqCvWpjauO18abj0fpAwGNE5-FtNGvDHLSn_Hk6rCteKuyFDMPZqxYIJRy1RFp6oQVca72TR-E1jAPoBhkiPTda2e7qmpGIfVGOHxTr0mn0_OnC7Oya-M1PbNcZBoG-8FzeU0nutQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=J4MUGqWiYhXqJ-KAW_HpQNtnwHveCNr6fCgQ06eDZp3-n2gHpmRp16a0yEv90t1suG1OuDG4CdLSI21IM4tMd7tXyxCZ1TiSlfAtFlXE8UTrdl6Lv4UGqtCbbpSFouqt0wuOHlt4sglLe6hgwlSUuS9F2g20FEzP_0Z26beRVjP8EiJBLEOt8Wfkv2k28FIDEHjWbhvKIGHj9BqCvWpjauO18abj0fpAwGNE5-FtNGvDHLSn_Hk6rCteKuyFDMPZqxYIJRy1RFp6oQVca72TR-E1jAPoBhkiPTda2e7qmpGIfVGOHxTr0mn0_OnC7Oya-M1PbNcZBoG-8FzeU0nutQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSwSuBAj17SaHjfEydlFmmOgImn58M7HyJEZM9ywER81NuqbqzOLL3AO5Ccd6W2lTaF-gthATCV03JrqVnAoMnb98l6oiEtgJIpKZFh5dJDNgITxlE3Hgl9rtU2j-JKPQPImMq1nGC8qnuuGgTYULLn8ksF8uwhd8Ptx1cVM2tf7sqT4teOZnlJ2-HYEy4JlhyYQNtyBLSuZNQulSeJZQWC4qCxHj-wQXcdJc48TSq_n8qzIuX2mz5p-rptcBEFiiT_LlVXQ6XYRc8Od69IzbFBp2UBYDw5O2wxj8k3hKnSt485LlM0JEUeGPsnGn3dcm6YF7oTr99Gkba6-d4t4sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌
میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره!
پس اگه کشور ما رو کلا آشغال گرفته
و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!
مثل همین حمید معصومی نژاد
که دیروز براش نوشتم، میگه فلان مراسم
عزداری، توی چند روستا در جنوب ایتالیا انجام میشه! هر سال هم این موضوع رو یادآوری می‌کنه!  خب اهمیت این چند روستا چیه؟
پارلمان و حکومت و بودجه کشور و قوه قضاییه  نیروی انتظامی و قضات ایتالیا رو از این مجموعه و از این ‌افکار انتخاب میکنن؟
آموزش و دروس و دانشگاه و رسانه‌ها، دست اینهاست؟
از افکار این عده است که صنایع مد و فشن و خوردروی لوکس و ….. ایتالیا در اومده؟
یا از مناطق دیگه کشوره؟
توی اون مناطقی که موجب شدن ایتالیا قدرت‌ هفتم صنعتی جهان بشه و از مراکز مد و فشن،
اصلا این‌ افراد رو راه میدن؟ چی کاره‌ان؟
یه مشت عقب افتاده در حاشیه کشورن! هیچ کاره!</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moSxpUc2JnKInodra7dnt41Gg7_H1p6wg5XwpQdgTIXoSr1R7vH4zy_tKp3bNGZ0Wow-7RHpiMRLe9wshIwuUl_dTUwIgK6bJjdkj3UgfB19a438QNOLkmX9dN4wfz45Y7c92qqPtUy0vJ2B_wftm_qsJXqukqCVUBa2vpcJofRAZ1zrX9NCVFRId8ocYbwgJRQiH6YwFdQEASKPt5H2ybTKLMb7VGT0Ze4IpHam3_2Q-MAv9_-L952nNg5Itj0nWQrhNu1_g7TzEQa4U1WzCjzX0G5g7K0Lfk99hdL5oikGj5IMCmqlSt4eQq0lVOeywiQ49i0FAiySqUiaYrTg0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=mbntu6O_48cvMNM442l0EeFRvbiEU8yuJkJNc2B5ni-b-2NfAK6rp3Hf7tZy3qchSoMkr5JzVvvsgoEW-yWmL0CuddsGBJOFVjnzkBWTf1Lz7HMWNkH1UwGvUZsWk2qTl6PXCMUWRw6PCKNVTJgCcYNIBI4Zqv9W219nfySZd2Hq22s0uRNl0L8MntxicfLTWkvrDAwtx4az-XRx1ftbxrPXlm_R_b-VwRv_ynMW3MhAiSr6GNNbxR2PnCRlQ0BRrdEHpGdMNgS4AXAEkkKMsKO85qdNDS6d6E1PwOgXFlXoL6xZQkXz4MIPOB5IDNwPZrLja2f7Js6_mZIbAB1caQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=mbntu6O_48cvMNM442l0EeFRvbiEU8yuJkJNc2B5ni-b-2NfAK6rp3Hf7tZy3qchSoMkr5JzVvvsgoEW-yWmL0CuddsGBJOFVjnzkBWTf1Lz7HMWNkH1UwGvUZsWk2qTl6PXCMUWRw6PCKNVTJgCcYNIBI4Zqv9W219nfySZd2Hq22s0uRNl0L8MntxicfLTWkvrDAwtx4az-XRx1ftbxrPXlm_R_b-VwRv_ynMW3MhAiSr6GNNbxR2PnCRlQ0BRrdEHpGdMNgS4AXAEkkKMsKO85qdNDS6d6E1PwOgXFlXoL6xZQkXz4MIPOB5IDNwPZrLja2f7Js6_mZIbAB1caQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=pFs4eW5jllaxm1P6X4-AhizBMI_J5-z723I43iPQSFE5DR4wIv08WWwnDu22XSbFJlxwpWOs1XNgQWAsNdSbY9VI87sgk1Nj1sSrYP4P9OGgqHikP1nL3Zpw5Jl1TiJXTvKqHOmyHLOwdd8lWP-kJIy0SsCaH1GkjT965bFMt9ytxj7TWQyAqo-AXkVOFZs7lY6OeYEadWQ1CFek2b_lfqnix51kVg7ZbyuS3IRRF1r_-G3Ndg6WAzPP4LNwkWodptLu860ewXKYT5t6q2ROuE9eRWtC4P5Wk9G_a086GUydD-NnJ-3j0OhHga_u4OH84d_qiDfjINV6xQv7ccpJgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=pFs4eW5jllaxm1P6X4-AhizBMI_J5-z723I43iPQSFE5DR4wIv08WWwnDu22XSbFJlxwpWOs1XNgQWAsNdSbY9VI87sgk1Nj1sSrYP4P9OGgqHikP1nL3Zpw5Jl1TiJXTvKqHOmyHLOwdd8lWP-kJIy0SsCaH1GkjT965bFMt9ytxj7TWQyAqo-AXkVOFZs7lY6OeYEadWQ1CFek2b_lfqnix51kVg7ZbyuS3IRRF1r_-G3Ndg6WAzPP4LNwkWodptLu860ewXKYT5t6q2ROuE9eRWtC4P5Wk9G_a086GUydD-NnJ-3j0OhHga_u4OH84d_qiDfjINV6xQv7ccpJgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sdc4wemlDfKPuV1RoLxgZ4ZrB51RPvMtbalFS1j2XdgWjKz_DPCpO7h-Fot9zPO6bA0B13W0n4J2-u3CqPZan_6C45SxAPZ1yLCzMeL_Y0A7kZi1PNHLTsAP0UwN4HgpqA6Ur9tlSZHF_nT-m5rFkhYdTqanOzywiRvr99r7Q49m5aDnsLLwdszlRdjnOZwUxYy3MywARSNgmrYqCs4eziZSr8Zv_yGXYJHHSSkDD3Ir5KdYB0HYiHowqWkGCKCR0mUmWrlcBh3L5GHBh1WU1cG_1-KxLIOMLYbQMzl6jtYXMx0T3ezSjOsoIMhQzHUzmGoueo1BUz0U3bIHz7S4-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تاکید مجدد ترامپ بر ذرت و سویای آمریکایی
و اینکه ج‌ا حق دریافت هیچ درآمدی از تنگه را ندارد.
ترامپ : ایران به ایالات متحده اطلاع داده است که برخلاف گزارش‌های دروغین و جنجال‌آفرین رسانه‌های جعلی، ایران نه از کشتی‌های عبوری از تنگه هرمز عوارضی مطالبه یا دریافت می‌کند،
نه هزینه بیمه‌ای و نه هیچ‌گونه مبلغ دیگری.
اگر این اطلاعات نادرست باشد،
مذاکرات فوراً متوقف خواهد شد!
🔺
همچنین، ایالات متحده هیچ پولی به ایران نداده و هیچ‌یک از دارایی‌های ایران را نیز برای در اختیار گذاشتن به آن‌ها آزاد نکرده است.
🔺
ما بخشی از پول‌های ایران را که کاملاً تحت کنترل ماست، در اختیار کشاورزان و دامداران آمریکایی قرار خواهیم داد تا با آن برای ایران ذرت، گندم،
سویا و محصولات دیگر خریداری شود.
🔺
ایران به‌شدت به مواد غذایی نیاز دارد و ما این مواد غذایی را برای آن‌ها،
منحصراً از ایالات متحده خریداری خواهیم کرد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fOc_ziQPPPkiZYQDX4qb2AdWwzaY8wGsIcwpO7kY9230UsTUSgf-MXqHJhWC310d_yAuZU1H-CmYnT70IfREHs1Xj-tWfRd3nI3eQO8bTZHq3YKpeWPPTOcX5MJFPg-_kNV989zFz9CnlqNFI-k_lShtAtvy76eBmnPesf83WJ_UHz6cIMit9XosdXW-t6lz7zZJpbqQTJNBjRNZRCT1O3b8AV5RirJ1AGdXAjF3T6JyKpb1GxWCM5pzQZKkH90IeDg7UERi55LnEbBaOnkfQvzpt_FsdlMrLi-Ef4IsBMVwLi28shCxbTMoZVy4HEpWOclWobiWm58xLOdRB-CO7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KRhDgQvEDNioyBw9g6VJNJZEVhcnBxWqK-YlVFc32TMe7g61iedCgTFLFR-H5O2g4Gk4ipEpRiyZC7TBrxAZNEvEUEdYCZ1oWZYxfI0lJ2rdN5DNlK1ck99Lj8nSf7UXEcuLTpIpKY2s8RFppUI0qckTLED5WTY2vpxsxT66E14TESSmWhoXdhkqVJ65-RWsw99tl4IwRdqhyyEF0RagvUR5deed2_aMUGNnIw19iAdaXE3efyuEQCtMLUxb9ZESqRqeX-PTXERVRGzt8_6uDe4jygARUbJptYJk1C_ECvCcsIGM17S3DU_ZwH77Qe8YKR_CS_Z0qtSpzrBpciofDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=nxj-ky6d-qFpntKyBP062GwX5YH09ze3Jp_zvOVwxUfC6tboGqo4qqOCfIjTgZ6Mg9cN58NIEaZV75Tk3UYPY9wIFLoHSVApvkjaHzUFmpa98V9iCm55FIT9_YK6CDPt0adeMiKVmkCOhquj6nTEYrduU6fJmUNktG8ZJUauDvfGeZGcvZbRYSMTDPnXymnaxouCyN_BMfd3RXXTMNSnWpg2gYHycHSpTGOH1vpjysXnY9QLhc0BZGodz1eATiWZmenPsMQ4ufabartnZsbN4KHi4ddS3RsroE8a2MZs9IWO_PThV18Xt-L-dm-eaOtcYCUYP2_rYfvuYrTY5nAJiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=nxj-ky6d-qFpntKyBP062GwX5YH09ze3Jp_zvOVwxUfC6tboGqo4qqOCfIjTgZ6Mg9cN58NIEaZV75Tk3UYPY9wIFLoHSVApvkjaHzUFmpa98V9iCm55FIT9_YK6CDPt0adeMiKVmkCOhquj6nTEYrduU6fJmUNktG8ZJUauDvfGeZGcvZbRYSMTDPnXymnaxouCyN_BMfd3RXXTMNSnWpg2gYHycHSpTGOH1vpjysXnY9QLhc0BZGodz1eATiWZmenPsMQ4ufabartnZsbN4KHi4ddS3RsroE8a2MZs9IWO_PThV18Xt-L-dm-eaOtcYCUYP2_rYfvuYrTY5nAJiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9UT7PepDfUgZ3w2k50iOe66w9BeQrU7tX65wenccdxDD9CFZKAGciArDeK_PuG8NnvAeFKI3c6WrqwBxgkpJ2eBzi_zdW1ZVv7AUINvaXm0Z6V49jEq0InW4QIrOCV5rrEuR6lfRkc9bI0daf6ym_WTdAVLe1PpuvgakzRdGs1DVTyW8srg_Ne0qmnY5xUKSxp5lW125biMD6BqSp9chcHEPeX3wZFZ4yXI1SozfJnOc72pugaU2xxKgvUGPBtXRx6HPA7Zldvy64W_80MmME2Y4lWBWP5PvL78QAnbL5QtE8B7oVSeZ8arkTq_3ze605YoferxzOboggox8H1uag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STDhdyc79FEgR-zBLnRVSBz1TRIOftuHI-PEW4zZPLyjZO8Ykzgvfr661dXlzPSZk7KCt842j7XozP44q37VN_IwsPQoSB4ztXo3WfIiXPhFaL6LRYOI-YfQy2xE3RUWb530eOR_H2eC9h6XU0eS3G6dXgjcKJ5VkHHqhbl8Y95YYL-c6nIZD3yv35PfSP1E6xJIpzuyevHhZYjgNsu6E8WtV7tVOIwjruEFqJRHgwbfpVe1kVLEBa3-LvM-G806wjOEmvg4gVgreUUnfH8v5EU5jUdW3Z8xYI5rs2XTL_RmG7VvgplwVkBqViMdn6Q1FEV3vbljC8udSPmPPKIzLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWW1WS8pLppRT8tor61uw3MuAS02n3kz0wES8lFFI4WD95KjMSq0YrtMoH-OFBApjad5rDYEo0jXlGZaug3pzUglv-9jGHB7xMbQtZuDVgWDrgDtnJw0ztR2j4Q_DC1GNky5nCgpRJNMECnJPP422mtmHh-aowmmyeLETOlwArfKEnjKIdmfh-9bEzcEwgDS7KeQxaB6tGKsqmb9Ecif0HuFYmFnYOmIxIXydinSAO9zqU1crFgH0Betee7bwETrVkD7u67092HidN3l-R-uJQHSAs7yGXVIg8j4JwTwzEaTR6JR-yLCtwsWuPLcr8qnk9kS5DAvOlDT1b16eu_afQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان ملل گزارش داده که در عملیات خون‌خواهی خامنه‌ای، توسط تروریست‌های حزب‌الله ،
۱۱ هزار ساختمان،  که میشه
۱۸ هزار واحد مسکونی کاملا ویران شده!
بیش از ۵ هزار واحد مسکونی
هم بالای ۵۰٪ آسیب دیدن!
هزینه‌ این عملیات قهرمانانه!  ۱.۳۸ میلیارد دلار بود
که قاعدتا باید از جیب مردم ایران
پرداخته بشه!
بیش از ۴ هزار نفر رو هم به کشتن دادن
از حمله حدود ۸۰۰ کودک! بیش از ۲۰٪ خاک لبنان رو هم دادند دست اسرائیل!
🔺
آمارهای این گزارش سازمان ملل، شامل ساختمان‌های ویران شده در یک ماه اخیر نمی‌شود!</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZyTGF2K6br_GcyUgFmyW-qZkJilTOHHS5qMBMYkLIFpDHvLCwXhQiRPGy280EgayohF9nhxWxfaESBADCUeMNoRZbqnT8zwvCkMUaEfeq9tgx47nJAr6eeMMv_I-1uIkzgGqvZTGqzITG44oOYCzD9XahaA_W6AzlBm6r1OKp7oX3aHgyOFOp-70hR20Kf0Olvzwc0fxqe61tgTleq8KEXUCXnNyDPJ2fQ2zWjxh7ekRSHCbjRTXcZnro6zvSk3cACUg5pHMn7snSsW7Eb-6S741PKquaeCaWDXd2iZjOqZjVwDwdNmkaHjDjSLzaNg4JFmeHTxesqgjt6UYepu3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=KMq5XVf1n8FNIWjFsVeRsGOvb0uOCJS1t_ljt0H2wOo11D63g5X-6ea3YhnAUOHIT_puDKQLWMqNdLF6GGUPk5VKYDLwAQPnL9eTUtChhFaqCEUJ-IkS4IMVmHylVkxgGXQ2x_egQmb0OffWyWQGLOXdbNVvN1nMj0U-ie54csvbyTcr4PWbrdPpnbrpdxFx84bXo-BcfM5VTDfW247bxdj01YHe-2H1wWOwGxFZOMcwg9ZOgcuqIIPbJgslVNNVBCbzrfokw-GASKbxxkCkJqUReLe7ukGt0rJdDw8jSEbJHQEwwB0Y3fxDCd9Yu6zu-NQft6sPI6l9GO0kQUT5NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=KMq5XVf1n8FNIWjFsVeRsGOvb0uOCJS1t_ljt0H2wOo11D63g5X-6ea3YhnAUOHIT_puDKQLWMqNdLF6GGUPk5VKYDLwAQPnL9eTUtChhFaqCEUJ-IkS4IMVmHylVkxgGXQ2x_egQmb0OffWyWQGLOXdbNVvN1nMj0U-ie54csvbyTcr4PWbrdPpnbrpdxFx84bXo-BcfM5VTDfW247bxdj01YHe-2H1wWOwGxFZOMcwg9ZOgcuqIIPbJgslVNNVBCbzrfokw-GASKbxxkCkJqUReLe7ukGt0rJdDw8jSEbJHQEwwB0Y3fxDCd9Yu6zu-NQft6sPI6l9GO0kQUT5NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffpqzKnv1OMgvR3z9ZCLANpWbMjlV9Pj8rPTNTt_WbN9-w-lVTLZzm88JKXxp1qhX7WudH5BYCikANZGN6H1jLTN_2-EgXJuXG2f2bhGnVBarDZQnVlINwoo6F7Mk9nFccI-G2MHvVCO0LZwkUsSo0MZr_spcSfby39PXHpllTSkJWJPFDiQxoBIsbkOhbAtGlPumeKp_X63dH-ryDaYdD9HrkawPWbb04DJ9o7BCaw6cLDB4r2ZNXYhUPlpItL0I6ALoPmxJYLF4umEV8KRhUzXm7huE4pGd8n4fn7AcR2IMpvqt33LCO_42DQwUG85Hi3eE3IuANqRTPuKrRYT-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLnvj__EXI7QP9LMmfl0jG0A7uKNIu-PRF-oiPtVa5fMZlpamP_TKLabM_YWApCiIf_2_9kx4WbXt4bMu8cYx-dOePHjnECtSd-HxSBvngC73CiYduRNRSZZ4cysWvt2JryQn6o_CEKVortAluZVBSACrrEhie4bCQMKTU_WFo7BvMBgxDBGO3jW2LmbPysAQJDBSo0abvABa1Z8EyUO6OusehBztRDKpR0Tupv5CO5cdExJhsjjrbbVwp0Ovu1PBswapEspvuWXT2zLeyzDVBsQUCG5paHxq1rpExNRYjXOt8dMeQ_tUgZMWCUOe-ZaDnxQqt-U3i1inmhClzicoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiLnLlKcyidpg_y8hD-nAkBtrCl2sDR-NxZ9l0jZdN7Vrj_DeAREOtrBuQJty9Kpup0PAC4LeRNDITF-3E7lB4H1g80jec3GfzGO-CjcNOFfD13oPTlxxV1xAWbl784cNk5rW5TfXv6FSTZWnuvT0H1HWN7llU0xfQrJvR-EDvlH5XUtLbhSZdlWGOQcm-ua8CcbRxSmcKypYwhVk67Ei0lKLs_F3gyrpoGFAxYhVj6GmF1KVPGap_f-HKwUzV63kCbGMAKup7V7d0vdL_8fFIldJIFCAI_yPgtbm2eudV1VZno3yPrS4vA99S9uhj0pkfWcbVKjj1fZ4qpZnpNyWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی
فقط با سنی‌ها دشمنی دارند؟
با یهودیان؟ با مسیحیان؟
حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.
توی کربلا و نجف وقتی اونها رو می‌بینن
دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت کنن. با افتخار هم میگن
بیرونشون کردیم! انحصار طلب‌تر و افراطی‌تر
از این فرقه که با پول نفت و با پول مردم ایران
فربه و وقیح شدند، وجود نداره.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5706" target="_blank">📅 11:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5705">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=nJGnnfPcgYcB4ackte5lPfwkfFn1Hk9GwscyHYJSuZ6iN5wB9Ps7Bt_8vVR099aOBF2HWcQPRtTfGFMb85Y3ZeUE1kjEPDQK0DkTg59dGhF9tAauSvEjJmFUp7dIz5nxLK3yswxLwpQEHKvsT6Ouix6kV0rFIU6KbA4b2oXc9nM8l3EHKRXgbBZSs_fUsU5YGL0K3ytzqNUsE10Skucuj5bvVzldpMdMxqidZUbVVSf1zukYwSsxOTTDKEXE5s7MnqJlTqyKwAl2EaYx7EUuu_QBY4fBveAIDyI2cXfpg8ES6QFLAFPHuLdTZacbA5wH49mcOZY7UwlWUhMHyxDLYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=nJGnnfPcgYcB4ackte5lPfwkfFn1Hk9GwscyHYJSuZ6iN5wB9Ps7Bt_8vVR099aOBF2HWcQPRtTfGFMb85Y3ZeUE1kjEPDQK0DkTg59dGhF9tAauSvEjJmFUp7dIz5nxLK3yswxLwpQEHKvsT6Ouix6kV0rFIU6KbA4b2oXc9nM8l3EHKRXgbBZSs_fUsU5YGL0K3ytzqNUsE10Skucuj5bvVzldpMdMxqidZUbVVSf1zukYwSsxOTTDKEXE5s7MnqJlTqyKwAl2EaYx7EUuu_QBY4fBveAIDyI2cXfpg8ES6QFLAFPHuLdTZacbA5wH49mcOZY7UwlWUhMHyxDLYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=u0y2UtZF_LOM-_VE9bQWaUAIafzlQ_iqmTFsXND09g3i6z0oxCFgyRXWhHciN-g90z1LPX4neIynQtBgVHQvcyFgbe2mXzZaMpRZYUTZ-Ozw5rPg_A-RY_vcd9SlrElfhOqP7r9BRzpcKGgD0-sY5o5fX9klAMyxpQQ8o86AQpFNP15Hbfcm5cqk0b3i19jdvG3gIX9-p3LpaE6JmooVDi1xsFn4LF9YxldFI01KKOgunMp8cWk5toftkadnRDhzltIrGmH4i005hT6rKNqfkEP7DT-d1HVXl4gMwzForyHeTVwlITceVRxt6Zt8Q3nYwCgJSC_Bj6mlNYFcf0hTdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=u0y2UtZF_LOM-_VE9bQWaUAIafzlQ_iqmTFsXND09g3i6z0oxCFgyRXWhHciN-g90z1LPX4neIynQtBgVHQvcyFgbe2mXzZaMpRZYUTZ-Ozw5rPg_A-RY_vcd9SlrElfhOqP7r9BRzpcKGgD0-sY5o5fX9klAMyxpQQ8o86AQpFNP15Hbfcm5cqk0b3i19jdvG3gIX9-p3LpaE6JmooVDi1xsFn4LF9YxldFI01KKOgunMp8cWk5toftkadnRDhzltIrGmH4i005hT6rKNqfkEP7DT-d1HVXl4gMwzForyHeTVwlITceVRxt6Zt8Q3nYwCgJSC_Bj6mlNYFcf0hTdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=JoQLhPs0vP4WdBDkZWMjouXqKaRwtnhVE-8JDL-KJo90clwIubTaqzKhdFlMKwKI0gjk29LIBulIjMd0qiFz2eEe9Cef0uzu_UltW07wAMWU4AwzhZAV5CgaCmBHs8WsBcv_U0v3r7Vrg8gzXcjHS9CgBOack0HmsnXZDMrFJVsjeUgu0ehoGraD7U_tpXq9yfdbMD18BV71RXmKbi4kkoT6AV1hbjvmYan29pC3AAbN1s1hUEgVjzRb8V-M7MVPANN1zvcsyuwa5Lo2e3LPesF1NhqL0UtQCkAD6WbPiS_4Wp91RMN_U4Ochr79mIHhZt1z0WT-0_WYiZtKhelA_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=JoQLhPs0vP4WdBDkZWMjouXqKaRwtnhVE-8JDL-KJo90clwIubTaqzKhdFlMKwKI0gjk29LIBulIjMd0qiFz2eEe9Cef0uzu_UltW07wAMWU4AwzhZAV5CgaCmBHs8WsBcv_U0v3r7Vrg8gzXcjHS9CgBOack0HmsnXZDMrFJVsjeUgu0ehoGraD7U_tpXq9yfdbMD18BV71RXmKbi4kkoT6AV1hbjvmYan29pC3AAbN1s1hUEgVjzRb8V-M7MVPANN1zvcsyuwa5Lo2e3LPesF1NhqL0UtQCkAD6WbPiS_4Wp91RMN_U4Ochr79mIHhZt1z0WT-0_WYiZtKhelA_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-text">🔸
گفته شده این آموزگار زن به جرم تدریس آنلاین به دختران و زنان که از آموزش محروم مانده‌اند، این‌گونه مجازات شده
🔸
براساس گزارش یوناما طالبان تنها در سه ماه نخست سال ۲۰۲۶ دست‌کم ۳۱۲ نفر، از جمله ۳۹ زن، را در ملأعام شلاق زده‌اند.
🔸
با آغاز سال تعلیمی جدید، ممنوعیت آموزش دختران بالاتر از صنف ششم وارد پنجمین سال متوالی شد.
🔸
آمار یونسکو اشاره می‌کند که حدود ۲.۲ میلیون دختر افغان از آموزش متوسطه و عالی محروم مانده‌اند.
🔸
زنان در افغانستان با محدودیت های چون اشتغال، سفر بدون محرم، پوشش، فعالیت‌های فرهنگی و ورزشی و غیره روبرو اند.
🔸
در پی بازداشت ده‌ها زن و دختر در هرات به اتهام رعایت نکردن پوشش مورد نظر طالبان، اعتراضاتی در ولسوالی انجیل شکل گرفت که به گفته یوناما با سرکوب خشونت‌آمیز مواجه شد و دست‌کم دو نفر کشته و بیش از ۲۰ نفر زخمی شدند.
@RadioFarda</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5701" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5700">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6hvXyUzcMGyZ81YCgPY514uVNV0MfP-vI009NxdngVNN0uFtjcxXA8GVs62IHXvObyDV3H4FHppiYy27gsL6jQ6b7K4MOeRQ7u1Z7yFge7c9NFZPCce9116lQ8UqxfDOIaVCNnkHFuQa_35ZiA7gHRptzudo218Qu8TG23-BivM5mnHyrpUzzfGjKUV-IopbIQLTI2v968YPYO-m9LIWLQY8M_RlTyMiA6_TO5FISWME8K8IAwHGCSsiszN_d7NVgimDkIRs9gaf0s2yMkC12oeFHD052O1LYG_BPZwwZPJVYN-mTb7HydsDWFVrU0NLn4vVq3ZReVaQIGFJwjEpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
