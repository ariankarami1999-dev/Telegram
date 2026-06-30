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
<img src="https://cdn4.telesco.pe/file/QPhxttf61Bal1DBnavNe44s7Z2aw0MzFFjELH0XlnMRIn_xvexJpAkIiesGYT13amHYS3fPaF6LEBpcuQoqUB25VszXmvoS9JPLWHVVUPLixwEgF7ceEA029XxwmAEfBWFBMuAKAZlKZPKLVqBbLknz3eUaio4W57Fq4JqbAnWR77iKPsORrv3KMSBUg2acPpDLphpVd0du0grQ0T4sZn7HmBM1SErMIxNuVXixWSWp0lETtaOleJVUGOEwHuIXdrg5u84megkKDuq7f8nWiLHOJ87iOsKQrWBBsomDNPabgGHuESG1njjQa3kYkrWQ1ozBhoOdrJQZk_8lM3fi7Uw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 02:18:09</div>
<hr>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwtalJuI4ISK7IQV7YrAvbHJj4aZpfjdhF9SZnPXUenA8e3JE6VYZ_JgQGbOAe1JK-AzhTyC-u6Ps8BU6bRa-JO1s_WMStSN1Uv7k0F67k970czKZ1Tm98V19lLVw9QRv5st6M_c0-tNi6nh_ibfKOrsdtxJFOGxW6YmxiBJuEa8oozwQrqUZsXwLC1dqMU4371nMe5z6ufR01qgVhDsgJxFeMnRBMvBYgjtLw8w02tcuhsPJbTHlZg0f6pPtYeWjGsN6844T1At9MdsN4Y8i-AwutsrC942gOzp7EnQDrtgr47tQv422sdIF6mVPhHsfqVYxNfFEM0gpUgqxz3tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkPlS5eGMm6Yc2WSpo-utRTSYJ8NveD-Uz_xnXbrQ5OdIOrxaejh4CRYvlbHJijvdWWxn98GV4MadzaLXfnGpTa-prm-wjofhmQjv_pwdLPBS0uIL-6-w4udEWjpNHmXeDi2_W1wBepQswCNwdXVRXlxvmP319q2M8DCnIeZ5381YrzMrIESYlV-3pBN2MSCKLtffFE8GFvQB3MqEiW-XV4Ebomn1ZZP4GBetgeNMsJ4tKrVoPuU9I47u72Deo-xMW5d4YXMiZLm06cBEcoJHFyVGFg_YnWkrtkIbx37p-kmdDJhVdOdc7oOEoqSR5GFelXpdoqukKaWxPAmtAz5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKj_RbNEOApa6XNKCrrK75Gw5e6ZW1EVOpYxKDb6Ux3P_MCLKBpD8crp4tmqBODk0DBVG6X5CrJuMPlligOXIjIUDciCZGi5wMBIiN2oXrD1eezOH5TBeUTDaMamIE-US9vzUSJyExD8-cyxZsXsLI6aDalTb_jzM0fSw69jzDZjlCnxH6UHvUOi743zHiMyPx6y1y5rDgLXs3Yy_uQ3kvKpGXbUPfO9YJEfprhBXxV6a-O611YvPpu5F6USuis8KmI1CYNg5iGsKCT4vqfOx-TJlWFkGqdpVu0aQPksQIUXm1P07_EdDd9XUgLJiYadFvxxCMeLZ-Tp4jpKYEDnDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CGsBezb_kAcCvvIbu3c8ORkvDGf8smzEdU_VVT_TjSLJxxcAAPp1lmm_73MDj13lpt53fG7X9iGyMGB1PsMcQLpupLmf5DrilMcW2GSiuZCPCKfDAYubJrOOX5-lGEWQ_lPQGj_Z7RnQ5v0b8zcr6mW6uHRUji4ANCF3cx6qku8f-YvfFVsfwaAETLKEOXBC0V7b3fF8ZEs5O5b5L0pubu_8VMV6hWvBep58Z96fVX13u-iprdfcuF23fzwt8ir0l2esRbv66E9yIPt5clRxOqTaEr6K5ip-KfgAS_kpXaOm2lfaOq4Fvf4DEAUkf6MOoTeznqvEFx-5KeWi6lfn6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CGsBezb_kAcCvvIbu3c8ORkvDGf8smzEdU_VVT_TjSLJxxcAAPp1lmm_73MDj13lpt53fG7X9iGyMGB1PsMcQLpupLmf5DrilMcW2GSiuZCPCKfDAYubJrOOX5-lGEWQ_lPQGj_Z7RnQ5v0b8zcr6mW6uHRUji4ANCF3cx6qku8f-YvfFVsfwaAETLKEOXBC0V7b3fF8ZEs5O5b5L0pubu_8VMV6hWvBep58Z96fVX13u-iprdfcuF23fzwt8ir0l2esRbv66E9yIPt5clRxOqTaEr6K5ip-KfgAS_kpXaOm2lfaOq4Fvf4DEAUkf6MOoTeznqvEFx-5KeWi6lfn6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=LA4Fz94EBVFVm1Cp34sJG6WOSsfnVDTlcmjvKSs-dYDwtY0AQl7vJAS_RihmCsb_5fL_Skk4PKXfEKUnKLF-0fI8Um0rSnAE8xPXFkzIa8K5c9HVHPY4TrdUi-bFiSPgDaOYbgU1q_BsnnTtcbAeLIz8hILb-vnzi4MV4DmNM8FQ3Gu1nL61fl9PCA0vdoS2b4I9oiH9OlM8pRQcL0BC536FQkBfsE0FUpFJavt9KlojYfBbTC3PAE096_KGRz747rjH4K5gbOK_TXlr9IY659Bvyc6RqBsmMRLgK3ZaEm14zLFN0UDM_Vt-zx2a8XsLUzIgRwEgVLj0ZCI6FqTTHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=LA4Fz94EBVFVm1Cp34sJG6WOSsfnVDTlcmjvKSs-dYDwtY0AQl7vJAS_RihmCsb_5fL_Skk4PKXfEKUnKLF-0fI8Um0rSnAE8xPXFkzIa8K5c9HVHPY4TrdUi-bFiSPgDaOYbgU1q_BsnnTtcbAeLIz8hILb-vnzi4MV4DmNM8FQ3Gu1nL61fl9PCA0vdoS2b4I9oiH9OlM8pRQcL0BC536FQkBfsE0FUpFJavt9KlojYfBbTC3PAE096_KGRz747rjH4K5gbOK_TXlr9IY659Bvyc6RqBsmMRLgK3ZaEm14zLFN0UDM_Vt-zx2a8XsLUzIgRwEgVLj0ZCI6FqTTHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX_EEbd8ka955gUXa8mjqa3j00ezQAkz8Wd7L1Hn8nEVCuzYntInb8g1G8PB3j6jbX4UYMq1UngMzJnI8rgc3lE54-OZHvEEC7lmVXj9eHTB40f2RWOPjlorBYln1aTS7c-p_wiO2RNOrA7kmRphQSOc0UeJaygPurCnf1Rb67TwkZ50HA1l8eTOYYvvlwCQR7ZpkYQIG4WVmRXAjTwnAez9JZILcbTNSVbzVSyCXsJDd-x8x5-WRr99AUPX3fjklB0Hi9lPLdyzpLvm9Gzs2Vx1XB-jCvs1Sm7pk8JGZla7Rbk-bZhviEfnSZg7kAgCRgsKTOywsOD2TcHt8niaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=jzbZbj7-scTgVJCSvdCzLPqTPNSkL_kbhOu_bzF3pTJ0WkGIXPtm55X7VDOj7plM9xS_VWyajJa8zUbSQveaeWC1styvAQ_9iFWkaihXHVs2e2o_1HG6AOw0irFmiishZ7blo31IShoBRlg6IOxT2yewkE5w96Ntkx0myBj7SkGxtDeA1NImw7E3C7nq9GNhowif7eIHyJmCvZLKVzTpfwFsxBJxGIrE07KGgfgN3qmp4nrfzsi22FKA2e8S-4fnZdbrbzb8jL_dUG41gVR-oTGNaBFxxHs2eMhAobUjC1vBKRCLy4TqCFV1rm6cP3nYlU9iWXoWZGymhUq3CIl92g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=jzbZbj7-scTgVJCSvdCzLPqTPNSkL_kbhOu_bzF3pTJ0WkGIXPtm55X7VDOj7plM9xS_VWyajJa8zUbSQveaeWC1styvAQ_9iFWkaihXHVs2e2o_1HG6AOw0irFmiishZ7blo31IShoBRlg6IOxT2yewkE5w96Ntkx0myBj7SkGxtDeA1NImw7E3C7nq9GNhowif7eIHyJmCvZLKVzTpfwFsxBJxGIrE07KGgfgN3qmp4nrfzsi22FKA2e8S-4fnZdbrbzb8jL_dUG41gVR-oTGNaBFxxHs2eMhAobUjC1vBKRCLy4TqCFV1rm6cP3nYlU9iWXoWZGymhUq3CIl92g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly5igrZ1ehGhU-YLwi3Ls-0096_W2bCwU9VhBKsgA37_vMRud3ZturgL_A7-ZnAMTmcnZBVbKl9ykrfLRrtr_Uyoe2seVsjEJ-PM9lp_oCaaK1qB0cBjpa2tLfhF8naElsu4uSOUTNbKZIX5yjvdzJVU6N3CWyMuDJ9jVufryb_ZzCTXTQEokIyl-Pcafe3oQ12tW4viYd684G4dtSHEbMJAbtPfz5bWGIdLH3ES5HhLXUlTliTVDucimKDSOc5bXHyfnr0GZqskLy1ghsXuU-9oFsBQFZ3pyHe36UYzXdXgrRWjNOqC0gWDyKHVCPeoUOus3Gd8eC-zXASfP8uHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=P1yi7FeWh9g_zQFRfXcwVgiTN1V_8RVMzsHPUaGDlUOLUXIR6gFEk_QmM1Hzjk88_ChYQNH21tVKqOt9V1EJAshHUdw0wz6SEMZmsYsqCfTDWLn4_BM59QXmGyTipt28Zyd5BvK4eKkrt_JzMaFPMW-fuoGlDfFwRzaEpZdU9PACvoaPX4OCmfb4D3lS4Z6KW8Ofd3CdL4Ck12GDa-OaOfguqOmIdTAhjbQSA-Kg6tnVWO6rKKpl62DH2aUWUtNlT0Gh_VrgtQXfnGX2OLAcIgKsmBQVh8c4ERS5G5sbh1WZMsMJIifJCX2pX0T5q-0hDNLTAua5W0UCAerS7zdjLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=P1yi7FeWh9g_zQFRfXcwVgiTN1V_8RVMzsHPUaGDlUOLUXIR6gFEk_QmM1Hzjk88_ChYQNH21tVKqOt9V1EJAshHUdw0wz6SEMZmsYsqCfTDWLn4_BM59QXmGyTipt28Zyd5BvK4eKkrt_JzMaFPMW-fuoGlDfFwRzaEpZdU9PACvoaPX4OCmfb4D3lS4Z6KW8Ofd3CdL4Ck12GDa-OaOfguqOmIdTAhjbQSA-Kg6tnVWO6rKKpl62DH2aUWUtNlT0Gh_VrgtQXfnGX2OLAcIgKsmBQVh8c4ERS5G5sbh1WZMsMJIifJCX2pX0T5q-0hDNLTAua5W0UCAerS7zdjLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGABtpcmRldRbeArnPKagi6V8fcMCNSgAVqAKXnMikTZyl9oR5GPs0sPdSqsR2H6Ra-tba076ly8kOq3P5cLv4WQXOEp4nSeYQOTVEUpdOl_wZi5k6Bhw9a8i74wl5d7ZNyqFU90XnCTaZgqqDA0CB4xaUv0MkuFNcOjnrwH5SDQYByqfsVaXFb5Y_mjGLcCo9H0ewI6LhelWK7rRkMlZWi0Ges2Ah-ulxIlJzAn7P-1Ft6zxudZhFqetKUcd6scLQEsfsxpx6HCn-ZipWQTu05O9Bz76AQXkgQiqIZLOe-K88j9cPRAgf9E6d82F-CGSMMvDbYC8K4ZQws_HtTcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OuE68X0_aqxSFHY76Ilmu07nIQ3MT-EEgzx6v1sMOpNCCUiYVVN2a0HFRfnQDVYaKr1q36M3w7JRScF318ILbBv2Y-Z93J7-c-X87xbHcyWRi6tg2m2oJfsKCXSS7HXdrbJfuRSw5cyn0x5Iz-3h5HwEZr76pmDrfZY--33BOJ6AcWiE7vltZfWMGmt4PbeL1BqFh9cxuIhTOd9GhdLLUJKnx-lGqnpzyo56Yh4wccEbVQN1mDMhwPItXuAbwsO7IYoIBJp_Ojqhie3mPJ2otAmd60Smu0mUHUBlYXZB1Z74DRHR5RzxDc5EByTifRoFhsna4rvdUITdxeRaDfacBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=HNd2UtviVvF6QHJQBRGQVyOvinrH8urRv-8mEMocxeG1mPm7FtCPPCWYU4MaPYMkFvJ3xjBCVe2BGzIparJKf7jjamP_M6UUVStgvjAt3cEGv76miDE0DW_boMUSSPVFBF3US2c3AVGgkyXKRRRxqjSEKAfdf0jLI1oztB0_exaHNXFJtlqhmbFw4pkeTJ3yD2BwXjXRc8hByrg0jm9zCipfqolpOzQX5V1xEDEE_Pyr5E9eepbIlyo-y6UFMrN8Nd8SYfyB5ibghB88mUxD_PE-F3nPthwSVlROBVhjZ5sn3RgeWcGV_E0ndfrQNBbwkuAwUJff_Xs_N79VYCUW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=HNd2UtviVvF6QHJQBRGQVyOvinrH8urRv-8mEMocxeG1mPm7FtCPPCWYU4MaPYMkFvJ3xjBCVe2BGzIparJKf7jjamP_M6UUVStgvjAt3cEGv76miDE0DW_boMUSSPVFBF3US2c3AVGgkyXKRRRxqjSEKAfdf0jLI1oztB0_exaHNXFJtlqhmbFw4pkeTJ3yD2BwXjXRc8hByrg0jm9zCipfqolpOzQX5V1xEDEE_Pyr5E9eepbIlyo-y6UFMrN8Nd8SYfyB5ibghB88mUxD_PE-F3nPthwSVlROBVhjZ5sn3RgeWcGV_E0ndfrQNBbwkuAwUJff_Xs_N79VYCUW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0iZx8HjQ9llnYgq6Axr7-F362uhBsOvOJPc1Je_kHD6BDwXDDuBzGs9SD702-EoJXBcVloMwVqtYCAyWHEa9oEfzbdSaLIluC8ifM9tuquO3nufxQmkDXo7iMFrSSA0KgwGA4u8Gg60G4e0G_AHNUxyF3GedyV8oSdFfx9wAufvrQh8eoFr3zHxLF0s5b1kYZFGaEDCnhujNTaJc8hRGphzlfZY0pKuf8HMhJtqfLhil3xtXzwYJs_opwTpdVu1UGjQWBTgU7ZAppfWUJ6g4CSZhdeyjDoTbyDfDuDkbPXbimdum1p4WaJ0pFu0IuAW6OUO_r8aVAsaWn20XgSucU9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0iZx8HjQ9llnYgq6Axr7-F362uhBsOvOJPc1Je_kHD6BDwXDDuBzGs9SD702-EoJXBcVloMwVqtYCAyWHEa9oEfzbdSaLIluC8ifM9tuquO3nufxQmkDXo7iMFrSSA0KgwGA4u8Gg60G4e0G_AHNUxyF3GedyV8oSdFfx9wAufvrQh8eoFr3zHxLF0s5b1kYZFGaEDCnhujNTaJc8hRGphzlfZY0pKuf8HMhJtqfLhil3xtXzwYJs_opwTpdVu1UGjQWBTgU7ZAppfWUJ6g4CSZhdeyjDoTbyDfDuDkbPXbimdum1p4WaJ0pFu0IuAW6OUO_r8aVAsaWn20XgSucU9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=DinWOiSJpVMzAtMjhwX3fEtbyPAIIQ_LGr4PLa29MxtI2a-Ur6-LBclp9H7QBvfdXLJzMktmPvKEoS9MGrP_9I8E50JkhuCaHMsY8wH8OgTYMCuq8v8pOHHAJ1ky6V1i5dlMoXUz6vtENZy6DVoO5p_QJx6V7SvuxIn7Vg54vZx8Gm_ZaJHZnGiSjGNjl5sjfIwwWkT65Ve7VJk8f41hZOP-hG0NS9jQdvw6NpqDlJ5hhETssz3M-yPpFFlwNoxi3KwWYHu3bVWln8ikV2vP11rYRsa_prQq7qrtZ2rQcshj-mQ4j9GUk-udGbWHLkMZi55XnNOuLyyH4lo9LpFF5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=DinWOiSJpVMzAtMjhwX3fEtbyPAIIQ_LGr4PLa29MxtI2a-Ur6-LBclp9H7QBvfdXLJzMktmPvKEoS9MGrP_9I8E50JkhuCaHMsY8wH8OgTYMCuq8v8pOHHAJ1ky6V1i5dlMoXUz6vtENZy6DVoO5p_QJx6V7SvuxIn7Vg54vZx8Gm_ZaJHZnGiSjGNjl5sjfIwwWkT65Ve7VJk8f41hZOP-hG0NS9jQdvw6NpqDlJ5hhETssz3M-yPpFFlwNoxi3KwWYHu3bVWln8ikV2vP11rYRsa_prQq7qrtZ2rQcshj-mQ4j9GUk-udGbWHLkMZi55XnNOuLyyH4lo9LpFF5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC1Jok--6O0bZCzcB4qXtza5JrJlFIEcUtCkTA1ipaYtmh3kl6_xP4Lqr1YYpjacPtKN3GTNR_Zb64UUTAm9tJBKpAcGnbgPsWLW0kXd3jescoCZI_ECNekED4JomlzMxMwH3Hn_Y5Qq5E-4fxsZe8M309QanP81bNEj-UyMt6-g8L1Rt0gn7AA43dSeH4nYAsIHWy3N6W2lruG0SO08yyMoYz3RIomf7UWXn88J5UvUn1fr36NEdNmaeYcPp0U1cuBurZ0o8nmsc9HFwo0X_Vgd_yfsUtr8VkJjrKpWMTKAhdj8NAsf_XLv1YEpSPyLMCY_FBVwa-O1QM25EfJeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=YicZ_SXlzfzSbKsnSO-ny1pSf-nSDW66BbKCqD_dFnSVSpFtDCWNS6ET7fx_SujaM8S4hRWFLY7c_t2poaDY-kv0fiwvtUtc_b3iavfPuG6eWmHrD9Emdx04yNvjPDUWTGXvisqfEnEhJ924i4MV4EMMGc8U3a_jfreqFaoADig5oiF0NY-1IepSAZYbmAXkcqIeNE7c3IQIJQ7Qxl7afkk65Nyrsf5qgzCJ8irj0xQJorVY44Sdo-soSkgN-5B5SzkNYwK2iHXUzA6WRuDpkiYX_3btqAx13uAhKUUBm9456-1wLoAAOt3KMq0YsZIjx4RVRix5XKHlJfpiiWN35Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=YicZ_SXlzfzSbKsnSO-ny1pSf-nSDW66BbKCqD_dFnSVSpFtDCWNS6ET7fx_SujaM8S4hRWFLY7c_t2poaDY-kv0fiwvtUtc_b3iavfPuG6eWmHrD9Emdx04yNvjPDUWTGXvisqfEnEhJ924i4MV4EMMGc8U3a_jfreqFaoADig5oiF0NY-1IepSAZYbmAXkcqIeNE7c3IQIJQ7Qxl7afkk65Nyrsf5qgzCJ8irj0xQJorVY44Sdo-soSkgN-5B5SzkNYwK2iHXUzA6WRuDpkiYX_3btqAx13uAhKUUBm9456-1wLoAAOt3KMq0YsZIjx4RVRix5XKHlJfpiiWN35Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=jDiy80x9zd88iQfzJuFC8z7CujgtX5CaqUpfE7-1kIqun7PuyemCa3cK6WGXuuGhuHhOS9xgLolmDr0N2kUuqkPIdK5SY9IIFcP8rrgOrM0vdtyHkzdbuBGJSch88YNceqnhGHgZY7Q2vo2hNiHPKncuDOU2bU-uMPndl5nj0KcJahlaC4NuNpXm_LPYTq5hiALR5g7jBrxy9iMaDs31ZHVhl-iessXf79amL9PSravSOnCHTk4wrySqVzpEMLMY6U6Qs3lksvBVGuryhth39DLdhIGz-yDpvNQylFLiCbn9rwdW3q9YYK9ErcduCLgWLX3roqLAWgjHqlu9KbEFRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=jDiy80x9zd88iQfzJuFC8z7CujgtX5CaqUpfE7-1kIqun7PuyemCa3cK6WGXuuGhuHhOS9xgLolmDr0N2kUuqkPIdK5SY9IIFcP8rrgOrM0vdtyHkzdbuBGJSch88YNceqnhGHgZY7Q2vo2hNiHPKncuDOU2bU-uMPndl5nj0KcJahlaC4NuNpXm_LPYTq5hiALR5g7jBrxy9iMaDs31ZHVhl-iessXf79amL9PSravSOnCHTk4wrySqVzpEMLMY6U6Qs3lksvBVGuryhth39DLdhIGz-yDpvNQylFLiCbn9rwdW3q9YYK9ErcduCLgWLX3roqLAWgjHqlu9KbEFRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=ofSXZtqeA70ml-VJjAKqqIZj9eIX1ANA210et2o2vd6K0w7UprPb0wK-ZaF230U6Zb9JENc0CI3V6tQxVyDx27O-cqPuM_VC1SJ3Ta3z74U01VpmEyNNIyFfm_8QSUZaOEugh3l4NbWs73b-JBIm63OrWbyDr1ABoD5wMdrv2WO1po9cEWf8rrrHelqbi6ZCcDCL5iiTKzgC3wg0UnwA8OlBgHOiF6C6pW-uyey91YDK2Pae4Vv6cAsw2HqiyBFVzCIyx4IsyuT7zYNZWGiTg3xhdl7L2wPhm68f1YdFb2fE7qH75oP1wZm7dXSscNi3_zSx_z0GMtD2j2jbHnndNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=ofSXZtqeA70ml-VJjAKqqIZj9eIX1ANA210et2o2vd6K0w7UprPb0wK-ZaF230U6Zb9JENc0CI3V6tQxVyDx27O-cqPuM_VC1SJ3Ta3z74U01VpmEyNNIyFfm_8QSUZaOEugh3l4NbWs73b-JBIm63OrWbyDr1ABoD5wMdrv2WO1po9cEWf8rrrHelqbi6ZCcDCL5iiTKzgC3wg0UnwA8OlBgHOiF6C6pW-uyey91YDK2Pae4Vv6cAsw2HqiyBFVzCIyx4IsyuT7zYNZWGiTg3xhdl7L2wPhm68f1YdFb2fE7qH75oP1wZm7dXSscNi3_zSx_z0GMtD2j2jbHnndNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=WDY7ssBPK2SvKy26fuSBOTJA97EraZhaCj0f2GccddTA370xq0bc4U58p0h7_jRikiisGL5iOt3JuoS-yQql20IMCBgNPAJCyyoDKU8EtwnT5pbOPwL-setXuxJM08wvaQvIr_tbB_UB9VuTIXM7hg2H9FXmSQ2B855rYpOdj-iKyXv9f6DofooZ3ScW9_Onk1i3df_qd0fkZwao-78VxwsXxUAEHWlQP-geiCDJ7cQRRgFEWI2tBgFpDzfo5rny7Zso1ft5MYDcnBC_w7qaf5BoCc_x5ZKOWFDc7VgaOwdGtTVGfAn28prJa0MZxxi6h23R_NFpsTePYAtoS7IWBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=WDY7ssBPK2SvKy26fuSBOTJA97EraZhaCj0f2GccddTA370xq0bc4U58p0h7_jRikiisGL5iOt3JuoS-yQql20IMCBgNPAJCyyoDKU8EtwnT5pbOPwL-setXuxJM08wvaQvIr_tbB_UB9VuTIXM7hg2H9FXmSQ2B855rYpOdj-iKyXv9f6DofooZ3ScW9_Onk1i3df_qd0fkZwao-78VxwsXxUAEHWlQP-geiCDJ7cQRRgFEWI2tBgFpDzfo5rny7Zso1ft5MYDcnBC_w7qaf5BoCc_x5ZKOWFDc7VgaOwdGtTVGfAn28prJa0MZxxi6h23R_NFpsTePYAtoS7IWBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v4d8M1OnlU-iKiWgUjChxJ4ITh5lwucnxvi1sU4Q1qkV_xGUrld5YU84NEGgwFI3LXTbY8KCWglL_kLmMBKMuhGoUhyFmZauPhjmNvkTDJhjlXdy0T90qWVUnDW3IuYtAt0KtP38NFoqToq2L3Nlu43abdD5d3yL7UIongHCYouNkDSw2rR5_N_r_nf0P7RNuC7hUqq_ft99KuZ-VV2kW01if7absXG8ioSMBmoigZJ0uACul6R7q4GSiC4qE1kwbZZc99PZT-IhHfU5TScJ_3Cmt9oAWbFOUpOAoenz4yWAPN10SCjf7ySCAtoQIIZo4g1DqMtsVWI4NEVZpOVkwA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=qz9xcclIdSqhoHUV_akqUikCCLh8_Z7Y2Zb83Xp0RXzhDG0SVkErqlKwup0sKKw4-J28LXbxzRebabY9ro7uaiQVGyNSCw5n3_crd_dU1zjmjwsgEZgaJ0xL0d3ia_3-54pcUWwjTEg5vG5WTdFDcKQKT4oumBeJ-mansEYC1PQu-4myLMNkpmizHgn_94yHphUXN0EFvJgfOf7LLJI-JXWVlHvyLANzJprcgdZMojQjXl6rRQmvQ-pHhsQYUslJX5wAFeRf3ehvdWGIiSWopzxgRXHe9pMPoibZeiYuWy-Q-VMgpoNwFlnAdmmRzWClXYaKLTX0Jx6oA4KbieJ14A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=qz9xcclIdSqhoHUV_akqUikCCLh8_Z7Y2Zb83Xp0RXzhDG0SVkErqlKwup0sKKw4-J28LXbxzRebabY9ro7uaiQVGyNSCw5n3_crd_dU1zjmjwsgEZgaJ0xL0d3ia_3-54pcUWwjTEg5vG5WTdFDcKQKT4oumBeJ-mansEYC1PQu-4myLMNkpmizHgn_94yHphUXN0EFvJgfOf7LLJI-JXWVlHvyLANzJprcgdZMojQjXl6rRQmvQ-pHhsQYUslJX5wAFeRf3ehvdWGIiSWopzxgRXHe9pMPoibZeiYuWy-Q-VMgpoNwFlnAdmmRzWClXYaKLTX0Jx6oA4KbieJ14A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=e0Y0Meo6hFbAGV3E2SaAnqfjP0vTIT7QMouyIdEa_oQpCW-xiIphoLA0drQHEAfhpp46xH7l8nhBkklHKwTzNnF3wCIWxRUmBR7aHJ5YClJ0yPqcHwKUoOqaw1YO4zhxgsO-BwBVbxROKtC-lHuZ5PpCfO3NslfOCiV1sYVn1B1DtvU-x9Hc2FGmVs6SaLW4IB8lqxaKcTvMaT8LbLpK3sHLwRSoYaW-vz50KbFj6qFgsspjbFfTtiG1xWSmL5-gbD_YSHjrO4Y7yMJHuEoznRvoDFyyq1Bnvvaqu13iCzWGtUMuPPx-APxseEQbqyg6ksGT736al-_QWXh2RPU-rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=e0Y0Meo6hFbAGV3E2SaAnqfjP0vTIT7QMouyIdEa_oQpCW-xiIphoLA0drQHEAfhpp46xH7l8nhBkklHKwTzNnF3wCIWxRUmBR7aHJ5YClJ0yPqcHwKUoOqaw1YO4zhxgsO-BwBVbxROKtC-lHuZ5PpCfO3NslfOCiV1sYVn1B1DtvU-x9Hc2FGmVs6SaLW4IB8lqxaKcTvMaT8LbLpK3sHLwRSoYaW-vz50KbFj6qFgsspjbFfTtiG1xWSmL5-gbD_YSHjrO4Y7yMJHuEoznRvoDFyyq1Bnvvaqu13iCzWGtUMuPPx-APxseEQbqyg6ksGT736al-_QWXh2RPU-rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksGpPRwvGyXwZMPNUbQdY8p6tiGJJauGI7oDIj62XZISbv8Vcg195LjzlVxsH1PwcMTloEBwlzGc_kqQRLJr-1L2U55amm10PF6LM9ot7eyp6Zl2FjENqm775IP7nNE9qCLMkotaTpevi0ZnN7MQ_j_-9Wk8ACN7NEaRD1CDU2bl3QmKaHgKm8K20AcyEJN5CKCXXg5neW9wJslvPfWye2flfVjkoy8TguplsZUacEvIQ6vbAyNNUENKsJyip6uB7fR5DzoJM9mQPJvMfG4PskhPQsnF4LrDcT1DsJOGVL2zUcjTTPonWYKIbLhWy9bKkpBiFjcr9UKVlm0iqYQYUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=txwy_dvpoKExtfXs06eRHvrnkGt2zZ_xtRmG2mGUTNygLdg84e-AixVa3FqxmVUKmgjwK_cAgAubKSsgqe0TYkHYaY26UNsyniIR7Ou4ABKdQ3IUTH4sqfEGuwpXy0i3b8Dlc8D8kqzTlpOn7EQWtZJZoH0NQyI8jYziUUUyECUq6sTCJFikvjyNap1VPcWePZ2XY5mrVWjpIeQuRW_NOQG1Rew5uWnioN-jwyz7UtGJpHhr2-TwUJHcUE22v3VOzrIa5y1I8m0iY4vg77wiIeRPQz5C_53-8VXvJ93gYZtJdFsPlLtX-o1pFB2IJv-1LlNU8x5ucvp095Oit2hFEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=txwy_dvpoKExtfXs06eRHvrnkGt2zZ_xtRmG2mGUTNygLdg84e-AixVa3FqxmVUKmgjwK_cAgAubKSsgqe0TYkHYaY26UNsyniIR7Ou4ABKdQ3IUTH4sqfEGuwpXy0i3b8Dlc8D8kqzTlpOn7EQWtZJZoH0NQyI8jYziUUUyECUq6sTCJFikvjyNap1VPcWePZ2XY5mrVWjpIeQuRW_NOQG1Rew5uWnioN-jwyz7UtGJpHhr2-TwUJHcUE22v3VOzrIa5y1I8m0iY4vg77wiIeRPQz5C_53-8VXvJ93gYZtJdFsPlLtX-o1pFB2IJv-1LlNU8x5ucvp095Oit2hFEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=UacyuHk8sn3lim_nqFAcHE5YJm6FKmisIR-EwFvKOgR_gcvushGH2N6Z-efTWYTEDhNWzF-NzfjgsDApLdK_Vrj1WKjx99kFcTKUOyoz4k8yLJzJIizCd2nMfAF2um-buKq8xtoNYJy-rMsIqFbR7NpE43xA7mFprT5mBPYdy21j33lz9QyVowEziDMMi7R82tcJFzq-kahOj60U_b9u87Xl_AycwUTn9rIspo6lKsXmD7KeE01BMtN8OdMFTEVQfLLKCkiY9P4bEQi6Zzk-uQ8LuUDRwOLzXtZHVxovRSUQcJTJJaPv2TWDIzIL8shXxmU9yXU895qP_0BX4Y0uHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=UacyuHk8sn3lim_nqFAcHE5YJm6FKmisIR-EwFvKOgR_gcvushGH2N6Z-efTWYTEDhNWzF-NzfjgsDApLdK_Vrj1WKjx99kFcTKUOyoz4k8yLJzJIizCd2nMfAF2um-buKq8xtoNYJy-rMsIqFbR7NpE43xA7mFprT5mBPYdy21j33lz9QyVowEziDMMi7R82tcJFzq-kahOj60U_b9u87Xl_AycwUTn9rIspo6lKsXmD7KeE01BMtN8OdMFTEVQfLLKCkiY9P4bEQi6Zzk-uQ8LuUDRwOLzXtZHVxovRSUQcJTJJaPv2TWDIzIL8shXxmU9yXU895qP_0BX4Y0uHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=K_iK5i4tGfTSnDqfonHVu-9QFT89PSoisSANkpn2wmPwG1PIy_mw4rmAbWI9WQIKsRJ4tPshuBuDDfwa2eYBWa1LHlAqSRNcjAFuaFEYR3w2K0fgAHKuaeDIbkKXBbYFKKw7bdMky-mKQcut3Q8IW4dqXrQLH3hqfUj7Ed4kGgdX-YxlbtR2xa5E703MTUFEvibzSER6mWD_kXuihARTZL4O2-Q6ZRhk72WssvV5PoPo7uB4hPXHKM9OWjl3_kl4UeGvsWEsTaltNXlE566DZIJCB7LM9y_sPcT4lZE2x727KnJ3cTVQjl_2zG8Rd6HdhOP5FPMVn3pC5pKlqbAPIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=K_iK5i4tGfTSnDqfonHVu-9QFT89PSoisSANkpn2wmPwG1PIy_mw4rmAbWI9WQIKsRJ4tPshuBuDDfwa2eYBWa1LHlAqSRNcjAFuaFEYR3w2K0fgAHKuaeDIbkKXBbYFKKw7bdMky-mKQcut3Q8IW4dqXrQLH3hqfUj7Ed4kGgdX-YxlbtR2xa5E703MTUFEvibzSER6mWD_kXuihARTZL4O2-Q6ZRhk72WssvV5PoPo7uB4hPXHKM9OWjl3_kl4UeGvsWEsTaltNXlE566DZIJCB7LM9y_sPcT4lZE2x727KnJ3cTVQjl_2zG8Rd6HdhOP5FPMVn3pC5pKlqbAPIDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Eo2C1-VzuEUnL5rRqy2dRnyR2sgiBB83NX0KZ84DEwkt-CqfXfREixC68kc4jwZ1VlVLJTfNYJxuY426gbzKCbLSlUiNlD4FZs9iq3A1_dQD-yTAwj2esOpuGCa6lIw-0Dxv7ev4CyTp-CAuiP2jQLjfk7HE9s2hBuxGBR2VIYhjuJXoysqX_vYcGiwMg-hx2BHseYo7O2-coA3fbqiIdYPm86cCZMvxhR56uRlHi8d2JbCnjAcX7u0nl-hbDWJ_-HyBXuxOwqcrXuvpj6a5mDsq3KdnhFxwpyYrgCqVRmAU-UNbvwlG2RJBNmiGtP40w0yGxnvBVlo9TN6ONEWGQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sdU86XmhDmoH2xA9g-u-X-n3LnqWIzK0cnNTsNa63ByLYGDdX-xSmzx2Whfs0EIyDNMYm4BsLj7nwNAqN1fx5NZlTiGXUb3DRckJh8S6wb5eQw3sw0FFJRfS6I_Db_tWBfu4p8LbXdrrU5WbjDqdEGH6dKQMyiFOUBHAVVUYf6LWNf7JnJs99vZyS7godkhvWP5OVSNLHaanXoNZKgqHNEk2Y0CXLeUaR30dNmYhLyv4sgTMUTR4AoQF81t9c-cFEMjaTuY94Hf2exNLXnvusthJlwdiXAaHOpAvIe2geKNSpC15eRUcHiZLtT1QCsDrYTeJsvLYZw1zXl-u-8dXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T8Do3cMM2Ew98Rf2qsdRrxK66d5qRK6XxklNmefOlk8TwH16_k2g3LOIkBzIqa0ZB_7QsGMkxhoEAFF3-UmKYNT114Xo6JiGGE9DWpuPDmSt5-gcfxexpOBSqcdMwh72CflNckc2CwFSHqBbBeByCWnLh4U3MCcMp3PVZQfUO3zDGlNHLpeN7HeWDciSsLkx5DqPkixlVq9HBCh8fUVcEUHjDfOoiMV_Dz03Rb3MZomgQLRjWtOv8jffiFLYzazvPWQu29JLOF91I5mW3Ww3pxVxOmHBZ8uY6OYcJK7h_M5bM5evDJIFnJFYlOw2yvVNIm1nmJsdgtHM2-U_JPhfPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=bRqHQmu9MZqVtokpXfCXvK8UweDTqe3ePPLj4rBxyjH0AyM6ljA92MKDMEzksT7XMLdJgWffzTQkT7AfrOwDTRCpVgDjMWdPMf5LfGxNQd2I7rsJALGktmDg8V8FRTxFojg5ZtsM1YaNKoO8oig57zFqwgQ9vHHY94gplv2wX1njOeR_yfqWzLGsMnruPjZtKCmxMpfToSvCFX0yh9qx5W3EdnjP2_8ZMXpc_nNpBd9ELc7lIoBw_P0wgTblUksgZ_LxiGENEmY3EHjQCNf_icqXPIt7Q4-sS939ZzouyhyFBdCJsKWchwYbbxGQerTJVNqtKmaqmZON3fafSZTaog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=bRqHQmu9MZqVtokpXfCXvK8UweDTqe3ePPLj4rBxyjH0AyM6ljA92MKDMEzksT7XMLdJgWffzTQkT7AfrOwDTRCpVgDjMWdPMf5LfGxNQd2I7rsJALGktmDg8V8FRTxFojg5ZtsM1YaNKoO8oig57zFqwgQ9vHHY94gplv2wX1njOeR_yfqWzLGsMnruPjZtKCmxMpfToSvCFX0yh9qx5W3EdnjP2_8ZMXpc_nNpBd9ELc7lIoBw_P0wgTblUksgZ_LxiGENEmY3EHjQCNf_icqXPIt7Q4-sS939ZzouyhyFBdCJsKWchwYbbxGQerTJVNqtKmaqmZON3fafSZTaog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaQlCLKnJXBEHTN7yIe-6_Ycuq3CtOoYeMXXGGtBguNs5au0bvI_jEyK_wlraic5Wmj6z7Ip8XTabfFSv4uT_P3Od9kdGT61Yv6yB5yWHavdXLwhUK7e_bRYbY9wUZXH67ML92Iz0c0l2Sf5AO2q0_fc2QRAz0flfRL2LJeRIDFVT2iqhYXjZG4c315HTQRBZ6GEsTpPDjjJHOFARd9bdoNZsRxLXENT65oGWTuLaRQq5Cudx3Iex48TXa_xgq1gR5r69uhFxP_3Hz_-JS3d0nemKa0QWoP80hhTarI8zeryO68WOpKaYovPKVlpMx7iztdH99vYNSmoFou99Nc8GnpI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaQlCLKnJXBEHTN7yIe-6_Ycuq3CtOoYeMXXGGtBguNs5au0bvI_jEyK_wlraic5Wmj6z7Ip8XTabfFSv4uT_P3Od9kdGT61Yv6yB5yWHavdXLwhUK7e_bRYbY9wUZXH67ML92Iz0c0l2Sf5AO2q0_fc2QRAz0flfRL2LJeRIDFVT2iqhYXjZG4c315HTQRBZ6GEsTpPDjjJHOFARd9bdoNZsRxLXENT65oGWTuLaRQq5Cudx3Iex48TXa_xgq1gR5r69uhFxP_3Hz_-JS3d0nemKa0QWoP80hhTarI8zeryO68WOpKaYovPKVlpMx7iztdH99vYNSmoFou99Nc8GnpI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=JGkL-l6zolgkzljr0hXbhfjEQjV0SJG0MRaani58FkWYPrhr4s74N3KJIQaKlT62o5ayfiILAHNTVw86b5oM-uA_7W72pTtpn9BGBxwpdaXf0qUvlFKRZGBim9V-1zwa48ImbWMpOUgttqqhYDgi3vdNMsnjLoxPTIxe4vSd7-jNUwS-o1GWBJHtzPfXs9cFcGQyXggyHc7r0QPQF2dd7k4FLuDwUzI98daczDmM8APJioMG7tbHsFpBJ8ipZZI9ESfWHiETA-S4KXg8y9_9F-F_NRL6nt7qOWgtPkbevMc63uIodiAK6VHmsvBEUZN9-qh1tMTr_Scho9_WPQgvJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=JGkL-l6zolgkzljr0hXbhfjEQjV0SJG0MRaani58FkWYPrhr4s74N3KJIQaKlT62o5ayfiILAHNTVw86b5oM-uA_7W72pTtpn9BGBxwpdaXf0qUvlFKRZGBim9V-1zwa48ImbWMpOUgttqqhYDgi3vdNMsnjLoxPTIxe4vSd7-jNUwS-o1GWBJHtzPfXs9cFcGQyXggyHc7r0QPQF2dd7k4FLuDwUzI98daczDmM8APJioMG7tbHsFpBJ8ipZZI9ESfWHiETA-S4KXg8y9_9F-F_NRL6nt7qOWgtPkbevMc63uIodiAK6VHmsvBEUZN9-qh1tMTr_Scho9_WPQgvJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alDw8hhih3OgIQUzvMS3dvC37fbuS6FkUGEkTGdi3uJgiLNYdSY5QoS8llfq4GWcgIZR6EDuecO8PnmDEZEHiUErWgBdZqs7aEJYodaAxHebhnQToKldwr3PImh2F0rC8LH57sY-sOYvpSTqrL_eHzdAgWoIOPAVFkDgDvcLlQWT7m2ETZrdgKzfOVQwgnET6cV8xSeLXp4pmBoUGtCYDA2be2SnD0CQCVpfYMiyacgZrg7z59-BR-a8VbqpWYaaBF1xxEJ0b5go6moYc34Jp5XtQAI3wC7CejAssg3mBceC7cj8sV_L0yhPZpwVEyRct3dMQ0Ii8TBplaCjk1A_TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHG684A6AcQ6F_3qPphV11S7w8rnIgZs9wDyXy1vCvv2ZDcLGqMQkrgEx5VCbmfVPw9OWxZY5mbfPXO65iiOXhksJ6AKfqfaGfcqXZBbhhIyEBGg3v1BOnk5dqWetA_jWd2hmcVUchirDt2I2X4SVe8vkri2KQWTlMxaw0AaaZ63qPgae_bEgb6u3BYXDwtFLueXxDdy_OJa6mQDQpir74kpSmPt9ijuLs3K2i3ZiKDDAeNrCMZ3gDha20TMYMlv1-sLPmq8Lnqi9fOBqcFfUt0MQZhrT4zy6BFrZGG5Z5FM7R-1jIOJZWVHs0Yga8GOEQ5e4Ijt9GIfk06OJrljPEIc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=M4lB4JLXoCrTgUWi7_QH_ctNglzJHF4UCrLsHZjQfGGznLYf00LFmi_o5rE8w2tj8zwuZqX-0cx-Ut6WAlRr7Spk0d7ladt8Pz-5Y93WLPBwb2EpgkJvm5DANDIq6_hXLMmqU7-20JZ8jXVJxoShcLF9sK2ZUAoj8PCziJAX6hx4DuosgXJ0uw2rv2FEurj-enwhhgOLxrVqYnurEKogJEM5MmdEH9Fg0FsFQanfP21l4eIbueLVu6KIFovLyrael5W8tZyjMoQs7sO7KdGEgydJH2zzXLgD-SntKeSdztMuPrIDZgE6o5jL0hylWVlMCubiVm6TQItyIWjtdrKXHG684A6AcQ6F_3qPphV11S7w8rnIgZs9wDyXy1vCvv2ZDcLGqMQkrgEx5VCbmfVPw9OWxZY5mbfPXO65iiOXhksJ6AKfqfaGfcqXZBbhhIyEBGg3v1BOnk5dqWetA_jWd2hmcVUchirDt2I2X4SVe8vkri2KQWTlMxaw0AaaZ63qPgae_bEgb6u3BYXDwtFLueXxDdy_OJa6mQDQpir74kpSmPt9ijuLs3K2i3ZiKDDAeNrCMZ3gDha20TMYMlv1-sLPmq8Lnqi9fOBqcFfUt0MQZhrT4zy6BFrZGG5Z5FM7R-1jIOJZWVHs0Yga8GOEQ5e4Ijt9GIfk06OJrljPEIc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fueWxIUQBE2-YmA9nag0cS9TJ0aKyrNdlnl-8tVC6t873s-CyORfmXc9g8Fxygl0kVPPzgEJoU5k4FAitMFo0AU_HWyHDgt9mC3RgNjSpa65zS9jwkjMS4fFFe92L5bBYoXl4iLVOxy4lgwqv103Co-weqmI9ouCzbSTdF8tNxSAKMDW8PgwwVNaEnwDBAP7vHNa-_plbhzeARcxWN9-Ool50LQGZvLR_Dz3hmF-PChx_RpYMH11HhtUKAiKAJiYC8ZBMndwyEmmnqoe5ukCAe5DUa5Glcg4ds_NlUqh2NdeuTzdNz8iCEN8paRzoTh_YazlJKuwXrw6tdt-Esb-_A.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Tb5Nw2OMjV5rvmyDQTqZwekrzFBD3aIgd1FXzViNQBK9hIQjCGu3z506KDEdnq7Ko9rUuS1SlrX1XBXKscpASbKuE_zrhqV4U_1NLYcCjf5fNs0NAwd6zHmt4x5UFuzB5gEYz91ual4TymHhRj77YMYzRy4eshGIfeLNf_Emkw8-vybdU0FoC6vNpMubx32sjjRPPJR6RINgEhTvvgJsBB2znFhnN9MBwRIUBcBGlP_hSx_OGPLw54tTKLV0fddwfSk_4iNDQ5G1-EVntRjmrunZUNmQ4QcL_BE7e9C9oEbYi_9h26c__DqO0Phhgf_5KcGU-Cxa2vwY35LXAw6Ysg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Tb5Nw2OMjV5rvmyDQTqZwekrzFBD3aIgd1FXzViNQBK9hIQjCGu3z506KDEdnq7Ko9rUuS1SlrX1XBXKscpASbKuE_zrhqV4U_1NLYcCjf5fNs0NAwd6zHmt4x5UFuzB5gEYz91ual4TymHhRj77YMYzRy4eshGIfeLNf_Emkw8-vybdU0FoC6vNpMubx32sjjRPPJR6RINgEhTvvgJsBB2znFhnN9MBwRIUBcBGlP_hSx_OGPLw54tTKLV0fddwfSk_4iNDQ5G1-EVntRjmrunZUNmQ4QcL_BE7e9C9oEbYi_9h26c__DqO0Phhgf_5KcGU-Cxa2vwY35LXAw6Ysg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=gtsj6Y2TFF02CH4y2gNpJ8TloG1r36YXDfZfHNp-M7OY8aaRMEFT-C6-dBFjaVMAcfY2_gKQKj7owvSZ1fPQdcE44q0bYGhxYefBjFkzXLlkrsjtX_mQQydRidtWfO-th8mGRKLz184jJjHK2UEq4PC85vw6bl0SQIgwuHUAzZWNxjYhRgnMnjf_PNYvOmHXTaSn-fXSdvPqN8h8_enybi6BN7oHNfyvSWOkxk8xo9jkTg-qe8PtMNJ9p1ryD9lwGdmed1kIRA30MeEoDNoljRVOd4ZmHn9ixNNNdYxPTB1n4szWn41v6PWQdedvqtTnOnqPpGnJv7A-UgTdUtWG5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=gtsj6Y2TFF02CH4y2gNpJ8TloG1r36YXDfZfHNp-M7OY8aaRMEFT-C6-dBFjaVMAcfY2_gKQKj7owvSZ1fPQdcE44q0bYGhxYefBjFkzXLlkrsjtX_mQQydRidtWfO-th8mGRKLz184jJjHK2UEq4PC85vw6bl0SQIgwuHUAzZWNxjYhRgnMnjf_PNYvOmHXTaSn-fXSdvPqN8h8_enybi6BN7oHNfyvSWOkxk8xo9jkTg-qe8PtMNJ9p1ryD9lwGdmed1kIRA30MeEoDNoljRVOd4ZmHn9ixNNNdYxPTB1n4szWn41v6PWQdedvqtTnOnqPpGnJv7A-UgTdUtWG5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=j6k43rrcXRahWBOEp0UCVFMrSm1hwvyBBqPvgZnomp7g7wJYNtVHCzZTZ5l7CMkuEg32bMh1lNI0tFkQOsbTkb0xzaFFVhg4eJ-0xy7rSjJvHratX51bd8_0wUzA7m1xapZi6lXwBEeFJvsEVDj2q_R_epCuQZIW5IGbgg9HdiJMmLubk3LkT-LY-woilMFXktRKkqENLZ7EfmUuuyy19dhGtT5uLG_davvbWEuLISsFbUPRphpGO3bFGAYC3VlEPEAu6d-lghIHmKAURKH9-xLgVexC34VbI-67-ydb_VHyWkI38FhbJdLJpoF0mJS7bhu44bhAEU2Egv1kSA9e3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=j6k43rrcXRahWBOEp0UCVFMrSm1hwvyBBqPvgZnomp7g7wJYNtVHCzZTZ5l7CMkuEg32bMh1lNI0tFkQOsbTkb0xzaFFVhg4eJ-0xy7rSjJvHratX51bd8_0wUzA7m1xapZi6lXwBEeFJvsEVDj2q_R_epCuQZIW5IGbgg9HdiJMmLubk3LkT-LY-woilMFXktRKkqENLZ7EfmUuuyy19dhGtT5uLG_davvbWEuLISsFbUPRphpGO3bFGAYC3VlEPEAu6d-lghIHmKAURKH9-xLgVexC34VbI-67-ydb_VHyWkI38FhbJdLJpoF0mJS7bhu44bhAEU2Egv1kSA9e3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XRADbTYgEfTEsCz_AR3wRhO-VcwKewxxmck1Rf_6mfsJAhRdVrSujLfhkz7FDCqvpH-kdMZnZYQ2rt1qN7Jao4DA2h7s7v8m7D6q7VUwcTlrjA4bXeY6F_zXh3sOt5B2GtaeZx-bRvqwwJr3YKhNzMJPMX0Jx6ZyqjdfnsICK258wKXx0piYPq3OydnpzSImR0i1BiW3MzFzzdEc4Isv7MCr5fOy-gfy6OLhTivyHoAy5vZ7K5uHv8iYR1QTQTFKkagbIBnnD2qsZK0mbetPe-D_wC16bLpuSnyIESeXTYfEHViDUaVaU8iFJ03ebbtPo9OByuSSyY34A-wXzIHXCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yi_WrTrKcZGT2LuAwlm7b79I2D6F6QC3knqP0oT6_6fyQOGRSE_LhBEoQVdDu8XljY_8MKVq0WS2US5aJX4PzTBPYd7cP0e-l-t-LatPTptNimMnsZ29NdOwKCBbFkyxdS6gfdIHn5Q2NheN6xKeNYk9j9tXEP7CixQQeV16LEaiwmf-b07b0_-FUCuCp_ChZT9PDZUitgOxtSY5ERQwkmOL8qwGCsbD7fyQSlziA53pCnSxOIpK9Zo9rJDM1gkscP_JPtx98IF6L8RYaaOjynVZqO3WEkgI8Xub9T9lsLv7Vkp8FDHA0b6Z-uSEEwOZvPIC4RHjv08cQFtsVNMiug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=XoV2Xk1_bXVo-_fXpEo6-EUzG968z1XLqHZzSGp6YIppawblZZH0lPN0Fm7FVpYfRZDTi_nH9HO1xIRRgmcS6vwtcS5s51sW_vRxjLmfIXIHaHssySmxB0cRVpvKfr1MYGaAapkcnqoMOqK6VhD2SefYf6I91kV8zLUUhEpjrPe_5jCR_xntvDWXpJACdDwgMXhidEvwrbiKgsJACsoO2XarvjcnmuUEjwNqY3SeMM6dvrG2TY0pClMk2HGqL9pRfTim0JWHYLYDrJR1n2OmHUrsFzEBonfaVYsqkvni89Rf4aw6ZzzR5KaVOEw-WO943B6tTQleK80ihBH3z5MaWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=XoV2Xk1_bXVo-_fXpEo6-EUzG968z1XLqHZzSGp6YIppawblZZH0lPN0Fm7FVpYfRZDTi_nH9HO1xIRRgmcS6vwtcS5s51sW_vRxjLmfIXIHaHssySmxB0cRVpvKfr1MYGaAapkcnqoMOqK6VhD2SefYf6I91kV8zLUUhEpjrPe_5jCR_xntvDWXpJACdDwgMXhidEvwrbiKgsJACsoO2XarvjcnmuUEjwNqY3SeMM6dvrG2TY0pClMk2HGqL9pRfTim0JWHYLYDrJR1n2OmHUrsFzEBonfaVYsqkvni89Rf4aw6ZzzR5KaVOEw-WO943B6tTQleK80ihBH3z5MaWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqmkULX0AwRdUE2U2bgewSG_kRp8AfEgMZmbyNKfDYHaeqQsiSQDeFqZJJAvjUZCOD9ePIS9u4OJy3PozKG7W3cJjg-iRktVMObxJ5y0-e2-ScrdaLCT1vDlDI6tF-4Kr7REtLzhL3hu-REEOederCpqFF8WRXUp2is_qRJrAGwA78KT05Q00Utn3i2whiOfYcD62T3Fu2uNd6LVkzYxTiGmgm-EtHDU1dVEy2hBaA9xzZKF0Vs5PmnSJ3AJaCD7p-PHmKqprzO_PNwe_1cuitTj31Ni9OREYIGS3BjGke3oLyIjZhG0FIE7QpiKQlmYxCQLZHiVfVGwHZlhjN-kAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUKzxkiSpjySxs7FGvpN2Ibw3ShZha9f0V9t4eTz5EG_Vy-fneq36ZQ6eMbe36qoNs5VdT8CNNATfo8mc1iG6XDn8BqEek-RNxZsoLC8v3g2UtTeRvTL5Ol-1GgJRCAKJbfRCCZ5GXWAXO_yontnmY1qhwM_uKJIJmVYOSTg5RILz-If35mQSbtRqGfv4qH-pFbDosuSovVOEa32AXDGp8rwZyZHmnGiDB5Nswnjlh12A6qrW1IwISHDkUjhLUqRYHSHqduDRGh8KhegiWoP2R1io9rixeubc886_9aoJ4N0cP7tmkJDOcw4p8xSHUrJCkQW3WaXZOm0246NH-7psA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=VDxuJ_wXUOFU72J1kBvEtBnzKtFgjGLK3kG7rFqPvYlcNBrGhcuSu2iqgthNa1Ofhw-DPSgpjb1wzo7MCofjFuENLozm5vzn_Fr-lg295ijsXYfHgbAWcTXsHMZbMJu-Z_yaIeZ24vHcsDsNzbhdOPeJHgQBJ47Xuy4LaQUYLDUlzLwsGxtHqWzdRbZYJLLKuyqmVM4ZZWt-f0RbNCREHwA65P3Lit3bHzWVlZK3WuTmioZymHIT2luutkeTLWKnhC99VWY0h9n14bjbXHEijhnWASlVlcPYvy3sqWGsmt0aDDNFN2K7xppYYZWecEmkoq8NOLO8hg6oZdnlqy6m7WIo4x7rwnkie2wfpszWswGoWLk5tyYOYL8s7E9S-9uc4hox-iicuYM_LiEr5bXFLY8D5KIs78Su4xu1_ncrBTw9gknl1q3nlR7gXuyiOYC6YNPmDlWUYZ2M6DZYFyJele2PfU8wyzzwvRXp76IdLwLRQ6EsarGulsNHGEmlpfMRsmZtZU8Bm4EBroTACwlCxoag2kSexjwPbdf6jrEX4QHDwgVoEuQute_wHipLm4ssqsE4ermwxXhppqAQeEZ06lpWQYRe699mYAB4ei7u355ZC5jiWeTmXUfvvfotrlkdtMIO1hUFgVMW-X5zeWZm0U9fQkrlqazNv6tFyQejQbM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=VDxuJ_wXUOFU72J1kBvEtBnzKtFgjGLK3kG7rFqPvYlcNBrGhcuSu2iqgthNa1Ofhw-DPSgpjb1wzo7MCofjFuENLozm5vzn_Fr-lg295ijsXYfHgbAWcTXsHMZbMJu-Z_yaIeZ24vHcsDsNzbhdOPeJHgQBJ47Xuy4LaQUYLDUlzLwsGxtHqWzdRbZYJLLKuyqmVM4ZZWt-f0RbNCREHwA65P3Lit3bHzWVlZK3WuTmioZymHIT2luutkeTLWKnhC99VWY0h9n14bjbXHEijhnWASlVlcPYvy3sqWGsmt0aDDNFN2K7xppYYZWecEmkoq8NOLO8hg6oZdnlqy6m7WIo4x7rwnkie2wfpszWswGoWLk5tyYOYL8s7E9S-9uc4hox-iicuYM_LiEr5bXFLY8D5KIs78Su4xu1_ncrBTw9gknl1q3nlR7gXuyiOYC6YNPmDlWUYZ2M6DZYFyJele2PfU8wyzzwvRXp76IdLwLRQ6EsarGulsNHGEmlpfMRsmZtZU8Bm4EBroTACwlCxoag2kSexjwPbdf6jrEX4QHDwgVoEuQute_wHipLm4ssqsE4ermwxXhppqAQeEZ06lpWQYRe699mYAB4ei7u355ZC5jiWeTmXUfvvfotrlkdtMIO1hUFgVMW-X5zeWZm0U9fQkrlqazNv6tFyQejQbM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmE0HxaV0Erf1qJtnsTQTaJfANtIM8XZcQuldJSA3cCmR_4aE1767iRETVW2BkNUMoPGQChQtruDjHnDNlMBxHWec6FoZGYKIHd-5aPcvuPfQjOthjZSCUbKnUgUnTtzR321eMgP8Q3CwUQhXgVp0dY8sBQWDp7t2ze-Rt7CcHhvLhau_p_IPrAl5iNb0Eb-vLqpRPMhOulKQBhlP2caOTIl4ndUukB-_12WhLbzsZUCSohTlFMyRl2Sp-3wSLhrwn0fZ-a9_IMmWzJwinM9xKu6_xCyaxXYg08KZ-CYJSs_0gOLWaqkcvd4Bwk3iwCLrurMzB1E-x7B8b-1sFtKbYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=FGbthytExUGlv7VVAMnFmTdW2bUIzMJvOsp7pkwDL8lVYtKO2oDVE5D20Q0KsyG4SD44BmJ8_L-WU2g-cP21D4bZBnOLcyzxmCcSX2g6dvqZp0VrN-onBZwhIyyNrLnCckiy2Smdrk9uUiHTG3OSBdq6akCLIGCKZK6nv4R0g8NT2C8t4zRz6uO1HkQ6KBEWVHz-OMvyBq27flYBTNYdPEdpFxJEhy-bHYGI66whvt5myxonPcRIA4fgN4jCCtovGNP20hJnbpBqKeUngG2-ZJxKxipqTzLHgP-GLTq_eRqRKd9kIMfYNQxHa7JzE_3Q7-3O-dKm6q2MH3r7el9ETmE0HxaV0Erf1qJtnsTQTaJfANtIM8XZcQuldJSA3cCmR_4aE1767iRETVW2BkNUMoPGQChQtruDjHnDNlMBxHWec6FoZGYKIHd-5aPcvuPfQjOthjZSCUbKnUgUnTtzR321eMgP8Q3CwUQhXgVp0dY8sBQWDp7t2ze-Rt7CcHhvLhau_p_IPrAl5iNb0Eb-vLqpRPMhOulKQBhlP2caOTIl4ndUukB-_12WhLbzsZUCSohTlFMyRl2Sp-3wSLhrwn0fZ-a9_IMmWzJwinM9xKu6_xCyaxXYg08KZ-CYJSs_0gOLWaqkcvd4Bwk3iwCLrurMzB1E-x7B8b-1sFtKbYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=XSzbrWiz22iiUylCURvVdNe9v08zZke2Sg-SizIeJcK9PTcQxJZhrsUypUKMeCP7DNwfQ89NlmCHu8Gyuk27-_g3miZDaZZWUfZ5weF2KyXLzWsccoiNY1qNTdHZGQrtEbXRgauH8FObQ_5vZyvE2VKoNCPygGTLrXCINLhW3vsz3lqm8HeDbTd_g36DjubH8SJo47FbI0tuVG24UWsJfhZp7523NfCbqUiXTRQppS52xKQGz6FmqQ-Zvl7oFN7ytsDIdm4espLEKfDY0kbL3wVXxGfxBc3ANqq48VClEF8Jk1R5e_VwiIXsZwYvWB-1kPl3_SVmjaA4eAlcPQGo1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=XSzbrWiz22iiUylCURvVdNe9v08zZke2Sg-SizIeJcK9PTcQxJZhrsUypUKMeCP7DNwfQ89NlmCHu8Gyuk27-_g3miZDaZZWUfZ5weF2KyXLzWsccoiNY1qNTdHZGQrtEbXRgauH8FObQ_5vZyvE2VKoNCPygGTLrXCINLhW3vsz3lqm8HeDbTd_g36DjubH8SJo47FbI0tuVG24UWsJfhZp7523NfCbqUiXTRQppS52xKQGz6FmqQ-Zvl7oFN7ytsDIdm4espLEKfDY0kbL3wVXxGfxBc3ANqq48VClEF8Jk1R5e_VwiIXsZwYvWB-1kPl3_SVmjaA4eAlcPQGo1Ii-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=rhCecmwInf1IP3Cfq27Nwi3XZ1Tzdb773DAFy66Ju5cQM4nh4c3pbjbBDLVSBRsL884oSujXyklT0yy0mSXcqE9lW08HywIUuiHHYNcC4oES2T6MwzxZIGfRKrpordj8sc8kU9Z2gst_gGFVxNmJgJtEWGPdKOwyYTTJBSo5CBR_F1C06sxWX8K0svMqTeYWNGnzF3AJ9dhs05FMBrvsSX6MsTjXU6QCBujXf8PvyjTu9lm-BnYRxu9e2iwWuT3f4S0xi5GA92fX8CSea-MwhS4pSVctveoai8iJyaaHP4wj4ApIn22jNTqCfbes4Dw16_aI4XjJjYlkYimwnt0ZTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=rhCecmwInf1IP3Cfq27Nwi3XZ1Tzdb773DAFy66Ju5cQM4nh4c3pbjbBDLVSBRsL884oSujXyklT0yy0mSXcqE9lW08HywIUuiHHYNcC4oES2T6MwzxZIGfRKrpordj8sc8kU9Z2gst_gGFVxNmJgJtEWGPdKOwyYTTJBSo5CBR_F1C06sxWX8K0svMqTeYWNGnzF3AJ9dhs05FMBrvsSX6MsTjXU6QCBujXf8PvyjTu9lm-BnYRxu9e2iwWuT3f4S0xi5GA92fX8CSea-MwhS4pSVctveoai8iJyaaHP4wj4ApIn22jNTqCfbes4Dw16_aI4XjJjYlkYimwnt0ZTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kPcbAZSOcUAf48ju5evKNVaySbLLgBIXt2dBl2xA5-eWh7n9LFIRjLlX7yP-SsS95VXYr_t-L9hOT2BP5hLgfQal2RKhclyIGnx3NTRJqOv5Cl4yhQU0gvxMV-iBkgSiiQI68jKQINn9vD05EcV1GroAYEpaauZ09NZ6Y1cwpOaF635E0S3Mq-AXVZwR-4nhFZbhv4pMhbW_ITA9JKxpN68Lt7Nyn52fW7mtdVM_QHz936VmPgkLdqLTaeFEo3e5siBCWx9As4I9Qycu_2ehzgCd06P4Qt0qUT2dYZ22DhBt8MEJtJ-jIGXfQ5gZv42uCtVHWBm8ZoJ2RjM05AsuNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6dyVPeQZiXU7OWU2p4YSWlB0_wy0fPsah-n8cbRdSNH-PQc1g3tY_9RHk8gE-iVaR8m2s9o1oUTIy1NWX3ghGDMhPvtbAiB_0kGm4WfOFkk42F8CmNvHTKHwQzqgwHAGA3qfVSbczFX5FuJEX656oonccOqfIPKYOCElTAUhXy2C9YU67bBE15XuCWkOjZhKe0nhlla0W8Loxb4gd8NZmigL6VpAFpIHBtsZB9uvqzvUSFHyklH5hi7aLSUr74JVEqRqYQw66sX-NJUPH_WPoIvjAZz9kJRCMwlown7PByT6GQ9G3MXjZ1om2oLZnKZfWMeeJMcuCFf2bv8Te3RDg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKV5cUf8lWTfqIysS1tI8-Mn3mxYPehyetUb1El6X2olYqqDHpCeDdAtTIAJG4qno5SCW0axsYB3vegBQga9dJuDLvjAAs3TMBM3Woe-3yLzLS2gx3Gp-arJg9PA-mlTsxxq3Sg7vbt_V0C6EXHTNihG6i4YUb2rFBPdDaINr0E0xGZw4pipsaFGLSJIjLxEONJ0ZN541aAJXyHow5afrQ11rA6tVhlNOWroF6A0MTp0VWR-L70NsmT5OMABXbhRa2D_X_TtIjjXU8kAUJu0X1BXvI0O6vAS6Wmh1N1ESQKECbzjG4DgvOKqfpxirPuIYOAH-IP0ndBuBfX1juUbbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJVg98knM3AvvmFFUabfwSZFMBCYSM-XoQ579BWCZFPk5mkLd22BlfCwqYkFohB0d_R6IPHgIsxLq1LH5rgCP2tB7ALs4X8Q4Y3dOnbQemj__dDCyQ19ndnGK6W8BDm8gsA9zGjobuA6wQvlqBBBEXeUgMT2kK36oxqM2kY0GIUs8rhEWSnZOmeaPe_-JD1XG0tqGj4c03qUJdYh0dZquZjBNcMLi2j2GbOTu_vPl05_5u_0adUpY2Z4LHhPTpQ0iJ9TejccTGxpmJQz0LZ33iJT1Z1KvjvulfRxNuRs3B3NPaMrc_pXndS9w5AegdiiakocdMJajhPWfCGO_AOFXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/murOERzPXb77YA9AkvgYJsdQj1zsfWX14lHzKo8CsrThSXzqtSUTbyCj0s6i6K8uK2MyUj_UeYW_YLeJWwtuuDav8EXvJr3u1Ba8FZEKD0cufgp_g2CnVGtUXrJxywzd8BtfBrhJOrRUROEtgdOvTAwt4d5y-Fuzvb6gCeR2WWwUbDPbJSbMWOyHo0qCHTRp8U6Mb-dpJ1-Z6ZJoyWY0ZSzGnASWa6lyZmC99Yw3uEHwY-YL_544QNx2UHHZHbztDezdoJslOe8kXwmoHKBRfXuDKZ64_2V1cr_mw1cFf4OSOhQRz2yLqYgM0B7EaIzAUxBA4FtD9-5EypPBmxCYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=oT0CwWZdvjGGQZtIC852vrwm2rfqgum20h7q-mD2XVYZpSqlHGlAZRdYOE2_WFy51Q0ouYIygSx2hrN2iAYF_RifpL7Aa0dtIJ4EtHFslBA8n0RxjPFjcNByTexJkcdMAGH1JXdOpWUVPw__Vd5SsVm_TtCEZT-LmehCxeV3e7WUaI8sJ7zjWhonY8Wmy2kQ08RXRBiRqrFVIBem9QAh3aL3lxfRcDt1y9eHorpetfV7BdI3Oha68HEZZi-YtE7NE75X6VFXDglDAJG7YrMaWFb1ZI2J4nSkmYrwNL6gN4IHCRq8QkTUmuNigopKaul7_IfKdMGEkY9AbZ8jQ4XbpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=oT0CwWZdvjGGQZtIC852vrwm2rfqgum20h7q-mD2XVYZpSqlHGlAZRdYOE2_WFy51Q0ouYIygSx2hrN2iAYF_RifpL7Aa0dtIJ4EtHFslBA8n0RxjPFjcNByTexJkcdMAGH1JXdOpWUVPw__Vd5SsVm_TtCEZT-LmehCxeV3e7WUaI8sJ7zjWhonY8Wmy2kQ08RXRBiRqrFVIBem9QAh3aL3lxfRcDt1y9eHorpetfV7BdI3Oha68HEZZi-YtE7NE75X6VFXDglDAJG7YrMaWFb1ZI2J4nSkmYrwNL6gN4IHCRq8QkTUmuNigopKaul7_IfKdMGEkY9AbZ8jQ4XbpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=VzY75YTarsKJLw5X31hClNz43030Gb8xm9moQ1pPTwxAOb9Nm3H1eFo-s1XQnS_IsxHMyU2s24BjBTEGJ8s6-1Qcradrooc0ki-JOX-69dc1R_22R3PD7Rb6o_dGn9NvRCFgMdQRnx2mipZsXFPcq_SZFrVHoSPDFFHObl9WEUDrmyTFxBFR_hLbIsfNmdMdPDbTMhwyQm6jy2ipcn4UxhcWcj5WNXOrAIFgdCVaNTmbzvwCQoWUixLs5U4oP5neBsr6v2inuttuEHPZEBefiUEQKd6xxHh1LfjRjJyWS8gcsO31lzrIjqNKk42fG5TYBLShmDvRs3qxSJNcDxdzFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=VzY75YTarsKJLw5X31hClNz43030Gb8xm9moQ1pPTwxAOb9Nm3H1eFo-s1XQnS_IsxHMyU2s24BjBTEGJ8s6-1Qcradrooc0ki-JOX-69dc1R_22R3PD7Rb6o_dGn9NvRCFgMdQRnx2mipZsXFPcq_SZFrVHoSPDFFHObl9WEUDrmyTFxBFR_hLbIsfNmdMdPDbTMhwyQm6jy2ipcn4UxhcWcj5WNXOrAIFgdCVaNTmbzvwCQoWUixLs5U4oP5neBsr6v2inuttuEHPZEBefiUEQKd6xxHh1LfjRjJyWS8gcsO31lzrIjqNKk42fG5TYBLShmDvRs3qxSJNcDxdzFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fy1k5Vf7YwxgThKIkhtVz36vWtwgUSoq3WC-OIvWJnGe-L59JimCk76otEfQpUMmPaHKaEUyAxzkcrQLUFRRIXbUDTIBXfGwC4cJpRAst7CdIYe8DPbELfAf5yfyMpqiH2aw04EZK2BQGEOq4cSp2R4z9D8tubuCPJbNTv9RbrtQwnUCR-WuDA86T4uN_-UIfpDqzKEIVbEaa8nsVuypeZXoSWi6Z0vyxfaYJschQ5-SIn3_8wlyg6fuaGl6sKiEz0nxG_lhoRo2gFxSCYFBauCBAOKrPJUPA9SmhD1cNwWMYacglrtP9ckmxz_67GgJkH1rDbvOpj7qSQmV5JBXyA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NF7KERBhAV430yuSCttRDvz8alrloxKl1YfesAeoxHmNP47hfSaBCiMr1KRBhRyFCfYpn9nD0xBPEIVmN5zj9dn-eTBpPPWc9NTZVxp6M1TDDJgKDMZgpoyq7SvK4zIw3inw4o2jlFb0Kn_9Pq0G_HAQhXv4SWJrWO4byjDWm6TVvwVbtXMhsrXqBEy1xr0TzaZwdLBu_OM8LB2GzFBdzbcnQWpDChkSjOCTcfBeOFVxb-FWPJbuki-krgfYGnenLkYOwdSn75Z6b6fDhQkp58edt8t5FuqCOFrH2988ELTiP5Z4c0QgqqSklVPXaRN1gcfKZ0dYCOsasQ529RCpEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=MF4WiKiyxaFEXBmzfnwVFVRnyd9Mq7A1mk9A548eR-2GmDUs7o9lD-9lIWIuMYjv216ZHEZAWc_DEr2LlPdjwRGEMVMIr4zLB9iZFtwoMZTu2khjKvIwB_0IwvoKHGKGtaqx3LhpUTjpGFQadcCKlFAOYNJmgOJMeJtpJ7D9pt42k76hj-cJBGB_Svjl1iTGyAyyfq3P_1ujSh4HTqBHMgGak67poLO0KXBDsI_yPHHuXl1-0shYKTDOWROvHGlCjXWb8tvzN-YOggLGZIv2F52RFYqdcvGTPhrBN9_CorLG4ZUTtoZyDgjFH1XqoMJuOir1qRfj20F85uB2St-jeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=MF4WiKiyxaFEXBmzfnwVFVRnyd9Mq7A1mk9A548eR-2GmDUs7o9lD-9lIWIuMYjv216ZHEZAWc_DEr2LlPdjwRGEMVMIr4zLB9iZFtwoMZTu2khjKvIwB_0IwvoKHGKGtaqx3LhpUTjpGFQadcCKlFAOYNJmgOJMeJtpJ7D9pt42k76hj-cJBGB_Svjl1iTGyAyyfq3P_1ujSh4HTqBHMgGak67poLO0KXBDsI_yPHHuXl1-0shYKTDOWROvHGlCjXWb8tvzN-YOggLGZIv2F52RFYqdcvGTPhrBN9_CorLG4ZUTtoZyDgjFH1XqoMJuOir1qRfj20F85uB2St-jeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=IvtYFxEgOa_kJWmt2hV4e3S6YQrmysbU7KFazAveryFPVt0JApybryOHDcBaEG9rTVaNOrOAJ55k8elKMx2sDDMeyE9GpJKoCKfuU8QTkU5UdwXt7Hxmev2hcNdF6jC5Md3MqMK7MGKM9EGginNmg_ZSXK3SZYXaaBqXx34I8ops3wJEEdWHEtOeOvbQ529C3Y-se0tKSv6GsRdJEKF9kF91da9TOCgRcuYIb-snffxjD3Y0Oq94Pr-F0SIwyZ7TvLJrhkdk-UEAM0gLpNbmP0rgJ6JdYhhiqd1DsHMARLXbGBVfaVf5tjTafVbZWGYj7xE5W7J02kxp1MujIka2Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=IvtYFxEgOa_kJWmt2hV4e3S6YQrmysbU7KFazAveryFPVt0JApybryOHDcBaEG9rTVaNOrOAJ55k8elKMx2sDDMeyE9GpJKoCKfuU8QTkU5UdwXt7Hxmev2hcNdF6jC5Md3MqMK7MGKM9EGginNmg_ZSXK3SZYXaaBqXx34I8ops3wJEEdWHEtOeOvbQ529C3Y-se0tKSv6GsRdJEKF9kF91da9TOCgRcuYIb-snffxjD3Y0Oq94Pr-F0SIwyZ7TvLJrhkdk-UEAM0gLpNbmP0rgJ6JdYhhiqd1DsHMARLXbGBVfaVf5tjTafVbZWGYj7xE5W7J02kxp1MujIka2Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6fdYdnWD-80IvlR7j3a3vn-eFBRhAqIJxoiA8HWmI081o6N8qa1-QST_PqQbHHRSsRY5nQQMoOVtM1RKpjc3hTEuTl2TB4t1koahRpzw9SbnZcsK1_UwkUrkUy2AO4wMYdYyLvBz5jTIDhFP1S7-OhWsLAI03-EwZcuEACZDeEXYme2_soZCHoo2zNMmthSv0LOLhe3lPKRil_J5F4tIc8y8MugFzxUpe9ziN_0FN4-HiJXWbzvJHJzskbG9Q267_U-f8epVWCLJTELlsIERaNvGy4BWM3iL-0tnlPjJYcrGOdZbAf7pRQccusVg9oZH_XM9Q2rQc2evrp4uHmJSw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qze6NfrvT1Z5k1Q9gKl4EsTR4-NtLpz0UsXr7SGYqkNsYmDSm56Q_GTY9DsMLgNOlj2e5qRY-thIltyUlkBeSNtcZqEZFo7Es_hOBlYj8D1WcT5knpPMtj5rVFqbHZVJSuiVmlIWIuE9aECdjZ0tULYOE3I-6MaxiVHVcolfmW8rEpWHIl5EqbBETpd0AaeDDBgdYd4PY5e5f75T4t8j-ENdKQlxCirDT59-OUGlCIAGDk66vBICj51rLWTWJEppUT0tl-NIJFV7wpLvXkKICH8M5b9Wjg8swf3ty9_HMff-I6EopeSzEe0y-N7ZNcEnGiMCV_6-qVCy3V5kkYH5Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVTA69UmVeeQLrnGHiMP3g0xGn9JIDm7Jef85ps4f9J3jzSjJlJq4TSwtnFR1zzQaKjjexlM5G9SanEl_oayswpqkacSEXGD8jkFzIUs4smtjxjWMn09y16aS-_KaQL8qdVVxuaJqXCkwjnmupKo3_rEnRNSSDKhHXKeOwMbKvTOiN2Eodg9O1X8WLHwKfVJLAHi7t5VeUkX_yzWqARDG2R4QaWt2sZxdHsuy4n-Aw3Dva_ECXPO5JDVzbo5_QhxYmh7lLtM54rfSUvxRKDMvA8S7HB7Vgfagx_jGtOutlfW286oaO8nhrIELZRSY3n3I3X4c5jjOkdIRWdxW4ikxQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=XinfZlSG-9LajhOIJ2gucOV01MMcOswG6aFFx2zFW9QUaj4h8URJoXtUpv0kKiag3yCbFrc1TQcPX0epxEOLQ8e92-dYxQXEDeT1dqMCFC_J9WsIefig1OJAtOnk207kRsEpLdo1DM4vf07H7b6rHJVSkUwuaR_Yv6jfmTo9ISLooRT1zo17BIyB2InZUs6niRheotpmUaHZcnkG4feShR0rI3vQKsXbP-9-coczGdytCtzTStIEgqDmF8-CCJYPVMyLDX-egpbJviFsHTWq0R6J573DA4V6c-PK0BRkrCaUpSQ0lvUCLJ4drlErnPRZSy1awI6uW77lUnIlIIrzZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=XinfZlSG-9LajhOIJ2gucOV01MMcOswG6aFFx2zFW9QUaj4h8URJoXtUpv0kKiag3yCbFrc1TQcPX0epxEOLQ8e92-dYxQXEDeT1dqMCFC_J9WsIefig1OJAtOnk207kRsEpLdo1DM4vf07H7b6rHJVSkUwuaR_Yv6jfmTo9ISLooRT1zo17BIyB2InZUs6niRheotpmUaHZcnkG4feShR0rI3vQKsXbP-9-coczGdytCtzTStIEgqDmF8-CCJYPVMyLDX-egpbJviFsHTWq0R6J573DA4V6c-PK0BRkrCaUpSQ0lvUCLJ4drlErnPRZSy1awI6uW77lUnIlIIrzZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uz_cDoehAKUPJ_34xoKExdmZLygNZKInPKESnvc7Ka-uM0fKkDtDQCMTApiUn0rHFzIILeGyCtKVIsMClBpK3yjRyXe8DXBFvDlsbP-DBHX_2wDFCOE2x5ow21Zbcc6qhDMvX6F_3nQlNkQc9MhIbsGoko9JSCzhAUb1Z8bJohLWEehxsX5MiK-ZITX4qtYUgpjSe5AKiuexaOlVzZh6QaPgfwd6HbcUE9DYzE6aZ-Msg1pXQnb_y3ofqNFjEGKk5iHHP_ycML3ICi57BmGvSdm04qcsfj99wz-_eCjCXUEXWadkEV5n7sLMcbdb-BpgPTVotA0hl_Ubvq0GY3z5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyZXfE8jVQmQaXB0aaH0VwSY7aOxv2imAeqMGH1Vit2_vJF4AVjQHjyE0M2JtwUe1YqU8RHErlJKQCasd34bYqJrVTiOwcW-JX-ceaRKtpp10cq85orpfUbFSoSgnE-GRi1mSujDShLnzHSHousDogElsFz-MzkxdH2sYHXND0pveAhUy4p2-oUDBW4UznU-mslHFysijyFWGHJIsL9RMAJcjVCL7bYTKlrMSAqi3tlSOB0Mia28yTHFVw-yi6jnKcrslqJ5nTKbNzxSaooZrN-o0u3r2mjLcq0B-4R4_gleUbxtGDMqXmm1UdPt_HmKe3HXl54MeTNjPPU2YReHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A7CBmV70VgEKiKJclme4VpMHbw-dbgLd85TSR5-WA5Df22KpdyQCQW_bMT8Gx2KP0Z11KdRrywoEg2LkruJaIM4NBggXV7yeQJNqU7qavJ9WNrGX2xmFvn2Fk43dRLAFUAIKjo-D9E9KsWpfhkuZy1KHIt4lsvTVcM8I7s7Jb-7L2G9BSvAQ6S8QyQPsS6D9b-pOkEaqzko40inutWfMWKkhdJ3uXUpPDkTitIBPlYijMuzuEWO0tfeEF0LvCKJ7iOIvvLSiD2NdE1PNlKVqq5J84rOxY4mO2y0ugZr7IDoERY96KNQ1Nn3CFTiGRXrX2XuWRFHM_TTpfIPyKwS_lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TG5Q2jSeM0MT_f9bQYOhPyu2kUC4YQN0uKtk34xczKLYZr2AZLncsaNqCP4l_8V1MsKMIq1TdLn3U2QEpB4K3G73vjvtuFlKcfGzFmSsWIvGhzFbfprsSXEzSJMT_la2jM0PYl0TLMOcMTiUDWyyI2uTPsixV3OV9oJtOsCBpLkcrbAcFHcMqKjiKpZA4flFwA7Nj2whpPH3fOvtnbq6OfN7k4OebVVGh42wFK5VLMbN2LIcxX_B1LFwCbG8Uzdk0zzPgzbyIX0OQq5GdbZ9yvf7ImdgLdvIqjeIJA8aECXBtZ3-Bv8uzvSJHS8bh0w5oDe6bqSZ2gVuIJ_tCDSGtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=aeN5-dgp47YLumJvHymo8QXc_XDHt6klCBxzsyUa17Oylor6XIaQO8WzvbXh-5NIGAAhqJVlcqBf-_Jk_msi-BdGBCWEMuL3pO5GMKbxU524S4AuZctthqLRKhHs-brzfJnXuyXWcfxOHjx6suVu8I-m5iDtAeM1rF_2xz9K7syIEL8lS4ZO3A09mpwyrs-IQ1kxHu9-e09bAeK3M-4rGoInrAzGn4J9EEBcxGz50X7ofJzREn_m9JSEv68oVf2Fj9KH1fyJyK689Y7CQkZH9IUx_QyFw9ZyhJ3biHB-x62zVfCyBpbg4p05QjEGP5x5ckv-tYY-ij3NjR68yK6kIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=aeN5-dgp47YLumJvHymo8QXc_XDHt6klCBxzsyUa17Oylor6XIaQO8WzvbXh-5NIGAAhqJVlcqBf-_Jk_msi-BdGBCWEMuL3pO5GMKbxU524S4AuZctthqLRKhHs-brzfJnXuyXWcfxOHjx6suVu8I-m5iDtAeM1rF_2xz9K7syIEL8lS4ZO3A09mpwyrs-IQ1kxHu9-e09bAeK3M-4rGoInrAzGn4J9EEBcxGz50X7ofJzREn_m9JSEv68oVf2Fj9KH1fyJyK689Y7CQkZH9IUx_QyFw9ZyhJ3biHB-x62zVfCyBpbg4p05QjEGP5x5ckv-tYY-ij3NjR68yK6kIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx6pXE-u974voRjhtcrk8fGGiX-ewUsYf3tCaY_6LjRwiNH0Hrsq0SEwmwCjzYB5IZR2n-uGpHJrH3gZgZr8tbYUp02QhBGxZ0rPsGt6uAQNdBW9VdLqvZd6dBM2AAfl8O1v3UmBdXAYLTUik9khuO0BGDaHb9vfcIgRp18UG_PA_j61x3COyMxt2GpwAz5EGt-XDjLRK5kZaH-SqJ_VYznrKmmsTYDDne0w9Sk9p4g9yKFSJtOFUfryXVEiQXDxrTY6kTsJ32FW2laCl4FU8DfyWDnpYZIRE_2BlSf6WoUsI9fZBsLOt0igbrTuxkk2JF1RwqUhAhQYsEtKdVbDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bi9vYE2a__uwU48dlLBaOwOD6TBDAq5nv9EjaWbABfw5XYJIq3isu_9DATt-A-_OWFrTtgZFQcc0g7a-zQ0nFsA5ACIegp-NP1QFmYUlnrQnKrAF7j6T8KVVmcjaVIyP7HTUNeIH0Dup93fWp-0NBStGhuFgl2IgTJ9ww3loLAL9hxd5puDMiguTzIpBe6TSTrCBmttoVosm-ykKrEAQdKUZ-7XBO0YMV2jX0gcPlOXcT2YaUPLs7z3KZ4MLWJBRZywkyL68xmAs6vX2OruGIKMSBRMBTROipQx375UOTo4yGIjN2ImybWxKzHlYLYqYGdFuvmCrykyV1qWfyK56SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQKYHVEcBq261PpFJ7FkjJ8doQDS5SK80E0RFXTGUs-YcOi9UHgVjX-9YBXZqajfcNWDn6tGMHn47Z1c41AhegEvkJ3Z8LDY_SEeYHYkymWzzsAx2rALEFtnoKsyvVbjwU7c3MR_37xnwM_kF-DxBlBtRtAJ26MppsRE9EVUzvvrGCOyIcMwREzaBybyN0dQPA1fbeaX5J1gvq7TFH4_YuErMFwTQLCyXmMgpuhZ0ky-O3-5S_P_D2wL6_E_Ru4kuLYEMvQM1SUGnDF-KD-PgERqbpzxBdSTJn2kQYjVGcR7hB6m9ssn9gxXButjPRygWE9tp3rpWNIuQSvwI8eKxw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=ACz5A5rlwSsK5TBn5CBgp7qtSB-Krm8tYlSc9TURQE_x-A_uZfZyD7ScUluXSoOzwJSm6U_fymebJtuznHgvVtFmiBIQ1o-_aO4YPF-MLo1xfZfYURdN1rfZtckkpsKgifwKOb2K3qfTejBWn-mi7laJhXF7ch7943XAXkCtSKyyUqkfV8_CyxXOqv_mY1PoC6p0tYfnNmuQumV4GON7ls_CmcwdIw3bYvEq8Aw_ylhwa5l0l8Eb_Q3aWf3mMsMty4bVXyl9yzFVLhWULhTP5CJ0wN06frZbgODQXRzMZSIfLZFPfinGExo_ZQLQtNcKYGHB_Y1QcptEDxREJe46og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=ACz5A5rlwSsK5TBn5CBgp7qtSB-Krm8tYlSc9TURQE_x-A_uZfZyD7ScUluXSoOzwJSm6U_fymebJtuznHgvVtFmiBIQ1o-_aO4YPF-MLo1xfZfYURdN1rfZtckkpsKgifwKOb2K3qfTejBWn-mi7laJhXF7ch7943XAXkCtSKyyUqkfV8_CyxXOqv_mY1PoC6p0tYfnNmuQumV4GON7ls_CmcwdIw3bYvEq8Aw_ylhwa5l0l8Eb_Q3aWf3mMsMty4bVXyl9yzFVLhWULhTP5CJ0wN06frZbgODQXRzMZSIfLZFPfinGExo_ZQLQtNcKYGHB_Y1QcptEDxREJe46og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=PjTUPvccj-uASD020DySWC23Fp7itAfgksXoxfIWcUjo0YEHOwM7lz1XGzn2B1605o38dj_vcj8Cx-YD-koWfhtlllptiSbgB3zUvOWqTQd0OfelO-uRXeX3vn5jF3WJbWtCm-Z72iGxTByth-hkFJDq86hoKpn_LsELkqdiT4d9BOhhtBpW877gsz0crqSEKSFEIZeY-v8tPrx163qhzWMEe_StxhH3ZUCi-14LtErqsmdnIwvMTbHNufFQ441NlE68le-DOsCTC5obDPAiRUENP3QMjwtymyvo_arLZ7uXgviLTn9w6rJ3ZFPGDXmUMsGUvJWX6vMC6XibcyRHSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=PjTUPvccj-uASD020DySWC23Fp7itAfgksXoxfIWcUjo0YEHOwM7lz1XGzn2B1605o38dj_vcj8Cx-YD-koWfhtlllptiSbgB3zUvOWqTQd0OfelO-uRXeX3vn5jF3WJbWtCm-Z72iGxTByth-hkFJDq86hoKpn_LsELkqdiT4d9BOhhtBpW877gsz0crqSEKSFEIZeY-v8tPrx163qhzWMEe_StxhH3ZUCi-14LtErqsmdnIwvMTbHNufFQ441NlE68le-DOsCTC5obDPAiRUENP3QMjwtymyvo_arLZ7uXgviLTn9w6rJ3ZFPGDXmUMsGUvJWX6vMC6XibcyRHSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=Ow0RGYEDMRXIilkkb4kBKQkCWMiZbRjgpNW3cDpJCq_tW8UfM8b-WW5Wo79_Yrt_CMoyia2uRVViYskCCJhZG0VxFIHXsaObk1zAd6GymXe1dH-PPmU4PReu3Js-2XTcSo0M4aqXvf34_U27635iQsxc6uKiaMcEnItoAS0SxdrPsnbqnMFWlaIuIVjtF-Zx1BlCcp_7v3rSzBYc1eKGgVUMscimtkQalQXdEjs78rZFZoqmOg-fEPxgeer0TgnpOVDNPvLadPTrEP772S94ccCun6bfTndFt95BsHSMuFpCvF6AsQ6tq2hYT_1CZergjlsGvV8vQHDxKiYtPPh1GA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=Ow0RGYEDMRXIilkkb4kBKQkCWMiZbRjgpNW3cDpJCq_tW8UfM8b-WW5Wo79_Yrt_CMoyia2uRVViYskCCJhZG0VxFIHXsaObk1zAd6GymXe1dH-PPmU4PReu3Js-2XTcSo0M4aqXvf34_U27635iQsxc6uKiaMcEnItoAS0SxdrPsnbqnMFWlaIuIVjtF-Zx1BlCcp_7v3rSzBYc1eKGgVUMscimtkQalQXdEjs78rZFZoqmOg-fEPxgeer0TgnpOVDNPvLadPTrEP772S94ccCun6bfTndFt95BsHSMuFpCvF6AsQ6tq2hYT_1CZergjlsGvV8vQHDxKiYtPPh1GA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Li_mtCeMk0P__U75aTht3mrjtSgoniawpMWvAf81j9Oymhaq52teS0WKDGwCBs5D7lrWXghm_RhFeAbZiW3kVSELEjY-MoNzYzE7xtJ0qn9ENt9J4h0dXUzlUhBE5PYE1s14mAEpQ1UqW5SfN63gfsDXY0SVnR-2SP7dTKW9DgXK9edqz1ZrQid6vJK3VbBbu5btTrrZIYqgtEAUThp2Jf8LNHe2VxxuYbRYb0whfoSMLNl1mn7kIMA12jfCuD4z1NFxRpi_6FyXMvHJzIPnUEVhcQvBFmf_vmFP--93lLnmqTYxRmLuJvvimm0hFryoiXAjqmdHubrb1T5njVObrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
