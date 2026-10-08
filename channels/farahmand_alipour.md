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
<img src="https://cdn4.telesco.pe/file/ZBKwSSKyFaDo5gZTGFIejcAyq4jjwfFXZfiCoq1rsSGeBNL093Ym7vKRxV8Rwi4GzvKN0CoMI4HC1aCWV25aqfgNVuwLtGx5QVnZS7usU2sM8zbMhN3FimQN3i_9_iOUWaBpS4ORuM4WNtwJMiX19ULc2yeEZMQUZ8oJh3Lz6pb_V62paqzWni1GFMnmMwGeMBnA12-FHChP2GHaau80xMpBo4-Gqs7qdf7Gh52BEbCqZgheL5DgmlIvbpeHeDC7dAGCjmGl00qIZGoWEoPuVRiG0PWU6K2R2y2HbyJ0dP-9PMLJ3CIh9uxsR1u3qUl4EnhO2JV2Ww_ibUyUUhdabQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.5K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 12:43:35</div>
<hr>

<div class="tg-post" id="msg-6803">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=gr4RQrVTUaT5QD3rE3L3qccM97CCfGfI955KRmGp8JrATQnLx3w9q7vzL1A2hBQVpHwLbLMyXsfdtzyO3OsH1rTMIcta9yqZJnNojRt4fI15ZArP_TIQjmN8MBY-s3MnC4MxoHWBOr1p8M5ZWNrHvSfIGWGiyNi3y0h9ubgPX7GFDGCQnp5c7yBqH7-eTd0jq4aY4Ci620vhOiSso38v8XhFoW4hJhYcFs3Yef32UgmuJoHb2GED861Ho9QIMZQEFQdwuGS1NwXmIaOdJ7loDOpjBKF0XWQUpt7rkHNIGLmHhBDPp09Su3ZhDhPZu0TKFksReZY58qoA2KpOjujIGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04f7f5c283.mp4?token=gr4RQrVTUaT5QD3rE3L3qccM97CCfGfI955KRmGp8JrATQnLx3w9q7vzL1A2hBQVpHwLbLMyXsfdtzyO3OsH1rTMIcta9yqZJnNojRt4fI15ZArP_TIQjmN8MBY-s3MnC4MxoHWBOr1p8M5ZWNrHvSfIGWGiyNi3y0h9ubgPX7GFDGCQnp5c7yBqH7-eTd0jq4aY4Ci620vhOiSso38v8XhFoW4hJhYcFs3Yef32UgmuJoHb2GED861Ho9QIMZQEFQdwuGS1NwXmIaOdJ7loDOpjBKF0XWQUpt7rkHNIGLmHhBDPp09Su3ZhDhPZu0TKFksReZY58qoA2KpOjujIGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/farahmand_alipour/6803" target="_blank">📅 11:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6802">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fkU7GP-7UdRPPrkQxpLzz2Ubr7NZLzhYLK5ylbjiGMH68dQssEh2c8-XBy9VO-OOiWIUOLdMrJxJk_MJWSGsNvdHgM1mmySixaOQGJoo_Ky_EPA8j4R-DrtTEljhYectwB-l_NsJkYdHZBJ--SXN-6EhO4hKyYAI6zvJckOK1jAC-Jum7LE6O_3rUug1ckOh5BLCGYjDLEfXrNvz38T_DsPsHt0C4lON6Puj6u88NBrh8jZyS1PdO5pZ5lWG6zXyVr5FdubYOlDEq7YlKt0KIsUlx11dxVDIWfcjJ37KqGyCYU2CjUeR1DxSPsXWq7dX69Pw81lCp9LZD-1r14kOdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن  که آخوندها دائم به نفع خودشون و شیعه و….. استفاده می‌کنن آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟  یعنی قرآن وسط تعریف یک داستانه، و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل  و فرعون صحبت میکنه و  اینکه خدا…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6802" target="_blank">📅 10:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6801">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz2_RKwSWjDv1K7AXcWKMF0Z4zMOk0YprDBQZ84zBENhdzrobykC9gIg_bEKMgSPtUkDpLBOnNDm2QDxcWxnhp7l2vA_7sQGHOjS8oLeE58JR2nay2I18RU6jB5na9Bu27gFXUD_-z-jLopbxc4OgVvA_-U2sZLMWRdupFjz57lwFm_2QPRW7fip60X9FFKdpAfyLu1gSisaVSZvcA3ys13QyRJI5UHjqap15Z5Wp-xIfMgEesP2xSd2I4E6wBNZNRvlyhV3TVQYM60VJn3vJe5L3yHZXl-8xu37fh6ke99OBU-qcpftvWZwPJJ3p0ONu4yki9d3-XuEfRfzlPLPVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌د‌ونستید یکی از معروفترین آیات قرآن
که آخوندها دائم به نفع خودشون و شیعه و…..
استفاده می‌کنن
آیه ای است که دقیقا و مستقیما در مورد یهودیانه؟
یعنی قرآن وسط تعریف یک داستانه،
و آیه  قبل و بعدش داره در خصوص جدال بنی‌اسرائیل
و فرعون صحبت میکنه و
اینکه خدا اراده کرد امت بنی‌اسرائیل
رو  پیشوا قرار بده و البته «وارث»!
این آیه مکی است و این نکته مهمیه!
چون آیات قرآن در مکه همه در مدح و ستایش یهودیان و مسیحیان بود، تا زمانی که اسلام در مدینه قدرتمند شد و شمشیر و سرباز هم به دست آورد!
اون موقع آیات متفاوتی نازل شد سراسر سرزنش یهودیان و مسیحیانی که مسلمون‌ها  رو تحویل نمی‌گرفتن!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/6801" target="_blank">📅 10:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6800">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">روز ۷ اکتبر ۲۰۲۳  وقتی به اسرائیل حمله کردن،  نوشتن که دنبال کنیز اسرائیلی هستن!  هر چقدر اونجا کنیز گرفتید اینجا از تنگه‌ پول در میارید!</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/farahmand_alipour/6800" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6799">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=mxgo_UurUnLh_ovBYkNn3e_ISd_qYUsoi1ppQab0c7DpTX1kTqrEOCu1IOZdz4hwv4-zIpim7Jcz4i_Nwy6MQ3r_J73yj6GRAoKZzGjM1QkcrndKrnTRgs2IHIS11FLBor7OIOwTORr0TZ1Rt7WJbnt_zNZhmd0uyCH62jr3JHepDxFEOq9_663fjtkeOUlFn7YPWiXqR0DCUh6SQHwqAo1LE-v4Vdqtkqrlbiw66SZDV1cRdfiCzUNhR_JQvK0c6i5v9JkZ4ZXsAVt_fd-r9pyECtLepOcXYkeSbb6E31pVxDPQtl_i_0_LhJDYwxbhZPOY6bJNgw5AkGUjA8Mzd4xsK0gxloix0fkloXxBu7vYcEawd94FOnAzXX-3XXVWkZKB46iwxRdrhJ6b7RwsxlCF3KBQSzIbNomH29F2Q3tx0_EsWXg1f-_W0YXeS-8k-Na-Y2VHVS60kHLwykbs80vLRZiLZkYdZRFwEkwNtGMk5rVKNmREsqN8laG0n0f90AxgCvH6SUMcllGLYk-0aH8LeHgU3tXU7bLe_BFuH3CMWUfzkEoW9o6ZfYJFzgMFL-DXoa9Vq-Bsz9ac6QyAAUCF2ngl6a2RemZqgp0CCGQJ6r7BYZPClcvkf_v2QHXYq6zJ95zWf6lnrW-CI9PrMOpvT7EbalYRw_6NUgYHpMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebe3608b04.mp4?token=mxgo_UurUnLh_ovBYkNn3e_ISd_qYUsoi1ppQab0c7DpTX1kTqrEOCu1IOZdz4hwv4-zIpim7Jcz4i_Nwy6MQ3r_J73yj6GRAoKZzGjM1QkcrndKrnTRgs2IHIS11FLBor7OIOwTORr0TZ1Rt7WJbnt_zNZhmd0uyCH62jr3JHepDxFEOq9_663fjtkeOUlFn7YPWiXqR0DCUh6SQHwqAo1LE-v4Vdqtkqrlbiw66SZDV1cRdfiCzUNhR_JQvK0c6i5v9JkZ4ZXsAVt_fd-r9pyECtLepOcXYkeSbb6E31pVxDPQtl_i_0_LhJDYwxbhZPOY6bJNgw5AkGUjA8Mzd4xsK0gxloix0fkloXxBu7vYcEawd94FOnAzXX-3XXVWkZKB46iwxRdrhJ6b7RwsxlCF3KBQSzIbNomH29F2Q3tx0_EsWXg1f-_W0YXeS-8k-Na-Y2VHVS60kHLwykbs80vLRZiLZkYdZRFwEkwNtGMk5rVKNmREsqN8laG0n0f90AxgCvH6SUMcllGLYk-0aH8LeHgU3tXU7bLe_BFuH3CMWUfzkEoW9o6ZfYJFzgMFL-DXoa9Vq-Bsz9ac6QyAAUCF2ngl6a2RemZqgp0CCGQJ6r7BYZPClcvkf_v2QHXYq6zJ95zWf6lnrW-CI9PrMOpvT7EbalYRw_6NUgYHpMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو روز پیش به فراخوان یک اینفلونسر مسلمان
و هجوم جوانان عمدتا مسلمان در شهر «وینچنزا» در شمال ایتالیا، شهر  به آشوب کشیده شد.
در این ویدئو یکی از دیگر از اینفلونسر‌های مسلمان رو به دوربین به صراحت میگه :« باید اصول کشور مبدا خودمون رو به اینجا بیاریم. باید به کشور مبدا خودمون احترام بگذاریم.
دیدید دیروز در فرانسه چه کار کردیم؟
همین کار رو در این «فاکینگ» کشور [ایتالیا] ، این کشور گوه، انجام میدیم! تغییرش میدیم ، مگه نه؟ تغییرش میدیم!»</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6799" target="_blank">📅 12:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6798">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvG_MmqYw18OWuvXMyX_-x2nIY5NjEMYWomy-V2iZcD82mDSzopcBzVAbgCELFy5ho3rYbP6wrPha-EASXRMA3i55snhpwTJ6Ym4xD3HkFTr7EcmnbB9uAnotYlPaqjaDI1Rulor5ZdVMZddbr-kPixR-5wFmoFgSsx59vCJMRTIPmRViqmUtNjEzz_hCGvjqRiScfNWQ7x6S_MhLaydzojTC48aDId7kXApdN7m8ME43Vgxdrb-q7ob4JD_PBVz0oeIIVqEofbvgh-Q3sCVM20IYxc2DlTf5slJljB9ZL-A_m_csuzTE3QSGBq7gXDQcP2qgVFY5PxTugyGAUJKMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»  در تخریب‌های اخیر خبر میده. دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.  در حالی که اعتراضات دانش‌آموزان…</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6798" target="_blank">📅 12:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6796">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YYJdRgFd8d3DmYRnLZS78hdAnxtdbKskJQ0n7MsffybgVJOVmZKcyfYaaIRddo7eG6VSE9fRdlhR27zzIuFRxHnmJlT7LJ7E6BI2rlJ5SGpRABaJc1dtlc97Lhd3XIyDhtqSEtjGE8rEALd6rJPj5of16cVYrr7NZ3HvVtozwJEYY5VUlQWojf-0HOpCMnap2Nzm_cX3u7PZs3Oeb6kLcSaLTx47MCPn5DPsMgFFhkl1LhEEcBWG2OmfaCIyvUZVLnQOeZOHNgnFD23dn_MC7DVuGB1YDKrmU1_kZy5Jnkyyxc-pRqifAfXAY0EJQs-4asNnFnoNtbv9L_wX7tWHYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpi8Ii19b2z4GHOqwMJNsowIBmCl88CLlO2yK9NhciP7xETvZHtiFrNjw6IuLRNT-85HCNtPsGSw3onGrECWmq8Hgv_qujAnaObhs5gleTrTWtKEiP5R9CVu0wy-2ft3P-zvUnd8Nt23OOUcfQ6kWbUT9UXjEjX3-I20rD_vy3iBAMw1-q4SwcYMFwrzEIW7DngLVDWCRmsV-PgWXAhlaMIsm9Q-qL2_7e0heF4T6qQ_MRQJ1cCziFfyY_JY98IOv4EQjXkBC0sLwIi--E69xu63XxhnxW1CyT4WzzkjVFfMqsTIgcZwWiiGuAwegNQQaA2fyYtmoA1shOVaGl-qmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">روزنامه فرانسوی لوپون از همکاری چپ افراطی فرانسه و «اخوان المسلمین»
در تخریب‌های اخیر خبر میده.
دولت فرانسه نیز دیروز بر اساس اطلاعات نهادهای امنیتی از حضور چپ افراطی در گسترش دادن اعتراضات و به آشوب کشیدن اعتراضات خبر داده بود.
در حالی که اعتراضات دانش‌آموزان فرانسوی
کاملا مشروعه و دولت بهشون مجوز میده،
عده زیادی با پرچم فلسطین، الجزایر و مراکش،
در تجمعات حضور دارند و دست به تخریب میزنند. دقیقا مثل هر بار که بازی فوتبال هست
و همین جماعت شهر رو به آشوب میکشن.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6796" target="_blank">📅 12:43 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6795">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">می‌د‌ونید چرا جریان چپ اینقدر خودش رو
هم داستان و همراستا با آخوندِ جنایتکار دیده؟ می‌دونید چرا اینقدر چپ از جامعه ایران
متنفر و خشمگینه؟
چون همه هویت و هستی اینها مبارزه با آمریکاست!
ایران اگه یک پایگاه ضد آمریکایی و یک کوبا
و یک ویتنام بشه براشون ارزش داره!
ج‌ا، چپ‌ها رو قت@ل عام هم کنه براشون مهم نیست!
چون هدف و نقطه مرکزی آمریکاست.
همه هستی‌شون در این تعریف شده که جایی آمریکا
حمله کنه و اینها سریعا بیان وسط میدون
و ضد آمریکا شعار بدن،
در قضیه ایران ناراحتن که چرا آمریکا حمله کرد
و اکثر مردم ضد آمریکا نشدن؟
البته به جز اقلیت مزدور اسلامگرا و اقلیت بی‌آبروی چپ که هر دو اساس انقلاب ۵۷ رو داشتند.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6795" target="_blank">📅 13:10 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6794">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">مثال دوم گنده‌گویی‌ها و شعارها که کار رو به جنگ کشوند و به شکست سنگین  هم ماجرای شاه اسماعیل صفویه شیعه افراطی بود که چند باری داستانش رو مرور کردیم که دائم نامه‌های فحاشی  برای خلیفه عثمانی می‌فرستاد،  یک لباس زنانه هم همراه با نامه می‌فرستاد،  پایان نامه…</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/6794" target="_blank">📅 14:41 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6793">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بالاخره امام علی در کوفه  تونست ۲ هزار نفر جمع کنه!  برای کمک به محمد بن‌ابی‌بکر!  در حالی که در خود مصر ۱۰ هزار نفر مصری جمع شده بودند علیه محمد بن‌ابی‌بکر و به لشکر ۶ هزار نفری عمر و عاص پیوسته بودند!  این ۲ هزار نفر از کوفه،  تا راه افتاد و …..  هنوز وسط…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6793" target="_blank">📅 13:02 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6792">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">امام علی هم که خلیفه بود و در کوفه بود، قبلا هم گفته بودم که کوفه (و بصره)  اساسا شهرهای پادگانی - نظامی بودند. احداث شده بودند برای حمله به شهرهای ایران و تصرف مناطق مرکزی ایران.  با این وجود به خاطر جنگ‌های پشت سر هم مثلا جنگ صفین که نزدیک دو سال طول کشید،…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6792" target="_blank">📅 12:57 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6791">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">کار به جایی رسید که جنگی بین  محمد بن‌ابی‌بکر و «عمر و عاص»  بر سر حکومت مصر شکل گرفت!  عمر و عاص، دفاع قبل توضیح داده بودم که اولین حاکم مصر بود!  و جایگاه محکمی هم در مصر داشت!  و مرور کردیم  که اوضاع مصر هم از زمان حکومت  محمد بن‌ابوبکر از لحاظ اقتصادی…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6791" target="_blank">📅 12:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6790">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">معاویه برای محمد بن‌ابو‌بکر  نوشت که تو که هر بار توی نامه‌‌ات علیه پدر من می‌نویسی، و یادآوری میکنی پدر من فلان بود و بهمان بود، پس من حقی ندارم و خلافت حق علی است،  پس چرا پدر خود تو (ابوبکر)  همراه با عمر در سقیفه بنی‌ساعده،  حق خلافت رو از علی گرفتند ؟؟…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6790" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6789">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">بعد از چندین نامه تند که معاویه نامه‌ها رو هم می‌فرستاد برای نخبگان و مردم مصر،  (البته محمد بن‌ابی‌بکر هم خوشحال میشد که نامه‌هاش خطاب به معاویه،  دوباره برمیگرده به مصر و‌ مردم مصر هم می‌بینن نامه‌ها رو!  اما قضاوت مردم به سود محمد بن‌ابی‌بکر نبود! نمی‌گفتن…</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/farahmand_alipour/6789" target="_blank">📅 12:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6788">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">محمد بن‌ابی‌بکر نامه می‌فرستاد بدون سلام!  همون اولش به مادر معاویه فحش میداد!  (این موضوع فحش دادن کلا در بین شیعه به شدت رایجه! حتی در متن سخنرانی‌های امام حسین در کربلا!  یکبار هم مستقیما معاویه برگشت به خود امام علی گفت تو با من مشکل داری با مادر من چی…</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6788" target="_blank">📅 12:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6787">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مصر، ثروتمندترين استان حكومت اسلامى بود،به خاطر جلگه رود نيل وكشاورزى پررونق و...! به خاطر اينكه در دوره حكومت امام على ساختارهاى اقتصادى رو عوض كردن وساختار جديدشون رو هم نتونستند به درستى پياده كنند، اين مصر بسيار ثروتمند فقير شد!! يعنى اوضاع اقتصادى داغون!…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6787" target="_blank">📅 12:22 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6786">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">این رو هم در نظر بگیرید که امروزه به خاطر حدود ۴۰۰ سال تبلیغات یکطرفه، اکثریت مردم ایران میگن حق با علی بود و معاویه در سمت اشتباه بود!  اما در اون سال‌های اولیه اسلام،  چنین شکاف و فاصله‌‌ای هنوز وجود نداشت!  بین نخبگان بود!  برای عموم مردم، جایگاه این افراد…</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/farahmand_alipour/6786" target="_blank">📅 12:16 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6784">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">محمد بن ابوبکر  یکی از نزدیکترین چهره‌ها به امام علی بود که حاکم مصر شد!  یک جوان تندخو! از این حزب‌الهی‌های افراطی و عرزشی‌های گنده‌گو!  نه سن کافی داشت! نه تجربه داشت!  اینو امام علی گذاشت حاکم مصر!  حکومت خودش که متزلزل بود!  چون وسط آشوب کشتن خلیفه سوم…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6784" target="_blank">📅 12:08 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6783">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پس تا اینجا همه می‌دونیم که  فقط شعار ندادند!!  همه ما این قوم رو می‌شناسیم و ۵۰ ساله که حیاتشون در تنش و بحرانه!  اما فرض بگیریم،  فقط شعار دادن و حرفهای تند زدن بود آیا در تاریخ داشتیم که حرفهای تند زدن باعث جنگ و ….. بشه؟   بله! و اتفاقا دو مثال روشن در…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6783" target="_blank">📅 11:52 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6782">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید که حامیان حکومت،  در دفاع از خودشون میگن :  بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل شعار میدیم، ولی کدوم کشور به خاطر  شعار دادن و پرچم آتش زدن و حرف،  حمله کرده به یک کشور دیگه؟   البته که همین جا هم صادق نیستند، …</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6782" target="_blank">📅 11:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6781">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">لابد در این ماه‌های اخیر زیاد دیدید
که حامیان حکومت،
در دفاع از خودشون میگن :
بله درسته، ما نیم قرنه علیه آمریکا و اسرائیل
شعار میدیم، ولی کدوم کشور به خاطر
شعار دادن و پرچم آتش زدن و حرف،
حمله کرده به یک کشور دیگه؟
البته که همین جا هم صادق نیستند،
چون اونها فقط شعار ندادند!
خامنه‌ای رسما در برنامه «گام دوم»
که سیاست‌ها و اولویت‌های جمهوری اسلامی
رو برای ۴۰ سال بعدی تعیین می‌کرد،
اخراج آمریکا از منطقه خاورمیانه
و مبارزه با اسرائیل رو رسما جزو برنامه‌های نظام قرار داد، بگذریم به اینکه در عمل و با افتخار و صدای بلند می‌گفتند ما به گروه‌های تروریستی حزب‌الله لبنان، حماس، جهاد اسلامی و….. موشک، سلاح و پول میدیم برای مبارزه با اسراییل و….!
هر گروه دیگه هم بخواد مبارزه کنه،
بهش پول و سلاح میدیم! اینو خامنه‌ای هم علنا گفت.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6781" target="_blank">📅 11:37 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6780">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aw78psjhXu8_b4KGSQR8l-unPAx75CUeu2Eauo4KPMa9lSYXqRgPVVDUS8JLuKK-weKgzizhB1m40Tf8SGU5Dzh83GmeroQRK-o7i8Q9Rt9p4yDrFL_pbGlLgA8ziuUV5otsxmTBufFYCjlexQTgQPNkVBwqkqC7LqK4XltTkWzH_-dLAxt0qh7H6VqudYDmB5CwObYNMGJwFLiPiCc-LTA0-N7WFd0pFstqe_Tap9sBhjU38kK8Gf6tyS5hzI-1RlOQkhEEwCfrGs75UE8T9BtuN9tUF1E4iURKUAFVeY9uxFfPwD_J-EgayJFXqPLeIHevI7YpniGJJUqn3BevOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یورو شده ۳۰۰ هزار تومن!
و دلار تقریبا به ۲۷۰ هزار تومن رسیده.
ولی یادمون باشه که بزرگ‌ترین
فروشنده و عرضه کننده ارز در بازارهای ایران
خود حکومت و عوامل حکومت هستند!
ارز دست اونهاست!
صادرات دست اونهاست!
حکومت و عواملش خودشون دارند قیمت رو بالا
می‌برن، تا ارزهاشون رو به قیمتی بالاتر بفروشند
و سود بیشتری به جیب بزنند!
اساسا برخی از دامن زدن به جو جنگ و التهاب،
کار خود حکومته و مافیای حکومتیه، برای افزایش
قیمت‌ها و افزایش قیمت ارز
و افزایش درآمدهای خودش!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6780" target="_blank">📅 14:21 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6779">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بلومبرگ به نقل از منابع آگاه:
جمهوری اسلامی  پیشنهاد داده در ازای لغو تحریم‌ها، اجازه دسترسی بازرسان هسته‌ای به تأسیسات بمباران شده خود را بدهد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6779" target="_blank">📅 22:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6778">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rxMb__GltLHpicME5i2YNUGYtHxEiMVtpcS1NhFxtKav9bALJFRtSj1AmGaZFj82NY4JRhsQXbivUC2-Q2nBOuCMiGSgkRcq4uSnfV-GF0czpJb67eLjlBg1mr0gDY-UocOj3gJXzfHTQYeAxOyiby-TRL0fQxmbEVyDp0sLc0IoA3f0wO9_hANieJBqzsoK9khxMSAJ9QcO5lKHNt4f-38_nBYb6Ns1J7Kgo4rGanq3bSEFfLm21FtRtDszfv-IdjQzbAfkdXoBvcENYDHby2-X162UtlneGXW63NhaH7M6cLD_XfaGiJ4wIOh8luCaI6JRWKEcUYaQPpJc0AXkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمهوری اسلامی این ۷ شرط رو داده
به آمریکا که در قبالش  ج‌ا تنگه هرمز
رو «باز کنه»! آمریکا گفته تنگه هرمز برای شما بسته است!
برای ما که بازه! نفت که داره عبور میکنه!
و اصلا درباره تنگه هرمز مذاکره نمی‌کنیم!
اینها مثلا زرنگی کرده بودن بریم تنگه رو ببندیم در آستانه انتخابات قیمت نفت بره بالا،
آمریکا بیاد گریه و التماس کنه!
برای «زمستان سخت اروپا» هم منتظر بودن روسای جمهور اروپا برن بیت رهبری گریه کنه، لکن هیچ کس بهشون محل نگذاشت و خودشون دچار مشکل کبود گاز و برق شدن!</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/farahmand_alipour/6778" target="_blank">📅 09:57 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6777">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FNmApfalNVT16nxO1EB4zc91w9joz3reEFpOs9GyIzcRsGGE6qOrQGGlpjILj-SNdqQr34hi4IeaIkEM76ASdEVHFdXfraPWKu4OLEHc6XMpUX42Vl9JvWYBhlLtGHdlQe7ZiqVePO1nwFouiMZCXe86L3UKPXGc4ZlWa3aOxbGaj66lc5GoJhMH0fTFgnscrJr3hnTr3Bg6QjxYFPz3iheoOs1HsW7cF2FC9aHwv0cPH56IoxNlyrjI8Sy_Wn_QUCnQ7CcIhvC5ctNJ73ED7S-tyr5r9Rkqi7OIhqg5qWIhcS0FrnRRNr-jA8lLdfCs3I9e0I01S-L5t5gmpDcXEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزش واحد پول ایران، «ریال»، قدرتمندترین کشور جهان در محاسبات الهی، در برابر «دلار آمریکا» رسما «صفر» شده!
در زمان حکومت صفویه،
و بر اثر سیاست‌های شدید مذهبی شیعه‌گرایانه شاه سلطان حسین (مردم بهش میگفتن ملا/ آخوند حسین)  مردم اصفهان از زور گرسنگی به مرده‌خواری افتادن،
علمای شیعه از همین هم یک پیروزی
ساختند و گفتند همین خودش نشون میده که دیگه وقت ظهوره و امام زمان داره میاد و ما بر جهان مسلط میشیم و….
چند روز بعدش شاه سلطان حسین
تاج شاهی‌‌اش رو با دست خودش گذاشت روی سر یک شورشی سنی مذهب افغان و خواهرش رو هم به همسری بهش داد و امام زمان هم نیومد!</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/farahmand_alipour/6777" target="_blank">📅 08:07 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6776">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=T0vgVEyopMWxfGoMqi70yy0UoEkHkaXQHMyRTVTZdItMhXi8HN7IWXZoK5gfck0xgpDZK0WXOQxwifrkD3mBxl8HJDsXH4O86mUPw75zii9pVY4cssUgCuDb1PEOQy9fXF7WPL3-yb77gtAHefr7YybbtQdmGBdzXIhvlZ7aqaIavxBvTEhDho8Ka4kRPBEn7SH99yYly93-x6PHu7ElUNlwaPeSrt7pgHVQb-fJc6mxyAhNDCfCMlg4pRU8zlbbtV8wulWyFIv1Gl6twi3REo0No1_wNGc0J3IhY-h7yP44VGEoqdsposeKdbyKLcCTEH2DIFgP6ES3t6q25V-x1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c578cb6e91.mp4?token=T0vgVEyopMWxfGoMqi70yy0UoEkHkaXQHMyRTVTZdItMhXi8HN7IWXZoK5gfck0xgpDZK0WXOQxwifrkD3mBxl8HJDsXH4O86mUPw75zii9pVY4cssUgCuDb1PEOQy9fXF7WPL3-yb77gtAHefr7YybbtQdmGBdzXIhvlZ7aqaIavxBvTEhDho8Ka4kRPBEn7SH99yYly93-x6PHu7ElUNlwaPeSrt7pgHVQb-fJc6mxyAhNDCfCMlg4pRU8zlbbtV8wulWyFIv1Gl6twi3REo0No1_wNGc0J3IhY-h7yP44VGEoqdsposeKdbyKLcCTEH2DIFgP6ES3t6q25V-x1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند سال پیش یکی از دوستان با آب و تاب تعریف می‌کرد از سیستم پیشرفته
بانکی ایران و کارت و انتقال پول با کارت و …
همون موقع بهش گفتم این گسترش سریع
فعالیت‌های دیجیتال بانکی به خاطر پنهان کردن بحران عظیمی است که اقتصاد کشور باهاش دست به گریبان شده!
وقتی پول نقد دستشون باشه خیلی بهتر متوجه میزان بحران اقتصادی کشور میشن تا با پرداخت آنلاین و کارت و…!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6776" target="_blank">📅 12:33 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6775">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=IjMbOyKj1RL_NtteMGJZsm5Gs6RcKu0dk1HAaq7jWdOEreWhdm0O0g6qcVEpwcKlep0pS7pX8c__X0FNKZ4yPwjYkIsKjoxEDQbbklNZhwqKg_8IHSkIj8rYC4yUzDxXTRsseWGcio64djvynU_SSIbMkdXBxJVuGpYDMV-S73dsJHZk0CuNsJXlRDoTKfUhQYZb0mNkqyZI-IVHPFBu38BrLKVji3qwOib7YROAqWH2TkoRX_oXLZgsMhkthEYtzRn0OjoHRut4ySyyhdproPU8V3dcnMcVvSOKCJieY7-8zzjvj1qwzGfAnk-bGA_r0xkNe2yz60nqQFCip_8wSlp-IhltTmdPSZnWUNhbqC2e3BGEDDoztfK2HFiKJpBzYUdQQFUrY-5ZINd3JQRJ_zkjlseDt6fIMiBJUXdOppKfMZTY92iOXtV8x2rYtzQDEFkViBX_PM5P4G-tABWUMeGExhb7ViL7e5Gmy_3jndSnk-isV6CYr6DCWWHucAOAV46IMMb6pCBwqC3m1aG9F0ToSpR0CCV8XDZz1bUpOg1ky8Ibohf7aLbPL4VNfg9qIgR50XyB6XBuAfAP8Xjp6bdYw8ArxpaewLzScURxo_ApfwMR8GhqxTaVa9lPpnLUc0uZN4KU-eDp1gNWpT7bfT1R25F9JUs_1nBAH6SZ7zI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a5052b840.mp4?token=IjMbOyKj1RL_NtteMGJZsm5Gs6RcKu0dk1HAaq7jWdOEreWhdm0O0g6qcVEpwcKlep0pS7pX8c__X0FNKZ4yPwjYkIsKjoxEDQbbklNZhwqKg_8IHSkIj8rYC4yUzDxXTRsseWGcio64djvynU_SSIbMkdXBxJVuGpYDMV-S73dsJHZk0CuNsJXlRDoTKfUhQYZb0mNkqyZI-IVHPFBu38BrLKVji3qwOib7YROAqWH2TkoRX_oXLZgsMhkthEYtzRn0OjoHRut4ySyyhdproPU8V3dcnMcVvSOKCJieY7-8zzjvj1qwzGfAnk-bGA_r0xkNe2yz60nqQFCip_8wSlp-IhltTmdPSZnWUNhbqC2e3BGEDDoztfK2HFiKJpBzYUdQQFUrY-5ZINd3JQRJ_zkjlseDt6fIMiBJUXdOppKfMZTY92iOXtV8x2rYtzQDEFkViBX_PM5P4G-tABWUMeGExhb7ViL7e5Gmy_3jndSnk-isV6CYr6DCWWHucAOAV46IMMb6pCBwqC3m1aG9F0ToSpR0CCV8XDZz1bUpOg1ky8Ibohf7aLbPL4VNfg9qIgR50XyB6XBuAfAP8Xjp6bdYw8ArxpaewLzScURxo_ApfwMR8GhqxTaVa9lPpnLUc0uZN4KU-eDp1gNWpT7bfT1R25F9JUs_1nBAH6SZ7zI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو : ‏مشکل ایران انقلاب است. مشکل آن مقامات دولتی نیست که کت‌وشلوار پوشیده‌اند و در برنامه «میت د پرس» ظاهر می‌شوند و در رسانه‌های آمریکایی آزادانه حرف می‌زنند.
‏ما در مورد آن‌ها حرف نمی‌زنیم. کسانی که در ایران حرف آخر را می‌زنند، روحانیون رادیکال شیعه هستند که نگاهی آخرالزمانی به آینده دارند.
‏آن‌ها باور دارند وظیفه دینی‌شان این است که آخرین روزهای دنیا و آخرالزمان را به راه بیندازند. می‌دانم این حرف برای خیلی از بیننده‌ها شبیه فیلم به نظر می‌رسد.
‏اما واقعیت همین است. این هدف اعلام‌شده انقلاب آن‌هاست. چنین آدم‌هایی هرگز نباید سلاح هسته‌ای داشته باشند، چون از آن برای باج‌گیری از دنیا و کشتن مردم استفاده می‌کنند. این خطر غیرقابل‌قبول است.</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6775" target="_blank">📅 08:13 · 07 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6774">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4Szyt3iwKiffkfFbZwes-L3QaC1asqZfO9dzIktwZilhsAIRENpp3CilQaIXj_4D1TrtBd65Gj_2yhCjuEe68GZvop1P_JHj6l5Tuvi5BEveqqd4npgHrYkdith1NsJaDZNMHHH7CDvIrGwfsuFoewrLpqnxHBEswhwpLsyGH8vR8iFn2NbIzwSv9VFYMbzyfLT-SGWIk6i_salmV4VJ2R1OLzRbqIWebdzjj2aT7tJ1bvPfxgFFjt41RFYxHgNyNJG00wLp7TyxHtJ4geE95Cd_q70XDmz4Eb9i2miy7TVgDq4FjUK_4qyobyATnjP0E6a6DSEhHo-9lDQhjn1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6774" target="_blank">📅 02:00 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6771">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d3KCI50qHVAJnzHKMSYzng5IIRtxQ9_gjC_kkLH6hXLSoqEJbvf_Tq9pmoeFfQ9od7qrhyHXHeQGCQAshk_6r8R-gnl2DNj1AMsBRQHV59u91II6mtsZW63G1OMNHyvSwwmlHtIkDl3BkKwE-CG960LC1AyucjF78jJie11CM3FwOz59nAmsnu60YwSbrQ_pQp-UOY39wjUmQlQ3fwdRsHA9Ztqs7a7cTZNIIgIjgT-gzgY9LlaG62U43R4szobEAZkGQ3hA7fK2u_l7ku6_w--QcU4dg3Rjgq_gUJjqkD0HeK-YiQXjw0Z2eXFyyETcdVKfM3NrOZpyw5TFKfJvbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gAsrkvuxsOklhhKEKO7UjKh2DkGVbYg2AsUBmJQtSyzEhPicuKQInAuLj6fXOhHvz1d7cnrkD6B1dZ-t2E53XkH9EPO0lkh7pc-wIIOVUm2HXBURGBJLW8mjIDVazuzXKonaMu07JICBeq95NBJJcw_noFnvdDDgJj_U5aJuTNIbYLjUlewqK_XyjBGm1PksmYs0RCTpWyau_8Zdo03Gg5NZO_OzjyhAtKcheg7YxV7NkGZJyhyfnD1O_treW5TZhr-zReREG0BA6yHbd8iIUA28qJF_0ta0puJfyFSgX4I0APX9JZWpPCwa4KoclFaHhahOqJIVFAoX8D090zX7kw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895be358cd.mp4?token=WEDRBayLMP_9jobkwTxR8btAMd1S7JXq6ezRpC9OErcvqwNfCSAzJXRmlY1ArhMmDnSMPwk6zN0xhmryvMjdclO5n7Gcekc54f0F6HiWt0fY4TJiOKXMu_BDdd44S-B-Ngbzwz5sGONMM__D70g5YOXGreIRLp80oGg1e0G_P5Wlf5wDLmeB28S1AoJ01Z5RE9rxu23gvJQfBSIxLc2GJ7yHYuSiblhv1SAxqk6Z5dMDqPfP68u72lq_HVXwvyBZpw2O_RbZU2VjT0MZYkPN1lvGe4V73b7zKKApBt8P5uNbOfObAzxGzXzsXMZZ2ffM-LJrl0BJeZ-GeMfShhJMSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895be358cd.mp4?token=WEDRBayLMP_9jobkwTxR8btAMd1S7JXq6ezRpC9OErcvqwNfCSAzJXRmlY1ArhMmDnSMPwk6zN0xhmryvMjdclO5n7Gcekc54f0F6HiWt0fY4TJiOKXMu_BDdd44S-B-Ngbzwz5sGONMM__D70g5YOXGreIRLp80oGg1e0G_P5Wlf5wDLmeB28S1AoJ01Z5RE9rxu23gvJQfBSIxLc2GJ7yHYuSiblhv1SAxqk6Z5dMDqPfP68u72lq_HVXwvyBZpw2O_RbZU2VjT0MZYkPN1lvGe4V73b7zKKApBt8P5uNbOfObAzxGzXzsXMZZ2ffM-LJrl0BJeZ-GeMfShhJMSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دو سال پیش
حسن نصرالله، رهبر گروه تروریستی
حزب الله لبنان، برای چند هفته،
ویدئوهای تهدید آمیز می‌ساخت!
کج نگاه میکنه! انگشت میزنه روی میز!
رد میشه و…!
رسانه‌های جمهوری اسلامی هم جشن گرفته بودن که آقا اسرائیل «با یک ویدئو!!» بهم ریخت!
تا اینکه در روزی چون امروز
(۲۷ سپتامبر)  ارتش اسرائیل با احداث یک گودال ۳۰ متری (به اندازه یک ساختمان ۹ طبقه) در بیروت، به تهدیدها و ویدئوها  و گنده گویی‌ها پایان داد!
به همین سادگی! فقط چند ثانیه زمان برد!</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6771" target="_blank">📅 13:06 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6770">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=BYz7CoYBGXOr652PkpdDJev0EMHMF-ffsiG_miBgWZCQPSv_iXy32i5RjfgqBhnz73njC0_-QlO3ldl5DLwK5lQdq0c9cDA0Yx0ukUIODtafoXMIxBPxmqPSi6Rba2YgKqFCHk2VdS09gfm3crDeyTKywWuy_Rlah8ErAjccqJ--baI-5kkwW9-RVDU9e1liBhmYPfdmu1m96o_RocEJAjKhM5p7WdDqh78c3-ErEuxpmM7VaOi8Ox30ZaUPZrIlwpLjswoQrUvdvAxJLghQsCbqJ8AGpQgySi5HWQsVffhrXNDdKr9IkRh1k89vpNrJFSFnV-z5oAvbBpfufXYSZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6de17ae0.mp4?token=BYz7CoYBGXOr652PkpdDJev0EMHMF-ffsiG_miBgWZCQPSv_iXy32i5RjfgqBhnz73njC0_-QlO3ldl5DLwK5lQdq0c9cDA0Yx0ukUIODtafoXMIxBPxmqPSi6Rba2YgKqFCHk2VdS09gfm3crDeyTKywWuy_Rlah8ErAjccqJ--baI-5kkwW9-RVDU9e1liBhmYPfdmu1m96o_RocEJAjKhM5p7WdDqh78c3-ErEuxpmM7VaOi8Ox30ZaUPZrIlwpLjswoQrUvdvAxJLghQsCbqJ8AGpQgySi5HWQsVffhrXNDdKr9IkRh1k89vpNrJFSFnV-z5oAvbBpfufXYSZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افتادن به التماس برای بازگشت به همون شرایط قبلی!  ترامپ ولی رد کرد!    احمدی مقدم چند روز پیش گفته بود به کشتی‌ها حمله کردیم - و تفاهم نامه نابود شد - چون میخواستیم چند میلیون بشکه نفت رو به قیمت بالاتر بفروشیم!  می‌د‌ونید که بخش عمده نفت ایران در دست گروه‌های…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6770" target="_blank">📅 12:49 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6769">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je6ivKDwKFKzgXC91bS1hlgrMeq9K1LDlEQBP0g1t01mNYeQdkz2OWcPyl7WjwI8JkjQ5Bm8lbNlL2vdfOvkMNVhB8SaKnaMqRmLTKZxa8qxuKQH3oCwlBAt-xvVvYjDSkCCTdSeN9rkAZj04oGpFdyhcuLAoZqHMUiVpp-Uf_yNcOfCsUMd6pEnIS_t5sV9r4n5PeM317lIcO8hD2fDAy93DdRq3ZJSZVL1MHOlIpdFFCi_4pnsmllAxOIt01t_hEBUlgkZZmv4tieOELtAmvCL4uKXiiastPkWYueI6FVENN_kngby5mEhQOivXZHfySDwqj8ciDpabvl20gK_dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد  تا به دنیا فشار بیاره،  اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6769" target="_blank">📅 12:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6768">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89284f5821.mp4?token=RJk8F9qUBeeynayv7zJMAx1nvHboUJw2V1IRdt6U0AYPUIQHJx3XHXdNF4ofJzvBeBgMnqPYMJC2pk9g0CZCCIjuff5UK4Nrh4YMRz0GHZxyUMAOh1hy7NEz-em-j4NwcknBtXK-Df6mZ45UVteWJ9watkW8MvQrXObxfNAO-O3KPEdVkhUFVpdyjZyWX_PkXfJAYXgDAFYE7tczKoIl0iuUy-xzJXIqJ682HzUjR0Op4UsNzEKW2M6XaEyERZX64_hqKJqtIrLrJuWnlfp1veozS00jvFwp5JxquUvGuW9YODElrVM9iD7hxr8B9RwVGh9IgqSqoYzWEkS9PmywTW1JiMdbWfSvAylzIJkKux19cd1XZE8EQ79ayw_wJT5hg7-K31c4-OKXLPjNuCYSt12KBeYuCQQxWh0-I9OtlwO_YxTVQiCK_APML5cMNcmm5fdcGb6BWBdmeN57r-uC7ChZyOvzNzvCvBjZx-2GO-VCK8YmVkPG4AU8WLaGuFL7PQIOZITgofe83dtB7af4Ea8aUI3QvTMpN17DN1QAx3MiqyFIp9T1zaUFSsMWNY1cHuTawyMlMc9m_an3ItGWK_aUXDjp9kjJEQgidNSuPnNh5Q0sTtjcixnch-Kmfd5aLzeRFzRzk4bQURCl9snLmY5SSf4f9JsM4sr433WzyiE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89284f5821.mp4?token=RJk8F9qUBeeynayv7zJMAx1nvHboUJw2V1IRdt6U0AYPUIQHJx3XHXdNF4ofJzvBeBgMnqPYMJC2pk9g0CZCCIjuff5UK4Nrh4YMRz0GHZxyUMAOh1hy7NEz-em-j4NwcknBtXK-Df6mZ45UVteWJ9watkW8MvQrXObxfNAO-O3KPEdVkhUFVpdyjZyWX_PkXfJAYXgDAFYE7tczKoIl0iuUy-xzJXIqJ682HzUjR0Op4UsNzEKW2M6XaEyERZX64_hqKJqtIrLrJuWnlfp1veozS00jvFwp5JxquUvGuW9YODElrVM9iD7hxr8B9RwVGh9IgqSqoYzWEkS9PmywTW1JiMdbWfSvAylzIJkKux19cd1XZE8EQ79ayw_wJT5hg7-K31c4-OKXLPjNuCYSt12KBeYuCQQxWh0-I9OtlwO_YxTVQiCK_APML5cMNcmm5fdcGb6BWBdmeN57r-uC7ChZyOvzNzvCvBjZx-2GO-VCK8YmVkPG4AU8WLaGuFL7PQIOZITgofe83dtB7af4Ea8aUI3QvTMpN17DN1QAx3MiqyFIp9T1zaUFSsMWNY1cHuTawyMlMc9m_an3ItGWK_aUXDjp9kjJEQgidNSuPnNh5Q0sTtjcixnch-Kmfd5aLzeRFzRzk4bQURCl9snLmY5SSf4f9JsM4sr433WzyiE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ با اشاره به تنگه هرمز : جمهوری اسلامی دامی پهن کرد
تا به دنیا فشار بیاره،
اما این دام علیه خودشون شد!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6768" target="_blank">📅 12:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6767">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0493705c07.mp4?token=KXq79byRHedWhzehx38SeBrGXBbg7YNrR2OZweYLneu3wnU5NlyjjovC9fTgeKC_znz_WLbs1glG5HL1MCMUHTGY1_FUdcK9FHym5iV-j8lHtX55kuImtYGkHwHRJGEfwIeGNo9GWjStUSl0UAB1bzT50Riam0cMBI6FUK4DUL2dUxQUAeW3ehyekQETxVqsrOEmPx19GHVjC9D5PcNXjqOu_CyLcyTTR1L-gg97qov-2jU8-aFoNdo69RQvnKDjjkr16A-8YU_sfkIlaaOOXwOF4IBX301iRmranQd4YcIs1J6Q1xp74SugZPhqn86cAU-j2_iXG9LqQbbmiUkuKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0493705c07.mp4?token=KXq79byRHedWhzehx38SeBrGXBbg7YNrR2OZweYLneu3wnU5NlyjjovC9fTgeKC_znz_WLbs1glG5HL1MCMUHTGY1_FUdcK9FHym5iV-j8lHtX55kuImtYGkHwHRJGEfwIeGNo9GWjStUSl0UAB1bzT50Riam0cMBI6FUK4DUL2dUxQUAeW3ehyekQETxVqsrOEmPx19GHVjC9D5PcNXjqOu_CyLcyTTR1L-gg97qov-2jU8-aFoNdo69RQvnKDjjkr16A-8YU_sfkIlaaOOXwOF4IBX301iRmranQd4YcIs1J6Q1xp74SugZPhqn86cAU-j2_iXG9LqQbbmiUkuKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موج جدید پناهجویان و مهاجران افغان
به سوی مرزهای ایران</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/farahmand_alipour/6767" target="_blank">📅 17:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6766">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vroIkvU940MFg33QLnzAhmWi9p5DpOztt8usiQZS3i7WWpVmaKJt7Cml66r3d5XZedldMSRQHVAY2kHXFbVcy3R2LB8i_gerKctScpoaY-bCXzPwl4R2I9f6mcUXscPAHSKG5a4sE_PdEpCPPkmFNqvOpIQKt-hb42u7Lw02w5a3kX2T43AnHU2L1nKkK_Cm5cC7AzrM9jD1zCCpviUbdbh4RISWfqDViJhI0gmaBW4e3-FvhqgZClpbOkAbg39FGdujWPcG4LH3qez43TL9oAUR-gZ_HeJqN5DvzHs0_Vm5HuRhHXchvfDvLf1qEobGe3_K_Y25WG-XrNc-7r8gfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این ویدئو و این حرکت یادآور داستان‌های عهد عتیق است!  شجاعت و جسارت فرزندان داوود!  که در عین جوانی و نحیف و خرد بودن،  مصمم و بی‌هراس،   مستقیم به چهره دشمنان خود می‌نگرند!  مثل داوود، نوجوانی ظریف و آواز خوان!  خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6766" target="_blank">📅 15:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6765">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=TuWrMbxOM98xIEPR3XsLTGxqDLrWIZfUX_0rzKahLIPMvzaIJme5FJtb29k0Y-vtqpKGh097CvYO2Dy6z3vQVCpgrpmYg9NGjVo-dKmusrk2M2y6XOWHxsHbf6gornS0OGc_LPnFf55rd0XhWVVBiMbIlZi0eUMkM89wWsY9RSOgaReo9-vSA6nQ3BBh-p-0b4FEdMYcNd1lfu0-Y9sW0YtNutGFSvilAIKNvTeKLgLGs22-5CU66WMaXYNb_2L6llra1V8aus_7pV5BTSkuEODgvOwaFZ_i1thbCguHxE1L4qRBU-cYP1VdolcyXo6ItwVZBzISzmeTN1AknVHRmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bed2bf69f8.mp4?token=TuWrMbxOM98xIEPR3XsLTGxqDLrWIZfUX_0rzKahLIPMvzaIJme5FJtb29k0Y-vtqpKGh097CvYO2Dy6z3vQVCpgrpmYg9NGjVo-dKmusrk2M2y6XOWHxsHbf6gornS0OGc_LPnFf55rd0XhWVVBiMbIlZi0eUMkM89wWsY9RSOgaReo9-vSA6nQ3BBh-p-0b4FEdMYcNd1lfu0-Y9sW0YtNutGFSvilAIKNvTeKLgLGs22-5CU66WMaXYNb_2L6llra1V8aus_7pV5BTSkuEODgvOwaFZ_i1thbCguHxE1L4qRBU-cYP1VdolcyXo6ItwVZBzISzmeTN1AknVHRmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدئو و این حرکت
یادآور داستان‌های عهد عتیق است!
شجاعت و جسارت فرزندان داوود!
که در عین جوانی و نحیف و خرد بودن،
مصمم و بی‌هراس،
مستقیم به چهره دشمنان خود می‌نگرند!
مثل داوود، نوجوانی ظریف و آواز خوان!
خامنه‌ای بر تخت ۲۵۰۰ ساله شاهان ایران تکیه زده بود، اما اسرائیلِ ۸۰ ساله، از این نهراسید!
یا از اینکه جمعیت ایران ۱۰ برابر اسرائیل است!
یا اینکه مساحت ایران ۷۵ برابر اسرائیل است!
در قطع سر حکومت جمهوری اسلامی تردید نکرد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6765" target="_blank">📅 15:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6764">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gX3caXtZRV_jMSbj7XRr-jQEnxanLvz3aOCEnAdSNWRNSeFKqZtcwNar3OGkPmgevN5CjjabMJDlLAmdLv_AJBDh3yktYQyICJ_g9BNtxFjNFPpdxaqK-Z32iH7-A5xukIoNyzFxZlBwgq3cKcdjwqVFAU8cJbG2MvX0eq5fQUaxFNWjKFh4PsV5fV7AzxaJsDh74YnPKvV74qSTVgXVB8zC0agxJLODvsaRwDRR_h92xlfCSATLZMeWflmqv4ggJygaLCHOhnfdo-ACJ5JKfBxjQPA7qdaBjTuTGmpOzCK2AcpfCy-Z0691SlLQczFb_KwHa48W7cgHbZNtpTkO_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.  . این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،  و نقش میانجی‌گری این کشور. (وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6764" target="_blank">📅 14:27 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6763">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-ugFNVS16n73qjk7Vl4LusWR0EioQMZioAl1BLhR4BREWd8BnUIwYDONBQFrD1uNNP1xZdiQUBH7B5isZ5d14xw72IFinruo9-D9ZxWcD7wY30Z1iY1FLUooxBTS46MJ4wUeX1wKX78hkkwyXqtyATu42Cx47pS1kHekb1iWRJrUJp992uKeG-mMcEUHbfArYfM5tBb5Iez_HAGCVIXFQLP9NUDh8xFs-lpeV-iknTCFj7htkbQlROC7K6DO__x4COUNXel3Y9B7MP04n29Yzjf-WhCVz_i-0Dh-8FZMd4FIkCfJIAhdEjVf9BFzWrZDpgnugswU3uKkc1D8e-O_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
احتمالا ترکیه تنها کانالی خواهد بود
که برای پروازهای ایرانی (به سمت غرب)  باز خواهد ماند.
.
این به خاطر جایگاه متوازن ترکیه در سیاست خارجه است،
و نقش میانجی‌گری این کشور.
(وقتی همه دنیا بعد از  شروع جنگ اوکراین، پروازهای روسیه رو با شدت و حساسیت بالا بستند،
باز هم ترکیه این مسیر رو باز نگه داشت و گرچه  از انتقادها هم مصون نماند، اما کار خودش رو ادامه داد و سود بالایی هم برد)
🔴
با توجه به وضعیت افغانستان، پروازهای ایرانی به سمت شرق (چین و..) هم احتمالا ادامه داشته باشه
🔴
و از روی خزر پروازها به روسیه ادامه خواهد یافت.</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/farahmand_alipour/6763" target="_blank">📅 14:24 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6761">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=OrlztzsVVE1Z8DHLP883izlU8eNg29kgqq0nCqM-bm6Bu79OXI6vToIHEsh6cP3sMmkfg0lVGyZEr_qmA-BJGXYvLnFSq7Nq5tuQOu9kJqXZtT9z74mfGIm9VxLRYaTvXmJfg-S1k_FfTwQyl4VVUvwwucEx2TvfvJHo-N7k5UulyNuoQmtX2Jzd8j5u-nln8Dwy1h3UwNueVfcycRizI66AOUHUbrVmyUSp3w4AL3BpzQBTM80hHfcC59wulk9yTGI_tNkb8O74Uy-3yuqQzW62XecylwKKKqmTgwfpbmqx0cHBeMssdF_LgzPJIvfkT8Ls7iUnu8gn0n0UEd7mdXIOtolZuKnLq4YI6EHXZpchlglHakzzyO1dkqy9Lcch9xvWbG-1Uf64VXFuvFcx-4DVwIFPJKJ09uCbnFzf9I9jCCjkRMHag8ekpI_8qF5THI1kzkTYgzgYbPM6scuHJoaMDJnO_oa8TxdnU_xFOZBPDljwNmI3zp2o3kl4Q9675aIUOAByQxSRYUzOQO4E3A_L37dF4FJlO8heCrFP33q_H_5uIta7L1ln-xBN1oyxPa-6Lyl4-xIK-ZHBGtzNFdcSnsH9y3GPAbgP8Qs8hePvRTreZobSGTe4U9VsJl2rm9DTAIDIhu9U0q7OVFXLhPwfsAe7mAcczWONICnAWP8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ad92c6104.mp4?token=OrlztzsVVE1Z8DHLP883izlU8eNg29kgqq0nCqM-bm6Bu79OXI6vToIHEsh6cP3sMmkfg0lVGyZEr_qmA-BJGXYvLnFSq7Nq5tuQOu9kJqXZtT9z74mfGIm9VxLRYaTvXmJfg-S1k_FfTwQyl4VVUvwwucEx2TvfvJHo-N7k5UulyNuoQmtX2Jzd8j5u-nln8Dwy1h3UwNueVfcycRizI66AOUHUbrVmyUSp3w4AL3BpzQBTM80hHfcC59wulk9yTGI_tNkb8O74Uy-3yuqQzW62XecylwKKKqmTgwfpbmqx0cHBeMssdF_LgzPJIvfkT8Ls7iUnu8gn0n0UEd7mdXIOtolZuKnLq4YI6EHXZpchlglHakzzyO1dkqy9Lcch9xvWbG-1Uf64VXFuvFcx-4DVwIFPJKJ09uCbnFzf9I9jCCjkRMHag8ekpI_8qF5THI1kzkTYgzgYbPM6scuHJoaMDJnO_oa8TxdnU_xFOZBPDljwNmI3zp2o3kl4Q9675aIUOAByQxSRYUzOQO4E3A_L37dF4FJlO8heCrFP33q_H_5uIta7L1ln-xBN1oyxPa-6Lyl4-xIK-ZHBGtzNFdcSnsH9y3GPAbgP8Qs8hePvRTreZobSGTe4U9VsJl2rm9DTAIDIhu9U0q7OVFXLhPwfsAe7mAcczWONICnAWP8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترکمنستان، آذربایجان ، گرجستان و
امارات و تا حدودی عراق،  آسمان خود را
بر روی پروازهای ایران بسته‌اند.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6761" target="_blank">📅 14:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6760">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gZQt3INfJU8DGU4XfxR1K5z4CBCFrL5p1VlEAuswbVK9GIAIibMsCucx-EO5HF1CWhCZa31dVkt5_nIYgYOlAD1qCIloLm53qzqt7Hdme4EQcBWaGbkYJ4eZ0-BC31iZ8bXWoQsKEkibPZJSBwpmdpQh6TSlg9aTvE921vAra7lxSL9beINFPSnWHnivzL5qp-q6YaA9Ab9oJDMXMu5fCIcarkHTk9cYsDraducqN15vq45PdGpvOQr33uIrXNAJ8bCrApkO5nf_ra52Hp3zcc_WJn9cKu2O5aZhdMpxE0Roi3eHVHh6cmpgcJPJJ-fTD6gPHvxTWn0F2J3tUVyZYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6760" target="_blank">📅 00:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-6759">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CtWTs6t1ccYN0HRsE9uZp0-8ex0pBmW8zIt8QuzYnBReXhQ5ttx-8GWPGfPN8WSt710gq6_hYWD_-vY_9LyvKnNLbQ5xp5mDtHgqu5Kf-poZYoEPdWH3AYIjbQbPhrgfCUCTpxB7GYpg8nbMqHle_cW16kDaqf_SVWtHAajON9uGcHZjRTQvwFH6DZJesbVhoDNDkcruLWhTQQT0Qa92NYKj6C3EHrRQCm75DvNUKq2uAGNY3kpzd4DepyuZBOEqEotJteGeSTIcHcC6SdvrfTCMsklSLRtaufHctK05sxzWXx2Oa8yNhG-qumJHJm_r4yaOr2Kg2VKZ5R9ALVN95A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمد مهدی حبیبی؛ دبیر کانون امام الرحمه:
پزشکیان باید تو نیویورک با دستای خالی به ترامپ حمله کنه و اون رو توی سازمان ملل خفه کنه تا انتقام خون رهبر شهید رو بگیره.</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6759" target="_blank">📅 20:19 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6758">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=QcXq-Q84jFGnScrqdQyP4zk74S77NQFQ_O6aBkeFIFuBhOetRbgSgi0OaVgmRAM9cHX_-KQ1uCXOEKED_vMy929tVaXTXjf32KrbXpYUFGq25yqxG6QcCtfNePGNWFbS2inr204dR5dI1t9lIRiyH9eI13wdzuDcbyFx1rz58jLERunweKtUmDX99vRr9jit__WOs0JnwYVpG2YDABYDhzr9IE_xvflWot575irAh1b35lAblED4aeKfUYe8IN7jivL6khPjVrwSJg9mCD-X4nQ2R1-WOIEq30edbmpbkZp5shFgMQe0pUcZEpHuBkXAqfOo7m_C67D95sLustrh9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1873c41e65.mp4?token=QcXq-Q84jFGnScrqdQyP4zk74S77NQFQ_O6aBkeFIFuBhOetRbgSgi0OaVgmRAM9cHX_-KQ1uCXOEKED_vMy929tVaXTXjf32KrbXpYUFGq25yqxG6QcCtfNePGNWFbS2inr204dR5dI1t9lIRiyH9eI13wdzuDcbyFx1rz58jLERunweKtUmDX99vRr9jit__WOs0JnwYVpG2YDABYDhzr9IE_xvflWot575irAh1b35lAblED4aeKfUYe8IN7jivL6khPjVrwSJg9mCD-X4nQ2R1-WOIEq30edbmpbkZp5shFgMQe0pUcZEpHuBkXAqfOo7m_C67D95sLustrh9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در دوره «جاهلیت» سطح موفقیت خدیجه
چنان بود که کاروان‌ تجارت خدیجه، به تنهایی،
با کاروان تمامی بازرگانان مکه برابری می‌کرد!
اسلام - ظاهرا - ایشون رو به جایگاهی رسوند
که به گرسنگی افتاد و خوردن چرم کمربند.
حالا شما میگید جمهوری اسلامی
ایران با اینهمه نفت و سرمایه رو فقیر کرد.
این چیزها ظاهرا ریشه داره!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6758" target="_blank">📅 16:27 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6757">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=F7_khznJW2-DBns24H0Cw-mVvEzDAoTcYwy4P_BqEVxDld7_AkSyNkY7nTAMEMAAWcG3uBw4vo08i_Rj7JZHNlkkbE9MbiJaOvggYAmXd-dvJG75TLbWCRr35ygSBRdbOSKoFauwttqJx0XUb9e_18Ll0_h2NnIZ4cXk_bw6tnTcbbBItb1rCjVMANoB6nqvTbG9K2zRcxPztetY8dhmqTjCLTN0d8NmwTQS5uztGVODCuBEpRMrJe4QdWyPK_LFiY58Dvjww3b6TLDDlH4thu1rdfoWXhu-o0Hzf8VV5pbiu209Y6SU-I_FXT9ZUCleJSEdpQtsPx_LED7y3nx7uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ea338b87e.mp4?token=F7_khznJW2-DBns24H0Cw-mVvEzDAoTcYwy4P_BqEVxDld7_AkSyNkY7nTAMEMAAWcG3uBw4vo08i_Rj7JZHNlkkbE9MbiJaOvggYAmXd-dvJG75TLbWCRr35ygSBRdbOSKoFauwttqJx0XUb9e_18Ll0_h2NnIZ4cXk_bw6tnTcbbBItb1rCjVMANoB6nqvTbG9K2zRcxPztetY8dhmqTjCLTN0d8NmwTQS5uztGVODCuBEpRMrJe4QdWyPK_LFiY58Dvjww3b6TLDDlH4thu1rdfoWXhu-o0Hzf8VV5pbiu209Y6SU-I_FXT9ZUCleJSEdpQtsPx_LED7y3nx7uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سر تکون دادن،  یعنی خیلی اوضاع خرابه نه؟
رئیسی هم کتاب حافظ رو برای اردوغان باز کرد و خوند :
«خوش باش که ظالم نبرد راه به منزل»
و امروز نه رئیسی هست و نه خامنه‌ای!</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/farahmand_alipour/6757" target="_blank">📅 13:33 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6756">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
دولت عراق تصمیم گرفته تمامی پروازهای هوایی با ایران را متوقف کند و این اقدام در چارچوب پایبندی عراق به تحریم‌های آمریکا علیه ایران انجام می‌شود.</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/farahmand_alipour/6756" target="_blank">📅 22:22 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6755">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترامپ: اتفاق بسیار بزرگی در راه است
‏خبرنگار فاکس‌نیوز می‌گوید دونالد ترامپ در گفت‌وگو با او درباره ایران گفته در مرحله تصمیم‌گیری است و در آینده نه‌چندان دور «اتفاق بسیار بزرگی» رخ خواهد داد.
‏به گفته خبرنگار فاکس، ترامپ سه گزینه را مطرح کرده است: نابودی کامل ایران، رها کردن جمهوری اسلامی تا از نظر اقتصادی فروبپاشد، یا رسیدن به توافق.
‏ترامپ همچنین با لحنی تهدیدآمیز گفته پرسش این است که اگر تصمیم به چنین اقدامی بگیرد، چه زمانی کل کشور را نابود کند؛ و هشدار داده که «بهتر است آنها رفتارشان را اصلاح کنند.</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/farahmand_alipour/6755" target="_blank">📅 17:40 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6754">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">این حرف‌ها چه چیزهایی رو یادآور میشه؟  ۱- اکثر مردم لبنان دشمنی با اسرائیل ندارند!  مسیحیان و سنی‌ها که بیش از ۶۰٪  جمعیت کشور هستند، گروه تروریستی  حزب‌اله وابسته به جمهوری اسلامی را عامل تداوم جنگ‌ها می‌دونن!  حتی به زخمی‌هاشون و آواره‌هاشون خونه هم اجاره…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/farahmand_alipour/6754" target="_blank">📅 16:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6753">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.  انتقام خون خامنه‌ای رو گرفتید؟  عزتتون مستدام!</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6753" target="_blank">📅 16:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6752">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=PwQtNMybDXma1u42zIofAWGanesFh5TWKKCPoN25M0ztfy9DxKDtfo_JtREYBa7ODqqky13AZNRes_cp1wJjKNRxsmefgvG5xX9kn5eBZ65M155km_gbZ9Y3vBY-fdKHebrYkEDlc3kMFssTDpKx_ukIWi0q-1LTFP2pr17THguaoWUha4jC8wMwMYT3nvJX8bl4SgWNYCpYz-_RqcPmIWziUG89RW8181X196WATKVhXG91VFQQ78oJ7ZVIUx04TPg2zIcjWkn1WfvBgYFHVRoDdSvGfgblsC6eerGYAnvhZ8QqsIOYUtd6dX9AX9oHXbIVmFObgBmeJKyjBphF0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fd2c8ce135.mp4?token=PwQtNMybDXma1u42zIofAWGanesFh5TWKKCPoN25M0ztfy9DxKDtfo_JtREYBa7ODqqky13AZNRes_cp1wJjKNRxsmefgvG5xX9kn5eBZ65M155km_gbZ9Y3vBY-fdKHebrYkEDlc3kMFssTDpKx_ukIWi0q-1LTFP2pr17THguaoWUha4jC8wMwMYT3nvJX8bl4SgWNYCpYz-_RqcPmIWziUG89RW8181X196WATKVhXG91VFQQ78oJ7ZVIUx04TPg2zIcjWkn1WfvBgYFHVRoDdSvGfgblsC6eerGYAnvhZ8QqsIOYUtd6dX9AX9oHXbIVmFObgBmeJKyjBphF0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهو :
«نصرالله، دو سال پیش هنوز در پناهگاهش نشسته بود. الان کجاست؟ با من تکرار کنید: پررررر!
و سنوار کجاست؟
پررررر!
و ضیف کجاست؟
پرررر!
و هنیه کجاست؟
پررررر!
و با خامنه‌ای چه کردیم؟
پرررر!
«سران ترور را یکی پس از دیگری هدف قرار دادیم.»</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/farahmand_alipour/6752" target="_blank">📅 13:42 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6751">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GTbWAwAi5KekLQBz4JuJDdv6SYzWbx7p__6MoeKT3w4wad1cu8wlVt-BRsIA1eouVdTNNKmEWuRnxNlR1Y2r_-cKX0JQGQqWk8Ox8cdbi1hS_fHV9VtdYw7vQC_NfYvX7HdyeP4k6k4FwEfxv8EFeiIa9a49BxqJG1Z7ZcLh46IJoRgDaCwaL0lzQ0JrDwe128pnbWZuQ3n_BFCj-IYU-cAwwYfr9ut3UmlIatYBs52ufbPaRVZylvLe_l1fBSNvN96h4ny1TOIMyiA3CNfeyV_R1tjfuGFdDJyXG3_c28e_Rt2NtHVt3axzLv68GlHGM30c87ZoFZjDg2a9-nkY8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فردا میگن : اروپایی‌ها و غربی‌ها
حسادت کردند به اینکه ما تنگه رو داشته باشیم!
نمیگن ما رفتیم بستیم تا به دنیا فشار بیاریم دنیا هم اون تنگه رو دور زد و ارزش جغرافیایی و اهمیت استراتژیکش رو ازش گرفت!
تا گروگانگیری شما بی‌اهمیت بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6751" target="_blank">📅 13:34 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6750">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JzpTPRFIWN5lLP_O-ioP59PKwlgtXeGaIv1YxlV5C8TfXDZwF4z_G-Y4RCW9YJroAjOFfB0hAoOwi68TJkpDlYznfFJxZXHlRhsdKDiuPOjsmN03SaLs6FO8uziyp86iAjwYZO_XpdPIylndHdgBZ3HqDhEkEwBH9lbX7YO22XI1Ru1yQMRL3sLFgYWjQTkcsRciBbV_GX4V7Q9em9btZKizt9UiaTdm34LqXCUW4Y8_jv-Uw4qnMBH6JRYOb1QiHGhTSxtzVdtcMEehd64WKjSa55cJPX_2YH0OHvWC5_-J3JFWxShWzDAmfe9_5SosIYAKuf7cWEXPOLVPMr4_HU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04900863be.mp4?token=W0_-iWPkYEHS_8631ORfEGhIyMUOtOaEh1tr7UfriUmR97NPuodmi4eZhNRxxADqPC4J06R6ujWaJTw0ygoBToeja22wMgw_qCoQyLpqVGk3hQ_UXRVskS0vsJkweKmVAyAdPvonNvG1oHbkn-txIOr8Vzwtvuyc5xF6etSUsfLh8Kc7Urr_QolJ8a6jGFtJieljguC-20DYK7JySvJNyc_sWagFBneTUWwHDAHpRAJckGs93oLutUUe_Az9G_W0hTAo7rry0HURrQ3W2j6qfduIeP1WFxCTHn0mzKqsVl4BooB3uc7kWRXwKfO1SnDybbAecBydosl35w2qfSrw8JzpTPRFIWN5lLP_O-ioP59PKwlgtXeGaIv1YxlV5C8TfXDZwF4z_G-Y4RCW9YJroAjOFfB0hAoOwi68TJkpDlYznfFJxZXHlRhsdKDiuPOjsmN03SaLs6FO8uziyp86iAjwYZO_XpdPIylndHdgBZ3HqDhEkEwBH9lbX7YO22XI1Ru1yQMRL3sLFgYWjQTkcsRciBbV_GX4V7Q9em9btZKizt9UiaTdm34LqXCUW4Y8_jv-Uw4qnMBH6JRYOb1QiHGhTSxtzVdtcMEehd64WKjSa55cJPX_2YH0OHvWC5_-J3JFWxShWzDAmfe9_5SosIYAKuf7cWEXPOLVPMr4_HU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیلی‌ها بمبارانشون میکنن
مسیحیان و سنی‌های لبنان هم محلشون نمی‌گذارن و حتی خونه هم به اجاره بهشون نمیدن.
انتقام خون خامنه‌ای رو گرفتید؟
عزتتون مستدام!</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6750" target="_blank">📅 10:26 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6749">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وزیر نفت اختیار فروش نفت نداره
صد میلیون بشکه نفت گم شده!!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6749" target="_blank">📅 09:55 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QKujfk2edENFsxqEcggsXEly7we0bo6E1hC4EkjxTgCSPVu-rlQ6iEfuhlOZJD4FV8G6ttFYV5e5aJ3kuGFv53AbdKhpH3jcht-o7ejnLG225bXZ3erBCrR0JUIIg0OZLKKeLKvMhx51KrDCvS_P8DxSqup5943JfaJmYElaybrq8lnv3oLIvOkncSIFb2rcarR0J1O-R2tu2XYzmuBBj_3cuOmvZr-k_LY2rMM3MyA2SVDGUCTk0FpeOlTaqJtkyR6UcTwz7HPrvHWVj9AghWVaUfXTEeIl4W1XukB5OkGQ96O0KF0rz2LE2B3SxcBjadT2AJ7FMCMOKs8sh-2Vaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=QKujfk2edENFsxqEcggsXEly7we0bo6E1hC4EkjxTgCSPVu-rlQ6iEfuhlOZJD4FV8G6ttFYV5e5aJ3kuGFv53AbdKhpH3jcht-o7ejnLG225bXZ3erBCrR0JUIIg0OZLKKeLKvMhx51KrDCvS_P8DxSqup5943JfaJmYElaybrq8lnv3oLIvOkncSIFb2rcarR0J1O-R2tu2XYzmuBBj_3cuOmvZr-k_LY2rMM3MyA2SVDGUCTk0FpeOlTaqJtkyR6UcTwz7HPrvHWVj9AghWVaUfXTEeIl4W1XukB5OkGQ96O0KF0rz2LE2B3SxcBjadT2AJ7FMCMOKs8sh-2Vaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SziB2irWk7KHN1cCfCv-IKskCpVicYsKqNKYBcPv2EuXD9LlmJzijUS3ogqROKH0mWA9AHyqGMz04m9moNsZBS2ZMS3ditVSBs402HL4ZJZTeNXd8wHfxJ5A6RbTzSpv5-Mpo-lXaKE8MLsRJg93bKHkQVnr5msfYdKN5iLenc7vojxJ1nu-3izg20S0BtnDbnAj9OtbWZxityJ1IkulAWGhEN3quOfi1ol-s91prjHtNSCEoxh0mf166wavFAIZuZ6x4vFSP_Td1c14iFjiBm9qaHhlshyaGPXHF-T7F9S7Krhy7sYS6sDP8k3YQkyUIypI0NstcQGXaFNfjsPQsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=BmD0CPgWZIW92e0q7PYBYrKnuQdCG3hm30ReEc5UYZxsxS70qXA2Wga2DdcOu84NA24IS6gmadNwav4fpw0EzW38SCzdpWa91qDgAje_oxNeV8COelMad0Bi8xKYVQfQYpyjl_A9aeSH5iHCmChcLApaY3J5MKaMvaeOssY-vLYf03kWQtYtXHXsVaDDcR5ilSbg5JzmQSvX9e_UrNixZoh0D7mImoG4MMYJw-Ce2EvAGKFBaeDTD4M4WhenWyhiW4bqm0CqcfEycHlri5a7WSxrM82ALzZl_i8pdmGBnunqFK4AQKpoevCXxkpW85Nqx7x9DixU8K37lJvSEyhg1wFzlcn2dQcpeD10HobsooV54B_EZ0lLCuRfQ_i3O0QPHw71SFHRRYST2YMmeKKObK_R-1VDsNpb51BIL0L3Z_mG4X8D9Sr_2bH99pYEjBhHGJ8chZPnUbGegLbgG-QUGlmC1Ly_O2FjxT0RYl8nAaoWUXomcuEI0jmnFMCAO9ryI0svvTdU4UNd0Smk0rf7Ek0K0r7xlwIipIPmbNYeSeNJsmQ74vMa80vRY3iGGDe6NkpadjIVezUTUhy52cpx9GOUfukHYJtuU2SSeBQLx7rR1BJNH5KldZLoMKrCVRrSpvPyJ-avJlVWhZ4juiDthfNYLEn6EWBOio3omG7_fls" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=BmD0CPgWZIW92e0q7PYBYrKnuQdCG3hm30ReEc5UYZxsxS70qXA2Wga2DdcOu84NA24IS6gmadNwav4fpw0EzW38SCzdpWa91qDgAje_oxNeV8COelMad0Bi8xKYVQfQYpyjl_A9aeSH5iHCmChcLApaY3J5MKaMvaeOssY-vLYf03kWQtYtXHXsVaDDcR5ilSbg5JzmQSvX9e_UrNixZoh0D7mImoG4MMYJw-Ce2EvAGKFBaeDTD4M4WhenWyhiW4bqm0CqcfEycHlri5a7WSxrM82ALzZl_i8pdmGBnunqFK4AQKpoevCXxkpW85Nqx7x9DixU8K37lJvSEyhg1wFzlcn2dQcpeD10HobsooV54B_EZ0lLCuRfQ_i3O0QPHw71SFHRRYST2YMmeKKObK_R-1VDsNpb51BIL0L3Z_mG4X8D9Sr_2bH99pYEjBhHGJ8chZPnUbGegLbgG-QUGlmC1Ly_O2FjxT0RYl8nAaoWUXomcuEI0jmnFMCAO9ryI0svvTdU4UNd0Smk0rf7Ek0K0r7xlwIipIPmbNYeSeNJsmQ74vMa80vRY3iGGDe6NkpadjIVezUTUhy52cpx9GOUfukHYJtuU2SSeBQLx7rR1BJNH5KldZLoMKrCVRrSpvPyJ-avJlVWhZ4juiDthfNYLEn6EWBOio3omG7_fls" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mq-M6nALbYHpsfy7ExE-9EeVcI-N5RVNW9fznoEbzpRJRv3byg0bX7MIwx1aNRfp8V2eh09HE9flNCVQiVCcU0l5Fuu357Jj3899_MmNDJOu4-SDNp150N9yk0cWInOA6vRuTFq-XrNqrOR3sdHJTv9_JEBqYw3Z1JMVWaa_8P-4_dGMYz5xJeAxjwZpD-UV0hF0SISNqA8diAwnKzYcOK0daMGe3tLFpcnjwbO1r0XocSHP1qURZ7mJR26afRPwGrfQcl4mK0EJuT-BjTsya3gLfi40LWDT24KK1TJVVJjL7qrrNdUiv1XLTmdhydRV-mLMgAV8OawwBnSXEGfdaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ov1N55Ev1PFD9-H2aDAhjPCjWly1FR_RxWyNw_VukJ76IHD2cWn691S7zW_KA0cxNxNsVB1HKOAgD5oFt1xpfGBP1gtd3WnW6C4EoqctYjBOp4g5qQlcRE3pIDQdcc-kMDEvuODzM6x5sFhjA5W80B4jZnqP8tCaIIMJPTHYS-SW8FMt005_No6MXqRgZxOLCpzY8RwN9myxq9YKchnspdVzSO-8nQeXSblolj8XWL60ekyHw9-uJs_U9ZKHm7ZNYKrOaj9Dp4IwrTU1muAPZseG5-d36TTUwwdYXf-wcwrbvJxtBKGkzMgVyG4OvpPevKdcD3oRvqVFB79HDVhjFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=ov1N55Ev1PFD9-H2aDAhjPCjWly1FR_RxWyNw_VukJ76IHD2cWn691S7zW_KA0cxNxNsVB1HKOAgD5oFt1xpfGBP1gtd3WnW6C4EoqctYjBOp4g5qQlcRE3pIDQdcc-kMDEvuODzM6x5sFhjA5W80B4jZnqP8tCaIIMJPTHYS-SW8FMt005_No6MXqRgZxOLCpzY8RwN9myxq9YKchnspdVzSO-8nQeXSblolj8XWL60ekyHw9-uJs_U9ZKHm7ZNYKrOaj9Dp4IwrTU1muAPZseG5-d36TTUwwdYXf-wcwrbvJxtBKGkzMgVyG4OvpPevKdcD3oRvqVFB79HDVhjFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1N-Fdf0CQhAPlh-iiL3ddFozflyAIfZlS9duGEAX5FQgZybv5e19IOMd32o65irI4O52f0EMWJy0UIK9JGC6vWV4LoLXuj-AIBf80F9Tg0OuM2pR8Im7PAJcI7iOlVNx5YWXUg-NRIhM-5K42Kz7CjjJiAcFj2qifbdNxXqQHjGJGaObmUyLMVGKlGBmwpehzcDVRegXriDMRP-YzA23fLCjd1QOvLJIdTJXLlFC3R_wuXo5dmANqCo2RmoMRA5xVbnvCl42wijd_VdVuAZczRX-DQLaC2jSO7Qugtf_eGxxzmJmTvp3JD8VY1_-RowcQqukKB6IUBI18_vjz1nZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CnQ3rBF_5J3Yu19zUxT3oX5xwUfBleJ7_M0Eq5QY1S5m9j_RT2s_QKa9mLkWteU-6ARj0GXtywImAQx3X161LCDrXyKALyujuKTvLIZZihW5VjrHOS-hQqLfWjoJuuwTWQZbcGxEerzIzxGH7Hm59etui106c6vCWq4BkIzlFwI9n0YAo6HM-KNPJQF1p0MSyb6EAux3SCOvGWlJL2c6Jdl54v9Rb1TT1-Tl8wGlUfFz1S_4Z8uaBcb9TFK5k7X3Ync7NKHaF-3KfATZugjyTFbJ98uYfoXSyQ6IyzgBxE1C20a1gL1xjy6cdvUd6iPzky02u1LaNDiFJgkGDDXqzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbUaTNbnzk5KMfP-uoB3rKdh8KxrqViTndVo9ys_vUAbgG52o_kLD4U0I2K_Zw_JWIATKxccbj5mZ-5XbGauwklnSYq1Jp_gQ_AskLWJeA7q3c93K2ij6g70rryrdMPVVxm72vkYqHtmsK1GUshNKpnLbs6uQcrsFYqh_V-0CADWYnxLMszw_Ak5kn8s9PDGKVcavl_SipyG3FbciBTHBanRgRHvWh_zajrgf4MH-CnTrxuD_lVty4uDrek5bz2TT7p3YbOmIF1hbc527yfVyVnwZrLHctKC7oHUOz_h1AlwYdDn59Hu_WaKTBuZAXnb6SNBKYg6VYFDqLqVSakjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Drmnvez0vsNUos18f85qV1wrW96Rm3aRhlO6xbd1BurqzrOQdg59DIb3S5NJXgBo44Bl_MLYwI6mf9Miomi9uS1FMWnmS5pvnDJCVVHqfIr7Tu-grLa4jqKAGCIsp1gsiB4UIiHEB-ikEyqROXKYdqktgUII0Oa0xpPAA9K3ullafSRankDtue-12FAWgPkd3sTZMK_owrhbP3Dn7kpKbyuT5FemBHh0_36Wo7y5XisAGULHIqpX6MKD_rBPkEEwkwvcOw3cOieuMo4a8WPcYEHaTa_3QcqcLjOkVq2wM5bXFGqxEnLrNPz5YNNXMOVcLhoYRirR2pUFsmD8oddYTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=Drmnvez0vsNUos18f85qV1wrW96Rm3aRhlO6xbd1BurqzrOQdg59DIb3S5NJXgBo44Bl_MLYwI6mf9Miomi9uS1FMWnmS5pvnDJCVVHqfIr7Tu-grLa4jqKAGCIsp1gsiB4UIiHEB-ikEyqROXKYdqktgUII0Oa0xpPAA9K3ullafSRankDtue-12FAWgPkd3sTZMK_owrhbP3Dn7kpKbyuT5FemBHh0_36Wo7y5XisAGULHIqpX6MKD_rBPkEEwkwvcOw3cOieuMo4a8WPcYEHaTa_3QcqcLjOkVq2wM5bXFGqxEnLrNPz5YNNXMOVcLhoYRirR2pUFsmD8oddYTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LdkW3RUTtnBpJFjQjqZlv4BSwlXHi6MVZ6FvyG9FnrNuc_f7Xca9GovfmkcPVUDUs9nKei-F2xuyuiybZEpiAD34dQkA0JepS8_RdJsJnOWl4KG-WlduDdWCaM89b18UDRBcGffFZMdBbxFIhPxssdOzdmr27ey-XFvNDtMmV5wYuqjnwJiPNFLoR_mxLOdIKTiDvlGC07zULbc6DQVkEnioC1BE_llCHXQBqpKyd-TinoiPfMirlOQv1ZHKUoOqawEQu6cCzcCme_rZhelLyen27QhPAO1DvmkKp3Nvh8RVSoQBx7qdBXZAqcP4uxR9A7utHAkhupTB0OIvRrMGWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0wCn9HL7Ndbe36LsWo1SzXWeZkZLMOjBBKQR3MjJgpmN3pN5IoTNz3HKTvCzgTIerWU4vfPokZ7jOAlWpv0i7DMb6dZu0HU91UDpkdp75cKn1hGHXOfYMmqIBONfrFOmCEC6H2DLtUk4UDoOdqg8RFRwf4tldllkBdKAIn9QxcwoDKSC_qrxYPPqzdip0kk_yDhFMeXwvLcAwghUFLG8ifntrjeFAy3vvB8oGWaKhQfbl0IsD9ZtlqZnShZXQ5XXIQwnJFT6EfyGbGGd9k4GL0Es9jnu78zRWpRJfXAVvCJ7mgOHlwEEisVwzqh0G6hsFy5uVRG7xG-OJGknnPGbaU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=uxW10lYajjtidk1qzAGMdjh-Pdxrr8Lb-kkyNLlAhcGCnkM3IJVYDiGx4-bDQJjyNrSOFfS64fTGTMZAac5DPYzyW9q5LS6LJ0ckRP6EBeufKKvwfoXD-Pvi4UX5tISFkzPunfCOE41sQXiWCblU3hod8gVA5snp85ktRRsswI1uZslzVa47Gqopz69UxSuVPG3eMdgQl-PNSY0WK78z-F8pyqCnhe1QO-tyyAGhoZVF_mmKeQVNOfVIrgefuUfWlFCE2RpCS5LEfT_R8Z4uvhcvSrGMvY4lP1oaIKXxlx_rTOQjf9anqjp_4G_5zLmizfUWbPx0Uhm5odPXQS-uu0wCn9HL7Ndbe36LsWo1SzXWeZkZLMOjBBKQR3MjJgpmN3pN5IoTNz3HKTvCzgTIerWU4vfPokZ7jOAlWpv0i7DMb6dZu0HU91UDpkdp75cKn1hGHXOfYMmqIBONfrFOmCEC6H2DLtUk4UDoOdqg8RFRwf4tldllkBdKAIn9QxcwoDKSC_qrxYPPqzdip0kk_yDhFMeXwvLcAwghUFLG8ifntrjeFAy3vvB8oGWaKhQfbl0IsD9ZtlqZnShZXQ5XXIQwnJFT6EfyGbGGd9k4GL0Es9jnu78zRWpRJfXAVvCJ7mgOHlwEEisVwzqh0G6hsFy5uVRG7xG-OJGknnPGbaU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=N-4PM7LDjS6yzAJ11mpy7uzNfkg4VwxP9nNSd2qzmcYh4BAhzNxK2syEzzIgMLrdBhIs0kD-rpEx2iOoJhryL1anqbNI6OGTodiKhHSh_Fx2XOp6V-4JNt0Nd77cl6bnqR_X4AFWMYi3xZeF81YajRBujH5lLZc-jhca26j9lJxCsT3-dRlM5XQjqZxJtSGu51jjOUly2fs7CAQ7aAZGGjTqtKdrbQY5N03Rvj6JET_eRKfMvX2wicd9FMOnt1O21BXVfSLDVTDUZctKz3J5KXKqUU08dGApcSHioQAf1KcQ9Z2L6O0XvjlTMg_sF2f-jsPxD5qZfsfWIVNVF1BlFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=N-4PM7LDjS6yzAJ11mpy7uzNfkg4VwxP9nNSd2qzmcYh4BAhzNxK2syEzzIgMLrdBhIs0kD-rpEx2iOoJhryL1anqbNI6OGTodiKhHSh_Fx2XOp6V-4JNt0Nd77cl6bnqR_X4AFWMYi3xZeF81YajRBujH5lLZc-jhca26j9lJxCsT3-dRlM5XQjqZxJtSGu51jjOUly2fs7CAQ7aAZGGjTqtKdrbQY5N03Rvj6JET_eRKfMvX2wicd9FMOnt1O21BXVfSLDVTDUZctKz3J5KXKqUU08dGApcSHioQAf1KcQ9Z2L6O0XvjlTMg_sF2f-jsPxD5qZfsfWIVNVF1BlFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=dICtOyA0Y0aiP2XbhvdbxQoB3gmNlQy1pB0EdsLppK4LI1YEXTXP7IcHLn8YtZQtAjRnn_fWru6-Jgkw81_HoCDi8Hec16-8PAhYv5LGVxdwxYXLrJk9gSrJ7oaKrUgpZe-OyDAvKN50CiWzG_7dryKeCZMTRBwSOIFelTnMUGR7gRbndGXJx3HTYc4xIpBL1z7jhZyReaOZFMjSt79yrARJfTe102xAiBLXrGFIeBo-_3VEFhWzHW_MEr3obZIqNe7MaO6_g_6z-3ojW5elGjkI9uvNlI84qUutvMJDvYu8IPG7eHmb8dU0XcJ8rLy_O8FdT9GxOu5M4QYxtud4gjkSlP5Af9WJrc-vwFoJTYWt1divKpQiWM8CqlYtPcyC4KTbyRbr0YTtyDvhrq2T64pSfXyOqOUlu4zddZtoGLuubpXfvOFxrJFNRLnwKbnnXF7IJMr8swXHXAmoN1hVe9xlj8ND5SQ1yge666dzMECPD-wZtZSevY9yFgHSAJzYkImXl4ef64g1t21NKlMmiAPfvLNGNzQfslKr7i7rekEKUve_VsbhuB4zgh7W3l45jCd3TMG-VyQuGmKQ-Abe8gh5Bh9kJvscn78WwC_zhboMlKmKWuqDX79ZOelDVq-W9d3UqfQ3VCutq4J7D0zH1F3IYmCGagODo35wSBSYj9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=dICtOyA0Y0aiP2XbhvdbxQoB3gmNlQy1pB0EdsLppK4LI1YEXTXP7IcHLn8YtZQtAjRnn_fWru6-Jgkw81_HoCDi8Hec16-8PAhYv5LGVxdwxYXLrJk9gSrJ7oaKrUgpZe-OyDAvKN50CiWzG_7dryKeCZMTRBwSOIFelTnMUGR7gRbndGXJx3HTYc4xIpBL1z7jhZyReaOZFMjSt79yrARJfTe102xAiBLXrGFIeBo-_3VEFhWzHW_MEr3obZIqNe7MaO6_g_6z-3ojW5elGjkI9uvNlI84qUutvMJDvYu8IPG7eHmb8dU0XcJ8rLy_O8FdT9GxOu5M4QYxtud4gjkSlP5Af9WJrc-vwFoJTYWt1divKpQiWM8CqlYtPcyC4KTbyRbr0YTtyDvhrq2T64pSfXyOqOUlu4zddZtoGLuubpXfvOFxrJFNRLnwKbnnXF7IJMr8swXHXAmoN1hVe9xlj8ND5SQ1yge666dzMECPD-wZtZSevY9yFgHSAJzYkImXl4ef64g1t21NKlMmiAPfvLNGNzQfslKr7i7rekEKUve_VsbhuB4zgh7W3l45jCd3TMG-VyQuGmKQ-Abe8gh5Bh9kJvscn78WwC_zhboMlKmKWuqDX79ZOelDVq-W9d3UqfQ3VCutq4J7D0zH1F3IYmCGagODo35wSBSYj9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=LKwLk_Be4BjJcnfoy9AczzLShUU1RuVNm3c803KSP0BKHYzMQpgdiN2zUg6MSwwTwsbmmEXdkMF4mt4NUeZcTa1rHPivCL6GAIgFkIZUGjShLXqnP0eFOd5FhgUKRP-iSx4jWOQH3ksdSudTxsZN3Uva3zVLaCY8M_yq-CrZh_y51jJQLVbY2deezV7-zLaSK9FwNBj1VtZ5uOdjFS3Y6f5JLWOUFP7YEqoWGSyLFn-uXGSOjIeuwsCf06usgXf9--7aTXJLNr-T7uS8dyoI8wmkiKay2KYbqSSYV-jaZTqrSJMyFV7WrsRru23b-P58JO1OsmDKMtnfQY-7eGuSTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=LKwLk_Be4BjJcnfoy9AczzLShUU1RuVNm3c803KSP0BKHYzMQpgdiN2zUg6MSwwTwsbmmEXdkMF4mt4NUeZcTa1rHPivCL6GAIgFkIZUGjShLXqnP0eFOd5FhgUKRP-iSx4jWOQH3ksdSudTxsZN3Uva3zVLaCY8M_yq-CrZh_y51jJQLVbY2deezV7-zLaSK9FwNBj1VtZ5uOdjFS3Y6f5JLWOUFP7YEqoWGSyLFn-uXGSOjIeuwsCf06usgXf9--7aTXJLNr-T7uS8dyoI8wmkiKay2KYbqSSYV-jaZTqrSJMyFV7WrsRru23b-P58JO1OsmDKMtnfQY-7eGuSTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaUC0WQp798FjLMkhhejsf1-j40VL3AvumJX2rrSfCyNshrAnkzPlPm0u3d2_62Co3FRlG1P_s2jVqrZor5GvkX05CUAPj4oXXQ53o2yeZ5b-q-BmsGRfUnZtrHw-wEMUGQIFIjN0VHayPxI9pcIW9dpR1hOQFaiL_L4yqBJanXHrutuCh9Z28lVrWjcsm__tf0lg7OmNJuuWVAVQP_3UwcxpqGFN5L-TQ5uk93Q848tY-3RHCWVuN2ao3aH_l1CwOtKpDu0JLedPh_IPD8lyJO9HJmnR7UWjd4aQLnVx5JJdxShKFReY1alqJwAg5rVaHLElw9oM1Kzykx-wJgYWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=FJMYK9dTyg64YJ5qozh7VZBIWw8vjqhCmslzPweHhf9hp9ngd2aNDwa5cO4StiFDEU7Evo6IF-1-J5qvxDc3o3Jxkj-LQKppYWW-_3XTjJ7EQOGZAHJsbrACiU54WtFZv7wPOqMS9luPM-32MfaWSFEnlELr4ELys9A4kAoORhG815D5wV7feYBbPfYfs_40NNPNqt20O4_sg4HDqgsOkGrP7erPYDkZtL_H3kUd2-invXO4xVs0SuY4nbbRSonhgWFfrmFJEC_R9S3B3ZR2nBSvgp53zKUp7-bmWIxc6PzdQfBPE3hEbvQYQZhmQnhIh6omgzMhRAoycgwAePc2Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=FJMYK9dTyg64YJ5qozh7VZBIWw8vjqhCmslzPweHhf9hp9ngd2aNDwa5cO4StiFDEU7Evo6IF-1-J5qvxDc3o3Jxkj-LQKppYWW-_3XTjJ7EQOGZAHJsbrACiU54WtFZv7wPOqMS9luPM-32MfaWSFEnlELr4ELys9A4kAoORhG815D5wV7feYBbPfYfs_40NNPNqt20O4_sg4HDqgsOkGrP7erPYDkZtL_H3kUd2-invXO4xVs0SuY4nbbRSonhgWFfrmFJEC_R9S3B3ZR2nBSvgp53zKUp7-bmWIxc6PzdQfBPE3hEbvQYQZhmQnhIh6omgzMhRAoycgwAePc2Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=hPTxcYMYYIPZGILmYnB0AApLlG--TlpeXp40rRfUiVp69TU0U1aaZhJ_YCB_uUVqheDm0sADW8KNyb-7WItDgTtawj6GcZu7MC-M-kD55km3A5ljMkdA9qIPsaHJdQBXTcgfuzXSCYGCVleyvwt6LPUwd86bRaqUwuP2wTsrDnh9gUzEJR5RbcFddycbQ6vtujC6HKt3yhpGhZrYiWayluXJ8DHUFfI8D7hVF3ICsDGZzyQb0wKIXE-Q4cEnXY8GygREeEI8UD3wzVraxj9m9QCOSGyDYki0OQvgtzYkG0fbgTdP82tM09fepO22nuZBSCNNr8xXnBUKcy0ZeqwWH1b8qyiHyGDdY7iPTiNgfxQasJ4n0cjxsYUcrp0swO9lzcdMt0J5birTOTVNfBFvtjvF6H7rD-GdasyvLqS4ypQFMIO1Wh9XNLBFOAIwb2snED1DRhrcs5g3Th-zYdidotov4v4ak3qSn9IfOONxXESE906I15gUTy7SsyVGK-6ot0oCqRlIQ1IwW-AnuAl1dYd8IkglC3sD7alokYsJyL1a7XTFyFpwP3DlnxBLBC-j0irL6l774h9vJUEDJMdlcAQ4op4TTTH6j-uiUc_zsXeeZ43gz7XtCsKz3WilZsOKxjivj6_ki6J4CjoKhrbvmwSny8Gd8Q8XX-3JsHqbWYc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=hPTxcYMYYIPZGILmYnB0AApLlG--TlpeXp40rRfUiVp69TU0U1aaZhJ_YCB_uUVqheDm0sADW8KNyb-7WItDgTtawj6GcZu7MC-M-kD55km3A5ljMkdA9qIPsaHJdQBXTcgfuzXSCYGCVleyvwt6LPUwd86bRaqUwuP2wTsrDnh9gUzEJR5RbcFddycbQ6vtujC6HKt3yhpGhZrYiWayluXJ8DHUFfI8D7hVF3ICsDGZzyQb0wKIXE-Q4cEnXY8GygREeEI8UD3wzVraxj9m9QCOSGyDYki0OQvgtzYkG0fbgTdP82tM09fepO22nuZBSCNNr8xXnBUKcy0ZeqwWH1b8qyiHyGDdY7iPTiNgfxQasJ4n0cjxsYUcrp0swO9lzcdMt0J5birTOTVNfBFvtjvF6H7rD-GdasyvLqS4ypQFMIO1Wh9XNLBFOAIwb2snED1DRhrcs5g3Th-zYdidotov4v4ak3qSn9IfOONxXESE906I15gUTy7SsyVGK-6ot0oCqRlIQ1IwW-AnuAl1dYd8IkglC3sD7alokYsJyL1a7XTFyFpwP3DlnxBLBC-j0irL6l774h9vJUEDJMdlcAQ4op4TTTH6j-uiUc_zsXeeZ43gz7XtCsKz3WilZsOKxjivj6_ki6J4CjoKhrbvmwSny8Gd8Q8XX-3JsHqbWYc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BU4S7dxdVy4lJ-jsE9rZBz-OdFz6fj1qTB-SgqNnNJRCdTmYSn4dOwJ88KEJc-Ogfr7MUnJEQKNHiClXv9swvsrh3BLH15sOCREuWKV7tvyza-zPQSLFNE2uH1EDOELoIuQUIzN-a-qEDATEDyBn8egLeg9_6BMDWwOS_Iyfns98CPQX-4Qi5kzL4BxwpY7UjXo4m5YHH82l6rO9NIhBmcF8gOJgaLpkLq5E6WG1dcWvW2SRQHd99dexM4zQiSKX7q2d0fMp2kfE11btimXvgR3wSFdMCDabr8qvT7WQuoYn7u8EjX-dgQA47BTrcLq6ou7vwZvl2TZk6bRM5QcZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=jg6530hMdpUGPDsv-NNbjPZZdINIGS1KSxkGavSL9JZfifzynSTy3U59FlzqpzqD46i2hpEeVoi4spcfeuPufQXLU6TSHLJSicdhPs58IkEaEL1xac_E6o5ZCCliDA2Bxh2lYkkUvV9MMLI_CxuQBMiGJSsVekMs6JYlSvSUjTrYl6XCkAaGjZRPShIEQpyYhRGboj-a_cxudEljH8o99dMPoCocdg-5l0aFqWqtF1jPWyoSDmOJpr7vtjgsAEMByMMGXtY_5Dsmvuf9FQamIyYunv0YHaNXemerIOMtZSwkowY0o-CdVchdhXNp1hm0NTKX4mhQcx4Tzjof1twhKZm65DPafLEBy4RQL_Xc6RJNRQm-7DYYrV--XWra8UhS3YRuS7gk8luyU-S-XV9Zknvl5qTDeawEKaQwS2eOpGalypDAidAdE_dX3Y_8GlKt0pjmV3L0z_HNymQ2L9DXJkmrvCqtUY5ye_oVClpK7HkPy8J1fxSwMt6z_pRIL6UrPHodqhd4fLCST2_rMUYHkgDg2hHCEaL4KCTX9H2iJKjxDDUR4OYdgU-rshLsbAWf-ePXQ71w21DaPmIP0EpS8s90-KssnT_hoMlwDweElTa7-Qli0aEFltZXo7mFjUclFWSB0KbAZQNIAKuzxQ9P0dy1Hpnga8-TZnHpdEGl8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=jg6530hMdpUGPDsv-NNbjPZZdINIGS1KSxkGavSL9JZfifzynSTy3U59FlzqpzqD46i2hpEeVoi4spcfeuPufQXLU6TSHLJSicdhPs58IkEaEL1xac_E6o5ZCCliDA2Bxh2lYkkUvV9MMLI_CxuQBMiGJSsVekMs6JYlSvSUjTrYl6XCkAaGjZRPShIEQpyYhRGboj-a_cxudEljH8o99dMPoCocdg-5l0aFqWqtF1jPWyoSDmOJpr7vtjgsAEMByMMGXtY_5Dsmvuf9FQamIyYunv0YHaNXemerIOMtZSwkowY0o-CdVchdhXNp1hm0NTKX4mhQcx4Tzjof1twhKZm65DPafLEBy4RQL_Xc6RJNRQm-7DYYrV--XWra8UhS3YRuS7gk8luyU-S-XV9Zknvl5qTDeawEKaQwS2eOpGalypDAidAdE_dX3Y_8GlKt0pjmV3L0z_HNymQ2L9DXJkmrvCqtUY5ye_oVClpK7HkPy8J1fxSwMt6z_pRIL6UrPHodqhd4fLCST2_rMUYHkgDg2hHCEaL4KCTX9H2iJKjxDDUR4OYdgU-rshLsbAWf-ePXQ71w21DaPmIP0EpS8s90-KssnT_hoMlwDweElTa7-Qli0aEFltZXo7mFjUclFWSB0KbAZQNIAKuzxQ9P0dy1Hpnga8-TZnHpdEGl8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=WEcHlcl-i3Tqg-q9xndsdPCHr10C2Sn0akV2ZcBlS4J1CDbuvhWCb3hacxWyONUr0SOe2rc3tr0XyzGGtSevBaKw3xG_QLHjwwG-K70RBlHV7X_Zepy43SUlEL_tfJ0usc880nldC118Omn2LgutV3sgwS0hOPj2plyn6PXSH8BLvol9IGeWEO15qHTlJxNoDNAxaZt8nkjrTvxTWrGPg_GI4CW7ixhedhk_50UvmPI-jU3pHR8nsb4h0pAyaKwSZGhMiOi4DPVfJTY--sPkSw8gpkt_JYRwoVwfrhxqWvRtRfkZRACzzJJXth0GT5TeEno43o8z6819uGgu_b-xKbywp21uKsksbOfqZDLJuESGe-pafZfBIv_gzkUc0oO6_xYF3QMz0tgcw3YjdtP9cEez8Iyg0CorjSz0P9hj9x9W2L9OM8oV6ILZl8__gtisZYJwcSm6IYfsn7LX1wGoR7wBg49etxUhPZj3hoDjWLN_zr5g3NjmNKhmxXBLiMSUX-xEjvpBq9QjdqmTg4KfidVXRS11iRgF9ItpO-YyK73hkANxL3iDUTR89jzf4M_h5BbmiI25BkLAgvHh9I71XVHCkgvwiqKIOsmhXB_Cc4RYoD225ugsKiolQfspIuhL5vDh9zulli4G99192PGvfjKOlhu5cOk9DEXXl_lmk0I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=WEcHlcl-i3Tqg-q9xndsdPCHr10C2Sn0akV2ZcBlS4J1CDbuvhWCb3hacxWyONUr0SOe2rc3tr0XyzGGtSevBaKw3xG_QLHjwwG-K70RBlHV7X_Zepy43SUlEL_tfJ0usc880nldC118Omn2LgutV3sgwS0hOPj2plyn6PXSH8BLvol9IGeWEO15qHTlJxNoDNAxaZt8nkjrTvxTWrGPg_GI4CW7ixhedhk_50UvmPI-jU3pHR8nsb4h0pAyaKwSZGhMiOi4DPVfJTY--sPkSw8gpkt_JYRwoVwfrhxqWvRtRfkZRACzzJJXth0GT5TeEno43o8z6819uGgu_b-xKbywp21uKsksbOfqZDLJuESGe-pafZfBIv_gzkUc0oO6_xYF3QMz0tgcw3YjdtP9cEez8Iyg0CorjSz0P9hj9x9W2L9OM8oV6ILZl8__gtisZYJwcSm6IYfsn7LX1wGoR7wBg49etxUhPZj3hoDjWLN_zr5g3NjmNKhmxXBLiMSUX-xEjvpBq9QjdqmTg4KfidVXRS11iRgF9ItpO-YyK73hkANxL3iDUTR89jzf4M_h5BbmiI25BkLAgvHh9I71XVHCkgvwiqKIOsmhXB_Cc4RYoD225ugsKiolQfspIuhL5vDh9zulli4G99192PGvfjKOlhu5cOk9DEXXl_lmk0I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=BZK9V2AQ88nNLKM1MBu2CUTA_rmLPMwpwwVCsH29QpZ27s4fj4AIlFjVEqJ1ORvVdoP2RuA3E9POrpMmfv1u36Vj0I3-GSSPExyv-_mToR91hC7DJ-QoGJ-fvYIOdgQEqmt3HCRJ4GLN60QcBXX9svwDlYwUgshcYfPUnk7aevaHT1Kt1xxt5yvQbVQmLw-M7N5dWlhzI9P_ZoQ9lh9lXT_a7neI47KhLTJv8pYnsV4PSgP9KtC8bx7JElzQlWF5qd0sRpRbJclb_OzwQE2oZ7grfdE838MncSz7zgpVEe_s1UoOWJm4_c-pHY3Wq4KFfcGCxnXSRmLevHo5O3ozsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=BZK9V2AQ88nNLKM1MBu2CUTA_rmLPMwpwwVCsH29QpZ27s4fj4AIlFjVEqJ1ORvVdoP2RuA3E9POrpMmfv1u36Vj0I3-GSSPExyv-_mToR91hC7DJ-QoGJ-fvYIOdgQEqmt3HCRJ4GLN60QcBXX9svwDlYwUgshcYfPUnk7aevaHT1Kt1xxt5yvQbVQmLw-M7N5dWlhzI9P_ZoQ9lh9lXT_a7neI47KhLTJv8pYnsV4PSgP9KtC8bx7JElzQlWF5qd0sRpRbJclb_OzwQE2oZ7grfdE838MncSz7zgpVEe_s1UoOWJm4_c-pHY3Wq4KFfcGCxnXSRmLevHo5O3ozsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=DjDr7yrt5Ji923adqb2hM8vCbtM28-Tq_K-_Bwv0EChxtCR3-yBslnwS1Jp73KVThiVJnFk8Digx1IFZeDi2VnO5ZvIAnB6RzFvnd1uyrsIEUF-kZVABK5wH1c23Aj9_sIhJ8n_TjxgFQa6Hbt-_CMuRUxgpnJb7sPIxXRG3lxPikcfuxo0AfL84hfRxEJ2h4pUX3Gx_JpbxqBHP8Cgdi7RiQbuNGRFd5aHoaVqRPC_kSuL2T-R3IwkCL2c7An25HoH1F1dt5JHLTxV5R4bIevM-4tT82WbnGaUaGdNnW2-fNTqfcLvLSuIKCrWFfaqb3R4Gz6MxZsJY46EiXbGEJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=DjDr7yrt5Ji923adqb2hM8vCbtM28-Tq_K-_Bwv0EChxtCR3-yBslnwS1Jp73KVThiVJnFk8Digx1IFZeDi2VnO5ZvIAnB6RzFvnd1uyrsIEUF-kZVABK5wH1c23Aj9_sIhJ8n_TjxgFQa6Hbt-_CMuRUxgpnJb7sPIxXRG3lxPikcfuxo0AfL84hfRxEJ2h4pUX3Gx_JpbxqBHP8Cgdi7RiQbuNGRFd5aHoaVqRPC_kSuL2T-R3IwkCL2c7An25HoH1F1dt5JHLTxV5R4bIevM-4tT82WbnGaUaGdNnW2-fNTqfcLvLSuIKCrWFfaqb3R4Gz6MxZsJY46EiXbGEJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=J57zjUmgReEDVJBKqyUTEi6MtiXcWZeUuyEGGFFCmYYMfmh5CfiWy6966vi8X6tRQoMD5fhFtdTQjXKsmyntX4p873db7V-AAcatz3z6cQhTvq03rx6zI_ubJ-kFXFJl5Pk1EQbZHiYFnse4hheDlh-dGQwp3ezxsY9PcPyFiCn5RIwIaw0MnaW5cBgEi9g1iRK3rozxaDg7-iFLeX8w6Qze-p5ouKjeIw6vmidZGcFDz18cwVzq49TPfocPA4VETUT-klg7kcHf_6rnoXbPumb2wpGfOf7tcIl7efWQGH1KC4WZx3wSWzp_f1UXsLUMGIuQ8E6KGGUx0_BQ8w59Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=J57zjUmgReEDVJBKqyUTEi6MtiXcWZeUuyEGGFFCmYYMfmh5CfiWy6966vi8X6tRQoMD5fhFtdTQjXKsmyntX4p873db7V-AAcatz3z6cQhTvq03rx6zI_ubJ-kFXFJl5Pk1EQbZHiYFnse4hheDlh-dGQwp3ezxsY9PcPyFiCn5RIwIaw0MnaW5cBgEi9g1iRK3rozxaDg7-iFLeX8w6Qze-p5ouKjeIw6vmidZGcFDz18cwVzq49TPfocPA4VETUT-klg7kcHf_6rnoXbPumb2wpGfOf7tcIl7efWQGH1KC4WZx3wSWzp_f1UXsLUMGIuQ8E6KGGUx0_BQ8w59Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=LBClov9G6ZRSbGxSRc3oXwe5SiVavWh0Sxbl9DklIUbX0JkPJqMOJVy3ztQ8cZxOFICtO8cKWffRiMaV0nSX36EAhbAHorTZZkMX8T_L66XV-YvGww0i6N7JSw33BKBTfQecNoF-FjBcym6CcAgO1EnzLxhcXRNQNFhNt8S1bXIRmhgK57mlYYwoH_rsrig5T6Yi55-b2T9eg6dBYlIW8BbxW4Vx7Qra-ypk31OLAQ7jbp8pT4dHv98g0kqhwEsOmHyvuszjXHezsfNey9nxQV3a_V3QbqVh7KdLWli4GBVkencuKTmf-zCnR8V-ht-AtRtmBZdUzyeyyyBo1J6ZHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=LBClov9G6ZRSbGxSRc3oXwe5SiVavWh0Sxbl9DklIUbX0JkPJqMOJVy3ztQ8cZxOFICtO8cKWffRiMaV0nSX36EAhbAHorTZZkMX8T_L66XV-YvGww0i6N7JSw33BKBTfQecNoF-FjBcym6CcAgO1EnzLxhcXRNQNFhNt8S1bXIRmhgK57mlYYwoH_rsrig5T6Yi55-b2T9eg6dBYlIW8BbxW4Vx7Qra-ypk31OLAQ7jbp8pT4dHv98g0kqhwEsOmHyvuszjXHezsfNey9nxQV3a_V3QbqVh7KdLWli4GBVkencuKTmf-zCnR8V-ht-AtRtmBZdUzyeyyyBo1J6ZHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=LEVUi-byU_HlcNtpO_BHNAZYJxamkM64FhW0D9gShIKFVU9r84FJwIkjZfo5UXRaJiGNW7u70unNLodHx57DC14_hGEqYW_LcB3H4m-SqZUnj0r6ZtrLX_HjXnlGeMxF9wpU-gcE0aiDU7gVpsSQXP0CznwNiZL3vH_VJFZdj22dGgUt-ham08TNlm07p6prx1OseZvotbApk6l-ADjtGcECYbjx42Y1ox3-vv5Y8kSAm5CaAUr9O_khwRabJQHA3zNl2ZHvRMjO1AUopi8-N9W8rGIOOtCWeGHsaBFUVrJVEBv1kJXWqRypqG7DzM5tQMnlapPysLQ1yoYECWK6DQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=LEVUi-byU_HlcNtpO_BHNAZYJxamkM64FhW0D9gShIKFVU9r84FJwIkjZfo5UXRaJiGNW7u70unNLodHx57DC14_hGEqYW_LcB3H4m-SqZUnj0r6ZtrLX_HjXnlGeMxF9wpU-gcE0aiDU7gVpsSQXP0CznwNiZL3vH_VJFZdj22dGgUt-ham08TNlm07p6prx1OseZvotbApk6l-ADjtGcECYbjx42Y1ox3-vv5Y8kSAm5CaAUr9O_khwRabJQHA3zNl2ZHvRMjO1AUopi8-N9W8rGIOOtCWeGHsaBFUVrJVEBv1kJXWqRypqG7DzM5tQMnlapPysLQ1yoYECWK6DQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=EKy8S1ISR2nhc7n6AqZmI84deNuOT5982dDs2kzKROlUmtI0xgVB8ulzAbd8bGZgvMOdyZcos9O3cOHnx1b9-c7D6doHGGosE0QxRdwZP2PM_eB3BNRcy93xh8fVQYf4_xCMQcu-ofvXgtr2IXtTZJO51g9bpb5QjWA_efRAp8PDNA_YEsZ-PLbl9HXmufAP1ao7mGln2Zrz3r-5TL_-nkQTflSPv6LMadLXT4escCr6be2Eujtr8Fd4rVYdJFAgqgVVegp7wNXJ6osvHZMj_7T1rkB2iFoI7gl9A_JZe9iVJXSGVR5qchJAEYSpsEe4RY8Ad0xqyz4QhPDZDd5SlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=EKy8S1ISR2nhc7n6AqZmI84deNuOT5982dDs2kzKROlUmtI0xgVB8ulzAbd8bGZgvMOdyZcos9O3cOHnx1b9-c7D6doHGGosE0QxRdwZP2PM_eB3BNRcy93xh8fVQYf4_xCMQcu-ofvXgtr2IXtTZJO51g9bpb5QjWA_efRAp8PDNA_YEsZ-PLbl9HXmufAP1ao7mGln2Zrz3r-5TL_-nkQTflSPv6LMadLXT4escCr6be2Eujtr8Fd4rVYdJFAgqgVVegp7wNXJ6osvHZMj_7T1rkB2iFoI7gl9A_JZe9iVJXSGVR5qchJAEYSpsEe4RY8Ad0xqyz4QhPDZDd5SlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Tr-qdp0HqVNsoU7XqeiDQoLmu5AJ9uXUZTpUnJW96YjE2Lr7w7E5CJB-20y7aT2yzZohwXM9Hx4vPDc2Una_AO8E3-b9U37PVy2leRL0-eeeQnGAkeVfEHTwdlBHE1Awtfs7FPpZk4mxod5NmkrSKKjvPLp42FHIGieyJTicmfGSsus37hjIpREVPrQ7oPpuRgAjzQFGkIXoWKwWqZA07UO2aQf-fXQlrskdWR-sILuEr2LTb-GX9tRudh2miBfKKmcIY_or7fVadyuN2rdi2jGW6KX1wG50SV0l_2MQaJKAOHVfzOwf2HiO9E8jzkESuqjvhY9FJ-3IUaoviqFmfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=Tr-qdp0HqVNsoU7XqeiDQoLmu5AJ9uXUZTpUnJW96YjE2Lr7w7E5CJB-20y7aT2yzZohwXM9Hx4vPDc2Una_AO8E3-b9U37PVy2leRL0-eeeQnGAkeVfEHTwdlBHE1Awtfs7FPpZk4mxod5NmkrSKKjvPLp42FHIGieyJTicmfGSsus37hjIpREVPrQ7oPpuRgAjzQFGkIXoWKwWqZA07UO2aQf-fXQlrskdWR-sILuEr2LTb-GX9tRudh2miBfKKmcIY_or7fVadyuN2rdi2jGW6KX1wG50SV0l_2MQaJKAOHVfzOwf2HiO9E8jzkESuqjvhY9FJ-3IUaoviqFmfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT80pB0N4xDf-KxIn2LUHoOSiLO4A2BOVimPACwxCrJRPE6d5a7xwkmEL2CoCZywGSYnhD2ZYkA4jk0tdBEIwUCpihVYg-bsPIq4Y70xZAea3ov0WC2xpwXXa8c8DdM-HW7HO98UTD5wJ2JklmgWo6FK-xpIjMxg2CBJo9XsLw15Ir82Ms0pRNpNSh9ubg56c2STGN-Nr_11Cxs--0Pa0CYwZr4zwlWBW70TDPWGCKeBD0hNYHOTT6ULnYv0tZp8jlZ3OlY3rrFjiJQMLABEXwXK4uLmscagPyJOOKfUZH_m5AtijizAIamqoE6hEs0du_86R2X-3ZuWNwBQpxTAZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dVaTYeyLWOdj6QJySFJo8iaiddn5_G55g-QFLzos8nlyLT6irglf6nt1foiqaLA5G5MHwiNk7zhq368bdvcnpCiwTavejg-25a6cEVSmiSWuHiBlo1aHfuK7zBAOhbtyX_FixumUuHvEm-5oO115cj3jGy-O6Q20ooFTgyB2IG9CvDd3_Qf3DRD-sPofyeC7rjJ-fQTWpVQLk2teODL5a750oSmCvV06__8moIY8iTcFrzsC4nxkhSxSXNm6NvThgcqo7WrQcHob8D5-8h5KmlDeKYF0E8r5xLY7agEGUta1MtcedKcsWm1TGby-cprYk_YYBgjZXD1RlNzGd2soPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=dVaTYeyLWOdj6QJySFJo8iaiddn5_G55g-QFLzos8nlyLT6irglf6nt1foiqaLA5G5MHwiNk7zhq368bdvcnpCiwTavejg-25a6cEVSmiSWuHiBlo1aHfuK7zBAOhbtyX_FixumUuHvEm-5oO115cj3jGy-O6Q20ooFTgyB2IG9CvDd3_Qf3DRD-sPofyeC7rjJ-fQTWpVQLk2teODL5a750oSmCvV06__8moIY8iTcFrzsC4nxkhSxSXNm6NvThgcqo7WrQcHob8D5-8h5KmlDeKYF0E8r5xLY7agEGUta1MtcedKcsWm1TGby-cprYk_YYBgjZXD1RlNzGd2soPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=tSFLSWsLi588qf7sZIBC1ZftVXS4gWI1k3aqzb_if4MeFEnqVloC_2uqhGGXgxxNzsm0hAwxxCXZlGXYrqrRraZCZRhnOAMeLeVM_J7Ygoz2Lb_XTXeo4oMwuz6hwYJe1UM0IC8jFCYhlcSwwAVIgo_x_75I6FDHgf7E7q6fFeRGVIrvA8yBm6aBn1G2lH4zBtDuwrbTVyLVyWzscrD6iIdzuA44y72Dp6RGb_uNLMMiFch4nL6VqBqZZCdTwj3D5B3LfPFhPUXcSl0kURTlgZPgI9UvX94CAGUR6RKu7UVJrWuTyXcAtTkgdyt_3Y79O2WQWo0J-h_VxXzBXMmJ7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=tSFLSWsLi588qf7sZIBC1ZftVXS4gWI1k3aqzb_if4MeFEnqVloC_2uqhGGXgxxNzsm0hAwxxCXZlGXYrqrRraZCZRhnOAMeLeVM_J7Ygoz2Lb_XTXeo4oMwuz6hwYJe1UM0IC8jFCYhlcSwwAVIgo_x_75I6FDHgf7E7q6fFeRGVIrvA8yBm6aBn1G2lH4zBtDuwrbTVyLVyWzscrD6iIdzuA44y72Dp6RGb_uNLMMiFch4nL6VqBqZZCdTwj3D5B3LfPFhPUXcSl0kURTlgZPgI9UvX94CAGUR6RKu7UVJrWuTyXcAtTkgdyt_3Y79O2WQWo0J-h_VxXzBXMmJ7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=igBlQUrDLn5uCuO6DkxCPI8_8qBQfpU28sIjUfYe3BMVJWKNlHhPrmh7n2rrGNPE5F4SBy9Ku5GX6l8mMee0CBOChmnTleY655rUfvqiH9kVh7nNS3HTxOSWA3QzUpMt-SEUT2IsqPpqNmfswdZP_0MyWaAVWdBDaNZyaLniwOhhJv-wDpfllFgX3aL1NQZWBPR2y4KejvH_vloyoVlwa-glZvbTtmuQikW7wzpcskmT9Sli4maMz2Lc4lPiQ7KCoHIQI5jN0suUJ2HrbgExsgCts9l2rUemF7z_HqT1zlsjbi0RdLwexeNCgiaK_FIyEWoVnBTjRxsY4h4uclh9BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=igBlQUrDLn5uCuO6DkxCPI8_8qBQfpU28sIjUfYe3BMVJWKNlHhPrmh7n2rrGNPE5F4SBy9Ku5GX6l8mMee0CBOChmnTleY655rUfvqiH9kVh7nNS3HTxOSWA3QzUpMt-SEUT2IsqPpqNmfswdZP_0MyWaAVWdBDaNZyaLniwOhhJv-wDpfllFgX3aL1NQZWBPR2y4KejvH_vloyoVlwa-glZvbTtmuQikW7wzpcskmT9Sli4maMz2Lc4lPiQ7KCoHIQI5jN0suUJ2HrbgExsgCts9l2rUemF7z_HqT1zlsjbi0RdLwexeNCgiaK_FIyEWoVnBTjRxsY4h4uclh9BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=s8xVP2QZbH-9-g1D21DZOuAqh0B5ax6bgSWyEs-7TeEITR_F35vKVU06GiXKlS6sj-RhlZI_QHKKZ9KA0vCOtGM_k8D9dRG91T3-Qxi6On-eNFFFdm446M0pNt_emx9UW0JG8w8NjdyKz1--c18YpdbWFCWZ8y09hO8NHJhDPGP_-7Xekg5rBCIoE5Wdw1ynIEIepHg0yQ6KH82bmbd34KCoN2yC_oHu8AE_HOR0zGaWMxUob9GhgRpuErSH4vbCuJIVLmsPkWwHO0ha6PiaOnED_2Pk9ZgFsldrtlC_wxG0clY2Z4Y6OukeVy2ngnp0ISWEfaHkaAyfz5jSjq8oqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=s8xVP2QZbH-9-g1D21DZOuAqh0B5ax6bgSWyEs-7TeEITR_F35vKVU06GiXKlS6sj-RhlZI_QHKKZ9KA0vCOtGM_k8D9dRG91T3-Qxi6On-eNFFFdm446M0pNt_emx9UW0JG8w8NjdyKz1--c18YpdbWFCWZ8y09hO8NHJhDPGP_-7Xekg5rBCIoE5Wdw1ynIEIepHg0yQ6KH82bmbd34KCoN2yC_oHu8AE_HOR0zGaWMxUob9GhgRpuErSH4vbCuJIVLmsPkWwHO0ha6PiaOnED_2Pk9ZgFsldrtlC_wxG0clY2Z4Y6OukeVy2ngnp0ISWEfaHkaAyfz5jSjq8oqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DT1ViZ-Ar3WrfoPSrTBC31nrRu2ILdP9ZygQ1uLbmyX-7aYjUcAIO0zwbx19x9R_Kjfs7zvWzO-GRlkhbYSZ-LgliZOVJMZuaaTRsUv1C8qQthq3R81v_3HVgwPA-2FQ_wCCtoYwhXtkSSmaVhltl7Ew5XHVBxWADbhq7-u8uWrndjTh-PhVhmvVC1lCuRYfAcj3POVeXEkxDfj1Ep4lm6ba-rmsJA0sMDT-UwGubTvFEV0C4ZHnyZ-QlCovi_P0F9Aisr08Xq6mR2bJ1cVcLxqcZUqSX6E_GG2mzvaOMk-XyCcqtge_D1GL2m_pf3NbGjPH-kZaTKm8U6BcxMLfRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=NUlhZMFs9bkwsVIaIFH-WtlscQr_AvEIsu28qiWDuHCbmfN15xj3usMvd8NtBBChrA9zNxUwjqzHYg7xIYJl0DkxM2xWq9psX2I-0PMGOjIeRSuo1f2P1fX52W1mWWdETJYtQh1_1vZOIlKhqzOnKb6YCekf7QgcQ0HfcSLdvcnbaiMK0cJKSm5PB7jv7A5b0Jikmk2UTOKKFEjDpbuHd9j9I5oXPvJ6EVcjbxo4uOPKfuJy2FJaUwWOOcBNG4nE0Cf_rO150oDbDz8u4_bra_YK_44nugQwaQ0gPOEDafD01uN32aNuU4yjGjkGU6A8LsY1b3H1wZv0AkUKm9RpfjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=NUlhZMFs9bkwsVIaIFH-WtlscQr_AvEIsu28qiWDuHCbmfN15xj3usMvd8NtBBChrA9zNxUwjqzHYg7xIYJl0DkxM2xWq9psX2I-0PMGOjIeRSuo1f2P1fX52W1mWWdETJYtQh1_1vZOIlKhqzOnKb6YCekf7QgcQ0HfcSLdvcnbaiMK0cJKSm5PB7jv7A5b0Jikmk2UTOKKFEjDpbuHd9j9I5oXPvJ6EVcjbxo4uOPKfuJy2FJaUwWOOcBNG4nE0Cf_rO150oDbDz8u4_bra_YK_44nugQwaQ0gPOEDafD01uN32aNuU4yjGjkGU6A8LsY1b3H1wZv0AkUKm9RpfjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=uF6c-jStKjPqt7_8zz3IK6ODC8o-LiV26nlxumkhyScRxPwTqtIrhd5cP5BiFmxBWI_vuZfPosg-dr6X4OThITyCqEx_ll6cRpd5u60Rd4yaCxGpsx-1alZziAfDtckt9X6C39z6RyPvHpVbvjRDC0xWYsDrbM5FxqGNBE-8vVFnMFCSN6M_CzFiKE6nvoDLIB-z-9Qy6S-sW2eLOJLnYeSqVkieVk5Cc070KO_vlwBEMdy4_oRH-6XU0Zcc_2ZwxAoU_0LKJCuvWLyOQqYmMRtIyckq15ygR159Z9xvEfT8JB9Gj-Svbp8f4vjY4RVF6EDGUjA0ZD7JG2zkpL4TQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=uF6c-jStKjPqt7_8zz3IK6ODC8o-LiV26nlxumkhyScRxPwTqtIrhd5cP5BiFmxBWI_vuZfPosg-dr6X4OThITyCqEx_ll6cRpd5u60Rd4yaCxGpsx-1alZziAfDtckt9X6C39z6RyPvHpVbvjRDC0xWYsDrbM5FxqGNBE-8vVFnMFCSN6M_CzFiKE6nvoDLIB-z-9Qy6S-sW2eLOJLnYeSqVkieVk5Cc070KO_vlwBEMdy4_oRH-6XU0Zcc_2ZwxAoU_0LKJCuvWLyOQqYmMRtIyckq15ygR159Z9xvEfT8JB9Gj-Svbp8f4vjY4RVF6EDGUjA0ZD7JG2zkpL4TQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Azc68vEMs3RKdcmj0uhdSK0gJEvgvh9ousvPyimOUgW9AJKhk5Xc4clAHhICLCShpifp2IMPjp17Ck5I4wvvyJKp5jkM2J-gVz_rx42LEycbeQaxbo8BCbEH8dze7Z5rWMStOKMXP8GVysCH47ZcPCM8V5KqEEc3SduRtiSNfYHxKNzkb0Y0OQnrcntKulp5Jy36WxI-t6Kifgmf-xL611Y3DsIEl3GH2pJE0hnxc03NkAjov_pyTCTYWLLNJrXbJK9OA8ROI-UUtS5qX6-pHTce3HqdbJNTN-d2hQGtqxCmdjPl_j4_x-iN4pT4Rq2NFH8sA0vuuDMMVrTRIF66MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eB-RXS0bUqxjOrSAxnkE7CO8cgj_U4YvLBBaxnopdv9sMMrzxYJlFvCQ9N3gwuEN-fzh2kF7c3Equ_y1MZmArF3kFd_WtH1w-Ty400b3N_uB8uA0EzcclWq0Palvjd17PcarULFex6wtTdqL8bL5-JfUcYf7m4Huav11g-h_pSLyqYdW83jOAnBHB41AgYQ4SHcICyrcl4EMSApiipnZMj1dbsk84OSdjyJ4sf41LMwRLKhsB__qsMtf_ckIbS_t9CS2RAA6HuaxWO3zetREsYlGLZgnI9PVurMGf0MqP59RMsH4zK0B-Gm_1ItbqX592DT8BODsI2aAMFBGA-hP3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=QTHmRqKWJsibCdD4YApyPhNS2A20LGuiZVHBGlkazLUaFutfygCqMvtmDX4hAPoH8Q7mWRyYrdagk7uyPzZV0DeTQeovmAF1FMojpEHGNajgTY3JdFjNa3eRsY98YLUr2B322EjIhvKw8VzI3q0IErcTak-RiNj-qFS5NEQCbNGyJqIbQqkviRuw3u5SQVjdnyGpJUjZkhIgD1k0eeNoJSxUE5i2E3KDc3CPU7xm5wb_gUik9X1alNjdUNOuRH8l0vx1yhHbmL2SO79pIti-qUfM3jkT-bu1xlH3ILV--1XOSlj4cMKJM3Z_bZWA1eCbU2A4YTCIzwzBvYy_zUy6RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=QTHmRqKWJsibCdD4YApyPhNS2A20LGuiZVHBGlkazLUaFutfygCqMvtmDX4hAPoH8Q7mWRyYrdagk7uyPzZV0DeTQeovmAF1FMojpEHGNajgTY3JdFjNa3eRsY98YLUr2B322EjIhvKw8VzI3q0IErcTak-RiNj-qFS5NEQCbNGyJqIbQqkviRuw3u5SQVjdnyGpJUjZkhIgD1k0eeNoJSxUE5i2E3KDc3CPU7xm5wb_gUik9X1alNjdUNOuRH8l0vx1yhHbmL2SO79pIti-qUfM3jkT-bu1xlH3ILV--1XOSlj4cMKJM3Z_bZWA1eCbU2A4YTCIzwzBvYy_zUy6RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ck6XIpjtokhw0Tjso8VMTR1RfFLiu_Gxn26Mqj0JNb7cIEnj30zItkSDD14hPirSFKISoWlbLUGJ8IaDvCuzTBKPjoRyzKaE2ZQOURqfTaHycpQIdA6R3AUvOZ7QhIuvaGt1LEt8E1gpbmaMSqmYl1ff3Gv2sA6i9qysI-XZAVC84ScDDGb0DAimv4mUeLrSUpTBOYgUm3Ump-skN3Szbh30A7VMXcGAaXDEyc-CCemLUy380kqiPAHQqd2r-XtyW0KYDL5yb1tKpS1mITGScHkvt_ZYi_aAUwgNLqSTZjqkuf2MVPTHs-WZwtQw4pnVUV3fG5c1R-9IievbwUIobw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JZiD4S3uzEuYQ2A-8kb9ngyWv-NsAIDYjiPZBQhgqD1e9hmKye-uhf-crinGZSumiWF872xCdaRCp-3R43rmBJH8Zj4ANDYov8AErpObqBbKtz2sM4bodAWx4EuQ8H_cbI1YG6z84KCceeE99hdIAJciF8-iaGqaS4r2phty6gezho-bAxymTU3NuOzqxWrO00RMOZbtdybmX1TrlRkfIaGT97dCL4Bky5g0fqKqlC_ImF9dkclxPiJBOAoV4T4kQ_g5AB9YwJHOZxtwD19psLHsh1wh0F1RlOH3YrkCor_SuAPMzeUa-jyKa1ixxIhO_QBsUIIyff_rD9mpAlGhMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
