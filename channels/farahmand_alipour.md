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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-10 00:42:18</div>
<hr>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwtalJuI4ISK7IQV7YrAvbHJj4aZpfjdhF9SZnPXUenA8e3JE6VYZ_JgQGbOAe1JK-AzhTyC-u6Ps8BU6bRa-JO1s_WMStSN1Uv7k0F67k970czKZ1Tm98V19lLVw9QRv5st6M_c0-tNi6nh_ibfKOrsdtxJFOGxW6YmxiBJuEa8oozwQrqUZsXwLC1dqMU4371nMe5z6ufR01qgVhDsgJxFeMnRBMvBYgjtLw8w02tcuhsPJbTHlZg0f6pPtYeWjGsN6844T1At9MdsN4Y8i-AwutsrC942gOzp7EnQDrtgr47tQv422sdIF6mVPhHsfqVYxNfFEM0gpUgqxz3tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkPlS5eGMm6Yc2WSpo-utRTSYJ8NveD-Uz_xnXbrQ5OdIOrxaejh4CRYvlbHJijvdWWxn98GV4MadzaLXfnGpTa-prm-wjofhmQjv_pwdLPBS0uIL-6-w4udEWjpNHmXeDi2_W1wBepQswCNwdXVRXlxvmP319q2M8DCnIeZ5381YrzMrIESYlV-3pBN2MSCKLtffFE8GFvQB3MqEiW-XV4Ebomn1ZZP4GBetgeNMsJ4tKrVoPuU9I47u72Deo-xMW5d4YXMiZLm06cBEcoJHFyVGFg_YnWkrtkIbx37p-kmdDJhVdOdc7oOEoqSR5GFelXpdoqukKaWxPAmtAz5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKj_RbNEOApa6XNKCrrK75Gw5e6ZW1EVOpYxKDb6Ux3P_MCLKBpD8crp4tmqBODk0DBVG6X5CrJuMPlligOXIjIUDciCZGi5wMBIiN2oXrD1eezOH5TBeUTDaMamIE-US9vzUSJyExD8-cyxZsXsLI6aDalTb_jzM0fSw69jzDZjlCnxH6UHvUOi743zHiMyPx6y1y5rDgLXs3Yy_uQ3kvKpGXbUPfO9YJEfprhBXxV6a-O611YvPpu5F6USuis8KmI1CYNg5iGsKCT4vqfOx-TJlWFkGqdpVu0aQPksQIUXm1P07_EdDd9XUgLJiYadFvxxCMeLZ-Tp4jpKYEDnDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX_EEbd8ka955gUXa8mjqa3j00ezQAkz8Wd7L1Hn8nEVCuzYntInb8g1G8PB3j6jbX4UYMq1UngMzJnI8rgc3lE54-OZHvEEC7lmVXj9eHTB40f2RWOPjlorBYln1aTS7c-p_wiO2RNOrA7kmRphQSOc0UeJaygPurCnf1Rb67TwkZ50HA1l8eTOYYvvlwCQR7ZpkYQIG4WVmRXAjTwnAez9JZILcbTNSVbzVSyCXsJDd-x8x5-WRr99AUPX3fjklB0Hi9lPLdyzpLvm9Gzs2Vx1XB-jCvs1Sm7pk8JGZla7Rbk-bZhviEfnSZg7kAgCRgsKTOywsOD2TcHt8niaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGABtpcmRldRbeArnPKagi6V8fcMCNSgAVqAKXnMikTZyl9oR5GPs0sPdSqsR2H6Ra-tba076ly8kOq3P5cLv4WQXOEp4nSeYQOTVEUpdOl_wZi5k6Bhw9a8i74wl5d7ZNyqFU90XnCTaZgqqDA0CB4xaUv0MkuFNcOjnrwH5SDQYByqfsVaXFb5Y_mjGLcCo9H0ewI6LhelWK7rRkMlZWi0Ges2Ah-ulxIlJzAn7P-1Ft6zxudZhFqetKUcd6scLQEsfsxpx6HCn-ZipWQTu05O9Bz76AQXkgQiqIZLOe-K88j9cPRAgf9E6d82F-CGSMMvDbYC8K4ZQws_HtTcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjjiFfkD37YJ-9r444SvNCeaCLvGYsVpF0FXB6xTrTm_pHNONDcLmBCutBfcDXGnVAqbK4C4VBEbj-nPKQro34BVOjo4J4ja6R64SR_UwuZR58yZ-yZ8mUlmpZxiCpUopbfCaHVrsLvBgLBkC44-lZ9vl3k-C0DX1E6cZLhz5HitWkZ9uJS25UCwZA1y4hMvTX7FGZ69BNT3LX-Uep8ZEK90xCSDjjU0P2P2Q7h0FSWW1R4xKuMUmLnEN0QpM6sB8Ru3ZsYnlvDpAZpSNZdUAnbls3vctAze2ldEhha0cRvYhrDAc7jV4vPZevUxfDnELeMAw12-2lT875w7wZzwKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=HNd2UtviVvF6QHJQBRGQVyOvinrH8urRv-8mEMocxeG1mPm7FtCPPCWYU4MaPYMkFvJ3xjBCVe2BGzIparJKf7jjamP_M6UUVStgvjAt3cEGv76miDE0DW_boMUSSPVFBF3US2c3AVGgkyXKRRRxqjSEKAfdf0jLI1oztB0_exaHNXFJtlqhmbFw4pkeTJ3yD2BwXjXRc8hByrg0jm9zCipfqolpOzQX5V1xEDEE_Pyr5E9eepbIlyo-y6UFMrN8Nd8SYfyB5ibghB88mUxD_PE-F3nPthwSVlROBVhjZ5sn3RgeWcGV_E0ndfrQNBbwkuAwUJff_Xs_N79VYCUW9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=HNd2UtviVvF6QHJQBRGQVyOvinrH8urRv-8mEMocxeG1mPm7FtCPPCWYU4MaPYMkFvJ3xjBCVe2BGzIparJKf7jjamP_M6UUVStgvjAt3cEGv76miDE0DW_boMUSSPVFBF3US2c3AVGgkyXKRRRxqjSEKAfdf0jLI1oztB0_exaHNXFJtlqhmbFw4pkeTJ3yD2BwXjXRc8hByrg0jm9zCipfqolpOzQX5V1xEDEE_Pyr5E9eepbIlyo-y6UFMrN8Nd8SYfyB5ibghB88mUxD_PE-F3nPthwSVlROBVhjZ5sn3RgeWcGV_E0ndfrQNBbwkuAwUJff_Xs_N79VYCUW9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UC1Jok--6O0bZCzcB4qXtza5JrJlFIEcUtCkTA1ipaYtmh3kl6_xP4Lqr1YYpjacPtKN3GTNR_Zb64UUTAm9tJBKpAcGnbgPsWLW0kXd3jescoCZI_ECNekED4JomlzMxMwH3Hn_Y5Qq5E-4fxsZe8M309QanP81bNEj-UyMt6-g8L1Rt0gn7AA43dSeH4nYAsIHWy3N6W2lruG0SO08yyMoYz3RIomf7UWXn88J5UvUn1fr36NEdNmaeYcPp0U1cuBurZ0o8nmsc9HFwo0X_Vgd_yfsUtr8VkJjrKpWMTKAhdj8NAsf_XLv1YEpSPyLMCY_FBVwa-O1QM25EfJeXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=N22LUK6hLL51utmyE-unwGm6OEqhL0gw2zt8TtgfX2_rUav6Fj6vg1BabTlmg8asPU8b8jSn0HRR-u3CG1yIkdbR80tplaDIZhMZHMkCQcgQRZjBHQEzxfzFoyjwwHc_gB5zpT5N_9r9GGs_S6wXyXG3dw5g4sC8AiD1ipRxkgkDbu11LCe6C3gg6uz-d0b963FNijmiNG17mKBXjSvPwTm6NfqVPzx9-BZ_ssu58JoXSLbaGzOUGbEdrSGk3ws-ftliloQ7aUAUcbCiCTsqIbnziUCgl4C3-jrHWpM24zR0XK6VIMng49QQvJlu8GQSJi7t6mIe589w7xdjXsP3dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=N22LUK6hLL51utmyE-unwGm6OEqhL0gw2zt8TtgfX2_rUav6Fj6vg1BabTlmg8asPU8b8jSn0HRR-u3CG1yIkdbR80tplaDIZhMZHMkCQcgQRZjBHQEzxfzFoyjwwHc_gB5zpT5N_9r9GGs_S6wXyXG3dw5g4sC8AiD1ipRxkgkDbu11LCe6C3gg6uz-d0b963FNijmiNG17mKBXjSvPwTm6NfqVPzx9-BZ_ssu58JoXSLbaGzOUGbEdrSGk3ws-ftliloQ7aUAUcbCiCTsqIbnziUCgl4C3-jrHWpM24zR0XK6VIMng49QQvJlu8GQSJi7t6mIe589w7xdjXsP3dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=RC3OajRNwwy5gi2VFkItZA6LDVStUYAvTgTy8QmpMu-s51Xq-kqOxeRsJzVaD5w1zBDSRrIKd2yFUp7IBjMrXc0xIKk005KTgRy438xSjJCXIYVfdl3hQGB7JmjrJjbs53lcxr34Wkb7CRgy2_isM84nG3hic9NX4Ak2eWoLZi2Azv7Se409p6_VdCRVaZi7BnKI-gYPIywG0uDLGTLcr9l92Upgs6dUBaebDZARahEVfl8ZqhARGe7XA2EaQtJRoIEvjU4f2H6yDlg5fy9eU4KrqlJwOBD_3x2sidmjp_z00G3F-pKRqQbfxugBnKjTyNtkA2otXCzvQgQIU_b9vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=RC3OajRNwwy5gi2VFkItZA6LDVStUYAvTgTy8QmpMu-s51Xq-kqOxeRsJzVaD5w1zBDSRrIKd2yFUp7IBjMrXc0xIKk005KTgRy438xSjJCXIYVfdl3hQGB7JmjrJjbs53lcxr34Wkb7CRgy2_isM84nG3hic9NX4Ak2eWoLZi2Azv7Se409p6_VdCRVaZi7BnKI-gYPIywG0uDLGTLcr9l92Upgs6dUBaebDZARahEVfl8ZqhARGe7XA2EaQtJRoIEvjU4f2H6yDlg5fy9eU4KrqlJwOBD_3x2sidmjp_z00G3F-pKRqQbfxugBnKjTyNtkA2otXCzvQgQIU_b9vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=XaYGJW0KrCOhodoHSa6zSKa74rIzIaWp0cT_03e8YYgGFPiyzgCD_6x0sIgHG_AuYlx2Iee0WS-RY49wgnBlJ5cviQ7MjJrmadwLEc8CO65BiUhPP--XZCMsEeMkLHrAuYT3NxALCu-WRQrLRC_qb6qkzLMFs99DykVNbtJAht5sP3plT1VDrpFeAzlFLBv1sR0mBJlyXe2FFaJ5-tBjaVSWpkWRTB3SmFT88BtIG-bIfn8NrR8w4O14eUNyG0iMSC_9YOQ4sddu3h9dbmJtEMAvlO4nrj4kg9QBSEntsZuE4OaNv-BdeQh7NPK1ZGI2WIEInyMeLCHvlYQtx_Vizg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=XaYGJW0KrCOhodoHSa6zSKa74rIzIaWp0cT_03e8YYgGFPiyzgCD_6x0sIgHG_AuYlx2Iee0WS-RY49wgnBlJ5cviQ7MjJrmadwLEc8CO65BiUhPP--XZCMsEeMkLHrAuYT3NxALCu-WRQrLRC_qb6qkzLMFs99DykVNbtJAht5sP3plT1VDrpFeAzlFLBv1sR0mBJlyXe2FFaJ5-tBjaVSWpkWRTB3SmFT88BtIG-bIfn8NrR8w4O14eUNyG0iMSC_9YOQ4sddu3h9dbmJtEMAvlO4nrj4kg9QBSEntsZuE4OaNv-BdeQh7NPK1ZGI2WIEInyMeLCHvlYQtx_Vizg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=CBF6WotVV37iC7PbDXeu-sStOtCbZi7S8bagIZAzLm6pZPm9U2lDwbe7vf_W80yObebYiC0dXEyK8zfllntPAfC0i9jFBcP9hAMd6uyNIVaIrTw37Mi7k_DESLxNASHiTVZLaMXjqCU2QkMOZdCpZbiIX8dd18Xh7LRuDQDTd0TPDExMsJEF6uICAsJLCnq9Hi7XClERS3dHC7WpNaHjI_o2PX56ZHRtHpE5oouCimIwjTM39j03VgHqxPd-am3b229syHUSAbV4av7AuJNAN9l7b4h0P-3SbPUNfmp3oKhkDhMSqf1XJpqV25v0O4LIkuYo4s3JAdywIg6N3FJMODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=CBF6WotVV37iC7PbDXeu-sStOtCbZi7S8bagIZAzLm6pZPm9U2lDwbe7vf_W80yObebYiC0dXEyK8zfllntPAfC0i9jFBcP9hAMd6uyNIVaIrTw37Mi7k_DESLxNASHiTVZLaMXjqCU2QkMOZdCpZbiIX8dd18Xh7LRuDQDTd0TPDExMsJEF6uICAsJLCnq9Hi7XClERS3dHC7WpNaHjI_o2PX56ZHRtHpE5oouCimIwjTM39j03VgHqxPd-am3b229syHUSAbV4av7AuJNAN9l7b4h0P-3SbPUNfmp3oKhkDhMSqf1XJpqV25v0O4LIkuYo4s3JAdywIg6N3FJMODzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eenRNdcZgpBXr6qMVj_80wwW3WRMPDpIJtafp-_BwAIVTHnvQKT8RcKrNnfRhlAzaG2J_8z2FW2IYFbx2rPHES4kv9oHbbWWOcgHdz5bkAh-ZVfewtKth74VmXMn7hykCjV4BhdimUvbf4vX7fPBjpsj5zh_lHwTpYrcM1M-pphdE3gy10Mq6v04Np93VIkDfVdWYq_OXzAY1F5uCYyOfBshmZ9XtsvaCo5JUh_QKL7E9oeAiEemRz2ndZqfhVOOIXMWlkIkzzB8mzSPvRl7bjvpIf27kLPHFvXSPG2inqB33t6Q0SlBtXoAiQktMLI0ZhThmAQE5LgQuOlioTs_nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GXianbG7PAHB3zPX67C7uFnHCUtC0pi2XiO6TLb8N9JoWPWcdkX23qfwMdkqxN32kNJxipqXklAwfRSkVPlXdAAM-9OnFrtcdFJ2ERaHt2G2W4IPt4nFv1ZGXY9WVfTIDeq4gRSTsJW9cGNnsQkJCERjSisN10Ws2-4mBpLLtV2-QYF1gl2PBMdQ5vN8iHboWtTvF0Xd7vIrm-I1rdLR2_fZqxS8UA9J-KZUZNITEmwTNIGxeaWQUe1So9kLZFzuiTW6NU2haYLsu-4fl88c7i15EJNryveYs9K2UPbcdCV5Dq8UfJ6yMsXuiL7OPQhc6ZfsGcnr9l2tBi7X2svDYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N9gM0fXr_bJLeusenNOEcrfBwpQxSt095uHnYOFuxhRFLazpHBmoHK6z2yrTiA5OpsKH_53PMt_JKVFWijvVGpRTS1wGPjBH9CgNOMqeHUpXZIvIvhKEqswCd2bwcS0iRcacY0jQQ0sSUYThsKQM9cwPw3YRsH123BYUS14CA9qc6GyJ7sCI37GGaab3NSHXebR0aSCuZmDA2H5PoE2hwr6CbsEifWL7-ADvH_KvQiHHwW9zQrGoXK0GJ_83j1H-zTu_sSxJjSgxgkHMIHK0xJXvHPlsEZzVVFlryRqaFFLn6CrSetrkqRAruEaDQvx-W69QTq5z115DGb6hxXWbUw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=rS7AJtROk3Nam3Uu37FeVGHT63mrLnEFaz9cSy2MO3zGSzjNKWoY7MFUcKq1RD6t8_IQCvz52jPXQQEtafHvj1tV0FLJsDVWoxs4t6WnX8_MUVt6A4Df9hhSBgQX-HXgk7jnv09GNcwOiWMBOEeYuldS96hV7TSWtMa5DMkZROCchFjPPEqALP3B_m2QTYlskZNq7hO-lWHWagWArPn7pgayirvCSXwtZLiXrSFOSk2PMfguPWahchPGDpF0S3eCSomTJoKrsGhcGeO7rZ0PZ7CmAs4KImfczBNjPuldfKhWg5PtP7q5OKsUATeFHMFhjCCNq3oHH9LXHAgC3QCZxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=rS7AJtROk3Nam3Uu37FeVGHT63mrLnEFaz9cSy2MO3zGSzjNKWoY7MFUcKq1RD6t8_IQCvz52jPXQQEtafHvj1tV0FLJsDVWoxs4t6WnX8_MUVt6A4Df9hhSBgQX-HXgk7jnv09GNcwOiWMBOEeYuldS96hV7TSWtMa5DMkZROCchFjPPEqALP3B_m2QTYlskZNq7hO-lWHWagWArPn7pgayirvCSXwtZLiXrSFOSk2PMfguPWahchPGDpF0S3eCSomTJoKrsGhcGeO7rZ0PZ7CmAs4KImfczBNjPuldfKhWg5PtP7q5OKsUATeFHMFhjCCNq3oHH9LXHAgC3QCZxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_5EXqTZ_5OMp8HvyaRxy0Ao2MBBH1ioASBtTNSMHHEIRqtgXHv30Wb5C1edBOlemrXBnVZ-SZ1MMPKmZvgR6l0XYx-l430dB-BHEFFkROUHBXtjFR-sBpz9RAqnMVGB3Lv_bLu-fqTZPveWMOlJoOMqxbRIgUycMXxH0t8SBfJbMkqp3hpNig6gSpzVgvZhERcUU7ks_yBZg_PTbM0ukPbdO8A6uB77EVkJ_b4J2-sn5qi3JId5VBAYn0jnAuXYI76leOKr6ntV1EkPpzDWISwIllRJVkPEXFmjTcBOlcPKjdnvTaJGzlJ_280jeKyV5iAMDuu6kVMEVmOiFVv-kkXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_5EXqTZ_5OMp8HvyaRxy0Ao2MBBH1ioASBtTNSMHHEIRqtgXHv30Wb5C1edBOlemrXBnVZ-SZ1MMPKmZvgR6l0XYx-l430dB-BHEFFkROUHBXtjFR-sBpz9RAqnMVGB3Lv_bLu-fqTZPveWMOlJoOMqxbRIgUycMXxH0t8SBfJbMkqp3hpNig6gSpzVgvZhERcUU7ks_yBZg_PTbM0ukPbdO8A6uB77EVkJ_b4J2-sn5qi3JId5VBAYn0jnAuXYI76leOKr6ntV1EkPpzDWISwIllRJVkPEXFmjTcBOlcPKjdnvTaJGzlJ_280jeKyV5iAMDuu6kVMEVmOiFVv-kkXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=W1O6wwYIQ9G72lTj_fhWUUdUnCP_DMsojlcYP1PzV0Cu9O8o1SrGrZBFbtQs5P5RT4YAP49hcOIdPyoSszwwcFsLT5w1jAzNQeLubRc2cwp9kAWJCEoUGBVmcZjHikcnPlrkjxjD_vbYkyWnaWzh30_LuPUzTVinrCg_MMTGt-BgwLwnZhpdNRqDivBSN860JhYRkpZ7f1aoWdGd-VPmj16xN1SpDKDOzU6B9ud6hlSk3stvYWFa37PClpgHROeuzKEHBELLA73q7rWgO7rsBTzIOukmgvNk4Vg8Ep797cgu26uWbiznL8DWuMXpLOUrRHHpEOd0amVoai0zzHcXvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=W1O6wwYIQ9G72lTj_fhWUUdUnCP_DMsojlcYP1PzV0Cu9O8o1SrGrZBFbtQs5P5RT4YAP49hcOIdPyoSszwwcFsLT5w1jAzNQeLubRc2cwp9kAWJCEoUGBVmcZjHikcnPlrkjxjD_vbYkyWnaWzh30_LuPUzTVinrCg_MMTGt-BgwLwnZhpdNRqDivBSN860JhYRkpZ7f1aoWdGd-VPmj16xN1SpDKDOzU6B9ud6hlSk3stvYWFa37PClpgHROeuzKEHBELLA73q7rWgO7rsBTzIOukmgvNk4Vg8Ep797cgu26uWbiznL8DWuMXpLOUrRHHpEOd0amVoai0zzHcXvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c93KHz4rLIhVbHL3UBrHg4x2Oo_6tRWajeTQGiw0dN9G26YQg7dyZh3Hab47l-PS2ZK18bcHEmxxhjLicyqJ24v-XhVMU97oMRSVmghqQyBuW8dipf5VR21Y_eQWhwjl4z88BdFTdf2vkVRnDzafxilXc5-HiAybBsQNgmuX92Njh9fnlJ263wyIfqWUEo9FJtMg3m_GCuOGqydzZrFyT-YACX03bovHzEirn_xRvZCcdZBIvUGWxMtxMlfL82Vv_5rY57nIpoDRDpalf_HDpbRGnr-Cw71hWrsbn5j-_Hl6GUzq0T5cdkZk_0RbzLLNakY73enQGEdZJO-fygVfnA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTihcZ7EUyXZbcs_-8FT-N1LUaQGlKFrfXOBDkd57bAQf2sr51lYOMPy8CAcC05X86cJhekKpA4FNCxmDzHZ95spzKtCqsRlnLel2FDQnRVcUfsGNeoQ7q5w2HxPWKUps6Dgf7wx1rJwndYN7nrAwcSO83Vwc7vBdHuYb7brkiVnkeKYLoa3lWl2AS2bKisUSKxkPH7Lxm4zRCUc06uhsejVQ8wTgvvTXDe8A5hS069zGWAxY0d9pXy7q7N0PXOy109VXhHqas0JA_fuev0M8pDi1JwT7pPCmtvxynhGoJnQS2OXTtye2IGEZQYLj6FubYvMEw2_nsn5x-0ipizU8p40" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTihcZ7EUyXZbcs_-8FT-N1LUaQGlKFrfXOBDkd57bAQf2sr51lYOMPy8CAcC05X86cJhekKpA4FNCxmDzHZ95spzKtCqsRlnLel2FDQnRVcUfsGNeoQ7q5w2HxPWKUps6Dgf7wx1rJwndYN7nrAwcSO83Vwc7vBdHuYb7brkiVnkeKYLoa3lWl2AS2bKisUSKxkPH7Lxm4zRCUc06uhsejVQ8wTgvvTXDe8A5hS069zGWAxY0d9pXy7q7N0PXOy109VXhHqas0JA_fuev0M8pDi1JwT7pPCmtvxynhGoJnQS2OXTtye2IGEZQYLj6FubYvMEw2_nsn5x-0ipizU8p40" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJuHNDV0co2egF-i5s--ft9dgwi_HQCIq88vLsQfORe-ZlK5ss0j2WUN3djkGqZNMDRQBeLyrniZdsyK9cI9jEU5tksmD30LlOVlNo1dKzgKujYNN_0VUOnDA-s1fTvaK4dGnm-b_UDSHL4G6sdLxJ-_eg9OpkmI7GDx05LOpw6kWdaw4L8GuT28DWIP_X1VENOlBwzOcjea7tdp0zwjduU2SQOvMOpuBNWwoJ0HWa9HQq-DzHvdcA3Q5ozlCG0-ZwOeDb5psRdx5PKmo4-WWX2K2SWUVQkqqp2kBE6fDVN8fg3HThFSTJTyLbIrswnlVK1TDFssXwqrJChQAAHqqg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=e59kfr6ApDBxe1KItEZSQ1IjwE7amlVZALancKC8reGLrmNyfwGz67ER-oKPuCNgBrKXSry9iiq23TVwJmATZyN26vhuC1MGqjbi-huJOx6iuk-_WK4uzy8VPsHgKPEXGpzm48Sv0Z3plL0CXzolLS5U4CzGlajlffzn7G88NuSXltA2h252i8dV7NsSlQ1BvUwU2k78XLTVEkQSihoL6mnWDBLZlFEF6zc4MdUSudTDyZgUVyVaUkNM5U1tLW41D6z8TB7s7c1hkj634Q-jEOyO0pq6PAuqdVApvgWD6PKW4e9qOAXdMReKaD8sgQK4BIfI2DrnHmwhY_pphmaf4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=e59kfr6ApDBxe1KItEZSQ1IjwE7amlVZALancKC8reGLrmNyfwGz67ER-oKPuCNgBrKXSry9iiq23TVwJmATZyN26vhuC1MGqjbi-huJOx6iuk-_WK4uzy8VPsHgKPEXGpzm48Sv0Z3plL0CXzolLS5U4CzGlajlffzn7G88NuSXltA2h252i8dV7NsSlQ1BvUwU2k78XLTVEkQSihoL6mnWDBLZlFEF6zc4MdUSudTDyZgUVyVaUkNM5U1tLW41D6z8TB7s7c1hkj634Q-jEOyO0pq6PAuqdVApvgWD6PKW4e9qOAXdMReKaD8sgQK4BIfI2DrnHmwhY_pphmaf4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=mm1uT--83v-U2H6VaHaL_GDnhdCSC5T79Bw3m0KeUnzpLMWWtyrmGNWRVGKh_rNRyYbsV6cca4M2wZC0LHbIclr1XDbVZ8QQpyyTBh7RN-EEVk79ZKJSI39BnKPJpfYku4wSIkxRmYMpf6cmTiSLHkdObfb6A7JQDEf_5juZd2uh6rV2lFVXHuZET8Hw6YRsv6RowWwUTfYjJtb_pVoHoaLfme1B32gMe1X93uJavouwunNeezb-HbawcEyWWWd7VPieeD0_itGG0wIZpo5ldFNAYBHPas0Oby9c6drUZBTWAKtiZnlJbEnHNE50V3IvY26AmEg-Pn0nrJmiNSIQkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=mm1uT--83v-U2H6VaHaL_GDnhdCSC5T79Bw3m0KeUnzpLMWWtyrmGNWRVGKh_rNRyYbsV6cca4M2wZC0LHbIclr1XDbVZ8QQpyyTBh7RN-EEVk79ZKJSI39BnKPJpfYku4wSIkxRmYMpf6cmTiSLHkdObfb6A7JQDEf_5juZd2uh6rV2lFVXHuZET8Hw6YRsv6RowWwUTfYjJtb_pVoHoaLfme1B32gMe1X93uJavouwunNeezb-HbawcEyWWWd7VPieeD0_itGG0wIZpo5ldFNAYBHPas0Oby9c6drUZBTWAKtiZnlJbEnHNE50V3IvY26AmEg-Pn0nrJmiNSIQkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=BQkR8dtjGupR7NSV8fJ7siQn1JHDMv1gFbL3dAztrv3oBwDhnaFVyQUs3ESn4zFkHL4i4iTYjNAcU4s5Yqzqxu1hT9KszOfYz8ajrxSIZyLPO7yYvfWOEZznn3Q2eiKiF6h4ijPLsFki1G2JoqOyZ7jGiXDpIUhnt4UI7EwHy9cxyEa9lmIP8vIitoNTiirLwqSxAQ1ICFZ0EHDQC9xIhlBHEQnSqeMa40gVXFt0SSDLHEUqDtvYHw_NYBZEPUZt2Wxv4nxN2Hsp5pmVUrJX4NZG0O0jAVDMEJdwVEe7in_Lej--6rVk9Foy7O4XkEJrIPHg_FbZ9dwHbGxokshpiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=BQkR8dtjGupR7NSV8fJ7siQn1JHDMv1gFbL3dAztrv3oBwDhnaFVyQUs3ESn4zFkHL4i4iTYjNAcU4s5Yqzqxu1hT9KszOfYz8ajrxSIZyLPO7yYvfWOEZznn3Q2eiKiF6h4ijPLsFki1G2JoqOyZ7jGiXDpIUhnt4UI7EwHy9cxyEa9lmIP8vIitoNTiirLwqSxAQ1ICFZ0EHDQC9xIhlBHEQnSqeMa40gVXFt0SSDLHEUqDtvYHw_NYBZEPUZt2Wxv4nxN2Hsp5pmVUrJX4NZG0O0jAVDMEJdwVEe7in_Lej--6rVk9Foy7O4XkEJrIPHg_FbZ9dwHbGxokshpiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkXMCVQK8uyFsGdVtRv5jyQ_qiT6ZhwjCv-BczbfwWXuAgrThWZemY5mSrwSwc1ICOfw-NPNofHhTftXdNd2pn34b7LeF_GXcndw0BpaXd8mHAA6yhhIm50Zur2QZU6kUkvpM0_UDNjovcHLuZw-khm66ts1_VnXBYLVaCceivcxvB41GOpDwr7rjcbpIHdMwgUWJfAeU26ZT9VuMOr_M0A4UyBSip0t_UzJJAeO85Yu0Db7tmZfYQ_ZViL9NQgQCERdS4Vz3qG02ao98xUMB_VhlBFeKMfqSkY_31JbyGylksBUPdJeH_-jwn3NdmH5lIxOVXhC_xcFQKQ4ScQfQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9n3YBrK0ek9RGU7L2HRHVahhk86T13HEZoKSYOo2hnoWDPQR4cNBaK-ww3jIyuLtBLhnVxjASir_w4aKkHCuQtLVQxlGvKGPfHB7jzAjY178l4ssR1UDNtStJ1xizsAyLnBkgh1gf7bn__gZ5RaX2LL1LuO-IOkvzQeD-CrLKPkEIGkPK5gsrW2LnDhkH2c71RSDTDaMTE1b-NdoJSmBEAzg-wGS3pS2uBcpfe5LFlwEFsyC_Po72QNJ-IHRChyqinJpyaRgzDPxtmCc8qt9SVxPiHoAE2oTJVPe_ODq0YtNEk33EFLomHrTCEgfPXQ3MNtpW__h5sFCLcqcg5anw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Fgs9kfwvstVTQ_ZVstfyXbvwSQlI0o5kbakBYqUOqkgT-EPwfI4yEchdA-I2i89uPeOjVIbqsFn57ulkejGbR6URdeRHJlwZEVDx1rS8n-YzLxvv_hGHhZ-eJRC40AMoLvrldcHdy-g-jwK9ZwKOkigBPZ5gFLH1C7XpNMkd-2GyXSQFl0HlZ7NcfMf3cV8b1Y7GtCfqWvKI851LmR0-0DILXAuCytbCbwI0kBoSCoRdgzcZ1iizYUjwAFbHuINZoJBAT4VlKwyYq9fPxhOTCyOpTdDbci3GDTT3Vs13J23j_s6-JhZb0XSEtw6qO2uMQl2mUJaaRHQVCTbob2Ji_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Fgs9kfwvstVTQ_ZVstfyXbvwSQlI0o5kbakBYqUOqkgT-EPwfI4yEchdA-I2i89uPeOjVIbqsFn57ulkejGbR6URdeRHJlwZEVDx1rS8n-YzLxvv_hGHhZ-eJRC40AMoLvrldcHdy-g-jwK9ZwKOkigBPZ5gFLH1C7XpNMkd-2GyXSQFl0HlZ7NcfMf3cV8b1Y7GtCfqWvKI851LmR0-0DILXAuCytbCbwI0kBoSCoRdgzcZ1iizYUjwAFbHuINZoJBAT4VlKwyYq9fPxhOTCyOpTdDbci3GDTT3Vs13J23j_s6-JhZb0XSEtw6qO2uMQl2mUJaaRHQVCTbob2Ji_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDeV2KcF2cyxe23IsGdw2iZa_efrdu7hnHViBp-pJW6oBDQo8TRSSwdUOlm1hiIDvG4VkOcUCdfeEnRy9bpc0OeYdH-w6HlhXFkpd6YdpUEnOQgQIm3yxJi53gyEyj0MJhC6wbT40kQL6rPrrMXxthlEtIuxzfWnkV5N5yBc-OICQPCcaK25T_yJPBOxbE353J0pxL0HO_DsEb530uJX-8qqIYiRU8LtBqysKbAOh6jb6CfINKcOu4iozPWleV1elXN4hIrNj0B2FgsRQJfEK-T-1fe048i2DCkOvhMkSQDNnOI7MN1610WRus8QliY-_nU0jmQe5bGgJW_jvhfkfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raif5oN5OvtGuqhfu1flfWkFrXRfaDtd5Kj_Kcbe457FjD_tsa7_XJwMeibDQfTXFMagd5s5h5aKc7RcgRZa1ukhyBp3fmxsHt3--uG85KMv9pkY9JMhcZNJyQax6cnBjbxLdvbSu7DTATYdEq6HWQYmj8hyTRbDruutxjRiRI7_AAXWM2DJwk18wTWmFkt-cn9op77wy6vCEQk3HkEmPKiXZ82tFFzOXvAnPy6GWYRY-ZeN1qxG-sQndKS1dRXpfgwQuS-XVr7hF7tt_fVaOMSDJSYB3bWRxxD-RnrC_kCTv60oMJR3vtWSBlsm_aIwcj-or0GjrDO3ALHFoUobzQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=tfIRvw21mmt4JtYIESkvfZODF87ViAzt4SNa-WCj_WtZO3Ri0VF4kuYAAiTM8rWHfVR-GfX0iP4H8qDHeUtQxzqtoNxw8SUlOFHnRai5oKFoAi7y7rTGT5f3p-2dVKL0hmlMhdTPeCRW7FRUAtUP2RPy8bwCKuLio0wYShDAXfOCIdXtGzWSzwKsD3F97CBQJkrufet_jIx6RkvoTYcTJCK-SivZ58D3WmfRqw_yMThq8oVE-HCl6-zuZn9SvFqcq7T1GBRFhb41MiIXVb9g4L5NolIU_p4-EuxlYhckmppdLDCGsuAa0K1NCEi4PeNfY7Fns_2PhxwW0S-z8i8_ZQvL7njtaJX213spr_jjuaR89z_jZy_oos_Tmw4xtJob75p6DYb9_64OWc-fXx-K17FzU9Xn0uohLwQq6uPqLHJXG6Avdqk86qejvED8s5zVsKv2gvJqvgfcteXmyNFneR1zUWseSBELJUiGGq4ojyOiTvcBst8MY3iUexrqlxgklKBS_NQA2lfvShtVqFLmtuHUf9omVsOCymRiZ9M034u8MXefajawB8GKoR59bar5azWhM_bMqrHDfLfnpEoYJleoz8dRLYTsvA0v2gMOLjZ-X96n4yBll1UznDXBkObwNf4MdfxPeyot1zo5nuZNj7QPxE0ZmKesHgfzx7Egvq0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=tfIRvw21mmt4JtYIESkvfZODF87ViAzt4SNa-WCj_WtZO3Ri0VF4kuYAAiTM8rWHfVR-GfX0iP4H8qDHeUtQxzqtoNxw8SUlOFHnRai5oKFoAi7y7rTGT5f3p-2dVKL0hmlMhdTPeCRW7FRUAtUP2RPy8bwCKuLio0wYShDAXfOCIdXtGzWSzwKsD3F97CBQJkrufet_jIx6RkvoTYcTJCK-SivZ58D3WmfRqw_yMThq8oVE-HCl6-zuZn9SvFqcq7T1GBRFhb41MiIXVb9g4L5NolIU_p4-EuxlYhckmppdLDCGsuAa0K1NCEi4PeNfY7Fns_2PhxwW0S-z8i8_ZQvL7njtaJX213spr_jjuaR89z_jZy_oos_Tmw4xtJob75p6DYb9_64OWc-fXx-K17FzU9Xn0uohLwQq6uPqLHJXG6Avdqk86qejvED8s5zVsKv2gvJqvgfcteXmyNFneR1zUWseSBELJUiGGq4ojyOiTvcBst8MY3iUexrqlxgklKBS_NQA2lfvShtVqFLmtuHUf9omVsOCymRiZ9M034u8MXefajawB8GKoR59bar5azWhM_bMqrHDfLfnpEoYJleoz8dRLYTsvA0v2gMOLjZ-X96n4yBll1UznDXBkObwNf4MdfxPeyot1zo5nuZNj7QPxE0ZmKesHgfzx7Egvq0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6zE5izrWqyduBdDf0o6W2J8SqjNMzIHd7YOSCWRxJJSRFkNaTJrXPuqCi_9UW6bDOV3M-LFN5hK9u77pfzkkjI405izR6KFIZ5s3CIjKxvK6zCOnhRNn-wQ49aKz8y_ChBGoRqRa2PAjZSBU-Oy1k-bLHXMiYA1RixuUPH45KJw-S722_4YyzhhFGNitPJzd-P_W84mkEd_QdMrOy7hmrnpwNKWwhpue1tsBegdWDxOa7d5MQFwTstVdA8T4S-ZFRJ5JGmd8_BZfvNUkroFreOg9xFGSoXmYCY4UEicWh0d5N0oD0-AIArpsB_yeiHkdjloKD055DVfeQjLSyWvsty0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6zE5izrWqyduBdDf0o6W2J8SqjNMzIHd7YOSCWRxJJSRFkNaTJrXPuqCi_9UW6bDOV3M-LFN5hK9u77pfzkkjI405izR6KFIZ5s3CIjKxvK6zCOnhRNn-wQ49aKz8y_ChBGoRqRa2PAjZSBU-Oy1k-bLHXMiYA1RixuUPH45KJw-S722_4YyzhhFGNitPJzd-P_W84mkEd_QdMrOy7hmrnpwNKWwhpue1tsBegdWDxOa7d5MQFwTstVdA8T4S-ZFRJ5JGmd8_BZfvNUkroFreOg9xFGSoXmYCY4UEicWh0d5N0oD0-AIArpsB_yeiHkdjloKD055DVfeQjLSyWvsty0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=ENKM8c3k7v8F9d1uxljwq1jG48qPHAUP0UYyOkaQ2J745Da7qNHl5OATgy_amGd4b3XnJ-lhgg2DvEYlm58zyZrE13CpOOZQKhHXFhc02aQ6O3Nv-scsYt6CFziuAdFx2JgsMTGjK6rrK9MXrBzu94ljaAZiGq2XLMZzKk82h3JGAlvbtdjVSAdePgArsrfXEbPuj6P0Hx9tpOZewayqO9ooPxc8JugII9M8k-aSkOPDKkUX4rAPHHArLFJauBiUr_zsv2zwW-ObMg2Rf07CO6Gnf-ykk4rV5BC1UBKwxBM6oi76y8ZOSITCuaLcwya-V44n6lx4GN_tHmEhgaE1MYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=ENKM8c3k7v8F9d1uxljwq1jG48qPHAUP0UYyOkaQ2J745Da7qNHl5OATgy_amGd4b3XnJ-lhgg2DvEYlm58zyZrE13CpOOZQKhHXFhc02aQ6O3Nv-scsYt6CFziuAdFx2JgsMTGjK6rrK9MXrBzu94ljaAZiGq2XLMZzKk82h3JGAlvbtdjVSAdePgArsrfXEbPuj6P0Hx9tpOZewayqO9ooPxc8JugII9M8k-aSkOPDKkUX4rAPHHArLFJauBiUr_zsv2zwW-ObMg2Rf07CO6Gnf-ykk4rV5BC1UBKwxBM6oi76y8ZOSITCuaLcwya-V44n6lx4GN_tHmEhgaE1MYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=VOBQLVn1DZs0zJi3heH1GT7lH5EnQj-2u_UOjx2WRcm4Y2v075h15clnpbdDM_VblxXM1LWPFI8H3O1ko5SRdhVmMQao196zKBOHIkSV7KhFclNLUw5tjkCJanuwNCIptsaVQ6Mvb_BAxrs_kcWtB8KlQ2OjfDqf5lPgqlXjALVkC0rz3k3OwmKdtNDB8I6zeV0-2FkVZiEtD7TFPxWpOZMpygFiSLKyAWWIdqDQP9w3PEi0Mrb88luxSeCxpf9utYjxqqDVTFLN_9jaA-1XgF_ajpX6eg8GZvFFc0ffgDOnFzfxcwoW7oICKo1LL_Zky2neXhiRGKlF31oAkL3Dkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=VOBQLVn1DZs0zJi3heH1GT7lH5EnQj-2u_UOjx2WRcm4Y2v075h15clnpbdDM_VblxXM1LWPFI8H3O1ko5SRdhVmMQao196zKBOHIkSV7KhFclNLUw5tjkCJanuwNCIptsaVQ6Mvb_BAxrs_kcWtB8KlQ2OjfDqf5lPgqlXjALVkC0rz3k3OwmKdtNDB8I6zeV0-2FkVZiEtD7TFPxWpOZMpygFiSLKyAWWIdqDQP9w3PEi0Mrb88luxSeCxpf9utYjxqqDVTFLN_9jaA-1XgF_ajpX6eg8GZvFFc0ffgDOnFzfxcwoW7oICKo1LL_Zky2neXhiRGKlF31oAkL3Dkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqlXuIlMAvzvr9vJoE-rIirabUdHlkr3w1EZUa2BXbT-7uUsI71L9KwxOn6Rp8d_tAAIxJHXN1yYgi8q41YY3mP0-7LoibBR_kuh5g5Y_umFqPuNsjOFpQARCPotalnQd217AG33j5dCPBOeJyNwiKKVjoCZ9topL-15TbgJDHzS5KVWiPyQ72WWaS4LND5CwPtiP-ZMAyQArholq4fSn9bl6BGtG3j37Ja_wenqR2Fv6-HW7tye_Q93a2fksc6Fku9riyYPg_cENFDbpHjyJWg_xnXV7jVZKjNGqK1a3ug0ZAOp_14JhmZK8nR-pJdQZDkb70mTOOMK4vzpptC7dA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxUZIHkz1jCQbt9oBSNWIjNanGKjnl-MWXW1B8ateR1T19b_WqoRBKLSpFjbQbLrOBoRUA4WX6tcge676uh7_ndOA_gexCkH5l84vx80STNqsgDl48KJfjy6BBp6tBZ_3SZodlWUbscc5rUSjk3wh6b3prfI8LzdjOSE9846pPg94D0bpZ-XFjb2NjDcEnzBJeSQ8K34ACKPXtOVaKJ1SJXko5a74RGKv8JJXK8FY8Xb2KL8U5I0Rd2pCFTivbC_dtqmmdUi94kG-K2ofnDhUnUf4HYePJC4pBr46EOwr1HDVYLf_J9515J8WlL_lUxoJ9OCubOfJA64pDKfj32sGw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rcrOU4yG3qIXtZT4sD--aBu9TLKfpwAqOMNKuRW51fwguYl-_q0at6tGbVZhHBZCYOkZ0p5D6I4QAzR4ZFPmPLO7di_J7nywuafiVrc4swPoERBB2828rG8ezeoBtudsqi4MQFqsNTtSf4ddS75mXXvs2Mj0aWO5KYFL_1G4WuwgpLWv-pUzMU1dvkKTiR4hmOha9zUCmsBHpP7f8TTvCfxJjyBDTZIoCApEmDmz-Yv6qIcYYE-L5f1KS5LROgyfa7O7vAhwS7pkNWy81M-F_LmQLYB4xeFaTyN0hYlnCD53PNM8M4nWZD7I-zickKaiYXCbASnGuW5LzYOx0eKq7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQn73HoXZuu2d55v_8JhCbC1DZc6Ax-cToUX3oxF2D0j11W2O0d3esIvzrRzxT1ckJ5WNfTNe7gkMRjKyO0oSS12y-geF3jcur7miyG-rpQwsJ8N7evqhTN3BlRGT6WfSHG6_zWyFwpMHuy6KD9V2pw0eBV2MQFZk46izC4iWOtRzvgkLEl_V9NbfqoEZlyICSVupODTaWvH8kE5RjiHwIoHBwrGGDs_bb7hPwOOwtEV2i0vRtAUBzHqN9jk7O4v_kZGyHP22Of_P25Ud9CzBnopLl5V6-8q539WNanPJriZwByXWbplmDjS3ZsQs4lwzcHnxLbhGq9JPK4xGArtMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLN8jpArh7nuaOV_Wm245OKGqpayZQ5kEYx7DQTtEE4Ff_a4hnotxPYgyU2L5BVvtlrHLT6bha0GuGm7_o4tUunqeGvVBdCV_hZPlUNaAhkpPLEi5d8itIi23HqIqIDPJiLhajnUTATUS6-HStrjRTjlbEBJ1_Bt-AjX9lzslLS1eyAvcPFtA5Gk8-Ftjvy0o9oSqFg83ZB80fQ1Q4r1YRMKR48Umrb1g23umHacVl-74FCr5ejiAlPP2RijIDd_XSv7cPftRT0kxhIAKe9AihbCcL-Ae7Eeoix9eea9dYq15Idwf9Jl86XNaKvThadu4IWPKeOQtcTOQsH35Fs0zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=LEXhMhR5jB8pTu69ZY4iOFGPO6GZqEyL4aiXp89JcO0PeOd7DvmeHLswHHgn-yu_yQfTwPyso-OZ0urdhyHXY3Xaa5IcIgFzqRFmcWsHvlzjKiCt-25Fs_2j66KeKW6901kTJxvHv-RENJUX5poWuJ2l4HPYZPanPvKVQqUYVwQ-1pBU7nyTVe5BWoyanQ3u3SPckmW2wQjmcv_cp-GzLYLBfglwrW1cUBxi0ap2NAnozkRj8YlgHRqF-9jaxirFLBZ1RxuFk-CU5L-GxK09c55ILChdspiNqQ9Dr8vISJA0Gn1UtCEl7i9jfC-2FS-cgFsDSSXYi1vWrv73UIC58A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=LEXhMhR5jB8pTu69ZY4iOFGPO6GZqEyL4aiXp89JcO0PeOd7DvmeHLswHHgn-yu_yQfTwPyso-OZ0urdhyHXY3Xaa5IcIgFzqRFmcWsHvlzjKiCt-25Fs_2j66KeKW6901kTJxvHv-RENJUX5poWuJ2l4HPYZPanPvKVQqUYVwQ-1pBU7nyTVe5BWoyanQ3u3SPckmW2wQjmcv_cp-GzLYLBfglwrW1cUBxi0ap2NAnozkRj8YlgHRqF-9jaxirFLBZ1RxuFk-CU5L-GxK09c55ILChdspiNqQ9Dr8vISJA0Gn1UtCEl7i9jfC-2FS-cgFsDSSXYi1vWrv73UIC58A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=E28xFiB86TRC2zK3wXY9yRTL9aZGVt-JUj2HPCsByDDTvT0S_dG8_yXASFyrQNKVg8BmpZnCH3D9T6Y7o0uV4gTiYkuJvjsfC8xleALzd_O4oBK7SCHF8dn-Nycvvhms-uaDvTMw_PqCQrQS7DJi7sRWgGMCvKYY2Ga7xD7MUfr_kIo9baEfma-_1tuFOPc3Gvnpv7Ix_mQhDspl2JFfyV9N6cvua79_TlmpG_kTE8cSpVAI9ulTu6GamHB3NjpWrh1xzwMc_11MEM4s7fFaER5NyqKWcWlVq1m_Uo4ciJGEDsLA2douMmPGWtOdSejaZaFedDrRPkLRwA5UbtZ_vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=E28xFiB86TRC2zK3wXY9yRTL9aZGVt-JUj2HPCsByDDTvT0S_dG8_yXASFyrQNKVg8BmpZnCH3D9T6Y7o0uV4gTiYkuJvjsfC8xleALzd_O4oBK7SCHF8dn-Nycvvhms-uaDvTMw_PqCQrQS7DJi7sRWgGMCvKYY2Ga7xD7MUfr_kIo9baEfma-_1tuFOPc3Gvnpv7Ix_mQhDspl2JFfyV9N6cvua79_TlmpG_kTE8cSpVAI9ulTu6GamHB3NjpWrh1xzwMc_11MEM4s7fFaER5NyqKWcWlVq1m_Uo4ciJGEDsLA2douMmPGWtOdSejaZaFedDrRPkLRwA5UbtZ_vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD57jo1d1hyhojohCYpYYxwVLXFADrcwCdvO13KGCYnQWiPM0Y8qSAnNvGWqNx64zIPletDO0hNeYsF02CJpfK2fmcHLD8gfYVlNmQgwj1zoIOpvLgGOUQNqMyVv9EOHlWgleWaiJoVYYk9ZhJIskpvVlVKbGRkxV-J0r7mNrGJukOxP4ezNz0kN8stC596kt44-VYq80iwyh8lGpfPiED5C7UXwD4iMypbK8tSiHBc0FcRk2EJNcbWP7LHDVsfV8TI8xIBH7L90PcBB5kw2HaXDQIg6kSAXEj8hWxAgwC3QBI2BGjMQU0OLlgoTDOjB5Smp4Ak7aQ6cvNHj-lXu0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NG-zv95N42Q8vGdWt9O-ID9rivCj59iDqv02pmGOP5rQ8MMjLzYloSt8pgNxJjurzPjI9WyfQ2KsmxDPJ2Xogm4yIFJpKWC1UVWajtFPI7Ynjh4fwF_quK61EQH2Zrs1MD-kHZh91NOUVqfW3zw_jOiaoEXJEGMXJJqyXOk4Oh0E2YwrzVng4pIMYeRP4zl7Ae5HREpaGrKm4q0ukvCnMZ-Cl2Lc77QazKUPlUtlVi-_-eEYw8-l_FgJxkLDXpshIv5hDp3aovjnus71ToqN9h-7TZrU6Lq2Djayg669DmNQqrvleulrR5l9VHNhPgjvnLKkhuWX41FwavznN8-gMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=gVEgCpOruImDpgLn6JXg4dcDZYVWgBOY3upx_8w7TQiO_IMe4mZYgzzilHRxrFi_KfgMeyK_NpZF_YOi0PIV1DW2MA-cfo29ZKzjilu6zvrAq5IXs2NJqG38NXH3zdkfaUfR6rJjHlMEc6GTbqE_peQqrK6_Fb4JwOwuxMCA0V0SFNU7gKjqzmaO7S_OblPYYw7Z2g5E10BL3TuJtTutmjCWRLCnXsH2ci9WcvFg-7W6ZbSGfYOZzNwg3oe08PL0uTJiTD-PZU0ajMA7N9y9IPsEoRpc8zheoa8SGFX3Rrn_lIbSHpEzIK--xEojtkEsKMeA66oVH5VYdOZYpqFGmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=gVEgCpOruImDpgLn6JXg4dcDZYVWgBOY3upx_8w7TQiO_IMe4mZYgzzilHRxrFi_KfgMeyK_NpZF_YOi0PIV1DW2MA-cfo29ZKzjilu6zvrAq5IXs2NJqG38NXH3zdkfaUfR6rJjHlMEc6GTbqE_peQqrK6_Fb4JwOwuxMCA0V0SFNU7gKjqzmaO7S_OblPYYw7Z2g5E10BL3TuJtTutmjCWRLCnXsH2ci9WcvFg-7W6ZbSGfYOZzNwg3oe08PL0uTJiTD-PZU0ajMA7N9y9IPsEoRpc8zheoa8SGFX3Rrn_lIbSHpEzIK--xEojtkEsKMeA66oVH5VYdOZYpqFGmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ZoAQPF3u38x1fjA0TrLiRKB5nBBX6vG1G6olT1KQAiWMv6u7kJ-MpN5tFRH-5xuQbV8k-eBAZ2O1_pXO8ozBnMwUO1nhTCiktWOfxyo-DIAGWvI-npRdI-fGpY9SoIFReZutg2bdbb8VvAMDH8jE6U65B8kXxTreO8pGNScpWu2GEinftt5tKbJLusxzs-tbhkCjGC6GVq3nf9Mip19u4zANDCV1j3gvDndGNMBUTBLTSW4USuB4JgYqeRVpBQEaz2f0qRaQnhMAnFGSH3oEDMf0Kw_AsqyDdrL7Yveu5E17qhgAtVBHMw9TciqNU6M5kwFSuk4qNSIZAk-aeLdaZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ZoAQPF3u38x1fjA0TrLiRKB5nBBX6vG1G6olT1KQAiWMv6u7kJ-MpN5tFRH-5xuQbV8k-eBAZ2O1_pXO8ozBnMwUO1nhTCiktWOfxyo-DIAGWvI-npRdI-fGpY9SoIFReZutg2bdbb8VvAMDH8jE6U65B8kXxTreO8pGNScpWu2GEinftt5tKbJLusxzs-tbhkCjGC6GVq3nf9Mip19u4zANDCV1j3gvDndGNMBUTBLTSW4USuB4JgYqeRVpBQEaz2f0qRaQnhMAnFGSH3oEDMf0Kw_AsqyDdrL7Yveu5E17qhgAtVBHMw9TciqNU6M5kwFSuk4qNSIZAk-aeLdaZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_v5P6-SdfLDe5y3MVprgVT9VRVGStoSNEKeZ2NdGhr9FSfsBgGTCAXSq-rq5VD2pM01p2xO8qSqyxlCsa5RWUE9H-n6bPy2tirYjo0OFVCeRzeIZ_08OZ5iknXLjO8soPGL8S1y30LnslJX4kTdz7Vqh9W8HnYnlQsuA0DAyd_8ltDqZt3AMDO8zcR8riBIXe_tYYPfoiCl6TL5cTb9Yy-FjaXsMwEYwaxtfdtkYZ_64cmAhITftFRjaLStU5L1WQ1U0ZIJkg17ePW2bCEFMOw64oXTF7bSA4Owma0DxqbHPZ7t6RNylnZVOLTsMz5HCyzyqpT3cFL1Gm52Lwl1Ug.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QTcYYXyRU6eTRiJC6tKLXmBy14xmJGryliXFsMk1lNEXYliiOREqV7hBebZOjPFhjsulSAn07uelwG-bxlRuqUxRt0ZtBMF2tf2R29IQY1WiJvEHZmLPgKUQ_odr7BS7bU2dLBV89HTufJC-d6ooUUjV4Eo5GuoPZUrRwTyX0_wXU1a7uq4BYmv6_7N0HJGHs81OJNVqtdLachEPk_QgEUz0GHc3Fh7oRiSFu2ZoxFFiTb_JS5XuxcFcgqtm2b1vsjmUPCoBWM7U5kOMXRy8-I0vJ0LI5S-iMCvs1NlMfZphyNVutoNWHupJy2TnAO-iJHA3i1g8idupzjIXL_dvNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qTb5vOHsGNaf1UVT-EA9rHwLxzJsf_3ti2u0rYGw5aCJcdZw9Qbk8djr5oxxi2qIBYkgQ9l5e-fRL4ztksoTociCEqaPfCtjwed48MqFbAilu6ajLdK0fnbM7Iqk6217Za6rjWcT_E5u-DOjELcNUcan1bWKPS_kcSw1Cn8oxzP1pyj8aDs658W35tEmRvV-ALqjeBSncbZitpIP9289t0s-O5QcbeBy-r31j3nSW2BibbDR1F1jyYCJKBMEVny2g6wZhBpaoJ6_WwIx6CGqjmmqtxjuxIhNduUdjy6iL4Nq7WOS1tNEULmnt3eOU1U20Q0IOe7Wc9bNXgTQAWFOHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=TupzjVZykCE2W1le470LHyVJMNpCDgLXYRWyX_04eCx_C3OWENeE1NMAikzzwEqmGMvEucN599k1kt_Hx2Q6M_rEMPtcryKZxfpqPyOTdu1fU6oBY2-6LEeghAc5C_y2o_JcqXo2iUZR7AR-k3zrOD6kRCuK9sjZhpyMkuITP1-k6jBYXq63KeoAowpOk8QX3wyATHdOxukDetElQjPMKuGOBQBGrqxfX5YU94Ya6DQj4YzSF-xJqkr-Sf4AhkgP37EuY_VLKJzsidXRcN_rxTzq6CbnE1y_Tzk8cTQ3sxNRdGTIZWwJu7zk9JFUJBgXKema9nT1RIJQ-8we6qcgdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=TupzjVZykCE2W1le470LHyVJMNpCDgLXYRWyX_04eCx_C3OWENeE1NMAikzzwEqmGMvEucN599k1kt_Hx2Q6M_rEMPtcryKZxfpqPyOTdu1fU6oBY2-6LEeghAc5C_y2o_JcqXo2iUZR7AR-k3zrOD6kRCuK9sjZhpyMkuITP1-k6jBYXq63KeoAowpOk8QX3wyATHdOxukDetElQjPMKuGOBQBGrqxfX5YU94Ya6DQj4YzSF-xJqkr-Sf4AhkgP37EuY_VLKJzsidXRcN_rxTzq6CbnE1y_Tzk8cTQ3sxNRdGTIZWwJu7zk9JFUJBgXKema9nT1RIJQ-8we6qcgdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pTlg5Wf54KedNgRVqnh6_qOHzptNf5FBrUhcRYNHew5xt61HZ00Spk_VJiQdv8C-gfdKF8t4QBSqWyWYc38c97IJE0jmEPE8EV4oiBZKM-4YUsOu2cYfdWRsAbeaLOuynRFVFA5yMXQpJ2EukapDG-reIGko7Gbx2_2Uq3r99lGayEXXvNm4t6awR5KGrKbObi2Vb8WNWsDNuBirpFTZY97QKtwu7-LHcbiUsSziOJrpeIOnUgbOjwMaATxUKY1_wTRuAGlzibo0ziyPYMtFQb6U5scDVB1WxBbYazP6Cif39XUJL4cWGf8oHyq8niyKtCOHCfpa015Uku07NNHPqw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BxHXCuDoE8xtGeewLw9HicyYAqBnNP-CTchjB-PGSf6XzjzqPZx245RsLN3_oQLvOGXXMe2zjKOxPFB83R5y0r3Jz1-w0z6-3Wufy7K_xj0KJgLzcUIWbbC9tsFP1-gUHKFkW1exeHU6uheF9feSYlUuEB8-paFS8mK_4zt7CyIZMnfE9LJghotP4qr7OyUXn_2boqww0BDfzn27ekvudIf8jflDDO7E93_mh4pymVDLF_fZwjzCtqncPpX0MjLIJ-SLIftlPJKmVSsguW9EU7dsT-cmCkic1Ua_UiGHy6sRP6uiYCmKbkmBy3YQdd8R8jR3za5Qjgd4xZvmd78NBQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIJ_4J4sa4M0PJRxTZUFSaMidZPMPaWRGEs_Szy2f8eT9nFalksXjz8nW6HCuG6ksvi4xyPMruENIglkg8aEZLoa90XXJN8ZVZcSBtfDDVKPXHnGi14dmFGre5NOeGVlrXqHM5SuDm1q3eQ4FMzdPFYvuOaE9kT8_sEVS05OfBFkZNGSXXqjff6rLc0_lz76x9A5YU0zUeqE8xxGpQ4YWHF6vAIucAyQy_oW5LL0HoE3S6bCHPKzFyDGuNcF8xP2IEIg8CzhRjWI8dLiiNjvFdaohan3ItfRi6s_JQTdEjBlEta4tb6X9r5baB0oVoU1lYWAo8hGBiF34WlcBHKUVg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Ew8FVqt9Z-tLyo8OquM-1lGWvGX6Nwm28VCxpg9VLV7A_Om20dtuMMcFacBh70_bMLllDjJcCuq1M3LsWR73Ds_XsoF8xK-AL1GzI5TjDsgtYxjESPouHc7OqVJmYxTmMRNtJMLNrG1HTzlAL1JPdr8RnjmHsLATJzrX95hFc2JIWN2ObZPUlybNR656BgQxzwsuEwsqo3jjNEF2WxEGXMgOpTKYP21CMprErnlyNIX_d5BoRMBRY1W9qLZm73LLB3G9Ak5mIRsyI6mosTxthdnJYv4UzU7lEx5r2unlQeOIJ9qRL259_BjIWsyF_fJdGYUomZ7WI_cvmzO-s9KIHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=Ew8FVqt9Z-tLyo8OquM-1lGWvGX6Nwm28VCxpg9VLV7A_Om20dtuMMcFacBh70_bMLllDjJcCuq1M3LsWR73Ds_XsoF8xK-AL1GzI5TjDsgtYxjESPouHc7OqVJmYxTmMRNtJMLNrG1HTzlAL1JPdr8RnjmHsLATJzrX95hFc2JIWN2ObZPUlybNR656BgQxzwsuEwsqo3jjNEF2WxEGXMgOpTKYP21CMprErnlyNIX_d5BoRMBRY1W9qLZm73LLB3G9Ak5mIRsyI6mosTxthdnJYv4UzU7lEx5r2unlQeOIJ9qRL259_BjIWsyF_fJdGYUomZ7WI_cvmzO-s9KIHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ex2axMfAk0VPGOrPSLidJsNctZqPrxOOkQNpmOIvBzWTjJVPNMf0PL4wWTbXjsvkHrRhJycTExj5Dk7_s7J4wBo61OrZ2lxNz13IHeCzwoH9PjuKCbpUuV4P0tCxWkxKmkyQiXC31zSMnNTCei22-oY9lr-YnTbGa6XX1RcaLDKTmU-lVdQ7Un2N56Pd4ejHIxEAeKm2EbCMgKxkfSKl4-QpwTK5DntpgbcJULxJkppb5SyYQmW9P_3qMqR3Rrd3leH5PZscmVMimJ2Qz2Cb1QQXYaFVVwuwyxvVLEbZZoSBB94nQXHZzo0XCbqQl3IGYhPb7nPnWYRmK-LnjHAkVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFSdtY07WPc-IJQN33x56ydzwrCrO2Q9H-jzPquYi7L0x98iovzbGQlpCSgisXRArKSrz3MZkJKejMHB1u_6apXZM7-6DmfRla12BWJKEeJs5Nt2B1Fl-PD56VM3ztZHzhIAZaaSai1EODv0g8f67jD38ZyE1RstyorFte2aY8EfoT_7Edp1sEMcgrNNj9b_ZSSBXZv0lBgvhAlmn4SQ_WMKs1UTZBp5262wIOThYJLbcZTCMFjXfKNQx75pOiiTZ4LUYSebnwVOOy-7GroMViISjKIb5FmOgxVT6vIzCn59b_8niPjdGnmyFn__wGPqSTrgaBprLS9eXBt6KKO4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vawwxaSTgruLCmUXDBKnv5SsjOiBYjuo3w1VIbLpHmmT1pUveL4nVySJ0MzvqlvqrN13s69dEg5CVffQGMw_AuAtwzsm6x5lgvDv7vMdpUjirTR4UAVaVpoY1nFmaC7LsVWnGKrufBidhQJidyvOfS2H0S7sDEClI_-3ZYSHxevHqKZO4w1WDEnEa06ksZNDPjlWp01q9wx5A01FLDiLl_3SDze9STzYgn8wYQiRgUtXHZxGIZ6Q5b0aaNXYY1EySIM7sXGjplJV5-mojJHmEzKubq6g1Ofp8lrRan4RvaSNF5TNmVUj1Lw8W8JvH58NJLonnZ-7aO51m22NaKv3Pg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=WPTtj0XuYi0e3sgfH-w54ZHE9U6WcfqRHWaopWvzZeosrUolakFEg8IIh54Qt26xJNsRX9E5E1EJAvYPfi2dA3sc6gGfhiTlYwtKHAUUw6cPsK49SwAYz4xg3ATRUiV21SfN8JcV90TuuvNoPaiRBM7IXdC5A-QguNMPaN1IW4C_8SCHuiBwvDl6v2ammOaS2OZGQxLfJG-1-Qqo-AkDtxIxNCbUJ5gWnxt0Ujx0OScndMz99KBfOe-XlYtmWyYgBhFPRx0eHFXgEcXhtzvw0E1k-7HsOJkjPaqoVTobSC0VEE02u46EWdmtFyOL881biR8LFA6MARl_m1N3up0emA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=WPTtj0XuYi0e3sgfH-w54ZHE9U6WcfqRHWaopWvzZeosrUolakFEg8IIh54Qt26xJNsRX9E5E1EJAvYPfi2dA3sc6gGfhiTlYwtKHAUUw6cPsK49SwAYz4xg3ATRUiV21SfN8JcV90TuuvNoPaiRBM7IXdC5A-QguNMPaN1IW4C_8SCHuiBwvDl6v2ammOaS2OZGQxLfJG-1-Qqo-AkDtxIxNCbUJ5gWnxt0Ujx0OScndMz99KBfOe-XlYtmWyYgBhFPRx0eHFXgEcXhtzvw0E1k-7HsOJkjPaqoVTobSC0VEE02u46EWdmtFyOL881biR8LFA6MARl_m1N3up0emA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=gf0S8Ypjvp6q16YKnlpuC_3GZVv_D6DtlJjPEvUwVzNrQORFY2_mDEclCcirMu4zxtISuQMz7Ug2cqGnhCqjmCgURBBkqzwUsBHg0rPXvAbMtjh7S6nwdjBHRjyV_qIny3G6h_gKWVjMbLm7tgyvLiyoJ0pOS_kqaeO4YnuhMReeXFUbJlYBtvU0RQLIVQmgXwdJ8cYRha5vp9CZF0-PKKCY8j0BTFfXH1FkxZnvIK88U93kOQgdYn3p2z0Htg0CWGzO9G34NBqWkarC1NHBpwja_lTK1c-gguDGdxgvb5PF6-IwhdTurNd8lhdXyKiFndcwdDZe8RB1RP-XkSgIeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=gf0S8Ypjvp6q16YKnlpuC_3GZVv_D6DtlJjPEvUwVzNrQORFY2_mDEclCcirMu4zxtISuQMz7Ug2cqGnhCqjmCgURBBkqzwUsBHg0rPXvAbMtjh7S6nwdjBHRjyV_qIny3G6h_gKWVjMbLm7tgyvLiyoJ0pOS_kqaeO4YnuhMReeXFUbJlYBtvU0RQLIVQmgXwdJ8cYRha5vp9CZF0-PKKCY8j0BTFfXH1FkxZnvIK88U93kOQgdYn3p2z0Htg0CWGzO9G34NBqWkarC1NHBpwja_lTK1c-gguDGdxgvb5PF6-IwhdTurNd8lhdXyKiFndcwdDZe8RB1RP-XkSgIeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=k-cfljrGkEGwKNlxOcGVQMfd8-fBpffTb6GR-HEimT2bKZ14sIMH3967fUpg4_SPECd_gum6NIuSZhAEVHSw_MkFE1XzU-7SWW7h0O_jvGSNomnAowN0Mq0Yw-h-ZBSWgrIEu4z2W61PnyB6OBx0Xap1azkl2y1ywZoYhktjKVuixnf9hz6FupTpgHWzYno4ke-ql0evSlrU39SQbvHJu0AwtaGKidAF5jRBw44SD9JhMpxyij71JLGa98FOLi2dB_ZVpPwBb4abZrLO4Q2K-vIp5FghL6wqNmeKz00ZTOadsSpOjcZXUMgtqmuJ0aByWxftLGrL7UhS6qDxhUKG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=k-cfljrGkEGwKNlxOcGVQMfd8-fBpffTb6GR-HEimT2bKZ14sIMH3967fUpg4_SPECd_gum6NIuSZhAEVHSw_MkFE1XzU-7SWW7h0O_jvGSNomnAowN0Mq0Yw-h-ZBSWgrIEu4z2W61PnyB6OBx0Xap1azkl2y1ywZoYhktjKVuixnf9hz6FupTpgHWzYno4ke-ql0evSlrU39SQbvHJu0AwtaGKidAF5jRBw44SD9JhMpxyij71JLGa98FOLi2dB_ZVpPwBb4abZrLO4Q2K-vIp5FghL6wqNmeKz00ZTOadsSpOjcZXUMgtqmuJ0aByWxftLGrL7UhS6qDxhUKG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8gZ6AYHahfLeZWNNvgqm48Z4VR7Qqbtkn0oEk1kU9iBCkBTKrw8VLJD0GH4oKaOqsDVYEylY13DpN6dpm6wgJn1KvIjfwGl7FxgTdznrkZkh01MBUuGwG38mrlK3464UEfzlrhJhA0IGSHNTLL_7qCd2ZYaDCQ6Sekuc93aFagyz3xl5ajmbJSEh3Z4Uzl7kwdi-VvnbRC4s7DPuaqegzJ2XLjuBRwU8SUiUWM07eh1-uYrfuQx22H_7VmNCoFh-TNIwFf5AEWMdSI2caXNKnBiPsASYvvgLiFiCtI6aWqeoKosKdBjdl4t0SgUtdQPUlZvKpJ81eLO61JgPrRGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
