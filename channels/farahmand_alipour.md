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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 20:51:17</div>
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
<div class="tg-footer">👁️ 8.72K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwtalJuI4ISK7IQV7YrAvbHJj4aZpfjdhF9SZnPXUenA8e3JE6VYZ_JgQGbOAe1JK-AzhTyC-u6Ps8BU6bRa-JO1s_WMStSN1Uv7k0F67k970czKZ1Tm98V19lLVw9QRv5st6M_c0-tNi6nh_ibfKOrsdtxJFOGxW6YmxiBJuEa8oozwQrqUZsXwLC1dqMU4371nMe5z6ufR01qgVhDsgJxFeMnRBMvBYgjtLw8w02tcuhsPJbTHlZg0f6pPtYeWjGsN6844T1At9MdsN4Y8i-AwutsrC942gOzp7EnQDrtgr47tQv422sdIF6mVPhHsfqVYxNfFEM0gpUgqxz3tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkPlS5eGMm6Yc2WSpo-utRTSYJ8NveD-Uz_xnXbrQ5OdIOrxaejh4CRYvlbHJijvdWWxn98GV4MadzaLXfnGpTa-prm-wjofhmQjv_pwdLPBS0uIL-6-w4udEWjpNHmXeDi2_W1wBepQswCNwdXVRXlxvmP319q2M8DCnIeZ5381YrzMrIESYlV-3pBN2MSCKLtffFE8GFvQB3MqEiW-XV4Ebomn1ZZP4GBetgeNMsJ4tKrVoPuU9I47u72Deo-xMW5d4YXMiZLm06cBEcoJHFyVGFg_YnWkrtkIbx37p-kmdDJhVdOdc7oOEoqSR5GFelXpdoqukKaWxPAmtAz5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKj_RbNEOApa6XNKCrrK75Gw5e6ZW1EVOpYxKDb6Ux3P_MCLKBpD8crp4tmqBODk0DBVG6X5CrJuMPlligOXIjIUDciCZGi5wMBIiN2oXrD1eezOH5TBeUTDaMamIE-US9vzUSJyExD8-cyxZsXsLI6aDalTb_jzM0fSw69jzDZjlCnxH6UHvUOi743zHiMyPx6y1y5rDgLXs3Yy_uQ3kvKpGXbUPfO9YJEfprhBXxV6a-O611YvPpu5F6USuis8KmI1CYNg5iGsKCT4vqfOx-TJlWFkGqdpVu0aQPksQIUXm1P07_EdDd9XUgLJiYadFvxxCMeLZ-Tp4jpKYEDnDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX_EEbd8ka955gUXa8mjqa3j00ezQAkz8Wd7L1Hn8nEVCuzYntInb8g1G8PB3j6jbX4UYMq1UngMzJnI8rgc3lE54-OZHvEEC7lmVXj9eHTB40f2RWOPjlorBYln1aTS7c-p_wiO2RNOrA7kmRphQSOc0UeJaygPurCnf1Rb67TwkZ50HA1l8eTOYYvvlwCQR7ZpkYQIG4WVmRXAjTwnAez9JZILcbTNSVbzVSyCXsJDd-x8x5-WRr99AUPX3fjklB0Hi9lPLdyzpLvm9Gzs2Vx1XB-jCvs1Sm7pk8JGZla7Rbk-bZhviEfnSZg7kAgCRgsKTOywsOD2TcHt8niaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=UN1D6h4EzNSfbERZERv_pivz4TcBLEEdwVNdhfmGBzlEVOxqdqk5dAhEVUniz8zUFeJjCGjvwFuK_GqM8zEwcs1-wi3pn3Uhccfdz9oKd78rW9zGvuOMOlsh4X7pCoOeGk5oK0-7kLCCZXGFDpNkE6Hvsv6c1o15qNzj960y0NRDy8X4ok2enn_0cyqOtM_-tXapgnX6TlnSAbpX4mKmzRCBKFniSmm45CkYzLz3yExhlI2uzpccmIPpb-l4i_LcDBGv3-gtQkTREf197-ATBmDtlGeTKBIRLSpGYJfze9W5IercC3oDL0SKlyxVOT5jFWFukZcTSbYwFhqU_Wfuag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=UN1D6h4EzNSfbERZERv_pivz4TcBLEEdwVNdhfmGBzlEVOxqdqk5dAhEVUniz8zUFeJjCGjvwFuK_GqM8zEwcs1-wi3pn3Uhccfdz9oKd78rW9zGvuOMOlsh4X7pCoOeGk5oK0-7kLCCZXGFDpNkE6Hvsv6c1o15qNzj960y0NRDy8X4ok2enn_0cyqOtM_-tXapgnX6TlnSAbpX4mKmzRCBKFniSmm45CkYzLz3yExhlI2uzpccmIPpb-l4i_LcDBGv3-gtQkTREf197-ATBmDtlGeTKBIRLSpGYJfze9W5IercC3oDL0SKlyxVOT5jFWFukZcTSbYwFhqU_Wfuag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW2SqDem0543MHEF_k9vw7KaGLkuuO3ykjQBBo3EuSaud0AnuxWTrIhGf5THW58NWaobF6-u7-95mxm3d0Izx-6iAof1lE_ZXtmMj2xwGEwvoIRaUuI-5GT4UQ_77wCCdxU8zFEB2DpM_Xgpwx60rhWZYL_fY_E3gtb6mploWZVex7R253cIzO5UMBLUQ7trEGZxMqLYlz5i7QOP2d4QrJPpzeYpHqAAEiFpnad3reMb1jhykrrC8p01wsCU9qyyNp6m5RFR-LOiFKNo_2hzOQDXBVdh8rY-NekwyMkv3UUkA9MqMmwNLWpmkxOS0_4X-93_XX4eBs1-uNYclbphyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rQajGQJG3xIORQMFllTNi_suvEtbYABOnZz-KuYygOG-jZ1JIpIOyxRGiDLdvuPFKbC2jImUIKEp-bgEGk_6ZW-lcWHerNe04zIFslSj5b0FjSbwHiUT8WAwpf9xmXDT1SF8T5AvjCiKMIe9FTKgqmhHL4SZTC77YmeCD_HkwAjaUPJy4ZEOZzq0rS5fR2Ct3XdLSgcRxN5pFpgNM9c2GLBK_-CmJT9j8qu6ZQnRLeJYe5HX_7EjpbhSuNOtooXNL1GrXdg-IsWe7j4YDMukpnuDOYItn9yRC_Jzy7iYESWA2_7vMDBKKPB_chbFuTaGcJvg-czibP3rbZ2yGE76RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=asozKzb4c_2Rhr-YkwSWtxcI4ODTmZQySSVIE7ZaQsIjVk-4z_7WtXrIEl5fMMK8YpTVMmAB0nz1dCQI2hqkuSffBNGCE2QwZX0eTDxybs9ktJ3j4KYnGI5wvcgSLInsiR76AwbJrKHJS-tf92VyPnuKZE3BCDdV9uzfGyyFNH772k5bOcqFnj786Qe30XEGMQsQncHXPIh5CSoPXqgADEfGLMBOrnna2pmHUBIwQcnWbyqSQfLaxDzt3YLM9_KUXNQJI_v4rinY3kW6NjFYNh0Sqrk6Qgzmqrg9B5km9MZ-uLwdwL_PnGh3JGfiahyNiEv6QYumybNE0lLXc0Z0OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=asozKzb4c_2Rhr-YkwSWtxcI4ODTmZQySSVIE7ZaQsIjVk-4z_7WtXrIEl5fMMK8YpTVMmAB0nz1dCQI2hqkuSffBNGCE2QwZX0eTDxybs9ktJ3j4KYnGI5wvcgSLInsiR76AwbJrKHJS-tf92VyPnuKZE3BCDdV9uzfGyyFNH772k5bOcqFnj786Qe30XEGMQsQncHXPIh5CSoPXqgADEfGLMBOrnna2pmHUBIwQcnWbyqSQfLaxDzt3YLM9_KUXNQJI_v4rinY3kW6NjFYNh0Sqrk6Qgzmqrg9B5km9MZ-uLwdwL_PnGh3JGfiahyNiEv6QYumybNE0lLXc0Z0OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0kByLnNA_L_jdF758SedAo03gtgVi8mltjaJmpANMU53WeDN1_te-xkcQs2G2TUxcL__6CWZZmKzPoOMSJgDSaxXcy2RZJg4BKP2WcLGStIqSWFuPq57yqsZiMxXIS4fIfhgNrr8yGBD3lHfvZ8Pdr2gbLIZJY5TYrjYv6oScugNI9M93-pcKWHwT2Gll47Iy4u9YhWuuEN5XftF2jCjiqsxCVt-XpU5fFemaFwFhbagAXu3ijBOLruzcK-MIWkjO8k0uD45JHu5emJMdcn7G74pICoWasP3rMcjpA7B6MxN63A5j2guGbKu7Ov-Wa2jPQ_kHcwyR64o_7X2F4cPhbc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0kByLnNA_L_jdF758SedAo03gtgVi8mltjaJmpANMU53WeDN1_te-xkcQs2G2TUxcL__6CWZZmKzPoOMSJgDSaxXcy2RZJg4BKP2WcLGStIqSWFuPq57yqsZiMxXIS4fIfhgNrr8yGBD3lHfvZ8Pdr2gbLIZJY5TYrjYv6oScugNI9M93-pcKWHwT2Gll47Iy4u9YhWuuEN5XftF2jCjiqsxCVt-XpU5fFemaFwFhbagAXu3ijBOLruzcK-MIWkjO8k0uD45JHu5emJMdcn7G74pICoWasP3rMcjpA7B6MxN63A5j2guGbKu7Ov-Wa2jPQ_kHcwyR64o_7X2F4cPhbc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=aOhc7EtrzV-02HBjKq1BocnBncYx1SxWOjtR_ubruzsZ6ZiJVAbsjL00YP2ohhKlZyzZZk0gNVaBkYrM1Gn8GpPYb5qn5PmwJO4Q5AyGKHtxpLmgZk65TanwLN9zWYqVqHtadcBJNOibwCKD8M1mmSk3YeIwXC-TgAb2oX-1i_lJiIHGNxn6QPCfh0ghcYZJPUqucbwUhiiEBg32si-CMgvhV5xbOTNLpC1ERqyOimqxbw_j2ZmNepFhoMwGTjgSbDxhw-423NUNYvLHjPykvO3jSUHGF1ARKlrHbkjrE5yj4f4lokbmH0U9gZrE0P49IjH-uh-3fSKQq5S8ZMGs5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=aOhc7EtrzV-02HBjKq1BocnBncYx1SxWOjtR_ubruzsZ6ZiJVAbsjL00YP2ohhKlZyzZZk0gNVaBkYrM1Gn8GpPYb5qn5PmwJO4Q5AyGKHtxpLmgZk65TanwLN9zWYqVqHtadcBJNOibwCKD8M1mmSk3YeIwXC-TgAb2oX-1i_lJiIHGNxn6QPCfh0ghcYZJPUqucbwUhiiEBg32si-CMgvhV5xbOTNLpC1ERqyOimqxbw_j2ZmNepFhoMwGTjgSbDxhw-423NUNYvLHjPykvO3jSUHGF1ARKlrHbkjrE5yj4f4lokbmH0U9gZrE0P49IjH-uh-3fSKQq5S8ZMGs5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2tLILs_Dq6gpnnnBkIp0IuqGRi80ruwERa04hGqlXzuT7lOvyhoVHBq9L8cQ7jjIZVs319MT40WoTcpPwkBllsrgHAvOOr1ksbnT1Vwdi_CkQhlFvnAT3XYncapWx8uuFQvKADCPVxUXNhsKZcKzahZmhzjd62SWxnhxEQhlv2_32ADqBFWqaFRQ4yjIxhwuJpVJrbKvc7Z50IK7J4HcK3hX1sigkdnepZf6g0SRlH30ir0pGe9im4rzZyl1JurE_JszP_2xsfPPqGSkKAN-ShYl8Gfgw4V2JFy1UkupcBoR14FivFqC8LasI0xaIMba1NcGfjW0_4KoEmYdD1uJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=aEyI3RI4oa7OpnqAEF0pW5-_hhh84aPwjXhOrrIGipJ1oMz-KuAYoLrF0V6A1TatWjC6o8wAs7C-Fq0z5-VMGfnf2LQ0d5JCpyL38-WRj-HoueaastHv11nnXQ8JfAlM850ADdT6lUfTiSz1vH0T9lMkVxAu1V9uwXfpj0Stn05JaUe69deXEu6RqEV0rdPGohNEraUJTMsmAgBl7Pc_KTGeRh_US_2cPA3MREwY2gwL-lvrtJ_jvnoYg6T2uK5RpfQPHV7TiiUkpZUc4s1y37KLI_2IMXfz97iwtucvAqLLArPu5SUVkigeexr5uZRwlQa7nuNwO50f6fTnce7wCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=aEyI3RI4oa7OpnqAEF0pW5-_hhh84aPwjXhOrrIGipJ1oMz-KuAYoLrF0V6A1TatWjC6o8wAs7C-Fq0z5-VMGfnf2LQ0d5JCpyL38-WRj-HoueaastHv11nnXQ8JfAlM850ADdT6lUfTiSz1vH0T9lMkVxAu1V9uwXfpj0Stn05JaUe69deXEu6RqEV0rdPGohNEraUJTMsmAgBl7Pc_KTGeRh_US_2cPA3MREwY2gwL-lvrtJ_jvnoYg6T2uK5RpfQPHV7TiiUkpZUc4s1y37KLI_2IMXfz97iwtucvAqLLArPu5SUVkigeexr5uZRwlQa7nuNwO50f6fTnce7wCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=d7uQyulIeSxY2kHgnkXnTj42pVK6OfxtKYwwB_wFk-7MBjaTs-M1m8GJ8ECSP3HckKxwQoif9cfFluxTvq5O7mL8YdFcCQweWXyBIVmZ1ATcwbVSO4jGOedcDu7jj5X28m4AgvHejWwQw6plbGn1XzTuAdq7ADEbfRGXx62yJ557CbSMsO9VYmPs3lWK-Bx16y-7mZwyofmXEkblFzBlXWOqoagIR8esGaGNUmogCANNh12yG0WaT3WquRcPQ3vUITYaumDt9KdJc-lJp9PaPr3D0Z1zjNKMiK_mFZdcnVu1tMeAR_yjTeNpuKYcpv7DuktVJxveMO7gADAWXiaw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=d7uQyulIeSxY2kHgnkXnTj42pVK6OfxtKYwwB_wFk-7MBjaTs-M1m8GJ8ECSP3HckKxwQoif9cfFluxTvq5O7mL8YdFcCQweWXyBIVmZ1ATcwbVSO4jGOedcDu7jj5X28m4AgvHejWwQw6plbGn1XzTuAdq7ADEbfRGXx62yJ557CbSMsO9VYmPs3lWK-Bx16y-7mZwyofmXEkblFzBlXWOqoagIR8esGaGNUmogCANNh12yG0WaT3WquRcPQ3vUITYaumDt9KdJc-lJp9PaPr3D0Z1zjNKMiK_mFZdcnVu1tMeAR_yjTeNpuKYcpv7DuktVJxveMO7gADAWXiaw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=LcPpfydwlo8TieWTJsTubVY-wi4zZp3NG1SZ_G4nUDT2H98azV50o8xzViHWG53brNNte9CDwvb884ng_R-7ma-rhJhZuMkf7Tv0bNy071ZBvdzqVeP8VzTh_jA3vE_EI5tEXHCYaRzfteawhYi2-gVBpcuwADKmtJ42bOjyktGiCRP2pvuJiXlCqzsLfEYjcebmKukTCao54Q1XIbkfs0uDXpAkoRFCd8VbOki0DO2hmBEbKC-hopDWAhx50d0L-TjzyhdIJ9PjT4l4AK6Hs_I-oyVuDVhw1zvbLRQlZMt3b4l2EuC0bIQ8ialDaD_W_Wpei9ls9FHZBV5-V6Zn8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=LcPpfydwlo8TieWTJsTubVY-wi4zZp3NG1SZ_G4nUDT2H98azV50o8xzViHWG53brNNte9CDwvb884ng_R-7ma-rhJhZuMkf7Tv0bNy071ZBvdzqVeP8VzTh_jA3vE_EI5tEXHCYaRzfteawhYi2-gVBpcuwADKmtJ42bOjyktGiCRP2pvuJiXlCqzsLfEYjcebmKukTCao54Q1XIbkfs0uDXpAkoRFCd8VbOki0DO2hmBEbKC-hopDWAhx50d0L-TjzyhdIJ9PjT4l4AK6Hs_I-oyVuDVhw1zvbLRQlZMt3b4l2EuC0bIQ8ialDaD_W_Wpei9ls9FHZBV5-V6Zn8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=O5dn_3AUBn-qWMRidCu2qbbJwsoYHpmAaEvkYMPPXrgH7HOWsu8CHIeuomCy23uJZVWAetkT-5w7ey57t6Za5CteeEOa_3WmR3N3D6bT7xxzoe0XkXwoAp-SFB4rAiollfcF5_pLHOTr2oANlo77Mrr6Q8DxK3-GzNUy7hSxBa4m4YDmWkQaAhYEpi1Hf0sHQMqTwJ141aCONqTd64T7wWwsKeOXSdhsCU7MQWN0KI4_48SOBL8IXto8otch_xgt0c7gLsknj5kpxMvJJZ1qd2ZElJkJCINYDOURCUa6ySru-sarioAUOjL4dCTAmWpkoThn4PUyU0ZxkERbT7zh-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=O5dn_3AUBn-qWMRidCu2qbbJwsoYHpmAaEvkYMPPXrgH7HOWsu8CHIeuomCy23uJZVWAetkT-5w7ey57t6Za5CteeEOa_3WmR3N3D6bT7xxzoe0XkXwoAp-SFB4rAiollfcF5_pLHOTr2oANlo77Mrr6Q8DxK3-GzNUy7hSxBa4m4YDmWkQaAhYEpi1Hf0sHQMqTwJ141aCONqTd64T7wWwsKeOXSdhsCU7MQWN0KI4_48SOBL8IXto8otch_xgt0c7gLsknj5kpxMvJJZ1qd2ZElJkJCINYDOURCUa6ySru-sarioAUOjL4dCTAmWpkoThn4PUyU0ZxkERbT7zh-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YNfMZDaNIfBnOvdwkuE3KDP20kjpnEGAqrfxk5Stiy9nPidRaN34Hv51vwWpdRyu4VasduIA6AH1ZGhQ-ycKIH2_WScOUtiI2UXjHt9cbAn0hZAs_Zg7zSEKj7HeoF2KCSaNsFLrrxbuAtHRhop377z05mZIeY6G6bCdTEddRlf_mhM-TjSQ_0yyxQu5utf9FtvmRFjUaSIIwlqo8TMhClKrfqUGPla6LG9beEN-hyPGPilPOgkCnPAC4eYyBhONyHQvviBO0EHhywBpNslbTzps-Gen_ONxRuGm0i5WrSjJTFkf1kOu3N2VaIDf2xmaOQcq3osXd0Ey0TtmhKOrsA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=ljwK76l35VqywGlAfzpBgWtLAtKoXjvSZDg5Qe5_pX45R5v_xLC2KhGkpOALPthU7XO3mYj5zG1TaRkJeQ8ySEP1H603FaNh924pWMyOc27FYKOS0CWafK2Y_-Nh1z1fd2lyWaV17-YXXLXA0cvMzICJDHbTcGjEM30YAjb1EHnR88o2rWmf0UaFn6n6k-nQFuhQKKWHMeuYEuNlLJqX990hRd7YAbhWRiCXczQLmmO5OqY_KKBbhPA9TbyMUwhckkIJhjmdue2NFixjT0T0eYloxZwQOz0_whmcx-zivJGXcEXzGUIterHb0f6yE7L16qGoUADd_4yRwF2H9UiXwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=ljwK76l35VqywGlAfzpBgWtLAtKoXjvSZDg5Qe5_pX45R5v_xLC2KhGkpOALPthU7XO3mYj5zG1TaRkJeQ8ySEP1H603FaNh924pWMyOc27FYKOS0CWafK2Y_-Nh1z1fd2lyWaV17-YXXLXA0cvMzICJDHbTcGjEM30YAjb1EHnR88o2rWmf0UaFn6n6k-nQFuhQKKWHMeuYEuNlLJqX990hRd7YAbhWRiCXczQLmmO5OqY_KKBbhPA9TbyMUwhckkIJhjmdue2NFixjT0T0eYloxZwQOz0_whmcx-zivJGXcEXzGUIterHb0f6yE7L16qGoUADd_4yRwF2H9UiXwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=OobyKf7CSi3pRbrSsYKcKvJrnMQVuV2K0YjfLnhfFE14r1pu5amFIowXODRCnWtdbm8havN2iH9bTR6HXQad0_7jfy5BxazI2rLzf4iUxQhd8olynrtVRRK7Gvz0UGWoZEhsh76_XPUeeZ07-kNqwbBdxtnJlMyqDT3IRAKWfELtgDXloAFswsOB1tArdZWFR9bhFyqZrHo5Qe43Hkp44Y2s44O5Zcuj99e8reLBqHAcSPwUh5lP8ktGQg1ta1ehgq24EApmVCRv5jBhxGhW3DhD_w0fJrXMZJcZgL1S00Z27K-Kk9F9j7Tje87n0DHNjazpG41evqtgjPj05kjDtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=OobyKf7CSi3pRbrSsYKcKvJrnMQVuV2K0YjfLnhfFE14r1pu5amFIowXODRCnWtdbm8havN2iH9bTR6HXQad0_7jfy5BxazI2rLzf4iUxQhd8olynrtVRRK7Gvz0UGWoZEhsh76_XPUeeZ07-kNqwbBdxtnJlMyqDT3IRAKWfELtgDXloAFswsOB1tArdZWFR9bhFyqZrHo5Qe43Hkp44Y2s44O5Zcuj99e8reLBqHAcSPwUh5lP8ktGQg1ta1ehgq24EApmVCRv5jBhxGhW3DhD_w0fJrXMZJcZgL1S00Z27K-Kk9F9j7Tje87n0DHNjazpG41evqtgjPj05kjDtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YO8K-zT-cGN7hVO8pcKF_aQUPlkUL-mys0WjVn8SrXR3P0GLioed-jmvY5Seor4_6xxGhuniS9x-PQqzx5cWp0tQyeV-LaMCqokaIJ30oOhj_os8bVuYMCh6KWaZP3FXslSSIWsn7jC1XyA3xijbyFjCIymqqIGDiUrZ7zAMum3IV9-8szL4_Wr-0po04OS-WzDhT95xZYFCGSBCLhLYmOmsZxC2NoAzWz2pmt1Gk5ch0Yw2BIZkOdV99glhVkYu9ntAdDVYiKv3W1fRsOk5VsOk96Xb3u7pLoElOjyZAFXxaGaQOKtujGuGsQMVh71BjhFE6qxR0_K57UgrAu6aQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=T94aysEV-PZYFEpg79-BbzWJ8UIN5ywmwm5qxu5AA6V_8vjN_0HAZNfSLvpg6SjJrHR1HyTKG8fwzXncyluEvxxLP_ia0z0V_tE8knTReA0LDL4OP3PTBi5WjxYebXrELfy4WgygP1zbMirYtJrTNoJdhv7L3uzLnYP4P6O5OTlOUBR8TKaMWkzaqt2qv55QTU8kMcHJrRojuXuZnJKeb3bQ2of40FF_pBYEmIOCoBHpJB13SkcO0OgHBbhSpKZsgjBfGeJ0bV_HfeYlFcXGUwLdYjK0zcHO97tmYywUbC3uIcZ99JWxB9KSFkkzAJCf7IpBaUOC6afqt8jpf8biqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=T94aysEV-PZYFEpg79-BbzWJ8UIN5ywmwm5qxu5AA6V_8vjN_0HAZNfSLvpg6SjJrHR1HyTKG8fwzXncyluEvxxLP_ia0z0V_tE8knTReA0LDL4OP3PTBi5WjxYebXrELfy4WgygP1zbMirYtJrTNoJdhv7L3uzLnYP4P6O5OTlOUBR8TKaMWkzaqt2qv55QTU8kMcHJrRojuXuZnJKeb3bQ2of40FF_pBYEmIOCoBHpJB13SkcO0OgHBbhSpKZsgjBfGeJ0bV_HfeYlFcXGUwLdYjK0zcHO97tmYywUbC3uIcZ99JWxB9KSFkkzAJCf7IpBaUOC6afqt8jpf8biqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=XcbHyUpcGiEo6H0FblbChY2BSXGcu4Gi5YcG6LMGMM1UFLRfMIZ01hkVVY37HQzN5jMkqkXde2NvqCAYczow0EsfuvixwkHfXwasMrWNbkMHwNFajtUWltYHU8UVPSe0Puzvs2m9KBVgfPf4LktGtr70sGDmQCRW3eSisQL4xZ9ONdIr_0vHp9R-0lcOcoFosCG9RKTtQb93wAKhHJtRTzgaL8nV3szRJlb5xSyKnDRJeKELDa2GJR2o3SSkug9XplBm2WrSIWMPoC7bUcR90jBomhQIMhFf5vozmImLQ4lXo8UZHnQrY9aXxqPdpxI9OsvbdKDm8sOVwa17HdgTLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=XcbHyUpcGiEo6H0FblbChY2BSXGcu4Gi5YcG6LMGMM1UFLRfMIZ01hkVVY37HQzN5jMkqkXde2NvqCAYczow0EsfuvixwkHfXwasMrWNbkMHwNFajtUWltYHU8UVPSe0Puzvs2m9KBVgfPf4LktGtr70sGDmQCRW3eSisQL4xZ9ONdIr_0vHp9R-0lcOcoFosCG9RKTtQb93wAKhHJtRTzgaL8nV3szRJlb5xSyKnDRJeKELDa2GJR2o3SSkug9XplBm2WrSIWMPoC7bUcR90jBomhQIMhFf5vozmImLQ4lXo8UZHnQrY9aXxqPdpxI9OsvbdKDm8sOVwa17HdgTLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Xe-H5U2hCiA8et2iKORVryUCSfeM_Jrzm2K-qgjkZz_DiXoWlUVAcEbK0Q8tS-szvHj-pm7FFrdFT8l1onCyhnX_Nz9GDf9KceZshASvMBzVgNt4Hj4JFdJ_O_nvUbsP6mXMzfTAR8VNxDNuu3JLk8lPYZpv2oxzcs8RtiwdeHQYBstwnu98EhuERbcqbWsn1JssrR2larwgTbW5m-qMYof-yhH1m13aVQV_sXkmV8vYhnxoSO4O-Z4haphcg3ouRxzvx1j60nqI4ElwoqLxUyfE-jQEvpmZxnTD_cg4hS3ME5Hfdv9R2zf3C8AJidGDAIQD4Uj2wddyiYkKibCQtTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=Xe-H5U2hCiA8et2iKORVryUCSfeM_Jrzm2K-qgjkZz_DiXoWlUVAcEbK0Q8tS-szvHj-pm7FFrdFT8l1onCyhnX_Nz9GDf9KceZshASvMBzVgNt4Hj4JFdJ_O_nvUbsP6mXMzfTAR8VNxDNuu3JLk8lPYZpv2oxzcs8RtiwdeHQYBstwnu98EhuERbcqbWsn1JssrR2larwgTbW5m-qMYof-yhH1m13aVQV_sXkmV8vYhnxoSO4O-Z4haphcg3ouRxzvx1j60nqI4ElwoqLxUyfE-jQEvpmZxnTD_cg4hS3ME5Hfdv9R2zf3C8AJidGDAIQD4Uj2wddyiYkKibCQtTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fevCIMxVdsAk6AxhpzkPGWkEjSV4H8ajNdJLnM8_5MeNNx2F-DCyXKSLSqWgwMjuJx2AbL_onI6hN3YirVquhnVuPqMESjgYYxhNfqs2IOCfZ7gXRkZlOgyVWoThJqS07ks48hijh5V0m8tqT7MP75JCDcdbQ4zI9D7AHeSBjxahJ9HPmeKRqlDAf1RMTgbsmKmNwo7G-NziG9BkzLGynRgz1lAZ5fQPM0qtTcFnQsMewC3B01Tg66t-mBLBaesrS9QqefHUhkZrRkuylccsxBFFLjA5yeVqCbvycVfIR-tv1dwqLCnfAbgYMXzSgD5dyYBPjWQaKeuf4KoAkzMvdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/spDgRiA8kJOKQ26gg2k5W_TPsUSznAu9-rgLOScjKZpg2EXdYpuviIO27pyaBBNmpq4QT-yvvFfLNFHmTIGkLJVQ7RUMtsMqBToboLVzLxqLDyhjOusCUMIyuQR4VmJ12sIHti5fEg3MEnYTw2GRLmGhFTELG4MVskDdTxGROMjFLzhC3hgYNJrZS9E1Ji1NvrcYZRb2VBLpfaeyC3dNzafJ6xosUUUg3vbnvR8AHYuJhbLrTa70PXFxrBeJcidIPWjl2tY0Rdla3p4iFSHWHrvdHdyTZWgLzvY1fxQjxCOjntSFGQbRhVESYyrkkG4Rwe-_zXYImvJrZdlN8Msr1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uinQsFiaQhNvt6z94EvPSxfUSB6kxiSdARGLEpFwLVQIKo9TkRKZgO7W-h0X1HitCTaz0bPBC10dKi_bz8TeXXRfDh-4bz0TaS6YDy7Og-1ra4Kk1qhDjpN3-EI_mTjqta5idoC-WvP5hMFcnTghiX3KYXztV5Gpw96MfxZM8GXT3qt2nOJnV5BS9Gj8nhNo_rmm-M927nyUNavRKkz2NzbVXm-EpcsNKAerB58KH2jfpAnVRKPXaYO2jrmABPHsTwZl8G55yjN1rgr9jACu5ds4xMqjTN8TDFBtuSFysJlZM7J_b8F_S_dd5BJ1iaTWM6UgTzp-4qsXjxSqYVNvoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=XJdhr5B7GiAVXGQw96H3uIQ4Edyqqk-62yF4i1k9FoZ_nwe9dlxDV7ZZqYPSHUM_LOc9vwFrgFvgLfAlId2IG048gDwjKSZlBcKL6hgyHt4--XWA_p4jhez0e5c8xgR-nRhsH25K7UxIxqC7MxGkabPtrHRcvhGkZNWbzvL0P0ZaGYRqFK4sSgKe52pZBR_x353zJjT5rFiUXVnvwSLtTNvtzPezs8TCoNyyhN-pcjy9EvqmALiiI61j2kNkyByud_UlwckWiGH6zjISB1c_ETHs2zCGGSq-WjDpWD8VgSnN6hsBLWRdvtPaXXST4rKLeqshO5DO9FcoUydDuRcEEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=XJdhr5B7GiAVXGQw96H3uIQ4Edyqqk-62yF4i1k9FoZ_nwe9dlxDV7ZZqYPSHUM_LOc9vwFrgFvgLfAlId2IG048gDwjKSZlBcKL6hgyHt4--XWA_p4jhez0e5c8xgR-nRhsH25K7UxIxqC7MxGkabPtrHRcvhGkZNWbzvL0P0ZaGYRqFK4sSgKe52pZBR_x353zJjT5rFiUXVnvwSLtTNvtzPezs8TCoNyyhN-pcjy9EvqmALiiI61j2kNkyByud_UlwckWiGH6zjISB1c_ETHs2zCGGSq-WjDpWD8VgSnN6hsBLWRdvtPaXXST4rKLeqshO5DO9FcoUydDuRcEEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_0QliuujHPcCBqKJavMAM8k8-lVLDPVgB3ZwFLp76y3rPh4_N4BJOdz5N7x6XYUJHFdJ5QKKWEq5_NqICx4u2hdEw3ksoU9ePyCDYT1hIKXWYaDvf4XiGWR7-PHg9VyktS1FuF_Sx2VYs0697irbtKTDp9HhLUEyUgNEtjutU-rrmtIEwhCbn02FZcqEQtKrlqbfhxRL5dScT2wD-PtKhapdfHQfY8rBePfFrNhTj9Pv4ABI5Ma-Ju0rT8ptsC85ic-RP_9HrnpPUiGcQ1XQa9lJQX4xbGOQSRU-PyzOz9UFLjsG67aIfPNiwAiKnAVYzT6nZsN86-epP9kdQCsdils" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=OGrx7AM4pCNc3KsZ363lynOcmp_zSOf8oWcawmpTBLJ66ATd1tp7vIz1WzRyXogaZElhAIuy8D4ACYJcP-rLp9pWQpLhuEq_cIogvR06QmDVJs6dqRmUunyUl3-1c90ufAqQ7dBoTnDCiKCR-LWMBJKG0NbuBMTlbyxAJl9OkMvllLmPHgKZ7eyf1dcc_v7jDPBwgL8gejXjcX6VbBBe9XyPooXKGe2R_dZUaSlSIW0gYaGGf86sQ5Rz4_jyniTB5wHbBFTfLBfcwx9JQqWyO12HoVKK33nn41DFaxue9S-703EMFh4jiMuxWBf3Ht8f3r8dFWWQ2OZ8lmIgGAXi_0QliuujHPcCBqKJavMAM8k8-lVLDPVgB3ZwFLp76y3rPh4_N4BJOdz5N7x6XYUJHFdJ5QKKWEq5_NqICx4u2hdEw3ksoU9ePyCDYT1hIKXWYaDvf4XiGWR7-PHg9VyktS1FuF_Sx2VYs0697irbtKTDp9HhLUEyUgNEtjutU-rrmtIEwhCbn02FZcqEQtKrlqbfhxRL5dScT2wD-PtKhapdfHQfY8rBePfFrNhTj9Pv4ABI5Ma-Ju0rT8ptsC85ic-RP_9HrnpPUiGcQ1XQa9lJQX4xbGOQSRU-PyzOz9UFLjsG67aIfPNiwAiKnAVYzT6nZsN86-epP9kdQCsdils" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=MBXYXO6I1RqGNV30FpkpGfEZnnIBXDGZPc_Rv6j6gjZYrVKmmfO-9e2vghFAN4vdPqHGHtDsTJaxDQD8DDLnsIsyfHlYAxwxK46mysBLulHmnFgZ5td50-8nx6boMP99DbRgTUKlSz2CBrbcfHxJHtYPdHXxBDkMZSCgHy26-ZBpWNMIPPgvnA9VQKz5HYwxmXvoARiOMXdq1C_sgQuyTpIHSub4efRtq4biVsXyneh6q602r9sUOHwHKLDBUweLksAmoMwzwnco0d-6rTtxU40TWzQRC3IhtiSY0HlCtduT8eJzqymAyZdbsI-VFznqwADRpBx73NWoOs2fAG5THA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=MBXYXO6I1RqGNV30FpkpGfEZnnIBXDGZPc_Rv6j6gjZYrVKmmfO-9e2vghFAN4vdPqHGHtDsTJaxDQD8DDLnsIsyfHlYAxwxK46mysBLulHmnFgZ5td50-8nx6boMP99DbRgTUKlSz2CBrbcfHxJHtYPdHXxBDkMZSCgHy26-ZBpWNMIPPgvnA9VQKz5HYwxmXvoARiOMXdq1C_sgQuyTpIHSub4efRtq4biVsXyneh6q602r9sUOHwHKLDBUweLksAmoMwzwnco0d-6rTtxU40TWzQRC3IhtiSY0HlCtduT8eJzqymAyZdbsI-VFznqwADRpBx73NWoOs2fAG5THA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IxeIZ4SxJKAG4ReY-ZaHsTjCeRyZNcXRQM3ZDGh_HupPgxvjzswhPKpJqybOv3K0yaJrYem2LBvQ8GABB_enGGYEMKVMamvEM3mx64oqg1Vv0HqPIFAaFhFdxso4fK8hMQ9SaF2RqnySg_hpbTz7z-ehwjPS2Vn0Z9ZddSWxvO93IyLFjCcSZiWF5N5OUGfUn2VCn04D0k1gdTs5prj0_-t44oHYokvBJmJx8vH5dtU2JbFLN0RnwPoEoSEw6AvFX4yRJmNHxuKAA9NC0Q9DSEckPsNdk2bt0Dhi1kihdjll1Av8VRcHjtDnMp3Ign1cKccUxmmD9TRFSlryC-DYhw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTrjXlHcjwlWj4sIfyF-6wQdweM0qNU4G1kTFFqAQly4MYbRh3jPWA0Huq7As9962LfHR8C48R16cskmtimXDzgyvp3AShn7kZLBhawYQc1uqVPM7kUd0UXcO36v7dWOa1AE-eP_7v8ZC5h03geZqH_xFmlV3zDlXI67Nv-5uWlerwW67OOdInP2hEiHraC2m8Zejodn--1ARxKZBVvikSzFHP_EJSU087EMEBCINe4evIuTu9c6TXKfsTbRm4ZEVs_dFvsLKfNYcZrD7i7J6c1vA2wVayghVAnjmgLBJwJTI7Neetc7cWaIJzko6zS3KRb2pKGWG603vuoT2dLGBSWU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTrjXlHcjwlWj4sIfyF-6wQdweM0qNU4G1kTFFqAQly4MYbRh3jPWA0Huq7As9962LfHR8C48R16cskmtimXDzgyvp3AShn7kZLBhawYQc1uqVPM7kUd0UXcO36v7dWOa1AE-eP_7v8ZC5h03geZqH_xFmlV3zDlXI67Nv-5uWlerwW67OOdInP2hEiHraC2m8Zejodn--1ARxKZBVvikSzFHP_EJSU087EMEBCINe4evIuTu9c6TXKfsTbRm4ZEVs_dFvsLKfNYcZrD7i7J6c1vA2wVayghVAnjmgLBJwJTI7Neetc7cWaIJzko6zS3KRb2pKGWG603vuoT2dLGBSWU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZHu1wsAhuOc9DhxNSGpKrMMaug_OLtFgofBcdVgKkGgmlYrV7pPzngOGAlWeHj_lAxBR29AsNsyufRzxsyUJA3OIpljeTCr278HG6F3NnSy4iLFJsdJTX16lm8UkASzpRIgKust_p13p-xs4oujXCqq43fHDZI1tmA8S8LkzsQVrfw8lkZa5y1nHe8RgIeaUJodkVN6_as8He5BMwyGAjolDXqxKPONJXP3aLBJmKpXAsg2nvB7Q08yb1KSevoGM3lfyyhDUbVQjnEMYIeT-ESNk_qISc6Anv6W3BncmYuIMG74Uz7kYI_MS1hEmJJrG2BNiAJHeZlBnKAW3FnGjA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Dt9r3D0YmQzpVqKHYwyulFbA3m63g-bvDCq26o1o4K6JrWHz7G-2qHBn31QingN5Jj5ZOz9qms0WIDnPw7yy0fzYb5NJwLLYmEGyWYp20z5m4cHAGaH4Glp99Hcsxv_KN2eKZ6XoH-DPlz-occzZLBCcQGaqhKlh3sV5SC_Qi0jHOqU6rYcph2vDgFR1E2eaWBnjtWgit1entkrzOJyfBcVbvPwZWpOu0um1VnQbx-3E-LV9j1OaEzYEQJtmJBPrUZospVLu6ormTPs8yEaxLRTGF1mox-Hdj7ytQQ--p0lGwpvWM47WknMXBu-0d2M6QsqkheICi2V4SgWwAyV5Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=Dt9r3D0YmQzpVqKHYwyulFbA3m63g-bvDCq26o1o4K6JrWHz7G-2qHBn31QingN5Jj5ZOz9qms0WIDnPw7yy0fzYb5NJwLLYmEGyWYp20z5m4cHAGaH4Glp99Hcsxv_KN2eKZ6XoH-DPlz-occzZLBCcQGaqhKlh3sV5SC_Qi0jHOqU6rYcph2vDgFR1E2eaWBnjtWgit1entkrzOJyfBcVbvPwZWpOu0um1VnQbx-3E-LV9j1OaEzYEQJtmJBPrUZospVLu6ormTPs8yEaxLRTGF1mox-Hdj7ytQQ--p0lGwpvWM47WknMXBu-0d2M6QsqkheICi2V4SgWwAyV5Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=MArn5oyG-8Q_eStZRajmp4YN8bfBTWgLEGT6OsRcpXUMYwGPoXzFra4pZ3cTxSG9n37UKSkZkfcFCGJb69k5pGKffcLqFcsGLWb_PsthrGmxosN0M8RTbBBHerhTFDNxk292wPet-f0k-cu0-YJ5ieS4lR-TjjLFCRRD-cY_Oc1B2XJcNc7VyNlZvTRyGZzlo-9MqmgLa1nXs6T9l749I_R2OWb7Eof-VYmVi2xDoQ6XEwoPUPSbY6voljAXusWDwZGqNLR0EbASO5VRUNeTJkpK67_edTuDPOkvtayvpzdVwCaIofc_CosTIsl_nI-BQKMrr0FenJM8hYTtDTa4Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=MArn5oyG-8Q_eStZRajmp4YN8bfBTWgLEGT6OsRcpXUMYwGPoXzFra4pZ3cTxSG9n37UKSkZkfcFCGJb69k5pGKffcLqFcsGLWb_PsthrGmxosN0M8RTbBBHerhTFDNxk292wPet-f0k-cu0-YJ5ieS4lR-TjjLFCRRD-cY_Oc1B2XJcNc7VyNlZvTRyGZzlo-9MqmgLa1nXs6T9l749I_R2OWb7Eof-VYmVi2xDoQ6XEwoPUPSbY6voljAXusWDwZGqNLR0EbASO5VRUNeTJkpK67_edTuDPOkvtayvpzdVwCaIofc_CosTIsl_nI-BQKMrr0FenJM8hYTtDTa4Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=vM1rPxFcurCcL_B5SURgtNSW-YNqqUuM0MoojloPIkrixZFxq8WzhIM3EuZDnX6wH92KeVNKdzi-qDxkCwIOLWTwcFlwr-7220nsiRnT73Q3ydXnEnXHqivoy6NCpKAOCW-Gpx2aIjQh-TKx0_f1QFdQthkyhG0YoXAC6b_vQm7p4yq7V2XvhvwmWQr-jxRWJ_25FjQ_0WeyeBeG4uv1ddWP22CHUK0O6PoZn4rtqB48YWRH3YhlboctfN4Em3o4IWiTC6Cro6oaKCurHEjLmll9N0Be5q2-FlnAXzTn4vqQrL4xhl-8h9lqGybc6Ot7WIivq5a4h-u0N8yiTQChxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=vM1rPxFcurCcL_B5SURgtNSW-YNqqUuM0MoojloPIkrixZFxq8WzhIM3EuZDnX6wH92KeVNKdzi-qDxkCwIOLWTwcFlwr-7220nsiRnT73Q3ydXnEnXHqivoy6NCpKAOCW-Gpx2aIjQh-TKx0_f1QFdQthkyhG0YoXAC6b_vQm7p4yq7V2XvhvwmWQr-jxRWJ_25FjQ_0WeyeBeG4uv1ddWP22CHUK0O6PoZn4rtqB48YWRH3YhlboctfN4Em3o4IWiTC6Cro6oaKCurHEjLmll9N0Be5q2-FlnAXzTn4vqQrL4xhl-8h9lqGybc6Ot7WIivq5a4h-u0N8yiTQChxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R_rNuL7zkOZfPDUZe5va7BM3yuv5Gq-wx_0DPYa3Z-roqk7QO3rfKr1gDaRZcZEijlgadNj28eIl9r6Ijpv4-kuxsP2X5_SMk4zOtlks1zMHSFa7iDS0UOXZtDqMHsVLUZgvhImOCZckYZv9nJy8kZAX3Cm4OAUqoh5c9-HdaZHeaUuNLZ6CjUHXGjoJL48UXFj21s1p7zRQuyu8p37T7I6iDMfrdDrwi3wu6rGXZGdQhcWStQZ3NNOz05nLRIP7zVY68oUMhaSWy3gWfT6BYYg4XhOtP4iKTRsdToTRhIoZvM2z4k3NwaTVjE-BUaRjJzkpzl1eJeFIHy6tJJdhpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiSncguiSpTmCwuTXhl4Dp1FenYcGFyMfPo7EKoAW3SiC0LpMmsZyMslBUh2yQTLcK5XLWwVntsTMFHAlzd5h8dUBjY7gHuVLFTdOi9tLc1poF-jNxy5JWPRWrZs6b49KLC_aBYgUf78CbCQUL9plDU3cqPt6xchv0oieOHt1lG1BCBxKfiW_N4ChroJHm4cm-6Xsd_sGv9W0ZWymbGubmTYQBNFLWgquASwMhX0l7TGxijKM5Yt2SV9ZkbAGDZV5RXGY3Hhu1uGOFKxLAt6_yEvBcg_OjuuZonnwyUrfQq3MYTWkAw7gxnrTj6v_s7Xje_0bU-EYUD_2Py_zYlGmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=T9qT0wojfOtiiO8Zg63bn9TZcy2jojPHVwR_m8tKhExJ4332wc_IEfMsKFlXD6-x2tsAvvsHSJF8_ewUgh3CEy-D9GFfvLO-1PmMp33fdR0k8Oz9GkAP1K5Jhbz5o6maEh-jRg-u_ZwHtxeGBgVzFAeiDSCrdTIZg6GmC15qPw7YHzrZbpnxQsoiW4A3zc4Qq0fxhg-fIUFWDmj5uz5whpKHJqyvKLfq0FxJRiJGIKPirgOoekFM08Lu4ywSYVcfwy6mwePO2UAvBAeH7p8Om38TABfIfJWRv_zcwicWBeIYIZ9RScpncL5kXmfG_Xo7PG0b77jlaoNCgR0PhWT5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=T9qT0wojfOtiiO8Zg63bn9TZcy2jojPHVwR_m8tKhExJ4332wc_IEfMsKFlXD6-x2tsAvvsHSJF8_ewUgh3CEy-D9GFfvLO-1PmMp33fdR0k8Oz9GkAP1K5Jhbz5o6maEh-jRg-u_ZwHtxeGBgVzFAeiDSCrdTIZg6GmC15qPw7YHzrZbpnxQsoiW4A3zc4Qq0fxhg-fIUFWDmj5uz5whpKHJqyvKLfq0FxJRiJGIKPirgOoekFM08Lu4ywSYVcfwy6mwePO2UAvBAeH7p8Om38TABfIfJWRv_zcwicWBeIYIZ9RScpncL5kXmfG_Xo7PG0b77jlaoNCgR0PhWT5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wnr7LcdqNBJHailU-LJgIYVk2X0RB7nbx16xR1YuJpPLLJn1WKaU9C4nPgocYcNcbM2UowfnoNZWet_hbEyQr8b3QPznU1EPKZGDMAo7luQc_x5BmquWKplGicyngMFYLuOWLNdOJJfbFJBPifEPqqiUGhl-3utoA_79aUH7B2gXJAvUboKc7Cy02TcaBzHb3nv5atgdZi9dbyQMGq4IyO3ZHPLx1y1R_4urFG0U7muJKPHgGer2mbRSGOymOI8fz46n5-9Fa1MJ2aVc2Zl8Ri1oxys4S3yThT490UKiNsnEpYNuF7lQmlCUqOl-pe5kucGaNJj1Yp60sLS4XMGx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4trBl8IPGCxTpxvLLl2SJyRyJ8W2z2D2uaMQAFG6u7yfXe_VqxCqD9wHbJIK1xBklNZOTw0IIvKXb5pRpEGUTsNl89Yacl2deF9teihs4ydt0GS6cwoyInw_MWN9dwrBPXisTjsbQZA0XFnxCzgXAUevLZoChVwYxk9zYBzHbllxviJj1-X2erIzVaYU4VuWtAZpZXv5iw4EI7kpwFTdwZ8bhlbfN78KnQyrEQuvApQW4nE232rjW-K3O_bRgz_EkXT3WsQLWtpDuIkA9FCbaIxL_Aqpbo6wcTe4FXCLTuujm0EQAATX3qTJLYNDSXHEpqmX40qNTWY1FjeNiVkyA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=VBkPDegar_0Djb_YXmcUjiK6RZ6Gu_UooCBl3g83PIYINOS1Iro2fsYtvqvWbjhBZiirE7kHxJEToBVsNix3sk6F0ip5xNmtuPr_t0ZBTwZTaeuIDvJC_vdYnXkXSGEZdYClgBjqkGvmx6vGOWWGNk8DAqPaIYesfdQJxHosdB5wuoxyux5a-CqrQv34H6UphAtePyxN9GAOZfia0TBoqLuhsz1v5dHfplwVoHeyI62oNYCLVGYX9cwEazf6mtRDr92QhsNBApHXYk1tPqsR75-atem51zys0EU9B36PTC2E530_2bxHu_C_rlwN4v_nzEvcphJL5k7-IjTp60TzSYDa_ViKZVY8X2FyePGFysC0CqnEFJQx44_0Hf2ryY0g5t-POkD1KokDvD0RYmlArffyteiI2inmczG1fdRtydIrLO3MOAX2OsqAigi4Zb-wrJwLt76g5ZmZ6iHdGUyrngzEOCueY5XxFXNXEqV80KXLc4fUHprBPGpsC4T6_tAB60hGl4V-1Nv2oqBccSentzMVcs3Rehh-7Fiaiy_wl4pEsfXecVFyCk1SVAz-1naOKYcz1qY6SmmXLRuGmzdXrlyNv-dGjmtGODvh1oC9ZCPnRCrzDZ94dI0elhxHEPF-vZNgc6zU5-VpoTbDoZzJYs9Fq7oSrwko9_0ZWKdE9D8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=VBkPDegar_0Djb_YXmcUjiK6RZ6Gu_UooCBl3g83PIYINOS1Iro2fsYtvqvWbjhBZiirE7kHxJEToBVsNix3sk6F0ip5xNmtuPr_t0ZBTwZTaeuIDvJC_vdYnXkXSGEZdYClgBjqkGvmx6vGOWWGNk8DAqPaIYesfdQJxHosdB5wuoxyux5a-CqrQv34H6UphAtePyxN9GAOZfia0TBoqLuhsz1v5dHfplwVoHeyI62oNYCLVGYX9cwEazf6mtRDr92QhsNBApHXYk1tPqsR75-atem51zys0EU9B36PTC2E530_2bxHu_C_rlwN4v_nzEvcphJL5k7-IjTp60TzSYDa_ViKZVY8X2FyePGFysC0CqnEFJQx44_0Hf2ryY0g5t-POkD1KokDvD0RYmlArffyteiI2inmczG1fdRtydIrLO3MOAX2OsqAigi4Zb-wrJwLt76g5ZmZ6iHdGUyrngzEOCueY5XxFXNXEqV80KXLc4fUHprBPGpsC4T6_tAB60hGl4V-1Nv2oqBccSentzMVcs3Rehh-7Fiaiy_wl4pEsfXecVFyCk1SVAz-1naOKYcz1qY6SmmXLRuGmzdXrlyNv-dGjmtGODvh1oC9ZCPnRCrzDZ94dI0elhxHEPF-vZNgc6zU5-VpoTbDoZzJYs9Fq7oSrwko9_0ZWKdE9D8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6yelb1TVCid5CNjpqfknqiA5C2wME1VMI0z9KDGZE1YyKqSVKBGtihFlB8k1FUBGFuFFRlLifFGGicCbFiRka1TAf4FcfwmQ-90F5BDfO0y2MbyRcWu5EKlFZS2OSgofZ2xiWIl9NgyCu2Xl8k5BQK1GoZG68DbzXVFVUgeakeQyO9JFGOxv1Zk1WEJnEAQUDuWVpCD8CD5VC1DOfrEfbfwkvTDR8CdnU5fQGQl4mSAQWcyE5L5pNkHtW5DztKA3X0UIiMEycvf4wehTYbuRc7_moOz8YpdFF24WbryBPhq3_9Y5bSMK2IWCn-Lk_wWrU8g0xme-Qv8ASkP_imJrOOk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6yelb1TVCid5CNjpqfknqiA5C2wME1VMI0z9KDGZE1YyKqSVKBGtihFlB8k1FUBGFuFFRlLifFGGicCbFiRka1TAf4FcfwmQ-90F5BDfO0y2MbyRcWu5EKlFZS2OSgofZ2xiWIl9NgyCu2Xl8k5BQK1GoZG68DbzXVFVUgeakeQyO9JFGOxv1Zk1WEJnEAQUDuWVpCD8CD5VC1DOfrEfbfwkvTDR8CdnU5fQGQl4mSAQWcyE5L5pNkHtW5DztKA3X0UIiMEycvf4wehTYbuRc7_moOz8YpdFF24WbryBPhq3_9Y5bSMK2IWCn-Lk_wWrU8g0xme-Qv8ASkP_imJrOOk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=wAfgFj7ENIeWMoT9H7CfAF6Qym9S41ZMguXEm4532EuGTjKNspibw9mBGWVU3foWsWYyLcs7DNHw8NA_BZw6tm95CmWc9CAzdtFDim8TCM6OUoKa6EKfoZA2Zsyecm5acr9qlel8UiF70GSyyZaODrgfm6O6aUFHbQ8VYBlADrbFCOmXOOOIM5ZwHxpZaI-V-fmFHO1M-0rVszZPST-TLjuJuW8MMkg-PwWhEuEQfHP8OS-GBQUrVa9hC1ihSRNIQ6zk1mIhCWX8m59Gjbg22wHSiwOyveuWl9eByCmejzttc7HL4o6FXFbdUyGC6qlawT6ZTRGNogfPJPvfEmt-EIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=wAfgFj7ENIeWMoT9H7CfAF6Qym9S41ZMguXEm4532EuGTjKNspibw9mBGWVU3foWsWYyLcs7DNHw8NA_BZw6tm95CmWc9CAzdtFDim8TCM6OUoKa6EKfoZA2Zsyecm5acr9qlel8UiF70GSyyZaODrgfm6O6aUFHbQ8VYBlADrbFCOmXOOOIM5ZwHxpZaI-V-fmFHO1M-0rVszZPST-TLjuJuW8MMkg-PwWhEuEQfHP8OS-GBQUrVa9hC1ihSRNIQ6zk1mIhCWX8m59Gjbg22wHSiwOyveuWl9eByCmejzttc7HL4o6FXFbdUyGC6qlawT6ZTRGNogfPJPvfEmt-EIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=rGAuXT97o1wRPsVoONwhn87GThpeocpFuJZj-iYvIT-xJ0V0KUytMecMvC9dlrJUOtqdlHjw1wALjsojc46hwX6mhceF2Vji4sKjZYGaCTB_iNUUPHVlNvU9M2CcGJW4ridek4Dw_e7PpK4eUnRakkBYIHOww10f_YCCvTw8XEKQrgyDxdWEIIVrVcgCm81EAswGXHc-SPLum09hk4Bpi7uXrDOsF_bJStn2_8T_oRta6EBXBUrXqHoZlSEI-ymQE7G5KITK85EAp9YA-eBt8sqnHonrFJ0bYHLUjlOGqk6z2Bh36TKDWpbjayefbJM8mnn4ZZGVQTnfBp98C5gABg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=rGAuXT97o1wRPsVoONwhn87GThpeocpFuJZj-iYvIT-xJ0V0KUytMecMvC9dlrJUOtqdlHjw1wALjsojc46hwX6mhceF2Vji4sKjZYGaCTB_iNUUPHVlNvU9M2CcGJW4ridek4Dw_e7PpK4eUnRakkBYIHOww10f_YCCvTw8XEKQrgyDxdWEIIVrVcgCm81EAswGXHc-SPLum09hk4Bpi7uXrDOsF_bJStn2_8T_oRta6EBXBUrXqHoZlSEI-ymQE7G5KITK85EAp9YA-eBt8sqnHonrFJ0bYHLUjlOGqk6z2Bh36TKDWpbjayefbJM8mnn4ZZGVQTnfBp98C5gABg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eR-QyfSoFF5oC4EQoZ5a0bWKW0UkIGbQ0taG8lgUyZlPsJioByvZTYL80PkFTeV1YLqfi_CksbdELi7CJtQjLcSS2BH5zQ4OHoObQiTp2TRfCSJeXtEJj8ZN70-K6e74JB4VPXwzADPW1Y5SUkxpw1n5V_3mluyDbWCtsiAv3Zfp9wBbpVdjXZ03wypjYd8HkMEtuwROMLXTgOTaFtcH4xU4H9Cms9Wu0gr9xrEuu8vcS7Hx4TSqx6lo2dZ3U_Bwnj7-8qsjr6txYzOcbRlQqVb5aq6UauEC80zvcPGJcCkqUW4PZQTKeJggUfNqaoCps6L2iRBDgTLR3LsvwwCfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام فارسی وزیر دفاع اسرائیل خطاب به قاآنی فرمانده سپاه قدس
آماده‌ایم کار را به پایان برسانیم.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5737" target="_blank">📅 17:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نحوه اعلام خبر کشته شدن خامنه‌ای
و عدم تعطیلی مدارس</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5736" target="_blank">📅 16:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T0Lv-bx4-h8yggk-0t0CluhV49tn2_i3AVBHc3VjFn3zuagU0M96sPEyTl_02gtHpSuB2o1SSTLXBp8sc4Or9w6t9KvmMJ4mo9lQ09FUVxhYMYZBanDHv3f0t751RTqoOvrBwSaqm7KfYcTKO97AVzW8afKipxoz6njhK-B4xQDmlLDtf3oGCexpavAPN1lXg5H1A-Z0Sm9cSRXLNNJ4L0q7hXKRA3b-J5aMaGufACPqX9srx7NI8WA_2k8yLrBXnwgQexgzNolz49sjHAhwITnAv6MqYpMev0xkmD1qhbhDzPfRcjN7AQyrCGzphixStYvAmW8iJ61NsrMXvwdBKg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5735" target="_blank">📅 11:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1pHTWo5E4kj8CRhPfzqhmNaMjBl0vncTt3e1IIwDBD22hjmeAo7s5UUoXk2qhlZgge0ubVMZt9cADeXAtk3FBo7gi4-yE-kewA8TezKnrQ3QtNEhIrPIKQV0VnwBYlvjOXL0hyOV4gZHi0ctl9i6mqNm8Oj3pYu2G6hgzAGDuaZQ-CYkgZrHYvdFXiL9qFIhwdbtF0AFgW-BUFz5vRV50o08i6bkWVxheLXy7glZRphACg1LH0iGM6n9W6Ni4B-Vi5qMcXFunrJQ_c6r3UlsSK_hJm0vVDW-FE8zK91gB_oAtPZWGP2I5z4G2-kr_5NCI-uW7vrNcmte8J03yF4Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hJm4RUINhScvAfROamGe_CDZCFT3n-hJmqrrQ_IEjfhMXOh-VlwrAjMzeBCImkKQQPe9kWCFd_-UNE-tB_3_RXeEXpJb6aDZGD8krWrRTloMXBLgpWXKg047jMruoiuQhW5mRHVkgWKLM5LLxFVvWVjmFChdKKhJb3GAgPvTy0q3iwjx79OIv56olUEya7aEO7xkKvUdqMGuiF6vW4IiaVKZUB2XxoazR4XZzQVPDBTt82AGUTMt347LTjlAS0P7mZJmXT-NfQNzTneryhYPHgvDm30xVMuDlmxyMBknXiebX4BmJSoYfu2OrKCGz0VnzMdvFQk4_WybcIcBqT9QDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBWdnzjr_a2uz2g97QqvBL_Eq4V0PdG6AqNHuauyGiabmeWwMuoOr40JZndtMsjtKmyEADgWZlDAz-1Zq3WsCNDECLVPxR7R8f8hIulylIkRTGZB5Y2DLwG2um7oo6PmlUbQ0ZAg_YOV1MLWNYvZXHHqLZBY5d3d2TsS4FXRvOoKW_NvcZu6TdvaDTVciCW6Lcvb6U_9z7OA62KBBcLYP-JPggkUJiJl5eoycsgSNMFoKP2YknGwNPDnZKloqQy4HQFZpSofYe9nmZ5yX1aBcChNawePtFl97iQStNxFqzX7paiEXcoRJbcpWyWjUi9WETsyHINe-1k6i-J0n85AOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=b6bloEvutPkmD5M7FxYqa4P_ltSfEIpSi9tnnRJBjhqkwwNpfJxxqqPnZZF9P7PDv7VJIKQxln7x6Ka4iYqJvO3Zs2zRZNixxFfDi9luv0zWOLZtJoJVT8JOe1zYhd3pYC5WjgnKI9FCclFs4AS7v8YwzcS8tQ2NHjJEQjW3QnpGWRXbFQcAxHtDTDNP5IRTZtpbAOfp6LBjugJvNSZ92i4BkjmD62AuFVTxn8twNvUz_20TqpiV8xYBhfjyAPMCIGkdjYSVvzulEBMSBBKO9Zv9RWMV8ybfhp9Q42cYdKAmWDnZUs6X6VOWRXHWaMn8N3Ag7i-Tymi47du0mG_Vaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=b6bloEvutPkmD5M7FxYqa4P_ltSfEIpSi9tnnRJBjhqkwwNpfJxxqqPnZZF9P7PDv7VJIKQxln7x6Ka4iYqJvO3Zs2zRZNixxFfDi9luv0zWOLZtJoJVT8JOe1zYhd3pYC5WjgnKI9FCclFs4AS7v8YwzcS8tQ2NHjJEQjW3QnpGWRXbFQcAxHtDTDNP5IRTZtpbAOfp6LBjugJvNSZ92i4BkjmD62AuFVTxn8twNvUz_20TqpiV8xYBhfjyAPMCIGkdjYSVvzulEBMSBBKO9Zv9RWMV8ybfhp9Q42cYdKAmWDnZUs6X6VOWRXHWaMn8N3Ag7i-Tymi47du0mG_Vaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=StsAAf766CAXzwSCP3MEjU5N3CL6Y-rAx9SkEbjb4uejNQfBDyNyWecSHe0SQ1MIv6E7fu4V1B509djBXQnoksAVUQp2V5PV-Yx3AXFe3WGcjYiqVpXdQbb1QDSyH5_nexCmYXuoJ9-5g5n3no_TS-8kkNQLXBUOpj5gjXrs_cLW8SFq7WRqr05Q9VUdWEYUnbfAjpuqfU7VuJqtS71TXbfwJXvBevJarR2ZYVKM7inB41YoYk248E5BI-O7vZwop4F4CIezktL8G9S3pnJ7VWWGHpEm1Zj36sbsm49S5kK5b5j0sbpc1nvMFKFUsShzhEX0S3UZkNLnXuMYcA7jEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=StsAAf766CAXzwSCP3MEjU5N3CL6Y-rAx9SkEbjb4uejNQfBDyNyWecSHe0SQ1MIv6E7fu4V1B509djBXQnoksAVUQp2V5PV-Yx3AXFe3WGcjYiqVpXdQbb1QDSyH5_nexCmYXuoJ9-5g5n3no_TS-8kkNQLXBUOpj5gjXrs_cLW8SFq7WRqr05Q9VUdWEYUnbfAjpuqfU7VuJqtS71TXbfwJXvBevJarR2ZYVKM7inB41YoYk248E5BI-O7vZwop4F4CIezktL8G9S3pnJ7VWWGHpEm1Zj36sbsm49S5kK5b5j0sbpc1nvMFKFUsShzhEX0S3UZkNLnXuMYcA7jEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTdse3LQq9YlCNcztpLX7wVX5p0NiE8z7oe3eK40uG1NyNa5Ext4YQBae1STzraYJZnkK0jADqGXbvb8bURdGP4OBH4OBMOwqC3kySKNOjJ78_5uxZ1hHIF8wkIjbCZy_qk_c5h4LXI6dWbGGXmCMUnm-c8vlhMoLgtK071QSmx20uXxwmJYWe5x7SxuUQgNd4I8RXhkgzlq6lnpnmcUtstsjU1KJmWfP3HR8ZXHz2iVzPu9b2AiPXRLHAL0-9XV8hBTzkawW35jh1DpKQkl60Yj3XD3ggXnGNpz8YzUiHnfVmgRCg8_pgqyBOjCey2-aqoTfkkllq4ccpQroJpPzQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bPBaYy64luXh9pUvcMXzHf22C-GraOscxAX94lnEJ7vP7K-LX3m5v83LelnPDjcu72fAQ6aSp6CyZoFNvyjjDu4dpd1sz6l9pado2Rf2s5lsVRQLAQgloEd8wmsaHxZTOaa8B1L4ETk5z16bHgxJR65CZEppCpO-m-KnzhhmQG-bRdv9fE98b1Luo3QsIPIcjksG4IbV1GTlQm0QSdCGRyZL0qJCFwOJ7bw4hhotS5vl5VLpOybXBp-xLr_Yfuamfn2RybgrVpfF5328df0cpTyfqy-GeYSjzv9qSMUVhEc-T2vIAQ_1ZGMTezBb2LO-gZ7wAs0f5Fb79Wn08KEM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ZQWDqDzMCfRdabTF4im8RKMGlNgc410sebIwAWB3ILhsXoaiaXZgNt0T46o0JV8DJtTG00yaIbu_1UGqMH9UHo9bEJdwgMB19PvMLrRXwADpANMKuXv_StouzY_3QFQB80JB1tvnvxLNJlA7RjdLb6nhFQL7d1_0pDkywMKyYlu5BijCWgIRUldf9plZVpVoG6vZp2vy7B-0sx-wNZsc-6a7D_yyIxQYoZ0SvKreQHmdWMb30f0LhyMzX7wV8qkZe3a-0-EKW025SekEf3OkVowi6YuBaF5vqjYzxyE2RH4VosPK_XGDsQt930aHJ09RxNDdZyh0WAS_a6LJ2c-jSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=ZQWDqDzMCfRdabTF4im8RKMGlNgc410sebIwAWB3ILhsXoaiaXZgNt0T46o0JV8DJtTG00yaIbu_1UGqMH9UHo9bEJdwgMB19PvMLrRXwADpANMKuXv_StouzY_3QFQB80JB1tvnvxLNJlA7RjdLb6nhFQL7d1_0pDkywMKyYlu5BijCWgIRUldf9plZVpVoG6vZp2vy7B-0sx-wNZsc-6a7D_yyIxQYoZ0SvKreQHmdWMb30f0LhyMzX7wV8qkZe3a-0-EKW025SekEf3OkVowi6YuBaF5vqjYzxyE2RH4VosPK_XGDsQt930aHJ09RxNDdZyh0WAS_a6LJ2c-jSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5724" target="_blank">📅 22:23 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=AISXSXZuZrV3JcuhpviL0rvqE9bR1_ed3QB-DoSOac9SS172yjVrol7CzJVcSonL6kmfK_edqj1rjZrlGOTx_vJc3M5vUUxg-XxW5PVM79ElDR2YPm3v3h2zZmohEVC0UodaXZqdKq7duFgHWYtDJbE1DoUg3fUzOfD5LSgeX6lwvItSj62QudL6GYTP0Lmi-7dWM5g1Rr_LfChqFlagKUPZ2RnBZthJ8Clmd05k4rZkUBXl2ZpINCCTqHQSCO-PV4Md1sCRYdj586hLGpWHs2bRs7JkLL0v52JPc-eU8cJQyQJ-T-_4tRzF3AAw4dFB9flb-TGpnjF_mZCmyAAlNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=AISXSXZuZrV3JcuhpviL0rvqE9bR1_ed3QB-DoSOac9SS172yjVrol7CzJVcSonL6kmfK_edqj1rjZrlGOTx_vJc3M5vUUxg-XxW5PVM79ElDR2YPm3v3h2zZmohEVC0UodaXZqdKq7duFgHWYtDJbE1DoUg3fUzOfD5LSgeX6lwvItSj62QudL6GYTP0Lmi-7dWM5g1Rr_LfChqFlagKUPZ2RnBZthJ8Clmd05k4rZkUBXl2ZpINCCTqHQSCO-PV4Md1sCRYdj586hLGpWHs2bRs7JkLL0v52JPc-eU8cJQyQJ-T-_4tRzF3AAw4dFB9flb-TGpnjF_mZCmyAAlNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E1Sccw10-B0AiQd9FGjXzKhN0k1VD7HKFYrnmN2LFWI5TLVAcDSF_Ae1f6Vl-ohi9HxstJ5bwY6PMouwgdMFd5v7KqQnrcv4dIPrvPMDSI_gr1Tk_QpW6IfE6T7zvkc1cG75ZhyCuEe_DVh3RO5nwpFV4Qlp7C7QdpaFAUJALpe8L_GzXIRnmlgGAru7NjOQHcTUe6C3Lkn9oes4WkRwlNs3YvFd7vF26xzJ57HyfOylLnfpUtyMb34gokItiCkre_TUuyEVndbyrOZTos9-mcowbzN3lKIySS0wmzvE4Fz5vRMHgxgrv1-wflCUOGa4N_px5NqtTGtyK2kuY13wkw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l8BiwDeSCqr9ZrGOdQvVDtHVHQxJ9BQAVjUd3u1TFCeD_gmH2AAvvtHJFbJwhqiTpS5ekXzGJ_TYVrgefKorMdsHfdMtzsVKDb8S_iAj-4DzLHA-N9l-PZEv9Ym7sgoae0oWbgFxCooM1co2k4QoedZ4xjhCQR27gkSiAgj09qbaC-vM2Uv1lDU_tDGm8IqSXiNirWAyHnnbBgFucFRF2MrKET9-idudNBFCi-4IDBiHd_Tx89NcAlJSsGU0iT17pzmN4_Pln527A8u41NZJCcojnI4R3S5YKEFm235ewPcMAZXVBqeSTnSTJHPdOt3ytkL1FYToMP2FSiZT_lQwHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MlvuAMzSwmq4_qsNlZBkLh8mpwMX70aijn5u_M4IM5eNeLkNHn_QUtrRcUNleCy7Ou6YDo78oAa3EdQYxQ2nG1bEs_GNpg8yw9rzjVYrWccuYZVArfEm8GHuLkcrnUNk9lBnv8MLPZkZ4EmuO_JcMUl0t8W5LFA42dl15EcAs9WoOBEFGJPpFkp0BQC0Ck1-8Ds1iBSB8vobi7WSSjckSzcnN42KM3BmHwdkpjmqUIN6Wg7kZCx99jIPzdU9fIJMdIHQLUC42_43ZvsRgSsb3uXTncBnwCZOjREh_CaJjPi2OYpQMOG_MlyJA0261wrROqxcgcngAsb6HmlPP1nJ_Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ZV5O0cVhEyJFQ6wzV8DszyZ-xeT_MMMpgZwOZ45xe6_koStUrO7DgP7brIhb0TyuxQvkn22nAqwdbK2rXLzJKl4CUeYjjy1kdH6Q6yNAvCfT1Ez6nFBatS4F411IB07xKpveTLT7IAcOutqyd0Ma4QoAE9nuTuT8BlUPmDzeqF3YleVa2q94-YZasrrpNT16m6Me3roxQa1OcRS4QWBS_vHsGpSsPz8R-BhrgEzrzEvTLEd43utNmgcDshkIbKM9KCf-8HF7EnoKIHa6nEAViUZzXJh3uMGqYsTHkll0IDgTDR4iu7Pr_QYNvZUN_-HefHql2Cu5hpc0od05BTfqfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=ZV5O0cVhEyJFQ6wzV8DszyZ-xeT_MMMpgZwOZ45xe6_koStUrO7DgP7brIhb0TyuxQvkn22nAqwdbK2rXLzJKl4CUeYjjy1kdH6Q6yNAvCfT1Ez6nFBatS4F411IB07xKpveTLT7IAcOutqyd0Ma4QoAE9nuTuT8BlUPmDzeqF3YleVa2q94-YZasrrpNT16m6Me3roxQa1OcRS4QWBS_vHsGpSsPz8R-BhrgEzrzEvTLEd43utNmgcDshkIbKM9KCf-8HF7EnoKIHa6nEAViUZzXJh3uMGqYsTHkll0IDgTDR4iu7Pr_QYNvZUN_-HefHql2Cu5hpc0od05BTfqfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mt8GFKOMqIVKmCEaDzi6Dgma0fPwuwxsBMW-o0XZnlUSI3LmsW_PgTla9FpoArQUH53H9JHzS7FysvDnx1iZ68SufAldXgFb6oMQVWqmARsvX-5GjJ-mhnZnkKiFAzbYDgQ0X7wMFRW-kPavIhb4JeoWV5bfWXEJUn6OeRrv0fdNkdv50olJUVV8aSlbsX9CWNhOjTv06NM1dlMfskSYt9q_w4QbGEebiHtgzvSLQOuQFFWVAVBoy1p1RGu0uWd8mfz2_fWe3GZNggZUNTvhPyuV3CBy73icD-gqp2DmlRB8hSWcjzUIpkErbkM325UD6tJIFJWgrO1ttVIVCrnRbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jI5pKKz2Pzo4BSEsOJhvaU3REH3mUGXLwHHOMWXVdIRJ-NPBWkqoodUuoAY-7fu0ozOhe4lgUsA3t6iaUWkzkA19yeo1Xj5d4hlZizXf_PaO5fjGIhqGPMmyIcCEm_T490ZePjiFkSAAVkO-eFAvVTYfmW9DYB6vBrBSEG_XC91SjevP4ahqZ-0ur6fw_8Ntuv9cQ2MR-Hmq1I4qfCV72wZiuedF9Ti7rlqj5Gy_As1Si5h2cF9gU96YoI2Gww7o7y0WLsZ79O-7-rU6-vmf9wQOicRG-H_JgLSHUrPWImq2RSCPMR9s1JkaexRQrjlpckEvp_ntUTAklBfmF5QYYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BFvtQ2qIs1VY9id6fIHniOu6rSBTXeds0idDtfrdJjBaob0PrcnzxYe8kJAFMysPdEIuWVe2yKVHeO89EU3XKXp42naILRLnIiI1HjzpJHkeuEx4oypr82FBqaitD0cL__jvvF8a6-_KUD-GxgKCOIEi4BSc-j6ltLQc76Q9t7NkXqcBKnYMABm-zginAyC1gTuuIis6Mlnya5i5nVEplwa3zOwjIuTSzcx7bJ0Z6h9dDJgEc6RhadoM6TC50wNmJtRa0NLSfvgG6T6FgFLlYapxw9J1D059aB2oBwDlbxPPj1rWcGwFlQ6Yi0yTsvY1RZ6oIb_BpC-V1biuA4_uNg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TN8Qfrd38uBc-vyHvIaR1eeMDaU2dNgzMyO_peyzE_QGuYpUQh9t22NhKmAnkmMraIgrH3ZZWh1z-g1nX3r6WWu_qV-2G36Xf65immfLXgAfuIPzntZ97Cpw0_8BFC2j2MBiC78426sJOfTruMDtZR7S7ucgg2KXACX8SvcFsug6Dpocpi-ngQ17OB6i_a1d_TWL0Zp5NH45_UB8fKHQd6pCWvB1HvYkG8GfmYpflNDQYoOqbdhx4OcOipFZoP6fb-X1Owjl2vkacKmZBqHgvGgooA3JrgQA6ke_cIRKPctSwhCZVdPIoIdo93eLxmKD1lOdz-9qSo-slhLFvGsdjg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=cBn4tRsN2VrUEV70NyCpPpaHOiIkeQtdulAMu-tesjGboooFPpjsKQsVhG9ltl8nsVtlgnEAt-NZ11mawLkZ-kgugB8TTY_AnErJgeRKeYjuhZlgq0tvu7ojGI0HghOgXuMLvCokJAHHhVeLNxsKjHQxJab0F1cmUGfHwXFrZ305NcGGq434DqiNDMwC8-rshGXqFQISGoBX_9P7kKQd-wyZkOsfllILi9zc4e1rL8Y9OXNgk65TIB1p5wxOxHbBVzARJFlpq77dkYp3qB9ACJfZ8xbidJkgXTh9N25kt5SmH4X493Ey1KTT-yuwTqFLD3SuZZiaxFO40VncMda6kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=cBn4tRsN2VrUEV70NyCpPpaHOiIkeQtdulAMu-tesjGboooFPpjsKQsVhG9ltl8nsVtlgnEAt-NZ11mawLkZ-kgugB8TTY_AnErJgeRKeYjuhZlgq0tvu7ojGI0HghOgXuMLvCokJAHHhVeLNxsKjHQxJab0F1cmUGfHwXFrZ305NcGGq434DqiNDMwC8-rshGXqFQISGoBX_9P7kKQd-wyZkOsfllILi9zc4e1rL8Y9OXNgk65TIB1p5wxOxHbBVzARJFlpq77dkYp3qB9ACJfZ8xbidJkgXTh9N25kt5SmH4X493Ey1KTT-yuwTqFLD3SuZZiaxFO40VncMda6kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDZNV7gsZf3FowaG-vNHauJ8bkQHxVIxDNWEyThU27ab64J02QGImug4sqs0PM6uh0nrFC-tmqcBJww1frkNyD1IOXbKVz1OfCvOmzjTCJmxSjTuyhogDORZg8VgQsSYAamy1z6DceyAiIOg23dyJ_XdubyTrc8kNisUjMm4ww-uAUvlqaGtOM_o7BtJdIkPdzLbezU5mcqCqkO8Y4RS3PSzEIT_kl7xO_qCjuU6_JcullA0_Q0tpQI5Z1ImJgx_pPNmbXOXlGil9wTpSQcd79aWOyy56n2aJ6UDEomV-NW8pzVqmfiCuNThrGALZN4ROHXTPvouQ5Y1aXAzHLvmHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OF8I4YpqV1nLT4p8K80fxi3NppVu2Dz0YDiwZZslSqOCQY5128vgaxQV6u5GvcbT1xB4qYZGcpS6zbL4tH5Uqw5WA1rb8IZXMukb8SgN33GAkX_llEZsE4GuKNoMXXEmD6NEFDO_Ji-RhonsIG8fgJALeZisqvvufykSlEM_JJYMYbEMDMQGBU0h6LU9WcRUbbkdxy1eaZe0GL1zSxj2aBFYkf-mCMlxIgdvVIuRdI8Mkz_K9vC_kiFDBa8VUf07ox8SSNPpyQNa41hP5nwYAjnCV-JoPwdvsu_VYBrxEIct3Bi-3lb8dk1Udfz6vMZCLbtyPjh2wyrCU1RSSqfxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMKXrqh52Arm_6lerN20XRuzDSinLx3G3J9066sMeINPRZTgLOpAP7ZuroleIEiMi_6_RA6H96QXRY7xVpekdA89BQjwjf6PMxJFEOygstF0AWqv3Glq3S92VnnlUCdkaWClg682cnLyuAbMJf4RVvz2-4EOsaOhZVXMzcWtTcjubPvKyhgxdlsMdL1w0yWBXGsbpOMZxTh6WcdwEtzpFwaJ9PW0UOqF9yZlKfqj0em9P8h9QA7tqmvql7aIAWIbTpLraJ_fGVB6LdvIreIMnD50W2sIWcq3na_gYvnQhehWnCWfZxoDBqctiE0iKoq6l0N61AiPRSd7jaw4q4gzug.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=W2dRmKCkaJ7adGivkIPR0IlBniHZ8htrmtHpHmR18W1hw9EiEeFyY-SwiUBJXp_kN80zHXGrSrXRqDacGgT_alCSSuEfJ1CaDx77Wz8-2M-6oD_3tGIRpDKeyW6qDwYPGviEZsHOm7vi3OubED1QN-0Zkr0fMPYp6KCC8BR9_qIY_ha8zzAuZBZc8TroGxuKhx73LN-qfGwvbvDEF0vFkaWo7ss5wDb5AZ1DEvAycKu7MHpAawhOdJBN5gGMKYqzWmg112-aA0-S5Pb_RsskniW7HJ-jnx0tydbbcdnsN0IELYPku0TZNlg38tXonjeCzkAi1nm8ePky0IvU8IV1gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=W2dRmKCkaJ7adGivkIPR0IlBniHZ8htrmtHpHmR18W1hw9EiEeFyY-SwiUBJXp_kN80zHXGrSrXRqDacGgT_alCSSuEfJ1CaDx77Wz8-2M-6oD_3tGIRpDKeyW6qDwYPGviEZsHOm7vi3OubED1QN-0Zkr0fMPYp6KCC8BR9_qIY_ha8zzAuZBZc8TroGxuKhx73LN-qfGwvbvDEF0vFkaWo7ss5wDb5AZ1DEvAycKu7MHpAawhOdJBN5gGMKYqzWmg112-aA0-S5Pb_RsskniW7HJ-jnx0tydbbcdnsN0IELYPku0TZNlg38tXonjeCzkAi1nm8ePky0IvU8IV1gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=LgdQkbdaFHK58BMIEnQMmSwPJNqnfpb6Evd6DLTwPx2qD1gDSXwA5jC6Lk38QEt_aZriM3nhhmnwH6g1wLMtjXl45jpgEx000LnWdpqLMq24EtfuYztPJnXUYgWcib0_HH-uXnuT4K6L-_vdAiK_U4kt61dgr64N-XqfxkXlhTRY9m1Pm8fkRah_yWFOEYNHdwgBsNLAb0-QcmZUogDwW2-KGomXNyqWDHWh-iWdz1syM1SqnHw6I1S-FTMo9l1AoxBHM6I42aZx7YRXc3EW8kGc3rQBTnsVLzayR1mphoOjPyilxU-7Zy4cy9nO4_ON8Q0EDdH-ESAHfwRnOpOrBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=LgdQkbdaFHK58BMIEnQMmSwPJNqnfpb6Evd6DLTwPx2qD1gDSXwA5jC6Lk38QEt_aZriM3nhhmnwH6g1wLMtjXl45jpgEx000LnWdpqLMq24EtfuYztPJnXUYgWcib0_HH-uXnuT4K6L-_vdAiK_U4kt61dgr64N-XqfxkXlhTRY9m1Pm8fkRah_yWFOEYNHdwgBsNLAb0-QcmZUogDwW2-KGomXNyqWDHWh-iWdz1syM1SqnHw6I1S-FTMo9l1AoxBHM6I42aZx7YRXc3EW8kGc3rQBTnsVLzayR1mphoOjPyilxU-7Zy4cy9nO4_ON8Q0EDdH-ESAHfwRnOpOrBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=ttsJNrxb2QFRQW2yn5i7Y_4cfB4EMmd_lxkoXcK4l_K9ZwggBKS4NIkmJdUkM4uaiTfAfUwAzaBW4KoWzhv4HwMPVbFDL1Khd_g58HfMuKUKc9DmKLT1Rb52BjEItvAyl940vaBi7LoRaNb8--USVlWv8RcxX4_btI1Txy45cR2jVZCus4v2rRT9MV4mzPCviO4wYYAbC7etCAHjBJPze-laEJLHbXB8kgTnBaLkeSrrQz4bc9naXvJtGFBpEzqluyWK4CLgL7bqKT_oopyXIg28u5K_5Va7DROBvGvZUHeDuGVOMwiJYjmlTyPJtp8_p8ZlcTlYf_VH6ZTPbFmvLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=ttsJNrxb2QFRQW2yn5i7Y_4cfB4EMmd_lxkoXcK4l_K9ZwggBKS4NIkmJdUkM4uaiTfAfUwAzaBW4KoWzhv4HwMPVbFDL1Khd_g58HfMuKUKc9DmKLT1Rb52BjEItvAyl940vaBi7LoRaNb8--USVlWv8RcxX4_btI1Txy45cR2jVZCus4v2rRT9MV4mzPCviO4wYYAbC7etCAHjBJPze-laEJLHbXB8kgTnBaLkeSrrQz4bc9naXvJtGFBpEzqluyWK4CLgL7bqKT_oopyXIg28u5K_5Va7DROBvGvZUHeDuGVOMwiJYjmlTyPJtp8_p8ZlcTlYf_VH6ZTPbFmvLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ : پولهای ایران  که قراره آزاد بشه
باید برای خرید مواد غذایی باشه
و فقط هم باید از محصولات کشاورزی
آمریکا باشه از کشاورزان آمریکا.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5702" target="_blank">📅 23:39 · 01 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDryvBV2dNZNUlfLAHPDgwYPnHh96G2eB0NiBJXhTebXuMYnWVSbQXv-iaL8wL9GsrRjAOYY7vtcb0gRcYBPhJf8CF0TkKEtY5pwRWiSG2qdJzNeVnCrd3rc_5M3ZrGHB-42FfTZZCOdIarDkQMIvJozFKo187GiGVA1ipWw2gcZ5sGUmpNd52McCJSyHOU8ZwGoEDySGZavsLLdn13qdYqr4moWFf_X_5_8fzSrlCCnxTcL5wP8hnwNWrw1NvIiTgBt9SGPLiEip-tM8jVamGqlKEys4wRAQN8ynaC6CKbn0Chkz7aOFSqAcrEPb2rIEUuBC_g0o783HB2bYu5mkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sS7EDh6gCsQI3j8ssiNKUjGNhH6UiOBP9j1uM0CXK7mheMbDsoqbAJac6I5yZaSF2_WBGwCx2jUsVFLRnhWl5_wPViRT3YD1EjpqqToluDZT20xyNHI9IOFu_F20d_CvvqKhI7ELMDgiUwcQXhzXvw2YmH_Z9mbBdwvGIRLaVUqTWRrJcoJGBzD8exRpi7c-iDpUl8y30mNgzdqUbP85kQrqPPQZ4-zPLWyhOuA1NcATqAzndT2KQgAEW_YEU1lrmrW3LgcPrh3Bi4DdNiewPwFPgOf8ij0rhYWo9k5qT5UpkPxXX1o9CH8GNBq1_bpNtcAIt32ElgFmnRyU7TIxjw.jpg" alt="photo" loading="lazy"/></div>
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
