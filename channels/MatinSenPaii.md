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
<img src="https://cdn1.telesco.pe/file/pINAfCe3NJcSmRidlr5iBT3tJ1zi0E-RB9SCQRQcITzTzddPoDh1ZRodv_RQR_dnrH84ZqnBZpd7BVEoa-Qpewjtv6Uhdcpt27jgHlEN1a_5a2Hcm9r_1aZbLl-4sGybDO0h1rXNeu2kWJ2tKkV1ngMIuMrzk_Az7MO-obVLQhH68S2XKOVMohSSN1TlI4XTIThcbFJ7Zj-2d40-rsJwP18PMFQ0OSVCkkCnn1mc8A9tSR88UZaTOmSnF7Gf3RRpLw8CNXpBJ4c4YfoSOasz7tBaZHQzkcyjN8e3nWVGpkziRsBiPxoLVPzLF5widU6nWD8A_GGYFvHl69oT0G8M3w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Matin SenPai</h1>
<p>@MatinSenPaii • 👥 155K عضو</p>
<a href="https://t.me/MatinSenPaii" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 متین هستم و کامپیوتر رو دوست دارم! در حال یادگیری هستم و چیزهایی که یاد میگیرم رو سعی میکنم به شما هم یاد بدم اگر به دردتون بخوره=)•YouTube:http://www.youtube.com/@Matin_SenPai•Github:https://github.com/MatinSenPai</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-12 23:28:45</div>
<hr>

