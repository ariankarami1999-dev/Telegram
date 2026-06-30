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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 22:44:58</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwtalJuI4ISK7IQV7YrAvbHJj4aZpfjdhF9SZnPXUenA8e3JE6VYZ_JgQGbOAe1JK-AzhTyC-u6Ps8BU6bRa-JO1s_WMStSN1Uv7k0F67k970czKZ1Tm98V19lLVw9QRv5st6M_c0-tNi6nh_ibfKOrsdtxJFOGxW6YmxiBJuEa8oozwQrqUZsXwLC1dqMU4371nMe5z6ufR01qgVhDsgJxFeMnRBMvBYgjtLw8w02tcuhsPJbTHlZg0f6pPtYeWjGsN6844T1At9MdsN4Y8i-AwutsrC942gOzp7EnQDrtgr47tQv422sdIF6mVPhHsfqVYxNfFEM0gpUgqxz3tvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YkPlS5eGMm6Yc2WSpo-utRTSYJ8NveD-Uz_xnXbrQ5OdIOrxaejh4CRYvlbHJijvdWWxn98GV4MadzaLXfnGpTa-prm-wjofhmQjv_pwdLPBS0uIL-6-w4udEWjpNHmXeDi2_W1wBepQswCNwdXVRXlxvmP319q2M8DCnIeZ5381YrzMrIESYlV-3pBN2MSCKLtffFE8GFvQB3MqEiW-XV4Ebomn1ZZP4GBetgeNMsJ4tKrVoPuU9I47u72Deo-xMW5d4YXMiZLm06cBEcoJHFyVGFg_YnWkrtkIbx37p-kmdDJhVdOdc7oOEoqSR5GFelXpdoqukKaWxPAmtAz5QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PKj_RbNEOApa6XNKCrrK75Gw5e6ZW1EVOpYxKDb6Ux3P_MCLKBpD8crp4tmqBODk0DBVG6X5CrJuMPlligOXIjIUDciCZGi5wMBIiN2oXrD1eezOH5TBeUTDaMamIE-US9vzUSJyExD8-cyxZsXsLI6aDalTb_jzM0fSw69jzDZjlCnxH6UHvUOi743zHiMyPx6y1y5rDgLXs3Yy_uQ3kvKpGXbUPfO9YJEfprhBXxV6a-O611YvPpu5F6USuis8KmI1CYNg5iGsKCT4vqfOx-TJlWFkGqdpVu0aQPksQIUXm1P07_EdDd9XUgLJiYadFvxxCMeLZ-Tp4jpKYEDnDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swX_EEbd8ka955gUXa8mjqa3j00ezQAkz8Wd7L1Hn8nEVCuzYntInb8g1G8PB3j6jbX4UYMq1UngMzJnI8rgc3lE54-OZHvEEC7lmVXj9eHTB40f2RWOPjlorBYln1aTS7c-p_wiO2RNOrA7kmRphQSOc0UeJaygPurCnf1Rb67TwkZ50HA1l8eTOYYvvlwCQR7ZpkYQIG4WVmRXAjTwnAez9JZILcbTNSVbzVSyCXsJDd-x8x5-WRr99AUPX3fjklB0Hi9lPLdyzpLvm9Gzs2Vx1XB-jCvs1Sm7pk8JGZla7Rbk-bZhviEfnSZg7kAgCRgsKTOywsOD2TcHt8niaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=VbTSEL0KEGOq4JKiz2dNuodS1tatNKABjZVSCPzus3UiUe_pwpn796JAeVzpnc-9e0DFUT287ZbwnEIk5Ke30dVQVOCywf_7xE7pA1DpxKUH3_uWkJ9o9fSw2izgRqZ-pLF8pSmVEnnaZ-cD1YM3lZ7m2mkaDdP2fpeJLzridHdxc6LwEsRv5VoLfx71rko5CwJ-jrrYZWTL2dcgia-ZFUWEHVjIuDdQ9q1Nn3CzuGeWyeELNj8oqzv487WrcDJ-lIJZFci_0bq7eyrOjFsMHfw4a0T_kt8KPMMsZhIfBgMlfOpGSObQkyuJhAhi2tUxbe50cgQYMn8XAbFnwzpWOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=VbTSEL0KEGOq4JKiz2dNuodS1tatNKABjZVSCPzus3UiUe_pwpn796JAeVzpnc-9e0DFUT287ZbwnEIk5Ke30dVQVOCywf_7xE7pA1DpxKUH3_uWkJ9o9fSw2izgRqZ-pLF8pSmVEnnaZ-cD1YM3lZ7m2mkaDdP2fpeJLzridHdxc6LwEsRv5VoLfx71rko5CwJ-jrrYZWTL2dcgia-ZFUWEHVjIuDdQ9q1Nn3CzuGeWyeELNj8oqzv487WrcDJ-lIJZFci_0bq7eyrOjFsMHfw4a0T_kt8KPMMsZhIfBgMlfOpGSObQkyuJhAhi2tUxbe50cgQYMn8XAbFnwzpWOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
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
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=WzM_YV4ZnTb-3fHBI-MdqKpW5rGtIlwep7hYsUu4-JiQFRORNT_nTNmfcIBwW-USU6QN1LSqbfkTzImcK6TYOIAvvclEQm729gPzLG8VEUzC0S_tQDYo6HqGmosgAdcrL-26NyJzCKHnORQ0pH4SDi5Qh5j7cyRstL-hH7SyAXQ7kfVZVVNH0cbJvdcx2pCcZh2MwKRHoNYa8PtiMTncc6sZQPgD9fWectjuaRcQthxz84kvQ_Pi_n2jEVxXzomqmUcNe_qOaBRWXFeHe75hM87faM2YJTYLyIVijl5FFc1dIsbvRfH1euTCi_LlyZ1VKiqhugYMRU0dTvjik-fgbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=WzM_YV4ZnTb-3fHBI-MdqKpW5rGtIlwep7hYsUu4-JiQFRORNT_nTNmfcIBwW-USU6QN1LSqbfkTzImcK6TYOIAvvclEQm729gPzLG8VEUzC0S_tQDYo6HqGmosgAdcrL-26NyJzCKHnORQ0pH4SDi5Qh5j7cyRstL-hH7SyAXQ7kfVZVVNH0cbJvdcx2pCcZh2MwKRHoNYa8PtiMTncc6sZQPgD9fWectjuaRcQthxz84kvQ_Pi_n2jEVxXzomqmUcNe_qOaBRWXFeHe75hM87faM2YJTYLyIVijl5FFc1dIsbvRfH1euTCi_LlyZ1VKiqhugYMRU0dTvjik-fgbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6lKZVdvD8uYMowGHb04GYp7qj2LfhEFX8iX-s_JLZgJw_Miibbuo-otTOUfDNOE9gZNNLi8F-RZy-v-h5ZzvPlDw7ViqjCNTkUHDMJ9SM3Qin-sixVLXn56ZPPeRlN2oMIq9C1-UXcTWOVxTyIFIYRm-TRMbSVekySi3feh_Rg99SJrDkXA4loNiXYMZi3txtUQTXETGJQ2bxw6yGInrTUb7Vt6mZ78LKybsQ5vxii67KCZP30nOt0N1_Lhzs6xMqs4xFpp1PoseT8KdJ8aUItGt8K6JF6ts6yb_hUmiaB0J4pNUUUX_qshgypNXMax-9Ce0pa6kAiGddkvg3vTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEd9GG0AnYOrt2LOlEdUOkf5JxkTXVrk7QeTXdMVq0K3Jf0YpoP07Z901vcTQX3UQFodMfCi3_K-oyFqIkYj5vPn1t1Je9sSSwELoAjbBPp8idR_HhthH65xOWP5hkWmSR2ofEuo9MDyU8kiBf9CGqBvNh4gNGf1ywYHZduhvWMgD-UU53IIlgczztksBDPGZhvKDiyWHnnxjCVnTKrYUevsBAeE1NpYPPYBhjmaXc3wJ2bsSAWG1LQ5Pufi0v7JCmk57oliIFfhCWoPnYRdL0Ox8LrXJx7tSJYr2TTzBLiaAdAb1hW1BIi8fzkC3kpm6q_QJJBfVclrt3bN5D6Tfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=kRGlDSh4na-lWQqm586cbVXR7ANzao-vRKYjVCGPMo0jVc64trgG3yXYIEGkbzCmCaLi1-K4aPRedNc855jnJOpSzIs5TYVdtl_Fd5jidD0eNSpmFb0Ah9MX_EKYBPwcHCRyrMhsXekqO9BrE4MCa9jLFx7GT6yiiVvCg0hDdjVGHwRC7squiXChDbOBy5F72pHEJLnrP715T8H702WZLUEBDfpuoPaGFZmZvy7Gaaq0E1Qhq0aaY3HTzNskL638rSSXBeiE-lLqw4oNjAoY5PHo05oEmn3rQrxnAI8MArPhw3jdWuMJvjKeHliYtIVsBQGpnVcNbtcZDdB5uqdWNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=kRGlDSh4na-lWQqm586cbVXR7ANzao-vRKYjVCGPMo0jVc64trgG3yXYIEGkbzCmCaLi1-K4aPRedNc855jnJOpSzIs5TYVdtl_Fd5jidD0eNSpmFb0Ah9MX_EKYBPwcHCRyrMhsXekqO9BrE4MCa9jLFx7GT6yiiVvCg0hDdjVGHwRC7squiXChDbOBy5F72pHEJLnrP715T8H702WZLUEBDfpuoPaGFZmZvy7Gaaq0E1Qhq0aaY3HTzNskL638rSSXBeiE-lLqw4oNjAoY5PHo05oEmn3rQrxnAI8MArPhw3jdWuMJvjKeHliYtIVsBQGpnVcNbtcZDdB5uqdWNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0g7HyqoH2znWUaZnHbnFoDOWmRBHDtA1JViIxsCII2-yXpKKd7XksqoCfBbedMgq_uwLe-xaf58tlHQ9Rh4_MvRvPqmns2Acfrb-3XE9-suJUj27C2jM1WFUFG8ooSEqRg1h8m_LX4dlKgD2LwIofAacIEzZOADrxGFRKv0ZDUcheJ4xKDKm-P0ex_deoC7XSS06vgXj_gbm_8Ie25n7P-tUec1rMMv7PoRWdpmcylS-xUtJSahx0yid_Gs4z-WIyh4D9QYaUsNCxl7raYe9H1hgB7yGXQgthP6HhypMWV-JJBAdfn8-nCAAS0-h7GcI1noqMwq6CetCZ0P6uHnVv0E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0g7HyqoH2znWUaZnHbnFoDOWmRBHDtA1JViIxsCII2-yXpKKd7XksqoCfBbedMgq_uwLe-xaf58tlHQ9Rh4_MvRvPqmns2Acfrb-3XE9-suJUj27C2jM1WFUFG8ooSEqRg1h8m_LX4dlKgD2LwIofAacIEzZOADrxGFRKv0ZDUcheJ4xKDKm-P0ex_deoC7XSS06vgXj_gbm_8Ie25n7P-tUec1rMMv7PoRWdpmcylS-xUtJSahx0yid_Gs4z-WIyh4D9QYaUsNCxl7raYe9H1hgB7yGXQgthP6HhypMWV-JJBAdfn8-nCAAS0-h7GcI1noqMwq6CetCZ0P6uHnVv0E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=ayQbNcAoLSqp11hWiuXpa827m1gH9hP7MYRV8SAcWmoz6-n_PnEgGqF8kygiFUxgNXZ-anjvbFh8_r1nrQ4hA9dYymu8mDJKTJjfiGsSB53WUKVAYVNVbT54aLo_j1KMI4q2QFs24R6Hro_pH8h5TneWSP2YTVoNH2oXhC7cbPtuRGW8IYZ-waEvuJFJkS2YBdLuLR3IMpS9w3I9DudAOGv0Jv2xstcG3iAIiLYKrA79NAgjU5t3uiG163Gpuigc-jBINeUGF3vTuTgkmqf0cJWtpgzwxzEyzh7yrG4PTgipNTskYw5ko3xhRJ8Tw83Wxlzit2GJRuaoo5cmG7nRsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=ayQbNcAoLSqp11hWiuXpa827m1gH9hP7MYRV8SAcWmoz6-n_PnEgGqF8kygiFUxgNXZ-anjvbFh8_r1nrQ4hA9dYymu8mDJKTJjfiGsSB53WUKVAYVNVbT54aLo_j1KMI4q2QFs24R6Hro_pH8h5TneWSP2YTVoNH2oXhC7cbPtuRGW8IYZ-waEvuJFJkS2YBdLuLR3IMpS9w3I9DudAOGv0Jv2xstcG3iAIiLYKrA79NAgjU5t3uiG163Gpuigc-jBINeUGF3vTuTgkmqf0cJWtpgzwxzEyzh7yrG4PTgipNTskYw5ko3xhRJ8Tw83Wxlzit2GJRuaoo5cmG7nRsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZNh-eUjENGQfk8apxCShzT4UlDWZJuRCMIUwh16ubR3YjpzPCh4Ot-l5b8SiBmrbllYI_76wL-o8m7XiSsjxqLASyUz_oEQXXvCIpmo50BY-Fw3-Rjzz5jqq9Ql3uj-50LXLbNapHn98tIer8b7xvmqR4ZgT9XR_l_iPAnhLtfEudUw9zw4YIYCbKL-O3JrDgyl-dUOZ0eGbOmleoSLJkszHCZyI5ZMkmijpqer4TMeVDJ9-Ev1HkgdLj98j7Ro_cnxSXCWVIcPmnbNmmx3GpvZP-UEb8wcG4RN4QZo8DIeSxvuJe1G6DKCAzyiEjRVB55vOJdHLBlmI7pUyXvUxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=gdAbsEbNVQQj8-Ux2P_9pPOt2PvR9EN8Et350fiQ7FKdmWXaEoKMIRI6lM5VdIF_reZG0nCDrGVZknxvA5U_6xdUhsJWadRx1frCQSgjEoALDexJm8DVYAmxmpL-2taLTSrFFHMXr8y0163gYeQa8Y2RFbbMq8M98OLaaxiG0RCz7sTmzyMI2blIugkMd_RsXrx68OG0EZ97RsRZafeJggmUenXqpzTpz7iSHC4MbYbpwA4ve48U0SQosH1jVSTIGEvgHxL9LNxk4ClFb7NdTN4FUBXRzUq-NMbIPFuIqzxOc64WSfvj2mbd2_CUZXBg4ZiLCgIMIDHJW7yuRfacPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=gdAbsEbNVQQj8-Ux2P_9pPOt2PvR9EN8Et350fiQ7FKdmWXaEoKMIRI6lM5VdIF_reZG0nCDrGVZknxvA5U_6xdUhsJWadRx1frCQSgjEoALDexJm8DVYAmxmpL-2taLTSrFFHMXr8y0163gYeQa8Y2RFbbMq8M98OLaaxiG0RCz7sTmzyMI2blIugkMd_RsXrx68OG0EZ97RsRZafeJggmUenXqpzTpz7iSHC4MbYbpwA4ve48U0SQosH1jVSTIGEvgHxL9LNxk4ClFb7NdTN4FUBXRzUq-NMbIPFuIqzxOc64WSfvj2mbd2_CUZXBg4ZiLCgIMIDHJW7yuRfacPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=bBE-oPE8Xq4kO2EqWLMqw8x6jUldlYVbV6SgxWu3-9IbCRcFOjjB7BPNKnpOJiiGFpLz5eXcUAJfkBXAAGPzQZNy6wQfIK46V3qJoMiAZoKYK176s0yHyrOPykLsegLRzcyJ_o5nWnzlG3OijWv5UOQuYwleBY0MvSGUD01DZ4KTlBRrcmNnrFroBh0T22fJb3MOQ_02gLpfDBOSAqjVVhMUNoECsabHgIdhS2szTq0K1aV6perhOHT_Ol7bN0LU-QK3PwINH2mX3MSaqjjVRbHOMR5lwWp7i0AVEvcbVeZVjMIpUkY-6L3ICinfP0XVB_8UJqbuJoGLjj0dFzBcvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=bBE-oPE8Xq4kO2EqWLMqw8x6jUldlYVbV6SgxWu3-9IbCRcFOjjB7BPNKnpOJiiGFpLz5eXcUAJfkBXAAGPzQZNy6wQfIK46V3qJoMiAZoKYK176s0yHyrOPykLsegLRzcyJ_o5nWnzlG3OijWv5UOQuYwleBY0MvSGUD01DZ4KTlBRrcmNnrFroBh0T22fJb3MOQ_02gLpfDBOSAqjVVhMUNoECsabHgIdhS2szTq0K1aV6perhOHT_Ol7bN0LU-QK3PwINH2mX3MSaqjjVRbHOMR5lwWp7i0AVEvcbVeZVjMIpUkY-6L3ICinfP0XVB_8UJqbuJoGLjj0dFzBcvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=JbdE7t0vldeoDxQcILmtXNjzkMFnT_ic5_pdNkYKOlJrzM1CXFkSZZ4bujpCA5wE1mONH1e4GllpIfo-D9zxOhTpDncLloT1g3jPrhatcmt_d7LmIOV8DsBnPAUhLVs_hexxOA4JUXSpRl65Cz0CQ_6rJfvC08OKfnXEdy0p-zX3WhP7ZR99vMMTVJw_Ar_Lgw-HWALt1BuEYGCOB_73FO-H1Nt5nVgSJCSNlAyFR3WlBGynu-S8TaT9xDrNxNlxoP7gxMrp5wNR0-Fg1LqhZwyv7DIwmIMOgN0As8LrkblUpkFFg2qFYtQsaPe-anPoDBwv5CSc4rceAWmpljOY8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=JbdE7t0vldeoDxQcILmtXNjzkMFnT_ic5_pdNkYKOlJrzM1CXFkSZZ4bujpCA5wE1mONH1e4GllpIfo-D9zxOhTpDncLloT1g3jPrhatcmt_d7LmIOV8DsBnPAUhLVs_hexxOA4JUXSpRl65Cz0CQ_6rJfvC08OKfnXEdy0p-zX3WhP7ZR99vMMTVJw_Ar_Lgw-HWALt1BuEYGCOB_73FO-H1Nt5nVgSJCSNlAyFR3WlBGynu-S8TaT9xDrNxNlxoP7gxMrp5wNR0-Fg1LqhZwyv7DIwmIMOgN0As8LrkblUpkFFg2qFYtQsaPe-anPoDBwv5CSc4rceAWmpljOY8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=XcNBeq13d5kGVJOEaBMlyie96DQZ2mxQL4XpTr6euFzhk_xwFWd95LIXG1tV7oJgrVDsAFzC4BSBs03i6eahZ7LAy14pf7Tc1-N2R7W0d6yeWkvxbuS6SJjkhunklbZCMaXlEzsZhgevppN2E9bs21shbFknQTCZGS3mnR2wtjAqVV8aiMHeF7IhNVVFUWiBkJT5wueJyyRIc9F_mudEoCFkEy0ildYwmYo3xYrdzCZJFMQd_0TMGg8PU1EI0ZJ7bwk8iremcQAXnpbwcAnYsxw778FwdbEujNe4l3DrAJnQXI0bnJPo-0eJxCqnAIeMM16vVcMuZXOJigZhFKgWsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=XcNBeq13d5kGVJOEaBMlyie96DQZ2mxQL4XpTr6euFzhk_xwFWd95LIXG1tV7oJgrVDsAFzC4BSBs03i6eahZ7LAy14pf7Tc1-N2R7W0d6yeWkvxbuS6SJjkhunklbZCMaXlEzsZhgevppN2E9bs21shbFknQTCZGS3mnR2wtjAqVV8aiMHeF7IhNVVFUWiBkJT5wueJyyRIc9F_mudEoCFkEy0ildYwmYo3xYrdzCZJFMQd_0TMGg8PU1EI0ZJ7bwk8iremcQAXnpbwcAnYsxw778FwdbEujNe4l3DrAJnQXI0bnJPo-0eJxCqnAIeMM16vVcMuZXOJigZhFKgWsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0fBa9D1UzW9B7B9EJdz44GQnsOFRn8GxmAeWvboqsBL8FdAQXelPprOJhGnWRFuAGCV2jxZcJtkleXL5fHCPGAWLBxIS1WKB54ko4A7HooiCfD25VfOPdLesQBeEBwLm4Tp9uXsj8Wdu31P1K9N2JgBL7zDpaVDEmcqS-9COzwhJlf1UiDzoTqUr-tpllz-nRI4mVO3fJ8VlwGGO3rfA4-GKTkfYqOF1xEbML2GyxsdxBqpLoMFVcUM847GA2GHHembeZN4SlqoIgtJibeAWqcYo22Zruj0lAS3eLIChBo3qlB9zU7T7A-suPTbH1DuRBWNbRnENGsY5ACShtkI0g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=Hm49WV_GYQedwG82MFSiR02PLJIceouqtz45JYuiTCkXmDH_8ArqLonRU4OLsuxRkDtjpgfPBSTRuoJdRSGmwACxsTra9W6j-YKg0vL2Y2XA5uOIGnnt_AvnIt7ZENMh1KRnOeMRTk-aq39utZjOcQLfmkyDkQ7nQ51Mri-NDrGO_0bMNJcvWjUU0Xp4olI2jTR3vAdiT2Lch9tfx1So84b1iLEXQQgqZbUg5JylXtqQGsp0PgwYi1ULbJweiHCuNjqILCEKYbX27LLljkNd-Su8DnSznOznRqBFZfNRvAMQECcC0dlHMNygkMgpqiTSH8gg0qiRnyxbg_zYYfZRHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=Hm49WV_GYQedwG82MFSiR02PLJIceouqtz45JYuiTCkXmDH_8ArqLonRU4OLsuxRkDtjpgfPBSTRuoJdRSGmwACxsTra9W6j-YKg0vL2Y2XA5uOIGnnt_AvnIt7ZENMh1KRnOeMRTk-aq39utZjOcQLfmkyDkQ7nQ51Mri-NDrGO_0bMNJcvWjUU0Xp4olI2jTR3vAdiT2Lch9tfx1So84b1iLEXQQgqZbUg5JylXtqQGsp0PgwYi1ULbJweiHCuNjqILCEKYbX27LLljkNd-Su8DnSznOznRqBFZfNRvAMQECcC0dlHMNygkMgpqiTSH8gg0qiRnyxbg_zYYfZRHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=rxsMCU1kdmnYeYH9K8qWMG58hVsZn9uCjuXpAb9PryqknaM_R695s9tgE4C0c_k0ty0-_8VIRXS1om80h-qZRcLIPvN_4_enw11R8SMvcrCpbFOjFU0VH8nwytaz5relTtzG0U8HdPnAfjjyPGStEwzLT0XVBeGXrBBiOJu-vmH_18F1YII1f0WFu9MIjOCINKqisbI2g8g8QjczEZmk_e-NVmncYeJCiaMy2HZ7iqGxboiCFRyfBecQlBG3oCcdl9ZVnZZIUDiejsTpLnMWnTUgS7xygycposYu8BRbWU7bLTCGWWSQg9P_nv5f9qyxbiy3eOBy40hosPSiEEIsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=rxsMCU1kdmnYeYH9K8qWMG58hVsZn9uCjuXpAb9PryqknaM_R695s9tgE4C0c_k0ty0-_8VIRXS1om80h-qZRcLIPvN_4_enw11R8SMvcrCpbFOjFU0VH8nwytaz5relTtzG0U8HdPnAfjjyPGStEwzLT0XVBeGXrBBiOJu-vmH_18F1YII1f0WFu9MIjOCINKqisbI2g8g8QjczEZmk_e-NVmncYeJCiaMy2HZ7iqGxboiCFRyfBecQlBG3oCcdl9ZVnZZIUDiejsTpLnMWnTUgS7xygycposYu8BRbWU7bLTCGWWSQg9P_nv5f9qyxbiy3eOBy40hosPSiEEIsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9dngFZ0dr-QPLOeDypHPfX9HQsJ50WuZWAOUjsJOtyQ_JGBET70HqU5cwNxv-OTiS-FF8SJdiF7L8sutHPWccEO7MqivFyKzhuURI2hQ3z2wllZRkmITMKKfoIx7Z9bDJo8FRZ-Bfuv5e6BEs5bmOmxMgGH2I9RnRNbc1wD_y_6inokWxtPnwJIwH4UzTZpHU2dwd26HLcx1JUiYl7czpkz-v1JAPrWFw9NwDA81l-MQumLjD_clxLPteCpA6eMwBvP29uPwEvsr5mtw39TKM4A8Gri_ZwNk6YYHAxcssYVBpDnkEtl8pvK8clU-QtlQiTp1lKGqEyU6N8-fvZQfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=BPcM3d6XK5MA_BkhPHfuRX4wgptxMdD59B0NcinZRznci4Ai3HQr6DXwqxHibL6euqI51aV_LjKXolviUyX9avC2NfMsARCYNbnirgwNFdN5tZVN530gIiuujOV0RbGasRjPCQtkgmUQhffmf1bTEIMBbVQn2GVUyQzLE8MMmuQPlxRcubEMZ84UQCBF0csnQ2YpjhjFbaKWvlr6GnyUM0aG1kAdNKQAES4wvOMVPXbvHZLoCSKtRl0Es6s89gh95bH_HXG3QYaBfis6p2ixmIUC8QyCuISVYMtPvGO6oRiyahgPvpRPMN8gdY3zAzI-D0932cVDtKUR7uKplHzfkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=BPcM3d6XK5MA_BkhPHfuRX4wgptxMdD59B0NcinZRznci4Ai3HQr6DXwqxHibL6euqI51aV_LjKXolviUyX9avC2NfMsARCYNbnirgwNFdN5tZVN530gIiuujOV0RbGasRjPCQtkgmUQhffmf1bTEIMBbVQn2GVUyQzLE8MMmuQPlxRcubEMZ84UQCBF0csnQ2YpjhjFbaKWvlr6GnyUM0aG1kAdNKQAES4wvOMVPXbvHZLoCSKtRl0Es6s89gh95bH_HXG3QYaBfis6p2ixmIUC8QyCuISVYMtPvGO6oRiyahgPvpRPMN8gdY3zAzI-D0932cVDtKUR7uKplHzfkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=MUKlihTHkTPSrI0orUyGgZZUVHcVZMEtc5_1AS-AbQEkQiXOVwnocbuCYuH9oEslvE1Z2TBK9xgFdwOFsJDpZFVVbe53VKGK2xFTyVb3JF5BFytmgbwWqL1wyfLVpCuAkH-yUu11z4piZdXSkn4-6yO3en2j6X8WhxKo6UtIwhJAr-Pa4pd9R01i7w6b1-Lul7dAP6lejo6sQSMuLapjSSS8vjIWTy9r52OvrPJOCBzkXpkEgieg72J8V42co7uURAeFD8J5DsBY87ASiajNQsFrCp63gJOKJp24WhmrxFNoto7Usd0Rauo-xa0Gr-2YBwVE9J_tGdmw_nTkluj9_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=MUKlihTHkTPSrI0orUyGgZZUVHcVZMEtc5_1AS-AbQEkQiXOVwnocbuCYuH9oEslvE1Z2TBK9xgFdwOFsJDpZFVVbe53VKGK2xFTyVb3JF5BFytmgbwWqL1wyfLVpCuAkH-yUu11z4piZdXSkn4-6yO3en2j6X8WhxKo6UtIwhJAr-Pa4pd9R01i7w6b1-Lul7dAP6lejo6sQSMuLapjSSS8vjIWTy9r52OvrPJOCBzkXpkEgieg72J8V42co7uURAeFD8J5DsBY87ASiajNQsFrCp63gJOKJp24WhmrxFNoto7Usd0Rauo-xa0Gr-2YBwVE9J_tGdmw_nTkluj9_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=g9jqFvUDpXqyVZl1FXx-9FQN8p5uTdOBVg0QXjem0gVaaE9fHx8T-E3lHN3i240xOYqvPXER1kLl2hjS0AIEWD7J2yZwC2hulUqZg9T2hvDxyawdm5cqUSxhUEgvQZf4mXWjOu-yOHWa1mrWD9SA06e9FRIqokevcEF87l-dDfH51Jg84H0VKpCZsH_bJqGbPqvmR0cgISXo-k3yOmYxvCpO02OChuqjDCiZn3bBgK7eiOWivZW4PkQ7mlhSwGq9Q8RA9WhiT6FSD-HjyWeso5NDXO9DhSL1q9VK5R2Vdb7ze0EdfNu-OpJC995yPsHyBrB52oXT27iOj3qLhfsDKzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=g9jqFvUDpXqyVZl1FXx-9FQN8p5uTdOBVg0QXjem0gVaaE9fHx8T-E3lHN3i240xOYqvPXER1kLl2hjS0AIEWD7J2yZwC2hulUqZg9T2hvDxyawdm5cqUSxhUEgvQZf4mXWjOu-yOHWa1mrWD9SA06e9FRIqokevcEF87l-dDfH51Jg84H0VKpCZsH_bJqGbPqvmR0cgISXo-k3yOmYxvCpO02OChuqjDCiZn3bBgK7eiOWivZW4PkQ7mlhSwGq9Q8RA9WhiT6FSD-HjyWeso5NDXO9DhSL1q9VK5R2Vdb7ze0EdfNu-OpJC995yPsHyBrB52oXT27iOj3qLhfsDKzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mA0yPMwnwdZvm8MYFe7jz1biKaVUMuCf2W5q_qWKZlO7If9SEawV-kMX-3AW7R844ZHTnPcknAEtdK7pzgesrS6hfTgSDXdAAN3Ks3yZCGyFPLUdHXzE_DB1IN3J_subUDGoSPnOQn1GsJuHmZbOgE3-Q9aboAuOHYQJ1MOMUkx9iyXQD_BPuQp7KZAwz2Xuh7KYJBhz7G1ky1ZJJpnLMACaRT2OpWK9SBQTjly32p3xr4qA9AZ0ayljLYQil7kSd9xGQn__0mmYXBAQ7cQJQOqYU_pKqIbDs2KBlFyn1-kIQ36VE5Mw8Z6zWVzY-aZSpdh7rkl6kMSJehD1bkiEdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SlyjyBf25Cp09zTUFirYYQaPS22_xrIZqKYLgALvEKw85ESW5cfwkJd9YA_OgJBzzyrQmfaHEn6ajNX8Fy5je3rL-ZiuWefXN12ODjRCZTJLi99B5uOHSq9uKhErBZAEU_YjDt69VFRCtEuSuufGALo3prljkQRZ3HaMctSuL2JQ6GyZLw_0QU4ZRUJjMeJggLbQTeU88vIeWBLpsnQcFW5ZXlLbjbxQhOcU6blmLqT1y6ctoTPKooUg0dKjT6yj5ZTX6Tp8gPyz76gZ8zwvh8OViJi5kU6uyXsgdkiU4fs-TXClPr08QxjHYXoLHIipE4FSg6IiBKm5PoLkRE1wUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j2yEcyPU2ICQR9IZDdzFtoH8tLGUJWIp41AHmHHR5MWFC4lyOJzj6ivXy-Oha2-GCumYR9MnW5AzeQ-hcZPKul-TS5b7g3LteiP1Ytimi29YENcJTo0B_eZD_g1LLeSVoqCiK03V_zv5KT65-IkJTgPNxjArNqjtG14tGzAwqZIBCryS9apKcLdrg_AxIQNRSZHiLndBkvsV3iJSn4hNjNOrmch4Q_L8FMEFbZhdB2oKVEbkgBwFiWLil0d_j54MQ40KO_xK_57JV6NhwvcjrsUZ3CZCI7WOWVhRcyfaR7mRn8YG1jselnUR_2Nbwdgs7tZM6lotlMFkG_MVM4p1uQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=voR4z6RMhGx-tUqubklUPjnF_7RSIBsSbRgupIObgPWVoZ5fU2yVNFIjId-hUBMAdXwsmQc55_HOArb1CpkBYOo6DfMSmGmVbzbGtYROrTQ8a_Mf4o22ICD8YD808iPD7cWSIzeNzus5peUK9b_sU0PQsMsIihVRbdSWZ7aVTQ57nIhx_CqGRWaVCRthFC_VG1DkXvqdY5BpmHj2X0meqyJE4m2ZF72xpKqtngVerrRiYsey4qrYjEtriFjRw7TyCwh-zIOqNCPfuac3sbHznCsqHYa6yHStOWN6melDNteP3bUYmShu0pzJe-qfynuDgVfPbnVOZy8ttzFJX2HVMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=voR4z6RMhGx-tUqubklUPjnF_7RSIBsSbRgupIObgPWVoZ5fU2yVNFIjId-hUBMAdXwsmQc55_HOArb1CpkBYOo6DfMSmGmVbzbGtYROrTQ8a_Mf4o22ICD8YD808iPD7cWSIzeNzus5peUK9b_sU0PQsMsIihVRbdSWZ7aVTQ57nIhx_CqGRWaVCRthFC_VG1DkXvqdY5BpmHj2X0meqyJE4m2ZF72xpKqtngVerrRiYsey4qrYjEtriFjRw7TyCwh-zIOqNCPfuac3sbHznCsqHYa6yHStOWN6melDNteP3bUYmShu0pzJe-qfynuDgVfPbnVOZy8ttzFJX2HVMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaF2rogItIwyDdYEj_rUE8fShEuaiNQzqeM-hq0HsEY7v9br6eMCM4908vrtuCkt3AE_vxxf1jIZegKAF1M57yr7UpYxZg9yiXx6KgAv4g_z2u_AcC44Ca1Fw_fJw656c8a7rqeanTFkcxBmn1-Hl0Ka2wL97GegG3uO7SaOr4qMD-K1kZb4VfuE0BRQ6vAjym5QfEOQroxM0PDu5xGOMGuoS50FxjwPkFJeUtFnyRXsKXs5bX5q2StmDcGXXR3a_jSXURK53lve1pDaFUJ9BwwgbyLp8kDNYwP8MjAOXS51IUqJ9BZX53KNhfOKZhq6EQRGhVTRc6kB30TkAhDPksM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaaF2rogItIwyDdYEj_rUE8fShEuaiNQzqeM-hq0HsEY7v9br6eMCM4908vrtuCkt3AE_vxxf1jIZegKAF1M57yr7UpYxZg9yiXx6KgAv4g_z2u_AcC44Ca1Fw_fJw656c8a7rqeanTFkcxBmn1-Hl0Ka2wL97GegG3uO7SaOr4qMD-K1kZb4VfuE0BRQ6vAjym5QfEOQroxM0PDu5xGOMGuoS50FxjwPkFJeUtFnyRXsKXs5bX5q2StmDcGXXR3a_jSXURK53lve1pDaFUJ9BwwgbyLp8kDNYwP8MjAOXS51IUqJ9BZX53KNhfOKZhq6EQRGhVTRc6kB30TkAhDPksM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=CZC29sfeuwKk2Ve5Ea3VcH90-OeTotAbKzJBCNOC6mlGFRrYkUc8p9COWPQbxSAjqFndqvSJcsnVeNCSdpVi8HfCBjIMPM6-IWScsBVXf9MkaUepkW6BEkD-HN_cjI0u8QrJ3TCFIcVpbNZDp1pS0gMFjeNNKf0rUmS_TqkRIM-y_FK39B2ejqCL489Y-qY9HxJeMQ5J34qL7qmE5TQl8PvUoMHtLYxO2iI-Uptp2jWTpDoT20M0yCR7lOYsqtXsffSpJZ_oxd8fj17NbBxESMZtbw5Q7ZnX7823IahPcWGaaX9_CqLsDP4ZYpTAb4DtsCAGbFErMA54WeBTfxKJPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=CZC29sfeuwKk2Ve5Ea3VcH90-OeTotAbKzJBCNOC6mlGFRrYkUc8p9COWPQbxSAjqFndqvSJcsnVeNCSdpVi8HfCBjIMPM6-IWScsBVXf9MkaUepkW6BEkD-HN_cjI0u8QrJ3TCFIcVpbNZDp1pS0gMFjeNNKf0rUmS_TqkRIM-y_FK39B2ejqCL489Y-qY9HxJeMQ5J34qL7qmE5TQl8PvUoMHtLYxO2iI-Uptp2jWTpDoT20M0yCR7lOYsqtXsffSpJZ_oxd8fj17NbBxESMZtbw5Q7ZnX7823IahPcWGaaX9_CqLsDP4ZYpTAb4DtsCAGbFErMA54WeBTfxKJPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jn4v1kOcPhS5vVa_IeyLG-HxWXIM3rs3B6GLGUzDXJh6VpqZfPYP7cor9pczXOatg1qu4n-7HjiQHWy2wBE1PuMqgIqVYzS-GaleN4RKVQtz_B6cV_tt1SzAsf4Eh8qRbbwrGhJrFD_ZJfes5ZYQdqX5_yFvK-wiEMP2O81e7FIdD4vb5nLao0FWKI7PbZ4UEqSAHcOJHzIRVHNfippPewcsKPeGm8YwY8rWHPWnqWLSEKp3Ofd0KFGCFtdERAyf0GfA74qO7EfV43bS0SZWSU9rhI3IW3b_nPnRSSZ70mRrRLPNDwrreYNVjxB-00tFTVk28CsmCK4BxMmMRBnAqQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTgfiy2qIM1dn4XZfkGv3FfdBcOH7afeik8WHcXKkQbDRrKxVjxJpyu1XWW7e2HLZvmmgolWl0p-bMA82jWvnAenan64ZOP9VPIG0xG8If4E0pKEIrlgA8cg77JYCLL8_BwDJaWFNTAlAtejz3nRtGqcTrtqSQAhqi9yviSpm-GrWpphqXc9XSe5nTR4IrghODnYvu9D3eu8RM8lFPtMa_fJSvh0QnLJ_n9DWqHQefNN8RAdcytnr8js6UHmLy7ddbMWfXy350ES6rcyul1lDzQa_vcQ6vZKHZcTA04ZastO6bojx5RzNCXM9zp0jmwNL6ef2TnGqVyLUtSLYNp319Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTgfiy2qIM1dn4XZfkGv3FfdBcOH7afeik8WHcXKkQbDRrKxVjxJpyu1XWW7e2HLZvmmgolWl0p-bMA82jWvnAenan64ZOP9VPIG0xG8If4E0pKEIrlgA8cg77JYCLL8_BwDJaWFNTAlAtejz3nRtGqcTrtqSQAhqi9yviSpm-GrWpphqXc9XSe5nTR4IrghODnYvu9D3eu8RM8lFPtMa_fJSvh0QnLJ_n9DWqHQefNN8RAdcytnr8js6UHmLy7ddbMWfXy350ES6rcyul1lDzQa_vcQ6vZKHZcTA04ZastO6bojx5RzNCXM9zp0jmwNL6ef2TnGqVyLUtSLYNp319Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WehA-YY4Z6U_U2nBUyykHE8dESjyzIaMoEN-nVIf0lvXhwwBIprg_a-L7sB9obEYxNy63rR2L-i5M2BoxxwxdCNcUJR3p6CiATBvfPrHuKo-3WQW05LWThGVzKOo5wsz5f8AMD1O-PiA9RZ0wEup8v_naH_Teeuc220lKJO9r1Ff5QNeZUumK3NXzNhSqeUcQV2KxtBD5ZaYmfx6BvDG7Yj80lKElD-geDqzG0Jr8OO07AF7Gn13xAKt-02g9jGj97VsX6sZI03r3A9ZvQhx_gbh9ImwhEQsNOdWD90DUFT2x2tJCiDjgyxVRlem0-krU4iCybIWlFTwLdPtDw8Utg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=cEb9ojeZM0j6tgY4txrH9R9C08EfngEATOGiKodBMiQWSl5eb4CJeMnSJf0YjHDL5IyQvZuNBtkyXVRA-2fnycF0epBr0U19ThdfAFy18ozQ_dtBNVdGCqbNZOWhepjQKidEbsFuoyyWOjheWx7s2jDK5TGGnHBrNXZO8DWCPtbhQIkkq6e6Mns4xwksk4vEFbH8m8QUjOjgKuEN-vpZtRwNENFZgTOpkMqiaV2Fs98PulA9ZG41TyPxDC3QWc67avgC_46dpYeXxwvBU3aoZhKAC9_v-YEgmxRiYrnwIjFXth0_m_RZTdNWoG5Sm3wry8ATBETZ_KVOc76-bItR8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=cEb9ojeZM0j6tgY4txrH9R9C08EfngEATOGiKodBMiQWSl5eb4CJeMnSJf0YjHDL5IyQvZuNBtkyXVRA-2fnycF0epBr0U19ThdfAFy18ozQ_dtBNVdGCqbNZOWhepjQKidEbsFuoyyWOjheWx7s2jDK5TGGnHBrNXZO8DWCPtbhQIkkq6e6Mns4xwksk4vEFbH8m8QUjOjgKuEN-vpZtRwNENFZgTOpkMqiaV2Fs98PulA9ZG41TyPxDC3QWc67avgC_46dpYeXxwvBU3aoZhKAC9_v-YEgmxRiYrnwIjFXth0_m_RZTdNWoG5Sm3wry8ATBETZ_KVOc76-bItR8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=GQ4UQInjmt3CEBH1emeQ9FKSIoUFoS-63Tzw0h9FS5EgDuxtjpo0n-Jk1PYXjz3nFkW9EdZdFUqeylatFrHeqFfI0sfmfBnRWWSWZKnZapseNkjY7urbKk1tagOHncI1y16ujo8X9c8eWWfGo4czNZ-rfVltQZ5s5f4TK0ySs9C5lOIdfrrOWKZ-VZtRRUj5PVzR4MZfNWvU9QNrdGMzvNoNh6P9Bat_z6stVVCtB1215lpL4XeGrDrCLNyvDlNX-y2mkndpPtNUwnjUUnl--APuMpOl0dZJRYQOhvjJXBCyy-u-sLv2xjv7g-xLouwmnRXN4j8DYoHRTpXfU-K4AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=GQ4UQInjmt3CEBH1emeQ9FKSIoUFoS-63Tzw0h9FS5EgDuxtjpo0n-Jk1PYXjz3nFkW9EdZdFUqeylatFrHeqFfI0sfmfBnRWWSWZKnZapseNkjY7urbKk1tagOHncI1y16ujo8X9c8eWWfGo4czNZ-rfVltQZ5s5f4TK0ySs9C5lOIdfrrOWKZ-VZtRRUj5PVzR4MZfNWvU9QNrdGMzvNoNh6P9Bat_z6stVVCtB1215lpL4XeGrDrCLNyvDlNX-y2mkndpPtNUwnjUUnl--APuMpOl0dZJRYQOhvjJXBCyy-u-sLv2xjv7g-xLouwmnRXN4j8DYoHRTpXfU-K4AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ccjb2Sah8rpYP9sc29NhF1F342wELn_AkEexg-zccO4XpqWH9tHeBZQFVLDM-4H-kUYJdve6yezkQZcoM4xkixuw3wS0BGkbXC7OGBptsjmOEccCquXuZIGccml1uzwT2VvV04e2888wui_qiKfC5KuCrHH7IaoCmHLKSTOM6wJepon3m0uR-I3ZdFKVXWL5jgpkETnktJzXYYRg0p8mFEKJYhWUzB4zkDqs4bqe04Iz4MjfW1sfizkFVchX5kVzTe1pKDxpkELcc7l2dZFlH40plA8lv_w1WgSZjwTGNpd7oW-fqK6x4duMpOhcvOWAGs672ladyo9XDaBnvwoH1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=Ccjb2Sah8rpYP9sc29NhF1F342wELn_AkEexg-zccO4XpqWH9tHeBZQFVLDM-4H-kUYJdve6yezkQZcoM4xkixuw3wS0BGkbXC7OGBptsjmOEccCquXuZIGccml1uzwT2VvV04e2888wui_qiKfC5KuCrHH7IaoCmHLKSTOM6wJepon3m0uR-I3ZdFKVXWL5jgpkETnktJzXYYRg0p8mFEKJYhWUzB4zkDqs4bqe04Iz4MjfW1sfizkFVchX5kVzTe1pKDxpkELcc7l2dZFlH40plA8lv_w1WgSZjwTGNpd7oW-fqK6x4duMpOhcvOWAGs672ladyo9XDaBnvwoH1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIb5r1jgKKYE-gpgEnENDvI5ozV13BGfSuJXatm0C1sH2lQ5e9qgRfwGz-heHevlJiwVtXuuNQCSWhFxkN5sWSw6IH6Sfcs2JnkpnnE0B8uAumZhZIYyQ7Sxe5o3gi2FGF6GjKcZJ5pBQo5ICA_GHSLUzEpMLaJgc9WlQ1JMIuncgnvb15ZITXNscg7v9XvYS-cjtgNsaxLoaqvv5rxrjD_KD2jCD7I1GtBjC7eOkz_5YbV77eyohkUmnLscDKjH3KWyDBWlaxdBrbnxTz5NgPCp8xsY7IdHS5aVKZ-k4-k95M_z8VQ5v9VIc1pmR8aCjadIG3fLav4yIL6-3MhUjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5748">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjjSvo7YmaFPSlQxaHvfzkZAWMHqDTPNAkn1xXZ2MhkqIBo5emsMysY9PGgHvtXTIqRiTa4gm2cbsAJZgsOwrDZNx0R1Nf77IUk47Kj_41tQaTh8CHph79azQHn_kSJymmaWM9d_6chdLAsY85Qo6ntz6kBj7843yS2AGy_QzKzTOn4B6ftvGFHHapDgQvLxgKTrsHMa3YYG3cHzecKcwaX3KpM7Fbwj2qKU5PPvsGrfebZjrFPZyvQfwddoLM9fbrh8XkWzfpdVHysynihoH1RFlujmtL7Qwe26BTZVtFUe8BpVturFWNxE0nJZuRoGUnnwHaWNqA8EqQMLokK-nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/5748" target="_blank">📅 00:59 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e245d71920.mp4?token=OMDwRB-y2Cx1Y53MwObYef7nSVMr5zEQzrH56U0zLYG8kXkhG7KxbAFAbBxyZ8oLhrgKn7sbRA1BF7XnG4Icmnthh7eFBiFXGUOxxzlX24vOoI1hi6MO4abcuTRnR0m0JnQLGrHyK_gmDQTos22JZSszX9jKJBgrVfgtb22Qe4WcxwWJ0xqnS8VXZfFWW4qbvZQscflxRFDoqopMxYX73zgAydI4eZLigYjF_k0TdTUH2XDrbAPM8FftRF425kl9EDyNcJzgJRimZM56JWP3W8WpDSg4kmPUk1JKbPqXMCGk2BVpC3GwGjgNnGYi9Zp0tUruohc7kLM85fe-Jchiqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e245d71920.mp4?token=OMDwRB-y2Cx1Y53MwObYef7nSVMr5zEQzrH56U0zLYG8kXkhG7KxbAFAbBxyZ8oLhrgKn7sbRA1BF7XnG4Icmnthh7eFBiFXGUOxxzlX24vOoI1hi6MO4abcuTRnR0m0JnQLGrHyK_gmDQTos22JZSszX9jKJBgrVfgtb22Qe4WcxwWJ0xqnS8VXZfFWW4qbvZQscflxRFDoqopMxYX73zgAydI4eZLigYjF_k0TdTUH2XDrbAPM8FftRF425kl9EDyNcJzgJRimZM56JWP3W8WpDSg4kmPUk1JKbPqXMCGk2BVpC3GwGjgNnGYi9Zp0tUruohc7kLM85fe-Jchiqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان گروه تروریستی حزب‌الله
در اعتراض به توافق دولت‌ لبنان و اسرائیل به خیابان ریختند
بر اساس یکی از مفاد این توافق حزب‌الله باید خلع سلاح شود!
اینها مخالف خلع سلاح هستند! تاکید بر مبارزه مسلحانه با اسرائیل دارند! جنگ رو شروع میکنن و بعد سریع از همه دنیا میخوان بیان مداخله کنن برای آتش‌بس!
خب مبارزه کنید!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5745" target="_blank">📅 00:49 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P4ZTXvCbH6Er29jXXAYgAqm7_qnoK4dxzpehkWqzfdPhVp4IFK7hfHjilLU3cIdLaZ4R4BhVKI_USIr-7Q0ZqTV3RSZTJwlDrR3HYh5RvaX1XxslsuNsQwX3PeUddUO8l-gXeBGj3qHe9_leMbj5-KC5T-ov-0u6CMjDUIxWw8XfxwX-j4iAccifbT9Wq44Dk--Pnix6Hp-3rcAUS_hCSKVuJK8pchh3mSIWxIcMrgtVEQmLn4S0blxPhGL7DrzOVuScGttr0cYmxkDKYGAH1-e3WwIw4bIZ9jMMJqGpXj0lXqK3xcswaUdPqnGxOiLbWt-PzlvzCGsj6EF_AJBJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5744" target="_blank">📅 00:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACZgM2dl8IrkcUdJ4e_dfln1csyuWKrigRLjdQhLdWUUY9emXz2YMv4Djb9IB1D_71PEQt8LwQORkJ82XosJ-lFWiseRbys3yvLdM-85TX3XSY9b86bC1COVDQ2T88mTR54ghfVQgZV-iaoe2BnfTKX4l9YbG70xJLFWeqAJBj6qFr8Ev8TI73A0g6nY7ejp_ILw82QiwdnUGpNRMEnjL3mHknvx659JUBj7Cs-wVhtNWXFpegP07GYRkcDkkj9mSzHlk0lmOk6rG9LJhCvLgLeuaYbZtYK86BJwenp60_vM4hzRTE8qXYv7XrbG8pb1xxQMHdbBreHl7MzG8Ae12w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=lDUrQaYzD8tkamiLkJXPn5xDDjMEYXqHeDz7PStea7tATol0qX3ZIBEscsTZ-iL3gxHTSgrfSdIdZfojBM1FjanOsAH5uypzuHfOT7NLX6V17uG_sf-G111TJ6TxkHAALydNfVWI1Cf0f2DKmJFZrzJbf6Qqg0jf2ejBkuVYnNuuB2SCM7ZKdAtvWIUq5vk6GNekp07cBHn9HzvQmI__SKcBBb9QAS9QywH6agkQhtkBTzYIq5t6KZekuQBPO2GSg8VsH-lCgJUCYenTjvCQnIZxZPA38ER-wq-w7VUz6i_O_CBTQ5eMHYwlmkwzp7pdAEY-XHL_P4sW5PkOWzejFESng33Kh1WB6cRys5JDM3GSmq5B6pOc9e6sbBLH5J3lVi51efOXJKiZWvYMpyDPrYVGVn-GtevBbV-4JYb0qNgktzRMumQNQhZ2jSi7HNa3hslx_HJ7i_O6hdvqEtlYvujgilfaXioBm3uzbl6CirqmAGVNUImoLP6QawLxBmlymTrlXaYpk_p6nfFGzx6VuqloH_nCFaOOGUuKw0DsAnRKomvgx48ol5kaybux8vluBG2e-sdDX72Jvy-5RcxOTtuLbovBKMoPwcLHm0aUvEx5WO-y2UkmkxjZVKqXBdf6rauoP3wQVPQCkDNkwZUhmIDijO5lCjcqKknu1q6zsLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9a1f1d75.mp4?token=lDUrQaYzD8tkamiLkJXPn5xDDjMEYXqHeDz7PStea7tATol0qX3ZIBEscsTZ-iL3gxHTSgrfSdIdZfojBM1FjanOsAH5uypzuHfOT7NLX6V17uG_sf-G111TJ6TxkHAALydNfVWI1Cf0f2DKmJFZrzJbf6Qqg0jf2ejBkuVYnNuuB2SCM7ZKdAtvWIUq5vk6GNekp07cBHn9HzvQmI__SKcBBb9QAS9QywH6agkQhtkBTzYIq5t6KZekuQBPO2GSg8VsH-lCgJUCYenTjvCQnIZxZPA38ER-wq-w7VUz6i_O_CBTQ5eMHYwlmkwzp7pdAEY-XHL_P4sW5PkOWzejFESng33Kh1WB6cRys5JDM3GSmq5B6pOc9e6sbBLH5J3lVi51efOXJKiZWvYMpyDPrYVGVn-GtevBbV-4JYb0qNgktzRMumQNQhZ2jSi7HNa3hslx_HJ7i_O6hdvqEtlYvujgilfaXioBm3uzbl6CirqmAGVNUImoLP6QawLxBmlymTrlXaYpk_p6nfFGzx6VuqloH_nCFaOOGUuKw0DsAnRKomvgx48ol5kaybux8vluBG2e-sdDX72Jvy-5RcxOTtuLbovBKMoPwcLHm0aUvEx5WO-y2UkmkxjZVKqXBdf6rauoP3wQVPQCkDNkwZUhmIDijO5lCjcqKknu1q6zsLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه خورده گرفتن که چرا میگید سگ هستید …</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5742" target="_blank">📅 19:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6wKbFu2milgqbkqVVR-DtO67XMt0LpHiKzno9QZ53t32DIAm1NgJGI5H22zbqSjdR85dj2PqDyVhoblI-d0JfNSMc5S3JiuMCUcxBJkAyJkAmNX3YkTFKXpaRx3tT0OsZjJOC874nAqwMdf8vcDc0bUu6X4yVYzOsSeq7r7j046tP_a2GG5nOSmzIoOW3NbAFMGPEHJrrRxeVobQ7lczWzMyS0uLFprYK5ydAElgfP-tBQeoiSnRBW2yHmyGbWLSZ3isb70cNcYXeIptPJnedDAcGDRZk-Px2ij5Geh_nrI5cppcLUcpXp9L0PU05HCWgQU11FPGlxwBx_Ym5c3rn9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad365bb7a.mp4?token=ZDr-STvQFPYHiROFw6OPE7okjr7IEHAwGcDfqUYyBg4k0-Dvk9qRQIKcE5xG2aewUJ912dVo_83a_jiYAwUcvSQphHICVJSnFHRCEsILiVyq2xA7qkuZr3bk5_ki9cNSYAuQW9RXOvqhjOSU2zL83IZYkxIZ15AIiPW56JRm1EuZ3RUKct9SeWjS-LFiZfgVlvHezTVkjslzw-S6Ybnjf4E8HQGRf9U2lczcyRXgE_g6QFYzHZV-PLIL5FT8yd0mL40Sp7E4N3lG-LybSPWDd_qpdQBnRXlbNlM4oOGZPr3XikHkTMJCVShwXA1Nnrb6TaFoTfgoL74RMT_P6d5E6wKbFu2milgqbkqVVR-DtO67XMt0LpHiKzno9QZ53t32DIAm1NgJGI5H22zbqSjdR85dj2PqDyVhoblI-d0JfNSMc5S3JiuMCUcxBJkAyJkAmNX3YkTFKXpaRx3tT0OsZjJOC874nAqwMdf8vcDc0bUu6X4yVYzOsSeq7r7j046tP_a2GG5nOSmzIoOW3NbAFMGPEHJrrRxeVobQ7lczWzMyS0uLFprYK5ydAElgfP-tBQeoiSnRBW2yHmyGbWLSZ3isb70cNcYXeIptPJnedDAcGDRZk-Px2ij5Geh_nrI5cppcLUcpXp9L0PU05HCWgQU11FPGlxwBx_Ym5c3rn9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=EPPQ4NOHqs9InM0vakPm1kF50Z1bAPLybVW0Be4bkWmyMPDC_XsvwQR9A2VI7mYbLQuvtiryGp4IbXaoYy2_beKJf-hvV9svTXWVgq9hqtj-KWAQDl-weXCbMeC_JvLd36c1BM9d7dRkSEY_byZLyibsHILWXFwltU3a77_1yqDVFn35MpfIO-AA2QiuM3eTRk-WdOPW0mMT8b7aIlkV-gclpko9ztxeIqha8wX_LE6hZcYm9h0rD4idXQDYWf2tBEBI4UjltQA1H35JdaZg9DzEKqHdcpGcfJpuicsBJAid8wsTnz-TdBbeUOr-ANSWrngHgDMOV5pAS7zrSKgO5oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/726fb491ae.mp4?token=EPPQ4NOHqs9InM0vakPm1kF50Z1bAPLybVW0Be4bkWmyMPDC_XsvwQR9A2VI7mYbLQuvtiryGp4IbXaoYy2_beKJf-hvV9svTXWVgq9hqtj-KWAQDl-weXCbMeC_JvLd36c1BM9d7dRkSEY_byZLyibsHILWXFwltU3a77_1yqDVFn35MpfIO-AA2QiuM3eTRk-WdOPW0mMT8b7aIlkV-gclpko9ztxeIqha8wX_LE6hZcYm9h0rD4idXQDYWf2tBEBI4UjltQA1H35JdaZg9DzEKqHdcpGcfJpuicsBJAid8wsTnz-TdBbeUOr-ANSWrngHgDMOV5pAS7zrSKgO5oi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟  بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/farahmand_alipour/5739" target="_blank">📅 19:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=YbiuJX-b8gEnXhcDnDoRaPNH4hA-GuSM8jReQ7UqeICj3Ecdr_BBVsndIe4ozS1ZPQlzPeFm5ytY8bbUXHJmmh5K3kJYWmQJOwsOFYqX9JJbLy29DvcQO8fWCcOwHNDlwISHjoAs2vGT_Nz8zcw80NqTzp8NmWt_h4uz1cirO07yphgl4bDnm9ihVz1m6VuGeDtnZKov08yhDM-KXghJDfNJhLvnu-9vHsiNZzSl7rfx26-teuIrlXvCQMHOnPe6DpO7bKaPQZ0y8sBPkEGUwHtt4yw24OxkPXO8hsVlKuZTMy4asPm2LJ3wDNo9vLKCKyj9ijkzP3TnixEvdZ8m1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e184bbb012.mp4?token=YbiuJX-b8gEnXhcDnDoRaPNH4hA-GuSM8jReQ7UqeICj3Ecdr_BBVsndIe4ozS1ZPQlzPeFm5ytY8bbUXHJmmh5K3kJYWmQJOwsOFYqX9JJbLy29DvcQO8fWCcOwHNDlwISHjoAs2vGT_Nz8zcw80NqTzp8NmWt_h4uz1cirO07yphgl4bDnm9ihVz1m6VuGeDtnZKov08yhDM-KXghJDfNJhLvnu-9vHsiNZzSl7rfx26-teuIrlXvCQMHOnPe6DpO7bKaPQZ0y8sBPkEGUwHtt4yw24OxkPXO8hsVlKuZTMy4asPm2LJ3wDNo9vLKCKyj9ijkzP3TnixEvdZ8m1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنان امام حسین رو چرا می‌برید بیمارستان؟
بگید خودش شفا بده!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5738" target="_blank">📅 19:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_uRqvDxUpAdx8CrYk2BkGioPw4kTBRdQTRG5wGlbALeloy-Qd6W9WtwRZfRMSvToTgMKNzuWjWttqbkpQ_tmDDdoELxKwA3ya3hyHmbyxDbHBRfW1dqT6hAnta6cLVteJR6mCzFlrou9cfSljFAMgb_Ku3ARLD-Xj8XJLeqyrOrTsZIDxOFDo1ywDuKMGVR2viqUxUcUHSBMrywrFPlVpz7JxDn4RodJqRuqJlfH6Co6Z47HsAgEJQQsfx0ZRAb92DFPMHi7ZxNWHp_LwyNmcRkMDU2HfzWt70itrEGgBWhyhw2ZPJCZl9iF-7kPpFvvr6AZjbQPch7NwRyAbMmOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9HmJNawAtIP22aDjgsWmZoN8sVXumGbjhtQeIBeoWLjldeYePZ7eEY7_ytEBUFXcrY8GPLACqTFfBQfV5Beg6X-5v0sJAdeGg9C5SQChADadTMOyaQJoMZ3IQIq4VQZ7gzdVYrDoSnoU2JvAwOMEzFUcUpsWoxj6Ieow1FO9Z7yillH6D3pdWs_Tn64NYRPqBg97jTH1EtwfHRDj6furQ_iqbmOSzeMtDkRZumE7_kCQQtsX4dwAqOtSy05bbXeNyGzF0Kgw0lqtEgQ8HU33s73i2kxKXuHWjmFOYpvkb1grPz1fJvJVKNmpHW_TbTFCEgAcPIM9MmOTmFID3R-lg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lArHJjocBoH19U8kypmcdQ94XRdH7ya_r5LrTlXkZNDv41eF1ysIKYTPLmCBaw0sK9znWki6PLQO4KVQoGNyMeEmsLJftiuwyebZZDwEmMRO6NqGbZBcR9iKVA0HFfms0_3kjLuN_hnpT-yOoN3IMHfQv32q7HAL2bZcZAEH5bXHXu9AvJOGle65BfP3SE9J1DiIrBLOVR26xYqKoQZki256QHxi4Up3srZR7uB7NZ7wezDbQI6Tj1NrTBm2w_APj3CMu02mCWKfn8mwFraFDJxkm_5XyjfhA3jCyrUP-eyVT2cD1udzRqTN_fGfdYJGjOQTNM59v4ZXnttUihCYMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر علوم جمهوری اسلامی  در ترکیه،
خامنه‌ای را از اولاد حسین عنوان کرد.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5734" target="_blank">📅 22:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4svX629Txxdfyko4PLgnOFEwhzbNs4pwNPR4n_wCHcLZJ3Ll_bod6j2ugc90kksQB4gW2WLa70_P8h68g-1l7MCJkNvLbTSkf-B_OqQDlg681zJMFkuqolXqtyNA7crUsieXMYF2hcZvuLISNIcEJxtjINOxhoXrcx0L880eaE7Mdl5c6vKAGQQx0HT_kIGSFnyh429q-t4L8FW5f5ZWXBTJ5P0WgCZKVwCsERKYzMA0fLvXPf8S93Qx8bs3QcC6HzUnDLMUkg2meG91n5DEAbiHfczWFrcXiBWeR1YT3Lu4SDcBF81s0APAKiyooB71NfGlT2MPUJWgbrXGKPGdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسرائیل به یک خودرو در نبطیه در جنوب لبنان حمله کرد و در نتیجه ۳ تن کشته شدند. مشخص نیست سرنشینان خودرو چه افرادی بودند.
صبح امروز هم در جنوب لبنان یک سرباز اسرائیلی در جریان حملات
حزب الله کشته شد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5733" target="_blank">📅 18:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NRz0cLCmpaOXPizNWIW19NIYcNrlQ044evPSNN5to2HbBust7Yg_Ss1mCrFkx2CJmi1vb-4XKE-pOY9OU2ffClTtOI1c7QtOy2XcLnPN_cGDhn4f85DeQpg5kegEb9pfr-eu0r-qe9ReCW6-HHxTPcvhYDPDRNbyXu3JQ-vw_EPlw4EJo6DmFdccvgtSLaMoTOdKnl4BCeoV-5me7sb7gy6v1dIGZsvCll_zalYPAQC1Bf9Diu9CjDpaOluZf8BAeosjzDwg-DH3nCVXRs6IijfPyYlPfKMvzBn0D_ZIHijaj9_LvbS69ghP62cYSHCeC9eLXWpn12iP8i3AJoVe7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صد رحمت به اهل کوفه!
لااقل به دینارهای طلا فروختند!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/5732" target="_blank">📅 15:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ksP52h-PwWwa-EEAX5Nn9GL_C_hpbd4N5FWdCGiu-Y1sj5IUpoLaNMD3LRpjIKN8gUraB-3C-lR6JvAOT7wzL6fRC-S94Ymp1mE8v3wjTko76jC3sOc5Aa768tKcOfBBPByxElHdZ2M5etKB0mYEx1W8ONufjCPdXC-ye-3BgpPwspZVSecRV0yO4vcvJb_Gi2Hgf0Tjs6Cd35FOTQvWPE-2Z0GWjxfPjwj-ZLo4ojtY720Ie5AguyPRjxNqGHQ7Hm9LK6YwXlu51qh4qpTnPSEnRcKH2yLh0Y28lqb-f2oIv3A7fige9rjjD-ajlfXuefCdY3MMb4kfzNiUKW_ntA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6715f87786.mp4?token=ksP52h-PwWwa-EEAX5Nn9GL_C_hpbd4N5FWdCGiu-Y1sj5IUpoLaNMD3LRpjIKN8gUraB-3C-lR6JvAOT7wzL6fRC-S94Ymp1mE8v3wjTko76jC3sOc5Aa768tKcOfBBPByxElHdZ2M5etKB0mYEx1W8ONufjCPdXC-ye-3BgpPwspZVSecRV0yO4vcvJb_Gi2Hgf0Tjs6Cd35FOTQvWPE-2Z0GWjxfPjwj-ZLo4ojtY720Ie5AguyPRjxNqGHQ7Hm9LK6YwXlu51qh4qpTnPSEnRcKH2yLh0Y28lqb-f2oIv3A7fige9rjjD-ajlfXuefCdY3MMb4kfzNiUKW_ntA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی ارسالی به ایران اینترنشنال نشان می‌دهد که صبح چهارم تیرماه در همایونشهر اصفهان پرچمی با نام‌ها و چهره‌های جاویدنامان انقلاب ملی ایرانیان برافراشته شد. بر اساس روایت رسیده، این اقدام «بدون ترس و با قدرت» در جریان مراسم مذهبی «عاشورا» انجام گرفت.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5731" target="_blank">📅 15:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=vijX1eoEm2Zin2tdkOxiJPD2eJZetwqYjg8ySIYHyoFw053MQdfcq5VnSVCJHm0E5hgVkRJQgav19kacsmMvyHgcEgWI-Zw-bvqXh6AafChp-zBKxAVd4gBwZ0rD3hEGIRWI-CADfYV8TT04bNMANrCzth1hz7b5jLv3jUI-KvTUhRTeyIvN6cnJKmNzqNFs3xl0lF0q4bs_jJuArlMAK1vIQtOsx-XrV2MJO9ahBlUBK6twwIm9XFvyKGC2olP_1ISjf894OZvzaQDi-PPbHx27AyfZCI42AHR2tw6w8Ci7CgwYw7BmBGiD2SCwY-tmv26sGEwqStmwoHaLCwGm5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afaf9624af.mp4?token=vijX1eoEm2Zin2tdkOxiJPD2eJZetwqYjg8ySIYHyoFw053MQdfcq5VnSVCJHm0E5hgVkRJQgav19kacsmMvyHgcEgWI-Zw-bvqXh6AafChp-zBKxAVd4gBwZ0rD3hEGIRWI-CADfYV8TT04bNMANrCzth1hz7b5jLv3jUI-KvTUhRTeyIvN6cnJKmNzqNFs3xl0lF0q4bs_jJuArlMAK1vIQtOsx-XrV2MJO9ahBlUBK6twwIm9XFvyKGC2olP_1ISjf894OZvzaQDi-PPbHx27AyfZCI42AHR2tw6w8Ci7CgwYw7BmBGiD2SCwY-tmv26sGEwqStmwoHaLCwGm5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گوشه‌ای از جنایت‌های دیماه جمهوری اسلامی</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5730" target="_blank">📅 12:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینفلونسرهای عقب‌‌افتاده‌شون‌ میگردن توی دنیا تا سطل آشغال کشورهای دیگه رو نشون بدن  و بگن ببینید اینجا هم آشغال وجود داره! پس اگه کشور ما رو کلا آشغال گرفته و به زباله‌‌ دانی تبدیل شده، عالیه! عادیه! معمولیه!   مثل همین حمید معصومی نژاد  که دیروز براش نوشتم،…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5729" target="_blank">📅 12:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uy3bbt7jGt6Qz5pZ8nVQfyA9w-5zGarM8_mpCDbN6ATXaKm1Q4Tl1kaQ7XrUxy72xY4_bCzyyVo-M1wxJfIpA5WzloFzOYHyPOOq81wYAe5_BaUsNunuzQCl-QSIlEAcIbjtnMV9Q91sqys6fyhw9i551qpYIV_6flTNSsFDVdMvaLNmmLj3Kap6eCCjDWfXUOABzB94Q8nUh6YY0UA9PN6NXDT7vNyt5CFJ_cqedK-KtHpJGwocPPApp8wBNCLrOVipsXDO939NNooHdJItvFDKxp8p0k7P8lNtM1JS6TVOe9EE1gdUKNs82-LLTj6igTmRrbNPZtXQ4Lmr6SOmCw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM738NvBoXJ-CmyxOP86yE2R6IaToshoFXZetrLlJl1tweyK0w55gUv0nQ3gxgQberkCKsNun_dIFZjO68HBsGfZCPqo1-z34xIOSEuDjVGoGP9ylW1QEJald7C7gWw3VR6VZNrdHi8pSXP373oLYRA5CPDu2IUKh--JVc38eMpVPVTN_62C6fIicAfabD1PZmOIzLhvE3Oes3M5j_9Dhf86nPGw0W0yNuTOtfUmNzwj2XoYG4fhsfi27jByfKh65Igiea0sqoHEAcc0XKYFTWplBUChX84a2msa-fi67dvHGhppGxPgyAIBRczrqcfJ80_1zAKTMb4G_HvNS3wbxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده گروه هکری «حنظله» که در جنگ ۴۰ روزه کشته شد، ولی خبرش الان منتشر شده.</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/5726" target="_blank">📅 09:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=KVkbIljGbPot5wCu8AgMs8AQpIb8h-qKaTNli84JLmTmFcg__j_4lE0Bc_dM2FbRO7zY3EH8UN5f9oy62kLPDxSrv4MpeyGGzKpss-erinXjIaE-jLzyPNgp2P9DHEu6CarG145O4noeEtQrV4MVpQzlahQ9y2xRdmpGIJXNGq3RZmwATdBCRahG0YOYg311ClGs_b9KWTMbEteTwQ2JGbyjFwOPG-7dq9HDvGQl5SUWpTuR_lni67_ZcR490bVmwZRlUktSPQhWZ-C5PhQpjvPoAtVG_SyukSWZwOKRagULYBbZtDKP0-WfiVvTWImb8zvzSFWNc6zVSeRio1E-Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c17f6d3c.mp4?token=KVkbIljGbPot5wCu8AgMs8AQpIb8h-qKaTNli84JLmTmFcg__j_4lE0Bc_dM2FbRO7zY3EH8UN5f9oy62kLPDxSrv4MpeyGGzKpss-erinXjIaE-jLzyPNgp2P9DHEu6CarG145O4noeEtQrV4MVpQzlahQ9y2xRdmpGIJXNGq3RZmwATdBCRahG0YOYg311ClGs_b9KWTMbEteTwQ2JGbyjFwOPG-7dq9HDvGQl5SUWpTuR_lni67_ZcR490bVmwZRlUktSPQhWZ-C5PhQpjvPoAtVG_SyukSWZwOKRagULYBbZtDKP0-WfiVvTWImb8zvzSFWNc6zVSeRio1E-Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/171eba79df.mp4?token=GlBqw1tECda09wSnVmnJ0uL9IQRfMsvoHoVJjVRp8wULfFsGVswcJZVZbIX3htUZngJ8tvy_qHROrSurI1KeEHfi9xaCkCIPbWPGS19jjaoEkr-vlj63PzlUS50qKvb3FlnXsNCUq4WW-yLT_fjRRTyDQQebBhv7sXaJuFb7VgjcpvL4FZYVLEiPLrii7DiR55Ue4N3jMkwOCakn4rQMf7wGM_Z89mKqq_RLmRZYvBBBGQPogBgW9Gw8Tzyoh26QaH7iMxdNBcLiCLYyJuvuWsGlzTr9ZsWUF4Ax_zr1gqriPt5xhzumQNDvGsE_yQbhoTFeB5sub9K3waecF-1Q-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171eba79df.mp4?token=GlBqw1tECda09wSnVmnJ0uL9IQRfMsvoHoVJjVRp8wULfFsGVswcJZVZbIX3htUZngJ8tvy_qHROrSurI1KeEHfi9xaCkCIPbWPGS19jjaoEkr-vlj63PzlUS50qKvb3FlnXsNCUq4WW-yLT_fjRRTyDQQebBhv7sXaJuFb7VgjcpvL4FZYVLEiPLrii7DiR55Ue4N3jMkwOCakn4rQMf7wGM_Z89mKqq_RLmRZYvBBBGQPogBgW9Gw8Tzyoh26QaH7iMxdNBcLiCLYyJuvuWsGlzTr9ZsWUF4Ax_zr1gqriPt5xhzumQNDvGsE_yQbhoTFeB5sub9K3waecF-1Q-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قمه زنی گروه بزرگی از شیعیان در کربلا</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5723" target="_blank">📅 21:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5721">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZlOVGSZqlkFwVHToumAgubNy_gtlRsvzTj2IGR93g3TLIlH_5U1L22NV-KImPanU0XyE6-QkTaFg8kAdC8IAc2-rLPnLxWzKyfHJ2PVd6ALMaHR9BsfK6Eq3AnVFybZC8pcYCYrzNXmQehpGX7Q8as3OcYRtURzFYDLh56C-TqWyyFakFPj0WdPigdhruLo9CEkSt2vyt0u6Feg_dzVYNaMu1iW44wvB6OXMitoU8zLsbHE-znjxkvyP947h5d_aVmBDhqp2n9heposz2bVrwLmqSbklqlGSbWLzeN-P01rMetCZhcJj3lnSvdrVxnB-C4_wjEe1E2zkHzB3_NmotQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DBG8JutYHKoE6WJ65_5vNe4IIaI8SmfsJLuOze021kQCBvaolGGJjKahcdcsOybdX4M2IK2d7PveKLW9BPNI6o3SevJRWk_PDVbkiZXNzjPS_lPxYPZ_a86UY_W5sbVILziyjF1T91NBJEQZWWNqtBG4G5d_B9M9_yKcrdS-TGAPDyFSJBAh-BsZVLxABDx9cjZzxjy-YfqfKTqDleGHpP1mRUeLgbfBJ-T1QF-7sv2l6BLq7yepvatSsx5PwMeqotrDIXuHRkcPAy4IUtSTryrxi0K5d8qKr9zFSQtRudv8DcXnfYMp_jLpDPM7eJTWPLcm68TWkHQh5dn2-VDL_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U5hHv954a9ZDqENEMqG15_ELNKeNhS3ZMosh-UcXH8-RUVJppd-un5fEqLnxL6xKLtUIDf1u7s6evNhHN1X9St76RKsv5MDWmCOXup3yOaiCMxuQFe0z1NI33RG0blKAdgYUKhHoIne-o9Wgjluftb6UsxtkR0hhQdwNP7HXZD5yg8evBfGc7ItZbDR9w1x0m9mO3g69rEC9tpldfBAvUjc-5yjCGcVJ6oPzh1-lF61kFzesRQuqH62uZxIQJifXatCDtvDakyfCJx-vw4nHXWRz0voVyeoyWGECTt_AoIyJSV_6tWp7r2nhChQRIkghWIBQKSSgEt7y6a0E3vOxxA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5718" target="_blank">📅 23:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5717">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/975d16374b.mp4?token=PoxNQR2G0XjLvIv2CfH2ZU6MxNOBW-dQ-1UeFXbcdLRcVtj5lWD7Wcm2X6y8hxT9GP9hHXCH6rxjpIEaUeezv6VKpdnDNOnH-7lGI4pIkVUFNZofyb_ftXYJlyAN8EcCPcwFYfBcxw0lH699B0jdpOtOnEf7mYnPB43HAa7Jn4HXsGECZdo20QlaQCwQiHJODIjFoH7NEsZXHGzt1LWMzL4RKyUMZuoBrs8aQkrmT9Jxg9hZCHT_wz1ccgQFBzvgPGZ8DbFKlNcP-TAfBscNzi1569c6zjYeKU9Pjci9HD-A2XewfIrPzGvSn5pG0er-nvlRmvCnrl4vqcYrrVVNhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/975d16374b.mp4?token=PoxNQR2G0XjLvIv2CfH2ZU6MxNOBW-dQ-1UeFXbcdLRcVtj5lWD7Wcm2X6y8hxT9GP9hHXCH6rxjpIEaUeezv6VKpdnDNOnH-7lGI4pIkVUFNZofyb_ftXYJlyAN8EcCPcwFYfBcxw0lH699B0jdpOtOnEf7mYnPB43HAa7Jn4HXsGECZdo20QlaQCwQiHJODIjFoH7NEsZXHGzt1LWMzL4RKyUMZuoBrs8aQkrmT9Jxg9hZCHT_wz1ccgQFBzvgPGZ8DbFKlNcP-TAfBscNzi1569c6zjYeKU9Pjci9HD-A2XewfIrPzGvSn5pG0er-nvlRmvCnrl4vqcYrrVVNhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سیرک‌های جمهوری اسلامی</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/5717" target="_blank">📅 23:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5716">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6d-xrlDsyLgDtx2vbIBTymlegpmwqWAmvdoIKaVbSCDGn9eCf7Yeornxj_WFl3eDzd0gt581v2Re8OfgPbxlhBVxnHFfKoDDOlLWaWSF26QOMOI8fTwQIE2CgZ89Z-GLHrUxsfqpBaLbyiRze7cmH8NAbsZQzYketLRxw9dRfHpKd0ptnP6MxFre2q3NQK9RGYtnKVXArHYqsSvi0KJ2lyPynYiQKKcwb-1Ir2YxU38ij_4ahVAn_GXdhxxZnj4nbJLy9npVq4teRQkuFQVHfGJ-WCAm0tTrZaPuS-9Jt2fp7NKwqZ63x5Jx9NcHuAmW1G_GzZqs0UbAxiLge2_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
شهباز شریف نخست‌وزیر پاکستان:
‏«مذاکرات شامل برنامه موشکی ایران نیز هست و آمریکا و جمهوری اسلامی ظرف ۶۰ روز آینده درباره برنامه موشک بالستیک و موضوع هسته‌ای گفتگو خواهند کرد»</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/5716" target="_blank">📅 19:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5715">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1iZ6yDMhNHzQbLIyfnmj8-5-Q1_V6qGN1XDCdHTMMzfV8nM4i4lmQr-ekcqR2-OmoyjSw8omwI-mV-3VG4PrRVsPULEiv9FGHh93NCLC6QdDvlgPk8jLBr_zmt8FP0dDMMO_M5YkuOBPIB7ygYqo9fHH1J6cMmh2dl1ZfNSommvRijIutFehBBRYEZ2xRBEz3HjSmtpBiEuIrqVUEEBI_6g42kHeUABKvwJ_Qf8F7oLEdrc98AdInHtfErPaFwUo4gpq-_yxsQNXx3BjeMPcRl893a5E1M8Uc7MbpnAknnsZp4Z1WcZ4_EOvUuqbcUPMuXVSMyKXrzrkUcJkTu5aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/5715" target="_blank">📅 16:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5714">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">فکر کن رهبرت رو بدی و سویا و ذرت بگیری.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/5714" target="_blank">📅 15:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5713">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AU5ARtK-i5iGg21eqALdGA0QG1RlrloBBRu3jX9GFco0qL03g72R3-eNO6pSUNMmzm-_GJMsHdtMc0NbsLXubS41T9DdlEUt6ZwXwqZNLm_q8U9EnGholtWz9zD4dQeQie_KVE5W68JHQFpxPcB3a6O59nClkA-I7tH97ILi6H2tzethmwJ9mY99eIvFAI7kvP3b_WheN4lnxu7KqbkkbhD2YzMauIU45X2-cwL3s4ke2w2jIt0F8YzrcqG9JthDZZNgdWVjRac0sgP8vvUDNTARUvPS_05mhfTnZcryMqI0O8aAVfAZDolVh9CQ0csCH8VAJqh_OUpGWlKY93FMHA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxwHVgwV1KhwGL6sPGyU2y3HWYmABIGq-pgklTCrVpzh15ZW_5GAnd_oEP74OToGQG240-VtzLh03PWXFiMwv1HqHu5Bt4XmpioGSrJXJ0dZQeaxCU095X5DLKuX0SC08kye6YtD0Mv8fyiTGyplOdQ7bZzarMpBUXHkFSKa772miqJwmkhOtUaj7iDOy-XmWWNct8cQgzssGQAw0idXsD69rWOpeFA6gzNll0s1J9cas6BMSJbTdz799YlVnJ4De-vp6T-R1YaRZ8McVZc1xEEG6mBa9akUGeWajpJCkCfCMqiSPMRFujC7NpVVZ4Ka8zbx5ITNU-OAUkyqstCuZw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=eHbLqJjdsmFBR13RKU6YIN6J76tzGMNSIKq-duseKvQiL6vVwkmskQSZFl6hQ7oLJ5z_u3TVOmIKkC1ugiEN1JSdo4SLr82j2Mhzjgf2IP0TBWz3sL6JWHbKyx78LYaRACJxAVO4_RvSL3mUVIy7QbeiFyBPyB0Xoywr16x_a6lifvMa4228f77ma2StDdFjpL-DgNP_50FR4aOFzENc_pgyjMuKR-77zpdiLcVR0ltS-FqWaJwiSaK8x8OHJCfjuAVYIC4sjfjYw-0EVhvDP8jmIvqPgwATGPzqdIRLNv5HwCxClyKXO_zUbvO_O1ewk5oGBBvsp2YkyXCFKyJwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c4fa249d98.mp4?token=eHbLqJjdsmFBR13RKU6YIN6J76tzGMNSIKq-duseKvQiL6vVwkmskQSZFl6hQ7oLJ5z_u3TVOmIKkC1ugiEN1JSdo4SLr82j2Mhzjgf2IP0TBWz3sL6JWHbKyx78LYaRACJxAVO4_RvSL3mUVIy7QbeiFyBPyB0Xoywr16x_a6lifvMa4228f77ma2StDdFjpL-DgNP_50FR4aOFzENc_pgyjMuKR-77zpdiLcVR0ltS-FqWaJwiSaK8x8OHJCfjuAVYIC4sjfjYw-0EVhvDP8jmIvqPgwATGPzqdIRLNv5HwCxClyKXO_zUbvO_O1ewk5oGBBvsp2YkyXCFKyJwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار  شبکه «الجزیره» ، احمد ویشا
که دو روز پیش توسط  اسرائیل کشته شد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/5710" target="_blank">📅 12:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5709">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y7r5QmTbLkYl4FUo0PgD6_yYBY4kbH7AI1Sc9lg567CXUVHg8iG2xt82zwXWRkwsytkMmFVG96sRZlNJnj7JFoGv1HdvwIS5pJ4ANefGBkUJw3W1Ft-neBZzVn_pF0ZtzBBpovx9M8JAoTBZj0FiLdt6-gSru4hynGXx_Gm5m6DE59uWURHYB7WXQM9_sP1q5vBI_e6byPLFKEpBhDzCYs28h7ky1J8_hI3pCl0vB_hZ4LmOUk2YxmJzITWmZzI4CUma0C6kFnhtCPz9upghl3jGxmkN6HtzZ7bQA0gOLkrZ3Rcy13d9tMWY_gb0R1Pea7iQRKrK7zfbFw4O_iPnzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هم‌دیر نشده.
«شیخ نعیم قاسم» می‌تونه از اندوه پیجر‌ها و کشته شدن نصرالله و کشته شدن خامنه‌ای و کشته شدن ۴ هزار لبنانی در جریان خون‌خواهی خامنه‌ای، برای همه یک جا از غصه و اندوه بمیره!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5709" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5708">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rtlnVW2fW6FTFUDGbfnapp1E9GmcOqSJ67Mr50CNH70ixSp13aE_i6KoiElxC1LbzBwx8jeXrIWMpmDSoYosD5PbFIDd-QVsFuSLTEC8qtv4gR3lRwG172tQ1zLqdsZYhYBzagoRjdsXPPIp5nFPs0Ybr_3euIwfr_P_SbDwOnowi4yVwsrRYBDJR5bgPG_IZGUA26rCIM7Hr8OVGvyRooLJpG7alGYnog_w67dFHc_G5khQqtxztpzwxdh0Xh1FEQb0kdhuT4PoBUNYF3xOtXcKjYVDN10H77jU4PyI_VeZvJmf0CId2mnZ45IDtZZ0qMUS_Ioya9_FuVyZCvi9dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکر میکنید شیعیان افراطی فرقه جمهوری اسلامی  فقط با سنی‌ها دشمنی دارند؟  با یهودیان؟ با مسیحیان؟  حتی با شیعیان مذهبی که از فرقه خودشون نیستن هم مشکل دارند! تحملشون نمیکنن.  توی کربلا و نجف وقتی اونها رو می‌بینن دست به انواع کارها میزنن، تا براشون ایجاد مزاحمت…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5708" target="_blank">📅 11:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5706">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWtAaUGRqRYB4YODPHoG8QAu6w_owQE7y9FjKLGqRq9iHrtak4eVlCqO3803G0AIszrEq2sIYEwUfGEcx7GKn77Hzra30o0qJ5H81nZgplMGBBfxMHwYZG3SWxxBLB8cPQ1QLk347X9CqfT2oWgsu1TCL8NsMNSeNnoQled3tnidkkwnRbUspNXYBg80srrPbKn9qBZEYQZIbfEsCn9sZoe8nHuZJg2x4GOORCRH-yKUgBiVGIA1EUlha1Ue7quzscwMTUrt811INqi2je2n1C3F2V82jowP_EFRDq5Ge0JVS-eC6xBTAPI-Ye5IYUu_tQWlg5mCQg67VlH9X9Apow.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=VIpVpIEeqgNdZlMQTKdFiCRYq2Ce4PSM9YE-mtzUDef4b4PK-s3BDuuekwi-NZLJpSm0T_XCXcNrCrwnpvil1N_iNSs_yWsP3IcWPz4i9U05jGBF5oks_6PU9tM1P9JaAH_lBfj0qi0Lxjv82xmie8e21MyNdWZSeri3LT1YRo2KSc-asgBvaEWlqSoAu77O5NE5zBjHgBjkebpKaBCcRYkAt_ruZIVAf_IYNkVoa3MAAAO_9bbNfUJR8eUlNhbzGDjegAk_TSjFtxUSGdWYkelh5LIqQykswmvmGZ36ehH3Nom5kQLsARjXsge5TyuGvKZEXM6hHTsb6gPoECpgkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c656e44d19.mp4?token=VIpVpIEeqgNdZlMQTKdFiCRYq2Ce4PSM9YE-mtzUDef4b4PK-s3BDuuekwi-NZLJpSm0T_XCXcNrCrwnpvil1N_iNSs_yWsP3IcWPz4i9U05jGBF5oks_6PU9tM1P9JaAH_lBfj0qi0Lxjv82xmie8e21MyNdWZSeri3LT1YRo2KSc-asgBvaEWlqSoAu77O5NE5zBjHgBjkebpKaBCcRYkAt_ruZIVAf_IYNkVoa3MAAAO_9bbNfUJR8eUlNhbzGDjegAk_TSjFtxUSGdWYkelh5LIqQykswmvmGZ36ehH3Nom5kQLsARjXsge5TyuGvKZEXM6hHTsb6gPoECpgkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه مفتی مفتی گشاد شد</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/5705" target="_blank">📅 10:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5704">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=gywzh9yXEoLvmFj0kJmF0_LqiNEPYTfOGeZDmsc-RE0Mpa9rBdgN0kTHZ8sfVCdFxjn267QZzCqTkv2X-xmIsQd8QvG_izYe1ikuV8AdgkBljEzz5sm8Jsj_vAndyfy20l9_wE2HXWASTh7vnDWDnZuq6Vq0KdNmdp3A5rovjZ58zQT4Ssy7AOGgGn5lgGGBFb2kPuD4-mwRieUtphKU1n-6AooSF0y0G7Ec3iaIv6DKD04_Jiaxne_WHP7URq2ScwpbaECV0LcnKo9FOJasImedy0ZlQKRC5pK57km0zj5JRKyPVBKQgq_SC5ZwlgkR3I6sjmDPIrJBpqYlW08C3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa6e1aeb6b.mp4?token=gywzh9yXEoLvmFj0kJmF0_LqiNEPYTfOGeZDmsc-RE0Mpa9rBdgN0kTHZ8sfVCdFxjn267QZzCqTkv2X-xmIsQd8QvG_izYe1ikuV8AdgkBljEzz5sm8Jsj_vAndyfy20l9_wE2HXWASTh7vnDWDnZuq6Vq0KdNmdp3A5rovjZ58zQT4Ssy7AOGgGn5lgGGBFb2kPuD4-mwRieUtphKU1n-6AooSF0y0G7Ec3iaIv6DKD04_Jiaxne_WHP7URq2ScwpbaECV0LcnKo9FOJasImedy0ZlQKRC5pK57km0zj5JRKyPVBKQgq_SC5ZwlgkR3I6sjmDPIrJBpqYlW08C3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامپ:
‏اگر ایران به توافق خود پایبند نباشد یا رفتار مناسبی نداشته باشد، من کاری را که لازم باشد انجام خواهم داد.</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5704" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=u-qxszMaLttswEVfVtB6uXgsUHmgmYOk0o90qC-yDSjl9hby6kwq_27D2YRDFrxoQeSWcap1zhLpU_mgZiC3g7eiKDBYEJuHvQGkXGb7bUd3BhSrerWQpbs_tVze-ZIV5qALsvDwI3Adctxw0Owkx84kD63-28yCjd1rigGqrYaOcrzaFLAr4F7p5Na49L7DaAs3oBT-ur2q12PSifMnIDKcw72ywTaufBwiDQXki0lAgacHn1gZVpxPIAM7IQ5bL57yqTOa29aeY2rB0AZRJSCVjHlGwSdpY2mB7yFoZC9UXMFImU3vhS2XylbiDaGiqiEWaw2fGJRH2IDJBTJF_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d53a76b465.mp4?token=u-qxszMaLttswEVfVtB6uXgsUHmgmYOk0o90qC-yDSjl9hby6kwq_27D2YRDFrxoQeSWcap1zhLpU_mgZiC3g7eiKDBYEJuHvQGkXGb7bUd3BhSrerWQpbs_tVze-ZIV5qALsvDwI3Adctxw0Owkx84kD63-28yCjd1rigGqrYaOcrzaFLAr4F7p5Na49L7DaAs3oBT-ur2q12PSifMnIDKcw72ywTaufBwiDQXki0lAgacHn1gZVpxPIAM7IQ5bL57yqTOa29aeY2rB0AZRJSCVjHlGwSdpY2mB7yFoZC9UXMFImU3vhS2XylbiDaGiqiEWaw2fGJRH2IDJBTJF_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1F8TczdoNt5f-CaXTekzgl-o8SzD0pr50uw2ARgr6Y4H7S1U8EPyzL0PZ3mB7zf2wS1CFoYM5s47hMPbGtPhptJ0lUvV01SqmAv61FMmAqewCeKKpLNZw0XehEqzloToILOKitfcMVumvVqnldAZzvUlH7ew00r5kB3s7qTEUqlaOk4P8AjIIzkVpbLR4omURHizJRB4fttjf28g_G_vDPCWy82PLldvT1MwlvnwSgwbK6x7DmH7Pms7Tac1XPvRxjX2E_8jY3aflzFSlFN_KjtI2Hn8rroh_uNuTcHNUFfDYhQjJqvUXHFwXoIQnofBGqEK6eM-w7ScdhoBKI_jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این درآمدها هیچ وقت برای مردم ایران نبوده
هر جا پولی رد بشه، خودشون اونجا
قرارگاهی زدن و پول رو میزنن به جیب خودشون.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/5700" target="_blank">📅 20:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5699">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0_46igjaoAmH_f1vRDEz5tSLAsNTYOjGCAagWfLY7TchCMOowHydlP8_6NYGB_7rAT3kps05uGjlnRcu6NPxr089J6fBEXvbb23_NU7-eAbcsrEOOqS-JvO4VEREJoX7U9Da6RYu-YAZsy1tYawLX_EnfobkanLdgbW2ioKQTD_7mL5Kt08yvnxzB2M1jYV5sSha7ZHkldBYMd_lHOdVPTNG5-zMFrXD_h-trZpnmhZdyrORNz9-_6zL64Tcuv8Nh4dzqh05QDa4S2qUQ7_aXQZZy-36xm0pq4ebYyQUvHYdIPUawXyTLWPGVK4mqnheXdRl7Sk-7SrycVwVeyJmA.jpg" alt="photo" loading="lazy"/></div>
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
