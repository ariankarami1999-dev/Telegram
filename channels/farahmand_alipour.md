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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 12:04:43</div>
<hr>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=nIYYyuwuGqilQdKhS2iqJtCPyGzP1pSifxiIWIYY8jRh8YlBVYsTPhDo4Ui3yH1tkNMHvTnUP8eGro55Qfh2OtcXAAExTQ0Wwh53iu0pXgW1hhsoD8qInymMZiDsykeNfPZ9VkIyFFk2bLs-wqps94-ZeqKqxj_4IxbeElMrGF_yq72Mt17FoM8BeD_bg9sfoV04gG_E1a9ucN0XvYKU7lNTp_nGunBcnOSvJkk2isO_nv3iqo0a_t1dDa0ioJv5QevRqYc-hDr0b2eMsKluollpuvv29hYjzpLPtzd7kuPcRvdrdF88eY6KPG7whzTZCNrjX5wfPj63ceNC-WiKTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=nIYYyuwuGqilQdKhS2iqJtCPyGzP1pSifxiIWIYY8jRh8YlBVYsTPhDo4Ui3yH1tkNMHvTnUP8eGro55Qfh2OtcXAAExTQ0Wwh53iu0pXgW1hhsoD8qInymMZiDsykeNfPZ9VkIyFFk2bLs-wqps94-ZeqKqxj_4IxbeElMrGF_yq72Mt17FoM8BeD_bg9sfoV04gG_E1a9ucN0XvYKU7lNTp_nGunBcnOSvJkk2isO_nv3iqo0a_t1dDa0ioJv5QevRqYc-hDr0b2eMsKluollpuvv29hYjzpLPtzd7kuPcRvdrdF88eY6KPG7whzTZCNrjX5wfPj63ceNC-WiKTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPC0_tFl3pbMOow3W4bWk5VLuLoGY6TM0wFhOo1zV30sUUIE2nxt8F0Qs8ZVKN3E9FEqYAX6_2EaMrCNnQZ47ytAZAcJBPiXKPVowGdjzDSeGbz5QtxvWFkumSwOL6q92qbYNh7IYjcJR96LSDjBGnRU5jetamb7s5hEu8s6jLvpolYBz8semwBTaXFL0kte8jHkQK4MLV17B428zZRq58x_0PqCSz10ZSRmV6yrCIQmvKevm2IEKwFWS_0nbJiZmhoakOqvtPVQjnzXq6aZoKLRZfdbpxBU8ZiUcim4F_fzWQ0vMzCgdFBBc1kVsztPDzJwCh_G9lvtG0ZhMb8cxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYaHsv2IVNm9nRk61lBOzxSKSanQRBiwJFHs3jJnL973EvD0q0z46Ad4867yHg2afmhhcyv_lMn3EWXovOLzkOBm-bdFvzxK-3lDeSDdS9OXhVyVHuoQPATDHEzWluZIjyEuQkXreKuYBpD9Qbb5xw7_3Rvn5jCiUSadDkhrhmto-frAOHhHpyBLGn8c8rNRVl9bJBUjCt9i0Pt5PZg1JG9UR2q5dgzESslqL7iToavuXjG1IIcBFzVlkLh6AaUPWza2jloRtZa9SGjqlZ6z-kjCpy27jYbsLX-h0o3f1hZSPyzA778k5LSET7KOdHuMuLt7DGAz16mQxURs2nzmWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=pTE_pvYUWo3TAWAEmra0aKYzeid9S6K5VZf6MAb_3U2kGlfC0U192pI6Vi68x0-h_bnTxprzBr8NLqCtTFhFBBsQFUfKUuzyLRjjWfCYSXLGMWwjoWb9cdc0SJhkBWsNf8lCqDECu2NK5HErAEFRAV0RCFNfFOQxH1pxq0ebRXmCKKHt47YGPQmlpkXZ5U9p96JblQ1DXVvt7ia1q61L2dzvwg7ajOgO0GaVhiW9R4VFAtZJSieYkLRYDX3bbA8jr3DcoTa0rINI-jE6rqGh3wqcOSLHfjE1DSPMAToV5MGSIqn9_OxkvBKaPdrqijkdLlY90YlXQV_IcuRzjWMgszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=pTE_pvYUWo3TAWAEmra0aKYzeid9S6K5VZf6MAb_3U2kGlfC0U192pI6Vi68x0-h_bnTxprzBr8NLqCtTFhFBBsQFUfKUuzyLRjjWfCYSXLGMWwjoWb9cdc0SJhkBWsNf8lCqDECu2NK5HErAEFRAV0RCFNfFOQxH1pxq0ebRXmCKKHt47YGPQmlpkXZ5U9p96JblQ1DXVvt7ia1q61L2dzvwg7ajOgO0GaVhiW9R4VFAtZJSieYkLRYDX3bbA8jr3DcoTa0rINI-jE6rqGh3wqcOSLHfjE1DSPMAToV5MGSIqn9_OxkvBKaPdrqijkdLlY90YlXQV_IcuRzjWMgszzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwtalJuI4ISK7IQV7YrAvbHJj4aZpfjdhF9SZnPXUenA8e3JE6VYZ_JgQGbOAe1JK-AzhTyC-u6Ps8BU6bRa-JO1s_WMStSN1Uv7k0F67k970czKZ1Tm98V19lLVw9QRv5st6M_c0-tNi6nh_ibfKOrsdtxJFOGxW6YmxiBJuEa8oozwQrqUZsXwLC1dqMU4371nMe5z6ufR01qgVhDsgJxFeMnRBMvBYgjtLw8w02tcuhsPJbTHlZg0f6pPtYeWjGsN6844T1At9MdsN4Y8i-AwutsrC942gOzp7EnQDrtgr47tQv422sdIF6mVPhHsfqVYxNfFEM0gpUgqxz3tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkPlS5eGMm6Yc2WSpo-utRTSYJ8NveD-Uz_xnXbrQ5OdIOrxaejh4CRYvlbHJijvdWWxn98GV4MadzaLXfnGpTa-prm-wjofhmQjv_pwdLPBS0uIL-6-w4udEWjpNHmXeDi2_W1wBepQswCNwdXVRXlxvmP319q2M8DCnIeZ5381YrzMrIESYlV-3pBN2MSCKLtffFE8GFvQB3MqEiW-XV4Ebomn1ZZP4GBetgeNMsJ4tKrVoPuU9I47u72Deo-xMW5d4YXMiZLm06cBEcoJHFyVGFg_YnWkrtkIbx37p-kmdDJhVdOdc7oOEoqSR5GFelXpdoqukKaWxPAmtAz5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKj_RbNEOApa6XNKCrrK75Gw5e6ZW1EVOpYxKDb6Ux3P_MCLKBpD8crp4tmqBODk0DBVG6X5CrJuMPlligOXIjIUDciCZGi5wMBIiN2oXrD1eezOH5TBeUTDaMamIE-US9vzUSJyExD8-cyxZsXsLI6aDalTb_jzM0fSw69jzDZjlCnxH6UHvUOi743zHiMyPx6y1y5rDgLXs3Yy_uQ3kvKpGXbUPfO9YJEfprhBXxV6a-O611YvPpu5F6USuis8KmI1CYNg5iGsKCT4vqfOx-TJlWFkGqdpVu0aQPksQIUXm1P07_EdDd9XUgLJiYadFvxxCMeLZ-Tp4jpKYEDnDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmKIYoON7V6Ue4IkHr6qG7AVT4tY2Ozky8KeIfbSAqpNh62uYZwH7vemVUT15BNcjb5AjtcsMNXTKvPU2ZJITBXwE9bjHioiK5MfFCLo6F2SnKxt7b5upzfJovKZEPAMhR87YZsoUiR2E_9jwY3KPlTr0QTsS7OpNAeU3V35XqFjIbD3lABISNE4dW9TLcqxnw05fEaDX-tk0S9AkWzHB0j5KywpFhMFNJ4Jn70AMEQCiayYtpFvPCSZUY9osiK66PyhE51ayLuFt8DcGu_IMvJaiBvArbD-RBLN6n9zuJpe1tyjaK7wmCdj0cAnPeypBDf7IKLvd3WVngyZq6Xn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m46TuP3PAp490yyTC_6e09TgZAx8XWoRcMECmbj6fcvYVRoeicLLevldZpWfnzBzyY4woizHV0xqr0FG4zfqtSoOZ4iLdrOrkLOXw79rp_1EZd-PyPvlw-0GqVJLZlQIvtRaRAMTlUHkVpbIKdfjXT42CvmUxKyPNp7YQa8L7gtI2aImBYzy3FM05CHdDZYei0B5Mf2meSKimT_160ytU_tTh0L9vL94IdqjyTmeMsUl_ybzBXveR2O3rEnX-aanuHjlN2dKwdIN0t_58qagDMn90noEcYuBuMa-vjw3PZRd6kUVBZk5DXPoVX_JBnNQm6gHPWbx69tyAohLzN79fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mQfqmpo6GuQ87K3eC1N5it_xQiyu-XZ5sqCkdd0NlMWeNc9K0g51Gy5kkGxEPpb7tD3OMThd-x00YB8LW0zQMwM59MZ20_OKtm_jMe9U-Wd4d9CJxSHXeFm43IguGx2Y9B8kXGdhqgYP28IWx9r8WqQi1bdOmYIxxITzk8Grx-LCE6gAVzoAIBmSR8aAjThdfmbQa7noJuI_QrYbfsJQChY3MGsigdTx4yjYuZrfjYMZKFYsFlWntdkdiA-lEerFznipD2tZcZJIwxcc89uzlznqmICFgGWE2kTvwV1vlfo3PGng1D7mQhrfisVmfSgi0LMDL6sE4iQ0-tuFmYT_BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=ZJHobNxnyz0MSzXb51C6Saf6TQAG9rbpSu7twUDRmNREX_eElKoRDQ-9KAgX6DoCl_ZuSeSh1fYMOiIxhN0OHf0MkVpspPtcvT5oziEl17lhRZRNdYcKRRvs3fh5W1Vuqr0pKtMHFObdhIQ4LXQktUCy4j7tVZ6lRgGWzLegFWJDVw_KtMddy_sybGGDuvBuRn0JJS456xl_I1ty-E3-YU4xk5kEjAQmNWFpVfUBTZqHAIlCFBe1YEXVJCDtYcGuDbFY_VlGOV3_C5lq373D30r7vsg8RpynhhpkpcL_GP_qpYfJnXIykbbc95IwBAvh2E2tUbcryGiyEcfiSPWXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=ZJHobNxnyz0MSzXb51C6Saf6TQAG9rbpSu7twUDRmNREX_eElKoRDQ-9KAgX6DoCl_ZuSeSh1fYMOiIxhN0OHf0MkVpspPtcvT5oziEl17lhRZRNdYcKRRvs3fh5W1Vuqr0pKtMHFObdhIQ4LXQktUCy4j7tVZ6lRgGWzLegFWJDVw_KtMddy_sybGGDuvBuRn0JJS456xl_I1ty-E3-YU4xk5kEjAQmNWFpVfUBTZqHAIlCFBe1YEXVJCDtYcGuDbFY_VlGOV3_C5lq373D30r7vsg8RpynhhpkpcL_GP_qpYfJnXIykbbc95IwBAvh2E2tUbcryGiyEcfiSPWXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEvWwtapCvzT32cBrsDPqZXhcQUnuxedHS_iJ7qfVmFUSn7L6LcDe9HxKatepZaNUgccA_hbw6kfciCk-EQqyRBWpKl3-x_cqaw8Bd2xBC7MVaWIxOS7wdK63xPeTD6U2Hofmu4LW_Wy306hrCT8naZD-OsjZ7ILlFw-O5_0rlybykFWWqnj6ipoJfvVOGJQRBbJsHtD3T3FGT_nzCG0OvmirC9yWRRxUv7WhlU5ej-LjVRkCJyWV4YbUVVyGbs07Aijguk7QeA3uBfZQ61cEKidIm-f8CtlV5oNi-mpUW8u68cTokT2RmcKkv4L2H5RoeKbs6RCcVtyntHISQ8zmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQuMKM6YOelISeedi510seEPWFx8FR0vDe9pNlAaAbFIK6Yj_RJX6Okf0KOris9DsyifdSLxSkVFROmwwKtjh1TX0QyZkeMeZDXYlhTtDJgjVReYdb46grEkz90LY8uRvbsVreHLnA0NO1nfE1xtYj0upxvaZwQei3Zn3T7iZZUJ34WlKmqIutFPloXPXa2eytu4Y2Q6315KgrJzZu6K_hPQ57ge-qeZa4OLIarmGDYGeXQzzklUlwqB_934H5rkN_JhaYQQv4DKs2uX9hhEbvsPNY3fDs2CB-6m62g6HDREK8H4Irldfym8mov9NiwjPYLTJUAMl5wuXXW4cPuxig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=h5rRCLyeYsDJSVmRMGsJKaHf3bRSH3y_Blk6Kq-jztsTBkQc7RkbUslDCNlyuzzU5OTRCTUIXpZHFaYiTawrarGofs9J2W29L4nXQAvPKI2OcbknYT4WNk8liBNs8LjvEV-33yiAtqYDo4WOKw1XLQ2zwnJ1LHw4S5qHqRYbC-Xv8rj5UdKykVK12HNP-eH5kS49S0RU37lJCk0HlYwuZrwb80vT2rNyEQHQdQ2N6jTOXgjpAeP8O22oKFJTuDadA06Uc1qi429L4R0GCiUX3mRsauBvo-c_rHAeGGNb-TxwlJhgBYSBjU3Yf4FSUF8DE_uT5xqRPhRTycmB4FNA9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=h5rRCLyeYsDJSVmRMGsJKaHf3bRSH3y_Blk6Kq-jztsTBkQc7RkbUslDCNlyuzzU5OTRCTUIXpZHFaYiTawrarGofs9J2W29L4nXQAvPKI2OcbknYT4WNk8liBNs8LjvEV-33yiAtqYDo4WOKw1XLQ2zwnJ1LHw4S5qHqRYbC-Xv8rj5UdKykVK12HNP-eH5kS49S0RU37lJCk0HlYwuZrwb80vT2rNyEQHQdQ2N6jTOXgjpAeP8O22oKFJTuDadA06Uc1qi429L4R0GCiUX3mRsauBvo-c_rHAeGGNb-TxwlJhgBYSBjU3Yf4FSUF8DE_uT5xqRPhRTycmB4FNA9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0jrkJPyYHzcBixSoJjM8QRecjJ2iwZlBHcSSd8NuuLMTbmhnPDZ9Ty_WFD9p4nPTUDIgeDBzH-IHLOdU8A2ETRfw1TXF8QE5EbJmPdOdCtddRKBCrJEchV3wL8BfMpSQBhTqPlNTfQy3qbVdv1_1ZioKfR1HWOouNrx5wYIFwG79Y4-dd3QJI98b2dAzMS6FcETPqgU5c5LNxX3QxtBHmcNK2vAO3RYFX5c8_B183gYugzund9i57gZfT3bg0x9wbcSt0DJU-i3rGea0-0H4Hq0oDjONcaJFSAyrJEcYPWmMx6G4pinzYSI8SVDcrgkm1kOhRqC7sZ1dPH-BvHbjOlI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0jrkJPyYHzcBixSoJjM8QRecjJ2iwZlBHcSSd8NuuLMTbmhnPDZ9Ty_WFD9p4nPTUDIgeDBzH-IHLOdU8A2ETRfw1TXF8QE5EbJmPdOdCtddRKBCrJEchV3wL8BfMpSQBhTqPlNTfQy3qbVdv1_1ZioKfR1HWOouNrx5wYIFwG79Y4-dd3QJI98b2dAzMS6FcETPqgU5c5LNxX3QxtBHmcNK2vAO3RYFX5c8_B183gYugzund9i57gZfT3bg0x9wbcSt0DJU-i3rGea0-0H4Hq0oDjONcaJFSAyrJEcYPWmMx6G4pinzYSI8SVDcrgkm1kOhRqC7sZ1dPH-BvHbjOlI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=jBH1VRsVrzo3pfrEY9b0KEKFLDYnRtleKFN3Tk8owgTtebaWz_ITQrqCztKRZYAgE8AvYqzqriXNiQEZapL1Llda__PqCxZ1YLS6AD51ocg1cCDanljJ1jhY7xfroOgKBDiFlHEaCN4rFr6chCtQcikTHVmJ76olEGpeHisS1KoYYix9D18KMYjEndbluK_GA9f4Kj1-evOY30u9aNw9-rxuqK1ZnR0zm1Y9oNbsiEU07_K4CKBcALuVepT5eKhD_xeW5Z3yWU-8FAenUzzatgts_Opbz25NON_ZgS0prwDozYhd07aWVggLvZgQWyOBiWizshAVZ3P5OxVDCtvAFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=jBH1VRsVrzo3pfrEY9b0KEKFLDYnRtleKFN3Tk8owgTtebaWz_ITQrqCztKRZYAgE8AvYqzqriXNiQEZapL1Llda__PqCxZ1YLS6AD51ocg1cCDanljJ1jhY7xfroOgKBDiFlHEaCN4rFr6chCtQcikTHVmJ76olEGpeHisS1KoYYix9D18KMYjEndbluK_GA9f4Kj1-evOY30u9aNw9-rxuqK1ZnR0zm1Y9oNbsiEU07_K4CKBcALuVepT5eKhD_xeW5Z3yWU-8FAenUzzatgts_Opbz25NON_ZgS0prwDozYhd07aWVggLvZgQWyOBiWizshAVZ3P5OxVDCtvAFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J3QGchar9F1EPL8ogUPWmtan4lhO1Iq0bczDWgV-n1a5YY5GSiPuPTgsu60cgi7U-9f6KWIJm4UGbqsEAHOShwfGzvaQa86EDcJXMOhTh3HxLyL9JHmm1aHWXlmuCXPWQ76GgWpYnShm0wGqRTcC71j5cckeYgXzkUEwr7ibcSeFDbtuczncvCzoT3TkTrZIAGCzEyhbA_dTkz8lqkdkHu7qA0kI4Zqw00qhtaGtVG2DEmorSIYHKU5zEYG811P56FBkW2I8w9ahUg8-Y5kvgbsZXieNYXdyRxbgO-sM9ukb8_gVuW0GlxU17knAjl03aeRAcAxC1Wi9SpFa3BXVVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=NrHxO4MOw3IkgkbVcBMkANeuqDcVIqqmIc3AriKZlkhtJUng9MkXNWtia7FLkoOqD58ba2tRIO-pHkkAMRcgqVAPvy9bpkVRc_oBR2l5pR56c0Nr0GVr290FBZTFPVR9jRyoA8T3jZH0tf6gaoQPW7WR7GtX09Nbia8NLBhghkpC2P95lut775l3s2AoyF_yiecBxbOEbR8t2KE181apjjWLJUmszXadhzt8878eifeFx6us-bja2r-kbI9uqeS88VnkCXpdYpOJOmXe_yVbpxsSPBDZLDehk_bEPE-XllvDcM7WBNJ_HJoN-k3MJxUIkVVzH80YsWq-yHHEd-nalw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=NrHxO4MOw3IkgkbVcBMkANeuqDcVIqqmIc3AriKZlkhtJUng9MkXNWtia7FLkoOqD58ba2tRIO-pHkkAMRcgqVAPvy9bpkVRc_oBR2l5pR56c0Nr0GVr290FBZTFPVR9jRyoA8T3jZH0tf6gaoQPW7WR7GtX09Nbia8NLBhghkpC2P95lut775l3s2AoyF_yiecBxbOEbR8t2KE181apjjWLJUmszXadhzt8878eifeFx6us-bja2r-kbI9uqeS88VnkCXpdYpOJOmXe_yVbpxsSPBDZLDehk_bEPE-XllvDcM7WBNJ_HJoN-k3MJxUIkVVzH80YsWq-yHHEd-nalw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=HgxQyUHgD3ah4A4hinAxrFDqJjfZQc6E6d-cb1yib-V9YmtC39I7vV8-gZk4BjjtnsOq_bKolkVseUpyrpSVeC8Je2KFqUY6N2XdRdjm1uT2mA2nMFr8yCmclz29qJUnW1vawJH-FTZwXgoFhwbKpBUU1KXiVNPnfJ64F0U08YOKUe3z45JTCVIZNPpEFjFo8kuq5rHs-Qe002q19f9lSBiQ5p3DszVWRs1RQwx6_0ubk7tAm2HfVEFnV8Y9hYh3m0h5tWHGCj7vrmK90Pxvt6P4eWOs0L68SgW2kZT9JjWbbgBhjMJ11w2FYN2r3KqNOIxO_8LLBIutletlCn3WkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=HgxQyUHgD3ah4A4hinAxrFDqJjfZQc6E6d-cb1yib-V9YmtC39I7vV8-gZk4BjjtnsOq_bKolkVseUpyrpSVeC8Je2KFqUY6N2XdRdjm1uT2mA2nMFr8yCmclz29qJUnW1vawJH-FTZwXgoFhwbKpBUU1KXiVNPnfJ64F0U08YOKUe3z45JTCVIZNPpEFjFo8kuq5rHs-Qe002q19f9lSBiQ5p3DszVWRs1RQwx6_0ubk7tAm2HfVEFnV8Y9hYh3m0h5tWHGCj7vrmK90Pxvt6P4eWOs0L68SgW2kZT9JjWbbgBhjMJ11w2FYN2r3KqNOIxO_8LLBIutletlCn3WkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=bv0b9kQznTut63qogGHv1nJ0q1kIqlB2Wxz5USszzrDPZiHlPr8g7nPMjDye6EOQlvYgdwCzN5kiHAx5INyMvUICCfnKw8smaATyl0TFpIPi6mHqarVXn4f-oGz7A3pZQR86-kve-eamu-k7YwsQ3Gm6Fdl1ZQ2oRrNsgvvlYAOpglZoOLn_ChMo-6-dsdvCKKoBoW3VK54j4QhC0VrZXw4_tVMJjjgCLYLs1Cr757RDUnEiTUenboc9yGFGff9P1qDg9CWkctP2eUIU4M5Lhei3Jk7mlZ3avK7L5hpFniKHn96zSDIjahAwwa1RDsBxep_poywSTRw_RR8PNsJLDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=bv0b9kQznTut63qogGHv1nJ0q1kIqlB2Wxz5USszzrDPZiHlPr8g7nPMjDye6EOQlvYgdwCzN5kiHAx5INyMvUICCfnKw8smaATyl0TFpIPi6mHqarVXn4f-oGz7A3pZQR86-kve-eamu-k7YwsQ3Gm6Fdl1ZQ2oRrNsgvvlYAOpglZoOLn_ChMo-6-dsdvCKKoBoW3VK54j4QhC0VrZXw4_tVMJjjgCLYLs1Cr757RDUnEiTUenboc9yGFGff9P1qDg9CWkctP2eUIU4M5Lhei3Jk7mlZ3avK7L5hpFniKHn96zSDIjahAwwa1RDsBxep_poywSTRw_RR8PNsJLDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ejfXSRS0vfNns-wy9a4G1tFh7DMnXU4GbYtaraCCpR8d5d6HAgfSQgMA7dxMSUvjZFox93N87EvzGok8yZr8IBGQy3zWT7wQg5So8IcbKHqfYe-5WDQPNGP6Bv741_GAMcobYqKYJCDmcBhWLLvBZPHjg2Gq0yKfIL_YhiPX4bHPK6C2CHXxZ4YvinMYWD2KwjF3K97PR4sFHDRYaManXeuXmQnRA6x5Gg-YT23i1kX2POO3R2PFXWuVEV60ch2Zqnd70QSJbfjm44jqFMKv4xfzEfsAlzPEtKwUMsAARo-oTxa3IxG5nwcWohtUoX8qcVkXc2w3z7uTyrWo0lLb4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=ejfXSRS0vfNns-wy9a4G1tFh7DMnXU4GbYtaraCCpR8d5d6HAgfSQgMA7dxMSUvjZFox93N87EvzGok8yZr8IBGQy3zWT7wQg5So8IcbKHqfYe-5WDQPNGP6Bv741_GAMcobYqKYJCDmcBhWLLvBZPHjg2Gq0yKfIL_YhiPX4bHPK6C2CHXxZ4YvinMYWD2KwjF3K97PR4sFHDRYaManXeuXmQnRA6x5Gg-YT23i1kX2POO3R2PFXWuVEV60ch2Zqnd70QSJbfjm44jqFMKv4xfzEfsAlzPEtKwUMsAARo-oTxa3IxG5nwcWohtUoX8qcVkXc2w3z7uTyrWo0lLb4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEkr9drtrZ4uTpKtSif6ZdPUJOuXmfK4kjR0jfaRhGvFYYkvFOPjMvO0FIzZnB-QOt4-cKRkHFsKFSliLsgkJ-B6ZEs6yjCc3nI5z1UR4ljHaMjGjfSZJdBrc6S5BLj7XccC3QtwYsXw2it8L6rXHsTF2yr4wQ3svlaf3Ijfg3g53lLkFJ6fnY40IosEsPGfr6ldHeczCcSAlVFSQoB4MRb_ZrD7X68b1JdcPn9fhyHAthmsprHBTKzCd3lOEGcDzvzXByuIYckdJuhBUUKr6WCNVuVB2kd6F482xkTr1WaSnhNUtSAJaEqiTvWNOZrgr3A9KmMF7Sofdj1ex5Lr-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=hMiJ2TR2G_ov52Rhu1GN91ieVcVxQXuDiTxSBvwFEcflsAHQ6W2ZTmhac4PGsD4SOePtt9hPpIzVGPsPf-rXg99G9n0TMh9FRjPkNHLvvcPkmMmBEwraywXfFpkRlLDEpN6P0WP3AWbkocByyJ-gYBUZS_qcAXNfvh0PLGLoZouF9rLq-iaV83KRaoJZ1s3QNrnphe06UqpHfl8yO6XYdWij-dy_tjkagrkVyBBeW--DGcgT-JpSxWNB-26FVnvio7G47YkYxIyeE6oDJD2N85ECi4r9TzqR-22M66dyqXxjXBAyl23n2UGPFMI1k1sJWrleCqKv5T7vWNZjDgLI3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=hMiJ2TR2G_ov52Rhu1GN91ieVcVxQXuDiTxSBvwFEcflsAHQ6W2ZTmhac4PGsD4SOePtt9hPpIzVGPsPf-rXg99G9n0TMh9FRjPkNHLvvcPkmMmBEwraywXfFpkRlLDEpN6P0WP3AWbkocByyJ-gYBUZS_qcAXNfvh0PLGLoZouF9rLq-iaV83KRaoJZ1s3QNrnphe06UqpHfl8yO6XYdWij-dy_tjkagrkVyBBeW--DGcgT-JpSxWNB-26FVnvio7G47YkYxIyeE6oDJD2N85ECi4r9TzqR-22M66dyqXxjXBAyl23n2UGPFMI1k1sJWrleCqKv5T7vWNZjDgLI3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=lUayLCX-U236mcsaTPMvu2HlXs_Dw-TVICIxL74C58y7iYLXHuwKTGtU635Rgqw-FpUjooN7b4jBC8Q_w6N1lg1iT5n7N5ejx3bY46nfJSRmjzc1ZSmW1xG1gwIECA2O9e-YzvLRvw7nsSD7OGwQVxXSVvatZqI1k4VMHJbXuoFGhWVJsiLM6Lj334A4pGB1AqhuOgF7NDN7YjebzmpeGyS_QX1RFlmD-FlML0yyjIhMb5FwwtvnWFKX1BIw4OxrYxa-NyAaFNkG5fMUDwCTPeFifjXmw7SCLXEjWaCEvEk9RbaeprZkRgbINau1PTp129U99XXusMBkm4jtB59lWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=lUayLCX-U236mcsaTPMvu2HlXs_Dw-TVICIxL74C58y7iYLXHuwKTGtU635Rgqw-FpUjooN7b4jBC8Q_w6N1lg1iT5n7N5ejx3bY46nfJSRmjzc1ZSmW1xG1gwIECA2O9e-YzvLRvw7nsSD7OGwQVxXSVvatZqI1k4VMHJbXuoFGhWVJsiLM6Lj334A4pGB1AqhuOgF7NDN7YjebzmpeGyS_QX1RFlmD-FlML0yyjIhMb5FwwtvnWFKX1BIw4OxrYxa-NyAaFNkG5fMUDwCTPeFifjXmw7SCLXEjWaCEvEk9RbaeprZkRgbINau1PTp129U99XXusMBkm4jtB59lWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dK44h2cpFuvIrNZMgEYt-KwsEqK1dryccc8ajOtvRDJsG7F8qYmnCtPbETH31gm0bX9JdD_5ZetV9ZsaS27GsvAchHj6HZw1cA3_GqXxVcl7JXXqY6jcZ0tkpX3asFujCORjmjGFknimtdMsG-ss7voIHnE_KvsAiuJPVR-yNkAsJvDanLeoQm_IJqSxIjrp4-vUFkpw06MhWE1z7hz-D_EHdYcnndQQLbwSAWu2vxPULn05FIlu06Wpe2APcBjrClGGaYO18_6BQOhw1qD8E79JPYvDiznsJNwYVsmS7fn9yTKjDr3dnksbOkNW6adj7zawzGdFOmQrVZWMcWabRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=S2W3ErmzP1gcqd2rj6hLTk9j-BkDLuy2Sq6ugnit5Zkej8er6uv0UBbfOscFfrUJXeU1E3h9UjVELBfeK-v85GxPHhssl_Fr2nPf-ucSWrSD2TtFLwwj3PdOj_ZuEsYxUzDJyLCLrncNu4i3VPscekvoVzpXqlx221gWNhOehWq1BL9x8GqPpa-fSuTH8ym3SoxT98EdrIWKHgdsGN_rKGt5zG9TeVhZtlP2am90KLqana59YO2M6KPYIlMBJ2hBD5uymPO0vQRCjia6flWca_RSDkUIQsqaYAu-3xTDh8i_QZm7ac2g86nGgNb-FoDDW4lXEA95M1SqgZE73zcXdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=S2W3ErmzP1gcqd2rj6hLTk9j-BkDLuy2Sq6ugnit5Zkej8er6uv0UBbfOscFfrUJXeU1E3h9UjVELBfeK-v85GxPHhssl_Fr2nPf-ucSWrSD2TtFLwwj3PdOj_ZuEsYxUzDJyLCLrncNu4i3VPscekvoVzpXqlx221gWNhOehWq1BL9x8GqPpa-fSuTH8ym3SoxT98EdrIWKHgdsGN_rKGt5zG9TeVhZtlP2am90KLqana59YO2M6KPYIlMBJ2hBD5uymPO0vQRCjia6flWca_RSDkUIQsqaYAu-3xTDh8i_QZm7ac2g86nGgNb-FoDDW4lXEA95M1SqgZE73zcXdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=uQAs-79pUy0bCk7tky_h-KrCfIu2u6n0tzyERaeb9gkPVcNAkMsGJYOWThDxaCegk-z_LEyoxfdITwz-CGFyq1cBINJk23PUfD11jX5IgSmWNK-G0XFb58h4IEtuGSlX6fQg9PpmBSFnaUFL_5rWS0fvJC3kyKSPYpTQCit3_ezQuZmakpmEux_r_kYMRbuUSkk6e0HDj69oDRPowVTEYz_NYgjckzbel87s-LdGhIKKLNMprCQXuRi1xANSpdV8dRZ5xB4ouEC3rRjoXgT_w7e-6RvDBo42JYUslQ_BqHmF9tDyqK7uMRE8ljL__0rRX_yVO_bgSPXPjc6RbEukhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=uQAs-79pUy0bCk7tky_h-KrCfIu2u6n0tzyERaeb9gkPVcNAkMsGJYOWThDxaCegk-z_LEyoxfdITwz-CGFyq1cBINJk23PUfD11jX5IgSmWNK-G0XFb58h4IEtuGSlX6fQg9PpmBSFnaUFL_5rWS0fvJC3kyKSPYpTQCit3_ezQuZmakpmEux_r_kYMRbuUSkk6e0HDj69oDRPowVTEYz_NYgjckzbel87s-LdGhIKKLNMprCQXuRi1xANSpdV8dRZ5xB4ouEC3rRjoXgT_w7e-6RvDBo42JYUslQ_BqHmF9tDyqK7uMRE8ljL__0rRX_yVO_bgSPXPjc6RbEukhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=UL22fRnLNGv9Qe4CcmAVrGHpuLe8onZReMQSr9r0aCifRuTDO2oFHzr_ZkM8xfg8OujL3RPM_nspeMNSFKnUxjAIszHzg-2KWrGCCKavcpHKi9zk8UeDyouOt5thNdkr9wxQAHlEhloZ2Asv3oWJl-NLKH7exx_G1EjHs44Y2K5X5LdxZwQWmCYbG-yXvqTSKyArYeSPHdfVEZnTpQarGa9m41r27XuhoUTFvNbdEj1yBbxsJhLfZ4ROCsjzFgFB3I8cok7ckTYYXd2az0x-9nvVVshcAx7rZ8lCP64ngVAf1wCfpkw8yoTBpKpfGiTKY8ylvmVYvuxZdTltOtpZnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=UL22fRnLNGv9Qe4CcmAVrGHpuLe8onZReMQSr9r0aCifRuTDO2oFHzr_ZkM8xfg8OujL3RPM_nspeMNSFKnUxjAIszHzg-2KWrGCCKavcpHKi9zk8UeDyouOt5thNdkr9wxQAHlEhloZ2Asv3oWJl-NLKH7exx_G1EjHs44Y2K5X5LdxZwQWmCYbG-yXvqTSKyArYeSPHdfVEZnTpQarGa9m41r27XuhoUTFvNbdEj1yBbxsJhLfZ4ROCsjzFgFB3I8cok7ckTYYXd2az0x-9nvVVshcAx7rZ8lCP64ngVAf1wCfpkw8yoTBpKpfGiTKY8ylvmVYvuxZdTltOtpZnzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GduQ5wuoXFOnkfjuXArHqtEGeR6WNK5s4xTHKVMf7uJMSt6FedMv3L6YJ-EH84_ydbuVOeXWqPkZ8kewIgjcyG9GOe1GpCUh70OmDwkhI-28lblzCAh86cX3FfVrbG-kGpnlFLAfNEX6M2ib4UqiSdXOQXevrD6atOVSiuLHAIQ7dnQLyWrr6Ru6D_0BILIyO1x59xY9VpR4pPMOkBxSyiYjrRp3QxP1Eyfh3fIMJhuG3B4bEojELzBToOVidhhBy2UZ0G0qO1xLvC4FXKO85bwZQ97VV54vcWwsM8WvvDvzRpXar4pllW0aGcbaKxXsAzBYc2gqoFqBPLX2IkbpIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qi0QzUDSSXF8QMfl_ePg46nfQhh2FmIDtiY2RerirDdcaBGHWu6WfERagQ9UtyMzH4u1MH6tlLmHYWZ-L_6wYwWSAOY3cL7OaAIIJCyptEiU1AZ5R_-8Q5a_TRwM_pGhkP7og9I5Vu9_59y254vah3jjdllRITdcIh9UHxwnr7LjlVEMr4O4M76VhJvSuTjVV0hoRtivUEPowdx4VHFUJPm2CaIBDuY5W0meXqv7tUlRPQiCCTnltMVGJa_gBoMdJJHd1HJFTMaq1h2eQNVV344iqD2P_BKAGdIhIImP7MyjcYMFYdmeXFpIOj9o_y05EtJc98b_uczznQzDTIgo_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BkfGyHtPSEBtaPUHBnE_gnrJkfat_rC1qA5ZTUrKOesBtm_BKH2oc64d_6hMOhN2ZBz0CWhRZMQ8aGV6jCcnQ4GsicFCsEXfmTglRgCFRd2L6-iEoYc1cSVpm1FkuJXMN2U-T5X42_GKA4ss48s-56jBxuKbW8-cPB5Rv7n2E5reDYWTc3UyNS4Slaepbq92zUlTD5MUbhInaYdJXb1tD9Em77IEyCH5Rx7z2pmkWzKITVs2Y58_Ef6G2tIlN7Gb8fKBW6qYawzVm-zboZIO5u8JN6KpsD_ggxC2HG_NifteQ5cHVnN2DcXXEz6faOgxKGb1209q5jgnBKgLn4ZZag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=uWW3XZY7PH556P4jj1yYyaq3g1p9m8Zp3P8iV5AIUwgJ-5nFSqzSh5uK0y1NUxi4BpguGe58yaFmmpZFxhZsOUm9LH-71nJUB8MyTcHDrsh4uhlLXuCz8ATphj-aBGGDev30LpaHsrJW3sc6zkPAJXKirHoQPqHHCRiA3y1-NGF3z6jGjXJQAEvg08g8uCfdFRanJFHBGtiCFdkA0RZ_qiQUl56V5Sl2JYbD65PZXf0Pha3n0mKO3RZfUVvbDE7TCuC5ElHeauloclQH9bKJpvTC9Ql243Y4o0a7gh9b5NyH3BBhoNhPyr0euK806IhLCUQByaA75o7wZqcY626row" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=uWW3XZY7PH556P4jj1yYyaq3g1p9m8Zp3P8iV5AIUwgJ-5nFSqzSh5uK0y1NUxi4BpguGe58yaFmmpZFxhZsOUm9LH-71nJUB8MyTcHDrsh4uhlLXuCz8ATphj-aBGGDev30LpaHsrJW3sc6zkPAJXKirHoQPqHHCRiA3y1-NGF3z6jGjXJQAEvg08g8uCfdFRanJFHBGtiCFdkA0RZ_qiQUl56V5Sl2JYbD65PZXf0Pha3n0mKO3RZfUVvbDE7TCuC5ElHeauloclQH9bKJpvTC9Ql243Y4o0a7gh9b5NyH3BBhoNhPyr0euK806IhLCUQByaA75o7wZqcY626row" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaqa47ES_FqGTHYQG1lEXJUWXJeSqsQdSfbENlp2_kjXGtLfyNyZ3F7RQ2iRJNPxQ4o1kTttoFv36BGkmV4w6sUufHz1OWyohi4P-GrMtrg84GrrmP8y981rYnsb43wencOrDyoGIXp1fQTbtDO2xjtHi7vk-V5Ep_fG3S8k7cAB5GYLzxFCHSJWHSjSHYN5MMRb-FhW9EaeiCxPUb75NMj4HF5Vm0c0xeIHpZc5fFOfQdQffn4akLOq9xxPRcjhPpOOt-SQDegMke0ZrmnaSJJk8FCNRb9NWVS4GTUDAN6pTIupWdFwplX8-byPHmMDHavuje65XiMMz601w52-Xtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaqa47ES_FqGTHYQG1lEXJUWXJeSqsQdSfbENlp2_kjXGtLfyNyZ3F7RQ2iRJNPxQ4o1kTttoFv36BGkmV4w6sUufHz1OWyohi4P-GrMtrg84GrrmP8y981rYnsb43wencOrDyoGIXp1fQTbtDO2xjtHi7vk-V5Ep_fG3S8k7cAB5GYLzxFCHSJWHSjSHYN5MMRb-FhW9EaeiCxPUb75NMj4HF5Vm0c0xeIHpZc5fFOfQdQffn4akLOq9xxPRcjhPpOOt-SQDegMke0ZrmnaSJJk8FCNRb9NWVS4GTUDAN6pTIupWdFwplX8-byPHmMDHavuje65XiMMz601w52-Xtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=LeyXbiiJ8TaILWT1zJ42ZGhW7lMqCctiznW2nObB8FtwYJsq7XzqNL96rookL471kYuH-zSn_kn_Zh5-zr4EwYwjbUX5N0pvK-3EnnXHMWJX1aIONqtkWzKlQhoIbnzOBb7UxMhXLdQYsZXElZCRz_XtSkVCLiiDzVYTJIKBKZVzlsRDSRfnrV5qSCKIMhRjvsLTibIe05FPSIwHZ3xTRP1gdrcOBHAHhOzN_nezDEn93wdibAixoLKpZ8AzwEQJX0ltpGnVRf_wUUs1jGTXvgeHS5qF-729WnPzxAb9L5WP5cbeq0jeoYbtTf9a-i58nseTsgyY6rS4Mmc6OnvB-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=LeyXbiiJ8TaILWT1zJ42ZGhW7lMqCctiznW2nObB8FtwYJsq7XzqNL96rookL471kYuH-zSn_kn_Zh5-zr4EwYwjbUX5N0pvK-3EnnXHMWJX1aIONqtkWzKlQhoIbnzOBb7UxMhXLdQYsZXElZCRz_XtSkVCLiiDzVYTJIKBKZVzlsRDSRfnrV5qSCKIMhRjvsLTibIe05FPSIwHZ3xTRP1gdrcOBHAHhOzN_nezDEn93wdibAixoLKpZ8AzwEQJX0ltpGnVRf_wUUs1jGTXvgeHS5qF-729WnPzxAb9L5WP5cbeq0jeoYbtTf9a-i58nseTsgyY6rS4Mmc6OnvB-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-P2WP-W5vywskwzN07mCRoLiSdD8Q2VHptWEU1ReUISryk-fCGxjb4LbG3iMpMDGamB2EJSPQcpJ8KDJltmJHHFhtAVJPgz0qmmwVom3IkBV_05jyx3oO83RvcSPedl0rWpzCTj1vimJfPwrDET7V41nXoWSNgW4xXJGMR55SZrWQ8svRArvSnQRyqmA0wKGKFd35Woj2sDKmbMKVQIIDMzFjxeTYAzkzjA8bJc79n1mkTElnXpAPmDI8DDKx3Xmr9fK80aPiUlMNxulU1urKzTleCPf_BoJ8AaUX5zDfe-cbsEkUkHlYzS5MtJqzcg2PsztitOLfI3KTaorG2pfQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHE-qusHw9yBypMqzTxpqYvjg0_X7nLcovvg7CEgKrJ8d-Y6dzGcE5j3yqSMSHkoIMMCpFWn5gMmdMSScy_ebAjvYeiRYrTAIEZSgNQQOAglvJKmUS5vVmbKm8vg87DP-iaMHx4DFGZ6DVq8SQM48zS_s3Axo854yNV6ktGaCGa5IVKzuCp04dN5zJEkZOFA-SK3nc0ze9pQ09BXYtBrPMjdOZML-c7TXffGjAo1IMiWLbgHcQ5FqVDqKazT8Nuyxlfif75H5exUNYOvWIoC1PbFwVQkzszRmygeoDAU94nzrMgXdCOYnEwUAOMHyhVSDSEmC8eI7BtN39tstq0KGLPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHE-qusHw9yBypMqzTxpqYvjg0_X7nLcovvg7CEgKrJ8d-Y6dzGcE5j3yqSMSHkoIMMCpFWn5gMmdMSScy_ebAjvYeiRYrTAIEZSgNQQOAglvJKmUS5vVmbKm8vg87DP-iaMHx4DFGZ6DVq8SQM48zS_s3Axo854yNV6ktGaCGa5IVKzuCp04dN5zJEkZOFA-SK3nc0ze9pQ09BXYtBrPMjdOZML-c7TXffGjAo1IMiWLbgHcQ5FqVDqKazT8Nuyxlfif75H5exUNYOvWIoC1PbFwVQkzszRmygeoDAU94nzrMgXdCOYnEwUAOMHyhVSDSEmC8eI7BtN39tstq0KGLPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qcTRhUwRafX-t-5DlSJzQNwftxWzDK4RxlVJFppCPamirCQb8fX0KMvXxiM0hVCbqLOVgae9onb1OQEIC9F4CdkySwn_cMU12-0U_RFE6tQdl0S6HFscP9DaNN7LPazvAQu3XozJrcymDaZbgbyuTZNhmmdnzz5W4IuGaVJxIFnz08arQ0d8skzrHHKtxV5chpCro_sqoup5b2LEqr9wvvmRayd9B30nKgTYnPjuv83sHb5oj9unIixeiA6z_40UenEJ94FIwbonKKkCgeY1tKBfkacaW79ysE9iEtpnVtnSecQtVPgUPV0Lni71NuKMbVUbuJ_DvtNOhpr3T8dMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=PpeKyNcgZBbB_V3ANzgFMyP1QWEcaqUBuLTV6Z-DGbRvnbpt-Mz7uk0mtGZvPkVkA4bniGhfZQF1i2ez0dw_1WV-fG095Er4KUfi7uUgtNoHarmH6Dyg8OzeTBDyxmD-fSKbIFhry9dqFlI9vdepKmgCHN8K4qIhoMSdjc_P1i7NCbVZeW4iY8BdGZptJsePixqSpkvrcbSlH14QOBSlz3MAXb7cmVQg_rusxD74h6eOEIQKhhUcTZoTK2xoTYqubuZkqLx0jOcP9CbOXs-fggBHDTq2DNhBOYW_LE8Zpg-8r9dltaKWrNs-wCsJMfSNuiLZWNSXg5yUztujPL2PDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=PpeKyNcgZBbB_V3ANzgFMyP1QWEcaqUBuLTV6Z-DGbRvnbpt-Mz7uk0mtGZvPkVkA4bniGhfZQF1i2ez0dw_1WV-fG095Er4KUfi7uUgtNoHarmH6Dyg8OzeTBDyxmD-fSKbIFhry9dqFlI9vdepKmgCHN8K4qIhoMSdjc_P1i7NCbVZeW4iY8BdGZptJsePixqSpkvrcbSlH14QOBSlz3MAXb7cmVQg_rusxD74h6eOEIQKhhUcTZoTK2xoTYqubuZkqLx0jOcP9CbOXs-fggBHDTq2DNhBOYW_LE8Zpg-8r9dltaKWrNs-wCsJMfSNuiLZWNSXg5yUztujPL2PDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=D79qT9-Xy6h7j32Gqk4V4_X2dvZn7VC1UBsI1a9gTvI0BHXyA1wctmHTmyef1V8gucsk8Ir7_rAoVjny4jfWmYzeoQZZ2yn5333WB4piYQtfg1197ZibZ_1azntXdbXM0pgap46gLVl59iUB4eg93j08E06dJOJcbOHVRZ2tsrGrvjo6GL2d_t24B_lX_XT94BTIjnNvdOsTVKjdvVMiMipLUK5OXxbdt_Zm_tzSpcFeY94Zk0IgfSmkIdtT4qEMFGcWTHi2RbydYaeIWuW2afxwCbbmWCC1ggCZ3GQ-4Ep1KHGLj6NLqFt_cCputp0PJ5K314fP_TcDWO1Om6tlhw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=D79qT9-Xy6h7j32Gqk4V4_X2dvZn7VC1UBsI1a9gTvI0BHXyA1wctmHTmyef1V8gucsk8Ir7_rAoVjny4jfWmYzeoQZZ2yn5333WB4piYQtfg1197ZibZ_1azntXdbXM0pgap46gLVl59iUB4eg93j08E06dJOJcbOHVRZ2tsrGrvjo6GL2d_t24B_lX_XT94BTIjnNvdOsTVKjdvVMiMipLUK5OXxbdt_Zm_tzSpcFeY94Zk0IgfSmkIdtT4qEMFGcWTHi2RbydYaeIWuW2afxwCbbmWCC1ggCZ3GQ-4Ep1KHGLj6NLqFt_cCputp0PJ5K314fP_TcDWO1Om6tlhw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=OxtUqLzASstrkWuNuxJcu3MhaTuJK9Q4XEUKRgSwBEXadiwOshaJJjUn0ZQV_-Rjkky0fZPVHORLL7pPiCFsnXBmpaPnYpOoVWxy1tjUGCng8I2DtbNTCUDqhrBG5jVmk2iC5qY7hOlfTb0C-_QWo1HIjc0Q9X1rJNjYud4ynzWs-Hln7B5mjRONt5IaBJ_r4A6ycji9d7vQPh_ikuAGfHvuqS7NCCZO_J2ow0_mLmsmQm0haV_qdb6Bgz_Y-_0T_JqtBp23YITyizvq02lgPiJHglJntM43VHvw_aqs5HfUvBAF9O6JriwvrAejIUq6tCdhD9Y7ppox4cHJz-5K9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=OxtUqLzASstrkWuNuxJcu3MhaTuJK9Q4XEUKRgSwBEXadiwOshaJJjUn0ZQV_-Rjkky0fZPVHORLL7pPiCFsnXBmpaPnYpOoVWxy1tjUGCng8I2DtbNTCUDqhrBG5jVmk2iC5qY7hOlfTb0C-_QWo1HIjc0Q9X1rJNjYud4ynzWs-Hln7B5mjRONt5IaBJ_r4A6ycji9d7vQPh_ikuAGfHvuqS7NCCZO_J2ow0_mLmsmQm0haV_qdb6Bgz_Y-_0T_JqtBp23YITyizvq02lgPiJHglJntM43VHvw_aqs5HfUvBAF9O6JriwvrAejIUq6tCdhD9Y7ppox4cHJz-5K9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGLeLUNw0_W5tzOt7q6jpF3WkQYMz-VTseWmSpBgrfHODksRWNM6n87kVw0gRtYhVnpmVR8MBSDlnVOYIBhtGQrzZfBXX4NYfXVkR88p5uQDTJVeDK3fU0n77456j4rJ1XvQ4BFckA3qLu0ro6wDAt4p3g6BfFgQZYlev30nh4haou6iYr-r8jjK5g6dKwUSBAZfaG7rXeiYzGYckoSGcdaMCcq7KJGXcSuXiSmUtkwYHp931HdGchhpy-WayQvSFRykX3QJgNz-5suI-yBaoKOTx_Cyq8q-kBpYWpLPlBOJuUVFfMt5IV8jAbQzTQmbVRyEMpG9MSE4LbKZJkIlBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIyxdSZD_7MDL7mJPoL1BAg-zh29N3BLRGqxdmCIX-QlXlwngUUaNLn01tsE9PgiGLjr9CHVw664z3n84R3KDtO8vnO1FPDJ-WItPU9METr6tJwk7n3ddewlQmudqfFSjA5F0YsBOObAs54rPmycRtcStDvY5Kn8-xVn8Z7zLojuqd0O3PGxkbemGE-nsOsHFcWj4Xb2cqRV5GSSk4MGOtjY5sj4bxtZlC1bCexH2EPBzk5ODCU8czqaXW0QRtAQsEqr0Qi45WoP39Hoy93DoFSplrNjySRI9QJlSDqPqi27s7atx4wkp4saRkHfx1mo9yR3s-OsQVTepWtcAOoycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=F1tDPeNFRnc4SI5vPi_bPzu0XDej9_cRZoo32VOdS80Lbtq-mtnQArxteQnboqL5fYLfa7yRCU4KquK8e-0jVsK-H3ga_2vqK8K3jUj34rpQH0TZG33vzWW8YCLzEYW5wg_aM7w5HBOC-_aIhKHkFgpd_YSQ2ZVwEA-1E8ChG9ibAXHNCFGSbbS7A4qNiphB7s1sY7ZaDx7AxmvsWkiWu0Y4NvfIcaE05z80JfRCpW1bHDUugunMyYjRE2Ed_A7LUcDn8VlAeU9r02iRmVqz2_EsuvLBYZHLbHNLhqr-KMO5K5iwT3Pcpixk1RsxSjt-d6WNO_ah2EsruOthQS9NUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=F1tDPeNFRnc4SI5vPi_bPzu0XDej9_cRZoo32VOdS80Lbtq-mtnQArxteQnboqL5fYLfa7yRCU4KquK8e-0jVsK-H3ga_2vqK8K3jUj34rpQH0TZG33vzWW8YCLzEYW5wg_aM7w5HBOC-_aIhKHkFgpd_YSQ2ZVwEA-1E8ChG9ibAXHNCFGSbbS7A4qNiphB7s1sY7ZaDx7AxmvsWkiWu0Y4NvfIcaE05z80JfRCpW1bHDUugunMyYjRE2Ed_A7LUcDn8VlAeU9r02iRmVqz2_EsuvLBYZHLbHNLhqr-KMO5K5iwT3Pcpixk1RsxSjt-d6WNO_ah2EsruOthQS9NUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_T0lIrH9qRN9sqt4sSmIjWTNLEVntJOFSG5hFVuaPJAeb16J5h1wPNY-OAI6cupJELX5js-BMv1LjSfSY8ScSlVJS0l19_KV--hufjnoSvnCPXdGCPtFSVFlSenfMIaz3TP0LYDBTHQZMpPTX4PCH2ErY5bQNGsYysLktkGF8N1zwIMMSWs0aD_SdC9TSzOSCjcH1-yD6iRONkWCIcQo-40w9kCy1OJZKQE3eA0QJtz1X7t-UuhHfUaBV8kVLR70nOvVYRiVSSdVVWwuHYkdwU2Bpvfm2jrDpUcgtlz59OzzFjd_VAScley9dH48UiMn7xIveDQ-7P97D7LTI28IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g3ga4KL6tktfsF_LkyYIspZ8VvahmV-yi24wz3DG7yoUHzfKUn_zYx8DGdByFZiRmSBIsIV3lXWNLIK-iJOcGSG6MD_lt0j7Gfx1sMpGm_at7DMW8YLr2FyVXc0yBJX6xVo83scUne-qSwzm24mVfAzh5UH5ldwEiwD8E7Unj_iPZOgMCXSmx2YufitGjDZkjcWN579mlzDZQ7X0Ryj5rFTmsXOGcn_5B6u69wgmEWP-QQsaQLM8O3yshlmquXgfANqV2LGmtdWcKPvRJnRwtcoCk1OCmcc_m42f8lC8BLK9AsruRnkprSmazx378L5dYgkilosuLtGmHOBNdIbkqg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WHFWiULjn0IpGOhXi49H_wv98x0qBjVtvuKZ0F-TCYNZWblFBI1Cg5BZM30eu0D0Cjn9wFuZi0dUOmUaCxhVg8lp2vxk1WX6_sgnl9sIRlzEt_79ic4GyKuU4f52-7IOeIre3OnCUumo3gY0pSRzDYU8MswAqc1C5-bh3k-eFE5uLlCn7-S6CrMvoJ5JdPnbVRk_2Ml5XiaHJIChWBz3NeC_vN8rrzRfPbFVZ1lLuspomVPZE1jIT__T4lU-21HnqabY128q6NlNIMxYVsUB46ViBwm_ykQbYtbfpFsmkX9BXxWw9HgdI_DZ75IiV81NMPYTjjjVRQodr7XuscsU1Tp1IoONmT18AcQUtJcox0cRv9EjK0b-68XAlBFzCvr6ebrsiXIxXvxWcGspBDlhM9q_wRSfiqD2r3rR-2PhWZo_6qHHO2htH1ois9iScKzC_jXP84q-I5_QjPJZwyQZZEPGj5OOG1Dzj0qWt04lVjZd8uAgrrMwogBhd5W85__ygzpHeI4zGjrJShPBJc1ber5ajj2dZbjYZaoP480rZlrJpQurTv0BKgxfj387eZh9UcYezfDqIxHtH_3bxu_vDCf5QOr4HD1XeLSR5Jib1lZkfKHURVGYdlsfmqVMdloUBOZ83p6REHVfD3L0keGF1OCAucUzmqDq3dinABkDXcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WHFWiULjn0IpGOhXi49H_wv98x0qBjVtvuKZ0F-TCYNZWblFBI1Cg5BZM30eu0D0Cjn9wFuZi0dUOmUaCxhVg8lp2vxk1WX6_sgnl9sIRlzEt_79ic4GyKuU4f52-7IOeIre3OnCUumo3gY0pSRzDYU8MswAqc1C5-bh3k-eFE5uLlCn7-S6CrMvoJ5JdPnbVRk_2Ml5XiaHJIChWBz3NeC_vN8rrzRfPbFVZ1lLuspomVPZE1jIT__T4lU-21HnqabY128q6NlNIMxYVsUB46ViBwm_ykQbYtbfpFsmkX9BXxWw9HgdI_DZ75IiV81NMPYTjjjVRQodr7XuscsU1Tp1IoONmT18AcQUtJcox0cRv9EjK0b-68XAlBFzCvr6ebrsiXIxXvxWcGspBDlhM9q_wRSfiqD2r3rR-2PhWZo_6qHHO2htH1ois9iScKzC_jXP84q-I5_QjPJZwyQZZEPGj5OOG1Dzj0qWt04lVjZd8uAgrrMwogBhd5W85__ygzpHeI4zGjrJShPBJc1ber5ajj2dZbjYZaoP480rZlrJpQurTv0BKgxfj387eZh9UcYezfDqIxHtH_3bxu_vDCf5QOr4HD1XeLSR5Jib1lZkfKHURVGYdlsfmqVMdloUBOZ83p6REHVfD3L0keGF1OCAucUzmqDq3dinABkDXcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETiJDygEz29qkeIJv_JJkikwtnt6DmnrJjk542p7vH5YMUkwHZEMvASc6SUTuKn1FqXVvHSasWHZ7Z5RYXT_cyXrAVK14e1fAZPJQf6wwUcfhfoepVWqfstQaV8KJs8PVHyDoxCcL6fUX0x-Y3vo4aj-J9hUYIIWe8iBfbfiIp8SHuvaZbWhyGjQD338oc-AZoF0dgUnbPsuvoXlmNEftsEzzvAG4y3BL9mGyg-U6z97Wi3Eh2csy5hvUw10l0b1ylq5dQZhppCN8hHrZCl5VtCzRIEEuusO9msU5BkV5rHF5y1OvkWE5sLqz5Op_MJE0Sn7vRgwUJCWMxTgwDhluKnc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETiJDygEz29qkeIJv_JJkikwtnt6DmnrJjk542p7vH5YMUkwHZEMvASc6SUTuKn1FqXVvHSasWHZ7Z5RYXT_cyXrAVK14e1fAZPJQf6wwUcfhfoepVWqfstQaV8KJs8PVHyDoxCcL6fUX0x-Y3vo4aj-J9hUYIIWe8iBfbfiIp8SHuvaZbWhyGjQD338oc-AZoF0dgUnbPsuvoXlmNEftsEzzvAG4y3BL9mGyg-U6z97Wi3Eh2csy5hvUw10l0b1ylq5dQZhppCN8hHrZCl5VtCzRIEEuusO9msU5BkV5rHF5y1OvkWE5sLqz5Op_MJE0Sn7vRgwUJCWMxTgwDhluKnc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=GD3L5CWIOLxBPJO3Thlyny8Kxfccw0JMVaT30ZjFuzUvR6ib0e1RGHsjD85L5-j09vKURtMGY3mrNL7hJFyXG21nXi_70LVwf44B-b1H6Vg8zqgoR72drNiA-oFLk6DFVe-mWK8ZTrOz6se5Em_vUx5ne42SSLKlIjf3r2PSgamJe0TKzU_7-4bLU9CeVkaDFNzhKaalW0-VRBSS7YPrTYmeg7oOwnbGpAnedSwKPXodZctEF3LWIYRWRnW5JS-ozTXrTkURiC7LDKSbDyKKNi4jiK1OzzoOlFP4RqPrqQVuqNPZBWenpNqAHGqrLx9z-Y7qeBoLS1d9uoxTWz29M4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=GD3L5CWIOLxBPJO3Thlyny8Kxfccw0JMVaT30ZjFuzUvR6ib0e1RGHsjD85L5-j09vKURtMGY3mrNL7hJFyXG21nXi_70LVwf44B-b1H6Vg8zqgoR72drNiA-oFLk6DFVe-mWK8ZTrOz6se5Em_vUx5ne42SSLKlIjf3r2PSgamJe0TKzU_7-4bLU9CeVkaDFNzhKaalW0-VRBSS7YPrTYmeg7oOwnbGpAnedSwKPXodZctEF3LWIYRWRnW5JS-ozTXrTkURiC7LDKSbDyKKNi4jiK1OzzoOlFP4RqPrqQVuqNPZBWenpNqAHGqrLx9z-Y7qeBoLS1d9uoxTWz29M4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=NKpqluDoec9G4r-pXqj7yisnwfATw88HK_15_hYQC2v1enpb0kqZ9dUzPftgQCqrBAlZPECJWSuM4jF0FUlhLNX3iDKk6ct0qm4Us6fjt5gkI6Uiz25bVzxh1sdThYUpOtCyyYKttSbzGaRAURndmeB_jZ_vJGeyTstAA0xAnXbZnTvaIS3jMOfy5-cQZQusRCK6HPLpM5bW4datIztdsX66WAXTVxad_wM0bEFD3uaZEmu9eSZiSF78RN8exBmmr4xvHDb21SpHFIBno_DmqV6PyF6lLjeGbTVMPo0oCn-M6eQyzVbY6OrS_c_cqpF2CoVRpEHSumikVhqgoII5gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=NKpqluDoec9G4r-pXqj7yisnwfATw88HK_15_hYQC2v1enpb0kqZ9dUzPftgQCqrBAlZPECJWSuM4jF0FUlhLNX3iDKk6ct0qm4Us6fjt5gkI6Uiz25bVzxh1sdThYUpOtCyyYKttSbzGaRAURndmeB_jZ_vJGeyTstAA0xAnXbZnTvaIS3jMOfy5-cQZQusRCK6HPLpM5bW4datIztdsX66WAXTVxad_wM0bEFD3uaZEmu9eSZiSF78RN8exBmmr4xvHDb21SpHFIBno_DmqV6PyF6lLjeGbTVMPo0oCn-M6eQyzVbY6OrS_c_cqpF2CoVRpEHSumikVhqgoII5gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pC-oYz2vCscK65Do2PRI-fpZFluojNXWZAbEVRqam54QypcLh5QXnJe_PMv9XzUg0KNxv4mWzBytCNyUgfVVi1EUkiCr5wzZqNIxJr3CZqD9f_v3DDFgdmZJPA-o79CQLp0rGIHucpQPoufHoWM1uTIx9qVQJ3R_QMXHq_QsnUzgS-W8msv8URJ4tPLYI_6xWtzngrLdjP5K5EbMAPc62npqaZxfvRh6Y1T3lvjWT3Q_MEh0VcKpUbjMQvVnpbxXHLroMOsJsWLOzuc1JKUkPe8vY_aeEgdY6nEuGeOOG0asdLnYppMScmY5xxp0QIBmLeOkkus_s6AfxhyuriJMnA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uwc9B4Wc4MHFvVwREF6JReiPssAmSrc_4dsbSSzNCTID1910S963SFGLUZEsgfANJg_sjujHaOVyXtugBg_P35cL_EzQzlyzZEDGZumoh4wn2zGy0coeSqiIHnTGsI_Ht_nMf9z8mA2gHq4VScySGMgdF9jtxlS03CgK3N3-6NJMo6Q2GtPjes11pyIGQaWwXv6wy6TQwjaxUjF26me6cWyehm7NOsb-Kkjdhi86kYvEyVGP3tJQYHvJx94kKV4zAY9idQskb3hfsYEPlnmW2u-leQdiPzSdCXOccyGdIqjRE-mxI0Bgm-fjiy9a3PsvGTmT_XcopU2XHf9Z8iCwgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ed5CptZyZmr_7qh-aP9lQvuE945manrpNpBPgB5dHQbmfGZh-BARl2TYQ9rr8BDBArO0maBuvlkF93BkcyZ6TpOO3jiJ2tUaLh09xCFrJ0JIdxtwjrMF-Yje-JB6Szt8jXWBJQRojyM319UWYEmhY5AQqaAXy9bdAQqugZMoCGofALbW2QQLqqzoLsRYWL_-JkeaJJ_MiDSDP9FvL8pd3YvZ-1bkRXcvY7JealFxKyN6RzFilfR1-cm51PVyDdQDZ9ThA_sbL8iLmKhe86frlWLGV15wiaxcG2p0di5Nq17oOZuBD60TpyRZtpJ9pNc8wc15dZSY1hfwiFDDwLCaTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqaPcBi9uHkMlcrhcvQTZIqDN3npSI0uTFrBS4LUvf5SNKN9keQ4Ey8IjYn2byARSKwaweRaxrLXFzQtQkZ7DWWmKCG10GsmM86f70oIrDrOr8MpYp2vwhAtC_p1MYSG5D8u88GP1FId_8VdRkG4izPs3Hgf5GaGAhjhvIQM9hKdPlIvFQTnR-HXZoELhnMzVmkgMtQKuIgAtey8ElOMGo5zqDSLi_AB-Vw1U-d0X3cCLW-JMgW02ymtmuBYSpGB8hAr-NtWKsieCD-KUVP38cVOJAgKuy1mpjAbwGHeJeRUyCkgTuJEqdTaX8z872kpcXJC7NgfnwIu3Xy81ytrhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NsY2X2SZTpfVKKtyl0D7qL_Nx5MorqoWDIc-jxSYIYbFd3oqbjkaqa2gLNFyZFHYn04o158HEf_dgfW3K2lXrqwnnuhcog8Ri9YKskNhPtS-yrvxCge4inH3CBQo8oFaZc-ODKJTASCtKUBJxacwy4NdjkOv65GCrDSfa8bFyRSa31oq2UUfGSRy8spCk21d451vk9gxB2vgA4V9SPHS4bMw-tvb_-FFg6-UuAq-h73XSw9Ur5hwxM7XguJObMYoeqUAeOKIugsHedF1-_mXrXDJU2EC3DkxpqJXuAaC-k-tIo_hULSgE_LUIJ5QzZt-u96DGnAwgrB0GCZrYbQgTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=OQTmZyjZUs3sPhZsCumpHwZBtWkDRVkIPPSG78_lFyzOSUwBSH7UYCnqSWwCNDaM1PkvDDE3Bz4YF0F8ixgFZLbeL7eV0M_3gRMCWHKTF4-Z--S89P3uHhuax9Yy6ocg5aExFMgIcIkCT7jK6ky8I4vrfGwW8g-qJpMOQ7s2CqKmmSFKXtbfPqZvabqIYz02X6p-3G0wwwaRL8azb7q0Jxg2U1JNG_ImDvufANsuqa83eHO3-qMUjcu8Ah27K7GOv6Ma4oJYCez-Lany62bDcy_KXEd_KosCbOffcC-2nwj3j6ZEZeXim5XVNfLb_A-0rfhFMxqRJHoMw6U_f_EtCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=OQTmZyjZUs3sPhZsCumpHwZBtWkDRVkIPPSG78_lFyzOSUwBSH7UYCnqSWwCNDaM1PkvDDE3Bz4YF0F8ixgFZLbeL7eV0M_3gRMCWHKTF4-Z--S89P3uHhuax9Yy6ocg5aExFMgIcIkCT7jK6ky8I4vrfGwW8g-qJpMOQ7s2CqKmmSFKXtbfPqZvabqIYz02X6p-3G0wwwaRL8azb7q0Jxg2U1JNG_ImDvufANsuqa83eHO3-qMUjcu8Ah27K7GOv6Ma4oJYCez-Lany62bDcy_KXEd_KosCbOffcC-2nwj3j6ZEZeXim5XVNfLb_A-0rfhFMxqRJHoMw6U_f_EtCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=Nml24zESo55SE35uzTRrKpZ-GPffLRN2tRLeJ9vgeRzaubgky6aiMueUFSI7-LBTN3sI3JV8aWu5oudP6N_1oznhf33Y5uptFpn5Bxj_TWjfE97L_tV_IkabNgIEhz36sXWVb5MACi9JCkaJr1tRWavvRExhgSBV_vpL8PvO94qbvsyNCahsM3A5r6g5xuh2ylqU2Tp1ojjmmkNgRK0sg7hKwd0hCHuuZFkgjJa06PotOp_l0P1asELq8kypzrIjhyXpqHJzV1wAVODVCxBhP1ydXaGDyA0Sf7lk-YIbbRUDj9zf59admlK8gJYAT6olrH9X505xLtk79CycFqcw2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=Nml24zESo55SE35uzTRrKpZ-GPffLRN2tRLeJ9vgeRzaubgky6aiMueUFSI7-LBTN3sI3JV8aWu5oudP6N_1oznhf33Y5uptFpn5Bxj_TWjfE97L_tV_IkabNgIEhz36sXWVb5MACi9JCkaJr1tRWavvRExhgSBV_vpL8PvO94qbvsyNCahsM3A5r6g5xuh2ylqU2Tp1ojjmmkNgRK0sg7hKwd0hCHuuZFkgjJa06PotOp_l0P1asELq8kypzrIjhyXpqHJzV1wAVODVCxBhP1ydXaGDyA0Sf7lk-YIbbRUDj9zf59admlK8gJYAT6olrH9X505xLtk79CycFqcw2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vWA6IqLxlXEG25rGhr52KQmiBPK-32iTgFiZpDuFkWp0nsK2Hz2bKlLqowJN4z4z8wVtjQ57DuDeYXk2xZKrsmFDMGSU_8sgG2ZqrOOpUTwXyBcZXRBkjWbycpo3o3yEqOdf3F8KpaxkzkDKkib-7hTyfUs3TxTLouSi_4qwwh7fDiiPcXccWEbx9CHonHD6Kdm-IzwusPtoCP3-iaSFupVksl4eyEvhedup3EcDYyTfwjuV9Cp01kvWf74ys6CISigqWVyq6nMQBpaXUmAhMhrs1RQ2S03HLHImNiHHHQVxMRDx9sHA6bqAigGEQ9725pJo5refyM0E4S3HuYSXLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qX1qsWJvphkxZJN5Yw6PhYvSxf2J9C2llJsl8y3zMKGYJFySGDrEuNNmqGtlCx_xir82jhyGLv1q6IMWao-h1M73gZyyUvMdKUfq-NXodRFLzSqxDtYutT82KwWh0GShHSggPg_hvOlWkFoSso4AXZrTs-PtIWMPRMEmaFvcrn0d8ki1_dTxR7105s79GVlrKfOZ32vO3eEOywuq9PwExSoTH6eXEx3ml5PKavGuEjD6n3CTAiEhNkDE_HeIl98ot7Z1YULEX5vRtVDtZH-hBXC8fuMrTPKjJDxUNEfTU0YFylOF9Hgs3r8b5hqRBrBcPM-DlMJybLbGxGU4IWw-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=tcKyh749Ru5hwp7rPvQLv-UyVFley8z97aFRoxDD3bDzDg_yABq2Gg5OPzoc4-LEpFahyNCQXRWhob8JDjSgv5R2QcUl9e6V7l6ONXjZa67IZ-_DaQao1pdgZEtCVjfTg_VSoN3BQpf0YKwCB9kGevR03jalHU3VbJ-9SpQBjFd0rmZ9aZG1trUFqlPlKwwKe6CdBc2qMe2K3NwKnsogQmLD_DGqzLSE0wriw7M6HZ-DPEXvdo6Ij9VCQaJioL-vHcsDPNINko_eIqZ3HzxfD-TBV4wRY8DCZPh2yJHZZSn0M4N4mXgjAHHqErs3lG9rJtWagyv9ARx54T0fkZYUBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=tcKyh749Ru5hwp7rPvQLv-UyVFley8z97aFRoxDD3bDzDg_yABq2Gg5OPzoc4-LEpFahyNCQXRWhob8JDjSgv5R2QcUl9e6V7l6ONXjZa67IZ-_DaQao1pdgZEtCVjfTg_VSoN3BQpf0YKwCB9kGevR03jalHU3VbJ-9SpQBjFd0rmZ9aZG1trUFqlPlKwwKe6CdBc2qMe2K3NwKnsogQmLD_DGqzLSE0wriw7M6HZ-DPEXvdo6Ij9VCQaJioL-vHcsDPNINko_eIqZ3HzxfD-TBV4wRY8DCZPh2yJHZZSn0M4N4mXgjAHHqErs3lG9rJtWagyv9ARx54T0fkZYUBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=AfdacTsC290edzRAwSZwVIYMl-oIvLyGV-mE5ZBIH8sTNCEiBVXLHTXF8W9-Fop5bjG63fXSvCI0IuemUtO_nkO3Mjd5GzBUVJdjrRTUgAf0rfX8RvnPEpk2sjmlqmt2tIusP5R1X7BmBeNSbaVBNSJz7EgWm0O_0aVlB7YE9HRPs08PzwHM1lpxJBL0gB3dAQmV39R55rWIipDDcllvCE2tYnaX2EWy2wi7aCZZMrxufutr9FLjYHpMks1st-lySUY1NRKEs20DLhw0fvlJgVXgtRx2Y8ZS0WohdQfDiU55KKy4HmaX_dz54ziAP-6ehUT3G54Qc-GFY1lT0k5ZHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=AfdacTsC290edzRAwSZwVIYMl-oIvLyGV-mE5ZBIH8sTNCEiBVXLHTXF8W9-Fop5bjG63fXSvCI0IuemUtO_nkO3Mjd5GzBUVJdjrRTUgAf0rfX8RvnPEpk2sjmlqmt2tIusP5R1X7BmBeNSbaVBNSJz7EgWm0O_0aVlB7YE9HRPs08PzwHM1lpxJBL0gB3dAQmV39R55rWIipDDcllvCE2tYnaX2EWy2wi7aCZZMrxufutr9FLjYHpMks1st-lySUY1NRKEs20DLhw0fvlJgVXgtRx2Y8ZS0WohdQfDiU55KKy4HmaX_dz54ziAP-6ehUT3G54Qc-GFY1lT0k5ZHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiNiHm51fdyrxsirfubTs6ubeS5_5BKrm3JNI2asSPmzLAA4lq5XH4XS_TUiC8j6d9ZrnjkPvSd6--qH9ZtNGxlg_g5AFrrXSGJizd6O6fsAr5t54NDoCyI0J3yJdjavqTVqD5_FS-DPOQVj5ph1TKTtZNeLGmJH9_0jYzc52mRxysGfycQerXCCud4vxwD7VxmVG4oi_GahekKW0z-aFuw94xsefPdrpO4XUZR2su-RyXgY9kV3S2Da5Ij71MQsQdBtFF6m0LVBFXvO37PALPvQWHETRSYunQaE-Uq0Dy41NNoA9e5PHRaz4TZpodH2beNklPoOBtfXEaVk2R4E2Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/alx-9KracBjVpfJIrWbJb2wl0fXrbbDimE12tyC8KPsYh9n9OEdo6wkeWNaD4t9x3Eh5SSTBjzmmX3GDNDzhwfukuFHLAQnlJvkFKiZaVMc8so4G2oGwd4fSc6PFjfTGd5ATGJ21bU8NB147PB4YFEBeNiI4TfXlPmfJJ88oTizZAWImofFfNkD7JVrsVOAVNnSPaOmqJEC_f7CxSFQ9oiJ-_7OcDpHYhH_yYgOZ3PNAKrYTaQjNVFv0GlnFa8t8L7IUi3qjqvWJxf6gpt2s_GJb2haHTbiqK3YkvKT92Ko2icWrSDAxOpLvauLMxhXiGWaOSNk2VCv5gViTscNW1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t0bJJJ_MDB4YN62O-5UJxf3ebCPO_78j3V9Mr_6tQ7xBJJcjNbTakhlS2fZa71nwBwZMILlGVY2B0-ktSjTG9VlWFzZMjN3Lrk-QMMeZ305KhjqKKwqHCCASmbQ3jlf7WsuO2JhGS-ku8qYFeX3apxquLHlCtu639ysxSTy6LPe5wnq8UpYIzJa__6fMJtdvkOiYO_49-TN1E_DvG9JO_DtqIx6IEaJw_we3VSAlluxCD-oiLDpPsMcnnTIZiUtllwq64n0spQaM0i4esfg8iDM8Zcbyve0e0lMWrSPWnH4adFhUu1lQRUl2PR6fP35aSiu1_GhYkojGnAphtj743Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=LrTSK6tBeN2c59wevEwzLPWt5CnZ8GGSUR2DJ9t4yNsQKMouiIUG9tdaXggyOBfO-8BHX08_8NhOJh7yGF9re3KbVaujQUw6Wuca_Y4bCS_8DNkH2sXJD2GUVPbDIfPGsgpwmgBEOF6EuHm9EmC04KrJLs9nY9CKRIJrn0Rp-r9V6IygGAYw_jXmurho7r59U0zsakHQ0FSsdLunWOXWY-hH-Hg7h3yCvhLTxxnbBL3SPYHoiitQt9FKf7hx75b1GXby6xcnTzPLKK2YYyGUQptO9RwPzXWL3TpnBU4glKFC_PElxfmODExW33xEw9U9rw6BNNGcNCTmREDPZnFq9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=LrTSK6tBeN2c59wevEwzLPWt5CnZ8GGSUR2DJ9t4yNsQKMouiIUG9tdaXggyOBfO-8BHX08_8NhOJh7yGF9re3KbVaujQUw6Wuca_Y4bCS_8DNkH2sXJD2GUVPbDIfPGsgpwmgBEOF6EuHm9EmC04KrJLs9nY9CKRIJrn0Rp-r9V6IygGAYw_jXmurho7r59U0zsakHQ0FSsdLunWOXWY-hH-Hg7h3yCvhLTxxnbBL3SPYHoiitQt9FKf7hx75b1GXby6xcnTzPLKK2YYyGUQptO9RwPzXWL3TpnBU4glKFC_PElxfmODExW33xEw9U9rw6BNNGcNCTmREDPZnFq9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzCLHlzu52WYnNljoLkQHAa6GvWD-vK28hXTzAHP76rWbZlx9XLosbIAhGFY7D6o8T6TBmotff3n1Ywtvm4W5iPAw42WKzA_bhbPzD_nX1vqnyidtY_Hy_qxT-BU1B7UHKDbsQUiIdWr5ImYJrEHiCitdE-T5u5nRquz9iCWf1PmWUZ5-w2ydVUDeZL9_kfmK4Eb9btego4GtxLDI2-hp26wZaENsle9Y-YgQeSSK59SDGgC_ZV8tzWpd0rdfDAf3QuUIdfhdfSSnr9NerUwWr2xv8dLKQpLVAnwAENnqyMrBZ_wjJSYmeW4-Ztxu2cauaSUvgtOuu2yBgeODftKkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qB9YLUcvlDfrLaEeuskedU36By47N1qq9f8o0hawafiaKEYOJ75O5k8ZwCSe9tNSHG4ZxwTtHRQpN6idkdjeBsxDf7bi_K1A6yLoGElMcgeT6lVwJp4CNkl0KChgrjaniphiwyvDAs77XdpMBI8W-0P1TpCSQ5c6IIJCejksUnrKreRt009rWIUwEfNO2htoMvAhScVxz8PRgSo6liNIxdzR5iLFbLtrvR91H9wrgJHvsDY4nsBMyC8t2aeNMj-E3pBk4A8FNRv3KqDBZvPpIZKIb6ivwZkKnDP6ZEB2shzZ2XIIheDMN_m9Grc73cI_a5ZqCH_ffxzgweaweeCJpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAIEOqe6-P73MDWGVPYP7SloN1e1_RAky34nBdQX5FsC4bnRF6eOGUjl5tQuXbXfcp9G4938mQOVAHdl0icUrDtfV6gfsTE0V3j2tZHmxkzimXk07cO542szMrJT2p3FIWGzoPAwo8jAwtdSnRLS7PXhY176pj6tMIOuZ09ja3XafFExyStqtTsZiJXHJ9G4z4urtCKmQx_0TPae8eTwx_gv8YXtwqB_LQdIW3jXK6R933sThsbSDqb0_K0mchMsBhEWvn3WIIIB41VLLOTKRbOXRGyv2RbVgiaDgB_3skFQrnKNb1WVd_upuUCmYYgfz7lr6mWxzrFlnYfgqHVD_w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESt0uLw_IJPJbEyD9LEHBu-YCAwsVlLeGgxgVpNW-I4dr_qH6xPW_Iv4QHe3EOHRpghd23PtuFrFXPiAQbBfhnjUkZ1Euy1WBse6dOcVwFK7o7hFaClkSymndcsFSaPWtbF7pDIOXdGbEodR_rvI63iNTQnHt1bVrvVKsHKstq-EVBYnqSDcCe9Q44WL3dm9HV78p9OOuKAkR971BV7DTXYLu3D9CZ9osOAyoNEnC_6U9yFEXzOLfyFB2zKTGk_CKaSWzfd2gsLjtcLR6D6Ps5EpYlXk0aAFabxa1u1p6iiYvTpcxdeCjMxoYWKCR8BSK1hHwdboBaxsVYuuHj40Zw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=JlOMITQpKkFXVJE7uaeLRSoRFN_AGiqIptLaEnlqUdkrVQjth2UQeiOEAXKz4GQFbnkgZ_-Dh95yBq6Ciutv46Z5v-4GdiHqfqqfGhVzItKD3xpvVPIEh16ie9oByNUdQicTyaoXBHTRqhEYMSep4rnCIkiIDtu8wzWcUWLNUCpBODeTfClq-0sFTK5EiuMRKDUBZUIxrvZhIhPMNvdfCVDlkcxMoimxZ9J23xFkNrx4MBVTXHisaSu-G4Y_PKvVbRrDNBXrqmlyfl1YjQYpLnkbNdqQFp-zQzkC15cShh1bYWPQFiGWMSgjQyKT_vwshQCUKRNAfY0y0yrRq9wG3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=JlOMITQpKkFXVJE7uaeLRSoRFN_AGiqIptLaEnlqUdkrVQjth2UQeiOEAXKz4GQFbnkgZ_-Dh95yBq6Ciutv46Z5v-4GdiHqfqqfGhVzItKD3xpvVPIEh16ie9oByNUdQicTyaoXBHTRqhEYMSep4rnCIkiIDtu8wzWcUWLNUCpBODeTfClq-0sFTK5EiuMRKDUBZUIxrvZhIhPMNvdfCVDlkcxMoimxZ9J23xFkNrx4MBVTXHisaSu-G4Y_PKvVbRrDNBXrqmlyfl1YjQYpLnkbNdqQFp-zQzkC15cShh1bYWPQFiGWMSgjQyKT_vwshQCUKRNAfY0y0yrRq9wG3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtbX4UkHs91WK8vdLqSODemYkaTLRGir7nxEnGEFfnhUjQcjeUKWNocTxFZdGfriO5eZD_NlmHhA1RAOpnSG76_Ai8YOzr7sY_MOte-XhUltugJRU24xTndZmvjV1MqB8XJqOOmvg6m-ZU7djSumF44nEGpbSSG4fhRKK1mrPSMqbsMNepxUj57e6qOirGusOAnSq2BI3imy7yk0IcMRnyuUaQBFR2PlqlKt0RJ-msEsERyhUl0brPE35PolivMFYTlMiwOf7_MWM16cvkOENk76Yfrk7bqRTEe8tq9zVZQ2DErwsLJY8UGfXzsGUkt16YuxS20UTrggJc_WC5DD5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETJ1VzxoI9cdj9hhCk9g0zqrrg4kzQlcNCgbgf4u61czMV2AXECvWxozqsML7iP_V0WVNmRq-LddyLqgSYCaSuo5HqUF0ZlLATbxMczOMsyeyAn62GlLwsh8v8VN_gowJPbH8O5DD_vOKvZnDtE91DXAUMryrgZIblpvJkL8TcL07ZG4HMC8sIwpNX9Ckhcp_1E9hRclXiynhUsi1JIU4aqYi_T9nyhr-65c4aQlED2gsh0eyylO0MO_XuMMa5VqOUB4u7b8JznflyhkOqrGFgLdLjqJHFm_PU-BnYzkwn3c36BoKV74MlH0ZiK4GC4UAT9VKhkXL6Z9Mi9bozBFHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqUT2_PYp0O7tIyfwAn37YstjKewfs7DYEt0bsI5FCJP_nk6d6xs39wQj4B3ngwWre3p8ese3Uen0RX2BJl68w8KJslNCVGjtc3ayMpxeyNJSzP04B_5kl4G3Tf6HKAwB-gOy5u4eHUphaTUwY6YZtbQz-yMJqGTbjq-sCCGoE6cjHVLpPQV7c-zQyC4EVbOemzVQtmQlS2pOIl0Boo13BqoAJmmRQ7f8dTw8UiSBvlXXYSIc7olHbhwRW3hFWIKiuya64fdz10Jyjlcqu25M7foyFNp2yYfk68CIKfCaP7sO5IGOlKqQ3_h2a7RSe2pp1tQojLFLhctKbCCC_ZgTg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=JWRmSGf8kUWIL8aXoxi2YIwdUHLQ0Gappt0r6tvXio_4cWu14aIfT4TkciHmrpFq40-sVlE8ZSRftleRSRvJg6TjOzm3XFKJFX8SNiHeoJWBDUmf1_DfwGCBH7lk5KJr9DlJGkUS-1kX3Ka7-rNtRMgmRDkkTiAV5U-MdoSjnY9DKGXonHygWAiNIRjgtdVRMIc5kaak74eNhW3dOZZSyCO30IBQNRgZA-9tQKb4FNceNVyrMsjZD-RwF_9YzDA-gEhHlzJ5q0iW2BImDNusdxYX-2T6I1FLvk1VFYdnL9sFj34ClKjfWCfPJDtfSV-5unHqcUn31QDvKqpqVV89nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=JWRmSGf8kUWIL8aXoxi2YIwdUHLQ0Gappt0r6tvXio_4cWu14aIfT4TkciHmrpFq40-sVlE8ZSRftleRSRvJg6TjOzm3XFKJFX8SNiHeoJWBDUmf1_DfwGCBH7lk5KJr9DlJGkUS-1kX3Ka7-rNtRMgmRDkkTiAV5U-MdoSjnY9DKGXonHygWAiNIRjgtdVRMIc5kaak74eNhW3dOZZSyCO30IBQNRgZA-9tQKb4FNceNVyrMsjZD-RwF_9YzDA-gEhHlzJ5q0iW2BImDNusdxYX-2T6I1FLvk1VFYdnL9sFj34ClKjfWCfPJDtfSV-5unHqcUn31QDvKqpqVV89nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Mh-MA8Hdmv5tL2x60zSfiNeNVichfhBJlXCnGfTDW0KtnynBkivwqJX0x-XSCGBjRnjfxPARgZzf5f947OKCBlpcxFMycom4MMn2ZXnElEz-t7nWgIb3uhiJFYY51jce3DwFZwqulp0_BFvyMLexA9eVyABg1-Cwkh9ARXM8x1QLGP1ImNdW3MoRzwnXAfcL8pF8KUDiaaMQABcQeeps-qFMrX-r8GBmwrgvtn37wwVySCW3ent4eaRcOulQRZ8RVK0vC1jGwU2g_3364T-MRyCAsZ6ql8_JKk1LFFP6pG0axUYpeJNtI6itz9tUFEj9I6p4n7sT3V0QuwHi7c2dlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Mh-MA8Hdmv5tL2x60zSfiNeNVichfhBJlXCnGfTDW0KtnynBkivwqJX0x-XSCGBjRnjfxPARgZzf5f947OKCBlpcxFMycom4MMn2ZXnElEz-t7nWgIb3uhiJFYY51jce3DwFZwqulp0_BFvyMLexA9eVyABg1-Cwkh9ARXM8x1QLGP1ImNdW3MoRzwnXAfcL8pF8KUDiaaMQABcQeeps-qFMrX-r8GBmwrgvtn37wwVySCW3ent4eaRcOulQRZ8RVK0vC1jGwU2g_3364T-MRyCAsZ6ql8_JKk1LFFP6pG0axUYpeJNtI6itz9tUFEj9I6p4n7sT3V0QuwHi7c2dlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=fSZclIA5ipPrZO1paIolPVxOOUSt84mUajDU-o7-wSE51uY_YtymQhn6JI9f3_ZJJNrYLFQnK3jW7L-xUkqv95pMErhkgYeT3c96W8Np6AWPsdMrY2JgUV7KgcQwf89ojOGK6QgtnFhwrsnafrSdAXf2vlVCVe_NHfG9usQMABbJNSI-RA0XOCnzjf8uybKbfp-Db9VgJ1p-PyGazyjjbGj0JeryfcvmERQM3b1Q7tOHKTT8Kxt3J7kI7fJ0QRbN9kcbMrKsTMk_t2SuZVqwc9H8lWJAvObtouWLkOzJg-nQuxdJTYrH0RJXbWJVqzAz_Qy5ShqYA2Jd3qgTDJED-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=fSZclIA5ipPrZO1paIolPVxOOUSt84mUajDU-o7-wSE51uY_YtymQhn6JI9f3_ZJJNrYLFQnK3jW7L-xUkqv95pMErhkgYeT3c96W8Np6AWPsdMrY2JgUV7KgcQwf89ojOGK6QgtnFhwrsnafrSdAXf2vlVCVe_NHfG9usQMABbJNSI-RA0XOCnzjf8uybKbfp-Db9VgJ1p-PyGazyjjbGj0JeryfcvmERQM3b1Q7tOHKTT8Kxt3J7kI7fJ0QRbN9kcbMrKsTMk_t2SuZVqwc9H8lWJAvObtouWLkOzJg-nQuxdJTYrH0RJXbWJVqzAz_Qy5ShqYA2Jd3qgTDJED-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e30uBwMlCIrMUu0Zq809ivIHyRKQpSRPETKjs94Ha7uXF6VR2SSk57CnUOiTNCpscHxw13t3y311FPN03jBSu-vn2ePEDVHGu3ZSOdIqPTbAhSOta0MwS27vaOHO4HJanJkjES0uy8qwrJa97VaEjB7N8APwnBnioH01kLB2soAoiTCcl-HFW1hIneumNlfpeWbh9-eRq0cWs-CioY0MxTw2kqrbPOCRef9u7N9YnoAOu8a7fr1GCxCGPBMcD-mzSqL_PCl-m3ggVzsKbAgV67WImrWbotMgYbfWkG2ePGS-BVOQBnfonNLgbMDe3HsLlLYJdUn4XIKte9SglWOBmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