<div class="tg-post" id="msg-5170">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RfdbCUvI5jkAnlFnvoiram3ZrNsc6jtQhlzUzGMhAR2GJXYvJNru4oD5_hveNyy3Hnp0g8f7GLBzah6Wx-X4Z9P7JsQhoUhRDwaZzvX4g3ipkpVZLsFp2bOFnGMn0v76frOzsc_V8vj-C0UJbYFtm6jT8FkfIGPj7HYLKN1tNME_V2Q4XfTEXWea7sZuuQSZFps0a2QbMuewbonhovrE-V39szfnBgRzS5QPQrJ_LME0rY18nf5_tp6nuXcIQkIe-1njXFWnbl2rwFjmeqdcViKdNCzGCSOWdkpHJoSqMOeHwzqORRnv8VA09y5Ix8v71TeyWGa2jA8JZZ43_MRkNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دارم با همین Nara و مدل Muse Spark 1.3 یه سری تسک سرچ متوسط انجام میدم(سه تا ساب‌ایجنت ران کرده که قیمت اجاره و... رو توی سه تا شهر مختلف برام در بیاره و اونایی که ارزش بیشتری دارن رو از دیوار و شیپور و اینها لیست کنه) با هرمس، چیزی که چشممو گرفته سرعتشه که…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/MatinSenPaii/5170" target="_blank">📅 23:07 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5169">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FHGDGlp2bkSrXtdJkTjogdIDJMCvmxD756XwGUAIpLlDkn7UURHDZc3f0sXd9uKb1iugk0rl-JMGcQ7wr2tsP0joXXZNHu3V-8YPaFAOhGx6lhyOBrzX6Ug09OzT403TRYnUIZdYSDxalMw5L-hWIR0dRCPzp54z0GGolr25o10vTvBvo2INSIDQ9jvo_vh0JHfKK_vbquQRW0x6w2knCoqjSYhEfJJZsaLNaQTJ3cDsZXXIBudJbNF_UzNTjE41faBVcqSfnKY4b1g133vUg_pCTvAD_eyefbNpW-hWXChMDAuKTo9nNZS06p1k7SVvVXFiTl7MmLxottEVsxzB4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جمنای هم تخفیف زده روی پلن‌هاش
می‌تونید خریداری کنید ولی حتما از اندروید + این متد که اینجا توضیح دادم:
https://t.me/MatinSenPaii/5092
استفاده کنید سر Google Pay</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/MatinSenPaii/5169" target="_blank">📅 22:41 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5168">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KpBZyx2rY4ElA8xjM1pGhm6yrgNSBKYBBQS0jFSJTRioGxXVV2KbKE-lwtt2mcsVb9lZ5UiyWWIQJhxD4mGvxTfVBre0yK-9QB_UdZOBBqOu2dBLSwgEf_QlvS1njRDKdk7rwfV-E-jx9WoFYnVF9OYsvS9zhM0cb-1Z0oXrjfQhn9DWq_phuzhByhI09Wgxv_BHVbhltChlSp04uWobLl5vSyF7V5yXn5dpM8xXIHls3sFy_k1uR4YY8cffk6gxO0xzvpN578nyCJT3gTZvFde9TCzjty1i8icy5s_uK39M6qMN25-JH33v4nHFLpduYxp7BYX21NTw8bfhSegkwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان با این سایت Nara که قبلا معرفی کرده بودم(https://t.me/MatinSenPaii/4061)، اگر که داخلش اکانت تلگرامتون رو وصل کنید به رباتش و توی کانالشون جوین بشید، می‌تونید نامحدود از مدل muse-spark-1.2-contributor-free متا استفاده کنید؛ بدون محدودیت ریجن و...  مینویسه…</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/MatinSenPaii/5168" target="_blank">📅 22:01 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5164">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UC0tllpU9e2Ot6lVDRLDUkYpP8TNIdXCAg5KF_P2x8Lo2ZLC2h9MnfS3-6SD7bXAhZ29beRy7zWpfEKK8jac0c6OFCxDFEYmuchq3kcupddkCPJHTdZUvp97gQGHn2frSMr5E7jf9tAzC99Lm-D0CRZG4T0pLKUCmOMjyxREWrGP34UBmut_5N0tE4jZCD56qkFIhrQcaRpZ3HVOQrvb78RrbL3zoiXofFh7pDOQHoCsdMVCImgttFVxSIve6-mWFWD_sOKxEn8RejlUCOV6yZ6uLlkY0F3eYssUYPwMlxuZpg28y9vl2eAwhCxFkkvDvBhzNPKklXhohfeFweAt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VrHVJlgal-1x0Dade3jNoWDa2PM9wc5Tto4Fv7lILvN6PntkR2cuC70ueqB77OGx1QxfDRjd5efsbplXu0vlQ0B6doc18EV91R5XoDZu_-zZxZ7VAI9_bS5xlKIPAdAfFa1ku3APSCQzCrYHuUqYTEe85u8ar1MV9T7qLimPin3UFGHZTb0kZp2Ot94usHIXPVWjekkKofxY3iBnvCmM-i3ZaceNv26c5eFxgJq8ynPbI9zG3amu4b6HVMCE1OlSt78thSo8FLx_EUJh7n3RC_PPs37d66EkA7ofV_vmmuke205KnRisZjJexP4qLck4lpqbplQu1vCMm9kqMyZ6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Ga8dxo0hRUtqErKCn_0v2qmB93j-mylLf1hCKK6io4MMrj-9c3Vwxr-eZ654-Qsg-bGZ4UwNrmaWjuzkk14TX13OXZOas5a3CauUKrF4WYzsf5qI_meBfbEVHZ7dIIKBqva5oeP1jRd1y7eoxjGWokbMpemOSfN_cemv1gZ4xcqlIw3ulZh2ZxM56nnf8VTCOuGDmP_F8iF4MxcUCRzhHp9Y2U4EziAenHvqGxlT9BicpoUUTy_nRcKirNb3G5NyirEt9nWmJIVlWCdqVC70k4PM0u7tVF8rsc9deyUjund8MenBLssyYDuctZ942ySbbvABuf0Wf0KMXQRCc1nyUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Kc0Ah0h0I6_nesWoI2pN9eYEL21Ulq6CVHZcpJ1x_3dqXEXPnLSGKg5FGYICsVrPlb4kT5HAMMtUooHKzj2sllo-2QLkURyXzDjiR7k44R139MvkBV2W7jHjml4hQ7syH-7BngYCQCp1PJmfPTZTXFfc3suVB8wQaVNzS4UjjPfnNeT2Ycn5ao7LF43W6cxo-A0Xzbnq66OJdx9sb7n8fCgW3oVTz3f9g7y-gc5WYWM0hMtz6HuuJJdffQEi5jwqs2hhOEHU_O_bGzQbQSk-XcncSVIHOAeRaWat497VRiMU4KKh3-JZEvcIQN_3sS_r3RCG-qhKIzEtCKe5Maiffg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایت Nara Router که ریک معرفی کرد دارم استفاده می‌کنم برای ‌Hermes و چیز خیلی خوبیه! یه ربات خیلی کوچولو هم دارم می‌نویسم. دارم تمرکز می‌کنم روی این قضیه ببینم چطوری می‌تونم کارهای روزمره رو Automate کنم و چطوری میشه حداکثر بهره‌وری رو داشت از Hermes  خوبی…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/MatinSenPaii/5164" target="_blank">📅 21:43 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5163">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">نمیدونم چرا انقدر از مدل Kimi 3 خوشم میاد
زیاد هم فرصت نشده استفاده کنم توی تسک‌های سنگین
اما در نهایت برای کدنویسی، compatibility ای که مدلهای کلاد با خود هارنس claude code دارن رو هنوز توی هیچ ابزار دیگه‌ای تجربه نکردم</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/MatinSenPaii/5163" target="_blank">📅 19:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5162">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/m9nuLh_gPIDEY-aQRwMm5EZDvFvJl0yMScY5PPGo-Nw9dJtAQToFWGJvtucglj4H4PjDZbCQRVtlO4Td6RvLqSR7A5VzP_ynzOBXFkYwHH9JYMUCvfNtx6Mw6S8ObPOc49P5miN6STQM4pKmhV78pvCdvvh2v-_z40C4z_XJFH8LXjRiS1__R-yYLcCRTuYu1sV12YgAp6mwsoBkqXpkXVLDMIa2FBOuL_2bbxU2FU9xsqCzWugYcRT9uuQS9QoMyfqI1TxPpR84fm-hAMQ6FytBFGrpTAdPxKWhsspqF3_gf9LtDX0c7VW2gdC7QRZqtkdHc4gL6B7Tp2s8AZfPhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل Muse Spark 1.3 توی OpenCode رایگان شده اینم آموزش استفاده‌اش</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/MatinSenPaii/5162" target="_blank">📅 19:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5161">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A_e06xT4xE_JyNedRfS-PskHrWuuko0dcCDNIGJlkpLEq41jJ6ALe20j5lNHNUfV48pCjDSllvIlIYSQyZSStLD0d2rIuAA1aKpKrnviRjm59V_O-pNomHj9YhJq91cJO9uBb3R0eq00qWUjx3TscdgFb9J9FUfGgCq9GsrPkXmM8pcAkdhY6VvSED0ONqyRlIxBO_m9x5tZmeywsYZPtK6pUt01HCmuTM8vlC1nh76XwS90_OEkWr8ia3_D2Vv3v37vSBPmBgw2oNqAhUIAjrpJXSlb8oCi2d2a0QOKH_eEX7A_l5Fijab6xFq5E92M76uuDqijlr4w-wUpnN3tYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هم بنچمارک Fable 5.1
البته با هزینه‌ی سرسام‌آور
10/50/0.25
In/Out/Cache
که خب با Fable 5 یکسانه، اما با پرامپت یکسان توکن بیشترس میخوره(و هزینه‌ی بیشتر طبیعتا)</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/MatinSenPaii/5161" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5160">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ces-zIFM96dYAVVTSL8zgZkiWc7_w8RiYLQNiJzCGS9kp6vEF1d-4vTBSh4zdPr510zGCe0WouI92cCM6WLhwZSGuUCBZFZ9n3aQyWBUDXwbAnq8EydJBTrMbEgQNT8DPh95jYC9uZz6MdRxSC5KQeQC0ExS8RigxA3zb1_MfrHdA1N3u2vjyRbnyzXzmPKS3m3vmpUHubiIXpfS7Qr6CLTcFUXAn8uLc6GYjyeI6XXolitub44LQwww5dNgUCrBf4yDq_sF8fIlYbUa3y6YFy_ETcwEFUgDIGhnT9Qbnqw0N8x22LW_s-O04Dvw0gAFLY6b_C-gSb8Z3yZTE8KaiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا مگه میشه مگه داریم اصلا  حس میکنم خیلی اغراق و بزرگنمایی داره. امکان نداره قدرتش از Opus 5 انقدر بالاتر باشه توی این بنچمارک‌ها:) باید تست کنیم</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/MatinSenPaii/5160" target="_blank">📅 16:30 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5159">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">کار کردن با مدل Fable 5.1 به قدری گرونه که می‌ترسم بهش سلام کنم لیمیت هفتگیم تموم بشه</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/MatinSenPaii/5159" target="_blank">📅 15:21 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5158">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/MatinSenPaii/5158" target="_blank">📅 12:51 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5155">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/q0gQXJ4_B7GMl-DZMp9nHhhuOrSRCEdzgj-As4wHP43GpO2WaczHcdjhwGhXrfkrn9-8LmXnlUtaIvNhw-7KsmMLFpAO-IqAT8oKUiWRc2UFZyk27vuy_LftcCCK1IrZ4qf0cfe1HUr73HX64iBQf890jucBeAvwSZyH9Tl47I6L7nNB9XxSxAE6wZ52gSaZiPwDniEYu7nweTqBu2GrEuQgfP_m9NgDbjlb1ghyPZ72PVhiG-u4TKX5oqgzOEjuuDEn-vrk1jgPKoU_YrDOJFtPlnO2Yl87Pfnk7t9eQ3XPRj9_IRxHiWb3PkncEfnKyAh_ZSVSHdy1NbaQPKHWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ReyvfLWhJaeba2mHVQzubRMYPa8xTwDHSQMU2dWmWR0AKr696CswvfSJ65XIB537bAZUJ5KDe2Jl1AvIqLYuSDFlCZpqPxF343gw696ulzq_IaIeX8I39UlHIcQqrfPBMYufz378HDtoS918DFyLIrdA7o3B4P-mE7xN_51-XkOlUKKB-3yW_Jmmk3eGC5JZujE3QpSKKhZrt2Im9KmRjgST3L7kMmv8hKcGp0ozM9EV4UY9RD85x0UaUp41sy_h9fBjXwfM6u28Urj3d8_mEnTHiovWssSWOfotSTEZhuoRX3yBDpkvbVEVM1Cxr3d9B1E4u2q1EGfazIhnFKsvPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SJeG4P-Vr-BFB1uXMfL2w1fQL60VXz1HjTaDOCiq3vM7ezQhzL7t_OY25-d5EKZzjSVOWyG0zRSEm5qvkWeXr__Jc2-VWev6jxPMP_kagA13ekTu8T9xklmKyNL6fELE5DKBvLM5P2Q8lqg4r9fNH2MO-qFeK_m1k9T0ubbpcv1C0CvOIRYX7hFflq5aBYZMxnzBYEQLa4Hn6SoGAxd6C0gEakce7dtSuzYFAswEZd_Zfc9WFqTced1idJiNUVE7R18tu_DLq54C15tGSE4noUrPzXQDu6hrEh50B-wMO7_WxiTffw0clk2zdfTmUX8mp6Iq1HFm4l9rnCHlbAiiRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم هم Gemini flash 3.8  فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5155" target="_blank">📅 06:22 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5154">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">امروز هم Muse spark 1.3 رو داشتیم
هم Gemini flash 3.8
فکر کنم گوگل از جمنای pro 3.5 کلا بپره بره روی 4 مستقیم با این وضعیت</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5154" target="_blank">📅 01:35 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5153">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-text">🔭
اگر نمی‌دونید Connection Chain چیه و چطور باید در WhiteVPN ازش استفاده کنید، توی این ویدیوی کوتاه قدم‌به‌قدم با هم یک زنجیره اتصال می‌سازیم.
📱
دانلود آخرین نسخه از گیتهاب</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/MatinSenPaii/5153" target="_blank">📅 22:02 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5152">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سعی می‌کنم آفر و... خوبی اگر باز دیدم که بتونید با این ویزاکارته بگیرید، بذارم واستون</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/MatinSenPaii/5152" target="_blank">📅 17:37 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5151">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud  این سرویس Free Tier دائمی داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)  و همینطور با این کردیت می‌تونید دسترسی…</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/MatinSenPaii/5151" target="_blank">📅 17:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5150">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">💸
دلار فردایی تهران
💵
220,300 خـرید
💸</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5150" target="_blank">📅 14:06 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5149">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/hQuzOXmclr1Ra1x9CVSi3F8AFHSzAV8xS3KeB6gxpra1jLMXykAz0kLL5eI8Ti2KHuj_D2WIz_UTv09pOyUgfBrlRCkJqSSb88WnYUZud5GcjISox35RASeM556ACpg4zKGwGxSoWXsksuqRR_IbJ6Z-1w_FXFO_H3lAKJZJzMdNM7xJsvCPpYnDJuYCNCjwDjSQvhtGIHh53cINxhNRr2JCx_rVwkDnclBQ5qMXRkDfagTz9M33Q5QX_Xhlivgq06iDCbHkd_aYuk8cvofKqeVz2g_YHpzGAIj1n7j5yoJAfvD_AdAIXnGo8AwYJviucLefpWIegWuidspPtjSZww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش گرفتن 300 دلار کردیت رایگان Google Cloud
این سرویس
Free Tier دائمی
داره. یعنی حتی بعد از تموم شدن کردیت، یه سری سرویس‌ها همیشه رایگان می‌مونن (مثلاً هر ماه یه سرور مجازی کوچیک e2-micro به‌صورت دائمی و رایگان)
و همینطور با این کردیت می‌تونید دسترسی به
بیشتر از ۲۰ محصول
محبوب مثل Compute Engine، BigQuery، Cloud Run و APIهای AI گوگل داشته باشید.
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://cloud.google.com/free
بشید و روی Start free بزنید
3- این قدم رو من حقیقتا چون واسه‌ی خودم جواب داده میگم. میتونید بدون این هم امتحان کنید. ابتدا از
https://policies.google.com/country-association-form
درخواست تغییر ریجنتون به امریکا رو ثبت کنید
4- تایید که شد، توی سایت آفر گوگل کلاد، ثبت نام کنید با یه آدرس فیک امریکا از
fakexy.com
5- دقت کنید که برای این کردیت باید حدود 10 یورو موجودی داشته باشید. و این برای من کم شد و در عوض 257 یورو(معادل 300 دلار) حسابم رو شارژ کرد. برای یه سری دوستان یه دلار خواسته بود و نمیدونم داستان چیه
6- من تونستم بگیرم و تا الان هم مشکلی نداشته. دقت کنید من تمام مراحل رو با یه آیپی ثابت امریکا رفتم و لوکیشنم رو هم امریکا زدم با ادرس و همه چیز، تهشم با گوگل پی پرداخت کردم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/MatinSenPaii/5149" target="_blank">📅 13:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5148">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GWxWpqLVRJ_bx7IbPdVL2AHuxf9ibugY8Z2fszoIpgA2bI-udyFMZLoQs2nCSqAthFfUHrP3Ov9MB-cP56My5wBab_O-VzovQiIW-jaG7Lhyo8EqryVrTkTlSILv-T907CDoSEHSr97RGoEn6_YJS00rI4zpg-h62ODIaCCOiMn67CQraNf5TTEWZVaIOXkmFcdNoleDaLObZXlmohZY_zzUIvUc8Du9htzQnef336Oo7vZJ4iMWogDIg6g3c8JHmvj66MY5HMEgbxXMkhhPTHC6Ha3VOrE-fyQX7_eKJaErf6GXpqVFJvTwPA-DQRmySEbUupiLqEbmqle3b7OSqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب بچه‌ها من وظیفه‌ی خودم دونستم که همه‌ی 210 تا کامنت رو جواب بدم. مخصوصا چون سر و کارش با جیب شما بود توی این شرایط داغون.
و الان تموم شد دیگه
لطفا قبل از پرسیدن سؤال جدید کامنت های دوستانمون رو بخونید</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/MatinSenPaii/5148" target="_blank">📅 13:30 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5147">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">و گویا از apple pay ساپورت نمیکنه. فقط Google pay</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5147" target="_blank">📅 13:22 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5146">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oTFDZBIYBVVe5SVMkT3gvcOY1j3IYY2N7rgPEXqoiRU5B69lF19--J-a1kseL_e6xuPpZimnY4WuereH_eoJaaoU1-qzqMuT-RqfZPwA7MGNcJ5rxpKHhE_sCIJlqqg_LrfvS-5uJf1ni8KcuLxFiHEcOZdPVoXGkTHQik08rlG49Clg4ZXLxCuwDNzaR8IdBQFAiF5XgXlD6RlvZ9tjzQzMg7WtBL-J1bPicKMiurGn6DMhklAeu5BfM8-tG4Hl_tYdOHI9SDE7amvc0lzb8ADvt7-rO7mToNxF0jFUYbwJP3rQ2ScBYtCd1Lonu3zuQYDHV-1LSB7XwN3tT3KS3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بچه‌ها هم تونسته بود با گوگل پی+اندروید
اشتراک Claudeاش رو تمدید کنه با
Mpay</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5146" target="_blank">📅 13:21 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5145">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ObB0s1om3hnfE30ymNFPL9ZW1Go1ezPqa7nLPcOGzxAPAq4dZ9DpK-HQ5HtCwjT95eK6oyYDYgy6Hb2kIACwLkb2cpaW-l9Op8JLm2ap3nmAQGPZA8G2FGKHVaPsozpEXQDAgsBICb4-tdr6zL086vE7UzXhK_oiDwMPutTfdCDmuBMdfZ1kEQhy7iNPB_OJoujQuoXqvMC04cCEqJija39TSTO-47nP2AGzWBP57m2ur-eezkV2xw6bappcIGVcZ-mcI3NDRWqaCGM_ulJnZ6sWpAGvOJ0JH0KWYAvlfJMXEJ0EykZMEMKQB88RjrgAngK1XFXOq8TeeaPtTe_8Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازم مشکلی که خیلی از دوستان داشتن</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5145" target="_blank">📅 12:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5144">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">و دوستان، با این کارت نمی‌تونید کریپتو بخرید. هرجایی بخواید کریپتو بگیرید نیاز به احراز هویت سفت و سخت داره
راه درست و خوبی برای نقد کردن پول توی کارت ندیدم من</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/MatinSenPaii/5144" target="_blank">📅 12:42 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5143">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/pcTh788CwC8ic6oe1S6uJHbypCSeI15HRM_wEcJxfKZ3TdIw4z2qHa9cVstoTuoi81ZcgGlgFTKnJqCVesYxpVNTxu8UcL_5qX14dXMgqlYgdkrr8ttrvIXZOS3-0cBGnK6V9G_3NbcWuhoKphgjZXIumWhqJRDNmd3HFEx8jheM4R56hxoaBSIbIOGjQ12EoXMk0qOLFd6MJ-8CJGcynJo9uxVPmGf-pD5LLC1fR66PiaEa1tNxlnmJ6U2wGhCeA7-AmquTThwEjofY7JYsnUeo8f3eudTTnXbMICEr8nPILfqFC7VXm5Ky737mTj5FmOgYG7i4OBi3T_LPmeZChQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نشستم دارم به کامنت‌های این ویدئو جواب میدم و دیدم ای داد بیداد:)
هیچکس نه دیسکریپشن رو خونده نه کامنت پین رو نه تلگرام
متاسفانه تغییری که سایت Mpay داشت این بودش که دیگه با پنج دلار و ساخت کارت، اطلاعات رو نشون نمیده. و من هر طور تونستم این قضیه رو اطلاع‌رسانی کردم
برای دیدن اطلاعات کارته باید ۲۵ دلار رو واریز داشته باشید و گویا این قانون رو برای جلوگیری از سواستفاده و سیاست‌هاشون گذاشتن
من سعی می‌کنم به تمام ۲۰۰-۳۰۰ کامنت جواب بدم که هیچ ابهامی نمونه.
این Ai جالب یوتوب هم که دورش خط کشیدم خیلی به درد بخوره</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5143" target="_blank">📅 12:41 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5142">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5142" target="_blank">📅 09:57 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5141">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">چشم روی هم می‌ذاریم دلار ۱۰ هزار رفته روش</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/MatinSenPaii/5141" target="_blank">📅 09:31 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5140">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">بچه‌ها من می‌خواستم آموزش کردیت ۳۰۰ دلاری Google Cloud و پلن Always free اش رو هم بذارم اما واقعا خسته‌ام. فردا می‌نویسمش واسه‌تون.
اوراکل متأسفانه خودم موفق نشدم؛ به شدت گیره روی آدرس و آیپی و...
اگر موفق شدم روی لوکیشن خاصی، بهتون میگم</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5140" target="_blank">📅 23:53 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5139">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/DXeTqtQpZM_2aNEgvb1nj1dVUgjih0wOZ9xZhTg9ZEWxzjf2u4rzieMUAUwc-xHzYtC4bMFG1at-4XvaiS50ZHE7KiF2Z03lMYwlH4qixFpRMoTA0FTAZ1dUvd9emJMnOg6VAKmCxBs8BUTg1vE3crQta0YCQsgWZsIxBFRs6iUI1kBFlLOHnnl0wkadVJIw4BxNmGxZf9l2azgQIUNFIoGV545QjBzLu6w9BjPQef311j1j1dbEYw0h1__l0a1C_CtmF0qU8ShzLlq-G8xkzpmfgz1rwtBcDdY7vF88VvF3hE_wTGI0ZNSPVrKPNIDTUVNj_0jSBn-qeqokJEiqLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجربیات خوب یکی از دوستان واسه‌ی استفاده از آمازون</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/MatinSenPaii/5139" target="_blank">📅 11:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5138">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وی پی ان رو ساختم. باید از بخش Networking، پورت ها رو اجازه بدید استفاده کنه. بعدشم پنل سنایی نصب کردم و یه اینباند TCP+Reality ساختم به راحتی هم مستقیم کانکت میشه بدون تانل، لوکیشن آمریکا</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5138" target="_blank">📅 11:24 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5137">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gyRretu8sNtXTak-yP1yvJBTdRuyJnxfbCFQ3KQWPdWeRXLvneQEaB6mkk9_qasqfrrGMtnH4v2MN_JB_YgOk195lLDfwBc3_ftB8D775fYK1r5qCLyoTirEZJ9I3FnT1EabrjBarLMsTEzBLgXDmFvQCIMdFq2IrbPrBspb_wCNrvUkNuUcjjRuIGI3FzXKzH-izS6gzHIm5CBkWI8a_y-hW_lSbj6INzshiOXT_RuBWtzu6CGC8fDA2oThaWbnx84wasKPMwxqvjBcEKdwVomOWbso-EXvhAhFww2T6qdBm1lG69xML33lHc_sJ1GCdUfl5-tnGrNHy23EzZy4hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5137" target="_blank">📅 11:20 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5136">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qlVkWuPEnNEhhGWBO7m6KHDnuR75CZ-IAlOnPx6HMeVRWEpT96mYVBA4D9u3MUPT-BwiesOs9ca04Whn-Q2MyC_HJcIRqPNcBjjLxXyV8bCsPU5oXiv5I7GqxH5m-yhcVQTFhSDMCvsLM4Vst6jJlBMA7PLaJcOOIaOU7W0dBsZUiVgBftsgekHRO4M-Qlj7AVNo93wlpGX4U8hZex7qVYwfmN60ZjvFWC3M9Btefp8S0khNmEzGZbUKYkZiCK_cxK0C_TU-e8Te17q5bu6w06vgVaWHlUlPeklKmgwALUKfJpt6UNbxXJBU8kISKCw6tGt1d37bwjJJNvXJqexF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری از دوستان میگن که اکانت ممکنه ساسپند بشه اما خب.. خودم هنوز ساسپند نشدم این ریسک رو در نظر بگیرید رفقا</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/MatinSenPaii/5136" target="_blank">📅 11:06 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5135">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون  با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)  1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه.…</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/MatinSenPaii/5135" target="_blank">📅 11:05 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5134">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GOEixMFBsW2NVSYFCSbOgUfKJgbIP-4Xu76RGYZFpPlVRtXxeII1w7NLIgFII6udz7NJMbfuwgHcoZLzRAzP5e6zysFLJc9fDfvNs9hJ0UuJdkuVPAx1BUenHMd-KJLtoYXjd9cBV68C_uuDwBwD3-vT0HqNepNb5fsMisxNTXRUNMNladJKdVWOiqS9MLErJoMhOJTwT4WT68L0eIJllKlR3LYdIEuc2Z-IWIXgCAa0uhtU1wYk97m8LwnlccHNg8h9NJShCt7DdVLVox6oM78rlBSuRFr4zzj-DxEypTAB3YCUYgV9XDOxPxmOm9tl4o6syr5TEQzbD7DRtrmnbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیپی‌های باکلاس آمازون
🥰
بریم یه VPN بسازیم باهاش و یه هرمس هم بالا بیاریم ببینم دنیا دست کیه</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5134" target="_blank">📅 10:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5130">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/r4U-LS77hhOoG5axzLOQDVkHUmHPTpT2a3F-V9fvETgSlmr9quxaGL1fou5_bOBXfnONG1ou6HEiS4g3HTh_f2FA1if3eBCZYJlO0wmJk_kXY4SlBiHaOoatmGNSXnXDy8n3uaACcWrkjByk1l5ZHDsH3wG0lwIwbvplbMpVc_IJzmm1lDvWgkmYH4XEjtsu8cze79e9TxQU9tX9NlhuCDWK-v35TLPp-Nm5AAChHxUaY_StRoI7xwoYyVS5sayAhRoVjwNub4aw3bNC096YG3a2LlZTXqgy_fPMDwvap0NVNgfCw6W91wOFNmqSYLp9GSXcU1fg31qWTbIE46kh7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/NFmpKPlT9pAMsbUH-JotuSIZxgvEU2pW2y8tIhORiWiOFXQYgkMEk1-EZVqpHpVHzoaQyo8YUnz9MrSUXFEc7f96fOfKifOls3XCY5HD7pB-MiBiOkX0CHH5G8Z-zYWgsWGiQ0dBXp88JkUaN_xgLmHynpaqEu_hXfvZAnER9tLO2__rLqBas7Cd3RqA3pzTADRzeI0UdQ2B8f7q_mhsGGxBGUAuaBuoV4B2mX0aWX4uREZMyYH6_HjChR_OfaO9ekEpn25_Y0yCetPD0RQ4o2NzEFyLvrUEvBYnSkreGYqQD0QOuMx7Km0HpUiLjJ0BJBiBFxnRgp28mEEq1SjJNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/CvnE68tvgHWk4l2LAo_9ZYeH47KeOAQzaZXPpwzPvHnR0JflFik3dJuYpF02WvE2JjHSLxpeohwo-QoZjwHxC0DLRLhGGGtiX8399KomHcjWA8G2HOKieCyLPaAZS4cCMt0ME_FtZJeMvNvljpKcZ6xbe-25xkfSVx1BG2_eaN0BikzCtq5COKyvfjKxdqcXjddoQySnh5Z1ZKmwplYHhnCbLVvZVf2VrzD8ZUKW93nT02URn_3lLSLCt53UwHdO2XSCniI2EI4z40WKvoRaP6Q3rI6AYXUPUKOruBYVk2cNxGMhjMjN0Sqqoy5WdG4PIuU7sqDaKKOYZw41H7AKSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/f2qibg0IpwRtDz2BPY0JDI5bpReq85D4iHqm10t_63HEiRpiJC_opmmb0RBpWrIVcTsLhH7PqbiTq2RwoXwh7BRFetKwVj9QiDpIbcAXs1tdQ-3ZA64TDSilvTxHPqHGXEok4nr7pKcU7MMWy17pmDcOhxd0CGie19RP2Rs3513RwnF_hBqbjbVnSTqcfEogj5IBkXllXWrhYiyOzuamjWeP1yclskSHAJjuuaS4XaYOMH-0bArRCpLnDlc7pd5uGc00xWmXsn19CzK9x4In1UdWqkUyaTOfgA_pZR1mWUY-cyf5T96kwCF7B-LBEQAPahRdm68chIMCrPeXoWndnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش گرفتن 200 دلار کردیت رایگان AWS آمازون
با این کردیت، شما می‌تونید روی آمازون سرور یا Storage و کلی چیز دیگه بسازید. اعتبارش 180 روز هست و اگر تموم شد هم، اکانت جدید:)
1- اول از همه، شما باید یه حساب Mpay داشته باشید که حداقل 1 دلار موجودی داشته باشه. آموزش متنی:
https://t.me/MatinSenPaii/4915
آموزش ویدئویی:
https://t.me/MatinSenPaii/5091
2- وارد سایت
https://aws.amazon.com/free/
میشید، و روی Create free account میزنید. بعدش سایت خودش شما رو هدایت میکنه به قسمت ثبت نام. VPN هم زیاد مهم نیست چی بزنید. من با کانفیگ‌های BPB رایگان رفتم که آموزش ساخت اون هم اینجاست:
https://www.youtube.com/watch?v=iAbYpjXyLpY
3- برای آدرس، یه آدرس فیک از سایت
https://www.fakexy.com
وارد کنید. شماره تلفن هم من گوگل ویس زدم اما نامبرلند و سایت‌های شماره مجازی، همه‌شون برای Amazon یه بخش مجزا دارن و زیاد هم نیست هزینه‌اش
4- یه ایمیل تأییدیه واستون میاد و تمام! 100 دلار کردیت رایگان میگیرید، بعدش هم با انجام دادن تسک‌های بخش Explore AWS که تصویرش رو گذاشتم، می‌تونید 5 تا 20 دلار دیگه بگیرید.
5- ممکنه محیط آمازون واستون گیج کننده باشه. نزدیک‌ترین بخش به یه VPS معمولی و راحت، توی محصولات قسمت Compute، بخش Lightsail هستش. چندتا نمونه قیمتی هم واستون گذاشتم
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/MatinSenPaii/5130" target="_blank">📅 10:12 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5129">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/D6eCZQVe8f2wy8GBrJHb9Bn1p0U6jwaqmc0i3op7IwF0ozEl9jU__8r1KTP-BFVXib5kxWhXPPC3gDw9dtUlHQO4GJpc1OzPMqeK7-yTKYZHyZHZwKyJhPx_mNx7bom0HHkgCQT6CyD1-BA2Q4ldlEazf7Ij26OKQHwvZGC4qaE4D-L7SdUZnJjYzE6xX0xHCQbIFRKokNpJmoPI5JDwopPxlaSEjw2fhwjvuvO3Is4w5DtjjNs44Blb_9MOojIIuNMf0u-rYVMojEFaAIXhBfrpNI4akY6HnchBxoOd_jhA5ObdWIOW23-0aUBC08po8F-n10dn2Ll_WMqyeTfONQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با ثبت نام ۱۰۰ دلار میده بعدش یه سری تسک کوچیک انجام بدید ۵ تا ۲۰ دلار دیگه هم میده
و می‌تونید ۱۸۳ روز استفاده کنید
به نظرم می‌ارزه</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/MatinSenPaii/5129" target="_blank">📅 09:35 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5128">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">این کردیت ۲۰۰ دلاری آمازون رو هم موفق شدم بگیرم با Mpay
آموزشش رو می‌نویسم الان واستون</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5128" target="_blank">📅 09:33 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5127">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خب بچه‌ها من تمام مدل‌های چینی و آمریکایی رو تست کردم. فعلا برای ترجمه، رتبه‌ی 1 رو
Gemini 3.7 Flash
میگیره. رتبه 2 هم متعلق به
Claude Sonnet 5
هست
که خب فلش توی هزینه، می‌بره. رتبه‌ی یک و دو به جهت قدرت ترجمه هستش
هم برای ترجمه‌ی کتاب فانتزی مقایسه‌ی سنگین کردم تمام مدل‌ها رو(از جمله GLM و MiniMax و.. تا GPT Sol و اینها)
هم برای ترجمه‌ی متون تخصصی علمی
هم برای ترجمه‌ی کتب برنامه‌نویسی به زبان عامیانه‌ی فارسی</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5127" target="_blank">📅 00:31 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5126">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFLeweMdbAfYCvtUhpFpAjndNnaqtl_3tCPCKikWiNa4NBODbCTinqWbzDwbjRD0TZicJei8A5dlwefp0QYRMLkVwTy7yP2KQzYyHplMw8Z_4F7WDdhXUt6FmMyNXWuebKn3Mx4sxBLCxSqRN1hhnGaWx1sd_4OpW1KSm8ZEZPQzwFGL1hjJ168HYyGWyHDvyUBEuLAjZLEk0nLTUe9zuiwkgkEb9r-PBY17YTpx9uuVYFfLVCi1qqZ98rVg15kHY4a3fsYHMD_3IAdj9rC6MdEv7gMj9EMeNfWoQ_MorNQ-oaHkUD1V4CxD4sGuIgxEVoamNH6shAyvjKHSE1WDQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه دنبال ساختن یه AI Agent برای کارهای علمی و تحقیقاتی هستید، این پروژه رو حتماً ببینید: یه مجموعه از 163+ مهارت تخصصی که به Agentها کمک می‌کنه کارهای علمی رو فقط با تولید چند خط کد انجام ندن، بلکه بر اساس workflowهای تخصصی جلو برن.
از Bioinformatics، Genomics و Single-cell گرفته تا Drug Discovery، Protein Engineering، Molecular Dynamics، Medical Imaging، Machine Learning، تحلیل داده و Scientific Writing. حتی برای کار با دیتابیس‌های علمی مثل PubChem، UniProt، ChEMBL و ClinicalTrials.go‌v هم Skillهای آماده داره.
نکته جذابش اینه که این‌ها خودشون مدل AI نیستن؛ در واقع یه لایه تخصصی روی Agentهایی مثل Claude Code، Codex، Cursor و ابزارهای مشابه قرار میدن. یعنی Agent می‌تونه بسته به کاری که ازش می‌خواید، Skill مرتبط رو پیدا کنه و از دستورالعمل‌ها و workflowهای تخصصی اون استفاده کنه:
github.com/K-Dense-AI/scientific-agent-skills
@Linuxor</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/MatinSenPaii/5126" target="_blank">📅 21:16 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">WhiteVPN-V1.6.4-arm64-v8a.apk</div>
  <div class="tg-doc-extra">34.4 MB</div>
