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
<img src="https://cdn5.telesco.pe/file/UtTh4SnhwovT9HG_8sxaAXeUXHG-EsVkleVMYxtXqU-mMr7FNRbD0890UpZ4N4Sr5W_6edr04Kh3xmNnHW_egAf380jLNWETFSMeIzbyfzo8E5dkj756DxwWbMNB_lFcGY7uvwSeu3-TzoT66sovNuegEV7G5TgSnhZHZ6mYSSWzQuetTRh12KusE8PQefEeXUpRbGJtD_ZwTj_4GUnclmBnv-wwqJ_VVXdLLgRgB8xSvj1ULcuBbZXOE0Ca62s_j6I1v0JaIc-o-84QDLeuE8eP4dfIvBn5EDJv0IT0b8aoxuhgkcAaIbNwsimJOT0-q1BNhe4h3UhASRYIBDKoUQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 429K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 17:11:05</div>
<hr>

<div class="tg-post" id="msg-105436">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=V0QoYx8f3CGU4wn9NGOmBBS2mRBf3IzGgRBYYJfH1gNObBt27VlX0avRgc4RuqlHSJfYcKcnoE2d2wpOB9R6J4g5Y78CQRRprmE7CcSYQy0Xag8kbXocBSxC3ye2gCQirqIaMkZH5EVTnVHV5EKMukCFmySmWpVd7DjXCVIm65zqBO5pZhfmtnnG5wEfq5LvaZc4eEOQpfoRYkBvQMpYzlK5xhF2mgQA8N_7n-HrnrJmejW076eqGlrv14LixpRKt73EemwUSyeJgBx2YuV2jx7AfQa8vy-_AdWQRI5p70O6R0wIZJ_HbOE4nihYihv19mrw06TpJthZ92YeIJmGUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f4ef259e8.mp4?token=V0QoYx8f3CGU4wn9NGOmBBS2mRBf3IzGgRBYYJfH1gNObBt27VlX0avRgc4RuqlHSJfYcKcnoE2d2wpOB9R6J4g5Y78CQRRprmE7CcSYQy0Xag8kbXocBSxC3ye2gCQirqIaMkZH5EVTnVHV5EKMukCFmySmWpVd7DjXCVIm65zqBO5pZhfmtnnG5wEfq5LvaZc4eEOQpfoRYkBvQMpYzlK5xhF2mgQA8N_7n-HrnrJmejW076eqGlrv14LixpRKt73EemwUSyeJgBx2YuV2jx7AfQa8vy-_AdWQRI5p70O6R0wIZJ_HbOE4nihYihv19mrw06TpJthZ92YeIJmGUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇹
سازوکار نقل‌وانتقالات در باشگاه کومو، از زبان میروان سوراسو، رئیس باشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.97K · <a href="https://t.me/Futball180TV/105436" target="_blank">📅 16:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105435">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f719399999.mp4?token=JLNi5fNFZkqHZlqbSbUXgKEQRLXUxmUqCQGErC_jiG1GiTGcv6-EKuGiFc6AOlnGb_w7k3t1cQfylBSHvFZig_gljw9IN1U1F7aXJV6uFjvlRlVM-gDKvfyWShlgz1s5epH6ObRHPJhqFf3u55RYYSbkaB4ANMN-79OWP_ubijYLwG1m8LeKi7cha8i70Ji1PZxCPYXtpY81X-SYWCd05aMXvsdetRo0ArcFrFmPowkKq6-s5a_Ck2c-I7zlUJZy7zJfRnfFDpYmXlfKED9U3E16Sb1pnbWh8lxIbXE130nqdjyUMMtZ3zKnDd59WqCUp6867gyTD6ldMj6dl7U3RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f719399999.mp4?token=JLNi5fNFZkqHZlqbSbUXgKEQRLXUxmUqCQGErC_jiG1GiTGcv6-EKuGiFc6AOlnGb_w7k3t1cQfylBSHvFZig_gljw9IN1U1F7aXJV6uFjvlRlVM-gDKvfyWShlgz1s5epH6ObRHPJhqFf3u55RYYSbkaB4ANMN-79OWP_ubijYLwG1m8LeKi7cha8i70Ji1PZxCPYXtpY81X-SYWCd05aMXvsdetRo0ArcFrFmPowkKq6-s5a_Ck2c-I7zlUJZy7zJfRnfFDpYmXlfKED9U3E16Sb1pnbWh8lxIbXE130nqdjyUMMtZ3zKnDd59WqCUp6867gyTD6ldMj6dl7U3RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
امیرحسین صادقی خطاب به فشنگچی: کم‌کاری کردید باختید بعد می‌گویید استقلالی‌ها دوپینگ کرده بودند؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/105435" target="_blank">📅 16:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105434">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=N957HKdD4ZCD2jAAdkrZTABFW2GkOL1tORGtxWM4sY6M4sdrSydFYHYlNDJVMHIEIvMI4thV6QTyS_NDtdvRDQ6Rhv8JuZSLpEjZbukWYIkR0-9s3PIrtPppeLgKoq8_Fe-a01ju9YAU7oZhS9QLtnZ8lDInvNQkqe6MEPu-5Tj4KQ3GI8x4XvjHvTxLGhWsJ4vX3IaSthSWgDrSvdsi7jTs7XZUMM9RIKmxrlXkLaG2ffOqHA-ohVVPLxdPZKj5vPrK6YDcI5VVpd7EdK0u3ubifw10QNG1WdbegeWGNBl3Fjjq7C_Pl48YFkk_CfY-K8iIefx6n52o_YHS3QoDAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/855a5a9849.mp4?token=N957HKdD4ZCD2jAAdkrZTABFW2GkOL1tORGtxWM4sY6M4sdrSydFYHYlNDJVMHIEIvMI4thV6QTyS_NDtdvRDQ6Rhv8JuZSLpEjZbukWYIkR0-9s3PIrtPppeLgKoq8_Fe-a01ju9YAU7oZhS9QLtnZ8lDInvNQkqe6MEPu-5Tj4KQ3GI8x4XvjHvTxLGhWsJ4vX3IaSthSWgDrSvdsi7jTs7XZUMM9RIKmxrlXkLaG2ffOqHA-ohVVPLxdPZKj5vPrK6YDcI5VVpd7EdK0u3ubifw10QNG1WdbegeWGNBl3Fjjq7C_Pl48YFkk_CfY-K8iIefx6n52o_YHS3QoDAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🇮🇷
🇮🇷
روایت وریا غفوری از گلی که آخرین برد استقلال در داربی‌ها را رقم زده: مسخره‌ام کردند، به خودم قول دادم گل بزنم
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/Futball180TV/105434" target="_blank">📅 16:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105433">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=k73NqxL1GPXj5tJtI_6gFraCOXYRHAmXqXheFJittOURIEdrmAxXam1xugHSv7ArcZL4D9Gv2A_Tts6Z8dQSwk1SQKy2rbMmqMpja9DmEC_A5NNVYYwwluhsAbSGFYOJDw4vwWe8WgB_XjnL3VaJPMChjrPqJCPU7a7kAv7qy-C5R2LrORjo8UiFySg4TKOxUGOpw9d5HYvMpOfN29pdeaV-TDMyQFJ9ceEYQU8Oww98FBB1P5X-fH6qAuWL_BAXRzwwCxK0vgBRT9kjAmU769iUmR2OmAZzA18QNkQRQisRnZc46k4g0H44nyAbxw6g4Q-RiNQN35CrB13Arro7EE0gvsu8dOSmBInmhS_TsCR_90Fwm9CZ18UuM3g_opVX2g1eXldDOZgSeRvWlf5VMkuM4Kor65ckW3awBngzwIuekwrnOxOB0nzwaCJcgl_fdagfoLMl6GN8Xi54yMyhBXlmoEdBY0sDvFiDVOMIIBl5A3Ox6i72d54RduPs6DGkJf8Y-XDYe3thvBdGqYbYtvc4eAR86DAdW0qQFjy3QsNlkBKNWc7R_FcTmk3POGrq1uKxgAvJaaLKxbyJkAJUHAE3NmYYhRutOiNnlRcNp8Tsb9c-_kjLNGxES-L02GYP6qjPxZ57GBC-0yt4Y2HxbAM4yLRJSYv50Go757c-9S8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d62c5ae06.mp4?token=k73NqxL1GPXj5tJtI_6gFraCOXYRHAmXqXheFJittOURIEdrmAxXam1xugHSv7ArcZL4D9Gv2A_Tts6Z8dQSwk1SQKy2rbMmqMpja9DmEC_A5NNVYYwwluhsAbSGFYOJDw4vwWe8WgB_XjnL3VaJPMChjrPqJCPU7a7kAv7qy-C5R2LrORjo8UiFySg4TKOxUGOpw9d5HYvMpOfN29pdeaV-TDMyQFJ9ceEYQU8Oww98FBB1P5X-fH6qAuWL_BAXRzwwCxK0vgBRT9kjAmU769iUmR2OmAZzA18QNkQRQisRnZc46k4g0H44nyAbxw6g4Q-RiNQN35CrB13Arro7EE0gvsu8dOSmBInmhS_TsCR_90Fwm9CZ18UuM3g_opVX2g1eXldDOZgSeRvWlf5VMkuM4Kor65ckW3awBngzwIuekwrnOxOB0nzwaCJcgl_fdagfoLMl6GN8Xi54yMyhBXlmoEdBY0sDvFiDVOMIIBl5A3Ox6i72d54RduPs6DGkJf8Y-XDYe3thvBdGqYbYtvc4eAR86DAdW0qQFjy3QsNlkBKNWc7R_FcTmk3POGrq1uKxgAvJaaLKxbyJkAJUHAE3NmYYhRutOiNnlRcNp8Tsb9c-_kjLNGxES-L02GYP6qjPxZ57GBC-0yt4Y2HxbAM4yLRJSYv50Go757c-9S8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🥇
رضا قیطاسی پرچمدار ایران در بازی های جهانی عشایری به مدال طلای مس رستلینگ (چوب کشی) دست یافت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/Futball180TV/105433" target="_blank">📅 15:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105432">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=Kp_LhPZiS8e-kxVhRP4KcpVF2iExUNhPnvGapwLxuFU0hA9wdkfn66IXx18WB_ZDHXaI_USPnZV2_0Xg6UxvzNxg2kBuXQaL1nuiL_Y1QXOK2hG6BCVxfleg5IN9p5C-4TrF23i_maaKRXZ-af-GTogJWB74XxbuSAWOtqRWRgMfUMPQEk-9ioCnhiKF12_frwB4y7az1i9Cy07ug0TiQY5jGwdSz1S9Ywyyi0fBztkEPeJ8-d5UVQiXGAnqJzsl_heL0cMNT2yPxmjNVtFIFcO9y2ASjn1a2mve1j5bi6UkDTNu_AY0_gk813NRNXErNQROLpZr4x1ga7ZDm5Rh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44a16cd1aa.mp4?token=Kp_LhPZiS8e-kxVhRP4KcpVF2iExUNhPnvGapwLxuFU0hA9wdkfn66IXx18WB_ZDHXaI_USPnZV2_0Xg6UxvzNxg2kBuXQaL1nuiL_Y1QXOK2hG6BCVxfleg5IN9p5C-4TrF23i_maaKRXZ-af-GTogJWB74XxbuSAWOtqRWRgMfUMPQEk-9ioCnhiKF12_frwB4y7az1i9Cy07ug0TiQY5jGwdSz1S9Ywyyi0fBztkEPeJ8-d5UVQiXGAnqJzsl_heL0cMNT2yPxmjNVtFIFcO9y2ASjn1a2mve1j5bi6UkDTNu_AY0_gk813NRNXErNQROLpZr4x1ga7ZDm5Rh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
اسپویلِ بازی بارسا-اتلتیکو در این فصل.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/Futball180TV/105432" target="_blank">📅 14:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105430">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqxghsRhAqzg11zetyzXO5x65CBLpZmftxHCV8qmXlwtP9KgUQfc4gEd8zW3mkQLKGEEUz7gov19-t6CfkO2WiCfBYHS7PMX6dN8X-cdNXLxTpiGSJK0J1efkrf51txwZVi_CPi0P_dfkrL6IcyM6PGpDJINscdhwblLRvFBMSrZuYVvk5WafU8o5RjQZP4s--yi57Qt163VVF_wdfdgFiXg95dNEWrBjkDHytpVb--7IF1W7SugkoDb-AoBv36n-EiK3-HXaW0z_XvGcAOMgZVFEg5m1dZGLmAJOTBPGfqlUVej4Vb2sHsHzLmngyvFKKXf_d4oG9VomtkN6kmmlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLK2TPrvgLJtw88qFvN1CW_0g1YJyIx61U9YBQkmL_5DeilHeGImMnDJNyAlPPyhWpHIX8ioOkkX3RpNR9oH-gnNM6bNrD_4ppNYLizq2nXw-MAQBx3QPNzN_DMvD3bl86ZFcVEO7iWhDeXXzH-qVMgc4QzsOGFgTYr9imFzYkCt-fMzRCx55pYLe79hLmz7oZSPL6Jiai6ZDgxtQGBo0vmwQYJdByxWRgqf7kwHMnH5rcIh2rkJWUPUnocyYjLYFmQPAO_1LYrj9AavkGkNXy_0cq1IQo8wNIN1SoZ9qiZ-kfbP9lE7_eQDUsn_jF62NIUtUMgAPuPFc1jQoYIWEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">💥
عیش‌ونوش لامین‌یامال و‌ زیدش در پاریس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/Futball180TV/105430" target="_blank">📅 14:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105429">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8bq9U4-5bb8P2xwJzS8xNL4KIOlo01T_0jrXqyLvM72cBu7veAK__Punp4O1KmB8D_EDc-IA5-IZqpSop7RXeY7j2iTR0jDAA0C727fKhVI20VMgsciQZpZQr-xndhWqbtBVnEQu3DCvqJeuOe6MXh1QkYgninU1TixaVSOHpjnGSu81_tE7-0t5VfvMRPZ3tIQZ2gOfDmDBElMfnDCVrpA2keFxDAvwmehu3im428B1PWqLbm1uqyCpcFyQ9Hf0jEpK7tqLeOqmF7EJzMGguRa2LZs6eGXq-D0IeOEcehbpotJfLLD0i4DZ-1N9mzgDtZGs4Hh-OMD6bnUwIoznw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/105429" target="_blank">📅 13:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105427">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaD8mcN9gspIRACdpReZeoLF3K3y6lyz3uSwoypkepdWE0YW6-9X2LdO2DPjKjmTxfG8Goq5kSjAo3krwawE0jW0jaISACxyyeu9X_fkU60Jq_u7nzYSjWC1Ml8rWKF1cksS8e_BQvnB-Mkd2pvkShBEIQzZlV9OEgnMCDeGAfBnXwrDTeduchgSbzPAxHGVaxdSBuO2x5nWfAPWZW3SdQeJxU33si7i6uRuaiRsm12-RT4FwQedNwOueeka9pBXNvU_iF3ZUTrokGUXLjzWJCuSFQvv6cBQb8jeO-w174EaRNoQ83CG1mOJBuyc-J1UBH6P-s2ONithmgGC3bTsPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/105427" target="_blank">📅 13:39 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105426">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEarT5ndKuF-Ja0RQkzDbiaILNmM6oKort0Dg8aX53yG6hbBITgVwlrYzCXu02ZGu0CKu6a9Dh4XBPyxgVfui3k5woS5paGIv2mK-8o00GfLnQm-7SQEHnxZ38QphpWALShAxS1icFF94UQak4TTwE_sXckWNtDxBbegfQEabinvsW-f4-hxZu3PrfYLgB7FL8Vzno4X355Y2MwnYViD82lm3qhqDsy9t2AvQdtPQb0XB8hgrPJq42c3iSOWDTdckEAFc7BloxCIZVu7E05mHD2HrpWQL5hFdXYnlNPVnCdkr5WicHs-znwhXGWsmJxhQLqL8yL_QrLaFWRa9TaGpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!  باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/105426" target="_blank">📅 13:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105425">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=sGqJePBiuuXQdy5WStRy8Gt447FPFhvdvLe_-5OcqY_Xx_ikiSBKo-PaeqIcdNNBTshN1la-6FUvgRLGhMfa3wJwMsHZ2S4XgYbXXLaqqQu5cfZODTI0unNHAq6EiJVr1Ztt1qaQSnlZsDukDOFC7T-Htb4B7Ew6-66LesFtIeRdYL2UWrzECkzYbrM1XHKzFxA4JHLG5IIg3Qc4v-DpIl6YPJAtaAO4f5SpPRVAjTl8zVAnKFkgumxKxPYIrgPwY6_HST8tn3cmcNieYgx-ZguTbLSc8SH0kWSBLGKOUEqCgLFK9ezmoFWIAuGe6xQwebazDvu8Jmxt821bksoMLScPwPKMZr13AFDo39VWpvzMxNfJ8nGYkujSx3ZsRAjoi4DJ0rBRx58L1TX5zH-w6j5MYMNfhEXQc4wIcgVXFXSvq_lokZLB6ygcMblvQdSQWb4MW63-ygWhbci209exWAsnedEP-zX7CjzDlF8zDGXwLciEgf12BiiCdG8oOFqWQIzn_qt2ocIHIS3zWCV2yYjhfyfRF9b1PZUP5A9b7LgNUw66MPWqCpItYbkznP_PkmZ1eJg6UrSZ4EvbLsK42IE9vQ0fIzpMudilSX5NhfD9xu1vSxElqCNtTnf6G3wsyBSHopmTAWAQAedOsREKCOgASwqYQEcRFEzbxFF1C6M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05e1941b9.mp4?token=sGqJePBiuuXQdy5WStRy8Gt447FPFhvdvLe_-5OcqY_Xx_ikiSBKo-PaeqIcdNNBTshN1la-6FUvgRLGhMfa3wJwMsHZ2S4XgYbXXLaqqQu5cfZODTI0unNHAq6EiJVr1Ztt1qaQSnlZsDukDOFC7T-Htb4B7Ew6-66LesFtIeRdYL2UWrzECkzYbrM1XHKzFxA4JHLG5IIg3Qc4v-DpIl6YPJAtaAO4f5SpPRVAjTl8zVAnKFkgumxKxPYIrgPwY6_HST8tn3cmcNieYgx-ZguTbLSc8SH0kWSBLGKOUEqCgLFK9ezmoFWIAuGe6xQwebazDvu8Jmxt821bksoMLScPwPKMZr13AFDo39VWpvzMxNfJ8nGYkujSx3ZsRAjoi4DJ0rBRx58L1TX5zH-w6j5MYMNfhEXQc4wIcgVXFXSvq_lokZLB6ygcMblvQdSQWb4MW63-ygWhbci209exWAsnedEP-zX7CjzDlF8zDGXwLciEgf12BiiCdG8oOFqWQIzn_qt2ocIHIS3zWCV2yYjhfyfRF9b1PZUP5A9b7LgNUw66MPWqCpItYbkznP_PkmZ1eJg6UrSZ4EvbLsK42IE9vQ0fIzpMudilSX5NhfD9xu1vSxElqCNtTnf6G3wsyBSHopmTAWAQAedOsREKCOgASwqYQEcRFEzbxFF1C6M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🔥
🇮🇷
🇮🇷
تمامی موقعیت‌های خطرناک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/105425" target="_blank">📅 13:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105424">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/INL4aivT5mFBm50sMlgWVPvnq-8mt4R9FzsW_K4ob0MKTW1hoGRhe__oWfu6QQyUGmrFGsel8Z9JvnxPJl7i-gcDUOonmTliWzm_P_TjyrvbBbRMftwD8jqwlyO3Ym0uMLXNzhLv44kt49WvSwpTGauJax6RgeYpAOj1B_V9qf5JuHvsEyLQUg8symVYfgNfgb0VjuZsKxBU0bGDzCmNQYHv-shQQYCkkKvzPvCfmenzpXlzszzcxj_KUCZ9x1iU803k6H7G9rss61n_ig0ZjXE4iX8ZUXR9WvWCu3HGI4MadIN40BeXHdLTd7lrji6S6OBPJQ0N77SwRl1wRsZHfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105424" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105423">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105423" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/105423" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105422">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1FU7ftkKT6-ScHAPXsng1skI6q4bkrvMGc2LRSPt6tJQnLyzkT_5pTExaLV1SFFAXTqbzE0tb4Q8XOBqwj4ODr3n-Q9yNrLOHf5SZ_wA6WpYBBiohBuPW3kHq87tUCiUG0EI85TC5p-HfrHBzio_s1E5HCqKEIA_YJ-kGU_qA6KIOdv9I70eJojD776kANU5vYnBIJ_oxR7xtoO-tRhF8f2zAtRqFsGhiBYfzgeLhGjiESrP6ClmigdbYBREE3EfIiB18sglt8M6mkQhcyivXo1jrQYkjprR35KN7vlEmXF_EU527YMfieRoIsbwUL2OKi-MnHlxHPXLoF_gHquPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105422" target="_blank">📅 12:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105421">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=EYw1o8kTX1zsYZ7FkEXosxOjjkaS9FCKt5LjAWTghklM5kaXDYJ9j98qka4EoCWtu6w8gfYMYnpmv9kWhEpRfWTDujfvC0Mkd-ibGqWeK3xZBgc4XqVVPp00cpcr2wwbQgZRelmbf0nBwvonYLLn7vXmgxJ5ExD5-fwUUFM34J3UA8GeY05hjZ45qGdZexoVTCX-v2nZbTCZwL3jhYB0JSOLT1NKJJk6aTnW9Inlcyy8Y_sfEgitm8zXuA84Lm2WgFJBj4IJ2cuYklCezR8xYYknPj1V6axzByKkvJ91wph0LU1JXQUVgyl0-IN1Iw1jHtt_-oB1LL7NDha1xLpSK1M-MS-gDuD7vBsR6UtYKWDyiscvz6CcLrzRJJ1BCdSQPr--Wqfjjz_BvrnE5urNmqcqQIpXVarUVdRCc8_ia_t07eT2s4brZa4dRzHOM5Kd-8DBIzPgsjslWG6gevFgJ0UU6jiS10rnsQZthHszBtzB2vYT3cUj1GwVaLYpwwQTsMRQeWBDxYl6DY5gd8isx22tDikZsX8KWxYHLdSizYlU5ELQRa6Be5YBK_i22gXqLSEcrGvzR-2SgQRxeHpwdnvsjYUw0VzRMsK4fvER0zZaWaXDpQ3teLTs_vjYtPgQW_uq4a0nC5jzTa_MQ94uxsXJ2SzWZmyCL3U8huzPEbU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/857b23b6b5.mp4?token=EYw1o8kTX1zsYZ7FkEXosxOjjkaS9FCKt5LjAWTghklM5kaXDYJ9j98qka4EoCWtu6w8gfYMYnpmv9kWhEpRfWTDujfvC0Mkd-ibGqWeK3xZBgc4XqVVPp00cpcr2wwbQgZRelmbf0nBwvonYLLn7vXmgxJ5ExD5-fwUUFM34J3UA8GeY05hjZ45qGdZexoVTCX-v2nZbTCZwL3jhYB0JSOLT1NKJJk6aTnW9Inlcyy8Y_sfEgitm8zXuA84Lm2WgFJBj4IJ2cuYklCezR8xYYknPj1V6axzByKkvJ91wph0LU1JXQUVgyl0-IN1Iw1jHtt_-oB1LL7NDha1xLpSK1M-MS-gDuD7vBsR6UtYKWDyiscvz6CcLrzRJJ1BCdSQPr--Wqfjjz_BvrnE5urNmqcqQIpXVarUVdRCc8_ia_t07eT2s4brZa4dRzHOM5Kd-8DBIzPgsjslWG6gevFgJ0UU6jiS10rnsQZthHszBtzB2vYT3cUj1GwVaLYpwwQTsMRQeWBDxYl6DY5gd8isx22tDikZsX8KWxYHLdSizYlU5ELQRa6Be5YBK_i22gXqLSEcrGvzR-2SgQRxeHpwdnvsjYUw0VzRMsK4fvER0zZaWaXDpQ3teLTs_vjYtPgQW_uq4a0nC5jzTa_MQ94uxsXJ2SzWZmyCL3U8huzPEbU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
افشاگری همسر رشید‌مظاهری از شرایط این گلر شریف سابق استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/105421" target="_blank">📅 12:45 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105420">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNCMpXV3zAhBxqzDzKnqRqTexzDlMpITSHtSyFI9z7r-tMbaEDtcFShpXTM65tac4aa1_O55H8p9vHndsUACo2BscepiVE3j3DUDTkU1AXyzXPOZ0SLzFEKoG89PkU0DYChaXymU7WLKL3eMKvMo4eQGydbzrDBtbivxKuHF2ubt0-O_eCxJb1M48RHnkiLHM_yMC3gQO-CmZ5cDmHsi32nhaG9ki0ev84H2X2hq8cEqyZJWHuC-i2jHczFfhVoo5Ok4gGisMHXDrpZM9NDdM67qI87qfw_f_Rfj-CDpShNDp-7ESvJHi9jTGtznd2omH27OM5ilOuHjg_GZ7FrzSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
✅
🇮🇷
پست اینستاگرامی مهدی تارتار سرمربی تیم فوتبال پرسپولیس پس از داربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/105420" target="_blank">📅 12:18 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105419">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzmCNTeC1jkvuv_3cwS3pgFxOWoV0G5I6HNrJhIDwFGe7xdmfSqy66j0Zo0FgMJeZR3IMDSN3Tm75AlIyeynusWUzrWDRULR5JjQ9pXAjqmy4oZ9ZwZJdzjT4R2-qPSs-LceDZRDeJH5giJcHoCSgNJuJfUlDHk8o1PPDVwl2zvF1mij2UJ5B5KHwsDkaQK66pilDvX64yEamdDZ9KSVFqkwBZ-bzYRKDrQWPDQtTJs5OZ3vPVkVCzGu6nZH5gzHmZuAHYWeI-SBDthCByG-FSnBmMmLLxhR8u76k27Z2DCOVY2T2J-lvPEVPAD9PY5iR7kobKcMjQoStuEGIso7Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
اعتراض تند مدیررسانه‌ای باشگاه استقلال به عدم اخراج حسین‌کنعانی‌زادگان در دو صحنه
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105419" target="_blank">📅 12:13 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105418">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/105418" target="_blank">📅 12:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105417">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFGzwP_v2WPwz7E-7PqPrtHCEBx5t6DlkiY2WXjMzpLm-Z64hBCP5UHQNryf76oUwkaisuiCuc-DeBI7uQf-oiR5RCcYouQZLFeEVE_5bnoXH7-rAmEUJtO-2DOnuUKkePxjVyPXYno7CC5ylQ4P9nc3vIsSaWcF5oA_oNEj9Pt2D55yDaLN0X8uWoW4MhHtX1gVQKlwfVplEmbmiBh-oLLbsmAEKMhOgPgayAYQdaPRGw_rZv7ei-HLcpFl7qEGRzvxhLvBgMfcdONITx_ZjnNOm5SdxbsAODpdw4ugWotjbdfSaGloEWHztcqrf8cjoapDP7alSQDsjzy-nkt51w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🇮🇷
محمود خردبین اسطوره پرسپولیس و دخترانش درحال تماشای بازی دیروز دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105417" target="_blank">📅 11:55 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105416">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=ciZcF_k9rcca4HywzAyfkQZqcQk3GCoy6-3qOi3ojNkkSh7fwoFPyqyYMjnfV9pPYS0w4sO8j9Oenvs5tdVpj04MOANH0MrFC2wHBYfTERoVL-Nm9AM3AwfsoiRh-TqbmwQHKr9MtwSWIv4YeBRgQWteUjUwO1yjPbTBEXgzGwtchS6qHOoyZvdg7g8DzNpLagKBxAmW7L9oqF-oCQpewPh9BsRc-Yjc8DiJSlXzZ655McEbAID7oTW_6pK3Xn1fLpJukqKfgvKQ3eCvlJSa0MpBD_EV6PP7aoYceXLi_oIOUude_hnHLhs1ENwC4LjRc8G2F11iJBXqDLFPB8KzrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f4fbd0e6c.mp4?token=ciZcF_k9rcca4HywzAyfkQZqcQk3GCoy6-3qOi3ojNkkSh7fwoFPyqyYMjnfV9pPYS0w4sO8j9Oenvs5tdVpj04MOANH0MrFC2wHBYfTERoVL-Nm9AM3AwfsoiRh-TqbmwQHKr9MtwSWIv4YeBRgQWteUjUwO1yjPbTBEXgzGwtchS6qHOoyZvdg7g8DzNpLagKBxAmW7L9oqF-oCQpewPh9BsRc-Yjc8DiJSlXzZ655McEbAID7oTW_6pK3Xn1fLpJukqKfgvKQ3eCvlJSa0MpBD_EV6PP7aoYceXLi_oIOUude_hnHLhs1ENwC4LjRc8G2F11iJBXqDLFPB8KzrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
داوود رفعتی: بنظرم داور دربی کوپال‌ناظمی بود اما چون تلویزیون رسمی پرسپولیس یک شب قبل از اعلام این داور رو معرفی کرد،‌ فدراسیون تصمیم به تغییر گرفت
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105416" target="_blank">📅 11:33 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105415">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=P-OsLfsA_cl_xcdOq5_fMCqJfF1O7QudTtrV5HbK_c9fbD7cXIokC6tErSs-J6LWzqkB9RJwTaojdM1NHiLwe137hn3KWBvRsO2a5w5VpTRF3dnD0KG_iipXGl4nE13RPIeRzcytPy-Zpq_TMIEX28BEkpzO7r0_49Hp-4Ma31qderX6CbynAun7dK7eHfpLzZCl9SZWbgwQ63A92R9fVCe8xNj67LCgVMV7SPNa8appQRg3o2X3fdFYfst4GN71TMzvTHF_cqmDoYbz2DJUp0h90cROmO_914K-ZmRGyKZsDnqaNOuCX4BEte6tcatr9Lra4gavJqEp-WT_2-xzdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e40e7ca6dd.mp4?token=P-OsLfsA_cl_xcdOq5_fMCqJfF1O7QudTtrV5HbK_c9fbD7cXIokC6tErSs-J6LWzqkB9RJwTaojdM1NHiLwe137hn3KWBvRsO2a5w5VpTRF3dnD0KG_iipXGl4nE13RPIeRzcytPy-Zpq_TMIEX28BEkpzO7r0_49Hp-4Ma31qderX6CbynAun7dK7eHfpLzZCl9SZWbgwQ63A92R9fVCe8xNj67LCgVMV7SPNa8appQRg3o2X3fdFYfst4GN71TMzvTHF_cqmDoYbz2DJUp0h90cROmO_914K-ZmRGyKZsDnqaNOuCX4BEte6tcatr9Lra4gavJqEp-WT_2-xzdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
هواداران اسنابروک حریف دیشب بایرن یه طرح قبل بازی زدن شبیه ترن‌هوایی که خیلی پشم ریزون و جالب بود. تیمشون هم در نهایت از جام‌حذفی کنار رفت
😂
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/105415" target="_blank">📅 11:05 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105414">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=SnFGQkF1dMNNGp9DXid-A90yzB0uYbewQndekdGoVOulT_CGNorhmVaseT6cITT8EoAEwGm4zHzDH1AFbq1FObeET8H0niz1Jj3-u58QEFAbMZpVcSd1A9MFA0PFW4Cu4_2q6QAej1LqJ9DmkH8uj0vztde30vPJNRTpe_TXdnPsi-1Fut42UuUKYkmc6lXzokkeP2VXUjHQCEeEPMq324Tnmh-okgIoqiTmoOtz_1v_TXjgXFhaUU_jiQVnhCKjmfBsutYrtr9d8cIvBHdEmWrLbrurUL6Ano63Rn6PyW8X2lPggAdSYKe6LiP5c_24R9Jv1hbISwqw9DIJ6BzTDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da46dad11a.mp4?token=SnFGQkF1dMNNGp9DXid-A90yzB0uYbewQndekdGoVOulT_CGNorhmVaseT6cITT8EoAEwGm4zHzDH1AFbq1FObeET8H0niz1Jj3-u58QEFAbMZpVcSd1A9MFA0PFW4Cu4_2q6QAej1LqJ9DmkH8uj0vztde30vPJNRTpe_TXdnPsi-1Fut42UuUKYkmc6lXzokkeP2VXUjHQCEeEPMq324Tnmh-okgIoqiTmoOtz_1v_TXjgXFhaUU_jiQVnhCKjmfBsutYrtr9d8cIvBHdEmWrLbrurUL6Ano63Rn6PyW8X2lPggAdSYKe6LiP5c_24R9Jv1hbISwqw9DIJ6BzTDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
ناراحتی شدید ایگور سرگیف از تارتار بابت  تعویض شدنش در بازی مقابل استقلال!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/105414" target="_blank">📅 10:40 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105413">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3-CvhzaWm9W9iERhpkEOooZf67tXjt3CVPPQhYJi7TH6qU3J-37i7vHxEoOUSExAcGZqft7haWRdnYR2wnPJoSU9vsrttDhbpSZZMJT2B9jsbR1mob3JZX2AbYAmlAQAAb3feNda3Cj33n9IVaQqBelK5viCC7C9e63_kBYbxKw4ES3Vow_ou3aT4L0S27uTJMJOdJx8q_TwBloEGGxKH7uVldZOIzQ36nbWCorubp2laft_xZyrGZNwrh5kX2MfBgTiCzpNlzxGkmwh-D2EC33tRU6ZFAwDmFTmukDtZZ0pMw3J9lI0lazPPk12HCYgCRyy4Q_2IUUjmDZr0FvxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇭
✅
قرارداد کارلوس کی‌روش با تیم‌ملی غنا پس از درخشش در جام‌جهانی تمدید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105413" target="_blank">📅 10:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105412">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8I9L_VhZp6ho5ldkzoK-3lQBp7S71oVzoy9eLqReFh3fJjHmWKelPqXvGRUVaIUZejs939xsxKWe9SHuZ1BfRkbXtIG8Xom3Dnf85N2_0YifNz_ntsG6dDOnJr-j0bT7sOHOkyjsDAyP5vFtYScpVYIoP6g-KcGzUQPqPlaIB2NpOyfNK81WCnewEKGpa_S2I_tysvT6WIw2Zm0dXadM-MUcuCsEnFg9tLDHk5A-xxLidn1DbWsSeOPF5HeeF4m_bfjcP3mbcEricU5xn9vqyTJy3nPebdT2y93Rj61vU13HY3H3Qd616cgC348PtgWvJQntj1eMD6KJJgZB7r50A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📱
استوری کنعانی‌زادگان کاپیتان پرسپولیس از صحنه مشکوک دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/105412" target="_blank">📅 10:09 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105411">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4193fef239.mp4?token=QFZgsajtTyb6RdNP0Cqn04ASLNIQbqJ4OZ1xy2nOkpYs6iQGvi0_ss7-YiD1Zar5yLt8WSzY5ZtftZBk7S0Ml0IdC9O9C2HOPWW91QLrpyYzn_CKbJXcjITZfKPTeI-D6K3EKlvhi-RNFyA7Prdw4jiSQ2he53WesP7Mdd_kYWhzA_f6L1v26OEiol_LL2PnnMiUEb1bRDFQcafn8unXC9tOOT9N_KHnVU8HJ7Y9TVS8iCJKcwPRSWwk0nRZB4fzIxrYYeXmKl7D3YCmy7gaUzS93XhTZk9hNM_Btq57KGlnxbJdTCqcIUtj5G2haqzfA4tYDrlVn0IwOPaQ5RPJhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4193fef239.mp4?token=QFZgsajtTyb6RdNP0Cqn04ASLNIQbqJ4OZ1xy2nOkpYs6iQGvi0_ss7-YiD1Zar5yLt8WSzY5ZtftZBk7S0Ml0IdC9O9C2HOPWW91QLrpyYzn_CKbJXcjITZfKPTeI-D6K3EKlvhi-RNFyA7Prdw4jiSQ2he53WesP7Mdd_kYWhzA_f6L1v26OEiol_LL2PnnMiUEb1bRDFQcafn8unXC9tOOT9N_KHnVU8HJ7Y9TVS8iCJKcwPRSWwk0nRZB4fzIxrYYeXmKl7D3YCmy7gaUzS93XhTZk9hNM_Btq57KGlnxbJdTCqcIUtj5G2haqzfA4tYDrlVn0IwOPaQ5RPJhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
🇮🇷
لحظه‌جنجالی و کمتر توجه شده از ناراحتی صالح‌حردانی از کادرفنی استقلال بابت نزدن ضربات کاشته‌های حساس در بازی دیشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/105411" target="_blank">📅 09:50 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=v4WOsS920meNvRVDlxk8lmy8-3aWRvujloFRWjj7ukJYma4eezRsNyVJaivlCuSGBMPIjQkRnYni1ZNcSm4M-Z3EvYFfiWXjm_PxUXjLZoZzDBfKgroxXiDZ3yPlgdasGR602-s9cvJwYPDNixndxLTujFJPfgEHYfJVp9FsfC6Vf-Dtu0UeP91PJO612aG4rgf_vbfIFUrIPHT-RgoX9kW8lTtxggKEbcT5tVVpkQSU_fyn_n49VS7l2FHMze5YxQka6_UNlm3rFrzLqHQS32xPGdv-3g_RJCeL844kUh4mbFE83u5CgFp750fjEmKCYAr0lMPrJdUbccA2pBz_9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e92a23e71a.mp4?token=v4WOsS920meNvRVDlxk8lmy8-3aWRvujloFRWjj7ukJYma4eezRsNyVJaivlCuSGBMPIjQkRnYni1ZNcSm4M-Z3EvYFfiWXjm_PxUXjLZoZzDBfKgroxXiDZ3yPlgdasGR602-s9cvJwYPDNixndxLTujFJPfgEHYfJVp9FsfC6Vf-Dtu0UeP91PJO612aG4rgf_vbfIFUrIPHT-RgoX9kW8lTtxggKEbcT5tVVpkQSU_fyn_n49VS7l2FHMze5YxQka6_UNlm3rFrzLqHQS32xPGdv-3g_RJCeL844kUh4mbFE83u5CgFp750fjEmKCYAr0lMPrJdUbccA2pBz_9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🎙
🇮🇷
🇮🇷
توصیف‌‌جالب عادل فردوسی‌پور از دربی جذاب و تماشایی پس از سال‌ها!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/105410" target="_blank">📅 09:25 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105409">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=X2zyjsa8t_dcnk2n_Cv9bpO7R0AEU90uTS5y9NU-YM3iqi3dqfiWLbgR1JaIojIWly2pP0YUZSxthI4FmAsKQnCU7NrLnKHJTGfxY1HEJKYSi6ExLFxOu2UCRM-Aev3F5POHOak08ojJ1bXaVd33dl58wQsDNNL40aBL7BDXEb7m_MtcnIhOe1KCOAdkBCeKooGWaaNy6vumL5MAvwlchJPDBFltWKySrmIzRVD7xAbSFLx5Z28ASyf8HTbNsruv4Cp1dipB-zR6aZA4zahjP8-UO3DHWjHiw4Z-bK4si8qpC_b4WkNYGhSVbNy6Ym0fBKaECmqsiBrAEahkbPAdHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cff9c433cb.mp4?token=X2zyjsa8t_dcnk2n_Cv9bpO7R0AEU90uTS5y9NU-YM3iqi3dqfiWLbgR1JaIojIWly2pP0YUZSxthI4FmAsKQnCU7NrLnKHJTGfxY1HEJKYSi6ExLFxOu2UCRM-Aev3F5POHOak08ojJ1bXaVd33dl58wQsDNNL40aBL7BDXEb7m_MtcnIhOe1KCOAdkBCeKooGWaaNy6vumL5MAvwlchJPDBFltWKySrmIzRVD7xAbSFLx5Z28ASyf8HTbNsruv4Cp1dipB-zR6aZA4zahjP8-UO3DHWjHiw4Z-bK4si8qpC_b4WkNYGhSVbNy6Ym0fBKaECmqsiBrAEahkbPAdHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📹
🇮🇷
🇮🇷
نظر مارک کلاتنبرگ درباره صحنه جنجالی بازی دیشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105409" target="_blank">📅 09:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105408">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/603e84d100.mp4?token=kHxUYHyE343tS9Gbgzu4H8c9o_LxtIM8l2io8JQeTTyIazZ5lh2rexS9jd2NYgp_DksczAebGJuvzzO6FUTYbxCARLhkH04ViN42VfTWc-BFGmwb0KatOcoHrgfmtBimxpEXUw9kFW-awH9a-QgPgcstSV6wPAOCbXqnnJNpmz_p_eELTWPrgR98puLYHEx6dApJPRQcXxAocQ47idqrIip7VRqMJBrZcuQjmQj6toLgwgNzunqZerljz0d1q33UY-AQpfhh0YhliGQd_VNUXQQovGKDuj3Dt3ffo5LgjO0pXwbdfxw3FgLzXQtcUvRaYEdvXTPHMarFTM8KyunZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/603e84d100.mp4?token=kHxUYHyE343tS9Gbgzu4H8c9o_LxtIM8l2io8JQeTTyIazZ5lh2rexS9jd2NYgp_DksczAebGJuvzzO6FUTYbxCARLhkH04ViN42VfTWc-BFGmwb0KatOcoHrgfmtBimxpEXUw9kFW-awH9a-QgPgcstSV6wPAOCbXqnnJNpmz_p_eELTWPrgR98puLYHEx6dApJPRQcXxAocQ47idqrIip7VRqMJBrZcuQjmQj6toLgwgNzunqZerljz0d1q33UY-AQpfhh0YhliGQd_VNUXQQovGKDuj3Dt3ffo5LgjO0pXwbdfxw3FgLzXQtcUvRaYEdvXTPHMarFTM8KyunZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
👍
وریا غفوری: یاسر‌آسانی جدا از فوتبال خوبش یک انسان شریف هست و در ایام حضورش در ایران برای یک فرد کم‌بضاعت خونه خریده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105408" target="_blank">📅 08:04 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105407">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105407" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/105407" target="_blank">📅 01:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105406">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1ot0_O1ssLZWH_GfdwStpnZn3ATWPuGB-zFo9XwEjQVKR7JwTMh5k46TUR31dS9zAXbvAc9vA4w2BpNekxOuKS8PyiYB4fsS8pZiE3oFHRooQhksXV-G-LmgIRKe0o566HfHuQsl8hx4hIAY-s4_TNSZz5VsXo9YQUq_8rE7edVE5t1Jqn8L7gwQ6LfNwjFXwaiHKt0bB6L9X4JzVjDIYnAMG9lztjgKSwkomOY5sHdvtIun8k10dTTiP7BYYSUSbbVbHeF2rS8NjoEg3obBEveJBLmcRYrGn5stmxqUAhjVoNgbkcKWWUxrz_4mCIFvVX3e6uSxyGdoWV4-xp5Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105406" target="_blank">📅 01:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105405">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
⭕️
فوووووری/ همین الان با شروع مجدد جنگ دلار و ارز منفجر شد
😳
‼️
همین حالا چک کنید
👇
https://t.me/+S5Mn2k3LOf0wNjJk
https://t.me/+S5Mn2k3LOf0wNjJk
فوری برید ببینید
☝️
☝️
☝️</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/105405" target="_blank">📅 00:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105404">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=FNVU25tF_hB6QFqTXfz2USl519P-B1lYN8ZBINZ9_7bf7eSvvEHkCxS2Zp4L5abDrUjqV5uu_QwWwxsBmnXZb54sF09xBWyGrmN6vMSueMEEkSU_orCi3h7dFVcW43fAVRVuzQrQ8yZcipHBi17EokSIl0EnSJU7DHz-hhAnpRkBvgfuiCbK5e4PP9S3ng-GAogElIojTnp-vTIDYM90UFR290tGG-akRV5AhKIExvi8SDCsVdt1Az148nLRpxAb_1YFJb9FCUJFvnxsz8RuKdK37kPdXqMAMrAWBibA3Tjcgb4tgCzbmU9gRtvwog9mkK2Tejnk4_9n367_jwu_1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d578329cd4.mp4?token=FNVU25tF_hB6QFqTXfz2USl519P-B1lYN8ZBINZ9_7bf7eSvvEHkCxS2Zp4L5abDrUjqV5uu_QwWwxsBmnXZb54sF09xBWyGrmN6vMSueMEEkSU_orCi3h7dFVcW43fAVRVuzQrQ8yZcipHBi17EokSIl0EnSJU7DHz-hhAnpRkBvgfuiCbK5e4PP9S3ng-GAogElIojTnp-vTIDYM90UFR290tGG-akRV5AhKIExvi8SDCsVdt1Az148nLRpxAb_1YFJb9FCUJFvnxsz8RuKdK37kPdXqMAMrAWBibA3Tjcgb4tgCzbmU9gRtvwog9mkK2Tejnk4_9n367_jwu_1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
‼️
ویدیو لحظه حمله حسین کنعانی و چنگ زدن به عارف‌آقاسی مدافع استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/105404" target="_blank">📅 00:08 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105403">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qEvWfxm--jfuwSUvkYQkRpdV7MWp1fnyMMoayj3wSqLkI0xfSzpFhEmS4UA74I915c19hzskT-2JFzn7qD9F8zqv-rKjHcZuZTC4XjfMyQ4L06fpGsFwa5-GAdPXPSkN1u3wLgUONP1rLEwP9TkCN-B8MYjIvGtxyDDO2tyQbHwXKlf5DexotAczNZpe8fNNdq-jxswZPycCS64eAZ82fNuhuJJ1YduD2UyDZJpgYw1oDO9bGeC2yyhsXaLPRZVshrXVMR_OO3PXPDJJezZR0i9WLbuSdUXt0wj2DCVHRDeKsz7o0o6d_5Nhj4GlPMAYtNhjCR3rpTyj8wxbtDxbTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👍
فدراسیون فوتبال آرژانتین برنامه‌ریزی کرده که همه بازی‌های هفته آینده مسابقات مردان و زنان توی دقیقه ۱۰ برای یک دقیقه متوقف بشه تا تماشاچی‌ها و بازیکنا لیونل مسی رو تشویق کنن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/105403" target="_blank">📅 00:06 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105402">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e447de2235.mp4?token=fPg89FGkTwWv7oJDAO3cxs5J434Xh_pEkEjRtP4yFJ4hcqxp4tZQKAgVEs8Ie5vXVbePMM7BZca-RQfpe7Xz6aOlX981DLlw0B1KI3fRtqNmly6kGh1fw5ccmOaaiC354zNqB_9Z2IqyCJnHERADpR-znXpD_3VM3xTlmtVv3YbwT6x-HtIWH5Do2tJRgp-NaTdQCIB_vB_BwK5fm1vi5Zm8mWLu7Q1tNIBv32waVPFW1iZc_IqnjWSeh6Ap_XaMwu6sPWSZ2DqLFS_U59lIopogQ9-UEPzAuoFdGYbtvdU2GP9SeXVAe4A2dl7lN3Rm4tS78MLW17bDdZlAyi4ogA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e447de2235.mp4?token=fPg89FGkTwWv7oJDAO3cxs5J434Xh_pEkEjRtP4yFJ4hcqxp4tZQKAgVEs8Ie5vXVbePMM7BZca-RQfpe7Xz6aOlX981DLlw0B1KI3fRtqNmly6kGh1fw5ccmOaaiC354zNqB_9Z2IqyCJnHERADpR-znXpD_3VM3xTlmtVv3YbwT6x-HtIWH5Do2tJRgp-NaTdQCIB_vB_BwK5fm1vi5Zm8mWLu7Q1tNIBv32waVPFW1iZc_IqnjWSeh6Ap_XaMwu6sPWSZ2DqLFS_U59lIopogQ9-UEPzAuoFdGYbtvdU2GP9SeXVAe4A2dl7lN3Rm4tS78MLW17bDdZlAyi4ogA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
‼️
⚠️
🇮🇷
تارتار: ارونوف؟ هیچکس از پرسپولیس بزرگتر نیست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/105402" target="_blank">📅 23:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105401">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
‼️
🇮🇷
❤️
کنعانی زادگان: از اول بازی استقلالی‌ها موز و سنگ به سمت ما پرتاب کردند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/Futball180TV/105401" target="_blank">📅 22:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105400">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=vtlSLvrZ5U32lGsjD_XlcNWIO9VDz1T8TVa_Y2_DnlExCb0TjhuMamrvEFSrK4kAuMnbuhYwnbvzpo4FBf4gj22UryciTnOu2s48_L85qVfMucOI-RQPG5ai1r2f4adFERDiKKfLf2HF7aFnjM73kcI_MCqiczUSuqPkD21jC9WT6zneR_i2o2gY4BlUmEc3U30HJyDeD7aziQCjSzwc6ahHV9pOlOYSmvRPNHvLO_vqN0ejUqHAafFPBAElFEZgqcaDAbgn2jXIa7C2Jr_1hjmu6Zss0rK--G5V3roO5H7wBAH1pchAak8MnRoEhFjVEHgjchNdVwIVA9ffqaScxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c06eb0d1ff.mp4?token=vtlSLvrZ5U32lGsjD_XlcNWIO9VDz1T8TVa_Y2_DnlExCb0TjhuMamrvEFSrK4kAuMnbuhYwnbvzpo4FBf4gj22UryciTnOu2s48_L85qVfMucOI-RQPG5ai1r2f4adFERDiKKfLf2HF7aFnjM73kcI_MCqiczUSuqPkD21jC9WT6zneR_i2o2gY4BlUmEc3U30HJyDeD7aziQCjSzwc6ahHV9pOlOYSmvRPNHvLO_vqN0ejUqHAafFPBAElFEZgqcaDAbgn2jXIa7C2Jr_1hjmu6Zss0rK--G5V3roO5H7wBAH1pchAak8MnRoEhFjVEHgjchNdVwIVA9ffqaScxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
🇮🇷
📹
مارک‌کلاتنبرگ در لایو برنامه عادل فردوسی‌پور: موعود بنیادی‌فر باید حسین کنعانی‌زادگان را اخراج می‌کرد و این تنها اشتباه فاحش داور بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/105400" target="_blank">📅 22:48 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105399">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=g5yGeNW-rs1dDltTCX853CCmxC56IPtTsDG20qYtfOMZcIe6ZFCvBc9tjKwV6mG4wofY5VQOi8r0ucaDVe9LkdCUYzdOGBL-3NpRQXeDhtn3jvTYMpysy7XKF8bp25kpcZ6cHgS_GgL-P5E7FhFKBfhsg8YG21BgXDYUk9G1KDuX9uCT8xbCKmTe2-pV4f48a4h1ZmxZu4fJodDMG9CSJuvHa4Gledr38kgWrlyRshv1I_qdemmPkzpckUt-wDH88n20_0rwJEbljvxex3wFACFQJjJhFBmdrGe95rjya0Ln7frYmL-DWmroK8YXSn_Es8-pkiyPHauxxVyzEeGP6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce1c0fb29d.mp4?token=g5yGeNW-rs1dDltTCX853CCmxC56IPtTsDG20qYtfOMZcIe6ZFCvBc9tjKwV6mG4wofY5VQOi8r0ucaDVe9LkdCUYzdOGBL-3NpRQXeDhtn3jvTYMpysy7XKF8bp25kpcZ6cHgS_GgL-P5E7FhFKBfhsg8YG21BgXDYUk9G1KDuX9uCT8xbCKmTe2-pV4f48a4h1ZmxZu4fJodDMG9CSJuvHa4Gledr38kgWrlyRshv1I_qdemmPkzpckUt-wDH88n20_0rwJEbljvxex3wFACFQJjJhFBmdrGe95rjya0Ln7frYmL-DWmroK8YXSn_Es8-pkiyPHauxxVyzEeGP6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
💙
سهراب بختیاری زاده: فکر می‌کنم اگر آقا مهدی (تارتار) بازی را دوباره ببیند، نظرش عوض می‌شود.
🔵
اوت دستی یکی از راهکارهای ضربه زدن به حریف است ولی ما جزو تیم‌هایی هستیم که بازیکنی نداریم بتواند اوت دستی به آن صورت در باکس حریف بیندازد.
🔵
من بازیکنانم را تحسین می‌کنم چون دو بازی را در مدت زمانی کوتاهی انجام دادند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/Futball180TV/105399" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105398">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=vFxHz_BoXKKoS-CLhmGFX1nJozeqrKnnh0PtssWmcUSr8-In5nXx_i9RUM_ulizrNrK4K5Am_L_K0jxhjx81iOyP_iMRB87J86Z_BqBD48sHwDKcqjYl1jatPyW8cqiXEdU-VwIT6wHAJyYz9MQsWYXdZ50SEvSGayQRxc4UTkPbSf9j3CFeF6W1JFpimscyVHX02f-0kIIknSezlsP95wdkp30FqMw3Ys8hjC3jqjt6SLBeLu0b7vBfhlKwplFAlOXHSNoAAWjOnXJvUZ2NyJFqBPiAhS4ht_NepK0KGALr7zQi6KBXn2D2OhWRdAP97vcBMiSMzw5oB9_27A0t_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cef9c1a80.mp4?token=vFxHz_BoXKKoS-CLhmGFX1nJozeqrKnnh0PtssWmcUSr8-In5nXx_i9RUM_ulizrNrK4K5Am_L_K0jxhjx81iOyP_iMRB87J86Z_BqBD48sHwDKcqjYl1jatPyW8cqiXEdU-VwIT6wHAJyYz9MQsWYXdZ50SEvSGayQRxc4UTkPbSf9j3CFeF6W1JFpimscyVHX02f-0kIIknSezlsP95wdkp30FqMw3Ys8hjC3jqjt6SLBeLu0b7vBfhlKwplFAlOXHSNoAAWjOnXJvUZ2NyJFqBPiAhS4ht_NepK0KGALr7zQi6KBXn2D2OhWRdAP97vcBMiSMzw5oB9_27A0t_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
💙
سهراب بختیاری زاده: کسانی که بازی را دیدند، از این بازی لذت بردند و از دربی‌هایی بود که حاشیه به آن شکل نداشت.
🔵
در نیمه دوم ما تغییراتی دادیم، به دلیل اینکه در نیمه اول نظم بازی را در میانه زمین به حریف داده بودیم و این موضوع را رفع کردیم.
🔵
روی یک غافلگیری گل خوردیم ولی برگشتیم و این نکته مهمی است. می‌شد گل‌های دیگری هم بزنیم.
🔵
هیچوقت درباره داوری قضاوت نکرده‌ام ولی دو هفته است که اتفاقاتی رخ می‌دهد. در بازی با فولاد دو کارت زرد اشتباه به ما دادند و امروز هم فکر می‌کنم صحنه اسلامی، پنالتی بود.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/105398" target="_blank">📅 22:46 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105397">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRCTjaTm5yzyRytfC8e60VFkzNNy5mPObtDKTpA3vzLcocvwhYHjmdTDrXEzU7Bz4cTNbQgrKWQaUbPUijmbho1zTCRDhXa-61FVvb3Eb0bNcvuZnDL8yR4oAAxVyORONjKNtcaoXx6NFiUjbS-IubEncoh9R2BL0klyFRk45taB6TwzTZBSgFjObYF5IY0Ffr1ST1u1QyqDiHiKw8AIcCnC6pe71UySLJyFeja_jtv9DLc-MIaoJbdKTsFQUEfLE1J1DPBEFEtDiGI2nIH1lPOGH1R9i1gatgI2l2AbraiZsirsWwcNtR_Cl9ttgItbLjT80GsLWdX6k0BJ4sj5Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/Futball180TV/105397" target="_blank">📅 22:35 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105396">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiBi4V9Lq9tL_i2NpZOUCpdBCqlzq5TPVJ3uBPICnH0c3hSCp7Bz8sUiQGELN1jkwvhGgt5_bD89a-jGcNf_Ny4MbJHPJsJLK3KAvEbZLzQh-AmYFpNzycEAV-lrlnouFinLv608tnZBUDBB6133m5LTSwgExurFk-U5qEh6RcUsv8AnpusFYF5yl-U1IGxDnk2Rg-qLGOGvNOOjwATxswXUFbpNhj4V0EnkfJ-HkkU2LMscCTcLXkbG9AInsVHnnEvsoSotSonOYuwGH32vdWd3S1RccBB67Ta1hgWTr94nnmCDdy7dkm6aHWnckNDNqSvtrelJv3_YW_7RWQTRDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
سپاهان در بازی مقابل نفت‌آبادان به تساوی بدون‌گل دست‌یافت!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/Futball180TV/105396" target="_blank">📅 22:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105395">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
‼️
⚠️
لحظه حمله کنعانی‌زادگان به عارف آقاسی که منجر به خونریزی گلوی مدافع استقلال شد و داور هم این صحنه را ندید!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/Futball180TV/105395" target="_blank">📅 22:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105394">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=akeDvVEYOPC8nq-AZCHzYQzbWCuAaT7cw-8vXUl8-4hizyA3QiYTVDqyjWThPXWRvjdgkhTkcEpPyDOJY8z6RQB_GwHMGn3HvZyHcA2B3DKSojQKQIyykMfiE1_1pI6nj2aZo0RbTcDUiuf1TdJZ97ETQQqyFrFyjk_w-dagoPMVNpZtOmHsRle8K3hg_vdlkXXiHmwhCJuYPv9DQhHklCQbEdYaSNFrxuldLYM6puPyldfONf0rXPoUNQpfJs4_Y-seLpMymgqZ3TOJroVFSHf9I0X6Ou4Yj8yEvZO5PWEYOpQZYA3ImQycUjna_X4aUeYrHuF1aYYNusaYkGFc3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/507e713ebd.mp4?token=akeDvVEYOPC8nq-AZCHzYQzbWCuAaT7cw-8vXUl8-4hizyA3QiYTVDqyjWThPXWRvjdgkhTkcEpPyDOJY8z6RQB_GwHMGn3HvZyHcA2B3DKSojQKQIyykMfiE1_1pI6nj2aZo0RbTcDUiuf1TdJZ97ETQQqyFrFyjk_w-dagoPMVNpZtOmHsRle8K3hg_vdlkXXiHmwhCJuYPv9DQhHklCQbEdYaSNFrxuldLYM6puPyldfONf0rXPoUNQpfJs4_Y-seLpMymgqZ3TOJroVFSHf9I0X6Ou4Yj8yEvZO5PWEYOpQZYA3ImQycUjna_X4aUeYrHuF1aYYNusaYkGFc3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🎙
❤️
تارتار در نشست خبری: گروه داوری امروز خیلی خوب عمل کرد، خسته نباشید به آنها می گویم/ امروز هم پرسپولیس خوب بازی کرد و هم استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/105394" target="_blank">📅 22:16 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105393">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
ترامپ: برای آغاز یک حمله ویرانگر دیگر به ایران آماده‌ایم که مدت کوتاهی خواهد بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/Futball180TV/105393" target="_blank">📅 22:11 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105392">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Ph6NOd2bi16shhNYYWHKT-vLHL45JO39HXY-B5IFce2Oe1bWhDe2loXUYlQIymWE0tQgFKavFBUDZ1oeVqyuCqfKuy2jetoCC4A-9aCcAr4BEPFlNGdJy6h_62t1GnkQWTodAHuytmqcepq2xus_rQta2q1ax2YeQBnE-jw15GO__m0SchF8LvYBo5NfcWuVS631SKZnNMb07ztzATpc8vZN4JRUEuoUFAJFLqNYpfPCFktGWft8Bn_TVe1XLTsdKKz3az7oLz7lbfeA57iNq8hKHJRiYc-Jw8cvE5SEttUP7a0yPSqEfN2rNgtZ2Dt4-L7PLSY0uoc-rDa7knfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/Futball180TV/105392" target="_blank">📅 22:07 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105391">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63becc7280.mp4?token=KXtei4f638h0qkGMXK8VbXSU6gSDVoEI1by3h0ZB1g6HMcPHUfAEa82GIGwya5kwzLJf_X2GQ3zS9Urn5by7L7oC5INeRrCbK9Z3q46qY3-xPsBZoxUYUZwTYzTVTpQJ9Q6z-vkyGND20g75ZtXT_-cQ0fwQhnVzmSrC9g94Gqp2dIwAcAMnz2YYDT9dGePZ00PDi25oX9XCXG8uzi72JAOT8ZUHMvCh6IGzRdnzUqzZO3oaORC2bBM1kdnZsP9ydGKy_7Vus5xhoda_J__HURPR43dzPSdQ__hMhVxp9FFGLgcCsrlH4OGUF3LbTdPNwv1nbmEsxKEs3eURhlIjRnedYHQe4c2AZDe9W-N0kag6JHrVPao2Afri89sYUqifmWENVvgJbFX2uBfVdavbByw3a8zGRYdnkmVpbBRgRNIBRDwJ8GpQkIZpxkxTHaTe0QyfSq0HFBHTAR1JBU3JESzVJDDLx-u36hBypvcY21f8RmqHd2jrwOa2O2b6vQXE48Lq99Akaa7sHnhlS8S4IRTAuoMGqv7vVD8cXRu2QUiMWo1t50Li-xMyNMJIPG8gp8TMYFUoGMAIbKU04MActWRIANB73qHlKh82x_yrbFsJqnS5U4DT9bwfAiKlk2hloPix3RpbGFg53-G-K1PYdO3kGXeb5RQYWp-b5HZdVOY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63becc7280.mp4?token=KXtei4f638h0qkGMXK8VbXSU6gSDVoEI1by3h0ZB1g6HMcPHUfAEa82GIGwya5kwzLJf_X2GQ3zS9Urn5by7L7oC5INeRrCbK9Z3q46qY3-xPsBZoxUYUZwTYzTVTpQJ9Q6z-vkyGND20g75ZtXT_-cQ0fwQhnVzmSrC9g94Gqp2dIwAcAMnz2YYDT9dGePZ00PDi25oX9XCXG8uzi72JAOT8ZUHMvCh6IGzRdnzUqzZO3oaORC2bBM1kdnZsP9ydGKy_7Vus5xhoda_J__HURPR43dzPSdQ__hMhVxp9FFGLgcCsrlH4OGUF3LbTdPNwv1nbmEsxKEs3eURhlIjRnedYHQe4c2AZDe9W-N0kag6JHrVPao2Afri89sYUqifmWENVvgJbFX2uBfVdavbByw3a8zGRYdnkmVpbBRgRNIBRDwJ8GpQkIZpxkxTHaTe0QyfSq0HFBHTAR1JBU3JESzVJDDLx-u36hBypvcY21f8RmqHd2jrwOa2O2b6vQXE48Lq99Akaa7sHnhlS8S4IRTAuoMGqv7vVD8cXRu2QUiMWo1t50Li-xMyNMJIPG8gp8TMYFUoGMAIbKU04MActWRIANB73qHlKh82x_yrbFsJqnS5U4DT9bwfAiKlk2hloPix3RpbGFg53-G-K1PYdO3kGXeb5RQYWp-b5HZdVOY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
📊
آنالیز گل پرسپولیس به استقلال در دربی که عدم یارگیری آبی‌پوشان مشهود است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/Futball180TV/105391" target="_blank">📅 21:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105390">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
‼️
🎙
تاجرنیا: موقعیت های استقلال بیشتر بود و حق ما برد بود/ یکی از جذاب ترین دربی‌های چند سال اخیر را شاهد بود
سهراب تیم بسیار خوبی را جمع کرده است/ من به این تیم امیدوارم
داوری بازی؟ مهم این بود تماشاگران بازی خوبی دیدند و باید 3 امتیاز را می گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/105390" target="_blank">📅 21:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105389">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOmjgsIU_zxz4eZoFUC0PMkxmZZz3v2W-tTuk_mK-JY9Z-k9pzquw3wOzPRc2GG8XXKK22mZ3VXG2BUt_84e6Fk_SUS99OfRx1ytxLaNYn7AVcSGzthG1Eiuv_A20hqV2R8RaF8NUqXWp4SrVymOFebMnMI0RowWFuj2MVF47fUNwMODozUPNHK66YFlqPMfX22fug61HcI8uDh_bqrYyOtwjTGRejZwHAsrnXip31meSD1EE9voEGXqvseiNwJrtznz2TF5StNWtlXNYD5QAKhziivAerejraTx6rlLI5nu-H8WZk6XHTWy8n7jFpT4jmUPIVZN7MsEDtC4xFBjpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇮🇷
🇮🇷
آمار بازی استقلال - پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/Futball180TV/105389" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105388">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
شکایت رسمی پرسپولیس از استقلال؛ پای ۳-۰ وسط است!
باشگاه پرسپولیس با استناد به الزامات سازمان لیگ، از استقلال شکایت کرده است. سرخ‌ها مدعی‌اند آسانی و اشورماتف طی دو فصل اخیر بدون پروانه کار و اقامت قانونی به میدان رفته‌اند و در صورت تأیید تخلف، باید نتایج بازی‌های مربوطه ۳ بر صفر اعلام شود.
حالا باید دید سازمان لیگ با این شکایت جنجالی چه برخوردی خواهد کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105388" target="_blank">📅 21:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105387">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
خلاصه بازی استقلال یک پرسپولیس یک
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/Futball180TV/105387" target="_blank">📅 21:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105385">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IRa0XgUC4G4QXx0YtSgwpJW_kn9f3Dot9kAiW9dRHBbpEwVYmN4bN6APyNemWLilhaPUIICfD53XC1OMYQpvn8fuDMGKbAGRjtt2dSH97--qGiVk5JEzw4Q2n7oBjpD-oRYNwar5Gt1Kxu53PxYhPzK6vC9wgxf1i5PIRkUEuUFsSx4MejsS0aNt_TFLZxGsY1Xpqb1TQJ6p2P91NThzIgjYuBTJqDFGBH7uz6tlotgbOLyektuI88vsLdTCRazUMYqcrlnfNiQsIdxbaYz1zAN2w2qnn8DKwuQRaWARz17B8Q2UZGa5l9JRe4DS-jL4U2CB3Xibgzgj_qFDsvgO-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
📊
جدول لیگ‌برتر پس از پایان بازی‌ دربی! پرسپولیس در دومین بازی بزرگ خودش هم با رقبای مستقیمش موفق به برتری نشد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/105385" target="_blank">📅 21:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105384">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GHC4AxN9ufNZUi8EVfp47GxS1Nspq0OM6JunGzGN9lf03IYSSXT1saR4Eom6E005_tD7kZQcv05z46_RtBuyPdk0Pe5c0yeHjAiqoUwaLMyWzSqL69oZ2HhffP7pQGSSn77UHRJHG7hBKx6Cw6XAMzA_vWgsPKhaYZR6b8oeeC-97g3Nv84byi7rDPD3vflYBSODi4ZPFl746VFL5r1K3OEX5PNNuHoxsnzI_iVUXAimVnlWY8_O6zG2YAwwxUK3tAiYooiC-ffhVBbofnAwJxCz6L3Uj6KosbImv-lPE_VEeR9mFIM_bcoVUlx_HAq70kWIwQ30ILK5fUQkQI4m0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/105384" target="_blank">📅 21:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105383">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VvBLRCxKmM0uoUN2l8pNSt3F5DbJ2Sf_VanvgHwsAuup5DVCQqKqKLuHN99WdOlxe2R978Jq_zWB_I9TM6avI7f9WwdB0jH5gFIpQ7Ow7AKJBsL2Y3dl2F85_Mh_gyyZqHYP8TQDEaaqBUKEWjgH-851G0gb2N_Qvsr61lybmr1SRey1MKr-gRU8Niz_qGrUHiXwA0O6jVDlcF7Y4Ac2WrJkfXnmBNHuwx2JskrdKdv1NsqIzvd_jNPz85P3YFWyqn-4pQugV1OmtGndkbsQ-LSQWCNwQsmFKo0ts7g8AUGIPJhJVnXH-ocDhxsH4tLU1kY8KfmIxlIkvFkJRSPT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
هفته‌پنجم لیگ‌برتر فوتبال؛ ۹۰ دقیقه هیجانی و تماشایی در اصفهان بدون برنده؛ هواداران از دیدن بازی تارتتا و گواردیولا لذت بردند!
🇮🇷
پرسپولیس
😃
-
😃
استقلال
🇮🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/105383" target="_blank">📅 21:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105382">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=XrJdxnG5i5MMQsTl8GVtmRLyRLzniMXoo4ppTKeTwqxLvt9v7CP0HzvRALj_G8LUYS6FT0bKN2zfc5QdgNRK3TL2QP5WZvkvkygVLQ3sYhaSzmX3m2HErT6RFY448yUAYivqzHvOOswCJaePcDK_iayn4vPGtqmNhv6Bq9MEdsK3ltwJLyuwUeVHf3iOFxr_563tsH0tAT65P2x2CoJ_H9To5lwykBoiyer54ZA9XkeSKKy8mN6bkGzzla_xgFb5pwRg9IBDWUxNDW8B2Jh_kU_ezD9Pm0Bl_2WlZNwTyx1xTHtpUfl110ryutkFpDGF-Sw1sRjlb72shIY_4ncPnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b714d173a5.mp4?token=XrJdxnG5i5MMQsTl8GVtmRLyRLzniMXoo4ppTKeTwqxLvt9v7CP0HzvRALj_G8LUYS6FT0bKN2zfc5QdgNRK3TL2QP5WZvkvkygVLQ3sYhaSzmX3m2HErT6RFY448yUAYivqzHvOOswCJaePcDK_iayn4vPGtqmNhv6Bq9MEdsK3ltwJLyuwUeVHf3iOFxr_563tsH0tAT65P2x2CoJ_H9To5lwykBoiyer54ZA9XkeSKKy8mN6bkGzzla_xgFb5pwRg9IBDWUxNDW8B2Jh_kU_ezD9Pm0Bl_2WlZNwTyx1xTHtpUfl110ryutkFpDGF-Sw1sRjlb72shIY_4ncPnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
صحنه ای که بازیکنان پرسپولیس اعتقاد به هند داشتند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/105382" target="_blank">📅 21:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105381">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=KHSJzIpkK9HHYi_viH5vQTEwTLa6EYobVgFipbB08fRnunfzEbH6OcU9MhUBK2Wn3JOgzWQMBNM6QqozY3x2_mCXqeWhCJ51J6yHBHsnl_yeahfpO_VWOkFNWwE0qwQMt9yVxUQvh5QKQgJ9XOOtlbsQBA-C87akCdP9UCXAqEeMUzj1twMtbYpcmXpRNPd1dR5XfhkdOpm0b2EegOLLFiV20hnfxRzUwnXjSJbUB3_r_m1ioxJoum3mOvzCpu6lruyvn4BXlyljruSbudSNT2mmh2rLefLUeTmgYWQomXP65foUgWASFnfMgtX5Jqhzy9QTh3Skp11zyAxKDpX6Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d553ea91ff.mp4?token=KHSJzIpkK9HHYi_viH5vQTEwTLa6EYobVgFipbB08fRnunfzEbH6OcU9MhUBK2Wn3JOgzWQMBNM6QqozY3x2_mCXqeWhCJ51J6yHBHsnl_yeahfpO_VWOkFNWwE0qwQMt9yVxUQvh5QKQgJ9XOOtlbsQBA-C87akCdP9UCXAqEeMUzj1twMtbYpcmXpRNPd1dR5XfhkdOpm0b2EegOLLFiV20hnfxRzUwnXjSJbUB3_r_m1ioxJoum3mOvzCpu6lruyvn4BXlyljruSbudSNT2mmh2rLefLUeTmgYWQomXP65foUgWASFnfMgtX5Jqhzy9QTh3Skp11zyAxKDpX6Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوت علیپور خطرناک به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/105381" target="_blank">📅 21:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105380">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsScHz8W8nfcdpErj5GRqav6qjBMWQY7x2EpaBlW_jQ90orasx6OacfDOorHBuxjXxWQ86WN1hh0fJMrfUR875VnGwKNVUwVl9wCMW0XXHO0ftWnVv6nd92WVhaGoa0bsopWl10uLkahFCIhfl40JADZpapyq_St5Gs0GDkjVs6dJTHymdBpoX5Nk29ghhu87eem-1YDpQJd_u-0LN4T_T4VpcL1KN8hKbqyd8YCg_s2XXRECmWNpapOmoF9Fa4Eo7nv8EXdfX8e_GrCzLeM6CdpMSe3QNOB8LqTwc4-GiIbzt0SQ_ZpaNhJWyg0aP86ERPfn6JxocAgb-JkVSZILA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
‼️
🇮🇷
🇮🇷
باشگاه استقلال با انتشار این عکس نوشت: تصویری از آسیب به گلوی عارف آقاسی که توسط کنعانی‌زادگان رقم خورد و با بی توجهی داور همراه شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105380" target="_blank">📅 20:58 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105379">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=bY4Fx-OMQBNt12FR6IzXqpRX4hR1aRFNMxk6BIlA7TDHVORjPr7-f7oOKwXO-qpUNtCk01PLTU0tPio7nudlR4jgpAhMmpnlbIuHwicAiCjDFOcUZOCE42QOp8xfb-7FxFt__7exUwofDY0FeM-FvRHkdRDhm_zQF_O3D-jXFjbh2bOCt7GkFugIIGjN82sejweA0c3hcwlJxAbx_QWg9W7lmAM0ZEEVt0DiqLqWIWytNwwdRXpIvQ4ZsBTq5BiUPMCdU21IV58J_1bkKzeAgXu5BRLiEfdHtkV8HYzTrxhpxg26ORl2ear4eU0HCgsFmTzXBwjCOHNrv0Ti_DL2sQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3436b36eb0.mp4?token=bY4Fx-OMQBNt12FR6IzXqpRX4hR1aRFNMxk6BIlA7TDHVORjPr7-f7oOKwXO-qpUNtCk01PLTU0tPio7nudlR4jgpAhMmpnlbIuHwicAiCjDFOcUZOCE42QOp8xfb-7FxFt__7exUwofDY0FeM-FvRHkdRDhm_zQF_O3D-jXFjbh2bOCt7GkFugIIGjN82sejweA0c3hcwlJxAbx_QWg9W7lmAM0ZEEVt0DiqLqWIWytNwwdRXpIvQ4ZsBTq5BiUPMCdU21IV58J_1bkKzeAgXu5BRLiEfdHtkV8HYzTrxhpxg26ORl2ear4eU0HCgsFmTzXBwjCOHNrv0Ti_DL2sQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول استقلال به پرسپولیس توسط آسانی(60)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105379" target="_blank">📅 20:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105378">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">آسانییییییی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/105378" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105377">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یاسرررررررر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/105377" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105376">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">استقلال مساویووووو زددد</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105376" target="_blank">📅 20:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105375">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">گلگلگگلگلگلگگلگلگلگل</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/105375" target="_blank">📅 20:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105374">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=SQdMYtvizasq40LrmpfSBHdvaig2VqZZhbSrc0eAYnXAgGtLOYvi0DzUwkj6xRLOROVTwRQYcAyMkHV5w5zI-8WCjMiES08OJYugnUxLNkTn4xtvEDjUhLJR5dEBMGz8X1nubG2dmwIabGZ9Jm5blqfvuz3YjVekafM4TR6m39qLO52X-ct2-gzYXY1uwrlxmseGxwZrtqa4ceukygb6qMiRTbsF07BvYlGS1mvSDbk7sLE4VTXhajDJWqUhZ-qSGS-iU4JvIgNdqDBLGOTzs9Fr2frBjMCoAoPUxxRolh2I3NzfzAXYzwxidaCTdplLThyE8-A3x_8RFv-Jph7DPY6Fwx-paIcdxVATMhwk_emVbWQOcpRidrZ4XRnbVSM6VPVe_sGcJ5Q_Y8hXhwaVD_SAJI_XkmcIl-zOCbsmeefLJ-_v0j_bd08Zwj3X0U_0h2M71TOtMBnwOWrOORQGfKPrKNXoB6Ap7JItKV1ZFhSzf1ssdIcFwDRCYjfjGJIK6Zz5M1Y1gkkOBRKOc9xYv8omriXFrsxPcz0XE9HDTBhs50t59qiscxLJ1FKwgqhrhmTbDFLpti4Hvyw-p4HeY7lzuQ7Q_yZY6kwHs8sLP5yy051TZjC1bsyv_U9liCSTOiHEx8cys84MkNI3BT_8NGpI7Y9XVsAdQdshN4ob7FI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c9bc0b70b2.mp4?token=SQdMYtvizasq40LrmpfSBHdvaig2VqZZhbSrc0eAYnXAgGtLOYvi0DzUwkj6xRLOROVTwRQYcAyMkHV5w5zI-8WCjMiES08OJYugnUxLNkTn4xtvEDjUhLJR5dEBMGz8X1nubG2dmwIabGZ9Jm5blqfvuz3YjVekafM4TR6m39qLO52X-ct2-gzYXY1uwrlxmseGxwZrtqa4ceukygb6qMiRTbsF07BvYlGS1mvSDbk7sLE4VTXhajDJWqUhZ-qSGS-iU4JvIgNdqDBLGOTzs9Fr2frBjMCoAoPUxxRolh2I3NzfzAXYzwxidaCTdplLThyE8-A3x_8RFv-Jph7DPY6Fwx-paIcdxVATMhwk_emVbWQOcpRidrZ4XRnbVSM6VPVe_sGcJ5Q_Y8hXhwaVD_SAJI_XkmcIl-zOCbsmeefLJ-_v0j_bd08Zwj3X0U_0h2M71TOtMBnwOWrOORQGfKPrKNXoB6Ap7JItKV1ZFhSzf1ssdIcFwDRCYjfjGJIK6Zz5M1Y1gkkOBRKOc9xYv8omriXFrsxPcz0XE9HDTBhs50t59qiscxLJ1FKwgqhrhmTbDFLpti4Hvyw-p4HeY7lzuQ7Q_yZY6kwHs8sLP5yy051TZjC1bsyv_U9liCSTOiHEx8cys84MkNI3BT_8NGpI7Y9XVsAdQdshN4ob7FI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ضربه خطرناک آسانی به تیرک برخورد کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/105374" target="_blank">📅 20:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105373">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=eaBV2eqs966XVAvuwjsBnQ6lfZf23Bv1NzVSfHABG7lIN2oF82Y-Is0D2Cf4PdrFxRUrDADIWyIvpzgdJ70O-4vnDHBUxzgTDcHHpnWiOqYjxkhr8wvl69h34tKhYZ4Fb8Nj89m7zcyFye8VkNPpr1TBSMPi3NMVIyWGrDOT-5Ar-lohbuUfOG9j_Aacy8yeDpXkT6eSEs1sfLMlrfxeKn_p8lYfmf-DZZpWWL_j0yekJ3MncZXaRMFkM1ydCQMLh56hKbvYnXx7YANY4S4Kq9ITb-b8zyA1tbZgmKNq60vKeQCUHvNF9PZ9g-mXFjNSZsBQksKZVE0lvL2x2Lhn2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c2230f3b.mp4?token=eaBV2eqs966XVAvuwjsBnQ6lfZf23Bv1NzVSfHABG7lIN2oF82Y-Is0D2Cf4PdrFxRUrDADIWyIvpzgdJ70O-4vnDHBUxzgTDcHHpnWiOqYjxkhr8wvl69h34tKhYZ4Fb8Nj89m7zcyFye8VkNPpr1TBSMPi3NMVIyWGrDOT-5Ar-lohbuUfOG9j_Aacy8yeDpXkT6eSEs1sfLMlrfxeKn_p8lYfmf-DZZpWWL_j0yekJ3MncZXaRMFkM1ydCQMLh56hKbvYnXx7YANY4S4Kq9ITb-b8zyA1tbZgmKNq60vKeQCUHvNF9PZ9g-mXFjNSZsBQksKZVE0lvL2x2Lhn2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
گل اول پرسپولیس به استقلال توسط محمدمهدی محبی 50
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/105373" target="_blank">📅 20:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105372">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پرسپولیس زدددذذذذدذدد</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/105372" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105371">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">گلگلگلگگلگلگگلگلگلگلگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/105371" target="_blank">📅 20:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105370">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bef49689e.mp4?token=RPhOlh0Cd7l0ARSHvORcm3jDSdHKRory8qVHTRNnvJ5-yC8yGpkVtR-ag4hJEIPLnNET3A1ecakit2rYjr9z8ak5K_A78x3vqqhnM8dVDfO21XBJOpbpniHpfrWCsv3eluvP66PlO1iTLlLtaLdECQQrdqfyWD-tcjo0Y9w_UTkPemLBgjoe4OWClUBmryWYhsa7vOAZ4X65jN0almrKjtzV5piU1sKzONknuaQ6MRhzM-djkrCxM_9hE62dpEZjw-rBEmltfcL3NJcMTuv_tmMlkVb2nRfo_Fe4FU-cqGv2FesmZgChRfN5P5DKsJBPyuzBx03q-xz2qrTboaxlaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bef49689e.mp4?token=RPhOlh0Cd7l0ARSHvORcm3jDSdHKRory8qVHTRNnvJ5-yC8yGpkVtR-ag4hJEIPLnNET3A1ecakit2rYjr9z8ak5K_A78x3vqqhnM8dVDfO21XBJOpbpniHpfrWCsv3eluvP66PlO1iTLlLtaLdECQQrdqfyWD-tcjo0Y9w_UTkPemLBgjoe4OWClUBmryWYhsa7vOAZ4X65jN0almrKjtzV5piU1sKzONknuaQ6MRhzM-djkrCxM_9hE62dpEZjw-rBEmltfcL3NJcMTuv_tmMlkVb2nRfo_Fe4FU-cqGv2FesmZgChRfN5P5DKsJBPyuzBx03q-xz2qrTboaxlaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
مهدی تارتار خطاب به بازیکن پرسپولیس؛ پا نشو!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/105370" target="_blank">📅 20:34 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105369">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ae4fcc9a0.mp4?token=BME-G4-SJO-aHI2FGK4UwGUm3hX3-SlpMSTxYS0XLGkRz3tawf_-2iExmic-gucrixwZV3dgK6vfP_5jgaffydNs0-5ptW8-Lnm3rXsOD1osNfx0sp6YBB7eBi42lorSCDywL2brrVA9DXpnuB_GYzzVkUqOH9OSCqZJ2WG-4iUY-BHHXaUlPcUw0KUs_hM8KKL3klPX-ZxXrIq8KJn9trx_GS6hii4gOUD_pNlQLpAKRamsG1nWF3CaD0na5xmwVaGqkXWLXoYxH2JROBdVCt4OcfPdODVeE7K1viywgbTM0-rVtkQ-VFsw7IbKD4UkmIVd7oKNXV11upagGGJjlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ae4fcc9a0.mp4?token=BME-G4-SJO-aHI2FGK4UwGUm3hX3-SlpMSTxYS0XLGkRz3tawf_-2iExmic-gucrixwZV3dgK6vfP_5jgaffydNs0-5ptW8-Lnm3rXsOD1osNfx0sp6YBB7eBi42lorSCDywL2brrVA9DXpnuB_GYzzVkUqOH9OSCqZJ2WG-4iUY-BHHXaUlPcUw0KUs_hM8KKL3klPX-ZxXrIq8KJn9trx_GS6hii4gOUD_pNlQLpAKRamsG1nWF3CaD0na5xmwVaGqkXWLXoYxH2JROBdVCt4OcfPdODVeE7K1viywgbTM0-rVtkQ-VFsw7IbKD4UkmIVd7oKNXV11upagGGJjlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
طرح هواداری دو تیم روی سکوهای نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105369" target="_blank">📅 20:26 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105368">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=aVr2PdyfSYaiyOe-VTppd-zvSbtVEJlo-GBPvfvRWzF1-dtItRAPlAumwUvErMpZE1yx-s01ZD723fHbpnBbncmErbMj1tKkPcJ14QUJPHD-kmxnrlTonZNkrasWeF6ELCWhVDhM6-omvByjKruXfZzMVQdBOVzfHYW3bL28Jhm39yGpA2qa3bPDeH2lA-ksjXnB4EdxqX9QLsjwr7xJriXETSkcmdiB4jf8M5fECNZRApSgaWmr3GsMz-84yKDDMA0kgbfxZEmitL28Lqg-X3bB9T8gvZwFXMfLBpUeWqC2NRkoxT7PAa0yZC9-r4eHUzI1GquXIQs6t-sh4Wjn3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a8cd40ab6.mp4?token=aVr2PdyfSYaiyOe-VTppd-zvSbtVEJlo-GBPvfvRWzF1-dtItRAPlAumwUvErMpZE1yx-s01ZD723fHbpnBbncmErbMj1tKkPcJ14QUJPHD-kmxnrlTonZNkrasWeF6ELCWhVDhM6-omvByjKruXfZzMVQdBOVzfHYW3bL28Jhm39yGpA2qa3bPDeH2lA-ksjXnB4EdxqX9QLsjwr7xJriXETSkcmdiB4jf8M5fECNZRApSgaWmr3GsMz-84yKDDMA0kgbfxZEmitL28Lqg-X3bB9T8gvZwFXMfLBpUeWqC2NRkoxT7PAa0yZC9-r4eHUzI1GquXIQs6t-sh4Wjn3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
موقعیت خطرناک یاسر‌آسانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/105368" target="_blank">📅 20:14 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105367">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a811272008.mp4?token=d_0YvEIH6yZYNXrmgUNF5sO0oAv9UvjB_pwYI0ZBbRFDbsIDw17HVMgEAtlLYTNc0JR92QxBKER592lvGv6uZx2j0Pv-jVQEq7-s4Z9J0dnBYwc8uNwsercFONrVFI5ijW0S3MhJxMuE9ItI6pinK0GcZnQ6HMoD4sbv5Co5fg0bdarqXDT2n_4JGoluwn_nsmHZfZ5-D9qaLSA3mXw9LQ7JpcSDnUVUW3hwV4q3folUT1agRg1s4Wj9ObFzXI2dqyJIPnwy6NTLAmTIb5Oqe5qtQRMpkhMFa2eAmtkve_9-Ta-930RsmPDixPaPxI97Er44n0CTPhVUg_8BOoDKnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a811272008.mp4?token=d_0YvEIH6yZYNXrmgUNF5sO0oAv9UvjB_pwYI0ZBbRFDbsIDw17HVMgEAtlLYTNc0JR92QxBKER592lvGv6uZx2j0Pv-jVQEq7-s4Z9J0dnBYwc8uNwsercFONrVFI5ijW0S3MhJxMuE9ItI6pinK0GcZnQ6HMoD4sbv5Co5fg0bdarqXDT2n_4JGoluwn_nsmHZfZ5-D9qaLSA3mXw9LQ7JpcSDnUVUW3hwV4q3folUT1agRg1s4Wj9ObFzXI2dqyJIPnwy6NTLAmTIb5Oqe5qtQRMpkhMFa2eAmtkve_9-Ta-930RsmPDixPaPxI97Er44n0CTPhVUg_8BOoDKnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
فرصت عالی علی علیپور به بیرون رفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105367" target="_blank">📅 19:47 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105366">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=GHo_ZtTY5GZ6gv5U8IFN_VUvOzVcP1d8nParMcBphYdbgf-L7idpKDlZ8dANYcLRgMRDMAU-f31cuSZ8Gk_iyad6CD3d8Cv01qcnoVdUb_TqKBX_cb6s7zYW0RhFqpaDnwBVqtC3XcyI1Y5RKWkIdr7uSRuKuCJgfNFUTHFhKMYxF_jf9b_dN51lUVLUR6LoW2UumJenEdZAdjwnwyJZ9Dz5ECyOjk4u3CTph68EPL0SkSPDtqIZ0zYGTxrv1L6jKZgKrdg9lgh5eJC7jrke_A3gW1QOaHS0ALqZ0W1PVwOQCXOzp0vlJVsN0iUKd-4VgJaHNYtm1dFskFtbhjH7Xg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a4f888f78.mp4?token=GHo_ZtTY5GZ6gv5U8IFN_VUvOzVcP1d8nParMcBphYdbgf-L7idpKDlZ8dANYcLRgMRDMAU-f31cuSZ8Gk_iyad6CD3d8Cv01qcnoVdUb_TqKBX_cb6s7zYW0RhFqpaDnwBVqtC3XcyI1Y5RKWkIdr7uSRuKuCJgfNFUTHFhKMYxF_jf9b_dN51lUVLUR6LoW2UumJenEdZAdjwnwyJZ9Dz5ECyOjk4u3CTph68EPL0SkSPDtqIZ0zYGTxrv1L6jKZgKrdg9lgh5eJC7jrke_A3gW1QOaHS0ALqZ0W1PVwOQCXOzp0vlJVsN0iUKd-4VgJaHNYtm1dFskFtbhjH7Xg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
بهروز رهبری فرد: خیلی دوست داشتم که جلالی در این بازی باشد چون نقطه قوت استقلال همان سمت است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105366" target="_blank">📅 19:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105365">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KYmWye0K-mxnIW4gdetwwifNFQXA-Vv2EPar0R5ZRqppqfpNPYMMdrZjansSrawdwzFn1ZsdY8JmV5vuhWcDoXHNCWMASdDZG2nm3CdOw-wKG2uxp_G_37KsE10XsSUvb9MBGevjCoUHzNnXCi0kJHaiABp6hVTjGezsE19gpb5SjFHZ4H4VC9nV11OmRKFPkVi1yVSxLoNUirDB3-0w4CBUFCwDt5kpPk1EqzZIS2ZWsmxhmipPO_BSOUikdBydJr97SSzqgx_yyhy5s40aeosy9ESYi1MzIvOH8jUmigNqEoe0uXysejr3M2CQK1v31j9Q5IiFr1fBtXEB0TmKKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇷
ظاهرا جدید صالح‌حردانی در بازی امشب
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105365" target="_blank">📅 19:09 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105364">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=B0DvnnJkQbnxAZSofPkMtaFVBiLD0g3WuUqAUImGnC_WdLo49qmsDO5tRMbRL81cEGHekopM673O01Se8aoRjEaS81aU-I6YQT-LnKm4FD1apsPt8_6IMlkfPNQyZE812mrgglR5GPIO-M2_xVXBzlXP2GG5d2XRLsf9nwfgabae3wbAiNmVm_XSk5-yke_XVO2_htv8YOoBccsGTG9alyNVA938L8zzZcHc-CqRvX0mxRDoeq-8vgwmRC7HDbRiDZ55pQnKLNBKramlMvekw_RWUBxUGMHJtv4AfTIXAxQaveQuoA6xWR7xCBAm-zOButJKWO9CowdfbbYvEDCmpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04c8c7c65b.mp4?token=B0DvnnJkQbnxAZSofPkMtaFVBiLD0g3WuUqAUImGnC_WdLo49qmsDO5tRMbRL81cEGHekopM673O01Se8aoRjEaS81aU-I6YQT-LnKm4FD1apsPt8_6IMlkfPNQyZE812mrgglR5GPIO-M2_xVXBzlXP2GG5d2XRLsf9nwfgabae3wbAiNmVm_XSk5-yke_XVO2_htv8YOoBccsGTG9alyNVA938L8zzZcHc-CqRvX0mxRDoeq-8vgwmRC7HDbRiDZ55pQnKLNBKramlMvekw_RWUBxUGMHJtv4AfTIXAxQaveQuoA6xWR7xCBAm-zOButJKWO9CowdfbbYvEDCmpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
😳
😳
به‌قرآن خاک کسخل‌خیزی داریم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105364" target="_blank">📅 18:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105363">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=ULOXbaXjAX7wEMOTSuqH8OOFVuTZOOztfbTEFJBEDIBTX_MXAJ42G8TUT4plEmYut5_luhDYxXTvReKyS4_7SJ8Ww1-7OqkAwfkrBwPY58oYCm8BvYrSR2EEvT2WAEl3612ZTXzwp2gQYw1Wl40vxVasHlwOAJ4atmsq13Uu7DNrphC8fY3nYAhgXk0mKbuOS53ZDLlZoQnPRY1RharkjBm94SHjK8_9kWaPA8-WAzvX3NWNixMqeN1OA3eZm9XglrOwfq4dflODeJxR12NmwQ5voTEbQza2yALagZVKt2pQP-rebxvaedG-T8dFJtJQBXJq0FGRGUjUvget27yEpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7da52ed6cf.mp4?token=ULOXbaXjAX7wEMOTSuqH8OOFVuTZOOztfbTEFJBEDIBTX_MXAJ42G8TUT4plEmYut5_luhDYxXTvReKyS4_7SJ8Ww1-7OqkAwfkrBwPY58oYCm8BvYrSR2EEvT2WAEl3612ZTXzwp2gQYw1Wl40vxVasHlwOAJ4atmsq13Uu7DNrphC8fY3nYAhgXk0mKbuOS53ZDLlZoQnPRY1RharkjBm94SHjK8_9kWaPA8-WAzvX3NWNixMqeN1OA3eZm9XglrOwfq4dflODeJxR12NmwQ5voTEbQza2yALagZVKt2pQP-rebxvaedG-T8dFJtJQBXJq0FGRGUjUvget27yEpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
⚠️
🇮🇷
🇮🇷
هوادار استقلال به سبک هوادار معروف غنایی در جام‌جهانی، با طلسم اژدها وارد ورزشگاه شده
😂
😳
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/105363" target="_blank">📅 18:51 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105362">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=F5Kxk8AL_z68FQfb3fh6ieGSw70aEmtlwgK8Cct5znZ64KWDse-1WZOLDOqSPQqSi_QQTLItnRh4pOrmOd2dZ6yBDy1gpWn0RaKmjGRCnkFsVyWmHmNoFAgQcx_4ww_53b8CkAW8HGmzyD6qHDst8XWx9fO3fUDU0Nm99wsX_R8AtjwKBe5S8JdkOq0h-GCngUr5suwOOfzbaMLcpbVFzanjjQrpzFiuSDE1btLToZSSK0KdMyBqdAJpZ0o7z7H1s6BS7hrkWk9n-rwYVN1YNXsTk-GH1gv4hIElv0hLRsd-wa4YO_VakKFz45I2XeKVItBRNcfTShSfmy5c5d_IPFQCudC6I345GVD1BBuuk21ciyG5deR_1TexdDy7J9jjMRRMzDKLQTKqK_zrA7grIzd5vq-YHHuobXuv2NqlqjLmpSuO00kumPNHUAuKCyzWCvgA_fRrRXXIGHHlAAd1jBwouPFFxxV0YUiXai-TPnxhBu2UT6xtt_Ocmye__J291qpDVcTpqpEAtiappxO9cYdeTiSspmfuwOZGJxeNzukwbrvagpO4ZFhb-LmNyon8YdBX1-HYITffx4WFKQ1IbA-W_lqGsu9A_ZGQ2KPbMw4D1RU656jROt9Nu0PlZ7sSSekPwfaEpsoTLwbU6T7W5aZ71J3yfpjrhuw_dXKEzNo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4866011c8d.mp4?token=F5Kxk8AL_z68FQfb3fh6ieGSw70aEmtlwgK8Cct5znZ64KWDse-1WZOLDOqSPQqSi_QQTLItnRh4pOrmOd2dZ6yBDy1gpWn0RaKmjGRCnkFsVyWmHmNoFAgQcx_4ww_53b8CkAW8HGmzyD6qHDst8XWx9fO3fUDU0Nm99wsX_R8AtjwKBe5S8JdkOq0h-GCngUr5suwOOfzbaMLcpbVFzanjjQrpzFiuSDE1btLToZSSK0KdMyBqdAJpZ0o7z7H1s6BS7hrkWk9n-rwYVN1YNXsTk-GH1gv4hIElv0hLRsd-wa4YO_VakKFz45I2XeKVItBRNcfTShSfmy5c5d_IPFQCudC6I345GVD1BBuuk21ciyG5deR_1TexdDy7J9jjMRRMzDKLQTKqK_zrA7grIzd5vq-YHHuobXuv2NqlqjLmpSuO00kumPNHUAuKCyzWCvgA_fRrRXXIGHHlAAd1jBwouPFFxxV0YUiXai-TPnxhBu2UT6xtt_Ocmye__J291qpDVcTpqpEAtiappxO9cYdeTiSspmfuwOZGJxeNzukwbrvagpO4ZFhb-LmNyon8YdBX1-HYITffx4WFKQ1IbA-W_lqGsu9A_ZGQ2KPbMw4D1RU656jROt9Nu0PlZ7sSSekPwfaEpsoTLwbU6T7W5aZ71J3yfpjrhuw_dXKEzNo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇮🇷
شباهت گل‌های این فصل دو تیم به گل‌های به یاد ماندنی داربی‌های گذشته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/105362" target="_blank">📅 18:49 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105361">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MdICaVspJz0pJuSt-_lXaMH46ICIy1eRtjcVBHskwmBr44fIWmgXMvvolmpbCLGSbPwMr24-4Vymw_GfFPa92IiHYHK_k0jrwlG0tGaAcrysinfIrUF3_POq9aeyt0vMPrJlH-cc72lnx8vxSiM4Sf7FeNjFb0mQRDrsWBOygANgjhRqFaz3xv_2hd-m3kYyFwV8z4RdeHHubSkj7t0vVxdd6GJA8M4Gw3wsdC5iJ6hP0fiooHTtlIJ2izqPY3yLT5dFvKwKZe1-rch5sBtR8Opx850bA68OUJC_572Aj1lrDDzdh1lGl0P6iKmmC2E9uaNwFehKFVvyQ8jcWuQL-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🇮🇷
🇮🇷
لیست‌کامل بازی امشب دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/105361" target="_blank">📅 18:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105360">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=BjrOPPg3WMuZC7n9XoNLlEKm5MUtQFrTA0CDdnFcRBRnMlzOfLFVV5bwRrYP_9zmped5E4GGP3DxqTIcDoENz3FxYcNuSH44afBwmBjTAgdSRy3TdCgmyzTGylj5JFuVtt1Gz8n60Uhc_fPUY6Vk0Lwx0KV1vnAE50_RBF_WxHIuMdOeSUYNbkuHXJOG2tRDFoQnPDWgCJp6opSLjwvu9m7__udiL2R8q1tphh0Fo4KIlJVIp5zikG76M4kRYy4gsaC2RnyIsaEX6kB_f57mHJRteUIMW3OYO6D2l61naw6hxSU7oY4s0Linjyjh-nbIRFpxli4nOerR4KGUoRRM7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e961f8ed7f.mp4?token=BjrOPPg3WMuZC7n9XoNLlEKm5MUtQFrTA0CDdnFcRBRnMlzOfLFVV5bwRrYP_9zmped5E4GGP3DxqTIcDoENz3FxYcNuSH44afBwmBjTAgdSRy3TdCgmyzTGylj5JFuVtt1Gz8n60Uhc_fPUY6Vk0Lwx0KV1vnAE50_RBF_WxHIuMdOeSUYNbkuHXJOG2tRDFoQnPDWgCJp6opSLjwvu9m7__udiL2R8q1tphh0Fo4KIlJVIp5zikG76M4kRYy4gsaC2RnyIsaEX6kB_f57mHJRteUIMW3OYO6D2l61naw6hxSU7oY4s0Linjyjh-nbIRFpxli4nOerR4KGUoRRM7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
‼️
🇮🇷
🇮🇷
یاسر آسانی رو به هواداران پرسپولیس کری‌خوانی را آغاز کرد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105360" target="_blank">📅 18:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105359">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=Yol7NgM6wv6W0c2yuyrp9WWA_BQY0aK3QwgOas0pgG8qt4G2c3cYoON2MlzNWKwpGP084y_U5dGxKbTnEFGgl8tJIQAwhH9theHbcHShM1xcCRvU1Jr9j0KxQgi22tczAa-Vdm0wQCWUvI6VKseUpoeXtB3ahlKyIMYo-eW-Nt1P0uxDIGjMmkp0_EIBFP55wKi1o_b4r4p5z3-JRXnOp_hPERMK9wWMzvD4nMPHcgio6Cb7ZjfsuqscUr24P2_a6TDdtdF_pGOrJxlF2hnjkIZXe3hD4b62SByVjgCLin4Ah3xWSNMCXaI-t1wONs6VLOpphQ2tQmtCY6zI8cpyVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d420dd3220.mp4?token=Yol7NgM6wv6W0c2yuyrp9WWA_BQY0aK3QwgOas0pgG8qt4G2c3cYoON2MlzNWKwpGP084y_U5dGxKbTnEFGgl8tJIQAwhH9theHbcHShM1xcCRvU1Jr9j0KxQgi22tczAa-Vdm0wQCWUvI6VKseUpoeXtB3ahlKyIMYo-eW-Nt1P0uxDIGjMmkp0_EIBFP55wKi1o_b4r4p5z3-JRXnOp_hPERMK9wWMzvD4nMPHcgio6Cb7ZjfsuqscUr24P2_a6TDdtdF_pGOrJxlF2hnjkIZXe3hD4b62SByVjgCLin4Ah3xWSNMCXaI-t1wONs6VLOpphQ2tQmtCY6zI8cpyVIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
سیروس دین محمدی: قبلا اگر مساوی می شد حداقل ما همدیگر را در زمین می زدیم جذاب می شد
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/105359" target="_blank">📅 18:32 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105358">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if_5M0x9dD5muz43LlGJxE535o3uVrVNhf283hrZmLSdIgmIGCh_A6NEc0lI0Eb_0dnDb_Svak-NHlA8mP_yyCvhNH0M61Cstz55_L5PqdkvOMiqYES9_xKIx-FByxTCuF4Rm7ALlpv5t7fkU8i70HS0tZxj3EkDaQXtEro1v3uA6KyRXwQD4va3SCbYA-C2LmGYVJn7fkqDu5z4a2QomrS8_Ade0PZtVR4CPe5j0FxNx0OEYNpoQyGXL3EjdLGNlc7-NJRBrZYovLGA05Oz5y_qDO9pNdvlyfLm-i7EKmvuqPDsQS5HuUe5AFz-cfaFU2OQQY6vN0i-_a9J8yWq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
مقایسه نتایج سرخابی‌ها در دربی پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/105358" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105357">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/105357" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105357" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105356">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvDtcX6W_A9T-zRTU37BryHD4AXZVdmjtYC80MsXilEaDVoqP89kEfha_vcQ4nmmEQxg5e6-9xSMyU08GOJ0vInHFcpP_LtI5ojwEDTZXaln4p3uGea8zcL4A7VxeA4kCVF9qJdwHdoC4TVFajEIpQarU5uL9d3AtY4x-QsFMk2xvYI7OWLuo30EbDRy_icHkGDL3uQfP8c3nfKWPMvMWtCDBApUERwdQ2OeI82eW5-nXeXb4c7SVTcSQT5vpYiOjgdtDAyCZ9GYHByl0-3KOoMUqTgcfQD9Yzm5lt_saOd1kki9FCuChIsAnNv9VCIRyhLRgoJXoI9e_TlQXB2kzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
استقلال
🆚
پرسپولیس
⚽️
پیش‌بینی دربی رو در
TrexBet
از دست نده!
📉
نگاهی به 5 دربی اخیر:
2 برد پرسپولیس | 0 برد استقلال | 3 مساوی
4 گل پرسپولیس | 2 گل استقلال
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/105356" target="_blank">📅 18:27 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105355">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mse9pxR0VR1u0mYyiJJ6oSXchjhW5ctSmof9mRZmM9AqcD95BhQa7O9pscY5VPmUbCN1Z-wHrhAuV4zeXliI9AL06Cjz3u0Yyj0le-vVkOWTBhkJ2lctLJXw7OJbHGwxyxITd7S0Vagq1JSpGubFHxDmrqvkc05Cavy5tTXK18Su03QVm3-N5O4wm5DccBHVMA7WdoVg3f_0VtT49JwMT3eppANWFo1T_7pyfrgXO9R2vnwC54qqXPbVaWmldU0IJ1sfLUw5iaasrQJA36KY8hrsmW7OMPmumGr1xfn25hn_GliPZYW78pWoj4iKXwZbE7BMhAzqVL22wTPnMqG4xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/105355" target="_blank">📅 18:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105354">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMIAXLc4qjyeZe91RRSVEM5uhxFTBVtleoO2fvKs_vRiv8qt2jElG1kd0rdGYX0lxPlweilkHxggtr6zHeANWR-n_v2ShX870YdHRXQrD6YoCvLUEVqKC1RZaqvngzsEJ0PTbuAbHZ0MKUbGyhzPskEex5rnn9Kjkm0d5ZQHsubXWf0OGRaA_3DBm-WFv99-ThgwmeYRyDcEtmjXQYA8QsKmaEfPU6DSwHl-CsYVo94_BZ-_kp9SEr3FkNO8FOndcqT1Fbf9QAXc8knarqt70xoSTAnYSA3hgGcVF46AJRY2FgC54wNRETZV_lCOzg5Rir7nyzhIoThuV4vbUokRHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب پرسپولیس مقابل استقلال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/105354" target="_blank">📅 18:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105353">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I8yHt7vNrZKZN6nCHQFoMFWFq9bp4O4usk7IzU6eivu5HKRMNZjJcCsf3DPQd1Cuq4BVAb26RHkPhHmUrh4QaLadSiItOymRmBgCazvtyMVX1K7Xp5rumql7z3h5R6Lve3p0a7w5HpYps1TE20CXqdFZbreXgZtzid7Q0YwOxV9I4KrasWn6ou_hXfDL1dHSJTSxSp3CSGBdgyrw3XkeJGrgSYU_OtjyJ1UrfEj3Gu4z2knTnteQzhljPcybIWv5FPXZSTLC8cTLHBLuypX5VnNltiJm4fWzuEmzS5e36Tz7AaQA9vp-VCm3KTkU7qgpWryFc9dKCU1-9Fsk9-INeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/105353" target="_blank">📅 18:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105352">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CQmfDUMjbpviSz_ObESjxYkEqCK-V2WsOMu4-KniFysQy2FaCm5kQDGfO0i0M0d26nI9b793cpifBq51tZ6Ay9-Zzoh8aJjMuK2me1sRV_HFoTQjKCgMYiPw3jatA2rtyyk7Ed3PMFtCHlOYEoBBItVdhFmVknR0LHsUMlpLPdvPqCUw-SLwADx9xM6YHf9BWYH_gNHbfGfm2ZtysnDQOWGTP7yEp2ZjuL9zNeWVtHdWVPzyaU1n4uCtSyE4GG6vBorDKalAos_JVBQnofDmP8DzXjkUAnP3gk6aI3jD9Xopn8gSNB0YgaLQxn0Yt7fyVaNmuNrGOlwz9QsviF6VbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇮🇷
ترکیب استقلال مقابل پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/105352" target="_blank">📅 18:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105351">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=SxZvYjZKrYEg8aeHizLYJTfMtcXf-kb4gxeLSU8nJGEsnq-QxpyJbTdOIq0QrnN_Vhu3jZ6gNVFdtVmT9amsOqYhjgBNFiULBKfNPng70494qur5ex5G2p4guXmUeZiAw_3F6n1xQFTGf4s2wX3FYTWrTHEV3lDS_9BHx7SELoTFPswpBU3xvei2w61-eFnwQ0C7jUe3SPYlc0csarp9zFMYlq-UZJ3lixPvcBWwnUlqaHb4AKfYqJFZkHgdJZmL0m7VJWkBcKtZAMdp5hqw93G1VpvuXUetzOtZc4-fLP1LKc2QQ0HL5IV1LA5vIonpyRasCxKbjZtHHxWI5gA2CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4a83d7c6e.mp4?token=SxZvYjZKrYEg8aeHizLYJTfMtcXf-kb4gxeLSU8nJGEsnq-QxpyJbTdOIq0QrnN_Vhu3jZ6gNVFdtVmT9amsOqYhjgBNFiULBKfNPng70494qur5ex5G2p4guXmUeZiAw_3F6n1xQFTGf4s2wX3FYTWrTHEV3lDS_9BHx7SELoTFPswpBU3xvei2w61-eFnwQ0C7jUe3SPYlc0csarp9zFMYlq-UZJ3lixPvcBWwnUlqaHb4AKfYqJFZkHgdJZmL0m7VJWkBcKtZAMdp5hqw93G1VpvuXUetzOtZc4-fLP1LKc2QQ0HL5IV1LA5vIonpyRasCxKbjZtHHxWI5gA2CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
😳
ترمیم‌ناخن‌های علیپور در آستانه دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/105351" target="_blank">📅 18:12 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105350">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=CpDIQZ3pr6zYtnwv0LzR_-Q7h1_S4qJ8aZu63qVAm_3_5IbR5EWcojmI4p2-XkL--tcOtP9zvTOcG8WL3qgJ3z8yWV7jdxHRZRsuJCNZm9H4p-ivC33pFcmyj9OAg81qYXWiFw6PmWLLmgXs8PRj_SnVIwG-zYxUnYcIoQdqupyl5rWDSJ2foUDAvEIOxj6lIjxdp5KN26kPJ3YaX-5RjFZgzdu7Dn-xhh0eY7SkaCTtp3yZxqCFEju2-ejg3xt_yFAUhB2SbJyTdkHc09WIlPJgXXMWQhbdHf-1I_6UMdCc5hy3M8kGSY8h5VCfF7Y-jQFZ5gCwnCkuxvRaxuCRFmTmmOW5MNvGiXMLCR1UlAI-pM6MtEBguCz6DD6fHED9R2m7-j7H05X6Huvb2_GbPINXqEH0lCuMOnXh4gu1M9nS271Aq9CLTFY1cGTlp8Od-IrtKKIh0Sh62g6q9BYx4kW9Q0Qyy36pXKPqCs-CJhVECaW8FPW11wpeovyBP5fRhlbiMzg2JBK3AV8EVWj0u52NLnvCCADRUJGMoZEVDDlhgUebOtU9VmEupfceSvIisViMVzXWjrAj2Sk7RWunXGRimkX_bE6sBt7FTgicvXBKGLlE2t2Nnfh5Oc6G_a7yQoUa_Fc7_lU6NqSRVmToe0eYrogWWR8o_0iCrZoc0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9531a98f1.mp4?token=CpDIQZ3pr6zYtnwv0LzR_-Q7h1_S4qJ8aZu63qVAm_3_5IbR5EWcojmI4p2-XkL--tcOtP9zvTOcG8WL3qgJ3z8yWV7jdxHRZRsuJCNZm9H4p-ivC33pFcmyj9OAg81qYXWiFw6PmWLLmgXs8PRj_SnVIwG-zYxUnYcIoQdqupyl5rWDSJ2foUDAvEIOxj6lIjxdp5KN26kPJ3YaX-5RjFZgzdu7Dn-xhh0eY7SkaCTtp3yZxqCFEju2-ejg3xt_yFAUhB2SbJyTdkHc09WIlPJgXXMWQhbdHf-1I_6UMdCc5hy3M8kGSY8h5VCfF7Y-jQFZ5gCwnCkuxvRaxuCRFmTmmOW5MNvGiXMLCR1UlAI-pM6MtEBguCz6DD6fHED9R2m7-j7H05X6Huvb2_GbPINXqEH0lCuMOnXh4gu1M9nS271Aq9CLTFY1cGTlp8Od-IrtKKIh0Sh62g6q9BYx4kW9Q0Qyy36pXKPqCs-CJhVECaW8FPW11wpeovyBP5fRhlbiMzg2JBK3AV8EVWj0u52NLnvCCADRUJGMoZEVDDlhgUebOtU9VmEupfceSvIisViMVzXWjrAj2Sk7RWunXGRimkX_bE6sBt7FTgicvXBKGLlE2t2Nnfh5Oc6G_a7yQoUa_Fc7_lU6NqSRVmToe0eYrogWWR8o_0iCrZoc0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
کری‌خوانی بازیکن اسبق پرسپولیس برای امیرحسین صادقی: آخرین باری که استقلال دربی را برد، دلار ۴ هزار تومان بود!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/105350" target="_blank">📅 18:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105349">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=tz2Cdqw3Od6Ymj0cwJk1pp3aVVCyW0qNWI77MInITv751DpuFiaP6l6_PIP9bclqPebtrmW3LUUK8Y5Vgslt8exkIytWgPxzpWt-_NeRfscf9Q5Fy614qK2WM4iY5ghwsKVstNvbRy4jgw6kZRXinxaEhA_LmY9g3eiFbhsn7_7yjtcOl6uK-Wd0d1R5IldtKuC8zyO2E4pEGUC3tou_AJsNuQKbKJLINRQGnD09rq6f6Pn3VPQOoAqel_B80K-q0bPYnijhFBegBdn0KXCWAVpRzCVOdVfNd7IuGi96uOe3mmlNe41MRjbV5DogGuP7AWtHXbLD_mZK_kIFEWfzdC_A-ZWfPW3qHSK7i-ygEKMEwpV0T2FiVZzmra18qBCIF6PrSSGMlemGEhQZ4pHgztUUIhwrwm6VrstepnpoHxmrdJnQiVqgoV9uYk0zDrm6Y3tA95PzJGnWYrCK6iyHS18albVv9cNuOJm05fVagZ07pIo8vXDt_czgdFl2SRgOOJBBiQkTSPo1ytTyaW3wsBydhO-XOQARYkCesDRiubHcJ-DkR2IwzB503qi0HP64xgko6BuApTh7l0BlAo9wXY21wpTAhFCPgHaSUuaYK6NH_IThIHVEHc5uhqAkiVufeAVYJr0Z9u4xKnKJmKzZ1VMEwKsqNem2LcgRXlCK3no" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a801f0de.mp4?token=tz2Cdqw3Od6Ymj0cwJk1pp3aVVCyW0qNWI77MInITv751DpuFiaP6l6_PIP9bclqPebtrmW3LUUK8Y5Vgslt8exkIytWgPxzpWt-_NeRfscf9Q5Fy614qK2WM4iY5ghwsKVstNvbRy4jgw6kZRXinxaEhA_LmY9g3eiFbhsn7_7yjtcOl6uK-Wd0d1R5IldtKuC8zyO2E4pEGUC3tou_AJsNuQKbKJLINRQGnD09rq6f6Pn3VPQOoAqel_B80K-q0bPYnijhFBegBdn0KXCWAVpRzCVOdVfNd7IuGi96uOe3mmlNe41MRjbV5DogGuP7AWtHXbLD_mZK_kIFEWfzdC_A-ZWfPW3qHSK7i-ygEKMEwpV0T2FiVZzmra18qBCIF6PrSSGMlemGEhQZ4pHgztUUIhwrwm6VrstepnpoHxmrdJnQiVqgoV9uYk0zDrm6Y3tA95PzJGnWYrCK6iyHS18albVv9cNuOJm05fVagZ07pIo8vXDt_czgdFl2SRgOOJBBiQkTSPo1ytTyaW3wsBydhO-XOQARYkCesDRiubHcJ-DkR2IwzB503qi0HP64xgko6BuApTh7l0BlAo9wXY21wpTAhFCPgHaSUuaYK6NH_IThIHVEHc5uhqAkiVufeAVYJr0Z9u4xKnKJmKzZ1VMEwKsqNem2LcgRXlCK3no" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
هوادار پرسپولیسی خطاب به استقلال: دربی اصلی ما با پیکانه، شما ده سال مارو نبردید
!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105349" target="_blank">📅 17:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105348">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c2dc5b376.mp4?token=q4hnUw91OUXVWjvykDXaQwr14Y7kuvqhMgHwZzXUFNTNs8QklEnE8L4_KanzpRDNNglkEvLsjlQGSQpPYM3rK3rf1os539DImV5cFQGwBh6GvgM5yY9mFLozUd5wX9kTYW2u717YmQuckRdznrB0H-zEIsjNfvxTuHGrc0O_xjV9VRPod3QQAxVSm3B5LN8_FpzjAGzxLO1L0uUP__8TKOds_9wtBpky3QwlZNEisPwVDqiwRqBHpitm9T5WHLnEHFA4cRLWaxZ0Ft-REiGuNsOhqqLKxw63YSM35ptSrXjkURDQ0ImhvIprVJX9CXnxZUqtYxdOV5JFzt96vO1NDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c2dc5b376.mp4?token=q4hnUw91OUXVWjvykDXaQwr14Y7kuvqhMgHwZzXUFNTNs8QklEnE8L4_KanzpRDNNglkEvLsjlQGSQpPYM3rK3rf1os539DImV5cFQGwBh6GvgM5yY9mFLozUd5wX9kTYW2u717YmQuckRdznrB0H-zEIsjNfvxTuHGrc0O_xjV9VRPod3QQAxVSm3B5LN8_FpzjAGzxLO1L0uUP__8TKOds_9wtBpky3QwlZNEisPwVDqiwRqBHpitm9T5WHLnEHFA4cRLWaxZ0Ft-REiGuNsOhqqLKxw63YSM35ptSrXjkURDQ0ImhvIprVJX9CXnxZUqtYxdOV5JFzt96vO1NDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
کری‌خوانی هواداران کودک استقلال برای پرسپولیس: ما با پرسپولیس کری و دعوایی نداریم؛ پاس رفت آسیا قهرمان شد اما شما نشدید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/105348" target="_blank">📅 17:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105347">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4634665f37.mp4?token=Ypt8xhLYE6NDAk_b2j98Oxe0VElxQktWHPG4Zm2ZYEff2b9UI0JPlA02FGJnBF-D5Kj3BAN7eA9TFuATexg5SDEiSR7lz4uGnvohmoqRdlQLdPD8S6JaEqt0vqsqdoSAjUjSDPiUsm6P0-8VCs0eN1oN0j4fDx-sZBHJZA1dnwZ7sh8vHy7A7tqRTxj7iZBtKfCKQkGJDi1qXv1pKzbJ_pTCeiDUb0zlg_pKPBpUKaDwT946tghgWlH2jerOBzvT6mPQa18y-F1bVMDtTPAa7GvM1k3-ysrbZHn2DVl3bb3Bsl6c2fweN538Xor8uGsj5tmWymx_vTgLkK87YlKMmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4634665f37.mp4?token=Ypt8xhLYE6NDAk_b2j98Oxe0VElxQktWHPG4Zm2ZYEff2b9UI0JPlA02FGJnBF-D5Kj3BAN7eA9TFuATexg5SDEiSR7lz4uGnvohmoqRdlQLdPD8S6JaEqt0vqsqdoSAjUjSDPiUsm6P0-8VCs0eN1oN0j4fDx-sZBHJZA1dnwZ7sh8vHy7A7tqRTxj7iZBtKfCKQkGJDi1qXv1pKzbJ_pTCeiDUb0zlg_pKPBpUKaDwT946tghgWlH2jerOBzvT6mPQa18y-F1bVMDtTPAa7GvM1k3-ysrbZHn2DVl3bb3Bsl6c2fweN538Xor8uGsj5tmWymx_vTgLkK87YlKMmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
🔥
نمایی از ورزشگاه نقش‌جهان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/Futball180TV/105347" target="_blank">📅 17:52 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105346">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1699b2c157.mp4?token=FDvWnd_oDBm7oi1a07kvin3FaIm9LC5EFu6pP18HcsLcD4YGfuz2nGkkUvAgsblVE_EbsapTJRafVhcyBlt03EKqGyR46zVkPbDbNHlt7zhlqGnHiFLYUUCkICo7oi4tsDxLDc6SNEic5OvckytMC-1sGEIA4altKZsBqRBlNXXP6OkR48JskD1Em3yPiO835gjWTRz6dpowwZVeOeVJDMLtXqoQcmMB6iBXdj74PjDPBXynpAQulwq6lAym6WJRxG2-xyZMQfRl-o9S0kMWcHUcAcR7yP2PJ54lD0z_Y454XJIAmwZCrUz699aGwFyOrjnqP83KLMfAgc3J24cZnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1699b2c157.mp4?token=FDvWnd_oDBm7oi1a07kvin3FaIm9LC5EFu6pP18HcsLcD4YGfuz2nGkkUvAgsblVE_EbsapTJRafVhcyBlt03EKqGyR46zVkPbDbNHlt7zhlqGnHiFLYUUCkICo7oi4tsDxLDc6SNEic5OvckytMC-1sGEIA4altKZsBqRBlNXXP6OkR48JskD1Em3yPiO835gjWTRz6dpowwZVeOeVJDMLtXqoQcmMB6iBXdj74PjDPBXynpAQulwq6lAym6WJRxG2-xyZMQfRl-o9S0kMWcHUcAcR7yP2PJ54lD0z_Y454XJIAmwZCrUz699aGwFyOrjnqP83KLMfAgc3J24cZnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کری خوانی هواداران زن دو تیم پیش از دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105346" target="_blank">📅 17:33 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105345">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ef377348e.mp4?token=ip6AsO1gdTTeM3_HkWgeKxhYzp7ac9IdthlLF9mMhSHy1-Jc6pU4aeiAzC4MTbuqBv4tcfnTP9mvyjjuK1zQ46qf11F8TU7pFFR_9xXmSfGOlkMMgejaLykYdGO52yCo6xa-8dVuDvHd5CD_s3c_2GawFWjBu-kfst7daD-EqewClYuvesTDPwdW8YRXOi9cBHpMbbFFpqW_GWesAGeb86z8KDXydczygGDBJ9QicCreWBPq3KmwU-VN2Z3wDmqcTK7e4wZVGYOH9bmFiQAKGU46Og0T3e9Cixv87Ksc9UsnCZGbC6OMbO6bnRgXDUefLAxjiw5d99khadCb11RkpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ef377348e.mp4?token=ip6AsO1gdTTeM3_HkWgeKxhYzp7ac9IdthlLF9mMhSHy1-Jc6pU4aeiAzC4MTbuqBv4tcfnTP9mvyjjuK1zQ46qf11F8TU7pFFR_9xXmSfGOlkMMgejaLykYdGO52yCo6xa-8dVuDvHd5CD_s3c_2GawFWjBu-kfst7daD-EqewClYuvesTDPwdW8YRXOi9cBHpMbbFFpqW_GWesAGeb86z8KDXydczygGDBJ9QicCreWBPq3KmwU-VN2Z3wDmqcTK7e4wZVGYOH9bmFiQAKGU46Og0T3e9Cixv87Ksc9UsnCZGbC6OMbO6bnRgXDUefLAxjiw5d99khadCb11RkpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🔥
و بالاخره جانشینان رودری معرفی شدند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/105345" target="_blank">📅 16:55 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105344">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcaqSJp7SEX6Hkrlo8mvdb_nXsX5c0fWCeVzUhzQ333eNWPhHb2PMhoHJFQoCcqwLLhRNkkdQDhLYMoZtCE5glnKXvN_GQIwdJqWLHd415ReMTfW77UjAfpoROKeulSD0KmtK5RephhWo4-JGjQdgZy6DORGygCEwz-H0mac0tCb6pKEBsf6VDCMtFDYBSVjXyUsn3wQ4NG8x3fagJSG_Tdh2L2rbeQc-1k1hFgkpXmiFwKQvAU-GwLO08vE4UlGOnafs9N5FbAcq6cc9jYf3iIa8-ytwS76gTOl3yTSrZZ2FAf2MplMjQDT6NPREuiLu2eM5bwC0OKtQpmwdW8H7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🗞
رومانو: انزو فرناندز از چلسی به منچسترسیتی با رقم ۱۲۵ میلیون پوند
🤯
🤯
🤯
HERE WE GO
🔥
🔥
🔥
🔥
✅
✅
✅
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/105344" target="_blank">📅 16:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105343">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQzC1u-ZlyUxeK57UA2WucoQkgadymPkXkdI2arLpo0iDJ6dVz67A9Lsl_NebSYhU75kt51BiwVWIpD6txkSciteeMIzbqDILW-zWs37UTS-jZg1acvFYkvsIIDPKI7EzhuLfHLqvkwZ8Cbs6chjsyWuDienfIb6-HNZF-jWUjX_0O_I8TD9XhdARh6_yWX0m3tiNUizqYJ2Jyi9CgW80I-thAC7NINWXq01rn-GwmGP-zYzENRt6bc1sb8RKGjivH7WsOt7ki5evn24hjTWYZgKHGgWepe6BA3WTbVaNMS73nYSdH-gwmd6YSM29-wnMTW0M1bPDWoUPybLpKibqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
مقایسه سن ترکیب اصلی رئال و بارسا؛ تیم فلیک فقط یه بازیکن متولد دهه نود داره
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105343" target="_blank">📅 16:05 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105342">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=AV8FloMcGHTZy5ZT0LWcdKNUuH_dU6lqFRZ7O37M8z21wui4zs25dkR9eGx7WXYSUJGC5Y0woq88G9N1EaT4sKV1Dsv5lFFjgzAXoKZZ-P3iWudsMG5xDC2bAP0spAigVXHOFr3SAwBXNFs29fxuk5zkya9Xj9Wh5gQefhsM2Gx73u_022hZn_FZThNfofInhwxt8D8xEwocHGjuVDt5AxKXVuacYFoOcZRQZspg7yXjWYErFNSvrGTSR76ZhjrIJWSGuK2RQOdoCxiOX6RwvU2yxF9KwcqF9V5K3Tvw-VJBvQjyFm10OG-zHao3oFFkvAD1W1kl314TgsPRTeZkmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91b6a8d69.mp4?token=AV8FloMcGHTZy5ZT0LWcdKNUuH_dU6lqFRZ7O37M8z21wui4zs25dkR9eGx7WXYSUJGC5Y0woq88G9N1EaT4sKV1Dsv5lFFjgzAXoKZZ-P3iWudsMG5xDC2bAP0spAigVXHOFr3SAwBXNFs29fxuk5zkya9Xj9Wh5gQefhsM2Gx73u_022hZn_FZThNfofInhwxt8D8xEwocHGjuVDt5AxKXVuacYFoOcZRQZspg7yXjWYErFNSvrGTSR76ZhjrIJWSGuK2RQOdoCxiOX6RwvU2yxF9KwcqF9V5K3Tvw-VJBvQjyFm10OG-zHao3oFFkvAD1W1kl314TgsPRTeZkmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداحافظ لئو. خداحافظ تا تولد یک اعجوبه دیگر در آرژانتین.
🩵
🇦🇷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/105342" target="_blank">📅 15:40 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105341">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=E8r5RlJYaef2Xi2ur17h3RGJ5Tx00swioRDcvs3cCgjslEHqSl4sb_kKe-r4RYoPpzWJfHp9JKcKj92buUVG3YScCrVw_CRBPHChM5wDFrxkEk7wy08h3vCGJ4eaBs9ZEWNMXXtPJCHgCOCiHat6_jF0m5qvavnKT8hZ_1ZuGWnjJcf245h1imjFhWAtkm4dQrFJznW47SXhNFrXrnDV3-z9G3zxjZYIZp1XcoEwBOSCcQHYjNwWeW_h9--0Bu1O-2Zp13Hn3uF_b2o0lGdTA_CRwo3FlQo7_KCbH01QT5X13LzHEcnrRjd6fW4SgSexT-Y_BYytmLrdpS6Yupvmyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9af28d1f54.mp4?token=E8r5RlJYaef2Xi2ur17h3RGJ5Tx00swioRDcvs3cCgjslEHqSl4sb_kKe-r4RYoPpzWJfHp9JKcKj92buUVG3YScCrVw_CRBPHChM5wDFrxkEk7wy08h3vCGJ4eaBs9ZEWNMXXtPJCHgCOCiHat6_jF0m5qvavnKT8hZ_1ZuGWnjJcf245h1imjFhWAtkm4dQrFJznW47SXhNFrXrnDV3-z9G3zxjZYIZp1XcoEwBOSCcQHYjNwWeW_h9--0Bu1O-2Zp13Hn3uF_b2o0lGdTA_CRwo3FlQo7_KCbH01QT5X13LzHEcnrRjd6fW4SgSexT-Y_BYytmLrdpS6Yupvmyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
🇮🇷
🇮🇷
دربی فقط یک بازی نیست…
⚔️
یه حسه، یه خاطره‌ست، یه جنگ برای افتخاره.
🔥
۹۰ دقیقه‌ای که هیچ‌کس نمی‌تونه نسبت بهش بی‌تفاوت باشه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/105341" target="_blank">📅 15:15 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105340">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=iNGa1R1JavJn7Y9c-rVGQ2pgiUlYzX03ox-KyAxakzbSD-UfTKyUTZhRNPOVhORs3zrWTe83TQZhf8l1o0LdMsRWrJGrOeLS14GOU_6e0HBAklbZ8N8v23YRZletaGCMCxivo9rjM_fy8d1rHUWw0aON3rbD4twSlLubX7dVv2Kd2bP3nc3JoIeZ_fJTMkRWG97wcG4YllpW5ZczxuQq-pi1dcyvHhIOcuEh6hO_151pPHNSDHHrhTptlVUddCVRovkhW2I4zZA56MHYMXiccGWWtjY7KrDANzWUEif2-BkO272Hf4Tb7I6IZK9hPrPBLlYheRaVPyDA8RaJcBqhwEW8DkFb0WWpR9wRt-_aE34BIZmW-vpgTe-2oxSWN-XSuxkVdgpX410CSUi0KVDCMz82CL2Q5r41HixUJ2fA4X_MOshYYjQeHZQJLbPdzdPnJEkSaIx3RCcS4B-Dape52quxhI5E_38W5fhAY-ZDOm1Ja9X8JTFpRSkV8Pavm9L7YGzWthTkj16sQ6rwMTkmqP_665dkIBSYXA-xJ6JKlQLPpfcsXdO9aXPdxoEyMbSYBvb5f4BzvzmSGdU0Y1-qa7ea4EfosVVyFArcZ0UduqAIzOHmJMhpl3YPy-p6ZbFoTTZ7anKAiv5pyVpkgVqgVvhgcQD9_LbkkKedF2_Tb8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3a4e2ac35.mp4?token=iNGa1R1JavJn7Y9c-rVGQ2pgiUlYzX03ox-KyAxakzbSD-UfTKyUTZhRNPOVhORs3zrWTe83TQZhf8l1o0LdMsRWrJGrOeLS14GOU_6e0HBAklbZ8N8v23YRZletaGCMCxivo9rjM_fy8d1rHUWw0aON3rbD4twSlLubX7dVv2Kd2bP3nc3JoIeZ_fJTMkRWG97wcG4YllpW5ZczxuQq-pi1dcyvHhIOcuEh6hO_151pPHNSDHHrhTptlVUddCVRovkhW2I4zZA56MHYMXiccGWWtjY7KrDANzWUEif2-BkO272Hf4Tb7I6IZK9hPrPBLlYheRaVPyDA8RaJcBqhwEW8DkFb0WWpR9wRt-_aE34BIZmW-vpgTe-2oxSWN-XSuxkVdgpX410CSUi0KVDCMz82CL2Q5r41HixUJ2fA4X_MOshYYjQeHZQJLbPdzdPnJEkSaIx3RCcS4B-Dape52quxhI5E_38W5fhAY-ZDOm1Ja9X8JTFpRSkV8Pavm9L7YGzWthTkj16sQ6rwMTkmqP_665dkIBSYXA-xJ6JKlQLPpfcsXdO9aXPdxoEyMbSYBvb5f4BzvzmSGdU0Y1-qa7ea4EfosVVyFArcZ0UduqAIzOHmJMhpl3YPy-p6ZbFoTTZ7anKAiv5pyVpkgVqgVvhgcQD9_LbkkKedF2_Tb8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
▶️
🇮🇷
🇮🇷
سریع‌‌ترین گل‌های تاریخ دربی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105340" target="_blank">📅 14:50 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105339">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dw3Q1PEgQgL_bZTKFkdBVwlWGMK6zpuRFTn_gqt7MFDxsdHn8dNbUsHL4XswiNqYB0PwBkMTgQk2aM1-b1NRqn1kb8S548iVNJwleSTlQuh6LKf1NSBfKEAa7m8T_Dah6AbaW2GIm5gBzp1vvAcJ7F6KPsANHMdNrP4nshTFb3vm23EiizRaYTl2-GV-uQZYOUKDd9JNmnsXBDTrMRch2akOmgQ9wdPT6jAbul8vMwNYrpDZmu9rR4PnP5S_pOQlUHXbme1QskFZNF0HCY9-4bS1KGwQ8NtLU46w0pAI3zLQulzFZwb-znJkt2cWFR9MmXDZsaIMQJ6IP0N_WqZfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
💵
قیمت دلار تو دربی قبلی ۱۲۰ بود و الان در کمتر از یک سال رسید ۲۲۰؛ قدرت گنده‌گوز منطقه
🙏🏻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105339" target="_blank">📅 14:38 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105338">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=ZI14Xhlqln4klqnl6Rsp_S1FtXvxFXwyQx4qIvHqPNFtTb_wAm9HF8KFjYheoLi3hCdqDaU1NhyU-XJphh9IO3s5r9ia_drdTmolESF4SBYRJujRswNlupSamXsDJWzwLF9uPohDE7imGcrAFAu995LJevI98NoITBeTshS9ERGn60-n184SmjfgKeg-QeTohbqglqFiLXDhTdt3WZoJMAzEw6hiAKW12cN-EP5UC5Qeh2rLBaU_cuGY8dIH7EPYipJMyi-Qw_t8LLfWVMGCm3lt_KYdNYxPciTNzfUMrwBfZXAq0Z5fFTLrl8hS3tEOW_yPLJnxWYZWoKTwzZhJbYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8d7c8fe82.mp4?token=ZI14Xhlqln4klqnl6Rsp_S1FtXvxFXwyQx4qIvHqPNFtTb_wAm9HF8KFjYheoLi3hCdqDaU1NhyU-XJphh9IO3s5r9ia_drdTmolESF4SBYRJujRswNlupSamXsDJWzwLF9uPohDE7imGcrAFAu995LJevI98NoITBeTshS9ERGn60-n184SmjfgKeg-QeTohbqglqFiLXDhTdt3WZoJMAzEw6hiAKW12cN-EP5UC5Qeh2rLBaU_cuGY8dIH7EPYipJMyi-Qw_t8LLfWVMGCm3lt_KYdNYxPciTNzfUMrwBfZXAq0Z5fFTLrl8hS3tEOW_yPLJnxWYZWoKTwzZhJbYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
🇮🇷
زنده از ورزشگاه نقش‌جهان در فاصله ۵ ساعت تا دربی حساس پایتخت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/105338" target="_blank">📅 14:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105337">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
بهترین گلهای استقلال در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105337" target="_blank">📅 14:25 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105336">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🇮🇷
بهترین گلهای پرسپولیس در دربی‌های لیگ برتری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/105336" target="_blank">📅 14:01 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105335">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IjF2OyUeeuL8SVonFXU7BVlkQgKoHKn_QKKAX96Rdtdau06croyNSAaByfHj1uH9gHgPIIt6Jy0_rI5spewMSyAxEO5gEPI2UUnZLHDjFkYa7LZ088B0un3vu8Sww5RnAxCArf5le-nV-Ks2NegNJVlhoGSLWi92njlR2nW_gckxONILENXh5_JhWsSIgJ-LxulWBdP_fqwcZiTasEwXTpdVWXmkQJWQ1izKT0c0Qsi1T9K-v0ngSsV5SbSHSSVERkTHC5xmKRIaPso9ephiLrgMrWMnHo__5F4HFuQlzh6yUp_xc3R1WXuKhZOLkrzojysOOFmcK91y2fV0JgeMDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😳
💵
خارکسده
افسار پاره کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/105335" target="_blank">📅 13:44 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-105334">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGOVI4EKElXZAIbLNZ0BwVeBEynG1KR5uGrSKevpFvMKqQndA1rNy78qITCbWW41E4ohlC-vSt3qTK8CIdKSva3wxogpoi96lSe0_sbNqq-lnyagh-ghvFO_DlVwZ9SbLbu7ElJzlx5gMuMkbuEyJ18Lm8xl1RqyYILyE3IRGP0C0V26G9oOpFNVl8W9QP0xTqiZoP_jE46Vvp-SahCBeNUQPhKyRmIXcEfygAm8QfLzoHJ3ps3QqG5Znb8qzFOrj234kxyxtIqrY54HBqd_wnBerFk2VBhxyd6AEdZ1vP_6nZAL0rMOe_-zHhdh-zkgjg9cpx7_zOvpvw559-at0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤯
مسیر‌ فوتبالی عجیب‌وغریب آلوارو موراتا!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/105334" target="_blank">📅 13:35 · 11 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
