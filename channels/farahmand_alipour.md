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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 18:41:02</div>
<hr>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rPC0_tFl3pbMOow3W4bWk5VLuLoGY6TM0wFhOo1zV30sUUIE2nxt8F0Qs8ZVKN3E9FEqYAX6_2EaMrCNnQZ47ytAZAcJBPiXKPVowGdjzDSeGbz5QtxvWFkumSwOL6q92qbYNh7IYjcJR96LSDjBGnRU5jetamb7s5hEu8s6jLvpolYBz8semwBTaXFL0kte8jHkQK4MLV17B428zZRq58x_0PqCSz10ZSRmV6yrCIQmvKevm2IEKwFWS_0nbJiZmhoakOqvtPVQjnzXq6aZoKLRZfdbpxBU8ZiUcim4F_fzWQ0vMzCgdFBBc1kVsztPDzJwCh_G9lvtG0ZhMb8cxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pYaHsv2IVNm9nRk61lBOzxSKSanQRBiwJFHs3jJnL973EvD0q0z46Ad4867yHg2afmhhcyv_lMn3EWXovOLzkOBm-bdFvzxK-3lDeSDdS9OXhVyVHuoQPATDHEzWluZIjyEuQkXreKuYBpD9Qbb5xw7_3Rvn5jCiUSadDkhrhmto-frAOHhHpyBLGn8c8rNRVl9bJBUjCt9i0Pt5PZg1JG9UR2q5dgzESslqL7iToavuXjG1IIcBFzVlkLh6AaUPWza2jloRtZa9SGjqlZ6z-kjCpy27jYbsLX-h0o3f1hZSPyzA778k5LSET7KOdHuMuLt7DGAz16mQxURs2nzmWQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #96</div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwtalJuI4ISK7IQV7YrAvbHJj4aZpfjdhF9SZnPXUenA8e3JE6VYZ_JgQGbOAe1JK-AzhTyC-u6Ps8BU6bRa-JO1s_WMStSN1Uv7k0F67k970czKZ1Tm98V19lLVw9QRv5st6M_c0-tNi6nh_ibfKOrsdtxJFOGxW6YmxiBJuEa8oozwQrqUZsXwLC1dqMU4371nMe5z6ufR01qgVhDsgJxFeMnRBMvBYgjtLw8w02tcuhsPJbTHlZg0f6pPtYeWjGsN6844T1At9MdsN4Y8i-AwutsrC942gOzp7EnQDrtgr47tQv422sdIF6mVPhHsfqVYxNfFEM0gpUgqxz3tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkPlS5eGMm6Yc2WSpo-utRTSYJ8NveD-Uz_xnXbrQ5OdIOrxaejh4CRYvlbHJijvdWWxn98GV4MadzaLXfnGpTa-prm-wjofhmQjv_pwdLPBS0uIL-6-w4udEWjpNHmXeDi2_W1wBepQswCNwdXVRXlxvmP319q2M8DCnIeZ5381YrzMrIESYlV-3pBN2MSCKLtffFE8GFvQB3MqEiW-XV4Ebomn1ZZP4GBetgeNMsJ4tKrVoPuU9I47u72Deo-xMW5d4YXMiZLm06cBEcoJHFyVGFg_YnWkrtkIbx37p-kmdDJhVdOdc7oOEoqSR5GFelXpdoqukKaWxPAmtAz5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKj_RbNEOApa6XNKCrrK75Gw5e6ZW1EVOpYxKDb6Ux3P_MCLKBpD8crp4tmqBODk0DBVG6X5CrJuMPlligOXIjIUDciCZGi5wMBIiN2oXrD1eezOH5TBeUTDaMamIE-US9vzUSJyExD8-cyxZsXsLI6aDalTb_jzM0fSw69jzDZjlCnxH6UHvUOi743zHiMyPx6y1y5rDgLXs3Yy_uQ3kvKpGXbUPfO9YJEfprhBXxV6a-O611YvPpu5F6USuis8KmI1CYNg5iGsKCT4vqfOx-TJlWFkGqdpVu0aQPksQIUXm1P07_EdDd9XUgLJiYadFvxxCMeLZ-Tp4jpKYEDnDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmKIYoON7V6Ue4IkHr6qG7AVT4tY2Ozky8KeIfbSAqpNh62uYZwH7vemVUT15BNcjb5AjtcsMNXTKvPU2ZJITBXwE9bjHioiK5MfFCLo6F2SnKxt7b5upzfJovKZEPAMhR87YZsoUiR2E_9jwY3KPlTr0QTsS7OpNAeU3V35XqFjIbD3lABISNE4dW9TLcqxnw05fEaDX-tk0S9AkWzHB0j5KywpFhMFNJ4Jn70AMEQCiayYtpFvPCSZUY9osiK66PyhE51ayLuFt8DcGu_IMvJaiBvArbD-RBLN6n9zuJpe1tyjaK7wmCdj0cAnPeypBDf7IKLvd3WVngyZq6Xn4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CGsBezb_kAcCvvIbu3c8ORkvDGf8smzEdU_VVT_TjSLJxxcAAPp1lmm_73MDj13lpt53fG7X9iGyMGB1PsMcQLpupLmf5DrilMcW2GSiuZCPCKfDAYubJrOOX5-lGEWQ_lPQGj_Z7RnQ5v0b8zcr6mW6uHRUji4ANCF3cx6qku8f-YvfFVsfwaAETLKEOXBC0V7b3fF8ZEs5O5b5L0pubu_8VMV6hWvBep58Z96fVX13u-iprdfcuF23fzwt8ir0l2esRbv66E9yIPt5clRxOqTaEr6K5ip-KfgAS_kpXaOm2lfaOq4Fvf4DEAUkf6MOoTeznqvEFx-5KeWi6lfn6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=CGsBezb_kAcCvvIbu3c8ORkvDGf8smzEdU_VVT_TjSLJxxcAAPp1lmm_73MDj13lpt53fG7X9iGyMGB1PsMcQLpupLmf5DrilMcW2GSiuZCPCKfDAYubJrOOX5-lGEWQ_lPQGj_Z7RnQ5v0b8zcr6mW6uHRUji4ANCF3cx6qku8f-YvfFVsfwaAETLKEOXBC0V7b3fF8ZEs5O5b5L0pubu_8VMV6hWvBep58Z96fVX13u-iprdfcuF23fzwt8ir0l2esRbv66E9yIPt5clRxOqTaEr6K5ip-KfgAS_kpXaOm2lfaOq4Fvf4DEAUkf6MOoTeznqvEFx-5KeWi6lfn6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX_EEbd8ka955gUXa8mjqa3j00ezQAkz8Wd7L1Hn8nEVCuzYntInb8g1G8PB3j6jbX4UYMq1UngMzJnI8rgc3lE54-OZHvEEC7lmVXj9eHTB40f2RWOPjlorBYln1aTS7c-p_wiO2RNOrA7kmRphQSOc0UeJaygPurCnf1Rb67TwkZ50HA1l8eTOYYvvlwCQR7ZpkYQIG4WVmRXAjTwnAez9JZILcbTNSVbzVSyCXsJDd-x8x5-WRr99AUPX3fjklB0Hi9lPLdyzpLvm9Gzs2Vx1XB-jCvs1Sm7pk8JGZla7Rbk-bZhviEfnSZg7kAgCRgsKTOywsOD2TcHt8niaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=ikV5mJC_Lw2eeSiVZwr-Bgr2dr4LY0Jv9O1hPG4jXnbSVs4NjO-0hHsJ6sqbXh6IEi-tZhJ8LQDKeUloCAiIbzmbVr1SqsrMKXeP6RMvqcX5bSYfPjl3ERQ9X-tVKyiTXbAPbIC9OO2dvBKbjkVXW08D20RjDwURnDcL47e6OvKHwlLAxoazfK4np2-bTmwEmTOJ7dzhjnBcDfGRVS05p3IXKUTaV6HYTPvLK0CODVK_aLe3mr7wKEVp2SpbIJ6UY5M_Szzu8WW9H63Kmg3DrGkOLilbiDLb1Ox-23TnYwUkRTRswv0jhl0qbJq0XuH9TzAyAKypDZdCTiQdJFZV-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=YQ9jhX0V4au9-TB6KT3K4pvFzY1tcwrxAtDJX0NqILQbptdycHmCb8LXgP-sHrDVWXo1FKFTm3yjypmszMUmG8idcz28hg5ZqQa2cMbj32rSuAQpr9Od2XXxA1ye7t6jBG02-A5kQK0Txv6JEvcZRV60r8meCJWZ1ToZePNeah8h4jWC80J3dRYv-8g_dpq7KzJZbSrzCsbg5hFEAw64Dnvrr6ER61ezDTbialkyVzquQR4BkqDVkhfiJZyKLjfq0lq6pW_DYXmIX2P0nh6uN3ltkvkjlGd67urc5Q1z-Lv8_aozFZke9mlU91wZwQYxnr6IWyyp66b-BU0o9NhGIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=YQ9jhX0V4au9-TB6KT3K4pvFzY1tcwrxAtDJX0NqILQbptdycHmCb8LXgP-sHrDVWXo1FKFTm3yjypmszMUmG8idcz28hg5ZqQa2cMbj32rSuAQpr9Od2XXxA1ye7t6jBG02-A5kQK0Txv6JEvcZRV60r8meCJWZ1ToZePNeah8h4jWC80J3dRYv-8g_dpq7KzJZbSrzCsbg5hFEAw64Dnvrr6ER61ezDTbialkyVzquQR4BkqDVkhfiJZyKLjfq0lq6pW_DYXmIX2P0nh6uN3ltkvkjlGd67urc5Q1z-Lv8_aozFZke9mlU91wZwQYxnr6IWyyp66b-BU0o9NhGIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ly5igrZ1ehGhU-YLwi3Ls-0096_W2bCwU9VhBKsgA37_vMRud3ZturgL_A7-ZnAMTmcnZBVbKl9ykrfLRrtr_Uyoe2seVsjEJ-PM9lp_oCaaK1qB0cBjpa2tLfhF8naElsu4uSOUTNbKZIX5yjvdzJVU6N3CWyMuDJ9jVufryb_ZzCTXTQEokIyl-Pcafe3oQ12tW4viYd684G4dtSHEbMJAbtPfz5bWGIdLH3ES5HhLXUlTliTVDucimKDSOc5bXHyfnr0GZqskLy1ghsXuU-9oFsBQFZ3pyHe36UYzXdXgrRWjNOqC0gWDyKHVCPeoUOus3Gd8eC-zXASfP8uHaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=IsyIqyewstC2gJo3KTrzOrajHNgnSdCM_y_j-W9bOQ0c6hsCiAjr_rHaGF5VXyQWJyjkiMuEGjZxAsOE_1CjEZu-fWaxEKzqowAKusnAg8TxfUtDW1wh9hdLyZe_k_tDC3QhVqjEDHAlc-jo3-S9VnI0NdxoWW4R5JLC2lHN6O11QW4hWuWQHFeEeVIl8vwTxTvxMfXfiTc8fLC7LXR7sm4UkLlfkn6n38y36DxN8z3B9QhgZ5f9QuL7HQ_xuWRJU4NAm0BN6I7J9aCwjQIdE5oFSSMpiNskaAKI2pb845yRJBlojZ3seR98XAlroHLYoQhYF08utWqSmz7TOR90CQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=IsyIqyewstC2gJo3KTrzOrajHNgnSdCM_y_j-W9bOQ0c6hsCiAjr_rHaGF5VXyQWJyjkiMuEGjZxAsOE_1CjEZu-fWaxEKzqowAKusnAg8TxfUtDW1wh9hdLyZe_k_tDC3QhVqjEDHAlc-jo3-S9VnI0NdxoWW4R5JLC2lHN6O11QW4hWuWQHFeEeVIl8vwTxTvxMfXfiTc8fLC7LXR7sm4UkLlfkn6n38y36DxN8z3B9QhgZ5f9QuL7HQ_xuWRJU4NAm0BN6I7J9aCwjQIdE5oFSSMpiNskaAKI2pb845yRJBlojZ3seR98XAlroHLYoQhYF08utWqSmz7TOR90CQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obtLZBDVA716BI4x_7waktIOmJ2oS1LQSssN0r9rxhQjyO9CsogT5CuBF1bVY7gO1IRJ9_WAipmBrKUWxFkM_Ibl02Y8BnAnTLOivliGAKmklqCeRvL5ULwdvxY9zroestHUQp3a5IupB71k4L00gr0jDXxzNOsx9EgD9JnpxGJFV6pCHfGD1GaEMw2AK9VDHD2F2Eo9hZglC--aMZIkdqox4ALdAdPu0gEjBNH1F8aLCk656vh4MllyiEzQJVOA5163nZMmY-SWd1Gl5iULqxvWJG1ynYqRtKGkiXIiy1Er5baWb2BZvt8jcRC6rdsK6X4_v2qkr6xBZZnh3n6zMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cWGhZTxQIbeJCrAILbBzBpdKJLFlwm--_m2wdqEV3z50igm5fxiOaNpnsgEtTGxv5kQJIlsHQ7HvjGR_IEYF6lOm4cKhlDfgDSwKY0_4UdXn_-YBFZAXNv02k-dMxbpgH1HRlY6iNgG-qM77jA8hcJCinuVdoAeQHsZY09DY_A2FdUwoCBXsupWMW3r1PXMzPeqXhn9nsnUtWcvu1vv1JUJAYfF3hLekQ_JG5euyPjwcTv_pnED-3Qz2CWa6aKQF0fWYDvX9pt8rwVa9lmy_XKFruaPyzW3tBn4vGMrdsH-PZmjgkV04vTlvUb6Sy9Fkf4-s3OVJlYRCM_IiBxbs2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=nAqlR_LTde5IbuHIqz41fxHqb-OgESfe60T_feUduiPRkqcVRmr7Rv6Wzbm6P--MDuzh0WKRUXk6vvwVFzXAIFRyUT1YCmI6Jg8XSvzSMRn-dBdSAXU-BaV8gWyOpQ7HcsNgSHXwbruK8Lm2qZ75ni66f7gCDQS0dNDlgMDUO_BaGPVd60alhUy1XEL-iXnSOhC3B-1G8eQrTs3x8nokQSJWh_pBCobMP4c5E-4gZ30ikK_UK7JsD2fqRsM4RusP19T5UPeFAUcSCkFtCiLlpRCm6dqXPkXU7495oNB_8N1JyYFvOs2a9zNG6nuikJXkdtX_c1RtZfoTW4NaPkn_JA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=nAqlR_LTde5IbuHIqz41fxHqb-OgESfe60T_feUduiPRkqcVRmr7Rv6Wzbm6P--MDuzh0WKRUXk6vvwVFzXAIFRyUT1YCmI6Jg8XSvzSMRn-dBdSAXU-BaV8gWyOpQ7HcsNgSHXwbruK8Lm2qZ75ni66f7gCDQS0dNDlgMDUO_BaGPVd60alhUy1XEL-iXnSOhC3B-1G8eQrTs3x8nokQSJWh_pBCobMP4c5E-4gZ30ikK_UK7JsD2fqRsM4RusP19T5UPeFAUcSCkFtCiLlpRCm6dqXPkXU7495oNB_8N1JyYFvOs2a9zNG6nuikJXkdtX_c1RtZfoTW4NaPkn_JA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0nmLIHw3U-jGjbQoGy5F5oUgeI6u-lTfBS_cyg3S0uxdToGriT25C-mee1Xm9Bjdym_xdtAd-spXOcjbipTuhenupGqGXY-v9zHujsKtouQOLBweUMet6M9D9pSMhsIH6SA5iRE-trujmgCjLVlOYmKz6rf9Fs6AFumfFEXRtg238N42mzxXToiKnXdbRzYtALJhmbDt4yz7pOhKbyN03KP8iPW4KEHQnr45o1W8pubx5NdTRr5T5H4W8nqOQ2p__-RRt6L-VQogRJ2ES1WU8fSntLWhvy68Ht3nMjxLWnpCxsnVXViXYwNrB_MO9DiqsTRjQCJ44rSQd9_andZeqos" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0nmLIHw3U-jGjbQoGy5F5oUgeI6u-lTfBS_cyg3S0uxdToGriT25C-mee1Xm9Bjdym_xdtAd-spXOcjbipTuhenupGqGXY-v9zHujsKtouQOLBweUMet6M9D9pSMhsIH6SA5iRE-trujmgCjLVlOYmKz6rf9Fs6AFumfFEXRtg238N42mzxXToiKnXdbRzYtALJhmbDt4yz7pOhKbyN03KP8iPW4KEHQnr45o1W8pubx5NdTRr5T5H4W8nqOQ2p__-RRt6L-VQogRJ2ES1WU8fSntLWhvy68Ht3nMjxLWnpCxsnVXViXYwNrB_MO9DiqsTRjQCJ44rSQd9_andZeqos" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=V4YQ_ttJXK0FAs8hxgft8jj2qPXAL9Y8fCqJ5ACTLQIjOqFo6GmZ87Hg5N6lJZbVdwKa2z030X_p2pvJOxGkAlthnregb2DTylOQrScwQ6jlEgIP3j3QGbUOy9sm6XJ2dIPLZoYkptqHDoRZjxOmZSLri1GNDCgKOBu4YwQzLoAU8fGDYIAlIPqukPnxWvoyLEYsU2PpELK14rAPObGh0lB8LU2ewIjWnvOCRF3kBNx5DYEQtVYl7O2ktm8cixl3WM4RdK9abKSzecDsgrADh1dO7liEB57UuG2csq3JHoGMFBaKqYh52v3sj5JbZWX6aIymgtyBp86lJVgvivCjAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=V4YQ_ttJXK0FAs8hxgft8jj2qPXAL9Y8fCqJ5ACTLQIjOqFo6GmZ87Hg5N6lJZbVdwKa2z030X_p2pvJOxGkAlthnregb2DTylOQrScwQ6jlEgIP3j3QGbUOy9sm6XJ2dIPLZoYkptqHDoRZjxOmZSLri1GNDCgKOBu4YwQzLoAU8fGDYIAlIPqukPnxWvoyLEYsU2PpELK14rAPObGh0lB8LU2ewIjWnvOCRF3kBNx5DYEQtVYl7O2ktm8cixl3WM4RdK9abKSzecDsgrADh1dO7liEB57UuG2csq3JHoGMFBaKqYh52v3sj5JbZWX6aIymgtyBp86lJVgvivCjAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSrMo2Tf0KARjRRV1WjYDoovCnOK-DjFCFugtxx001mqrqAi-H8ncmqrMZDCh6TmdXTEXppoI0fcmy4que8UEYycxsTnnz5i8FUWHt2MrapJvHYRFJuJAEC35oYtDP5cWBywzDNgZ9SrTpJFu0rmkZewYPp5He1PpwxvcUNI2Io1_q6Ugc3O11gDJ_H8pumogNgDnSAcwhg-WfD_muG6YkF-eFwfYlq00eIbTVkYPFn__wYAUbA11J4mt7QOMx3JZYXydq5Fko6-atwVM-_FxEJ8zF96DM_JA4KHElAcV7MIF9h6JucCyVfampWg3eVZT04mjAuqYGLfZBGxIGosoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=fpQdHCCw5ZoP-v9kmdDt8ApvRioQglb2xwEh3eZhMAuzsccYTlpWX8QujMqtWNcKRAYNur-xH7YCBGpqNnS4PcSuB_g-jwtVc8b8tH6z6jR_oujDEq_-cvMhOc8jvAtZ7IDK-eEnx8IkkJPm6UHVxn_bVCSY3HKc7lekxxB2JXauhEL3uhkE_tWgEIAE9FXX9Hgwzb19mXqQEacBKevUrfHH0Y_DGJCoMg_l9IfUG1oVXIVhjuW94ATnNa9-PRghQbCg4TgnV3jBK9jTQIZaRlqY_ax1IBMUl4xtcAITY0hv-49nlwtsZW8T73wTphxg4Im68Mp74HE46SDcoRERRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=fpQdHCCw5ZoP-v9kmdDt8ApvRioQglb2xwEh3eZhMAuzsccYTlpWX8QujMqtWNcKRAYNur-xH7YCBGpqNnS4PcSuB_g-jwtVc8b8tH6z6jR_oujDEq_-cvMhOc8jvAtZ7IDK-eEnx8IkkJPm6UHVxn_bVCSY3HKc7lekxxB2JXauhEL3uhkE_tWgEIAE9FXX9Hgwzb19mXqQEacBKevUrfHH0Y_DGJCoMg_l9IfUG1oVXIVhjuW94ATnNa9-PRghQbCg4TgnV3jBK9jTQIZaRlqY_ax1IBMUl4xtcAITY0hv-49nlwtsZW8T73wTphxg4Im68Mp74HE46SDcoRERRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=GZNg51x5YdZ85MOAQVXq-Zh1SQtIu-qcMjjTliTUfXQISbIdc9R_Lhk87yGBhspGrcNXD0Te2s__W7bL81NnIGQqYxZNye9qHva_fnxaUeZcdf2ToDmvnbHvc49E98y8humD1F8CaYlroQod8Ipc-mBLSHE7gPfHkpHMdeWg8MsOgiCo_q0N0oYXqvEGVkpQTcf-o6MRVmqytf-Ec5yW8h4CJNr-MZAlsCk-AGQG9rKR6cHM1UKjmIEDJ7sPmPdBpojqpt3FnM5uYzDR7UUNmqoCtkiBikUSFwC8WEbwiS-xkptFGPjnWsV_NfHkv2t2oPMmT181rKBSXnLfp36AoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=GZNg51x5YdZ85MOAQVXq-Zh1SQtIu-qcMjjTliTUfXQISbIdc9R_Lhk87yGBhspGrcNXD0Te2s__W7bL81NnIGQqYxZNye9qHva_fnxaUeZcdf2ToDmvnbHvc49E98y8humD1F8CaYlroQod8Ipc-mBLSHE7gPfHkpHMdeWg8MsOgiCo_q0N0oYXqvEGVkpQTcf-o6MRVmqytf-Ec5yW8h4CJNr-MZAlsCk-AGQG9rKR6cHM1UKjmIEDJ7sPmPdBpojqpt3FnM5uYzDR7UUNmqoCtkiBikUSFwC8WEbwiS-xkptFGPjnWsV_NfHkv2t2oPMmT181rKBSXnLfp36AoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=d7_zdlxoREirkYJCgUGdXbX1zbYzIb5QekeYGVYfHTIBgng6RhlLvULdYETbxRTVDsDZVQ0KWyji02ZQBNmBEEaTdL1iBc3UnyJETm2tyvqTQNABIHmdRRY_5LwdKKiQA6iyOn-FK-ZgHlqMnS_X05Jl1c7PyaBQ2_3nKuEitCEOGv8T2MwS_dnsAa_c0CZ37gxo7kojFioLGpgiTbF7BCOglfPoDV9CbaQKRrgc56s2xef8F74F5yvcT6LjAWpVUcHogGnvu58kNM2Eh1AZYioj2VzSFw3Xw3VNQWTLQ_tC5bFaSn4zM5zCrnC1WzbBU62j6JTF85mCfysZF_uoiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=d7_zdlxoREirkYJCgUGdXbX1zbYzIb5QekeYGVYfHTIBgng6RhlLvULdYETbxRTVDsDZVQ0KWyji02ZQBNmBEEaTdL1iBc3UnyJETm2tyvqTQNABIHmdRRY_5LwdKKiQA6iyOn-FK-ZgHlqMnS_X05Jl1c7PyaBQ2_3nKuEitCEOGv8T2MwS_dnsAa_c0CZ37gxo7kojFioLGpgiTbF7BCOglfPoDV9CbaQKRrgc56s2xef8F74F5yvcT6LjAWpVUcHogGnvu58kNM2Eh1AZYioj2VzSFw3Xw3VNQWTLQ_tC5bFaSn4zM5zCrnC1WzbBU62j6JTF85mCfysZF_uoiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=gFL0HS0j6Esv49_uUthdE8BvCzYy9RjgBu31wx8JWP0Hn_bg84H_pciWfuatB46LDCwKK7ZNggcWxrewMS6cU83p0tSGVh3dBn8hVEUGhe7_GM1tgEkrLSgsYkgX0HtB0QuOg9iYFC0H1A8jkpx_LxJg6INx5y9jnRMUfLTHTMhpQW7BOoN_4uhgZ_KV0BVaRMomr2QoniL03uVc2tC5NNdCYjlh1yEm5ZpypWcCsc2Zfekm5vIqLkz_0EHRtPv-3FOtUnqU6fvSVjuI45nub6DC82MGbvWzDUSWsCXZeP8pYarYcxFOudAmE68Qze1LnsxbqqQML5-gLJA2NnUtJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=gFL0HS0j6Esv49_uUthdE8BvCzYy9RjgBu31wx8JWP0Hn_bg84H_pciWfuatB46LDCwKK7ZNggcWxrewMS6cU83p0tSGVh3dBn8hVEUGhe7_GM1tgEkrLSgsYkgX0HtB0QuOg9iYFC0H1A8jkpx_LxJg6INx5y9jnRMUfLTHTMhpQW7BOoN_4uhgZ_KV0BVaRMomr2QoniL03uVc2tC5NNdCYjlh1yEm5ZpypWcCsc2Zfekm5vIqLkz_0EHRtPv-3FOtUnqU6fvSVjuI45nub6DC82MGbvWzDUSWsCXZeP8pYarYcxFOudAmE68Qze1LnsxbqqQML5-gLJA2NnUtJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ati38VoJF2RJms0D6XThDHsFDQQnrWhw3qOVgM1TnkRfdWZai2aJvmSMdY1mAalHHxZz4T5PQw0SfPDzIxe8Wf1mrd8yIm5pCeNJYzKj8rNvhiLzBKHjqX_TGq-DIaeXWx7hWlV8gDFJfibhrM28HvOjnxTDROMIId1RvmGFI1czYF8CvhImvGzbcxjhQa1cV9-cbmsMX798ToVDpI7f7Wdt_SZjJvvJBIhe8CvVv59tbIpWTf_UjV3D0mGTNybNpyVHap6f75KTUASFhY8N-6tZdnGJRXdDUDz4cQA5XyBAsCEuKFqB_L44ZVIcoUp5cIcJEm_Bvz_V5rE40dG4rw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=C16QNFw5Kxdk_hTfOfcts-e30ksaVQz3-MVkZCLRz8fflV32BS4hjyTCRAqIchjV-PJdan9wY-gpZeQvd0uGsKjcqeAGWUFrsUCK_0eQYPtlsAuhCH-k9ECBg3pYigUY2_cn78FtU4OyZoDtOoOTU6pnJymHD4APf-FhJjZzESO9IfzDQq4G4KG9U-M4AlgML12E3UatbI1rebVyR8W4cEwe_LkJN-ibYDprGiFo8TMKEECQ5alrZT56ODcvL_T21aaO2UzGyeOpCj55K6gnkB_RrM1ojjPRX9a67Ffq4arql4c6nIakiLmHluRalPGWceTPOhGjaaCiu9bwmHa-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=C16QNFw5Kxdk_hTfOfcts-e30ksaVQz3-MVkZCLRz8fflV32BS4hjyTCRAqIchjV-PJdan9wY-gpZeQvd0uGsKjcqeAGWUFrsUCK_0eQYPtlsAuhCH-k9ECBg3pYigUY2_cn78FtU4OyZoDtOoOTU6pnJymHD4APf-FhJjZzESO9IfzDQq4G4KG9U-M4AlgML12E3UatbI1rebVyR8W4cEwe_LkJN-ibYDprGiFo8TMKEECQ5alrZT56ODcvL_T21aaO2UzGyeOpCj55K6gnkB_RrM1ojjPRX9a67Ffq4arql4c6nIakiLmHluRalPGWceTPOhGjaaCiu9bwmHa-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=QDM4KVJqk2CFcYtt86_EUPqLFGX9ALo7cVrV-nR0kD3QGJgT6CLmq_SXbfC6a2KaM2CM_KDMU8mg6NtQ9qCNbreV3K4nU1lx6i6C5wxxXFkBEhteJ0y3hxp_m5xEmldOHcVseozUVztiwNOixhoHdYLxVnWAxVWfNQA4yAVso4_fzTdQmYB-7GKb0mWl_VkEe49ZNCDM4tQn02WTsZT5Sjz7q-Au9rLiqNPmtsvMghYGmea7F_1Q4ww9SqdJEV4yCegek4L_-QwXQ6defgBILWiRIK5mZnB_-51zusp-aMoY0uq7QpHYv-kHmJh1mOuWq7w6uNjTAtNaQilF3AfWfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=QDM4KVJqk2CFcYtt86_EUPqLFGX9ALo7cVrV-nR0kD3QGJgT6CLmq_SXbfC6a2KaM2CM_KDMU8mg6NtQ9qCNbreV3K4nU1lx6i6C5wxxXFkBEhteJ0y3hxp_m5xEmldOHcVseozUVztiwNOixhoHdYLxVnWAxVWfNQA4yAVso4_fzTdQmYB-7GKb0mWl_VkEe49ZNCDM4tQn02WTsZT5Sjz7q-Au9rLiqNPmtsvMghYGmea7F_1Q4ww9SqdJEV4yCegek4L_-QwXQ6defgBILWiRIK5mZnB_-51zusp-aMoY0uq7QpHYv-kHmJh1mOuWq7w6uNjTAtNaQilF3AfWfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmsnGTlCQ-ekgrEN6cdoG37Ok5bf7MhJpvjuVL_Ma6MDNWgjsQQtjapsbSE4Yt7x_DlFQrs82kpXMhknAcc-bozPn80z-crtE9jbFYPrxt0ScE2U_OUo9pxAZsHrffzHMzD35oz7dhWM6ihEoyqbM_noRPjtFRR7jJswNOHHwYrb6JY812W4bL3GjGaGB5aOcx_O7ttSbfqggI1xDIMtfjVm3jWvypYladVTf0gXxcKYtl-AIAal2aVlQDRH5LvV20_XJV2h0BBGLSN1wWEqKasY4exjLsp5IkWqMYpdQs-0AwK6YRwRZgJL_GLNPRillizeI7MlvlHwWk80V1oBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=khqSO6f50SF3AyhNLYcGXfoluIS8ieYPwMrEV1u0Bot7dfcf2l_ooNiSGoFbfbm-YT0gJ1G5vrOQbjcp6xYfNALX6Vgu9_5P1l9O2FrI97kpwIeMzJoa1QqcdZlLas9sD3s3_e6y99MdZtYzGL1lKnSOV5sO2fWf6SZ0zHr2MhWrLAsBLu1S524w7-qZkJxhSfbxhxcdwxH3v5iAgfPozxOFMxwLtOpHIhN1mn_TM5AGL0AHe1d4PJus9inkB0C-XyeqYRK6CQTQBdnOsQ6F21nTjonMifgStzBuEtEoTttJc1E5Uh5IMrkommT5bW9YRInmUmFMYsrprPqJsXuong" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=thPPJ-rx50Scm0hSqx062SdUNbO38bI4SjfSQBPosXX-YUFyeFs7hYwHjIxPt89wecHlsP7178izSeRf7d3Jk0BSyRQGkhIsLXwL_z0Cwab55fr2nZp8MXUyjgmp0j334psNSbkJ-QAeterAHY7Wl31XUnsPCeo3G0t2hsFJrzYT8hj6n5H1f9q8L3KShvpQJd3a8WiVaLStRyJ70ThMk-jtngDzIZbHhxl0vssUQNEBmImmzhc_RUs56XKBbW2XdLMu1xee-n6sHhmflBVERbkZxRSiqA6SerOp-fZeXMrtDqiPO7tsy5j1glqLRg4zPykpbSySbzNxsmGhOQaq4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=thPPJ-rx50Scm0hSqx062SdUNbO38bI4SjfSQBPosXX-YUFyeFs7hYwHjIxPt89wecHlsP7178izSeRf7d3Jk0BSyRQGkhIsLXwL_z0Cwab55fr2nZp8MXUyjgmp0j334psNSbkJ-QAeterAHY7Wl31XUnsPCeo3G0t2hsFJrzYT8hj6n5H1f9q8L3KShvpQJd3a8WiVaLStRyJ70ThMk-jtngDzIZbHhxl0vssUQNEBmImmzhc_RUs56XKBbW2XdLMu1xee-n6sHhmflBVERbkZxRSiqA6SerOp-fZeXMrtDqiPO7tsy5j1glqLRg4zPykpbSySbzNxsmGhOQaq4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=o5v3JexWGj3_Itp2uXpPAa4H-NrBZrbupg6NFOEsg7A_pF_dE7Z9_BQo0Ajvk8I37NgbFvfTOmX7DxA3lIzwA2JBvP3iT5hzSrAiCbQ1RghgUWLC7M7sVGjwZdPY7hgNyENVJ9xMsPcG8uT6MDm1POmulkGy_c2q0FTZ_187dZhLar2RRkmG52g6cADGyOUAEribqPkx1oUXIQVT7RHMNkKEusxdepmTVpvgQDab5t3Yq46YC1Qie53H4IiaMMN1Bcj7gKcLhp6jUGwyr2TC_ISjwA5FEFOFDWOZIhLCUQPSEBG3YW2ncZ8nirLACBYMiETSQY9KulVkDKZT3GoEpjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=o5v3JexWGj3_Itp2uXpPAa4H-NrBZrbupg6NFOEsg7A_pF_dE7Z9_BQo0Ajvk8I37NgbFvfTOmX7DxA3lIzwA2JBvP3iT5hzSrAiCbQ1RghgUWLC7M7sVGjwZdPY7hgNyENVJ9xMsPcG8uT6MDm1POmulkGy_c2q0FTZ_187dZhLar2RRkmG52g6cADGyOUAEribqPkx1oUXIQVT7RHMNkKEusxdepmTVpvgQDab5t3Yq46YC1Qie53H4IiaMMN1Bcj7gKcLhp6jUGwyr2TC_ISjwA5FEFOFDWOZIhLCUQPSEBG3YW2ncZ8nirLACBYMiETSQY9KulVkDKZT3GoEpjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lZ05jpMjOrH24prX8J2ohsxSli7f44P-MCe9EvgUTnKX9wKfbbqrXYXjgsPrZ5YNOW6S_BDDXdlP6NuJRVAuvC-m2_oQbdxxrLShk2TtawLexCX2NhjKzI5JsEn3qDTRoyXi-IhvjrLwP7p4HdtQZ25b7nfZoMKEECIpZ8O_pqB-I2wW_CHkG-ME6Ix9EP1403-bYkx99Q1Ehs2p3WQI6NwghGqUCKvy8kpjuMEon5_JnTUttW3U0uGWbSrKnI_Jdx-v7ijU0PGzCZRxKl3el3zvCqEsBIma6YhD6MWFe8u_KtzdgOHhpQAcq-F_bchc7TOvKiXAD57GPmOh8OPe4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aIAwfHlc8gXN-yDquF237XoOyXPGYtGcYln0Mpq_fSpv6uzaeCoOH44Fcl-DrcX9x7bfdQ4HZYKf-NGjsYQskw7uw0FcsrJFuh3HCUfbMo_1RYxPhrWqmN9JeHCxd4FHKBt-0A7DCYmsDY4G_STov25J-aISXvU_01rj3qAeIK6F9jMKdle9jb_D-eR70_ocnE2_75vm-NmQF3f9i4bxxlQnxwfeognXLYGIEx8eEkpIWWX0tDU6_8d-mZJ0cXS5Jbue44VQC-8mlhogp-hjWexPR2MHOnAd0XI0NFJjgvZ6uSdpcSgkA2cf1WmSHM8HvOPie_lmIq4458m8iRqwCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O2FZVvuI0u5YETS_cSuxQ_mPeMuHX41AFLueHHE1UdnXjGKrKJu8TNSKerf1hnNhI4_JAFv6vx7azos5SVAvX0dUa9PE6DnbHZPcS7vIXsnn_yli55R_LIYmtx8GLSNWxrFyH4gdpICR_02UYFmqUN4-v09p2VMEwZYgwT8DsqSE-dr5sNCRPJh695Uc6PBpjfqkB6EsiiLxqCJ2VYXsAKC1SpyKpI-4MhGTCEUwN-nTdFVHUdF_Cq-nikad137e0-xkcLxKtf3HBl2zpvIuolP5zhaJzk6dnnjRDz5MQpPxrm2uqRTlHsq8rZjXOs-6LyIast0sONJv3EejbxIg5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=eNh2iDg2Pw888RuVSJB1bCUp8zzKfJKNQg3yxBe4CcEmZqdKlSEjwAUX5hBAZUCLYEjTqiFzSiCqgggWqUp10dTF1RpyfjK1j7MhF7kjSzTUJPzye0ag_G9oLVOMMIoVbknCaTBTDuTEYGZHPgoVCvyWoSnkLvG3Ec-4rbDjzVQJI82k4kKs3UDBhFSjV3XQh7Dj3J4Ak5FB6qW0bcI7bDmNcNHmiqCWW3t3fKWPdHWMlEII23WIOSvYaYX4X_H18OCX8_FaIcvXcM6F_V4jK0x8UnfMO83jInj-IsEB1i5N3JRQ8oIoqX2X4rvM5PzvsF2_XJDCf6FKvZAEuZhs7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=eNh2iDg2Pw888RuVSJB1bCUp8zzKfJKNQg3yxBe4CcEmZqdKlSEjwAUX5hBAZUCLYEjTqiFzSiCqgggWqUp10dTF1RpyfjK1j7MhF7kjSzTUJPzye0ag_G9oLVOMMIoVbknCaTBTDuTEYGZHPgoVCvyWoSnkLvG3Ec-4rbDjzVQJI82k4kKs3UDBhFSjV3XQh7Dj3J4Ak5FB6qW0bcI7bDmNcNHmiqCWW3t3fKWPdHWMlEII23WIOSvYaYX4X_H18OCX8_FaIcvXcM6F_V4jK0x8UnfMO83jInj-IsEB1i5N3JRQ8oIoqX2X4rvM5PzvsF2_XJDCf6FKvZAEuZhs7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaSVOitERDa46K7Roz_RN5lJIe0pyzi5p5dK9jalDOAreAXd8rkQZkvuGme5XSUGfMwuk4IGe25mYO1jDtqNsnUccT6wHh9JqBCGQYlppJPZFJuM7PzBb80u09fQ3OV8RFxyMYeMH2iRQ5SniGRtX1M4pFny05wWnh2zib_e-lZSlU9SlD5vMfIY77aA68Ba6xujgLWbIwzKddkfoiJE3mZbjuDmqTYwbcMaNwU6LIFGXTstmMnWhLU9vB5EO-I9Pf6j5dJ0hGdgKfuhkBH15zFgqkXDaShSkYzhqCmFWrZ51LE2_hwsA18Nq-biPNbfcU5RvHSABxUFzPmBB2uV1fug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaSVOitERDa46K7Roz_RN5lJIe0pyzi5p5dK9jalDOAreAXd8rkQZkvuGme5XSUGfMwuk4IGe25mYO1jDtqNsnUccT6wHh9JqBCGQYlppJPZFJuM7PzBb80u09fQ3OV8RFxyMYeMH2iRQ5SniGRtX1M4pFny05wWnh2zib_e-lZSlU9SlD5vMfIY77aA68Ba6xujgLWbIwzKddkfoiJE3mZbjuDmqTYwbcMaNwU6LIFGXTstmMnWhLU9vB5EO-I9Pf6j5dJ0hGdgKfuhkBH15zFgqkXDaShSkYzhqCmFWrZ51LE2_hwsA18Nq-biPNbfcU5RvHSABxUFzPmBB2uV1fug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=ckqUumrKWhPQrypU3xORAcCiDWAd2LtwkQHN3t37zAJv2xyM6c85Wk0RGVOM4dxisb2QtPyGlmTslC2WFqWmB-SWWhws2FnljAXY9oyaRa9I3Vy5EpwXIgDGrCEX7G6JIVkC4haCyiz2CqqoA2RegSpMDuzTYJRsGquTmS9wppYXrB3IaXuml7PruKLqf_wJXLIiNYsLIKm4yaaUyNFWo7VSOlZ9I-LnZOMSqrbkwvzcchFwN_Hzt-PDW4xyxCEcy_F0BiEEXqfy46LQjW1vCAHV2gWq6io-QJvD2uhcdl_5dxj6MzlgYGJ_ij8ntbRQyjxDfTJsZ0rIyNookFmmhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=ckqUumrKWhPQrypU3xORAcCiDWAd2LtwkQHN3t37zAJv2xyM6c85Wk0RGVOM4dxisb2QtPyGlmTslC2WFqWmB-SWWhws2FnljAXY9oyaRa9I3Vy5EpwXIgDGrCEX7G6JIVkC4haCyiz2CqqoA2RegSpMDuzTYJRsGquTmS9wppYXrB3IaXuml7PruKLqf_wJXLIiNYsLIKm4yaaUyNFWo7VSOlZ9I-LnZOMSqrbkwvzcchFwN_Hzt-PDW4xyxCEcy_F0BiEEXqfy46LQjW1vCAHV2gWq6io-QJvD2uhcdl_5dxj6MzlgYGJ_ij8ntbRQyjxDfTJsZ0rIyNookFmmhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HJonXNwx-S1tgHC9_mAsybmDJ13uwPyqt54vFrTYMd624UNtZGyzVNfO3AdFABwnGd79o8YQM_OOhJ-3eVOWdV3Tg-luvoFjzEEtEiKVuRwdyKIBiQ4fPJwB1sbXICtbhlWdz_7JXNGwUQ9teCn6EJt6POlW79hH4Z9mmkQARoNZxEpIQk-ca1D_ZB8URAemNtXiN9aviBXWoZLBiuqFR9kvnwDFQOw1OoQIo1hni5v2u1F6BVj2pST1uZMaUcGPE8nO-wsNuZFSN17a7rZMQYQhkXG37REgx7d-yZePMz3jQVdJEIPdu_GBS8PRTjoHmPLeRLxA7P8k-IITLbXvMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTlOS98PcYp-VK6EDn7ziFewM2JDpZVtLZTzBpMygbUL_4efVh2qJEV0eXfEPNaU6RU0bZQY-iGdq1aSKuTS1Be_yY1G-3judlFN9pLoWArokYYedh0Xbmvv55BwgqISSzECGMl-ggg1uQE-tq_4NTrl6fT-MGg3QARrpIqKUYfj5Ui_HLhL3vmLbwXgF-5VwzpUgj4lByDFCiCP62tbeYORFZ6_LQFB_FnG_dZsq3pX5VH9wG5a2Qzv33eN5nvgS19cP7Ae5u78MT2wTd_1ebBL6qw5PLKvbfmV0649Os6PaZXRgIP_frJeeRbJKgF1yh5nFWPQjrt8ByL5mxxUKlMk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTlOS98PcYp-VK6EDn7ziFewM2JDpZVtLZTzBpMygbUL_4efVh2qJEV0eXfEPNaU6RU0bZQY-iGdq1aSKuTS1Be_yY1G-3judlFN9pLoWArokYYedh0Xbmvv55BwgqISSzECGMl-ggg1uQE-tq_4NTrl6fT-MGg3QARrpIqKUYfj5Ui_HLhL3vmLbwXgF-5VwzpUgj4lByDFCiCP62tbeYORFZ6_LQFB_FnG_dZsq3pX5VH9wG5a2Qzv33eN5nvgS19cP7Ae5u78MT2wTd_1ebBL6qw5PLKvbfmV0649Os6PaZXRgIP_frJeeRbJKgF1yh5nFWPQjrt8ByL5mxxUKlMk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGopaBcURTDuWGz5ik5wGOc-9FPwLA6a02kin3p_r4a0Tn7sS8x03GML5L11NB-J4Dg82AQUznr5f6aAs0ZkwTuOi7nbPCAYMWsaVeMmhKsYOgm-BKfxs6_BdvSKOs1L4d_HsXO1KuPL7T6M9eHVipb6ayiNSxPddsilb6GrpgSrwmN1sOXu0Bo5w2I4q3KRqYni81Y4eOzOvo2IaQ_o1P1rF7m_02tQBHt56xZSWGUeIUdQQ5Wur_KjowQmMYQX5Zfm5c8xXI3afPZjZw3VeGuiSruCmruVwCk4f62mfRGMOEubmxkGLwurcZOLukkGHUpB7FoWupO1YpnxXyQ-pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=N27VTmjsVEy61Pg1Ev7EmKiw32LehKPoNVWMjqSWHE5gz-ypboN4lw9fGo8SfmcI05zwyTKe91zWlF2Lu2uwe3RAf3esg4wr6IXFzkBtU9MQQVjBzL22MZEchT5ElTdaCJWej9eF83NUq-Dn0jSe8p3bx1M2XxEUan4A-9TQmWzptASLo6WF5qnnnPaYOa7XQYAM3w4mJxyrOb64mRegaGu7vVXCyOtntpxzi7dWyL1qpYqD3em_4Q8Q9EVI1PPjpMpfUjY903VPfp5rc_vaZ7Bqp9wIIyevAkuMNRh7eMvTQPFGUVtEAvUFxxXmKjUdnMHQL-mzy58lgINj0VTs0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=N27VTmjsVEy61Pg1Ev7EmKiw32LehKPoNVWMjqSWHE5gz-ypboN4lw9fGo8SfmcI05zwyTKe91zWlF2Lu2uwe3RAf3esg4wr6IXFzkBtU9MQQVjBzL22MZEchT5ElTdaCJWej9eF83NUq-Dn0jSe8p3bx1M2XxEUan4A-9TQmWzptASLo6WF5qnnnPaYOa7XQYAM3w4mJxyrOb64mRegaGu7vVXCyOtntpxzi7dWyL1qpYqD3em_4Q8Q9EVI1PPjpMpfUjY903VPfp5rc_vaZ7Bqp9wIIyevAkuMNRh7eMvTQPFGUVtEAvUFxxXmKjUdnMHQL-mzy58lgINj0VTs0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=largQOG5z-JidN7JDFlgQ3N2gdzQdwN7UIt51wfY_Hy9y7rmTMus1J0_5Rdohx-Uvk3kKT7a4Wn4hps0AIP-h5XKAgabYIT_SY_fvKlt2k_EEM4LROPD_YA_zFHlUAQRQ6bfC0Iamzf76NNQSvAwi1wuyZjwJxR8rgZ_4_nbMD9BaLsjDmbi7-sHdQ-7G05hQX_0Jqp6yFJB0XTkn24ynfCMG2VQcSDkosgXkPj38BX1NVQ3rjcnxIP-yopv2fEYUh03TQBak-oitAWJazL1xlJX_n9YqelDvfS6PNwEoKT2bCvqdUo8-WhSAsrS0w3-HTOaYHvQ_TjkeEV8sBveqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=largQOG5z-JidN7JDFlgQ3N2gdzQdwN7UIt51wfY_Hy9y7rmTMus1J0_5Rdohx-Uvk3kKT7a4Wn4hps0AIP-h5XKAgabYIT_SY_fvKlt2k_EEM4LROPD_YA_zFHlUAQRQ6bfC0Iamzf76NNQSvAwi1wuyZjwJxR8rgZ_4_nbMD9BaLsjDmbi7-sHdQ-7G05hQX_0Jqp6yFJB0XTkn24ynfCMG2VQcSDkosgXkPj38BX1NVQ3rjcnxIP-yopv2fEYUh03TQBak-oitAWJazL1xlJX_n9YqelDvfS6PNwEoKT2bCvqdUo8-WhSAsrS0w3-HTOaYHvQ_TjkeEV8sBveqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=oJhOIiZKw0mgmd9_8zwlyM1mB78W5xjA30S1BiuPehQweuCLpVDUiQQaUdy2mUpu9DHiddGDhhNumWFCSp0O3u2cwWyOWNmGw587rZCu3TMA6_Box0-YJYYN5Uj6jec0dn96liQT-V57nKjAaXMVHHCIjTlsphuaoUowQ0h4vSpQfP2pdggUX5tGi6WcGCROU7T3u5Kh7sMx2YlnZqsC5556KuXIKj8TE130yh3wG3K9i7DjvmIY1L0_Zi9t9KptmuV7hXeL3TGH0Czwi2Zjm8Cj46H4L3c1tmsXeJZeWdd3ERTOl1oUd_-O2rGTUev1iAWtw4FZPIeLHjQAeRvpYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=oJhOIiZKw0mgmd9_8zwlyM1mB78W5xjA30S1BiuPehQweuCLpVDUiQQaUdy2mUpu9DHiddGDhhNumWFCSp0O3u2cwWyOWNmGw587rZCu3TMA6_Box0-YJYYN5Uj6jec0dn96liQT-V57nKjAaXMVHHCIjTlsphuaoUowQ0h4vSpQfP2pdggUX5tGi6WcGCROU7T3u5Kh7sMx2YlnZqsC5556KuXIKj8TE130yh3wG3K9i7DjvmIY1L0_Zi9t9KptmuV7hXeL3TGH0Czwi2Zjm8Cj46H4L3c1tmsXeJZeWdd3ERTOl1oUd_-O2rGTUev1iAWtw4FZPIeLHjQAeRvpYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbl8LgnvkbrVqvad9G152WXh7CChBcPV9b3T2eO1LSFnmTWOn7QoGcAcivscPyYzCpRfHuPSjNggtNroCf73KsDQs1qbU0sMQl6_mWS9--QwFdTItT7sloZugjGBdLLi4FKVuMOP2hwjfgOxgMxPVGztN1Xb6m7T3eTSGDbVxo-fgf-ozo4n9I5u2Zgm3zV3kvz_8KVWHpr7bqRRZ6KLsc12ClzuTppiT-6pWJea7p4bO858VlcZvrhO4y2MlRDlYSeLaXGRIvhZ8DMt3gh_yr-K08GK0BlSUG23JFGOaPooGbj-jV9JcGoW_DpzE9SKMHUfQK0u8j7cxPgaQ35FuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2Om9-hgjsOg9LGS_MLPEAeZ33ZELeFHpLrlPRLjUEvYQmBT3hMb9NeWsCp8QTiGqzvC7Hz3fOityunHvcES9Bs4pHMDWhpY098Ht0jNxvDTrDpntwm3QEbKvngTgH-4RdHnAFj1MP9-OSKjEzFS61Ha5Mn6m-mpaYTvzb6LXZVYzhwwIQWnDqyIQxZn8uS0lVZJzT3TGurESIHgaVZ-baxg7pfE-xfMPi83MDgFNNdUjWEDPHKTvvEfhypuCXaw2ysj3tS6lhOgzcBW3rBHLRlavG7AjriyGNA8h_8xNV9gTvPOu-IMBXluthLHLYrE5jgiYKM-e-DJXqJqbNbqRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Eg2roZjGMLDJjbmKgpskfJFf-L0fZTn3gW7kBmwi0fLuvzJcUeUFNDGr_Da71Oe0h3CwFKVmcW2jSbzoyPu6BPU9_B6exFShl9gXnVrwnFWQjenQDO1ipguxB99Vl7xWKTrVkCxujCLOpKYVmv6-vfXu42bcs39xqe_LlFOedkb8cwJA4C1oNjEHRa2g4swZjNuiO-mvFP5iRragnaZ4fO7VcOhE0riNU-M9_jFDyIM2pwtwYW84L8i1ztX_Dw5dMTydC6ddyyeaSl-V0iWhcla7DJ6Kduuo8hj2GRo5K_2bjwMt5ht-30S79Ah2_-Y8sBBh_uUBdbXbo10yQBfEhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=Eg2roZjGMLDJjbmKgpskfJFf-L0fZTn3gW7kBmwi0fLuvzJcUeUFNDGr_Da71Oe0h3CwFKVmcW2jSbzoyPu6BPU9_B6exFShl9gXnVrwnFWQjenQDO1ipguxB99Vl7xWKTrVkCxujCLOpKYVmv6-vfXu42bcs39xqe_LlFOedkb8cwJA4C1oNjEHRa2g4swZjNuiO-mvFP5iRragnaZ4fO7VcOhE0riNU-M9_jFDyIM2pwtwYW84L8i1ztX_Dw5dMTydC6ddyyeaSl-V0iWhcla7DJ6Kduuo8hj2GRo5K_2bjwMt5ht-30S79Ah2_-Y8sBBh_uUBdbXbo10yQBfEhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mxO8a-8GujqmoSzer8bQnlrcv6hcw2hAKD5u89-z4KD3xhlKku4AZtR1irU5JcGrfuqLrKCNGi3qHdZ4eAuvORGRU8h_WTOLLdcVBq1Ty1mt5vA8l2VQbvBt6ajEXdFdALLgVfa7bf1vgcfIbvnnftWjaRyO7VoW_l3ptXLDzNQyRE1U7QrvuhMcDVlU8cppngSvakCHyBHhYDLg_PdBuxiwVeqMc4KJfBSzME0CSBTXFO2Dhqufm6yO-_LzhqvqUANqlzCcjYGEeSrxJ0M7UUhWF3ojpjEMUTPapaC1Ev5aA5FAWc3FmXx0Oo59XR6AJPNTXOw9ffk85DyFQfv4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ_Jn-ojEpXvWkrVMGw4-oiV5R5f0Zn6gKwLqMun_GeyjuNWFZK_Q6gSmxDh1oeNob_--MVrR4AjlnELlnAVxd3TYz8B5PycrbksUFMlEHbfdA57dLx1xzLvdBIy6RoAD5LGf7-AXQJrXvh651rqkdk9c8fsobuhC3Qk7G4xI7-A-PLSXKzWc1kYM02E-JYsAiQTY3sNcquwnxdnVmfVFtIuxTUrz8j5uWGJ0OgryT5e2QjtfatOjHoiIQ7OlIqh3FqfWSlLbl5E0cNUwGe-OHKfvPsrcdwHKBPrHD7HPeonAiXYD0OzmemtfpHUsipYM5mMGhYU60Lya2kt0amKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز
‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های رادار ساحلی انجام داده‌اند.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5743" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WRxgS9o87uCR5FXqYwPiOodoV-WWBjnkAi21Z98yzktViACL3fqL3caIBYaI9OVFN778QZQgKtST9l8mChVsmp6hsXH3hXnezjNcXlPCwpo9ECcTF9q6b85mwL_sIasd5lmrkogt4-pGoXRnGcd2VzPdzMiKCj8LspMtcpziroe2PpHwQZxHyTCB-gcdXOGeZG52eW_EYlL5tB0TJQxb1ZiGVGex2xotfmXBgPIY8wwqIoCe21WIayeB3-gby4GAgH3Nt8ankEvBkp1LfKIo18z3xZ_UofowHqr9C058TskMekKaDO2A1sInGAgugaql0FXNmqynu14GirZjEYvD_Q3btgsKv8M0QEz83hFXQfC5Xfl73xVbm4embUpIEzVXiDIPVuP62S8_9w-biqB5QpXiGghTLjpL_10ErfD70AO5UHNI616Xr7n78GFjpyuGpyL58Y-qeDxUDAdbLsBu-nVZsjTXw55wwLYWi-JNqSTX7ZEQ3Tux6G3GD-9jFpD1kbGMatPCOVCwcozAmhFMO6pQM_0URG89tmIZAqTBbaph2Bxpo7fJyI5LzUK4mv7P9aZaELuSTt4Y8DR5Jrxblqx1BJuMLKa3_ks4t7NGpvpDTuKRC1rYG6EEPxP_iZXZrqr5101x6GLiYGudNw-YYf-USFGjriQHty3q2FAwols" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=WRxgS9o87uCR5FXqYwPiOodoV-WWBjnkAi21Z98yzktViACL3fqL3caIBYaI9OVFN778QZQgKtST9l8mChVsmp6hsXH3hXnezjNcXlPCwpo9ECcTF9q6b85mwL_sIasd5lmrkogt4-pGoXRnGcd2VzPdzMiKCj8LspMtcpziroe2PpHwQZxHyTCB-gcdXOGeZG52eW_EYlL5tB0TJQxb1ZiGVGex2xotfmXBgPIY8wwqIoCe21WIayeB3-gby4GAgH3Nt8ankEvBkp1LfKIo18z3xZ_UofowHqr9C058TskMekKaDO2A1sInGAgugaql0FXNmqynu14GirZjEYvD_Q3btgsKv8M0QEz83hFXQfC5Xfl73xVbm4embUpIEzVXiDIPVuP62S8_9w-biqB5QpXiGghTLjpL_10ErfD70AO5UHNI616Xr7n78GFjpyuGpyL58Y-qeDxUDAdbLsBu-nVZsjTXw55wwLYWi-JNqSTX7ZEQ3Tux6G3GD-9jFpD1kbGMatPCOVCwcozAmhFMO6pQM_0URG89tmIZAqTBbaph2Bxpo7fJyI5LzUK4mv7P9aZaELuSTt4Y8DR5Jrxblqx1BJuMLKa3_ks4t7NGpvpDTuKRC1rYG6EEPxP_iZXZrqr5101x6GLiYGudNw-YYf-USFGjriQHty3q2FAwols" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E631Ba2oJyn4-mc1Zwv5qWkpowRdVq1Ukt6at-iFXrauh3dZ_Xwp3lsKFRbLfAWleQHSumQuXNJh0br_z0xY8ns0ElNPOR2McpShPCR63BFqJUQQGskJkfvQShbeK6Ndl4vU9nxThnEUG1u_I2FR3Kf-FSL-y9xXftktnVhpK8aOc0YmRjgz0CwMf2knn1parmkjNoeBveSoXBEt8UDlBC_0Liqy_zbFjTE15I0paRcD8nbov10Q-sMSCcqs2bIQJjVmq_CBn2A3weBoe4Hbxg5aEebVv6jfx0KNBg0X3w8SYN2g-EAjvpKg-uo5hkt7b7nOda_tHjG6v_mw8es2tlYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E631Ba2oJyn4-mc1Zwv5qWkpowRdVq1Ukt6at-iFXrauh3dZ_Xwp3lsKFRbLfAWleQHSumQuXNJh0br_z0xY8ns0ElNPOR2McpShPCR63BFqJUQQGskJkfvQShbeK6Ndl4vU9nxThnEUG1u_I2FR3Kf-FSL-y9xXftktnVhpK8aOc0YmRjgz0CwMf2knn1parmkjNoeBveSoXBEt8UDlBC_0Liqy_zbFjTE15I0paRcD8nbov10Q-sMSCcqs2bIQJjVmq_CBn2A3weBoe4Hbxg5aEebVv6jfx0KNBg0X3w8SYN2g-EAjvpKg-uo5hkt7b7nOda_tHjG6v_mw8es2tlYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین‌ها رو یک تلویزیون غربی پخش کنه، سریع میگن این برای اسلام هراسیه!</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5741" target="_blank">📅 19:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">ترامپ در شبکه «تروث سوشال»: «جمهوری اسلامی ایران دست‌کم چهار پهپاد انتحاری یک‌طرفه را به‌سوی کشتی‌هایی که از تنگه هرمز عبور می‌کردند، شلیک کرد. یکی از این پهپادها مستقیماً به عرشه بالایی یک کشتی باری بزرگ و بسیار گران‌قیمت برخورد کرد. کشتی آسیب دید، اما توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این اقدام، نقض احمقانه توافق آتش‌بس ماست.»</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5740" target="_blank">📅 19:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=I4F4IjSFU-ZtYkwUzqeoot4a3C95ZEsmB_LVD3WFsYHDpUGeFr3fiO1m7SnSk_NzV6yW4ucsg_pHA1U9Up2_XH7y7snq7s1iMkYsj6p8JGqHPwmFXBSLtjwFmfb25YxPao26vp27uLsB0JnSNaDU8-fNXActZqHyOX77wc413pvo_PzVJG81XIaxEL7dvqoN3AxGdlqCCvNHoyGTD_EhHCTGx7kyFemkrPrZs3xPyEH7e9DG3u_XJo4BVygSQRZLxW9FiyFLA2RryZkJisEeNoQu9fNh-ltyo30hMx5IOyju5LESN80myR7IVgQ65smxZnnbW4vKM5oRxtuuIOB9-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=I4F4IjSFU-ZtYkwUzqeoot4a3C95ZEsmB_LVD3WFsYHDpUGeFr3fiO1m7SnSk_NzV6yW4ucsg_pHA1U9Up2_XH7y7snq7s1iMkYsj6p8JGqHPwmFXBSLtjwFmfb25YxPao26vp27uLsB0JnSNaDU8-fNXActZqHyOX77wc413pvo_PzVJG81XIaxEL7dvqoN3AxGdlqCCvNHoyGTD_EhHCTGx7kyFemkrPrZs3xPyEH7e9DG3u_XJo4BVygSQRZLxW9FiyFLA2RryZkJisEeNoQu9fNh-ltyo30hMx5IOyju5LESN80myR7IVgQ65smxZnnbW4vKM5oRxtuuIOB9-Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=lyQ7210aLUiCDqaRxr9I8PyRXCphSFftMinaR9U63UQ6xbUivxnJLvx7h54WWdGN5i9CjeTttAMA4PZTEJMHnb-F4GYTBGkttDE8hU4OW-8nDkhOYx-ryMc5yDtfvsjYtAjkwyLdNT-wK1CLhF6xjGLUTiyIIqwBpFWbOK-Esn4Xv7NsSusbViGV6M-UiD7Um-cXe_yTlQdMqPfhL8beOkosvRAs6eynhiK85suJf4xKEBzoJnwbFSD4JVc6hSNaFoM765aNzC2Trsy2B0QbUVf2_Tk7XJztxGHNixAZXT2dYNlcd9GdrrJ-sAEb1EdB0tYZlxQKnS_l8HiCaQ4dUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=lyQ7210aLUiCDqaRxr9I8PyRXCphSFftMinaR9U63UQ6xbUivxnJLvx7h54WWdGN5i9CjeTttAMA4PZTEJMHnb-F4GYTBGkttDE8hU4OW-8nDkhOYx-ryMc5yDtfvsjYtAjkwyLdNT-wK1CLhF6xjGLUTiyIIqwBpFWbOK-Esn4Xv7NsSusbViGV6M-UiD7Um-cXe_yTlQdMqPfhL8beOkosvRAs6eynhiK85suJf4xKEBzoJnwbFSD4JVc6hSNaFoM765aNzC2Trsy2B0QbUVf2_Tk7XJztxGHNixAZXT2dYNlcd9GdrrJ-sAEb1EdB0tYZlxQKnS_l8HiCaQ4dUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ikty6krhTHB5laJmVq96E5dYro22gQ6YR8vwD83s913DAqfeLPOnoA926N2wNnC_vWE9Mvi8RfV9aYY8A5hH8cmTNfu_dfuA11wN6i2avPWppwWJwy85H3dMIV9xTUm2aqgnKeKtBLiF89lnhOWEEpYzpBNVuJffnsVatQu_500t-1tPtPrpGHYqo4nXXh942pmfw8AmGqDB3w8nkcG8u1ykJPV40QeXG1na9aoAblww-pONPP7kEHZcFzQLKv-TqnLsPBNiwevBTqcvs4INppXmV2mZgt7osRY2S4LAdvIKgD8dPAG8RZqNPEmr2CO4btNj5FhZh7c3mgO4xwiO-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tauOpLCnRtpMkBF9bc-_FDRZioWzSiXQFRV4nje3VhPDz7U2Ud-i6fnjdf5Ry9wxRthIZRaF0pqJsH-k2zTHhjXhNsY-SIY3JIu9951n5GdJiMQcoewp6VaPBRSuuxv4JQL6r3ExVjaND6tzce1D6R9xlkDO-3XIe89RzlsFkMw8G_GhReP8dUDlE9DadoTzgfS_LKEO6dlVPAH9IbFg2qB7GVvfPBoxSE5BUqSki_j3tUN4E7pOv_7E3ggNGVOwOumeO8Za9Uq5-u43qWkL9xzW5aqrD4AZ52AGn9JL9eDhEYX2y6Saue-t2re9g63tl7TG8pB9ek3NRHQ6y4Stxw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9DUhPVtrePjuJSejRh3fZYEt2cvMCQX4JcgvPwv-lfFAcP13qraXxtvgZRS4TYFMMQVnicYrPVB88nJSrSNjuChNE5-VUbieDBXLzpfV6mTFfdgcBrKMS4RZCK6cnoRzUSKK1EBDDGNSOAFHtbISEtzK9Ku8LAgOR40clTfjSFjMXFHOiiVlBHpphe1v-5CSKPBo2QFozJsEMivppPUTEcNQiR_nM9pofRoSC94dNMD8G6l0DdMrfZl8SIOuLo7Oidxt9Cl8l9imr8qJ6i0zrEiaASvgOry6swtuv2Xxe1QGcjwkkgIdUxfkco8u66AuWFSWY6pfrQKScXn957FRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0CoVv9Gd7GJzoBvahjCeF5-02Ce9agKtqJIGaK9Oo3HRfCTRfVygAHQCHZT27VQ_C73J70qZnlMXbVilMUhdz1R4TmMthSdcaXpm5ocdOEP1e8vX_N4F9xXNmo7Z1tTb4hpVEcP66VT_Kr_a1osx4TCkPpi0wdCLTKE-RkmaAU0EuT4VBZkoXE6j2y40LkKKg0bVr4Y7nLNfkplpPCsTzluHauuQeVyl1G9DsrScGE4Qz8cNCpI8CmMgHaeGiIlDTK-cVFeDZqMQwG1w0CtP8Fe_0qGrE06a0Gb0zPY8AQaKME-UPAwy2LgXUcab7q1ZQr0BcuD5V4yHvb31NrJFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VAuZML2k4kNcOTq44YdpxJHjnJlOOQUa1BXpsfLxj0f3T1nVvEk3WU3M_ORoPllu9baDZ5lpmItGIYCQ1GouN3ebidPPLfMEziZfPh3bau4ij_oqSdQKFYuwzj86w7lb8-uTOciXNFiKq2_koABvWPeqO1vpAU5qt6SHXR8pW46V0xLyAWwA263BQ5NjGKS7bxm4_f0TedR_WY_t_65IngmX8nZB81VLEnykxUoHUjLKHxe7YwrgdH6jPphmSSUCp2fufiOl68FZ7mTuRaQA6XwtZAd71JJlFVZ_JeS4gXWo3BKt70M4FkZpakCsm0dA30gkWshWCvY8rEhkGXGNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=BN_SYWoaOAWa8ixgBhRqXfiGUCepaZ1Oj2829_2Qp7FJ_SMx1-cn8mV-15Y2T1tUIeuQ51GYLsOgYSJyvtcVrKb7nY_Rhfpkc1C_lEO_EyXglY4hNs9D3qcGo91tybmX3rUaIwNJJZpWW90Oi_NwfEk-Bfg7G1mF2vBqbsAP-pWX4RPNAeaP-Wqjd5ZcjJ_Pk4_4Dc9c6zix_9DnqAyUa_IzlLqORI5Xsv01MnQdATWDlNrC8Hkpn6nfqunSCq2tGmmNp1tWoDtBTd0j6kWogiljPJ3fenm5UBDhjD07KXLdMR4GLzMKIJBJE3yAwHMHreAiENhzwtLT7NGIJEg7vQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=BN_SYWoaOAWa8ixgBhRqXfiGUCepaZ1Oj2829_2Qp7FJ_SMx1-cn8mV-15Y2T1tUIeuQ51GYLsOgYSJyvtcVrKb7nY_Rhfpkc1C_lEO_EyXglY4hNs9D3qcGo91tybmX3rUaIwNJJZpWW90Oi_NwfEk-Bfg7G1mF2vBqbsAP-pWX4RPNAeaP-Wqjd5ZcjJ_Pk4_4Dc9c6zix_9DnqAyUa_IzlLqORI5Xsv01MnQdATWDlNrC8Hkpn6nfqunSCq2tGmmNp1tWoDtBTd0j6kWogiljPJ3fenm5UBDhjD07KXLdMR4GLzMKIJBJE3yAwHMHreAiENhzwtLT7NGIJEg7vQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=jBJAfiZRVFX3N5qYcCWp557AblOMjRQiGxNxhT_qo_5joKpFYtetRY6UZC8wUrqYZoaz4aXLajgip4qg3-XcLLz02TSWv1u0siIfBP-klnk2E5nVoq5itsUqMCvfYciTjTeq3-VtCijtJYpi0iN5DHmRDCs-LLChtsHjVl3fboWqlMEx93k5r85H4szctAC59WfELSY0EkYNf3BtnUoKclkvF25ViyaBgQ-FWCkqPwF5PcHVj7hJ8125oHTxbApnnF8j-YVA8cU_lulKaSujQ9jWSD3uuSwwnYnELXaFI4xOagRcpRWK_fbpBlU1ItA4MVLiWLrdZmdx7A4WHqWTiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=jBJAfiZRVFX3N5qYcCWp557AblOMjRQiGxNxhT_qo_5joKpFYtetRY6UZC8wUrqYZoaz4aXLajgip4qg3-XcLLz02TSWv1u0siIfBP-klnk2E5nVoq5itsUqMCvfYciTjTeq3-VtCijtJYpi0iN5DHmRDCs-LLChtsHjVl3fboWqlMEx93k5r85H4szctAC59WfELSY0EkYNf3BtnUoKclkvF25ViyaBgQ-FWCkqPwF5PcHVj7hJ8125oHTxbApnnF8j-YVA8cU_lulKaSujQ9jWSD3uuSwwnYnELXaFI4xOagRcpRWK_fbpBlU1ItA4MVLiWLrdZmdx7A4WHqWTiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E9s14rNV_fJFLYyUavcuw0ER2HQL9RL77M8LvEy6GruLYx3Vv2w3X7oRYeFYrnpo3WvtbZt1-pYDxwmri0PMr3sqkmZhbmuULRl1pzqTTZKOCyWfkXF5qpJHdcVz-rCPTPx_0HbReoL6qGAi2qKS28Hr9SH3bvmD_pyhtrw2fJrTBBxH-7sNoV5QKY1pdwzbbi10Hkx6G0dJOmX-FxHGfDeVEqS7zQXuDNQIFCCMWPa2D5YoPA3M_ux0mCWVKM6pD7W7QHoeQhSJEj5AXQNnV7uEa6MZ_iyqYOeHM_joqHjihyg3FY06VI9m1iw24OyasjdpB_mPMuCHbdHQ2bjg3Q.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5728" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
یک سرباز اسرائیلی در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5727" target="_blank">📅 10:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2ruTLPyAf0MrB5QC-BFKzne5KxPEATfx-lU_Gau9tZefB6fbQwkBRkGA39lvfL7NPKKe0KeOVDXCzx3LKQfwGUncxiqnZ1y2FKc1UgfvpYMvguzk5sPWqGer2pm6ANUW4JZx7CCjSpI4zCr5uob-GBNisgd69rSpVoJ3B-xmXyi1ZMB3qYOvKmmKJ8wKmKdfc0jD8URr0jLHzpU4VZLe6yGkCfHtdt3HTPVRWa2rLz2KT_K3FlLMq4eh630emQRDQYX7Kgpb2r4Gi54XXKlS1Ar0CnwR69oMt-SaXk3myIDYqGjkvjoWUpQ3RDahJafwUGZxncCwQQZd6ehKhI7tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=giCd_pwc2W28h7iDYeWTEozUvDrHJz6A4q2Wehht6ruAZM9L5oPJrLAryoOpPGPvczYug6eAH5Q-U9cMs9WNpzPdqXRnR3E3Y9vKCntdTVUlCyUOl2Srvk_8pRZr63lPCgsEfa2jAJIUXDSZwnYXMYM-ydaUo3IonKkoyim2-sMqcXvIK7sFAftjDnY9Qp2gi1Z9Gul6_YtCNiK0Lr7taRUWKggn1T0PTr3aMewOUBdbSSpDfqx2lq8CLo6w-yPWKQ82vSNVGtBZGraVe5Qn_8y2xCfpJiq901ySMKU0UTNfS0RJDz6tOt3FXzCw2XUDEDv7sSStSgkAgxFqyq7PLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=giCd_pwc2W28h7iDYeWTEozUvDrHJz6A4q2Wehht6ruAZM9L5oPJrLAryoOpPGPvczYug6eAH5Q-U9cMs9WNpzPdqXRnR3E3Y9vKCntdTVUlCyUOl2Srvk_8pRZr63lPCgsEfa2jAJIUXDSZwnYXMYM-ydaUo3IonKkoyim2-sMqcXvIK7sFAftjDnY9Qp2gi1Z9Gul6_YtCNiK0Lr7taRUWKggn1T0PTr3aMewOUBdbSSpDfqx2lq8CLo6w-yPWKQ82vSNVGtBZGraVe5Qn_8y2xCfpJiq901ySMKU0UTNfS0RJDz6tOt3FXzCw2XUDEDv7sSStSgkAgxFqyq7PLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ میگه جمهوری اسلامی خیلی رفتار خوبی داره با هر چیزی که من میخواستم موافقت کردن!
باید هم موافقت کنن و گرنه دوباره
برمیگردیم سراغشون!</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5725" target="_blank">📅 22:56 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وحید اشتری، فعال رسانه‌ای حکومتی :
تنگه هرمز شبیه یک بومرنگ برگشت به صورت خود ما، در ۴۰ روز گذشته حتی یک بشکه نفت نفروختیم. از لحاظ نظامی توان شکست این محاصره را نداشتیم.
گقتم تنگه هرمز میشه تنگه احد براتون!
به هوای غنیمت گرفتید، ولی فهمیدید باید دو دستی خودتون پس بدید!</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ATWMSSjz3R_6X5fXKg_ti7J6GMZcF3brq4lRUIJckzrQZVVLvLfGtCjA6ndwhswPc7yxsrSAL3okasF2E7wrM7fp20r9BmaFyWuKJTHLYGEkcSftSKI1aTaO5X6dJM6SWLtImIBar-g_HeanZ5FbFfOVZ6eIjLLy81204OogjvolVoAdza1Wvdf4x_0G_GDdzn0nehRaLmlUCBC7FLU0DxnTdpwx2g_ovxU4oXNEJapBgjcHILu0Ks7OMa0oRYuLG8GMKtoYTmamsaQhDwws-W9BaJIIyRyQ4z70CLO7fO2FuO8EGT6HWTpAVhtdQRqQ22g5-E9B5DbTp6EHiMoBZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=ATWMSSjz3R_6X5fXKg_ti7J6GMZcF3brq4lRUIJckzrQZVVLvLfGtCjA6ndwhswPc7yxsrSAL3okasF2E7wrM7fp20r9BmaFyWuKJTHLYGEkcSftSKI1aTaO5X6dJM6SWLtImIBar-g_HeanZ5FbFfOVZ6eIjLLy81204OogjvolVoAdza1Wvdf4x_0G_GDdzn0nehRaLmlUCBC7FLU0DxnTdpwx2g_ovxU4oXNEJapBgjcHILu0Ks7OMa0oRYuLG8GMKtoYTmamsaQhDwws-W9BaJIIyRyQ4z70CLO7fO2FuO8EGT6HWTpAVhtdQRqQ22g5-E9B5DbTp6EHiMoBZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0VWm3r5SD4JCe65sqWuq0L4AG5-Bwg5tAhFuNryTiTQVhJWwqAPGKANPXPgOdbTjVdo79E7HainxKHzRoJD8hVTzyEZUkrCCQwTusMVHq-B6gvLxjuXXdzPyRvsC-bGoDj579LcRUuYhxaaUKeRBPROIcU_ZlX-D9H_Q4Fg-2KYx4-82OKuxL0-3wLL3jbdhMTiy8jH2fyYalvHudNbW82-cskUjBJGUl6Jcs7Pide0lSx935Ke-bvwjj2lgCt1YEvamra7YR5pRugHB6Fv2X520ASEX2rn54ufOc7yFpQ_rjYcvBbgA_KT72GISMjYfYSBfq8WODTZt17YY8n0-g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5721" target="_blank">📅 15:52 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5719">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tyj3hUg5By7NMMY0TYN7csxMPYH52-7y0krwerk7qXCuNuUkS258i0Q5e7uM4FB3dGSVR3wM1q_ZG5sa5mxjm8acyyU1GEX048eDRLukx4EYI-EfBwvsghLHErTkXm7DKQUrRt8Z36kfYTIdkyPRr5zNkt_32WlyfptmeiOkpK-UOLL1LTFjFm0jupYTMN2Ci43tG6rZrVWlWaclPM8vXiBarNeN8GbwuCZ4WE_Tm-gapL_4ZJzhnu_1fx-L7UTY2f2viIPch6pkSsHy5BWv2Y2gKTyySFljwRUH-8h5xwGScTwkF0bBr3vRZvrKP5IvncE_BRdvdtKSkFK0kq9Dog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hk3RljMd-7UrOBOnFWxprN329jBH0LJpq2TutZwD7lz9L-qDgf9pTVxLGH3oMDyvQPQlWpBQqMGLDN_pfw4HwJwDl-xx_5Z2nefWz3ZP_nFEnuIf_lgqeCYbZS73tpH17kCMx0mHQIX16H95ysd0xrU1PYUOcVpo9aMCjNz79EswZPNg4Pc0dEydPagBfgQQoSZZmce4eSRy8vukguKOXk89xA3mL8LH2NfPmI6XJUoaF6qEz9VuQutztYH8S4oPIYEeeDT2RVtHt6epKeTtENQEuZGU_eiP_jWHuoDX1pQWSuHuH77pLut6ChgCvncZXOjtN_BzFar2xBFkeZt2ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز تولد «آیدا عقیلی» بود
آیدا ۳۴ ساله بود که به دست جمهوری اسلامی و در جریان کشتار ۱۸-۱۹ دیماه به قتل رسید.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/5719" target="_blank">📅 14:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5718">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">‏خبرنگار : اونا می‌گن هیچ بازدید برنامه‌ریزی‌شده‌ای برای بازرسان آژانس وجود نداره؟
‏ترامپ :
بلوف میزنن ، ۱۰۰٪ بازرسی رو ثبت و قطعی کردیم.
‏اگر راست می‌گفتن، همین الان مذاکرات رو لغو می‌کردم.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=hv9jSFWKWpwVw_FaXu8DVh0OX9RX0sY48BqSwIKIwxURwNQfQhP-qW8M14TqDWRxYsDgHsxNuVNOcp2owL6L8qMWN76oNWI8uB3rIQ0TBWz2zHFkJZzwAKm7I1IuYjmLzU737uPND2wCWQ6kgdnm1m-2FspkU2PdvVpGjCgeekPTrmrxJzd8vDsPfdFkuZ5_FevgoQegyrrXhucV84C0AnUXnpOHVVf6xptxSEFC5N-s0tnZ72Ae0uWTDDRWScPJoV4uP61AKMsLigrEg5qfyCLtKmNnaZT8sp3VmSXSAb1WhdJ8idNwDbi2esZLi_qSmZD-HwIDLY1LMymF_bwYxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=hv9jSFWKWpwVw_FaXu8DVh0OX9RX0sY48BqSwIKIwxURwNQfQhP-qW8M14TqDWRxYsDgHsxNuVNOcp2owL6L8qMWN76oNWI8uB3rIQ0TBWz2zHFkJZzwAKm7I1IuYjmLzU737uPND2wCWQ6kgdnm1m-2FspkU2PdvVpGjCgeekPTrmrxJzd8vDsPfdFkuZ5_FevgoQegyrrXhucV84C0AnUXnpOHVVf6xptxSEFC5N-s0tnZ72Ae0uWTDDRWScPJoV4uP61AKMsLigrEg5qfyCLtKmNnaZT8sp3VmSXSAb1WhdJ8idNwDbi2esZLi_qSmZD-HwIDLY1LMymF_bwYxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm_-EoZ4VerZ9zchbzUzF8_8gMcVGQuWrg4nodBjDuhC2CAJA1su_FmKhyHd_OTmIm4i9lODtaBn9YeCDFak-LHE9VITcZoCvgjXz7xhcoXTs60s9v4lpZT8jVE6iZeEF5cg6mnqRjQHfcQhseM7wWVhqB7m7U7dLsDTpuygugJj4uUzI4wPqNdii6md5ONHGwu0oiYVaUNzQZ0iiKLEhT0UARlayml-OXu4NHNrhSqg0ome9kNEufI1Pu8tnQgdll-QxaPV792XZ8wUXB_gOScteq1UTVxXIRaJE-9GA6oC8BxkzQ42hPOz-1ga4gRaLNN1ejmgeC967OtcyW5vzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPcCJskSXbwE2fhmC23JE1YQBYQ0KN7cJwn1Gr5Q3VSiC-lyK8HN1Cg3xqC6n_4eeUIDvbwtlxJB379Ql-VS4HmHswVcl6P7k0cU4qtk0mItnsyXKRRi3PYIQe5MqB8HVWnx46cvJJhT8B0iN-PhCWzRtNHXmpinxmyJaDpSQTc0Zexb6ooEi1V_8ksURBKMnY_QHESxplNwr7-rTtFzxzQXIjQJt2oZPe1cEycyQFSBv4cg-qzD4L6foYShGQwqgWJdQyP4ksi1KGJUnc0laygLoCOKgz5vOfNLyAOuXVtIkXzK0TQeB7J6n-hQfK_h9fOEQ7cgLBAjD6aOQcRBFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WHOMlGdPf7BGeW4KCX-Go0tNE7fcOtjgOKaXS4tuWYj1xuPrVoVmoO4H4yguiOq0ekZaDTlqSKc8dvFjyFMn7sUmm7g4cERC1BZlFd17mgXjBf0XzjpOtf0xl8CWf8shomdDz5LlvIYrEkFVNbpTZSdJf5JXUhrbfQ7BFrUxjIIvFk5CgH8t8r5ni4ChGxX3wrkU_sBnb2kDVk4PNK85EsR35EfgRly_ZQCFI7JESBV7ZjWUZY7e0Yb_azbR5JlCcSyHCTiLjFrmzohqE6MuN39kJ34cvQ-JdHsDl7VVxFs6Fw53oWngDFMYAZmK6MyCN7SwkgKnIUh7OOU4QLvEzw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/5713" target="_blank">📅 15:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5712">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ :  با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها، ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.  این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5712" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5711">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUKx8aoYz6SyJjNGPTqKvzneH7zOHiBloKMvDRNrOA5SBUHLk3xEo5Hyge7P4Cvd5W7ts-4G9_3al4Xc96EKlsX17IqDHQ2OSdPAKv19rXYwYBF-LG4ku8LZ9x0Id6UjPK4v1ocmCLot82SXlAyURq0NSprSAXyDz8wEU4pDYGM91Dgzsqs_jtUr2kq2khGkVLj1cTHxa63QVwsDFuVHPNDHruVvn63OBdrL_-SaXwO06YZndjcpHCPcLsl04F18IJxK3eNwCLV5AVaSRFdpxjSp0jCOtAwH9r_Z4-iBMTfHvtwpOD4d3if1jKsyhgqmfXYFhcfnsNzTWA38sDDEfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ :
با وجود اعتراض‌ها و ادعاهای خلاف واقع آن‌ها،
ایران به‌طور کامل و قطعی پذیرفته است که در آینده‌ای بسیار طولانی ــ عملاً برای همیشه ــ تحت بالاترین سطح بازرسی‌های هسته‌ای قرار بگیرد.
این موضوع «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این شرط موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد.
بر اساس این توافق و دیگر امتیازات بزرگی که ایران داده است، من موافقت کرده‌ام که تنگه هرمز باز بماند و محاصره دریایی دیگری اعمال نشود. با این حال، تمام کشتی‌های نظامی همچنان در محل باقی خواهند ماند تا در صورت لزوم، محاصره دوباره برقرار شود.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5711" target="_blank">📅 14:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5710">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=dlpNZ4a0c5bZS_ypkl5SF5FIZmtjuAxVUS_T9Kv1GqmhP2Wsgk39v_sDcX99AT51xB1n8t0PQS3Po5og02gdbH8mkykgH7DMwWMxf46gTvPLNANBcrboyBOM94VxSuCULMpoUjLopWdul-jgZwtl-Kf1GvpdVlsVvL8gK2Eh4txjGvkq7kVdpFxs0Q4gx8kA4vgs_HP5vbdF6NebSGMm7pUl4p_pPqRH5jPiIIapJGum3H5r602Nk3pxgTN1zddDdv9ue1pfE72tiL-MsoQ49d_V35E8lTikc7bMKvcIV_CSOisM4lDdfnBKgsHWyghhB93CSaOVCd14UjKlIRXzmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=dlpNZ4a0c5bZS_ypkl5SF5FIZmtjuAxVUS_T9Kv1GqmhP2Wsgk39v_sDcX99AT51xB1n8t0PQS3Po5og02gdbH8mkykgH7DMwWMxf46gTvPLNANBcrboyBOM94VxSuCULMpoUjLopWdul-jgZwtl-Kf1GvpdVlsVvL8gK2Eh4txjGvkq7kVdpFxs0Q4gx8kA4vgs_HP5vbdF6NebSGMm7pUl4p_pPqRH5jPiIIapJGum3H5r602Nk3pxgTN1zddDdv9ue1pfE72tiL-MsoQ49d_V35E8lTikc7bMKvcIV_CSOisM4lDdfnBKgsHWyghhB93CSaOVCd14UjKlIRXzmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8un-R81R0y6MTU_xOcFZPv8gjthy6nXhsNVHtuE_FUzY3yLYKTO3PfP2oJUgODxMZKAUPAS9OiEDfp5yqvuB4QE4CGkUF5b2gDBuimoDDWrt2JJ-ZRCSuqE5nluCrLoPPnuZfiB7UHuu-LWKeVqxBmqI51GambhefC0DDbyoxnSZ6uSENJ3ur_j5njebcI23cv3Fi7EuhI9vp0o0n_H6Bh74arYxqJhvMYHj2cUq1bSRJ-jgWoRPg7XnezdJFaxpnJFBfraIjV-5j5WSzSmeTXuqRzAUbsK8HSA8CJPnjOQDiUj2JeEPVtCL125CsoeuVdZccAtamCSm3fk8l6x3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iIfZAxxs0C-ku-c_NuB8vHqmsmvpyOPQrFss6vO_6PKjVGtlh-MvV6tVdjAg9VJr5e8_Uw7PXzSRlAbXj7qZdQeX-iKesh7Da0IG2oLpXIhJ0KjJmXnaon8tRxW_mJNfVsJNAS3Kl45KFM0hESvZWvW2SgXKNAOuGqbRqFruW42k7ZwjcDJ6uz3-Hy73pogF32pKsJUeIMus0fTVHZCFlfp09HLMkkhl1dDzKpaKt3tGraXLayZyD660VfLHk3p6oXQG-jsFJgApvqrDXJuYS4jzRjLMU_I1EKGbjyS9lT_6T9SRafAXUI-huZmr6mRrh3W4jvV8VoGmTjk43C6Pxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZR6bgXBu6Beuw21jcbnGN8XCzISG6XV5OME7VST6u-LyIvaMEhGZIJIHtC_xNAns2XcPJaFNAVUYHpZ90cPACVKCySaIKyTgO5FGw1-RAvjIq_i2dX7SvVgJw8W2Mn7netaAlq8vEpcsgePLucZz_2ZvkikT9Wqwm5NBLPeDAaBbi-Uh8wwe9Nc4x0piRzd7SZH2_7JLlbrqUwCfL8p5K5F-Awk-wW2kkPqsULoKrp35YP5uARmEa4m-JjywG9zC6tQ_i95bZMfb8suWZ1mpb94vB1peUvTdUcpEEmbNhf4YUFleOG8CFtbDfaP2X6GA9K6oM3T9ZQX3RmWtz1kmA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=OjUxXRQJc5mzr9Gq-vXVOVJ28Bk3uKWy_D81HrvxXQudPaE5_maBAU_YmyQtrk2V_6rZGmbXZ6k8tVulf5lWOkAhpudYviruk3IR8UxtFQ0OaT-RgeVQZefkdZrOlJcec4PWhzTkEXoKd-dQByvlrl7rBBBQzVztFeHmIxLynTMJaEz1c0KowyP_vQGaj9_FPi9F-nUYS_OpoSN_R0P5luLqnxIEKGnACEu_LPvUyZlZG-zSrogikMS4HNr7C2AOU3qx9HFCYT7VVeaZwehVSWBYA21Qqzej6x5AHiqk4srMCFjLTxR8x_ZrH5TTAtOKy4Kb_wmZ1gYoUwwGOCi1GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=OjUxXRQJc5mzr9Gq-vXVOVJ28Bk3uKWy_D81HrvxXQudPaE5_maBAU_YmyQtrk2V_6rZGmbXZ6k8tVulf5lWOkAhpudYviruk3IR8UxtFQ0OaT-RgeVQZefkdZrOlJcec4PWhzTkEXoKd-dQByvlrl7rBBBQzVztFeHmIxLynTMJaEz1c0KowyP_vQGaj9_FPi9F-nUYS_OpoSN_R0P5luLqnxIEKGnACEu_LPvUyZlZG-zSrogikMS4HNr7C2AOU3qx9HFCYT7VVeaZwehVSWBYA21Qqzej6x5AHiqk4srMCFjLTxR8x_ZrH5TTAtOKy4Kb_wmZ1gYoUwwGOCi1GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Qnam70Fq9CgwnKA3pFSajQ5mNXTkTefwbPrhd8NE8gSqFyCZszyjidSMoE162T8klm0Y6iyhRAfsduAUCxwBsM1WZa9XfAUOpc7KRMSXMtPEJMHoAc27cpFJLY0Kc-VucskqL9mkZdDI9asfxhaZexo5D77poZWodwlwgU6hI7Sug0gfZR-t9c5d1FIQDlMGV7bwPUkkePVEpi7nJRhH3xKFEPGccGHxj0Z5yUwM81HYkAoDU87z0GRZ88SjzgfmkdJaEPxnD6JoB6C79GoJfFtXM0LEFnuNG0v9Py7YPJU3NTS8z0SFA3l9xdrOYrEZwYI_RecxkAYRPxVn-y2uQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=Qnam70Fq9CgwnKA3pFSajQ5mNXTkTefwbPrhd8NE8gSqFyCZszyjidSMoE162T8klm0Y6iyhRAfsduAUCxwBsM1WZa9XfAUOpc7KRMSXMtPEJMHoAc27cpFJLY0Kc-VucskqL9mkZdDI9asfxhaZexo5D77poZWodwlwgU6hI7Sug0gfZR-t9c5d1FIQDlMGV7bwPUkkePVEpi7nJRhH3xKFEPGccGHxj0Z5yUwM81HYkAoDU87z0GRZ88SjzgfmkdJaEPxnD6JoB6C79GoJfFtXM0LEFnuNG0v9Py7YPJU3NTS8z0SFA3l9xdrOYrEZwYI_RecxkAYRPxVn-y2uQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5703">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بیانیه مشترک نتانیاهو (نخست وزیر)، وزیر دفاع و رئیس ستاد ارتش اسراییل:
در لبنان خواهیم ماند و زیرساخت‌های تروریست‌ها را نابود خواهیم کرد.
🔺
از مهم‌ترین خواست‌های جمهوری اسلامی موضوع لبنان است و خروج ارتش اسرائیل و بازگشت شیعیان به جنوب لبنان.
🔺
وجود بیش از یک میلیون آواره شیعه، فشار سنگین اقتصادی و روانی بر جمهوری اسلامی در لبنان ایجاد کرده.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5703" target="_blank">📅 23:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5702">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=oRlvzR5_7oqyrfh19pzCfh4h-BRlcwP3HApFKXQV2ZnRVODpk0R_f0NusFOiAFMNYBL47uGeWIjsCk1QswzK0K7aySivuYmqXluolFZ5PUIonSXaM88tqtsLTbSg8aJQMfbU2GPZ_dfuLu7PW9YXphJw-BiMq7Aih7dPO24rhcmI7lfL4ZuastFypj9G_1maci4Da2x6SAcgQZj10_Q_SwKubbo3r5FfRuwfWtM1yIMPmr5uEvjbdHmYQIO8vPeubDeS0jHx1wwVas3dOWGjHHENFe70C0QkH9PtyDAgf0tde84pmv5UGLZyn-gdxwUHUTc4ioWgXpK1OVb4BM64Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=oRlvzR5_7oqyrfh19pzCfh4h-BRlcwP3HApFKXQV2ZnRVODpk0R_f0NusFOiAFMNYBL47uGeWIjsCk1QswzK0K7aySivuYmqXluolFZ5PUIonSXaM88tqtsLTbSg8aJQMfbU2GPZ_dfuLu7PW9YXphJw-BiMq7Aih7dPO24rhcmI7lfL4ZuastFypj9G_1maci4Da2x6SAcgQZj10_Q_SwKubbo3r5FfRuwfWtM1yIMPmr5uEvjbdHmYQIO8vPeubDeS0jHx1wwVas3dOWGjHHENFe70C0QkH9PtyDAgf0tde84pmv5UGLZyn-gdxwUHUTc4ioWgXpK1OVb4BM64Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5701">
<div class="tg-post-header">📌 پیام #3</div>
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
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gdVwDhMbYVZDt53FPw9UFXgNC2n9HQbEFwptVF4O1n3DLaYCqHWfWgAcQ_G4_hWqlo24DRNaKaY_C9MuiwFpsxNcbXErLIgWU89WEpaIL009MHAYLs98rZm5HwcIvjsEviXGEDlfbLOSjLv9xfKKISK_5flTFx0027Od1Bxcnp64vkvUJYcqcbmh2RXafEv0eKssiF3dNKfhwtJeSNv7FUw9_gqpohc-UXdmcc04HupNRGMD9gyNxWyMZh3hVTKWyr2kblp2RaGzUgs8liPBa1iDlzW7EcYJvviL545FJqa3WXzL3YZRD9aq4dtcxDLjAWWQYVbmze9vXTfrPnmwkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h-41fDa3EZ6frz6sXc4emH2gCc0-_vwi2vItjCTHAFmd1c6RibUioKbcwygmDFCZD0XUVUrG9vgbAv92yc3ISsCo-WzxJtAZz7Mzjaky1fi8Kv6-hx2HpCAaOmtS0YRn1wiC4E9HY1kd4ghXGTIefgXfEvhIvQnUeWrwPTSWv3OD-4qqUe4RaCPtglEiXQuP02uzWGVJxZ1W554kxHz8FYwucpef68lO3_Kj-IqGnk9PW_6z8_IWVUa6bm2RlkpNndA7GXm9CLKKssXQuLlBbmpXI2TO9tCItVp23sRZFoyMLKWwqzAvTIZ1-aZ45qG9lv5nBfnD7Eax3d9-dBVvGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
ترامپ  گفته برای راستی آزمایی
«صداقت هسته‌ای» ، جمهوری اسلامی
علاوه بر پذیرش بازرسان آژانس اتمی
باید با «بازرسی‌های تسلیحاتی»
هم موافقت کنه!
«همه کاملاً می‌دونن که جمهوری اسلامی با انجام بازرسی‌های گسترده تسلیحاتی موافقت خواهد کرد تا برای سال‌های طولانی از «صداقت هسته‌ای» اطمینان حاصل بشه.»</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5699" target="_blank">📅 20:45 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
