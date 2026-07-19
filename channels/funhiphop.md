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
<img src="https://cdn4.telesco.pe/file/KU2x9gC7cdFQxRf6VfrnFb0Qeq4CCntXZpQ00NfSsBA9tWbcID7wZCjw9ocSnocU7VmZkWEh1Uxf23kR2P_A50y_P-4MRML0zDAsUsYFK36EiRd5bjKIq3ycJa2D4ehHP--0H0lFjTVtReNg5KT9TrJ9Upo5Ja7l6LA394GE7dVDGZdVupLk5y02UJxLz4YXIqTuqcb26zwqdG2975RfvPQPUT8LCg1mCJ4fHFxJXJwfQVf-5ywEgqypi3wZW_1g0c7gA7c1HrBXdz7z36y0yxs7DDjXtEvhnXhb3x5tU1oGLcOecP5R3n6GQT7-rOGQNHDKnoSDAyaiwD237M2foQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 196K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-28 21:20:57</div>
<hr>

<div class="tg-post" id="msg-80753">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JP9qWN0wD9ZKGLBVRPdYtHdzd1eWbsrVnGPPop9XoQo2eXrK_GsoQI84TMrILSdvg_5FLo7GdRJz24yRfbzrg0FJ5ozpsV2p6tOqBMAxxTrPpbTbf0ZnM4T-fdy_VtVfHxfCqvlI4k9bcg2DzX_k1m3nxYp-QZnQB6U4AYVkWiklEa8M_GgpooSqRCJmxJfYa0h-y4FGpFzogQMS6jZlcH2oAjNw09TLijMEaCJEBflY-41R6zUugx2AqapTu9oHycPCf5JxlcyDodeiPl0a5wPfev2srHW9Wjtsch4nf3-f0mTSyw6hdWMFZI6hm4Cr3zM8OGlfN2Ch6emzF5CNPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دمت گرم این فینال رو هم برامون در بیار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/funhiphop/80753" target="_blank">📅 21:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80751">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-poll">
<h4>📊 کی میبره؟</h4>
<ul>
<li>✓ پرتغال</li>
<li>✓ مکزیک</li>
</ul>
</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/80751" target="_blank">📅 21:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80750">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXkJ2r09Z59BLBwDCJHOgI_eiE2c4F0c-3RbcNl8V1EFiNRPSyLZEueK5NmjnhKocu9nZmUfCY6F_xhiqq71O2iitziRFzh-LXMaH0AqY0vjZr1ZHtMI6Q9Y33egFwjozWIwHbqfYXpEBkg-lw0vznJ72bNCM875WxJ41fT793qiw3QOY6G9WeclMN23cBpC9X8MQu89jHLLHeeTJW1CukJ7k9VGENybrCk11xpBM_RB5aGud3ES5ZCYk4BYqsEHFBwnyL7kzO5nbECMw8qU9ffE1SSHZ9S_14pE_G2WLUFfdurq-z0AbfZjzeC7KdgMOmekF5WYWpFduTxBRo2cfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست رونالدینیو
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.76K · <a href="https://t.me/funhiphop/80750" target="_blank">📅 21:03 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80749">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">مسی فن بودن هم دردسر های خودش رو داره  تا آخرین روز جام نگرانی و استرس داری  ولی‌ بازیکن های دیگه خیلی زود خیال طرفداراشون رو با حذف راحت میکنند   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/funhiphop/80749" target="_blank">📅 21:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80748">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">مسی فن بودن هم دردسر های خودش رو داره
تا آخرین روز جام نگرانی و استرس داری
ولی‌ بازیکن های دیگه خیلی زود خیال طرفداراشون رو با حذف راحت میکنند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/funhiphop/80748" target="_blank">📅 20:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80746">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">و رسیدیم به آخرین بازی مسی تو جام جهانی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/funhiphop/80746" target="_blank">📅 20:47 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80745">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jnvmqqfh_v7Dt43hkVS4OYoxgk0-TnbudWGO0E_CcuohkY9u5dl6U0k2bMJTqoc7r3evJhiHPg5Sqv2ve1raQjXBFdTPQ6oHkShkiP0z7GY0UzwFUcGlqf_uWCf8uHBvw2KuV2XsqNool9D45XqSF83EH3QtJPYqZCVqiAd-83nBL7WEPb879U5uFrPA25jVBaz436iylTAtuNUoAby9achfOcSVbyb1ey-prz7hAeQuFRdewU-TeyxqijfmHi4Dd9YSRSwNhH2XvYIKg-nx5SNjYPCpsWl4v2deY0GUdecL0GEXf0ZUOffeCB38r-5C_UWU50N28ZFcyk2sSnMsKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری فران از فناشون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/80745" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80744">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترکیب دو تیم   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/80744" target="_blank">📅 20:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80742">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kZAOXrzQAj5em_84TlclNJjaRnKE6vdqEnRCe-RYea7er6AwtqFjVc6lZHYL1dR8PGAZ9GGCCRp6R8dKuvBuaUejbpmuv0sIzvwda_XSSvfxsOoaya77Je5Jss82f8j36kU3F-bnt_igcbKlAbI0_4j90vr8VbuPny7hpBaRq96ajAbaj3zK_tRTdpaR6b1FT9J7UX7xxtDZLBR3m4snyVzvDXxzSdaYOMVCDBz_ddEkK4CQnbsGYxqyAMP2OsbSSVfDPE2mNYOHcOrBOV9tw-7BHWW3vmyYBmmRPpWB1dgVpQvdpUfHSHulutjSU_dWEMGW5PuG-_cB_-9zcl395Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EkusIygnubGxCaWwEju03pvw9yI58gIBj7VcZfMxpS09ZN8d8OCRvaIQj715lml7tnKpjqeVuX-I3wsTLh7OOl6HcpYkuPCUDJi9h-1AiJBg89ZUI0o9ID-GSdZqP9iIsmcovEuLPiOLTp7u5a_l7kaBwMZ6GS4uy_Gl5KazknBnmeoSspIPxqJ6XEOzh7cu-w_j0bwazYcmAKOtjL_jQQKLn0muCHwYWDeJHSRjHg1W4xDNlBlyPmRIePCVd0McyR8HqbrcTSk5tL_-iBNkHGVIIdXwcybR9JtwaixyutItvaU7bs7URPbr0taqnFu9TQoE5HFOQwIy-TcGfm2t5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/80742" target="_blank">📅 20:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80741">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwDgLPawcwLRhuUow0EyPqDqW26rsT6mkKIZWcjNUJn8eHRogcf9mTVc0Hk6LeOHslysWbk4zA8QS6wZsf51wHxieXT9BQoIfWRZ4JoTyAuI27xy2qXkA0toQ872hv3II-Aj3XopwnDd-w4Iz4MVVkWdipZKuRhz9e_D8oJsqWuwU7UrWkqNnB0zTZ5zsFY52ZIC0i_N5SQ_2qFPmoIoPt6eqTYnUg23QK79UfLBgLsI4rUvAJkvJ3zjo9vZtFu-JU8pQdjDol0oyczQ7XD3Gv0KpSeDu9UIbXfWljld3Q6gRRZEqNJN3A04kZWkWEtvSnrGGuiBxmFNVjS40AZwhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا باید یکی برا خیابون فینال جام‌جهانی ببره کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/funhiphop/80741" target="_blank">📅 20:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80740">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80b6ad923b.mp4?token=Fb7IIBjgHRtSF99jUn7IMRgrARxf0TXD9RXwKdYtXYqYX6eBs7YC0dyrCfdRmLI3IHrljyOm36HApqzsmuldpEPT-rLqLMiBGyUtmlMV1s-lKF-sQgD5bVyFq1oYnniw6A2DFJNR4agdEULdMSnRow5_zjI94XyoAoE-tBC09QngMVqu4ZZtAdlNc8so2KHxf9C6SI0l_H7iIRNBZbpUQSdbdxwF1PYu2krZILlsrpmBwnmRziTu1--OWnRIZvcdVIgcbrQ6gB0fpKrw9fG1GLXUMffDHnGj-FHYiU6N4re5Q4HRi4-KqwqwpTMOoA3l_X0N4i4kwnjXLuyji7nmtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80b6ad923b.mp4?token=Fb7IIBjgHRtSF99jUn7IMRgrARxf0TXD9RXwKdYtXYqYX6eBs7YC0dyrCfdRmLI3IHrljyOm36HApqzsmuldpEPT-rLqLMiBGyUtmlMV1s-lKF-sQgD5bVyFq1oYnniw6A2DFJNR4agdEULdMSnRow5_zjI94XyoAoE-tBC09QngMVqu4ZZtAdlNc8so2KHxf9C6SI0l_H7iIRNBZbpUQSdbdxwF1PYu2krZILlsrpmBwnmRziTu1--OWnRIZvcdVIgcbrQ6gB0fpKrw9fG1GLXUMffDHnGj-FHYiU6N4re5Q4HRi4-KqwqwpTMOoA3l_X0N4i4kwnjXLuyji7nmtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت خونه ها امشب
پدر: نگاه به سن یامال بکن
من: نگاه به سن مسی بکن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/funhiphop/80740" target="_blank">📅 20:22 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80739">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امشب فینال جام جهانیه؟
بازی ساعت چنده؟
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/80739" target="_blank">📅 20:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80738">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اسرائیل تو ارتباطات رادیویی جمهوری اسلامی نفوذ کرده و ۱۰۰ دقیقه قبل شلیک موشک ها از هدف همشون خبردار میشه، این موشکی هم امروز تو اردن زدن همینطوری بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/80738" target="_blank">📅 19:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80737">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f776ec876.mp4?token=YOC2vRW3-5E1MolYcnQkQb8qY7hjVw98FBL4xT5ZpNmatSKIM2W1Ot0hAhvYgeosnU2pYIEbXXC9BpnsbimJ3o3B99k9uzOcwO3oRnTCojIYr4siT5vP7moCtqFpvOfz9Xzfmr8DLyWFMnazZ1EAvCJ0FyUyojly5DesF3Rw_SnIE4OdauS0vHbsc45YprCNXv0e8qBXbeaeaO1IrXpLxbvdGivCNaYeGLaKRxnuI2rQS0RnQ6ZXced1Tv01IMKQwh0sQpRHR8fzvU1IlXL1wUHqnuoQXMTmhmVKOpBt2aaS45QpLcI8ZYRPhPmsqkevRJQyLIEv3YJs19HLwPcK8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f776ec876.mp4?token=YOC2vRW3-5E1MolYcnQkQb8qY7hjVw98FBL4xT5ZpNmatSKIM2W1Ot0hAhvYgeosnU2pYIEbXXC9BpnsbimJ3o3B99k9uzOcwO3oRnTCojIYr4siT5vP7moCtqFpvOfz9Xzfmr8DLyWFMnazZ1EAvCJ0FyUyojly5DesF3Rw_SnIE4OdauS0vHbsc45YprCNXv0e8qBXbeaeaO1IrXpLxbvdGivCNaYeGLaKRxnuI2rQS0RnQ6ZXced1Tv01IMKQwh0sQpRHR8fzvU1IlXL1wUHqnuoQXMTmhmVKOpBt2aaS45QpLcI8ZYRPhPmsqkevRJQyLIEv3YJs19HLwPcK8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این قسمت مصاحبه جدید عراقچی خیلی وایرال شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/funhiphop/80737" target="_blank">📅 19:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80736">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">سپاه یه نیروگاه برق تو کویتو زده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/funhiphop/80736" target="_blank">📅 19:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80734">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد   YouTube   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.36K · <a href="https://t.me/funhiphop/80734" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80733">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UB1rYcczZLwjHlw-RPOJ9_2MgJzjVrZH26Vf-bgBbh7jWchdifpx70Ap1RpyAWAle8gkAvbaSjJQJVNUXHrbQ3aeaTyWX1z0WbVT1-LLkC0XZaduqP4dRk5VKll0oN03zmLlIw_jR0HG2LiwRluQhNHEbydENtrLqlcj37c5Ld_4On3YNyx8EbPVm5DuN4MwS8BGDE2QHPET7K-PIf6nTX4vlLq4fmFZ6rVIDZrWxipYgPlqE8-o4rfZaiRy54FaYHPbVA2GN-0k4NRm-gPby08r3wFpgwIhXrPeHIlfEdnFp5bQloTS7Se1XzHhpZN4u2vDMK8sh8C6jcWsubTXHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم راکستار از گوچی فلیم و اشکان کاگان ریلیز شد
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/80733" target="_blank">📅 19:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c6TtcmNGLP_4Y1ae-1XK6SRA6ExyIm_OuCdMzUrV2Hv09nQCYjjjjRLVCrSDyBbfgJFrNuafpNdmb011flI6nOPmFdlqoaGz7AVO3pxSDxvtYZ_L-N8ZxhD702drkfWXrsXZpWmvX13aJzInTU6ZW31B7C77yQYBo7ynOREOd3c1vgCxKY4QS4L9UxlPAbJDVukOTksCu_mfYwiRxarZTMTBhmz-F7Pu2d4WBOWzTCuFuiU3-ylh0rjpRxv-HMIg_m5OZfXuzE7jNTt_o1maHlpG1KEGJjxD6Hs7aNUkuD53jHog8iv8FdGI-ardhPBYv4cyCFHb3c7bZNo87KIWmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا وریا یک اصلاح طلبا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/80732" target="_blank">📅 18:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80731">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خیلی وقته چنلای رپی پست نزدن داریوش ترک‌کرده، حس‌میکنم یه کمبودی تو‌ وجودم دارم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.44K · <a href="https://t.me/funhiphop/80731" target="_blank">📅 18:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80730">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">تنها دکل باقی مونده نرخ ارزون بنزین بود که اونم اینطور که معلومه قراره بگا بره و تا خایه گرون شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80730" target="_blank">📅 17:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80727">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VUr1sD4yAZHU4HTF17Y7LzEiV4lPV7WAnYcfGgt4edri8nBV2PsL6pVueTtDdpSqJzLyFyKgsLDiKKzwfPWt9QERk6hXRAOa_8gp7IcJonpZ7G9G0W9YxV7DPryjwFs92jifYJjA9JDL22NvRliuI3NOPmF12SQhpXXa_-hWhv604Uo5OHhCbKPGZOxDk09zIxTJV-AkuQLtY4t8fxtg-gqKXQLeovDRB1uXQrJgz3smDc5xE9DFOTtssr5k9okG7k-6hzO7XObWOtkHwe3bYB6cyzOWSY4rOTghIEYbtEKZd4fz3vX4AhvrujlMzRV4POV7eahckFrgqnzkqMolqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OzuG5Gn-Y-4CDXqgQNjRICCS8R-Go9YnyVF5hs7VAdzpaNm1Y24Ug9iO4tU5C1xtROcG5vy2GHKS5X7svJ3-IPHOkOqsKlCtlRFbuRSWCzBR6gh9q4RMDgCZVhXkIJU-ciy8-L0ZkJrAHzEpc_PvvGVfTEbOG1dyjWi8YkOlgG-_TjOcJ3XlOKlc4hZk3V5YvTbUMIUCQRDJ_aYhr-f6wNXKEnldb1l0NBC9CpQu69lrxX5oQCgXJeB2LDelkf-_1IWacrMFweYx959_e_ZeeclR1EgxFz2aqPn-zwdMRp9Lp-w9_szLqeVn1vzuAKzyqcOq7Aw4Dga1dgss_2W6TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PkZ_Slx1kPeeYxSSi67hLkPaYEjwUYtTLY5ezsruYgbYN6xEQvJSVCKRbewzJYMkwOV0oM3Cw9vVrrQwOz9JUCha-mA4SWBUL_l9JsaQFofWkBxtwOMjn7ouCBqlotfYD0zoy9Y7cItrjWbr77-7aQPY-iRSrojfZi4slzuBWfiPl2OkE6oI39XmpYC9UBYft7yP_KEtjewA3JRegL1aQKQTpCFOzDVg5xbvxru-LBipDHkI3j7atOVdrU71lwqNoaTviQ4FWq2JaSiweITPQwhG2kk39dn9AnXFjbIQ9dYRPfv72_veraihPmOOaFNG7nnsKi17SoADVOpNM5CHtQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیس ال قلعه‌نویی:
وقتی میام ساعت میندازم و کت‌شلوار می‌پوشم، شما باید بگی به به چه مربی خوش‌تیپی ولی شروع کردید به مسخره کردن!
حتما باید یقه باز بذارم و زنجیر طلا بندازم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/80727" target="_blank">📅 17:24 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80726">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAvalNetwork - اول نتورک</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtXpuWkxlxaNXugGF-Wieq2Llux2iRrQ6sukbuVNUAcD64HcrXxAkU7XfNNiyAHBDkCrCmIYw0ZisehunO_a-mMgdFe8icAF3k0EjPWIdjWLG0U0fM2TM7xgza7qeBR8Wv6WCR1GC526DCYE3C1QmQbQnKwduk1m7xdfcIoWg_a1k61Xz5qB4-Fq4BY72mWgVMemdZzq5JaY3lyZ9JkioQWmVt4nhWHxkXYansHUfhghTa8EHgeb4hz-YtEH1ZEdw990hYoh6F2oJDLEkZtAiE_c0oKZ3KYdkLEUZezuJT01el0c3PiUeYGjcGRfVSGxmu6e_jA9cn9R4ZmWwD6yyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🤩
🤩
فینال جام‌جهانی 2026 رو
رایگان پیش بینی کن و جایزه ببر .!
⚽️
فقط کافیه روی دکمه زیر کلیک کنی، پیش بینیتو راحت ثبت کنی و منتظر بازی باشی.
🔜
زمان بازی: ۲۲:۳۰ دقیقه امشب
کلیک کن روی دکمه زیر و بگو کی میبره!
👇</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80726" target="_blank">📅 17:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80725">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فرهاد مجیدی اگه سرمربی آرژانتین بود خطاب به امباپه و اولیسه میگفت ما جامو میبریم اونا میتونن توپی که باهاش گل زدن و پاس گل دادنو ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80725" target="_blank">📅 16:58 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80724">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5BP00bQkFEObZH_lKRPgGJz5fdClxc9rC-Ai0ZRpANZZMlqXMSoYkCRtNt41nh6Jvv8IF8pQmDN8bKRQ6l_jp0MR_GfVAMSVKF7cYxiOWNKEhEVwJkqeYFhAwuCj6YfW7_msJEnWGqLfwn-G0LG2_1CmPMzPPcuDQr-Y8ZinqLZaUXMtsyND2IMM99mXfye44C3-xSj3Ar8534vYgw6cbK0l2YlHg95psyW0kk6JAht8K5ouQag-ZM6QFFBb7dXZ8P3fQAKOCGAR-FvtO8ee-tukq_2da0DDlU0iWmU0_-HWz67aAbBaQaWI535fPG3oensUQDlImxEuNx4yG7K3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۴  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/80724" target="_blank">📅 16:46 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80723">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چند تا موشک زدن سمت اردن که یدونه اش بدنه اش افتاده تو اسرائیل و ممکنه سر همین اسرائیل وارد جنگ بشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/80723" target="_blank">📅 16:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80722">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">چند تا موشک زدن سمت اردن که یدونه اش بدنه اش افتاده تو اسرائیل و ممکنه سر همین اسرائیل وارد جنگ بشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80722" target="_blank">📅 16:05 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80721">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhnzxWPqZEdxSJBGv3Ea1B_5Ts8qJFHm35tbWUBIWtFQZ0N9IqDdgCIPSdHtC9A4MGTXacgnarZVWHQx5acChau7KI8kSj7zK4JcWAQy4eUFGP6FWM54yfjhT2HVivuXQrh57r0iixCswrlNo7pckBMNzswr9RiWcIsngevGvl8yUmSiBZ3glf7O58n8H3QUuyRGZain9-FWMREt8Hs-wGHh72AXkOlrKWZ0b4e2ReFrtcPBuTUUQFSO_No72T64fvxuDRX56giykmFYSzNcwI46l185UXY1lmlFFUrkDur4R1ZQ7mhJ4Lbkb7sFpG8ByjqY_gosWv2f56ifp_iT4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا یکی دوسال پیش هم همین قیمت بود ولی جلوش بجای تومن نوشته بود ریال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80721" target="_blank">📅 15:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80720">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/biXeEm2xa8vEGQtgkF7TuTt2LKHtshxo06JrHn7t0l0rnmclh7voJ7eoHeFpCGwLBI_iBu2SFM3zmcnDC9iJ3tYpdWZGpC4_A1tMJswMcHrY8qUMc35zCYZHdC4QvAa4l_3TlIHdETxTOXkoJiwMP-bydjWJY5nMMWzgTvOI3vErOvK0uSw-W4XZm8bujmPQ2e6SjZ6_xEntWNVJ9Zx6Azy4V0K2wziUGfXvpauOJVgcSLcBk-8Maf6V9GhS0PlTxPtBPGzkPrXrN189RWViKbUh0tHffERib5hICxr_Crc82-nkVczZUk_7VEkMpPgi4YjWMeuf6wuIAU3-TL34ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کسی که دیشب باخت ما بودیم نه امباپه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80720" target="_blank">📅 15:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSM6chEFp2CM7jaZYmAc0YOIG8wJqhAIhV7HY7wcmUNhTIx8gHXfgmHJljPbtXOYDfgu1k7_ym286lWvrRrObAESmLdlztsTnEiOwpH7FfnJOHoAmSHUmY15aQaQ5UpKpB7fE43qvsbr5DHWt0gybUQ0f11KIQefEujDejYJU83G4Ufudjr0RDwnGlUbblzSc79WQ4p7Sb74inY5G8KUmBKtj55vSvX7OzoqjaNBVcNSapThkjMXc6DGgp1Oe0ViewTjzj5B2jOzR8hLDRSaUUYbVIMDqR_qyfzkQxEMTV3XowPkZbmcfIlnGWs6HBKZLvdKC-p1WuEMe6ZD56qFAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇦🇷
آرژانتین
🏆
فینال جام جهانی ۲۰۲۶
🏆
🕔
یکشنبه ساعت ۲۲:۳۰
📍
ورزشگاه نیوجرسی (متلایف)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در مرحله نیمه‌نهایی با یک نمایش مقتدرانه، با نتیجه دو بر صفر فرانسه را شکست داد.
- آرژانتین نیز در مرحله نیمه‌نهایی، در دیداری دراماتیک، شکست را با پیروزی ۲ بر ۱ مقابل انگلیس عوض کرد.
- برنده این دیدار، جام جهانی را بالای سر خواهد برد.
- آرژانتین در مسیر رسیدن به فینال نمایش‌های درخشانی ارائه کرده است، اما با توجه به ثبات و قدرت لاروخا، قهرمانی اسپانیا منطقی‌ترین گزینه است.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r28
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80718" target="_blank">📅 15:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80716">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">امروز صبح گل محمد محمدی جوان افغان بازداشت شده در دی ماه اعدام شد و جانش رو فدای آزادی و آبادی ایران کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80716" target="_blank">📅 14:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80715">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">امروز صبح گل محمد محمدی جوان افغان بازداشت شده در دی ماه اعدام شد و جانش رو فدای آزادی و آبادی ایران کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80715" target="_blank">📅 14:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80714">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">دوستان قضاوت نکنید منظورش کشور کردستانه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80714" target="_blank">📅 14:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80713">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huPp9rm0dVv-FEZZb8In1Gs3nqa8svlBjrLwMDjHktFXXOfe4Swu7WlgPloWXWTE4VmQ2JY30lD2aMn75kQkhNJ0ayHCrhPV5Wu1iscG3UagOahgNnCd_08Q7TJli8JSlULxY_kqN8bSCRA9xxT1s2NKtqaiFNy6Z6Y5piurK9l20yObjyA0gerly-uesfa2VtKo61mkPMKw1whJYw3apYAVhC00gGwAuaq0yMUdk_N4ZCMm8KfF4U90Ed1QDRn6iZrNHQGY-LNSwhTTcer9m1Ro2v3HNnQQzs9xcJQuZfEaxF-Dd5cH-QDUGglId_u7drQKzF2qHNy_lhurrB_SbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وریا غفوری:
مشکلات داخلی یک کشور با دخالت بیگانگان حل نخواهد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80713" target="_blank">📅 14:15 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80712">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عجب امتحان نقاشی سختی بود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80712" target="_blank">📅 14:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80711">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دلار 200</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80711" target="_blank">📅 12:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80710">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دلار 200</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80710" target="_blank">📅 12:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">واقعا وضعیت خنده داریه چطور ممکنه یهو کلی بلا سر یه بخشی از یه مملکت بیاد، چرا انقدر ما کیر شانسیم ناموسا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/80709" target="_blank">📅 06:17 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80708">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یه شبم آمریکا رحم کرد خدا رحم نکرد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/80708" target="_blank">📅 06:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه شبم آمریکا رحم کرد خدا رحم نکرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80707" target="_blank">📅 06:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80706">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">اهواز زلزله شدید اومده   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/80706" target="_blank">📅 06:04 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80705">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">اهواز زلزله شدید اومده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80705" target="_blank">📅 06:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ خوش غیرت 2 تا از سربازای مملکتش کشته شد شدت حملاتشو کمتر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/80704" target="_blank">📅 05:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k6gmbAYf0r_t93NVbqDSmOukl_qEfK2NzVFMg-U5_U7VWFu5JTzkRNQFZFX-5VPiuVTQCTx9jiXlOoRznbCIfrdcAP1SKVQc0o1JScpKJ09X82OkG5MdaID_Ovn2j2bUcrV5k-XZgpTAYYA9hlki-C_-OVbMB9XzZiw5allrktVxLSVjZPkRX4bDkMX7wFkUM4s6T2DmHEk_PHlGX9dXrURMR1LsC3NxACMCA_jBCv4KCB6i1gtJHaH1UGjRael-vIh8AJ2AhoKocs9qo52W_nXTJyEHvFqt1iwNOtCBL64xyLNyQo5VX5nNcw0bJ8QNYkLXgrGSHuFXfQtaUCUGng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام بهونه قشنگ من برای زندگی.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80703" target="_blank">📅 05:09 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80702" target="_blank">📅 03:06 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خب بریم سراغ جنگ فوتبال بسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80701" target="_blank">📅 02:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80700">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یاد گل اوزیل افتادم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80700" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80699">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">عجب گلی زد جواد</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80699" target="_blank">📅 02:31 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80698">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فرانسه چهارمی رو زد انگلیس هم شیشمی رو</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80698" target="_blank">📅 02:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80697">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80697" target="_blank">📅 02:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80696">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ولی عجب فودبالیه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80696" target="_blank">📅 02:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80695">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">حملات دوباره به جنوب کشور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80695" target="_blank">📅 02:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80689">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">آمریکا حملاتش به جنوب رو شروع کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80689" target="_blank">📅 01:57 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80687">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZdcmBD7FECf5v9WrgMSNwqB8Kye4XOn5PHYASRZAmsUyv3ydS3F-y4FRW3r9Z97v3ZC91YSpFFzlu65h7SrywJOf-dTPO5eyBfSP95-CoSXFSJdp0uDq9TFpQROntROVNlaEMhpvmKkNbpu48UOszrP2-ZEmWoN282c3jkdFWFt03uY4YiBrl3jkF1xZ1jw3M7uO_-Ca64Za27LmzA_e3eovp1lqKHERHCAVZpYeQDYoHL9kzqCnH3qhVQ1vQNMzgfxCr1JkyFKYcy9FNdADPx4tgxt8yJOTPk_OQiu-I0umgdxszZFtrwyrutC_DYScCcWUXwwvriYOQznVaroWFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hxHOKruZEfMTem2O5Ouvzw-Cktm_otBIRJhDe-4Z1zJuHxA-HQnhjIrFgWOSwXnXVieVUB0a8xMRyNPFeUnSxWdwfWCiLATvreAC3bxI0lTxIEzUqkeiXm8j2Lfj4txmvkC6KyfuCpk6-L7OXuLUVAb1g5vHe2FJfghBMcdpzywGDBT06DMX3mM9xHGMz9O514hnLqZSJffoTYbsbGMm_ILZ7bEPa-LRddGOJHZDdCwuIe2pUnp-WkRJdwLVwrdfRfYK_EHKE_p8FECjdedWd72IuvnQKVobir06RTAQpQ7nBhI72iU0ypNfDaVKto82fZO5a540iNcrtiHCSLq8YA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میخواستم پست بزنم بگم لاکپشت کثیف کیرم دهنت چطوری تونستی بانو رو ناراحت کنی که جبران کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80687" target="_blank">📅 01:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80683">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSHtvw1GFMce4_dJB8Oi_O8AQy3rfD23XRdgStlynTc259wIUxYx5JBJO-Ut7u_tK3-7qlh-SqTZ9zI5WHK6eoQyLyeDuhcUKECaj8xm9X9DGCCKTY4Nyp6tBxqgequ9-YBJQku2Rc_hYVCBtI_ICBdu31Vv3biq0A4mrvxwzBRSmZxvP1ahhG0Y2dSCavXd-Z3fe_EU1ykQO-UkkC57K1DfgVHb1Y-sronw7SEN_mWI-c712AxppZiel8LWI7fRYn4jgGr1P4NS9VCBAzEVZ6QP8NFu8gd5LLjBfUPQwTGWalshYir9n1XdUuRnRJdBdtr3qHSPX3Rda_v5BMv40A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب خریدی پسر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80683" target="_blank">📅 01:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80682">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طرفدارای بارسا نیمه دوم تلویزیونو خاموش کنید، به صلاح خودتونه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80682" target="_blank">📅 01:23 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80680">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یا امام حسین چهارمی</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80680" target="_blank">📅 01:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80677">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">حیف که دیکتاتور ها گریه نمیکنن سقوط میکنن وگرنه رو گریه امباپه میبستم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80677" target="_blank">📅 00:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80668">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzoQ-a7g0LN7aN9wvDLzk87ojdXKJrIbwc-RsoRjYc_92yMQwW28XLPFLgTSbKF7qCqXlfssl2XnwV1MUKybBchmTXqU9ouBSZroLhc8FdlyUGQAcvaxyWHBd816LaexUSUPa5T4n6cov84XCyRaNbvdVyOCn0aMYXf9LdG7rxVofbrbrIH-xP51sxDpCI3eeBYnl_jQSM1p7qqUSdG3gynv-Evw9aUf813_sdS46CTjn1ufczuvXL6q4vnkVB93J2kfqPGUp10bzuKJbUTFz4zY6tfDsDqH6J1i7AqxLhwXL_s0wjyV3Z5htZPYM1l6vLpocbkoxbtLXcOi1HBu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امتحانا تعویق افتاد؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80668" target="_blank">📅 00:27 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80666">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">من دلم نمیاد تو حساب دمو هم ۱۴۰ میلیون خرج مورگان راجرز بکنم، چلسی چطوری انقد پول داده پاش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80666" target="_blank">📅 00:12 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80665">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حدود ۲۰ دقیقه دیگه نبرد بازنده های جام، امباپه و بلینگهام شروع میشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80665" target="_blank">📅 00:08 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kANaEd8i4xbB0x19a9mrjyn9czNdHsPo6qNrXqWId5vavPC6P7FAwyhJEdULKOcR_4IZ7x0EUIk6uUVRYJ-PzIJcnNfEd8HIXJTbtG8MzYf-xyBY3EmCC_HozrSrQyx2UOpxRkudZSRe9exHFi9lcXZQt031zVC-1DMkyik1VBRdTcTAhbu3j9AWZ1t1bzUxWj2HesABMe54ugklaD5JDkN2Sr-1vo7mV3FzhxvkYFEuyCMhV8x8DM4kDZHnDn3E4caVFLLgLiq_Qr3EsQlo3G-e0OyBmHnu44zriVPWhGa7n5wxXHO6WRjjAdVJh8ekcqShMqefAUkR0F6x1qe3HQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقدر زود ترسیدن میزاشتین حالا برسن بعد انصراف میدادید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80663" target="_blank">📅 23:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80662">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دشان جان بازی قبلی اینجوری ارنج کرده بودی فرداشب میدیدمت</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80662" target="_blank">📅 23:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دخترا عکسو آروم باز کنید  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80661" target="_blank">📅 23:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ol8FSpDMge8jEgFUvaswNSqSVO28GIk5U8mETiLvTb669sA_sSfaosoLoZYF-YPiMpJmF2GXsxrHl2t_2uR4mYIn38OpsRl9acsZ04bYKdhjzWeNUeOjj_hhGZtXCqe-D9era7EJQrulMGWhF0xVL3jt9yPLxFg728vBp-1r4i_q-GrlWUytSB9FxFGBoRUA-AoeKwfdDybYqAMdwFEFlELpelBXvvcFxc-5w9lQ3DZ1AJCpXNOAEoWAtE7L3_rMT20njArRxICnNNnFisfmpHBiluiTYzA8Sb5hBcz09dWhOeZtN5E7SH-_AUX06TTjwgS4jxEqyV9Kfz6OUILSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دخترا عکسو آروم باز کنید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/80660" target="_blank">📅 23:32 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستان مگه ایرانه رئیس جمهور مملکت بیاد برای جذب نیرو فراخوان بده و چارتا تازه کار بردارن بیارن خاورمیانه برا جنگ، این پستی که از ترامپ داره پخش میشه فیکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80659" target="_blank">📅 23:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فرانسه هم قشنگ معلومه فقط اومدن برا آقای گلی امباپه، خط دفاع رو ذخیره ها بازی داده خط حمله همه هستن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80658" target="_blank">📅 23:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80656">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انگلیس یجوری ترکیب دومشو بازی داده انگار بعد این مسابقه میره برا فینال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80656" target="_blank">📅 23:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80655">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ولی جدی قطع نکنید، این پولدارایی که وصل میمونن خیلی یبس و توکون نرو ان، حوصلم سر می‌ره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80655" target="_blank">📅 22:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80654">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه نت قطع شد بدونید دوستون داشتم، اگه نشد هم که کیرم دهنتون ازتون بدم میاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80654" target="_blank">📅 22:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80653">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">یکی به این کصکشا بگه جام جهانی فردا تموم میشه نه امروز</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80653" target="_blank">📅 22:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80652">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V7QgudmJE1ePi4FwNXHvwWx6MwTX8urZuc3i0N1PUEk2qY0OGWEc3ZZWzJ4QDsLaqTeLsK1aSakAkwyaKD3p_lSLaAVFDN4RYQJf9Wgf_VFjMt-mJN83GnGuX2l1SA06yaw3ydjGQlzQo0MeYjZDVSD28FGCinBcyorxPuCDgYRlz0aoYZs00Bc3ixZ7vJdmVcQgxfwDm3Qk419zW_G-Wa7oSNieVEgyt3VEPBMzdMuLVQheQcm4YSzvsgZDC4XRABFO1WQESq7yLc73Jy-DISxlyXaTyKkl_Rmr3OuXsy4EJyn4J1ojQbgldVCMkkcCu8Lxwptce9zTeiT-F_2K8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت بنیامین نتانیاهو از آرژانتین
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80652" target="_blank">📅 22:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80651">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">اسرائیل به آمریکا پیشنهاد داده در صورت شروع مجدد جنگ تهران رو به اسرائیل بسپارن و بقیه شهر هارو آمریکا مورد حمله قرار بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80651" target="_blank">📅 21:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80650">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">امشب به احتمال زیاد حجم زیادی از حملات به زیرساختای اقتصادی کشور انجام بشه، اگر جنوب کشورید از پل ها و صنایع پتروشیمی و بندر ها فاصله بگیرید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80650" target="_blank">📅 21:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80649">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🌎
اَپرا | سرویس مولتی لوکیشن
🔥
زیر ۳٬۰۰۰ تومان برای هر گیگ
✅
اتصال هم‌زمان به همه لوکیشن‌ها
✅
اتصال با ضریب در زمان نت ملی
🎮
سرویس گیمینگ اختصاصی هم موجوده
📥
خرید: @apranetbot
💬
پشتیبانی: @aprasupp
📢
کانال: @apranetwork
🚀
سرعت، پایداری و قیمت؛ همه‌چی توی…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80649" target="_blank">📅 21:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80648">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApra Network | اَپرا</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtAFByfnCcu2UJq1LFPkTlgMpY1mOeZaj72tkRqAUxMNmne9SUc3udpoegObd59BpvC_i2tz37l6TWV3dPeqAFpBcyyxmvp43QG5JBoIgkM-HaUMm_L1MuuUiyIJneusL2aBqIye0EB5SanCAXafTa-7xOmSNDyRKlJFxkNW7qlRA25GVcVeLRCCI-pnmDWzWJWLX1T89cSUsLm1WTBVWFzvh4s9X-WBDVpHzcq-M7io5ZQMp6niCU9p7PB8yB6XA6r3ZUE8ASsGKNFJArBCMUn1g7wubKE5B9bATRAlXwKGcqUEkU8r3uWLGVI44Dd_C7JDsX_HNXvMN7M-9tI4Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌎
اَپرا | سرویس مولتی لوکیشن
🔥
زیر ۳٬۰۰۰ تومان برای هر گیگ
✅
اتصال هم‌زمان به همه لوکیشن‌ها
✅
اتصال با ضریب در زمان نت ملی
🎮
سرویس گیمینگ اختصاصی هم موجوده
📥
خرید:
@apranetbot
💬
پشتیبانی:
@aprasupp
📢
کانال:
@apranetwork
🚀
سرعت، پایداری و قیمت؛ همه‌چی توی اَپرا</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80648" target="_blank">📅 21:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80647">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ترامپ کونی حرکت کن
فاکس نیوز :موشک های ایران مستقیم به نیروهای امریکا در کویت برخورد کرده و حتی جسدشان پیدا نشده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/80647" target="_blank">📅 21:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80646">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یکی از سربازا هم مفقود شده   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80646" target="_blank">📅 21:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80645">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عاصم حرکت کن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80645" target="_blank">📅 21:18 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80643">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سنتکام اعلام کرد 2 تا سرباز تو حمله جمهوری اسلامی به اردن کشته شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80643" target="_blank">📅 20:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80642">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سنتکام اعلام کرد 2 تا سرباز تو حمله جمهوری اسلامی به اردن کشته شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80642" target="_blank">📅 20:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80641">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">یونان اعلام کرده ۶۰ مسجد رو در این کشور تخریب و تعطیل کرده و هر کسی که مکان مذهبی اسلامی بسازه رو از کشور دیپورت می‌کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80641" target="_blank">📅 20:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80640">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RKQG5I0ewuxD2wxJk2TIzdHe9h7UlvCbNZYoYSFpBHJJQqa0GYKZZQjcc9ni9vVEU_u4mSymBeiR5sAIwk6pq79Dqj8hdGrwxK65I5ridfhn72ZHrdvcI7QeGLhpUdW60fVcnN89g-IpDNadvsqfUbWyVxLC0_875dpXBvOmmNlHnfakXORaY__IC1tAUx5ovxAHgN6QfBqM5xSpeWrSGbUMbTjnNDLIfmln8wMNMdk7Hd7a5tfnOZCdSrKs-qlPdY76mO1ZAaS_EL0a9GsAjP0vsq1pEsl6yLAqQMwaXxBVu7UD6hlq6PYaaGJ86F7VttQqGfVs5iDRWDCFMakrqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا چرا ایران  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80640" target="_blank">📅 20:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80639">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9gQiPhpY2jWPBzhVaja8xrpEeWRiTvkejDPe6ICJAAw5MENaZRVQ8hOLe7ZB5Q2hdclbMk0nvn8r46tDrUz5eLLChamujIFnS0KqAjGWIuZpad2mHAunTLN8ebXrD30sGhV2B02sBCNUUkMgsNBb3Jty5FNBavNwfS9O32I1TGUI8CzYKV-8DJ3mvomUxY87-Xb2Y8QR2bjlW7Xki4nO5_Ot9cbSG8VIAo90cVVRdI6Dr_rjzQNaVLxOcqDh2PQFeuUEBfd3oNatW_HlPlS2jZLZGX8Tfo0L1dg7lU5Q46fJ4GpW2P5-ZNW9OpcOngkhGi5t8rs6Ppx13MJiz_vgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا چرا ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80639" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80638">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rNocvbopD8Dhc5A7Mv9p2tXCqDMPucLoDghJXydJ-w_3Kx9zzm7vSn6W-2FBC1RqHG4PxMBNx3Z3jsdKJnbVdXu1Td5UvoUNXObKbTQb-jq_RdVEC7bXf-o4--e-II8dXrw9Lfma9lAkVKWrhkb3VWs-osfEWGYYldGugzMfyWQpV9fnICnmerLhy0GsyllSpghDCnu-BL3R9dHWvy2Cx1G6msEA-otUzCHHt5IqPraAzKYy_xzPNbyqCFzK5nDftN6qxlQSF8atbtL5ci-dhYSCVCoMT-5BaC7nq1X9ZWnTKobK1vaDoJ3-4JidmBItQmK8OljpjaEv_zkPRKxNvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🏴
انگلیس
🏆
رده‌بندی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در مرحله نیمه‌نهایی با یک نمایش ضعیف، با نتیجه دو بر صفر از اسپانیا شکست خورد.
- انگلیس نیز در مرحله نیمه‌نهایی در یک دیدار دراماتیک، بازی را با نتیجه دو بر یک به آرژانتین واگذار کرد.
- برنده این دیدار، مقام سوم جام جهانی را کسب خواهد کرد.
- با توجه به قدرت هجومی هر دو تیم و عملکرد دفاعی ضعیف در نیمه‌نهایی، گلزنی هر دو تیم گزینه مناسبی برای پیش‌بینی است.
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
g27
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80638" target="_blank">📅 18:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80637">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S1Ef2_ZpV9h8mpAzJkri4JTf4Ec0J9Lxr-fSsIKkhaWZZeIxVu6WyJyqg8dvgqZRfMzKhtpi0n8XpOVO6DQmXtm7_IFN0l54_AlYN3GmrY6t62PuYM-kjXZlem38FmevdYk32jsRcpPImeO9s5P6S4y2Vj545WnxkPKFev176cjpymQhTrIWCOCJRQe-i_LtY6wxViHZ8jyQdmO5ewWT-98BCLVPt3M1iT6hNClizVDcQG-1jiXW7W_Kn8gf8NE05mnUSx1PV-zT8iuxhsq2eOjCq9Yyf3BeERbOuxk1KWAuzUwjdBleVRh9IP5gjcgI5VEjJASAvo7O5kkMkblogA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوکراین خار زیرساخت های روسیه رو گاییده، کل اصرارشون هم سر بسته بودن تنگه هرمز بخاطر همینه که نفت بفروشن بتونن جبران کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80637" target="_blank">📅 17:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80636">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">جمهوری اسلامی ایران تعلیق توافقنامه و مفاد آنرا اعلام کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80636" target="_blank">📅 17:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80635">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIfPnMvUoYy1wXLe45aw6SNZ-Y5VLhnJlDPsDB8PtDY7hAdFghxl4nnsxtuzNvd3nCIoO1HMPgszoSkJAPzLNB_vy3Pm56-SrNgfjTczxvf2AX6BJt0oKnv6JGrmQx2tUOMbLEVxsPmbrhHjSJDqsrUkKKB2M7kVAVZPwu09l0mbngB2pESfiFyYV8v8b5Rhu_8p_jTPMKqlE0sT3-4c6bPQwWcnZX4LEsyzlnG04Fk6PkHLcfll0vwsKfsakmlbG05hM6_sq6AjMW6i5E91aCA9RDmjZ5P9kppDyxVfgQ4FXN7F5TQxNmEOlPoI-B2tKcMOM1YlsGWIlEGaWgH1Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عشقتون برا فینال کاستوم آرژانتین زده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80635" target="_blank">📅 17:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80634">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">این قضیه ۳.۲ اسپانیا جلو آرژانتین چیه، چیزیو از دست دادم؟ چرا همه همینو میگن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80634" target="_blank">📅 17:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80632">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RoFthmI0pQgK9XzAlTtpFCCdtkert-6aWlNZxFGerwsYuWR_mtiQQWs90Ggyf_09xuRn0heWMd_MPHA49iM8-8pSUGDjjCrpkqAn8FjRsrQ3VH0WduOQszp7x2BDY6vvbTYk8zuZF2Fi6W8W9c9VH947qxUfUYN1WUtkSglZV4GclkpjWBEPWMYM5-ZIm7VxLHQ7MTrqlPq3oRb6OKTc9nY0qglBFKTWNcXM36QUCjT5926TcArIDxaiQOnPAwSMo8k4zB_CI5Yf-R_8YoosdpSf8cEy9Rbg9w5bvwu9dUmLlkm5FEAPeQD7rBUaozzjXcyqnBbToDICcH79fGhVFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا به من ربطی نداره ولی آقای حیایی یکم شک بد نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80632" target="_blank">📅 16:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80631">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اسرائیل همچنان جنوب لبنان رو میزنه، آمریکا هم جنوب ایران و آتش بس همچنان پابرجاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80631" target="_blank">📅 15:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80630">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67c8c64445.mp4?token=MHvvHXBDkBoQcSoOyrkJ8LTTzEipnrjF2XbLWoVfToP78jI3N-Vssw06ymztyvZ2GRfHLJkl-y9GdcRP3fuhGZ7DNpY4E9sQdF_IYluuy-uWbQEZwFSdt7xBPOhQIFp5FTA8zlztgelvrg0yDylpJMnip4B31AW4kAnMDmjCV8maNxokeDLw8GAjwQq5mNXMIHNoSUrR35ui5ME58DZOSDE7PMtTrd1SchXkXf3XrZh0Ow0qlTjlgdxkJJPcyNLWcpQF_PHY3AX8APC6TW3oZMAQGl2Lrb0FYfHyz2izhhudbndfl72JAtUWXQYjUDIB32_MEW-aXZqJhJmJacYmqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67c8c64445.mp4?token=MHvvHXBDkBoQcSoOyrkJ8LTTzEipnrjF2XbLWoVfToP78jI3N-Vssw06ymztyvZ2GRfHLJkl-y9GdcRP3fuhGZ7DNpY4E9sQdF_IYluuy-uWbQEZwFSdt7xBPOhQIFp5FTA8zlztgelvrg0yDylpJMnip4B31AW4kAnMDmjCV8maNxokeDLw8GAjwQq5mNXMIHNoSUrR35ui5ME58DZOSDE7PMtTrd1SchXkXf3XrZh0Ow0qlTjlgdxkJJPcyNLWcpQF_PHY3AX8APC6TW3oZMAQGl2Lrb0FYfHyz2izhhudbndfl72JAtUWXQYjUDIB32_MEW-aXZqJhJmJacYmqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در آمریکا به دلیل پخش «اذان» از تلفن یک مسلمان در هواپیما، فردی دچار وحشت شد و پس از شکایت او، هواپیما به صورت اضطراری فرود آمد.
پلیس های مجهز به سلاح وارد هواپیما شدند و مسافر مسلمان را بازداشت کردند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/80630" target="_blank">📅 15:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80628">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CtvveeiA79ykzvjEMAmu_CNRtLtOlEIhSzrAy-6XQF2N-e2JcJH37kUlwWUTd-ezLgnp-Ncdb4tJDFrgvcfw38431nvPGkhnGQ6yKf7ZXmphSSIshPl12Y9tD3ENEk0smRZuhWXsXTL9xPiktV3opxXckq2NEgqrMrMUHdccAoq-THQ-Qp1eqmMfn7rx9N0aOWJ15KtaPy6p8dGB5sIOXAKLyTuSKCZqC8U5gnt03YrQc-fSeAa1cvyKNE-MAbcqNoXqr9fjN881tlg3BpE4h614xUe7yyuM2F1-zzaCZF5II_YKnSgaOO1uvBBIZP131DRl8jKQE9KVoa1Vwiv6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kGPU5TdRuSuHuqKLhZj-o5VcMYAW_ybp1Pvlpx35MwQJM9ZqJaJNG_8_mN6CB-8BHu9NemC_ayEHYA0L7v4SqGF_YA7wJpwXsEYLUSvzaLT3bW-pOctzu8G9JkRsCnOF_1N3Z4VVFM078QDtI0lWFP-fWO6HWaYaQ3Zb6zwJtJ2HDRN6RqOVRfkRZbRUE0NNqJosQnr4akedYj_k9zNGpa8MPK7_XPO4EegBnaFJ7KOKm3H8rnxEP1CXndHmAwSGBtLDT24hdT8au_Xx7aFCOLWd9GXenG0dr5T240roYqSSCRmg-fLYLFAJcQTmukdn94d_vlYf4aXv4tc2ApvchQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این سگ تو فضای مجازی خیلی معروف شده، چون همه فکر می‌کردند این سگ نابیناست، اما آزمایش نشون داد فقط آدم‌ها رو نادیده می‌گرفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80628" target="_blank">📅 14:56 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80627">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ولی خیلی حرفه بعنوان کسی که دوسال نتونسته تو لیگ کصشر بلژیک دووم بیاره به کسی که تو فینال لیگ قهرمانان اروپا بازی کرده و قهرمان آلمان شده بگی رانت خوار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80627" target="_blank">📅 13:33 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80626">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">خوش اومدی به بلاد پاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80626" target="_blank">📅 13:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31fa509f3a.mp4?token=e-zcUgF1XlLo1c1MOhHP1Gz2eUB3FKbbJA37m4tjoRrE0ciWc6pcVQ8UznWbVCUwn7e7WEoYTjordLtp8f7EiaojDvErdOc08BppKncyDWAhlpGrTb045VVqkAwdQgouiTn6ee7L6XutpHbXPlGu7Qdve0NXqS9UW2GtPwLIVQpMaiB6L8WXLxYT6lMaeb0PIK3zix6NSoPC85S6_kwX4CyVB_XzpkGtFDJlkUYRfPkeGOmsn9ayKWoDNvxe5EPK_OiwRT_lZH5i0Ox5JkvxVtpRPWM7g7W5_e-aB3qmzohyOEgBghn0T1sq-qrWUjELfhE-HdXJk8EYV6aHK01_ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31fa509f3a.mp4?token=e-zcUgF1XlLo1c1MOhHP1Gz2eUB3FKbbJA37m4tjoRrE0ciWc6pcVQ8UznWbVCUwn7e7WEoYTjordLtp8f7EiaojDvErdOc08BppKncyDWAhlpGrTb045VVqkAwdQgouiTn6ee7L6XutpHbXPlGu7Qdve0NXqS9UW2GtPwLIVQpMaiB6L8WXLxYT6lMaeb0PIK3zix6NSoPC85S6_kwX4CyVB_XzpkGtFDJlkUYRfPkeGOmsn9ayKWoDNvxe5EPK_OiwRT_lZH5i0Ox5JkvxVtpRPWM7g7W5_e-aB3qmzohyOEgBghn0T1sq-qrWUjELfhE-HdXJk8EYV6aHK01_ijzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قبلا مسئول شستن ماشین علی دایی بودی بعد الان خودتو در جایگاهی میبینی که به اسطوره فوتبال ایران حمله کنی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/80624" target="_blank">📅 13:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WrrTqHB4cnRYhd_Fa4LTWVeN-D3ZUUNb0wzWa_sukBGX39fmM3bxm9FG3A3K8-cORUTezq2p2KAcUizztH_UpKv4xp_-FSkhDfIP0pIvLNTkAzM-XCbnk8jkM6oml9QPcgF3E9jj-_iY94QPjZ6n2c7aot5LVE6C0l6ygdZiYvjXoIGlVoCYY4xHroE35RC9mJVNn2lyeFmHJ4ZZ_DZxs48KaFkd-80KY7SVTbc4Ojt-tGlxQCGewqLYqcDoRPNNJAoVyBSR7YaCF5ivNTKEoVASqx4-y3DDTfgr8J6j7EKEKMyKVFeidWW44vWRftImclVn0RQGzOiGH4sgViEasw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باخت آرژانتین قطعی شد، دریک رو برد آرژانتین بسته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80623" target="_blank">📅 12:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سخنگوی قوه قضاییه: برای ترامپ و نتانیاهو پرونده قضایی تشکیل دادیم و کیفرخواست اونا صادر شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80622" target="_blank">📅 12:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbfbfbbd0e.mp4?token=IIvzqSdHKOgntf02oI1sPlcCZHxTw957PrvKHgppLd3_U7zib1Mp9NNw7Ukh3o4K0aAVgpXlyZDHWxWI4aKczL0VijzVIMnb5mOHA7weXc0BInbI11I5rFoFv6xa336e9Zr3kyhmHXCMFRIyunDp6TzOb3gl955ugn0mNNrqheXwKCCqgckAvhjOVkmB4ZwUwntnrpnHScFqQH09RQ4K1guf1auInMexMPaXyx2DyfrgnDyM98lX6x0KUUO-EvCA8qV9v43e_rEDuJSV2anS0vLsXXV6YknNZ9ThJpsE0Bf0Z0lieAgrWy6rnYsjyrYPNNCWTa94nRnDNCVICKkp4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbfbfbbd0e.mp4?token=IIvzqSdHKOgntf02oI1sPlcCZHxTw957PrvKHgppLd3_U7zib1Mp9NNw7Ukh3o4K0aAVgpXlyZDHWxWI4aKczL0VijzVIMnb5mOHA7weXc0BInbI11I5rFoFv6xa336e9Zr3kyhmHXCMFRIyunDp6TzOb3gl955ugn0mNNrqheXwKCCqgckAvhjOVkmB4ZwUwntnrpnHScFqQH09RQ4K1guf1auInMexMPaXyx2DyfrgnDyM98lX6x0KUUO-EvCA8qV9v43e_rEDuJSV2anS0vLsXXV6YknNZ9ThJpsE0Bf0Z0lieAgrWy6rnYsjyrYPNNCWTa94nRnDNCVICKkp4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تشکر پرسپولیسیا از علی بیرانوند برای استوری های دیروزش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/80621" target="_blank">📅 11:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Kyt5L-w_I_kTYEozLO2DJvc2wEce91EAbLY74OZVZLA-7oqW-zZIwg_8VdmUbRj0YEX6lFeEUMZKrW_39x8uzXefVXt-30EUUgZkOAG7xT8r4kAr66m995bOhRzivteALM4yyvjuBsHn_DQdTq-1m0ooQN9icn3zY-j3mnEnV9WRT-s73ERDnbXbA5mhuSsgKFuwfrcZ_CcPo4e-uH0YfBDQ28i06kMS4gevAerv70pyVUCGVmTiBHVd_PNh8uHbXM5jSPkaQ5p7QUk0pG-z9o2gBuv5wNosOD7yHnU49iOVHioiqF97PeCqum01pXhLRUzKk4L400e3rscbjscw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه تو یه کشور نرمال امیرمحمدو میکرد میفتاد زندان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80620" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e54zhT8fYvorKi3Xv6Pt5dtq7lE9D1CFmGtsCy3BL7gKjkt9Tzkt4ExhLHD2WZ8AXa9rEkK4yOtWNu79ew8Fb0J_0Y0l74nGP7UsGd7XaodsMj466SbPsm5Dal37QB_nv6Ll_HCRE6np3dkePY-LS5BDmj4x7voE935tY0m0C9SkrSiqPOpLPeeD6bLiDmuTdzJd-1Im2P7Y7QD7DoFfMzDWXKrqxJSBAUPTUEhlejIHamWyMUNOOLmvEvJU1_rXlCd1daOgwxRKSaZd6XdGNaftmhNaU2OHbxmbVB9d5IRmzvAm7MzgP21IhGyZWUEFKPKeD7YV9HMXfM2goCSHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
فرانسه
🇫🇷
-
🏴
انگلیس
🏆
رده‌بندی جام جهانی ۲۰۲۶
🏆
🕔
بامداد یکشنبه ساعت ۰۰:۳۰
📍
ورزشگاه میامی (هارد راک)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- فرانسه در مرحله نیمه‌نهایی با یک نمایش ضعیف، با نتیجه دو بر صفر از اسپانیا شکست خورد.
- انگلیس نیز در مرحله نیمه‌نهایی در یک دیدار دراماتیک، بازی را با نتیجه دو بر یک به آرژانتین واگذار کرد.
- برنده این دیدار، مقام سوم جام جهانی را کسب خواهد کرد.
- با توجه به قدرت هجومی هر دو تیم و عملکرد دفاعی ضعیف در نیمه‌نهایی، گلزنی هر دو تیم گزینه مناسبی برای پیش‌بینی است.
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
27
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/80619" target="_blank">📅 11:14 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
