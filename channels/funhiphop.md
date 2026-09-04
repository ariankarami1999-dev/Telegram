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
<img src="https://cdn4.telesco.pe/file/ShaYEiRS6PDqfbaW6PlcXUPZYvGx3YGLtK_u04XaNbghF06yalGIPzxUm4k67pNgNoV1D9WIaO38K1gOvw6-LgjCp0ZLn8MLc5W8ea57udMoy-nDyfTztVqfTZHo0XQRFvnPON6UIBj3hhfcDkYv4scMm5ZlsEf4cXr71Vs_dDBj9YLX0g0X3ocsbpaWM5fBvp38h757GVPdYYQPgF6mrIYYqYeQ5PrIlBdH5WzTo3DkmSN7COiR4UfYf5lp49-kI-tSJFDfj5aAa4mTF6jLCL2xlssdz77jI23IThWsrZpTEIxWsSqWLmJqG-sFGa8-R7ebINuA6lBsRJ3fjG0ArA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-13 17:07:57</div>
<hr>

<div class="tg-post" id="msg-82981">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJUem1kUjXEseERNWHIpJDywT4Fcu_iLZeQ3aO37a-Q78b12J5goXGLYI522EAgVtxyBVkwbN4l6Q4ZMFepAaF88N6UcAFk-1bNqS5taFh0ciejFbW5_ScjCrTzmCPcgLjmKwEgAE3ngKXiVInEuyYvhhVUTWeedbLChOJvlvDRkq7n_nY4lkY-1jzqC3BoF5t75tOH3YinTN7WAgugNhK4bKZSGiLEsceZEGpXZ-18sd0FJ26r4f7kY-sNDhwzxRJvEB4OuT8MHNvrBObhG5uzjzLaJUhL9cBlEWaDyQ5GcdVc9k5ueC2MizlcjYIRZaQ0BxdGS6mBgxVBbaf5TFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش و سیا به نام “چندتا؟” ریلیز شد.
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/funhiphop/82981" target="_blank">📅 16:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82980">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=cX-g_tB9U_RouNzB3HoZBezsvYUQB6qPIoEvGrIbcv2trW9rh8yhBu1RKRkYFMb0wy1RmBSswI5_hiLc1QXAuQ5pr2xoXYcwbboALCZElhY3blDLhbmwnziSpVTG8e-FAvhbkkkJUplT9w_zba1g3iflNQIoawRvxKHvqpvMXUyBicJ3x7Vetvrx6icjGPl0VLRSaNws46EOXLTyic-nJTfuLPYwN3g8b91u9LrdGQoVqEc8RwOJUDRba-Jl7pIz4YdnF-XLFMRSHWaG4sY_4OSgBs1L8iX2kTpSXbL1ioz31jjAZwx62gdokOV1K3doiTcyaLzoFqvHr2DdS_MCcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/575bec5ffb.mp4?token=cX-g_tB9U_RouNzB3HoZBezsvYUQB6qPIoEvGrIbcv2trW9rh8yhBu1RKRkYFMb0wy1RmBSswI5_hiLc1QXAuQ5pr2xoXYcwbboALCZElhY3blDLhbmwnziSpVTG8e-FAvhbkkkJUplT9w_zba1g3iflNQIoawRvxKHvqpvMXUyBicJ3x7Vetvrx6icjGPl0VLRSaNws46EOXLTyic-nJTfuLPYwN3g8b91u9LrdGQoVqEc8RwOJUDRba-Jl7pIz4YdnF-XLFMRSHWaG4sY_4OSgBs1L8iX2kTpSXbL1ioz31jjAZwx62gdokOV1K3doiTcyaLzoFqvHr2DdS_MCcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقال تانک‌ها از ایرانشهر به سمت چابهار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/funhiphop/82980" target="_blank">📅 16:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82979">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد. SoundCloud Spotify  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/funhiphop/82979" target="_blank">📅 16:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82977">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwUf19dlbWzFWHtWdYJbTlwf5HhKCFTeX7E8oEUcMQdHfO9SYHvwm1ZU1lay4aPV7hsfEoS_8vqcUijXkeNdf8b2pfwpUVT6PRMkaG7HC1Dox6tKU3FrsdLGzOBB9PWq6xNLQfhIya8CVNQ7sup6GC0Yj3wAfWWwal0WvSmogldnDvKrRfTLuYieARxg8iesP1pvBLExPmEfXsk0E6w1mDbme3EbOgTkwydaFX7BW2fGSf_AcoVMKDLPW61EFAev6fh-Y4tUYzZi24Q9T_j9x9CIJAO3nFwECqI-NgqWuFVWWfCpoV_zihxgJBNy2rbnutbxzjDvoO9NoeUqrt3Iwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بهزاد داورپناه و آیسم به نام "تا بتونم" ریلیز شد.
SoundCloud
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/funhiphop/82977" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82976">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_54FsfO08TLC4Ym_t1SZ7dFQICmCsLh5eiyCH6B0KBi4Wr9KXuZcFYkCpkDz-N2IPOw8TTvzQ7dAZAgVkiIR929vLqEnf4kcM_WiJFAWax3RoXmM76PV3UwMo9h9NidYNtyMre8vWLENjr0eMYxVfpVx-fxQocS3G4iVk42UP0SV9JrekXnMel0AAyXYAVbO998wa9GlhKM-mvNBvTJyBo83b4kuCEowkdIEUzZk-lr8rHER8eDAs6gpJVapxgdoYaDhIuV5J9xHj_qO32bDu7ixwacdaMgnUXZfJ7TJFBqKDqSr74ubPaYpu-REYL6GncKKuCGzWDVJ9SyNlvb4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهیار و خار مادرش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/82976" target="_blank">📅 15:49 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82975">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1dyD15hShyd3z6ADoQwOA4ZcnmbNJlIrUamU8_SyRnBD17HSU6RkjfciLDCwwbZKc1azkSNiMEIuKv7adueoaTv0frrC-RrfqckIlt5YT8RqyKigM0UDO9MEv7P2UJx7UzUGV_z3bd0UQmIZPVbFPb7L729PA4ZACvYaj_mLhX1caU211uq4hatO-VsaWGCvY1TashBLq23_Lku5SwSdetM687jCnQcQBJ6YvKAov6RWMTIqTNr4EDdg8b53gBSS8m2-p286-Pp4jywmRtR1fQoaZgwBeA_sLYkJ6NoHbsa1KuiuP_SWwofHWCLG_p2r7xsPN8CRT5f10g-hIQRxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دکتر حسام خوشبختی تو کیر خلاصه میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/82975" target="_blank">📅 14:37 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82974">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia6HRXbVxY01GNSXOCgHc7O6t3Y_xVCVtnKS6T8sn3kCSg39Mz3dd1a6tlySKl_j_wYfTnn5YWvyBwPPyLisO36e0pkvRZ_6RgP2sHNwrkynFsBMebyecowOKnQDiU0eSXl3N0ixZIyfGwaZKGFdJi-q9bEQqzJg-OhwNpeQ2jjiZ3nW7JYYwb7Vev-VRP1VLUfadqck-wZYY9KDbdrv6MCn7rXZ7fMdChWBjoiiLcJPMcifSL57EqtFmVb7OVi8XLo-29zK_zbDGnbCmuEo_TeFRgyItY4pq07N3SS6a8MBemn7cSPzY26NPoZoQjOCU-YEFL5yPydZA5v5aNk6Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید عزیزان، کمبود محتوا تو سطح فضای مجازی و رپفارسی واقعا بی‌داد می‌کنه و ما چون دوست نداریم پرامپت و کصشعرای سه سال پیش رو پست کنیم، مجبوریم هر روز به پیج این اسطوره یه سر بزنیم، ممنون از صبوریتون.
🙏
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/82974" target="_blank">📅 13:21 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82973">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">خبرگزاری مهر: موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/82973" target="_blank">📅 12:50 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82971">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1SETWi-_aUK7FoR2lWShapkQfcgOl_ii3E2vZl2ZwO2IBPU1W4EV4X6sl8JojyvKBcl9t6PJLwnkhPeAGV28OGXfG_95XIedjZo2ExeZADk44BH9BB9XeYiIR7tWaWcYhy2HPYg8BWmM0gIr52EzIuLJP6FSGap8BqB7TnaNMYhTEGg9ToLfFFauas2gZB9CP-RjtPfwT5uYJvoLVkkopibGS5XaBVdFNYZTaH7hIuluVoPvZDNlyrvhsS_Mzp31y81D4BVS4i0B3-QVmtvMlLF3QLtdssVT1uwvGFh_WuepDiGjLva1KFh_fEiKwsGtrSzAsbmJTVijXy5uE4PtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=vO5ULkzATK_5YjK-CZqsCjCtbYUBQpH8zE27N_vmUGX2zTSDHKFhJ8XkUyyKnjC5OmgnibYx0MZyty_bnXqFZyuwRAl2AWnRCCx1Pz68Hxdtc2MK466M7rjrfcpTm6QwYM5C-jA_K1R8rJ9BorqpI3gq9RLg46tdhRaBh8kjGGPOfycSDcoJmxLZi-lh3gtoR5v-C94RHtPFoWClJ0a0jZ9t8c1ynhVU_4NpkMcTLoVn16Ez49TmDIjaWlXvavYTEeMKjzvO2Bn_fQGPGgVK-T6YWsE9o0XMH1gwOELf0GExnxUGVWwZj8hIT1dPQA7CzZaJtIlO1lWgfuH3HJYbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ad8899803.mp4?token=vO5ULkzATK_5YjK-CZqsCjCtbYUBQpH8zE27N_vmUGX2zTSDHKFhJ8XkUyyKnjC5OmgnibYx0MZyty_bnXqFZyuwRAl2AWnRCCx1Pz68Hxdtc2MK466M7rjrfcpTm6QwYM5C-jA_K1R8rJ9BorqpI3gq9RLg46tdhRaBh8kjGGPOfycSDcoJmxLZi-lh3gtoR5v-C94RHtPFoWClJ0a0jZ9t8c1ynhVU_4NpkMcTLoVn16Ez49TmDIjaWlXvavYTEeMKjzvO2Bn_fQGPGgVK-T6YWsE9o0XMH1gwOELf0GExnxUGVWwZj8hIT1dPQA7CzZaJtIlO1lWgfuH3HJYbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره رسمی شد بچه‌ها، آه از دل‌های شکسته و حسرت‌های ما
💔
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/82971" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82970">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/miYzaydBUFbJjNtdiHJNsrDhVeT8IwLcqhA1uIvt9wJLQn3GCw4wa3vKsW0bSDtCAzAmRWa_BxzE0p0xvAfMGIVTFVJcjGE99u2Q1hd9KQT4YpUBLCNJbPzaWI57-ZMODjxMYqhVoxLOUbpVOv7Ds2nhh101RPd2Tq1kXUNfN2bn4lAMzFIOu8Wqru4HhTPcsTA3aJkG58NJcfymcBDbQ7_l-0mhK7Q_M10iZ1Tc9-ZILg47XS7T5QV8mYmCfOEGn0dXw-HWK8497Cs8YSHizE0KdNdB6ec5NJVhmSi2gR_PqXqmdX_RPeSshzGuq44mKu9EIuAjGs7uQ1t76R3tZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بیمه صد درصدی هفته سوم لیگ برتر انگلیس
💯
⏩
با ثبت حداقل ۳ میلیون ریال پیش‌بینی میکس بر روی رقابت‌های نفس‌گیر هفته سوم لیگ برتر انگلیس، در صورت ناموفق شدن نتیجه پیش‌بینی، بت‌فوروارد ۱۰۰ درصد مبلغ پیش‌بینی را به عنوان اعتبار پیش‌بینی رایگان ورزشی به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bwrd.link/PL3
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r13
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/82970" target="_blank">📅 12:40 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82967">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82967" target="_blank">📅 00:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82966">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=uB4imfOkCIN_3qAOc7LUAgZ0zp-ysi_hL_eg-JPukrj5hF68ryEdlZhB-t8hWkO_J_ybnR8smEdusJGDjVgy2gj93CU4XW0g-ZMm0_a6waQAg_BWZWYHfGX995aHv-ZShKXKcFJD9cUS9B4djRFgvWh36PmwpFRieDORLStYs04AEspNmPmlD5B7Goo1DmjGIr91ljWZf-HO04DteGi9p6IV6yxao8MydJ_yW0rt2JBEN2ryheN8bS9HMQismcxvZk0RRgaK4YNNLBAu1tyd9gizwvgFCelAnu70y3r-D2TbngxctfrAnJ3KDEGtCNvvTwVL0ubxCoZMRcBe-2JU3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b02f59615.mp4?token=uB4imfOkCIN_3qAOc7LUAgZ0zp-ysi_hL_eg-JPukrj5hF68ryEdlZhB-t8hWkO_J_ybnR8smEdusJGDjVgy2gj93CU4XW0g-ZMm0_a6waQAg_BWZWYHfGX995aHv-ZShKXKcFJD9cUS9B4djRFgvWh36PmwpFRieDORLStYs04AEspNmPmlD5B7Goo1DmjGIr91ljWZf-HO04DteGi9p6IV6yxao8MydJ_yW0rt2JBEN2ryheN8bS9HMQismcxvZk0RRgaK4YNNLBAu1tyd9gizwvgFCelAnu70y3r-D2TbngxctfrAnJ3KDEGtCNvvTwVL0ubxCoZMRcBe-2JU3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ای یو علی هستم، ۲۸ ساله از کرج
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82966" target="_blank">📅 00:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82965">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=lXyi6Hv_MX1Bi-nTi1g44HQ2iUycqEC44klNkFsc4TBTYoAhDJgVt8VpLzWyNqpf4CAmV-Z_rpNqR3AZyKknET0w7OxN9L7zyr7DKPlbbkj-PvRb_iLVxuvBoI3MJs3V2SK6x0o6xwBgAlX3IRLz1dRfhKHtvUoB14qjUN8oQzfvZH8KKVid6N-_sHeoLR1MoZed2nz3oFhs-0gMO5rHzFYf6K3ys5u3vrg8e8kTwWZSv3_wEtDbtDFVFMvtYbPNKCEoNWcRLFCWdYZWCAHGNSDZXZc5eNvSgEwEgNoLrgv1D3DqCo4KvcfvsYwpVncldQqZ-hZEBA6WGk5yuwWMlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c3f3bba65.mp4?token=lXyi6Hv_MX1Bi-nTi1g44HQ2iUycqEC44klNkFsc4TBTYoAhDJgVt8VpLzWyNqpf4CAmV-Z_rpNqR3AZyKknET0w7OxN9L7zyr7DKPlbbkj-PvRb_iLVxuvBoI3MJs3V2SK6x0o6xwBgAlX3IRLz1dRfhKHtvUoB14qjUN8oQzfvZH8KKVid6N-_sHeoLR1MoZed2nz3oFhs-0gMO5rHzFYf6K3ys5u3vrg8e8kTwWZSv3_wEtDbtDFVFMvtYbPNKCEoNWcRLFCWdYZWCAHGNSDZXZc5eNvSgEwEgNoLrgv1D3DqCo4KvcfvsYwpVncldQqZ-hZEBA6WGk5yuwWMlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این ویدیو از صفحه رسمی فدراسیون تکواندو ایران منتشر شده به مناسبت گرندپری کره جنوبی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82965" target="_blank">📅 23:31 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82964">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🦁
سرعت و کیفیت را با قیمت مناسب تهیه کنید
🦁
💫
چرا دژنت وان ؟
⭐️
پشتیبانی قوی
⭐️
امکان خرید آنی در هر ساعت با سیستم تایید خودکار
⭐️
کیفیت در سرعت و پایداری
⭐️
قیمت مناسب + تست رایگان
⭐️
اتصال پایدار حتی در صورت قطعی اینترت                               …</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82964" target="_blank">📅 23:26 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82962">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UM3ycYChQ1IGPkDIFDuE4FJpWW_akdTvkaerQyc8_NRmn2O6tbeXyOX-W9IKgfn4qqOoFpJyg3dfDvry1-SJQwJmcq59Q9q1fiR2-ICvDuKkljEAgig4ntl6n-ALcVeQhuqMok5wYxUGTOuratAdgD8fqL4wg1y_QXDy_Nm8F7WFX9sY7Hzmudg7LMTPwgvKEwzQKKVgW8YjN0WYli8j63w2Jg9Bgi_l1tDeGHazh_aSPt8iAlhW6UwM66JRJys0HPNuf0zv5mqFhl6X-WQ9zt9wlqvz29KXHfCb0zy52hJz83rSwVlWXeQ7jLjoBc4VXfza7epygzn6oqkKEvSFgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦁
سرعت و کیفیت را با قیمت مناسب تهیه کنید
🦁
💫
چرا
دژنت وان
؟
⭐️
پشتیبانی قوی
⭐️
امکان خرید آنی در هر ساعت با سیستم تایید خودکار
⭐️
کیفیت در سرعت و پایداری
⭐️
قیمت مناسب + تست رایگان
⭐️
اتصال پایدار حتی در صورت قطعی اینترت
◀
️
ربات
🤖
|
◀
️
کانال
💙</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/82962" target="_blank">📅 23:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82961">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اون قسمت از جنوب لبنان که میگفتن اسرائیل حمله کنه میزنیمش
کنترلش دست اسرائیله دیگه</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/82961" target="_blank">📅 22:59 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82959">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmnOH0OuF624BxU1FQC8m5sibQ9OJ3n8fncOyOptkWREXX9w0BNOdejOHt1Hyrsy3eSzLa3t6LhUqJ57Tr2fVkmBafZKF-vYJXsbBgl82bwHUPqNDxH29XW4_5MUD_RK5CDOsN0TYMG-W-XLOwS_sUH2JhL9koORWZI8VZPVD4JialfPBOEhOg5Su8G6nMewVeJn3yQTEygevJPaTd3oYT0uxGcf55BUg6R60B9sOa8Q0qpgueskId1ZhhgQipshsB0HMUF7nA_Pa4u9IY2VgoZm1gm26EKZOEr67jU74Q6SDyNAGWMNKlfK-MZ4Oc1sKCbeyRJ7WXaKDM6VqMhTRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکوندی شاه عالی بودی شاه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82959" target="_blank">📅 22:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82958">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=G7jbzJ4eHPgBlkzGyMbdVERTj5OSUbW3GAorlujhWCLOosdSkR2SnzMbOaJN_UtRx9Rsh4f0I0fRczFQZsMslT-koCoeMk-Jzsp9DZSNJrcfo5pAACrrzwviykhTkce8Au6NcBYuo4Nv8gNCG_r5X22ku-o0PsZrz0FdBAFqady1AuLbNAaK9YF3_0lLs1Wd9YnCsXoGksAlrs1wRGg9lLVbEy59qIhm909Ead4M1WbwD0Ke7GApGJtXzh67AYLIaDATaj0qZda1WiqT33jIfZ9PCoFWVdN00e2KHLwmgIit5joszYG9vSKBO_OxNEyTqpaWeIZmEBt5YZJaxAZCBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a86445b0.mp4?token=G7jbzJ4eHPgBlkzGyMbdVERTj5OSUbW3GAorlujhWCLOosdSkR2SnzMbOaJN_UtRx9Rsh4f0I0fRczFQZsMslT-koCoeMk-Jzsp9DZSNJrcfo5pAACrrzwviykhTkce8Au6NcBYuo4Nv8gNCG_r5X22ku-o0PsZrz0FdBAFqady1AuLbNAaK9YF3_0lLs1Wd9YnCsXoGksAlrs1wRGg9lLVbEy59qIhm909Ead4M1WbwD0Ke7GApGJtXzh67AYLIaDATaj0qZda1WiqT33jIfZ9PCoFWVdN00e2KHLwmgIit5joszYG9vSKBO_OxNEyTqpaWeIZmEBt5YZJaxAZCBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کافه ها هم مثل طلافروشی ها و صرافی ها جای منو مانیتور گذاشتن که هی بتونن قیمتو عوض کنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82958" target="_blank">📅 21:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82956">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8uf9nbfQ3ehDTjCHZvUdZq1iz53XY4nCxmQrnveenS6c_85jpySQtyiTVnBs3HJohTwZJf7Vg14mvw0CsUIZ2Zy4OksM7_5JitIlaXGM3bMXI1kBeKrzZLCxanKe-RKhnpzieaV_Rab3xeqMbKFNQ3F7rjs6LvTZ5U3_Zzbz8JifGxuQTqxsadAgMs1I5RxpRq0SSXyu8dka4Jq4Bl-YguramKZZHAe7OyP5gJ5LUQSlkeAfpMct3_EFYshaSwJlllK4CPs1_9iTVrUWy7FvZKVOV5gowh1SSJ1SNMOdKPJKvrZPs7-gcR-zmFwVAWtE7dXdo9sCaf6jYxRt9q3MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دانیال و پیدار به نام "Bipolar" منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82956" target="_blank">📅 20:29 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82955">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UsaFMqlAZAbOM1bytnwDu8N3dxgKdeAwcnOkUxP-VcMNClrs7WP7fjCT7XiypKFkFMIbieicTsmom0EgVTKkVsn5mpVfG2jXuDjpuPfod_tbyNPDju_GPrWzSK7-ziQHF_65SBeA1hEdlVFcB3cFyGsICknMU4HvsxpzLpezURrgwpeE4jf7FR9JHOYNc2kzcL2LGYFifuiAIJFxWCwvgiex9krAE_EuKfqE7jA7LRIcTpoOrW5HkT0WKyFQJg_eUVGoqW0koOqr_Bdflb6GRegZa-ddChJtHjErESfPiOKE1Xkda6IujumSb5Rzwlof76JfUUV9Me7H243DRRXL_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا رامین بد سلیقه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82955" target="_blank">📅 19:42 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82954">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvmdanzqfawDSf7JACFaPy0AzpIQ26jhXA8VA3ds4ITWBO5C6yORuuwN8bNDTyMWUWWbmoSf7CkijDCEPlMOdWB0q5VA1pcSP3mWzkUX8yZvovPsQaUUE1-Udy3Oa6iwwxO1cOYQ8GQorcOhZfFdDVFRBihWFoh7ZeLZuQQtRCCtKIWtIFDRCAWo7771Xd0RHwRe94QmAKhvgB9fHe7GW-h971Z9wfuhJQZKWGe_3KUB5-e0_Rk5V1hdHw3jb_GbYZpXyHDkp1SfkaKkQNY56uBAFvzHR3GypLg98HlhfxHX0OmUnnkt_gfWbV1fER58v6ql_oxwTe_RefR9g2RNaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی و پسرش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/82954" target="_blank">📅 19:12 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82951">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2_Qta5WrNr9J3TkoNO2gLjXCZ3uRujjXEPUDA5c0K2SewNX9mRhTC_Vh5M6cGznhp3lhMh2ENlfJDw_2wcT63FHo5G5T-qR5_y7BGmNtpZiz71sdVUClJTvhe_EbpV6SIC4LWaWEG5l6vxipBUU8X9prZfQlM29dfRzCaJsV69PkiV3XSdj3g29rdUP4q5saaxQmX_5v-2WuUT4i-jgb6SsvGTf67hesf4eZfAchdBNI-gc4q85-VSI258Xy7-atWJtu8rmtf7-F956ODb3TX9WcaIZ4CtadbIiWsHh0hyau8m7vFGneRYP-WDm7gYDfqKcde_4uax_dDwLascYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=FVtyBFW57KpZV4MBSFjTDbqToUc4PhuvjHri8yn_N4Q59OmJ4GMC7qTZkYtz4o8iF77zMpbsaM0OBzVTVEGJc8jMpkxHCZawHDaavDDnipY3Xh-a1Lu5Sacw1jZoQBne1V5-UJEzfiEfZtyFaWrVJ4r2QfkeGQKQy95HhTpYiydlkUbbkmKff-SWkfOzieGF2T8gP7zyoaxKGk45x4GXNTrnuxdLUsK2v3ojE1gC1Dn7JOkkoxg4fpeucCqK2bsJrLwunQhRx4NRt9jmu3q7VJCQa_rThZoF4kYB6h3xqy0jKSVD7qBQgeOxkEpqcInH5tpE5mNHMustdVnQwo8rhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4876dd24fb.mp4?token=FVtyBFW57KpZV4MBSFjTDbqToUc4PhuvjHri8yn_N4Q59OmJ4GMC7qTZkYtz4o8iF77zMpbsaM0OBzVTVEGJc8jMpkxHCZawHDaavDDnipY3Xh-a1Lu5Sacw1jZoQBne1V5-UJEzfiEfZtyFaWrVJ4r2QfkeGQKQy95HhTpYiydlkUbbkmKff-SWkfOzieGF2T8gP7zyoaxKGk45x4GXNTrnuxdLUsK2v3ojE1gC1Dn7JOkkoxg4fpeucCqK2bsJrLwunQhRx4NRt9jmu3q7VJCQa_rThZoF4kYB6h3xqy0jKSVD7qBQgeOxkEpqcInH5tpE5mNHMustdVnQwo8rhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شات های جدید سیدنی سوئینی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82951" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82950">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Q2Ia5pUjKLpEXDfZg9CSuPhOsxQj23etoi5TIGgASlpCTqmvkpP9HAziBLHRD4Cg6ddHwuXXgCPb7LfcpVjSw919jfVPjhqJq7TLjDTOBXnVOQtJ5-MDsiiTSVRgcmZNgyiHL7Y5afSloUm_ohX4HC17QFvgFWJlWeK3NiR0fh0CAl_AtVeL4ybMh1H5UNtMcoJqvEatSL5wDx2TNVz4g98Nh1C5KXpOkl6G9IAWFgQl-jbO1VglNFfgp9cPdWXqKACrhjb2sA4vvKc1OjlgFbbDzmLfkol2-yb86iKJNMk95bTJXXexxfo2V3Rg6bjGy6wa938Tz9J3eNe4TLtk9EIIxeM94dkvsY6WyH0PUsBGfAlZUDLxhQpdC68m2CPXF_AiNc77rj_INJYJhbyncLla25EVI936Hp4NUiVoCLlVi5Esc7pz5ylLfpnvniD8qf4d3ZQj8SBekxaGMSp1IXLH1q-iWFdC2SgWGL2bHiOyDsqk-c4IeQh5BMVsIRg1J1158yRr761Oidy20Gf7GSts6UDnyB_Dk_-E__JIAp6jGkFQ2Amagd_OxS0fnAe_qGP_06HvMTfBNbpjaZkDI9LTuz45FRvyuGyXH32-6kwGUy5Hy3xM9lQ_sykSsmYF_fdxYE5XCIObXAG2lu2vQGOTgplDCeYuWX7HhlwYn14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Q2Ia5pUjKLpEXDfZg9CSuPhOsxQj23etoi5TIGgASlpCTqmvkpP9HAziBLHRD4Cg6ddHwuXXgCPb7LfcpVjSw919jfVPjhqJq7TLjDTOBXnVOQtJ5-MDsiiTSVRgcmZNgyiHL7Y5afSloUm_ohX4HC17QFvgFWJlWeK3NiR0fh0CAl_AtVeL4ybMh1H5UNtMcoJqvEatSL5wDx2TNVz4g98Nh1C5KXpOkl6G9IAWFgQl-jbO1VglNFfgp9cPdWXqKACrhjb2sA4vvKc1OjlgFbbDzmLfkol2-yb86iKJNMk95bTJXXexxfo2V3Rg6bjGy6wa938Tz9J3eNe4TLtk9EIIxeM94dkvsY6WyH0PUsBGfAlZUDLxhQpdC68m2CPXF_AiNc77rj_INJYJhbyncLla25EVI936Hp4NUiVoCLlVi5Esc7pz5ylLfpnvniD8qf4d3ZQj8SBekxaGMSp1IXLH1q-iWFdC2SgWGL2bHiOyDsqk-c4IeQh5BMVsIRg1J1158yRr761Oidy20Gf7GSts6UDnyB_Dk_-E__JIAp6jGkFQ2Amagd_OxS0fnAe_qGP_06HvMTfBNbpjaZkDI9LTuz45FRvyuGyXH32-6kwGUy5Hy3xM9lQ_sykSsmYF_fdxYE5XCIObXAG2lu2vQGOTgplDCeYuWX7HhlwYn14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
g12
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82950" target="_blank">📅 18:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82949">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqtfEcdzxIjhvaFbet5U0dMkyW83jpKyIGKu38V7sVfVGJv7LEZ2eT5ovOCu4BkoVlLRyFkxfNK6WhEEmYgEhwXaT00P0qUUN00QMSi5n25AK-i-FgeCWGv6M-N4R1A6XMHJYmv06vmrGZBdXCYTkSDOhqWS-xpqtpS8Ar-AoCAGZCMmwqdpE5PpC0nmDBF_7OSMIfkPW7UVOwoo0qke3vLvAXAq36Sn4kHMDJ0GArM_zYnkdLbnpNPLHv18NZPKyayeIK1YrrV2rb8eSfzV8euKyo5P8uOtDXmwhHtpFEXjAPl6rGDrGUUiIQ9Iv1yilKnn-WYXz6jfqz4_8dB5AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام “منو میشناسی” ریلیز شد.
Soundcloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82949" target="_blank">📅 17:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82948">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">خلاصه بگم کونمون پارس
ترامپ میخواد پایان جنگ رو اعلام کنه و بزاره بره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82948" target="_blank">📅 16:48 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82947">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFkeDhnJQmRYqkLNATNisCudsRguSPrvpoJ421cQ808LmMjBiG0R83kg9BguElAz87YpfT9E8MLfsXWcwHPO2Tm5HHtIeLLEZgi5SweE7im7_Ucas5VHfG6nPfKu498TW62xTnGvMV-NZDFnERgIASWJQuplmVCxEccOL3NNb240X7Ecsknbwjk8P_ePkYybOeio9EuAh5qrulm4MqWO_mYgtQ2ebHUs5Vr1j2m6QaMd1PF9e9I8QuNEHITXmz4lI4kx8TeFKdFnB3_lVneYLL69MG3VJksxo_pxo5-zY6PPT_aZBF4Ie7wadyenyBWyJ1Clc1z4tPd-rC8US7Y3gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل دوم این شاهکار اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82947" target="_blank">📅 15:53 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82946">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=bmhNh3tN7gyHIyM70Ho6AqY3X6UgN0BtsZsZcQteuplyu2x2o4tIP_cfkUspiBno0WziwWFSawQZTneDeFBWrZDhmlnHAo8iMTqaokuFnuA3yB1yWEpkg1HYz-lnwjXRARJEeViSs6QcfBLaiwZ2fh8E2MCHuBUhtkmNPYnbXU5BVOr6eUgMLoQVy0X6SIVs0TTa00KoStldWURppouZkff7F0VtCpcD-YtJj3mDqSCI2510AZkiAAxhPa8lXHVqMVCiGow6LmO0g737TKaD70hAN6gld8aYCDWsMdYUOorxkWz6M4F-aybYxUo4LV4gNJHUNrhh3wz__hLur6FU7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c808b4326f.mp4?token=bmhNh3tN7gyHIyM70Ho6AqY3X6UgN0BtsZsZcQteuplyu2x2o4tIP_cfkUspiBno0WziwWFSawQZTneDeFBWrZDhmlnHAo8iMTqaokuFnuA3yB1yWEpkg1HYz-lnwjXRARJEeViSs6QcfBLaiwZ2fh8E2MCHuBUhtkmNPYnbXU5BVOr6eUgMLoQVy0X6SIVs0TTa00KoStldWURppouZkff7F0VtCpcD-YtJj3mDqSCI2510AZkiAAxhPa8lXHVqMVCiGow6LmO0g737TKaD70hAN6gld8aYCDWsMdYUOorxkWz6M4F-aybYxUo4LV4gNJHUNrhh3wz__hLur6FU7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82946" target="_blank">📅 15:23 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82945">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmjdGqHRpkOrnDaUpXQndN9nWjcyuO3FqwZFyKH5eWBynnZ-VAKfDsRKyC0qp6RvaE3fssVN_-S4zmaDsfSH_fZcCvtbn97PGvf6aFEOXozSQ1L8kPsIpiMqbyqy6GgkcS_EBCoCrtLX7Pr6jo8575eMFF18TYR5wFFvCt9pPyKHKKDTRobbLSOxHvpnjYJWSVXlHZepssNjpcLgvUalzkBYF3EijUpsB1XH9EkNu9nAEJ71nb47h6lY9oXjnI0iV5R-Wrqi_6LgFo9g3VJyr9eYSSL46gSdvCO-xNoz0_GKftasL17dd1AD5ImYFbzIsdLkc-9f0qRcJjJ14KaMnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست اکانت تلگرام تو توییتر: امروز احساس میکنم خیلی کیوت شدم، شاید بعداً عکسای نودمو براتون بزارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82945" target="_blank">📅 15:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82944">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MmUOzZLGLlNXDjAkjFoEF9d7uPBGjb7cVqB22oXHkmrjuLSWb90V5YywKWVuB2oM6xAFkVK2Qs6Hf_m6fCtKGxGSSRckw28nI-ZXFUZobCHJmwaogrwAV8mCTLK_H_OO3c_UrzQWC6tKgj6t44XKoqzofGatvboaOYt4tRdgpyG6JV6_pBklxqxPb7ylLh549-yOFFM7hLoxO84rbbO5FCAnKUccfxkwiV0T5xR2hQ615bnCL5iqvuW4dtPDy_8GOfxwjTb__6IeHaLrrXzGVMuHeGhbl3fkF288UvSEzlAiQoKxWapw-cDjND78tBpuHrrZH6c9mFGocqy7vfmOFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد توافق ونس رو دعوت کنید برا تحصیل بیاد حوزه علمیه قم حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82944" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82943">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=g5gOVOz-9bIo2LT3Gzm5xisQZHSzrHF4SV5o6dfn3kFCxqvHGnR5pWmczFnQOBtqCtUrnFmc8Oq-psuomUduivUj0Vsj2mrL-3m2k3uXftvlo9ETItoHan6UJWIMPOsHi8AQZa5NN-cNOBXlulfVIKp9TfNh9R_w8J0ILaWOcFVkbivxGLE0_Cfvx2as5NOEZtl_4ukUIjG1S2HCEeGzH9jsCl_vhryppXJckPgAQwg_TihKnLuB4hlMfJs0KDPzSlQjLikigzpzj5e5oPKY6V-fRFjeRxYen46mvlW1_8ru2U7LvJl2mnFx5adpXopzmE3juBzdCrtE4WsS8bUHJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70a5ddace4.mp4?token=g5gOVOz-9bIo2LT3Gzm5xisQZHSzrHF4SV5o6dfn3kFCxqvHGnR5pWmczFnQOBtqCtUrnFmc8Oq-psuomUduivUj0Vsj2mrL-3m2k3uXftvlo9ETItoHan6UJWIMPOsHi8AQZa5NN-cNOBXlulfVIKp9TfNh9R_w8J0ILaWOcFVkbivxGLE0_Cfvx2as5NOEZtl_4ukUIjG1S2HCEeGzH9jsCl_vhryppXJckPgAQwg_TihKnLuB4hlMfJs0KDPzSlQjLikigzpzj5e5oPKY6V-fRFjeRxYen46mvlW1_8ru2U7LvJl2mnFx5adpXopzmE3juBzdCrtE4WsS8bUHJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بهت میگن اگه ناراحت باشی عامل خود فروخته دشمنی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82943" target="_blank">📅 14:36 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82941">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">حاجی دوران شهید رئیسی، یادش بخیر</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82941" target="_blank">📅 14:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82940">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VZbIOVx1hoY8j0gIpQNx3AMliFbkGcg0O-zXmmNsjwFOLD63psKAk5PT_f_nDVVEOgiChUzkDgwCWcDOvyUMMP9JxSk-k-RcAlqj5sBUkN4EXSe3niqxIYTAbyl4oclaMxjJnavMIie4zUSWbwI81yTmsF0N2Xz2WVotW0fBR9rvjx-eRjAGNpU1WQrgQPYmqvqTqh02_oiRe4vIg1LkLFfZQRUASHFgber1VNrW7en0wlM1_8gOkesX6wj9mytxUieVlucv6Z2i8FckSNs-nubwwcUgyKnnjsD9tvvOGDcfCqAYhY8o3facBNwh81AahDJts-TB3DEhsvha_DRmIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی از سنت خجالت بکش این ایموجیا چیه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82940" target="_blank">📅 13:47 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82939">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یه گدای ایرانی تو ترکیه با  ۵۸ هزار لیر (۲۷۰ میلیون تومن)  پول نقد گرفتن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82939" target="_blank">📅 13:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_uzO_pbszXovLtbv5UlnCJrnaEbknbRc2wp-fmowAjdx4P4PapJGSWXQgB_JKEK43fZ3pTZRmfGPcYNln_dPflhp3ZzvnsmcWqpe7gFRb326tcuoyez5hIz7yCcLxGVecCkaCoOAHPam_JhKc_E5ach7Dy0MmB25Mcf5IvezAjLhH0U5e5nc1NHA89ZaZqNHDCj4Y8zUR4x5zphjCd5DJl8pHjgwT6QiyjnrLnlP2OZs10ExEW2R9J00Psrn3pkMotcjTC9fRKLXj3OMw_BJIv5wSlzw4Tsb6hBmXHEtkwssLMZlBjzr_erzYnyK23_5QfJ8dyyXn1m_7-2CDpxfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=evSmKE-Nxhi1En1TkCqg8o--7W1uco8GRGmmY5YniiH0ZAzhsLBenTNa8aZD7DIeUJgwwHzYTiPNf2FXaSZJJAM175JDjCTPdeN4zHdoTpzzKMZ3AaSe1RCE0s3EkOmsJ8Hj_DXYd4We1LXoTxNxrk9IAPNLX95zb-_sMq8Asd0jSPoaOxuptBKRkh2Y1NDgnhqrt20Up4vraPsflegbqxfNzkdX98KRgh64ctiTYXMT2Qw84W0l4I8JmqV0Vs63_XEePMJnHITF3DT-ZNuKD70G007m-f_unxiybzUE8L-6PnGi3Rc9eh3r_7iZCIbIgsw3WVcEJh30C5mW-JR0NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3cc88bd3.mp4?token=evSmKE-Nxhi1En1TkCqg8o--7W1uco8GRGmmY5YniiH0ZAzhsLBenTNa8aZD7DIeUJgwwHzYTiPNf2FXaSZJJAM175JDjCTPdeN4zHdoTpzzKMZ3AaSe1RCE0s3EkOmsJ8Hj_DXYd4We1LXoTxNxrk9IAPNLX95zb-_sMq8Asd0jSPoaOxuptBKRkh2Y1NDgnhqrt20Up4vraPsflegbqxfNzkdX98KRgh64ctiTYXMT2Qw84W0l4I8JmqV0Vs63_XEePMJnHITF3DT-ZNuKD70G007m-f_unxiybzUE8L-6PnGi3Rc9eh3r_7iZCIbIgsw3WVcEJh30C5mW-JR0NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید مسی که قبول کرده GOAT خودشه.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82937" target="_blank">📅 11:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uk87K2llCC5IxFGdnn9Zuhcpoh7sdEunCsRkh5CQTqIGOQlhRzioGxfPFkUTFRFDE2aSAHEtftc4qgbKeBeeTk8a5Ub8yJ8iaky3vN-rKviz0JxfQmjeBfZ42iN4NLcDlNp0CHRyJaaeH6QEVGe6HNqDGVdgqm23b8pTegC12JYvOPXFnI_XmFeqEAEUtTZiJnoeVmgh0vfjhOqb2HAMP59_-qZ-7DXy6C10_5qga3RzbnpzDsC1N9xmh4t0uGKvVvN0TYvmAo4gR0Z2Nve8-dm1zzIs8HLnlnaoB-RwUj6Jk2Lw1j9NLEZANWbRz2JYleqKRLgWJ9AvN5-Ah0vfPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیوید بکهام اینو توی باغچه خودش پرورش داده و به زنش کادوش داد، ایشالا که خیره
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82936" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Cf4VbhTfqsLs86F99JUKeTus816dSun_IavFXKfTynLoVpJwPRKcG4zV0J8CnX_opCcZKAc2ldztdQal_CMOpxsVQs2VuktcGsy4u9JdtQ0i1XSmTuYp6BmHSynuEVDlL4nZE8vYjB5CVbAFa9JpYubJRTtTeIERGptvogh8aopo9j8toAZ-3_AA8WRmNvptHrc4S2M48eudJs71xAamzT_lC4M497plPXzQzp87S9iZsqjYS73_o-W8FF5ZJUFUmesUWSFqNNT5LC17KSSmMmRiDJUO8vwNxGny9JJOpSCFLUFCwqEtm6yT7jg43RQid2CBvb02yLQJe1sPqQkHFrNOl-uUyDz5Gw3RqVB1Ibc--ESaxz0XEIxgeojq8mgg4wUWbciCcH3AiiqmLdQuHKVwvgWL14IXkPJktKL0AIJeoryCL0lNOurBLQyESVaG8toT7iO8MY23AMIXHlUOqUorQDR1Y-xOfr8SZ5V8Y6SP6ugRTMluZqli6w1D2ATdj6OEvZ5EkkkwK-0-l0VxDsq8XvhNOeEfO-PdAlLcyNLTo4eP-BMAbzQf80WW6gvjChcRdbFWXrQALduaX0lM_mpPyAYPyfDiOU9W7xDO9ZkdMJx9llUXVE1OaG0NGxfQHzFCd0ESZdA0WD2a15cP7XoZilojX2BMhRCunk0Rx9c" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/319e1218da.mp4?token=Cf4VbhTfqsLs86F99JUKeTus816dSun_IavFXKfTynLoVpJwPRKcG4zV0J8CnX_opCcZKAc2ldztdQal_CMOpxsVQs2VuktcGsy4u9JdtQ0i1XSmTuYp6BmHSynuEVDlL4nZE8vYjB5CVbAFa9JpYubJRTtTeIERGptvogh8aopo9j8toAZ-3_AA8WRmNvptHrc4S2M48eudJs71xAamzT_lC4M497plPXzQzp87S9iZsqjYS73_o-W8FF5ZJUFUmesUWSFqNNT5LC17KSSmMmRiDJUO8vwNxGny9JJOpSCFLUFCwqEtm6yT7jg43RQid2CBvb02yLQJe1sPqQkHFrNOl-uUyDz5Gw3RqVB1Ibc--ESaxz0XEIxgeojq8mgg4wUWbciCcH3AiiqmLdQuHKVwvgWL14IXkPJktKL0AIJeoryCL0lNOurBLQyESVaG8toT7iO8MY23AMIXHlUOqUorQDR1Y-xOfr8SZ5V8Y6SP6ugRTMluZqli6w1D2ATdj6OEvZ5EkkkwK-0-l0VxDsq8XvhNOeEfO-PdAlLcyNLTo4eP-BMAbzQf80WW6gvjChcRdbFWXrQALduaX0lM_mpPyAYPyfDiOU9W7xDO9ZkdMJx9llUXVE1OaG0NGxfQHzFCd0ESZdA0WD2a15cP7XoZilojX2BMhRCunk0Rx9c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82935" target="_blank">📅 11:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82934">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g68Lw6nEzDo0uPGMf_0LzFoPet7ZR5F2dc1_foxkedhR8RHNULg_7EULGqE3trxIKt3zUKtUpIJxGFHzzjSl7IWpyAiV1vBh74kHQ7IkFWPNkpiyw7Td3X_W6zE7laegXROgXoREf6MFgnUpXbzFC1hzIMvcL_nHV36Pyj4M-_dldhLzG6Xvv9yhYRDE0Tv_0Um0LTpYhVf9bOfKD6EaR8z8bf58Q9B94_NhRzKBGh5Yk4bjH6zvgAzps7L7TdWtrdCLb19uAj7ByCTK_1TUq9IgU7Ftf_Mi2NwuwHZHRaBXajUbmmTtZeOruB71EKHxPRLAyG_5EnLFbIM6WHmFxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرسی نکن پسر تو تازه ازدواج کردی
😐
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82934" target="_blank">📅 06:19 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82933">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=DVyOVWjBzb5P2xVgTQre3hO08IB4pZWRBAYz7vmVgaJ19G26VxLHEFZa0Nkx7_McuwKPqXHsLbewBm82bOLw9kk4oBE0e7F0ZAF__Ua9qjOE8F6nsHmAW23IyktQY2GpBJ9hrygqa8I9J4GK1gsGVeH8gui2EYgdqXGziP3a0eO6X6CIC8xDyRep1SrHez44EEfkApC_NPKgd5JNehJfNqmUdF2v0zTFXcMu07_mTav_bmCzGJYcza8e-f2V2avIobB1StlWOzWOgRvWJ2FExJQg5vsZa62VBLguovBFvjfiXmZiwdoG28Xmz1PQHFqaK7jH-e3GKSLhkqzvcudoKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c96481e00.mp4?token=DVyOVWjBzb5P2xVgTQre3hO08IB4pZWRBAYz7vmVgaJ19G26VxLHEFZa0Nkx7_McuwKPqXHsLbewBm82bOLw9kk4oBE0e7F0ZAF__Ua9qjOE8F6nsHmAW23IyktQY2GpBJ9hrygqa8I9J4GK1gsGVeH8gui2EYgdqXGziP3a0eO6X6CIC8xDyRep1SrHez44EEfkApC_NPKgd5JNehJfNqmUdF2v0zTFXcMu07_mTav_bmCzGJYcza8e-f2V2avIobB1StlWOzWOgRvWJ2FExJQg5vsZa62VBLguovBFvjfiXmZiwdoG28Xmz1PQHFqaK7jH-e3GKSLhkqzvcudoKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش میخوای کلیپ غمگین درست کنی درست، ولی خب مشتی از وقتی یادمونه این بازی مساوی میشه خب.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/82933" target="_blank">📅 01:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82932">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgbXhu4pHQTMosKv1ZIpKAvCWnZpaKIHKbZROrClzwPflOk7kBA5rFQrYCQYzGSiCLwe6MzdLhZGRNlie-uZLajZgmLds-li3WijW5YWSxal84rcb8kvH60MnPyENKTzb0y3rvvU1BDZ_61bQ6UHnIE_0X4gjQxSRK0XmYEezh7Ue60oBK-PVHrfLt5lPkx3DYSkEP1-vM4X1pq8WMpa9K5iIbT3nUQU-rL7MA575RmaDrtFgpSuh_cJuUacC1hvkq62sh1VrVHn4jCfQ6LrI53Nj-oOFHx1C-bP6Acw_Mt0XIJozCU5p2xuFdZhyXvSEByQ-9IOS6dcjzAVbB8-nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش بی‌خیالش شو نصف شبی بگیر بخواب، اون بی‌لیاقت بود تقصیر تو نیست که، لیاقت تو خیلی بیشتر از بودن با اون بود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/82932" target="_blank">📅 00:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82931">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OngZYvSns3POk1GgSThoUpuUFJww2vCcqMP6KS0TNdL95jd0ud31y6qbWPt6wSGwSqnwfV2mWyA19REGXUVqEtOdS6XnDI__3LEAONUXXA3V4PzKbSy1Ei56I6zpBPocJiOyuvoBFtGie-IL9-fTwE8KEBrwbpDEpihb5MgbuxwzTD2HtoxLuq3Hbz_gflHHXB72k6aJ0Cu10URTg_ukTDFqFdggtRGXCz8_QxOgfh943aFcc0X0SmSvjIynSbsy1zQFJu3pZ3fpLZgE9W9PZmfqektaBNaaj4zvPgoWzY3mQj57WEW36KlAMb7eLX8WFRJq-v9iX9rMzZSppFY5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۰۳ سپتامبر ۲۶
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82931" target="_blank">📅 00:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82930">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qf4r_mKQpkKrxvLskUYNVp96HCWkSTFu1KjpjhVAsBFq6yn20QAQc736hjYSZ1VzI2rcSItjwR3FuWYr52c2G092MyZgs4TPmcz8DRfK3aDa03knkH_nnFrwcw_OHNlH7-k5zAF5ptC8FflTAp13U9CFAtF_Z--6VqsyNn2kV0pQEsvIPyJKgnOx2Qtm0UiSjsyQZdy6TpaAxVyRQCV0y1ijqIZ4NLup2LJeFzoHsA8rUr_933JZ4VDNbpxZTCGIDHAaqPfDcvugdSNSKfO2U3OEUlb0hrBcx9gRb25JRmxOFyg-5oyCNkVUfcZ9K0RuPNLmkSAH-Nsbcqr1M3gaBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود: عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/82930" target="_blank">📅 23:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82929">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">راننده جنسیس که توی مشهد یه تجمع رو زیر گرفته بود:
عمدی نبود، از تعادل خارج شدم و وقتی به یه نفر برخورد کردم دچار تشنج شدم و جا اینکه ترمز بگیرم، گاز دادم و یه دفعه همه رو زیر گرفتم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82929" target="_blank">📅 23:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82928">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n0ZO79EdjwmRiyIOvhEDOuvnaPnGphZxkVDnvuoFVG6OXky_MSO7wapY9CJpsui3yKM4_OYX3Iqk4ielzx_yb0swr8cl4u2PlTswI18-2ojeIKUbVReI2wdDHfuYztP0INCbIHaznrSNC6tJ8iJmwksBaMDiGCCiGVgEtY3pM8pCAePneWYK9P9wLOq0rvYgjpNbcCqE82FsvwhbwPJoD7ILs03VQzU7YxoIkACkVsG8S3-O248SgUSir6KqdnFsGdhJsoTknPFHblO7zjuNu0kLrkky-jCxIwfl23q7Mnbi-yzGclfjhNE-jB546nQ2ypuFJViesjq44xqo9dUQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی به این پزشکیان بگه یه زمانی همین روسیه نقش آمریکای الان رو داشت اندازه دو تا اصفهان از ایران خاک غصب کرد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82928" target="_blank">📅 23:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82926">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پزشکیان خطاب به پوتین :  قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن. حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.  @FunHipHop | چمن…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82926" target="_blank">📅 23:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82925">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">پزشکیان خطاب به پوتین :
قدرت‌های بزرگ صرفاً چون زور و قدرت دارن، حق ندارن بدون توجه به چارچوب‌ها و قوانین بین‌المللی به بقیه کشورها حمله کنن.
حمله‌ای که آمریکا علیه ایران انجام داد، نه مبنای قانونی داشت، نه مبنای علمی و نه حتی توجیه منطقی.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/82925" target="_blank">📅 23:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82924">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">لطفا موقع بازی های حساس دنیای فوتبال، شو های مهم و حاشیه های بولد قیمت دلار رو ۵۰هزار تومن تصور کنید، تا کیر نکنید تو مغز جوون ایرانی ای که تنها دلخوشی هاش همین کصشراس اونم چون دلار گرونه نبینه، نکنه، نگه و...
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82924" target="_blank">📅 22:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82923">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سیگارا وینستون جدیدا بوی پهن گوسفند میدن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82923" target="_blank">📅 22:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82921">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HZ4shZfqbWD0xUDHM5s5GmQ9szD2rrsJE6aIDaKCafqEHMhE9vFnjCCS-q9RZYuJcYx2tSHGcnX5PiKeR2KAF1yCEf4evq-osdRTDTDTDAe7IetFjkpfx8oHJEVBpxHnisjIWjBJv9YuKFuJBgGwKpx_DAxTVYSNhZne6PxPw4FgwAAJyOwNOw3IywNIP6xLr_L2l2h2nTyVdjxxFjN9kPwnLC6nkHfbZEP7ixG2vW2eE0n3wI5YnaoQQ1VN9rItxMb9ERdTgBcGzWWwdEfWWbO2faRd2wJJvRX_ABHy37rhF6WJg-L3PVI0zeIrFICDW68oxUfj51bAjzSJgUP0kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QUUmHemxe9lO2YCx05-JXbKxoMIc3TIOJ6TUCvyIA9kSPcRWclnqkbgXuvdYb3k7hIJxRY-P6LB2nItdSOit7c0tbw_cZSPJ-A6NgRqOV22qmq1c-QykxSOimJqV8jwguiqX2bFKEHC_HLNKlJym4uTKwakkd70B9Y-vbosgMRt9JPw9B7Imd5cXitrSrJXKI4kmu6qcuaeC9k6LJvv8xkMG18zITk20Q52JzylgN_tD7y6mleWqGhQ8wFTYiPEvP5R9MF7mHk0ASgrzPC31iukzU93LZ3fgsiWEKUyn57M55nwqpn-BSZPd00gO6Op8k-FdoZi8oMsX6E4LzBi_wg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید لنا.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82921" target="_blank">📅 22:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82920">
<div class="tg-post-header">📌 پیام #52</div>
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
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82920" target="_blank">📅 22:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">چقد غیرقابل پیش‌بینی</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82919" target="_blank">📅 21:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">0.000000000001 ثانیه فرض کن لیگ ایران ببینی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/82918" target="_blank">📅 21:08 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این دربی با اختلاف بهترین دربی ۴ سال اخیره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82917" target="_blank">📅 20:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">چه موشکی ول داد یاسر آسانی</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82916" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.   Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82915" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nPStDjwnXbdoE0RJfkSqfTthSrk1aSroKOuzN8gbhydl2L9RfC2mXkpiOyXVd3cwyfR11UXhe-MvaVPY0NQr6tC7nEE25Tjytzuz8mPFy9mT2V7sKh4cgoIlRhafLeHsif0iC9HSgJKDIruiKLRxj7e6p-zp2ysEBl9S-geV0qPMJAMwUDk1kvSGm86rk0Cmj6qFWPqJkB4A25YJnlf7EBc4VzgZJiljVAsb5OAa_tYEeMMw5zLgC9et1KtBBpVVQ6ffQPsMDjajht66eKvPNH7Lx_Hg70m3TooNaZT2xZ85n_1HqFteZ71wlFFe_EBGy9UpGNX1z9g6_65q1Gub-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی و بیگ‌شگی به نام “رقص اندام ۳” ریلیز شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82914" target="_blank">📅 20:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tb-JEqB-uXCOnbKYdnr-4Mo8G33surbSMAh7C4dO08dE69jcPi-8TTtUqRkFKzzCkLa2LbpJ7ej5SsEltONZcMkbpusqxi3cmo50Zij4ADZT-0dXnYyiRMIlGlRzxrU19rCfd3C-wbSp3oERdbys9uXzem1Dox_RhRXLiouSQa-HKJLIvm10nFxJ-btQRUOvxmPmrqiGgF1d2S3RkXEzrnbH7y9tXEaq-n_xBsoSxlT2_21EmAgY1iXiuO0uThYULcfuO-kWNvkm_3I0rsu_PU9ChBnBLPKnd2KamnLTeyGbJHCCKFu2r9sUZOGNDk5BqTDl_H6N5TtoPE-CKyXvIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سکو ها جذاب تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/82913" target="_blank">📅 20:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqcFnlj1jGdIzepqYjHg70n1z5Af8LIN-OvpjWVuBTRqVAm8d9e0TXn_0Ed0kq7cx6Y4ud-3fxmuod2GrfAEAdWfy0sI9af3CLBakP17UV62BOURn2FifkhrR1IMv4p1C4P_Xsi5HGpXFARtwJchO0_G__zzVKJpNTyGv3ddeUwsog0fXa9THbPx6xv2N3-XSkpU5f6JgIEcLPXlxuO2pctxSmjc9QywJG0N-AAwFNdtwoQXEQsTeMuoN_zuaAfq2kwQf2bkTBWuNHBF8hiYhWSgqzqDo5Ai6JMKnvPRBCmov15YMv3zZvMpZfrrCfHtzZsfdaqdeVkQ31SfqQmipA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت استقلالیا از دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82912" target="_blank">📅 20:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پرسپولیس از کون آورد که نیمه اول مساوی تموم شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82911" target="_blank">📅 20:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بیرانوند کص ننت</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82910" target="_blank">📅 20:13 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خلاصه دربی تا الان: آقاسی به علیپور میگه بیا گل بزن علیپور میگه گوه نخور
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82909" target="_blank">📅 19:56 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">علی پور
😂
😂
😂</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/82908" target="_blank">📅 19:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">موقعی که پزشکیان زنگ زده گفته دربی باید مساوی شه صالح و آسانی دستشویی بودن فک کنم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82907" target="_blank">📅 19:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4l18EuNhLlUjDSNlafVrSELrU1X9F8y2jRIuX7Uo3JPJHKMcCbTFSk8iGlFfiFHTARuhW86grVtsD2QzSAnlMki7EwD6VSp2akq9ohXavRkRQZotdK4rQ5f0U9e0jp5Rl9XFPVFiDyWe4Di1Z74xz11bT8Ah6F6DwS0MoYfO6h3Fl-k1KyRfiS0gCYjXDHa9FkFR69qOoxGKlao-B95RYzmv12Olld6qdtC_P3vSjE1oXR3Hf-5M3wMtAyfoqmo06r3X2T4OhNhxHl0Kgh8gjD8F6Eaqm-PowY_29KjyDEEiHlHMtvkyueUyjxWmm0aLVJWSKCiJWkzCtEH9xWttQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافینیا مناطق خاورمیانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82906" target="_blank">📅 19:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد    YouTube  Spotify   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/82905" target="_blank">📅 19:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QS00zIju2hyVlcrQCXqJAoLBcS0KeU8zO-DGBsQqaN6liaLo5lkpHe6Jk4ZgIteN75Vix2bH97XKpUC3YzBfB7YMqnCqSQcxzmEt6q803Ypkzw3I5HBS4BbAcek1ZqZqhFz2zTOazhvu8_1IfoFv7XJkg4jf74P4rV1XS-XP40_mw-ZvQT99PWiKNrVo5KaLx-1aLvUyS3GkPAMjwcvhk6cw8SngDTnggVXi7D3_KPaPhCrfWTrbddD6IDTMLonZiHl9UNd5RnI5nDKhXEybo0sSegFJPolJYJMYO8-UoX85cdM_Fhybr3QdMRq9CFBAyZSb7BQPOcDMkTmPWfNXrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و آرون به نام "Alone Rockstar" منتشر شد
YouTube
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/82904" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">آرون جزو معدود دلایلیه که رپفارسی رو دنبال میکنم هنوز</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82903" target="_blank">📅 19:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82902" target="_blank">📅 18:29 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82900">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IpXX7miqEfZZZlt035OwmrU1eorEG7A7O3IY28bx0tbRh1PJ6aYS1J_xTmn-JKMuxgEmzNsLvpuYHgUiXeXawBrqV87IoXOw3lEDvIcI3vsfHcHRk0Smcxn2qtqanYN-TymQX1TWY1wruxKAaqmulArJJBBX0uiv6AN-gD3Lu90Da-nFQ7cjuenVLaDQh8v0843DX9heSrzyMlykCR8l7pNqQXBiO7jyDRn5mKrBkbkionlktjdk7HiU4I13lkxwYJdq-XmqOGQjt7MJZ6tO3Mzv0vRVpXESNX9jWQ2U9QVLp1U-hYiVVIAlfrVpm29XmIx88yFWUpVTTbcOeWvWFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5Z-M2mdE9BqH9me83nnpej2osBs5N5CI2hsL4Xij_Aig-YIgSFwgQ9U1lrJBCFIgPN2AT0L0kJs_lwThlgpQnSmDQFrSZkn_y_--26n_OHvVa_ULGfeuSbJcIk4ticzYVnUrtu-8YW8a9wX2zZXuVab-INXuErGQSH__wPbr2WfNQqIXLFCpzw16z5SKejNLqNQmxXcuUT9_sSPkUYvsWMpoZYo9DqepJ1-8LrhgldO4CGnuNmT6G7GlnWV4SHDt5YA2CdikyyTjIvYhVhtLuGKia8aOYZgTSTR_ESNdGwnFEfDDxv4bfExVzv22LN6_rUSZMd2bkBMU0jDxr8GoQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب استقلال و پرسپولیس برا دربی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/82900" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82898">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">جدی نمیدونم تا وقتی رافینیا هست انسان ها چطوری میتونن فن بازیکن دیگه ای بشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/82898" target="_blank">📅 18:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82897">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_yaT7EA4T6BwUxinV5fuE0phZVz3zL3dUU6Ut0QK1ySo85IOfnItWBXvJkRIHUXhJ4P_Lm_boO3aERenWHif-Bv-43jE8cCOWBSIjuuSziWYAbgueOdcynrcg7oa8tFgSmuDzswsODJq9x5fWwdvi0hBhf3P8BvZ5_gxE1uHbCqozTJ3ta86ehlmmcKiGV1hM7tKv87vmx-KwXig_DjnKAhYB0Ds4PyNQfgMQp1eQY0RvcSb4BFfHaw9jNVfNvR6dIhxi2GtbZ_PDlY60e88ul3EmoXhAfvhJsTUdNpsXFfmFnUG4T0uyiyCdAYKEUdth3yah8Y8JrWcS74BS23OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوه اوه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82897" target="_blank">📅 17:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82896">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دربی ساعت چنده بچه ها</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82896" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82895">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">خدایی چطور هنوز فوتبال ایرانو دنبال میکنید</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82895" target="_blank">📅 16:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82894">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82894" target="_blank">📅 16:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82893">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شب هالووین امسال آلمان قراره یکی از ترسناک ترین شب های تاریخ خودش رو تجربه کنه.
کنسرت مشترک عرفان، ریری، هیپهاپولوژیست و ایمانمون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/82893" target="_blank">📅 15:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82892">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دلار هر 10هزار تومن که گرون میشه ویلسون 10تا ویس میگیره میگه "شما رپرای اونور آب اصلا چی میگید چاقالا"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82892" target="_blank">📅 15:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82891">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">امروز در کنار دربی تهران، دربی شمال هم بین نساجی و ملوان برگزار میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82891" target="_blank">📅 15:04 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82890">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/82890" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82889">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aMN8Mr7TkHBU1Erv4uH7ACLFzGLBZOtvuJqdBeeAelN--Gnh7yw41ESIEsC6VFdWinfK0qPhCSyMkBL0YGLSLy1goVKB60us2pY_vMZdvjqEa_CePQuoP3Yvo8ESudL6h2HMwHQtH-fE6U7orZHkgyXVHNmFqd-NKH5-sgZ4UfYhNCc3lfmkNWBVC0iixcLHDfr58SyEIUsFqTeBe2h9yqKhBlprB96WaCZFY0IL6k_Yu0vJYjRPjP2FlkQCjt2bTXJ05Y5AEa1pZe3xd1jJmTccnH5cEvsQ70dXV4xUVWSnlaFFLKlW7sCabJXedokWRwwo_jes0hnUyH5bZK85tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش، خشی و021کید به نام «کاتالان» منتشر شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/82889" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82888">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فان هیپ هاپ بابت تشدید تنش ها در خاورمیانه ابراز نگرانی کرد و خواهان توقف حملات نظامی شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82888" target="_blank">📅 14:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82887">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">شاید باورتون نشه ولی زمان اعتراضات 401 دلار ی چیزی حدود سی هزار تومن بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/82887" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82886">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIQEb_g0O1i3UVO9TbRORbCMo1sycVPM_6NewwRF-c0rbckJEazPAix3AohU-dxo2LYDP3OAjQrASLbRa4x214ev_rSss8sF2zgr718OyGKQtuoPWdrshbmfMUEAb2tvueZsivUphw3fg8Wek7HdtIMy0hFlJFMRfRfKv-a2XwbDRO5oMFdZts4Qt6DJRKqgB7C1RZAGKG9JR2z4o5jrCRe7GeHbKxva1v-33usJQSLIRSVKCEEoMgjZxS4Co2WpIhZqPaJD4YmHvsoEVncmQpIYbL4nECc0Iuv2OLopiCHKsQ3avhN6kP_I3fHGwq4X5kiFV1FKFEG3ZtdxGqmonw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مال دیروزه امیدوارم الان گرون تر نشده باشه
@FuunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82886" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82883">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TnbalF5gLpFqYT45Csn-UJbmtpF9tJun9ExUzERcJS90Bl31uN5Loh-V2fT8Wuha1KoZ5x-uQV2PODFqST7hs1B9SsG_412MMb-lvgggHs3nILpwyZyNEGPIxmYj7GHdd_1m2MlqO7SHkj3WHynx1U8qJgeSHQg4rlaJq1E2yLDS55iKulzRMHILmdMDlN8WHprggLfIX92PiqHiN-arE2y_fP-NBmE832xtInfpCIQy24yAiAo3Q0QUXdIm1uEpf1-CiQTDsPsr3c6MdMvceuCVbNQ3pJlVBHwzlyLYEZdvfWbjzTPpAUn-rYO6P7lFgaDunmctvDUAn9IeNoRj_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید عرفان حاج‌رسولی‌ها و آرتا میرحسینی به نام "مست سر صبح" ریلیز شد.
SoundCloud
YouTube
Spotify
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/82883" target="_blank">📅 13:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82882">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">دلار 222</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82882" target="_blank">📅 12:43 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82881">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کویت اعلام کرد پدافند این کشور در حال مقابله با پهباد هاست.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82881" target="_blank">📅 01:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82880">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انشالا هدف بعدی سر زمین فلسطین اشغالی باشه
سپاه: پادگان تفنگداران آمریکایی در اردن موسوم به کمپ تبتین هدف موشک‌های بالستیک قرار گرفت. تعداد زیادی از نیروهای آمریکایی به درک واصل شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/82880" target="_blank">📅 00:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82879">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تو وکیل آباد مشهد یه ماشین به تجمعات شبانه زده و ٢٠ نفر کشته و زخمی شدن
یه خبر دیگه هم از شیراز اومده که فعلا تایید یا تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/82879" target="_blank">📅 23:56 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82878">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82878" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82877">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">خبرگزاری مهر:
موج یکی از انفجارهای ناشی از حملات آمریکا به یه مراسم عروسی تو هرمزگان رسیده و باعث ۵۰ مجروح و ۴ کشته شده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/82877" target="_blank">📅 23:43 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82876">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_j3UmyAlbhaT28dqBD48hyBPAj-1lbmmt9yRYbw_jStrqIwWvFu9z_R-R9G6VP5cMfwS_s6F1l-VkjKdYB8v7Cts2GgzGMGT5cURwOtzNBYGnxNC0XrVzj6QlM2YBlxkQk_EgDWYVxSFWVjc7jFeDs19LTHUBNJ0uD_9WzPa5OVGQGUh_HLEK4-05bG9QZm_MAv-QZT1vTWyZL3Oh74USjtdxctLTK0TeCD-XYh3pYedsXxBnBRXBJp6jxn1qQGv_t_dibCit8Vj2el9uYhSiyTXCL4yFP9QQq4ZCJkPvZvmLGxb_tkUKw70BS-WpiSLuyb2ABpXE39CDpZQSv0sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عیب ندارە قهرمان، تو همین ایران خودمون تو مسابقات مسترخایەمالیا شرکت کن،با ترابی و بیرانوند و خلیل زادە و علی اکبری رقابت کن.</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/82876" target="_blank">📅 23:09 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82875">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n9pvAp1Ge0QtgjXyqYllGwI2x4283vSLUYOSBJ6YP75mfVVwTlAmNw-l0DOvC5dH2VK49hz-FD0LxSC9W5YtVK0w4tET2HtduDpFzk07EYRTDt4L4qfd_-wptLnmydPqwfD4AmBlUyHzKzhlfIc9I5gSKWybPQR-FrT4ou63ptmTFDSPzxe8ka2kLUkPKY4v8RkWbNvBtb4SR7m-oQKacB0U6MGszD9kaE7wURk9utbGOtPilHakenUM3M9D_wQ2sGY3AbrO8Q8-2LpP8vfpROuIM7oFvSR4_gVd2Li86D0AlgbPXhxhH1WezSG3qYqN1dMhX6lHr-mHTqz3mB4HUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بشر خیلی خوبه
😂
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/82875" target="_blank">📅 22:46 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82874">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/my2aOOsh7QyUL7U4w7lZ4B4MWydUkl4GPVKNrFinKRXWy2L-21mx8jBue47BEYtJDviAN4Xc4T_nL9qCZjyxYhaQXoaBMeReQI0lD5Ysll9L-aBzqbF0jpCW8P8TYjBFXLv_WlrQ05k7cCu9T_WZYhuzPAkj0lwwjo0AFu3oGagxTf3nv0LsLR0gQkE2ZuT789CDx6pE_KmKeQKOQKHVRXFaYO0YYUfzh8jHr6iLdmJs1tUlWE5_4-RBwOM3rzX6rFEeWiDiGC5FeHO3Bo3yUmfjfOLCkzaizNj93RzCtbBlzojsRz6CIfVdToD-To_FU4_p81V_tXCYeqQwRr4aNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چه کاوریه گوسفند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/82874" target="_blank">📅 22:28 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82873">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">انفجار در عسلویه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/82873" target="_blank">📅 21:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82872">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجار در عسلویه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/82872" target="_blank">📅 21:54 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82871">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فرودگاه جیرفتو زدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82871" target="_blank">📅 21:47 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82870">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91af576da.mp4?token=uLCmhboubVMBTZ6lDVRZA34m7m68atV1CF4lbABixWTHxGHOWJnH_vvfflpZF1HeE9NHnTEurTK1HHT1lo7EflUB-W1lM90umbImTDeGDi-deyELlZKAMde9k3RoyU8-_OUovZL1q2G8QaPBeTdsGEcAv5mvv7aeCpWg2udR5gclqpytU9b1lRedVzzwk4nbX6z5W9p0PekKBQQPz_Kxc_-JBCVwZMEsX5nBVfED4OuC_Vg3ihYuox9P7cQd3ul4C5kfW-x-m4wFaz3BxrV3DBMW5Ngb7pdAJRCaZGKv_UlF_TypP8ZQbmsVAleyuK9YzGtyZo8dRnUhcpRG-xdZ-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91af576da.mp4?token=uLCmhboubVMBTZ6lDVRZA34m7m68atV1CF4lbABixWTHxGHOWJnH_vvfflpZF1HeE9NHnTEurTK1HHT1lo7EflUB-W1lM90umbImTDeGDi-deyELlZKAMde9k3RoyU8-_OUovZL1q2G8QaPBeTdsGEcAv5mvv7aeCpWg2udR5gclqpytU9b1lRedVzzwk4nbX6z5W9p0PekKBQQPz_Kxc_-JBCVwZMEsX5nBVfED4OuC_Vg3ihYuox9P7cQd3ul4C5kfW-x-m4wFaz3BxrV3DBMW5Ngb7pdAJRCaZGKv_UlF_TypP8ZQbmsVAleyuK9YzGtyZo8dRnUhcpRG-xdZ-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه از خمین موشک زده بعد فیل شده و به خود خمین اصابت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/82870" target="_blank">📅 21:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">زدننننن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82869" target="_blank">📅 21:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.   Soundcould  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/82868" target="_blank">📅 20:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82867">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWg8NwkdR4QIC-W_kDMGznJ8isT8QGsVAPKfTj7PhzvRUjn1jcgepHXgG5dbo6VlhWk3WMzW88mR2k6OWF6KmKQdzXteiAn6hgMSEDudxV6AWmeXtp4uPXErQV3Sh5CcDkytX8MetvgmZA9ZfIOV3CVSYBJAH7uueftxhxUPGjKGwwcud8vHO7CE45OrE4C8PY4odwhn6LIff25Jv3XKP1KXXEvUNF0JIV2hiysLpI7FnGZDgP1F2kqpepGq_MetLSYwjbGVaHrKeqWTMlgqjbFChJeCOf5oWZ_OTZz-au__yFksOqisnViH8uL7TzItcupcvcZhx0lf6H97o1APow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سجاد شاهی به نام “تا ناموس” ریلیز شد.
Soundcould
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/82867" target="_blank">📅 20:36 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82866">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بندرعباس صدای انفجار اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82866" target="_blank">📅 19:37 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-82865">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فکر کنم اعضای وانتونز رو یا ایلومناتی کلون کرده یا پیشرو جن زده کرده، لاشیا همزمان تو همه پلتفرم های سوشال مدیا دارن پشت سر هم پست و استوری میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/82865" target="_blank">📅 19:32 · 10 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
