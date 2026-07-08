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
<img src="https://cdn4.telesco.pe/file/M1FT8c7QyAppcfNGFAocN76S4whyyv0zNJNkUqbnCB8EDfv_lTkjnybNV7U87FsLeEHzMLqev9P7gd3mUxL-NXox7mHQNvZbv6_4uKcSv5BWeRYoRmeB-ZdUmqgBBS50bOfj1Nldj_RMu-dn61AgwFqGXJVIKnjiLXjXfoYvZQtkHVsBIMuH8PX8Uko8slLtqa-kvhrhcvZ9o9OYBwY6gV2j1W9zDQdIKQ_a3e_MmB_kZmCPnMdZS-qZZssxXIavVBHUM5RgCQJfLUgS0pYOMIYtmZZ7F6OY578STl-l_-o-M7prEerRbXq5bL7xTkd_UXZuMWYW-WUD7QLUzVDVBA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.48M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-17 22:46:24</div>
<hr>

<div class="tg-post" id="msg-668647">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd4066b49a.mp4?token=pfSWkWsQaTx7POFC9C3gXjJhOaIZWNG-Ph13TaBsR3Zz9l0-r2kGqi-B6pSXVy3drnEYTKOc7Hy42dw7GschioDdhux_4pMeFuvQiJHHxK7DWdncYqn3Wv_e8zWNrWJzfieS1JEo0bHPCwzkMvpVOc7CTVeCQtrapogEoPAMXa42ILMyCygotFHYjIZ6RSjEmlpehHK9jLD1C4J6tzPHhlYMPffTCHgtnAFFj6stiG0kpMjT-o5OdBz0Bm0EhO2LCkrjViWpwvc4hCWsC7p7m7naKxs3RO4Ib-8F6VVY6pPJKIzRbh8tvBtq6kjfH2MA-P1jHYAgxUta7HCaSA0lYywD9u6ovtU4kAJGq8bRfhdmqCHWZzQPTKXj3bblKbLvONzNcZx-hHTqlVN_EjgHJRcrhRbVlNeLRI9szq3yCHLFuXHVmw2C8iKeGFHpZtSfp-RrAseVAQ7rqUEsqPHqyvmcDaetb-JBSpeNiJeP5bqngA2jaX2pJoxCUM7Av_AuojXtfizXaEmQhwGf62CemjN1MDTL0T11TtoSAZiLGH_q36WIrGX8BftJS9QcX66AN5nD698xP1DUAUOcTmZ20bDd6Ir3EPdyHq72wmpsYw6DzYNK5bg88eU95ufiyDGzvdsif7frILj0mKlqkhY5j6VX_Y2SViYPNi0VCl5LUCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd4066b49a.mp4?token=pfSWkWsQaTx7POFC9C3gXjJhOaIZWNG-Ph13TaBsR3Zz9l0-r2kGqi-B6pSXVy3drnEYTKOc7Hy42dw7GschioDdhux_4pMeFuvQiJHHxK7DWdncYqn3Wv_e8zWNrWJzfieS1JEo0bHPCwzkMvpVOc7CTVeCQtrapogEoPAMXa42ILMyCygotFHYjIZ6RSjEmlpehHK9jLD1C4J6tzPHhlYMPffTCHgtnAFFj6stiG0kpMjT-o5OdBz0Bm0EhO2LCkrjViWpwvc4hCWsC7p7m7naKxs3RO4Ib-8F6VVY6pPJKIzRbh8tvBtq6kjfH2MA-P1jHYAgxUta7HCaSA0lYywD9u6ovtU4kAJGq8bRfhdmqCHWZzQPTKXj3bblKbLvONzNcZx-hHTqlVN_EjgHJRcrhRbVlNeLRI9szq3yCHLFuXHVmw2C8iKeGFHpZtSfp-RrAseVAQ7rqUEsqPHqyvmcDaetb-JBSpeNiJeP5bqngA2jaX2pJoxCUM7Av_AuojXtfizXaEmQhwGf62CemjN1MDTL0T11TtoSAZiLGH_q36WIrGX8BftJS9QcX66AN5nD698xP1DUAUOcTmZ20bDd6Ir3EPdyHq72wmpsYw6DzYNK5bg88eU95ufiyDGzvdsif7frILj0mKlqkhY5j6VX_Y2SViYPNi0VCl5LUCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر هوایی از مراسم حزب‌الله برای رهبر آزادی‌خواهان جهان انقلاب در ضاحیه بیروت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/akhbarefori/668647" target="_blank">📅 22:44 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668646">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pEqTLgl8PIlWZosGEaLh5YJDr_Uju1PHNg13aXxc29Ipyk6xNdTkdzPF0ma-MSN429CGz60nYe1tRxTCM01N3aLt75RtApzQRXxapt98C73aSeFoAl0kw84IgY4xv-OwtTdCLb3VJVxc35RaOE-KKJ-m2it_BAqflHN6OWPKdHPhJ9-1PWprz52-NkDbrXG2t_m1y4Wz5BWc4KcbjKzsbZFfs5IGxRGYbQ816VnAr85RK_fpOPdvtkF-7rLV2qx_Bfx8weQWPqrE02o2HecZTAOjZlPvnhzpth-TnsWl6jvrhpKmOquCIeqC0TqOZ5-qou3N-QPf7Kv_KqnI7Aev1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ابراهیم رضایی: در دفاع از امنیت ملت بزرگ ایران خط قرمزی نداریم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/akhbarefori/668646" target="_blank">📅 22:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668645">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RA_ldXul1fWanxgDlHy3SpRFtCSKHKSyK7sFFMatj_FTRlNHbmI7DyAV8xn4awmSK5jmT4IjuXuIj9xUzObaTY0HiRqcVkFaIcTY4OQ0dB94lr1Vaqx3FJk8MCjIEKuWZpEFPObhzk8ZSdLIV46iff-5amgFdFSsUUKLDZool-NW91tsKrzje15znmKfn3cbXzMyQ8u9bkZw67Pt5nz2yZxNQqCoVBkQYTpFjKdb0a6iOZzL0KE516uT_nAsZLMiPEV8nc2eRbme4fWIpwNaoSSfQ0zJW1EKL-aeKN-U5jks5gtPfEjFDCoVtfy6LRMl9_8sLgA-MBkXQ3aI67dMfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شاهد کابوس همیشگی تو هستیم
#تقاص_خواهید_داد
#WillPayThePrice
#خونخواهی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/akhbarefori/668645" target="_blank">📅 22:40 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668644">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G-KQ54Dvv96X5N14cB4wbwKRND1T449ywJDcANVQiLFmo5T0X5WEDo0nRFENK6uK06eRpwtySkJ9L8mmDs4KldzRpw2BPVpDcGrZHi7pJ8Rl-76Q7SZ-yPlcpm7VzZE54DcgnFBXacy0BknwU34lNYw1SpZ6k_3lB2qNZMGxm7bo6LhX0Kpu9U9tjs_UGC4r36AQqfk3YQgrwz-q120z4fCI9r5QHME4LBPWc32pvWT0m-e0yawiIKHle3msbD7MdNMA-IDwn9IDF7fdOfa4MZ1WItrui4d1j8rvaJmw1zWX6NhdNWloU-PQqSr1tQNROtswBkcniSTX2qp9UaJeKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دستخط عاشقانه رهبر شهید انقلاب در وصف امام حسین علیه‌السلام
بنفسى انت، بروحى انت، بِمُهجَةِ قلبى انت...
🔹
بسم الله الرّحمن الرّحیم
این حسین کیست که عالم همه دیوانه‌ى اوست‌
این چه شمعی است که جانها همه پروانه‌ى اوست‌
اى شعله‌ى فروزان، اى فروغ تابان، اى گرمابخش دلهاى خلایق!
🔹
تو کیستى با این شکوه و جلال، با این شیرینى و دلنشینى، با این هیبت و اقتدار، با این‌همه لشکر دل‌به‌همراه، با غلغله‌ى فرشتگان که در کنار موکب تو با آدمیان رقابت میکنند؟
🔹
تو کیستى اى نور خدا، اى نداى حقیقت، اى فرقان، و اى سفینةالنجاة؟ چه کرده‌ئى در راه خدایت که پاداش آن خدائى‌شدنِ هر آن چیزى است که به تو نسبت میرساند؟
🔹
بنفسى انت، بروحى انت، بِمُهجَةِ قلبى انت، و سلام الله علیکَ یومَ وُلِدتَ و یوم اُستُشهِدتَ مظلوماً و یوم تُبعَثُ فاخِراً و مَفخَراً. ۹۳/۲/۲۹
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/akhbarefori/668644" target="_blank">📅 22:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668643">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a8484cb22b.mp4?token=J9_HXxl5Lbq9o_TcFJucAt9JWFPRWIn-OWAUy8gOC_PX_eX2LzNO2ryX3APXM9qKYRvWa7L-YTnN-CNujt7q8AAlni0h7tbDT9ndpbpm08aF92t37YtI88ru_je2z8RnesmERUFhWXvjhV-Rz3rFDaZQafLTx4WHrfeNY2mNtqMnu8G3bpKMlJy7VOR5VDnDlhrGkRcbGR_njQcFAkg2Aupoy93-H6CJBbWcZGmiqGf5tUS-2b8OTTIlvDXSQ9W7gI5o165SP_cfcUm4fU0CxWGaA9dpzwpvjCmAsMMuZZDShFihTs1_6jFokTLxXoCb-E5mz_aq4NJeTwAcb1tzpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a8484cb22b.mp4?token=J9_HXxl5Lbq9o_TcFJucAt9JWFPRWIn-OWAUy8gOC_PX_eX2LzNO2ryX3APXM9qKYRvWa7L-YTnN-CNujt7q8AAlni0h7tbDT9ndpbpm08aF92t37YtI88ru_je2z8RnesmERUFhWXvjhV-Rz3rFDaZQafLTx4WHrfeNY2mNtqMnu8G3bpKMlJy7VOR5VDnDlhrGkRcbGR_njQcFAkg2Aupoy93-H6CJBbWcZGmiqGf5tUS-2b8OTTIlvDXSQ9W7gI5o165SP_cfcUm4fU0CxWGaA9dpzwpvjCmAsMMuZZDShFihTs1_6jFokTLxXoCb-E5mz_aq4NJeTwAcb1tzpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جامانده
🔹
رهبر شهید، دل‌های مردم ایران را در امتداد یک عهد و یک آرمان به هم پیوند زده است.
🔹
اگر از حضور در این بدرقه باشکوه بازمانده‌اید، صدای دل خود را با ما همراه کنید؛ و اگر توفیق حضور دارید، به نیابت از آنان که چشم‌انتظار مانده‌اند، گام بردارید.
🔸
ویس خود را برای ما ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/akhbarefori/668643" target="_blank">📅 22:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668642">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/a8HLA7eEPHJQyx74BHVDyYirE0y-zBXiplvAKUvorQb4gXY-g3qoXspUHMq6LklZNQIKwL58SrTayUSXDPkMA5BxCE2HPqEleJNIj6g-2jMiNcq0n6Ge_APUwzR5jmiFa0_xpIBzSCf76k3fuUMxznTwiYXLjOV674rJVl0XaheCbdKiKwiUf4oQ2ld3cWMXmboFz8_uGiRY0qr1_ujg9RhhufPu6qVsu8BvRcK_nL2Tk7q7KkgRuFkja56uJB68x2qXmfZK-eqtaM-05FjQ8t1BZd0EgvTsJNa4FcURnFz43PmPUoJykzCIVZGGbST7JhF3Lo-8Ah-KbenCI9EPSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
پست جدید امیر قلعه‌نویی: کاش بعد از گل شجاع، همون لحظه زمان متوقف می‌شد و شادی مردم هیچ‌ وقت تموم نمی‌شد
🔹
کاش اون چند سانت آفساید نبود یا توپ‌هایی که به تیر خورد، گل می‌شد تا مردم ایران صعود رو جشن بگیرن.
🔹
این تیم واقعاً لیاقت صعود داشت. تو اوج جنگ، با وجود نگرانی برای خانواده‌ها و سختی مسیر، هیچ‌کس کم نیاورد و همه برای ایران جنگیدن.
🔹
جنگ، تعطیلی لیگ، لغو بازی‌های دوستانه، مشکلات ویزا و دردسرهای دیگه باعث شد اون تیمی که ساخته بودیم، آماده نباشه. اینا بهونه نیست؛ فقط می‌خوام مردم بدونن این تیم چه سختی‌هایی کشید.
🔹
آخرش فقط نتیجه روی تابلو موند، اما پشت اون نتیجه ماه‌ها زحمت و ازخودگذشتگی بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/akhbarefori/668642" target="_blank">📅 22:30 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668641">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JLU3LKQKYedbvMrLeSi7VIu0VAfG7VjuquhfwEUzu1mvQ6NT8DSNadoexAYim-rFyb2CXWlXH6kKRznMDzM7Y0n2T1KJoAl78kFAp79iALdAmWYwwQ3kRs_t_36UWhMYJn7u0397hKoQG9eVp6mlUr-mJTnlni3QvpS1TdT1NDHV1vZNTx3O3Tc1zOZysdvq6Kc4FlJgII4pbF38klWt76cCa5FGZXok59sQYt1Bb1dVzOqz2xRrLsX7oBpMusHnJ5d2AAJATkWikDkTFVqQ8yLmdu9XsnTrobC817foj2G9eBrYIP4g8CQwmU7Ck9TcOM4L7XczZHk-XjlaBjQG3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معرفی مستند: ضیاء‌الدین
🔹
ضیاءالدین، مستندی متفاوت و شنیدنی است که با روایتی صمیمی، بخش‌هایی کمتر گفته‌شده از کودکی و جوانی رهبر انقلاب را از دریچه انس عمیق با قرآن به تصویر می‌کشد از علاقه به قرائت و تفسیر تا نقش‌آفرینی در ترویج فرهنگ قرآنی. اثری الهام‌بخش،…</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/668641" target="_blank">📅 22:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668640">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b611e737b.mp4?token=of0VXM8WDrjLMrcRrSLhMUKpdFATu4XDE5iEJ80nNq5zNb8a8lnaP1MScIgs4wq9H_8yowQlGQusQ9rhdxysb5m2R627mVLePBeTs7viwC0qDCoVbTs_2OfaIrvOIKwhHs6uI2R_rUfbNrsu9GjWdZcNy8tOu7x2Cqfb-O-N2VsgVqHMv7F29yTfhTknbttuevp2CGmC4rfydkj1za35BV6s9iR3jnBh89ZFmu_rKrfRXiRQ9C9KvPcIzaz6w653KmQjH6OiNjYUztU1ih8jqa-KLGhKcISvN-OVpMxiE3kBWglL78R9QV6vFrMXWQNei9gGN8MzqD2lBMB9dm-YbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b611e737b.mp4?token=of0VXM8WDrjLMrcRrSLhMUKpdFATu4XDE5iEJ80nNq5zNb8a8lnaP1MScIgs4wq9H_8yowQlGQusQ9rhdxysb5m2R627mVLePBeTs7viwC0qDCoVbTs_2OfaIrvOIKwhHs6uI2R_rUfbNrsu9GjWdZcNy8tOu7x2Cqfb-O-N2VsgVqHMv7F29yTfhTknbttuevp2CGmC4rfydkj1za35BV6s9iR3jnBh89ZFmu_rKrfRXiRQ9C9KvPcIzaz6w653KmQjH6OiNjYUztU1ih8jqa-KLGhKcISvN-OVpMxiE3kBWglL78R9QV6vFrMXWQNei9gGN8MzqD2lBMB9dm-YbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بین‌الحرمین همچنان چشم‌انتظار پیکر مطهر امام شهید
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/akhbarefori/668640" target="_blank">📅 22:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668639">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zy8gPTmuVEzKUTWgOnGYP1hbSAob5gnTc7DJzKGNw4YGvthMlHpfTVPgc8aCq5RbtG9DnQpJjkB-A6-0s6hH5XdvVogckXttM-pIE94mxVEAXCC9Z_3m3zmOt512NICSIZtWQFmSFW7f32Kudgx5_nNY445_kZJyZVl7JXJsfkRBNc62NphF8stncTATnw46KKIUHrHK6PcEGUVK1y1eNNEoTThsDVLZ3IiuJRhIs9dPUQwifukL6ZzJuLzrrl6pJvqq9PPpogLk1k7VmUeaClWCswhWUWU2rcK-l5f0Rwf4azX2G65eaANO31d5mpCymrE9odSq33NWBglha4r15A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
در مسیر بدرقه پیکر مطهر، خدمت تنها در کلام معنا نمی‌یابد؛ در هر قطره آب، هر المان، هر درخت آراسته و هر گامی که برای آسایش مردم برداشته شد، احترام به عزت این بدرقه جاری بود
🔹
سازمان پارک‌ها و فضای سبز نیز با تمام توان، سهم خود را در خدمت‌رسانی ایفا کرد تا مسیر تشییع، شایسته حضور مردم قدرشناس و یاد شهیدان باشد؛ خدمتی بی‌ادعا، اما ماندگار.
#پارکها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/668639" target="_blank">📅 22:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668638">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f95cccf4d4.mp4?token=ZtyV4vI_5dZQlQzHcVuQIsDLlNS30fEVJmpsyiWaHBZIgA8EUAawRuURvPgmH83jHdqBPt9UN98KKw_J8wgr33a_cGoQDfMNpeBggWZnBt72kSCPMW-qKhj6P17uE0Z7-j6s8Wq0NUQ6T2Davdh-hXBqKJfd_4clh_BsXScO4-9aHCNBJSWCstB7eIKrOMskjzqxD5Hj_73I7yQD2J-v5FwAR208ntzr0w2B8bHlddsDSAHzEgcyFf7I0FMZY8iro9JKt1ycHSiylC-XA7gGyi3ItKUgO4gX488Ho0tIOif-PHliBMD41_bv5bBNSujffrh3U_dN52BOKbGFvM7MWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f95cccf4d4.mp4?token=ZtyV4vI_5dZQlQzHcVuQIsDLlNS30fEVJmpsyiWaHBZIgA8EUAawRuURvPgmH83jHdqBPt9UN98KKw_J8wgr33a_cGoQDfMNpeBggWZnBt72kSCPMW-qKhj6P17uE0Z7-j6s8Wq0NUQ6T2Davdh-hXBqKJfd_4clh_BsXScO4-9aHCNBJSWCstB7eIKrOMskjzqxD5Hj_73I7yQD2J-v5FwAR208ntzr0w2B8bHlddsDSAHzEgcyFf7I0FMZY8iro9JKt1ycHSiylC-XA7gGyi3ItKUgO4gX488Ho0tIOif-PHliBMD41_bv5bBNSujffrh3U_dN52BOKbGFvM7MWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نمایی از جمعیت حاضر در اطراف خودروی حامل پیکر مطهر رهبر شهید انقلاب در کربلای معلی
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668638" target="_blank">📅 22:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668637">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">♦️
معاون رئیس‌جمهور آمریکا: اقدام نظامی آمریکا ادامه خواهد یافت مگر آنکه ایران از شلیک به کشتی‌ها دست بکشد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/akhbarefori/668637" target="_blank">📅 22:22 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668636">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sihIFx5VdPTfB6Xwsn4j2h19qgYNoHDc8AJVZZy1DwsbAWX7VW4OtjborhP_CSqYqAu44fgBwLodyesIAgNibI6a5WQpi4LD70_X3HnR6yLCKQ8mPf5zSQNPN2O4PUNnuBBfW5spE-c5jc3AaDUMOi3y7DLklO20Ik1TdTGrrIF-Jy3hLqd3c7jwoXN1Deci8hdjMCx_-Fd87i8VD8ytgKrkEnVWqFjSH250eIr38LuwQkmVhqvbM0ocYZt4fESKgfExV5sPNGlkvIGD0A2ljATnvQx6-TXisac3mIrS0ceV9hAJ0ru8FAYxQ_9VCVi9WTj5BWe_5MbmSALWQHUgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
معشوق به سامان شد
🔹
پس از روزهایی که میلیون‌ها دلداده، چشم‌انتظار واپسین وداع بودند، امروز پیکر رهبر شهید انقلاب بر دوش سیل خروشان عزاداران در نجف اشرف، از جوار حرم مطهر امیرالمؤمنین(ع) تشییع شد. آیینی که با اقامه نماز و حضور پرشور زائران، مردم عراق و دوستداران مقاومت، صحنه‌ای ماندگار از عشق، وفاداری و پیوند عمیق ملت‌های منطقه با آرمان‌های جهاد و ایثار را رقم زد. نجف امروز تنها میزبان یک تشییع نبود؛ منزلگاه آخرین دیدار معشوقی بود که تا آستان مولایش بدرقه شد. گویی همه سال‌های مجاهدت، غربت و استقامت، در سایه گنبد علوی به آرامش رسید و این سرباز خستگی‌ناپذیر، پس از عمری خدمت و ایستادگی، سرانجام از کنار مولای خویش امیرالمؤمنین(ع) بدرقه شد.
🔹
هشتصدوچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/akhbarefori/668636" target="_blank">📅 22:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668635">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
العربیه: فرمانده ارتش پاکستان با مقامات ایرانی تماس گرفته است تا از تشدید تنش‌ها جلوگیری کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/668635" target="_blank">📅 22:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668633">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kEeMHXfCRgx9UUbQ4gllft-lbr02NWsTzKX1lBu9TdRs_mJJasW-zO5F9ufcQ68Qel_qPuQGDPpebz_tZgxFK6js46tDDVief6LRGkpg7751R8HJc03Boro4rrTwzZhVzTnqSlpbY6ldxnKNn0lTM4hLJ-Hmi8XkcY9VD55bBDCHqsxpnsMX1PA1CCXuDFc0CzRHfYC7C6A5-DLEQe9dC5k3uRMi2ySV5F4u-47Cn7K1qrse0NnirjdP4UavvejhJO1a9itNp_kqsv4MnXf0CQNBqEdDfnNqyhDCpKc-kXS0KalTm0CdkHDNxGoVxsgb8v6m9w7Vpr6gWKW4MrdNYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jg5I49FLIFB1mRlE9NwL2FsaDQHnFbial_IXJw0LXUpnQl2IoTiREJUWnzz9uH5Mkf6B2PPyrJjMVXgLD1qdi0W7m1-__rpRhQ3V5q_ouPXrlrxHlInhJ1cJnHEfkJDk6gnKiHgYmt641VuivZMiWgLmVQo5cPhyk3tf-BrhoBGsjsAfSLoowfPAjdD4gzMFXEahSV8dzHbtBLR6xbi8OR0PhAOM8sAUb3r1crrSUHtxbsWtrxsXGTP3AW0VyUlff8htp2OJoXWTNwd--lHfhKJp_R2eXG74E3v6Y8OGTtaZjGSakyCQCq7jkWTDLmGyW179WVCN70uqIAZ7WudfqA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
فرماندهان مقاومت در یک قاب و در کنار هم
🔹
تصاویری از سردار قاآنی و حاج ابو الاء الولائی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/akhbarefori/668633" target="_blank">📅 22:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668632">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">♦️
جانشین رئیس پلیس راهور: از ساعت ۲۲ امشب، محدودیت‌های تردد در خیابان‌های اطراف حرم مطهر رضوی اعمال می‌شود
🔹
محورهای ورودی به شهر مشهد با ترافیک سنگین مواجه است و پیش‌بینی می‌شود تا ساعاتی دیگر بر حجم ترافیک افزوده شود.
🔹
برای هر خودرویی که وارد شهر مشهد شود، پیامکی حاوی آدرس پارکینگ تعیین‌‌شده ارسال خواهد شد.
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/akhbarefori/668632" target="_blank">📅 22:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668631">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f71242ec26.mp4?token=joqf8ZhscSEoSgn9UGmrc8i7bS4wpVxOrJF5KVnhs7_QcNh7_grM390IfTljEB8rJfWxe1L-gRt3d0FirnV39HklMelerBt5ZiOoxphXPiCD2VfkpSpB2ZxuzFBhJpfPiu0ONbEv4zOFlFJ-arNIz-weD0M4Ar8qrlzImQT9LBKEucgUK4s4AmU0FV5VTGZ1fIdkjg9FLFh3njMysCfYKo7y5mIoGko-7JVGmGeKNngu9cG5fOBIFcVTnT4YISgXCtlVt8-AOw30aMEFbsATHqmwVCcp6uF31kRSlcyMXpfnUGCRkpwdQXxpgsOVC7Db9F1E30bDF9TRIS6CrQvPUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f71242ec26.mp4?token=joqf8ZhscSEoSgn9UGmrc8i7bS4wpVxOrJF5KVnhs7_QcNh7_grM390IfTljEB8rJfWxe1L-gRt3d0FirnV39HklMelerBt5ZiOoxphXPiCD2VfkpSpB2ZxuzFBhJpfPiu0ONbEv4zOFlFJ-arNIz-weD0M4Ar8qrlzImQT9LBKEucgUK4s4AmU0FV5VTGZ1fIdkjg9FLFh3njMysCfYKo7y5mIoGko-7JVGmGeKNngu9cG5fOBIFcVTnT4YISgXCtlVt8-AOw30aMEFbsATHqmwVCcp6uF31kRSlcyMXpfnUGCRkpwdQXxpgsOVC7Db9F1E30bDF9TRIS6CrQvPUjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حسینی بوشهری، نایب رییس مجلس خبرگان رهبری در
#گفتگو
با خبرفوری: مردم واقعا در سراسر کشور و شهرهایی که تشییع در آنها انجام شد سنگ تمام گذاشتند و الان هم در نجف و کربلا شاهد حضور گسترده مردم هستیم. مردم کل جهان امیدوار شدند که می‌شود در مقابل یک ابرقدرت ایستاد
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/akhbarefori/668631" target="_blank">📅 22:08 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668630">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/549c90c39d.mp4?token=s_TOaJpE9-FpzdsPQCBWUnudKs-A4_awdTyMWL5lCZbXjGJ69H0hhnZ4mqrjZ3ijNkcKvV-fjxHmrhlthI4XD2zbbkLmSv_77Bibn13wEY3zA6UFIzucVYtxvZQxuAqn5jzIsF51YovJf0DjIyjsJoL_wRG3z_rxdvHEqyAw7WuahW3hOyeZ6y1Bu1UbHOjwoPusv-xNCGDPovxcqK2apsE0PYiFmB2K5wysskg3WUiK4b5mN2nZQO4LoGGoxfau1gJnnYqEG55NGs1Q_4WJZV8vOitaGkNsbAXv5Oxonror-RcaceX1yDd2T5pVQ_C2ajO3BBZZcf4oWciwsei2Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/549c90c39d.mp4?token=s_TOaJpE9-FpzdsPQCBWUnudKs-A4_awdTyMWL5lCZbXjGJ69H0hhnZ4mqrjZ3ijNkcKvV-fjxHmrhlthI4XD2zbbkLmSv_77Bibn13wEY3zA6UFIzucVYtxvZQxuAqn5jzIsF51YovJf0DjIyjsJoL_wRG3z_rxdvHEqyAw7WuahW3hOyeZ6y1Bu1UbHOjwoPusv-xNCGDPovxcqK2apsE0PYiFmB2K5wysskg3WUiK4b5mN2nZQO4LoGGoxfau1gJnnYqEG55NGs1Q_4WJZV8vOitaGkNsbAXv5Oxonror-RcaceX1yDd2T5pVQ_C2ajO3BBZZcf4oWciwsei2Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعارهای ضد استکباری زائران در حرم امام حسین(ع)
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668630" target="_blank">📅 22:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668629">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/vuWaUMbzwAnXVn3HYy82S_TURrQdAjgxmxg_vvaJUbH26fp8BsUQvIu6RQgqoc_BsXHgY7Hx0YZuuYVdq8DBCO3BtoT0b6Tt6Jd4BgtwZLd6rD4Oyfp5NFrSEd6vuZpFT4bX_A3h-ZIfz4isu_2-422gy24XHxMdsFMU5CiqjFBC5hOhqMIsf5UNLN_CuigLdHhl8baawbNRj0RVgqS1zNhQzyiUbkaeogMyZR6-h9hiXBdAgHekg3QyfeSbUM__th3KAujXYWDk95uvpE9T0-SqKoAV12gdZ6VDXWS52mP0LsMvAK6U90joMUdFtjpF9se468Xbq1ZlEbV9g363pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بانوی مشهد؛ روایت‌گر بزرگ‌ترین بدرقه تاریخ
هر شاخه گل، یک سلام...
هر قدم، یک بیعت...
هر بانو، یک پرچم وفاداری و خونخواهی...
🔹
از همه بانوان ولایتمدار مشهد دعوت می‌گردد تا به رسم بانوان نوغان با حضوری باشکوه ، در پویش عظیم «گلباران پیکر مطهر رهبر شهید ایران» شرکت کرده و برگ زرین دیگری از وفاداری زنان این سرزمین را رقم بزنند.
🔹
پویش بزرگ بانوان مشهدی
«هر بانو، یک شاخه گل»
مراسم گلباران پیکر مطهر رهبر شهید ایران
آیت‌الله العظمی سید علی خامنه‌ای
و خانواده معظم ایشان
🔹
زمان: پنجشنبه ۱۸ تیرماه، ساعت ۶ صبح
(با توجه به ازدحام، پس از نماز صبح از منزل حرکت فرمایید.)
🔹
مکان: امام رضا ۷۴ ـ محل آغاز مراسم تشییع
توصیه‌های مهم:
• احتمال تغییر زمان یا چند ساعت انتظار وجود دارد؛ همراهی و صبوری، بخشی از شکوه این حضور خواهد بود.
• برای حضور به‌موقع، حرکت پس از نماز صبح توصیه می‌شود.
• همراه داشتن بطری آب، زیرانداز،لقمه سبک و شاخه گل پیشنهاد می‌شود.
مشهد، با حضور بانوان‌اش، فصل دیگری از وفاداری را خواهد نوشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668629" target="_blank">📅 22:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668628">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e1d1b87ab.mp4?token=TIWHAMb1wtSrIvLxCQtMfWBklM125BI1WruZrRitY2Qg14R0CM4MBO6h2_m0n-bgU21z8v9_PH68IeymTOltFJhJIz4OdOD9LLgmvlACy2sSLdmnTh3SQ5tHs6aonlgcBOS2YclmJgTzJZHnjgjh3VHyOtpsDJcGPIAcjLLOrPxME4oeitwWd0dEEVUmwYUgprDFbD9QARo_dQ7RuAEHzzDhPKULY9CXW5-iyREIUgE4cmtBg-Ym4DZ5Do48mJjWoQ1HdoTyZ20wv7cIYoPeH2SNH3biBU8xunFxBxpQNzlS5Q8TdtFaMpve8O-FwdZViOdxJwX_liY_RzU8YVRfcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e1d1b87ab.mp4?token=TIWHAMb1wtSrIvLxCQtMfWBklM125BI1WruZrRitY2Qg14R0CM4MBO6h2_m0n-bgU21z8v9_PH68IeymTOltFJhJIz4OdOD9LLgmvlACy2sSLdmnTh3SQ5tHs6aonlgcBOS2YclmJgTzJZHnjgjh3VHyOtpsDJcGPIAcjLLOrPxME4oeitwWd0dEEVUmwYUgprDFbD9QARo_dQ7RuAEHzzDhPKULY9CXW5-iyREIUgE4cmtBg-Ym4DZ5Do48mJjWoQ1HdoTyZ20wv7cIYoPeH2SNH3biBU8xunFxBxpQNzlS5Q8TdtFaMpve8O-FwdZViOdxJwX_liY_RzU8YVRfcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انبوه مردم مشهد از حالا به استقبال مراسم تشییع فردا در حرم رضوی می‌روند
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668628" target="_blank">📅 22:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668627">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b818cc85ea.mp4?token=QrQvBG_GdAUXDAXx0Nbf8TbAy420vfCEBZIzRU1-m4drDuGa2CSnrsNqbe5vJekf4puN3VB3OwdAhtFK0oJseO03x8XYVYrz7Kg47TBag54-QvMYSdNvvE8UtNhGsvfGKvS9eZkKlhUfNM2Vl8BMi3f_VLwJFem5aUfyJvRFOkoJjwN-De7JDDOZrfgaIDGIB22FDTc-uhg6Scr6KYwHcwN5LWBs4MVhzl_Gs4OP3IRXzOkTFPlbjbLsfG51JLzmUoShKdOjyl2fCNWEWInQRDWBGeqOrxjs43meDWQMhVCRX8By4UJI4GBzGVAzPDsQ74m6cZT8Ri-bpMvr5_4NcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b818cc85ea.mp4?token=QrQvBG_GdAUXDAXx0Nbf8TbAy420vfCEBZIzRU1-m4drDuGa2CSnrsNqbe5vJekf4puN3VB3OwdAhtFK0oJseO03x8XYVYrz7Kg47TBag54-QvMYSdNvvE8UtNhGsvfGKvS9eZkKlhUfNM2Vl8BMi3f_VLwJFem5aUfyJvRFOkoJjwN-De7JDDOZrfgaIDGIB22FDTc-uhg6Scr6KYwHcwN5LWBs4MVhzl_Gs4OP3IRXzOkTFPlbjbLsfG51JLzmUoShKdOjyl2fCNWEWInQRDWBGeqOrxjs43meDWQMhVCRX8By4UJI4GBzGVAzPDsQ74m6cZT8Ri-bpMvr5_4NcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام پهپاد MQ9 در بامداد ۱۷ تیر ۱۴۰۵ توسط سامانه‌ی نوین پدافند نیروی هوافضای سپاه در حوالی خورموج استان بوشهر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/akhbarefori/668627" target="_blank">📅 21:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668626">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
رویترز به نقل از یک مقام ارشد در دولت آمریکا: به رهبران کنگره اطلاع داده شده است که دولت تصمیم گرفته است سوریه را از فهرست کشورهایی که حامی تروریسم هستند، حذف کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/668626" target="_blank">📅 21:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668625">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">♦️
خبرگزاری رسمی عراق: مراسم تشییع پیکر رهبر آزادی‌خواهان جهان در کربلاء آغاز شد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/668625" target="_blank">📅 21:51 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668624">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/leBvJ327v1cSN7ZGV-O8CSebVM7SNLYqyIA2vdIBxXYdEid_xHf0ZqoqanqVQnbdWvhiSZFFcLkjcKOnKzcYz2lY7WhmpH6-HkTk-clSYhic2A-FXXbhw8krVd_inG03NAKD5Mj9zIuU3boQz-et-YgQOioU5pXGTLGG1S1aeTmPLbSljrNH995ne-CbXcrw64ADLZUcIwq3dy40JshjbLLTx0Jepe1Ci-oPCwsiVmT60qTJQ_PDLpBbF-oxZWZ60jbIEW8w0t6ORnMI8dhTXAn79bgz1wtWeQYIf9MBb_QOgo4-53xBAoo9nUmYKn-3iGS-m6Atq0SV-WdSxnXAoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#باید_برخاست
#اینفوگرافی
راهنمای خدمات مراسم تشییع قائد امت
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668624" target="_blank">📅 21:47 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668623">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l8fmBHRrS44a39pViKojjig57nV0t3GvIWFjziXDpZq8oVtq9G1qFGwMRYaYvSev2w_W0d1xOCIcAMY-mLpoO_wfV6M6KIT0mAHPAfJiZwVUPXQ6UEF5ZphKEmX4sjZV5smytCGX0M1fJbKJncS3hPCYKKimsdvVUpY6GVqBbeC81ykAlq4WqHkWudnmQnpIhnBDgmQuaPWPkVB_rthnOlVD2-Rx1uv1jVJ7xa6v9qmX9sNE_6HuGtgoCxpTnFwQMeWIEg2wSBq4QqKSQSjpMaLZLZLsDxd7JKNzYqetpNW3KeZWfBlwM7U6W1l2EZSPIPscJJ7jx1gRbelu9aIUTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: حقیقتاً باید به حال مردم آمریکا با این رئیس‌جمهور کم‌خردشان تاسف خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/668623" target="_blank">📅 21:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668622">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf80ccd738.mp4?token=QHAx1RuEMIdrUQD51Ejx8CssgNn2jEqnn8q8QMDVOs7iBYT2tQnB898W1ypyKcMBde1iL6muA4WIepUU-tKOsJjWSoQsaHtWCdlE6MSImXSoGD31XtUU3Cg68ZSRYf2x11ttQIuzoB6c07wGr40LbYUgEz4LqZMeIMRnNht2b5mas4v2gYPrglrC6ogNamzfv754CIhiVSUuzjblHD5M_nIwnVp6kFrmAGiMYzbe4_QZ87HdSeyqipfxGk4hHm_pODQOv_UBDSwgcu49Q8LV_5E1uNUlcCsRpwOxLYPr7oWjY3VbqHtXn7VvgPqgLb8gy_fWIc_fQL9YpUXPXH_jlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf80ccd738.mp4?token=QHAx1RuEMIdrUQD51Ejx8CssgNn2jEqnn8q8QMDVOs7iBYT2tQnB898W1ypyKcMBde1iL6muA4WIepUU-tKOsJjWSoQsaHtWCdlE6MSImXSoGD31XtUU3Cg68ZSRYf2x11ttQIuzoB6c07wGr40LbYUgEz4LqZMeIMRnNht2b5mas4v2gYPrglrC6ogNamzfv754CIhiVSUuzjblHD5M_nIwnVp6kFrmAGiMYzbe4_QZ87HdSeyqipfxGk4hHm_pODQOv_UBDSwgcu49Q8LV_5E1uNUlcCsRpwOxLYPr7oWjY3VbqHtXn7VvgPqgLb8gy_fWIc_fQL9YpUXPXH_jlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویر خبرفوری از حضور سردار قاآنی در حرم حضرت سیدالشهدا علیه السلام
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668622" target="_blank">📅 21:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668621">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/cGfkHbIJ6_a03jHVjOrI0GuJnPM19FSre-RFJpzIq9hp7QfXjYz8G1QLa-KKnbJdCrPnXE5YUOAv8ehWg9Nn-Ja7ouL2kmDuAA8hlB6HWjmdFAOjwGJvb-XEZe3TRI4_q8BnsHyQSae07L10noXOHXF5Q8pOm_fA26f81e2Wjk9RbmDSTt9CUIEcdJzIJppnPcolmsBRwGnJzWtAn-quW6w7FOMoINUJPYQTEErKcGSiS4UqbhKSI-4sk8MwcNULuOvWN23T_iFeERYg4HphtXkzYXLfKojZRqIZzKfcyW2QIi-SmhASWOz-MyDWCsrmnrlrosM5SIRHeB93yAbobQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خدمات رایگان و شبانه‌روزی مترو و اتوبوسرانی مشهد برای عزاداران، زائران و مجاوران
🔹
محمدرضا قلندرشریف، شهردار مشهد مقدس، از ارائه خدمات رایگان و شبانه‌روزی ناوگان حمل‌ونقل عمومی این کلان‌شهر همزمان با مراسم وداع خبر داد.
🔹
شهردار مشهد افزود: به‌منظور تکریم عزاداران، زائران و مجاوران و تسهیل تردد شرکت‌کنندگان در مراسم،کلیه خطوط ناوگان اتوبوسرانی و متروی مشهد تا ۱۹ تیرماه به‌صورت شبانه‌روزی خدمت‌رسانی خواهد کرد و خدمات این ناوگان تا پایان روز شنبه ۲۰ تیرماه به‌صورت کاملاً رایگان ارائه می‌شود.
🔹
قلندرشریف تأکید کرد: هدف از اجرای این طرح، تسهیل رفت‌وآمد عزاداران و زائران و ارائه خدمات شایسته در ایام برگزاری مراسم است و تمامی بخش‌های مرتبط با حداکثر توان در خدمت شهروندان خواهند بود.
🔹
شهردار مشهد تأکید کرد: در صورت نیاز و با توجه به شرایط و میزان استقبال شهروندان، ارائه خدمات رایگان ناوگان اتوبوسرانی پس از روز جمعه نیز ادامه خواهد داشت تا روند خدمت‌رسانی بدون وقفه انجام شود.
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/668621" target="_blank">📅 21:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668620">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
خبرگزاری رسمی اسرائیل: اسرائیل در آماده‌باش کامل است/ ترامپ و نتانیاهو حرف زدند
سازمان پخش اسرائیل:
🔹
نتانیاهو و ترامپ در مورد تنش‌ها با ایران گفتگوی مستقیم داشتند. ایالات متحده در ساعات اخیر اعزام مجدد هواپیماهای سوخت‌رسانی به اسرائیل و خاورمیانه را آغاز کرده است.
🔹
اسرائیل در حالت آماده‌باش کامل است و رئیس ستاد ارتش با مقامات ارشد ارتش گفتگوهایی داشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/668620" target="_blank">📅 21:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668619">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUKR6o7AEzpPiyGP9O4gcwVC04g7RIiFtNZUOx2JCypAfpcOUBl2BsK1PTclrGI4PTx28r7tD3x1W5fYxcqcuttACq79oT01hczpi2sHLrUOyNI8LpGR9YGiOAdx8v9od8V0LoPll8lyiIN_3R2t29cY0S4sOC5KAwlKXK7EHUOHj0eq6kaLk1Wo1r2SfDS43_AtrF6CvbaVT1TuxKCUUGfmWiBOxbHQzEC7IRwQ7esUN2O82vUeyofhHTeNYVJgdmIBBXMnHIcQXcbQ0YHOBPTAlvYXOUfa5gGHpa4sm2Za0Pz-jP_1LMMEulwameu5K5QTGjm4-7mOLx1zURGRqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آغاز دور جدید جنگ های ایران و آمریکا/ تفاهم اسلام آباد مرد؛ منتظر «جنگ بزرگ» باشیم؟
🔹
دونالد ترامپ، رئیس جمهور آمریکا، در اظهارات اخیرش گفته که دیگر به آتش بس با ایران پایبند نیست و حملاتی را به ایران ترتیب داده و می دهد. این واقعیت نشان از این دارد که باید خود را برای دور جدیدی از درگیری ها آماده کنیم.
گزارش خبرفوری را اینجا بخوانید و‌نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3228841</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/668619" target="_blank">📅 21:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668618">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
خوک نحس، پس از پایان اجلاس ناتو، ترکیه را ترک کرد
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/668618" target="_blank">📅 21:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668617">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
پیش‌بینی می‌شود که مراسم تشییع پیکر رهبر انقلاب در بین‌الحرمین در حدود ۳ ساعت با تاخیر برگزار شود
🔹
در حال حاضر بیش از ۴ ساعت و نیم است که پیکر رهبر شهیدمان در مبادی ورودی شهر کربلا در حال تشییع و وداع است و هنوز بدلیل ازدحام جمعیت و حضور میلیونی مردم عراق به بین‌الحرمین نرسیده است و در فاصله ۲ کیلومتری بین‌الحرمین قرار دارد.
🔹
پس از ورود پیکر رهبر انقلاب به بین‌الحرمین در حرم امام حسین (ع) و حضرت ابوالفضل (ع) طواف داده می‌شود و قرار است پرچم امام حسین (ع) بر روی پیکر قرار بگیرد و تشییع شود و پس از اجرای برنامه در حرم پیکر رهبر انقلاب به نجف و پس از آن به کشورمان منتقل می‌شود./ صداوسیما
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668617" target="_blank">📅 21:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668615">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/432b3d5d28.mp4?token=DHOTyq8BOqvJHiBCpESNTky3gbY9QFrt--7jdTd3bfP28mDmFtJJbeknwjZf_0DNIaUeHVY3Iw0IRgKSaldXQqIeK9vmNrUNlVQZKtMNnoGpmkstQvbMSjWVVRCSN3eVHL4Vv9BI0FSGvqqi8hUbNPdmatcc-YTTL-vtiJiZ-179pKZxdJQyK-Glt8zm-c7KqKDkjkgeNbhyucsbUEvthqX4k5mqpR5YyftZTGe3OnW2xHabG5L639ghhTiXchS_ckRGxSdI24dsNlkubTckFSu3HsK5mnai7VrII4WFpWomcoWGs9HrwNS_digOt2aV6_AkObOm6zie9PFp2UZiMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/432b3d5d28.mp4?token=DHOTyq8BOqvJHiBCpESNTky3gbY9QFrt--7jdTd3bfP28mDmFtJJbeknwjZf_0DNIaUeHVY3Iw0IRgKSaldXQqIeK9vmNrUNlVQZKtMNnoGpmkstQvbMSjWVVRCSN3eVHL4Vv9BI0FSGvqqi8hUbNPdmatcc-YTTL-vtiJiZ-179pKZxdJQyK-Glt8zm-c7KqKDkjkgeNbhyucsbUEvthqX4k5mqpR5YyftZTGe3OnW2xHabG5L639ghhTiXchS_ckRGxSdI24dsNlkubTckFSu3HsK5mnai7VrII4WFpWomcoWGs9HrwNS_digOt2aV6_AkObOm6zie9PFp2UZiMoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور غلامعلی حداد عادل و علی باقری و برخی دیگر از مقامات و چهره‌های سیاسی کشور در حرم حضرت سیدالشهدا علیه‌السلام قبل از مراسم تشییع رهبر شهید انقلاب
/ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668615" target="_blank">📅 21:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668614">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3eb9ead4df.mp4?token=nN-nUrCxfBMad9Af2NTrgplJsgB475WF-gnnrnscqTUZ9vKPgaNj1mOjV9rqkEe0xXrS7owMsjnKGZw2ntwawExDiW2xjjPgFrh_TzJwKluWknNP1u-Hw86KVD4S4qFH1bqjShjpYSMWlnMw62mpqdfNjHtsIGgXfqDRnZC_mfqHNMtBPuq2_uO4AF0HngZ_Xr2N5hshTgmvLur6rxxIUIGmYZ_ZzL1uzszDz1WEyU8isHjK1uX3ZlDj8AqZRmmohy3gGKD3jmHhQahEuYdXZTcIVfugwXuvsDkX3eHV6XvwH2X8z0dOjUnEeDXEbsXbeSnO1RUf2ziKrM2tlwd06g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3eb9ead4df.mp4?token=nN-nUrCxfBMad9Af2NTrgplJsgB475WF-gnnrnscqTUZ9vKPgaNj1mOjV9rqkEe0xXrS7owMsjnKGZw2ntwawExDiW2xjjPgFrh_TzJwKluWknNP1u-Hw86KVD4S4qFH1bqjShjpYSMWlnMw62mpqdfNjHtsIGgXfqDRnZC_mfqHNMtBPuq2_uO4AF0HngZ_Xr2N5hshTgmvLur6rxxIUIGmYZ_ZzL1uzszDz1WEyU8isHjK1uX3ZlDj8AqZRmmohy3gGKD3jmHhQahEuYdXZTcIVfugwXuvsDkX3eHV6XvwH2X8z0dOjUnEeDXEbsXbeSnO1RUf2ziKrM2tlwd06g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حداد عادل در گفتگو با خبرفوری: این تشییع بی‌نظیر مقدمه‌ای برای آینده‌ای روشن است
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/668614" target="_blank">📅 21:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668613">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtegFQqdQhUWNBAHGXiat16ILwJ7j8qSE1DFYPqMXsgAZ3TTfktiut18oD4w97kjT3G22dpA8K-xyQ7F9sCEsXn03OKJuFszLCr_qLN60LdEppksZT8_NwSlkJuv57pDLKcg624U5iU5OGB7hV0Z-qK1UWcFiO-vpRzcSStU949JKIsNO9DVxpuWRshVMuHFElq_PIqwLb2GnyN_HfF3wzkuvb6Fd6SN6WOrJ90ox5iZnIZHGpAH1LD_Iz7VyvffDohKSXrTdpu-74TYitZ9LNG_4BjbIO7kJ8Q0DuGIwg3XS3__dDcxb5OkQF1Ui5b_L5pH5faSIYEsDuXkylhoQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شگفت مانده‌ام از بامداد روز وداع
که برنخاست قیامت چو بی‌تو بنشستم
💔
🏴
مراسم عزاداری شام غریبان قائد امت و شب شهادت امام سجاد(ع)
▪️
با کلام : حجت الاسلام برمایی
▪️
با حضور : دکتر سعید عزیزی
▪️
با شعرخوانی : محمد رسولی
▪️
با نوای: حاج سید رضا نریمانی و کربلایی علی اکبر حائری
▪️
با اجرای :  امیر مهدی باقری
📅
پنجشنبه ۱۸ تیرماه
⏰
ساعت ۲۲:۳۰
📍
مشهد مقدس، میدان احمدآباد
◾️
حضور شما، موجب شکوه بیشتر این محفل عزاداری و معنوی‌تر شدن مجلس سوگواری اهل‌بیت(ع) خواهد شد.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668613" target="_blank">📅 21:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668611">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222d67cdc2.mp4?token=hMaWnbR4Yw1Od78m2IQZjCY4NwEQZXjAoEu0odHkSrPcYYEGQzmejSKbIfD8ZTV4Xv42HUhgVloTqFPc36kL4vzuwWNYc7OzPoMFG7V9hm1a1SNMT3ZsenFn-BabTegU-D7FD4vZEi99ABZZ0FCdxWUNWl6eKLjNVyJQYUXXbJ_XPcbLWEuwtc_laV09GcpFHM_kHDUUG178BBkhKDO093RV8-srZmQ_9QjIAcuACQfsZj36AsmGl6YjbUgKRX4o26kg21I2B_L8MgMWxvTjzt3iBtBnAi2JziCVxJV4F0Q_xXQwP22EsMOFymgaYNYurAI7u5dCSK3x2OXybRweiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222d67cdc2.mp4?token=hMaWnbR4Yw1Od78m2IQZjCY4NwEQZXjAoEu0odHkSrPcYYEGQzmejSKbIfD8ZTV4Xv42HUhgVloTqFPc36kL4vzuwWNYc7OzPoMFG7V9hm1a1SNMT3ZsenFn-BabTegU-D7FD4vZEi99ABZZ0FCdxWUNWl6eKLjNVyJQYUXXbJ_XPcbLWEuwtc_laV09GcpFHM_kHDUUG178BBkhKDO093RV8-srZmQ_9QjIAcuACQfsZj36AsmGl6YjbUgKRX4o26kg21I2B_L8MgMWxvTjzt3iBtBnAi2JziCVxJV4F0Q_xXQwP22EsMOFymgaYNYurAI7u5dCSK3x2OXybRweiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از ورود خودروی حامل پیکر مطهر رهبر شهید انقلاب به شهر مقدس کربلا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668611" target="_blank">📅 21:15 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668610">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SUe-UapTn_Wjbm9rdaTv_yNACagm4grA5oegwZK1PxrMV9mRmXW0tEmpmgLYD0DkMu5wEJ9jEG4BqQgFI7YKyDAdxEtfu7g_Br0ZHyvx-TIrByAl9lC9NLaz2cmJn1_oNJIztJoBz7lDZJvasKJkCJbTOr_vHHMlQ8Gi2P5Ul7_9yifHGRg_CxZq74BEq1VxvcEQVVAA4B0AdVNerFK4rb0JU5tAZQ_AjrU0IMvFsjQUAed4_rjo4nw4M-HNGS1bDRX99eip_u2egUpyCbruyTFRSzl94nIKGSBMVsYdNR8O8t6Sh-1P1KxuJQKNSR2xk5s_VPaBsuSUfU7efN8I1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#باید_برخاست
برای اطلاع از مراسم بدرقه رهبر شهید در مشهد، می توانید از نرم افزار باد صبا استفاده کنید
#شهرداری_مشهد
#جهان_شهر_برکت_و_کرامت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668610" target="_blank">📅 21:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668609">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
رمان‌های خارجی محبوب رهبر شهید انقلاب
#بدرقه_یار
@TV_Fori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668609" target="_blank">📅 21:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668608">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
به گزارش خبرنگار خبرفوری مستقر در عراق، پیکر رهبر شهید انقلاب به عمود ١٣٠٠ رسیده و به نظر می‌رسد زودتر از ساعت ١٠ شب به وقت عراق، پیکر مطهر به بین‌الحرمین نمی‌رسد
🔹
با توجه به ازدحام و استقبال بی‌سابقه مراسم تشییع در کربلا، احتمالا این مراسم تا بامداد به طول خواهد انجامید.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668608" target="_blank">📅 21:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668607">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/161e370067.mp4?token=rFOfS_pJBUOo3kOUsBUY1tvHmDhcgZuAmTQ1O9CPvhPcKGoV799GBA-BbRcLtQB1Ww10_5WZv6fwsbz82aHb5cDw4xNH6Gb_iwD6xJvkU00z2lxux8rZrbc5rcy5n4PV6nbCubtijSUAoKGq1uLAeQk1hDNLxY0wa6eUfqsREYVgcn3Fn6ybyIXnkOoano1HTWsRAYWbjAWmsMcveWVO3mJT59n-UmRkUUqfc9GzifoB5Qyri-SRKU28WKBsg-uaaGk5DulKn6qwNUGj1wJ8nPNK3ho_agFOE8mNh_PdhQmAajOA2nvp9_OH8J1wGy2bQ2IRLmivQb48ZMRJJzCozIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/161e370067.mp4?token=rFOfS_pJBUOo3kOUsBUY1tvHmDhcgZuAmTQ1O9CPvhPcKGoV799GBA-BbRcLtQB1Ww10_5WZv6fwsbz82aHb5cDw4xNH6Gb_iwD6xJvkU00z2lxux8rZrbc5rcy5n4PV6nbCubtijSUAoKGq1uLAeQk1hDNLxY0wa6eUfqsREYVgcn3Fn6ybyIXnkOoano1HTWsRAYWbjAWmsMcveWVO3mJT59n-UmRkUUqfc9GzifoB5Qyri-SRKU28WKBsg-uaaGk5DulKn6qwNUGj1wJ8nPNK3ho_agFOE8mNh_PdhQmAajOA2nvp9_OH8J1wGy2bQ2IRLmivQb48ZMRJJzCozIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💧
هم‌زمان با برگزاری مراسم تشیع رهبرشهید، طرح تأمین و توزیع آب معدنی برای خدمت‌رسانی به زائران و شرکت‌کنندگان توسط سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی در حال اجراست تا دسترسی به آب آشامیدنی در نقاط پیش‌بینی‌شده تسهیل شود.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668607" target="_blank">📅 21:04 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668606">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f77ea52796.mp4?token=dpjo3vlUzBAGgPNwXV7Z1Syd2BtoGSqZJRi5oq7dVaby-WdL5piZQvQ5he_0EQGl9vany1EKHRx_wqQZYuHp_tE2N_4Gse8xIfCZW_zurFuXdNx1K_ozyhtlWFEE7fxD5l7H6V5M0ts09jtcN7tzwpuKJBZvkedfcdUsJqpvUnSeLrcbEpIWyl9h1I8Aav3yCWLo581skmLqfjCA8V9YWy-5Yu64lS3GDk3c-sKTbKJ70HpYGfoZ2eZxqP3BjZIa4DfeRv0582axIK9NApz6gy2xpN6XIMpIV4XKaGr5H4KSjvzjry0WdUQ-0bSsnefMVonPop5NZyp5E5_cKvxo4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f77ea52796.mp4?token=dpjo3vlUzBAGgPNwXV7Z1Syd2BtoGSqZJRi5oq7dVaby-WdL5piZQvQ5he_0EQGl9vany1EKHRx_wqQZYuHp_tE2N_4Gse8xIfCZW_zurFuXdNx1K_ozyhtlWFEE7fxD5l7H6V5M0ts09jtcN7tzwpuKJBZvkedfcdUsJqpvUnSeLrcbEpIWyl9h1I8Aav3yCWLo581skmLqfjCA8V9YWy-5Yu64lS3GDk3c-sKTbKJ70HpYGfoZ2eZxqP3BjZIa4DfeRv0582axIK9NApz6gy2xpN6XIMpIV4XKaGr5H4KSjvzjry0WdUQ-0bSsnefMVonPop5NZyp5E5_cKvxo4jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
این صداها، فقط روایت نیست.... بغضِ دلدادگانی‌ست که با دل، بدرقه‌ات کردند
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668606" target="_blank">📅 21:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668605">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
عشایر عراق در حال تشییع پیکر رهبر شهید امت در عمود ۶۰۰ طریق نجف به کربلا #بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668605" target="_blank">📅 20:55 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668604">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">♦️
پاکستان: ایران و آمریکا طبق یادداشت تفاهم‌نامه عمل کنند
وزارت خارجه پاکستان:
🔹
از همه طرف‌ها می‌خواهیم که به تعهدات خود ذیل یادداشت تفاهم‌نامه عمل کنند و به آن پایبند باشند.
🔹
ما همچنان آماده‌ایم تا به نقش خود به‌عنوان میانجی بین ایران و ایالات متحده ادامه دهیم.
🔹
جنگ مجدد به نفع هیچکس نیست.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668604" target="_blank">📅 20:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668603">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFS6ouzafh1xWVHncSgozXDo15hLEqKwVatHDsztZCiTHkJlkMuO5IIpJq6Bdz3CVcmOQhabcR9AfhUYD7IJcDNlObSyfZgoh5dmGyw0lk1cFd-VRwAdY0wF1cVvyM2F_bGFfd7lclz1snDVwOSwQkg2aEFNRCXfYF12QJ8vnroHT25YtASAENyOSwaTJNvKarf6ePA7InmIyZrFDvy1vSGBGsivI_icNXmvNJ8ju_lyr6Sopu4JJArcQXn4ktmixX8SYlMLmJ-ucoz0UTmH4-UfgWLYvbCMoTkIMeeu-weWGcgC4Aia1WTQc098-KBZD_8DfaRg0ARN09B96pLURQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عراقچی: ما بی‌ادبی ترامپ را در عمل پاسخ می‌دهیم
🔹
عباس عراقچی در واکنش به اظهارات موهن رئیس‌جمهور آمریکا تأکید کرد که ایران پاسخ سخنان رکیک را با کلام مشابه نمی‌دهد.
🔹
وی تصریح کرد پاسخ ایران به این ادبیات، عمل قاطع و شجاعانه است و این‌گونه اظهارات از عظمت و شأن ملت متمدن ایران نخواهد کاست.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668603" target="_blank">📅 20:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668602">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYtHdPsLWSWUQSybj-HE_pX0JOxMuf7foy5AaotNwIKH0zexs9uRgAHMZQBP5zOWmG6CJGEU2PgyiIB2GWh7j9SwAASaOAsOntj9_qc73tNMoipCWke2o5OFMqc0j27w0SDQ7H9GgjiIwCq-2WesRlrHpklHVBUcHO7aOdOTkWlUq2yfgyFqn6tEgBzoe6_0P9cEaF2ZjWl8elJfGVaI8s6-IhgKYWGEQcyAgsatHP3kbT-PwZPaoDXT0_UZPm2r89K102oFH6B8vr4-IehG6ojjfdmRTxHX25wtJX57YbkDQgYrc4mtpqpmOaMi0ntp5qEFD7hJwmsfRGRkh8YVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
تجارت در مسیر خدمت
🙏
📣
شعب بانک تجارت در خدمت مشتریان
✅
خدمات در حال ارائه به مشتریان حقیقی و حقوقی:
🔺
واریز و برداشت وجه
🔺
پایای صادره
🔺
ساتنای صادره
🔺
صدور چک بانکی و بین بانکی
🔺
ارائه سرویس های واریز گروهی داخلی و شناسه دار برای پرداخت حقوق و مزایای پرسنل شرکت‌های دارای حساب نزد این بانک
🔺
صدور مجدد کارت نقدی، خرید و هدیه
🔺
صدور مجدد رمز اول کارت
🔺
فعالسازی رمز پویا و ثابت
🔺
تمدید تاریخ انقضا و رفع مسدودی کارت
🔺
ارائه خدمات ضمانت‌نامه، اعتبار اسنادی، تسهیلات و وصول اقساط ( عقود مرابحه )
🔺
ارائه سرویس پایا و ساتنا ( وارده )
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668602" target="_blank">📅 20:49 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668601">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3412d0e472.mp4?token=hYe4FO1nDDacSJXGa4xZ8nKdt1NJe4rkP5wNHewV9c2JLCxzMZ6NXihJsvjPINizuKh3fi22V5qGtn1vVhXwkZ3598Pa1hgHN4dK2koOCk9l9agkYel_ONnIIOIdq3CZ8JmAH3l31tzhbKZnxjOCgLOzQA7wy3H3WivbT4SIPbZNKwaFuQRvcgBFv71CPkG8rbFvbPRlK-NB0khKt7C3XXSxnmveyKWpRpRyY39Y4tXzhvZwgMwXOSnAt-Ye6A_FGdhnR_oagJXUBqlVW7vfpubKpeR1pTnCNSWiWQu65N_6FR6bkFtgi7hRqZmXzGiI9YtqzGCYeIE3u_fK9r4wlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3412d0e472.mp4?token=hYe4FO1nDDacSJXGa4xZ8nKdt1NJe4rkP5wNHewV9c2JLCxzMZ6NXihJsvjPINizuKh3fi22V5qGtn1vVhXwkZ3598Pa1hgHN4dK2koOCk9l9agkYel_ONnIIOIdq3CZ8JmAH3l31tzhbKZnxjOCgLOzQA7wy3H3WivbT4SIPbZNKwaFuQRvcgBFv71CPkG8rbFvbPRlK-NB0khKt7C3XXSxnmveyKWpRpRyY39Y4tXzhvZwgMwXOSnAt-Ye6A_FGdhnR_oagJXUBqlVW7vfpubKpeR1pTnCNSWiWQu65N_6FR6bkFtgi7hRqZmXzGiI9YtqzGCYeIE3u_fK9r4wlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حال و هوای کف بین‌الحرمین و عاشقان منتظر معشوق
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/akhbarefori/668601" target="_blank">📅 20:48 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668600">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8g_wrJ9hjG2WBVCVmVo8iGI-zvDx-nw9M_UNVh8zXdqER43rKfBePnDJju118W-Ub0st0B1NIRZjzud-zzn4C-q8zADNbfC1MlvzA9GnNN-w3kFykAIrX4gjtost8BWETXEa4KahuhtAwW-v7HemSQ7lqylw6Y5t0E4xRzQB1LFtZlBKVzQ1pTPbxImhdT1mtvdOiJiHNI3cb9bgmSCrrDAm8aXKH2JXui0DK2xxjWbAYxkcnsMgR8Xt1hmSD4zHsQCRnqJFk7_Qw70Jy-4KG1bPzMsyBOFwxvp9Jn36H83Wj8oPWDeOHcTPQ7QVBDpwYwiA5DT08akuugSPNiXlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سخنگوی وزارت امور خارجه: آمریکا ساختار توافق را نقض کرده ‌است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668600" target="_blank">📅 20:38 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668599">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
منبع آگاه به پرس‌تی‌وی: در صورت تجاوز مجدد، تنگه هرمز کاملاً بسته می‌شود و ایران  ۲ برابر تجاوزات دشمن را هدف قرار خواهد داد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668599" target="_blank">📅 20:37 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668598">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C5MBui6JVRsWemVz9MA6DhzqxXySEieTYAUcGXXTTGRmmsVR5FZGsD_BfxkPDonWtzIFKZnvobZy3zPNQa0NmIbaHpY6_eHX9wF5Qh5UnFeQYSKxMXt_rkALpyV2-omK2htS-1eYYGLQFA_zgQbcz73lvubPC_Wi2exB3TfOw0cZzAXQ1rXrM9dgV28ESfgfvCmX5be-Sai41L_JB4lSbWNyJKara2YRGx9qiDJ-gLxuYlcPaMtFDIn6z_-1aQJjlu5-vb5hZe1SqxNp_YiNDqL3W0VQhkiR35-v0DjLdbKI19GUGXzUo55J9ZUxi0pWzIXif4PTVgE6tR0TBpwZnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قدردانی پزشکیان از نخست‌وزیر پاکستان برای حضور در مراسم تشییع رهبر شهید
🔹
مسعود پزشکیان، رئیس‌جمهور، در پیامی خطاب به شهباز شریف، از حضور نخست‌وزیر و هیئت عالی‌رتبه پاکستان در مراسم وداع با رهبر شهید ایران قدردانی کرد. وی با تأکید بر پیوندهای عمیق تاریخی و فرهنگی دو ملت، ابراز امیدواری کرد که این سطح از همبستگی، زمینه‌ساز گسترش بیش از پیش روابط دوجانبه شود.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668598" target="_blank">📅 20:36 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668597">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/opQWskduUnbogEnzGEpyCVqKzU-d_lR-qwBWzZtDR4AGAMbrLEAAeDqx-S93pKBzCL_f3v2Pto9Zmx7XQgMlyhM-09I21JcHmA0Au8dLQblXCKD7k5Lt8x8pFoWnPH7qH7hdmKekhezfnHIEmRqyBuUs77n4KjZog1TpQvOPVsfpwu5f9IFd0GSRGdeOUU1QXWbsANoYP6FKXJ1STfX11L1BSNRdn12cKgWLd9X7sADwny33uUml54dYd26pk2w3gXX8b4pogqEsaE3O__f_haESSXZUXDeQxBpP3hf2xO7V97CoGSDT5CcYaW3l9Jzl5JImnAo-p7TrnSwls_UvRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاانی در صف اول نماز مغرب حرم امام حسین(ع)
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668597" target="_blank">📅 20:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668596">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/740a7be7c7.mp4?token=ivKRic4Z0yqFEFrTS-tUgXWzd2j9KDb-Ptvb-73f7rNHfs07pgQaR6_qW-FZLRmACrZertLN2fYAcQUEJlz-gPxyoKOmdcAqF7x_8F4ge61osQDNSMc-djR-3Muwh0rw_A1FPahePOu9QWdPgW9P6MPTMjQk1WDQDyZZutRVcyztikWw1lUjDuTqA58WdkIh4yvIq49jU4xqm2ThYXGM-73Cov9q6_ONTYn9pGgNa9M3bbtkUAbnvAG9tqnhyboCn9QxQryLr4kx41ulJcqlqTWOjNnsvhf5A_O7vMI4b81ciskhyXjR-f9oxJJlbHeg43fEsxCIMQ4q6xnkpVMgFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/740a7be7c7.mp4?token=ivKRic4Z0yqFEFrTS-tUgXWzd2j9KDb-Ptvb-73f7rNHfs07pgQaR6_qW-FZLRmACrZertLN2fYAcQUEJlz-gPxyoKOmdcAqF7x_8F4ge61osQDNSMc-djR-3Muwh0rw_A1FPahePOu9QWdPgW9P6MPTMjQk1WDQDyZZutRVcyztikWw1lUjDuTqA58WdkIh4yvIq49jU4xqm2ThYXGM-73Cov9q6_ONTYn9pGgNa9M3bbtkUAbnvAG9tqnhyboCn9QxQryLr4kx41ulJcqlqTWOjNnsvhf5A_O7vMI4b81ciskhyXjR-f9oxJJlbHeg43fEsxCIMQ4q6xnkpVMgFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور فرزند ارشد رهبر جانفدا در حرم مطهر سیدالشهدا
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668596" target="_blank">📅 20:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668595">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Df0b-7q1rCfNP63vahgiGqLFq5eQyQh0PZjLdzaa4Ivj-SAHeax1kpLUqdWDOD7BWdvoh_-NBTXPWeEvPltdSBWB2tyewqiwqjuHg1OdAa9_gS_F4nKzzmKijvK_A_Ww5oqJ7ZU1qoy0T3WZ3byYlSDXdx48HBF1JZ_Mvxt-i8tGp8eEcAfUwLjKlU4lXNhkud1Mj6RlhoMyS7VgIRDZR5zxispLLfj2vEE-da4tbIlpi1GlpN_SBj49W3X3cu92JgVXBNxR4vPgG6NnoDHzYTyDDEyTbfXV0gOWN89VWLChgSZR0Lb3Myhwd9_GWslg3Abyrez8hL2EefOIKkBYCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سوء مدیریت سالانه ۵۲ میلیون تن زباله پلاستیکی در جهان
🔹
ایران با تولید حدود ۵ تا ۱۰ کیلوگرم پسماند پلاستیکی مدیریت‌نشده به ازای هر نفر در سال، وضعیت متوسطی در مدیریت زباله‌های پلاستیکی دارد.
🔹
کشورهایی با مدیریت پسماند ضعیف‌تر و زیرساخت‌های بازیافت محدودتر، معمولاً میزان بیشتری پسماند پلاستیکی مدیریت‌نشده به ازای هر نفر تولید می‌کنند.
🔹
تفاوت کشورها فقط به میزان مصرف پلاستیک محدود نمی‌شود؛ کیفیت جمع‌آوری زباله، تفکیک از مبدأ، بازیافت و شیوه دفع پسماند نیز نقش تعیین‌کننده‌ای دارند.
@amarfact</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668595" target="_blank">📅 20:29 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668594">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiY_EY-YWID6-Sy5ueFQNjkr6HpNr3BVTPZ8R8B5THsfyyklgcnsyhabnnY0DKNzo_c4_i46zsW7EDzkQUKp1RTOGVxiBTez51ZenR_4Et7JhCrSGuQz4x2w0C3j0CpM19EGoJsUXirrLKRWneuuj1Xpkeaz8WzHiZ4J3OdEy5BPRXxp2ZC0wthpEjNNDGbZ2DNyZZ15aTiyVu33FL8GzEC0PtVE4yxMZ5ocjqO384zj80OE0lEeXuWP7xnJsQan0Si-zh94UQ9ueZRWkTiZyGm5WzuXI9wChhJf7cK_mwuMjWZe23e7lUQblB2lG4FFIqJNlRFHfz4K6aIl6b4JLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غریب آبادی: با ترامپ جنایتکار و قاتل باید با زبان خودش صحبت کرد، ظاهرا زبان زور را بهتر می‌فهمد!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668594" target="_blank">📅 20:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668593">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
انگلیس: باید آتش‌بس بین ایران و آمریکا برقرار شود.
🔹
نخست‌وزیر ایتالیا: در حملات علیه ایران شرکت نمی‌کنیم.
🔹
وزارت خارجه پاکستان: از سرگیری درگیری‌ها در منطقه به نفع هیچ‌کس نیست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/akhbarefori/668593" target="_blank">📅 20:27 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668592">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حرکت کند خودرو حامل پیکر قائد شهید در کربلا بدلیل ازدحام جمعیت
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668592" target="_blank">📅 20:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668591">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eqj3-ptTjjXJJGgboi7l_LLLR2QezwwAxSqDwRoS0ui8Z23NZnNDrpL-V9CA8gG7tpGnw4UKFET3aerAjfdZuUddm2pBkIsALdIuUZK1E43kQPDgyjw1vaJm9XiWTmuvBi2nfI3VCEQiTwENN6IsMRyd4deY4J6q1xbFv1tc5yjYB1eFs3nSAPdq_eiLNw2yNzNj6bhkfvomlocmBNFPxBjO9Mw_CKBA3QqJ_3tkHTKy-3R2O1fzIXo9NOHy3nFDVCdlJwZc5ePfaENkQdNOHTKv-uXO3LvaZvxO9Dl9EbeklsUxn5q8sWs55Teb0UWNH9FDnrg7trsGL268iQ_mtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پرتکرارترین کلیدواژه‌های رهبری در طول ۳۷ سال رهبری ایشان
#بدرقه_یار
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668591" target="_blank">📅 20:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668590">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWct0hPz5H6vgf7s8K34aj7bP262oDqwt-E7mfltwcZX25ZhPqoc41J06CkPxticoSam4BU1y8-F4aKtbeqDwJvMXvaEWpY_TuGpI90MGxbw2LpPEFGTAiIOMFnXiywlvak6jw91ZwfiHlnkR_HIpIjcknAQ4ASpeppZsk3KxWMF6wy0gCiDWehBBjNsh-PinIoqPlcORCmLhXPvXCr6BEKhwyP_CCA-lnrQNX6_QzdH0B-rXXef9RbHQ6o7ihSZallEiW0YxGLNWuUgrFgTnC_CO0y_u-DGrKmqwVmp6jywKHXSYZLLB61HvC_E1Unbg_5VV4ShwfX6gY2rbTDgWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ضرغامی: ترامپ را در ترکیه ترور نکردیم؛ به دلیل حفظ دوستی و حسن همجواری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668590" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668589">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">♦️
خوک زرد: من هدف شماره یک ایرانی‌ها هستم
🔹
ایران می‌خواهد به توافق برسد، اما بلد نیست چطور توافق کند و سپس شب‌ها می‌روند و به کشتی‌ها تیراندازی می‌کنند. من این کار را دوست ندارم.
🔹
من می‌خواهم موضوع را در ایران به پایان برسانم و نه اینکه با رهبران فعلی بازی…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668589" target="_blank">📅 20:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668587">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WRlls0b9YRyYB0f8sm0n2VmOrfEmzOVbJh24TTNfNCJ6UZioZoTAL5Oj7DjGB9NZX_ZSq9T2gUB99yPa9OViB5_gvJ8Pp5NgNdUXT17crle7seVMoysMs21oTp7NNHlTpRHy0Xk2pHhbVBowrirKpeVng3EeEShTO-OKDYz2hdM0Vi7cgnYIdGHcEXA6pl2jmwqMZ2tjF7GeT9F9a1YyUjkvMSzokSFUavUGzm4vXmDadMWILMXXtW2_rx92tPyA0kx1ZzTtBUHwklO1ep53r5ZMUj2BXH-T2DWOwVWEu7sYt8zv5-vwBxtD0mJyZw1ZAHnwwEfKI9prLOKHRcP-WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQtTDVw_pgSa6oZ98Ylqq_FoPr891KvzxWmJd77eGaSf5JlaaHeLycfFc1n1anflpvwOA-TLjI_zP8rMtpqtB8dpF8v2403PeglZHvFORW5pW1ngSaC41MVnN6B_nho7SwkVBbl5tvKXYSOHqM1sPanlXQREvktO5u6P8emN8OZoxsfnB9zaMDokF23w9CC8rQnNz1_6quWRHIdInE7u40h4wW1p_06CPq3KUHcaXyNCUa9NXZ13cPhQ7kw_UvxDcfRnp2CezpxpmhLi011bDnNQizIp3khZDy1__TArKyZrbNdA1HliuXmL-14ddgMYPw1A3Jr7dJ09pXAH5lhXeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
روایت‌های خواندنی از روزهای رهبر شهید انقلاب در تبعید پیش از انقلاب
🔹
کتاب برتبعید به دوران تبعید رهبر معظم انقلاب در سال های ۵۶ و ۵۷ می پردازد. آنچه در کتاب «برتبعید» آمده، داستان و تاریخ گذشته نیست، تصویر زیبایی است از سبک زندگی و مبارزه و مردم داریِ یک…</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/akhbarefori/668587" target="_blank">📅 20:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668586">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fb51ba2cf.mp4?token=kSVVa8z_kbZlmwpLju-eCk_w4eyXNmcsc2_mNSXQbn0QCfe74LacNZsTesTNYiG3XVf7UAW09Ni-VhBAl2MjKRH0HahbNthcFV4jl1u8YhpZaETkfeAcYHIZc-TzZIsP0zRI5Zz1l3w4ty-XcVhBCKzHmyXqmk7XBujGAiHiiYdVnP2egojlEBpgsynkxTh7hRsS2Si-iEYGDOacZVNzkU3jgEyDzTsC89Y8kwM66Uamzxo4bQ8gT3uujn-qkXOGypt7P-PDcKUufuCTgpo108RKXNvDkJWEALdPIqIVZarfMgHe6nmnLedN8XNXVALMwxrHSEb8ICPnOBRKMKlrHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fb51ba2cf.mp4?token=kSVVa8z_kbZlmwpLju-eCk_w4eyXNmcsc2_mNSXQbn0QCfe74LacNZsTesTNYiG3XVf7UAW09Ni-VhBAl2MjKRH0HahbNthcFV4jl1u8YhpZaETkfeAcYHIZc-TzZIsP0zRI5Zz1l3w4ty-XcVhBCKzHmyXqmk7XBujGAiHiiYdVnP2egojlEBpgsynkxTh7hRsS2Si-iEYGDOacZVNzkU3jgEyDzTsC89Y8kwM66Uamzxo4bQ8gT3uujn-qkXOGypt7P-PDcKUufuCTgpo108RKXNvDkJWEALdPIqIVZarfMgHe6nmnLedN8XNXVALMwxrHSEb8ICPnOBRKMKlrHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خوک زرد: من هدف شماره یک ایرانی‌ها هستم
🔹
ایران می‌خواهد به توافق برسد، اما بلد نیست چطور توافق کند و سپس شب‌ها می‌روند و به کشتی‌ها تیراندازی می‌کنند. من این کار را دوست ندارم.
🔹
من می‌خواهم موضوع را در ایران به پایان برسانم و نه اینکه با رهبران فعلی بازی کنم
#Devil
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668586" target="_blank">📅 20:07 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668585">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35725a8b4a.mp4?token=FFbpYQGYbvj6Sj2cfkyS0sObM12nhp225-U9u6pLA1lkjbvGegGJZou4pVe2eB5Y8IA_C8W1JpgsmKlStJzEc3ijLVoKDSHSt3DLSefEfUL-ojhC7bY5DZe_2F61qb5AUcWbn_H9fdoq8HUWRcTqKxCMZC3-0peXYx_bPUWx-Jd0vPBo77G1C-hMq2a_xbzV2dDYB3B-NBwU3Xx9VKgCLLphIN3O3tu6fjQ143pa50hYh9Ej4D6aWYqrENNoT08PvE9sxvhigG9OCHGIVPDmQCm4iNAifntU6dbww85Qhj3d_4PTeS-CE5Tbods7Ya2agEpbIHU_LN3PJAfD9GaWvb1Dpiqy1eiyE8ngQ5kUTK0ecE599GR-8MikCQ4lCvKyl1abeob1Pod4d9kMFGap6qx8CcoSrJiqAty740V4Iw52m4-he4b25NoTxTGIbs0UJd4DhkTUjNAMkkV36Y8q4Gc1bxxtnOaKhtgQm3hn-FL20uMKDqKJ_cBINgVWdze83Wy_yvyfJI7N8-9DHJ447CcfaNvfksgQZXmC4z-EW3plIv1zWTrbzPfk0w6EHE8TtW0nNbgchJIYZoPdx9dRjVRp2wuVigBSyXyloPf-j_sEvhtF52ftea0Z_eIp5I8itHZS561YvnNlURsd1jsEDT1reRB4xxUcIFH5mTywNGM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35725a8b4a.mp4?token=FFbpYQGYbvj6Sj2cfkyS0sObM12nhp225-U9u6pLA1lkjbvGegGJZou4pVe2eB5Y8IA_C8W1JpgsmKlStJzEc3ijLVoKDSHSt3DLSefEfUL-ojhC7bY5DZe_2F61qb5AUcWbn_H9fdoq8HUWRcTqKxCMZC3-0peXYx_bPUWx-Jd0vPBo77G1C-hMq2a_xbzV2dDYB3B-NBwU3Xx9VKgCLLphIN3O3tu6fjQ143pa50hYh9Ej4D6aWYqrENNoT08PvE9sxvhigG9OCHGIVPDmQCm4iNAifntU6dbww85Qhj3d_4PTeS-CE5Tbods7Ya2agEpbIHU_LN3PJAfD9GaWvb1Dpiqy1eiyE8ngQ5kUTK0ecE599GR-8MikCQ4lCvKyl1abeob1Pod4d9kMFGap6qx8CcoSrJiqAty740V4Iw52m4-he4b25NoTxTGIbs0UJd4DhkTUjNAMkkV36Y8q4Gc1bxxtnOaKhtgQm3hn-FL20uMKDqKJ_cBINgVWdze83Wy_yvyfJI7N8-9DHJ447CcfaNvfksgQZXmC4z-EW3plIv1zWTrbzPfk0w6EHE8TtW0nNbgchJIYZoPdx9dRjVRp2wuVigBSyXyloPf-j_sEvhtF52ftea0Z_eIp5I8itHZS561YvnNlURsd1jsEDT1reRB4xxUcIFH5mTywNGM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خدمت بی وقفه در حریم رضوی
🔹
برای خدمت‌رسانی بهتر به زائران و مجاوران در مراسم تشییع پیکر مطهر رهبر شهید انقلاب، اطراف حرم مطهر رضوی به ۱۳ جایگاه عرضه ارزاق عمومی، ۱۲ جایگاه میوه و تره‌بار و ۸ نانوایی مجهز شد.
این اقدام، بخشی از تمهیدات سازمان ساماندهی مشاغل شهری برای میزبانی شایسته، تأمین به‌موقع مایحتاج ضروری و روان‌سازی خدمات‌رسانی در روزهای حضور گسترده سوگواران است
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668585" target="_blank">📅 20:06 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668584">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
سنتکام: بیش از ۲۰ کشتی جنگی آمریکایی در منطقه خاورمیانه گشت‌زنی می‌کنند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/akhbarefori/668584" target="_blank">📅 20:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668583">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
آموزش‌وپرورش: فرصت ثبت‌نام در آزمون‌های نهایی ایجاد و ترمیم سابقه تحصیلی تا ساعت ۱۲:۰۰ روز پنجشنبه ۱۸ تیرماه تمدید شد
🔹
این مهلت قابل تمدید نخواهد بود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/akhbarefori/668583" target="_blank">📅 19:58 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668582">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">♦️
حضور پرشمار عزاداران در بین‌الحرمین و کربلای معلی برای تشییع پیکر رهبر شهید انقلاب
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668582" target="_blank">📅 19:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668581">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aozAba08GG8d9j7CEB_oZ0S9BUhuqZ-VDunnE6Nc0AXPDTGi3RxtQvJYUHNZSuvjHvr7bZq3B1-2K__84XWoigMHXA1Ba6KQlOf2Xeh0n5mDTCgyEuxKmvywU3w5BQ0jDtcRp_fgZxOvgBfek_8152Y96wETKEpfl-sKngVHSdH__KMt621ovswHQE8H-GbOtBJ9rRY63TfUhudZlfFWy0TqXkGlxKMDHjeV85oRYbTgO62XDk87ysb5bWGWX35fUMDCkYPDkXwMOuUnxezF8wlukkF0hSSjxwJCICGfWAtJEhE3Nn2jd73hQZkzKtwgLqF0A2V2gIou5pBO06tOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حضور مسیحیان و صابئی‌ها و طوایف مختلف عراق در کربلای معلی برای استقبال از پیکر مطهر رهبر مسلمانان جهان
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668581" target="_blank">📅 19:50 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668580">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpRfM_6cd_2CU8r6Y-u9Vs39Lya4dyyZ97xvj0yTThp_VjZbtK8FngAgY5AZ8xB1Fmsql3x7VEX7_9Ysy5ELK89S_INj-lxbXsFUeN2pAZLln3dIqxSWlTawYNlJBHOKxWtqY69FIQr2uwg56v56xjzCnhojGvSINzsYbfHjSNInD3EloKZjcREJj23dFs48rjd8Fv5zmwc115hrJpXyde_1Z0jXSOqV2wSDwI28RkdLy_eRrXlrvxe8NnIJEJX0hflRjEuIzdx3hA8NGMBdzXyEK4OPZBSjJqh7ESCRlqVlvhCkOwjQzICvAaOGnXYSVweqf4vNJQLChaQjrp_voQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خامنه‌ای ادامه دارد...
🔹
تطبیق اصول حکمرانی امام شهید انقلاب با پیام‌های رهبر جدید انقلاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668580" target="_blank">📅 19:45 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668579">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
بی‌بی‌سی: ترامپ با وجود تمام لاف‌زنی‌هایش، گزینه‌ای بهتر از مذاکره با ایران ندارد
🔹
تهدیدات جدید ترامپ، قطعاً حرف آخر او نیست. او بارها درباره جنگ و تفاهم‌نامه اظهار نظر کرده است.
🔹
اظهارات امروز ترامپ را می‌توان به عنوان اعتراف دیگری تلقی کرد مبنی بر این که رئیس‌جمهور آمریکا با وجود همه لاف‌زنی‌هایش، گزینه بهتری جز مذاکره ندارد.
🔹
آمریکا همراه با اسرائیل تلاش کرد و نتوانست حکومت ایران را نابود کند.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668579" target="_blank">📅 19:32 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668578">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUYLVSf3mxj9Oydq9zNNh0YLYlm96dXHbR8mTdSBc9YBOQU0N53BfhTUPEZtZVICJ12CD--zV3JfysyYTKFcCfiroUxqtACCNRWiwpqrhbICRkAPbW_4kmFyvyPzK_RCD8CkMwGyTyxVyxF_PssJdoQ3bEZ7A6KbGZNxDXNTcQLF4Bmcudee0n2XFVi18Cn9vtkSYZKuH_RUqnDWhQ35sBqAVPmTkTqIQU1egS_KpxnswoFLGalLyZ4hjFqSNIha2yNhKBd4hTmnQ0_C7hHJr-8lIHZlwzaV0nzTx-ZbbDQKoxJrHZ0oQpq8NDjBnGkcoyF468e9D1SVUpdipdaK2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🛒
فعالیت ویژه ۱۴ فروشگاه «شهرما» در مشهد برای خدمت‌رسانی به زائران
هم‌زمان با برگزاری آیین تشییع پیکر مطهر رهبر شهید انقلاب، ۱۴ فروشگاه «شهرما» در مشهد با عرضه اقلام اساسی و افزایش ساعات فعالیت از ۸ صبح تا ۲۲ شب، آماده تأمین نیازهای زائران و مجاوران شدند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/668578" target="_blank">📅 19:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668577">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
ادعای تاس: مذاکرات ایران و آمریکا متوقف شد
🔹
رسانه روس به نقل از یک مقام ایرانی مدعی شد که به دلیل نقض مکرر آتش‌بس و تهدیدهای آمریکا، ایران مذاکرات را به حالت تعلیق درآورده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668577" target="_blank">📅 19:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668576">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20f87b03e2.mp4?token=VjemKpDxaZHxSm1Hz6ZkrS1EgrNrJDZOVS0VnW6IjhIJ9YiwM5BPDRV6skc5MK825OIajMQdXvua6DfsHXsP7Lcoa_L4tf_KwA-0-EPr4SdcLx-oKyKtAJdZifaEE8rOd0hMTqexqAvnYZZ6jgtho30xr_oATuPS0KEEpY1rrbDZkieo8zICKqf79MfszYhujCgk9QAdH8taqkQbGT1VdshFKjhy5MKcc_prjSZI5eB1gPpMuhqmJa3AnkJmzctG9Dlm1-2Y-4vspZ3PumeimP31I7lYWz-ikFwrvx8ExsLxkTTdpuBS9tJTzE3LEccQfMxD4yOrTRl9P40nJgnoDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20f87b03e2.mp4?token=VjemKpDxaZHxSm1Hz6ZkrS1EgrNrJDZOVS0VnW6IjhIJ9YiwM5BPDRV6skc5MK825OIajMQdXvua6DfsHXsP7Lcoa_L4tf_KwA-0-EPr4SdcLx-oKyKtAJdZifaEE8rOd0hMTqexqAvnYZZ6jgtho30xr_oATuPS0KEEpY1rrbDZkieo8zICKqf79MfszYhujCgk9QAdH8taqkQbGT1VdshFKjhy5MKcc_prjSZI5eB1gPpMuhqmJa3AnkJmzctG9Dlm1-2Y-4vspZ3PumeimP31I7lYWz-ikFwrvx8ExsLxkTTdpuBS9tJTzE3LEccQfMxD4yOrTRl9P40nJgnoDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
محل تعیین شده برای قرار دادن تابوت رهبر شهید در حرم امام حسین علیه السلام
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/akhbarefori/668576" target="_blank">📅 19:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668575">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2a11958c8.mp4?token=kSZtZXXRE57QPaBHTuoeARulELCIonF6S9hQzAJLt0i5LTOfQ5zd34hm4oMQNIxlxGpyxDu40pxK_aCnBS3unEz4pRVXTfClmPjcI8pYCrHcJfF5A2z1T8RUC-NExJdf-SN8XFo_C_diA4loyo5KMjx8U5ptNAMxM2hf112MlJT8ZiCNisQBwYEG5ZRAQ0Gw4DVs2UhSZiqSsT0Or9TkqK0ruuncE5TFNsfoP9fsIR1d6mmB29OzvJSy5tY4BTD_O50gKrgLJiF-SNqlGcHL4eDa9mknUkgZnSlxjYVc5ar6zZJi7D88zi-UxG8L6neWrgjyovJRgHSa42fl21FUSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2a11958c8.mp4?token=kSZtZXXRE57QPaBHTuoeARulELCIonF6S9hQzAJLt0i5LTOfQ5zd34hm4oMQNIxlxGpyxDu40pxK_aCnBS3unEz4pRVXTfClmPjcI8pYCrHcJfF5A2z1T8RUC-NExJdf-SN8XFo_C_diA4loyo5KMjx8U5ptNAMxM2hf112MlJT8ZiCNisQBwYEG5ZRAQ0Gw4DVs2UhSZiqSsT0Or9TkqK0ruuncE5TFNsfoP9fsIR1d6mmB29OzvJSy5tY4BTD_O50gKrgLJiF-SNqlGcHL4eDa9mknUkgZnSlxjYVc5ar6zZJi7D88zi-UxG8L6neWrgjyovJRgHSa42fl21FUSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شعار عراقی‌ها: یاحسین علیه‌السلام پسرت سر خم نکرد
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/akhbarefori/668575" target="_blank">📅 19:25 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668574">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=u9YNovL-I6bPb4NV2jOeAdlC6vOA_onjAap-3a6LEmFu-IW3p5B_yyBpiFt1e1Oc--Py5EIaqIM-eUKdAysuaMvsyloicyxz0fpMIN4qTuosvBXGSUvuuMGQQC8pOAJnWRhX5mpVDgT4z9QfzYsB4H2zGb_ujywcNgnAUxtC-22l1nlsqcY8BIRZUnXHxZqePqQdorMFXA6aMuLNo-iqe3bF-kJ1M52XT0Wt_fuVGJqn8XbvyfR-9kWdHJIA6Zy-aWUguZ9ldPF1zqYZHrnJPhV41wBbnYAe3_ZmlBhPfEGxG9T9-mkanC7efeT3VzXKuTWVezSqroEO3QGH1tTI2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c194d5bb86.mp4?token=u9YNovL-I6bPb4NV2jOeAdlC6vOA_onjAap-3a6LEmFu-IW3p5B_yyBpiFt1e1Oc--Py5EIaqIM-eUKdAysuaMvsyloicyxz0fpMIN4qTuosvBXGSUvuuMGQQC8pOAJnWRhX5mpVDgT4z9QfzYsB4H2zGb_ujywcNgnAUxtC-22l1nlsqcY8BIRZUnXHxZqePqQdorMFXA6aMuLNo-iqe3bF-kJ1M52XT0Wt_fuVGJqn8XbvyfR-9kWdHJIA6Zy-aWUguZ9ldPF1zqYZHrnJPhV41wBbnYAe3_ZmlBhPfEGxG9T9-mkanC7efeT3VzXKuTWVezSqroEO3QGH1tTI2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حضور مرجع تقلید شیعیان کربلا در مراسم تشییع پیکر رهبر مسلمانان جهان
🔹
حضرت آیت‌الله سید تقی المدرسی، از مراجع تقلید شیعیان در کربلا به حرم امام حسین برای حضور در مراسم تشییع پیکر رهبر شهید انقلاب رفتند.
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668574" target="_blank">📅 19:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668573">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxTT_c9kEAXyLHeKRMnvnIcnzHX4SlR_1eL6LwIAsLct6tRRtOoQ8Sfh7KJrqgXtH3SG0xaXinpbzHctRTxZ5z5Z8uh71NdNok8ePaThZtMjWdXAF567kJPYigNZhT0F1kaa5eJwr54A_jx4KA236Mcw4W2IBEVj2q9hL0jWUVADsH1w8znG163j3c-q-CpZyaeaFWuHGZZP2taCvee5tSSwqb2Een-LPG6FeKZrhKf7DIaA3ToNwKURlidRi6aRbwIxnqOf66xAampPyUSoVcuJelzlvgpG2XKZtnygCIJICgasA5k2Rnf9A3EC7GSQZOns8tsf2gaRVwwDaNXLZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ارتش: به دنبال حملات بامداد آمریکا،
۸ نفر از دلاورمردان ارتش به شهادت رسیدند
روابط عمومی ارتش:
🔹
در پی حملات جنایتکارانه ارتش آمریکا به مناطقی از جنوب کشور (بندرعباس و بوشهر) در بامداد امروز، ۸ نفر از نیروهای هوایی و دریایی ارتش در حین دفاع از میهن به شهادت رسیدند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/akhbarefori/668573" target="_blank">📅 19:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668572">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آموزش‌وپرورش با تعویق مجدد امتحانات نهایی مخالفت کرد
رمضان رحیمی، دبیر کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
پیشنهاد تعویق امتحانات نهایی به وزارت آموزش‌وپرورش داده شد اما به دلیل تداخل با برنامه‌های آینده و کنکور، با تغییرات کلی موافقت نکرده است.
🔹
دانش‌آموزان و داوطلبان کنکور ارشد درخواست جابه‌جایی امتحانات برای حضور در مراسم اربعین را داشتند که ما این دغدغه‌ها را به وزارت علوم، سازمان سنجش و آموزش‌وپرورش منعکس کردیم، اما مقاومت‌هایی به دلیل تداخل با برنامه‌های آینده وجود دارد.
🔹
توصیه من به دانش‌آموزان این است که درس خود را بخوانند و به امید تغییر قطعی امتحانات، از مطالعه غافل نشوند.
@TV_Fori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/668572" target="_blank">📅 19:11 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668570">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
سخنگوی کمیسیون امنیت ملی مجلس: حملۀ مجدد آمریکا با تغییر دکترین هسته‌ای پاسخ داده می‌شود.
🔹
خوک زرد
:
احتمالاً سوریه را از فهرست کشورهای حامی تروریسم حذف خواهیم کرد.
🔹
لبنان مشارکت در مذاکرات رم را به عقب‌نشینی رژیم صهیونیستی از دو منطقه آزمایشی مشروط کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/668570" target="_blank">📅 19:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668569">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
حمله هوایی اسرائیل به اطراف یک بیمارستان در جنوب لبنان
🔹
رسانه‌های لبنانی از حمله هوایی جدید رژیم صهیونیستی به نزدیکی یک مرکز درمانی در منطقه «النبطیه الفوقا» در جنوب لبنان خبر دادند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668569" target="_blank">📅 19:02 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668568">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jjGcUtRnADQbgi-IVe-JtNboDeXJ9CErkshxWvabWWtXas5mYMqCSyanvJBha5-d3uwK1cA7SoZTvcoM6jdFBOtfn0otxNNrIgk1TudfMCpvL9NstRwbigoJHQol4KcmW3oHfHVt4n689P0YaGMPETMLTlAb-9EXv2J0rYYymIwp3di00pEmttxg4TFW4LysJGvjlBV3U8R6rYdj425LOACImNrhaaaHTWobOJBJNWuxk_KB6dTCN7Pn6Mv3UNJRGXwyqbKTTTNyfPyqHmKrF8vETjUt-UabYYse-b4XgLgxFBQLlEiG80hheziKWgEAHgBUZ8Xen3cg7bJHyrRQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📺
پخش زنده مراسم تشییع رهبر شهید از نمایشگرهای شهری مشهد
هم‌زمان با آیین تشییع رهبر شهید انقلاب، پخش زنده مراسم و تیزرهای هویت بصری از ۸ نمایشگر شهری در نقاط پرتردد مشهد آغاز شد تا شهروندان و زائران در جریان این رویداد ملی قرار گیرند.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668568" target="_blank">📅 19:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668567">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1SFOCgHrv79N0y6Asmn7CeCCBLL0415rf-0S4O0-UyIqvhgofB2r8GOo_ld7hwgmrjCjSb4kUDyGPlRD2YX3RY7OF9ZHyP5OoQcawNB39_4H-2YlLxbxGCXdpmC2s2KzAjebr3eWMfDTmVUSwarQaSanI8vIs_A482aQOn4ab_DdWL6CzVjHj43aTKPkKl1ohdHN7LgiNoFu9mGJQSSLNHkHu4XgzHlboJ4HltEgD-qee3Du20kf8VQYVlHtSU1KpMqbtdkt7W-AeiClgqKGyedxVh24SgTYQ2NnXnb0jOTYbxIy6cAisRI6Oir7prJiwBRVHLnWO2anXZ1m0FyEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/668567" target="_blank">📅 19:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668566">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGU89VyKw-Z3plC7oEWybI_PeX7JL0n7FjE7m56lhWLf-6qHft8vnwKEWGuB7MMSHtX4mBG0gHRbrEVLuE2TCkWVUA2T7dC42QEpfHDiukrJXqgamrQsL8JoSbBCx4dwtnVqOBoX92dEr5F3w_TW8WSBar8kVrV53kom9snITT5rXvCqkatT31G9ZN8JouGwCKvQ8wqtIZWMqQQVxkMT4TYwwgyJjaqm8EH3NtvqcovPUJDUbyLrtML-awkj-n1HRrbSAcuNvu1FqlPgj-r2iEJ7CPjdYY0U1khiikX77pAmXUCigmjGdKA4aZ-FYcVyDLaiuhVYlwiziaAi7xNElA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت دوباره از مرز ۸۰ دلار به ازای هر بشکه عبور کرده است
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/akhbarefori/668566" target="_blank">📅 18:59 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668565">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc185bc0cf.mp4?token=KUQqTQq3DgXtc9OSOVDnMLCHJLRJUW1Vxu7aD-ruvDm2UYtAY_RgaV8vyaF_DCfSNTyp9EIc6PwN9EMcXINzN9cpjm8rXrqu7KqAZHxbSxPxwS5JDl5y_lV4Fa8_NMRFgf_cZSrrxya9z7TSQFsXnwdBqLbfQcZJKjtdet_-wrZkRGYVWyDhEF9Sif9o7zQMu7pC66dPesV33BKAU7bJVkJ-uZcwA2_mqNlKL0oY0SEzC29v51Mh85q271Cp9A-Q-B1J2fldxhUmRiYn5MpSV-E0ZaJ1LZRzLz5WQHl1GWcr-ITSdN-4zAV0C9apyfQzjYQQsQjGmV6J2vnDPsNdFAwlFBq8nQVncTIFLqToAxlkR3rVW_aG5WW2h1F3eBdx-mzeUsvZySEKBWvb8gw0eWmxEIyq059q3qIleUPLv3opG1-TA4J9V5HNmqIE0XxcyFYgmA9lE-5IpLi3g3JNNwSD6x1gz9YUVsY_-fvpIR7unOdBfWD2U9BObL5gF-PO3jeGv_S9Zpusm4kCZTBPYkrP-3kpWDsPj7RjF-ZK2zgWWT8FEuQnMFGiq2H2mHvPfvTx4Y2ziLiCfkgF251fFJ-vQizsovGE0Bfny-6Lfrax8iZsnvh393HebxGGjWqtlRVId6G9bu6DOT2X7SybHdMptEImVA406zVkvf9Udv4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc185bc0cf.mp4?token=KUQqTQq3DgXtc9OSOVDnMLCHJLRJUW1Vxu7aD-ruvDm2UYtAY_RgaV8vyaF_DCfSNTyp9EIc6PwN9EMcXINzN9cpjm8rXrqu7KqAZHxbSxPxwS5JDl5y_lV4Fa8_NMRFgf_cZSrrxya9z7TSQFsXnwdBqLbfQcZJKjtdet_-wrZkRGYVWyDhEF9Sif9o7zQMu7pC66dPesV33BKAU7bJVkJ-uZcwA2_mqNlKL0oY0SEzC29v51Mh85q271Cp9A-Q-B1J2fldxhUmRiYn5MpSV-E0ZaJ1LZRzLz5WQHl1GWcr-ITSdN-4zAV0C9apyfQzjYQQsQjGmV6J2vnDPsNdFAwlFBq8nQVncTIFLqToAxlkR3rVW_aG5WW2h1F3eBdx-mzeUsvZySEKBWvb8gw0eWmxEIyq059q3qIleUPLv3opG1-TA4J9V5HNmqIE0XxcyFYgmA9lE-5IpLi3g3JNNwSD6x1gz9YUVsY_-fvpIR7unOdBfWD2U9BObL5gF-PO3jeGv_S9Zpusm4kCZTBPYkrP-3kpWDsPj7RjF-ZK2zgWWT8FEuQnMFGiq2H2mHvPfvTx4Y2ziLiCfkgF251fFJ-vQizsovGE0Bfny-6Lfrax8iZsnvh393HebxGGjWqtlRVId6G9bu6DOT2X7SybHdMptEImVA406zVkvf9Udv4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
در فاصله کمتر از ۱۲ ساعت تا شروع مراسم؛ حرکت کاروان‌های مردمی مشهد به سمت حرم آغاز شد
#بدرقه_یار
#اخبار_مشهد
در فضای مجازی
👇
@AkhbarMashhad</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668565" target="_blank">📅 18:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668564">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
حشدالشعبی: ۴ میلیون نفر پیش از ورود پیکر رهبر شهید امت، در کربلا تجمع کردند.
🔹
یکی از کارکنان پایگاه هوایی بوشهر در حمله تروریستی آمریکا به شهادت رسید.
🔹
روزنامه فرانسوی لوموند: امارات مخفیانه در سومالی‌لند برای آمریکا و اسرائیل پایگاه نظامی می‌سازد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668564" target="_blank">📅 18:53 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668563">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WETvRAOkOMxIbdeUo2_lS5etG-XV_T64GsFPScy4KyUp3-Q1BHYnV2oiuTPqQeEhNIQVLKkhyjdxOMo8dOQygK2qFO2toqUn7V52UJ_fCZNbghHXLts0hjdeNT4lEpvsLLVbtH3yQ_FyjvfvUdZYmxEtAvK-Ceub05BzDS6wmQWQ6NVAyf2rW5jtDSTIRK9ZeneUSaBfs7MxUhC2ILI7aEtyMqH0AaJmkVHOdlCu32oz_JBmk4cjeuvXuaLZWk2mcsMKmSFB1Rvskp0rBYo-t29BN1GdE35BmDZwB1Wjl1fIWpUrsEvPC54UDq1RCJs6BtWCLTC5QCk1JunI6EJ4Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رئیس شورای سیاست‌گذاری ائمه جمعه: از این پس، نمازهای جمعه «خونخواهی و انتقام» اقامه خواهد شد
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/668563" target="_blank">📅 18:42 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668561">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">♦️
ادعای نتانیاهو: ایران «قطعاً» دارای تسلیحات شیمیایی است
!
نتانیاهو مدعی شد:
🔹
ایران در استفاده از سلاح‌‌های کشتارجمعی هیچ ابایی نخواهد داشت!
#Demon
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/668561" target="_blank">📅 18:35 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668560">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
حمله هوایی رژیم صهیونیستی به شهر غزه
🔹
رسانه‌های خبری از حمله هوایی رژیم صهیونیستی به خیابان «الجامعات» در غرب شهر غزه خبر دادند.
🔹
تا این لحظه جزئیات بیشتری درباره میزان خسارات یا تلفات احتمالی منتشر نشده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/668560" target="_blank">📅 18:33 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668559">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maa3iuBlSKAgrlDnRwm9MO3EwZFRWjoE52999GKkvuF6AznHcw9IGIOlxcHTzAE-3BMCFK-p7frWZFMm3SkgVcroaPbvfxs3phe56GAKGPAYHnnklQo3djb4YVZIbasUSSJe987YKTqxaSzPMil5GIQdlN8BwjBGYSrey53-JhHRgLujtb4MY9eUVcnPgu5JfzGRfMEKyZJOemXclNHtlrFhP0iGtn_mQf4A8v3OG5jSiW9CV8EBRw0Wdz-DCq9TPJTzTuAlucy9LN7VwHqryFefWEQnm6TEdguk-puQgIJB1-5NKGFVnNxJVkFSYVwWUe2t0fBo_0YSpC__PApfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرزند ارشد رهبر آزادگان جهان در کنار فرزندان آیت‌الله سیستانی در انتظار رسیدن پیکر مطهر رهبر شهید
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/668559" target="_blank">📅 18:31 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668558">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rmgure5C8UolSGikSXspjHOv9cXmobg4XPVYqO8EZep092iCOr88-SP68jloe3YFH3nB1IdE6DR3CPxJqffWGmVugyUHMAuHQWaPy1JDw0Dke85Gq2T5ODrFb_8G1h8nnACFbhFkldPqfcxIJE3b2-jRxNuuD9v4q9tQCKZ9CZ1do5jsNnrZAwkI7R2yA6LUNRBDSk50FJW-ubJ1mgJ7_QMiZROlAyMWfLmIicgIzhKVnD3CkvrTajfJqOMaEa8vux1bUpJdZ33Cok9Rg_P5qAecFqgh4VCmN5PrrwwM-PmBjQuuMnqz9LMvJBsSk85YWXsO3oydoKdXHIAa3kcv3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت به مرز ۸۰ دلار رسید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/668558" target="_blank">📅 18:28 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668557">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
سی‌ان‌ان: توقف عملی تردد نفتکش‌ها در تنگه هرمز
سی‌ان‌ان به نقل از مؤسسه «ریستاد انرژی»:
🔹
تردد نفتکش‌ها در تنگه هرمز عملاً متوقف شده است؛ بر اساس داده‌های شرکت «کپلر»، امروز تنها ۴ نفتکش از این مسیر عبور کرده‌اند که این روند هم‌زمان با ابهامات پیرامون تداوم آتش‌بس ایران و آمریکا رخ داده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/akhbarefori/668557" target="_blank">📅 18:26 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668556">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fdc8e6ccb.mp4?token=bRybzropB3b14lEHiX_bnnpn9weA9cHDc45D0XoSNMRY93yoHFP_Z8GdVYa5nYpPbxO9bLR0Yxa0wglRrDVQjF42LRgnp5zkwI0HJdzAwPBgscVkSw4K41rZf0B7KTnJ5Y_YMQns0XybdouDKkIncXkgngpqGMVtc9I2DWszOxOBn8yLM845riGoeEPsdzFqPOihsmj5qdGiGmFe4X78h62OZsc5Aa3UgHF5XAVWIFEaFMZmQYOvBzp5jOcfSoBrDDAMqEOnLxLPt9PHqTn_81mGoGM05K833VB7weN7USJ8OPM5zcsU9reUoHdvcHu3n39mGLIuQWv91nhZEQljXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fdc8e6ccb.mp4?token=bRybzropB3b14lEHiX_bnnpn9weA9cHDc45D0XoSNMRY93yoHFP_Z8GdVYa5nYpPbxO9bLR0Yxa0wglRrDVQjF42LRgnp5zkwI0HJdzAwPBgscVkSw4K41rZf0B7KTnJ5Y_YMQns0XybdouDKkIncXkgngpqGMVtc9I2DWszOxOBn8yLM845riGoeEPsdzFqPOihsmj5qdGiGmFe4X78h62OZsc5Aa3UgHF5XAVWIFEaFMZmQYOvBzp5jOcfSoBrDDAMqEOnLxLPt9PHqTn_81mGoGM05K833VB7weN7USJ8OPM5zcsU9reUoHdvcHu3n39mGLIuQWv91nhZEQljXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آقای شهید در مسیر پیاده‌روی اربعین
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/668556" target="_blank">📅 18:24 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668555">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j5Zl4Z8s4-iBISZ-PPcHJZ7zqAHKC6lXueR9X2kpMw8gnrlarTZbwA0PT2QqyMjyjpjmSYfCEhZVuzmJRebY_XFlI6glqd4zHpASHhNEVLMk9WZA_B28suKsM_Yp4-SLTAotKCk0_iOzYKRitqnGNhVIfODhVee2wKzJJiMIzHfUFmJuxG92jytLRLRWNYErLswDI619p5YdjlY5JG2Q8vius4QWP9Dof6tyGpQBnRLzYkS98aYDb5cfU3DS9laga9bqZ-fO6hB86LkWF9ayNOlJgnn5acH2WPFno1KwaQUg4P9dyfKNKJuMx6I9ovKgGtUZs_FWvh4AcZSKTaVdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سقوط یک هواپیمای باری با ۵ سرنشین در دریای عمان  ادارۀ فرودگاه‌های پاکستان:
🔹
این هواپیما ساعت ۲۱:۱۸ به وقت اقیانوس آرام از شارجه به کراچی در حرکت بود، که مشکل سیستم ناوبری را گزارش کرد و بلافاصله توسط مرکز کنترل ترافیک هوایی کراچی راهنمایی شد.
🔹
در ساعت…</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/668555" target="_blank">📅 18:19 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668554">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55e7da8d03.mp4?token=GhSTC5aVHW--JZpBR2_XP-lO1qMeJ9N30DlOSyzVmZxOB-3Tcy-AS4P_YKhme6LSMLgh3GJXfpQsDfxtSwrp_mV3NsgTpbUdZIzTdh3BNMXONvej2_hXNfS8j3Io5dqMFirw25moAVToFx9QoZed0JhqC_hMWvk2wmcLK6y7JxVUZsaGdqhJXxY9EPW7aYcwTRXjFOjsEI6rWBpBTJfRlS6R52XdTWMl3ORKKHf_B-VBnbmUAf25R9nFm085_Ui4pfmHCyKed8zVvp9mZHyTCGkUBTrSazmpDQ_QaxTW2I54Fj01ulCNlN28up464ImQaLN0X8-i1eMrQLLf9s1Esw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55e7da8d03.mp4?token=GhSTC5aVHW--JZpBR2_XP-lO1qMeJ9N30DlOSyzVmZxOB-3Tcy-AS4P_YKhme6LSMLgh3GJXfpQsDfxtSwrp_mV3NsgTpbUdZIzTdh3BNMXONvej2_hXNfS8j3Io5dqMFirw25moAVToFx9QoZed0JhqC_hMWvk2wmcLK6y7JxVUZsaGdqhJXxY9EPW7aYcwTRXjFOjsEI6rWBpBTJfRlS6R52XdTWMl3ORKKHf_B-VBnbmUAf25R9nFm085_Ui4pfmHCyKed8zVvp9mZHyTCGkUBTrSazmpDQ_QaxTW2I54Fj01ulCNlN28up464ImQaLN0X8-i1eMrQLLf9s1Esw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عشایر عراق در حال تشییع پیکر رهبر شهید امت در عمود ۶۰۰ طریق نجف به کربلا
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668554" target="_blank">📅 18:16 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668553">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">♦️
تعریف و تمجید خوک هار از الشرع
🔹
رئیس جمهور دولت تروریستی آمریکا در دیدار با احمد الشرع، رئیس دولت موقت سوریه گفت: او آدم استواری است. او رهبر بزرگی است.همه به او احترام می‌گذارند، از جمله من.
🔹
به داشتن او در کنار خود افتخار می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori…</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668553" target="_blank">📅 18:14 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668552">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/328871d827.mp4?token=J64WH8N3FtfHQ5bb_nqPXBDA7j0mcKtu8QD3FKOdYLdn3GhRQA_rAC24-U6HeGoxWWD1UlBCwnnOww1Gi6XR6kgwpruwcvzpwyfC80rwqbVIV92S_JK9lDDf8pN98nRchd_jlJpwlnr76x3wCk19WNVTmsqGo6ha6YtQFBAib10ucY215N1q43lJG4pxH6haLyU2AHmuTLFNoc8nYfRdS8dcGNPwXMlcRoJwhBkqvf6EVWkdHcHmiUxCDthSuFTGuBJChQIeTQfppHhlL_HXXnYLkBw48el_QR0sdDvg1snR6A1vVUIbEKrjnzSqSbeumf3Uwwy0szK_xpNO4FcblA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/328871d827.mp4?token=J64WH8N3FtfHQ5bb_nqPXBDA7j0mcKtu8QD3FKOdYLdn3GhRQA_rAC24-U6HeGoxWWD1UlBCwnnOww1Gi6XR6kgwpruwcvzpwyfC80rwqbVIV92S_JK9lDDf8pN98nRchd_jlJpwlnr76x3wCk19WNVTmsqGo6ha6YtQFBAib10ucY215N1q43lJG4pxH6haLyU2AHmuTLFNoc8nYfRdS8dcGNPwXMlcRoJwhBkqvf6EVWkdHcHmiUxCDthSuFTGuBJChQIeTQfppHhlL_HXXnYLkBw48el_QR0sdDvg1snR6A1vVUIbEKrjnzSqSbeumf3Uwwy0szK_xpNO4FcblA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای انتقام، ‌قدرت تو را می‌خواهیم یا مولا؛ خون در برابر خون
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/akhbarefori/668552" target="_blank">📅 18:10 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668551">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2p_jhttze3YMAdT8yy8pBYKb_Hgv0KFjCQnmXZmwLMIUWHHsohg96vCW5-4DV31FEUs4FUpyUp93UhK8u8rSBb7d6B4mkCoQb6xTEiWg5Qz0HOtddawPu2L7Yig3hESiMTnHzrkF7aiL_rYSw8-C6N9BHm_z-9QjwH2qdx95nywSgQOVQWbKTBBcXTuzl-wtpI_fYmmZxPWqJE-tVl2KYPxf3NCRpexv8wMkLBJJbTEXdSVBecedWoDJGIxQi_-3Cg2dHPSCSXrqltKo6wX_4NgBfpyyHRzwUTHoIjIT2mLWr06oa2_UCqI2Dz_18sozMp1Q_PtqS1VITXqP4uR4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
تصویر رهبر شیعیان جهان در دست نظامیان عراقی‌
#بدرقه_یار
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668551" target="_blank">📅 18:09 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668550">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
خروج پیکر ابرمرد تاریخ ایران از فرودگاه نجف پس از مراسم کربلا
🔹
مدیریت فرودگاه بین‌المللی نجف اعلام کرد پیکر رهبر مسلمانان جهان، عصر امروز و پس از پایان مراسم تشییع در کربلا، از این فرودگاه منتقل خواهد شد./ خبرفوری
#بدرقه_یار
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668550" target="_blank">📅 18:05 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668549">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e731519fe9.mp4?token=M5HY7xmhtPkZm2km1lzROsaqNAB8JqB1NB0nltscX-7O1z4nFWIKlX5_d37oulwOTSDwIlodw4B1pr13ePT2kDU6b1o5FDrqnx2-IK7GP4mtQBegtQuW-2_sT5Fz5abpGzuhckTgsTX2Myf2Cf-bh40mteCMvRYeqvKCG7iCKK1rZxiya3o6xqPWJ0xQqc_elQbOAHlggNOY8mECO7Li1l0I3R4GzPTv3vZAz4Ixk4vTe1bt9mJ2nlgU7p3XQjyVATmLh9GvPbqfRLiTsNN6LyOMJZ_6OeYYJtvQRaC6nxBB4xWnwxc5lnaK-Bo1nyzaN4_K-O-usIjWV1hGazM3lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e731519fe9.mp4?token=M5HY7xmhtPkZm2km1lzROsaqNAB8JqB1NB0nltscX-7O1z4nFWIKlX5_d37oulwOTSDwIlodw4B1pr13ePT2kDU6b1o5FDrqnx2-IK7GP4mtQBegtQuW-2_sT5Fz5abpGzuhckTgsTX2Myf2Cf-bh40mteCMvRYeqvKCG7iCKK1rZxiya3o6xqPWJ0xQqc_elQbOAHlggNOY8mECO7Li1l0I3R4GzPTv3vZAz4Ixk4vTe1bt9mJ2nlgU7p3XQjyVATmLh9GvPbqfRLiTsNN6LyOMJZ_6OeYYJtvQRaC6nxBB4xWnwxc5lnaK-Bo1nyzaN4_K-O-usIjWV1hGazM3lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعریف و تمجید خوک هار از الشرع
🔹
رئیس جمهور دولت تروریستی آمریکا در دیدار با احمد الشرع، رئیس دولت موقت سوریه گفت: او آدم استواری است. او رهبر بزرگی است.همه به او احترام می‌گذارند، از جمله من.
🔹
به داشتن او در کنار خود افتخار می‌کنیم.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/668549" target="_blank">📅 18:03 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668548">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9aed159197.mp4?token=He_Rdki0_N42tkHMjo8rtp-hbh1aGqPigJG6Ztrrib2csyxw78GvlzSMhTXZhfhxE6y9HPzpvTvvWa95Yy3oxCflXVf3ezCC9IsCtjT8yshv3VUNJRoSjhcHr7NILXIeByrIsu5d9L_lZ3c9434cJuobwHU2FyXU4IWS-3zzDYIEoqwuCjATCkmNF5G8TES0WUlY2S4ZNS8UN-MA0-WiudferZKzIJhwXmDNA2N4gma_foz1SfA9K129G5MOXUS8Q5nm-js8X3Ne3bduSJjFwV7nNyhP2S2fyJc65IQvxNuEBgbJuT39ci7AUqls4KBHsac1f8vD9_rcxc62KwnIpLneAIb50CWlLfRWJwQRQ7IqSQC-coVaghDTcNkmRu3tOgh3Qt6enF92jBzKrKatCqGFL4TY-UJsuRst1UwYJY0sEXpAAxCxBMyLtHABy6btruHy09V47jyfUR-4K7g5cvEKUrgBazt-qowy78UFNedILaXR5UmiuBSzVO_oBAM3oZLxtmJMDa9dUbtnRTE5yVOHCtRIuTuBxwwyU4Jq6fR7UPIWYmApAmjlbc7zzJG9Q04_XAlidlCZcu_sv7g1xZbMYkPosn3GDk6FjjvLCoxEUvBF01PxIGLPfWGX5HDwsK-CI9usBkm1YzxaJmRaGXcEnaJh3p7YyF1cbvBPUUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9aed159197.mp4?token=He_Rdki0_N42tkHMjo8rtp-hbh1aGqPigJG6Ztrrib2csyxw78GvlzSMhTXZhfhxE6y9HPzpvTvvWa95Yy3oxCflXVf3ezCC9IsCtjT8yshv3VUNJRoSjhcHr7NILXIeByrIsu5d9L_lZ3c9434cJuobwHU2FyXU4IWS-3zzDYIEoqwuCjATCkmNF5G8TES0WUlY2S4ZNS8UN-MA0-WiudferZKzIJhwXmDNA2N4gma_foz1SfA9K129G5MOXUS8Q5nm-js8X3Ne3bduSJjFwV7nNyhP2S2fyJc65IQvxNuEBgbJuT39ci7AUqls4KBHsac1f8vD9_rcxc62KwnIpLneAIb50CWlLfRWJwQRQ7IqSQC-coVaghDTcNkmRu3tOgh3Qt6enF92jBzKrKatCqGFL4TY-UJsuRst1UwYJY0sEXpAAxCxBMyLtHABy6btruHy09V47jyfUR-4K7g5cvEKUrgBazt-qowy78UFNedILaXR5UmiuBSzVO_oBAM3oZLxtmJMDa9dUbtnRTE5yVOHCtRIuTuBxwwyU4Jq6fR7UPIWYmApAmjlbc7zzJG9Q04_XAlidlCZcu_sv7g1xZbMYkPosn3GDk6FjjvLCoxEUvBF01PxIGLPfWGX5HDwsK-CI9usBkm1YzxaJmRaGXcEnaJh3p7YyF1cbvBPUUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریه‌های فرمانده ارشد عراقی در مراسم تشییع پیکر رهبر مسلمانان جهان
🔹
«ابو حسام السهلاني» فرمانده عملیات شمال و شرق دجله در مراسم تشییع پیکر رهبر شهید انقلاب در نجف در کنار جمعیت میلیونی مردم عراق به عزاداری پرداخت.
#بدرقه_یار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668548" target="_blank">📅 18:01 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668547">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from| تهران روشن |</strong></div>
<div class="tg-text">🌺
گاهی خداوند رسالت‌های بزرگ را به دل‌هایی می‌سپارد که رنج را شناخته‌اند و با امید زندگی را معنا کرده‌اند.
🔅
امروز پهلوان عرفان ناصری را به‌عنوان
سفیر افتخاری انرژی و برق معرفی می‌کنیم؛
جوانی که با وجود بیماری خاص، هرگز در برابر سختی‌ها تسلیم نشد و ثابت کرد اراده، از هر محدودیتی قدرتمندتر است.
🏆
عرفان تنها یک سفیر نیست؛ او نماد امید، استقامت و مسئولیت‌ پذیری در قبال آیند سرزمین ماست.
🇮🇷
در روزگاری که منابع انرژی و سرمایه‌های طبیعی کشور عزیزمان نیازمند مراقبت و مدیریت آگاهانه هستند، مسئولیت همه ماست که در صیانت از منابع سرزمینی، مصرف درست انرژی و حفظ ثروت‌های ملی سهم خود را ایفا کنیم.
#عرفان_ناصری
#همدلی_جادوی_توانستن
🆔
@tehran_roshan</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/668547" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668546">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngfXAWA8OHAByhn3BvZ-RL0oOCy6-qVpAtp-9el-B-Scyc4YBEOQAp1MiRrZa0lneJkOYmO9sCJ4hj7ch6c_hDcbIqx5y5cZ6n6EA89u8mP11KCuvaNnSMxMUk9gETC2XJheMESzeax-bP3zkepYSbceRM8OdMlQ0Jn24DvEkLE0bDR5UULSGbuwwA48qM1r7oFf7SlZRzVfhpmh1tgaCZKd5uOXXpJAbp_yk6RMvp2mLt9Po_P-8xzFLza2pKlVA3C01p05g65vBZjGHz30WC7_eYCVdIap_dGXubk-veLuG8R1jZcDididRfaZ3IjzSmVzzaBTWWbclxx70fmiuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚻
مشهد به ۱۴ کانکس سرویس بهداشتی سیار جدید مجهز شد
در آستانه برگزاری مراسم تشییع رهبر شهید انقلاب، سازمان ساماندهی مشاغل شهری و فرآورده‌های کشاورزی مشهد با خرید و استقرار ۱۴ کانکس سرویس بهداشتی سیار با ظرفیت ۷۳ چشمه، زیرساخت‌های رفاهی شهر را برای خدمت‌رسانی بهتر به زائران و مجاوران تقویت کرد.
#باید_برخاست
#رهبر_شهید
#استقبال_باشکوه
#مشهد
#سازمان_ساماندهی_مشاغل_شهری_و_فرآورده_های_کشاورزی
🌐
https://samesh.mashhad.ir
🔸
http://Instagram.com/mashhadsamesh
🔸
http://eitaa.com/mashhadsaman
🔶
https://rubika.ir/mashhadsamesh
🔸
https://ble.ir/mashhadsamesh
🔸
https://gap.im/mashhadsamesh
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/668546" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668545">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=WxdceFCrhykzCRO3GA2MQaD9z6POF28-mJ4D2c-EoqaUbecJdX_fDhCUJql8l_1O8_UZzAWTh-m8alNS6AaZNQ67GKW_Nwkxq23_J23CQ6ueAlFo2eh-x47ZnK15Xb228F47IUu_JsaYA0k3BpFy9w6DgLC_SZoNH6n-sDAvHyhIUrkqLfhkS8zHq8lbj46o_4uAWHZHDxOPfe6C8hQsSHIv3ewzDh7UDzG_t7FwVJpdL43-N7wsSQTYCkgjD7dKxt0Dmi59ysNRmLLbXAwgrXBNqHSBQ49TWfqYBDOsr9god9QvegnBZveT6hutZidOnMJhualZj8phjtQVx0qRWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee1ab04b1.mp4?token=WxdceFCrhykzCRO3GA2MQaD9z6POF28-mJ4D2c-EoqaUbecJdX_fDhCUJql8l_1O8_UZzAWTh-m8alNS6AaZNQ67GKW_Nwkxq23_J23CQ6ueAlFo2eh-x47ZnK15Xb228F47IUu_JsaYA0k3BpFy9w6DgLC_SZoNH6n-sDAvHyhIUrkqLfhkS8zHq8lbj46o_4uAWHZHDxOPfe6C8hQsSHIv3ewzDh7UDzG_t7FwVJpdL43-N7wsSQTYCkgjD7dKxt0Dmi59ysNRmLLbXAwgrXBNqHSBQ49TWfqYBDOsr9god9QvegnBZveT6hutZidOnMJhualZj8phjtQVx0qRWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصویر شهید لاریجانی در دست عراقی‌ها
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/668545" target="_blank">📅 18:00 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668544">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
باید برخاست؛ نه فقط یک شعار، بلکه عهدی برای ساختن ایران
🔹
امروز، در میان پرچم‌های «باید برخاست»، خانواده بزرگ صنعت، معدن و تجارت در کنار مردم، پیمان دوباره‌ای بست؛ پیمان خدمت، پیمان تولید و پیمان ساختن ایران.
#باید_برخاست
🇮🇷
برای ایران؛ برای تولید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/akhbarefori/668544" target="_blank">📅 17:56 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668543">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=ZPa9BqD2cp9FY5f8M3ccFRwm03VVAUWPwBt7OJTCqjmk8_NMZsggaEx9ORhODNGAAjfT5KOR5bjtgI_MAaYgpSi-0fNwcOM6VV7paBR7-8lyTuXxTeycGaMrga3cHGXUDgtQKQXqKZuDXtCeIS8JJijU8688vXz25edPV9QWX7WD2XLbC5gIR2ZtSt1C1PyALR70Aqy17uqZ0be9pt-4Rb5UgVW8jOHUAfJYWLwWCkAIWn6BOUUjUesRQGGuwqA6splldopIKWTHCR_U9uABIYdJgHbjQ7lnXjJUuteBYE3PNblb4emeN8a-7NpAnbpx08W_sCm9ypfmc2dVFrsvzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/36af8503e9.mp4?token=ZPa9BqD2cp9FY5f8M3ccFRwm03VVAUWPwBt7OJTCqjmk8_NMZsggaEx9ORhODNGAAjfT5KOR5bjtgI_MAaYgpSi-0fNwcOM6VV7paBR7-8lyTuXxTeycGaMrga3cHGXUDgtQKQXqKZuDXtCeIS8JJijU8688vXz25edPV9QWX7WD2XLbC5gIR2ZtSt1C1PyALR70Aqy17uqZ0be9pt-4Rb5UgVW8jOHUAfJYWLwWCkAIWn6BOUUjUesRQGGuwqA6splldopIKWTHCR_U9uABIYdJgHbjQ7lnXjJUuteBYE3PNblb4emeN8a-7NpAnbpx08W_sCm9ypfmc2dVFrsvzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برافراشته‌شدن پرچم «یا لثارات الخامنه‌ای» در کربلا
#خونخواهی
#تقاص_خواهید_داد
#WillPayThePrice
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/akhbarefori/668543" target="_blank">📅 17:54 · 17 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-668541">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
حاجی‌دلیگانی: مردم ایران برای سر ترامپ ۱۰۰ میلیون دلار جایزه تعیین کردند
حسین‌علی حاجی‌دلیگانی، نماینده مجلس در
#گفتگو
با خبرفوری:
🔹
برای تأمین هزینه‌های خونخواهی رهبر شهید در عرصه بین‌الملل و پوشش رسانه‌ای نیازی به بودجه دولتی نیست و مردم هزینه‌های آن را تقبل کرده‌اند.
🔹
مردم ایران برای سر ترامپ یکصد میلیون دلار جایزه تعیین کرده‌اند تا هر کسی او را به سزای اعمالش برساند این مبلغ را دریافت کند.
@TV_Fori</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/akhbarefori/668541" target="_blank">📅 17:45 · 17 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