</div>
<a href="https://t.me/MatinSenPaii/5121" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5121" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5120">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbWZjbJSpyxATmrp6tNc1eXUUqNlGYGFjdjESOuSQ_aIe2YWY9k3ybGJSWTa0akcI2dQ6s08uFrppdP0fIMS3vq8idwnG2QEKw55cNytj-GL7jmpR9gPL1mipLkwcAd9TnbZlhlXPmEdsSjayMOvC3WGE1pfuVuNmSyg9ePY-c46CexJskUrjjHbsbQ9McRZSNDExNPMc9t5tXKgRG75vA8nfxPTINfcMoKipabT51tV-IAhxclG-Yl6gj3dvsBhcKd_SzwreTnoyxUf1G8iFSCSWIbVsqVfd5U_IPm2ZvRDsjmXG30qIbEYOt8_eZHQywLfi_8nh9y_OYHo1LoN7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💬
ورژن جدید WhiteVPN  1.6.4 برای گوشی های اندرویدی
تغییرات در این نسخه:
🎯
اتصال و قطع اتصال پایدارتر. رفع مشکل قطع اتصال.
🔒
بهبود امنیت با رفع مشکل لیک با IP V6
🔭
افزودن کانفیگ با QR Code یا Clipboard
🎨
نمایش واضح‌تر وضعیت اتصال و بهبود ظاهر برنامه
📱
دانلود آخرین نسخه از گیتهاب
نکته:
⚠️
در صورت دانلود نشدن از گیت هاب مرورگر خود را به فایرفاکس تغییر دهید</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/MatinSenPaii/5120" target="_blank">📅 11:15 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/MatinSenPaii/5119" target="_blank">📅 10:12 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">باز دلار رفت بالا و این پیج‌های زرد اینستاگرامی در تلاشن پکیج کسب درآمد دلاری از برنامه‌نویسی رو بندازن به ملت</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/MatinSenPaii/5118" target="_blank">📅 10:03 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آموزش ویدئویی رفع مشکل آنتی گرویتی و سرویس‌های هوش مصنوعی گوگل:
https://www.instagram.com/reel/DZ7NWUOMeHy
هرچند ارور ۴۰۳ به خاطر vpn هست و صرفا باید از کانفیگ‌های bpb استفاده کنید</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5117" target="_blank">📅 09:38 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">زلزله به بزرگی ۳٫۸ در پردیس در شرق استان تهران
در عمق ۸ کیلومتری زمین</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5116" target="_blank">📅 08:09 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟  توی این ویدئو، با یزدان عزیز در مورد این مسائل صحبت می‌کنیم:  1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور 2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن 3- تجربه شخصی خودم…</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5115" target="_blank">📅 07:27 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sjvSdC74ACCqfGko4TCJ-eZk_u2LjhnR18cJiFjyOxauu4wt10UJZLunGU1NrseqqXRMSE8iEVZ4a1cpRp8dubNgtO2Gyx-JyemCb7o5jEflaw3xNndxnc-BaqZw2ihxcVzUQhocrtGQOeOPVn-35gPsbNLzGy35lVhdLcb3NIF4rJoqHgcE8JoSvR5bMjzjemYut_vQ4i-DImix979gWD9GPMKDOAPEyAxPEqwHM19YZly9aUM-CHC2q2FVAr_VJahEj9acNHn7J0oRWMM-_KgYiv17T0TRDDcDLM8kSkdtamcuJ5TjcQLdfveaB9urEkzs4xdKcDwrmdC-MKjpJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا کنه هیچی راجب
mpay
نفهمن
😦</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5114" target="_blank">📅 07:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مجددا:
این api های رایگان ممکنه امن نباشن پس توی پروژه‌های حساس استفاده ازشون توصیه نمیشه</div>
<div class="tg-footer">👁️ 31.4K · <a href="https://t.me/MatinSenPaii/5113" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9hWGlYNPwUno6VptZTKTrawqb_YqVWQfl7x0VadLd3Ve3byq_rF7Vf-l66roVbdCXae_M6hDrg9vdeNeAcRD07uRKSth7L7_VFJclWG2kq0ShvcpSV_2r-jtnbhFn-_ypDxRM1FoSGHkFUPmIEA3qaeOISlgO0iXGQwjwX6G5N87vZCZ0DJMtt-CS1wQUxCK5hqE9Iq3TmEIqs1Fl3mTrrdU18o6fwpe3u30TyVoT4C2zBtfmzYsVp6M5zxaXTxDUfYTVFf8vqMUdLbCDQMXw-SKbB_U1kke1UGA6UwQYm1fx0duDkOx2WL-P7PN9amtZKBHUw-FtGIf4JWxwGxpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا دو سه تا اکانت بذارید و Round Robin رو فعال کنید، خیلی خیلی کمتر احتمال داره که به لیمیت بخورید
تا تموم نشده استفاده کنید</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/MatinSenPaii/5112" target="_blank">📅 17:43 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hdIwAbN0T4IWgGdWs-ZC5C4Agn1z7HJTe3h9l1R1wZHP-lWaYme_63iEKsB3QG-gZ4kiZ12N6CBKW-v7dIJ9jVoan--uffILS-crH_FafBVT7Q8OKARf_7F_yrWYKXE5UmXgOmg7zH69kSAIB6f3peSWqzvbaqmYIvs0cRoCxR3pdi2TZco5fy2PLrPjgEHWlzlTE5GUEGU_mqF4mNLRAJsC1CIC3jd-LjIB1v17MEIc_5CfOxJjVuw9z3ZrgH7-XkW1eu2OykjF1dP1MZnKOb6vBePVWmmWpX2Da6uWsTGF_P5qWFgkHWoeR_W_TDVMidYGkZzN_lvb95l0h5DdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ugVVfNFJjmP_D_MwJL3KH_LSsQcGN32kvlrxCi_xakH2alr0XKJwB78cOspnC8FUgCHdnwDEAVXShPKpJwwvaWyUXb_g6ENavrMFXTS6gU2BdPWuYDgaMlME3lp6w_CO39ZXwksmz9NSVbj-hHkkyOMsU7bsi-2xBZZKs3Xf1qrnoOJjTDAgae7m07QAWLUZjOH9pc9LXfDsVNewMN3uwCecT5vsVs3TBx95WG4L7Hk_uqK9m_6uuz70t9HDHFHoJUWZ2F3ssg_Df1Xz8xtygFQxiGYF5bGng4dZRXNaGgYSHzr81-OyFo6PXk_Oaa3SWaavjXs8vCiqEVVwbFV6hQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">خب بچه‌ها انگار هر api key اش حدود 30 میلیون توکن روی 9router میده
بریم اکانت‌های جدید بسازیم
🥸</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/MatinSenPaii/5110" target="_blank">📅 17:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5109">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شاید براتون سؤال باشه که من چه کارِ بسیار مهمی دارم انجام میدم؟
باید بگم که 18 تا پرامپت الکی بازی سه بعدی دادم به هارنس کلاد و وصلش کردم به 9Router و همزمان با 18 تا ساب ایجنت داره واسم میسازه
😂</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5109" target="_blank">📅 16:42 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5108">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EDEADgzfBDADb66DgFQoy41X-VMLIRdh1uqbMcvH9k2b2gIMSjgtxX7ZZ84LYE7szaeKorAt0wUV8BtA1NHQgYoSukOZTIgQMgbwznoBDDf1OtIf119iWYoUFwbDKp_cAhkZFywldLyB9loD2d2NRaliIzqO2TOxG_AWTN-34-RRHr8LxxdmTb2jGJH9HAMZ0dPYNph9v0QKd2IcJrwpVrFYuRhoRASSCJfRSe2WWST_yOT4_kGDmh96EUkqutkKs45_o6p0yNZEk0pFn50mFQtAVFwIVUGCXOAKtGHWo-2liIb5ySeBhE7IqFkwnS6RpE-0k0_qWRdeBVVYsiWaDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایشالا که خیره</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5108" target="_blank">📅 16:39 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5107">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/f3rhsTxLaXf03lO1ajtKNJNFo_pbj3WsMmpt5QW2VrDcOiSdmupa8QrdfenxFLpRoddDFbOsGQ7SvFQFo4d6YpYsTsW9Bh_gOKkbOhrS8p95ID6kELKpcZHR5YZ6Eb5YhhPPtm9Nw2V7PuMtUH_tpClNZlIadJYZqgLvid5EleL4v6Gt6ypEa_jsh9uFN8NCNhHbFLTMHl6sKISIvvjo9yfdffUS-0qARlnymYpte3bzehppMPTHPTOBtoWMmOWRxaJFwDKyKtePI7_xgi5WXpZuzTeWBBxoVEXOf06bLTs15UU1sJL0UecujS33V6emUoh5qm9cMfsHek9Iq0FeAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا از B.ai هم میتونید api رایگان بگیرید واسه‌ی GLM 5.3 Flash یه ورک‌فلو سنگین دارم میندازم پشتش ببینم تا چقدر توکن جوابگو هستش</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5107" target="_blank">📅 16:30 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5106">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/eey-FU1e3GrYCxkd2E_YQqNVV6w37r1C0TrdGpV8psdSDWkTkDdRZ_HJr-AvbQs2_V5TYhll5aCq3gt6IIQPzSKg_g_tD_jxkWrs6bMTNymP7ZlSe50O8UyhU8eWAFGuPuSRu6VsocSg1Wb8LNsmCzm-dY9B4-eI5Q107ArncTRXvjlhJy41rCZ8Z-RnestXgJY-bQhfbHLeR3biUpNE8v_8wphTbASGqam0bAwZfU_Fe5biM7cKlylZA3e-6Kop05G1MhRSOV79SG1yDLGPNarIbJXU8DvsJzSzfUhoh3rnKy4NdK4lOkqxaMXjikhKr1y7EuLappb1l-5ol4YFpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/MatinSenPaii/5106" target="_blank">📅 16:26 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5105">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AC58B2GWxxx5Xktb6q-336L48_cpEdwgoiHKqmOWLoEMKi-Lx72pEljIUYosAuCyVpSMY4M632T2qzFFzqudRCGwy-bY_zcd-7E9RZtcDN0pXm6ACt30lg-Yt5WQEnb0x6RMpleM75VKiBqzrEfPtAo-p8Y1N9xS4trPtuQ9NK0jZXlssLnL6_rt0wAVAiylwptHt_J4f4nS1piNnhnVhGDg5c2h_XzSyVegOyoYkir6oqMju3MhM2UsDdLMmk2OutVVXIWBuK3-Fj3G9nYQUow1f1aGEs7u6vVYidJcPLjuZbAD1BzCsMjZvmVhbcSldHMTD347eQaquZtpgnteDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🙏
🥰</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/MatinSenPaii/5105" target="_blank">📅 16:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5104">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/tMR7SxwXXrCmY2LBvVHCrB2RI4PIn4jPeZrNqrpL_8SQUEljUqBfXc1IoI6LQKwBwABsa9fcpAMmSPR1ETbb2ib0b1aEa31L5eIQiPSpSgbtnGDkKmz4E7ZG1y2ckhUAmBKxCryrvCcgNatYgpF_GmJusOas_M6Nn6MjegES-lBr_zxXq_z6vtEcLIabEzRnsdoA8AFMag-gIPhr3B-wQGYg0QLGw6OY5Be0pTp4kZ0_cwNGYvcH1kOBtTAc8G5H8uoeJz1aolV4UmoILgKGu8wMBs56Gc1KMsZMz4uW3ArAmC5X9vFj9uSb3qGJlbkEY6SGE88amEVmfCKoJ_-f6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازار کار جدید دنیا و هوش مصنوعی! توی 2026 چطور می‌تونیم برنامه‌نویس بشیم و رقابت کنیم؟
توی این ویدئو، با
یزدان عزیز
در مورد این مسائل صحبت می‌کنیم:
1- مرگ پکیج‌های آموزشی و یادگیری پروژه‌محور
2- دیده شدن و شبکه‌سازی به جای رزومه فرستادن
3- تجربه شخصی خودم و شروع واقعی برنامه‌نویسی و مسیری که خودم رفتم(به علاوه چیزایی که به درد شما ممکنه بخوره)
4- تغییر قوانین بازار کار و حذف جونیورها
5- اضطراب، فومو و جو الکی شبکه‌های اجتماعی
6- درس‌های حباب دات‌کام برای هوش مصنوعی
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5104" target="_blank">📅 15:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5103">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت: https://app.mpay.cards?startapp=ref_S4FPMh ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر: https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/MatinSenPaii/5103" target="_blank">📅 15:09 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5102">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">و آره، منم حس میکنم یه کم ضعیف‌تر شده نسبت به پرومو Ox Alpha</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/MatinSenPaii/5102" target="_blank">📅 14:41 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/i_1iBDgS1ZTj_we_rmaR3GHUg5j9GRAdANA-hAWEsn7uZmjd-M8K2XhqHWxEW7-vVQmr1cy-UWJuLaLhIqiJAwuZxqRiExKqCYV96H4BjrMr9as_sDxJjqC4tddn5VOyB7A-1_PgZkKA3PEQhOg4-JTXAyWEOjl6bUP88YBPTUqMhSKBHEZ3wF3N7RLtd30_tGoy4tnjKEFDG1c1nXKEF3jipxUacuYZMrFX87MabmwxCYzl70qd4ZVBzoEt19-P9uz1VfWz2JpqjrAmhtzHhfEByy-znI3qZNqzvgb6JDWRe8y4MxkT9C1rnkKdBitU2Zo0CZkD4sXJhF4ubBq-qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:  با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.  1- خود 9Router رو که اینجا آموزشش رو دادم باز می‌کنید 2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline 3- این مدل رو…</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/MatinSenPaii/5101" target="_blank">📅 14:37 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5099">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fGx4PHjY0o52txUg9wT4kweJBr3i63tO5tT4Z-_U_ciofLdX3pOttVtJt8QF_micVwKWIeMfipJyq4TBo5HnOZ2Kmxf1n_z54HUajRU0n5nR0j55avuS1qTXXnftI0oHCYnBzIJZOhS8VXCNE5QjV2oZE4JfyWret08c5I_8lRag6YjSaJEEeeECCcv-W0Dmezmw0FbTS-7w1koZbclxqmBwe9hri8OfC-om0y5yavQUijIn2hXpysaGe3FazpKhszqbMkILrDjsBvwh18jMWE6tCouDoBsguJ6Ikz26udt3P4qbMmDSOTtiikgRLxDPY01JWN7MkY3jvdV-JgjXIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oXOofNbw0-BuH0nCviN97eezmU3frzs-4ygwnQ_mp5aAOXo_SseR2yxQ-55j2Xxm-ByfgukQHXVTeabeCH-L3gTaj5sFdkheXVUsZSCRI0Fv9LvDxwWuM-p1K7ajn5Xjv_rG70_Dm4vrrODOBPxl33aoedpUi6PmJgQEd9gy-WqwOpfEy8nXAT97o9S-SgkFZ6kbbJS6wZ0QhROGdmnXHdAnx7MU30kQFpi_AXLWxvZungIxtlU7Sjhr4LHC_KK6ch-KGB1NuTtRc6aZUWAg3Vyx_phtEMq3iaxa4CnuxpHLecXo9TSvPy88YSIFl1mt1hNo8xiQtuB4IcTXx5y8-A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آموزش استفاده‌ی رایگان از GLM-5.3 Flash توی 9Router:
با این روش، با هر جیمیل روزانه می‌تونید حدود 15 میلیون توکن مصرف کنید.
1- خود 9Router رو
که اینجا آموزشش رو دادم
باز می‌کنید
2- وارد پروایدر Cline میشید. دقت کنید، Cline Pass نه. خود Cline
3- این مدل رو از بخش Add Model، اد میکنید. دقیقا همین رو بنویسید: z-ai/glm-5.3-flash
4- می‌تونید چندین تا جیمیل اد کنید و استفاده کنید به راحتی
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5099" target="_blank">📅 14:21 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5098">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I1tJkmy8RkVLWNBWnDXzXQtisvSS_GXP0qTvVoM9D8WXlmvnkU8-rmiUV8XXtcYzsp6iTju4QB0FYA90kWIfS5eTgUQwwyDo8mBISg_SzoerQZ58G_upcbIDVDmUr9jVUkN206W4xYiM8QwFjj-GRCwRNxCxjkbpFjuHVVLJaRGuHHEP5gDDFPp24RQ_rJmAg7U70eAW8w9rldcEhJQWOP0HmiGzTWBDJiyakAY6BYmu4SjLYW3fEwySogpuJ5wdrCmMD0o130n1BUACGcq54Ulo4K6bufSVBiYGxCaOE-bvI6nmpRoDKnTK2Qng7sAsrRroW6x-AcGe7oZ3jIkEjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن #ClosedAI</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/MatinSenPaii/5098" target="_blank">📅 13:57 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5097">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">دوستان من به نود درصد سؤالات غیرتکراری توی کامنت های یوتوب جواب دادم. بخونید شاید جوابتون اونجا باشه
هم راجب کلاد توضیح دادم هم پلن رایگان Oracle و...</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/MatinSenPaii/5097" target="_blank">📅 00:44 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5096">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LZiqri4cT2kfDG7ta4ZpRgMt9Bu_7vsyLl_Fg6ZYHUl8uxqxOoXgxToCAODpBw-aszLOBTqLEccHGBDd50aRBZ6b07tIl97pZV71Z_8ITaoDwDE1noYG7EAOBaMs9y9IeBSxm9V-aKtSOWiCv9_1xjbeXOpPGPBD5ANTlVJeodw5JiEW1hFBssXkStfbWfhaq0DcU_21JWnPuesHW0UvFQNNZhV6RsRiSVQ65xaTJdAZs4a3o2PfusqIVAZCIK3s-hHntBh81FcDKG8VFNFe1l9CjgJRqiu-dxbiCF-x70QdUwtc1dISGdF38-pB6LwowwjkinPvEeQbcpcrSNgmWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مورد پرداخت توی بازی‌ها</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5096" target="_blank">📅 23:16 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5095">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/I6XX9JfHKGO2ZbecCaPUDDI1S19yXpQ3MPFPjMZjb4MPUQHjPhx9oESV7wYC2S_xTrkUPOviazdQcK7Tl0DUarkVla8E5p_27qRCCuauqvl-LxztjhqbjruqXD795689X4cMxHILRGiMdhsVupQstE__tquzln1XBaW4vK3jkfnL6cQB6VOsPzbEOuO2ndqr7E-7B64Kj2flWdkTqdE3WA4w4gCkrtDx1FhrQ3BQDGC2yC1uMSc6qIiJMVn4gbYX83OENm941pyvx2RERjvV2gMsLH7RA0smQyXFr2WXRA63PJi__ghFmiFHqaJpF8z5fewEaoDHUn2jIPYN3o6Nxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها بدی‌ای که صرافی سواپ ولت داشت این بود که اسمشو هی با این تپ سواپ که دوره‌ی همستر و اینا بود اشتباه میگرفتم ده بار مجبور شدم کات بزنم
😂</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/MatinSenPaii/5095" target="_blank">📅 23:15 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5094">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">Iran is not for beginners</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/MatinSenPaii/5094" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5093">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">روشی که اسپاتیفای رو گرفتم، این شکلی بودش که هی ارور Country و اینا میداد و میگفت ریجنت با روش پرداختت یکی نیست و این داستانا. منم ریجنم رو رفتم آمریکا کردم با راهنمایی از grok و بعدش با خود google play پرداخت زدم کامل اوکی شد
حدسم اینه که برای اشتراک‌های AI مثل Claude هم خیلی ریسک خرید با گوگل پلی کمتره با اینکه شاید یه دلار اینا کارمزد بره سرش</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5093" target="_blank">📅 23:03 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5092">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ببینید من خیلی از نکات رو نمی‌تونستم توی ویدئو بگم به خاطر قوانین یوتوب. اما برای اینکه پرداخت موفق داشته باشید چندتا نکته هست که باید لحاظ کنید:
1- برای خیلی از جاها می‌تونید به راحتی از Google Pay استفاده کنید. یعنی میرید توی
https://pay.google.com
، کارت رو ثبت میکنید و تمام. اما نکته خیلی مهم: برای اتصال کارتتون به Google pay، بهتره که با آیپی آمریکا وارد بشید که با همون روشی که توی ویدئو گفتم من تونستم وارد بشم. اگر کانفیگ‌ها واستون پینگ نداد، کافیه که Chain کنید با یه دونه BPBای چیزی.
2- تمام چیزهایی که روی گوشیتون از گوگل پلی دانلود می‌کنید، می‌تونید این کارت رو بهش وصل کنید و خرید کنید. حواستون صرفا به اون آیپی آمریکا باشه
سؤال1: اگه یهو بدون آیپی امریکا رفتم بن میشم؟
جواب1: نه بابا. من دویست بار با آیپی آلمان و حتی ایران رفتم. صرفا ارور ممکنه بده یه وقتایی که ارور کانکشن میده و ایپی آمریکا که میزنید تازه درست میشه
سؤال2: آدرس و اینها که ازم می‌خواد و کد پستی و... رو چی بزنم؟
جواب2: خیلی راحت سرچ کنید Fake America Address و اطلاعات فیک وارد کنید اما سعی کنید همه جا همون رو وارد کنید. حتی یه جا از من کد مالیاتی و اینا خواست من الکی یه کد 8-9 رقمی زدم و گیر نداد دیگه.
سؤال3: کجاها نمیتونم پرداخت کنم؟
جواب3: ببینید یه سری سایت‌ها احراز هویت با Passport و... میخوان. مثل اکثر سایت‌هایی که کریپتو میفروشن با Debit card و اینها. فقط توی اونها من نتونستم پرداخت کنم. تا الان هرچیزی که خواستم رو گرفتم. که اکثرش هم توی همون گوگل پلی بوده</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/MatinSenPaii/5092" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5091">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KPyIfqa3oKPjJ5cF7v6JA_gceG0HumJlCB97B73qah_ColT1M3Qg9xALB5o_C1Z83IS1_kyJYNxKVBtgebXVY4NOnbJBfioc-SsbQhKDzmfg1OdFwKXib2ypwT7X5pr4ouA-JK6yz-FWB_8YLgJoRUpznkLmnP0tWo0e1aSo4Rn7sj1Cl6yO-KF7vK0SE0KKzO5nRguXEGz9sx6SPj9TGI8Dv2CCwWAn6xv8ZxoyLHE2HeEtF_ksPYuL49Ucxz69GRtom2CmRVgsBe9weTac4X747pwQWmfcwjLeBCpp2YDlVpd9mF4-ki19o0qIoCmno80CFmlx6Sw9hCDtih9tTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☠️
خرید اشتراک‌های دلاری با Visa کارت شخصی و کریپتو
⚡️
ثبت نام توی Mpay برای ویزا کارت:
https://app.mpay.cards?startapp=ref_S4FPMh
ثبت نام توی سواپ ولت با 5 درصد کارمزد دائمی کمتر:
https://t.me/swapwalletbot/app?startapp=invite-515916
🔴
نکات مهم در مورد پرداخت برای گوگل پی و اینها:
https://t.me/MatinSenPaii/5092
⭐️
توی این ویدئو:
1- بهتون یاد میدم که چه شکلی می‌تونید توی اکثر سرویس‌های خارجی دنیا پرداخت دلاری داشته باشید که وصله به ایمیل خودتون با اسم خودتون
2- با کریپتو حسابتون رو شارژ کنید و از هرجایی خواستید خرید کنید
3- حتی بدون شارژ، کلی آفر رایگان بگیرید
4- و یه صرافی با کارمزد پایین معرفی می‌کنم که می‌تونید به راحتی ازش خرید کنید
5- سرور رایگان V2ray آمریکا بگیرید و ازش استفاده کنید برای پرداخت‌ها
6- اشتراک Command Code رو هم با همدیگه با همین کارت میخریم توی ویدئو
📹
تماشا در یوتوب</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/MatinSenPaii/5091" target="_blank">📅 22:54 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5090">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PYsXi7qKwww3owTX4kM5SOYjV08owd9kMSHU8ja6ffA2g4BRpDmBqTteEZlFVIpq73W9HFRYReeYYQ2K73PzzD-NHER97qbS2AW5soQ-nCbznioktgB4aXlo4veOARedJYzdOm9A3aSN6qKIG1q3r-K8XVjTlMTNQZbJyILObtr_w1jQiVbhkLDeiRYVradXofhhz5sxtGwFMzSlwL7hKTaH5a_XCrMZtS9MK78kAZMmvwgy_a0LdjH4-6adwe1P1EYv2T8Uwy2Ni9muGr1SQ9nwXaCeM8xgELjVLmHYzPT6DwkWAmK3jsu_4aAOD9DAx0wLzVoPgQa8d5Uy_fYrSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی که خبر خوبیه یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/MatinSenPaii/5090" target="_blank">📅 22:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5089">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">گویا کلاد هم داره محدودیت مصرف رو افزایش میده به صورت کلی
که خبر خوبیه
یه میم الان میسازم بهتون نشون میدم منظورم چیه</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5089" target="_blank">📅 21:39 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5088">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این وسط واقعا چیزی که حال یه جمعیتی رو میتونست خراب کنه خبر کنسل شدن آزمون تافل بود</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/MatinSenPaii/5088" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5087">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/MatinSenPaii/5087" target="_blank">📅 16:41 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5086">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خوب شد امسال مدل‌های AI پیشرفت چشمگیری داشتن توی تولید تصویر؛ تا این بنرهای درب و داغون الکامپ یه کم زیباتر بشه</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/MatinSenPaii/5086" target="_blank">📅 13:32 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5085">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دلار بالاخره به قیمت ماشین مورد علاقه امیرها رسید
🔥
🔥</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5085" target="_blank">📅 13:19 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5084">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گویا  OpenAI تصمیم گرفته قرارداد تأمین مدل‌هاش با Cursor رو تموم کنه بعد از اینکه SpaceX کرسر رو خرید
😂
کامیونیتی خارجی هم به شدت از دستش عصبانی شدن و همه‌اش دارن هشتگ میزنن
#ClosedAI</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5084" target="_blank">📅 13:01 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5083">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=bZYzpYdwLMeRd6RMDGnCnUmI7qXShdYx8qZB89eBGbuSefvWn423n0pE91qQcH9nkLzM14kdji2oLOCX24D0LnE6bieIJ0p8fgSdPO__UqSxRJnO4P_pOVNryWayiTHl6M5xvEGcTn4NROedoJlWJjYbeVfSJ0QT9veKeacfHHupBKh-6y8nDgrWeMds-YptGtzpYY7OsKW37DxF4BoXZcGxuEgJuHVBV85W-iDTgj2J0-ZHmEYYnUjGbkrAFrV7Kvrsgndt6yXNPfTBYtLw74p9B9wRxsym6BbkFJimbG4oju-yRpKbBLl_WWJEFWV2Gs-VS205X_HkWoDGDaDK8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f91f653dec.mp4?token=bZYzpYdwLMeRd6RMDGnCnUmI7qXShdYx8qZB89eBGbuSefvWn423n0pE91qQcH9nkLzM14kdji2oLOCX24D0LnE6bieIJ0p8fgSdPO__UqSxRJnO4P_pOVNryWayiTHl6M5xvEGcTn4NROedoJlWJjYbeVfSJ0QT9veKeacfHHupBKh-6y8nDgrWeMds-YptGtzpYY7OsKW37DxF4BoXZcGxuEgJuHVBV85W-iDTgj2J0-ZHmEYYnUjGbkrAFrV7Kvrsgndt6yXNPfTBYtLw74p9B9wRxsym6BbkFJimbG4oju-yRpKbBLl_WWJEFWV2Gs-VS205X_HkWoDGDaDK8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شرکت Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0  مشخصات کلیدی:  1-مقدار ۷۷۰B پارامتر کل ولی فقط ۴۹B برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر…</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/MatinSenPaii/5083" target="_blank">📅 21:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5080">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWhite DNS</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/mTL4IIM14otRFrZMA6nF0hCHUJlrlDgl1Cxa-Yfq6fAIZgMjuWQYpfkgAYUTQIweeWnTzSxRSKS257EDpoeQ-yoG9orTgL3HL93WLSsJkI5S-HQsPUnmcHaWLeyaYU0LFehw858CPvppWg0Yz3JgNtAbxpuPLao8mkfFE8P9QhRwsyyAFyTUiJ5e8VLU_gAFpQzjglxLptoGz48C0eKM4et0DAybuPUVe8v--PMGP3xBIeA4Kf0YvS8ULmLJbqGad-lIRZBLOsg84FzyoSVW-Vb_THVeKS3yy1HOUjMmALvx-1pxkSjsx9elxZqndL1rjjGWx56-ac5OTf3rWUKmgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/KtimhyaXA19Unb_h6McUQj8TejBwrJsudLy_sMWbiVR5AW0wsw71BlKFseQcXSZtMuBS4dWHDOIi75DGtnlSk8rnwXOhjVwjqtRBDmkIFnJxXblsHRTgWovMCQEoH5V9r9Gv4nzG16GixnQ1mu1kiXUrLH0eC4wPTCiukeIPZpeNyNHmH6UNBd2d2BUjeRFUQSLf7_xXJC9e5ETZt98u6bBXDC9bq0oCFRe2Du_ssBvCtkW1U6xBfj1SdJujZeb9oyDeqzt9hDsG3OX1LwrqVmCnohuYt5n8aTaVlMZV_R1v8LDjFF68fQe3BLyHlg7Dck_nlbpVulcJbdsgGN-bBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn5.telesco.pe/file/DOWXwwy_dW8sAw3K5cvQhIjHRk0-x9meHpkbV4032D3CjL5PNVuVxk0MAunNUOOnbwO9LJ7TCbQAnPaRaHgK855ze-0q7yzJ6o6fTFBzJ-FvLbaQBVrM85y5W8YneEtElLqjsu-bsP-idJLPw79z0YRnY0esrXdGcbLro5VMibNwcVL0OKQ9FknNHog6KuQ0DWbJuDmdTbvLtLvXO1lhqU8YhRMMC9U4S4Qh2nt6d-yHtALxWOVAPxgMH0n5LCu4QHB0U5o7JnWUEbkdJMDL6_NPs2uTcXy-hX1xlmJd4miS3Gy8d69qOI-baIAcFJFvXn4VsDFIG6C9P1pyvwGh_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">راهنمای زنجیر کردن  Psiphon Desktop
با
whiteaesther
Desktop
🔥
🔥
اول Psiphon را وصل کنید.
در تنظیمات Psiphon proxy محلی را پیدا کنید. و یکی از پورت های زیر را وارد کنید . توصیه میشود از ساکس استفاده کنید
SOCKS5:1080
HTTP:8080
WhiteAesther را باز کنید.
بروید به:
Advanced
→
Routes & transports
→
Anti-blocking
در فیلد
Dial through a local proxy
یکی از این‌ها را وارد کنید:
socks5://127.0.0.1:1080
یا:
http://127.0.0.1:8080
بعد
Save profile
را بزنید.
حالا Connect کنید. مسیر  می‌شود:
App traffic -> WhiteAesther local SOCKS -> Aether/WARP -> Psiphon local upstream -> Internet
اگر میخواهید که whiteaesther سیستم شما را تانل کند روی Full tunnel و اگر نه از پراکسی whiteaesther برای نرم افزارهای خاص خودتون استفاده کنید
نکته : قابلیت exit chain را توی تنظیمات خاموش کنید
⚠️
⚠️
تیم وایت
@whitedns</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5080" target="_blank">📅 19:43 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5079">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با npm i -g cline خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/MatinSenPaii/5079" target="_blank">📅 15:16 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5078">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sIH7g2SiNe77rCNTckzViYAilf8d8Z5cz9JWRDrPbWDh4NloICCEdg_6LoDjTz8DtJM2YdGMaQJZ8nBc4atMKlTNZV2BUSpzgcf2U7mrVLZ8zHLY7K6y7r3GBJ-MQsFynpFdWPwtkbZWADq0_Mam2IkEYITSbX2TlWFUAiSIzuPg_YGAgh_Ql7LHiKNFTpQ9SNEc5_h_LEeKbZGXk_Wn5aI3Epu8zkh9i6oZviSCBkmWZnDLGkUTIZ_TIeEhGOGqUW9r7-4yU8BKueCcpn-huH3ZXDrs9GHu7mrvY5ARLfGuN3tF-RKzajlkudSb2yZ7-AwNikS_pXNRFDSLexv12Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه‌ای که GLM 5.3 Flash برد برای تمیز کردن گندکاری‌های اون دوتا، مقابل خود هزینه‌های GLM 5.3 که تقریبا 20 دلار شده بود</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/MatinSenPaii/5078" target="_blank">📅 15:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5077">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">این سیستم Re-Stream همراه با بکاپ استریم رو ابتدا با GPT 5.6 Sol و GLM 5.3 در تلاش بودم که بنویسم
اما چون نسبتا پیچیده بود و تانل هم داشت و سر اینترنت ایران یهو پکت‌ها غیب می‌شدن،
می‌خواستم Claude Opus 5 رو بندازم به جونش
تا اینکه Ox Alpha اومد
دادم و کلی از جاهاش رو کامل کرد، جوری که واقعا Glm و Gpt نتونسته بودن انجامش بدن
و در نهایت هم خودش، اما نسخه ریویل شده‌اش(GLM 5.3 Flash) اومد و کاملش کرد و فرغونی که از Gpt و Glm 5.3 تحویل گرفته بود رو تبدیل کرد به بوگاتی عملا</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/MatinSenPaii/5077" target="_blank">📅 15:08 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5076">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/KVgAb-5lfRcUZ4QWcPqduxy0XrgISoKQ4Q1Ff7346Od4df2_MLLufKmIPTtpT_zbvGfzl-nC3M7-S2_yVw6T2uRA6kKR7zOpIS_4kMy5jX0fqTKTouZLT4afr7vfL-PwpyTPgEq-7d58__3DlGHpjRG0zh0pvk2rPiJUipV9zWD48OZO-xdviDXBdDZr38OnRQVSipqJlatZ6wcFxz2I5Z1i2GvdTTeFs3cb3sjuEx2_fnAXvNFGz1OxoeZQriI1CxnWICJPEm6mxwdtQa45mkx9tsxH7eoRn10EIzEBJxysqVbSymJVjQ1sTbYPGIl0Q5ksv3epO-Bsb4MYarignw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم. دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه  و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/MatinSenPaii/5076" target="_blank">📅 15:05 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5075">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin's Dungeon(᯽マティ️️ン先輩)</strong></div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/N-BIJw1OypA8vyhY-pKXxfdtfX4-1GIA3aBA9AU52NdtaDCwChTXZ2JhWbhlWkWtZexwgV3jtPdd1hVP86C04siBr4qEMH7fPyO4TCZEpof2PEnuGfX2zzNcqVR9nGGmt5agSlyjn0WzuWu-rajPBKeIzvnj4-graaSgJRH-8fxqs1pFf2IyQELa3ZPzsmR6Cw6Suej7IKECqI-klFkmQpU9jqcQDL1wHy8aK73cWgeAQp7D4OjJDA7mYfYaW12ycUndKfKdcZMZFZ-kZlzWhNp3o_IloJ2WmbizLm15Zq_gJEprj7s8LRY0MUfC1x34mV8P57pgekA3QczyY5xqCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که انجام دادم برای استریم‌ها این بودش که اگر نت من قطع شد، کل استریم قطع نشه و برای ۱۲۰ ثانیه روی استریم بمونه تا قبل از اینکه من برگردم.
دیگه نیاز به رفرش ندارید شما و استریم هم تیکه تیکه نمیشه
و در کل به این میگن سیستم Backup Stream</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/MatinSenPaii/5075" target="_blank">📅 14:35 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5074">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/C1sEhe2LMrYThG1NG_HuQ1qM6fhgwvvtJnyb5p03XUlrlp4_eYvIM406w-zMAjDZvcgTzhnMCI_1deXxfFt3DDzKTkqoA3mEiPFXOVkJvxhTWjTdECO4UQ2mhkZj8_w7OTeE2wQpQ7npZromFfZzZ9iuOCz848-YLGCjEaZdzt-BrK3tvhuE9KancLMNrkSdm92-hkRrqmET36cIxTaBbRDv2emhrLj2qlN32ZWjLTTpBWIRpiioXjyMG1w1EtNdRXqYf6Gt9uAx6YmUh7WrOC8NDtWRdrIL2CVP_7WxFAXir0b9piR4exrrGojVLkoLwOmPsMRgepsQyXVi6s3ceA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت
Tencent مدل Hy4-preview رو منتشر کرد
🚀
مدل: Hy4-preview — 770B پارامتر MoE با 49B فعال، کانتکست ۱ میلیون توکنی، لایسنس Apache 2.0
مشخصات کلیدی:
1-مقدار
۷۷۰B پارامتر کل
ولی فقط
۴۹B
برای هر توکن فعال میشه — یعنی قدرت مدل‌های فلگشیپ با هزینه‌ی خیلی کمتر
2- روی بنچمارک
DeepSWE
از ۲۸ (Hy3) رفته روی
۶۴.۳
— تقریباً دو برابر
3- بنچمارک
Terminal-Bench 2.1
: نمره
۸۵.۴
— هم‌تراز GLM-5.3 و Claude Opus
4- بنچمارک
Code Arena WebDev
: رتبه
#5
با ۱۶۳۳ امتیاز — بین مدل‌های متن‌باز
#3
5- ارزیابی داخلی با
۱۶۳ متخصص
: Hy4 با
۲.۹۹/۴
بالاتر از Kimi K3 و GLM-5.3
قیمت API (خیلی رقابتی):
- Input:
$0.83
به ازای هر ۱ میلیون توکن
- Output:
$2.50
- Cached input:
$0.04
اما هنوز، رقابت رو به GLM 5.3 Flash باخته به نظرم</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/MatinSenPaii/5074" target="_blank">📅 13:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5073">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/aR3_CMfISUKCdqmuGm1b4MmLvtw_OqmfMTvO5bwRu3VOgxfAjxsORozkZHMHaDI99XLqZkYaL9EJTfv5GtSZIou2YqC_eEe4Or0J6w1T0pJ-ZuIWhBRHjKqfk3Rq-Cq0dDy-tHczlXbaKH0APAtQJ5HBciAZgdw9QOO226m5AaV2oDdVKiTpGs6iTZ-XBvbjLIAccKuts_68umq-TX_h0ji1bnzEfInMiI8_epknEb1dgvywxzyj5DCHU7wF0LC2rmEn8P6dpnrwp6KXYuT1v8xfUxcPYn9joxRVg9hM3mypDkRp8Qa4wsOxAjcLigZRV-dGtSza1ay_tngdV9SDiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/MatinSenPaii/5073" target="_blank">📅 13:12 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5072">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SG2cOA4J6AEJGhms04BISREG12CWMB2AVvg_llgH0_VQs3qWiFAMi6DsDFU5lfOOMvOx0AbE1ZyXmCOWPohksgszblLG-cQOzZMYeqN6y7ZsVq-RpluB6YYf27qe73keTeWsuBxEz2Vrxmq41Evqbd7D2IsschRd5qNeSUY2h3bmxMj3ixWGbt2eLZtyYx_6TP_JMLE9Gzh8-v8kuSGOa2cw-G2dImte2mUOd0pqBcR8HrpQfPG5iz2oSNXXyR6aQMWgE7czxkkASmy-s_T0pgghu1NOZrdHHWFkA2XuvCfxUluYEMSyB7H3z8GbV83DBUlP84JBOSvxKoomqJbXXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل ۱۲۵ میلیاردی Qwen 3.8 Flash Next در بنچمارک Agentic Index با ثبت امتیاز ۵۶، توانست Kimi K3 Max را پشت سر بگذارد و با یک قدم فاصله درست پشت سر Claude Fable 5 قرار بگیرد؛ اما نکته شگفت‌انگیز عملکرد آن نیست، نحوه اجرای آن است:
• سرعت: ۲۱ توکن بر ثانیه
• پنجره زمینه: ۲۵۰ هزار توکن
• سخت‌افزار: فقط یک کارت گرافیک RTX 4090 و ۱۰۰ گیگابایت رم اقتصادی DDR4
مدلی با این ابعاد تا همین دیروز به کلاسترهای گران‌قیمت نیاز داشت، اما امروز به‌صورت کاملاً محلی روی یک سیستم دسکتاپ اجرا می‌شود. مرز بین مدل‌های ابری و اجرای لوکال عملاً از بین رفت.
✍️
callitVer1</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/MatinSenPaii/5072" target="_blank">📅 12:03 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5071">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLinuxor ?</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=IexlkG759TjRSACVYzB26yY9cpeXqBJk0m1-FC92SmN_KxhcKbaE01QaweJPIY7bEZWERtewR6XQnZp7_iVr4-czs4PuWyw6ug10hcNuxUKedBReaWAlxZDBOySc6bmPq2Dc-HyZlmgxgVKV7mVSkmG82IUBMFVr6zfIzCFFg8eQHlsJ-vEtGk1i0L-VUCVeve2ytpPG95oVeguNYkQLx4uf5bVnGqAHX3qIIhhsQZQsX0MORbzLLxIpseqnjuG_A0Z1kcvCHcrOSQRIHus6OIEIyXdQ8p4IckSAhV_MUSg629Tizu7Q8yeOwBZCFY91tknOe6vKuAWci6XLp-3xRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a2386a8b3.mp4?token=IexlkG759TjRSACVYzB26yY9cpeXqBJk0m1-FC92SmN_KxhcKbaE01QaweJPIY7bEZWERtewR6XQnZp7_iVr4-czs4PuWyw6ug10hcNuxUKedBReaWAlxZDBOySc6bmPq2Dc-HyZlmgxgVKV7mVSkmG82IUBMFVr6zfIzCFFg8eQHlsJ-vEtGk1i0L-VUCVeve2ytpPG95oVeguNYkQLx4uf5bVnGqAHX3qIIhhsQZQsX0MORbzLLxIpseqnjuG_A0Z1kcvCHcrOSQRIHus6OIEIyXdQ8p4IckSAhV_MUSg629Tizu7Q8yeOwBZCFY91tknOe6vKuAWci6XLp-3xRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این لودینگ ها هم جدیدن و خلاقانه خوبیش اینه که SVG هستن و توی سایت و اپلیکیشن و هرجایی می‌تونید ازش استفاده کنید:
circleloaders.dominikakissi.com
@Linuxor</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/MatinSenPaii/5071" target="_blank">📅 18:25 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5070">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AhNGaRuPbCp9wncEHhFxyz2nGlqcsYE68LE2Gs-OPkFwPxNwNm0Rck1I08LlIPHNhvAeZ61ciHe59JQYJS2YSVNObCkn7asoiCB85-7v5UfmTA4eKF5cgB6ss0oXZKcEXrZQbRnxUgXge4IpnX10GR7SNytbMXGtjVlMQ86PLqG7i72weVH6pw_3iRY54JjNXfB_UpXpuOPj9XksoOqsbXsstxp4uSZjufRj6HcaP5XQNefCQ1XOowR0JM-xlw87lPzf0rt1rAQsmZhrRu4ILxkVIbS4Q6YAnbRuvgBNWIkcBTHF3anVcb4Fhd1vAvh6tRRf2Kddc3VEaOVjjS32_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچقدر از هوشمندیش هم بگم کم گفتم</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/MatinSenPaii/5070" target="_blank">📅 13:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5069">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HN8tzLyXGcJcu4BSWUKORvSG1FBc6Bo1r1OARNvKzd9zYat5qiRmp8ewWdglXeGMuP9vM11nQc5AUof9J4re002yw5rpLfkkTHQZRA8Ix8iv26AzQXTnqIjzuipcRL0N8JhNeiltgJqnnJyFnCBpQQBzIyaUXBBBMO2cW2oaLrnjdcc6h-R-5KjGPm8fzfXfNImHb4N23pEAmWv2LaxwDw2q_OLSUmFUnTAU2i9z5GSFA6BwXRKW-3JCvXeXClGu_zKT9yYiYhKo0hsxPJT6vXzbahyGtMIwQPSnHPxuYPQHhF-gGqFBnkO18xKzGQdgmN_A8N9skaLV7WW7WNTlxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نرخ Input Cache اش خارق‌العادست
روی خود هارنس OpenCode</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/MatinSenPaii/5069" target="_blank">📅 13:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5068">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/O2qJ0YPwvcof8RBq-J4SntrZPWQ_dtcSeS_pVGWwpxsfcAhCJpJHbXxlPBoih1CUiJ_mPHyKKTNgz65OzOMAGlXuw2rTsvh202ml_0z3uYus1963Hh1yzMGT4vUzqn6utA7sMSYlOovQE8n1sUYHOxnWk8U359Ncd6md5EiwljXht2sB8yDoh1eGaEC4ZE4zao0QmdVo0jOMPJxiZJJrO-5TAw04ipY38DJW0N4aXf_C3vAJeBQv1PPOAZZjF6NcEuNGZPqJY9VJRuiXX-c6ul3mNANhQzpxBqR55sFWfg3JNsAUHG4bwNzXUIKY8ywW_Xs1NjWnjlvvtcFu5p_vYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصرفش خییییییییییییلی نسبت به GLM 5.3 اوکی تره
و راجب هوشمند بودنش هم که دیگه یه ویدئو کامل دادم نیازی نیست بیشتر صحبت کنم. باز ما میگیم درود بر مدل‌های چینی به یه سریا بر میخوره</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/MatinSenPaii/5068" target="_blank">📅 13:45 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5067">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwzua_eVsyyH7QrTi159e5trJaOl_a5IWfQpzNiIzSR-eiwNJezSRDRrTtLXN3OHr0-bBwDMbO9akczbu7moswo7CdTx4pBeJFmANXhb75Ecp2pDZE4qLhg5yl9NU5ByxHRtQ-9KMe1f-PSAPQlBGIYrMaQ_PLhkOJJEkPpPPbAPmurv99BNo6bHLxuMEkCaNz9WDurdOy-_fKziDu0AfobR8K1KfBmsDrtlkXsSJIJ0IE40FELMCLKzMF5DUbpHBnKDZU5mAHc8s6Op6PiMeFHoICs5IA00qcHXjF2oYag-7C_Z5OG8W1vT2Joszdpr0ozA9z1SaapE8Z92-CGOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/MatinSenPaii/5067" target="_blank">📅 13:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5066">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خیلی درد داشت که Ox Alpha رو عوض کردم روی GLM 5.3 Flash و الان دارم واسش پول میدم روی OpenCode Go
😭</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/MatinSenPaii/5066" target="_blank">📅 13:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5065">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/MatinSenPaii/5065" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5064">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/gRA2cW_5710ZDRNTLatKxwmoPDO3KFfXCo80S44XlxW_GAbDg5L_uyPaqzhq2qzytC9LUl3Wuv2NvvwO8Jvks23q0NIbaHW4KegGGOZJ-VKbmCJB-kjkpiZPqugYvImVGDP_xa4GakDqS_Txag1P3Ux-u1oCN4ltoEZXdK_qEz536uMpORwFqsdZo7ObSCpaJoQGX-an0xS3zpu-YiWxsK7cbYHeZvqXqatOAkNURC28oPiOR1wgfZHAapj43Ai7vWIOyz7uRBIPJMXNPU3OLpyrThBN-6ozep09VR1gVMzsMs4wrm_Naf9WbyawGfHgkcLl4pEdYg1BNkQrz6pmXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل GLM 5.3 Flash یا همون Ox Alpha، به صورت رایگان روی Cline قرار داره. Cline هم اکستنشن Vs Code داره هم می‌تونید با
npm i -g cline
خودش رو نصب کنید
✉️
t.me/MatinSenPaii</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/MatinSenPaii/5064" target="_blank">📅 02:26 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5063">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qfQ9Ur6Di29665y6YQ4yauhVGg_9qiSOAphPClIzH2jiH6-6UmmyRuAcldXfWI-StLMdmbQpLL68EMm0hheIRHo1aRSnZBA_RishEqmonNjsEnu2k3ePKGVbkLQriPoLP_rp9HJ6iC-0eqmBADOvU4HhzA391RQqMtrrXoYP4aOzxuSK-wp1_tu1kY6q9iLrU-xTcN7qCbTd7FUtxWswytVU8Xyal2Sdi6uP5tgdGddsjNmYTrTVSbHFo5CvjwuBSzvUrRL0wyc63loxm5ZaFGyqN19gf9vsaCS0X6Ti-B7i8huGm6_MO0Sk6-6ZOxOBCl-CUKRWLT3rIW7Pu7atvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/MatinSenPaii/5063" target="_blank">📅 21:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5062">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">توی این بنچمارکا همه‌اش GLM 5.3-Flash رو با GLM 5.2 مقایسه میکنن
سؤالم اینه که چرا با خود GLM 5.3 مقایسه نمی‌کنن؟</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/MatinSenPaii/5062" target="_blank">📅 21:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5058">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hBekT_nSzgT5EIQfnyank7lZ_cUdwF3mIn_dLAJkV_mcYYiqepQyNQLyX5wsTAgK0iSuZcmlH0QPIxoelT6zOIFVwAoePyKarZfwCNejKacW0Ut9cYdlBaXpJ_N0AQYTuektuyIKoM7OSYZP-H19x56teGCi0napFoZyB4e4FJGvSlTY9VkkmWg47P4gZ5343TsRpk0pWSTcazgI_k_VHCw59j2sI3OROtxkqP0hH6MAowhBuO_BKQqfNuJW-rZmnBINmWIputwr20ezE5HeF0UCTn3udtCAeyH3cakWLuiAuV1KnwS_lJBkTrzJLZlY496azOF8dIxVzdps3SD2YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W6YWaligCrU8rRNKQNg9qvKxZ0XIpW_smuOVWBYF1MggKl7jPOyB3EBsSqJD8fjjw3JkzXVswRC0BMFYkRxYSvtCg6jMW7JGAAjS4sOLrBSHM07Yo8Cf4DzCN77WbKVenVdxlcNPKLZFWAbUzTiQlzbHAAJxT80dq77_OY_1WOycvzqC9XTnt-Fh8g-BaWNLozUEISrImgTTFpX_5pqTk4sGQYcAWOSAdinZR8KGSjcF-UDw5vOrsscNLem1QtdLUH-DFVnn1NKwdv5BGi4Gmpzaept-aCO8lA9DOG-0oMq_FVfyTGkWFA1P3wFqZFKXGqJVFyzp0Gl7l2quBhyYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eRLZyGaPzrPn-gpfxdFBIbkBghidMBLUASREHTl0cBY6ujYulSTGEj2WJEcUNgFRuhMOlKgPmFNAHWv96CoUFhaaCDxT3z6lNk1rSyHVPLhiXNLrU9VHlE-j9cFotdFaG5zdVB3PjaEqb5MEhygJegr3bVH3H7gobJuDkRWzCEfo_taAX3vhCBwg5aR6kVPg7XasTfzlBGZbhtOkiY8T6UeGpKjJjIROhznsCxOMrFlVy8gK2hvTsWeb0KSQWUcIMdHwQBuLZ4nUESL0BXXLkNL3nr590QkAy1fGAGottv8kmL69KItYfae2j9woqiA1FrMc_HSts04Zyo4ihpuzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tJYALUsvhHQ59baSJT0QLDljFhxKBRAcgkUYS_pqbN-3Y6x6u0kbhHLDCc2iOpuUJ6oLQO8R59_CO_u4uL9vRzCUjLFiXGPtf7Lfh7DuIsWU0Nnr0yOlLAZHnuj6BQCVYww_pn-5d25o8cdRL_FttB3OTRoi0_3hrHC_8_2lX0CC-BH8zDniDWJxfzQ5gkZQCe_KmmyQ6rlrVlR-RGRXazZeUKKPTlXPLdac-ESB-Ni8sp2p6C_r_KRPsmsT2vapQkTWNIxPI2BtWkXyg7FH4m_hbENH0m6LZXx1g7kQQvWv5xvKcAG6SmTrw6rtICY7aB6pzvmK5YmBUN5_lQebqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معرفی GLM-5.3-Flash و ماجرای Ox Alpha
شرکت چینی
Z.ai
بالاخره مدل GLM-5.3-Flash را رسماً معرفی کرد؛ مدلی با ۳۲۰ میلیارد پارامتر (معماری ۳۲۰B-A18B)، لایسنس کاملا متن‌باز MIT، کانتکست یک میلیون توکنی و قابلیت چندوجهی (multimodal)، که به‌طور کامل روی تراشه‌های هوش مصنوعی داخلی چین اجرا می‌شود.
نکته جالب ماجرا، پیشینه‌ی این مدل است. حدود یک هفته قبل از رونمایی رسمی، یک مدل ناشناس با نام Ox Alpha به‌صورت رایگان روی پلتفرم‌هایی مثل OpenRouter ظاهر شد و به‌سرعت بین توسعه‌دهندگان وایرال شد؛ در عرض چند روز، حجم مصرف توکن آن به رقم نجومی ۴۲ تریلیون توکن در شش روز رسید و صدر جدول‌های استفاده را قبضه کرد. جامعه‌ی فنی با تحلیل نشانه‌های تکنیکال (مثل نوع توکنایزر و کدهای خطای مشخص API) به این نتیجه رسیدند که Ox Alpha احتمالاً نسخه‌ی آزمایشی همین مدل GLM است، تا اینکه بلومبرگ گزارش داد
Z.ai
این حدس را تأیید کرده و وعده‌ی انتشار رسمی وزن‌های مدل را داد. جالب است که Ox Alpha پنجمین مدل ناشناسی بود که طی شش ماه اخیر همین الگو را تکرار کرد (قبلاً Pony Alpha از GLM-5 و Hunter Alpha از Xiaomi هم به همین شکل رونمایی شده بودند).
از نظر قیمت، GLM-5.3-Flash بسیار رقابتی است: ۰.۱۵ دلار برای هر یک‌میلیون توکن ورودی، ۰.۵۰ دلار برای خروجی و ۰.۰۳ دلار برای ورودی کش‌شده. روی بنچمارک کدنویسی واقعی (Code Bench) در همه‌ی سطوح تلاش از نسخه‌ی قبلی (GLM-5.2) بهتر عمل کرده و با Claude Opus 4.8 برابری می‌کند!
از نظر معماری هم ترکیبی از MoE، Sparse Attention، Linear Attention و لایه MTP به‌کار رفته که باعث شده حافظه KV-Cache به ازای هر لایه حدود ۴.۴۴ برابر و محاسبات attention به ازای هر توکن حدود ۳ برابر کاهش پیدا کند؛
خلاصه: هوش وحشتناک بیشتر با محاسبات بسیار کمتر.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/MatinSenPaii/5058" target="_blank">📅 18:54 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5055">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/gMzDfzyD-GcVCWOIeB3b9VKkpmyv6qs-UPLqujs_JO1t4875pg76XpAklX9eei90zqxil6CwdbeQ8-LbENrbG4k7xoWPXUnG95a6JI-4xdvZGOXvpaMfhkGL4BAKsKTjWq0BAt3ZB0GntepqLM8iyaNa0S5iuf5gE2BdPVpwtP6ZX6qQuVPYnmZahAS3TkhjjMY61uztNM5NmCKvKWCGGKlAByhSIXFY1wLfaWVAHjQcOVEWGCguiBvhAoA85Wp7E9ihQc1v2uPmGieNxmS8BTPZqum6LVvaWOWwxHLMcRP690EOPeUMFflc0Nd0CEOf1H28a1Q2pcAhdzMrzLF6sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aykB77orZIcv9zUBkjxqQxwoEGiutiG9S1dalFhQrjEs4WQWll8Th3X9FH6eYeF4udG2Jdwzr8yw7jRgoRRRIAWv35e_j8XjJIG2AU4WAoyGIhlsNI54w8G_2k_sQ7i9RTvJPC_SCigFsZo58VekZhNz34f6uvQISL285SvJJ0dh5Vhrmad5I5hQ-ajz7J7j3l_B7opY1p-woTkww-1RnASx0XTYH6Tf7X1-aL9yc5wQHQaBH7JsIzs1ItY7tiTnckEVHckuxSWR-ONhSyu5y_riWx4EIEPi-tTPw1V_eEQe7R8RsSm4lcaA4z-Y9KCz996ILRkFpLUr1wMCq2NgkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/UZW_1rxCiWDKiu2h1dYB2hVwSYvDqlO99RBvoyIXgPEgTmofT_UuJozZti8QBOqtuxga-hJHcKP67AGiwZTAwP5Y5LgrygHWyKaFwHOSPImWF_lQipiyD73t6HY5i5SOKyp-OnTWc6Z7nMg0HzcjQYQ6OrSxJn3GFuD2Yvhjcl8T00uBo2in0C5D_l-gVvt_i48J8d-tj0xeOPzNyQ1O2OwjOHw2FlXEqXf-uDG1g9uTKZVBvcmjSKj8kCTSC8YaUJCGXSbnH5KurwoKeG3Gv6SDsC0md73jl8VLlvBdZPT9xZDTGyyvWChFhlJ_-QqofYxg1zk9sFPeqaTg-heA6Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">باورم نمیشه
running Entirely on Chinese AI Chips
😐</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/MatinSenPaii/5055" target="_blank">📅 18:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5054">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خبر:
مدل Ox Alpha در واقع GLM 5.3 Flaah بود و گویا حدس همه درست بود و جمنای نبود
🥲
اما....
مگه میشهههههه
مدل فلش از مدل اصلی انقدر قوی‌تر
😭
😭
برم تحقیق کنم ببینم چی شد این دو ساعت که خواب بودم</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/MatinSenPaii/5054" target="_blank">📅 18:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5053">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/J49V-xhhbhcEb8pwLHTmtIl0OHsIavHPND-qsR16t_7wOEKjkgQhFyLkKsdwPLQc7Wrw8EehroiwFLpwsbQ_9LJyDtOov7WDPuFr-lQflL38z-oj6OYhvP6QiHmGy1sxBAN-1mw_tGDkkRZctGJCAnMQavwd0LtyAVLTzKieui8349xBMcSKwKnyhYZFxMMWGrpi6xe8Oyki8Wu_QcBRXGo-Rd9PekvWER_AQnVuQ16Z_m29M48rxqqjybJR2uGFi7jbtv0Do0OMY4HpHai_A4xjX4yGuvPaDZot2APJ-acbme8V_7l6z3KEVfXeh6y67F43Rjp9mZPEB1HYwZl6lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دو ساعت خوابیدما
😂
😂
😂</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/MatinSenPaii/5053" target="_blank">📅 18:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5052">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🐂
چالش Ox Alpha با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.  هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha: https://youtu.be/FIhoccZtpZQ  برای شرکت در چالش: 1-…</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/MatinSenPaii/5052" target="_blank">📅 10:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5051">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/BN0vsj83NLL8Hj3Qm3UY881b_7j7caA64cYKW6Yl6wPpLzac6SF5rJagYncHDAulE5BmA6R5BRPlj4E67sCM_NgA957T-9ZGbddBGeA6hLP9K9UC0tOrrcKxXqWRc99wpm6if1NoUouT3CVx3y1gshDehuXNXjHofvUurHv4MX4qylWJowGOYU4vZUzqe3dlPOd9t5MpbN08CCA0zAoxxt6nVLSjQfOr-lCeKfz3i54CXLvnrcT8X81Sjg8AuaNxHcckXrt9XwPD-zxQXLEVQBTYHeboIHrmf_kYIpBkjFrLrLdhS5BRqXVQ7DJpwhjs5Gar7qB10bnVP_9ZErTPLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐂
چالش Ox Alpha
با Ox Alpha یه ابزار بسازید که یکی از مشکلات واقعی زندگی روزمره‌ی مردم رو حل کنه.
هرچی ایده خلاقانه‌تر و ابزار کاربردی‌تر باشه، شانس بردنتون بیشتره
👀
📹
آموزش استفاده رایگان از Ox Alpha:
https://youtu.be/FIhoccZtpZQ
برای شرکت در چالش:
1- ابزار یا پروژه‌ای که ساختید رو همراه با یه توضیح کوتاه و ترجیحاً عکس/ویدئو ازش توییت کنید.
2- من رو توی توییت تگ کنید:
@MatinSenPai
3- عضو کانال اسپانسر چالش، Lira Candles باشید:
https://t.me/liracandles
من پروژه‌هایی که برام جالب باشن رو ری‌توییت می‌کنم و در نهایت از بین شرکت‌کننده‌ها ۵ پروژه برتر رو انتخاب می‌کنم.
🔥
🎁
جایزه هرکدوم از ۵ برنده: یک
شمع صدف
و
توت‌فرنگی
از Lira
🕯️
🍓
معیار انتخابم بیشتر روی خلاقیت ایده، کاربردی بودن و کیفیت چیزی که با Ox Alpha ساختید خواهد بود.
تا فردا همین ساعت می‌تونید توی چالش شرکت کنید! چون احتمالا آخرین مهلت استفاده‌ی رایگان از مدل Ox Alpha خواهد بود طبق گفته‌ی OpenCode</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/MatinSenPaii/5051" target="_blank">📅 05:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-5050">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">به زودی آموزش ویدئویی این ویزا کارت مجازی و روش گرفتن آفرهای رایگان و اینکه چطوری وصلش کنید به Google Pay و... رو می‌ذارم
🎨</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/MatinSenPaii/5050" target="_blank">📅 01:29 · 04 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
