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
<img src="https://cdn4.telesco.pe/file/RxVfxO9xAD7BnRjBWq4bqok6ZtG8_PGh82EGy-Y3PqHZb-n5n7m5GrHF47ahNlUMBReFklgXaJOfnkuFc66okQHj4P7sTGIbrEMlrOuOcfYVurfqDl13olHVPyUARNkJGLjW_1OUanREo3X13kjnWyF2Oss5aF9YgFdiBPF5TL2NgLh8Db2ne-5AtT13_BgIzE1UIFD6jsuyfGp7ZYfVuLR6fAUENGZ6ukPO6kqkdN0go6l20voKR3i1HKqcUOl5A4vPyhMjDjSuTbl0HOBNaqsjym-IGBj8QTRlfM5yNCDoXKxusz1NWecidnRENwxN-Ma-14PzQDQ0EEsDhHWWbA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خلاصه بگم کونمون پارس
ترامپ میخواد پایان جنگ رو اعلام کنه و بزاره بره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.47K · <a href="https://t.me/funhiphop/82948" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RcvTSJZzJncmUxCtBCXU9Lm9anG6Z5GvPQ6Yfj1A1cw-KzjrWpbASuBTWZ0cEATteKPMudjVvc4CXHVvVxr9bstmxWRFV_6H2jt7LAkQtCNCch7P876ASgFIlxzBr8odyx9KpjJjViTJ3WXX_wGvb4LhrRaiSxnaUbRl-pSQgs3i6E54qfTdmWiC2RzLm0uaEOcrQ4t1MN0dIWuUpxyJiFJmRSwVf8azLbGI_CSDlzr0J7v4lO5E8BVVebx6Wnq_FjfkzSm3RXkNZA-qCfnAx1of8gN5j3bWvhmzJwTcK7FWc89IXBhNegXflOls05vK6JH_2LbL-3i0NQs9SZ7Kfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل دوم این شاهکار اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/82947" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=AuVEFnNZ9Yn8NqqO_oquM7m4LwzSTGUW7TiT7VYZmmwPvERulcOH3T7KvEAtUp14tbnUFRCYPMuy6AXBAVRe1IpaF_rHWEHTOdXGg210dwHKJ37p9UaXMySzG22ycs1H2hFtbOLCfhdeCO0nu3PLanRjuyGu_g5lYkaBwVM6ogzgOi4GJKN51XiEBYsHYRKGxhBIv_BvDkZXppU2bz3AURB21m7-PxJcV9m76iAAS3fJE7jHYXwz1eatHrAIimFiXTscZ8CIZqsmQJllo-ug8PYnT8CqBeW1t-kFwTrps-yHkJSf21C5Vz3RDwWr9EbnwuzGE2ZtGFI5cz3yYOrLdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=AuVEFnNZ9Yn8NqqO_oquM7m4LwzSTGUW7TiT7VYZmmwPvERulcOH3T7KvEAtUp14tbnUFRCYPMuy6AXBAVRe1IpaF_rHWEHTOdXGg210dwHKJ37p9UaXMySzG22ycs1H2hFtbOLCfhdeCO0nu3PLanRjuyGu_g5lYkaBwVM6ogzgOi4GJKN51XiEBYsHYRKGxhBIv_BvDkZXppU2bz3AURB21m7-PxJcV9m76iAAS3fJE7jHYXwz1eatHrAIimFiXTscZ8CIZqsmQJllo-ug8PYnT8CqBeW1t-kFwTrps-yHkJSf21C5Vz3RDwWr9EbnwuzGE2ZtGFI5cz3yYOrLdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/82946" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJBmFbSEERjdmtdCv5ws-rp8fYA6T8Uejcqu2rT1icfug3mc5N-bAuIHBDxl1HQcM7YfWZjML6nODKODdlyjTNqKjqQehvX5TH6w4JivlmtPl-rNpd_XLGGYZOJPr3AtkNj650sxtit75sE84N1IFacRlZBq5fZYC8S-bedMjcBKoYCcT9fYhyvMKVrcQ7XUruQSVdWwV72KvmC-O4E-3sj9nd68OSqdEqyyC9wQy8SbwJoFbraHZ_iRhwzM13q7x4w5eifVQdZ2iS4gs1gvch0bNpGmzglLOvIbYcyVHiYON7tPMh3sTDl8ItJ-m5CF5V7xVYiYYgOpQgbBaDHj2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت تلگرام تو توییتر: امروز احساس میکنم خیلی کیوت شدم، شاید بعداً عکسای نودمو براتون بزارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/82945" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QHmF5j6M3f6z5idsZi--VfeBsZFZAmnXSeb1wo_-14GGRREQd-ttuD2m6kadtFvcZOOTVljvjMouBA4OD6vHkw7nifHKDErvuIrjrz52i5Z9Bb8zdf0-96jN5WLhz6mJV05g781Uo6k4FHPfQAFzAJvDv_PXqXPbNZtJeQcBxx1WZMt7aMkPHjZwS6rptnh1ME_-z11m2vKfvvSdG9738ehDfdxTAIyDiTla59djfjZy_h5XDlQiZGdlC8wOlQMBXwW6S3bhHkjMj2NMufiGyjsUSrsn0x0EDUZk59pTFAeJbn9PNhQh_9GCgF-UBUUMlK0Hd3sC3Vb0jdTfqG0f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد توافق ونس رو دعوت کنید برا تحصیل بیاد حوزه علمیه قم حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/funhiphop/82944" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=OwX1qFM621bZXKhphUoR8BVd53nNYmAUGWDykVO2d7ioRhBY84ocjZJ2FX_ydCmdODREIMiaLCmqTUH6K43mn9kat6570gZG9mm9fS32R7yC7l-lIXVNr7_02dXitMD-PR-n02u23xUm4_cIjNOgO5flr16BwFpeQfkjFCTlZh1huaAFkBNzbdYY-9F23jlzMWik_18cdzfLbr8UoUzCYc8i2xxDGxF24Uhda7sw2vvquunKMp998XLRpT7408sH8RvYxwqP1bzNGeTKxCo1gHrn5k-NHfZDs_Mtubgk4lcwHM59FaN4AHbZNRR9BeI9MMEgGYdQ7lNp3RhYjBuP6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=OwX1qFM621bZXKhphUoR8BVd53nNYmAUGWDykVO2d7ioRhBY84ocjZJ2FX_ydCmdODREIMiaLCmqTUH6K43mn9kat6570gZG9mm9fS32R7yC7l-lIXVNr7_02dXitMD-PR-n02u23xUm4_cIjNOgO5flr16BwFpeQfkjFCTlZh1huaAFkBNzbdYY-9F23jlzMWik_18cdzfLbr8UoUzCYc8i2xxDGxF24Uhda7sw2vvquunKMp998XLRpT7408sH8RvYxwqP1bzNGeTKxCo1gHrn5k-NHfZDs_Mtubgk4lcwHM59FaN4AHbZNRR9BeI9MMEgGYdQ7lNp3RhYjBuP6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بهت میگن اگه ناراحت باشی عامل خود فروخته دشمنی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/funhiphop/82943" target="_blank">📅 14:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">حاجی دوران شهید رئیسی، یادش بخیر</div>
<div class="tg-footer">👁️ 9.63K · <a href="https://t.me/funhiphop/82941" target="_blank">📅 14:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J2N40tyGc9xubw-Xm4vIJGRBojjwj6qdJVpsWDbMGQFwhg1cHIFOClns7TyHfOOe72o2DK9cHomfJBB5CAyLcx4kO_NLuGX177LtFLccsvUQeBV62HUT6R6BVXHI6DW4Q37EQxrEwU-k41zjDe4dEnZaPgaNqcDos7qP13MPyhJslZ1gbqHYHRQ2av2fUFt_y31eOGC63M7x-v-YVSFhByCPcZhqY0qjGO3reughsP8jP5mbopRyhqeVdhTENFPCnGAhVG-SmoQqmM_Ub2evELLdGyDz0hhVrJj-R84sUqcrveZVUKLfM7kk0ZiidHF1fsna3LKvnhjGw3fS8qfNCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی از سنت خجالت بکش این ایموجیا چیه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/82940" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه گدای ایرانی تو ترکیه با  ۵۸ هزار لیر (۲۷۰ میلیون تومن)  پول نقد گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/82939" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJ2ocz8HYYIIaSYsioPbDALynrxTlzPA7wDrfPV7hYRJjUWAbVgZDshNAvYmAnBBl48zVX3fhTmUjpy7wPm-Jn2znbv4mVE4X0A-KvvuPV_HehiTJRKALLIvHANd483P8QoA3CZGYle9rcpxF-J6vS3FDR16KK_5K-8u5V7iUVm9HYrd3ftQSqIF1SXjWl9Uy4pTs5X8Z6477VkQoHljtXzrESdPfXbZvNjGU9WXHTuPvKW89Ivi2Q7W38SY9rFPQ_yX1lNkT4ejWhUTu2ogouhdlQow6_45bfQLuyOTwNEzLGHaI0qKPEziLnSmlCcHNJY_STzBYJQJmnTHojx_yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=t7AIx0uKns3jMahKPLThh8i5Pnu4tD-2SsXg2TK-DiOOgTVXJQngu93-dI8Uy8UiG83olr0CjYq1E0soa5w2DRVm-1oGUU094N6Kd4Q9MxuFIk01j5JgAusWu4Rz4LGgodsUnyjLAVg9LkTri3qQbE0rhBYdb4KZPqpngjBjcJs0n07lBsNhMcXXqOWy9nTXmrIhVy1QkrEV4I8LgWXiZKJjmYvdvBHbePwRqJQjVAaw37XaaZXyR84fl3-5Bxfi7MvGl4SdqhIqtecgSCB5di_d7QJ0Gclmb8M_XbOh5kNrA93TT-cgpqpxARGPRQMuKq8wtbuC6A8ltnfIjL3K-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=t7AIx0uKns3jMahKPLThh8i5Pnu4tD-2SsXg2TK-DiOOgTVXJQngu93-dI8Uy8UiG83olr0CjYq1E0soa5w2DRVm-1oGUU094N6Kd4Q9MxuFIk01j5JgAusWu4Rz4LGgodsUnyjLAVg9LkTri3qQbE0rhBYdb4KZPqpngjBjcJs0n07lBsNhMcXXqOWy9nTXmrIhVy1QkrEV4I8LgWXiZKJjmYvdvBHbePwRqJQjVAaw37XaaZXyR84fl3-5Bxfi7MvGl4SdqhIqtecgSCB5di_d7QJ0Gclmb8M_XbOh5kNrA93TT-cgpqpxARGPRQMuKq8wtbuC6A8ltnfIjL3K-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مسی که قبول کرده GOAT خودشه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82937" target="_blank">📅 11:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw0ejteOcedTZg98ClYVKTgaOEZ4HGEl_YF-LquxpCg6uzhgrj5OJWi1dmOLOP-Zev-yFlP8G7SvftsWsI9geLuaplauRwSFL-Iu8dP2j2OmLlJsHgXPGqfMsrRyfMlvOAy_pmadn4TAHl9JoHExeiVaz1R_Wpn3G-vPfNM0ZcEZwOb5jWgV9_eid3TQKmGhUTBvJisKtAgpzhOFvQqfrX119zhRfM0cwONcSRYlhxR2fK55-HjYYTRIjcY9_cKRKpB7Jz6LhUtz0_rE_pxY_agyiXDCP_PtixNAr-V3drwhq5giYsyRf5UgP1SiZLktK6ik-m0u2jrfc4J2bFvZFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام اینو توی باغچه خودش پرورش داده و به زنش کادوش داد، ایشالا که خیره
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/82936" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82935">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Q2Ia5pUjKLpEXDfZg9CSuPhOsxQj23etoi5TIGgASlpCTqmvkpP9HAziBLHRD4Cg6ddHwuXXgCPb7LfcpVjSw919jfVPjhqJq7TLjDTOBXnVOQtJ5-MDsiiTSVRgcmZNgyiHL7Y5afSloUm_ohX4HC17QFvgFWJlWeK3NiR0fh0CAl_AtVeL4ybMh1H5UNtMcoJqvEatSL5wDx2TNVz4g98Nh1C5KXpOkl6G9IAWFgQl-jbO1VglNFfgp9cPdWXqKACrhjb2sA4vvKc1OjlgFbbDzmLfkol2-yb86iKJNMk95bTJXXexxfo2V3Rg6bjGy6wa938Tz9J3eNe4TLtk9K4yFkS3Ba993IxIigrVyaVEbmHBD9r_tSqTALLqk6scS7JOkuRUHKM70UazhM8ErCIEufAmYM2Q8xV1N59o9ttZ17aUdQEQ7hZ3mcLj8rXT8hfB1lkXZ8R3yQMOkNuoq3MCxWGP36o0AY1R8knRywISUR4fa6jCjVX_RJ044PqLbtDG_RLTtlMNqA2dUbEOMEeFmHhSJ1tpnrFWfaQfjpnzPNzYo8tFVGfZ_E-bKeFDwYnzvivMUc8LC9sJQnyCe86Kncm1TDO5v05vjc2WGiYwgzG6DveLf0lxxYbas3XldaLozw-B-ktfEXct5F59MfT8bNIOIe8McBj3jluu5mY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Q2Ia5pUjKLpEXDfZg9CSuPhOsxQj23etoi5TIGgASlpCTqmvkpP9HAziBLHRD4Cg6ddHwuXXgCPb7LfcpVjSw919jfVPjhqJq7TLjDTOBXnVOQtJ5-MDsiiTSVRgcmZNgyiHL7Y5afSloUm_ohX4HC17QFvgFWJlWeK3NiR0fh0CAl_AtVeL4ybMh1H5UNtMcoJqvEatSL5wDx2TNVz4g98Nh1C5KXpOkl6G9IAWFgQl-jbO1VglNFfgp9cPdWXqKACrhjb2sA4vvKc1OjlgFbbDzmLfkol2-yb86iKJNMk95bTJXXexxfo2V3Rg6bjGy6wa938Tz9J3eNe4TLtk9K4yFkS3Ba993IxIigrVyaVEbmHBD9r_tSqTALLqk6scS7JOkuRUHKM70UazhM8ErCIEufAmYM2Q8xV1N59o9ttZ17aUdQEQ7hZ3mcLj8rXT8hfB1lkXZ8R3yQMOkNuoq3MCxWGP36o0AY1R8knRywISUR4fa6jCjVX_RJ044PqLbtDG_RLTtlMNqA2dUbEOMEeFmHhSJ1tpnrFWfaQfjpnzPNzYo8tFVGfZ_E-bKeFDwYnzvivMUc8LC9sJQnyCe86Kncm1TDO5v05vjc2WGiYwgzG6DveLf0lxxYbas3XldaLozw-B-ktfEXct5F59MfT8bNIOIe8McBj3jluu5mY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏩
بازی Chicky Choice، هر قدم، یک تصمیم تازه
🐔
⏩
در بازی هیجان‌انگیز Chicky Choice در بت‌فوروارد، مبلغ موردنظر خود را ثبت کنید، بازی را آغاز کنید و مرغ را با دقت از میان ترافیک و موانع عبور دهید.
🦊
در طول مسیر، مراقب ماشین‌ها و روباه‌ها باشید و با هر بار عبور موفق از خیابان، ضرایب بالاتری را کسب کنید.
⚡️
واریز و برداشت سریع
🎁
بونوس‌های ویژه روزانه
💬
پشتیبانی ۲۴ ساعته
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r12
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/82935" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VQI7rWtUEC3fEwwytSp3MD8_0AWe1be5CgYhlco3U-rGjeVv6ixwL874ugbW56CVbn82fRGtO5iYbf_6zx0FQNp2UfLzVF_a1lJd9hiQ-HfF7Od--xqCS2Ta_V184XwXVBQvXBZXPhY-ILY6I1NayCQxSjzoiNC-xgHnwhLUiUnDExl9cZW8ffuyxndWYKkdWxvG6uQqAt8CpEbRg4KBgwH0mnJwEC5UD8-kAlZh-GIf6fGcnnm-_02BmZSMlw-1GbN4_ZG6hRb1DKUdFvgVAh4sCuIxGRDG1VGwoxkrZBI0M9CXajQbGli3OzBwS2RQ-SaViGtGSEkUdYpxO5oFvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرسی نکن پسر تو تازه ازدواج کردی
😐
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82934" target="_blank">📅 06:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82933">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=o6dKT_0rFEycwjq1cJVY_hJIniR1GdmsjqLTrOvOOJVJrtCBiolaOEO1oyZaTQKE-zyYDOR2f5FMB95tfM0GWgbQEQzHjN9RpkTq7DTZxHuxs-yD6RoR2BwjKbmBdGctVr6aBX38DZS4PcoOWbsyFvWT_ts3njxEg2nDsDl96F4BBAX4uBib7eCBX7N3HlTD-831IZ_PIZcVTquSSRh615r5evT1hoNj1-80oOouXnIY5qVN6G5WSCYMBe7fXdLUALqtus8gKismA-NnRftFrugsJi7AQQ8tO0F1CLdHUybPZg-Io-dFt4FOoFq_MyNjoSzd5XT9iWFK9E0EeP86Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=o6dKT_0rFEycwjq1cJVY_hJIniR1GdmsjqLTrOvOOJVJrtCBiolaOEO1oyZaTQKE-zyYDOR2f5FMB95tfM0GWgbQEQzHjN9RpkTq7DTZxHuxs-yD6RoR2BwjKbmBdGctVr6aBX38DZS4PcoOWbsyFvWT_ts3njxEg2nDsDl96F4BBAX4uBib7eCBX7N3HlTD-831IZ_PIZcVTquSSRh615r5evT1hoNj1-80oOouXnIY5qVN6G5WSCYMBe7fXdLUALqtus8gKismA-NnRftFrugsJi7AQQ8tO0F1CLdHUybPZg-Io-dFt4FOoFq_MyNjoSzd5XT9iWFK9E0EeP86Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش میخوای کلیپ غمگین درست کنی درست، ولی خب مشتی از وقتی یادمونه این بازی مساوی میشه خب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82933" target="_blank">📅 01:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82932">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hspKDNUoEilkSDh4nV2YwP-nIx5julD3jp2ABw6jVk5liu9FnG0dui_W8s2Q-EDiTEIt-Gniyqrw2fveGRdsygRfWBU_ccEaFpK7OwAQouawcu69fFwTr2FssVLKltGlBBh8Mw0JZI8pgKtdLZrmJ6nYSJk8TVaxEHKmat-KZcsMSsiv-6uOQMPUfxE7YqwBudHjy6KUPS4G1_0mfflnYGdlbGyc9Lgy4k-4IykZ2nG2cFeDVM_5wwXFPptqb-M-5HR0Bqi0tK7iApVAAtyNxq49SNkJ-FNcWxraGq29XMCOjoM312pWEk7tj8Ri4Zam564D25AttAls8UEckHhwRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش بی‌خیالش شو نصف شبی بگیر بخواب، اون بی‌لیاقت بود تقصیر تو نیست که، لیاقت تو خیلی بیشتر از بودن با اون بود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82932" target="_blank">📅 00:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82931">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2ob8kklbwhVFiDV_Px33nwj2y9FzUiqks79kDgsIRLaWB5_bdiveB4sX9tQGyfV80-NEfYClRp194gdI-p5anOVvhKRjfvf5rMBNckvuuuzrByMEGMDgw8NVOD9HXEsptMIaXzdyliaGfC_WDDSMcQAwvxZd3FJZ39kaOD1BmqP4AwL27nS5Zg_cBgiy6MMtSaAFruWAtTfUfay8P5gM5HRuynB3n_LfhEaJkpzeP4BzZSBiuxCH90LFO4NbDl1HDngc08KqyU7MKAbtkgLM321yXTN7kzja1UaOYgGF2aKlI6TWnJzfWnX7mDLN22PQXM-vJUisPwtGoG-m9O7Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۰۳ سپتامبر ۲۶
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82931" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82930">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFiU9nT2bpqldxJxwA3PcNB-xJjBBmuOcP6DQ9AXKs6rmoA5gVEI2m__593_g2FRHDhKqlQx5If87NGu5NFYP4G8VTtfKYn51qh-kPoq73HumK320fsD472b3SSa4bDxESv7YcDmMYOtMFHms2M3oW9R7FcoCG1WeEgoV458Sm87atMD4yW_fP_hleG1-rNfMtw6dOXCjXb0S-CjwFknyWpckO2VjFXCAVdkoCiHlL8hXI6YPdKCMTbaorq6O2eQaqZMDAAWKHW-JSrTHtvpGt7EsndwJAPgwcheB38xz5-D_msX0e2xP4P6wTT1v0xmUb_7pHcTFdTXxiuqnSDeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82930" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82929">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود:
عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82929" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82928">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NvkI13fWwzcX9IynQYmtLeKvuXtPp5wWsFTGLKq8GjmfGbXhDMWQ-OHwWaMUc1Afz5AIGTvRYW12fESBucA2j9JuyvLtXvP-yZEOzrybhewLjBA-Lu_cbNOQ_6CGIH180m7qTo7_ntis_aypYbtY7zHnKKME4tdZUOoshSP6Es0TIqTENZpmN1mZZsigCKBPDrfoOttk7aM_OmtgEcOY0VPLezQmd5oiCU9luSCybTSNrofenylsE-_nWmC_zWqKb1DEjUFSLgRip43tdE4VNdv5rnySK9mYw2o17G3rvAuf2VocnI0edmU_dLO8tSy1838Ha5CPWZh7TYl60XtvuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این پزشکیان بگه یه زمانی همین روسیه نقش آمریکای الان رو داشت اندازه دو تا اصفهان از ایران خاک غصب کرد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82928" target="_blank">📅 23:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82926">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پزشکیان خطاب به پوتین :  قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن. حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82926" target="_blank">📅 23:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82925">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82925" target="_blank">📅 23:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82924">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لطفا موقع بازی های حساس دنیای فوتبال، شو های مهم و حاشیه های بولد قیمت دلار رو ۵۰هزار تومن تصور کنید، تا کیر نکنید تو مغز جوون ایرانی ای که تنها دلخوشی هاش همین کصشراس اونم چون دلار گرونه نبینه، نکنه، نگه و...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82924" target="_blank">📅 22:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82923">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سیگارا وینستون جدیدا بوی پهن گوسفند میدن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82923" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82921">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ATDziInGVDPgN8YjcnYijpWhV8r9wtiZq2xIPYUOXB_DyOn3cKfVJcQB7KwF4ZrJoaAtcxTxoXCbjEYwx74eZNeSGhGxOMbY9-xU9bpfmUgzcLZCva94wXjaue2EUe0KAUg-ToaqC9gvo_iVj5xW9SUDJmmLYQ_KzGLzE28Nl-y3JLPg4g8ywOd31Gpsf7V8MwpuqvdV5zVKDDmsYCMG4nwRK-9QsIsP0R0n78j9mWTzqoU2ufV7chAzwmQskAtOcw_dTNrxbb_4zqB47z7yV8r0k7evh6eOA2SG7YACXBNJTRL3T7JYyQvOWSBVenJjxG2WVAHLJtpB-9O66zEyWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Exp-2CQxWIY-0rPDpHTW_GHoF2FRdn0BY5E2Gqy1J-N5KN3_TOFqEuPt9mS31clAWPcTZUbCXDsHpi1JS0lu5H9TcdyHBZItQAG5m1Og2gQ__rYnWyvv3y_X6aNhWSgIQZr1jATnij3ecvoaw3kv6f1CBrHlZ5GVHWrykxg62f80uZEQdJG17oUyV0TCZWmUNqg-tHIakGvESquQfZrUuE9oACTlHRo2TKPsw3EEassYO_C4Tvk8dcHiacYwnWV1munPqZUJ1tUXReIb6TjzO24Zl9NRNNBkUPLOFakPhXguFXykppwaq3MVr600WvoF3K6ySpIHxw_kwJ0fp3FLzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید لنا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82921" target="_blank">📅 22:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82920">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خلاصه‌ی صحبت‌های امشب دونالد ترامپ، رئیس جمهور آمریکا درمورد ایران:
تقریباً سه ماه پیش، گزارش‌هایی وجود داشت مبنی بر اینکه ۵۲۰۰۰ معترض کشته شده‌اند. و اکنون می‌شنوم که احتمالاً ۲۰ تا ۲۵ هزار نفر دیگر نیز به این تعداد اضافه شده‌اند.
به نظر می‌رسد نزدیک به ۶۵۰۰۰ معترض کشته شده‌اند. تنها توضیح این است که آن‌ها مورد اصابت گلوله قرار گرفته‌اند.
این رژیم روز به روز ضعیف‌تر می‌شود و به زودی به مرحله‌ای خواهیم رسید که دیگر نتوانند به راحتی مردم را به قتل برسانند، زیرا فکر می‌کنم مردم دیگر این وضعیت را تحمل نخواهند کرد.
اکثر حکومت‌ها نمی‌توانند این‌گونه با مردم خود رفتار کنند.
در اکثر حکومت‌ها، مردم تلاش می‌کنند، استدلال می‌کنند، صحبت می‌کنند و سپس ممکن است یک تغییر سیاسی و انقلاب و کودتا رخ دهد.
اما در ایران، آن‌ها مردم را می‌کشند. وقتی مردم برای اعتراض به خیابان‌ها می‌روند، آن‌ها را می‌کشند. آن‌ها با مسلسل و سلاح جنگی، درست به چشمان و سر مردم خودشان شلیک می‌کنند.
خبرنگار: اگر می‌خواهید مردم ایران قیام کنند، آیا سازمان سیا را برای مسلح کردن ایرانی‌ها اعزام خواهید کرد؟
ترامپ: من نمی‌خواهم در این مورد حرف بزنم. دلیلی ندارد چیزی را افشا کنم.
یه سری کصشعرم درمورد حملات محدود و تنگه هرمز گفت که اونا ارزشش پوشش ندارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82920" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82919">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چقد غیرقابل پیش‌بینی</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/82919" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82918">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">0.000000000001 ثانیه فرض کن لیگ ایران ببینی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82918" target="_blank">📅 21:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82917">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این دربی با اختلاف بهترین دربی ۴ سال اخیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82917" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82916">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">چه موشکی ول داد یاسر آسانی</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82916" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82915">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82915" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82914">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QnKgMwqxNTf6ZYEazAxD-MVDH6IqOMfnSimmBeJXNr2b2aCwRycBx4Nd4gx2SCUU1QmX5nKCqDkzIEKP0rX3q55wMn8fMRzpdxSj_KeC5QG1_VBY8xTs2Og5qlbfrDVLrktPlsl-FnsTyoW9b2wfWzDFyPG0F93OO-ptgGYKRp94Vbl3pTyEs-czhhqbFRWbdIY0TL9YVUTdgbWeFMi6CZtb7rroQVcqJjzvh1qB8xQi6zJwhdZ4i8-NQVx0Bh6gKOWfqHGR7YcPHqTBPjhT-Ewgnv0IFubN5rkBxuq954ktkSiHMyfy6aPX8pIPPkfADYNYqheGbSTLwOLQ624bcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82914" target="_blank">📅 20:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82913">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzM4NCx6ZwxTiiRsstLeZuyhQpl1pJu0IS4B1E8qSgbfFIA0x-ZNlB4t9bXk_ZV2DusrII4Ok9BbrR9fyGVAc2Amg3PlSeTOpeooYf0q2fTxCUdGHhEDtpISwOIyuys5GaJic_9EbmwaOVRH_ep44dBTn74OdQPr_LUSrQoK_YmGaw0gFh2WuklCqPPmakuJ4EYxrXkrc5RBqajEC7KYSMVlgjVi09FsyiY_m0YvSMflantSqB9yuOx4Gf47kzt1hYuFfoXp4V7ZmjuNU3agi6iqosAR-YWCmih15PRx-piyqqwSefTtYShldlmCCcwquYr2k8hrmk5_jQbwRhRWLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکو ها جذاب تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82913" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82912">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OV24eqdHfqCx9Y0vTJAbJBhexgGInqo_a0yjS1zE7WGbKtX1W2eJ64catJOhDDAkpQdFppthpBUE0tjpNfT4z7BZIj4T3LgEaGMYfPoUUwhrEtAe1YAy0WRr4abC9LLJZbYd3_LaS0KChFy9n4v3J1_tnqF386eMWI98upo-w9NhHEfTWcr3lLLX5y8a5hnpHAJ9Ch3bIO1iv63YkjjYezfvJd8Mktgc7IilBibW35eu1gPNlKHRdqQZe81c3MAiHQAyLE4hS8wKQPVOF3sqCYRXapl0spX64c55CzF_VgBMHDTWJE1XslZ0_Hf9RN5_PNxpGdNP6z6hru9Gnx37pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت استقلالیا از دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82912" target="_blank">📅 20:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82911">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">پرسپولیس از کون آورد که نیمه اول مساوی تموم شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82911" target="_blank">📅 20:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بیرانوند کص ننت</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82910" target="_blank">📅 20:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خلاصه دربی تا الان: آقاسی به علیپور میگه بیا گل بزن علیپور میگه گوه نخور
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82909" target="_blank">📅 19:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">علی پور
😂
😂
😂</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82908" target="_blank">📅 19:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82907">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">موقعی که پزشکیان زنگ زده گفته دربی باید مساوی شه صالح و آسانی دستشویی بودن فک کنم</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82907" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82906">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aS6gGjS2upJ5IwXrOj_ZdNdgQ_mbZAQ3fZbhEjP2jAqTLg-dM0eN8OaxdpinHZzORE381DiaTjxI4KgWNjnukg4Yg0Bt-pPR7A5Bz-65dZ1WkAALcRY8EOItuOAH0oEMC3S0iym4gS_vAlHb466Owg5qpKo-D_5cMTuBLMDzf3eJuzjuKaYhEWdaw13fHvSnBDG1Y0qDwr0tdbpGMFr_lzeiFvmUfoTgMLlGgbExwc5uYQqf4Yq2P3Ekj8Ks9VB2zP465pETo8YFBYOryfOI3HDc-U9sH8MG69N_u553JsChp3_mHb9xBLTl9C49Hx7KmcmvkryP0D8BSW96ckzdDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا مناطق خاورمیانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82906" target="_blank">📅 19:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82905">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد    YouTube  Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82905" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82904">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjM11XoqbphBZ0LMd4TFLX8tiAK6zlwip64KM51_PUyKOqkbN-gTOhyxJzzv2VNEE2CY8MWVaeorNie_DMrpzoD3jYvI0AqnWYiQwT7esBJRUZMMTNlLO3LgyCHnMkk45CVzsJB8sR7oVz6wblVZE_8fbFJLGMFZsFOy8hH4BjEdlELwkrNlW9Ts1ktFd5Q3zyrgf7DUKN0M-TEUa34aVV9a1XJ8AzzkkhM3TdyVQLLYaa0AHmAwYWIH5gEGlzXYKOu3aNPLSTinUQVoTK2I33d23RfDd3EOPephuUDtSJuzmKpp_kKoCwFHEIT3cpJdlUds1HhIJAkP78rLQdCUrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد
YouTube
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/82904" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82903">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آرون جزو معدود دلایلیه که رپفارسی رو دنبال میکنم هنوز</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82903" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82902">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82902" target="_blank">📅 18:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82900">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vKcMjSOWELu3KToDWF8XV7WfGpFFrvdL4U0An2UvyB6xaL4xv0BrDF2LhGJ0wla4Aawf2oPs6DFx4Q9tyMRppNdYNn6asiHU0qcySOcb3nhRgR24QFbsVi1FqgLe_dQNGMEYDQUYoR-CT6iStIx4P_smrjr_SHv5r3wRWyRk8dQ_yQE0J2nmD1SC0ryg_hVyNxQzqRb9N90jG8FDElKl3nycV9-Hj-VllWB3BpVhE_Q297W-hlnGLEajbNma9uZjB-6miDTYgbqLaSCefbRbyI2EIi6qEsFZ1hq0rcoVrl7ymaS5qI0R4rT7uKQRRKAhDo0203N55ma47BsFjHde_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lJ2fwuu3JO8ywWyEZnpp-U_yNW2jMHKeFW1_KZhFywzte7hWz1Aw-DHvzoX5hd0SnKNbx47da7NP3Rik7EIMHcR2hU2Tjd55lp5sMneRg-lwRGsEaP0GwCPgB1MO-i9Tom-RZKbvZjHiwi_7TyzJ1RS-TfWqfJ8ukIoxvKfHxnBP2PZH5TNujH7fTS-s1pDo-b5P1Ifh75Ij8fc3wZP1-8TqwsYVZ5uODu76G8cBhjIrjHKxtbNtcdS3veze6-Hyfqb7b7BXImag_iN89wppH13f-zhAc4SyuW2VZNSdA-VK-efkc3ZIWjDJRcCnHfPKDhEpcGY02YgmctaPfb51tw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82900" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82899">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L0HOkodQfAiX9gORq-KGyhHXKkQGKslLn1pEDIiFZ7ObcjKbi9kdU_Wjb_wV84orM40SGtowZMO5zkyXZ1dE5jJY53UWk_0GpT4iXRhigONwV3vuyTCiYZNi3vUHe8pHIiVPitIqansqZ4TddirL5BfRduedGqoB_NTsp3eT4lyUE2jZQo_DvuaScHAJOLGumDneTRc8T1LyCU_WKTahkg4hqkmS8MWsGLAsAL4Kwfot_fRxN_Ckb98XKK7EOrwgq8QVq1HDDlNjir6qFhMd_sK6FX2RsU7ygQsbnRRY1X7YHkmB1SL-nXNxQiar81Dnv2vCcQi6fR6t_vPWB7bl1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استقلال
🔵
-
🔴
پرسپولیس
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
چهارشنبه ساعت ۱۹:۳۰
📍
ورزشگاه نقش جهان
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
استقلال
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
پرسپولیس
:
۴ برد، ۱ تساوی و ۵ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر استقلال: ۲.۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر پرسپولیس: ۲.۶ گل در هر بازی.
🧠
برنده واقعی کسی است که بر هیجان خود غلبه کند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g11
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/82899" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82898">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">جدی نمیدونم تا وقتی رافینیا هست انسان ها چطوری میتونن فن بازیکن دیگه ای بشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/82898" target="_blank">📅 18:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82897">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPPlhEIZlupnAkKzwKKpkEYeOHWjKXJNd-4ZD3_8jr2ajMl7zp-MglFr5f26bOCE15a_qt--s6b3IHTddEs1MoKqOMIKjgtQJ2qZcYpLyM6Wl9Sz3NS1ugbS60IIA9lArs8XsKXwpkKNZbi3seG6zTIbzz92MDiHYBEggtOKtsV2stBZd2ZaN9tf8D3KGZql6dzalz0RwNfz0ypbxdzA2WGuN0_pxaUOfgxcLuz9zCey0lfFa3nwL5ByKmCNDJZo_PHOaerz0PRNw4BC5JB-pDkuUR1Ej7RsjWrdrpZii76owWMjvqt-CPVpaubD1i5AIqZv4ca5RYuRGHndjPzdig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82897" target="_blank">📅 17:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82896">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دربی ساعت چنده بچه ها</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/82896" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82895">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خدایی چطور هنوز فوتبال ایرانو دنبال میکنید</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82895" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82894">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82894" target="_blank">📅 16:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82893">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شب هالووین امسال آلمان قراره یکی از ترسناک ترین شب های تاریخ خودش رو تجربه کنه.
کنسرت مشترک عرفان، ریری، هیپهاپولوژیست و ایمانمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82893" target="_blank">📅 15:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82892">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دلار هر 10هزار تومن که گرون میشه ویلسون 10تا ویس میگیره میگه "شما رپرای اونور آب اصلا چی میگید چاقالا"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82892" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82891">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">امروز در کنار دربی تهران، دربی شمال هم بین نساجی و ملوان برگزار میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82891" target="_blank">📅 15:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82890">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82890" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82889">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/itCP0ta-N564ymxcwMcA_WvVpw0ktZF76QJpN5CI_t_RW_hs9hkeFyuCgdxPCdtoy-X5kpi84VV0tr_2h6gMUjFYFWR9jrQKx_rAK3o19w48yTTAAv3_7YzP2WBkzD3vpdhOmQuAC_pzFupZtWrljnSicVAI7Mc8pe2Jl3cUjRrvIZ9TwE-Ec8N3gnyNiRB47mdlkfD4-N2srASzCEk0ZJt_wc9PrECf83oWVecWaeqCmf2DaQqzNzYqXtjagZAziPu59PTYUjsimqNbOkb33lWSmnkTvQ23lWbC5wbVMdrP2adv7jXFYVOAmf-Q1MSJ3hGHby8Mv6GlRc-mCWGJIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82889" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82888">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">فان هیپ هاپ بابت تشدید تنش ها در خاورمیانه ابراز نگرانی کرد و خواهان توقف حملات نظامی شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82888" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82887">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">شاید باورتون نشه ولی زمان اعتراضات 401 دلار ی چیزی حدود سی هزار تومن بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82887" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82886">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W5-e_m9Aa3_9V3FYqLOgrgQnIi96VTpjZdHEhkEhoprSXb40pf8XiQipL6Qj4Ui6H7I9NXm1xLmjzhNU3IzVOEFPTxw3k98JW5Mj2C6AWCejrR52haFV1F9njsn3DKwY9GYY34WhbnPH6t3GUSf1KWZ3ddnf7PjC8qmdJgtrlVW_1w-VC2r1oyAhM_me2TX3cb0mV2b0kIF_xtQKKA7ape8bFMuCfmuReMJMNMlCnoWrFGNRDD-OB_kyZPfe_QQ0Su5qjr5KTJH-UCdDHl9eys_nFIu4XdFOP7Pm4FMh1ksRABuDAtKVxCGLNwvATkXuaVmnEKUCujJY2kHKUh7jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مال دیروزه امیدوارم الان گرون تر نشده باشه
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82886" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82884">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNDi59Nm4AlVi0rqgCElqPfrXATwaI5j9uYqcQMxSAmeWXqrkzdzqRjtwm08zk7lzekPznrQxaCq1GOJIotuJ_1nthI8WhQtt81e0yRFmi_m4an68SaXHMRExMbmk6SlPb3PS-LMmg_3Av07Gs1DzASaQAG96sw9U3PC4-YBsuJ3yH9I3No7AfInBjLd6x6hkGW7vakaiFHbJV8N5ZpeZoBNqszQEgR3FEkcw2mTgvugcOLT18d-BD5NOGdQI92VfBX-y8by_-1oOmOCWG61P6JQ1lvHukehWvKHcefwp0jX1M4l9d452bipZlaVAufOpeIBP0_1wW5gp01-AARsVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
استقلال
🔵
-
🔴
پرسپولیس
🏆
لیگ برتر خلیج فارس ایران
🙌
🕔
چهارشنبه ساعت ۱۹:۳۰
📍
ورزشگاه نقش جهان
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
استقلال
:
۶ برد، ۱ تساوی و ۳ شکست در ۱۰ بازی اخیر.
✅
پرسپولیس
:
۴ برد، ۱ تساوی و ۵ شکست در ۱۰ بازی اخیر.
📈
میانگین گل در ۱۰ بازی اخیر استقلال: ۲.۳ گل در هر بازی.
📈
میانگین گل در ۱۰ بازی اخیر پرسپولیس: ۲.۶ گل در هر بازی.
🧠
برنده واقعی کسی است که بر هیجان خود غلبه کند.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82884" target="_blank">📅 13:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82883">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oibkTnt7dmank_QI_7RoTGlni9w_UEBJpqqkpfV8Cd7ERJr-B-2jbbxRDA_eleHLVeJtHdkNL1xh6S4lFtx_BIkNb_nC_sCtR73QtCbhK_6NCB0kSvwiP8FkTt6PUyQUfO695fBfgqsHw4H285iczwK8zZzsJCDE-mepZsbKO88nfkzVcSoeVzTVzVawIX9Di543X8KcWkuIQRiPqHik0DERRXmsXrTaVNGtj5QKRChAVLJAK3W3hydDzQf4xfbOIAEDMOYuCrPsYnwKl_XOJl-0cbr3vFp-9OC6385ZJASgr_dtGhB0GzMtSmP7fNnY_DmuoI1tK7u5dutYiFr8Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان حاج‌رسولی‌ها و آرتا میرحسینی به نام "مست سر صبح" ریلیز شد.
SoundCloud
YouTube
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82883" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82882">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دلار 222</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82882" target="_blank">📅 12:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82881" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">انشالا هدف بعدی سر زمین فلسطین اشغالی باشه
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک‌های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82880" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تو وکیل آباد مشهد یه ماشین به تجمعات شبانه زده و ٢٠ نفر کشته و زخمی شدن
یه خبر دیگه هم از شیراز اومده که فعلا تایید یا تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82879" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82878" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">خبرگزاری مهر:
موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82877" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82876">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9oL2miOwom7AFtbIpI6iQZqHwRYUS5I4gOJw77bY72fOITdL_STcSFU8EfirdUClLlDWLobjkmKmj6AuaeteL1VXWRqe4Z_9q01JTGn7oNZF-uKHi-7yce4xS-Pfl6v21WJVuNJvmDyJg045b1Jt5PajjXiu7eawPO1yqquhzhFgKn8BvWRqp3oIjBoDaAUMl0xVUhGTvBqYonIoA95cLKW472PsQPjQ1Y8G4Op5X0yK0NExH4nhmOe0xZcRZcUXLYObNkPQLPJeSZbp6r9_ohbAB4vVKFCybM4tcqLM0_O5dzAkMNBuR_yFrwU3tIoPhQN3czD2F4oswxejYr07g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیب ندارە قهرمان، تو همین ایران خودمون تو مسابقات مسترخایەمالیا شرکت کن،با ترابی و بیرانوند و خلیل زادە و علی اکبری رقابت کن.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82876" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82875">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdkYDFNOTJ2O63E4z8lcjV24dkdm5kImP9-_gug83Q6SuY3JNQUgweQvAS4N9KMW_O7CDI_SdswyA2l8qqmLgSYB6l1_8sR7UIW1s0kTWTCNJrALTL3dmOVyvye0WNwAgGn46sNHvE87GNB-NhSd3u7-iKuK-pT4HxNToi_v2zgJ4dRb5eInzVmeKth1n_mjaKYzM97rswn69wt0cdU_4De1YHGC6ZXpBMEQH0giNt6fiqlz8UiDaOaLSl-hbZFi_GtR1V3_NcKIudmEU0yzXxZiHobRZx065QKzySAwVKGEiKjgjY4H4KWOxUOCWVogTF_uSPCsnNw7T3VuGIRYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر خیلی خوبه
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82875" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82874">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEp7Rw9MPwoJ0GwMh5lyJXT2PzEYphPzJ_NsIvh55M6eocRhuJ55E2-_varfiL4ud4RQpTxASWbWq4dwQjTyU4ab8SU4jI5sJwi6uuS3LkqlFtZru2oEtePWVrYRNTtfc2j4ycWmed5DG2-Wlw96iLGx5iZ_0WyTnMMirselsxyKPL9L9lVPOrNu__euZhC6FTKosGnZF8xrkQfQa_z_94xXIoc4-ZXJGphcwclJsZpucccnC_E0iWRzQrgBUniNfqsjN5Pjm8vWAsCIFkjivfAVaQP3v-1F4M0G7POsx5proj00xVr91pa1nS-WXsUJ5A-Nz-p-_0fLfLNVGlwW-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کاوریه گوسفند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82874" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82873">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انفجار در عسلویه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/82873" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82872">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار در عسلویه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82872" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82871">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">فرودگاه جیرفتو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82871" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82870">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=BQjnklUiXoVP-brTpy0P41z17h0r0aDc8duTWy5FKhtEzPnSxgPqjciJUTGIal8IXxmCrJU9lNfAfPJCRbE-FzI3jeoh55meIaOLJo2ukopSo_sgIXEx1QqLDZfL4JZblQ7QohZyhXpb7r4oeGSA1tlGORqB-15lngreKHUrBi0TwAiwguTBMWJmSAgJS0pDrRSK1jMtcWDwJBZyF-VSL_yAbXdSlTbQM-ehX6g49_CqSW9v46fN8DT_juov7BHMFOlc1CbHmT6SVrECYTDuYZWYiSzmdSbNP4cv2UDLrOwSrGZDKOGumuw36cAJKz7Q1jxhP_Vp_buG0Z3euSKjPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=BQjnklUiXoVP-brTpy0P41z17h0r0aDc8duTWy5FKhtEzPnSxgPqjciJUTGIal8IXxmCrJU9lNfAfPJCRbE-FzI3jeoh55meIaOLJo2ukopSo_sgIXEx1QqLDZfL4JZblQ7QohZyhXpb7r4oeGSA1tlGORqB-15lngreKHUrBi0TwAiwguTBMWJmSAgJS0pDrRSK1jMtcWDwJBZyF-VSL_yAbXdSlTbQM-ehX6g49_CqSW9v46fN8DT_juov7BHMFOlc1CbHmT6SVrECYTDuYZWYiSzmdSbNP4cv2UDLrOwSrGZDKOGumuw36cAJKz7Q1jxhP_Vp_buG0Z3euSKjPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82870" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82869">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/82869" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82868">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.   Soundcould  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82868" target="_blank">📅 20:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82867">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AP_36qZXkU7Qm7qAKJEAOD3MswAoIibWXBcPRQpMVL2PMC8bQ9-SecDj_c_o298noO4pS2hZ6QvyIRN-HDxfXO3wtkPDM8SSokKdU6iherVyqJlTV683xslu3gUsAv9Zs9MuISpTTzfWaTfOW8n4KlpfngAXleM7XMjqbZ8M80wDkAiDQ9Js2ZjLxGloMpgNELjLPNOlwXOXhzaOEYVAOgKcI7dYCjdb1hj6az1NWyI02WgzxOlhd42GsnBdCmWUHOZ3Op9mNV0i9xCiUqctvekWoAXP3KNHP5SExwKvh_i7-vV_3zdrp4J9l_7sIB-3YGWa3-RCIwtyuc2p9gVv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82867" target="_blank">📅 20:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82866">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بندرعباس صدای انفجار اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82866" target="_blank">📅 19:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82865">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">فکر کنم اعضای وانتونز رو یا ایلومناتی کلون کرده یا پیشرو جن زده کرده، لاشیا همزمان تو همه پلتفرم های سوشال مدیا دارن پشت سر هم پست و استوری میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82865" target="_blank">📅 19:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82864">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGyT88C2Yn6T99BCnma3TPOqQSUrapoLSldg9uFsPmvH5VDrus3AZR2LuSLimq92wN9ZkXhKEBMqnUeqEaYp7a2ep_5PPOJmT3_fSNsM0q-dk6w26i68_mjNOCI50BLSCQ0fxjGla1GU1p7VkbwX0CE8G-SePDWiRkLzgajUw8QIQLrMs1JyxVDkhDtTGcQy_QR-NR0LOz7ir2kzX26tlT3QJy3nXcSd0LHSlxoadYyev_VhpuEQ56sYPBPqdlNk1A0ImMCQ4GG9LyNcse5wewk_iHFfE6Bu-DLEbYvk8cYDkyD45oWuyGrrgeC3yP3SwTLNCIZhZyPybakJ76oIcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگید چرا دیگه به سجاد شاهی فحش نمیدی، دلیلش:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82864" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82863">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGfPG86Zn5tq0IgSAQIBpVeWpaa0uYkZl07jAh1Do-HE-8fRGiL2r7XS0x7MuXNwVDaJMcwac83dRWfO43D8dvkIKTb_TQlX1WCO6kCFo88ASeTsVNFV1By3QgKp09OfvqPOVYp6UVFvVjQQXafqAsMRIaEa4rZVpKZW61CQLAAa6YVXDAFBuauw-YrO7nVV6aZsfePRaYKEOrshMK2nroq9LxBl8fkZlQGeWIiiouL-z5SkVI6E-qhLfLueyMY_MLSBdjFUpPm8m8sGTO85eg21K698lHmtz15C0Lu9V4GhEqcZgczS_3WqxUbXK8b45T5cDhH8cln8E01tjrpiqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/82863" target="_blank">📅 19:15 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82862">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwbxszkUBhUEjuuhtRnHSDm8Rvs--K8-GbiVGBa9GUeunkj-kjfZbNgEpKO7dnNauz1Ueyxm6OEIh5zcNpz_62fujrBbgFFwsAQuFt-EtO3C5phewyELohbL9lFyl1nlvkk-4uxocJOZPWn-5nZwvMTJBbk2ayLv1-IcFHZuCmj1dHvjBO9O33xa9u8QLhp1yT2l4VADiTxCr9bJ_iJ13RAvkPfyo-dWg0Ip2ryDZNPwPei-CinKQ66fvxb_pV78QBUIE86z9W887pIwkE5iMcVez5bN4-_7Epb4jcHvNYBn_t72ffwasF3qGzrZfYh6g-h9cPlfNe8qHhvKbkoQXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان هر کاری که دارید می‌کنید رو همین الان متوقف کنید و سریع برید از بهترین تخفیف ثبت شده تو تاریخ بشریت استفاده کنید چون کلا ۶ ساعت ازش مونده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82862" target="_blank">📅 18:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82861">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTzt2T3ksufFN9KKBYU9YQOHguXmngNC9kWwSNc4QoKYncIw5qECPwOyE4EArZVbVxOxRO7YndG0kJ0QT9kFvQS39hBLWk5fNHyCWSKLK7MZ99mIjh7i8CA6cBe26yUfBNE2LkNaZDX9Ybnvo9tL08iS-dJLbMRmOnoUltwaJbVrNO9A3O_mV1janNpwFdAptt8ig8BrbQiXJGwcBiO0DFKfl0ZsVlksRXW6zTfFke6_25bJEesnNhkAz9SYYc2AUio-EEeh3DCbp8V0QC_mUupygc21_f-hC9nI4rp8YyyLXwwhScU791AEwpdSg90tgTIUw_vlLcN6pc5L-GldtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فان‌هیپ‌هاپ هم فانه داداش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82861" target="_blank">📅 18:45 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82860">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwLOPgRLs8r8_itm7gz3-0xQN0cx2vFmYLj94iMU9yMBHuqmY7Wl9A6iZIolCeTXVLAITtP2cJN1adV1lEy-QkoBGzCGT7NOfAAdmPQqFGA32uqTPA-CI8cR7TYXWZEJbu-goRpPP0aA8o8lq0-3c6V-7uJuLQ1GUfSMMl5hjlyciDezch2nIVqnItt-JbSROtDq6Gw8_iYijZyL4R4GtHoB38PcPpQTWbZi0yGBcSLQYH1Q0nlLSoNbeFPBSsvU15eBsZE0Y-kAEtkBAYCBzXtIEUmHLGFxkDv83EIS0Ucq7Qshw3HLhFa0RfzKvelhNkkHic5pchTkN8M9YTIzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82860" target="_blank">📅 18:29 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82859">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82859" target="_blank">📅 18:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82858">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">داریم به لحظات ملکوتی آزادی امیر تتلو نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82858" target="_blank">📅 17:58 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82857">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسکات بسنت:
ایران تلاش می‌کند از تنگه هرمز به عنوان یک گلوگاه استراتژیک استفاده کند.
-این تنگه برای ایالات متحده یک گلوگاه نیست، اما برای بسیاری از کشورهای دیگر این‌گونه است.
-این وضعیت در عرض ۲ سال تغییر خواهد کرد. در ۲ سال آینده، تنگه هرمز به یک مسیر آبی بی‌ارزش تبدیل خواهد شد و نفت از طریق خطوط لوله در خشکی منتقل خواهد شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82857" target="_blank">📅 17:32 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82856">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دوستان چون این روزا قمیت دلار لحظه‌ای میره بالا و شما هم که دیگه براتون مهم نیست چون سِر شدید، هر ۱۰ هزار تومن افزایش اعلام قیمت جدید میکنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82856" target="_blank">📅 16:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82855">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86f513feec.mp4?token=HJUQpOHj-79-7nEO6f5xg-MIMoufh5una_tsWhS2WxdZQqBeMz4X4qxxUWOVZIgoiyJN5Md9JREoDr8Dl_iCsn2GlS-fGMFZzi7PnoYEilkBzwdh7KHoJEqVxTWXBwaWgILIbcZikXnTMDxPFZLoh6BURv5Ex47vQqOdzzuiNgL7K0vXF1oNhhv8SFMP36qpDYJlAxalm5P2P-wzHNIwkUSAZz4TnM0-2dwVnUPWOr2l67PnhjTeu7RsMpGJgThvPDOG0CraMVXA5hz0E_Zsc16hrrKS2tW2jfaDKRNrok_2Jp5Rq5uK3M7lYO_XyPrkvqLPKnPw7OVns_A_AMRooA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86f513feec.mp4?token=HJUQpOHj-79-7nEO6f5xg-MIMoufh5una_tsWhS2WxdZQqBeMz4X4qxxUWOVZIgoiyJN5Md9JREoDr8Dl_iCsn2GlS-fGMFZzi7PnoYEilkBzwdh7KHoJEqVxTWXBwaWgILIbcZikXnTMDxPFZLoh6BURv5Ex47vQqOdzzuiNgL7K0vXF1oNhhv8SFMP36qpDYJlAxalm5P2P-wzHNIwkUSAZz4TnM0-2dwVnUPWOr2l67PnhjTeu7RsMpGJgThvPDOG0CraMVXA5hz0E_Zsc16hrrKS2tW2jfaDKRNrok_2Jp5Rq5uK3M7lYO_XyPrkvqLPKnPw7OVns_A_AMRooA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیا این شاهکار رو یادشونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82855" target="_blank">📅 15:50 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82854">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">به طور خیلی طبیعی یکی از دیگه مقامات نظامی آمریکا که میانه رو بود به دلیل اختلاف نظر با هگست که تندرو تره استعفا داد(اصلا هم مجبورش نکردن)
این استعفا ها قبل از شروع جنگ ۴۰روزه هم اتفاق افتاده بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82854" target="_blank">📅 15:30 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82853">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VuOgiGQHGynIEt3Vfyne6KdQeWVvSEF327I0qkkTMxLJnrSVE1Ry1CuA2ldIkmkyrEXRAF462kJm1VXCjD92npxSYD9Oq5aOwhlOJSM04IqKpi_Ona42YGZit5L1vHu8RmscS9GIljUPwY2kfuGRWxEbtbwSUO4dl_GvWqUdnw3w-wZGBllO772MRaZbJZ-tcllOr7MMgGvTQ0j721gB_DjRTD1OGxBPZObU7jYspEIrZIZWfB7sNPoe00w5ybLW6CIK-yhtsVDHngoZ0arBKoHFnJxWKgrwVzsVJgPt0TYVt-HjZJqlEAYPfh6ijFnMpDoOkoS1TRnZLkCDA8kqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخوام زندگیمو بزارم رو این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82853" target="_blank">📅 14:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82852">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=nnjaqjgyFpt-8B3BsyvbrRQMVnAS_iJshAsgIvYMwP7qtl3d2iTmwmWHcG0wBASo5rvAinYN3LB5wtDz5OM5o7kjJnzI5-MwrL8hg2ITscbs1-DZt8DGlGsqLwZu0KVCMgWw2huDQ_uC7VaIGRa-IZsDk_3SAsP8HhlNPASehMx_o65MDeMvtu0sPISsX8sJQF5P7azLvHv-sLwhSHlLdsFpbGQB1bvKcwONdtCJPy6SkjTxZcG3dQyaa1zrWDnloREwzs-wpBSq8MeCwGdOgrD68puBfiRQOEZGx0qTrJcQKnYn5nt_TCYC5_tNj2YcRPIWw-yrxqjvf1OoiKXxow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bebbef3244.mp4?token=nnjaqjgyFpt-8B3BsyvbrRQMVnAS_iJshAsgIvYMwP7qtl3d2iTmwmWHcG0wBASo5rvAinYN3LB5wtDz5OM5o7kjJnzI5-MwrL8hg2ITscbs1-DZt8DGlGsqLwZu0KVCMgWw2huDQ_uC7VaIGRa-IZsDk_3SAsP8HhlNPASehMx_o65MDeMvtu0sPISsX8sJQF5P7azLvHv-sLwhSHlLdsFpbGQB1bvKcwONdtCJPy6SkjTxZcG3dQyaa1zrWDnloREwzs-wpBSq8MeCwGdOgrD68puBfiRQOEZGx0qTrJcQKnYn5nt_TCYC5_tNj2YcRPIWw-yrxqjvf1OoiKXxow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این بنده خدا در پاکستان داشته خودروی بدون راننده‌ای رو که خودش توسعه داده آزمایش می‌کرده که با ماشین پلیس تصادف میکنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82852" target="_blank">📅 14:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82851">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش : با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82851" target="_blank">📅 14:02 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82850">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فردوسی‌پور بعد از شروع مجدد برنامش :
با دیدن فوتبالِ لیگ ایران، می‌تونیم غم و رنج خودمون رو فراموش کنیم و به قیمت دلار فکر نکنیم و شاد باشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82850" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82849">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R5pGRk0u7jzVN-dzHkwy7InWO7fX_djmlBMnmocgSfauD7QNdt7yTQIL67pJwnCb99bqwv5-xLRyMlFjxnW_6n-XUF05Ff67ydp1VX14zk2RlWDqc4cTDQmeGXlviU8GbD8dzltHClt3TwDrIHfWqJxl9_G1WX9AI1ytf22nTP_gvWmZyiekAnSlCfe_rl23n12pXTSXl2LHjCa2-p3Sz7A7m4YU9mXsSWz4XtKAnUkaRqjJW3K_8d-BEP2Hb9QoZlPJdzkkynRkzzvqtPXybwA8C_YQnRl343V3tVRYWDOBRiTsgrdmYEOVXuC6q5prrEeDNhE4riiPB8MtxX4OCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس سه + یک ویژه تنیس آزاد آمریکا
🔥
⏩
روزانه با ثبت سه پیش‌بینی میکس با مبلغ حداقل ۱۰ میلیون ریال بر روی رقابت‌های تنیس آزاد آمریکا،‌ بدون توجه به برد یا باخت، در هر روز از رقابت‌ها مبلغ ۱۰٫۰۰۰٫۰۰۰ ریال اعتبار پیش‌بینی رایگان ورزشی از بت‌فوروارد هدیه بگیرید.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/USO31
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82849" target="_blank">📅 13:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82848">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oNmo-lwSDZDFXX6POVhPUfvnhT4RKlWEJsJiHHiTpmVHgjcrWYZD8ufH5LfN2mY_1B8FKw8PUQPwOJx7qZ1p_yei8hj2O7c7bjH6nkH8uV_16Wob6qcv9kqzO80-Og0i6JTJZJarLZKYR-6VifKHRcP_NG1sDWIzBvGsz07D4_o8AM9XLQ_r9aLBQGJN83sPizGW9UpswllXpZ48dnP2lZWkzbG1Ns_Oh7hGxDaK42x10P3Jdqm7zZJHVVp7tmAxc_BGuMdnjUUteSU7K-ylZX0tDs8qEIXnJpLR9zwcP7cEeDOSmAYZ2zhtWqRHnbGZxx8hI-dvlRHaDquLV9nc9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من جای نخست‌وزیر کانادا بودم بعد از این توییت کل نیروهای نظامی کانادا رو منحل می‌کردم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82848" target="_blank">📅 12:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82847">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=sAhqOICecGo9lI9wwXtjpscsPnSt8RONVZ5FVw6REbgZ7T4HIFwzrE1FLOeXsK3q07SJK6Qi2cqki81neVM_vqov5sxAUxnbBhoM8k39gu40CRz_5mmOw07LuX4VlmJQ3-4u2gIa3vFEx78_T31yCQrNV6YdAKRT-M56NBPOQSJOs6nyZMQ42kane63iDnsbSzQ0RXritG9SimRgdsQXSCE0vxL80Wv_2hK7jSbpgrs1CfEDvDNP_lbR7UBCpUvepUnoC_hYzbBda0g3Ik4h4FLamET-GQqPvg_LQ77TVqdWa_Fm1xbQMO_fAB5ElPFfDU6Jt04-7lDKOjHtoxTGTg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/003dd1185d.mp4?token=sAhqOICecGo9lI9wwXtjpscsPnSt8RONVZ5FVw6REbgZ7T4HIFwzrE1FLOeXsK3q07SJK6Qi2cqki81neVM_vqov5sxAUxnbBhoM8k39gu40CRz_5mmOw07LuX4VlmJQ3-4u2gIa3vFEx78_T31yCQrNV6YdAKRT-M56NBPOQSJOs6nyZMQ42kane63iDnsbSzQ0RXritG9SimRgdsQXSCE0vxL80Wv_2hK7jSbpgrs1CfEDvDNP_lbR7UBCpUvepUnoC_hYzbBda0g3Ik4h4FLamET-GQqPvg_LQ77TVqdWa_Fm1xbQMO_fAB5ElPFfDU6Jt04-7lDKOjHtoxTGTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استوری اعتراضی سنگین جهان پهلوان هادی چوپان در واکنش به حذف شدن از مسابقه ناعادلانه دشمنان و ناملایمتی مردم کوفه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82847" target="_blank">📅 12:01 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82846">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YieMK9ITFKheWBD6mIu-pekm-w51v9lgXPfF9O5HjhykVREEulcVXAtZ2PSrVAO9FGS9xbHzvl2jDAVQFWz6Kzwn57L4VwMU3hF6bUAorh8vNE6ZZsHVLmGlmSJz72CVYgEQVkko2VVfhOKcTiiB13VVId46SZb4qoDwELWznRlT1sCxflbSkGdYl22RFU2yAJKUAyk3vc7MP7iTlMMiVwK0yEBgmDQGTKirjx8hQhzBNLEI7Ak4cLJcBP50WZrw-tQa_iLHsxju9NJfBELBbnq-ckK7S1iZn34ajU-EGtPRG0EzoRKbweAU3PLndJyuP_4WXWfHap8ys7CcKrH21Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلیپ لام جدید تو اروپا متولد شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82846" target="_blank">📅 01:44 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82845">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کصخلیتی ها.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82845" target="_blank">📅 01:34 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82843">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LheY36isd_FyjsdqXh4pJQYruCLIKkArCY_trbpxLcoZEjTf5B0NjAj3x-2qDr-XJ2LC1AvHsW99O6KtXn9ln93N_reJpKKVBo72lNC2a0chol3mmNKwf_sZ-FoBIpAUEsOtm8mNrSkoPvMRfVBdp4WmsX_cCVnEGvfdvroBbPBk7VAmysmHdEOYcfEjgYrrZj-wzqmanR9o0V_sL0Dbvde45-4HJh6jJHRPXO3H2B-tFZWoELWyZAB3Wmg1sAepVWzfI7-Uw_TsSHSCfS1nUFlPHuCzyvCttbzd590og28S1sNWVI_FGg8L076PI3KJDDZ9feSCW-5VSS7xBb86fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=EaMG0CXY1SOXujoW4Ci8ASkvVDa-lkgOpuP9vMziSA2h2rWmZlUL66scgnr1SEvRP58zKoFXnl8nd1i3cHLy6-RAL4AOxfHgI-5WTwXsTHHc-1_VH5e8O_TBhC_Hlq-68zUdDGTeHwpY_tJmDa5Z2UsWWs2nrpm2uPVIu7UxU3rWdF6BEmSVqS8ovqAcAUbMTllUL3ICtVBgnqxQ0uO0mXPE5moeFrcmCwfCm4De07aPO53ZCi9kzcjV_3-X40ikruSNfHGI1poJ2v7-Ca1--591F63vZBADYQ6stV4VQnJhGeKfDZ_3pUmdaqsdJhCu6tWs95bAJnTPVjO6bwrd8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6efb1a9258.mp4?token=EaMG0CXY1SOXujoW4Ci8ASkvVDa-lkgOpuP9vMziSA2h2rWmZlUL66scgnr1SEvRP58zKoFXnl8nd1i3cHLy6-RAL4AOxfHgI-5WTwXsTHHc-1_VH5e8O_TBhC_Hlq-68zUdDGTeHwpY_tJmDa5Z2UsWWs2nrpm2uPVIu7UxU3rWdF6BEmSVqS8ovqAcAUbMTllUL3ICtVBgnqxQ0uO0mXPE5moeFrcmCwfCm4De07aPO53ZCi9kzcjV_3-X40ikruSNfHGI1poJ2v7-Ca1--591F63vZBADYQ6stV4VQnJhGeKfDZ_3pUmdaqsdJhCu6tWs95bAJnTPVjO6bwrd8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پیشرو داره غوغا می‌کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82843" target="_blank">📅 01:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82842">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">حالا که ما رفتیم ولی ارتتا مادرجنده به این کاری که دارید میکنید فوتبال بازی کردن نمیگن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82842" target="_blank">📅 00:33 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
